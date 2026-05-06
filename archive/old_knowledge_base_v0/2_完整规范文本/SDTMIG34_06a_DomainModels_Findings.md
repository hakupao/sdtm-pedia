# SDTMIG v3.4 --- Domain Models: Findings — Part 1

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 1/8 — 6.3.1-6.3.4: DA, DD, EG, IE
> **Original:** `SDTMIG34_06_DomainModels_Findings.md`
> **Related:** `SDTMIG34_06b_DomainModels_Findings.md`, `SDTMIG34_06c_DomainModels_Findings.md`, `SDTMIG34_06d_DomainModels_Findings.md`, `SDTMIG34_06e_DomainModels_Findings.md`, `SDTMIG34_06f_DomainModels_Findings.md`, `SDTMIG34_06g_DomainModels_Findings.md`, `SDTMIG34_06h_DomainModels_Findings.md`

---

## 6.3 Models for Findings Domains

Most subject-level observations collected during the study should be represented according to one of the 3 SDTM general observation classes. The following domains correspond to the Findings class:


---

### 6.3.1 Product Accountability (DA)

#### DA – Description/Overview
A findings domain that contains the accountability of study products, such as information on the receipt, dispensing, return, and packaging.

#### DA – Specification
da.xpt, Product Accountability — Findings. One record per product accountability finding per subject, Tabulation.

**Structure:** One record per product accountability finding per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | DA |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | DASEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | DAGRPID | Group ID | Char | Identifier | Perm |  |
| 6 | DAREFID | Reference ID | Char | Identifier | Perm |  |
| 7 | DASPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 8 | DALNKID | Link ID | Char | Identifier | Perm |  |
| 9 | DALNKGRP | Link Group ID | Char | Identifier | Perm |  |
| 10 | DATESTCD | Short Name of Accountability Assessment | Char | Topic | Req | C78732 |
| 11 | DATEST | Name of Accountability Assessment | Char | Synonym Qualifier | Req | C78731 |
| 12 | DACAT | Category | Char | Grouping Qualifier | Perm |  |
| 13 | DASCAT | Subcategory | Char | Grouping Qualifier | Perm |  |
| 14 | DAORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 15 | DAORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 16 | DASTRESC | Result or Finding in Standard Format | Char | Result Qualifier | Exp |  |
| 17 | DASTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 18 | DASTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 19 | DASTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 20 | DAREASND | Reason Not Done | Char | Record Qualifier | Perm |  |
| 21 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 22 | VISIT | Visit Name | Char | Timing | Perm |  |
| 23 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 24 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 25 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 26 | DADTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 27 | DADY | Study Day of Visit/Collection/Exam | Num | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study within the submission.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **DASEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **DAGRPID**: Used to tie together a block of related records in a single domain for a subject.
- **DAREFID**: Optional internal or external identifier such as a code from the product packaging (e.g., bottle label, package label, kit label).
- **DASPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Examples: Line number on the Product Accountability CRF page, a code from the product packaging (e.g., bottle label, package label, kit label).
- **DALNKID**: Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.
- **DALNKGRP**: Identifier used to link related records across domains. This will usually be a many-to-one relationship.
- **DATESTCD**: Short character value for DATEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters and cannot begin with a number or contain characters other than letters, numbers, or underscores. Examples: "DISPAMT", "RETAMT".
- **DATEST**: Verbatim name corresponding to the topic variable of the test or examination used to obtain the product accountability assessment. The value in DATEST cannot be longer than 40 characters. Examples: "Dispensed Amount", "Returned Amount".
- **DACAT**: Used to define a category of topic-variable values. Examples: "STUDY MEDICATION", "RESCUE MEDICATION".
- **DASCAT**: Used to define a further categorization level for a group of related records.
- **DAORRES**: Result of the product accountability assessment as originally received or collected.
- **DAORRESU**: Unit for DAORRES.
- **DASTRESC**: Contains the result value for all product accountability assessments copied or derived from DAORRES, in a standard format or in standard units. DASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in DASTRESN.
- **DASTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from DASTRESC. DASTRESN should store all numeric test results or findings.
- **DASTRESU**: Standardized units used for DASTRESC and DASTRESN.
- **DASTAT**: Used to indicate that a product accountability assessment was not done. Should be null or have a value of "NOT DONE".
- **DAREASND**: Reason not done. Used in conjunction with DASTAT when value is "NOT DONE".
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit, based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm (see Section 7.2.1, Trial Arms).
- **EPOCH**: Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.
- **DADTC**: Date and time of the product accountability assessment represented in ISO 8601 character format.
- **DADY**: Study day of product accountability assessment, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC in Demographics.


#### DA – Assumptions

1. This domain records the amount of study product transferred to or from the study subject.

    a. Transfers of devices are not represented in this domain, but in the Device Tracking and Disposition (DT) domain. See the SDTMIG for Medical Devices.

    b. For drugs, transfers are usually recorded using the tests "Dispensed Amount" and "Returned Amount".

    c. Test terminology for other products may be different; for example, for nutrition, the tests might be "Prepared Amount" and "Unused Amount"
2. DACAT may be used to differentiate transfers of different groups of products (e.g., rescue medications vs. investigational medications).
3. DAREFID and DASPID are both available for capturing label information.
4. The following qualifiers would not generally be used in DA: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --NAM, --LOINC, --SPEC, --SPCCND, --METHOD, --BLFL, --FAST, --DRVRL, --TOX, --TOXGR, --SEV.

#### DA – Examples

**Example 1**
This example shows drug accounting for a study with 2 study medications and one rescue medication, all of which were measured in tablets. The sponsor chose to add EPOCH from the list of timing variables and to use DASPID and DAREFID for code numbers that appeared on the label.

*da.xpt*

