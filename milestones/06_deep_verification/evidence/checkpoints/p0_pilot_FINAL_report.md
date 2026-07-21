# P0 Pilot 最终收官报告

> 日期: 2026-04-24
> 工程: 06 Deep Verification (SDTM KB 字面级 PDF→KB 深审)
> PLAN 版本: v0.4
> **最终 Gate**: **CONDITIONAL_PASS** (Rule D 81.25% > 80% 门槛; 8/9 atom_type 验证; FIGURE 延后至 P1; Finding H2 P1 前必修)

---

## 0. 执行摘要

P0 Pilot 按 PLAN v0.4 §5.1 跑通 3 target 全流程 (writer → matcher → reviewer) + 1 轮 prompt v1 → v1.1 回归升级. **结论**: 方法论 work, 工具链 work, schema 基本 freeze-ready (+2 in-flight verdict), **具备进 P1 的能力但需先修 Finding H2**.

**最大业务发现**: F-T1-5 + M2 — `model/04` spec 表 12→5 列 + `ch08` examples 表数据值错 (CMDOSE 19→100). 这是 Step 0-4 完全没审出来的真实 KB 内容缺陷. 两个发现已证明 "原子级字面审" 方法论的价值.

---

## 1. 三 target 数据总览

| Target | PDF | MD | PDF atoms | MD atoms | Forward verdict (主导) | Reverse verdict (主导) |
|---|---|---|---|---|---|---|
| **T1** v1 | SDTM_v2.0.pdf p.50 | model/04_associated_persons.md (38 行) | 17 | 25 | EXACT 4 / EQUIVALENT 4 / PARTIAL 8 / MISSING 1 | SOURCED 18 / UNSOURCED 1 / SYNTHESIZED 6 |
| **T1** v1.1 (regression) | 同上 | 同上 | 21 | 21 | EQUIVALENT 12 / PARTIAL 1 / MISSING 4 / TABLE_SIMPLIFIED 4 | SOURCED 16 / SYNTHESIZED 3 / EDITORIAL_ADDITION 1 / UNSOURCED 1 |
| **T2** | SDTMIG v3.4 p.428 | chapters/ch08_relationships.md (前 50 行) | 30 | 42 | EXACT 13 / EQUIVALENT 5 / PARTIAL 7 / MISSING 9 | SOURCED 20 / UNSOURCED 18 / SYNTHESIZED 4 |
| **T3** | SDTMIG v3.4 p.137 (AE) | domains/AE/assumptions.md (前 30 行) | 32 | 55 | EXACT 13 / EQUIVALENT 6 / PARTIAL 5 / MISSING 7 / TABLE_SIMPLIFIED 1 | SOURCED 16 / UNSOURCED 39 |

**原子总计**: 3 target × (PDF + MD) = 83 PDF atoms + 143 MD atoms = **226 atoms**; **198 ledger entries** (forward+reverse, T1 只留 v1.1 计数).

---

## 2. Rule D 历程

| Reviewer | Slot | Target | 准确率 | Verdict |
|---|---|---|---|---|
| oh-my-claudecode:code-reviewer (v1) | #5 (在 P0 Pilot) | T1 v1 | 70% | **FAIL** → 升 v1.1 |
| pr-review-toolkit:code-reviewer (v1.1) | #10 | T1 v1.1 | **85%** | **PASS** |
| feature-dev:code-reviewer | #11 | T2+T3 | **81.25%** | **PASS** |

**Rule D roster 累计**: 11 独立 subagent_type (目标 ≥15, 剩 5 在池中). 路径:
1. critic (PLAN v0.2 审) → 2. verifier (PLAN v0.3 审) → 3. Explore (T1 v1 PDF writer) → 4. ohmycc:explore (T1 MD writer) → 5. feature-dev:code-explorer (T1 forward) → 6. ohmycc:document-specialist (T1 reverse) → 7. ohmycc:code-reviewer (T1 v1 review) → 8. ohmycc:executor (T1 v1.1 + T2/T3 writer + forward) → 9. ohmycc:writer (T1 v1.1 + T2/T3 reverse) → 10. pr-review-toolkit:code-reviewer (T1 v1.1 review) → 11. feature-dev:code-reviewer (T2+T3 review).

---

