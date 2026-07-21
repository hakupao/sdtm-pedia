# 04_sp_se_sm_sv_co

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `04`
> - **Concept**: SE + SM + SV + CO (Special-Purpose 剩余 4)
> - **Merged files**: 12
> - **Words**: 9,417
> - **Chars**: 55,015
> - **Sources**:
>   - `domains/SE/spec.md`
>   - `domains/SE/assumptions.md`
>   - `domains/SE/examples.md`
>   - `domains/SM/spec.md`
>   - `domains/SM/assumptions.md`
>   - `domains/SM/examples.md`
>   - `domains/SV/spec.md`
>   - `domains/SV/assumptions.md`
>   - `domains/SV/examples.md`
>   - `domains/CO/spec.md`
>   - `domains/CO/assumptions.md`
>   - `domains/CO/examples.md`

---
## Source: `domains/SE/spec.md`

# SE — Subject Elements

> Class: Special-Purpose | Structure: One record per actual Element per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### SESEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. Should be assigned to be consistent chronological order.

### ETCD
- **Order:** 5
- **Label:** Element Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** 1. ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.  2. If an encountered element differs from the planned element to the point that it is considered a new element, then use "UNPLAN" as the value for ETCD to represent this element.

### ELEMENT
- **Order:** 6
- **Label:** Description of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** The name of the element. If ETCD has a value of "UNPLAN", then ELEMENT should be null.

### TAETORD
- **Order:** 7
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the subject's assigned trial arm.

### EPOCH
- **Order:** 8
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the element in the planned sequence of elements for the arm to which the subject was assigned.

### SESTDTC
- **Order:** 9
- **Label:** Start Date/Time of Element
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** Start date/time for an element for each subject.

### SEENDTC
- **Order:** 10
- **Label:** End Date/Time of Element
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time for an element for each subject.

### SESTDY
- **Order:** 11
- **Label:** Study Day of Start of Element
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of start of element relative to the sponsor-defined RFSTDTC.

### SEENDY
- **Order:** 12
- **Label:** Study Day of End of Element
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of end of element relative to the sponsor-defined RFSTDTC.

### SEUPDES
- **Order:** 13
- **Label:** Description of Unplanned Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of what happened to the subject during an unplanned element. Used only if ETCD has the value of "UNPLAN".
---

## Cross References

### Controlled Terminology
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Special-Purpose):** CO, DM, SM, SV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)

## Source: `domains/SE/assumptions.md`

# SE — Assumptions

Submission of the SE dataset is strongly recommended, as it provides information needed by reviewers to place observations in context within the study. As noted in the SE - Description/Overview, the TE and TA datasets should also be submitted, as these define the design and the terms referenced by the SE dataset.

The SE domain allows the submission of data on the timing of the trial elements a subject actually passed through in their participation in the trial. Section 7.2.2, Trial Elements, and Section 7.2.1, Trial Arms, provide additional information on these datasets, which define a trial's planned elements and describe the planned sequences of elements for the arms of the trial.

1. For any particular subject, the dates in the SE table are the dates when the transition events identified in the TE table occurred. Judgment may be needed to match actual events in a subject's experience with the definitions of transition events (i.e., events that mark the start of new elements) in the TE table; actual events may vary from the plan. For instance, in a single-dose pharmacokinetics (PK) study, the transition events might correspond to study drug doses of 5 and 10 mg. If a subject actually received a dose of 7 mg when they were scheduled to receive 5 mg, a decision will have to be made on how to represent this in the SE domain.

2. If the date/time of a transition element was not collected directly, the method used to infer the element start date/time should be explained in the Comments column of the Define-XML document.

3. Judgment will also have to be used in deciding how to represent a subject's experience if an element does not proceed or end as planned. For instance, the plan might identify a trial element that is to start with the first of a series of 5 daily doses and end after 1 week, when the subject transitions to the next treatment element. If the subject actually started the next treatment epoch (see Section 7.1, Introduction to Trial Design Model Datasets, and Section 7.1.2, Definitions of Trial Design Concepts) after 4 weeks, the sponsor would have to decide whether to represent this as an abnormally long element, or as a normal element plus an unplanned non-treatment element.

4. If the sponsor decides that the subject's experience for a particular period of time cannot be represented with one of the planned elements, then that period of time should be represented as an unplanned element. The value of ETCD for an unplanned element is "UNPLAN" and SEUPDES should be populated with a description of the unplanned element.

5. The values of SESTDTC provide the chronological order of the actual subject elements. SESEQ should be assigned to be consistent with the chronological order. Note that the requirement that SESEQ be consistent with chronological order is more stringent than in most other domains, where --SEQ values need only be unique within subject.

6. When TAETORD is included in the SE domain, it represents the planned order of an element in an arm. This should not be confused with the actual order of the elements, which will be represented by their chronological order and SESEQ. TAETORD will not be populated for subject elements that are not planned for the arm to which the subject was assigned. Thus, TAETORD will not be populated for any element with an ETCD value of "UNPLAN". TAETORD also will not be populated if a subject passed through an element that, although defined in the TE dataset, was out of place for the arm to which the subject was assigned. For example, if a subject in a parallel study of drug A vs. drug B was assigned to receive drug A but received drug B instead, then TAETORD would be left blank for the SE record for their drug B element. If a subject was assigned to receive the sequence of elements A, B, C, D, and instead received A, D, B, C, then the sponsor would have to decide for which of these SE records TAETORD should be populated. The rationale for this decision should be documented in the Comments column of the Define-XML document.

