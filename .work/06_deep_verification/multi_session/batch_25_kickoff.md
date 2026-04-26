# Batch 25 Kickoff (Multi-Session Parallel — Session D, Round 4) — DOUBLE TRANSITION

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 8 STEPs (pre-flight + dispatch + schema + sweep + drift cal-skip + Rule A + findings + final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号是 STEP 8 echo `PARALLEL_SESSION_25_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list>` 单行 + 简短 user-facing summary.
>
> Halt-only fallback (per G-MS-4 round 2 spec): 若 unrecoverable halt → 写 `multi_session/halt_state_batch_25.md` with `recommended_fallback` field + halt 信号 `HALT_BATCH_25 reason=<X>`. 不要私自决定 abort, 由 reconciler decision tree 决定.
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel 实验 round 4 的 **session D**.
> 与 session B (batch 23) + session C (batch 24) 物理并行, 互不可见.
> 你的职责: 只跑 batch 25 (ig34 p.241-250, §6.3.5.6 LB NEW + §6.3.5.7 Microbiology Domains group NEW — **DOUBLE sub-domain transition**).

═══════════════════════════════════════════════════════════════════
## §0 Finding ID Range Cross-Validation Table (G-MS-13 round 3 NEW fix)
═══════════════════════════════════════════════════════════════════

**3-batch reserved finding ID ranges (round 4)**:
| Batch | Reserved range | Owner |
|---|---|---|
| batch 23 (sister session B) | O-P1-67..70 (4 IDs) | sister, do NOT use |
| batch 24 (sister session C) | O-P1-71..74 (4 IDs) | sister, do NOT use |
| **batch 25 (本 session D)** | **O-P1-75..78 (4 IDs)** | YOU — use these ONLY |

**Self-validation gate**: before finalizing `_progress_batch_25.json.findings_added`, verify each ID ∈ O-P1-75..78. If any finding has ID 67-74 → STOP, you've mis-read the range, fix to O-P1-75..78 before continuing.

═══════════════════════════════════════════════════════════════════
## §1 Reviewer Slot Pre-allocation (Rule D)
═══════════════════════════════════════════════════════════════════

| Item | Value |
|---|---|
| Slot # | **#34** |
| Subagent type | **`feature-dev:code-architect`** |
| AUDIT-mode pivot index | **15th** cumulative |
| Family | feature-dev (feature-dev family **3rd burn = pool COMPLETED** — 3rd family pool exhausted post round 4 batch 25; previously: feature-dev:code-explorer #5 + feature-dev:code-reviewer #11) |
| Tools | Glob / Grep / LS / Read / NotebookRead / WebFetch / TodoWrite / WebSearch / KillShell / BashOutput (no Write tool, no plain Bash — apply write-tool-less + no-Bash adaptation per round 3 batch 20 #29 plugin-dev:skill-reviewer sub-pattern: reviewer produces verdicts.jsonl + summary.md content **inline** in response, main session writes files preserving content verbatim) |
| AUDIT pivot prompt prepend | "Mode: AUDIT for PDF atomization quality, NOT architecture design / NOT feature blueprint / NOT codebase pattern analysis. Audit atom_type / verbatim / parent_section / heading_fields against PDF ground truth." |

**严禁** session 自选 reviewer slot — 必须用 #34 above.

═══════════════════════════════════════════════════════════════════
## §2 TOC Ground Truth (PDF p.4 verified, round 4 PRE-VERIFIED 2026-04-26)
═══════════════════════════════════════════════════════════════════

**Batch 25 page→section structure** (per PDF p.4 TOC):
- p.241: §6.3.5.6 Laboratory Test Results (LB) **NEW sub-domain transition** (L4 sib=6 under §6.3.5; LB is largest finding domain)
- p.242-247: §6.3.5.6 LB body (Description / Specification / Assumptions / Examples — 7 pages of LB content)
- p.248: §6.3.5.7 Microbiology Domains **NEW L4 group container transition** (L4 sib=7 under §6.3.5; plural "Domains" = group container similar to §6.3.5 itself but at L4 level — internal sub-domains MB/MS may use L5 sib=1, 2 within §6.3.5.7 group)
- p.249-250: §6.3.5.7 Microbiology Domains body (likely §6.3.5.7.1 Microbiology Specimen (MB) head OR generic Microbiology spec — TBD by writer based on PDF text)

**§6.3.5.X deep-nesting Level Model** (round 3 NEW for §6.3.5.X children):
- §6.3.5 group = L3 sib=5 under §6.3
- §6.3.5.X individual domains = L4 sib=1..N under §6.3.5
- 各 §6.3.5.X 的 Description / Spec / Assump / Examples = **L5** (NEW7 chain at +1 level)
- 各 §6.3.5.X.Examples N = **L6**
- Example Na/Nb sub-examples = **L7** (round 3 NEW7 L7 precedent)

**§6.3.5.7 Microbiology Domains as group container (round 4 NEW for batch 25)**:
- §6.3.5.7 itself = L4 sib=7 under §6.3.5 (parent='§6.3.5 Specimen-based Findings Domains' L3 group canonical full-form)
- IF §6.3.5.7 has internal sub-domains (e.g. §6.3.5.7.1 MB / §6.3.5.7.2 MS per TOC) → those are **L5 sib=1, 2** under §6.3.5.7 (parent='§6.3.5.7 Microbiology Domains' L4 group canonical full-form, similar pattern to §6.3.5 group)
- IF §6.3.5.7 is a generic Microbiology spec (no nested sub-domains in batch 25 page range) → continue L5 chain Description=1 / Spec=2 / Assump=3 / Examples=4 directly under §6.3.5.7
- Writer dispatch must read PDF p.248-250 text to determine actual structure

**R15 cross-batch sibling continuity (batch 24 → batch 25)**:
- §6.3.5.5 IS L4 sib=5 (already opened batch 23, body in batch 23+24) — batch 25 starts §6.3.5.6 LB sib=6 RESTART under §6.3.5
- §6.3.5.6 LB L5 chain Description=1 RESTART under §6.3.5.6 LB (canonical full-form `§6.3.5.6 Laboratory Test Results (LB)`)
- §6.3.5.7 Microbiology Domains L4 sib=7 RESTART under §6.3.5 (parent='§6.3.5 Specimen-based Findings Domains')

═══════════════════════════════════════════════════════════════════
## §3 R-Rules Cumulative (R1-R15 + O-P1-26 + NEW1-NEW8 inline, v1.2 base)
═══════════════════════════════════════════════════════════════════

[Same R-rule block as batch_23_kickoff.md §3 — verbatim copy applies. Reference: see batch 23 kickoff for full text.]

**Brief recap critical for batch 25 DOUBLE-TRANSITION work**:
- **NEW6.b round 3 extension CRITICAL**: §6.3.5.6 LB L4 HEADING atom on p.241 parent_section = `§6.3.5 Specimen-based Findings Domains` (L3 group canonical, NOT self-parent). Same for §6.3.5.7 Microbiology Domains L4 HEADING atom on p.248 parent = `§6.3.5 Specimen-based Findings Domains`. **This is the round 3 batch 22 GF L4 self-parent O-P1-64 lesson — DO NOT recur**.
- NEW6 dual-form: chapter `§N.N [TITLE-ALL-CAPS]` (no chapter transitions in batch 25; only sub-domain L4 transitions) + sub-domain canonical `§N.N.N Title (CODE)` for LB content + L4 group canonical `§6.3.5.7 Microbiology Domains` for Microbiology container content
- NEW7 L4-L7 deterministic chain
- R12 transition discipline DOUBLE: 2 sub-domain transitions in batch 25 (p.241 IS→LB + p.248 LB→Microbiology) — each must have ≥8 atoms with 3-zone partition
- NEW2 + NEW8 writer self-validation post-DONE
- Density alarm spec G-MS-12

═══════════════════════════════════════════════════════════════════
## §4 STEP 0 — Pre-flight Pre-dispatch
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `subagent_prompts/P0_writer_pdf_v1.2.md` (base writer prompt)
2. `_progress_batch_22.json` (round 3 batch 22 _progress for O-P1-64 NEW6 self-parent lesson context — applies to batch 25 LB + Microbiology L4 transitions)
3. PDF p.4 (TOC re-verify §6.3.5.5 IS p.228-240 / §6.3.5.6 LB p.241-247 / §6.3.5.7 Microbiology Domains p.248-262 boundaries — confirmed above but re-read for safety)
4. PDF p.248-250 (preview to determine §6.3.5.7 Microbiology Domains structure — group container with sub-domains OR generic spec? Affects L4-L5 chain decision)

Verify pre-flight:
- batch 22 status=completed in `_progress_batch_22.json` (already merged to root via reconciler eb51567)
- root pdf_atoms.jsonl = 5502 atoms / 220 pages confirmed
- reviewer slot #34 feature-dev:code-architect dispatchable

═══════════════════════════════════════════════════════════════════
## §5 STEP 1-3 — Writer Dispatch (Option C parallel + alternation)
═══════════════════════════════════════════════════════════════════

**Alternation rule**: batch 25 = 奇 → **25a=writer + 25b=executor** (per established alternation pattern; same as batch 23).

But writer-family R10 verbatim drift 历史 7 batches — same as batch 23, dispatch writer with NEW8 enforcement + monitor for Option E rerun trigger.

### Sub-batch 25a writer prompt (核心)

```
Mode: PDF atomization writer per P0_writer_pdf_v1.2 + inline R10-R15 + O-P1-26 + NEW1-NEW8 (see batch 23 kickoff §3 for full rules).

Scope: ig34 p.241-245 (§6.3.5.6 LB NEW sub-domain transition + LB body Description/Specification head).

TOC anchor:
- p.241: §6.3.5.6 Laboratory Test Results (LB) NEW L4 sib=6 RESTART under §6.3.5
  - **CRITICAL NEW6.b round 3 extension**: §6.3.5.6 LB L4 HEADING atom on p.241 parent_section = `§6.3.5 Specimen-based Findings Domains` (L3 group canonical full-form, NOT self-parent — this is the round 3 batch 22 GF L4 self-parent O-P1-64 lesson codified)
- p.241-245 LB body: parent_section = `§6.3.5.6 Laboratory Test Results (LB)` canonical full-form
- L5 chain: LB-Description=1 RESTART under §6.3.5.6 LB / LB-Specification=2 / continue body

R12 transition page p.241 (§6.3.5.5 IS → §6.3.5.6 LB): expect ≥8 atoms with 3-zone partition (IS tail / LB L4 HEADING / LB L5 Description HEADING + intro)

Output: `evidence/checkpoints/pdf_atoms_batch_25a.jsonl`

Pre-DONE self-validation (NEW2 + NEW8):
1. Iterate all TABLE_ROW + TABLE_HEADER atoms — char-by-char check vs PDF p.241-245 spec table column 1 (LB variable names like LBSEQ/LBTESTCD/LBORRES etc — LB is largest finding domain, lots of variables)
2. NEW8 substring n-gram cross-check: for each `[A-Z]{3,}` candidate variable name (LBxxx common prefix), compute trigrams + 4-grams, cross-check against canonical CDISC LB variable list. Flag any candidate matching canonical within Levenshtein 1-2 but char-differing.
3. Verify §6.3.5.6 LB L4 HEADING parent_section = `§6.3.5 Specimen-based Findings Domains` (NOT self-parent)
4. wc -l output.jsonl; verify == DONE atoms=N

Final message format: DONE atoms=<N> failures=<F>
```

### Sub-batch 25b executor prompt (核心)

```
Mode: PDF atomization executor per P0_writer_pdf_v1.2 + inline R10-R15 + O-P1-26 + NEW1-NEW8 (see batch 23 kickoff §3 for full rules).

Scope: ig34 p.246-250 (§6.3.5.6 LB body tail + §6.3.5.7 Microbiology Domains group NEW transition + Microbiology head).

TOC anchor:
- p.246-247: continue LB body (Assumptions / Examples likely) — parent='§6.3.5.6 Laboratory Test Results (LB)' canonical
- p.248: §6.3.5.7 Microbiology Domains NEW L4 group container transition
  - **CRITICAL NEW6.b round 3 extension**: §6.3.5.7 Microbiology Domains L4 HEADING atom on p.248 parent_section = `§6.3.5 Specimen-based Findings Domains` (L3 group canonical full-form, NOT self-parent)
  - §6.3.5.7 may be a group container (similar to §6.3.5 itself) — if internal sub-domains (e.g. §6.3.5.7.1 MB / §6.3.5.7.2 MS) are visible in p.248-250, they are L5 sib=1, 2 RESTART under §6.3.5.7 (parent='§6.3.5.7 Microbiology Domains' L4 group canonical full-form)
  - If §6.3.5.7 is a generic spec (no nested sub-domains visible in p.248-250) → L5 chain Description=1 directly under §6.3.5.7 (parent='§6.3.5.7 Microbiology Domains')
- p.249-250: §6.3.5.7 Microbiology body — read PDF text to determine structure

R12 transition page p.248 (§6.3.5.6 LB → §6.3.5.7 Microbiology Domains): expect ≥8 atoms with 3-zone partition (LB tail / §6.3.5.7 L4 HEADING / Microbiology body intro OR §6.3.5.7.1 MB head)

Output: `evidence/checkpoints/pdf_atoms_batch_25b.jsonl`

Final message format: DONE atoms=<N> failures=<F>
```

Dispatch BOTH in parallel.

═══════════════════════════════════════════════════════════════════
## §6 STEP 4 — Schema + format sweeps + density alarm + DOUBLE TRANSITION sweeps (post-DONE)
═══════════════════════════════════════════════════════════════════

[Same as batch 23 kickoff §6, plus DOUBLE TRANSITION specific:]

### NEW6.b L4 HEADING parent_section verification (CRITICAL post round 3 batch 22 lesson)
- Find §6.3.5.6 LB L4 HEADING atom on p.241 → verify parent_section = `§6.3.5 Specimen-based Findings Domains` (NOT `§6.3.5.6 Laboratory Test Results (LB)` self-parent)
- Find §6.3.5.7 Microbiology Domains L4 HEADING atom on p.248 → verify parent_section = `§6.3.5 Specimen-based Findings Domains` (NOT self-parent)
- IF either violates → Option H inline 1-atom fix + Rule B backup `pdf_atoms_batch_25*.jsonl.pre-OptionH-NEW6-<DOMAIN>-parent.bak`

### R12 transition discipline DOUBLE
- p.241 (IS→LB): ≥8 atoms with 3-zone partition
- p.248 (LB→Microbiology): ≥8 atoms with 3-zone partition

═══════════════════════════════════════════════════════════════════
## §7 STEP 5 — Drift Cal SKIP per cadence
═══════════════════════════════════════════════════════════════════

Drift cal NOT mandatory batch 25 (cadence next mandatory batch 27 per every-3-batches batch 24→27 per session 24 trigger). Skipped.

═══════════════════════════════════════════════════════════════════
## §8 STEP 6 — Rule A 10-atom 1/page Stratified Audit
═══════════════════════════════════════════════════════════════════

### Sample design
- Seed: 20260530 (round 4 batch 25 base)
- Coverage: 1/page p.241-250 (10 atoms total)
- Stratification: aim 5+ TABLE_ROW (LB spec table dense + Microbiology spec) + 3+ HEADING (NEW6.b L4 self-parent CRITICAL ×2: LB + Microbiology + NEW7 L5 chain + R12 transitions ×2) + 1 LIST_ITEM + 1 CODE_LITERAL (lb.xpt + mb.xpt if visible)

### Reviewer dispatch
- Agent: `feature-dev:code-architect` (slot #34, AUDIT-mode pivot 15th, feature-dev family 3rd burn = pool COMPLETED)
- Mode prepend: "Mode: AUDIT for PDF atomization quality, NOT architecture design / NOT feature blueprint / NOT codebase pattern analysis. Audit per-atom 4-dimension: atom_type / verbatim / parent_section / heading_fields. Compare against PDF p.241-250 ground truth. Special attention: §6.3.5.6 LB L4 HEADING parent + §6.3.5.7 Microbiology Domains L4 HEADING parent must NOT be self-parent (per round 3 batch 22 O-P1-64 lesson)."
- Tool: Read + Grep + Glob + WebFetch (no Write, no Bash — apply write-tool-less + no-Bash adaptation: produce verdicts.jsonl + summary.md content **inline** in response; main session writes files preserving content verbatim per round 3 batch 20 #29 plugin-dev:skill-reviewer sub-pattern)
- Final message: `Rule A batch 25 weighted=<X>% PASS_n=<P> PARTIAL_n=<PA> FAIL_n=<F>`

### Threshold
≥90% effective. DOUBLE-transition batch likely surfaces 1-2 NEW6.b violations OR R12 transition zone partition issues — Option H inline fix expected.

═══════════════════════════════════════════════════════════════════
## §9 STEP 7 — Findings Documentation
═══════════════════════════════════════════════════════════════════

**Finding ID range: O-P1-75..78** (per §0 cross-validation table). Reserved 4 IDs for batch 25.

Likely findings (DOUBLE-transition batch + LB largest domain + Microbiology group container):
- O-P1-75 LOW/MEDIUM: NEW6.b L4 self-parent violation (if any caught — round 3 batch 22 saw 1 violation despite explicit kickoff spec; round 4 batch 25 has 2 L4 transitions = 2× risk)
- O-P1-76 MEDIUM: Microbiology Domains group container structure interpretation (if §6.3.5.7 has internal sub-domains MB/MS, document the L5 group-of-group precedent — extends round 3 NEW7 L7 precedent)
- O-P1-77 LOW: any LB writer-family verbatim drift caught (LB largest domain = highest risk for character substitution like batch 22 O-P1-63 wide-TABLE_ROW corruption)
- O-P1-78: reserved

**Self-validation**: verify each finding ID ∈ {O-P1-75, O-P1-76, O-P1-77, O-P1-78}. If any ID 67-74 → STOP + fix.

═══════════════════════════════════════════════════════════════════
## §10 STEP 8 — Final Message + Files Written
═══════════════════════════════════════════════════════════════════

### Files written by session D (independent scope)
- `evidence/checkpoints/pdf_atoms_batch_25a.jsonl` (writer 25a output)
- `evidence/checkpoints/pdf_atoms_batch_25b.jsonl` (executor 25b output)
- `evidence/checkpoints/pdf_atoms_batch_25*.jsonl.pre-*.bak` (Rule B backups if any Option E/H — likely Option H NEW6.b LB or Microbiology parent fix)
- `evidence/checkpoints/_progress_batch_25.json` (sub-progress + round_4_compliance)
- `evidence/checkpoints/P1_batch_25_report.md` (full batch report)
- `evidence/checkpoints/rule_a_batch_25_sample.jsonl` + `_verdicts.jsonl` + `_summary.md`
- `evidence/checkpoints/option_e_rerun_*.jsonl` (if any Option E triggered)

### Files NOT touched (留给 reconciler)
[Same as batch 23 kickoff §10 NOT-touched list]

### Final message (single line)
```
PARALLEL_SESSION_25_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-75,...>
```

User-facing summary (3-5 sentences): batch 25 contributions + LB NEW + Microbiology Domains group NEW + DOUBLE transition + AUDIT pivot 15th + reviewer slot #34 verdict + carry-over to reconciler.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

[Same as batch 23 kickoff NEVER-DO list]

The boulder never stops. 第一步 STEP 0 并行 4-file Read + Pre-flight check (incl PDF p.248-250 preview).
