# PE — Examples

## Example 1

This example shows data for 1 subject collected at 1 visit. The data come from a general physical examination.

**Rows 1-2, 6:** Show how PESTRESC is populated if result is "NORMAL".
**Rows 3-5:** Show how PESPID is used to show the sponsor-defined identifier, which in this case is the CRF sequence number used for identifying abnormalities within a body system. Additionally, the abnormalities were encoded; PESTRESC represents the MedDRA Preferred Term and PEBODSYS represents the MedDRA system organ class.

**pe.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PESEQ | PESPID | PETESTCD | PETEST | PELOC | PELAT | PEBODSYS | PEORRES | PESTRESC | VISITNUM | VISIT | VISITDY | PEDTC | PEDY |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|-------|----------|---------|----------|----------|-------|---------|-------|------|
| 1 | ABC | PE | ABC-001-001 | 1 | | HEAD | Head | | | | NORMAL | NORMAL | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 2 | ABC | PE | ABC-001-001 | 2 | | ENT | Ear/Nose/Throat | | | | NORMAL | NORMAL | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 3 | ABC | PE | ABC-001-001 | 3 | 1 | SKIN | Skin | FACE | | Skin and subcutaneous tissue disorder | ACNE | Acne | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 4 | ABC | PE | ABC-001-001 | 4 | 2 | SKIN | Skin | HANDS | | Skin and subcutaneous tissue disorder | DERMATITIS | Dermatitis | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 5 | ABC | PE | ABC-001-001 | 5 | 3 | SKIN | Skin | ARM | LEFT | Skin and subcutaneous tissue disorder | SKIN RASH | Rash | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 6 | ABC | PE | ABC-001-001 | 6 | | HEART | Heart | | | | NORMAL | NORMAL | -1 | BASELINE | -1 | 1999-06-06 | -3 |
