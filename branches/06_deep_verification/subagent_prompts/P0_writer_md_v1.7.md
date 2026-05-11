# P0 Writer MD — 原子化 prompt v1.7

> Version: v1.7 (2026-04-29, post P1 round 10 cut, paired-sync with `P0_writer_pdf_v1.7.md` BUT scoped MD-side scope NOTED EXPLICITLY)
> 基于 v1.6 (round 9 cut, 3 NEW patches N18-N20 sync + STRONGLY VALIDATED status sustained N14 + G-MS-4 + CROSS-LEAF-DOMAIN VALIDATED N9+N10) + round 10 cumulative
> 角色: Writer MD (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.7 变更 over v1.6: **N21 SCOPED EXPLICITLY TO PDF-side ONLY (per handoff §4.2 recommendation).** MD-side preserves writer-family eligibility under v1.6 N18 EXTENDED scope baseline (5 sub-rules a-e content-type-binding). Justification: MD-side has different content-type profile + lower cumulative writer-direction VALUE HALLUCINATION recurrence count (PDF-side 6 cumulative recurrences round 5-10; MD-side 0 cumulative recurrences in P0 + P1 MD-side atomization). MD writer prompt v1.7 = thin paired-sync of v1.7 PDF prompt with N21 explicitly noted as **PDF-only**, not MD.

## 角色硬约束 (v1.6 carry-forward unchanged)

参 `archive/v1.6_final_2026-04-29/P0_writer_md_v1.6.md` §角色硬约束 全文.

## 派发 subagent_type (v1.7 N21 SCOPED PDF-side ONLY — MD-side carry-forward v1.6 N18 EXTENDED)

**🔴 CRITICAL SCOPING NOTE**: v1.7 N21 EMERGENCY-CRITICAL writer-family complete deprecation applies to **PDF-side P1 production atomization ONLY** (per `P0_writer_pdf_v1.7.md` §派发). MD-side production atomization is **NOT subject to N21 complete deprecation**.

**MD-side dispatch table (carry-forward v1.6 N18 EXTENDED scope unchanged)**:

| Content type / Pattern | MD-side dispatch (v1.6 carry-forward, NOT subject to v1.7 N21) | Justification |
|---|---|---|
| **MD with Examples-narrative + spec-table dense** (carry-forward N16) | `oh-my-claudecode:executor` MANDATORY (writer-family BANNED MD-side per v1.5 N16) | round 5+6+7+8 4 cumulative PDF-side recurrences (MD-side 0 recurrences but conservative ban sustained per v1.5 N16 cross-applicability) |
| **MD with URLs / DOIs** (carry-forward v1.6 N18.b) | `oh-my-claudecode:executor` MANDATORY | PDF-side N18.b cross-applies (URL motif content-type-independent cross-format) |
| **MD with paragraphs ≥500 chars in single SENTENCE** (carry-forward v1.6 N18.c) | `oh-my-claudecode:executor` MANDATORY | long-cell / paragraph-concat motif cross-format |
| **MD with citation, identifier, or VERBATIM-CRITICAL fact** (carry-forward v1.6 N18.d) | `oh-my-claudecode:executor` MANDATORY | generalization clause cross-format |
| **MD with structural transitions (chapter NEW + L3-leaf-pattern L4 chain start)** (carry-forward v1.6 N18.e) | `oh-my-claudecode:executor` MANDATORY | mixed_structural_transition recurrence proof PDF-side cross-applies |
| **SENTENCE-paragraph + LIST_ITEM-heavy** (no URLs/long/citations/transitions) | `oh-my-claudecode:writer` 或 executor (free choice — writer-family ELIGIBLE MD-side) | No systematic family-direction motif on this content (MD-side carry-forward v1.6 free choice) |

**Effect**: v1.7 MD-side preserves v1.6 N18 EXTENDED scope baseline. MD writer-family permissible content remains plain narrative ONLY (no URLs / no long-cells / no transitions / no Examples). **Critical distinction from PDF-side N21**: MD-side carry-forward v1.6 N18 5-sub-rule binding, NOT escalated to total ban.

**Justification for MD-side preservation** (per handoff §4.2):
1. **Different content-type profile**: MD-side atomization operates on already-structured markdown (knowledge_base/ chapters/) where atom-emission semantics differ from raw PDF table extraction (no OCR-style table fabrication risk; column structure is plain markdown not visual)
2. **Lower cumulative recurrence count**: 0 MD-side cumulative writer-direction VALUE HALLUCINATION recurrences in P0 + P1 cumulative (vs 6 PDF-side cumulative)
3. **Defense-in-depth**: v1.5 N16 + v1.6 N18 5-sub-rule MD-side bans for high-risk content types (Examples + URLs + long-cells + citations + transitions) sustained — MD writer-family eligible ONLY for plain SENTENCE-paragraph + LIST_ITEM-heavy

**Pre-dispatch validation** (carry-forward v1.6 Hook 15.5 / 16 — sync with PDF Hook 16.6 EXTENDED scope, NOT replaced by PDF Hook 16.7 simplified ban): MD-side maintains 5-sub-rule a-e content-type-aware dispatch assert.

## 输入 (v1.6 carry-forward unchanged)

参 v1.6 §输入. v1.7 NEW: NO removal of v1.6 N18 input fields for MD-side (PDF-side N18 input fields removed per N21; MD-side preserves N18 5-sub-rule scan needs).

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.6 carry-forward §A-N20 FULL TEXT IN ARCHIVE)
═══════════════════════════════════════════════════════════════════

