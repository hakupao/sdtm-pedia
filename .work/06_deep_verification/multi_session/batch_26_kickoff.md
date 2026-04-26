# Batch 26 Kickoff (Multi-Session Parallel — Session B, Round 5)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 8 STEPs (pre-flight / writer dispatch / schema sweep / drift cal SKIP / Rule A / findings / final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control, 不要说 "ready for review".**
>
> 唯一合法收尾信号 = STEP 8 echo 单行 `PARALLEL_SESSION_26_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-80,...>` + 一段 3-5 句 user-facing summary.
>
> 仅 halt-only fallback (per G-MS-4 round 2 spec, 4 rounds 累计 spec-only 无 live-fire) 才允许 echo `HALT_BATCH_26 reason=<X>` + 写 `halt_state_batch_26.md`. 其他场景全 hard-stop 不可中断.
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel round 5 的 **session B (batch 26)**.
> Sister sessions = C (batch 27) + D (batch 28); 物理并行 3 终端各跑 1 batch + 1 reconciler 收尾.
> Session 之间 **绝对不通信**, 只通过 evidence/checkpoints/ 下独占文件交付; 共享 root files (pdf_atoms.jsonl / audit_matrix.md / _progress.json) **绝对不动** — 留 reconciler 串行合并.

═══════════════════════════════════════════════════════════════════
## §0 — Round 5 Finding ID Range Cross-Validation Table (G-MS-13 round 3 NEW gap fix codified)
═══════════════════════════════════════════════════════════════════

**Round 5 reserved ranges** (3 sister sessions disjoint, post round 4 last used O-P1-79):

| Session | Batch | Range | 本 batch 用 |
|---|---|---|---|
| B | 26 | **O-P1-80..83** | ✅ 本 session 唯一合法范围 |
| C | 27 | O-P1-84..87 | ❌ sister session, 不可越界 |
| D | 28 | O-P1-88..91 | ❌ sister session, 不可越界 |

**Self-validation gate** (STEP 7 强制): 任何 finding ID ≤79 OR ≥84 → STOP fix. 仅 O-P1-80/81/82/83 允许 (用 0-4 个, 未用 freed for compression).

═══════════════════════════════════════════════════════════════════
## §1 — Scope + Pre-Dispatch TOC Verification
═══════════════════════════════════════════════════════════════════

**Page range**: ig34 p.251-260 (10 pages)

**Expected sections** (per round 4 reconciler retro carry-forward):
- p.251-260: §6.3.5.7 Microbiology Domains group container 续 (likely §6.3.5.7.1 MB body Spec/Assumptions/Examples + 可能 §6.3.5.7.2 MS NEW sub-domain RESTART under §6.3.5.7)
- 触 §6.3.5.8 MI 概率低 (per CLAUDE.md key paths §6.3.5.8 MI 起 p.263 = batch 27 scope)

**MUST pre-dispatch verify** (主 session 不可省, ground truth 锁):
1. Read PDF `source/SDTMIG v3.4 (no header footer).pdf` p.4 (TOC) 验 §6.3.5.7.X sub-domain 实际页号 + §6.3.5.8 MI 实际起页 + 任何 §6.3.5.7.X.X 三级 sub-domain
2. Read PDF p.250-260 preview (5-10 atoms/page sanity) 锁:
   - p.250 末 = §6.3.5.7.1 MB Specification table 续 (round 4 batch 25 terminal)
   - p.251 起 = MB Spec table 续 OR MB-Assumptions L6 sib=3 OR §6.3.5.7.2 MS L5 sib=2 RESTART (group container internal)
3. 写 pre-dispatch TOC anchor block 加到 STEP 2 dispatch prompt (每 sub-batch 顶部)

═══════════════════════════════════════════════════════════════════
## §2 — Cumulative R-Rules + NEW Codification Carry-Forward (ROUND 5 PROCEDURAL ENFORCEMENT)
═══════════════════════════════════════════════════════════════════

### R-Rules R1-R15 + NEW1-NEW8 Codification

**v1.3 cut completed 2026-04-27** — 13 codification items (A-M: R1-R15 + O-P1-26 + NEW1-NEW8 + NEW6/NEW6.b dual-form L4 self-parent + NEW7 chain + NEW7 L4 group-container branch + NEW8.b SENTENCE-trigram + NEW8.c TABLE_HEADER column-set + G-MS-12 density + G-MS-12.a content-type-aware floor + G-MS-13 cross-validation table cross-reference) all codified inline in `subagent_prompts/P0_writer_pdf_v1.3.md`. Each sub-batch dispatch prompt MUST inline-prepend the v1.3 prompt body (no need to repeat individual R-rule + NEW item details in this kickoff).

