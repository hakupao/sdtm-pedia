# Batch 39 Kickoff — Round 9 Multi-Session Parallel (Session C, **MANDATORY DRIFT CAL**)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-7 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 7 单行 echo:
> ```
> PARALLEL_SESSION_39_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered drift_cal_strict=<X>% drift_cal_verbatim=<Y>% findings_added=<list>
> ```
> ═══════════════════════════════════════════════════════════════════

## §0 — Cross-validation Table (G-MS-13)

| Session | Batch | Page range | Finding ID 范围 | 本 batch 用 |
|---|---|---|---|---|
| B (sister) | 38 | p.371-380 | O-P1-129..132 (4 reserved) | (sister) |
| **C (本)** | **39** | **p.381-390** | **O-P1-133..136** (4 reserved) | ✅ |
| D (sister) | 40 | p.391-400 | O-P1-137..140 (4 reserved) | (sister) |
| E (reconciler) | n/a | n/a | O-P1-141+ (overflow) | (reconciler) |

**Self-validation gate** (STEP 7): any finding_id ∉ {133,134,135,136} → STOP fix.

## §0.5 — SKILL-vs-AGENT pre-allocation lint (v1.5 N15+ G-MS-NEW-8-1 codification)

**🔴 round 8 O-P1-121 recurring O-P1-110 motif lint mandatory** — pre-dispatch verify reviewer slot is registered AGENT, NOT SKILL:

| Slot | Type | Status |
|---|---|---|
| #49 (sister batch 38) | `Explore` (top-level capital E) | ✅ AGENT (not skill) |
| #50 (本 batch 39) | `oh-my-claudecode:planner` | ✅ AGENT (not skill, omc 10th burn) |
| #51 (sister batch 40) | `general-purpose` | ✅ AGENT (not skill, 3rd burn extension) |

If pre-allocated reviewer fails registry check at dispatch → halt + write `halt_state_batch_39.md` + 4 resume options A-D + wait user auth per G-MS-4 STRONGLY VALIDATED protocol.

## §1 — Background

- Round 9 第 9 轮 multi-session; v1.5 prompts ACTIVE since 2026-04-28
- Reviewer slot 已预分配: batch 39 = #50 `oh-my-claudecode:planner` (**omc family 10th burn intra-family depth — D-MS-7 round 8 candidate "planner-strategist" validated**; drift cal carrier 9th time; AUDIT pivot 31st cumulative; full-tool variant)
- Round 9 protocol sustains round 7-8 spec: G-MS-4 halt fallback **STRONGLY VALIDATED** + G-MS-7 finding ID range pre-allocation + G-MS-13 cross-validation table + N14 strict alternation methodology procedural enforcement **STRONGLY VALIDATED** (本 batch 必触 — drift cal mandatory)
- 🔴 **DRIFT CAL MANDATORY 本 batch (batch 39)** per cadence batch 36→39 (3-batch interval) + cumulative atoms post-p.357 expected ≥600 双触发, per v1.4 N14 STRONGLY VALIDATED strict alternation table:
  ```
  | Baseline subagent_type     | Rerun subagent_type        |
  | oh-my-claudecode:writer    | oh-my-claudecode:executor  |
  | oh-my-claudecode:executor  | oh-my-claudecode:writer    |
  ```
  Round 8 batch 36 NEW1 8th time CATASTROPHIC FAIL writer-direction VALUE HALLUCINATION 4th cumulative recurrence main-line → N3 NEW8.d EMERGENCY-CRITICAL halt 1st live-fire EFFECTIVE → G-MS-4 2nd LIVE-FIRE EFFECTIVE → STRONGLY VALIDATED. **Round 9 batch 39 = 9th cumulative drift cal carrier; v1.5 N16 writer-family ban for Examples-narrative + spec-table content type now ACTIVE — if drift cal target page is Examples-narrative + spec-table content type, baseline MUST be executor (writer-family BANNED per N16); rerun goes to writer (alternation). If 5th cumulative writer-direction recurrence DESPITE N16 dispatch ban, ESCALATE to mandatory writer-family ban for ALL TABLE_ROW-heavy content type per v1.5 N16 escalation clause.**
  - Recommend dense Spec table OR Examples table page for drift cal target (TBD by 主 session post-39a baseline write)
