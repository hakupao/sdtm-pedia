# Multi-Session Parallel Round 4 Retrospective (batches 23/24/25)

> Created: 2026-04-26 (reconciler session E, post 3 sister sessions B/C/D PARALLEL_SESSION_NN_DONE)
> Strategy: 方案 B 物理并行 (3 终端各跑 1 batch + 1 reconciler 收尾)
> Authorship: Rule C 强制 — 三段式 (保留 / 缺口 / 决策)
> Carry-forward: Rounds 1+2+3 retro patterns extended; round 4 surfaces 3 reaffirms + 2 recurrences + 1 NEW pattern

## Round 4 Headline Metrics

| Metric | Round 1 | Round 2 | Round 3 | **Round 4** |
|---|---|---|---|---|
| Sister sessions | 3 (B/C/D) | 3 | 3 | **3** |
| Wall savings vs serial | ~50% | ~52% | ~50% | **~50%** (sustained 4th round) |
| Atoms contributed | ~750 | ~601 | 608 | **644** (226+208+210) |
| Pages added | 30 (p.121-150) | 30 (p.161-190) | 30 (p.191-220) | **30** (p.221-250) |
| In-batch repair cycles | varies | 5 | 4 | **3** (batch 23 +1 / batch 24 +2 / batch 25 +0) |
| Reconciler-side fixes | 0 | 5 | 0 + 1 metadata renumber | **4 atoms (batch 25b NEW7 L6 LB-Examples)** |
| Cross-round Rule D collision | 0 | 0 | 0 | **0** (4 rounds clean) |
| AUDIT-mode pivots | +3 (#22-#24) | +3 (#26-#28) | +3 (#29-#31) | **+3 (#32-#34)** |
| Family pools EXHAUSTED post-round | 0 | 1 (vercel) | 2 (+plugin-dev) | **3 (+feature-dev)** |
| TOC anchor n cumulative | 70 | 110 | 140 | **170** |
| Consecutive batches anchored | 5 | 11 | 14 | **17** |
| Drift cal NEW1 dual-threshold validations | n/a | 1st | 2nd | **4th** (round 1+2+3+4) |
| G-MS-4 halt fallback live-fire | n/a | NOT triggered | NOT triggered | **NOT triggered** (4 rounds spec-only) |
| G-MS-13 cross-validation table | n/a | n/a | NEW gap surfaced | **EFFECTIVE** (0 mis-allocation) |
| NEW7 L6 sub-batch context drift | n/a | n/a | 1× (batch 23 GF Examples 4-5) | **2× cumulative** (round 4 batch 25 LB Examples 1-3 = recurrence formal codification mandatory) |

## Per-Batch Breakdown

### Batch 23 (Session B Round 4, p.221-230)
- 23a oh-my-claudecode:executor 107 atoms (GF Specification middle + Assumptions + Examples + Examples 1-3 L6)
- 23b oh-my-claudecode:executor 119 atoms (sub-split 23b_i 76 + 23b_ii 43 due to 32K output cap; GF Examples 4-5 + IS L4 transition + IS-Description + IS-Specification head)
- Repair: Option H NEW7 L6 GF Examples 4-5 hl=5→6 cross-sub-batch context drift fix (2 atoms)
- Rule A #32 oh-my-claudecode:security-reviewer (AUDIT pivot 13th, omc-family 6th burn) raw 95% PASS (1 PARTIAL)
- Findings: O-P1-67 LOW (R10 narrow-scope GFTSTDTL+GRCh38) + O-P1-68 LOW (NEW7 L6 cross-sub-batch context drift; v1.4 codification candidate) + O-P1-69 INFO (NEW6.b proactive EFFECTIVE first precedent — IS L4 first-attempt correct)
- G-MS-13 cross-validation table at top of kickoff EFFECTIVE (no sister-session mis-read)

### Batch 24 (Session C Round 4, p.231-240)
- 24a oh-my-claudecode:executor 118 atoms (IS-Assumptions + IS-Examples + Examples 1-5 L6)
- 24b oh-my-claudecode:writer pre-Option-E 113 → executor post-Option-E 90 atoms (IS Examples 6-11 L6 + Spec table tail; Option E -23 atoms duplicate-hallucinated TABLE_HEADER columns removed)
- Repair: Option H R15 Examples 6-11 sib renumber + Option E p.236-240 wholesale rerun
- Rule A #33 oh-my-claudecode:scientist (AUDIT pivot 14th, omc-family 7th burn) raw 90% PASS_AT_THRESHOLD (1 FAIL = O-P1-74 reconciler-deferred)
- Drift cal MANDATORY p.233 NEW1 dual-threshold strict 94.1% PASS / verbatim 41.2% FAIL → overall FAIL (DIRECTION REVERSED 8th + value-add 9th precedent)
- Writer-family wide-TABLE_HEADER 8th batch corruption (joins O-P1-23/34/36/37/38/50/63)
- Findings: O-P1-71 HIGH (writer-family 8th cumulative) + O-P1-72 MEDIUM (drift cal verbatim FAIL paraphrase; v1.4 NEW8.b SENTENCE-trigram) + O-P1-73 LOW (G-MS-12 density 3rd FALSE POSITIVE; v1.4 G-MS-12.a content-type-aware floor) + O-P1-74 INFO (TABLE_HEADER column-set; v1.4 NEW8.c)

### Batch 25 (Session D Round 4, p.241-250)
- 25a oh-my-claudecode:writer 100 atoms (LB L4 transition + LB-Description + LB-Specification head + LB-Assumptions head)
- 25b oh-my-claudecode:executor 110 atoms (LB-Examples + Examples 1-3 + Microbiology Domains L4 + MB L5 + MB-Description + MB-Specification head)
- In-batch repair cycles: 0
- Rule A #34 feature-dev:code-architect (AUDIT pivot 15th, feature-dev family 3rd burn = pool COMPLETED) raw 100% PASS
- DOUBLE sub-domain transition: §6.3.5.5 IS → §6.3.5.6 LB at p.241 + §6.3.5.6 LB → §6.3.5.7 Microbiology Domains group container at p.248; both NEW6.b L3-group-parent first-attempt correct
- NEW round-4 L5 sub-domain RESTART under L4 group container precedent: §6.3.5.7.1 MB L5 sib=1 RESTART under §6.3.5.7
- Findings: O-P1-75 INFO (NEW round-4 L5 RESTART precedent; v1.4 codify NEW7 L4 group-container branch)

### Reconciler Session E (post B+C+D DONE)
- Sibling continuity sweep caught 1 systematic block in batch 25b: NEW7 L6 LB-Examples sub-batch context drift (4 atoms — 'LB – Examples' hl=6 sib=3 → hl=5 sib=4 + 'Example 1/2/3' SENTENCE → HEADING hl=6 sib=1/2/3); reconciler-side Option H + Rule B backup
- Finding: O-P1-79 LOW (NEW7 L6 sub-batch context drift recurrence batch 25b; **2nd recurrence of round 3 batch 23 O-P1-68 motif** — formal v1.3+ codification mandatory)
- Sequential merge: 5502 → 6146 atoms / 220 → 250 pages / 22 → 25 batches; 0 schema err / 0 atom_id collision / pages 1-250 unique

---

## §1 保留下来的做法 (Round 4 Reaffirmed/Extended)

### R-MS-1 round 4: Multi-session parallel pattern saturated (4 rounds running)
~50% wall savings replicated 4th consecutive round (round 1 ~50% / round 2 ~52% / round 3 ~50% / round 4 ~50%). Pattern is SATURATED + STABLE; recommend Tier 3 default eligibility for independent dense batches.

**Why retain**: 4 rounds × ~50% × 30-page batches = ~6 hours wall savings cumulative; replicable at constant cost; no protocol degradation across rounds.

**How to apply**: Reuse multi_session/MULTI_SESSION_PROTOCOL.md template + write 3 batch_NN_kickoff.md + 1 reconciler_kickoff_round_X.md before each round; pre-allocate Rule D slots (avoid cross-batch + cross-round collisions); pre-allocate G-MS-7 finding ID ranges; embed G-MS-13 cross-validation table at top of each kickoff.

### R-MS-2 round 4: Rule D pool partition cross-round zero-collision (4 rounds clean)
Round 1 #22-#24 + batch 16 #25 + Round 2 #26-#28 + Round 3 #29-#31 + **Round 4 #32-#34** = 0 cross-round collision through 4 rounds (15 multi-session slots + 15 single-session slots prior).

**Why retain**: Rule D writer/reviewer isolation requires zero-collision pool partition; 4-round zero-collision proves the pre-allocation methodology scales.

**How to apply**: Each round reconciler enumerates prior #N slots in retro; round X+1 kickoff allocates next 3 slots from disjoint family branches (4 families pr/omc/vercel/plugin-dev/feature-dev → 5 families counting feature-dev added round 4; round 5 must pivot to data/firecrawl/superpowers families).

### R-MS-3 round 4: TOC anchor methodology n=170 cumulative locked (17 consecutive batches across 4 families)
0 FP / 0 inversion sustained from n=40 (batch 09-12 lock) → n=70 (round 1) → n=110 (round 2) → n=140 (round 3) → **n=170 round 4**. 4 family pools (3 EXHAUSTED + omc 7×) confirms anchor methodology is family-agnostic.

**Why retain**: 4-round 0 FP / 0 inversion proves PDF p.4 TOC ground truth pre-dispatch verification eliminates parent_section ambiguity at scale.

**How to apply**: Continue main-session pre-dispatch PDF p.4 TOC verification + prepend TOC anchor section + R-rules to each kickoff; n now sufficient for any future agent family pivot.

### R-MS-4 round 4: NEW6/NEW6.b dual-form codification + L4 self-parent extension EFFECTIVE proactively (round 3 G-MS-11.b extension validated round 4)
3 L4 sub-domain section-start HEADINGs in round 4 (IS p.228 batch 23 + LB p.241 batch 25 + Microbiology Domains p.248 batch 25) ALL first-attempt correct (parent_section=`§6.3.5 Specimen-based Findings Domains` L3 group, NOT self-parent). Vs round 3 batch 22 GF L4 1 violation (post-detection Option H O-P1-64).

**Why retain**: Round 3 G-MS-11.b extension codification flowing into round 4 kickoff prepend is generating correct L4 sub-domain section-start HEADING parent semantics in writer/executor agents AT FIRST ATTEMPT. Validates positive feedback loop: round-3 finding → spec extension → round-4 proactive correctness.

**How to apply**: Continue NEW6.b spec text in kickoff prepend until v1.3 cut; v1.3+ codification must include NEW6.b L4 self-parent rule explicitly.

### R-MS-5 round 4: Density alarm threshold (G-MS-12) 3rd FALSE POSITIVE precedent + content-type-aware sub-rule v1.4 candidate
Round 4 batch 24 p.232 14 atoms <15 floor = list-only page genuinely sparse (IS-Assumptions LIST_ITEM continuation + lettered sub-items). 3rd FALSE POSITIVE precedent (round 3 batch 20 p.192 sparse eg.xpt + round 4 batch 24 p.232 list-only).

**Why retain**: G-MS-12 main-session adjudication via PDF cross-check correctly distinguishes content-type sparseness from writer-family under-extraction. Spec functioning as designed across 4 rounds.

**How to apply**: Continue density alarm + main-session PDF cross-check protocol; v1.4 codification candidate G-MS-12.a content-type-aware sub-rule (list-only floor=8 / spec-table floor=15 / transition floor=8).

### R-MS-6 round 4: NEW1 dual-threshold drift cal STRONGLY VALIDATED 4th time (round 1+2+3+4)
Round 4 batch 24 p.233: strict 94.1% PASS / verbatim 41.2% FAIL — caught writer-family SENTENCE/LIST_ITEM paraphrase drift ('illustrate'→'distinguish' + wholesale re-summarization + whitespace normalization) that strict count alone would miss. DIRECTION REVERSED 8th precedent + drift cal value-add 9th precedent.

**Why retain**: 4 rounds × 100% validation rate (4/4 drift cals where dual-threshold spec applied) proves NEW1 design correctness. Verbatim hash overlap is mandatory companion to strict count.

**How to apply**: NEW1 dual-threshold mandatory in v1.3 cut codification; verbatim hash overlap target ≥80% paired with strict count ≥80%.

### R-MS-7 round 4: NEW8 substring n-gram cross-check caught writer-family char drifts (round 3 NEW + round 4 8th batch corruption)
Round 4 batch 24 NEW8 caught 6+ writer-family wide-TABLE_HEADER char-drift in 24b pre-Option-E (joins round 3 NEW8 catch of CPSCMRKS adjacent-letter swap; **NEW8 effectiveness validated 2× cumulative**).

**Why retain**: NEW8 substring n-gram cross-check vs canonical CDISC variable list catches char-swap that NEW2 single-character iteration misses; round 3 + round 4 evidence proves NEW8 closes a NEW2 gap.

**How to apply**: NEW8 mandatory in v1.3 cut; v1.4 candidate NEW8.b SENTENCE-trigram extension + NEW8.c TABLE_HEADER column-set validation.

### R-MS-8 round 4: AUDIT-mode pivot 4-family multi-burn-to-pool-exhaustion + write-tool-less + no-Bash adaptation sub-pattern reusable
Round 4 burned 3 slots: #32 omc:security-reviewer (write-tool-less + Bash heredoc) + #33 omc:scientist (write-tool-less + Bash heredoc) + #34 feature-dev:code-architect (write-tool-less + no-Bash inline content). Feature-dev family completes 3rd pool exhausted. Cumulative: 15 AUDIT-mode pivots cross 4 families, 3 EXHAUSTED.

**Why retain**: AUDIT-mode pivot recipe ("Mode: AUDIT, NOT <agent's normal action>" + write-tool-less adaptation + heredoc/inline content) proves family-agnostic. Future round 5+ can pivot to data/firecrawl/superpowers families using same recipe.

**How to apply**: Round 5 pre-allocate slots #35-#37 from data/firecrawl/superpowers/omc-family-remaining; reuse write-tool-less + inline-content sub-pattern.

### R-MS-9 round 4: G-MS-7 finding ID range pre-allocation 100% compliant + G-MS-13 cross-validation table EFFECTIVE
Round 4 G-MS-7 100% compliance (batch 23 67-70 / batch 24 71-74 / batch 25 75-78 all expected) + G-MS-13 round-3 mis-read pattern NOT recurred (kickoff §0 cross-validation table at top of each kickoff effective). Reconciler-side O-P1-79 added without collision.

**Why retain**: Round-3 G-MS-13 NEW gap → round-4 spec extension (cross-validation table) → round-4 0 mis-allocation; positive feedback loop replicated.

**How to apply**: Continue G-MS-13 cross-validation table at top of each round-X+ kickoff; codify in v1.3 cut as kickoff template.

### R-MS-10 round 4: G-MS-4 halt fallback decision tree spec'd 4 rounds running (live-fire still NOT triggered — accept spec-only validation OR design live-fire scenario for round 5+)
G-MS-4 halt fallback: (a) reconciler retry / (b) defer batch + merge sisters / (c) abort — spec'd round 2 + carried forward round 3 + 4. 4 rounds running success without live-fire test.

**Why retain**: 4 rounds without halt-state suggests sub-session implementation is robust; spec-only validation may be sufficient (or design adversarial scenario for round 5+).

**How to apply**: Round 5 retro decision: accept spec-only validation 4 rounds running OR design adversarial halt scenario (e.g., simulate ctx exhaustion or output cap hit) to live-fire test the decision tree.

### R-MS-11 round 4: Reconciler safety net validates 1/page Rule A audit limitation
Round 4 batch 25 Rule A 100% PASS (10/10 sampled atoms correct) but 4 atoms in LB-Examples block had NEW7 L6 sub-batch context drift not caught by Rule A 1/page sample (sample didn't include p.246 LB-Examples atoms). Reconciler cross-batch sibling continuity sweep caught it = O-P1-79 LOW Option H 4-atom fix.

**Why retain**: 1/page Rule A sample is statistical, not exhaustive; reconciler safety net is exactly the layer that catches systematic cross-sub-batch-block violations slipped past sampled audit. Architecture validated.

**How to apply**: Continue Rule A 1/page + reconciler sibling sweep as complementary layers; do NOT replace sweep with expanded Rule A sample (sample size grows linearly, sweep is structural).

### R-MS-12 round 4: NEW round-4 L5 sub-domain RESTART under L4 group container precedent
§6.3.5.7.1 MB L5 sib=1 RESTART under §6.3.5.7 Microbiology Domains (L4 plural group container, analogous to §6.3.5 L3 group). Extends NEW7 deep-nesting model with new branching for group-container L4 sub-domains.

**Why retain**: New deep-nesting precedent expands NEW7 chain spec; codify in v1.4 to handle similar group-container L4 sub-domains in future batches (likely §6.3.5.7.2 MS in batch 26).

**How to apply**: v1.4 codify NEW7 chain L4 sub-domain vs L4 group container branch; group-container case adds L5 RESTART for internal sub-domains, with L6 chain underneath each L5 sub-domain.

---

## §2 必须补上的缺口 (Round 4 Surfaces)

### G-MS-4 round 4 status: live-fire G-MS-4 NOT triggered 4 rounds running
**Gap**: 4 rounds spec-only validation; no live-fire test of decision tree fallback.

**Why**: Sub-session implementation robust; halt scenarios (writer failure rate >15%, drift cal <80%, ctx >80%, reviewer dispatch failure, shared-file write attempt) all avoided across 12 sub-sessions.

**How to apply**: Round 5 retro decision needed — accept spec-only validation as sufficient OR design adversarial halt scenario to live-fire test (e.g., simulate ctx exhaustion or unavailable reviewer).

### G-MS-NEW-4-1 round 4 NEW gap: NEW7 L6 sub-batch context drift RECURRENCE (round 3 batch 23 + round 4 batch 25)
**Gap**: 2nd recurrence within 2 rounds of same NEW7 L6 cross-sub-batch HEADING continuity drift motif:
- Round 3 batch 23 O-P1-68 (GF Examples 4-5 hl=5→6 fix)
- Round 4 batch 25 O-P1-79 (LB-Examples block 4 atoms — header hl/sib + 3 SENTENCE→HEADING promotion)

**Why**: Sub-batch executors lack visibility into other sub-batch state; 'Example N' default extraction defaults to SENTENCE without explicit HEADING prompt; L5/L6 sib counter restarts incorrectly without sub-batch handoff state.

**How to apply**: v1.3+ codification MUST include:
1. Explicit `'§6.3.5.X.Examples HEADING ALWAYS heading_level=5 sib=4'` bullet
2. Explicit `'Example N HEADING ALWAYS heading_level=6 sib=1..N RESTART per §6.3.5.X domain (NEVER SENTENCE)'` bullet
3. Procedural sub-batch handoff: kickoff dispatch prompt MUST include prior sub-batch L5/L6 chain state (Description=N/Spec=N/Assump=N/Examples=N + last Example sib used) so 25b-style executors don't restart sib counter

This is now the MOST URGENT v1.3 codification item alongside NEW1 dual-threshold.

### G-MS-NEW-4-2 round 4 NEW gap: writer-family wide-TABLE_HEADER 8th batch P1 cumulative + Option-E-resistant residual
**Gap**: Writer-family wide-TABLE corruption 8th cumulative batch (joins O-P1-23/34/36/37/38/50/63 + O-P1-71 round 4); Option-E partial recovery + reconciler-deferred residuals (O-P1-65 column-shift + O-P1-66 ABC0 + O-P1-67 GFTSTDTL/GRCh38 + O-P1-74 column-set + O-P1-67 narrow-scope = 5 cumulative reconciler-deferred manual repair items).

**Why**: Writer-family R10 strict no-paraphrase prepend not always followed; certain corruptions (column-shift, multi-row systemic) Option-E-resistant; 1/page Rule A sample misses bulk corruption residuals.

**How to apply**: v1.4 candidate writer-family R10 strict no-paraphrase prepend re-emphasis + char-level pre-DONE NEW2 hook for SENTENCE atoms similar to NEW2 for variable names; bulk reconciler-deferred sweep pass (mechanical sed/jq for residual character substitutions like ABC0→ABCD or GRCh38g12→GRCh38.p12) — to be scheduled at v1.3 cut session OR before P1 closure (currently 5 cumulative residuals; quantity stable per round = systemic not ramping).

### G-MS-NEW-4-3 round 4 NEW gap: v1.3 cut DEFERRED 4th time = ULTRA-CRITICAL escalation
**Gap**: v1.3 prompt cut DEFERRED 4 rounds running (round 1 deferred / round 2 deferred / round 3 DOUBLE-RECOMMENDED deferred / round 4 TRIPLE-RECOMMENDED + ULTRA-CRITICAL deferred). Cumulative inline-prepend overhead growing each round (~10-15 min/batch × 13 batches ≥ ~3 hours cumulative; ~250-375 min if continuing through P1 55-batch end).

**Why**: Rule D writer/reviewer isolation requires v1.3 cut in dedicated session (writer creates v1.3 + reviewer validates as separate agents/contexts); reconciler session writes too many things to do v1.3 cut without violation.

**How to apply**: ULTRA-CRITICAL escalation — schedule dedicated v1.3 cut session BEFORE batch 27 (next mandatory drift cal); v1.3 must include: R1-R15 + O-P1-26 + NEW1-NEW8 + NEW6/NEW6.b dual-form + NEW7-L6 sub-batch handoff procedural enforcement + density alarm spec G-MS-12 + NEW8 substring n-gram + G-MS-13 cross-validation table + NEW round-4 L5 group-container precedent.

### G-MS-NEW-4-4 round 4 NEW gap: 3 family pools EXHAUSTED post round 4 = round 5+ must pivot to new families
**Gap**: vercel + plugin-dev + feature-dev family pools all EXHAUSTED post round 4 (3/3 burned each); omc-family burned 7×; pr-family burned 1×.

**Why**: Roster expansion strategy started with 4 families post-batch-12; 4 rounds of multi-session burned 12 slots cross-family; 3 pools fully exhausted.

**How to apply**: Round 5 pre-allocate from data/firecrawl/superpowers/omc-family-remaining (release / setup / explore-deeper / planner-strategist / autopilot etc.); validate AUDIT-mode pivot recipe still applicable to data-pipeline-focused or web-scraping-focused agents (no precedent); fallback to omc-family-remaining most reliable.

### G-MS-NEW-4-5 round 4 NEW gap: drift cal cumulative cross-batch state still informal
**Gap**: Drift cal trigger cadence + cumulative atoms threshold still tracked in kickoff narrative + each batch _progress.json comment fields, not in structured state field.

**Why**: _progress.json structured arrays lag (batches_log + drift_cal_log not updated since batch 11); recovery_hint string + audit_matrix tables = single source of truth.

**How to apply**: Round 5 retro decision — invest in structured _progress.json arrays update (one-time catch-up batches 12-25) OR continue narrative-only tracking (acceptable but adds overhead at session boundary).

---

## §3 关键决策 (Round 4 Decisions)

### D-MS-1 round 4: Round 4 multi-session ✅ accept verdict + pattern saturated
**Decision**: Multi-session pattern is SATURATED after 4 rounds (~50% wall savings × 4 rounds × 30-page batches = ~6 hours cumulative savings); Tier 3 default-eligible for independent dense batches.

**Why**: 4 rounds × ~50% savings × 0 quality regression × 0 cross-round Rule D collision × NEW6.b proactive correctness × NEW1 4× validated × G-MS-13 cross-validation effective.

**How to apply**: Update CLAUDE.md / Tier 3 workflow template to mark multi-session pattern as default-eligible (with caveat: requires v1.3 stable prompt to retire inline-prepend overhead).

### D-MS-2 round 4: Round 5 (batches 26+) decision pending — recommend v1.3 cut FIRST
**Decision**: Round 5 strategy depends on v1.3 cut decision:
- (a) v1.3 cut FIRST (TRIPLE-RECOMMENDED + ULTRA-CRITICAL) then **single-session** with v1.3 (efficient, no inline-prepend overhead)
- (b) v1.3 cut FIRST then **multi-session round 5** with v1.3 stability + G-MS-13 cross-validation
- (c) skip multi-session round 5 if v1.3 cut delivers single-session efficiency comparable to multi-session ~50% savings

**Why**: v1.3 cut is the key blocking factor for further efficiency; without v1.3, inline-prepend overhead grows ~10-15 min/batch (~80-120 min/round); with v1.3, kickoffs can be terse and writer-family more reliable.

**How to apply**: User decides v1.3 cut session timing; once cut, run round 5 with v1.3 in single-session OR multi-session mode (pick based on batch size + dependency).

### D-MS-3 round 4: v1.3 cut DEFERRED 4th time + ULTRA-CRITICAL escalation
**Decision**: Defer v1.3 cut 4th time per Rule D writer/reviewer isolation; reconciler session cannot cut v1.3 without writer/reviewer self-overlap.

**Why**: Rule D mandates writer (creates v1.3) + reviewer (validates) be separate agents/contexts; reconciler session does merge + audit_matrix + _progress + retro = too many roles for clean v1.3 cut.

**How to apply**: User schedules dedicated v1.3 cut session BEFORE batch 27 (next mandatory drift cal); inputs = subagent_prompts/v1.3_patch_candidates.md + this retro §1 + rounds 2/3 retro + audit_matrix + _progress recovery_hint.

### D-MS-4 round 4: NEW7 L6 sub-batch context drift recurrence = formal codification mandatory
**Decision**: Round 3 batch 23 O-P1-68 + round 4 batch 25 O-P1-79 = 2 occurrences within 2 rounds of same motif; formal v1.3+ codification is now MANDATORY (not just RECOMMENDED).

**Why**: Recurrence within 2 rounds of same gap means current spec text (narrative-only) is insufficient; need procedural enforcement (explicit per-sub-batch HEADING handoff state + explicit 'Example N HEADING hl=6' bullet).

**How to apply**: v1.3 cut MUST include procedural sub-batch handoff template + explicit 'Example N HEADING hl=6' bullet (not just narrative NEW7 chain spec).

### D-MS-5 round 4: NEW round-4 L5 group-container precedent codification candidate
**Decision**: §6.3.5.7.1 MB L5 RESTART under §6.3.5.7 group container is NEW deep-nesting precedent; codify in v1.4 (not v1.3 since first occurrence vs NEW7-L6 recurrence which is v1.3 priority).

**Why**: First-occurrence finding at INFO severity; v1.3 cut already loaded with mandatory items; v1.4 patch can absorb L5 group-container branch alongside other v1.4 candidates (NEW8.b SENTENCE-trigram + NEW8.c TABLE_HEADER column-set + G-MS-12.a content-type-aware density).

**How to apply**: v1.4 patch agenda items: L5 group-container branch + NEW8.b + NEW8.c + G-MS-12.a; schedule v1.4 patch session AFTER v1.3 cut + 1-2 batches with v1.3 (validate v1.3 effectiveness before adding v1.4 patches).

### D-MS-6 round 4: Reconciler safety net validation = retain Rule A 1/page + reconciler sweep as complementary layers
**Decision**: Round 4 batch 25 Rule A 100% PASS but reconciler caught 4-atom systematic block (O-P1-79); 1/page Rule A sample is statistical not exhaustive; reconciler structural sweep is mandatory complement.

**Why**: Sample-based audit cannot catch systematic block violations; structural sweep across 6 batch jsonls + sort by (page, atom_index) is the only way to catch cross-sub-batch HEADING continuity gaps.

**How to apply**: Retain both layers in round 5+ multi-session protocol; document in MULTI_SESSION_PROTOCOL.md as architectural complement (not redundancy).

### D-MS-7 round 4: 3 family pools EXHAUSTED → round 5+ must pivot to data/firecrawl/superpowers
**Decision**: Round 5 pre-allocate slots #35-#37 from data/firecrawl/superpowers/omc-family-remaining families; AUDIT-mode pivot recipe applies; write-tool-less + heredoc/inline-content sub-pattern reusable.

**Why**: vercel + plugin-dev + feature-dev pools all 3/3 EXHAUSTED; omc-family burned 7× (still 1-2 candidates); pr-family burned 1× (1-2 candidates remaining). Round 5+ must pivot.

**How to apply**: Pre-allocate round 5 reviewer slots from candidate list (data:debugging-dags / data:airflow-hitl / firecrawl:skill-gen / superpowers:executing-plans / oh-my-claudecode:release / etc); apply AUDIT-mode prepend ("Mode: AUDIT, NOT <normal action>") + write-tool-less adaptation.

---

## Appendix: Cumulative State Post Round 4

| Field | Value |
|---|---|
| Total atoms | 6146 (5502 + 226 + 208 + 210) |
| Total pages | 250 (1-250 unique) |
| Total batches | 25 |
| Total findings | 62 (53 prior + 8 round 4 issued + 1 reconciler-side O-P1-79; 70/76/77/78 reserved-but-unused freed) |
| Total Rule D slots | 34 |
| AUDIT-mode pivots | 15 |
| Family pools EXHAUSTED | 3 (vercel + plugin-dev + feature-dev) |
| TOC anchor cumulative n | 170 |
| Consecutive batches anchored | 17 |
| Repair cycles cumulative | 39 (36 + 3 round 4) |
| Multi-session rounds completed | 4 |
| Wall savings cumulative | ~6 hours (~50% × 4 × 4 hrs/round serial) |
| v1.3 cut status | DEFERRED 4th time + ULTRA-CRITICAL escalation |
| Next mandatory drift cal | batch 27 |
| Next critical decision | v1.3 cut session before batch 27 |

---

> Round 4 verdict ✅ — multi-session pattern saturated; reconciler safety net validated (caught O-P1-79 systematic block); v1.3 cut DEFERRED 4th time + ULTRA-CRITICAL.
> The boulder never stops.
