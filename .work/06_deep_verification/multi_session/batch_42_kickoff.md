# Batch 42 Kickoff — Round 10 (Session C, post v1.6 cut, MANDATORY DRIFT CAL CARRIER 10TH TIME)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-7 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法停止信号 = STEP 7 末尾 echo 单行 `PARALLEL_SESSION_42_DONE atoms=N failures=N repair_cycles=N rule_a=NN.N% drift_cal=triggered_strict=NN.N%_verbatim=NN.N% findings_added=...` OR halt 信号 `HALT_BATCH_42 reason=<X>` (per G-MS-4 STRONGLY VALIDATED halt fallback).
>
> **CRITICAL**: 本 batch 含 mandatory drift cal at p.412 (10th time NEW1 dual-threshold) + **6th cumulative writer-direction VALUE HALLUCINATION recurrence WATCH** (per v1.6 N18 EXTENDED scope dispatch — if 6th recurrence DETECTED DESPITE N18 EXTENDED scope: ESCALATE to v1.7 trigger = deprecate writer-family entirely from P1 atomization, special halt + escalate to user via halt_state_batch_42.md).
> ═══════════════════════════════════════════════════════════════════

## §0 — Pre-flight (Cross-validation table + AGENT-vs-SKILL pre-allocation lint)

### §0.1 Round 10 multi-session kickoff context

3 sister sessions B/C/D 物理并行 batches 41/42/43 + reconciler E 串行收尾 (round 10 = 1st round running v1.6 baseline post v1.6 cut 2026-04-29).

### §0.2 Cross-validation table (G-MS-13 codification)

| Session | Batch | Page range | Atoms reserved finding ID range | Reviewer slot pre-allocation | Drift cal |
|---|---|---|---|---|---|
| B | 41 | p.401-410 | O-P1-141..144 (4 IDs) | #53 `oh-my-claudecode:verifier` (omc family 11th burn, AUDIT pivot 34th) | SKIP |
| C (this) | **42** | p.411-420 | O-P1-145..148 (4 IDs) | **#54 `general-purpose`** (4th burn extension, AUDIT pivot 35th, drift cal carrier 10th time) | **MANDATORY p.412 (10th time NEW1 dual-threshold per cadence batch 39→42 + cumulative atoms post-p.382 ≥600 双触发)** |
| D | 43 | p.421-430 | O-P1-149..152 (4 IDs) | #55 `oh-my-claudecode:tracer` (omc family 12th burn, AUDIT pivot 36th) | SKIP |
| E | reconciler | merge + sweep | (uses unused IDs from above ranges if needed) | (no slot — reconciler is integrator) | (validates batch 42 p.412 result + 6th recurrence watch) |

### §0.3 SKILL-vs-AGENT pre-allocation lint (v1.6 §0 codification)

✅ Slot #54 `general-purpose` verified AGENT (top-level family 4th burn extension; precedent chain #28 round 5 1st burn inaugural + #41 round 7 2nd burn G-MS-4 1st LIVE-FIRE fallback + #51 round 9 3rd burn extension validation + #54 round 10 4th burn extension); recipe family-agnostic at 4-burn intra-family depth scale validated post round 10 batch 42.

### §0.4 Halt fallback (G-MS-4 STRONGLY VALIDATED + 6th recurrence escalation)

Two halt triggers:
- **G-MS-4 standard**: pre-allocated reviewer unavailable / shared-file write attempts / failure rate >15% / Rule A <70% post-Option-H / ctx >80%
- **6TH CUMULATIVE WRITER-DIRECTION VALUE HALLUCINATION RECURRENCE escalation** (NEW v1.6 N18 halt threshold): if drift cal p.412 reveals 6th cumulative recurrence DESPITE v1.6 N18 EXTENDED scope dispatch (writer-family BANNED for content covered by N18 sub-rules a-e + writer dispatched per N18 PERMITTED narrow content type): ESCALATE to v1.7 trigger = **deprecate writer-family entirely from P1 atomization**. Action: write `halt_state_batch_42.md` + 4 resume options + halt signal `HALT_BATCH_42 reason=6th_writer_direction_recurrence_v1.7_trigger`.

## §1 — Background

