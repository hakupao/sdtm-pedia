# Drift Cal Batch 24 p.233 Report (NEW1 dual-threshold)

> Status: **FAIL** (verbatim FAIL <80%) — DIRECTION REVERSED 8th precedent (writer-family motif)
> Date: 2026-04-26
> Trigger: every-3-batches cadence batch 21→24 + cumulative atoms post-p.205 ≥300 (双触发 MANDATORY)

## Pair design
| Role | Subagent | File | Atoms |
|---|---|---|---|
| Baseline | sub-batch 24a executor | `pdf_atoms_batch_24a.jsonl` (filtered p.233) | 32 |
| Rerun | oh-my-claudecode:writer | `drift_cal_p233_writer_rerun.jsonl` | 34 |

Alternation: 24a baseline = executor → drift cal rerun = writer (per kickoff §7 alternation rule).

## NEW1 dual-threshold computation

| Metric | Value | Threshold | Verdict |
|---|---|---|---|
| Strict count match | 94.1% (32/34) | ≥80% | **PASS** |
| Verbatim hash overlap | 41.2% (intersection 14/34) | ≥80% | **FAIL** |
| **Overall** | strict PASS + verbatim FAIL | both ≥80% | **FAIL** |

## Direction check (which side is correct)

- baseline-only atoms: 18 (24a executor)
- rerun-only atoms: 20 (writer rerun)

**Sample divergences** (writer rerun semantic-drifted vs baseline executor):

| Baseline (24a executor) | Rerun (writer) | Drift type |
|---|---|---|
| `In order to illustrate the distinctive differences...` | `In order to distinguish the distinctive differences...` | "illustrate" → "distinguish" SEMANTIC drift |
| `The samples that are positive for ADA in both the screen and confirm tests...` | `This frequently includes analysis of antibody titer and neutralization...` | Wholesale paraphrase rather than verbatim |
| `Row 1:     Shows the screening...` (5 spaces preserved) | `Row 1: Shows the screening...` (1 space) | whitespace normalization |
| `These values help to describe the operational objective or the test purpose.` | `These values help to describe the operational objective or the test purpose.` | (matched) |
| `The study drug AZ-007, which induces the subject's production of antibodies...` | (rerun rephrased differently) | SEMANTIC drift |
| `ISGRPID is used in this example to show that the records are related...` | (rerun rephrased) | SEMANTIC drift |

## Root cause
Writer-family R10 verbatim drift on SENTENCE atoms (paraphrase / synonym substitution / whitespace normalization). Baseline executor reads PDF char-by-char and copies verbatim; writer rerun appears to re-summarize. Joins motif precedents O-P1-23/34/36/46 (writer-family R10 verbatim drift on SENTENCE/LIST_ITEM atoms — distinct from wide-TABLE_ROW corruption O-P1-23/37/38/50/63 which writer-family also exhibits).

## Action
- **NO root file repair needed**: baseline 24a executor is correct, root inherits 24a executor verbatim via reconciler merge.
- DIRECTION REVERSED 8th precedent (post round 3 batch 21 7th).
- Drift cal value-add 9th precedent (drift cal caught writer-family SENTENCE/LIST_ITEM verbatim drift that NEW2 single-char iteration misses).
- Findings filed: O-P1-72 MEDIUM (drift cal NEW1 verbatim FAIL writer-family motif).

## v1.4 candidate
- NEW8.b extension: extend NEW8 substring n-gram cross-check to SENTENCE-level paraphrase detection (currently NEW8 only catches `[A-Z]{3,}` variable name char-swap; expand to whole-SENTENCE trigram comparison vs baseline).
- Alternative: writer-family R10 strict no-paraphrase prepend re-emphasis (already in v1.2 — but writer family ignores it for SENTENCE atoms; needs char-level pre-DONE self-validation hook for SENTENCE atoms similar to NEW2 for variable names).

## Scoring vs spec
- Strict count: 94.1% PASS — close enough to be FALSE POSITIVE on count alone. Verbatim hash catches semantic drift.
- This is exactly the pattern NEW1 dual-threshold was designed to detect (round 1 +round 2 + round 3 STRONGLY VALIDATED + round 4 4th time validated).
- Drift cal NEW1 dual-threshold STRONGLY VALIDATED 4th time (round 1+2+3+4) — strictly count-based threshold misses verbatim drift.
