# IS — Assumptions

1. The Immunogenicity Specimen Assessments (IS) domain holds assessments that describe whether a therapy (e.g., biologic, drug, vaccine) provoked/caused/induced an immune response in a subject. The response can be either positive or negative. For example, a vaccine is expected to induce a beneficial immune response, whereas a cellular therapy (e.g., erythropoiesis-stimulating agents) may cause an adverse immune response.

2. The IS domain also holds assessments that describe whether an allergen, microorganism, or endogenous molecule provoked/caused/induced an immune response in a subject, such as a subject's antibody reaction (autoantibodies) against auto/self-antigens for autoimmune studies or antibody production in response to allergens in allergy tests. Expected outputs can be positive or negative, present or absent for the antibody of interest, as well as quantification of the antibody. Assessments pertaining to antibodies produced in response to microbial infection will also be represented in the IS domain.

3. Assessments about all other types of "induced" humoral (antibody) immune response in a subject (e.g., antibodies against human leukocyte antigen (HLA) proteins) will also be represented in the IS domain.

4. Certain types of cellular immune responses will also be modeled in IS using non-flow cytometry techniques (see example 6). Flow cytometry data should be modeled in the Cell Phenotype Findings (CP) domain, section 6.3.5.3.

5. An exception is made to the class of antigen/antibody (Ag/Ab) combination assays. Microbial antigen/antibody (Ag/Ab) combination tests should be represented in the Microbiology Specimen (MB) domain. An example is fourth-generation HIV Ag/Ab combination tests, which are commonly seen as HIV identification or detection assays rather than tests that provide additional details on and characterization of a subject's immunological responses. The outputs of these assays can be expected as reactive, non-reactive, or indeterminate. Whereas some tests generate separate outputs for antigen and antibody, others just indicate "reactive" when either or both are detected. Output is generally based on relative light units, where a result of "reactive" typically requires the signal to cutoff ratio to be greater than 1.

6. Measurements of cytokines, chemokines, and complement proteins should be represented in the Laboratory Test Results (LB) domain.

7. The IS domain variable ISBDAGNT (Binding Agent) is currently supported by 2 Controlled Terminology codelists: Microorganism (MICROORG) and Binding Agent for Immunogenicity Tests (ISBDAGT). Controlled Terminology Rules for Immunogenicity Tests describes how and when to use each codelist (see https://www.cdisc.org/standards/terminology/controlled-terminology).
   a. For antidrug antibody (ADA) tests, the ISBDAGNT variable is used to represent the free-text description of the name/identity of the therapy the antidrug antibody targets. CDISC does not control study therapy names (e.g., drugs, biologics). For ADA tests as a part of regulatory agency submissions, the proprietary binding study therapy name(s) should be considered as extended values of the ISBDAGT codelist when represented in Define-XML.
   b. For mixed-allergens panel tests, submission values represented in the ISBDAGNT variable should follow this format: "XXX, Multiple" (e.g., Dairy Mix Antigens, Multiple; Animal Mix Antigens, Multiple; use the plural form for the word "antigen" if needed). Should the sponsor wish to specify the individual antigens in a mixed antigen panel (e.g., ISBDAGNT = "Animal Mix Antigens, Multiple"), put the names of the specific antigens in Suppqual (e.g., Cat, Dog, Cow, Horse; see example 11).

8. The IS domain variable ISTSTOPO (Test Operational Objective) is supported by a nonextensible Controlled Terminology codelist containing the values SCREEN, CONFIRM, and QUANTIFY.

9. For vaccine studies, in order to distinguish collected data between study vaccine-induced immunogenicity and immunogenicity findings unrelated to the study vaccine (i.e., immunity as a result of natural infection or previous vaccination), the following ISCAT and ISSCAT values are recommended (see example 5):
   a. For immunological data pertaining to the study vaccine, ISCAT = STUDY VACCINE-RELATED IMMUNOGENICITY.
   b. For immunological data collected during the vaccine trial but which are not assessments about the study vaccine, ISCAT = NON-STUDY-RELATED IMMUNOGENICITY.
   c. For assessments measuring the induced-antibody response, ISSCAT = HUMORAL IMMUNITY.
   d. For assessments measuring the induced-cellular response, ISSCAT = CELLULAR IMMUNITY.

10. Any Identifier variables, Timing variables, or Findings general observation class qualifiers may be added to the IS domain.
