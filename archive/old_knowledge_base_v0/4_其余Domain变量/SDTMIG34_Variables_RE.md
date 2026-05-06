# SDTM IG v3.4 Variables - RE Domain

**Domain Code:** `RE`

**Total Variables:** 47

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SPDEVID` | Sponsor Device Identifier | Char | Perm | Identifier | Sponsor-defined identifier for a device. |
| `RESEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| `REGRPID` | Group ID | Char | Perm | Identifier | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| `REREFID` | Reference ID | Char | Perm | Identifier | Optional internal or external procedure identifier. |
| `RESPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| `RELNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| `RELNKGRP` | Link Group | Char | Perm | Identifier | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| `RETESTCD` | Short Name of Respiratory Test | Char | Req | Topic | Short name of the measurement, test, or examination. It can be used as a column name when converting a dataset from a vertical format to a horizontal format. The value in RETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). RETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "FEV1", "FVC". |
| `RETEST` | Name of Respiratory Test | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in RETEST cannot be longer than 40 characters. Examples: "Forced Expiratory Volume in 1 Second", "Forced Vital Capacity". |
| `RECAT` | Category for Respiratory Test | Char | Perm | Grouping Qualifier | Used to categorize observations across subjects. |
| `RESCAT` | Subcategory for Respiratory Test | Char | Perm | Grouping Qualifier | A further categorization. |
| `REPOS` | Position of Subject During Observation | Char | Perm | Record Qualifier | Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING". |
| `REORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the procedure measurement or finding as originally received or collected. |
| `REORRESU` | Original Units | Char | Perm | Variable Qualifier | Original units in which the data were collected. The unit for REORRES and REORREF. |
| `REORREF` | Reference Result in Original Units | Char | Perm | Variable Qualifier | Reference result for continuous measurements in original units. Should be collected only for continuous results. |
| `RESTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings, copied or derived from REORRES in a standard format or in standard units. RESTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in RESTRESN. |
| `RESTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from RESTRESC. RESTRESN should store all numeric test results or findings. |
| `RESTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized unit used for RESTRESC, RESTRESN and RESTREFN. |
| `RESTREFC` | Character Reference Result | Char | Perm | Variable Qualifier | Reference value for the result or finding copied or derived from --ORREF in a standard format. |
| `RESTREFN` | Numeric Reference Result in Std Units | Num | Perm | Variable Qualifier | Reference result for continuous measurements in standard units. Should be populated only for continuous results. |
| `RESTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a test was not done or a measurement was not taken. Should be null if a result exists in REORRES. |
| `REREASND` | Reason Not Done | Char | Perm | Record Qualifier | Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with RESTAT when value is "NOT DONE". |
| `RELOC` | Location Used for the Measurement | Char | Perm | Record Qualifier | Anatomical location of the subject relevant to the collection of the measurement. Examples: "LUNG", "BRONCHUS". |
| `RELAT` | Laterality | Char | Perm | Variable Qualifier | Side of the body used to collect measurement. Examples: "RIGHT", "LEFT". |
| `REDIR` | Directionality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| `REMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method used to create the result. |
| `RELOBXFL` | Last Observation Before Exposure Flag | Char | Exp | Record Qualifier | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `REBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be Y or null. Note that REBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| `REDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record. Should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If REDRVFL = "Y", then REORRES could be null, with RESTRESC and (if numeric) RESTRESN having the derived value. |
| `REEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| `REEVALID` | Evaluator Identifier | Char | Perm | Variable Qualifier | Used to distinguish multiple evaluators with the same role recorded in REEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". |
| `REREPNUM` | Repetition Number | Num | Perm | Record Qualifier | The instance number of a test that is repeated within a given time frame for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Example: multiple measurements of pulmonary function. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time at which the assessment was made. |
| `REDTC` | Date/Time of Collection | Char | Exp | Timing | Date/time of procedure or test. |
| `REDY` | Study Day of Visit/Collection/Exam | Num | Perm | Timing | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `RETPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See RETPTNUM and RETPTREF. Examples: "START", "5 MINUTES POST". |
| `RETPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numeric version of RETPT to aid in sorting. |
| `REELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time relative to a planned fixed reference (RETPTREF). Not a clock time or a date/time variable, but an interval, represented as ISO duration. Examples: "-PT15M" to represent 15 minutes prior to the reference time point indicated by RETPTREF, "PT8H" to represent 8 hours after the reference time point represented by RETPTREF. |
| `RETPTREF` | Time Point Reference | Char | Perm | Timing | Description of the fixed reference point referred to by REELTM, RETPTNUM, and RETPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `RERFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by RETPTREF. |
