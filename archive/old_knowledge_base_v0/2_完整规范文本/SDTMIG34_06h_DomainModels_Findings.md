# SDTMIG v3.4 --- Domain Models: Findings — Part 8

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 8/8 — 6.3.10-6.3.13: SC, SS, Tumor/Lesion, VS
> **Original:** `SDTMIG34_06_DomainModels_Findings.md`
> **Related:** `SDTMIG34_06a_DomainModels_Findings.md`, `SDTMIG34_06b_DomainModels_Findings.md`, `SDTMIG34_06c_DomainModels_Findings.md`, `SDTMIG34_06d_DomainModels_Findings.md`, `SDTMIG34_06e_DomainModels_Findings.md`, `SDTMIG34_06f_DomainModels_Findings.md`, `SDTMIG34_06g_DomainModels_Findings.md`

---

### 6.3.10 Subject Characteristics (SC)

#### SC – Description/Overview
A findings domain that contains subject-related data not collected in other domains.

#### SC – Specification
sc.xpt, Subject Characteristics — Findings. One record per characteristic per visit per subject., Tabulation.

**Structure:** One record per characteristic per visit per subject.
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | SC |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | SCSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | SCGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | SCSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 7 | SCTESTCD | Subject Characteristic Short Name | Char | Topic | Req | (SCTESTCD) |
| 8 | SCTEST | Subject Characteristic | Char | Synonym Qualifier | Req | (SCTEST) |
| 9 | SCCAT | Category for Subject Characteristic | Char | Grouping Qualifier | Perm | * |
| 10 | SCSCAT | Subcategory for Subject Characteristic | Char | Grouping Qualifier | Perm | * |
| 11 | SCORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 12 | SCORRESU | Original Units | Char | Variable Qualifier | Perm | (UNIT) |
| 13 | SCSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 14 | SCSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 15 | SCSTRESU | Standard Units | Char | Variable Qualifier | Perm | (UNIT) |
| 16 | SCSTAT | Completion Status | Char | Record Qualifier | Perm | (ND) |
| 17 | SCREASND | Reason Not Performed | Char | Record Qualifier | Perm |  |
| 18 | VISITNUM | Visit Number | Num | Timing | Perm |  |
| 19 | VISIT | Visit Name | Char | Timing | Perm |  |
| 20 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 21 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 22 | EPOCH | Epoch | Char | Timing | Perm | (EPOCH) |
| 23 | SCDTC | Date/Time of Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| 24 | SCDY | Study Day of Examination | Num | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SCSEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **SCGRPID**: Used to tie together a block of related records in a single domain for a subject.
- **SCSPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.
- **SCTESTCD**: Short name of the measurement, test, or examination described in SCTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MARISTAT", "NATORIG".
- **SCTEST**: Verbatim name of the test or examination used to obtain the measurement or finding. The value in SCTEST cannot be longer than 40 characters. Examples: "Marital Status", "National Origin".
- **SCCAT**: Used to define a category of related records.
- **SCSCAT**: A further categorization of the subject characteristic.
- **SCORRES**: Result of the subject characteristic as originally received or collected.
- **SCORRESU**: Original unit in which the data were collected. The unit for SCORRES.
- **SCSTRESC**: Contains the result value for all findings copied or derived from SCORRES, in a standard format or standard units. SCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in SCORRES, and these results effectively have the same meaning, they could be represented in standard format in SCSTRESC as "NEGATIVE".
- **SCSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from SCSTRESC. SCSTRESN should store all numeric test results or findings.
- **SCSTRESU**: Standardized unit used for SCSTRESC or SCSTRESN.
- **SCSTAT**: Used to indicate that the measurement was not done. Should be null if a result exists in SCORRES.
- **SCREASND**: Describes why the observation has no result. Example: "Subject refused". Used in conjunction with SCSTAT when value is "NOT DONE".
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm.
- **EPOCH**: Epoch associated with the start date/time at which the assessment was made.
- **SCDTC**: Collection date and time of the subject characteristic represented in ISO 8601 character format.
- **SCDY**: Study day of collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.


#### SC – Assumptions

1. The structure of subject characteristics is based on the Findings general observation class and is an extension of the demographics data, including socioeconomic or other broad characteristics. The structure for demographic data is fixed and includes date of birth, age, sex, race, ethnicity, and country. Subject characteristics may be collected periodically over time. Some examples of subject characteristics include education level, marital status, and national origin.
2. Associations between some subject characteristic tests and response codelists are described in the SC Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.
3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the SC domain, but the following qualifiers would generally not be used in SC: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --NAM, --LOINC, --SPEC, --SPCCND, --BLFL, --LOBXFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV.

#### SC – Examples

**Example 1**
This example shows data collected once per subject that does not fit into the Demographics (DM) domain. For this example, national origin and marital status were collected.

*sc.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SCSEQ | SCTESTCD | SCTEST | SCORRES | SCSTRESC | SCDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | SC | ABC-001-001 | 1 | NATORIG | National Origin | UNITED STATES | USA | 1999-06-19 |
| 2 | ABC | SC | ABC-001-001 | 2 | MARISTAT | Marital Status | DIVORCED | DIVORCED | 1999-06-19 |
| 3 | ABC | SC | ABC-001-002 | 1 | NATORIG | National Origin | CANADA | CAN | 1999-03-19 |
| 4 | ABC | SC | ABC-001-002 | 2 | MARISTAT | Marital Status | MARRIED | MARRIED | 1999-03-19 |
| 5 | ABC | SC | ABC-001-003 | 1 | NATORIG | National Origin | USA | USA | 1999-05-03 |
| 6 | ABC | SC | ABC-001-003 | 2 | MARISTAT | Marital Status | NEVER MARRIED | NEVER MARRIED | 1999-05-03 |
| 7 | ABC | SC | ABC-001-201 | 1 | NATORIG | National Origin | JAPAN | JPN | 1999-06-14 |
| 8 | ABC | SC | ABC-002-001 | 2 | MARISTAT | Marital Status | WIDOWED | WIDOWED | 1999-06-14 |

**Example 2**
In this example, only infants were study subjects. However, with the possible exception of USUBJID values, the example would be unchanged for a study in which mothers were study subjects. If these data were collected for an infant who was an associated person, they would be represented in the APSC domain and the dataset would include APID, RSUBJID, and SREL, rather than USUBJID.

Although there is a test for gestational age in the CDISC Controlled Terminology for Reproductive Findings, gestational age is an attribute of the fetus or infant, and is not a finding about their reproductive system; in this example, gestational age is represented in the Subject Characteristics (SC) domain. The structure of the SC domain formerly was 1 record per characteristic (test) per subject, but with this version of the SDTMIG the structure has changed to allow multiple records per test. This example shows multiple estimates of gestational age for the same subject. Not all of the values of METHOD shown in this example are currently in the METHOD codelist.

Gestational age is often expressed (and sometimes collected) in weeks and days. SDTM does not support the recording of an individual finding result with mixed units (e.g., "20 weeks and 5 days"), so the gestational age would be converted to days for representation in SDTM.

*sc.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SCSEQ | SCTESTCD | SCTEST | SCCAT | SCORRES | SCORRESU | SCSTRESC | SCSTRESN | SCSTRESU | SCMETHOD | VISITNUM | SCDTC | SCDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC-123 | SC | 101 | 1 | EGESTAGE | Estimated Gestational Age | PREGNANCY-RELATED FINDINGS | 100 | DAYS | 100 | 100 | DAYS | MENSTRUAL HISTORY | 10 | 2017-03-02 | 196 |
| 2 | ABC-123 | SC | 101 | 2 | EGESTAGE | Estimated Gestational Age | PREGNANCY-RELATED FINDINGS | 135 | DAYS | 135 | 135 | DAYS | ULTRASOUND | 11 | 2017-04-01 | 226 |
| 3 | ABC-123 | SC | 101 | 3 | EGESTAGE | Estimated Gestational Age | PREGNANCY-RELATED FINDINGS | 265 | DAYS | 265 | 265 | DAYS | BALLARD | 13.1 | 2017-06-10 | 297 |

**Example 3**
This example shows data from a multi-year study in which marital status and whether the subject was a student were collected annually.

*sc.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SCSEQ | SCTESTCD | SCTEST | SCORRES | SCSTRESC | SCDTC | SCDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | SC | 305 | 1 | MARISTAT | Marital Status | NEVER MARRIED | NEVER MARRIED | 2012-01-14 | -2 |
| 2 | ABC123 | SC | 305 | 2 | STDNTIND | Student Indicator | Y | Y | 2012-01-14 | -2 |
| 3 | ABC123 | SC | 305 | 3 | MARISTAT | Marital Status | DOMESTIC PARTNER | DOMESTIC PARTNER | 2013-01-22 | 374 |
| 4 | ABC123 | SC | 305 | 4 | STDNTIND | Student Indicator | Y | Y | 2013-01-22 | 374 |
| 5 | ABC123 | SC | 305 | 5 | MARISTAT | Marital Status | MARRIED | MARRIED | 2014-01-16 | 734 |
| 6 | ABC123 | SC | 305 | 6 | STDNTIND | Student Indicator | N | N | 2014-01-16 | 734 |

---
### 6.3.11 Subject Status (SS)

#### SS – Description/Overview
A findings domain that contains the subject's status that is evaluated periodically to determine if it has changed.

