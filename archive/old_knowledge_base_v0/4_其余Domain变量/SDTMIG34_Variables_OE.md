# SDTM IG v3.4 Variables - OE Domain

**Domain Code:** `OE`

**Total Variables:** 52

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `FOCID` | Focus of Study-Specific Interest | Char | Perm | Identifier | Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed. |
| `OESEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `OEGRPID` | Group ID | Char | Perm | Identifier | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| `OELNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. |
| `OELNKGRP` | Link Group | Char | Perm | Identifier | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| `OETESTCD` | Short Name of Ophthalmic Test or Exam | Char | Req | Topic | Short character value for OETEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in OETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). OETESTCD cannot contain characters other than letters, numbers, or underscores. Example: "NUMLCOR". |
| `OETEST` | Name of Ophthalmic Test or Exam | Char | Req | Synonym Qualifier | Long name for the test or examination used to obtain the measurement or finding. The value in OETEST cannot be longer than 40 characters. Example: "Number of Letters Correct" for OETESTCD = "NUMLCOR". |
| `OETSTDTL` | Ophthalmic Test or Exam Detail | Char | Perm | Variable Qualifier | Further description of OETESTCD and OETEST. |
| `OECAT` | Category for Ophthalmic Test or Exam | Char | Perm | Grouping Qualifier | Used to define a category of topic-variable values. Examples: "VISUAL ACUITY", "CONTRAST SENSITIVITY", "OCULAR COMFORT". |
| `OESCAT` | Subcategory for Ophthalmic Test or Exam | Char | Perm | Grouping Qualifier | Used to define a further categorization of OECAT values. Example: "HIGH CONTRAST" or "LOW CONTRAST" when OECAT is "VISUAL ACUITY". |
| `OEORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the measurement or finding as originally received or collected. Examples: "120", "<1, NORMAL", "RED SPOT VISIBLE". |
| `OEORRESU` | Original Units | Char | Exp | Variable Qualifier | Original unit for OEORRES. Examples: "mm", "um". |
| `OEORNRLO` | Normal Range Lower Limit-Original Units | Char | Perm | Variable Qualifier | Lower end of normal range or reference range for results stored in OEORRES. |
| `OEORNRHI` | Normal Range Upper Limit-Original Units | Char | Perm | Variable Qualifier | Upper end of normal range or reference range for results stored in OEORRES. |
| `OESTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from OEORRES, in a standard format or in standard units. OESTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in OESTRESN. |
| `OESTRESN` | Numeric Result/Finding in Standard Units | Num | Exp | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from OESTRESC. OESTRESN should store all numeric test results or findings. |
| `OESTRESU` | Standard Units | Char | Exp | Variable Qualifier | Standardized units used for OESTRESC and OESTRESN. Examples: "mm", "um". |
| `OESTNRLO` | Normal Range Lower Limit-Standard Units | Num | Perm | Variable Qualifier | Lower end of normal range or reference range for standardized results (e.g., OESTRESC, OESTRESN) represented in standardized units (OESTRESU). |
| `OESTNRHI` | Normal Range Upper Limit-Standard Units | Num | Perm | Variable Qualifier | Upper end of normal range or reference range for standardized results (e.g., OESTRESC, OESTRESN) represented in standardized units (OESTRESU). |
| `OESTNRC` | Normal Range for Character Results | Char | Perm | Variable Qualifier | Normal range or reference range for results stored in OESTRESC that are character in ordinal or categorical scale. Example: "Negative to Trace". |
| `OENRIND` | Normal/Reference Range Indicator | Char | Perm | Variable Qualifier | Used to indicate the value is outside the normal range or reference range. May be defined by OEORNRLO and OEORNRHI or other objective criteria. Examples: "Y", "N"; "HIGH", "LOW"; "NORMAL", "ABNORMAL". |
| `OERESCAT` | Result Category | Char | Perm | Variable Qualifier | Used to categorize the result of a finding or medical status per interpretation of test results. Examples: "POSITIVE", "NEGATIVE". The variable OERESCAT is not meant to replace the use of OENRIND for cases where normal ranges are provided. |
| `OESTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| `OEREASND` | Reason Not Done | Char | Perm | Record Qualifier | Reason not done. Used in conjunction with OESTAT when value is "NOT DONE". |
| `OEXFN` | External File Path | Char | Perm | Record Qualifier | Filename for an external file, such as one for a retinal OCT image. |
| `OELOC` | Location Used for the Measurement | Char | Exp | Record Qualifier | Anatomical location of the subject relevant to the collection of the measurement. Examples: "EYE" for a finding record relative to the complete eye, "RETINA" for a measurement or assessment of only the retina. |
| `OELAT` | Laterality | Char | Exp | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| `OEDIR` | Directionality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| `OEPORTOT` | Portion or Totality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing the distribution (i.e., arrangement of, apportioning of). Examples: "ENTIRE", "SINGLE", "SEGMENT", "MANY". |
| `OEMETHOD` | Method of Test or Examination | Char | Exp | Record Qualifier | Method of the test or examination. Example: "ETDRS EYE CHART" for OETESTCD = "NUMLCOR". The different methods may offer different functionality or granularity, affecting the set of results and associated meaning. |
| `OELOBXFL` | Last Observation Before Exposure Flag | Char | Exp | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `OEBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that OEBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| `OEDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| `OEEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "INDEPENDENT ASSESSOR", "INVESTIGATOR". |
| `OEEVALID` | Evaluator Identifier | Char | Perm | Variable Qualifier | Used to distinguish multiple evaluators with the same role recorded in OEEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". |
| `OEACPTFL` | Accepted Record Flag | Char | Perm | Record Qualifier | In cases where more than one assessor provides an evaluation of a result or response, this flag identifies the record that is considered, by an independent assessor, to be the accepted evaluation. Expected to be "Y" or null. |
| `OEREPNUM` | Repetition Number | Num | Perm | Record Qualifier | The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time at which the assessment was made. |
| `OEDTC` | Date/Time of Collection | Char | Exp | Timing | Collection date/time of the observation. |
| `OEDY` | Study Day of Visit/Collection/Exam | Num | Exp | Timing | Actual study day of observation/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `OETPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point. |
| `OETPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numeric version of planned time point used in sorting. |
| `OEELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time relative to a planned fixed reference (OETPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| `OETPTREF` | Time Point Reference | Char | Perm | Timing | Description of the fixed reference point referred to by OETPT, OETPTNUM, and OEELTM. |
| `OERFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time of the reference time point, OETPTREF. |
