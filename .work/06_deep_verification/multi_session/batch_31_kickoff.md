# Batch 31 Kickoff (Multi-Session Parallel — Session D, Round 6)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 8 STEPs (pre-flight / writer dispatch / schema sweep / drift cal SKIP / Rule A / findings / final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号 = STEP 8 echo 单行 `PARALLEL_SESSION_31_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-101,...>` + 3-5 句 user-facing summary.
>
> Halt-only fallback per G-MS-4: echo `HALT_BATCH_31 reason=<X>` + write `halt_state_batch_31.md`.
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel round 6 的 **session D (batch 31)**.
> Sister sessions = B (batch 29) + C (batch 30); 物理并行 3 终端各跑 1 batch + 1 reconciler 收尾.

═══════════════════════════════════════════════════════════════════
## §0 — Round 6 Finding ID Range Cross-Validation Table (G-MS-13 codified)
═══════════════════════════════════════════════════════════════════

**Round 6 reserved ranges** (post round 5 last used **O-P1-92** = reconciler-side NEW7 L6 cross-batch context drift 3rd recurrence):

| Session | Batch | Range | 本 batch 用 |
|---|---|---|---|
| B | 29 | O-P1-93..96 | ❌ sister, 不可越界 |
| C | 30 | O-P1-97..100 | ❌ sister, 不可越界 |
| D | 31 | **O-P1-101..104** | ✅ 本 session 唯一合法范围 |

**Self-validation gate** (STEP 7 强制): 任何 finding ID ≤100 OR ≥105 → STOP fix.

═══════════════════════════════════════════════════════════════════
## §1 — Scope + Pre-Dispatch TOC Verification
═══════════════════════════════════════════════════════════════════

**Page range**: ig34 p.301-310 (10 pages)

**Expected sections** (per round 5 retro carry-forward + batch 30 anticipated):
- Round 5 ended at §6.3.5.9.3 PP-PC Relating p.280; batch 29-30 (p.281-300) likely 跨 §6.3.5.10+ NEW sub-domain transitions + 概率 MEDIUM-HIGH §6.3.5 终结
- p.301-310: 续 batch 30 终态; 取决 §6.3.5 是否完结于 round 5/早 round 6 + §6.3.6 / §6.4 / §7 章节起页
- 任何 chapter / class / sub-domain transition 概率随 §6.3.5 完结而升 — 概率 HIGH 落 batch 31 scope (§6.3.5 完结后 R12 chapter-level transition discipline)

**MUST pre-dispatch verify**:
1. Read PDF `source/SDTMIG v3.4 (no header footer).pdf` p.4 TOC 锁 §6.3.5.X+ 末页 + §6.3.6+ / §6.4+ / §7+ 起页 + 任何 deeper sub-domain in p.301-310 scope
2. Read PDF p.300-310 preview 锁 任何 transition zone
3. 写 pre-dispatch TOC anchor block 加到 STEP 2 dispatch prompt

═══════════════════════════════════════════════════════════════════
## §2 — Cumulative R-Rules + NEW Codification Carry-Forward
═══════════════════════════════════════════════════════════════════

**v1.3 prompts active since 2026-04-27** — 13 codification items (A-M) all codified inline in `subagent_prompts/P0_writer_pdf_v1.3.md`. Each sub-batch dispatch prompt MUST inline-prepend the v1.3 prompt body. See `P0_writer_pdf_v1.3.md` §CODIFIED R-RULES + NEW for full details A-M.

**Round 5 carry-forward addendum** (per `MULTI_SESSION_RETRO_ROUND_5.md`):
- v1.4 candidate accumulation: 5 累 (O-P1-89 Write-overwrite Bash-heredoc HIGH + O-P1-91 NEW7 parent_section canonical full-form LOW + O-P1-85 NEW8.d TABLE_ROW value-cell verbatim integrity MEDIUM + O-P1-88 EDITORIAL_CORRECTION verdict path HIGH + O-P1-90 atom_id 4-digit padding regex hardening LOW); v1.4 cut decision pending round 6 reconciler.
- O-P1-80 round 5 NEW7 L4-group-container shared-Examples-L5-as-peer precedent (round 4 O-P1-75 RESTART branch extended).

