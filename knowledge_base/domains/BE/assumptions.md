# BE — Assumptions

1. The BE domain contains data about actions taken that affect or may affect a specimen, such as specimen collection, freezing and thawing, aliquoting, and transportation. This domain is intended to be applicable to any specimen tracking data, regardless of the reason for specimen collection.

2. The value in BEREFID identifies the specimen most affected by the event. For aliquoting, this would be the child specimen(s) created by the event, rather than the parent specimen. BEREFID should not contain any identifiers other than specimen IDs.

3. BELOC holds the relevant anatomic location of the subject, so it should only be populated when the subject participates in and is directly affected by the event given in BETERM.

4. BEPARTY and BEPRTYID together identify the individual or organization that takes responsibility for the biospecimen as a result of the action in BETERM. For example, if BETERM is COLLECTED, BEPARTY would be a general term defining the type of responsible party, such as SITE, and BEPRTYID would contain the site identifier, such as 02. If BEPARTY is sufficient to uniquely identify the party (such as SPONSOR in a single-sponsor study), then BEPRTYID may be null.

5. Usually BEPARTY and BEPRTYID refer to who has possession of the biospecimen after the action in BETERM. In the cases where a biospecimen is lost or destroyed for example, BEPARTY and BEPRTYID may be null.

6. Timing variables:
   a. BESTDTC and BEENDTC hold the start and end date/times for the event given in BETERM. If the end date/time is the same as the start date/time for the event, then BEENDTC is null.
   b. Unlike other Events domains, BEDTC does not hold the date/time of data collection. Instead, it holds the date/time of specimen collection, in alignment with the use of --DTC for specimen-related findings. BEDTC values for extracted or otherwise derived specimens are copied from that of the parent specimen.
   c. VISITNUM, VISIT, and VISITDY values for all records refer to the visit in which the originally collected specimen was collected.

7. The following variables generally would not be used in BE: dictionary coding variables (--LLT, --LLTCD, --PTCD, --HLT, --HLTCD, --HLGT, --HLGTCD), AE-specific variables (--SEV, --SER, --ACN, --ACNOTH, --ACNDEV, --REL, --RELNST, --PATT, --OUT, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --CONTRT), toxicity variables (--TOX, --TOXGR).
