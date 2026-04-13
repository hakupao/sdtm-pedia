# TD — Trial Disease Assessments

> Class: Trial Design | Structure: One record per planned constant assessment period

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

### TDORDER
- **Order:** 3
- **Label:** Sequence of Planned Assessment Schedule
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** A number given to ensure ordinal sequencing of the planned assessment schedules within a trial.

### TDANCVAR
- **Order:** 4
- **Label:** Anchor Variable Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** A reference to the date variable name that provides the start point from which the planned disease assessment schedule is measured. This must be a referenced from the ADaM ADSL dataset (e.g., "ANCH1DT"). Note: TDANCVAR will contain the name of a reference date variable.

### TDSTOFF
- **Order:** 5
- **Label:** Offset from the Anchor
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** A fixed offset from the date provided by the variable referenced in TDANCVAR. This is used when the timing of planned cycles does not start on the exact day referenced in the variable indicated in TDANCVAR. The value of this variable will be either zero or a positive value and will be represented in ISO 8601 character format.

### TDTGTPAI
- **Order:** 6
- **Label:** Planned Assessment Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** The planned interval between disease assessments represented in ISO 8601 character format.

### TDMINPAI
- **Order:** 7
- **Label:** Planned Assessment Interval Minimum
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** The lower limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format.

### TDMAXPAI
- **Order:** 8
- **Label:** Planned Assessment Interval Maximum
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** The upper limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format.

### TDNUMRPT
- **Order:** 9
- **Label:** Maximum Number of Actual Assessments
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** This variable must represent the maximum number of actual assessments for the analysis that this disease assessment schedule describes. In a trial where the maximum number of assessments is not defined explicitly in the protocol (e.g., assessments occur until death), TDNUMRPT should represent the maximum number of disease assessments that support the efficacy analysis encountered by any subject across the trial at that point in time.
