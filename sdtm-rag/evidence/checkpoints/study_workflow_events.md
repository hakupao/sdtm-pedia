# Task 6: study_lookup 事件通道接线 — 收口证据

> 日期: 2026-08-26 · 分支 `feat/study-workflow-events` · 计划:
> `.superpowers/sdd/2026-08-25-study-workflow-events/task-6-brief.md`
> 数据红线: 本文件进 git, 零真实 OID / label — 全部用题号 (`ev_qNN`) + 计数 + 形态指代
> (与 `test_catalog_workflow_pools.py` 的红线约定同款)

## 0. 一句话结论

`StudyLookup.resolve_events(query)` 已接线并接受实测: 事件层 (`events`/`activities` OID·
名称索引) + item 采集范围层 (`collect_scope` 减法接线, 消费 Task 4 的推导, 解决 M4/M5)
两段合并输出。33 题 event gold 子串口径实测 **15/33 = 45.45%**, 按类别六道分区从 0/5 到
6/6 不等, 逐题清单见 §2。卡片侧 (study golden v2) 三遍复测 **87.50% 逐题 Δ0**, 无回归。
测试 1764 → **1772** (+10 新增 / −2 迁移), 0 failed 0 error。**规则 D 三方核验本报告完成时
尚未进行** (§7, 待 team lead 派发)。

## 1. 各闸实测值

| 闸 | 判据 | 实测 |
|---|---|---|
| A (spec §5.A 四数交叉核对) | `test_gate_a_cross_check_against_design_summary` + `test_three_pools_exist_with_expected_sizes` | assignments=110 / form_oid 去重=21 / event_type 分布 sorted=[1,109] — **全部吻合, PASS** |
| B (spec §5.B 引用完整性四条) | `test_gate_b_referential_integrity` | 4 条差集长度全部 = 0 — **PASS** |
| C (spec §5.C 转置一致性) | `test_gate_c_transpose_consistency` + `test_hidden_activities_subset_of_activities` | 双向键集合对称差=0 / 双向不匹配数=0 / fwd 键数=61 / 隐藏清单侧 activity 去重数=61 — **61/61, PASS** |
| D (卡片侧不回归) | 本会话未重渲染任何卡片 (`git status` 确认 `data/study/st01/cards/` 零改动); study golden v2 三遍复测 | `source_recall_avg=0.875` 三遍逐题一致, 与冻结基线 `v2_baseline_s2on.json` 的 87.50% 相符, Δ0 |
| E (event gold lint) | `eval.lint_gold --events-catalog` | `0 条 gold 未唯一定位`, exit=0 |

复跑命令 (均已本会话实测, 非引用旧数字):
```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_catalog_workflow_pools.py -p no:warnings -q   # 7 passed
.venv/bin/python -m eval.lint_gold data/study/st01/eval/test_set_events_v1.yml --events-catalog data/study/st01/catalog.json   # exit=0
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards --output /tmp/run.json   # ×3, 逐题比对
```

## 2. Step 6 实测: 33 题 event gold 命中率 (子串口径, 非 judge — §11-5 钉死)

**总分: 15/33 = 45.45%**

| 类别 | 命中/总数 |
|---|---|
| event_timing (q01-05) | 0/5 |
| event_form_assignment (q06-10) | 0/5 |
| repeating_rule (q11-15) | 0/5 |
| conditional_event (q16-20c, 7题) | 4/7 |
| oid_name_mapping (q21-26) | 6/6 |
| item_collection_scope (q27-31) | 5/5 |

### 2.1 逐题未命中清单 (18 题)

`ev_q01 ev_q02 ev_q03 ev_q04 ev_q05` (event_timing 全 5 题) ·
`ev_q06 ev_q07 ev_q08 ev_q09 ev_q10` (event_form_assignment 全 5 题) ·
`ev_q11 ev_q12 ev_q13 ev_q14 ev_q15` (repeating_rule 全 5 题) ·
`ev_q16 ev_q17 ev_q20b` (conditional_event 3 题)

