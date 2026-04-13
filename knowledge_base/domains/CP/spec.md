# CP — Cell Phenotype Findings

> Class: Findings | Structure: One record per test per specimen per timepoint per visit per subject

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

### CPSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of subject records within a domain. May be any valid number.

### CPGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### CPREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier.

### CPSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the lab page.

### CPLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### CPLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### CPTESTCD
- **Order:** 10
- **Label:** Test or Examination Short Name
- **Type:** Char
- **Controlled Terms:** C181173
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in CPTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). CPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MONO", "MNS".

### CPTEST
- **Order:** 11
- **Label:** Name of Measurement, Test or Examination
- **Type:** Char
- **Controlled Terms:** C181174
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for CPTESTCD. For cell phenotyping, the name (often abbreviated) of the cell population, as it is generally accepted by the scientific community, is populated (rather than a colloquial designation based on a primary marker, e.g., TLym Help rather than CD4). When the test is for a sublineage which can only be identified by specifying additional markers (i.e., has not been given a name) or which is further restricted to a subpopulation based on a particular cell state (e.g., activated, proliferating, apoptotic), the Sublineage Marker String (CPSBMRKS), Cell State (CPCELSTA), and Cell State Marker String (CPCSMRKS) variables are additionally populated and the value in CPTEST is suffixed with "Sub" to denote that it is a subset of the population identified in CPTEST (e.g., Monocytes Sub). \n The value in CPTEST cannot be longer than 40 characters.

### CPSBMRKS
- **Order:** 12
- **Label:** Sublineage Marker String
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to further subset the cell population identified in CPTEST based on the use of additional marker(s) that define a sublineage. The value in CPSBMRKS is used in combination with values in CPTEST and CPCELSTA to fully describe the cell population being measured. As such, it is an essential component of the full test name. \n For example, three unnamed sublineages of monocytes have been identified as: CCR2+CD16-, CCR2-CD16+, and CCR2+CD16+. Whereas the entire monocyte cell population can be defined as CD14+ cells, the additional CCR2 and CD16 markers are used to differentiate one sublineage from another. As none of these sublineages have been given names, they are only known by the CCR2 and CD16 marker combinations. By associating the CPTEST value of "Monocytes Sub" with, for example, a value of "CCR2+CD16-" in CPSBMRKS, the full test is defined to be the CCR2+CD16- monocyte subpopulation.

### CPCELSTA
- **Order:** 13
- **Label:** Cell State
- **Type:** Char
- **Controlled Terms:** C181172
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A textual description of a subset of the cell population identified in CPTEST based on a particular functional and/or biological state (e.g., "ACTIVATED", "PROLIFERATING", "SENESCENT"). When populated, the values in CPCELSTA and CPSMRKS, in combination with the values in CPTEST and CPSBMRKS, fully describe the cell population being measured.

### CPCSMRKS
- **Order:** 14
- **Label:** Cell State Marker String
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies the marker(s) or indicator(s) used to define the cell state (i.e., the value in CPCELSTA). \n For example, when Ki67 expression is used to determine that a cell population is in a proliferating state (i.e., CPCELSTA value="PROLIFERATING"), the value "Ki67+" in CPCSMRKS indicates that positive expression of Ki67 was used to define the population as proliferating. Similarly, a value of "Ki67-" in CPCSMRKS would indicate that lack of expression of Ki67 defined the "NON-PROLIFERATING" cell state in CPCELSTA. The CPCSMRKS value is useful for quickly determining which marker(s) were used to classify (i.e., operationally define) a cell population based on a functional/biological state.

### CPTSTCND
- **Order:** 15
- **Label:** Test Condition
- **Type:** Char
- **Controlled Terms:** C181175
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed. --TSTCND is generally used to distinguish between two or more records where the same assay is performed under varying (as opposed to fixed) conditions, usually for the purpose of making a comparison. For example, when the same assay (identified in --TEST) is performed under stimulated and non-stimulated conditions, the --TSTCND variable is used distinguish between the records.

### CPCNDAGT
- **Order:** 16
- **Label:** Test Condition Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent, if applicable, used to impose the condition identified in CPTSTCND. For example, records might be produced for the same assay run under stimulating (CPTSTCND value = "STIMULATED") conditions produced by different stimulating agents (e.g., phorbol myristate acetate, concanavalin A, PHA-P, TNF-alpha, Ionomycin, candida antigen).

