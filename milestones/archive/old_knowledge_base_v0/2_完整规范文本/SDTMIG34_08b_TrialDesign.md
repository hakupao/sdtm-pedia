# SDTMIG v3.4 --- Trial Design Model Datasets — Part 2

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 2/2 — 7.3-7.5: Schedule (TV, TD, TM), Eligibility (TI, TS), Modeling Guide
> **Original:** `SDTMIG34_08_TrialDesign.md`
> **Related:** `SDTMIG34_08a_TrialDesign.md`

---

### 7.3 Schedule for Assessments (TV, TD, and TM)

This section contains the Trial Design (TD) datasets that describe:
- The protocol-defined planned schedule of subject encounters at the healthcare facility where the study is being conducted (Section 7.3.1, Trial Visits (TV))
- The planned schedule of efficacy assessments related to the disease under study (Section 7.3.2, Trial
Disease Assessments (TD))
- The things (events, interventions, or findings) which, if and when they happen, are the occasion for assessments planned in the protocol (Section 7.3.3, Trial Disease Milestones (TM))
The Trial Visits (TV) and TD datasets provide the planned scheduling of assessments to which a subject’s actual visits and disease assessments can be compared.

#### 7.3.1 Trial Visits (TV)

##### TV – Description/Overview
A trial design domain that contains the planned order and number of visits in the study within each arm.

Visits are defined as "clinical encounters" and are described using the timing variables VISIT, VISITNUM, and VISITDY.

Protocols define visits in order to describe assessments and procedures that are to be performed at the visits.

##### TV – Specification
tv.xpt, Trial Visits — Trial Design. One record per planned Visit per Arm, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |
| --- | --- | --- | --- | --- | --- | --- |
| STUDYID | Study Identifier | Char |  | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char |  | Identifier | Two-character abbreviation for the domain. | Req |
| VISITNUM | Visit Number | Num |  | Topic | Clinical encounter number. Numeric version of VISIT, used for sorting. | Req |
| VISIT | Visit Name | Char |  | Synonym Qualifier | Description of clinical encounter. This is often defined in the protocol. Used in addition to VISITNUM and/or VISITDY as a text description of the clinical encounter. | Req |
| VISITDY | Planned Study Day of Visit | Num |  | Timing | Planned study day of VISIT. Due to its sequential nature, used for sorting. | Perm |
| ARMCD | Planned Arm Code | Char | * | Record Qualifier | 1. ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20.<br>2. If the timing of visits for a trial does not depend on which arm a subject is in, then ARMCD should be null. | Exp |
| ARM | Description of Planned Arm | Char | * | Synonym Qualifier | 1. Name given to an arm or treatment group.<br>2. If the timing of visits for a trial does not depend on which arm a subject is in, then Arm should be left blank. | Perm |
| TVSTRL | Visit Start Rule | Char |  | Rule | Rule describing when the visit starts, in relation to the sequence of elements. | Req |
| TVENRL | Visit End Rule | Char |  | Rule | Rule describing when the visit ends, in relation to the sequence of elements. | Perm |

1. In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

##### TV – Assumptions
1. Although the general structure of the Trial Visits (TV) dataset is "One Record per Planned Visit per Arm," for many clinical trials-particularly blinded clinical trials-the schedule of visits is the same for all arms, and the structure of the TV dataset will be "One Record per Planned Visit." If the schedule of visits is the same for all arms, ARMCD should be left blank for all records in the TV dataset. For trials with trial visits that are different for different arms (e.g., Example Trial 7 in Section 7.2.1, Trial Arms), ARMCD and ARM should be populated for all records. If some visits are the same for all arms, and some visits differ by arm, then ARMCD and ARM should be populated for all records, to ensure clarity, even though this will mean creating near-duplicate records for visits that are the same for all arms.
2. A visit may start in one element and end in another. This means that a visit may start in one epoch and end in another. For example, if one of the activities planned for a visit is the administration of the first dose of study drug, the visit might start in the screen epoch and end in a treatment epoch.
3. TVSTRL describes the scheduling of the visit and should reflect the wording in the protocol. In many trials, all visits are scheduled relative to the study's day 1 (RFSTDTC). In such trials, it is useful to include VISITDY, which is, in effect, a special case representation of TVSTRL.
4. Note that there is a subtle difference between the following 2 examples. In the first case, if visit 3 were delayed for some reason, visit 4 would be unaffected. In the second case, a delay to visit 3 would result in visit 4 being delayed as well.

   a. Case 1: Visit 3 starts 2 weeks after RFSTDTC. Visit 4 starts 4 weeks after RFSTDTC.

   b. Case 2: Visit 3 starts 2 weeks after RFSTDTC. Visit 4 starts 2 weeks after visit 3.

5. Many protocols do not give any information about visit ends because visits are assumed to end on the same day they start. In such a case, TVENRL may be left blank to indicate that the visit ends on the same day it starts. Care should be taken to assure that this is appropriate; common practice may be to record data collected over more than 1 day as occurring within a single visit. Screening visits may be particularly prone to collection of data over multiple days. The examples for this domain show how TVENRL could be populated.
6. The values of VISITNUM in the TV dataset are the valid values of VISITNUM for planned visits. Any values of VISITNUM that appear in subject-level datasets that are not in the TV dataset are assumed to correspond to unplanned visits. This applies, in particular, to the subject-level dataset; see Section 5.5, Subject Visits, for additional information about handling unplanned visits. If a subject-level dataset includes both VISITNUM and VISIT, then records that include values of VISITNUM that appear in the TV dataset should also include the corresponding values of VISIT from the TV dataset.


##### TV – Examples
###### Example 1

The following diagram represents visits as numbered "flags" with visit numbers. Each flag has 2 supports, one at the beginning of the visit and the other at the end of the visit. Note that visits 2 and 3 span epoch transitions. In other words, the transition event that marks the beginning of the run-in epoch (confirmation of eligibility) occurs during visit 2, and the transition event that marks the beginning of the treatment epoch (the first dose of study drug) occurs during visit 3.

Two TV datasets are shown for this trial. The first shows a somewhat idealized situation, where the protocol has provided specific timings for the visits. The second shows a more common situation, where the timings have been described only loosely.

tv.xpt

| Row | STUDYID | DOMAIN | VISITNUM | TVSTRL | TVENRL |
| --- | --- | --- | --- | --- | --- |
| 1 | EX1 | TV | 1 | Start of Screen Epoch | 1 hour after start of Visit |
| 2 | EX1 | TV | 2 | 30 minutes before end of Screen Epoch | 30 minutes after start of Run-in Epoch |
| 3 | EX1 | TV | 3 | 30 minutes before end of Run-in Epoch | 1 hour after start of Treatment Epoch |
| 4 | EX1 | TV | 4 | 1 week after start of Treatment Epoch | 1 hour after start of Visit |
| 5 | EX1 | TV | 5 | 2 weeks after start of Treatment Epoch | 1 hour after start of Visit |

tv.xpt

| Row | STUDYID | DOMAIN | VISITNUM | TVSTRL | TVENRL |
| --- | --- | --- | --- | --- | --- |
| 1 | EX1 | TV | 1 | Start of Screen Epoch |  |
| 2 | EX1 | TV | 2 | On the same day as, but before, the end of the Screen Epoch | On the same day as, but after, the start of the Run-in Epoch |
| 3 | EX1 | TV | 3 | On the same day as, but before, the end of the Run-in Epoch | On the same day as, but after, the start of the Treatment Epoch |
| 4 | EX1 | TV | 4 | 1 week after start of Treatment Epoch |  |
| 5 | EX1 | TV | 5 | 2 weeks after start of Treatment Epoch | At Trial Exit |

Although the start and end rules in this example reference the starts and ends of epochs, the start and end rules of some visits for trials with epochs that span multiple elements will need to reference elements rather than epochs. When an arm includes repetitions of the same element, it may be necessary to use TAETORD as well as an element name to specify when a visit is to occur.

##### 7.3.1.1 Trial Visits Issues

###### Identifying Trial Visits

In general, a trial's visits are defined in its protocol. The term "visit" reflects the fact that data in outpatient studies is usually collected during a physical visit by the subject to a clinic. Sometimes a trial visit defined by the protocol may not correspond to a physical visit. It may span multiple physical visits, as when screening data is collected over several clinic visits but recorded under one TV name (VISIT) and number (VISITNUM). A trial visit also may represent only a portion of an extended physical visit, as when a trial of in-patients collects data under multiple trial visits for a single hospital admission.

