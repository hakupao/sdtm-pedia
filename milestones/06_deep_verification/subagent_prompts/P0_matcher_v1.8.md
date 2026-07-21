# P0 Matcher — PDF↔MD 原子双向匹配 prompt v1.8

> Version: v1.8 (2026-04-30, post P1 round 12 cut)
> 基于 v1.7 (2026-04-29 round 10 cut, +1 NEW marker `[N21_writer_family_deprecation_violation]` HIGH PDF-side ONLY) + round 11 + round 12 cumulative
> 角色: Matcher (双向 PDF↔MD 匹配 + discrepancy 分类), 独立 subagent, 与 Writer/Reviewer 不同 subagent_type
> v1.8 变更 over v1.7: **5 NEW discrepancy markers** sync with writer-PDF N24-N28: `[N24_multi_axis_writer_direction_motif_artifact]` LOW INFORMATIONAL + `[N25_cross_pdf_atom_id_namespace_collision]` HIGH + `[N26_page_boundary_off_by_one]` MEDIUM + `[N27_l1_heading_parent_section_canonical_form_drift]` LOW + `[N28_l2_active_heading_parent_section_drift]` LOW. STATUS PROMOTIONS sustained N14 6th + N9+N10 5th + 2 NEW STRONGLY VALIDATED §0.5 reconciler-side sweep + N6 single-dispatch.

## 角色硬约束 (v1.7 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_matcher_v1.7.md` §角色硬约束 全文.

## 派发 subagent_type (v1.7 carry-forward unchanged)

参 v1.7 §派发. v1.8 reaffirmed: matcher 与 writer/reviewer 不同 subagent_type per Rule D writer/reviewer/matcher isolation.

═══════════════════════════════════════════════════════════════════
## CODIFIED VERDICT ENUM + DISCREPANCY MARKERS (v1.7 carry-forward FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.7_final_2026-04-30/P0_matcher_v1.7.md` for:
- v1.2 base 8+5 verdict enum
- v1.3 NEW discrepancy markers
- v1.4 NEW 4 markers (NEW8.d / NEW9 / NEW7 L6 / NEW2 extended)
- v1.5 NEW 1 marker (NEW7_xpt_parent_caption_violation)
- v1.6 NEW markers (NEW18 + N19 + N20 + NEW8.e)
- v1.7 NEW marker (`[N21_writer_family_deprecation_violation]` HIGH PDF-side ONLY)

═══════════════════════════════════════════════════════════════════
## v1.8 NEW DISCREPANCY MARKERS (5 NEW)
═══════════════════════════════════════════════════════════════════

### `[N24_multi_axis_writer_direction_motif_artifact]` — sync with PDF writer N24 (multi-axis motif taxonomy)

**Trigger**: drift cal artifact (writer rerun jsonl) exhibits writer-direction motif in any axis (Axis 1 VERBATIM cell-value fabrication / Axis 2 canonical-form delimiter granularity / Axis 3 schema-field enum fabrication / future axes if surfaced). Specifically:
- Axis 1: TABLE_ROW / TABLE_HEADER cell-value digit-deletion / column-name fabrication / value invention / cross-table contamination on rerun atoms
- Axis 2: TABLE_ROW / TABLE_HEADER pipe-encoding convention drift (writer drops leading/trailing pipes vs executor canonical N5 form) on rerun atoms
- Axis 3: atom_type field fabrication (e.g., `SECTION_HEADING` not in 9-enum) on rerun atoms

**Severity**: **LOW INFORMATIONAL** — drift cal artifact is BY DESIGN under v1.7 N21 §派发 `drift_cal_alternation_artifact` exception (rerun atoms NOT merged to root regardless); marker tracks taxonomy axis classification for v1.8 candidate stack hypothesis testing.

**Detection**: cross-check writer rerun jsonl atoms vs PDF source per axis classification:
- Axis 1: PDF-byte-exact verify TABLE_ROW cell values + TABLE_HEADER columns
- Axis 2: pipe-encoding form vs executor baseline canonical N5 form `\| cell \| cell \|`
- Axis 3: atom_type ∈ atom_schema.v1.2 9-enum {HEADING, SENTENCE, LIST_ITEM, TABLE_HEADER, TABLE_ROW, CODE_LITERAL, CROSS_REF, FIGURE, NOTE}

**Source**: round 11 batch 45 NEW class (Axis 2 canonical-form delimiter granularity 1st cumulative) + round 12 batch 48 multi-motif simultaneous (Axis 1 7th cumulative artifact-only + Axis 2 2nd cumulative + Axis 3 1st cumulative); v1.8 N24 codification post round 12.

**Resolution**: writer-side N24 codification (multi-axis motif taxonomy formalization in §N24) + matcher-side per-axis flagging during drift cal artifact analysis + reviewer-side fix matrix item AF verification.

**MD-side note**: marker applies cross-format. MD-side cumulative motif count post round 12 = 0 in all axes. If MD-side motif surfaces, classify per same taxonomy.

### `[N25_cross_pdf_atom_id_namespace_collision]` — sync with PDF writer N25 (cross-PDF boundary §3.5 sweep)

