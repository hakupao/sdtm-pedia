# 20_fnd_about_fa_sr

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `20`
> - **Concept**: Findings About: FA + SR (2 domains)
> - **Merged files**: 6
> - **Words**: 10,739
> - **Chars**: 61,162
> - **Sources**:
>   - `domains/FA/spec.md`
>   - `domains/FA/assumptions.md`
>   - `domains/FA/examples.md`
>   - `domains/SR/spec.md`
>   - `domains/SR/assumptions.md`
>   - `domains/SR/examples.md`

---
## Source: `domains/FA/spec.md`

# FA — Findings About Events or Interventions

> Class: Findings About | Structure: One record per finding, per object, per time point, per visit per subject

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

### FASEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### FAGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### FASPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF.

### FATESTCD
- **Order:** 7
- **Label:** Findings About Test Short Name
- **Type:** Char
- **Controlled Terms:** C101832
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in FATEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in FATESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FATESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SEV", "OCCUR". Note that controlled terminology is in a FATESTCD general codelist and in several therapeutic area-specific codelists.

### FATEST
- **Order:** 8
- **Label:** Findings About Test Name
- **Type:** Char
- **Controlled Terms:** C101833
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in FATEST cannot be longer than 40 characters. Examples: "Severity/Intensity", "Occurrence". Note that controlled terminology is in a FATEST general codelist and in several therapeutic area-specific codelists.

### FAOBJ
- **Order:** 9
- **Label:** Object of the Observation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the term (e.g., "Acne") describing a clinical sign or symptom that is being measured by a severity test; an event (e.g., "VOMIT, where the volume of vomit is being measured by a VOLUME test).

### FACAT
- **Order:** 10
- **Label:** Category for Findings About
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records. Examples: "GERD", "PRE-SPECIFIED AE".

### FASCAT
- **Order:** 11
- **Label:** Subcategory for Findings About
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of FACAT.

### FAORRES
- **Order:** 12
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the test as originally received or collected.

### FAORRESU
- **Order:** 13
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for FAORRES.

### FASTRESC
- **Order:** 14
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from FAORRES in a standard format or standard units. FASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FASTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in FAORRES, and these results effectively have the same meaning; they could be represented in standard format in FASTRESC as "NEGATIVE".

### FASTRESN
- **Order:** 15
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from FASTRESC. FASTRESN should store all numeric test results or findings.

### FASTRESU
- **Order:** 16
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for FASTRESC and FASTRESN.

### FASTAT
- **Order:** 17
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that the measurement was not done. Should be null if a result exists in FAORRES.

### FAREASND
- **Order:** 18
- **Label:** Reason Not Performed
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a question was not answered. Example: "Subject refused". Used in conjunction with FASTAT when value is "NOT DONE".

### FALOC
- **Order:** 19
- **Label:** Location of the Finding About
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to specify the location of the clinical evaluation. Example: "ARM".

### FALAT
- **Order:** 20
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### FALOBXFL
- **Order:** 21
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### FABLFL
- **Order:** 22
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. The value should be "Y" or null. Note that FABLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### FAEVAL
- **Order:** 23
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR".

### VISITNUM
- **Order:** 24
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** 1. Clinical encounter number.  2. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 25
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** 1. Protocol-defined description of clinical encounter.  2. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 26
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 27
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 28
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP".

### FADTC
- **Order:** 29
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of findings assessment represented in ISO 8601 character format.

### FADY
- **Order:** 30
- **Label:** Study Day of Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** 1. Study day of collection, measured as integer days.  2. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.
---

## Cross References

### Controlled Terminology
- [Findings About Test Code (C101832)](../../terminology/core/findings_about.md) — FATESTCD
- [Findings About Test Name (C101833)](../../terminology/core/findings_about.md) — FATEST
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — FALOBXFL, FABLFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — FASTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — FAORRESU, FASTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — FALOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — FAEVAL
- [Laterality (C99073)](../../terminology/core/general_part2.md) — FALAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings About):** SR
- **Source Domain:** [AE](../AE/) — findings about adverse events
- **Source Domain:** [CM](../CM/) — findings about concomitant medications
- **Source Domain:** [PR](../PR/) — findings about procedures
- **Source Domain:** [EX](../EX/) — findings about exposure
- **Source Domain:** [EC](../EC/) — findings about exposure as collected
- **Source Domain:** [ML](../ML/) — findings about meals
- **Source Domain:** [SU](../SU/) — findings about substance use

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings About class definition](../../model/02_observation_classes.md)

## Source: `domains/FA/assumptions.md`

# FA — Assumptions

1. The Findings About domain shares all qualities and conventions of findings observations.

2. See Section 6.4.1, When to Use Findings About Events or Interventions; and Section 8.6.3, Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions; for guidance on deciding between the use of the FA domain and other SDTM structures.

3. See Section 6.4.2, Naming Findings About Domains, for advice on splitting the FA domain.

4. Some variables in the events and interventions domains (e.g., OCCUR, SEV, TOXGR) represent findings about the whole of the event or intervention. When FA is used to represent findings about a part of the event or intervention (i.e., the assessment has different timing from the event as a whole), the FATEST and FATESTCD values should be the same as the variable name and variable label in the corresponding event or intervention domain. See Section 6.4.3, Variables Unique to Findings About.
   a. Associations between some findings about cardiovascular interventions or events and their response codelists are described in the CV codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

5. When data collection establishes a relationship between FA records and an events or interventions record, the relationship should be represented in RELREC.
   a. The FAOBJ variable alone is not sufficient to establish a relationship, because an events or interventions dataset may have multiple records for the same topic (e.g., --TERM or --DECOD, --TRT or --DECOD).

6. Any Identifier variables, Timing variables, or Findings general observation-class qualifiers may be added to the FA domain, but the following qualifiers should generally not be used: --BODSYS, --MODIFY, --SEV, --TOXGR.