#### SS – Specification
ss.xpt, Subject Status — Findings. One record per status per visit per subject, Tabulation.

**Structure:** One record per status per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | SS |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | SSSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | SSGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | SSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 7 | SSTESTCD | Status Short Name | Char | Topic | Req | * |
| 8 | SSTEST | Status Name | Char | Synonym Qualifier | Req | * |
| 9 | SSCAT | Category for Assessment | Char | Grouping Qualifier | Perm | * |
| 10 | SSSCAT | Subcategory for Assessment | Char | Grouping Qualifier | Perm | * |
| 11 | SSORRES | Result or Finding Original Result | Char | Result Qualifier | Exp |  |
| 12 | SSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | * |
| 13 | SSSTAT | Completion Status | Char | Record Qualifier | Perm | (ND) |
| 14 | SSREASND | Reason Assessment Not Performed | Char | Record Qualifier | Perm |  |
| 15 | SSEVAL | Evaluator | Char | Record Qualifier | Perm | (EVAL) |
| 16 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 17 | VISIT | Visit Name | Char | Timing | Perm |  |
| 18 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 19 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 20 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 21 | SSDTC | Date/Time of Assessment | Char | Timing | Exp | ISO 8601 datetime or interval |
| 22 | SSDY | Study Day of Assessment | Num | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SSSEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **SSGRPID**: Used to tie together a block of related records in a single domain for a subject.
- **SSSPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page.
- **SSTESTCD**: Short name of the status assessment described in SSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SSTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "SURVSTAT".
- **SSTEST**: Verbatim name of the status assessment used to obtain the finding. The value in SSTEST cannot be longer than 40 characters. Example: "Survival Status".
- **SSCAT**: Used to categorize observations across subjects.
- **SSSCAT**: A further categorization.
- **SSORRES**: Result of the status assessment finding as originally received or collected.
- **SSSTRESC**: Contains the result value for all findings copied or derived from SSORRES, in a standard format.
- **SSSTAT**: Used to indicate a status assessment was not done. Should be null if a result exists in SSORRES.
- **SSREASND**: Describes why an assessment was not performed. Example: "Subject refused". Used in conjunction with SSSTAT when value is "NOT DONE".
- **SSEVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "CAREGIVER", "ADJUDICATION COMMITTEE", "FRIEND".
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm.
- **EPOCH**: Epoch associated with the start date/time of the subject status assessment.
- **SSDTC**: Date and time of the subject status assessment represented in ISO 8601 character format.
- **SSDY**: Study day of the subject status assessment, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.


#### SS – Assumptions

1. Details about the circumstances of a subject's status are stored in the appropriate separate domain(s), even when collection is triggered by the response to the status assessment. For example, if a subject's survival status is "DEAD", the date of death must be stored in DM and within a final disposition record in DS. Only the status collection date, the status question, and the status response are stored in SS.

2. RELREC may be used to link assessments in SS with data in other domains that were collected as a result of the subject's status assessment.

3. There are separate codelists for SS tests and responses.

    a. Associations between the SS tests and response codelists are described in the SS Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

4. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the SS domain, but the following qualifiers would generally not be used: --MODIFY, --POS, --BODSYS, --ORRESU, --ORNRLO, --ORNRHI, --STRESN, --STRESU, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --NAM, --LOINC, --SPEC, --SPCCND, --LOC, --METHOD, --BLFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV.

#### SS – Examples

**Example 1**
In this example, subjects complete a 10-week treatment regimen and are then contacted by phone every month for 3 months. The phone contact assesses the subject's survival status. If the survival status is "DEAD", additional information is collected in order to complete the subject's final disposition record in DS and to record the date of death in DM (DS and DM records are not shown here).

*ss.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SSSEQ | SSTESTCD | SSTEST | SSORRES | SSSTRESC | VISITNUM | VISIT | SSDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | SS | XYZ-333-009 | 1 | SURVSTAT | Survival Status | ALIVE | ALIVE | 10 | MONTH 1 | 2010-04-15 |
| 2 | XYZ | SS | XYZ-333-009 | 2 | SURVSTAT | Survival Status | ALIVE | ALIVE | 20 | MONTH 2 | 2010-05-12 |
| 3 | XYZ | SS | XYZ-333-009 | 3 | SURVSTAT | Survival Status | ALIVE | ALIVE | 30 | MONTH 3 | 2010-06-15 |
| 4 | XYZ | SS | XYZ-428-021 | 1 | SURVSTAT | Survival Status | ALIVE | ALIVE | 10 | MONTH 1 | 2010-08-03 |
| 5 | XYZ | SS | XYZ-428-021 | 2 | SURVSTAT | Survival Status | DEAD | DEAD | 20 | MONTH 2 | 2010-09-06 |

---
### 6.3.12 Tumor/Lesion Domains

The Tumor/Lesion domains (TU, TR) represent data collected in clinical trials where sites of disease (e.g., tumors/lesions/locations of interest, lymph nodes, organs of interest in the assessment of the disease) are identified and then repeatedly measured/assessed at subsequent time points and often used in an evaluation of disease response(s). As such, these domains would be applicable for representing data to support disease response criteria. These 2 domains each have a distinct purpose and are related to each other, and may also be related to assessments in the RS domain (see Section 6.3.9.3, Disease Response and Clin Classification).
#### 6.3.12.1 Tumor/Lesion Identification (TU)

##### TU -- Description/Overview

A findings domain that represents data that uniquely identifies tumors, lesions, or locations of interest under study.

The TU domain represents data that uniquely identifies tumors, lesions, or locations of interest (e.g., tumors, cardiovascular culprit lesions, organs, bone marrow, other sites of disease such as lymph nodes). Commonly, tumors/lesions/locations of interest are identified by an investigator and/or independent assessor and classified according to the disease assessment criteria. For example, an oncology study using RECIST criteria would identify target, non-target, and new tumors.

A record in the TU domain contains the following information:

- a unique tumor ID value
- anatomical location of the tumor
- method used to identify the tumor
- role of the individual identifying the tumor
- timing information.

##### TU -- Specification

tu.xpt, Tumor/Lesion Identification -- Findings. One record per identified tumor per subject per assessor, Tabulation.

**Structure:** One record per identified tumor per subject per assessor
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | TU |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | TUSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | TUGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | TUREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | TUSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | TULNKID | Link ID | Char | Identifier | Exp |  |
| 9 | TULNKGRP | Link Group ID | Char | Identifier | Perm |  |
| 10 | TUTESTCD | Tumor/Lesion ID Short Name | Char | Topic | Req | C96784 |
| 11 | TUTEST | Tumor/Lesion ID Test Name | Char | Synonym Qualifier | Req | C96783 |
| 12 | TUORRES | Tumor/Lesion ID Result | Char | Result Qualifier | Exp |  |
| 13 | TUSTRESC | Tumor/Lesion ID Result Std. Format | Char | Result Qualifier | Exp | C123650 |
| 14 | TUNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |
| 15 | TULOC | Location of the Tumor/Lesion | Char | Record Qualifier | Exp | C74456 |
| 16 | TULAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| 17 | TUDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| 18 | TUPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |
| 19 | TUMETHOD | Method of Identification | Char | Record Qualifier | Exp | C85492 |
| 20 | TULOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 21 | TUBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 22 | TUEVAL | Evaluator | Char | Record Qualifier | Exp | C78735 |
| 23 | TUEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| 24 | TUACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |
| 25 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 26 | VISIT | Visit Name | Char | Timing | Perm |  |
| 27 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 28 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 29 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 30 | TUDTC | Date/Time of Tumor/Lesion Identification | Char | Timing | Exp | ISO 8601 datetime or interval |
| 31 | TUDY | Study Day of Tumor/Lesion Identification | Num | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **TUSEQ**: Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number.
- **TUGRPID**: Used to link together a block of related records within a subject in a domain. Can be used to group split or merged tumors/lesions which have been identified.
- **TUREFID**: Internal or external identifier (e.g., medical image ID number).
- **TUSPID**: Sponsor-defined identifier.
- **TULNKID**: Identifier used to link identified tumor/lesion/location of interest to the assessment results (in TR domain) over the course of the study.
- **TULNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **TUTESTCD**: Short name of the TEST in TUTEST. TUTESTCD cannot be longer than 8 characters nor can start with a number. TUTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "TUMIDENT". See assumption 3.
- **TUTEST**: Verbatim name of the test for the tumor/lesion identification. The value in TUTEST cannot be longer than 40 characters. Example: "Tumor identification". See assumption 3.
- **TUORRES**: Result of the tumor/lesion identification. The result of tumor/lesion identification is a classification of the identified tumor/lesion. Example: When TUTESTCD = "TUMIDENT", values of TUORRES might be "TARGET", "NON-TARGET", "NEW", or "BENIGN ABNORMALITY".
- **TUSTRESC**: Contains the result value for all findings copied or derived from TUORRES in a standard format.
- **TUNAM**: The name or identifier of the vendor that performed the tumor/lesion Identification. This column can be left null when the investigator provides the complete set of data in the domain.
- **TULOC**: Used to specify the anatomical location of the identified tumor/lesion (e.g., "LIVER"). Note: When anatomical location is broken down and collected as distinct pieces of data that when combined provide the overall location information (e.g., laterality/directionality/distribution), then additional anatomical location qualifiers should be used. See assumption 3.
- **TULAT**: Qualifier for anatomical location or specimen further detailing laterality (e.g., "LEFT", "RIGHT", "BILATERAL").
- **TUDIR**: Qualifier for anatomical location or specimen further detailing directionality (e.g., "UPPER", "INTERIOR").
- **TUPORTOT**: Qualifier for anatomical location or specimen further detailing the distribution, which means arrangement of, or apportioning of. Examples: "ENTIRE", "SINGLE", "SEGMENT", "MULTIPLE".
- **TUMETHOD**: Method used to identify the tumor/lesion. Examples: "MRI", "CT SCAN".
- **TULOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.
- **TUBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that TUBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.
- **TUEVAL**: Role of the person who provided the evaluation. Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR". This column can be left null when the investigator provides the complete set of data in the domain. However, the column should contain no null values when data from 1 or more independent assessors is included. For example, the rows attributed to the investigator should contain a value of "INVESTIGATOR".
- **TUEVALID**: Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 9.
- **TUACPTFL**: In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the date/time at which the assessment was made.
- **TUDTC**: TUDTC variable represents the date of the scan/image/physical exam. TUDTC does not represent the date that the image was read to identify tumors. TUDTC also does not represent the VISIT date.
- **TUDY**: Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

