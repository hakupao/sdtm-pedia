# SDTM IG v3.4 Variables - ML Domain

**Domain Code:** `ML`

**Total Variables:** 37

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `MLSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `MLGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `MLSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. Examples: a number preprinted on the CRF as an explicit line identifier, record identifier defined in the sponsor's operational database. |
| `MLTRT` | Name of Meal | Char | Req | Topic | Verbatim food product name that is either preprinted or collected on a CRF. |
| `MLCAT` | Category for Meal | Char | Perm | Grouping Qualifier | Used to define a category of MLTRT values. |
| `MLSCAT` | Subcategory for Meal | Char | Perm | Grouping Qualifier | Used to define a further categorization of MLCAT values. |
| `MLPRESP` | ML Pre-specified | Char | Perm | Variable Qualifier | Used when a specific meal is prespecified on a CRF. Values should be "Y" or null. |
| `MLOCCUR` | ML Occurrence | Char | Perm | Record Qualifier | Used to record whether a prespecified meal occurred when information about the occurrence of a specific meal is solicited. |
| `MLSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate when a question about the occurrence of a prespecified meal was not answered. Should be null or have a value of "NOT DONE". |
| `MLREASND` | Reason Meal Not Collected | Char | Perm | Record Qualifier | Describes the reason a response to a question about the occurrence of a meal was not collected. Used in conjunction with MLSTAT when value is "NOT DONE". |
| `MLDOSE` | Dose | Num | Perm | Record Qualifier | Amount of MLTRT consumed. Not populated when MLDOSTXT is populated. |
| `MLDOSTXT` | Dose Description | Char | Perm | Record Qualifier | Amount description of MLTRT consumed, collected in text form. Not populated when MLDOSE is populated. Examples: "<1 per day", "200-400". |
| `MLDOSU` | Dose Units | Char | Perm | Variable Qualifier | Units for MLDOSE, MLDOSTOT, or MLDOSTXT. |
| `MLDOSFRM` | Dose Form | Char | Perm | Variable Qualifier | Dosage form for MLTRT. Example: "BAR, CHEWABLE". |
| `VISITNUM` | Visit Number | Num | Perm | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the meal started. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the meal. |
| `MLDTC` | Date/Time of Collection | Char | Perm | Timing | Collection date and time of the meal represented in ISO 8601 character format. |
| `MLSTDTC` | Start Date/Time of Meal | Char | Perm | Timing | Start date/time of the meal represented in ISO 8601 character format. |
| `MLENDTC` | End Date/Time of Meal | Char | Perm | Timing | End date/time of the meal represented in ISO 8601 character format. |
| `MLDY` | Study Day of Visit/Collection/Exam | Num | Perm | Timing | Actual study day of the visit/collection expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `MLSTDY` | Study Day of Start of Meal | Num | Perm | Timing | Actual study day of start of the meal expressed in integer days relative to sponsor-defined RFSTDTC in Demographics. |
| `MLENDY` | Study Day of End of Meal | Num | Perm | Timing | Actual study day of end of the meal expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `MLDUR` | Duration of Meal | Char | Perm | Timing | Collected duration of the meal represented in ISO 8601 character format. Used only if collected on the CRF and not derived. |
| `MLTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point. See MLTPTNUM and MLTPTREF. |
| `MLTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numeric version of planned time point used in sorting. |
| `MLELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time (in ISO 8601) relative to the planned fixed reference (MLTPTREF). This variable is useful when there are repetitive measures. Not a clock time or a date/time variable. Represented as an ISO 8601 duration. |
| `MLTPTREF` | Time Point Reference | Char | Perm | Timing | Description of the fixed reference point referred to by MLELTM, MLTPTNUM, and MLTPT. |
| `MLRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by MLTPTREF in ISO 8601 character format. |
| `MIDS` | Disease Milestone Instance Name | Char | Perm | Timing | The name of a specific instance of a disease milestone type (MIDSTYPE) described in the Trial Disease Milestones dataset. This should be unique within a subject. Used only in conjunction with RELMIDS and MIDSDTC. |
| `RELMIDS` | Temporal Relation to Milestone Instance | Char | Perm | Timing | The temporal relationship of the observation to the disease milestone instance name in MIDS. Examples: "IMMEDIATELY BEFORE", "AT TIME OF", "AFTER". |
| `MIDSDTC` | Disease Milestone Instance Date/Time | Char | Perm | Timing | The start date/time of the disease milestone instance name in MIDS, in ISO 8601 format. |