## Source: `domains/FA/examples.md`

# FA — Examples

## Example 1

The following example CRF collects severity and symptoms data at multiple time points about a migraine event, relative to dosing.

In this example trial, migraines and symptoms associated with migraines were considered clinical events rather than reportable adverse events. The migraine, its sponsor identifier (i.e., the "Migraine Reference Number" on the CRF), and its start date were represented in a CE record.

**ce.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CESEQ | CESPID | CETERM | CEDECOD | CESTDTC |
|-----|---------|--------|---------|-------|--------|--------|---------|---------|
| 1 | ABC | CE | ABC-123 | 1 | 90567 | Migraine | Migraine | 2007-05-16T10:30 |

The time the migraine medication was taken was recorded in the Exposure (EX) domain. This date also serves as the reference time point for the symptom assessments.

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXSPID | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC |
|-----|---------|--------|---------|-------|--------|-------|--------|--------|----------|----------|---------|-------|---------|---------|
| 1 | ABC | EX | ABC-123 | 1 | 4 | CURALL | 50 | mg | TABLET | ONCE | ORAL | TREATMENT | 2007-05-16T11:05 | 2007-05-16T11:05 |

The remaining data on the CRF were "snapshots" taken at 3 time points; in accordance with Section 6.4.1, When to Use Findings About Events or Interventions, criterion 1, these were represented as findings about events. The FACAT value "MIGRAINE SYMPTOMS" was used to represent the fact that these data were collected in a CRF module called "Migraine Symptoms Diary."

**Rows 1, 6, 11:** Severity of the migraine was represented with FATESTCD="SEV". This FATESTCD value is derived from the events class variable name --SEV, and represents the same assessment as CESEV, except that this assessment is at a point in time rather than for the event as a whole.
**Rows 2-5, 7-10, 12-15:** The presence of symptoms associated with migraine was represented with the name of the symptom in FAOBJ, as the data collected is about the occurrence of a particular symptom. The test code value "OCCUR" is derived from the events class variable name --OCCUR, but is an assessment at a point in time, rather than about the event as a whole. The relationship of these symptoms to migraine is represented in FACAT, which indicates that these data were collected in the Migraine Symptoms Diary.

**face.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FACAT | FAORRES | FASTRESC | FADTC | FATPT | FATPTNUM | FAELTM | FATPTREF |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|-------|---------|----------|-------|-------|----------|--------|----------|
| 1 | ABC | FA | ABC-123 | 1 | 90567 | SEV | Severity/Intensity | Migraine | MIGRAINE SYMPTOMS | SEVERE | SEVERE | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 2 | ABC | FA | ABC-123 | 2 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Light | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 3 | ABC | FA | ABC-123 | 3 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Sound | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 4 | ABC | FA | ABC-123 | 4 | 90567 | OCCUR | Occurrence Indicator | Nausea | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 5 | ABC | FA | ABC-123 | 5 | 90567 | OCCUR | Occurrence Indicator | Aura | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 6 | ABC | FA | ABC-123 | 6 | 90567 | SEV | Severity/Intensity | Migraine | MIGRAINE SYMPTOMS | MODERATE | MODERATE | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 7 | ABC | FA | ABC-123 | 7 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Light | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 8 | ABC | FA | ABC-123 | 8 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Sound | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 9 | ABC | FA | ABC-123 | 9 | 90567 | OCCUR | Occurrence Indicator | Nausea | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 10 | ABC | FA | ABC-123 | 10 | 90567 | OCCUR | Occurrence Indicator | Aura | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 11 | ABC | FA | ABC-123 | 11 | 90567 | SEV | Severity/Intensity | Migraine | MIGRAINE SYMPTOMS | MILD | MILD | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 12 | ABC | FA | ABC-123 | 12 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Light | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 13 | ABC | FA | ABC-123 | 13 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Sound | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 14 | ABC | FA | ABC-123 | 14 | 90567 | OCCUR | Occurrence Indicator | Nausea | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 15 | ABC | FA | ABC-123 | 15 | 90567 | OCCUR | Occurrence Indicator | Aura | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |

A dataset-level relationship in RELREC is based on the sponsor ID (--SPID) value, which was populated with a system-generated identifier unique to each iteration of this form.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | CE | | CESPID | | ONE | 1 |
| 2 | ABC | FA | | FASPID | | MANY | 1 |

## Example 2

This CRF collects details about injection site rash events at each visit, until resolved.

In this scenario, the injection site rash event was considered a reportable adverse event; therefore, the rash itself was represented in the AE domain. The rash assessment form collects a reference number for the AE, represented in AESPID. Certain required or expected variables have been omitted from the example dataset in consideration of space and clarity.

Additional data about the rash were collected at visits 3 and 4, which occurred 2 days and 9 days after the start of the rash. These data were represented in an FA dataset because they were not about the event as a whole (see Section 6.4.1, When to Use Findings About Events or Interventions, criterion 1). In addition, the measurement of the rash requires multiple variables (value and unit) for its representation and the numbers of various kinds of lesions within the rash are a set of similar assessments of the event (see Section 6.4.1, When to Use Findings About Events or Interventions, criterion 2).

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AESPID | AETERM | AEBODSYS | AELOC | AELAT | AESEV | AESER | AEACN | AESTDTC |
|-----|---------|--------|---------|-------|--------|--------|----------|-------|-------|-------|-------|-------|---------|
| 1 | XYZ | AE | XYZ-789 | 47869 | 5 | Injection site rash | General disorders and administration site conditions | ARM | LEFT | MILD | N | NOT APPLICABLE | 2007-05-10 |

