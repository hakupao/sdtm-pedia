# 12_fnd_vitals_vs_eg

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `12`
> - **Concept**: Findings: VS + EG (生命体征 + ECG)
> - **Merged files**: 6
> - **Words**: 9,238
> - **Chars**: 53,294
> - **Sources**:
>   - `domains/VS/spec.md`
>   - `domains/VS/assumptions.md`
>   - `domains/VS/examples.md`
>   - `domains/EG/spec.md`
>   - `domains/EG/assumptions.md`
>   - `domains/EG/examples.md`

---
## Source: `domains/VS/spec.md`

# VS — Vital Signs

> Class: Findings | Structure: One record per vital sign measurement per time point per visit per subject

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

### VSSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### VSGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### VSSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.

### VSTESTCD
- **Order:** 7
- **Label:** Vital Signs Test Short Name
- **Type:** Char
- **Controlled Terms:** C66741
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in VSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in VSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). VSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SYSBP", "DIABP", "BMI".

### VSTEST
- **Order:** 8
- **Label:** Vital Signs Test Name
- **Type:** Char
- **Controlled Terms:** C67153
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in VSTEST cannot be longer than 40 characters. Examples: "Systolic Blood Pressure", "Diastolic Blood Pressure", "Body Mass Index".

### VSCAT
- **Order:** 9
- **Label:** Category for Vital Signs
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records.

### VSSCAT
- **Order:** 10
- **Label:** Subcategory for Vital Signs
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of a measurement or examination.

### VSPOS
- **Order:** 11
- **Label:** Vital Signs Position of Subject
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".

### VSORRES
- **Order:** 12
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the vital signs measurement as originally received or collected.

### VSORRESU
- **Order:** 13
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C66770
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for VSORRES. Examples: "in", "LB", "beats/min".

### VSSTRESC
- **Order:** 14
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from VSORRES in a standard format or standard units. VSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in VSSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in VSORRES, and these results effectively have the same meaning, they could be represented in standard format in VSSTRESC as "NEGATIVE".

### VSSTRESN
- **Order:** 15
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from VSSTRESC. VSSTRESN should store all numeric test results or findings.

### VSSTRESU
- **Order:** 16
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C66770
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for VSSTRESC and VSSTRESN.

### VSSTAT
- **Order:** 17
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a vital sign measurement was not done. Should be null if a result exists in VSORRES.

### VSREASND
- **Order:** 18
- **Label:** Reason Not Performed
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with VSSTAT when value is "NOT DONE".

### VSLOC
- **Order:** 19
- **Label:** Location of Vital Signs Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Location relevant to the collection of vital signs measurement. Example: "ARM" for blood pressure.

### VSLAT
- **Order:** 20
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### VSLOBXFL
- **Order:** 21
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.

### VSBLFL
- **Order:** 22
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that VSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### VSDRVFL
- **Order:** 23
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records or that do not come from the CRF are examples of records that would be derived for the submission datasets. If VSDRVFL = "Y," then VSORRES may be null, with VSSTRESC and (if numeric) VSSTRESN having the derived value.

### VSTOX
- **Order:** 24
- **Label:** Toxicity
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of toxicity quantified by VSTOXGR. The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.

### VSTOXGR
- **Order:** 25
- **Label:** Standard Toxicity Grade
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Records toxicity grade value using a standard toxicity scale (e.g., NCI CTCAE). If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2"). The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.

### VSCLSIG
- **Order:** 26
- **Label:** Clinically Significant, Collected
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a collected observation is clinically significant based on judgment.

### VISITNUM
- **Order:** 27
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 28
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 29
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 30
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 31
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time at which the assessment was made.

### VSDTC
- **Order:** 32
- **Label:** Date/Time of Measurements
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of the vital signs assessment represented in ISO 8601 character format.

### VSDY
- **Order:** 33
- **Label:** Study Day of Vital Signs
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of vital signs measurements, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### VSTPT
- **Order:** 34
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See VSTPTNUM and VSTPTREF. Examples: "START", "5 MIN POST".

### VSTPTNUM
- **Order:** 35
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of VSTPT to aid in sorting.

