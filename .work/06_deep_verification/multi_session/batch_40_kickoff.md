# Batch 40 Kickoff — Round 9 Multi-Session Parallel (Session D)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-7 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 7 单行 echo:
> ```
> PARALLEL_SESSION_40_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list>
> ```
> ═══════════════════════════════════════════════════════════════════

## §0 — Cross-validation Table (G-MS-13)

| Session | Batch | Page range | Finding ID 范围 | 本 batch 用 |
|---|---|---|---|---|
| B (sister) | 38 | p.371-380 | O-P1-129..132 (4 reserved) | (sister) |
| C (sister) | 39 | p.381-390 | O-P1-133..136 (4 reserved) | (sister) |
| **D (本)** | **40** | **p.391-400** | **O-P1-137..140** (4 reserved) | ✅ |
| E (reconciler) | n/a | n/a | O-P1-141+ (overflow) | (reconciler) |

**Self-validation gate** (STEP 7): any finding_id ∉ {137,138,139,140} → STOP fix.

## §0.5 — SKILL-vs-AGENT pre-allocation lint (v1.5 N15+ G-MS-NEW-8-1 codification)

**🔴 round 8 O-P1-121 recurring O-P1-110 motif lint mandatory** — pre-dispatch verify reviewer slot is registered AGENT, NOT SKILL:

| Slot | Type | Status |
|---|---|---|
| #49 (sister batch 38) | `Explore` (top-level capital E) | ✅ AGENT (not skill) |
| #50 (sister batch 39) | `oh-my-claudecode:planner` | ✅ AGENT (not skill, omc 10th burn) |
| #51 (本 batch 40) | `general-purpose` | ✅ AGENT (not skill, 3rd burn extension) |

If pre-allocated reviewer fails registry check at dispatch → halt + write `halt_state_batch_40.md` + 4 resume options A-D + wait user auth per G-MS-4 STRONGLY VALIDATED protocol.

## §1 — Background

- Round 9 第 9 轮 multi-session; v1.5 prompts ACTIVE since 2026-04-28
- Reviewer slot 已预分配: batch 40 = #51 `general-purpose` (**general-purpose family 3rd burn extension validated per round 8 D-MS-7 candidate "general-purpose-extension"**; AUDIT pivot 32nd cumulative; full-tool variant — recipe family-agnostic VALIDATED at 3-burn intra-family depth scale)
- Round 9 protocol sustains round 7-8 spec: G-MS-4 halt fallback **STRONGLY VALIDATED** + G-MS-7 finding ID range pre-allocation + G-MS-13 cross-validation table + N14 strict alternation methodology procedural enforcement **STRONGLY VALIDATED**
- v1.5 prompts ACTIVE: N15 .xpt-parent FORBID + N16 writer-family ban for Examples-narrative + spec-table + N17 post-extraction VALIDATION pass Self-Validate hooks 14→17
- v1.4 N6 NEW7 L6 sub-batch handoff codification ACTIVE: extended to ALL L6 sub-headings + INTRA-AGENT consistency check
- 主 session dispatch batch 40a prompt MUST inline-prepend prior batch 39b 终态 (per cross-BATCH handoff codification + N6 v1.4)
- batch 40 NO drift cal (batch 39 mandatory; batch 40 SKIP per cadence; next mandatory at batch 42)
- general-purpose 3rd burn precedent: round 5 #28 1st burn (single-agent inaugural) + round 7 #41 2nd burn (G-MS-4 fallback) + round 9 #51 3rd burn (extension validation) — round 8 retro D-MS-7 candidate validated

## §2 — Required Reads (并行)

1. `.work/06_deep_verification/_progress.json`
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.5.md` (144 lines)
3. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.5.md` (131 lines)
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md`
5. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_8.md`
6. `source/SDTMIG v3.4 (no header footer).pdf` p.4-5 TOC (verify §6.4 chapter end + any §6.5 chapter NEW transition + §6.5.X L3 sub-section transitions in p.391-400 scope; or alternative §6.4.X continuation)

**附读**: `evidence/checkpoints/_progress_batch_38.json` + `_progress_batch_39.json` (cross-batch handoff context fallback when sister batches DONE)

## §3 — Pre-shared State + Cross-Batch Handoff (N6 v1.4 mandatory + v1.5 N15/N16/N17 active)