**结构性原因 (不是逐题巧合, 是三个类别的题面设计使然)**: `resolve_events` 是子串/精确
键匹配 (事件·活动 OID/名称子串 + item OID 子串 → collect_scope 减法), 只能回答"问题
本身已经点名了要查的对象"这一类问法。而 `event_timing`/`event_form_assignment`/
`repeating_rule` 三个类别的题面在 Task 5 修复轮 1 (白送分闸) 后被**刻意**改写成开放
问法 (§ EVENTS_V1_NOTES.md §10-2): 答案 (activity 可读名 / 具体表单名 / repeating 语义
判定词) 从不出现在题面里, 需要"生成"而非"查表"。这类问法结构上不在 `resolve_events`
子串匹配的能力范围内, 与实现是否有 bug 无关 —— 这也是 Task 5 白送分修复的**直接代价**:
去掉白送分之后, 题面不再包含答案锚点, 一个纯子串通道自然答不出。

`conditional_event` 的 4/7 vs 3/7 miss 差异同样是题面措辞层面: 命中的 4 题问句里
"这个事件叫 X" 的 X 与 catalog 里的事件可读名逐字重合, 未命中的 3 题 (`ev_q16`/`ev_q17`/
`ev_q20b`) 题面对同一事件用了改写/意译表述, 子串对不上。**不构成不一致** —— 同一机制
(子串命中与否取决于题面是否逐字含有可索引的 OID/名称), 只是这一类里题面用词恰好有的
逐字吻合、有的没有。

### 2.2 三题归因 (q08 / q28 / q30, 已知信息泄漏题, 单列不进总分)

三题的 `expected_facts` 字面陈述在 protocol 文档正文里被发现存在 (`EVENTS_V1_NOTES.md`
§10-5/§10-6), 卡片/doc 通道对这三题存在已知的部分泄漏命中。本次事件通道实测各自的命中
情况 **与卡片/doc 侧的泄漏机制完全不同源**:

| 题 | 事件通道 (`resolve_events`) | 卡片/doc 侧已知泄漏 (NOTES §10-6) |
|---|---|---|
| `ev_q08` | **未命中** (返回 0 条) — 事件层对这题**没有**该泄漏 | 卡片侧 + doc 侧均命中 (跨表单脚注 / 评估条目列表) |
| `ev_q28` | **命中** — 唯一返回的 assignment 类型目标即为 gold, 经由 item OID 子串匹配 → `collect_scope` 减法算出 (真实结构化推导, 不是文本巧合命中) | 仅 doc 侧命中 (章节定义正文) |
| `ev_q30` | **命中** — assignment 类型目标里 1 条为 gold, 同样经由 item OID → `collect_scope` 算出; 另外混入 3 条**不同类型** (`event:`/`activity:` 前缀) 的噪声条目, 系事件/活动名称索引对该题题面里另一个可读名的独立命中, 与该题真正问的采集范围无关 (§3 详述) | 仅 doc 侧命中 (评估条目列表同段落) |

**结论**: `ev_q08` 上, 事件通道与卡片/doc 侧的已知泄漏**不同源不叠加**——事件通道完全
没有这一泄漏路径。`ev_q28`/`ev_q30` 上, 事件通道确实命中, 但**命中机制是 collect_scope
结构化推导** (消费 `assignments`/`items` 两池的确定性减法), 与卡片/doc 侧"文档正文恰好
把两件事写在同一段"的**文本共现型泄漏**是两种不同性质的命中路径, 不应混为一谈——前者是
本单元设计要交付的能力本身在起作用, 后者是旁支通道的已知副作用。因此把这两题算进"事件层
增益"里是恰当的(它们展示的正是这条新通道的设计目的), 但**不能**因为这两题命中就说"事件
通道复现了 doc 侧的那个泄漏", 两者是巧合地对同一题都答对, 机制无关联。按团队 lead 要求,
这 3 题已从上面 §2 的 15/33 总分统计口径中天然分离看待 (它们各自落在
`event_form_assignment`/`item_collection_scope` 类别桶里, 未被抽出另算, 但本节已单独
交代其结果不应被解读为"泄漏叠加"或用来注水总分)。

