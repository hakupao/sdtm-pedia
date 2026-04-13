# VS — Examples

## Example 1

This example shows results for 1 subject from 2 visits (i.e., baseline, visit 2).

**Rows 1-4, 6-7:** VSTPT and VSTPTNUM are populated because more than 1 measurement was taken at this visit.
**Rows 2, 4-5, 7-9:** VSLOBXFL="Y" indicates that the observation was used as the last observation before exposure measurement.
**Rows 10-11:** Show blood pressure observations obtained at visit 2.
**Row 12:** Shows a value collected in one unit, but converted to selected standard unit.
**Row 13:** Shows the proper use of the --STAT variable to indicate "NOT DONE" where a reason was collected when a test was not done.

**vs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | VSSEQ | VSTESTCD | VSTEST | VSPOS | VSORRES | VSORRESU | VSSTRESC | VSSTRESN | VSSTRESU | VSSTAT | VSREASND | VSLOC | VSLAT | VSLOBXFL | VISITNUM | VISIT | VISITDY | VSDTC | VSDY | VSTPT | VSTPTNUM |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|----------|----------|-------|---------|-------|------|-------|----------|
| 1 | ABC | VS | ABC-001-001 | 1 | SYSBP | Systolic Blood Pressure | SITTING | 154 | mmHg | 154 | 154 | mmHg | | | ARM | LEFT | | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE | 1 |
| 2 | ABC | VS | ABC-001-001 | 2 | SYSBP | Systolic Blood Pressure | SITTING | 152 | mmHg | 152 | 152 | mmHg | | | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE | 2 |
| 3 | ABC | VS | ABC-001-001 | 3 | DIABP | Diastolic Blood Pressure | SITTING | 44 | mmHg | 44 | 44 | mmHg | | | ARM | LEFT | | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE | 1 |
| 4 | ABC | VS | ABC-001-001 | 4 | DIABP | Diastolic Blood Pressure | SITTING | 48 | mmHg | 48 | 48 | mmHg | | | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE | 2 |
| 5 | ABC | VS | ABC-001-001 | 5 | PULSE | Pulse Rate | SITTING | 72 | beats/min | 72 | 72 | beats/min | | | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19 | 1 | | |
| 6 | ABC | VS | ABC-001-001 | 6 | TEMP | Temperature | | 34.7 | C | 34.7 | 34.7 | C | | | SUBLINGUAL REGION | | | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE | 1 |
| 7 | ABC | VS | ABC-001-001 | 7 | TEMP | Temperature | | 38.2 | C | 38.2 | 38.2 | C | | | SUBLINGUAL REGION | | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE | 2 |
| 8 | ABC | VS | ABC-001-001 | 8 | WEIGHT | Weight | STANDING | 90.5 | kg | 90.5 | 90.5 | kg | | | | | Y | 1 | Baseline | 1 | 1999-06-19 | 1 | | |
| 9 | ABC | VS | ABC-001-001 | 9 | HEIGHT | Height | STANDING | 157 | cm | 157 | 157 | cm | | | | | Y | 1 | Baseline | 1 | 1999-06-19 | 1 | | |
| 10 | ABC | VS | ABC-001-001 | 10 | SYSBP | Systolic Blood Pressure | SITTING | 95 | mmHg | 95 | 95 | mmHg | | | ARM | LEFT | | 2 | Visit 2 | 35 | 1999-07-21 | 33 | | |
| 11 | ABC | VS | ABC-001-001 | 11 | DIABP | Diastolic Blood Pressure | SITTING | 44 | mmHg | 44 | 44 | mmHg | | | ARM | LEFT | | 2 | Visit 2 | 35 | 1999-07-21 | 33 | | |
| 12 | ABC | VS | ABC-001-001 | 12 | TEMP | Temperature | | 97.16 | F | 38.2 | 36.2 | C | | | SUBLINGUAL REGION | | | 2 | Visit 2 | 35 | 1999-07-21 | 33 | | |
| 13 | ABC | VS | ABC-001-001 | 13 | WEIGHT | Weight | | | | | | | NOT DONE | SUBJECT REFUSED | | | | 2 | Visit 2 | 35 | 1999-07-21 | 33 | | |
