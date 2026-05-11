# Rule A Audit Summary — P2 B-03c Batch 129 (TI/examples.md)

> Reviewer: pr-review-toolkit:review-pr (subagent_type ≠ writer general-purpose, Rule D PASS)
> Prompt version: P0_reviewer_v1.9.3
> Sample N=8 stratified seed=20260507
> Source: knowledge_base/domains/TI/examples.md (20L, 13 atoms)
> Round: 12 (B-03c)
> Timestamp: 2026-05-07

## Sample selection (N=8 stratified)

| sample | atom_id | stratum | line | rationale |
|---|---|---|---|---|
| 1 | md_dmTI_ex_a001 | H1 | L1 | unique H1 (1/1) |
| 2 | md_dmTI_ex_a002 | H2_numbered §2.5 | L3 | unique numbered H2 (1/1) §2.5 lock |
| 3 | md_dmTI_ex_a004 | SENTENCE | L7 | narrative sample (Rows 1-3 row-band annotation) |
| 4 | md_dmTI_ex_a006 | SENTENCE_bold_label | L11 | required `**ti.xpt**` decision (D-NOTE-BQ) |
| 5 | md_dmTI_ex_a007 | TABLE_HEADER | L13-14 | unique table header (1/1) §E-3 sib=null lock |
| 6 | md_dmTI_ex_a008 | TABLE_ROW | L15 | Row 1 (v1 first INCL) |
| 7 | md_dmTI_ex_a011 | TABLE_ROW | L18 | Row 4 (v2.2 boundary) |
| 8 | md_dmTI_ex_a013 | TABLE_ROW | L20 | Row 6 (file-end final row) |

Stratum coverage: H1 1/1 · H2 1/1 · SENTENCE 2/4 · TABLE_HEADER 1/1 · TABLE_ROW 3/6.

## 4-dimension verdicts

| atom_id | verbatim | schema | parent_section | hooks | overall |
|---|---|---|---|---|---|
| a001 | PASS | PASS | PASS §TI | PASS §E-2 H1 sib=1 | PASS |
| a002 | PASS | PASS | PASS §TI (§2.5 file-root) | PASS §2.5 numbered H2 sib=1 | PASS |
| a004 | PASS | PASS | PASS §TI.1 | PASS §E-5 MED-01 | PASS |
| a006 | PASS | PASS | PASS §TI.1 | PASS Hook D-NOTE-BQ | PASS |
| a007 | PASS | PASS | PASS §TI.1 | PASS §E-3 sib=null | PASS |
| a008 | PASS | PASS | PASS §TI.1 | PASS §E-5 MED-01 | PASS |
| a011 | PASS | PASS | PASS §TI.1 | PASS §E-5 MED-01 | PASS |
| a013 | PASS | PASS | PASS §TI.1 | PASS §E-5 MED-01 | PASS |

**Per-dimension totals**: verbatim 8/8 · schema 8/8 · parent_section 8/8 · hooks 8/8.

## §F-1 §2.11 Plan B trigger evaluation

NOT TRIGGERED. File contains 0 H3 elements; the only H2 (`## Example 1`) is numbered → §2.5 lock applies (file-root parent_section), NOT §F-1 §2.11 Plan B (which requires numberless H2 with H3 children). Writer report assertion at L48 confirmed correct.

## §F-2 atoms/line ratio retrospective (INFO)

- Atoms: 13
- Source lines: 20 (`wc -l` verified)
- Ratio: **0.650** — within empirical band [0.59, 0.85]
- Driver: balanced narrative + dense 6-row example table; typical ex.md profile
- Status: **CONFIRMED in band**, no INFO finding

## §F-3 kickoff atom estimate calibration (INFO)

Kickoff estimate band declared in writer report: [4, 18]. Actual: 13. Mid=11. delta_pct = |13-11|/11 = 18.2% — well within 50% threshold. **No INFO finding.**

## §R-E1..E-6 carry-forward checks

| Rule | Check | Status |
|---|---|---|
| §R-E1 Schema regression sweep PRIORITY 1 | 13 atoms × 8 required + sub-fields + conditional | PASS 12/12 |
| §R-E2 R-2.8-1 H1 sib=1 universal | a001 sib=1 hl=1 | PASS |
| §R-E3 R-2.8-2 TABLE_HEADER sib=null universal | a007 sib=null hl=null | PASS |
| §R-E4 R-2.8-3 extracted_by object schema | all 13 atoms have subagent_type+prompt_version+ts | PASS |
| §R-E5 MED-01 non-HEADING field-explicit-null | 11/11 non-HEADING atoms heading_level=null AND sib_idx=null | PASS |
| §R-E6 LOW FIGURE/CODE_LITERAL boundary | N/A (0 figure/code in batch) | N/A |

## Rule D isolation

- Writer subagent_type: `general-purpose`
- Reviewer subagent_type: `pr-review-toolkit:review-pr` (this session) ≠ writer ✓
- Independent context (this session has no writer artifacts authored) ✓
- **Rule D PASS** — independent audit confirmed.

## Findings

- HIGH: 0
- MED: 0
- LOW: 0
- INFO: 0

## Verdict

**PASS** — 8/8 atoms PASS across all 4 dimensions (verbatim/schema/parent_section/hooks). 0 HIGH/MED/LOW/INFO findings. §F-1 NOT TRIGGERED (correctly — no H3 children). §F-2 ratio 0.650 in band confirmed. §F-3 calibration delta 18.2% well within threshold. All §R-E1..E-6 carry-forward checks PASS or N/A.

## DONE

`REVIEWER_129_DONE pass_rate=100.00%_8_of_8 dim_verbatim=8/8 dim_schema=8/8 dim_parent_section=8/8 dim_hooks=8/8 findings_HIGH=0 findings_MED=0 findings_LOW=0`
