# TS — Trial Summary

> Class: Trial Design | Structure: One record per trial summary parameter value

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

### TSSEQ
- **Order:** 3
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a parameter. Allows inclusion of multiple records for the same TSPARMCD.

### TSGRPID
- **Order:** 4
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a group of related records.

### TSPARMCD
- **Order:** 5
- **Label:** Trial Summary Parameter Short Name
- **Type:** Char
- **Controlled Terms:** C66738
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** TSPARMCD (the companion to TSPARM) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that TSPARMCD will need to serve as variable names. Examples: "AGEMIN", "AGEMAX".

### TSPARM
- **Order:** 6
- **Label:** Trial Summary Parameter
- **Type:** Char
- **Controlled Terms:** C67152
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Term for the trial summary parameter. The value in TSPARM cannot be longer than 40 characters. Examples: "Planned Minimum Age of Subjects", "Planned Maximum Age of Subjects".

### TSVAL
- **Order:** 7
- **Label:** Parameter Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Value of TSPARM. Example: "ASTHMA" when TSPARM value is "Trial Indication". TSVAL can only be null when TSVALNF is populated. Text over 200 characters can be added to additional columns TSVAL1-TSVALn. See Assumption 8.

### TSVALNF
- **Order:** 8
- **Label:** Parameter Value Null Flavor
- **Type:** Char
- **Controlled Terms:** ISO 21090 NullFlavor
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Null flavor for the value of TSPARM, to be populated only if TSVAL is null.

### TSVALCD
- **Order:** 9
- **Label:** Parameter Value Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** This is the code of the term in TSVAL. For example, "6CW7F3G59X" is the code for gabapentin; "C49488" is the code for Y. The length of this variable can be longer than 8 to accommodate the length of the external terminology.

### TSVCDREF
- **Order:** 10
- **Label:** Name of the Reference Terminology
- **Type:** Char
- **Controlled Terms:** C66788
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** The name of the reference terminology from which TSVALCD is taken. For example; CDISC CT, SNOMED, ISO 8601.

### TSVCDVER
- **Order:** 11
- **Label:** Version of the Reference Terminology
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** The version number of the reference terminology, if applicable.
---

## Cross References

### Controlled Terminology
- [Trial Summary Parameter Test Code (C66738)](../../terminology/core/trial_design.md) — TSPARMCD
- [Dictionary Name (C66788)](../../terminology/core/trial_design.md) — TSVCDREF
- [Trial Summary Parameter Test Name (C67152)](../../terminology/core/trial_design.md) — TSPARM

### Related Domains
- **Same class (Trial Design):** TA, TD, TE, TI, TM, TV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)
