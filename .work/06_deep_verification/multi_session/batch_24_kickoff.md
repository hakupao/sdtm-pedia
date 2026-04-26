# Batch 24 Kickoff (Multi-Session Parallel — Session C, Round 4) — DRIFT CAL MANDATORY

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 9 STEPs (pre-flight + dispatch + schema + sweep + drift cal MANDATORY + Rule A + findings + final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号是 STEP 9 echo `PARALLEL_SESSION_24_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered findings_added=<list>` 单行 + 简短 user-facing summary.
>
> Halt-only fallback (per G-MS-4 round 2 spec): 若 unrecoverable halt → 写 `multi_session/halt_state_batch_24.md` with `recommended_fallback` field + halt 信号 `HALT_BATCH_24 reason=<X>`. 不要私自决定 abort, 由 reconciler decision tree 决定.
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel 实验 round 4 的 **session C**.
> 与 session B (batch 23) + session D (batch 25) 物理并行, 互不可见.
> 你的职责: 只跑 batch 24 (ig34 p.231-240, §6.3.5.5 IS body) + **drift cal MANDATORY** per cadence.

═══════════════════════════════════════════════════════════════════
## §0 Finding ID Range Cross-Validation Table (G-MS-13 round 3 NEW fix)
═══════════════════════════════════════════════════════════════════

**3-batch reserved finding ID ranges (round 4)**:
| Batch | Reserved range | Owner |
|---|---|---|
| batch 23 (sister session B) | O-P1-67..70 (4 IDs) | sister, do NOT use |
| **batch 24 (本 session C)** | **O-P1-71..74 (4 IDs)** | YOU — use these ONLY |
| batch 25 (sister session D) | O-P1-75..78 (4 IDs) | sister, do NOT use |

**Self-validation gate**: before finalizing `_progress_batch_24.json.findings_added`, verify each ID ∈ O-P1-71..74. If any finding has ID 67-70 or 75+ → STOP, you've mis-read the range, fix to O-P1-71..74 before continuing.

═══════════════════════════════════════════════════════════════════
## §1 Reviewer Slot Pre-allocation (Rule D)
═══════════════════════════════════════════════════════════════════

| Item | Value |
|---|---|
| Slot # | **#33** |
| Subagent type | **`oh-my-claudecode:scientist`** |
| AUDIT-mode pivot index | **14th** cumulative |
| Family | oh-my-claudecode (omc-family **7th burn** post #21/23/28/30/31/32) |
| Tools | All tools except Write, Edit (no Write — apply write-tool-less + Bash adaptation; Bash heredoc preferred for verdicts.jsonl + summary.md output) |
| AUDIT pivot prompt prepend | "Mode: AUDIT for PDF atomization quality, NOT data analysis / NOT research execution / NOT scientific computing. Audit atom_type / verbatim / parent_section / heading_fields against PDF ground truth." |

**严禁** session 自选 reviewer slot — 必须用 #33 above.

═══════════════════════════════════════════════════════════════════
## §2 TOC Ground Truth (PDF p.4 verified, round 4 PRE-VERIFIED 2026-04-26)
═══════════════════════════════════════════════════════════════════

**Batch 24 page→section structure** (per PDF p.4 TOC):
- p.231-240: §6.3.5.5 Immunogenicity Specimen Assessments (IS) **body** (continues from batch 23 p.228-230 IS head; IS spans p.228-240 = 13 pages total)
- **NO chapter/sub-domain transitions in batch 24** (entirely inside §6.3.5.5 IS middle pages)
- p.241+ = §6.3.5.6 LB NEW (handled batch 25, NOT batch 24)

**§6.3.5.5 IS L5 chain expected** per NEW7:
- IS-Description = L5 sib=1 (already in batch 23 p.229)
- IS-Specification = L5 sib=2 (likely batch 23 p.230 head + batch 24 p.231-235 body)
- IS-Assumptions = L5 sib=3 (somewhere in batch 24 middle)
- IS-Examples = L5 sib=4 (likely batch 24 tail OR batch 25 head)
- IS-Examples Example N HEADINGs = L6 sib=1, 2, ... RESTART under IS

**R15 cross-batch sibling continuity (batch 23 → batch 24)**:
- §6.3.5.5 IS L4 already opened batch 23 p.228 (sib=5 under §6.3.5)
- IS L5 chain Description=1 + Specification=2 head from batch 23 → batch 24 continues Specification=2 body / Assumptions=3 / Examples=4
- All batch 24 atoms parent_section = `§6.3.5.5 Immunogenicity Specimen Assessments (IS)` canonical full-form (no chapter/sub-domain transitions)

═══════════════════════════════════════════════════════════════════
## §3 R-Rules Cumulative (R1-R15 + O-P1-26 + NEW1-NEW8 inline, v1.2 base)
═══════════════════════════════════════════════════════════════════

[Same R-rule block as batch_23_kickoff.md §3 — verbatim copy applies to all round 4 batches. Reference: see batch 23 kickoff for full text. R1-R15 + O-P1-26 outer-pipe + NEW1-NEW8 + NEW6.b L4 self-parent extension + density alarm spec all apply.]

**Brief recap critical for batch 24 IS body work**:
- NEW1 dual-threshold drift cal (this batch is mandatory drift cal target)
- NEW2 writer character-level self-validation pre-DONE
- NEW8 substring n-gram cross-check post-DONE (catches CPSCMRKS-class adjacent-letter swap that NEW2 misses)
- NEW6 sub-domain canonical full-form `§6.3.5.5 Immunogenicity Specimen Assessments (IS)` for all atoms
- NEW7 L5 chain Description=1 / Spec=2 / Assump=3 / Examples=4 (Description already in batch 23, you continue Spec/Assump/Examples)
- Density alarm spec G-MS-12 baseline 25-30 atoms/page

═══════════════════════════════════════════════════════════════════
## §4 STEP 0 — Pre-flight Pre-dispatch
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `subagent_prompts/P0_writer_pdf_v1.2.md` (base writer prompt)
2. `_progress_batch_22.json` (round 3 batch 22 _progress for cumulative atom count post-p.205 calculation — needed for drift cal cadence verification)
3. PDF p.4 (TOC re-verify §6.3.5.5 IS p.228-240 boundaries — confirmed above but re-read for safety)

Verify pre-flight:
- batch 22 status=completed in `_progress_batch_22.json` (already merged to root via reconciler eb51567, 5502 atoms / 220 pages baseline)
- root pdf_atoms.jsonl = 5502 atoms / 220 pages confirmed
- reviewer slot #33 oh-my-claudecode:scientist dispatchable
- drift cal cadence: every-3-batches batch 21→24 + cumulative atoms post-p.205 (batch 22 193 + batch 23 ~250 = ~443 ≥300) — both triggers 双触发 MANDATORY

═══════════════════════════════════════════════════════════════════
## §5 STEP 1-3 — Writer Dispatch (Option C parallel + alternation)
═══════════════════════════════════════════════════════════════════

**Alternation rule**: batch 24 = 偶 → **24a=executor + 24b=writer** (per established alternation pattern; opposite of batch 23).

But: writer-family R10 verbatim drift 历史 7 batches — round 4 recommend **24b=oh-my-claudecode:writer** per alternation but writer prompt prepend NEW8 substring n-gram cross-check enforcement. If writer 24b returns >5% R10 verbatim drift signal OR density alarm fires → trigger Option E executor rerun.

### Sub-batch 24a executor prompt (核心)

```
Mode: PDF atomization executor per P0_writer_pdf_v1.2 + inline R10-R15 + O-P1-26 + NEW1-NEW8 (see batch 23 kickoff §3 for full rules).

Scope: ig34 p.231-235 (§6.3.5.5 IS body — IS-Specification continuation + IS-Assumptions if reached).

TOC anchor:
- All atoms parent_section = `§6.3.5.5 Immunogenicity Specimen Assessments (IS)` canonical full-form (no chapter/sub-domain transitions in this range)
- L5 chain continuation: IS-Specification=2 (already opened batch 23 p.230) → continue body / IS-Assumptions=3 if reached / IS-Examples=4 if reached
- L6 Example N HEADINGs (if any): sib=1, 2, ... RESTART under IS

Output: `evidence/checkpoints/pdf_atoms_batch_24a.jsonl`

Pre-DONE self-validation (NEW2):
1. Iterate all TABLE_ROW + TABLE_HEADER atoms — verify variable names char-by-char vs PDF p.231-235 spec table column 1
2. wc -l output.jsonl; verify == DONE atoms=N

Final message format: DONE atoms=<N> failures=<F>
```

### Sub-batch 24b writer prompt (核心)

```
Mode: PDF atomization writer per P0_writer_pdf_v1.2 + inline R10-R15 + O-P1-26 + NEW1-NEW8 (see batch 23 kickoff §3 for full rules).

Scope: ig34 p.236-240 (§6.3.5.5 IS body — IS-Examples + Examples N L6 likely + IS tail).

TOC anchor:
- All atoms parent_section = `§6.3.5.5 Immunogenicity Specimen Assessments (IS)` canonical full-form
- L5 IS-Examples=4 likely opens in this range — sib=4 RESTART under IS
- L6 Example N HEADINGs: sib=1, 2, ... RESTART under IS (independent from CP/GF Examples chains)
- L7 sub-example (Example Na/Nb if present, per round 3 NEW7 L7 precedent): sib=1, 2 RESTART under Example N

Output: `evidence/checkpoints/pdf_atoms_batch_24b.jsonl`

Pre-DONE self-validation (NEW2):
1. Iterate all TABLE_ROW + TABLE_HEADER atoms — char-by-char check vs PDF p.236-240 spec table
2. NEW8 substring n-gram cross-check (per round 3 batch 21 lesson): for each `[A-Z]{3,}` candidate variable name, compute trigrams + 4-grams, cross-check against canonical CDISC variable list (PDF spec table column 1). Flag any candidate matching canonical within Levenshtein 1-2 but char-differing.
3. wc -l output.jsonl; verify == DONE atoms=N

Final message format: DONE atoms=<N> failures=<F>
```

Dispatch BOTH in parallel via single Task message with 2 Agent calls.

═══════════════════════════════════════════════════════════════════
## §6 STEP 4 — Schema + format sweeps + density alarm + sweeps (post-DONE)
═══════════════════════════════════════════════════════════════════

[Same as batch 23 kickoff §6 — schema + density alarm G-MS-12 + NEW6 + NEW7 L4-L7 chain + R12 (no chapter transitions in batch 24, only IS L5 sub-section transitions internal) + R15 cross-batch sibling continuity]

═══════════════════════════════════════════════════════════════════
## §7 STEP 5 — Drift Cal MANDATORY (NEW1 dual-threshold)
═══════════════════════════════════════════════════════════════════

| Item | Value |
|---|---|
| **Trigger** | every-3-batches cadence batch 21→24 + cumulative atoms post-p.205 (batch 22 193 + batch 23 ~250 + batch 24 ~250 ≥300 single-batch alone) — **双触发 MANDATORY** |
| **Target page** | TBD — recommend dense IS spec table page in p.232-235 range OR IS-Assumptions LIST_ITEM-heavy page (≥15 atoms threshold). **Selection criterion**: HEADING + LIST_ITEM mix OR TABLE_ROW dense data → tests both heading_fields drift AND verbatim drift. Final decision by session C based on PDF read. |
| **Methodology** | NEW1 dual-threshold (round 2 + round 3 STRONGLY VALIDATED 2× — strict count match + verbatim hash overlap, both ≥80% PASS) |

### Pair design
| Role | Subagent | Output |
|---|---|---|
| Baseline | sub-batch 24a executor (re-use existing 24a output for the target page) | `pdf_atoms_batch_24a.jsonl` filtered to target page |
| Rerun | `oh-my-claudecode:writer` (drift cal independent re-run, single page) | `drift_cal_p<NNN>_writer_rerun.jsonl` |

**Alternation rule**: 24a baseline = executor → drift cal rerun = writer (opposite family per round 2 batch 18 + round 3 batch 21 precedent).

### NEW1 dual-threshold computation
- **Strict count match**: baseline count == rerun count, ≥80% PASS
- **Verbatim hash overlap**: SHA256 of `(atom_type | verbatim)` per atom — intersection / max(baseline, rerun) ≥80% PASS
- **Overall verdict**: BOTH ≥80% = PASS. If either fails investigate root cause.

### Action matrix
- BOTH PASS + 0-1 atom drift → document as drift cal value-add (potentially 9th precedent if applicable), NO root file repair needed if baseline correct
- Strict PASS + verbatim FAIL <80% → DIRECTION REVERSED check (baseline correct vs rerun drift) → document writer-family motif finding (likely O-P1-71 HIGH)
- Strict FAIL → main-session PDF cross-check + Option E rerun consideration for affected page

### Report file
`evidence/checkpoints/drift_cal_batch_24_p<NNN>_report.md` (NEW1 dual-threshold result + root cause + action + any v1.4 candidate)

═══════════════════════════════════════════════════════════════════
## §8 STEP 6 — Rule A 10-atom 1/page Stratified Audit
═══════════════════════════════════════════════════════════════════

### Sample design
- Seed: 20260525 (round 4 batch 24 base)
- Coverage: 1/page p.231-240 (10 atoms total, strict 1/page)
- Stratification: 5 TABLE_ROW + 2-3 HEADING + 1-2 LIST_ITEM + 1 CODE_LITERAL
- Includes drift cal target page if HEADING/TABLE_ROW present

### Reviewer dispatch
- Agent: `oh-my-claudecode:scientist` (slot #33, AUDIT-mode pivot 14th, omc-family 7th burn)
- Mode prepend: "Mode: AUDIT for PDF atomization quality, NOT data analysis / NOT research / NOT scientific computing. Audit per-atom 4-dimension: atom_type / verbatim / parent_section / heading_fields. Compare against PDF p.231-240 ground truth."
- Tool: Read + Bash (Bash heredoc for verdicts.jsonl + summary.md output preferred per #25/#27 precedent)
- Final message: `Rule A batch 24 weighted=<X>% PASS_n=<P> PARTIAL_n=<PA> FAIL_n=<F>`

### Threshold
≥90% effective. Drift cal value-add 超 Rule A 9th precedent expected if NEW1 catches anything.

═══════════════════════════════════════════════════════════════════
## §9 STEP 7 — Findings Documentation
═══════════════════════════════════════════════════════════════════

**Finding ID range: O-P1-71..74** (per §0 cross-validation table). Reserved 4 IDs for batch 24.

Likely findings (drift cal MANDATORY batch + IS body domain):
- O-P1-71 HIGH: drift cal NEW1 dual-threshold result + writer-family motif (if any caught)
- O-P1-72 MEDIUM/LOW: any NEW6/NEW7 violation found
- O-P1-73-74: reserved for additional findings

**Self-validation**: verify each finding ID ∈ {O-P1-71, O-P1-72, O-P1-73, O-P1-74}. If any ID 67-70 or 75+ → STOP + fix.

═══════════════════════════════════════════════════════════════════
## §10 STEP 8 — Final Message + Files Written
═══════════════════════════════════════════════════════════════════

### Files written by session C (independent scope)
- `evidence/checkpoints/pdf_atoms_batch_24a.jsonl` (executor output)
- `evidence/checkpoints/pdf_atoms_batch_24b.jsonl` (writer output)
- `evidence/checkpoints/pdf_atoms_batch_24*.jsonl.pre-*.bak` (Rule B backups if any Option E/H)
- `evidence/checkpoints/drift_cal_p<NNN>_writer_rerun.jsonl` (drift cal rerun output)
- `evidence/checkpoints/drift_cal_batch_24_p<NNN>_report.md` (NEW1 dual-threshold report)
- `evidence/checkpoints/_progress_batch_24.json` (sub-progress + round_4_compliance)
- `evidence/checkpoints/P1_batch_24_report.md` (full batch report)
- `evidence/checkpoints/rule_a_batch_24_sample.jsonl` + `_verdicts.jsonl` + `_summary.md`
- `evidence/checkpoints/option_e_rerun_*.jsonl` (if any Option E triggered)

### Files NOT touched (留给 reconciler — multi-session shared file off-limits)
[Same as batch 23 kickoff §10 NOT-touched list — root pdf_atoms.jsonl / audit_matrix.md / _progress.json / sister batch files / subagent_prompts/* / schema/* / PLAN.md / plans/* / CLAUDE.md / MEMORY]

### Final message (single line)
```
PARALLEL_SESSION_24_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered findings_added=<O-P1-71,...>
```

User-facing summary (3-5 sentences): batch 24 contributions + IS body + drift cal NEW1 result + AUDIT pivot 14th + reviewer slot #33 verdict + carry-over to reconciler.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

[Same as batch 23 kickoff NEVER-DO list]

The boulder never stops. 第一步 STEP 0 并行 3-file Read + Pre-flight check.
