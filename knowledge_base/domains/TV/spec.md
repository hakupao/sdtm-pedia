# TV — Trial Visits

> Class: Trial Design | Structure: One record per planned Visit per Arm

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

### VISITNUM
- **Order:** 3
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 4
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Description of clinical encounter. This is often defined in the protocol. Used in addition to VISITNUM and/or VISITDY as a text description of the clinical encounter.

### VISITDY
- **Order:** 5
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Due to its sequential nature, used for sorting.

### ARMCD
- **Order:** 6
- **Label:** Planned Arm Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** 1. ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. \n 2. If the timing of visits for a trial does not depend on which arm a subject is in, then ARMCD should be null.

### ARM
- **Order:** 7
- **Label:** Description of Planned Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** 1. Name given to an arm or treatment group. \n 2. If the timing of visits for a trial does not depend on which arm a subject is in, then Arm should be left blank.

### TVSTRL
- **Order:** 8
- **Label:** Visit Start Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Req
- **CDISC Notes:** Rule describing when the visit starts, in relation to the sequence of elements.

### TVENRL
- **Order:** 9
- **Label:** Visit End Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Perm
- **CDISC Notes:** Rule describing when the visit ends, in relation to the sequence of elements.