**Trigger**: cross-PDF or cross-namespace batch (e.g., ig34 + sv20 in single batch like round 12 batch 47a) exhibits atom_id namespace collision OR source field per-atom mismatch OR PDF-specific furniture leak. Specifically:
- atom_id namespace collision: atom_id matches both `ig34_p\d{4}_aXXX` and `sv20_p\d{4}_aXXX` patterns (impossible by namespace partition design but flagged if observed)
- source field mismatch: per-atom `source` field does NOT match PDF source per page (e.g., `SDTMIG_v3.4` for sv20 atom — incorrect)
- furniture leak: sv20 atom verbatim matches `^\s*CDISC.*Standards` / `©\s*2021` / `\b2021-11-29\b` / `^\s*Page\s+\d+\s*$` / `^\s*Page\s+\d+\s+of\s+\d+\s*$` (excluding legitimate cover-page content like `2021-11-29 | 2.0 Final` TABLE_ROW under §0 [Cover] / Revision History)

**Severity**: **HIGH** — cross-PDF boundary integrity is foundational; collision or source field mismatch indicates dispatch-time error or namespace partition violation.

**Detection**: §3.5 cross-PDF boundary canonical-form sweep at reconciler-side pre-merge (codified writer-PDF §N25). 3 dimensions check.

**Source**: round 12 batch 47 cross-PDF boundary 1st cumulative in P1 atomization (1st INAUGURAL live-fire EFFECTIVE 0 collisions / 0 source mismatches / 0 furniture leaks excluding 1 false-positive resolved via context inspection).

**Resolution**: writer-side N25 codification + reconciler-side §3.5 sweep mandatory for any future cross-PDF or cross-namespace batches + reviewer-side fix matrix item AG verification.

### `[N26_page_boundary_off_by_one]` — sync with PDF writer N26 (page-boundary Hook 21)

**Trigger**: TABLE_ROW / SENTENCE atom verbatim's leading text matches start of page N+1 (not page N) but atom_id encodes page N (page-boundary off-by-one motif). Specifically:
- Atom encodes `..._p<N>_a<NN>` but verbatim's first 50 chars match `pdftotext page N+1` content (not page N)
- Dense spec-table content where row continues across page footer/header
- Multi-row sustained-content-narrative across 5+ page sub-batch (e.g., round 12 batch 49 §3.1.3 Findings spec table p.20-29)

**Severity**: **MEDIUM** — content-correctness preserved (verbatim is PDF-byte-exact) but page integer + atom_id + page_region misattribution affects retrieval and cross-batch consistency.

**Detection**: NEW Hook 21 (Self-Validate pre-DONE WARN-mode for dense spec-table content; recommends Option H page-label correction). Cross-page row physical-page disambiguation via pdftotext per-page extraction OR explicit footer 'Page N' marker tracking.

**Source**: round 12 batch 49 page-label correction Option H 13 atoms (page off-by-one boundary p.22→p.23 + p.23→p.24 wrap detection); v1.8 N26 codification post round 12.

**Resolution**: writer-side N26 codification (NEW Hook 21) + matcher-side flagging during cross-batch sweep + reviewer-side fix matrix item AH verification + Option H page-label correction (Rule B backup preserved per round 12 batch 49 precedent).

**Trigger condition note**: pdf source with explicit footer 'Page N' marker (sv20) → Hook 21 high-confidence detection; pdf source without explicit footer (ig34) → Hook 21 via pdftotext per-page extraction comparison.

### `[N27_l1_heading_parent_section_canonical_form_drift]` — sync with PDF writer N27 (L1 parent_section canonical form mandate)

**Trigger**: L1 NEW HEADING atom emitted with parent_section in non-canonical form. Specifically:
- Main-body L1 chapter (numbered §1, §2, etc.): parent_section uses natural-form `§N TITLE` instead of chapter-short-bracket `§N [TITLE]` (per N11 codification)
- Cover-anchor / frontmatter L1: parent_section deviates from `§0 [Cover]` convention (sv20 frontmatter precedent round 12 batch 47)
- Legacy ig34 v1.2 anomalies preserved per Rule B (NOT triggered for retroactive form)

**Severity**: **LOW** — non-canonical form does NOT affect content-correctness; cross-batch consistency degraded if mixed forms observed within same batch or cross-batch.

**Detection**: cross-check L1 NEW HEADING parent_section field matches single canonical form mandate per writer-PDF §N27.

**Source**: round 12 batch 47 reviewer omc:critic flagged 3 variants observed (a) self-bracket §N [TITLE] dominant ig34 v1.4+ 8/11 cases + (b) natural-form §N TITLE ig34 v1.2 anomalies + (c) NEW cover-anchor §0 [Cover] sv20 cross-PDF batch 47 2/2 cases = O-P1-165 LOW DEFER to v1.8.

**Resolution**: writer-side N27 codification (single canonical form mandate for L1 NEW HEADING parent_section) + matcher-side flagging during cross-batch sweep + reviewer-side fix matrix item AI verification.

### `[N28_l2_active_heading_parent_section_drift]` — sync with PDF writer N28 (L2 active-heading parent_section drift fix-up)

