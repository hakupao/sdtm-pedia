# SR — Examples

## Example 1

In this example, the subject is dosed with increasing concentrations of Johnson grass IgE.

**Rows 1-4:** Show responses associated with the administration of a histamine control.
**Rows 5-8:** Show responses associated with the administration of Johnson grass IgE. These records describe the dose response to different concentrations of Johnson grass IgE antigen, as reflected in SROBJ.

All rows show a specific location on the back (e.g., SITE1), represented in FOCID.

**sr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FOCID | SRSEQ | SRTESTCD | SRTEST | SROBJ | SRORRES | SRORRESU | SRSTRESC | SRSTRESN | SRSTRESU | SRLOC | VISITNUM | VISIT |
|-----|---------|--------|---------|-------|-------|----------|--------|-------|---------|----------|----------|----------|----------|-------|----------|-------|
| 1 | SPI-001 | SR | SPI-001-11035 | SITE1 | 1 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 5 | mm | 5 | 5 | mm | BACK | 1 | VISIT 1 |
| 2 | SPI-001 | SR | SPI-001-11035 | SITE2 | 2 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 4 | mm | 4 | 4 | mm | BACK | 1 | VISIT 1 |
| 3 | SPI-001 | SR | SPI-001-11035 | SITE3 | 3 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 5 | mm | 5 | 5 | mm | BACK | 1 | VISIT 1 |
| 4 | SPI-001 | SR | SPI-001-11035 | SITE4 | 4 | FLRMDIAM | Flare Mean Diameter | Histamine Control 10 mg/mL | 5 | mm | 5 | 5 | mm | BACK | 1 | VISIT 1 |
| 5 | SPI-001 | SR | SPI-001-11035 | SITE5 | 5 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.05 BAU/mL | 10 | mm | 10 | 10 | mm | BACK | 1 | VISIT 1 |
| 6 | SPI-001 | SR | SPI-001-11035 | SITE6 | 6 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.10 BAU/mL | 11 | mm | 11 | 11 | mm | BACK | 1 | VISIT 1 |
| 7 | SPI-001 | SR | SPI-001-11035 | SITE7 | 7 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.15 BAU/mL | 20 | mm | 20 | 20 | mm | BACK | 1 | VISIT 1 |
| 8 | SPI-001 | SR | SPI-001-11035 | SITE8 | 8 | FLRMDIAM | Flare Mean Diameter | Johnson Grass 0.20 BAU/mL | 30 | mm | 30 | 30 | mm | BACK | 1 | VISIT 1 |

## Example 2

In this example, the study product dose, Dog Epi IgG, was administered at increasing concentrations. The size of the wheal is being measured (reaction to Dog Epi IgG) to evaluate the efficacy of the Dog Epi IgG extract versus a negative control (NC) and a positive control (PC) in the testing of allergenic extracts. While SROBJ is populated with information about the substance administered, full details regarding the study product would be submitted in the Exposure (EX) dataset. The relationship between SR records and EX records would be represented using RELREC.

**Rows 1-6:** Show the response (description and reaction grade) to the study product at a series of different dose levels, the latter reflected in SROBJ. The descriptions of SRORRES values are correlated to a grade, and the grade values are stored in SRSTRESC.
**Rows 7-12:** Show the results of wheal diameter measurements in response to the study product at a series of different dose levels.

