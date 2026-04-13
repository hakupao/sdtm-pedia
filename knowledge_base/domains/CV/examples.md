# CV — Examples

## Example 1

This example shows various findings related to the aortic artery, along with evaluation for the presence or absence of abdominal aortic aneurysms. The suprarenal, infrarenal, and thoracic sections of the aorta were examined for aneurysms. This level of anatomical location detail can be found in CVLOC. The records in rows 1 to 3 are related assessments regarding an aneurysm in the thoracic aorta and are grouped together using the CVGRPID variable.

**cv.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CVSEQ | CVGRPID | CVTESTCD | CVTEST | CVORRES | CVSTRESC | CVLOC | CVMETHOD | VISITNUM | VISIT | CVDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|---------|----------|-------|----------|----------|-------|-------|
| 1 | ABC123 | CV | 002-2004 | 1 | 2 | ANEURIND | Aneurysm Indicator | Y | Y | THORACIC AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 2 | ABC123 | CV | 002-2004 | 2 | 2 | DISECIND | Dissection Indicator | Y | Y | THORACIC AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 3 | ABC123 | CV | 002-2004 | 3 | 2 | STANFADC | Stanford AoD Classification | CLASS A | CLASS A | THORACIC AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 4 | ABC123 | CV | 002-2004 | 4 | | ANEURIND | Aneurysm Indicator | N | N | SUPRARENAL AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |
| 5 | ABC123 | CV | 002-2004 | 5 | | ANEURIND | Aneurysm Indicator | N | N | INFRARENAL AORTA | TRANSTHORACIC ECHOCARDIOGRAPHY | 2 | BASELINE | 2015-06-09T14:20 |

## Example 2

In this example CVTEST represents the structure of the aortic valve evaluated during a transthoracic echocardiography procedure.

**cv.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CVSEQ | NCVALTYP | CVTESTCD | CVTEST | CVCAT | CVORRES | CVORRESU | CVSTRESC | CVSTRESN | CVSTRESU | CVLOC | CVMETHOD | VISITNUM | VISIT | CVDTC |
|-----|---------|--------|---------|-------|----------|----------|--------|-------|---------|----------|----------|----------|----------|-------|----------|----------|-------|-------|
| 1 | ABC123 | CV | 1001 | 1 | | NCVALTYP | Native Cardiac Valve Structure Without Intervention Type | VALVULAR STRUCTURE, COMMON | NATIVE, WITHOUT INTERVENTION | | NATIVE, WITHOUT INTERVENTION | | | AORTIC VALVE | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 2 | ABC123 | CV | 1001 | 2 | | SIZE | Size | VALVULAR STRUCTURE, COMMON | REDUCED | | REDUCED | | | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 3 | ABC123 | CV | 1001 | 3 | | MNDIAEVS | Minor Axis Cross-sec Diameter, EVS | VALVULAR STRUCTURE, COMMON | 2.18 | cm | 2.18 | 2.18 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 4 | ABC123 | CV | 1001 | 4 | | MJDIAEVS | Major Axis Cross-sec Diameter, EVS | VALVULAR STRUCTURE, COMMON | 2.48 | cm | 2.48 | 2.48 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 5 | ABC123 | CV | 1001 | 5 | | MNDIAEVD | Minor Axis Cross-sec Diameter, EVD | VALVULAR STRUCTURE, COMMON | 1.92 | cm | 1.92 | 1.92 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 6 | ABC123 | CV | 1001 | 6 | | MJDIAEVD | Major Axis Cross-sec Diameter, EVD | VALVULAR STRUCTURE, COMMON | 2.58 | cm | 2.58 | 2.58 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 7 | ABC123 | CV | 1001 | 7 | | MNDIAMVS | Minor Axis Cross-sec Diameter, MVS | VALVULAR STRUCTURE, COMMON | 2.11 | cm | 2.11 | 2.11 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
| 8 | ABC123 | CV | 1001 | 8 | | MJDIAMVS | Major Axis Cross-sec Diameter, MVS | VALVULAR STRUCTURE, COMMON | 2.39 | cm | 2.39 | 2.39 | cm | AORTIC VALVE ANNULUS | TRANSTHORACIC ECHOCARDIOGRAPHY | 5 | MONTH 2 | 2015-08-05T11:15 |
