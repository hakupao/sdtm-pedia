# Batch 28 Kickoff (Multi-Session Parallel — Session D, Round 5)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 8 STEPs (pre-flight / writer dispatch / schema sweep / drift cal SKIP / Rule A / findings / final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号 = STEP 8 echo 单行 `PARALLEL_SESSION_28_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-88,...>` + 3-5 句 user-facing summary.
>
> Halt-only fallback per G-MS-4: echo `HALT_BATCH_28 reason=<X>` + write `halt_state_batch_28.md`.
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel round 5 的 **session D (batch 28)**.
> Sister sessions = B (batch 26) + C (batch 27); 物理并行 3 终端各跑 1 batch + 1 reconciler 收尾.

═══════════════════════════════════════════════════════════════════
## §0 — Round 5 Finding ID Range Cross-Validation Table (G-MS-13 codified)
═══════════════════════════════════════════════════════════════════

| Session | Batch | Range | 本 batch 用 |
|---|---|---|---|
| B | 26 | O-P1-80..83 | ❌ sister, 不可越界 |
| C | 27 | O-P1-84..87 | ❌ sister, 不可越界 |
| D | 28 | **O-P1-88..91** | ✅ 本 session 唯一合法范围 |

**Self-validation gate** (STEP 7 强制): 任何 finding ID ≤87 OR ≥92 → STOP fix.

═══════════════════════════════════════════════════════════════════
## §1 — Scope + Pre-Dispatch TOC Verification
═══════════════════════════════════════════════════════════════════

**Page range**: ig34 p.271-280 (10 pages)

**Expected sections** (per CLAUDE.md TOC carry-forward):
- p.271-280: §6.3.5.8 MI body 续 (Examples L6 + 可能 §6.3.5.9+ NEW sub-domain transition)
- 可能触 §6.3.5.9 PE / §6.3.5.10 PC / §6.3.5.X next sub-domain (TBD by sub-session pre-dispatch verify)

**MUST pre-dispatch verify**:
1. Read PDF `source/SDTMIG v3.4 (no header footer).pdf` p.4 TOC 锁 §6.3.5.9+ 实际起页 + §6.3.5.8 MI 末页
2. Read PDF p.270-280 preview 锁 任何 sub-domain transition zone
3. 写 pre-dispatch TOC anchor block 加到 STEP 2 dispatch prompt

═══════════════════════════════════════════════════════════════════
## §2 — Cumulative R-Rules + NEW Codification Carry-Forward
═══════════════════════════════════════════════════════════════════

[同 batch_26_kickoff.md §2 完整 R1-R15 + NEW1-NEW8 + NEW6/NEW6.b + NEW7 L6 procedural + density + G-MS-13]

### 🔴 NEW7 L6 Sub-Batch Handoff (PROCEDURAL ENFORCEMENT — ROUND 5 MANDATORY)

主 session **必须** inline-prepend prior 28a 终态 to 28b dispatch prompt:
```
PRIOR SUB-BATCH 28a HEADING STATE (sub-batch 28b MUST continue, NOT restart):
- Last L4 sib used (under §6.3.5): <N> (§6.3.5.8 MI sib=8 carried; §6.3.5.9+ if NEW)
- Last L5 sib used: <M> (e.g. §6.3.5.8.X if applicable)
- Last L6 Example sib used: <K>
- Convention: Example N+1 = HEADING hl=6 sib=K+1 (ALWAYS, NEVER SENTENCE)
- §6.3.5.X.Examples HEADING ALWAYS hl=5 sib=4
- §6.3.5.9+ L4 HEADING parent = `§6.3.5 Specimen-based Findings Domains` (NEW6.b L3-group-parent)
```

═══════════════════════════════════════════════════════════════════
## §3 — STEP 0 Pre-Flight + R-Rules Pre-Dispatch
═══════════════════════════════════════════════════════════════════

### STEP 0.1 Read necessary files (并行 Read)
1. `multi_session/MULTI_SESSION_PROTOCOL.md`
2. `multi_session/MULTI_SESSION_RETRO_ROUND_4.md`
3. `subagent_prompts/P0_writer_pdf_v1.2.md`
4. `evidence/checkpoints/_progress_batch_25.json` (round 4 batch 25 terminal R15 carry)

### STEP 0.2 Pre-dispatch verify
- root `pdf_atoms.jsonl` line count == 6146
- `_progress_batch_25.json` status == "completed"
- PDF p.4 TOC re-verified for §6.3.5.9+ sub-domain page ranges
- PDF p.270-280 preview verified
- Reviewer slot #37 general-purpose dispatchable (NEW family first burn — has all tools, full-power; AUDIT-mode pivot 18th)

═══════════════════════════════════════════════════════════════════
## §4 — STEP 1-3 Writer Dispatch
═══════════════════════════════════════════════════════════════════

### Sub-batch split strategy
- 28a = oh-my-claudecode:writer × p.271-275 (5 pages, MI body Examples 续)
- 28b = oh-my-claudecode:executor × p.276-280 (5 pages, MI body 末 + 可能 §6.3.5.9 NEW sub-domain transition)
- **NEW7 L6 procedural handoff**: 28b prompt 必须 inline-prepend 28a 终态 (last L4/L5/L6 sib + Example N convention)

