# P1 Batch 36 Report — Round 8 Multi-Session, Session C, Drift Cal Carrier (HALT + Option H Repair)

> Date: 2026-04-28 (post v1.4 cut)
> Session ID: session_c_round_8
> Status: completed_with_halt_and_resume
> Final atoms: **241** (36a executor 112 + 36b post-Option-H 129)
> Round 8 protocol: G-MS-4 halt fallback 2nd LIVE-FIRE EFFECTIVE + N14 strict alternation 2nd LIVE-FIRE EFFECTIVE

---

## §1 — Executive summary

Batch 36 (Round 8 multi-session, Session C, drift cal carrier 8th time) executed v1.4 protocol on SDTMIG v3.4 p.351-360 with the following critical events:

1. **36a executor baseline (p.351-355, 112 atoms)**: clean atomization of TR Spec table tail + TR Assumptions L5 NEW + §6.3.12.3 Tumor Identification/Tumor Results Examples L4 sib=3 NEW + Example 1/2 L5 RESTART. Schema sweep PASS.

2. **36b writer baseline (p.356-360, 127 atoms)**: produced **4th cumulative writer-direction main-line VALUE HALLUCINATION recurrence** — multi-axis corruption (char-level R1↔RT, numeric 0↔9, test code ACNSD↔ACRSD/PCBSD↔PCRSD, classification NEW↔TARGET, paraphrase, header column collapse TRSTRESC×4 vs distinct columns, header typos TRORRSU/TRREAND/TREVALDI, N5 empty-cell drop systematic).

3. **Drift cal p.357 mandatory** (per cadence + N14 alternation): executor rerun caught writer-direction signal — strict 100% PASS / verbatim 0% FAIL → **BOTH thresholds FAIL** → DIRECTION_REVERSED.

4. **Halt protocol G-MS-4** (round 7 1st LIVE-FIRE EFFECTIVE precedent → round 8 2nd LIVE-FIRE EFFECTIVE): main session wrote `halt_state_batch_36.md` (191 lines, 13.7KB, 4 resume options + evidence), waited user authorization.

5. **User authorized RESUME_BATCH_36 option=A** (Option H bulk repair via executor rerun on 4 corrupt pages).

6. **Option H bulk repair**: Rule B backup `pdf_atoms_batch_36b.jsonl.pre-OptionH-bulk.bak` → executor rerun on p.356/358/359/360 (104 atoms) + reuse drift_cal_p357_executor_rerun.jsonl (25 atoms) → combined 129 atoms clean replacement. Schema sweep PASS post-repair (0 9-enum / 0 N8 / 0 atom_id format / 0 sib collision violations; spot-checks Row 9 / VSCAT / Row 14 / Row 15 / Row 19 all corrected).

7. **Reviewer slot #46 dispatch failure**: pre-allocated `superpowers:verification-before-completion` was a SKILL not registered AGENT (recurring O-P1-110 round 7 motif). Pivoted to **Plan agent inaugural burn** (slot #46, AUDIT pivot 27th cumulative, single-agent family inaugural).

8. **Plan reviewer verdict**: CONDITIONAL_PASS (9 CONFIRM / 0 OVERRIDE / 1 AMBIGUOUS-lean-OVERRIDE on atom 6 .xpt-parent discipline). Reviewer accuracy 95.0% ≥80% Rule D PASS. v1.4 fix matrix 7/8 PASS + 1 ADVISORY.

9. **4 NEW findings** O-P1-121..124 logged (kickoff lint motif + .xpt-parent discipline + drift cal carrier 8/8 + N14+G-MS-4 STRONGLY VALIDATED).

---

## §2 — Atom production metrics

### 2.1 Final atoms (post Option H repair)

| Sub-batch | Pages | Atoms | Subagent | Status |
|---|---|---|---|---|
| 36a | p.351-355 | 112 | oh-my-claudecode:executor (baseline) | clean |
| 36b | p.356-360 | 129 | oh-my-claudecode:executor (Option H repair via 4-page rerun + drift_cal p.357 reuse) | clean post-repair |
| **Total** | **p.351-360** | **241** | mixed | **post halt + Option H repair** |

### 2.2 Per-page distribution

