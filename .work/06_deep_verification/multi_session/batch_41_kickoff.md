# Batch 41 Kickoff — Round 10 (Session B, post v1.6 cut)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-7 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法停止信号 = STEP 7 末尾 echo 单行 `PARALLEL_SESSION_41_DONE atoms=N failures=N repair_cycles=N rule_a=NN.N% drift_cal=skipped findings_added=...` OR halt 信号 `HALT_BATCH_41 reason=<X>` (per G-MS-4 STRONGLY VALIDATED halt fallback)
> ═══════════════════════════════════════════════════════════════════

## §0 — Pre-flight (Cross-validation table + AGENT-vs-SKILL pre-allocation lint)

### §0.1 Round 10 multi-session kickoff context

3 sister sessions B/C/D 物理并行 batches 41/42/43 + reconciler E 串行收尾 (round 10 = 1st round running v1.6 baseline post v1.6 cut 2026-04-29).

### §0.2 Cross-validation table (G-MS-13 codification)

| Session | Batch | Page range | Atoms reserved finding ID range | Reviewer slot pre-allocation | Drift cal |
|---|---|---|---|---|---|
| B (this) | **41** | p.401-410 | O-P1-141..144 (4 IDs) | **#53 `oh-my-claudecode:verifier`** (omc family 11th burn intra-family depth, AUDIT pivot 34th, D-MS-7 candidate "verifier-strategist") | SKIP (next mandatory batch 42) |
| C | 42 | p.411-420 | O-P1-145..148 (4 IDs) | #54 `general-purpose` (4th burn extension, AUDIT pivot 35th) | **MANDATORY (10th time NEW1 dual-threshold per cadence batch 39→42 + cumulative atoms post-p.382 ≥600 双触发)** |
| D | 43 | p.421-430 | O-P1-149..152 (4 IDs) | #55 `oh-my-claudecode:tracer` (omc family 12th burn intra-family depth, AUDIT pivot 36th, D-MS-7 candidate "tracer-strategist") | SKIP |
| E | reconciler | merge + sweep | (N/A — uses unused IDs from above ranges if needed) | (no slot — reconciler is integrator) | (validates batch 42 p.412 result) |

### §0.3 SKILL-vs-AGENT pre-allocation lint (v1.6 §0 codification)

✅ Slot #53 `oh-my-claudecode:verifier` verified AGENT (per v1.6 §0 roster — omc-family un-burned AUDIT-suitable; round 9 batch 39 lint EFFECTIVE 1st live-fire precedent).
✅ Slot #54 `general-purpose` verified AGENT (top-level family 4th burn extension).
✅ Slot #55 `oh-my-claudecode:tracer` verified AGENT (per v1.6 §0 roster — omc-family un-burned AUDIT-suitable).

No SKILL pre-allocation. Pre-dispatch lint PASS for all 3 round 10 reviewer slots.

### §0.4 Halt fallback (G-MS-4 STRONGLY VALIDATED)

If pre-allocated reviewer agent unavailable in session registry: execute G-MS-4 protocol per round 7 batch 32 1st live-fire + round 8 batch 36 2nd live-fire precedent: write `evidence/checkpoints/halt_state_batch_41.md` + present 4 resume options to user.

## §1 — Background

