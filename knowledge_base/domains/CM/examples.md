# CM — Examples

## Example 1

Sponsors collect the timing of concomitant medication use with varying specificity, depending on the pattern of use; the type, purpose, and importance of the medication; and the needs of the study. It is often unnecessary to record every unique instance of medication use, since the same information can be conveyed with start and end dates and frequency of use. If appropriate, medications taken as needed (intermittently or sporadically over a time period) may be reported with a start and end date and a frequency of "PRN".

The example below shows 3 subjects who took the same medication on the same day.

**Rows 1-6:** For subject ABC-0001, each instance of aspirin use was recorded separately, and the frequency in each record is (CMDOSFRQ) is "ONCE".

**Rows 7-9:** For subject ABC-0002, frequency was once a day ("QD") in the first and third records (where CMSEQ is "1" and "3"), but twice a day in the second record (CMSEQ = "2").

**Row 10:** Records for subject ABC-0003 are collapsed into a single entry that spans the relevant time period, with a frequency of "PRN". This is shown as an example only, not as a recommendation. This approach assumes that knowing exactly when aspirin was used is not important for evaluating safety and efficacy in this study.

**cm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMTRT | CMDOSE | CMDOSU | CMDOSFRQ | CMSTDTC | CMENDTC |
|-----|---------|--------|---------|-------|-------|--------|--------|----------|---------|---------|
| 1 | ABC | CM | ABC-0001 | 1 | ASPIRIN | 100 | mg | ONCE | 2004-01-01 | 2004-01-01 |
| 2 | ABC | CM | ABC-0001 | 2 | ASPIRIN | 100 | mg | ONCE | 2004-01-02 | 2004-01-02 |
| 3 | ABC | CM | ABC-0001 | 3 | ASPIRIN | 100 | mg | ONCE | 2004-01-03 | 2004-01-03 |
| 4 | ABC | CM | ABC-0001 | 4 | ASPIRIN | 100 | mg | ONCE | 2004-01-07 | 2004-01-07 |
| 5 | ABC | CM | ABC-0001 | 5 | ASPIRIN | 100 | mg | ONCE | 2004-01-07 | 2004-01-07 |
| 6 | ABC | CM | ABC-0001 | 6 | ASPIRIN | 100 | mg | ONCE | 2004-01-09 | 2004-01-09 |
| 7 | ABC | CM | ABC-0002 | 1 | ASPIRIN | 100 | mg | QD | 2004-01-01 | 2004-01-03 |
| 8 | ABC | CM | ABC-0002 | 2 | ASPIRIN | 100 | mg | BID | 2004-01-07 | 2004-01-07 |
| 9 | ABC | CM | ABC-0002 | 3 | ASPIRIN | 100 | mg | QD | 2004-01-09 | 2004-01-09 |
| 10 | ABC | CM | ABC-0003 | 1 | ASPIRIN | 100 | mg | PRN | 2004-01-01 | 2004-01-09 |

## Example 2

In this example study, it was of particular interest whether subjects use any anticonvulsant medications. The medication history, dosing, and so on was not of interest; the study only asked for the anticonvulsants to which subjects were exposed.

**cm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMTRT | CMCAT |
|-----|---------|--------|---------|-------|-------|-------|
| 1 | ABC123 | CM | 1 | 1 | LITHIUM | ANTI-CONVULSANT |
| 2 | ABC123 | CM | 1 | 2 | VPA | ANTI-CONVULSANT |

## Example 3

Sponsors often are interested in whether subjects are exposed to specific concomitant medications, and collect this information using a checklist. This example is for a study that had a particular interest in the antidepressant medications that subjects used. For the study's purposes, absence is just as important as presence of a medication. This can be clearly shown using CMOCCUR.

In this example, CMPRESP shows that the subjects were specifically asked if they use any of 3 antidepressants (Zoloft, Prozac, and Paxil). The value of CMOCCUR indicates the response to the prespecified medication question. CMSTAT indicates whether the response was missing for a prespecified medication, and CMREASND shows the reason for missing response. The medication details (e.g., dose, frequency) were not of interest in this study.

**Row 1:** Medication use was solicited and the medication was taken.

**Row 2:** Medication use was solicited and the medication was not taken.

**Row 3:** Medication use was solicited, but data were not collected. The reason for the lack of a response was collected and is represented in CMREASND.

**cm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMTRT | CMPRESP | CMOCCUR | CMSTAT | CMREASND |
|-----|---------|--------|---------|-------|-------|---------|---------|--------|----------|
| 1 | ABC123 | CM | 1 | 1 | ZOLOFT | Y | Y | | |
| 2 | ABC123 | CM | 1 | 2 | PROZAC | Y | N | | |
| 3 | ABC123 | CM | 1 | 3 | PAXIL | Y | | NOT DONE | Didn't ask due to interruption |

## Example 4

