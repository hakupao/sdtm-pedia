# SDTM IG v3.4 Variables - TA Domain

**Domain Code:** `TA`

**Total Variables:** 10

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `ARMCD` | Planned Arm Code | Char | Req | Topic | ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than that for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. |
| `ARM` | Description of Planned Arm | Char | Req | Synonym Qualifier | Name given to an arm or treatment group. |
| `TAETORD` | Planned Order of Element within Arm | Num | Req | Timing | Number that gives the order of the element within the arm. |
| `ETCD` | Element Code | Char | Req | Record Qualifier | ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name. |
| `ELEMENT` | Description of Element | Char | Perm | Synonym Qualifier | The name of the element. The same element may occur more than once within an arm. |
| `TABRANCH` | Branch | Char | Exp | Rule | Condition subject met, at a "branch" in the trial design at the end of this element, to be included in this arm (e.g., "Randomization to DRUG X"). |
| `TATRANS` | Transition Rule | Char | Exp | Rule | If the trial design allows a subject to transition to an element other than the next element in sequence, then the conditions for transitioning to those other elements, and the alternative element sequences, are specified in this rule (e.g., "Responders go to washout"). |
| `EPOCH` | Epoch | Char | Req | Timing | Name of the trial epoch with which this element of the arm is associated. |
