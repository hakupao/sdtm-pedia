# MS — Examples

*Note: MB and MS share a combined examples section (6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples). MS-specific data tables are shown here; see also MB examples for organism identification data from the same studies.*

## Example 1

This example shows susceptibility testing results following organism identification. After E. faecalis was identified in the subject sample (see MB Example 1), drug susceptibility testing was performed at each of the labs using both the sponsor's investigational drug and amoxicillin.

**Rows 1-4:** Show the minimum inhibitory concentration and the interpretation result reported from Central Lab ABC from a sample that was tested for susceptibility to the sponsor drug and amoxicillin, using an epsilometer test method.
**Rows 5-6:** Show that Local Lab XYZ found that the sample was susceptible to the sponsor drug at a concentration of 0.5 ug/dL and resistant to amoxicillin at a concentration of 0.5 ug/dL.
**Rows 7-10:** Show the diameter of the zone of inhibition and the interpretation result reported from Local Lab XYZ from a sample that was tested for susceptibility to the sponsor drug and amoxicillin using a disk diffusion test method.

**ms.xpt**

| Row | STUDYID | DOMAIN | USUBJID | NHOID | MSGRPID | MSSEQ | MSREFID | MSLNKGRP | MSTESTCD | MSTEST | MSAGENT | MSCONC | MSCONCU | MSORRES | MSORRESU | MSSTRESC | MSSTRESN | MSSTRESU | MSNAM | MSMETHOD | MSDTC |
|-----|---------|--------|---------|-------|---------|-------|---------|----------|----------|--------|---------|--------|---------|---------|----------|----------|----------|----------|-------|----------|-------|
| 1 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 1 | 1 | SPEC01 | | MIC | Minimum Inhibitory Concentration | Sponsor Drug | 0.25 | ug/dL | 0.25 | ug/dL | | | | CENTRAL LAB ABC | EPSILOMETER | 2005-06-19T08:00 |
| 2 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 1 | 2 | SPEC01 | | MICROSUS | Microbial Susceptibility | Sponsor Drug | | | SUSCEPTIBLE | | SUSCEPTIBLE | | | CENTRAL LAB ABC | EPSILOMETER | 2005-06-19T08:00 |
| 3 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 2 | 3 | SPEC01 | | MIC | Minimum Inhibitory Concentration | Amoxicillin | 1 | ug/dL | 1 | ug/dL | | | | CENTRAL LAB ABC | EPSILOMETER | 2005-06-19T08:00 |
| 4 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 2 | 4 | SPEC01 | | MICROSUS | Microbial Susceptibility | Amoxicillin | | | RESISTANT | | RESISTANT | | | CENTRAL LAB ABC | EPSILOMETER | 2005-06-19T08:00 |
| 5 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | | 5 | SPEC01 | 2 | MICROSUS | Microbial Susceptibility | Sponsor Drug | 0.5 | ug/dL | SUSCEPTIBLE | | SUSCEPTIBLE | | | LOCAL LAB XYZ | MACRO BROTH DILUTION | 2005-06-19T08:00 |
| 6 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | | 6 | SPEC01 | 2 | MICROSUS | Microbial Susceptibility | Amoxicillin | 0.5 | ug/dL | RESISTANT | | RESISTANT | | | LOCAL LAB XYZ | MACRO BROTH DILUTION | 2005-06-19T08:00 |
| 7 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 3 | 7 | SPEC01 | 2 | DIAZOINH | Diameter of the Zone of Inhibition | Sponsor Drug | | | 23 | mm | 23 | 23 | mm | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-19T08:00 |
| 8 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 3 | 8 | SPEC01 | 2 | MICROSUS | Microbial Susceptibility | Sponsor Drug | | | SUSCEPTIBLE | | SUSCEPTIBLE | | | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-19T08:00 |
| 9 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 4 | 9 | SPEC01 | 2 | DIAZOINH | Diameter of the Zone of Inhibition | Amoxicillin | | | 25 | mm | 25 | 25 | mm | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-19T08:00 |
| 10 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 4 | 10 | SPEC01 | 2 | MICROSUS | Microbial Susceptibility | Amoxicillin | | | RESISTANT | | RESISTANT | | | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-19T08:00 |

## Example 2

