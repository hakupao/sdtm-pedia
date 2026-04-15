# EG — ECG Test Results

> Class: Findings | Structure: One record per ECG observation per replicate per time point or one record per ECG observation per beat per visit per subject

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

### SPDEVID
- **Order:** 4
- **Label:** Sponsor Device Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a device.

### EGSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### EGGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### EGREFID
- **Order:** 7
- **Label:** ECG Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external ECG identifier. Example: "334PT89".

### EGSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the ECG page.

### EGBEATNO
- **Order:** 9
- **Label:** ECG Beat Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** A sequence number that identifies the beat within an ECG.

### EGTESTCD
- **Order:** 10
- **Label:** ECG Test or Examination Short Name
- **Type:** Char
- **Controlled Terms:** C71153; C120523
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in EGTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in EGTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). EGTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRAG", "QRSAG".  Test codes are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTESTCD) and one 1 tests based on Holter monitoring (HETESTCD).

### EGTEST
- **Order:** 11
- **Label:** ECG Test or Examination Name
- **Type:** Char
- **Controlled Terms:** C71152; C120524
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in EGTEST cannot be longer than 40 characters. Examples: "PR Interval, Aggregate", "QRS Duration, Aggregate".  Test names are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTEST) and 1 for tests based on Holter monitoring (HETEST).

### EGCAT
- **Order:** 12
- **Label:** Category for ECG
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize ECG observations across subjects. Examples: "MEASUREMENT", "FINDING", "INTERVAL".

### EGSCAT
- **Order:** 13
- **Label:** Subcategory for ECG
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the ECG.

### EGPOS
- **Order:** 14
- **Label:** ECG Position of Subject
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".

### EGORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the ECG measurement or finding as originally received or collected. Examples of expected values are "62" or "0.151" when the result is an interval or measurement, or "ATRIAL FIBRILLATION" or "QT PROLONGATION" when the result is a finding.

### EGORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for EGORRES. Examples: "sec", "msec".

### EGSTRESC
- **Order:** 17
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C71150; C120522; C101834
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from EGORRES, in a standard format or standard units. EGSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in EGSTRESN. For example, if a test has results of 62 beats/min, then EGORRES = "62", EGORRESU = "beats/min", EGSTRESC = "62", EGSTRESN = 62, and EGSTRESU = "beats/min" . For other examples, see Original and Standardized Results. Additional examples of result data: "SINUS BRADYCARDIA", "ATRIAL FLUTTER", "ATRIAL FIBRILLATION".  Test results are in 3 separate codelists: EGSTRESC for abnormal test results based on regular 10-second ECGs; HESTRESC for abnormal test results based on Holter monitoring, and NORMABNM for generic test results and/or responses to EGTEST = "Interpretation".

### EGSTRESN
- **Order:** 18
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from EGSTRESC. EGSTRESN should store all numeric test results or findings.

### EGSTRESU
- **Order:** 19
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for EGSTRESC and EGSTRESN.

### EGSTAT
- **Order:** 20
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate an ECG was not done, or an ECG measurement was not taken. Should be null if a result exists in EGORRES.

### EGREASND
- **Order:** 21
- **Label:** Reason ECG Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with EGSTAT when value is "NOT DONE".

### EGXFN
- **Order:** 22
- **Label:** ECG External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** File name and path for the external ECG waveform file.

### EGNAM
- **Order:** 23
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the laboratory or vendor providing the test results.

### EGMETHOD
- **Order:** 24
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C71151
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the ECG test. Example: "12-LEAD STANDARD".

### EGLEAD
- **Order:** 25
- **Label:** Lead Location Used for Measurement
- **Type:** Char
- **Controlled Terms:** C90013
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The lead used for the measurement. Examples: "LEAD 1", "LEAD 2", "LEAD rV2", "LEAD V1".

### EGLOBXFL
- **Order:** 26
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### EGBLFL
- **Order:** 27
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that EGBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### EGDRVFL
- **Order:** 28
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If EGDRVFL="Y", then EGORRES could be null, with EGSTRESC and EGSTRESN (if the result is numeric) having the derived value.

### EGEVAL
- **Order:** 29
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR".

### EGEVALID
- **Order:** 30
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in EGEVAL. Examples: "RADIOLOGIST 1" or "RADIOLOGIST 2".

### EGCLSIG
- **Order:** 31
- **Label:** Clinically Significant, Collected
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a collected observation is clinically significant based on judgment.

### EGREPNUM
- **Order:** 32
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.

### VISITNUM
- **Order:** 33
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 34
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 35
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 36
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 37
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### EGDTC
- **Order:** 38
- **Label:** Date/Time of ECG
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/Time of ECG.

### EGDY
- **Order:** 39
- **Label:** Study Day of ECG
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the ECG, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### EGTPT
- **Order:** 40
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EGTPTNUM and EGTPTREF. Examples: "Start", "5 min post".

### EGTPTNUM
- **Order:** 41
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of EGTPT to aid in sorting.

### EGELTM
- **Order:** 42
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a fixed time point reference (EGTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by EGTPTREF.

### EGTPTREF
- **Order:** 43
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by EGELTM, EGTPTNUM, and EGTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### EGRFTDTC
- **Order:** 44
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by EGTPTREF.