7. For subjects who follow the planned sequence of elements for the arm to which they were assigned, the values of EPOCH in the SE domain will match those associated with the elements for the subject's arm in the TA dataset. The sponsor will have to decide what value, if any, of EPOCH to assign SE records for unplanned elements and in other cases where the subject's actual elements deviate from the plan. The sponsor's methods for such decisions should be documented in the Define-XML document, in the row for EPOCH in the SE dataset table.

8. Because there are, by definition, no gaps between elements, the value of SEENDTC for one element will always be the same as the value of SESTDTC for the next element.

9. Note that SESTDTC is required, although --STDTC is not required in any other subject-level dataset. The purpose of the dataset is to record the elements a subject actually passed through. If it is known that a subject passed through a particular element, then there must be some information (perhaps imprecise) on when it started. Thus, SESTDTC may not be null, although some records may not have all the components (e.g., year, month, day, hour, minute) of the date/time value collected.

10. The following identifier variables are permissible and may be added as appropriate: --GRPID, --REFID, --SPID.

11. Care should be taken in adding additional timing variables:
    a. The purpose of --DTC and --DY is to record the date and study day on which data was collected. Elements are generally "derived" in the sense that they are a secondary use of data collected elsewhere; it is not generally useful to know when those date/times were recorded.
    b. --DUR could be added only if the duration of an element was collected, not derived.
    c. It would be inappropriate to add the variables that support time points (--TPT, --TPTNUM, --ELTM, --TPTREF, and --RFTDTC), because the topic of this dataset is elements.

## Source: `domains/SE/examples.md`

# SE — Examples

STUDYID and DOMAIN, which are required in the SE and Demographics (DM) domains, have not been included in the following examples, to improve readability.

## Example 1

This example shows data for 2 subjects for a crossover trial with 4 epochs.

**Row 1:** The record for the SCREEN element for subject 789. Note that only the date of the start of the SCREEN element was collected, whereas for the end of the element (which corresponds to the start of IV dosing) both date and time were collected.

**Row 2:** The record for the IV element for subject 789. The IV element started with the start of IV dosing and ended with the start of oral dosing, and full date/times were collected for both.

**Row 3:** The record for the ORAL element for subject 789. Only the date, and not the time, of the start of follow-up was collected.

**Row 4:** The FOLLOWUP element for subject 789 started and ended on the same day. Presumably, the element had a positive duration, but no times were collected.

**Rows 5-8:** Subject 790 was treated incorrectly. This subject entered the IV element before the ORAL element, although the planned order of elements for this subject was ORAL, then IV. The sponsor has assigned EPOCH values for this subject according to the actual order of elements, rather than the planned order. Per Assumption 6, TAETORD is missing for the elements that were out of order. The correct order of elements is the subject's ARMCD, shown in the DM dataset.

**Rows 9-10:** Subject 791 was screened, randomized to the IV-ORAL arm, and received the IV treatment, but did not return to the unit for the treatment epoch or follow-up.

**se.xpt**

| Row | USUBJID | SESEQ | ETCD | SESTDTC | SEENDTC | SEUPDES | TAETORD | EPOCH |
|-----|---------|-------|------|---------|---------|---------|---------|-------|
| 1 | 789 | 1 | SCREEN | 2006-06-01 | 2006-06-03T10:32 | | 1 | SCREENING |
| 2 | 789 | 2 | IV | 2006-06-03T10:32 | 2006-06-10T09:47 | | 2 | TREATMENT 1 |
| 3 | 789 | 3 | ORAL | 2006-06-10T09:47 | 2006-06-17 | | 3 | TREATMENT 2 |
| 4 | 789 | 4 | FOLLOWUP | 2006-06-17 | 2006-06-17 | | 4 | FOLLOW-UP |
| 5 | 790 | 1 | SCREEN | 2006-06-01 | 2006-06-03T10:14 | | 1 | SCREENING |
| 6 | 790 | 2 | IV | 2006-06-03T10:14 | 2006-06-10T10:32 | | | TREATMENT 1 |
| 7 | 790 | 3 | ORAL | 2006-06-10T10:32 | 2006-06-17 | | | TREATMENT 2 |
| 8 | 790 | 4 | FOLLOWUP | 2006-06-17 | 2006-06-17 | | 4 | FOLLOW-UP |
| 9 | 791 | 1 | SCREEN | 2006-06-01 | 2006-06-03T10:17 | | 1 | SCREENING |
| 10 | 791 | 2 | IV | 2006-06-03T10:17 | 2006-06-07 | | 2 | TREATMENT 1 |

**Row 1:** Subject 789 was assigned to the IV-ORAL arm and was treated accordingly.

**Row 2:** Subject 790 was assigned to the ORAL-IV arm, but their actual treatment was IV, then oral.

**Row 3:** Subject 791 was assigned to the IV-ORAL arm, received the first of the 2 planned treatment elements, and were following the assigned treatment when they withdrew early. The actual arm variables are populated with the values for the arm to which subject 791 was assigned.

**dm.xpt**

| Row | USUBJID | SUBJID | RFSTDTC | RFENDTC | SITEID | INVNAM | BRTHDTC | AGE | AGEU | SEX | RACE | ETHNIC | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD | COUNTRY |
|-----|---------|--------|---------|---------|--------|--------|---------|-----|------|-----|------|--------|-------|-----|----------|--------|--------|----------|---------|
| 1 | 789 | 001 | 2006-06-03 | 2006-06-17 | 01 | SMITH, J | 1948-12-13 | 57 | YEARS | M | WHITE | HISPANIC OR LATINO | IO | IV-ORAL | IO | IV-ORAL | | | USA |
| 2 | 790 | 002 | 2006-06-03 | 2006-06-17 | 01 | SMITH, J | 1955-03-22 | 51 | YEARS | M | WHITE | NOT HISPANIC OR LATINO | OI | ORAL-IV | IO | IV-ORAL | | | USA |
| 3 | 791 | 003 | 2006-06-03 | 2006-06-07 | 01 | SMITH, J | 1956-07-17 | 49 | YEARS | M | WHITE | NOT HISPANIC OR LATINO | IO | IV-ORAL | IO | IV-ORAL | | | USA |

