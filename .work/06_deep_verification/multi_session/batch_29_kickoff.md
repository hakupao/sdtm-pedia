# Batch 29 Kickoff (Multi-Session Parallel — Session B, Round 6)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 8 STEPs (pre-flight / writer dispatch / schema sweep / drift cal SKIP / Rule A / findings / final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control, 不要说 "ready for review".**
>
> 唯一合法收尾信号 = STEP 8 echo 单行 `PARALLEL_SESSION_29_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-93,...>` + 一段 3-5 句 user-facing summary.
>
> 仅 halt-only fallback (per G-MS-4 round 2 spec, 5 rounds 累计 spec-only 无 live-fire — round 5 confirmed spec-only carry-forward) 才允许 echo `HALT_BATCH_29 reason=<X>` + 写 `halt_state_batch_29.md`. 其他场景全 hard-stop 不可中断.
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel round 6 的 **session B (batch 29)**.
> Sister sessions = C (batch 30) + D (batch 31); 物理并行 3 终端各跑 1 batch + 1 reconciler 收尾.
> Session 之间 **绝对不通信**, 只通过 evidence/checkpoints/ 下独占文件交付; 共享 root files (pdf_atoms.jsonl / audit_matrix.md / _progress.json) **绝对不动** — 留 reconciler 串行合并.

═══════════════════════════════════════════════════════════════════
## §0 — Round 6 Finding ID Range Cross-Validation Table (G-MS-13 codified, round 4+5 EFFECTIVE)
═══════════════════════════════════════════════════════════════════

**Round 6 reserved ranges** (3 sister sessions disjoint, post round 5 last used **O-P1-92** = reconciler-side NEW7 L6 cross-batch context drift 3rd recurrence):

| Session | Batch | Range | 本 batch 用 |
|---|---|---|---|
| B | 29 | **O-P1-93..96** | ✅ 本 session 唯一合法范围 |
| C | 30 | O-P1-97..100 | ❌ sister session, 不可越界 |
| D | 31 | O-P1-101..104 | ❌ sister session, 不可越界 |

**Self-validation gate** (STEP 7 强制): 任何 finding ID 越界 (≤92 OR ≥97) → STOP fix.

═══════════════════════════════════════════════════════════════════
## §1 — Scope + Pre-Dispatch TOC Verification
═══════════════════════════════════════════════════════════════════

**Page range**: ig34 p.281-290 (10 pages)

**Expected sections** (per round 5 reconciler retro carry-forward):
- p.280 末 = §6.3.5.9.3 Relating PP Records to PC Records (PD group container internal L5 sib=3) Examples 3 / Method D L6/L7 chain context
- §6.3.5.9 = PD (Pharmacokinetics Domains) group container with §6.3.5.9.1 PC + §6.3.5.9.2 PP + §6.3.5.9.3 PP-PC Relating (3 sister L5 sub-domains)
- p.281-290: 续 §6.3.5.9.3 末 (若 PP-PC Relating Examples 续 OR 终结) + likely §6.3.5.10+ NEW sub-domain transition OR §6.3.6+ class transition if §6.3.5 完结
- 实际 sub-domain 节号 / 起页 / transition 数 = 主 session pre-dispatch 时根据 PDF p.4 TOC 复核

**MUST pre-dispatch verify** (主 session 不可省, ground truth 锁):
1. Read PDF `source/SDTMIG v3.4 (no header footer).pdf` p.4 (TOC) 验 §6.3.5.10+ / §6.3.6+ 实际起页 + 任何 deeper sub-domain
2. Read PDF p.280-290 preview (5-10 atoms/page sanity) 锁:
   - p.280 末 atom = §6.3.5.9.3 Examples 3 / Method D 区域 (per O-P1-91 finding scope: §6.3.5.9.3 Examples Method A/B/C/D × Example 1/2/3 L6/L7 chain)
   - p.281 起 = batch 29 起点
3. 写 pre-dispatch TOC anchor block 加到 STEP 2 dispatch prompt (每 sub-batch 顶部)

═══════════════════════════════════════════════════════════════════
## §2 — Cumulative R-Rules + NEW Codification Carry-Forward (ROUND 6 PROCEDURAL ENFORCEMENT)
═══════════════════════════════════════════════════════════════════

### R-Rules R1-R15 + NEW1-NEW8 Codification

