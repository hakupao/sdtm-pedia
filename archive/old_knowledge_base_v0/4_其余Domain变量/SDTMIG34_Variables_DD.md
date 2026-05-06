# SDTM IG v3.4 Variables - DD Domain

**Domain Code:** `DD`

**Total Variables:** 12

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `DDSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `DDTESTCD` | Death Detail Assessment Short Name | Char | Req | Topic | Short name of the measurement, test, or examination described in DDTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in DDTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). DDTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRCDTH", "SECDTH". |
| `DDTEST` | Death Detail Assessment Name | Char | Req | Synonym Qualifier | Long name for DDTESTCD. The value in DDTEST cannot be longer than 40 characters. Examples: "Primary Cause of Death", "Secondary Cause of Death". |
| `DDORRES` | Result or Finding as Collected | Char | Exp | Result Qualifier | Result of the test defined in DDTEST, as originally received or collected. |
| `DDSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result or finding copied or derived from DDORRES in a standard format. |
| `DDRESCAT` | Result Category | Char | Perm | Variable Qualifier | Used to categorize the result of a finding. Examples: "TREATMENT RELATED", "NONTREATMENT RELATED", "UNDETERMINED", "ACCIDENTAL". |
| `DDEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. |
| `DDDTC` | Date/Time of Collection | Char | Exp | Timing | Date/time of collection of the diagnosis or other death assessment data in ISO 8601 format. This is not necessarily the date of death. |
| `DDDY` | Study Day of Collection | Num | Perm | Timing | Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |
