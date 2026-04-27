# Batch 36 Kickoff — Round 8 Multi-Session Parallel (Session C, **MANDATORY DRIFT CAL**)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-7 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 7 单行 echo:
> ```
> PARALLEL_SESSION_36_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered findings_added=<list>
> ```
> ═══════════════════════════════════════════════════════════════════

## §0 — Cross-validation Table (G-MS-13)

| Session | Batch | Page range | Finding ID 范围 | 本 batch 用 |
|---|---|---|---|---|
| B (sister) | 35 | p.341-350 | O-P1-117..120 (4 reserved) | (sister) |
| **C (本)** | **36** | **p.351-360** | **O-P1-121..124** (4 reserved) | ✅ |
| D (sister) | 37 | p.361-370 | O-P1-125..128 (4 reserved) | (sister) |
| E (reconciler) | n/a | n/a | O-P1-129+ (overflow) | (reconciler) |

**Self-validation gate** (STEP 7): any finding_id ∉ {121,122,123,124} → STOP fix.

## §1 — Background

- Round 8 第 8 轮 multi-session; v1.4 prompts ACTIVE since 2026-04-28
- Reviewer slot 已预分配: batch 36 = #46 `superpowers:verification-before-completion` (**superpowers family 2nd burn intra-family depth + drift cal carrier 8th time** — round 6 #39 superpowers:code-reviewer 1st burn precedent; AUDIT pivot 27th cumulative; full-tool variant)
- Round 8 protocol sustains round 7 spec: G-MS-4 halt fallback (round 7 1st LIVE-FIRE EFFECTIVE) + G-MS-7 finding ID range pre-allocation + G-MS-13 cross-validation table + N14 strict alternation methodology procedural enforcement (本 batch 必触 — drift cal mandatory)
- 🔴 **DRIFT CAL MANDATORY 本 batch (batch 36)** per cadence batch 33→36 (3-batch interval) + cumulative atoms post-p.325 ≥600 双触发, per v1.4 N14 strict alternation table:
  ```
  | Baseline subagent_type     | Rerun subagent_type        |
  | oh-my-claudecode:writer    | oh-my-claudecode:executor  |
  | oh-my-claudecode:executor  | oh-my-claudecode:writer    |
  ```
  Round 7 batch 33 NEW1 7th time CATASTROPHIC FAIL writer-direction VALUE HALLUCINATION 3rd cumulative recurrence main-line (O-P1-109 HIGH); v1.4 N3 NEW8.d EMERGENCY-CRITICAL whole-row check 现 ACTIVE; recommend dense Spec table OR Examples table page for drift cal target (TBD by 主 session post-35a baseline write)
- v1.4 N6 NEW7 L6 sub-batch handoff codification ACTIVE: extended to ALL L6 sub-headings + INTRA-AGENT consistency check
- 主 session dispatch batch 36a prompt MUST inline-prepend prior batch 35b 终态 (per cross-BATCH handoff codification + N6 v1.4)

## §2 — Required Reads (并行)

