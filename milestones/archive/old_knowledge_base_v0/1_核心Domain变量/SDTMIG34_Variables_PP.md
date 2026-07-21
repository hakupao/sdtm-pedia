# SDTM IG v3.4 Variables - PP Domain

**Domain Code:** `PP`

**Total Variables:** 26

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. \n |
| `PPSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `PPGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain to support relationships within the domain and between domains. |
| `PPTESTCD` | Parameter Short Name | Char | Req | Topic | Short name of the pharmacokinetic parameter. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "AUCALL", "TMAX", "CMAX". |
| `PPTEST` | Parameter Name | Char | Req | Synonym Qualifier | Name of the pharmacokinetic parameter. The value in PPTEST cannot be longer than 40 characters. Examples: "AUC All", "Time of CMAX", "Max Conc". |
| `PPCAT` | Parameter Category | Char | Exp | Grouping Qualifier | Used to define a category of related records. For PP, this should be the name of the analyte in PCTEST whose profile the parameter is associated with. |
| `PPSCAT` | Parameter Subcategory | Char | Perm | Grouping Qualifier | Categorization of the model type used to calculate the PK parameters. Examples: "COMPARTMENTAL", "NON-COMPARTMENTAL". |
| `PPORRES` | Result or Finding in Original Units | Char | Exp | Result Qualifier | Result of the measurement or finding as originally received or collected. |
| `PPORRESU` | Original Units | Char | Exp | Variable Qualifier | Original units in which the data were collected. The unit for PPORRES. Example: "ng/L". See PP Assumption 3. |
| `PPSTRESC` | Character Result/Finding in Std Format | Char | Exp | Result Qualifier | Contains the result value for all findings, copied or derived from PPORRES in a standard format or standard units. PPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PPSTRESN. |
| `PPSTRESN` | Numeric Result/Finding in Standard Units | Num | Exp | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from PPSTRESC. PPSTRESN should store all numeric test results or findings. |
| `PPSTRESU` | Standard Units | Char | Exp | Variable Qualifier | Standardized unit used for PPSTRESC and PPSTRESN. See PP Assumption 3. |
| `PPSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a parameter was not calculated. Should be null if a result exists in PPORRES. |
| `PPREASND` | Reason Parameter Not Calculated | Char | Perm | Record Qualifier | Describes why a parameter was not calculated, such as "INSUFFICIENT DATA". Used in conjunction with PPSTAT when value is "NOT DONE". |
| `PPSPEC` | Specimen Material Type | Char | Exp | Record Qualifier | Defines the type of specimen used for a measurement. If multiple specimen types are used for a calculation (e.g., serum and urine for renal clearance), then this field should be left blank. Examples: "SERUM", "PLASMA", "URINE". |
| `PPANMETH` | Analysis Method | Char | Perm | Record Qualifier | Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result. Example: A named formula used to calculate AUC, such as "LIN-LOG TRAPEZOIDAL METHOD". \n Sponsor-defined formulas can also be represented by this variable. Example: Calculating ratio AUCs where the PPANMETH may be "DRUG METABOLITE 1 TO DRUG PARENT" or "DRUG METABOLITE 2 TO METABOLITE 1". |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected. |
| `PPDTC` | Date/Time of Parameter Calculations | Char | Perm | Timing | Nominal date/time of parameter calculations. |
| `PPDY` | Study Day of Parameter Calculations | Num | Perm | Timing | Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. |
| `PPTPTREF` | Time Point Reference | Char | Perm | Timing | The description of a time point that acts as a fixed reference for a series of planned time points. |
| `PPRFTDTC` | Date/Time of Reference Point | Char | Exp | Timing | Date/time of the reference time point from the PC records used to calculate a parameter record. The values in PPRFTDTC should be the same as that in PCRFTDTC for related records. |
| `PPSTINT` | Planned Start of Assessment Interval | Char | Perm | Timing | The start of a planned evaluation or assessment interval relative to the time point reference. |
| `PPENINT` | Planned End of Assessment Interval | Char | Perm | Timing | The end of a planned evaluation or assessment interval relative to the time point reference. |
