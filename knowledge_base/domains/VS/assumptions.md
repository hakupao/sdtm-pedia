# VS — Assumptions

1. In cases where the LOINC dictionary is used for vital sign tests, the permissible variable VSLOINC may be used. Sponsors are expected to provide the dictionary name and version used to map terms using the external codelist element in the Define-XML document.

2. If a reference range is available for a vital signs test, the variables VSORNRLO, VSORNRHI, VSNRIND from the Findings observation class may be added to the domain. VSORNRLO and VSORNRHI would represent the reference range, and VSNRIND would be used to indicate where a result falls with respect to the reference range (e.g., "HIGH", "LOW"). If toxicity grading is available, values would be represented in the variables VSTOX and VSTOXGR. Clinical significance would be represented in VSCLSIG, as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data.

3. Associations between some vital sign tests and qualifier codelists are described in the VS codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

4. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the VS domain, but the following qualifiers would not generally be used: --BODSYS, --XFN, --SPEC, --SPCCND, --FAST.