### Dispatch protocol
1. 主 session 并行 dispatch 2 Agent calls — 28a writer + 28b executor
2. Each agent prompt 完整 R-rules + NEW1-NEW8 + handoff prepend (28b only)
3. Output: `evidence/checkpoints/pdf_atoms_batch_28<a|b>.jsonl`

═══════════════════════════════════════════════════════════════════
## §5 — STEP 4 Schema + Format Sweeps
═══════════════════════════════════════════════════════════════════

Python integrity sweep:
1. **0 JSON parse errors** + 9-enum + 4-digit atom_id + 0 frame tag + 0 within-batch dup + 0 root collision
2. **Density alarm** per-page (15 floor) + sub-batch (100 floor)
3. **NEW6.b L4 self-parent sweep** (任何 §6.3.5.X NEW L4 sub-domain transition in scope)
4. **NEW7 chain check**:
   - §6.3.5.8 MI L6 Examples chain RESTART under §6.3.5.8 MI (continuity from batch 27)
   - L7 sub-example (Example Na/Nb) if visible
   - §6.3.5.9+ L5 chain Description=1/Spec=2/Assump=3/Examples=4 RESTART under §6.3.5.9+ if NEW visible
5. **R12 transition page sweep** (if §6.3.5.9+ NEW transition visible)
6. **R15 cross-batch sibling check** with batch 27 terminal: §6.3.5.8 MI L6 sib=N → batch 28 sib=N+1 contiguous + L4 sib chain §6.3.5.8 sib=8 → §6.3.5.9+ sib=9+ if NEW
7. Any violation → Option H inline + Rule B backup

═══════════════════════════════════════════════════════════════════
## §6 — STEP 5 Drift Cal SKIP per Cadence
═══════════════════════════════════════════════════════════════════

- 不触发 (per cadence: batch 27 = mandatory; batch 28 next mandatory at batch 30)
- 写 `_progress_batch_28.json` drift_cal: triggered=false, next_mandatory="batch 30"

═══════════════════════════════════════════════════════════════════
## §7 — STEP 6 Rule A 10-Atom Audit (slot #37 general-purpose, AUDIT pivot 18th, **NEW family first burn**)
═══════════════════════════════════════════════════════════════════

### Rule A sample build
- Sample size: 10 atoms (1/page p.271-280 stratified)
- Seed: 20260610 (round 5 deterministic)
- Stratification target: 4-5 TABLE_ROW + 2-3 HEADING (含 MI L6 + 任何 §6.3.5.9+ L4 transition) + 1-2 LIST_ITEM + 1 CODE_LITERAL
- Output: `evidence/checkpoints/rule_a_batch_28_sample.jsonl`

### Reviewer dispatch — slot #37 general-purpose (NEW family first burn)
- AUDIT-mode pivot 18th
- **NEW family extension**: post round 4 vercel + plugin-dev + feature-dev all EXHAUSTED → general-purpose family inaugurated to validate AUDIT-mode pivot recipe family-agnostic
- Tools: All tools (含 Write — full-power, no adaptation needed; vs round 3-4 write-tool-less family)
- AUDIT-mode prepend:
  ```
  Mode: AUDIT for PDF atomization quality, NOT general-purpose research / NOT multi-step task execution / NOT codebase exploration.
  Task: 10-atom Rule A reviewer for SDTM PDF atom verification against PDF p.271-280 ground truth.
  Adaptation: full-tool — write verdicts.jsonl + summary.md to evidence/checkpoints/ directly.
  ```
- Final reviewer message: `Rule A batch 28 weighted=<X>% PASS_n=<P> PARTIAL_n=<PA> FAIL_n=<F>`

### Output files (reviewer writes directly via Write tool)
- `evidence/checkpoints/rule_a_batch_28_verdicts.jsonl`
- `evidence/checkpoints/rule_a_batch_28_summary.md`

═══════════════════════════════════════════════════════════════════
## §8 — STEP 7 Findings Documentation (G-MS-13 self-validation gate)
═══════════════════════════════════════════════════════════════════

### Allowed range
**O-P1-88, O-P1-89, O-P1-90, O-P1-91** (4 reserved).

═══════════════════════════════════════════════════════════════════
## §9 — STEP 8 Final Message + Files Written
═══════════════════════════════════════════════════════════════════

### Files written by session D
- `evidence/checkpoints/pdf_atoms_batch_28a.jsonl` + `pdf_atoms_batch_28b.jsonl`
- 任何 Rule B 备份 + Option E rerun
- `evidence/checkpoints/_progress_batch_28.json`
- `evidence/checkpoints/P1_batch_28_report.md`
- `evidence/checkpoints/rule_a_batch_28_sample.jsonl` + `_verdicts.jsonl` + `_summary.md`

### Files NOT touched
[同 batch_26_kickoff.md §9 NEVER DO 列表]

### Final echo (single line, mandatory)
```
PARALLEL_SESSION_28_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-88,...>
```

### Brief 3-5 sentence user-facing summary
含: §6.3.5.8 MI body + 任何 §6.3.5.9+ NEW transition + NEW7 L6 sub-batch handoff effectiveness + reviewer slot #37 general-purpose AUDIT pivot 18th NEW family first burn + carry-over to reconciler.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

[同 batch_26_kickoff.md NEVER DO 列表]

The boulder never stops. 第一步 STEP 0 并行 4-file Read + Pre-flight + PDF p.4 TOC verify + p.270-280 preview.
