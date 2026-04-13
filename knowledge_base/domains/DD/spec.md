# DD — Death Details

> Class: Findings | Structure: One record per finding per subject

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

### DDSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### DDTESTCD
- **Order:** 5
- **Label:** Death Detail Assessment Short Name
- **Type:** Char
- **Controlled Terms:** C116108
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in DDTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in DDTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). DDTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRCDTH", "SECDTH".

### DDTEST
- **Order:** 6
- **Label:** Death Detail Assessment Name
- **Type:** Char
- **Controlled Terms:** C116107
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for DDTESTCD. The value in DDTEST cannot be longer than 40 characters. Examples: "Primary Cause of Death", "Secondary Cause of Death".

### DDORRES
- **Order:** 7
- **Label:** Result or Finding as Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the test defined in DDTEST, as originally received or collected.

### DDSTRESC
- **Order:** 8
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result or finding copied or derived from DDORRES in a standard format.

### DDRESCAT
- **Order:** 9
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding. Examples: "TREATMENT RELATED", "NONTREATMENT RELATED", "UNDETERMINED", "ACCIDENTAL".

### DDEVAL
- **Order:** 10
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation.

### DDDTC
- **Order:** 11
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of collection of the diagnosis or other death assessment data in ISO 8601 format. This is not necessarily the date of death.

### DDDY
- **Order:** 12
- **Label:** Study Day of Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.
