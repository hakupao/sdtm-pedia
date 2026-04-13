# MI — Examples

## Example 1

Immunohistochemistry (IHC) is a method that involves treating tissue with a stain that adheres to very specific substances. IHC is the method most commonly used to assess the amount of HER2 receptor protein on the surface of the cancer cells. A cell with too many receptors receives too many growth signals. In this study, IHC assessment of HER2 in samples of breast cancer tissue yielded staining intensity on a scale of 0 to 3+. Staining intensity values of 0 to 1+ were categorized as negative; values of 2+ and 3+ were categorized as positive.

**Row 1:** Shows a subject with a receptor protein stain intensity value of "0", categorized in MIRESCAT as "NEGATIVE".
**Row 2:** Shows a subject with a receptor protein stain intensity value of "2+", categorized in MIRESCAT as "POSITIVE".

**mi.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MISEQ | MITESTCD | MITEST | MITSTDTL | MIORRES | MISTRESC | MIRESCAT | MISPEC | MILOC | MIMETHOD | VISIT | MIDTC |
|-----|---------|--------|---------|-------|----------|--------|----------|---------|----------|----------|--------|-------|----------|-------|-------|
| 1 | ABC | MI | ABC-1001 | 1 | HER2 | Human Epidermal Growth Factor Receptor 2 | STAINING INTENSITY | 0 | 0 | NEGATIVE | TISSUE | BREAST | IHC | SCREENING | 2001-06-15 |
| 2 | ABC | MI | ABC-2002 | 1 | HER2 | Human Epidermal Growth Factor Receptor 2 | STAINING INTENSITY | 2+ | 2+ | POSITIVE | TISSUE | BREAST | IHC | SCREENING | 2001-06-15 |

## Example 2

In this study, IHC for estrogen receptor protein expression in a tissue was reported using the Allred scoring system. The proportion positive score was assessed as the percentage of tumor cells that stained positive on a scale from 0 to 5. Staining intensity was assessed as none, weak, intermediate, or strong, and scored from 0 to 3, respectively. The total score is the sum of the proportion positive and stain intensity scores.

**Row 1:** Shows the Allred proportion positive score.
**Row 2:** Shows the staining intensity, which was assessed as "Strong". The score associated with an intensity of "STRONG" is in MISTRESC and MISTRESN.
**Row 3:** The total score is a represented in a derived record, so MIORRES is null.

**mi.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MISEQ | MIGRPID | MITESTCD | MITEST | MITSTDTL | MIORRES | MISTRESC | MISTRESN | MISPEC | MILOC | MIMETHOD | MIDRVFL | VISIT | MIDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|---------|----------|----------|--------|-------|----------|---------|-------|-------|
| 1 | ABC | MI | ABC-1001 | 1 | 1 | ESTRCPT | Estrogen Receptor | ALLRED PROPORTION POSITIVE SCORE | 3 | 3 | 3 | TISSUE | BREAST | IHC | | SCREENING | 2001-06-15 |
| 2 | ABC | MI | ABC-1001 | 2 | 1 | ESTRCPT | Estrogen Receptor | ALLRED STAINING INTENSITY SCORE | STRONG | 3 | 3 | TISSUE | BREAST | IHC | | SCREENING | 2001-06-15 |
| 3 | ABC | MI | ABC-1001 | 3 | 1 | ESTRCPT | Estrogen Receptor | ALLRED TOTAL SCORE | | 6 | 6 | TISSUE | BREAST | IHC | Y | SCREENING | 2001-06-15 |

These IHC staining results were all for the cell nucleus, represented using a supplemental qualifier for subcellular location.

**suppmi.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC | MI | ABC-1001 | MIGRPID | 1 | MISCELOC | Subcellular Location | NUCLEUS | CRF | |

## Example 3

In this study, IHC staining for NK2 homeobox 1 (NKX2-1; also known as thyroid transcription factor 1) was reported at a detailed level. Staining intensity of individual cells was assessed on a semi-quantitative scale ranging from 0 to 3+, and the percentage of tumor cells at each staining intensity level was reported. These results were used to calculate the H-score, which ranges from 0 to 300.

**Rows 1-4:** Show the percentage of cells at each H-Score staining intensity.
**Row 5:** Shows the H-score derived from the percentages. This is a derived record, so MIORRES is blank.

**mi.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MISEQ | MIGRPID | MITESTCD | MITEST | MITSTDTL | MIORRES | MIORRESU | MISTRESC | MISTRESN | MISTRESU | MISPEC | MILOC | MIMETHOD | MIDRVFL | VISIT | MIDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|---------|----------|----------|----------|----------|--------|-------|----------|---------|-------|-------|
| 1 | ABC | MI | ABC-1001 | 1 | 1 | NKX2_1 | NK2 Homeobox 1 | H SCORE STAINING INTENSITY 0 | 25 | % | 25 | 25 | % | TISSUE | LUNG | IHC | | SCREENING | 2001-06-15 |
| 2 | ABC | MI | ABC-1001 | 2 | 1 | NKX2_1 | NK2 Homeobox 1 | H SCORE STAINING INTENSITY 1+ | 40 | % | 40 | 40 | % | TISSUE | LUNG | IHC | | SCREENING | 2001-06-15 |
| 3 | ABC | MI | ABC-1001 | 3 | 1 | NKX2_1 | NK2 Homeobox 1 | H SCORE STAINING INTENSITY 2+ | 35 | % | 35 | 35 | % | TISSUE | LUNG | IHC | | SCREENING | 2001-06-15 |
| 4 | ABC | MI | ABC-1001 | 4 | 1 | NKX2_1 | NK2 Homeobox 1 | H SCORE STAINING INTENSITY 3+ | 0 | % | 0 | 0 | % | TISSUE | LUNG | IHC | | SCREENING | 2001-06-15 |
| 5 | ABC | MI | ABC-1001 | 5 | 1 | NKX2_1 | NK2 Homeobox 1 | H SCORE TOTAL SCORE | | | 110 | 110 | | TISSUE | LUNG | IHC | Y | SCREENING | 2001-06-15 |

These IHC staining results were all for the cell cytoplasm, represented using a supplemental qualifier for subcellular location.

**suppmi.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC | MI | ABC-1001 | MIGRPID | 1 | MISCELOC | Subcellular Location | CYTOPLASM | CRF | |
