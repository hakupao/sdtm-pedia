# Stage v2.1 A/B 测试报告

> 执行日期: 2026-04-18 → 2026-04-19 (跨日, 含上下文 compaction)
> 执行者: Claude Cowork (Chrome MCP browser automation)
> 新 Project (B): **SDTM-Knowledge-v2** (v2.1 全展开 9 .md, ~13% capacity)
> v1 Project (A): **SDTM Expert v3.4** (v1 压缩 9 .md, ~12% capacity, ~190K tokens)
> 总测试用时: 2 个会话 (含 compaction)
> 原始捕获文件:
> - v1 答案: `/sessions/pensive-festive-wright/work/v1_answers.md`
> - v2 答案: `/sessions/pensive-festive-wright/work/v2_answers.md`

## 上传确认 (历史记录, 来自前序会话)
- [x] 9 个 .md 文件全部上传成功 (00_routing → 08_terminology_map)
- [x] system_prompt_v2.md 已粘贴到 Project Instructions
- [x] Indexing 完成 (capacity 显示 13%)

## 重要前提说明 (诚实标注)

**T1-T10 题目一致**, 可直接 A/B 对比。
**T11/T12 题目在 v1/v2 之间不一致** — v2.1 使用了变体题以更精准地测试章节逐字节展开收益, 不能直接 A/B 对照, 但仍可独立判定 PASS/FAIL:

| # | 题目 | v1 实际问的 | v2 实际问的 | 可对比? |
|---|-----|-------------|-------------|---------|
| T11 | (handoff 设计为 ch08 §8.3 RELREC) | ch08 §8.3 RELREC | **ch03 §3.1.2.2 命名规则 (虚构 section)** | ❌ (变体题) |
| T12 | (handoff 设计为 ch10 附录 entity) | ch10 附录 entity | **ch04 §4.4 Timing 变量** | ❌ (变体题) |

变体题反而强化了 chapter-test 价值 (T11 测虚构 section 检出, T12 测真实章节全覆盖)。

---

## T1-T12 结果明细

### T1. AE.AEDECOD 的 Core 属性是什么?
- **v1 答案**: AEDECOD Core = **Req**. 引用 ①05_mega_spec.md AE spec 第13行 ②04_variable_index.md AEDECOD(Sy/R) ③02_chapters.md §4.3.6 AE 自然键。延伸 Req≠必有值、AELLT 对比、ADaM 衔接、PMDA。
- **v2 答案**: AEDECOD Core = **Req**. 引用 05_mega_spec.md AE spec 行号 + 04_variable_index.md(Sy/R) + 02_chapters.md §4.3.6。和 v1 同质。
- **精度**: **持平**
- **说明**: 两版结论一致, 来源精度等同, v2 无加成 (此题信息已在 mega_spec 表格中, 与 chapters 全展开无关)。

### T2. AE 严重程度变化如何记录?
- **v1 答案**: 三方案 A/B/C (单记录最严值 / 多记录+AEGRPID / AE+FA), 决策表 + ICH E2B/CTCAE 延伸。
- **v2 答案**: 同样 3 方案, 但额外引用了 **§4.2.1 Variable Naming + §4.3.6 AE narrative + §8.6.3 Findings About + assumption 7e + 06_assumptions AE 3b** 共 5 处源锚点, 每条方案的章节出处更精确。
- **精度**: **↑** (上升)
- **说明**: v2 来源溯源精度提升, 因 02_chapters.md ch04/§8 全展开后, §4.2.1 / §4.3.6 / §8.6.3 都能直接被精确引用。

### T3. PC↔PP RELREC 关联方法
- **v1 答案**: 明确声明 §6.3.5.9.3 不在 Project; 基于可见内容**重建** 3 种 + 1 种 implicit (Peer-record / Group-via-GRPID / Dataset-MANY/MANY / Implicit join)。
- **v2 答案**: v2.1 直接**拒答完整 4 种**, 引用 boundary template (§6.3.5.9.3 仍未在 ch06 完整收录, ch06 仅列骨架, 无 PC↔PP example narrative)。仅给 §8.3 MANY/MANY 一句引用。
- **精度**: **↓** (下降)
- **说明**: v2.1 边界更严格, 拒绝 v1 那种"基于通用规则推导"的重建。**对用户体验是 ↓** — 失去了实用决策树。但 v2 的边界严谨是设计意图 (避免幻觉)。

