# IS — Immunogenicity Specimen Assessments

> Class: Findings | Structure: One record per test per visit per subject

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

### NHOID
- **Order:** 4
- **Label:** Non-host Organism ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears.

### ISSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### ISGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### ISREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier. Example: "458975-01".

### ISSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### ISTESTCD
- **Order:** 9
- **Label:** Immunogenicity Test/Exam Short Name
- **Type:** Char
- **Controlled Terms:** C120525
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in ISTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in ISTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). ISTESTCD cannot contain characters other than letters, numbers, or underscores.

### ISTEST
- **Order:** 10
- **Label:** Immunogenicity Test or Examination Name
- **Type:** Char
- **Controlled Terms:** C120526
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in ISTEST cannot be longer than 40 characters. Example: "Immunoglobulin E".

### ISTSTCND
- **Order:** 11
- **Label:** Test Condition
- **Type:** Char
- **Controlled Terms:** C181175
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed.

### ISCNDAGT
- **Order:** 12
- **Label:** Test Condition Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent used to impose a test condition. Examples are different stimulating agents used in immunoassays such as those in the Interferon Gamma Response assay (e.g., Mycobacterium tuberculosis ESAT-6, CFP-10, TB 7.7, Mitogen).

### ISBDAGNT
- **Order:** 13
- **Label:** Binding Agent
- **Type:** Char
- **Controlled Terms:** C85491; C181169
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the agent that is binding to the entity in the ISTEST variable. ISBDAGNT is used to indicate that there is a binding relationship between the entities in the ISTEST and ISBDAGNT variables, regardless of direction. \n ISBDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the 2 entities in ISTEST and ISBDAGNT. In other words, the combination of ISTEST and ISBDAGNT should describe the entity or the analyte being measured, without the need for additional variables. \n The binding agent may be (but is not limited to) a test article, a portion of the test article, a related compound, an endogenous molecule, an allergen, or an infectious agent.

### ISTSTOPO
- **Order:** 14
- **Label:** Test Operational Objective
- **Type:** Char
- **Controlled Terms:** C181170
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the high-level purpose of the test at the operational level. If populated, valid values are "SCREEN", "CONFIRM", and "QUANTIFY".

### ISMSCBCE
- **Order:** 15
- **Label:** Molecule Secreted by Cells
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the entity secreted by the cells represented in ISTEST. The combination of ISTEST and ISMSCBCE should describe the entity or the analyte being measured, without the need for additional variables.

### ISTSTDTL
- **Order:** 16
- **Label:** Test Detail
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of ISTESTCD and ISTEST.

### ISCAT
- **Order:** 17
- **Label:** Category for Immunogenicity Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values across subjects. Example: "SEROLOGY".

### ISSCAT
- **Order:** 18
- **Label:** Subcategory for Immunogenicity Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of ISCAT.

### ISORRES
- **Order:** 19
- **Label:** Results or Findings in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### ISORRESU
- **Order:** 20
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for ISORRES. Examples: "Index Value", "gpELISA", "unit/mL".

### ISORNRLO
- **Order:** 21
- **Label:** Reference Range Lower Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### ISORNRHI
- **Order:** 22
- **Label:** Reference Range Upper Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### ISSTRESC
- **Order:** 23
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from ISORRES, in a standard format or in standard units. ISSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in ISSTRESN.

### ISSTRESN
- **Order:** 24
- **Label:** Numeric Results/Findings in Std. Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from ISSTRESC. ISSTRESN should store all numeric test results or findings.

### ISSTRESU
- **Order:** 25
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized units used for ISSTRESC and ISSTRESN. Examples: "Index Value", "gpELISA", "unit/mL".

### ISSTNRLO
- **Order:** 26
- **Label:** Reference Range Lower Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Lower end of reference range for continuous measurements for ISSTRESC/ISSTRESN in standardized units. Should be populated only for continuous results.

### ISSTNRHI
- **Order:** 27
- **Label:** Reference Range Upper Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.

### ISSTNRC
- **Order:** 28
- **Label:** Reference Range for Char Rslt-Std Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** For normal range values that are character in ordinal scale or if categorical ranges were supplied. Examples: "-1 to +1", "NEGATIVE TO TRACE".

### ISNRIND
- **Order:** 29
- **Label:** Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates where the value falls with respect to reference range defined by ISORNRLO and ISORNRHI, ISSTNRLO and ISSTNRHI, or by ISSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". \n Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether ISNRIND refers to the original or standard reference ranges and results. \n Should not be used to indicate clinical significance.

### ISSTAT
- **Order:** 30
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a test was not done. Should be null if a result exists in ISORRES.

### ISREASND
- **Order:** 31
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Used in conjunction with ISSTAT when value is "NOT DONE".

### ISNAM
- **Order:** 32
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the laboratory or vendor who provided the test results.

### ISSPEC
- **Order:** 33
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the types of specimen used for a measurement. Example: "SERUM".

### ISSPCCND
- **Order:** 34
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC".

### ISSPCUFL
- **Order:** 35
- **Label:** Specimen Usability for the Test
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the usability of the specimen for the test. The value will be "N" if the specimen is not usable, and null if the specimen is usable.

### ISMETHOD
- **Order:** 36
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "ELISA", "ELISPOT".

### ISLOBXFL
- **Order:** 37
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### ISBLFL
- **Order:** 38
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that ISBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### ISDRVFL
- **Order:** 39
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Examples of records that might be derived for the submission datasets include those that represent the average of other records, do not come from the CRF, or are not as originally received or collected. If ISDRVFL="Y", then ISORRES may be null, with ISSTRESC and (if numeric) ISSTRESN having the derived value.

### ISLLOQ
- **Order:** 40
- **Label:** Lower Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates the lower limit of quantitation for an assay. Units will be those used for ISSTRESU.

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
- **CDISC Notes:** Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

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
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 45
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### ISDTC
- **Order:** 46
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation.

### ISENDTC
- **Order:** 47
- **Label:** End Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the observation.

### ISDY
- **Order:** 48
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to sponsor-defined RFSTDTC in Demographics.

### ISENDY
- **Order:** 49
- **Label:** Study Day of End of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### ISTPT
- **Order:** 50
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See ISTPTNUM and ISTPTREF. Examples: "Start", "5 min post".

### ISTPTNUM
- **Order:** 51
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of ISTPT to aid in sorting.

### ISELTM
- **Order:** 52
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (ISTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable. Represented as ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by ISTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by ISTPTREF.

### ISTPTREF
- **Order:** 53
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by ISELTM, ISTPTNUM, and ISTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### ISRFTDTC
- **Order:** 54
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, ISTPTREF.
