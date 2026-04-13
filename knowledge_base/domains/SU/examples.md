# SU — Examples

## Example 1

This example illustrates how typical SU data could be populated. Here, the CRF collected:

- Smoking data
   - Smoking status of "previous", "current", or "never"
   - If a current or past smoker, number of packs per day
   - If a former smoker, the year the subject quit
- Current caffeine use
   - What caffeine drinks subjects consumed today
   - How many cups today

SUCAT allows the records to be grouped into smoking-related data and caffeine-related data. In this example, the treatments are prespecified on the CRF page, so SUTRT does not require a standardized SUDECOD equivalent.

**Not shown:** A subject who never smoked does not have a tobacco record. Alternatively, a row for the subject could have been included with SUOCCUR = "N" and null dosing and timing fields; the interpretation would be the same. A subject who did not drink any caffeinated drinks on the day of the assessment does not have any caffeine records. A subject who never smoked and did not drink caffeinated drinks on the day of the assessment does not appear in the dataset.

**Row 1:** Subject 1234005 is a 2-pack/day current smoker. "Current" implies that smoking started sometime before the time the question was asked (SUSTTPT = "2006-01-01", SUSTRTPT = "BEFORE") and had not ended as of that date (SUENTPT = "2006-01-01", SUENRTPT = "ONGOING"). See Section 4.4.7, Use of Relative Timing Variables for the use of these variables. Both the beginning and ending reference time points for this question are the date of the assessment.

**Row 2:** Subject 1234005 drank 3 cups of coffee on the day of the assessment.

**Row 3:** Subject 1234006 is a former smoker. The date this subject began smoking is unknown, but it was sometime before the assessment date; this is shown by the values of SUSTTPT and SUSTRTPT. The end date of smoking was collected, so SUENTPT and SUENRTPT are not populated. Instead, the end date is in SUENDTC.

**Row 4:** Subject 1234006 drank tea on the day of the assessment.

**Row 5:** Subject 1234006 drank coffee on the day of the assessment.

**Row 6:** Subject 1234007 had missing data for the smoking questions; this is indicated by SUSTAT = "NOT DONE". The reason is in SUREASND.

**Row 7:** Subject 1234007 also had missing data for all of the caffeine questions.

**su.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SUSEQ | SUTRT | SUCAT | SUSTAT | SUREASND | SUDOSE | SUDOSU | SUDOSFRQ | SUSTDTC | SUENDTC | SUSTTPT | SUSTRTPT | SUENTPT | SUENRTPT |
|-----|---------|--------|---------|-------|-------|-------|--------|----------|--------|--------|----------|---------|---------|---------|----------|---------|----------|
| 1 | 1234 | SU | 1234005 | 1 | CIGARETTES | TOBACCO | | | 2 | PACK | QD | | | 2006-01-01 | BEFORE | 2006-01-01 | ONGOING |
| 2 | 1234 | SU | 1234005 | 2 | COFFEE | CAFFEINE | | | 3 | CUP | QD | 2006-01-01 | 2006-01-01 | | | | |
| 3 | 1234 | SU | 1234006 | 1 | CIGARETTES | TOBACCO | | | 1 | PACK | QD | | 2003 | 2006-03-15 | BEFORE | | |
| 4 | 1234 | SU | 1234006 | 2 | TEA | CAFFEINE | | | 1 | CUP | QD | 2006-03-15 | 2006-03-15 | | | | |
| 5 | 1234 | SU | 1234006 | 3 | COFFEE | CAFFEINE | | | 2 | CUP | QD | 2006-03-15 | 2006-03-15 | | | | |
| 6 | 1234 | SU | 1234007 | 1 | CIGARETTES | TOBACCO | NOT DONE | Subject left office before CRF was completed | | | | | | | | | |
| 7 | 1234 | SU | 1234007 | 2 | CAFFEINE | CAFFEINE | NOT DONE | Subject left office before CRF was completed | | | | | | | | | |
