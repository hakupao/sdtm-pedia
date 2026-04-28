# v1.7 Cut Session Handoff — Design Spec for Fresh Session Execution

> **Date**: 2026-04-29
> **Trigger**: round 10 batch 42 drift cal p.412 6th cumulative writer-direction VALUE HALLUCINATION recurrence DESPITE v1.6 N18 EXTENDED scope dispatch (CATASTROPHIC FAIL both thresholds: strict 25.0% + verbatim Jaccard 17.1%) → v1.7 trigger ESCALATION
> **Daisy ack**: Option B authorized 2026-04-29 ("走 b, 听你的建议") in halt_state_batch_42.md §9
> **Owner**: fresh session (NOT current session C; this is a v1.7 cut design handoff per v1.4/v1.5/v1.6 cut precedent of dedicated sessions)
> **Pre-condition**: round 10 reconciler E DONE (sister B batch 41 + sister D batch 43 + reconciler E cross-session merge complete) — v1.7 cut absorbs reconciler-stage candidates if any

## §1 Background

5 cumulative writer-direction VALUE HALLUCINATION recurrences (round 5+6+7+8+9) on 2 distinct content types (`examples_narrative_spec_table` + `mixed_structural_transition`) progressively expanded the writer-family ban scope:
- v1.4 (post round 7): 14 NEW patches N1-N14, no writer-family ban
- v1.5 (post round 8): N16 writer-family ban for `examples_narrative_spec_table` content type (partial ban scope)
- v1.6 (post round 9): N18 EMERGENCY-CRITICAL writer-family ban EXTENDED scope (5 sub-rules a-e: Examples-narrative+spec-table + URLs/DOIs + TABLE_ROW ≥500 chars + general VERBATIM-CRITICAL + mixed_structural_transition MANDATORY)

Round 10 batch 42 drift cal p.412 (10th cumulative drift cal carrier) confirmed N18 partial ban INSUFFICIENT — writer-direction VALUE HALLUCINATION is **content-type-INDEPENDENT** (writer fabricated TABLE_HEADER columns + TABLE_ROW values on `examples_narrative_spec_table` content type that v1.6 N18.a EXPLICITLY BANS via executor-MANDATORY dispatch). 6th cumulative recurrence triggers v1.7 ESCALATION per v1.6 N18 last paragraph + kickoff §0.4.

## §2 v1.7 PRIMARY trigger — N21 EMERGENCY-CRITICAL writer-family complete deprecation

### §2.1 Codification

**Rule v1.7 N21**: `oh-my-claudecode:writer` (writer-family) is INELIGIBLE for **ANY production atomization** across **ALL content types** in P1 batch atomization workflow. This replaces:
- v1.5 N16 partial ban (Examples-narrative+spec-table content type only)
- v1.6 N18 EXTENDED scope partial ban (5 sub-rules a-e)

with COMPLETE ban: writer-family permitted ONLY for:
- v1.4-or-earlier prompt audit reviewer slots (Rule D AUDIT pivot mode, NOT atomization)
- Drift cal alternation rerun for direction-attribution validation (NOT merged to root regardless — same as v1.6 NEW EXECUTOR-VARIANT alternation pattern kickoff §3.3)

**All P1 atomization** (sub-batch a/b/c writer dispatch) MUST use `oh-my-claudecode:executor` family (or non-writer-family agents like `general-purpose` etc. permitted under Rule D when used as reviewer).

**Pre-dispatch validation Hook 16.7 (NEW v1.7)**:
```python
# v1.7 N21 pre-dispatch hook (replaces v1.6 Hook 16.6 5-sub-rule a-e check with simpler total ban)
if subagent_type.endswith("writer") and dispatch_purpose == "production_atomization":
    raise AssertionError("v1.7 N21 violation: writer-family BANNED for ALL production atomization across ALL content types")
# Drift cal alternation exception:
if subagent_type.endswith("writer") and dispatch_purpose == "drift_cal_alternation_artifact":
    pass  # OK — artifact NOT merged to root; for direction-attribution validation only
```

### §2.2 Dispatch table simplification

v1.6 N18 EXTENDED scope dispatch table (5 sub-rules a-e content-type-binding) → v1.7 single rule: **production atomization → executor-family MANDATORY across ALL content types**. Eliminates content-type-hint pre-dispatch scan complexity (v1.6 NEW input fields `n18_url_atoms_count` + `n18_long_cell_atoms_count` REMOVED in v1.7 since redundant under N21).

### §2.3 Halt threshold for 7th recurrence (escalation beyond writer-family deprecation)

