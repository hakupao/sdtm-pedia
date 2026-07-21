# SDTM IG v3.4 Variables - RELSUB Domain

**Domain Code:** `RELSUB`

**Total Variables:** 5

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `USUBJID` | Unique Subject Identifier | Char | Exp | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. Either USUBJID or POOLID must be populated. |
| `POOLID` | Pool Identifier | Char | Perm | Identifier | Identifier used to identify a pool of subjects. If POOLID is entered, POOLDEF records must exist for each subject in the pool and USUBJID must be null. Either USUBJID or POOLID must be populated. |
| `RSUBJID` | Related Subject or Pool Identifier | Char | Req | Identifier | Identifier used to identify a related subject or pool of subjects. RSUBJID will be populated with either the USUBJID of the related subject or the POOLID of the related pool. |
| `SREL` | Subject Relationship | Char | Req | Record Qualifier | Describes the relationship of the subject identified in USUBJID or the pool identified in POOLID to the subject or pool identified in RSUBJID. |
