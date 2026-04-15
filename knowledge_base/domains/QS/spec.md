# QS — Questionnaires

> Class: Findings | Structure: One record per questionnaire per question per time point per visit per subject

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

### QSSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### QSGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### QSSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Question number on a questionnaire.

### QSTESTCD
- **Order:** 7
- **Label:** Question Short Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Topic variable for QS. Short name for the value in QSTEST, which can be used as a column name when converting the dataset from a vertical format to a horizontal format. The value in QSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). QSTESTCD cannot contain characters other than letters, numbers, or underscores.  Controlled terminology for QSTESTCD is published in separate codelists for each questionnaire. See https://www.cdisc.org/standards/semantics/terminology for values for QSTESTCD. Examples: "ADCCMD01", "BPR0103".

### QSTEST
- **Order:** 8
- **Label:** Question Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the question or group of questions used to obtain the measurement or finding. The value in QSTEST cannot be longer than 40 characters.  Controlled terminology for QSTEST is published in separate codelists for each questionnaire. See https://www.cdisc.org/standards/semantics/terminology for values for QSTEST. Example: "BPR01 - Emotional Withdrawal".

### QSCAT
- **Order:** 9
- **Label:** Category of Question
- **Type:** Char
- **Controlled Terms:** C100129
- **Role:** Grouping Qualifier
- **Core:** Req
- **CDISC Notes:** Used to specify the questionnaire in which the question identified by QSTEST and QSTESTCD was included. Examples: "ADAS-COG", "MDS-UPDRS".

### QSSCAT
- **Order:** 10
- **Label:** Subcategory for Question
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the questions within the category. Examples: "MENTAL HEALTH" , "DEPRESSION", "WORD RECALL".

### QSORRES
- **Order:** 11
- **Label:** Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Finding as originally received or collected (e.g., "RARELY", "SOMETIMES"). When sponsors apply codelist to indicate that code values are statistically meaningful standardized scores (which are defined by sponsors or by valid methodologies, e.g., SF36 questionnaires), QSORRES will contain the decode format; QSSTRESC and QSSTRESN may contain the standardized code values or scores.

### QSORRESU
- **Order:** 12
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for QSORRES, such as minutes or seconds or the units associated with a visual analog scale.

### QSSTRESC
- **Order:** 13
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the finding for all questions or subscores copied or derived from QSORRES, in a standard format or standard units. QSSTRESC should store all findings in character format; if findings are numeric, they should also be stored in numeric format in QSSTRESN. If question scores are derived from the original finding, then the standard format is the score. Examples: "0", "1".  When sponsors apply codelist to indicate the code values are statistically meaningful standardized scores (which are defined by sponsors or by valid methodologies, e.g., SF36 questionnaires), QSORRES will contain the decode format; QSSTRESC and QSSTRESN may contain the standardized code values or scores.

### QSSTRESN
- **Order:** 14
- **Label:** Numeric Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric findings in standard format; copied in numeric format from QSSTRESC. QSSTRESN should store all numeric results or findings.

### QSSTRESU
- **Order:** 15
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for QSSTRESC or QSSTRESN.

### QSSTAT
- **Order:** 16
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not done or was not answered. Should be null if a result exists in QSORRES.

### QSREASND
- **Order:** 17
- **Label:** Reason Not Performed
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a question was not answered. Used in conjunction with QSSTAT when value is "NOT DONE". Example: "SUBJECT REFUSED".

### QSMETHOD
- **Order:** 18
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C158113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination.

### QSLOBXFL
- **Order:** 19
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.

### QSBLFL
- **Order:** 20
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that QSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### QSDRVFL
- **Order:** 21
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records or questionnaire subscores that do not come from the CRF are examples of records that would be derived for the submission datasets. If QSDRVFL = "Y", then QSORRES may be null with QSSTRESC and (if numeric) QSSTRESN having the derived value.

### VISITNUM
- **Order:** 22
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 23
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 24
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 25
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 26
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the observation date/time of the physical exam finding.

### QSDTC
- **Order:** 27
- **Label:** Date/Time of Finding
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date of questionnaire.

### QSDY
- **Order:** 28
- **Label:** Study Day of Finding
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of finding collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### QSTPT
- **Order:** 29
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when questionnaire should be administered. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See QSTPTNUM and QSTPTREF.

### QSTPTNUM
- **Order:** 30
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of QSTPT to aid in sorting.

### QSELTM
- **Order:** 31
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (QSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by QSTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by QSTPTREF.

### QSTPTREF
- **Order:** 32
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by QSELTM, QSTPTNUM, and QSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### QSRFTDTC
- **Order:** 33
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, QSTPTREF.

### QSEVLINT
- **Order:** 34
- **Label:** Evaluation Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Evaluation interval associated with a QSTEST question represented in ISO 8601 character format. Example: "-P2Y" to represent an interval of 2 years in the question "Have you experienced any episodes in the past 2 years?".

### QSEVINTX
- **Order:** 35
- **Label:** Evaluation Interval Text
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS".
