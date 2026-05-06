# SDTM IG v3.4 Variables - IS Domain

**Domain Code:** `IS`

**Total Variables:** 54

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `NHOID` | Non-host Organism ID | Char | Perm | Identifier | Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears. |
| `ISSEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| `ISGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `ISREFID` | Reference ID | Char | Perm | Identifier | Internal or external specimen identifier. Example: "458975-01". |
| `ISSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. |
| `ISTESTCD` | Immunogenicity Test/Exam Short Name | Char | Req | Topic | Short name of the measurement, test, or examination described in ISTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in ISTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). ISTESTCD cannot contain characters other than letters, numbers, or underscores. |
| `ISTEST` | Immunogenicity Test or Examination Name | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in ISTEST cannot be longer than 40 characters. Example: "Immunoglobulin E". |
| `ISTSTCND` | Test Condition | Char | Perm | Variable Qualifier | Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed. |
| `ISCNDAGT` | Test Condition Agent | Char | Perm | Record Qualifier | The textual description of the agent used to impose a test condition. Examples are different stimulating agents used in immunoassays such as those in the Interferon Gamma Response assay (e.g., Mycobacterium tuberculosis ESAT-6, CFP-10, TB 7.7, Mitogen). |
| `ISBDAGNT` | Binding Agent | Char | Perm | Variable Qualifier | Text description of the agent that is binding to the entity in the ISTEST variable. ISBDAGNT is used to indicate that there is a binding relationship between the entities in the ISTEST and ISBDAGNT variables, regardless of direction. \n ISBDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the 2 entities in ISTEST and ISBDAGNT. In other words, the combination of ISTEST and ISBDAGNT should describe the entity or the analyte being measured, without the need for additional variables. \n The binding agent may be (but is not limited to) a test article, a portion of the test article, a related compound, an endogenous molecule, an allergen, or an infectious agent. |
| `ISTSTOPO` | Test Operational Objective | Char | Perm | Variable Qualifier | Text description of the high-level purpose of the test at the operational level. If populated, valid values are "SCREEN", "CONFIRM", and "QUANTIFY". |
| `ISMSCBCE` | Molecule Secreted by Cells | Char | Perm | Variable Qualifier | Text description of the entity secreted by the cells represented in ISTEST. The combination of ISTEST and ISMSCBCE should describe the entity or the analyte being measured, without the need for additional variables. |
| `ISTSTDTL` | Test Detail | Char | Perm | Variable Qualifier | Further description of ISTESTCD and ISTEST. |
| `ISCAT` | Category for Immunogenicity Test | Char | Perm | Grouping Qualifier | Used to define a category of topic-variable values across subjects. Example: "SEROLOGY". |
| `ISSCAT` | Subcategory for Immunogenicity Test | Char | Perm | Grouping Qualifier | A further categorization of ISCAT. |
| `ISORRES` | Results or Findings in Original Units | Char | Exp | Result Qualifier | Result of the measurement or finding as originally received or collected. |
| `ISORRESU` | Original Units | Char | Exp | Variable Qualifier | Original units in which the data were collected. The unit for ISORRES. Examples: "Index Value", "gpELISA", "unit/mL". |
| `ISORNRLO` | Reference Range Lower Limit in Orig Unit | Char | Exp | Variable Qualifier | Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results. |
| `ISORNRHI` | Reference Range Upper Limit in Orig Unit | Char | Exp | Variable Qualifier | Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results. |
| `ISSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from ISORRES, in a standard format or in standard units. ISSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in ISSTRESN. |
| `ISSTRESN` | Numeric Results/Findings in Std. Units | Num | Exp | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from ISSTRESC. ISSTRESN should store all numeric test results or findings. |
| `ISSTRESU` | Standard Units | Char | Exp | Variable Qualifier | Standardized units used for ISSTRESC and ISSTRESN. Examples: "Index Value", "gpELISA", "unit/mL". |
| `ISSTNRLO` | Reference Range Lower Limit-Std Units | Num | Exp | Variable Qualifier | Lower end of reference range for continuous measurements for ISSTRESC/ISSTRESN in standardized units. Should be populated only for continuous results. |
| `ISSTNRHI` | Reference Range Upper Limit-Std Units | Num | Exp | Variable Qualifier | Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results. |
| `ISSTNRC` | Reference Range for Char Rslt-Std Units | Char | Perm | Variable Qualifier | For normal range values that are character in ordinal scale or if categorical ranges were supplied. Examples: "-1 to +1", "NEGATIVE TO TRACE". |
| `ISNRIND` | Reference Range Indicator | Char | Exp | Variable Qualifier | Indicates where the value falls with respect to reference range defined by ISORNRLO and ISORNRHI, ISSTNRLO and ISSTNRHI, or by ISSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". \n Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether ISNRIND refers to the original or standard reference ranges and results. \n Should not be used to indicate clinical significance. |
| `ISSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate a test was not done. Should be null if a result exists in ISORRES. |
| `ISREASND` | Reason Not Done | Char | Perm | Record Qualifier | Describes why a measurement or test was not performed. Used in conjunction with ISSTAT when value is "NOT DONE". |
| `ISNAM` | Vendor Name | Char | Perm | Record Qualifier | Name or identifier of the laboratory or vendor who provided the test results. |
| `ISSPEC` | Specimen Type | Char | Perm | Record Qualifier | Defines the types of specimen used for a measurement. Example: "SERUM". |
| `ISSPCCND` | Specimen Condition | Char | Perm | Record Qualifier | Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC". |
| `ISSPCUFL` | Specimen Usability for the Test | Char | Perm | Record Qualifier | Describes the usability of the specimen for the test. The value will be "N" if the specimen is not usable, and null if the specimen is usable. |
| `ISMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the test or examination. Examples: "ELISA", "ELISPOT". |
| `ISLOBXFL` | Last Observation Before Exposure Flag | Char | Perm | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `ISBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that ISBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| `ISDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record. The value should be "Y" or null. Examples of records that might be derived for the submission datasets include those that represent the average of other records, do not come from the CRF, or are not as originally received or collected. If ISDRVFL="Y", then ISORRES may be null, with ISSTRESC and (if numeric) ISSTRESN having the derived value. |
| `ISLLOQ` | Lower Limit of Quantitation | Num | Exp | Variable Qualifier | Indicates the lower limit of quantitation for an assay. Units will be those used for ISSTRESU. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of the visit based upon RFSTDTC in Demographics. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| `ISDTC` | Date/Time of Collection | Char | Exp | Timing | Collection date and time of an observation. |
| `ISENDTC` | End Date/Time of Specimen Collection | Char | Perm | Timing | End date/time of the observation. |
| `ISDY` | Study Day of Visit/Collection/Exam | Num | Perm | Timing | Actual study day of visit/collection/exam expressed in integer days relative to sponsor-defined RFSTDTC in Demographics. |
| `ISENDY` | Study Day of End of Specimen Collection | Num | Perm | Timing | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `ISTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See ISTPTNUM and ISTPTREF. Examples: "Start", "5 min post". |
| `ISTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of ISTPT to aid in sorting. |
| `ISELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (ISTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable. Represented as ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by ISTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by ISTPTREF. |
| `ISTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by ISELTM, ISTPTNUM, and ISTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `ISRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time of the reference time point, ISTPTREF. |
