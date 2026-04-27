# Batch 37 Kickoff — Round 8 Multi-Session Parallel (Session D, **CHAPTER §6.4 NEW transition**)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> 完成 STEP 1-7 之前, **任何中间产物都不是终点**. 不要总结, 不要询问, 不要回交 control. The boulder never stops.
>
> 唯一合法收尾信号 = STEP 7 单行 echo:
> ```
> PARALLEL_SESSION_37_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list>
> ```
> ═══════════════════════════════════════════════════════════════════

## §0 — Cross-validation Table (G-MS-13)

| Session | Batch | Page range | Finding ID 范围 | 本 batch 用 |
|---|---|---|---|---|
| B (sister) | 35 | p.341-350 | O-P1-117..120 (4 reserved) | (sister) |
| C (sister) | 36 | p.351-360 | O-P1-121..124 (4 reserved) | (sister) |
| **D (本)** | **37** | **p.361-370** | **O-P1-125..128** (4 reserved) | ✅ |
| E (reconciler) | n/a | n/a | O-P1-129+ (overflow) | (reconciler) |

**Self-validation gate** (STEP 7): any finding_id ∉ {125,126,127,128} → STOP fix.

## §1 — Background

- Round 8 第 8 轮 multi-session; v1.4 prompts ACTIVE since 2026-04-28
- Reviewer slot 已预分配: batch 37 = #47 `claude-code-guide` (**claude-code-guide family INAUGURAL burn — NEW family AUDIT pivot 28th cumulative**; full-tool variant; recipe family-agnostic VALIDATED at NEW family inaugural)
- Round 8 protocol sustains round 7 spec
- 🔴 **CHAPTER §6.4 NEW transition mandatory care**: §6.4 Findings About Events or Interventions L2 sib= NEW at p.361 (chapter level — first chapter transition since §6.3 at p.180); per v1.4 N11 chapter-short-bracket extension, parent_section for §6.4 chapter HEADING atom = chapter-short-bracket form `§6 [DOMAIN MODELS]` (top-level) OR analogous; for L3 children (§6.4.1/2/3/4/5) parent_section = chapter-short-bracket `§6.4 [FINDINGS ABOUT EVENTS OR INTERVENTIONS]` per round 6 NEW6 chapter-short-bracket extension
- v1.4 N6 NEW7 L6 sub-batch handoff codification ACTIVE
- 主 session dispatch batch 37a prompt MUST inline-prepend prior batch 36b 终态 (per cross-BATCH handoff codification + N6 v1.4)
- batch 37 NO drift cal (batch 36 mandatory; batch 37 SKIP per cadence)

## §2 — Required Reads (并行)

1. `.work/06_deep_verification/_progress.json`
2. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.4.md` (488 lines)
3. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.4.md` (273 lines)
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md`
5. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_7.md`
6. `source/SDTMIG v3.4 (no header footer).pdf` p.4-5 TOC (verify §6.4 chapter p.361 / §6.4.1 When to Use p.361 / §6.4.2 Naming p.363 / §6.4.3 Variables Unique p.364 / §6.4.4 Findings About Events or Interventions (FA) p.364 / §6.4.5 Skin Response (SR) p.375 — SR outside p.361-370 scope)

**附读**: `evidence/checkpoints/_progress_batch_34.json` (cross-batch handoff context fallback)

## §3 — Pre-shared State + Cross-Batch Handoff (N6 v1.4 mandatory)