```
PRIOR BATCH 39 HEADING STATE (batch 40 sub-batch a MUST continue, NOT restart):
- Last L2 chapter sib used: TBD by sister 39 actual emission — likely §6.4 [FINDINGS ABOUT EVENTS OR INTERVENTIONS] L2 sib=4 still active OR §6.5 chapter NEW transition L2 sib=5 if §6.5 entered in p.381-390 scope
- Last L3 sib used: TBD by sister 39 — possible terminal §6.4.X (X=5 SR + any §6.4.6+) OR §6.5.X children if §6.5 entered
- L4/L5/L6/L7 sib state: TBD by sister 39 actual emission (predicted §6.4.X leaf-pattern Description=L4 sib=1/Spec=2/Assumptions=3/Examples=4 + L5 Examples N)
- Convention: §6.4.X L3 children parent='§6.4 [FINDINGS ABOUT EVENTS OR INTERVENTIONS]' chapter-short-bracket all-caps per round 6 NEW6 chapter-short-bracket extension + N11 v1.4 (1st live-fire EFFECTIVE round 8 batch 37)
- Convention: if §6.5 chapter NEW transition in p.391-400 scope, §6.5 L2 chapter HEADING parent='§6 [DOMAIN MODELS]' top-level chapter; §6.5.X L3 children parent='§6.5 [SHORT-BRACKET CHAPTER NAME]' chapter-short-bracket all-caps per N11
- L4 atoms (e.g. §6.5.X.Y SR L4 Description/Spec) parent = '§6.5.X Domain Name (XX)' canonical full-form (NEVER self-parent per NEW6.b)
- L5/L6 atoms parent = '§6.5.X Domain Name (XX)' canonical full-form (NOT bare shortcut per O-P1-91/N7)
- INTRA-AGENT consistency check (v1.4 N6 NEW round-7 dimension): ALL sub-batches MUST emit canonical chain form consistently from start
- 🔴 v1.5 N15 .xpt-parent FORBID — `parent_section` 值 MUST NOT match `^[a-z]+\.xpt$`. If §6.5.X Examples reference dataset filenames (xx.xpt), use canonical section ancestor NOT .xpt filename.
- 🔴 v1.5 N16 content-type-aware dispatch: 40a baseline subagent_type per content_type_hint (Examples-narrative + spec-table → executor MANDATORY; SENTENCE-paragraph + LIST_ITEM-heavy → free; mixed structural transition → executor PREFERRED).
- 🔴 If §6.5 chapter NEW transition in p.391-400 scope = mixed structural transition content type → executor PREFERRED (analogous to round 8 batch 37 §6.4 chapter NEW EFFECTIVE 100% PASS first-attempt with 0-amplification baseline)
```

## §4 — Steps (sequential, no skip)

### STEP 1: TOC verify + cross-validate root tail / sister state
- Read PDF p.4-5 TOC for §6.4 chapter end + any §6.5 chapter NEW transition + §6.5.X L3 sub-section transitions in p.391-400 scope
- Cross-validate sister batch 39 ground truth via `_progress_batch_39.json` (when available) OR live root tail; assume 39 still running, use predicted state above
- **v1.5 N16 content-type cross-check**: classify p.391-395 vs p.396-400 by content type pre-dispatch (recommend executor PREFERRED if chapter NEW transition expected)

### STEP 2: Dispatch 40a (recommend `oh-my-claudecode:executor` per v1.5 N16 if mixed structural transition expected)
- Pages: p.391-395 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_40a.jsonl`
- Inline-prepend cross-BATCH handoff state from §3
- `content_type_hint`: TBD by content type cross-check; recommend `mixed_structural_transition` if §6.5 chapter NEW expected OR `examples_narrative_spec_table` if FA/SR Examples table heavy
- Expected content: §6.4 chapter tail (any §6.4.X continuation from sister 39) + possible §6.5 chapter NEW L2 sib=5 transition + §6.5.X L3 children intro

### STEP 3: Dispatch 40b (alternation per N14 STRONGLY VALIDATED: opposite of 40a)
- Pages: p.396-400 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_40b.jsonl`
- Inline-prepend prior sub-batch 40a 终态
- `content_type_hint`: TBD by 主 session post-40a actual content
- Expected content: continuation of §6.5.X L3 children + L4 chain start for first §6.5.X.Y domain (Description=1/Spec=2 head)

