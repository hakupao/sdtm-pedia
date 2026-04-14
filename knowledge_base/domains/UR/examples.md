# UR — Examples

## Example 1

This example shows measurements of the kidney, number of renal arteries and veins, and presence/absence results for prespecified abnormalities of the kidneys. These findings were made using computed tomography (CT) imaging.

**Row 1:** Shows that the subject's left kidney was measured to be 126 mm long.
**Row 2:** Shows that the subject's left kidney had 2 renal arteries.
**Row 3:** Shows that the subject's left kidney had 1 renal vein.
**Row 4:** Shows that no hematomas were found in the kidney. If a hematoma had been present, the variable URLOC (with URDIR as necessary) would have specified where within the kidney.
**Row 5:** Shows that surgical damage was noted in the superior portion of the kidney cortex. Note that in SDTM, there is no way to clearly distinguish between the use of --LOC as a qualifier of --TEST vs. as a qualifier of results, as it is used here.

ur.xpt

| Row | STUDYID | DOMAIN | USUBJID | URSEQ | URTESTCD | URTEST | URORRES | URORRESU | URSTRESC | URSTRESN | URSTRESU | URLOC | URLAT | URDIR | URMETHOD | URDTC |
|-----|---------|--------|---------|-------|----------|--------|---------|----------|----------|----------|----------|-------|-------|-------|----------|-------|
| 1 | ABC | UR | ABC-001-011 | 1 | LENGTH | Length | 12.6 | cm | 126 | 126 | mm | KIDNEY | LEFT | | CT SCAN | 2016-03-30 |
| 2 | ABC | UR | ABC-001-011 | 2 | RNLANUM | Number of Renal Arteries | 2 | | 2 | 2 | | KIDNEY | LEFT | | CT SCAN | 2016-03-30 |
| 3 | ABC | UR | ABC-001-011 | 3 | RNLVNUM | Number of Renal Veins | 1 | | 1 | 1 | | KIDNEY | LEFT | | CT SCAN | 2016-03-30 |
| 4 | ABC | UR | ABC-001-011 | 4 | HEMAIND | Hematoma Indicator | N | | N | | | KIDNEY | | | CT SCAN | 2016-03-30 |
| 5 | ABC | UR | ABC-001-011 | 5 | SGDMGIND | Surgical Damage Indicator | Y | | Y | | | KIDNEY, CORTEX | LEFT | SUPERIOR | CT SCAN | 2016-03-30 |

## Example 2

This example shows a subject's renal blood flow measurement for each visit based on the subject's para-amino hippuric acid (PAH) clearance, indicated by URMETHOD = "PARA-AMINO HIPPURIC ACID CLEARANCE".

ur.xpt

| Row | STUDYID | DOMAIN | USUBJID | URSEQ | URTESTCD | URTEST | URORRES | URORRESU | URSTRESC | URSTRESN | URSTRESU | URLOC | URLAT | URMETHOD | VISITNUM | VISIT | URDTC |
|-----|---------|--------|---------|-------|----------|--------|---------|----------|----------|----------|----------|-------|-------|----------|----------|-------|-------|
| 1 | DEF | UR | DEF-0123 | 1 | BLDFLRT | Blood Flow Rate | 20 | mL/min | 20 | 20 | mL/min | KIDNEY | BILATERAL | PARA-AMINO HIPPURIC ACID CLEARANCE | 1 | VISIT 1 | 2016-03-15 |
| 2 | DEF | UR | DEF-0123 | 2 | BLDFLRT | Blood Flow Rate | 10 | mL/min | 10 | 10 | mL/min | KIDNEY | LEFT | PARA-AMINO HIPPURIC ACID CLEARANCE | 2 | VISIT 2 | 2016-03-20 |
| 3 | DEF | UR | DEF-0123 | 3 | BLDFLRT | Blood Flow Rate | 10 | mL/min | 10 | 10 | mL/min | KIDNEY | RIGHT | PARA-AMINO HIPPURIC ACID CLEARANCE | 3 | VISIT 3 | 2016-04-07 |
