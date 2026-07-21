# SDTM IG v3.4 Variables - PC Domain

**Domain Code:** `PC`

**Total Variables:** 41

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `PCSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `PCGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain to support relationships within the domain and between domains. |
| `PCREFID` | Reference ID | Char | Perm | Identifier | Internal or external specimen identifier. |
| `PCSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. |
| `PCTESTCD` | Pharmacokinetic Test Short Name | Char | Req | Topic | Short name of the analyte or specimen characteristic. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "ASA", "VOL", "SPG". |
| `PCTEST` | Pharmacokinetic Test Name | Char | Req | Synonym Qualifier | Name of the analyte or specimen characteristic. Note any test normally performed by a clinical laboratory is considered a lab test. The value in PCTEST cannot be longer than 40 characters. Examples: "Acetylsalicylic Acid", "Volume", "Specific Gravity". |
| `PCCAT` | Test Category | Char | Perm | Grouping Qualifier | Used to define a category of related records. Examples: "ANALYTE", "SPECIMEN PROPERTY". |
| `PCSCAT` | Test Subcategory | Char | Perm | Grouping Qualifier | A further categorization of a test category. |
| `PCORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the measurement or finding as originally received or collected. |
| `PCORRESU` | Original Units | Char | Exp | Variable Qualifier | Original units in which the data were collected. The unit for PCORRES. Example: "mg/L". |
| `PCSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings, copied or derived from PCORRES in a standard format or standard units. PCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in PCORRES, and these results effectively have the same meaning, they could be represented in standard format in PCSTRESC as "NEGATIVE". For other examples, see general assumptions. |
| `PCSTRESN` | Numeric Result/Finding in Standard Units | Num | Exp | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from PCSTRESC. PCSTRESN should store all numeric test results or findings. |
| `PCSTRESU` | Standard Units | Char | Exp | Variable Qualifier | Standardized unit used for PCSTRESC and PCSTRESN. |
| `PCSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate a result was not obtained. Should be null if a result exists in PCORRES. |
| `PCREASND` | Reason Test Not Done | Char | Perm | Record Qualifier | Describes why a result was not obtained, such as "SPECIMEN LOST". Used in conjunction with PCSTAT when value is "NOT DONE". |
| `PCNAM` | Vendor Name | Char | Exp | Record Qualifier | Name or identifier of the laboratory or vendor who provides the test results. |
| `PCSPEC` | Specimen Material Type | Char | Exp | Record Qualifier | Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE". |
| `PCSPCCND` | Specimen Condition | Char | Perm | Record Qualifier | Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC". |
| `PCMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the test or examination. Examples: "HPLC/MS", "ELISA". This should contain sufficient information and granularity to allow differentiation of various methods that might have been used within a study. |
| `PCFAST` | Fasting Status | Char | Perm | Record Qualifier | Indicator used to identify fasting status. |
| `PCDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, which do not come from the CRF, are examples of records that would be derived for the submission datasets. If PCDRVFL = "Y", then PCORRES may be null with PCSTRESC, and PCSTRESN (if the result is numeric) having the derived value. |
| `PCLLOQ` | Lower Limit of Quantitation | Num | Exp | Variable Qualifier | Indicates the lower limit of quantitation for an assay. Units should be those used in PCSTRESU. |
| `PCULOQ` | Upper Limit of Quantitation | Num | Perm | Variable Qualifier | Indicates the upper limit of quantitation for an assay. Units should be those used in PCSTRESU. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| `PCDTC` | Date/Time of Specimen Collection | Char | Exp | Timing | Date/time of specimen collection represented in ISO 8601 character format. If there is no end time, then this will be the collection time. |
| `PCENDTC` | End Date/Time of Specimen Collection | Char | Perm | Timing | End date/time of specimen collection represented in ISO 8601 character format. If there is no end time, the collection time should be stored in PCDTC, and PCENDTC should be null. |
| `PCDY` | Actual Study Day of Specimen Collection | Num | Perm | Timing | Study day of specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| `PCENDY` | Study Day of End of Observation | Num | Perm | Timing | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `PCTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See PCTPTNUM and PCTPTREF. Examples: "Start", "5 min post". |
| `PCTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of PCTPT to aid in sorting. |
| `PCELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (PCTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. |
| `PCTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point used as a basis for PCTPT, PCTPTNUM, and PCELTM. Example: "MOST RECENT DOSE". |
| `PCRFTDTC` | Date/Time of Reference Point | Char | Perm | Timing | Date/time of the reference time point described by PCTPTREF. |
| `PCEVLINT` | Evaluation Interval | Char | Perm | Timing | Evaluation Interval associated with a PCTEST record represented in ISO 8601 character format. Example: "-PT2H" to represent an evaluation interval of 2 hours prior to a PCTPT. |