Diary data and other data collected outside a clinic may not fit the usual concept of a trial visit, but the planned times of collection of such data may be described as "visits" in the TV dataset if desired.

###### Trial Visit Rules

Visit start rules are different from element start rules in that they usually describe when a visit should occur; element start rules describe the moment at which an element is considered to start. There are usually gaps between visits, periods of time that do not belong to any visit, so it is usually not necessary to identify the moment when one visit stops and another starts. However, some trials of hospitalized subjects may divide time into visits in a manner more like that used for elements, and a transition event may need to be defined in such cases.

Visit start rules are usually expressed relative to the start or end of an element or epoch (e.g., "1-2 hours before end of First Wash-out", "8 weeks after end of 2nd Treatment Epoch"). Note that the visit may or may not occur during the element used as the reference for the visit start rule. For example, a trial with elements based on treatment of disease episodes might plan a visit 6 months after the start of the first treatment period, regardless of how many disease episodes have occurred.

Visit end rules are similar to element end rules, describing when a visit should end. They may be expressed relative to the start or end of an element or epoch, or relative to the start of the visit.

The timings of visits relative to elements may be expressed in terms that cannot be easily quantified. For instance, a protocol might instruct that at a baseline visit the subject be randomized, given the study drug, and instructed to take the first dose of study drug X at bedtime that night. This baseline visit is thus started and ended before the start of the treatment epoch, but we don't know how long before the start of the treatment epoch the visit will occur. The visit start rule might contain the value "On the day of, but before, the start of the Treatment Epoch".

###### Visit Schedules Expressed with Ranges

Ranges may be used to describe the planned timing of visits (e.g., 12-16 days after the start of 2nd Element), but this is different from the "windows" that may be used in selecting data points to be included in an analysis associated with that visit. For example, although visit 2 was planned for 12-16 days after the start of treatment, data collected 10-18 days after the start of treatment might be included in a visit 1 analysis. The 2 ranges serve different purposes.

###### Contingent Visits

Some data collection is contingent on the occurrence of a "trigger" event or disease milestone (see Section 7.3.3, Trial Disease Milestones (TM)). When such planned data collection involves an additional clinic visit, a "contingent" visit may be included in the TV table, with a rule that describes the circumstances under which it will take place. Because values of VISITNUM must be assigned to all records in the TV dataset, a contingent visit included in the TV dataset must have a VISITNUM, but the VISITNUM value might not be a "chronological" value, due to the uncertain timing of a contingent visit. If contingent visits are not included in the TV dataset, then they would be treated as unplanned visits in the Subject Visits (SV) domain (see Section 6.2.8, Subject Visits).

#### 7.3.2 Trial Disease Assessments (TD)

##### TD – Description/Overview
A trial design domain that provides information on the protocol-specified disease assessment schedule, to be used for comparison with the actual occurrence of the efficacy assessments in order to determine whether there was good compliance with the schedule.

##### TD – Specification
`td.xpt`, Trial Disease Assessments - Trial Design. One record per planned constant assessment period, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |
| --- | --- | --- | --- | --- | --- | --- |
| STUDYID | Study Identifier | Char |  | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | TD | Identifier | Two-character abbreviation for the domain. | Req |
| TDORDER | Sequence of Planned Assessment Schedule | Num |  | Timing | A number given to ensure ordinal sequencing of the planned assessment schedules within a trial. | Req |
| TDANCVAR | Anchor Variable Name | Char |  | Timing | A reference to the date variable name that provides the start point from which the planned disease assessment schedule is measured. This must be a variable from the ADaM ADSL dataset (e.g., `ANCH1DT`). Note: `TDANCVAR` will contain the name of a reference date variable. | Req |
| TDSTOFF | Offset from the Anchor | Char | ISO 8601 duration | Timing | A fixed offset from the date provided by the variable referenced in `TDANCVAR`. This is used when the timing of planned cycles does not start on the exact day referenced in the variable indicated in `TDANCVAR`. The value of this variable will be either zero or a positive value and will be represented in ISO 8601 character format. | Req |
| TDTGTPAI | Planned Assessment Interval | Char | ISO 8601 duration | Timing | The planned interval between disease assessments represented in ISO 8601 character format. | Req |
| TDMINPAI | Planned Assessment Interval Minimum | Char | ISO 8601 duration | Timing | The lower limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format. | Req |
| TDMAXPAI | Planned Assessment Interval Maximum | Char | ISO 8601 duration | Timing | The upper limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format. | Req |
| TDNUMRPT | Maximum Number of Actual Assessments | Num |  | Record Qualifier | This variable must represent the maximum number of actual assessments for the analysis that this disease assessment schedule describes. In a trial where the maximum number of assessments is not defined explicitly in the protocol (e.g., assessments occur until death), `TDNUMRPT` should represent the maximum number of disease assessments that support the efficacy analysis encountered by any subject across the trial at that point in time. | Req |

1 In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

##### TD – Assumptions
1. The purpose of the Trial Disease Assessments (TD) domain is to provide information on planned scheduling of disease assessments when the scheduling of disease assessments is not necessarily tied to the scheduling of visits. In oncology studies, good compliance with the disease-assessment schedule is essential to reduce the risk of "assessment time bias." The TD domain makes possible an evaluation of assessment time bias from the SDTM, in particular for studies with progression-free survival (PFS) endpoints. TD has limited utility within oncology and was developed specifically with RECIST in mind and where an assessment-time bias analysis is appropriate. It is understood that extending this approach to Cheson and other criteria may not be appropriate or may pose difficulties. It is also understood that this approach may not be necessary in non-oncology studies, although it is available for use if appropriate.
2. A planned schedule of assessments will have a defined start point; the `TDANCVAR` variable is used to identify the variable in the ADaM subject-level dataset (ADSL) that holds the anchor date. By default, the anchor variable for the first pattern is `ANCH1DT`. An anchor date must be provided for each pattern of assessments, and each anchor variable must exist in ADSL. `TDANCVAR` is therefore a Required variable. Anchor date variable names should adhere to ADaM variable naming conventions (e.g., `ANCH1DT`, `ANCH2DT`). One anchor date may be used to anchor more than one pattern of disease assessments. When that is the case, the appropriate offset for the start of a subsequent pattern, represented as an ISO 8601 duration value, should be provided in the `TDSTOFF` variable.
3. The `TDSTOFF` variable is used in conjunction with the anchor date value from the anchor date variable identified in `TDANCVAR`. If the pattern of disease assessments does not start exactly on a date collected on the CRF, this variable will represent the offset between the anchor date value and the start date of the pattern of disease assessments. This may be a positive or zero interval value represented in ISO 8601 format.
4. A pattern of assessments consists of a series of intervals of equal duration, each followed by an assessment. Thus, the first assessment in a pattern is planned to occur at the anchor date, given by the variable named in `TDANCVAR`, plus the offset (`TDSTOFF`) plus the target assessment interval (`TDTGTPAI`). A baseline evaluation is usually not preceded by an interval, and would therefore not be considered part of an assessment pattern.
5. This domain should not be created when the disease assessment schedule may vary for individual subjects (e.g., when completion of the first phase of a study is event-driven).

##### TD – Examples
*Example 1*

This example shows a study where the disease assessment schedule changes over the course of the study. In this example, there are 3 distinct disease-assessment schedule patterns. A single anchor date variable (`TDANCVAR`) provides the anchor date for each pattern. The offset variable (`TDSTOFF`), used in conjunction with the anchor date variable, provides the start point of each pattern of assessments.

- The first disease-assessment schedule pattern starts at the reference start date, identified in the ADSL `ANCH1DT` variable, and repeats every 8 weeks for a total of 6 repeated assessments (i.e., week 8, week 16, week 24, week 32, week 40, week 48). Note that there is an upper and lower limit around the planned disease assessment target where the first assessment (8 weeks) could occur as early as day 53 and as late as week 9. This upper and lower limit (-3 days, +1 week) would be applied to all assessments during that pattern.
- The second disease assessment schedule starts from week 48 and repeats every 12 weeks for a total of 4 repeats (i.e., week 60, week 72, week 84, week 96), with respective upper and lower limits of -1 week and +1 week.
- The third disease assessment schedule starts from week 96 and repeats every 24 weeks (week 120, week 144, and so on), with respective upper and lower limits of -1 week and +1 week, for an indefinite length of time. The preceding schematic shows that, for the third pattern, assessments will occur until disease progression; this therefore leaves the pattern open-ended. However, when data is included in an analysis, the total number of repeats can be identified and the highest number of repeat assessments for any subject in that pattern must be recorded in the `TDNUMRPT` variable on the final pattern record.

