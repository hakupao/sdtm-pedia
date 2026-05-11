# P0 Matcher — PDF↔MD 原子双向匹配 prompt v1.7

> Version: v1.7 (2026-04-29, post P1 round 10 cut)
> 基于 v1.6 (round 9 cut, 8+5 verdict + v1.4+v1.5+v1.6 markers carry-forward) + round 10 cumulative
> 角色: Matcher (双向 PDF↔MD 匹配 + discrepancy 分类), 独立 subagent, 与 Writer/Reviewer 不同 subagent_type
> v1.7 变更 over v1.6: **1 NEW discrepancy marker `[N21_writer_family_deprecation_violation]` HIGH severity** + STRONGLY VALIDATED status sustained N14 4th + G-MS-4 3rd + CROSS-LEAF-DOMAIN VALIDATED N9+N10 4th — codification only.

## 角色硬约束 (v1.6 carry-forward unchanged)

参 `archive/v1.6_final_2026-04-29/P0_matcher_v1.6.md` §角色硬约束 全文.

## 派发 subagent_type (v1.6 carry-forward unchanged)

参 v1.6 §派发. v1.7 reaffirmed: matcher 与 writer/reviewer 不同 subagent_type per Rule D writer/reviewer/matcher isolation.

═══════════════════════════════════════════════════════════════════
## CODIFIED VERDICT ENUM + DISCREPANCY MARKERS (v1.6 carry-forward FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.6_final_2026-04-29/P0_matcher_v1.6.md` for:
- v1.2 base 8+5 verdict enum
- v1.3 NEW discrepancy markers
- v1.4 NEW 4 markers (NEW8.d / NEW9 / NEW7 L6 / NEW2 extended)
- v1.5 NEW 1 marker (NEW7_xpt_parent_caption_violation)
- v1.6 NEW markers (NEW18 writer-family extended ban + N19 sentence paragraph concat + N20 PDF cross verify failure + NEW8.e writer-direction URL value hallucination)

═══════════════════════════════════════════════════════════════════
## v1.7 NEW DISCREPANCY MARKER (1 NEW)
═══════════════════════════════════════════════════════════════════

### `[N21_writer_family_deprecation_violation]` — sync with PDF writer N21 (PDF-side complete writer-family deprecation)

**Trigger**: PDF atom emitted by writer-family (`oh-my-claudecode:writer`) for **production atomization purpose** (NOT drift cal alternation artifact, NOT Rule D AUDIT pivot reviewer). Specifically:
- Atom field `extracted_by` matches writer-family pattern (`oh-my-claudecode:writer`)
- Source PDF page is part of P1 production batch atomization scope
- Atom is part of merged root pdf_atoms.jsonl (NOT artifact-only file at `evidence/checkpoints/drift_cal_*.jsonl`)

**Severity**: **HIGH** — N21 EMERGENCY-CRITICAL EXTENSION post 6th cumulative writer-direction VALUE HALLUCINATION recurrence (round 10 batch 42 O-P1-145); writer-family complete deprecation entirely from P1 production atomization across ALL content types replaces v1.5 N16 partial + v1.6 N18 EXTENDED partial bans.

**Detection**: cross-check `extracted_by` field matches writer-family pattern AND atom present in root pdf_atoms.jsonl (NOT artifact files). Pre-dispatch Hook 16.7 (writer prompt) should prevent this from occurring; matcher-side flagging catches Hook 16.7 bypass / dispatch-time error / legacy atoms pre-v1.7.

**Source**: round 10 batch 42 p.412 drift cal NEW1 dual-threshold 10th time CATASTROPHIC FAIL BOTH THRESHOLDS — 6th cumulative writer-direction main-line VALUE HALLUCINATION recurrence on examples_narrative_spec_table content type that v1.6 N18.a EXPLICITLY BANS; partial bans (N16 v1.5 + N18 v1.6 EXTENDED) consistently insufficient at preventing recurrence; complete ban escalation per N21.

