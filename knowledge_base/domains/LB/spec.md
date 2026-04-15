# LB — Laboratory Test Results

> Class: Findings | Structure: One record per lab test per time point per visit per subject

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

### LBSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### LBGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### LBREFID
- **Order:** 6
- **Label:** Specimen ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier. Example: specimen ID.

### LBSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the Lab page.

### LBTESTCD
- **Order:** 8
- **Label:** Lab Test or Examination Short Name
- **Type:** Char
- **Controlled Terms:** C65047
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in LBTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in LBTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). LBTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "ALT", "LDH".

### LBTEST
- **Order:** 9
- **Label:** Lab Test or Examination Name
- **Type:** Char
- **Controlled Terms:** C67154
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. Note: Any test normally performed by a clinical laboratory is considered a lab test. The value in LBTEST cannot be longer than 40 characters. Examples: "Alanine Aminotransferase", "Lactate Dehydrogenase".

### LBTSTCND
- **Order:** 10
- **Label:** Test Condition
- **Type:** Char
- **Controlled Terms:** C181175
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed.

### LBBDAGNT
- **Order:** 11
- **Label:** Binding Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent that is binding to the entity in the LBTEST variable. The LBBDAGNT variable is used to indicate that there is a binding relationship between the entities in the LBTEST and LBBDAGNT variables, regardless of direction.  LBBDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the 2 entities in LBTEST and LBBDAGNT. In other words, the combination of LBTEST and LBBDAGNT should describe the thing, the entity, or the analyte being measured, without the need for additional variables.  The binding agent may be (but is not limited to) a test article, a portion of the test article, a related compound, or an endogenous molecule.

### LBTSTOPO
- **Order:** 12
- **Label:** Test Operational Objective
- **Type:** Char
- **Controlled Terms:** C181170
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the high-level purpose of the test at the operational level.

### LBCAT
- **Order:** 13
- **Label:** Category for Lab Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of related records across subjects. Examples: "HEMATOLOGY", "URINALYSIS", "CHEMISTRY".

### LBSCAT
- **Order:** 14
- **Label:** Subcategory for Lab Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of a test category. Examples: "DIFFERENTIAL", "COAGULATION", "LIVER FUNCTION", "ELECTROLYTES".

### LBORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### LBORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for LBORRES. Example: "g/L".

### LBRESSCL
- **Order:** 17
- **Label:** Result Scale
- **Type:** Char
- **Controlled Terms:** C177910
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Classifies the scale of the original result value; for example, whether the result is ordinal, nominal, quantitative, or narrative.

### LBRESTYP
- **Order:** 18
- **Label:** Result Type
- **Type:** Char
- **Controlled Terms:** C179588
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Classifies the kind of result (i.e., property type) originally reported for the test. Examples include substance concentration, proportion, mass rate, and arbitrary concentration.

### LBCOLSRT
- **Order:** 19
- **Label:** Collected Summary Result Type
- **Type:** Char
- **Controlled Terms:** C177908
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the type of collected summary result. This includes source summary results collected on a CRF or provided by an external vendor (e.g., central lab). If the summary result is derived by the sponsor using individual source data records from SDTM, the derived summary result is represented in ADaM. If the summary result is produced and reported by the lab, the collected summary result is represented in SDTM.

### LBORNRLO
- **Order:** 20
- **Label:** Reference Range Lower Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### LBORNRHI
- **Order:** 21
- **Label:** Reference Range Upper Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### LBLLOD
- **Order:** 22
- **Label:** Lower Limit of Detection
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** The lowest threshold (as originally received or collected) for reliably detecting the presence or absence of substance measured by a specific test. The value for the field will be as described in documentation from the instrument or lab vendor.

### LBSTRESC
- **Order:** 23
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C102580
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from LBORRES in a standard format or standard units. LBSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in LBSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in LBORRES and these results effectively have the same meaning, they could be represented in standard format in LBSTRESC as "NEGATIVE". For other examples, see Original and Standardized Results.

### LBSTRESN
- **Order:** 24
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from LBSTRESC. LBSTRESN should store all numeric test results or findings.

### LBSTRESU
- **Order:** 25
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for LBSTRESC or LBSTRESN.

### LBSTNRLO
- **Order:** 26
- **Label:** Reference Range Lower Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Lower end of reference range for continuous measurements for LBSTRESC/LBSTRESN in standardized units. Should be populated only for continuous results.

