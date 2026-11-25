# Rule A audit summary — P2 B-03c round 11 batch_120 (TD/assumptions.md)

> Date: 2026-05-07
> Reviewer subagent_type: `code-reviewer` (P0 Reviewer v1.9.3, Rule D writer ≠ reviewer enforced; writer = `general-purpose`)
> Source: `knowledge_base/domains/TD/assumptions.md` (13 lines)
> Atoms: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_120_md_atoms.jsonl` (7 atoms a001..a007)
> Prompt baseline: P0_reviewer_v1.9.3.md (35 hooks: 32 v1.9.2 + 3 NEW F-rules)

---

## Verdict: PASS

- Rule A semantic full census: **7/7 PASS** (small batch → full census instead of ≥7 sample; effectively N=7=100%)
- Hook A1 byte-exact: **7/7 PASS**
- 35/35 hooks pass (29 carry-forward + 3 v1.9.3 F-rules + 3 v1.9.2 hooks; §R-F-2 + §R-F-3 fired as INFO non-blocking)
- HIGH severity findings: **0**
- MED severity findings: **0**
- LOW severity findings: **0**
- INFO carries (non-blocking, expected per kickoff §0.5 + §F-2/F-3): **2** (§F-2 ratio 0.538 below band lower edge + §F-3 calibration delta 55.6% > ±50%)

---

## Hook results detail

### §R-E1 CRITICAL Schema regression sweep PRIORITY 1
- 7/7 atoms have exactly the canonical 12 keys: `atom_id, file, line_start, line_end, parent_section, atom_type, verbatim, heading_level, sibling_index, figure_ref, cross_refs, extracted_by`
- Status: **PASS** (0 schema regression; sustains post-v1.9.2 cumulative 9294+7=9301 atoms 0 schema regression streak)

### §R-E2 HIGH H1 sib_idx=1 universal verify (R-2.8-1)
- a001 H1 (`# TD — Assumptions`): hl=1, sib=1 → **PASS**

### §R-E3 HIGH TABLE_HEADER sib_idx=null universal verify (R-2.8-2)
- 0 TABLE_HEADER atoms in batch — **N/A**

### §R-E4 HIGH extracted_by object schema verify (R-2.8-3)
- 7/7 atoms: `extracted_by = {"subagent_type":"general-purpose","prompt_version":"P0_writer_md_v1.9.3","ts":"2026-05-07T13:45:00Z"}` (3 keys, all required) → **PASS**

### §R-E5 MED non-HEADING field-explicit-null (MED-01)
- 6/6 non-HEADING atoms (a002..a007): `heading_level: null, sibling_index: null` explicitly present (NOT omitted) → **PASS**

### §R-E6 LOW FIGURE-vs-CODE_LITERAL boundary
- 0 FIGURE / 0 CODE_LITERAL in batch — **N/A**

### §R-F-1 HIGH §2.11 Plan B sub-namespace verify (NEW v1.9.3)
- Source TD/assumptions.md has 0 H2 / 0 H3 → §F-1 trigger does NOT fire
- Status: **N/A** (no Plan B namespace required)
- Backward-compat consideration: confirms numberless-H2-with-H3-children pattern absent; no regression risk this batch

### §R-F-2 INFO atoms/line ratio retrospective (NEW v1.9.3)
- atoms=7 / source_lines=13 = **0.538**
- Empirical band: 0.59-0.85 → **0.538 below lower edge by 0.052**
- Driver: smallest-in-round 13L file with 5/13 lines being blank separators (38% blank-line ratio); narrative L3 + overlapping list-items L5/L7/L9/L11/L13 = 6 content lines yielding 7 atoms (1 H1 + 1 narrative SENTENCE + 5 LIST_ITEM)
- Comparable precedent: small ass.md files generally trend lower-edge; round 10 cumulative ratio 0.591 also at lower edge
- **INFO carry C-R11-batch_120-01**: small-file ratio drift below 0.59 lower edge — non-blocking, contributes to round 11 cumulative ratio retrospective
- Status: **INFO carry, non-blocking** (per §F-2 INFO designation)

### §R-F-3 INFO kickoff atom estimate calibration retrospective (NEW v1.9.3)
- Kickoff §1 row 7 estimate: `~3-6` → mid=4.5
- Actual atoms: 7
- delta_pct = |7 - 4.5| / 4.5 × 100 = **55.6%** (above ±50% threshold)
- Driver: kickoff estimated 3-6 atoms assuming narrative-only or list-only (not both); source actually has BOTH narrative L3 AND duplicate-content list-items L5-L13 → 1 SENTENCE + 5 LIST_ITEM = 6 content atoms + H1 = 7 total
- Halt threshold per kickoff §4 row 120 (TD/ass): low<2 / high>9 → actual 7 within thresholds (no halt)
- **INFO carry C-R11-batch_120-02**: kickoff estimate-too-low for files with duplicate narrative+list-item content pattern
- Status: **INFO carry, non-blocking** (per §F-3 INFO designation)

