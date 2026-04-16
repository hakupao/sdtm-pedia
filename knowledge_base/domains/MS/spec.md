# MS — Microbiology Susceptibility

> Class: Findings | Structure: One record per microbiology susceptibility test (or other organism-related finding) per organism found in MB

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

### MSSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1.

### MSGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain. In SDTMIG v3.2 this was an Expected variable. In this version, the core designation has been changed to Permissible.

### MSREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier (e.g., an identifier for the culture/isolate being tested for susceptibility).

### MSSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.

### MSLNKID
- **Order:** 9
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. For example, it may be used to link genetic findings (in the PF domain) about a microbe to the original culture of that microbe (in MB), or to susceptibility records (in MS) if needed.

### MSTESTCD
- **Order:** 10
- **Label:** Short Name of Assessment
- **Type:** Char
- **Controlled Terms:** C128688
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for MSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MIC" for Minimum Inhibitory Concentration; "MICROSUS" for Microbial Susceptibility.

### MSTEST
- **Order:** 11
- **Label:** Name of Assessment
- **Type:** Char
- **Controlled Terms:** C128687
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in MSTEST cannot be longer than 40 characters. Examples: "Minimum Inhibitory Concentration", "Microbial Susceptibility".

### MSAGENT
- **Order:** 12
- **Label:** Agent Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** The name of the agent for which resistance is tested. The agent specified may be based on genetic markers or direct phenotypic drug sensitivity testing. Examples: "Penicillin", name of study drug.

### MSCONC
- **Order:** 13
- **Label:** Agent Concentration
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Numeric concentration of agent listed in MSAGENT.

### MSCONCU
- **Order:** 14
- **Label:** Agent Concentration Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Units for value of the agent concentration listed in MSCONC. Example: "mg/L".

### MSTSTDTL
- **Order:** 15
- **Label:** Measurement, Test or Examination Detail
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of MSTESTCD and MSTEST.

### MSCAT
- **Order:** 16
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of MSTEST values.

### MSSCAT
- **Order:** 17
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of MSCAT values.

### MSORRES
- **Order:** 18
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### MSORRESU
- **Order:** 19
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for MSORRES. Examples: "ug/mL".

### MSSTRESC
- **Order:** 20
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from MSORRES in a standard format or in standard units. MSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MSSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in MSORRES and these results effectively have the same meaning, they could be represented in standard format in MSSTRESC as "NEGATIVE".

### MSSTRESN
- **Order:** 21
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from MSSTRESC. MSSTRESN should store all numeric test results or findings.

### MSSTRESU
- **Order:** 22
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for MSSTRESC and MSSTRESN. Example: "mol/L".

### MSNRIND
- **Order:** 23
- **Label:** Normal/Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the value is outside the normal range or reference range. May be defined by MSORNRLO and MSORNRHI or other objective criteria. Examples: "Y", "N", "HIGH", "LOW", "NORMAL". "ABNORMAL".

### MSRESCAT
- **Order:** 24
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** C85495
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding. In SDTMIG v3.2, MSRESCAT was used to categorize a numeric susceptibility result represented in MSORRES as either "SUSCEPTIBLE", "INTERMEDIATE", or "RESISTANT". However, results from some susceptibility tests may report only a categorical result and not a numeric result. Thus, in order for susceptibility results to be represented consistently, MSRESCAT should no longer be used for this purpose. In this version, the core designation has been changed from Expected to Permissible.

### MSSTAT
- **Order:** 25
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### MSREASND
- **Order:** 26
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with MSSTAT when value is "NOT DONE".

### MSXFN
- **Order:** 27
- **Label:** External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Filename for an external file.

### MSNAM
- **Order:** 28
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor (e.g., laboratory) that provided the test results.

### MSLOINC
- **Order:** 29
- **Label:** LOINC Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Logical Observation Identifiers Names and Codes (LOINC) code for the topic variable such as a lab test.