- v1.4 N6 NEW7 L6 sub-batch handoff codification ACTIVE: extended to ALL L6 sub-headings + INTRA-AGENT consistency check
- v1.5 N15 .xpt-parent FORBID rule ACTIVE: pre-DONE hook 14.5 halt-on-violation
- v1.5 N17 post-extraction VALIDATION pass Self-Validate hooks 15-17 ACTIVE: per-batch pre-DONE
- 主 session dispatch batch 39a prompt MUST inline-prepend prior batch 38b 终态 (per cross-BATCH handoff codification + N6 v1.4)

## §2 — Required Reads (并行)

1. `.work/06_deep_verification/_progress.json` (recovery_hint + v1_5_cut_completed)
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.5.md` (144 lines, v1.5 N15-N17 + STRONGLY VALIDATED status + content-type-aware dispatch)
3. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.5.md` (131 lines, Rule D 48 slots + 25-item matrix A-Y + AGENT-vs-SKILL roster doc §0)
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (master 219 lines)
5. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_8.md` (round 8 retro — drift cal 8th time CATASTROPHIC FAIL + N3 NEW8.d 1st live-fire EFFECTIVE + G-MS-4 STRONGLY VALIDATED)
6. `source/SDTMIG v3.4 (no header footer).pdf` p.4-5 TOC (verify §6.4.5 SR tail / any §6.4.6+ or §6.5 transitions in p.381-390 scope)

**附读**: `evidence/checkpoints/_progress_batch_37.json` + `_progress_batch_38.json` (when available) — cross-batch handoff context

## §3 — Pre-shared State + Cross-Batch Handoff (N6 v1.4 mandatory + v1.5 N15/N16/N17 active)

```
PRIOR BATCH 38 HEADING STATE (batch 39 sub-batch a MUST continue, NOT restart):
- Last L2 chapter sib used: §6.4 [FINDINGS ABOUT EVENTS OR INTERVENTIONS] L2 sib=4 (batch 37 NEW, continuing in batches 38/39)
- Last L3 sib used (under §6.4 chapter): sib=5 (§6.4.5 Skin Response (SR) at p.375 leaf-pattern — head/L4 chain in batch 38; possibly extending into 39 OR completed)
- §6.4.5 SR L4 chain Description=1 / Spec=2 / Assumptions=3 / Examples=4 (per N9 leaf-pattern, status TBD by sister 38 actual emission)
- §6.4.5 SR L5 Examples N atoms per N10 leaf-pattern Examples-at-L5 (status TBD)
- Last L6 sib used: NONE expected (SR L4-leaf — Examples at L5 per N10)
- Last L7 sib used: NONE expected
- Convention: §6.4.X subsequent L3 sub-domains (§6.4.6+ if any) per N9 leaf-pattern with chapter-short-bracket parent `§6 [DOMAIN MODELS]` for L3 HEADING + L4 atoms parent canonical full-form '§6.4.X Domain Name (XX)' (NEVER self-parent per NEW6.b)
- Possible §6.5 chapter NEW transition in p.381-390 scope (TBD by TOC verify STEP 1) — if so, L2 sib=5 NEW + chapter-short-bracket parent `§6 [DOMAIN MODELS]`; child L3 atoms parent `§6.5 [SHORT-BRACKET CHAPTER NAME]`
- INTRA-AGENT consistency check (v1.4 N6 NEW round-7 dimension): ALL sub-batches MUST emit canonical chain form consistently from start
- 🔴 v1.5 N15 .xpt-parent FORBID — `parent_section` 值 MUST NOT match `^[a-z]+\.xpt$`. If §6.4.X Examples reference dataset filenames (sr.xpt / etc.), use canonical section ancestor NOT .xpt filename.
- 🔴 v1.5 N16 content-type-aware dispatch: 39a baseline subagent_type MUST be selected per content_type_hint (Examples-narrative + spec-table → executor MANDATORY; SENTENCE-paragraph + LIST_ITEM-heavy → free; mixed structural transition → executor PREFERRED). 39a baseline + drift cal alternation table determines 39b rerun and drift cal rerun subagent_type.
```

## §4 — Steps (sequential, no skip)

### STEP 1: TOC verify + cross-validate root tail / sister 38 state
- Read PDF p.4-5 TOC for §6.4.5 SR tail + §6.4.6+ if any + §6.5 chapter NEW if any in p.381-390 scope
- Cross-validate sister batch 38 ground truth via `_progress_batch_38.json` (when available) OR live root tail; assume 38 still running, use predicted state above
- **v1.5 N16 content-type cross-check**: classify p.381-385 vs p.386-390 by content type pre-dispatch

### STEP 2: Dispatch 39a (alternation per N14 STRONGLY VALIDATED + N16 content-type-aware)
- Pages: p.381-385 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_39a.jsonl`
- Inline-prepend cross-BATCH handoff state from §3
- `content_type_hint`: TBD by content type cross-check; recommend `oh-my-claudecode:executor` baseline (per v1.5 N16 — round 8 batch 36/37 demonstrated executor produces clean output for Examples-narrative + spec-table; alternation rerun goes to writer)
- Expected content: §6.4.5 SR L4 chain continuation (if not completed in 38) + SR L5 Examples N + any §6.4.6+ L3 sub-domain or §6.5 chapter NEW transition