参 `archive/v1.6_final_2026-04-29/P0_writer_md_v1.6.md` for full §A-M v1.3 base + §N1-N9 v1.4 patches + §N15-N17 v1.5 patches + §N18-N20 v1.6 patches.

═══════════════════════════════════════════════════════════════════
## v1.7 NEW PATCH (N21, scoped PDF-side ONLY — MD writer paired sync explicit-non-applicability note)
═══════════════════════════════════════════════════════════════════

### §N21 (PDF-only, MD-side NOT applicable per handoff §4.2 recommendation)

**Rationale for MD-side preservation**: see §派发 above. MD writer prompt v1.7 sustains v1.6 N18 EXTENDED scope dispatch table; PDF writer prompt v1.7 §N21 escalates to complete writer-family deprecation.

**MD-side carry-forward**:
- v1.5 N16 Examples-narrative + spec-table dense MD: writer-family BANNED (MD-side conservative; carry-forward v1.5)
- v1.6 N18.b URLs/DOIs MD: executor MANDATORY (carry-forward v1.6)
- v1.6 N18.c long-paragraph (≥500 chars) MD: executor MANDATORY (carry-forward v1.6)
- v1.6 N18.d general VERBATIM-CRITICAL MD: executor MANDATORY (carry-forward v1.6)
- v1.6 N18.e structural transition MD: executor MANDATORY (carry-forward v1.6)
- Plain SENTENCE-paragraph + LIST_ITEM-heavy (no URLs/long/citations/transitions) MD: writer-family ELIGIBLE (carry-forward v1.6)

**MD-side Hook 15.5 / 16 sustained** (NOT replaced by PDF Hook 16.7 simplified ban): preserve content-type-aware 5-sub-rule a-e dispatch assert.

═══════════════════════════════════════════════════════════════════
## v1.7 SECONDARY decisions (sync with PDF N22 + N23)
═══════════════════════════════════════════════════════════════════

### §N22 Hook 18 SENTENCE-paragraph-concat WARN-mode SUSTAINED (sync with PDF N22)

MD writer Hook 18 carry-forward v1.6 unchanged (regex `\.\s+[A-Z]` WARN-mode pre-DONE detection). Same recommendation: keep WARN-mode + narrative-chapter exemplar.

### §N23 Hook 19 PDF-cross-verify RENDERED MOOT by N21 PDF-only (sync with PDF N23)

MD writer Hook 19 carry-forward v1.6 unchanged (sample N=3→N=10 + mandatory URL/DOI/citation cross-check + long-cell halt-on-violation). MD-side carry-forward unchanged (NOT rendered moot since MD-side preserves writer-family eligibility for plain content per N21 PDF-only scoping).

═══════════════════════════════════════════════════════════════════
## Self-Validate hooks final list (v1.7 = 18 hooks unchanged)
═══════════════════════════════════════════════════════════════════

参 v1.6 §Self-Validate hooks (1-18). v1.7 carry-forward unchanged. **NO Hook 16.7 substitution for MD-side** (v1.6 Hook 15.5 / 16 sustained per N21 PDF-only scoping).