**faae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FAORRES | FAORRESU | FASTRESC | FASTRESU | VISITNUM | FADTC |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|---------|----------|----------|----------|----------|-------|
| 1 | XYZ | FA | XYZ-789 | 123451 | 5 | LDIAM | Longest Diameter | Injection Site Rash | 2.5 | IN | 2.5 | IN | 3 | 2007-05-12 |
| 2 | XYZ | FA | XYZ-789 | 123452 | 5 | MACRNG | Number of Macules Range | Injection Site Rash | 26 to 100 | | 26 to 100 | | 3 | 2007-05-12 |
| 3 | XYZ | FA | XYZ-789 | 123453 | 5 | FAPRNG | Number of Papules Range | Injection Site Rash | 1 to 25 | | 1 to 25 | | 3 | 2007-05-12 |
| 4 | XYZ | FA | XYZ-789 | 123454 | 5 | VESRNG | Number of Vesicles Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 5 | XYZ | FA | XYZ-789 | 123455 | 5 | PUSRNG | Number of Pustules Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 6 | XYZ | FA | XYZ-789 | 123456 | 5 | SCBRNG | Number of Scabs Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 7 | XYZ | FA | XYZ-789 | 123457 | 5 | SCRRNG | Number of Scars Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 8 | XYZ | FA | XYZ-789 | 123459 | 5 | LDIAM | Longest Diameter | Injection Site Rash | 1 | IN | 1 | IN | 4 | 2007-05-19 |
| 9 | XYZ | FA | XYZ-789 | 123460 | 5 | MACRNG | Number of Macules Range | Injection Site Rash | 1 to 25 | | 1 to 25 | | 4 | 2007-05-19 |
| 10 | XYZ | FA | XYZ-789 | 123461 | 5 | FAPRNG | Number of Papules Range | Injection Site Rash | 1 to 25 | | 1 to 25 | | 4 | 2007-05-19 |
| 11 | XYZ | FA | XYZ-789 | 123462 | 5 | VESRNG | Number of Vesicles Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |
| 12 | XYZ | FA | XYZ-789 | 123463 | 5 | PUSRNG | Number of Pustules Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |
| 13 | XYZ | FA | XYZ-789 | 123464 | 5 | SCBRNG | Number of Scabs Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |
| 14 | XYZ | FA | XYZ-789 | 123465 | 5 | SCRRNG | Number of Scars Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |

The FA records were linked to the parent CE record via the AE reference number, which was used to populate both AESPID and FASPID.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | XYZ | AE | | AESPID | | ONE | 23 |
| 2 | XYZ | FA | | FASPID | | MANY | 23 |

## Example 3

This CRF collects information about rheumatoid arthritis. In this scenario, rheumatoid arthritis is a prerequisite for participation in an osteoporosis trial and was not collected as a Medical History (MH) event.

In this study, data were collected only at baseline. Because the occurrence and severity apply to the symptoms as a whole, they are represented in the MH domain. Note that the average duration of early morning stiffness cannot be represented in MHDUR because MHDUR would be the duration of the entire event, rather than the average of daily durations.

**Row 1:** Because the CRF specifically collected date of diagnosis for rheumatoid arthritis, MHEVDTYP is populated with DIAGNOSIS to indicate that the date in MHSTDTC is the date of diagnosis.
**Rows 2-6:** No start or end dates were collected for the symptoms, so the variable MHEVDTYP is not relevant for those records. MHEVDTYP is used only to specify the aspect of the event used to determine start and/or end dates.

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHDECOD | MHEVDTYP | MHCAT | MHSCAT | MHPRESP | MHOCCUR | MHSEV | MHDTC | MHSTDTC | MHEVLINT |
|-----|---------|--------|---------|-------|--------|---------|----------|-------|--------|---------|---------|-------|-------|---------|----------|
| 1 | ABC | MH | 001-001 | 1 | RHEUMATOID ARTHRITIS | Rheumatoid arthritis | DIAGNOSIS | RHEUMATOID ARTHRITIS HISTORY | | Y | Y | | | 2003 | -P6M |
| 2 | ABC | MH | 001-001 | 2 | JOINT STIFFNESS | Joint stiffness | | RHEUMATOID ARTHRITIS HISTORY | SYMPTOMS | Y | Y | SEVERE | 2006-08-13 | | -P6M |
| 3 | ABC | MH | 001-001 | 3 | JOINT SWELLING | Joint swelling | | RHEUMATOID ARTHRITIS HISTORY | SYMPTOMS | Y | Y | MODERATE | 2006-08-13 | | -P6M |
| 4 | ABC | MH | 001-001 | 4 | JOINT PAIN | Arthralgia | | RHEUMATOID ARTHRITIS HISTORY | SYMPTOMS | Y | Y | MODERATE | 2006-08-13 | | -P6M |
| 5 | ABC | MH | 001-001 | 5 | MALAISE | Malaise | | RHEUMATOID ARTHRITIS HISTORY | SYMPTOMS | Y | Y | MILD | 2006-08-13 | | -P6M |
| 6 | ABC | MH | 001-001 | 6 | EARLY MORNING STIFFNESS | Stiffness | | RHEUMATOID ARTHRITIS HISTORY | SYMPTOMS | Y | | | 2006-08-13 | | -P6M |

The average duration of early morning stiffness would be represented in ISO 8601 duration format as a supplemental qualifier.

**suppmh.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC | MH | 001-001 | MHSEQ | 6 | MHAVDDUR | Average Daily Duration | PT1H30M | CRF | |

## Example 4

In this example, the occurrence of prespecified adverse events was solicited at every visit and the visit date was used as the date of collection. The data collected meet criterion 3 in Section 6.4.1, When to Use Findings About Events or Interventions; that is, data that indicate the occurrence of prespecified AEs.

**Rows 1, 4:** "Headache" was reported at both visits.
**Rows 2, 5:** "Respiratory infection" was not present at either visit.
**Row 3:** The investigator did not ask the subject about the occurrence of nausea. This was represented by FASTAT="NOT DONE".
**Row 6:** "Nausea" was reported at visit 3.