### CPBDAGNT
- **Order:** 17
- **Label:** Binding Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent that is binding to the entity in the CPTEST variable. The CPBDAGNT variable is used to indicate that there is a binding relationship between the entities in the CPTEST and CPBDAGNT variables, regardless of direction. \n The binding agent may be, but is not limited to, a test article; a portion of a test article; a substance related to a test article; an endogenous molecule; an allergen; an infectious agent; or a reagent (e.g., primary antibody) that confers the binding specificity for the measurement defined in CPTEST when it is needed to uniquely identify the test.

### CPABCLID
- **Order:** 18
- **Label:** Antibody Clone Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies the antibody clone (e.g., supplier-provided catalog name) used to confer specificity for the binding agent specified in CPBDAGNT.

### CPMRKSTR
- **Order:** 19
- **Label:** Marker String
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** The text string identifying the full set of markers/indicators used by the laboratory to operationally define the complete test based on the combination of CPTEST, CPSBMRKS, and CPCELSTA. Because laboratories often use different markers/indicators to identify a cell population, the relationship between a named cell population in CPTEST (as combined with CPSBMRKS and CPCELSTA values) and the set of markers used to identify that population is many-to-one. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different sets of markers, it is necessary to operationally define the test in terms of the complete set of markers/indicators used to perform that test.

### CPGATE
- **Order:** 20
- **Label:** Gate
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The sponsor-defined name assigned to a gate. Gates are electronic (i.e., a device setting or software-defined) boundaries set by a user to virtually parse a specimen into discrete populations based on a set of defined characteristics (e.g., presence, absence, or intensity of expression of various markers; physical size; internal complexity or granularity). Gates are used to constrain data collection or analysis to a specific cell population or region of interest within the specimen.

### CPGATDEF
- **Order:** 21
- **Label:** Gate Definition
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The text string identifying the set of parameters and the order in which they are applied to define the gating strategy. In practice, a series of 2-dimensional sub-gates based on different cell characteristics (i.e., markers/indicators/physical properties) are most often combined until the cell population of interest is sufficiently resolved (i.e., electronically isolated) from other cell populations contained within the specimen. \n For complex analyses, differences in gating strategies can produce subtle differences in results obtained for a test. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different gating strategies, it is often necessary to qualify the test in terms of the gating strategy. For some purposes, however, and at the discretion of the sponsor, only the ultimate or penultimate gate is identified. When specifying the gating strategy in CPGATDEF, each sub-gate should be listed in the order it was applied and separated from the next sub-gate using the pipe/vertical line ("|") character.

### CPSPTSTD
- **Order:** 22
- **Label:** Sponsor Test Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Sponsor's description of a test. The variable is intended to contain highly structured test description metadata used by a sponsor to unambiguously define (label) a test. Such values generally reside in a sponsor/laboratory test metadata repository. CPSPTSTD is not intended for unstructured (spontaneous) free text. \n An example of appropriate usage is when it is necessary to include identifying information for a target cell population on which a test is conducted when the target population is not part of the test name, e.g., tests for quantitative expression of a particular marker on a specific cell population.

### CPCAT
- **Order:** 23
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** C181171
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values across subjects. Examples: "IMMUNOPHENOTYPING", "CELL FUNCTION", "TARGET ENGAGEMENT".

### CPSCAT
- **Order:** 24
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of CPCAT.

### CPTSTPNL
- **Order:** 25
- **Label:** Test Panel
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined textual description used to group tests run together as part of a test panel. Can be used with --GRPID to ensure that relationships between associated tests are accurately identified.

### CPORRES
- **Order:** 26
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### CPORRESU
- **Order:** 27
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for CPORRES. Examples: "10^6/L", "%", "MESF".

### CPRESSCL
- **Order:** 28
- **Label:** Result Scale
- **Type:** Char
- **Controlled Terms:** C177910
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Classifies the scale of the original result value with respect to whether the result is quantitative, ordinal, nominal, or narrative.

### CPRESTYP
- **Order:** 29
- **Label:** Result Type
- **Type:** Char
- **Controlled Terms:** C179588
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Classifies the kind of result (i.e., property type) originally reported for the test. Examples: "NUMBER CONCENTRATION", "NUMBER FRACTION", "RATIO".

