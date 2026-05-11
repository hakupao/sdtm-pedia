# P0 Writer PDF — 原子化 prompt v1.7

> Version: v1.7 (2026-04-29, post P1 round 10 cut — formal codification of round 10 v1.7 trigger ESCALATION + 6 cumulative writer-direction VALUE HALLUCINATION recurrences across 6 rounds 5-10 on 2 distinct content types)
> 基于 v1.6 (2026-04-29 round 9 cut + 3 NEW patches N18-N20 + Self-Validate hooks 17→20 + STATUS PROMOTIONS) + round 10 (batches 41/42/43) cumulative
> 角色: Writer (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.7 变更 over v1.6: **EMERGENCY-CRITICAL writer-family complete deprecation entirely from P1 production atomization across ALL content types (N21 PRIMARY).** Replaces N16 v1.5 partial ban (Examples-narrative+spec-table only) + N18 v1.6 EXTENDED partial ban (5 sub-rules a-e) with COMPLETE ban. Schema link + 13 §A-M v1.3 base + 14 §N1-N14 v1.4 patches + 3 §N15-N17 v1.5 patches + 3 §N18-N20 v1.6 patches 全 carry-forward unchanged. v1.7 把 round 10 1 PRIMARY trigger + 2 SECONDARY decisions 固化进 prompt; 1 NEW writer-side patch N21 加在 §A-AB codified base 之上 + Self-Validate Hook 16.6 → 16.7 (simplified pre-dispatch ban) + N18 input fields REMOVED (redundant under N21) + Changelog. POST 6th cumulative writer-direction main-line VALUE HALLUCINATION recurrence on **examples_narrative_spec_table** content type DESPITE v1.6 N18.a EXPLICITLY BANS (round 10 batch 42 p.412 TABLE_HEADER fabrication TDDESC/TDANCVRF/TDEVALU1-4/STUDYID-duplicate/ARMCD/TDSEQ INVENTED columns + TABLE_ROW value fabrication P9W→P1W/P11W→P1W/P13W cell DROPPED) ESCALATED to writer-family complete deprecation per N21.

## 角色硬约束 (v1.6 carry-forward unchanged)

参 `archive/v1.6_final_2026-04-29/P0_writer_pdf_v1.6.md` §角色硬约束 + v1.5 base + v1.4 baseline carry-forward 全文.

## 派发 subagent_type (v1.7 N21 EMERGENCY-CRITICAL writer-family complete deprecation)

**v1.6 carry-forward N18 EXTENDED scope base SUPERSEDED by v1.7 N21 COMPLETE BAN.**

**🔴 v1.7 N21 EMERGENCY-CRITICAL writer-family complete deprecation (post 6th cumulative writer-direction VALUE HALLUCINATION recurrence DESPITE v1.6 N18 EXTENDED scope dispatch on examples_narrative_spec_table content type N18.a EXPLICITLY BANS)**:

| Dispatch purpose | v1.6 N18 EXTENDED dispatch (SUPERSEDED) | v1.7 N21 COMPLETE BAN dispatch | Justification |
|---|---|---|---|
| **ANY P1 production atomization** (sub-batch a/b/c) | content-type-binding 5 sub-rules a-e (executor MANDATORY for a/b/c/d/e; writer permitted for SENTENCE-paragraph + LIST_ITEM-heavy ONLY) | **`oh-my-claudecode:executor` MANDATORY across ALL content types** (writer-family INELIGIBLE) | round 5+6+7+8+9+10 = 6 cumulative writer-direction VALUE HALLUCINATION recurrences across 2 distinct content types (`examples_narrative_spec_table` + `mixed_structural_transition`) PROVES writer-direction motif is content-type-INDEPENDENT |
| **Drift cal alternation rerun** (direction-attribution validation) | EXECUTOR-VARIANT alternation pattern (kickoff §3.3 v1.6 NEW) — baseline executor + rerun writer | **continue EXECUTOR-VARIANT alternation pattern UNCHANGED** — rerun writer used ONLY for direction-attribution validation; **rerun atoms NOT MERGED to root regardless** (artifact-only per kickoff §3.3) | preserves N14 STRONGLY VALIDATED methodology direction-attribution capability without contaminating production atoms |
| **Rule D AUDIT pivot reviewer slots** (v1.4-or-earlier prompt audit reviewer slots) | writer-family permitted in AUDIT-mode (NOT atomization) | **writer-family permitted in AUDIT-mode (NOT atomization)** carry-forward unchanged | Rule D AUDIT pivot reviewer evaluates prompt files (read-only), not atom emission; no VALUE HALLUCINATION risk applies |

**Effect**: v1.7 N21 = writer-family **INELIGIBLE for ANY production atomization across ALL content types**. Production atomization MUST use `oh-my-claudecode:executor` family (or non-writer-family agents like `general-purpose` etc. when used as reviewer/AUDIT pivot per Rule D).

**Pre-dispatch validation Hook 16.7 (NEW v1.7, REPLACES Hook 16.6 v1.6 5-sub-rule check)**:

```python
# v1.7 N21 pre-dispatch hook (replaces v1.6 Hook 16.6 5-sub-rule a-e check with simpler total ban)
if subagent_type.endswith("writer") and dispatch_purpose == "production_atomization":
    raise AssertionError("v1.7 N21 violation: writer-family BANNED for ALL production atomization across ALL content types (deprecate post 6th cumulative writer-direction VALUE HALLUCINATION recurrence round 10 batch 42 p.412)")
# Drift cal EXECUTOR-VARIANT alternation exception (carry-forward kickoff §3.3 v1.6 NEW):
if subagent_type.endswith("writer") and dispatch_purpose == "drift_cal_alternation_artifact":
    pass  # OK — artifact NOT merged to root regardless; for direction-attribution validation only
# Rule D AUDIT-mode reviewer exception (carry-forward unchanged):
if subagent_type.endswith("writer") and dispatch_purpose == "rule_d_audit_pivot_reviewer":
    pass  # OK — read-only prompt audit, no atom emission
```

**Halt threshold for 7th recurrence**: under N21 design (writer NOT used in production), 7th cumulative writer-direction recurrence is impossible by construction. BUT if a NEW motif surfaces at executor-direction (round 11+), v1.8 trigger candidates surface (executor-family hardening — out-of-scope for v1.7).

## 输入 (v1.6 carry-forward + v1.7 REMOVE N18 input fields)

参 v1.6 §输入. v1.7 NEW:
- **REMOVE v1.6 N18 input fields**: `n18_url_atoms_count` + `n18_long_cell_atoms_count` REMOVED — no longer needed since N21 mandates executor for ALL content types regardless of URL/DOI/long-cell content. Eliminates content-type-hint pre-dispatch scan complexity.

## 任务流程 (v1.6 carry-forward + Hook 16.7 replaces 16.6)

参 v1.6 §任务流程 8 steps. v1.7 NEW:
- **Step 8 Hook 16.6 → 16.7 substitution**: simplified pre-dispatch ban (see §派发 above). All other hooks 1-20 carry-forward unchanged.

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.6 carry-forward §A-AB, FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.6_final_2026-04-29/P0_writer_pdf_v1.6.md` for full §A-AB text:
- §A R1-R15 (15 累 R-rules) — v1.3 base + v1.4 N5/N13 hardening + v1.5 carry-forward + v1.6 carry-forward
- §B-§M v1.3 base codifications
- §N1-N14 v1.4 NEW patches
- §N15-N17 v1.5 NEW patches (.xpt-parent FORBID + writer-family ban Examples-narrative+spec-table + post-extraction VALIDATION pass Self-Validate hooks 14→17)
- §N18-N20 v1.6 NEW patches (writer-family ban EXTENDED scope 5 sub-rules a-e + SENTENCE-paragraph-concat Hook 18 WARN-mode + PDF-cross-verify expansion N=10 + mandatory URL/DOI/citation cross-check)

═══════════════════════════════════════════════════════════════════
## v1.7 NEW PATCH (N21, codifying round 10 v1.7 PRIMARY trigger)
═══════════════════════════════════════════════════════════════════

### §N21 EMERGENCY-CRITICAL writer-family complete deprecation entirely from P1 production atomization across ALL content types (per round 10 batch 42 6th cumulative writer-direction VALUE HALLUCINATION recurrence DESPITE v1.6 N18 EXTENDED scope dispatch = O-P1-145 HIGH)

**Source**: round 10 batch 42 p.412 drift cal NEW1 dual-threshold 10th time CATASTROPHIC FAIL BOTH THRESHOLDS — 6th cumulative writer-direction main-line VALUE HALLUCINATION recurrence on `examples_narrative_spec_table` content type that v1.6 N18.a EXPLICITLY BANS. v1.6 NEW EXECUTOR-VARIANT alternation pattern (kickoff §3.3) successfully attributed direction REVERSED — baseline executor PDF-correct + rerun writer hallucinated. Hallucinations PDF-verified by main session post drift cal:

- **TABLE_HEADER fabrication** (NEW MODE not seen rounds 5-9): writer ig34_p0412_a021 invented columns `STUDYID-duplicate / ARMCD (TA-domain not TD) / TDSEQ (no such variable) / TDDESC (no such variable) / TDANCVRF (actual is TDANCVAR) / TDEVALU1-4 (no such variables)` while DROPPING actual PDF columns `DOMAIN / TDORDER / TDANCVAR / TDTGTPAI / TDMINPAI / TDMAXPAI / TDNUMRPT`. Same training-data-template motif extends to TABLE_HEADER column-name fabrication.
- **TABLE_ROW value fabrication** (carry-forward motif rounds 5-9): a022/a023/a024 cells `P9W→P1W` (digit deletion) + `P11W→P1W` (digit deletion) + `P13W` cell DROPPED + 3-4 EXTRA empty pipe cells per row creating cascading column-misalignment from fabricated header.

**Cumulative recurrence trace**:

| Round | Batch | Drift cal page | Content type | Recurrence # | Motif |
|---|---|---|---|---|---|
| 5 | 28 | p.270 | examples_narrative_spec_table | 1st | TABLE_ROW VALUE HALLUCINATION (USUBJID/PCREFID/PCTESTCD INVENTED IDs) (O-P1-85) |
| 6 | 31 | p.293 | examples_narrative_spec_table | 2nd | TABLE_ROW VALUE HALLUCINATION (O-P1-103) |
| 7 | 34 | p.325 | examples_narrative_spec_table | 3rd | TABLE_ROW VALUE HALLUCINATION (O-P1-109) |
| 8 | 36 | p.357 | examples_narrative_spec_table | 4th | TABLE_ROW VALUE HALLUCINATION → halt → Option H bulk repair → triggered v1.5 N16 codification |
| 9 | 39 | p.382 | mixed_structural_transition | 5th | URL .org→.ch + word `clinical` deletion + TABLE_ROW Study cell ~26% TRUNCATION+REORDER (O-P1-134) → triggered v1.6 N18 EXTENDED scope codification |
| **10** | **42** | **p.412** | **examples_narrative_spec_table** | **6th** | **TABLE_HEADER FABRICATION (NEW MODE) + TABLE_ROW VALUE FABRICATION** (O-P1-145) → **v1.7 TRIGGER ESCALATION**: deprecate writer-family entirely from P1 atomization |

**Conclusion**: writer-direction VALUE HALLUCINATION is **content-type-INDEPENDENT**. Partial bans (N16 v1.5 examples_narrative_spec_table only + N18 v1.6 EXTENDED 5 sub-rules a-e) consistently insufficient at preventing recurrence. Complete ban is the only escalation level remaining short of restructuring writer-family architecture.

**Rule v1.7 N21**: `oh-my-claudecode:writer` (writer-family) is **INELIGIBLE for ANY production atomization** across **ALL content types** in P1 batch atomization workflow. This replaces:
- v1.5 N16 partial ban (Examples-narrative + spec-table content type only)
- v1.6 N18 EXTENDED scope partial ban (5 sub-rules a-e: a Examples-narrative+spec-table + b URLs/DOIs + c TABLE_ROW ≥500 chars + d general VERBATIM-CRITICAL clause + e mixed_structural_transition MANDATORY)

with **COMPLETE BAN**: writer-family permitted ONLY for:
- (a) Rule D AUDIT pivot reviewer slots (read-only prompt audit, NOT atomization)
- (b) Drift cal EXECUTOR-VARIANT alternation rerun for direction-attribution validation (kickoff §3.3, artifact NOT merged to root regardless)

**All P1 atomization** (sub-batch a/b/c writer dispatch) MUST use `oh-my-claudecode:executor` family (or non-writer-family agents like `general-purpose` etc. permitted under Rule D when used as reviewer).

**Self-Validate hook (NEW Hook 16.7 pre-dispatch — REPLACES Hook 16.6 v1.6)**: pseudo-code in §派发 above. Halt-on-violation pre-dispatch for `production_atomization` purpose; `drift_cal_alternation_artifact` + `rule_d_audit_pivot_reviewer` exceptions allowed.

**Production-side prevention layer EFFECTIVENESS PROVEN round 10**: v1.6 N18.a/b/d/e content-type-binding caught 0 hallucinations across 782 production atoms 6 sub-batches (round 10 batches 41/42/43 production all executor-clean). N18 EXTENDED scope ban scope was JUSTIFIED for production prevention (writer NOT dispatched for production). The 6th-recurrence was on drift cal EXECUTOR-VARIANT alternation rerun (artifact, NOT merged). N21 = formal codification of "ALL production atomization MUST be executor" extending the de-facto post-v1.6 production discipline to a hard pre-dispatch ban.

**Halt threshold for 7th recurrence**: under N21 design, writer NOT used in production = 7th-recurrence impossible by construction. BUT if NEW motif surfaces at executor-direction (round 11+), v1.8 trigger candidates surface (executor-family hardening — out-of-scope for v1.7). Round 5-10 cumulative evidence: production 9828+782=10610 atoms post-round-10 with 0 cumulative writer-direction VALUE HALLUCINATION when executor-only (when writer dispatched for production rounds 1-7 pre-N16 = 4 cumulative recurrences; post-N16 v1.5 cut = N16 PARTIAL prevented round 8+9+10 production direction recurrences but drift cal artifact still surfaced rounds 9+10 on EXECUTOR-VARIANT alternation = direction-attribution-validation purpose only).

═══════════════════════════════════════════════════════════════════
## v1.7 SECONDARY decisions (N22 + N23)
═══════════════════════════════════════════════════════════════════

### §N22 Hook 18 SENTENCE-paragraph-concat WARN-mode SUSTAINED (decision: keep WARN-mode, recommend executor narrative-chapter exemplar refinement)

**Source**: round 9 + round 10 cumulative 5+ PARTIAL atoms on SENTENCE-paragraph-concat motif (round 9 batch 39 4 PARTIAL + round 9 batch 40 1 PARTIAL ig34_p0391_a002 + round 10 batch 42 11 WARN candidates non-blocking). v1.6 Hook 18 WARN-mode codification working as designed.

**Decision options considered for v1.7** (per handoff §3.1):
- (a) Promote to halt-on-violation: regex `\.\s+[A-Z]` match (multi-sentence concat detected) → halt
- (b) **Keep WARN-mode** + add narrative-chapter exemplar refinement to executor prompt — RECOMMENDED
- (c) Reaffirm unchanged: minimal change

**Decision: option (b) — keep WARN-mode**. Justification: under N21, writer-family deprecated entirely; executor-family round 9+10 cumulative SENTENCE-paragraph-concat motif rate may be lower (Rule A PASS-rate 95%+ suggests soft motif, not blocking quality). Hook 18 WARN-mode acceptable. Executor narrative-chapter exemplar refinement: when emitting SENTENCE atoms in narrative chapters, prefer 1-sentence-per-atom split (carry-forward v1.6 §N19 exemplar — wording carry-forward unchanged but applied to executor-only context post N21).

**Rule v1.7 N22**: Hook 18 SENTENCE-paragraph-concat WARN-mode codification carry-forward from v1.6 §N19 unchanged. Executor narrative-chapter exemplar in writer prompt §N19 sustained (writer prompt deprecated for production under N21 but exemplar text reused for executor reference).

### §N23 Hook 19 PDF-cross-verify N=10 + mandatory URL/DOI/citation cross-check RENDERED MOOT by N21 (decision: N20 Hook 19 carry-forward unchanged; no further escalation needed)

**Source**: round 9 batch 39 + round 10 batch 42 = 2 cumulative writer self-claim "all hooks PASS" disproven by main-session post-rerun PDF cross-check (round 9 caught 3 hallucinated atoms; round 10 caught 5+ hallucinated atoms incl. TABLE_HEADER fabrication). Hook 19 N=10 sample expansion + mandatory URL/DOI/citation cross-check INSUFFICIENT to catch column-name fabrication or cell-value drift when applied to writer outputs.

**Decision options considered for v1.7** (per handoff §3.2):
- (a) Full-table cross-verify mandatory: ALL TABLE_HEADER + TABLE_ROW atoms (no sample, full population) → halt-on-violation per any cell-value or column-name discrepancy. High overhead but eliminates writer self-claim trust gap.
- (b) **Rendered moot by N21** — RECOMMENDED. Under writer-family deprecation, executor-family Hook 19 self-claim trust profile differs (executor doesn't exhibit fabrication motif per round 5-10 cumulative evidence: production 10610 atoms post-round-10 executor-only = 0 cumulative writer-direction VALUE HALLUCINATION at executor-direction).
- (c) Promote sample N=10 → N=20 + add table-axis stratification: middle ground

**Decision: option (b) — N23 RENDERED MOOT by N21**. Justification: executor self-claim trust profile validated cumulative round 5-10 (production 10610 atoms post-round-10 executor-only = 0 cumulative writer-direction VALUE HALLUCINATION at executor-direction). N23 codification deferred to v1.8 if executor-family ever exhibits motif. v1.6 §N20 Hook 19 N=10 + mandatory URL/DOI/citation cross-check carry-forward unchanged for executor (sustains preventive discipline; post-N21 motif probability low but defense-in-depth retained).

**Rule v1.7 N23**: v1.6 §N20 Hook 19 carry-forward unchanged. No additional escalation needed under N21.

═══════════════════════════════════════════════════════════════════
## OBS items (v1.6 carry-forward, no NEW v1.7 OBS items)
═══════════════════════════════════════════════════════════════════

参 v1.6 §OBS items absorbed (OBS-1/2/3/4 + Item Z all absorbed in v1.5/v1.6 cuts; carry-forward unchanged in v1.7).

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks final list (v1.7 = 20 hooks unchanged, Hook 16.6 → 16.7)
═══════════════════════════════════════════════════════════════════

1-9 (P0 v1.1 base): atom_id format / atom_type 9-enum / verbatim non-empty / parent_section non-empty / heading fields / page-region / cross-refs valid / extracted_by required / output_file JSONL strict
10-14 (v1.4 base): R10 verbatim no-paraphrase / R14 wc -l / N3 NEW8.d whole-row VALUE check / N5 TABLE_ROW pipe-count / N6 INTRA-AGENT consistency
14.5 (v1.5 per N15): .xpt-parent FORBID assert
15-17 (v1.5 per N17): cross-row TABLE_ROW pipe-count / cross-row USUBJID format / multi-axis value-cell spot-check N=3
16.5 (v1.5 per N16): content-type-aware dispatch assert (pre-dispatch)
**16.7 (v1.7 NEW per N21, REPLACES v1.6 Hook 16.6)**: writer-family complete deprecation assert (pre-dispatch for `production_atomization`; `drift_cal_alternation_artifact` + `rule_d_audit_pivot_reviewer` exceptions)
18 (v1.6 per N19): SENTENCE-paragraph-concat detection (pre-DONE WARN-mode) — carry-forward unchanged
19 (v1.6 per N20): PDF-cross-verify expansion N=3→N=10 + mandatory URL/DOI/citation cross-check — carry-forward unchanged
20 (v1.6 per OBS-4): Hook 15 (parent_section, table_id) granularity refinement — carry-forward unchanged

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.7 carry-forward + 2 NEW)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post **4th live-fire** sustained (round 7 batch 33 + round 8 batch 36 + round 9 batch 39 + round 10 batch 42) — production-ready protocol sustained at 4 cumulative live-fires.
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post **3rd live-fire** sustained (round 7 batch 32 + round 8 batch 36 + round 10 batch 42) — production-ready protocol sustained at 3 cumulative live-fires.
- **N9 + N10 leaf-pattern codifications**: graduated **CROSS-LEAF-DOMAIN VALIDATED post 4th live-fire** (round 8 batch 37 FA + round 9 batch 38 SR + round 9 batch 39 TA + round 10 TD/TM/TI/TS = 4-leaf-domain cumulative).
- **N11 chapter-short-bracket extension**: L1+L2+L3 FULL-SCOPE VALIDATED + 1 NEW L2 transition round 10 batch 42 §7.4 [TRIAL ELIGIBILITY AND SUMMARY (TI AND TS)] — sustained.
- **N18 EXTENDED scope EFFECTIVENESS PROVEN production-side** (round 10 batch 42 production 217 atoms executor-clean post N18.a/b/d/e bindings) but **N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side** (round 10 batch 42 drift cal 6th recurrence on N18.a-banned content type) → v1.7 N21 PRIMARY trigger justified.
- **NEW v1.7**: **N21 writer-family complete deprecation** (replaces N16 + N18 partial bans).

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1 | 2026-04-24 | initial P0 Pilot prompt |
| v1.2 | 2026-04-24 | post-P0 收官: schema frozen + 6-item fix matrix |
| v1.3 | 2026-04-27 | post P1 round 4 cut: 13 items A-M codified |
| v1.4 | 2026-04-28 | post P1 round 7 cut EMERGENCY-CRITICAL: 14 NEW patches N1-N14 |
| v1.5 | 2026-04-28 | post P1 round 8 cut: 3 NEW patches N15-N17 + STRONGLY VALIDATED status promotions N14 + G-MS-4 |
| v1.6 | 2026-04-29 | post P1 round 9 cut EMERGENCY-CRITICAL: 3 NEW patches N18-N20 + Self-Validate hooks 17→20 + STATUS PROMOTIONS N14 STRONGLY VALIDATED 3rd + N9+N10 CROSS-LEAF-DOMAIN VALIDATED |
| **v1.7** | **2026-04-29** | **post P1 round 10 cut EMERGENCY-CRITICAL**: (a) 1 NEW writer-side patch N21 codifying round 10 v1.7 PRIMARY trigger: **N21 EMERGENCY-CRITICAL writer-family complete deprecation entirely from P1 production atomization across ALL content types** (replaces N16 v1.5 partial ban + N18 v1.6 EXTENDED partial ban with COMPLETE ban) post 6th cumulative writer-direction VALUE HALLUCINATION recurrence on examples_narrative_spec_table content type DESPITE v1.6 N18.a EXPLICITLY BANS (round 10 batch 42 p.412 TABLE_HEADER fabrication NEW MODE + TABLE_ROW value fabrication = O-P1-145 HIGH); 2 SECONDARY decisions: **N22 Hook 18 SENTENCE-paragraph-concat WARN-mode SUSTAINED** (option b: keep WARN-mode + executor narrative-chapter exemplar refinement) per round 9+10 cumulative 5+ PARTIAL atoms non-blocking + **N23 Hook 19 PDF-cross-verify RENDERED MOOT by N21** (option b: executor self-claim trust profile validated cumulative round 5-10 production 10610 atoms 0 cumulative writer-direction VALUE HALLUCINATION at executor-direction; v1.6 §N20 carry-forward unchanged for defense-in-depth); (b) Self-Validate hooks 20 unchanged but Hook 16.6 → 16.7 substitution (simplified pre-dispatch ban replaces v1.6 5-sub-rule a-e check with simpler total ban + drift_cal_alternation + rule_d_audit_pivot exceptions); (c) REMOVE v1.6 N18 input fields `n18_url_atoms_count` + `n18_long_cell_atoms_count` (redundant under N21); (d) STATUS PROMOTIONS sustained N14 STRONGLY VALIDATED 4th + G-MS-4 STRONGLY VALIDATED 3rd + N9+N10 CROSS-LEAF-DOMAIN VALIDATED 4th + N11 L1+L2+L3 FULL-SCOPE VALIDATED + 1 NEW v1.7 status N18 EXTENDED scope EFFECTIVENESS PROVEN production-side + N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side; (e) v1.6 archived `archive/v1.6_final_2026-04-29/`. NOT behavior change for executor — writer task structure (Step 1-8 with Hook 16.7 substitution) / DONE format / atom_type 9-enum / heading semantic 全 carry-forward unchanged; only writer-family eligibility scope changed. **Halt threshold for 7th recurrence**: under N21 design (writer NOT used in production), 7th-recurrence impossible by construction. If NEW motif surfaces at executor-direction (round 11+), v1.8 trigger candidates surface (executor-family hardening — out-of-scope for v1.7). |