**faae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FATESTCD | FATEST | FAOBJ | FAORRES | FASTRESC | FASTAT | VISITNUM | VISIT | FADTC | FAEVINTX |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|----------|--------|----------|-------|-------|----------|
| 1 | ABC101 | FA | 1234 | 1 | OCCUR | Occurrence Indicator | Headache | Y | Y | | 2 | VISIT 2 | 2005-10-01 | SINCE LAST VISIT |
| 2 | ABC101 | FA | 1234 | 2 | OCCUR | Occurrence Indicator | Respiratory Infection | N | N | | 2 | VISIT 2 | 2005-10-01 | SINCE LAST VISIT |
| 3 | ABC101 | FA | 1234 | 3 | OCCUR | Occurrence Indicator | Nausea | | | NOT DONE | 2 | VISIT 2 | 2005-10-01 | SINCE LAST VISIT |
| 4 | ABC101 | FA | 1234 | 4 | OCCUR | Occurrence Indicator | Headache | Y | Y | | 3 | VISIT 3 | 2005-10-10 | SINCE LAST VISIT |
| 5 | ABC101 | FA | 1234 | 5 | OCCUR | Occurrence Indicator | Respiratory Infection | N | N | | 3 | VISIT 3 | 2005-10-10 | SINCE LAST VISIT |
| 6 | ABC101 | FA | 1234 | 6 | OCCUR | Occurrence Indicator | Nausea | Y | Y | | 3 | VISIT 3 | 2005-10-10 | SINCE LAST VISIT |

For each prespecified adverse event for which FAORRES = "Y", the adverse event has a record in the AE domain with AEPRESP = "Y". No relationship was collected to link the FAAE record for the occurrence indicator test with the AE entries, so no RELREC was created.

Note that not all AE expected variables are included in the following example.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEDECOD | AEPRESP | AEBODSYS | AESEV | AEACN | AESTDTC | AEENDTC |
|-----|---------|--------|---------|-------|--------|---------|---------|----------|-------|-------|---------|---------|
| 1 | ABC101 | AE | 1234 | 1 | Headache | Headache | Y | Nervous system disorders | MILD | NONE | 2005-09-30 | 2005-10-03 |
| 2 | ABC101 | AE | 1234 | 2 | Nausea | Nausea | Y | Gastrointestinal disorders | MODERATE | NONE | 2005-10-08 | 2005-10-09 |

**Row 1:** Comparison of this AE record with the FA dataset records for "Headache" shows that there are 2 records with FAOBJ="Headache". FAORRES="Y" indicates that this AE record is associated with both FA records, because this headache started before visit 2 and ended between visits 2 and 3.

**Row 2:** Comparison of this AE record with the FA dataset shows that this AE started and ended in the time between visits 2 and 3, and is consistent with the FA response for FAOBJ="Nausea" for visit 3.

## Example 5

In this example, data about prespecified symptoms of the disease under study were collected on a daily basis. Although the date of the assessment was captured in the CRF header (not shown), start and end timing of the prespecified symptoms was not.

The collected data were represented in FA because they meet criterion 1 in Section 6.4.1, When to Use Findings About Events or Interventions, that is, data that do not describe an event or intervention as a whole. In addition, the volume of vomit data met criterion 2 data ("about" an event or intervention), having qualifiers that can be represented in Findings variables (e.g., units, method).

This SDTM example represents data from 2 visits for 1 subject. FAEVINTX indicates that assessments were for the previous 24 hours.

**Rows 1-4:** Show the results for the vomiting tests at visit 1. Because the number of episodes was recorded as ">10", this is represented in FASTRESC but not in FASTRESN.
**Rows 5-7:** Show the results for the diarrhea tests at visit 1.
**Rows 8-10:** Show the results for the nausea tests at visit 1.
**Row 11:** Shows that vomiting did not occur in the 24 hours before visit 2; thus, volume, number of episodes, and severity were not applicable.
**Rows 12-14:** Show the results for the diarrhea tests at visit 2.
**Row 15:** Indicates that the occurrence of nausea was not assessed at visit 2.

**face.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FATESTCD | FATEST | FAOBJ | FACAT | FAORRES | FAORRESU | FASTRESC | FASTRESN | FASTRESU | FASTAT | VISITNUM | VISIT | FADTC | FAEVLINT |
|-----|---------|--------|---------|-------|----------|--------|-------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|----------|
| 1 | XYZ | FA | XYZ-701-002 | 1 | OCCUR | Occurrence Indicator | Vomiting | GERD SYMPTOMS | Y | | Y | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 2 | XYZ | FA | XYZ-701-002 | 2 | VOL | Volume | Vomiting | GERD SYMPTOMS | 250 | mL | 250 | 250 | mL | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 3 | XYZ | FA | XYZ-701-002 | 3 | NUMEPISO | Number of Episodes | Vomiting | GERD SYMPTOMS | >10 | | >10 | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 4 | XYZ | FA | XYZ-701-002 | 4 | SEV | Severity/Intensity | Vomiting | GERD SYMPTOMS | SEVERE | | SEVERE | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 5 | XYZ | FA | XYZ-701-002 | 5 | OCCUR | Occurrence Indicator | Diarrhea | GERD SYMPTOMS | Y | | Y | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 6 | XYZ | FA | XYZ-701-002 | 6 | NUMEPISO | Number of Episodes | Diarrhea | GERD SYMPTOMS | 2 | | 2 | 2 | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 7 | XYZ | FA | XYZ-701-002 | 7 | SEV | Severity/Intensity | Diarrhea | GERD SYMPTOMS | SEVERE | | SEVERE | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 8 | XYZ | FA | XYZ-701-002 | 8 | OCCUR | Occurrence Indicator | Nausea | GERD SYMPTOMS | Y | | Y | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 9 | XYZ | FA | XYZ-701-002 | 9 | NUMEPISO | Number of Episodes | Nausea | GERD SYMPTOMS | 1 | | 1 | 1 | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 10 | XYZ | FA | XYZ-701-002 | 10 | SEV | Severity/Intensity | Nausea | GERD SYMPTOMS | MODERATE | | MODERATE | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 11 | XYZ | FA | XYZ-701-002 | 11 | OCCUR | Occurrence Indicator | Vomiting | GERD SYMPTOMS | N | | N | | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 12 | XYZ | FA | XYZ-701-002 | 12 | OCCUR | Occurrence Indicator | Diarrhea | GERD SYMPTOMS | Y | | Y | | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 13 | XYZ | FA | XYZ-701-002 | 13 | NUMEPISO | Number of Episodes | Diarrhea | GERD SYMPTOMS | 1 | | 1 | 1 | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 14 | XYZ | FA | XYZ-701-002 | 14 | SEV | Severity/Intensity | Diarrhea | GERD SYMPTOMS | SEVERE | | SEVERE | | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 15 | XYZ | FA | XYZ-701-002 | 15 | OCCUR | Occurrence Indicator | Nausea | GERD SYMPTOMS | | | | | | NOT DONE | 2 | VISIT 2 | 2006-02-03 | -PT24H |

