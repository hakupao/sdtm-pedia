# Drift Cal Batch 27 p.270 Report (NEW1 dual-threshold, round 5 5th time)

> Status: **FAIL** (either <80%)
> Date: 2026-04-27
> Trigger: every-3-batches cadence batch 24→27 + cumulative atoms post-p.233 ≥600 (双触发 MANDATORY)
> NEW1 dual-threshold validated round 1+2+3+4 STRONGLY (4× consecutive); round 5 = 5th time

## Pair design
| Role | Subagent | File | Atoms |
|---|---|---|---|
| Baseline | sub-batch 27b executor | `pdf_atoms_batch_27b.jsonl` (filtered p.270) | 32 |
| Rerun | oh-my-claudecode:writer | `drift_cal_p270_writer_rerun.jsonl` | 45 |

Alternation: 27b baseline = executor → drift cal rerun = writer (per kickoff §6 alternation rule).

## NEW1 dual-threshold computation

| Metric | Value | Threshold | Verdict |
|---|---|---|---|
| Strict count match | 71.1% (32/45) | ≥80% | **FAIL** |
| Verbatim hash overlap | 6.7% (intersection 3/45) | ≥80% | **FAIL** |
| **Overall** | strict FAIL + verbatim FAIL | both ≥80% | **FAIL** |

## Direction analysis
- baseline-only atoms: 29 (27b executor, missing in writer rerun)
- rerun-only atoms: 42 (writer rerun, missing in 27b executor)
- common atoms: 3
- Direction inference: **writer-family drift (paraphrase / synonym / whitespace)**

## Type distribution comparison
| Type | Baseline (executor) | Rerun (writer) |
|---|---|---|
| CODE_LITERAL | 1 | 1 |
| HEADING | 1 | 1 |
| LIST_ITEM | 7 | 7 |
| SENTENCE | 2 | 5 |
| TABLE_HEADER | 1 | 1 |
| TABLE_ROW | 20 | 30 |

## Sample divergences

### baseline-only (executor wrote, writer didn't)
- ig34_p0270_a015 (TABLE_ROW): `3 | ABC-123 | PC | 123-0001 | 3 | Day 1 | A854134-11 | DRGA_MET | Drug A Metabolite | ANALYTE | URINE | <2 | ng/mL | <2 | | ng/mL | | 2.00 | 500 | 1 | DAY 1 | 1 | 2001-02-01T07:45 | 2001-02-01T07:45 |`
- ig34_p0270_a009 (LIST_ITEM): `Rows 17-20:	Show day 11 drug and metabolite concentrations in urine specimens collected over an interval. The elapsed times for urine samples are calculated as the elapsed time (from the reference tim`
- ig34_p0270_a012 (TABLE_HEADER): `Row | STUDYID | DOMAIN | USUBJID | PCSEQ | PCGRPID | PCREFID | PCTESTCD | PCTEST | PCCAT | PCSPEC | PCORRES | PCORRESU | PCSTRESC | PCSTRESN | PCSTRESU | PCSTAT | PCLLOQ | PCULOQ | VISITNUM | VISIT | `
- ig34_p0270_a032 (TABLE_ROW): `20 | ABC-123 | PC | 123-0001 | 20 | Day 11 | A854134-17 | PH | PH | SPECIMEN PROPERTY | URINE | 5.5 | | 5.5 | 5.5 | | | | | | 3 | DAY 11 | 11 | 2001-02-11T08:00 | 2001-02-11T14:03 | 11 | 6H | 6 | Day `
- ig34_p0270_a026 (TABLE_ROW): `14 | ABC-123 | PC | 123-0001 | 14 | Day 11 | A854134-15 | DRGA_PAR | Drug A Parent | ANALYTE | PLASMA | <0.1 | ng/mL | <0.1 | | ng/mL | | 0.10 | 20 | 3 | DAY 11 | 11 | 2001-02-11T07:45 | | 11 | PREDOS`

### rerun-only (writer wrote, executor didn't)
- ig34_p0270_a004 (SENTENCE): `It should be meaningful.`
- ig34_p0270_a045 (TABLE_ROW): `30 | ABC-123 | PC | 1223-001 | 30 | Day 11 | 1223-0111 | PH | Urine pH | SPECIMEN PROPERTY | URINE | 6.8 | | 6.8 | 6.8 | | | | | 2 | Day 11 | 11 | 1223-0111 | 1223-0111 | 0 | 9 | 24-48 | 24-48 hr |  |`
- ig34_p0270_a035 (TABLE_ROW): `20 | ABC-123 | PC | 1223-001 | 20 | Day 11 | 1223-0111 | METABOLITE A | Metabolite A Concentration | | URINE | 0.4 | µg | 0.4 | 0.4 | µg | | | | 2 | Day 11 | 11 | 1223-0111 | 1223-0111 | 0 | 7 | 0-8 |`
- ig34_p0270_a043 (TABLE_ROW): `28 | ABC-123 | PC | 1223-001 | 28 | Day 11 | 1223-0111 | METABOLITE A | Metabolite A Concentration | | URINE | 0.1 | µg | 0.1 | 0.1 | µg | | | | 2 | Day 11 | 11 | 1223-0111 | 1223-0111 | 0 | 9 | 24-48`
- ig34_p0270_a006 (SENTENCE): `In this example, such values for PCTPTREF are required to make values of PCTPTNUM and PCTPT unique (see Section 4.4.10, Representing Time Points).`

## Action
- **Repair decision pending**: strict count <80%/verbatim hash <80% — DIRECTION = writer-family drift (paraphrase / synonym / whitespace).
- DIRECTION REVERSED 9th precedent if writer-family drift confirmed (round 4 batch 24 p.233 was 8th).
- Drift cal value-add: caught divergence dual-threshold spec is designed to surface.
- Findings filed: O-P1-84 HIGH/MEDIUM (drift cal NEW1 strict count <80%+verbatim hash <80%; writer-family drift motif if direction-reversed).

## v1.3 cut implication
- NEW1 dual-threshold round 5 5th time validation: FAIL continues evidence saturation.
- v1.3+ NEW8.b SENTENCE-trigram extension mandatory.
