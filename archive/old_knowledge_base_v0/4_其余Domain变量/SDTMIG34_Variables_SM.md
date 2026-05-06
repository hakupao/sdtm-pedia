# SDTM IG v3.4 Variables - SM Domain

**Domain Code:** `SM`

**Total Variables:** 10

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `SMSEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of subject records. Should be assigned to be consistent chronological order. |
| `MIDS` | Disease Milestone Instance Name | Char | Req | Topic | Name of the specific disease milestone. For types of disease milestones that can occur multiple times, the name will end with a sequence number. Example: "HYPO1". |
| `MIDSTYPE` | Disease Milestone Type | Char | Req | Record Qualifier | The type of disease milestone. Example: "HYPOGLYCEMIC EVENT". |
| `SMSTDTC` | Start Date/Time of Milestone | Char | Exp | Timing | Start date/time of milestone instance (if milestone is an intervention or event) or date of milestone (if Milestone is a finding). |
| `SMENDTC` | End Date/Time of Milestone | Char | Exp | Timing | End date/time of disease milestone instance. |
| `SMSTDY` | Study Day of Start of Milestone | Num | Exp | Timing | Study day of start of disease milestone instance, relative to the sponsor-defined RFSTDTC. |
| `SMENDY` | Study Day of End of Milestone | Num | Exp | Timing | Study day of end of disease milestone instance, relative to the sponsor-defined RFSTDTC. |