In this hepatitis C study, collection of data on prior treatments included reason for discontinuation. Because hepatitis C is usually treated with a combinations of medications, CMGRPID was used to group records into regimens.

**Rows 1-3:** This subject's treatment consisted of the 3 medications grouped by means of CMGRPID = "1". The subject completed the scheduled treatment.

**Rows 4-6:** Another subject received the same set of 3 medications. The medications for this subject are also grouped using CMGRPID = "1". Note, however, that the fact that the same CMGRPID value has been used for the same set of medications for subjects "ABC123-765" and "ABC123-899" is coincidence; CMGRPID groups records only within a subject. This subject stopped the regimen due to side effects.

**cm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMGRPID | CMTRT | CMCAT | CMDOSFRM | CMROUTE | CMRSDISC |
|-----|---------|--------|---------|-------|---------|-------|-------|----------|---------|----------|
| 1 | ABC123 | CM | ABC123-765 | 1 | 1 | PEGINTRON | HCV TREATMENT | INJECTION | SUBCUTANEOUS | COMPLETED SCHEDULED TREATMENT |
| 2 | ABC123 | CM | ABC123-765 | 2 | 1 | RIBAVIRIN | HCV TREATMENT | TABLET | ORAL | COMPLETED SCHEDULED TREATMENT |
| 3 | ABC123 | CM | ABC123-765 | 3 | 1 | BOCEPREVIR | HCV TREATMENT | TABLET | ORAL | COMPLETED SCHEDULED TREATMENT |
| 4 | ABC123 | CM | ABC123-899 | 1 | 1 | PEGINTRON | HCV TREATMENT | INJECTION | SUBCUTANEOUS | TOXICITY/INTOLERANCE |
| 5 | ABC123 | CM | ABC123-899 | 2 | 1 | RIBAVIRIN | HCV TREATMENT | TABLET | ORAL | TOXICITY/INTOLERANCE |
| 6 | ABC123 | CM | ABC123-899 | 3 | 1 | BOCEPREVIR | HCV TREATMENT | TABLET | ORAL | TOXICITY/INTOLERANCE |

## Example 5

In this rheumatoid arthritis (RA) study, the sponsor collected medications using the category "Prior RA Medications", then collected information on whether the subject had received certain medication classes, represented as subcategories. If a subject did receive medications in a subcategory, information about those medications was collected. This example shows data for 2 subjects who received prior RA medications. It includes data only about their prior disease-modifying antirheumatic drugs (DMARDs); information about other kinds of prior RA medications is not included.

**Row 1:** Shows that subject 101 received prior RA medications. The values of CMTRT and CMCAT are the same, indicating that this record represents the response to a question about a category of medications, rather than an individual medication.

**Row 2:** Shows that subject 101 did not receive prior DMARDs. The values in CMTRT and CMSCAT are the same, indicating that this record represents the response to a question about a group of medications, rather than an individual medication.

**Row 3:** Shows that subject 102 received prior RA medications.

**Row 4:** Shows that subject 102 received prior DMARDs.

**Rows 5-6:** Show 2 prior DMARDS received by subject 102, one ending before the date of data collection, and the other ongoing at that time. These medications were not prespecified, so CMPRESP is null.

**cm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMTRT | CMCAT | CMSCAT | CMPRESP | CMOCCUR | CMINDC | CMDTC | CMDY | CMENRTPT | CMENTPT |
|-----|---------|--------|---------|-------|-------|-------|--------|---------|---------|--------|-------|------|----------|---------|
| 1 | ABC123 | CM | 101 | 1 | PRIOR RA MEDICATIONS | PRIOR RA MEDICATIONS | | Y | Y | RHEUMATOID ARTHRITIS | 2020-02-02 | -1 | | |
| 2 | ABC123 | CM | 101 | 2 | PRIOR DMARDS | PRIOR RA MEDICATIONS | PRIOR DMARDS | Y | N | RHEUMATOID ARTHRITIS | 2020-02-02 | -1 | | |
| 3 | ABC123 | CM | 102 | 1 | PRIOR RA MEDICATIONS | PRIOR RA MEDICATIONS | | Y | Y | RHEUMATOID ARTHRITIS | 2020-01-25 | -3 | | |
| 4 | ABC123 | CM | 102 | 2 | PRIOR DMARDS | PRIOR RA MEDICATIONS | PRIOR DMARDS | Y | Y | RHEUMATOID ARTHRITIS | 2020-01-25 | -3 | | |
| 5 | ABC123 | CM | 102 | 3 | SULFASALAZINE | PRIOR RA MEDICATIONS | PRIOR DMARDS | | | RHEUMATOID ARTHRITIS | 2020-01-25 | -3 | BEFORE | 2020-01-25 |
| 6 | ABC123 | CM | 102 | 4 | METHOTREXATE | PRIOR RA MEDICATIONS | PRIOR DMARDS | | | RHEUMATOID ARTHRITIS | 2020-01-25 | -3 | ONGOING | 2020-01-25 |
