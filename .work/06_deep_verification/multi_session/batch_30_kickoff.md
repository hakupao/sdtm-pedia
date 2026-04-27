# Batch 30 Kickoff (Multi-Session Parallel — Session C, Round 6)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 9 STEPs (pre-flight / writer dispatch / schema sweep / DRIFT CAL MANDATORY / Rule A / findings / final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号 = STEP 9 echo 单行 `PARALLEL_SESSION_30_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered findings_added=<O-P1-97,...>` + 3-5 句 user-facing summary.
>
> Halt-only fallback per G-MS-4 (5 rounds spec-only no live-fire — round 5 confirmed spec-only carry-forward): echo `HALT_BATCH_30 reason=<X>` + write `halt_state_batch_30.md`.
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel round 6 的 **session C (batch 30)**.
> Sister sessions = B (batch 29) + D (batch 31); 物理并行 3 终端各跑 1 batch + 1 reconciler 收尾.
> **Drift cal MANDATORY 本 batch** (cadence batch 27→30, every-3-batches + cumulative atoms post-p.270 ≥600 双触发 — NEW1 dual-threshold 6th time).

═══════════════════════════════════════════════════════════════════
## §0 — Round 6 Finding ID Range Cross-Validation Table (G-MS-13 codified)
═══════════════════════════════════════════════════════════════════

**Round 6 reserved ranges** (post round 5 last used **O-P1-92** = reconciler-side NEW7 L6 cross-batch context drift 3rd recurrence):

| Session | Batch | Range | 本 batch 用 |
|---|---|---|---|
| B | 29 | O-P1-93..96 | ❌ sister, 不可越界 |
| C | 30 | **O-P1-97..100** | ✅ 本 session 唯一合法范围 |
| D | 31 | O-P1-101..104 | ❌ sister, 不可越界 |

**Self-validation gate** (STEP 8 强制): 任何 finding ID ≤96 OR ≥101 → STOP fix.

═══════════════════════════════════════════════════════════════════
## §1 — Scope + Pre-Dispatch TOC Verification
═══════════════════════════════════════════════════════════════════

**Page range**: ig34 p.291-300 (10 pages)

**Expected sections** (per round 5 retro carry-forward + batch 29 anticipated terminal):
- Round 5 ended at §6.3.5.9.3 PP-PC Relating (PD group container L5 sib=3) p.280; batch 29 (p.281-290) likely 续 §6.3.5.9.3 末 + §6.3.5.10+ NEW sub-domain transition
- p.291-300: 续 batch 29 终态; 取决 batch 29 处于哪个 §6.3.5.X+ / §6.3.6 sub-domain (主 session pre-dispatch 时根据 batch 29 a/b 终态 + PDF p.4 TOC 复核)
- 任何 NEW class transition (§6.3 → §6.4 OR §6.5+) 概率随 §6.3.5 终结而升 — 概率 MEDIUM-HIGH 落 batch 30 scope

**MUST pre-dispatch verify**:
1. Read PDF `source/SDTMIG v3.4 (no header footer).pdf` p.4 TOC 锁 §6.3.5.X+ 末页 + §6.3.6+ / §6.4+ 起页
2. Read PDF p.290-300 preview 锁 任何 transition zone (R12 3-zone partition target)
3. 写 pre-dispatch TOC anchor block 加到 STEP 2 dispatch prompt

═══════════════════════════════════════════════════════════════════
## §2 — Cumulative R-Rules + NEW Codification Carry-Forward
═══════════════════════════════════════════════════════════════════

**v1.3 prompts active since 2026-04-27** — 13 codification items (A-M) all codified inline in `subagent_prompts/P0_writer_pdf_v1.3.md`. Each sub-batch dispatch prompt MUST inline-prepend the v1.3 prompt body. See `P0_writer_pdf_v1.3.md` §CODIFIED R-RULES + NEW for full details A-M.

**Round 5 carry-forward addendum** (per `MULTI_SESSION_RETRO_ROUND_5.md`):
- v1.4 candidate accumulation: 5 累 (O-P1-89 Write-overwrite Bash-heredoc append HIGH + O-P1-91 NEW7 parent_section canonical full-form LOW + O-P1-85 NEW8.d TABLE_ROW value-cell verbatim integrity MEDIUM + O-P1-88 EDITORIAL_CORRECTION verdict path HIGH + O-P1-90 atom_id 4-digit padding regex hardening LOW); v1.4 cut decision pending round 6 reconciler.
- O-P1-80 round 5 NEW7 L4-group-container shared-Examples-L5-as-peer precedent (round 4 O-P1-75 RESTART branch extended).

