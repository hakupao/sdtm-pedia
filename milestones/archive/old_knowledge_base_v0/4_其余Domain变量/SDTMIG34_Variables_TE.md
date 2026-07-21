# SDTM IG v3.4 Variables - TE Domain

**Domain Code:** `TE`

**Total Variables:** 7

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `ETCD` | Element Code | Char | Req | Topic | ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name. |
| `ELEMENT` | Description of Element | Char | Req | Synonym Qualifier | The name of the element. |
| `TESTRL` | Rule for Start of Element | Char | Req | Rule | Describes condition for beginning element. |
| `TEENRL` | Rule for End of Element | Char | Perm | Rule | Describes condition for ending element. Either TEENRL or TEDUR must be present for each element. |
| `TEDUR` | Planned Duration of Element | Char | Perm | Timing | Planned duration of element in ISO 8601 format. Used when the rule for ending the element is applied after a fixed duration. |