| Page | Atoms | atom_type breakdown |
|---|---|---|
| p.351 | 22 | TABLE_ROW=22 (TR Spec table cross-batch continuation from sister batch 35) |
| p.352 | 10 | TABLE_ROW=2 + SENTENCE=1 + HEADING=1 (TR Assumptions L5 NEW) + LIST_ITEM=4 + TABLE_HEADER=1 + NOTE=1 (transition page R12 PASS) |
| p.353 | 18 | LIST_ITEM=4 + HEADING=2 (§6.3.12.3 L4 NEW + Example 1 L5 NEW) + SENTENCE=5 + CODE_LITERAL=1 + TABLE_HEADER=1 + TABLE_ROW=5 |
| p.354 | 35 | SENTENCE=10 + CODE_LITERAL=3 + TABLE_HEADER=3 + TABLE_ROW=18 + HEADING=1 (Example 2 L5 NEW) (Examples-narrative content type) |
| p.355 | 27 | CODE_LITERAL=1 + TABLE_HEADER=1 + TABLE_ROW=25 (Example 2 tr.xpt dense) |
| p.356 | 29 | SENTENCE=4 + HEADING=4 (relrec.xpt L6 + Example 3 L5 NEW + tu.xpt L6 + tr.xpt L6) + TABLE_HEADER=3 + TABLE_ROW=12 + LIST_ITEM=6 |
| p.357 | 25 | TABLE_ROW=25 (Example 3 tr.xpt continuation, drift cal carrier) |
| p.358 | 26 | TABLE_ROW=17 (TR Example 3 close + relrec.xpt + VS Spec head) + SENTENCE=3 + HEADING=4 (relrec.xpt L6 sib=4 + §6.3.13 VS L3 sib=13 NEW + VS-Description L4 sib=1 + VS-Specification L4 sib=2) + TABLE_HEADER=2 |
| p.359 | 25 | TABLE_ROW=25 (VS Spec dense) |
| p.360 | 24 | TABLE_ROW=8 + NOTE=1 + HEADING=4 (VS-Assumptions L4 sib=3 + VS-Examples L4 sib=4 + Example 1 L5 sib=1 + vs.xpt L6 sib=1) + LIST_ITEM=9 + SENTENCE=1 + TABLE_HEADER=1 |

### 2.3 atom_type combined distribution

| atom_type | Count | % |
|---|---|---|
| TABLE_ROW | 159 | 66.0% |
| LIST_ITEM | 23 | 9.5% |
| SENTENCE | 20 | 8.3% |
| HEADING | 16 | 6.6% |
| TABLE_HEADER | 9 | 3.7% |
| CODE_LITERAL | 5 | 2.1% |
| NOTE | 2 | 0.8% |
| **Total** | **241** | **100%** |

5/9 atom_type enum hit (no CROSS_REF / no FIGURE in this batch — appropriate for spec-table + Examples-narrative content type).

### 2.4 HEADING chain inventory (16 atoms)

| atom_id | hl | sib | parent_section | text |
|---|---|---|---|---|
| ig34_p0352_a003 | 5 | 3 | §6.3.12.2 Tumor/Lesion Results (TR) | TR – Assumptions |
| ig34_p0353_a005 | 4 | 3 | §6.3.12 Tumor/Lesion Domains | §6.3.12.3 Tumor Identification/Tumor Results Examples NEW |
| ig34_p0353_a006 | 5 | 1 | §6.3.12.3 Tumor Identification/Tumor Results Examples | Example 1 |
| ig34_p0354_a009 | 5 | 2 | §6.3.12.3 Tumor Identification/Tumor Results Examples | Example 2 |
| ig34_p0356_a004 | 6 | 1 | §6.3.12.3 Tumor Identification/Tumor Results Examples | relrec.xpt (Example 2 close) |
| ig34_p0356_a008 | 5 | 3 | §6.3.12.3 Tumor Identification/Tumor Results Examples | Example 3 |
| ig34_p0356_a014 | 6 | 2 | §6.3.12.3 Tumor Identification/Tumor Results Examples | tu.xpt |
| ig34_p0356_a027 | 6 | 3 | §6.3.12.3 Tumor Identification/Tumor Results Examples | tr.xpt |
| ig34_p0358_a008 | 6 | 4 | §6.3.12.3 Tumor Identification/Tumor Results Examples | relrec.xpt (Example 3 close) |
| ig34_p0358_a012 | 3 | 13 | §6.3 [MODELS FOR FINDINGS DOMAINS] | §6.3.13 Vital Signs (VS) NEW |
| ig34_p0358_a013 | 4 | 1 | §6.3.13 Vital Signs (VS) | VS – Description/Overview |
| ig34_p0358_a015 | 4 | 2 | §6.3.13 Vital Signs (VS) | VS – Specification |
| ig34_p0360_a006 | 4 | 3 | §6.3.13 Vital Signs (VS) | VS – Assumptions |
| ig34_p0360_a011 | 4 | 4 | §6.3.13 Vital Signs (VS) | VS – Examples |
| ig34_p0360_a012 | 5 | 1 | VS – Examples | Example 1 |
| ig34_p0360_a019 | 6 | 1 | VS – Examples | vs.xpt |

