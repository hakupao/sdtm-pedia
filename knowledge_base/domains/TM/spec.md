# TM — Trial Disease Milestones

> Class: Trial Design | Structure: One record per Disease Milestone type

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
- **CDISC Notes:** Two-character abbreviation for the domain, which must be TM.

### MIDSTYPE
- **Order:** 3
- **Label:** Disease Milestone Type
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** The type of disease milestone. Example: "HYPOGLYCEMIC EVENT".

### TMDEF
- **Order:** 4
- **Label:** Disease Milestone Definition
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Req
- **CDISC Notes:** Definition of the disease milestone.

### TMRPT
- **Order:** 5
- **Label:** Disease Milestone Repetition Indicator
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Indicates whether this is a disease milestone that can occur only once ("N") or a type of disease milestone that can occur multiple times ("Y").
---

## Cross References

### Controlled Terminology
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — TMRPT

### Related Domains
- **Same class (Trial Design):** TA, TD, TE, TI, TS, TV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)