## Example 2

The following data represent 2 subjects enrolled in a trial in which assignment to an arm occurs in 2 stages.

See Section 7.2.1, Trial Arms, Example Trial 3. In this trial, subjects were randomized at the beginning of the blinded treatment epoch, then assigned to treatment for the open treatment epoch according to their response to treatment in the blinded treatment epoch. See Section 5.2, Demographics, for other examples of ARM and ARMCD values for this trial.

In this trial, start of dosing was recorded as dates without times, so SESTDTC values include only dates. Epochs could not be assigned to observations that occurred on epoch transition dates on the basis of the SE dataset alone, so the sponsor's algorithms for dealing with this ambiguity were documented in the Define-XML document.

**Rows 1-2:** Show data for a subject who completed only 2 elements of the trial.

**Rows 3-6:** Show data for a subject who completed the trial, but received the wrong drug for the last 2 weeks of the double-blind treatment period. This has been represented by treating the period when the subject received the wrong drug as an unplanned element. Note that TAETORD, which represents the planned order of elements within an arm, has not been populated for this unplanned element. Even though this element was unplanned, the sponsor assigned a value of BLINDED TREATMENT to EPOCH.

**se.xpt**

| Row | USUBJID | SESEQ | ETCD | SESTDTC | SEENDTC | SEUPDES | TAETORD | EPOCH |
|-----|---------|-------|------|---------|---------|---------|---------|-------|
| 1 | 123 | 1 | SCRN | 2006-06-01 | 2006-06-03 | | 1 | SCREENING |
| 2 | 123 | 2 | DBA | 2006-06-03 | 2006-06-10 | | 2 | BLINDED TREATMENT |
| 3 | 456 | 1 | SCRN | 2006-05-01 | 2006-05-03 | | 1 | SCREENING |
| 4 | 456 | 2 | DBA | 2006-05-03 | 2006-05-31 | | 2 | BLINDED TREATMENT |
| 5 | 456 | 3 | UNPLAN | 2006-05-31 | 2006-06-13 | Drug B dispensed in error | | BLINDED TREATMENT |
| 6 | 456 | 4 | RSC | 2006-06-13 | 2006-07-30 | | 3 | OPEN LABEL TREATMENT |

**Row 1:** Shows the record for a subject who was randomized to blinded treatment A, but withdrew from the trial before the open treatment epoch and did not have a second treatment assignment. They were thus incompletely assigned to an arm. The code used to represent this incomplete assignment, "A", is not in the TA table for this trial design, but is the first part of the codes for the 2 arms to which subject 123 could have been assigned ("AR" or "AO").

**Row 2:** Shows the record for a subject who was randomized to blinded treatment A, but was erroneously treated with drug B for part of the blinded treatment epoch. ARM and ARMCD for this subject reflect the planned treatment and are not affected by the fact that treatment deviated from plan. The sponsor decided that the subject's treatment, which consisted partly of drug A and partly of drug B, did not match any planned arm, so ACTARMCD and ACTARM were left null. ARMNRS was populated with "UNPLANNED TREATMENT" and the way in which this treatment was unplanned was described in ACTARMUD.

**dm.xpt**

| Row | USUBJID | SUBJID | RFSTDTC | RFENDTC | SITEID | INVNAM | BRTHDTC | AGE | AGEU | SEX | RACE | ETHNIC | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD | COUNTRY |
|-----|---------|--------|---------|---------|--------|--------|---------|-----|------|-----|------|--------|-------|-----|----------|--------|--------|----------|---------|
| 1 | 123 | 012 | 2006-06-03 | 2006-06-10 | 01 | JONES, D | 1943-12-08 | 62 | YEARS | M | ASIAN | HISPANIC OR LATINO | A | A | A | A | | | USA |
| 2 | 456 | 103 | 2006-05-03 | 2006-07-30 | 01 | JONES, D | 1950-05-15 | 55 | YEARS | F | WHITE | NOT HISPANIC OR LATINO | AR | A-Rescue | | | UNPLANNED TREATMENT | Drug B dispensed for part of Drug A element | USA |

## Source: `domains/SM/spec.md`

# SM — Subject Disease Milestones

> Class: Special-Purpose | Structure: One record per Disease Milestone per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### SMSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of subject records. Should be assigned to be consistent chronological order.

### MIDS
- **Order:** 5
- **Label:** Disease Milestone Instance Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Name of the specific disease milestone. For types of disease milestones that can occur multiple times, the name will end with a sequence number. Example: "HYPO1".

### MIDSTYPE
- **Order:** 6
- **Label:** Disease Milestone Type
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** The type of disease milestone. Example: "HYPOGLYCEMIC EVENT".

### SMSTDTC
- **Order:** 7
- **Label:** Start Date/Time of Milestone
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of milestone instance (if milestone is an intervention or event) or date of milestone (if Milestone is a finding).

### SMENDTC
- **Order:** 8
- **Label:** End Date/Time of Milestone
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time of disease milestone instance.

### SMSTDY
- **Order:** 9
- **Label:** Study Day of Start of Milestone
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Study day of start of disease milestone instance, relative to the sponsor-defined RFSTDTC.

### SMENDY
- **Order:** 10
- **Label:** Study Day of End of Milestone
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Study day of end of disease milestone instance, relative to the sponsor-defined RFSTDTC.
---

## Cross References

### Related Domains
- **Same class (Special-Purpose):** CO, DM, SE, SV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)

