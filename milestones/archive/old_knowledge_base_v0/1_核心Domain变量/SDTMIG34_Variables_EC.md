# SDTM IG v3.4 Variables - EC Domain

**Domain Code:** `EC`

**Total Variables:** 45

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `ECSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `ECGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `ECREFID` | Reference ID | Char | Perm | Identifier | Internal or external identifier (e.g., kit number, bottle label, vial identifier). |
| `ECSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page. |
| `ECLNKID` | Link ID | Char | Perm | Identifier | Identifier used to link related records across domains. |
| `ECLNKGRP` | Link Group ID | Char | Perm | Identifier | Identifier used to link related, grouped records across domains. |
| `ECTRT` | Name of Treatment | Char | Req | Topic | Name of the intervention treatment known to the subject and/or administrator. |
| `ECMOOD` | Mood | Char | Perm | Record Qualifier | Mode or condition of the record specifying whether the intervention (activity) is intended to happen or has happened. Values align with BRIDG pillars (e.g., scheduled context, performed context) and HL7 activity moods (e.g., intent, event). Examples: "SCHEDULED", "PERFORMED". |
| `ECCAT` | Category of Treatment | Char | Perm | Grouping Qualifier | Used to define a category of related ECTRT values. |
| `ECSCAT` | Subcategory of Treatment | Char | Perm | Grouping Qualifier | A further categorization of ECCAT values. |
| `ECPRESP` | Pre-Specified | Char | Perm | Variable Qualifier | Used when a specific intervention is prespecified. Values should be "Y" or null. |
| `ECOCCUR` | Occurrence | Char | Perm | Record Qualifier | Used to indicate whether a treatment occurred when information about the occurrence is solicited. ECOCCUR = "N" when a treatment was not taken, not given, or missed. |
| `ECREASOC` | Reason for Occur Value | Char | Perm | Record Qualifier | The reason for the value in --OCCUR. If --OCCUR = "N", this is the reason the exposure did not occur. |
| `ECDOSE` | Dose | Num | Exp | Record Qualifier | Amount of ECTRT when numeric. Not populated when ECDOSTXT is populated. |
| `ECDOSTXT` | Dose Description | Char | Perm | Record Qualifier | Amount of ECTRT when non-numeric. Dosing amounts or a range of dosing information collected in text form. Example: "200-400". Not populated when ECDOSE is populated. |
| `ECDOSU` | Dose Units | Char | Exp | Variable Qualifier | Units for ECDOSE, ECDOSTOT, or ECDOSTXT. |
| `ECDOSFRM` | Dose Form | Char | Exp | Variable Qualifier | Dose form for ECTRT. Examples: "TABLET", "LOTION". |
| `ECDOSFRQ` | Dosing Frequency per Interval | Char | Perm | Record Qualifier | Usually expressed as the number of repeated administrations of ECDOSE within a specific time period. Examples: "Q2H", "QD", "BID". |
| `ECDOSTOT` | Total Daily Dose | Num | Perm | Record Qualifier | Total daily dose of ECTRT using the units in ECDOSU. Used when dosing is collected as total daily dose. |
| `ECDOSRGM` | Intended Dose Regimen | Char | Perm | Record Qualifier | Text description of the intended schedule or regimen for the Intervention. Example: "TWO WEEKS ON", "TWO WEEKS OFF". |
| `ECROUTE` | Route of Administration | Char | Perm | Variable Qualifier | Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS". |
| `ECLOT` | Lot Number | Char | Perm | Record Qualifier | Lot number of the ECTRT product. |
| `ECLOC` | Location of Dose Administration | Char | Perm | Record Qualifier | Specifies location of administration. Example: "ARM", "LIP". |
| `ECLAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for anatomical location further detailing laterality of the intervention administration. Examples: "LEFT", "RIGHT". |
| `ECDIR` | Directionality | Char | Perm | Variable Qualifier | Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL", "UPPER". |
| `ECPORTOT` | Portion or Totality | Char | Perm | Variable Qualifier | Qualifier for anatomical location further detailing distribution (i.e., arrangement of, apportioning of). Examples: "ENTIRE", "SINGLE", "SEGMENT". |
| `ECFAST` | Fasting Status | Char | Perm | Record Qualifier | Indicator used to identify fasting status. Examples: "Y", "N". |
| `ECPSTRG` | Pharmaceutical Strength | Num | Perm | Record Qualifier | Amount of an active ingredient expressed quantitatively per dosage unit, per unit of volume, or per unit of weight, according to the pharmaceutical dose form. |
| `ECPSTRGU` | Pharmaceutical Strength Units | Char | Perm | Variable Qualifier | Unit for ECPSTRG. Examples: "mg/TABLET", "mg/mL". |
| `ECADJ` | Reason for Dose Adjustment | Char | Perm | Record Qualifier | Describes reason or explanation of why a dose is adjusted. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Trial epoch of the exposure as collected record. Examples: "RUN-IN", "TREATMENT". |
| `ECSTDTC` | Start Date/Time of Treatment | Char | Exp | Timing | The date/time when administration of the treatment indicated by ECTRT and ECDOSE began. |
| `ECENDTC` | End Date/Time of Treatment | Char | Exp | Timing | The date/time when administration of the treatment indicated by ECTRT and ECDOSE ended. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, ECSTDTC should be copied to ECENDTC as the standard representation. |
| `ECSTDY` | Study Day of Start of Treatment | Num | Perm | Timing | Study day of ECSTDTC relative to the sponsor-defined DM.RFSTDTC. |
| `ECENDY` | Study Day of End of Treatment | Num | Perm | Timing | Study day of ECENDTC relative to the sponsor-defined DM.RFSTDTC. |
| `ECDUR` | Duration of Treatment | Char | Perm | Timing | Collected duration of administration. Used only if collected on the CRF and not derived from start and end date/times. |
| `ECTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when administration should occur. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See ECTPTNUM and ECTPTREF. |
| `ECTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of ECTPT to aid in sorting. |
| `ECELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time relative to the planned fixed reference (ECTPTREF). This variable is useful where there are repetitive measures. Not a clock time. |
| `ECTPTREF` | Time Point Reference | Char | Perm | Timing | Name of the fixed reference point referred to by ECELTM, ECTPTNUM, and ECTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". |
| `ECRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by ECTPTREF. |