```
PRIOR BATCH 36 HEADING STATE (batch 37 sub-batch a MUST continue, NOT restart):
- Last L3 sib used (under §6.3 [MODELS FOR FINDINGS DOMAINS]): sib=13 (§6.3.13 VS at p.358 — single-domain L3 leaf-pattern, completed in sister batch 36)
- Last L4 sib used (under §6.3.13 VS): sib=4 (Examples completed in sister batch 36 OR cross-batch into 37 — TBD by sister 36 actual emission)
- Last L5 sib used: VS leaf-pattern Examples-at-L5 sib=1..N RESTART per §6.3.13 VS (per N10 leaf-pattern Examples-at-L5)
- Last L6 sib used: NONE expected (VS L4-leaf — Examples at L5 not L6 per N10)
- Last L7 sib used: NONE expected
- Convention: §6.4 NEW chapter at p.361 — chapter-short-bracket parent `§6 [DOMAIN MODELS]` for chapter HEADING atom; L3 children of §6.4 parent='§6.4 [FINDINGS ABOUT EVENTS OR INTERVENTIONS]' chapter-short-bracket all-caps per round 6 NEW6 chapter-short-bracket extension + N11 v1.4
- §6.4.1 When to Use Findings About Events or Interventions L3 sib=1 NEW (p.361 — first child of §6.4 chapter)
- §6.4.2 Naming Findings About Domains L3 sib=2 NEW (p.363)
- §6.4.3 Variables Unique to Findings About L3 sib=3 NEW (p.364)
- §6.4.4 Findings About Events or Interventions (FA) L3 sib=4 NEW (p.364) — leaf-pattern domain (single-domain like SC/SS/VS)
- §6.4.4 FA L4 chain Description=1 / Spec=2 / Assumptions=3 / Examples=4 per N9 leaf-pattern
- §6.4.4 FA L5 Examples N atoms per N10 leaf-pattern Examples-at-L5
- §6.4.5 SR L3 sib=5 NEW at p.375 — outside p.361-370 batch 37 scope
- INTRA-AGENT consistency check (v1.4 N6 NEW round-7 dimension): ALL sub-batches MUST emit canonical chain form consistently
- 🔴 SPECIAL: §6.4.X children (When to Use / Naming / Variables Unique / FA) ALL share §6.4 chapter parent — first multi-L3 chapter chunk in P1 cumulative; N9 leaf-pattern check applies to FA + SR (not §6.4.1/2/3 which are introductory L3 sub-sections, NOT domains; their L3 atoms have parent §6.4 short-bracket but their child atoms (LIST_ITEM/SENTENCE) likely parent the L3 sub-section canonical full-form e.g. '§6.4.1 When to Use Findings About Events or Interventions')
```

## §4 — Steps (sequential, no skip)

### STEP 1: TOC verify + cross-validate root tail / sister state
- Read PDF p.4-5 TOC for §6.4 chapter + §6.4.1-5 page boundaries (above)
- Cross-validate sister batch 36 ground truth via `_progress_batch_36.json` (when available) OR live root tail; assume 36 still running, use predicted state above