Susceptibility testing results from the sputum multi-visit study (see MB Example 2).

**Rows 1-2:** Show that the sponsor drug (MSAGENT) was tested against "STREPTOCOCCUS PNEUMONIAE" (NHOID) from subject sample SP01 and that the drug has a minimum inhibitory concentration (MSTESTCD/MSTEST) of 0.004 mg/L (row 1). This led to the conclusion that this organism is susceptible to that drug (row 2).
**Rows 3-4:** Show that penicillin was tested against the same organism from the same sample and found to have a minimum inhibitory concentration of 0.023 mg/L (row 3). This led to the conclusion that "STREPTOCOCCUS PNEUMONIAE" is resistant to penicillin (row 4).
**Rows 5-8:** Similar to rows 1-4, the sponsor drug (rows 5-6) and penicillin (rows 7-8) were tested against "KLEBSIELLA PNEUMONIAE" from an additional sample at a later time point. Results from these tests indicated that the organism was susceptible to sponsor drug, yet had intermediate resistance to penicillin.
**Rows 9-10:** A test against "KLEBSIELLA PNEUMONIAE" from an additional sample at a later time point showed little change in the minimum inhibitory concentration of penicillin, and that the organism is still classified as having intermediate resistance to penicillin.

**ms.xpt**

| Row | STUDYID | DOMAIN | USUBJID | NHOID | MSGRPID | MSSEQ | MSREFID | MSTESTCD | MSTEST | MSAGENT | MSORRES | MSORRESU | MSSTRESC | MSSTRESN | MSSTRESU | MSNAM | MSMETHOD | VISITNUM | VISIT | MSDTC |
|-----|---------|--------|---------|-------|---------|-------|---------|----------|--------|---------|---------|----------|----------|----------|----------|-------|----------|----------|-------|-------|
| 1 | ABC | MS | ABC-001-001 | STREPTOCOCCUS PNEUMONIAE | | 1 | SP01 | MIC | Minimum Inhibitory Concentration | Sponsor Drug | 0.004 | mg/L | 0.004 | 0.004 | mg/L | | EPSILOMETER | 1 | VISIT 1 | 2005-06-19T08:00 |
| 2 | ABC | MS | ABC-001-001 | STREPTOCOCCUS PNEUMONIAE | | 2 | SP01 | MICROSUS | Microbial Susceptibility | Sponsor Drug | SUSCEPTIBLE | | SUSCEPTIBLE | | | | EPSILOMETER | 1 | VISIT 1 | 2005-06-19T08:00 |
| 3 | ABC | MS | ABC-001-001 | STREPTOCOCCUS PNEUMONIAE | | 3 | SP01 | MIC | Minimum Inhibitory Concentration | Penicillin | 0.125 | mg/L | 0.125 | 0.125 | mg/L | | EPSILOMETER | 1 | VISIT 1 | 2005-06-19T08:00 |
| 4 | ABC | MS | ABC-001-001 | STREPTOCOCCUS PNEUMONIAE | | 4 | SP01 | MICROSUS | Microbial Susceptibility | Penicillin | RESISTANT | | RESISTANT | | | | EPSILOMETER | 1 | VISIT 1 | 2005-06-19T08:00 |
| 5 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | | 5 | SP02 | MIC | Minimum Inhibitory Concentration | Sponsor Drug | 0.19 | mg/L | 0.19 | 0.19 | mg/L | | EPSILOMETER | 2 | VISIT 2 | 2005-06-26T08:00 |
| 6 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | | 6 | SP02 | MICROSUS | Microbial Susceptibility | Sponsor Drug | SUSCEPTIBLE | | SUSCEPTIBLE | | | | EPSILOMETER | 2 | VISIT 2 | 2005-06-26T08:00 |
| 7 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | | 7 | SP02 | MIC | Minimum Inhibitory Concentration | Penicillin | 4.9 | mg/L | 4.9 | 4.9 | mg/L | | EPSILOMETER | 2 | VISIT 2 | 2005-06-26T08:00 |
| 8 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | | 8 | SP02 | MICROSUS | Microbial Susceptibility | Penicillin | SUSCEPTIBLE | | SUSCEPTIBLE | | | | EPSILOMETER | 2 | VISIT 2 | 2005-06-26T08:00 |
| 9 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | | 9 | SP03 | MIC | Minimum Inhibitory Concentration | Penicillin | 4.8 | mg/L | 4.8 | 4.8 | mg/L | | EPSILOMETER | 3 | VISIT 3 | 2005-07-01T08:00 |
| 10 | ABC | MS | ABC-001-001 | KLEBSIELLA PNEUMONIAE | | 10 | SP03 | MICROSUS | Microbial Susceptibility | Penicillin | SUSCEPTIBLE | | SUSCEPTIBLE | | | | EPSILOMETER | 3 | VISIT 3 | 2005-07-01T08:00 |

