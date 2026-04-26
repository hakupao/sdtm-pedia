# Batch 27 Kickoff (Multi-Session Parallel — Session C, Round 5)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 9 STEPs (pre-flight / writer dispatch / schema sweep / DRIFT CAL MANDATORY / Rule A / findings / final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号 = STEP 9 echo 单行 `PARALLEL_SESSION_27_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered findings_added=<O-P1-84,...>` + 3-5 句 user-facing summary.
>
> Halt-only fallback per G-MS-4 (4 rounds spec-only no live-fire): echo `HALT_BATCH_27 reason=<X>` + write `halt_state_batch_27.md`.
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel round 5 的 **session C (batch 27)**.
> Sister sessions = B (batch 26) + D (batch 28); 物理并行 3 终端各跑 1 batch + 1 reconciler 收尾.
> **Drift cal MANDATORY 本 batch** (cadence batch 24→27 + cumulative atoms post-p.233 ≥600 双触发).

═══════════════════════════════════════════════════════════════════
## §0 — Round 5 Finding ID Range Cross-Validation Table (G-MS-13 codified)
═══════════════════════════════════════════════════════════════════

| Session | Batch | Range | 本 batch 用 |
|---|---|---|---|
| B | 26 | O-P1-80..83 | ❌ sister, 不可越界 |
| C | 27 | **O-P1-84..87** | ✅ 本 session 唯一合法范围 |
| D | 28 | O-P1-88..91 | ❌ sister, 不可越界 |

**Self-validation gate** (STEP 8 强制): 任何 finding ID ≤83 OR ≥88 → STOP fix.

═══════════════════════════════════════════════════════════════════
## §1 — Scope + Pre-Dispatch TOC Verification
═══════════════════════════════════════════════════════════════════

**Page range**: ig34 p.261-270 (10 pages)

**Expected sections** (per CLAUDE.md TOC carry-forward):
- p.261-262: §6.3.5.7 Microbiology body 末 (likely §6.3.5.7.X sub-domain Examples tail)
- **p.263**: 🔴 §6.3.5.8 MI Microscopic Findings NEW L4 sub-domain transition (R12 + NEW6.b L3-group-parent first-attempt critical)
- p.264-270: §6.3.5.8 MI body (Description / Specification table / Assumptions / Examples)

**MUST pre-dispatch verify**:
1. Read PDF `source/SDTMIG v3.4 (no header footer).pdf` p.4 (TOC) 锁 §6.3.5.8 MI 实际起页 ± §6.3.5.7 Microbiology 末页 ± §6.3.5.9+ 任何 sub-domain in p.261-270 scope
2. Read PDF p.260-270 preview 锁 transition zone (R12 3-zone partition target)
3. 写 pre-dispatch TOC anchor block 加到 STEP 2 dispatch prompt

═══════════════════════════════════════════════════════════════════
## §2 — Cumulative R-Rules + NEW Codification Carry-Forward
═══════════════════════════════════════════════════════════════════

[同 batch_26_kickoff.md §2 完整 R1-R15 + NEW1-NEW8 + NEW6/NEW6.b + NEW7 L6 procedural + density alarm + G-MS-13 — 此处不 inline 重复, 主 session dispatch sub-agent 时 inline-prepend 完整 block]

### 🔴 NEW7 L6 Sub-Batch Handoff (PROCEDURAL ENFORCEMENT — ROUND 5 MANDATORY)

Round 3 batch 23 + round 4 batch 25 = 2× 复发. Round 5 batch 27 高风险 (R12 §6.3.5.7→§6.3.5.8 MI L4 transition + 27a/27b sub-batch boundary 可能跨 transition page).

主 session **必须** prepend prior sub-batch state when dispatching 27b:
```
PRIOR SUB-BATCH 27a HEADING STATE (sub-batch 27b MUST continue, NOT restart):
- Last L4 sib used (under §6.3.5): <N> (e.g. §6.3.5.7 sib=7; §6.3.5.8 MI sib=8 if NEW transition in 27a scope)
- Last L5 sib used: <M> (e.g. §6.3.5.8.X if visible)
- Last L6 Example sib used: <K>
- Convention: Example N+1 = HEADING hl=6 sib=K+1 (ALWAYS, NEVER SENTENCE)
- §6.3.5.X.Examples HEADING ALWAYS hl=5 sib=4
- §6.3.5.8 MI L4 HEADING parent = `§6.3.5 Specimen-based Findings Domains` (NEW6.b L3-group-parent, NEVER self-parent)
```

═══════════════════════════════════════════════════════════════════
## §3 — STEP 0 Pre-Flight + R-Rules Pre-Dispatch
═══════════════════════════════════════════════════════════════════

### STEP 0.1 Read necessary files (并行 Read)
1. `multi_session/MULTI_SESSION_PROTOCOL.md` (master)
2. `multi_session/MULTI_SESSION_RETRO_ROUND_4.md` (round 4 retro — read §1.6 NEW1 4× validated for drift cal protocol)
3. `subagent_prompts/P0_writer_pdf_v1.2.md` (writer/executor R-rule block)
4. `evidence/checkpoints/_progress_batch_25.json` (round 4 batch 25 terminal state)
5. `evidence/checkpoints/drift_cal_batch_24_p233_report.md` (last drift cal protocol reference)