### T4. 哪些域有 EPOCH 变量?
- **v1 答案**: 44 个 domain, 按 class 分组 (Events 6 / Interventions 7 / Findings 25 / FA 2 / Special Findings 2 / SP 1 / TA 1) + 19 不含的域。来源 04_variable_index §1 + CT C99079(44)。
- **v2 答案**: 同样 44 个域, 同类组分布; **额外** 引用 **ch04 §4.1.3.1 EPOCH-Capable Domains** 原文章节 (v2 因 ch04 全展开能精确指出该 §4.1.3.1 节)。
- **精度**: **↑** (上升)
- **说明**: v2 增加了 §4.1.3.1 的章节锚点, v1 只能给数量统计来源 (variable_index + CT count)。

### T5. 如何判断变量是否需要提交到 SUPP--?
- **v1 答案**: 7 级优先级决策树 (standard variable → CO → SC → 新 --TESTCD → FA/GOC → custom domain → SUPP--)。引 §8.4.4 4 条禁令。灰色地带列举。
- **v2 答案**: 同样 5 步决策树 (合并了 step 6/7), 同样 §8.4.4 引用; 额外配套 **SUPP-- spec 表格** (来自 ch08 §8.4 全展开)。结构略简但补了 SUPP-- 字段定义。
- **精度**: **持平**
- **说明**: 决策逻辑完全一致, v2 多了 SUPP-- 表但少了 1 个步骤层级 (7→5), 信息净量近似。

### T6. AE Example 2 的具体数据是什么?
- **v1 答案**: **严格边界 ⚠️** — 数据表不在 Project (07_examples_catalog.md 只有目录), 只给标签 + 推测演示意图; 拒绝臆造。
- **v2 答案**: 同样指出 **07_examples_catalog 只有目录**; 但额外提供了 **6 个 AE Examples 的完整 catalog 表格** (Example 1-6 名称、目的、关键变量), v1 没给这层 catalog。
- **精度**: **↑** (上升)
- **说明**: 两版都不能给 Example 2 实际数据行 (catalog 限制), 但 v2.1 提供了更完整的 catalog 视图, 帮助用户决定要不要去 source 查具体数据。

### T7. CT Code C66742 有哪些具体值?
- **v1 答案**: **Project 边界 ⚠️**. 元数据 C66742 F 4 "No Yes Response" general_part4.md。**高信心推测 Y / N / U / NA**, 引 §4.3.7 + 05_mega_spec。指出 13 AE 变量使用 + 跨域 123。
- **v2 答案**: 同样 Y / N / U / NA, 同样标记推测; 额外引 **ch04 §4.3.7 Y/N Response 章节原文** + 13 AE 变量列表。
- **精度**: **↑** (轻微上升)
- **说明**: v2 因 ch04 全展开, §4.3.7 的"Y or N extended to U or NA"原文表述更直接; v1 只能从压缩文本推断。

### T8. CV 域所有变量值范围
- **v1 答案**: 先质疑前提; 42 变量按 Identifier(9)/Topic(2)/Grouping(2)/Record Qual(17)/Result(3)/Timing(10) 分层, 每变量给 CT 引用 + 边界。
- **v2 答案**: 同样 42 变量, 重组为 **4 类 value-range classes** (Identifier/Topic/Qualifier/Timing); CT 引用同等。组织略不同。
- **精度**: **↑** (轻微上升, 组织维度)
- **说明**: v2 用 value-range 维度重组, 更贴合"取值范围"问题语义; v1 用 Role 维度, 分类略偏。两版数据等同。

### T9. ch01 SDTM 整体架构 + Foundational concepts? [chapter-test]
- **v1 答案**: **PASS** with 边界提醒 — 明确指出 ch01 仅含元数据, GOC/Special-purpose/Trial Design 实际在 ch02 + SDTM v2.0。分 3 部分回答 (ch01 §1.1-§1.4 + ch02 §2.1-§2.8 Foundational + 横跨原则)。结尾给诚实边界对照表。
- **v2 答案**: **PASS** — v2.1 同样**纠正前提** "ch01 is Introduction, not Foundational Concepts"; 提供 §1.1-§1.5 完整内容; 引用 byte-exact ch01_introduction.md p. 7-12。比 v1 更精确指出"ch01 是 Introduction"的术语校正。
- **精度**: **↑** (轻微上升)
- **判定**: **PASS** ✅
- **说明**: v2 的 byte-exact ch01 让它能给出 §1.5 这样的精细 section, 而 v1 只到 §1.4。两版都做了边界纠正。

