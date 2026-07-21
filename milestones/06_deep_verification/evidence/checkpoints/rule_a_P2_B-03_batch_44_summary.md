# Rule A Audit Summary — P2 B-03c Round 03 batch_44 (EG/examples.md)

> Reviewer: pr-review-toolkit:code-reviewer (FALLBACK peer-alternative pool, sustained 100% PASS through B-02 + round 01/02 + round 03 batches)
> Writer subagent: general-purpose (Rule D 隔离硬约束: writer ≠ reviewer subagent_type ✓)
> Reviewer prompt: P0_reviewer_v1.9.1.md (26 hooks: v1.7 18 + v1.9 2 + v1.9.1 6)
> Audit date: 2026-05-06
> Source: `knowledge_base/domains/EG/examples.md` (110 lines)
> Writer output: `evidence/checkpoints/P2_B-03_batch_44_md_atoms.jsonl` (78 atoms)

## 1. Sample plan executed

| # | atom_id | class | atom_type | line | parent_section |
|---|---|---|---|---|---|
| 1 | md_dmEG_ex_a001 | boundary_first | HEADING | 1 | §EG [EG — Examples] |
| 2 | md_dmEG_ex_a002 | boundary_first | HEADING | 3 | §EG [EG — Examples] |
| 3 | md_dmEG_ex_a003 | boundary_first | SENTENCE | 5 | §EG.1 [Example 1] |
| 4 | md_dmEG_ex_a004 | boundary_first | SENTENCE (bold-caption) | 7 | §EG.1 [Example 1] |
| 5 | md_dmEG_ex_a012 | stratified_TABLE_HEADER | TABLE_HEADER | 23-24 | §EG.1 [Example 1] |
| 6 | md_dmEG_ex_a017 | stratified_TABLE_ROW_empty_cells | TABLE_ROW | 29 | §EG.1 [Example 1] |
| 7 | md_dmEG_ex_a025 | stratified_HEADING_H2 | HEADING | 38 | §EG [EG — Examples] |
| 8 | md_dmEG_ex_a075 | boundary_last | TABLE_ROW | 107 | §EG.4 [Example 4] |
| 9 | md_dmEG_ex_a076 | boundary_last | TABLE_ROW | 108 | §EG.4 [Example 4] |
| 10 | md_dmEG_ex_a077 | boundary_last | TABLE_ROW | 109 | §EG.4 [Example 4] |
| 11 | md_dmEG_ex_a078 | boundary_last | TABLE_ROW | 110 | §EG.4 [Example 4] |

Sample size: **11** (8 boundary + 3 stratified per kickoff §Sample plan; matches v1.9.1 §R-Stratified-Sampling per-batch standard).

## 2. Standard dimensions per atom — verdicts

All 11 atoms verified across 7 standard dimensions (verbatim_byte_exact / atom_id format / atom_type valid / parent_section valid / heading_level+sibling_index / cross_refs / extracted_by).

**Result**: 11/11 PASS across all 7 dimensions.

| Dimension | PASS count |
|---|---|
| verbatim_byte_exact | 11/11 |
| atom_id format `md_dmEG_ex_a\d{3}` | 11/11 |
| atom_type ∈ 9-enum | 11/11 |
| parent_section legality | 11/11 |
| heading_level + sibling_index discipline | 11/11 |
| cross_refs (empty array uniform) | 11/11 |
| extracted_by (general-purpose + P0_writer_md_v1.9.1 + ISO8601-Z ts) | 11/11 |

## 3. Schema invariants (full 78 atoms) — 8/8 PASS

| # | Invariant | Result |
|---|---|---|
| 1 | atom_id collision: 78 unique a001..a078 sequential | **PASS** |
| 2 | Hook C-8 prefix `knowledge_base/` universal | **PASS** (78/78) |
| 3 | atom_type ∈ 9-enum (HEADING/SENTENCE/LIST_ITEM/TABLE_HEADER/TABLE_ROW/FIGURE/NOTE/CODE_LITERAL/CROSS_REF) | **PASS** |
| 4 | HEADING h_lvl/sib non-null + non-HEADING null | **PASS** (5 HEADING all populated; 73 non-HEADING all null) |
| 5 | extracted_by + ts ISO8601-Z uniform | **PASS** (all 78 = `general-purpose` + `P0_writer_md_v1.9.1` + `2026-05-06T07:00:00Z`) |
| 6 | H2 sib chain 1,2,3,4 (clean, no skip) | **PASS** (a002=1, a025=2, a036=3, a064=4) |
| 7 | parent_section legality (H1 root self; H2 children → §EG.N [Example N] for N=1..4) | **PASS** (all H2 atoms parent=root; all non-HEADING under each H2 N inherit §EG.N [Example N]) |
| 8 | TABLE_HEADER Hook A1 v1.9 standard 2-row span (line_end - line_start == 1) | **PASS** (a012 23-24, a030 48-49, a039 62-63, a070 101-102 — all 4 = span 1) |