- Round 10 = **1st round running v1.6 baseline** post v1.6 cut 2026-04-29 (commit `5e2b953`)
- v1.6 active prompts: `subagent_prompts/P0_writer_pdf_v1.6.md` + `P0_writer_md_v1.6.md` + `P0_matcher_v1.6.md` + `P0_reviewer_v1.6.md` (v1.5 archived to `archive/v1.5_final_2026-04-29/`)
- Round 9 cumulative state pre-batch-41: 9828 atoms / 400 pages / 40 batches / Rule D 52 (post v1.6 cut #52) / 33 AUDIT pivots / 11 active families
- Expected post-batch-41 contribution: ~150-250 atoms (10 pages, transition-heavy region)

## §2 — Required Reads (parallel)

1. `subagent_prompts/P0_writer_pdf_v1.6.md` (200 lines, 5 sub-rules a-e dispatch + Self-Validate hooks 17→20)
2. `subagent_prompts/P0_reviewer_v1.6.md` (145 lines, fix matrix 28 items A-AB + AGENT-vs-SKILL roster + §0.5 reconciler-side cross-session canonical-form drift sweep)
3. `multi_session/MULTI_SESSION_PROTOCOL.md` (master)
4. `multi_session/MULTI_SESSION_RETRO_ROUND_9.md` (round 9 retro for context — N18 EXTENDED scope rationale)
5. `evidence/checkpoints/v1_6_cut_reviewer_report.md` (codex audit verdict 28/28 SAFE_FOR_DAISY_ACK)
6. `_progress.json` (v1_6_cut_details + round_9_compliance + recovery_hint round 9 narrative)

## §3 — Sub-batch dispatch protocol (N18 EXTENDED scope dispatch)

### §3.1 41a (p.401-405) content_type assessment

**TOC ground truth (verify pre-dispatch via `Read source/SDTMIG\ v3.4\ \(no\ header\ footer\).pdf p.401-405`)**:
- p.401: §7.2.1 Trial Arms (TA) tail (Example 7 RTOG continuation from sister batch 40)
- p.402: **§7.2.1.1 Trial Arms Issues L4 NEW** (under §7.2.1 TA L3 parent) + **§7.2.2 Trial Elements (TE) L3 NEW** (under §7.2 [EXPERIMENTAL DESIGN (TA AND TE)] L2 parent, chapter-short-bracket all-caps per N11)
- p.403-404: TE L4 leaf-pattern chain Description/Specification/Assumptions
- p.405: TE Examples L4 NEW + Example 1 L5 NEW + **§7.2.2.1 Trial Elements Issues L4 NEW** (under §7.2.2 TE L3 parent)

**Content type assessment**: `mixed_structural_transition` heavy (4+ NEW HEADING transitions in 5 pages = HIGHEST mixed_structural_transition density predicted)

**v1.6 N18.e dispatch**: executor MANDATORY (was PREFERRED in v1.5 N16; now MANDATORY per v1.6 N18.e post 5th cumulative writer-direction VALUE HALLUCINATION recurrence on mixed_structural_transition).

**Dispatch**: `oh-my-claudecode:executor` MANDATORY (writer-family BANNED).

### §3.2 41b (p.406-410) content_type assessment

**TOC ground truth**:
- p.406: §7.2.2.1 TE Issues continuation
- p.407: **§7.3 [SCHEDULE FOR ASSESSMENTS (TV, TD, AND TM)] L2 NEW** (chapter-short-bracket all-caps per N11) + §7.3.1 Trial Visits (TV) L3 NEW
- p.408-409: TV L4 leaf-pattern chain Description/Specification/Assumptions/Examples
- p.410: TV L5 Examples 1-N

**Content type assessment**: `mixed_structural_transition` continued (L2 chapter NEW + L3 sub-section NEW + L4 leaf-pattern chain + L5 Examples)

**v1.6 N18.e dispatch**: executor MANDATORY.

### §3.3 N14 alternation (3rd live-fire methodology STRONGLY VALIDATED)

Per round 9 batch 39 3rd live-fire methodology confirmation: alternation table spec is baseline writer ↔ rerun executor or vice versa for drift cal direction-attribution.

For batch 41 (no drift cal): both 41a + 41b dispatched executor per N18.e MANDATORY content-type binding (no alternation possible / not required for this batch).

### §3.4 INTRA-AGENT consistency check (N6 v1.6 carry-forward)

Both 41a + 41b same executor agent → INTRA-AGENT consistency check applies. 41b dispatch prompt MUST inline-prepend 41a 终态 (last L4/L5 sib + last L6 sib + active heading state) per round 5 D-MS-4 codification + round 6/7/8/9 5 cumulative live-fires EFFECTIVE.

### §3.5 N18 EXTENDED scope sub-rule pre-dispatch scan

Main session pre-dispatch scan (per N18 Hook 16.6 pseudo-code):
- N18.a (Examples-narrative + spec-table): partially applicable (TE/TV Examples L5 + TV L5 1-N)
- N18.b (URLs/DOIs): scan p.401-410 for `https?://` matches → main session scan + report `n18_url_atoms_count`
- N18.c (TABLE_ROW ≥500 chars): scan for long-cell patterns → report `n18_long_cell_atoms_count`
- N18.d (general VERBATIM-CRITICAL): main session judgment — citation patterns / clinical trial registry IDs / publication identifiers
- N18.e (mixed_structural_transition): YES (highest density predicted)

Result: executor MANDATORY for both 41a + 41b. 41b inherits same content-type-binding constraint.

## §4 — Workflow per atom (v1.6 carry-forward)

参 `subagent_prompts/P0_writer_pdf_v1.6.md` §任务流程 8 steps + Self-Validate hooks 1-20:
- Steps 1-6 (atom emission): R1-R15 + N1-N17 carry-forward unchanged
- Step 7 (v1.5 N17 post-extraction VALIDATION pass): Hook 15 cross-row pipe-count + Hook 16 USUBJID format + Hook 17 multi-axis spot-check N=3
- Step 8 (v1.6 NEW per N19 + N20): Hook 18 SENTENCE-paragraph-concat WARN-mode + Hook 19 PDF-cross-verify N=10 + mandatory URL/DOI/citation cross-check + Hook 20 (parent_section, table_id) granularity pipe-count

## §5 — Drift cal (SKIP this batch; next mandatory batch 42)

Drift cal NOT triggered for batch 41 per cadence (last drift cal batch 39 p.382; next mandatory batch 42 p.412 per every-3-batches cadence + cumulative atoms post-p.382 ≥600 双触发 trigger).

## §6 — Halt fallback (G-MS-4 STRONGLY VALIDATED)

Trigger conditions: failure rate >15% / Rule A <70% post-Option-H / ctx >80% / pre-allocated reviewer unavailable / shared-file write attempts. Action: write `evidence/checkpoints/halt_state_batch_41.md` + 4 resume options + halt signal `HALT_BATCH_41 reason=<X>`.

If 6th cumulative writer-direction VALUE HALLUCINATION recurrence detected (DESPITE v1.6 N18 EXTENDED scope dispatch): ESCALATE to v1.7 trigger = deprecate writer-family entirely from P1 atomization (special halt + escalate to user).

## §7 — STEP 7 DONE echo

After all atoms emitted + schema sweep PASS + Rule A audit slot #53 PASS ≥80% threshold + atoms written to `evidence/checkpoints/pdf_atoms_batch_41a.jsonl` + `pdf_atoms_batch_41b.jsonl` + `_progress_batch_41.json` + `P1_batch_41_report.md`:

```
PARALLEL_SESSION_41_DONE atoms=<N> failures=<N> repair_cycles=<N> rule_a=<NN.N>% drift_cal=skipped findings_added=<list-or-none-O-P1-141..144-reserved-unused>
```

Halt signal alternative if HALT triggered: `HALT_BATCH_41 reason=<X>` (write halt_state_batch_41.md per G-MS-4 STRONGLY VALIDATED protocol).

## §8 — DO NOT TOUCH (reconciler scope)

- root `pdf_atoms.jsonl` (9828 atoms baseline post round 9 — reconciler scope)
- `audit_matrix.md`
- `_progress.json` (root)
- sister batch files (`pdf_atoms_batch_42*`, `pdf_atoms_batch_43*`)
- `subagent_prompts/*` (v1.6 active 不动)
- `schema/*.json`
- `PLAN.md` / `plans/*.md`
- `CLAUDE.md` / `MEMORY/*` (project-scope)

## §9 — Rule A reviewer slot #53 specific notes

`oh-my-claudecode:verifier` 是 omc-family 11th burn intra-family depth — D-MS-7 candidate "verifier-strategist". 此 slot 是 v1.6 cut 后 first round 10 reviewer dispatch, 验证 D-MS-7 candidate validation 模式可重复. 

AUDIT-mode pivot reflection (3-axis analogy):
1. **Verification strategy ↔ atom verbatim PDF ground-truth verification**
2. **Evidence-based completion checks ↔ atom_type 9-enum classification correctness via PDF cross-check**
3. **Test adequacy ↔ atom coverage adequacy + parent_section canonical-form precision**

verifier 是 full-tool agent (Bash + Read + Grep + Glob + WebFetch + WebSearch + Write — 验证). Branch A direct-write Write-tool default per v1.6 §Step 4. AUDIT independence preserved.

10-atom sample 1/page p.401-410 stratified, seed=20260429.

═══════════════════════════════════════════════════════════════════
The boulder never stops. STEP 0 pre-flight check first (verify reviewer #53 oh-my-claudecode:verifier in agent registry; if unavailable → G-MS-4 halt protocol).
