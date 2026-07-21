# Rule A audit summary — P2 B-03c round 03 batch_38 (DS/examples.md L210-413, Ex10+Ex11)

> Reviewer: pr-review-toolkit:code-reviewer (Rule D 隔离: writer = general-purpose ≠ reviewer subagent_type)
> Prompt version: P0_reviewer_v1.9.1
> Audit date: 2026-05-06
> Source: knowledge_base/domains/DS/examples.md L210-413 (204 lines, sliced part 2 of 2)
> Writer output: evidence/checkpoints/P2_B-03_batch_38_md_atoms.jsonl (135 atoms a128..a262)
> Cross-batch pair: batch_37 (a001..a127, L1-209, Ex1-Ex9) + batch_38 (a128..a262, L210-413, Ex10-Ex11)

---

## 1. Sample plan (11 atoms)

8 boundary + 3 stratified per umbrella §6 (round 03 §2.4 first-time slice convention demands boundary atoms a128/a259+ priority for cross-batch + cross-H2 verification):

| # | atom_id | layer | atom_type | L_start-L_end | parent_section |
|---|---|---|---|---|---|
| 1 | md_dmDS_ex_a128 | boundary_first | HEADING | 210-210 | §DS [DS — Examples] |
| 2 | md_dmDS_ex_a129 | boundary | SENTENCE | 212-212 | §DS.10 [Example 10] |
| 3 | md_dmDS_ex_a130 | boundary | SENTENCE | 214-214 | §DS.10 [Example 10] |
| 4 | md_dmDS_ex_a131 | boundary | SENTENCE | 216-216 | §DS.10 [Example 10] |
| 5 | md_dmDS_ex_a209 | stratified_H2 | HEADING | 334-334 | §DS [DS — Examples] |
| 6 | md_dmDS_ex_a213 | stratified_TABLE_HEADER | TABLE_HEADER | 342-343 | §DS.11 [Example 11] |
| 7 | md_dmDS_ex_a151 | stratified_TABLE_ROW_empty | TABLE_ROW | 250-250 | §DS.10 [Example 10] |
| 8 | md_dmDS_ex_a259 | boundary_tail | TABLE_ROW | 410-410 | §DS.11 [Example 11] |
| 9 | md_dmDS_ex_a260 | boundary_tail | TABLE_ROW | 411-411 | §DS.11 [Example 11] |
| 10 | md_dmDS_ex_a261 | boundary_tail | TABLE_ROW | 412-412 | §DS.11 [Example 11] |
| 11 | md_dmDS_ex_a262 | boundary_last | TABLE_ROW | 413-413 | §DS.11 [Example 11] |

---

## 2. Per-sample verdicts

All 11 atoms PASS on all 7 dimensions (verbatim byte-exact / atom_id / atom_type / parent_section / heading_level/sib / cross_refs / extracted_by).

- a128 H2 `## Example 10` h_lvl=2 sib=10 (continues batch_37 sib chain ending §DS.9 sib=9; +1 increment ✓ NOT restart)
- a209 H2 `## Example 11` h_lvl=2 sib=11 (continues a128 sib=10; +1 increment ✓ NOT restart)
- a131 = `**Row 1:** Shows the screening element.` — bold-caption SENTENCE per §R-D5 (non-Note/Exception bold prefix); accepted as canonical SENTENCE ✓
- a213 TABLE_HEADER L342-343 = `line_end - line_start == 1` v1.9 standard 2-row span (Hook A1 PASS); applies to all 10 TABLE_HEADER atoms in batch_38 (style classification: 10 v1.9 standard 2-row + 0 v1.8 pilot 1-row legacy)
- a151 TABLE_ROW with consecutive empty cells `| 2 | XYZ | TA | DG1INDG | Drug-1+Investigation-Drug | 2 | DRUG1 | Drug-1 | | | TREATMENT 1 |` — byte-exact preserved (no whitespace normalization) ✓

---

## 3. Cross-batch §2.4 invariants (CRITICAL second sliced pair)

| # | Invariant | Result |
|---|---|---|
| 1 | batch_38 first atom = `md_dmDS_ex_a128`, line_start = 210 | ✓ PASS |
| 2 | batch_37 last atom = `md_dmDS_ex_a127` (L208 §DS.9, TABLE_ROW) | ✓ PASS (verified jsonl tail) |
| 3 | batch_38 atom_id contiguous a128..a262 (no gaps, 0 skipped numbers) | ✓ PASS (sorted list = list(range(128, 263))) |
| 4 | NO atom_id collision between batch_37 + batch_38 (set intersection = ∅) | ✓ PASS (collision count = 0) |
| 5 | Cross-batch H2 boundary clean: batch_37 last H2 ≤ §DS.9; batch_38 first H2 = §DS.10 (no leak) | ✓ PASS (batch_37 a127 parent=§DS.9; batch_38 a128 verbatim=`## Example 10` sib=10) |