## Source: `domains/SM/assumptions.md`

# SM — Assumptions

1. Disease milestones are observations or activities whose timings are of interest in the study. The types of disease milestones are defined at the study level in the TM dataset. The purpose of the SM dataset is to provide a summary timeline of the milestones for a particular subject.

2. The name of the disease milestone is recorded in MIDS.
   a. For disease milestones that can occur only once (TMRPT = "N"), the value of MIDS may be the value in MIDSTYPE or may an abbreviated version.
   b. For types of disease milestones that can occur multiple times, MIDS will usually be an abbreviated version of MIDSTYPE and will always end with a sequence number. Sequence numbers should start with 1 and indicate the chronological order of the instances of this type of disease milestone.

3. The timing variables SMSTDTC and SMENDTC hold start and end date/times of data collected for the disease milestone(s) for each subject. SMSTDY and SMENDY represent the corresponding study day variables.
   a. The start date/time of the disease milestone is the critical date/time, and must be populated. If the disease milestone is an event, then the meaning of "start date" for the event may need to be defined.
   b. The start study day will not be populated if the start date/time includes only a year or only a year and month.
   c. The end date/time for the disease milestone is less important than the start date/time. It will not be populated if the disease milestone is a finding without an end date/time or if it is an event or intervention for which an end date/time has not yet occurred or was not collected.
   d. The end study day will not be populated if the end date/time includes only a year or only a year and month.

## Source: `domains/SM/examples.md`

# SM — Examples

## Example 1

In this study, the disease milestones of interest were initial diagnosis and hypoglycemic events, as shown in Section 7.3.3, Trial Disease Milestones, Example 1.

**Row 1:** Shows that subject 001's initial diagnosis of diabetes occurred in October 2005. Because this is a partial date, SMDY is not populated. No end date/time was recorded for this milestone.

**Rows 2-3:** Show that subject 001 had 2 hypoglycemic events. In this case, only start date/times have been collected. Because these date/times include full dates, SMSTDY has been populated in each case.

**Row 4:** Shows that subject 002's initial diagnosis of diabetes occurred on May 15, 2010. Because a full date was collected, the study day of this disease milestone was populated. Diagnosis was pre-study, so the study day of the disease milestone is negative. No hypoglycemic events were recorded for this subject.

**sm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SMSEQ | MIDS | MIDSTYPE | SMSTDTC | SMENDTC | SMSTDY | SMENDY |
|-----|---------|--------|---------|-------|------|----------|---------|---------|--------|--------|
| 1 | XYZ | SM | 001 | 1 | DIAG | DIAGNOSIS | 2005-10 | | | |
| 2 | XYZ | SM | 001 | 2 | HYPO1 | HYPOGLYCEMIC EVENT | 2013-09-01T11:00 | | 25 | |
| 3 | XYZ | SM | 001 | 3 | HYPO2 | HYPOGLYCEMIC EVENT | 2013-09-24T6:48 | | 50 | |
| 4 | XYZ | SM | 002 | 1 | DIAG | DIAGNOSIS | 2010-05-15 | | -1046 | |

Information in SM is taken from records in other domains. In this study, diagnosis was represented in the Medical History (MH) domain, and hypoglycemic events were represented in the Clinical Events (CE) domain.

The MH records for diabetes (MHEVDTYP = "DIAGNOSIS") are the records which represent the disease milestones for the defined MIDSTYPE of "DIAGNOSIS", so these records include the MIDS variable with the value "DIAG". Because these are records for disease milestones rather than associated records, the variables RELMIDS and MIDSDTC are not needed.

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHDECOD | MHEVDTYP | MHPRESP | MHOCCUR | MHDTC | MHSTDTC | MHENDTC | MHDY | MIDS |
|-----|---------|--------|---------|-------|--------|---------|----------|---------|---------|-------|---------|---------|------|------|
| 1 | XYZ | MH | 001 | 1 | TYPE 2 DIABETES | Type 2 diabetes mellitus | DIAGNOSIS | Y | Y | 2013-08-06 | 2005-10 | | | DIAG |
| 2 | XYZ | MH | 002 | 1 | TYPE 2 DIABETES | Type 2 diabetes mellitus | DIAGNOSIS | Y | Y | 2013-08-06 | 2010-05-15 | | 1 | DIAG |

In this study, information about hypoglycemic events was collected in a separate CRF module, and CE records recorded in this module were represented with CECAT = "HYPOGLYCEMIC EVENT". Each CE record for a hypoglycemic event is a disease milestone, and records for a study have distinct values of MIDS.

**ce.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CESEQ | CETERM | CEDECOD | CECAT | CEPRESP | CEOCCUR | CESTDTC | CEENDTC | MIDS |
|-----|---------|--------|---------|-------|--------|---------|-------|---------|---------|---------|---------|------|
| 1 | XYZ | CE | 001 | 1 | HYPOGLYCEMIC EVENT | Hypoglycaemia | HYPOGLYCEMIC EVENT | Y | Y | 2013-09-01T11:00 | 2013-09-01T12:30 | HYPO1 |
| 2 | XYZ | CE | 001 | 2 | HYPOGLYCEMIC EVENT | Hypoglycaemia | HYPOGLYCEMIC EVENT | Y | Y | 2013-09-24T6:48 | 2013-09-24T10:00 | HYPO2 |

## Source: `domains/SV/spec.md`

# SV — Subject Visits

> Class: Special-Purpose | Structure: One record per actual or planned visit per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain most relevant to the observation. The domain abbreviation is also used as a prefix for variables to ensure uniqueness when datasets are merged.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### VISITNUM
- **Order:** 4
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 5
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### SVPRESP
- **Order:** 6
- **Label:** Pre-specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to indicate whether the visit was planned (i.e., visits specified in the TV domain). Value is "Y" for planned visits, null for unplanned visits.