### VSELTM
- **Order:** 36
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (VSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 Duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by VSTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by VSTPTREF.

### VSTPTREF
- **Order:** 37
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by VSELTM, VSTPTNUM, and VSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### VSRFTDTC
- **Order:** 38
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, VSTPTREF.
---

## Cross References

### Controlled Terminology
- [Vital Signs Test Code (C66741)](../../terminology/core/vs.md) — VSTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — VSLOBXFL, VSBLFL, VSDRVFL, VSCLSIG
- [Units for Vital Signs Results (C66770)](../../terminology/core/vs.md) — VSORRESU, VSSTRESU
- [Not Done (C66789)](../../terminology/core/general_part4.md) — VSSTAT
- [Vital Signs Test Name (C67153)](../../terminology/core/vs.md) — VSTEST
- [Position (C71148)](../../terminology/core/interventions.md) — VSPOS
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — VSLOC
- [Laterality (C99073)](../../terminology/core/general_part2.md) — VSLAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

## Source: `domains/VS/assumptions.md`

# VS — Assumptions

1. In cases where the LOINC dictionary is used for vital sign tests, the permissible variable VSLOINC may be used. Sponsors are expected to provide the dictionary name and version used to map terms using the external codelist element in the Define-XML document.

2. If a reference range is available for a vital signs test, the variables VSORNRLO, VSORNRHI, VSNRIND from the Findings observation class may be added to the domain. VSORNRLO and VSORNRHI would represent the reference range, and VSNRIND would be used to indicate where a result falls with respect to the reference range (e.g., "HIGH", "LOW"). If toxicity grading is available, values would be represented in the variables VSTOX and VSTOXGR. Clinical significance would be represented in VSCLSIG, as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data.

3. Associations between some vital sign tests and qualifier codelists are described in the VS codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

4. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the VS domain, but the following qualifiers would not generally be used: --BODSYS, --XFN, --SPEC, --SPCCND, --FAST.

## Source: `domains/VS/examples.md`

# VS — Examples

## Example 1

This example shows results for 1 subject from 2 visits (i.e., baseline, visit 2).

**Rows 1-4, 6-7:** VSTPT and VSTPTNUM are populated because more than 1 measurement was taken at this visit.
**Rows 2, 4-5, 7-9:** VSLOBXFL="Y" indicates that the observation was used as the last observation before exposure measurement.
**Rows 10-11:** Show blood pressure observations obtained at visit 2.
**Row 12:** Shows a value collected in one unit, but converted to selected standard unit.
**Row 13:** Shows the proper use of the --STAT variable to indicate "NOT DONE" where a reason was collected when a test was not done.

**vs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | VSSEQ | VSTESTCD | VSTEST | VSPOS | VSORRES | VSORRESU | VSSTRESC | VSSTRESN | VSSTRESU | VSSTAT | VSREASND | VSLOC | VSLAT | VSLOBXFL | VISITNUM | VISIT | VISITDY | VSDTC | VSDY | VSTPT | VSTPTNUM |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|----------|----------|-------|---------|-------|------|-------|----------|
| 1 | ABC | VS | ABC-001-001 | 1 | SYSBP | Systolic Blood Pressure | SITTING | 154 | mmHg | 154 | 154 | mmHg | | | ARM | LEFT | | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE | 1 |
| 2 | ABC | VS | ABC-001-001 | 2 | SYSBP | Systolic Blood Pressure | SITTING | 152 | mmHg | 152 | 152 | mmHg | | | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE | 2 |
| 3 | ABC | VS | ABC-001-001 | 3 | DIABP | Diastolic Blood Pressure | SITTING | 44 | mmHg | 44 | 44 | mmHg | | | ARM | LEFT | | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE | 1 |
| 4 | ABC | VS | ABC-001-001 | 4 | DIABP | Diastolic Blood Pressure | SITTING | 48 | mmHg | 48 | 48 | mmHg | | | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE | 2 |
| 5 | ABC | VS | ABC-001-001 | 5 | PULSE | Pulse Rate | SITTING | 72 | beats/min | 72 | 72 | beats/min | | | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19 | 1 | | |
| 6 | ABC | VS | ABC-001-001 | 6 | TEMP | Temperature | | 34.7 | C | 34.7 | 34.7 | C | | | SUBLINGUAL REGION | | | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE | 1 |
| 7 | ABC | VS | ABC-001-001 | 7 | TEMP | Temperature | | 38.2 | C | 38.2 | 38.2 | C | | | SUBLINGUAL REGION | | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE | 2 |
| 8 | ABC | VS | ABC-001-001 | 8 | WEIGHT | Weight | STANDING | 90.5 | kg | 90.5 | 90.5 | kg | | | | | Y | 1 | Baseline | 1 | 1999-06-19 | 1 | | |
| 9 | ABC | VS | ABC-001-001 | 9 | HEIGHT | Height | STANDING | 157 | cm | 157 | 157 | cm | | | | | Y | 1 | Baseline | 1 | 1999-06-19 | 1 | | |
| 10 | ABC | VS | ABC-001-001 | 10 | SYSBP | Systolic Blood Pressure | SITTING | 95 | mmHg | 95 | 95 | mmHg | | | ARM | LEFT | | 2 | Visit 2 | 35 | 1999-07-21 | 33 | | |
| 11 | ABC | VS | ABC-001-001 | 11 | DIABP | Diastolic Blood Pressure | SITTING | 44 | mmHg | 44 | 44 | mmHg | | | ARM | LEFT | | 2 | Visit 2 | 35 | 1999-07-21 | 33 | | |
| 12 | ABC | VS | ABC-001-001 | 12 | TEMP | Temperature | | 97.16 | F | 38.2 | 36.2 | C | | | SUBLINGUAL REGION | | | 2 | Visit 2 | 35 | 1999-07-21 | 33 | | |
| 13 | ABC | VS | ABC-001-001 | 13 | WEIGHT | Weight | | | | | | | NOT DONE | SUBJECT REFUSED | | | | 2 | Visit 2 | 35 | 1999-07-21 | 33 | | |

## Source: `domains/EG/spec.md`

# EG — ECG Test Results

> Class: Findings | Structure: One record per ECG observation per replicate per time point or one record per ECG observation per beat per visit per subject

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

### EGSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### EGGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### EGREFID
- **Order:** 7
- **Label:** ECG Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external ECG identifier. Example: "334PT89".

### EGSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the ECG page.

### EGBEATNO
- **Order:** 9
- **Label:** ECG Beat Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** A sequence number that identifies the beat within an ECG.

### EGTESTCD
- **Order:** 10
- **Label:** ECG Test or Examination Short Name
- **Type:** Char
- **Controlled Terms:** C71153; C120523
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in EGTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in EGTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). EGTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRAG", "QRSAG".  Test codes are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTESTCD) and one 1 tests based on Holter monitoring (HETESTCD).

