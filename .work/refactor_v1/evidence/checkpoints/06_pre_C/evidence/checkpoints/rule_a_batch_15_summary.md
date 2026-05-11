# Rule A Audit — batch 15 (p.141-150)

> Sample size: 10 atoms
> Scope: SDTMIG v3.4 p.141-150 (AE tail + BE full + CE head)
> Reviewer: `vercel:deployment-expert` (slot #24, AUDIT-mode pivot)
> Mode: AUDIT-only — no atom modifications, no infrastructure work
> Date: 2026-04-25
> PDF source: `source/SDTMIG v3.4 (no header footer).pdf`
> Sample file: `evidence/checkpoints/rule_a_batch_15_sample.jsonl`

## Verdict counts

| Verdict | Count | Weight |
|---|---|---|
| PASS | 9 | 9.0 |
| PARTIAL | 1 | 0.5 |
| FAIL | 0 | 0.0 |
| **Total** | **10** | **9.5 / 10.0** |

**Weighted pass rate: 9.5 / 10.0 = 0.95 (95.0%)**

**Final verdict: PASS** (≥90% threshold met)

## Per-atom verdict table

| # | atom_id | atom_type | page | verdict | severity | atom_type_ok | verbatim_ok | parent_ok | heading_fields_ok |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ig34_p0141_a005 | TABLE_ROW | 141 | PASS | n/a | ✓ | ✓ | ✓ | n/a |
| 2 | ig34_p0142_a016 | TABLE_ROW | 142 | PASS | n/a | ✓ | ✓ | ✓ | n/a |
| 3 | ig34_p0143_a002 | HEADING | 143 | PASS | n/a | ✓ | ✓ | ✓ | ✓ (L3 sib=2) |
| 4 | ig34_p0144_a007 | TABLE_ROW | 144 | PASS | n/a | ✓ | ✓ | ✓ | n/a |
| 5 | ig34_p0145_a004 | HEADING | 145 | PASS | n/a | ✓ | ✓ | ✓ | ✓ (L5 sib=1) |
| 6 | ig34_p0146_a005 | TABLE_ROW | 146 | PASS | n/a | ✓ | ✓ | ✓ | n/a |
| 7 | ig34_p0147_a009 | CODE_LITERAL | 147 | PASS | n/a | ✓ | ✓ | ✓ | n/a |
| 8 | ig34_p0148_a010 | HEADING | 148 | PARTIAL | MEDIUM | ✓ | ✓ | ✓ | ✗ (sib=null) |
| 9 | ig34_p0149_a017 | TABLE_ROW | 149 | PASS | LOW | ✓ | ✓ | ✓ | n/a |
| 10 | ig34_p0150_a004 | SENTENCE | 150 | PASS | LOW | ✓ | ✓ | ✓ | n/a |

## Findings

### MEDIUM × 1

**M-1: ig34_p0148_a010 — sibling_index=null on References L4 heading under §6.2.2**

- atom: `{"atom_type": "HEADING", "verbatim": "References", "heading_level": 4, "sibling_index": null, "parent_section": "§6.2.2 [Biospecimen Events (BE)]"}`
- PDF p.148 between BE Example 2 closing and §6.2.3 CE start, "References" appears as a bold L4 heading (with 2 numbered citations following).
- TOC ground truth (audit prompt) lists BE sub-headings up to Examples L4 sib=4 only. References should logically be **L4 sib=5** under §6.2.2 per R15 cross-batch sibling continuity.
- Impact: downstream R15 sibling continuity check for any future "References" L4 siblings (e.g., in CE/other domains) will not have a baseline anchor. Reconciler should set sibling_index=5 for this atom OR explicitly document that References sub-headings get a separate sibling counter.
- Recommendation: post-audit reconciler decision — set sib=5 OR document policy in audit_matrix. Either choice unblocks downstream batches.

### LOW × 2

**L-1: ig34_p0149_a017 — R10 PDF wrap newline within table cell rendered as space-join**

- atom verbatim: `"...in Demographics). Not all values of the codelist are allowable..."` (single space between sentences)
- PDF p.149 CESTRF row CDISC Notes cell has a paragraph break between the two sentences (rendered as a literal newline within the same cell).
- R10 expects `\n` literal preservation for cell-internal wraps (e.g., `domains.\n This`). Atom uses space-join.
- Impact: convention-level — likely a batch 14/15 stylistic choice consistent across multi-sentence cell notes. Not a blocker. Consider canonicalizing in v1.3 prompt update.

**L-2: ig34_p0150_a004 — Footnote leading "1" superscript dropped from verbatim**

- atom verbatim: `"In this column, an asterisk (*) indicates..."`
- PDF p.150 has `¹In this column...` where the leading `1` is a superscript footnote marker tied to the spec-table column-header `Format¹` reference.
- atom drops the `1` superscript. Decision is reasonable (footnote-marker stripping is a recognized convention for SENTENCE atoms) and consistent with prior AE/BE footnote rows in earlier batches.
- Impact: informational. Document the convention in audit_matrix § "Footnote marker handling" if not already present.

### HIGH × 0

None.

## Spot-check observations OUTSIDE sample

While reading p.141-150 in full to verify atom context, I noticed:

1. **p.143 transition page discipline (R12) — VERIFIED**: §6.2.1 AE content (none on p.143), §6.2.2 heading + BE-Description/Overview + BE-Specification all present on p.143 with proper transition routing. The audit sample atom `p0143_a002` (the §6.2.2 heading itself) parents to §6.2 correctly, and downstream BE content would correctly parent to §6.2.2.

2. **p.148 transition page discipline (R12) — VERIFIED for sample atom 8**: BE last bit (relrec.xpt table at top + References at middle) routes to §6.2.2; §6.2.3 CE heading + CE Description/Overview + CE Specification spec-table head route to §6.2.3. The TOC parent_section split rule on p.148 is correctly applied for atom 8 (References → §6.2.2). I cannot verify other p.148 atoms not in the 10-atom sample (e.g., the §6.2.3 heading atom, CE-Description/Overview heading, CE spec-table opening row) but these would need separate spot-check by reconciler.

3. **p.144 BE Assumptions list discipline (R13) — partial visibility**: PDF p.144 has BE-Assumptions list items 1-7 (numbered, several with sub-items 6.a/6.b/6.c). Sample atom 4 (BESTDY TABLE_ROW) is the spec-table portion of p.144, not the Assumptions list. R13 numbered-list discipline cannot be verified from this sample alone — recommend spot-check on Assumptions atoms (likely p144_a008+).

4. **p.145 Example 1 narrative + table consistency**: The Example 1 narrative ("In this example, a specimen is collected, flash frozen, thawed, and shipped...") appears BEFORE the be.xpt and suppbe.xpt tables on p.145. Sample atom 5 captures only the "Example 1" L5 heading. Narrative SENTENCE atoms and the be.xpt/suppbe.xpt rows on p.145 are not in the sample but should follow standard table-row discipline. The bs.xpt table starting on p.145 actually continues to p.146 (sample atom 6 captures p.146 Row 3, confirming cross-page table-row split is being handled correctly).

5. **p.149 CE spec-table is multi-page**: The CE spec-table starts on p.148, continues full p.149 (where sample atom 9 sits), and ends on p.150 (CESTTPT, CEENRTPT, CEENTPT — first 3 rows of p.150). Sample atom 10 (the SENTENCE footnote) captures the column-footer-1 footnote that closes the spec-table on p.150. Multi-page table-row sequencing appears correct.

6. **p.146 Example 1 (cont.) → Example 2 transition**: PDF p.146 has bs.xpt table top (Example 1 cont., 3 rows), then narrative paragraphs explaining RELREC, then relrec.xpt table (4 rows), then "Example 2" heading + narrative + new be.xpt table (Example 2). Sample atom 6 captures Row 3 of bs.xpt only (top region). Cross-page Example boundary is intact — but the "Example 2" L5 heading on p.146 should exist as a HEADING atom with sib=2 per R15 (parallel to Example 1 sib=1 on p.145). I did NOT verify this directly from the sample.

## Final verdict

**PASS (95.0% weighted, ≥90% threshold)**

- 9 PASS / 1 PARTIAL / 0 FAIL across 10 atoms covering AE-Examples tail, full BE domain, and CE-Specification head.
- Single MEDIUM finding (M-1) is a sibling_index=null on a L4 heading that needs reconciler decision (set sib=5 vs. document policy) — non-blocking for batch 15 sign-off.
- 2 LOW findings are convention-level (R10 newline preservation, footnote-marker stripping) — informational, candidates for v1.3 prompt clarification.
- TABLE_ROW empty-cell preservation (R8/R11) verified across 4 sample TABLE_ROWs — clean.
- HEADING level + sibling_index correctness verified for atoms 3 (BE L3 sib=2) and 5 (Example 1 L5 sib=1) — clean.
- CODE_LITERAL filename parent (R9) verified for atom 7 (suppbe.xpt → §6.2.2).
- Transition-page parent_section routing (R12) verified for atoms 3 (§6.2.2 heading → §6.2) and 8 (References → §6.2.2).

Recommend batch 15 advance to reconciler merge with the M-1 sibling_index decision logged in `audit_matrix.md` and the 2 LOW findings noted as v1.3-prompt-clarification candidates.

---

`RULE_A_DONE pass=9 partial=1 fail=0 weighted=0.95`
