# MB — Microbiology Specimen

> Class: Findings | Structure: One record per microbiology specimen finding per time point per visit per subject

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

### FOCID
- **Order:** 4
- **Label:** Focus of Study-Specific Interest
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed. The value in this variable should have inherent semantic meaning.

### MBSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number.

### MBGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### MBREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier (e.g., sample ID for a subject sample from which a microbial culture was generated).

### MBSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.

### MBLNKID
- **Order:** 9
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. For example, it may be used to link genetic findings (in the PF domain) about a microbe to the original culture of that microbe (in MB), or to susceptibility records (in MS) if needed.

### MBLNKGRP
- **Order:** 10
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### MBTESTCD
- **Order:** 11
- **Label:** Microbiology Test or Finding Short Name
- **Type:** Char
- **Controlled Terms:** C120527
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or finding described in MBTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MBTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MBTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MCORGIDN" for Microbial Organism Identification "GMNCOC" for Gram Negative Cocci.

### MBTEST
- **Order:** 12
- **Label:** Microbiology Test or Finding Name
- **Type:** Char
- **Controlled Terms:** C120528
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in MBTEST cannot be longer than 40 characters. Examples: "Microbial Organism Identification", "Gram Negative Cocci", "HIV-1 RNA".

### MBTSTDTL
- **Order:** 13
- **Label:** Measurement, Test or Examination Detail
- **Type:** Char
- **Controlled Terms:** C174225
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of MBTESTCD and MBTEST. Example: "VIRAL LOAD" when MBTESTCD represents viral genetic material, such as "HCRNA", "QUANTIFICATION" when MBTESTCD represents any organism being quantified.

### MBCAT
- **Order:** 14
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records.

### MBSCAT
- **Order:** 15
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of MBCAT values.

### MBORRES
- **Order:** 16
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the microbiology measurement or finding as originally received or collected. Examples for "GRAM STAIN" findings: "+3 MODERATE", "+2 FEW", "<10". Examples for "CULTURE PLATE" findings: "KLEBSIELLA PNEUMONIAE", "STREPTOCOCCUS PNEUMONIAE".

### MBORRESU
- **Order:** 17
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original unit for MBORRES. Example: "mcg/mL".

### MBSTRESC
- **Order:** 18
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from MBORRES, in a standard format or standard units. MBSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MBSTRESN. For example, if a test has results "+3 MODERATE", "MOD", and "MODERATE" in MBORRES and these results effectively have the same meaning, they could be represented in standard format in MBSTRESC as "MODERATE".

### MBSTRESN
- **Order:** 19
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from MBSTRESC. MBSTRESN should store all numeric test results or findings.

### MBSTRESU
- **Order:** 20
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for MBSTRESC and MBSTRESN.

### MBRESCAT
- **Order:** 21
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding in a standard format.

### MBSTAT
- **Order:** 22
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or that a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### MBREASND
- **Order:** 23
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with MBSTAT when value is NOT DONE. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED".

### MBNAM
- **Order:** 24
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor (e.g., laboratory) that provided the test results.

### MBLOINC
- **Order:** 25
- **Label:** LOINC Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Logical Observation Identifiers Names and Codes (LOINC) code for the topic variable (e.g., lab test).

### MBSPEC
- **Order:** 26
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "SPUTUM", "BLOOD", "PUS".

### MBSPCCND
- **Order:** 27
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Free or standardized text describing the condition of the specimen. Example: "CONTAMINATED".

### MBLOC
- **Order:** 28
- **Label:** Specimen Collection Location
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location relevant to the collection of the measurement.

### MBLAT
- **Order:** 29
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for specimen collection location further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### MBDIR
- **Order:** 30
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for specimen collection location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### MBMETHOD
- **Order:** 31
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Method of the test or examination. Examples: "GRAM STAIN", "MICROBIAL CULTURE, LIQUID", "QUANTITATIVE REVERSE TRANSCRIPTASE POLYMERASE CHAIN REACTION".

### MBLOBXFL
- **Order:** 32
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### MBBLFL
- **Order:** 33
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that MBBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### MBFAST
- **Order:** 34
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status. Valid values include "Y", "N", "U", or null if not relevant.

### MBDRVFL
- **Order:** 35
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### VISITNUM
- **Order:** 36
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 37
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 38
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 39
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element which the specimen collection occurred.

### EPOCH
- **Order:** 40
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the specimen was collected.

### MBDTC
- **Order:** 41
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection.

### MBDY
- **Order:** 42
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.

### MBTPT
- **Order:** 43
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See MBTPTNUM and MBTPTREF. Examples: "Start", "5 min post".

### MBTPTNUM
- **Order:** 44
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of MBTPT used in sorting.

### MBELTM
- **Order:** 45
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (MBTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by MBTPTREF, or "PT8H" to represent the period of 8 hours after the reference point indicated by MBTPTREF.

### MBTPTREF
- **Order:** 46
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by MBELTM, MBTPTNUM, and MBTPT. Example: "PREVIOUS DOSE".

### MBRFTDTC
- **Order:** 47
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point, MBTPTREF.
---

## Cross References

### Controlled Terminology
- [Microbiology Test Code (C120527)](../../terminology/core/microbiology_part2.md) — MBTESTCD
- [Microbiology Test Name (C120528)](../../terminology/core/microbiology_part3.md) — MBTEST
- [Microbiology Findings Test Details (C174225)](../../terminology/core/microbiology_part1.md) — MBTSTDTL
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — MBLOBXFL, MBBLFL, MBFAST, MBDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — MBSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — MBORRESU, MBSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — MBLOC
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — MBSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — MBSPEC
- [Method (C85492)](../../terminology/core/general_part3.md) — MBMETHOD
- [Laterality (C99073)](../../terminology/core/general_part2.md) — MBLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — MBDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Shared Dataset:** [MS](../MS/) — microbiology susceptibility results
- **Related Findings:** [MI](../MI/) — microbiology microscopic findings
- **Specimen:** [BS](../BS/) — microbiology specimen data
- **Specimen Relationship:** [RELSPEC](../RELSPEC/) — specimen hierarchy

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)