##### TU -- Assumptions

1. The TU domain should contain only 1 record for each unique tumor/lesion/location of interest identified by an assessor (e.g., investigator, independent assessor) per medical evaluator. The initial identification of a tumor/lesion/location of interest is done once, usually at baseline (e.g., identification of target and non-target tumors/lesions) or first appearance of new tumor/lesion. The identification information, including the location description, must not be repeated for every visit. A record is required in TU to identify and create the TULNKID when there are associated records in TR with matching TRLNKID. The following are examples of when post-baseline records might be included in the TU domain:

    a. A new tumor/lesion may emerge at any time during a study; therefore, a new post-baseline record would represent the identification of the new tumor/lesion.

    b. If a tumor/lesion identified at baseline subsequently splits into separate distinct tumors/lesions, then additional post-baseline records can be included to distinctly identify the split tumors/lesions.

    c. In situations where a re-baseline of targets and non-targets is required (e.g., a cross-over study), then a separate set of target and non-target tumors/lesions might be identified and those identification records would be represented.

2. TRLNKID is used to relate an identification record in the TU domain to assessment records in the Tumor/Lesion Results (TR) domain. The organization of data across the TU and TR domains requires a linking mechanism. The TULNKID variable is used to provide a unique code for each identified tumor/lesion. The values of TULNKID are compound values that may carry the following information: an indication of the role (or assessor) providing the data record, when it is someone other than the principal investigator; an indication of whether the data record is for a target or non-target tumor/lesion; a tracking identifier or number; and an indication of whether the tumor/lesion has split (see assumption 3 for details on splitting). A RELREC relationship record can be created to describe the link, probably as a dataset-to-dataset link.

   TUTESTCD/TUTEST values for this domain are published as Controlled Terminology. For some TUTESTCD/TUTEST values, CDISC CT includes codelists for use with TUORRES. The associations between the test values and results are in the Oncology codetable, which, along with the CT Rules for Oncology, is available at https://www.cdisc.org/standards/terminology/controlled-terminology. During the course of a trial, a tumor/lesion might split into one or more distinct tumors/lesions, or 2 or more tumors/lesions might merge to form a single tumor/lesion. The following example shows the preferred approach for representing split lesions in TU. However, the approach depends on how the data for split and merged tumors/lesions are captured. The preferred approach requires the measurements of each distinct tumor/lesion to be captured individually.

    Example target tumor T04, identified at the screening visit, splits into 2 at week 16. Two new records are created with TUTEST = "Tumor Split"; TULNKID reflects the split by adding 0.1 and 0.2 to the original TULNKID value.

| TULNKID | TUTESTCD | TUTEST | TUORRES | VISIT |
|---------|----------|--------|---------|-------|
| T01 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
| T02 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
| T03 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
| T04 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
| NT01 | TUMIDENT | Tumor Identification | NON-TARGET | SCREEN |
| NT02 | TUMIDENT | Tumor Identification | NON-TARGET | SCREEN |
| T04.1 | TUSPLIT | Tumor Split | TARGET | WEEK 16 |
| T04.2 | TUSPLIT | Tumor Split | TARGET | WEEK 16 |
| NEW01 | TUMIDENT | Tumor Identification | NEW | WEEK 32 |

    If the data collection does not support this approach (i.e., measurements of split tumors/lesions are reported as a summary under the "parent" tumor/lesion), then it may not be possible to include a record in the TU domain. In this situation, the assessments of split and merge tumors/lesions would be represented only in the TR domain.

3. For some response criteria (e.g., Lugano, Kumar IMWG 2016), tumors are assessed by location of interest. A record is required in TU in order to link the assessments of the particular location of interest in TR.

    This example represents tumors assessed by location of interest. In TULNKID = "L01", the spleen is identified as a location of interest using computerized tomography (CT) scan. In TULNKID = "L04", the whole body is identified as a location of interest using positron emission tomography (PET) scan.

| TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TUMETHOD |
|---------|----------|--------|---------|-------|----------|
| L01 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | SPLEEN | CT SCAN |
| L02 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | LIVER | CT SCAN |
| L03 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | BONE MARROW | PET SCAN |
| L04 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | BODY | PET SCAN |

4. During the course of a trial, when a new tumor/lesion is identified, information about that new tumor/lesion may be collected to different levels of detail. For example, if anatomical location of a new tumor/lesion is not collected, TULOC will be blank. All new tumors/lesions are to be represented in TU and TR domains.

5. The additional anatomical location variables --LAT, --DIR, --PORTOT were added from the SDTM. These extra variables allow for more detailed information to be collected that further clarifies the value of the TULOC variable.

6. In the oncology setting, when a new tumor is identified, a record must be included in both the TU and TR domains. At a minimum, the TR record would contain TRLNKID = "NEW0" and TRTESTCD = "TUMSTATE" and TRORRES = "PRESENT" for unequivocal new tumors. The TU record may contain different levels of detail depending upon the data collection methods employed. Although it is possible that a sponsor may have a different chosen method, the following are the most common scenarios:

    a. The occurrence of a new tumor/lesion is the sole piece of information that a sponsor collects, because this is a sign of disease progression; no further details are required. In such cases, a record would be created where TUTEST = "Tumor Identification" and TUORRES = "NEW", and the identifier, TULNKID, would be populated in order to link to the associated information in the TR domain.

    b. The occurrence of a new tumor/lesion and the anatomical location of that newly identified tumor/lesion are the only collected pieces of information. In this case, it is expected that a record would be created where TUTEST = "Tumor Identification" and TUORRES = "NEW"; the TULOC variable would be populated with the anatomical location information (the additional location variables may be populated depending on the level of detail collected), and the identifier, TULNKID, would be populated in order to link to the associated information in the TR domain.

    c. The sponsor records the occurrence of a new tumor/lesion to the same level of detail as target tumors/lesions. For example, with the occurrence of a new tumor/lesion, its anatomical location and its measurement might be recorded. In this case, it is expected that a record would be created where TUTEST = "Tumor Identification" and TUORRES = "NEW". The TULOC variable would be populated with the anatomical location information (the additional location variables may be populated depending on the level of detail collected) and the identifier, TULNKID, would be populated in order to link to the associated information in the TR domain. In this scenario, measurements/assessments would also be recorded in the TR domain.

