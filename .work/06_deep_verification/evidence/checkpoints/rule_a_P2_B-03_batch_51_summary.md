# Rule A Audit Summary — P2 B-03 batch_51 (FT/examples.md, round 04)

> Reviewer subagent_type: `pr-review-toolkit:code-reviewer` (round 04 default per kickoff §3 reviewer pool)
> Writer subagent_type: `general-purpose` (per atoms `extracted_by`)
> Rule D 隔离: PASS (writer ≠ reviewer subagent_type)
> Date: 2026-05-06
> Source: `knowledge_base/domains/FT/examples.md` (28L)
> Writer output: `evidence/checkpoints/P2_B-03_batch_51_md_atoms.jsonl` (17 atoms)
> Prompt baseline: P0_writer_md_v1.9.1 + P0_reviewer_v1.9.1 (26 hooks)

## 0. 执行 mode 声明

**AUDIT mode** (per kickoff prompt) — JSONL atoms vs markdown source byte-exact verification + 5 round invariants + Hook D-NOTE-BQ (negative case) + TABLE_HEADER sib_idx convention drift check vs root jsonl precedent.

## 1. Sample plan vs Sample taken

| 维度 | 计划 | 实际 |
|---|---|---|
| 总 atom | 17 | 17 |
| 抽样数 | full coverage 12/17 (8 boundary + 4 stratified) | 12/17 (70.6%) |
| boundary | first/last/H1/H2 + max line_end + Hook negative case + each table first/last row + first/last bold caption | S01/S02/S03/S04/S06/S07/S08/S11/S12 (9) |
| stratified | between-tables narrative + second bold caption + second TABLE_HEADER (sib=2 anomaly) | S09/S10/S11 (3) |
| anomaly verify | TABLE_HEADER sib_idx=2 drift + Hook D-NOTE-BQ negative case (URL link → SENTENCE) | S02 + S06 + S11 (per §R-Stratified-Sampling v1.9.1 +) |

## 2. 全 atom byte-exact verbatim verification (full coverage)

独立 Python diff (Bash above) 对 17/17 atoms 全 source byte-exact 验证: **17/17 PASS**.

```
Source total lines: 29 (含末尾空行)
Atom count: 17
Byte-exact verbatim PASS: 17/17
```

抽样 12 atom 详细判定全在 `verdicts.jsonl`. **0 verbatim FAIL**.

## 3. 5 round invariants check (per kickoff §6 + carry-forward locks)

| # | Invariant | 结果 | 证据 |
|---|---|---|---|
| 1 | atom_id collision check (sequential a001..a017 + pattern `^md_dmFT_ex_a\d{3,}$`) | **PASS** | 17 unique sequential ids, all match pattern |
| 2 | Hook C-8 file prefix universal (`knowledge_base/`) | **PASS** | 17/17 atoms `file` field starts with `knowledge_base/domains/FT/examples.md` |
| 3 | LIST_ITEM/SENTENCE/TABLE_ROW sib_idx=null lock (round 03 carry-forward) | **PASS** | 0 SENTENCE/TABLE_ROW with non-null sib_idx; LIST_ITEM count=0 (FT/ex 无 LIST_ITEM) |
| 4 | TABLE_HEADER Hook A1 v1.9 standard 2-row (line_end - line_start ≤ 1) | **PASS** | a007 L13-14 (=1); a016 L26-27 (=1); 0 v1.8 pilot legacy 1-row |
| 5 | extracted_by uniform (subagent_type + prompt_version) | **PASS** | 全 17 atoms = `general-purpose` + `P0_writer_md_v1.9.1` |

**5/5 invariants PASS**.

## 4. Hook 专项 verify

### Hook D-NOTE-BQ negative case (HIGH per §R-D2)
- L3 SENTENCE `CDISC publishes supplements for individual functional tests (at https://...). Additional FT examples...`
- 无 `> **Note:**` / `> **Exception:**` blockquote prefix
- writer 正确 emit atom_type=**SENTENCE** (NOT NOTE) per Hook negative case
- URL `https://www.cdisc.org/standards/foundational/qrs` 正确入 `cross_refs` field per §R-D7.3 (inline cross-ref single-atom assignment)
- **PASS** ✓