See `subagent_prompts/P0_writer_pdf_v1.3.md` §CODIFIED R-RULES + NEW (v1.3 retire inline-prepend) for full details A-M.

### 🔴 NEW7 L6 Sub-Batch Handoff (PROCEDURAL ENFORCEMENT — ROUND 5 MANDATORY)

Round 3 batch 23 + round 4 batch 25 = 2 occurrences of same NEW7 L6 cross-sub-batch HEADING continuity drift:
- Sub-batch B 写手没看到 sub-batch A 的 L5/L6 sib state → 'Example N' 默认 SENTENCE (而非 HEADING hl=6) + L5 sib counter 错重启

**Round 5 fix (procedural)**: 主 session **必须** 在 dispatch sub-batch B prompt 时 inline-prepend prior sub-batch A 的 L5/L6 chain 终态:
```
PRIOR SUB-BATCH A HEADING STATE (sub-batch B MUST continue, NOT restart):
- Last L5 sib used: <N> (e.g. §6.3.5.X-Examples sib=4)
- Last L6 Example sib used: <M> (e.g. Example 5 hl=6 sib=5)
- Convention: Example N+1 = HEADING hl=6 sib=M+1 (ALWAYS, NEVER SENTENCE)
- §6.3.5.X.Examples HEADING ALWAYS hl=5 sib=4
```

无 prior state 推断 = 视为 R15 + NEW7 procedural violation, 必须 Option H 修.

### G-MS-12 Density Alarm Threshold
- Per-page floor 15 atoms (list-only sub-rule v1.4 candidate floor=8)
- Per-sub-batch floor 100 atoms
- Alarm fires → 主 session PDF cross-check (Read tool `pages: "<N>"`) + adjudicate FALSE POSITIVE vs TRUE POSITIVE → Option E iff TRUE POSITIVE
- Round 4 reaffirm: 3rd FALSE POSITIVE precedent (batch 24 p.232 list-only)

### G-MS-13 Finding ID Range Cross-Validation
- §0 cross-validation table at top of kickoff (3-batch range table)
- Self-validation gate at STEP 7 (any ID outside reserved range → STOP fix)
- Round 4 EFFECTIVE (0 mis-allocation across 3 sister sessions)

═══════════════════════════════════════════════════════════════════
## §3 — STEP 0 Pre-Flight + R-Rules Pre-Dispatch
═══════════════════════════════════════════════════════════════════

### STEP 0.1 Read necessary files (并行 Read)
1. `multi_session/MULTI_SESSION_PROTOCOL.md` (master)
2. `multi_session/MULTI_SESSION_RETRO_ROUND_4.md` (round 4 retro)
3. `subagent_prompts/P0_writer_pdf_v1.3.md` (writer/executor R-rule block — v1.3 cut 2026-04-27, 13 items A-M codified inline)
4. `evidence/checkpoints/_progress_batch_25.json` (round 4 batch 25 terminal state for R15 carry)

### STEP 0.2 Pre-dispatch verify
- root `pdf_atoms.jsonl` line count == 6146 (post round 4 reconciler merge baseline)
- `_progress_batch_25.json` status == "completed"
- PDF p.4 TOC re-verified for §6.3.5.7.X sub-domain page ranges
- PDF p.250-260 preview verified for batch 26 actual content
- Reviewer slot #35 oh-my-claudecode:analyst dispatchable (agent appears in agent list, Tools include Read/Grep/Glob/WebFetch but NO Write)

### STEP 0.3 Pre-Flight Gate PASS
任一不通过 → halt + 报告 `HALT_BATCH_26 reason=<X>`. **不要** 私自 fix.

═══════════════════════════════════════════════════════════════════
## §4 — STEP 1-3 Writer Dispatch
═══════════════════════════════════════════════════════════════════

### Sub-batch split strategy
- 26a = oh-my-claudecode:writer × p.251-255 (5 pages, dense Spec table OR Assumptions/Examples 续)
- 26b = oh-my-claudecode:executor × p.256-260 (5 pages, 续接 26a; if §6.3.5.7.2 MS NEW sub-domain visible at this scope, 26b 必须看到 26a L5/L6 chain 终态 — NEW7 L6 procedural handoff prepend mandatory)

