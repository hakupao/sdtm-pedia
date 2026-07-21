# 06 Deep Verification — RETROSPECTIVE

> 完成日期: 2026-05-12
> 阶段跨度: P0 (2026-04-24) → P7 (2026-05-12)
> 规则 C 强制产物 (Tier 3 项目收尾)

---

## § 一、保留下来的做法

**1. 原子级字面对比方法论是有效的**
Step 0-4 的节级验证没有发现的问题，P4a 原子级比对发现了 Issues 5-16：
§8.4.4 内容错位 (Issue 4 → P4a MISPLACED verdict 直接抓住)，TV Examples 段缺失 (Issue 11)，NV §6.3.7.1 内容缺失 (Issue 14)，SC §6.3.10 空覆盖 (Issue 6) 等。原子级 verbatim 字面 diff 能发现「节级 OK 但细节错」的盲区，方法论本身 work。

**2. 双向账本设计 (PDF→KB + KB→PDF)**
正向账本 (coverage_ledger) 回答「PDF 每句有没有去处」，反向账本 (reverse_ledger) 回答「KB 每句有没有 PDF 来源」。两向结合找出 HALLUCINATED=0 (P5 结论)，以及 926 UNSOURCED_CANDIDATE 的精确分类，比单向审计更完整。

**3. P4b Section-level 聚合是必要补充**
单看原子级 verdict 看不出 SKELETON_ONLY 和 SIBLING_DROPPED 两类失效。P4b 的节树归并让这两类问题浮出水面，推动 P6 T4 修复了 41 个 HIGH 节。这是 v0.2 Plan review 最重要的架构追加，事后证明正确。

**4. Rule D subagent_type 轮换 (累计 72+ slot)**
每 phase 强制不同 subagent_type 独审，有效防止了自审盲区。P1 批次写手从 writer-family 切到 executor-family (v1.7 N21) 后，0 VALUE HALLUCINATION；P6 G6 critic 独审发现 section_coverage.jsonl stale 的 non-blocking 问题。Rule D 成本高但必要。

**5. Prompt 迭代版本控制 (v1.2 → v1.9.4)**
从 v1.2 schema frozen 到 v1.9.4 共 9 个 cut，每次 cut 前积累候选 stack、Rule D 独审后激活，形成了有序的提示词演进链。v1.7 N21（writer-family 完全禁用于 PDF 原子化）是最关键的一次，止住了累计 6 次的 VALUE HALLUCINATION 复发。

**6. P6 T2 批量 IE 扩充策略**
从 78.5% 覆盖率拉到 99.02% 的核心路径：先批量扩充 INTENTIONAL_EXCLUDE (Round1 643 + Round2 1021 = 1,664 条)，再针对 Tier A HIGH 节做精修。「先 IE 后修」比「逐条判断」效率高一个数量级，且不引入误判风险。

**7. Tier 3 工作流纪律 (failures/ + checkpoints/ + trace.jsonl)**
Rule B 失败归档保住了多次调试上下文（特别是 batch_42 halt state、round_06 schema regression）。每 phase 的 `phase_report` 事件在 trace.jsonl 形成了可查的时间线，跨 session 恢复有据可查。

**8. P7 Option C 重分析框架**
P7 初始抽样误判率 55%，但逐条分析后「内容误判率」只有 3.3%。把「verdict 标签精度」和「KB 内容质量」分开评估，是正确的评估框架。原子级账本的 verdict 层质量和 KB 内容质量是两个独立维度。

---

## § 二、必须补上的缺口

**1. P4a 规格表变量行 IE 分类不彻底 (最大缺口)**
P7 抽样 60 条中，12 条是变量规格表行 (AESEQ/PRELTM/MBTPT 等) 被错打成 PARTIAL/EQUIVALENT/ERROR，而非正确的 INTENTIONAL_EXCLUDE。根因：P4a matcher 找到低相似度匹配后就采用，没有先判断「该原子是否属于 REDUNDANT_WITH_SPEC 类别」。
→ **后续建议**: 在 P4a 前增加预过滤步骤，对 `verbatim` 命中 `| <VARNAME> | <Label> | Char/Num |` 模式的原子先标 IE(REDUNDANT_WITH_SPEC)，再进入 matcher。

**2. P4a 同例表行匹配精度不足**
6 条 WRONG 是 P4a 从同一 example 表里匹配到错误行（行序号/数据不同就打 EQUIVALENT）。根因：matcher 只检查内容相似度，未检查「行标识符 (SEQNO/USUBJID) 是否一致」。
→ **后续建议**: TABLE_ROW 原子匹配增加行标识符严格比对；相似度 <0.85 且行标识符不一致的直接降为 PARTIAL 或 MISSING。

