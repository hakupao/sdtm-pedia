# SDTM IG v3.4 Variables - IE Domain

**Domain Code:** `IE`

**Total Variables:** 18

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `IESEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `IESPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Inclusion or exclusion criteria number from CRF. |
| `IETESTCD` | Inclusion/Exclusion Criterion Short Name | Char | Req | Topic | Short name of the criterion described in IETEST. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "IN01", "EX01". |
| `IETEST` | Inclusion/Exclusion Criterion | Char | Req | Synonym Qualifier | Verbatim description of the inclusion or exclusion criterion that was the exception for the subject within the study. IETEST cannot be longer than 200 characters. |
| `IECAT` | Inclusion/Exclusion Category | Char | Req | Grouping Qualifier | Used to define a category of related records across subjects. |
| `IESCAT` | Inclusion/Exclusion Subcategory | Char | Perm | Grouping Qualifier | A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or for to categorize as a major or minor exceptions. Examples: "MAJOR", "MINOR". |
| `IEORRES` | I/E Criterion Original Result | Char | Req | Result Qualifier | Original response to inclusion/exclusion criterion question, i.e., whether the inclusion or exclusion criterion was met. |
| `IESTRESC` | I/E Criterion Result in Std Format | Char | Req | Result Qualifier | Response to inclusion/exclusion criterion result, in standard format. |
| `VISITNUM` | Visit Number | Num | Perm | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the observation date/time of the inclusion/exclusion finding. |
| `IEDTC` | Date/Time of Collection | Char | Perm | Timing | Collection date and time of the inclusion/exclusion criterion represented in ISO 8601 character format. |
| `IEDY` | Study Day of Collection | Num | Perm | Timing | Study day of collection of the inclusion/exclusion exceptions, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