| Row | STUDYID | DOMAIN | USUBJID | DASEQ | DAREFID | DASPID | DATESTCD | DATEST | DACAT | DASCAT | DAORRES | DAORRESU | DASTRESC | DASTRESN | DASTRESU | VISITNUM | EPOCH | DADTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | DA | ABC-01001 | 1 | XBYCC-E990A | A375827 | DISPAMT | Dispensed Amount | Study Medication | Bottle A | 30 | TABLET | 30 | 30 | TABLET | 1 | Study Med Period 1 | 2004-06-15 |
| 2 | ABC | DA | ABC-01001 | 2 | XBYCC-E990A | A375827 | RETAMT | Returned Amount | Study Medication | Bottle A | 5 | TABLET | 5 | 5 | TABLET | 2 | Study Med Period 1 | 2004-07-15 |
| 3 | ABC | DA | ABC-01001 | 3 | XBYCC-E990B | A227588 | DISPAMT | Dispensed Amount | Study Medication | Bottle B | 15 | TABLET | 15 | 15 | TABLET | 1 | Study Med Period 1 | 2004-06-15 |
| 4 | ABC | DA | ABC-01001 | 4 | XBYCC-E990B | A227588 | RETAMT | Returned Amount | Study Medication | Bottle B | 0 | TABLET | 0 | 0 | TABLET | 2 | Study Med Period 1 | 2004-07-15 |
| 5 | ABC | DA | ABC-01001 | 5 |  |  | DISPAMT | Dispensed Amount | Rescue Medication |  | 10 | TABLET | 10 | 10 | TABLET | 1 | Study Med Period 1 | 2004-06-15 |
| 6 | ABC | DA | ABC-01001 | 6 |  |  | RETAMT | Returned Amount | Rescue Medication |  | 10 | TABLET | 10 | 10 | TABLET | 2 | Study Med Period 1 | 2004-07-15 |

**Example 2**
This example shows drug containers (rather than contents) being accounted for. The sponsor did not track returns. The purpose was to verify containers dispensed were consistent with randomization. DASPID records the identifying number of the container.

*da.xpt*

| Row | STUDYID | DOMAIN | USUBJID | DASEQ | DASPID | DATESTCD | DATEST | DACAT | DASCAT | DAORRES | DAORRESU | DASTRESC | DASTRESN | DASTRESU | VISITNUM | DADTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | DA | ABC-01001 | 1 | AB001 | DISPAMT | Dispensed Amount | Study Medication | Drug A | 1 | CONTAINER | 1 | 1 | CONTAINER | 1 | 2004-06-15 |
| 2 | ABC | DA | ABC-01001 | 2 | AB002 | DISPAMT | Dispensed Amount | Study Medication | Drug B | 1 | CONTAINER | 1 | 1 | CONTAINER | 1 | 2004-06-15 |

**Example 3**
This example shows a nutrition study where the volume of infant feeding formula prepared and the volume remaining after feeding are tracked.

**Rows 1-2:** Volume of formula prepared and left after feeding for the first feed of the diary (day 1).
**Rows 3-4:** Volume of formula prepared and left after feeding for the second feed of the diary (day 1).
**Rows 5-6:** Volume of formula prepared and left after feeding for the third feed of the diary (day 2).

*da.xpt*

| Row | STUDYID | DOMAIN | USUBJID | DASEQ | DAGRPID | DASPID | DATESTCD | DATEST | DACAT | DAORRES | DAORRESU | DASTRESC | DASTRESN | DASTRESU | DADTC | DADY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | DA | 101 | 1 | 1 | 1 | PREPAMT | Prepared Amount | Study Product | 100 | mL | 100 | 100 | mL | 2017-05-19 | 1 |
| 2 | ABC | DA | 101 | 2 | 1 | 1 | REMAMT | Remaining Amount | Study Product | 15 | mL | 15 | 15 | mL | 2017-05-19 | 1 |
| 3 | ABC | DA | 101 | 3 | 2 | 2 | PREPAMT | Prepared Amount | Study Product | 100 | mL | 100 | 100 | mL | 2017-05-19 | 1 |
| 4 | ABC | DA | 101 | 4 | 2 | 2 | REMAMT | Remaining Amount | Study Product | 25 | mL | 25 | 25 | mL | 2017-05-19 | 1 |
| 5 | ABC | DA | 101 | 5 | 3 | 1 | PREPAMT | Prepared Amount | Study Product | 100 | mL | 100 | 100 | mL | 2017-05-20 | 2 |
| 6 | ABC | DA | 101 | 6 | 3 | 1 | REMAMT | Remaining Amount | Study Product | 10 | mL | 10 | 10 | mL | 2017-05-20 | 2 |


---

### 6.3.2 Death Details (DD)

#### DD – Description/Overview
A findings domain that contains the diagnosis of the cause of death for a subject.
The domain is designed to hold supplemental data that are typically collected when a death occurs, such as the official cause of death. It does not replace existing data such as serious adverse event details in AE. Further, it does not introduce a new requirement to collect information that is not already indicated as good clinical practice or defined in regulatory guidelines. Instead, it provides a consistent place within the SDTM to hold information that previously did not have a clearly defined home.

#### DD – Specification
dd.xpt, Death Details — Findings. One record per finding per subject, Tabulation.

**Structure:** One record per finding per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | DD |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | DDSEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | DDTESTCD | Death Detail Assessment Short Name | Char | Topic | Req | C116108 |
| 6 | DDTEST | Death Detail Assessment Name | Char | Synonym Qualifier | Req | C116107 |
| 7 | DDORRES | Result or Finding as Collected | Char | Result Qualifier | Exp |  |
| 8 | DDSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp |  |
| 9 | DDRESCAT | Result Category | Char | Variable Qualifier | Perm |  |
| 10 | DDEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 11 | DDDTC | Date/Time of Collection | Char | Timing | Exp | ISO 8601 datetime or interval |
| 12 | DDDY | Study Day of Collection | Num | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **DDSEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **DDTESTCD**: Short name of the measurement, test, or examination described in DDTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in DDTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). DDTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRCDTH", "SECDTH".
- **DDTEST**: Long name for DDTESTCD. The value in DDTEST cannot be longer than 40 characters. Examples: "Primary Cause of Death", "Secondary Cause of Death".
- **DDORRES**: Result of the test defined in DDTEST, as originally received or collected.
- **DDSTRESC**: Contains the result or finding copied or derived from DDORRES in a standard format.
- **DDRESCAT**: Used to categorize the result of a finding. Examples: "TREATMENT RELATED", "NONTREATMENT RELATED", "UNDETERMINED", "ACCIDENTAL".
- **DDEVAL**: Role of the person who provided the evaluation.
- **DDDTC**: Date/time of collection of the diagnosis or other death assessment data in ISO 8601 format. This is not necessarily the date of death.
- **DDDY**: Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.