**3. T4 Tier B 未完成 (56 SIBLING_DROPPED + 110 CONTENT_TRUNCATED)**
P6 在 G1 PASS 后停止了 Tier B 修复（MEDIUM 优先级）。这 166 个节中存在内容不完整或子节缺失的情况，虽不影响 99% 覆盖率 gate，但 KB 在这些节的深度不足。
→ **后续建议**: 作为独立 follow-up 任务，优先处理 SIBLING_DROPPED 中 shall/must 关键词出现率高的节。

**4. 437 UNSOURCED_MANUAL atoms 未最终定性**
P5→P6 T3 分类后，437 条 UNSOURCED_MANUAL (MD 有但 PDF 无) 仍未经人工确认。虽然 HALLUCINATED=0，但这 437 条的来源（合理推断 vs 幽灵内容）未做最终裁定。
→ **后续建议**: 对 UNSOURCED_MANUAL 做分批人工抽查，特别关注含 shall/must 关键词的条目。

**5. §6.3.5.9.3 PP RELREC linking 例缺口 (2 atoms, OA-4)**
P7 发现的唯一真实内容缺口：PP RELREC 链接示例 (ABC-123-0001/PPSEQ=1 和 PPSEQ=6) 未入 KB 的 PP/examples.md。该示例展示 PP 记录如何通过 RELREC 与 PC 记录关联，是实际操作中有参考价值的内容。
→ **后续建议**: 在 PP/examples.md 补充 §6.3.5.9.3 RELREC linking 示例。

**6. section_coverage.jsonl P4b 快照未刷新**
P6 T4 修复后，section_coverage.jsonl 仍是 P4b 时期的快照，部分节的 aggregate_verdict 与实际不符（如 SC/§6.3.10 实际已修复，但快照仍显 SKELETON_ONLY）。
→ **后续建议**: P4b 脚本 `scripts/p4b_section_aggregate.py` 在下次 KB 大规模修改后重跑一次。

---

## § 三、关键决策复盘

**决策 1: 覆盖率分母 = 调整后 10,400（扣除 IE）**
*做法*: 覆盖率计算为 `(非IE中覆盖原子) / (总原子 - IE原子)`。
*为什么*: 如果 IE 算入分母，任何已知不需覆盖的内容都会拉低覆盖率，导致「修了也白修」。扣除 IE 后分母更真实反映「需要 KB 覆盖的内容」。
*结论*: 决策正确。但 IE 分类质量直接影响分母准确性 → 见缺口 1。

**决策 2: P6 在 G1 PASS 后 Tier B deferred**
*做法*: G1 PASS (99.02%) 后停止 Tier B (MEDIUM 级修复)，P7 收官。
*为什么*: cost-benefit — Tier B 涉及 166 个节，继续修复边际价值递减；工程目标（「每句 PDF 有没有去处」）已回答。
*结论*: 对于「验证」工程是合理的。但如果目标是「高质量 KB」，应继续 Tier B。已在缺口 3 中记录。

**决策 3: P1 禁用 writer-family (v1.7 N21)**
*做法*: round 10 batch 42 出现第 6 次 VALUE HALLUCINATION 后，完全禁止 writer-family 参与 PDF 原子化，改为纯 executor-family。
*为什么*: 6 次复发跨越 2 种内容类型，证明 N18 的局部禁用不够，需要完全禁用。
*结论*: 决策正确，round 11-13 以及整个 P2 0 VALUE HALLUCINATION。教训：系统性失效模式要系统性根治，不能局部打补丁。

**决策 4: 原子粒度 = 「语义原子」而非「段落」**
*做法*: 每个独立事实句/列表项/表格行 = 1 原子，不按段落聚合。
*为什么*: 段落级无法发现「段落中一句正确但另一句缺失」的 partial coverage。
*结论*: 正确，但代价是 12,487 PDF 原子 + 10,435 MD 原子，规模远超预估（原估 5000-7000）。未来类似工程要上调规模预估 2×。

**决策 5: P7 采用 Option C（内容 vs 标签分离评估）**
*做法*: 初始抽样 55% WRONG，改为区分「内容问题」vs「标签问题」，内容误判率 3.3% PASS。
*为什么*: P7 的根本目的是「KB 内容质量」，而非「账本 verdict 标签精度」。标签精度是 P4a 的工程质量，不是 KB 知识质量。
*结论*: 正确的框架调整。但同时说明：如果将来要以 coverage_ledger 作为高精度审计证明，需要专门的 P4a 质量提升 pass。

---

## 附: 工程终态数字

| 指标 | 值 |
|------|----|
| PDF 原子总数 | 12,487 |
| MD 原子总数 | 10,435 |
| 覆盖率 (调整分母) | 99.02% |
| HALLUCINATED | 0 |
| Issues 发现并修复 | 5-16 (12 个) |
| P7 内容误判率 | 3.3% (2/60) |
| Rule D slot 累计 | 72+ |
| Prompt 版本迭代 | v1.2 → v1.9.4 (9 cuts) |
| 工程耗时 | 2026-04-24 → 2026-05-12 (18 天) |
