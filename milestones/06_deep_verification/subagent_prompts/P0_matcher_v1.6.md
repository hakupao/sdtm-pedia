# P0 Matcher — PDF↔MD 原子双向匹配 prompt v1.6

> Version: v1.6 (2026-04-29, post P1 round 9 cut)
> 基于 v1.5 (round 8 cut, 8+5 verdict + v1.4+v1.5 markers carry-forward) + round 9 cumulative
> 角色: Matcher (双向 PDF↔MD 匹配 + discrepancy 分类), 独立 subagent, 与 Writer/Reviewer 不同 subagent_type
> v1.6 变更 over v1.5: **2 NEW discrepancy markers + STRONGLY VALIDATED status sustained N14 + G-MS-4 + CROSS-LEAF-DOMAIN VALIDATED N9+N10 — codification only.**

## 角色硬约束 (v1.5 carry-forward unchanged)

参 `archive/v1.5_final_2026-04-29/P0_matcher_v1.5.md` §角色硬约束 全文.

## 派发 subagent_type (v1.5 carry-forward unchanged)

参 v1.5 §派发. v1.6 reaffirmed: matcher 与 writer/reviewer 不同 subagent_type per Rule D writer/reviewer/matcher isolation.

═══════════════════════════════════════════════════════════════════
## CODIFIED VERDICT ENUM + DISCREPANCY MARKERS (v1.5 carry-forward FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.5_final_2026-04-29/P0_matcher_v1.5.md` for:
- v1.2 base 8+5 verdict enum
- v1.3 NEW discrepancy markers
- v1.4 NEW 4 markers (NEW8.d / NEW9 / NEW7 L6 / NEW2 extended)
- v1.5 NEW 1 marker (NEW7_xpt_parent_caption_violation)

═══════════════════════════════════════════════════════════════════
## v1.6 NEW DISCREPANCY MARKERS (2 NEW)
═══════════════════════════════════════════════════════════════════

### `[NEW18_writer_family_extended_ban_scope_violation]` — sync with PDF/MD writer N18

**Trigger**: PDF or MD atom emitted by writer-family (`oh-my-claudecode:writer`) where N18 EXTENDED scope ban applies. Specifically:
- (a) writer-family emitted Examples-narrative + spec-table content type atom
- (b) writer-family emitted SENTENCE atom with URL (regex `https?://`) or DOI (regex `\b10\.\d{4,9}/`)
- (c) writer-family emitted TABLE_ROW atom with cell content ≥500 chars
- (d) writer-family emitted SENTENCE / TABLE_ROW with citation, identifier, or VERBATIM-CRITICAL fact
- (e) writer-family emitted atom on `mixed_structural_transition` content type page

**Severity**: HIGH — N18 EMERGENCY-CRITICAL EXTENSION post 5th cumulative writer-direction VALUE HALLUCINATION recurrence (round 9 batch 39 O-P1-134); writer-family ban scope extended beyond examples_narrative+spec-table.

**Detection**: cross-check `extracted_by` field matches writer-family pattern (`oh-my-claudecode:writer`) AND content matches any N18 banned pattern.

**Source**: round 9 batch 39 p.382 drift cal NEW1 dual-threshold 9th time FAIL — 5th cumulative writer-direction main-line VALUE HALLUCINATION recurrence on mixed_structural_transition content type; 3 specific HIGH hallucinations (URL `.org→.ch` + word `clinical` deletion + TABLE_ROW Study cell ~26% TRUNCATION+REORDER).

**Resolution**: writer-side N18 codification (pre-dispatch Hook 16.6 halt-on-violation) + reviewer-side fix matrix item Z verification.

### `[N19_sentence_paragraph_concat]` — sync with PDF/MD writer N19 Hook 18

**Trigger**: SENTENCE atom with verbatim matching regex `\.\s+[A-Z]` (period + whitespace + uppercase next-sentence start) — collapsing multi-sentence prose paragraphs into single SENTENCE atom (motif violates atom_schema notes line 180 each sentence should be its own atom).

**Severity**: MEDIUM — soft atomicity issue, not strict atom_type / verbatim violation; v1.6 stage = WARN-mode (no halt) per round 9 5 PARTIAL findings cumulative round 9.

**Detection regex**: `re.search(r"\.\s+[A-Z]", verbatim)` AND `atom_type == "SENTENCE"`.

