# TR — Tumor/Lesion Results

> Class: Findings | Structure: One record per tumor measurement/assessment per visit per subject per assessor

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

### TRSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number.

### TRGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain.

### TRREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier.

### TRSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### TRLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifier used to link the assessment result records to the individual tumor/lesion identification record in TU domain.

### TRLNKGRP
- **Order:** 9
- **Label:** Link Group
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to group and link all of the measurement/assessment records used in the assessment of the response record in the RS domain.

### TRTESTCD
- **Order:** 10
- **Label:** Tumor/Lesion Assessment Short Name
- **Type:** Char
- **Controlled Terms:** C96779
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the TEST in TRTEST. TRTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TUMSTATE", "DIAMETER", "LESSCIND", "LESRVIND". See assumption 3.

### TRTEST
- **Order:** 11
- **Label:** Tumor/Lesion Assessment Test Name
- **Type:** Char
- **Controlled Terms:** C96778
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in TRTEST cannot be longer than 40 characters. Examples: "Tumor State", "Diameter", "Volume", "Lesion Success Indicator", "Lesion Revascularization Indicator". See assumption 3.

### TRORRES
- **Order:** 12
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the tumor/lesion measurement/assessment as originally received or collected.

### TRORRESU
- **Order:** 13
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for TRORRES. Example: "mm".

### TRSTRESC
- **Order:** 14
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C124309
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from TRORRES, in a standard format or standard units. TRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in TRSTRESN.

### TRSTRESN
- **Order:** 15
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from TRSTRESC. TRSTRESN should store all numeric test results or findings.

### TRSTRESU
- **Order:** 16
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for TRSTRESN.

### TRSTAT
- **Order:** 17
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Should be null if a result exists in TRORRES.

### TRREASND
- **Order:** 18
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Examples: "SCAN NOT PERFORMED", "NOT ASSESSABLE: IMAGE OBSCURED TUMOR". Used in conjunction with TRSTAT when value is "NOT DONE".

### TRNAM
- **Order:** 19
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the vendor that performed the tumor/lesion measurement or assessment. This column can be left null when the investigator provides the complete set of data in the domain.

### TRMETHOD
- **Order:** 20
- **Label:** Method Used to Identify the Tumor/Lesion
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Method used to measure the tumor/lesion/location of interest. Examples: "MRI", "CT SCAN", "PET SCAN", "Coronary angiography".

### TRLOBXFL
- **Order:** 21
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.

### TRBLFL
- **Order:** 22
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that TRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### TREVAL
- **Order:** 23
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR".

### TREVALID
- **Order:** 24
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in TREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 6.

### TRACPTFL
- **Order:** 25
- **Label:** Accepted Record Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment.

### VISITNUM
- **Order:** 26
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 27
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 28
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 29
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### EPOCH
- **Order:** 30
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the element in the planned sequence of elements for the arm to which the subject was assigned.

### TRDTC
- **Order:** 31
- **Label:** Date/Time of Tumor/Lesion Measurement
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** The date of the scan/image/physical exam. TRDTC does not represent the date that the image was read to identify tumors/lesions. TRDTC also does not represent the VISIT date.

### TRDY
- **Order:** 32
- **Label:** Study Day of Tumor/Lesion Measurement
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
---

## Cross References

### Controlled Terminology
- [Tumor or Lesion Properties Test Result (C124309)](../../terminology/core/oncology_part2.md) — TRSTRESC
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — TRLOBXFL, TRBLFL, TRACPTFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — TRSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — TRORRESU, TRSTRESU
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — TREVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — TRMETHOD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — TREVALID
- [Tumor or Lesion Properties Test Name (C96778)](../../terminology/core/oncology_part2.md) — TRTEST
- [Tumor or Lesion Properties Test Code (C96779)](../../terminology/core/oncology_part2.md) — TRTESTCD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TU, UR, VS
- **Shared Dataset:** [TU](../TU/) — tumor results ← tumor identification
- **Related Findings:** [RS](../RS/) — tumor results → disease response

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)
