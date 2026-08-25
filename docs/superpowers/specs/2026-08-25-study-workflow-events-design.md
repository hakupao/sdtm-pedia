# study 轨 workflow 事件层 — 设计 (spec)

> 建立: 2026-08-25 · 轨: study (st01) · 性质: **确定性 xlsx 解析, 零有损转换, 零 LLM**
> 上游判决: `sdtm-rag/evidence/checkpoints/c2_pre_survey.md` §8 (Plan C 两份 PDF 均判 DROP)
> 用户裁定 2026-08-25: 范围 = **事件表可查 + OID 双向打通**; 形状 = **四步全做**
> 红线: 一切进 git 的内容零真名; 研究一律代号 `st01`; 本 spec 只出列名/计数, 不出取值

## 1. 背景 (为什么不是 Plan C)

Plan C 原设想「protocol/aCRF PDF → markdown 有损入库」。C2-pre 勘察实测判否:
两份 PDF (933 / 212 页) 相对**源数据**零增量。**根因不是 PDF 没内容, 是 ConfigReport
7 个 sheet 中有 3 个从未被任何管线解析**:

| sheet | 表头行 (0-based) | 数据行 (滤脚注后) | 关键列 |
|---|---|---|---|
| `Study workflow-Events` | 2 | **14** | `Study event ID` / `Event name` / `Event type` / `Visibility condition` / **Scheduling: Days·After·Reference·-days·+days·Enable recurrence·No of times** |
| `Study workflow-Activities` | 2 | **77** | `Study event ID` / `Activity ID` / `Activity name` / `Activity description` / `Visibility condition` / `At time`·`-hours`·`+hours` |
| `Study workflow-Forms` | **1** | **110** | `Event ID` / `Activity ID` / `Form ID` / **`Repeating`** / `Item visibility` / **`Hidden items`** |

⚠ **三个 sheet 的表头行号不同, 且底部有说明性脚注行** (ID 列含空格或以句点结尾)。
解析器**必须自适应表头 + 过滤脚注**, 不许写死行号 —— 本 spec 作者第一次读就因写死行号而读错。

## 2. 目标与范围

### In scope

1. **事件层入 catalog**: 三个 sheet → `events` / `activities` / `assignments` 三池
2. **OID ↔ 人类可读名打通**: 事件/活动 OID 与名称双向可查。⚠ 2026-08-26 Task 6 收口
   补注: 实现是 `resolve_events(query) -> list[str]`, **输出恒为目标标识符**
   (`event:{oid}`/`activity:{event_oid}/{oid}`/`assignment:...`), **不直接返回人类
   可读名字符串**——"双向可查"指 OID 与名称**均可作为查询输入**命中同一目标, 不是
   "调用后能拿到对方的可读名"。措辞比交付宽半格, 非虚假声称, 但可能让人以为能拿到名字,
   记录以防误读。
3. **item 真实采集范围 (核心推导)**:
   ```
   item 的采集范围 = (该 item 所属 form 被分配到的 (event, activity) 集合)
                    − (该 item 的 Hidden in activity 集合)
   ```
   ⚠ 2026-08-26 S3 触发, 用户裁定退回卡片渲染 (详见 §6 S3 / §7 任务1); 本条改由
   catalog 三池 + `resolve_events` 交付, 不再进卡片正文。
4. **修一处生产缺陷**: 卡片 `- 適用範囲:` 行实为 `Visibility::Hidden in activity` (语义相反)
5. **event 侧 gold 题集** (尺子先于接线)
6. **接 `study_lookup` 确定性直查**

### Out of scope (明确不做)

- 任何 PDF 解析 (Plan C 已判 DROP)
- SDTM TA/TE/TV/SV 映射建议 (用户 2026-08-25 明确排除; 属未验证价值层, 不捆进数据单元)
- 事件层进向量库切 chunk (增量是关系型, 走确定性通道)
- 任何 LLM 调用

## 3. 数据模型