7. The acceptance flag variable (TUACPTFL) identifies records that have been determined to be the accepted assessments/measurements by an independent assessor. This flag would be provided by an independent assessor and when multiple evaluators (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provide assessments or evaluations at the same time point or an overall evaluation. This flag should not be used by a sponsor for any other purpose. It is not expected that the TUACPTFL flag would be populated by the sponsor; instead, that type of record selection should be handled in the analysis dataset (ADaM).

8. The evaluator-specified variable TUEVALID is used in conjunction with TUEVAL to provide additional detail regarding who is providing tumor identification information (e.g., TUEVAL = "INDEPENDENT ASSESSOR", TUEVALID = "RADIOLOGIST 1"). The TUEVALID variable is subject to controlled terminology. Note: TUEVAL must also be populated when TUEVALID is populated.

9. If indicator questions for specific types of tumor or lesions are collected (e.g., Does the subject have target tumors? Does the subject have any non-targets? Did the subject have metastatic disease at screening?), then these TUTESTs will be included in TU. If indicator questions are not collected, do not introduce them into TU.

    This example shows indicator TUTESTs for a subject with non-target lesions only.

| TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TUMETHOD |
|---------|----------|--------|---------|-------|----------|
|  | NTIND | Non-Target Indicator | Y |  | CT SCAN |
|  | TIND | Target Indicator | N |  | CT SCAN |
| NT01 | TUMIDENT | Tumor Identification | NON-TARGET | LUNG | CT SCAN |

    This example shows indicator TUTESTs for the identification of the sites of metastatic disease sites at baseline.

| TULNKID | TUTESTCD | TUTEST | TUORRES | TUSTAT | TULOC | TUMETHOD | VISIT |
|---------|----------|--------|---------|--------|-------|----------|-------|
|  | METIND | Metastatic Tumor Site Indicator | Y |  | LIVER | CT SCAN | BASELINE |
|  | METIND | Metastatic Tumor Site Indicator | N |  | BRAIN | MRI | BASELINE |
|  | METIND | Metastatic Tumor Site Indicator |  | NOT DONE | PLEURAL CAVITY |  | BASELINE |

10. Disease recurrence can be represented in the TU domain as an identification for the appearance of new tumors. The TUTEST Disease Recurrence Relative Location is used identify the region or relative location for the disease recurrence. The image identifier is in TUREFID and may match a PRREFID in the Procedures (PR) domain. The PR domain would contain the scans performed per protocol at each assessment; only when new tumors appear would records be included in TU.

    This example shows disease recurrence data in an adjuvant breast cancer study where the subject was initially diagnosed with cancer in the left breast only. This example shows a case where disease recurrence was identified in various locations. TUTEST=Disease Recurrence Relative Location is used to identify the reference location of the recurrence (e.g., LOCAL, REGIONAL, DISTANT, LOCOREGIONAL). A local disease recurrence was identified in the left breast, regional disease recurrence was identified in the ipsilateral internal mammary and the ipsilateral infraclavicular nodes, distant disease recurrence was identified in the liver and colon, and contralateral disease recurrence was identified in the right breast.

| TUREFID | TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TULAT | TUMETHOD |
|---------|---------|----------|--------|---------|-------|-------|----------|
| IMG-00007 | LOC01 | DRCRLTLC | Disease Recurrence Relative Location | LOCAL | BREAST | LEFT | CT SCAN |
| IMG-00007 | REG01 | DRCRLTLC | Disease Recurrence Relative Location | REGIONAL | INTERNAL MAMMARY LYMPH NODE |  | CT SCAN |
| IMG-00007 | REG02 | DRCRLTLC | Disease Recurrence Relative Location | REGIONAL | INFRACLAVICULAR LYMPH NODE |  | CT SCAN |
| IMG-00007 | DIS01 | DRCRLTLC | Disease Recurrence Relative Location | DISTANT | LIVER |  | CT SCAN |
| IMG-00007 | DIS02 | DRCRLTLC | Disease Recurrence Relative Location | DISTANT | COLON |  | CT SCAN |
| IMG-00007 | CON01 | DRCRLTLC | Disease Recurrence Relative Location | CONTRALATERAL | BREAST | RIGHT | CT SCAN |

11. The following proposed supplemental qualifiers would be used for oncology studies to represent information regarding previous irradiation of a tumor when that information is captured in association with a specific tumor.

| QNAM | QLABEL | Definition |
|------|--------|------------|
| TUPREVIR | Previously Irradiated | Indication of previous irradiation to a tumor |
| TUPREISP | Irradiated then Subsequent Progression | Indication of documented progression subsequent to irradiation |

12. When additional data are collected about a procedure used for tumor/lesion identification, the data about the procedure are stored in the PR domain; the link between the tumor/lesion identification and the procedure should be recorded using RELREC.

13. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the TU domain, but the following qualifiers would not generally be used: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.
#### 6.3.12.2 Tumor/Lesion Results (TR)

##### TR – Description/Overview
A findings domain that represents quantitative measurements and/or qualitative assessments of the tumors, lesions, or locations of interest identified in the Tumor/Lesion Identification (TU) domain.

The TR domain represents quantitative measurements and/or qualitative assessments of the tumors, lesions, or locations of interest (e.g., tumors, cardiovascular culprit lesions, organs, bone marrow, other sites of disease such as lymph nodes) identified in the Tumor/Lesion Identification (TU) domain. These measurements or qualitative assessments may be recorded at baseline and then at each subsequent assessment to support response evaluations. A typical record in the TR domain contains the following information:

- a unique tumor/lesion/location of interest ID value
- test and result
- method used
- role of the individual making the assessment
- timing information

Clinically accepted evaluation criteria expect that a tumor/lesion/location of interest identified by the ID is the same tumor/lesion/location of interest at each subsequent assessment. The TR domain does not include anatomical location information on each measurement/assessment record, because this would duplicate information represented in TU. The multi-domain approach to representing oncology assessment data was developed largely to reduce duplication of stored information.

##### TR – Specification
tr.xpt, Tumor/Lesion Results — Findings. One record per tumor measurement/assessment per visit per subject per assessor, Tabulation.

**Structure:** One record per tumor measurement/assessment per visit per subject per assessor
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | TR |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | TRSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | TRGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | TRREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | TRSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | TRLNKID | Link ID | Char | Identifier | Exp |  |
| 9 | TRLNKGRP | Link Group ID | Char | Identifier | Perm |  |
| 10 | TRTESTCD | Tumor/Lesion Assessment Short Name | Char | Topic | Req | (TRTESTCD) |
| 11 | TRTEST | Tumor/Lesion Assessment Test Name | Char | Synonym Qualifier | Req | (TRTEST) |
| 12 | TRORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 13 | TRORRESU | Original Units | Char | Variable Qualifier | Exp | (UNIT) |
| 14 | TRSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | (TRPROPRS) |
| 15 | TRSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |
| 16 | TRSTRESU | Standard Units | Char | Variable Qualifier | Exp | (UNIT) |
| 17 | TRSTAT | Completion Status | Char | Record Qualifier | Perm | (ND) |
| 18 | TRREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 19 | TRNAM | Laboratory/Vendor Name | Char | Record Qualifier | Perm |  |
| 20 | TRMETHOD | Method Used to Identify the Tumor/Lesion | Char | Record Qualifier | Exp | (METHOD) |
| 21 | TRLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | (NY) |
| 22 | TRBLFL | Baseline Flag | Char | Record Qualifier | Perm | (NY) |
| 23 | TREVAL | Evaluator | Char | Record Qualifier | Exp | (EVAL) |
| 24 | TREVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | (MEDEVAL) |
| 25 | TRACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | (NY) |
| 26 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 27 | VISIT | Visit Name | Char | Timing | Perm |  |
| 28 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 29 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 30 | EPOCH | Epoch | Char | Timing | Perm | (EPOCH) |
| 31 | TRDTC | Date/Time of Tumor/Lesion Measurement | Char | Timing | Exp | ISO 8601 datetime or interval |
| 32 | TRDY | Study Day of Tumor/Lesion Measurement | Num | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **TRSEQ**: Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number.
- **TRGRPID**: Used to link together a block of related records within a subject in a domain.
- **TRREFID**: Internal or external identifier.
- **TRSPID**: Sponsor-defined identifier.
- **TRLNKID**: Identifier used to link the assessment result records to the individual tumor/lesion identification record in TU domain.
- **TRLNKGRP**: Used to group and link all of the measurement/assessment records used in the assessment of the response record in the RS domain.
- **TRTESTCD**: Short name of the TEST in TRTEST. TRTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TUMSTATE", "DIAMETER", "LESSCIND", "LESRVIND". See assumption 3.
- **TRTEST**: Verbatim name of the test or examination used to obtain the measurement or finding. The value in TRTEST cannot be longer than 40 characters. Examples: "Tumor State", "Diameter", "Volume", "Lesion Success Indicator", "Lesion Revascularization Indicator". See assumption 3.
- **TRORRES**: Result of the tumor/lesion measurement/assessment as originally received or collected.
- **TRORRESU**: Original units in which the data were collected. The unit for TRORRES. Example: "mm".
- **TRSTRESC**: Contains the result value for all findings copied or derived from TRORRES, in a standard format or standard units. TRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in TRSTRESN.
- **TRSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from TRSTRESC. TRSTRESN should store all numeric test results or findings.
- **TRSTRESU**: Standardized unit used for TRSTRESN.
- **TRSTAT**: Used to indicate a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Should be null if a result exists in TRORRES.
- **TRREASND**: Describes why a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Examples: "SCAN NOT PERFORMED", "NOT ASSESSABLE: IMAGE OBSCURED TUMOR". Used in conjunction with TRSTAT when value is "NOT DONE".
- **TRNAM**: The name or identifier of the vendor that performed the tumor/lesion measurement or assessment. This column can be left null when the investigator provides the complete set of data in the domain.
- **TRMETHOD**: Method used to measure the tumor/lesion/location of interest. Examples: "MRI", "CT SCAN", "PET SCAN", "Coronary angiography".
- **TRLOBXFL**: Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.
- **TRBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that TRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.
- **TREVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR".
- **TREVALID**: Used to distinguish multiple evaluators with the same role recorded in TREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 6.
- **TRACPTFL**: In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Epoch associated with the element in the planned sequence of elements for the arm to which the subject was assigned.
- **EPOCH**: Epoch associated with the date/time at which the assessment was made.
- **TRDTC**: The date of the scan/image/physical exam. TRDTC does not represent the date that the image was read to identify tumors/lesions. TRDTC also does not represent the VISIT date.
- **TRDY**: Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.


##### TR – Assumptions
1. TRLNKID is used to relate records in the TR domain to an identification record in TU domain. The organization of data across the TU and TR domains requires a RELREC relationship to link the related data rows. A dataset-to-dataset link would be the most appropriate linking mechanism. Utilizing 1 of the existing ID variables is not possible, because --GRPID, --REFID, and --SPID may be used for other purposes, per the SDTM. The --LNKID variable is used for values that support a RELREC dataset-to-dataset relationship and to provide a unique code for each identified tumor/lesion/location of interest.
2. TRLNKGRP is used to relate records in the TR domain to a response assessment record in the RS domain. The organization of data across the TR and RS domains requires a RELREC relationship to link the related data rows. A dataset-to-dataset link would be the most appropriate linking mechanism. Utilizing 1 of the existing ID variables is not possible because --GRPID, --REFID, and --SPID may be used for other purposes, per the SDTM. The --LNKGRP variable is used for values that support a RELREC dataset-to-dataset relationship and to provide a unique code for each response and associated tumor/lesion measurements/assessments.
3. TRTESTCD/TRTEST values for this domain are published as Controlled Terminology. For some TRTESTCD/TRTEST values, CDISC CT includes codelists for use with TRORRES. The associations between the test values and results are in the Oncology codetable, which, along with the Controlled Terminology Rules for Oncology, is available at https://www.cdisc.org/standards/terminology/controlled-terminology. The sponsor should not derive results for any test (e.g., percent change from nadir in sum of diameter) if the result was not collected. Tests would be included in the domain only if those data points have been collected on a CRF, presented by the CRF collection system, or supplied by an external assessor as part of an electronic data transfer. It is not intended that the sponsor would create derived records to supply those values in the TR domain. Derived records/results (outside the CRF) should be provided in the analysis dataset (ADaM).
4. In order to support data value standardization it is sometimes appropriate to standardize an original result value in TRORRES to a standardized result value in TRSTRESC and TRSTRESN. For example, in the published RECIST criteria, a standardized value of 5 mm is used in the calculation to determine response when a tumor is "too small to measure." The original or collected value "TOO SMALL TO MEASURE" should be represented in the TRORRES variable and the standardized value should be represented in the TRSTRESC and TRSTRESN variables. The information should be represented on a single row of data showing the standardization between the original result, TRORRES, and the standard results, TRSTRESC/TRSTRESN, as follows:

    | TRLNKID | TRTESTCD | TRTEST | TRORRES | TRORRESU | TRSTRESC | TRSTRESN | TRSTRESU |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | T01 | DIAMETER | Diameter | TOO SMALL TO MEASURE | mm | 5 | 5 | mm |

    Note: This is an exception to SDTMIG general variable rule 4.1.5.1, Original and Standardized Results of Findings and Tests Not Done.

5. The acceptance flag variable (TRACPTFL) identifies those records that have been determined to be the accepted assessments/measurements by an independent assessor. This flag would be provided by an independent assessor and when multiple assessors (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provide assessments or evaluations at the same time point or an overall evaluation. This flag should not be used by a sponsor for any other purpose. It is not expected that the TRACPTFL flag would be populated by the sponsor; instead, that type of record selection should be handled in the analysis dataset (ADaM).
6. The evaluator-specified variable (TREVALID) is used in conjunction with TREVAL to provide additional detail of who is providing measurements or assessments (e.g., TREVAL = "INDEPENDENT ASSESSOR", TREVALID = "RADIOLOGIST 1"). The TREVALID variable is subject to controlled terminology. Note: TREVAL must also be populated when TREVALID is populated.
7. When additional data are collected about a procedure (e.g., imaging procedure) from which tumor/lesion results are determined, the data about the procedure is stored in the PR domain and the link between the tumor/lesion results and the procedure should be recorded using RELREC.
8. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the TR domain, but the following qualifiers would not generally be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.
#### 6.3.12.3 Tumor Identification/Tumor Results Examples

**Example 1**

This is an example of using the TU domain to represent non-cancerous lesions identified in the heart.

Subject 40913 had a peripheral vascular intervention (PVI) procedure on February 1, 2007. A target lesion (L01) was identified in the infrarenal aorta within the aorto-iliac vessel (L01-1). During the same PVI procedure, the subject also had a target graft lesion (L01-G) identified in the left femoro-popliteal graft (L01-G1). The lesion location was noted within the graft anastomosis proximal, the type was a synthetic graft composed of Gore-Tex, and the anastomosis was in the left popliteal artery.

**Rows 1-2:** Show the target lesion located in the infrarenal aorta and within the aorta-iliac vessel.

**Row 3:** Shows the PVI target limb in which the graft lesion is located identified by the investigator.

**Rows 4-5:** Show the target graft lesion located in the left femoro-popliteal graft and within the femoro-popliteal vessel.

*tu.xpt*

| Row | STUDYID | DOMAIN | USUBJID | TUSEQ | TULNKID | TUTESTCD | TUTEST | TUORRES | TUSTRESC | TULOC | TULAT | TUMETHOD | TUEVAL | VISITNUM | VISIT | TUDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | STUDY01 | TU | 40913 | 1 | L01 | LESIDENT | Lesion Identification | TARGET | TARGET | INFRARENAL AORTA | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
| 2 | STUDY01 | TU | 40913 | 2 | L01-1 | VSLIDENT | Vessel Lesion Identification | TARGET | TARGET | AORTO-ILIAC PERIPHERAL ARTERY | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
| 3 | STUDY01 | TU | 40913 | 3 | L01-2 | LMLIDENT | Limb Lesion Identification | TARGET | TARGET | LEG | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
| 4 | STUDY01 | TU | 40913 | 4 | L01-G | GRLIDENT | Graft Lesion Identification | TARGET | TARGET | FEMORO-POPLITEAL PERIPHERAL ARTERY | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
| 5 | STUDY01 | TU | 40913 | 5 | L01-G1 | VSLIDENT | Vessel Lesion Identification | TARGET | TARGET | FEMORO-POPLITEAL PERIPHERAL ARTERY | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |

Additional information about the lesion (e.g., lesion location within the graft, graft anastomosis) as well as details regarding the graft type and material are given using supplemental qualifiers.

*supptu.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | STUDY01 | TU | 40913 | TUSEQ | 4 | TUPAGLL | Peripheral Graft Lesion Location | GRAFT ANASTOMOSIS PROXIMAL | CRF |  |
| 2 | STUDY01 | TU | 40913 | TUSEQ | 4 | TUPAGA | Peripheral Artery Graft Anastomosis | LEFT POPLITEAL ARTERY | CRF |  |
| 3 | STUDY01 | TU | 40913 | TUSEQ | 4 | TUOTHLDS | Other Lesion Description | LESION IS 5MM FROM THE ORIGIN OF THE GRAFT | CRF |  |
| 4 | STUDY01 | TU | 40913 | TUSEQ | 4 | TUPAGT | Peripheral Artery Graft Type | SYNTHETIC GRAFT | CRF |  |
| 5 | STUDY01 | TU | 40913 | TUSEQ | 4 | TUPAGSM | Peripheral Artery Graft Synthetic Material | GORE-TEX | CRF |  |

**Example 2**

This is an example of tumors identified and tracked using RECIST 1.1 criteria.

TU shows the target and non-target tumors identified by an investigator at a screening visit and also shows that the investigator determined at the week 6 visit that 1 of the previously identified tumors had split.

**Rows 1-6:** Show for subject 44444 the target and non-target tumors identified by the investigator at the screening visit.

**Rows 7-8:** Show the investigator determined that a tumor (TULNKID = "T04" at screening) had split into 2 separate tumors at the week 6 visit. The 2 distinct pieces of the original tumor were then tracked independently from that point in the study forward.

*tu.xpt*

| Row | STUDYID | DOMAIN | USUBJID | TUSEQ | TUGRPID | TULNKID | TUTESTCD | TUTEST | TUORRES | TUSTRESC | TULOC | TULAT | TUMETHOD | TUEVAL | VISITNUM | VISIT | TUDTC | TUDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | TU | 44444 | 1 |  | T01 | TUMIDENT | Tumor Identification | TARGET | TARGET | LIVER |  | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 2 | ABC | TU | 44444 | 2 |  | T02 | TUMIDENT | Tumor Identification | TARGET | TARGET | KIDNEY | RIGHT | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 3 | ABC | TU | 44444 | 3 |  | T03 | TUMIDENT | Tumor Identification | TARGET | TARGET | CERVICAL LYMPH NODE | LEFT | MRI | INVESTIGATOR | 10 | SCREEN | 2010-01-02 | -2 |
| 4 | ABC | TU | 44444 | 4 |  | T04 | TUMIDENT | Tumor Identification | TARGET | TARGET | SKIN OF THE TRUNK |  | PHOTOGRAPHY | INVESTIGATOR | 10 | SCREEN | 2010-01-03 | -1 |
| 5 | ABC | TU | 44444 | 5 |  | NT01 | TUMIDENT | Tumor Identification | NON-TARGET | NON-TARGET | THYROID GLAND | RIGHT | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 6 | ABC | TU | 44444 | 6 |  | NT02 | TUMIDENT | Tumor Identification | NON-TARGET | NON-TARGET | CEREBELLUM | RIGHT | MRI | INVESTIGATOR | 10 | SCREEN | 2010-01-02 | -2 |
| 7 | ABC | TU | 44444 | 7 | T04 | T04.1 | TUSPLIT | Tumor Split | TARGET | TARGET | SKIN OF THE TRUNK |  | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
| 8 | ABC | TU | 44444 | 8 | T04 | T04.2 | TUSPLIT | Tumor Split | TARGET | TARGET | SKIN OF THE TRUNK |  | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |

The supplemental qualifier dataset below shows that "T01", "T02", and "T04" were not previously irradiated and "T03" was previously irradiated with subsequent progression after irradiation.

*supptu.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | TU | 44444 | TULNKID | T01 | TUPREVIR | Previously Irradiated | N |
| 2 | ABC | TU | 44444 | TULNKID | T02 | TUPREVIR | Previously Irradiated | N |
| 3 | ABC | TU | 44444 | TULNKID | T03 | TUPREVIR | Previously Irradiated | Y |
| 4 | ABC | TU | 44444 | TULNKID | T03 | TUPREISP | Irradiated then Subsequent Progression | Y |
| 5 | ABC | TU | 44444 | TULNKID | T04 | TUPREVIR | Previously Irradiated | N |

TR shows measurements (i.e., short axis) of lymph nodes as well as measurements of other non-lymph node target tumors (i.e., longest diameter). In this example, when TRTEST = "Tumor State" and TRORRES = "ABSENT", it indicates that the target lymph node lesion was no longer pathological (i.e., diameter reduced below 10mm). The overall assessment of lymph nodes is represented with TRTEST = "Lymph Nodes State". A lymph node state of "NON-PATHOLOGICAL" means that all target lymph node lesions have a short axis less than 10mm. A lymph node state of "PATHOLOGICAL" means that at least 1 target lymph node lesion has a short axis greater than or equal to 10mm.

**Rows 1-8:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the screening visit.

**Rows 9-21:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 6 visit.

**Rows 22-27:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 12 visit.

*tr.xpt*

| Row | STUDYID | DOMAIN | USUBJID | TRSEQ | TRGRPID | TRLNKGRP | TRLNKID | TRTESTCD | TRTEST | TRORRES | TRORRESU | TRSTRESC | TRSTRESN | TRSTRESU | TRSTAT | TRREASND | TRMETHOD | TREVAL | VISITNUM | VISIT | TRDTC | TRDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | TR | 44444 | 1 | TARGET | A1 | T01 | DIAMETER | Diameter | 17 | mm | 17 | 17 | mm |  |  | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 2 | ABC | TR | 44444 | 2 | TARGET | A1 | T02 | DIAMETER | Diameter | 16 | mm | 16 | 16 | mm |  |  | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 3 | ABC | TR | 44444 | 3 | TARGET | A1 | T03 | DIAMETER | Diameter | 15 | mm | 15 | 15 | mm |  |  | MRI | INVESTIGATOR | 10 | SCREEN | 2010-01-02 | -2 |
| 4 | ABC | TR | 44444 | 4 | TARGET | A1 | T04 | DIAMETER | Diameter | 14 | mm | 14 | 14 | mm |  |  | PHOTOGRAPHY | INVESTIGATOR | 10 | SCREEN | 2010-01-03 | -1 |
| 5 | ABC | TR | 44444 | 5 | TARGET | A1 |  | SUMDIAM | Sum of Diameter | 62 | mm | 62 | 62 | mm |  |  |  | INVESTIGATOR | 10 | SCREEN |  |  |
| 6 | ABC | TR | 44444 | 6 | TARGET | A1 |  | SUMNLNLD | Sum Diameters of Non Lymph Node Tumors | 47 | mm | 47 | 47 | mm |  |  |  | INVESTIGATOR | 10 | SCREEN |  |  |
| 7 | ABC | TR | 44444 | 7 | NON-TARGET | A1 | NT01 | TUMSTATE | Tumor State | PRESENT |  | PRESENT |  |  |  |  | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 8 | ABC | TR | 44444 | 8 | NON-TARGET | A1 | NT02 | TUMSTATE | Tumor State | PRESENT |  | PRESENT |  |  |  |  | MRI | INVESTIGATOR | 10 | SCREEN | 2010-01-02 | -2 |
| 9 | ABC | TR | 44444 | 9 | TARGET | A2 | T01 | DIAMETER | Diameter | 0 | mm | 0 | 0 | mm |  |  | CT SCAN | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 10 | ABC | TR | 44444 | 10 | TARGET | A2 | T02 | DIAMETER | Diameter | TOO SMALL TO MEASURE | mm | 5 | 5 | mm |  |  | CT SCAN | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 11 | ABC | TR | 44444 | 11 | TARGET | A2 | T03 | DIAMETER | Diameter | 12 | mm | 12 | 12 | mm |  |  | MRI | INVESTIGATOR | 40 | WEEK 6 | 2010-02-19 | 47 |
| 13 | ABC | TR | 44444 | 13 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm |  |  | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
| 14 | ABC | TR | 44444 | 14 | TARGET | A2 | T04.2 | DIAMETER | Diameter | 7 | mm | 7 | 7 | mm |  |  | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
| 15 | ABC | TR | 44444 | 15 | TARGET | A2 |  | SUMDIAM | Sum of Diameter | 30 | mm | 30 | 30 | mm |  |  |  | INVESTIGATOR | 40 | WEEK 6 |  |  |
| 16 | ABC | TR | 44444 | 16 | TARGET | A2 |  | SUMNLNLD | Sum Diameters of Non Lymph Node Tumors | 18 | mm | 18 | 18 | mm |  |  |  | INVESTIGATOR | 40 | WEEK 6 |  |  |
| 17 | ABC | TR | 44444 | 17 | TARGET | A2 |  | LNSTATE | Lymph Node State | PATHOLOGICAL |  | PATHOLOGICAL |  |  |  |  |  | INVESTIGATOR | 40 | WEEK 6 |  |  |
| 18 | ABC | TR | 44444 | 18 | TARGET | A2 |  | ACNSD | Absolute Change Nadir in Sum of Diam | -32 | mm | -32 | -32 | mm |  |  |  | INVESTIGATOR | 40 | WEEK 6 |  |  |
| 19 | ABC | TR | 44444 | 19 | TARGET | A2 |  | PCBSD | Percent Change From Baseline in Sum of Diameter | -52 | % | -52 | -52 | % |  |  |  | INVESTIGATOR | 40 | WEEK 6 |  |  |
| 20 | ABC | TR | 44444 | 20 | TARGET | A2 |  | PCNSD | Percent Change Nadir in Sum of Diam | -52 | % | -52 | -52 | % |  |  |  | INVESTIGATOR | 40 | WEEK 6 |  |  |
| 21 | ABC | TR | 44444 | 21 | NON-TARGET | A2 | NT01 | TUMSTATE | Tumor State | PRESENT |  | PRESENT |  |  |  |  | CT SCAN | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 22 | ABC | TR | 44444 | 22 | NON-TARGET | A2 | NT02 | TUMSTATE | Tumor State | PRESENT |  | PRESENT |  |  |  |  | MRI | INVESTIGATOR | 40 | WEEK 6 | 2010-02-19 | 47 |
| 23 | ABC | TR | 44444 | 23 | TARGET | A3 | T01 | DIAMETER | Diameter | 0 | mm | 0 | 0 | mm |  |  | CT SCAN | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 24 | ABC | TR | 44444 | 24 | TARGET | A3 | T02 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm |  |  | CT SCAN | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 25 | ABC | TR | 44444 | 25 | TARGET | A3 | T03 | DIAMETER | Diameter |  |  |  |  |  | NOT DONE | SCAN NOT PERFORMED | MRI | INVESTIGATOR | 60 | WEEK 12 |  |  |
| 26 | ABC | TR | 44444 | 26 | TARGET | A3 | T04 | DIAMETER | Diameter |  |  |  |  |  | NOT DONE | NOT ASSESSABLE: POOR IMAGE QUALITY | PHOTOGRAPHY | INVESTIGATOR | 60 | WEEK 12 |  |  |
| 27 | ABC | TR | 44444 | 27 | NON-TARGET | A3 | NT01 | TUMSTATE | Tumor State |  |  |  |  |  |  |  | CT SCAN | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 28 | ABC | TR | 44444 | 28 | NON-TARGET | A3 | NT02 | TUMSTATE | Tumor State |  |  |  |  |  | NOT DONE | SCAN NOT PERFORMED | MRI | INVESTIGATOR | 60 | WEEK 12 |  |  |

The relationship between the TU and TR datasets is represented in RELREC.

*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | TU |  | TULNKID |  | ONE | 1 |
| 2 | ABC | TR |  | TRLNKID |  | MANY | 1 |

**Example 3**

This is an example of tumors identified and tracked following RECIST 1.1 criteria, with an additional opinion provided by an independent assessor.

TU shows the target and non-target tumors identified by a radiologist at a screening visit. It also shows that the radiologist identified 2 new tumors: 1 at the week 6 visit and 1 at the week 12 visit.

**Rows 1-5:** Show the target and non-target tumors identified at screening by the independent assessor, Radiologist 1.

**Row 6:** Shows that a new tumor was identified at week 6 by the independent assessor, Radiologist 1.

**Row 7:** Shows that another new tumor was identified at week 12 by the independent assessor, Radiologist 1.

*tu.xpt*

| Row | STUDYID | DOMAIN | USUBJID | TUSEQ | TULNKID | TUTESTCD | TUTEST | TUORRES | TUSTRESC | TULOC | TULAT | TUMETHOD | TUNAM | TUEVAL | TUEVALID | VISITNUM | VISIT | TUDTC | TUDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | TU | 55555 | 1 | R1-T01 | TUMIDENT | Tumor Identification | TARGET | TARGET | CERVICAL LYMPH NODE | LEFT | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-02 | -2 |
| 2 | ABC | TU | 55555 | 2 | R1-T02 | TUMIDENT | Tumor Identification | TARGET | TARGET | LIVER |  | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 | -3 |
| 3 | ABC | TU | 55555 | 3 | R1-T03 | TUMIDENT | Tumor Identification | TARGET | TARGET | THYROID GLAND | RIGHT | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 | -3 |
| 4 | ABC | TU | 55555 | 4 | R1-NT01 | TUMIDENT | Tumor Identification | NON-TARGET | NON-TARGET | KIDNEY | RIGHT | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 | -3 |
| 5 | ABC | TU | 55555 | 5 | R1-NT02 | TUMIDENT | Tumor Identification | NON-TARGET | NON-TARGET | CEREBELLUM | RIGHT | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-02 | -2 |
| 6 | ABC | TU | 55555 | 6 | R1-NEW01 | TUMIDENT | Tumor Identification | NEW | NEW | LUNG |  | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-20 | 48 |
| 7 | ABC | TU | 55555 | 7 | R1-NEW02 | TUMIDENT | Tumor Identification | NEW | NEW | CEREBELLUM | LEFT | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 88 |

TR shows assessments provided by an independent assessor as opposed to the principal investigator.

**Rows 1-7:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the screening visit by the independent assessor, Radiologist 1.

**Rows 8-19:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 6 visit by the independent assessor, Radiologist 1.

**Rows 20-32:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 12 visit by the independent assessor, Radiologist 1.

*tr.xpt*

| Row | STUDYID | DOMAIN | USUBJID | TRSEQ | TRGRPID | TRLNKGRP | TRLNKID | TRTESTCD | TRTEST | TRORRES | TRORRESU | TRSTRESC | TRSTRESN | TRSTRESU | TRNAM | TRMETHOD | TREVAL | TREVALID | VISITNUM | VISIT | TRDTC | TRDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | TR | 55555 | 1 | TARGET | A1 | R1-T01 | DIAMETER | Diameter | 20 | mm | 20 | 20 | mm | ACE IMAGING | MRI | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-02 | -2 |
| 2 | ABC | TR | 55555 | 2 | TARGET | A1 | R1-T02 | DIAMETER | Diameter | 15 | mm | 15 | 15 | mm | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 | -3 |
| 3 | ABC | TR | 55555 | 3 | TARGET | A1 | R1-T03 | DIAMETER | Diameter | 15 | mm | 15 | 15 | mm | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 | -3 |
| 4 | ABC | TR | 55555 | 4 | TARGET | A1 |  | SUMDIAM | Sum of Diameter | 50 | mm | 50 | 50 | mm | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN |  |  |
| 5 | ABC | TR | 55555 | 5 | TARGET | A1 |  | SUMNLNLD | Sum Diameters of Non Lymph Node Tumors | 30 | mm | 30 | 30 | mm | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN |  |  |
| 6 | ABC | TR | 55555 | 6 | NON-TARGET | A1 | R1-NT01 | TUMSTATE | Tumor State | PRESENT |  | PRESENT |  |  | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-02 | -2 |
| 7 | ABC | TR | 55555 | 7 | NON-TARGET | A1 | R1-NT02 | TUMSTATE | Tumor State | PRESENT |  | PRESENT |  |  | ACE IMAGING | MRI | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-04 | 1 |
| 8 | ABC | TR | 55555 | 8 | TARGET | A2 | R1-T01 | DIAMETER | Diameter | 12 | mm | 12 | 12 | mm | ACE IMAGING | MRI | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-18 | 46 |
| 9 | ABC | TR | 55555 | 9 | TARGET | A2 | R1-T02 | DIAMETER | Diameter | 0 | mm | 0 | 0 | mm | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-19 | 47 |
| 10 | ABC | TR | 55555 | 10 | TARGET | A2 | R1-T03 | DIAMETER | Diameter | 13 | mm | 13 | 13 | mm | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-19 | 47 |
| 11 | ABC | TR | 55555 | 11 | TARGET | A2 |  | SUMDIAM | Sum of Diameter | 25 | mm | 25 | 25 | mm | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 |  |  |
| 12 | ABC | TR | 55555 | 12 | TARGET | A2 |  | SUMNLNLD | Sum Diameters of Non Lymph Node Tumors | 13 | mm | 13 | 13 | mm | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 |  |  |
| 13 | ABC | TR | 55555 | 13 | TARGET | A2 |  | LNSTATE | Lymph Nodes State | PATHOLOGICAL |  | PATHOLOGICAL |  |  | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 |  |  |
| 14 | ABC | TR | 55555 | 14 | TARGET | A2 |  | ACNSD | Absolute Change From Nadir in Sum of Diameters | -25 | mm | -25 | -25 | mm | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 |  |  |
| 15 | ABC | TR | 55555 | 15 | TARGET | A2 |  | PCBSD | Percent Change From Baseline in Sum of Diameters | -50 | % | -60 | -50 | % | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 |  |  |
| 16 | ABC | TR | 55555 | 16 | TARGET | A2 |  | PCNSD | Percent Change From Nadir in Sum of Diameters | -50 | % | -50 | -50 | % | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 |  |  |
| 17 | ABC | TR | 55555 | 17 | NON-TARGET | A2 | R1-NT01 | TUMSTATE | Tumor State | ABSENT |  | ABSENT |  |  | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-19 | 47 |
| 18 | ABC | TR | 55555 | 18 | NON-TARGET | A2 | R1-NT02 | TUMSTATE | Tumor State | ABSENT |  | ABSENT |  |  | ACE IMAGING | MRI | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-18 | 46 |
| 19 | ABC | TR | 55555 | 19 | NEW | A2 | R1-NEW01 | TUMSTATE | Tumor State | EQUIVOCAL |  | EQUIVOCAL |  |  | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-18 | 46 |
| 20 | ABC | TR | 55555 | 20 | TARGET | A3 | R1-T01 | DIAMETER | Diameter | 7 | mm | 7 | 7 | mm | ACE IMAGING | MRI | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 88 |
| 21 | ABC | TR | 55555 | 21 | TARGET | A3 | R1-T02 | DIAMETER | Diameter | 20 | mm | 20 | 20 | mm | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 88 |
| 22 | ABC | TR | 55555 | 22 | TARGET | A3 | R1-T03 | DIAMETER | Diameter | 10 | mm | 10 | 10 | mm | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 88 |
| 23 | ABC | TR | 55555 | 23 | TARGET | A3 |  | SUMDIAM | Sum of Diameter | 37 | mm | 37 | 37 | mm | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 |  |  |
| 24 | ABC | TR | 55555 | 24 | TARGET | A3 |  | SUMNLNLD | Sum Diameters of Non Lymph Node Tumors | 30 | mm | 30 | 30 | mm | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 |  |  |
| 25 | ABC | TR | 55555 | 25 | TARGET | A3 |  | LNSTATE | Lymph Nodes State | NONPATHOLOGICAL |  | NONPATHOLOGICAL |  |  | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 |  |  |
| 26 | ABC | TR | 55555 | 26 | TARGET | A3 |  | ACNSD | Absolute Change Nadir in Sum of Diam | 17 | mm | 17 | 17 | mm | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 |  |  |
| 27 | ABC | TR | 55555 | 27 | TARGET | A3 |  | PCBSD | Percent Change Baseline in Sum of Diam | -26 | % | -26 | -26 | % | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 |  |  |
| 28 | ABC | TR | 55555 | 28 | TARGET | A3 |  | PCNSD | Percent Change Nadir in Sum of Diam | 48 | % | 48 | 48 | % | ACE IMAGING |  | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 |  |  |
| 29 | ABC | TR | 55555 | 29 | NON-TARGET | A3 | R1-NT01 | TUMSTATE | Tumor State | ABSENT |  | ABSENT |  |  | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 88 |
| 30 | ABC | TR | 55555 | 30 | NON-TARGET | A3 | R1-NT02 | TUMSTATE | Tumor State | ABSENT |  | ABSENT |  |  | ACE IMAGING | MRI | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 88 |
| 31 | ABC | TR | 55555 | 31 | NEW | A3 | R1-NEW01 | TUMSTATE | Tumor State | EQUIVOCAL |  | EQUIVOCAL |  |  | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 88 |
| 32 | ABC | TR | 55555 | 32 | NEW | A3 | R1-NEW02 | TUMSTATE | Tumor State | UNEQUIVOCAL |  | UNEQUIVOCAL |  |  | ACE IMAGING | MRI | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 88 |

The relationship between the TU and TR records is represented in RELREC.

*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | TU |  | TULNKID |  | ONE | 1 |
| 2 | ABC | TR |  | TRLNKID |  | MANY | 1 |

---
### 6.3.13 Vital Signs (VS)

#### VS – Description/Overview
A findings domain that contains measurements including but not limited to blood pressure, temperature, respiration, body surface area, body mass index, height and weight.

#### VS – Specification
vs.xpt, Vital Signs — Findings. One record per vital sign measurement per time point per visit per subject, Tabulation.

**Structure:** One record per vital sign measurement per time point per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | VS |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | VSSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | VSGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | VSSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 7 | VSTESTCD | Vital Signs Test Short Name | Char | Topic | Req | C66741 |
| 8 | VSTEST | Vital Signs Test Name | Char | Synonym Qualifier | Req | C67153 |
| 9 | VSCAT | Category for Vital Signs | Char | Grouping Qualifier | Perm |  |
| 10 | VSSCAT | Subcategory for Vital Signs | Char | Grouping Qualifier | Perm |  |
| 11 | VSPOS | Vital Signs Position of Subject | Char | Record Qualifier | Perm | C71148 |
| 12 | VSORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 13 | VSORRESU | Original Units | Char | Variable Qualifier | Exp | C66770 |
| 14 | VSSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 15 | VSSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |
| 16 | VSSTRESU | Standard Units | Char | Variable Qualifier | Exp | C66770 |
| 17 | VSSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 18 | VSREASND | Reason Not Performed | Char | Record Qualifier | Perm |  |
| 19 | VSLOC | Location of Vital Signs Measurement | Char | Record Qualifier | Perm | C74456 |
| 20 | VSLAT | Laterality | Char | Result Qualifier | Perm | C99073 |
| 21 | VSLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 22 | VSBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 23 | VSDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 24 | VSTOX | Toxicity | Char | Variable Qualifier | Perm |  |
| 25 | VSTOXGR | Standard Toxicity Grade | Char | Record Qualifier | Perm |  |
| 26 | VSCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |
| 27 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 28 | VISIT | Visit Name | Char | Timing | Perm |  |
| 29 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 30 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 31 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 32 | VSDTC | Date/Time of Measurements | Char | Timing | Exp | ISO 8601 datetime or interval |
| 33 | VSDY | Study Day of Vital Signs | Num | Timing | Perm |  |
| 34 | VSTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 35 | VSTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 36 | VSELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 37 | VSTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 38 | VSRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **VSSEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **VSGRPID**: Used to tie together a block of related records in a single domain for a subject.
- **VSSPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.
- **VSTESTCD**: Short name of the measurement, test, or examination described in VSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in VSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). VSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SYSBP", "DIABP", "BMI".
- **VSTEST**: Verbatim name of the test or examination used to obtain the measurement or finding. The value in VSTEST cannot be longer than 40 characters. Examples: "Systolic Blood Pressure", "Diastolic Blood Pressure", "Body Mass Index".
- **VSCAT**: Used to define a category of related records.
- **VSSCAT**: A further categorization of a measurement or examination.
- **VSPOS**: Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".
- **VSORRES**: Result of the vital signs measurement as originally received or collected.
- **VSORRESU**: Original units in which the data were collected. The unit for VSORRES. Examples: "in", "LB", "beats/min".
- **VSSTRESC**: Contains the result value for all findings, copied or derived from VSORRES in a standard format or standard units. VSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in VSSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in VSORRES, and these results effectively have the same meaning, they could be represented in standard format in VSSTRESC as "NEGATIVE".
- **VSSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from VSSTRESC. VSSTRESN should store all numeric test results or findings.
- **VSSTRESU**: Standardized unit used for VSSTRESC and VSSTRESN.
- **VSSTAT**: Used to indicate that a vital sign measurement was not done. Should be null if a result exists in VSORRES.
- **VSREASND**: Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with VSSTAT when value is "NOT DONE".
- **VSLOC**: Location relevant to the collection of vital signs measurement. Example: "ARM" for blood pressure.
- **VSLAT**: Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".
- **VSLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.
- **VSBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that VSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **VSDRVFL**: Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records or that do not come from the CRF are examples of records that would be derived for the submission datasets. If VSDRVFL = "Y," then VSORRES may be null, with VSSTRESC and (if numeric) VSSTRESN having the derived value.
- **VSTOX**: Description of toxicity quantified by VSTOXGR. The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.
- **VSTOXGR**: Records toxicity grade value using a standard toxicity scale (e.g., NCI CTCAE). If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2"). The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.
- **VSCLSIG**: Used to indicate whether a collected observation is clinically significant based on judgment.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm.
- **EPOCH**: Epoch associated with the start date/time at which the assessment was made.
- **VSDTC**: Date and time of the vital signs assessment represented in ISO 8601 character format.
- **VSDY**: Study day of vital signs measurements, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
- **VSTPT**: Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See VSTPTNUM and VSTPTREF. Examples: "START", "5 MIN POST".
- **VSTPTNUM**: Numerical version of VSTPT to aid in sorting.
- **VSELTM**: Planned elapsed time (in ISO 8601) relative to a planned fixed reference (VSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 Duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by VSTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by VSTPTREF.
- **VSTPTREF**: Name of the fixed reference point referred to by VSELTM, VSTPTNUM, and VSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **VSRFTDTC**: Date/time of the reference time point, VSTPTREF.


#### VS – Assumptions

1. In cases where the LOINC dictionary is used for vital sign tests, the permissible variable VSLOINC may be used. Sponsors are expected to provide the dictionary name and version used to map terms using the external codelist element in the Define-XML document.
2. If a reference range is available for a vital signs test, the variables VSORNRLO, VSORNRHI, VSNRIND from the Findings observation class may be added to the domain. VSORNRLO and VSORNRHI would represent the reference range, and VSNRIND would be used to indicate where a result falls with respect to the reference range (e.g., "HIGH", "LOW"). If toxicity grading is available, values would be represented in the variables VSTOX and VSTOXGR. Clinical significance would be represented in VSCLSIG, as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data.
3. Associations between some vital sign tests and qualifier codelists are described in the VS codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.
4. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the VS domain, but the following qualifiers would not generally be used: --BODSYS, --XFN, --SPEC, --SPCCND, --FAST.

#### VS – Examples

**Example 1**
This example shows results for 1 subject from 2 visits (i.e., baseline, visit 2).
**Rows 1-4, 6-7:** VSTPT and VSTPTNUM are populated because more than 1 measurement was taken at this visit.
**Rows 2, 4-5, 7-9:** VSLOBXFL="Y" indicates that the observation was used as the last observation before exposure measurement.
**Rows 10-11:** Show blood pressure observations obtained at visit 2.
**Row 12:** Shows a value collected in one unit, but converted to selected standard unit.
**Row 13:** Shows the proper use of the --STAT variable to indicate "NOT DONE" where a reason was collected when a test was not done.

*vs.xpt*

| Row | STUDYID | DOMAIN | USUBJID | VSSEQ | VSTESTCD | VSTEST | VSPOS | VSORRES | VSORRESU | VSSTRESC | VSSTRESN | VSSTRESU | VSSTAT | VSREASND | VSLOC | VSLAT | VSLOBXFL | VISITNUM | VISIT | VISITDY | VSDTC | VSDY | VSTPT | VSTPTNUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | VS | ABC-001-001 | 1 | SYSBP | Systolic Blood Pressure | SITTING | 154 | mmHg | 154 | 154 | mmHg |  |  | ARM | LEFT |  | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE 1 | 1 |
| 2 | ABC | VS | ABC-001-001 | 2 | SYSBP | Systolic Blood Pressure | SITTING | 152 | mmHg | 152 | 152 | mmHg |  |  | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE 2 | 2 |
| 3 | ABC | VS | ABC-001-001 | 3 | DIABP | Diastolic Blood Pressure | SITTING | 44 | mmHg | 44 | 44 | mmHg |  |  | ARM | LEFT |  | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE 1 | 1 |
| 4 | ABC | VS | ABC-001-001 | 4 | DIABP | Diastolic Blood Pressure | SITTING | 48 | mmHg | 48 | 48 | mmHg |  |  | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE 2 | 2 |
| 5 | ABC | VS | ABC-001-001 | 5 | PULSE | Pulse Rate | SITTING | 72 | beats/min | 72 | 72 | beats/min |  |  | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19 | 1 |  |  |
| 6 | ABC | VS | ABC-001-001 | 6 | TEMP | Temperature |  | 34.7 | C | 34.7 | 34.7 | C |  |  | SUBLINGUAL REGION |  |  | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE 1 | 1 |
| 7 | ABC | VS | ABC-001-001 | 7 | TEMP | Temperature |  | 36.2 | C | 36.2 | 36.2 | C |  |  | SUBLINGUAL REGION |  | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE 2 | 2 |
| 8 | ABC | VS | ABC-001-001 | 8 | WEIGHT | Weight | STANDING | 90.5 | kg | 90.5 | 90.5 | kg |  |  |  |  | Y | 1 | Baseline | 1 | 1999-06-19 | 1 |  |  |
| 9 | ABC | VS | ABC-001-001 | 9 | HEIGHT | Height | STANDING | 157 | cm | 157 | 157 | cm |  |  |  |  | Y | 1 | Baseline | 1 | 1999-06-19 | 1 |  |  |
| 10 | ABC | VS | ABC-001-001 | 10 | SYSBP | Systolic Blood Pressure | SITTING | 95 | mmHg | 95 | 95 | mmHg |  |  | ARM | LEFT |  | 2 | Visit 2 | 35 | 1999-07-21 | 33 |  |  |
| 11 | ABC | VS | ABC-001-001 | 11 | DIABP | Diastolic Blood Pressure | SITTING | 44 | mmHg | 44 | 44 | mmHg |  |  | ARM | LEFT |  | 2 | Visit 2 | 35 | 1999-07-21 | 33 |  |  |
| 12 | ABC | VS | ABC-001-001 | 12 | TEMP | Temperature |  | 97.16 | F | 36.2 | 36.2 | C |  |  | SUBLINGUAL REGION |  |  | 2 | Visit 2 | 35 | 1999-07-21 | 33 |  |  |
| 13 | ABC | VS | ABC-001-001 | 13 | WEIGHT | Weight |  |  |  |  |  |  | NOT DONE | SUBJECT REFUSED |  |  |  | 2 | Visit 2 | 35 | 1999-07-21 | 33 |  |  |
