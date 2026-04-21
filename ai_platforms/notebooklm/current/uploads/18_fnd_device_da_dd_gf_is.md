# 18_fnd_device_da_dd_gf_is

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `18`
> - **Concept**: Findings: DA (drug accountability) + DD (death details) + GF (genomic findings) + IS (immunogen)
> - **Merged files**: 12
> - **Words**: 22,622
> - **Chars**: 140,100
> - **Sources**:
>   - `domains/DA/spec.md`
>   - `domains/DA/assumptions.md`
>   - `domains/DA/examples.md`
>   - `domains/DD/spec.md`
>   - `domains/DD/assumptions.md`
>   - `domains/DD/examples.md`
>   - `domains/GF/spec.md`
>   - `domains/GF/assumptions.md`
>   - `domains/GF/examples.md`
>   - `domains/IS/spec.md`
>   - `domains/IS/assumptions.md`
>   - `domains/IS/examples.md`

---
## Source: `domains/DA/spec.md`

# DA — Product Accountability

> Class: Findings | Structure: One record per product accountability finding per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study within the submission.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### DASEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### DAGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### DAREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier such as a code from the product packaging (e.g., bottle label, package label, kit label).

### DASPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Examples: Line number on the Product Accountability CRF page, a code from the product packaging (e.g., bottle label, package label, kit label).

### DALNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### DALNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### DATESTCD
- **Order:** 10
- **Label:** Short Name of Accountability Assessment
- **Type:** Char
- **Controlled Terms:** C78732
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for DATEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters and cannot begin with a number or contain characters other than letters, numbers, or underscores. Examples: "DISPAMT", "RETAMT".

### DATEST
- **Order:** 11
- **Label:** Name of Accountability Assessment
- **Type:** Char
- **Controlled Terms:** C78731
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name corresponding to the topic variable of the test or examination used to obtain the product accountability assessment. The value in DATEST cannot be longer than 40 characters. Examples: "Dispensed Amount", "Returned Amount".

### DACAT
- **Order:** 12
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Examples: "STUDY MEDICATION", "RESCUE MEDICATION".

### DASCAT
- **Order:** 13
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization level for a group of related records.

### DAORRES
- **Order:** 14
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the product accountability assessment as originally received or collected.

### DAORRESU
- **Order:** 15
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for DAORRES.

### DASTRESC
- **Order:** 16
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all product accountability assessments copied or derived from DAORRES, in a standard format or in standard units. DASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in DASTRESN.

### DASTRESN
- **Order:** 17
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from DASTRESC. DASTRESN should store all numeric test results or findings.

### DASTRESU
- **Order:** 18
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for DASTRESC and DASTRESN.

### DASTAT
- **Order:** 19
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a product accountability assessment was not done. Should be null or have a value of "NOT DONE".

### DAREASND
- **Order:** 20
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with DASTAT when value is "NOT DONE".

### VISITNUM
- **Order:** 21
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 22
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 23
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit, based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 24
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm (see Section 7.2.1, Trial Arms).

### EPOCH
- **Order:** 25
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### DADTC
- **Order:** 26
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of the product accountability assessment represented in ISO 8601 character format.

### DADY
- **Order:** 27
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of product accountability assessment, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC in Demographics.
---

## Cross References

### Controlled Terminology
- [Not Done (C66789)](../../terminology/core/general_part4.md) — DASTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — DAORRESU, DASTRESU
- [Drug Accountability Test Name (C78731)](../../terminology/core/other_part1.md) — DATEST
- [Drug Accountability Test Code (C78732)](../../terminology/core/other_part1.md) — DATESTCD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

## Source: `domains/DA/assumptions.md`

# DA — Assumptions

1. This domain records the amount of study product transferred to or from the study subject.
   a. Transfers of devices are not represented in this domain, but in the Device Tracking and Disposition (DT) domain. See the SDTMIG for Medical Devices (available at https://www.cdisc.org/standards/foundational/medical-devices-sdtmig/).
   b. For drugs, transfers are usually recorded using the tests "Dispensed Amount" and "Returned Amount".
   c. Test terminology for other products may be different; for example, for nutrition, the tests might be "Prepared Amount" and "Unused Amount".

2. DACAT may be used to differentiate transfers of different groups of products (e.g., rescue medications vs. investigational medications).

3. DAREFID and DASPID are both available for capturing label information.

4. The following qualifiers would not generally be used in DA: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --NAM, --LOINC, --SPEC, --SPCCND, --METHOD, --BLFL, --FAST, --DRVRL, --TOX, --TOXGR, --SEV.

## Source: `domains/DA/examples.md`

# DA — Examples

## Example 1

This example shows drug accounting for a study with 2 study medications and one rescue medication, all of which were measured in tablets. The sponsor chose to add EPOCH from the list of timing variables and to use DASPID and DAREFID for code numbers that appeared on the label.

**da.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DASEQ | DAREFID | DASPID | DATESTCD | DATEST | DACAT | DASCAT | DAORRES | DAORRESU | DASTRESC | DASTRESN | DASTRESU | VISITNUM | EPOCH | DADTC |
|-----|---------|--------|---------|-------|---------|--------|----------|--------|-------|--------|---------|----------|----------|----------|----------|----------|-------|-------|
| 1 | ABC | DA | ABC-01001 | 1 | XBYCC-E990A | A375827 | DISPAMT | Dispensed Amount | Study Medication | Bottle A | 30 | TABLET | 30 | 30 | TABLET | 1 | Study Med Period 1 | 2004-06-15 |
| 2 | ABC | DA | ABC-01001 | 2 | XBYCC-E990A | A375827 | RETAMT | Returned Amount | Study Medication | Bottle A | 5 | TABLET | 5 | 5 | TABLET | 2 | Study Med Period 1 | 2004-07-15 |
| 3 | ABC | DA | ABC-01001 | 3 | XBYCC-E990B | A227588 | DISPAMT | Dispensed Amount | Study Medication | Bottle B | 15 | TABLET | 15 | 15 | TABLET | 1 | Study Med Period 1 | 2004-06-15 |
| 4 | ABC | DA | ABC-01001 | 4 | XBYCC-E990B | A227588 | RETAMT | Returned Amount | Study Medication | Bottle B | 0 | TABLET | 0 | 0 | TABLET | 2 | Study Med Period 1 | 2004-07-15 |
| 5 | ABC | DA | ABC-01001 | 5 | | | DISPAMT | Dispensed Amount | Rescue Medication | | | 10 | TABLET | 10 | TABLET | 1 | | 2004-06-15 |
| 6 | ABC | DA | ABC-01001 | 6 | | | RETAMT | Returned Amount | Rescue Medication | | | 10 | TABLET | 10 | TABLET | 2 | | 2004-07-15 |

## Example 2

In this study, drug containers, rather than their contents, were being accounted for and the sponsor did not track returns. In this case, the purpose of accountability tracking is to verify that the containers dispensed were consistent with the randomization. The sponsor chose to use DASPID to record the identifying number of the container dispensed.

**da.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DASEQ | DASPID | DATESTCD | DATEST | DACAT | DASCAT | DAORRES | DAORRESU | DASTRESC | DASTRESN | DASTRESU | VISITNUM | DADTC |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|--------|---------|----------|----------|----------|----------|----------|-------|
| 1 | ABC | DA | ABC-01001 | 1 | AB001 | DISPAMT | Dispensed Amount | Study Medication | Drug A | 1 | CONTAINER | 1 | 1 | CONTAINER | 1 | 2004-06-15 |
| 2 | ABC | DA | ABC-01001 | 2 | AB002 | DISPAMT | Dispensed Amount | Study Medication | Drug B | 1 | CONTAINER | 1 | 1 | CONTAINER | 1 | 2004-06-15 |

## Example 3

This example shows, for a nutrition study, the volume of infant feeding formula prepared and the volume remaining after feeding.

**Rows 1-2:** Show the volume of formula prepared and the volume of formula left after feeding for the first feed of the diary (day 1).

**Rows 3-4:** Show the volume of formula prepared and the volume of formula left after feeding for the second feed of the diary (day 1).

**Rows 5-6:** Show the volume of formula prepared and the volume of formula left after feeding for the third feed of the diary (day 2).

**da.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DASEQ | DAGRPID | DASPID | DATESTCD | DATEST | DACAT | DAORRES | DAORRESU | DASTRESC | DASTRESN | DASTRESU | DADTC | DADY |
|-----|---------|--------|---------|-------|---------|--------|----------|--------|-------|---------|----------|----------|----------|----------|-------|------|
| 1 | ABC | DA | 101 | 1 | 1 | 1 | PREPAMT | Prepared Amount | Study Product | 100 | mL | 100 | 100 | mL | 2017-05-19 | 1 |
| 2 | ABC | DA | 101 | 2 | 1 | 1 | REMAMT | Remaining Amount | Study Product | 15 | mL | 15 | 15 | mL | 2017-05-19 | 1 |
| 3 | ABC | DA | 101 | 3 | 2 | 2 | PREPAMT | Prepared Amount | Study Product | 100 | mL | 100 | 100 | mL | 2017-05-19 | 1 |
| 4 | ABC | DA | 101 | 4 | 2 | 2 | REMAMT | Remaining Amount | Study Product | 25 | mL | 25 | 25 | mL | 2017-05-19 | 1 |
| 5 | ABC | DA | 101 | 5 | 3 | 1 | PREPAMT | Prepared Amount | Study Product | 100 | mL | 100 | 100 | mL | 2017-05-20 | 2 |
| 6 | ABC | DA | 101 | 6 | 3 | 1 | REMAMT | Remaining Amount | Study Product | 10 | mL | 10 | 10 | mL | 2017-05-20 | 2 |

## Source: `domains/DD/spec.md`

# DD — Death Details

> Class: Findings | Structure: One record per finding per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### DDSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### DDTESTCD
- **Order:** 5
- **Label:** Death Detail Assessment Short Name
- **Type:** Char
- **Controlled Terms:** C116108
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in DDTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in DDTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). DDTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRCDTH", "SECDTH".

### DDTEST
- **Order:** 6
- **Label:** Death Detail Assessment Name
- **Type:** Char
- **Controlled Terms:** C116107
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for DDTESTCD. The value in DDTEST cannot be longer than 40 characters. Examples: "Primary Cause of Death", "Secondary Cause of Death".

### DDORRES
- **Order:** 7
- **Label:** Result or Finding as Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the test defined in DDTEST, as originally received or collected.

### DDSTRESC
- **Order:** 8
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result or finding copied or derived from DDORRES in a standard format.

### DDRESCAT
- **Order:** 9
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding. Examples: "TREATMENT RELATED", "NONTREATMENT RELATED", "UNDETERMINED", "ACCIDENTAL".

### DDEVAL
- **Order:** 10
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation.

### DDDTC
- **Order:** 11
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of collection of the diagnosis or other death assessment data in ISO 8601 format. This is not necessarily the date of death.

### DDDY
- **Order:** 12
- **Label:** Study Day of Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.
---

## Cross References

### Controlled Terminology
- [SDTM Death Diagnosis and Details Test Name (C116107)](../../terminology/core/other_part4.md) — DDTEST
- [SDTM Death Diagnosis and Details Test Code (C116108)](../../terminology/core/other_part4.md) — DDTESTCD
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — DDEVAL

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

## Source: `domains/DD/assumptions.md`

# DD — Assumptions

1. There may be more than 1 cause of death. If so, these may be separated into primary and secondary causes and/or other appropriate designations. DD may also include other details about the death, such as where the death occurred and whether it was witnessed.