1. `.work/06_deep_verification/_progress.json` (recovery_hint + v1_4_cut)
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.4.md` (488 lines, v1.4 N1-N14 + Self-Validate 14 hooks)
3. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.4.md` (273 lines, Rule D 43 slots + 22-item matrix)
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (master 219 lines)
5. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_7.md` (round 7 retro — drift cal 7th time CATASTROPHIC FAIL writer-direction)
6. `source/SDTMIG v3.4 (no header footer).pdf` p.4-5 TOC (verify §6.3.12.2 TR L4 p.350 / §6.3.12.3 Tumor Identification/Tumor Results Examples L4 p.353 / §6.3.13 VS L3 p.358)

**附读**: `evidence/checkpoints/_progress_batch_34.json` (cross-batch handoff context)

## §3 — Pre-shared State + Cross-Batch Handoff (N6 v1.4 mandatory)

```
PRIOR BATCH 35 HEADING STATE (batch 36 sub-batch a MUST continue, NOT restart):
- Last L3 sib used (under §6.3 [MODELS FOR FINDINGS DOMAINS]): sib=12 (§6.3.12 Tumor/Lesion Domains group container at p.344)
- Last L4 sib used (under §6.3.12 group container): sib=2 (§6.3.12.2 Tumor/Lesion Results (TR) at p.350 — head only at sister batch 35 edge)
- Last L5 sib used (under §6.3.12.1 TU L4): sib=2 (TU-Specification, completed in batch 35; L5 chain Description=1/Spec=2/Assumptions=3/Examples=4 may extend into batch 36)
- Last L6 sib used (under §6.3.12.1 TU): TU Examples N (1..N RESTART per N7 — TBD by sister 35 actual emission)
- Last L7 sib used: NONE expected
- Convention: §6.3.12 group container per N7 L4 group-container branch — sub-domains §6.3.12.1 TU + §6.3.12.2 TR + §6.3.12.3 Examples L4 sib=1/2/3 RESTART; each sub-domain own L5 chain
- §6.3.12.X L4 atom parent = '§6.3.12 Tumor/Lesion Domains' canonical full-form (NEVER self-parent per NEW6.b)
- L5/L6 atoms parent = '§6.3.12.X Tumor/Lesion XXX (XX)' canonical full-form (per N7 L6/L7 canonical-form rule)
- §6.3.12.3 Tumor Identification/Tumor Results Examples L4 sib=3 NEW at p.353 — special "Examples" L4 sub-section under group container (analogous to round 5 §6.3.5.7.3 Examples L5 peer pattern shared between MB+MS, but here at L4 under TU+TR group)
- §6.3.13 Vital Signs (VS) L3 sib=13 NEW at p.358 — leaf-pattern (single-domain L3 like SC/SS; NOT group container)
- §6.3.13 VS L4 chain Description=1/Spec=2/Assumptions=3/Examples=4 per N9 leaf-pattern + N10 Examples-at-L5
- INTRA-AGENT consistency check (v1.4 N6 NEW round-7 dimension): ALL sub-batches MUST emit canonical chain form consistently from start
```

## §4 — Steps (sequential, no skip)

### STEP 1: TOC verify + cross-validate root tail
- Read PDF p.4 TOC for §6.3.12.X page boundaries (above)
- Cross-validate sister batch 35 ground truth via `_progress_batch_35.json` (when available) OR live root tail post 35 reconciler not yet — assume 35 still running, use predicted state above

### STEP 2: Dispatch 36a (alternation per N14 — choose subagent_type for baseline; recommend `oh-my-claudecode:executor` for consistency with round 7)
- Pages: p.351-355 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_36a.jsonl`
- Inline-prepend cross-BATCH handoff state from §3
- Expected content: §6.3.12.2 TR L4 chain (Description / Spec / Assumptions / Examples) + TR L6 Examples N RESTART per §6.3.12.2 + §6.3.12.3 Tumor Identification/Tumor Results Examples L4 sib=3 NEW (p.353) + Examples L5 atoms (Example N L5 sib=1..N RESTART under §6.3.12.3)