- Round 10 = **1st round running v1.6 baseline** post v1.6 cut 2026-04-29 (commit `5e2b953`)
- v1.6 active prompts: `subagent_prompts/P0_writer_pdf_v1.6.md` etc.
- Round 9 cumulative state pre-batch-42: 9828 atoms / 400 pages / 40 batches / Rule D 52 / 33 AUDIT pivots / 11 active families
- **Drift cal cumulative writer-direction VALUE HALLUCINATION tracking**: 5 cumulative recurrences post round 5+6+7+8+9 (last = round 9 batch 39 p.382 on `mixed_structural_transition` content type DESPITE N16 v1.5 PERMISSION = 5th recurrence triggered v1.6 N18 EXTENDED scope codification)
- Expected post-batch-42 contribution: ~150-250 atoms (10 pages, examples-narrative continuation region)

## §2 — Required Reads (parallel)

1. `subagent_prompts/P0_writer_pdf_v1.6.md` (200 lines, N18 EXTENDED scope dispatch + Self-Validate hooks 17→20)
2. `subagent_prompts/P0_reviewer_v1.6.md` (145 lines, fix matrix 28 items A-AB)
3. `multi_session/MULTI_SESSION_PROTOCOL.md` (master)
4. `multi_session/MULTI_SESSION_RETRO_ROUND_9.md` (round 9 retro — esp. drift cal batch 39 p.382 5th recurrence motif analysis)
5. `evidence/checkpoints/drift_cal_batch_39_p382_report.md` (round 9 drift cal 9th time FAIL motif analysis — UNDERSTAND BEFORE running batch 42 drift cal 10th time)
6. `evidence/checkpoints/v1_6_cut_reviewer_report.md` (codex audit verdict 28/28 SAFE_FOR_DAISY_ACK)
7. `_progress.json` (v1_6_cut_details + round_9_compliance + recovery_hint)

## §3 — Sub-batch dispatch protocol (N18 EXTENDED scope dispatch)

### §3.1 42a (p.411-415) content_type assessment

**TOC ground truth (verify pre-dispatch via `Read source/SDTMIG\ v3.4\ \(no\ header\ footer\).pdf p.411-415`)**:
- p.411: §7.3.1 Trial Visits (TV) Examples L4 Examples 1+2 (cross-batch continuation from sister batch 41 territory)
- p.412: **DRIFT CAL TARGET PAGE** (10th time NEW1 dual-threshold) + TV L5 Examples deep-interior
- p.413: §7.3.2 Trial Disease Assessments (TD) L3 NEW + TD L4 leaf-pattern chain Description/Specification
- p.414-415: TD Assumptions / Examples + TD L5 Example 1+2

**Content type assessment**: Mix of `examples_narrative_spec_table` (TV/TD examples) + `mixed_structural_transition` (§7.3.2 TD L3 NEW transition)

**v1.6 N18 dispatch**: executor MANDATORY (per N18.a Examples-narrative + spec-table OR N18.e mixed_structural_transition).

### §3.2 42b (p.416-420) content_type assessment

**TOC ground truth**:
- p.416-417: TD L5 Examples continuation + ~spec-table-heavy
- p.418: §7.3.3 Trial Summary (TS) L3 NEW + TS L4 leaf-pattern chain
- p.419-420: TS Examples / TI Trial Inclusion/Exclusion (TI) L3 NEW + TI L4 chain start

**Content type assessment**: `mixed_structural_transition` heavy + `examples_narrative_spec_table` mix

**v1.6 N18 dispatch**: executor MANDATORY.

### §3.3 N14 strict alternation (4th live-fire opportunity, drift cal carrier)

Drift cal at p.412 = 10th time NEW1 dual-threshold. Per v1.6 N14 STRONGLY VALIDATED post 3rd live-fire methodology:
- Baseline = 42a executor (per content-type-binding N18.a/e MANDATORY)
- Rerun = writer? **NO** — writer-family BANNED for ALL content in batch 42 per v1.6 N18 EXTENDED scope (URLs / Examples / mixed_structural_transition).