### EGTEST
- **Order:** 11
- **Label:** ECG Test or Examination Name
- **Type:** Char
- **Controlled Terms:** C71152; C120524
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in EGTEST cannot be longer than 40 characters. Examples: "PR Interval, Aggregate", "QRS Duration, Aggregate".  Test names are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTEST) and 1 for tests based on Holter monitoring (HETEST).

### EGCAT
- **Order:** 12
- **Label:** Category for ECG
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize ECG observations across subjects. Examples: "MEASUREMENT", "FINDING", "INTERVAL".

### EGSCAT
- **Order:** 13
- **Label:** Subcategory for ECG
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the ECG.

### EGPOS
- **Order:** 14
- **Label:** ECG Position of Subject
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".

### EGORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the ECG measurement or finding as originally received or collected. Examples of expected values are "62" or "0.151" when the result is an interval or measurement, or "ATRIAL FIBRILLATION" or "QT PROLONGATION" when the result is a finding.

### EGORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for EGORRES. Examples: "sec", "msec".

### EGSTRESC
- **Order:** 17
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C71150; C120522; C101834
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from EGORRES, in a standard format or standard units. EGSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in EGSTRESN. For example, if a test has results of 62 beats/min, then EGORRES = "62", EGORRESU = "beats/min", EGSTRESC = "62", EGSTRESN = 62, and EGSTRESU = "beats/min" . For other examples, see Original and Standardized Results. Additional examples of result data: "SINUS BRADYCARDIA", "ATRIAL FLUTTER", "ATRIAL FIBRILLATION".  Test results are in 3 separate codelists: EGSTRESC for abnormal test results based on regular 10-second ECGs; HESTRESC for abnormal test results based on Holter monitoring, and NORMABNM for generic test results and/or responses to EGTEST = "Interpretation".

