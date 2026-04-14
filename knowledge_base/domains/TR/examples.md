# TR — Examples

Note: TU and TR share examples. See also [TU Examples](../TU/examples.md).

## Example 2 (continued from TU)

TR shows measurements (i.e., short axis) of lymph nodes as well as measurements of other non-lymph node target tumors (i.e., longest diameter). In this example, when TRTEST = "Tumor State" and TRORRES = "ABSENT", it indicates that the target lymph node lesion was no longer pathological (i.e., diameter reduced below 10mm). The overall assessment of lymph nodes is represented with TRTEST = "Lymph Nodes State". A lymph node state of "NON-PATHOLOGICAL" means that all target lymph node lesions have a short axis less than 10mm. A lymph node state of "PATHOLOGICAL" means that at least 1 target lymph node lesion has a short axis greater than or equal to 10mm.

**Rows 1-8:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the screening visit.

**Rows 9-21:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 6 visit.

**Rows 22-27:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 12 visit.

**tr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | TRSEQ | TRGRPID | TRLNKGRP | TRLNKID | TRTESTCD | TRTEST | TRORRES | TRORRESU | TRSTRESC | TRSTRESN | TRSTRESU | TRSTAT | TREASND | TRMETHOD | TREVAL | VISITNUM | VISIT | TRDTC | TRDY |
|-----|---------|--------|---------|-------|---------|----------|---------|----------|--------|---------|----------|----------|----------|----------|--------|---------|----------|--------|----------|-------|-------|------|
| 1 | ABC | TR | 44444 | 1 | TARGET | A1 | T01 | DIAMETER | Diameter | 17 | mm | 17 | 17 | mm | | | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 2 | ABC | TR | 44444 | 2 | TARGET | A1 | T02 | DIAMETER | Diameter | 16 | mm | 16 | 16 | mm | | | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 3 | ABC | TR | 44444 | 3 | TARGET | A1 | T03 | DIAMETER | Diameter | 15 | mm | 15 | 15 | mm | | | MRI | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 4 | ABC | TR | 44444 | 4 | TARGET | A1 | T04 | DIAMETER | Diameter | 14 | mm | 14 | 14 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 10 | SCREEN | 2010-01-03 | -1 |
| 5 | ABC | TR | 44444 | 5 | TARGET | A1 | | SUMDIAM | Sum of Diameter | 62 | mm | 62 | 62 | mm | | | | INVESTIGATOR | 10 | SCREEN | | |
| 6 | ABC | TR | 44444 | 6 | TARGET | A1 | | SUMNLNLD | Sum Diameters of Non-Lymph Node Tumors | 47 | mm | 47 | 47 | mm | | | | INVESTIGATOR | 10 | SCREEN | | |
| 7 | ABC | TR | 44444 | 7 | NON-TARGET | A1 | NT01 | TUMSTATE | Tumor State | PRESENT | | PRESENT | | | | | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -2 |
| 8 | ABC | TR | 44444 | 8 | NON-TARGET | A1 | NT02 | TUMSTATE | Tumor State | PRESENT | | PRESENT | | | | | MRI | INVESTIGATOR | 10 | SCREEN | 2010-01-02 | |
| 9 | ABC | TR | 44444 | 9 | TARGET | A2 | T01 | DIAMETER | Diameter | 0 | mm | 0 | 0 | mm | | | CT SCAN | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 10 | ABC | TR | 44444 | 10 | TARGET | A2 | T02 | DIAMETER | Diameter | TOO SMALL TO MEASURE | mm | 5 | 5 | mm | | | CT SCAN | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 11 | ABC | TR | 44444 | 11 | TARGET | A2 | T03 | DIAMETER | Diameter | 12 | mm | 12 | 12 | mm | | | MRI | INVESTIGATOR | 40 | WEEK 6 | 2010-02-19 | 47 |
| 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
| 13 | ABC | TR | 44444 | 13 | TARGET | A2 | T04.2 | DIAMETER | Diameter | 7 | mm | 7 | 7 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
| 14 | ABC | TR | 44444 | 14 | TARGET | A2 | | SUMDIAM | Sum of Diameter | 30 | mm | 30 | 30 | mm | | | | INVESTIGATOR | 40 | | WEEK 6 | |
| 15 | ABC | TR | 44444 | 15 | TARGET | A2 | | SUMNLNLD | Sum Diameters of Non-Lymph Node Tumors | 18 | mm | 18 | 18 | mm | | | | INVESTIGATOR | 40 | | WEEK 6 | |
| 16 | ABC | TR | 44444 | 16 | TARGET | A2 | | LNSTATE | Lymph Node State | PATHOLOGICAL | | PATHOLOGICAL | | | | | | INVESTIGATOR | 40 | | WEEK 6 | |
| 17 | ABC | TR | 44444 | 17 | TARGET | A2 | | ACNSD | Absolute Change Nadir in Sum of Diam | -32 | mm | -32 | -32 | mm | | | | INVESTIGATOR | 40 | | WEEK 6 | |
| 18 | ABC | TR | 44444 | 18 | TARGET | A2 | | PCBSD | Percent Change From Baseline in Sum of Diameter | -52 | % | -52 | -52 | % | | | | INVESTIGATOR | 40 | | WEEK 6 | |
| 19 | ABC | TR | 44444 | 19 | TARGET | A2 | | PCNSD | Percent Change Nadir in Sum of Diam | -52 | % | -52 | -52 | % | | | | INVESTIGATOR | 40 | | WEEK 6 | |
| 20 | ABC | TR | 44444 | 20 | NON-TARGET | A2 | NT01 | TUMSTATE | Tumor State | PRESENT | | PRESENT | | | | | CT SCAN | INVESTIGATOR | 40 | WEEK 6 | 2010-02-18 | 46 |
| 21 | ABC | TR | 44444 | 21 | NON-TARGET | A2 | NT02 | TUMSTATE | Tumor State | PRESENT | | PRESENT | | | | | MRI | INVESTIGATOR | 40 | WEEK 6 | 2010-02-19 | 47 |
| 22 | ABC | TR | 44444 | 22 | TARGET | A3 | T01 | DIAMETER | Diameter | 0 | mm | 0 | 0 | mm | | | CT SCAN | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 23 | ABC | TR | 44444 | 23 | TARGET | A3 | T02 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | CT SCAN | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 24 | ABC | TR | 44444 | 24 | TARGET | A3 | T03 | DIAMETER | Diameter | | | | | | NOT DONE | SCAN NOT PERFORMED | MRI | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | |
| 25 | ABC | TR | 44444 | 25 | TARGET | A3 | T04 | DIAMETER | Diameter | | | | | | NOT DONE | NOT ASSESSABLE: IMAGE OBSCURED TUMOR | PHOTOGRAPHY | INVESTIGATOR | 60 | WEEK 12 | | |
| 26 | ABC | TR | 44444 | 26 | NON-TARGET | A3 | NT01 | TUMSTATE | Tumor State | | | | | | NOT DONE | POOR IMAGE INEQUALITY | CT SCAN | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |
| 27 | ABC | TR | 44444 | 27 | NON-TARGET | A3 | NT02 | TUMSTATE | Tumor State | | | | | | NOT DONE | SCAN NOT PERFORMED | MRI | INVESTIGATOR | 60 | WEEK 12 | | |

