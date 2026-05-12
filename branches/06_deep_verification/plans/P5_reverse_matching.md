<!-- chain: F (深度验证旁枝链 v2)
  修改本文件后, 必须检查:
  → ../_progress.json                       (phases.P5_reverse_matching 字段)
  → ../evidence/checkpoints/                (P5 产物快照)
  → ../PLAN.md §5                           (phase 状态更新)
  → ../audit_matrix.md                      (P5 section 新增)
  → ../trace.jsonl                          (phase_report 追加)
-->

# P5 — 反向比对 (MD → PDF) Sub-Plan

> Version: **v1.0 (2026-05-12, post P4b gate ALL PASS)**
> 父 PLAN: `branches/06_deep_verification/PLAN.md` v0.6
> 前置: P4b ✅ ALL PASS (section_coverage.jsonl 399 sections)
> 目标: 每个 MD 原子确定 PDF 来源 (SOURCED / SYNTHESIZED / UNSOURCED / HALLUCINATED)
> Tier 3 / 预估 **1-2 sessions**
> 脚本: `scripts/p5_reverse_match.py`

---

## 0. 输入 / 输出契约

| 项 | 值 |
|---|---|
| 输入 1 | `coverage_ledger.jsonl` (12,487 行 forward verdicts — P4a 产物) |
| 输入 2 | `md_atoms.jsonl` (10,435 atoms) |
| 输入 3 | `pdf_atoms.jsonl` (12,487 atoms — 用于 fuzzy lookup) |
| 主产物 | `reverse_ledger.jsonl` (一行/MD atom, reverse verdict) |
| 格式 | §4.4 reverse verdict 枚举: SOURCED / SOURCED_PARTIAL / SOURCED_MISPLACED / SOURCED_ERROR / SYNTHESIZED / UNSOURCED / HALLUCINATED |
| 消费方 | P6 Triage (HALLUCINATED + UNSOURCED → Issue 5+) |

---

## 1. 数据概况 (P5 启动时实测)

| 指标 | 值 |
|---|---|
| 总 MD 原子数 | 10,435 |
| 已在 coverage_ledger 被引用 (distinct md_atom_ids) | 6,214 (59.5%) |
| 未被引用 (orphaned) | 4,221 (40.5%) |

**Coverage_ledger verdict breakdown (forward)**:

| Forward Verdict | Count | P5 Reverse 对应 |
|---|---|---|
| EXACT / EQUIVALENT | 7,183 (pdf atoms) | → MD atom side: SOURCED |
| PARTIAL | 2,039 | → SOURCED_PARTIAL |
| MISPLACED | 276 | → SOURCED_MISPLACED |
| ERROR | 93 | → SOURCED_ERROR |
| MISSING / INTENTIONAL_EXCLUDE | 2,896 | → MD atom 不在 md_atom_ids → orphaned |

---

## 2. 分类算法

### 2.1 Step 1 — 反向索引 lookup (来自 coverage_ledger)

构建 `reverse_idx`: md_atom_id → [(pdf_atom_id, verdict), ...]

- 命中 EXACT/EQUIVALENT → **SOURCED**
- 命中 PARTIAL → **SOURCED_PARTIAL**
- 命中 MISPLACED → **SOURCED_MISPLACED**
- 命中 ERROR → **SOURCED_ERROR**
- 未命中 → 进 Step 2

### 2.2 Step 2 — 自动 SYNTHESIZED 规则

按以下规则自动分类为 SYNTHESIZED (无需 agent):

| 规则 | 说明 |
|---|---|
| file ∈ {VARIABLE_INDEX.md, INDEX.md, ROUTING.md} | AI/脚本派生索引文件 |
| atom_type ∈ {HEADING, FIGURE, TABLE_HEADER, CROSS_REF} | 结构锚点或合成结构 |
| atom_type = NOTE AND verbatim starts with {Source:, See also:, Reference:, Cross-reference:} | 元数据注解 |
| atom_type = TABLE_ROW AND file matches `domains/*/examples.md` AND verbatim 含 ≥5 个管道符 | 示例数据集行 (构造数据, 非 PDF verbatim) |

### 2.3 Step 3 — Fuzzy Lookup (P4a 漏网捞回)

对 Step 2 剩余的 UNSOURCED_CANDIDATE, 在 pdf_atoms.jsonl 中找同 parent_section 的 PDF 原子, 用 SequenceMatcher 计算 verbatim 相似度:

- max_similarity ≥ **0.65** → **SOURCED_P4A_MISSED** (P4a false negative, MD 内容有 PDF 源, 属于 P4a 质量问题)
- max_similarity < 0.65 → **UNSOURCED_CANDIDATE** (进 Step 4 agent review)

### 2.4 Step 4 — Agent Batch Review