`catalog.json` 新增三池 (与现有 `forms`/`items`/`codelists` 平级, **同源同 xlsx**):

- `events[]`: 事件 OID / 名称 / 类型 / 可见性条件 / 调度窗口 (Days·After·Reference·±days·recurrence)
- `activities[]`: 活动 OID / 所属事件 OID / 名称 / 描述 / 可见性条件 / 时刻窗口
- `assignments[]`: (事件 OID, 活动 OID, 表单 OID, Repeating, Item visibility, Hidden items)

`ledger` 同步扩展到这三个 sheet (现覆盖 `Forms`/`Items and Groups`/`Code lists` 三表)。

**不新建独立文件**: 三个 sheet 与现有三个 sheet 在**同一个 xlsx**, 由**同一个** `build_catalog.py`
读出, 放进同一个 `catalog.json` 才符合「catalog = ConfigReport 的结构化」这个既有不变量。

## 4. 已实测的事实 (设计据此成立, 复跑可验)

| # | 事实 | 实测值 |
|---|---|---|
| F1 | `Forms.FormID ⊆ catalog.forms` | **True**, 21/21 全部 form 均被分配 |
| F2 | items 的 hidden-activity ⊆ `Activities.ActivityID` | **True**, 61 ⊆ 77, 缺 0 |
| F3 | `Forms.Hidden items` 与 items 的 `Hidden in activity` **互为精确转置** | **61/61 逐键集合完全相同** |
| F4 | `Repeating` 取值分布 (滤脚注后) | `0`×106 + `Unlimited`×4 = **110** (滤前 112 行另有 `None`×2, 正是那 2 行脚注 — 可作脚注判据的旁证) |
| F5 | `Event type` 分布 | `<EVENT_TYPE_A>`×13 + `<EVENT_TYPE_B>`×1 = 14 (A=常规访视类, B=试验开始类) |

**F3 是本设计最强的一条**: xlsx 内两处独立表示完全一致 ⇒ join 可确定性完成, 且**语义确认为
hide-list** (Forms 侧列名直接叫 `Hidden items`), 从而坐实 §2.4 的缺陷判定。

## 5. 硬验收条件 (判据先于实现, 全部写死在此)

### A. 交叉核对闸 (与 PDF 封面摘要独立比对, 4 条全绿才算解析对)

PDF 封面的设计摘要给出 4 个数字, 必须由 xlsx 解析结果**完全复现**:

| 断言 | 期望 |
|---|---|
| `len(assignments)` | **110** |
| `len({a.form_oid for a in assignments})` | **21** |
| `<EVENT_TYPE_A>` 下的分配数 | **109** |
| `<EVENT_TYPE_B>` 下的分配数 | **1** |

(实测已 4/4 吻合, 见 §4; 本闸把它固化成回归断言。)

### B. 引用完整性闸
`Activities.EventID ⊆ Events.ID` · `Forms.EventID ⊆ Events.ID` · `Forms.ActivityID ⊆ Activities.ID`
· `Forms.FormID ⊆ catalog.forms` —— 四条全 True (滤脚注后)。

### C. 转置一致性闸
从 `assignments.Hidden items` 重建的 (activity → item 集合) 必须与从 `items.Hidden in activity`
重建的**逐键完全相同** (期望 61/61)。**这是解析正确性的独立参照物, 在解析器之外。**

### D. 卡片侧回归闸 (改动面最大的一环)
§2.4 的缺陷修复 + §2.3 的采集范围会让 **961 张卡片重新渲染** ⇒ 必须:
1. 重渲染前后逐卡 diff, **只允许 `適用範囲` 行与新增采集范围行发生变化**, 其余行逐字节相同;
2. study golden v2 (48 题) 重跑 **逐题 Δ0** (S2 开, 基线 87.50%);
3. 重灌索引后卡片侧检索三遍协议逐题稳定。

