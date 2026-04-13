# DD — Assumptions

1. There may be more than 1 cause of death. If so, these may be separated into primary and secondary causes and/or other appropriate designations. DD may also include other details about the death, such as where the death occurred and whether it was witnessed.

2. Death details are typically collected on designated CRF pages. The DD domain is not intended to collate data that are collected in standard variables in other domains, such as AE.AEOUT (Outcome of Adverse Event), AE.AESDTH (Results in Death) or DS.DSTERM (Reported Term for the Disposition Event). Data from other domains that relates to the death can be linked to DD using RELREC.

3. This domain is not intended to include data obtained from autopsy. An autopsy is a procedure from which there will usually be findings. Autopsy information should be handled as per recommendations in the Procedures (PR) domain.

4. There are separate codelists for DD tests and responses. Associations between the DD tests and response codelists are described in the DD codeable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).

5. Any identifiers, timing variables, or findings general observation-class qualifiers may be added to the DD domain, but the following qualifiers would not generally be used: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --NAM, --LOINC, --SPEC, --SPCCND, --LOBXFL, --BLFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV.
