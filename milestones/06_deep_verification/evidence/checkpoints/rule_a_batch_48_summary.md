# Rule A Batch 48 Audit Summary

## Headline Metrics

- Sample size: 10 atoms (sv20 p.10-19, 1 atom/page, seed=20260502)
- Strict PASS: 10
- PARTIAL: 0
- FAIL: 0
- Weighted PASS rate: 100.0%
- Threshold met: YES (100.0% >= 80.0%)

## Per-Atom Verdict Table

| atom_id | page | atom_type | D1 verbatim | D2 atom_type | D3 parent_section | D4 HEADING fields | verdict |
|---|---:|---|---|---|---|---|---|
| sv20_p0010_a013 | 10 | LIST_ITEM | PASS | PASS | PASS | N/A | PASS |
| sv20_p0011_a031 | 11 | SENTENCE | PASS | PASS | PASS | N/A | PASS |
| sv20_p0012_a015 | 12 | TABLE_ROW | PASS | PASS | PASS | N/A | PASS |
| sv20_p0013_a007 | 13 | TABLE_ROW | PASS | PASS | PASS | N/A | PASS |
| sv20_p0014_a011 | 14 | TABLE_ROW | PASS | PASS | PASS | N/A | PASS |
| sv20_p0015_a015 | 15 | TABLE_ROW | PASS | PASS | PASS | N/A | PASS |
| sv20_p0016_a001 | 16 | TABLE_ROW | PASS | PASS | PASS | N/A | PASS |
| sv20_p0017_a001 | 17 | TABLE_ROW | PASS | PASS | PASS | N/A | PASS |
| sv20_p0018_a008 | 18 | TABLE_ROW | PASS | PASS | PASS | N/A | PASS |
| sv20_p0019_a005 | 19 | TABLE_ROW | PASS | PASS | PASS | N/A | PASS |

## Evidence Notes

- `sv20_p0010_a013`: PDF line 21 has the matching list item content under `§2.2 Table Structure` at line 8. The bullet marker is structural and stripped per established LIST_ITEM convention.
- `sv20_p0011_a031`: PDF lines 82-84 contain the exact sentence ending `The variable names include the specific domain prefix.` under `§3.1 The General Observation Classes` at line 56.
- `sv20_p0012_a015`: PDF lines 136-140 match row 10 `--STAT`; empty table cells and Notes-column placement are preserved by pipe canonicalization under `§3.1.1 The Interventions Observation Class`.
- `sv20_p0013_a007`: PDF lines 180-183 match row 19 `--DOSU`, including `--DOSE; --DOSTXT; --DOSTOT`, `C73558`, notes, and examples.
- `sv20_p0014_a011`: PDF lines 259-263 match row 35 `--PSTRGU`, including `--PSTRG`, `C117055`, `Unit for --PSTRG.`, and examples.
- `sv20_p0015_a015`: PDF lines 333-336 match row 8 `--HLT` under `§3.1.2 The Events Observation Class`.
- `sv20_p0016_a001`: PDF lines 347-350 match row 9 `--HLTCD`.
- `sv20_p0017_a001`: PDF lines 411-414 match row 22 `--SOCCD`.
- `sv20_p0018_a008`: PDF lines 517-521 match row 44 `--SDTH`, including the `Valid values are "Y", "N", and null.` Notes cell.
- `sv20_p0019_a005`: PDF lines 590-595 match row 51 `--RLPRT`, including the device-related procedure parenthetical and examples.

## Findings

No NEW HIGH/MEDIUM finding raised. Reserved IDs `O-P1-169`..`O-P1-172` remain unused for this audit.

## Borderline / NON_BLOCKING_OBS

None. The only convention-sensitive point is `sv20_p0010_a013`: the PDF bullet marker is not included in `verbatim`, consistent with the established LIST_ITEM marker-stripping convention and therefore not a blocker.

## Reviewer Slot Context

Slot #61 `codex:codex-rescue` codex-family 4th burn extension AUDIT pivot 42nd cumulative. D-MS-7 sister chain context retained. v1.7 N21 2nd cumulative + 1st in sv20 context retained.

## Production-Side Prevention Layer Validation

- Read-only production files used: `evidence/checkpoints/pdf_atoms_batch_48a.jsonl` and `evidence/checkpoints/pdf_atoms_batch_48b.jsonl`.
- Sample-file line count: 10 atoms.
- Production batch line counts: 48a = 92 atoms; 48b = 58 atoms.
- Sampled atom presence in production: all 10 located (`48a` lines 13, 47, 63, 72, 88; `48b` lines 15, 16, 29, 51, 58).
- Header/footer/date leak sweep on production atoms: 0 matches for `CDISC Study Data Tabulation Model (2.0 Final)`, copyright footer, or `2021-11-29`.
- Non-enum/fabricated atom_type sweep on production atoms: 0 matches for `SECTION_HEADING`, `PARAGRAPH`, `TABLE`, `BULLET`, `LIST`, or `TEXT`.

## Schema Sweep Cross-Reference

- Production: 0 schema errors per main-session sweep; this audit's sampled production atoms all use the frozen v1.2 9-enum (`LIST_ITEM`, `SENTENCE`, `TABLE_ROW`) correctly.
- Drift calibration artifact: 2 `atom_type` ENUM FABRICATION errors for `SECTION_HEADING`, which is not in the 9-enum. This is separate from the production-atoms audit here and does not affect batch 48 production Rule A verdicts.

## Final Verdict

PASS. Weighted PASS rate = 10.0 / 10 = 100.0%, meeting the >=80% Rule A threshold.