⚠ 2026-08-26 S3 触发, 用户裁定退回卡片渲染: **第 1 条的判据已无对象**——采集范围行
从未进入生产卡片正文 (`build_field_cards.py` 恒传 `assignments=None`), 故"逐卡 diff
只允许两行变化"这条断言实际上是"逐卡 diff 应为 0 变化" (只有 §2.4 的语义修复那次
真实渲染过, 且已完成)。第 2/3 条仍然有效并已复测 (87.50% 逐题 Δ0, sha256 961/961
不回归), 判据落在 `evidence/checkpoints/study_workflow_events.md` §1 闸 D。

### E. 尺子先于接线 (硬顺序, 不许跳)
event 侧 gold 题集**必须在**接 `study_lookup` **之前**建成并冻结。
`c2_pre_survey.md` §7-4 那 10 道候选可作起点, 但**须逐题重新裁定** —— 它们当初的判据是
「961 张卡片答不出」, 现在语义已变成「workflow 三表能不能答出」。

## 6. 自毁条款

- **S1**: §5.A 四条交叉核对任一不吻合 ⇒ **停**, 先查解析器, 不许调整期望值迁就实现。
- **S2**: §5.C 转置一致性 < 61/61 ⇒ **停**。两处独立表示不一致意味着我对语义的理解有错,
  此时**不许**继续 §2.3 的采集范围推导 (它整个建立在该语义之上)。
- **S3**: §5.D 卡片侧出现**任何**非预期行变化, 或 study golden v2 出现**任何**逐题回归 ⇒
  **退回**卡片改动, 事件层入 catalog 但不改卡片渲染。
- **S4**: 若 event 侧 gold 题集建成后实测 **doc/卡片侧已能答出 ≥8/10** ⇒ 本单元价值不成立,
  只保留 §2.4 的缺陷修复, 其余退回。

## 7. 任务分解 (四步, 顺序是硬的)

| # | 任务 | 产出 | 闸 |
|---|---|---|---|
| 1 | 修 `適用範囲` 语义反转 | `build_field_cards.py` 改标签 + 961 卡重渲染 | §5.D |
| 2 | 三表解析进 catalog | `build_catalog.py` + 新增三池 + ledger 扩展 | §5.A/B/C |
| 3 | event 侧 gold 题集 | 题集 yml + lint 闸 (复用 `eval/lint_gold.py` 口径) | §5.E |
| 4 | 接 `study_lookup` 直查 + 实测 | 事件查询通道 + 逐题实测 | §5.D2 + 规则 D 三方 |

## 8. 红线与纪律

- 进 git 的一切内容**零真名**: 本 spec、题集、证据、报告只出列名/OID 形态/计数, 不出取值
- 题面若含真实 form/field OID / label, **只允许**存在于 `sdtm-rag/data/study/` (gitignored)
- 红线检查**必须程序化** (与 `catalog.json` 比对, 双向扫描), 不许「我觉得这个不算」
- 规则 D: writer / reviewer 走不同 `subagent_type`, 不许同 context 自审
- 规则 B: 任何失败 attempt 归档 `evidence/failures/`, 不删

## 9. 已知风险

1. **改动面**: §7 任务 1+2 触及 961 张卡片与索引重灌, 是本单元唯一的回归风险源。
   §5.D 三条闸与 §6.S3 退回条款为此而设。
2. **`Event type` 等列含日文取值**, 属研究专有内容 ⇒ 解析产物进 `data/study/` (gitignored),
   **进 git 的只有代码与计数**。
3. **脚注行判据是启发式** (ID 列含空格或以句点结尾)。它当前实测有效 (14/77/110 三个数与
   §5.A 全部吻合), 但**换研究/换 ConfigReport 版本可能失效** ⇒ 须配显式断言, 且
   §5.A 的四条闸就是它的看守。
4. **`c2_pre_survey.md` 本身的规则 D 审查方未派** (spike 性质), 其 DROP 判决未经独立复核。
   本单元不依赖该判决的强度 —— 本单元的立足点是 §4 的 F1-F5 实测, 与 PDF 无关。
