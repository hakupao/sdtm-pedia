# SDTM IG v3.4 Variables - SE Domain

**Domain Code:** `SE`

**Total Variables:** 13

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SESEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. Should be assigned to be consistent chronological order. |
| `ETCD` | Element Code | Char | Req | Topic | 1. ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name. \n 2. If an encountered element differs from the planned element to the point that it is considered a new element, then use "UNPLAN" as the value for ETCD to represent this element. |
| `ELEMENT` | Description of Element | Char | Perm | Synonym Qualifier | The name of the element. If ETCD has a value of "UNPLAN", then ELEMENT should be null. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the subject's assigned trial arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the element in the planned sequence of elements for the arm to which the subject was assigned. |
| `SESTDTC` | Start Date/Time of Element | Char | Req | Timing | Start date/time for an element for each subject. |
| `SEENDTC` | End Date/Time of Element | Char | Exp | Timing | End date/time for an element for each subject. |
| `SESTDY` | Study Day of Start of Element | Num | Perm | Timing | Study day of start of element relative to the sponsor-defined RFSTDTC. |
| `SEENDY` | Study Day of End of Element | Num | Perm | Timing | Study day of end of element relative to the sponsor-defined RFSTDTC. |
| `SEUPDES` | Description of Unplanned Element | Char | Perm | Synonym Qualifier | Description of what happened to the subject during an unplanned element. Used only if ETCD has the value of "UNPLAN". |
