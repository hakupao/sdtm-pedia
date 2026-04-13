# DA — Product Accountability

> Class: Findings | Structure: One record per product accountability finding per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study within the submission.

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

### DASEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### DAGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### DAREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier such as a code from the product packaging (e.g., bottle label, package label, kit label).

### DASPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Examples: Line number on the Product Accountability CRF page, a code from the product packaging (e.g., bottle label, package label, kit label).

### DALNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### DALNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### DATESTCD
- **Order:** 10
- **Label:** Short Name of Accountability Assessment
- **Type:** Char
- **Controlled Terms:** C78732
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for DATEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters and cannot begin with a number or contain characters other than letters, numbers, or underscores. Examples: "DISPAMT", "RETAMT".

### DATEST
- **Order:** 11
- **Label:** Name of Accountability Assessment
- **Type:** Char
- **Controlled Terms:** C78731
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name corresponding to the topic variable of the test or examination used to obtain the product accountability assessment. The value in DATEST cannot be longer than 40 characters. Examples: "Dispensed Amount", "Returned Amount".

### DACAT
- **Order:** 12
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Examples: "STUDY MEDICATION", "RESCUE MEDICATION".

### DASCAT
- **Order:** 13
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization level for a group of related records.

### DAORRES
- **Order:** 14
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the product accountability assessment as originally received or collected.

### DAORRESU
- **Order:** 15
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for DAORRES.

### DASTRESC
- **Order:** 16
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all product accountability assessments copied or derived from DAORRES, in a standard format or in standard units. DASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in DASTRESN.

### DASTRESN
- **Order:** 17
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from DASTRESC. DASTRESN should store all numeric test results or findings.

### DASTRESU
- **Order:** 18
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for DASTRESC and DASTRESN.

### DASTAT
- **Order:** 19
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a product accountability assessment was not done. Should be null or have a value of "NOT DONE".

### DAREASND
- **Order:** 20
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with DASTAT when value is "NOT DONE".

### VISITNUM
- **Order:** 21
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 22
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 23
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit, based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 24
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm (see Section 7.2.1, Trial Arms).

### EPOCH
- **Order:** 25
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### DADTC
- **Order:** 26
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of the product accountability assessment represented in ISO 8601 character format.

### DADY
- **Order:** 27
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of product accountability assessment, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC in Demographics.
