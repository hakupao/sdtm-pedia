# SM — Subject Disease Milestones

> Class: Special-Purpose | Structure: One record per Disease Milestone per subject

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

### SMSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of subject records. Should be assigned to be consistent chronological order.

### MIDS
- **Order:** 5
- **Label:** Disease Milestone Instance Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Name of the specific disease milestone. For types of disease milestones that can occur multiple times, the name will end with a sequence number. Example: "HYPO1".

### MIDSTYPE
- **Order:** 6
- **Label:** Disease Milestone Type
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** The type of disease milestone. Example: "HYPOGLYCEMIC EVENT".

### SMSTDTC
- **Order:** 7
- **Label:** Start Date/Time of Milestone
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of milestone instance (if milestone is an intervention or event) or date of milestone (if Milestone is a finding).

### SMENDTC
- **Order:** 8
- **Label:** End Date/Time of Milestone
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time of disease milestone instance.

### SMSTDY
- **Order:** 9
- **Label:** Study Day of Start of Milestone
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Study day of start of disease milestone instance, relative to the sponsor-defined RFSTDTC.

### SMENDY
- **Order:** 10
- **Label:** Study Day of End of Milestone
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Study day of end of disease milestone instance, relative to the sponsor-defined RFSTDTC.
---

## Cross References

### Related Domains
- **Same class (Special-Purpose):** CO, DM, SE, SV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)