### SVOCCUR
- **Order:** 7
- **Label:** Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to record whether a planned visit occurred. The value is null for unplanned visits.

### SVREASOC
- **Order:** 8
- **Label:** Reason for Occur Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The reason for the value in SVOCCUR. If SVOCCUR="N", SVREASOC is the reason the visit did not occur.

### SVCNTMOD
- **Order:** 9
- **Label:** Contact Mode
- **Type:** Char
- **Controlled Terms:** C171445
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The way in which the visit was conducted. Examples: "IN PERSON", "TELEPHONE CALL", "IVRS".

### SVEPCHGI
- **Order:** 10
- **Label:** Epi/Pandemic Related Change Indicator
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates whether the visit was changed due to an epidemic or pandemic.

### VISITDY
- **Order:** 11
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### SVSTDTC
- **Order:** 12
- **Label:** Start Date/Time of Observation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of an observation represented in IS0 8601 character format.

### SVENDTC
- **Order:** 13
- **Label:** End Date/Time of Observation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time of the observation represented in IS0 8601 character format.

### SVSTDY
- **Order:** 14
- **Label:** Study Day of Start of Observation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### SVENDY
- **Order:** 15
- **Label:** Study Day of End of Observation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### SVUPDES
- **Order:** 16
- **Label:** Description of Unplanned Visit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of what happened to the subject during an unplanned visit. Only populated for unplanned visits.
---

## Cross References

### Controlled Terminology
- [Mode of Subject Contact (C171445)](../../terminology/core/special_purpose.md) — SVCNTMOD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — SVPRESP, SVOCCUR, SVEPCHGI

### Related Domains
- **Same class (Special-Purpose):** CO, DM, SE, SM

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)

## Source: `domains/SV/assumptions.md`

# SV — Assumptions

1. The Subject Visits domain allows the submission of data on the timing of the trial visits for a subject, including both those visits they actually passed through in their participation in the trial and those visits that did not occur. Refer to Section 7.3.1, Trial Visits (TV), as the TV dataset defines the planned visits for the trial.

2. Subjects can have 1 and only 1 record per VISITNUM.

3. Subjects who screen fail, withdraw, die, or otherwise discontinue study participation will not have records for planned visits subsequent to their final disposition event.

4. Planned and unplanned visits with a subject, whether or not they are physical visits to the investigational site, are represented in this domain.
   a. SVPRESP = "Y" identifies rows for planned visits.
   b. For planned visits, SVOCCUR indicates whether the visit occurred.
   c. For unplanned visits, SVPRESP and SVOCCUR are null.
   d. See Section 4.5.7, Presence or Absence of Prespecified Interventions and Events, for more information on the use of --PRESP and --OCCUR.

5. The identification of an actual visit with a planned visit sometimes calls for judgment. In general, data collection forms are prepared for particular visits, and the fact that data was collected on a form labeled with a planned visit is sufficient to make the association. Occasionally, the association will not be so clear, and the sponsor will need to make decisions about how to label actual visits. The sponsor's rules for making such decisions should be documented in the Define-XML document.

6. Records for unplanned visits should be included in the SV dataset. For unplanned visits, SVUPDES can be populated with a description of the reason for the unplanned visit. Some judgment may be required to determine what constitutes an unplanned visit. When data are collected outside a planned visit, that act of collecting data may or may not be described as a "visit." The encounter should generally be treated as a visit if data from the encounter are included in any domain for which VISITNUM is included; a record with a missing value for VISITNUM is generally less useful than a record with VISITNUM populated. If the occasion is considered a visit, its date/times must be included in the SV table and a value of VISITNUM must be assigned. Refer to Section 4.4.5, Clinical Encounters and Visits, for information on the population of visit variables for unplanned visits.

7. The variable SVCNTMOD is used to record the way in which the visit was conducted. For example, for visits to a clinic, SVCNTMOD = "IN PERSON", visits conducted remotely might have values such as "TELEPHONE", "REMOTE AUDIO VIDEO", or "IVRS". If there are multiple contact modes, refer to Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable.

8. The planned study day of visit variable (VISITDY) should not be populated for unplanned visits.

9. If SVSTDY is included, it is the actual study day corresponding to SVSTDTC. In studies for which VISITDY has been populated, it may be desirable to populate SVSTDY, as this will facilitate the comparison of planned (VISITDY) and actual (SVSTDY) study days for the start of a visit.

10. If SVENDY is included, it is the actual day corresponding to SVENDTC.

11. For many studies, all visits are assumed to occur within 1 calendar day, and only 1 date is collected for the visit. In such a case, the values for SVENDTC duplicate values in SVSTDTC. However, if the data for a visit is actually collected over several physical visits and/or over several days, then SVSTDTC and SVENDTC should reflect this fact. Note that it is fairly common for screening data to be collected over several days, but for the data to be treated as belonging to a single planned screening visit, even in studies for which all other visits are single-day visits.

12. Differentiating between planned and unplanned visits may be challenging if unplanned assessments (e.g., repeat labs) are performed during the time period of a planned visit.

13. Algorithms for populating SVSTDTC and SVENDTC from the dates of assessments performed at a visit may be particularly challenging for screening visits, since baseline values collected at a screening visit are sometimes historical data from tests performed before the subject started screening for the trial. Therefore dates prior to informed consent are not part of the determination of SVSTDTC.

14. The following Identifier variables are permissible and may be added as appropriate: --SEQ, --GRPID, --REFID, and --SPID.