#### DD – Assumptions
1. There may be more than 1 cause of death. If so, these may be separated into primary and secondary causes and/or other appropriate designations. DD may also include other details about the death, such as where the death occurred and whether it was witnessed.
2. Death details are typically collected on designated CRF pages. The DD domain is not intended to collate data that are collected in standard variables in other domains, such as AE.AEOUT (Outcome of Adverse Event), AE.AESDTH (Results in Death) or DS.DSTERM (Reported Term for the Disposition Event). Data from other domains that relates to the death can be linked to DD using RELREC.
3. This domain is not intended to include data obtained from autopsy. An autopsy is a procedure from which there will usually be findings. Autopsy information should be handled as per recommendations in the Procedures (PR) domain.
4. There are separate codelists for DD tests and responses. Associations between the DD tests and response codelists are described in the DD codetable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).
5. Any identifiers, timing variables, or findings general observation-class qualifiers may be added to the DD domain, but the following qualifiers would not generally be used: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --NAM, --LOINC, -- SPEC, --SPCCND, --LOBXFL, --BLFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV.

#### DD – Examples

**Example 1**
This example shows the primary cause of death for 3 subjects. The CRF also collected the location of the subject’s death and a secondary cause of death.

**Rows 1-2:** Show the primary cause of death and location of death for a subject. DDDTC is the date of assessment.
**Rows 3-4:** Show records for primary cause of death and location of death for another subject for whom the information was not known.
**Rows 5-7:** Show primary and secondary cause of death and location of death for a third subject.

*dd.xpt*

| Row | STUDYID | DOMAIN | USUBJID | DDSEQ | DDTESTCD | DDTEST | DDORRES | DDSTRESC | DDDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | DD | ABC12301001 | 1 | PRCDTH | Primary Cause of Death | SUDDEN CARDIAC DEATH | SUDDEN CARDIAC DEATH | 2011-01-12 |
| 2 | ABC123 | DD | ABC12301001 | 2 | LOCDTH | Location of Death | HOME | HOME | 2011-01-12 |
| 3 | ABC123 | DD | ABC12301002 | 1 | PRCDTH | Primary Cause of Death | UNKNOWN | UNKNOWN | 2011-03-15 |
| 4 | ABC123 | DD | ABC12301002 | 2 | LOCDTH | Location of Death | UNKNOWN | UNKNOWN | 2011-03-15 |
| 5 | ABC123 | DD | ABC12301023 | 1 | PRCDTH | Primary Cause of Death | CARDIAC ARRHYTHMIA | CARDIAC ARRHYTHMIA | 2011-09-09 |
| 6 | ABC123 | DD | ABC12301023 | 2 | SECDTH | Secondary Cause of Death | CHF | CONGESTIVE HEART FAILURE | 2011-09-09 |
| 7 | ABC123 | DD | ABC12301023 | 3 | LOCDTH | Location of Death | MEMORIAL HOSPITAL | HOSPITAL | 2011-09-09 |

**Example 2**
This example illustrates how the DD, Disposition (DS), and AE data for a subject were linked using RELREC. Note that each of these domains serves a different purpose, even though the information is related. This subject had a fatal adverse event, represented in the AE domain.

*ae.xpt*

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AESTDTC | AEENDTC | AEDECOD | AEBODSYS | AEOUT | AESER | AESDTH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | AE | ABC12301001 | 6 | SUDDEN CARDIAC DEATH | 2011-01-10 | 2011-01-10 | SUDDEN CARDIAC DEATH | CARDIOVASCULAR SYSTEM | FATAL | Y | Y |

The primary cause of death was collected and is represented in DD. In this case, the result for primary cause of death is the same as the term in the AE record.

*dd.xpt*

| Row | STUDYID | DOMAIN | USUBJID | DDSEQ | DDTESTCD | DDTEST | DDORRES | DDSTRESC | DDDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | DD | ABC12301001 | 1 | PRCDTH | Primary Cause of Death | SUDDEN CARDIAC DEATH | SUDDEN CARDIAC DEATH | 2011-01-12 |

The subject’s death is also represented in the DS domain as the reason for withdrawal from the study.

**Rows 1-2:** Show typical protocol milestones and disposition events.
**Row 3:** Shows the date the death event occurred (DSSTDTC) and was recorded (DSDTC).

*ds.xpt*

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSDTC | DSSTDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | DS | ABC12301001 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | 2011-01-02 | 2011-01-02 |
| 2 | ABC123 | DS | ABC12301001 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | 2011-01-03 | 2011-01-03 |
| 3 | ABC123 | DS | ABC12301001 | 3 | SUDDEN CARDIAC DEATH | DEATH | DISPOSITION EVENT | 2011-01-10 | 2011-01-10 |

The relationship between the DS, AE, and DD records that reflect the subject’s death is represented in RELREC.

*relrec.xpt*

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | DS | ABC12301001 | DSSEQ | 3 |  | 1 |
| 2 | ABC123 | AE | ABC12301001 | AESEQ | 6 |  | 1 |
| 3 | ABC123 | DD | ABC12301001 | DDSEQ | 1 |  | 1 |


---

### 6.3.3 ECG Test Results (EG)

#### EG – Description/Overview
A findings domain that contains ECG data, including position of the subject, method of evaluation, all cycle measurements and all findings from the ECG including an overall interpretation if collected or derived.

#### EG – Specification
eg.xpt, ECG Test Results — Findings. One record per ECG observation per replicate per time point or one record per ECG observation per beat per visit per subject, Tabulation.

**Structure:** One record per ECG observation per replicate per time point or one record per ECG observation per beat per visit per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | EG |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier | Perm |  |
| 5 | EGSEQ | Sequence Number | Num | Identifier | Req |  |
| 6 | EGGRPID | Group ID | Char | Identifier | Perm |  |
| 7 | EGREFID | ECG Reference ID | Char | Identifier | Perm |  |
| 8 | EGSPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 9 | EGBEATNO | ECG Beat Number | Num | Identifier | Perm |  |
| 10 | EGTESTCD | ECG Test or Examination Short Name | Char | Topic | Req | C71153; C120523 |
| 11 | EGTEST | ECG Test or Examination Name | Char | Synonym Qualifier | Req | C71152; C120524 |
| 12 | EGCAT | Category for ECG | Char | Grouping Qualifier | Perm |  |
| 13 | EGSCAT | Subcategory for ECG | Char | Grouping Qualifier | Perm |  |
| 14 | EGPOS | ECG Position of Subject | Char | Record Qualifier | Perm | C71148 |
| 15 | EGORRES | Result or Finding in Original Units | Char | Result Qualifier | Exp |  |
| 16 | EGORRESU | Original Units | Char | Variable Qualifier | Perm | C71620 |
| 17 | EGSTRESC | Character Result/Finding in Std Format | Char | Result Qualifier | Exp | C71150; C120522; C101834 |
| 18 | EGSTRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Perm |  |
| 19 | EGSTRESU | Standard Units | Char | Variable Qualifier | Perm | C71620 |
| 20 | EGSTAT | Completion Status | Char | Record Qualifier | Perm | C66789 |
| 21 | EGREASND | Reason ECG Not Done | Char | Record Qualifier | Perm |  |
| 22 | EGXFN | ECG External File Path | Char | Record Qualifier | Perm |  |
| 23 | EGNAM | Vendor Name | Char | Record Qualifier | Perm |  |
| 24 | EGMETHOD | Method of Test or Examination | Char | Record Qualifier | Perm | C71151 |
| 25 | EGLEAD | Lead Location Used for Measurement | Char | Record Qualifier | Perm | C90013 |
| 26 | EGLOBXFL | Last Observation Before Exposure Flag | Char | Record Qualifier | Exp | C66742 |
| 27 | EGBLFL | Baseline Flag | Char | Record Qualifier | Perm | C66742 |
| 28 | EGDRVFL | Derived Flag | Char | Record Qualifier | Perm | C66742 |
| 29 | EGEVAL | Evaluator | Char | Record Qualifier | Perm | C78735 |
| 30 | EGEVALID | Evaluator Identifier | Char | Variable Qualifier | Perm | C96777 |
| 31 | EGCLSIG | Clinically Significant, Collected | Char | Record Qualifier | Perm | C66742 |
| 32 | EGREPNUM | Repetition Number | Num | Record Qualifier | Perm |  |
| 33 | VISITNUM | Visit Number | Num | Timing | Exp |  |
| 34 | VISIT | Visit Name | Char | Timing | Perm |  |
| 35 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 36 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 37 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 38 | EGDTC | Date/Time of ECG | Char | Timing | Exp | ISO 8601 datetime or interval |
| 39 | EGDY | Study Day of ECG | Num | Timing | Perm |  |
| 40 | EGTPT | Planned Time Point Name | Char | Timing | Perm |  |
| 41 | EGTPTNUM | Planned Time Point Number | Num | Timing | Perm |  |
| 42 | EGELTM | Planned Elapsed Time from Time Point Ref | Char | Timing | Perm | ISO 8601 duration |
| 43 | EGTPTREF | Time Point Reference | Char | Timing | Perm |  |
| 44 | EGRFTDTC | Date/Time of Reference Time Point | Char | Timing | Perm | ISO 8601 datetime or interval |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SPDEVID**: Sponsor-defined identifier for a device.
- **EGSEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **EGGRPID**: Used to tie together a block of related records in a single domain for a subject.
- **EGREFID**: Internal or external ECG identifier. Example: "334PT89".
- **EGSPID**: Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the ECG page.
- **EGBEATNO**: A sequence number that identifies the beat within an ECG.
- **EGTESTCD**: Short name of the measurement, test, or examination described in EGTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in EGTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). EGTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRAG", "QRSAG".; Test codes are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTESTCD) and one 1 tests based on Holter monitoring (HETESTCD).
- **EGTEST**: Verbatim name of the test or examination used to obtain the measurement or finding. The value in EGTEST cannot be longer than 40 characters. Examples: "PR Interval, Aggregate", "QRS Duration, Aggregate".; Test names are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTEST) and 1 for tests based on Holter monitoring (HETEST).
- **EGCAT**: Used to categorize ECG observations across subjects. Examples: "MEASUREMENT", "FINDING", "INTERVAL".
- **EGSCAT**: A further categorization of the ECG.
- **EGPOS**: Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".
- **EGORRES**: Result of the ECG measurement or finding as originally received or collected. Examples of expected values are "62" or "0.151" when the result is an interval or measurement, or "ATRIAL FIBRILLATION" or "QT PROLONGATION" when the result is a finding.
- **EGORRESU**: Original units in which the data were collected. The unit for EGORRES. Examples: "sec", "msec".
- **EGSTRESC**: Contains the result value for all findings copied or derived from EGORRES, in a standard format or standard units. EGSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in EGSTRESN. For example, if a test has results of 62 beats/min, then EGORRES = "62", EGORRESU = "beats/min", EGSTRESC = "62", EGSTRESN = 62, and EGSTRESU = "beats/min" . For other examples, see Original and Standardized Results. Additional examples of result data: "SINUS BRADYCARDIA", "ATRIAL FLUTTER", "ATRIAL FIBRILLATION".; Test results are in 3 separate codelists: EGSTRESC for abnormal test results based on regular 10-second ECGs; HESTRESC for abnormal test results based on Holter monitoring, and NORMABNM for generic test results and/or responses to EGTEST = "Interpretation".
- **EGSTRESN**: Used for continuous or numeric results or findings in standard format; copied in numeric format from EGSTRESC. EGSTRESN should store all numeric test results or findings.
- **EGSTRESU**: Standardized units used for EGSTRESC and EGSTRESN.
- **EGSTAT**: Used to indicate an ECG was not done, or an ECG measurement was not taken. Should be null if a result exists in EGORRES.
- **EGREASND**: Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with EGSTAT when value is "NOT DONE".
- **EGXFN**: File name and path for the external ECG waveform file.
- **EGNAM**: Name or identifier of the laboratory or vendor providing the test results.
- **EGMETHOD**: Method of the ECG test. Example: "12-LEAD STANDARD".
- **EGLEAD**: The lead used for the measurement. Examples: "LEAD 1", "LEAD 2", "LEAD rV2", "LEAD V1".
- **EGLOBXFL**: Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.
- **EGBLFL**: Indicator used to identify a baseline value. Should be "Y" or null. Note that EGBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.
- **EGDRVFL**: Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If EGDRVFL="Y", then EGORRES could be null, with EGSTRESC and EGSTRESN (if the result is numeric) having the derived value.
- **EGEVAL**: Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR".
- **EGEVALID**: Used to distinguish multiple evaluators with the same role recorded in EGEVAL. Examples: "RADIOLOGIST 1" or "RADIOLOGIST 2".
- **EGCLSIG**: Used to indicate whether a collected observation is clinically significant based on judgment.
- **EGREPNUM**: The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the date/time at which the assessment was made.
- **EGDTC**: Date/Time of ECG.
- **EGDY**: Study day of the ECG, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
- **EGTPT**: Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EGTPTNUM and EGTPTREF. Examples: "Start", "5 min post".
- **EGTPTNUM**: Numerical version of EGTPT to aid in sorting.
- **EGELTM**: Planned elapsed time (in ISO 8601) relative to a fixed time point reference (EGTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by EGTPTREF.
- **EGTPTREF**: Name of the fixed reference point referred to by EGELTM, EGTPTNUM, and EGTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".
- **EGRFTDTC**: Date/time for a fixed reference time point defined by EGTPTREF.


#### EG – Assumptions
1. EGREFID is intended to store an identifier (e.g., UUID) for the associated ECG tracing. EGXFN is intended to store the name of and path to the electrocardiogram (ECG) waveform file when it is submitted.
2. There are separate codelists for tests and results based on regular 10-second ECGs and for tests and results based on Holter monitoring.
    a. Associations between some ECG abnormality tests and response codelists are described in the ECG codetable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).
3. For non-individual ECG beat data and for aggregate ECG parameter results (e.g., "QT interval", "RR", "PR", "QRS"), EGREFID is populated for all unique ECGs, so that submitted SDTM data can be matched to the actual ECGs stored in the ECG warehouse. Therefore, this variable is expected for these types of records.
4. For individual-beat parameter results, waveform data will not be stored in the warehouse, so there will be no associated identifier for these beats.
5. The method for QT interval correction is specified in the test name by controlled terminology: EGTESTCD = "QTCFAG" and EGTEST = "QTcF Interval, Aggregate" is used for Fridericia's formula; EGTESTCD = "QTCBAG" and EGTEST = "QTcB Interval, Aggregate", is used for Bazett's formula.
6. EGBEATNO is used to differentiate between beats in beat-to-beat records.
7. EGREPNUM is used to differentiate between multiple repetitions of a test within a given time frame.
8. EGNRIND can be added to indicate where a result falls with respect to reference range defined by EGORNRLO and EGORNRHI. Examples: "HIGH", "LOW". Clinical significance would be represented as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data, in EGCLSIG (see also EG Example 1).
9. When "QTcF Interval, Aggregate" or "QTcB Interval, Aggregate" is derived by the sponsor, the derived flag (EGDRVFL) is set to "Y". However, when the "QTcF Interval, Aggregate" or "QTcB Interval, Aggregate" is received from a central provider or vendor, the value would go into EGORRES and EGDRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).
10. If this domain is used in conjunction with the ECG QT Correction Model Data (QT) domain:
    a. For each QT correction method used in the study, values of EGTESTCD and EGTEST are assigned at the study level.
    b. The sponsor should assign values for EGTESTCD/EGTEST appropriately with clear documentation on what each test code represents. For example, if the protocol calls for computing the top two best fit models, the sponsor could choose to name the top best fit model QTCIAG1 and the second best fit model QTCIAG2, in rank order.
11. Any identifiers, timing variables, or findings general observation-class qualifiers may be added to the EG domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --SPEC, --SPCCND, --FAST, --SEV. It is recommended that --LOINC not be used.

#### EG – Examples

**Example 1**
This example shows ECG measurements and other findings from one ECG for one subject. EGCAT has been used to group tests.

**Row 1:** Shows a measurement of ventricular rate. This result was assessed as not clinically significant (EGCLSIG = “N”).
**Row 2:** Shows a measurement of PR interval. This result was assessed as clinically significant (EGCLSIG = “Y”).
**Rows 2-4:** These interval measurements were collected in seconds. However, in this submission, the standard unit for these tests was milliseconds, so the results have been converted in EGSTRESC and EGSTRESN.
**Rows 5-6:** Show “QTcB Interval, Aggregate” and “QTcF Interval, Aggregate”. These results were derived by the sponsor, as indicated by the “Y” in the EGDRVFL column. Note that EGORRES is null for these derived records.
**Rows 7-10:** Show results from tests looking for certain kinds of abnormalities, which have been grouped using EGCAT = “FINDINGS”.
**Row 11:** Shows a technical problem represented as the result of the test “Technical Quality”. Results of this test can be important to the overall understanding of an ECG, but are not truly findings or interpretations about the subject's heart function.
**Row 12:** Shows the result of the TEST “Interpretation” (i.e., the interpretation of the ECG strip as a whole), which for this ECG was “ABNORMAL”.

