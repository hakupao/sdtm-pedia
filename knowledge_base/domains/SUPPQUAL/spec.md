# SUPPQUAL — Supplemental Qualifiers for [domain name]

> Class: Relationship | Structure: One record per supplemental qualifier per related parent domain record(s)

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Study identifier of the parent record(s).

### RDOMAIN
- **Order:** 2
- **Label:** Related Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** C66734
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain of the parent record(s).

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. This is the value of USUBJID in the parent record(s).

### IDVAR
- **Order:** 4
- **Label:** Identifying Variable
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifying variable in the dataset that identifies the related record(s). Examples: --SEQ, --GRPID.

### IDVARVAL
- **Order:** 5
- **Label:** Identifying Variable Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Value of identifying variable of the parent record(s).

### QNAM
- **Order:** 6
- **Label:** Qualifier Variable Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** The short name of the qualifier variable, which is used as a column name in a domain view with data from the parent domain. The value in QNAM cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). QNAM cannot contain characters other than letters, numbers, or underscores. This will often be the column name in the sponsor's operational dataset.

### QLABEL
- **Order:** 7
- **Label:** Qualifier Variable Label
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** This is the long name or label associated with QNAM. The value in QLABEL cannot be longer than 40 characters. This will often be the column label in the sponsor's original dataset.

### QVAL
- **Order:** 8
- **Label:** Data Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Req
- **CDISC Notes:** Result of, response to, or value associated with QNAM. A value for this column is required; no records can be in SUPP-- with a null value for QVAL.

### QORIG
- **Order:** 9
- **Label:** Origin
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Because QVAL can represent a mixture of collected (on a CRF), derived, or assigned items, QORIG is used to indicate the origin of this data. Examples: "CRF", "Assigned", "Derived". See Section 4.1.8, Origin Metadata.

### QEVAL
- **Order:** 10
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain objectively collected or derived data. Examples: "ADJUDICATION COMMITTEE", "STATISTICIAN", "DATABASE ADMINISTRATOR", "CLINICAL COORDINATOR".