**sr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SRSEQ | SRSPID | SRTESTCD | SRTEST | SROBJ | SRORRES | SRORRESU | SRSTRESC | SRSTRESN | SRSTRESU | SRLOC | VISITNUM | VISIT |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|---------|----------|----------|----------|----------|-------|----------|-------|
| 1 | CC-001 | SR | CC-001-101 | 1 | 1 | REACTGR | Reaction Grade | Dog Epi 0 mg | NEGATIVE | | NEGATIVE | | | FOREARM | 1 | WEEK 1 |
| 2 | CC-001 | SR | CC-001-101 | 2 | 2 | REACTGR | Reaction Grade | Dog Epi 0.1 mg | NEGATIVE | | NEGATIVE | | | FOREARM | 1 | WEEK 1 |
| 3 | CC-001 | SR | CC-001-101 | 3 | 3 | REACTGR | Reaction Grade | Dog Epi 0.5 mg | ERYTHEMA, INFILTRATION, POSSIBLY DISCRETE PAPULES | | 1+ | | | FOREARM | 1 | WEEK 1 |
| 4 | CC-001 | SR | CC-001-101 | 4 | 4 | REACTGR | Reaction Grade | Dog Epi 1 mg | ERYTHEMA, INFILTRATION, PAPULES, VESICLES | | 2+ | | | FOREARM | 1 | WEEK 1 |
| 5 | CC-001 | SR | CC-001-101 | 5 | 5 | REACTGR | Reaction Grade | Dog Epi 1.5 mg | ERYTHEMA, INFILTRATION, PAPULES, VESICLES | | 2+ | | | FOREARM | 1 | WEEK 1 |
| 6 | CC-001 | SR | CC-001-101 | 6 | 6 | REACTGR | Reaction Grade | Dog Epi 2 mg | ERYTHEMA, INFILTRATION, PAPULES, COALESCING VESICLES | | 3+ | | | FOREARM | 1 | WEEK 1 |
| 7 | CC-001 | SR | CC-001-101 | 7 | 7 | FLRMDIAM | Flare Mean Diameter | Dog Epi 0 mg | 5 | mm | 5 | 5 | mm | FOREARM | 1 | WEEK 1 |
| 8 | CC-001 | SR | CC-001-101 | 8 | 8 | FLRMDIAM | Flare Mean Diameter | Dog Epi 0.1 mg | 10 | mm | 10 | 10 | mm | FOREARM | 1 | WEEK 1 |
| 9 | CC-001 | SR | CC-001-101 | 9 | 9 | FLRMDIAM | Flare Mean Diameter | Dog Epi 0.5 mg | 22 | mm | 22 | 22 | mm | FOREARM | 1 | WEEK 1 |
| 10 | CC-001 | SR | CC-001-101 | 10 | 10 | FLRMDIAM | Flare Mean Diameter | Dog Epi 1 mg | 100 | mm | 100 | 100 | mm | FOREARM | 1 | WEEK 1 |
| 11 | CC-001 | SR | CC-001-101 | 11 | 11 | FLRMDIAM | Flare Mean Diameter | Dog Epi 1.5 mg | 1 | mm | 1 | 1 | mm | FOREARM | 1 | WEEK 1 |
| 12 | CC-001 | SR | CC-001-101 | 12 | 12 | FLRMDIAM | Flare Mean Diameter | Dog Epi 2 mg | 8 | mm | 8 | 8 | mm | FOREARM | 1 | WEEK 1 |

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSPID | EXTRT | EXDOSE | EXDOSEU | EXROUTE | EXLOC |
|-----|---------|--------|---------|--------|-------|--------|---------|---------|-------|
| 1 | CC-001 | EX | 101 | 1 | Dog Epi IgG | 0 | mg | CUTANEOUS | FOREARM |
| 2 | CC-001 | EX | 101 | 2 | Dog Epi IgG | 0.1 | mg | CUTANEOUS | FOREARM |
| 3 | CC-001 | EX | 101 | 3 | Dog Epi IgG | 0.5 | mg | CUTANEOUS | FOREARM |
| 4 | CC-001 | EX | 101 | 4 | Dog Epi IgG | 1 | mg | CUTANEOUS | FOREARM |
| 5 | CC-001 | EX | 101 | 5 | Dog Epi IgG | 1.5 | mg | CUTANEOUS | FOREARM |
| 6 | CC-001 | EX | 101 | 6 | Dog Epi IgG | 2 | mg | CUTANEOUS | FOREARM |

The relationships between SR and EX records are represented at the record level in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | CC-001 | SR | CC-001-101 | SRSPID | 1 | | R1 |
| 2 | CC-001 | EX | CC-001-101 | EXSPID | 1 | | R1 |
| 3 | CC-001 | SR | CC-001-101 | SRSPID | 7 | | R1 |
| 4 | CC-001 | SR | CC-001-101 | SRSPID | 2 | | R2 |
| 5 | CC-001 | EX | CC-001-101 | EXSPID | 2 | | R2 |
| 6 | CC-001 | SR | CC-001-101 | SRSPID | 8 | | R2 |
| 7 | CC-001 | SR | CC-001-101 | SRSPID | 3 | | R3 |
| 8 | CC-001 | EX | CC-001-101 | EXSPID | 3 | | R3 |
| 9 | CC-001 | SR | CC-001-101 | SRSPID | 9 | | R3 |
| 10 | CC-001 | SR | CC-001-101 | SRSPID | 4 | | R4 |
| 11 | CC-001 | SR | CC-001-101 | SRSPID | 10 | | R4 |
| 12 | CC-001 | EX | CC-001-101 | EXSPID | 4 | | R4 |
| 13 | CC-001 | SR | CC-001-101 | SRSPID | 5 | | R5 |
| 14 | CC-001 | SR | CC-001-101 | SRSPID | 11 | | R5 |
| 15 | CC-001 | EX | CC-001-101 | EXSPID | 5 | | R5 |
| 16 | CC-001 | SR | CC-001-101 | SRSPID | 6 | | R6 |
| 17 | CC-001 | SR | CC-001-101 | SRSPID | 12 | | R6 |
| 18 | CC-001 | EX | CC-001-101 | EXSPID | 6 | | R6 |

