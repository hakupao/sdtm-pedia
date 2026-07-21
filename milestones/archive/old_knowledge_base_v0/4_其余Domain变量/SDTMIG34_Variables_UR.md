# SDTM IG v3.4 Variables - UR Domain

**Domain Code:** `UR`

**Total Variables:** 43

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `URSEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| `URGRPID` | Group ID | Char | Perm | Identifier | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| `URREFID` | Reference ID | Char | Perm | Identifier | Optional internal or external identifier (e.g., lab specimen ID, universally unique identifier (UUID) for a medical image). |
| `URSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. Example: Preprinted line identifier. |
| `URLNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| `URLNKGRP` | Link Group ID | Char | Perm | Identifier | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| `URTESTCD` | Short Name of Urinary Test | Char | Req | Topic | Short character value for URTEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in URTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). URTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "COUNT", "LENGTH", "RBLDFLW". |
| `URTEST` | Name of Urinary Test | Char | Req | Synonym Qualifier | Long name For URTESTCD. Examples: "Count", "Length", "Renal Blood Flow". |
| `URTSTDTL` | Urinary Test Detail | Char | Perm | Variable Qualifier | Further description of URTESTCD and URTEST. |
| `URCAT` | Category for Urinary Test | Char | Perm | Grouping Qualifier | Used to define a category of topic-variable values. |
| `URSCAT` | Subcategory for Urinary Test | Char | Perm | Grouping Qualifier | Used to define a further categorization of URCAT values. |
| `URORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the measurement or finding as originally received or collected. |
| `URORRESU` | Original Units | Char | Perm | Variable Qualifier | Unit for URORRES. |
| `URSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from URORRES, in a standard format or in standard units. URSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in URSTRESN. |
| `URSTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from URSTRESC. URSTRESN should store all numeric test results or findings. |
| `URSTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized units used for URSTRESC and URSTRESN. |
| `URRESCAT` | Result Category | Char | Perm | Variable Qualifier | Used to categorize the result of a finding. |
| `URSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| `URREASND` | Reason Not Done | Char | Perm | Record Qualifier | Reason not done. Used in conjunction with URSTAT when value is "NOT DONE". |
| `URLOC` | Location Used for the Measurement | Char | Perm | Record Qualifier | Anatomical location of the subject relevant to the collection of the measurement. |
| `URLAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| `URDIR` | Directionality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| `URMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the test or examination. |
| `URLOBXFL` | Last Observation Before Exposure Flag | Char | Exp | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `URBLFL` | Baseline Flag | Char | Perm | Record Qualifier | A baseline defined by the sponsor The value should be "Y" or null. Note that URBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| `URDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| `UREVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST". |
| `UREVALID` | Evaluator Identifier | Char | Perm | Variable Qualifier | Used to distinguish multiple evaluators with the same role recorded in UREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the observation was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time at which the observation was made. |
| `URDTC` | Date/Time of Collection | Char | Exp | Timing | Collection date and time of an observation. |
| `URDY` | Study Day of Visit/Collection/Exam | Num | Perm | Timing | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `URTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See URTPTNUM and URTPTREF. |
| `URTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numeric version of planned time point used in sorting. |
| `URELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time relative to a planned fixed reference (URTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| `URTPTREF` | Time Point Reference | Char | Perm | Timing | Description of the fixed reference point referred to by URELTM, URTPTNUM, and URTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `URRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by URTPTREF. |