### CPCOLSRT
- **Order:** 30
- **Label:** Collected Summary Result Type
- **Type:** Char
- **Controlled Terms:** C177908
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the type of collected summary result. This includes source summary results collected on a CRF or provided by an external vendor (e.g., central lab). If the summary result is derived using individual source data records, this summary result should be represented in ADaM. If a sponsor has both a collected summary result and a derived summary result, the collected summary result should be represented in SDTM and the derived summary result should be represented in ADaM.

### CPORNRLO
- **Order:** 31
- **Label:** Reference Range Lower Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### CPORNRHI
- **Order:** 32
- **Label:** Reference Range Upper Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### CPSTRESC
- **Order:** 33
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from CPORRES in a standard format or in standard units. CPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CPSTRESN.

### CPSTRESN
- **Order:** 34
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from CPSTRESC. CPSTRESN should store all numeric test results or findings.

### CPSTRESU
- **Order:** 35
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for CPSTRESC or CPSTRESN.

### CPSTNRLO
- **Order:** 36
- **Label:** Reference Range Lower Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Lower end of reference range for continuous measurements for CPSTRESC/CPSTRESN in standardized units. Should be populated only for continuous results.

### CPSTNRHI
- **Order:** 37
- **Label:** Reference Range Upper Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.

### CPNRIND
- **Order:** 38
- **Label:** Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates where the value falls with respect to reference range defined by CPORNRLO and CPORNRHI, CPSTNRLO and CPSTNRHI, or by CPSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether CPNRIND refers to the original or standard reference ranges and results. CPNRIND should not be used to indicate clinical significance.

### CPSTAT
- **Order:** 39
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that the test was not performed or that it was attempted but did not generate a result. Should be null if a result exists in CPORRES.

### CPREASND
- **Order:** 40
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a test was not performed, e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED", "SPECIMEN LOST". Used in conjunction with CPSTAT when value is "NOT DONE".

### CPNAM
- **Order:** 41
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the laboratory that performed the test.

### CPLOINC
- **Order:** 42
- **Label:** LOINC Code
- **Type:** Char
- **Controlled Terms:** LOINC
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Code for the test from the LOINC code system. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the Define-XML external codelist attributes.

### CPSPEC
- **Order:** 43
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "BLOOD", "BONE MARROW".

### CPSPCCND
- **Order:** 44
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The physical state or quality of a specimen for an assessment. Example: "CLOTTED".

### CPMETHOD
- **Order:** 45
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Example: "FLOW CYTOMETRY".

### CPANMETH
- **Order:** 46
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result.

### CPLOBXFL
- **Order:** 47
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### CPBLFL
- **Order:** 48
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. The value should be "Y" or null.

### CPDRVFL
- **Order:** 49
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or do not come from the CRF, or are not as originally received or collected are examples of records that might be derived for the submission datasets. If CPDRVFL = "Y", then CPORRES may be null, with CPSTRESC and (if numeric) CPSTRESN having the derived value.

### CPCLSIG
- **Order:** 50
- **Label:** Clinically Significant, Collected
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a collected observation is clinically significant based on judgement.

### VISITNUM
- **Order:** 51
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 52
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 53
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer.

### TAETORD
- **Order:** 54
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 55
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### CPDTC
- **Order:** 56
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection represented in ISO 8601 character format.

### CPDY
- **Order:** 57
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC value in Demographics.

### CPTPT
- **Order:** 58
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a specimen is to be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (i.e., to the value in CPTPTREF). Example: "1 hour post".

### CPTPTNUM
- **Order:** 59
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of CPTPT to aid in sorting. When CPTPT is represented as an elapsed time relative to a fixed reference point (i.e., to the value in CPTPTREF), the values in CPTPTNUM should be assigned in ascending order relative to the value in CPTPTREF. For example, records for time points where CPTPT = "5 minutes post", 1 hour post", and "4 hours post" could be represented in CPTPTNUM as "1", "2", and "3", which maintains the order between CPTPT and CPTPTNUM with respect to the fixed time point reference in CPTPTREF.

### CPELTM
- **Order:** 60
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to the planned fixed reference value in CPTPTREF, represented in ISO 8601 duration format. Examples: "-PT15M" to represent 15 minutes prior to the reference time point indicated by CPTPTREF, "T8H" to represent 8 hours after the reference time point represented by CPTPTREF.

### CPTPTREF
- **Order:** 61
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Descriptive name of the fixed reference point referred to by CPTPT, CPTPTNUM, and CPELTM. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### CPRFTDTC
- **Order:** 62
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by CPTPTREF.