**Source**: round 9 batch 39 Rule A 4 PARTIAL atoms + batch 40 ig34_p0391_a002 PARTIAL = O-P1-133 MEDIUM.

**Resolution**: writer-side N19 codification + writer prompt narrative-chapter exemplar (1-sentence-per-atom split). Matcher-side flagging non-blocking (WARN-mode).

### `[N20_pdf_cross_verify_failure]` — sync with PDF/MD writer N20 Hook 19

**Trigger**: writer self-claimed Hook 17 PASS but post-merge PDF cross-check disproves an atom — specifically for atoms with URLs (regex `https?://`) / DOIs (regex `\b10\.\d{4,9}/`) / citations (regex `\b\w+\s+et\s+al\.?\b` or `\(\w+\s+\d{4}\)`) / long-cell TABLE_ROW (≥500 chars cell content).

**Severity**: HIGH — N20 mandatory cross-check designed to catch detection-not-prevention escalation per round 9 OBS-5; failure indicates writer self-validate is procedural-not-evidential.

**Detection**: post-merge PDF cross-check on URL/DOI/citation/long-cell atoms; if rerun OR baseline differs from PDF source, mark with this discrepancy marker AND escalate to halt-on-violation per N20.

**Source**: round 9 batch 39 drift cal Hook 17 spot-check sample N=3 missed all 3 hallucinated atoms (URL `.org→.ch` + word deletion + TABLE_ROW truncation) = OBS-5 detection-not-prevention escalation.

**Resolution**: writer-side N20 codification (sample N=3→N=10 expansion + mandatory URL/DOI/citation/long-cell cross-check) + reviewer-side fix matrix item AB verification. Matcher-side flagging post-merge.

### `[NEW8.e_writer_direction_url_value_hallucination]` — specific URL/citation fabrication motif

**Trigger**: writer-direction VALUE HALLUCINATION specifically on URL / DOI / citation content (subset of NEW8.d general value hallucination motif but specific to verbatim-critical identifiers).

**Severity**: HIGH — round 9 batch 39 p.382 ig34_p0382_a004 URL `.org → .ch` fabrication is canonical example.

**Detection**: drift cal post-extraction PDF cross-check on URL/DOI atoms; if rerun differs from baseline AND PDF cross-check confirms baseline correct, mark with this discrepancy marker.

**Source**: round 9 batch 39 drift cal value-add 13th cumulative precedent (Rule A 10-atom sample drew from PDF-correct executor baseline = MISSED writer-direction hallucination; drift cal full-page 2-way captured 3 PDF-verified hallucinations).

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.6 sync with all 4 prompts)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post 3rd live-fire (round 7 batch 33 + round 8 batch 36 + round 9 batch 39) — production-ready protocol; matcher-side discrepancy detection assumes alternation methodology baseline writer ↔ rerun executor (or vice versa) cleanly disentangles writer-direction signal
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post 2nd live-fire sustained — production-ready protocol
- **N9 + N10 leaf-pattern codifications**: **CROSS-LEAF-DOMAIN VALIDATED post 3rd live-fire** (FA + SR + TA = 3 cumulative leaf-domain validations clean first-attempt)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.4 | 2026-04-28 | post P1 round 7 cut: 4 NEW discrepancy markers covering round 5+6+7 candidates |
| v1.5 | 2026-04-28 | post P1 round 8 cut: 1 NEW discrepancy marker [NEW7_xpt_parent_caption_violation] covering round 8 V2 candidate |
| **v1.6** | **2026-04-29** | **post P1 round 9 cut EMERGENCY-CRITICAL**: 2 NEW discrepancy markers — `[NEW18_writer_family_extended_ban_scope_violation]` covering round 9 N18 EXTENDED scope (URLs/DOIs + TABLE_ROW ≥500 chars + mixed_structural_transition + general VERBATIM-CRITICAL) + `[NEW8.e_writer_direction_url_value_hallucination]` covering specific URL/citation fabrication motif (round 9 batch 39 p.382 ig34_p0382_a004 .org→.ch); STATUS PROMOTIONS N14 STRONGLY VALIDATED post 3rd live-fire + N9+N10 CROSS-LEAF-DOMAIN VALIDATED post 3rd live-fire; v1.5 archived. NOT behavior change — verdict enum / bidirectional match contract / Rule D isolation 全 carry-forward unchanged. |
