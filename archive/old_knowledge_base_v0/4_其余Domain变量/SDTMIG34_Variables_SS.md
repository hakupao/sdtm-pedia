# SDTM IG v3.4 Variables - SS Domain

**Domain Code:** `SS`

**Total Variables:** 22

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SSSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `SSGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `SSSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page. |
| `SSTESTCD` | Status Short Name | Char | Req | Topic | Short name of the status assessment described in SSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SSTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "SURVSTAT". |
| `SSTEST` | Status Name | Char | Req | Synonym Qualifier | Verbatim name of the status assessment used to obtain the finding. The value in SSTEST cannot be longer than 40 characters. Example: "Survival Status". |
| `SSCAT` | Category for Assessment | Char | Perm | Grouping Qualifier | Used to categorize observations across subjects. |
| `SSSCAT` | Subcategory for Assessment | Char | Perm | Grouping Qualifier | A further categorization. |
| `SSORRES` | Result or Finding Original Result | Char | Exp | Result Qualifier | Result of the status assessment finding as originally received or collected. |
| `SSSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from SSORRES, in a standard format. |
| `SSSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate a status assessment was not done. Should be null if a result exists in SSORRES. |
| `SSREASND` | Reason Assessment Not Performed | Char | Perm | Record Qualifier | Describes why an assessment was not performed. Example: "Subject refused". Used in conjunction with SSSTAT when value is "NOT DONE". |
| `SSEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "CAREGIVER", "ADJUDICATION COMMITTEE", "FRIEND". |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the subject status assessment. |
| `SSDTC` | Date/Time of Assessment | Char | Exp | Timing | Date and time of the subject status assessment represented in ISO 8601 character format. |
| `SSDY` | Study Day of Assessment | Num | Perm | Timing | Study day of the subject status assessment, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