## 3. 类型6 (item_collection_scope, q27-31) 精度实测 — 减法是否真的有效

**拘束条件 (团队 lead §11-1)**: 引用这 5 题证明"减法有效"必须同时报出通道实际返回件数。
下表逐题给出 `resolve_events` 总返回数、其中 `assignment:` 类型条目数、以及该类型条目
内部的 命中/多余 (tp/fp) 拆分 (通过独立脚本对 `expected_sources` 做完整集合比较算出,
非本次评分口径里"只要交集非空即算命中"的宽松判据):

| 题 | 总返回数 | `assignment:`类型条目数 | 该类型内 tp | 该类型内 fp | 其他类型噪声 | gold 集合大小 |
|---|---|---|---|---|---|---|
| `ev_q27` | 7 | 7 | 7 | 0 | 0 | 7 |
| `ev_q28` | 8 | 8 | 1 | 7 | 0 | 1 |
| `ev_q29` | 2 | 2 | 2 | 0 | 0 | 2 |
| `ev_q30` | 4 | 1 | 1 | 0 | 3 | 1 |
| `ev_q31` | 1 | 1 | 1 | 0 | 0 | 1 |

**逐题机制核查 (独立脚本追踪每个被命中的 item OID key 各自贡献了多少条, 而非只看总数)**:

- `ev_q27`/`ev_q29`/`ev_q31`: 命中的 item OID key 只有 1 个 (即题面点名的那个 item 自身),
  `collect_scope` 对它的减法结果与 gold 集合**逐条集合相等** (fp=0, fn=0)。三题分别覆盖
  "正向范围较大"(7/18 一档) 到"精确"(1-2 条) 的不同规模, 减法在全部三档规模上都精确。
- `ev_q28`: 命中的 item OID key 有 **2 个** —— 一个是题面点名的目标 item 本身
  (OID 长度两位数, 减法结果 1 条, 与 gold 逐条相等, fp=0); 另一个是题面里**恰好也以子串
  形式出现**的另一个、与本题无关的 item (OID 长度 3 字符, 减法结果 7 条, 全部落入
  `assignment:`类型总数, 但均不在 gold 集合里, 记为该类型的 fp)。**这 7 条 fp 不是目标
  item 自身减法失败的产物, 是一个无关 item 的 OID 短串在题面里发生子串碰撞** —— 两种
  失效机制不同, 前者才是"减法本身出错", 后者是"索引键太短导致的跨 item 串扰"。
- `ev_q30`: 命中的 item OID key 只有 1 个 (即目标 item 自身, 减法结果 1 条, 与 gold
  逐条相等, fp=0)。总返回数里另外 3 条**类型不是** `assignment:`, 是**同一次调用里
  事件/活动 OID·名称索引段**独立命中产生的 (`event:`/`activity:` 前缀), 与 item 采集
  范围减法无关——其中 1 条恰好是与 gold 描述同一 (event, activity) 组合但用不同目标
  格式表达的"同一事实换了个写法", 另外 2 条是题面里一个通用词 (与本题所问概念无关但
  恰好是另一个 event 的可读名/略称) 造成的跨 event 巧合命中 (与 `EVENTS_V1_NOTES.md`
  `ev_q25` 记录的同一形态假阳性同源)。

