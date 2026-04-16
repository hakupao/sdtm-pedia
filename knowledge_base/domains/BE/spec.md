# BE — Biospecimen Events

> Class: Events | Structure: One record per instance per biospecimen event per biospecimen identifier per subject

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

### BESEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### BEGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### BEREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Internal or external identifier for the specimen affected or created by the event.

### BESPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional sponsor-defined reference number. Example: Line number on a CRF page.

### BETERM
- **Order:** 9
- **Label:** Reported Term for the Biospecimen Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Topic variable for an event observation, which is the verbatim or pre-specified name of the event.

### BEMODIFY
- **Order:** 10
- **Label:** Modified Reported Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** If the value for BETERM is modified for coding purposes, then the modified text is placed here.

### BEDECOD
- **Order:** 11
- **Label:** Dictionary-Derived Term
- **Type:** Char
- **Controlled Terms:** C124297
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Dictionary-derived text description of BETERM or BEMODIFY, if applicable.

### BECAT
- **Order:** 12
- **Label:** Category for Biospecimen Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Example: COLLECTION, PREPARATION, TRANSPORT.

### BESCAT
- **Order:** 13
- **Label:** Subcategory for Biospecimen Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of BECAT values.

### BELOC
- **Order:** 14
- **Label:** Anatomical Location of Event
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the anatomical location relevant for the event (e.g. BRAIN, LUNG).

### BEPARTY
- **Order:** 15
- **Label:** Accountable Party
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Party accountable for the transferable object (e.g. specimen) as a result of the activity performed in the associated BETERM variable. The party could be an individual (e.g., subject), an organization (e.g., sponsor), or a location that is a proxy for an individual or organization (e.g., site). It is usually a somewhat general term that is further identified in the BEPRTYID variable.

### BEPRTYID
- **Order:** 16
- **Label:** Identification of Accountable Party
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identification of the specific party accountable for the transferable object (e.g. Specimen) after the action in BETERM is taken. Used in conjunction with BEPARTY.

### VISITNUM
- **Order:** 17
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 18
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter.

### VISITDY
- **Order:** 19
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### BEDTC
- **Order:** 20
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of specimen collection.

### BESTDTC
- **Order:** 21
- **Label:** Start Date/Time of Biospecimen Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of the event.

### BEENDTC
- **Order:** 22
- **Label:** End Date/Time of Biospecimen Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time of the event.

### BESTDY
- **Order:** 23
- **Label:** Study Day of Start of Biospecimen Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### BEENDY
- **Order:** 24
- **Label:** Study Day of End of Biospecimen Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### BEDUR
- **Order:** 25
- **Label:** Duration of Biospecimen Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration and unit of a biospecimen event. Used only if collected on the CRF and not derived from start and end date/times. Example: P1DT2H (for 1 day, 2 hours).
---

## Cross References

### Controlled Terminology
- [Biospecimen Events Dictionary Derived Term (C124297)](../../terminology/core/other_part1.md) — BEDECOD
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — BELOC

### Related Domains
- **Same class (Events):** AE, CE, DS, DV, HO, MH
- **Specimen:** [BS](../BS/) — biospecimen data for the event

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Events class definition](../../model/02_observation_classes.md)
