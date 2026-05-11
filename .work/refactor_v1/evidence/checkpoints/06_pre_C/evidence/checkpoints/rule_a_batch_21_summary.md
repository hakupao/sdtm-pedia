# Rule A Audit — Batch 21 (slot #30 oh-my-claudecode:test-engineer AUDIT-mode pivot 11th)

Date: 2026-04-26
Sample: 10 atoms 1/page p.201-210, seed=20260510
Dimensions: atom_type / verbatim / parent_section / heading_fields
Section: §6.3.5.3 Cell Phenotype Findings (CP) — entirely within CP, no chapter/sub-domain transitions

## Per-atom verdict table

| # | atom_id | atom_type | verbatim | parent_section | heading_fields | score |
|---|---|---|---|---|---|---|
| 1 | ig34_p0201_a008 | PASS | PASS | PASS | PASS | 1.0 |
| 2 | ig34_p0202_a020 | PASS | PASS | PASS | PASS | 1.0 |
| 3 | ig34_p0203_a014 | PASS | PASS | PASS | PASS | 1.0 |
| 4 | ig34_p0204_a009 | PASS | PASS | PASS | PASS | 1.0 |
| 5 | ig34_p0205_a001 | PASS | PASS | PASS | PASS | 1.0 |
| 6 | ig34_p0206_a007 | PASS | PASS | PASS | PASS | 1.0 |
| 7 | ig34_p0207_a001 | PASS | PASS | PASS | PASS | 1.0 |
| 8 | ig34_p0208_a003 | PASS | PASS | PASS | PASS | 1.0 |
| 9 | ig34_p0209_a002 | PASS | PASS | PASS | PASS | 1.0 |
| 10 | ig34_p0210_a003 | PASS | PASS | PASS | PASS | 1.0 |

## Aggregate

- Raw PASS: 40/40 dims
- Raw PARTIAL: 0/40 dims
- Raw FAIL: 0/40 dims
- Weighted %: 100.0%
- Verdict: **PASS** (threshold ≥90%)

## Findings

None. All 10 atoms across all 4 dimensions verified PASS against PDF ground truth.

## Dimension-level notes

### atom_type
All atom_type assignments correct:
- TABLE_ROW (atoms 1, 2, 4, 10): specification table rows and example dataset rows — correctly distinguished from HEADING/LIST_ITEM.
- CODE_LITERAL (atom 3): `"SPECIMEN LOST"` from CPREASND CDISC Notes — correct R6 application for quoted controlled value.
- HEADING (atoms 5, 8): `CP – Assumptions` (L5 sib=3) and `CP – Examples` (L5 sib=4) — TOC-anchored sub-section headings, en-dash verified character-perfect.
- LIST_ITEM (atoms 6, 7, 9): lettered/labeled list items under numbered assumptions and Example 1a row descriptions — correct R3/R13 application.

### verbatim
All verbatim fields character-perfect against PDF:
- Atom 1 (CPCNDAGT): empty Controlled Terms cell rendered as `| |` (NEW3 outer-pipe compliant).
- Atom 2 (CPRESTYP): (RESTYPRS) codelist, examples with double-quoted values match exactly.
- Atom 3: `"SPECIMEN LOST"` with surrounding quotes preserved verbatim.
- Atom 4 (CPTPTREF): empty Controlled Terms cell, "PREVIOUS DOSE"/"PREVIOUS MEAL" examples match.
- Atom 7 (FSC/SSC item e): long multi-sentence paragraph with grammatical artifact "a descriptions" preserved verbatim; CPMRKSTR variable name `CD45+SSClo/CD45+` character-perfect (O-P1-26 PASS).
- Atom 9 (Rows 4-5): CPMRKSTR value `CD45+CD3-CD19+CD14-CD56-` character-perfect (O-P1-26 PASS).
- Atom 10 (cp.xpt row 1): `10^6/L` notation, all column values, outer-pipe and trailing pipe present (NEW3 compliant).

### parent_section
All 10 atoms: `§6.3.5.3 Cell Phenotype Findings (CP)` — correct NEW6 sub-domain canonical form.
No short-bracket `§6.3.5.3 [CP]` or sentence-case deviations detected.

### heading_fields
- Atoms 5, 8 (HEADING): heading_level and sibling_index correct per NEW7 L5 chain.
  - `CP – Assumptions`: L5 sib=3 (Description=1, Specification=2, Assumptions=3). PASS.
  - `CP – Examples`: L5 sib=4 (Description=1, Specification=2, Assumptions=3, Examples=4). PASS.
- All non-HEADING atoms (1, 2, 3, 4, 6, 7, 9, 10): heading_level=null, sibling_index=null. PASS.

## Reviewer notes

- AUDIT-mode pivot success: PASS (test-engineer agent repurposed successfully for atom verdict review)
- TOC-anchored audit: 0 FP / 0 inverted — all parent_section assignments correct, no spurious TOC entries claimed
- Cross-family pool depth: omc-family 4th burn (test-engineer); cumulative 11th AUDIT pivot across 4 families (writer, vercel, pr-review-toolkit, oh-my-claudecode)
- O-P1-26 CDISC variable name spot-check: CPCNDAGT, CPRESTYP, CPTPTREF, CPRESSCL, CPRESTYP, CPMRKSTR, CPGATDEF, CPCAT all character-perfect in relevant atoms — 0 STUDIID/DALKID/HETSTESTCD-class errors detected
- NEW3 outer-pipe compliance: all TABLE_ROW atoms verified with leading and trailing pipe
- NEW6 sub-domain canonical form: 10/10 correct
- NEW7 L5 sib chain: 2/2 HEADING atoms correct (sib=3 Assumptions, sib=4 Examples)
- R6 CODE_LITERAL: 1/1 correct (atom 3, "SPECIMEN LOST")
- Batch 21 entirely within §6.3.5.3 CP per TOC anchor — no transition pages in p.201-210 range
