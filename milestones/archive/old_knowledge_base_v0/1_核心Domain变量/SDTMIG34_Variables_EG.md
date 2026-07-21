# SDTM IG v3.4 Variables - EG Domain

**Domain Code:** `EG`

**Total Variables:** 44

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SPDEVID` | Sponsor Device Identifier | Char | Perm | Identifier | Sponsor-defined identifier for a device. |
| `EGSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `EGGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `EGREFID` | ECG Reference ID | Char | Perm | Identifier | Internal or external ECG identifier. Example: "334PT89". |
| `EGSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the ECG page. |
| `EGBEATNO` | ECG Beat Number | Num | Perm | Identifier | A sequence number that identifies the beat within an ECG. |
| `EGTESTCD` | ECG Test or Examination Short Name | Char | Req | Topic | Short name of the measurement, test, or examination described in EGTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in EGTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). EGTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRAG", "QRSAG". \n Test codes are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTESTCD) and one 1 tests based on Holter monitoring (HETESTCD). |
| `EGTEST` | ECG Test or Examination Name | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in EGTEST cannot be longer than 40 characters. Examples: "PR Interval, Aggregate", "QRS Duration, Aggregate". \n Test names are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTEST) and 1 for tests based on Holter monitoring (HETEST). |
| `EGCAT` | Category for ECG | Char | Perm | Grouping Qualifier | Used to categorize ECG observations across subjects. Examples: "MEASUREMENT", "FINDING", "INTERVAL". |
| `EGSCAT` | Subcategory for ECG | Char | Perm | Grouping Qualifier | A further categorization of the ECG. |
| `EGPOS` | ECG Position of Subject | Char | Perm | Record Qualifier | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| `EGORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the ECG measurement or finding as originally received or collected. Examples of expected values are "62" or "0.151" when the result is an interval or measurement, or "ATRIAL FIBRILLATION" or "QT PROLONGATION" when the result is a finding. |
| `EGORRESU` | Original Units | Char | Perm | Variable Qualifier | Original units in which the data were collected. The unit for EGORRES. Examples: "sec", "msec". |
| `EGSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from EGORRES, in a standard format or standard units. EGSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in EGSTRESN. For example, if a test has results of 62 beats/min, then EGORRES = "62", EGORRESU = "beats/min", EGSTRESC = "62", EGSTRESN = 62, and EGSTRESU = "beats/min" . For other examples, see Original and Standardized Results. Additional examples of result data: "SINUS BRADYCARDIA", "ATRIAL FLUTTER", "ATRIAL FIBRILLATION". \n Test results are in 3 separate codelists: EGSTRESC for abnormal test results based on regular 10-second ECGs; HESTRESC for abnormal test results based on Holter monitoring, and NORMABNM for generic test results and/or responses to EGTEST = "Interpretation". |
| `EGSTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from EGSTRESC. EGSTRESN should store all numeric test results or findings. |
| `EGSTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized units used for EGSTRESC and EGSTRESN. |
| `EGSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate an ECG was not done, or an ECG measurement was not taken. Should be null if a result exists in EGORRES. |
| `EGREASND` | Reason ECG Not Done | Char | Perm | Record Qualifier | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with EGSTAT when value is "NOT DONE". |
| `EGXFN` | ECG External File Path | Char | Perm | Record Qualifier | File name and path for the external ECG waveform file. |
| `EGNAM` | Vendor Name | Char | Perm | Record Qualifier | Name or identifier of the laboratory or vendor providing the test results. |
| `EGMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the ECG test. Example: "12-LEAD STANDARD". |
| `EGLEAD` | Lead Location Used for Measurement | Char | Perm | Record Qualifier | The lead used for the measurement. Examples: "LEAD 1", "LEAD 2", "LEAD rV2", "LEAD V1". |
| `EGLOBXFL` | Last Observation Before Exposure Flag | Char | Exp | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `EGBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that EGBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| `EGDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If EGDRVFL="Y", then EGORRES could be null, with EGSTRESC and EGSTRESN (if the result is numeric) having the derived value. |
| `EGEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR". |
| `EGEVALID` | Evaluator Identifier | Char | Perm | Variable Qualifier | Used to distinguish multiple evaluators with the same role recorded in EGEVAL. Examples: "RADIOLOGIST 1" or "RADIOLOGIST 2". |
| `EGCLSIG` | Clinically Significant, Collected | Char | Perm | Record Qualifier | Used to indicate whether a collected observation is clinically significant based on judgment. |
| `EGREPNUM` | Repetition Number | Num | Perm | Record Qualifier | The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time at which the assessment was made. |
| `EGDTC` | Date/Time of ECG | Char | Exp | Timing | Date/Time of ECG. |
| `EGDY` | Study Day of ECG | Num | Perm | Timing | Study day of the ECG, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| `EGTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EGTPTNUM and EGTPTREF. Examples: "Start", "5 min post". |
| `EGTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of EGTPT to aid in sorting. |
| `EGELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time (in ISO 8601) relative to a fixed time point reference (EGTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by EGTPTREF. |
| `EGTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by EGELTM, EGTPTNUM, and EGTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `EGRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by EGTPTREF. |