## Example 6

In this example, the sponsor's definition of "event" meant that 1 record would be created for each adverse event, covering it from start to finish (see Section 6.2.1, Adverse Events, assumption 6.4). The AE module also collected information about severity at each visit.

An electronic data collection instrument would probably be constructed as 2 related modules:
- A module for the adverse event, where a record would be entered for each event
- A module for the severity assessment, where a record would be entered for each assessment

*Note: The FA Example 6 CRF shows severity assessed at Visits 2-6 for up to 3 concurrent AEs per subject. The data collected about severity at each visit represents snapshots or slices of the AE over time, meeting criterion 1 for When to Use Findings About Events or Interventions.*

AE collection started after visit 1, so the first severity data was collected at visit 2.

The collected data met criterion 1 in Section 6.4.1, When to Use Findings About Events or Interventions, for data that do not describe an event or intervention as a whole.

In this example, the sponsor populated AESEV with the maximum severity over the course of the event. This was not directly collected, but rather determined from the weekly maximum severity assessments collected on the CRF. For clarity, only selected variables in the AE dataset are shown here.

**ae.xpt**

| Row | DOMAIN | USUBJID | AESEQ | AESPID | AETERM | AEDECOD | AESEV | AESTDTC | AEENDTC |
|-----|--------|---------|-------|--------|--------|---------|-------|---------|---------|
| 1 | AE | 123 | 1 | 1 | Morning queasiness | Nausea | MODERATE | 2006-02-01 | 2006-02-23 |
| 2 | AE | 123 | 2 | 2 | Watery stools | Diarrhea | MILD | 2006-02-01 | 2006-02-15 |

The values in FAOBJ are the values from AEDECOD, which were assigned during coding, rather than directly collected. The values in FASPID are the AE identifiers from AESPID. FAEVINTX indicates that the evaluation was for the period since the last visit.

**Rows 1-4:** Show severity data collected at the 4 visits that occurred between the start and end of the AE "Morning queasiness". FAOBJ=NAUSEA, which is the value of AEDECOD in the associated AE record.

**Rows 5-6:** Show severity data collected at the 2 visits that occurred between the start and end of the AE "Watery stools." FAOBJ=DIARRHEA, which is the value of AEDECOD in the associated AE record.

**faae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FAORRES | FACOLSRT | VISITNUM | VISIT | FADTC | FAEVINTX |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|---------|----------|----------|-------|-------|----------|
| 1 | XYZ | FA | XYZ-US-701-002 | 1 | 1 | SEV | Severity/Intensity | Nausea | MILD | MAXIMUM | 2 | VISIT 2 | 2006-02-02 | SINCE LAST VISIT |
| 2 | XYZ | FA | XYZ-US-701-002 | 2 | 1 | SEV | Severity/Intensity | Nausea | MODERATE | MAXIMUM | 3 | VISIT 3 | 2006-02-09 | SINCE LAST VISIT |
| 3 | XYZ | FA | XYZ-US-701-002 | 3 | 1 | SEV | Severity/Intensity | Nausea | MODERATE | MAXIMUM | 4 | VISIT 4 | 2006-02-16 | SINCE LAST VISIT |
| 4 | XYZ | FA | XYZ-US-701-002 | 4 | 1 | SEV | Severity/Intensity | Nausea | MILD | MAXIMUM | 5 | VISIT 5 | 2006-02-23 | SINCE LAST VISIT |
| 5 | XYZ | FA | XYZ-US-701-002 | 5 | 2 | SEV | Severity/Intensity | Diarrhea | MILD | MAXIMUM | 2 | VISIT 2 | 2006-02-02 | SINCE LAST VISIT |
| 6 | XYZ | FA | XYZ-US-701-002 | 6 | 2 | SEV | Severity/Intensity | Diarrhea | MILD | MAXIMUM | 3 | VISIT 3 | 2006-02-09 | SINCE LAST VISIT |

Because the AE identifier (AESPID) was included in the FA dataset, AE and FA data can be related with a dataset-to-dataset relationship.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | AE | | AESPID | | ONE | 1 |
| 2 | ABC | FA | | FASPID | | MANY | 1 |

## Source: `domains/SR/spec.md`

# SR — Skin Response

> Class: Findings About | Structure: One record per finding, per object, per time point, per visit per subject

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

### SRSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### SRGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### SRREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier. Example: "Specimen ID".

### SRSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### SRTESTCD
- **Order:** 8
- **Label:** Skin Response Test or Exam Short Name
- **Type:** Char
- **Controlled Terms:** C112024
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in SRTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SRTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SRTESTCD cannot contain characters other than letters, numbers, or underscores.

