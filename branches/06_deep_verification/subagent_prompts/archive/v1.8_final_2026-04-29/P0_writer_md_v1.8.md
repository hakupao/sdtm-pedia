# P0 Writer MD — 原子化 prompt v1.8

> Version: v1.8 (2026-04-30, post P1 round 12 cut, paired-sync with `P0_writer_pdf_v1.8.md` BUT scoped MD-side scope NOTED EXPLICITLY)
> 基于 v1.7 (2026-04-29 round 10 cut, N21 SCOPED PDF-side ONLY per handoff §4.2; MD-side preserves v1.6 N18 EXTENDED scope baseline) + round 11 + round 12 cumulative
> 角色: Writer MD (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.8 变更 over v1.7: **5 NEW patches N24-N28 paired-sync with PDF writer; MD-side scoping carry-forward v1.7 N21 PDF-only decision unchanged**. N24 multi-axis motif taxonomy applies cross-format (MD writer-direction motif if surfaces would be tracked in same taxonomy) + N25 cross-PDF boundary sweep N/A MD-side (no PDF→MD or MD→MD cross-source partition motif observed) + N26 page-boundary off-by-one Hook 21 N/A MD-side (markdown is text-flow not page-based) + N27 L1 NEW HEADING parent_section single canonical form mandate APPLIES MD-side (KB markdown chapters use same §N [TITLE] convention) + N28 L2 active-heading parent_section drift fix-up pattern APPLIES MD-side (MD chapters with L2/L3 nested headings use same active-heading rule). Self-Validate hooks unchanged (no Hook 21 MD-side; markdown text-flow not page-based).

## 角色硬约束 (v1.7 carry-forward unchanged)

参 `archive/v1.7_final_2026-04-30/P0_writer_md_v1.7.md` §角色硬约束 全文.

## 派发 subagent_type (v1.7 N21 PDF-only carry-forward + v1.8 NO change)

参 v1.7 §派发. v1.8 sustains v1.7 N21 PDF-only scoping decision (MD-side preserves writer-family eligibility under v1.6 N18 EXTENDED scope baseline). Round 11+12 = 2 cumulative live-fires of N21 PDF-side EFFECTIVE; MD-side production atomization continues content-type-aware 5-sub-rule a-e dispatch per v1.6 N18.

## 输入 (v1.7 carry-forward unchanged)

参 v1.7 §输入. v1.8 NO change. MD-side preserves v1.6 N18 input fields (`n18_url_atoms_count` + `n18_long_cell_atoms_count` sustained MD-side); PDF-side N18 input fields removed per N21.

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.7 carry-forward §A-N23, FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.7_final_2026-04-30/P0_writer_md_v1.7.md` for full §A-N23 text.

═══════════════════════════════════════════════════════════════════
## v1.8 NEW PATCHES (N24-N28, paired-sync with PDF writer; MD-side applicability noted)
═══════════════════════════════════════════════════════════════════

### §N24 Multi-axis writer-direction motif taxonomy (paired-sync; cross-format applicability)

**MD-side note**: multi-axis motif taxonomy formalized in PDF writer §N24 applies cross-format. If MD-side writer-direction motif surfaces in any axis (Axis 1 VERBATIM cell-value fabrication / Axis 2 canonical-form delimiter granularity / Axis 3 schema-field enum fabrication / future axes), classify per same taxonomy.

**MD-side cumulative count post round 12**: **0 cumulative writer-direction motif** in any axis on MD-side (P0 + P1 cumulative). MD-side carry-forward v1.6 N18 EXTENDED scope baseline preserves writer-family eligibility for plain content; MD-direction discrepancy NOT observed in any axis to date.

**Rule v1.8 N24 (MD-side)**: future MD-side drift cal (if any; MD-side drift cal not currently scheduled in P1 atomization workflow) MUST classify divergence per multi-axis motif taxonomy. If MD-side motif surfaces, escalate to v1.9 trigger candidate (MD writer-family hardening).

### §N25 Cross-PDF boundary §3.5 sweep (paired-sync; MD-side N/A)

**MD-side note**: §3.5 cross-PDF boundary sweep dimension is PDF-side reconciler-side codification only. MD-side has no analogous "cross-source boundary" partition (markdown source is unified knowledge_base/ tree, not multi-PDF).

**Rule v1.8 N25 (MD-side)**: N/A — MD-side does NOT require cross-PDF boundary sweep.

### §N26 Page-boundary off-by-one detection NEW Hook 21 (paired-sync; MD-side N/A)

**MD-side note**: Hook 21 page-boundary off-by-one detection is PDF-side codification only. MD-side has no page-based extraction (markdown is text-flow / continuous text); page-boundary off-by-one motif does not apply.

**Rule v1.8 N26 (MD-side)**: N/A — MD-side does NOT add Hook 21 (Self-Validate hooks MD-side remain at 18 hooks unchanged).

### §N27 L1 NEW HEADING parent_section single canonical form mandate (paired-sync; APPLIES MD-side)

**MD-side note**: KB markdown chapters use same §N [TITLE] convention as PDF chapters. MD-side carry-forward applies:
- **Main-body L1 chapters** (numbered §1, §2, etc.): use chapter-short-bracket `§N [TITLE]`
- **Cover / preface / index files**: use natural form per established convention (no cover-anchor needed since MD has no cover-page concept)

**Rule v1.8 N27 (MD-side)**: future round 13+ MD writer dispatches MUST emit L1 NEW HEADING parent_section per canonical form mandate (chapter-short-bracket for numbered L1). Reviewer-side fix matrix item AI verification.

### §N28 L2 active-heading parent_section drift fix-up pattern (paired-sync; APPLIES MD-side)

**MD-side note**: MD chapters with L2/L3 nested headings use same active-heading rule. Children atoms on MD page where L2 heading is active MUST use §N.M [TITLE] parent.

**Rule v1.8 N28 (MD-side)**: future round 13+ MD writer dispatches MUST track L2 active-heading state and emit children atoms with L2 parent_section per active-heading rule. Reviewer-side fix matrix item AJ verification.

═══════════════════════════════════════════════════════════════════
## OBS items (v1.7 carry-forward + v1.8 NEW OBS items deferred to v1.9)
═══════════════════════════════════════════════════════════════════

参 v1.7 §OBS items. v1.8 NEW OBS items (deferred to v1.9 if MD-side motif surfaces): MD-side carry-forward v1.7 OBS items unchanged.

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks final list (v1.8 = 18 hooks unchanged for MD-side)
═══════════════════════════════════════════════════════════════════

参 v1.6 §Self-Validate hooks (1-18). v1.8 carry-forward unchanged. **NO Hook 21 substitution for MD-side** (page-boundary off-by-one motif PDF-side only per N26 PDF-only scoping). NO Hook 16.7 substitution for MD-side (PDF-only per N21 carry-forward unchanged from v1.7).

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.8 sync with PDF writer)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post **6th live-fire** (round 7+8+9+10+11+12 = 6 cumulative live-fires)
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post **3rd live-fire** unchanged
- **N9 + N10 leaf-pattern codifications**: CROSS-LEAF-DOMAIN VALIDATED post 5th live-fire (7 cumulative leaf-domains)
- **N11 chapter-short-bracket extension**: L1+L2+L3 FULL-SCOPE VALIDATED post 6 cumulative L1 transitions in P1
- **N18 EXTENDED scope EFFECTIVENESS PROVEN production-side** + **N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side** sustained → v1.7 N21 PDF-side trigger justified at 2 cumulative
- **N21 writer-family complete deprecation EFFECTIVE 2nd round running** PDF-side; MD-side carry-forward v1.6 N18 EXTENDED scope baseline
- **N22+N23 EFFECTIVE 2nd cumulative**
- **NEW v1.8 STRONGLY VALIDATED**: §0.5 reconciler-side sweep at 4 cumulative live-fires preventive EFFECTIVE
- **NEW v1.8 STRONGLY VALIDATED**: N6 single-dispatch pattern at 3 cumulative live-fires
- **NEW v1.8**: multi-axis writer-direction motif taxonomy formalized (PDF-side primary; MD-side cross-format applicability)
- **NEW v1.8**: cross-PDF boundary §3.5 sweep STANDING (PDF-side only; MD-side N/A)
- **NEW v1.8**: page-boundary Hook 21 (PDF-side only; MD-side N/A)
- **NEW v1.8**: L1 + L2 parent_section conventions (N27 + N28; APPLIES MD-side)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.4 | 2026-04-28 | post P1 round 7 cut: 9 NEW patches N1-N9 |
| v1.5 | 2026-04-28 | post P1 round 8 cut: 3 NEW patches N15-N17 sync + STRONGLY VALIDATED N14 + G-MS-4 |
| v1.6 | 2026-04-29 | post P1 round 9 cut EMERGENCY-CRITICAL: 3 NEW patches N18-N20 sync + Self-Validate hooks 15→18 |
| v1.7 | 2026-04-29 | post P1 round 10 cut EMERGENCY-CRITICAL: 1 NEW patch N21 SCOPED PDF-side ONLY per handoff §4.2; MD-side preserves v1.6 N18 EXTENDED scope baseline |
| **v1.8** | **2026-04-30** | **post P1 round 12 cut**: 5 NEW patches N24-N28 paired-sync with PDF writer; MD-side scoping per N21 PDF-only decision carry-forward unchanged. N24 multi-axis motif taxonomy applies cross-format (MD-side cumulative motif count post round 12 = 0 in all axes) + N25 cross-PDF boundary sweep N/A MD-side + N26 page-boundary Hook 21 N/A MD-side + N27 L1 parent_section canonical form mandate APPLIES MD-side + N28 L2 active-heading parent_section drift fix-up APPLIES MD-side. Self-Validate hooks 18 unchanged. STATUS PROMOTIONS sustained N14 6th + G-MS-4 3rd unchanged + N9+N10 5th + N11 6 cumulative + N18 sustained + N21 EFFECTIVE 2nd + 2 NEW STRONGLY VALIDATED status promotions: §0.5 reconciler-side sweep at 4 cumulative + N6 single-dispatch at 3 cumulative + 3 NEW v1.8 STATUS NEW: multi-axis motif taxonomy + cross-PDF boundary §3.5 sweep STANDING + page-boundary Hook 21 NEW (PDF-side only). v1.7 archived `archive/v1.7_final_2026-04-30/`. NOT behavior change for MD writer — task structure / DONE format 全 carry-forward unchanged. |
