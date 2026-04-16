# ML — Meal Data

> Class: Interventions | Structure: One record per food product occurrence or constant intake interval per subject

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

### MLSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### MLGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### MLSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. Examples: a number preprinted on the CRF as an explicit line identifier, record identifier defined in the sponsor's operational database.

### MLTRT
- **Order:** 7
- **Label:** Name of Meal
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim food product name that is either preprinted or collected on a CRF.

### MLCAT
- **Order:** 8
- **Label:** Category for Meal
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of MLTRT values.

### MLSCAT
- **Order:** 9
- **Label:** Subcategory for Meal
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of MLCAT values.

### MLPRESP
- **Order:** 10
- **Label:** ML Pre-specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used when a specific meal is prespecified on a CRF. Values should be "Y" or null.

### MLOCCUR
- **Order:** 11
- **Label:** ML Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to record whether a prespecified meal occurred when information about the occurrence of a specific meal is solicited.

### MLSTAT
- **Order:** 12
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate when a question about the occurrence of a prespecified meal was not answered. Should be null or have a value of "NOT DONE".

### MLREASND
- **Order:** 13
- **Label:** Reason Meal Not Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason a response to a question about the occurrence of a meal was not collected. Used in conjunction with MLSTAT when value is "NOT DONE".

### MLDOSE
- **Order:** 14
- **Label:** Dose
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of MLTRT consumed. Not populated when MLDOSTXT is populated.

### MLDOSTXT
- **Order:** 15
- **Label:** Dose Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount description of MLTRT consumed, collected in text form. Not populated when MLDOSE is populated. Examples: "<1 per day", "200-400".

### MLDOSU
- **Order:** 16
- **Label:** Dose Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Units for MLDOSE, MLDOSTOT, or MLDOSTXT.

### MLDOSFRM
- **Order:** 17
- **Label:** Dose Form
- **Type:** Char
- **Controlled Terms:** C66726
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Dosage form for MLTRT. Example: "BAR, CHEWABLE".

### VISITNUM
- **Order:** 18
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 19
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 20
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 21
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the meal started.

### EPOCH
- **Order:** 22
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the meal.

### MLDTC
- **Order:** 23
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of the meal represented in ISO 8601 character format.

### MLSTDTC
- **Order:** 24
- **Label:** Start Date/Time of Meal
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Start date/time of the meal represented in ISO 8601 character format.

### MLENDTC
- **Order:** 25
- **Label:** End Date/Time of Meal
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the meal represented in ISO 8601 character format.

### MLDY
- **Order:** 26
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of the visit/collection expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### MLSTDY
- **Order:** 27
- **Label:** Study Day of Start of Meal
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of start of the meal expressed in integer days relative to sponsor-defined RFSTDTC in Demographics.

### MLENDY
- **Order:** 28
- **Label:** Study Day of End of Meal
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of the meal expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### MLDUR
- **Order:** 29
- **Label:** Duration of Meal
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of the meal represented in ISO 8601 character format. Used only if collected on the CRF and not derived.

### MLTPT
- **Order:** 30
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point. See MLTPTNUM and MLTPTREF.

### MLTPTNUM
- **Order:** 31
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### MLELTM
- **Order:** 32
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to the planned fixed reference (MLTPTREF). This variable is useful when there are repetitive measures. Not a clock time or a date/time variable. Represented as an ISO 8601 duration.

### MLTPTREF
- **Order:** 33
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by MLELTM, MLTPTNUM, and MLTPT.

### MLRFTDTC
- **Order:** 34
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by MLTPTREF in ISO 8601 character format.

### MIDS
- **Order:** 35
- **Label:** Disease Milestone Instance Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The name of a specific instance of a disease milestone type (MIDSTYPE) described in the Trial Disease Milestones dataset. This should be unique within a subject. Used only in conjunction with RELMIDS and MIDSDTC.

### RELMIDS
- **Order:** 36
- **Label:** Temporal Relation to Milestone Instance
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The temporal relationship of the observation to the disease milestone instance name in MIDS. Examples: "IMMEDIATELY BEFORE", "AT TIME OF", "AFTER".

### MIDSDTC
- **Order:** 37
- **Label:** Disease Milestone Instance Date/Time
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The start date/time of the disease milestone instance name in MIDS, in ISO 8601 format.
---

## Cross References

### Controlled Terminology
- [Pharmaceutical Dosage Form (C66726)](../../terminology/core/interventions.md) — MLDOSFRM
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — MLPRESP, MLOCCUR
- [Not Done (C66789)](../../terminology/core/general_part4.md) — MLSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — MLDOSU
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Interventions):** AG, CM, EC, EX, PR, SU

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Interventions class definition](../../model/02_observation_classes.md)
