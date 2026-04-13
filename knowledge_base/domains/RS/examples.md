# RS — Examples

## RS — Examples - Disease Response

The following are examples for oncology response criteria.

### Example 1

This example shows response assessments determined from the TR domain based on RECIST 1.1 criteria and also shows a case where progressive disease due to symptomatic deterioration was determined based on a clinical assessment by the investigator.

**Rows 1-3:** Show the target response, non-target response, and the overall response by the investigator using RECIST 1.1 at the week 6 visit.
**Rows 4-7:** Show the target response and non-target response by the investigator using RECIST 1.1, as well as the determination of symptomatic determination (pleural effusion) and overall response using protocol-defined response criteria, at the week 12 visit.

**rs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | RSSEQ | RSLNKGRP | RSTESTCD | RSTEST | RSCAT | RSORRES | RSSTRESC | RSEVAL | VISITNUM | VISIT | RSDTC | RSDY |
|-----|---------|--------|---------|-------|----------|----------|--------|-------|---------|----------|--------|----------|-------|-------|------|
| 1 | ABC | RS | 44444 | 1 | | TRGRESP | Target Response | RECIST 1.1 | PR | PR | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 2 | ABC | RS | 44444 | 2 | | NTRGRESP | Non-target Response | RECIST 1.1 | SD | SD | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 3 | ABC | RS | 44444 | 3 | A2 | OVRLRESP | Overall Response | RECIST 1.1 | PR | PR | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 4 | ABC | RS | 44444 | 4 | | TRGRESP | Target Response | RECIST 1.1 | NE | NE | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 5 | ABC | RS | 44444 | 5 | | NTRGRESP | Non-target Response | RECIST 1.1 | NE | NE | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 6 | ABC | RS | 44444 | 6 | | SYMPTDTR | Symptomatic Deterioration | PROTOCOL DEFINED RESPONSE CRITERIA | Pleural Effusion | PD | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 7 | ABC | RS | 44444 | 7 | A3 | OVRLRESP | Overall Response | PROTOCOL DEFINED RESPONSE CRITERIA | PD | PD | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |

### Example 2

This example shows response assessments determined from the TR domain based on RECIST 1.1 criteria and also shows a confirmation of an equivocal new lesion progression.

**Rows 1-4:** Show the target response, non-target response, and the overall response by the independent assessor Radiologist 1 using RECIST 1.1 at the week 6 visit. At this week 6 visit, an equivocal new lesion was identified.
**Rows 5-8:** Show the target response, non-target response, and the overall response by the independent assessor Radiologist 1 using RECIST 1.1 at the week 12 visit. At this week 12 visit, the new lesion was determined to be unequivocally a new lesion.

**rs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | RSSEQ | RSLNKGRP | RSTESTCD | RSTEST | RSCAT | RSORRES | RSSTRESC | RSNAM | RSEVAL | RSEVALID | RSACPTFL | VISITNUM | VISIT | RSDTC | RSDY |
|-----|---------|--------|---------|-------|----------|----------|--------|-------|---------|----------|-------|--------|----------|----------|----------|-------|-------|------|
| 1 | ABC | RS | 55555 | 1 | | TRGRESP | Target Response | RECIST 1.1 | PR | PR | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 40 | WEEK 6 | 2010-02-18 | 46 |
| 2 | ABC | RS | 55555 | 2 | | NTRGRESP | Non-target Response | RECIST 1.1 | CR | CR | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 40 | WEEK 6 | 2010-02-18 | 46 |
| 3 | ABC | RS | 55555 | 3 | | NEWLPROG | New Lesion Progression | RECIST 1.1 | EQUIVOCAL | EQUIVOCAL | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 40 | WEEK 6 | 2010-02-18 | 46 |
| 4 | ABC | RS | 55555 | 4 | A2 | OVRLRESP | Overall Response | RECIST 1.1 | PR | PR | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 40 | WEEK 6 | 2010-02-18 | 46 |
| 5 | ABC | RS | 55555 | 5 | | TRGRESP | Target Response | RECIST 1.1 | PD | PD | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 60 | WEEK 12 | 2010-04-02 | 88 |
| 6 | ABC | RS | 55555 | 6 | | NTRGRESP | Non-target Response | RECIST 1.1 | CR | CR | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 60 | WEEK 12 | 2010-04-02 | 88 |
| 7 | ABC | RS | 55555 | 7 | | NEWLPROG | New Lesion Progression | RECIST 1.1 | UNEQUIVOCAL | UNEQUIVOCAL | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 60 | WEEK 12 | 2010-04-02 | 88 |
| 8 | ABC | RS | 55555 | 8 | A3 | OVRLRESP | Overall Response | RECIST 1.1 | PD | PD | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | Y | 60 | WEEK 12 | 2010-04-02 | 88 |

### Example 3

This example shows best response and the overall response of progression to prior therapies and follow-up therapies.

**Row 1:** Shows disease progression on or after a prior chemotherapy regimen. The date of progression is represented in RSDTC. RSENTPT and RSENRTPT represent that the disease progression was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the disease progression was unknown or not collected. RSPLNKGRP = "CM1" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM1".
**Row 2:** Shows best response to prior chemotherapy regimen. The date of best response is represented in RSDTC. RSENTPT and RSENRTPT represent that the best response was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the best response was unknown or not collected. RSPLNKGRP = "CM2" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM2".
**Row 3:** Shows best response to prior radiotherapy. The date of best response is represented in RSDTC. RSENTPT and RSENRTPT represent that the best response was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the best response was unknown or not collected. RSPLNKGRP = "PR2" is used to link this record in RS to the prior radiotherapy in PR where the PRLNKGRP = "PR2".
**Rows 4-5:** Show best response and progression to a follow-up anti-cancer therapy. The date of best response and date of progression are represented in RSDTC. RSSTTPT and RSSTRTPT represent that the best response and progression were after study treatment discontinuation. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the best response and progression was unknown or not collected. RSPLNKGRP = "CM3" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM3".