### 🔴 NEW7 L6 Sub-Batch Handoff (PROCEDURAL ENFORCEMENT — ROUND 6 MANDATORY)

Round 5 verdict: INTRA-batch EFFECTIVE 1st live-fire (O-P1-81 PROACTIVE batch 26); CROSS-batch 3rd recurrence (O-P1-92 reconciler-side Option H) → round 6 cross-batch handoff codification mandatory.

主 session **必须** inline-prepend prior 31a 终态 to 31b dispatch prompt:
```
PRIOR SUB-BATCH 31a HEADING STATE (sub-batch 31b MUST continue, NOT restart):
- Last L4 sib used (under §6.3.5 OR §6.3.6+): <N>
- Last L5 sib used: <M>
- Last L6 Example sib used: <K>
- Convention: Example N+1 = HEADING hl=6 sib=K+1 (ALWAYS, NEVER SENTENCE)
- §6.3.5.X.Examples HEADING ALWAYS hl=5 sib=4
- 任何 NEW L4 HEADING parent = group container per NEW6.b L3-group-parent
```

═══════════════════════════════════════════════════════════════════
## §3 — STEP 0 Pre-Flight + R-Rules Pre-Dispatch
═══════════════════════════════════════════════════════════════════

### STEP 0.1 Read necessary files (并行 Read)
1. `multi_session/MULTI_SESSION_PROTOCOL.md`
2. `multi_session/MULTI_SESSION_RETRO_ROUND_5.md`
3. `subagent_prompts/P0_writer_pdf_v1.3.md` (v1.3 prompts active)
4. `evidence/checkpoints/_progress_batch_28.json` (round 5 batch 28 terminal R15 carry)

### STEP 0.2 Pre-dispatch verify
- root `pdf_atoms.jsonl` line count == **7092** (post round 5 baseline)
- `_progress_batch_28.json` status == "completed"
- PDF p.4 TOC re-verified for §6.3.5.X+ 末页 + §6.3.6+ / §6.4+ / §7+ 起页
- PDF p.300-310 preview verified
- Reviewer slot #40 **pr-review-toolkit:silent-failure-hunter** dispatchable (pr family second-agent depth burn — All tools incl. Write/Edit, full-tool no adaptation; 21st AUDIT pivot, validates intra-family agent variation post #38 pr-review-toolkit:code-reviewer first burn)

═══════════════════════════════════════════════════════════════════
## §4 — STEP 1-3 Writer Dispatch
═══════════════════════════════════════════════════════════════════

### Sub-batch split strategy
- 31a = oh-my-claudecode:writer × p.301-305 (5 pages)
- 31b = oh-my-claudecode:executor × p.306-310 (5 pages)
- **NEW7 L6 procedural handoff**: 31b prompt 必须 inline-prepend 31a 终态 (last L4/L5/L6 sib + Example N convention)

### Dispatch protocol
1. 主 session 并行 dispatch 2 Agent calls — 31a writer + 31b executor
2. Each agent prompt 完整 v1.3 R-rules + NEW1-NEW8 + handoff prepend (31b only)
3. Output: `evidence/checkpoints/pdf_atoms_batch_31<a|b>.jsonl`

═══════════════════════════════════════════════════════════════════
## §5 — STEP 4 Schema + Format Sweeps
═══════════════════════════════════════════════════════════════════

Python integrity sweep:
1. **0 JSON parse errors** + 9-enum + 4-digit atom_id + 0 frame tag + 0 within-batch dup + 0 root collision
2. **Density alarm** per-page (15 floor) + sub-batch (100 floor)
3. **NEW6.b L4 self-parent sweep** (任何 NEW L4 sub-domain transition in scope)
4. **NEW7 chain check**:
   - L5/L6 chain continuity from batch 30 terminal
   - L7 sub-example if visible
   - 任何 §6.3.5.X+ / §6.3.6+ / §6.4+ NEW sub-domain RESTART
5. **R12 transition page sweep** (任何 NEW transition visible, 含 chapter/class transition if §6.3.5 完结)
6. **R15 cross-batch sibling check** with batch 30 terminal: chain continuity per actual round 6 mid 状态
7. Any violation → Option H inline + Rule B backup