### 🔴 NEW7 L6 Sub-Batch Handoff (PROCEDURAL ENFORCEMENT — ROUND 6 MANDATORY)

Round 3 batch 23 + round 4 batch 25 + round 5 reconciler-side O-P1-92 = **3× cross-batch RECURRENCE**. Round 5 verdict:
- **INTRA-batch** prepend EFFECTIVE 1st live-fire 0 recurrence (O-P1-81 PROACTIVE batch 26)
- **CROSS-batch** STILL DRIFTS (O-P1-92 reconciler-side Option H 3rd recurrence) → round 6 kickoff CROSS-batch handoff codification MANDATORY.

主 session **必须** prepend prior sub-batch state when dispatching 30b:
```
PRIOR SUB-BATCH 30a HEADING STATE (sub-batch 30b MUST continue, NOT restart):
- Last L4 sib used (under §6.3.5 OR §6.3.6+): <N>
- Last L5 sib used: <M>
- Last L6 Example sib used: <K>
- Convention: Example N+1 = HEADING hl=6 sib=K+1 (ALWAYS, NEVER SENTENCE)
- §6.3.5.X.Examples HEADING ALWAYS hl=5 sib=4
- 任何 NEW L4 HEADING parent = `§6.3.5 Specimen-based Findings Domains` OR §6.3.6+ group container per NEW6.b L3-group-parent
```

═══════════════════════════════════════════════════════════════════
## §3 — STEP 0 Pre-Flight + R-Rules Pre-Dispatch
═══════════════════════════════════════════════════════════════════

### STEP 0.1 Read necessary files (并行 Read)
1. `multi_session/MULTI_SESSION_PROTOCOL.md` (master)
2. `multi_session/MULTI_SESSION_RETRO_ROUND_5.md` (round 5 retro — read §1.6 NEW1 5× validated for drift cal protocol)
3. `subagent_prompts/P0_writer_pdf_v1.3.md` (v1.3 prompts active)
4. `evidence/checkpoints/_progress_batch_28.json` (round 5 batch 28 terminal state)
5. `evidence/checkpoints/drift_cal_batch_27_p270_report.md` (last drift cal NEW1 5th time CATASTROPHIC FAIL p.270 — strict 71.1% / verbatim 6.7% LOWEST EVER; writer-family R10 + value-hallucination NEW motif O-P1-85; safety net validated writer rerun discarded root preserved)

### STEP 0.2 Pre-dispatch verify
- root `pdf_atoms.jsonl` line count == **7092** (post round 5 baseline; round 4 6146 + round 5 +946)
- `_progress_batch_28.json` status == "completed"
- PDF p.4 TOC re-verified for §6.3.5.X+ 末页 / §6.3.6+ / §6.4+ 起页
- PDF p.290-300 preview verified
- Reviewer slot #39 **superpowers:code-reviewer** dispatchable (superpowers family first burn — All tools incl. Write/Edit, full-tool no adaptation; 20th AUDIT pivot, drift cal carrier 6th time)

═══════════════════════════════════════════════════════════════════
## §4 — STEP 1-3 Writer Dispatch
═══════════════════════════════════════════════════════════════════

### Sub-batch split strategy
- 30a = oh-my-claudecode:writer × p.291-295 (5 pages)
- 30b = oh-my-claudecode:executor × p.296-300 (5 pages)
- **NEW7 L6 procedural handoff**: 30b prompt 必须 inline-prepend 30a 终态 (last L4/L5/L6 sib + Example N convention)

### Dispatch protocol
1. 主 session 并行 dispatch 2 Agent calls — 30a writer + 30b executor (single message, 2 tool uses)
2. Each agent prompt 必须 inline-prepend 完整 v1.3 R-rules + NEW1-NEW8 + sub-batch handoff prepend (30b only)
3. Output: `evidence/checkpoints/pdf_atoms_batch_30<a|b>.jsonl`
4. Final DONE single-line per agent