**rs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | RSSEQ | RSLNKGRP | RSTESTCD | RSTEST | RSCAT | RSORRES | RSORRESU | RSSTRESC | RSSTRESN | RSSTRESU | RSEVAL | VISITNUM | VISIT | RSDTC | RSDY | RSSTRTPT | RSSTTPT | RSENRTPT | RSENTPT |
|-----|---------|--------|---------|-------|----------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|------|----------|---------|----------|---------|
| 1 | ABC | RS | 55555 | 1 | CM1 | OVRLRESP | Overall Response | UNSPECIFIED | PD | | PD | | | INVESTIGATOR | 10 | SCREEN | 2015-02-18 | -32 | | | BEFORE | SCREEN |
| 2 | ABC | RS | 66666 | 2 | CM2 | BESTRESP | Best Response | UNSPECIFIED | SD | | SD | | | INVESTIGATOR | 10 | SCREEN | | | | | BEFORE | SCREEN |
| 3 | ABC | RS | 66666 | 3 | PR2 | BESTRESP | Best Response | UNSPECIFIED | MINIMAL RESPONSE | | MINIMAL RESPONSE | | | INVESTIGATOR | 10 | SCREEN | | | | | BEFORE | SCREEN |
| 4 | ABC | RS | 77777 | 4 | CM3 | BESTRESP | Best Response | UNSPECIFIED | SD | | SD | | | INVESTIGATOR | 240 | FOLLOW-UP MONTH 6 | 2015-04-02 | 520 | AFTER | STUDY TREATMENT DISCONTINUATION | | |
| 5 | ABC | RS | 77777 | 5 | CM3 | OVRLRESP | Overall Response | UNSPECIFIED | PD | | PD | | | INVESTIGATOR | 260 | FOLLOW-UP MONTH 8 | 2015-06-01 | 581 | AFTER | STUDY TREATMENT DISCONTINUATION | | |

## RS — Examples - Clinical Classifications

The following example is for a clinical classification. For additional RS examples, see the CDISC-published supplements for individual clinical classifications, at https://www.cdisc.org/standards/foundational/qrs.

### Example 1

**Glasgow Coma Scale NINDS Version (GCS NINDS VERSION)**

The rs.xpt dataset represents the items from the GCS NINDS VERSION instrument.

**rs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | RSSEQ | RSTESTCD | RSTEST | RSCAT | RSORRES | RSSTRESC | RSSTRESN | RSLOBXFL | VISITNUM | RSDTC |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|----------|----------|----------|----------|-------|
| 1 | STUDYX | RS | P0001 | 1 | GCS0101 | GCS01-Best Eye Response | GCS NINDS VERSION | No eye opening | 1 | 1 | Y | 1 | 2012-11-16 |
| 2 | STUDYX | RS | P0001 | 2 | GCS0102 | GCS01-Motor Response | GCS NINDS VERSION | Abnormal extension | 2 | 2 | Y | 1 | 2012-11-16 |
| 3 | STUDYX | RS | P0001 | 3 | GCS0103 | GCS01-Verbal Response | GCS NINDS VERSION | Incomprehensible sound | 2 | 2 | Y | 1 | 2012-11-16 |
| 4 | STUDYX | RS | P0001 | 4 | GCS0104 | GCS01-Total Score | GCS NINDS VERSION | 5 | 5 | 5 | Y | 1 | 2012-11-16 |
| 5 | STUDYX | RS | P0001 | 5 | GCS0105A | GCS01-Confounder: GCS Accurate | GCS NINDS VERSION | CHECKED | CHECKED | | Y | 1 | 2012-11-16 |
| 6 | STUDYX | RS | P0001 | 6 | GCS0105B | GCS01-Confounder: Paralytic | GCS NINDS VERSION | CHECKED | CHECKED | | Y | 1 | 2012-11-16 |
| 7 | STUDYX | RS | P0001 | 7 | GCS0105C | GCS01-Confounder: Alcohol/Drug of Abuse | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED | | Y | 1 | 2012-11-16 |
| 8 | STUDYX | RS | P0001 | 8 | GCS0105D | GCS01-Confounder: C-Spine Injury | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED | | Y | 1 | 2012-11-16 |
| 9 | STUDYX | RS | P0001 | 9 | GCS0105E | GCS01-Confounder: Hypoxia/Hypotension | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED | | Y | 1 | 2012-11-16 |
| 10 | STUDYX | RS | P0001 | 10 | GCS0105F | GCS01-Confounder: Hypothermia | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED | | Y | 1 | 2012-11-16 |
| 11 | STUDYX | RS | P0001 | 11 | GCS0105G | GCS01-Confounder: Sedation | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED | | Y | 1 | 2012-11-16 |
| 12 | STUDYX | RS | P0001 | 12 | GCS0105H | GCS01-Confounder: Unknown | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED | | Y | 1 | 2012-11-16 |

### References

1. Eisenhauer EA, Therasse P, Bogaerts J, et al. New response evaluation criteria in solid tumours: revised RECIST guideline (version 1.1). Eur J Cancer. 2009;45(2):228-247. doi:10.1016/j.ejca.2008.10.026
2. Cheson BD, Fisher RI, Barrington SF, et al. Recommendations for initial evaluation, staging, and response assessment of Hodgkin and non-Hodgkin lymphoma: the Lugano classification. J Clin Oncol. 2014;32(27):3059-3068. doi:10.1200/JCO.2013.54.8800
