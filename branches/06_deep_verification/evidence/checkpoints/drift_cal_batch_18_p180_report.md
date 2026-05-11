# Drift Calibration Report — batch 18 p.180 (Multi-Session Parallel Round 2 Session C)

> Date: 2026-04-26
> Trigger: every-3-batches cadence (last cal batch 15 p.147) + cumulative atoms ≥300 since p.147 (双触发 mandatory per kickoff)
> Target: p.180 §6.3 Models for Findings Domains chapter-level transition + §6.3.1 Product Accountability (DA) start (densest TABLE_ROW value-add page in 18b — chapter-level + 15 spec rows + 4 HEADING + dropdown CT cluster)
> Strategy: 2-way (executor 18b baseline 23 atoms + Option C oh-my-claudecode:writer independent rerun 23 atoms)
> Outcome: **Strict count 100% (23/23) PASS @ ≥80% threshold; verbatim hash overlap 69.6% (16/23) FAIL @ ≥80% threshold → NEW1 dual-threshold FAIL → triggered root cause analysis revealing writer-family rerun verbatim drift across 7 atoms (NOT baseline 18b errors — DIRECTION REVERSED from prior drift cal precedents)**

---

## Metrics

| 指标 | 18b executor (baseline) | writer (rerun) |
|---|---|---|
| Atoms | 23 | 23 |
| atom_type dist | HEADING 4 / TABLE_ROW 15 / TABLE_HEADER 1 / SENTENCE 2 / CODE_LITERAL 1 | HEADING 4 / TABLE_ROW 15 / TABLE_HEADER 1 / SENTENCE 2 / CODE_LITERAL 1 |
| Strict count match | 23/23 = **100%** | — |
| Verbatim hash set overlap | 16/23 = **69.6%** | 16/23 = 69.6% |
| 4-dim verdict | atom_type 23/23 ✓ / parent_section 23/23 ✓ / heading_level+sib 4/4 HEADINGs ✓ / verbatim 16/23 FAIL | — |
| NEW1 dual-threshold | strict PASS / verbatim FAIL → **DUAL FAIL** | — |
| Tiebreaker | NOT triggered (root cause definitive — writer-family rerun verbatim drift, baseline accurate per PDF) | — |

## Root cause analysis

### Direction REVERSED from prior precedents (NEW lesson)

Prior drift cal precedents (batch 06 p.60 / batch 09 p.89 / batch 12 p.118 / batch 15 p.147) all surfaced **writer baseline bugs** caught by **executor rerun**. Batch 18 p.180 reverses this:

- **Baseline executor 18b**: PDF-accurate verbatim across all 23 atoms
- **Rerun writer**: introduced 7-atom verbatim drift cluster

This validates the dispatch decision (chose executor for 18b spec-table-dense pages) and adds a new finding pattern: **writer family is unreliable for dense Findings spec tables in either baseline or rerun role**.

### 7-atom writer-family verbatim drift cluster (per PDF p.180 cross-check by main session)

| atom_id | Variable | Drift type | BASE 18b (PDF-correct) | RERUN writer (drift) |
|---|---|---|---|---|
| a0012 | DASEQ | CDISC Notes paraphrase | `Sequence number given to ensure uniqueness...` | `Number used to ensure uniqueness...` |
| a0016 | DALNKID | Variable name typo | `DALNKID` | `DALKID` (missing N — same N-drop pattern as O-P1-23 DSDTC) |
| a0017 | DALNKGRP | Variable name typo + paraphrase | `DALNKGRP` + `usually be a many-to-one` | `DALKGRP` (missing N) + `usually be in a many-to-one` (extra word `in`) |
| a0018 | DATESTCD | Examples value drop | `Examples: "DISPAMT", "RETAMT".` | `Examples.` (entire example list dropped + colon→period) |
| a0019 | DATEST | CDISC Notes paraphrase | `test or examination` | `test of examination` (or→of single-char drift) |
| a0020 | DACAT | CT column literal drop + quote drop | CT col `*` + Examples `"STUDY MEDICATION", "RESCUE MEDICATION"` (with quotes) | CT col empty (single-char `*` dropped) + Examples `STUDY MEDICATION, RESCUE MEDICATION` (quotes dropped) |
| a0021 | DASCAT | CT column literal drop | CT col `*` | CT col empty (single-char `*` dropped) |