对 UNSOURCED_CANDIDATE 残余, 按以下分组派 subagent 分批审查:

| 批次 | 文件组 | 原因 | 优先级 |
|---|---|---|---|
| G-A | `model/*.md` (sv20 衍生) | 系统性 sv20 gap — 预期多为 SOURCED_SV20 | MEDIUM |
| G-B | `chapters/ch04_general_assumptions.md` | ig34 章节, 高 risk | HIGH |
| G-C | `chapters/ch08_relationships.md` | ig34 章节, 高 risk | HIGH |
| G-D | `domains/*/examples.md` (非数据行) | 示例叙述 | MEDIUM |
| G-E | 其他 (小体量文件) | 长尾 | LOW |

每批 ≤ 50 原子; 每 agent: {atom verbatim + file + parent_section} → 对比对应 KB 文件上下文 → verdict

---

## 3. Reverse Verdict 枚举 (来自父 PLAN §4.4)

| Verdict | 语义 |
|---|---|
| `SOURCED` | MD 原子在 PDF 可找到源 (EXACT/EQUIVALENT 正向匹配) |
| `SOURCED_PARTIAL` | 正向 PARTIAL 覆盖 |
| `SOURCED_MISPLACED` | 有源但 parent_section 不对 |
| `SOURCED_ERROR` | 有源但 MD 内容有误 |
| `SOURCED_P4A_MISSED` | 有 PDF 源但 P4a 未匹配 (fuzzy 补找) |
| `SYNTHESIZED` | 合成产物 (合法, 不需 1:1 PDF 对应) |
| `UNSOURCED` | PDF 无, 但属合理推断/编辑 |
| `HALLUCINATED` | PDF 无且不合理 (开 Issue HIGH) |

---

## 4. 数字预估 (基于 2026-05-12 分析)

| 类别 | 预估数量 | % |
|---|---|---|
| SOURCED (含 PARTIAL/MISPLACED/ERROR) | ~6,214 | 59.5% |
| SYNTHESIZED (auto) | ~2,866 | 27.5% |
| SOURCED_P4A_MISSED (fuzzy 补找) | ~500-800 | 5-8% |
| UNSOURCED_CANDIDATE → agent review | ~500-900 | 5-9% |

**关键预期**: HALLUCINATED 应极少 (< 1%); 主要发现是 SYNTHESIZED 规模 + SOURCED_P4A_MISSED 揭示 P4a 在 sv20 章节的系统性漏网.

---

## 5. Exit Gate (P5)

来自父 PLAN §5 P5 行 + §9.1:

| Gate 条件 | 阈值 | 说明 |
|---|---|---|
| 100% MD 原子有 reverse_verdict | 10,435/10,435 | 脚本产物完整性检查 |
| Rule A 独审 100 原子分层样本 ≥95% 一致率 | ≥95% | HEADING×20+SENTENCE×20+TABLE_ROW×20+LIST_ITEM×20+FIGURE/NOTE×20 |
| HALLUCINATED 原子全部开 Issue 5+ | 0 未登记 | HIGH severity |
| UNSOURCED 原子全部开 Issue 或标记合理推断 | 0 未登记 | MEDIUM severity |
| Rule D reviewer (独立 subagent_type) PASS | ≥1 | 父 PLAN IR3 |
| trace.jsonl P5 phase_report ≥1 | ≥1 | 父 PLAN §5 v0.4 Fix Gap 7 |

---

## 6. Writer / Reviewer 分配 (Rule D)

| Slot | Type | Role | 状态 |
|---|---|---|---|
| P5-W1 | `oh-my-claudecode:executor` | Script + batch agent writer | 主 session |
| P5-R1 | `oh-my-claudecode:scientist` | Rule A 100-atom 独审 | 待派发 |
| P5-R2 | `oh-my-claudecode:code-reviewer` | Gate reviewer | 待派发 (gate 时) |

P5 batch agent review: 按批次使用 `Explore` / `oh-my-claudecode:explore` / `feature-dev:code-explorer` 轮换 (Rule D IR3).

---

## 7. 下一步 (P5 → P6)

P5 完成后:
1. HALLUCINATED atoms → P6 Triage HIGH priority Issue 5+
2. UNSOURCED atoms → P6 Triage MEDIUM priority Issue 5+
3. SOURCED_P4A_MISSED → 记录作为 P4a 质量参考 (不一定需修复)
4. P5 + P6 Triage 可交叉进行 (per P4b plan §7 "P5 可与 P6 并行")

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-05-12 | Initial, post P4b gate ALL PASS. Pre-analysis complete (10,435 md_atoms; ~6,214 SOURCED; ~2,866 auto-SYNTHESIZED; ~1,355 UNSOURCED_CANDIDATE after refinement). |
