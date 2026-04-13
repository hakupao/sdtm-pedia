# RS — Assumptions

## RS — Disease Response Use Case Assumptions

The following assumptions are unique to the RS domain disease response use case:

1. The RS domain is used to record disease response assessments as assessed by the investigator, an independent assessor, or a sponsor, using RECIST, Lugano, or other disease-specific criteria. RS also records the results of clinical classification instruments (see Section 6.3.9.3.2).

2. Disease response assessments from the RS domain may link to source data in other domains (e.g., Tumor/Lesion Results) through RSLNKGRP.

3. The RS domain disease response criteria use case may include records derived by the investigator or with a data collection tool, but not sponsor-derived records. Sponsor-derived records and results should be provided in an analysis dataset (ADaM).
   a. For disease response criteria, the BEST Response assessment records are included in the RS domain only when provided by the investigator or an independent assessor (i.e., Best responses that are derived by the sponsor for the analysis are not included in the RS domain).

4. The RSLNKGRP variable is used to provide a link between the records in a findings domain (e.g., Tumor/Lesion Results, TR; Laboratory Test Results, LB) that contribute to a record in the RS domain. Records should exist in the RELREC dataset to support this relationship. A RELREC relationship could also be defined using RSLNKID when a response evaluation or clinical classification measure relates back to another source dataset (e.g., tumor assessment in TR). The domain in which data that contribute to an assessment of response reside should not affect whether a link to the RS record through a RELREC relationship is created. For example, a set of oncology response criteria might require lab results in the LB domain, not only tumor results in the TR domain.

5. When using the RS domain to represent response evaluation or clinical classification instruments that incorporate data from other domains:
   a. Whenever possible, all source data must be represented in the topic-based domain(s) to which they pertain. For example, if a lab test value is collected and then scored for a response evaluation, the lab test value must be recorded in the LB domain using the rules that apply to that domain and the tests being represented.
   b. In the oncology setting, the response to therapy would often be determined, at least in part, from data in the TR domain. Data from other sources (in other SDTM domains) might also be used in an assessment of response (e.g., lab test results, assessments of symptoms).
   c. Oncology response assessments sometimes include symptomatic deterioration. Symptomatic deterioration may be considered as non-radiologic evidence of progressive disease. Symptomatic deterioration is recorded in RS with RSTEST = "Symptomatic Deterioration" and the standardized response (e.g., "PD") in RSSTRESC.
   d. In all cases, RSSTRESC should be populated as indicated in controlled terminology.

6. Best response, duration of response, or the progression to prior therapies and follow-up therapies may be represented in the RS domain.
   a. The record in RS may be related and linked to record(s) in Concomitant/Prior Medications (CM) using CMLNKGRP and RSLNKGRP. Likewise, the link to Procedures (PR; e.g., radiotherapy, surgery) would be made using PRLNKGRP.
   b. If the criteria used to determine the response is unknown or not collected, this is represented as RSCAT = "UNSPECIFIED".

7. The evaluator identifier variable (RSEVALID) can be used in conjunction with RSEVAL to provide additional detail of who is providing the assessment. For example, RSEVAL = "INDEPENDENT ASSESSOR" and RSEVALID = "RADIOLOGIST 1" may further qualify the RSEVALID variable. RSEVALID may be subject to controlled terminology but may also represent free text values depending on the use case. When used with disease response data, RSEVALID is subject to MEDEVAL controlled terminology.

8. In cases where an independent assessor identifies one of multiple assessments/measurements to be the accepted one, the accepted record flag variable (RSACPTFL) identifies records that have been determined to be the accepted assessments/measurements by an independent assessor. This flag would be provided by an independent assessor when multiple assessors (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provide assessments or evaluations at the same time point or for an overall evaluation.
   a. RSACPTFL should not be derived by the sponsor. If a derivation is needed to make the record selection, then this derivation should be done in the analysis dataset (ADaM).

9. Disease recurrence can be represented in the RS domain using RSTEST = "Disease Recurrence Indicator" to indicate that there was an assessment of whether there was disease recurrence. The RSCAT = "PROTOCOL DEFINED RESPONSE CRITERIA" can be used to indicate that the response assessment of disease recurrence was based on protocol-specified criteria rather than published response criteria.

10. When a disease response result is based on multiple procedures/scans/images/physical exams performed on different dates, RSDTC may be derived.

11. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the RS domain, but the following qualifiers would not generally be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STRNC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

## RS — Clinical Classifications Use Case Assumptions

The following assumptions are unique to the RS domain clinical classifications use case:

1. Clinical classifications are named instruments whose output is an ordinal or categorical score that serves as a surrogate for or ranking of disease status or other physiological or biological status.
   a. Clinical classifications may be based solely on objective data from clinical records, or they may involve a clinical judgment or interpretation of directly observable signs, behaviors, or other physical manifestations related to a condition or subject status. These physical manifestations may be findings (e.g., lab results, vital signs, clinical events) that are typically represented in other SDTM domains.

2. RSCAT is used to group a set of assessments based on a clinical classification. One of the codelists for RSCAT is CCCAT. The CCCAT codelist contains CDISC Controlled Terminology for clinical classifications instruments.

3. When using the RS domain to represent a clinical classification instrument that incorporates data from other domains:
   a. Whenever possible, all source data must be represented in the topic-based domain(s) to which they pertain. For example, if a lab test value is collected and then scored for a response evaluation or clinical classification instrument, the lab test value must be recorded in the LB domain using the rules that apply to that domain and the tests being represented.
   b. If the source value is directly collected on the clinical classification instrument, then the values from the source record may be transcribed to the corresponding RS record, with RSORRES and RSORRESU populated to agree with the units shown on the clinical classification instrument, which may be different from the sponsor's usual practice for original and standard units.
   c. If a clinical classification uses a source value by comparing it to a range (e.g., "2-5", ">3"), then the source value will exist only in the source domain; the range is represented in the corresponding RS record in RSORRES and RSORRESU.
   d. In all cases, RSSTRESC/RSSTRESN should be populated with the assigned ordinal score as indicated on the instrument.

## QRS Shared Assumptions

The QRS Shared Assumptions (see FT assumptions) also apply to the Clinical Classifications use case of the RS domain, but not the Disease Response use case.
