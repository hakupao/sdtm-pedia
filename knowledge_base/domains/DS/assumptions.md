# DS — Assumptions

1. The Disposition (DS) dataset provides an accounting for all subjects who entered the study and may include protocol milestones, such as randomization, as well as the subject's completion status or reason for discontinuation for the entire study or each phase or segment of the study, including screening and post-treatment follow-up. Sponsors may choose which disposition events and milestones to submit for a study. See ICH E3, Section 10.1, for information about disposition events.

2. **Categorization**
   a. DSCAT is used to distinguish between disposition events, protocol milestones, and other events. The controlled terminology for DSCAT consists of "DISPOSITION EVENT", "PROTOCOL MILESTONE", and "OTHER EVENT".
   b. An event with DSCAT = "DISPOSITION EVENT" describes either disposition of study participation or of a study treatment. It describes whether a subject completed study participation or a study treatment and, if not, the reason they did not complete it. Dispositions may be described for each epoch (e.g., screening, initial treatment, washout, cross-over treatment, follow-up) or for the study as a whole. If disposition events for both study participation and study treatment(s) are to be represented, then DSCAT provides this distinction. For records with DSCAT = "DISPOSITION EVENT",
      i. DSSCAT = "STUDY PARTICIPATION" is used to represent disposition of study participation.
      ii. DSSCAT = "STUDY TREATMENT" is used when a study has only a single treatment.
      iii. If a study has multiple treatments, then DSSCAT should name the individual treatment.
   c. DSSCAT may be used when DSCAT = "PROTOCOL MILESTONE" or "OTHER EVENT", but would be subject to additional CDISC Controlled Terminology.
   d. An event with DSCAT = "PROTOCOL MILESTONE" is a protocol-specified, point-in-time event. Common protocol milestones include "INFORMED CONSENT OBTAINED" and "RANDOMIZED." DSSCAT may be used for subcategories of protocol milestones.
   e. An event with DSCAT = "OTHER EVENT" is another important event that occurred during a trial, but was not driven by protocol requirements and was not captured in another Events or Interventions class dataset. "TREATMENT UNBLINDED" is an example of an event that would be represented with DSCAT = "OTHER EVENT".
   f. Associations between DSCAT and some DSDECOD codelist values are described in the DS Codetable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).

3. **DS description and coding**
   a. DSDECOD values are drawn from controlled terminology. The controlled terminology depends on the value of DSCAT.
   b. When DSCAT = "DISPOSITION EVENT" DSTERM contains either "COMPLETED" or, if the subject did not complete, specific verbatim information about the reason for non-completion.
      i. When DSTERM = "COMPLETED", DSDECOD is the term "COMPLETED" from the Controlled Terminology codelist NCOMPLT.
      ii. When DSTERM contains verbatim text, DSDECOD will use the extensible Controlled Terminology Codelist NCOMPLT. For example, DSTERM = "Subject moved" might be coded to DSDECOD = "LOST TO FOLLOW-UP".
   c. When DSCAT = "PROTOCOL MILESTONE", DSTERM contains the verbatim (as collected) and/or standardized text, DSDECOD will use the extensible Controlled Terminology codelist PROTMLST.
   d. When DSCAT = "OTHER EVENT", DSTERM and DSDECOD uses sponsor terminology.
      i. If a reason for the event was collected, the reason for the event is in DSTERM and the DSDECOD is a term from sponsor terminology. For example, if treatment was unblinded due to investigator error, this might be represented in a record with DSTERM = "INVESTIGATOR ERROR" and DSDECOD = "TREATMENT UNBLINDED".
      ii. If no reason was collected, then DSTERM should be populated with the value in DSDECOD.

4. **Timing variables**
   a. DSSTDTC is expected and is used for the date/time of the disposition event. Events represented in the DS domain do not have end dates; disposition events do not span an interval, but rather occur at a single date/time (e.g., randomization date, disposition of study participation or study treatment).
   b. DSSTDTC documents the date/time that a protocol milestone, disposition event, or other event occurred. For an event with DSCAT = "DISPOSITION EVENT" where DSTERM is not "COMPLETED", the reason for non-completion may be related to an observation reported in another dataset. DSSTDTC is the date/time that the Epoch was completed and is not necessarily the same as the date/time, start date/time, or end date/time of the observation that led to discontinuation.

      For example, a subject reported severe vertigo on June 1, 2006 (AESTDTC). After ruling out other possible causes, the investigator decided to discontinue study treatment on June 6, 2006 (DSSTDTC). The subject reported that the vertigo had resolved on June 8, 2006 (AEENDTC).
   c. EPOCH may be included as a timing variable as in other general observation-class domains. In DS, EPOCH is based on DSSTDTC. The values of EPOCH are drawn from the Trial Arms (TA) dataset (see Section 7.2.1, Trial Arms).

5. Reasons for termination: ICH E3 Section 10.1 indicates that "the specific reason for discontinuation" should be presented, and that summaries should be grouped by treatment and by major reason." The CDISC SDS Team interprets this guidance as requiring 1 standardized disposition term (DSDECOD) per disposition event. If multiple reasons are reported, the sponsor should identify a primary reason and use that to populate DSTERM and DSDECOD. Additional reasons should be submitted in SUPPDS.

   For example, in a case where DSTERM = "SEVERE NAUSEA" and DSDECOD = "ADVERSE EVENT", the supplemental qualifiers dataset might include records with

   SUPPDS QNAM = "DSTERM1", SUPPDS QLABEL = "Reported Term for Disposition Event 1", and SUPPDS QVAL = "SUBJECT REFUSED FURTHER TREATMENT"

   SUPPDS QNAM = "DSDECOD1", SUPPDS QLABEL = "Standardized Disposition Term 1", and SUPPDS QVAL = "WITHDREW CONSENT"

6. Any identifier variables, timing variables, or Events general observation-class qualifiers may be added to the DS domain, but the following Qualifiers would generally not be used: --PRESP, --OCCUR, --STAT, --REASND, --BODSYS, --LOC, --SEV, --SER, --ACN, --ACNOTH, --REL, --RELNST, --PATT, --OUT, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --CONTRT, --TOXGR.