## Example 3

This example shows the results from a tuberculin purified protein derivative (PPD) skin test administered using the Mantoux technique. The subject was given an intradermal injection of standard PPD (i.e., PPD-S) in the left forearm at visit 1; see the Procedure Agents (AG) record below. At visit 2, the induration diameter and presence of blistering were recorded. Because the tuberculin PPD skin test cannot be interpreted using the induration diameter and blistering alone (e.g., risk for being infected with TB must also be considered), the interpretation of the skin test resides in its own row. Time point variables show that the planned time for reading the test was 48 hours after Mantoux administration. However, a comparison of datetime values in SRDTC and SRRFTDTC shows that in this case the test was read at 53 hours and 56 minutes after Mantoux administration.

**Row 1:** Shows the longest diameter in millimeters of the induration after receiving an intradermal injection of 0.1 mL containing 5TU of PPD-S in the left forearm.
**Row 2:** Shows the presence of blistering at the tuberculin PPD skin test site.
**Row 3:** Shows the interpretation of the tuberculin PPD skin test. SRGRPID is used to tie together the results to the interpretation.

**sr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SRSEQ | SRGRPID | SRTESTCD | SRTEST | SROBJ | SRORRES | SRORRESU | SRSTRESC | SRSTRESN | SRSTRESU | SRLOC | SRLAT | SRMETHOD | VISITNUM | VISIT | EPOCH | SRDTC | SRTPT | SRELTM | SRTPTREF | SRRFTDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|-------|-------|----------|----------|-------|-------|-------|-------|--------|----------|----------|
| 1 | ABC | SR | ABC-001 | 1 | 1 | DRLDOM | Induration Longest Diameter | Tuberculin PPD-S | 16 | mm | 16 | 16 | mm | FOREARM | LEFT | RULER | 2 | VISIT 2 | OPEN LABEL TREATMENT | 2011-01-19T14:26 | 48 H | PT48H | MANTOUX ADMINISTRATION | 2011-01-17T08:30:00 |
| 2 | ABC | SR | ABC-001 | 2 | 1 | BLISTIND | Blistering Indicator | Tuberculin PPD-S | Y | | Y | | | FOREARM | LEFT | | 2 | VISIT 2 | OPEN LABEL TREATMENT | 2011-01-19T14:26 | 48 H | PT48H | MANTOUX ADMINISTRATION | 2011-01-17T08:30:00 |
| 3 | ABC | SR | ABC-001 | 3 | 1 | INTP | Interpretation | Tuberculin PPD-S | POSITIVE | | POSITIVE | | | | | | 2 | VISIT 2 | OPEN LABEL TREATMENT | 2011-01-19T14:26 | 48 H | PT48H | MANTOUX ADMINISTRATION | 2011-01-17T08:30:00 |

The tuberculin PPD skin test administration was represented in the AG domain.

**ag.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AGSEQ | AGTRT | AGDOSE | AGDOSU | AGVAMT | AGVAMTU | VISITNUM | VISIT | EPOCH | AGSTDTC |
|-----|---------|--------|---------|-------|-------|--------|--------|--------|---------|----------|-------|-------|---------|
| 1 | ABC | AG | ABC-001 | 1 | tuberculin PPD-S | 5 | tuberculin unit | 0.1 | mL | 1 | VISIT 1 | OPEN LABEL TREATMENT | 2011-01-17T08:30:00 |

Relationships between SR and AG records were shown in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | SR | ABC-001 | SRGRPID | 1 | | R1 |
| 2 | ABC | AG | ABC-001 | AGSEQ | 1 | | R1 |