`td.xpt`

| Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | TD | 1 | ANCH1DT | P0D | P8W | P53D | P9W | 6 |
| 2 | ABC123 | TD | 2 | ANCH1DT | P48W | P12W | P11W | P13W | 4 |
| 3 | ABC123 | TD | 3 | ANCH1DT | P96W | P24W | P23W | P25W | 12 |

*Example 2*

This example shows a crossover study, where subjects are given the period 1 treatment according to the first disease-assessment schedule until disease progression, then there is a rest period of 28 days prior to the start of period 2 treatment (i.e., re-baseline for period 2). The subjects are then given the period 2 treatment according to the second disease assessment schedule until disease progression. This example also shows how two different reference or anchor dates can be used.

- The Rest element is not represented as a row in the TD dataset, since no disease assessments occur during the Rest. Note that although the Rest epoch in this example is not important for TD, it is important that it is represented in other trial design datasets.
- Row 1 shows the disease assessment schedule for the first treatment period. The diagram above shows that this schedule repeats until disease progression. After the trial ended, the maximum number of repeats in this schedule was determined to be 6, so that is the value in `TDNUMRPT` for this schedule.
- Row 2 shows the disease assessment schedule for the second period. The pattern starts on the date identified in the ADSL variable `ANCH2DT` and repeats every 8 weeks with respective upper and lower limits of -1 week and +1 week. The maximum number of repeats that occurred on this schedule was 4.

`td.xpt`

| Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | TD | 1 | ANCH1DT | P0D | P8W | P53D | P9W | 6 |
| 2 | ABC123 | TD | 2 | ANCH2DT | P0D | P8W | P53D | P9W | 4 |

*Example 3*

This example shows a study where subjects are randomized to standard treatment or an experimental treatment. The subjects who are randomized to standard treatment are given the option to receive experimental treatment after they end the standard treatment (e.g., due to disease progression on standard treatment). In the randomized treatment epoch, the disease assessment schedule changes over the course of the study. At the start of the extension treatment epoch, subjects are re-baselined, i.e., an extension baseline disease assessment is performed and the disease assessment schedule is restarted.

In this example, there are 3 distinct disease-assessment schedule patterns:

- The first disease-assessment schedule pattern starts at the reference start date, identified in the ADSL `ANCH1DT` variable, and repeats every 8 weeks for a total of 6 repeats (i.e., week 8, week 16, week 24, week 32, week 40, week 48), with respective upper and lower limits of -3 days and +1 week.
- The second disease assessment schedule starts from week 48 and repeats every 12 weeks (week 60, week 72, etc.), with respective upper and lower limits of -1 week and +1 week, for an indefinite length of time. The preceding schematic shows that, for the second pattern, assessments will occur until disease progression; this therefore leaves the pattern open-ended.
- The third disease assessment schedule starts at the extension reference start date, identified in the ADSL `ANCH2DT` variable, from week 96 and repeats every 24 weeks (week 120, week 144, etc.), with respective upper and lower limits of -1 week and +1 week, for an indefinite length of time. The schematic shows that, for the third pattern, assessments will occur until disease progression; this therefore leaves the pattern open-ended.

For open-ended patterns, the total number of repeats can be identified when the data analysis is performed; the highest number of repeat assessments for any subject in that pattern must be recorded in the `TDNUMRPT` variable on the final pattern record.

`td.xpt`

| Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | TD | 1 | ANCH1DT | P0D | P8W | P53D | P9W | 6 |
| 2 | ABC123 | TD | 2 | ANCH1DT | P48W | P12W | P11W | P13W | 17 |
| 3 | ABC123 | TD | 3 | ANCH2DT | P0D | P12W | P11W | P13W | 17 |

#### 7.3.3 Trial Disease Milestones (TM)

##### TM – Description/Overview
A trial design domain that is used to describe disease milestones, which are observations or activities anticipated to occur in the course of the disease under study, and which trigger the collection of data.

##### TM – Specification
`tm.xpt`, Trial Disease Milestones - Trial Design. One record per Disease Milestone type, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |
| --- | --- | --- | --- | --- | --- | --- |
| STUDYID | Study Identifier | Char |  | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | TM | Identifier | Two-character abbreviation for the domain, which must be TM. | Req |
| MIDSTYPE | Disease Milestone Type | Char |  | Topic | The type of disease milestone. Example: `"HYPOGLYCEMIC EVENT"`. | Req |
| TMDEF | Disease Milestone Definition | Char |  | Variable Qualifier | Definition of the disease milestone. | Req |
| TMRPT | Disease Milestone Repetition Indicator | Char | (NY) | Record Qualifier | Indicates whether this is a disease milestone that can occur only once (`"N"`) or a type of disease milestone that can occur multiple times (`"Y"`). | Req |

1 In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

##### TM – Assumptions
1. Disease milestones may be things that would be expected to happen before the study, or things that are anticipated to happen during the study. The occurrence of disease milestones for particular subjects are represented in the Subject Disease Milestones (SM) dataset.
2. The Trial Disease Milestones (TM) dataset contains a record for each type of disease milestone. The disease milestone is defined in `TMDEF`.

##### TM – Examples
*Example 1*

In this diabetes study, initial diagnosis of diabetes and the hypoglycemic events that occur during the trial have been identified as disease milestones of interest.

- Row 1 shows that the initial diagnosis is given the `MIDSTYPE` of `"DIAGNOSIS"` and is defined in `TMDEF`. It is not repeating and occurs only once.
- Row 2 shows that hypoglycemic events are given the `MIDSTYPE` of `"HYPOGLYCEMIC EVENT"` and a definition in `TMDEF`. For an actual study, the definition would be expected to include a particular threshold level, rather than the text "threshold level" used in this example. A subject may experience multiple hypoglycemic events, as indicated by `TMRPT = "Y"`.

`tm.xpt`

| Row | STUDYID | DOMAIN | MIDSTYPE | TMDEF | TMRPT |
| --- | --- | --- | --- | --- | --- |
| 1 | XYZ | TM | DIAGNOSIS | Initial diagnosis of diabetes, the first time a physician told the subject they had diabetes | N |
| 2 | XYZ | TM | HYPOGLYCEMIC EVENT | Hypoglycemic Event, the occurrence of a glucose level below (threshold level) | Y |
### 7.4 Trial Eligibility and Summary (TI and TS)

This section contains the Trial Design (TD) datasets that describe:
- Subject eligibility criteria for trial participation (Section 7.4.1, Trial Inclusion/Exclusion Criteria (TI))
- The characteristics of the trial (Section 7.4.2, Trial Summary (TS))
The TI and TS datasets are tabular synopses of parts of the study protocol.


#### 7.4.1 Trial Inclusion/Exclusion Criteria (TI)

##### TI – Proposed Removal of Variable TIRL
The variable `TIRL` was included in the Trial Inclusion/Exclusion Criteria (TI) domain in anticipation of developing a way to represent eligibility criteria in a computer-executable manner. However, such a method has not been developed, and it is not clear that an SDTM dataset would be the best place to represent such a computer-executable representation.

##### TI – Description/Overview
A trial design domain that contains one record for each of the inclusion and exclusion criteria for the trial. This domain is not subject oriented.

TI contains all the inclusion and exclusion criteria for the trial, and thus provides information that may not be present in the subject-level data on inclusion and exclusion criteria. The IE domain, described in Section 6.3.4, Inclusion/Exclusion Criteria Not Met, contains records only for inclusion and exclusion criteria that subjects did not meet.

