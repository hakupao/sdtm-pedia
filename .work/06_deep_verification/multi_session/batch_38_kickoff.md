# Batch 38 Kickoff — Round 9 Multi-Session Parallel (Session B)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-7 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 7 单行 echo:
> ```
> PARALLEL_SESSION_38_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list>
> ```
> ═══════════════════════════════════════════════════════════════════

## §0 — Cross-validation Table (G-MS-13, kickoff prepend mandatory)

| Session | Batch | Page range | Finding ID 范围 | 本 batch 用 |
|---|---|---|---|---|
| **B (本)** | **38** | **p.371-380** | **O-P1-129..132** (4 reserved) | ✅ |
| C (sister) | 39 | p.381-390 | O-P1-133..136 (4 reserved) | (sister) |
| D (sister) | 40 | p.391-400 | O-P1-137..140 (4 reserved) | (sister) |
| E (reconciler) | n/a | n/a | O-P1-141+ (overflow) | (reconciler) |

**Self-validation gate** (STEP 7): any finding_id ∉ {129,130,131,132} → STOP fix.

## §0.5 — SKILL-vs-AGENT pre-allocation lint (v1.5 N15+ G-MS-NEW-8-1 codification)

**🔴 round 8 O-P1-121 recurring O-P1-110 motif lint mandatory** — pre-dispatch verify reviewer slot is registered AGENT, NOT SKILL:

| Slot | Type | Status |
|---|---|---|
| #49 (本 batch 38) | `Explore` (top-level capital E) | ✅ AGENT (not skill) |
| #50 (sister batch 39) | `oh-my-claudecode:planner` | ✅ AGENT (not skill) |
| #51 (sister batch 40) | `general-purpose` | ✅ AGENT (not skill, 3rd burn extension) |

If pre-allocated reviewer fails registry check at dispatch → halt + write `halt_state_batch_38.md` + 4 resume options A-D + wait user auth per G-MS-4 STRONGLY VALIDATED protocol.

## §1 — Background (Round 9 第 1 round post v1.5 cut + multi-session experiment 第 9 轮)