### STEP 0.2 Pre-dispatch verify
- root `pdf_atoms.jsonl` line count == 6146
- `_progress_batch_25.json` status == "completed"
- PDF p.4 TOC re-verified for §6.3.5.8 MI 起页 + 任何 §6.3.5.7.X sub-domain 末页
- PDF p.260-270 preview verified
- Reviewer slot #36 oh-my-claudecode:architect dispatchable (Tools: All except Write/Edit, READ-ONLY = no Bash either; write-tool-less + no-Bash inline content adaptation per round 3 #29 sub-pattern)

═══════════════════════════════════════════════════════════════════
## §4 — STEP 1-3 Writer Dispatch
═══════════════════════════════════════════════════════════════════

### Sub-batch split strategy
- 27a = oh-my-claudecode:writer × p.261-265 (5 pages, 含 §6.3.5.7 末 + p.263 §6.3.5.8 MI L4 transition + MI head)
- 27b = oh-my-claudecode:executor × p.266-270 (5 pages, MI body Spec + Assumptions/Examples)
- **NEW7 L6 procedural handoff**: 27b prompt 必须 inline-prepend 27a 终态 (last L4/L5/L6 sib + Example N convention)

### Dispatch protocol
1. 主 session 并行 dispatch 2 Agent calls — 27a writer + 27b executor (single message, 2 tool uses)
2. Each agent prompt 必须 inline-prepend 完整 R-rules + NEW1-NEW8 + sub-batch handoff prepend (27b only)
3. Output: `evidence/checkpoints/pdf_atoms_batch_27<a|b>.jsonl`
4. Final DONE single-line per agent

═══════════════════════════════════════════════════════════════════
## §5 — STEP 4 Schema + Format Sweeps + R12 Transition + NEW6.b
═══════════════════════════════════════════════════════════════════

Python integrity sweep:
1. **0 JSON parse errors** + 9-enum + 4-digit atom_id + 0 frame tag + 0 within-batch dup + 0 root collision
2. **Density alarm** per-page (15 floor) + sub-batch (100 floor)
3. **NEW6.b L4 self-parent sweep**: §6.3.5.8 MI L4 HEADING (likely p.263 a0XX) parent_section MUST = `§6.3.5 Specimen-based Findings Domains` (NOT self-parent); 4× round 4 EFFECTIVE proactive precedent → expect 0 violation if procedural enforcement holds
4. **NEW7 chain check**:
   - §6.3.5.7 末 chain (Microbiology Domains group container internal) — 验 last sub-domain L5/L6 chain
   - §6.3.5.8 MI L5 chain RESTART: Description=1 / Specification=2 / Assumptions=3 / Examples=4 RESTART under §6.3.5.8 MI
   - L6 Examples N RESTART under §6.3.5.8 MI
5. **R12 transition page sweep** at p.263 (§6.3.5.7 → §6.3.5.8 MI):
   - ≥8 atoms required + 3-zone partition (Microbiology tail / MI L4 HEADING / MI L5 Description HEADING + intro)
   - 27a 单批 sub-batch 写 transition → handoff state critical for 27b
6. **R15 cross-batch sibling check**:
   - With batch 26 terminal: §6.3.5.7 Microbiology末 → batch 27 §6.3.5.8 MI L4 sib=8 RESTART contiguous
7. Any violation → Option H inline + Rule B backup

═══════════════════════════════════════════════════════════════════
## §6 — STEP 5 🔴 DRIFT CAL MANDATORY (NEW1 dual-threshold, 5th time round 5)
═══════════════════════════════════════════════════════════════════

### Trigger basis
- Cadence: every-3-batches batch 24 → 27
- Cumulative atoms post-p.233: batch 25 (210) + batch 26 (~250 est) + batch 27 (~250 est) ≥600 ✅ 双触发

### Target page selection
推荐 dense page in 27a scope (TBD by session C upon p.261-270 preview):
- Top candidate: p.265 IF MI Description/Specification table dense (mixed HEADING + TABLE_HEADER + TABLE_ROW)
- Alternative: p.263 transition page (R12 + L4 HEADING + L5 HEADING — tests heading_fields drift)
- Alternative: dense Examples page in 27b scope if MI Examples 1+ visible

### Method (NEW1 dual-threshold, round 5 5th time)
1. Baseline = 27a/27b 主写手 atom set on target page
2. Rerun = alternation agent (if baseline = writer → rerun = executor; if baseline = executor → rerun = writer)
3. Compare:
   - **Strict count overlap** (atom_id count match) ≥80% threshold
   - **Verbatim hash overlap** (atom verbatim Jaccard or sha256 hash intersection) ≥80% threshold
