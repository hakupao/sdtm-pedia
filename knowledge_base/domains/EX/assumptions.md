# EX — Assumptions

1. EX structure and use
   a. Examples of treatments represented in the EX domain include but are not limited to placebo, active comparators, and investigational products. Treatments that are not protocol-specified should be represented in the Concomitant/Prior Medications (CM) or another Interventions domain as appropriate.
   b. The EX domain is recognized in most cases as a derived dataset where EXDOSU reflects the protocol-specified unit per study treatment. Collected data points (e.g., number of tablets, total volume infused) along with additional inputs (e.g., randomization file, concentration, dosage strength, product accountability) are used to derive records in the EX domain.
   c. The EX domain is required for all studies that include protocol-specified study treatment. Exposure records may be directly or indirectly determined; metadata should describe how the records were derived. Common methods for determining exposure (from most direct to least direct) include the following:
      i. Derived from actual observation of the administration of drug by the investigator
      ii. Derived from automated dispensing device that records administrations
      iii. Derived from subject recall
      iv. Derived from product accountability data
      v. Derived from the protocol. When a study is still masked and protocol-specified study treatment doses cannot yet be reflected in the protocol-specified unit due to blinding requirements, then the EX domain is not expected to be populated.
   d. The EX domain should contain 1 record per constant-dosing interval per subject. Sponsors define the constant-dosing interval, which may include any period of time that can be described in terms of a known treatment given at a consistent dose, frequency, infusion rate, and so on. For example, for a study with once-a-week administration of a standard dose for 6 weeks, exposure may be represented as:
      i. a single record per subject, spanning the entire 6-week treatment phase, if information about each dose is not collected; or
      ii. up to 6 records (1 for each weekly administration), if the sponsor monitors each treatment administration.

2. Exposure treatment description
   a. EXTRT captures the name of the protocol-specified study treatment and is the topic variable. It is a required variable and must have a value. EXTRT must include only the treatment name and must not include dosage, formulation, or other qualifying information. For example, "ASPIRIN 100MG TABLET" is not a valid value for EXTRT. This example should be expressed as EXTRT = "ASPIRIN", EXDOSE = "100", EXDOSU = "mg", and EXDOSFRM = "TABLET".
   b. Doses of placebo should be represented by EXTRT = "PLACEBO" and EXDOSE = "0" (indicating 0 mg of active ingredient was taken or administered).

3. Categorization and grouping
   a. EXCAT and EXSCAT may be used when appropriate to categorize treatments into categories and subcategories. For example, if a study contains several active comparator medications, EXCAT may be set to "ACTIVE COMPARATOR". Such categorization may not be useful in all studies, so these variables are permissible.
![alt text](image.png)
4. Timing variables
   a. The timing of exposure to study treatment is captured by the start/end date and start/end time of each constant-dosing interval. If the subject is only exposed to study medication within a clinical encounter (e.g., if an injection is administered at the clinic), VISITNUM may be added to the domain as an additional timing variable. VISITDY and VISIT would then also be permissible qualifiers. However, if the beginning and end of a constant-dosing interval is not confined within the time limits of a clinical encounter (e.g., if a subject takes pills at home), then it is not appropriate to include VISITNUM in the EX domain. This is because EX is designed to capture the timing of exposure to treatment, not the timing of dispensing treatment. Further, VISITNUM should not be used to indicate that treatment began at a particular visit and continued for a period of time. The SDTM does not have any provision for recording "start visit" and "end visit" of exposure.
   b. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, EXSTDTC should be copied to EXENDTC as the standard representation.

5. Collected exposure data points are to be represented in the Exposure as Collected (EC) domain. When the relationship between EC and EX records can be described in RELREC, then it should be defined. EX derivations must be described in the Define-XML document.

6. Additional interventions qualifiers
   a. EX contains medications received; the inclusion of administrations not taken, not given, or missed is under evaluation. Because EX includes only treatments received, --MOOD would generally not be used in EX.
   b. --DOSTOT is under evaluation for potential deprecation and replacement with a mechanism to describe total dose over any interval of time (e.g., day, week, month). Sponsors considering use of EXDOSTOT may want to consider using other dose-amount variables (EXDOSE or EXDOSTXT) in combination with frequency (EXDOSFRQ) and timing variables to represent the data.
   c. When the EC domain is implemented in conjunction with the EX domain, EXVAMT and EXVAMTU would not be used in EX; collected values instead would be represented in ECDOSE and ECDOSU (and ECVAMT and ECVAMTU as needed).
   d. Any identifier variables, timing variables, or findings general observation-class qualifiers may be added to the EX domain, but the following qualifiers would generally not be used: --PRESP, --OCCUR, --STAT, and --REASND.