### STEP 2: Dispatch 37a (recommend `oh-my-claudecode:executor`)
- Pages: p.361-365 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_37a.jsonl`
- Inline-prepend cross-BATCH handoff state from §3
- Expected content: §6.4 Findings About Events or Interventions L2 chapter HEADING NEW (p.361) + §6.4.1 When to Use L3 sib=1 NEW + §6.4.1 intro/LIST_ITEMs + §6.4.2 Naming L3 sib=2 NEW (p.363) + §6.4.2 intro/LIST_ITEMs + §6.4.3 Variables Unique L3 sib=3 NEW (p.364) + §6.4.3 intro + §6.4.4 FA L3 sib=4 NEW (p.364 leaf-pattern domain) + §6.4.4 FA L4 chain Description=1 / Spec=2 head

### STEP 3: Dispatch 37b (alternation: opposite of 37a)
- Pages: p.366-370 (~5 pages)
- Output: `evidence/checkpoints/pdf_atoms_batch_37b.jsonl`
- Inline-prepend prior sub-batch 37a 终态
- Expected content: §6.4.4 FA L4 chain continuation (Spec table tail / Assumptions=3 / Examples=4) + FA L5 Examples N RESTART per §6.4.4 leaf-pattern Examples-at-L5

### STEP 4: Pre-reviewer schema sweep (Option H if needed)
- 验 v1.4 Self-Validate hooks 1-14
- 特殊 chapter §6.4 transition: parent_section dual-form check (chapter-short-bracket for §6.4 HEADING + canonical full-form for §6.4.X L3 children + L4/L5 atoms)
- N11 chapter-short-bracket extension: §6.4 chapter HEADING parent_section likely `§6 [DOMAIN MODELS]` analogous to §6.3 chapter parenting; L3 children parent `§6.4 [FINDINGS ABOUT EVENTS OR INTERVENTIONS]` short-bracket all-caps
- N9 leaf-pattern check for §6.4.4 FA (single-domain L3 leaf, NOT group container — Description=L4 sib=1 / Spec=L4 sib=2 / Assumptions=L4 sib=3 / Examples=L4 sib=4 layout)
- N6 INTRA-AGENT consistency check across 37a/37b
- N8 NEW9 L2 short-bracket parent FORBID for non-L3-HEADING (CRITICAL given §6.4 chapter + §6.4.1/2/3 intro sub-sections — child LIST_ITEM/SENTENCE MUST parent the most specific containing L3 sub-section canonical full-form, NOT escalate to §6.4 chapter short-bracket)
- Apply Option H + Rule B backup

### STEP 5: Rule A 10-atom audit via reviewer slot #47 `claude-code-guide`
- **AUDIT-mode pivot 28th cumulative — claude-code-guide family INAUGURAL burn full-tool variant**
- Mode prompt: `"Mode: AUDIT for SDTM PDF atomization quality, NOT Claude Code CLI feature/hook/MCP/setting documentation guidance / NOT user-facing tutorial answers about Claude Code"`
- Reflection bridge: 'CLI feature documentation precision ↔ atom verbatim PDF ground-truth precision' / 'config/settings disambiguation ↔ atom_type 9-enum disambiguation' / 'troubleshooting workflow steps ↔ Rule A audit step protocol'
- Sample: 10 atoms stratified 1/page (p.361-370)
- Output: `evidence/checkpoints/rule_a_batch_37_sample.jsonl` + verdicts.jsonl + summary.md
- claude-code-guide family inaugural validation: recipe family-agnostic at 9th family pool post round 8 (vercel/plugin-dev/feature-dev EXHAUSTED + omc 9× + pr 6/6 COMPLETED post batch 35 #45 + general-purpose 2× + superpowers 3× post batches 36+37 + claude-code-guide INAUGURAL)

### STEP 6: Drift cal SKIP (batch 36 mandatory; batch 37 next mandatory at batch 39)

### STEP 7: Compose `_progress_batch_37.json` + `P1_batch_37_report.md` + DONE echo
- Single-line DONE: `PARALLEL_SESSION_37_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list O-P1-125..128 used>`

## §5 — Drift cal trigger schedule (本 batch SKIP)

- Batch 35 (sister B): SKIP
- Batch 36 (sister C): MANDATORY
- **Batch 37 (本)**: SKIP
- Next mandatory: batch 39 per cadence

## §6 — Halt conditions (per session — halt + write `halt_state_batch_37.md` + 4 resume options + wait user auth per G-MS-4)

- writer failure rate >15%
- Rule A raw FAIL <70%
- ctx 用量超 80%
- 预分配 reviewer #47 claude-code-guide 不可派发 → halt_state per G-MS-4 (NEW family inaugural burn — fallback candidates: superpowers-extension remaining / Plan / Explore / general-purpose-extension 3rd burn / omc-family-remaining)
- 任何尝试写 shared file 的代码路径
- INTRA-AGENT inconsistency detected (v1.4 N6)
- N8 NEW9 L2 short-bracket parent-skip violation in §6.4.X intro sub-section children (CRITICAL — first chapter-level child structure since §6.3 in P1 cumulative, motif risk)

## §7 — Final message format

```
PARALLEL_SESSION_37_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-125,...>
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
  evidence/checkpoints/halt_state_batch_32.md
```

CLAUDE.md / MEMORY: **绝对不动**.
`pdf_atoms.jsonl.pre-multi-*-*.bak` 历史 backup: **绝对不动**.

The boulder never stops. STEP 1 并行 6-file Read.
