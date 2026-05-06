# SDTM IG v3.4 Variables - FA Domain

**Domain Code:** `FA`

**Total Variables:** 30

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `FASEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `FAGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `FASPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF. |
| `FATESTCD` | Findings About Test Short Name | Char | Req | Topic | Short name of the measurement, test, or examination described in FATEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in FATESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FATESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SEV", "OCCUR". Note that controlled terminology is in a FATESTCD general codelist and in several therapeutic area-specific codelists. |
| `FATEST` | Findings About Test Name | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in FATEST cannot be longer than 40 characters. Examples: "Severity/Intensity", "Occurrence". Note that controlled terminology is in a FATEST general codelist and in several therapeutic area-specific codelists. |
| `FAOBJ` | Object of the Observation | Char | Req | Record Qualifier | Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the term (e.g., "Acne") describing a clinical sign or symptom that is being measured by a severity test; an event (e.g., "VOMIT, where the volume of vomit is being measured by a VOLUME test). |
| `FACAT` | Category for Findings About | Char | Perm | Grouping Qualifier | Used to define a category of related records. Examples: "GERD", "PRE-SPECIFIED AE". |
| `FASCAT` | Subcategory for Findings About | Char | Perm | Grouping Qualifier | A further categorization of FACAT. |
| `FAORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the test as originally received or collected. |
| `FAORRESU` | Original Units | Char | Perm | Variable Qualifier | Original units in which the data were collected. The unit for FAORRES. |
| `FASTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings, copied or derived from FAORRES in a standard format or standard units. FASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FASTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in FAORRES, and these results effectively have the same meaning; they could be represented in standard format in FASTRESC as "NEGATIVE". |
| `FASTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from FASTRESC. FASTRESN should store all numeric test results or findings. |
| `FASTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized unit used for FASTRESC and FASTRESN. |
| `FASTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that the measurement was not done. Should be null if a result exists in FAORRES. |
| `FAREASND` | Reason Not Performed | Char | Perm | Record Qualifier | Describes why a question was not answered. Example: "Subject refused". Used in conjunction with FASTAT when value is "NOT DONE". |
| `FALOC` | Location of the Finding About | Char | Perm | Record Qualifier | Used to specify the location of the clinical evaluation. Example: "ARM". |
| `FALAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| `FALOBXFL` | Last Observation Before Exposure Flag | Char | Perm | Record Qualifier | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `FABLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. The value should be "Y" or null. Note that FABLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| `FAEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR". |
| `VISITNUM` | Visit Number | Num | Exp | Timing | 1. Clinical encounter number. \n 2. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | 1. Protocol-defined description of clinical encounter. \n 2. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP". |
| `FADTC` | Date/Time of Collection | Char | Exp | Timing | Collection date and time of findings assessment represented in ISO 8601 character format. |
| `FADY` | Study Day of Collection | Num | Perm | Timing | 1. Study day of collection, measured as integer days. \n 2. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
