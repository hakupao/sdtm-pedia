# SDTM IG v3.4 Variables - TD Domain

**Domain Code:** `TD`

**Total Variables:** 9

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `TDORDER` | Sequence of Planned Assessment Schedule | Num | Req | Timing | A number given to ensure ordinal sequencing of the planned assessment schedules within a trial. |
| `TDANCVAR` | Anchor Variable Name | Char | Req | Timing | A reference to the date variable name that provides the start point from which the planned disease assessment schedule is measured. This must be a referenced from the ADaM ADSL dataset (e.g., "ANCH1DT"). Note: TDANCVAR will contain the name of a reference date variable. |
| `TDSTOFF` | Offset from the Anchor | Char | Req | Timing | A fixed offset from the date provided by the variable referenced in TDANCVAR. This is used when the timing of planned cycles does not start on the exact day referenced in the variable indicated in TDANCVAR. The value of this variable will be either zero or a positive value and will be represented in ISO 8601 character format. |
| `TDTGTPAI` | Planned Assessment Interval | Char | Req | Timing | The planned interval between disease assessments represented in ISO 8601 character format. |
| `TDMINPAI` | Planned Assessment Interval Minimum | Char | Req | Timing | The lower limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format. |
| `TDMAXPAI` | Planned Assessment Interval Maximum | Char | Req | Timing | The upper limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format. |
| `TDNUMRPT` | Maximum Number of Actual Assessments | Num | Req | Record Qualifier | This variable must represent the maximum number of actual assessments for the analysis that this disease assessment schedule describes. In a trial where the maximum number of assessments is not defined explicitly in the protocol (e.g., assessments occur until death), TDNUMRPT should represent the maximum number of disease assessments that support the efficacy analysis encountered by any subject across the trial at that point in time. |
