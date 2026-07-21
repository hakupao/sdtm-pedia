# SDTMIG v3.4 --- Domain Models: Findings — Part 7

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 7/8 — 6.3.8-6.3.9: PE, QRS Domains (FT, QS, RS)
> **Original:** `SDTMIG34_06_DomainModels_Findings.md`
> **Related:** `SDTMIG34_06a_DomainModels_Findings.md`, `SDTMIG34_06b_DomainModels_Findings.md`, `SDTMIG34_06c_DomainModels_Findings.md`, `SDTMIG34_06d_DomainModels_Findings.md`, `SDTMIG34_06e_DomainModels_Findings.md`, `SDTMIG34_06f_DomainModels_Findings.md`, `SDTMIG34_06h_DomainModels_Findings.md`

---

### 6.3.8 Physical Examination (PE)

> **PE - Proposed Removal of --MODIFY and --BODSYS**
> In the version of the SDTM associated with the next version of the SDTMIG, --MODIFY is being considered for deprecation as a qualifier variable for findings class domains and --BODSYS will be considered for restriction to use in nonclinical studies.

> **PE - Alignment with CDASH Best Practice**
> In the CDASH "Best Practice" approach as described in the CDASHIG, which is becoming common in human clinical trials, the PE domain is not used to record the "findings" from a physical exam. The abnormalities found are recorded in the appropriate events-class domain. An abnormality is recorded in Medical History (MH) when found to previously exist at a baseline or screening examination. Abnormalities identified after baseline or screening, or worsening abnormalities, are recorded on the Adverse Events (AE) form (or possibly on a Clinical Events form). When following this approach, the PE domain is not used in SDTM. The Procedure (PR) domain is used to document the examination details (e.g., occurrence, date) using a Procedure record for each physical exam.

#### PE – Description/Overview

A findings domain that contains findings observed during a physical examination where the body is evaluated by inspection, palpation, percussion, and auscultation.

#### PE – Specification

pe.xpt, Physical Examination — Findings. One record per body system or abnormality per visit per subject, Tabulation.

**Structure:** One record per body system or abnormality per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | PE |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | PESEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | PEGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | PESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 7 | PETESTCD | Body System Examined Short Name | Char | Topic | Req |  |
| 8 | PETEST | Body System Examined | Char | Synonym Qualifier | Req |  |
| 9 | PEMODIFY | Modified Reported Term | Char | Synonym Qualifier | Perm |  |
| 10 | PECAT | Category for Examination | Char | Grouping Qualifier | Perm |  |
| 11 | PESCAT | Subcategory for Examination | Char | Grouping Qualifier | Perm |  |
| 12 | PEBODSYS | Body System or Organ Class | Char | Record Qualifier | Perm |  |
| 13 | PEORRES | Verbatim Examination Finding | Char | Result Qualifier | Exp |  |
| 14 | PEORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 15 | PESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 16 | PESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 17 | PEREASND | Reason Not Examined | Char | Record Qualifier | Perm |  |
| 18 | PELOC | Location of Physical Exam Finding | Char | Record Qualifier | Perm | C74456 |
| 19 | PELAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| 20 | PEMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 21 | PELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| 22 | PEBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 23 | PEEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 24 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 25 | VISIT | Visit Name | Char | Timing | Perm |  |
| 26 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 27 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 28 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 29 | PEDTC | Date/Time of Examination | Char | Timing | Exp | ISO 8601 datetime or interval |
| 30 | PEDY | Study Day of Examination | Num | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **PESEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number.
- **PEGRPID**: Used to link together a block of related records in a single domain for a subject.
- **PESPID**: Sponsor-defined reference number. Perhaps preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF.
- **PETESTCD**: Short name of a part of the body examined in a physical examination. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HEAD", "ENT". If the results of the entire physical examination are represented in one record, value should be "PHYSEXAM".
- **PETEST**: Long name of a part of the body examined in a physical examination. The value in PETEST cannot be longer than 40 characters. Examples: "Head", "Ear/Nose/Throat". If the results of the entire physical examination are represented in one record, value should be "Physical Examination".
- **PEMODIFY**: If the value of PEORRES is modified for coding purposes, then the modified text is placed here.
- **PECAT**: Used to define a category of topic-variable values. Example: "GENERAL".
- **PESCAT**: Used to define a further categorization of --CAT values.
- **PEBODSYS**: Body system or organ class (e.g., MedDRA SOC) that is involved for a finding from the standard hierarchy for dictionary-coded results.
- **PEORRES**: Text description of any abnormal findings. If the examination was completed and there were no abnormal findings, the value should be "NORMAL". If the examination was not performed on a particular body system, or at the subject level, then the value should be null, and "NOT DONE" should appear in PESTAT.
- **PEORRESU**: Original units in which the data were collected. The unit for PEORRES.
- **PESTRESC**: If there are findings for a body system, then either the dictionary preferred term (if findings are coded using a dictionary) or PEORRES (if findings are not encoded) should appear here. If PEORRES is null, PESTRESC must be null.
- **PESTAT**: Used to indicate exam not done. Must be null if a result exists in PEORRES/PESTRESC.
- **PEREASND**: Describes why an examination was not performed or why a body system was not examined. Example: "SUBJECT REFUSED". Used in conjunction with PESTAT when value is "NOT DONE".
- **PELOC**: Anatomical location of the subject relevant to the collection of the measurement. Example: "ARM" for skin rash.
- **PELAT**: Qualifier for anatomical location or specimen further detailing laterallity. Examples: "RIGHT", "LEFT", "BILATERAL".
- **PEMETHOD**: Method of the test or examination. Examples: "PALPATION", "PERCUSSION".
- **PELOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.
- **PEBLFL**: A baseline defined by the sponsor (could be derived in the same manner as PELOBXFL or ABLFL, but is not required to be). The value should be "Y" or null. Note that PEBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.
- **PEEVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Example: "INVESTIGATOR".
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of VISIT. Should be an integer.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the observation date/time of the physical exam finding.
- **PEDTC**: Date and time of the physical examination represented in ISO 8601 character format.
- **PEDY**: Study day of physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

#### PE – Assumptions

