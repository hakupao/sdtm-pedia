# DD — Assumptions

## DD – Description/Overview

A findings domain that contains the diagnosis of the cause of death for a subject.

The domain is designed to hold supplemental data that are typically collected when a death occurs, such as the official cause of death. It does **not** replace existing data such as serious adverse event details in AE. Further, it does **not** introduce a new requirement to collect information that is not already indicated as good clinical practice or defined in regulatory guidelines. Instead, it provides a consistent place within the SDTM to hold information that previously did not have a clearly defined home.

## DD – Specification

dd.xpt, Death Details — Findings. One record per finding per subject, Tabulation.

## DD – Assumptions

1. There may be more than 1 cause of death. If so, these may be separated into primary and secondary causes and/or other appropriate designations. DD may also include other details about the death, such as where the death occurred and whether it was witnessed.

2. Death details are typically collected on designated CRF pages. The DD domain is not intended to collate data that are collected in standard variables in other domains, such as AE.AEOUT (Outcome of Adverse Event), AE.AESDTH (Results in Death) or DS.DSTERM (Reported Term for the Disposition Event). Data from other domains that relates to the death can be linked to DD using RELREC.

3. This domain is not intended to include data obtained from autopsy. An autopsy is a procedure from which there will usually be findings. Autopsy information should be handled as per recommendations in the Procedures (PR) domain.

4. There are separate codelists for DD tests and responses. Associations between the DD tests and response codelists are described in the DD codetable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).

5. Any identifiers, timing variables, or findings general observation-class qualifiers may be added to the DD domain, but the following qualifiers would not generally be used: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --NAM, --LOINC, --SPEC, --SPCCND, --LOBXFL, --BLFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV.
