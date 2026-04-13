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
