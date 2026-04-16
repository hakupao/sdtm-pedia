# SV — Subject Visits

> Class: Special-Purpose | Structure: One record per actual or planned visit per subject

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
- **CDISC Notes:** Two-character abbreviation for the domain most relevant to the observation. The domain abbreviation is also used as a prefix for variables to ensure uniqueness when datasets are merged.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### VISITNUM
- **Order:** 4
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 5
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### SVPRESP
- **Order:** 6
- **Label:** Pre-specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to indicate whether the visit was planned (i.e., visits specified in the TV domain). Value is "Y" for planned visits, null for unplanned visits.

### SVOCCUR
- **Order:** 7
- **Label:** Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to record whether a planned visit occurred. The value is null for unplanned visits.

### SVREASOC
- **Order:** 8
- **Label:** Reason for Occur Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The reason for the value in SVOCCUR. If SVOCCUR="N", SVREASOC is the reason the visit did not occur.

### SVCNTMOD
- **Order:** 9
- **Label:** Contact Mode
- **Type:** Char
- **Controlled Terms:** C171445
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The way in which the visit was conducted. Examples: "IN PERSON", "TELEPHONE CALL", "IVRS".

### SVEPCHGI
- **Order:** 10
- **Label:** Epi/Pandemic Related Change Indicator
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates whether the visit was changed due to an epidemic or pandemic.

### VISITDY
- **Order:** 11
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### SVSTDTC
- **Order:** 12
- **Label:** Start Date/Time of Observation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of an observation represented in IS0 8601 character format.

### SVENDTC
- **Order:** 13
- **Label:** End Date/Time of Observation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time of the observation represented in IS0 8601 character format.

### SVSTDY
- **Order:** 14
- **Label:** Study Day of Start of Observation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### SVENDY
- **Order:** 15
- **Label:** Study Day of End of Observation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### SVUPDES
- **Order:** 16
- **Label:** Description of Unplanned Visit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of what happened to the subject during an unplanned visit. Only populated for unplanned visits.
---

## Cross References

### Controlled Terminology
- [Mode of Subject Contact (C171445)](../../terminology/core/special_purpose.md) — SVCNTMOD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — SVPRESP, SVOCCUR, SVEPCHGI

### Related Domains
- **Same class (Special-Purpose):** CO, DM, SE, SM

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)