### LBSTNRHI
- **Order:** 27
- **Label:** Reference Range Upper Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.

### LBSTNRC
- **Order:** 28
- **Label:** Reference Range for Char Rslt-Std Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** For normal range values that are character in ordinal scale or if categorical ranges were supplied. Examples: "-1 to +1", "NEGATIVE TO TRACE".

### LBNRIND
- **Order:** 29
- **Label:** Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates where the value falls with respect to reference range defined by LBORNRLO and LBORNRHI, LBSTNRLO and LBSTNRHI, or by LBSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether LBNRIND refers to the original or standard reference ranges and results. LBNRIND is not used to indicate clinical significance.

### LBSTAT
- **Order:** 30
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate exam not done. Should be null if a result exists in LBORRES.

### LBREASND
- **Order:** 31
- **Label:** Reason Test Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED", or "SPECIMEN LOST". Used in conjunction with LBSTAT when value is "NOT DONE".

### LBNAM
- **Order:** 32
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the laboratory that performed the test.

### LBLOINC
- **Order:** 33
- **Label:** LOINC Code
- **Type:** Char
- **Controlled Terms:** LOINC
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Code for the lab test from the LOINC code system. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the Define-XML external codelist attributes.

### LBSPEC
- **Order:** 34
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE".

### LBSPCCND
- **Order:** 35
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The physical state or quality of a sample for an assessment. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC".

### LBSPCUFL
- **Order:** 36
- **Label:** Specimen Usability for the Test
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the usability of the specimen for the test. The value will be "N" if the specimen is not usable, and null if the specimen is usable.

### LBMETHOD
- **Order:** 37
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "EIA" (enzyme immunoassay), "ELECTROPHORESIS", "DIPSTICK".

### LBANMETH
- **Order:** 38
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** C160922
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result (e.g., a calculation used to measure eGFR).

### LBTMTHSN
- **Order:** 39
- **Label:** Test Method Sensitivity
- **Type:** Char
- **Controlled Terms:** C179589
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The sensitivity of the test methodology with respect to observation, detection, or quantification.

### LBLOBXFL
- **Order:** 40
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### LBBLFL
- **Order:** 41
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that LBBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### LBFAST
- **Order:** 42
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status. Examples: "Y", "N".

### LBDRVFL
- **Order:** 43
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or do not come from the CRF, or are not as originally received or collected are examples of records that might be derived for the submission datasets. If LBDRVFL="Y", then LBORRES may be null, with LBSTRESC and (if numeric) LBSTRESN having the derived value.

### LBTOX
- **Order:** 44
- **Label:** Toxicity
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of toxicity quantified by LBTOXGR. The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.

### LBTOXGR
- **Order:** 45
- **Label:** Standard Toxicity Grade
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Records toxicity grade value using a standard toxicity scale (e.g., the NCI CTCAE). If value is from a numeric scale, represent only the number (e.g., "2" not "Grade 2"). The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.

### LBCLSIG
- **Order:** 46
- **Label:** Clinically Significant, Collected
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a collected observation is clinically significant based on judgment.

### VISITNUM
- **Order:** 47
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 48
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 49
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 50
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 51
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### LBDTC
- **Order:** 52
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection represented in ISO 8601 character format.

### LBENDTC
- **Order:** 53
- **Label:** End Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of specimen collection represented in ISO 8601 character format.

### LBDY
- **Order:** 54
- **Label:** Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.

### LBENDY
- **Order:** 55
- **Label:** Study Day of End of Observation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### LBTPT
- **Order:** 56
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See LBTPTNUM and LBTPTREF. Examples: "Start", "5 min post".

### LBTPTNUM
- **Order:** 57
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of LBTPT to aid in sorting.

### LBELTM
- **Order:** 58
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (LBTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable. Represented as ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by LBTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by LBTPTREF.

### LBTPTREF
- **Order:** 59
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by LBELTM, LBTPTNUM, and LBTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### LBRFTDTC
- **Order:** 60
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, LBTPTREF.

### LBPTFL
- **Order:** 61
- **Label:** Point in Time Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** An indication that the specimen was collected at a single point in time. The value is "Y" or null. The intent of this variable in the LB domain is to aid mapping to LOINC codes in the dataset, when LOINC part "Time Aspect" = "Pt".

### LBPDUR
- **Order:** 62
- **Label:** Planned Duration
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned duration of specimen collection. If LBPTFL is "Y" then LBPDUR is null.
