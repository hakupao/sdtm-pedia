# Rule A Audit Summary — P2 B-03c round 01 batch_21

> Batch: P2 B-03c round 01 batch_21 (CE/assumptions.md, 17 atoms)
> Reviewer subagent_type: pr-review-toolkit:code-reviewer (peer-alternative pool per §R-D8)
> Writer subagent_type: general-purpose (Rule D 隔离 OK; reviewer ≠ writer)
> Prompt version baseline: P0_reviewer_v1.9.1 / writer P0_writer_md_v1.9.1
> Date: 2026-05-05

## Source / Writer Output

- Source: `knowledge_base/domains/CE/assumptions.md` (1–25 lines, 1 H1 + 6 top-level numbered + 5 sub-letter + 1 small CRF table at L10-15)
- Writer atoms: `.work/06_deep_verification/evidence/checkpoints/P2_B-03_batch_21_md_atoms.jsonl` (17 atoms)
  - Distribution: HEADING=1, LIST_ITEM=11, TABLE_HEADER=1, TABLE_ROW=4
- Verdicts: `.work/06_deep_verification/evidence/checkpoints/rule_a_P2_B-03_batch_21_verdicts.jsonl` (11 rows)

## Sampling Plan (kickoff §3 spec)

11 atoms = 8 boundary + 3 stratified:

| # | atom_id | role | line | atom_type | rationale |
|---|---------|------|------|-----------|-----------|
| 1 | a001 | boundary first HEADING | L1 | HEADING | sole H1, h_lvl=1 sib=1 |
| 2 | a017 | boundary last | L25 | LIST_ITEM | last atom in file ('6.') |
| 3 | a014 | boundary TABLE_HEADER 2-row | L10-11 | TABLE_HEADER | only TABLE_HEADER, Hook A1 span check |
| 4 | a015 | boundary cross_refs | L22 | LIST_ITEM | only atom with cross_refs (Section 4.4.7) |
| 5 | a012 | boundary mid LIST_ITEM | L17 | LIST_ITEM | mid file '3.' |
| 6 | a002 | boundary first numbered | L3 | LIST_ITEM | first '1.' top-level |
| 7 | a004 | boundary sub-letter | L5 | LIST_ITEM | 'b.' under '1.', --SER flag list |
| 8 | a008 | boundary first TABLE_ROW | L12 | TABLE_ROW | first/boundary data row, empty cells |
| 9 | a003 | stratified sub-letter | L4 | LIST_ITEM | 'a.' under '1.' |
| 10 | a013 | stratified top-level numbered | L19 | LIST_ITEM | '4.' single-sentence |
| 11 | a016 | stratified sub-letter different parent | L23 | LIST_ITEM | 'b.' under '5.' (≠ a004 parent) |

## Check Coverage

1. **verbatim byte-exact**: 11/11 PASS (preserved `**` bold, `|` pipe, 3-space indent, `\"...\"` quotes, `--XXX` flags)
2. **atom_type**: 11/11 PASS — HEADING for `^# `, LIST_ITEM for `^\d+\.\s+` (top-level) + `^\s+[a-z]\.\s+` (sub-letter), TABLE_HEADER for L10-11, TABLE_ROW for L12-15
3. **parent_section**: 17/17 atoms file-wide = `§CE [CE — Assumptions]` (only 1 H1, all atoms inherit)
4. **HEADING meta a001**: h_lvl=1, sib=1 (sole H1) — PASS
5. **TABLE_HEADER 2-row span (Hook A1 + §R-D6)**: a014 line_start=10, line_end=11, span=1 → v1.9 standard 2-row — PASS
6. **cross_refs (a015 spot-check + §R-D7.3 + §R-D7.5)**: `["Section 4.4.7"]` correctly assigned to single sub-line atom (L22, the only atom containing "See Section 4.4.7, Use of Relative Timing Variables.") — PASS
7. **extracted_by**: 17/17 atoms = `subagent_type=general-purpose` + `prompt_version=P0_writer_md_v1.9.1` — PASS

## Style Classification (§R-D6)

- **TABLE_HEADER style**: 1 v1.9 standard 2-row (a014 L10-11 span=1); 0 v1.8 pilot 1-row legacy. 0 FAIL_LINE_RANGE post-classification.

## Kickoff Drift Verification (§R-D1 + Hook R24)

- Kickoff `multi_session/P2_B-03c_round_01_kickoff.md` not flagged for drift in writer batch report. Source L10-15 small CRF table (4 data rows + 2-row header) — atom counts (TABLE_HEADER=1, TABLE_ROW=4) match source verbatim. No kickoff-doc drift detected; no writer fabrication. INFO log: kickoff numeric claim (17 atoms; 1+11+1+4=17) consistent with writer output.

## D-codified Anomaly Instances (§R-Stratified-Sampling v1.9.1)

- **§R-D7.3 cross_refs field**: 1 instance (a015 L22, "Section 4.4.7") — sampled and verified canonical
- No NOTE-BQ / D5 dual-constraint / D8 chapter-root / bold-caption SENTENCE / mixed sib chain / ch04 pilot legacy in this batch (small domain assumptions file)

## Tally

- Sampled: 11
- Strict PASS: 11
- HIGH defects: 0
- MEDIUM defects: 0
- LOW defects: 0
- INFO findings: 0
- **PASS rate: 11/11 = 100%** (≥90% gate met)

## Rule D 隔离 (post-PASS confirmation)

- Writer subagent_type: `general-purpose`
- Reviewer subagent_type: `pr-review-toolkit:code-reviewer` (peer-alternative pool, B-02 sustained 7-batch 100% PASS empirical)
- Constraint: writer ≠ reviewer subagent_type — **OK** (different family)

## Verdict

11/11 strict PASS, 0 defects across all 7 check axes. TABLE_HEADER 2-row v1.9 standard. cross_refs §R-D7.3 canonical. parent_section uniform inherit (single-H1 file). extracted_by uniform. No kickoff drift detected. No D-codified anomalies requiring extra scrutiny beyond §R-D7.3 cross_refs (verified clean).

---

`RULE_A_VERDICT: PASS`