**v1.3 prompts active since 2026-04-27** — 13 codification items (A-M: R1-R15 + O-P1-26 + NEW1-NEW8 + NEW6/NEW6.b dual-form L4 self-parent + NEW7 chain + NEW7 L4 group-container branch + NEW8.b SENTENCE-trigram + NEW8.c TABLE_HEADER column-set + G-MS-12 density + G-MS-12.a content-type-aware floor + G-MS-13 cross-validation table cross-reference) all codified inline in `subagent_prompts/P0_writer_pdf_v1.3.md`. Each sub-batch dispatch prompt MUST inline-prepend the v1.3 prompt body.

See `subagent_prompts/P0_writer_pdf_v1.3.md` §CODIFIED R-RULES + NEW for full details A-M.

**Round 5 carry-forward addendum** (per `MULTI_SESSION_RETRO_ROUND_5.md` + reconciler status string):
- v1.4 candidate accumulation: O-P1-89 Write-overwrite Bash-heredoc append procedural enforcement (HIGH) + O-P1-91 NEW7 L6/L7 parent_section canonical full-form (LOW) + O-P1-85 NEW8.d TABLE_ROW value-cell verbatim integrity (MEDIUM) + O-P1-88 EDITORIAL_CORRECTION verdict path (HIGH) + O-P1-90 atom_id 4-digit padding regex hardening (LOW) — 累 5 v1.4 candidates (0 EMERGENCY, 2 HIGH); v1.4 cut decision pending round 6 reconciler.
- O-P1-80 round 5 NEW7 L4-group-container shared-Examples-L5-as-peer precedent (round 4 O-P1-75 RESTART branch extended) — codified addendum to NEW7 chain.

### 🔴 NEW7 L6 Sub-Batch Handoff (PROCEDURAL ENFORCEMENT — ROUND 6 MANDATORY)

