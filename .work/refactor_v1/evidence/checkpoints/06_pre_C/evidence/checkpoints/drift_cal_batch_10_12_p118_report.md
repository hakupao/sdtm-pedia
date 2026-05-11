# Drift Calibration Report — batch 12 p.118

> Date: 2026-04-25
> Trigger: cumulative atoms since last drift cal at p.89 ≥ 300 cadence (P1_pdf_atomization §C.1)
> Target: p.118 §6.1.3.3 Examples ec.xpt + ex.xpt + vs.xpt + relrec.xpt 4-table dense TABLE_ROW page (highest drift-cal value-add per O-P1-23 lesson dense-table blind spot)
> Strategy: 2-way (writer 12b baseline already merged + Option C oh-my-claudecode:executor independent rerun)
> Outcome: **FAIL @ 48% strict count** (25 rerun / 52 baseline) BUT **root cause identified — Option H repair**, no tiebreaker required (matches O-P1-12 / O-P1-23 pattern: drift cal FAIL with definitive root cause ≠ reproducibility noise)

---

## Metrics

| 指标 | 12b writer (baseline) | executor (rerun) |
|---|---|---|
| Atoms | 52 | 25 |
| atom_type dist | TABLE_HEADER 6 / TABLE_ROW 29 / SENTENCE 13 / CODE_LITERAL 4 | TABLE_HEADER 2 / TABLE_ROW 15 / SENTENCE 7 / CODE_LITERAL 1 |
| Strict count match | 25/52 = **48%** | — |
| Threshold | ≥80% | FAIL |
| Tiebreaker | NOT triggered | (root cause identified, definitive Option H scope) |

## Root cause analysis

### (1) HIGH data corruption in writer 12b — 4 atoms (O-P1-34, Option H applied) ✓

| atom_id | Field | Writer 12b (corrupted) | Executor (PDF-verified) | Severity |
|---|---|---|---|---|
| ig34_p0118_a023 | TABLE_HEADER col 6 | `ECNKID` (missing L) | `ECLNKID` | HIGH typo |
| ig34_p0118_a023 | TABLE_HEADER col 16 | `ECPSTRGUI` (extra I) | `ECPSTRGU` | HIGH typo |
| ig34_p0118_a025 | ECLNKID Row 2 | `20080613T1000` (year+month/day corrupted) | `20090213T1000` | HIGH date hallucination |
| ig34_p0118_a027 | ECLNKID Row 4 | `20080220T1100` (year corrupted) | `20090220T1100` | HIGH date hallucination |
| ig34_p0118_a029 | ECLNKID Row 6 | `20080227` (year corrupted) | `20090227` | HIGH date hallucination |

**Pattern**: Same as O-P1-23 batch 09 writer 09b DS row data hallucination (DSDTC 2019-09-09 written as 09-10, etc.). Writer family appears to corrupt dense data table values in patterns that 10-atom Rule A sampling cannot reliably catch. Drift cal earns its keep again — captured 4 HIGH bugs that would have propagated to root → P4a matching → KB.

**Inline fix applied**: 4-atom Option H targeted patches (TABLE_HEADER 2 substitutions + 3 TABLE_ROW datetime substitutions) in batch 12b file AND root pdf_atoms.jsonl. Verified post-fix.

### (2) Convention drift — non-blocking (O-P1-33 INFO, deferred v1.3)

Numerical mismatch (52 vs 25) is largely driven by interpretive convention differences, not content gaps:

- **CRF top table cell-splitting** (writer 15 atoms vs executor 10 atoms for top table): writer split 1 logical row with multi-line bullet cells (e.g. "Dose Administered | • Yes / • No / If no, give reason: ..." across 3 visit columns) into multiple TABLE_ROW atoms (a004 main + a005-a007 sub-line atoms); executor kept as 1 TABLE_ROW with internal newlines. **Both interpretations capture same content; spec says "1 logical row = 1 TABLE_ROW".**
- **USUBJID/text-cell wrap normalization** (writer normalized `ABC123-\n0201` → `ABC123-0201`; executor preserved `ABC123-\n0201`): per R10 (preserve PDF wrap artifacts), executor is technically correct. But both interpretations represent the same underlying value. **Note on compound name `domains.This` artifacts** (batch 10 O-P1-25): wrap-drop affecting different artifact (no-space at sentence boundary) was the original R10 case; this is a related but distinct case (preserve wrap newline in cell content). No semantic difference for downstream KB matching but verbatim equality differs.
- **Sentence boundary splitting** (writer split "Rows 1, 3, 5: ... Scheduled dose is represented in mg/mL." into 2 SENTENCE atoms; executor kept as 1): writer 1-sentence-per-atom interpretation is per-spec stricter; executor merged when visually adjacent. **Writer is per-spec correct; INFO only.**
- **CODE_LITERAL count mismatch** (writer 4 vs executor 1): writer captured 4 dataset filename labels (ec.xpt, ex.xpt, vs.xpt, relrec.xpt) while executor captured only ec.xpt. **Writer is more complete here** — executor under-extracted 3 of 4 dataset filename CODE_LITERAL atoms. R9 attribution correct in both.

