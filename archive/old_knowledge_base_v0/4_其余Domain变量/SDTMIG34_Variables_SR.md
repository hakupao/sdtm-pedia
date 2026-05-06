# SDTM IG v3.4 Variables - SR Domain

**Domain Code:** `SR`

**Total Variables:** 39

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SRSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `SRGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `SRREFID` | Reference ID | Char | Perm | Identifier | Internal or external specimen identifier. Example: "Specimen ID". |
| `SRSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. |
| `SRTESTCD` | Skin Response Test or Exam Short Name | Char | Req | Topic | Short name of the measurement, test, or examination described in SRTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SRTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SRTESTCD cannot contain characters other than letters, numbers, or underscores. |
| `SRTEST` | Skin Response Test or Examination Name | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in SRTEST cannot be longer than 40 characters. Example: "Wheal Diameter". |
| `SROBJ` | Object of the Observation | Char | Req | Record Qualifier | Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the dose of the immunogenic material or the allergen associated with the response (e.g., "Johnson Grass IgE 0.15 BAU mL"). |
| `SRCAT` | Category for Test | Char | Perm | Grouping Qualifier | Used to define a category of topic-variable values across subjects. |
| `SRSCAT` | Subcategory for Test | Char | Perm | Grouping Qualifier | A further categorization of SRCAT values. |
| `SRORRES` | Results or Findings in Original Units | Char | Exp | Result Qualifier | Results of measurement or finding as originally received or collected. |
| `SRORRESU` | Original Units | Char | Exp | Variable Qualifier | Original units in which the data were collected. The unit for SRORRES. Example: "mm". |
| `SRSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from SRORRES, in a standard format or in standard units. SRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SRSTRESN. |
| `SRSTRESN` | Numeric Results/Findings in Std. Units | Num | Exp | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from SRSTRESC. SRSTRESN should store all numeric test results or findings. |
| `SRSTRESU` | Standard Units | Char | Exp | Variable Qualifier | Standardized units used for SRSTRESC and SRSTRESN. Example: "mm". |
| `SRSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate exam not done. Should be null if a result exists in SRORRES. |
| `SRREASND` | Reason Not Done | Char | Perm | Record Qualifier | Describes why a measurement or test was not performed. Used in conjunction with SRSTAT when value is "NOT DONE". |
| `SRNAM` | Vendor Name | Char | Perm | Record Qualifier | Name or identifier of the laboratory or vendor who provided the test results. |
| `SRSPEC` | Specimen Type | Char | Perm | Record Qualifier | Defines the types of specimen used for a measurement. Example: "SKIN". |
| `SRLOC` | Location Used for Measurement | Char | Perm | Record Qualifier | Location relevant to the collection of the measurement. |
| `SRLAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for anatomical location further detailing laterality of intervention administration. Examples: "RIGHT", "LEFT", "BILATERAL". |
| `SRMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of test or examination. Examples: "ELISA", "EIA", "MICRONEUTRALIZATION ASSAY", "PLAQUE REDUCTION NEUTRALIZATION ASSAY". |
| `SRLOBXFL` | Last Observation Before Exposure Flag | Char | Perm | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `SRBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. The value should be "Y" or null. Note that SRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| `SREVAL` | Evaluator | Char | Perm | Record Qualifier | Role of person who provided evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR". |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", and "FOLLOW-UP". |
| `SRDTC` | Date/Time of Collection | Char | Exp | Timing | Collection date and time of an observation represented in ISO 8601. |
| `SRDY` | Study Day of Visit/Collection/Exam | Num | Perm | Timing | Actual study day of visit/collection/exam expressed in integer days relative to sponsor- defined RFSTDTC in Demographics. |
| `SRTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See SRTPTNUM and SRTPTREF. Examples: "START", "5 MIN POST". |
| `SRTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of SRTPT to aid in sorting. |
| `SRELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time (in ISO 8601) relative to a fixed time point reference (SRTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by SRTPTREF. |
| `SRTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by SRELTM, SRTPTNUM, and SRTPT. Example: "INTRADERMAL INJECTION". |
| `SRRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time of the reference time point, SRTPTREF. |