1. PE findings reflect the presence or absence of physical signs of disease or abnormality observed during a general physical examination. Multiple body systems are assessed during a physical examination, often starting at the head and ending at the toes, where the body is evaluated by inspection, palpation (feeling with the hands), percussion (tapping with fingers), and auscultation (listening). The examination often includes macro assessments (e.g., normal/abnormal) of appearance, general health, behavior, and body system review from head to toe.

    a. Evaluation of targeted body systems (e.g., cardiovascular, ophthalmic, reproductive) as part of therapeutic specific assessments should be represented in the appropriate body system domain (e.g., CV, OE, RP, respectively).

    b. See CDASHIG Section 8.3.11, PE - Physical Examination (available at https://www.cdisc.org/standards/foundational/cdash/), for additional collection guidance.

2. Abnormalities observed during a physical examination may be encoded. When collected/reported as a PE finding, the verbatim value is represented in PEORRES and the encoded value in PESTRESC. When collected/reported as medical history or an adverse event, the verbatim value is represented in MHTERM or AETERM and the encoded value is represented in MHDECOD or AEDECOD, respectively.
3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the PE domain, but the following qualifiers would generally not be used: --XFN, --NAM, --LOINC, --FAST, --TOX, --TOXGR.

#### PE – Examples

**Example 1**

This example shows data for 1 subject collected at 1 visit. The data come from a general physical examination.

**Rows 1-2, 6:** Show how PESTRESC is populated if result is "NORMAL".

**Rows 3-5:** Show how PESPID is used to show the sponsor-defined identifier, which in this case is the CRF sequence number used for identifying abnormalities within a body system. Additionally, the abnormalities were encoded; PESTRESC represents the MedDRA Preferred Term and PEBODSYS represents the MedDRA system organ class.

*pe.xpt*

| Row | STUDYID | DOMAIN | USUBJID | PESEQ | PESPID | PETESTCD | PETEST | PELOC | PELAT | PEBODSYS | PEORRES | PESTRESC | VISITNUM | VISIT | VISITDY | PEDTC | PEDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | PE | ABC-001-001 | 1 |  | HEAD | Head |  |  |  | NORMAL | NORMAL | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 2 | ABC | PE | ABC-001-001 | 2 |  | ENT | Ear/Nose/Throat |  |  |  | NORMAL | NORMAL | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 3 | ABC | PE | ABC-001-001 | 3 | 1 | SKIN | Skin | FACE |  | Skin and subcutaneous tissue disorder | ACNE | Acne | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 4 | ABC | PE | ABC-001-001 | 4 | 2 | SKIN | Skin | HANDS |  | Skin and subcutaneous tissue disorder | DERMATITIS | Dermatitis | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 5 | ABC | PE | ABC-001-001 | 5 | 3 | SKIN | Skin | ARM | LEFT | Skin and subcutaneous tissue disorder | SKIN RASH | Rash | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 6 | ABC | PE | ABC-001-001 | 6 |  | HEART | Heart |  |  |  | NORMAL | NORMAL | -1 | BASELINE | -1 | 1999-06-06 | -3 |

---
### 6.3.9 Questionnaires, Ratings, and Scales (QRS) Domains (FT, QS, RS)

This section includes domains used to represent data from questionnaires, ratings, and scales (QRS). The Functional Tests (FT) and Questionnaires (QS) sections each provide an overview, specifications, assumptions, and examples for these domains. The Disease Response and Clin Classification (RS) section contains an overview and specification for that domain; assumptions and examples are provided in subsections for the 2 use cases within the RS domain (i.e., disease response use case, clinical classifications use case).

The SDTMIG includes the FT, QS, and RS domains for QRS findings for different QRS concepts. These differ only in concept, in domain code, and in informative content such as examples. A set of shared assumptions is included in each of the domain sections.

CDISC develops controlled terminology and publishes supplements for individual QRS instruments when the instrument is in the public domain or when permission has been granted by the copyright holder.

- Controlled Terminology release downloads and information about the CT development process are available at: https://www.cdisc.org/standards/terminology/controlled-terminology.
- QRS supplements, implementation documents, and information about the QRS development process are available at: https://www.cdisc.org/standards/foundational/qrs.

Each QRS supplement includes instrument-specific implementation assumptions, a dataset example, SDTM mapping strategies, and a list of any applicable supplemental qualifiers. SDTM annotated CRFs are also provided where available.
#### 6.3.9.1 Functional Tests (FT)

##### FT – Description/Overview
A findings domain that contains data for named, stand-alone, task-based evaluations designed to provide an assessment of mobility, dexterity, or cognitive ability.

##### FT – Specification
ft.xpt, Functional Tests — Findings. One record per Functional Test finding per time point per visit per subject, Tabulation.

**Structure:** One record per Functional Test finding per time point per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | FT |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | FTSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | FTGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | FTREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | FTSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | FTTESTCD | Short Name of Test | Char | Topic | Req |  |
| 9 | FTTEST | Name of Test | Char | Synonym Qualifier | Req |  |
| 10 | FTCAT | Category | Char | Grouping Qualifier | Req | C115304 |
| 11 | FTSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |
| 12 | FTPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |
| 13 | FTORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 14 | FTORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 15 | FTSTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |
| 16 | FTSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 17 | FTSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 18 | FTSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 19 | FTREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 20 | FTXFN | External File Path | Char | Record Qualifier | Perm |  |
| 21 | FTNAM | Vendor Name | Char | Record Qualifier | Perm |  |
| 22 | FTMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C158113 |
| 23 | FTLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 24 | FTBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 25 | FTDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 26 | FTREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |
| 27 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 28 | VISIT | Visit Name | Char | Timing | Perm |  |
| 29 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 30 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 31 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 32 | FTDTC | Date/Time of Test | Char | Timing | Exp | ISO 8601 datetime or interval |
| 33 | FTDY | Study Day of Test | Num | Timing | Perm |  |
| 34 | FTTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 35 | FTTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 36 | FTELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 37 | FTTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 38 | FTRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **FTSEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number.
- **FTGRPID**: Optional group identifier, used to link together a block of related records within a subject in a domain.
- **FTREFID**: Optional internal or external identifier.
- **FTSPID**: Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the Test page.
- **FTTESTCD**: Short character value for FTTEST, which can be used as a column name when converting a dataset from a vertical format to a horizontal format. The value cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FTTESTCD cannot contain characters other than letters, numbers, or underscores.; Controlled terminology for FTTESTCD is published in separate codelists for each instrument. See https://www.cdisc.org/standards/terminology/controlled-terminology for values for FTTESTCD. Examples: "W250101", "W25F0102".
- **FTTEST**: Verbatim name of the question used to obtain the finding. The value in FTTEST cannot be longer than 40 characters.; Controlled terminology for FTTEST is published in separate codelists for each instrument. See https://www.cdisc.org/standards/terminology/controlled-terminology for values for FTTEST. Examples: "W2501-25 Foot Walk Time", "W25F-More Than Two Attempts".
- **FTCAT**: Used to specify the functional test in which the functional test question identified by FTTEST and FTTESTCD was included.
- **FTSCAT**: Used to define a further categorization of FTCAT values.
- **FTPOS**: Position of the subject during the test. Examples: "SUPINE", "STANDING", "SITTING".
- **FTORRES**: Result of the measurement or finding as originally received or collected.
- **FTORRESU**: Original units in which the data were collected. Unit for FTORRES.
- **FTSTRESC**: Contains the result value for all findings, copied or derived from FTORRES in a standard format or in standard units. FTSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FTSTRESN.
- **FTSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from FTSTRESC. FTSTRESN should store all numeric test results or findings.
- **FTSTRESU**: Standardized units used for FTSTRESC and FTSTRESN.
- **FTSTAT**: Used to indicate that a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".
- **FTREASND**: Describes why a test was not done, or a test was attempted but did not generate a result. Used in conjunction with FTSTAT when value is "NOT DONE".
- **FTXFN**: File path to an external file.
- **FTNAM**: Name or identifier of the vendor or laboratory that provided the test results.
- **FTMETHOD**: Method of the test or examination.
- **FTLOBXFL**: Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **FTBLFL**: A baseline defined by the sponsor (could be derived in the same manner as FTLOBXFL or ABLFL, but is not required to be). The value should be "Y" or null. Note that FTBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.
- **FTDRVFL**: Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.
- **FTREPNUM**: The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter.
- **VISITDY**: Planned study day of VISIT based upon RFSTDTC in Demographics. Should be an integer.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the observation date/time of the functional tests finding.
- **FTDTC**: Collection date and time of functional test.
- **FTDY**: Actual study day of test expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **FTTPT**: Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See FTTPTNUM and FTTPTREF.
- **FTTPTNUM**: Numeric version of planned time point used in sorting.
- **FTELTM**: Planned elapsed time relative to a planned fixed reference (FTTPTREF). Not a clock time or a date/time variable, but an interval, represented as ISO duration.
- **FTTPTREF**: Description of the fixed reference point referred to by FTELTM, FTTPTNUM, and FTTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **FTRFTDTC**: Date/time for a fixed reference time point defined by FTTPTREF.

##### FT – Assumptions
The following assumptions are unique to the FT domain:
1. A functional test is not a subjective assessment of how the subject generally performs a task, but rather an objective measurement of the performance of the task by the subject in a specific instance.
2. Functional tests have documented methods for administration and analysis and require a subject to perform specific activities that are evaluated and recorded. Most often, functional tests are direct quantitative measurements. Examples of functional tests include the Timed 25-Foot Walk, 9-Hole Peg Test, and the Hauser Ambulation Index.

**QRS Shared Assumptions**

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
3. There are cases where QRS CRFs do not include numeric "standardized responses" assigned to text responses (e.g., mild, moderate, severe being 1, 2, 3). It is clearly in everyone's best interest to include the numeric "standardized responses" in the SDTMIG QRS dataset. This is only done when the numeric "standardized responses" are documented in the QRS CRF instructions, a user manual, a website specific to the QRS instrument, or another reference document that provides a clear explanation and rationale for providing them in the SDTMIG QRS dataset.
4. Sponsors should always consult published QRS supplements for guidance on submitting derived information in a SDTMIG QRS domain. Derived variable results in QRS are usually considered captured data. If sponsors operationally derive variable results, then the derived records that are submitted in a QRS domain should be flagged by --DRVFL.
    a. The following rules apply for "total"-type scores in QRS datasets.
        i. QRS subtotal, total, etc. scores listed on the CRF are considered captured data and are included in the instrument's controlled terminology.
        ii. QRS subtotal, total, etc. scores not listed on the CRF but documented in an associated instrument manual or reference paper are considered captured data and are included in the instrument's controlled terminology.
        iii. QRS subtotal, total, etc. scores not listed on the CRF, but known to be included in eData by sponsors are considered as captured data, are included in the instrument's controlled terminology. The QRS instrument's CT is considered extensible for this case and the subtotal or total score should be requested to be added.
            1. Any imputations/calculations done to numeric "standardized responses" to produce the total score via transforming numeric "standardized responses" in any way would be done as ADaM derivations.
    b. The QRS instrument subtotal or total score, which is the sum of the numeric responses for an instrument, is populated in --ORRES, --STRESC, and --STRESN. It is considered a captured subtotal or total score without any knowledge of the sponsor-data management processes related to the score.
        i. If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their eCRF process to derive subtotal and total scores. An investigator-derived score written on a CRF will be considered a captured score and not flagged. When subtotal and total scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y". However, when the subtotal and total scores are received from a central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).
5. The variable --REPNUM variable is populated when there are multiple repeats of the same question. When records are related to the first trial of the question, the variable --REPNUM should be set to "1". When records are related to the second trial of the same question, --REPNUM should be set to "2", and so forth.
6. The actual version number of an instrument is represented in the --CAT value as designated by the QRS Terminology Team. If it is determined that this is not the case for an instrument:
    a. Notify the QRS Terminology Team that the instrument has a specific or multiple version numbers. This team will assist in providing an resolution on how the situation will be handled.
    b. Consider the use of the --GRPID variable to indicate the instrument's version number prior to a decision by the QRS Terminology Team.
    c. The sponsor is expected to provide information about the version used for each QRS instrument in the metadata (using the Comments column in the Define-XML document). This could be provided as value-level metadata for --CAT.
    d. The sponsor is expected to provide information about the scoring rules in the metadata.
7. If the variable --TEST is represented with verbatim text >40 characters, represent the abbreviated meaningful text in --TEST within 40 characters and describe the full text of the item in the study metadata. If the verbatim item response (e.g., --QSORRES) is >200 characters, represent the abbreviated meaningful text in QSORRES within the 200 characters and describe the full text in the study metadata; see Section 4 of the QRS supplement. See Section 4.5.3, Text Strings that Exceed the Maximum Length for General Observation-class Domain Variables, for further information.
    a. The instrument's annotated CRF can also be used as a reference for the full text in both of these situations.
8. --EVAL and --EVALID must not be used to model QRS data in SDTM. These variables have had various interpretations on QRS CRFs and were used to represent a multitude of evaluator information about QRS instruments. This has made it more difficult for users of SDTM QRS data to interpret this data and more difficult to pool data for analyses. If needed, supplemental qualifiers may be used to represent this data. Updated information on a proposed solution to this issue will be posted on the CDISC QRS webpage (https://www.cdisc.org/standards/foundational/qrs).
9. All standard QRS supplement development is coordinated with the CDISC SDS QRS Subteam as the governing body. The process involves drafting the controlled terminology and defining instrument-specific standardized values for qualifier, timing, and result variables to populate the SDTMIG FT, QS, and RS domains. These supplements are developed based on user demand and therapeutic area standards development needs. Sponsors should always consult the CDISC website to review the terminology and supplements prior to modeling any QRS instrument.
    a. Sponsors may participate and/or request the development of additional QRS supplements and terminology through the CDISC SDS QRS subteam and the Controlled Terminology QRS subteam.
        i. Once generated, the QRS supplement is posted on the CDISC website (https://www.cdisc.org/standards/foundational/qrs).
        ii. Sponsors should always consult the published QRS supplements for guidance on submitting derived information in SDTMIG-based domains.
10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STRNC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.

##### FT – Examples
CDISC publishes supplements for individual functional tests (at https://www.cdisc.org/standards/foundational/qrs Additional FT examples can be found in supplements on that webpage.

**Example 1**
6-Minute Walk Test (SIX MINUTE WALK) The example represents the distance (in meters) that were walked at each minute of the 6-Minute Walk Test. The assistive device the subject used during the test is represented in the SUPPFT dataset.

*ft.xpt*

| Row | STUDYID | DOMAIN | USUBJID | FTSEQ | FTGRPID | FTTESTCD | FTTEST | FTCAT | FTORRES | FTORRESU | FTSTRESC | FTSTRESN | FTSTRESU | FTBLFL | VISITNUM | FTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | STUDYX | FT | MS01-01 | 1 | 1 | SIXMW101 | SIXMW1- Distance at 1 Minute | SIX MINUTE WALK | 101 | m | 101 | 101 | m | Y | 1 | 2014-03-10 |
| 2 | STUDYX | FT | MS01-01 | 2 | 1 | SIXMW102 | SIXMW1- Distance at 2 Minutes | SIX MINUTE WALK | 201 | m | 201 | 201 | m | Y | 1 | 2014-03-10 |
| 3 | STUDYX | FT | MS01-01 | 3 | 1 | SIXMW103 | SIXMW1- Distance at 3 Minutes | SIX MINUTE WALK | 299 | m | 299 | 299 | m | Y | 1 | 2014-03-10 |
| 4 | STUDYX | FT | MS01-01 | 4 | 1 | SIXMW104 | SIXMW1- Distance at 4 Minutes | SIX MINUTE WALK | 396 | m | 396 | 396 | m | Y | 1 | 2014-03-10 |
| 5 | STUDYX | FT | MS01-01 | 5 | 1 | SIXMW105 | SIXMW1- Distance at 5 Minutes | SIX MINUTE WALK | 493 | m | 493 | 493 | m | Y | 1 | 2014-03-10 |
| 6 | STUDYX | FT | MS01-01 | 6 | 1 | SIXMW106 | SIXMW1- Distance at 6 Minutes | SIX MINUTE WALK | 597 | m | 597 | 597 | m | Y | 1 | 2014-03-10 |

The suppft.xpt dataset represents that the subject used a cane while performing the 6 Minute Walk Test. In this example, FTGRPID is used to link this SUPPFT record to the 6 result records in FT. FTGRPID groups the FT records together by FTCAT and VISITNUM for an USUBJID.

*suppft.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | STUDYX | FT | MS01-01 | FTGRPID | 1 | FTASSTDV | Assistance Device | CANE | CRF | INVESTIGATOR |

#### 6.3.9.2 Questionnaires (QS)

##### QS – Description/Overview
A findings domain that contains data for named, stand-alone instruments designed to provide an assessment of a concept. Questionnaires have a defined standard structure, format, and content; consist of conceptually related items that are typically scored; and have documented methods for administration and analysis.

##### QS – Specification
qs.xpt, Questionnaires — Findings. One record per questionnaire per question per time point per visit per subject, Tabulation.

**Structure:** One record per questionnaire per question per time point per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | QS |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | QSSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | QSGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | QSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 7 | QSTESTCD | Question Short Name | Char | Topic | Req | * |
| 8 | QSTEST | Question Name | Char | Synonym Qualifier | Req | * |
| 9 | QSCAT | Category of Question | Char | Grouping Qualifier | Req | (QSCAT) |
| 10 | QSSCAT | Subcategory for Question | Char | Grouping Qualifier | Perm | * |
| 11 | QSORRES | Finding in Original Units | Char | Result Qualifier | Exp |  |
| 12 | QSORRESU | Original Units | Char | Variable Qualifier | Perm | (UNIT) |
| 13 | QSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 14 | QSSTRESN | Numeric Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 15 | QSSTRESU | Standard Units | Char | Variable Qualifier | Perm | (UNIT) |
| 16 | QSSTAT | Completion Status | Char | Record Qualifier | Perm | (ND) |
| 17 | QSREASND | Reason Not Performed | Char | Record Qualifier | Perm |  |
| 18 | QSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | (QRSMTHOD) |
| 19 | QSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | (NY) |
| 20 | QSBLFL | Baseline Flag | Char | Record Qualifier | Perm | (NY) |
| 21 | QSDRVFL | Derived Flag | Char | Record Qualifier | Perm | (NY) |
| 22 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 23 | VISIT | Visit Name | Char | Timing | Perm |  |
| 24 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 25 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 26 | EPOCH | Epoch | Char | Timing | Perm | (EPOCH) |
| 27 | QSDTC | Date/Time of Finding | Char | Timing | Exp | ISO 8601 datetime or interval |
| 28 | QSDY | Study Day of Finding | Num | Timing | Perm |  |
| 29 | QSTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 30 | QSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 31 | QSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 32 | QSTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 33 | QSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| 34 | QSEVLINT | Evaluation Interval | Char | Timing | Perm | ISO 8601 duration or interval |
| 35 | QSEVINTX | Evaluation Interval Text | Char | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **QSSEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **QSGRPID**: Used to tie together a block of related records in a single domain for a subject.
- **QSSPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Question number on a questionnaire.
- **QSTESTCD**: Topic variable for QS. Short name for the value in QSTEST, which can be used as a column name when converting the dataset from a vertical format to a horizontal format. The value in QSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). QSTESTCD cannot contain characters other than letters, numbers, or underscores. Controlled terminology for QSTESTCD is published in separate codelists for each questionnaire. See https://www.cdisc.org/standards/semantics/terminology for values for QSTESTCD. Examples: "ADCCMD01", "BPR0103".
- **QSTEST**: Verbatim name of the question or group of questions used to obtain the measurement or finding. The value in QSTEST cannot be longer than 40 characters. Controlled terminology for QSTEST is published in separate codelists for each questionnaire. See https://www.cdisc.org/standards/semantics/terminology for values for QSTEST. Example: "BPR01 - Emotional Withdrawal".
- **QSCAT**: Used to specify the questionnaire in which the question identified by QSTEST and QSTESTCD was included. Examples: "ADAS-COG", "MDS-UPDRS".
- **QSSCAT**: A further categorization of the questions within the category. Examples: "MENTAL HEALTH", "DEPRESSION", "WORD RECALL".
- **QSORRES**: Finding as originally received or collected (e.g., "RARELY", "SOMETIMES"). When sponsors apply codelist to indicate that code values are statistically meaningful standardized scores (which are defined by sponsors or by valid methodologies, e.g., SF36 questionnaires), QSORRES will contain the decode format; QSSTRESC and QSSTRESN may contain the standardized code values or scores.
- **QSORRESU**: Original units in which the data were collected. The unit for QSORRES, such as minutes or seconds or the units associated with a visual analog scale.
- **QSSTRESC**: Contains the finding for all questions or subscores copied or derived from QSORRES, in a standard format or standard units. QSSTRESC should store all findings in character format; if findings are numeric, they should also be stored in numeric format in QSSTRESN. If question scores are derived from the original finding, then the standard format is the score. Examples: "0", "1". When sponsors apply codelist to indicate the code values are statistically meaningful standardized scores (which are defined by sponsors or by valid methodologies, e.g., SF36 questionnaires), QSORRES will contain the decode format; QSSTRESC and QSSTRESN may contain the standardized code values or scores.
- **QSSTRESN**: Used for continuous or numeric findings in standard format; copied in numeric format from QSSTRESC. QSSTRESN should store all numeric results or findings.
- **QSSTRESU**: Standardized unit used for QSSTRESC or QSSTRESN.
- **QSSTAT**: Used to indicate that a question was not done or was not answered. Should be null if a result exists in QSORRES.
- **QSREASND**: Describes why a question was not answered. Used in conjunction with QSSTAT when value is "NOT DONE". Example: "SUBJECT REFUSED".
- **QSMETHOD**: Method of the test or examination.
- **QSLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.
- **QSBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that QSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **QSDRVFL**: Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records or questionnaire subscores that do not come from the CRF are examples of records that would be derived for the submission datasets. If QSDRVFL = "Y", then QSORRES may be null with QSSTRESC and (if numeric) QSSTRESN having the derived value.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the observation date/time of the physical exam finding.
- **QSDTC**: Date of questionnaire.
- **QSDY**: Study day of finding collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
- **QSTPT**: Text description of time when questionnaire should be administered. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See QSTPTNUM and QSTPTREF.
- **QSTPTNUM**: Numerical version of QSTPT to aid in sorting.
- **QSELTM**: Planned elapsed time (in ISO 8601) relative to a planned fixed reference (QSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by QSTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by QSTPTREF.
- **QSTPTREF**: Name of the fixed reference point referred to by QSELTM, QSTPTNUM, and QSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **QSRFTDTC**: Date/time of the reference time point, QSTPTREF.
- **QSEVLINT**: Evaluation interval associated with a QSTEST question represented in ISO 8601 character format. Example: "-P2Y" to represent an interval of 2 years in the question "Have you experienced any episodes in the past 2 years?".
- **QSEVINTX**: Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS".


##### QS – Assumptions
There are no additional QS-specific assumptions; all are included in the QRS Shared Assumptions.

**QRS Shared Assumptions**

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

3. There are cases where QRS CRFs do not include numeric "standardized responses" assigned to text responses (e.g., mild, moderate, severe being 1, 2, 3). It is clearly in everyone's best interest to include the numeric "standardized responses" in the SDTMIG QRS dataset. This is only done when the numeric "standardized responses" are documented in the QRS CRF instructions, a user manual, a website specific to the QRS instrument, or another reference document that provides a clear explanation and rationale for providing them in the SDTMIG QRS dataset.

4. Sponsors should always consult published QRS supplements for guidance on submitting derived information in a SDTMIG QRS domain. Derived variable results in QRS are usually considered captured data. If sponsors operationally derive variable results, then the derived records that are submitted in a QRS domain should be flagged by --DRVFL.

    a. The following rules apply for "total"-type scores in QRS datasets.

        i. QRS subtotal, total, etc. scores listed on the CRF are considered captured data and are included in the instrument's controlled terminology.

        ii. QRS subtotal, total, etc. scores not listed on the CRF but documented in an associated instrument manual or reference paper are considered captured data and are included in the instrument's controlled terminology.

        iii. QRS subtotal, total, etc. scores not listed on the CRF, but known to be included in eData by sponsors are considered as captured data, are included in the instrument's controlled terminology. The QRS instrument's CT is considered extensible for this case and the subtotal or total score should be requested to be added.

            1. Any imputations/calculations done to numeric "standardized responses" to produce the total score via transforming numeric "standardized responses" in any way would be done as ADaM derivations.

    b. The QRS instrument subtotal or total score, which is the sum of the numeric responses for an instrument, is populated in --ORRES, --STRESC, and --STRESN. It is considered a captured subtotal or total score without any knowledge of the sponsor-data management processes related to the score.

        i. If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their eCRF process to derive subtotal and total scores. An investigator-derived score written on a CRF will be considered a captured score and not flagged. When subtotal and total scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y". However, when the subtotal and total scores are received from a central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).

5. The variable --REPNUM variable is populated when there are multiple repeats of the same question. When records are related to the first trial of the question, the variable --REPNUM should be set to "1". When records are related to the second trial of the same question, --REPNUM should be set to "2", and so forth.

6. The actual version number of an instrument is represented in the --CAT value as designated by the QRS Terminology Team. If it is determined that this is not the case for an instrument:

    a. Notify the QRS Terminology Team that the instrument has a specific or multiple version numbers. This team will assist in providing an resolution on how the situation will be handled.

    b. Consider the use of the --GRPID variable to indicate the instrument's version number prior to a decision by the QRS Terminology Team.

    c. The sponsor is expected to provide information about the version used for each QRS instrument in the metadata (using the Comments column in the Define-XML document). This could be provided as value-level metadata for --CAT.

    d. The sponsor is expected to provide information about the scoring rules in the metadata.

7. If the variable --TEST is represented with verbatim text >40 characters, represent the abbreviated meaningful text in --TEST within 40 characters and describe the full text of the item in the study metadata. If the verbatim item response (e.g., --QSORRES) is >200 characters, represent the abbreviated meaningful text in QSORRES within the 200 characters and describe the full text in the study metadata; see Section 4 of the QRS supplement. See Section 4.5.3, Text Strings that Exceed the Maximum Length for General Observation-class Domain Variables, for further information.

    a. The instrument's annotated CRF can also be used as a reference for the full text in both of these situations.

8. --EVAL and --EVALID must not be used to model QRS data in SDTM. These variables have had various interpretations on QRS CRFs and were used to represent a multitude of evaluator information about QRS instruments. This has made it more difficult for users of SDTM QRS data to interpret this data and more difficult to pool data for analyses. If needed, supplemental qualifiers may be used to represent this data. Updated information on a proposed solution to this issue will be posted on the CDISC QRS webpage (https://www.cdisc.org/standards/foundational/qrs).

9. All standard QRS supplement development is coordinated with the CDISC SDS QRS Subteam as the governing body. The process involves drafting the controlled terminology and defining instrument-specific standardized values for qualifier, timing, and result variables to populate the SDTMIG FT, QS, and RS domains. These supplements are developed based on user demand and therapeutic area standards development needs. Sponsors should always consult the CDISC website to review the terminology and supplements prior to modeling any QRS instrument.

    a. Sponsors may participate and/or request the development of additional QRS supplements and terminology through the CDISC SDS QRS subteam and the Controlled Terminology QRS subteam.

        i. Once generated, the QRS supplement is posted on the CDISC website (https://www.cdisc.org/standards/foundational/qrs).

        ii. Sponsors should always consult the published QRS supplements for guidance on submitting derived information in SDTMIG-based domains.

10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STRNC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.

##### QS – Examples
CDISC publishes supplements for individual questionnaires (at https://www.cdisc.org/standards/foundational/qrs). Additional QS examples can be found in supplements on that webpage.

**Example 1**
Satisfaction With Life Scale (SWLS). The example represents the items from the SWLS instrument.

*qs.xpt*

| Row | STUDYID | DOMAIN | USUBJID | QSSEQ | QSTESTCD | QSTEST | QSCAT | QSORRES | QSSTRESC | QSSTRESN | QSLOBXFL | VISITNUM | QSDTC | QSDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CDISC01 | QS | CDISC01.100008 | 1 | SWLS0101 | SWLS01-My Life is Close to Ideal | SWLS | Slightly agree | 5 | 5 | Y | 1 | 2003-04-15 | 1 |
| 2 | CDISC01 | QS | CDISC01.100008 | 2 | SWLS0102 | SWLS01-My Life Conditions are Excellent | SWLS | Neither agree nor disagree | 4 | 4 | Y | 1 | 2003-04-15 | 1 |
| 3 | CDISC01 | QS | CDISC01.100008 | 3 | SWLS0103 | SWLS01-I Am Satisfied with My Life | SWLS | Agree | 6 | 6 | Y | 1 | 2003-04-15 | 1 |
| 4 | CDISC01 | QS | CDISC01.100008 | 4 | SWLS0104 | SWLS01-Have Gotten Important Things | SWLS | Disagree | 2 | 2 | Y | 1 | 2003-04-15 | 1 |
| 5 | CDISC01 | QS | CDISC01.100008 | 5 | SWLS0105 | SWLS01-Live Life Over Change Nothing | SWLS | Strongly disagree | 1 | 1 | Y | 1 | 2003-04-15 | 1 |
| 6 | CDISC01 | QS | CDISC01.100014 | 6 | SWLS0101 | SWLS01-My Life is Close to Ideal | SWLS | Slightly agree | 5 | 5 | Y | 1 | 2003-04-15 | 1 |
| 7 | CDISC01 | QS | CDISC01.100014 | 7 | SWLS0102 | SWLS01-My Life Conditions are Excellent | SWLS | Neither agree nor disagree | 4 | 4 | Y | 1 | 2003-04-15 | 1 |
| 8 | CDISC01 | QS | CDISC01.100014 | 8 | SWLS0103 | SWLS01-I Am Satisfied with My Life | SWLS | Agree | 6 | 6 | Y | 1 | 2003-04-15 | 1 |
| 9 | CDISC01 | QS | CDISC01.100014 | 9 | SWLS0104 | SWLS01-Have Gotten Important Things | SWLS | Disagree | 2 | 2 | Y | 1 | 2003-04-15 | 1 |
| 10 | CDISC01 | QS | CDISC01.100014 | 10 | SWLS0105 | SWLS01-Live Life Over Change Nothing | SWLS | Strongly disagree | 1 | 1 | Y | 1 | 2003-04-15 | 1 |
#### 6.3.9.3 Disease Response and Clin Classification (RS)

##### RS – Description/Overview

A findings domain for the assessment of disease response to therapy, or clinical classification based on published criteria.
Data in this domain may or may not be collected by means of a standard CRF.
- Clinical classification instruments usually have a standard CRF for data capture, but also may instead be based on an evaluator providing response evaluations based on published criteria.
- Oncology response criteria are evaluated based on published criteria.
- Additional disease classifications or scoring systems (e.g., staging criteria) are based on published criteria.
- There are separate supplements prepared for clinical classification instruments and therapeutic-area disease response criteria use cases.

##### RS – Specification

rs.xpt, Disease Response and Clin Classification — Findings. One record per response assessment or clinical classification assessment per time point per visit per subject per assessor per medical evaluator, Tabulation.

**Structure:** One record per response assessment or clinical classification assessment per time point per visit per subject per assessor per medical evaluator
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | RS |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | RSSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | RSGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | RSREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | RSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | RSLNKID | Link ID | Char | Identifier | Perm |  |
| 9 | RSLNKGRP | Link Group ID | Char | Identifier | Perm |  |
| 10 | RSTESTCD | Assessment Short Name | Char | Topic | Req | C96782 |
| 11 | RSTEST | Assessment Name | Char | Synonym Qualifier | Req | C96781 |
| 12 | RSCAT | Category for Assessment | Char | Grouping Qualifier | Exp | C124298; C118971 |
| 13 | RSSCAT | Subcategory | Char | Grouping Qualifier | Perm |  |
| 14 | RSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 15 | RSORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 16 | RSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C96785 |
| 17 | RSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 18 | RSSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 19 | RSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 20 | RSREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 21 | RSNAM | Vendor Name | Char | Record Qualifier | Perm |  |
| 22 | RSMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C158113 |
| 23 | RSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| 24 | RSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 25 | RSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 26 | RSEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 27 | RSEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| 28 | RSACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |
| 29 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 30 | VISIT | Visit Name | Char | Timing | Perm |  |
| 31 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 32 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 33 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 34 | RSDTC | Date/Time of Assessment | Char | Timing | Exp | ISO 8601 datetime or interval |
| 35 | RSDY | Study Day of Assessment | Num | Timing | Perm |  |
| 36 | RSTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 37 | RSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 38 | RSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 39 | RSTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 40 | RSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |
| 41 | RSEVLINT | Evaluation Interval | Char | Timing | Perm | ISO 8601 duration or interval |
| 42 | RSEVINTX | Evaluation Interval Text | Char | Timing | Perm |  |
| 43 | RSSTRTPT | Start Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| 44 | RSSTTPT | Start Reference Time Point | Char | Timing | Perm |  |
| 45 | RSENRTPT | End Relative to Reference Time Point | Char | Timing | Perm | C66728 |
| 46 | RSENTPT | End Reference Time Point | Char | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **RSSEQ**: Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number.
- **RSGRPID**: Used to link together a block of related records within a subject in a domain.
- **RSREFID**: Internal or external identifier.
- **RSSPID**: Sponsor-defined identifier.
- **RSLNKID**: An identifier used to link the response assessment to the related measurement record in another domain which was used to determine the response result. LNKID values group records within USUBJID.
- **RSLNKGRP**: A grouping identifier used to link the response assessment to a group of measurement/assessment records which were used in the assessment of the response. LNKGRP values group records within USUBJID.
- **RSTESTCD**: Short name of the TEST in RSTEST. The value in RSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). RSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TRGRESP", "NTRGRESP", "OVRLRESP", "SYMPTDTR", "CPS0102".; There are separate codelists used for RSTESTCD where the choice depends on the value of RSCAT. Codelist "ONCRTSCD" is used for oncology response criteria (when RSCAT is a term in codelist "ONCRSCAT"). Examples: TRGRESP, "NTRGRESP, "OVRLRESP". For Clinical Classifications (when RSCAT is a term in codelist "CCCAT"), QRS Naming Rules apply. These instruments have individual dedicated terminology codelists.
- **RSTEST**: Verbatim name of the response assessment. The value in RSTEST cannot be longer than 40 characters.; There are separate codelists used for RSTEST where the choice depends on the value of RSCAT. Codelist "ONCRTS" is used for oncology response criteria (when RSCAT is a term in codelist "ONCRSCAT"). Examples: "Target Response", "Non-target Response", "Overall Response", "Symptomatic Deterioration". For Clinical Classifications (when RSCAT is a term in codelist "CCCAT"), QRS Naming Rules apply. These instruments have individual dedicated terminology codelists.
- **RSCAT**: Used to define a category of related records across subjects. Examples: "RECIST 1.1", "CHILD-PUGH CLASSIFICATION". There are separate codelists used for RSCAT where the choice depends on whether the related records are about an oncology response criterion or another clinical classification.; RSCAT is required for clinical classifications other than oncology response criteria.
- **RSSCAT**: Used to define a further categorization of RSCAT values.
- **RSORRES**: Result of the response assessment as originally received, collected, or calculated.
- **RSORRESU**: Unit for RSORRES.
- **RSSTRESC**: Contains the result value for the response assessment, copied, or derived from RSORRES in a standard format or standard units. RSSTRESC should store all results or findings in character format.; For Clinical Classifications, this may be a score.
- **RSSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from --STRESC. --STRESN should store all numeric test results or findings. For Clinical Classifications, this may be a score.
- **RSSTRESU**: Standardized units used for RSSTRESC and RSSTRESN.
- **RSSTAT**: Used to indicate the response assessment was not performed. Should be null if a result exists in RSORRES.
- **RSREASND**: Describes why a response assessment was not performed. Examples: "All target tumors not evaluated", "Subject does not have non-target tumors". Used in conjunction with RSSTAT when value is "NOT DONE".
- **RSNAM**: The name or identifier of the vendor that performed the response assessment. This column can be left null when the investigator provides the complete set of data in the domain.
- **RSMETHOD**: Method of the test or examination.
- **RSLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.; When a clinical classification is assessed at multiple times, including baseline, RSLOBXFL should be included in the dataset.
- **RSBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that --BLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **RSDRVFL**: Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.
- **RSEVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".; RSEVAL is expected for oncology response criteria. It can be left null when the investigator provides the complete set of data in the domain. However, the column should contain no null values when data from one or more independent assessors is included, meaning that the rows attributed to the investigator should contain a value of "INVESTIGATOR".
- **RSEVALID**: Used to distinguish multiple evaluators with the same role recorded in RSEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumptions in Section 6.3.9.3.1, Disease Response Use Case.
- **RSACPTFL**: In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provides an evaluation of response, this flag identifies the record that is considered to be the accepted evaluation.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the date/time at which the assessment was made.
- **RSDTC**: Collection date and time of the assessment represented in ISO 8601 character format.
- **RSDY**: Study day of the assessment, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
- **RSTPT**: Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See RSTPTNUM and RSTPTREF.
- **RSTPTNUM**: Numeric version of planned time point used in sorting.
- **RSELTM**: Planned elapsed time in ISO 8601 character format relative to a planned fixed reference (RSTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.
- **RSTPTREF**: Description of the fixed reference point referred to by RSELTM, RSTPTNUM, and RSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **RSRFTDTC**: Date/time for a fixed reference time point defined by RSTPTREF in ISO 8601 character format.
- **RSEVLINT**: Duration of interval associated with an observation such as a finding RSTESTCD, represented in ISO 8601 character format. Example: "-P2M" to represent a period of the past 2 months as the evaluation interval.
- **RSEVINTX**: Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS".
- **RSSTRTPT**: Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable RSSTTPT.. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.
- **RSSTTPT**: Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by RSSTRTPT. Examples: "2003-12-15", "VISIT 1".
- **RSENRTPT**: Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable RSENTPT.. Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.
- **RSENTPT**: Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by RSENRTPT. Examples: "2003-12-25", "VISIT 2".

Assumptions and examples are different for the disease response and clinical classifications use cases.
##### 6.3.9.3.1 Disease Response Use Case

**RS -- Disease Response Use Case Assumptions**

Assumptions here discuss the oncology use case, which is the only disease-response use case that currently exists.

1. RSCAT is used to group a set of assessments based on a disease response criterion (published or protocol-defined). One of the codelists for RSCAT is ONCRSCAT. The ONCRSCAT codelist contains controlled terminology for oncology disease response assessments.
2. Oncology response criteria assess the change in tumor burden, an important feature of the clinical evaluation of cancer therapeutics: Both tumor shrinkage (objective response) and disease progression are useful endpoints in cancer clinical trials. The RS domain is applicable for representing responses to assessment criteria such as RECIST[1] or Lugano classification.[2] The SDTM domain examples provided reference RECIST. Disease Response supplements will be developed as 1 supplement per response criterion and will contained criterion-specific guidance and examples.
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
| --- | --- | --- | --- | --- |
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

##### RS -- Examples - Disease Response

The following are examples for oncology response criteria.

**Example 1**

This example shows response assessments determined from the TR domain based on RECIST 1.1 criteria and also shows a case where progressive disease due to symptomatic deterioration was determined based on a clinical assessment by the investigator.

**Rows 1-3:** Show the target response, non-target response, and the overall response by the investigator using RECIST 1.1 at the week 6 visit.

**Rows 4-7:** Show the target response and non-target response by the investigator using RECIST 1.1, as well as the determination of symptomatic determination (pleural effusion) and overall response using protocol-defined response criteria, at the week 12 visit.

*rs.xpt*

| Row | STUDYID | DOMAIN | USUBJID | RSSEQ | RSLNKGRP | RSTESTCD | RSTEST | RSCAT | RSORRES | RSSTRESC | RSEVAL | VISITNUM | VISIT | RSDTC | RSDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | RS | 44444 | 1 |  | TRGRESP | Target Response | RECIST 1.1 | PR | PR | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 2 | ABC | RS | 44444 | 2 |  | NTRGRESP | Non-target Response | RECIST 1.1 | SD | SD | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 3 | ABC | RS | 44444 | 3 | A2 | OVRLRESP | Overall Response | RECIST 1.1 | PR | PR | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 4 | ABC | RS | 44444 | 4 |  | TRGRESP | Target Response | RECIST 1.1 | NE | NE | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 5 | ABC | RS | 44444 | 5 |  | NTRGRESP | Non-target Response | RECIST 1.1 | NE | NE | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 6 | ABC | RS | 44444 | 6 |  | SYMPTDTR | Symptomatic Deterioration | PROTOCOL DEFINED RESPONSE CRITERIA | Pleural Effusion | PD | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 7 | ABC | RS | 44444 | 7 | A3 | OVRLRESP | Overall Response | PROTOCOL DEFINED RESPONSE CRITERIA | PD | PD | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |

**Example 2**

This example shows response assessments determined from the TR domain based on RECIST 1.1 criteria and also shows a confirmation of an equivocal new lesion progression.

**Rows 1-4:** Show the target response, non-target response, and the overall response by the independent assessor Radiologist 1 using RECIST 1.1 at the week 6 visit. At this week 6 visit, an equivocal new lesion was identified.

**Rows 5-8:** Show the target response, non-target response, and the overall response by the independent assessor Radiologist 1 using RECIST 1.1 at the week 12 visit. At this week 12 visit, the new lesion was determined to be unequivocally a new lesion.

*rs.xpt*

| Row | STUDYID | DOMAIN | USUBJID | RSSEQ | RSLNKGRP | RSTESTCD | RSTEST | RSCAT | RSORRES | RSSTRESC | RSNAM | RSEVAL | RSEVALID | RSACPTFL | VISITNUM | VISIT | RSDTC | RSDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | RS | 55555 | 1 |  | TRGRESP | Target Response | RECIST 1.1 | PR | PR | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 40 | WEEK 6 | 2010-02-18 | 46 |
| 2 | ABC | RS | 55555 | 2 |  | NTRGRESP | Non-target Response | RECIST 1.1 | CR | CR | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 40 | WEEK 6 | 2010-02-18 | 46 |
| 3 | ABC | RS | 55555 | 3 |  | NEWLPROG | New Lesion Progression | RECIST 1.1 | EQUIVOCAL | EQUIVOCAL | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 40 | WEEK 6 | 2010-04-02 |  |
| 4 | ABC | RS | 55555 | 4 | A2 | OVRLRESP | Overall Response | RECIST 1.1 | PR | PR | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 40 | WEEK 6 | 2010-04-02 |  |
| 5 | ABC | RS | 55555 | 5 |  | TRGRESP | Target Response | RECIST 1.1 | PD | PD | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 60 | WEEK 12 |  |  |
| 6 | ABC | RS | 55555 | 6 |  | NTRGRESP | Non-target Response | RECIST 1.1 | CR | CR | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 60 | WEEK 12 |  |  |
| 7 | ABC | RS | 55555 | 7 |  | NEWLPROG | New Lesion Progression | RECIST 1.1 | UNEQUIVOCAL | UNEQUIVOCAL | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 60 | WEEK 12 |  |  |
| 8 | ABC | RS | 55555 | 8 | A3 | OVRLRESP | Overall Response | RECIST 1.1 | PD | PD | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 60 | WEEK 12 |  |  |

**Example 3**

This example shows best response and the overall response of progression to prior therapies and follow-up therapies.

**Row 1:** Shows disease progression on or after a prior chemotherapy regimen. The date of progression is represented in RSDTC. RSENTPT and RSENRTPT represent that the disease progression was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the disease progression was unknown or not collected. RSLNKGRP = "CM1" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM1".

**Row 2:** Shows best response to prior chemotherapy regimen. The date of best response is represented in RSDTC. RSENTPT and RSENRTPT represent that the best response was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the best response was unknown or not collected. RSLNKGRP = "CM2" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM2".

**Row 3:** Shows best response to prior radiotherapy. The date of best response is represented in RSDTC. RSENTPT and RSENRTPT represent that the best response was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the best response was unknown or not collected. RSLNKGRP = "PR2" is used to link this record in RS to the prior radiotherapy in PR where the PRLNKGRP = "PR2".

**Rows 4-5:** Show best response and progression to a follow-up anti-cancer therapy. The date of best response and date of progression are represented in RSDTC. RSSTTPT and RSSTRTPT represent that the best response and progression were after study treatment discontinuation. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the best response and progression was unknown or not collected. RSLNKGRP = "CM3" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM3".

*rs.xpt*

| Row | STUDYID | DOMAIN | USUBJID | RSSEQ | RSLNKGRP | RSTESTCD | RSTEST | RSCAT | RSORRES | RSORRESU | RSSTRESC | RSSTRESN | RSSTRESU | RSEVAL | VISITNUM | VISIT | RSDTC | RSDY | RSSTRTPT | RSSTTPT | RSENRTPT | RSENTPT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | RS | 55555 | 1 | CM1 | OVRLRESP | Overall Response | UNSPECIFIED | PD |  | PD |  |  | INVESTIGATOR | 10 | SCREEN | 2010-02-18 | -32 |  |  | BEFORE | SCREEN |
| 2 | ABC | RS | 66666 | 2 | CM2 | BESTRESP | Best Response | UNSPECIFIED | SD |  | SD |  |  | INVESTIGATOR | 10 | SCREEN |  |  |  |  | BEFORE | SCREEN |
| 3 | ABC | RS | 66666 | 3 | PR2 | BESTRESP | Best Response | UNSPECIFIED | MINIMAL RESPONSE |  | MINIMAL RESPONSE |  |  | INVESTIGATOR | 10 | SCREEN |  |  |  |  | BEFORE | SCREEN |
| 4 | ABC | RS | 77777 | 4 | CM3 | BESTRESP | Best Response | UNSPECIFIED | SD |  | SD |  |  | INVESTIGATOR | 240 | FOLLOW-UP MONTH 4 | 2010-04-02 | 520 | AFTER | STUDY TREATMENT DISCONTINUATION |  |  |
| 5 | ABC | RS | 77777 | 5 | CM3 | OVRLRESP | Overall Response | UNSPECIFIED | PD |  | PD |  |  | INVESTIGATOR | 260 | FOLLOW-UP MONTH 6 | 2010-06-01 | 581 | AFTER | STUDY TREATMENT DISCONTINUATION |  |  |

**References**

1. Eisenhauer EA, Therasse P, Bogaerts J, et al. New response evaluation criteria in solid tumours: revised RECIST guideline (version 1.1). Eur J Cancer. 2009;45(2):228-247. doi:10.1016/j.ejca.2008.10.026
2. Cheson BD, Fisher RI, Barrington SF, et al. Recommendations for initial evaluation, staging, and response assessment of Hodgkin and non-Hodgkin lymphoma: the Lugano classification. J Clin Oncol. 2014;32(27):3059-3068. doi:10.1200/JCO.2013.54.8800
##### 6.3.9.3.2 Clinical Classifications Use Case

**RS -- Clinical Classifications Use Case Assumptions**

The following assumptions are unique to the RS domain clinical classifications use case:

1. Clinical classifications are named instruments whose output is an ordinal or categorical score that serves as a surrogate for or ranking of disease status or other physiological or biological status.
   a. Clinical classifications may be based solely on objective data from clinical records, or they may involve a clinical judgment or interpretation of directly observable signs, behaviors, or other physical manifestations related to a condition or subject status. These physical manifestations may be findings (e.g., lab results, vital signs, clinical events) that are typically represented in other SDTM domains .
2. RSCAT is used to group a set of assessments based on a clinical classification. One of the codelists for RSCAT is CCCAT. The CCCAT codelist contains CDISC Controlled Terminology for clinical classifications instruments.
3. When using the RS domain to represent a clinical classification instrument that incorporates data from other domains:
   a. Whenever possible, all source data must be represented in the topic-based domain(s) to which they pertain. For example, if a lab test value is collected and then scored for a response evaluation or clinical classification instrument, the lab test value must be recorded in the LB domain using the rules that apply to that domain and the tests being represented.
   b. If the source value is directly collected on the clinical classification instrument, then the values from the source record may be transcribed to the corresponding RS record, with RSORRES and RSORRESU populated to agree with the units shown on the clinical classification instrument, which may be different from the sponsor's usual practice for original and standard units.
   c. If a clinical classification uses a a source value by comparing it to a range (e.g., "2-5", ">3"), then the source value will exist only in the source domain; the range is represented in the corresponding RS record in RSORRES and RSORRESU.
   d. In all cases, RSSTRESC/RSSTRESN should be populated with the assigned ordinal score as indicated on the instrument.

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
3. There are cases where QRS CRFs do not include numeric "standardized responses" assigned to text responses (e.g., mild, moderate, severe being 1, 2, 3). It is clearly in everyone's best interest to include the numeric "standardized responses" in the SDTMIG QRS dataset. This is only done when the numeric "standardized responses" are documented in the QRS CRF instructions, a user manual, a website specific to the QRS instrument, or another reference document that provides a clear explanation and rationale for providing them in the SDTMIG QRS dataset.
4. Sponsors should always consult published QRS supplements for guidance on submitting derived information in a SDTMIG QRS domain. Derived variable results in QRS are usually considered captured data. If sponsors operationally derive variable results, then the derived records that are submitted in a QRS domain should be flagged by --DRVFL.
   a. The following rules apply for "total"-type scores in QRS datasets.
      i. QRS subtotal, total, etc. scores listed on the CRF are considered captured data and are included in the instrument's controlled terminology.
      ii. QRS subtotal, total, etc. scores not listed on the CRF but documented in an associated instrument manual or reference paper are considered captured data and are included in the instrument's controlled terminology.
      iii. QRS subtotal, total, etc. scores not listed on the CRF, but known to be included in eData by sponsors are considered as captured data, are included in the instrument's controlled terminology. The QRS instrument's CT is considered extensible for this case and the subtotal or total score should be requested to be added.
         1. Any imputations/calculations done to numeric "standardized responses" to produce the total score via transforming numeric "standardized responses" in any way would be done as ADaM derivations.
   b. The QRS instrument subtotal or total score, which is the sum of the numeric responses for an instrument, is populated in --ORRES, --STRESC, and --STRESN. It is considered a captured subtotal or total score without any knowledge of the sponsor-data management processes related to the score.
      i. If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their eCRF process to derive subtotal and total scores. An investigator-derived score written on a CRF will be considered a captured score and not flagged. When subtotal and total scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y". However, when the subtotal and total scores are received from a central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).
5. The variable --REPNUM variable is populated when there are multiple repeats of the same question. When records are related to the first trial of the question, the variable --REPNUM should be set to "1". When records are related to the second trial of the same question, --REPNUM should be set to "2", and so forth.
6. The actual version number of an instrument is represented in the --CAT value as designated by the QRS Terminology Team. If it is determined that this is not the case for an instrument:
   a. Notify the QRS Terminology Team that the instrument has a specific or multiple version numbers. This team will assist in providing an resolution on how the situation will be handled.
   b. Consider the use of the --GRPID variable to indicate the instrument's version number prior to a decision by the QRS Terminology Team.
   c. The sponsor is expected to provide information about the version used for each QRS instrument in the metadata (using the Comments column in the Define-XML document). This could be provided as value-level metadata for --CAT.
   d. The sponsor is expected to provide information about the scoring rules in the metadata.
7. If the variable --TEST is represented with verbatim text >40 characters, represent the abbreviated meaningful text in --TEST within 40 characters and describe the full text of the item in the study metadata. If the verbatim item response (e.g., --QSORRES) is >200 characters, represent the abbreviated meaningful text in QSORRES within the 200 characters and describe the full text in the study metadata; see Section 4 of the QRS supplement. See Section 4.5.3, Text Strings that Exceed the Maximum Length for General Observation-class Domain Variables, for further information.
   a. The instrument's annotated CRF can also be used as a reference for the full text in both of these situations.
8. --EVAL and --EVALID must not be used to model QRS data in SDTM. These variables have had various interpretations on QRS CRFs and were used to represent a multitude of evaluator information about QRS instruments. This has made it more difficult for users of SDTM QRS data to interpret this data and more difficult to pool data for analyses. If needed, supplemental qualifiers may be used to represent this data. Updated information on a proposed solution to this issue will be posted on the CDISC QRS webpage (https://www.cdisc.org/standards/foundational/qrs).
9. All standard QRS supplement development is coordinated with the CDISC SDS QRS Subteam as the governing body. The process involves drafting the controlled terminology and defining instrument-specific standardized values for qualifier, timing, and result variables to populate the SDTMIG FT, QS, and RS domains. These supplements are developed based on user demand and therapeutic area standards development needs. Sponsors should always consult the CDISC website to review the terminology and supplements prior to modeling any QRS instrument.
   a. Sponsors may participate and/or request the development of additional QRS supplements and terminology through the CDISC SDS QRS subteam and the Controlled Terminology QRS subteam.
      i. Once generated, the QRS supplement is posted on the CDISC website (https://www.cdisc.org/standards/foundational/qrs).
      ii. Sponsors should always consult the published QRS supplements for guidance on submitting derived information in SDTMIG-based domains.
10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STRNC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.

##### RS -- Examples - Clinical Classifications

The following example is for a clinical classification. For additional RS examples, see the CDISC-published supplements for individual clinical classifications, at https://www.cdisc.org/standards/foundational/qrs.

**Example 1**

Glasgow Coma Scale NINDS Version (GCS NINDS VERSION)

The rs.xpt dataset represents the items from the GCS NINDS VERSION instrument.

*rs.xpt*

| Row | STUDYID | DOMAIN | USUBJID | RSSEQ | RSTESTCD | RSTEST | RSCAT | RSORRES | RSSTRESC | RSSTRESN | RSLOBXFL | VISITNUM | RSDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | STUDYX | RS | P0001 | 1 | GCS0101 | GCS01-Best Eye Response | GCS NINDS VERSION | No eye opening | 1 | 1 | Y | 1 | 2012-11-16 |
| 2 | STUDYX | RS | P0001 | 2 | GCS0102 | GCS01-Motor Response | GCS NINDS VERSION | Abnormal extension | 2 | 2 | Y | 1 | 2012-11-16 |
| 3 | STUDYX | RS | P0001 | 3 | GCS0103 | GCS01-Verbal Response | GCS NINDS VERSION | Incomprehensible sound | 2 | 2 | Y | 1 | 2012-11-16 |
| 4 | STUDYX | RS | P0001 | 4 | GCS0104 | GCS01-Total Score | GCS NINDS VERSION | 5 | 5 | 5 | Y | 1 | 2012-11-16 |
| 5 | STUDYX | RS | P0001 | 5 | GCS0105A | GCS01-Confounder: GCS Accurate | GCS NINDS VERSION | CHECKED | CHECKED |  | Y | 1 | 2012-11-16 |
| 6 | STUDYX | RS | P0001 | 6 | GCS0105B | GCS01-Confounder: Paralytic | GCS NINDS VERSION | CHECKED | CHECKED |  | Y | 1 | 2012-11-16 |
| 7 | STUDYX | RS | P0001 | 7 | GCS0105C | GCS01-Confounder: Alcohol/Drug of Abuse | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED |  | Y | 1 | 2012-11-16 |
| 8 | STUDYX | RS | P0001 | 8 | GCS0105D | GCS01-Confounder: C-Spine Injury | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED |  | Y | 1 | 2012-11-16 |
| 9 | STUDYX | RS | P0001 | 9 | GCS0105E | GCS01-Confounder: Hypoxia/Hypotension | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED |  | Y | 1 | 2012-11-16 |
| 10 | STUDYX | RS | P0001 | 10 | GCS0105F | GCS01-Confounder: Hypothermia | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED |  | Y | 1 | 2012-11-16 |
| 11 | STUDYX | RS | P0001 | 11 | GCS0105G | GCS01-Confounder: Sedation | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED |  | Y | 1 | 2012-11-16 |
| 12 | STUDYX | RS | P0001 | 12 | GCS0105H | GCS01-Confounder: Unknown | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED |  | Y | 1 | 2012-11-16 |

---
