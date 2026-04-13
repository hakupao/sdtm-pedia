# AG — Assumptions

1. Purpose of the domain: Some tests involve administration of substances, and it has been unclear in which domain these should be represented.
   a. The Concomitant/Prior Medications (CM) domain seemed particularly inappropriate when the substance was one that would never be given as a medication. Even substances that are medications are not being used as such when they are given as part of a testing procedure.
   b. The Exposure (EX) domain also seemed inappropriate; although the testing procedure might be part of the study plan, these data would not be used or analyzed in the same way as data about study treatments. The AG domain was created to fill this gap.
   c. The AG domain has advantages over the Procedures (PR) domain for this purpose. It allows recording of multiple substance administrations for a single testing procedure. It also separates data about substance administrations from data about procedures that do not involve substance administration.
   d. Information about the conduct of the procedure with which the procedure agent administration was associated, if collected, should be represented in the PR domain.

2. Examples and structure
   a. Examples of agents administered as part of a procedure include a short-acting bronchodilator administered as part of a reversibility assessment and contrast agents or radio-labeled substances used in imaging studies.
   b. The structure of the AG domain is 1 record per agent intervention episode, or prespecified agent assessment per subject. It is the sponsor's responsibility to define an intervention episode. This definition may vary based on the sponsor's requirements for review and analysis.

3. AG description and coding
   a. AGTRT captures the name of the agent and it is the topic variable. It is a required variable and must have a value. AGTRT should include only the agent name, and should not include dosage, formulation, or other qualifying information. For example, "ALBUTEROL 2 PUFF" is not a valid value for AGTRT. This example should be expressed as AGTRT = "ALBUTEROL", AGDOSE = "2", AGDOSU = "PUFF", and AGDOSFRM = "AEROSOL".
   b. AGMODIFY should be included if the sponsor's procedure permits modification of a verbatim term for coding.
   c. AGDECOD is the standardized agent term derived by the sponsor from the coding dictionary. It is possible that the reported term (AGTRT) or the modified term (AGMODIFY) can be coded using a standard dictionary. In such cases, sponsors are expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

4. Prespecified terms; presence or absence of procedure agents
   a. AGPRESP is used to indicate whether an agent was prespecified.
   b. AGOCCUR is used to indicate whether a prespecified agent was used. A value of "Y" indicates that the agent was used and "N" indicates that it was not.
   c. If an agent was not prespecified, the value of AGOCCUR should be null. AGPRESP and AGOCCUR are permissible fields and may be omitted from the dataset if all agents were collected as free text. Values of AGOCCUR may also be null for prespecified agents if no Y/N response was collected; in this case, AGSTAT = "NOT DONE", and AGREASND could be used to describe the reason the answer was missing.

5. Any identifier variables, timing variables, or interventions general observation-class qualifiers may be added to the AG domain.
   a. However, --INDC, although allowed, would not generally be used because substance administrations represented in AG are given as part of a testing procedure rather than with therapeutic intent.
   b. The variables --DOSTOT and --DOSRGM, although allowed, would generally not be used because procedure agents are likely to be recorded at the level of single administrations.