### SRTEST
- **Order:** 9
- **Label:** Skin Response Test or Examination Name
- **Type:** Char
- **Controlled Terms:** C112023
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in SRTEST cannot be longer than 40 characters. Example: "Wheal Diameter".

### SROBJ
- **Order:** 10
- **Label:** Object of the Observation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the dose of the immunogenic material or the allergen associated with the response (e.g., "Johnson Grass IgE 0.15 BAU mL").

### SRCAT
- **Order:** 11
- **Label:** Category for Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values across subjects.

### SRSCAT
- **Order:** 12
- **Label:** Subcategory for Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of SRCAT values.

### SRORRES
- **Order:** 13
- **Label:** Results or Findings in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Results of measurement or finding as originally received or collected.

### SRORRESU
- **Order:** 14
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for SRORRES. Example: "mm".

### SRSTRESC
- **Order:** 15
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from SRORRES, in a standard format or in standard units. SRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SRSTRESN.

### SRSTRESN
- **Order:** 16
- **Label:** Numeric Results/Findings in Std. Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from SRSTRESC. SRSTRESN should store all numeric test results or findings.

### SRSTRESU
- **Order:** 17
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized units used for SRSTRESC and SRSTRESN. Example: "mm".

### SRSTAT
- **Order:** 18
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate exam not done. Should be null if a result exists in SRORRES.

### SRREASND
- **Order:** 19
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Used in conjunction with SRSTAT when value is "NOT DONE".

### SRNAM
- **Order:** 20
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the laboratory or vendor who provided the test results.

### SRSPEC
- **Order:** 21
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the types of specimen used for a measurement. Example: "SKIN".

### SRLOC
- **Order:** 22
- **Label:** Location Used for Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Location relevant to the collection of the measurement.

### SRLAT
- **Order:** 23
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location further detailing laterality of intervention administration. Examples: "RIGHT", "LEFT", "BILATERAL".

### SRMETHOD
- **Order:** 24
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of test or examination. Examples: "ELISA", "EIA", "MICRONEUTRALIZATION ASSAY", "PLAQUE REDUCTION NEUTRALIZATION ASSAY".

### SRLOBXFL
- **Order:** 25
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### SRBLFL
- **Order:** 26
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. The value should be "Y" or null. Note that SRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### SREVAL
- **Order:** 27
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of person who provided evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR".

### VISITNUM
- **Order:** 28
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 29
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 30
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 31
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 32
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", and "FOLLOW-UP".

### SRDTC
- **Order:** 33
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation represented in ISO 8601.

### SRDY
- **Order:** 34
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to sponsor- defined RFSTDTC in Demographics.

### SRTPT
- **Order:** 35
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See SRTPTNUM and SRTPTREF. Examples: "START", "5 MIN POST".

### SRTPTNUM
- **Order:** 36
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of SRTPT to aid in sorting.

### SRELTM
- **Order:** 37
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a fixed time point reference (SRTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by SRTPTREF.

### SRTPTREF
- **Order:** 38
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by SRELTM, SRTPTNUM, and SRTPT. Example: "INTRADERMAL INJECTION".

### SRRFTDTC
- **Order:** 39
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, SRTPTREF.
---

## Cross References

### Controlled Terminology
- [Skin Response Test Name (C112023)](../../terminology/core/findings_about.md) — SRTEST
- [Skin Response Test Code (C112024)](../../terminology/core/findings_about.md) — SRTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — SRLOBXFL, SRBLFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — SRSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — SRORRESU, SRSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — SRLOC
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — SRSPEC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — SREVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — SRMETHOD
- [Laterality (C99073)](../../terminology/core/general_part2.md) — SRLAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings About):** FA
- **Source Domain:** [AE](../AE/) — device-related findings about AEs
- **Source Domain:** [CM](../CM/) — device-related findings about treatments
- **Source Domain:** [PR](../PR/) — device-related findings about procedures

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings About class definition](../../model/02_observation_classes.md)

## Source: `domains/SR/assumptions.md`

# SR — Assumptions

1. The Skin Response (SR) domain is used to represent findings about an intervention, but it has its own domain code, SR, rather than the domain code FA.

2. This domain is intended specifically for tests of the immune response to substances that are intended to provoke such a response (e.g., allergens used in allergy testing). SR is not intended for other injection-site reactions, including reactogenicity events that may follow a vaccine administration.

3. Because a subject is typically exposed to many test materials at the same time, SROBJ is needed to represent the test material for each response record. The method of assessment could be a skin-prick test, a skin-scratch test, or other method of introducing the challenge substance into the skin.

4. Any Identifier variables, Timing variables, or Findings general observation class qualifiers may be added to the SR domain, but the following qualifiers would not generally be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --LOINC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

## Source: `domains/SR/examples.md`

# SR — Examples

## Example 1

In this example, the subject is dosed with increasing concentrations of Johnson grass IgE.

**Rows 1-4:** Show responses associated with the administration of a histamine control.
**Rows 5-8:** Show responses associated with the administration of Johnson grass IgE. These records describe the dose response to different concentrations of Johnson grass IgE antigen, as reflected in SROBJ.

All rows show a specific location on the back (e.g., SITE1), represented in FOCID.