2. Death details are typically collected on designated CRF pages. The DD domain is not intended to collate data that are collected in standard variables in other domains, such as AE.AEOUT (Outcome of Adverse Event), AE.AESDTH (Results in Death) or DS.DSTERM (Reported Term for the Disposition Event). Data from other domains that relates to the death can be linked to DD using RELREC.

3. This domain is not intended to include data obtained from autopsy. An autopsy is a procedure from which there will usually be findings. Autopsy information should be handled as per recommendations in the Procedures (PR) domain.

4. There are separate codelists for DD tests and responses. Associations between the DD tests and response codelists are described in the DD codeable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).

5. Any identifiers, timing variables, or findings general observation-class qualifiers may be added to the DD domain, but the following qualifiers would not generally be used: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --NAM, --LOINC, --SPEC, --SPCCND, --LOBXFL, --BLFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV.

## Source: `domains/DD/examples.md`

# DD — Examples

## Example 1

This example shows the primary cause of death for 3 subjects. The CRF also collected the location of the subject's death and a secondary cause of death.

**Rows 1-2:** Show the primary cause of death and location of death for a subject. DDDTC is the date of assessment.

**Rows 3-4:** Show records for primary cause of death and location of death for another subject for whom the information was not known.

**Rows 5-7:** Show primary and secondary cause of death and location of death for a third subject.

**dd.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DDSEQ | DDTESTCD | DDTEST | DDORRES | DDSTRESC | DDDTC |
|-----|---------|--------|---------|-------|----------|--------|---------|----------|-------|
| 1 | ABC123 | DD | ABC12301001 | 1 | PRCDTH | Primary Cause of Death | SUDDEN CARDIAC DEATH | SUDDEN CARDIAC DEATH | 2011-01-12 |
| 2 | ABC123 | DD | ABC12301001 | 2 | LOCDTH | Location of Death | HOME | HOME | 2011-01-12 |
| 3 | ABC123 | DD | ABC12301002 | 1 | PRCDTH | Primary Cause of Death | UNKNOWN | UNKNOWN | 2011-03-15 |
| 4 | ABC123 | DD | ABC12301002 | 2 | LOCDTH | Location of Death | UNKNOWN | UNKNOWN | 2011-03-15 |
| 5 | ABC123 | DD | ABC12301023 | 1 | PRCDTH | Primary Cause of Death | CARDIAC ARRHYTHMIA | CARDIAC ARRHYTHMIA | 2011-09-09 |
| 6 | ABC123 | DD | ABC12301023 | 2 | SECDTH | Secondary Cause of Death | CHF | CONGESTIVE HEART FAILURE | 2011-09-09 |
| 7 | ABC123 | DD | ABC12301023 | 3 | LOCDTH | Location of Death | MEMORIAL HOSPITAL | HOSPITAL | 2011-09-09 |

## Example 2

This example illustrates how the DD, Disposition (DS), and AE data for a subject were linked using RELREC. Note that each of these domains serves a different purpose, even though the information is related. This subject had a fatal adverse event, represented in the AE domain.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AESTDTC | AEENDTC | AEDECOD | AEBODSYS | AEOUT | AESER | AESDTH |
|-----|---------|--------|---------|-------|--------|---------|---------|---------|----------|-------|-------|--------|
| 1 | ABC123 | AE | ABC12301001 | 6 | SUDDEN CARDIAC DEATH | 2011-01-10 | 2011-01-10 | SUDDEN CARDIAC DEATH | CARDIOVASCULAR SYSTEM | FATAL | Y | Y |

The primary cause of death was collected and is represented in DD. In this case, the result for primary cause of death is the same as the term in the AE record.

**dd.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DDSEQ | DDTESTCD | DDTEST | DDORRES | DDSTRESC | DDDTC |
|-----|---------|--------|---------|-------|----------|--------|---------|----------|-------|
| 1 | ABC123 | DD | ABC12301001 | 1 | PRCDTH | Primary Cause of Death | SUDDEN CARDIAC DEATH | SUDDEN CARDIAC DEATH | 2011-01-12 |

The subject's death is also represented in the DS domain as the reason for withdrawal from the study.

**Rows 1-2:** Show typical protocol milestones and disposition events.

**Row 3:** Shows the date the death event occurred (DSSTDTC) and was recorded (DSDTC).

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSDTC | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|-------|---------|
| 1 | ABC123 | DS | ABC12301001 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | 2011-01-02 | 2011-01-02 |
| 2 | ABC123 | DS | ABC12301001 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | 2011-01-03 | 2011-01-03 |
| 3 | ABC123 | DS | ABC12301001 | 3 | SUDDEN CARDIAC DEATH | DEATH | DISPOSITION EVENT | 2011-01-10 | 2011-01-10 |

The relationship between the DS, AE, and DD records that reflect the subject's death is represented in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC123 | DS | ABC12301001 | DSSEQ | 3 | | 1 |
| 2 | ABC123 | AE | ABC12301001 | AESEQ | 6 | | 1 |
| 3 | ABC123 | DD | ABC12301001 | DDSEQ | 1 | | 1 |

## Source: `domains/GF/spec.md`

# GF — Genomics Findings

> Class: Findings | Structure: One record per finding per observation per biospecimen per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### SPDEVID
- **Order:** 4
- **Label:** Sponsor Device Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a device.

### NHOID
- **Order:** 5
- **Label:** Non-Host Organism Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears.

### GFSEQ
- **Order:** 6
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### GFGRPID
- **Order:** 7
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain.

### GFREFID
- **Order:** 8
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** A unique identifier for the assayed genetic specimen.

### GFSPID
- **Order:** 9
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### GFLNKID
- **Order:** 10
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### GFLNKGRP
- **Order:** 11
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### GFTESTCD
- **Order:** 12
- **Label:** Short Name of Genomic Measurement
- **Type:** Char
- **Controlled Terms:** C181178
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in GFTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in GFTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). GFTESTCD cannot contain characters other than letters, numbers, or underscores.

### GFTEST
- **Order:** 13
- **Label:** Name of Genomic Measurement
- **Type:** Char
- **Controlled Terms:** C181179
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for GFTESTCD. The value in GFTEST cannot be longer than 40 characters.

### GFTSTDTL
- **Order:** 14
- **Label:** Measurement, Test, or Examination Detail
- **Type:** Char
- **Controlled Terms:** C181180
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of a reportable qualifying the assessment in GFTESTCD and GFTEST.

### GFCAT
- **Order:** 15
- **Label:** Category for Genomic Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values.

### GFSCAT
- **Order:** 16
- **Label:** Subcategory for Genomic Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of GFCAT values.

### GFORRES
- **Order:** 17
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### GFORRESU
- **Order:** 18
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for GFORRES.

### GFORREF
- **Order:** 19
- **Label:** Reference Result in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference value for the result or finding as originally received or collected. GFORREF uses the same units as GFORRES, if applicable.

### GFSTRESC
- **Order:** 20
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from GFORRES, in a standard format or in standard units. GFSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in GFSTRESN.

### GFSTRESN
- **Order:** 21
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from GFSTRESC. GFSTRESN should store all numeric test results or findings.

### GFSTRESU
- **Order:** 22
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for GFSTRESC, GFSTRESN, GFSTREFC, and GFSTREFN.

### GFSTREFC
- **Order:** 23
- **Label:** Reference Result in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference value for the result or finding copied or derived from GFORREF in a standard format.

### GFSTREFN
- **Order:** 24
- **Label:** Numeric Reference Result in Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference value for continuous or numeric results or findings in standard format or in standard units. GFSTREFN uses the same units as GFSTRESN, if applicable.

### GFRESCAT
- **Order:** 25
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding.

### GFINHERT
- **Order:** 26
- **Label:** Inheritability
- **Type:** Char
- **Controlled Terms:** C181177
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies whether the variation can be passed to the next generation.

### GFGENREF
- **Order:** 27
- **Label:** Genome Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** An identifier for the genome reference used to generate the reported result. For example, Genome Reference Consortium Human Build 38 patch release 13 may be represented as "GRCh38.p13".

### GFCHROM
- **Order:** 28
- **Label:** Chromosome Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** The designation (name or number) of the chromosome or contig on which the variant or other feature appears (e.g., "17"; "X").

### GFSYM
- **Order:** 29
- **Label:** Genomic Symbol
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A published symbol for the portion of the genome serving as a locus for the experiment/test.

### GFSYMTYP
- **Order:** 30
- **Label:** Genomic Symbol Type
- **Type:** Char
- **Controlled Terms:** C181176
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A description of the type of genomic entity that is represented by the published symbol in GFSYM.

### GFGENLOC
- **Order:** 31
- **Label:** Genetic Location
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Specifies the location within a sequence for the observed value in GFORRES.

### GFGENSR
- **Order:** 32
- **Label:** Genetic Sub-Region
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** The portion of the locus in which the variation was found. Examples: "Exon 15", "Kinase domain".

### GFSEQID
- **Order:** 33
- **Label:** Sequence Identifier 
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A unique identifier for the sequence used as the reference to identify the genetic variation in the result. Examples: "NM_001234", "ENSG00000182533", "ENST00000343849.2".

### GFPVRID
- **Order:** 34
- **Label:** Published Variant Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A unique identifier for the variation that has been publicly characterized in an external database. Examples: "rs2231142", "COSM41596".

### GFCOPYID
- **Order:** 35
- **Label:** Copy Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** An arbitrary identifier used to differentiate between copies of a genetic target of interest present on homologous chromosomes.

### GFSTAT
- **Order:** 36
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### GFREASND
- **Order:** 37
- **Label:** Reason Test Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with GFSTAT when value is "NOT DONE".

### GFXFN
- **Order:** 38
- **Label:** External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The filename and/or path to external data not stored in the same format and possibly not the same location as the other data for a study.

### GFNAM
- **Order:** 39
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor that provided the test result. When more than 1 vendor is involved in the generation of the result, additional vendors should be represented as supplemental qualifiers.

### GFSPEC
- **Order:** 40
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C111114
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies the type of genetic material used for the measurement.

### GFMETHOD
- **Order:** 41
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** The test method by which the examination is performed by the wet lab in order to yield the result reported in the dataset.

### GFRUNID
- **Order:** 42
- **Label:** Run ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** A unique identifier for a particular run of a test performed by the wet lab on a particular batch of samples. This identifier can be used to distinguish between records for the same test performed at different times.

### GFANMETH
- **Order:** 43
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** C181181
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The method of secondary processing performed by the dry lab to yield the result reported in the dataset.

### GFBLFL
- **Order:** 44
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null.

### GFDRVFL
- **Order:** 45
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### GFLLOQ
- **Order:** 46
- **Label:** Lower Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates the lower limit of quantitation for an assay. Units will be those used for GFSTRESU.

### GFREPNUM
- **Order:** 47
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The instance number of a test that is repeated within a given timeframe for the same test performed by the wet lab.

### VISITNUM
- **Order:** 48
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 49
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter.

### VISITDY
- **Order:** 50
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### GFDTC
- **Order:** 51
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of specimen collection.

### GFDY
- **Order:** 52
- **Label:** Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### GFTPT
- **Order:** 53
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See GFTPTNUM and GFTPTREF.

### GFTPTNUM
- **Order:** 54
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of GFTPT used in sorting.