### Pattern characterization

**Writer family on dense Findings spec tables exhibits 4 distinct hallucination modes**:
1. Variable name N-drop typo (DALNKID→DALKID, DALNKGRP→DALKGRP) — same pattern as O-P1-23 DSDTC + O-P1-34 ECNKID/ECPSTRGUI + batch 13 O-P1-37 JPTW + batch 15 O-P1-36 STUDIID
2. CDISC Notes paraphrase (Sequence number given→Number used; test or→test of; usually be a→usually be in a) — same as O-P1-21 SVCNTMOD-class
3. CT column single-char literal drop (`*` Grouping Qualifier marker dropped) — NEW failure mode for batch 18
4. Quote mark drop in Examples list (`"STUDY MEDICATION"`→`STUDY MEDICATION`) — NEW failure mode for batch 18

Modes 1+2 are recurring writer-family hallucination patterns (cumulative across batches 09/12/13/15/18 = 5 batch evidence accumulation, very strong).
Modes 3+4 are NEW for batch 18 (Findings domain `*` Grouping Qualifier marker handling).

### Tiebreaker decision: NOT TRIGGERED ✓

Per drift cal precedent (O-P1-12 batch 06 / O-P1-23 batch 09 / O-P1-34 batch 12 / O-P1-36-38 batch 15), tiebreaker is required when FAIL root cause cannot be conclusively identified. Here:
- Variable name typos (DALKID/DALKGRP): definitively root-caused to writer-family character drop hallucination (executor + PDF agree as ground truth)
- CDISC Notes paraphrases: definitively root-caused to writer-family content rewriting hallucination
- `*` single-char drops: definitively root-caused to writer-family interpretive convention drift (writer interpreted `*` as "no CT" and omitted)
- Quote mark drops: definitively root-caused to writer-family literal-character normalization drift

Therefore tiebreaker would not add information. Skip tiebreaker.

## Repair scope applied

| # | Type | Scope | Action |
|---|---|---|---|
| **0** | **NONE** | **0 atoms** | **NO root file repair**: baseline 18b is PDF-accurate. Drift cal value-add is to surface writer-family drift pattern, NOT to "fix" the baseline. Applying Option E with writer rerun output would CORRUPT baseline. |
| INFO | Documentation | n/a | Findings logged as O-P1-46 HIGH (writer-family verbatim drift, direction-reversed drift cal value-add 6th precedent) |

**Critical decision rationale (NEW lesson for v1.3 prompt update)**: When NEW1 dual-threshold FAILs on verbatim overlap, the agent doing the worse work is NOT necessarily the baseline. PDF cross-check is mandatory before deciding repair direction.

## Findings added

| ID | Severity | Summary |
|---|---|---|
| O-P1-46 | HIGH | Writer-family verbatim drift cluster on p.180 DA spec table (drift cal rerun, not baseline): (a) variable name N-drop typos DALNKID→DALKID + DALNKGRP→DALKGRP (same pattern as O-P1-23 DSDTC + O-P1-34 ECNKID + O-P1-36 STUDIID — N drop instead of Y/I drop, accumulating writer-family character-drop motif across 5 batches); (b) CDISC Notes paraphrases (Sequence number given→Number used + test or→test of + usually be a→usually be in a — content rewriting hallucination, accumulating writer-family interpretation-shift motif since O-P1-21 SVCNTMOD); (c) NEW failure mode `*` Grouping Qualifier marker single-char drop in CT column (DACAT + DASCAT both dropped); (d) NEW failure mode quote mark drop in Examples list (`"STUDY MEDICATION"`→`STUDY MEDICATION`). 7 atoms drift cluster. **Direction reversed from prior 5 drift cal precedents** — baseline executor 18b is PDF-accurate, rerun writer introduced drift. **Drift cal value-add 超 Rule A 6th precedent** (Rule A 1-atom-per-page sample at most 1-2 of 7 affected). NO root file repair (baseline correct). v1.3 prompt candidate: writer-family character-level + interpretation-rigidity self-validation MORE strongly enforced (NEW2 requires extension to single-char marker preservation + literal-character normalization ban). |