Round 3 batch 23 + round 4 batch 25 + **round 5 reconciler-side O-P1-92** = 3 occurrences of NEW7 L6 cross-batch HEADING continuity drift. Round 5 verdict (per `MULTI_SESSION_RETRO_ROUND_5.md` D-MS-X):
- **INTRA-batch** procedural prepend (sub-batch a → sub-batch b within same batch) = EFFECTIVE 1st live-fire 0 recurrence (O-P1-81 PROACTIVE first-attempt batch 26 §6.3.5.7.3 Examples 1/2/3 hl=6 sib=1/2/3 RESTART correct)
- **CROSS-batch** procedural enforcement = STILL DRIFTS (O-P1-92 reconciler-side Option H 3rd recurrence = round 3 + round 4 + round 5 = 3× motif) — **round 6 kickoff CROSS-batch handoff codification MANDATORY** (kickoff §1 expected sections + §4 dispatch prompt prepend prior batch's terminal sub-batch L4/L5/L6 chain state).

**Round 6 fix (procedural, sustains)**: 主 session **必须** 在 dispatch sub-batch B prompt 时 inline-prepend prior sub-batch A 的 L5/L6 chain 终态:
```
PRIOR SUB-BATCH A HEADING STATE (sub-batch B MUST continue, NOT restart):
- Last L5 sib used: <N>
- Last L6 Example sib used: <M>
- Convention: Example N+1 = HEADING hl=6 sib=M+1 (ALWAYS, NEVER SENTENCE)
- §6.3.5.X.Examples HEADING ALWAYS hl=5 sib=4
```

无 prior state 推断 = 视为 R15 + NEW7 procedural violation, 必须 Option H 修.

### G-MS-12 Density Alarm Threshold
- Per-page floor 15 atoms (list-only sub-rule v1.4 candidate floor=8)
- Per-sub-batch floor 100 atoms
- Alarm fires → 主 session PDF cross-check (Read tool `pages: "<N>"`) + adjudicate FALSE POSITIVE vs TRUE POSITIVE → Option E iff TRUE POSITIVE
- Round 2-4 reaffirm: 3 FALSE POSITIVE precedent

### G-MS-13 Finding ID Range Cross-Validation
- §0 cross-validation table at top of kickoff (3-batch range table)
- Self-validation gate at STEP 7
- Round 4+5 EFFECTIVE (0 mis-allocation across 6 sister sessions)

═══════════════════════════════════════════════════════════════════
## §3 — STEP 0 Pre-Flight + R-Rules Pre-Dispatch
═══════════════════════════════════════════════════════════════════

### STEP 0.1 Read necessary files (并行 Read)
1. `multi_session/MULTI_SESSION_PROTOCOL.md` (master)
2. `multi_session/MULTI_SESSION_RETRO_ROUND_5.md` (round 5 retro 36469 bytes — 主要读 §1 retain (NEW7 L6 intra-batch EFFECTIVE 1st live-fire + general-purpose family-agnostic recipe + NEW6.b 6× streak) + §2 gap (NEW7 L6 cross-batch 3rd recurrence + NEW1 5th time CATASTROPHIC FAIL + Write-overwrite NEW motif) + §3 decision (v1.4 cut RECOMMENDED 1st time))
3. `subagent_prompts/P0_writer_pdf_v1.3.md` (writer/executor R-rule block — v1.3 prompts active)
4. `evidence/checkpoints/_progress_batch_28.json` (round 5 batch 28 terminal state for R15 carry)

### STEP 0.2 Pre-dispatch verify
- root `pdf_atoms.jsonl` line count == **7092** (post round 5 reconciler merge baseline; round 4 baseline 6146 + round 5 +946 = 7092)
- `_progress_batch_28.json` status == "completed"
- PDF p.4 TOC re-verified for §6.3.5.10+ / §6.3.6+ sub-domain page ranges
- PDF p.280-290 preview verified
- Reviewer slot #38 **pr-review-toolkit:code-reviewer** dispatchable (pr family first burn — All tools incl. Write/Edit, full-tool no adaptation needed; 19th AUDIT pivot, recipe family-agnostic round 5 batch 28 general-purpose validation extends to pr family round 6)

### STEP 0.3 Pre-Flight Gate PASS
任一不通过 → halt + 报告 `HALT_BATCH_29 reason=<X>`. **不要** 私自 fix.

═══════════════════════════════════════════════════════════════════
## §4 — STEP 1-3 Writer Dispatch
═══════════════════════════════════════════════════════════════════

### Sub-batch split strategy
- 29a = oh-my-claudecode:writer × p.281-285 (5 pages)
- 29b = oh-my-claudecode:executor × p.286-290 (5 pages, 续接 29a; NEW7 L6 procedural handoff prepend mandatory)

### Dispatch protocol
1. 主 session 并行 dispatch 2 Agent calls (single message, 2 tool uses) — 29a writer + 29b executor
2. Each agent prompt MUST include:
   - HARD-STOP DIRECTIVE (sub-agent context only — return DONE single line atoms=N failures=F not user-facing)
   - Full v1.3 R-rules block (inline-prepend per `subagent_prompts/P0_writer_pdf_v1.3.md`)
   - **NEW7 L6 procedural handoff prepend** (29b only — 29a 终态 echo'd into 29b prompt; for 29a alone, prior sub-batch is round 5 batch 28b 终态 = `§6.3.5.9.3 Relating PP Records to PC Records (PD group container L5 sib=3) — last L6 Example sib=3 (Example 3) + last L7 Method sib=4 (Method D) + atoms ending at p.280 within Example 3 / Method D context; convention: 后续若 PP-PC Relating 续 → Example/Method chain continuation; 若 §6.3.5.10+ NEW L4/L5 sub-domain transition → L4 sib chain RESTART per NEW6.b L3-group-parent + L5 chain Description=1/Spec=2/Assump=3/Examples=4 RESTART under NEW sub-domain`)
   - Density alarm threshold spec
   - G-MS-13 finding ID range note (no findings written by writer/executor; reviewer + main session reserve)
   - Output: append-mode JSONL to `evidence/checkpoints/pdf_atoms_batch_29<a|b>.jsonl`
   - Final DONE line single-line `DONE atoms=N failures=F`
3. 验 29a + 29b 终 DONE; wc -l 各 jsonl 与 atoms=N 匹配; 0 schema err

═══════════════════════════════════════════════════════════════════
## §5 — STEP 4 Schema + Format Sweeps
═══════════════════════════════════════════════════════════════════

Python integrity sweep (执行后写 `_progress_batch_29.json` step_4_sweeps 字段):
1. **0 JSON parse errors** + 0 BAD atom_type (∈ 9-enum) + 0 BAD atom_id (4-digit `_aXXX_`) + 0 frame tag in verbatim + 0 within-batch dup atom_ids + 0 collision with root pdf_atoms.jsonl
2. **Density alarm check** per-page (15 floor) + sub-batch (100 floor)
3. **NEW6 dual-form sweep** + **NEW6.b L4 self-parent** sweep (任何 §6.3.5.X+ / §6.3.6+ NEW L4 sub-domain transition — parent = group container OR L3 parent per dual-form)
4. **NEW7 chain check**:
   - L5/L6 chain continuity from batch 28 terminal: §6.3.5.9.3 Examples sib=4 → if PP-PC Relating Examples 续 in 29a → L6 Example N sib continuation OR Method-level L7 continuation; if §6.3.5.10+ NEW transition → 全 chain RESTART under NEW sub-domain
   - L7 sub-example if visible (Method A/B/C/D within Example pattern from batch 28 may continue; round 5 deepest precedent O-P1-86 = L7 PC Example 1 round 5)
   - 任何 §6.3.5.10+ / §6.3.6+ NEW sub-domain RESTART under appropriate L3/L4 parent (per NEW6.b 6× streak post round 5 — proactive parent assignment expected)
   - O-P1-91 round 5 carry-forward: L6/L7 atoms parent_section MUST use canonical full-form `§N.N.N — Sub-Heading-Title` (NOT bare `Example N` shortcut; v1.4 candidate but apply now per round 5 reviewer flag)
5. **R12 transition page sweep** (任何 NEW sub-domain transition in scope — ≥8 atoms 3-zone partition)
6. **R15 cross-batch sibling check** with batch 28 terminal: §6.3.5.9.3 PP-PC Relating L5 sib=3 / Examples L5 sib=4 / Example 3 L6 sib=3 / Method D L7 sib=4 → batch 29 起点 contiguous OR §6.3.5.10+ NEW L4 sib=10+ RESTART under §6.3.5
7. Any violation → Option H inline + Rule B backup (`pdf_atoms_batch_29<a|b>.jsonl.pre-OptionH-<reason>.bak`)

═══════════════════════════════════════════════════════════════════
## §6 — STEP 5 Drift Cal SKIP per Cadence
═══════════════════════════════════════════════════════════════════

- 不触发 (per cadence: 上次 batch 27 p.270 NEW1 5th time CATASTROPHIC FAIL, next mandatory batch 30 = sister session C scope)
- 写 `_progress_batch_29.json` drift_cal: triggered=false, next_mandatory="batch 30"

═══════════════════════════════════════════════════════════════════
## §7 — STEP 6 Rule A 10-Atom Audit (slot #38 pr-review-toolkit:code-reviewer, AUDIT pivot 19th, pr family first burn)
═══════════════════════════════════════════════════════════════════

### Rule A sample build
- Sample size: 10 atoms (1/page p.281-290 stratified)
- Seed: 20260615 (round 6 deterministic)
- Stratification target: 4-5 TABLE_ROW + 2-3 HEADING (含 任何 NEW sub-domain L4 transition + L5/L6 sub-section transitions) + 1-2 LIST_ITEM + 1 CODE_LITERAL/TABLE_HEADER
- Output: `evidence/checkpoints/rule_a_batch_29_sample.jsonl`

### Reviewer dispatch — slot #38 **pr-review-toolkit:code-reviewer**
- AUDIT-mode pivot 19th, **pr-review-toolkit family first burn** (round 5 batch 28 general-purpose family AUDIT pivot SUCCESS 18th = recipe family-agnostic VALIDATED → round 6 extends to pr-review-toolkit)
- Tools: All tools (full-tool — Write/Edit available, no adaptation needed; vs round 3-5 omc/feature-dev/vercel/plugin-dev write-tool-less family + bash-heredoc adaptation)
- **AUDIT-mode prepend** (强调禁止默认 mode):
  ```
  Mode: AUDIT for SDTM PDF atomization quality, NOT general PR code review / NOT CLAUDE.md style guide compliance / NOT git diff analysis.
  Task: 10-atom Rule A reviewer for SDTM PDF atom verification against PDF p.281-290 ground truth.
  Adaptation: full-tool — write verdicts.jsonl + summary.md to evidence/checkpoints/ directly via Write tool (per round 5 batch 28 #37 general-purpose precedent).
  ```
- Final reviewer message: `Rule A batch 29 weighted=<X>% PASS_n=<P> PARTIAL_n=<PA> FAIL_n=<F>`
- Effective threshold: ≥90% (raw or post-Option-E rerun)

### Output files (reviewer writes directly via Write tool)
- `evidence/checkpoints/rule_a_batch_29_verdicts.jsonl`
- `evidence/checkpoints/rule_a_batch_29_summary.md`

═══════════════════════════════════════════════════════════════════
## §8 — STEP 7 Findings Documentation (G-MS-13 self-validation gate)
═══════════════════════════════════════════════════════════════════

### Allowed range
**O-P1-93..O-P1-96** (4 reserved, 0-4 used; unused freed for compression).

### Self-validation gate
After drafting findings_added array in `_progress_batch_29.json`, verify each finding_id:
- ∈ {93, 94, 95, 96} → PASS
- ≤92 (collide with prior cumulative incl. round 5 reconciler O-P1-92 NEW7 L6 cross-batch 3rd recurrence) → STOP renumber
- ≥97 (collide with sister batch 30 O-P1-97..100 OR batch 31 O-P1-101..104) → STOP renumber

### Each finding 字段
ID + Severity + Category + Title + Scope + atom_id(s) affected + rule_violation + repair_action + v1.3/v1.4_candidate (if applicable) + writer_family_motif (if applicable, joining cumulative wide-table family O-P1-23/34/36/37/38/50/63/71 + round 5 新增 O-P1-84 drift-cal-CATASTROPHIC + O-P1-85 NEW VALUE-HALLUCINATION motif + O-P1-88 EDITORIAL_CORRECTION + O-P1-89 Write-overwrite-silent-loss)

═══════════════════════════════════════════════════════════════════
## §9 — STEP 8 Final Message + Files Written
═══════════════════════════════════════════════════════════════════

### Files written by session B (independent scope)
- `evidence/checkpoints/pdf_atoms_batch_29a.jsonl`
- `evidence/checkpoints/pdf_atoms_batch_29b.jsonl`
- 任何 `pdf_atoms_batch_29<a|b>.jsonl.pre-OptionH-*.bak` (Rule B 修前 backup)
- 任何 `option_e_rerun_p<NNN>.jsonl` (若 Option E 触)
- `evidence/checkpoints/_progress_batch_29.json`
- `evidence/checkpoints/P1_batch_29_report.md`
- `evidence/checkpoints/rule_a_batch_29_sample.jsonl`
- `evidence/checkpoints/rule_a_batch_29_verdicts.jsonl`
- `evidence/checkpoints/rule_a_batch_29_summary.md`

### Files NOT touched
- root `pdf_atoms.jsonl` (post round 5 baseline = **7092** atoms — reconciler scope)
- `audit_matrix.md` (reconciler scope)
- `_progress.json` (reconciler scope)
- sister batch files `pdf_atoms_batch_30*` / `pdf_atoms_batch_31*`
- `subagent_prompts/*` (v1.3 active — no edits)
- `schema/*.json` / `PLAN.md` / `plans/*.md` / `CLAUDE.md` / `MEMORY/*`

### Final echo (single line, mandatory)
```
PARALLEL_SESSION_29_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-93,...>
```

### Brief 3-5 sentence user-facing summary (mandatory)
含: §6.3.5.10+ / §6.3.6+ scope verified + sub-batch handoff NEW7 L6 procedural enforcement (intra-batch + 新加 cross-batch from round 5 batch 28b 终态) effective/violation + reviewer slot #38 **pr-review-toolkit:code-reviewer** AUDIT pivot 19th pr family first burn verdict + carry-over to reconciler.

═══════════════════════════════════════════════════════════════════
## NEVER DO (round 6 carry-forward)
═══════════════════════════════════════════════════════════════════

- 修改 root `pdf_atoms.jsonl` / `audit_matrix.md` / `_progress.json`
- 修改 sister batch jsonl 文件
- 修改 `CLAUDE.md` / `MEMORY/*` / `PLAN.md` / `subagent_prompts/*` / `schema/*`
- 跑额外 PDF atomization beyond p.281-290 / 跑 reviewer 不在 slot #38 / 跑 drift cal (cadence skip)
- 中途回交 control / summarize / ask user — 唯一合法停止 = `PARALLEL_SESSION_29_DONE` OR `HALT_BATCH_29` echo

The boulder never stops. 第一步 STEP 0 并行 4-file Read + Pre-flight check + PDF p.4 TOC verify + p.280-290 preview.
