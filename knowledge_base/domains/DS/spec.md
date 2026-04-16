# DS — Disposition

> Class: Events | Structure: One record per disposition status or protocol milestone per subject

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

### DSSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### DSGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### DSREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier.

### DSSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Disposition page.

### DSTERM
- **Order:** 8
- **Label:** Reported Term for the Disposition Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim name of the event or protocol milestone. Some terms in DSTERM will match DSDECOD, but others, such as "Subject moved", will map to controlled terminology in DSDECOD, such as "LOST TO FOLLOW-UP".

### DSDECOD
- **Order:** 9
- **Label:** Standardized Disposition Term
- **Type:** Char
- **Controlled Terms:** C66727; C114118; C150811
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Controlled terminology for the name of disposition event or protocol milestone. Examples of protocol milestones: "INFORMED CONSENT OBTAINED", "RANDOMIZED". There are separate codelists used for DSDECOD where the choice depends on the value of DSCAT. Codelist "NCOMPLT" is used for disposition events, codelist "PROTMLST" is used for protocol milestones, and codelist "OTHEVENT" is used for other events.

### DSCAT
- **Order:** 10
- **Label:** Category for Disposition Event
- **Type:** Char
- **Controlled Terms:** C74558
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of related records.

### DSSCAT
- **Order:** 11
- **Label:** Subcategory for Disposition Event
- **Type:** Char
- **Controlled Terms:** C170443
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of DSCAT (e.g., "STUDY PARTICIPATION", "STUDY TREATMENT" when DSCAT = "DISPOSITION EVENT"). The variable may be subject to controlled terminology for other categories of disposition event records.

### EPOCH
- **Order:** 12
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the event.

### DSDTC
- **Order:** 13
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of the disposition observation represented in ISO 8601 character format.

### DSSTDTC
- **Order:** 14
- **Label:** Start Date/Time of Disposition Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of the disposition event in ISO 8601 character format.

### DSDY
- **Order:** 15
- **Label:** Study Day of Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of collection of event relative to the sponsor-defined RFSTDTC.

### DSSTDY
- **Order:** 16
- **Label:** Study Day of Start of Disposition Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Study day of start of event relative to the sponsor-defined RFSTDTC.
---

## Cross References

### Controlled Terminology
- [Protocol Milestone (C114118)](../../terminology/core/disposition.md) — DSDECOD
- [Other Disposition Event Response (C150811)](../../terminology/core/disposition.md) — DSDECOD
- [Subcategory for Disposition Event (C170443)](../../terminology/core/disposition.md) — DSSCAT
- [Completion/Reason for Non-Completion (C66727)](../../terminology/core/disposition.md) — DSDECOD
- [Category of Disposition Event (C74558)](../../terminology/core/disposition.md) — DSCAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Events):** AE, BE, CE, DV, HO, MH
- **Demographics:** [DM](../DM/) — disposition dates relate to DM reference dates

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Events class definition](../../model/02_observation_classes.md)