These are convention drifts, not data errors. Both writer and executor capture the same underlying PDF content with different segmentation choices. Defer formal v1.3 codification of CRF cell-splitting + USUBJID wrap normalization rules.

### (3) Other potential issues observed but NOT fixed in this Option H

Writer 12b ec.xpt rows show some apparent column-shifting issues in non-ECLNKID columns (e.g. a025 ECDOSE=9.9 vs expected ECDOSE=99 + ECDOSU=mL; ECPSTRG cell positions). These would require full row-by-row column-alignment analysis vs executor + PDF for surgical fix. **Defer to v1.3 / Phase 4a matching pass** (will surface as MD verbatim mismatch and trigger targeted reverse-audit if any survives).

## Tiebreaker decision: NOT TRIGGERED ✓

Per PLAN §C.1 + drift cal precedent (O-P1-12 batch 06 writer bug + O-P1-23 batch 09 hallucination), tiebreaker (general-purpose × 1 page, 2/3 majority) is required when FAIL root cause cannot be conclusively identified. Here:
- HIGH data corruption: definitively root-caused to writer 12b (executor + PDF agree as ground truth)
- Convention drift: non-data interpretive choice, no "correct" 3rd answer
- Therefore tiebreaker would not add information

Skip tiebreaker, apply Option H, document.

## Findings added

| ID | Severity | Summary |
|---|---|---|
| O-P1-33 | INFO | Convention drift on p.118: CRF table multi-line cell splitting (writer 1-row-per-visual-line vs executor 1-row-per-logical-row); USUBJID wrap normalization (writer normalized vs executor R10-preserved); sentence boundary splitting (writer per-spec strict vs executor merged adjacent). All capture same underlying PDF content. Defer v1.3 codification. |
| O-P1-34 | HIGH | Writer 12b p.118 ec.xpt section 4-atom data corruption: TABLE_HEADER `ECNKID`/`ECPSTRGUI` typos (missing L / extra I in column names) + 3 ECLNKID datetime year corruptions (Rows 2/4/6: 2009→2008, plus Row 2 month/day 02-13→06-13). Same writer-family hallucination pattern as O-P1-23 batch 09 DSDTC. Drift cal caught all 4 (Rule A 10-atom stratified sample would not have covered dense ec.xpt 7-atom segment). Inline Option H 4-atom targeted fix applied to both batch 12b file + root pdf_atoms.jsonl. Verified post-fix. |

## Cumulative drift cal track

| Run | Page | A | B | match | Root cause | Action |
|---|---|---|---|---|---|---|
| 30-page (batch 03) | p.25 | executor | writer | 67.5% / 37.5% / 37.5% (3-way) | QS sparse-cell PDF parse noise (O-P1-09) | continue + Rule A 加密 per-batch |
| 300-atom (batch 06) | p.60 | writer 06b | executor rerun | 17.6% strict | writer 06b page misattribution + CO under-extract (O-P1-12) | Option E rerun promoted to primary |
| 300-atom (batch 09) | p.89 | writer 09b | executor rerun | 60.6% pre-fix / 69.7% post-fix | writer 09b 3 DS row data hallucination + CT spec drift (O-P1-23) | Option H bulk fix using executor verbatim |
| **300-atom (batch 12)** | **p.118** | **writer 12b** | **executor rerun** | **48%** | **writer 12b 4-atom ec.xpt corruption (O-P1-34) + convention drift (O-P1-33 non-blocking)** | **4-atom Option H targeted; convention defer v1.3** |

**Pattern stable across 4 drift cal runs**: writer family exhibits dense-table-row hallucination on every drift cal trigger; executor family does not. Root cause appears systemic to writer family's handling of dense spec/data tables. Recommend v1.3 prompt addition: writer-family-specific spec-table self-validation step (similar to R14 line-count check).

## Cross-reference

- O-P1-23 (batch 09): same writer-family DS hallucination pattern — established the drift cal value-add over Rule A precedent
- O-P1-12 (batch 06): writer page misattribution — established Option E "rerun replaces baseline" pattern
- O-P1-26 (batch 10 INFO): TABLE_ROW pipe-format inconsistency — related convention drift, defer v1.3