### STEP 3: Dispatch 39b (alternation per N14: opposite of 39a)
- Pages: p.386-390 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_39b.jsonl`
- Inline-prepend prior sub-batch 39a 终态
- `content_type_hint`: TBD by 主 session post-39a actual content
- Expected content: continuation of 39a content + drift cal target page candidate (recommend dense Spec/Examples table)

### STEP 4: Pre-reviewer schema sweep (Option H if needed)
- 验 v1.5 Self-Validate hooks 1-17 (1-9 base + 10-14 v1.4 + 14.5 v1.5 N15 .xpt-parent FORBID + 15-17 v1.5 N17 cross-row + 16.5 v1.5 N16 dispatch assert)
- 关键 hooks: 9-enum / R10 strict / **N3 NEW8.d EMERGENCY-CRITICAL whole-row** (TABLE_ROW value-cell IDVAR ∈ parent domain Identifier set) / N5 TABLE_ROW pipe-count regex / N6 INTRA-AGENT consistency / N8 NEW9 L2 short-bracket parent FORBID / **v1.5 N15 .xpt-parent FORBID** / **v1.5 N17 cross-row pipe-count + USUBJID format + multi-axis spot-check N=3** PDF-cross-verify
- Density alarm check (N12 LIST_ITEM-heavy floor 8/sub-batch 80 if applicable + v1.5 N12.b boundary-region floor)
- Apply Option H + Rule B backup

### STEP 5: Rule A 10-atom audit via reviewer slot #50 `oh-my-claudecode:planner`
- AUDIT-mode pivot 31st cumulative (omc family 10th burn intra-family depth — D-MS-7 round 8 candidate "planner-strategist")
- Mode prompt: `"Mode: AUDIT for SDTM PDF atomization quality, NOT strategic planning consultant / NOT interview workflow / NOT Opus planning ideation / NOT planning before code execution"`
- Reflection bridge: 'strategic planning rigor ↔ atom verbatim PDF ground-truth rigor' / 'interview workflow precision ↔ atom_type 9-enum classification precision' / 'plan structure clarity ↔ atom hierarchy parent_section canonical-form clarity'
- Sample: 10 atoms stratified 1/page (p.381-390)
- Output: `evidence/checkpoints/rule_a_batch_39_sample.jsonl` + verdicts.jsonl + summary.md
- omc-family 10th burn = recipe intra-family depth burn at 10-agent scale post round 8 (omc family had 9 burns post round 8; this is 10th)

### STEP 6: 🔴 Drift cal MANDATORY (NEW1 9th time + N14 STRONGLY VALIDATED 3rd live-fire opportunity)
- Target page: TBD by 主 session — recommend dense Spec table OR Examples table (e.g. §6.4.5 SR Spec table p.376 OR FA Examples table page in p.381-390 scope)
- Baseline = 39a sub-batch baseline subagent_type (likely `oh-my-claudecode:executor` per N16)
- Rerun subagent_type per N14 STRONGLY VALIDATED alternation: opposite family member (executor → writer per table)
- Output: `evidence/checkpoints/drift_cal_batch_39_p<XXX>_report.md` + `drift_cal_p<XXX>_<rerun_type>_rerun.jsonl`
- Dual-threshold: strict count overlap ≥80% AND verbatim hash overlap ≥80% (per v1.3 §C NEW1 — STRONGLY VALIDATED 8× round 1-8)
- 任一<80% → FAIL + DIRECTION REVERSED 分析 + writer-family motif
- v1.4 N3 NEW8.d ACTIVE + v1.5 N16 writer-family ban ACTIVE — if 5th cumulative writer-direction main-line VALUE HALLUCINATION recurrence detected DESPITE N16 dispatch ban, ESCALATE per v1.5 N16 escalation clause (mandatory writer-family ban for ALL TABLE_ROW-heavy content type)
- v1.5 N17 cross-row pipe-count + USUBJID format + multi-axis spot-check pre-DONE hooks should catch any value-cell hallucination at writer pre-DONE stage (prevention layer in addition to N3 detection layer)

### STEP 7: Compose `_progress_batch_39.json` + `P1_batch_39_report.md` + DONE echo
- Single-line DONE: `PARALLEL_SESSION_39_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered drift_cal_strict=<X>% drift_cal_verbatim=<Y>% findings_added=<list O-P1-133..136 used>`

## §5 — Drift cal trigger schedule (本 batch MANDATORY)

- Batch 38 (sister B): SKIP
- **Batch 39 (本): MANDATORY** (every-3-batches batch 36→39 + cumulative ≥600 双触发; N14 STRONGLY VALIDATED alternation 3rd cumulative live-fire opportunity)
- Batch 40 (sister D): SKIP

## §6 — Halt conditions (per session — halt + write `halt_state_batch_39.md` + 4 resume options + wait user auth per G-MS-4 STRONGLY VALIDATED)

- writer failure rate >15%
- **drift cal both thresholds <80%** (per NEW1 strict spec — single threshold <80% NOT halt but FAIL with motif analysis)
- Rule A raw FAIL <70%
- ctx 用量超 80%
- 预分配 reviewer #50 omc:planner 不可派发 → halt_state per G-MS-4 STRONGLY VALIDATED (fallback candidates: omc-family-remaining e.g. test-engineer/qa-tester/security-reviewer; or claude-code-guide extension; or codex extension)
- 任何尝试写 shared file 的代码路径
- INTRA-AGENT inconsistency detected (v1.4 N6)
- N3 NEW8.d EMERGENCY-CRITICAL whole-row VALUE HALLUCINATION 5th cumulative recurrence detected → halt + 主 session emergency review + ESCALATE to v1.5 N16 escalation clause (writer-family ban for ALL TABLE_ROW-heavy content type)
- v1.5 N15 .xpt-parent violation detected (`^[a-z]+\.xpt$` parent_section pattern — pre-DONE hook 14.5 halt)
- v1.5 N16 dispatch violation detected (writer-family used for Examples-narrative + spec-table content type — pre-dispatch hook 16.5 halt)

## §7 — Final message format

```
PARALLEL_SESSION_39_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered drift_cal_strict=<X>% drift_cal_verbatim=<Y>% findings_added=<O-P1-133,...>
```

## §8 — Do NOT touch

```
.work/06_deep_verification/
  pdf_atoms.jsonl
  audit_matrix.md
  _progress.json
  subagent_prompts/*  (v1.5 active 不动)
  schema/*.json
  PLAN.md (v0.6)
  plans/*.md
  multi_session/sibling_continuity_sweep_report*.md
  multi_session/MULTI_SESSION_PROTOCOL.md
  multi_session/MULTI_SESSION_RETRO_*.md
  evidence/checkpoints/halt_state_batch_32.md (round 7 G-MS-4 1st LIVE-FIRE)
  evidence/checkpoints/halt_state_batch_36.md (round 8 G-MS-4 2nd LIVE-FIRE)
  evidence/checkpoints/v1_5_cut_reviewer_report.md
```

CLAUDE.md / MEMORY: **绝对不动**.
`pdf_atoms.jsonl.pre-multi-*-*.bak` + `pdf_atoms.jsonl.pre-v1.5-retroactive.bak` 历史 backup: **绝对不动**.

The boulder never stops. STEP 1 并行 6-file Read.