**sr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FOCID | SRSEQ | SRTESTCD | SRTEST | SROBJ | SRORRES | SRORRESU | SRSTRESC | SRSTRESN | SRSTRESU | SRLOC | VISITNUM | VISIT |
|-----|---------|--------|---------|-------|-------|----------|--------|-------|---------|----------|----------|----------|----------|-------|----------|-------|
| 1 | SPI-001 | SR | SPI-001-11035 | SITE1 | 1 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 5 | mm | 5 | 5 | mm | BACK | 1 | VISIT 1 |
| 2 | SPI-001 | SR | SPI-001-11035 | SITE2 | 2 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 4 | mm | 4 | 4 | mm | BACK | 1 | VISIT 1 |
| 3 | SPI-001 | SR | SPI-001-11035 | SITE3 | 3 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 5 | mm | 5 | 5 | mm | BACK | 1 | VISIT 1 |
| 4 | SPI-001 | SR | SPI-001-11035 | SITE4 | 4 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 5 | mm | 5 | 5 | mm | BACK | 1 | VISIT 1 |
| 5 | SPI-001 | SR | SPI-001-11035 | SITE5 | 5 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.05 BAU/mL | 10 | mm | 10 | 10 | mm | BACK | 1 | VISIT 1 |
| 6 | SPI-001 | SR | SPI-001-11035 | SITE6 | 6 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.10 BAU/mL | 11 | mm | 11 | 11 | mm | BACK | 1 | VISIT 1 |
| 7 | SPI-001 | SR | SPI-001-11035 | SITE7 | 7 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.15 BAU/mL | 20 | mm | 20 | 20 | mm | BACK | 1 | VISIT 1 |
| 8 | SPI-001 | SR | SPI-001-11035 | SITE8 | 8 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.20 BAU/mL | 30 | mm | 30 | 30 | mm | BACK | 1 | VISIT 1 |

## Example 2

In this example, the study product dose, Dog Epi IgG, was administered at increasing concentrations. The size of the wheal is being measured (reaction to Dog Epi IgG) to evaluate the efficacy of the Dog Epi IgG extract versus a negative control (NC) and a positive control (PC) in the testing of allergenic extracts. While SROBJ is populated with information about the substance administered, full details regarding the study product would be submitted in the Exposure (EX) dataset. The relationship between SR records and EX records would be represented using RELREC.

**Rows 1-6:** Show the response (description and reaction grade) to the study product at a series of different dose levels, the latter reflected in SROBJ. The descriptions of SRORRES values are correlated to a grade, and the grade values are stored in SRSTRESC.
**Rows 7-12:** Show the results of wheal diameter measurements in response to the study product at a series of different dose levels.

**sr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SRSEQ | SRSPID | SRTESTCD | SRTEST | SROBJ | SRORRES | SRORRESU | SRSTRESC | SRSTRESN | SRSTRESU | SRLOC | VISITNUM | VISIT |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|---------|----------|----------|----------|----------|-------|----------|-------|
| 1 | CC-001 | SR | CC-001-101 | 1 | 1 | REACTGR | Reaction Grade | Dog Epi 0 mg | NEGATIVE | | NEGATIVE | | | FOREARM | 1 | WEEK 1 |
| 2 | CC-001 | SR | CC-001-101 | 2 | 2 | REACTGR | Reaction Grade | Dog Epi 0.1 mg | NEGATIVE | | NEGATIVE | | | FOREARM | 1 | WEEK 1 |
| 3 | CC-001 | SR | CC-001-101 | 3 | 3 | REACTGR | Reaction Grade | Dog Epi 0.5 mg | ERYTHEMA, INFILTRATION, POSSIBLY DISCRETE PAPULES | | 1+ | | | FOREARM | 1 | WEEK 1 |
| 4 | CC-001 | SR | CC-001-101 | 4 | 4 | REACTGR | Reaction Grade | Dog Epi 1 mg | ERYTHEMA, INFILTRATION, PAPULES, VESICLES | | 2+ | | | FOREARM | 1 | WEEK 1 |
| 5 | CC-001 | SR | CC-001-101 | 5 | 5 | REACTGR | Reaction Grade | Dog Epi 1.5 mg | ERYTHEMA, INFILTRATION, PAPULES, VESICLES | | 2+ | | | FOREARM | 1 | WEEK 1 |
| 6 | CC-001 | SR | CC-001-101 | 6 | 6 | REACTGR | Reaction Grade | Dog Epi 2 mg | ERYTHEMA, INFILTRATION, PAPULES, COALESCING VESICLES | | 3+ | | | FOREARM | 1 | WEEK 1 |
| 7 | CC-001 | SR | CC-001-101 | 7 | 7 | FLRMDIAM | Flare Mean Diameter | Dog Epi 0 mg | 5 | mm | 5 | 5 | mm | FOREARM | 1 | WEEK 1 |
| 8 | CC-001 | SR | CC-001-101 | 8 | 8 | FLRMDIAM | Flare Mean Diameter | Dog Epi 0.1 mg | 10 | mm | 10 | 10 | mm | FOREARM | 1 | WEEK 1 |
| 9 | CC-001 | SR | CC-001-101 | 9 | 9 | FLRMDIAM | Flare Mean Diameter | Dog Epi 0.5 mg | 22 | mm | 22 | 22 | mm | FOREARM | 1 | WEEK 1 |
| 10 | CC-001 | SR | CC-001-101 | 10 | 10 | FLRMDIAM | Flare Mean Diameter | Dog Epi 1 mg | 100 | mm | 100 | 100 | mm | FOREARM | 1 | WEEK 1 |
| 11 | CC-001 | SR | CC-001-101 | 11 | 11 | FLRMDIAM | Flare Mean Diameter | Dog Epi 1.5 mg | 1 | mm | 1 | 1 | mm | FOREARM | 1 | WEEK 1 |
| 12 | CC-001 | SR | CC-001-101 | 12 | 12 | FLRMDIAM | Flare Mean Diameter | Dog Epi 2 mg | 8 | mm | 8 | 8 | mm | FOREARM | 1 | WEEK 1 |

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSPID | EXTRT | EXDOSE | EXDOSEU | EXROUTE | EXLOC |
|-----|---------|--------|---------|--------|-------|--------|---------|---------|-------|
| 1 | CC-001 | EX | 101 | 1 | Dog Epi IgG | 0 | mg | CUTANEOUS | FOREARM |
| 2 | CC-001 | EX | 101 | 2 | Dog Epi IgG | 0.1 | mg | CUTANEOUS | FOREARM |
| 3 | CC-001 | EX | 101 | 3 | Dog Epi IgG | 0.5 | mg | CUTANEOUS | FOREARM |
| 4 | CC-001 | EX | 101 | 4 | Dog Epi IgG | 1 | mg | CUTANEOUS | FOREARM |
| 5 | CC-001 | EX | 101 | 5 | Dog Epi IgG | 1.5 | mg | CUTANEOUS | FOREARM |
| 6 | CC-001 | EX | 101 | 6 | Dog Epi IgG | 2 | mg | CUTANEOUS | FOREARM |