### EGSTRESN
- **Order:** 18
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from EGSTRESC. EGSTRESN should store all numeric test results or findings.

### EGSTRESU
- **Order:** 19
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for EGSTRESC and EGSTRESN.

### EGSTAT
- **Order:** 20
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate an ECG was not done, or an ECG measurement was not taken. Should be null if a result exists in EGORRES.

### EGREASND
- **Order:** 21
- **Label:** Reason ECG Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with EGSTAT when value is "NOT DONE".

### EGXFN
- **Order:** 22
- **Label:** ECG External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** File name and path for the external ECG waveform file.

### EGNAM
- **Order:** 23
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the laboratory or vendor providing the test results.

### EGMETHOD
- **Order:** 24
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C71151
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the ECG test. Example: "12-LEAD STANDARD".

### EGLEAD
- **Order:** 25
- **Label:** Lead Location Used for Measurement
- **Type:** Char
- **Controlled Terms:** C90013
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The lead used for the measurement. Examples: "LEAD 1", "LEAD 2", "LEAD rV2", "LEAD V1".

### EGLOBXFL
- **Order:** 26
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### EGBLFL
- **Order:** 27
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that EGBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### EGDRVFL
- **Order:** 28
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If EGDRVFL="Y", then EGORRES could be null, with EGSTRESC and EGSTRESN (if the result is numeric) having the derived value.

### EGEVAL
- **Order:** 29
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR".

### EGEVALID
- **Order:** 30
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in EGEVAL. Examples: "RADIOLOGIST 1" or "RADIOLOGIST 2".

### EGCLSIG
- **Order:** 31
- **Label:** Clinically Significant, Collected
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a collected observation is clinically significant based on judgment.

### EGREPNUM
- **Order:** 32
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.

### VISITNUM
- **Order:** 33
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 34
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 35
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 36
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 37
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### EGDTC
- **Order:** 38
- **Label:** Date/Time of ECG
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/Time of ECG.

### EGDY
- **Order:** 39
- **Label:** Study Day of ECG
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the ECG, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### EGTPT
- **Order:** 40
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EGTPTNUM and EGTPTREF. Examples: "Start", "5 min post".

### EGTPTNUM
- **Order:** 41
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of EGTPT to aid in sorting.

