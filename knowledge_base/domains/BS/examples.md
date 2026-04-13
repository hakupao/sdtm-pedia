# BS — Examples

## Example 1

This example shows data about RNA integrity. The data collected focus on the quality of the RNA sample being collected. It has been shown that improper storage or isolation methods might compromise the usability of a sample.

**Rows 1-2:** The A260/A280 and A260/A230 ratios are used to determine the purity of the RNA sample. Any ratios outside of the accepted values may indicate contamination with protein or reagents used during the extraction process.

**Row 3:** The amounts of both 28S and 18S ribosomal RNA are measured and then a ratio is calculated. Because values in --TESTCD cannot begin with a number, the test code has been prefixed with an "I" for integrity.

**Row 4:** The RNA integrity number is a quality measurement calculated using a special algorithm and used to determine the usability of the RNA sample.

**bs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | BSSEQ | BSREFID | BSTESTCD | BSTEST | BSCAT | BSORRES | BSSTRESC | BSSTRESN | BSXFN | BSNAM | BSSPEC | BSMETHOD | BSRUNID | VISIT | VISITNUM | VISITDY | BSDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|-------|-------|--------|----------|---------|-------|----------|---------|-------|
| 1 | A12345 | BS | 43871 | 1 | 1148.26704 | A260/A230 | A260/A230 | QUALITY CONTROL | 2.05 | 2.05 | 2.05 | 2.16.090.1.135764.3.4.7280912 | Deluxe Central Labs | rRNA | SPECTROPHOTOMETRY | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |
| 2 | A12345 | BS | 43871 | 2 | 1148.26704 | A260/A280 | A260/A280 | QUALITY CONTROL | 2 | 2 | 2 | 2.16.090.1.135764.3.4.7280912 | Deluxe Central Labs | rRNA | SPECTROPHOTOMETRY | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |
| 3 | A12345 | BS | 43871 | 3 | 1148.26704 | 28S/18S | 28S/18S | QUALITY CONTROL | 1.2 | 1.2 | 1.2 | 2.16.090.1.135764.3.4.7280912 | Deluxe Central Labs | rRNA | ELECTROPHORESIS | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |
| 4 | A12345 | BS | 43871 | 4 | 1148.26704 | RIN | RNA INTEGRITY NUMBER | QUALITY CONTROL | 9.5 | 9.5 | 9.5 | 2.16.090.1.135764.3.4.7280912 | Deluxe Central Labs | rRNA | ELECTROPHORESIS | 1000450001 | Baseline | 1 | 1 | 2005-03-21T11:28:17 |