### Dispatch protocol
1. 主 session 并行 dispatch 2 Agent calls (single message, 2 tool uses) — 26a writer + 26b executor
2. Each agent prompt MUST include:
   - HARD-STOP DIRECTIVE (sub-agent context only — return DONE single line atoms=N failures=F not user-facing)
   - Full R-rules R1-R15 block
   - NEW1-NEW8 + NEW6/NEW6.b dual-form spec
   - **NEW7 L6 procedural handoff prepend** (26b only — 26a 终态 echo'd into 26b prompt; for 26a alone, prior sub-batch is round 4 batch 25b 终态 = `§6.3.5.7.1 MB L6 last sib=2 (Specification)`)
   - Density alarm threshold spec
   - G-MS-13 finding ID range note (no findings written by writer/executor; reviewer + main session reserve)
   - Output: append-mode JSONL to `evidence/checkpoints/pdf_atoms_batch_26<a|b>.jsonl`
   - Final DONE line single-line `DONE atoms=N failures=F`
3. 验 26a + 26b 终 DONE; wc -l 各 jsonl 与 atoms=N 匹配; 0 schema err

═══════════════════════════════════════════════════════════════════
## §5 — STEP 4 Schema + Format Sweeps
═══════════════════════════════════════════════════════════════════

Python integrity sweep (执行后写 `_progress_batch_26.json` step_4_sweeps 字段):
1. **0 JSON parse errors** + 0 BAD atom_type (∈ 9-enum) + 0 BAD atom_id (4-digit `_aXXX_`) + 0 frame tag in verbatim + 0 within-batch dup atom_ids + 0 collision with root pdf_atoms.jsonl
2. **Density alarm check** per-page; if any page <15 atoms OR sub-batch <100 atoms → 主 session PDF cross-check (Read pages) + 判 FALSE/TRUE POSITIVE
3. **NEW6 dual-form sweep** + **NEW6.b L4 self-parent** sweep (any L4 §6.3.5.7.X HEADING parent must = `§6.3.5 Specimen-based Findings Domains` if §6.3.5.7.2 MS appears as L4-style; OR parent = `§6.3.5.7 Microbiology Domains` if as group container internal L5)
4. **NEW7 chain check**:
   - §6.3.5.7.1 MB L6 chain continuity (round 4 terminal sib=2 → batch 26 sib=3 Assumptions / sib=4 Examples)
   - L7 Examples within MB if visible
   - §6.3.5.7.2 MS L5 sib=2 RESTART under §6.3.5.7 (if NEW visible)
5. **R12 transition page sweep** (if §6.3.5.7.2 MS NEW transition visible — ≥8 atoms 3-zone partition)
6. **R15 cross-batch sibling check** with batch 25 terminal: §6.3.5.7.1 MB L6 sib=2 → batch 26 sib=3 contiguous
7. Any violation → Option H inline + Rule B backup (`pdf_atoms_batch_26<a|b>.jsonl.pre-OptionH-<reason>.bak`)

═══════════════════════════════════════════════════════════════════
## §6 — STEP 5 Drift Cal SKIP per Cadence
═══════════════════════════════════════════════════════════════════

- 不触发 (per cadence: 上次 batch 24 p.233, next mandatory batch 27 = sister session C scope)
- 写 `_progress_batch_26.json` drift_cal: triggered=false, next_mandatory="batch 27"

═══════════════════════════════════════════════════════════════════
## §7 — STEP 6 Rule A 10-Atom Audit (slot #35 oh-my-claudecode:analyst, AUDIT pivot 16th, omc-family 8th burn)
═══════════════════════════════════════════════════════════════════

### Rule A sample build
- Sample size: 10 atoms (1/page p.251-260 stratified)
- Seed: 20260601 (round 5 deterministic)
- Stratification target: 4-5 TABLE_ROW + 2-3 HEADING (含 §6.3.5.7.2 MS L5 RESTART 如可见 + L6 sub-section transitions) + 1-2 LIST_ITEM + 1 CODE_LITERAL/TABLE_HEADER
- Output: `evidence/checkpoints/rule_a_batch_26_sample.jsonl`

### Reviewer dispatch — slot #35 oh-my-claudecode:analyst
- AUDIT-mode pivot 16th, omc-family 8th burn (post round 4 #33 scientist 7th)
- Tools: All except Write/Edit (write-tool-less + Bash heredoc adaptation per round 4 #32/#33 sub-pattern)
- **AUDIT-mode prepend** (强调禁止默认 mode):
  ```
  Mode: AUDIT for PDF atomization quality, NOT requirements analysis / NOT pre-planning consultation / NOT user story decomposition.
  Task: 10-atom Rule A reviewer for SDTM PDF atom verification against PDF p.251-260 ground truth.
  Adaptation: write-tool-less + Bash heredoc — produce verdicts.jsonl + summary.md inline; main session writes files preserving content verbatim.
  ```
- 反馈: per-atom 4-dimension verdict (atom_type / verbatim / parent_section / heading_fields) + summary.md inline
- Final reviewer message: `Rule A batch 26 weighted=<X>% PASS_n=<P> PARTIAL_n=<PA> FAIL_n=<F>`
- Effective threshold: ≥90% (raw or post-Option-E rerun)

### Output files
- `evidence/checkpoints/rule_a_batch_26_verdicts.jsonl` (main session writes verbatim from reviewer inline)
- `evidence/checkpoints/rule_a_batch_26_summary.md` (main session writes verbatim)

═══════════════════════════════════════════════════════════════════
## §8 — STEP 7 Findings Documentation (G-MS-13 self-validation gate)
═══════════════════════════════════════════════════════════════════

### Allowed range
**O-P1-80, O-P1-81, O-P1-82, O-P1-83** (4 reserved, 0-4 used; unused freed for compression).

### Self-validation gate
After drafting findings_added array in `_progress_batch_26.json`, verify each finding_id:
- ∈ {O-P1-80, O-P1-81, O-P1-82, O-P1-83} → PASS
- ≤79 (collide with prior cumulative) → STOP renumber
- ≥84 (collide with sister batch 27 O-P1-84..87 or batch 28 O-P1-88..91) → STOP renumber

### Each finding 字段
ID + Severity + Category + Title + Scope + atom_id(s) affected + rule_violation + repair_action + v1.3/v1.4_candidate (if applicable) + writer_family_motif (if applicable, joining cumulative O-P1-23/34/36/37/38/50/63/71 wide-table family)

═══════════════════════════════════════════════════════════════════
## §9 — STEP 8 Final Message + Files Written
═══════════════════════════════════════════════════════════════════

### Files written by session B (independent scope)
- `evidence/checkpoints/pdf_atoms_batch_26a.jsonl`
- `evidence/checkpoints/pdf_atoms_batch_26b.jsonl`
- 任何 `pdf_atoms_batch_26<a|b>.jsonl.pre-OptionH-*.bak` (Rule B 修前 backup)
- 任何 `option_e_rerun_p<NNN>.jsonl` (若 Option E 触)
- `evidence/checkpoints/_progress_batch_26.json`
- `evidence/checkpoints/P1_batch_26_report.md`
- `evidence/checkpoints/rule_a_batch_26_sample.jsonl`
- `evidence/checkpoints/rule_a_batch_26_verdicts.jsonl`
- `evidence/checkpoints/rule_a_batch_26_summary.md`

### Files NOT touched
- root `pdf_atoms.jsonl` (5502 + 226 + 208 + 210 = 6146 atoms unchanged — reconciler scope)
- `audit_matrix.md` (reconciler scope)
- `_progress.json` (reconciler scope)
- sister batch files `pdf_atoms_batch_27*` / `pdf_atoms_batch_28*`
- `subagent_prompts/*` (v1.3 cut DEFERRED 4th — defer per Rule D)
- `schema/*.json` / `PLAN.md` / `plans/*.md` / `CLAUDE.md` / `MEMORY/*`

### Final echo (single line, mandatory)
```
PARALLEL_SESSION_26_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-80,...>
```

### Brief 3-5 sentence user-facing summary (mandatory)
含: §6.3.5.7.X scope verified + sub-batch handoff NEW7 L6 procedural enforcement effective/violation + reviewer slot #35 omc:analyst AUDIT pivot 16th verdict + carry-over to reconciler.

═══════════════════════════════════════════════════════════════════
## NEVER DO (round 5 carry-forward)
═══════════════════════════════════════════════════════════════════

- 修改 root `pdf_atoms.jsonl` / `audit_matrix.md` / `_progress.json`
- 修改 sister batch jsonl 文件
- 修改 `CLAUDE.md` / `MEMORY/*` / `PLAN.md` / `subagent_prompts/*` / `schema/*`
- 跑额外 PDF atomization beyond p.251-260 / 跑 reviewer 不在 slot #35 / 跑 drift cal (cadence skip)
- 中途回交 control / summarize / ask user — 唯一合法停止 = `PARALLEL_SESSION_26_DONE` OR `HALT_BATCH_26` echo

The boulder never stops. 第一步 STEP 0 并行 4-file Read + Pre-flight check + PDF p.4 TOC verify + p.250-260 preview.