### GFELTM
- **Order:** 55
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Elapsed time relative to a planned fixed reference (GFTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration.

### GFTPTREF
- **Order:** 56
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by GFELTM, GFTPTNUM, and GFTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### GFRFTDTC
- **Order:** 57
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by GFTPTREF.
---

## Cross References

### Controlled Terminology
- [Genetic Sample Type (C111114)](../../terminology/core/general_part2.md) — GFSPEC
- [Genomic Symbol Type Response (C181176)](../../terminology/core/gf.md) — GFSYMTYP
- [Genomic Inheritability Type Response (C181177)](../../terminology/core/gf.md) — GFINHERT
- [Genomic Findings Test Code (C181178)](../../terminology/core/gf.md) — GFTESTCD
- [Genomic Findings Test Name (C181179)](../../terminology/core/gf.md) — GFTEST
- [Genomic Findings Test Detail (C181180)](../../terminology/core/gf.md) — GFTSTDTL
- [Genomic Findings Analytical Method Calculation Formula (C181181)](../../terminology/core/gf.md) — GFANMETH
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — GFBLFL, GFDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — GFSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — GFORRESU, GFSTRESU
- [Method (C85492)](../../terminology/core/general_part3.md) — GFMETHOD

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Related Findings:** [IS](../IS/) — genomics/genetics vs immunogenicity

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

## Source: `domains/GF/assumptions.md`

# GF — Assumptions

1. The Genomics Findings domain is used to represent findings related to the structure, function, evolution, mapping, and editing of subject and non-host organism genomic material of interest. This domain includes but is not limited to assessments and results for genetic variation and transcription, and summary measures derived from these assessments. The GF domain is used for findings from characteristics assessed from nucleic acids and may include subsequent inferences and/or predictions about related proteins/amino acids. However, direct assessments of proteins (e.g., assessments of amino acids) are out of scope for this domain.

2. Regarding genetic testing on non-host organisms (including but not limited to bacteria, viruses, and parasites), the following additional assumptions apply:
   a. Tests that give genetic results (e.g., expressed in terms of genetic variation, specific sequence information) on non-host organisms that have been identified in subject samples should be represented in GF. To distinguish these findings from subject genetic data, the variable NHOID must be populated to identify the non-host organism as the focus of the record (see Section 9.2, Non-host Organism Identifiers, assumption 2 for more information).
   b. If the purpose of the test is to detect or determine the identity of a viable, non-host organism or infectious agent in a subject sample, data should be represented in the Microbiology Specimen (MB) domain.
   c. Tests that are used to determine the resistance/susceptibility of a non-host organism to a drug on a genetic basis should be represented in the Microbiology Susceptibility (MS) domain.
   d. If the test provides both genetic data and susceptibility/resistance data, genetic data should be represented in GF and the susceptibility/resistance data should be represented in the MS domain (See Section 6.3.5.7.2, Microbiology Susceptibility, assumption 1b for more information).

3. The platform used to detect the finding may be represented in SPDEVID. Attributes used in conjunction with a platform (e.g., assay panel, reagents) may be represented in the Device Identifiers (DI) domain and other associated device domains. See the SDTM Implementation Guide for Medical Devices (SDTMIG-MD) for further information about SPDEVID and the device domains.

4. Values populated in GFCAT and GFSCAT are sponsor-defined and there is no CDISC Controlled Terminology for these variables.

5. Genomic symbols are represented in GFSYM.
   a. GFTESTCD and GFTEST should not include genomic names or symbols, including but not limited to official gene symbols.
   b. For human genetic data, standard nomenclature populated in variable GFSYM must be obtained from the genomic symbol list maintained in the HUGO Gene Nomenclature Committee (HGNC) database (www.genenames.org).

6. When populating GFGENSR, caution should be exercised for annotations of loci where more than 1 annotation applies. In such cases, the source of the annotation should be captured and documented in Define-XML. In addition, the value populated in GFGENSR may be dependent on the precision of the value populated in GFSEQID.

7. Values populated in GFGENREF, GFSEQID, and GFPVRID should reflect the level of granularity collected (e.g., version, build, patch, release) to support interpretation of the reported result.

8. GFMETHOD lists wet lab techniques for the execution of genomics or genetic testing. Methods related to specimen processing or reagents are not represented in GFMETHOD.

9. The following variables generally would not be used in GF: --POS, --BODSYS, --ORNRLO, ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --CHRON, --DISTR, --ANTREG, --LOC, --LAT, --DIR, --PORTOT, --LEAD, --CSTATE, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

## Source: `domains/GF/examples.md`

# GF — Examples

## Example 1

This example shows findings from an assessment of single nucleotide and copy number variation generated from biocomputational analysis with wet laboratory methodology targeted genome sequencing. Findings from this assessment show variation from DNA extracted from an individual's tumor tissue. As the DNA specimen was extracted from tumor tissue, the inheritability of the variation is considered to be somatic.

**Row 1:** Shows the predicted amino acid change due to the single nucleotide variant.

**Row 2:** Shows the predicted coding sequence change due to the single nucleotide variant.

**Row 3:** Shows the classification of the variant impact given the predicted amino acid change.

**Row 4:** Shows the number of times the locus specified in variables GFCHROM and GFGENLOC was observed.

**Row 5:** Shows the percent variant read depth to total read depth.

**Row 6:** Shows the number of copies of the gene of interest within the genome of the tumor cell.

**Row 7:** Shows the number of altered exons within the gene of interest in the genome of the tumor cell.

**Row 8:** Shows the ratio of the copy number of the gene of interest in the tumor cell to the reference number of copies.

**Row 9:** Shows the interpretation of the copy number of the gene of interest within the genome of the tumor cell.

**gf.xpt**

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFSTRESC | GFSTREFN | GFSTRESU | GFINHERTG | GFGENREF | GFCHROM | GFSYM | GFSYMTYP | GFGENLOC | GFGENSR | GFSEQID | GFPVRID | GFCOPYID | GFNAM | GFSPEC | GFMETHOD | GFRUNID | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|---------|----------|----------|----------|-----------|----------|---------|-------|----------|----------|---------|---------|---------|----------|-------|--------|----------|---------|----------|-------|---------|-------|------|
| 1 | ABC-123 | GF | 123101 | 1 | | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | p.Val600Glu | | | | SOMATIC | | 7 | BRAF | Gene with Protein Product | Exon 15 | | ENSG00000157764 | rs121913227 | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 2 | ABC-123 | GF | 123101 | 2 | | SNV | Single Nucleotide Variation | PREDICTED CODING SEQUENCE CHANGE | c.1799T>A | | | | SOMATIC | GRCh38.p13 | 7 | BRAF | Gene with Protein Product | 140753336 | Exon 15 | ENSG00000157764 | rs121913227 | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 3 | ABC-123 | GF | 123101 | 3 | | SNV | Single Nucleotide Variation | VARIANT CLASSIFICATION | Pathogenic | | | | SOMATIC | | 7 | BRAF | Gene with Protein Product | Exon 15 | | ENSG00000157764 | rs121913227 | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 4 | ABC-123 | GF | 123101 | 4 | | SNV | Single Nucleotide Variation | LOCUS COUNT | | | 200 | | SOMATIC | GRCh38.p13 | 7 | BRAF | Gene with Protein Product | 140753336 | Exon 15 | ENSG00000157764 | rs121913227 | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 5 | ABC-123 | GF | 123101 | 5 | | SNV | Single Nucleotide Variation | PERCENT VARIANT READ DEPTH | | | 50 | % | SOMATIC | GRCh38.p13 | 7 | BRAF | Gene with Protein Product | 140753336 | Exon 15 | ENSG00000157764 | rs121913227 | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 6 | ABC-123 | GF | 123101 | 6 | | CNV | Copy Number Variation | COPY NUMBER | | | 5 | | SOMATIC | | 7 | BRAF | Gene with Protein Product | | | ENSG00000157764 | | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 7 | ABC-123 | GF | 123101 | 7 | | CNV | Copy Number Variation | EXON COPY NUMBER ALTERATION | | | 3 | | SOMATIC | | 7 | BRAF | Gene with Protein Product | | | ENSG00000157764 | | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 8 | ABC-123 | GF | 123101 | 8 | | CNV | Copy Number Variation | COPY NUMBER RATIO | | | 2.5 | | SOMATIC | | 7 | BRAF | Gene with Protein Product | | | ENSG00000157764 | | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |
| 9 | ABC-123 | GF | 123101 | 9 | | CNV | Copy Number Variation | INTERPRETATION | AMPLIFICATION | | | | SOMATIC | | 7 | BRAF | Gene with Protein Product | | | ENSG00000157764 | | | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | | 1 | Screening | -25 | | |

Identifying information for the gene panel used to generate the result is in the DI domain. The gene panel is represented in SDTM, as the panel used as part of the wet laboratory methodology may change and affects interpretation of the result. The platform in which the gene panel was used is not represented, because it does not provide additional context for the result.

**di.xpt**

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
|-----|---------|--------|---------|-------|----------|--------|-------|
| 1 | ABC-123 | DI | ACME GenePanel 500 | 1 | DEVTYPE | Device Type | Gene Panel |
| 2 | ABC-123 | DI | ACME GenePanel 500 | 2 | MANUF | Manufacturer | ACME |

## Example 2

This example shows findings from an assessment of a known single nucleotide variant in gene ABCG2 using wet laboratory methodology real-time polymerase chain reaction. Findings from this assessment show the genotypes from DNA extracted from the blood of 3 individuals, each with a different genotype at the genetic locus of interest. Because the DNA specimen was extracted from normal blood, the inheritability of the variation is considered to be in the germline.

**Row 1:** Shows a subject genotype which is homozygous for the variant nucleotide in the reference sequence.

**Row 2:** Shows a subject genotype which is heterozygous for the nucleotide in the reference sequence.

**Row 3:** Shows a subject genotype which is homozygous for the nucleotide in the reference sequence.

**gf.xpt**

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFSTRESC | GFSTREFN | GFINHERTG | GFGENREF | GFCHROM | GFSYM | GFGENLOC | GFGENSR | GFSEQID | GFPVRID | GFNAM | GFSPEC | GFMETHOD | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|---------|----------|----------|-----------|----------|---------|-------|----------|---------|---------|---------|-------|--------|----------|----------|-------|---------|-------|------|
| 1 | C12345 | GF | C12345-001 | 1 | NA01001 | SNV | Single Nucleotide Variation | GENOTYPE | G/G | G/G | | GERMLINE | GRCh38.p13 | 4 | ABCG2 | | 4.88131177 | ENSG00000118777 | rs2231142 | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | | -25 |
| 2 | C12345 | GF | C12345-002 | 1 | NA01001 | SNV | Single Nucleotide Variation | GENOTYPE | G/G | G/G | | GERMLINE | | | ABCG2 | | 4.88131177 | ENSG00000118777 | rs2231142 | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | | -25 |
| 3 | C12345 | GF | C12345-003 | 1 | NA01001 | SNV | Single Nucleotide Variation | GENOTYPE | G/G | G/G | | GERMLINE | GRCh38.p13 | 4 | ABCG2 | GENE WITH PROTEIN PRODUCT | 4.88131177 | ENSG00000118777 | rs2231142 | ACME Labs | DNA | REAL TIME POLYMERASE CHAIN REACTION | 1 | SCREENING | -1 | 2020-06-3 | -3 |

## Example 3

This example shows transcription levels of genes ACTB and GAPDH and summarized scores from the transcription levels. Transcription levels and scores were determined using biocomputational analysis with wet laboratory methodology targeted transcriptome sequencing. Specific formulas used in biocomputational analyses to generate normalized and summarized score results are respresented when applicable.

**Rows 1, 7:** Show the number of fragments counted corresponding to the indicated gene.

**Rows 2-4, 8-10:** Show normalized transcription levels based on the normalization methods noted in variable GFANMETH and the raw fragment count reported in rows 1 and 7.

**Rows 5, 11:** Show the percentile rank of the indicated gene among those genes reported in the indicated panel.

**Rows 6, 12:** Show the predicted expression status of the indicated gene based on a threshold established by the assay.

**Rows 13-14:** Show normalized transcription levels based on the normalization methods noted in variable GFANMETH and the raw fragment count reported in rows 1 and 7.

**Rows 15-16:** Show gene signature scores from summarization of genetic data based on the methods noted in variable GFANMETH.

**gf.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | GFSEQ | GFGRPID | GFREFID | GFSPID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFORRESU | GFSTRESC | GFSTRESN | GFSTRESU | GFGENREF | GFCHROM | GFSYM | GFSYMTYP | GFSEQID | GFXFN | GFNAM | GFSPEC | GFMETHOD | GFANMETH | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
|-----|---------|--------|---------|---------|-------|---------|---------|--------|----------|--------|----------|---------|----------|----------|----------|----------|----------|---------|-------|----------|---------|-------|-------|--------|----------|----------|----------|-------|---------|-------|------|
| 1 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 1 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | FRAGMENT COUNT | 36 | | 36 | 36 | | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 2 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 2 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 0.5679 | /MBP | 0.5679 | 0.5679 | /MBP | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | FRAGMENTS PER KILOBASE MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 3 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 3 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 1.0523 | /10^6 | 1.0523 | 1.0523 | /10^6 | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | COUNTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 4 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 4 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 1.9935 | /MBP | 1.9935 | 1.9935 | /MBP | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | TRANSCRIPTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 5 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 5 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | PERCENTILE RANK | 0.37 | % | 0.37 | 0.37 | % | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 6 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 6 | 1 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | no | | no | | | hs37d5 | 7 | ACTB | GENE WITH PROTEIN PRODUCT | ENST00000646664.1 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-04 | 2 |
| 7 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 7 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | FRAGMENT COUNT | 23658 | | 23658 | 23658 | | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 8 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 8 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 148.6268 | /MBP | 148.6268 | 148.6268 | /MBP | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | FRAGMENTS PER KILOBASE MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 9 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 9 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 691.5607 | /10^6 | 691.5607 | 691.5607 | /10^6 | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | COUNTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 10 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 10 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | NORMALIZED LEVEL | 521.716 | /MBP | 521.716 | 521.716 | /MBP | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | TRANSCRIPTS PER MILLION FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 11 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 11 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | PERCENTILE RANK | 0.99 | % | 0.99 | 0.99 | % | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 12 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 12 | 2 | ABU3908A52 | AH749754 | TRNSCPTN | Transcription | GENETIC TRANSCRIPTION INDICATOR | yes | | yes | | | hs37d5 | 12 | GAPDH | GENE WITH PROTEIN PRODUCT | ENST00000396861.5 | AH749754.fastq.gz | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 13 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 13 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | -0.056299177 | | -0.056299177 | -0.056299177 | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 14 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 14 | 1 | ABC1234567 | AP483910 | TRNSCPTN | Transcription | NORMALIZED LEVEL | -0.046787999 | | -0.046787999 | -0.046787999 | | GRCh38.p12 | | GAPDH | GENE WITH PROTEIN PRODUCT | NM_001256799.3 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | DIFFERENCES OF LOG2 INTENSITIES FORMULA | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 15 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 15 | 2 | ABC1234567 | AP483910 | GENESIG | Gene Signature | GENETIC TRANSCRIPTION INTERPRETATION | LOW | | LOW | | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | IFN-1 GENE SIGNATURE | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |
| 16 | ABC-123 | GF | 123101 | ACME GenePanel 250 | 16 | 3 | ABC1234567 | AP483910 | GENESIG | Gene Signature | SCORE | -1.126819661 | | -1.126819661 | -1.126819661 | | GRCh38.p12 | | ACTB | GENE WITH PROTEIN PRODUCT | NM_001101.5 | | ACME | RNA | TARGETED TRANSCRIPTOME SEQUENCING | IFN-1 GENE SIGNATURE | 1 | VISIT 1 | 1 | 2018-09-18 | 2 |

Identifying information for the gene panel used to generate the result is in the DI domain. The gene panel is represented in SDTM, as the panel used as part of the wet laboratory methodology may change and affects interpretation of the result. The platform in which the gene panel was used is not represented, because it does not provide additional context for the result.

The DI example shows the device type and manufacturer for the device identified as ACME GenePanel 250.

**di.xpt**

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
|-----|---------|--------|---------|-------|----------|--------|-------|
| 1 | ABC-123 | DI | ACME GenePanel 250 | 1 | DEVTYPE | Device Type | Gene Panel |
| 2 | ABC-123 | DI | ACME GenePanel 250 | 2 | MANUF | Manufacturer | ACME |

## Example 4

This example shows findings from an assessment of microsatellite instability for genetic subregions that are known to be unstable. DNA extracted from tumor tissue is amplified and the resulting amplicons are resolved using wet laboratory methodology capillary electrophoresis.

**Row 1:** Shows the summarized interpretation of overall microsatellite instability.

**Rows 2-6:** Show whether microsatellite instability is detected in the genetic subregions indicated.

**gf.xpt**

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFSTRESC | GFXFN | GFNAM | GFSPEC | GFMETHOD | GFRUNID | VISITNUM | VISIT | VISITDY | GFDTC | GFDY |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|---------|----------|-------|-------|--------|----------|---------|----------|-------|---------|-------|------|
| 1 | ABC123 | GF | 123101 | 1 | 4401470-2-6 | MICRISTB | Microsatellite Instability | MSI-Stable | MSI-Stable | | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 2 | ABC123 | GF | 123101 | 2 | 4401470-2-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | BAT-25 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 3 | ABC123 | GF | 123101 | 3 | 4401470-2-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | BAT-26 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 4 | ABC123 | GF | 123101 | 4 | 4401470-2-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | MONO-27 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 5 | ABC123 | GF | 123101 | 5 | 4401470-2-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | NR-21 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |
| 6 | ABC123 | GF | 123101 | 6 | 4401470-2-6 | MICRISTB | Microsatellite Instability | DETECTION | Not Detected | Not Detected | NR-24 | msi_abc_gf.csv | ACME Laboratories | DNA | CAPILLARY ELECTROPHORESIS | MS-D10418 | 1 | VISIT 1 | 1 | 2020-02-04 | -2 |

## Example 5

This example includes 3 datasets (i.e., MB and MS in addition to GF). The purpose of this 3-part example is to illustrate how these domains are appropriately used in cases where the concepts in each domain are very closely related. Specifically, the example demonstrates the use of these domains by following a subject through a hypothetical scenario of influenza diagnosis, genetic evaluation of the virus, and interpretation of drug susceptibility resulting from genetic testing.

Tests that diagnose or identify the presence of an infectious agent in a subject sample are represented in the MB domain, regardless of the methodology used. In this example, the subject was diagnosed with influenza A H3N2 via a nucleic acid amplification test (NAAT) at the baseline visit. MBTEST = "Microbial Organism Identification" because the assay does not specifically test for the presence of 1 organism or subtype to the exclusion of all others.

**mb.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MBSEQ | MBREFID | MBTESTCD | MBTEST | MBORRES | MBSTRESC | MBSPEC | MBLOC | MBMETHOD | VISITNUM | VISIT | MBDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|---------|----------|--------|-------|----------|----------|-------|-------|
| 1 | INFLU122 | MB | INF01-01 | 1 | INFLU0101.1 | MCORGIDN | Microbial Organism Identification | INFLUENZA A VIRUS SUBTYPE | INFLUENZA A VIRUS SUBTYPE H3N2 | MUCUS | NOSTRIL | NUCLEIC ACID AMPLIFICATION TEST | 1 | BASELINE | 2020-06-11 |

Next, a series of virus samples extracted from the subject underwent targeted single nucleotide polymorphism (SNP) testing to determine the feasibility of using the neuraminidase inhibitor oseltamivir to treat the infection (i.e., drug susceptibility testing). Findings from this testing provide both genetic data in the form of the genotype identified and the susceptibility/resistance data as inferred phenotype. Genotypic findings are represented in the GF domain, and inferred susceptibility/resistance in MS.

GFLNKID serves as the link between this dataset and the MS dataset which follows.

**Row 1:** Shows the result of a targeted test to detect a single nucleotide polymorphism in the influenza neuraminidase gene known to confer resistance to the drug oseltamivir. The result (R292R) indicates that the amino acid residue R (arginine) at position 292 remains unchanged at the baseline visit.

**Rows 2-3:** Show the results of the same targeted test at the day 2 and day 5 visits. The results (R292K) show that a mutation has occurred at position 292 from the amino acid R (arginine) to the amino acid K (lysine).

**gf.xpt**

| Row | STUDYID | DOMAIN | USUBJID | GFSEQ | GFREFID | NHOID | GFLNKID | GFTESTCD | GFTEST | GFTSTDTL | GFORRES | GFSTRESC | GFSYM | GFGENLOC | GFSEQID | GFSPEC | GFMETHOD | VISITNUM | VISIT | GFDTC |
|-----|---------|--------|---------|-------|---------|-------|---------|----------|--------|----------|---------|----------|-------|----------|---------|--------|----------|----------|-------|-------|
| 1 | INFLU122 | GF | INF01-01 | 1 | INFLU0101.1 | INFLUENZA A H3N2 | GF-MS-01 | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | R292R | R292R | NA | 292 | U43427 | RNA | | 1 | BASELINE | 2020-06-11 |
| 2 | INFLU122 | GF | INF01-01 | 2 | INFLU0102 | INFLUENZA A H3N2 | GF-MS-02 | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | R292K | R292K | NA | 292 | U43427 | RNA | | 2 | DAY 2 | 2020-06-12 |
| 3 | INFLU122 | GF | INF01-01 | 3 | INFLU0103 | INFLUENZA A H3N2 | GF-MS-03 | SNV | Single Nucleotide Variation | PREDICTED AMINO ACID CHANGE | R292K | R292K | NA | 292 | U43427 | RNA | | 3 | DAY 5 | 2020-06-15 |

The susceptibility data stemming from this genetic testing above are represented in MS (see Section 6.3.5.7.2, Microbiology Susceptibility, assumption 1b). GFLINKID matches MSLNKID to connect the records in GF with the corresponding conclusion regarding susceptibility in MS. As above, NHOID is used to indicate that influenza A H3N2 is the focus of these records. MSAGENT represents the drug to which the results of susceptible or resistant pertain.

**Row 1:** Shows the influenza extracted from the subject at the baseline visit is susceptible to oseltamivir.

**Rows 2-3:** Show the influenza extracted from the subject at the day 2 and day 5 visits is resistant to oseltamivir.

**ms.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MSSEQ | MSREFID | NHOID | MSLNKID | MSTESTCD | MSTEST | MSAGENT | MSORRES | MSSTRESC | MSMETHOD | VISITNUM | VISIT | MSDTC |
|-----|---------|--------|---------|-------|---------|-------|---------|----------|--------|---------|---------|----------|----------|----------|-------|-------|
| 1 | INFLU122 | MS | INF01-01 | 1 | INFLU0101.1 | INFLUENZA A H3N2 | GF-MS-01 | MICROSUS | Microbial Susceptibility | OSELTAMIVIR | SUSCEPTIBLE | SUSCEPTIBLE | | 1 | BASELINE | 2020-06-11 |
| 2 | INFLU122 | MS | INF01-01 | 2 | INFLU0102 | INFLUENZA A H3N2 | GF-MS-02 | MICROSUS | Microbial Susceptibility | OSELTAMIVIR | RESISTANT | RESISTANT | | 2 | DAY 2 | 2020-06-12 |
| 3 | INFLU122 | MS | INF01-01 | 3 | INFLU0103 | INFLUENZA A H3N2 | GF-MS-03 | MICROSUS | Microbial Susceptibility | OSELTAMIVIR | RESISTANT | RESISTANT | | 3 | DAY 5 | 2020-06-15 |

The relrec dataset example shows the relationship between the genetic assessment in GF and the resistance/susceptibility data in MS.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | PS001 | GF | | GFLNKID | | ONE | 1 |
| 2 | PS001 | MS | | MSLNKID | | ONE | 1 |

## Source: `domains/IS/spec.md`

# IS — Immunogenicity Specimen Assessments

> Class: Findings | Structure: One record per test per visit per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### NHOID
- **Order:** 4
- **Label:** Non-host Organism ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears.

### ISSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### ISGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### ISREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier. Example: "458975-01".

### ISSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### ISTESTCD
- **Order:** 9
- **Label:** Immunogenicity Test/Exam Short Name
- **Type:** Char
- **Controlled Terms:** C120525
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in ISTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in ISTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). ISTESTCD cannot contain characters other than letters, numbers, or underscores.

