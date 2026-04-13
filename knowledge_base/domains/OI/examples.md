# OI — Examples

## Example 1

This example shows taxonomic identifiers for human immunodeficiency virus (HIV) and hepatitis C virus (HCV). NHOID is a unique non-host organism ID used to link findings on that organism in other datasets with details about its identification in OI. OIPARM shows the name of the individual taxa identified and OIVAL shows the experimentally determined values of those taxa.

**Rows 1-4:** Show the taxonomy for the HIV organism given the NHOID of HIV1MC. This virus has been identified as HIV-1, Group M, Subtype C.

**Rows 5-8:** Show the taxonomy for the HIV organism given the NHOID of HIV1MB, which was used as a reference. This virus has been identified as HIV-1, Group M, Subtype B.

**Rows 9-11:** Show the taxonomy for the HCV organism given the NHOID of HCV2C. This virus has been identified as HCV 2c.

**Rows 12-14:** Show the taxonomy for the HCV organism given the NHOID of H77. This virus is a known reference strain of HCV 1a.

**oi.xpt**

| Row | STUDYID | DOMAIN | NHOID | OISEQ | OIPARMCD | OIPARM | OIVAL |
|-----|---------|--------|-------|-------|----------|--------|-------|
| 1 | STUDY123 | OI | HIV1MC | 1 | SPCIES | Species | HIV |
| 2 | STUDY123 | OI | HIV1MC | 2 | TYPE | Type | 1 |
| 3 | STUDY123 | OI | HIV1MC | 3 | GROUP | Group | M |
| 4 | STUDY123 | OI | HIV1MC | 4 | SUBTYP | Subtype | C |
| 5 | STUDY123 | OI | HIV1MB | 1 | SPCIES | Species | HIV |
| 6 | STUDY123 | OI | HIV1MB | 2 | TYPE | Type | 1 |
| 7 | STUDY123 | OI | HIV1MB | 3 | GROUP | Group | M |
| 8 | STUDY123 | OI | HIV1MB | 4 | SUBTYP | Subtype | B |
| 9 | STUDY123 | OI | HCV2C | 1 | SPCIES | Species | HCV |
| 10 | STUDY123 | OI | HCV2C | 2 | GENTYP | Genotype | 2 |
| 11 | STUDY123 | OI | HCV2C | 3 | SUBTYP | Subtype | C |
| 12 | STUDY123 | OI | H77 | 1 | SPCIES | Species | HCV |
| 13 | STUDY123 | OI | H77 | 2 | GENTYP | Genotype | 1 |
| 14 | STUDY123 | OI | H77 | 3 | SUBTYP | Subtype | A |