##### TI – Specification
`ti.xpt`, Trial Inclusion/Exclusion Criteria - Trial Design. One record per I/E criterion, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |
| --- | --- | --- | --- | --- | --- | --- |
| STUDYID | Study Identifier | Char |  | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | TI | Identifier | Two-character abbreviation for the domain. | Req |
| IETESTCD | Incl/Excl Criterion Short Name | Char | * | Topic | Short name `IETEST`. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in `IETESTCD` cannot be longer than 8 characters, nor can it start with a number (e.g., `"1TEST"` is not valid). `IETESTCD` cannot contain characters other than letters, numbers, or underscores. The prefix `"IE"` is used to ensure consistency with the IE domain. | Req |
| IETEST | Inclusion/Exclusion Criterion | Char | * | Synonym Qualifier | Full text of the inclusion or exclusion criterion. The prefix `"IE"` is used to ensure consistency with the IE domain. | Req |
| IECAT | Inclusion/Exclusion Category | Char | (IECAT) | Grouping Qualifier | Used for categorization of the inclusion or exclusion criteria. | Req |
| IESCAT | Inclusion/Exclusion Subcategory | Char | * | Grouping Qualifier | A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or to categorize as major or minor exceptions. Examples: `"MAJOR"`, `"MINOR"`. | Perm |
| TIRL | Inclusion/Exclusion Criterion Rule | Char |  | Rule | Rule that expresses the criterion in computer-executable form. See Assumption 4. | Perm |
| TIVERS | Protocol Criteria Versions | Char |  | Record Qualifier | The number of this version of the Inclusion/Exclusion criteria. May be omitted if there is only 1 version. | Perm |

1 In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

##### TI – Assumptions
1. If inclusion or exclusion criteria were amended during the trial, then each complete set of criteria must be included in the TI domain. `TIVERS` is used to distinguish between the versions.
2. Protocol version numbers should be used to identify criteria versions, although there may be more versions of the protocol than versions of the inclusion or exclusion criteria. For example, a protocol might have versions 1, 2, 3, and 4, but if the inclusion or exclusion criteria in version 1 were unchanged through versions 2 and 3, and changed only in version 4, then there would be 2 sets of inclusion or exclusion criteria in TI: one for version 1 and one for version 4.
3. Individual criteria do not have versions. If a criterion changes, it should be treated as a new criterion, with a new value for `IETESTCD`. If criteria have been numbered and values of `IETESTCD` are generally of the form `INCL00n` or `EXCL00n`, and new versions of a criterion have not been given new numbers, separate values of `IETESTCD` might be created by appending letters (e.g., `INCL003A`, `INCL003B`).
4. `IETEST` contains the text of the inclusion or exclusion criterion. However, because entry criteria are rules, the variable `TIRL` has been included in anticipation of the development of computer-executable rules.
5. If a criterion text is <200 characters, it goes in `IETEST`; if the text is >200 characters, put meaningful text in `IETEST` and describe the full text in the study metadata. See Section 4.5.3.1, Test Name (`--TEST`) Greater than 40 Characters, for further information.

##### TI – Examples
*Example 1*

This example shows records for a trial with 2 versions of inclusion or exclusion criteria.

- Rows 1-3 show the 2 inclusion criteria and 1 exclusion criterion for version 1 of the protocol.
- Rows 4-6 show the inclusion or exclusion criteria for version 2.2 of the protocol, which changed the minimum age for entry from 21 to 18.

`ti.xpt`

| Row | STUDYID | DOMAIN | IETESTCD | IETEST | IECAT | TIVERS |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | TI | INCL01 | Has disease under study | INCLUSION | 1 |
| 2 | XYZ | TI | INCL02 | Age 21 or greater | INCLUSION | 1 |
| 3 | XYZ | TI | EXCL01 | Pregnant or lactating | EXCLUSION | 1 |
| 4 | XYZ | TI | INCL01 | Has disease under study | INCLUSION | 2.2 |
| 5 | XYZ | TI | INCL02A | Age 18 or greater | INCLUSION | 2.2 |
| 6 | XYZ | TI | EXCL01 | Pregnant or lactating | EXCLUSION | 2.2 |

#### 7.4.2 Trial Summary (TS)

##### TS – Description/Overview
A trial design domain that contains one record for each trial summary characteristic. This domain is not subject oriented.
The Trial Summary (TS) dataset allows the sponsor to submit a summary of the trial in a structured format. Each record in the TS dataset contains the value of a parameter, a characteristic of the trial. For example, TS is used to record basic information about the study such as trial phase, protocol title, and trial objectives. The TS dataset contains information about the planned and actual trial characteristics.

##### TS – Specification
`ts.xpt`, Trial Summary - Trial Design. One record per trial summary parameter value, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |
| --- | --- | --- | --- | --- | --- | --- |
| STUDYID | Study Identifier | Char |  | Identifier | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | TS | Identifier | Two-character abbreviation for the domain. | Req |
| TSSEQ | Sequence Number | Num |  | Identifier | Sequence number given to ensure uniqueness within a parameter. Allows inclusion of multiple records for the same `TSPARMCD`. | Req |
| TSGRPID | Group ID | Char |  | Identifier | Used to tie together a group of related records. | Perm |
| TSPARMCD | Trial Summary Parameter Short Name | Char | (TSPARMCD) | Topic | `TSPARMCD` (the companion to `TSPARM`) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that `TSPARMCD` will need to serve as variable names. Examples: `"AGEMIN"`, `"AGEMAX"`. | Req |
| TSPARM | Trial Summary Parameter | Char | (TSPARM) | Synonym Qualifier | Term for the trial summary parameter. The value in `TSPARM` cannot be longer than 40 characters. Examples: `"Planned Minimum Age of Subjects"`, `"Planned Maximum Age of Subjects"`. | Req |
| TSVAL | Parameter Value | Char | * | Result Qualifier | Value of `TSPARM`. Example: `"ASTHMA"` when `TSPARM` value is `"Trial Indication"`. `TSVAL` can only be null when `TSVALNF` is populated. Text over 200 characters can be added to additional columns `TSVAL1-TSVALn`. See Assumption 8. | Exp |
| TSVALNF | Parameter Value Null Flavor | Char | ISO 21090 NullFlavor | Result Qualifier | Null flavor for the value of `TSPARM`, to be populated only if `TSVAL` is null. | Perm |
| TSVALCD | Parameter Value Code | Char | * | Result Qualifier | This is the code of the term in `TSVAL`. For example, `"6CW7F3G59X"` is the code for gabapentin; `"C49488"` is the code for `Y`. The length of this variable can be longer than 8 to accommodate the length of the external terminology. | Exp |
| TSVCDREF | Name of the Reference Terminology | Char | (DICTNAM) | Result Qualifier | The name of the reference terminology from which `TSVALCD` is taken. For example: CDISC CT, SNOMED, ISO 8601. | Exp |
| TSVCDVER | Version of the Reference Terminology | Char |  | Result Qualifier | The version number of the reference terminology, if applicable. | Exp |

1 In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