Cross-batch continuity = **PASS** (5/5).

---

## 4. Schema invariants — full 135 atoms

| # | Invariant | Result |
|---|---|---|
| 1 | atom_id unique a128..a262 | ✓ PASS (135 unique, contiguous) |
| 2 | file Hook C-8 prefix `knowledge_base/domains/DS/examples.md` 全 135 atoms | ✓ PASS |
| 3 | atom_type ∈ 9-enum (HEADING/SENTENCE/LIST_ITEM/NOTE/FIGURE/TABLE_HEADER/TABLE_ROW/CODE_LITERAL/CROSS_REF) | ✓ PASS (4 types in use: HEADING/SENTENCE/TABLE_HEADER/TABLE_ROW) |
| 4 | HEADING h_lvl/sib non-null AND non-HEADING h_lvl/sib null | ✓ PASS (2 HEADING + 133 non-HEADING all conformant) |
| 5 | extracted_by uniform `general-purpose` + `P0_writer_md_v1.9.1` + ts `2026-05-06T12:00:00Z` | ✓ PASS (135/135) |
| 6 | HEADING sib chain — H2 sib=10, 11 (no sib=12+; NOT restart at 1) | ✓ PASS (a128 sib=10, a209 sib=11, continues batch_37 chain) |
| 7 | parent_section legality: H2 root `§DS [DS — Examples]`; non-HEADING ∈ {`§DS.10 [Example 10]`, `§DS.11 [Example 11]`} | ✓ PASS (2 H2 atoms parent=root; 133 non-HEADING parent ∈ expected set) |
| 8 | 0 FIGURE / 0 LIST_ITEM / 0 CODE_LITERAL (DS/ex content type) | ✓ PASS (0 of each) |

Distribution check (per writer): HEADING:2 / SENTENCE:48 / TABLE_HEADER:10 / TABLE_ROW:75 / 0 LIST_ITEM / 0 FIGURE / 0 CODE_LITERAL — matches actual (2+48+10+75=135) ✓

Schema invariants = **8/8 PASS**.

---

## 5. Kickoff drift verification (§R-D1 Hook R24)

Batch_38 writer report does not flag kickoff drift. Independent grep verify:
- DS/examples.md L210 = `## Example 10` (matches kickoff §0.5 row 13: H2 boundary at L210 split point) ✓
- DS/examples.md L334 = `## Example 11` (within batch_38 scope, sib=11) ✓
- DS/examples.md L413 = final `| 7 | DS10 | DS | 101 | 7 | Death due to cancer | ...` (matches batch_38 last atom a262) ✓
- 11 H2 total in DS/examples.md per kickoff §0.5 row 13 ✓ (verified via grep)

No kickoff drift detected. No writer Rule-B fabrication. ✓

---

## 6. Findings

**0 findings.**

- 0 HIGH severity
- 0 MEDIUM severity
- 0 LOW severity

No D-codified anomaly instances triggered (no NOTE-BQ, no D5 dual-constraint, no D8 chapter root, no FIGURE, no LIST_ITEM in batch_38). Sample includes 1 bold-caption SENTENCE (a131 §R-D5) — accepted as canonical SENTENCE per v1.9.1. Sample includes 1 TABLE_ROW with empty cells (a151) — byte-exact preserved.

---

## 7. Verdict

| Metric | Value |
|---|---|
| Sample size | 11 |
| Raw PASS rate | 11/11 = **100.00%** |
| Weighted PASS rate (boundary 70% + stratified 30%) | 8/8 boundary × 0.7 + 3/3 stratified × 0.3 = 0.7 + 0.3 = **100.00%** |
| Gate (≥90%) | ✓ PASS |
| Schema invariants | 8/8 PASS |
| Cross-batch continuity | 5/5 PASS |
| Halt conditions triggered | 0 |
| Findings | 0 (HIGH/MEDIUM/LOW all 0) |

**Final verdict: PASS** — batch_38 cleared for round 03 progression to batch_39 (DV/assumptions.md 7L).

---

*Audit complete 2026-05-06. Reviewer subagent_type ≠ writer subagent_type ✓ (Rule D). 11/11 byte-exact PASS, 8/8 schema invariants PASS, 5/5 cross-batch §2.4 invariants PASS. Round 03 §2.4 first-time multi-batch slice convention CONFIRMED working for second sliced pair (DS/examples.md). DM/ex slice (batch_34/35) + DS/ex slice (batch_37/38) both CLEAN.*
