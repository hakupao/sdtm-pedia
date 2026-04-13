# CV — Cardiovascular System Findings

> Class: Findings | Structure: One record per finding or result per time point per visit per subject

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

### CVSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### CVGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### CVREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier.

### CVSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. Example: a preprinted line identifier on a CRF.

### CVLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### CVLNKGRP
- **Order:** 9
- **Label:** Link Group
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### CVTESTCD
- **Order:** 10
- **Label:** Short Name of Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** C101847
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in CVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" would not be valid). CVTESTCD cannot contain characters other than letters, numbers, or underscores.

### CVTEST
- **Order:** 11
- **Label:** Name of Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** C101846
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name For CVTESTCD. The value in CVTEST cannot be longer than 40 characters.

### CVCAT
- **Order:** 12
- **Label:** Category for Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values.

### CVSCAT
- **Order:** 13
- **Label:** Subcategory for Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of CVCAT values.

### CVPOS
- **Order:** 14
- **Label:** Position of Subject During Observation
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".

### CVORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### CVORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. Unit for CVORRES.

### CVSTRESC
- **Order:** 17
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived, from CVORRES in a standard format or in standard units. CVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CVSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in CVORRES and these results effectively have the same meaning, they could be represented in standard format in CVSTRESC as "NEGATIVE".

### CVSTRESN
- **Order:** 18
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from CVSTRESC. CVSTRESN should store all numeric test results or findings.

### CVSTRESU
- **Order:** 19
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for CVSTRESC and CVSTRESN.

### CVSTAT
- **Order:** 20
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### CVREASND
- **Order:** 21
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed (e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED"). Used in conjunction with CVSTAT when value is "NOT DONE".

### CVLOC
- **Order:** 22
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement. Examples: "HEART", "LEFT VENTRICLE".

### CVLAT
- **Order:** 23
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL", "UNILATERAL".

### CVDIR
- **Order:** 24
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### CVMETHOD
- **Order:** 25
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method used to create the result.

### CVLOBXFL
- **Order:** 26
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### CVBLFL
- **Order:** 27
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that CVBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### CVDRVFL
- **Order:** 28
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (i.e., a record that represents the average of other records, such as a computed baseline). Should be "Y" or null.

### CVEVAL
- **Order:** 29
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", " INDEPENDENT ASSESSOR", "RADIOLOGIST".

### CVEVALID
- **Order:** 30
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in CVEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2".

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
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

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

### CVDTC
- **Order:** 36
- **Label:** Date/Time of Test
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation.

### CVDY
- **Order:** 37
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### CVTPT
- **Order:** 38
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See CVTPTNUM and CVTPTREF.

### CVTPTNUM
- **Order:** 39
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### CVELTM
- **Order:** 40
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to a planned fixed reference (CVTPTREF). Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### CVTPTREF
- **Order:** 41
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by CVELTM, CVTPTNUM, and CVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### CVRFTDTC
- **Order:** 42
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by CVTPTREF.
