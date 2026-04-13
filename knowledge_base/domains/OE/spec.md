# OE — Ophthalmic Examinations

> Class: Findings | Structure: One record per ophthalmic finding per method per location, per time point per visit per subject

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
- **Controlled Terms:** C119013
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed.

### OESEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### OEGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### OELNKID
- **Order:** 7
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### OELNKGRP
- **Order:** 8
- **Label:** Link Group
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### OETESTCD
- **Order:** 9
- **Label:** Short Name of Ophthalmic Test or Exam
- **Type:** Char
- **Controlled Terms:** C117743
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for OETEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in OETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). OETESTCD cannot contain characters other than letters, numbers, or underscores. Example: "NUMLCOR".

### OETEST
- **Order:** 10
- **Label:** Name of Ophthalmic Test or Exam
- **Type:** Char
- **Controlled Terms:** C117742
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for the test or examination used to obtain the measurement or finding. The value in OETEST cannot be longer than 40 characters. Example: "Number of Letters Correct" for OETESTCD = "NUMLCOR".

### OETSTDTL
- **Order:** 11
- **Label:** Ophthalmic Test or Exam Detail
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of OETESTCD and OETEST.

### OECAT
- **Order:** 12
- **Label:** Category for Ophthalmic Test or Exam
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Examples: "VISUAL ACUITY", "CONTRAST SENSITIVITY", "OCULAR COMFORT".

### OESCAT
- **Order:** 13
- **Label:** Subcategory for Ophthalmic Test or Exam
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of OECAT values. Example: "HIGH CONTRAST" or "LOW CONTRAST" when OECAT is "VISUAL ACUITY".

### OEORRES
- **Order:** 14
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected. Examples: "120", "<1, NORMAL", "RED SPOT VISIBLE".

### OEORRESU
- **Order:** 15
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original unit for OEORRES. Examples: "mm", "um".

### OEORNRLO
- **Order:** 16
- **Label:** Normal Range Lower Limit-Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Lower end of normal range or reference range for results stored in OEORRES.

### OEORNRHI
- **Order:** 17
- **Label:** Normal Range Upper Limit-Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Upper end of normal range or reference range for results stored in OEORRES.

### OESTRESC
- **Order:** 18
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from OEORRES, in a standard format or in standard units. OESTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in OESTRESN.

### OESTRESN
- **Order:** 19
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from OESTRESC. OESTRESN should store all numeric test results or findings.

### OESTRESU
- **Order:** 20
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized units used for OESTRESC and OESTRESN. Examples: "mm", "um".

### OESTNRLO
- **Order:** 21
- **Label:** Normal Range Lower Limit-Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Lower end of normal range or reference range for standardized results (e.g., OESTRESC, OESTRESN) represented in standardized units (OESTRESU).

### OESTNRHI
- **Order:** 22
- **Label:** Normal Range Upper Limit-Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Upper end of normal range or reference range for standardized results (e.g., OESTRESC, OESTRESN) represented in standardized units (OESTRESU).

### OESTNRC
- **Order:** 23
- **Label:** Normal Range for Character Results
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Normal range or reference range for results stored in OESTRESC that are character in ordinal or categorical scale. Example: "Negative to Trace".

### OENRIND
- **Order:** 24
- **Label:** Normal/Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the value is outside the normal range or reference range. May be defined by OEORNRLO and OEORNRHI or other objective criteria. Examples: "Y", "N"; "HIGH", "LOW"; "NORMAL", "ABNORMAL".

### OERESCAT
- **Order:** 25
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding or medical status per interpretation of test results. Examples: "POSITIVE", "NEGATIVE". The variable OERESCAT is not meant to replace the use of OENRIND for cases where normal ranges are provided.

### OESTAT
- **Order:** 26
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### OEREASND
- **Order:** 27
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with OESTAT when value is "NOT DONE".

### OEXFN
- **Order:** 28
- **Label:** External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Filename for an external file, such as one for a retinal OCT image.

### OELOC
- **Order:** 29
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement. Examples: "EYE" for a finding record relative to the complete eye, "RETINA" for a measurement or assessment of only the retina.

### OELAT
- **Order:** 30
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### OEDIR
- **Order:** 31
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### OEPORTOT
- **Order:** 32
- **Label:** Portion or Totality
- **Type:** Char
- **Controlled Terms:** C99075
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing the distribution (i.e., arrangement of, apportioning of). Examples: "ENTIRE", "SINGLE", "SEGMENT", "MANY".

### OEMETHOD
- **Order:** 33
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Method of the test or examination. Example: "ETDRS EYE CHART" for OETESTCD = "NUMLCOR". The different methods may offer different functionality or granularity, affecting the set of results and associated meaning.

### OELOBXFL
- **Order:** 34
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### OEBLFL
- **Order:** 35
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that OEBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### OEDRVFL
- **Order:** 36
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### OEEVAL
- **Order:** 37
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "INDEPENDENT ASSESSOR", "INVESTIGATOR".

### OEEVALID
- **Order:** 38
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in OEEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2".

### OEACPTFL
- **Order:** 39
- **Label:** Accepted Record Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** In cases where more than one assessor provides an evaluation of a result or response, this flag identifies the record that is considered, by an independent assessor, to be the accepted evaluation. Expected to be "Y" or null.

### OEREPNUM
- **Order:** 40
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.

### VISITNUM
- **Order:** 41
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 42
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 43
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 44
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 45
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### OEDTC
- **Order:** 46
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date/time of the observation.

### OEDY
- **Order:** 47
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Actual study day of observation/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### OETPT
- **Order:** 48
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point.

### OETPTNUM
- **Order:** 49
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### OEELTM
- **Order:** 50
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to a planned fixed reference (OETPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### OETPTREF
- **Order:** 51
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by OETPT, OETPTNUM, and OEELTM.

### OERFTDTC
- **Order:** 52
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, OETPTREF.
