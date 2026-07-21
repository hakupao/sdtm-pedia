# SDTM IG v3.4 Variables - HO Domain

**Domain Code:** `HO`

**Total Variables:** 28

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `HOSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `HOGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `HOREFID` | Reference ID | Char | Perm | Identifier | Internal or external healthcare encounter identifier. |
| `HOSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Healthcare Encounters CRF page. |
| `HOTERM` | Healthcare Encounter Term | Char | Req | Topic | Verbatim or preprinted CRF term for the healthcare encounter. |
| `HODECOD` | Dictionary-Derived Term | Char | Perm | Synonym Qualifier | Dictionary or sponsor-defined derived text description of HOTERM or the modified topic variable (HOMODIFY). |
| `HOCAT` | Category for Healthcare Encounter | Char | Perm | Grouping Qualifier | Used to define a category of topic-related values. |
| `HOSCAT` | Subcategory for Healthcare Encounter | Char | Perm | Grouping Qualifier | A further categorization of HOCAT values. |
| `HOPRESP` | Pre-Specified Healthcare Encounter | Char | Perm | Variable Qualifier | A value of "Y" indicates that this healthcare encounter event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms). |
| `HOOCCUR` | Healthcare Encounter Occurrence | Char | Perm | Record Qualifier | Used when the occurrence of specific healthcare encounters is solicited, to indicate whether an encounter occurred. Values are null for spontaneously reported events. |
| `HOSTAT` | Completion Status | Char | Perm | Record Qualifier | The status indicates that the prespecified question was not answered. |
| `HOREASND` | Reason Healthcare Encounter Not Done | Char | Perm | Record Qualifier | Describes the reason data for a prespecified event were not collected. Used in conjunction with HOSTAT when value is "NOT DONE". |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the healthcare encounter. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP". |
| `HODTC` | Date/Time of Event Collection | Char | Perm | Timing | Collection date and time of the healthcare encounter. |
| `HOSTDTC` | Start Date/Time of Healthcare Encounter | Char | Exp | Timing | Start date/time of the healthcare encounter (e.g., date of admission). |
| `HOENDTC` | End Date/Time of Healthcare Encounter | Char | Perm | Timing | End date/time of the healthcare encounter (e.g., date of discharge). |
| `HODY` | Study Day of Event Collection | Num | Perm | Timing | Study day of event collection relative to the sponsor-defined RFSTDTC. |
| `HOSTDY` | Study Day of Start of Encounter | Num | Perm | Timing | Study day of the start of the healthcare encounter relative to the sponsor-defined RFSTDTC. |
| `HOENDY` | Study Day of End of Healthcare Encounter | Num | Perm | Timing | Study day of the end of the healthcare encounter relative to the sponsor-defined RFSTDTC. |
| `HODUR` | Duration of Healthcare Encounter | Char | Perm | Timing | Collected duration of the healthcare encounter. Used only if collected on the CRF and not derived from the start and end date/times. Example: "P1DT2H" (for 1 day, 2 hours). |
| `HOSTRTPT` | Start Relative to Reference Time Point | Char | Perm | Timing | Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable --STTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `HOSTTPT` | Start Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by STRTPT. Examples: "2003-12-15", "VISIT 1". |
| `HOENRTPT` | End Relative to Reference Time Point | Char | Perm | Timing | Identifies the end of the event as being before or after the reference time point defined by variable HOENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `HOENTPT` | End Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by HOENRTPT. Examples: "2003-12-25", "VISIT 2". |