*eg.xpt*

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGREFID | EGTESTCD | EGTEST | EGCAT | EGPOS | EGORRES | EGORRESU | EGSTRESC | EGSTRESN | EGSTRESU | EGXFN | EGNAM | EGLOBXFL | EGDRVFL | EGCLSIG | VISITNUM | VISIT | EGDTC | EGDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | EG | XYZ-US-701-002 | 1 | 334PT89 | EGHRMN | ECG Mean Heart Rate | MEASUREMENT | SUPINE | 62 | beats/min | 62 | 62 | beats/min | PQW436789-07.xml | Test Lab |  |  | N | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 2 | XYZ | EG | XYZ-US-701-002 | 2 | 334PT89 | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 0.15 | sec | 150 | 150 | msec | PQW436789-07.xml | Test Lab |  |  | Y | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 3 | XYZ | EG | XYZ-US-701-002 | 3 | 334PT89 | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 0.103 | sec | 103 | 103 | msec | PQW436789-07.xml | Test Lab |  |  |  | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 4 | XYZ | EG | XYZ-US-701-002 | 4 | 334PT89 | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 0.406 | sec | 406 | 406 | msec | PQW436789-07.xml | Test Lab |  |  |  | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 5 | XYZ | EG | XYZ-US-701-002 | 5 | 334PT89 | QTCBAG | QTcB Interval, Aggregate | INTERVAL | SUPINE |  |  | 469 | 469 | msec | PQW436789-07.xml | Test Lab |  | Y |  | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 6 | XYZ | EG | XYZ-US-701-002 | 6 | 334PT89 | QTCFAG | QTcF Interval, Aggregate | INTERVAL | SUPINE |  |  | 446 | 446 | msec | PQW436789-07.xml | Test Lab |  | Y |  | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 7 | XYZ | EG | XYZ-US-701-002 | 7 | 334PT89 | SPRTARRY | Supraventricular Tachyarrhythmias | FINDING | SUPINE | ATRIAL FIBRILLATION |  | ATRIAL FIBRILLATION |  |  | PQW436789-07.xml | Test Lab |  |  |  | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 8 | XYZ | EG | XYZ-US-701-002 | 8 | 334PT89 | SPRTARRY | Supraventricular Tachyarrhythmias | FINDING | SUPINE | ATRIAL FLUTTER |  | ATRIAL FLUTTER |  |  | PQW436789-07.xml | Test Lab |  |  |  | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 9 | XYZ | EG | XYZ-US-701-002 | 9 | 334PT89 | STSTWUW | ST Segment, T wave, and U wave | FINDING | SUPINE | PROLONGED QT |  | PROLONGED QT |  |  | PQW436789-07.xml | Test Lab |  |  |  | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 10 | XYZ | EG | XYZ-US-701-002 | 10 | 334PT89 | CHYPTENL | Chamber Hypertrophy or Enlargement | FINDING | SUPINE | LEFT VENTRICULAR HYPERTROPHY |  | LEFT VENTRICULAR HYPERTROPHY |  |  | PQW436789-07.xml | Test Lab |  |  |  | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 11 | XYZ | EG | XYZ-US-701-002 | 11 | 334PT89 | TECHQUAL | Technical Quality |  | SUPINE | OTHER INCORRECT ELECTRODE PLACEMENT |  | OTHER INCORRECT ELECTRODE PLACEMENT |  |  | PQW436789-07.xml | Test Lab |  |  |  | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
| 12 | XYZ | EG | XYZ-US-701-002 | 12 | 334PT89 | INTP | Interpretation |  | SUPINE | ABNORMAL |  | ABNORMAL |  |  |  |  |  |  |  | 1 | Screening 1 | 2003-04-15T11:58 | -36 |

**Example 2**
This example shows ECG results where only the overall assessment was collected. Results are for one subject across multiple visits. In addition, the ECG interpretation was provided by the investigator and, when necessary, by a cardiologist. EGGRPID is used to group the overall assessments collected on each ECG.

**Rows 1-3:** Show interpretations performed by the principal investigator on three different occasions. The ECG at Visit “SCREEN II” has been flagged as the last observation before start of study treatment.
**Rows 4-5:** Show interpretations of the same ECG by both the investigator and a cardiologist. EGGRPID has been used to group these two records to emphasize their relationship.

*eg.xpt*

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGGRPID | EGTESTCD | EGTEST | EGPOS | EGORRES | EGSTRESC | EGSTRESN | EGLOBXFL | EGEVAL | VISITNUM | VISIT | VISITDY | EGDTC | EGDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC | EG | ABC-99-CA-456 | 1 |  | INTP | Interpretation | SUPINE | NORMAL | NORMAL |  |  | PRINCIPAL INVESTIGATOR | 1 | SCREEN I | -2 | 2003-11-26 | -2 |
| 2 | ABC | EG | ABC-99-CA-456 | 2 |  | INTP | Interpretation | SUPINE | ABNORMAL | ABNORMAL |  | Y | PRINCIPAL INVESTIGATOR | 2 | SCREEN II | -1 | 2003-11-27 | -1 |
| 3 | ABC | EG | ABC-99-CA-456 | 3 |  | INTP | Interpretation | SUPINE | ABNORMAL | ABNORMAL |  |  | PRINCIPAL INVESTIGATOR | 3 | DAY 10 | 10 | 2003-12-07T09:02 | 10 |
| 4 | ABC | EG | ABC-99-CA-456 | 4 | Comp 1 | INTP | Interpretation | SUPINE | ABNORMAL | ABNORMAL |  |  | PRINCIPAL INVESTIGATOR | 4 | DAY 15 | 15 | 2003-12-12 | 15 |
| 5 | ABC | EG | ABC-99-CA-456 | 5 | Comp 1 | INTP | Interpretation | SUPINE | ABNORMAL | ABNORMAL |  |  | CARDIOLOGIST | 4 | DAY 15 | 15 | 2003-12-12 | 15 |

**Example 3**
This example shows 10-second ECG replicates extracted from a continuous recording. The example shows one subject's extracted 10-second ECG replicate results. Three replicates were extracted for planned time points “1 HR” and “2 HR”; EGREPNUM is used to identify the replicates. Summary mean measurements are reported for the 10 seconds of extracted data for each replicate. EGDTC is the date/time of the first individual beat in the extracted 10-second ECG. In order to save space, some permissible variables (EGREFID, VISITDY, EGTPTNUM, EGTPTREF, EGRFTDTC) have been omitted, as marked by ellipses.