### EGELTM
- **Order:** 42
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a fixed time point reference (EGTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by EGTPTREF.

### EGTPTREF
- **Order:** 43
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by EGELTM, EGTPTNUM, and EGTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### EGRFTDTC
- **Order:** 44
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by EGTPTREF.
---

## Cross References

### Controlled Terminology
- [Normal Abnormal Response (C101834)](../../terminology/core/eg_part3.md) — EGSTRESC
- [Holter ECG Results (C120522)](../../terminology/core/eg_part3.md) — EGSTRESC
- [Holter ECG Test Code (C120523)](../../terminology/core/eg_part3.md) — EGTESTCD
- [Holter ECG Test Name (C120524)](../../terminology/core/eg_part3.md) — EGTEST
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — EGLOBXFL, EGBLFL, EGDRVFL, EGCLSIG
- [Not Done (C66789)](../../terminology/core/general_part4.md) — EGSTAT
- [Position (C71148)](../../terminology/core/interventions.md) — EGPOS
- [ECG Result (C71150)](../../terminology/core/eg_part1.md) — EGSTRESC
- [ECG Test Method (C71151)](../../terminology/core/eg_part2.md) — EGMETHOD
- [ECG Test Name (C71152)](../../terminology/core/eg_part2.md) — EGTEST
- [ECG Test Code (C71153)](../../terminology/core/eg_part2.md) — EGTESTCD
- [Unit (C71620)](../../terminology/core/general_part5.md) — EGORRESU, EGSTRESU
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — EGEVAL
- [ECG Lead (C90013)](../../terminology/core/eg_part1.md) — EGLEAD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — EGEVALID
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Related Findings:** [CP](../CP/) — ECG vs cardiac electrophysiology

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

## Source: `domains/EG/assumptions.md`

# EG — Assumptions

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

## Source: `domains/EG/examples.md`

# EG — Examples

## Example 1

This example shows ECG measurements and other findings from one ECG for one subject. EGCAT has been used to group tests.

**Row 1:** Shows a measurement of ventricular rate. This result was assessed as not clinically significant (EGCLSIG = "N").

**Row 2:** Shows a measurement of PR interval. This result was assessed as clinically significant (EGCLSIG = "Y").

**Rows 2-4:** These interval measurements were collected in seconds. However, in this submission, the standard unit for these tests was milliseconds, so the results have been converted in EGSTRESC and EGSTRESN.

**Rows 5-6:** Show "QTcB Interval, Aggregate" and "QTcF Interval, Aggregate". These results were derived by the sponsor, as indicated by the "Y" in the EGDRVFL column. Note that EGORRES is null for these derived records.

**Rows 7-10:** Show results from tests looking for certain kinds of abnormalities, which have been grouped using EGCAT = "FINDINGS".

**Row 11:** Shows a technical problem represented as the result of the test "Technical Quality". Results of this test can be important to the overall understanding of an ECG, but are not truly findings or interpretations about the subject's heart function.

**Row 12:** Shows the result of the TEST "Interpretation" (i.e., the interpretation of the ECG strip as a whole), which for this ECG was "ABNORMAL".

**eg.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGREFID | EGTESTCD | EGTEST | EGCAT | EGPOS | EGORRES | EGORRESU | EGSTRESC | EGSTRESN | EGSTRESU | EGXFN | EGNAM | EGCLSIG | EGDRVFL | VISITNUM | VISIT | EGDTC | EGDY |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|-------|---------|----------|----------|----------|----------|-------|-------|---------|---------|----------|-------|-------|------|
| 1 | XYZ | EG | XYZ-US-701-002 | 1 | 334PT89 | EGHRMN | ECG Mean Heart Rate | MEASUREMENT | SUPINE | 62 | beats/min | 62 | 62 | beats/min | PQW43787B-07.xml | Test | N | | 1 | Screening | 2003-04-36 | -36 |
| 2 | XYZ | EG | XYZ-US-701-002 | 2 | 334PT89 | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 0.15 | sec | 150 | 150 | msec | PQW43787B-07.xml | Test | Y | | 1 | Screening | 2003-04-36 | -36 |
| 3 | XYZ | EG | XYZ-US-701-002 | 3 | 334PT89 | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 0.103 | sec | 103 | 103 | msec | PQW43787B-07.xml | Test | | | 1 | Screening | 2003-04-36 | -36 |
| 4 | XYZ | EG | XYZ-US-701-002 | 4 | 334PT89 | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 0.406 | sec | 406 | 406 | msec | PQW43787B-07.xml | Test | | | 1 | Screening | 2003-04-36 | -36 |
| 5 | XYZ | EG | XYZ-US-701-002 | 5 | 334PT89 | QTCBAG | QTcB Interval, Aggregate | INTERVAL | SUPINE | | | 469 | 469 | msec | PQW43787B-07.xml | Test | Y | | 1 | Screening | 2003-04-36 | -36 |
| 6 | XYZ | EG | XYZ-US-701-002 | 6 | 334PT89 | QTCFAG | QTcF Interval, Aggregate | INTERVAL | SUPINE | | | 448 | 448 | msec | PQW43787B-07.xml | Test | Y | | 1 | Screening | 2003-04-36 | -36 |
| 7 | XYZ | EG | XYZ-US-701-002 | 7 | 334PT89 | SPRATRY | Supraventricular Tachyarrhythmias | FINDING | SUPINE | ATRIAL FIBRILLATION | | ATRIAL FIBRILLATION | | | PQW43787B-07.xml | Lab | | | 1 | Screening | 15T11:58 | -36 |
| 8 | XYZ | EG | XYZ-US-701-002 | 8 | 334PT89 | SPRATRY | Supraventricular Tachyarrhythmias | FINDING | SUPINE | ATRIAL FLUTTER | | ATRIAL FLUTTER | | | PQW43787B-07.xml | Lab | | | 1 | Screening | 15T11:58 | -36 |
| 9 | XYZ | EG | XYZ-US-701-002 | 9 | 334PT89 | STSTWUN | ST Segment, T wave, and U wave Changes: nonspecific or Enlargement | FINDING | SUPINE | PROLONGED QT | | PROLONGED QT | | | PQW43787B-07.xml | Lab | | | 1 | Screening | 15T11:58 | -36 |
| 10 | XYZ | EG | XYZ-US-701-002 | 10 | 334PT89 | CHPTEN2 | Chamber Hypertrophy or Enlargement | FINDING | SUPINE | LEFT VENTRICULAR HYPERTROPHY | | LEFT VENTRICULAR HYPERTROPHY | | | PQW43787B-07.xml | Lab | | | 1 | Screening | 15T11:58 | -36 |
| 11 | XYZ | EG | XYZ-US-701-002 | 11 | 334PT89 | TECHQUAL | Technical Quality | FINDING | SUPINE | OTHER/INCORRECT ELECTRODE PLACEMENT | | OTHER/INCORRECT ELECTRODE PLACEMENT | | | PQW43787B-07.xml | Lab | | | 1 | Screening | 15T11:58 | -36 |
| 12 | XYZ | EG | XYZ-US-701-002 | 12 | 334PT89 | INTP | Interpretation | | SUPINE | ABNORMAL | | ABNORMAL | | | | | | | 1 | Screening | 15T11:58 | -36 |

## Example 2

This example shows ECG results where only the overall assessment was collected. Results are for one subject across multiple visits. In addition, the ECG interpretation was provided by the investigator and, when necessary, by a cardiologist. EGGRPID is used to group the overall assessments collected on each ECG.

**Rows 1-3:** Show interpretations performed by the principal investigation on three different occasions. The ECG at Visit "SCREEN 2" has been flagged as the last observation before start of study treatment.

**Rows 4-5:** Show interpretations of the same ECG by both the investigator and a cardiologist. EGGRPID has been used to group these two records to emphasize their relationship.

**eg.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGGRPID | EGTESTCD | EGTEST | EGPOS | EGORRES | EGSTRESC | EGLOBXFL | EGEVAL | VISITNUM | VISIT | VISITDY | EGDTC | EGDY |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|--------|----------|-------|---------|-------|------|
| 1 | ABC | EG | ABC-99-CA-456 | 1 | | INTP | Interpretation | SUPINE | NORMAL | NORMAL | | PRINCIPAL INVESTIGATOR | 1 | SCREEN 1 | -2 | 2003-11-26 | -2 |
| 2 | ABC | EG | ABC-99-CA-456 | 2 | | INTP | Interpretation | SUPINE | NORMAL | NORMAL | Y | PRINCIPAL INVESTIGATOR | 2 | SCREEN II | -1 | 2003-11-27 | -1 |
| 3 | ABC | EG | ABC-99-CA-456 | 3 | | INTP | Interpretation | SUPINE | ABNORMAL | ABNORMAL | | PRINCIPAL INVESTIGATOR | 3 | DAY 10 | 10 | 2003-12-07T09:02 | 10 |
| 4 | ABC | EG | ABC-99-CA-456 | 4 | Comp 1 | INTP | Interpretation | SUPINE | ABNORMAL | ABNORMAL | | PRINCIPAL INVESTIGATOR | 4 | DAY 15 | 15 | 2003-12-12 | 15 |
| 5 | ABC | EG | ABC-99-CA-456 | 5 | Comp 1 | INTP | Interpretation | SUPINE | ABNORMAL | ABNORMAL | | CARDIOLOGIST | 4 | DAY 15 | 15 | 2003-12-12 | 15 |

## Example 3

This example shows 10-second ECG replicates extracted from a continuous recording. The example shows one subject's extracted 10-second ECG replicate results. Three replicates were extracted for planned time points "1 HR" and "2 HR"; EGREPNUM is used to identify the replicates. Summary mean measurements are reported for the 10 seconds of extracted data for each replicate. EGDTC is the date/time of the first individual beat in the extracted 10-second ECG. In order to save space, some permissible variables (EGREFID, VISITDY, EGTPTNUM, EGTPTREF, EGRFTDTC) have been omitted, as marked by ellipses.

**eg.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | ... | EGTESTCD | EGTEST | EGCAT | EGPOS | EGORRES | EGORRESU | EGSTRESC | EGSTRESN | EGSTRESU | EGMETHOD | EGLEAD | EGLOBXFL | VISITNUM | VISIT | EGDTC | EGTPT | ... | EGREPNUM |
|-----|---------|--------|---------|-------|-----|----------|--------|-------|-------|---------|----------|----------|----------|----------|----------|--------|----------|----------|-------|-------|-------|-----|----------|
| 1 | STUDY01 | EG | 2324-P0001 | 1 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
| 2 | STUDY01 | EG | 2324-P0001 | 2 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 658 | msec | 658 | 658 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
| 3 | STUDY01 | EG | 2324-P0001 | 3 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 97 | msec | 97 | 97 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
| 4 | STUDY01 | EG | 2324-P0001 | 4 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 440 | msec | 440 | 440 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
| 5 | STUDY01 | EG | 2324-P0001 | 5 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | ... | 2 |
| 6 | STUDY01 | EG | 2324-P0001 | 6 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 679 | msec | 679 | 679 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | ... | 2 |
| 7 | STUDY01 | EG | 2324-P0001 | 7 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 95 | msec | 95 | 95 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | ... | 2 |
| 8 | STUDY01 | EG | 2324-P0001 | 8 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 389 | msec | 389 | 389 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | ... | 2 |
| 9 | STUDY01 | EG | 2324-P0001 | 9 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 169 | msec | 169 | 169 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:02:14 | 1 HR | ... | 3 |
| 10 | STUDY01 | EG | 2324-P0001 | 10 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 661 | msec | 661 | 661 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:02:14 | 1 HR | ... | 3 |
| 11 | STUDY01 | EG | 2324-P0001 | 11 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 90 | msec | 90 | 90 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:02:14 | 1 HR | ... | 3 |
| 12 | STUDY01 | EG | 2324-P0001 | 12 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 377 | msec | 377 | 377 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:02:14 | 1 HR | ... | 3 |
| 13 | STUDY01 | EG | 2324-P0001 | 13 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:00:21 | 2 HR | ... | 1 |
| 14 | STUDY01 | EG | 2324-P0001 | 14 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 771 | msec | 771 | 771 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:00:21 | 2 HR | ... | 1 |
| 15 | STUDY01 | EG | 2324-P0001 | 15 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 100 | msec | 100 | 100 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:00:21 | 2 HR | ... | 1 |
| 16 | STUDY01 | EG | 2324-P0001 | 16 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 379 | msec | 379 | 379 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:00:21 | 2 HR | ... | 1 |
| 17 | STUDY01 | EG | 2324-P0001 | 17 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 179 | msec | 179 | 179 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:01:31 | 2 HR | ... | 2 |
| 18 | STUDY01 | EG | 2324-P0001 | 18 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 749 | msec | 749 | 749 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:01:31 | 2 HR | ... | 2 |
| 19 | STUDY01 | EG | 2324-P0001 | 19 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 103 | msec | 103 | 103 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:01:31 | 2 HR | ... | 2 |
| 20 | STUDY01 | EG | 2324-P0001 | 20 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 402 | msec | 402 | 402 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:01:31 | 2 HR | ... | 2 |
| 21 | STUDY01 | EG | 2324-P0001 | 21 | ... | PRAG | PR Interval, Aggregate | INTERVAL | SUPINE | 175 | msec | 175 | 175 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:02:40 | 2 HR | ... | 3 |
| 22 | STUDY01 | EG | 2324-P0001 | 22 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 771 | msec | 771 | 771 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:02:40 | 2 HR | ... | 3 |
| 23 | STUDY01 | EG | 2324-P0001 | 23 | ... | QRSAG | QRS Duration, Aggregate | INTERVAL | SUPINE | 98 | msec | 98 | 98 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:02:40 | 2 HR | ... | 3 |
| 24 | STUDY01 | EG | 2324-P0001 | 24 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 356 | msec | 356 | 356 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T11:02:40 | 2 HR | ... | 3 |

## Example 4

The example shows one subject's continuous beat-to-beat EG results. Only 3 beats are shown, but there could be measurements for, as an example, 101,000 complexes in 24 hours. The actual number of complexes in 24 hours can be variable and depends on average heart rate. The results are mapped to the EG domain using EGBEATNO. If there is no result to be reported, then the row would not be included.

**Rows 1-2:** Show the first beat recorded. The first beat was considered to be the beat for which the recording contained a complete P-wave. It was assigned EGBEATNO = "1". There is no RR measurement for this beat because RR is measured as the duration (time) between the peak of the R-wave in the reported single beat and peak of the R-wave in the preceding single beat, and the partial recording that preceded EGBEATNO = "1" did not contain an R-wave. EGDTC was the date/time of the individual beat.

**Rows 3-5:** EGBEATNO = "2" had an RR measurement, since the R-wave of the preceding beat (EGBEATNO = "1") was recorded.

**Rows 6-8:** There is a 1-hour gap between beats 2 and 3 due to electrical interference or other artifacts that prevented measurements from being recorded. Note that EGBEATNO = "3" does have an RR measurement because the partial beat preceding EGBEATNO = "3" contained an R-wave.

**eg.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGBEATNO | EGTESTCD | EGTEST | EGCAT | EGPOS | EGORRES | EGORRESU | EGSTRESC | EGSTRESN | EGSTRESU | EGMETHOD | EGLEAD | EGLOBXFL | VISITNUM | VISIT | VISITDY | EGDTC |
|-----|---------|--------|---------|-------|----------|----------|--------|-------|-------|---------|----------|----------|----------|----------|----------|--------|----------|----------|-------|---------|-------|
| 1 | STUDY01 | EG | 2324-P0001 | 1 | 1 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T14:32:12.3 |
| 2 | STUDY01 | EG | 2324-P0001 | 2 | 1 | QRSSB | QRS Duration, Single Beat | INTERVAL | SUPINE | 97 | msec | 97 | 97 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T14:32:12.3 |
| 3 | STUDY01 | EG | 2324-P0001 | 3 | 2 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 176 | msec | 176 | 176 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T14:32:12.3 |
| 4 | STUDY01 | EG | 2324-P0001 | 4 | 2 | RRSM | RR Interval, Single Measurement | INTERVAL | SUPINE | 679 | msec | 679 | 679 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T14:32:13.3 |
| 5 | STUDY01 | EG | 2324-P0001 | 5 | 2 | QRSSB | QRS Duration, Single Beat | INTERVAL | SUPINE | 95 | msec | 95 | 95 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T14:32:13.3 |
| 6 | STUDY01 | EG | 2324-P0001 | 6 | 3 | PRSB | PR Interval, Single Beat | INTERVAL | SUPINE | 169 | msec | 169 | 169 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T15:32:13.3 |
| 7 | STUDY01 | EG | 2324-P0001 | 7 | 3 | RRSM | RR Interval, Single Measurement | INTERVAL | SUPINE | 661 | msec | 661 | 661 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T15:32:14.2 |
| 8 | STUDY01 | EG | 2324-P0001 | 8 | 3 | QRSSB | QRS Duration, Single Beat | INTERVAL | SUPINE | 90 | msec | 90 | 90 | msec | 12 LEAD STANDARD | LEAD II | | 1 | SCREENING | -7 | 2014-02-11T15:32:14.2 |
