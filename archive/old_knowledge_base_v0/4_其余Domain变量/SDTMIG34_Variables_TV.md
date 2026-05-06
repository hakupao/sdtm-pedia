# SDTM IG v3.4 Variables - TV Domain

**Domain Code:** `TV`

**Total Variables:** 9

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `VISITNUM` | Visit Number | Num | Req | Topic | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Req | Synonym Qualifier | Description of clinical encounter. This is often defined in the protocol. Used in addition to VISITNUM and/or VISITDY as a text description of the clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Due to its sequential nature, used for sorting. |
| `ARMCD` | Planned Arm Code | Char | Exp | Record Qualifier | 1. ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. \n 2. If the timing of visits for a trial does not depend on which arm a subject is in, then ARMCD should be null. |
| `ARM` | Description of Planned Arm | Char | Perm | Synonym Qualifier | 1. Name given to an arm or treatment group. \n 2. If the timing of visits for a trial does not depend on which arm a subject is in, then Arm should be left blank. |
| `TVSTRL` | Visit Start Rule | Char | Req | Rule | Rule describing when the visit starts, in relation to the sequence of elements. |
| `TVENRL` | Visit End Rule | Char | Perm | Rule | Rule describing when the visit ends, in relation to the sequence of elements. |
