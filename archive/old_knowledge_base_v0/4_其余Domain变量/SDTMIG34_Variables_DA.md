# SDTM IG v3.4 Variables - DA Domain

**Domain Code:** `DA`

**Total Variables:** 27

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study within the submission. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `DASEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `DAGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `DAREFID` | Reference ID | Char | Perm | Identifier | Optional internal or external identifier such as a code from the product packaging (e.g., bottle label, package label, kit label). |
| `DASPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Examples: Line number on the Product Accountability CRF page, a code from the product packaging (e.g., bottle label, package label, kit label). |
| `DALNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| `DALNKGRP` | Link Group ID | Char | Perm | Identifier | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| `DATESTCD` | Short Name of Accountability Assessment | Char | Req | Topic | Short character value for DATEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters and cannot begin with a number or contain characters other than letters, numbers, or underscores. Examples: "DISPAMT", "RETAMT". |
| `DATEST` | Name of Accountability Assessment | Char | Req | Synonym Qualifier | Verbatim name corresponding to the topic variable of the test or examination used to obtain the product accountability assessment. The value in DATEST cannot be longer than 40 characters. Examples: "Dispensed Amount", "Returned Amount". |
| `DACAT` | Category | Char | Perm | Grouping Qualifier | Used to define a category of topic-variable values. Examples: "STUDY MEDICATION", "RESCUE MEDICATION". |
| `DASCAT` | Subcategory | Char | Perm | Grouping Qualifier | Used to define a further categorization level for a group of related records. |
| `DAORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the product accountability assessment as originally received or collected. |
| `DAORRESU` | Original Units | Char | Perm | Variable Qualifier | Unit for DAORRES. |
| `DASTRESC` | Result or Finding in Standard Format | Char | Exp | Result Qualifier | Contains the result value for all product accountability assessments copied or derived from DAORRES, in a standard format or in standard units. DASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in DASTRESN. |
| `DASTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from DASTRESC. DASTRESN should store all numeric test results or findings. |
| `DASTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized units used for DASTRESC and DASTRESN. |
| `DASTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a product accountability assessment was not done. Should be null or have a value of "NOT DONE". |
| `DAREASND` | Reason Not Done | Char | Perm | Record Qualifier | Reason not done. Used in conjunction with DASTAT when value is "NOT DONE". |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit, based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm (see Section 7.2.1, Trial Arms). |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| `DADTC` | Date/Time of Collection | Char | Exp | Timing | Date and time of the product accountability assessment represented in ISO 8601 character format. |
| `DADY` | Study Day of Visit/Collection/Exam | Num | Perm | Timing | Study day of product accountability assessment, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC in Demographics. |
