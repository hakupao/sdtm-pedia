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
