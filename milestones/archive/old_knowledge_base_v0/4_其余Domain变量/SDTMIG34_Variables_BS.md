# SDTM IG v3.4 Variables - BS Domain

**Domain Code:** `BS`

**Total Variables:** 35

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SPDEVID` | Sponsor Device Identifier | Char | Perm | Identifier | Sponsor-defined identifier for a device. |
| `BSSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1. |
| `BSGRPID` | Group ID | Char | Perm | Identifier | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| `BSREFID` | Reference ID | Char | Exp | Identifier | Internal or external identifier such as lab specimen ID. |
| `BSSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. |
| `BSTESTCD` | Biospecimen Test Short Name | Char | Req | Topic | Short character value for BSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: VOLUME, RIN. |
| `BSTEST` | Biospecimen Test Name | Char | Req | Synonym Qualifier | Long name for BSTESTCD. Examples: Volume, RNA Integrity Number. |
| `BSCAT` | Category for Biospecimen Test | Char | Exp | Grouping Qualifier | Used to define a category of topic-variable values. Example: MEASUREMENT, QUALITY. |
| `BSSCAT` | Subcategory for Biospecimen Test | Char | Perm | Grouping Qualifier | Used to define a further categorization of BSCAT values. |
| `BSORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the measurement or finding as originally received or collected. |
| `BSORRESU` | Original Units | Char | Exp | Variable Qualifier | Unit for BSORRES. Examples: mg, mL. |
| `BSSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings, copied or derived from BSORRES in a standard format or standard units. BSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in BSSTRESN. |
| `BSSTRESN` | Numeric Result/Finding in Standard Units | Num | Exp | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from BSSTRESC. BSSTRESN should store all numeric test results or findings. |
| `BSSTRESU` | Standard Units | Char | Exp | Variable Qualifier | Standardized unit used for BSSTRESC and BSSTRESN. |
| `BSSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a test was not done, or was attempted but did not generate a result. Should be null or have a value of NOT DONE. |
| `BSREASND` | Reason Test Not Done | Char | Perm | Record Qualifier | Reason not done. Used in conjunction with BSSTAT when value is NOT DONE. |
| `BSNAM` | Vendor Name | Char | Perm | Record Qualifier | Name or identifier of the vendor (e.g., laboratory) that provided the test results. |
| `BSSPEC` | Specimen Type | Char | Perm | Record Qualifier | Defines the type of specimen used for a measurement. Examples: SERUM, PLASMA, URINE, SOFT TISSUE. |
| `BSANTREG` | Anatomical Region of Specimen | Char | Perm | Variable Qualifier | Defines the specific anatomical or biological region of a tissue, organ specimen or the region from which the specimen is obtained, as defined in the protocol, such as a section or part of what is described in the BSSPEC variable. Examples: CORTEX, MEDULLA, MUCOSA. |
| `BSSPCCND` | Specimen Condition | Char | Perm | Record Qualifier | Defines the condition of the specimen. Examples: HEMOLYZED, ICTERIC, LIPEMIC. |
| `BSMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the test or examination. Examples: SPECTROPHOTOMETRY, ELECTROPHORESIS. |
| `BSBLFL` | Baseline Flag | Char | Perm | Record Qualifier | Indicator used to identify a baseline value. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `BSDTC` | Date/Time of Specimen Collection | Char | Exp | Timing | Date and time of specimen collection. |
| `BSDY` | Study Day of Specimen Collection | Num | Perm | Timing | Study day of specimen collection relative to the sponsor-defined RFSTDTC. |
| `BSTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See BSTPTNUM and BSTPTREF. |
| `BSTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of BSTPT used in sorting. |
| `BSELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Elapsed time relative to a planned fixed reference (BSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration. |
| `BSTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by BSELTM, BSTPTNUM, and BSTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL. |
| `BSRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by BSTPTREF. |