═══════════════════════════════════════════════════════════════════
## §6 — STEP 5 Drift Cal SKIP per Cadence
═══════════════════════════════════════════════════════════════════

- 不触发 (per cadence: batch 30 = mandatory; batch 31 next mandatory at batch 33)
- 写 `_progress_batch_31.json` drift_cal: triggered=false, next_mandatory="batch 33"

═══════════════════════════════════════════════════════════════════
## §7 — STEP 6 Rule A 10-Atom Audit (slot #40 pr-review-toolkit:silent-failure-hunter, AUDIT pivot 21st, pr family second agent depth burn)
═══════════════════════════════════════════════════════════════════

### Rule A sample build
- Sample size: 10 atoms (1/page p.301-310 stratified)
- Seed: 20260625 (round 6 deterministic)
- Stratification target: 4-5 TABLE_ROW + 2-3 HEADING (含 任何 NEW L4 transition + L5/L6) + 1-2 LIST_ITEM + 1 CODE_LITERAL
- Output: `evidence/checkpoints/rule_a_batch_31_sample.jsonl`

### Reviewer dispatch — slot #40 **pr-review-toolkit:silent-failure-hunter**
- AUDIT-mode pivot 21st (round 6 closing batch), **pr family second-agent depth burn** (batch 29 = pr-review-toolkit:code-reviewer / batch 30 = superpowers:code-reviewer / batch 31 = pr-review-toolkit:silent-failure-hunter — validates AUDIT recipe consistency across same-family different-agent within pr-review-toolkit, complementing cross-family validation)
- Tools: All tools (full-tool — Write/Edit available, no adaptation needed)
- **AUDIT-mode prepend** (强调禁止默认 mode):
  ```
  Mode: AUDIT for SDTM PDF atomization quality, NOT silent failure detection in catch blocks / NOT inadequate error handling review / NOT fallback behavior audit.
  Task: 10-atom Rule A reviewer for SDTM PDF atom verification against PDF p.301-310 ground truth.
  Adaptation: full-tool — write verdicts.jsonl + summary.md to evidence/checkpoints/ directly via Write tool.
  ```
- Final reviewer message: `Rule A batch 31 weighted=<X>% PASS_n=<P> PARTIAL_n=<PA> FAIL_n=<F>`

### Output files (reviewer writes directly via Write tool)
- `evidence/checkpoints/rule_a_batch_31_verdicts.jsonl`
- `evidence/checkpoints/rule_a_batch_31_summary.md`

═══════════════════════════════════════════════════════════════════
## §8 — STEP 7 Findings Documentation (G-MS-13 self-validation gate)
═══════════════════════════════════════════════════════════════════

### Allowed range
**O-P1-101..O-P1-104** (4 reserved).

═══════════════════════════════════════════════════════════════════
## §9 — STEP 8 Final Message + Files Written
═══════════════════════════════════════════════════════════════════

### Files written by session D
- `evidence/checkpoints/pdf_atoms_batch_31a.jsonl` + `pdf_atoms_batch_31b.jsonl`
- 任何 Rule B 备份 + Option E rerun
- `evidence/checkpoints/_progress_batch_31.json`
- `evidence/checkpoints/P1_batch_31_report.md`
- `evidence/checkpoints/rule_a_batch_31_sample.jsonl` + `_verdicts.jsonl` + `_summary.md`

### Files NOT touched
[同 batch_29_kickoff.md §9 NEVER DO 列表]

### Final echo (single line, mandatory)
```
PARALLEL_SESSION_31_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-101,...>
```

### Brief 3-5 sentence user-facing summary
含: §6.3.5.X+ / §6.3.6+ / §6.4+ scope + 任何 NEW transition (chapter-level if §6.3.5 完结) + NEW7 L6 sub-batch handoff (intra+cross) effectiveness + reviewer slot #40 **pr-review-toolkit:silent-failure-hunter** AUDIT pivot 21st pr family second-agent depth burn 验证 + carry-over to reconciler.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

[同 batch_29_kickoff.md NEVER DO 列表]

The boulder never stops. 第一步 STEP 0 并行 4-file Read + Pre-flight + PDF p.4 TOC verify + p.300-310 preview.