---

## §3 — Halt event narrative (G-MS-4 2nd LIVE-FIRE)

### 3.1 Halt trigger

Drift cal p.357 (mandatory per cadence batch 33→36 every-3-batches + cumulative atoms post-p.325 ≥600 双触发) executed via N14 strict alternation table:
- Baseline: oh-my-claudecode:writer (36b sub-batch baseline)
- Rerun: oh-my-claudecode:executor (alternation table)
- Strict count overlap: 25 vs 25 = **100.0%** PASS
- Verbatim hash overlap (Jaccard): 0/50 = **0.0%** FAIL
- BOTH thresholds: FAIL → DIRECTION_REVERSED writer-family motif

PDF p.357 cross-check confirmed executor rerun matches PDF + 36b writer hallucinated 38 rows across 4 pages (p.356 tu.xpt 5 rows + p.356-358 tr.xpt 32 rows + p.358 VSCAT 1 row).

### 3.2 4th cumulative writer-direction main-line VALUE HALLUCINATION recurrence

| Round | Batch | Finding ID | Severity | Description |
|---|---|---|---|---|
| 5 | 27 | O-P1-85 | HIGH | USUBJID/PCREFID/PCTESTCD INVENTED IDs (drift-cal-rerun-only context) |
| 6 | 31 | O-P1-103 | HIGH | SUPPQUAL Example 3 IDVAR=OESEO + QNAM=OEEDILST stale-template (main-line) |
| 7 | 33 | O-P1-109 | HIGH | QSORRES vs QSORRESU + Character→Standardized + Variable→Result Qualifier role swap + structural phantom TABLE_HEADER (main-line, multi-axis 4 axes) |
| **8** | **36** | **O-P1-122-related** | **HIGH** | **TR Example 3 tr.xpt + tu.xpt + VS Spec VSCAT 38 rows; multi-axis: char-level (R1→RT, ACNSD→ACRSD, PCBSD→PCRSD), numeric (0→9), classification (NEW→TARGET), paraphrase, N5 empty-cell drop, header column collapse (TRSTRESC×4)** |

→ Halt threshold **N3 NEW8.d EMERGENCY-CRITICAL 4th cumulative** crossed.

### 3.3 Halt artifact

- File: `evidence/checkpoints/halt_state_batch_36.md` (191 lines, 13.7KB)
- §1 trigger summary + §2 PDF ground-truth evidence + §3 file inventory + §4 4 resume options (A/B/C/D) + §5 self-validation gate + §6 user authorization protocol + §7 single-line halt echo
- Single-line halt echo: `HALT_BATCH_36 reason=N3_NEW8d_4th_cumulative_writer_direction_value_hallucination atoms_36a=112 atoms_36b_corrupt=127 drift_cal_p357_strict=100% drift_cal_p357_verbatim=0% direction=writer_family_4th_cumulative`

### 3.4 User authorization received

**Daisy responded** (Chinese summary first then concise authorization): `走a` = RESUME_BATCH_36 option=A (Option H bulk repair via executor rerun on p.356/358/359/360 corrupt blocks).

### 3.5 Resume execution (Option H bulk repair)

1. Rule B backup: `cp pdf_atoms_batch_36b.jsonl pdf_atoms_batch_36b.jsonl.pre-OptionH-bulk.bak` (73KB preserved)
2. Dispatch executor on p.356/358/359/360 → 104 atoms in `pdf_atoms_batch_36b_executor_repair.jsonl`
3. Reuse `drift_cal_p357_executor_rerun.jsonl` (25 atoms p.357)
4. Python merge (sort by atom_id) → 129 atoms in new `pdf_atoms_batch_36b.jsonl`
5. Schema sweep verify: PASS