The relationship between the TU and TR datasets is represented in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | TU | | TULNKID | | ONE | 1 |
| 2 | ABC | TR | | TRLNKID | | MANY | 1 |

## Example 3 (continued from TU)

TR shows assessments provided by an independent assessor as opposed to the principal investigator.

**Rows 1-7:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the screening visit by the independent assessor, Radiologist 1.

**Rows 8-19:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 6 visit by the independent assessor, Radiologist 1.

**Rows 20-32:** Show the measurements of the target tumors and other assessments of the target and non-target tumors at the week 12 visit by the independent assessor, Radiologist 1.

**tr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | TRSEQ | TRGRPID | TRLNKGRP | TRLNKID | TRTESTCD | TRTEST | TRORRES | TRORRESU | TRSTRESC | TRSTRESN | TRSTRESU | TRMETHOD | TRNAM | TREVAL | TREVALID | VISITNUM | VISIT | TRDTC | TRDY |
|-----|---------|--------|---------|-------|---------|----------|---------|----------|--------|---------|----------|----------|----------|----------|----------|-------|--------|----------|----------|-------|-------|------|
| 1 | ABC | TR | 55555 | 1 | TARGET | A1 | R1-T01 | DIAMETER | Diameter | 20 | mm | 20 | 20 | mm | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-02 | -2 |
| 2 | ABC | TR | 55555 | 2 | TARGET | A1 | R1-T02 | DIAMETER | Diameter | 15 | mm | 15 | 15 | mm | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 | -3 |
| 3 | ABC | TR | 55555 | 3 | TARGET | A1 | R1-T03 | DIAMETER | Diameter | 15 | mm | 15 | 15 | mm | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 | -3 |
| 4 | ABC | TR | 55555 | 4 | TARGET | A1 | | SUMDIAM | Sum of Diameter | 50 | mm | 50 | 50 | mm | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | | |
| 5 | ABC | TR | 55555 | 5 | TARGET | A1 | | SUMNLNLD | Sum Diameters of Non-Lymph Node Tumors | 30 | mm | 30 | 30 | mm | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | | |
| 6 | ABC | TR | 55555 | 6 | NON-TARGET | A1 | R1-NT01 | TUMSTATE | Tumor State | PRESENT | | PRESENT | | | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 | -2 |
| 7 | ABC | TR | 55555 | 7 | NON-TARGET | A1 | R1-NT02 | TUMSTATE | Tumor State | PRESENT | | PRESENT | | | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-02 | 1 |
| 8 | ABC | TR | 55555 | 8 | TARGET | A2 | R1-T01 | DIAMETER | Diameter | 12 | mm | 12 | 12 | mm | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-18 | 46 |
| 9 | ABC | TR | 55555 | 9 | TARGET | A2 | R1-T02 | DIAMETER | Diameter | 0 | mm | 0 | 0 | mm | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-18 | 47 |
| 10 | ABC | TR | 55555 | 10 | TARGET | A2 | R1-T03 | DIAMETER | Diameter | 13 | mm | 13 | 13 | mm | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-19 | 47 |
| 11 | ABC | TR | 55555 | 11 | TARGET | A2 | | SUMDIAM | Sum of Diameter | 25 | mm | 25 | 25 | mm | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
| 12 | ABC | TR | 55555 | 12 | TARGET | A2 | | SUMNLNLD | Sum Diameters of Non-Lymph Node Tumors | 13 | mm | 13 | 13 | mm | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
| 13 | ABC | TR | 55555 | 13 | TARGET | A2 | | LNSTATE | Lymph Nodes State | PATHOLOGICAL | | PATHOLOGICAL | | | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
| 14 | ABC | TR | 55555 | 14 | TARGET | A2 | | ACNSD | Absolute Change From Nadir in Sum of Diameters | -25 | mm | -25 | -25 | mm | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
| 15 | ABC | TR | 55555 | 15 | TARGET | A2 | | PCBSD | Percent Change From Baseline in Sum of Diameters | -50 | % | -50 | -50 | % | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
| 16 | ABC | TR | 55555 | 16 | TARGET | A2 | | PCNSD | Percent Change Nadir in Sum of Diameters | -50 | % | -50 | -50 | % | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
| 17 | ABC | TR | 55555 | 17 | NON-TARGET | A2 | R1-NT01 | TUMSTATE | Tumor State | ABSENT | | ABSENT | | | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-19 | 47 |
| 18 | ABC | TR | 55555 | 18 | NON-TARGET | A2 | R1-NT02 | TUMSTATE | Tumor State | ABSENT | | ABSENT | | | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-18 | 46 |
| 19 | ABC | TR | 55555 | 19 | NON-TARGET | A2 | R1-NEW01 | TUMSTATE | Tumor State | EQUIVOCAL | | EQUIVOCAL | | | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-18 | |
| 20 | ABC | TR | 55555 | 20 | TARGET | A2 | R1-NEW01 | DIAMETER | Diameter | 7 | mm | 7 | 7 | mm | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-18 | 55 |
| 21 | ABC | TR | 55555 | 21 | TARGET | A3 | R1-T01 | DIAMETER | Diameter | 20 | mm | 20 | 20 | mm | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 88 |
| 22 | ABC | TR | 55555 | 22 | TARGET | A3 | R1-T02 | DIAMETER | Diameter | 10 | mm | 10 | 10 | mm | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 85 |
| 23 | ABC | TR | 55555 | 23 | TARGET | A3 | | SUMDIAM | Sum of Diameter | 37 | mm | 37 | 37 | mm | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | | |
| 24 | ABC | TR | 55555 | 24 | TARGET | A3 | | SUMNLNLD | Sum Diameters of Non-Lymph Node Tumors | 30 | mm | 30 | 30 | mm | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | | |
| 25 | ABC | TR | 55555 | 25 | TARGET | A3 | | LNSTATE | Lymph Nodes State | NONPATHOLOGICAL | | NONPATHOLOGICAL | | | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | | |
| 26 | ABC | TR | 55555 | 26 | TARGET | A3 | | ACNSD | Absolute Change Nadir in Sum of Diameters | 17 | mm | 17 | 17 | mm | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | | |
| 27 | ABC | TR | 55555 | 27 | TARGET | A3 | | PCBSD | Percent Change From Baseline in Sum of Diameters | -50 | % | -50 | -50 | % | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | | |
| 28 | ABC | TR | 55555 | 28 | TARGET | A3 | | PCNSD | Percent Change Nadir in Sum of Diameters | -50 | % | -50 | -50 | % | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | | |
