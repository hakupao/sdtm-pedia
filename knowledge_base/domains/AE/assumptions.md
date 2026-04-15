# AE — Assumptions

1. The Adverse Events dataset includes clinical data describing "any untoward medical occurrence in a patient or clinical investigation subject administered a pharmaceutical product and which does not necessarily have to have a causal relationship with this treatment" (ICH E2A). In consultation with regulatory authorities, sponsors may extend or limit the scope of adverse event collection (e.g., collecting pre-treatment events related to trial conduct, not collecting events that are assessed as efficacy endpoints). The events included in the AE dataset should be consistent with the protocol requirements. Adverse events may be captured either as free text or via a prespecified list of terms.

2. **AE description and coding**
   a. AETERM captures the verbatim term collected for the event. It is the topic variable for the AE dataset. AETERM is a required variable and must have a value.
   b. AEMODIFY is a permissible variable and should be included if the sponsor's procedure permits modification of a verbatim term for coding. The variable should be populated as per the sponsor's procedures.
   c. AEDECOD is the preferred term derived by the sponsor from the coding dictionary. It is a required variable and must have a value. It is expected that the reported term (AETERM) will be coded using a standard dictionary such as MedDRA. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.
   d. AEBODSYS is the system organ class (SOC) from the coding dictionary associated with the adverse event by the sponsor. This value may differ from the primary SOC designated in the coding dictionary's standard hierarchy. It is expected that this variable will be populated.

3. **Additional categorization and grouping**
   a. AECAT and AESCAT should not be redundant with the domain code or dictionary classification provided by AEDECOD and AEBODSYS (i.e., they should provide a different means of defining or classifying AE records). AECAT and AESCAT are intended for categorizations that are defined in advance. For example, a sponsor may have a CRF page for AEs of special interest and another page for all other AEs. AECAT and AESCAT should not be used for after-the-fact categorizations such as "clinically significant." In cases where a category of AEs of special interest resembles a part of the dictionary hierarchy (e.g., "CARDIAC EVENTS"), the categorization represented by AECAT and AESCAT may differ from the categorization derived from the coding dictionary.
   b. AEGRPID may be used to link (or associate) different records together to form a block of related records at the subject level within the AE domain, see Section 4.2.6, Grouping Variables and Categorization.

4. **Prespecified terms; presence or absence of events**
   a. Adverse events are generally collected in 2 different ways, either by recording free text or using a prespecified list of terms. In the latter case, the solicitation of information on specific adverse events may affect the frequency at which they are reported; therefore, the fact that a specific adverse event was solicited may be of interest to reviewers. An AEPRESP value of "Y" is used to indicate that the event in AETERM was prespecified on the CRF.
   b. If it is important to know which adverse events from a prespecified list were not reported as well as those that did occur, these data should be submitted in a Findings class dataset such as Findings About Events and Interventions (see Section 6.4, Findings About Events or Interventions). A record should be included in that Findings dataset for each prespecified adverse-event term. Records for adverse events that actually occurred should also exist in the AE dataset with AEPRESP set to "Y."
   c. If a study collects both prespecified adverse events and free-text events, the value of AEPRESP should be "Y" for all prespecified events and null for events reported as free text. AEPRESP is a permissible field and may be omitted from the dataset if all adverse events were collected as free text.
   d. When adverse events are collected with the recording of free text, a record may be entered into the sponsor's data management system to indicate "no adverse events" for a specific subject. For these subjects, do not include a record in the AE submission dataset to indicate that there were no events. Records should be included in the submission AE dataset only for adverse events that have actually occurred.

5. **Timing variables**
   a. Relative timing assessment "Ongoing" is common in the collection of AE information. AEENRF may be used when this relative timing assessment is made coincident with the end of the study reference period for the subject represented in the Demographics (DM) dataset (RFENDTC). AEENRTPT with AEENTPT may be used when "Ongoing" is relative to another date (e.g., the final safety follow-up visit date). See Section 4.4.7, Use of Relative Timing Variables.
   b. Additional timing variables (e.g., AEDTC) may be used when appropriate.

6. **Actions taken**
   a. AECONTRT is a Y/N variable. If the non-study treatment is collected, the name and other information about the treatment should be represented in the appropriate Interventions domain—usually Concomitant/Prior Medications (CM) or Procedures (PR)—and linked to the AE record with RELREC.
   b. Actions other than concomitant treatments are recorded in:
      - AEACN, only for actions taken with study treatment
      - AEACNDEV, for actions with a device
      - AEACNOTH, for actions that do not involve treatment or a device

