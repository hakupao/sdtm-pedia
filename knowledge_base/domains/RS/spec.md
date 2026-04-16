# RS — Disease Response and Clin Classification

> Class: Findings | Structure: One record per response assessment or clinical classification assessment per time point per visit per subject per assessor per medical evaluator

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

### RSSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number.

### RSGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain.

### RSREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier.

### RSSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### RSLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** An identifier used to link the response assessment to the related measurement record in another domain which was used to determine the response result. LNKID values group records within USUBJID.

### RSLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** A grouping identifier used to link the response assessment to a group of measurement/assessment records which were used in the assessment of the response. LNKGRP values group records within USUBJID.

### RSTESTCD
- **Order:** 10
- **Label:** Assessment Short Name
- **Type:** Char
- **Controlled Terms:** C96782
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the TEST in RSTEST. The value in RSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). RSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TRGRESP", "NTRGRESP", "OVRLRESP", "SYMPTDTR", "CPS0102".  There are separate codelists used for RSTESTCD where the choice depends on the value of RSCAT. Codelist "ONCRTSCD" is used for oncology response criteria (when RSCAT is a term in codelist "ONCRSCAT"). Examples: TRGRESP, "NTRGRESP, "OVRLRESP". For Clinical Classifications (when RSCAT is a term in codelist "CCCAT"), QRS Naming Rules apply. These instruments have individual dedicated terminology codelists.

### RSTEST
- **Order:** 11
- **Label:** Assessment Name
- **Type:** Char
- **Controlled Terms:** C96781
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the response assessment. The value in RSTEST cannot be longer than 40 characters.  There are separate codelists used for RSTEST where the choice depends on the value of RSCAT. Codelist "ONCRTS" is used for oncology response criteria (when RSCAT is a term in codelist "ONCRSCAT"). Examples: "Target Response", "Non-target Response", "Overall Response", "Symptomatic Deterioration". For Clinical Classifications (when RSCAT is a term in codelist "CCCAT"), QRS Naming Rules apply. These instruments have individual dedicated terminology codelists.

### RSCAT
- **Order:** 12
- **Label:** Category for Assessment
- **Type:** Char
- **Controlled Terms:** C124298; C118971
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of related records across subjects. Examples: "RECIST 1.1", "CHILD-PUGH CLASSIFICATION". There are separate codelists used for RSCAT where the choice depends on whether the related records are about an oncology response criterion or another clinical classification.  RSCAT is required for clinical classifications other than oncology response criteria.

### RSSCAT
- **Order:** 13
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of RSCAT values.

### RSORRES
- **Order:** 14
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the response assessment as originally received, collected, or calculated.

### RSORRESU
- **Order:** 15
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for RSORRES.

### RSSTRESC
- **Order:** 16
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C96785
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for the response assessment, copied, or derived from RSORRES in a standard format or standard units. RSSTRESC should store all results or findings in character format.  For Clinical Classifications, this may be a score.

### RSSTRESN
- **Order:** 17
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from --STRESC. --STRESN should store all numeric test results or findings. For Clinical Classifications, this may be a score.

### RSSTRESU
- **Order:** 18
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for RSSTRESC and RSSTRESN.

### RSSTAT
- **Order:** 19
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the response assessment was not performed. Should be null if a result exists in RSORRES.

### RSREASND
- **Order:** 20
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a response assessment was not performed. Examples: "All target tumors not evaluated", "Subject does not have non-target tumors". Used in conjunction with RSSTAT when value is "NOT DONE".

### RSNAM
- **Order:** 21
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the vendor that performed the response assessment. This column can be left null when the investigator provides the complete set of data in the domain.

### RSMETHOD
- **Order:** 22
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C158113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination.

### RSLOBXFL
- **Order:** 23
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.  When a clinical classification is assessed at multiple times, including baseline, RSLOBXFL should be included in the dataset.

### RSBLFL
- **Order:** 24
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that --BLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### RSDRVFL
- **Order:** 25
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### RSEVAL
- **Order:** 26
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".  RSEVAL is expected for oncology response criteria. It can be left null when the investigator provides the complete set of data in the domain. However, the column should contain no null values when data from one or more independent assessors is included, meaning that the rows attributed to the investigator should contain a value of "INVESTIGATOR".

### RSEVALID
- **Order:** 27
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in RSEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumptions in Section 6.3.9.3.1, Disease Response Use Case.

### RSACPTFL
- **Order:** 28
- **Label:** Accepted Record Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provides an evaluation of response, this flag identifies the record that is considered to be the accepted evaluation.

### VISITNUM
- **Order:** 29
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 30
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 31
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 32
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 33
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### RSDTC
- **Order:** 34
- **Label:** Date/Time of Assessment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of the assessment represented in ISO 8601 character format.

### RSDY
- **Order:** 35
- **Label:** Study Day of Assessment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the assessment, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### RSTPT
- **Order:** 36
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See RSTPTNUM and RSTPTREF.

### RSTPTNUM
- **Order:** 37
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### RSELTM
- **Order:** 38
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time in ISO 8601 character format relative to a planned fixed reference (RSTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### RSTPTREF
- **Order:** 39
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by RSELTM, RSTPTNUM, and RSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### RSRFTDTC
- **Order:** 40
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by RSTPTREF in ISO 8601 character format.

### RSEVLINT
- **Order:** 41
- **Label:** Evaluation Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Duration of interval associated with an observation such as a finding RSTESTCD, represented in ISO 8601 character format. Example: "-P2M" to represent a period of the past 2 months as the evaluation interval.

### RSEVINTX
- **Order:** 42
- **Label:** Evaluation Interval Text
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS".

### RSSTRTPT
- **Order:** 43
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable RSSTTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### RSSTTPT
- **Order:** 44
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by RSSTRTPT. Examples: "2003-12-15", "VISIT 1".

### RSENRTPT
- **Order:** 45
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable RSENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### RSENTPT
- **Order:** 46
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by RSENRTPT. Examples: "2003-12-25", "VISIT 2".
---

## Cross References

### Controlled Terminology
- [Category of Clinical Classification (C118971)](../../terminology/core/oncology_part1.md) — RSCAT
- [Category of Oncology Response Assessment (C124298)](../../terminology/core/oncology_part1.md) — RSCAT
- [QRS Method (C158113)](../../terminology/core/general_part4.md) — RSMETHOD
- [Relation to Reference Period (C66728)](../../terminology/core/general_part4.md) — RSSTRTPT, RSENRTPT
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — RSLOBXFL, RSBLFL, RSDRVFL, RSACPTFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — RSSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — RSORRESU, RSSTRESU
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — RSEVAL
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — RSEVALID
- [Oncology Response Assessment Test Name (C96781)](../../terminology/core/oncology_part2.md) — RSTEST
- [Oncology Response Assessment Test Code (C96782)](../../terminology/core/oncology_part1.md) — RSTESTCD
- [Oncology Response Assessment Result (C96785)](../../terminology/core/oncology_part1.md) — RSSTRESC
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, SC, SS, TR, TU, UR, VS
- **Related Findings:** [TR](../TR/) — disease response ← tumor results
- **Related Findings:** [TU](../TU/) — disease response ← tumor identification

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)
