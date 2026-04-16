# RELSUB — Related Subjects

> Class: Relationship | Structure: One record per relationship per related subject per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### USUBJID
- **Order:** 2
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. Either USUBJID or POOLID must be populated.

### POOLID
- **Order:** 3
- **Label:** Pool Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to identify a pool of subjects. If POOLID is entered, POOLDEF records must exist for each subject in the pool and USUBJID must be null. Either USUBJID or POOLID must be populated.

### RSUBJID
- **Order:** 4
- **Label:** Related Subject or Pool Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to identify a related subject or pool of subjects. RSUBJID will be populated with either the USUBJID of the related subject or the POOLID of the related pool.

### SREL
- **Order:** 5
- **Label:** Subject Relationship
- **Type:** Char
- **Controlled Terms:** C100130
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Describes the relationship of the subject identified in USUBJID or the pool identified in POOLID to the subject or pool identified in RSUBJID.
---

## Cross References

### Controlled Terminology
- [Relationship to Subject (C100130)](../../terminology/core/other_part4.md) — SREL

### Related Domains
- **Same class (Relationship):** RELREC, RELSPEC, SUPPQUAL

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Relationship class definition](../../model/06_relationship_datasets.md)
