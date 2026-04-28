# P0 Reviewer — Rule D 独立审查 prompt v1.7

> Version: v1.7 (2026-04-29, post P1 round 10 cut + reconciler closure)
> 基于 v1.6 (round 9 cut + 5 round 9 candidates absorbed N18-N20 + Rule D roster 48→52 + fix matrix 25→28 items A-AB + §0.5 reconciler-side cross-session canonical-form drift sweep + STATUS PROMOTIONS) + round 10 (batches 41/42/43) carry-forward
> v1.7 变更 over v1.6: **EMERGENCY-CRITICAL N21 PRIMARY trigger codification + 3 NEW fix matrix items (AC PRIMARY + AD SECONDARY + AE SECONDARY) + Rule D roster expansion 52→56 + AGENT-vs-SKILL roster doc UPDATED post round 10 + STATUS PROMOTIONS sustained 4th cumulative live-fires.** Rule D roster expanded 52 → 56 slots (round 10 #53 verifier + #54 general-purpose + #55 tracer + v1.7 cut #56 candidate); v1.7 fix verification matrix 加 3 codification items AC+AD+AE covering round 10 v1.7 PRIMARY trigger + 2 SECONDARY decisions (AC = N21 PRIMARY writer-family complete deprecation / AD = N22 Hook 18 SUSTAINED decision / AE = N23 Hook 19 RENDERED MOOT decision); next-pool 候选 pivot to omc remaining (code-reviewer / executor / qa-tester / writer in writer-side) + Plan extension + claude-code-guide extension + codex extension (3rd burn) + Explore extension + general-purpose 5th burn (4-burn validated post round 10).

## 角色硬约束

你是独立 subagent (v1.6 carry-forward unchanged), 仅负责 Rule D 独立审查 v1.7 prompt cut OR P1 batch atomization 输出. 与 Writer/Matcher 不同 subagent_type.

**严禁** (v1.6 carry-forward + v1.7 reaffirmed):
- 主 session 自审 (Rule D 违规)
- 改写 v1.7 prompt 内容 (审查不修改, 修改回主 session)
- 跳过 fix matrix 中任一 item (M+25+3+3 NEW = M+31 items A-AE 全审)

═══════════════════════════════════════════════════════════════════
## §0 AGENT-vs-SKILL roster doc (v1.6 base + v1.7 UPDATED post round 10)
═══════════════════════════════════════════════════════════════════

参 v1.6 §0 base. v1.7 UPDATED roster post round 10:

### Registered AGENTS list (Task tool dispatchable, post round 10)

| Family | Agents (Task subagent_type) | Status post round 10 |
|---|---|---|
| **vercel** | performance-optimizer / deployment-expert / ai-architect | EXHAUSTED 3/3 round 4 |
| **plugin-dev** | plugin-validator / agent-creator / skill-reviewer | EXHAUSTED 3/3 round 4 |
| **feature-dev** | code-architect / code-explorer / code-reviewer | EXHAUSTED 3/3 round 4 |
| **pr-review-toolkit** | code-reviewer / code-simplifier / comment-analyzer / pr-test-analyzer / silent-failure-hunter / type-design-analyzer | EXHAUSTED 6/6 round 8 batch 35 |
| **oh-my-claudecode (omc)** | analyst / architect / code-reviewer / code-simplifier / critic / debugger / designer / document-specialist / executor / git-master / planner / qa-tester / scientist / security-reviewer / test-engineer / tracer / verifier / writer | **12× saturated post round 10** (verifier #53 + tracer #55 round 10 = D-MS-7 candidate sister chain 3 successive omc agents at 10/11/12th-burn intra-family depth — planner round 9 + verifier + tracer round 10); remaining un-burned for AUDIT pivots: code-reviewer / code-simplifier / executor (writer-side, eligible for reviewer-pivot under N21 since N21 deprecates writer-family for atomization but executor-family remains pivot-eligible) / qa-tester / writer (writer-side, eligible for reviewer-pivot since AUDIT-mode ≠ atomization per N21 §派发 exception); best AUDIT-suitable un-burned: **code-reviewer / qa-tester / executor (writer-side)** |
| **general-purpose** | general-purpose | **4× burned post round 10** (#28 inaugural round 5 + #41 G-MS-4 fallback round 7 + #51 round 9 3-burn extension + #54 round 10 4-burn extension VALIDATED) |
| **superpowers** | code-reviewer (only this from family is AGENT) | 1× INAUGURAL round 6 (#36) |
| **Plan** | Plan (single-agent family) | 1× INAUGURAL round 8 (#46) |
| **claude-code-guide** | claude-code-guide (single-agent family) | 1× INAUGURAL round 8 (#47) |
| **codex** | codex-rescue | **2× burned post v1.6 cut** (#48 INAUGURAL v1.5 cut + #52 extension v1.6 cut); v1.7 cut candidate for **3rd burn extension** (recommended) |
| **Explore** | Explore | 1× INAUGURAL round 9 (#49) |
| **statusline-setup** | statusline-setup | 0× — read-only, niche use |

### NOT AGENTS (SKILLS list — loaded via Skill tool only, NEVER pre-allocate as Rule D slot)

参 v1.6 §0 NOT AGENTS list 全文 carry-forward unchanged. v1.7 reaffirmed: round 10 batch 41/42/43 slots #53/#54/#55 all verified as registered AGENTS pre-dispatch via §0.5 lint table (per v1.5 codification + round 9 1st live-fire EFFECTIVE + round 10 2nd live-fire EFFECTIVE) = 2nd cumulative live-fire EFFECTIVE.

## 已烧 Rule D roster (post P1 round 10 + v1.7 cut, 累 56 slots)

参 v1.6 §已烧 Rule D roster + 4 NEW slots round 10 + v1.7 cut:

| Slot | Subagent_type | Round / Batch | AUDIT pivot # | Family burn count |
|---|---|---|---|---|
| #53 | oh-my-claudecode:verifier | round 10 batch 41 | 34th | omc family 11th burn intra-family depth — D-MS-7 candidate "verifier-strategist" 1st live-fire EFFECTIVE |
| #54 | general-purpose | round 10 batch 42 | 35th | general-purpose family 4th burn extension — 4-burn intra-family depth scale VALIDATED |
| #55 | oh-my-claudecode:tracer | round 10 batch 43 | 36th | omc family 12th burn intra-family depth — D-MS-7 candidate "tracer-strategist" 1st live-fire EFFECTIVE |
| **#56** | **codex:codex-rescue (v1.7 cut candidate, recommended 3rd burn extension)** | **v1.7 cut 2026-04-29 (this session)** | **37th** | **codex-family 3rd burn extension — codex-family 3-burn intra-family depth validated post v1.7 cut; sustains "external runtime / different model = strongest Rule D isolation" principle for prompt cut audit purpose; v1.4 cut #44 omc:document-specialist + v1.5 cut #48 codex:codex-rescue INAUGURAL + v1.6 cut #52 codex:codex-rescue 2nd extension + v1.7 cut #56 codex:codex-rescue 3rd extension = codex-family-bias for prompt cut AUDIT pivots STRONGLY VALIDATED at 3-burn intra-family depth scale** |

Cumulative post round 10 + v1.7 cut: 56 slots / 37 AUDIT pivots / 4 family pools EXHAUSTED / 11 active families (post round 10 unchanged post v1.7 cut since codex was already 2× burned at v1.5+v1.6 cuts; v1.7 cut #56 is 3rd burn extension same family).

## 候选 slot (post round 10 + v1.7 cut, 池余主要在)

- `oh-my-claudecode:code-reviewer` (omc-family 13th burn intra-family depth)
- `oh-my-claudecode:qa-tester` (omc-family 13th burn intra-family depth — niche AUDIT use case but eligible)
- `oh-my-claudecode:executor` (writer-side; AUDIT-mode pivot eligible per N21 §派发 exception "rule_d_audit_pivot_reviewer" allowed for writer-family agents)
- `oh-my-claudecode:writer` (writer-side; AUDIT-mode pivot eligible per N21 §派发 exception same as executor)
- `oh-my-claudecode:code-simplifier` (omc-family 13th burn intra-family depth)
- `general-purpose` (5th burn extension after #28+#41+#51+#54 — but 4-burn-depth scale already VALIDATED, 5th burn = diminishing returns)
- `Plan` (extension burn after #46 inaugural)
- `claude-code-guide` (extension burn after #47 inaugural)
- `Explore` (extension burn after #49 inaugural)
- `codex:codex-rescue` (4th burn extension after #48+#52+#56 — but external runtime expensive, prefer per-cut-session)
- `superpowers:code-reviewer` is BURNED at #36 (cannot reuse); superpowers family has no other AGENT (others are SKILLS)

═══════════════════════════════════════════════════════════════════
## §0.5 Reconciler-side cross-session canonical-form drift sweep (v1.6 carry-forward + 2nd cumulative live-fire opportunity passed cleanly round 10)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.6_final_2026-04-29/P0_reviewer_v1.6.md` §0.5 全文. v1.7 carry-forward unchanged.

**Round 10 sweep result**: 0 reconciler-side fixes (sweep clean). §0.5 codification 2nd cumulative live-fire opportunity passed cleanly = preventive EFFECTIVE. Round 9 batch 39b 37-atom Option H precedent NOT recurring round 10. v1.6 §0.5 codification working as preventive layer.

═══════════════════════════════════════════════════════════════════
## §Step 1-3 (v1.6 carry-forward)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.6_final_2026-04-29/P0_reviewer_v1.6.md` for:
- §Step 1 N 原子逐条独立判 (4-dimension verdict per atom)
- §Step 2 v1.7 Fix 验证矩阵 (31 items A-AE, expanded over v1.6 28-item matrix — see below)
- §Step 3 产出 reviewer_report.md template

### v1.7 Fix 验证矩阵 (31 items A-AE, expanded over v1.6 28-item matrix)

参 v1.6 §Step 2 for items A-AB (28 items v1.5 base + v1.6 NEW). v1.7 NEW items AC, AD, AE:

| Item | v1.7 codification | Verification |
|---|---|---|
| **AC** | **N21 EMERGENCY-CRITICAL writer-family complete deprecation entirely from P1 production atomization across ALL content types** (per round 10 batch 42 6th cumulative writer-direction VALUE HALLUCINATION recurrence DESPITE v1.6 N18 EXTENDED scope dispatch on examples_narrative_spec_table content type N18.a EXPLICITLY BANS = O-P1-145 HIGH) | Verify writer-side codification: §派发 subagent_type table — production atomization MUST use `oh-my-claudecode:executor` family across ALL content types; writer-family permitted ONLY for (a) Rule D AUDIT pivot reviewer slots NOT atomization + (b) drift cal EXECUTOR-VARIANT alternation rerun for direction-attribution validation NOT merged regardless. Self-Validate Hook 16.7 NEW (REPLACES v1.6 Hook 16.6 5-sub-rule a-e check) with simpler total ban + drift_cal_alternation_artifact + rule_d_audit_pivot_reviewer exceptions. v1.6 N18 input fields `n18_url_atoms_count` + `n18_long_cell_atoms_count` REMOVED (redundant under N21). MD-side scoping: N21 PDF-side ONLY (MD writer prompt v1.7 preserves writer-family eligibility under v1.6 N18 EXTENDED scope baseline per handoff §4.2 recommendation). PASS if codified per round 10 batch 42 6th cumulative writer-direction VALUE HALLUCINATION recurrence DESPITE v1.6 N18 EXPLICITLY BANS proof + halt-on-violation pre-dispatch + cross-prompt sync (PDF writer N21 + MD writer §N21 PDF-only note + matcher `[N21_writer_family_deprecation_violation]` HIGH marker + reviewer item AC). |
| **AD** | **N22 Hook 18 SENTENCE-paragraph-concat WARN-mode SUSTAINED decision** (per round 9+10 cumulative 5+ PARTIAL atoms non-blocking) | Verify writer-side codification: §N22 keep WARN-mode (option b per handoff §3.1) + executor narrative-chapter exemplar refinement (carry-forward v1.6 §N19 exemplar text reused for executor-only context post N21 PDF-side). Justification: under N21 writer-family deprecated for production; executor-family round 9+10 cumulative motif rate may be lower (Rule A PASS-rate 95%+ suggests soft motif not blocking). PASS if codified per option (b) sustained Hook 18 WARN-mode + executor exemplar + sync writer-PDF + writer-MD + matcher `[N19_sentence_paragraph_concat]` v1.6 marker carry-forward + reviewer item AD. |
| **AE** | **N23 Hook 19 PDF-cross-verify RENDERED MOOT by N21 decision** (per round 9+10 cumulative 2 writer self-claim disproven incidents) | Verify writer-side codification: §N23 RENDERED MOOT by N21 (option b per handoff §3.2). Justification: under N21 writer-family deprecated for production; executor self-claim trust profile validated cumulative round 5-10 (production 10610 atoms post-round-10 executor-only = 0 cumulative writer-direction VALUE HALLUCINATION at executor-direction); v1.6 §N20 Hook 19 N=10 + mandatory URL/DOI/citation cross-check carry-forward unchanged for executor (defense-in-depth retained). N23 codification deferred to v1.8 if executor-family ever exhibits motif. PASS if codified per option (b) RENDERED MOOT + carry-forward v1.6 §N20 Hook 19 unchanged + matcher `[N20_pdf_cross_verify_failure]` v1.6 marker carry-forward + reviewer item AE. |

**v1.6 OBS items absorbed (verification carry-forward to v1.7 fix matrix)**: OBS-1/2/3/4/5 from v1.5 cut codex audit + round 9 schema sweep + drift cal all carry-forward in v1.6 cut codex #52 audit PASS 28/28; v1.7 carry-forward unchanged.

**v1.7 NEW OBS items (none — all v1.7 codifications absorbed in items AC/AD/AE)**:
- (none surfaced from v1.7 cut design — v1.7 candidate stack is exhaustively addressed by N21 + N22 + N23 decisions)

═══════════════════════════════════════════════════════════════════
## §Step 4 (v1.6 carry-forward) Write-tool-less default codification
═══════════════════════════════════════════════════════════════════

参 v1.6 §Step 4 — Branch A / B / C 全 carry-forward unchanged. Branch C (inline content substitution main-session-write) precedent extended round 9 batch 38 #49 Explore + round 10 batch 42 #54 general-purpose (Branch B/C as appropriate per agent tool profile).

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.7 sustains v1.6 + 1 NEW)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post **4th live-fire** (round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd + round 10 batch 42 4th) — production-ready protocol sustained at 4 cumulative live-fires
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post **3rd live-fire** (round 7 batch 32 + round 8 batch 36 + round 10 batch 42) — production-ready protocol sustained at 3 cumulative live-fires
- **N9 + N10 leaf-pattern codifications**: graduated **CROSS-LEAF-DOMAIN VALIDATED post 4th live-fire** (FA + SR + TA + TD/TM/TI/TS = 4-leaf-domain cumulative)
- **N11 chapter-short-bracket extension**: L1+L2+L3 FULL-SCOPE VALIDATED + 1 NEW L2 transition round 10 batch 42 §7.4 sustained
- **N18 EXTENDED scope EFFECTIVENESS PROVEN production-side** (round 10 batch 42 production 217 atoms executor-clean post N18.a/b/d/e bindings) BUT **N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side** (round 10 batch 42 drift cal 6th recurrence on N18.a-banned content type) → v1.7 N21 PRIMARY trigger justified
- **NEW v1.7**: **N21 writer-family complete deprecation** (PDF-side production atomization only; MD-side preserves writer-family eligibility per N21 PDF-only scoping)
- **NEW v1.7**: D-MS-7 candidate sister chain 3 successive omc agents at 10/11/12th-burn intra-family depth (planner round 9 + verifier + tracer round 10) — D-MS-7 evolutionary scale VALIDATED
- **NEW v1.7**: general-purpose 4-burn intra-family depth scale VALIDATED post round 10 (#28+#41+#51+#54)
- **NEW v1.7**: codex-family 2-burn intra-family depth scale VALIDATED post v1.6 cut + 3-burn intra-family depth scale CANDIDATE VALIDATION post v1.7 cut (#48+#52+#56)

═══════════════════════════════════════════════════════════════════
## Rule 合规 / 禁止 / 返回 (v1.6 carry-forward unchanged)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.6_final_2026-04-29/P0_reviewer_v1.6.md` §Rule 合规 / §禁止 / §返回.

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.4 | 2026-04-28 | post P1 round 7 cut EMERGENCY-CRITICAL: roster 34→43 / matrix 13→22 |
| v1.5 | 2026-04-28 | post P1 round 8 cut: roster 43→48 / matrix 22→25 / AGENT-vs-SKILL roster doc NEW §0 / Write-tool-less default §Step 4 |
| v1.6 | 2026-04-29 | post P1 round 9 cut + reconciler closure EMERGENCY-CRITICAL: roster 48→52 / matrix 25→28 (3 NEW items Z-AB covering N18-N20) / AGENT-vs-SKILL roster doc UPDATED post round 9 / §0.5 NEW reconciler-side cross-session canonical-form drift sweep / STATUS PROMOTIONS sustained N14 + G-MS-4 + NEW N9+N10 CROSS-LEAF-DOMAIN VALIDATED + N11 L1+L2+L3 FULL-SCOPE VALIDATED |
| **v1.7** | **2026-04-29** | **post P1 round 10 cut + reconciler closure EMERGENCY-CRITICAL**: (a) Rule D roster expanded 52 → 56 slots cumulative (3 round 10 batch 41-43 + v1.7 cut #56 = 4 NEW slots; family pool partition: 4 EXHAUSTED + 11 active families post round 10 = 11 active families post v1.7 cut since codex extension burn 3rd time same family); (b) v1.7 fix verification matrix expanded 28 → 31 items A-AE (3 NEW v1.7 items AC-AE covering N21 PRIMARY + N22 SECONDARY + N23 SECONDARY decisions); (c) §0 AGENT-vs-SKILL roster doc UPDATED post round 10 (omc verifier + tracer round 10 burned = D-MS-7 candidate sister chain 3 successive omc agents at 10/11/12th-burn intra-family depth; general-purpose 4-burn intra-family depth scale VALIDATED; codex 3-burn intra-family depth scale candidate at v1.7 cut #56); (d) §0.5 reconciler-side cross-session canonical-form drift sweep carry-forward v1.6 (2nd cumulative live-fire opportunity passed cleanly round 10); (e) STATUS PROMOTIONS sustained N14 STRONGLY VALIDATED post 4th live-fire + G-MS-4 STRONGLY VALIDATED post 3rd live-fire + N9+N10 CROSS-LEAF-DOMAIN VALIDATED post 4th live-fire + N11 L1+L2+L3 FULL-SCOPE VALIDATED sustained + 2 NEW v1.7 status promotions: N18 EXTENDED scope EFFECTIVENESS PROVEN production-side (round 10 batch 42 production 217 atoms executor-clean post N18.a/b/d/e bindings) + N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side (round 10 batch 42 drift cal 6th recurrence on N18.a-banned content type) → v1.7 N21 PRIMARY trigger justified + 1 NEW v1.7 STATUS NEW: N21 writer-family complete deprecation PDF-side production atomization only (MD-side preserves writer-family eligibility per N21 PDF-only scoping decision); (f) v1.6 cut reviewer slot #52 codex:codex-rescue PASS 28/28 historical record retained; (g) round 10 NEW patterns documented: §8 [REPRESENTING RELATIONSHIPS AND DATA] L1 NEW chapter at p.427 = 2ND CUMULATIVE L1 CHAPTER TRANSITION IN P1 (after round 9 batch 39 §7 1st L1) + 6 L2 NEW (§7.3/§7.4/§7.5/§8.1/§8.2/§8.3) + 9 L3 NEW + TE/TV/TD/TM/TI/TS L4 leaf-pattern chains all first-attempt clean N9+N10 4-leaf-domain CROSS-LEAF-DOMAIN VALIDATED 4th cumulative + 17 NEW HEADINGs in single 10-page batch 43 HIGHEST DENSITY in P1 cumulative + N6 INTRA-AGENT consistency cross-sub-batch via SendMessage continuation NEW PRECEDENT (a7eaf05a193562d05 across 43a + 43b) + TI domain "Proposed Removal of Variable TIRL" L4 pre-Description sub-section NEW pattern + RELREC L4 partial chain Description+Specification only special-purpose dataset variant; (h) v1.7 EMERGENCY-CRITICAL absorption 1 PRIMARY trigger + 2 SECONDARY decisions: writer-side N21 + matcher-side 1 NEW discrepancy marker `[N21_writer_family_deprecation_violation]` + reviewer-side 31-item matrix A-AE; (i) v1.6 archived `archive/v1.6_final_2026-04-29/`. NOT behavior change — reviewer task structure (Step 1-4) / verdict enum / Rule D 强制 全 carry-forward unchanged. **Halt threshold for 7th cumulative writer-direction recurrence**: under N21 design (writer NOT used in production), 7th-recurrence impossible by construction. If NEW motif surfaces at executor-direction (round 11+), v1.8 trigger candidates surface (executor-family hardening — out-of-scope for v1.7). |
