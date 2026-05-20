# A4 Rule D Independent Reviewer Audit — UNSOURCED_MANUAL N=10 HIGH-Risk Sub-Sample

**Reviewer identity:** oh-my-claudecode:scientist (claude-sonnet-4-6)
**Date:** 2026-05-20
**Task:** Independent Rule D review of 10 HIGH-risk stratum atoms (shall/must/required keyword) from the v1.3 Phase A4 N=40 UNSOURCED_MANUAL classified sample. Validates main session's 0-HALLUCINATED claim.

---

## Per-Atom Review Table

| # | atom_id | Main-session category | Reviewer category | Agree? | Reviewer reasoning (condensed) |
|---|---------|----------------------|-------------------|--------|-------------------------------|
| 1 | md_ch04_a035 | DERIVED_FROM_XLSX | REASONABLE_INFERENCE | DISAGREE (cat only) | PDF §4.1.5 (p22-23) defines Req/Exp/Perm as bullet prose — KB table restructures this into a 3-column table with a synthesized "Rule" column. Source is PDF, not xlsx variable-spec. No hallucination; category reclassified. |
| 2 | md_ch01_a077 | DERIVED_FROM_XLSX | REASONABLE_INFERENCE | DISAGREE (cat only) | PDF §1.4.1 (p10, ig34_p0010_a016) verbatim: 'Core: Contains 1 of the 3 values—"Req", "Exp", or "Perm"'. Source is PDF §1.4.1, not xlsx. No hallucination; category reclassified. |
| 3 | md_ch08_a286 | REASONABLE_INFERENCE | REASONABLE_INFERENCE | AGREE | PDF §8.7 RELSUB Assumptions #3 (p438-439) verbatim: 'If POOLID is submitted, then in any record, 1 and only 1 of USUBJID and POOLID must be populated.' Near-verbatim extraction. |
| 4 | md_ch08_a288 | REASONABLE_INFERENCE | REASONABLE_INFERENCE | AGREE | PDF §8.7 RELSUB Assumptions #5 (p438-439) verbatim: 'RSUBJID must be a USUBJID value present in the Demographics (DM) domain. RSUBJID must be populated in every record.' Near-verbatim extraction. |
| 5 | md_ch08_a294 | REASONABLE_INFERENCE | REASONABLE_INFERENCE | AGREE | Recurring SDTMIG boilerplate phrase 'Some expected and required variables not needed to illustrate the example are not shown.' Appears in PDF §8.7 Examples (p439). No hallucination. |
| 6 | md_dmDM_assn_a018 | REASONABLE_INFERENCE | REASONABLE_INFERENCE | AGREE | KB DM/assumptions.md is a verbatim copy of DM Assumption #5 from PDF §5.2: 'Study population flags should not be included in SDTM data.' Directly traceable. |
| 7 | md_dmPC_ex_a049 | REASONABLE_INFERENCE | REASONABLE_INFERENCE | AGREE | PDF §6.3.5.9.3 opening paragraph verbatim (confirmed in KB PC/assumptions.md line 21): 'Sponsors must document the concentrations used to calculate each parameter.' KB/examples.md placement is a file-routing issue, not a provenance issue. |
| 8 | md_dmSUPPQUAL_assn_a007 | DERIVED_FROM_XLSX | REASONABLE_INFERENCE | DISAGREE (cat only) | pdf_atoms.jsonl confirms ig34_p0433_a003/004/005 (p433, §8.4.1): three consecutive PDF sentences verbatim. Source is PDF §8.4.1, not xlsx. Category reclassified to REASONABLE_INFERENCE. No hallucination. |
| 9 | md_dmTR_assn_a018 | DERIVED_FROM_XLSX | REASONABLE_INFERENCE | DISAGREE (cat only) | pdf_atoms.jsonl ig34_p0353_a002 (p353, TR Assumptions #6) contains verbatim: 'Note: TREVAL must also be populated when TREVALID is populated.' Source is PDF §6.3.12.2 TR Assumptions. No hallucination; category reclassified. |
| 10 | md_dmTU_assn_a046 | DERIVED_FROM_XLSX | REASONABLE_INFERENCE | DISAGREE (cat only) | pdf_atoms.jsonl ig34_p0348_a009 (p348, TU Assumptions #8) contains verbatim: 'Note: TUEVAL must also be populated when TUEVALID is populated.' Source is PDF §6.3.12.1 TU Assumptions. No hallucination; category reclassified. |

---

## Aggregate Summary

| Metric | Count |
|--------|-------|
| Total atoms reviewed | 10 |
| AGREE (same category) | 5 |
| DISAGREE (category reclassification only) | 5 |
| HALLUCINATED flagged by reviewer | **0** |
| NEEDS_DEEPER_REVIEW | 0 |

**Nature of all 5 disagreements:** Every disagreement is a sub-category distinction between `DERIVED_FROM_XLSX` (main session) vs `REASONABLE_INFERENCE` (reviewer). In all 5 cases, the reviewer found the content source to be the SDTMIG PDF rather than the xlsx variable-spec files. This does NOT affect the HALLUCINATED count — all 5 disputed atoms have clear PDF provenance confirmed via pdf_atoms.jsonl.

**Critical finding check:** No atom received a HALLUCINATED classification. The main session's 0-HALLUCINATED claim is confirmed.

---

## Verdict

**PASS**

The independent reviewer confirms the main session's 0-HALLUCINATED finding on the HIGH-risk stratum (N=10, all atoms containing shall/must/required keywords). All 10 atoms have traceable CDISC SDTMIG v3.4 PDF sources confirmed via:
- Direct PDF page rendering (§4.1.5, §8.7 RELSUB, §5.2 DM, §6.3.5.9.3 PC, §8.4.1 SUPPQUAL)
- pdf_atoms.jsonl cross-reference (TR p353 ig34_p0353_a002, TU p348 ig34_p0348_a009, SUPPQUAL p433 ig34_p0433_a003-005)

Phase A hallucination risk verdict: **CONFIRMED SAFE** for HIGH-risk stratum. Phase A may proceed.

---

## Methodological Observations on Main Session Classifier

1. **DERIVED_FROM_XLSX over-attribution:** The main session classified 5 atoms as DERIVED_FROM_XLSX where the content is plainly from the PDF text body (not xlsx spec tables). Atoms 1, 2, 8, 9, 10 all originate from PDF prose/assumptions sections. The main session may have applied "DERIVED_FROM_XLSX" as a catch-all for "structured/tabular-looking" KB content, rather than tracing the actual source. This is a systematic heuristic bias, not a hallucination risk.

2. **Correct hallucination screening:** Despite the category mis-attribution, the main session correctly identified that these atoms are NOT hallucinated — they all have CDISC source backing. The 0-HALLUCINATED conclusion is sound.

3. **HIGH-risk stratum calibration:** The HIGH-risk stratum (shall/must/required keywords) correctly selected prescriptive normative statements, which are most likely to be verbatim or near-verbatim PDF extractions. This is appropriate risk-stratification.

4. **Recommendation:** For Phase A5 or future audits, the DERIVED_FROM_XLSX classification should be reserved for content that does not appear in PDF prose but matches xlsx variable-spec CDISC Notes/metadata fields. Content from PDF Assumptions sections should default to REASONABLE_INFERENCE.
