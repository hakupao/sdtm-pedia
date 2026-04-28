# Rule A Batch 51 Summary

## 1. Method (sample selection + seed + 4-dim rubric)

- Reproduced the requested Python sampling logic with `random.seed(20260602)` across `.work/06_deep_verification/evidence/checkpoints/pdf_atoms_batch_51a.jsonl` and `pdf_atoms_batch_51b.jsonl`.
- Drew 10 atoms total: 1 atom from each sorted page, sv20 p.40 through p.49.
- Extracted page-local PDF ground truth with `pdftotext -layout -f <page> -l <page> source/SDTM_v2.0.pdf -`.
- Applied the 4-dimension rubric: `verbatim`, `atom_type`, `parent_section`, `schema` as PASS / PARTIAL / FAIL.
- Normalization applied only for PDF layout ambiguity: collapse whitespace runs, strip line edges, and join obvious line-wrap hyphenation such as `COVAL1-` + `COVALn`. For `TABLE_ROW`, pipe characters were treated as atom-schema cell delimiters; the page check verified exact cell text/digits in the extracted page row region because `pdftotext -layout` does not emit literal pipes.
- Schema check used the task-required fields plus frozen schema v1.2 properties from `.work/06_deep_verification/schema/atom_schema.json`; undeclared fields were treated invalid under the task clause `no extra invalid fields`.

## 2. Sample manifest (10 atom_ids + page distribution)

- sv20_p0040_a011 — page 40 — HEADING — §3.2.1 [Demographics]
- sv20_p0041_a007 — page 41 — TABLE_ROW — §3.2.1 [Demographics]
- sv20_p0042_a007 — page 42 — TABLE_ROW — §3.2.1 [Demographics]
- sv20_p0043_a011 — page 43 — TABLE_ROW — §3.2.1 [Demographics]
- sv20_p0044_a015 — page 44 — TABLE_ROW — §3.2.2 [Comments]
- sv20_p0045_a004 — page 45 — TABLE_ROW — §3.2.2 [Comments]
- sv20_p0046_a018 — page 46 — SENTENCE — §3.2.3.2 [Subject Repro Stages]
- sv20_p0047_a013 — page 47 — HEADING — §3.2.3 [Subject Summary Domains]
- sv20_p0048_a001 — page 48 — HEADING — §3.2.3.3 [Subject Visits]
- sv20_p0049_a009 — page 49 — TABLE_ROW — §3.2.3.4 [Subject Disease Milestones]

Page distribution: p40=1, p41=1, p42=1, p43=1, p44=1, p45=1, p46=1, p47=1, p48=1, p49=1.

## 3. Verdict matrix (table: atom_id x 4 dims x PASS/PARTIAL/FAIL)

| atom_id | page | verbatim | atom_type | parent_section | schema |
|---|---:|---|---|---|---|
| sv20_p0040_a011 | 40 | PASS | PASS | PASS | FAIL |
| sv20_p0041_a007 | 41 | PASS | PASS | PASS | PASS |
| sv20_p0042_a007 | 42 | PASS | PASS | PASS | PASS |
| sv20_p0043_a011 | 43 | FAIL | PASS | PASS | PASS |
| sv20_p0044_a015 | 44 | PASS | PASS | PASS | PASS |
| sv20_p0045_a004 | 45 | PASS | PASS | PASS | PASS |
| sv20_p0046_a018 | 46 | PASS | PASS | PASS | PASS |
| sv20_p0047_a013 | 47 | PASS | PASS | PASS | FAIL |
| sv20_p0048_a001 | 48 | PASS | PASS | PASS | FAIL |
| sv20_p0049_a009 | 49 | PASS | PASS | PASS | PASS |

## 4. PDF cross-check evidence (per-atom byte-exact comparison snippet for verbatim dim)

