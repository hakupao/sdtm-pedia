# PC — Pharmacokinetics Concentrations

> Class: Findings | Structure: One record per sample characteristic or time-point concentration per reference time point or per analyte per subject

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

### PCSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### PCGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain to support relationships within the domain and between domains.

### PCREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier.

### PCSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number.

### PCTESTCD
- **Order:** 8
- **Label:** Pharmacokinetic Test Short Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the analyte or specimen characteristic. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "ASA", "VOL", "SPG".

### PCTEST
- **Order:** 9
- **Label:** Pharmacokinetic Test Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Name of the analyte or specimen characteristic. Note any test normally performed by a clinical laboratory is considered a lab test. The value in PCTEST cannot be longer than 40 characters. Examples: "Acetylsalicylic Acid", "Volume", "Specific Gravity".

### PCCAT
- **Order:** 10
- **Label:** Test Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records. Examples: "ANALYTE", "SPECIMEN PROPERTY".

### PCSCAT
- **Order:** 11
- **Label:** Test Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of a test category.

### PCORRES
- **Order:** 12
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### PCORRESU
- **Order:** 13
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C85494
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for PCORRES. Example: "mg/L".

### PCSTRESC
- **Order:** 14
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from PCORRES in a standard format or standard units. PCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in PCORRES, and these results effectively have the same meaning, they could be represented in standard format in PCSTRESC as "NEGATIVE". For other examples, see general assumptions.

### PCSTRESN
- **Order:** 15
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from PCSTRESC. PCSTRESN should store all numeric test results or findings.

### PCSTRESU
- **Order:** 16
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C85494
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for PCSTRESC and PCSTRESN.

### PCSTAT
- **Order:** 17
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a result was not obtained. Should be null if a result exists in PCORRES.

### PCREASND
- **Order:** 18
- **Label:** Reason Test Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a result was not obtained, such as "SPECIMEN LOST". Used in conjunction with PCSTAT when value is "NOT DONE".

### PCNAM
- **Order:** 19
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Name or identifier of the laboratory or vendor who provides the test results.

### PCSPEC
- **Order:** 20
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE".

### PCSPCCND
- **Order:** 21
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC".

### PCMETHOD
- **Order:** 22
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "HPLC/MS", "ELISA". This should contain sufficient information and granularity to allow differentiation of various methods that might have been used within a study.

### PCFAST
- **Order:** 23
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status.

### PCDRVFL
- **Order:** 24
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, which do not come from the CRF, are examples of records that would be derived for the submission datasets. If PCDRVFL = "Y", then PCORRES may be null with PCSTRESC, and PCSTRESN (if the result is numeric) having the derived value.

### PCLLOQ
- **Order:** 25
- **Label:** Lower Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates the lower limit of quantitation for an assay. Units should be those used in PCSTRESU.

### PCULOQ
- **Order:** 26
- **Label:** Upper Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates the upper limit of quantitation for an assay. Units should be those used in PCSTRESU.

### VISITNUM
- **Order:** 27
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 28
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 29
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 30
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 31
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### PCDTC
- **Order:** 32
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection represented in ISO 8601 character format. If there is no end time, then this will be the collection time.

### PCENDTC
- **Order:** 33
- **Label:** End Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of specimen collection represented in ISO 8601 character format. If there is no end time, the collection time should be stored in PCDTC, and PCENDTC should be null.

### PCDY
- **Order:** 34
- **Label:** Actual Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### PCENDY
- **Order:** 35
- **Label:** Study Day of End of Observation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### PCTPT
- **Order:** 36
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See PCTPTNUM and PCTPTREF. Examples: "Start", "5 min post".

### PCTPTNUM
- **Order:** 37
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of PCTPT to aid in sorting.

### PCELTM
- **Order:** 38
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (PCTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date time variable.

### PCTPTREF
- **Order:** 39
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point used as a basis for PCTPT, PCTPTNUM, and PCELTM. Example: "MOST RECENT DOSE".

### PCRFTDTC
- **Order:** 40
- **Label:** Date/Time of Reference Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point described by PCTPTREF.

### PCEVLINT
- **Order:** 41
- **Label:** Evaluation Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Evaluation Interval associated with a PCTEST record represented in ISO 8601 character format. Example: "-PT2H" to represent an evaluation interval of 2 hours prior to a PCTPT.