### ISTEST
- **Order:** 10
- **Label:** Immunogenicity Test or Examination Name
- **Type:** Char
- **Controlled Terms:** C120526
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in ISTEST cannot be longer than 40 characters. Example: "Immunoglobulin E".

### ISTSTCND
- **Order:** 11
- **Label:** Test Condition
- **Type:** Char
- **Controlled Terms:** C181175
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed.

### ISCNDAGT
- **Order:** 12
- **Label:** Test Condition Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent used to impose a test condition. Examples are different stimulating agents used in immunoassays such as those in the Interferon Gamma Response assay (e.g., Mycobacterium tuberculosis ESAT-6, CFP-10, TB 7.7, Mitogen).

### ISBDAGNT
- **Order:** 13
- **Label:** Binding Agent
- **Type:** Char
- **Controlled Terms:** C85491; C181169
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the agent that is binding to the entity in the ISTEST variable. ISBDAGNT is used to indicate that there is a binding relationship between the entities in the ISTEST and ISBDAGNT variables, regardless of direction.  ISBDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the 2 entities in ISTEST and ISBDAGNT. In other words, the combination of ISTEST and ISBDAGNT should describe the entity or the analyte being measured, without the need for additional variables.  The binding agent may be (but is not limited to) a test article, a portion of the test article, a related compound, an endogenous molecule, an allergen, or an infectious agent.