### 3.6 G-MS-4 protocol validation

- Round 7 batch 33 = 1st LIVE-FIRE EFFECTIVE (writer accept resume via halt_state file + user authorization fallback)
- **Round 8 batch 36 = 2nd LIVE-FIRE EFFECTIVE**
- End-to-end cycle: drift cal pre-DONE hook detection → halt → halt_state file write → user reviewed + authorized → main session executed Option H repair → reviewer slot #46 confirmed CONDITIONAL_PASS post-repair → DONE

→ **G-MS-4 STRONGLY VALIDATED** post 2nd live-fire (codify in v1.5).

---

## §4 — N14 strict alternation methodology 2nd LIVE-FIRE

### 4.1 Application

| Stage | Subagent family | Per N14 alternation table compliance |
|---|---|---|
| 36a baseline | oh-my-claudecode:executor | initial |
| 36b baseline | oh-my-claudecode:writer | opposite of 36a (alternation) |
| Drift cal rerun (p.357) | oh-my-claudecode:executor | opposite of 36b baseline (alternation) |
| Option H repair rerun (p.356/358/359/360) | oh-my-claudecode:executor | opposite of 36b baseline (alternation, repair scope) |

All cross-family on opposite-family-side per N14 alternation table.

### 4.2 Effect

Cleanly disentangled writer-direction signal from intra-family non-determinism. Without N14 alternation, baseline+rerun=same family would have masked the 4th cumulative writer-direction VALUE HALLUCINATION recurrence as intra-family non-determinism (per round 6 G-MS-NEW-6-2 codification rationale).

### 4.3 Validation status

- Round 7 batch 33 = 1st LIVE-FIRE EFFECTIVE
- **Round 8 batch 36 = 2nd LIVE-FIRE EFFECTIVE**
- → **N14 STRONGLY VALIDATED** post 2nd live-fire (codify in v1.5).

---

## §5 — Rule A reviewer slot #46 (Plan family INAUGURAL burn)

### 5.1 Pivot context

Original kickoff §1 pre-allocation: `superpowers:verification-before-completion` for slot #46. Agent dispatch failed: `Agent type 'superpowers:verification-before-completion' not found. Available agents: ...`. Same root-cause as round 7 O-P1-110 motif (SKILLS mistakenly listed in family pre-allocation).