### MSSPEC
- **Order:** 30
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Example: "SPUTUM".

### MSSPCCND
- **Order:** 31
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the condition of the specimen. Example: "CLOUDY".

### MSLOC
- **Order:** 32
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement.

### MSLAT
- **Order:** 33
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### MSDIR
- **Order:** 34
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### MSMETHOD
- **Order:** 35
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "EPSILOMETER", "MACRO BROTH DILUTION".

### MSANMETH
- **Order:** 36
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result (e.g., an image or a genetic sequence).

### MSLOBXFL
- **Order:** 37
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### MSBLFL
- **Order:** 38
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that MSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### MSFAST
- **Order:** 39
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status. Valid values include "Y", "N", "U", or null if not relevant.

### MSDRVFL
- **Order:** 40
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### MSEVAL
- **Order:** 41
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "MICROSCOPIST".

### MSEVALID
- **Order:** 42
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in MSEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2".

### MSACPTFL
- **Order:** 43
- **Label:** Accepted Record Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** In cases where more than 1 assessor provides an evaluation of a result or response, this flag identifies the record that is considered, by an independent assessor, to be the accepted evaluation. Expected to be "Y" or null.

### MSLLOQ
- **Order:** 44
- **Label:** Lower Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates the lower limit of quantitation for an assay. Units will be those used for MSSTRESU.

### MSULOQ
- **Order:** 45
- **Label:** Upper Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates the upper limit of quantitation for an assay. Units will be those used for MSSTRESU.

### MSREPNUM
- **Order:** 46
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.

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
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 49
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 50
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the specimen was collected.

### EPOCH
- **Order:** 51
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the specimen was collected.

### MSDTC
- **Order:** 52
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of an observation.

### MSDY
- **Order:** 53
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### MSDUR
- **Order:** 54
- **Label:** Duration
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of an event, intervention, or finding. Used only if collected on the CRF and not derived.

### MSTPT
- **Order:** 55
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See MSTPTNUM and MSTPTREF.

### MSTPTNUM
- **Order:** 56
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### MSELTM
- **Order:** 57
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to a planned fixed reference (MSTPTREF; e.g., previous dose, previous meal). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### MSTPTREF
- **Order:** 58
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by MSELTM, MSTPTNUM, and MSTPT. Example: "PREVIOUS DOSE".

### MSRFTDTC
- **Order:** 59
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by MSTPTREF.

### MSEVLINT
- **Order:** 60
- **Label:** Evaluation Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Duration of interval associated with an observation such as a finding MSTESTCD. Example: "-P2M" to represent a period of the past 2 months before the assessment.

### MSEVINTX
- **Order:** 61
- **Label:** Evaluation Interval Text
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS".
---

## Cross References

### Controlled Terminology
- [Microbiology Susceptibility Test Name (C128687)](../../terminology/core/microbiology_part1.md) — MSTEST
- [Microbiology Susceptibility Test Code (C128688)](../../terminology/core/microbiology_part1.md) — MSTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — MSLOBXFL, MSBLFL, MSFAST, MSDRVFL, MSACPTFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — MSSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — MSCONCU, MSORRESU, MSSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — MSLOC
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — MSSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — MSSPEC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — MSEVAL
- [Reference Range Indicator (C78736)](../../terminology/core/general_part4.md) — MSNRIND
- [Method (C85492)](../../terminology/core/general_part3.md) — MSMETHOD
- [Microbiology Susceptibility Testing Result Category (C85495)](../../terminology/core/microbiology_part1.md) — MSRESCAT
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — MSEVALID
- [Laterality (C99073)](../../terminology/core/general_part2.md) — MSLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — MSDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Shared Dataset:** [MB](../MB/) — microbiology organism identification
- **Specimen:** [BS](../BS/) — susceptibility specimen data
- **Specimen Relationship:** [RELSPEC](../RELSPEC/) — specimen hierarchy

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)