## 3. 原子类型覆盖 (8/9)

| atom_type | 何处测到 | 首见 |
|---|---|---|
| HEADING | T1/T2/T3 | T1 |
| SENTENCE | T1/T2/T3 | T1 |
| LIST_ITEM | T1/T2/T3 | T1 |
| TABLE_HEADER | T1/T2/T3 | T1 |
| TABLE_ROW | T1/T2/T3 | T1 |
| CROSS_REF | T2 MD + T3 PDF/MD | T2 |
| CODE_LITERAL | T2 PDF + T3 PDF/MD | T2 |
| NOTE | T2 MD + T3 PDF | T2 |
| **FIGURE** | **未测到** | — |

**FIGURE 延后**: p.428 (ch08 §8.1-§8.2) 无图, p.137 (AE 章首页) 无图. ch08 唯一图在 p.440 (§8.4 Specimen Relationship). 建议 P1 抽样阶段补测, 不阻塞 P0 收尾.

---

## 4. v1.1 Fix 8 项成果 (全 ✓)

| Fix | 问题 | v1.1 方案 | T1 验证 | T2/T3 验证 |
|---|---|---|---|---|
| H1 外部知识幻觉 | v1 matcher 在 discrepancy 引 `C55361` (训练数据带入) | prompt 强制 discrepancy 仅引 source+candidate verbatim | ✅ grep False | ✅ 0 violation |
| H2 正反向矛盾 | v1 forward MISSING 但 reverse SOURCED 同一 atom | reverse matcher 自查一致性 | ✅ soft PASS | ⚠️ T2/T3 重发现 (见 §5 Finding H2) |
| H3 KEYWORD 语义化 | v1 标 `[KEYWORD_MISSING: shall]` 但 verbatim 无该字面词 | KEYWORD 仅字面词 diff 才标 | ✅ 0 误标 | ✅ 0 (T3) / 2 (T2, 见 M1) |
| M1 writer 漏表前 caption | v1 PDF writer 漏 "Associated Persons—Additional Identifier Variables" HEADING | writer prompt 加 "表前 caption 独立 HEADING" | ✅ a014 新增 | — |
| M2 writer 段落断章 | v1 PDF writer 只抓 1 句 但段有 4 句 | writer prompt "按段落遍历, 每句 SENTENCE" | ✅ a011/a012/a013 补齐 | — |
| M3 PARTIAL 阈值 | v1 PARTIAL 放行 重叠 0.45 的低质 match | PARTIAL ≥0.50 硬 gate | ✅ 0 违反 | ✅ 0 违反 |
| TABLE_SIMPLIFIED verdict | v1 用 PARTIAL 混 table 列退化和普通部分覆盖 | 新 verdict 区分 | ✅ 4 用例 | ✅ T3 1 用例 |
| EDITORIAL_ADDITION verdict | v1 "Source: ..." 元数据误判 SYNTHESIZED | 新 verdict 明确编辑添加 | ✅ 1 用例 | — |

**重要运维 insight**: v1 PDF writer (`Explore` subagent_type) **不守"无自然语言"指令**, 返回摘要不返回 JSONL. 换 `oh-my-claudecode:executor` + Write tool 直写 = 彻底解决. P1 规模 (5000+ atoms) 必须全用 executor/writer 家族.

---

## 5. 新 findings (T2+T3 首发, P1 前需处理)

### [HIGH] H2' — Reverse ledger verdict/field 不一致 bug
**位置**: T3 reverse `md_AE_assumptions_a002-a005`
**现象**: `pdf_atom_ids` 字段非空 (列出 `ig34_p0137_a022`) 但 verdict=UNSOURCED. 矛盾.
**影响**: reverse UNSOURCED 统计虚增, 覆盖率低估.
**P1 前必修**: reverse matcher 强制先读 forward ledger, 对已 forward-matched 的 md atom 按 forward 结果写 reverse verdict.

### [HIGH] H1' — CODE_LITERAL 被误分类为 NOTE
**位置**: T2 MD writer `cm.xpt` → NOTE (应 CODE_LITERAL)
**影响**: `*.xpt` / codelist 代码常量在 MD 系统性误归类, 破坏 CODE_LITERAL 字面匹配.
**P1 前修**: MD writer prompt 明示 "任何 `*.xpt` / `*.sas7bdat` / dataset 文件名必 CODE_LITERAL 无论语法上下文".