═══════════════════════════════════════════════════════════════════
## §5 — STEP 4 Schema + Format Sweeps + R12 Transition + NEW6.b
═══════════════════════════════════════════════════════════════════

Python integrity sweep:
1. **0 JSON parse errors** + 9-enum + 4-digit atom_id + 0 frame tag + 0 within-batch dup + 0 root collision
2. **Density alarm** per-page (15 floor) + sub-batch (100 floor)
3. **NEW6.b L4 self-parent sweep**: 任何 NEW L4 sub-domain HEADING (likely §6.3.5.X+ OR §6.3.6+ if class transition) parent_section MUST = group container (NOT self-parent); round 4-5 EFFECTIVE proactive precedent → expect 0 violation if procedural enforcement holds
4. **NEW7 chain check**:
   - L5 chain Description=1/Spec=2/Assump=3/Examples=4 RESTART under each new sub-domain
   - L6 Examples N RESTART under sub-domain
   - L7 sub-example if visible
5. **R12 transition page sweep** (任何 NEW L4 sub-domain transition OR class transition):
   - ≥8 atoms required + 3-zone partition
   - 30a/30b sub-batch boundary 可能跨 transition page → handoff state critical for 30b
6. **R15 cross-batch sibling check**:
   - With batch 29 terminal: chain continuity OR domain change
7. Any violation → Option H inline + Rule B backup

═══════════════════════════════════════════════════════════════════
## §6 — STEP 5 🔴 DRIFT CAL MANDATORY (NEW1 dual-threshold, 6th time)
═══════════════════════════════════════════════════════════════════

### Trigger basis
- Cadence: every-3-batches batch 27 → 30
- Cumulative atoms post-p.270: batch 28 (~250 est) + batch 29 (~250 est) + batch 30 (~250 est) ≥600 ✅ 双触发

### Target page selection
推荐 dense page in 30a/30b scope (TBD by session C upon p.291-300 preview):
- Top candidate: dense Spec/Assumption table page (mixed HEADING + TABLE_HEADER + TABLE_ROW) IF 任何 sub-domain Spec table 落 30 scope
- Alternative: any R12 transition page IF NEW sub-domain visible (tests heading_fields drift)
- Alternative: dense Examples page IF Examples L6 visible

### Method (NEW1 dual-threshold, round 6 6th time, 5 rounds × 100% effective if round 5 PASS)
1. Baseline = 30a/30b 主写手 atom set on target page
2. Rerun = alternation agent (if baseline = writer → rerun = executor; if baseline = executor → rerun = writer)
3. Compare:
   - **Strict count overlap** (atom_id count match) ≥80% threshold
   - **Verbatim hash overlap** (atom verbatim Jaccard or sha256 hash intersection) ≥80% threshold
4. **Both ≥80% → PASS** (5+ rounds × 100% effective rate validates spec)
5. **Either <80% → FAIL** + DIRECTION analysis (which agent drifted) + writer-family motif analysis + finding accumulation

### Reports
- `evidence/checkpoints/drift_cal_p<XXX>_<rerun_agent>_rerun.jsonl` (raw rerun output)
- `evidence/checkpoints/drift_cal_batch_30_p<XXX>_report.md` (NEW1 dual-threshold report + DIRECTION + writer-family motif)

### Finding allocation
- If FAIL: O-P1-97 HIGH/MEDIUM (drift cal value-add) + DIRECTION REVERSED 10th precedent (round 5 batch 27 was 9th — round 5 was first FAIL after 4 PASS so direction continuation possible) + writer-family motif analysis (round 5 NEW VALUE-HALLUCINATION motif O-P1-85 may extend)
- If PASS: log validation streak break-and-resume + free finding ID

═══════════════════════════════════════════════════════════════════
## §7 — STEP 6 Rule A 10-Atom Audit (slot #39 superpowers:code-reviewer, AUDIT pivot 20th, superpowers family first burn)
═══════════════════════════════════════════════════════════════════

### Rule A sample build
- Sample size: 10 atoms (1/page p.291-300 stratified)
- Seed: 20260620 (round 6 deterministic)
- Stratification target: 4-5 TABLE_ROW + 3 HEADING (含 任何 NEW L4 transition + L5 + L6 + R12 transition) + 1-2 LIST_ITEM + 1 CODE_LITERAL
- Output: `evidence/checkpoints/rule_a_batch_30_sample.jsonl`