**Trigger**: children atom on page where L2 heading is active uses §N [TITLE] L1 ancestor parent instead of §N.M [TITLE] L2 parent. Specifically:
- L2 heading appears on page P; subsequent children atoms on page P (or later until next L2 heading) MUST use §N.M [TITLE] L2 parent
- Atoms emitted BEFORE L2 heading on same page may use L1 parent (carry-forward L1 active context until L2 surfaces)
- Cross-page persistence: L2 active-heading state persists across page boundaries within same sub-batch until next L2 heading

**Severity**: **LOW** — non-canonical parent attribution does NOT affect content-correctness; impacts heading-tree-derived retrieval depth.

**Detection**: cross-check children atom parent_section field matches L2 active-heading rule per writer-PDF §N28.

**Source**: round 12 batch 47 reviewer omc:critic flagged systematic L2 active-heading drift on sv20 §2.1 children (sv20_p0009 a002-a019 with §2.1 Model Concepts and Terms – Variables active but parent uses §2 [...] L1 form) = O-P1-166 LOW DEFER to v1.8 (~18 atoms 1 batch).

**Resolution**: writer-side N28 codification (L2 active-heading rule) + matcher-side flagging during cross-batch sweep + reviewer-side fix matrix item AJ verification.

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.8 sync with all 4 prompts)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post 6th live-fire (round 7+8+9+10+11+12 = 6 cumulative live-fires)
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post 3rd live-fire unchanged
- **N9 + N10 leaf-pattern codifications**: CROSS-LEAF-DOMAIN VALIDATED post 5th live-fire (7 cumulative leaf-domains)
- **N11 chapter-short-bracket extension**: L1+L2+L3 FULL-SCOPE VALIDATED post 6 cumulative L1 transitions in P1
- **N18 EXTENDED scope EFFECTIVENESS PROVEN production-side** + **N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side** sustained → v1.7 N21 PDF-side trigger justified at 2 cumulative
- **N21 writer-family complete deprecation EFFECTIVE 2nd round running** (PDF-side production atomization only)
- **N22+N23 EFFECTIVE 2nd cumulative** (sustained from v1.7)
- **NEW v1.8 STRONGLY VALIDATED**: §0.5 reconciler-side sweep at 4 cumulative live-fires preventive EFFECTIVE
- **NEW v1.8 STRONGLY VALIDATED**: N6 single-dispatch pattern at 3 cumulative live-fires
- **NEW v1.8**: multi-axis writer-direction motif taxonomy (3 axes formalized — matcher per-axis discrepancy flagging via N24 marker)
- **NEW v1.8**: cross-PDF boundary §3.5 sweep STANDING (N25 marker for namespace collision / source mismatch / furniture leak)
- **NEW v1.8**: page-boundary Hook 21 (N26 marker for off-by-one motif)
- **NEW v1.8**: L1 + L2 parent_section canonical form codification (N27 + N28 markers; APPLIES MD-side + PDF-side)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.4 | 2026-04-28 | post P1 round 7 cut: 4 NEW discrepancy markers covering round 5+6+7 candidates |
| v1.5 | 2026-04-28 | post P1 round 8 cut: 1 NEW discrepancy marker [NEW7_xpt_parent_caption_violation] |
| v1.6 | 2026-04-29 | post P1 round 9 cut EMERGENCY-CRITICAL: 4 NEW discrepancy markers (NEW18 + N19 + N20 + NEW8.e) |
| v1.7 | 2026-04-29 | post P1 round 10 cut EMERGENCY-CRITICAL: 1 NEW discrepancy marker [N21_writer_family_deprecation_violation] HIGH PDF-side ONLY |
| **v1.8** | **2026-04-30** | **post P1 round 12 cut**: 5 NEW discrepancy markers covering round 11+12 v1.8 codifications: `[N24_multi_axis_writer_direction_motif_artifact]` LOW INFORMATIONAL (multi-axis motif taxonomy artifact-only flagging) + `[N25_cross_pdf_atom_id_namespace_collision]` HIGH (cross-PDF boundary §3.5 sweep dimension violations) + `[N26_page_boundary_off_by_one]` MEDIUM (page-boundary off-by-one motif) + `[N27_l1_heading_parent_section_canonical_form_drift]` LOW (L1 NEW HEADING parent_section non-canonical form) + `[N28_l2_active_heading_parent_section_drift]` LOW (L2 active-heading parent_section attribution drift); STATUS PROMOTIONS sustained N14 6th + G-MS-4 3rd unchanged + N9+N10 5th + N11 6 cumulative + N18 sustained + N21 EFFECTIVE 2nd + 2 NEW STRONGLY VALIDATED status promotions: §0.5 reconciler-side sweep at 4 cumulative + N6 single-dispatch at 3 cumulative + 3 NEW v1.8 STATUS NEW: multi-axis motif taxonomy + cross-PDF boundary §3.5 sweep STANDING + page-boundary Hook 21 NEW; v1.7 archived `archive/v1.7_final_2026-04-30/`. NOT behavior change — verdict enum / bidirectional match contract / Rule D isolation 全 carry-forward unchanged. |