If round 11+ drift cal under v1.7 baseline reveals 7th cumulative writer-direction VALUE HALLUCINATION recurrence (impossible by N21 design since writer NOT used in production), the trigger is impossible. BUT if the recurrence is observed at executor-direction (NEW motif), v1.8 trigger candidates surface (executor-family hardening — out-of-scope for v1.7).

## §3 v1.7 SECONDARY candidates — N22 + N23

### §3.1 N22 Hook 18 SENTENCE-paragraph-concat WARN→halt-on-violation promotion

**Source**: round 9 + round 10 cumulative 5+ PARTIAL atoms on SENTENCE-paragraph-concat motif (round 9 batch 39 4 PARTIAL + round 9 batch 40 1 PARTIAL ig34_p0391_a002 + round 10 batch 42 likely 0-1 PARTIAL — Rule A reviewer report has details).

**Decision options for v1.7**:
- **(a) Promote to halt-on-violation**: v1.6 Hook 18 was WARN-mode; v1.7 may mandate halt-on-violation if SENTENCE atom verbatim contains regex `\.\s+[A-Z]` match (multi-sentence concat detected). Rationale: round 9+10 motif persistent.
- **(b) Keep WARN-mode**: under N21, writer-family deprecated entirely; executor-family round 9+10 cumulative SENTENCE-paragraph-concat motif rate may be lower (Rule A PASS-rate 95%+ suggests soft motif, not blocking). Hook 18 WARN-mode acceptable.
- **(c) Reaffirm unchanged**: minimal change; let round 11+ data decide promotion.

**Recommendation**: option (b) — keep WARN-mode, but add narrative-chapter exemplar refinement to executor prompt (writer prompt deprecated under N21).

### §3.2 N23 Hook 19 PDF-cross-verify detection-not-prevention REINFORCED escalation

**Source**: round 9 batch 39 + round 10 batch 42 = 2 cumulative writer self-claim "all hooks PASS" disproven by main-session post-rerun PDF cross-check (round 9 caught 3 hallucinated atoms; round 10 caught 5+ hallucinated atoms incl. TABLE_HEADER fabrication). Hook 19 N=10 sample expansion + mandatory URL/DOI/citation cross-check INSUFFICIENT to catch column-name fabrication or cell-value drift.

