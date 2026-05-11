# P4a Session S1 Report

> Date: 2026-05-11
> Session: S1 (batches 001–025)
> Status: COMPLETE
> Atoms processed: 2,500 / 12,487 (20.0%)

## Verdict Distribution

| Verdict | Count | % |
|---------|------|----|
| EXACT | 880 | 35.2% |
| EQUIVALENT | 733 | 29.3% |
| PARTIAL | 384 | 15.4% |
| MISSING | 263 | 10.5% |
| INTENTIONAL_EXCLUDE | 227 | 9.1% |
| MISPLACED | 10 | 0.4% |
| ERROR | 3 | 0.1% |
| **Total** | **2,500** | |

**Matched (EXACT + EQUIVALENT)**: 1,613 / 2,273 substantive atoms = **71.0%**
*(Excluding 227 INTENTIONAL_EXCLUDE from denominator)*

## Coverage Quality Summary

- **Batches 001–002** (200 atoms): 100% INTENTIONAL_EXCLUDE — §0 Cover/TOC, auto-classified by script
- **Batches 003–025** (2,300 atoms): AI agent processing
  - Highest coverage: §3 SDTM metadata tables, §4.x general assumptions, §4.1–4.4 model rules
  - Gaps identified: §5.1 CO spec table variable definitions, §5.2 DM spec table rows, §4.5.x sub-sections flattened into parent

## MISPLACED Atoms (10 total)

All 10 documented in `discrepancies.md`. Two structure drift clusters:

1. **§4.1.6–4.1.7.1** (3 atoms, ~10% rate) — borderline, monitor in S2
2. **§4.5.3.2–4.5.8** (7 atoms, ~14% rate) — **P4b STRUCTURE_DRIFTED flag** warranted; KB collapsed §4.5.x subsections into parent §4.5

## ERROR Atoms (3 total — requires KB correction in P4b)

| Atom | PDF value | KB value | Location |
|------|-----------|----------|----------|
| ig34_p0041_a024 | P14DT**7**H57M | P14DT**2**H57M | Duration example table |
| ig34_p0078_a021 | SEX=**M** | SEX=**F** | DM Example, USUBJID ABC789-010-047 |
| ig34_p0090_a002 | date 2020-03-05, DSSTDY=25 | date 2020-03-16, DSSTDY=28 | SV/DS example row 6 |

## Notable MISSING Patterns

- **CO domain** (§5.1): Spec table variable definitions (RDOMAIN, IDVAR, IDVARVAL, QVAL, QNAM, QLABEL) not captured in KB
- **DM domain** (§5.2): Spec table rows (STUDYID, DOMAIN, USUBJID, RFSTDTC, etc.) absent; only example tables present
- **Timing variables** (batch_015, ~34 MISSING): Narrative/example sentences for EPOCH, --STRTPT, --ENRTPT not in KB
- **SV domain** (batch_025, 26 MISSING): SV spec table entirely absent from KB
- **Sub-heading atoms**: Many "Example 1/2/3", "Row N:", "Rows 1–N:" heading atoms not captured as separate KB atoms

## Batch-by-Batch Highlights

| Batch | Notable |
|-------|---------|
| 003 | §0 TOC + §1 intro — good coverage |
| 008 | 3 MISPLACED (§4.1.6–4.1.7.1) |
| 013 | 1 ERROR: duration hours wrong (7H→2H) |
| 015 | ~34 MISSING: timing variable examples |
| 018 | 7 MISPLACED (§4.5.3.2–4.5.8 → §4.5) |
| 019 | 49 MISSING: CO spec table + DM spec table start |
| 021 | 33 MISSING: DM example sub-headings + RACEC subcodes |
| 023 | 1 ERROR: SEX=F vs SEX=M in DM Example |
| 025 | 26 MISSING: SV spec table; 1 ERROR: DS example dates |

## Post-S1 Actions Completed

- [x] `p4a_merge_ledger.py` → `coverage_ledger.jsonl` (2,500 entries)
- [x] Per-batch trace.json files consolidated (wrong-path files fixed)
- [x] `discrepancies.md` populated (10 MISPLACED + 3 ERROR)
- [x] `_progress.json` updated (S1_complete_2026-05-11)

## S2 Preparation

- Build batch_026–050 input files: `python3 scripts/p4a_build_batches.py --batches 26-50`
- S2 scope: batches 026–050 (2,500 atoms, pages ~82–??)
- Expected content: §5.2 DM continued, §5.3–§5.x domain specs
