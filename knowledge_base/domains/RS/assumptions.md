# RS — Assumptions

## RS – Description/Overview

A findings domain for the assessment of disease response to therapy, or clinical classification based on published criteria.

Data in this domain may or may not be collected by means of a standard CRF.

- Clinical classification instruments usually have a standard CRF for data capture, but also may instead be based on an evaluator providing response evaluations based on published criteria.
- Oncology response criteria are evaluated based on published criteria.
- Additional disease classifications or scoring systems (e.g., staging criteria) are based on published criteria.
- There are separate supplements prepared for clinical classification instruments and therapeutic-area disease response criteria use cases.

## RS – Specification

rs.xpt, Disease Response and Clin Classification — Findings. One record per response assessment or clinical classification assessment per time point per visit per subject per assessor per medical evaluator, Tabulation.

Assumptions and examples are different for the disease response and clinical classifications use cases.

## §6.3.9.3.1 Disease Response Use Case

## RS — Disease Response Use Case Assumptions

Assumptions here discuss the oncology use case, which is the only disease-response use case that currently exists.

1. RSCAT is used to group a set of assessments based on a disease response criterion (published or protocol-defined). One of the codelists for RSCAT is ONCRSCAT. The ONCRSCAT codelist contains controlled terminology for oncology disease response assessments.