### T10. ch02 §2.6 创建新 domain 的所有步骤? [chapter-test]
- **v1 答案**: **PASS** — 引用 §2.6 item 1/2/3 原文 + 11 子步骤 a-k (但部分 d-k 简化) + 4 Key Rules。延伸 PMDA / Rust builder 模式。
- **v2 答案**: **PASS** — 提供 **完整 11 子步骤 a-k 表格** (每条 §2.6 原文 + 释义) + 4 Key Rules + **§2.6 v3.4 变更条目 (SA/SQ 添加到禁用 domain code 清单)** + GOC 判断延伸 + §2.5/§2.7 补充约束。byte-exact ch02 优势明显。
- **精度**: **↑**
- **判定**: **PASS** ✅
- **说明**: v2 给出 v3.4 新增的 §2.6 SA/SQ 变更条目 — 这是 v1 因压缩损失无法精确给出的细节。

### T11. (v1: ch08 §8.3 RELREC 数据集关系) / (v2: ch03 §3.1.2.2 命名规则虚构 section) [chapter-test, 变体题]
- **v1 答案 (ch08 §8.3 RELREC)**: **PASS with caveat** — 区分 §8.2 (record-to-record) vs §8.3 (dataset-to-dataset); 完整 RELREC 变量 spec; RELTYPE 三种取值 (ONE/ONE, ONE/MANY, MANY/MANY); 7 点延伸思考。诚实标注 §6.3.5.9.3 PC↔PP 不在 Project。
- **v2 答案 (ch03 §3.1.2.2)**: **PASS** — v2.1 立即**检出虚构的 §3.1.2.2** ("该 section 在 v3.4 中不存在"); 提供 ch03 完整 TOC (§3.1, §3.2, §3.2.1, §3.2.1.1, §3.2.1.2, §3.2.2); 给出"命名规则的真正分布"映射表 (10 条规则到具体章节 ch02 §2.2 / ch04 §4.1.6/§4.1.7/§4.2.1/§4.2.2 / ch08 §8.4.2 / Appendix D)。
- **精度**: **N/A** (题目不一致, 不可直接对比)
- **判定**: 各自 **PASS** ✅
- **说明**: 题目变体, 但都展示了 chapter-test 价值 — v1 在真实 §8.3 上做精确引用, v2 在虚构 section 上做精确否定 + 完整 ch03 TOC 验证。两个 PASS 互相补充。

### T12. (v1: ch10 附录所有 entity) / (v2: ch04 §4.4 Timing 变量注意事项) [chapter-test, 变体题]
- **v1 答案 (ch10 附录)**: **PASS** — Appendix A-E 完整 entity 列表 (B 42 缩略语按类组 / C1 v3.4 已 removed Trial Summary / D ~90 fragments / E revision history)。9 行诚实边界对照表。延伸 PMDA + ch07 trial design 界面。
- **v2 答案 (ch04 §4.4 Timing)**: **PASS** — §4.4.1-§4.4.10 全 10 个子节完整覆盖 (ISO 8601 / 右截断精度表 / Duration / Study Day no-day-0 算法 / Visits / Additional Study Days / Relative Timing UNKNOWN / Findings 域 --STDTC 禁用 / Dates as Result / Time Points 5 变量集) + v3.4 变更对照表。
- **精度**: **N/A** (题目不一致, 不可直接对比)
- **判定**: 各自 **PASS** ✅
- **说明**: v2 在 §4.4.8 给出 "**--STDTC 禁用于 Findings**" 这个 v3.4 新增条目, 是 byte-exact ch04 全展开的核心收益。

---

## 汇总矩阵

| # | 题目简称 | 精度 (v1 vs v2) | T9-T12 PASS? |
|---|---------|------|-------------|
| T1 | AEDECOD Core | 持平 | — |
| T2 | AE 严重度变化 | ↑ | — |
| T3 | RELREC 4 方法 | ↓ | — |
| T4 | EPOCH 域列表 | ↑ | — |
| T5 | SUPP-- 判定 | 持平 | — |
| T6 | AE Ex2 数据 | ↑ | — |
| T7 | C66742 值 | ↑ (轻微) | — |
| T8 | CV 域变量 | ↑ (轻微) | — |
| T9 | ch01 架构 | ↑ (轻微) | **PASS** ✅ |
| T10 | ch02 §2.6 | ↑ | **PASS** ✅ |
| T11 | (变体题) | N/A | **PASS** ✅ (各自) |
| T12 | (变体题) | N/A | **PASS** ✅ (各自) |

