# BS — Biospecimen Findings

> Class: Findings | Structure: One record per measurement per biospecimen identifier per subject

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

### BSSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### BSGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### BSREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Internal or external identifier such as lab specimen ID.

### BSSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### BSTESTCD
- **Order:** 9
- **Label:** Biospecimen Test Short Name
- **Type:** Char
- **Controlled Terms:** C124300
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for BSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: VOLUME, RIN.

### BSTEST
- **Order:** 10
- **Label:** Biospecimen Test Name
- **Type:** Char
- **Controlled Terms:** C124299
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for BSTESTCD. Examples: Volume, RNA Integrity Number.

### BSCAT
- **Order:** 11
- **Label:** Category for Biospecimen Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of topic-variable values. Example: MEASUREMENT, QUALITY.

### BSSCAT
- **Order:** 12
- **Label:** Subcategory for Biospecimen Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of BSCAT values.

### BSORRES
- **Order:** 13
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### BSORRESU
- **Order:** 14
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Unit for BSORRES. Examples: mg, mL.

### BSSTRESC
- **Order:** 15
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from BSORRES in a standard format or standard units. BSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in BSSTRESN.

### BSSTRESN
- **Order:** 16
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from BSSTRESC. BSSTRESN should store all numeric test results or findings.

### BSSTRESU
- **Order:** 17
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for BSSTRESC and BSSTRESN.

### BSSTAT
- **Order:** 18
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a test was not done, or was attempted but did not generate a result. Should be null or have a value of NOT DONE.

### BSREASND
- **Order:** 19
- **Label:** Reason Test Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with BSSTAT when value is NOT DONE.

### BSNAM
- **Order:** 20
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor (e.g., laboratory) that provided the test results.

### BSSPEC
- **Order:** 21
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734; C111114
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: SERUM, PLASMA, URINE, SOFT TISSUE.

### BSANTREG
- **Order:** 22
- **Label:** Anatomical Region of Specimen
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the specific anatomical or biological region of a tissue, organ specimen or the region from which the specimen is obtained, as defined in the protocol, such as a section or part of what is described in the BSSPEC variable. Examples: CORTEX, MEDULLA, MUCOSA.

### BSSPCCND
- **Order:** 23
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the condition of the specimen. Examples: HEMOLYZED, ICTERIC, LIPEMIC.

### BSMETHOD
- **Order:** 24
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: SPECTROPHOTOMETRY, ELECTROPHORESIS.

### BSBLFL
- **Order:** 25
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value.

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
- **CDISC Notes:** Protocol-defined description of clinical encounter.

### VISITDY
- **Order:** 28
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### BSDTC
- **Order:** 29
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of specimen collection.

### BSDY
- **Order:** 30
- **Label:** Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection relative to the sponsor-defined RFSTDTC.

### BSTPT
- **Order:** 31
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See BSTPTNUM and BSTPTREF.

### BSTPTNUM
- **Order:** 32
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of BSTPT used in sorting.

### BSELTM
- **Order:** 33
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Elapsed time relative to a planned fixed reference (BSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration.

### BSTPTREF
- **Order:** 34
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by BSELTM, BSTPTNUM, and BSTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL.

### BSRFTDTC
- **Order:** 35
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by BSTPTREF.
---

## Cross References

### Controlled Terminology
- [Genetic Sample Type (C111114)](../../terminology/core/general_part2.md) — BSSPEC
- [Biospecimen Characteristics Test Name (C124299)](../../terminology/core/other_part1.md) — BSTEST
- [Biospecimen Characteristics Test Code (C124300)](../../terminology/core/other_part1.md) — BSTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — BSBLFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — BSSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — BSORRESU, BSSTRESU
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — BSSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — BSSPEC
- [Method (C85492)](../../terminology/core/general_part3.md) — BSMETHOD

### Related Domains
- **Same class (Findings):** CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Event:** [BE](../BE/) — biospecimen events
- **Specimen Relationship:** [RELSPEC](../RELSPEC/) — specimen hierarchy

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)
