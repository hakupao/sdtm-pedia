# SDTM IG v3.4 Variables - QS Domain

**Domain Code:** `QS`

**Total Variables:** 35

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `QSSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `QSGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `QSSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Question number on a questionnaire. |
| `QSTESTCD` | Question Short Name | Char | Req | Topic | Topic variable for QS. Short name for the value in QSTEST, which can be used as a column name when converting the dataset from a vertical format to a horizontal format. The value in QSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). QSTESTCD cannot contain characters other than letters, numbers, or underscores. \n Controlled terminology for QSTESTCD is published in separate codelists for each questionnaire. See https://www.cdisc.org/standards/semantics/terminology for values for QSTESTCD. Examples: "ADCCMD01", "BPR0103". |
| `QSTEST` | Question Name | Char | Req | Synonym Qualifier | Verbatim name of the question or group of questions used to obtain the measurement or finding. The value in QSTEST cannot be longer than 40 characters. \n Controlled terminology for QSTEST is published in separate codelists for each questionnaire. See https://www.cdisc.org/standards/semantics/terminology for values for QSTEST. Example: "BPR01 - Emotional Withdrawal". |
| `QSCAT` | Category of Question | Char | Req | Grouping Qualifier | Used to specify the questionnaire in which the question identified by QSTEST and QSTESTCD was included. Examples: "ADAS-COG", "MDS-UPDRS". |
| `QSSCAT` | Subcategory for Question | Char | Perm | Grouping Qualifier | A further categorization of the questions within the category. Examples: "MENTAL HEALTH" , "DEPRESSION", "WORD RECALL". |
| `QSORRES` | Finding in Original Units | Char | Exp | Result Qualifier | Finding as originally received or collected (e.g., "RARELY", "SOMETIMES"). When sponsors apply codelist to indicate that code values are statistically meaningful standardized scores (which are defined by sponsors or by valid methodologies, e.g., SF36 questionnaires), QSORRES will contain the decode format; QSSTRESC and QSSTRESN may contain the standardized code values or scores. |
| `QSORRESU` | Original Units | Char | Perm | Variable Qualifier | Original units in which the data were collected. The unit for QSORRES, such as minutes or seconds or the units associated with a visual analog scale. |
| `QSSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the finding for all questions or subscores copied or derived from QSORRES, in a standard format or standard units. QSSTRESC should store all findings in character format; if findings are numeric, they should also be stored in numeric format in QSSTRESN. If question scores are derived from the original finding, then the standard format is the score. Examples: "0", "1". \n When sponsors apply codelist to indicate the code values are statistically meaningful standardized scores (which are defined by sponsors or by valid methodologies, e.g., SF36 questionnaires), QSORRES will contain the decode format; QSSTRESC and QSSTRESN may contain the standardized code values or scores. |
| `QSSTRESN` | Numeric Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric findings in standard format; copied in numeric format from QSSTRESC. QSSTRESN should store all numeric results or findings. |
| `QSSTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized unit used for QSSTRESC or QSSTRESN. |
| `QSSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a question was not done or was not answered. Should be null if a result exists in QSORRES. |
| `QSREASND` | Reason Not Performed | Char | Perm | Record Qualifier | Describes why a question was not answered. Used in conjunction with QSSTAT when value is "NOT DONE". Example: "SUBJECT REFUSED". |
| `QSMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the test or examination. |
| `QSLOBXFL` | Last Observation Before Exposure Flag | Char | Exp | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| `QSBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that QSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| `QSDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records or questionnaire subscores that do not come from the CRF are examples of records that would be derived for the submission datasets. If QSDRVFL = "Y", then QSORRES may be null with QSSTRESC and (if numeric) QSSTRESN having the derived value. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the observation date/time of the physical exam finding. |
| `QSDTC` | Date/Time of Finding | Char | Exp | Timing | Date of questionnaire. |
| `QSDY` | Study Day of Finding | Num | Perm | Timing | Study day of finding collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| `QSTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when questionnaire should be administered. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See QSTPTNUM and QSTPTREF. |
| `QSTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of QSTPT to aid in sorting. |
| `QSELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (QSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by QSTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by QSTPTREF. |
| `QSTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by QSELTM, QSTPTNUM, and QSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `QSRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time of the reference time point, QSTPTREF. |
| `QSEVLINT` | Evaluation Interval | Char | Perm | Timing | Evaluation interval associated with a QSTEST question represented in ISO 8601 character format. Example: "-P2Y" to represent an interval of 2 years in the question "Have you experienced any episodes in the past 2 years?". |
| `QSEVINTX` | Evaluation Interval Text | Char | Perm | Timing | Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS". |