### STEP 4: Pre-reviewer schema sweep (Option H if needed)
- 验 v1.5 Self-Validate hooks 1-17
- 关键 hooks: 9-enum atom_type / R10 strict verbatim / **N3 NEW8.d EMERGENCY-CRITICAL whole-row** / N5 TABLE_ROW pipe-count regex / N6 INTRA-AGENT consistency / N8 NEW9 L2 short-bracket parent FORBID / **v1.5 N15 .xpt-parent FORBID** / **v1.5 N17 cross-row pipe-count + USUBJID format + multi-axis spot-check N=3**
- 特殊 chapter §6.5 transition (if applicable): parent_section dual-form check (chapter-short-bracket for §6.5 HEADING + canonical full-form for §6.5.X L3 children)
- N11 chapter-short-bracket extension validation 2nd live-fire opportunity (round 8 batch 37 §6.4 1st live-fire EFFECTIVE)
- N9 leaf-pattern check for any §6.5.X single-domain L3 leaf (Description=L4 sib=1 / Spec=L4 sib=2 / Assumptions=L4 sib=3 / Examples=L4 sib=4 layout)
- N6 INTRA-AGENT consistency check across 40a/40b
- Density alarm check (N12 LIST_ITEM-heavy floor 8/sub-batch 80 if applicable + v1.5 N12.b boundary-region floor 80 if 4+ structural transitions)
- Apply Option H + Rule B backup `pdf_atoms_batch_40[ab].jsonl.pre-OptionH-*.bak`

### STEP 5: Rule A 10-atom audit via reviewer slot #51 `general-purpose`
- **AUDIT-mode pivot 32nd cumulative — general-purpose family 3rd burn extension validated** (round 5 #28 1st single-agent inaugural + round 7 #41 2nd burn G-MS-4 fallback + round 9 #51 3rd burn extension)
- Mode prompt: `"Mode: AUDIT for SDTM PDF atomization quality, NOT general-purpose research / NOT multi-step task execution / NOT keyword/file search across codebase / NOT complex question research"`
- Reflection bridge: 'general-purpose research thoroughness ↔ atom verbatim PDF ground-truth thoroughness' / 'multi-step task execution rigor ↔ atom_type 9-enum classification rigor' / 'keyword search precision ↔ verbatim text exact match precision'
- Sample: 10 atoms stratified 1/page (p.391-400)
- Output: `evidence/checkpoints/rule_a_batch_40_sample.jsonl` + verdicts.jsonl + summary.md
- general-purpose family 3rd burn validation: recipe family-agnostic at 3-burn intra-family depth scale post round 9 (joins pr-review-toolkit 6/6 + omc 10× as multi-burn family)

### STEP 6: Drift cal SKIP (batch 39 mandatory; batch 40 next mandatory at batch 42)

### STEP 7: Compose `_progress_batch_40.json` + `P1_batch_40_report.md` + DONE echo
- Single-line DONE: `PARALLEL_SESSION_40_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list O-P1-137..140 used>`

## §5 — Drift cal trigger schedule (本 batch SKIP)

- Batch 38 (sister B): SKIP
- Batch 39 (sister C): MANDATORY
- **Batch 40 (本)**: SKIP
- Next mandatory: batch 42 per cadence

## §6 — Halt conditions (per session — halt + write `halt_state_batch_40.md` + 4 resume options + wait user auth per G-MS-4 STRONGLY VALIDATED)

- writer failure rate >15%
- Rule A raw FAIL <70%
- ctx 用量超 80%
- 预分配 reviewer #51 general-purpose 不可派发 → halt_state per G-MS-4 STRONGLY VALIDATED (fallback candidates: omc-family-remaining e.g. test-engineer/qa-tester/security-reviewer; or claude-code-guide extension; or codex extension; or Plan extension)
- 任何尝试写 shared file 的代码路径
- INTRA-AGENT inconsistency detected (v1.4 N6)
- N8 NEW9 L2 short-bracket parent-skip violation in §6.5.X intro sub-section children if applicable (CRITICAL — 2nd potential chapter-level child structure since §6.4 in P1 cumulative)
- v1.5 N15 .xpt-parent violation detected (`^[a-z]+\.xpt$` parent_section pattern — pre-DONE hook 14.5 halt)
- v1.5 N16 dispatch violation detected (writer-family used for Examples-narrative + spec-table content type — pre-dispatch hook 16.5 halt)

## §7 — Final message format

```
PARALLEL_SESSION_40_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-137,...>
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
  evidence/checkpoints/halt_state_batch_32.md
  evidence/checkpoints/halt_state_batch_36.md
  evidence/checkpoints/v1_5_cut_reviewer_report.md
```

CLAUDE.md / MEMORY: **绝对不动**.
`pdf_atoms.jsonl.pre-multi-*-*.bak` + `pdf_atoms.jsonl.pre-v1.5-retroactive.bak` 历史 backup: **绝对不动**.

The boulder never stops. STEP 1 并行 6-file Read.
