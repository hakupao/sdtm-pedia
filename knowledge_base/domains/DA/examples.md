# DA — Examples

## Example 1

This example shows drug accounting for a study with 2 study medications and one rescue medication, all of which were measured in tablets. The sponsor chose to add EPOCH from the list of timing variables and to use DASPID and DAREFID for code numbers that appeared on the label.

**da.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DASEQ | DAREFID | DASPID | DATESTCD | DATEST | DACAT | DAORRES | DAORRESU | DASTRESC | DASTRESN | DASTRESU | VISITNUM | EPOCH | DADTC |
|-----|---------|--------|---------|-------|---------|--------|----------|--------|-------|---------|----------|----------|----------|----------|----------|-------|-------|
| 1 | ABC | DA | ABC-01001 | 1 | XBYCC-E990A | A375827 | DISPAMT | Dispensed Amount | Study Medication | Bottle A | 30 | TABLET | 30 | TABLET | 1 | Study Med Period 1 | 2004-06-15 |
| 2 | ABC | DA | ABC-01001 | 2 | XBYCC-E990A | A375827 | RETAMT | Returned Amount | Study Medication | Bottle A | 5 | TABLET | 5 | TABLET | 2 | Study Med Period 1 | 2004-07-15 |
| 3 | ABC | DA | ABC-01001 | 3 | XBYCC-E990B | A227588 | DISPAMT | Dispensed Amount | Study Medication | Bottle B | 15 | TABLET | 15 | TABLET | 1 | Study Med Period 1 | 2004-06-15 |
| 4 | ABC | DA | ABC-01001 | 4 | XBYCC-E990B | A227588 | RETAMT | Returned Amount | Study Medication | Bottle B | 0 | TABLET | 0 | TABLET | 2 | Study Med Period 1 | 2004-07-15 |
| 5 | ABC | DA | ABC-01001 | 5 | | | DISPAMT | Dispensed Amount | Rescue Medication | | 10 | TABLET | 10 | TABLET | 1 | | 2004-06-15 |
| 6 | ABC | DA | ABC-01001 | 6 | | | RETAMT | Returned Amount | Rescue Medication | | 10 | TABLET | 10 | TABLET | 2 | | 2004-07-15 |

## Example 2

In this study, drug containers, rather than their contents, were being accounted for and the sponsor did not track returns. In this case, the purpose of accountability tracking is to verify that the containers dispensed were consistent with the randomization. The sponsor chose to use DASPID to record the identifying number of the container dispensed.

**da.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DASEQ | DASPID | DATESTCD | DATEST | DACAT | DAORRES | DAORRESU | DASTRESC | DASTRESN | DASTRESU | VISITNUM | DADTC |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|---------|----------|----------|----------|----------|----------|-------|
| 1 | ABC | DA | ABC-01001 | 1 | AB001 | DISPAMT | Dispensed Amount | Study Medication | Drug A | 1 | CONTAINER | 1 | CONTAINER | 1 | 2004-06-15 |
| 2 | ABC | DA | ABC-01001 | 2 | AB002 | DISPAMT | Dispensed Amount | Study Medication | Drug B | 1 | CONTAINER | 1 | CONTAINER | 1 | 2004-06-15 |

## Example 3

This example shows, for a nutrition study, the volume of infant feeding formula prepared and the volume of formula remaining after feeding.

**Rows 1-2:** Show the volume of formula prepared and the volume of formula left after feeding for the first feed of the diary (day 1).

**Rows 3-4:** Show the volume of formula prepared and the volume of formula left after feeding for the second feed of the diary (day 1).

**Rows 5-6:** Show the volume of formula prepared and the volume of formula left after feeding for the third feed of the diary (day 2).

**da.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DASEQ | DAGRPID | DATESTCD | DATEST | DACAT | DAORRES | DAORRESU | DASTRESC | DASTRESN | DASTRESU | DADTC | DADY |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|-------|------|
| 1 | ABC | DA | 101 | 1 | 1 | PREPAMT | Prepared Amount | Study Product | 100 | mL | 100 | 100 | mL | 2017-05-19 | 1 |
| 2 | ABC | DA | 101 | 2 | 1 | REMAMT | Remaining Amount | Study Product | 15 | mL | 15 | 15 | mL | 2017-05-19 | 1 |
| 3 | ABC | DA | 101 | 3 | 2 | PREPAMT | Prepared Amount | Study Product | 100 | mL | 100 | 100 | mL | 2017-05-19 | 1 |
| 4 | ABC | DA | 101 | 4 | 2 | REMAMT | Remaining Amount | Study Product | 25 | mL | 25 | 25 | mL | 2017-05-19 | 1 |
| 5 | ABC | DA | 101 | 5 | 3 | PREPAMT | Prepared Amount | Study Product | 100 | mL | 100 | 100 | mL | 2017-05-20 | 2 |
| 6 | ABC | DA | 101 | 6 | 3 | REMAMT | Remaining Amount | Study Product | 10 | mL | 10 | 10 | mL | 2017-05-20 | 2 |
