# Batch 23 Kickoff (Multi-Session Parallel — Session B, Round 4)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 8 STEPs (pre-flight + dispatch + schema + sweep + drift cal-skip + Rule A + findings + final message) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号是 STEP 8 echo `PARALLEL_SESSION_23_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list>` 单行 + 简短 user-facing summary.
>
> Halt-only fallback (per G-MS-4 round 2 spec): 若 unrecoverable halt → 写 `multi_session/halt_state_batch_23.md` with `recommended_fallback` field + halt 信号 `HALT_BATCH_23 reason=<X>`. 不要私自决定 abort, 由 reconciler decision tree 决定.
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel 实验 round 4 的 **session B**.
> 与 session C (batch 24) + session D (batch 25) 物理并行, 互不可见.
> 你的职责: 只跑 batch 23 (ig34 p.221-230, §6.3.5.4 GF tail + §6.3.5.5 IS head).

═══════════════════════════════════════════════════════════════════
## §0 Finding ID Range Cross-Validation Table (G-MS-13 round 3 NEW fix)
═══════════════════════════════════════════════════════════════════

**3-batch reserved finding ID ranges (round 4)**:
| Batch | Reserved range | Owner |
|---|---|---|
| **batch 23 (本 session B)** | **O-P1-67..70 (4 IDs)** | YOU — use these ONLY |
| batch 24 (sister session C) | O-P1-71..74 (4 IDs) | sister, do NOT use |
| batch 25 (sister session D) | O-P1-75..78 (4 IDs) | sister, do NOT use |

**Self-validation gate**: before finalizing `_progress_batch_23.json.findings_added`, verify each ID ∈ O-P1-67..70. If any finding has ID 71+ → STOP, you've mis-read the range, fix to O-P1-67..70 before continuing. (Round 3 batch 21 mis-read O-P1-59..62 wrote O-P1-63..66 colliding with batch 22 → reconciler had to renumber. This table prevents recurrence.)

═══════════════════════════════════════════════════════════════════
## §1 Reviewer Slot Pre-allocation (Rule D)
═══════════════════════════════════════════════════════════════════