**Decision options for v1.7**:
- **(a) Full-table cross-verify mandatory**: ALL TABLE_HEADER + TABLE_ROW atoms (no sample, full population) → halt-on-violation per any cell-value or column-name discrepancy. High overhead but eliminates writer self-claim trust gap.
- **(b) Rendered moot by N21**: under writer-family deprecation, executor-family Hook 19 self-claim trust profile may differ (executor doesn't exhibit fabrication motif per round 5-10 cumulative evidence). N23 may be unnecessary.
- **(c) Promote sample N=10 → N=20 + add table-axis stratification**: middle ground.

**Recommendation**: option (b) — N23 RENDERED MOOT by N21. Executor self-claim trust profile validated cumulative round 5-10 (production 9828+217=10045 atoms post-round-9 0 cumulative writer-direction VALUE HALLUCINATION when executor-only). N23 codification deferred to v1.8 if executor-family ever exhibits motif.

## §4 v1.7 prompt files (4 files to compose)

### §4.1 P0_writer_pdf_v1.7.md

Delta-style carry-forward v1.6 §A-AB base + 1 NEW patch §N21 EMERGENCY-CRITICAL writer-family complete deprecation. Self-Validate hooks 1-20 carry-forward + Hook 16.6 → 16.7 (simplified pre-dispatch ban).

**Section structure** (analogous to v1.6 §200 lines):
- §角色硬约束 (carry-forward v1.6)
- §派发 subagent_type (REWRITE — v1.7 simple total ban replaces v1.6 EXTENDED scope table)
- §输入 (REMOVE v1.6 N18 input fields `n18_url_atoms_count` + `n18_long_cell_atoms_count`)
- §任务流程 8 steps (carry-forward; remove Hook 16.6 5-sub-rule check; add Hook 16.7 simple ban)
- CODIFIED R-RULES carry-forward §A-AB unchanged (28 items v1.6 → §A-AC v1.7 with N21 NEW)
- §N21 NEW (emergency-critical writer-family complete deprecation rationale + sub-rule replacement table v1.5 N16 + v1.6 N18 → v1.7 N21)
- Self-Validate hooks final list (1-20 carry-forward + 16.7 NEW replacing 16.6)
- STATUS PROMOTIONS sustained (N14 STRONGLY VALIDATED 4th live-fire post round 10 batch 42 + G-MS-4 STRONGLY VALIDATED 3rd live-fire post round 10 batch 42 + N18 EXTENDED scope EFFECTIVENESS PROVEN production-side post round 10 + N18 PARTIAL ban INSUFFICIENT PROVEN drift-cal-side post round 10)
- Changelog: v1.7 entry with all changes documented

### §4.2 P0_writer_md_v1.7.md

Paired sync N21 (MD writer also deprecated for production atomization across all content types? Or scoped only to PDF-side P1 atomization?).

**Decision needed at v1.7 cut session**: does N21 deprecate writer-family ALSO for MD-side atomization (P0 + P1 MD writer dispatch), or only for PDF-side atomization?

**Recommendation**: scope N21 to P1 PDF-side atomization only (preserve MD writer for MD-side atomization which has different content-type profile + lower cumulative recurrence count). MD writer prompt v1.7 = thin paired-sync of v1.7 PDF prompt with N21 explicitly noted as PDF-only.

### §4.3 P0_matcher_v1.7.md

Carry-forward v1.6 markers + 1 NEW marker:
- `[N21_writer_family_deprecation_violation]` HIGH severity covering N21 violation (writer-family used for production atomization post v1.7 cut)

### §4.4 P0_reviewer_v1.7.md

Major changes from v1.6 (145 lines):

**§0 AGENT-vs-SKILL roster doc UPDATED post round 10**:
- Add 4 NEW slots round 10 + v1.7 cut (#53 verifier round 10 batch 41 + #54 general-purpose round 10 batch 42 + #55 tracer round 10 batch 43 + #56 v1.7 cut candidate `oh-my-claudecode:tracer` 12th burn intra-family depth — but tracer was used #55, so #56 = `codex:codex-rescue` 3rd burn extension OR `Plan` 2nd burn extension OR `claude-code-guide` 2nd burn extension OR `Explore` 2nd burn extension)
- omc family burn count post round 10: planner 10 + verifier 11 + tracer 12 = **12 saturated** (3 NEW burns round 10 incl tracer 12th); remaining un-burned omc-family AGENTs: code-reviewer / code-simplifier / executor (writer-side) / explore (search-specialist) / qa-tester / writer (writer-side)
- general-purpose family 4× post round 10 (3rd → 4th burn extension at slot #54)
- Explore family 1× INAUGURAL (sustains)
- codex family 2× post v1.6 cut (sustains; v1.7 cut would extend to 3× if used)
- Plan + claude-code-guide each 1× INAUGURAL (sustain)

**§已烧 Rule D roster (post round 10 + v1.7 cut, 累 56 slots)**: add #53/#54/#55/#56 rows.

**v1.7 Fix 验证矩阵 (31 items A-AE, expanded over v1.6 28-item A-AB matrix)**:
- A-AB carry-forward (28 items v1.6)
- **AC**: N21 EMERGENCY-CRITICAL writer-family complete deprecation per O-P1-145 HIGH (round 10 batch 42 6th cumulative writer-direction VALUE HALLUCINATION recurrence proof)
- **AD**: N22 Hook 18 promotion candidate decision (recommend option b — keep WARN-mode + narrative-chapter exemplar refinement) per round 9+10 cumulative 5+ PARTIAL atoms
- **AE**: N23 Hook 19 N20 detection-not-prevention REINFORCED candidate decision (recommend option b — RENDERED MOOT by N21) per round 9+10 cumulative 2 writer self-claim disproven incidents

**§Step 4 Branch A/B/C** carry-forward unchanged.

**STATUS PROMOTIONS**:
- N14 STRONGLY VALIDATED 4th LIVE-FIRE (round 7 batch 33 + round 8 batch 36 + round 9 batch 39 + round 10 batch 42)
- G-MS-4 STRONGLY VALIDATED 3rd LIVE-FIRE (round 7 batch 32 + round 8 batch 36 + round 10 batch 42)
- N9 + N10 leaf-pattern codifications graduated CROSS-LEAF-DOMAIN VALIDATED 4th cumulative live-fire (round 8 FA + round 9 SR + round 9 TA + round 10 TD/TM/TI/TS = 4-leaf-domain)
- N11 chapter-short-bracket extension L1+L2+L3 FULL-SCOPE VALIDATED + 1 NEW L2 transition round 10 batch 42 (§7.4 [TRIAL ELIGIBILITY AND SUMMARY (TI AND TS)])
- **N18 EXTENDED scope EFFECTIVENESS PROVEN production-side** (round 10 batch 42 production 217 atoms executor-clean post N18.a/b/d/e bindings) but **N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side** (round 10 batch 42 drift cal 6th recurrence on N18.a-banned content type) → v1.7 trigger justified
- **NEW v1.7**: N21 writer-family complete deprecation (replaces N16 + N18 partial bans)

**§0.5 reconciler-side cross-session canonical-form drift sweep** carry-forward unchanged.

**Changelog**: v1.7 entry documenting all changes.

## §5 v1.7 cut session execution plan

### §5.1 Pre-condition checklist (verify before v1.7 cut session START)

- [ ] Round 10 sister B (batch 41) `PARALLEL_SESSION_41_DONE` or `HALT_BATCH_41` echoed
- [ ] Round 10 sister D (batch 43) `PARALLEL_SESSION_43_DONE` or `HALT_BATCH_43` echoed
- [ ] Reconciler E round 10 cross-session merge complete + `MULTI_SESSION_RETRO_ROUND_10.md` written
- [ ] No additional v1.7 candidates surface from sister B/D/reconciler E (if surfaced, append to §3 secondary candidates list before v1.7 prompts compose)

### §5.2 Session execution sequence (fresh session)

1. **Read context** (parallel reads):
   - `.work/06_deep_verification/multi_session/v1_7_cut_handoff.md` (this file — primary spec)
   - `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.6.md` + `P0_writer_md_v1.6.md` + `P0_matcher_v1.6.md` + `P0_reviewer_v1.6.md` (v1.6 base for delta carry-forward)
   - `.work/06_deep_verification/subagent_prompts/archive/v1.5_final_2026-04-29/` (for §A-Y carry-forward base text)
   - `.work/06_deep_verification/evidence/checkpoints/drift_cal_batch_42_p412_report.md` (v1.7 trigger evidence)
   - `.work/06_deep_verification/evidence/checkpoints/halt_state_batch_42.md` (Daisy ack)
   - `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_10.md` (post-reconciler — may have additional candidates)
   - `.work/06_deep_verification/_progress.json` (recovery_hint + halt_batch_42_resolution block)

2. **Compose v1.7 prompts** (4 files, delta-style carry-forward):
   - `subagent_prompts/P0_writer_pdf_v1.7.md` (per §4.1 above)
   - `subagent_prompts/P0_writer_md_v1.7.md` (per §4.2 above; MD-side scoping decision)
   - `subagent_prompts/P0_matcher_v1.7.md` (per §4.3 above; +1 NEW marker)
   - `subagent_prompts/P0_reviewer_v1.7.md` (per §4.4 above; roster 52→56 + matrix 28→31)

3. **Rule D AUDIT pivot for v1.7 cut**:
   - Recommended slot #56: `codex:codex-rescue` 3rd burn extension (codex-family 3-burn intra-family depth — sustains "external runtime / different model = strongest Rule D isolation" principle for prompt cut audit purpose)
   - Alternative: `Plan` 2nd burn extension (single-agent family) OR `claude-code-guide` 2nd burn extension OR `Explore` 2nd burn extension
   - Threshold: ≥25/31 PASS = production-ready bar (analogous to v1.6 cut codex audit ≥22/28)

4. **Audit findings remediation** (if any HIGH/MEDIUM findings surface, fix in-session before sign-off; v1.6 cut had 4 findings M1-M4 all remediated in-session)

5. **Archive v1.6 prompts to `subagent_prompts/archive/v1.6_final_2026-04-29/`**

6. **Update _progress.json + audit_matrix.md + CLAUDE.md Multi-Session Parallel Protocol section** (add v1.7 cut details block + update reviewer pool partition for round 11)

7. **Round 11 batches 44/45/46 multi-session preparation**:
   - 4 kickoff files: `multi_session/batch_44_kickoff.md` + `batch_45_kickoff.md` + `batch_46_kickoff.md` + `reconciler_kickoff_round11.md`
   - Pre-allocated reviewer slots #57/#58/#59 (NOT cumulative #1-#56)
   - content_type_hint per sub-batch + drift cal target page batch 45 (per cadence batch 42→45)
   - **CRITICAL**: under v1.7 N21, ALL writer dispatch in batch 44/45/46 = `oh-my-claudecode:executor` (writer-family deprecated entirely)

### §5.3 Sign-off criteria

- ≥25/31 fix matrix items PASS via Rule D AUDIT slot #56
- All HIGH/MEDIUM findings remediated in-session (no deferred)
- v1.6 archived correctly
- _progress.json + audit_matrix.md + CLAUDE.md updated
- Round 11 kickoffs prepared (or deferred per user decision)
- Daisy ack: SAFE_FOR_DAISY_ACK echo

## §6 Round 10 retro embedding (for reconciler E reference)

Round 10 post-batch-42 retro candidates (to be embedded in reconciler E `MULTI_SESSION_RETRO_ROUND_10.md`):

### R-MS-NEW-10-1 (retain): N18 EXTENDED scope EFFECTIVENESS PROVEN production-side
Round 10 batch 42 production 217 atoms (42a 87 + 42b 130) executor-clean post N18.a/b/d/e content-type-binding dispatch. Schema sweep 0 violations. Hook 19 N20 PDF-cross-verify all URLs (p.418 TS Assumption 5+8) + identifiers (p.420 TS Example 1 15+ controlled-term codes) BYTE-EXACT. N18 production-side prevention layer working as designed.

### G-MS-NEW-10-1 (gap): N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side
Round 10 batch 42 drift cal p.412 6th cumulative writer-direction VALUE HALLUCINATION recurrence on `examples_narrative_spec_table` content type that v1.6 N18.a EXPLICITLY BANS. Drift cal verdict CATASTROPHIC FAIL both thresholds (strict 25.0% / verbatim Jaccard 17.1% — LOWEST in P1 cumulative). Writer fabricated TABLE_HEADER columns + TABLE_ROW values via training-data-template motif. v1.7 trigger ESCALATION codified.

### D-MS-NEW-10-1 (decision): v1.7 cut Option B authorized → writer-family complete deprecation N21
User authorized 2026-04-29 ("走 b, 听你的建议") in halt_state_batch_42.md §9. v1.7 cut session prep handed off via this v1_7_cut_handoff.md design spec. v1.7 cut session = fresh session post-reconciler-E. Round 11 batches 44/45/46 dispatch under v1.7 baseline (writer-family INELIGIBLE for production atomization across ALL content types).

### D-MS-NEW-10-2 (decision): G-MS-4 halt fallback 3rd LIVE-FIRE EFFECTIVE
Round 10 batch 42 = 3rd cumulative G-MS-4 halt fallback live-fire (round 7 batch 32 1st + round 8 batch 36 2nd + round 10 batch 42 3rd). Halt protocol successfully escalated v1.7 trigger to user with structured 4-resume-options + recommendation. STRONGLY VALIDATED status sustained at 3 cumulative live-fires.

### D-MS-NEW-10-3 (decision): N14 strict alternation methodology 4th LIVE-FIRE EFFECTIVE
Round 10 batch 42 = 4th cumulative N14 live-fire (round 7 + round 8 + round 9 + round 10 = 4 live-fires). v1.6 NEW EXECUTOR-VARIANT alternation pattern (kickoff §3.3) successfully attributed direction (REVERSED — writer hallucinated, executor clean). Direction REVERSED 13th cumulative + value-add 14th precedent. STRONGLY VALIDATED status sustained at 4 cumulative live-fires.

## §7 References

- v1.6 prompts (current ACTIVE, will become v1.6 archived post v1.7 cut): `subagent_prompts/P0_writer_pdf_v1.6.md` + `P0_writer_md_v1.6.md` + `P0_matcher_v1.6.md` + `P0_reviewer_v1.6.md`
- v1.5 archived: `subagent_prompts/archive/v1.5_final_2026-04-29/` (full §A-Y carry-forward base text reference)
- Drift cal batch 42 evidence: `evidence/checkpoints/drift_cal_batch_42_p412_report.md` + `drift_cal_p412_metrics.json` + `drift_cal_p412_writer_rerun.jsonl`
- Halt state batch 42: `evidence/checkpoints/halt_state_batch_42.md`
- v1.6 cut reviewer report (precedent): `evidence/checkpoints/v1_6_cut_reviewer_report.md`
- Round 10 multi-session protocol: `multi_session/MULTI_SESSION_PROTOCOL.md` (master; round 1-9 augmented inline) + `MULTI_SESSION_RETRO_ROUND_9.md` (round 9 retro)
- Reconciler kickoff round 10: `multi_session/reconciler_kickoff_round10.md` (when sister B + D done)

---

*v1.7 cut session handoff prepared 2026-04-29 by session C post-HALT_BATCH_42 + Daisy Option B ack. Awaiting fresh session execution post-reconciler-E round 10 merge.*