*eg.xpt*

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | ... | EGTESTCD | EGTEST | EGCAT | EGPOS | EGORRES | EGORRESU | EGSTRESC | EGSTRESN | EGSTRESU | EGMETHOD | EGLEAD | EGLOBXFL | VISITNUM | VISIT | EGDTC | EGTPT | ... | EGREPNUM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | STUDY01 | EG | 2324-P0001 | 1 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
| 2 | STUDY01 | EG | 2324-P0001 | 2 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 658 | msec | 658 | 658 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
| 3 | STUDY01 | EG | 2324-P0001 | 3 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 97 | msec | 97 | 97 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
| 4 | STUDY01 | EG | 2324-P0001 | 4 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 440 | msec | 440 | 440 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
| 5 | STUDY01 | EG | 2324-P0001 | 5 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | ... | 2 |
| 6 | STUDY01 | EG | 2324-P0001 | 6 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 679 | msec | 679 | 679 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | ... | 2 |
| 7 | STUDY01 | EG | 2324-P0001 | 7 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 95 | msec | 95 | 95 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | ... | 2 |
| 8 | STUDY01 | EG | 2324-P0001 | 8 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 389 | msec | 389 | 389 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | ... | 2 |
| 9 | STUDY01 | EG | 2324-P0001 | 9 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 169 | msec | 169 | 169 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:02:14 | 1 HR | ... | 3 |
| 10 | STUDY01 | EG | 2324-P0001 | 10 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 661 | msec | 661 | 661 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:02:14 | 1 HR | ... | 3 |
| 11 | STUDY01 | EG | 2324-P0001 | 11 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 90 | msec | 90 | 90 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:02:14 | 1 HR | ... | 3 |
| 12 | STUDY01 | EG | 2324-P0001 | 12 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 377 | msec | 377 | 377 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T10:02:14 | 1 HR | ... | 3 |
| 13 | STUDY01 | EG | 2324-P0001 | 13 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:00:21 | 2 HR | ... | 1 |
| 14 | STUDY01 | EG | 2324-P0001 | 14 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 771 | msec | 771 | 771 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:00:21 | 2 HR | ... | 1 |
| 15 | STUDY01 | EG | 2324-P0001 | 15 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 100 | msec | 100 | 100 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:00:21 | 2 HR | ... | 1 |
| 16 | STUDY01 | EG | 2324-P0001 | 16 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 379 | msec | 379 | 379 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:00:21 | 2 HR | ... | 1 |
| 17 | STUDY01 | EG | 2324-P0001 | 17 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 179 | msec | 179 | 179 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:01:31 | 2 HR | ... | 2 |
| 18 | STUDY01 | EG | 2324-P0001 | 18 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 749 | msec | 749 | 749 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:01:31 | 2 HR | ... | 2 |
| 19 | STUDY01 | EG | 2324-P0001 | 19 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 103 | msec | 103 | 103 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:01:31 | 2 HR | ... | 2 |
| 20 | STUDY01 | EG | 2324-P0001 | 20 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 402 | msec | 402 | 402 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:01:31 | 2 HR | ... | 2 |
| 21 | STUDY01 | EG | 2324-P0001 | 21 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 175 | msec | 175 | 175 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:02:40 | 2 HR | ... | 3 |
| 22 | STUDY01 | EG | 2324-P0001 | 22 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 771 | msec | 771 | 771 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:02:40 | 2 HR | ... | 3 |
| 23 | STUDY01 | EG | 2324-P0001 | 23 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 98 | msec | 98 | 98 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:02:40 | 2 HR | ... | 3 |
| 24 | STUDY01 | EG | 2324-P0001 | 24 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 356 | msec | 356 | 356 | msec | 12 LEAD STANDARD | LEAD II |  | 2 | VISIT 2 | 2014-03-22T11:02:40 | 2 HR | ... | 3 |

**Example 4**
The example shows one subject's continuous beat-to-beat EG results. Only 3 beats are shown, but there could be measurements for, as an example, 101,000 complexes in 24 hours. The actual number of complexes in 24 hours can be variable and depends on average heart rate. The results are mapped to the EG domain using EGBEATNO. If there is no result to be reported, then the row would not be included.

**Rows 1-2:** Show the first beat recorded. The first beat was considered to be the beat for which the recording contained a complete P-wave. It was assigned EGBEATNO = “1”. There is no RR measurement for this beat because RR is measured as the duration (time) between the peak of the R-wave in the reported single beat and peak of the R-wave in the preceding single beat, and the partial recording that preceded EGBEATNO = “1” did not contain an R-wave. EGDTC was the date/time of the individual beat.
**Rows 3-5:** EGBEATNO = “2” had an RR measurement, since the R-wave of the preceding beat (EGBEATNO = “1”) was recorded.
**Rows 6-8:** There is a 1-hour gap between beats 2 and 3 due to electrical interference or other artifacts that prevented measurements from being recorded. Note that EGBEATNO = “3” does have an RR measurement because the partial beat preceding EGBEATNO = “3” contained an R-wave.

*eg.xpt*

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGBEATNO | EGTESTCD | EGTEST | EGCAT | EGPOS | EGORRES | EGORRESU | EGSTRESC | EGSTRESN | EGSTRESU | EGMETHOD | EGLEAD | EGLOBXFL | VISITNUM | VISIT | VISITDY | EGDTC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | STUDY01 | EG | 2324-P0001 | 1 | 1 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II |  | 1 | SCREENING | -7 | 2014-02-11T14:32:12.3 |
| 2 | STUDY01 | EG | 2324-P0001 | 2 | 1 | QRSSB | QRS Duration, Single Beat | INTERVAL | SUPINE | 97 | msec | 97 | 97 | msec | 12 LEAD STANDARD | LEAD II |  | 1 | SCREENING | -7 | 2014-02-11T14:32:12.3 |
| 3 | STUDY01 | EG | 2324-P0001 | 3 | 2 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II |  | 1 | SCREENING | -7 | 2014-02-11T14:32:13.3 |
| 4 | STUDY01 | EG | 2324-P0001 | 4 | 2 | RRSM | RR Interval, Single Measurement | INTERVAL | SUPINE | 679 | msec | 679 | 679 | msec | 12 LEAD STANDARD | LEAD II |  | 1 | SCREENING | -7 | 2014-02-11T14:32:13.3 |
| 5 | STUDY01 | EG | 2324-P0001 | 5 | 2 | QRSSB | QRS Duration, Single Beat | INTERVAL | SUPINE | 95 | msec | 95 | 95 | msec | 12 LEAD STANDARD | LEAD II |  | 1 | SCREENING | -7 | 2014-02-11T14:32:13.3 |
| 6 | STUDY01 | EG | 2324-P0001 | 6 | 3 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 169 | msec | 169 | 169 | msec | 12 LEAD STANDARD | LEAD II |  | 1 | SCREENING | -7 | 2014-02-11T15:32:14.2 |
| 7 | STUDY01 | EG | 2324-P0001 | 7 | 3 | RRSM | RR Interval, Single Measurement | INTERVAL | SUPINE | 661 | msec | 661 | 661 | msec | 12 LEAD STANDARD | LEAD II |  | 1 | SCREENING | -7 | 2014-02-11T15:32:14.2 |
| 8 | STUDY01 | EG | 2324-P0001 | 8 | 3 | QRSSB | QRS Duration, Single Beat | INTERVAL | SUPINE | 90 | msec | 90 | 90 | msec | 12 LEAD STANDARD | LEAD II |  | 1 | SCREENING | -7 | 2014-02-11T15:32:14.2 |