- 3 终端 (B/C/D) 同时跑 batches 38/39/40 — 物理并行 (round 9)
- 1 终端 (E) 启动 reconciler 收尾 (after B+C+D 全 PARALLEL_SESSION_NN_DONE)
- 各 session 写独立 batch files, **绝对不动** root `pdf_atoms.jsonl` (post round 8 baseline = 9224 atoms) / `audit_matrix.md` / `_progress.json`
- **v1.5 prompts ACTIVE** since 2026-04-28 (cut completed; Rule D reviewer #48 codex:codex-rescue codex-family INAUGURAL AUDIT verdict PASS 25/25 post 2 MEDIUM remediations)
- v1.5 absorbs 8 round 8 candidates V1-V8 via N15-N17 + STRONGLY VALIDATED status promotion (N14 + G-MS-4 post 2nd live-fire) + AGENT-vs-SKILL roster doc + Write-tool-less default codification
- Reviewer pool 已预分配 (Rule D 不撞 round 1-8 cumulative #1-#48, post round 8 + v1.5 cut family pool state: 4 EXHAUSTED [vercel + plugin-dev + feature-dev + pr-review-toolkit] + omc 9× + general-purpose 2× + superpowers 1× + Plan 1× INAUGURAL + claude-code-guide 1× INAUGURAL + codex 1× INAUGURAL):
  - batch 38 = #49 `Explore` (**top-level Explore agent INAUGURAL burn — 10th family pool inaugural**; recipe family-agnostic VALIDATED at 10th family pool; full-tool variant; **AUDIT pivot 30th cumulative** post v1.5 cut #48)
  - batch 39 = #50 `oh-my-claudecode:planner` (omc family 10th burn intra-family depth; drift cal carrier 9th time; full-tool variant; **AUDIT pivot 31st cumulative**)
  - batch 40 = #51 `general-purpose` (general-purpose family 3rd burn extension validated per round 8 D-MS-7; **AUDIT pivot 32nd cumulative**; full-tool variant)
- Round 9 protocol sustains round 7-8 spec: G-MS-4 halt fallback **STRONGLY VALIDATED post 2 live-fires** (round 7 batch 32 1st + round 8 batch 36 2nd) + G-MS-7 finding ID range pre-allocation + G-MS-13 cross-validation table at top of each kickoff + N14 strict alternation methodology procedural enforcement **STRONGLY VALIDATED post 2 live-fires** (drift cal in batch 39 only)
- 🔴 **v1.5 N15 .xpt-parent / table_caption FORBID rule ACTIVE** — 35-atom retroactive sweep applied at v1.5 cut (8 historical p.133 NEW9 + 27 batch 36 .xpt-parent); writer-side N15 hook prevents future occurrences. `parent_section` 值 MUST NOT match pattern `^[a-z]+\.xpt$`.
- 🔴 **v1.5 N16 writer-family ban for Examples-narrative + spec-table content type ACTIVE** — post 4 cumulative writer-direction main-line VALUE HALLUCINATION recurrences round 5+6+7+8. 主 session dispatch MUST cross-check `content_type_hint` pre-dispatch:
  - Examples-narrative + spec-table → **`oh-my-claudecode:executor` MANDATORY** (writer-family BANNED)
  - SENTENCE-paragraph + LIST_ITEM-heavy → free choice (writer or executor)
  - Mixed structural transition → executor PREFERRED
- 🔴 **v1.5 N17 post-extraction VALIDATION pass Self-Validate hooks 14→17** — per-batch pre-DONE validation cross-row pipe-count consistency + cross-row USUBJID format consistency + multi-axis value-cell spot-check N=3 random TABLE_ROWs PDF-cross-verify
- 主 session dispatch sub-batch 38b prompt MUST inline-prepend prior sub-batch 38a 终态. 主 session dispatch batch 38a prompt MUST inline-prepend prior batch 37b 终态 (per cross-BATCH handoff codification round 5 D-MS-2 + N6 v1.4 carry-forward).
- batch 38 NO drift cal (batch 39 mandatory per cadence batch 36→39)
- 每 kickoff 顶部 HARD-STOP DIRECTIVE — 唯一合法停止 = `PARALLEL_SESSION_38_DONE` 单行 echo OR `HALT_BATCH_38 reason=<X>` halt 信号

## §2 — Required Reads (并行 Read, ≤300 lines each)

1. `.work/06_deep_verification/_progress.json` (top-level + recovery_hint + v1_5_cut_completed)
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.5.md` (144 lines, MAIN writer base — note v1.5 N15-N17 + STRONGLY VALIDATED status + content-type-aware dispatch)
3. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.5.md` (131 lines, Rule D reviewer base — note Rule D roster 48 + fix matrix 25 items A-Y + AGENT-vs-SKILL roster doc §0)
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (master 219 lines)
5. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_8.md` (round 8 retro for context — pr-family 6/6 COMPLETED + Plan + claude-code-guide INAUGURAL + §6.4 chapter NEW + 4 EMERGENCY-CRITICAL hooks LIVE-FIRE EFFECTIVE + N14 + G-MS-4 STRONGLY VALIDATED)
6. `source/SDTMIG v3.4 (no header footer).pdf` p.4-5 TOC ground truth (verify §6.4.4 FA tail / §6.4.5 SR L3 sib=5 NEW p.375 / any subsequent §6.4.X or §6.5 transitions in p.371-380 scope)

**附读** (batch 37 terminal state for cross-BATCH handoff): `evidence/checkpoints/_progress_batch_37.json` + `P1_batch_37_report.md` — last L3/L4/L5 sib state under §6.4 chapter

## §3 — Pre-shared State + Cross-Batch Handoff (N6 v1.4 mandatory + v1.5 N15/N16 active)

```
PRIOR BATCH 37 HEADING STATE (batch 38 sub-batch a MUST continue, NOT restart):
- Last L2 chapter sib used: §6.4 [FINDINGS ABOUT EVENTS OR INTERVENTIONS] L2 sib=4 NEW (batch 37, p.361, first chapter NEW transition since §6.3 at p.180)
- Last L3 sib used (under §6.4 chapter): sib=4 (§6.4.4 Findings About Events or Interventions (FA) at p.364 leaf-pattern domain — completed in batch 37)
- §6.4.1 When to Use L3 sib=1 (batch 37, p.361 — completed)
- §6.4.2 Naming L3 sib=2 (batch 37, p.363 — completed)
- §6.4.3 Variables Unique L3 sib=3 (batch 37, p.364 — completed)
- §6.4.4 FA L4 chain Description=1 + Spec=2 + Assumptions=3 + Examples=4 (per N9 leaf-pattern, all completed in batch 37)
- §6.4.4 FA L5 Examples N atoms RESTART per §6.4.4 leaf-pattern Examples-at-L5 per N10 (Example 1 + Example 2 emitted in batch 37 per round 8 retro §1.3)
- Last L5 sib used (under §6.4.4 FA L4 Examples sib=4): sib=2 (Example 2 — TBD by sister 37 actual emission; may extend into batch 38)
- Last L6 sib used: NONE expected (FA L4-leaf — Examples at L5 per N10)
- Last L7 sib used: NONE expected
- Convention: §6.4.5 Skin Response (SR) L3 sib=5 NEW at p.375 — leaf-pattern (single-domain L3 like SC/SS/VS/FA; NOT group container); SR L4 chain Description=1/Spec=2/Assumptions=3/Examples=4 per N9 + L5 Examples-at-L5 per N10
- §6.4.X L3 children parent = '§6.4 [FINDINGS ABOUT EVENTS OR INTERVENTIONS]' chapter-short-bracket all-caps per round 6 NEW6 chapter-short-bracket extension + N11 v1.4 (1st live-fire EFFECTIVE round 8 batch 37)
- §6.4.X.Y L4 atoms (e.g. SR L4 Description/Spec) parent = '§6.4.5 Skin Response (SR)' canonical full-form (NEVER self-parent per NEW6.b)
- L5/L6 atoms parent = '§6.4.5 Skin Response (SR)' canonical full-form (NOT bare shortcut per O-P1-91/N7)
- INTRA-AGENT consistency check (v1.4 N6 NEW round-7 dimension): ALL sub-batches MUST emit canonical chain form consistently from start
- 🔴 v1.5 N15 .xpt-parent FORBID — `parent_section` 值 MUST NOT match `^[a-z]+\.xpt$`. If FA/SR Examples reference a dataset filename (fa.xpt / sr.xpt / etc.), use canonical section ancestor (e.g. '§6.4.4 FA – Examples' or '§6.4.5 SR – Examples') NOT the .xpt filename.
- 🔴 v1.5 N16 content-type-aware dispatch: p.371-375 likely §6.4.4 FA Examples-narrative continuation = Examples-narrative + spec-table → `oh-my-claudecode:executor` MANDATORY; p.375-380 §6.4.5 SR L3+L4 chain start = mixed structural transition → executor PREFERRED
```

## §4 — Steps (sequential, no skip)

### STEP 1: TOC verify + main session pre-dispatch state cross-validation
- Read PDF p.4-5 TOC for §6.4.5 SR + any subsequent §6.4.X or §6.5 chapter transitions in p.371-380 scope
- Cross-validate root `pdf_atoms.jsonl` tail (last 50 atoms ≈ p.367-370 batch 37b) with handoff state above per O-P1-93 round 6 procedural enforcement gap
- Confirm: §6.4.4 FA L4 chain + L5 Examples through Example 2 (or whatever batch 37 actually emitted) ✓
- **v1.5 N16 content-type cross-check**: classify p.371-375 vs p.376-380 by content type pre-dispatch (Examples-narrative + spec-table = executor MANDATORY / mixed structural transition = executor PREFERRED)

### STEP 2: Dispatch 38a (`oh-my-claudecode:executor` MANDATORY per v1.5 N16; baseline per N14 alternation)
- Pages: p.371-375 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_38a.jsonl`
- Inline-prepend cross-BATCH handoff state from §3 above
- `content_type_hint`: `examples_narrative_spec_table` (per N16 — FA Examples continuation expected)
- Expected content: §6.4.4 FA L5 Examples N continuation (Example 3+ if any) + §6.4.5 Skin Response (SR) L3 sib=5 NEW (p.375 leaf-pattern domain) + SR L4 chain Description=1/Spec=2 head
- Wait for DONE, capture atoms count

### STEP 3: Dispatch 38b (alternation per N14 STRONGLY VALIDATED: opposite of 38a; if 38a=executor → 38b=writer permissible IF content_type ≠ examples_narrative_spec_table else still executor)
- Pages: p.376-380 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_38b.jsonl`
- Inline-prepend prior sub-batch 38a 终态 (last L4/L5/L6/L7 sib + Examples convention + N6 ALL L6 sub-headings + INTRA-AGENT consistency check per v1.4 + v1.5 N17 pre-DONE hooks 15-17)
- `content_type_hint`: TBD by 主 session post-38a actual content; recommend `mixed_structural_transition` if §6.4.5 SR L4 chain continuation OR `examples_narrative_spec_table` if SR Examples table heavy
- Expected content: §6.4.5 SR L4 chain continuation (Spec / Assumptions / Examples) + SR L5 Examples N atoms per N10 + any subsequent §6.4.X or §6.5 chapter transition

### STEP 4: Pre-reviewer schema sweep (Option H if needed)
- 验 17 atom Self-Validate hooks per v1.5 (1-9 base + 10-14 v1.4 + 14.5 v1.5 N15 .xpt-parent FORBID + 15-17 v1.5 N17 cross-row consistency + 16.5 v1.5 N16 dispatch assert)
- 关键 hooks: 9-enum atom_type / R10 strict verbatim / **N3 NEW8.d EMERGENCY-CRITICAL whole-row** / N5 TABLE_ROW pipe-count regex / N6 INTRA-AGENT consistency / N8 NEW9 L2 short-bracket parent FORBID / **v1.5 N15 .xpt-parent FORBID** / **v1.5 N17 cross-row pipe-count + USUBJID format + multi-axis spot-check N=3**
- Density alarm check (v1.4 N12 LIST_ITEM-heavy floor 8 / sub-batch floor 80; v1.5 N12.b boundary-region floor 80 if 4+ structural transitions in 10-page span)
- INTRA-AGENT consistency check (v1.4 N6: ALL sub-batches MUST emit canonical chain form consistently)
- Apply Option H any defects + Rule B backup `pdf_atoms_batch_38[ab].jsonl.pre-OptionH-*.bak`

### STEP 5: Rule A 10-atom audit via reviewer slot #49 `Explore`
- **AUDIT-mode pivot 30th cumulative — Explore (top-level) family INAUGURAL burn (10th family pool inaugural)**; recipe family-agnostic VALIDATED at 10th family pool
- Mode prompt: `"Mode: AUDIT for SDTM PDF atomization quality, NOT codebase exploration / NOT file pattern search / NOT keyword grep across files / NOT 'how do API endpoints work' style discovery"`
- Reflection bridge: 'codebase exploration thoroughness ↔ atom verbatim PDF ground-truth thoroughness' / 'file pattern matching ↔ atom_type 9-enum classification' / 'keyword search precision ↔ verbatim text exact match precision'
- Sample: 10 atoms stratified 1/page (p.371-380)
- Output: `evidence/checkpoints/rule_a_batch_38_sample.jsonl` + `rule_a_batch_38_verdicts.jsonl` + `rule_a_batch_38_summary.md`
- Threshold: ≥80% raw weighted (PASS) / WARN band 70-90% / FAIL <70%
- Explore is full-tool agent (Bash, Read, Grep, Glob, etc. except Write); reviewer adaptation: if no Write tool, return verdicts.jsonl + summary.md content inline + main session writes files verbatim per v1.5 P0_reviewer §Step 4 Write-tool-less default codification

### STEP 6: Drift cal SKIP (next mandatory at batch 39 per cadence batch 36→39)

### STEP 7: Compose `_progress_batch_38.json` + `P1_batch_38_report.md` + DONE echo
- Single-line DONE: `PARALLEL_SESSION_38_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list O-P1-129..132 used>`

## §5 — Drift cal trigger schedule (本 batch SKIP)

- Batch 38 (本): SKIP (cumulative since batch 36 p.357 ≥600 atoms expected; per cadence next at batch 39)
- Batch 39 (sister C): MANDATORY (every-3-batches batch 36→39 + cumulative 双触发; per N14 STRONGLY VALIDATED alternation)
- Batch 40 (sister D): SKIP

## §6 — Halt conditions (per session — halt + write `halt_state_batch_38.md` + 4 resume options A-D + wait user auth per G-MS-4 STRONGLY VALIDATED protocol)

- writer failure rate >15%
- drift cal 2-way <80% (n/a 本 batch)
- Rule A raw FAIL <70%
- ctx 用量超 80%
- 预分配 reviewer 不可派发 (Rule D 撞风险 — write halt_state per G-MS-4 STRONGLY VALIDATED; fallback candidates: omc-family-remaining e.g. test-engineer/qa-tester/security-reviewer; or Plan extension; or claude-code-guide extension; or codex extension)
- 任何尝试写 shared file 的代码路径
- INTRA-AGENT inconsistency detected (v1.4 N6 NEW round-7 dimension — sub-batches divergent canonical chain form)
- v1.5 N15 .xpt-parent violation detected (`^[a-z]+\.xpt$` parent_section pattern — pre-DONE hook 14.5 halt)
- v1.5 N16 dispatch violation detected (writer-family used for Examples-narrative + spec-table content type — pre-dispatch hook 16.5 halt)

## §7 — Final message format (single-line echo)

```
PARALLEL_SESSION_38_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-129,...>
```

## §8 — Do NOT touch (shared files reserved for reconciler)

```
.work/06_deep_verification/
  pdf_atoms.jsonl                            ← root, reconciler 串行 merge
  audit_matrix.md                            ← reconciler 串行 append
  _progress.json                             ← reconciler 串行 update
  subagent_prompts/*                         ← v1.5 active 不动 (P0_writer_pdf/md/matcher/reviewer_v1.5.md)
  schema/*.json                              ← 不动
  PLAN.md                                    ← v0.6 不动
  plans/*.md                                 ← 不动
  multi_session/sibling_continuity_sweep_report*.md ← 历史
  multi_session/MULTI_SESSION_PROTOCOL.md    ← 历史
  multi_session/MULTI_SESSION_RETRO_*.md     ← 历史 (8 retros round 1-8)
  evidence/checkpoints/halt_state_batch_32.md ← G-MS-4 1st LIVE-FIRE 历史 evidence (round 7 D-MS-8)
  evidence/checkpoints/halt_state_batch_36.md ← G-MS-4 2nd LIVE-FIRE 历史 evidence (round 8 D-MS-8)
  evidence/checkpoints/v1_5_cut_reviewer_report.md ← v1.5 cut Rule D #48 codex:codex-rescue 历史
```

CLAUDE.md / MEMORY 类全项目文件: **绝对不动**.

`pdf_atoms.jsonl.pre-multi-*-*.bak` + `pdf_atoms.jsonl.pre-v1.5-retroactive.bak` 历史 backup: **绝对不动**.

The boulder never stops. STEP 1 并行 6-file Read.