### Hook 22b (D-1 CRITICAL) — kickoff §0.5 byte-exact verify
- Round 11 kickoff §0.5 was 30/30 PASS at write-time → trust kickoff numeric claims
- Status: **PASS (inherited from kickoff verify)**

### Hook D-NOTE-BQ (D-2 HIGH) — blockquote-prefix NOTE detection
- Source TD/assumptions.md has 0 blockquote lines (`> **Note:**` / `> **Exception:**`) → **N/A**

### Hook D-D8 (D-4) — numberless `## Overview` H2 chapter root inherit
- 0 H2 in source → **N/A**

### §2.4 multi-batch slice
- 13L < 300L threshold → single batch → **N/A**

### §2.5 numbered H2 self-namespace
- 0 H2 → **N/A**

### §2.6 FIGURE-in-domains lock
- 0 mermaid / 0 ASCII / 0 PNG-ref in source → **N/A**

### §2.7 numberless H2 childless = file-root parent inherit
- 0 H2 → **N/A**

### §2.9 LIST_ITEM sib_idx universal null
- 5/5 LIST_ITEM atoms (a003..a007): sib_idx=null explicit → **PASS**

### §2.10 / §R-E5 LIST_ITEM hl+sib explicit-null JSON form
- 5/5 LIST_ITEM: both `heading_level: null` and `sibling_index: null` present (NOT omitted) → **PASS**

### §2.11 Plan B sub-namespace
- 0 numberless H2 with H3 children → **N/A**

---

## atom_id uniqueness + sequential

- 7 atoms, all unique → **PASS**
- Sequential a001..a007 (3-digit) match expected → **PASS**
- Prefix `md_dmTD_assn_a` consistent per §2.2 → **PASS**

## parent_section consistency

- 7/7 atoms: `§TD [TD — Assumptions]` (file-root) → **PASS**
- Format `§<D> [<D> — <Section>]` matches kickoff §1 row 7 "parent_section root" column → **PASS**

---

## Rule A semantic full census (7/7)

| atom_id | line | type | verdict | semantic notes |
|---|---|---|---|---|
| a001 | L1 | HEADING h1 | PASS | File-root "# TD — Assumptions"; anchors §TD parent for all children |
| a002 | L3 | SENTENCE | PASS | Full intro narrative paragraph: TD purpose + assessment-time-bias + RECIST scope + non-oncology applicability caveat. Multi-sentence block correctly classified SENTENCE per existing convention (paragraph-level prose unit). |
| a003 | L5 | LIST_ITEM | PASS | Numbered "1." duplicating first portion of a002 narrative — **source-side intentional duplication faithfully preserved per Rule B**, not writer-introduced |
| a004 | L7 | LIST_ITEM | PASS | Numbered "2." TDANCVAR/anchor-date variable: Required, ANCH1DT default, ADaM naming convention, multi-pattern offset rule referencing TDSTOFF |
| a005 | L9 | LIST_ITEM | PASS | Numbered "3." TDSTOFF semantics: in-conjunction-with anchor, ISO 8601 positive-or-zero interval representation |
| a006 | L11 | LIST_ITEM | PASS | Numbered "4." pattern definition: equal-duration intervals, first assessment = anchor + TDSTOFF + TDTGTPAI; baseline exception clause |
| a007 | L13 | LIST_ITEM | PASS | Numbered "5." negative-applicability clause: TD not created when schedule varies per subject (e.g., event-driven first phase) |

**Semantic coverage**: all five SDTM TD assumptions captured + intro narrative + H1 anchor = complete domain assumption coverage. No semantic gap, no fabrication, no truncation.

**Source-side duplication note**: source authored a002 (L3 narrative) AND a003 (L5 list-item-1) with overlapping content. This is a **source-as-authored** artifact, not a writer defect — both atoms are byte-exact verbatim and Rule B preservation is correct. Reviewer flags this as observed but not actionable (source is upstream). If business judgment later wishes to deduplicate, that is a Rule B Phase-2 source-revision decision, not a P2 B-03c verification concern.

---

## Final verdict: **PASS**

- 35/35 hooks PASS (incl. 2 INFO carries non-blocking)
- 7/7 Rule A semantic
- 0 HIGH / 0 MED / 0 LOW severity findings
- 2 INFO carries forward to round 11 close mini-audit:
  - **C-R11-batch_120-01** §F-2 ratio 0.538 below 0.59 lower edge (small-file driver)
  - **C-R11-batch_120-02** §F-3 calibration delta 55.6% > ±50% (estimate-too-low for duplicate narrative+list pattern)

No HALT triggered. Proceed to batch_121 (TD/ex 165L §2.6 ×3 FIGURE largest-in-round).
