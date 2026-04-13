# MI — Assumptions

1. This domain holds findings resulting from the microscopic examination of tissue samples. These examinations are performed on a specimen, usually one that has been prepared with some type of stain. Some examinations of cells in fluid specimens (e.g., blood, urine) are classified as lab tests and should be stored in the Laboratory Test Results (LB) domain. Biomarkers assessed by histologic or histopathological examination (by employing cytochemical/immunocytochemical stains) are stored in the MI domain.

2. When biomarker results are represented in MI, MITESTCD reflects the biomarker of interest (e.g., "BRCA1", "HER2", "TTF1"), and MITSTDTL further qualifies the record. MITSTDTL is used to represent details descriptive of staining results (e.g., "H SCORE TOTAL SCORE", "STAINING INTENSITY", "PERCENT POSITIVE CELL").

3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MI domain, but the following qualifiers would generally not be used: --POS, --MODIFY, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --LEAD, --CSTATE, --BLFL, --FAST, --DRVFL, --LLOQ, --ULOQ.