### Reviewer dispatch — slot #39 **superpowers:code-reviewer**
- AUDIT-mode pivot 20th, **superpowers family first burn** (round 6 cross-family pivot: batch 29 = pr family / batch 30 = superpowers / batch 31 = pr family second agent — validates AUDIT recipe across 2 NEW families + 1 intra-family depth burn)
- Tools: All tools (full-tool — Write/Edit available, no adaptation needed)
- **AUDIT-mode prepend** (强调禁止默认 mode):
  ```
  Mode: AUDIT for SDTM PDF atomization quality, NOT general code review against project plan / NOT spec adherence / NOT step-by-step requirements review.
  Task: 10-atom Rule A reviewer for SDTM PDF atom verification against PDF p.291-300 ground truth + drift cal supplemental cross-validation if dense table page.
  Adaptation: full-tool — write verdicts.jsonl + summary.md to evidence/checkpoints/ directly via Write tool (per round 5 batch 28 #37 general-purpose precedent + round 6 batch 29 #38 pr-review-toolkit:code-reviewer precedent).
  ```
- Final reviewer message: `Rule A batch 30 weighted=<X>% PASS_n=<P> PARTIAL_n=<PA> FAIL_n=<F>`

### Output files (reviewer writes directly via Write tool)
- `evidence/checkpoints/rule_a_batch_30_verdicts.jsonl`
- `evidence/checkpoints/rule_a_batch_30_summary.md`

═══════════════════════════════════════════════════════════════════
## §8 — STEP 7 Findings Documentation (G-MS-13 self-validation gate)
═══════════════════════════════════════════════════════════════════

### Allowed range
**O-P1-97..O-P1-100** (4 reserved).

### Expected findings (round 6 batch 30 high-risk — drift cal carrier)
- O-P1-97 HIGH/MEDIUM (drift cal NEW1 6th result — verdict per data; round 5 was first FAIL after 4× PASS so 6th could be FAIL again OR recovery)
- O-P1-98+ (任何 NEW7 L6 cross-batch context drift 4th recurrence post round 5 reconciler O-P1-92 → ESCALATE v1.4 emergency)
- O-P1-99+ (任何 NEW6.b L4 violation despite 6× streak — would break streak + escalate)
- O-P1-100+ (任何 writer-family wide-table corruption / VALUE-HALLUCINATION extension / Write-overwrite recurrence — 10th+ batch cumulative)

═══════════════════════════════════════════════════════════════════
## §9 — STEP 8 Final Message + Files Written
═══════════════════════════════════════════════════════════════════

### Files written by session C
- `evidence/checkpoints/pdf_atoms_batch_30a.jsonl` + `pdf_atoms_batch_30b.jsonl`
- 任何 Rule B `.pre-OptionH-*.bak` 备份
- 任何 `option_e_rerun_p<NNN>.jsonl`
- `evidence/checkpoints/drift_cal_p<XXX>_<rerun_agent>_rerun.jsonl`
- `evidence/checkpoints/drift_cal_batch_30_p<XXX>_report.md`
- `evidence/checkpoints/_progress_batch_30.json`
- `evidence/checkpoints/P1_batch_30_report.md`
- `evidence/checkpoints/rule_a_batch_30_sample.jsonl` + `_verdicts.jsonl` + `_summary.md`

### Files NOT touched
[同 batch_29_kickoff.md §9 NEVER DO 列表]

### Final echo (single line, mandatory)
```
PARALLEL_SESSION_30_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered findings_added=<O-P1-97,...>
```

### Brief 3-5 sentence user-facing summary
含: §6.3.5.X+ / §6.3.6+ scope + 任何 R12 transition + NEW6.b proactive 7× streak status + NEW7 L6 sub-batch handoff (intra+cross) effectiveness + drift cal NEW1 6th time verdict + reviewer slot #39 **superpowers:code-reviewer** AUDIT pivot 20th superpowers family first burn + carry-over to reconciler.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

[同 batch_29_kickoff.md NEVER DO 列表]

The boulder never stops. 第一步 STEP 0 并行 5-file Read + Pre-flight + PDF p.4 TOC verify + p.290-300 preview + 选 drift cal target page.