Pivoted to **Plan agent inaugural burn** (Plan single-agent family unburned in P1 cumulative, registered in Task tool's `subagent_type` enum).

### 5.2 Reviewer details

- Subagent type: `Plan` (single-agent family INAUGURAL burn)
- Rule D slot: #46 (post #45 reserved sister batch 35 + #44 v1.4 cut reviewer)
- AUDIT pivot index: 27th cumulative
- Drift cal carrier: 8th time
- Sample: 10 atoms stratified 1/page p.351-360 seed=20260641
- Tool adaptation: Plan agent has no Write tool — inline markdown verdicts.jsonl + summary.md content for main-session write substitution (round 5/6/7 precedent reuse)

### 5.3 Verdict

**CONDITIONAL_PASS**

| Metric | Result |
|---|---|
| CONFIRM | 9 |
| OVERRIDE | 0 |
| AMBIGUOUS-lean-OVERRIDE | 1 (atom 6 ig34_p0356_a005 .xpt-parent discipline) |
| Reviewer accuracy | (9 + 0.5)/10 = **95.0%** |
| Rule D ≥80% | ✅ PASS |
| v1.4 fix matrix | **7/8 PASS + 1 ADVISORY** |
| 9-type atom coverage | 5/9 hit |

### 5.4 v1.4 fix matrix detail

| Item | Description | Result |
|---|---|---|
| (A) R1-R15 | atom_id format / R10 strict / R12 / R14 | ✅ PASS |
| (F) NEW6+NEW6.b | L4 NEVER self-parent + chapter dual-form | ✅ PASS |
| (G) NEW7 chain | L5/L6 sib continuity + INTRA-AGENT | ✅ PASS |
| (J) NEW8.c | TABLE_HEADER column-set canonical | ✅ PASS |
| (P) v1.4 N3 NEW8.d | TABLE_ROW whole-row VALUE HALLUCINATION (post Option H = 0 violations) | ✅ PASS |
| (R) v1.4 N5 G-MS-NEW-6-1 | TABLE_ROW pipe-count == TABLE_HEADER | ✅ PASS |
| (S) v1.4 N6 NEW7 L6 sub-batch handoff | INTRA-AGENT consistency + L6 textual heading canonical | ⚠️ ADVISORY (.xpt-parent regression, 27 cumulative atoms) |
| (U) v1.4 N8 NEW9 | non-L3-HEADING L2 short-bracket parent FORBID | ✅ PASS |

### 5.5 AUDIT-mode pivot reflection

Plan agent normal mode (software architect implementation plan design) mapped to SDTM atomization quality audit via 3-axis analogy: 'implementation plan design ↔ Rule A pre-DONE audit plan' / 'identifying critical files ↔ atom verbatim ground-truth verification' / 'architectural trade-offs ↔ atom_type 9-enum coverage trade-offs'.

Plan family inaugural burn observation: **Plan brings architectural-overview posture** which materialized as careful parent_section discipline scrutiny (1/10 AMBIGUOUS-lean-OVERRIDE on parent_section dimension, 0 on other dimensions) — analogous to Plan's normal mode flagging architectural debt + abstraction-leak patterns in code review.

---

## §6 — Findings

### 6.1 O-P1-121 (MEDIUM) — kickoff §1 SKILL-vs-AGENT pre-allocation lint missing

Recurring O-P1-110 motif from round 7. Despite v1.4 codification removing data + firecrawl families for SKILL-vs-AGENT confusion, kickoff §1 still scheduled `superpowers:verification-before-completion` SKILL for slot #46 — registry validation gate missing from kickoff §1 generator. **v1.5 codification mandatory.**

### 6.2 O-P1-122 (MEDIUM AMBIGUOUS) — parent_section table_caption regression

27 atoms in 36b post-Option-H use .xpt file caption as parent_section (8 tu.xpt + 8 tr.xpt + 6 relrec.xpt + 5 vs.xpt). AMBIGUOUS reading: (a) strict N7 v1.4 = `tu.xpt` IS the L6 textual heading per PDF visual; (b) discipline-extension = parent_section should resolve up to §6.3.12.3 OR a descriptive form like 'TU – Example 3 Dataset'. **v1.5 codification candidate** — defer to v1.5 cut session, joins round 7 O-P1-114 deferral pattern.

### 6.3 O-P1-123 (INFO) — drift cal carrier 8/8 cumulative verification

Atom 7 (ig34_p0357_a001) PDF-cross-checked PASS post Option H. v1.4 N3 NEW8.d EMERGENCY-CRITICAL hook EFFECTIVE end-to-end.

### 6.4 O-P1-124 (INFO) — N14 + G-MS-4 STRONGLY VALIDATED post 2nd live-fire

Both v1.4 codifications graduate from 1st-live-fire-EFFECTIVE → STRONGLY VALIDATED.

---

## §7 — File inventory

### 7.1 Files written by session C

| File | Atoms/Lines | Purpose |
|---|---|---|
| `pdf_atoms_batch_36a.jsonl` | 112 atoms | 36a executor baseline (clean) |
| `pdf_atoms_batch_36b.jsonl` | 129 atoms | 36b post Option H repair (clean replacement of 127 corrupt) |
| `pdf_atoms_batch_36b.jsonl.pre-OptionH-bulk.bak` | 127 atoms | Rule B backup of corrupt 36b writer original |
| `pdf_atoms_batch_36b_executor_repair.jsonl` | 104 atoms | Executor repair source (p.356/358/359/360) |
| `drift_cal_p357_executor_rerun.jsonl` | 25 atoms | Drift cal source + Option H reuse for p.357 |
| `halt_state_batch_36.md` | 191 lines | G-MS-4 halt protocol evidence + 4 resume options |
| `_progress_batch_36.json` | this file | sub-progress (single-session JSON state) |
| `P1_batch_36_report.md` | this file | full batch report |
| `rule_a_batch_36_sample.jsonl` | 10 atoms | Rule A sample seed=20260641 |
| `rule_a_batch_36_verdicts.jsonl` | 10 verdicts | Plan reviewer slot #46 verdicts |
| `rule_a_batch_36_summary.md` | 129 lines | Rule A summary + AUDIT-mode pivot reflection |

### 7.2 Files NOT touched (per kickoff §8 do-not-touch)

- root `pdf_atoms.jsonl` (8552 atoms unchanged — reconciler scope)
- `audit_matrix.md` / `_progress.json` (reconciler scope)
- sister batch files (`pdf_atoms_batch_35*`, `pdf_atoms_batch_37*`) — sister sessions still running parallel
- `subagent_prompts/*` (v1.4 active; v1.5 candidate stack accumulating with O-P1-121/122/123/124 round 8 additions)
- `schema/*.json` / `PLAN.md` / `plans/*.md`
- `CLAUDE.md` / MEMORY (absolute do-not-touch)

---

## §8 — Round 8 NEW precedents observed

1. QUADRUPLE structural transition single batch (p.352 L5 + p.353 L4 + p.358 MAJOR L3 + p.360 DOUBLE L4) — round 8 batch 36 NEW (analog to round 7 batch 34 first QUADRUPLE)
2. First DOUBLE Examples L4 sub-section coexistence (§6.3.12.3 Examples L4 sib=3 numbered + §6.3.12 group container L4 chain)
3. Plan family INAUGURAL burn (single-agent family) — slot #46 — 2nd cumulative single-agent inaugural burn post round 5 #28 general-purpose (1st)
4. **G-MS-4 halt fallback 2nd LIVE-FIRE EFFECTIVE** — promote G-MS-4 STRONGLY VALIDATED status
5. **N14 strict alternation methodology 2nd LIVE-FIRE EFFECTIVE** — promote N14 STRONGLY VALIDATED status
6. **4th cumulative writer-direction main-line VALUE HALLUCINATION recurrence** — multi-axis (char/numeric/classification/paraphrase/header collapse) — v1.5 candidate writer-family ban for Examples-narrative + spec-table content type STRONGLY RECOMMENDED
7. Two-layer audit 6th cumulative validation (drift cal pre-DONE hook + reviewer 1/page sample + main-session structural sweep amplification 1:27 ratio)

---

## §9 — Handoff to reconciler (Round 8 multi-session)

Session C contributes 241 atoms (112 + 129) over p.351-360 with 4 NEW findings (O-P1-121..124).

Reconciler should:
1. Merge `pdf_atoms_batch_36a.jsonl` + `pdf_atoms_batch_36b.jsonl` into root post sister batch 35+37 merges
2. Sweep cross-batch sibling continuity for §6.3 L3 chain (sib=12 §6.3.12 sister 35 → sib=13 VS batch 36) + §6.3.12 L4 chain (TU sister 35 + TR head sister 35/36a + §6.3.12.3 Examples 36a) + §6.3.12.3 L5 chain (Example 1/2 36a + Example 3 36b) + §6.3.13 VS L4 chain (36b)
3. Validate cross-session R15 TR Spec table TABLE_ROW continuity (sister batch 35 p.350 → batch 36a p.351, 22 atoms parent_section canonical match)
4. Update root `audit_matrix.md` with batch 36 row + Rule A 36 row + Rule D roster 43→46 + Plan family INAUGURAL
5. Update root `_progress.json` (atoms 8552→8552+sister35+241+sister37; pages 340→370; batches 34→37; Rule D 43→46; repair_cycles +2; findings +4)
6. **v1.5 patch session decision** — round 5+6+7+8 cumulative 17 v1.5 candidates accumulated; **v1.5 cut session BEFORE batch 39 STRONGLY RECOMMENDED** given 4th cumulative writer-direction VALUE HALLUCINATION recurrence threshold reached
7. O-P1-122 .xpt-parent reconciler-side decision — defer or apply L6 textual canonical bulk fix (~27 batch 36 + retroactive ~20-50 cumulative)
8. Multi-session round 8 protocol: write `MULTI_SESSION_RETRO_ROUND_8.md` (Rule C 三段式) + cleanup CLAUDE.md round-8 routing rule + delete one-shot kickoff files; **preserve `halt_state_batch_36.md` as historical evidence** (analog round 7 `halt_state_batch_32.md` per D-MS-8)

---

## §10 — Final DONE echo

```
PARALLEL_SESSION_36_DONE atoms=241 failures=0 repair_cycles=2 rule_a=95.0% drift_cal=triggered drift_cal_strict=100% drift_cal_verbatim=0% findings_added=O-P1-121,O-P1-122,O-P1-123,O-P1-124
```