## Cumulative drift cal track

| Run | Page | A | B | strict match | verbatim overlap | Root cause | Action |
|---|---|---|---|---|---|---|---|
| 30-page (batch 03) | p.25 | executor | writer | 67.5% / 37.5% / 37.5% (3-way) | — | QS sparse-cell PDF parse noise (O-P1-09) | continue + Rule A 加密 per-batch |
| 300-atom (batch 06) | p.60 | writer 06b | executor rerun | 17.6% strict | — | writer 06b page misattribution + CO under-extract (O-P1-12) | Option E rerun promoted to primary |
| 300-atom (batch 09) | p.89 | writer 09b | executor rerun | 60.6% pre-fix / 69.7% post-fix | — | writer 09b 3 DS row data hallucination + CT spec drift (O-P1-23) | Option H bulk fix using executor verbatim |
| 300-atom (batch 12) | p.118 | writer 12b | executor rerun | 48% strict | — | writer 12b 4-atom ec.xpt corruption (O-P1-34) + convention drift (O-P1-33 non-blocking) | 4-atom Option H targeted; convention defer v1.3 |
| 300-atom (batch 15) | p.147 | writer 15b | executor rerun | 97.4% strict / 41% verbatim | — | writer 15b multi-page systemic corruption: STUDIID×8 (O-P1-36) + supple→suppbe (O-P1-37) + bs/relrec/relspec data corruption + TABLE_HEADER cross-domain pollution (O-P1-38) + p.146 18-atom under-extraction | Option E p.146/p.147/p.148 wholesale × 3 + Option H × 3 |
| **300-atom (batch 18)** | **p.180** | **executor 18b (baseline)** | **writer rerun** | **100% strict / 69.6% verbatim** | **NEW1 dual-threshold FAIL** | **DIRECTION REVERSED — writer rerun introduced 7-atom drift cluster: variable name N-drop typos (DALKID/DALKGRP) + CDISC Notes paraphrases + NEW `*` CT marker drop + NEW quote mark drop; baseline 18b PDF-accurate** | **NO root repair (baseline correct) + finding O-P1-46 HIGH writer-family character-drop + interpretation-shift + NEW marker-drop + NEW quote-drop motif documented** |

**Pattern stable across 6 drift cal runs**: writer family exhibits dense-table verbatim hallucination + paraphrase + character drop in BOTH baseline AND rerun roles. Executor family does not exhibit this pattern in either role. Confidence: writer-family bug class fully characterized as "spec-table verbatim drift" — recommend strong v1.3 prompt patches. Direction-reversal at batch 18 confirms writer-family is the consistent bug source (independent of dispatch role).

**Strict-vs-verbatim divergence reaffirmed**: 100% strict count match would have masked 30.4% verbatim divergence. NEW1 dual-threshold caught the issue (working as designed batch-15 spec).

## Cross-reference

- O-P1-21 (batch 09): writer-family CDISC Notes paraphrase pattern (SVCNTMOD CT hallucination) — REAFFIRMED
- O-P1-23 (batch 09): writer-family DS hallucination + drift cal value-add over Rule A — REAFFIRMED 6th
- O-P1-34 (batch 12): writer-family ec.xpt 4-atom data corruption — REAFFIRMED variable name N-drop pattern
- O-P1-36 (batch 15): writer-family STUDIID×8 typo cluster — REAFFIRMED character-drop pattern (now N→nothing, prior Y→nothing)
- O-P1-26 (batch 10 INFO): TABLE_ROW pipe-format inconsistency — both 18b baseline + writer rerun used outer-pipe consistently (no recurrence)
- NEW1 (batch 15 candidate): drift cal dual-threshold worked as designed — strict 100% PASS would have masked 30.4% verbatim divergence
- NEW2 (batch 14 O-P1-36 candidate): writer character-level self-validation — REINFORCED need; v1.3 should require writer to spell-check variable names + preserve `*` markers + preserve quote marks
