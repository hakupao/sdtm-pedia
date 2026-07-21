# SDTMIG v3.4 --- Domain Models: Findings — Part 6

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 6/8 — 6.3.6-6.3.7: MO, Morphology/Physiology Domains
> **Original:** `SDTMIG34_06_DomainModels_Findings.md`
> **Related:** `SDTMIG34_06a_DomainModels_Findings.md`, `SDTMIG34_06b_DomainModels_Findings.md`, `SDTMIG34_06c_DomainModels_Findings.md`, `SDTMIG34_06d_DomainModels_Findings.md`, `SDTMIG34_06e_DomainModels_Findings.md`, `SDTMIG34_06g_DomainModels_Findings.md`, `SDTMIG34_06h_DomainModels_Findings.md`

---

### 6.3.6 Morphology (MO)

**Domain Decommissioning Update**

The MO domain has been decommissioned as of SDTMIG v3.4.

When the Morphology domain was introduced in SDTMIG v3.2, the SDS Team planned to represent morphology and physiology findings in separate domains: morphology findings in the MO domain and physiology findings in separate domains by body systems. Since then, the team found that separating morphology and physiology findings was more difficult than anticipated and provided little added value. This led to the decision to expand the body system-based domains to cover both morphology and physiology findings and to deprecate MO in a future version of the SDTMIG. Submissions using that later SDTMIG version would represent morphology results in the appropriate body system-based physiology/morphology domain.

For data prepared using a version of the SDTMIG that includes both the MO domain and body system-based physiology/morphology domains, morphology findings may be represented in either the MO domain or in a body-system based physiology/morphology domain. Custom body system-based domains may be used if the appropriate body system-based domain is not included in the SDTMIG version being used.

---

### 6.3.7 Morphology/Physiology Domains

Individual domains for morphology and physiology findings about specific body systems are grouped together in this section. This grouping is not meant to imply that there is a single morphology/physiology domain. Additional domains for other body systems are expected to be added in future versions of the SDTMIG. The CDISC Controlled Terminology of SDTM domain abbreviations and the therapeutic area user guides may have examples of other body system domains that are not yet in the SDTMIG.

#### 6.3.7.1 Generic Morphology/Physiology Specification

This section describes properties common to all the body system-based morphology/physiology domains.
- The SDTMIG includes several domains for physiology and morphology findings for different body systems. These differ only in body system, in domain code, and in informative content such as examples.
- In the partial generic domain specification table, "--" is used as a placeholder. In each individual body system-based morphology/physiology domain specification, this placeholder is replaced by the appropriate domain code.
- The variables included in the generic morphology/physiology domain specification table are those required or expected in the individual body system-based morphology/physiology domains. Individual morphology/physiology domains may included additional expected variables. All other variables allowed in findings domains are allowed in the body system-based morphology/physiology domains
- All body system-based physiology/morphology domains share the same structure, provided here. Although time point is not in the structure, it can be included in the structure of a particular domain if time point variables were included in the data represented.
- CDISC Controlled Terminology includes codelists for TEST and TESTCD values for each body-system based domain.

##### Generic Morphology/Physiology – Specification
--.xpt, Body System-Based Morphology/Physiology -- Findings, Version 3.3. One record per finding per visit per subject, Tabulation.

**Structure:** One record per finding per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | -- |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | --SEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | --TESTCD | Short Name of Measurement, Test or Exam | Char | Topic | Req | * |
| 6 | --TEST | Name of Measurement, Test or Examination | Char | Synonym Qualifier | Req | * |
| 7 | --ORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 8 | --STRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |
| 9 | --LOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp |  |
| 10 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 11 | --DTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 12 | --DY | Study Day of Collection | Num | Timing | Exp |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **--SEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1.
- **--TESTCD**: Short character value for --TEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Subject to Domain-specific test code controlled terminology.
- **--TEST**: Long name for --TESTCD. Subject to Domain-specific test code controlled terminology.
- **--ORRES**: Result of the measurement or finding as originally received or collected.
- **--STRESC**: Contains the result value for all findings, copied or derived from --ORRES in a standard format or in standard units. --STRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in --STRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in --ORRES, and these results effectively have the same meaning, they could be represented in standard format in --STRESC as "NEGATIVE".
- **--LOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **--DTC**: Collection date and time of an observation.
- **--DY**: Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.


#### 6.3.7.2 Cardiovascular System Findings (CV)

##### CV – Description/Overview
A findings domain that contains physiological and morphological findings related to the cardiovascular system, including the heart, blood vessels and lymphatic vessels.

##### CV – Specification
cv.xpt, Cardiovascular System Findings — Findings. One record per finding or result per time point per visit per subject, Tabulation.

