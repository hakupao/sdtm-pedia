# CO — Comments

> Class: Special-Purpose | Structure: One record per comment per subject

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

### RDOMAIN
- **Order:** 3
- **Label:** Related Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** C66734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Two-character abbreviation for the domain of the parent record(s). Null for comments collected on a general comments or additional information CRF page.

### USUBJID
- **Order:** 4
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### COSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence Number given to ensure uniqueness of subject records within a domain. May be any valid number.

### IDVAR
- **Order:** 6
- **Label:** Identifying Variable
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifying variable in the parent dataset that identifies the record(s) to which the comment applies. Examples AESEQ or CMGRPID. Used only when individual comments are related to domain records. Null for comments collected on separate CRFs.

### IDVARVAL
- **Order:** 7
- **Label:** Identifying Variable Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Value of identifying variable of the parent record(s). Used only when individual comments are related to domain records. Null for comments collected on separate CRFs.

### COREF
- **Order:** 8
- **Label:** Comment Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference associated with the comment. May be the CRF page number (e.g., 650), or a module name (e.g., DEMOG), or a combination of information that identifies the reference (e.g. 650-VITALS-VISIT 2).

### COVAL
- **Order:** 9
- **Label:** Comment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** The text of the comment. Text over 200 characters can be added to additional columns COVAL1-COVALn. See Assumption 3.

### COEVAL
- **Order:** 10
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Example: "INVESTIGATOR".

### COEVALID
- **Order:** 11
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST", "RADIOLOGIST 1", "RADIOLOGIST 2".

### CODTC
- **Order:** 12
- **Label:** Date/Time of Comment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of comment on dedicated comment form. Should be null if this is a child record of another domain or if comment date was not collected.

### CODY
- **Order:** 13
- **Label:** Study Day of Comment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the comment, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.