##### TS – Assumptions
1. The intent of this dataset is to provide a summary of trial information. This is not subject-level data.
2. Recipients may specify their requirements for which trial summary parameters should be included under which circumstances. For example, the US FDA includes such information in their Study Data Technical Conformance Guide.
3. The order of parameters in the examples of TS datasets should not be taken as a requirement. There are no requirements or expectations about the order of parameters within the TS dataset.
4. The method for treating text >200 characters in TS is similar to that used for the Comments (CO) special-purpose domain (Section 5.1, Comments). If `TSVAL` is >200 characters, then it should be split into multiple variables, `TSVAL-TSVALn`. See Section 4.5.3.2, Text Strings Greater than 200 Characters in Other Variables.
5. A list of values for `TSPARM` and `TSPARMCD` can be found in CDISC Controlled Terminology, available at [https://www.cancer.gov/research/resources/terminology/cdisc](https://www.cancer.gov/research/resources/terminology/cdisc).
6. Controlled terminology for `TSPARM` is extensible. The meaning of any added parameters should be explained in the metadata for the TS dataset.
7. For a particular trial summary parameter, responses (values in `TSVAL`) may be numeric, datetimes or amounts of time represented in ISO 8601 format, or text. For some parameters, textual responses may be taken from controlled terminology; for others, responses may be free text.
8. For some trial summary parameters, CDISC Controlled Terminology includes codelists for use with `TSVAL`. The associations between trial summary parameters and response codelists are in the TS codetable, available at [https://www.cdisc.org/standards/terminology/controlled-terminology](https://www.cdisc.org/standards/terminology/controlled-terminology). Recipients may also specify controlled terminology for `TSVAL`. These specifications may be for trial summary parameters for which there is no CDISC Controlled Terminology or they may replace CDISC Controlled Terminology for a trial summary parameter. For example, the US FDA Data Standards Catalog includes terminologies to be used for certain trial summary parameters.
9. There is a code value for `TSVALCD` only when there is controlled terminology for `TSVAL`. For example, when `TSPARMCD = "PLANSUB"` (Planned Number of Subjects) or `TSPARMCD = "TITLE"` (Trial Title), then `TSVALCD` will be null.
10. `TSVALNF` contains a "null flavor," a value that provides additional coded information when `TSVAL` is null. For example, for `TSPARM = "AGEMAX"` (Planned Maximum Age of Subjects), there is no value if a study does not specify a maximum age. In this case, the appropriate null flavor is `"PINF"`, which stands for "positive infinity." In a clinical pharmacology study conducted in healthy volunteers for a drug where indications are not yet established, the appropriate null flavor for `TSPARM = "INDIC"` (Trial Disease/Condition Indication) would be `"NA"` (i.e., not applicable). `TSVALNF` can also be used in a case where the value of a particular parameter is unknown.
11. Some codelists used for `TSVAL` include terms which are also null flavors. For example, the Pharmaceutical Dosage Form codelist includes the values `"UNKNOWN"` and `"NOT APPLICABLE"`. In such cases, `TSVAL` should have the term from the codelist and `TSVALNF` should be null.
12. For some trials, there will be multiple records in the TS dataset for a single parameter. For example, a trial that addresses both safety and efficacy could have 2 records with `TSPARMCD = "TTYPE"` (Trial Type), one with `TSVAL = "SAFETY"` and the other with `TSVAL = "EFFICACY"`. `TSSEQ` has a different value for each record for the same parameter. Note that this is different from datasets that contain subject data, where the `--SEQ` variable has a different value for each record for the same subject.
13. TS does not contain subject-level data, so there is no restriction analogous to the requirement in subject-level datasets that the blocks bound by `TSGRPID` are within a subject. `TSGRPID` can be used to tie together any block of records in the dataset. `TSGRPID` is most likely to be used when the TS dataset includes multiple records for the same parameter.

    For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records. There are 2 records each for `TSPARMCD = "DOSE"` and `TSPARMCD = "DOSFREQ"`. Records with the same `TSGRPID` are associated with each other. In this example, dose units are the same for both administration schedules, so only 1 record for `DOSU` is needed.

    | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL |
    | --- | --- | --- | --- | --- |
    | 1 | A | DOSE | Dose per Administration | 50 |
    | 1 | A | DOSFREQ | Dosing Frequency | BID |
    | 2 | B | DOSE | Dose per Administration | 100 |
    | 2 | B | DOSFREQ | Dosing Frequency | Q24H |
    | 1 |  | DOSU | Dose Units | mg |

14. Protocols vary in how they describe objectives. If the protocol does not provide information about which objectives meet the definition of `TSPARM = "OBJPRIM"` (Trial Primary Objective; i.e., the principal purpose of the trial), then the objectives should be provided as values of `TSPARM = "OBJPRIM"`. Consult the controlled terminology for trial summary parameters for appropriate parameter values for representing other objective designations (e.g., secondary, exploratory).
15. As per the definitions, the primary outcome measure is associated with the primary objective, the secondary outcome measure is associated with the secondary objective, and the exploratory outcome measure is associated with the exploratory objective. It is possible for the same outcome measure to be associated with more than 1 objective. For example, 2 objectives could use the same outcome measure at different time points, or using different analysis methods.
16. If a primary objective is assessed by means of multiple outcome measures, then all of these outcome measures should be provided as values of `TSPARM = "OUTMSPRI"` (Primary Outcome Measure). Similarly, all outcome measures used to assess secondary objectives should be provided as values of `TSPARM = "OUTMSSEC"` (Secondary Outcome Measure), and all outcome measures used to assess exploratory objectives should be provided as values of `TSPARM = "OUTMSEXP"` (Exploratory Outcome Measure). Additional key measures of a study that are not designated as primary, secondary, or exploratory should be provided as values of `TSPARM = "OUTMSADD"` (Additional Outcome Measure).
17. Trial indication: values for `TSVAL` when `TSPARMCD = "INDIC"` would indicate the condition, disease, or disorder the trial is intended to investigate or address. A vaccine study of healthy subjects, with the intended purpose of preventing influenza infection, would have `TSVAL = "Influenza"`. A clinical pharmacology study of healthy volunteers, with the purpose of collecting pharmacokinetic data, would have no trial indication; `TSVAL` would be null and `TSVALNF = "NA"` if TS contains a row where `TSPARMCD = "INDIC"`.
18. Values for `TSVAL` when `TSPARMCD = "REGID"` (Registry Identifier) will be identifiers assigned by the registry (e.g., ClinicalTrials.gov, EudraCT).

##### TS – Examples
*Example 1*

This example shows a subset of published controlled terminology parameters and the relationship of values across response variables `TSVAL`, `TSVALNF`, `TSVALCD`, `TSVCDREF`, and `TSVCDVER`.

`ts.xpt`

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | TS | 1 |  | ADDON | Added on to Existing Treatments | Y |  | C49488 | CDISC CT | 2011-06-10 |
| 2 | XYZ | TS | 1 |  | AGEMAX | Planned Maximum Age of Subjects | P70Y |  |  | ISO 8601 |  |
| 3 | XYZ | TS | 1 |  | AGEMIN | Planned Minimum Age of Subjects | P18M |  |  | ISO 8601 |  |
| 4 | XYZ | TS | 1 |  | LENGTH | Trial Length | P3M |  |  | ISO 8601 |  |
| 5 | XYZ | TS | 1 |  | PLANSUB | Planned Number of Subjects | 300 |  |  |  |  |
| 6 | XYZ | TS | 1 |  | RANDOM | Trial is Randomized | Y |  | C49488 | CDISC CT | 2011-06-10 |
| 7 | XYZ | TS | 1 |  | SEXPOP | Sex of Participants | BOTH |  | C49636 | CDISC CT | 2011-06-10 |
| 8 | XYZ | TS | 1 |  | STOPRULE | Study Stop Rules | INTERIM ANALYSIS FOR FUTILITY |  |  |  |  |
| 9 | XYZ | TS | 1 |  | TBLIND | Trial Blinding Schema | DOUBLE BLIND |  | C15228 | CDISC CT | 2011-06-10 |
| 10 | XYZ | TS | 1 |  | TCNTRL | Control Type | PLACEBO |  | C49648 | CDISC CT | 2011-06-10 |
| 11 | XYZ | TS | 1 |  | TDIGRP | Diagnosis Group | Neurofibromatosis Syndrome (Disorder) |  | 19133005 | SNOMED | 2011-03 |
| 12 | XYZ | TS | 1 |  | INDIC | Trial Disease/Condition Indication | Tonic-Clonic Epilepsy (Disorder) |  | 352818000 | SNOMED | 2011-03 |
| 13 | XYZ | TS | 1 |  | TINDTP | Trial Intent Type | TREATMENT |  | C49656 | CDISC CT | 2011-06-10 |
| 14 | XYZ | TS | 1 |  | TITLE | Trial Title | A 24 Week Study of Oral Gabapentin vs. Placebo as add-on Treatment to Phenytoin in Subjects with Epilepsy due to Neurofibromatosis |  |  |  |  |
| 15 | XYZ | TS | 1 |  | TPHASE | Trial Phase Classification | Phase II Trial |  | C15601 | CDISC CT | 2011-06-10 |
| 16 | XYZ | TS | 1 |  | TTYPE | Trial Type | EFFICACY |  | C49666 | CDISC CT | 2011-06-10 |
| 17 | XYZ | TS | 2 |  | TTYPE | Trial Type | SAFETY |  | C49667 | CDISC CT | 2011-06-10 |
| 18 | XYZ | TS | 1 |  | CURTRT | Current Therapy or Treatment | Phenytoin |  | 6158TKW0C5 | UNII |  |
| 19 | XYZ | TS | 1 |  | OBJPRIM | Trial Primary Objective | Reduction in the 3-month seizure frequency from baseline |  |  |  |  |
| 20 | XYZ | TS | 1 |  | OBJSEC | Trial Secondary Objective | Percent reduction in the 3-month seizure frequency from baseline |  |  |  |  |
| 21 | XYZ | TS | 2 |  | OBJSEC | Trial Secondary Objective | Reduction in the 3-month tonic-clonic seizure frequency from baseline |  |  |  |  |
| 22 | XYZ | TS | 1 |  | SPONSOR | Clinical Study Sponsor | Pharmaco |  | 123456789 | D-U-N-S NUMBER |  |
| 23 | XYZ | TS | 1 |  | TRT | Investigational Therapy or Treatment | Gabapentin |  | 6CW7F3G59X | UNII |  |
| 24 | XYZ | TS | 1 |  | RANDQT | Randomization Quotient | 0.67 |  |  |  |  |
| 25 | XYZ | TS | 1 |  | STRATFCT | Stratification Factor | SEX |  |  |  |  |
| 26 | XYZ | TS | 1 |  | REGID | Registry Identifier | NCT123456789 |  | NCT123456789 | ClinicalTrials.gov |  |
| 27 | XYZ | TS | 2 |  | REGID | Registry Identifier | XXYYZZ456 |  | XXYYZZ456 | EudraCT |  |
| 28 | XYZ | TS | 1 |  | OUTMSPRI | Primary Outcome Measure | SEIZURE FREQUENCY |  |  |  |  |
| 29 | XYZ | TS | 1 |  | OUTMSSEC | Secondary Outcome Measure | SEIZURE FREQUENCY |  |  |  |  |
| 30 | XYZ | TS | 2 |  | OUTMSSEC | Secondary Outcome Measure | SEIZURE DURATION |  |  |  |  |
| 31 | XYZ | TS | 1 |  | OUTMSEXP | Exploratory Outcome Measure | SEIZURE INTENSITY |  |  |  |  |
| 32 | XYZ | TS | 1 |  | PCLAS | Pharmacological Class | Anti-epileptic Agent |  | N0000175753 | MED-RT |  |
| 33 | XYZ | TS | 1 |  | FCNTRY | Planned Country of Investigational Sites | USA |  |  | ISO 3166-1 Alpha-3 |  |
| 34 | XYZ | TS | 2 |  | FCNTRY | Planned Country of Investigational Sites | CAN |  |  | ISO 3166-1 Alpha-3 |  |
| 35 | XYZ | TS | 3 |  | FCNTRY | Planned Country of Investigational Sites | MEX |  |  | ISO 3166-1 Alpha-3 |  |
| 36 | XYZ | TS | 1 |  | ADAPT | Adaptive Design | N |  | C49487 | CDISC CT | 2011-06-10 |
| 37 | XYZ | TS | 1 | PA | DCUTDTC | Data Cutoff Date | 2010-04-10 |  |  | ISO 8601 |  |
| 38 | XYZ | TS | 1 | PA | DCUTDESC | Data Cutoff Description | PRIMARY ANALYSIS |  |  |  |  |
| 39 | XYZ | TS | 1 |  | INTMODEL | Intervention Model | PARALLEL |  | C82639 | CDISC CT | 2011-06-10 |
| 40 | XYZ | TS | 1 |  | NARMS | Planned Number of Arms | 3 |  |  |  |  |
| 41 | XYZ | TS | 1 |  | STYPE | Study Type | INTERVENTIONAL |  | C98388 | CDISC CT | 2011-06-10 |
| 42 | XYZ | TS | 1 |  | INTTYPE | Intervention Type | DRUG |  | C1909 | CDISC CT | 2011-06-10 |
| 43 | XYZ | TS | 1 |  | SSTDTC | Study Start Date | 2009-03-11 |  |  | ISO 8601 |  |
| 44 | XYZ | TS | 1 |  | SENDTC | Study End Date | 2011-04-01 |  |  | ISO 8601 |  |
| 45 | XYZ | TS | 1 |  | ACTSUB | Actual Number of Subjects | 304 |  |  |  |  |
| 46 | XYZ | TS | 1 |  | HLTSUBJI | Healthy Subject Indicator | N |  | C49487 | CDISC CT | 2011-06-10 |
| 47 | XYZ | TS | 1 |  | SDMDUR | Stable Disease Minimum Duration | P3W |  |  | ISO 8601 |  |
| 48 | XYZ | TS | 1 |  | CRMDUR | Confirmed Response Minimum Duration | P28D |  |  | ISO 8601 |  |

*Example 2*

This example shows the relationship between parameters involving diagnosis and indication. Only selected trial summary parameters are included.

- Row 1 shows the trial title.
- Row 2 shows that subjects in this trial have a diagnosis of diabetes.
- Rows 3-4 show the conditions which the intervention in the trial is intended to address. The 2 rows for the same parameter are differentiated by their `TSSEQ` values.
- Row 5 shows that the intent of this trial is prevention of the conditions represented using the parameter `Trial Indication`.

`ts.xpt`

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | TS | 1 |  | TITLE | Trial Title | A Study Comparing Cardiovascular Effects of Ticagrelor Versus Placebo in Patients With Type 2 Diabetes Mellitus (THEMIS) |  |  |  |  |
| 2 | XYZ | TS | 1 |  | TDIGRP | Diagnosis Group | Diabetes mellitus type 2 |  | 44054006 | SNOMED | 2017-03 |
| 3 | XYZ | TS | 1 |  | INDIC | Trial Indication | Cardiac infarction |  | 22298006 | SNOMED | 2017-03 |
| 4 | XYZ | TS | 2 |  | INDIC | Trial Indication | Cerebrovascular accident |  | 230690007 | SNOMED | 2017-01 |
| 5 | XYZ | TS | 1 |  | TINDTP | Trial Intent Type | PREVENTION |  | C49657 | CDISC CT | 2017-03-01 |

*Example 3*

This example shows how to implement the null flavor in `TSVALNF` when the value in `TSVAL` is missing. Note that when `TSVAL` is null, `TSVALCD` is also null, and no code system is specified in `TSVCDREF` and `TSVCDVER`.

- Row 1 shows that there was no upper limit on planned age of subjects, as indicated by `TSVALNF = "PINF"` (the null value that means "positive infinity").
- Row 2 shows that trial phase classification is not applicable, as indicated by `TSVALNF = "NA"`.

`ts.xpt`

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | XYZ | TS | 1 |  | AGEMAX | Planned Maximum Age of Subjects |  | PINF |  |  |  |
| 2 | XYZ | TS | 1 |  | TPHASE | Trial Phase Classification |  | NA |  |  |  |

*Example 4*

This example shows use of `TSGRPID` to group parameter values describing specific study parts (e.g., `PHASE 1B`, `PHASE 3`) and specific study treatments (e.g., `DRUG X`, `DRUG Z`).

- Rows 1-6 show parameters and values that apply to the whole trial. `TSGRPID` is null for this set of parameters.
- Rows 7-17 show parameters and values that describe the Phase 1B part of the trial. `TSGRPID` is populated with a value of `PHASE 1B` for this set of parameters.
- Rows 18-29 show parameters and values that describe the Phase 3 part of the trial. `TSGRPID` is populated with a value of `PHASE 3` for this set of parameters.
- Rows 30-33 show parameters and values that describe details about 1 of the treatments planned in the trial. `TSGRPID = "DRUG X"` for this set of parameters.
- Rows 34-37 show parameters and values that describe details about 1 of the treatments planned in the trial. `TSGRPID = "DRUG Z"` for this set of parameters.

`ts.xpt`

| Row | STUDYID | DOMAIN | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL | TSVALNF | TSVALCD | TSVCDREF | TSVCDVER |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | ABC123 | TS | 1 |  | TITLE | Trial Title | A Phase 1b/3, Multicenter Trial of Drug Z in Combination with Drug X for Treatment of Melanoma |  |  |  |  |
| 2 | ABC123 | TS | 1 |  | INDIC | Trial Indication | Malignant melanoma |  | 372244006 | SNOMED | 2018-09-01 |
| 3 | ABC123 | TS | 1 |  | SEXPOP | Sex of Participants | BOTH |  | C49636 | CDISC CT | 2018-12-21 |
| 4 | ABC123 | TS | 1 |  | AGEMIN | Planned Minimum Age of Subjects | P18Y |  |  | ISO 8601 |  |
| 5 | ABC123 | TS | 1 |  | AGEMAX | Planned Maximum Age of Subjects |  | PINF |  |  |  |
| 6 | ABC123 | TS | 1 |  | HLTSUBJI | Healthy Subject Indicator | N |  | C49487 | CDISC CT | 2018-12-21 |
| 7 | ABC123 | TS | 1 | PHASE 1B | TPHASE | Trial Phase Classification | PHASE IB TRIAL |  |  |  |  |
| 8 | ABC123 | TS | 1 | PHASE 1B | TBLIND | Trial Blinding Schema | OPEN LABEL |  | C49659 | CDISC CT | 2018-12-21 |
| 9 | ABC123 | TS | 1 | PHASE 1B | TCNTRL | Control Type | NONE |  | C41132 | CDISC CT | 2018-12-21 |
| 10 | ABC123 | TS | 1 | PHASE 1B | TTYPE | Trial Type | SAFETY |  | C49667 | CDISC CT | 2018-12-21 |
| 11 | ABC123 | TS | 1 | PHASE 1B | INTMODEL | Intervention Model | SINGLE GROUP |  | C82640 | CDISC CT | 2018-12-21 |
| 12 | ABC123 | TS | 1 | PHASE 1B | NARMS | Planned Number of Arms | 1 |  |  |  |  |
| 13 | ABC123 | TS | 1 | PHASE 1B | PLANSUB | Planned Number of Subjects | 30 |  |  |  |  |
| 14 | ABC123 | TS | 1 | PHASE 1B | RANDOM | Trial is Randomized | N |  | C49487 | CDISC CT | 2018-12-21 |
| 15 | ABC123 | TS | 1 | PHASE 1B | OBJPRIM | Trial Primary Objective | To evaluate the safety, as assessed by incidence of dose limiting toxicity, of combination therapy (Drug X + Drug Z) |  |  |  |  |
| 16 | ABC123 | TS | 1 | PHASE 1B | OUTMSPRI | Primary Outcome Measure | Incidence of dose limiting toxicities |  |  |  |  |
| 17 | ABC123 | TS | 1 | PHASE 1B | COMPTRT | Comparative Treatment |  | NA |  |  |  |
| 18 | ABC123 | TS | 1 | PHASE 3 | TPHASE | Trial Phase Classification | PHASE III TRIAL |  | C15602 | CDISC CT | 2018-12-21 |
| 19 | ABC123 | TS | 1 | PHASE 3 | TBLIND | Trial Blinding Schema | DOUBLE BLIND |  | C15228 | CDISC CT | 2018-12-21 |
| 20 | ABC123 | TS | 1 | PHASE 3 | TCNTRL | Control Type | PLACEBO |  | C49648 | CDISC CT | 2018-12-21 |
| 21 | ABC123 | TS | 1 | PHASE 3 | TTYPE | Trial Type | EFFICACY |  | C49666 | CDISC CT | 2018-12-21 |
| 22 | ABC123 | TS | 1 | PHASE 3 | INTMODEL | Intervention Model | PARALLEL |  | C82639 | CDISC CT | 2018-12-21 |
| 23 | ABC123 | TS | 1 | PHASE 3 | NARMS | Planned Number of Arms | 2 |  |  |  |  |
| 24 | ABC123 | TS | 1 | PHASE 3 | PLANSUB | Planned Number of Subjects | 500 |  |  |  |  |
| 25 | ABC123 | TS | 1 | PHASE 3 | RANDOM | Trial is Randomized | Y |  | C49488 | CDISC CT | 2018-12-21 |
| 26 | ABC123 | TS | 1 | PHASE 3 | RANDQT | Randomization Quotient | 0.5 |  |  |  |  |
| 27 | ABC123 | TS | 1 | PHASE 3 | OBJPRIM | Trial Primary Objective | To evaluate the efficacy of combination therapy (Drug X + Drug Z) versus monotherapy (Drug X + Placebo), as assessed by progression-free survival using RECIST 1.1 |  |  |  |  |
| 28 | ABC123 | TS | 1 | PHASE 3 | OUTMSPRI | Primary Outcome Measure | Progression Free Survival (response evaluation by blinded central review using RECIST 1.1) |  |  |  |  |
| 29 | ABC123 | TS | 1 | PHASE 3 | COMPTRT | Comparative Treatment | DRUG X |  |  |  |  |
| 30 | ABC123 | TS | 1 | DRUG X | DOSE | Dose per Administration | 200 |  |  |  |  |
| 31 | ABC123 | TS | 1 | DRUG X | DOSU | Dose Units | mg |  | C28253 | CDISC CT | 2018-12-21 |
| 32 | ABC123 | TS | 1 | DRUG X | DOSFRQ | Dosing Frequency | EVERY WEEK |  | C67069 | CDISC CT | 2018-12-21 |
| 33 | ABC123 | TS | 1 | DRUG X | ROUTE | Route of Administration | ORAL |  | C38288 | CDISC CT | 2018-12-21 |
| 34 | ABC123 | TS | 1 | DRUG Z | DOSE | Dose per Administration | 10000 |  |  |  |  |
| 35 | ABC123 | TS | 1 | DRUG Z | DOSU | Dose Units | PFU |  | C67264 | CDISC CT | 2018-12-21 |
| 36 | ABC123 | TS | 1 | DRUG Z | DOSFRQ | Dosing Frequency | EVERY 2 WEEKS |  | C71127 | CDISC CT | 2018-12-21 |
| 37 | ABC123 | TS | 1 | DRUG Z | ROUTE | Route of Administration | INTRATUMOR |  | C38269 | CDISC CT | 2018-12-21 |
##### 7.4.2.1 Use of Null Flavor

The variable `TSVALNF` is based on the idea of a "null flavor" as embodied in the ISO 21090 standard (Health Informatics - Harmonized data types for information exchange; [https://www.iso.org/standard/35646.html](https://www.iso.org/standard/35646.html)). A null flavor is an ancillary piece of data that provides additional information when its primary piece of data is null (has a missing value). There is controlled terminology for the null flavor data item which includes such familiar values as `"Unknown"`, `"Other"`, and `"Not Applicable"` among its 14 terms.

The proposal to include a null flavor variable to supplement the `TSVAL` variable in the Trial Summary Information (TS) dataset arose when it was realized that the TS model did not have a good way to represent the fact that a protocol placed no upper limit on the age of study subjects. When the trial summary parameter is `AGEMAX`, then `TSVAL` should have a value expressed as an ISO 8601 time duration (e.g., `P43Y` for 43 years old, `P6M` for 6 months old). Although it would be possible to allow a value such as `"NONE"` or `"UNBOUNDED"` to be entered in `TSVAL`, validation programs would then have to recognize this special term as an exception to the expected data format. Therefore, the SDS team decided that a separate null flavor variable that uses the ISO 21090 null-flavor terminology would be a better solution.

The SDS Team also decided to specify the use of a null-flavor variable in the TS domain with SDTMIG v3.4 as a way of testing the use of such a variable in a limited setting. As the title of ISO 21090 suggests, that standard was developed for use with healthcare data; it is expected that it will eventually see wide use in the clinical data from which clinical trial data are derived. CDISC already uses this data-type standard (see BRIDG; [https://www.cdisc.org/standards/](https://www.cdisc.org/standards/)). The null flavor, in particular, is a solution to the widespread problem of needing or wanting to convey information that will help in the interpretation of a missing value. Although null flavors could certainly be eventually used for this purpose in other cases (e.g., with subject data), doing so at this time would be extremely disruptive and premature. The use of null flavors for the variable `TSVAL` provides an opportunity for sponsors and reviewers to learn about the null flavors and to evaluate their usefulness in a concrete setting.

The controlled terminology for null flavor, which supersedes Appendix C1, Supplemental Qualifiers Name Codes, is included below.

**NullFlavor Enumeration. OID: 2.16.840.1.113883.5.1008**

| Level | Code | Name | Description |
| --- | --- | --- | --- |
| 1 | NI | No information | The value is exceptional (i.e., missing, omitted, incomplete, improper). No information as to the reason for being an exceptional value is provided. This is the most general exceptional value. It is also the default exceptional value. |
| 2 | INV | Invalid | The value as represented in the instance is not a member of the set of permitted data values in the constrained value domain of a variable. |
| 3 | OTH | Other | The actual value is not a member of the set of permitted data values in the constrained value domain of a variable (e.g., concept not provided by required code system). |
| 4 | PINF | Positive infinity | Positive infinity of numbers. |
| 4 | NINF | Negative infinity | Negative infinity of numbers. |
| 3 | UNC | Unencoded | No attempt has been made to encode the information correctly, but the raw source information is represented (usually in original text). |
| 3 | DER | Derived | An actual value may exist, but it must be derived from the information provided (usually an expression is provided directly). |
| 2 | UNK | Unknown | A proper value is applicable, but not known. |
| 3 | ASKU | Asked but unknown | Information was sought but not found (e.g., patient was asked but did not know). |
| 4 | NAV | Temporarily unavailable | Information is not available at this time, but is expected to be available later. |
| 3 | NASK | Not asked | This information has not been sought (e.g., patient was not asked). |
| 3 | QS | Sufficient quantity | The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the bulk of the material. For example, if directions said, "Add 10 mg of ingredient X, 50 mg of ingredient Y, and sufficient quantity of water to 100 ml", the null flavor `QS` would be used to express the quantity of water. |
| 3 | TRC | Trace | The content is greater than zero, but too small to be quantified. |
| 2 | MSK | Masked | There is information on this item available, but it has not been provided by the sender due to security, privacy or other reasons. There may be an alternate mechanism for gaining access to this information. |
| 2 | NA | Not applicable | No proper value is applicable in this context (e.g., last menstrual period for a male). |

Warning for `MSK`: use of this null flavor does provide information that may be a breach of confidentiality, even though no detailed data are provided. Its primary purpose is for those circumstances where it is necessary to inform the receiver that the information does exist without providing any detail.

The numbers in column 1 of the table describe the hierarchy of these values:

- No information
  - Invalid
    - Other
    - Positive infinity
    - Negative infinity
    - Unencoded
    - Derived
  - Unknown
    - Asked but unknown
    - Temporarily unavailable
    - Not asked
    - Quantity sufficient
    - Trace
  - Masked
  - Not applicable

The value at level 1 (`No information`) is the least informative. It merely confirms that the primary piece of data is null.

The values at level 2 provide a little more information, distinguishing between situations where the primary piece of data is not applicable and those where it is applicable but masked, unknown, or invalid (i.e., not in the correct format to be represented in the primary piece of data).

The values at levels 3 and 4 provide successively more information about the situation. For example, for the `AGEMAX` case that provided the impetus for the creation of the `TSVALNF` variable, the value `PINF` means that there is information about the maximum age, but it is not something that can be expressed in the ISO 8601 quantity-of-time format required for populating `TSVAL`. The null flavor `PINF` provides the most complete information possible in this case (i.e., that the maximum age for the study is unbounded).

### 7.5 How to Model the Design of a Clinical Trial

The following steps allow the modeler to move from more-familiar concepts, such as arms, to less-familiar concepts, such as elements and epochs. The actual process of modeling a trial may depart from these numbered steps. Some steps will overlap; there may be several iterations; and not all steps are relevant for all studies.

1. Start from the flow chart or schema diagram usually included in the trial protocol. This diagram will show how many arms the trial has, and the branch points or decision points where the arms diverge.
2. Write down the decision rule for each branching point in the diagram. Does the assignment of a subject to an arm depend on a randomization? On whether the subject responded to treatment? On some other criterion?
3. If the trial has multiple branching points, check whether all the branches that have been identified really lead to different arms. The arms will relate to the major comparisons the trial is designed to address. For some trials, there may be a group of somewhat different paths through the trial that are all considered to belong to a single arm.
4. For each arm, identify the major time periods of treatment and non-treatment a subject assigned to that arm will go through. These are the elements, or building blocks, of which the arm is composed.
5. Define the starting point of each element. Define the rule for how long the element should last. Determine whether the element is of fixed duration.
6. Re-examine the sequences of elements that make up the various arms and consider alternative element definitions. Would it be better to "split" some elements into smaller pieces or "lump" some elements into larger pieces? Such decisions will depend on the aims of the trial and plans for analysis.
7. Compare the various arms. In most clinical trials, especially blinded trials, the pattern of elements will be similar for all arms, and it will make sense to define trial epochs. Assign names to these epochs. During the conduct of a blinded trial, it will not be known which arm a subject has been assigned to, or which treatment elements they are experiencing, but the epochs they are passing through will be known.
8. Identify the visits planned for the trial. Define the planned start timings for each visit, expressed relative to the ordered sequences of elements that make up the arms. Define the rules for when each visit should end.
9. For oncology trials or other trials with disease assessments that are not necessarily tied to visits, find the planned timing of disease assessments in the protocol and record it in the Trial Disease Assessments (TD) dataset.
10. If the protocol includes data collection that is triggered by the occurrence of certain events, interventions, or findings, record those triggers in the Trial Disease Milestones (TM) dataset. Note that disease milestones may be pre-study (e.g., disease diagnosis) or on-study.
11. Identify the inclusion and exclusion criteria to be able to populate the Trial Inclusion/Exclusion Criteria (TI) dataset. If inclusion and exclusion criteria were amended so that subjects entered under different versions, populate `TIVERS` to represent the different versions.
12. Populate the TS dataset with summary information.

---

## Domain Variable Specifications

### TA --- Trial Arms

**Structure:** One record per planned Element per Arm
**Class:** Trial Design

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | TA |
| 3 | ARMCD | Planned Arm Code | Char | Topic | Req |  |
| 4 | ARM | Description of Planned Arm | Char | Synonym Qualifier | Req |  |
| 5 | TAETORD | Planned Order of Element within Arm | Num | Timing | Req |  |
| 6 | ETCD | Element Code | Char | Record Qualifier | Req |  |
| 7 | ELEMENT | Description of Element | Char | Synonym Qualifier | Perm |  |
| 8 | TABRANCH | Branch | Char | Rule | Exp |  |
| 9 | TATRANS | Transition Rule | Char | Rule | Exp |  |
| 10 | EPOCH | Epoch | Char | Timing | Req | C99079 |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **ARMCD**: ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than that for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20.
- **ARM**: Name given to an arm or treatment group.
- **TAETORD**: Number that gives the order of the element within the arm.
- **ETCD**: ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.
- **ELEMENT**: The name of the element. The same element may occur more than once within an arm.
- **TABRANCH**: Condition subject met, at a "branch" in the trial design at the end of this element, to be included in this arm (e.g., "Randomization to DRUG X").
- **TATRANS**: If the trial design allows a subject to transition to an element other than the next element in sequence, then the conditions for transitioning to those other elements, and the alternative element sequences, are specified in this rule (e.g., "Responders go to washout").
- **EPOCH**: Name of the trial epoch with which this element of the arm is associated.

---

### TD --- Trial Disease Assessments

**Structure:** One record per planned constant assessment period
**Class:** Trial Design

| # | Variable | Label | Type | Role | Core | Controlled Terms/Format |
|---|----------|-------|------|------|------|-------------------------|
| 1 | STUDYID | Study Identifier | Char | Identifier | Req |  |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier | Req | TD |
| 3 | TDORDER | Sequence of Planned Assessment Schedule | Num | Timing | Req |  |
| 4 | TDANCVAR | Anchor Variable Name | Char | Timing | Req |  |
| 5 | TDSTOFF | Offset from the Anchor | Char | Timing | Req | ISO 8601 duration |
| 6 | TDTGTPAI | Planned Assessment Interval | Char | Timing | Req | ISO 8601 duration |
| 7 | TDMINPAI | Planned Assessment Interval Minimum | Char | Timing | Req | ISO 8601 duration |
| 8 | TDMAXPAI | Planned Assessment Interval Maximum | Char | Timing | Req | ISO 8601 duration |
| 9 | TDNUMRPT | Maximum Number of Actual Assessments | Num | Record Qualifier | Req |  |

**CDISC Notes:**

- **STUDYID**: Unique identifier for a study.
- **DOMAIN**: Two-character abbreviation for the domain.
- **TDORDER**: A number given to ensure ordinal sequencing of the planned assessment schedules within a trial.
- **TDANCVAR**: A reference to the date variable name that provides the start point from which the planned disease assessment schedule is measured. This must be a referenced from the ADaM ADSL dataset (e.g., "ANCH1DT"). Note: TDANCVAR will contain the name of a reference date variable.
- **TDSTOFF**: A fixed offset from the date provided by the variable referenced in TDANCVAR. This is used when the timing of planned cycles does not start on the exact day referenced in the variable indicated in TDANCVAR. The value of this variable will be either zero or a positive value and will be represented in ISO 8601 character format.
- **TDTGTPAI**: The planned interval between disease assessments represented in ISO 8601 character format.
- **TDMINPAI**: The lower limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format.
- **TDMAXPAI**: The upper limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format.
- **TDNUMRPT**: This variable must represent the maximum number of actual assessments for the analysis that this disease assessment schedule describes. In a trial where the maximum number of assessments is not defined explicitly in the protocol (e.g., assessments occur until death), TDNUMRPT should represent the maximum number of disease assessments that support the efficacy analysis encountered by any subject across the trial at that point in time.