**Drift cal alternation v1.6 ESCALATION**: if writer-family BANNED for both baseline + rerun (impossible to alternate writer ↔ executor cross-family for direction-attribution), use **EXECUTOR-VARIANT alternation** instead: baseline = `oh-my-claudecode:executor` (same as 42a), rerun = `oh-my-claudecode:writer` (writer-family) BUT only for direction-attribution validation purpose. The rerun atoms NOT merged to root regardless.

This is a v1.6 NEW alternation pattern: same-content-type direction-attribution via writer-family rerun (not merged) to validate N18 EXTENDED scope EFFECTIVENESS at preventing writer-direction VALUE HALLUCINATION at content-type level.

**Expected outcome**: if N18 working as designed, writer rerun should produce 6th cumulative writer-direction VALUE HALLUCINATION recurrence (URL fabrication / word deletion / TABLE_ROW truncation patterns analogous to round 9 batch 39 p.382). 6th recurrence DETECTED → v1.7 trigger ESCALATION (deprecate writer-family entirely from P1 atomization).

If 6th recurrence NOT detected (writer rerun PASS dual-threshold both ≥80%): N18 EXTENDED scope EFFECTIVE, writer-family deprecation NOT YET justified, continue v1.6 baseline through round 10+.

### §3.4 INTRA-AGENT consistency check (N6 v1.6 carry-forward)

Both 42a + 42b same executor agent → INTRA-AGENT consistency check applies. 42b dispatch prompt MUST inline-prepend 42a 终态.

### §3.5 N18 EXTENDED scope sub-rule pre-dispatch scan

Main session pre-dispatch scan (per N18 Hook 16.6 pseudo-code 5 sub-rules a-e):
- N18.a (Examples-narrative + spec-table): YES (TV/TD/TS Examples regions p.411-420)
- N18.b (URLs/DOIs): scan for `https?://` matches + DOI patterns
- N18.c (TABLE_ROW ≥500 chars): scan for long-cell patterns
- N18.d (general VERBATIM-CRITICAL): citation patterns / TS Spec table SDISGNTYP/SD codes / clinical trial registry IDs
- N18.e (mixed_structural_transition): YES (§7.3.2 TD + §7.3.3 TS + §7.3.4 TI L3 NEW transitions in 42b)

Result: executor MANDATORY for both 42a + 42b.

## §4 — Workflow per atom (v1.6 carry-forward)

参 `subagent_prompts/P0_writer_pdf_v1.6.md` §任务流程 8 steps + Self-Validate hooks 1-20.

## §5 — Drift cal protocol (10th time NEW1 dual-threshold)

### §5.1 Drift cal target

- **Page**: p.412 (10th time NEW1 dual-threshold cumulative)
- **Trigger**: per cadence every-3-batches batch 39→42 + cumulative atoms post-p.382 ≥600 双触发
- **Baseline**: 42a executor (atoms emitted at p.412 in normal Step 1-7 workflow)
- **Rerun**: `oh-my-claudecode:writer` (writer-family) — same page p.412, independent reproduction (no read of baseline output) — **NOT merged to root** regardless of verdict (artifact preserved as `drift_cal_p412_writer_rerun.jsonl`)

### §5.2 Dual-threshold metrics (v1.6 carry-forward NEW1)

- **Strict count overlap**: |intersection| / max(|baseline|, |rerun|) ≥ 80%
- **Verbatim hash Jaccard**: |intersection_verbatim_hashes| / |union_verbatim_hashes| ≥ 80%
- **Both thresholds PASS** = DRIFT CAL VERDICT PASS (no halt)
- **Single threshold FAIL** = VERDICT FAIL but NOT halt-condition (analogous to round 9 batch 39 strict 100% PASS / verbatim 69.2% FAIL = single-threshold FAIL but root atoms executor-clean preserved)
- **Both thresholds FAIL (BOTH <80%)** = halt-condition per G-MS-4 fallback

### §5.3 6th cumulative writer-direction VALUE HALLUCINATION recurrence WATCH

Per v1.6 N18 EXTENDED scope halt threshold: if drift cal p.412 rerun reveals 6th cumulative writer-direction VALUE HALLUCINATION recurrence (URL fabrication motif analogous round 9 batch 39 p.382 ig34_p0382_a004 .org→.ch / word deletion / TABLE_ROW truncation), ESCALATE to v1.7 trigger = **deprecate writer-family entirely from P1 atomization**.

