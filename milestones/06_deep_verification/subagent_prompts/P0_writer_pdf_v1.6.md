# P0 Writer PDF — 原子化 prompt v1.6

> Version: v1.6 (2026-04-29, post P1 round 9 cut — formal codification of round 9 5 cumulative v1.6 candidates)
> 基于 v1.5 (2026-04-28 round 8 cut + 3 NEW patches N15-N17 + STRONGLY VALIDATED status N14 + G-MS-4) + round 9 (batches 38/39/40) cumulative candidates
> 角色: Writer (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.6 变更 over v1.5: **EMERGENCY-CRITICAL N16 scope ESCALATION + SENTENCE-paragraph-concat Hook 18 + writer pre-DONE PDF-cross-verify expansion.** Schema link + 13 §A-M v1.3 base + 14 §N1-N14 v1.4 patches + 3 §N15-N17 v1.5 patches 全 carry-forward unchanged. v1.6 把 round 9 5 候选固化进 prompt; 3 NEW writer-side patches N18-N20 加在 §A-Y codified base 之上 + Self-Validate 扩 17 → 20 hooks + Changelog. POST 5th cumulative writer-direction main-line VALUE HALLUCINATION recurrence on **mixed_structural_transition** content type DESPITE N16 v1.5 PERMISSION (round 9 batch 39 p.382 URL `.org→.ch` + word `clinical` deletion + TABLE_ROW Study cell ~26% TRUNCATION+REORDER) ESCALATED to writer-family ban EXTENDED SCOPE per N18 (URLs/citations/long-cell-content NOT just Examples-narrative + spec-table).

## 角色硬约束 (v1.5 carry-forward unchanged)

参 `archive/v1.5_final_2026-04-29/P0_writer_pdf_v1.5.md` §角色硬约束 + v1.4 baseline carry-forward 全文.

## 派发 subagent_type (v1.6 N18 EXTENDED writer-family ban scope)

**v1.5 carry-forward N16 base**: 主 session dispatch MUST cross-check **content type** of target page(s) BEFORE selecting writer-family.

**🔴 v1.6 N18 EMERGENCY-CRITICAL EXTENSION (post 5th cumulative writer-direction VALUE HALLUCINATION recurrence DESPITE N16 v1.5 PERMISSION on `mixed_structural_transition`)**:

| Content type / Pattern | v1.5 N16 dispatch | v1.6 N18 EXTENDED dispatch | Justification |
|---|---|---|---|
| **Examples-narrative + spec-table** (carry-forward N16) | executor MANDATORY | executor MANDATORY (carry-forward) | round 5+6+7+8 4 cumulative recurrences |
| **SENTENCE atoms with URLs (regex `https?://`) or DOI references** | free choice | **executor MANDATORY (writer-family BANNED, NEW v1.6 N18.b)** | round 9 batch 39 p.382 URL `.org→.ch` fabrication = writer-direction VALUE HALLUCINATION on URL content where verbatim drift fabricates wrong domain |
| **TABLE_ROW atoms with cell content ≥500 chars** | free choice | **executor MANDATORY (writer-family BANNED, NEW v1.6 N18.c)** | round 9 batch 39 p.382 Study cell 1032→758 chars TRUNCATION + REORDER = writer-direction VALUE HALLUCINATION on long-cell content where verbatim drift truncates ~26% |
| **SENTENCE / TABLE_ROW with DOI, citation, identifier, or other VERBATIM-CRITICAL fact** | free choice | **executor MANDATORY (writer-family BANNED, NEW v1.6 N18.d)** | generalization clause — any content where verbatim drift could fabricate identifier/citation values |
| **SENTENCE-paragraph + LIST_ITEM-heavy** (no URLs/long-cells) | free choice | free choice (carry-forward) | No systematic family-direction motif on this content |
| **Mixed structural transition pages** (R12 transition zones / chapter NEW transitions) | executor PREFERRED | **executor MANDATORY (NEW v1.6 N18.e — was PREFERRED, now MANDATORY)** | round 9 batch 39 p.382 §7 L1 NEW chapter transition page = mixed_structural_transition where 5th cumulative writer-direction VALUE HALLUCINATION occurred — N16 v1.5 PREFERRED was insufficient, must MANDATE |

**Effect**: v1.6 reduces writer-family permissible content to **SENTENCE-paragraph + LIST_ITEM-heavy ONLY** (no URLs / no long-cells / no Examples-narrative + spec-table / no mixed_structural_transition). All other content types REQUIRE executor.

**Pre-dispatch validation (v1.6 NEW Hook 16.6)**: main session pre-dispatch MUST scan target page(s) for URL/DOI/long-cell/Examples-narrative/spec-table/structural-transition motifs. If ANY found → executor MANDATORY assert.

```python
# v1.6 NEW Hook 16.6 pre-dispatch pseudo-code (covers all 5 sub-rules a-e)
if content_type_hint in ("examples_narrative_spec_table", "mixed_structural_transition"):
    assert subagent_type == "oh-my-claudecode:executor", "N18.a/e violation"
if content_has_urls or content_has_dois:
    assert subagent_type == "oh-my-claudecode:executor", "N18.b violation"
if any(table_row.cell_content_len >= 500 for table_row in pages):
    assert subagent_type == "oh-my-claudecode:executor", "N18.c violation"
# N18.d general VERBATIM-CRITICAL clause — main session judgment per pre-dispatch scan
if has_citations or has_identifiers or has_other_verbatim_critical_facts:
    # main session judgment: SENTENCE / TABLE_ROW with citation / identifier / VERBATIM-CRITICAL fact
    # examples: scientific citation patterns `\b\w+\s+et\s+al\.?\b`, `\(\w+\s+\d{4}\)`,
    #           clinical trial registry IDs (NCT*), publication identifiers, regulatory codes
    assert subagent_type == "oh-my-claudecode:executor", "N18.d violation"
```

**Halt threshold for 6th cumulative recurrence**: if drift cal subsequent batch reveals 6th cumulative writer-direction main-line VALUE HALLUCINATION recurrence DESPITE N18 EXTENDED scope, ESCALATE to **mandatory writer-family ban for ALL content types** (essentially deprecating writer-family from P1 atomization workflow).

## 输入 (v1.5 carry-forward + v1.6 NEW N18 scan output)

参 v1.5 §输入. v1.6 NEW input field:
- `n18_url_atoms_count` (int): main-session pre-dispatch scan result count of atoms with URL/DOI in verbatim
- `n18_long_cell_atoms_count` (int): main-session pre-dispatch scan result count of TABLE_ROW atoms with cell content ≥500 chars

If either > 0, executor MANDATORY assert per N18.b/c.

## 任务流程 (v1.5 carry-forward + v1.6 N19 + N20 NEW steps)

参 v1.5 §任务流程 7 steps. v1.6 NEW step 8:
8. **(v1.6 NEW per N19 + N20)** Pre-DONE final validation pass:
   - **Hook 18 (NEW per N19)**: SENTENCE-paragraph-concat detection — for each SENTENCE atom, regex search `\.\s+[A-Z]` (period + whitespace + uppercase) inside verbatim. If match found AND atom_type=SENTENCE: WARN ("possible paragraph-concat motif: split into multiple SENTENCE atoms per atom_schema notes line 180 each sentence should be its own atom"). v1.6 stage = WARN-mode (round 9 5 PARTIAL findings = motif active but not blocking; v1.7 may promote to halt-on-violation).
   - **Hook 19 (NEW per N20)**: PDF-cross-verify sample expansion — pre-DONE PDF-cross-verify sample expand from N=3 (v1.5 N17 Hook 17) to **N=10 random TABLE_ROW + SENTENCE atoms per sub-batch** (was N=3); + MANDATORY cross-check for ALL atoms with URLs/DOIs (regex match) regardless of sample (was sample-only). Halt-on-violation per any URL/citation discrepancy.
   - **Hook 20 (NEW per OBS-4)**: Hook 15 cross-row TABLE_ROW pipe-count consistency refinement to (parent_section, table_id) granularity (was per-parent_section only) — distinguishes Trial Design Matrix 5-pipe + ta.xpt 12-pipe under same `§7.2.1 Trial Arms (TA) – Example N` parent. Per-table internal pipe-count enforced PER TABLE_HEADER scope (not per parent_section).

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.5 carry-forward §A-Y, FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.5_final_2026-04-29/P0_writer_pdf_v1.5.md` for full §A-Y text:
- §A R1-R15 (15 累 R-rules) — v1.3 base + v1.4 N5/N13 hardening + v1.5 carry-forward
- §B-§M v1.3 base codifications
- §N1-N14 v1.4 NEW patches
- §N15-N17 v1.5 NEW patches (.xpt-parent FORBID + writer-family ban Examples-narrative+spec-table + post-extraction VALIDATION pass Self-Validate hooks 14→17)

═══════════════════════════════════════════════════════════════════
## v1.6 NEW PATCHES (N18-N20, codifying 5 round 9 v1.6 candidates)
═══════════════════════════════════════════════════════════════════

### §N18 EMERGENCY-CRITICAL writer-family ban EXTENDED scope (per round 9 batch 39 5th cumulative writer-direction VALUE HALLUCINATION on mixed_structural_transition DESPITE N16 PERMISSION = O-P1-134 HIGH)

**Source**: round 9 batch 39 p.382 drift cal NEW1 dual-threshold 9th time FAIL — 5th cumulative writer-direction main-line VALUE HALLUCINATION recurrence on `mixed_structural_transition` content type. v1.5 N16 v1.5 PERMITS writer-family for mixed_structural_transition (PREFERRED executor); writer was dispatched per N16 PERMISSION NOT in violation. 3 specific HIGH hallucinations PDF-verified by main session post drift cal:
- ig34_p0382_a004 SENTENCE: URL `http://www.ich.org/products/guidelines/` → fabricated `http://www.ich.ch/products/guidelines/` (`.org → .ch` Switzerland TLD plausible but FACTUALLY WRONG; ICH actual domain is `ich.org`)
- ig34_p0382_a017 SENTENCE: WORD DELETION (`clinical` dropped from "definitions of clinical trial and objective" → "definitions of trial and objective")
- ig34_p0382_a022 TABLE_ROW Study cell: TEXT TRUNCATION + REORDER 1032→758 chars (~26% drift; baseline matches PDF, rerun truncated and reordered middle content about treatment strategy)

**Conclusion**: writer-direction VALUE HALLUCINATION extends BEYOND examples_narrative+spec-table content type to URLs / sentence content / long-cell TABLE_ROW content. **N16 v1.5 ban scope INSUFFICIENT proof.**

**Rule v1.6 N18**: writer-family BANNED for any of:
- (a) carry-forward Examples-narrative + spec-table content type [per N16 v1.5]
- (b) SENTENCE atoms with URLs (regex `https?://`) or DOI references (regex `\b10\.\d{4,9}/`)
- (c) TABLE_ROW atoms with cell content ≥500 chars
- (d) SENTENCE / TABLE_ROW with citation, identifier, or other VERBATIM-CRITICAL fact (generalization clause — main session judgment per pre-dispatch scan)
- (e) mixed_structural_transition pages (was PREFERRED in v1.5, now MANDATORY)

Executor-family MANDATORY for ALL above. Writer-family permitted ONLY for **SENTENCE-paragraph + LIST_ITEM-heavy** content with NO URLs / NO long-cells / NO transitions.

**Self-Validate hook (NEW Hook 16.6 pre-dispatch)**: pseudo-code in §派发 above. Halt-on-violation pre-dispatch.

**Halt threshold for 6th recurrence**: deprecate writer-family entirely from P1 atomization (v1.7 candidate trigger).

### §N19 SENTENCE-paragraph-concat detection Hook 18 (per round 9 O-P1-133 MEDIUM + Item Z)

**Source**: round 9 batch 39 Rule A 4 PARTIAL atoms (atoms 6/8/9 SENTENCE + atom 3 TABLE_ROW with cell-internal bullets) collapse multi-sentence prose paragraphs into single SENTENCE atoms. Per atom_schema notes line 180: "each sentence should be its own atom". Currently md-codified rule only, not PDF-side hard-enforced. Round 9 batch 40 atom ig34_p0391_a002 also surfaced same motif (1 PARTIAL).

**Rule v1.6 N19**: pre-DONE Hook 18 NEW — for each SENTENCE atom, regex search `\.\s+[A-Z]` (period + whitespace + uppercase) inside verbatim. If match found AND atom_type=SENTENCE: WARN ("possible paragraph-concat motif: split into multiple SENTENCE atoms per atom_schema notes line 180 each sentence should be its own atom"). 

**v1.6 stage**: WARN-mode only (no halt). Round 9 had 5 PARTIAL findings = motif active but not blocking quality. v1.7 may promote to halt-on-violation if motif persists.

**Writer prompt narrative-chapter exemplar** (for §N19): when emitting SENTENCE atoms in narrative chapters, prefer 1-sentence-per-atom split. Example:
- WRONG (paragraph concat): atom verbatim = "The Trial Arms domain represents study arms. Each arm is identified by ARM and ARMCD. Subjects are assigned to arms via DM domain."
- CORRECT (1-sentence-per-atom): emit 3 SENTENCE atoms, one per sentence.

### §N20 Writer pre-DONE PDF-cross-verify expansion (per round 9 OBS-5 + drift cal Hook 17 detection-not-prevention)

**Source**: round 9 batch 39 drift cal — writer self-claimed "17/17 hooks PASS" but PDF cross-check disproved 3 atoms in drift cal rerun. Hook 17 spot-check sample N=3 missed all 3 hallucinated atoms (URL + word deletion + TABLE_ROW truncation). Hooks are detection-not-prevention; need wider sample OR mandatory cross-check for high-risk content.

**Rule v1.6 N20**: pre-DONE PDF-cross-verify expansion:
- **Sample expansion**: Hook 17 (v1.5) sample N=3 → **N=10** random atoms per sub-batch (was 3, now 10). Sample stratified across atom_types.
- **Mandatory cross-check**: ALL atoms with URLs (regex `https?://`), DOIs (regex `\b10\.\d{4,9}/`), or citations (regex `\b\w+\s+et\s+al\.?\b` or `\(\w+\s+\d{4}\)`) — regardless of sample inclusion. Halt-on-violation per any URL/DOI/citation discrepancy with PDF source.
- **Long-cell TABLE_ROW** (cell content ≥500 chars): same mandatory cross-check, halt-on-violation per content drift.

**Self-Validate hook (NEW Hook 19)**: described in §任务流程 step 8 above. Halt-on-violation for URL/DOI/citation/long-cell discrepancy.

═══════════════════════════════════════════════════════════════════
## OBS items absorbed (v1.5 cut codex audit + round 9 OBS-1/2/3/4 + Item Z)
═══════════════════════════════════════════════════════════════════

- **OBS-1 reviewer item W verification grep tightening** (v1.5 cut codex audit OBS-1): reviewer-side prompt §Step 2 item W verification — grep target parent_section field-only (avoid false positives matching `.xpt` strings in verbatim/notes). Reviewer-side codification — see P0_reviewer_v1.6.md §Step 2 item W tightening.
- **OBS-2 sweep count source-of-truth normalization** (v1.5 cut codex audit OBS-2): all referencing files (audit_matrix.md / _progress.json / CLAUDE.md / MANIFEST.md) MUST use **35 atoms cumulative** as canonical retroactive sweep count (NOT 36 / NOT 9 / NOT 27 alone). Reviewer-side codification — see P0_reviewer_v1.6.md §Step 2.
- **OBS-3 slot ordinal vs cumulative total derivation** (v1.5 cut codex audit OBS-3): kickoff §0/§1 + audit_matrix.md narrative MUST distinguish "slot N" (sequential numbering 1, 2, ..., N) from "AUDIT pivot Mth cumulative" (counts only AUDIT-mode-pivot burns excluding writer/matcher non-AUDIT slots). Reviewer-side codification — see P0_reviewer_v1.6.md §Step 2.
- **OBS-4 N17 Hook 15 (parent_section, table_id) granularity** (round 9 batch 39 schema sweep OBS-4): codified in §N20 Hook 20 above + P0_writer_pdf_v1.6.md §任务流程 step 8.
- **Item Z SENTENCE-paragraph-concat Hook 18** (round 9 O-P1-133 MEDIUM + batch 40 ig34_p0391_a002 PARTIAL): codified in §N19 above.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks final list (v1.6 = 20 hooks)
═══════════════════════════════════════════════════════════════════

1-9 (P0 v1.1 base): atom_id format / atom_type 9-enum / verbatim non-empty / parent_section non-empty / heading fields / page-region / cross-refs valid / extracted_by required / output_file JSONL strict
10-14 (v1.4 base): R10 verbatim no-paraphrase / R14 wc -l / N3 NEW8.d whole-row VALUE check / N5 TABLE_ROW pipe-count / N6 INTRA-AGENT consistency
14.5 (v1.5 per N15): .xpt-parent FORBID assert
15-17 (v1.5 per N17): cross-row TABLE_ROW pipe-count / cross-row USUBJID format / multi-axis value-cell spot-check N=3
16.5 (v1.5 per N16): content-type-aware dispatch assert (pre-dispatch)
**16.6 (v1.6 NEW per N18)**: writer-family ban EXTENDED scope assert (pre-dispatch URL/DOI/long-cell/transition)
**18 (v1.6 NEW per N19)**: SENTENCE-paragraph-concat detection (pre-DONE WARN-mode)
**19 (v1.6 NEW per N20)**: PDF-cross-verify expansion N=3→N=10 + mandatory URL/DOI/citation cross-check
**20 (v1.6 NEW per OBS-4)**: Hook 15 (parent_section, table_id) granularity refinement

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.6 carry-forward + 1 NEW)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post 3rd live-fire (round 7 batch 33 1st + round 8 batch 36 2nd + round 9 batch 39 3rd) — production-ready protocol sustained at 3 cumulative live-fires.
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post 2nd live-fire sustained (NOT triggered round 9; carry-forward unchanged).
- **N9 + N10 leaf-pattern codifications** (NEW v1.6 promotion): graduate from "1st-live-fire-EFFECTIVE" → **"CROSS-LEAF-DOMAIN VALIDATED post 3rd live-fire"** (round 8 batch 37 FA + round 9 batch 38 SR + round 9 batch 39 TA = 3 cumulative leaf-domain validations clean first-attempt).

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
| **v1.6** | **2026-04-29** | **post P1 round 9 cut EMERGENCY-CRITICAL**: (a) 3 NEW writer-side patches N18-N20 covering 5 round 9 v1.6 candidates: **N18 EMERGENCY-CRITICAL writer-family ban EXTENDED scope** (was Examples-narrative+spec-table only per v1.5 N16; now extends to URLs/DOIs + TABLE_ROW ≥500 chars + mixed_structural_transition MANDATORY + general VERBATIM-CRITICAL clause) post 5th cumulative writer-direction VALUE HALLUCINATION recurrence on mixed_structural_transition DESPITE N16 v1.5 PERMISSION (O-P1-134 HIGH); **N19 SENTENCE-paragraph-concat Hook 18** WARN-mode pre-DONE detection per O-P1-133 MEDIUM + 5 PARTIAL atoms cumulative round 9; **N20 PDF-cross-verify expansion N=3→N=10 + mandatory URL/DOI/citation cross-check** per OBS-5 detection-not-prevention escalation; (b) Self-Validate hooks 17→20 (NEW Hook 16.6 pre-dispatch + Hook 18 paragraph-concat + Hook 19 PDF-cross-verify + Hook 20 (parent_section, table_id) granularity refinement); (c) STATUS PROMOTIONS N14 STRONGLY VALIDATED post 3rd live-fire + N9+N10 CROSS-LEAF-DOMAIN VALIDATED post 3rd live-fire; (d) absorbed OBS-1/2/3/4/5 from v1.5 cut codex audit + round 9 schema sweep + drift cal; (e) v1.5 archived `archive/v1.5_final_2026-04-29/`. NOT behavior change — writer task structure (Step 1-8) / DONE format / atom_type 9-enum / heading semantic 全 carry-forward unchanged. **Halt threshold for 6th recurrence**: deprecate writer-family entirely from P1 atomization (v1.7 trigger). |
