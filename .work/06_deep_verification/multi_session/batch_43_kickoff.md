# Batch 43 Kickoff — Round 10 (Session D, post v1.6 cut)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-7 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法停止信号 = STEP 7 末尾 echo 单行 `PARALLEL_SESSION_43_DONE atoms=N failures=N repair_cycles=N rule_a=NN.N% drift_cal=skipped findings_added=...` OR halt 信号 `HALT_BATCH_43 reason=<X>` (per G-MS-4 STRONGLY VALIDATED halt fallback)
> ═══════════════════════════════════════════════════════════════════

## §0 — Pre-flight (Cross-validation table + AGENT-vs-SKILL pre-allocation lint)

### §0.1 Round 10 multi-session kickoff context

3 sister sessions B/C/D 物理并行 batches 41/42/43 + reconciler E 串行收尾 (round 10 = 1st round running v1.6 baseline post v1.6 cut 2026-04-29).

### §0.2 Cross-validation table (G-MS-13 codification)

| Session | Batch | Page range | Atoms reserved finding ID range | Reviewer slot pre-allocation | Drift cal |
|---|---|---|---|---|---|
| B | 41 | p.401-410 | O-P1-141..144 (4 IDs) | #53 `oh-my-claudecode:verifier` (omc family 11th burn, AUDIT pivot 34th) | SKIP |
| C | 42 | p.411-420 | O-P1-145..148 (4 IDs) | #54 `general-purpose` (4th burn extension, AUDIT pivot 35th) | MANDATORY p.412 (10th time) + 6th recurrence WATCH |
| D (this) | **43** | p.421-430 | O-P1-149..152 (4 IDs) | **#55 `oh-my-claudecode:tracer`** (omc family 12th burn intra-family depth, AUDIT pivot 36th, D-MS-7 candidate "tracer-strategist") | SKIP (next mandatory batch 45) |
| E | reconciler | merge + sweep | (uses unused IDs from above ranges if needed) | (no slot — reconciler is integrator) | (validates batch 42 p.412 result) |

### §0.3 SKILL-vs-AGENT pre-allocation lint (v1.6 §0 codification)

✅ Slot #55 `oh-my-claudecode:tracer` verified AGENT (per v1.6 §0 roster — omc-family un-burned AUDIT-suitable; analogous to round 9 batch 39 #50 `oh-my-claudecode:planner` D-MS-7 candidate "planner-strategist" 1st live-fire EFFECTIVE).

### §0.4 Halt fallback (G-MS-4 STRONGLY VALIDATED)

If pre-allocated reviewer agent unavailable: execute G-MS-4 protocol per round 7 batch 32 1st live-fire + round 8 batch 36 2nd live-fire precedent: write `evidence/checkpoints/halt_state_batch_43.md` + 4 resume options.

## §1 — Background

- Round 10 = **1st round running v1.6 baseline** post v1.6 cut 2026-04-29 (commit `5e2b953`)
- v1.6 active prompts: `subagent_prompts/P0_writer_pdf_v1.6.md` etc.
- Round 9 cumulative state pre-batch-43: 9828 atoms / 400 pages / 40 batches / Rule D 52 / 33 AUDIT pivots / 11 active families
- Expected post-batch-43 contribution: ~150-250 atoms (10 pages, examples-narrative deep-interior region)

## §2 — Required Reads (parallel)

1. `subagent_prompts/P0_writer_pdf_v1.6.md` (200 lines, N18 EXTENDED scope dispatch)
2. `subagent_prompts/P0_reviewer_v1.6.md` (145 lines, fix matrix 28 items A-AB)
3. `multi_session/MULTI_SESSION_PROTOCOL.md` (master)
4. `multi_session/MULTI_SESSION_RETRO_ROUND_9.md` (round 9 retro for context)
5. `evidence/checkpoints/v1_6_cut_reviewer_report.md` (codex audit verdict 28/28 SAFE_FOR_DAISY_ACK)
6. `_progress.json` (v1_6_cut_details + round_9_compliance + recovery_hint)

## §3 — Sub-batch dispatch protocol (N18 EXTENDED scope dispatch)

### §3.1 43a (p.421-425) content_type assessment

**TOC ground truth (verify pre-dispatch via `Read source/SDTMIG\ v3.4\ \(no\ header\ footer\).pdf p.421-425`)**:
- p.421-422: §7.3.4 TI L4 leaf-pattern chain Description/Specification/Assumptions/Examples + TI L5 Examples 1-N
- p.423: §7.3.5 Trial Element Definitions (TM) L3 NEW (under §7.3 L2 parent — chapter-short-bracket all-caps per N11)
- p.424: TM L4 leaf-pattern chain Description/Specification
- p.425: TM Assumptions / Examples

**Content type assessment**: `mixed_structural_transition` (§7.3.5 TM L3 NEW + L4 chain start) + `examples_narrative_spec_table` (TI/TM Examples)

**v1.6 N18 dispatch**: executor MANDATORY (per N18.a Examples-narrative+spec-table OR N18.e mixed_structural_transition).

### §3.2 43b (p.426-430) content_type assessment

