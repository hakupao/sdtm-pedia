# SDTM IG v3.4 Variables - MB Domain

**Domain Code:** `MB`

**Total Variables:** 47

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `FOCID` | Focus of Study-Specific Interest | Char | Perm | Identifier | Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed. The value in this variable should have inherent semantic meaning. |
| `MBSEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number. |
| `MBGRPID` | Group ID | Char | Perm | Identifier | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| `MBREFID` | Reference ID | Char | Perm | Identifier | Internal or external specimen identifier (e.g., sample ID for a subject sample from which a microbial culture was generated). |
| `MBSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. |
| `MBLNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. For example, it may be used to link genetic findings (in the PF domain) about a microbe to the original culture of that microbe (in MB), or to susceptibility records (in MS) if needed. |
| `MBLNKGRP` | Link Group ID | Char | Perm | Identifier | Identifier used to link related records across domains. This will usually be a many-to-one relationship. |
| `MBTESTCD` | Microbiology Test or Finding Short Name | Char | Req | Topic | Short name of the measurement, test, or finding described in MBTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MBTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MBTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MCORGIDN" for Microbial Organism Identification "GMNCOC" for Gram Negative Cocci. |
| `MBTEST` | Microbiology Test or Finding Name | Char | Req | Synonym Qualifier | Verbatim name of the test or examination used to obtain the measurement or finding. The value in MBTEST cannot be longer than 40 characters. Examples: "Microbial Organism Identification", "Gram Negative Cocci", "HIV-1 RNA". |
| `MBTSTDTL` | Measurement, Test or Examination Detail | Char | Perm | Variable Qualifier | Further description of MBTESTCD and MBTEST. Example: "VIRAL LOAD" when MBTESTCD represents viral genetic material, such as "HCRNA", "QUANTIFICATION" when MBTESTCD represents any organism being quantified. |
| `MBCAT` | Category | Char | Perm | Grouping Qualifier | Used to define a category of related records. |
| `MBSCAT` | Subcategory | Char | Perm | Grouping Qualifier | Used to define a further categorization of MBCAT values. |
| `MBORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the microbiology measurement or finding as originally received or collected. Examples for "GRAM STAIN" findings: "+3 MODERATE", "+2 FEW", "<10". Examples for "CULTURE PLATE" findings: "KLEBSIELLA PNEUMONIAE", "STREPTOCOCCUS PNEUMONIAE". |
| `MBORRESU` | Original Units | Char | Perm | Variable Qualifier | Original unit for MBORRES. Example: "mcg/mL". |
| `MBSTRESC` | Result or Finding in Standard Format | Char | Exp | Result Qualifier | Contains the result value for all findings copied or derived from MBORRES, in a standard format or standard units. MBSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MBSTRESN. For example, if a test has results "+3 MODERATE", "MOD", and "MODERATE" in MBORRES and these results effectively have the same meaning, they could be represented in standard format in MBSTRESC as "MODERATE". |
| `MBSTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from MBSTRESC. MBSTRESN should store all numeric test results or findings. |
| `MBSTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized units used for MBSTRESC and MBSTRESN. |
| `MBRESCAT` | Result Category | Char | Perm | Variable Qualifier | Used to categorize the result of a finding in a standard format. |
| `MBSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a question was not asked or a test was not done, or that a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| `MBREASND` | Reason Not Done | Char | Perm | Record Qualifier | Reason not done. Used in conjunction with MBSTAT when value is NOT DONE. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". |
| `MBNAM` | Laboratory/Vendor Name | Char | Perm | Record Qualifier | Name or identifier of the vendor (e.g., laboratory) that provided the test results. |
| `MBLOINC` | LOINC Code | Char | Perm | Synonym Qualifier | Logical Observation Identifiers Names and Codes (LOINC) code for the topic variable (e.g., lab test). |
| `MBSPEC` | Specimen Material Type | Char | Perm | Record Qualifier | Defines the type of specimen used for a measurement. Examples: "SPUTUM", "BLOOD", "PUS". |
| `MBSPCCND` | Specimen Condition | Char | Perm | Record Qualifier | Free or standardized text describing the condition of the specimen. Example: "CONTAMINATED". |
| `MBLOC` | Specimen Collection Location | Char | Perm | Record Qualifier | Anatomical location relevant to the collection of the measurement. |
| `MBLAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for specimen collection location further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL". |
| `MBDIR` | Directionality | Char | Perm | Variable Qualifier | Qualifier for specimen collection location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL". |
| `MBMETHOD` | Method of Test or Examination | Char | Exp | Record Qualifier | Method of the test or examination. Examples: "GRAM STAIN", "MICROBIAL CULTURE, LIQUID", "QUANTITATIVE REVERSE TRANSCRIPTASE POLYMERASE CHAIN REACTION". |
| `MBLOBXFL` | Last Observation Before Exposure Flag | Char | Perm | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `MBBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. Should be "Y" or null. Note that MBBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset. |
| `MBFAST` | Fasting Status | Char | Perm | Record Qualifier | Indicator used to identify fasting status. Valid values include "Y", "N", "U", or null if not relevant. |
| `MBDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element which the specimen collection occurred. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the date/time at which the specimen was collected. |
| `MBDTC` | Date/Time of Collection | Char | Exp | Timing | Date/time of specimen collection. |
| `MBDY` | Study Day of Visit/Collection/Exam | Num | Perm | Timing | Study day of the specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
| `MBTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See MBTPTNUM and MBTPTREF. Examples: "Start", "5 min post". |
| `MBTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numeric version of MBTPT used in sorting. |
| `MBELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time (in ISO 8601) relative to a planned fixed reference (MBTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by MBTPTREF, or "PT8H" to represent the period of 8 hours after the reference point indicated by MBTPTREF. |
| `MBTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by MBELTM, MBTPTNUM, and MBTPT. Example: "PREVIOUS DOSE". |
| `MBRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point, MBTPTREF. |
