# SDTM IG v3.4 Variables - VS Domain

**Domain Code:** `VS`

**Total Variables:** 38

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `VSSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `VSGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `VSSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| `VSTESTCD` | Vital Signs Test Short Name | Char | Req | Topic | Short name of the measurement, test, or examination described in VSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in VSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). VSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SYSBP", "DIABP", "BMI". |
| `VSTEST` | Vital Signs Test Name | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in VSTEST cannot be longer than 40 characters. Examples: "Systolic Blood Pressure", "Diastolic Blood Pressure", "Body Mass Index". |
| `VSCAT` | Category for Vital Signs | Char | Perm | Grouping Qualifier | Used to define a category of related records. |
| `VSSCAT` | Subcategory for Vital Signs | Char | Perm | Grouping Qualifier | A further categorization of a measurement or examination. |
| `VSPOS` | Vital Signs Position of Subject | Char | Perm | Record Qualifier | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| `VSORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the vital signs measurement as originally received or collected. |
| `VSORRESU` | Original Units | Char | Exp | Variable Qualifier | Original units in which the data were collected. The unit for VSORRES. Examples: "in", "LB", "beats/min". |
| `VSSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings, copied or derived from VSORRES in a standard format or standard units. VSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in VSSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in VSORRES, and these results effectively have the same meaning, they could be represented in standard format in VSSTRESC as "NEGATIVE". |
| `VSSTRESN` | Numeric Result/Finding in Standard Units | Num | Exp | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from VSSTRESC. VSSTRESN should store all numeric test results or findings. |
| `VSSTRESU` | Standard Units | Char | Exp | Variable Qualifier | Standardized unit used for VSSTRESC and VSSTRESN. |
| `VSSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a vital sign measurement was not done. Should be null if a result exists in VSORRES. |
| `VSREASND` | Reason Not Performed | Char | Perm | Record Qualifier | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with VSSTAT when value is "NOT DONE". |
| `VSLOC` | Location of Vital Signs Measurement | Char | Perm | Record Qualifier | Location relevant to the collection of vital signs measurement. Example: "ARM" for blood pressure. |
| `VSLAT` | Laterality | Char | Perm | Result Qualifier | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| `VSLOBXFL` | Last Observation Before Exposure Flag | Char | Exp | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null. |
| `VSBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that VSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| `VSDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records or that do not come from the CRF are examples of records that would be derived for the submission datasets. If VSDRVFL = "Y," then VSORRES may be null, with VSSTRESC and (if numeric) VSSTRESN having the derived value. |
| `VSTOX` | Toxicity | Char | Perm | Variable Qualifier | Description of toxicity quantified by VSTOXGR. The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document. |
| `VSTOXGR` | Standard Toxicity Grade | Char | Perm | Record Qualifier | Records toxicity grade value using a standard toxicity scale (e.g., NCI CTCAE). If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2"). The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document. |
| `VSCLSIG` | Clinically Significant, Collected | Char | Perm | Record Qualifier | Used to indicate whether a collected observation is clinically significant based on judgment. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time at which the assessment was made. |
| `VSDTC` | Date/Time of Measurements | Char | Exp | Timing | Date and time of the vital signs assessment represented in ISO 8601 character format. |
| `VSDY` | Study Day of Vital Signs | Num | Perm | Timing | Study day of vital signs measurements, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| `VSTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See VSTPTNUM and VSTPTREF. Examples: "START", "5 MIN POST". |
| `VSTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of VSTPT to aid in sorting. |
| `VSELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (VSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 Duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by VSTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by VSTPTREF. |
| `VSTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by VSELTM, VSTPTNUM, and VSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `VSRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time of the reference time point, VSTPTREF. |
