# Drift Cal Batch 33 p.325 Report (NEW1 dual-threshold, round 7 7th time)

> Status: **FAIL** (verbatim 42.9% — distorted by structural offset; substantive R10 hallucinations underlie)
> Date: 2026-04-28
> Trigger: every-3-batches cadence batch 30→33 + cumulative atoms post-p.293 ≥600 (双触发 MANDATORY)
> NEW1 dual-threshold validated 6 prior rounds (PASS×1 round 3 / FAIL×5 round 1+2+4+5+6) → round 7 7th time = STRICT ALTERNATION ENFORCED per O-P1-99 round 6 mandate (baseline=executor → rerun=writer per round 6 G-MS-NEW-6-2 codification)

## Pair design

| Role | Subagent | File | Atoms |
|---|---|---|---|
| Baseline | sub-batch 33a `oh-my-claudecode:executor` | `pdf_atoms_batch_33a.jsonl` (filtered p.325) | 20 |
| Rerun | `oh-my-claudecode:writer` (STRICT ALTERNATION ENFORCED) | `drift_cal_p325_writer_rerun.jsonl` | 21 |

**Strict alternation enforcement working as designed** (round 6 G-MS-NEW-6-2 codification VALIDATED 1st live-fire round 7): Round 6 batch 30 used executor for BOTH baseline + rerun → corrupted alternation test → became intra-family non-determinism probe. Round 7 batch 33 enforced strict alternation (baseline=executor → rerun=writer per table) → cleanly disentangles cross-family drift signal from intra-family non-determinism.

## NEW1 dual-threshold computation

| Metric | Value | Threshold | Verdict |
|---|---|---|---|
| Strict count match | 95.2% (20/21) | ≥80% | **PASS** |
| Verbatim hash overlap | 42.9% (9/21 unique hashes) | ≥80% | **FAIL** |
| Per-atom_id verbatim exact match | 0% (0/21 same id same content) | n/a | (informational — distorted by 1-atom structural offset cascading through all atom_ids) |
| **Overall** | strict PASS + verbatim FAIL | both ≥80% | **FAIL** |

## Direction analysis

