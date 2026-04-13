# NV — Nervous System Findings

> Class: Findings | Structure: One record per finding per location per time point per visit per subject

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

### FOCID
- **Order:** 4
- **Label:** Focus of Study-Specific Interest
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed, such as a drug application site (e.g., "Injection site 1", "Biopsy site 1", "Treated site 1") or a more specific focus (e.g., "OD" (right eye), "Upper left quadrant of the back"). The value in this variable should have inherent semantic meaning.

### NVSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### NVGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### NVREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external procedure identifier.

### NVSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page.

### NVLNKID
- **Order:** 9
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link a procedure to the assessment results over the course of the study.

### NVLNKGRP
- **Order:** 10
- **Label:** Link Group
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### NVTESTCD
- **Order:** 11
- **Label:** Short Name of Nervous System Test
- **Type:** Char
- **Controlled Terms:** C116104
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in NVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in NVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). NVTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SUVR", "N75LAT", "P100LAT","N145LAT".

### NVTEST
- **Order:** 12
- **Label:** Name of Nervous System Test
- **Type:** Char
- **Controlled Terms:** C116103
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in NVTEST cannot be longer than 40 characters. Examples: "Standard Uptake Value Ratio", "N75 Latency", "P100 Latency", "N145 Latency".

### NVCAT
- **Order:** 13
- **Label:** Category for Nervous System Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Example: "VISUAL EVOKED POTENTIAL".

### NVSCAT
- **Order:** 14
- **Label:** Subcategory for Nervous System Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of NVCAT values.

### NVORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the procedure measurement or finding as originally received or collected.

### NVORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for NVORRES.

### NVSTRESC
- **Order:** 17
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from NVORRES, in a standard format or standard units. NVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in NVSTRESN.

### NVSTRESN
- **Order:** 18
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from NVSTRESC. NVSTRESN should store all numeric test results or findings.

### NVSTRESU
- **Order:** 19
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for NVSTRESC or NVSTRESN.

### NVSTAT
- **Order:** 20
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a test was not done, or a measurement was not taken. Should be null if a result exists in NVORRES.

### NVREASND
- **Order:** 21
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with NVSTAT when value is "NOT DONE".

### NVLOC
- **Order:** 22
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement. Examples: "BRAIN", "EYE", "PRECUNEUS", "CINGULATE CORTEX".

### NVLAT
- **Order:** 23
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### NVDIR
- **Order:** 24
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### NVMETHOD
- **Order:** 25
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "EEG", "PET/CT SCAN ", "FDGPET".

### NVLOBXFL
- **Order:** 26
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### NVBLFL
- **Order:** 27
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that NVBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### NVDRVFL
- **Order:** 28
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### NVEVAL
- **Order:** 29
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".

### NVEVALID
- **Order:** 30
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in NVEVAL. Examples: "RADIOLOGIST 1", "RADIOLOGIST 2".

### VISITNUM
- **Order:** 31
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 32
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 33
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 34
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 35
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### NVDTC
- **Order:** 36
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date of procedure or test.

### NVDY
- **Order:** 37
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the procedure or test, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### NVTPT
- **Order:** 38
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See NVTPTNUM and NVTPTREF. Examples: "START", "5 MIN POST".

### NVTPTNUM
- **Order:** 39
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of NVTPT to aid in sorting.

### NVELTM
- **Order:** 40
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a fixed time point reference (NVTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by NVTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by NVTPTREF.

### NVTPTREF
- **Order:** 41
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by NVELTM, NVTPTNUM, and NVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### NVRFTDTC
- **Order:** 42
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by --TPTREF in ISO 8601 character format.