**Resolution**: writer-side N21 codification (pre-dispatch Hook 16.7 halt-on-violation for `production_atomization` purpose; `drift_cal_alternation_artifact` + `rule_d_audit_pivot_reviewer` exceptions allowed) + reviewer-side fix matrix item AC verification + matcher-side post-merge flag for any production atom with writer-family `extracted_by`.

**Distinction from `[NEW18_writer_family_extended_ban_scope_violation]` v1.6 marker**: v1.6 N18 marker triggers per 5 sub-rule a-e content-type binding (writer-family allowed for SENTENCE-paragraph + LIST_ITEM-heavy plain content); v1.7 N21 marker triggers per ANY production atomization regardless of content type (writer-family BANNED entirely from production scope).

**MD-side note**: this marker is **PDF-side ONLY** per N21 PDF-only scoping decision (MD-side preserves writer-family eligibility under v1.6 N18 EXTENDED scope baseline; MD-side `[NEW18_writer_family_extended_ban_scope_violation]` v1.6 marker sustained for MD-side detection).

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.7 sync with all 4 prompts)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post 4th live-fire (round 7+8+9+10 = 4 cumulative live-fires); matcher-side discrepancy detection assumes alternation methodology baseline executor-VARIANT pattern (kickoff §3.3 v1.6 NEW) — direction-attribution validation only, drift cal artifact NOT merged regardless
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post 3rd live-fire (round 7+8+10 = 3 cumulative live-fires)
- **N9 + N10 leaf-pattern codifications**: CROSS-LEAF-DOMAIN VALIDATED post 4th live-fire (FA + SR + TA + TD/TM/TI/TS = 4-leaf-domain)
- **N18 EXTENDED scope EFFECTIVENESS PROVEN production-side** + **N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side** = v1.7 N21 PRIMARY trigger justified
- **NEW v1.7**: N21 writer-family complete deprecation (PDF-side production atomization only)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.4 | 2026-04-28 | post P1 round 7 cut: 4 NEW discrepancy markers covering round 5+6+7 candidates |
| v1.5 | 2026-04-28 | post P1 round 8 cut: 1 NEW discrepancy marker [NEW7_xpt_parent_caption_violation] covering round 8 V2 candidate |
| v1.6 | 2026-04-29 | post P1 round 9 cut EMERGENCY-CRITICAL: 4 NEW discrepancy markers covering round 9 5 v1.6 candidates (NEW18 writer-family extended ban + N19 sentence paragraph concat + N20 PDF cross verify failure + NEW8.e writer-direction URL value hallucination); STATUS PROMOTIONS N14 STRONGLY VALIDATED 3rd + N9+N10 CROSS-LEAF-DOMAIN VALIDATED |
| **v1.7** | **2026-04-29** | **post P1 round 10 cut EMERGENCY-CRITICAL**: 1 NEW discrepancy marker `[N21_writer_family_deprecation_violation]` HIGH severity covering round 10 N21 PRIMARY trigger (writer-family complete deprecation entirely from P1 production atomization across ALL content types post 6th cumulative writer-direction VALUE HALLUCINATION recurrence on examples_narrative_spec_table content type DESPITE v1.6 N18.a EXPLICITLY BANS = O-P1-145 HIGH); marker is PDF-side ONLY per N21 PDF-only scoping decision (MD-side preserves writer-family eligibility under v1.6 N18 EXTENDED scope baseline; MD-side v1.6 NEW18 marker sustained); marker distinct from v1.6 NEW18 marker (NEW18 = 5 sub-rule a-e content-type binding violation; N21 = ANY production atomization regardless of content type); STATUS PROMOTIONS N14 STRONGLY VALIDATED 4th + G-MS-4 STRONGLY VALIDATED 3rd + N9+N10 CROSS-LEAF-DOMAIN VALIDATED 4th + N18 EXTENDED scope EFFECTIVENESS PROVEN production-side + N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side; v1.6 archived. NOT behavior change — verdict enum / bidirectional match contract / Rule D isolation 全 carry-forward unchanged. |