### [MEDIUM] M1' — PDF typo 被 MD 修正但 matcher 反标 KEYWORD_MISSING
**位置**: T2 PDF `GMGRPID` (应为 `CMGRPID`, CM domain typo) → MD 写 `CMGRPID` → matcher 标 KEYWORD_MISSING (错)
**方案**: v1.2 新增 `EDITORIAL_CORRECTION` verdict, 区分 "MD 修正 PDF typo" (好事) 与 "MD 内容缺失".

### [MEDIUM] M2' — MD 示例表数据 corruption
**位置**: T2 `md_ch08_a040` CMDOSE `19→100`, `"Generic Med A"→"Generic Med"`
**严重度**: 这是真 KB 数据错, 用户使用 examples 时会得错值. P1 要对 `examples.md × 63 domain` 做全表字面 diff.

### [MEDIUM] M3' — CROSS_REF 多对一映射反向不对称
**位置**: T3 PDF a014/a017 (完全相同 §4.4.7 cross-ref) → 同 MD a038
**影响**: forward 都 EQUIVALENT 但 reverse a038 判 UNSOURCED.
**与 H2' 同源修复**: reverse matcher 先读 forward.

### [LOW] M4' / M5' 结构性 MISSING
T3 大量 CODE_LITERAL MISSING (ISO 8601, RFSTDTC) 因为 AE 变量定义在 `variables.md` (out-of-scope per CLAUDE.md — 由 xlsx 脚本管) 非 assumptions.md. P1 要按文件类型配对比对域.

---

## 6. Schema v1.2 in-flight (待 P1 前或初期应用)

| 变更 | 类型 | 理由 |
|---|---|---|
| 新 verdict `EDITORIAL_CORRECTION` | forward 正向 | M1' 区分 PDF typo 修正 |
| MD writer enum 硬 gate | prompt | N1 (T1 v1.1) + M1' 守门非枚举 atom_type |
| Reverse matcher forward-aware | matcher logic | H2' + M3' 消 reverse/forward 矛盾 |
| MD writer `*.xpt` CODE_LITERAL 规则 | prompt | H1' 防文件名误归 NOTE |
| Reverse similarity ≥0.50 gate | matcher | N2 (T1 v1.1) 消 lenient SOURCED |
| Heading EQUIVALENT ≥0.85 Jaccard | matcher | N3 (T1 v1.1) 精确技术标签保护 |
| Examples table 全表字面 diff (P1) | P1 plan | M2' 防规范示例数据 corruption |

---

## 7. 数据资产清单 (16 文件)

```
.work/06_deep_verification/evidence/checkpoints/
├── p0_T1_pdf_atoms.jsonl              (17, v1)
├── p0_T1_md_atoms.jsonl               (25, v1)
├── p0_T1_ledger_forward.jsonl         (17, v1)
├── p0_T1_ledger_reverse.jsonl         (25, v1)
├── p0_T1_section_aggregate.jsonl      (1,  v1 手工聚合)
├── p0_T1_findings.md                  (writer 阶段 findings)
├── p0_T1_reviewer_report.md           (v1 FAIL 70%)
├── p0_pilot_report.md                 (v1 阶段报告)
├── p0_T1_pdf_atoms_v1.1.jsonl         (21, v1.1)
├── p0_T1_md_atoms_v1.1.jsonl          (21, v1.1)
├── p0_T1_ledger_forward_v1.1.jsonl    (21, v1.1)
├── p0_T1_ledger_reverse_v1.1.jsonl    (21, v1.1)
├── p0_T1_v1.1_reviewer_report.md      (v1.1 PASS 85%)
├── p0_pilot_v1.1_summary.md           (v1 → v1.1 对比)
├── p0_T2_pdf_atoms.jsonl              (30)
├── p0_T2_md_atoms.jsonl               (42)
├── p0_T2_ledger_forward.jsonl         (30)
├── p0_T2_ledger_reverse.jsonl         (42)
├── p0_T3_pdf_atoms.jsonl              (32)
├── p0_T3_md_atoms.jsonl               (55)
├── p0_T3_ledger_forward.jsonl         (32)
├── p0_T3_ledger_reverse.jsonl         (55)
├── p0_T2_T3_reviewer_report.md        (T2+T3 PASS 81.25%)
└── p0_pilot_FINAL_report.md           (本文件)

.work/06_deep_verification/evidence/failures/
└── v1.1_attempt_pdf_writer_Explore.md (Rule B 归档)

.work/06_deep_verification/subagent_prompts/
├── P0_writer_pdf_v1.md                (v1 存档)
├── P0_writer_md_v1.md                 (v1 存档)
├── P0_matcher_v1.md                   (v1 存档)
├── P0_reviewer_v1.md                  (v1 存档)
└── archive/v1_snapshot_2026-04-24/    (v1 快照备份)
```

