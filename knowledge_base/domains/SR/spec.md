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