**Structure:** One record per finding or result per time point per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | CV |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | CVSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | CVGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | CVREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | CVSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | CVLNKID | Link ID | Char | Identifier | Perm |  |
| 9 | CVLNKGRP | Link Group | Char | Identifier | Perm |  |
| 10 | CVTESTCD | Short Name of Cardiovascular Test | Char | Topic | Req | C101847 |
| 11 | CVTEST | Name of Cardiovascular Test | Char | Synonym Qualifier | Req | C101846 |
| 12 | CVCAT | Category for Cardiovascular Test | Char | Grouping Qualifier | Perm |  |
| 13 | CVSCAT | Subcategory for Cardiovascular Test | Char | Grouping Qualifier | Perm |  |
| 14 | CVPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |
| 15 | CVORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 16 | CVORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 17 | CVSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 18 | CVSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 19 | CVSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 20 | CVSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 21 | CVREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 22 | CVLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |
| 23 | CVLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| 24 | CVDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| 25 | CVMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 26 | CVLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 27 | CVBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 28 | CVDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 29 | CVEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 30 | CVEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 36 | CVDTC | Date/Time of Test | Char | Timing | Exp | ISO 8601 datetime or interval |
| 37 | CVDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |
| 38 | CVTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 39 | CVTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 40 | CVELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 41 | CVTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 42 | CVRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **CVSEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.
- **CVGRPID**: Optional group identifier, used to link together a block of related records within a subject in a domain.
- **CVREFID**: Optional internal or external identifier.
- **CVSPID**: Sponsor-defined identifier. Example: a preprinted line identifier on a CRF.
- **CVLNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.
- **CVLNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **CVTESTCD**: Short name of the measurement, test, or examination described in CVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" would not be valid). CVTESTCD cannot contain characters other than letters, numbers, or underscores.
- **CVTEST**: Long name For CVTESTCD. The value in CVTEST cannot be longer than 40 characters.
- **CVCAT**: Used to define a category of topic-variable values.
- **CVSCAT**: Used to define a further categorization of CVCAT values.
- **CVPOS**: Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".
- **CVORRES**: Result of the measurement or finding as originally received or collected.
- **CVORRESU**: Original units in which the data were collected. Unit for CVORRES.
- **CVSTRESC**: Contains the result value for all findings, copied or derived, from CVORRES in a standard format or in standard units. CVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CVSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in CVORRES and these results effectively have the same meaning, they could be represented in standard format in CVSTRESC as "NEGATIVE".
- **CVSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from CVSTRESC. CVSTRESN should store all numeric test results or findings.
- **CVSTRESU**: Standardized units used for CVSTRESC and CVSTRESN.
- **CVSTAT**: Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".
- **CVREASND**: Describes why a measurement or test was not performed (e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED"). Used in conjunction with CVSTAT when value is "NOT DONE".
- **CVLOC**: Anatomical location of the subject relevant to the collection of the measurement. Examples: "HEART", "LEFT VENTRICLE".
- **CVLAT**: Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL", "UNILATERAL".
- **CVDIR**: Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".
- **CVMETHOD**: Method used to create the result.
- **CVLOBXFL**: Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **CVBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that CVBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **CVDRVFL**: Used to indicate a derived record (i.e., a record that represents the average of other records, such as a computed baseline). Should be "Y" or null.
- **CVEVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", " INDEPENDENT ASSESSOR", "RADIOLOGIST".
- **CVEVALID**: Used to distinguish multiple evaluators with the same role recorded in CVEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2".
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of VISIT. Should be an integer.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the date/time at which the assessment was made.
- **CVDTC**: Collection date and time of an observation.
- **CVDY**: Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **CVTPT**: Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See CVTPTNUM and CVTPTREF.
- **CVTPTNUM**: Numeric version of planned time point used in sorting.
- **CVELTM**: Planned elapsed time relative to a planned fixed reference (CVTPTREF). Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.
- **CVTPTREF**: Description of the fixed reference point referred to by CVELTM, CVTPTNUM, and CVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **CVRFTDTC**: Date/time for a fixed reference time point defined by CVTPTREF.


##### CV – Assumptions
1. The Cardiovascular System Findings domain is used to represent results and findings of cardiovascular diagnostic procedures. Information about the conduct of the procedure(s), if collected, is submitted in the Procedures (PR) domain.
2. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the CV domain, but the following qualifiers would generally not be used: --MODIFY, --BODSYS, --FAST, --ORNRLO, --ORNRHI, --TNRLO, --STNRHI, and --LOINC.


##### CV – Examples

**Example 1**
This example shows various findings related to the aortic artery, along with evaluation for the presence or absence of abdominal aortic aneurysms. The suprarenal, infrarenal, and thoracic sections of the aorta were examined for aneurysms. This level of anatomical location detail can be found in CVLOC. The records in rows 1 to 3 are related assessments regarding an aneurysm in the thoracic aorta and are grouped together using the CVGRPID variable. cv.xpt

| Row | STUDYID | DOMAIN | USUBJID | CVSEQ | CVGRPID | CVTESTCD | CVTEST | CVORRES | CVSTRESC | CVLOC | CVMETHOD | VISITNUM | VISIT | CVDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | CV | 002-2004 | 1 | 2 | ANEURIND | Aneurysm Indicator | Y | Y | THORACIC AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 2 | ABC123 | CV | 002-2004 | 2 | 2 | DISECIND | Dissection Indicator | Y | Y | THORACIC AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 3 | ABC123 | CV | 002-2004 | 3 | 2 | STANFADC | Stanford AoD Classification | CLASS A | CLASS A | THORACIC AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 4 | ABC123 | CV | 002-2004 | 4 |  | ANEURIND | Aneurysm Indicator | N | N | SUPRARENAL AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 5 | ABC123 | CV | 002-2004 | 5 |  | ANEURIND | Aneurysm Indicator | N | N | INFRARENAL AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |

**Example 2**
In this example CVTEST represents the structure of the aortic valve evaluated during a transthoracic echocardiography procedure. cv.xpt

| Row | STUDYID | DOMAIN | USUBJID | CVSEQ | CVTESTCD | CVTEST | CVCAT | CVORRES | CVORRESU | CVSTRESC | CVSTRESN | CVSTRESU | CVLOC | CVMETHOD | VISITNUM | VISIT | CVDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | CV | 1001 | 1 | NCVALTYP | Native Cardiac Valve Intervention Type | VALVULAR STRUCTURE, COMMON | NATIVE, WITHOUT INTERVENTION |  | NATIVE, WITHOUT INTERVENTION |  |  | AORTIC VALVE | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 2 | ABC123 | CV | 1001 | 2 | SIZE | Size | VALVULAR STRUCTURE, COMMON | REDUCED |  | REDUCED |  |  | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 3 | ABC123 | CV | 1001 | 3 | MNDIAEVS | Minor Axis Cross-sec Diameter, EVS | VALVULAR STRUCTURE, COMMON | 2.18 | cm | 2.18 | 2.18 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 4 | ABC123 | CV | 1001 | 4 | MJDIAEVS | Major Axis Cross-sec Diameter, EVS | VALVULAR STRUCTURE, COMMON | 2.48 | cm | 2.48 | 2.48 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 5 | ABC123 | CV | 1001 | 5 | MNDIAEVD | Minor Axis Cross-sec Diameter, EVD | VALVULAR STRUCTURE, COMMON | 1.92 | cm | 1.92 | 1.92 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 6 | ABC123 | CV | 1001 | 6 | MJDIAEVD | Major Axis Cross-sec Diameter, EVD | VALVULAR STRUCTURE, COMMON | 2.58 | cm | 2.58 | 2.58 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 7 | ABC123 | CV | 1001 | 7 | MNDIAMVS | Minor Axis Cross-sec. Diameter, MVS | VALVULAR STRUCTURE, COMMON | 2.11 | cm | 2.11 | 2.11 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 8 | ABC123 | CV | 1001 | 8 | MJDIAMVS | Major Axis Cross-sec. Diameter, MVS | VALVULAR STRUCTURE, COMMON | 2.39 | cm | 2.39 | 2.39 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |

#### 6.3.7.3 Musculoskeletal System Findings (MK)

##### MK – Description/Overview
A findings domain that contains physiological and morphological findings related to the system of muscles, tendons, ligaments, bones, joints, and associated tissues.

##### MK – Specification
mk.xpt, Musculoskeletal System Findings — Findings. One record per assessment per visit per subject, Tabulation.

**Structure:** One record per assessment per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | MK |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | MKSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | MKGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | MKREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | MKSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | MKLNKID | Link ID | Char | Identifier | Perm |  |
| 9 | MKLNKGRP | Link Group ID | Char | Identifier | Perm |  |
| 10 | MKTESTCD | Short Name of Musculoskeletal Test | Char | Topic | Req | C127269 |
| 11 | MKTEST | Name of Musculoskeletal Test | Char | Synonym Qualifier | Req | C127270 |
| 12 | MKCAT | Category for Musculoskeletal Test | Char | Grouping Qualifier | Perm |  |
| 13 | MKSCAT | Subcategory for Musculoskeletal Test | Char | Grouping Qualifier | Perm |  |
| 14 | MKPOS | Position of Subject | Char | Record Qualifier | Perm | C71148 |
| 15 | MKORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 16 | MKORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 17 | MKSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 18 | MKSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 19 | MKSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 20 | MKSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 21 | MKREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 22 | MKLOC | Location Used for the Measurement | Char | Record Qualifier | Exp | C74456 |
| 23 | MKLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| 24 | MKDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| 25 | MKMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 26 | MKLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 27 | MKBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 28 | MKDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 29 | MKEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 30 | MKEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 36 | MKDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 37 | MKDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |
| 38 | MKTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 39 | MKTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 40 | MKELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 41 | MKTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 42 | MKRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **MKSEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1.
- **MKGRPID**: Used to link together a block of related records within a subject in a domain.
- **MKREFID**: Optional internal or external identifier such as lab specimen ID or a medical image.
- **MKSPID**: Sponsor-defined identifier. Example: Preprinted line identifier on a Concomitant Medications page.
- **MKLNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.
- **MKLNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **MKTESTCD**: Short character value for MKTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The value in MKTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MKTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TNDRIND", "SWLLIND", "SGJSNSCR".
- **MKTEST**: Long name For MKTESTCD. Examples: "Tenderness Indicator", "Swollen Indicator", "Sharp/Genant JSN Score".
- **MKCAT**: Used to define a category of topic-variable values. Examples: "SWOLLEN/TENDER JOINT ASSESSMENT".
- **MKSCAT**: Used to define a further categorization of MKCAT values.
- **MKPOS**: Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".
- **MKORRES**: Result of the measurement or finding as originally received or collected.
- **MKORRESU**: Unit for MKORRES.
- **MKSTRESC**: Contains the result value for all findings, copied or derived from MKORRES in a standard format or in standard units. MKSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MKSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in MKORRES and these results effectively have the same meaning, they could be represented in standard format in MKSTRESC as "NEGATIVE".
- **MKSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from MKSTRESC. MKSTRESN should store all numeric test results or findings.
- **MKSTRESU**: Standardized units used for MKSTRESC and MKSTRESN.
- **MKSTAT**: Used to indicate that a question was not asked or a test was not done, or that a test was attempted but did not generate a result. Should be null if a result exists in MKORRES.
- **MKREASND**: Reason not done. Used in conjunction with MKSTAT when value is "NOT DONE".
- **MKLOC**: Anatomical location of the subject relevant to the collection of the measurement. Examples: "INTERPHALANGEAL JOINT 1", "SHOULDER JOINT".
- **MKLAT**: Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".
- **MKDIR**: Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".
- **MKMETHOD**: Method of the test or examination. Examples: "X-RAY", "MRI", "CT SCAN".
- **MKLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **MKBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that MKBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **MKDRVFL**: Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.
- **MKEVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".
- **MKEVALID**: Used to distinguish multiple evaluators with the same role recorded in MKEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2".
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter.
- **VISITDY**: Planned study day of VISIT. Should be an integer.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the date/time at which the assessment was made.
- **MKDTC**: Collection date and time of an observation.
- **MKDY**: Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **MKTPT**: Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See MKTPTNUM and MKTPTREF.
- **MKTPTNUM**: Numeric version of planned time point used in sorting.
- **MKELTM**: Planned Elapsed time relative to a planned fixed reference (MKTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.
- **MKTPTREF**: Description of the fixed reference point referred to by MKELTM, MKTPTNUM, and MKTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **MKRFTDTC**: Date/time for a fixed reference time point defined by MKTPTREF.


##### MK – Assumptions
1. The Musculoskeletal System Findings domain should not be used for oncology data related to the musculoskeletal system (e.g., bone lesions). Such data should be placed in the appropriate oncology domains: Tumor/Lesion Identification (TU), Tumor/Lesion Results (TR), and/or Disease Response and Clinical Classification (RS).
2. Musculoskeletal assessment examples that may have results represented in the MK domain include the following: morphology/physiology observations (e.g., swollen/tender joint count, limb movement, strength/grip measurements).
3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MK domain, but the following qualifiers would generally not be used: --MODIFY, --BODSYS, --LOINC, --TOX, --TOXGR, --FAST, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --ORREF, --STREFC, --STREFN.

##### MK – Examples

**Example 1**
This example illustrates data collected for the swollen/tender joint count assessment, specifically the 68-joint count.
After determining whether each joint is swollen or tender, the assessor will add up the number of "Yes" responses for swollen joints and tender joints to obtain a total count for each. Total counts were not collected on the CRF since they were to be derived in ADaM datasets. Data collection included a field for marking a joint not evaluable when that joint met a condition (e.g., infection of the overlying tissue or skin, grossly edematous, fused), which precluded joint assessment, as specified by the protocol and the protocol-related joint assessor training. A field for the reason that a joint was not evaluable was not needed. Note that there was a field for marking a joint assessment as not done; this was to be used if the joint assessor overlooked or missed a joint while performing the joint assessment.
The data collected are represented in the MK domain. Each joint location is specified in MKLOC with laterality ("RIGHT" or "LEFT") in MKLAT. Because the evaluation includes a large number of joints that would result in many records, only a subset of the data collected is shown below.
Rows 1-8, 11-12, 15-16: Show the occurrence of tenderness or swelling (MKORRES/MKSTRESC="Y", "N") at specific joint locations, represented in MKLOC, on the right and left sides (MKLAT) of the body.
**Rows 9-10:** Show that the assessments for tenderness and swelling of the acromioclavicular joint (see MKLOC) on the right side of the body was not performed (MKSTAT="NOT DONE"), but a specific reason was not collected on the CRF.
**Rows 13-14:** Show that the assessments for tenderness and swelling of the shoulder joint (see MKLOC) on the right side of the body was not performed (MKSTAT="NOT DONE") because it was not evaluable (MKREASND="JOINT NOT EVALUABLE").


*mk.xpt*

| Row | STUDYID | DOMAIN | USUBJID | MKSEQ | MKTESTCD | MKTEST | MKORRES | MKSTRESC | MKSTRESN | MKSTAT | MKREASND | MKLOC | MKLAT | MKMETHOD | VISITNUM | VISIT | MKDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DEF | MK | DEF-138 | 1 | TNDRIND | Tenderness Indicator | Y | Y |  |  |  | TEMPOROMANDIBULAR JOINT | RIGHT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 2 | DEF | MK | DEF-138 | 2 | SWLLIND | Swollen Indicator | Y | Y |  |  |  | TEMPOROMANDIBULAR JOINT | RIGHT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 3 | DEF | MK | DEF-138 | 3 | TNDRIND | Tenderness Indicator | N | N |  |  |  | TEMPOROMANDIBULAR JOINT | LEFT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 4 | DEF | MK | DEF-138 | 4 | SWLLIND | Swollen Indicator | N | N |  |  |  | TEMPOROMANDIBULAR JOINT | LEFT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 5 | DEF | MK | DEF-138 | 5 | TNDRIND | Tenderness Indicator | Y | Y |  |  |  | STERNOCLAVICULAR JOINT | RIGHT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 6 | DEF | MK | DEF-138 | 6 | SWLLIND | Swollen Indicator | N | N |  |  |  | STERNOCLAVICULAR JOINT | RIGHT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 7 | DEF | MK | DEF-138 | 7 | TNDRIND | Tenderness Indicator | Y | Y |  |  |  | STERNOCLAVICULAR JOINT | LEFT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 8 | DEF | MK | DEF-138 | 8 | SWLLIND | Swollen Indicator | Y | Y |  |  |  | STERNOCLAVICULAR JOINT | LEFT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 9 | DEF | MK | DEF-138 | 9 | TNDRIND | Tenderness Indicator |  |  |  | NOT DONE |  | ACROMIOCLAVICULAR JOINT | RIGHT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 10 | DEF | MK | DEF-138 | 10 | SWLLIND | Swollen Indicator |  |  |  | NOT DONE |  | ACROMIOCLAVICULAR JOINT | RIGHT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 11 | DEF | MK | DEF-138 | 11 | TNDRIND | Tenderness Indicator | Y | Y |  |  |  | ACROMIOCLAVICULAR JOINT | LEFT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 12 | DEF | MK | DEF-138 | 12 | SWLLIND | Swollen Indicator | Y | Y |  |  |  | ACROMIOCLAVICULAR JOINT | LEFT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 13 | DEF | MK | DEF-138 | 13 | TNDRIND | Tenderness Indicator |  |  |  | NOT DONE | JOINT NOT EVALUABLE | SHOULDER JOINT | RIGHT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 14 | DEF | MK | DEF-138 | 14 | SWLLIND | Swollen Indicator |  |  |  | NOT DONE | JOINT NOT EVALUABLE | SHOULDER JOINT | RIGHT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 15 | DEF | MK | DEF-138 | 15 | TNDRIND | Tenderness Indicator | N | N |  |  |  | SHOULDER JOINT | LEFT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |
| 16 | DEF | MK | DEF-138 | 16 | SWLLIND | Swollen Indicator | Y | Y |  |  |  | SHOULDER JOINT | LEFT | PHYSICAL EXAMINATION | 2 | WEEK 4 | 2012-09-30 |

**Example 2**
This example illustrates the collection of scores for the joint space-narrowing assessment.
There are 2 scoring methods that may be used to evaluate the joints via a radiographic image: Sharp/Genant and Sharp/van der Heijde. In this evaluation of radiographs for joint narrowing, each joint was graded. If the joint was not assessed, a reason why it was not assessed was provided.
The data collected are represented in the MK domain. In this example, the evaluation was done by a trained evaluator (MKEVAL = "INDEPENDENT ASSESSOR") from an x-ray using the Sharp/Genant method. Each image was assessed by 2 readers of the same role; in this example, MKEVALID is populated with "READER 1" because these assessments were performed by the first reader. The method used to obtain the image is represented in MKMETHOD = "X-RAY". The scoring method used for the assessment is precoordinated into MKTESTCD and MKTEST. Each joint location is specified in MKLOC with laterality ("RIGHT" or "LEFT") in MKLAT. Because the evaluation includes a large number of joints that would result in many records, only a subset of the data collected is shown here. The total score for the assessment was not collected, so is not represented in this dataset; it was to be derived in an ADaM dataset.
Rows 1-2, 4-5, 7-8, 10-11, 13-16: Show the text description of each joint space-narrowing score in MKORRES and the corresponding numeric score in MKSTRESC/MKSTRESN.
**Rows 3, 6, 9, 12:** Show data collected for joints that were not assessed (MKSTAT="NOT DONE"), with the reason collected on the CRF represented in MKREASND.

*mk.xpt*

| Row | STUDYID | DOMAIN | USUBJID | MKSEQ | MKTESTCD | MKTEST | MKORRES | MKSTRESC | MKSTRESN | MKSTAT | MKREASND | MKLOC | MKLAT | MKMETHOD | MKEVAL | MKEVALID | VISITNUM | VISIT | MKDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | MK | XYZ-002 | 1 | SGJSNSCR | Sharp/Genant JSN Score | MODERATE; 51-75% LOSS OF JOINT SPACE | 2 | 2 |  |  | INTERPHALANGEAL JOINT 1 | RIGHT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 2 | XYZ | MK | XYZ-002 | 2 | SGJSNSCR | Sharp/Genant JSN Score | MODERATE-SEVERE; 76-95% LOSS OF JOINT SPACE | 2.5 | 2.5 |  |  | INTERPHALANGEAL JOINT 1 | LEFT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 3 | XYZ | MK | XYZ-002 | 3 | SGJSNSCR | Sharp/Genant JSN Score |  |  |  | NOT DONE | AMPUTATION/MISSING ANATOMY/JOINT REPLACEMENT/SURGICAL ALTERATION | PROXIMAL INTERPHALANGEAL JOINT 2 OF THE HAND | RIGHT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 4 | XYZ | MK | XYZ-002 | 4 | SGJSNSCR | Sharp/Genant JSN Score | SEVERE; PARTIAL OR EQUIVOCAL ANKYLOSIS | 3.5 | 3.5 |  |  | PROXIMAL INTERPHALANGEAL JOINT 2 OF THE HAND | LEFT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 5 | XYZ | MK | XYZ-002 | 5 | SGJSNSCR | Sharp/Genant JSN Score | MODERATE; 51-75% LOSS OF JOINT SPACE | 2 | 2 |  |  | PROXIMAL INTERPHALANGEAL JOINT 3 OF THE HAND | RIGHT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 6 | XYZ | MK | XYZ-002 | 6 | SGJSNSCR | Sharp/Genant JSN Score |  |  |  | NOT DONE | INADEQUATE IMAGE QUALITY | PROXIMAL INTERPHALANGEAL JOINT 3 OF THE HAND | LEFT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 7 | XYZ | MK | XYZ-002 | 7 | SGJSNSCR | Sharp/Genant JSN Score | MODERATE-SEVERE; 76-95% LOSS OF JOINT SPACE | 2.5 | 2.5 |  |  | METACARPOPHALANGEAL JOINT 1 | RIGHT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 8 | XYZ | MK | XYZ-002 | 8 | SGJSNSCR | Sharp/Genant JSN Score | SEVERE; PARTIAL OR EQUIVOCAL ANKYLOSIS | 3.5 | 3.5 |  |  | METACARPOPHALANGEAL JOINT 1 | LEFT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 9 | XYZ | MK | XYZ-002 | 9 | SGJSNSCR | Sharp/Genant JSN Score |  |  |  | NOT DONE | INADEQUATE IMAGE QUALITY | METACARPOPHALANGEAL JOINT 2 | RIGHT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 10 | XYZ | MK | XYZ-002 | 10 | SGJSNSCR | Sharp/Genant JSN Score | MILD-MODERATE; 26-50% LOSS OF JOINT SPACE | 1.5 | 1.5 |  |  | METACARPOPHALANGEAL JOINT 2 | LEFT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 11 | XYZ | MK | XYZ-002 | 11 | SGJSNSCR | Sharp/Genant JSN Score | NORMAL | 0 | 0 |  |  | METACARPOPHALANGEAL JOINT 3 | RIGHT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 12 | XYZ | MK | XYZ-002 | 12 | SGJSNSCR | Sharp/Genant JSN Score |  |  |  | NOT DONE | AMPUTATION/MISSING ANATOMY/JOINT REPLACEMENT/SURGICAL ALTERATION | METACARPOPHALANGEAL JOINT 3 | LEFT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 13 | XYZ | MK | XYZ-002 | 13 | SGJSNSCR | Sharp/Genant JSN Score | SEVERE; COMPLETE LOSS OF JOINT SPACE, DISLOCATION WITH EROSION | 3 | 3 |  |  | METACARPOPHALANGEAL JOINT 4 | RIGHT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 14 | XYZ | MK | XYZ-002 | 14 | SGJSNSCR | Sharp/Genant JSN Score | SEVERE; PARTIAL OR EQUIVOCAL ANKYLOSIS | 3.5 | 3.5 |  |  | METACARPOPHALANGEAL JOINT 4 | LEFT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 15 | XYZ | MK | XYZ-002 | 15 | SGJSNSCR | Sharp/Genant JSN Score | QUESTIONABLE | 0.5 | 0.5 |  |  | METACARPOPHALANGEAL JOINT 5 | RIGHT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
| 16 | XYZ | MK | XYZ-002 | 16 | SGJSNSCR | Sharp/Genant JSN Score | NORMAL | 0 | 0 |  |  | METACARPOPHALANGEAL JOINT 5 | LEFT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |

#### 6.3.7.4 Nervous System Findings (NV)

##### NV – Description/Overview
A findings domain that contains physiological and morphological findings related to the nervous system, including the brain, spinal cord, the cranial and spinal nerves, autonomic ganglia and plexuses.

##### NV – Specification
nv.xpt, Nervous System Findings — Findings. One record per finding per location per time point per visit per subject, Tabulation.

**Structure:** One record per finding per location per time point per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | NV |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | FOCID | Focus of Study-Specific Interest | Char | Identifier | Perm |  |
| 5 | NVSEQ | Sequence Number | Num | Identifier | Req |  |
| 6 | NVGRPID | Group ID | Char | Identifier | Perm |  |
| 7 | NVREFID | Reference ID | Char | Identifier | Perm |  |
| 8 | NVSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 9 | NVLNKID | Link ID | Char | Identifier | Perm |  |
| 10 | NVLNKGRP | Link Group | Char | Identifier | Perm |  |
| 11 | NVTESTCD | Short Name of Nervous System Test | Char | Topic | Req | C116104 |
| 12 | NVTEST | Name of Nervous System Test | Char | Synonym Qualifier | Req | C116103 |
| 13 | NVCAT | Category for Nervous System Test | Char | Grouping Qualifier | Perm |  |
| 14 | NVSCAT | Subcategory for Nervous System Test | Char | Grouping Qualifier | Perm |  |
| 15 | NVORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 16 | NVORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 17 | NVSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 18 | NVSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 19 | NVSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 20 | NVSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 21 | NVREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 22 | NVLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |
| 23 | NVLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| 24 | NVDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| 25 | NVMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 26 | NVLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| 27 | NVBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 28 | NVDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 29 | NVEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 30 | NVEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| 31 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 32 | VISIT | Visit Name | Char | Timing | Perm |  |
| 33 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 34 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 35 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 36 | NVDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 37 | NVDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |
| 38 | NVTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 39 | NVTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 40 | NVELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 41 | NVTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 42 | NVRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **FOCID**: Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed, such as a drug application site (e.g., "Injection site 1", "Biopsy site 1", "Treated site 1") or a more specific focus (e.g., "OD" (right eye), "Upper left quadrant of the back"). The value in this variable should have inherent semantic meaning.
- **NVSEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **NVGRPID**: Used to tie together a block of related records in a single domain for a subject.
- **NVREFID**: Internal or external procedure identifier.
- **NVSPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page.
- **NVLNKID**: Identifier used to link a procedure to the assessment results over the course of the study.
- **NVLNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **NVTESTCD**: Short name of the measurement, test, or examination described in NVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in NVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). NVTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SUVR", "N75LAT", "P100LAT","N145LAT".
- **NVTEST**: Verbatim name of the test or examination used to obtain the measurement or finding. The value in NVTEST cannot be longer than 40 characters. Examples: "Standard Uptake Value Ratio", "N75 Latency", "P100 Latency", "N145 Latency".
- **NVCAT**: Used to define a category of topic-variable values. Example: "VISUAL EVOKED POTENTIAL".
- **NVSCAT**: Used to define a further categorization of NVCAT values.
- **NVORRES**: Result of the procedure measurement or finding as originally received or collected.
- **NVORRESU**: Original units in which the data were collected. The unit for NVORRES.
- **NVSTRESC**: Contains the result value for all findings copied or derived from NVORRES, in a standard format or standard units. NVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in NVSTRESN.
- **NVSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from NVSTRESC. NVSTRESN should store all numeric test results or findings.
- **NVSTRESU**: Standardized unit used for NVSTRESC or NVSTRESN.
- **NVSTAT**: Used to indicate a test was not done, or a measurement was not taken. Should be null if a result exists in NVORRES.
- **NVREASND**: Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with NVSTAT when value is "NOT DONE".
- **NVLOC**: Anatomical location of the subject relevant to the collection of the measurement. Examples: "BRAIN", "EYE", "PRECUNEUS", "CINGULATE CORTEX".
- **NVLAT**: Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".
- **NVDIR**: Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".
- **NVMETHOD**: Method of the test or examination. Examples: "EEG", "PET/CT SCAN ", "FDGPET".
- **NVLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **NVBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that NVBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.
- **NVDRVFL**: Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.
- **NVEVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".
- **NVEVALID**: Used to distinguish multiple evaluators with the same role recorded in NVEVAL. Examples: "RADIOLOGIST 1", "RADIOLOGIST 2".
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the date/time at which the assessment was made.
- **NVDTC**: Date of procedure or test.
- **NVDY**: Study day of the procedure or test, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
- **NVTPT**: Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See NVTPTNUM and NVTPTREF. Examples: "START", "5 MIN POST".
- **NVTPTNUM**: Numerical version of NVTPT to aid in sorting.
- **NVELTM**: Planned elapsed time (in ISO 8601) relative to a fixed time point reference (NVTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by NVTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by NVTPTREF.
- **NVTPTREF**: Name of the fixed reference point referred to by NVELTM, NVTPTNUM, and NVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **NVRFTDTC**: Date/time for a fixed reference time point defined by --TPTREF in ISO 8601 character format.


##### NV – Assumptions
1. Methods of assessment for nervous system findings may include nerve conduction studies, electroencephalogram (EEG), electromyography (EMG), and imaging.
2. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the NV domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --LOINC, --TOX, --TOXGR.

##### NV – Examples

**Example 1**
This example demonstrates the SDTM-based modeling of nervous system information collected and generated from separate positron emission tomography (PET) or PET/computed tomography (PET/CT) procedures.
For this study, measures for standard uptake value ratios (SUVRs) were taken from 3 PET or PET/CT scans. SPDEVID shows the scanner used. NVLNKID can be used to link to the imaging procedure record in the Procedures domain (PRLNKID), as well as to the tracer administration record in the Procedure Agents domain (AGLNKID). AGLNKID would be used to determine which tracer uptake is being measured (SUVR), and therefore to which biomarker the findings pertain. NVDTC corresponds to the date of the PET or PET/CT procedure from which these results were obtained.
**Rows 1-2:** Show the SUVR findings based on a PET/CT scan for a subject.
**Rows 3-4:** Show the SUVR findings based on a PET/CT scan for a subject.
**Rows 5-6:** Show the SUVR findings based on an fluorodeoxyglucose (FDG)-PET scan for a subject.

nv.xpt
| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | NVSEQ | NVREFID | NVLNKID | NVTESTCD | NVTEST | NVORRES | NVORRESU | NVSTRESC | NVSTRESN | NVSTRESU | NVLOC | NVDIR | NVMETHOD | VISITNUM | NVDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | NV | AD01-101 | 22 | 1 | 1236 | 03 | SUVR | Standard Uptake Value Ratio | .95 | RATIO | .95 | .95 | RATIO | PRECUNEUS |  | PET/CT SCAN | 1 | 2012-05-22 |
| 2 | ABC123 | NV | AD01-101 | 22 | 2 | 1236 | 03 | SUVR | Standard Uptake Value Ratio | 1.17 | RATIO | 1.17 |  | RATIO | CINGULATE CORTEX | POSTERIOR | PET/CT SCAN | 1 | 2012-05-22 |
| 3 | ABC123 | NV | AD01-102 | 22 | 1 | 1237 | 04 | SUVR | Standard Uptake Value Ratio | 1.21 | RATIO | 1.21 | 1.21 | RATIO | PRECUNEUS |  | PET/CT SCAN | 1 | 2012-05-22 |
| 4 | ABC123 | NV | AD01-102 | 22 | 2 | 1237 | 04 | SUVR | Standard Uptake Value Ratio | 1.78 | RATIO | 1.78 | 1.78 | RATIO | CINGULATE CORTEX | POSTERIOR | PET/CT SCAN | 1 | 2012-05-22 |
| 5 | ABC123 | NV | AD01-103 | 44 | 1 | 1238 | 05 | SUVR | Standard Uptake Value Ratio | 1.52 | RATIO | 1.52 | 1.52 | RATIO | PRECUNEUS |  | FDGPET | 1 | 2012-05-22 |
| 6 | ABC123 | NV | AD01-103 | 44 | 2 | 1238 | 05 | SUVR | Standard Uptake Value Ratio | 1.63 | RATIO | 1.63 | 1.63 | RATIO | CINGULATE CORTEX | POSTERIOR | FDGPET | 1 | 2012-05-22 |

The reference region used for the SUVR tests shown is represented in a supplemental qualifiers dataset.

suppnv.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | NV | AD01-101 | NVSEQ | 1 | REFREG | Reference Region | CEREBELLUM |
| 2 | ABC123 | NV | AD01-101 | NVSEQ | 2 | REFREG | Reference Region | CEREBELLUM |
| 3 | ABC123 | NV | AD01-102 | NVSEQ | 1 | REFREG | Reference Region | CEREBELLUM |
| 4 | ABC123 | NV | AD01-102 | NVSEQ | 2 | REFREG | Reference Region | CEREBELLUM |
| 5 | ABC123 | NV | AD01-103 | NVSEQ | 1 | REFREG | Reference Region | PONS |
| 6 | ABC123 | NV | AD01-103 | NVSEQ | 2 | REFREG | Reference Region | PONS |

The RELREC table displays the dataset relationship that links procedure to multiple NV domain records--specifically how an individual AG administration record related to a scan is linked to multiple NV domain records. The RELREC table uses --LNKID to relate the PR and AG domains to each other and to NV, and --REFID to relate NV and Device in Use (DU).

In this example, the sponsor has maintained 2 sets of reference identifiers (REFID values) for the specific purpose of being able to relate records across multiple domains. Because the SDTMIG-MD advocates the use of --REFID to link a group of settings to the results obtained from the reading or interpretation of the test (see SDTMIG-MD, Device-in-Use (DU) domain assumptions), --LNKID has been used to establish the relationships between the procedure, the substance administered during the procedure, and the results obtained from the procedure. --LNKID is unique for each procedure for each subject, so datasets may be related to each other as a whole.

**Rows 1-2:** Show the relationship between the scan, represented in PR, and the radiolabel tracer used, represented in AG. There is only 1 tracer administration for each scan, and only 1 scan for each tracer administration, so the relationship is one-to-one.
**Rows 3-4:** Show the relationship between the scan, represented in PR, and the SUVR results obtained from the scan, represented in NV. Each scan yields 2 results, so the relationship is one-to-many.
**Rows 5-6:** Show the relationship between the radiolabel tracer used and the SUVR results for each scan. This relationship may seem indirect, but it is not: The choice of radiolabel has the potential to affect the results obtained. Because the relationship between PR and AG is one-to-one and the relationship between PR and NV is one-to-many, the relationship between AG and NV must be one-to-many.
**Rows 7-8:** Show the relationship between the SUVR results and the specific settings for the device used for each scan. There is more than 1 result from each scan, and more than 1 setting for each scan, so the relationship is many-to-many. This relationship is unusual and challenging to manage in a join/merge, and only represents the concept of this relationship.

relrec.xpt

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | PR |  | PRLNKID |  | ONE | 6 |
| 2 | ABC123 | AG |  | AGLNKID |  | ONE | 6 |
| 3 | ABC123 | PR |  | PRLNKID |  | ONE | 7 |
| 4 | ABC123 | NV |  | NVLNKID |  | MANY | 7 |
| 5 | ABC123 | AG |  | AGLNKID |  | ONE | 8 |
| 6 | ABC123 | NV |  | NVLNKID |  | MANY | 8 |
| 7 | ABC123 | NV |  | NVLNKID |  | MANY | 9 |
| 8 | ABC123 | DU |  | DULNKID |  | MANY | 9 |

**Example 2**
This example shows how to represent components of a pattern-reversal visual evoked-potential (VEP) test elicited by checkerboard stimuli for a subject with optic neuritis. VEPs are detected via an EEG using leads that are placed on the back of the subject's head. It is important to note that the nature of VEP testing is such that NVMETHOD should be equal to "EEG", and that NVCAT should be equal to "VISUAL EVOKED POTENTIAL". Several latencies from each eye--including N75, P100, and N145, as well as the P100 peak-to-peak amplitude (75-100)--are collected and should be represented in NVTESTCD/NVTEST. Details about the VEP equipment including the checkerboard size should be represented in the appropriate device domains. To interpret, each VEP component is compared against normative values established by the laboratory using healthy controls.

In this example, a VEP component is considered abnormal if it falls outside of 3 standard deviations from the normative lab mean. These low and high values are stored in NVORNRLO and NVORNRHI, respectively, and the interpretation of each VEP component is represented in NVNRIND. In addition to interpreting each VEP component as normal or abnormal, the overall test for each eye may have an interpretation. In this scenario, NVTESTCD/NVTEST should be equal to "INTP" (Interpretation) and NVORRES should represent whether the overall test in each eye is normal or abnormal. NVGRPID links the each VEP component to the overall interpretation.

The NV domain should be used to represent the VEP latencies, P100 peak-to-peak amplitude, and their interpretations. SPDEVID allows the results to be related to both the VEP testing device and the checkerboard size.

**Rows 1-4:** Show the VEP measurements for the right eye.
**Row 5:** Shows that when all the components of right eye VEP are considered together (NVGRPID=1), the overall test is interpreted as abnormal.
**Rows 6-9:** Show the VEP measurements for the left eye.
**Row 10:** Shows that when all the components of left eye VEP are considered together (NVGRPID=2), the overall test is interpreted as abnormal.

nv.xpt

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | FOCID | NVSEQ | NVGRPID | NVTESTCD | NVTEST | NVCAT | NVORRES | NVORRESU | NVSTRESC | NVSTRESN | NVSTRESU | NVORNRLO | NVORNRHI | NVNRIND | NVLOC | NVLAT | NVMETHOD | VISITNUM | NVDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | MS123 | NV | MS01-01 | 123 | OD | 1 | 1 | N75LAT | N75 Latency | VISUAL EVOKED POTENTIAL | 79.8 | msec | 79.8 | 79.8 | msec | 54.68 | 94 | NORMAL | EYE | RIGHT | EEG | 1 | 2013-02-08 |
| 2 | MS123 | NV | MS01-01 | 123 | OD | 2 | 1 | P100LAT | P100 Latency | VISUAL EVOKED POTENTIAL | 129 | msec | 129 | 129 | msec | 76.75 | 113.71 | ABNORMAL | EYE | RIGHT | EEG | 1 | 2013-02-08 |
| 3 | MS123 | NV | MS01-01 | 123 | OD | 3 | 1 | N145LAT | N145 Latency | VISUAL EVOKED POTENTIAL | 181 | msec | 181 | 181 | msec | 114.27 | 156.03 | ABNORMAL | EYE | RIGHT | EEG | 1 | 2013-02-08 |
| 4 | MS123 | NV | MS01-01 | 123 | OD | 4 | 1 | P100AMP | P100 Amplitude | VISUAL EVOKED POTENTIAL | 5.02 | uV | 5.02 | 5.02 | uV | 5.26 | 12.64 | ABNORMAL | EYE | RIGHT | EEG | 1 | 2013-02-08 |
| 5 | MS123 | NV | MS01-01 | 123 | OD | 5 | 1 | INTP | Interpretation | VISUAL EVOKED POTENTIAL | ABNORMAL |  | ABNORMAL |  |  |  |  |  | EYE | RIGHT | EEG | 1 | 2013-02-08 |
| 6 | MS123 | NV | MS01-01 | 123 | OS | 6 | 2 | N75LAT | N75 Latency | VISUAL EVOKED POTENTIAL | 83.8 | msec | 83.8 | 83.8 | msec | 54.42 | 95.1 | NORMAL | EYE | LEFT | EEG | 1 | 2013-02-08 |
| 7 | MS123 | NV | MS01-01 | 123 | OS | 7 | 2 | P100LAT | P100 Latency | VISUAL EVOKED POTENTIAL | 126 | msec | 126 | 126 | msec | 76.9 | 115.78 | ABNORMAL | EYE | LEFT | EEG | 1 | 2013-02-08 |
| 8 | MS123 | NV | MS01-01 | 123 | OS | 8 | 2 | N145LAT | N145 Latency | VISUAL EVOKED POTENTIAL | 160 | msec | 160 | 160 | msec | 115.65 | 157.65 | ABNORMAL | EYE | LEFT | EEG | 1 | 2013-02-08 |
| 9 | MS123 | NV | MS01-01 | 123 | OS | 9 | 2 | P100AMP | P100 Amplitude | VISUAL EVOKED POTENTIAL | 4.37 | uV | 4.37 | 4.37 | uV | 4.78 | 12.7 | ABNORMAL | EYE | LEFT | EEG | 1 | 2013-02-08 |
| 10 | MS123 | NV | MS01-01 | 123 | OS | 10 | 2 | INTP | Interpretation | VISUAL EVOKED POTENTIAL | ABNORMAL |  | ABNORMAL |  |  |  |  |  | EYE | LEFT | EEG | 1 | 2013-02-08 |

Information about the VEP device is not shown. Identifying information would be represented using the DI domain, and any properties of the device that may change between assessments would be represented in the DO and DU domains. See the SDTMIG-MD for examples of these domains.

#### 6.3.7.5 Ophthalmic Examinations (OE)

##### OE – Description/Overview
A findings domain that contains tests that measure a person's ocular health and visual status, to detect abnormalities in the components of the visual system, and to determine how well the person can see.


##### OE – Specification
oe.xpt, Ophthalmic Examinations — Findings. One record per ophthalmic finding per method per location, per time point per visit per subject, Tabulation.

**Structure:** One record per ophthalmic finding per method per location, per time point per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | OE |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | FOCID | Focus of Study-Specific Interest | Char | Identifier | Perm | C119013 |
| 5 | OESEQ | Sequence Number | Num | Identifier | Req |  |
| 6 | OEGRPID | Group ID | Char | Identifier | Perm |  |
| 7 | OELNKID | Link ID | Char | Identifier | Perm |  |
| 8 | OELNKGRP | Link Group | Char | Identifier | Perm |  |
| 9 | OETESTCD | Short Name of Ophthalmic Test or Exam | Char | Topic | Req | C117743 |
| 10 | OETEST | Name of Ophthalmic Test or Exam | Char | Synonym Qualifier | Req | C117742 |
| 11 | OETSTDTL | Ophthalmic Test or Exam Detail | Char | Variable Qualifier | Perm |  |
| 12 | OECAT | Category for Ophthalmic Test or Exam | Char | Grouping Qualifier | Perm |  |
| 13 | OESCAT | Subcategory for Ophthalmic Test or Exam | Char | Grouping Qualifier | Perm |  |
| 14 | OEORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 15 | OEORRESU | Original Units | Char | Variable Qualifier | Exp | C71620 |
| 16 | OEORNRLO | Normal Range Lower Limit-Original Units | Char | Variable Qualifier | Perm |  |
| 17 | OEORNRHI | Normal Range Upper Limit-Original Units | Char | Variable Qualifier | Perm |  |
| 18 | OESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 19 | OESTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Exp |  |
| 20 | OESTRESU | Standard Units | Char | Variable Qualifier | Exp | C71620 |
| 21 | OESTNRLO | Normal Range Lower Limit-Standard Units | Num | Variable Qualifier | Perm |  |
| 22 | OESTNRHI | Normal Range Upper Limit-Standard Units | Num | Variable Qualifier | Perm |  |
| 23 | OESTNRC | Normal Range for Character Results | Char | Variable Qualifier | Perm |  |
| 24 | OENRIND | Normal/Reference Range Indicator | Char | Variable Qualifier | Perm | C78736 |
| 25 | OERESCAT | Result Category | Char | Variable Qualifier | Perm |  |
| 26 | OESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 27 | OEREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 28 | OEXFN | External File Path | Char | Record Qualifier | Perm |  |
| 29 | OELOC | Location Used for the Measurement | Char | Record Qualifier | Exp | C74456 |
| 30 | OELAT | Laterality | Char | Variable Qualifier | Exp | C99073 |
| 31 | OEDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| 32 | OEPORTOT | Portion or Totality | Char | Variable Qualifier | Perm | C99075 |
| 33 | OEMETHOD | Method of Test or Examination | Char | Record Qualifier | Exp | C85492 |
| 34 | OELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 35 | OEBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 36 | OEDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 37 | OEEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 38 | OEEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| 39 | OEACPTFL | Accepted Record Flag | Char | Record Qualifier | Perm | C66742 |
| 40 | OEREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |
| 41 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 42 | VISIT | Visit Name | Char | Timing | Perm |  |
| 43 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 44 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 45 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 46 | OEDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 47 | OEDY | Study Day of Visit/Collection/Exam | Num | Timing | Exp |  |
| 48 | OETPT | Planned Time Point Name | Char | Timing | Perm |  |
| 49 | OETPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 50 | OEELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 51 | OETPTREF | Time Point Reference | Char | Timing | Perm |  |
| 52 | OERFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **FOCID**: Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed.
- **OESEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **OEGRPID**: Optional group identifier, used to link together a block of related records within a subject in a domain.
- **OELNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.
- **OELNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **OETESTCD**: Short character value for OETEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in OETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). OETESTCD cannot contain characters other than letters, numbers, or underscores. Example: "NUMLCOR".
- **OETEST**: Long name for the test or examination used to obtain the measurement or finding. The value in OETEST cannot be longer than 40 characters. Example: "Number of Letters Correct" for OETESTCD = "NUMLCOR".
- **OETSTDTL**: Further description of OETESTCD and OETEST.
- **OECAT**: Used to define a category of topic-variable values. Examples: "VISUAL ACUITY", "CONTRAST SENSITIVITY", "OCULAR COMFORT".
- **OESCAT**: Used to define a further categorization of OECAT values. Example: "HIGH CONTRAST" or "LOW CONTRAST" when OECAT is "VISUAL ACUITY".
- **OEORRES**: Result of the measurement or finding as originally received or collected. Examples: "120", "<1, NORMAL", "RED SPOT VISIBLE".
- **OEORRESU**: Original unit for OEORRES. Examples: "mm", "um".
- **OEORNRLO**: Lower end of normal range or reference range for results stored in OEORRES.
- **OEORNRHI**: Upper end of normal range or reference range for results stored in OEORRES.
- **OESTRESC**: Contains the result value for all findings copied or derived from OEORRES, in a standard format or in standard units. OESTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in OESTRESN.
- **OESTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from OESTRESC. OESTRESN should store all numeric test results or findings.
- **OESTRESU**: Standardized units used for OESTRESC and OESTRESN. Examples: "mm", "um".
- **OESTNRLO**: Lower end of normal range or reference range for standardized results (e.g., OESTRESC, OESTRESN) represented in standardized units (OESTRESU).
- **OESTNRHI**: Upper end of normal range or reference range for standardized results (e.g., OESTRESC, OESTRESN) represented in standardized units (OESTRESU).
- **OESTNRC**: Normal range or reference range for results stored in OESTRESC that are character in ordinal or categorical scale. Example: "Negative to Trace".
- **OENRIND**: Used to indicate the value is outside the normal range or reference range. May be defined by OEORNRLO and OEORNRHI or other objective criteria. Examples: "Y", "N"; "HIGH", "LOW"; "NORMAL", "ABNORMAL".
- **OERESCAT**: Used to categorize the result of a finding or medical status per interpretation of test results. Examples: "POSITIVE", "NEGATIVE". The variable OERESCAT is not meant to replace the use of OENRIND for cases where normal ranges are provided.
- **OESTAT**: Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".
- **OEREASND**: Reason not done. Used in conjunction with OESTAT when value is "NOT DONE".
- **OEXFN**: Filename for an external file, such as one for a retinal OCT image.
- **OELOC**: Anatomical location of the subject relevant to the collection of the measurement. Examples: "EYE" for a finding record relative to the complete eye, "RETINA" for a measurement or assessment of only the retina.
- **OELAT**: Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".
- **OEDIR**: Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".
- **OEPORTOT**: Qualifier for anatomical location or specimen further detailing the distribution (i.e., arrangement of, apportioning of). Examples: "ENTIRE", "SINGLE", "SEGMENT", "MANY".
- **OEMETHOD**: Method of the test or examination. Example: "ETDRS EYE CHART" for OETESTCD = "NUMLCOR". The different methods may offer different functionality or granularity, affecting the set of results and associated meaning.
- **OELOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **OEBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that OEBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **OEDRVFL**: Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.
- **OEEVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "INDEPENDENT ASSESSOR", "INVESTIGATOR".
- **OEEVALID**: Used to distinguish multiple evaluators with the same role recorded in OEEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2".
- **OEACPTFL**: In cases where more than one assessor provides an evaluation of a result or response, this flag identifies the record that is considered, by an independent assessor, to be the accepted evaluation. Expected to be "Y" or null.
- **OEREPNUM**: The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the date/time at which the assessment was made.
- **OEDTC**: Collection date/time of the observation.
- **OEDY**: Actual study day of observation/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **OETPT**: Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point.
- **OETPTNUM**: Numeric version of planned time point used in sorting.
- **OEELTM**: Planned elapsed time relative to a planned fixed reference (OETPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.
- **OETPTREF**: Description of the fixed reference point referred to by OETPT, OETPTNUM, and OEELTM.
- **OERFTDTC**: Date/time of the reference time point, OETPTREF.


##### OE – Assumptions
1. In ophthalmic studies, the eyes are usually sites of treatment. It is appropriate to identify sites using the variable FOCID. When FOCID is used to identify the eyes, it is recommended that the values "OD" (oculus dexter, right eye), "OS" (oculus sinister, left eye), and "OU" (oculus uterque, both eyes) be used in FOCID. These terms are the exclusively preferred terms used by the ophthalmology community as abbreviations for the expanded Latin terms, and are included in the nonextensible CDISC Ophthalmic Focus of Study Specific Interest (OEFOCUS) codelist.
2. In any study that uses FOCID, FOCID would be included in records in any subject-level domain representing findings, interventions, or events (e.g., Adverse Events) related to the eyes. Whether or not FOCID is used in a study, --LOC and --LAT should be populated in records related to the eyes. The value in OELOC may be "EYE" but may also be a part of the eye (e.g., "RETINA", "CORNEA").
3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the OE domain, but the following qualifiers would not generally be used: --MODIFY, --NSPCES, --POS, --BODSYS, --ORREF, --STREFC, --STREFN, --CHRON, --DISTR, --ANTREG, --LEAD, --FAST, --TOX, --TOXGR, --LLOQ, --ULOQ.

##### OE – Examples

**Example 1**
This example shows a general anterior segment examination performed on each eye at 1 visit, with the purpose of evaluating general abnormalities.
**Rows 1-2:** Represent an overall interpretation (i.e., normal/abnormal) finding from the anterior segment examination, using OETESTCD="INTP". OELOC indicates that the assessor examined the lens and OELAT indicates which lens was examined.
**Row 3:** Represents an abnormality observed during the anterior segment examination of the right eye. OEDIR="MULTIPLE" and indicates multiple directionality values are applicable. OELOC, OELAT, and the multiple OEDIR values specify the location of the abnormality represented in OEORRES and OESTRESC. This observed abnormality (i.e., red spot visible) was determined to be clinically significant (OECLSIG="Y").

*oe.xpt*

| Row | STUDYID | DOMAIN | USUBJID | FOCID | OESEQ | OETESTCD | OETEST | OEORRES | OESTRESC | OELOC | OELAT | OEDIR | OEMETHOD | OEEVAL | OECLSIG | VISITNUM | VISIT | OEDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XXX | OE | XXX-450-110 | OS | 1 | INTP | Interpretation | NORMAL | NORMAL | LENS | LEFT |  | SLIT LAMP | INVESTIGATOR |  | 1 | SCREENING | 2012-03-20 |
| 2 | XXX | OE | XXX-450-110 | OD | 2 | INTP | Interpretation | ABNORMAL | ABNORMAL | LENS | RIGHT |  | SLIT LAMP | INVESTIGATOR |  | 1 | SCREENING | 2012-03-20 |
| 3 | XXX | OE | XXX-450-110 | OD | 3 | OEEXAM | Ophthalmic Examination | RED SPOT VISIBLE | RED SPOT VISIBLE | CONJUNCTIVA | RIGHT | MULTIPLE | SLIT LAMP | INVESTIGATOR | Y | 1 | SCREENING | 2012-03-20 |

The supplemental qualifier dataset represents the multiple directionality values, further describing the anatomical location where the abnormality was observed.

*suppoe.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XXX | OE | XXX-450-110 | OESEQ | 3 | OEDIR1 | Directionality 1 | SUPERIOR |
| 2 | XXX | OE | XXX-450-110 | OESEQ | 3 | OEDIR2 | Directionality 2 | TEMPORAL |

**Example 2**
This example shows:
- Different assessments, from the front to the back of the eye, for 1 subject at 1 visit
- The use of the supplemental qualifier non-standard variable (NSV) OEEDILST (Eye Dilation Status)

The test for iris color is in the OE domain because in this use case, the medication is likely to change the result over the course of the study. Otherwise, iris color should be represented in the Subject Characteristics (SC) domain (see Section 6.3.10, Subject Characteristics).
**Rows 1-2:** Show assessments of the color of the iris (OELOC="IRIS") for the right and left eyes, respectively.
**Rows 3-4:** Show assessments of the status of the lens (OELOC="LENS") for the right and left eyes, respectively. This status assessment is to determine whether the lens of the eye is the natural lens (OEORRES="PHAKIC") or a replacement (OEORRES="PSEUDOPHAKIC").
**Rows 5-6:** Show assessments looking for the presence of hyperemia (increased blood flow). The fact that OELOC="CONJUNCTIVA" even for the left eye, where hyperemia was absent, suggests that this examination was specifically an examination of the conjunctiva. Hyperemia was identified in the right eye and was judged to be clinically significant.
**Rows 7-8:** Show measurements of the cup-to-disc ratio for the right and left eyes, respectively.

*oe.xpt*

| Row | STUDYID | DOMAIN | USUBJID | FOCID | OESEQ | OETESTCD | OETEST | OEORRES | OEORRESU | OESTRESC | OESTRESN | OESTRESU | OELOC | OELAT | OEMETHOD | OEEVAL | OECLSIG | VISITNUM | VISIT | OEDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XXX | OE | XXX-450-120 | OD | 1 | COLOR | Color | BLUE |  | BLUE |  |  | IRIS | RIGHT | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR |  | 1 | SCREENING | 2012-04-20 |
| 2 | XXX | OE | XXX-450-120 | OS | 2 | COLOR | Color | BLUE |  | BLUE |  |  | IRIS | LEFT | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR |  | 1 | SCREENING | 2012-04-20 |
| 3 | XXX | OE | XXX-450-120 | OD | 3 | LENSSTAT | Lens Status | PHAKIC |  | PHAKIC |  |  | LENS | RIGHT | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR |  | 1 | SCREENING | 2012-04-20 |
| 4 | XXX | OE | XXX-450-120 | OS | 4 | LENSSTAT | Lens Status | PSEUDOPHAKIC |  | PSEUDOPHAKIC |  |  | LENS | LEFT | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR |  | 1 | SCREENING | 2012-04-20 |
| 5 | XXX | OE | XXX-450-120 | OD | 5 | HYPERMIA | Hyperemia | PRESENT |  | PRESENT |  |  | CONJUNCTIVA | RIGHT | OPHTHALMOSCOPY | INVESTIGATOR | Y | 1 | SCREENING | 2012-04-20 |
| 6 | XXX | OE | XXX-450-120 | OS | 6 | HYPERMIA | Hyperemia | ABSENT |  | ABSENT |  |  | CONJUNCTIVA | LEFT | OPHTHALMOSCOPY | INVESTIGATOR |  | 1 | SCREENING | 2012-04-20 |
| 7 | XXX | OE | XXX-450-120 | OD | 7 | CUPDISC | Cup-to-Disc Ratio | 0.5 | RATIO | 0.5 | 0.5 | RATIO | OPTIC DISC | RIGHT | OPHTHALMOSCOPY | INVESTIGATOR |  | 1 | SCREENING | 2012-04-20 |
| 8 | XXX | OE | XXX-450-120 | OS | 8 | CUPDISC | Cup-to-Disc Ratio | 0.6 | RATIO | 0.6 | 0.6 | RATIO | OPTIC DISC | LEFT | OPHTHALMOSCOPY | INVESTIGATOR |  | 1 | SCREENING | 2012-04-20 |

The suppoe.xpt dataset represents the testing condition (i.e., dilated eyes) qualifying the cup-to-disc ratio tests.

*suppoe.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XXX | OE | XXX-450-120 | OESEQ | 7 | OEEDILST | Eye Dilation Status | DILATED |
| 2 | XXX | OE | XXX-450-120 | OESEQ | 8 | OEEDILST | Eye Dilation Status | DILATED |

**Example 3**
This example shows:
- Partial results of the macula examination performed by the site investigator, as well as results provided by an independent assessor, for 1 visit
- The use of the NSV EVLDTC
- The use of the Procedures (PR) domain to represent the optical coherence tomography (OCT) procedure details, with specific device characteristics in the DI domain
- The relationship between the OE and PR domains in the RELREC dataset

**Rows 1-2:** Represent the assessments performed by the investigator. OECLSIG represents the investigator's assessment of clinical significance. OEDTC represents the ophthalmoscopy exam date.
**Rows 3-6:** Represent the assessments performed by an independent assessor. OEDTC represents the OCT image date.

*oe.xpt*

| Row | STUDYID | DOMAIN | USUBJID | FOCID | OESEQ | OELNKID | OETESTCD | OETEST | OEORRES | OEORRESU | OESTRESC | OESTRESN | OESTRESU | OELOC | OELAT | OEMETHOD | OEEVAL | OECLSIG | VISITNUM | VISIT | OEDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | OE | XYZ-100-001 | OS | 1 |  | EDEMA | Edema | PRESENT |  | PRESENT |  |  | MACULA | LEFT | OPHTHALMOSCOPY | INVESTIGATOR | Y | 1 | SCREENING | 2012-04-25 |
| 2 | XYZ | OE | XYZ-100-001 | OD | 2 |  | EDEMA | Edema | ABSENT |  | ABSENT |  |  | MACULA | RIGHT | OPHTHALMOSCOPY | INVESTIGATOR | N | 1 | SCREENING | 2012-04-25 |
| 3 | XYZ | OE | XYZ-100-001 | OS | 3 | 1 | EDEMA | Edema | PRESENT |  | PRESENT |  |  | MACULA | LEFT | OPTICAL COHERENCE TOMOGRAPHY | INDEPENDENT ASSESSOR |  | 1 | SCREENING | 2012-04-25 |
| 4 | XYZ | OE | XYZ-100-001 | OD | 4 | 2 | EDEMA | Edema | ABSENT |  | ABSENT |  |  | MACULA | RIGHT | OPTICAL COHERENCE TOMOGRAPHY | INDEPENDENT ASSESSOR |  | 1 | SCREENING | 2012-04-25 |
| 5 | XYZ | OE | XYZ-100-001 | OS | 5 | 1 | THICK | Thickness | 1030 | um | 1030 | 1030 | um | MACULA | LEFT | OPTICAL COHERENCE TOMOGRAPHY | INDEPENDENT ASSESSOR |  | 1 | SCREENING | 2012-04-25 |
| 6 | XYZ | OE | XYZ-100-001 | OD | 6 | 2 | THICK | Thickness | 1005 | um | 1005 | 1005 | um | MACULA | RIGHT | OPTICAL COHERENCE TOMOGRAPHY | INDEPENDENT ASSESSOR |  | 1 | SCREENING | 2012-04-25 |

The suppoe.xpt dataset represents the date the independent assessor performed the evaluation of the OCT image.

*suppoe.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | OE | XYZ-100-001 | OELNKID | 1 | OEEVLDTC | Evaluation Date | 2012-04-30 |
| 2 | XYZ | OE | XYZ-100-001 | OELNKID | 2 | OEEVLDTC | Evaluation Date | 2012-04-30 |

**Rows 1-4:** Represent OCT procedures performed at screening and visit 1 on the right and left eyes. SPDEVID identifies the device used in performing these tests.
**Row 5:** Indicates that an OCT procedure was not performed at visit 2. The reason the procedure was not performed was collected and is represented in PRREASOC.

*pr.xpt*

| Row | STUDYID | DOMAIN | USUBJID | FOCID | SPDEVID | PRSEQ | PRLNKID | PRTRT | PRPRESP | PROCCUR | PRREASOC | PRLOC | PRLAT | PRSTDTC | VISITNUM | VISIT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | PR | XYZ-100-001 | OS | 100 | 1 | 1 | OCT | Y | Y |  | EYE | LEFT | 2012-04-25T09:30:00 | 1 | SCREENING |
| 2 | XYZ | PR | XYZ-100-001 | OD | 100 | 2 | 2 | OCT | Y | Y |  | EYE | RIGHT | 2012-04-25T10:10:00 | 1 | SCREENING |
| 3 | XYZ | PR | XYZ-100-001 | OS | 100 | 3 | 3 | OCT | Y | Y |  | EYE | LEFT | 2012-05-25T08:00:00 | 2 | VISIT 1 |
| 4 | XYZ | PR | XYZ-100-001 | OD | 100 | 4 | 4 | OCT | Y | Y |  | EYE | RIGHT | 2012-05-25T08:30:00 | 2 | VISIT 1 |
| 5 | XYZ | PR | XYZ-100-001 | OU |  | 5 |  | OCT | Y | N | PATIENT WAS SICK FOR SEVERAL WEEKS |  |  |  | 3 | VISIT 2 |

Identifying information for the device with SPDEVID = "100" included in the PR domain is represented in the Device Identifiers (DI) domain.

*di.xpt*

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | DI | 100 | 1 | TYPE | Device Type | OCT |
| 2 | XYZ | DI | 100 | 2 | MANUF | Manufacturer | ZEISS |
| 3 | XYZ | DI | 100 | 3 | MODEL | Model | CIRRUS |
| 4 | XYZ | DI | 100 | 4 | SERIAL | Serial Number | yyyyyy |

The many-to-one relationship between records in the PR and OE domains is described in RELREC.

*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | PR |  | PRLNKID |  | ONE | 13 |
| 2 | XYZ | OE |  | OELNKID |  | MANY | 13 |

**Example 4**
This example shows:
- A CRF that collects subject's comfort of a lubricant eye drop for keratoconjunctivitis sicca (dry eye) on a numeric scale (i.e., 1 to 10, with 1 meaning most comfortable and 10 meaning most uncomfortable)
- The use of the NSV OERESCRT, to describe the numeric scale
- A subject who experienced an adverse event on the eye. The FOCID variable is included in the AE domain to allow the grouping of all ophthalmic observations.

**Row 1:** Represents the subject's assessment of ocular comfort in the right eye, upon instillation of a lubricant eye drop for dry eye.
**Row 2:** Represents the subject's assessment of ocular comfort in the right eye, 1 minute post-instillation of a lubricant eye drop for dry eye.
**Row 3:** Represents the subject's assessment of ocular comfort in the left eye, upon instillation of a lubricant eye drop for dry eye.
**Row 4:** Represents the subject's assessment of ocular comfort in the left eye, 1 minute post-instillation of a lubricant eye drop for dry eye.

*oe.xpt*

| Row | STUDYID | DOMAIN | USUBJID | FOCID | OESEQ | OETESTCD | OETEST | OECAT | OEORRES | OESTRESC | OESTRESN | OELOC | OELAT | OEMETHOD | OEEVAL | VISITNUM | VISIT | OEDTC | OETPT | OETPTNUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | OE | XYZ-100-0001 | OD | 1 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 1 | 1 | 1 | EYE | RIGHT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-02-11T09:00 | UPON INSTILLATION | 1 |
| 2 | XYZ | OE | XYZ-100-0001 | OD | 2 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 10 | 10 | 10 | EYE | RIGHT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-02-11T09:01 | 1 MINUTE POST-INSTILLATION | 2 |
| 3 | XYZ | OE | XYZ-100-0001 | OS | 1 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 1 | 1 | 1 | EYE | LEFT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-05-01T09:00 | UPON INSTILLATION | 1 |
| 4 | XYZ | OE | XYZ-100-0001 | OS | 2 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 10 | 10 | 10 | EYE | LEFT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-05-01T09:01 | 1 MINUTE POST-INSTILLATION | 2 |

The numeric scale used in grading ocular comfort is described in a supplemental qualifier dataset.

*suppoe.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | OE | XYZ-100-0001 | OECAT | OCULAR COMFORT | OERESCRT | Result Criteria | 10-point VAS (1=Best, 10=Worst) |

Adverse events affecting the eyes are represented in the AE domain. For events that affected only 1 eye, the sponsor populated FOCID, an identifier variable that can be included in any domain.

*ae.xpt*

| Row | STUDYID | DOMAIN | USUBJID | FOCID | AESEQ | AESPID | AETERM | AEDECOD | AEBODSYS | AELOC | AELAT | AESEV | AESER | AEACN | AEREL | AEOUT | AESTDTC | AEENDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | AE | XYZ-100-0001 |  | 5 | 1 | Headaches | Headache | Nervous system disorders |  |  | MILD | N | DOSE NOT CHANGED | NOT RELATED | RECOVERED/RESOLVED | 2011-05-02 | 2011-05-06 |
| 2 | XYZ | AE | XYZ-100-0001 | OD | 6 | 2 | Worsening Dry Eyes | Dry eye | Eye disorders | EYE | RIGHT | MODERATE | N | DOSE NOT CHANGED | NOT RELATED | RECOVERED/RESOLVED | 2011-05-03 | 2011-05-05 |
| 3 | XYZ | AE | XYZ-100-0001 | OS | 7 | 2 | Worsening Dry Eyes | Dry eye | Eye disorders | EYE | LEFT | MODERATE | N | DOSE NOT CHANGED | NOT RELATED | RECOVERED/RESOLVED | 2011-05-03 | 2011-05-04 |

#### 6.3.7.6 Reproductive System Findings (RP)

##### RP – Description/Overview
A findings domain that contains physiological and morphological findings related to the male and female reproductive systems.

##### RP – Specification
rp.xpt, Reproductive System Findings — Findings. One record per finding or result per time point per visit per subject, Tabulation.

**Structure:** One record per finding or result per time point per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | RP |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | RPSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | RPGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | RPREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | RPSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | RPLNKID | Link ID | Char | Identifier | Perm |  |
| 9 | RPLNKGRP | Link Group ID | Char | Identifier | Perm |  |
| 10 | RPTESTCD | Short Name of Reproductive Test | Char | Topic | Req | C106479 |
| 11 | RPTEST | Name of Reproductive Test | Char | Synonym Qualifier | Req | C106478 |
| 12 | RPCAT | Category for Reproductive Test | Char | Grouping Qualifier | Perm |  |
| 13 | RPSCAT | Subcategory for Reproductive Test | Char | Grouping Qualifier | Perm |  |
| 14 | RPORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 15 | RPORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 16 | RPSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 17 | RPSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 18 | RPSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 19 | RPSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 20 | RPREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 21 | RPLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Perm | C66742 |
| 22 | RPBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 23 | RPDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 24 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 25 | VISIT | Visit Name | Char | Timing | Perm |  |
| 26 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 27 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 28 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 29 | RPDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 30 | RPDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |
| 31 | RPDUR | Duration | Char | Timing | Perm | ISO 8601 duration |
| 32 | RPTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 33 | RPTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 34 | RPELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 35 | RPTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 36 | RPRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **RPSEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1.
- **RPGRPID**: Optional group identifier, used to link together a block of related records within a subject in a domain. Also used to link together a block of related records in the Trial Summary dataset.
- **RPREFID**: Optional internal or external identifier (e.g., lab specimen ID, UUID for an ECG waveform or a medical image).
- **RPSPID**: Sponsor-defined identifier. Example: Preprinted line identifier on a CRF.
- **RPLNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.
- **RPLNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **RPTESTCD**: Short character value for RPTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: "CHILDPOT", "BCMETHOD", "MENARAGE".
- **RPTEST**: Long name For RPTESTCD. Examples: "Childbearing Potential", "Birth Control Method", "Menarche Age".
- **RPCAT**: Used to define a category of topic-variable values. Example: "No use case to date, but values would be relative to reproduction tests grouping".
- **RPSCAT**: Used to define a further categorization of RPCAT values. Example: "No use case to date, but values would be relative to reproduction tests grouping".
- **RPORRES**: Result of the measurement or finding as originally received or collected. Examples: "120", "<1", "POS".
- **RPORRESU**: Unit for RPORRES. Examples: "in", "LB", "kg/L".
- **RPSTRESC**: Contains the result value for all findings copied or derived from RPORRES, in a standard format or in standard units. RPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in RPSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in RPORRES, and these results effectively have the same meaning, they could be represented in standard format in RPSTRESC as "NEGATIVE".
- **RPSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from RPSTRESC. RPSTRESN should store all numeric test results or findings.
- **RPSTRESU**: Standardized units used for RPSTRESC and RPSTRESN. Example: "mol/L".
- **RPSTAT**: Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".
- **RPREASND**: Reason not done. Used in conjunction with RPSTAT when value is "NOT DONE".
- **RPLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **RPBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that RPBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **RPDRVFL**: Used to indicate a derived record. The value should be "Y" or null. Records which represent the average of other records or which do not come from the CRF are examples of records that would be derived for the submission datasets. If RPDRVFL = "Y", then RPORRES may be null, with RPSTRESC and (if numeric) RPSTRESN having the derived value.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter.
- **VISITDY**: Planned study day of VISIT. Should be an integer.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the date/time at which the assessment was made.
- **RPDTC**: Collection date and time of an observation.
- **RPDY**: Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **RPDUR**: Collected duration of an event, intervention, or finding represented in ISO 8601 character format. Used only if collected on the CRF and not derived.
- **RPTPT**: Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose.
- **RPTPTNUM**: Numeric version of planned time point used in sorting.
- **RPELTM**: Planned elapsed time in ISO 8601 character format relative to a planned fixed reference (RPTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.
- **RPTPTREF**: Description of the fixed reference point referred to by RPELTM, RPTPTNUM, and RPTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **RPRFTDTC**: Date/time for a fixed reference time point defined by RPTPTREF in ISO 8601 character format.


##### RP – Assumptions
1. Reproductive System Findings domain contains information regarding a subject’s reproductive ability and reproductive history (e.g., number of previous pregnancies, number of births, pregnant during the study).
2. Information on medications related to reproduction (e.g., contraceptives, fertility treatments) should be included in the Concomitant/Prior Medications (CM) domain; see Section 6.1.2.
3. There are separate codelists for RP tests, responses, and units.
    a. Associations between RP tests and response codelists are described in the RP Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.
4. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the RP domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --LOINC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

##### RP – Examples

**Example 1**
This example represents reproductive system findings at the screening visit, visit 1, and visit 2 for 2 subjects.

rp.xpt

| Row | STUDYID | DOMAIN | USUBJID | RPSEQ | RPTESTCD | RPTEST | RPORRES | RPORRESU | RPSTRESC | RPSTRESN | RPSTRESU | RPDUR | RPBLFL | VISITNUM | VISIT | VISITDY | RPDTC | RPDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | STUDYX | RP | 2324P0001 | 1 | SPABORTN | Number of Spontaneous Abortions | 1 |  | 1 | 1 |  |  | Y | 1 | SCREENING | 1 | 2008-03-09 | -10 |
| 2 | STUDYX | RP | 2324P0001 | 2 | BRTHLVN | Number of Live Births | 2 |  | 2 | 2 |  |  | Y | 1 | SCREENING | 1 | 2008-03-09 | -10 |
| 3 | STUDYX | RP | 2324P0001 | 3 | PREGNN | Number of Pregnancies | 3 |  | 3 | 3 |  |  | Y | 1 | SCREENING | 1 | 2008-03-09 | -10 |
| 4 | STUDYX | RP | 2324P0001 | 4 | MENOSTAT | Menopause Status | Pre-Menopause |  | Pre-Menopause |  |  |  | Y | 1 | SCREENING | 1 | 2008-03-09 | -10 |
| 5 | STUDYX | RP | 2324P0001 | 5 | MENARAGE | Menarche Age | 10 | YEARS | 10 | 10 | YEARS |  | Y | 1 | SCREENING | 1 | 2008-03-09 | -10 |
| 6 | STUDYX | RP | 2324P0001 | 6 | BCMETHOD | Birth Control Method | FOAM OR OTHER SPERMICIDES |  | FOAM OR OTHER SPERMICIDES |  |  | P3Y | Y | 1 | SCREENING | 1 | 2008-03-09 | -10 |
| 7 | STUDYX | RP | 2324P0001 | 7 | CHILDPOT | Childbearing Potential | Y |  | Y |  |  |  | Y | 1 | SCREENING | 1 | 2008-03-09 | -10 |
| 8 | STUDYX | RP | 2324P0001 | 8 | CHILDPOT | Childbearing Potential | Y |  | Y |  |  |  |  | 2 | Day 1 | 1 | 2008-03-19 | 1 |
| 9 | STUDYX | RP | 2324P0001 | 9 | PREGST | Pregnant During the Study | N |  | N |  |  |  |  | 2 | Day 1 | 1 | 2008-03-19 | 1 |
| 10 | STUDYX | RP | 2324P0001 | 10 | CHILDPOT | Childbearing Potential | Y |  | Y |  |  |  |  | 3 | Day 29 | 29 | 2008-04-16 | 29 |
| 11 | STUDYX | RP | 2324P0001 | 11 | PREGST | Pregnant During the Study | N |  | N |  |  |  |  | 3 | Day 29 | 29 | 2008-04-16 | 29 |
| 12 | STUDYX | RP | 2324P0002 | 1 | INABORTN | Number of Induced Abortions | 0 |  | 0 | 0 |  |  | Y | 1 | SCREENING | 1 | 2009-03-09 | -10 |
| 13 | STUDYX | RP | 2324P0002 | 2 | BRTHLVN | Number of Live Births | 1 |  | 1 | 1 |  |  | Y | 1 | SCREENING | 1 | 2009-03-09 | -10 |
| 14 | STUDYX | RP | 2324P0002 | 3 | PREGNN | Number of Pregnancies | 1 |  | 1 | 1 |  |  | Y | 1 | SCREENING | 1 | 2009-03-09 | -10 |
| 15 | STUDYX | RP | 2324P0002 | 4 | MENOSTAT | Menopause Status | MENOPAUSE |  | MENOPAUSE |  |  |  | Y | 1 | SCREENING | 1 | 2009-03-09 | -10 |
| 16 | STUDYX | RP | 2324P0002 | 5 | MENOAGE | Menopause Age | 55 | YEARS | 55 | 55 | YEARS |  | Y | 1 | SCREENING | 1 | 2009-03-09 | -10 |
| 17 | STUDYX | RP | 2324P0002 | 6 | MENARAGE | Menarche Age | 11 | YEARS | 11 | 11 | YEARS |  | Y | 1 | SCREENING | 1 | 2009-03-09 | -10 |
| 18 | STUDYX | RP | 2324P0002 | 7 | BCMETHOD | Birth Control Method | DIAPHRAGM |  | DIAPHRAGM |  |  | P3Y | Y | 1 | SCREENING | 1 | 2009-03-09 | -10 |
| 19 | STUDYX | RP | 2324P0002 | 8 | CHILDPOT | Childbearing Potential | N |  | N |  |  |  | Y | 1 | SCREENING | 1 | 2009-03-09 | -10 |
| 20 | STUDYX | RP | 2324P0002 | 9 | CHILDPOT | Childbearing Potential | N |  | N |  |  |  |  | 2 | Day 1 | 1 | 2009-03-19 | 1 |
| 21 | STUDYX | RP | 2324P0002 | 10 | CHILDPOT | Childbearing Potential | N |  | N |  |  |  |  | 3 | Day 29 | 29 | 2009-04-16 | 29 |

#### 6.3.7.7 Respiratory System Findings (RE)

##### RE – Description/Overview
A findings domain that contains physiological and morphological findings related to the respiratory system, including the organs that are involved in breathing such as the nose, throat, larynx, trachea, bronchi and lungs.

##### RE – Specification
re.xpt, Respiratory System Findings — Findings. One record per finding or result per time point per visit per subject, Tabulation.

**Structure:** One record per finding or result per time point per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | RE |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |
| 5 | RESEQ | Sequence Number | Num | Identifier | Req |  |
| 6 | REGRPID | Group ID | Char | Identifier | Perm |  |
| 7 | REREFID | Reference ID | Char | Identifier | Perm |  |
| 8 | RESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 9 | RELNKID | Link ID | Char | Identifier | Perm |  |
| 10 | RELNKGRP | Link Group | Char | Identifier | Perm |  |
| 11 | RETESTCD | Short Name of Respiratory Test | Char | Topic | Req | C111106 |
| 12 | RETEST | Name of Respiratory Test | Char | Synonym Qualifier | Req | C111107 |
| 13 | RECAT | Category for Respiratory Test | Char | Grouping Qualifier | Perm |  |
| 14 | RESCAT | Subcategory for Respiratory Test | Char | Grouping Qualifier | Perm |  |
| 15 | REPOS | Position of Subject During Observation | Char | Record Qualifier | Perm | C71148 |
| 16 | REORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 17 | REORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 18 | REORREF | Reference Result in Original Units | Char | Variable Qualifier | Perm |  |
| 19 | RESTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 20 | RESTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 21 | RESTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 22 | RESTREFC | Character Reference Result | Char | Variable Qualifier | Perm |  |
| 23 | RESTREFN | Numeric Reference Result in Std Units | Num | Variable Qualifier | Perm |  |
| 24 | RESTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 25 | REREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 26 | RELOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |
| 27 | RELAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| 28 | REDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| 29 | REMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 30 | RELOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 31 | REBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 32 | REDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 33 | REEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 34 | REEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| 35 | REREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |
| 36 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 37 | VISIT | Visit Name | Char | Timing | Perm |  |
| 38 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 39 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 40 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 41 | REDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 42 | REDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |
| 43 | RETPT | Planned Time Point Name | Char | Timing | Perm |  |
| 44 | RETPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 45 | REELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 46 | RETPTREF | Time Point Reference | Char | Timing | Perm |  |
| 47 | RERFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SPDEVID**: Sponsor-defined identifier for a device.
- **RESEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.
- **REGRPID**: Optional group identifier, used to link together a block of related records within a subject in a domain.
- **REREFID**: Optional internal or external procedure identifier.
- **RESPID**: Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.
- **RELNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.
- **RELNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **RETESTCD**: Short name of the measurement, test, or examination. It can be used as a column name when converting a dataset from a vertical format to a horizontal format. The value in RETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). RETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "FEV1", "FVC".
- **RETEST**: Verbatim name of the test or examination used to obtain the measurement or finding. The value in RETEST cannot be longer than 40 characters. Examples: "Forced Expiratory Volume in 1 Second", "Forced Vital Capacity".
- **RECAT**: Used to categorize observations across subjects.
- **RESCAT**: A further categorization.
- **REPOS**: Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".
- **REORRES**: Result of the procedure measurement or finding as originally received or collected.
- **REORRESU**: Original units in which the data were collected. The unit for REORRES and REORREF.
- **REORREF**: Reference result for continuous measurements in original units. Should be collected only for continuous results.
- **RESTRESC**: Contains the result value for all findings, copied or derived from REORRES in a standard format or in standard units. RESTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in RESTRESN.
- **RESTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from RESTRESC. RESTRESN should store all numeric test results or findings.
- **RESTRESU**: Standardized unit used for RESTRESC, RESTRESN and RESTREFN.
- **RESTREFC**: Reference value for the result or finding copied or derived from --ORREF in a standard format.
- **RESTREFN**: Reference result for continuous measurements in standard units. Should be populated only for continuous results.
- **RESTAT**: Used to indicate that a test was not done or a measurement was not taken. Should be null if a result exists in REORRES.
- **REREASND**: Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with RESTAT when value is "NOT DONE".
- **RELOC**: Anatomical location of the subject relevant to the collection of the measurement. Examples: "LUNG", "BRONCHUS".
- **RELAT**: Side of the body used to collect measurement. Examples: "RIGHT", "LEFT".
- **REDIR**: Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".
- **REMETHOD**: Method used to create the result.
- **RELOBXFL**: Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **REBLFL**: Indicator used to identify a baseline value. Should be Y or null. Note that REBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.
- **REDRVFL**: Used to indicate a derived record. Should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If REDRVFL = "Y", then REORRES could be null, with RESTRESC and (if numeric) RESTRESN having the derived value.
- **REEVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".
- **REEVALID**: Used to distinguish multiple evaluators with the same role recorded in REEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2".
- **REREPNUM**: The instance number of a test that is repeated within a given time frame for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Example: multiple measurements of pulmonary function.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the date/time at which the assessment was made.
- **REDTC**: Date/time of procedure or test.
- **REDY**: Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **RETPT**: Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See RETPTNUM and RETPTREF. Examples: "START", "5 MINUTES POST".
- **RETPTNUM**: Numeric version of RETPT to aid in sorting.
- **REELTM**: Planned elapsed time relative to a planned fixed reference (RETPTREF). Not a clock time or a date/time variable, but an interval, represented as ISO duration. Examples: "-PT15M" to represent 15 minutes prior to the reference time point indicated by RETPTREF, "PT8H" to represent 8 hours after the reference time point represented by RETPTREF.
- **RETPTREF**: Description of the fixed reference point referred to by REELTM, RETPTNUM, and RETPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **RERFTDTC**: Date/time for a fixed reference time point defined by RETPTREF.


##### RE – Assumptions
1. The Respiratory System Findings domain is used to represent the results/findings of respiratory diagnostic procedures (e.g., spirometry). Information about the conduct of the procedure(s), if collected, should be submitted in the Procedures (PR) domain.
2. Many respiratory assessments require the use of a device. When data about the device used for an assessment or additional information about its use in the assessment are collected, SPDEVID should be included in the record. See the SDTMIG for Medical Devices (SDTMIG-MD, available at https://www.cdisc.org/standards/foundational/medical-devices-sdtmig/) for further information about SPDEVID and the Device domains.
3. Any Identifier variables, Timing variables, or Findings general observation class qualifiers may be added to the RE domain, but the following qualifiers would generally not be used: --MODIFY, --BODSYS, and --FAST.

##### RE – Examples

**Example 1**
This example shows results from several spirometry tests using either a spirometer or a peak flow meter. When spirometry tests are performed, the subject usually makes several efforts, each of which produces results, but only the best result for each test is used in analyses. In this study, the sponsor collected only the best results. The Device Identifiers (DI) domain was submitted for device identification, and the Device in Use (DU) domain was submitted to provide information about the use of the device.
Because the original and standardized units of measure are identical in this example, RESTRESC, RESTRESN, RESTRESU, and RESTREFN are not shown.
Instead, an ellipsis marks their place in the dataset. Spirometry test values are compared to a predicted value, rather than a normal range. Predicted values are represented in REORREF.
**Rows 1-2:** Show the results for the spirometry tests FEV1 and FVC, with the predicted values in REORREF. The spirometer used in the tests is identified by the SPDEVID.
**Rows 3-4:** Show the results for FEV1 and FVC as percentages of the predicted values. This result is output by the spirometer device, not derived by the sponsor. REORREF is null as there are no reference results for percent predicted tests.
**Row 5:** Shows the results of the PEF test with the predicted values in REORREF. These results were obtained with a different device, a peak flow meter, identified by the SPDEVID.


*re.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | RESEQ | RETESTCD | RETEST | REORRES | REORRESU | REORREF | ... | VISITNUM | VISIT | REDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | RE | XYZ-001-001 | ABC001 | 1 | FEV1 | Forced Expiratory Volume in 1 Second | 2.73 | L | 3.37 |  | 2 | VISIT 2 | 2013-06-30 |
| 2 | XYZ | RE | XYZ-001-001 | ABC001 | 2 | FVC | Forced Vital Capacity | 3.91 | L | 3.86 |  | 2 | VISIT 2 | 2013-06-30 |
| 3 | XYZ | RE | XYZ-001-001 | ABC001 | 3 | FEV1PP | Percent Predicted FEV1 | 81 | % |  |  | 2 | VISIT 2 | 2013-06-30 |
| 4 | XYZ | RE | XYZ-001-001 | ABC001 | 4 | FVCPP | Percent Predicted Forced Vital Capacity | 101.3 | % |  |  | 2 | VISIT 2 | 2013-06-30 |
| 5 | XYZ | RE | XYZ-001-001 | DEF999 | 5 | PEF | Peak Expiratory Flow | 6.11 | L/s | 7.33 |  | 4 | VISIT 4 | 2013-07-17 |

The DI domain provides the information needed to distinguish among devices used in the study. In this example, the only parameter needed to establish identifiers was the device type.

*di.xpt*

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | DI | ABC001 | 1 | DEVTYPE | Device Type | SPIROMETER |
| 2 | XYZ | DI | DEF999 | 1 | DEVTYPE | Device Type | PEAK FLOW METER |

The DU domain shows settings used on the devices with identifier "ABC001". The device was set to use the NHANES III reference equation. Because this setting was the same for all uses of the device for all subjects, USUBJID is null.

*du.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | DUSEQ | DUTESTCD | DUTEST | DUORRES |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | DU |  | ABC001 | 1 | SPIREFEQ | Spirometric Reference Equation | NATIONAL HEALTH NUTRITION EXAMINATION SURVEY (NHANES) III |

**Example 2**
In this example, a subject made 4 attempts at the FEV1 pulmonary function test, and data about all attempts were collected. It is standard practice for multiple attempts to be made, and for the best result to be used in analyses. In this example, the spirometry report included an indicator of which was the best result. The spirometry report also included an indicator that 1 of the attempts was considered to have produced an inadequate result, with the reasons the result was considered inadequate.
**Rows 1-3:** Show individual test results for FEV1 as measured by spirometry.
**Row 4:** Shows an individual test result for FEV1 as measured by spirometry. Note that this result is much less than the others.

*re.xpt*

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | RESEQ | RETESTCD | RETEST | REORRES | REORRESU | RESTRESN | RESTRESU | REREPNUM | VISITNUM | VISIT | REDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | RE | XYZ-001-001 | ABC001 | 1 | FEV1 | Forced Expiratory Volume in 1 Second | 1.94 | L | 1.94 | L | 1 | 2 | VISIT 2 | 2013-04-23 |
| 2 | XYZ | RE | XYZ-001-001 | ABC001 | 2 | FEV1 | Forced Expiratory Volume in 1 Second | 1.88 | L | 1.88 | L | 2 | 2 | VISIT 2 | 2013-04-23 |
| 3 | XYZ | RE | XYZ-001-001 | ABC001 | 3 | FEV1 | Forced Expiratory Volume in 1 Second | 1.88 | L | 1.88 | L | 3 | 2 | VISIT 2 | 2013-04-23 |
| 4 | XYZ | RE | XYZ-001-001 | ABC001 | 4 | FEV1 | Forced Expiratory Volume in 1 Second | 1.57 | L | 1.57 | L | 4 | 2 | VISIT 2 | 2013-04-23 |

Supplemental qualifiers were used to indicate which was the best result and to provide information on the attempt that was considered to produce inadequate results.
**Row 1:** Shows the record with RESEQ="1" was the best test result, indicated by BRESFL="Y".
**Rows 2-4:** The presence of a flag, IRESFL, indicates that the data were inadequate. The 2 reasons why this was the case are represented by QNAM="IRREA1" and "IREEA2".

*suppre.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | RE | XYZ-001-001 | RESEQ | 1 | REBRESFL | Best Result Flag | Y | CRF |  |
| 2 | XYZ | RE | XYZ-001-001 | RESEQ | 4 | REIRESFL | Inadequate Results Flag | Y | CRF |  |
| 3 | XYZ | RE | XYZ-001-001 | RESEQ | 4 | REIRREA1 | Inadequate Result Reason 1 | COUGHING WAS DETECTED IN THE FIRST PART OF THE EXPIRATION | CRF |  |
| 4 | XYZ | RE | XYZ-001-001 | RESEQ | 4 | REIRREA2 | Inadequate Result Reason 2 | FEV1 REPEATABILITY IS UNACCEPTABLE | CRF |  |

DI was used to represent the device type that was used to perform for the pulmonary function tests.

*di.xpt*

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | DI | ABC001 | 1 | DEVTYPE | Device Type | SPIROMETER |

#### 6.3.7.8 Urinary System Findings (UR)

##### UR – Description/Overview
A findings domain that contains physiological and morphological findings related to the urinary tract, including the organs involved in the creation and excretion of urine such as the kidneys, ureters, bladder and urethra.

##### UR – Specification
ur.xpt, Urinary System Findings — Findings. One record per finding per location per visit per subject, Tabulation.

**Structure:** One record per finding per location per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | UR |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | URSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | URGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | URREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | URSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | URLNKID | Link ID | Char | Identifier | Perm |  |
| 9 | URLNKGRP | Link Group ID | Char | Identifier | Perm |  |
| 10 | URTESTCD | Short Name of Urinary Test | Char | Topic | Req | C129942 |
| 11 | URTEST | Name of Urinary Test | Char | Synonym Qualifier | Req | C129941 |
| 12 | URTSTDTL | Urinary Test Detail | Char | Variable Qualifier | Perm |  |
| 13 | URCAT | Category for Urinary Test | Char | Grouping Qualifier | Perm |  |
| 14 | URSCAT | Subcategory for Urinary Test | Char | Grouping Qualifier | Perm |  |
| 15 | URORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 16 | URORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 17 | URSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 18 | URSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 19 | URSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 20 | URRESCAT | Result Category | Char | Variable Qualifier | Perm |  |
| 21 | URSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 22 | URREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 23 | URLOC | Location Used for the Measurement | Char | Record Qualifier | Perm | C74456 |
| 24 | URLAT | Laterality | Char | Variable Qualifier | Perm | C99073 |
| 25 | URDIR | Directionality | Char | Variable Qualifier | Perm | C99074 |
| 26 | URMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C85492 |
| 27 | URLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 28 | URBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 29 | URDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 30 | UREVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 31 | UREVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| 32 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 33 | VISIT | Visit Name | Char | Timing | Perm |  |
| 34 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 35 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 36 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 37 | URDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 38 | URDY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |
| 39 | URTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 40 | URTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 41 | URELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 42 | URTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 43 | URRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **URSEQ**: Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.
- **URGRPID**: Optional group identifier, used to link together a block of related records within a subject in a domain.
- **URREFID**: Optional internal or external identifier (e.g., lab specimen ID, universally unique identifier (UUID) for a medical image).
- **URSPID**: Sponsor-defined identifier. Example: Preprinted line identifier.
- **URLNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.
- **URLNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **URTESTCD**: Short character value for URTEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in URTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). URTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "COUNT", "LENGTH", "RBLDFLW".
- **URTEST**: Long name For URTESTCD. Examples: "Count", "Length", "Renal Blood Flow".
- **URTSTDTL**: Further description of URTESTCD and URTEST.
- **URCAT**: Used to define a category of topic-variable values.
- **URSCAT**: Used to define a further categorization of URCAT values.
- **URORRES**: Result of the measurement or finding as originally received or collected.
- **URORRESU**: Unit for URORRES.
- **URSTRESC**: Contains the result value for all findings copied or derived from URORRES, in a standard format or in standard units. URSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in URSTRESN.
- **URSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from URSTRESC. URSTRESN should store all numeric test results or findings.
- **URSTRESU**: Standardized units used for URSTRESC and URSTRESN.
- **URRESCAT**: Used to categorize the result of a finding.
- **URSTAT**: Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".
- **URREASND**: Reason not done. Used in conjunction with URSTAT when value is "NOT DONE".
- **URLOC**: Anatomical location of the subject relevant to the collection of the measurement.
- **URLAT**: Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".
- **URDIR**: Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".
- **URMETHOD**: Method of the test or examination.
- **URLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **URBLFL**: A baseline defined by the sponsor The value should be "Y" or null. Note that URBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.
- **URDRVFL**: Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.
- **UREVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".
- **UREVALID**: Used to distinguish multiple evaluators with the same role recorded in UREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2".
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter.
- **VISITDY**: Planned study day of VISIT. Should be an integer.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the observation was made.
- **EPOCH**: Epoch associated with the date/time at which the observation was made.
- **URDTC**: Collection date and time of an observation.
- **URDY**: Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.
- **URTPT**: Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See URTPTNUM and URTPTREF.
- **URTPTNUM**: Numeric version of planned time point used in sorting.
- **URELTM**: Planned elapsed time relative to a planned fixed reference (URTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.
- **URTPTREF**: Description of the fixed reference point referred to by URELTM, URTPTNUM, and URTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **URRFTDTC**: Date/time for a fixed reference time point defined by URTPTREF.


##### UR – Assumptions
1.  Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the UR domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --NRIND, --LOINC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV, --LLOQ.

##### UR – Examples

**Example 1**
This example shows measurements of the kidney, number of renal arteries and veins, and presence/absence results for prespecified abnormalities of the kidneys.
These findings were made using computed tomography (CT) imaging.
**Row 1:** Shows that the subject's left kidney was measured to be 126 mm long.
**Row 2:** Shows that the subject's left kidney had 2 renal arteries.
**Row 3:** Shows that the subject's left kidney had 1 renal vein.
**Row 4:** Shows that no hematomas were found in the kidney. If a hematoma had been present, the variable URLOC (with URDIR as necessary) would have specified where within the kidney.
**Row 5:** Shows that surgical damage was noted in the superior portion of the kidney cortex. Note that in SDTM, there is no way to clearly distinguish between the use of --LOC as a qualifier of --TEST vs. as a qualifier of results, as it is used here.


*ur.xpt*

| Row | STUDYID | DOMAIN | USUBJID | URSEQ | URTESTCD | URTEST | URORRES | URORRESU | URSTRESC | URSTRESN | URSTRESU | URLOC | URLAT | URDIR | URMETHOD | URDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | UR | ABC-001-011 | 1 | LENGTH | Length | 12.6 | cm | 126 | 126 | mm | KIDNEY | LEFT |  | CT SCAN | 2016-03-30 |
| 2 | ABC | UR | ABC-001-011 | 2 | RNLANUM | Number of Renal Arteries | 2 |  | 2 | 2 |  | KIDNEY | LEFT |  | CT SCAN | 2016-03-30 |
| 3 | ABC | UR | ABC-001-011 | 3 | RNLVNUM | Number of Renal Veins | 1 |  | 1 | 1 |  | KIDNEY | LEFT |  | CT SCAN | 2016-03-30 |
| 4 | ABC | UR | ABC-001-011 | 4 | HEMAIND | Hematoma Indicator | N |  | N |  |  | KIDNEY |  |  | CT SCAN | 2016-03-30 |
| 5 | ABC | UR | ABC-001-011 | 5 | SGDMGIND | Surgical Damage Indicator | Y |  | Y |  |  | KIDNEY, CORTEX | LEFT | SUPERIOR | CT SCAN | 2016-03-30 |

**Example 2**
This example shows a subject's renal blood flow measurement for each visit based on the subject's para-amino hippuric acid (PAH) clearance, indicated by URMETHOD = "PARA-AMINO HIPPURIC ACID CLEARANCE".

*ur.xpt*

| Row | STUDYID | DOMAIN | USUBJID | URSEQ | URTESTCD | URTEST | URORRES | URORRESU | URSTRESC | URSTRESN | URSTRESU | URLOC | URLAT | URMETHOD | VISITNUM | VISIT | URDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | DEF | UR | DEF-0123 | 1 | BLDFLRT | Blood Flow Rate | 20 | mL/min | 20 | 20 | mL/min | KIDNEY | BILATERAL | PARA-AMINO HIPPURIC ACID CLEARANCE | 1 | VISIT 1 | 2016-03-15 |
| 2 | DEF | UR | DEF-0123 | 2 | BLDFLRT | Blood Flow Rate | 10 | mL/min | 10 | 10 | mL/min | KIDNEY | LEFT | PARA-AMINO HIPPURIC ACID CLEARANCE | 2 | VISIT 2 | 2016-03-20 |
| 3 | DEF | UR | DEF-0123 | 3 | BLDFLRT | Blood Flow Rate | 10 | mL/min | 10 | 10 | mL/min | KIDNEY | RIGHT | PARA-AMINO HIPPURIC ACID CLEARANCE | 3 | VISIT 3 | 2016-04-07 |


---

