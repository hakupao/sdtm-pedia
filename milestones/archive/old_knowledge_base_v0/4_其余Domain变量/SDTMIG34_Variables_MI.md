# SDTM IG v3.4 Variables - MI Domain

**Domain Code:** `MI`

**Total Variables:** 37

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `MISEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `MIGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. This is not the treatment group number. |
| `MIREFID` | Reference ID | Char | Perm | Identifier | Internal or external specimen identifier. Example: specimen barcode number. |
| `MISPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: line number from the MI Findings page. |
| `MITESTCD` | Microscopic Examination Short Name | Char | Req | Topic | Short name of the measurement, test, or examination described in MITEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MITESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MITESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HER2", "BRCA1", "TTF1". |
| `MITEST` | Microscopic Examination Name | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in MITEST cannot be longer than 40 characters. Examples: "Human Epidermal Growth Factor Receptor 2", "Breast Cancer Susceptibility Gene 1", "Thyroid Transcription Factor 1". |
| `MITSTDTL` | Microscopic Examination Detail | Char | Perm | Record Qualifier | Further description of the test performed in producing the MI result. This would be used to represent specific attributes, such as intensity score or percentage of cells displaying presence of the biomarker or compound. |
| `MICAT` | Category for Microscopic Finding | Char | Perm | Grouping Qualifier | Used to define a category of related records. |
| `MISCAT` | Subcategory for Microscopic Finding | Char | Perm | Grouping Qualifier | Used to define a further categorization of MICAT. |
| `MIORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the histopathology measurement or finding as originally received or collected. |
| `MIORRESU` | Original Units | Char | Perm | Variable Qualifier | Original unit for MIORRES. |
| `MISTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings, copied or derived from MIORRES in a standard format or standard units. MISTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MISTRESN. |
| `MISTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from MISTRESC. MISTRESN should store all numeric test results or findings. |
| `MISTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized unit used for MISTRESC and MISTRESN. |
| `MIRESCAT` | Result Category | Char | Perm | Variable Qualifier | Used to categorize the result of a finding. Examples: "MALIGNANT" or "BENIGN" for tumor findings. |
| `MISTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate examination not done or result is missing. Should be null if a result exists in MIORRES or have a value of "NOT DONE" when MIORRES = "NULL". |
| `MIREASND` | Reason Not Done | Char | Perm | Record Qualifier | Reason not done. Used in conjunction with MISTAT when value is NOT DONE. Examples: "SAMPLE AUTOLYZED", "SPECIMEN LOST". |
| `MINAM` | Laboratory/Vendor Name | Char | Perm | Record Qualifier | Name or identifier of the vendor (e.g., laboratory) that provided the test results. |
| `MISPEC` | Specimen Material Type | Char | Req | Record Qualifier | Subject of the observation. Defines the type of specimen used for a measurement. Examples: "TISSUE", "BLOOD", "BONE MARROW". |
| `MISPCCND` | Specimen Condition | Char | Exp | Record Qualifier | Free or standardized text describing the condition of the specimen. Example: "AUTOLYZED". |
| `MILOC` | Specimen Collection Location | Char | Perm | Record Qualifier | Location relevant to the collection of the specimen. Examples: "LUNG", "KNEE JOINT", "ARM", "THIGH". |
| `MILAT` | Specimen Laterality within Subject | Char | Perm | Variable Qualifier | Qualifier for laterality of the location of the specimen in MILOC. Examples: "LEFT", "RIGHT", "BILATERAL". |
| `MIDIR` | Specimen Directionality within Subject | Char | Perm | Variable Qualifier | Qualifier for directionality of the location of the specimen in MILOC. Examples: "DORSAL", "PROXIMAL". |
| `MIMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the test or examination. This could include the technique or type of staining used for the slides. Examples: "IHC", "Crystal violet", "Safranin", "Trypan blue", or "Propidium iodide". |
| `MILOBXFL` | Last Observation Before Exposure Flag | Char | Exp | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `MIBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. The value should be "Y" or null. Note that MIBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| `MIEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Example: "PATHOLOGIST", "PEER REVIEW", "SPONSOR PATHOLOGIST". |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time at which the specimen was collected. |
| `MIDTC` | Date/Time of Specimen Collection | Char | Exp | Timing | Date/time of specimen collection, in ISO 8601 format. |
| `MIDY` | Study Day of Specimen Collection | Num | Perm | Timing | Study day of specimen collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |
