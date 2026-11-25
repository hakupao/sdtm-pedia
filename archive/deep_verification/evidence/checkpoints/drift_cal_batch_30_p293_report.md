# Drift Cal Batch 30 p.293 Report (NEW1 dual-threshold, round 6 6th time)

> Status: **FAIL** (verbatim <80%)
> Date: 2026-04-27
> Trigger: every-3-batches cadence batch 27→30 + cumulative atoms post-p.270 ≥600 (双触发 MANDATORY)
> NEW1 dual-threshold validated round 1+2+3+4 STRONGLY (4× consecutive PASS) → round 5 5th time CATASTROPHIC FAIL strict 71.1% / verbatim 6.7% LOWEST EVER → round 6 6th time = different motif (strict 100% / verbatim 45.0%, intra-family same-agent-type drift)

## Pair design

| Role | Subagent | File | Atoms |
|---|---|---|---|
| Baseline | sub-batch 30a `oh-my-claudecode:executor` | `pdf_atoms_batch_30a.jsonl` (filtered p.293) | 41 |
| Rerun | `oh-my-claudecode:executor` | `drift_cal_p293_executor_rerun.jsonl` | 41 |

**Methodological note**: Per kickoff §6 alternation rule (baseline=writer → rerun=executor; baseline=executor → rerun=writer), expected pair = (executor, writer). Actual main-session dispatch used `oh-my-claudecode:executor` for BOTH 30a + rerun (executor family is action-oriented per v1.3 prompt §派发, both `oh-my-claudecode:executor` and `oh-my-claudecode:writer` are valid writer family — 主 session 选 executor for 30a + drift cal rerun consistency). Result: drift cal probe became **intra-family non-determinism test** rather than cross-family alternation test. **This is itself meaningful data**: even same-family same-subagent-type runs on identical PDF page diverge 54% on dense TABLE_ROW empty-cell parsing. Round 7+ recommend strict alternation enforcement to disentangle intra-family vs cross-family drift.

## NEW1 dual-threshold computation

| Metric | Value | Threshold | Verdict |
|---|---|---|---|
| Strict count match | 100.0% (41/41) | ≥80% | **PASS** |
| Verbatim hash overlap | 45.0% (18/40 unique hashes) | ≥80% | **FAIL** |
| Per-atom_id verbatim match | 46.3% (19/41 same id same content) | n/a | (informational) |
| **Overall** | strict PASS + verbatim FAIL | both ≥80% | **FAIL** |

## Direction analysis