15. Care should be taken in adding additional timing variables:
    a. If TAETORD and/or EPOCH are added, then the values must be those at the start of the visit.
    b. The purpose of --DTC and --DY in other domains with start and end dates (Event and Intervention Domains) is to record the date on which data was collected. For a visit that occurred, it is not necessary to submit the date on which information about the visit was collected. When SVPRESP = "Y" and SVOCCUR = "N", --DTC and --DY are available for use to represent the date on which it was recorded that the visit did not take place.
    c. --DUR could be added if the duration of a visit was collected.
    d. It would be inappropriate to add the variables that support time points (--TPT, --TPTNUM, --ELTM, --TPTREF, and --RFTDTC), because the topic of this dataset is visits.
    e. --STRF and --ENRF could be used to say whether a visit started and ended before, during, or after the study reference period, although this seems unnecessary.
    f. --STRTPT, --STTPT, --ENRTPT, and --ENTPT could be used to say that a visit started or ended before or after particular dates, although this seems unnecessary.

16. SVOCCUR = "N" records are only to be created for planned visits that were expected to occur before the end of the subject's participation.

## Source: `domains/SV/examples.md`

# SV — Examples

## Example 1

This example shows the planned visit schedule for a study, along with disposition and study events data for 3 subjects. For this study, data on screen failures were submitted. The study was disrupted by the COVID-19 pandemic after many subjects had completed the study.

This is the planned schedule of visits for the study in this example.

**Row 1:** The activities for the SCREEN visit may occur over up to 7 days.

**Row 2:** The day 1 visit is planned to start before the start of treatment and end after the start of treatment.

**Rows 3-7:** These visits are scheduled relative to the start of the treatment epoch.

**Row 8:** The follow-up visit is generally scheduled relative to the start of the treatment epoch, but may occur earlier if treatment is stopped early.

**tv.xpt**

| Row | STUDYID | DOMAIN | VISITNUM | VISIT | VISITDY | TVSTRL | TVENRL |
|-----|---------|--------|----------|-------|---------|--------|--------|
| 1 | 123456 | TV | 1 | SCREEN | | Start of Screening Epoch | Up to 7 days after start of the Screening Epoch |
| 2 | 123456 | TV | 2 | DAY 1 | 1 | On the day of, but before, the end of the Screen Epoch | On the day of, but after, the start of the Treatment Epoch |
| 3 | 123456 | TV | 3 | WEEK 1 | 8 | 1 week after the start of the Treatment Epoch | |
| 4 | 123456 | TV | 4 | WEEK 2 | 15 | 2 weeks after the start of the Treatment Epoch | |
| 5 | 123456 | TV | 5 | WEEK 4 | 29 | 4 weeks after the start of the Treatment Epoch | |
| 6 | 123456 | TV | 6 | WEEK 6 | 43 | 6 weeks after the start of the Treatment Epoch | |
| 7 | 123456 | TV | 7 | WEEK 8 | 57 | 8 weeks after the start of the Treatment Epoch | |
| 8 | 123456 | TV | 8 | FOLLOW-UP | | The earlier of 14 days after the last dose of treatment and 10 weeks after the start of the Treatment Epoch | At Trial Exit |

This table shows the disposition records for the subjects in this example.

**Row 1:** Shows informed consent for subject 37.

**Row 2:** Shows the subject 37 was discontinued due to screen failure. Note that because the subject did not start treatment, DSSTDY is not populated in their records.

**Row 3:** Shows informed consent for subject 85.

**Row 4:** Shows that subject 85 completed the study.

**Row 5:** Shows informed consent for subject 101.

**Row 6:** Shows that subject 101 chose to withdraw early.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSDTC | DSSTDTC | DSSTDY |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|-------|---------|--------|
| 1 | 123456 | DS | 37 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2019-09-10 | 2019-09-10 | |
| 2 | 123456 | DS | 37 | 2 | SCREEN FAILURE | SCREEN FAILURE | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2019-09-16 | 2019-09-16 | |
| 3 | 123456 | DS | 85 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2019-12-13 | 2019-12-13 | -6 |
| 4 | 123456 | DS | 85 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT | 2020-02-27 | 2020-02-27 | 72 |
| 5 | 123456 | DS | 101 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2020-02-13 | 2020-02-13 | -6 |
| 6 | 123456 | DS | 101 | 2 | WITHDRAWAL BY SUBJECT | WITHDRAWAL BY SUBJECT | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT | 2020-03-16 | 2020-03-16 | 28 |

Because the study in this example was disrupted by an epidemic, the permissible variable SVEPCHGI (Epi/Pandemic Related Change Indicator) was included in the SV dataset. As originally planned, visits were to be conducted in person, but pandemic disruption included conducting some visits remotely. When the change to a remote visit was a change due to the pandemic, SVEPCHGI = "Y".

**Row 1:** Shows that screening data for subject 37 was collected during a period of 4 days. This subject is shown as a screen failure in ds.xpt and therefore would have a null DM.RFSTDTC, hence the study day values in SVSTDY and SVENDY, which are based on the sponsor-defined reference start date, are null.

**Rows 2-3:** Show normal completion of the first 2 visits for subject 85.

**Row 4:** Shows that for subject 85, the visit called "WEEK 1" did not occur; the reason it did not occur is represented in SVREASOC.

**Rows 5-9:** Normal completion of remaining visits for subject 85.

**Row 10:** Data for the screening visit was gathered over the course of six days. For this and subsequent visits, SVPRESP = "Y" indicates that a visit was planned and SVOCCUR = "Y" indicates that the visit occurred.

**Row 11:** The visit called "DAY 1" started and ended as planned, on Day 1.

**Row 12:** The visit scheduled for Day 8 occurred one day early, on Day 7.