7. **Other qualifier variables**
   a. If categories of serious events are collected secondarily to a leading question the values of the variables that capture reasons an event is considered serious (e.g., AESCAN, AESCONG) may be null. For example, if "Serious?" is answered "No", the values for these variables may be null. However, if "Serious?" is answered "Yes", at least one of them will have a "Y" response. Others may be "N" or null, according to the sponsor's convention.

      **CRF: AE Seriousness Classification**

      | Serious? | [ ] Yes  [ ] No |
      |----------|-----------------|
      | If yes, check all that apply: | [ ] Fatal  [ ] Life-threatening  [ ] Inpatient hospitalization or prolongation of existing hospitalization  [ ] Persistent or significant disability/incapacity  [ ] Congenital anomaly/birth defect  [ ] Other medically important serious event |

      On the other hand, if the CRF is structured so that a response is collected for each seriousness category, all category variables (e.g., AESDTH, AESHOSP) would be populated and AESER would be derived.
   b. The serious categories "Involves cancer" (AESCAN) and "Occurred with overdose" (AESOD) are not part of the ICH definition of a serious adverse event, but these categories are available for use in studies conducted under guidelines that existed prior to the FDA's adoption of the ICH definition.
   c. When a description of "Other Medically Important Serious Adverse Events" category is collected on a CRF, sponsors should place the description in the SUPPAE dataset using the standard supplemental qualifier name code AEOSOSP as described in Section 8.4, Relating Non-Standard Variables Values to a Parent Domain, and in Appendix C1, Supplemental Qualifiers Name Codes.
   d. In studies using toxicity grade according to a standard toxicity scale such as the Common Terminology Criteria for Adverse Events v3.0 (CTCAE), published by the National Cancer Institute (NCI; available at https://ctep.cancer.gov/protocoldevelopment/), AETOXGR should be used instead of AESEV. In most cases, either AESEV or AETOXGR is populated but not both. There may be cases when a sponsor may need to populate both variables. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.
   e. The structure of the AE domain is 1 record per adverse event per subject. It is the sponsor's responsibility to define an event. This definition may vary based on the sponsor's requirements for characterizing and reporting product safety and is usually described in the protocol. For example, the sponsor may submit 1 record that covers an adverse event from start to finish. Alternatively, if there is a need to evaluate AEs at a more granular level, a sponsor may submit a new record when severity, causality, or seriousness changes or worsens. By submitting these individual records, the sponsor indicates that each is considered to represent a different event. The submission dataset structure may differ from the structure at the time of collection. For example, a sponsor might collect data at each visit in order to meet operational needs, but submit records that summarize the event and contain the highest level of severity, causality, seriousness, and so on. Examples of dataset structure include:
      i. One record per adverse event per subject for each unique event. Multiple adverse event records reported by the investigator are submitted as summary records "collapsed" to the highest level of severity, causality, seriousness, and the final outcome.
      ii. One record per adverse event per subject. Changes over time in severity, causality, or seriousness are submitted as separate events. Alternatively, these changes may be submitted in a separate dataset based on the Findings About Events and Interventions model (see Section 6.4, Findings About Events or Interventions).
      iii. Other approaches may also be reasonable as long as they meet the sponsor's safety evaluation requirements and each submitted record represents a unique event. The domain-level metadata (see Section 3.2, Using the CDISC Domain Models in Regulatory Submissions – Dataset Metadata) should clarify the structure of the dataset.

8. Use of EPOCH and TAETORD: When EPOCH is included in the AE domain, it should be the epoch of the start of the adverse event. In other words, it should be based on AESTDTC, rather than AEENDTC. The computational method for EPOCH in the Define-XML document should describe any assumptions made to handle cases where an adverse event starts on the same day that a subject starts an epoch, if AESTDTC and SESTDTC are not captured with enough precision to determine the epoch of the onset of the adverse event unambiguously. Similarly, if TAETORD is included in the AE domain, it should be the value for the start of the adverse event, and the computational method in the Define-XML document should describe any assumptions.

9. Any additional identifier variables may be added to the AE domain.

10. The following qualifiers would not be used in AE: --OCCUR, --STAT, and--REASND. They are the only qualifiers from the SDTM Events class not in the AE domain. They are not permitted because the AE domain contains only records for adverse events that actually occurred. See Assumption 4b for information on how to deal with negative responses or missing responses to probing questions for prespecified adverse events.

11. Variable order in the domain should follow the rules as described in Section 4.1.4, Order of the Variables, and the order described in Section 1.1, Purpose.

12. The addition of AELLT, AELLTCD, AEPTCD, AEHLT, AEHLTCD, AEHLGT, AEHLGTCD, AEBDSYCD, AESOC, and AESOCD is applicable to submissions coded in MedDRA only. Data items are not expected for non-MedDRA coding.