### Hook D-D8 numberless H2 chapter-root inherit (NEW per §R-D4)
- FT/ex L5 `## Example 1` = numbered H2 (`## Example N` 格式), **NOT** numberless
- writer 正确 emit H2 self-namespace `§FT.1 [Example 1]`, under-H2 atoms 入此 namespace
- D-D8 chapter-root inherit 不适用本 batch (适用条件: numberless H2 like `## Overview`)
- **PASS (not applicable here)** ✓

### Hook A4 FIGURE figure_ref (sustained)
- 0 FIGURE atoms in batch (per kickoff §0.5 row 14 实证 0 mermaid in 12 source files of round 04)
- **PASS by absence** ✓

### parent_section assignments (per kickoff sample plan)
- **pre-H2 atoms** (L1-4): a001 (L1) + a002 (L3) → both `§FT [FT — Examples]` ✓
- **H2 atom** (L5): a003 → `§FT [FT — Examples]` (file root, H2 atom itself sits under file root) ✓
- **under-H2 atoms** (L7-28): a004-a017 (14 atoms) → all `§FT.1 [Example 1]` ✓
- **PASS** ✓

## 5. TABLE_HEADER sib_idx 约定漂移分析 (重要 finding F-01)

### 现状

batch_51 含 2 TABLE_HEADER atoms 共享同一 parent_section `§FT.1 [Example 1]`:
- a007 (L13-14, ft.xpt header) sib_idx=**1**
- a016 (L26-27, suppft.xpt header) sib_idx=**2**

### 与 root jsonl 累积语料对照 (grep 实证)

| 范畴 | TABLE_HEADER 总数 | sib_idx=null | sib_idx=1 | sib_idx≥2 |
|---|---|---|---|---|
| post-batch_50 累积 root jsonl | 353 | 338 (95.8%) | 15 (4.2%) | **0** |
| 仅 round 04 batch_49 (FA/ex, 立刻先例) | 15 | 0 | 15 (uniform sib=1, 无 sib≥2) | 0 |
| batch_51 (本 batch) | 2 | 0 | 1 | 1 (NEW, 首次) |

### 解读

1. **Schema 视角**: schema/atom_schema.json 仅对 HEADING enforce sib_idx. 非 HEADING atom sib_idx 任意 integer ≥1 或 null 都 schema-valid. **无 schema violation**.
2. **Writer prompt v1.9.1 视角**: §D-6 仅约定 TABLE_HEADER 2-row line_range, 未约定 sib_idx convention. **无 explicit prompt rule**.
3. **Reviewer prompt v1.9.1 视角**: §R-D6 同上仅 line_range. **无 explicit reject rule**.
4. **Corpus precedent 视角**: 
   - 截至 round 03 close (post batch_44) — TABLE_HEADER sib_idx **uniformly null** (338 atoms, 100%).
   - Round 04 batch_49 (FA/ex) — 首次 introduce sib_idx=1 (15 atoms, 100%); 但**未 increment** even when 多个 TABLE_HEADER 共 parent (e.g., §FA.1 4 个 都 sib=1; §FA.2 3 个 都 sib=1).
   - batch_51 — 首次 increment per-parent (sib=1, sib=2), 与 batch_49 模式不同.
5. **Semantic 视角**: 若 sib_idx 含义是"per-parent positional index", batch_51 模式 (1, 2) **更 correct** 比 batch_49 (1, 1, 1, ...) — 后者 collision 在同 parent 下.

### 严重性 + 处置

- **Severity**: **LOW (INFO)** — 不阻塞 batch_51 PASS (5/5 invariants + 17/17 verbatim PASS); 但 round 04 内部 batch_49/batch_51 出现 **2 种 mutually-incompatible sib_idx convention**, 需 round 04 mini-audit / round 05 kickoff §0.5 codify.
- **Reviewer 行为** per §R-D1 (kickoff drift handling): 不 fault writer (writer 在 prompt 无 explicit rule 下 reasonable 选择); route 到 **orchestrator level** for round-close codify decision.
- **建议 codify 选项** (orchestrator decide):
  - **Option A**: 全部 TABLE_HEADER sib_idx **null** (回归 round 01-03 corpus 100% 主流; 重 emit batch_49 + batch_51 共 17 atoms).
  - **Option B**: TABLE_HEADER sib_idx **per-parent positional 1, 2, 3, ...** (batch_51 模式; 重 emit batch_49 15 atoms, sib chain restart per H2 parent).
  - **Option C**: TABLE_HEADER sib_idx **uniformly 1** (batch_49 模式; batch_51 a016 改 sib=1; 但 collision 理论缺陷).