**Row 13:** The visit called "WEEK 2" did not occur due to clinic closure. SVOCCUR = "N" and SVREASOC contains the reason the visit did not occur.

**Row 14:** Shows an unscheduled visit. SVUPDES provides the information that this visit dealt with evaluation of an adverse event. Since this visit was not planned, VISITDY was not populated, SVPRESP and SVOCCUR are both null. VISITNUM is populated as required, but the sponsor chose not to populate VISIT. Data collected at this encounter may be in a Findings domain such as EG, LB, or VS, in which VISITNUM is treated as an important timing variable. This visit was over remote audio video due to having an adverse event during a pandemic.

**Row 15:** This subject had their last visit, a follow-up visit on study day 26, eight days after the unscheduled visit.

**sv.xpt**

| Row | STUDYID | DOMAIN | USUBJID | VISITNUM | VISIT | SVPRESP | SVOCCUR | SVREASOC | SVCNTMOD | SVEPCHGI | VISITDY | SVSTDTC | SVENDTC | SVSTDY | SVENDY | SVUPDES |
|-----|---------|--------|---------|----------|-------|---------|---------|----------|----------|----------|---------|---------|---------|--------|--------|---------|
| 1 | 123456 | SV | 37 | 1 | SCREEN | Y | Y | | IN PERSON | | | 2019-09-10 | 2019-09-16 | | | |
| 2 | 123456 | SV | 85 | 1 | SCREEN | Y | Y | | IN PERSON | | | 2019-12-13 | 2019-12-18 | -6 | -1 | |
| 3 | 123456 | SV | 85 | 2 | DAY 1 | Y | Y | | IN PERSON | | 1 | 2019-12-19 | 2019-12-19 | 1 | 1 | |
| 4 | 123456 | SV | 85 | 3 | WEEK 1 | Y | N | SUBJECT LACKED TRANSPORTATION | | | 8 | | | | | |
| 5 | 123456 | SV | 85 | 4 | WEEK 2 | Y | Y | | IN PERSON | | 15 | 2020-01-02 | 2020-01-02 | 15 | 15 | |
| 6 | 123456 | SV | 85 | 5 | WEEK 4 | Y | Y | | IN PERSON | | 29 | 2020-01-16 | 2020-01-16 | 30 | 30 | |
| 7 | 123456 | SV | 85 | 6 | WEEK 6 | Y | Y | | IN PERSON | | 43 | 2020-01-30 | 2020-01-30 | 43 | 43 | |
| 8 | 123456 | SV | 85 | 7 | WEEK 8 | Y | Y | | IN PERSON | | 57 | 2020-02-13 | 2020-02-13 | 57 | 57 | |
| 9 | 123456 | SV | 85 | 8 | FOLLOW-UP | Y | Y | | IN PERSON | | | 2020-02-27 | 2020-02-27 | 72 | 72 | |
| 10 | 123456 | SV | 101 | 1 | SCREEN | Y | Y | | IN PERSON | | | 2020-02-13 | 2020-02-18 | -6 | -1 | |
| 11 | 123456 | SV | 101 | 2 | DAY 1 | Y | Y | | IN PERSON | | 1 | 2020-02-19 | 2020-02-19 | 1 | 1 | |
| 12 | 123456 | SV | 101 | 3 | WEEK 1 | Y | Y | | IN PERSON | | 8 | 2020-02-25 | 2020-02-25 | 7 | 7 | |
| 13 | 123456 | SV | 101 | 4 | WEEK 2 | Y | N | CLINIC CLOSED DUE TO BAD WEATHER | | | 15 | | | | | |
| 14 | 123456 | SV | 101 | 4.1 | | | | | REMOTE AUDIO VIDEO | Y | | 2020-03-07 | 2020-03-07 | 18 | 18 | EVALUATION OF AE |
| 15 | 123456 | SV | 101 | 8 | FOLLOW-UP | Y | Y | | TELEPHONE CALL | Y | | 2020-03-16 | 2020-03-16 | 26 | 26 | |

## Source: `domains/CO/spec.md`

# CO — Comments

> Class: Special-Purpose | Structure: One record per comment per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### RDOMAIN
- **Order:** 3
- **Label:** Related Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** C66734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Two-character abbreviation for the domain of the parent record(s). Null for comments collected on a general comments or additional information CRF page.

### USUBJID
- **Order:** 4
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### COSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence Number given to ensure uniqueness of subject records within a domain. May be any valid number.

### IDVAR
- **Order:** 6
- **Label:** Identifying Variable
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifying variable in the parent dataset that identifies the record(s) to which the comment applies. Examples AESEQ or CMGRPID. Used only when individual comments are related to domain records. Null for comments collected on separate CRFs.

### IDVARVAL
- **Order:** 7
- **Label:** Identifying Variable Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Value of identifying variable of the parent record(s). Used only when individual comments are related to domain records. Null for comments collected on separate CRFs.

### COREF
- **Order:** 8
- **Label:** Comment Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference associated with the comment. May be the CRF page number (e.g., 650), or a module name (e.g., DEMOG), or a combination of information that identifies the reference (e.g. 650-VITALS-VISIT 2).

### COVAL
- **Order:** 9
- **Label:** Comment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** The text of the comment. Text over 200 characters can be added to additional columns COVAL1-COVALn. See Assumption 3.

### COEVAL
- **Order:** 10
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Example: "INVESTIGATOR".

### COEVALID
- **Order:** 11
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST", "RADIOLOGIST 1", "RADIOLOGIST 2".

### CODTC
- **Order:** 12
- **Label:** Date/Time of Comment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of comment on dedicated comment form. Should be null if this is a child record of another domain or if comment date was not collected.

