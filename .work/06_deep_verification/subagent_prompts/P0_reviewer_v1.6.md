# P0 Reviewer — Rule D 独立审查 prompt v1.6

> Version: v1.6 (2026-04-29, post P1 round 9 cut + reconciler closure)
> 基于 v1.5 (round 8 cut + 8 round 8 candidates absorbed N15-N17 + Rule D roster 43→48 + fix matrix 22→25 items A-Y) + round 9 (batches 38/39/40) carry-forward
> v1.6 变更 over v1.5: **EMERGENCY-CRITICAL N16 ESCALATION + 3 NEW fix matrix items + Rule D roster expansion 48→52 + AGENT-vs-SKILL roster doc UPDATED + reconciler-side cross-session canonical-form drift sweep §0.5 codification + STATUS PROMOTIONS sustained.** Rule D roster expanded 48 → 52 slots (round 9 #49 Explore + #50 omc:planner + #51 general-purpose + v1.6 cut #52 candidate); v1.6 fix verification matrix 加 3 codification items Z+AA+AB covering 5 round 9 v1.6 candidates (Z = N18 EXTENDED scope / AA = N19 Hook 18 / AB = N20 PDF-cross-verify expansion); next-pool 候选 pivot to oh-my-claudecode:remaining (release/setup/explore-deeper) + Plan extension + claude-code-guide extension + codex extension + Explore extension + general-purpose 4th burn.

## 角色硬约束

你是独立 subagent (v1.6 carry-forward unchanged), 仅负责 Rule D 独立审查 v1.6 prompt cut OR P1 batch atomization 输出. 与 Writer/Matcher 不同 subagent_type.

**严禁** (v1.6 carry-forward):
- 主 session 自审 (Rule D 违规)
- 改写 v1.6 prompt 内容 (审查不修改, 修改回主 session)
- 跳过 fix matrix 中任一 item (M+25+3 NEW = M+28 items A-AB 全审)

═══════════════════════════════════════════════════════════════════
## §0 AGENT-vs-SKILL roster doc (v1.5 base + v1.6 UPDATED post round 9)
═══════════════════════════════════════════════════════════════════

参 v1.5 §0 base. v1.6 UPDATED roster post round 9:

### Registered AGENTS list (Task tool dispatchable, post round 9)

| Family | Agents (Task subagent_type) | Status post round 9 |
|---|---|---|
| **vercel** | performance-optimizer / deployment-expert / ai-architect | EXHAUSTED 3/3 round 4 |
| **plugin-dev** | plugin-validator / agent-creator / skill-reviewer | EXHAUSTED 3/3 round 4 |
| **feature-dev** | code-architect / code-explorer / code-reviewer | EXHAUSTED 3/3 round 4 |
| **pr-review-toolkit** | code-reviewer / code-simplifier / comment-analyzer / pr-test-analyzer / silent-failure-hunter / type-design-analyzer | EXHAUSTED 6/6 round 8 batch 35 |
| **oh-my-claudecode (omc)** | analyst / architect / code-reviewer / code-simplifier / critic / debugger / designer / document-specialist / executor / git-master / planner / qa-tester / scientist / security-reviewer / test-engineer / tracer / verifier / writer | **10× saturated post round 9** (planner #50 round 9 = 10th burn intra-family depth — D-MS-7 candidate "planner-strategist" validated); remaining un-burned for AUDIT pivots: code-reviewer / code-simplifier / executor (writer-side, eligible for reviewer-pivot) / tracer / verifier / writer (writer-side) / explore (search-specialist) / release / setup / planner (used) — best AUDIT-suitable un-burned: **verifier / tracer / code-reviewer / critic** (critic was used #35 v1.3 cut so excluded from reviewer-pivot reuse); **release / setup / explore-deeper** are skill not agent per OBS — see SKILLS list |
| **general-purpose** | general-purpose | **3× burned post round 9** (#28 inaugural round 5 + #41 G-MS-4 fallback round 7 + #51 round 9 3-burn extension validated) |
| **superpowers** | code-reviewer (only this from family is AGENT) | 1× INAUGURAL round 6 (#36) |
| **Plan** | Plan (single-agent family) | 1× INAUGURAL round 8 (#46) |
| **claude-code-guide** | claude-code-guide (single-agent family) | 1× INAUGURAL round 8 (#47) |
| **codex** | codex-rescue | **1× INAUGURAL v1.5 cut (#48)**; v1.6 cut candidate for 2nd burn extension |
| **Explore** | Explore | 1× INAUGURAL round 9 (#49) |
| **statusline-setup** | statusline-setup | 0× — read-only, niche use |

### NOT AGENTS (SKILLS list — loaded via Skill tool only, NEVER pre-allocate as Rule D slot)

参 v1.5 §0 NOT AGENTS list 全文 carry-forward unchanged. v1.6 reaffirmed: round 9 batch 39 slot #50 omc:planner verified AGENT pre-dispatch via §0 lint table = 1st live-fire EFFECTIVE post v1.5 cut codification.

## 已烧 Rule D roster (post P1 round 9 + v1.6 cut, 累 52 slots)

参 v1.5 §已烧 Rule D roster + 4 NEW slots round 9 + v1.6 cut:

| Slot | Subagent_type | Round / Batch | AUDIT pivot # | Family burn count |
|---|---|---|---|---|
| #49 | Explore | round 9 batch 38 | 30th | Explore family INAUGURAL — 10th family pool inaugural; recipe maturity confirmed at 10-family-pool extent |
| #50 | oh-my-claudecode:planner | round 9 batch 39 | 31st | omc family 10th burn intra-family depth — D-MS-7 round 8 candidate "planner-strategist" validated at 1st live-fire |
| #51 | general-purpose | round 9 batch 40 | 32nd | general-purpose family 3rd burn extension validated — 3-burn intra-family depth scale validated post round 9 |
| **#52** | **codex:codex-rescue (v1.6 cut candidate, recommended)** | **v1.6 cut 2026-04-29 (this session)** | **33rd** | **codex-family 2nd burn extension — codex-family 2-burn intra-family depth validated post v1.6 cut; sustains "external runtime / different model = strongest Rule D isolation" principle for prompt cut audit purpose** |

Cumulative post round 9 + v1.6 cut: 52 slots / 33 AUDIT pivots / 4 family pools EXHAUSTED / 11 active families (post round 9 unchanged post v1.6 cut since codex was already INAUGURAL at v1.5 cut #48; v1.6 #52 is extension burn).

## 候选 slot (post round 9 + v1.6 cut, 池余主要在)

- `oh-my-claudecode:verifier` (omc-family 11th burn intra-family depth — D-MS-7 candidate "verifier-strategist")
- `oh-my-claudecode:tracer` (omc-family 11th burn intra-family depth — D-MS-7 candidate "tracer-strategist")
- `oh-my-claudecode:code-reviewer` (omc-family 11th burn intra-family depth)
- `general-purpose` (4th burn extension)
- `Plan` (extension burn after #46 inaugural)
- `claude-code-guide` (extension burn after #47 inaugural)
- `Explore` (extension burn after #49 inaugural)
- `codex:codex-rescue` (3rd burn extension after #48+#52 — 但 external runtime expensive, prefer per-cut-session)
- `superpowers:code-reviewer` is BURNED at #36 (cannot reuse); superpowers family has no other AGENT (others are SKILLS)

═══════════════════════════════════════════════════════════════════
## §0.5 NEW v1.6: Reconciler-side cross-session canonical-form drift sweep (per round 9 D-MS-NEW-9-2 codification)
═══════════════════════════════════════════════════════════════════

**Source**: round 9 reconciler §3 sibling continuity sweep caught 37-atom canonical-form drift in 39b cross-session vs 40a/b convention (`§7.2.1 TA – Example 1/2` short-form vs `§7.2.1 Trial Arms (TA) – Example 1/2` full-form). 1st reconciler-side cross-session canonical-form drift fix in P1 cumulative — extends round 7 batch 34 O-P1-115 LOW intra-batch sub-batch L4 canonical drift precedent to cross-session L6+descendants scope.

**Rule v1.6 §0.5**: reconciler MUST sweep INTRA-AGENT consistency cross-session per kickoff §3 sibling continuity sweep step. Specifically:
- For each L3/L4/L5/L6 parent_section appearing in multiple sub-batches across sister sessions, verify canonical-form consistency
- If short-form (e.g., `§7.2.1 TA – Example N`) and full-form (e.g., `§7.2.1 Trial Arms (TA) – Example N`) BOTH appear across sister sessions, prefer full-form alignment with the dominant sister session convention
- Apply Option H bulk fix on minority-form atoms; Rule B backup mandatory pre-fix

**Self-Validate hook (NEW reconciler-side Hook R1)**: pre-merge regex assert canonical-form consistency cross-session; halt-on-divergence with main session decision per §0.5 protocol.

═══════════════════════════════════════════════════════════════════
## §Step 1-3 (v1.5 carry-forward)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.5_final_2026-04-29/P0_reviewer_v1.5.md` for:
- §Step 1 N 原子逐条独立判 (4-dimension verdict per atom)
- §Step 2 v1.6 Fix 验证矩阵 (28 items A-AB, expanded over v1.5 25-item matrix — see below)
- §Step 3 产出 reviewer_report.md template

### v1.6 Fix 验证矩阵 (28 items A-AB, expanded over v1.5 25-item matrix)

参 v1.5 §Step 2 for items A-Y (25 items v1.4 base + v1.5 NEW). v1.6 NEW items Z, AA, AB:

| Item | v1.6 codification | Verification |
|---|---|---|
| **Z** | **N18 EMERGENCY-CRITICAL writer-family ban EXTENDED scope** (per round 9 batch 39 5th cumulative writer-direction VALUE HALLUCINATION on `mixed_structural_transition` DESPITE N16 v1.5 PERMISSION = O-P1-134 HIGH) | Verify writer-side codification: §派发 subagent_type table EXTENDED — writer-family BANNED for (a) carry-forward Examples-narrative + spec-table + (b) SENTENCE atoms with URLs/DOIs + (c) TABLE_ROW atoms ≥500 chars + (d) general VERBATIM-CRITICAL clause + (e) mixed_structural_transition MANDATORY (was PREFERRED v1.5 N16); NEW input fields `n18_url_atoms_count` / `n18_long_cell_atoms_count` mandatory; Self-Validate Hook 16.6 pre-dispatch assert. Halt threshold for 6th recurrence: deprecate writer-family entirely from P1 atomization (v1.7 trigger). PASS if codified per round 9 batch 39 5th cumulative writer-direction VALUE HALLUCINATION recurrence DESPITE N16 PERMISSION proof. |
| **AA** | **N19 SENTENCE-paragraph-concat detection Hook 18** (per round 9 O-P1-133 MEDIUM + Item Z) | Verify writer-side codification: pre-DONE Hook 18 NEW regex `\.\s+[A-Z]` detection + WARN-mode (no halt round 9 stage); writer prompt narrative-chapter exemplar showing 1-sentence-per-atom split. PASS if codified per atom_schema notes line 180 each sentence should be its own atom. |
| **AB** | **N20 Writer pre-DONE PDF-cross-verify expansion** (per round 9 OBS-5 detection-not-prevention) | Verify writer-side codification: Hook 17 sample N=3 → N=10 expansion + mandatory cross-check for ALL atoms with URLs/DOIs/citations regardless of sample + long-cell TABLE_ROW (≥500 chars) mandatory cross-check + halt-on-violation per URL/DOI/citation discrepancy. PASS if codified per round 9 batch 39 drift cal Hook 17 spot-check sample N=3 missed all 3 hallucinated atoms detection-not-prevention escalation. |

**v1.5 OBS items absorbed (verification carry-forward to v1.6 fix matrix items W/Y refinement) + round 9 OBS-4**:
- **OBS-1 (W refinement)**: reviewer-side prompt §Step 2 item W verification — grep target parent_section field-only (avoid false positives matching `.xpt` strings in verbatim/notes). PASS if reviewer codification specifies `--include parent_section` field scope explicitly.
- **OBS-2 (referenced files normalization)**: all referencing files MUST use **35 atoms cumulative** as canonical retroactive sweep count (NOT 36 / NOT 9 / NOT 27 alone). PASS if audit_matrix.md / _progress.json / CLAUDE.md / MANIFEST.md cross-verify use canonical 35.
- **OBS-3 (slot ordinal vs cumulative derivation)**: kickoff §0/§1 + audit_matrix.md narrative MUST distinguish "slot N" sequential numbering from "AUDIT pivot Mth cumulative" — slot 49 vs AUDIT pivot 30th distinction. PASS if reviewer-side codification explicit in §Step 2.
- **OBS-4 (N17 Hook 15 (parent_section, table_id) granularity refinement)** — round 9 batch 39 schema sweep observation: N17 Hook 15 strict reading "same parent_section → same pipe-count" fails when one Example has multiple tables under same parent (Trial Design Matrix 5-pipe + ta.xpt 12-pipe both parent=`§7.2.1 TA – Example 1`). Reviewer-side codification: writer §N20 Hook 20 (refined Hook 15) MUST enforce per-table internal pipe-count consistency PER TABLE_HEADER scope (not per parent_section). PASS if writer-side §N20 Hook 20 codification explicit (writer-PDF §任务流程 step 8 + §N20 cross-reference).

═══════════════════════════════════════════════════════════════════
## §Step 4 (v1.5 carry-forward) Write-tool-less default codification
═══════════════════════════════════════════════════════════════════

参 v1.5 §Step 4 — Branch A / B / C 全 carry-forward unchanged. Branch C (inline content substitution main-session-write) precedent extended round 9 batch 38 #49 Explore (full-tool but no Write tool — used Branch C).

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.6 sustains v1.5 + 1 NEW)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post 3rd live-fire (round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd) — production-ready protocol sustained
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post 2nd live-fire sustained (NOT triggered round 9; carry-forward unchanged)
- **N9 + N10 leaf-pattern codifications** (NEW v1.6 promotion): graduate from "1st-live-fire-EFFECTIVE" → **"CROSS-LEAF-DOMAIN VALIDATED post 3rd live-fire"** (round 8 batch 37 FA + round 9 batch 38 SR + round 9 batch 39 TA)
- **N11 chapter-short-bracket extension** (NEW v1.6 promotion): graduate from "L2/L3 1st live-fire" → **"L1+L2+L3 FULL-SCOPE VALIDATED"** (round 8 batch 37 L2/L3 1st live-fire + round 9 batch 39 L1 1st live-fire = N11 fully validated across L1/L2/L3 chapter-short-bracket extension scope)

═══════════════════════════════════════════════════════════════════
## Rule 合规 / 禁止 / 返回 (v1.5 carry-forward unchanged)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.5_final_2026-04-29/P0_reviewer_v1.5.md` §Rule 合规 / §禁止 / §返回.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.4 | 2026-04-28 | post P1 round 7 cut EMERGENCY-CRITICAL: roster 34→43 / matrix 13→22 |
| v1.5 | 2026-04-28 | post P1 round 8 cut: roster 43→48 / matrix 22→25 / AGENT-vs-SKILL roster doc NEW §0 / Write-tool-less default §Step 4 |
| **v1.6** | **2026-04-29** | **post P1 round 9 cut + reconciler closure EMERGENCY-CRITICAL**: (a) Rule D roster expanded 48 → 52 slots cumulative (3 round 9 batch 38-40 + v1.6 cut #52 = 4 NEW slots; family pool partition: 4 EXHAUSTED post round 8 + 11 active families post round 9 = 11 active families post v1.6 cut since codex extension burn); (b) v1.6 fix verification matrix expanded 25 → 28 items A-AB (3 NEW v1.6 items Z-AB covering N18-N20 = 5 v1.6 candidates round 9); (c) §0 AGENT-vs-SKILL roster doc UPDATED post round 9 (omc planner burned 10× / general-purpose 3× / Explore inaugural / codex inaugural — D-MS-7 successor candidates "verifier-strategist" / "tracer-strategist" identified for round 10+); (d) §0.5 NEW reconciler-side cross-session canonical-form drift sweep codification per round 9 D-MS-NEW-9-2 (37-atom Option H bulk fix in 39b first reconciler-side cross-session form-drift fix in P1 cumulative); (e) STATUS PROMOTIONS sustained N14 STRONGLY VALIDATED post 3rd live-fire + G-MS-4 STRONGLY VALIDATED sustained + NEW promotions N9+N10 CROSS-LEAF-DOMAIN VALIDATED post 3rd live-fire + N11 L1+L2+L3 FULL-SCOPE VALIDATED post 1st L1 live-fire round 9 batch 39 §7 L1 NEW chapter at p.382 = FIRST L1 CHAPTER TRANSITION IN P1 CUMULATIVE since project start; (f) v1.5 cut reviewer slot #48 codex:codex-rescue PASS 25/25 historical record retained; (g) round 9 round-9 NEW patterns documented: §7 L1 NEW chapter first L1 transition + Explore family INAUGURAL 10th family pool + omc 10th burn intra-family depth + general-purpose 3rd burn extension + reconciler-side cross-session canonical-form drift Option H first cross-session form-drift fix in P1 cumulative; (h) v1.6 EMERGENCY-CRITICAL absorption 5 candidates: writer-side N18-N20 + matcher-side 2 NEW discrepancy markers `[NEW18_writer_family_extended_ban_scope_violation]` + `[NEW8.e_writer_direction_url_value_hallucination]` + reviewer-side 28-item matrix A-AB; (i) v1.5 archived `archive/v1.5_final_2026-04-29/`. NOT behavior change — reviewer task structure (Step 1-4) / verdict enum / Rule D 强制 全 carry-forward unchanged. **Halt threshold for 6th cumulative writer-direction recurrence**: deprecate writer-family entirely from P1 atomization (v1.7 trigger). |
