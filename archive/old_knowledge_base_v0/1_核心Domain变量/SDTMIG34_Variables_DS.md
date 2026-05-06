# SDTM IG v3.4 Variables - DS Domain

**Domain Code:** `DS`

**Total Variables:** 16

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `DSSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `DSGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `DSREFID` | Reference ID | Char | Perm | Identifier | Internal or external identifier. |
| `DSSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Disposition page. |
| `DSTERM` | Reported Term for the Disposition Event | Char | Req | Topic | Verbatim name of the event or protocol milestone. Some terms in DSTERM will match DSDECOD, but others, such as "Subject moved", will map to controlled terminology in DSDECOD, such as "LOST TO FOLLOW-UP". |
| `DSDECOD` | Standardized Disposition Term | Char | Req | Synonym Qualifier | Controlled terminology for the name of disposition event or protocol milestone. Examples of protocol milestones: "INFORMED CONSENT OBTAINED", "RANDOMIZED". There are separate codelists used for DSDECOD where the choice depends on the value of DSCAT. Codelist "NCOMPLT" is used for disposition events, codelist "PROTMLST" is used for protocol milestones, and codelist "OTHEVENT" is used for other events. |
| `DSCAT` | Category for Disposition Event | Char | Exp | Grouping Qualifier | Used to define a category of related records. |
| `DSSCAT` | Subcategory for Disposition Event | Char | Perm | Grouping Qualifier | A further categorization of DSCAT (e.g., "STUDY PARTICIPATION", "STUDY TREATMENT" when DSCAT = "DISPOSITION EVENT"). The variable may be subject to controlled terminology for other categories of disposition event records. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the event. |
| `DSDTC` | Date/Time of Collection | Char | Perm | Timing | Collection date and time of the disposition observation represented in ISO 8601 character format. |
| `DSSTDTC` | Start Date/Time of Disposition Event | Char | Exp | Timing | Start date/time of the disposition event in ISO 8601 character format. |
| `DSDY` | Study Day of Collection | Num | Perm | Timing | Study day of collection of event relative to the sponsor-defined RFSTDTC. |
| `DSSTDY` | Study Day of Start of Disposition Event | Num | Exp | Timing | Study day of start of event relative to the sponsor-defined RFSTDTC. |