## 4. Distribution check (kickoff §0.5 expected)

| atom_type | Expected | Actual |
|---|---|---|
| HEADING | 5 (1 H1 + 4 H2) | **5** ✓ |
| SENTENCE | 20 | **20** ✓ |
| TABLE_HEADER | 4 | **4** ✓ |
| TABLE_ROW | 49 | **49** ✓ |
| LIST_ITEM | 0 | **0** ✓ |
| FIGURE | 0 | **0** ✓ |
| NOTE | 0 | **0** ✓ |
| CODE_LITERAL | 0 | **0** ✓ |
| CROSS_REF | 0 | **0** ✓ |
| **Total** | **78** | **78** ✓ |

Distribution matches kickoff expectation byte-exact.

## 5. v1.9.1 codified anomaly observations

### §R-D5 bold-caption SENTENCE accept (MEDIUM) — APPLIED

batch_44 contains multiple bold-caption SENTENCE atoms beginning with `**Row N:** ...` / `**Rows N-M:** ...` / `**eg.xpt**` (a004-a011, a027-a029, a038, a066-a069). Per §R-D5: bold-caption pattern `^\*\*[A-Z][^*]+(:|\.)\*\*\s+...` (non-Note/Exception) **= canonical SENTENCE**. Reviewer confirms — these are NOT misclassified as HEADING or NOTE. Specifically:

- a004 `**Row 1:** Shows a measurement of ventricular rate...` → SENTENCE canonical (caption text "Row 1" ≠ Note/Exception literal)
- a011 `**eg.xpt**` → SENTENCE canonical (file-name caption, non-Note/Exception)
- a029, a038, a069 same pattern

No FAIL emitted. §R-D5 accept rule honored.

### §R-D6 TABLE_HEADER style classification

All 4 TABLE_HEADER atoms (a012, a030, a039, a070) follow **v1.9 standard 2-row span** (`line_end - line_start == 1`). 0 v1.8 pilot legacy 1-row instances (none expected — batch is round 03 domains/, not ch04 a001-a218 pilot range). FAIL_LINE_RANGE: 0.

### §R-D1 Hook 22b kickoff drift handling — N/A

Reviewer independently grep-verified source EG/examples.md = 110 lines; H2 boundaries at lines 3, 38, 56, 89; 4 TABLE_HEADER 2-row instances at lines 23-24, 48-49, 62-63, 101-102. All match kickoff §0.5 + §1 batch_44 row + §2 distribution claims. No kickoff doc drift detected for batch_44.

## 6. Kickoff drift verification (per §R-D1)

Independent grep verify on source:
- Total lines: 110 ✓ (kickoff §1 batch_44 row "Lines: 110")
- H1 count: 1 (line 1) ✓
- H2 count: 4 (lines 3, 38, 56, 89) ✓ (kickoff §0.5 says "4 H2" indirectly via "Distribution: HEADING:5 (1 H1 + 4 H2)")
- TABLE_HEADER pairs: 4 ✓
- LIST_ITEM count: 0 ✓ (no `^- ` or `^N\.` lines)
- FIGURE: 0 (no fenced mermaid blocks) ✓ (kickoff §2.6 round 03 affected = batch_34/35 only)

**Conclusion**: writer atoms are byte-exact aligned with source AND kickoff numeric claims. Zero drift, zero writer fabrication.

## 7. Defect summary

| Severity | Count | Findings |
|---|---|---|
| HIGH | 0 | none |
| MEDIUM | 0 | none |
| LOW | 0 | none |
| INFO | 0 | none |

**Hook R23 explicit interpretation-vs-defect declaration**: 0 findings to interpret. No defect concentration to disambiguate.

## 8. Rule D 隔离硬约束 verification

- Writer subagent_type: `general-purpose` (per a001..a078 extracted_by field uniform)
- Reviewer subagent_type: `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative per kickoff §3 reviewer pool)
- **Distinct?** YES — no violation.

## 9. Final verdict

| Metric | Value |
|---|---|
| sample_size | **11** |
| weighted_pct | **100.00** |
| raw_pct | **100.00** |
| n_pass / n_total | 11/11 |
| schema invariants | **8/8 PASS** |
| HIGH/MEDIUM/LOW findings | **0/0/0** |
| **Verdict** | **PASS** |
| **halt_verdict** | **NO_HALT** |
| Gate ≥90% | **PASS (100% ≥ 90%)** |

Round 03 last per-batch reviewer audit closed. batch_44 ready to merge into root `md_atoms.jsonl` and trigger round close mini-audit (10 atoms cross 5 domains, per kickoff §6).

## 10. Done report

```
REVIEWER_BATCH_44_DONE sample_size=11 weighted_pct=100.00 raw_pct=100.00 verdict=PASS invariants=8/8 findings=0 halt_verdict=NO_HALT
```