Halt action: write `halt_state_batch_42.md` + 4 resume options:
- Option A: User authorizes Option H bulk repair via executor rerun on hallucinated atoms (analogous to round 8 batch 36 user-authorized RESUME_BATCH_36 option=A)
- Option B: User authorizes v1.7 cut session START (immediate writer-family deprecation across all v1.7 prompts)
- Option C: User authorizes batch 42 closure with FAIL verdict + escalation noted in retro
- Option D: User authorizes session pause for re-strategize

If 6th recurrence NOT detected (drift cal verdict PASS BOTH thresholds OR single-threshold FAIL with content-attribution to non-writer-direction motifs): continue STEP 7 closure normally; document N18 EXTENDED scope EFFECTIVE (1st cumulative INAUGURAL live-fire success).

### §5.4 Drift cal value-add precedent tracking

- 9 prior drift cal runs cumulative round 1-9 (p.25/60/89/118/147/180/205/233/270/293/325/357/382 = 13 cumulative drift cals)
- Direction REVERSED 12 cumulative precedents (round 1-9 + round 9 batch 39 = 12)
- Value-add 13 cumulative precedents
- Round 10 batch 42 = 10th cumulative drift cal carrier + 14th cumulative drift cal run

## §6 — Halt fallback (combined G-MS-4 + 6th recurrence escalation)

参 §0.4 above. Action: write `halt_state_batch_42.md` per round 7 batch 32 1st live-fire + round 8 batch 36 2nd live-fire precedent.

## §7 — STEP 7 DONE echo

After all atoms emitted + schema sweep PASS + drift cal p.412 result + Rule A audit slot #54 PASS ≥80% threshold + atoms written:

```
PARALLEL_SESSION_42_DONE atoms=<N> failures=<N> repair_cycles=<N> rule_a=<NN.N>% drift_cal=triggered_strict=<NN.N>%_verbatim=<NN.N>%_verdict=<PASS|FAIL_single|FAIL_both> 6th_recurrence_watch=<NOT_detected|DETECTED_v1.7_trigger> findings_added=<list-or-none-O-P1-145..148-reserved-unused>
```

Halt signal alternative: `HALT_BATCH_42 reason=<X>` (write halt_state_batch_42.md per G-MS-4 STRONGLY VALIDATED protocol).

## §8 — DO NOT TOUCH (reconciler scope)

- root `pdf_atoms.jsonl` (9828 atoms baseline post round 9 — reconciler scope)
- `audit_matrix.md`
- `_progress.json` (root)
- sister batch files (`pdf_atoms_batch_41*`, `pdf_atoms_batch_43*`)
- `subagent_prompts/*` (v1.6 active 不动)
- `schema/*.json`
- `PLAN.md` / `plans/*.md`
- `CLAUDE.md` / `MEMORY/*` (project-scope)

## §9 — Rule A reviewer slot #54 specific notes

`general-purpose` 4th burn extension (precedent chain #28 round 5 1st burn inaugural + #41 round 7 2nd burn G-MS-4 1st LIVE-FIRE fallback + #51 round 9 3rd burn extension validation + #54 round 10 4th burn extension). full-tool variant Branch A direct write per v1.6 §Step 4 (round 9 #51 confirmed full-tool Branch A direct write at intra-family-3rd-burn depth; round 10 #54 sustains at 4-burn intra-family depth).

AUDIT-mode pivot reflection (3-axis analogy general-purpose extension):
1. **General research / multi-step task ↔ multi-axis atom audit (verbatim + atom_type + parent_section + heading chain)**
2. **Open-ended question search ↔ atom edge case discovery (NEW HEADING / atom_type 9-enum boundary)**
3. **Code finding ↔ atom finding (with severity rating)**

Recipe family-agnostic at 4-burn intra-family depth scale validated post round 10 batch 42 (sustains 3-burn validation post round 9).

10-atom sample 1/page p.411-420 stratified, seed=20260429.

═══════════════════════════════════════════════════════════════════
The boulder never stops. STEP 0 pre-flight check first (verify reviewer #54 general-purpose in agent registry; if unavailable → G-MS-4 halt protocol + NB: drift cal alternation 6th recurrence WATCH is critical for v1.7 trigger detection).