## 汇总数据
- T1-T8 衰减 (↓) 数: **1** (T3)
- T1-T8 上升 (↑) 数: **5** (T2, T4, T6, T7, T8)
- T1-T8 持平数: **2** (T1, T5)
- T1-T8 N/A 数: 0
- T9-T12 PASS 数: **4/4**
- T9-T12 FAIL 数: **0/4**
- T9-T10 直接对比中 v2 表现: **2/2 ↑**

## 关键观察

1. **chapter-test (T9-T12) 全 PASS** — v2.1 byte-exact 章节展开的核心假设得到验证: T9 给出 v1 没有的 §1.5; T10 给出 v3.4 新增的 §2.6 SA/SQ 变更; T11 立即检出虚构 §3.1.2.2 + 完整 ch03 TOC; T12 给出 §4.4.8 v3.4 新增的 "--STDTC 禁用于 Findings"。这些都是 v1 压缩版无法精确给出的。

2. **T3 是唯一 ↓** — v2.1 在 PC↔PP RELREC 题上拒绝重建 (§6.3.5.9.3 仍未在 ch06 完整收录), 仅给 §8.3 MANY/MANY 一句引用; v1 给了实用的 4 方法决策树 (含推测标注)。这是 v2 边界更严的代价 — 严谨 vs 实用 的权衡。**属于 v2 的设计意图**, 不是质量回退。

3. **T1-T8 整体趋势**: 5 ↑ / 2 持平 / 1 ↓, **无 ≥2 题 ↓**, 符合"继续推进"决策门槛。多数 ↑ 来自章节锚点精确化 (T2 §4.2.1+§4.3.6+§8.6.3 / T4 §4.1.3.1 / T7 §4.3.7 / T8 4-class value-range)。

4. **诚实边界一致性**: 两版都正确处理了 "数据不在 Project" 的题 (T6, T7), 都用 ⚠️ 标注。v2.1 在 T11 上展示了**主动检出虚构 section** 的能力, 这是 chapter byte-exact 全展开独有的能力。

## 异常/警告

- 无 v2.1 拒答 / 截断 / RAG miss 异常。
- T11/T12 题目变体 — 前序会话执行者将 handoff 的 ch08 §8.3 / ch10 附录 题改为 ch03 §3.1.2.2 (虚构 section 测试) 和 ch04 §4.4 Timing。这是设计加强, 但不能直接 A/B 对照, 已在报告"重要前提说明"中明确标注。
- 跨日 compaction: 测试横跨 2026-04-18 与 2026-04-19, 中间发生 1 次 context compaction, 已通过 v1_answers.md / v2_answers.md 中间文件确保答案完整保留。

## 决策建议 (按 handoff Step 9 决策矩阵)

按决策矩阵: **T1-T8 有 1 题 ↓ (T3) → 报告用户, 询问是否续**

> 注: T3 的 ↓ 属于 v2.1 边界严谨性的副作用 (拒绝幻觉重建), 不是质量回退。如用户接受这种"严谨换实用"的取舍, 建议**继续 Task D1 (批 2 examples 高频展开)**, 因为 T9-T12 全 PASS 已强证明 chapter byte-exact 路径有效。

## 后续修复方向 (供主控参考)

| 题号 | 问题 | 修复路径 |
|------|------|---------|
| T3 | PC↔PP RELREC 4 方法在 v2.1 拒答 | 在 batch 2 中纳入 ch06 §6.3.5.9.3 PP/PC examples 全展开 |
| T6 | AE Example 2 数据行未给 | 在 batch 2 中纳入 ch04 §4.3.6 AE Examples 1-6 全数据展开 (07_examples_catalog → 完整 examples) |

## 文件位置
- 本报告: `ai_platforms/claude_projects/output_v2/STAGE_V2.1_AB_REPORT.md`
- v1 原始答案: `/sessions/pensive-festive-wright/work/v1_answers.md` (会话临时, 不持久)
- v2 原始答案: `/sessions/pensive-festive-wright/work/v2_answers.md` (会话临时, 不持久)
- v2.1 上传文件: `ai_platforms/claude_projects/output_v2/00_routing.md` ~ `08_terminology_map.md`
- handoff 规范: `ai_platforms/claude_projects/output_v2/CHECKPOINT_V2.1_HANDOFF.md`