## Example 3

Results from drug susceptibility tests performed on samples from the gastric TB study (see MB Example 3) are represented in the MS domain. This includes all phenotypic tests (where the drug is added directly to a culture medium) and genotypic tests (when the result is given as susceptible or resistant). In this example, the variable NHOID (Non-host Organism Identifier) is populated with the name of the organism that is the subject of the test.

**Rows 1-2:** Show phenotypic testing results on 2 separate culture plates: 1 with medium containing rifampicin (row 1) and 1 with medium containing isoniazid (row 2). MSAGENT is populated with the name of the drug being used in the susceptibility test. The variables MSCONC and MSCONCU represent the concentration and units of the drug being used. The culture start and stop dates are represented in BE and can be linked to MS by BELNKID and MSLNKID.
**Rows 3-4:** Show genotypic susceptibility testing results on the same aliquot from a NAAT that looks for mutations that confer resistance to 2 drugs. MSAGENT should be populated with the name of the drug whose action is affected by the mutation being tested for. However, because the drug is not used in the test, MSCONC and MSCONCU should be null. These results are represented in MS because the only result given is in terms of resistant/susceptible; no genetic results are reported.

**ms.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | NHOID | MSSEQ | MSREFID | MSLNKID | MSTESTCD | MSTEST | MSAGENT | MSCONC | MSCONCU | MSORRES | MSSTRESC | MSSPEC | MSLOC | MSMETHOD | MSDTC |
|-----|---------|--------|---------|---------|-------|-------|---------|---------|----------|--------|---------|--------|---------|---------|----------|--------|-------|----------|-------|
| 1 | ABC | MS | ABC-01-101 | | MYCOBACTERIUM TUBERCULOSIS | 1 | 100.4 | 2 | MICROSUS | Microbial Susceptibility | Rifampicin | 1 | ug/mL | RESISTANT | RESISTANT | LAVAGE FLUID | STOMACH | ANTIBIOTIC AGAR SCREEN | 2011-01-17T06:00 |
| 2 | ABC | MS | ABC-01-101 | | MYCOBACTERIUM TUBERCULOSIS | 2 | 100.5 | 3 | MICROSUS | Microbial Susceptibility | Isoniazid | 0.2 | ug/mL | SUSCEPTIBLE | SUSCEPTIBLE | LAVAGE FLUID | STOMACH | ANTIBIOTIC AGAR SCREEN | 2011-01-17T06:00 |
| 3 | ABC | MS | ABC-01-101 | ABC765 | MYCOBACTERIUM TUBERCULOSIS | 3 | 100.2 | | MICROSUS | Microbial Susceptibility | Rifampicin | | | RESISTANT | RESISTANT | LAVAGE FLUID | STOMACH | NUCLEIC ACID AMPLIFICATION TEST | 2011-01-17T06:00 |
| 4 | ABC | MS | ABC-01-101 | ABC765 | MYCOBACTERIUM TUBERCULOSIS | 4 | 100.2 | | MICROSUS | Microbial Susceptibility | Isoniazid | | | SUSCEPTIBLE | SUSCEPTIBLE | LAVAGE FLUID | STOMACH | NUCLEIC ACID AMPLIFICATION TEST | 2011-01-17T06:00 |

**suppms.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|
| 1 | ABC | MS | ABC-01-101 | MBREFID | 100.4 | MSMEDTYPE | Medium Type | LOWENSTEIN-JENSEN | Collected |
| 2 | ABC | MS | ABC-01-101 | MBREFID | 100.5 | MSMEDTYPE | Medium Type | LOWENSTEIN-JENSEN | Collected |