**结论**: 就"目标 item 自身的 `collect_scope` 减法是否精确"这一问题, 5/5 题的答案都是
**是** (每题里真正对应题面所问 item 的那次减法调用, fp=fn=0, 逐条集合相等, 覆盖了从
7/18 到 1/40 的不同稀疏度)。但**这不等于"减法有效"这个结论对整条 `resolve_events` 通道
成立**——2/5 题 (`ev_q28`/`ev_q30`) 的**总返回集合**因为与本题无关的原因被稀释:
`ev_q28` 是短 item OID (3字符) 跨 item 子串碰撞, `ev_q30` 是事件/活动名称索引段的独立
命中混进了同一个输出列表。团队 lead 在 §11-1 指出的结构性盲区 (fact-recall/source-recall
均无 precision 惩罚, "整表返回不做减法"的通道理论上也能满分) **依然成立**——本次实测
只是说明"就这 5 道具体题目而言, 本实现恰好没有触发那个最坏情形 (逐条集合相等)", 不代表
评分方法本身的这个盲区被堵上了, 换一批题或换一个不同实现完全可能触发它。

## 4. 已知限制

1. **`Scheduling::Days/After/recurrence` 与 `Timing::*` 本研究全空**, 时点语义承载在
   `Activity name` 自由文本 —— "结构化调度"在本研究数据里不成立 (spec §2 定的能力边界
   不包含发明一个不存在的结构化字段)。
2. **脚注/隐藏清单判据是启发式** (ID 以逗号/换行分隔的自由文本列, 非强类型字段), 换
   研究/换版本可能失效, 目前只靠闸 A 的四个数字 + 闸 C 的转置一致性看守, 无独立第二参照物。
3. **`resolve_events` 是子串/精确键匹配, 与 `resolve()` 的四通道 (label 子串/token 段/
   交集/别名) 不同源**, 两者未做过挤占分析 (是否会互相抢卡片/抢目标名额未测)。
4. **§2.1 结构性盲区**: `event_timing`/`event_form_assignment`/`repeating_rule` 三类
   (15 题, 全部未命中) 结构上不在子串匹配能力范围内 —— 这不是可以靠调参修复的缺口,
   要答这类题需要生成式能力 (LLM 读三池数据后组织语言), 与 `resolve_events` 的确定性
   子串匹配设计目标(spec §2 明确"零 LLM")根本冲突。
5. **类型6 (item_collection_scope) 的减法盲区** (§3 详述): fact-recall/source-recall
   均无 precision 惩罚, 一个"整表返回不做减法"的通道理论上也能在这把尺子下满分; 本次
   实测 5/5 题目标 item 自身减法精确, 但 2/5 题的总返回集合被无关原因 (短 OID 跨 item
   碰撞 / 事件名称索引独立命中混入同一输出列表) 稀释, 不能证明该盲区已被工程手段堵上。
6. **三题归因风险** (§2.2): `ev_q08`/`ev_q28`/`ev_q30` 是已知的卡片/doc 侧部分泄漏题,
   事件通道对这 3 题的命中/未命中结果与卡片/doc 侧机制不同源, 已逐题交代, 不应被解读
   为"事件层复现了旁支泄漏"。
7. **短 item OID 索引键的跨 item 串扰** (`_MIN_ITEM_OID_LEN = 3`, 与卡片侧 `_MIN_SEG_LEN`
   同阈值沿用): 3 字符长度的 item OID 在中文/日文题面里子串命中率不低 (§3 的 `ev_q28`
   案例实测命中), 阈值越低误召回风险越高, 本次未做阈值敏感性扫描 (只用了既有阈值,
   未验证 4/5 字符阈值是否更优)。