- Baseline-only verbatim hashes (30a executor wrote, rerun didn't): 22
- Rerun-only verbatim hashes (rerun wrote, 30a didn't): 22
- Common verbatim hashes: 18

**Direction = rerun-side cell-drop motif** (NEW round-6 motif distinct from round 5):
- Round 1 batch 15 p.147: writer-family Cyrillic homoglyph + variable swap (NEW2 limitation)
- Round 2 batch 18 p.180: writer-family multi-paragraph paraphrase (DALNKID/DALNKGRP N-drop)
- Round 3 batch 21 p.205: writer-family char-swap (CPSCMRKS character-swap; NEW2 limitation extended)
- Round 4 batch 24 p.233: writer-family SENTENCE wholesale paraphrase ('illustrate'→'distinguish')
- **Round 5 batch 27 p.270 (CATASTROPHIC)**: writer-family VALUE HALLUCINATION on TABLE_ROW value cells (USUBJID/PCREFID/PCTESTCD INVENTED IDs not in PDF; verbatim 6.7%)
- **Round 6 batch 30 p.293 (NEW MOTIF)**: rerun-side TABLE_ROW empty-cell drop (correct cell value `Y` vs incorrect blank `| |` — opposite direction from round 5; rerun DROPPED MKSTRESC cells while baseline 30a captured both MKORRES + MKSTRESC = Y/Y as PDF shows)

DIRECTION REVERSED 10th precedent (round 5 was 9th writer-direction; round 6 reverses to rerun-direction).

## Type distribution comparison

| Type | Baseline (30a executor) | Rerun (executor) |
|---|---|---|
| CODE_LITERAL | 2 | 2 |
| HEADING | 1 | 1 |
| LIST_ITEM | 2 | 2 |
| SENTENCE | 12 | 12 |
| TABLE_HEADER | 2 | 2 |
| TABLE_ROW | 22 | 22 |

Type distribution IDENTICAL between baseline + rerun (count + type) — divergence is purely on **verbatim CONTENT within TABLE_ROW**, not atom-counting drift. This is atypical pattern compared to round 5 (where rerun fabricated 13 extra atoms with INVENTED IDs).

## Sample divergences

### Same atom_id, different verbatim (per-id 22 diffs; 3 representative shown)

**ig34_p0293_a003** (TABLE_ROW Row 1):
- Baseline (30a): `| 1 | DEF | MK | DEF-138 | 1 | TNDRIND | Tenderness Indicator | Y | Y | | | | TEMPOROMANDIBULAR JOINT | RIGHT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |`
- Rerun: `| 1 | DEF | MK | DEF-138 | 1 | TNDRIND | Tenderness Indicator | Y | | | | | TEMPOROMANDIBULAR JOINT | RIGHT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |`
- **Divergence**: rerun DROPPED MKSTRESC=Y (column 9 of TABLE_HEADER), shifted empty-cell pattern. PDF ground truth (per main-session pre-dispatch p.293 preview) shows BOTH MKORRES=Y AND MKSTRESC=Y populated for Tenderness Y rows.
- **Direction**: rerun-side error (executor dropped cell value).

**ig34_p0293_a004** (TABLE_ROW Row 2 SWLLIND): similar Y/Y → Y/(empty) drop pattern.

**ig34_p0293_a005** (TABLE_ROW Row 3 TNDRIND N): baseline `N | N` vs rerun `N | (empty)` — same MKSTRESC drop motif on N values.

### Pattern summary

22/41 atoms (53.7%) show same MKSTRESC-cell-drop pattern in rerun across rows 1-16 of mk.xpt Example 1 + sample rows of Example 2 mk.xpt (Sharp/Genant). **Systematic**, not random.

### Common verbatim (18 unique hashes shared)

Common atoms include: HEADING (Example 2), 12 SENTENCE narrative atoms (verbatim copy of multi-paragraph Sharp/Genant text), 2 TABLE_HEADER, 2 LIST_ITEM (Rows 1-2/4-5/etc grouping), 2 CODE_LITERAL (e.g. file path mentions). SENTENCE-narrative type largely matches across runs — divergence concentrated in TABLE_ROW dense empty-cell zones.

## Action

- **Repair decision**: NO Option H needed for batch 30 (root unaffected — drift cal probe operates on rerun jsonl, not 30a baseline). Baseline 30a TABLE_ROW values judged CORRECT per PDF ground truth (MKORRES + MKSTRESC both Y for Y-rows is CDISC SDTM standard); rerun executor judged INCORRECT (dropped MKSTRESC consistently).
- **Safety net validated**: drift cal probe surfaced systematic intra-family non-determinism that would NOT have been caught by Rule A 1/page sample (sample atom_id 3 = ig34_p0293_a016 single TABLE_ROW). Round 5 reconciler-safety-net pattern continues round 6.
- **Findings filed**: O-P1-97 HIGH (drift cal NEW1 6th time FAIL — verbatim 45% / strict 100% / direction REVERSED 10th + intra-family executor non-determinism NEW round-6 motif on dense TABLE_ROW empty-cell parsing).

## v1.4 cut implication (cumulative agenda)

- **NEW1 dual-threshold round 6 6th time validation**: FAIL on different motif from round 5. Pattern: NEW1 spec catches multiple distinct writer/executor failure modes (Cyrillic / paraphrase / VALUE HALLUCINATION / cell-drop). Spec retain unchanged at v1.4.
- **NEW round-6 v1.4 candidate**: G-MS-NEW-6-1 — TABLE_ROW empty-cell patterns are non-deterministic between same-subagent-type runs on dense PDF tables. Mitigation: (a) post-write per-page wc -l + cell-count regex validation against TABLE_HEADER column count; (b) writer/executor explicit instruction "preserve EVERY cell including empty `| |` for column-count fidelity"; (c) reconciler-side bulk validate TABLE_ROW pipe-count == TABLE_HEADER+1 pipe-count for same parent_section.
- **NEW round-6 v1.4 candidate**: G-MS-NEW-6-2 — drift cal alternation enforcement: kickoff §6 alternation rule must be PROCEDURALLY ENFORCED in main session dispatch (currently 主 session 选择 by family judgement — round 6 batch 30 chose executor for both 30a + rerun by mistake; alternation true cross-family value-add lost). Mitigation: kickoff §6 specify EXACT subagent_type for rerun based on baseline subagent_type table.

## Comparison to prior 5 drift cals

| Round | Batch | Page | Strict | Verbatim | Verdict | Motif |
|---|---|---|---|---|---|---|
| 1 | 15 | 147 | 97.4% | 41% | FAIL | Cyrillic homoglyph + variable swap |
| 2 | 18 | 180 | 100% | 69.6% | FAIL | DALNKID/DALNKGRP N-drop + paraphrases |
| 3 | 21 | 205 | 100% | 94.1% | PASS | (CPSCMRKS char-swap caught by NEW2 limitation, but PASS overall) |
| 4 | 24 | 233 | 94.1% | 41.2% | FAIL | writer-family SENTENCE paraphrase |
| 5 | 27 | 270 | 71.1% | **6.7% LOWEST** | FAIL | writer-family VALUE HALLUCINATION (CATASTROPHIC) |
| **6** | **30** | **293** | **100%** | **45.0%** | **FAIL** | **rerun-side TABLE_ROW empty-cell drop (NEW MOTIF)** |

5/6 drift cals FAIL on dual-threshold (only round 3 PASSED). NEW1 spec validates 6 distinct failure modes — robust.