═══════════════════════════════════════════════════════════════════
## STATUS PROMOTIONS (v1.7 sync with PDF writer)
═══════════════════════════════════════════════════════════════════

- **N14 strict alternation methodology**: STRONGLY VALIDATED post 4th live-fire (round 7+8+9+10 = 4 cumulative live-fires)
- **G-MS-4 halt fallback**: STRONGLY VALIDATED post 3rd live-fire (round 7+8+10 = 3 cumulative live-fires)
- **N9 + N10 leaf-pattern codifications**: CROSS-LEAF-DOMAIN VALIDATED post 4th live-fire (FA + SR + TA + TD/TM/TI/TS = 4-leaf-domain cumulative)
- **N11 chapter-short-bracket extension**: L1+L2+L3 FULL-SCOPE VALIDATED sustained
- **NEW v1.7 (PDF-side trigger evidence carry-forward, applies as MD-side scoping rationale)**: N18 EXTENDED scope EFFECTIVENESS PROVEN production-side (PDF round 10 batch 42 production 217 atoms executor-clean post N18.a/b/d/e bindings) + N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side (PDF round 10 batch 42 drift cal 6th recurrence on N18.a-banned content type) → v1.7 N21 PDF-side trigger justified; MD-side dispatch remains v1.6 N18 EXTENDED scope per N21 PDF-only scoping decision (MD preserves writer-family eligibility for plain SENTENCE-paragraph + LIST_ITEM-heavy under v1.6 N18 5-sub-rule a-e baseline)
- **NEW v1.7**: N21 writer-family complete deprecation (PDF-side only; MD-side carry-forward v1.6 N18 EXTENDED scope)

═══════════════════════════════════════════════════════════════════
## Changelog
═══════════════════════════════════════════════════════════════════

| Version | Date | Changes |
|---|---|---|
| v1.4 | 2026-04-28 | post P1 round 7 cut: 9 NEW patches N1-N9 |
| v1.5 | 2026-04-28 | post P1 round 8 cut: 3 NEW patches N15-N17 sync + STRONGLY VALIDATED N14 + G-MS-4 |
| v1.6 | 2026-04-29 | post P1 round 9 cut EMERGENCY-CRITICAL: 3 NEW patches N18-N20 sync with PDF writer (writer-family ban EXTENDED scope + SENTENCE-paragraph-concat Hook 18 + PDF-cross-verify expansion); Self-Validate hooks 15→18 |
| **v1.7** | **2026-04-29** | **post P1 round 10 cut EMERGENCY-CRITICAL**: 1 NEW patch N21 paired-sync with PDF writer **SCOPED PDF-side ONLY** per handoff §4.2 recommendation. MD-side preserves v1.6 N18 EXTENDED scope baseline (5 sub-rules a-e content-type-binding); MD writer-family ELIGIBLE for plain SENTENCE-paragraph + LIST_ITEM-heavy content (no URLs/long/citations/transitions). Justification for MD-side preservation: different content-type profile (MD operates on already-structured markdown) + lower cumulative writer-direction VALUE HALLUCINATION recurrence count (0 MD-side recurrences in P0+P1 vs 6 PDF-side rounds 5-10) + defense-in-depth (v1.5 N16 + v1.6 N18 5-sub-rule MD bans sustained for high-risk content). N22 (Hook 18 WARN-mode) + N23 (Hook 19 cross-verify) MD-side carry-forward v1.6 unchanged. Self-Validate hooks 18 unchanged (NO Hook 16.7 substitution for MD-side; v1.6 Hook 15.5 / 16 sustained). STATUS PROMOTIONS sustained N14 4th + G-MS-4 3rd + N9+N10 CROSS-LEAF-DOMAIN VALIDATED 4th + N11 sustained + 2 NEW v1.7 PDF-side trigger evidence carry-forward (N18 EXTENDED scope EFFECTIVENESS PROVEN production-side + N18 PARTIAL ban scope INSUFFICIENT PROVEN drift-cal-side, applied as MD-side scoping rationale per N21 PDF-only decision) + NEW N21 PDF-only. v1.6 archived `archive/v1.6_final_2026-04-29/`. NOT behavior change for MD writer — task structure / DONE format 全 carry-forward unchanged. |