### CODY
- **Order:** 13
- **Label:** Study Day of Comment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the comment, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.
---

## Cross References

### Controlled Terminology
- [SDTM Domain Abbreviation (C66734)](../../terminology/core/general_part4.md) — RDOMAIN
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — COEVAL
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — COEVALID

### Related Domains
- **Same class (Special-Purpose):** DM, SE, SM, SV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)

## Source: `domains/CO/assumptions.md`

# CO — Assumptions

1. The Comments special-purpose domain provides a solution for submitting free-text comments related to data in 1 or more SDTM domains (as described in Section 8.5, Relating Comments to a Parent Domain) or collected on a separate CRF page dedicated to comments. Comments are generally not responses to specific questions; instead, comments usually consist of voluntary free-text or unsolicited observations.

2. Although the structure for the Comments domain in the SDTM is "One record per comment", USUBJID is required in the comments domain for human clinical trials, so the structure of the Comments domain in the SDTMIG is "One record per comment per subject."

3. The CO dataset accommodates 3 sources of comments:
   a. Those unrelated to a specific domain or parent record(s), in which case the values of the variables RDOMAIN, IDVAR, and IDVARVAL are null. CODTC should be populated if captured. See Example 1, row 1.
   b. Those related to a domain but not to specific parent record(s), in which case the value of the variable RDOMAIN is set to the DOMAIN code of the parent domain and the variables IDVAR and IDVARVAL are null. CODTC should be populated if captured. See Example 1, row 2.
   c. Those related to a specific parent record or group of parent records, in which case the value of the variable RDOMAIN is set to the DOMAIN code of the parent record(s) and the variables IDVAR and IDVARVAL are populated with the key variable name and value of the parent record(s). Assumptions for populating IDVAR and IDVARVAL are further described in Section 8.5, Relating Comments to a Parent Domain. CODTC should be null because the timing of the parent record(s) is inherited by the comment record. See Example 1, rows 3-5.

4. When the comment text is longer than 200 characters, the first 200 characters of the comment will be in COVAL, the next 200 in COVAL1, and additional text stored as needed to COVALn. See Example 1, rows 3-4. Additional information about how to relate comments to parent SDTM records is provided in Section 8.5, Relating Comments to a Parent Domain.

5. The variable COREF may be null unless it is used to identify the source of the comment. See Example 1, rows 1 and 5.

6. Identifier variables and Timing variables may be added to the CO domain, but the following qualifiers would generally not be used in CO: --GRPID, --REFID, --SPID, TAETORD, --TPT, --TPTNUM, --ELTM, --TPTREF, --RFTDTC.

## Source: `domains/CO/examples.md`

# CO — Examples

## Example 1

**Row 1:** Shows a comment collected on a separate comments page. Since it was unrelated to any specific domain or record, RDOMAIN, IDVAR, and IDVARVAL are null.

**Row 2:** Shows a comment that was collected on the bottom of the PE page for Visit 7, without any indication of specific records it applied to. Since the comment related to a specific domain, RDOMAIN is populated. Since it was related to a specific visit, VISIT, COREF is "VISIT 7". However, since it does not relate to a specific record, IDVAR and IDVARVAL are null.

**Row 3:** Shows a comment related to a single AE record having its AESEQ=7.

**Row 4:** Shows a comment related to multiple EX records with EXGRPID = "COMBO1".

**Row 5:** Shows a comment related to multiple VS records with VSGRPID = "VS2".

**Row 6:** Shows one option for representing a comment collected on a visit-specific comments page not associated with a particular domain. In this case, the comment is linked to the Subject Visit record in SV (RDOMAIN = "SV") and IDVAR and IDVARVAL are populated link the comment to the particular visit.

**Row 7:** Shows a second option for representing a comment associated only with a visit. In this case, COREF is used to show that the comment is related to the particular visit.

**Row 8:** Shows a third option for representing a comment associated only with a visit. In this case, the VISITNUM variable was populated to indicate that the comment was associated with a particular visit.

**co.xpt**

| Row | STUDYID | DOMAIN | RDOMAIN | USUBJID | COSEQ | IDVAR | IDVARVAL | COREF | COVAL | COVAL1 | COVAL2 | COEVAL | VISITNUM | CODTC |
|-----|---------|--------|---------|---------|-------|-------|----------|-------|-------|--------|--------|--------|----------|-------|
| 1 | 1234 | CO | | AB-99 | 1 | | | | Comment text | | | PRINCIPAL INVESTIGATOR | | 2003-11-08 |
| 2 | 1234 | CO | PE | AB-99 | 2 | | | VISIT 7 | Comment text | | | PRINCIPAL INVESTIGATOR | | 2004-01-14 |
| 3 | 1234 | CO | AE | AB-99 | 3 | AESEQ | 7 | PAGE 650 | First 200 characters | Next 200 characters | Remaining text | PRINCIPAL INVESTIGATOR | | |
| 4 | 1234 | CO | EX | AB-99 | 4 | EXGRPID | COMBO1 | PAGE 320-355 | First 200 characters | | Remaining text | PRINCIPAL INVESTIGATOR | | |
| 5 | 1234 | CO | VS | AB-99 | 5 | VSGRPID | VS2 | | Comment text | | | PRINCIPAL INVESTIGATOR | | |
| 6 | 1234 | CO | SV | AB-99 | 6 | VISITNUM | 4 | | Comment Text | | | PRINCIPAL INVESTIGATOR | | |
| 7 | 1234 | CO | | AB-99 | 7 | | | VISIT 4 | Comment Text | | | PRINCIPAL INVESTIGATOR | | |
| 8 | 1234 | CO | | AB-99 | 8 | | | | Comment Text | | | PRINCIPAL INVESTIGATOR | 4 | |