- `sv20_p0040_a011` PASS: p40 line 16 contains `Subject Demographics Domain Variables`; atom verbatim matches after whitespace normalization.
- `sv20_p0041_a007` PASS: p41 lines 56-59 contain row `13 DTHDTC Date/Time of Death ... C117450 ... database`; all atom cells match the page-local row text.
- `sv20_p0042_a007` PASS: p42 lines 33-41 contain row `20 AGETXT Age Text ... C170982 ... AGE or AGETXT`; line-wrap `number-` + `number` was normalized to `number-number`.
- `sv20_p0043_a011` FAIL: p43 lines 58-60 contain the start of row `37 DMDTC Date/Time of Collection ... demographic data collection,` but page 43 does not contain the atom tail `represented in a standardized character format.` That tail is only visible on the p44 continuation, so the atom is not byte-exact against its declared page text.
- `sv20_p0044_a015` PASS: p44 lines 49-50 contain row `7 COSEQ Sequence Number ... uniqueness within the dataset`; all atom cells match after layout normalization.
- `sv20_p0045_a004` PASS: p45 lines 18-21 contain row `11 COVAL Comment ... The text of the comment ... COVAL1-` plus `COVALn.`; hyphen line-wrap normalization yields the atom text.
- `sv20_p0046_a018` PASS: p46 lines 54-56 contain `Planned repro stages are described in the Trial Design Model (see Section 5.1.3.1, Trial Repro Stages).`; atom sentence matches after whitespace normalization.
- `sv20_p0047_a013` PASS: p47 line 43 contains `3.2.3.3 Subject Visits`; atom verbatim matches.
- `sv20_p0048_a001` PASS: p48 line 5 contains `Subject Visits—One Record per Subject Visit, per Subject`; atom verbatim matches.
- `sv20_p0049_a009` PASS: p49 lines 22-25 contain row `4 SMSEQ Sequence Number ... consistent with chronological order`; all atom cells match after layout normalization.

## 5. Weighted PASS% computation

- Max score: 10 atoms x 4 dimensions = 40.
- PASS counts: verbatim 9/10, atom_type 10/10, parent_section 10/10, schema 7/10.
- PARTIAL counts: 0 across all dimensions.
- FAIL counts: verbatim 1, schema 3.
- Weighted score: 36.0/40 = 90.0%.
- Threshold result: 90.0% is above the >=80% threshold, but halt still triggers because verbatim FAIL count is 1.

## 6. Findings filed (IDs O-P1-181..184 if any; mark unused if 0)

- O-P1-181: HALT-grade page-boundary verbatim failure in `sv20_p0043_a011`; declared page 43 atom includes text only present on page 44 continuation.
- O-P1-182: Schema-shape failure in sampled HEADING atoms `sv20_p0040_a011`, `sv20_p0047_a013`, and `sv20_p0048_a001`; each includes undeclared `heading_text` despite frozen schema v1.2 not defining that field. Batch-wide read-only scan found `heading_text` on 14/150 batch-51 atoms.
- O-P1-183: unused.
- O-P1-184: unused.

## 7. Halt analysis (threshold >=80% + halt-grade verbatim FAIL count)

- Weighted PASS% halt condition: not triggered (`90.0%` >= `80.0%`).
- Halt-grade verbatim condition: triggered (`1` verbatim FAIL).
- Disposition: HALT for batch 51 Rule A audit despite weighted score passing, because any verbatim FAIL is halt-grade under the task rubric.

## 8. Rule D compliance note (codex-family 5th burn extension AUDIT pivot 45th cumulative)

This was performed as an audit-only pivot for reviewer slot #64, codex-family 5th burn extension, AUDIT pivot 45th cumulative. The executor output was reviewed without atomization and without modifying the production atom JSONL files.

## 9. Rule A reflection on AUDIT-mode pivot (3-axis analogy per kickoff §9)

1. Cross-runtime independent reasoning mapped to page-local PDF ground-truth verification: the sample was checked against `pdftotext -layout` output rather than trusting executor reconstruction.
2. Diagnosis mapped to multi-axis issue separation: the halt-grade issue is a page-boundary verbatim overcapture, while the schema issue is an undeclared-field shape violation.
3. Handoff discipline mapped to the 4-dimension verdict matrix: every sampled atom received independent PASS/PARTIAL/FAIL verdicts for verbatim, atom_type, parent_section, and schema before disposition.