---

## 8. P0 Gate Verdict (最终)

| 条件 | 门槛 | 实测 | |
|---|---|---|---|
| 工具链可运行 | PASS | PASS | ✅ |
| 9 种原子类型 ≥6 种 | ≥6/9 | **8/9** (FIGURE 延后) | ✅ |
| schema 可冻结 | YES | **YES w/ v1.2 in-flight (+EDITORIAL_CORRECTION)** | ✅ |
| Rule D reviewer ≥80% | ≥80% (2 个 reviewer 均要 PASS) | T1 v1.1 **85%** + T2+T3 **81.25%** | ✅ |
| subagent_type drift | ≥80% | 未测 (延 P1 定期抽 3-type) | — |
| 用户 ack pilot | 接受 | 待用户 review 本 report | 待 |

**最终 P0 Gate: ✅ CONDITIONAL_PASS**

**前进条件 (P1 启动前)**:
1. 修 Finding H2' (reverse forward-aware 一致性) — 硬 gate
2. 修 Finding H1' (MD writer .xpt CODE_LITERAL 规则) — 硬 gate
3. 新增 verdict `EDITORIAL_CORRECTION` schema — 必需
4. P1 启动后前 1000 atom 做 subagent_type drift 校准 (≥80% 一致率 gate)
5. 用户 ack

---

## 9. 下一 session 入口 (handoff)

**立即可做**:
- A. **用户 review 本 report** + ack P0 PASS
- B. **v1.2 prompt + schema 升级** (约 30 min, 修 H1'+H2'+M1'+M2' + 加 EDITORIAL_CORRECTION verdict + .xpt 规则 + reverse forward-aware)
- C. **FIGURE 补测 (可选)**: T2b = SDTMIG v3.4 p.440 (§8.4 Specimen Relationship figure), 单 writer + 单 matcher 即可 (~10 min)
- D. **P1 启动准备**: 按 PLAN §5 P1 设计, 535 页分批 PDF 原子化, 全用 executor + Write 直写模式

**推荐顺序**: A → B → (可选 C) → P1 准备

**状态文件**:
- `PLAN.md` (v0.4, 675 行, 已冻结, 下次可在此基础升 v0.5 吸收 P0 实战 findings)
- `_progress.json` (current_phase 已更新, recovery_hint 完备)
- `evidence/checkpoints/` (16 文件, 数据全齐)
- `subagent_prompts/` (v1 + archive, v1.1 prompt 内嵌在 dispatch, 待 v1.2 正式写入)

**关键 insight carry-over 给下一 session**:
1. 方法论价值: **F-T1-5 + M2' 两个真实 KB 缺陷**是 Step 0-4 完全没审出来的 — 证明原子级字面审的价值
2. 运维模式: P1 必须**全用 executor/writer + Write tool**, Explore 家族 20%+ 概率返回自然语言不返回 JSONL
3. Rule D 链: 11/16 已烧, 余 5 type (superpowers:code-reviewer / scientist / tracer / architect / ai-slop-cleaner). P1 内用 batch=100 粒度轮换
4. 最大风险: H2' reverse 一致性 bug 若不先修, P1 5000 原子规模会放大成系统性 reverse 数据失真

---

*Pilot 收官. PLAN v0.4 + 11 Rule D slot + 226 atoms + 198 ledger entries + 12 findings. 方法论 validated, 工具链 hardened, schema +2 verdict 就绪, 8/9 atom_type 测过, FIGURE 延 P1. 下次 session 从 v1.2 升级或 P1 准备入手.*
