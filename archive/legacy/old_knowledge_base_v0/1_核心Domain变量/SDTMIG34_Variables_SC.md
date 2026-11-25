# SDTM IG v3.4 Variables - SC Domain

**Domain Code:** `SC`

**Total Variables:** 24

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SCSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `SCGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `SCSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| `SCTESTCD` | Subject Characteristic Short Name | Char | Req | Topic | Short name of the measurement, test, or examination described in SCTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MARISTAT", "NATORIG". |
| `SCTEST` | Subject Characteristic | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in SCTEST cannot be longer than 40 characters. Examples: "Marital Status", "National Origin". |
| `SCCAT` | Category for Subject Characteristic | Char | Perm | Grouping Qualifier | Used to define a category of related records. |
| `SCSCAT` | Subcategory for Subject Characteristic | Char | Perm | Grouping Qualifier | A further categorization of the subject characteristic. |
| `SCORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the subject characteristic as originally received or collected. |
| `SCORRESU` | Original Units | Char | Perm | Variable Qualifier | Original unit in which the data were collected. The unit for SCORRES. |
| `SCSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from SCORRES, in a standard format or standard units. SCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in SCORRES, and these results effectively have the same meaning, they could be represented in standard format in SCSTRESC as "NEGATIVE". |
| `SCSTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from SCSTRESC. SCSTRESN should store all numeric test results or findings. |
| `SCSTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized unit used for SCSTRESC or SCSTRESN. |
| `SCSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that the measurement was not done. Should be null if a result exists in SCORRES. |
| `SCREASND` | Reason Not Performed | Char | Perm | Record Qualifier | Describes why the observation has no result. Example: "Subject refused". Used in conjunction with SCSTAT when value is "NOT DONE". |
| `VISITNUM` | Visit Number | Num | Perm | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time at which the assessment was made. |
| `SCDTC` | Date/Time of Collection | Char | Perm | Timing | Collection date and time of the subject characteristic represented in ISO 8601 character format. |
| `SCDY` | Study Day of Examination | Num | Perm | Timing | Study day of collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
