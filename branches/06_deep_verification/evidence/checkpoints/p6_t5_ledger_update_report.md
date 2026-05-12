# P6 T5 — Ledger Update Report

**Date**: 2026-05-12T08:11:01Z
**Script**: scripts/p6_t5_update_ledger.py
**Input backup**: coverage_ledger.jsonl.p6_t4b_post.bak

---

## Update Summary

| Action | Count |
|--------|-------|
| MISSING prose → EQUIVALENT | 529 |
| MISSING prose → INTENTIONAL_EXCLUDE | 5 |
| Total prose MISSING updated | 534 |
| Non-prose MISSING (unchanged) | 304 |
| Other entries unchanged | 11649 |
| Total ledger entries | 12487 |

## IE Candidates Updated

| Atom ID | Category | Reason |
|---------|----------|--------|
| `ig34_p0070_a027` | RACEC_codelist_placeholder | PDF text is '<RACEC codelist>' — a cross-reference placeholder, not substantive ... |
| `ig34_p0071_a011` | RACEC_codelist_placeholder | PDF text is '<RACEC codelist>' — a cross-reference placeholder, not substantive ... |
| `ig34_p0071_a023` | RACEC_codelist_placeholder | PDF text is '<RACEC codelist>' — a cross-reference placeholder, not substantive ... |
| `ig34_p0071_a032` | RACEC_codelist_placeholder | PDF text is '<RACEC codelist>' — a cross-reference placeholder, not substantive ... |
| `ig34_p0037_a035` | TRUNCATED_AT_PAGE_BOUNDARY | Atom verbatim ends mid-sentence at PDF page boundary; reconstructed text unavail... |

## Post-Update Coverage Statistics

| Metric | Value |
|--------|-------|
| Total PDF atoms | 12487 |
| INTENTIONAL_EXCLUDE | 2063 |
| Adjusted denominator | 10424 |
| Covered (EXACT+EQUIV+PARTIAL+MISPLACED) | 10027 |
| MISSING | 304 |
| ERROR | 93 |
| **Coverage rate** | **96.19%** |
| 99% gate allows MISSING+ERROR ≤ | 120 |
| Current MISSING+ERROR | 397 |
| **Gate G1 status** | FAIL ❌ (397 > 120) |

## Verdict Distribution (post-update)

| Verdict | Count |
|---------|-------|
| EQUIVALENT | 3964 |
| EXACT | 3748 |
| INTENTIONAL_EXCLUDE | 2063 |
| PARTIAL | 2039 |
| MISSING | 304 |
| MISPLACED | 276 |
| ERROR | 93 |

## Notes

- §4.3.5 and §4.4.4 paraphrase atoms: KB has semantically equivalent content
  (paraphrases confirmed by Wave 2); classified as EQUIVALENT per verdict
  definition ("semantic consistency but with rewording").
- Tab→space normalization (16 atoms) and MD bold normalization (8 atoms):
  treated as EQUIVALENT (typographic/markup differences only).
- 5 IE candidates: 4 × `<RACEC codelist>` placeholder + 1 TRUNCATED_AT_PAGE_BOUNDARY.
- Non-prose MISSING (TABLE_ROW, HEADING, CODE_LITERAL, etc.) are NOT updated
  by this script — they are out of scope for T4b Wave work and remain MISSING
  pending T4 Tier B (CONTENT_TRUNCATED/SIBLING_DROPPED sections) processing.
