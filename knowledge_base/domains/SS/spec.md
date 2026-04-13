# SS — Subject Status

> Class: Findings | Structure: One record per status per visit per subject

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

### SSSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### SSGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### SSSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page.

### SSTESTCD
- **Order:** 7
- **Label:** Status Short Name
- **Type:** Char
- **Controlled Terms:** C124305
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the status assessment described in SSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SSTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "SURVSTAT".

### SSTEST
- **Order:** 8
- **Label:** Status Name
- **Type:** Char
- **Controlled Terms:** C124306
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the status assessment used to obtain the finding. The value in SSTEST cannot be longer than 40 characters. Example: "Survival Status".

### SSCAT
- **Order:** 9
- **Label:** Category for Assessment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize observations across subjects.

### SSSCAT
- **Order:** 10
- **Label:** Subcategory for Assessment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization.

### SSORRES
- **Order:** 11
- **Label:** Result or Finding Original Result
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the status assessment finding as originally received or collected.

### SSSTRESC
- **Order:** 12
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C124304
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from SSORRES, in a standard format.

### SSSTAT
- **Order:** 13
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a status assessment was not done. Should be null if a result exists in SSORRES.

### SSREASND
- **Order:** 14
- **Label:** Reason Assessment Not Performed
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why an assessment was not performed. Example: "Subject refused". Used in conjunction with SSSTAT when value is "NOT DONE".

### SSEVAL
- **Order:** 15
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "CAREGIVER", "ADJUDICATION COMMITTEE", "FRIEND".

### VISITNUM
- **Order:** 16
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 17
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 18
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 19
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 20
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the subject status assessment.

### SSDTC
- **Order:** 21
- **Label:** Date/Time of Assessment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of the subject status assessment represented in ISO 8601 character format.

### SSDY
- **Order:** 22
- **Label:** Study Day of Assessment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the subject status assessment, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
