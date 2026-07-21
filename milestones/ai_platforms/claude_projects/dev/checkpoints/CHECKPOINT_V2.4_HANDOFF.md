# Stage v2.4 Cowork 自动执行手册

> **给 Claude Cowork (computer-use / browser 模式) 执行.**
> Cowork 亲自点浏览器上传 **3 个新文件** + 更新 Instructions + 跑 **6 题** A/B, 返回结构化报告.

---

## 背景 (≤ 100 字)

Stage v2.4 给 v2 Project 再加 **3 个文件** (按 terminology subdir 拆分) 合计 **351,752 tokens**: `11a_terminology_high_core.md` (29 codelist/68.6K) + `11b_terminology_high_questionnaires.md` (152 codelist/256.3K) + `11c_terminology_high_supp.md` (19 codelist/26.9K). **Top 200 CDISC codelist 完整 Term 值** 正式入库 (Code / Submission Value / Synonyms / Definition + codelist header 级 Related Domains). NY (C66742) + FREQ (C71113) 均在 11a_core. 本批是 v2 最大跃升 (+22pp 容量), **RAG 衰减风险最高**.

---

## 你 (Cowork) 的任务

在**已存在的 v2 Project** (`SDTM-Knowledge-v2`) 下:
1. Project Knowledge 新增上传 **3 个文件**
2. 覆盖更新 Project Instructions, 粘贴最新 `output_v2/system_prompt_v2.md` 全文 (比 v2.3 多 `<!-- stage v2.4 begin -->` 段)
3. 跑 **6 题** A/B 测试 (新 2 + 回归 2 + 深度回归 2)
4. 返回 Markdown 结构化报告

**权限假设/目录**: 同 v2.3 handoff

---

## Step 1: 进入现有 v2 Project

1. 打开 `https://claude.ai`
2. 进入 **Projects** 列表, 打开 `SDTM-Knowledge-v2` (v2.3 已在, 含 11 文件)

---

## Step 2: 覆盖 Project Instructions

1. Instructions 编辑区
2. 读 `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/system_prompt_v2.md`
3. **全文覆盖粘贴**
4. 保存

注: 新增 `<!-- stage v2.4 begin -->` 段 (CT Code 查询优先级升级为 `11a/11b/11c (full Term) > 08 (映射)`, 子目录路由规则).

---

## Step 3: 上传 3 个新文件到 Project Knowledge