### STEP 3: Dispatch 36b (alternation: opposite of 36a)
- Pages: p.356-360 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_36b.jsonl`
- Inline-prepend prior sub-batch 36a 终态
- Expected content: §6.3.12.3 Examples continuation (Example N L7 children if applicable) + §6.3.13 Vital Signs (VS) L3 sib=13 NEW (p.358 leaf-pattern) + VS L4 chain Description / Spec head

### STEP 4: Pre-reviewer schema sweep (Option H if needed)
- 验 v1.4 Self-Validate hooks 1-14 (14 items per P0_writer_pdf_v1.4)
- 关键 hooks: 9-enum / R10 strict / **N3 NEW8.d EMERGENCY-CRITICAL whole-row** (TABLE_ROW value-cell IDVAR ∈ parent domain Identifier set) / N5 TABLE_ROW pipe-count regex / N6 INTRA-AGENT consistency / N8 NEW9 L2 short-bracket parent FORBID for non-L3-HEADING
- Density alarm check (N12 LIST_ITEM-heavy floor 8/sub-batch 80 if applicable)
- Apply Option H + Rule B backup

### STEP 5: Rule A 10-atom audit via reviewer slot #46 `superpowers:verification-before-completion`
- AUDIT-mode pivot 27th cumulative (superpowers family 2nd burn intra-family depth)
- Mode prompt: `"Mode: AUDIT for SDTM PDF atomization quality, NOT verification-before-completion advisory on code/test completion / NOT evidence collection workflow / NOT completion gate enforcement"`
- Reflection bridge: 'verification before completion ↔ Rule A pre-DONE audit' / 'evidence-based completion checks ↔ atom verbatim ground-truth verification' / 'test adequacy ↔ atom_type 9-enum coverage'
- Sample: 10 atoms stratified 1/page (p.351-360)
- Output: `evidence/checkpoints/rule_a_batch_36_sample.jsonl` + verdicts.jsonl + summary.md

### STEP 6: 🔴 Drift cal MANDATORY (NEW1 7th time + N14 strict alternation 2nd live-fire)
- Target page: TBD by 主 session — recommend dense Spec table OR Examples table (e.g. p.353 §6.3.12.3 Examples or p.359 VS Spec table)
- Baseline = 36a sub-batch baseline subagent_type (e.g. oh-my-claudecode:executor)
- Rerun subagent_type per N14 alternation: opposite family member (e.g. baseline executor → rerun writer per table)
- Output: `evidence/checkpoints/drift_cal_batch_36_p<XXX>_report.md` + `drift_cal_p<XXX>_<rerun_type>_rerun.jsonl`
- Dual-threshold: strict count overlap ≥80% AND verbatim hash overlap ≥80% (per v1.3 §C NEW1)
- 任一<80% → FAIL + DIRECTION REVERSED 分析 + writer-family motif
- v1.4 N3 NEW8.d expected to catch any whole-row VALUE HALLUCINATION recurrence (round 5 O-P1-85 + round 6 O-P1-103 + round 7 O-P1-109 = 3 cumulative writer-direction main-line)

### STEP 7: Compose `_progress_batch_36.json` + `P1_batch_36_report.md` + DONE echo
- Single-line DONE: `PARALLEL_SESSION_36_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered findings_added=<list O-P1-121..124 used>`

## §5 — Drift cal trigger schedule (本 batch MANDATORY)

- Batch 35 (sister B): SKIP
- **Batch 36 (本): MANDATORY** (every-3-batches batch 33→36 + cumulative ≥600 双触发; N14 strict alternation 2nd live-fire opportunity)
- Batch 37 (sister D): SKIP

## §6 — Halt conditions (per session — halt + write `halt_state_batch_36.md` + 4 resume options + wait user auth per G-MS-4)

- writer failure rate >15%
- **drift cal both thresholds <80%** (per NEW1 strict spec — single threshold <80% NOT halt but FAIL with motif analysis)
- Rule A raw FAIL <70%
- ctx 用量超 80%
- 预分配 reviewer #46 不可派发 → halt_state per G-MS-4 (round 7 1st LIVE-FIRE EFFECTIVE precedent — accept resume via halt_state file + user authorization fallback)
- 任何尝试写 shared file 的代码路径
- INTRA-AGENT inconsistency detected (v1.4 N6)
- N3 NEW8.d EMERGENCY-CRITICAL whole-row VALUE HALLUCINATION 4th cumulative recurrence detected → halt + 主 session emergency review

## §7 — Final message format

```
PARALLEL_SESSION_36_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered drift_cal_strict=<X>% drift_cal_verbatim=<Y>% findings_added=<O-P1-121,...>
```

## §8 — Do NOT touch

```
.work/06_deep_verification/
  pdf_atoms.jsonl
  audit_matrix.md
  _progress.json
  subagent_prompts/*  (v1.4 active 不动)
  schema/*.json
  PLAN.md (v0.6)
  plans/*.md
  multi_session/sibling_continuity_sweep_report*.md
  multi_session/MULTI_SESSION_PROTOCOL.md
  multi_session/MULTI_SESSION_RETRO_*.md
  evidence/checkpoints/halt_state_batch_32.md (round 7 G-MS-4 1st LIVE-FIRE 历史 evidence)
```

CLAUDE.md / MEMORY: **绝对不动**.
`pdf_atoms.jsonl.pre-multi-*-*.bak` 历史 backup: **绝对不动**.

The boulder never stops. STEP 1 并行 6-file Read.