### ISTSTOPO
- **Order:** 14
- **Label:** Test Operational Objective
- **Type:** Char
- **Controlled Terms:** C181170
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the high-level purpose of the test at the operational level. If populated, valid values are "SCREEN", "CONFIRM", and "QUANTIFY".

### ISMSCBCE
- **Order:** 15
- **Label:** Molecule Secreted by Cells
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the entity secreted by the cells represented in ISTEST. The combination of ISTEST and ISMSCBCE should describe the entity or the analyte being measured, without the need for additional variables.

### ISTSTDTL
- **Order:** 16
- **Label:** Test Detail
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of ISTESTCD and ISTEST.

### ISCAT
- **Order:** 17
- **Label:** Category for Immunogenicity Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values across subjects. Example: "SEROLOGY".

### ISSCAT
- **Order:** 18
- **Label:** Subcategory for Immunogenicity Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of ISCAT.

### ISORRES
- **Order:** 19
- **Label:** Results or Findings in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### ISORRESU
- **Order:** 20
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for ISORRES. Examples: "Index Value", "gpELISA", "unit/mL".

### ISORNRLO
- **Order:** 21
- **Label:** Reference Range Lower Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### ISORNRHI
- **Order:** 22
- **Label:** Reference Range Upper Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### ISSTRESC
- **Order:** 23
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from ISORRES, in a standard format or in standard units. ISSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in ISSTRESN.

### ISSTRESN
- **Order:** 24
- **Label:** Numeric Results/Findings in Std. Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from ISSTRESC. ISSTRESN should store all numeric test results or findings.

### ISSTRESU
- **Order:** 25
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized units used for ISSTRESC and ISSTRESN. Examples: "Index Value", "gpELISA", "unit/mL".

### ISSTNRLO
- **Order:** 26
- **Label:** Reference Range Lower Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Lower end of reference range for continuous measurements for ISSTRESC/ISSTRESN in standardized units. Should be populated only for continuous results.

### ISSTNRHI
- **Order:** 27
- **Label:** Reference Range Upper Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.

### ISSTNRC
- **Order:** 28
- **Label:** Reference Range for Char Rslt-Std Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** For normal range values that are character in ordinal scale or if categorical ranges were supplied. Examples: "-1 to +1", "NEGATIVE TO TRACE".

### ISNRIND
- **Order:** 29
- **Label:** Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates where the value falls with respect to reference range defined by ISORNRLO and ISORNRHI, ISSTNRLO and ISSTNRHI, or by ISSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW".  Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether ISNRIND refers to the original or standard reference ranges and results.  Should not be used to indicate clinical significance.

### ISSTAT
- **Order:** 30
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a test was not done. Should be null if a result exists in ISORRES.

### ISREASND
- **Order:** 31
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Used in conjunction with ISSTAT when value is "NOT DONE".

### ISNAM
- **Order:** 32
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the laboratory or vendor who provided the test results.

### ISSPEC
- **Order:** 33
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the types of specimen used for a measurement. Example: "SERUM".

### ISSPCCND
- **Order:** 34
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC".

### ISSPCUFL
- **Order:** 35
- **Label:** Specimen Usability for the Test
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the usability of the specimen for the test. The value will be "N" if the specimen is not usable, and null if the specimen is usable.

### ISMETHOD
- **Order:** 36
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "ELISA", "ELISPOT".

### ISLOBXFL
- **Order:** 37
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### ISBLFL
- **Order:** 38
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that ISBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### ISDRVFL
- **Order:** 39
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Examples of records that might be derived for the submission datasets include those that represent the average of other records, do not come from the CRF, or are not as originally received or collected. If ISDRVFL="Y", then ISORRES may be null, with ISSTRESC and (if numeric) ISSTRESN having the derived value.

### ISLLOQ
- **Order:** 40
- **Label:** Lower Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates the lower limit of quantitation for an assay. Units will be those used for ISSTRESU.

### VISITNUM
- **Order:** 41
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 42
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 43
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 44
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 45
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### ISDTC
- **Order:** 46
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation.

### ISENDTC
- **Order:** 47
- **Label:** End Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the observation.

### ISDY
- **Order:** 48
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to sponsor-defined RFSTDTC in Demographics.

### ISENDY
- **Order:** 49
- **Label:** Study Day of End of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### ISTPT
- **Order:** 50
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See ISTPTNUM and ISTPTREF. Examples: "Start", "5 min post".

### ISTPTNUM
- **Order:** 51
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of ISTPT to aid in sorting.

