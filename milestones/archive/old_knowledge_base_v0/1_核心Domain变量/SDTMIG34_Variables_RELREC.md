# SDTM IG v3.4 Variables - RELREC Domain

**Domain Code:** `RELREC`

**Total Variables:** 7

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `RDOMAIN` | Related Domain Abbreviation | Char | Req | Identifier | Abbreviation for the domain of the parent record(s). |
| `USUBJID` | Unique Subject Identifier | Char | Exp | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `IDVAR` | Identifying Variable | Char | Req | Identifier | Name of the identifying variable in the general-observation-class dataset that identifies the related record(s). Examples: --SEQ, --GRPID. |
| `IDVARVAL` | Identifying Variable Value | Char | Exp | Identifier | Value of identifying variable described in IDVAR. If --SEQ is the variable being used to describe this record, then the value of --SEQ would be entered here. |
| `RELTYPE` | Relationship Type | Char | Exp | Record Qualifier | Identifies the hierarchical level of the records in the relationship. Values should be either "ONE" or "MANY". Used only when identifying a relationship between datasets (as described in Section 8.3, Relating Datasets). |
| `RELID` | Relationship Identifier | Char | Req | Record Qualifier | Unique value within USUBJID that identifies the relationship. All records for the same USUBJID that have the same RELID are considered related/associated. RELID can be any value the sponsor chooses, and is only meaningful within the RELREC dataset to identify the related/associated domain records. |
