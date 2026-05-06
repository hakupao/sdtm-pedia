# SDTM IG v3.4 Variables - NV Domain

**Domain Code:** `NV`

**Total Variables:** 42

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `FOCID` | Focus of Study-Specific Interest | Char | Perm | Identifier | Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed, such as a drug application site (e.g., "Injection site 1", "Biopsy site 1", "Treated site 1") or a more specific focus (e.g., "OD" (right eye), "Upper left quadrant of the back"). The value in this variable should have inherent semantic meaning. |
| `NVSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `NVGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `NVREFID` | Reference ID | Char | Perm | Identifier | Internal or external procedure identifier. |
| `NVSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page. |
| `NVLNKID` | Link ID | Char | Perm | Identifier | Identifier used to link a procedure to the assessment results over the course of the study. |
| `NVLNKGRP` | Link Group | Char | Perm | Identifier | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| `NVTESTCD` | Short Name of Nervous System Test | Char | Req | Topic | Short name of the measurement, test, or examination described in NVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in NVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). NVTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SUVR", "N75LAT", "P100LAT","N145LAT". |
| `NVTEST` | Name of Nervous System Test | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in NVTEST cannot be longer than 40 characters. Examples: "Standard Uptake Value Ratio", "N75 Latency", "P100 Latency", "N145 Latency". |
| `NVCAT` | Category for Nervous System Test | Char | Perm | Grouping Qualifier | Used to define a category of topic-variable values. Example: "VISUAL EVOKED POTENTIAL". |
| `NVSCAT` | Subcategory for Nervous System Test | Char | Perm | Grouping Qualifier | Used to define a further categorization of NVCAT values. |
| `NVORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the procedure measurement or finding as originally received or collected. |
| `NVORRESU` | Original Units | Char | Perm | Variable Qualifier | Original units in which the data were collected. The unit for NVORRES. |
| `NVSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from NVORRES, in a standard format or standard units. NVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in NVSTRESN. |
| `NVSTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from NVSTRESC. NVSTRESN should store all numeric test results or findings. |
| `NVSTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized unit used for NVSTRESC or NVSTRESN. |
| `NVSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate a test was not done, or a measurement was not taken. Should be null if a result exists in NVORRES. |
| `NVREASND` | Reason Not Done | Char | Perm | Record Qualifier | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with NVSTAT when value is "NOT DONE". |
| `NVLOC` | Location Used for the Measurement | Char | Perm | Record Qualifier | Anatomical location of the subject relevant to the collection of the measurement. Examples: "BRAIN", "EYE", "PRECUNEUS", "CINGULATE CORTEX". |
| `NVLAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| `NVDIR` | Directionality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| `NVMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the test or examination. Examples: "EEG", "PET/CT SCAN ", "FDGPET". |
| `NVLOBXFL` | Last Observation Before Exposure Flag | Char | Perm | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `NVBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that NVBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| `NVDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| `NVEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| `NVEVALID` | Evaluator Identifier | Char | Perm | Variable Qualifier | Used to distinguish multiple evaluators with the same role recorded in NVEVAL. Examples: "RADIOLOGIST 1", "RADIOLOGIST 2". |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time at which the assessment was made. |
| `NVDTC` | Date/Time of Collection | Char | Exp | Timing | Date of procedure or test. |
| `NVDY` | Study Day of Visit/Collection/Exam | Num | Perm | Timing | Study day of the procedure or test, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. |
| `NVTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See NVTPTNUM and NVTPTREF. Examples: "START", "5 MIN POST". |
| `NVTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of NVTPT to aid in sorting. |
| `NVELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time (in ISO 8601) relative to a fixed time point reference (NVTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by NVTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by NVTPTREF. |
| `NVTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by NVELTM, NVTPTNUM, and NVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `NVRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by --TPTREF in ISO 8601 character format. |
