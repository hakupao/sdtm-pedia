# TA — Trial Arms

> Class: Trial Design | Structure: One record per planned Element per Arm

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

### ARMCD
- **Order:** 3
- **Label:** Planned Arm Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than that for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20.

### ARM
- **Order:** 4
- **Label:** Description of Planned Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Name given to an arm or treatment group.

### TAETORD
- **Order:** 5
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** Number that gives the order of the element within the arm.

### ETCD
- **Order:** 6
- **Label:** Element Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.

### ELEMENT
- **Order:** 7
- **Label:** Description of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** The name of the element. The same element may occur more than once within an arm.

### TABRANCH
- **Order:** 8
- **Label:** Branch
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Exp
- **CDISC Notes:** Condition subject met, at a "branch" in the trial design at the end of this element, to be included in this arm (e.g., "Randomization to DRUG X").

### TATRANS
- **Order:** 9
- **Label:** Transition Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Exp
- **CDISC Notes:** If the trial design allows a subject to transition to an element other than the next element in sequence, then the conditions for transitioning to those other elements, and the alternative element sequences, are specified in this rule (e.g., "Responders go to washout").

### EPOCH
- **Order:** 10
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** Name of the trial epoch with which this element of the arm is associated.
---

## Cross References

### Controlled Terminology
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Trial Design):** TD, TE, TI, TM, TS, TV
- **Trial Design:** [TE](../TE/) — arms use elements
- **Trial Design:** [TV](../TV/) — arms define visit schedules

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)