2. Oncology response criteria assess the change in tumor burden, an important feature of the clinical evaluation of cancer therapeutics: Both tumor shrinkage (objective response) and disease progression are useful endpoints in cancer clinical trials. The RS domain is applicable for representing responses to assessment criteria such as RECIST[1] or Lugano classification.[2] The SDTM domain examples provided reference RECIST. Disease Response supplements will be developed as 1 supplement per response criterion and will contain criterion-specific guidance and examples.
   a. CDISC submission values and definitions in the ONCRSR codelist have been developed to facilitate reuse by keeping the definitions focused on the meaning of the result rather than on relating them to a specific published criterion or a particular tumor type. CDISC submission values and definitions are intended to apply across multiple tumor types, imaging modalities, therapeutic agents, and published criterion. This means that there may be cases where the appropriate ONCRSR CDISC submission value may not exactly match the term used in the published criterion. It is expected that clinicians should use the precise criterion definitions outlined in the individual papers to assign the appropriate response according to the CDISC submission values.
   b. The terms "response" and "remission" are commonly used to describe functionally synonymous terms. "Response" is used in CDISC submission values based on the following agreement: FDA, CDISC, NCI-EVS, and select academic experts came to consensus that because the words "response" (used in solid tumors as an indicator of a favorable change in tumor burden) and "remission" (used in non-solid tumors) were functionally synonymous, 2 distinct terms were not required to be added to the ONCRSR codelist. Instead, "remission" has been added as a synonym in all instances where "response" is used in a CDISC submission value, for response values used in both solid and non-solid tumors. The FDA expects a single CDISC submission value to be submitted for both solid and non-solid tumors.
   c. Refer to the Controlled Terminology Rules for Oncology for more information (available at https://www.cdisc.org/standards/terminology/controlled-terminology).
   d. RSTESTCD/RSTEST values for this domain are published as Controlled Terminology. For some RSTESTCD/RSTEST values, CDISC CT includes codelists for use with RSORRES. The associations between the test values and results are in the Oncology codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

3. The RS domain disease response criteria use case may include records derived by the investigator or with a data collection tool, but not sponsor-derived records. Sponsor-derived records and results should be provided in an analysis dataset (ADaM).
   a. For disease response criteria, the BEST Response assessment records are included in the RS domain only when provided by the investigator or an independent assessor (i.e., Best responses that are derived by the sponsor for the analysis are not included in the RS domain).

4. The RSLNKGRP variable is used to provide a link between the records in a findings domain (e.g., Tumor/Lesion Results, TR; Laboratory Test Results, LB) that contribute to a record in the RS domain. Records should exist in the RELREC dataset to support this relationship. A RELREC relationship could also be defined using RSLNKID when a response evaluation or clinical classification measure relates back to another source dataset (e.g., tumor assessment in TR). The domain in which data that contribute to an assessment of response reside should not affect whether a link to the RS record through a RELREC relationship is created. For example, a set of oncology response criteria might require lab results in the LB domain, not only tumor results in the TR domain.

5. When using the RS domain to represent response evaluation or clinical classification instruments that incorporate data from other domains:
   a. Whenever possible, all source data must be represented in the topic-based domain(s) to which they pertain. For example, if a lab test value is collected and then scored for a response evaluation, the lab test value must be recorded in the LB domain using the rules that apply to the domain and the tests being represented.
   b. In the oncology setting, the response to therapy would often be determined, at least in part, from data in the TR domain. Data from other sources (in other SDTM domains) might also be used in an assessment of response (e.g., lab test results, assessments of symptoms).
   c. Oncology response assessments sometimes include symptomatic deterioration.

      Symptomatic deterioration may be considered as non-radiologic evidence of progressive disease. Symptomatic deterioration is recorded in RS with RSTEST = "Symptomatic Deterioration" and the standardized response (e.g., "PD") in RSSTRESC.

      | RSTESTCD | RSTEST | RSCAT | RSORRES | RSSTRESC |
      |----------|--------|-------|---------|----------|
      | SYMPTDTR | Symptomatic Deterioration | PROTOCOL DEFINED RESPONSE CRITERIA | Increased weakness and weight loss | PD |

   d. In all cases, RSSTRESC should be populated as indicated in controlled terminology.

6. Best response, duration of response, or the progression to prior therapies and follow-up therapies may be represented in the RS domain.
   a. The record in RS may be related and linked to record(s) in Concomitant/Prior Medications (CM) using CMLNKGRP and RSLNKGRP. Likewise, the link to Procedures (PR; e.g., radiotherapy, surgery) would be made using PRLNKGRP.
   b. If the criteria used to determine the response is unknown or not collected, this is represented as RSCAT = "UNSPECIFIED".

7. The evaluator identifier variable (RSEVALID) can be used in conjunction with RSEVAL to provide additional detail of who is providing the assessment. For example, RSEVAL = "INDEPENDENT ASSESSOR" and RSEVALID = "RADIOLOGIST 1" may further qualify the RSEVALID variable. RSEVALID may be subject to controlled terminology but may also represent free text values depending on the use case. When used with disease response data, RSEVALID is subject to MEDEVAL controlled terminology.

8. In cases where an independent assessor identifies one of multiple assessments/measurements to be the accepted one, the accepted record flag variable (RSACPTFL) identifies records that have been determined to be the accepted assessments/measurements by an independent assessor. This flag would be provided by an independent assessor when multiple assessors (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provide assessments or evaluations at the same time point or for an overall evaluation.
   a. RSACPTFL should not be derived by the sponsor. If a derivation is needed to make the record selection, then this derivation should be done in the analysis dataset (ADaM).

9. Disease recurrence can be represented in the RS domain using RSTEST = "Disease Recurrence Indicator" to indicate that there was an assessment of whether there was disease recurrence. The RSCAT = "PROTOCOL DEFINED RESPONSE CRITERIA" can be used to indicate that the response assessment of disease recurrence was based on protocol-specified criteria rather than published response criteria.

10. When a disease response result is based on multiple procedures/scans/images/physical exams performed on different dates, RSDTC may be derived.

11. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the RS domain, but the following qualifiers would not generally be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

## §6.3.9.3.2 Clinical Classifications Use Case

## RS — Clinical Classifications Use Case Assumptions

The following assumptions are unique to the RS domain clinical classifications use case:

1. Clinical classifications are named instruments whose output is an ordinal or categorical score that serves as a surrogate for or ranking of disease status or other physiological or biological status.
   a. Clinical classifications may be based solely on objective data from clinical records, or they may involve a clinical judgment or interpretation of directly observable signs, behaviors, or other physical manifestations related to a condition or subject status. These physical manifestations may be findings (e.g., lab results, vital signs, clinical events) that are typically represented in other SDTM domains.

2. RSCAT is used to group a set of assessments based on a clinical classification. One of the codelists for RSCAT is CCCAT. The CCCAT codelist contains CDISC Controlled Terminology for clinical classifications instruments.

3. When using the RS domain to represent a clinical classification instrument that incorporates data from other domains:
   a. Whenever possible, all source data must be represented in the topic-based domain(s) to which they pertain. For example, if a lab test value is collected and then scored for a response evaluation or clinical classification instrument, the lab test value must be recorded in the LB domain using the rules that apply to that domain and the tests being represented.
   b. If the source value is directly collected on the clinical classification instrument, then the values from the source record may be transcribed to the corresponding RS record, with RSORRES and RSORRESU populated to agree with the units shown on the clinical classification instrument, which may be different from the sponsor’s usual practice for original and standard units.
   c. If a clinical classification uses a source value by comparing it to a range (e.g., "2-5", ">3"), then the source value will exist only in the source domain; the range is represented in the corresponding RS record in RSORRES and RSORRESU.
   d. In all cases, RSSTRESC/RSSTRESN should be populated with the assigned ordinal score as indicated on the instrument.

## QRS Shared Assumptions

The following assumptions are common to the FT and QS domains as well as the Clinical Classifications use case of the RS domain (not the Disease Response use case of RS):

1. The name of a QRS instrument is described under the variable --CAT in the relevant QRS domain (i.e., FT, QS, RS), and may be either abbreviations or longer names. For example, "ADAS-COG", "BPI SHORT FORM", and "APACHE II" are all --CATs which are shortened names for the instruments they represent, whereas "4 STAIR ASCEND" is the FTCAT for the instrument of the same name. Sponsors should always reference CDISC Controlled Terminology.
   a. The QRS Naming Rules for --CAT, --TEST, and --TESTCD and the list of QRS instruments that have published CDISC Controlled Terminology with NCI/EVS are available at: https://www.cdisc.org/standards/terminology/controlled-terminology.
   b. Refer to the following CDISC Controlled Terminology codelists for QRS instrument --CAT terminology:
      i. Category of Clinical Classification
      ii. Category of Functional Test
      iii. Category of Questionnaire
   c. QRS --TESTCD/--TEST terminology codelists are listed separately by instrument name.

2. Names of subcategories for groups of items/questions are described under the --SCAT variable.
   a. --SCAT values are not included in the CDISC Controlled Terminology system but rather controlled as described in the QRS supplements in which they are used.

3. There are cases where QRS CRFs do not include numeric “standardized responses” assigned to text responses (e.g., mild, moderate, severe being 1, 2, 3). It is clearly in everyone's best interest to include the numeric “standardized responses” in the SDTMIG QRS dataset. This is only done when the numeric “standardized responses” are documented in the QRS CRF instructions, a user manual, a website specific to the QRS instrument, or another reference document that provides a clear explanation and rationale for providing them in the SDTMIG QRS dataset.

4. Sponsors should always consult published QRS supplements for guidance on submitting derived information in a SDTMIG QRS domain. Derived variable results in QRS are usually considered captured data. If sponsors operationally derive variable results, then the derived records that are submitted in a QRS domain should be flagged by --DRVFL.
   a. The following rules apply for “total”-type scores in QRS datasets.
      i. QRS subtotal, total, etc. scores listed on the CRF are considered captured data and are included in the instrument’s controlled terminology.
      ii. QRS subtotal, total, etc. scores not listed on the CRF but documented in an associated instrument manual or reference paper are considered captured data and are included in the instrument’s controlled terminology.
      iii. QRS subtotal, total, etc. scores not listed on the CRF, but known to be included in eData by sponsors are considered as captured data, are included in the instrument’s controlled terminology. The QRS instrument’s CT is considered extensible for this case and the subtotal or total score should be requested to be added.
         1. Any imputations/calculations done to numeric “standardized responses” to produce the total score via transforming numeric “standardized responses” in any way would be done as ADaM derivations.
   b. The QRS instrument subtotal or total score, which is the sum of the numeric responses for an instrument, is populated in --ORRES, --STRESC, and --STRESN. It is considered a captured subtotal or total score without any knowledge of the sponsor-data management processes related to the score.
      i. If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their eCRF process to derive subtotal and total scores. An investigator-derived score written on a CRF will be considered a captured score and not flagged. When subtotal and total scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y". However, when the subtotal and total scores are received from a central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).

5. The variable --REPNUM variable is populated when there are multiple repeats of the same question. When records are related to the first trial of the question, the variable --REPNUM should be set to "1". When records are related to the second trial of the same question, --REPNUM should be set to "2", and so forth.

6. The actual version number of an instrument is represented in the --CAT value as designated by the QRS Terminology Team. If it is determined that this is not the case for an instrument:
   a. Notify the QRS Terminology Team that the instrument has a specific or multiple version numbers. This team will assist in providing a resolution on how the situation will be handled.
   b. Consider the use of the --GRPID variable to indicate the instrument's version number prior to a decision by the QRS Terminology Team.
   c. The sponsor is expected to provide information about the version used for each QRS instrument in the metadata (using the Comments column in the Define-XML document). This could be provided as value-level metadata for --CAT.
   d. The sponsor is expected to provide information about the scoring rules in the metadata.

7. If the variable --TEST is represented with verbatim text >40 characters, represent the abbreviated meaningful text in --TEST within 40 characters and describe the full text of the item in the study metadata. If the verbatim item response (e.g., --QSORRES) is >200 characters, represent the abbreviated meaningful text in QSORRES within the 200 characters and describe the full text in the study metadata; see Section 4 of the QRS supplement. See Section 4.5.3, Text Strings that Exceed the Maximum Length for General Observation-class Domain Variables, for further information.
   a. The instrument’s annotated CRF can also be used as a reference for the full text in both of these situations.

8. --EVAL and --EVALID must not be used to model QRS data in SDTM. These variables have had various interpretations on QRS CRFs and were used to represent a multitude of evaluator information about QRS instruments. This has made it more difficult for users of SDTM QRS data to interpret this data and more difficult to pool data for analyses. If needed, supplemental qualifiers may be used to represent this data. Updated information on a proposed solution to this issue will be posted on the CDISC QRS webpage (https://www.cdisc.org/standards/foundational/qrs).

9. All standard QRS supplement development is coordinated with the CDISC SDS QRS Subteam as the governing body. The process involves drafting the controlled terminology and defining instrument-specific standardized values for qualifier, timing, and result variables to populate the SDTMIG FT, QS, and RS domains. These supplements are developed based on user demand and therapeutic area standards development needs. Sponsors should always consult the CDISC website to review the terminology and supplements prior to modeling any QRS instrument.
   a. Sponsors may participate and/or request the development of additional QRS supplements and terminology through the CDISC SDS QRS subteam and the Controlled Terminology QRS subteam.
      i. Once generated, the QRS supplement is posted on the CDISC website (https://www.cdisc.org/standards/foundational/qrs).
      ii. Sponsors should always consult the published QRS supplements for guidance on submitting derived information in SDTMIG-based domains.

10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.
