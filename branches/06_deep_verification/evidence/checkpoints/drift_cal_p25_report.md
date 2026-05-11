# Drift Calibration p.25 — batch 03 executor vs writer re-run

> Date: 2026-04-24
> Baseline: `pdf_atoms.jsonl` p.25 atoms from batch 03 (writer = oh-my-claudecode:executor)
> Re-run: `evidence/checkpoints/drift_cal_p25_writer_rerun.jsonl` (writer = oh-my-claudecode:writer, model=sonnet, independent read)
> Both: ≤1 page Read, prompt version P0_writer_pdf_v1.2+drift_cal_p25 / +batch03_4digit_fix
> Threshold: ≥ 80% (PLAN §9.1 P1 drift-calibration)

## Result

| Metric | Baseline | Re-run |
|---|---|---|
| Atoms | 40 | 40 |

### Agreement scores

| Level | Matches | Symmetric agreement | Verdict |
|---|---|---|---|
| **Strict** (atom_type + verbatim exact) | 27 | **67.5%** | **FAIL** |
| Loose (whitespace/case normalized) | 27 | 67.5% | — |
| Verbatim-only (text match, type-agnostic) | 27 | 67.5% | — |

### atom_type distribution comparison

| type | baseline | rerun | delta |
|---|---|---|---|
| CODE_LITERAL | 4 | 4 | +0 |
| HEADING | 6 | 6 | +0 |
| TABLE_HEADER | 4 | 4 | +0 |
| TABLE_ROW | 26 | 26 | +0 |

## Mismatches (verbatim level)

Only in baseline: 13
Only in re-run: 13

### Atoms only in baseline (batch 03 executor saw, writer missed)
- `1 | CDISC01 | QS | CDISC01.100008 | | SWLS0101 | SWLS01-My Life is Close to Ideal | SWLS | Slightly agree | 5 | 5 | Y | 1 | 2003-04-15 | 1`
- `10 | CDISC01 | QS | CDISC01.100014 | | SWLS0105 | SWLS01-Live Life Over Change Nothing | SWLS | Strongly disagree | 1 | 1 | | 1 | 2003-04-15 | 1`
- `2 | CDISC01 | QS | CDISC01.100008 | 2 | CGI0201 | CGI02-Severity | CGI | Mild | 3 | 3 | | | WEEK 2 | 7 | 2003-04-21 | 7`
- `2 | CDISC01 | QS | CDISC01.100008 | | SWLS0102 | SWLS01-My Life Conditions are Excellent | SWLS | Neither agree nor disagree | 4 | 4 | Y | 1 | 2003-04-15 | 1`
- `3 | CDISC01 | QS | CDISC01.100008 | | SWLS0103 | SWLS01-I Am Satisfied with My Life | SWLS | Agree | 6 | 6 | | 1 | 2003-04-15 | 1`
- `4 | CDISC01 | QS | CDISC01.100008 | | SWLS0104 | SWLS01-Have Gotten Important Things | SWLS | Disagree | 2 | 2 | | 1 | 2003-04-15 | 1`
- `5 | CDISC01 | QS | CDISC01.100008 | | SWLS0105 | SWLS01-Live Life Over Change Nothing | SWLS | Strongly disagree | 1 | 1 | | 1 | 2003-04-15 | 1`
- `6 | CDISC01 | QS | CDISC01.100014 | 2 | CGI0201 | CGI02-Severity | CGI | Mild | 3 | 3 | | 2 | WEEK 2 | 7 | 2003-04-21 | 7`
- `6 | CDISC01 | QS | CDISC01.100014 | | SWLS0101 | SWLS01-My Life is Close to Ideal | SWLS | Slightly agree | 5 | 5 | Y | 1 | 2003-04-15 | 1`
- `7 | CDISC01 | QS | CDISC01.100014 | | SWLS0102 | SWLS01-My Life Conditions are Excellent | SWLS | Neither agree nor disagree | 4 | 4 | | 1 | 2003-04-15 | 1`
- `8 | CDISC01 | QS | CDISC01.100014 | | SWLS0103 | SWLS01-I Am Satisfied with My Life | SWLS | Agree | 6 | 6 | | 1 | 2003-04-15 | 1`
- `9 | CDISC01 | QS | CDISC01.100014 | | SWLS0104 | SWLS01-Have Gotten Important Things | SWLS | Disagree | 2 | 2 | | 1 | 2003-04-15 | 1`
- `Row | STUDYID | DOMAIN | USUBJID | QSSEQ | QSTESTCD | QSTEST | QSCAT | QSSCAT | QSORRES | QSSTRESU | QSSTRESC | QSSTRESN | QSTRESU | QSLOC | QSMETHOD | QSLOBXFL | VISITNUM | QSDTC | QSDY | QSEVLINT`