### ISELTM
- **Order:** 52
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (ISTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable. Represented as ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by ISTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by ISTPTREF.

### ISTPTREF
- **Order:** 53
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by ISELTM, ISTPTNUM, and ISTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### ISRFTDTC
- **Order:** 54
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, ISTPTREF.
---

## Cross References

### Controlled Terminology
- [Immunogenicity Specimen Assessments Test Code (C120525)](../../terminology/core/is_domain_part1.md) — ISTESTCD
- [Immunogenicity Specimen Assessments Test Name (C120526)](../../terminology/core/is_domain_part1.md) — ISTEST
- [Binding Agent for Immunogenicity Tests (C181169)](../../terminology/core/is_domain_part1.md) — ISBDAGNT
- [Test Operational Objective (C181170)](../../terminology/core/general_part4.md) — ISTSTOPO
- [Test Condition Response (C181175)](../../terminology/core/general_part4.md) — ISTSTCND
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — ISSPCUFL, ISLOBXFL, ISBLFL, ISDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — ISSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — ISORRESU, ISSTRESU
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — ISSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — ISSPEC
- [Reference Range Indicator (C78736)](../../terminology/core/general_part4.md) — ISNRIND
- [Microorganism (C85491)](../../terminology/core/is_domain_part2.md) — ISBDAGNT
- [Method (C85492)](../../terminology/core/general_part3.md) — ISMETHOD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Specimen:** [BS](../BS/) — immunogenicity specimen data
- **Specimen Relationship:** [RELSPEC](../RELSPEC/) — specimen hierarchy

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

## Source: `domains/IS/assumptions.md`

# IS — Assumptions

1. The Immunogenicity Specimen Assessments (IS) domain holds assessments that describe whether a therapy (e.g., biologic, drug, vaccine) provoked/caused/induced an immune response in a subject. The response can be either positive or negative. For example, a vaccine is expected to induce a beneficial immune response, whereas a cellular therapy (e.g., erythropoiesis-stimulating agents) may cause an adverse immune response.

2. The IS domain also holds assessments that describe whether an allergen, microorganism, or endogenous molecule provoked/caused/induced an immune response in a subject, such as a subject's antibody reaction (autoantibodies) against auto/self-antigens for autoimmune studies or antibody production in response to allergens in allergy tests. Expected outputs can be positive or negative, present or absent for the antibody of interest, as well as quantification of the antibody. Assessments pertaining to antibodies produced in response to microbial infection will also be represented in the IS domain.

3. Assessments about all other types of "induced" humoral (antibody) immune response in a subject (e.g., antibodies against human leukocyte antigen (HLA) proteins) will also be represented in the IS domain.

4. Certain types of cellular immune responses will also be modeled in IS using non-flow cytometry techniques (see example 6). Flow cytometry data should be modeled in the Cell Phenotype Findings (CP) domain, section 6.3.5.3.

5. An exception is made to the class of antigen/antibody (Ag/Ab) combination assays. Microbial antigen/antibody (Ag/Ab) combination tests should be represented in the Microbiology Specimen (MB) domain. An example is fourth-generation HIV Ag/Ab combination tests, which are commonly seen as HIV identification or detection assays rather than tests that provide additional details on and characterization of a subject's immunological responses. The outputs of these assays can be expected as reactive, non-reactive, or indeterminate. Whereas some tests generate separate outputs for antigen and antibody, others just indicate "reactive" when either or both are detected. Output is generally based on relative light units, where a result of "reactive" typically requires the signal to cutoff ratio to be greater than 1.

6. Measurements of cytokines, chemokines, and complement proteins should be represented in the Laboratory Test Results (LB) domain.

7. The IS domain variable ISBDAGNT (Binding Agent) is currently supported by 2 Controlled Terminology codelists: Microorganism (MICROORG) and Binding Agent for Immunogenicity Tests (ISBDAGT). Controlled Terminology Rules for Immunogenicity Tests describes how and when to use each codelist (see https://www.cdisc.org/standards/terminology/controlled-terminology).
   a. For antidrug antibody (ADA) tests, the ISBDAGNT variable is used to represent the free-text description of the name/identity of the therapy the antidrug antibody targets. CDISC does not control study therapy names (e.g., drugs, biologics). For ADA tests as a part of regulatory agency submissions, the proprietary binding study therapy name(s) should be considered as extended values of the ISBDAGT codelist when represented in Define-XML.
   b. For mixed-allergens panel tests, submission values represented in the ISBDAGNT variable should follow this format: "XXX, Multiple" (e.g., Dairy Mix Antigens, Multiple; Animal Mix Antigens, Multiple; use the plural form for the word "antigen" if needed). Should the sponsor wish to specify the individual antigens in a mixed antigen panel (e.g., ISBDAGNT = "Animal Mix Antigens, Multiple"), put the names of the specific antigens in Suppqual (e.g., Cat, Dog, Cow, Horse; see example 11).

8. The IS domain variable ISTSTOPO (Test Operational Objective) is supported by a nonextensible Controlled Terminology codelist containing the values SCREEN, CONFIRM, and QUANTIFY.

9. For vaccine studies, in order to distinguish collected data between study vaccine-induced immunogenicity and immunogenicity findings unrelated to the study vaccine (i.e., immunity as a result of natural infection or previous vaccination), the following ISCAT and ISSCAT values are recommended (see example 5):
   a. For immunological data pertaining to the study vaccine, ISCAT = STUDY VACCINE-RELATED IMMUNOGENICITY.
   b. For immunological data collected during the vaccine trial but which are not assessments about the study vaccine, ISCAT = NON-STUDY-RELATED IMMUNOGENICITY.
   c. For assessments measuring the induced-antibody response, ISSCAT = HUMORAL IMMUNITY.
   d. For assessments measuring the induced-cellular response, ISSCAT = CELLULAR IMMUNITY.

10. Any Identifier variables, Timing variables, or Findings general observation class qualifiers may be added to the IS domain.

## Source: `domains/IS/examples.md`

# IS — Examples

## Example 1

This example shows data from tiered testing of antidrug antibody (ADA).

Tiered testing scheme for ADA evaluation generally includes the following steps: screening, confirmatory, and "characterization" of the antidrug antibody. In tier 1, all evaluable samples are run in a screening assay. Samples that are positive for ADA in the screen assay are then analyzed in a confirmatory assay (tier 2). The samples that are positive for ADA in both the screen and confirmatory tiers of testing are further tested in tier 3; this frequently includes analysis of antibody titer and neutralizing activity. In order to illustrate the distinctive differences between the 3 tiers of ADA testing, the standard variable ISTSTOPO is used to represent the controlled values SCREEN, CONFIRM, and QUANTIFY. These values help to describe the operational objective or the reason behind each testing step/tier, and also to provide uniqueness to each row of record. The study drug AZ-007, which induces the subject's production of, and is the target of the antidrug antibody, is represented by the variable ISBDAGNT. ISGRPID is used in this example to show that the records are related to each other; in this particular case, tests are done in a tiered, sequential manner from screen to confirm to quantification of the detected antidrug antibody.

Lastly, antibody titer is often defined as the reciprocal of the lowest dilution of a sample generating a signal that is above the assay cut-point. Alternatively, the titer is defined as the reciprocal of the dilution of a sample generating a signal that is equivalent to the assay cut-point, calculated by an interpolation formula provided in an assay specific bioanalytical method.

**Row 1:** Shows the screening of the presence of ADA to drug AZ-007.
**Row 2:** Shows the confirmation of the previously detected ADA to drug AZ-007.
**Row 3:** Shows the measurement of titer of the ADA from the screen and confirmatory steps.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | ABC | IS | ABC-002 | 1 | V555 | 1 | ADA_BAB | Binding Antidrug Antibody | DRUG AZ-007 | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-002 | 2 | V555 | 1 | ADA_BAB | Binding Antidrug Antibody | DRUG AZ-007 | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-002 | 3 | V555 | 1 | ADA_BAB | Binding Antidrug Antibody | DRUG AZ-007 | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 50 | titer | 50 | 50 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |

## Example 2

This example shows data from various subtypes of ADA tests.

Although most ADAs do not inhibit the pharmacodynamic activity of a drug, neutralizing antidrug antibodies (NAbs) can inhibit drug activity soon after a drug is administered. Most ADAs (those that are not classified as NAbs) can lower the drug's systemic exposure by increasing the rate of drug clearance, resulting in a clinically similar outcome to that of NAbs (i.e., reduced clinical efficacy).

In this example, the administered drug is an analogue of an endogenous protein. The example data include ADA reactions against both the administered drug and the endogenous protein. Both the study drug and the endogenous protein are represented by the standard variable ISBDAGNT, which qualifies ISTEST. The variable ISTSTOPO, is also used in this dataset to describe the purpose of each testing step, and provides uniqueness among similar records. ISGRPID is used to show which records are related in this dataset.

Note that, in this example, even though only confirmatory records are reported and shown, it is assumed that the screening step has also been performed.

**Rows 1-2:** Show the confirmation and quantification of binding ADA to coagulation factor VIII analogue drug. A binding antidrug antibody is an antibody that binds to a drug.
**Rows 3-4:** Show the confirmation and quantification of the neutralizing binding ADA to coagulation factor VIII analogue drug. A neutralizing binding antidrug antibody is a type of ADA that binds to the functional portion of a drug, leading to diminished or negated pharmacological activity. The neutralizing ADAs are a subset of the total ADAs.
**Rows 5-6:** Show the confirmation and quantification of the cross-reactive binding ADA to the endogenous coagulation factor VIII. A cross-reactive binding antidrug antibody is a type of ADA that binds to endogenous molecules, also a subset of the total ADAs.
**Rows 7-8:** Show the confirmation and quantification of the neutralizing cross-reactive binding ADA to the endogenous coagulation factor VIII. Neutralizing cross-reactive binding antidrug antibodies are a type of ADA that bind to endogenous molecules, leading to diminished or negated function; in some cases, they may also bind and negate the function of the study drug. They are a subset of the total ADAs.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | ABC | IS | ABC-001 | 1 | A42839 | 1 | ADA_BAB | Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-001 | 2 | A42839 | 1 | ADA_BAB | Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 30 | titer | 30 | 30 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-001 | 3 | A42839 | 2 | ADA_NAB | Neutralizing Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |
| 4 | ABC | IS | ABC-001 | 4 | A42839 | 2 | ADA_NAB | Neutralizing Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 60 | titer | 60 | 60 | titer | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |
| 5 | ABC | IS | ABC-001 | 5 | A42839 | 3 | ADA_X | Cross-Reactive Binding Antidrug Antibody | ENDOGENOUS COAGULATION FACTOR VIII | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 6 | ABC | IS | ABC-001 | 6 | A42839 | 3 | ADA_X | Cross-Reactive Binding Antidrug Antibody | ENDOGENOUS COAGULATION FACTOR VIII | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 90 | titer | 90 | 90 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 7 | ABC | IS | ABC-001 | 7 | A42839 | 3 | ADA_NX | Neutralize Cross-React Bind Antidrug Ab | ENDOGENOUS COAGULATION FACTOR VIII | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |
| 8 | ABC | IS | ABC-001 | 8 | A42839 | 4 | ADA_NX | Neutralize Cross-React Bind Antidrug Ab | ENDOGENOUS COAGULATION FACTOR VIII | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 150 | titer | 150 | 150 | titer | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |

## Example 3

This example shows data about ADA reaction against drug components.

This example shows the production of ADA in response to both the prodrug and its active metabolite. A prodrug is a compound that, after administration, is metabolized into a pharmacologically active drug. Note that, in this example, even though only confirmatory records are reported and shown, it is assumed that the screening step has also been performed.

**Rows 1-2:** Show the confirmation and quantification of the ADA against prodrug A.
**Rows 3-4:** Show the confirmation and quantification of the ADA against the active metabolite of prodrug A.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | ABC | IS | ABC-004 | 1 | J123 | 1 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-004 | 2 | J123 | 1 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 30 | titer | 30 | 30 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-004 | 3 | J123 | 2 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A ACTIVE METABOLITE | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 4 | ABC | IS | ABC-004 | 4 | J123 | 2 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A ACTIVE METABOLITE | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 60 | titer | 60 | 60 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |

## Example 4

This example shows data about ADA reaction against multiple epitopes of a drug molecule.

This example shows the production of ADA in response to the study biologic drug, peginterferon beta-1a; its active metabolite, active interferon beta 1a; and its immunogenic epitope, PEG epitope of peginterferon beta-1a. An immunogenic epitope of a biologic drug is a particular segment within the drug that is recognized by the immune system, specifically by antibodies, B cells, or T cells. This immunogenic epitope portion of the biologic drug is capable of inducing the production of and therefore the binding of ADAs.

This example also shows when tiered testing stops at the screening step (interferon beta1a assay) and goes straight to neutralizing antidrug antibody testing. Although this is unusual, it illustrates the flexibility of the fields ISTEST, ISBDAGNT, and ISTSTOPO to incorporate multiple options.

**Row 1:** Shows the presence of ADA against the active metabolite of peginterferon beta-1a, active interferon beta 1a, in subject ABC-007.
**Rows 2-3:** Show the screening and confirmation of ADA against the PEG epitope of peginterferon beta-1a in subject ABC-007.
**Rows 4-5:** Show the screen and quantification of neutralizing ADA against the whole molecule peginterferon beta-1a in subject ABC-007.
**Row 6:** Shows the absence of ADA against the active metabolite of peginterferon beta 1a, active interferon beta 1a portion, in subject ABC-008.
**Rows 7-9:** Show the screening, confirmation, and quantification of ADA against the PEG epitope of peginterferon beta-1a, in subject ABC-008.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | ABC | IS | ABC-007 | 1 | A1 | | ADA_BAB | Binding Antidrug Antibody | ACTIVE INTERFERON BETA 1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-007 | 2 | A1 | | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELISA | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-007 | 3 | A1 | | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA1A | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | NEGATIVE | | NEGATIVE | | | SERUM | ELISA | 1 | VISIT 1 | 2017-07-27 |
| 4 | ABC | IS | ABC-007 | 4 | A1 | | ADA_NAB | Neutralizing Binding Antidrug Antibody | PEGINTERFERON BETA1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | REPORTER GENE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 5 | ABC | IS | ABC-007 | 5 | A1 | | ADA_NAB | Neutralizing Binding Antidrug Antibody | PEGINTERFERON BETA1A | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 4.7 | titer | 4.7 | 4.7 | titer | SERUM | REPORTER GENE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 6 | ABC | IS | ABC-008 | 6 | V4 | | ADA_BAB | Binding Antidrug Antibody | ACTIVE INTERFERON BETA 1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | NEGATIVE | | NEGATIVE | | | SERUM | IMMUNOASSAY | 1 | VISIT 1 | 2017-08-27 |
| 7 | ABC | IS | ABC-008 | 7 | V4 | | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELISA | 1 | VISIT 1 | 2017-08-27 |
| 8 | ABC | IS | ABC-008 | 8 | V4 | | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA1A | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELISA | 1 | VISIT 1 | 2017-08-27 |
| 9 | ABC | IS | ABC-008 | 9 | V4 | | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA1A | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 40 | titer | 40 | 40 | titer | SERUM | ELISA | 1 | VISIT 1 | 2017-08-27 |

## Example 5

This example illustrates how to represent both study vaccine-induced humoral (antibody) immunity, and immunogenicity responses not related to the study vaccine but which are also important for collection, specifically in vaccine trials.

In this case, the subject was administered with a human respiratory syncytial virus (RSV) vaccine and his protective antibody production against the major component of the study vaccine, RSV-protein B, was assessed. Detection and quantification of the anti-RSV-protein B antibody data from baseline to post-vaccination were collected and are represented below. At baseline, antibody against RSV-protein Z was detected in the same subject, which suggests either natural infection by or previous vaccination with RSV-protein B at the time of assessment. Even though immunity against RSV-protein B was not the interest of the RSV vaccine study, immunological data pertaining to RSV-protein B was collected for the subject.

This example illustrates the use of the CDISC-recommended ISCAT values "STUDY VACCINE-RELATED IMMUNOGENICITY" and "NON-STUDY-RELATED IMMUNOGENICITY" to distinguish between study vaccine-induced immunogenicity and immunogenicity findings unrelated to the study vaccine data collected during a vaccine study. ISCAT = "NON-STUDY-RELATED IMMUNOGENICITY" was developed to explicitly and purposefully indicate whether an observed immunity toward an antigen was not related to the study vaccine but rather was a result of natural infection or previous vaccination. Oftentimes, it is simply impossible to tell whether the antibody found in a subject is due to a natural infection or previous vaccination (or both) — yet this immunogenicity, unrelated to the study vaccine, is important for collection and assessment at the screening phase of the trial.

In this example, immune responses against RSV-protein Z were measured during the study. Because protein Z is not inserted into the vaccine vector, any immune response detected toward protein Z was not related to the study vaccine, although important for assessment and collected per the study protocol. In order to show that RSV-protein Z-induced antibody production was unrelated to the immunity solicited by the study vaccine RSV-protein B (ISCAT = "STUDY VACCINE-RELATED IMMUNOGENICITY"), the ISCAT for rows 3 and 4 is "NON-STUDY-RELATED IMMUNOGENICITY" (note: protein Z and protein B are examples, refer to controlled terminology for standard terms associated with ISBDAGNT).

**Rows 1-2:** Show the screening and quantification of microbial-induced immunoglobulin G (IgG) antibody against the RSV-protein B at baseline, prior to the administration of the study vaccine. ISBDAGNT="HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B" is the immunogenic target in the study vaccine that could potentially stimulate the production of antibodies. Note: ISCAT="STUDY VACCINE-RELATED IMMUNOGENICITY", even though at this point the study vaccine has not been administered to the subject; this is done prospectively to enable the grouping of baseline and treatment measurements.
**Rows 3-4:** Show the screening and quantification of microbial-induced IgG antibody against the RSV-protein Z at baseline. Note: Because RSV-protein Z is not the immunogenic target of interest in this vaccine study, ISCAT is populated with the value "NON-STUDY-RELATED IMMUNOGENICITY".
**Rows 5-7:** Show the titer of microbial-induced IgG antibody against the RSV-protein B, post-vaccination at visits 1, 2, and 3. These 3 records show the antibody titers had increased post-vaccination, presumably due to the stimulation from the RSV study vaccine. ISCAT is populated with the value "STUDY VACCINE-RELATED IMMUNOGENICITY".

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | SCREEN | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | IMMUNOASSAY | 1 | BASELINE | 2017-05-27 |
| 2 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:24 | titer | NA | | | SERUM | IMMUNOASSAY | 1 | BASELINE | 2017-05-27 |
| 3 | RSV1230 | IS | RSV1230-011 | 3 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN Z | SCREEN | NON-STUDY-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | IMMUNOASSAY | 1 | BASELINE | 2017-05-27 |
| 4 | RSV1230 | IS | RSV1230-011 | 4 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN Z | QUANTIFY | NON-STUDY-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:50 | titer | NA | | | SERUM | IMMUNOASSAY | 1 | BASELINE | 2017-05-27 |
| 5 | RSV1230 | IS | RSV1230-011 | 5 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:100 | titer | NA | | | SERUM | IMMUNOASSAY | 2 | VISIT 1 | 2017-07-27 |
| 6 | RSV1230 | IS | RSV1230-011 | 6 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:250 | titer | NA | | | SERUM | IMMUNOASSAY | 3 | VISIT 2 | 2017-08-27 |
| 7 | RSV1230 | IS | RSV1230-011 | 7 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:500 | titer | NA | | | SERUM | IMMUNOASSAY | 4 | VISIT 3 | 2017-09-27 |

Thus far, all the IS tests illustrated are measurements of concentrations of a substance (e.g., antibody titer). However, some immunogenicity tests are actual counts of immune cells that secrete a particular substance. These tests are described by the combination of ISTEST (Immunogenicity Test or Examination Name) and ISMSCBCE (Molecule Secreted by Cells), where ISTEST identifies the type of cells that secrete a specific substance (e.g., antibody-secreting cells, cytokine-secreting cells) and ISMSCBCE names the substance (e.g., IgG antibody, interferon-gamma). The following 2 examples introduce the IS domain-specific variable, ISMSCBCE, and illustrate its use with ISTEST to represent a complete immunological analyte of interest.

## Example 6

This example shows data about the assessment of antibody-secreting cells (ASCs).

Traditional methods such as enzyme-linked immunosorbent assay (ELISA) that monitor humoral immune responses after immunization or infection typically only quantify specific antibody titers in serum. These methods do not provide any information about the actual number and location of the immune cells that secrete these antibodies or cytokines.

The enzyme-linked immunospot (ELISpot) assay is a method to detect and quantify analyte-secreting T or B cells. During ELISpot testing, a colored precipitate forms and appears as spots at the sites of analyte localization (analytes typically are cytokines or antibodies), with each individual spot representing an individual analyte-secreting cell. The spots can be counted with an automated ELISpot reader system or manually, using a stereomicroscope. This example shows how to represent the quantification of ASCs as the number of spots per million peripheral blood mononuclear cells (PBMC) as determined by B-cell ELISpot from a vaccine trial.

The IS domain-specific variable ISMSCBCE introduced in this example allows flexibility in data representation and post-coordination of the various secreted antibody types and their respective ASCs. This approach liberates the ISTEST variable from having to house precoordinated and thus hyperspecific values crafted based on secretion and cell types.

**Row 1:** Shows the total number of IgG ASCs from a subject's blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is represented by the variable ISMSCBCE (i.e. IGG antibody non-specific to any antigen).
**Row 2:** Shows the number of H1-specific IgG ASCs from the same blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is in ISMSCBCE (i.e. IgG antibody specific to H1 antigen).
**Row 3:** Shows the number of H3-specific IgG ASCs from the same subject's blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is in ISMSCBCE (i.e. IgG antibody specific to H3 antigen).

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISMSCBCE | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | ISDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|-------|
| 1 | INFLA456 | IS | INF02-01 | 1 | SAMPLBC001 | ABSCCL | Antibody-secreting Cells | IGG ANTIBODY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 2019 | SFC/10^6 PBMC | 2019 | 2019 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2011-06-08 |
| 2 | INFLA456 | IS | INF02-01 | 2 | SAMPLBC001 | ABSCCL | Antibody-secreting Cells | INFLUENZA H1-SPECIFIC IGG ANTIBODY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 626 | SFC/10^6 PBMC | 626 | 626 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2011-06-08 |
| 3 | INFLA456 | IS | INF02-01 | 3 | SAMPLBC001 | ABSCCL | Antibody-secreting Cells | INFLUENZA H3-SPECIFIC IGG ANTIBODY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 592 | SFC/10^6 PBMC | 592 | 592 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2011-06-08 |

## Example 7

This example shows data from the in vitro assessment and quantification of cytokine-secreting immune cells, expressed in number of spot-forming cells (SFC) per million peripheral blood mononuclear cells (PBMC) as determined by T-cell ELISpot from a vaccine trial.

Through vaccination, it is expected that cytokine secretion in immune cells is boosted whenever immune cells encounter the same virus and/or the previously exposed viral antigens. By increasing this cytokine secretion, immune cells aid in the host defense and protection against (re-)infections. In vaccine trials, this can be measured by isolating immune cells (e.g., PBMCs) from subjects at multiple time points during the course of the trial and restimulating them with the virus or its viral antigens in vitro.

In this example, PBMCs were isolated from a subject participating in a vaccine study for RSV and restimulated in vitro with either a RSV-antigen or without a stimulating agent. At baseline (i.e., before vaccination), the RSV antigen-stimulated PBMCs produced minimal number of interferon gamma, as expressed in interferon gamma-secreting cells quantified in the number of SFC/10^6 PBMC (row 2), as compared to no stimulation (row 1). Three weeks after vaccination, RSV-antigen stimulated PBMCs (row 4) showed significant increase in the number of interferon-gamma secreting cells compared to no stimulation (row 3) or baseline values (rows 1 and 2). This suggests immunological memory of the immune cells after encountering the same microorganism or its antigens, and the switch of cell state from resting to active.

**Rows 1-2:** Show the measurement of interferon gamma (ISMSCBCE) cytokine-secreting cells (ISTEST) at baseline either with no stimulation (row 1) or stimulated with the RSV-antigen (row 2) in ISCNDAGT.
**Rows 3-4:** Show the measurement of interferon gamma (ISMSCBCE) cytokine-secreting cells (ISTEST) 3 weeks after vaccination and restimulation in vitro with the RSV-antigen (row 4) in ISCNDAGT and no stimulation (row 3), respectively.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISMSCBCE | ISTCND | ISCNDAGT | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|--------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITHOUT STIMULATING AGENT | | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 5.1 | SFC/10^6 PBMC | 5.1 | 5.1 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 1 | BASELINE | 2017-05-27 |
| 2 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITH STIMULATING AGENT | RSV-EPITOPE B | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 10.5 | SFC/10^6 PBMC | 10.5 | 10.5 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 1 | BASELINE | 2017-05-27 |
| 3 | RSV1230 | IS | RSV1230-011 | 3 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITHOUT STIMULATING AGENT | | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 60.8 | SFC/10^6 PBMC | 60.8 | 60.8 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2 | VISIT 1 | 2017-06-27 |
| 4 | RSV1230 | IS | RSV1230-011 | 4 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITH STIMULATING AGENT | RSV-EPITOPE B | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 260.5 | SFC/10^6 PBMC | 260.5 | 260.5 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2 | VISIT 1 | 2017-06-27 |

## Example 8

In vaccine studies, microneutralization assays are commonly used in assays to quantify viral-specific neutralizing antibodies in a subject's specimen that can block viral infection in vitro, and therefore provide a measure of vaccine efficacy. A neutralizing antibody is an antibody that binds to, blocks, and prevents non-self agents from infecting cells.

When immunizing a subject with a vaccine, the hope is that the vaccine will induce antiviral and humoral-protective antibody responses in the subject; with an effective vaccine, the quantity of virus-specific antibodies that are able to block viral infection are increased. To test the efficacy of a vaccine, a microneutralization test is performed by adding a vaccinated subject's serum and the virus of study interest to cell cultures in vitro. If neutralizing antibodies are present in the subject's serum post-vaccination, those antibodies will bind to, block, and prevent the virus from infecting cells in the culture plates. The neutralization titer is the specific dilution of the antibody that blocks viral infection of the cells. The 50% neutralization titer (also known as NT50), in the context of microneutralization assays, is defined as the antiviral antibody titer that blocks 50% of viral infection of the cells. **Note:** Some users may represent the 50% neutralization titer as "IC50 titer" or other test descriptors. CDISC recommends mapping all such values in the ISTSTDTL variable.

NHOID is populated with respiratory syncytial virus because this microorganism is the subject of the vaccine efficacy test.

NHOID, defined by the Non-host Organism Identifiers (OI) domain, should be used to map microorganisms that have been either experimentally determined in the course of a study or are previously known (e.g., lab strains used as reference in the study). In other words, NHOID is used when the study subject is the microorganism, and when the microorganism is present in the testing sample. In vaccine efficacy studies, a subject's post-immunization sera is often incubated with a microbial strain of interest, where the functional capacities of the vaccine-induced antibodies are measured through whether the antibodies can effectively stop (from infection), neutralize, and kill the study microorganism of interest, in vitro. Examples of such tests include microneutralization, hemagglutination inhibition, and opsonophagocytic-killing assays. These are tests that measure the direct effect of the antimicrobial antibodies on the microorganism; therefore, said microorganism is the study subject and should be mapped to NHOID.

This example uses data from the same RSV vaccine study, where the subject is being vaccinated with a viral vector containing RSV. The subject is tested before (baseline) and after vaccination (visits 1 and 2) to investigate whether the anti-RSV antibodies present in the subject's serum also have the ability to neutralize RSV infection in vitro.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | NHOID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|-------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | RSV1230 | IS | RSV1230-011 | RESPIRATORY SYNCYTIAL VIRUS | 1 | 13668 | MBNAB | Neutralizing Microbial-induced Antibody | RESPIRATORY SYNCYTIAL VIRUS | NEUTRALIZING TITER 50% | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:40 | | 40 | 40 | titer | SERUM | MICRONEUTRALIZATION ASSAY | 1 | BASELINE | 2017-05-27 |
| 2 | RSV1230 | IS | RSV1230-011 | RESPIRATORY SYNCYTIAL VIRUS | 2 | 13668 | MBNAB | Neutralizing Microbial-induced Antibody | RESPIRATORY SYNCYTIAL VIRUS | NEUTRALIZING TITER 50% | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:80 | | 80 | 80 | titer | SERUM | MICRONEUTRALIZATION ASSAY | 2 | VISIT 1 | 2017-07-27 |
| 3 | RSV1230 | IS | RSV1230-011 | RESPIRATORY SYNCYTIAL VIRUS | 3 | 13668 | MBNAB | Neutralizing Microbial-induced Antibody | RESPIRATORY SYNCYTIAL VIRUS | NEUTRALIZING TITER 50% | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:200 | | 200 | 200 | titer | SERUM | MICRONEUTRALIZATION ASSAY | 3 | VISIT 2 | 2017-09-27 |

## Example 9

In vaccine trials, the OPK assay is used as a correlate for immunoprotectivity against antigens, by measuring the functional capacities of vaccine-induced antibodies.

Typically, this test is performed by incubating a subject's post-immunization sera with the bacterial strain of interest, phagocytes, and complement proteins. If antibacterial, functional antibodies are present in the serum, those antibodies will bind to the bacteria together with complement proteins. This subsequently targets the bacteria for opsonization, the ingestion and destruction of invading non-self agents by phagocytes. With vaccination, the quantity of bacterial-specific, functional antibodies are increased, leading to a decreased number of viable bacterial cells in the presence of phagocytes, functional antibodies, and complement. The assay read-out is expressed in by the opsonization index, which is calculated using linear interpolation of the serum dilution containing functional antibody killing the desired percentage (usually 50%) of the bacteria, using a specified algorithm.

NHOID is populated with Staphylococcus aureus 04-02981 because this strain of S. aureus is the subject of the vaccine efficacy test.

NHOID, defined by the Non-host Organism Identifiers (OI) domain, should be used to map microorganisms that have been either experimentally determined in the course of a study or are previously known (e.g., lab strains used as reference in the study). In other words, NHOID is used when the study subject is the microorganism, and when the microorganism is present in the testing sample. In vaccine efficacy studies, a subject's post-immunization sera is often incubated with a microbial strain of interest, where the functional capacities of the vaccine-induced antibodies are measured through whether the antibodies can effectively stop (from infection), neutralize, and kill the study microorganism of interest, in vitro. Examples of such tests include microneutralization, hemagglutination inhibition, and opsonophagocytic-killing assays. These are tests that measure the direct effect of the antimicrobial antibodies on the microorganism; therefore, said microorganism is the study subject and should be mapped to NHOID.

In this vaccine-study example, the subject is vaccinated with a vector containing S. aureus-epitope X (note: epitope X is an example, refer to controlled terminology for standard terms associated with ISBDAGNT). The subject is tested before (baseline) and after vaccination (visits 1 and 2) to investigate whether the vaccine-induced functional antibodies drive efficient complement deposition and subsequent opsonophagocytic killing of S. aureus, in vitro. The assay read-out is expressed by the opsonization index (ISTSTDTL), which is a unit-less test.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | NHOID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISCAT | ISSCAT | ISORRES | ISSTRESC | ISSTRESN | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|-------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|--------|----------|----------|-------|-------|
| 1 | SAU1230 | IS | SAU1230-011 | STAPHYLOCOCCUS AUREUS 04-02981 | 1 | 13668 | MBFAB | Functional Microbial-induced Antibody | STAPHYLOCOCCUS AUREUS-EPITOPE X | OPSONIZATION INDEX | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 100 | 100 | 100 | SERUM | OPSONOPHAGOCYTIC KILLING ASSAY | 1 | BASELINE | 2017-05-27 |
| 2 | SAU1230 | IS | SAU1230-011 | STAPHYLOCOCCUS AUREUS 04-02981 | 2 | 13668 | MBFAB | Functional Microbial-induced Antibody | STAPHYLOCOCCUS AUREUS-EPITOPE X | OPSONIZATION INDEX | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1000 | 1000 | 1000 | SERUM | OPSONOPHAGOCYTIC KILLING ASSAY | 2 | VISIT 1 | 2017-07-27 |
| 3 | SAU1230 | IS | SAU1230-011 | STAPHYLOCOCCUS AUREUS 04-02981 | 3 | 13668 | MBFAB | Functional Microbial-induced Antibody | STAPHYLOCOCCUS AUREUS-EPITOPE X | OPSONIZATION INDEX | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 5000 | 5000 | 5000 | SERUM | OPSONOPHAGOCYTIC KILLING ASSAY | 3 | VISIT 2 | 2017-09-27 |

## Example 10

This example shows how to present data from an autoimmune disease study, specifically how to represent information from disease-specific autoantibody tests.

Sjogren's syndrome (SS) is a systemic autoimmune disease characterized by dry eyes and dry mouth. Diagnosis of SS is generally based on the detection of antinuclear antibodies (ANAs), that is, anti-Ro (SS-A) and anti-La (SS-B) antibodies.

**Rows 1-5:** Show the screening (row 1) and quantification (rows 2, 4) of ANAs. Rows 2 and 3 are grouped together using ISGRPID="1a"; this means the titer result in row 2 is specifically related to the particular nuclear staining pattern (i.e., speckled) finding in row 3. The speckled pattern of ANA is typically indicative of SS, systemic lupus, and mixed connective tissue disease. Rows 4 and 5 are grouped together using ISGRPID="1b"; this means the titer result in row 4 is specifically related to the nuclear staining pattern (i.e., nucleolar) finding in row 5. Rows 1 to 5 are grouped together with values starting with the number "1", indicating that these records are related. The antinuclear antibodies test is post-coordinated using ISGRPID and represented by both ISTEST="Autoantibody" and ISBDAGNT="NUCLEAR AUTOANTIGENS".
**Rows 6-11:** Show the screening and quantification of the various SS-specific autoantibodies. SS autoantigens are represented by the ISBDAGNT variable, whereas the ISTEST="Autoantibody".

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISTSTOPO | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|----------|----------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | XYZ | IS | XYZ1234 | 1 | 19283746 | 1 | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | | SCREEN | POSITIVE | | POSITIVE | | | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 2 | XYZ | IS | XYZ1234 | 2 | 19283746 | 1a | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | | QUANTIFY | 1:340 | | 340 | 340 | titer | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 3 | XYZ | IS | XYZ1234 | 3 | 19283746 | 1a | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | STAINING PATTERN | | SPECKLED PATTERN | | SPECKLED PATTERN | | | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 4 | XYZ | IS | XYZ1234 | 4 | 19283746 | 1b | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | | QUANTIFY | 1:170 | | 170 | 170 | titer | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 5 | XYZ | IS | XYZ1234 | 5 | 19283746 | 1b | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | STAINING PATTERN | | NUCLEOLAR PATTERN | | NUCLEOLAR PATTERN | | | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 6 | XYZ | IS | XYZ1234 | 6 | 19283746 | 2 | ATAB | Autoantibody | SJOGRENS SS-A60 ANTIGEN | | SCREEN | POSITIVE | | POSITIVE | | | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 7 | XYZ | IS | XYZ1234 | 7 | 19283746 | 2 | ATAB | Autoantibody | SJOGRENS SS-A60 ANTIGEN | | QUANTIFY | 181 | U/mL | 181 | 181 | U/mL | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 8 | XYZ | IS | XYZ1234 | 8 | 19283746 | 3 | ATAB | Autoantibody | SJOGRENS SS-A52 ANTIGEN | | SCREEN | POSITIVE | | POSITIVE | | | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 9 | XYZ | IS | XYZ1234 | 9 | 19283746 | 3 | ATAB | Autoantibody | SJOGRENS SS-A52 ANTIGEN | | QUANTIFY | 51 | U/mL | 51 | 51 | U/mL | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 10 | XYZ | IS | XYZ1234 | 10 | 19283746 | 4 | ATAB | Autoantibody | SJOGRENS SS-B ANTIGEN | | SCREEN | POSITIVE | | POSITIVE | | | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 11 | XYZ | IS | XYZ1234 | 11 | 19283746 | 4 | ATAB | Autoantibody | SJOGRENS SS-B ANTIGEN | | QUANTIFY | 169 | U/mL | 169 | 169 | U/mL | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |

## Example 11

This example shows how to represent data from various allergy tests, specifically data from a mixed animal allergens test.

**Row 1:** Shows the detection of immunoglobulin E (IgE) antibody against multiple animal allergens. ISBDAGNT is used to house the generic but controlled value "ANIMAL MIX ANTIGENS, MULTIPLE".
**Rows 2-3:** Show the amount of IgE antibody against dog dander and its RAST classification score.
**Rows 4-5:** Show the amount of IgE antibody against cat dander and its RAST classification score.
**Rows 6-7:** Show the amount of IgE antibody against horse dander and its RAST classification score.
**Rows 8-9:** Show the amount of IgE antibody against cow dander and its RAST classification score.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|----------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | XYZ | IS | XYZ1234 | 1 | 12453333 | ARIGEAB | Allergen-induced IgE Antibody | ANIMAL MIX ANTIGENS, MULTIPLE | | POSITIVE | | POSITIVE | | | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 2 | XYZ | IS | XYZ1234 | 2 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | DOG DANDER ANTIGEN | | 0.12 | U/mL | 0.12 | 0.12 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 3 | XYZ | IS | XYZ1234 | 3 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | DOG DANDER ANTIGEN | RAST SCORE | 0 | | 0 | 0 | | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 4 | XYZ | IS | XYZ1234 | 4 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | CAT DANDER ANTIGEN | | 0.19 | U/mL | 0.19 | 0.19 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 5 | XYZ | IS | XYZ1234 | 5 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | CAT DANDER ANTIGEN | RAST SCORE | 0 | | 0 | 0 | | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 6 | XYZ | IS | XYZ1234 | 6 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | HORSE DANDER ANTIGEN | | 44 | U/mL | 44 | 44 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 7 | XYZ | IS | XYZ1234 | 7 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | HORSE DANDER ANTIGEN | RAST SCORE | 4 | | 4 | 4 | | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 8 | XYZ | IS | XYZ1234 | 8 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | COW DANDER ANTIGEN | | 120 | U/mL | 120 | 120 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 9 | XYZ | IS | XYZ1234 | 9 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | COW DANDER ANTIGEN | RAST SCORE | 6 | | 6 | 6 | | SERUM | RIA | 1 | SCREENING | 2018-06-20 |

The SUPPIS dataset shows the specific and individual animal allergens within the animal mixed antigens panel test.

**suppis.xpt**

| Row | STUDYID | DOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|--------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | DOG | CRF | |
| 2 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | CAT | CRF | |
| 3 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | HORSE | CRF | |
| 4 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | COW | CRF | |

Alternatively, instead of reporting the specific components of a mixed allergen panel, regional allergen mixes may also be reported by the specific regions/areas where they are predominant, as shown in the SUPPIS dataset below.

**suppis.xpt**

| Row | STUDYID | DOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|--------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISALGREG | Allergen Mixture Region | CENTRAL CA, AREA 14 | CRF | |