The relationships between SR and EX records are represented at the record level in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | CC-001 | SR | CC-001-101 | SRSPID | 1 | | R1 |
| 2 | CC-001 | EX | CC-001-101 | EXSPID | 1 | | R1 |
| 3 | CC-001 | SR | CC-001-101 | SRSPID | 7 | | R1 |
| 4 | CC-001 | SR | CC-001-101 | SRSPID | 2 | | R2 |
| 5 | CC-001 | EX | CC-001-101 | EXSPID | 2 | | R2 |
| 6 | CC-001 | SR | CC-001-101 | SRSPID | 8 | | R2 |
| 7 | CC-001 | SR | CC-001-101 | SRSPID | 3 | | R3 |
| 8 | CC-001 | EX | CC-001-101 | EXSPID | 3 | | R3 |
| 9 | CC-001 | SR | CC-001-101 | SRSPID | 9 | | R3 |
| 10 | CC-001 | SR | CC-001-101 | SRSPID | 4 | | R4 |
| 11 | CC-001 | SR | CC-001-101 | SRSPID | 10 | | R4 |
| 12 | CC-001 | EX | CC-001-101 | EXSPID | 4 | | R4 |
| 13 | CC-001 | SR | CC-001-101 | SRSPID | 5 | | R5 |
| 14 | CC-001 | SR | CC-001-101 | SRSPID | 11 | | R5 |
| 15 | CC-001 | EX | CC-001-101 | EXSPID | 5 | | R5 |
| 16 | CC-001 | SR | CC-001-101 | SRSPID | 6 | | R6 |
| 17 | CC-001 | SR | CC-001-101 | SRSPID | 12 | | R6 |
| 18 | CC-001 | EX | CC-001-101 | EXSPID | 6 | | R6 |

## Example 3

This example shows the results from a tuberculin purified protein derivative (PPD) skin test administered using the Mantoux technique. The subject was given an intradermal injection of standard PPD (i.e., PPD-S) in the left forearm at visit 1; see the Procedure Agents (AG) record below. At visit 2, the induration diameter and presence of blistering were recorded. Because the tuberculin PPD skin test cannot be interpreted using the induration diameter and blistering alone (e.g., risk for being infected with TB must also be considered), the interpretation of the skin test resides in its own row. Time point variables show that the planned time for reading the test was 48 hours after Mantoux administration. However, a comparison of datetime values in SRDTC and SRRFTDTC shows that in this case the test was read at 53 hours and 56 minutes after Mantoux administration.

**Row 1:** Shows the longest diameter in millimeters of the induration after receiving an intradermal injection of 0.1 mL containing 5TU of PPD-S in the left forearm.
**Row 2:** Shows the presence of blistering at the tuberculin PPD skin test site.
**Row 3:** Shows the interpretation of the tuberculin PPD skin test. SRGRPID is used to tie together the results to the interpretation.

**sr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SRSEQ | SRGRPID | SRTESTCD | SRTEST | SROBJ | SRORRES | SRORRESU | SRSTRESC | SRSTRESN | SRSTRESU | SRLOC | SRLAT | SRMETHOD | VISITNUM | VISIT | EPOCH | SRDTC | SRTPT | SRELTM | SRTPTREF | SRRFTDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|-------|-------|----------|----------|-------|-------|-------|-------|--------|----------|----------|
| 1 | ABC | SR | ABC-001 | 1 | 1 | DRLDOM | Induration Longest Diameter | Tuberculin PPD-S | 16 | mm | 16 | 16 | mm | FOREARM | LEFT | RULER | 2 | VISIT 2 | OPEN LABEL TREATMENT | 2011-01-19T14:26 | 48 H | PT48H | MANTOUX ADMINISTRATION | 2011-01-17T08:30:00 |
| 2 | ABC | SR | ABC-001 | 2 | 1 | BLISTIND | Blistering Indicator | Tuberculin PPD-S | Y | | Y | | | FOREARM | LEFT | | 2 | VISIT 2 | OPEN LABEL TREATMENT | 2011-01-19T14:26 | 48 H | PT48H | MANTOUX ADMINISTRATION | 2011-01-17T08:30:00 |
| 3 | ABC | SR | ABC-001 | 3 | 1 | INTP | Interpretation | Tuberculin PPD-S | POSITIVE | | POSITIVE | | | | | | 2 | VISIT 2 | OPEN LABEL TREATMENT | 2011-01-19T14:26 | 48 H | PT48H | MANTOUX ADMINISTRATION | 2011-01-17T08:30:00 |

The tuberculin PPD skin test administration was represented in the AG domain.

**ag.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AGSEQ | AGTRT | AGDOSE | AGDOSU | AGVAMT | AGVAMTU | VISITNUM | VISIT | EPOCH | AGSTDTC |
|-----|---------|--------|---------|-------|-------|--------|--------|--------|---------|----------|-------|-------|---------|
| 1 | ABC | AG | ABC-001 | 1 | tuberculin PPD-S | 5 | tuberculin unit | 0.1 | mL | 1 | VISIT 1 | OPEN LABEL TREATMENT | 2011-01-17T08:30:00 |

Relationships between SR and AG records were shown in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | SR | ABC-001 | SRGRPID | 1 | | R1 |
| 2 | ABC | AG | ABC-001 | AGSEQ | 1 | | R1 |
