# SDTM IG v3.4 Variables - MH Domain

**Domain Code:** `MH`

**Total Variables:** 27

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `MHSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `MHGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `MHREFID` | Reference ID | Char | Perm | Identifier | Internal or external medical history identifier. |
| `MHSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Medical History CRF page. |
| `MHTERM` | Reported Term for the Medical History | Char | Req | Topic | Verbatim or preprinted CRF term for the medical condition or event. |
| `MHMODIFY` | Modified Reported Term | Char | Perm | Synonym Qualifier | If MHTERM is modified to facilitate coding, then MHMODIFY will contain the modified text. |
| `MHDECOD` | Dictionary-Derived Term | Char | Perm | Synonym Qualifier | Dictionary-derived text description of MHTERM or MHMODIFY. Equivalent to the Preferred Term (PT in MedDRA). The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. |
| `MHEVDTYP` | Medical History Event Date Type | Char | Perm | Variable Qualifier | Specifies the aspect of the medical condition or event by which MHSTDTC and/or the MHENDTC is defined. Examples: "DIAGNOSIS", "SYMPTOMS", "RELAPSE", "INFECTION". |
| `MHCAT` | Category for Medical History | Char | Perm | Grouping Qualifier | Used to define a category of related records. Examples: "CARDIAC", "GENERAL". |
| `MHSCAT` | Subcategory for Medical History | Char | Perm | Grouping Qualifier | A further categorization of the condition or event. |
| `MHPRESP` | Medical History Event Pre-Specified | Char | Perm | Variable Qualifier | A value of "Y" indicates that this medical history event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms). |
| `MHOCCUR` | Medical History Occurrence | Char | Perm | Record Qualifier | Used when the occurrence of specific medical history conditions is solicited, to indicate whether ("Y"/"N") a medical condition (MHTERM) had ever occurred. Values are null for spontaneously reported events. |
| `MHSTAT` | Completion Status | Char | Perm | Record Qualifier | The status indicates that the prespecified question was not asked/answered. |
| `MHREASND` | Reason Medical History Not Collected | Char | Perm | Record Qualifier | Describes the reason why data for a prespecified condition was not collected. Used in conjunction with MHSTAT when value is "NOT DONE". |
| `MHBODSYS` | Body System or Organ Class | Char | Perm | Record Qualifier | Dictionary-derived. Body system or organ class that is involved in an event or measurement from a standard hierarchy (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables which may not necessarily be the primary SOC. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the assessment was made. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the medical history event. |
| `MHDTC` | Date/Time of History Collection | Char | Perm | Timing | Collection date and time of the medical history observation represented in ISO 8601 character format. |
| `MHSTDTC` | Start Date/Time of Medical History Event | Char | Perm | Timing | Start date/time of the medical history event represented in ISO 8601 character format. |
| `MHENDTC` | End Date/Time of Medical History Event | Char | Perm | Timing | End date/time of the medical history event. |
| `MHDY` | Study Day of History Collection | Num | Perm | Timing | Study day of medical history collection, measured as integer day. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
| `MHENRF` | End Relative to Reference Period | Char | Perm | Timing | Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `MHENRTPT` | End Relative to Reference Time Point | Char | Perm | Timing | Identifies the end of the event as being before or after the reference time point defined by variable MHENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `MHENTPT` | End Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by MHENRTPT. Examples: "2003-12-25", "VISIT 2". |
