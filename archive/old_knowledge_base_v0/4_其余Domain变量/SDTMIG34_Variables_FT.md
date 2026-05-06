# SDTM IG v3.4 Variables - FT Domain

**Domain Code:** `FT`

**Total Variables:** 38

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `FTSEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number. |
| `FTGRPID` | Group ID | Char | Perm | Identifier | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| `FTREFID` | Reference ID | Char | Perm | Identifier | Optional internal or external identifier. |
| `FTSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the Test page. |
| `FTTESTCD` | Short Name of Test | Char | Req | Topic | Short character value for FTTEST, which can be used as a column name when converting a dataset from a vertical format to a horizontal format. The value cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FTTESTCD cannot contain characters other than letters, numbers, or underscores. \n Controlled terminology for FTTESTCD is published in separate codelists for each instrument. See https://www.cdisc.org/standards/terminology/controlled-terminology for values for FTTESTCD. Examples: "W250101", "W25F0102". |
| `FTTEST` | Name of Test | Char | Req | Synonym Qualifier | Verbatim name of the question used to obtain the finding. The value in FTTEST cannot be longer than 40 characters. \n Controlled terminology for FTTEST is published in separate codelists for each instrument. See https://www.cdisc.org/standards/terminology/controlled-terminology for values for FTTEST. Examples: "W2501-25 Foot Walk Time", "W25F-More Than Two Attempts". |
| `FTCAT` | Category | Char | Req | Grouping Qualifier | Used to specify the functional test in which the functional test question identified by FTTEST and FTTESTCD was included. |
| `FTSCAT` | Subcategory | Char | Perm | Grouping Qualifier | Used to define a further categorization of FTCAT values. |
| `FTPOS` | Position of Subject During Observation | Char | Perm | Record Qualifier | Position of the subject during the test. Examples: "SUPINE", "STANDING", "SITTING". |
| `FTORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the measurement or finding as originally received or collected. |
| `FTORRESU` | Original Units | Char | Perm | Variable Qualifier | Original units in which the data were collected. Unit for FTORRES. |
| `FTSTRESC` | Result or Finding in Standard Format | Char | Exp | Result Qualifier | Contains the result value for all findings, copied or derived from FTORRES in a standard format or in standard units. FTSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FTSTRESN. |
| `FTSTRESN` | Numeric Result/Finding in Standard Units | Num | Perm | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from FTSTRESC. FTSTRESN should store all numeric test results or findings. |
| `FTSTRESU` | Standard Units | Char | Perm | Variable Qualifier | Standardized units used for FTSTRESC and FTSTRESN. |
| `FTSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". |
| `FTREASND` | Reason Not Done | Char | Perm | Record Qualifier | Describes why a test was not done, or a test was attempted but did not generate a result. Used in conjunction with FTSTAT when value is "NOT DONE". |
| `FTXFN` | External File Path | Char | Perm | Record Qualifier | File path to an external file. |
| `FTNAM` | Vendor Name | Char | Perm | Record Qualifier | Name or identifier of the vendor or laboratory that provided the test results. |
| `FTMETHOD` | Method of Test or Examination | Char | Perm | Record Qualifier | Method of the test or examination. |
| `FTLOBXFL` | Last Observation Before Exposure Flag | Char | Exp | Record Qualifier | Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. |
| `FTBLFL` | Baseline Flag | Char | Perm | Record Qualifier | A baseline defined by the sponsor (could be derived in the same manner as FTLOBXFL or ABLFL, but is not required to be). The value should be "Y" or null. Note that FTBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset. |
| `FTDRVFL` | Derived Flag | Char | Perm | Record Qualifier | Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null. |
| `FTREPNUM` | Repetition Number | Num | Perm | Record Qualifier | The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample. |
| `VISITNUM` | Visit Number | Num | Exp | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT based upon RFSTDTC in Demographics. Should be an integer. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the observation date/time of the functional tests finding. |
| `FTDTC` | Date/Time of Test | Char | Exp | Timing | Collection date and time of functional test. |
| `FTDY` | Study Day of Test | Num | Perm | Timing | Actual study day of test expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `FTTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See FTTPTNUM and FTTPTREF. |
| `FTTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numeric version of planned time point used in sorting. |
| `FTELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time relative to a planned fixed reference (FTTPTREF). Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| `FTTPTREF` | Time Point Reference | Char | Perm | Timing | Description of the fixed reference point referred to by FTELTM, FTTPTNUM, and FTTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `FTRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by FTTPTREF. |
