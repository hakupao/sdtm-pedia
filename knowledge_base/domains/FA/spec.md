# FA — Findings About Events or Interventions

> Class: Findings About | Structure: One record per finding, per object, per time point, per visit per subject

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

### FASEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### FAGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### FASPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF.

### FATESTCD
- **Order:** 7
- **Label:** Findings About Test Short Name
- **Type:** Char
- **Controlled Terms:** C101832
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in FATEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in FATESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FATESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SEV", "OCCUR". Note that controlled terminology is in a FATESTCD general codelist and in several therapeutic area-specific codelists.

### FATEST
- **Order:** 8
- **Label:** Findings About Test Name
- **Type:** Char
- **Controlled Terms:** C101833
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in FATEST cannot be longer than 40 characters. Examples: "Severity/Intensity", "Occurrence". Note that controlled terminology is in a FATEST general codelist and in several therapeutic area-specific codelists.

### FAOBJ
- **Order:** 9
- **Label:** Object of the Observation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the term (e.g., "Acne") describing a clinical sign or symptom that is being measured by a severity test; an event (e.g., "VOMIT, where the volume of vomit is being measured by a VOLUME test).

### FACAT
- **Order:** 10
- **Label:** Category for Findings About
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records. Examples: "GERD", "PRE-SPECIFIED AE".

### FASCAT
- **Order:** 11
- **Label:** Subcategory for Findings About
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of FACAT.

### FAORRES
- **Order:** 12
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the test as originally received or collected.

### FAORRESU
- **Order:** 13
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for FAORRES.

### FASTRESC
- **Order:** 14
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from FAORRES in a standard format or standard units. FASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FASTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in FAORRES, and these results effectively have the same meaning; they could be represented in standard format in FASTRESC as "NEGATIVE".

### FASTRESN
- **Order:** 15
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from FASTRESC. FASTRESN should store all numeric test results or findings.

### FASTRESU
- **Order:** 16
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for FASTRESC and FASTRESN.

### FASTAT
- **Order:** 17
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that the measurement was not done. Should be null if a result exists in FAORRES.

### FAREASND
- **Order:** 18
- **Label:** Reason Not Performed
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a question was not answered. Example: "Subject refused". Used in conjunction with FASTAT when value is "NOT DONE".

### FALOC
- **Order:** 19
- **Label:** Location of the Finding About
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to specify the location of the clinical evaluation. Example: "ARM".

### FALAT
- **Order:** 20
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### FALOBXFL
- **Order:** 21
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### FABLFL
- **Order:** 22
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. The value should be "Y" or null. Note that FABLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### FAEVAL
- **Order:** 23
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR".

### VISITNUM
- **Order:** 24
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** 1. Clinical encounter number. \n 2. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 25
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** 1. Protocol-defined description of clinical encounter. \n 2. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 26
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 27
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 28
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP".

### FADTC
- **Order:** 29
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of findings assessment represented in ISO 8601 character format.

### FADY
- **Order:** 30
- **Label:** Study Day of Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** 1. Study day of collection, measured as integer days. \n 2. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.