**TOC ground truth**:
- p.426-427: TM L5 Examples + §7.4 (if exists) TBD
- p.428-430: continuation deep-interior; possible §7.5 / §7.6 chapters TBD

**Content type assessment**: TBD per actual TOC verification — likely mix of `examples_narrative_spec_table` + occasional `mixed_structural_transition` at chapter boundaries

**v1.6 N18 dispatch**: executor MANDATORY (default for content-type N18 EXTENDED scope wins).

### §3.3 N14 alternation (no drift cal this batch)

For batch 43 (no drift cal): both 43a + 43b dispatched executor per N18 MANDATORY content-type binding (no alternation possible / not required for this batch).

### §3.4 INTRA-AGENT consistency check (N6 v1.6 carry-forward)

Both 43a + 43b same executor agent → INTRA-AGENT consistency check applies. 43b dispatch prompt MUST inline-prepend 43a 终态.

### §3.5 N18 EXTENDED scope sub-rule pre-dispatch scan

Main session pre-dispatch scan (per N18 Hook 16.6 pseudo-code 5 sub-rules a-e):
- N18.a (Examples-narrative + spec-table): YES (TI/TM Examples regions)
- N18.b (URLs/DOIs): scan for matches
- N18.c (TABLE_ROW ≥500 chars): scan
- N18.d (general VERBATIM-CRITICAL): citation patterns / TS Spec table SDISGNTYP / regulatory codes
- N18.e (mixed_structural_transition): partial (§7.3.5 TM L3 NEW + possible §7.4+ chapters)

Result: executor MANDATORY for both 43a + 43b.

## §4 — Workflow per atom (v1.6 carry-forward)

参 `subagent_prompts/P0_writer_pdf_v1.6.md` §任务流程 8 steps + Self-Validate hooks 1-20.

## §5 — Drift cal (SKIP this batch; next mandatory batch 45)

Drift cal NOT triggered for batch 43 per cadence (last drift cal batch 42 p.412; next mandatory batch 45 p.442 per every-3-batches cadence).

## §6 — Halt fallback (G-MS-4 STRONGLY VALIDATED)

If 6th cumulative writer-direction VALUE HALLUCINATION recurrence detected via INTRA-AGENT consistency check or schema sweep finding (DESPITE v1.6 N18 EXTENDED scope dispatch): ESCALATE to v1.7 trigger via halt_state_batch_43.md + 4 resume options analogous to batch 42 §6.

## §7 — STEP 7 DONE echo

After all atoms emitted + schema sweep PASS + Rule A audit slot #55 PASS ≥80% threshold + atoms written to `evidence/checkpoints/pdf_atoms_batch_43a.jsonl` + `pdf_atoms_batch_43b.jsonl` + `_progress_batch_43.json` + `P1_batch_43_report.md`:

```
PARALLEL_SESSION_43_DONE atoms=<N> failures=<N> repair_cycles=<N> rule_a=<NN.N>% drift_cal=skipped findings_added=<list-or-none-O-P1-149..152-reserved-unused>
```

Halt signal alternative if HALT triggered: `HALT_BATCH_43 reason=<X>` (write halt_state_batch_43.md per G-MS-4 STRONGLY VALIDATED protocol).

## §8 — DO NOT TOUCH (reconciler scope)

- root `pdf_atoms.jsonl` (9828 atoms baseline post round 9 — reconciler scope)
- `audit_matrix.md`
- `_progress.json` (root)
- sister batch files (`pdf_atoms_batch_41*`, `pdf_atoms_batch_42*`)
- `subagent_prompts/*` (v1.6 active 不动)
- `schema/*.json`
- `PLAN.md` / `plans/*.md`
- `CLAUDE.md` / `MEMORY/*` (project-scope)

## §9 — Rule A reviewer slot #55 specific notes

`oh-my-claudecode:tracer` 是 omc-family 12th burn intra-family depth — D-MS-7 candidate "tracer-strategist". 此 slot 是 round 10 round 9 #50 omc:planner "planner-strategist" 1st live-fire EFFECTIVE 的 sister extension burn, 验证 D-MS-7 candidate validation 模式可重复 in 同 family (omc) at intra-family-12th-burn depth scale.

AUDIT-mode pivot reflection (3-axis analogy):
1. **Evidence-driven causal tracing ↔ atom verbatim PDF ground-truth chain-of-evidence verification**
2. **Competing hypotheses ↔ atom_type 9-enum classification multi-candidate evaluation**
3. **Uncertainty tracking + next-probe recommendations ↔ Rule A residual flagging + main-session structural sweep extension recommendations**

tracer 是 full-tool agent (Bash + Read + Grep + Glob + WebFetch + WebSearch + Write — 兼 tracing). Branch A direct-write Write-tool default per v1.6 §Step 4. AUDIT independence preserved.

10-atom sample 1/page p.421-430 stratified, seed=20260429.

═══════════════════════════════════════════════════════════════════
The boulder never stops. STEP 0 pre-flight check first (verify reviewer #55 oh-my-claudecode:tracer in agent registry; if unavailable → G-MS-4 halt protocol).
