# SDTM IG v3.4 Variables - EX Domain

**Domain Code:** `EX`

**Total Variables:** 37

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `EXSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `EXGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `EXREFID` | Reference ID | Char | Perm | Identifier | Internal or external identifier (e.g., kit number, bottle label, vial identifier). |
| `EXSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page. |
| `EXLNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains. |
| `EXLNKGRP` | Link Group ID | Char | Perm | Identifier | Identifier used to link related, grouped records across domains. |
| `EXTRT` | Name of Treatment | Char | Req | Topic | Name of the protocol-specified study treatment given during the dosing period for the observation. |
| `EXCAT` | Category of Treatment | Char | Perm | Grouping Qualifier | Used to define a category of EXTRT values. |
| `EXSCAT` | Subcategory of Treatment | Char | Perm | Grouping Qualifier | A further categorization of EXCAT values. |
| `EXDOSE` | Dose | Num | Exp | Record Qualifier | Amount of EXTRT when numeric. Not populated when EXDOSTXT is populated. |
| `EXDOSTXT` | Dose Description | Char | Perm | Record Qualifier | Amount of EXTRT when non-numeric. Dosing amounts or a range of dosing information collected in text form. Example: "200-400". Not populated when EXDOSE is populated. |
| `EXDOSU` | Dose Units | Char | Exp | Variable Qualifier | Units for EXDOSE, EXDOSTOT, or EXDOSTXT representing protocol-specified values. Examples: "ng", "mg", "mg/kg", "mg/m2". |
| `EXDOSFRM` | Dose Form | Char | Exp | Variable Qualifier | Dose form for EXTRT. Examples: "TABLET", "LOTION". |
| `EXDOSFRQ` | Dosing Frequency per Interval | Char | Perm | Record Qualifier | Usually expressed as the number of repeated administrations of EXDOSE within a specific time period. Examples: "Q2H", "QD", "BID". |
| `EXDOSRGM` | Intended Dose Regimen | Char | Perm | Record Qualifier | Text description of the intended schedule or regimen for the Intervention. Example: "TWO WEEKS ON, TWO WEEKS OFF". |
| `EXROUTE` | Route of Administration | Char | Perm | Variable Qualifier | Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS". |
| `EXLOT` | Lot Number | Char | Perm | Record Qualifier | Lot number of the intervention product. |
| `EXLOC` | Location of Dose Administration | Char | Perm | Record Qualifier | Specifies location of administration. Examples: "ARM", "LIP". |
| `EXLAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for anatomical location further detailing laterality of the intervention administration. Examples: "LEFT", "RIGHT". |
| `EXDIR` | Directionality | Char | Perm | Variable Qualifier | Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL", "UPPER". |
| `EXFAST` | Fasting Status | Char | Perm | Record Qualifier | Indicator used to identify fasting status. Examples: "Y", "N". |
| `EXADJ` | Reason for Dose Adjustment | Char | Perm | Record Qualifier | Describes reason or explanation of why a dose is adjusted. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Trial epoch of the exposure record. Examples: "RUN-IN", "TREATMENT". |
| `EXSTDTC` | Start Date/Time of Treatment | Char | Exp | Timing | The date/time when administration of the treatment indicated by EXTRT and EXDOSE began. |
| `EXENDTC` | End Date/Time of Treatment | Char | Exp | Timing | The date/time when administration of the treatment indicated by EXTRT and EXDOSE ended. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, EXSTDTC should be copied to EXENDTC as the standard representation. |
| `EXSTDY` | Study Day of Start of Treatment | Num | Perm | Timing | Study day of EXSTDTC relative to DM.RFSTDTC. |
| `EXENDY` | Study Day of End of Treatment | Num | Perm | Timing | Study day of EXENDTC relative to DM.RFSTDTC. |
| `EXDUR` | Duration of Treatment | Char | Perm | Timing | Collected duration of administration. Used only if collected on the CRF and not derived from start and end date/times. |
| `EXTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when administration should occur. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EXTPTNUM and EXTPTREF. |
| `EXTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of EXTPT to aid in sorting. |
| `EXELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time relative to the planned fixed reference (EXTPTREF). This variable is useful where there are repetitive measures. Not a clock time. |
| `EXTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by EXELTM, EXTPTNUM, and EXTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL. |
| `EXRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by EXTPTREF. |