---

### 6.3.4 Inclusion/Exclusion Criteria Not Met (IE)

#### IE – Description/Overview
A findings domain that contains those criteria that cause the subject to be in violation of the inclusion/exclusion criteria.

#### IE – Specification
ie.xpt, Inclusion/Exclusion Criteria Not Met — Findings. One record per inclusion/exclusion criterion not met per subject, Tabulation.

**Structure:** One record per inclusion/exclusion criterion not met per subject
**Class:** Findings

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | IE |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier | Req |  |
| 4 | IESEQ | Sequence Number | Num | Identifier | Req |  |
| 5 | IESPID | Sponsor-Defined Identifier | Char | Identifier | Perm |  |
| 6 | IETESTCD | Inclusion/Exclusion Criterion Short Name | Char | Topic | Req |  |
| 7 | IETEST | Inclusion/Exclusion Criterion | Char | Synonym Qualifier | Req |  |
| 8 | IECAT | Inclusion/Exclusion Category | Char | Grouping Qualifier | Req | C66797 |
| 9 | IESCAT | Inclusion/Exclusion Subcategory | Char | Grouping Qualifier | Perm |  |
| 10 | IEORRES | I/E Criterion Original Result | Char | Result Qualifier | Req | C66742 |
| 11 | IESTRESC | I/E Criterion Result in Std Format | Char | Result Qualifier | Req | C66742 |
| 12 | VISITNUM | Visit Number | Num | Timing | Perm |  |
| 13 | VISIT | Visit Name | Char | Timing | Perm |  |
| 14 | VISITDY | Planned Study Day of Visit | Num | Timing | Perm |  |
| 15 | TAETORD | Planned Order of Element within Arm | Num | Timing | Perm |  |
| 16 | EPOCH | Epoch | Char | Timing | Perm | C99079 |
| 17 | IEDTC | Date/Time of Collection | Char | Timing | Perm | ISO 8601 datetime or interval |
| 18 | IEDY | Study Day of Collection | Num | Timing | Perm |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **USUBJID**: Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **IESEQ**: Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.
- **IESPID**: Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Inclusion or exclusion criteria number from CRF.
- **IETESTCD**: Short name of the criterion described in IETEST. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "IN01", "EX01".
- **IETEST**: Verbatim description of the inclusion or exclusion criterion that was the exception for the subject within the study. IETEST cannot be longer than 200 characters.
- **IECAT**: Used to define a category of related records across subjects.
- **IESCAT**: A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or for to categorize as a major or minor exceptions. Examples: "MAJOR", "MINOR".
- **IEORRES**: Original response to inclusion/exclusion criterion question, i.e., whether the inclusion or exclusion criterion was met.
- **IESTRESC**: Response to inclusion/exclusion criterion result, in standard format.
- **VISITNUM**: Clinical encounter number. Numeric version of VISIT, used for sorting.
- **VISIT**: Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: Planned study day of the visit based upon RFSTDTC in Demographics.
- **TAETORD**: Number that gives the planned order of the element within the arm for the element in which the assessment was made.
- **EPOCH**: Epoch associated with the observation date/time of the inclusion/exclusion finding.
- **IEDTC**: Collection date and time of the inclusion/exclusion criterion represented in ISO 8601 character format.
- **IEDY**: Study day of collection of the inclusion/exclusion exceptions, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.


#### IE – Assumptions
1. The intent of the IE domain model is to collect responses to only those criteria that the subject did not meet, and not the responses to all criteria. For the complete list of inclusion/exclusion criteria, see Section 7.4.1, Trial Inclusion/Exclusion Criteria.
2. This domain should be used to document the exceptions to inclusion or exclusion criteria at the time that eligibility for study entry is determined (e.g., at the end of a run-in period or immediately before randomization). This domain should not be used to collect protocol deviations/violations incurred during the course of the study, typically after randomization or start of study medication. See Section 6.2.7, Protocol Deviations, for the model that is used to submit protocol deviations/violations.
3. IETEST is to be used only for the verbatim description of the inclusion or exclusion criteria. If the text is no more than 200 characters, it goes in IETEST; if the text is more than 200 characters, put meaningful text in IETEST and describe the full text in the study metadata. See Section 4.5.3.1, Test Name (--TEST) Greater than 40 Characters, for further information.
4. The following qualifiers would generally not be used in IE: --MODIFY, --POS, --BODSYS, --ORRESU, --ORNRLO, --ORNRHI, --STRESN, --STRESU, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --NAM, --LOINC, --SPEC, --SPCCND, --LOC, --METHOD, --BLFL, --LOBXFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV, --STAT.

#### IE – Examples

**Example 1**
This example shows records for 3 subjects who failed to meet all inclusion/exclusion criteria but who were included in the study.

**Rows 1-2:** Show data for a subject with 2 inclusion/exclusion exceptions.
**Rows 3-4:** Show data for 2 other subjects, both of whom failed the same inclusion criterion.

*ie.xpt*

| Row | STUDYID | DOMAIN | USUBJID | IESEQ | IESPID | IETESTCD | IETEST | IECAT | IEORRES | IESTRESC | VISITNUM | VISIT | VISITDY | IEDTC | IEDY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | IE | XYZ-0007 | 1 | 17 | EXCL17 | Ventricular Rate | EXCLUSION | Y | Y | 1 | WEEK -8 | -56 | 1999-01-10 | -58 |
| 2 | XYZ | IE | XYZ-0007 | 2 | 3 | INCL03 | Acceptable mammogram from local radiologist? | INCLUSION | N | N | 1 | WEEK -8 | -56 | 1999-01-10 | -58 |
| 3 | XYZ | IE | XYZ-0047 | 1 | 3 | INCL03 | Acceptable mammogram from local radiologist? | INCLUSION | N | N | 1 | WEEK -8 | -56 | 1999-01-12 | -56 |
| 4 | XYZ | IE | XYZ-0096 | 1 | 3 | INCL03 | Acceptable mammogram from local radiologist? | INCLUSION | N | N | 1 | WEEK -8 | -56 | 1999-01-13 | -55 |


---