- **强烈推荐**: **Option A** (与 95.8% corpus 主流一致, 修订 batch_49 + batch_51 共 17 atoms; 最小 disruption).

## 6. atom 数 vs kickoff 估算 + halt threshold

- kickoff §1 batch_51 估算: 14-24
- 实际: **17** (in [14, 24] = within estimate, ratio 17/28 = 0.607 vs round 03 actual 0.589 baseline)
- halt §4 row 51 阈值: <7 (low) / >36 (high) — 17 远在安全带
- **PASS** ✓

## 7. Kickoff drift verification (per §R-D1 CRITICAL)

batch_51 报告 (writer 自评 / batch report) **无 `kickoff_doc_drift_detected` flag**. Reviewer 独立 verify:
- §0.5 row 7 claim: 6 domains × 2 = 12 source files — FT/examples.md ∈ scope ✓
- §1 row 7 claim: batch_51 = FT/ex 28L 估 14-24 atoms, prefix `md_dmFT_ex_a`, parent root `§FT [FT — Examples]` — 全 match ✓
- §2.1-2.6 inherit conventions — 全 atoms 满足 ✓
- §0.5 row 13 (EX/ex 特定) 不适用 batch_51 — N/A ✓
- §0.5 row 14 (round 04 expected 0 FIGURE) — batch_51 0 FIGURE ✓

**0 kickoff drift detected; 0 writer fabrication risk.**

## 8. Final verdict

| 维度 | 判定 |
|---|---|
| Verbatim byte-exact (full coverage 17/17) | **PASS** |
| 5 round invariants (atom_id / Hook C-8 / LIST_ITEM null / TABLE_HEADER 2-row / extracted_by) | **5/5 PASS** |
| Hook D-NOTE-BQ negative case (S02 URL → SENTENCE) | **PASS** |
| Hook D-D8 (N/A — numbered H2) | N/A |
| parent_section pre-H2 / H2 / under-H2 assignments | **PASS** |
| atom 数 vs kickoff 估算 + halt | **PASS** |
| kickoff drift detection | **PASS (0 drift)** |
| Rule D writer ≠ reviewer subagent_type 隔离 | **PASS** |

**Sample-level**: 12/12 verdicts PASS; **Full-corpus byte-exact**: 17/17 PASS; **5/5 invariants** PASS.

**Sample PASS rate**: 12/12 = **100%**
**Strict (full-corpus) byte-exact rate**: 17/17 = **100%**

## 9. Findings

### F-01 TABLE_HEADER sib_idx convention drift (LOW / INFO, route to orchestrator)

- **Type**: convention drift, NOT writer defect (per §R-D1 — no explicit prompt rule to violate)
- **Scope**: 影响 round 04 batch_49 (15 atoms uniform sib=1) + batch_51 (1× sib=1 + 1× sib=2); 与 round 01-03 + B-01/B-02 + 累积 corpus 338 atoms uniform sib=null 不一致
- **Risk**: round 04 mini-audit invariant #4 (TABLE_HEADER 仅 verify line_range, 不 verify sib_idx) — 但 round 05 kickoff 若引入 sib_idx invariant, 历史 atoms 需 re-emit
- **Recommendation**: round 04 close 前 orchestrator decide codify path (推 Option A null 主流) + v1.9.2 prompt 添加 explicit TABLE_HEADER sib_idx rule
- **Severity-justification**: schema-valid + byte-exact preserved + writer reasonable in absence of explicit rule → 不 block batch_51 PASS

### 无 HIGH / MEDIUM 严重 finding.

---

**BATCH_51_RULE_A PASS rate=100% invariants=5/5 findings=[F-01_TABLE_HEADER_sib_idx_convention_drift_LOW_route_to_orchestrator]**