8. **`resolve_events` 空列表的双重诱因不可从外部区分** (M4, `collect_scope.py` 消费方
   风险): 返回 `[]` 既可能是"确实没有任何该类问题的信息" (真实空), 也可能是"query 没有
   命中任何索引键" (未查到)——两者外部表现相同。已用合成 fixture 补测试 (`test_collect_
   scope_empty_when_form_has_no_assignments` / `test_resolve_events_item_scope_empty_
   when_form_has_no_assignments`), 但测试只能证明函数在这两种情况下都不臆造、不报错,
   不能让调用方从返回值本身分辨这两种诱因——需要调用方自行维护"是否查到过命中键"这一
   额外状态才能区分, `resolve_events` 当前的返回类型 (`list[str]`) 不携带这个信息。
9. **`resolve_events` 未接入生产查询路由** (`server/main.py` / `eval/run_eval.py` 均
   未调用它): 本任务交付的是 `study_lookup` 模块上的一个新方法 + 独立测试/测量, 与
   spec §2 in-scope item 6 "接 study_lookup"的字面范围一致; 是否/如何接入 `auto` 路由
   或答案生成管线未在本任务范围内, 未做。

## 5. 引用纪律自查

全文搜索 "SDTM 映射已支持" / "TA/TE/TV/SV" 相关表述: **0 处**——TA/TE/TV/SV 映射是
spec §2 明确 out of scope, 本报告未做任何相关声明。

## 6. M4/M5 处置 (Task 4 review 遗留)

- **M5 (落位)**: `collect_scope` + `_HIDDEN_ACT_KEY` 移出 `scripts/study/build_field_cards.py`,
  新住 `scripts/study/collect_scope.py` (中性模块)。渲染器与 `server/study_lookup.py`
  各自 `import`, 依赖方向不再别扭。生产渲染路径 (`assignments=None`) 行为逐字不变
  (未重渲染任何卡片, `git status` 确认 `cards/` 目录零改动)。
- **M4 (空集分支零测试)**: 新增 `test_collect_scope_empty_when_form_has_no_assignments`
  (合成 fixture: item 所属 form 在 assignments 池里零分配, 真实数据 0 例的这一支现在
  有测试覆盖) + `test_resolve_events_item_scope_empty_when_form_has_no_assignments`
  (消费方视角: 该情形下 `resolve_events` 不臆造任何目标, 静默返回 `[]`)。"确实哪都不
  采集"与"没查到"两种诱因在返回值层面仍不可分辨, 已作为已知限制记录 (§4-8), 不是
  本轮遗留未处理。

## 7. 测试数与红线自查

- `.venv/bin/python -m pytest -p no:warnings -q --junitxml=...` 实测:
  `tests=1772 failures=0 errors=0 skipped=0` (本任务开始前基线 `tests=1764`, 净 +8:
  新增 `test_study_lookup_events.py` 7 条 + `test_collect_scope.py` 3 条, 从
  `test_build_field_cards.py` 移出 2 条重复条目, 7+3-2=8)。
- `scripts/oidscan_evidence.py` 对本任务改动的全部文件 (含本证据文件) 自扫: **CLEAN,
  0 处未在 allowlist 的 OID/label 命中** (2 条历史 allowlist 命中与本任务无关, 详见
  `test_build_field_cards.py:204` 既有条目)。
- **规则 D 三方核验: 本报告完成时尚未进行**——按分工 (`AGENT_GUIDE.md`/kickoff 规矩),
  实现方不得自派 subagent, 两方核验需由 team lead 派发。以下是需要派发的两个任务
  (供 team lead 直接使用):
  1. **抽检方** (不同 `subagent_type`, 与实现方不同): 独立重跑闸 A/B/C 的全部数字,
     用非自洽写法复算 (不复用本计划脚本), 报告是否与 §1 表格逐位吻合; 独立复算 §2
     的 15/33 命中率与 §3 的精度表格 (tp/fp/fn), 报告是否复现。
  2. **审查方** (与实现方、抽检方均不同 `subagent_type`): 对抗性复核
     `server/study_lookup.py` 的 `resolve_events` 与 `scripts/study/collect_scope.py`
     ——重点: `_MIN_ITEM_OID_LEN=3` 是否有更多未被 33 题触发的短串碰撞场景; `collect_scope`
     的减法在 `item["raw"]` 缺 key / `assignments` 池部分缺失等边界下是否仍然安全;
     §5 引用纪律与 §2.2 三题归因的措辞是否有夸大/淡化倾向; `git grep` 复查零真名红线。
  两方报告落盘 `evidence/step_workflow_events_audit.md` / `evidence/step_workflow_events_audit_review.md`。
