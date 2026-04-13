# RELREC — Related Records

> Class: Relationship | Structure: One record per related record, group of records or dataset

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### RDOMAIN
- **Order:** 2
- **Label:** Related Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** C66734
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Abbreviation for the domain of the parent record(s).

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### IDVAR
- **Order:** 4
- **Label:** Identifying Variable
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Name of the identifying variable in the general-observation-class dataset that identifies the related record(s). Examples: --SEQ, --GRPID.

### IDVARVAL
- **Order:** 5
- **Label:** Identifying Variable Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Value of identifying variable described in IDVAR. If --SEQ is the variable being used to describe this record, then the value of --SEQ would be entered here.

### RELTYPE
- **Order:** 6
- **Label:** Relationship Type
- **Type:** Char
- **Controlled Terms:** C78737
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Identifies the hierarchical level of the records in the relationship. Values should be either "ONE" or "MANY". Used only when identifying a relationship between datasets (as described in Section 8.3, Relating Datasets).

### RELID
- **Order:** 7
- **Label:** Relationship Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Unique value within USUBJID that identifies the relationship. All records for the same USUBJID that have the same RELID are considered related/associated. RELID can be any value the sponsor chooses, and is only meaningful within the RELREC dataset to identify the related/associated domain records.
