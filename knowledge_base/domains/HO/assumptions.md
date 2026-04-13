# HO — Assumptions

1. The Healthcare Encounters (HO) dataset includes inpatient and outpatient healthcare events (e.g., hospitalizations, nursing home stays, rehabilitation facility stays, ambulatory surgery).

2. Values of HOTERM typically describe the location or place of the healthcare encounter (e.g., "HOSPITAL" rather than "HOSPITALIZATION"). HOSTDTC should represent the start or admission date and HOENDTC the end or discharge date.

3. Data collected about healthcare encounters may include the reason for the encounter. The following supplemental qualifiers may be appropriate for representing such data:
   a. The supplemental qualifier with QNAM = "HOINDC" would be used to represent the indication/medical condition for the encounter (e.g., stroke). Note that --INDC is an Interventions class variable, so is not a standard variable for HO, which is an Events class domain.
   b. The supplemental qualifier with QNAM = "HOREAS" would be used to represent a reason for the encounter other than a medical condition (e.g., annual checkup).

4. If collected data includes the name of the provider or the facility where the encounter took place, this may be represented using the supplemental qualifier with QNAM = "HONAM". Note that --NAM is a Findings class variable, so is not a standard variable for HO, which is an Events class domain.

5. Any identifier variables, timing variables, or Events general observation-class qualifiers may be added to the HO domain, but the following Qualifiers would generally not be used: --SER, --ACN, --ACNOTH, --REL, --RELNST, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --BODSYS, --LOC, --SEV, --TOX, --TOXGR, --PATT, --CONTRT.
