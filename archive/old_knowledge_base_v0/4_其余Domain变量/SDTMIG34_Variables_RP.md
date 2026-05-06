# SDTM IG v3.4 Variables - RP Domain

**Domain Code:** `RP`

**Total Variables:** 36

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `RPSEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1. |
| `RPGRPID` | Group ID | Char | Perm | Identifier | Optional group identifier, used to link together a block of related records within a subject in a domain. Also used to link together a block of related records in the Trial Summary dataset. |
| `RPREFID` | Reference ID | Char | Perm | Identifier | Optional internal or external identifier (e.g., lab specimen ID, UUID for an ECG waveform or a medical image). |
| `RPSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. Example: Preprinted line identifier on a CRF. |
| `RPLNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| `RPLNKGRP` | Link Group ID | Char | Perm | Identifier | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| `RPTESTCD` | Short Name of Reproductive Test | Char | Req | Topic | Short character value for RPTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: "CHILDPOT", "BCMETHOD", "MENARAGE". |
| `RPTEST` | Name of Reproductive Test | Char | Req | Synonym Qualifier | Long name For RPTESTCD. Examples: "Childbearing Potential", "Birth Control Method", "Menarche Age". |
| `RPCAT` | Category for Reproductive Test | Char | Perm | Grouping Qualifier | Used to define a category of topic-variable values. Example: "No use case to date, but values would be relative to reproduction tests grouping". |
| `RPSCAT` | Subcategory for Reproductive Test | Char | Perm | Grouping Qualifier | Used to define a further categorization of RPCAT values. Example: "No use case to date, but values would be relative to reproduction tests grouping". |
| `RPORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the measurement or finding as originally received or collected. Examples: "120", "<1", "POS". |
| `RPORRESU` | Original Units | Char | Perm | Variable Qualifier | Unit for RPORRES. Examples: "in", "LB", "kg/L". |
| `RPSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from RPORRES, in a standard format or in standard units. RPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in RPSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in RPORRES, and these results effectively have the same meaning, they could be represented in standard format in RPSTRESC as "NEGATIVE". |
| `RPSTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from RPSTRESC. RPSTRESN should store all numeric test results or findings. |
| `RPSTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized units used for RPSTRESC and RPSTRESN. Example: "mol/L". |
| `RPSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| `RPREASND` | Reason Not Done | Char | Perm | Record Qualifier | Reason not done. Used in conjunction with RPSTAT when value is "NOT DONE". |
| `RPLOBXFL` | Last Observation Before Exposure Flag | Char | Perm | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `RPBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that RPBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| `RPDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record. The value should be "Y" or null. Records which represent the average of other records or which do not come from the CRF are examples of records that would be derived for the submission datasets. If RPDRVFL = "Y", then RPORRES may be null, with RPSTRESC and (if numeric) RPSTRESN having the derived value. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time at which the assessment was made. |
| `RPDTC` | Date/Time of Collection | Char | Exp | Timing | Collection date and time of an observation. |
| `RPDY` | Study Day of Visit/Collection/Exam | Num | Perm | Timing | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `RPDUR` | Duration | Char | Perm | Timing | Collected duration of an event, intervention, or finding represented in ISO 8601 character format. Used only if collected on the CRF and not derived. |
| `RPTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. |
| `RPTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numeric version of planned time point used in sorting. |
| `RPELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time in ISO 8601 character format relative to a planned fixed reference (RPTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| `RPTPTREF` | Time Point Reference | Char | Perm | Timing | Description of the fixed reference point referred to by RPELTM, RPTPTNUM, and RPTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `RPRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by RPTPTREF in ISO 8601 character format. |
