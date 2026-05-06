# SDTM IG v3.4 Variables - MS Domain

**Domain Code:** `MS`

**Total Variables:** 61

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `NHOID` | Non-host Organism ID | Char | Perm | Identifier | Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears. |
| `MSSEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1. |
| `MSGRPID` | Group ID | Char | Perm | Identifier | Optional group identifier, used to link together a block of related records within a subject in a domain. In SDTMIG v3.2 this was an Expected variable. In this version, the core designation has been changed to Permissible. |
| `MSREFID` | Reference ID | Char | Perm | Identifier | Optional internal or external identifier (e.g., an identifier for the culture/isolate being tested for susceptibility). |
| `MSSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| `MSLNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. For example, it may be used to link genetic findings (in the PF domain) about a microbe to the original culture of that microbe (in MB), or to susceptibility records (in MS) if needed. |
| `MSTESTCD` | Short Name of Assessment | Char | Req | Topic | Short character value for MSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MIC" for Minimum Inhibitory Concentration; "MICROSUS" for Microbial Susceptibility. |
| `MSTEST` | Name of Assessment | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in MSTEST cannot be longer than 40 characters. Examples: "Minimum Inhibitory Concentration", "Microbial Susceptibility". |
| `MSAGENT` | Agent Name | Char | Exp | Variable Qualifier | The name of the agent for which resistance is tested. The agent specified may be based on genetic markers or direct phenotypic drug sensitivity testing. Examples: "Penicillin", name of study drug. |
| `MSCONC` | Agent Concentration | Num | Perm | Variable Qualifier | Numeric concentration of agent listed in MSAGENT. |
| `MSCONCU` | Agent Concentration Units | Char | Perm | Variable Qualifier | Units for value of the agent concentration listed in MSCONC. Example: "mg/L". |
| `MSTSTDTL` | Measurement, Test or Examination Detail | Char | Perm | Variable Qualifier | Further description of MSTESTCD and MSTEST. |
| `MSCAT` | Category | Char | Perm | Grouping Qualifier | Used to define a category of MSTEST values. |
| `MSSCAT` | Subcategory | Char | Perm | Grouping Qualifier | Used to define a further categorization of MSCAT values. |
| `MSORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the measurement or finding as originally received or collected. |
| `MSORRESU` | Original Units | Char | Perm | Variable Qualifier | Unit for MSORRES. Examples: "ug/mL". |
| `MSSTRESC` | Result or Finding in Standard Format | Char | Exp | Result Qualifier | Contains the result value for all findings, copied or derived from MSORRES in a standard format or in standard units. MSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MSSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in MSORRES and these results effectively have the same meaning, they could be represented in standard format in MSSTRESC as "NEGATIVE". |
| `MSSTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from MSSTRESC. MSSTRESN should store all numeric test results or findings. |
| `MSSTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized units used for MSSTRESC and MSSTRESN. Example: "mol/L". |
| `MSNRIND` | Normal/Reference Range Indicator | Char | Perm | Variable Qualifier | Used to indicate the value is outside the normal range or reference range. May be defined by MSORNRLO and MSORNRHI or other objective criteria. Examples: "Y", "N", "HIGH", "LOW", "NORMAL". "ABNORMAL". |
| `MSRESCAT` | Result Category | Char | Perm | Variable Qualifier | Used to categorize the result of a finding. In SDTMIG v3.2, MSRESCAT was used to categorize a numeric susceptibility result represented in MSORRES as either "SUSCEPTIBLE", "INTERMEDIATE", or "RESISTANT". However, results from some susceptibility tests may report only a categorical result and not a numeric result. Thus, in order for susceptibility results to be represented consistently, MSRESCAT should no longer be used for this purpose. In this version, the core designation has been changed from Expected to Permissible. |
| `MSSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| `MSREASND` | Reason Not Done | Char | Perm | Record Qualifier | Reason not done. Used in conjunction with MSSTAT when value is "NOT DONE". |
| `MSXFN` | External File Path | Char | Perm | Record Qualifier | Filename for an external file. |
| `MSNAM` | Laboratory/Vendor Name | Char | Perm | Record Qualifier | Name or identifier of the vendor (e.g., laboratory) that provided the test results. |
| `MSLOINC` | LOINC Code | Char | Perm | Synonym Qualifier | Logical Observation Identifiers Names and Codes (LOINC) code for the topic variable such as a lab test. |
| `MSSPEC` | Specimen Material Type | Char | Perm | Record Qualifier | Defines the type of specimen used for a measurement. Example: "SPUTUM". |
| `MSSPCCND` | Specimen Condition | Char | Perm | Record Qualifier | Defines the condition of the specimen. Example: "CLOUDY". |
| `MSLOC` | Location Used for the Measurement | Char | Perm | Record Qualifier | Anatomical location of the subject relevant to the collection of the measurement. |
| `MSLAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| `MSDIR` | Directionality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| `MSMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the test or examination. Examples: "EPSILOMETER", "MACRO BROTH DILUTION". |
| `MSANMETH` | Analysis Method | Char | Perm | Record Qualifier | Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result (e.g., an image or a genetic sequence). |
| `MSLOBXFL` | Last Observation Before Exposure Flag | Char | Perm | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `MSBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that MSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| `MSFAST` | Fasting Status | Char | Perm | Record Qualifier | Indicator used to identify fasting status. Valid values include "Y", "N", "U", or null if not relevant. |
| `MSDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| `MSEVAL` | Evaluator | Char | Perm | Record Qualifier | Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "MICROSCOPIST". |
| `MSEVALID` | Evaluator Identifier | Char | Perm | Variable Qualifier | Used to distinguish multiple evaluators with the same role recorded in MSEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2". |
| `MSACPTFL` | Accepted Record Flag | Char | Perm | Record Qualifier | In cases where more than 1 assessor provides an evaluation of a result or response, this flag identifies the record that is considered, by an independent assessor, to be the accepted evaluation. Expected to be "Y" or null. |
| `MSLLOQ` | Lower Limit of Quantitation | Num | Perm | Variable Qualifier | Indicates the lower limit of quantitation for an assay. Units will be those used for MSSTRESU. |
| `MSULOQ` | Upper Limit of Quantitation | Num | Perm | Variable Qualifier | Indicates the upper limit of quantitation for an assay. Units will be those used for MSSTRESU. |
| `MSREPNUM` | Repetition Number | Num | Perm | Record Qualifier | The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the specimen was collected. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time at which the specimen was collected. |
| `MSDTC` | Date/Time of Collection | Char | Perm | Timing | Collection date and time of an observation. |
| `MSDY` | Study Day of Visit/Collection/Exam | Num | Perm | Timing | Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `MSDUR` | Duration | Char | Perm | Timing | Collected duration of an event, intervention, or finding. Used only if collected on the CRF and not derived. |
| `MSTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See MSTPTNUM and MSTPTREF. |
| `MSTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numeric version of planned time point used in sorting. |
| `MSELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time relative to a planned fixed reference (MSTPTREF; e.g., previous dose, previous meal). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| `MSTPTREF` | Time Point Reference | Char | Perm | Timing | Description of the fixed reference point referred to by MSELTM, MSTPTNUM, and MSTPT. Example: "PREVIOUS DOSE". |
| `MSRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by MSTPTREF. |
| `MSEVLINT` | Evaluation Interval | Char | Perm | Timing | Duration of interval associated with an observation such as a finding MSTESTCD. Example: "-P2M" to represent a period of the past 2 months before the assessment. |
| `MSEVINTX` | Evaluation Interval Text | Char | Perm | Timing | Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS". |
