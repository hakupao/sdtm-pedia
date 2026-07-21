# SDTM IG v3.4 Variables - SV Domain

**Domain Code:** `SV`

**Total Variables:** 16

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain most relevant to the observation. The domain abbreviation is also used as a prefix for variables to ensure uniqueness when datasets are merged. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `VISITNUM` | Visit Number | Num | Req | Topic | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Synonym Qualifier | Protocol-defined description of a clinical encounter. |
| `SVPRESP` | Pre-specified | Char | Exp | Variable Qualifier | Used to indicate whether the visit was planned (i.e., visits specified in the TV domain). Value is "Y" for planned visits, null for unplanned visits. |
| `SVOCCUR` | Occurrence | Char | Exp | Record Qualifier | Used to record whether a planned visit occurred. The value is null for unplanned visits. |
| `SVREASOC` | Reason for Occur Value | Char | Perm | Record Qualifier | The reason for the value in SVOCCUR. If SVOCCUR="N", SVREASOC is the reason the visit did not occur. |
| `SVCNTMOD` | Contact Mode | Char | Perm | Record Qualifier | The way in which the visit was conducted. Examples: "IN PERSON", "TELEPHONE CALL", "IVRS". |
| `SVEPCHGI` | Epi/Pandemic Related Change Indicator | Char | Perm | Record Qualifier | Indicates whether the visit was changed due to an epidemic or pandemic. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `SVSTDTC` | Start Date/Time of Observation | Char | Exp | Timing | Start date/time of an observation represented in IS0 8601 character format. |
| `SVENDTC` | End Date/Time of Observation | Char | Exp | Timing | End date/time of the observation represented in IS0 8601 character format. |
| `SVSTDY` | Study Day of Start of Observation | Num | Perm | Timing | Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `SVENDY` | Study Day of End of Observation | Num | Perm | Timing | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `SVUPDES` | Description of Unplanned Visit | Char | Perm | Record Qualifier | Description of what happened to the subject during an unplanned visit. Only populated for unplanned visits. |