| # | 绝对路径 | 大小 (tokens) | 内容 |
|---|---------|--------------:|------|
| 1 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/11a_terminology_high_core.md` | **68,559** | 29 core codelist (NY/FREQ/Epoch/Unit/Not Done/Evaluator/...) |
| 2 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/11b_terminology_high_questionnaires.md` | **256,336** | 152 QRS Test Name/Code pair codelist |
| 3 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/11c_terminology_high_supp.md` | **26,857** | 19 Device / Functional Test / Discharge codelist |

**合计 (v2.4 终态)**: **14 实体文件 / 719,241 tokens** (v2.3 11 × 367,489 + 3 新 × 351,752).

**不要上传 meta**: 同 v2.3 list (含本 handoff 文件 + STAGE_V2.4_AB_REPORT + CHECKPOINT_V2.*). 不要重传 v2.3 的 11 文件.

---

## Step 4: 等 indexing + 记 capacity %

**预期 capacity ~44-46%** (v2.3 23% + 351.7K/16K-per-pp ≈ +22pp).

⚠️ **本批 indexing 可能明显变慢** (11b 单文件 256K tokens, 比 v2.3 最大文件 112K 的 09 还大 2.3x). 如 indicator >30 分钟仍显示 "Indexing", 沿用 v2.3 策略尝试提问, 命中即证可用. 若明显超时或 Claude 报错, 记录观察 + 报告.

记下:
- 实测 capacity %
- Indexing 指示器用时 (大概观察)
- 任何异常 (上传失败 / 文件过大拒绝 / indexing 超时)

---

## Step 5: 跑 6 题 A/B 测试

在同一 v2 Project 开**新对话**, 依次问 6 题:

### T17 (新增, 批 4 目标): C66742 codelist 所有 Term 值 + Definition 是什么?
期望: 完整 4 terms (N/NA/U/Y) + 每项 Definition, Source 标 `11a_terminology_high_core.md`. 不再兜底.

### T18 (新增, 批 4 目标, 边界测试): AERELN codelist 全部 Synonyms?
**AERELN 不在 knowledge_base 源** (F1 audit 已确认). 期望 Claude 坦诚:
- 声明 AERELN 在 v2 Project 的 top 200 high tier codelist 中不存在
- 指向源路径 `knowledge_base/terminology/core/ae.md` 或 `08_terminology_map.md`
- 提供相关 AE codelist 替代 (若能识别)

判定: **PASS** = 明确声明边界 + 指向源; **FAIL** = 臆造 Synonyms 或模棱两可.

### T7 (回归 — 关键修复期望): CT Code C66742 有哪些具体值?
**v1/v2.1-v2.3 答案**: 高信心推测 Y/N/U/NA + 引 §4.3.7 + 05 mega_spec (未命中 Term 表, 因 Project Knowledge 一直无完整 Term).

本批 C66742 在 11a (rank 1), 期望 v2.4 能:
- 直接引用 11a_terminology_high_core.md 里的完整 4×4 Term 表 (Code / Submission Value / Synonyms / Definition)
- 附 Related Domains 行 (41 个 SDTM 域)
- 判定标准: **↑ vs v2.3** (从推测转为原文命中) 或 **持平** (仍推测).

### T15 (回归): RP 域 Example 数据?
期望: 与 v2.3 答案一致 (RP examples.md 在 10 未变, 应 0 衰减). 关键校验 RP 完整 21×18 rp.xpt 表仍在.

### T1 (深度回归, PLAN §F4 额外): AE.AEDECOD 的 Core 属性是什么?
期望: 与 v2.2/v2.3 答案一致 (Core=Req, §4.3.6 三元, AEPTCD 配套). **本题最敏感**, 因 11b 256K 大文件可能压缩 05_mega_spec / 02_chapters 召回优先级.

### T3 (深度回归, v2.3 正向 ↑ 数据点): PC↔PP 通过 RELREC 关联的 4 种方法?
**v2.3 答案**: 从 09 PC relrec 推导 4 粒度 + 推断 Method A/B/C/D. 期望 v2.4 **保持或改善**:
- 持平: 仍 4 粒度 + 推断 → OK
- ↑: 若 11a 或 11c 包含 RELREC 相关 codelist, Claude 可能给出更明确的 Method 映射
- ↓: 若大 11b 挤出 09 PC relrec 召回, 回到硬拒答 → **警报** (主控立即调 reviewer 归因)

---

## Step 6: 评估每题精度

| 精度标签 | 说明 |
|---------|-----|
| **持平** | v2.3 和 v2.4 答案同质 |
| **↑** | v2.4 比 v2.3 更精确 (或突破边界) |
| **↓** | v2.4 比 v2.3 差 |

- T17/T18 额外: PASS / FAIL
- T7/T15/T1/T3 额外: 持平 / ↑ / ↓

---

## Step 7: 返回最终报告

```markdown
# Stage v2.4 A/B 测试报告

> 执行日期: YYYY-MM-DD HH:MM
> Capacity (v2.4): XX% (v2.3 参照: 23%)
> Indexing 用时: ~N 分钟 (或"仍显示但提问直接命中")

## 上传确认
- [x] 11a_terminology_high_core.md 上传 (68,559 tokens)
- [x] 11b_terminology_high_questionnaires.md 上传 (256,336 tokens)
- [x] 11c_terminology_high_supp.md 上传 (26,857 tokens)
- [x] system_prompt_v2.md 覆盖
- [x] Indexing 完成 (或"指示器仍显示但提问命中")

## 6 题结果明细

### T17. C66742 codelist 所有 Term 值 + Definition
- **v2.3 答案**: (兜底推测)
- **v2.4 答案**: [完整 4 Term + Definition]
- **精度**: ↑ / 持平
- **T17 判定**: PASS / FAIL
- 说明: Source 是否标 11a? 是否含 Related Domains 行?

### T18. AERELN codelist Synonyms (边界测试)
- **v2.4 答案**: [坦诚边界 / 臆造]
- **T18 判定**: PASS / FAIL
- 说明: 是否明确声明不在 Project? 是否指向源?