- Baseline-only verbatim hashes (33a executor wrote, rerun didn't): 11
- Rerun-only verbatim hashes (rerun wrote, 33a didn't): 12
- Common verbatim hashes: 9

**Direction = writer-direction main-line VALUE HALLUCINATION** (3rd cumulative recurrence post round 5 O-P1-85 + round 6 batch 31 O-P1-103):

1. **Writer rerun ADDED phantom TABLE_HEADER atom (a001)** — 1-atom structural offset cascading through all subsequent atom_ids. Debatable defensibility: PDF p.325 DOES have column header repeat at top because qs.xpt spec table continues from p.324; baseline executor SKIPPED this header (treating p.325 as pure continuation); writer rerun ATOMIZED it (adding new TABLE_HEADER). Both choices defensible per round 4 v1.4 candidate NEW8.c TABLE_HEADER column-set.

2. **Writer rerun VARIABLE NAME TRUNCATION**: a002 verbatim "QSORRES | Original Units" — should be "QSORRESU | Original Units" per PDF + canonical CDISC variable list. Writer dropped trailing 'U' → HALLUCINATED non-canonical QSORRES (which exists but means "Finding in Original Units", different variable on p.324). Equivalent to round 6 batch 31 O-P1-101 OESEQ→OESEO Q→O Latin-Latin adjacent-key swap motif (round 7 = STILL UNCAUGHT by NEW8 substring n-gram self-validation since QSORRES IS canonical QS variable — context-aware NEW8 oracle expansion needed per round 6 v1.4 candidate G-MS-NEW-6-5).

3. **Writer rerun PARAPHRASE**: "Character Result/Finding in Std Format" (PDF/baseline) → "Standardized Result/Finding in Std Format" (rerun). R10 strict no-paraphrase violation. Joins round 4 batch 24 SENTENCE wholesale paraphrase + round 5 O-P1-85 VALUE HALLUCINATION cumulative motif.

4. **Writer rerun ROLE HALLUCINATION**: a005 "QSSTRESU | ... | Variable Qualifier" PDF/baseline = "Variable Qualifier" → rerun "Result Qualifier". R10 strict + per-table-context coherence (round 6 v1.4 candidate G-MS-NEW-6-7 NEW8.d multi-axis whole-row).

DIRECTION REVERSED 11th precedent (round 5 was 9th writer-direction; round 6 was 10th rerun-direction; round 7 batch 33 reverts to 11th writer-direction main-line — confirms strict alternation methodology disentangles cross-family signal from intra-family non-determinism).

## Type distribution comparison

| Type | Baseline (33a executor) | Rerun (writer) |
|---|---|---|
| TABLE_HEADER | 0 | 1 |
| TABLE_ROW | 20 | 20 |

Type distribution differs by 1 atom (writer rerun added TABLE_HEADER continuation header). All 20 TABLE_ROW atoms present in both; cross-family content drift in their verbatim contents.

## Sample divergences

(See drift_cal_p325_writer_rerun.jsonl raw file + earlier compare output for full 5+ representative divergences.)

## Action

- **Repair decision**: NO Option H needed for batch 33 root atoms (root unaffected — drift cal probe operates on rerun jsonl, not 33a baseline). Baseline 33a TABLE_ROW values judged CORRECT per PDF ground truth (QSORRESU canonical variable name + Variable Qualifier role + Character Result/Finding label); rerun writer judged INCORRECT (HALLUCINATED QSORRES truncation + Result Qualifier role + Standardized paraphrase).
- **Safety net validated**: drift cal probe surfaced systematic writer-family VALUE HALLUCINATION + variable name truncation + role swap that would NOT have been caught by Rule A 1/page sample (sample atom_id depending on seed may or may not include p.325 a002/a005).
- **Strict alternation methodology validated**: round 6 G-MS-NEW-6-2 codification mandate VALIDATED 1st live-fire round 7 — clean disentanglement of cross-family writer-vs-executor drift signal.
- **Findings filed**: O-P1-109 HIGH (drift cal NEW1 7th time FAIL — verbatim 42.9% / strict 95.2% / direction REVERSED 11th writer-direction + 3rd cumulative main-line writer-direction VALUE HALLUCINATION recurrence post round 5 O-P1-85 + round 6 batch 31 O-P1-103).

## v1.4 cut implication (cumulative agenda)

- **NEW1 dual-threshold round 7 7th time validation**: FAIL on combined writer-direction multi-axis (variable name truncation + paraphrase + role hallucination + structural TABLE_HEADER addition). Pattern: NEW1 spec catches multiple distinct writer/executor failure modes (Cyrillic / paraphrase / N-drop / SENTENCE-paraphrase / VALUE-HALLUCINATION / cell-drop / variable-name-truncation). Spec retain unchanged at v1.4.
- **NEW round-7 v1.4 candidate**: G-MS-NEW-7-1 — strict alternation enforcement methodology VALIDATED 1st live-fire round 7. Continue codifying alternation table in kickoff §6 procedurally enforced in main session dispatch.
- **v1.4 candidates confirmed from round 6**: NEW8 oracle expansion canonical SUPPQUAL Identifier set (G-MS-NEW-6-5 = catches QSORRES truncation only with context-aware oracle); NEW8.d multi-axis whole-row TABLE_ROW value-cell verbatim integrity (G-MS-NEW-6-7 = catches Role hallucination via per-table-context coherence).

## Comparison to prior 6 drift cals

| Round | Batch | Page | Strict | Verbatim | Verdict | Motif | Direction |
|---|---|---|---|---|---|---|---|
| 1 | 15 | 147 | 97.4% | 41% | FAIL | Cyrillic homoglyph + variable swap | writer |
| 2 | 18 | 180 | 100% | 69.6% | FAIL | DALNKID/DALNKGRP N-drop + paraphrases | writer |
| 3 | 21 | 205 | 100% | 94.1% | PASS | (CPSCMRKS char-swap caught by NEW2 limitation, but PASS overall) | writer |
| 4 | 24 | 233 | 94.1% | 41.2% | FAIL | writer-family SENTENCE wholesale paraphrase | writer |
| 5 | 27 | 270 | 71.1% | **6.7% LOWEST** | FAIL | writer-family VALUE HALLUCINATION (CATASTROPHIC) | writer |
| 6 | 30 | 293 | 100% | 45.0% | FAIL | rerun-side TABLE_ROW empty-cell drop intra-family non-determinism (NEW MOTIF) | rerun |
| **7** | **33** | **325** | **95.2%** | **42.9%** | **FAIL** | **writer-family VALUE HALLUCINATION 3rd cumulative + variable name truncation + role swap + phantom TABLE_HEADER** | **writer** |

6/7 drift cals FAIL on dual-threshold (only round 3 PASSED). NEW1 spec validates 7 distinct failure modes — robust. Round 7 strict alternation enforcement validates clean disentanglement.
