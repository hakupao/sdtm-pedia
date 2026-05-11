# P4a MISPLACED Discrepancies

> Phase: P4a Forward Matching
> Created: 2026-05-11
> Purpose: Aggregate table for all `MISPLACED` verdict atoms (per parent PLAN Appendix C)
> Note: Individual MISPLACED atoms do NOT open Issues; parent PLAN Appendix C §MISPLACED↔STRUCTURE_DRIFTED
>       aggregation rule: if a section has ≥10% MISPLACED rate → P4b opens STRUCTURE_DRIFTED Issue
> Last updated: 2026-05-11 (S1 complete — batches 001-025, 10 MISPLACED found)

| pdf_atom_id | pdf_parent_section | md_atom_id | md_parent_section | batch_id | notes |
|-------------|-------------------|------------|-------------------|----------|-------|
| ig34_p0023_a009 | §4.1.6 [Additional Guidance on Dataset Naming] | md_ch04_a207 | §4.2.3 [Use of "Subject" and USUBJID] | batch_008 | Content placed under wrong chapter subsection |
| ig34_p0023_a016 | §4.1.7 [Splitting Domains] | md_ch04_a049 | §4.1 [General Domain Assumptions] | batch_008 | Splitting Domains content placed under General Assumptions |
| ig34_p0024_a013 | §4.1.7.1 [Example of Splitting Questionnaires] | md_ch04_a069 | §4.1.7 [Splitting Domains] | batch_008 | Sub-section example placed in parent section |
| ig34_p0055_a022 | §4.5.3.2 [Text Strings Greater than 200 Characters in Other Variables] | md_ch04_a207 | §4.2.3 [Use of "Subject" and USUBJID] | batch_018 | §4.5.3.2 content misrouted to §4.2.3 |
| ig34_p0055_a026 | §4.5.3.2 [Text Strings Greater than 200 Characters in Other Variables] | md_ch04_a104 | §4.1.7.1 [Example of Splitting Questionnaires] | batch_018 | §4.5.3.2 content misrouted to §4.1.7.1 |
| ig34_p0056_a008 | §4.5.4 [Evaluators in the Interventions and Events Observation Classes] | md_ch04_a951 | §4.5 [General Considerations] | batch_018 | §4.5.4 content placed in parent §4.5 |
| ig34_p0057_a007 | §4.5.5 [Clinical Significance for Findings Observation Class Data] | md_ch04_a968 | §4.5 [General Considerations] | batch_018 | §4.5.5 content placed in parent §4.5 |
| ig34_p0057_a013 | §4.5.6 [Supplemental Reason Variables] | md_ch04_a975 | §4.5 [General Considerations] | batch_018 | §4.5.6 content placed in parent §4.5 |
| ig34_p0058_a001 | §4.5.7 [Presence or Absence of Prespecified Interventions and Events] | md_ch04_a987 | §4.5 [General Considerations] | batch_018 | §4.5.7 content placed in parent §4.5 |
| ig34_p0059_a001 | §4.5.8 [Accounting for Long-term Follow-up] | md_ch04_a1008 | §4.5 [General Considerations] | batch_018 | §4.5.8 content placed in parent §4.5 |

## Structure Drift Analysis (S1)

| PDF Section | MISPLACED count | Atoms in section (approx) | MISPLACED rate | P4b flag? |
|-------------|-----------------|--------------------------|----------------|-----------|
| §4.1.6–4.1.7.1 | 3 | ~30 | ~10% | borderline — monitor |
| §4.5.3.2–4.5.8 | 7 | ~50 | ~14% | YES — §4.5.x subsections collapsed into §4.5 parent |

> **Action**: P4b should open STRUCTURE_DRIFTED Issue for §4.5.x subsections (7 atoms misplaced = §4.5.3.2–4.5.8 content flattened into parent §4.5 in KB).

## ERROR Atoms (for reference — tracked separately in P4b issues)

| pdf_atom_id | batch_id | discrepancy |
|-------------|----------|-------------|
| ig34_p0041_a024 | batch_013 | PDF: 14 days **7** hours 57 min (P14DT7H57M); KB: 14 days **2** hours 57 min (P14DT2H57M) — wrong hours |
| ig34_p0078_a021 | batch_023 | KB records SEX=**F** for USUBJID ABC789-010-047 row 3; PDF shows SEX=**M** |
| ig34_p0090_a002 | batch_025 | PDF DS row 6: date 2020-03-05, DSSTDY=25; KB: date 2020-03-16, DSSTDY=28 — date and study day both wrong |
