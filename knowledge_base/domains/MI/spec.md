# MI — Microscopic Findings

> Class: Findings | Structure: One record per finding per specimen per subject

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

### MISEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### MIGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject. This is not the treatment group number.

### MIREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier. Example: specimen barcode number.

### MISPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: line number from the MI Findings page.

### MITESTCD
- **Order:** 8
- **Label:** Microscopic Examination Short Name
- **Type:** Char
- **Controlled Terms:** C132263
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in MITEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MITESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MITESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HER2", "BRCA1", "TTF1".

### MITEST
- **Order:** 9
- **Label:** Microscopic Examination Name
- **Type:** Char
- **Controlled Terms:** C132262
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in MITEST cannot be longer than 40 characters. Examples: "Human Epidermal Growth Factor Receptor 2", "Breast Cancer Susceptibility Gene 1", "Thyroid Transcription Factor 1".

### MITSTDTL
- **Order:** 10
- **Label:** Microscopic Examination Detail
- **Type:** Char
- **Controlled Terms:** C125922
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of the test performed in producing the MI result. This would be used to represent specific attributes, such as intensity score or percentage of cells displaying presence of the biomarker or compound.

### MICAT
- **Order:** 11
- **Label:** Category for Microscopic Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records.

### MISCAT
- **Order:** 12
- **Label:** Subcategory for Microscopic Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of MICAT.

### MIORRES
- **Order:** 13
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the histopathology measurement or finding as originally received or collected.

### MIORRESU
- **Order:** 14
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original unit for MIORRES.

### MISTRESC
- **Order:** 15
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from MIORRES in a standard format or standard units. MISTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MISTRESN.

### MISTRESN
- **Order:** 16
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from MISTRESC. MISTRESN should store all numeric test results or findings.

### MISTRESU
- **Order:** 17
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for MISTRESC and MISTRESN.

### MIRESCAT
- **Order:** 18
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding. Examples: "MALIGNANT" or "BENIGN" for tumor findings.

### MISTAT
- **Order:** 19
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate examination not done or result is missing. Should be null if a result exists in MIORRES or have a value of "NOT DONE" when MIORRES = "NULL".

### MIREASND
- **Order:** 20
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with MISTAT when value is NOT DONE. Examples: "SAMPLE AUTOLYZED", "SPECIMEN LOST".

### MINAM
- **Order:** 21
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor (e.g., laboratory) that provided the test results.

### MISPEC
- **Order:** 22
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Subject of the observation. Defines the type of specimen used for a measurement. Examples: "TISSUE", "BLOOD", "BONE MARROW".

### MISPCCND
- **Order:** 23
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Free or standardized text describing the condition of the specimen. Example: "AUTOLYZED".

### MILOC
- **Order:** 24
- **Label:** Specimen Collection Location
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Location relevant to the collection of the specimen. Examples: "LUNG", "KNEE JOINT", "ARM", "THIGH".

### MILAT
- **Order:** 25
- **Label:** Specimen Laterality within Subject
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for laterality of the location of the specimen in MILOC. Examples: "LEFT", "RIGHT", "BILATERAL".

### MIDIR
- **Order:** 26
- **Label:** Specimen Directionality within Subject
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for directionality of the location of the specimen in MILOC. Examples: "DORSAL", "PROXIMAL".

### MIMETHOD
- **Order:** 27
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. This could include the technique or type of staining used for the slides. Examples: "IHC", "Crystal violet", "Safranin", "Trypan blue", or "Propidium iodide".

### MILOBXFL
- **Order:** 28
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### MIBLFL
- **Order:** 29
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. The value should be "Y" or null. Note that MIBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### MIEVAL
- **Order:** 30
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Example: "PATHOLOGIST", "PEER REVIEW", "SPONSOR PATHOLOGIST".

### VISITNUM
- **Order:** 31
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 32
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 33
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 34
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 35
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the specimen was collected.

### MIDTC
- **Order:** 36
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection, in ISO 8601 format.

### MIDY
- **Order:** 37
- **Label:** Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.
---

## Cross References

### Controlled Terminology
- [Microscopic Findings Test Details (C125922)](../../terminology/core/mi.md) — MITSTDTL
- [SDTM Microscopic Findings Test Name (C132262)](../../terminology/core/mi.md) — MITEST
- [SDTM Microscopic Findings Test Code (C132263)](../../terminology/core/mi.md) — MITESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — MILOBXFL, MIBLFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — MISTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — MIORRESU, MISTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — MILOC
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — MISPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — MISPEC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — MIEVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — MIMETHOD
- [Laterality (C99073)](../../terminology/core/general_part2.md) — MILAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — MIDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Related Findings:** [MB](../MB/) — microbiology organism identification

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)