### Atoms only in re-run (writer saw, executor missed)
- `1 | CDISC01 | QS | CDISC01.100008 | 1 | SWLS0101 | SWLS01-My Life is Close to Ideal | SWLS | Slightly agree | 5 | | Y | 1 | 2003-04-15 | 1`
- `10 | CDISC01 | QS | CDISC01.100014 | 10 | SWLS0105 | SWLS01-Live Life Over Change Nothing | SWLS | Strongly disagree | 1 | | | | 2003-04-15 | 1`
- `2 | CDISC01 | QS | CDISC01.100008 | 2 | CGI0201 | CGI02-Severity | CGI | Mild | 3 | | | 2 | WEEK 2 | 7 | 2003-04-21 | 7`
- `2 | CDISC01 | QS | CDISC01.100008 | 2 | SWLS0102 | SWLS01-My Life Conditions are Excellent | SWLS | Neither agree nor disagree | 4 | | Y | | 2003-04-15 | 1`
- `3 | CDISC01 | QS | CDISC01.100008 | 3 | SWLS0103 | SWLS01-I Am Satisfied with My Life | SWLS | Agree | 6 | | | | 2003-04-15 | 1`
- `4 | CDISC01 | QS | CDISC01.100008 | 4 | SWLS0104 | SWLS01-Have Gotten Important Things | SWLS | Disagree | 2 | | | | 2003-04-15 | 1`
- `5 | CDISC01 | QS | CDISC01.100008 | 5 | SWLS0105 | SWLS01-Live Life Over Change Nothing | SWLS | Strongly disagree | 1 | | | | 2003-04-15 | 1`
- `6 | CDISC01 | QS | CDISC01.100014 | 2 | CGI0201 | CGI02-Severity | CGI | Mild | 3 | | | 2 | WEEK 2 | 7 | 2003-04-21 | 7`
- `6 | CDISC01 | QS | CDISC01.100014 | 6 | SWLS0101 | SWLS01-My Life is Close to Ideal | SWLS | Slightly agree | 5 | | Y | 1 | 2003-04-15 | 1`
- `7 | CDISC01 | QS | CDISC01.100014 | 7 | SWLS0102 | SWLS01-My Life Conditions are Excellent | SWLS | Neither agree nor disagree | 4 | | Y | | 2003-04-15 | 1`
- `8 | CDISC01 | QS | CDISC01.100014 | 8 | SWLS0103 | SWLS01-I Am Satisfied with My Life | SWLS | Agree | 6 | | | | 2003-04-15 | 1`
- `9 | CDISC01 | QS | CDISC01.100014 | 9 | SWLS0104 | SWLS01-Have Gotten Important Things | SWLS | Disagree | 2 | | | | 2003-04-15 | 1`
- `Row | STUDYID | DOMAIN | USUBJID | QSSEQ | QSTESTCD | QSTEST | QSCAT | QSSCAT | QSORRES | QSORRESU | QSSTRESC | QSSTRESN | QSSTRESU | QSLOC | QSMETHOD | QSLOBXFL | VISITNUM | QSDTC | QSDY | QSEVLINT`

## Verdict: **FAIL** (strict 67.5% vs threshold 80%)

**Drift 校准 FAIL**: 一致率 < 80%, 需调查原因 (prompt 不同理解 / atom 粒度差异 / verbatim normalization 等). 派 general-purpose 作 tiebreaker 样本, 或回炉 prompt.