| Item | Value |
|---|---|
| Slot # | **#32** |
| Subagent type | **`oh-my-claudecode:security-reviewer`** |
| AUDIT-mode pivot index | **13th** cumulative (post #20-#31) |
| Family | oh-my-claudecode (omc-family **6th burn** post debugger #21 + designer #23 + qa-tester #28 + test-engineer #30 + git-master #31) |
| Tools | Read / Grep / Glob / Bash (no Write — apply write-tool-less + no-Bash adaptation per round 3 batch 20 #29 plugin-dev:skill-reviewer sub-pattern OR Bash heredoc per #25 plugin-dev:plugin-validator if Bash available) |
| AUDIT pivot prompt prepend | "Mode: AUDIT for PDF atomization quality, NOT security review / NOT OWASP Top 10 / NOT secrets detection / NOT unsafe pattern detection. Audit atom_type / verbatim / parent_section / heading_fields against PDF ground truth." |

**严禁** session 自选 reviewer slot — 必须用 #32 above (避免跨 session 撞烧 Rule D + 跨 round #22-#31 撞).

If pre-assigned reviewer fails to dispatch (agent type not available), session 必须 halt 并写 `halt_state_batch_23.md`, **不要** 私自选 fallback.

═══════════════════════════════════════════════════════════════════
## §2 TOC Ground Truth (PDF p.4 verified, round 4 PRE-VERIFIED 2026-04-26)
═══════════════════════════════════════════════════════════════════

**Batch 23 page→section structure** (per PDF p.4 TOC):
- p.221-227: §6.3.5.4 Genomics Findings (GF) **body** continuing from batch 22 p.220 (GF L4 sib=4 RESTART under §6.3.5)
- p.228: §6.3.5.5 Immunogenicity Specimen Assessments (IS) **NEW sub-domain transition** (L4 sib=5 under §6.3.5)
- p.229-230: §6.3.5.5 IS body (Description / Specification head)

**§6.3.5.X deep-nesting Level Model** (round 3 NEW vs round 1+2 flat structure):
- §6.3.5 group = L3 sib=5 under §6.3 (new chapter-internal section)
- §6.3.5.X individual domains = L4 sib=1..N under §6.3.5
- 各 §6.3.5.X 的 Description / Spec / Assump / Examples = **L5** (NEW7 chain at +1 level)
- 各 §6.3.5.X.Examples N = **L6**
- Example Na/Nb sub-examples = **L7** (round 3 NEW7 L7 precedent batch 21 Example 1a/1b)

**R15 cross-batch sibling continuity (batch 22 → batch 23)**:
- §6.3.5.4 GF L4 sib=4 (already opened batch 22 p.220) — 续 GF body atoms parent=`§6.3.5.4 Genomics Findings (GF)` canonical full-form
- §6.3.5.4 GF L5 chain (Description=1 already at batch 22 p.220 a022) — 续 Specification=2 / Assumptions=3 / Examples=4 within GF body p.221-227
- §6.3.5.4 GF L6 Examples N (any Example N HEADINGs) sib=1, 2, ... RESTART under GF (independent from CP Examples chain in batches 21+22)
- §6.3.5.5 IS NEW at p.228 = L4 sib=5 under §6.3.5 (parent='§6.3.5 Specimen-based Findings Domains' L3 group canonical full-form)
- §6.3.5.5 IS L5 chain Description=1 RESTART under §6.3.5.5 IS (parent='§6.3.5.5 Immunogenicity Specimen Assessments (IS)' L4 sub-domain canonical full-form)

═══════════════════════════════════════════════════════════════════
## §3 R-Rules Cumulative (R1-R15 + O-P1-26 + NEW1-NEW8 inline, v1.2 base)
═══════════════════════════════════════════════════════════════════

### Core (R1-R15)
- R1: atom_id format `ig34_pNNNN_aNNN` (4-digit page + 3-digit per-page; pages must be 4-digit zero-padded e.g. `p0221` not `p221`)
- R2: 9-enum atom_type strict {SENTENCE, LIST_ITEM, HEADING, TABLE_HEADER, TABLE_ROW, CODE_LITERAL, FIGURE, NOTE, CROSS_REF}
- R3: HEADING vs LIST_ITEM TOC-anchored (numbered list items 1./2./3./4. inside narrative = LIST_ITEM, NOT HEADING regardless of bold formatting)
- R4: lettered list dedup (a) text. (b) text. → 2 LIST_ITEMs not 1)
- R5: TOC anchor parent_section (each atom's parent_section = closest enclosing §N.N.N from TOC ground truth)
- R6: codelist literal verbatim (CT codelist names like `(NY)`, `(ROUTE)`, `(UNIT)` etc preserved exactly as PDF, NO hallucinated CT codelist names)
- R7: output JSONL pure + DONE strict match (writer DONE atoms=N must equal actual file line count; no frame tags like `</content>` `<output>` in output)
- R8: TABLE_ROW empty cell `\| \|` literal (preserve PDF empty cells as literal pipe-space-pipe, do NOT skip)
- R9: dataset filename CODE_LITERAL physical-page parent (xx.xpt CODE_LITERAL atoms get parent_section = the physical page's enclosing §N.N.N, NOT cross-domain reference; e.g. cm.xpt on §6.1.1 AG page = parent §6.1.1 AG even though cm.xpt belongs to CM)
- R10: spec table verbatim accuracy + writer-family character-level spell-check pre-DONE (variable names like AELLT/AEPTCD must match PDF exactly char-by-char; no character-drop / extra-letter / character-swap; no whitespace normalization on cell wraps `domains.This` PDF artifact must preserve)
- R11: TABLE_ROW trailing empty cell preservation (Row 1 ZOLOFT 1×`\|\|` vs PDF 2×`\|\|\|` 10-col table → preserve all trailing empty cells)
- R12: transition page full-content discipline + ≥8 atoms expected on transition pages (3-zone partition: prior section tail + new section heading + new section content)
- R13: numbered list item discipline regardless of bold (numbered items 1./2./3./4. always LIST_ITEM, NOT HEADING — even if visually bold)
- R14: writer DONE atoms=N self-validation (writer must `wc -l output.jsonl` and verify == DONE atoms=N before final message; if mismatch, fix before reporting DONE)
- R15: cross-batch sibling_index continuity (HEADING sibling_index continues across batch boundaries per pre-prepended R15 context above)

### O-P1-26 outer-pipe convention (cumulative round 2-3)
TABLE_ROW + TABLE_HEADER must use **outer-pipe** format `\| cell1 \| cell2 \| cell3 \|` (leading + trailing pipe), NOT inner-pipe `cell1 \| cell2 \| cell3`. Apply to all TABLE_ROW + TABLE_HEADER atoms uniformly within batch.

### NEW v1.3 candidate rules (NEW1-NEW8 inline-applied pre v1.3 cut)
- **NEW1 dual-threshold drift cal** (round 2 + round 3 STRONGLY VALIDATED 2×): drift cal verdict = strict ≥80% AND verbatim hash overlap ≥80%; if either fails investigate root cause. Catches strict-PASS-hides-verbatim-divergence pattern.
- **NEW2 writer character-level self-validation** (pre-DONE): writer iterates over all extracted variable names + checks character-by-character match against PDF spec table column 1 "Variable Name". Catches Cyrillic substitutions (CPCЕЛSTA→CPCELSTA self-correct). **Limitation exposed round 3**: misses adjacent-letter swaps within Latin alphabet (CPCSMRKS→CPSCMRKS C↔S swap) — **NEW8 below addresses**.
- **NEW3 Option E rerun convention** (round 1 G-MS-5 fix): Option E rerun prompt MUST explicitly require outer-pipe + null-key for non-HEADING atoms (heading_level: null + sibling_index: null). Prevents bulk Option H post-process fix (round 1 batch 14 91-atom fix).
- **NEW4 dataset filename CODE_LITERAL strict** (vs HEADING ambiguity): xx.xpt dataset captions/filenames are CODE_LITERAL atoms NOT HEADING. (Resolves O-P1-24 INFO ambiguity batch 09.)
- **NEW5 R12 chapter-level transition strengthening**: chapter transitions (§6.x → §6.x+1) must have explicit zone partition + ≥8 atoms with prior chapter tail + new chapter HEADING + new chapter intro all preserved.
- **NEW6 parent_section dual-form codification** (round 2 G-MS-11 + round 3 G-MS-11.b extension):
  - Chapter-level (§6 / §6.2 / §6.3): `§N.N [TITLE-ALL-CAPS]` short-bracket all-caps (e.g. `§6.3 [MODELS FOR FINDINGS DOMAINS]`)
  - L3 sub-domain group (§6.3.5): `§6.3.5 Specimen-based Findings Domains` canonical full-form (no CODE)
  - L4 §6.3.5.X individual domain: `§6.3.5.X Title (CODE)` canonical full-form (e.g. `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`)
  - L5+ atom parent: same canonical full-form as L4 domain
  - **NEW6.b round 3 extension**: L4 sub-domain section-start HEADING parent = L3 group container (NOT self-parent). E.g. §6.3.5.5 IS L4 HEADING atom on p.228 parent = `§6.3.5 Specimen-based Findings Domains` (L3 group canonical), NOT `§6.3.5.5 Immunogenicity Specimen Assessments (IS)` (self-parent anti-pattern).
- **NEW7 L4-L7 deterministic chain** (round 3 deep-nesting model):
  - §6.3.5.X own L5 chain Description=1 / Specification=2 / Assumptions=3 / Examples=4 ± References=5
  - §6.3.5.X.Examples N = L6 sib=N RESTART under §6.3.5.X
  - §6.3.5.X.Example N sub-example (Na/Nb) = L7 sib=1, 2 RESTART under Example N (round 3 NEW7 L7 precedent batch 21 Example 1a/1b)
- **NEW8 substring n-gram cross-check** (round 3 NEW v1.3 candidate): post-extraction validation pass checks each `[A-Z]{3,}` candidate variable name against canonical CDISC variable list extracted from PDF spec table column 1 + cumulative root atoms. If candidate matches canonical name within Levenshtein distance 1-2 BUT differs character-by-character → flag for human review. Catches adjacent character swap (C↔S, I↔L), transposition (CSCB↔SCBC), homoglyph substitution (Latin O↔digit 0). **Apply post-DONE before final message**.

### Density alarm spec (G-MS-12 round 2 + round 3 2× validated)
- Per-page density baseline finding-domain narrative+spec page = **25-30 atoms/page** (R12 transition pages can be lower if content-driven sparse)
- Sub-batch (5 pages) density baseline = **125-150 atoms** total
- **Alarm trigger**: any single page <60% baseline (= <15 atoms/page floor) OR sub-batch <100 atoms total OR continuous 3+ pages all <20 atoms/page
- **Alarm action**: main-session PDF cross-check via `Read tool with pages: "NNN"` BEFORE Rule A dispatch:
  - If PDF cross-check shows physical content matches extracted (sparse page genuinely sparse, e.g. eg.xpt 8-row dataset only) → **FALSE POSITIVE**, no Option E rerun, document in batch report
  - If PDF cross-check shows under-extraction (multi-sentence intros collapsed, missing TABLE_ROWs, dropped narrative) → **TRUE POSITIVE**, trigger Option E executor rerun for affected page(s)

═══════════════════════════════════════════════════════════════════
## §4 STEP 0 — Pre-flight Pre-dispatch
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `subagent_prompts/P0_writer_pdf_v1.2.md` (base writer prompt)
2. `_progress_batch_22.json` (sister round 3 batch 22 _progress for cross-batch context — only `findings_added` + `rule_d_chain_post_batch` + `handoff_to_reconciler` fields needed for context, do NOT use as base for batch 23 work)
3. PDF p.4 (TOC re-verify §6.3.5.4 GF p.220 / §6.3.5.5 IS p.228 boundaries — confirmed above but re-read for safety)

Verify pre-flight:
- batch 22 status=completed in `_progress_batch_22.json` (already merged to root via reconciler eb51567, 5502 atoms / 220 pages baseline)
- root pdf_atoms.jsonl = 5502 atoms / 220 pages confirmed
- reviewer slot #32 oh-my-claudecode:security-reviewer dispatchable

任一验证失败 → halt + 写 `halt_state_batch_23.md` (do NOT proceed).

═══════════════════════════════════════════════════════════════════
## §5 STEP 1-3 — Writer Dispatch (Option C parallel + alternation)
═══════════════════════════════════════════════════════════════════

**Alternation rule** (per plans/P1_pdf_atomization.md §B.2): batch 23 = 奇 → **23a=writer + 23b=executor** (per established alternation pattern).

But: writer-family R10 verbatim drift 历史 7 batches (O-P1-23/34/36/37/38/50/63 cumulative) — round 4 recommend **continue executor-only writer pool** to minimize writer-family corruption risk on dense GF/IS spec table content. Final decision: **23a = oh-my-claudecode:writer × p.221-225** (writer-role per alternation, but writer prompt prepend NEW8 substring n-gram cross-check enforcement) + **23b = oh-my-claudecode:executor × p.226-230** (executor-role).

If writer 23a returns >5% R10 verbatim drift signal in DONE message OR density alarm fires post-DONE on multiple pages → trigger Option E executor rerun for affected pages (per round 3 batch 22 pattern).

### Sub-batch 23a writer prompt (核心)

```
Mode: PDF atomization writer per P0_writer_pdf_v1.2 + inline R10-R15 + O-P1-26 + NEW1-NEW8 (see kickoff §3 for full rules).

Scope: ig34 p.221-225 (§6.3.5.4 GF body — Genomics Findings spec table + assumptions).

TOC anchor:
- §6.3.5.4 Genomics Findings (GF) L4 sib=4 RESTART under §6.3.5 (already opened batch 22 p.220 — you continue body content)
- All atoms parent_section = `§6.3.5.4 Genomics Findings (GF)` canonical full-form (NOT self-parent for any L5 sub-section HEADING; NOT short-bracket form)
- L5 sub-section chain per NEW7: GF-Description=1 (already at batch 22 p.220 a022 — you continue from Specification=2) / GF-Specification=2 / GF-Assumptions=3 / GF-Examples=4 if reached
- L6 Example N HEADINGs (if any in this range) sib=1, 2, ... RESTART under GF (independent from CP Examples chain in batches 21-22)

Output: `evidence/checkpoints/pdf_atoms_batch_23a.jsonl` (写到此路径, NOT root pdf_atoms.jsonl)

Pre-DONE self-validation (NEW2 + NEW8):
1. Iterate all TABLE_ROW + TABLE_HEADER atoms — for each candidate variable name `[A-Z]{3,}` (e.g. GFTESTCD, GFSTRESC), verify char-by-char vs PDF p.221-225 spec table column 1
2. NEW8 substring n-gram cross-check: compute trigrams + 4-grams for each candidate; cross-check against canonical CDISC variable list (from PDF p.221-225 spec table column 1 OR cumulative root atoms via grep). Flag any candidate matching canonical within Levenshtein 1-2 but char-differing.
3. wc -l output.jsonl; verify == DONE atoms=N; fix before final message.

Final message format: DONE atoms=<N> failures=<F>
```

### Sub-batch 23b executor prompt (核心)

```
Mode: PDF atomization executor per P0_writer_pdf_v1.2 + inline R10-R15 + O-P1-26 + NEW1-NEW8 (see kickoff §3 for full rules).

Scope: ig34 p.226-230 (§6.3.5.4 GF tail p.226-227 + §6.3.5.5 IS NEW sub-domain transition at p.228 + IS Description+Specification head p.229-230).

TOC anchor:
- p.226-227: continue GF L4 chain (Examples / References if present) — same parent_section as 23a above
- p.228: §6.3.5.5 Immunogenicity Specimen Assessments (IS) NEW L4 sib=5 RESTART under §6.3.5
  - **CRITICAL NEW6.b round 3 extension**: §6.3.5.5 IS L4 HEADING atom on p.228 parent_section = `§6.3.5 Specimen-based Findings Domains` (L3 group canonical full-form, NOT self-parent — this is the round 3 batch 22 GF L4 self-parent O-P1-64 lesson codified)
- p.229-230: IS body — IS-Description L5 sib=1 + IS-Specification L5 sib=2 (head only) — parent_section = `§6.3.5.5 Immunogenicity Specimen Assessments (IS)` canonical full-form

R12 transition page p.228 (§6.3.5.4 GF → §6.3.5.5 IS): expect ≥8 atoms with 3-zone partition (GF tail + IS L4 HEADING + IS L5 Description HEADING + IS intro)

Output: `evidence/checkpoints/pdf_atoms_batch_23b.jsonl`

Final message format: DONE atoms=<N> failures=<F>
```

Dispatch BOTH in parallel via single Task message with 2 Agent calls.

═══════════════════════════════════════════════════════════════════
## §6 STEP 4 — Schema + format sweeps + density alarm + NEW6/NEW7/R12/R15 sweeps (post-DONE)
═══════════════════════════════════════════════════════════════════

After both 23a + 23b DONE, main session runs:

### Schema validation
- Python script: load 23a + 23b jsonl → verify 0 JSON parse / 0 BAD atom_type / 0 BAD atom_id / 0 frame tag / 0 within-batch dup atom_ids / 0 collision with root pdf_atoms.jsonl

### Density alarm check (G-MS-12 round 2 + round 3 spec)
- Compute per-page atom counts; if any page <15 atoms OR sub-batch <100 atoms → trigger main-session PDF cross-check via Read tool

### NEW6 parent_section dual-form sweep
- Verify chapter-form `§N.N [TITLE-ALL-CAPS]` if any chapter-parent atoms present (no chapter transitions in batch 23 expected; only sub-domain transitions)
- Verify sub-domain canonical `§N.N.N Title (CODE)` for all GF + IS atoms
- Verify L3 group canonical `§6.3.5 Specimen-based Findings Domains` for §6.3.5.5 IS L4 HEADING atom on p.228 (NEW6.b extension — this is the round 3 batch 22 lesson)
- 0 violations expected (sub-session writers prepend NEW6 dual-form spec); if violations found → Option H inline fix + Rule B backup

### NEW7 L4-L7 chain check
- §6.3.5.4 GF L5 chain post batch 22 GF Description=1 → batch 23 should have GF-Specification=2 (and possibly Assumptions=3, Examples=4, References=5)
- §6.3.5.5 IS L5 chain Description=1 RESTART under IS

### R12 transition page p.228 check
- Expect ≥8 atoms with 3-zone partition (GF tail / IS L4 HEADING / IS L5 Description HEADING + intro)

### R15 cross-batch sibling continuity
- §6.3.5.5 IS L4 sib=5 contiguous from §6.3.5.4 GF L4 sib=4 (batch 22 terminal)

═══════════════════════════════════════════════════════════════════
## §7 STEP 5 — Drift Cal SKIP per cadence
═══════════════════════════════════════════════════════════════════

Drift cal NOT mandatory batch 23 (cadence next mandatory batch 24 per every-3-batches batch 21→24 + cumulative ≥300 atoms post-p.205). Skipped.

═══════════════════════════════════════════════════════════════════
## §8 STEP 6 — Rule A 10-atom 1/page Stratified Audit
═══════════════════════════════════════════════════════════════════

### Sample design
- Seed: 20260520 (round 4 batch 23 base)
- Coverage: 1/page p.221-230 (10 atoms total, strict 1/page)
- Stratification: aim 5+ TABLE_ROW (R8/R10/R11/NEW2/NEW8 verbatim heavy) + 2-3 HEADING (NEW6.b L4 self-parent + R15 cross-batch + NEW7 deterministic chain) + 1-2 LIST_ITEM (R13 numbered list discipline) + 1 CODE_LITERAL (R9 dataset filename gf.xpt + is.xpt physical-page parent)
- Sample file: `rule_a_batch_23_sample.jsonl`

### Reviewer dispatch
- Agent: `oh-my-claudecode:security-reviewer` (slot #32, AUDIT-mode pivot 13th, omc-family 6th burn)
- Mode prepend: "Mode: AUDIT for PDF atomization quality, NOT security review / NOT OWASP Top 10 / NOT secrets detection / NOT unsafe pattern detection. Audit per-atom 4-dimension: atom_type / verbatim / parent_section / heading_fields. Compare against PDF p.221-230 ground truth."
- Tool: Read (PDF + sample.jsonl) + Grep + Glob. No Write tool — produce verdicts.jsonl + summary.md content **inline** in your response (heredoc-style or quoted blocks); main session will write files preserving your content verbatim. (Per round 3 batch 20 #29 plugin-dev:skill-reviewer write-tool-less + no-Bash sub-pattern.)
- Final message: `Rule A batch 23 weighted=<X>% PASS_n=<P> PARTIAL_n=<PA> FAIL_n=<F>`

### Threshold
≥90% effective. If raw <90% → trigger Option E rerun on affected page(s) per round 3 batch 22 pattern; effective post-rerun must reach ≥90%.

═══════════════════════════════════════════════════════════════════
## §9 STEP 7 — Findings Documentation
═══════════════════════════════════════════════════════════════════

**Finding ID range: O-P1-67..70** (per §0 cross-validation table). Reserved 4 IDs for batch 23.

For each finding (likely 0-3 expected based on round 3 trend with NEW6.b + NEW8 inline applied):
- ID: O-P1-67, O-P1-68, O-P1-69, O-P1-70 (use in order)
- Severity: HIGH / MEDIUM / LOW / INFO
- Category: writer-family / NEW6-violation / NEW7-precedent / G-MS-12 / R10 / etc
- Title + scope + atom_id(s) affected + rule_violation + repair_action + v1.4 candidate (if applicable)

**Self-validation**: verify each finding ID ∈ {O-P1-67, O-P1-68, O-P1-69, O-P1-70}. If any ID 71+ → STOP + fix.

═══════════════════════════════════════════════════════════════════
## §10 STEP 8 — Final Message + Files Written
═══════════════════════════════════════════════════════════════════

### Files written by session B (independent scope)
- `evidence/checkpoints/pdf_atoms_batch_23a.jsonl` (writer 23a output)
- `evidence/checkpoints/pdf_atoms_batch_23b.jsonl` (executor 23b output)
- `evidence/checkpoints/pdf_atoms_batch_23a.jsonl.pre-*.bak` (Rule B backups if any Option E/H)
- `evidence/checkpoints/pdf_atoms_batch_23b.jsonl.pre-*.bak` (Rule B backups if any Option E/H)
- `evidence/checkpoints/_progress_batch_23.json` (sub-progress per round 3 batch 20-22 schema + round_4_compliance section)
- `evidence/checkpoints/P1_batch_23_report.md` (full batch report)
- `evidence/checkpoints/rule_a_batch_23_sample.jsonl` + `_verdicts.jsonl` + `_summary.md`
- `evidence/checkpoints/option_e_rerun_*.jsonl` (if any Option E triggered)

### Files NOT touched (留给 reconciler — multi-session shared file off-limits)
- root `pdf_atoms.jsonl`
- `audit_matrix.md`
- `_progress.json`
- `subagent_prompts/v1.3_patch_candidates.md`
- `subagent_prompts/P0_writer_pdf_v1.2.md`
- `schema/*.json` / `PLAN.md` / `plans/*.md`
- `CLAUDE.md` / MEMORY / project meta files
- sister batch files (`pdf_atoms_batch_24*` / `pdf_atoms_batch_25*`)
- historical .bak files (preserved per Rule B)

### Final message (single line)
```
PARALLEL_SESSION_23_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<O-P1-67,O-P1-68,...>
```

User-facing summary (3-5 sentences): batch 23 contributions + GF body + IS NEW transition + NEW6.b validation + AUDIT pivot 13th + reviewer slot #32 verdict + carry-over to reconciler.

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- Write to root `pdf_atoms.jsonl` / `audit_matrix.md` / `_progress.json` (reconciler scope)
- Write to sister batch files (`pdf_atoms_batch_24*` / `pdf_atoms_batch_25*`)
- Write to `subagent_prompts/*` / `schema/*` / `PLAN.md` / `plans/*` / `CLAUDE.md` / MEMORY (frozen)
- Pick reviewer slot OTHER than #32 (Rule D cross-session collision risk)
- Use finding IDs OUTSIDE O-P1-67..70 range (G-MS-13 G-MS-7 collision risk)
- Run drift cal (cadence next mandatory batch 24, NOT batch 23)
- Auto-decide halt fallback (write `halt_state_batch_23.md` + signal HALT_BATCH_23 + let reconciler decide)

The boulder never stops. 第一步 STEP 0 并行 3-file Read + Pre-flight check.