### T7. CT Code C66742 具体值 (回归)
- **v2.3 答案**: 高信心推测 Y/N/U/NA + §4.3.7
- **v2.4 答案**: [完整]
- **精度 vs v2.3**: ↑ / 持平
- 说明: v2.4 是否从推测转为 11a 原文命中?

### T15. RP 域 Example 数据 (回归)
- **v2.3 答案**: 完整 21×18 rp.xpt 表 (双场景 + RPDUR P3Y)
- **v2.4 答案**: [完整 / 衰减]
- **精度 vs v2.3**: 持平 / ↓
- 说明: RP 21 行是否仍命中?

### T1. AE.AEDECOD Core (深度回归)
- **v2.3 答案**: Core=Req, §4.3.6 三元, AEPTCD 配套
- **v2.4 答案**: [持平 / 衰减]
- **精度 vs v2.3**: 持平 / ↑ / ↓
- 说明: 11b 256K 是否挤出 05 + 02 召回?

### T3. PC↔PP RELREC 4 方法 (深度回归, v2.3 ↑ 数据点)
- **v2.3 答案**: 4 粒度 (Group↔Group / Seq→Group / Group→Seq / Seq↔Seq) + 推断 Method A/B/C/D
- **v2.4 答案**: [保持 / 改善 / 回退]
- **精度 vs v2.3**: 持平 / ↑ / ↓
- 说明: v2.4 是否保持 4 粒度推导? 或 11b 挤出 09 PC 召回?

## 汇总矩阵

| # | 题目简称 | 精度 vs v2.3 | PASS? | 类型 |
|---|---------|------------|-------|-----|
| T17 | C66742 Term+Def | ↑/持平 | PASS/FAIL | 新 批 4 |
| T18 | AERELN Synonyms | — | PASS/FAIL | 新 批 4 边界 |
| T7 | CT C66742 重测 | ↑/持平 | — | 回归 |
| T15 | RP Example | 持平/↓ | — | 回归 |
| T1 | AEDECOD Core | 持平/↓ | — | 深度回归 |
| T3 | PC↔PP RELREC | 持平/↑/↓ | — | 深度回归 (v2.3 ↑ 点) |

## 汇总
- 回归衰减 ↓ 数: N / 4 (T7 实际从"推测"→期望"命中", 不算 ↓; T15/T1/T3 才是真回归敏感)
- 新增 PASS: K / 2 (T17, T18)

## 关键观察
- T7 变化: v2.4 是否从推测转为 11a 原文命中 (C66742 codelist 应在 11a rank 1)?
- 11b 256K 文件是否造成 RAG 召回稀释, 从而让 T1/T3/T15 其中一题衰减?
- Indexing 超时是否真的出现? (v2.3 说法"指示器不可靠"是否仍成立?)
- Capacity 爬升曲线是否匹配预期 ~44-46%?

## 异常/警告
- 或 "无异常"
```

---

## 决策矩阵 (供主控参考)

| Cowork 报告 | 主控决策 |
|------------|---------|
| T1/T15/T3 无 ↓, T17+T18 ≥1 PASS | 继续 Task G1 (批 5 terminology mid) |
| T1/T15/T3 无 ↓, T17+T18 全 FAIL | 回退 F2 调整算法 (低概率, reviewer 已 PASS) |
| **T1 ↓ 或 T15 ↓ 或 T3 ↓ 任一** | **立即停, 视为 RAG 衰减拐点, 主控调 reviewer 归因** (PLAN §F4 明确) |
| Capacity < 40% 或 > 50% | 与预期偏差显著, 记入 rag_decay_curve 作数据点 |
| 用户要暂停 | 暂停 |

---

## 不要做

- 不要自行登录 claude.ai
- 不要编造 Claude 的回答
- 不要修改 output_v2/ 任何 .md
- 不要跳题
- 不要上传 meta 文件或重传 v2.3 的 11 文件
- 不要延长 Instructions (只粘 system_prompt_v2 原文)

---

## 完成信号

给出结构化报告 → 主控按决策矩阵进 G1 (批 5 terminology mid) 或回退.