4. **Both ≥80% → PASS** (4 rounds × 100% effective rate validates spec)
5. **Either <80% → FAIL** + DIRECTION analysis (which agent drifted) + writer-family motif analysis + finding accumulation

### Reports
- `evidence/checkpoints/drift_cal_p<XXX>_<rerun_agent>_rerun.jsonl` (raw rerun output)
- `evidence/checkpoints/drift_cal_batch_27_p<XXX>_report.md` (NEW1 dual-threshold report + DIRECTION + writer-family motif)

### Finding allocation
- If FAIL: O-P1-84 HIGH/MEDIUM (drift cal value-add) + DIRECTION REVERSED 9th precedent (or non-reversed)

═══════════════════════════════════════════════════════════════════
## §7 — STEP 6 Rule A 10-Atom Audit (slot #36 oh-my-claudecode:architect, AUDIT pivot 17th, omc-family 9th burn)
═══════════════════════════════════════════════════════════════════

### Rule A sample build
- Sample size: 10 atoms (1/page p.261-270 stratified)
- Seed: 20260605 (round 5 deterministic)
- Stratification target: 4-5 TABLE_ROW + 3 HEADING (含 §6.3.5.8 MI L4 + L5 + L6 + R12 transition) + 1-2 LIST_ITEM + 1 CODE_LITERAL
- Output: `evidence/checkpoints/rule_a_batch_27_sample.jsonl`

### Reviewer dispatch — slot #36 oh-my-claudecode:architect
- AUDIT-mode pivot 17th, omc-family 9th burn
- Tools: All except Write/Edit, **READ-ONLY** (per agent description)
- 适配: write-tool-less + **no-Bash inline content** (per round 3 batch 20 #29 plugin-dev:skill-reviewer + round 4 batch 25 #34 feature-dev:code-architect sub-pattern)
- AUDIT-mode prepend:
  ```
  Mode: AUDIT for PDF atomization quality, NOT strategic architecture / NOT debugging advisor / NOT codebase pattern analysis.
  Task: 10-atom Rule A reviewer for SDTM PDF atom verification against PDF p.261-270 ground truth.
  Adaptation: write-tool-less + no-Bash inline content — produce verdicts.jsonl + summary.md fully inline in your response; main session writes files preserving content verbatim.
  ```
- Final reviewer message: `Rule A batch 27 weighted=<X>% PASS_n=<P> PARTIAL_n=<PA> FAIL_n=<F>`

### Output files (main session writes verbatim from reviewer inline)
- `evidence/checkpoints/rule_a_batch_27_verdicts.jsonl`
- `evidence/checkpoints/rule_a_batch_27_summary.md`

═══════════════════════════════════════════════════════════════════
## §8 — STEP 7 Findings Documentation (G-MS-13 self-validation gate)
═══════════════════════════════════════════════════════════════════

### Allowed range
**O-P1-84, O-P1-85, O-P1-86, O-P1-87** (4 reserved).

### Expected findings (round 5 batch 27 high-risk)
- O-P1-84 HIGH/MEDIUM (drift cal NEW1 result — verdict per data)
- O-P1-85+ (any NEW7 L6 sub-batch context drift recurrence — round 3 + round 4 = 2× pattern)
- O-P1-86+ (any NEW6.b L4 violation despite procedural enforcement — would escalate v1.4 priority)
- O-P1-87+ (any writer-family wide-table corruption — 9th batch cumulative if so)

═══════════════════════════════════════════════════════════════════
## §9 — STEP 8 Final Message + Files Written
═══════════════════════════════════════════════════════════════════

### Files written by session C
- `evidence/checkpoints/pdf_atoms_batch_27a.jsonl` + `pdf_atoms_batch_27b.jsonl`
- 任何 Rule B `.pre-OptionH-*.bak` 备份
- 任何 `option_e_rerun_p<NNN>.jsonl`
- `evidence/checkpoints/drift_cal_p<XXX>_<rerun_agent>_rerun.jsonl`
- `evidence/checkpoints/drift_cal_batch_27_p<XXX>_report.md`
- `evidence/checkpoints/_progress_batch_27.json`
- `evidence/checkpoints/P1_batch_27_report.md`
- `evidence/checkpoints/rule_a_batch_27_sample.jsonl` + `_verdicts.jsonl` + `_summary.md`

### Files NOT touched
[同 batch_26_kickoff.md §9 NEVER DO 列表]

### Final echo (single line, mandatory)
```
PARALLEL_SESSION_27_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered findings_added=<O-P1-84,...>
```

### Brief 3-5 sentence user-facing summary
含: §6.3.5.7→§6.3.5.8 MI R12 transition + NEW6.b proactive verification + NEW7 L6 sub-batch handoff effectiveness + drift cal NEW1 5th time verdict + reviewer slot #36 omc:architect AUDIT pivot 17th + carry-over to reconciler.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

[同 batch_26_kickoff.md NEVER DO 列表]

The boulder never stops. 第一步 STEP 0 并行 5-file Read + Pre-flight + PDF p.4 TOC verify + p.260-270 preview + 选 drift cal target page.
