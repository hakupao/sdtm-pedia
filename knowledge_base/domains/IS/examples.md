# IS — Examples

## Example 1

This example shows data from tiered testing of antidrug antibody (ADA).

Tiered testing scheme for ADA evaluation generally includes the following steps: screening, confirmatory, and "characterization" of the antidrug antibody. In tier 1, all evaluable samples are run in a screening assay. Samples that are positive for ADA in the screen assay are then analyzed in a confirmatory assay (tier 2). The samples that are positive for ADA in both the screen and confirmatory tiers of testing are further tested in tier 3; this frequently includes analysis of antibody titer and neutralizing activity. In order to illustrate the distinctive differences between the 3 tiers of ADA testing, the standard variable ISTSTOPO is used to represent the controlled values SCREEN, CONFIRM, and QUANTIFY. These values help to describe the operational objective or the reason behind each testing step/tier, and also to provide uniqueness to each row of record. The study drug AZ-007, which induces the subject's production of, and is the target of the antidrug antibody, is represented by the variable ISBDAGNT. ISGRPID is used in this example to show that the records are related to each other; in this particular case, tests are done in a tiered, sequential manner from screen to confirm to quantification of the detected antidrug antibody.

Lastly, antibody titer is often defined as the reciprocal of the lowest dilution of a sample generating a signal that is above the assay cut-point. Alternatively, the titer is defined as the reciprocal of the dilution of a sample generating a signal that is equivalent to the assay cut-point, calculated by an interpolation formula provided in an assay specific bioanalytical method.

**Row 1:** Shows the screening of the presence of ADA to drug AZ-007.
**Row 2:** Shows the confirmation of the previously detected ADA to drug AZ-007.
**Row 3:** Shows the measurement of titer of the ADA from the screen and confirmatory steps.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | ABC | IS | ABC-002 | 1 | V555 | 1 | ADA_BAB | Binding Antidrug Antibody | DRUG AZ-007 | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-002 | 2 | V555 | 1 | ADA_BAB | Binding Antidrug Antibody | DRUG AZ-007 | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-002 | 3 | V555 | 1 | ADA_BAB | Binding Antidrug Antibody | DRUG AZ-007 | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 50 | titer | 50 | 50 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |

## Example 2

This example shows data from various subtypes of ADA tests.

Although most ADAs do not inhibit the pharmacodynamic activity of a drug, neutralizing antidrug antibodies (NAbs) can inhibit drug activity soon after a drug is administered. Most ADAs (those that are not classified as NAbs) can lower the drug's systemic exposure by increasing the rate of drug clearance, resulting in a clinically similar outcome to that of NAbs (i.e., reduced clinical efficacy).

In this example, the administered drug is an analogue of an endogenous protein. The example data include ADA reactions against both the administered drug and the endogenous protein. Both the study drug and the endogenous protein are represented by the standard variable ISBDAGNT, which qualifies ISTEST. The variable ISTSTOPO, is also used in this dataset to describe the purpose of each testing step, and provides uniqueness among similar records. ISGRPID is used to show which records are related in this dataset.

Note that, in this example, even though only confirmatory records are reported and shown, it is assumed that the screening step has also been performed.

**Rows 1-2:** Show the confirmation and quantification of binding ADA to coagulation factor VIII analogue drug. A binding antidrug antibody is an antibody that binds to a drug.
**Rows 3-4:** Show the confirmation and quantification of the neutralizing binding ADA to coagulation factor VIII analogue drug. A neutralizing binding antidrug antibody is a type of ADA that binds to the functional portion of a drug, leading to diminished or negated pharmacological activity. The neutralizing ADAs are a subset of the total ADAs.
**Rows 5-6:** Show the confirmation and quantification of the cross-reactive binding ADA to the endogenous coagulation factor VIII. A cross-reactive binding antidrug antibody is a type of ADA that binds to endogenous molecules, also a subset of the total ADAs.
**Rows 7-8:** Show the confirmation and quantification of the neutralizing cross-reactive binding ADA to the endogenous coagulation factor VIII. Neutralizing cross-reactive binding antidrug antibodies are a type of ADA that bind to endogenous molecules, leading to diminished or negated function; in some cases, they may also bind and negate the function of the study drug. They are a subset of the total ADAs.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | ABC | IS | ABC-001 | 1 | A42839 | 1 | ADA_BAB | Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-001 | 2 | A42839 | 1 | ADA_BAB | Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 30 | titer | 30 | 30 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-001 | 3 | A42839 | 2 | ADA_NAB | Neutralizing Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |
| 4 | ABC | IS | ABC-001 | 4 | A42839 | 2 | ADA_NAB | Neutralizing Binding Antidrug Antibody | COAGULATION FACTOR VIII ANALOGUE DRUG | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 60 | titer | 60 | 60 | titer | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |
| 5 | ABC | IS | ABC-001 | 5 | A42839 | 3 | ADA_X | Cross-Reactive Binding Antidrug Antibody | ENDOGENOUS COAGULATION FACTOR VIII | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 6 | ABC | IS | ABC-001 | 6 | A42839 | 3 | ADA_X | Cross-Reactive Binding Antidrug Antibody | ENDOGENOUS COAGULATION FACTOR VIII | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 90 | titer | 90 | 90 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 7 | ABC | IS | ABC-001 | 7 | A42839 | 3 | ADA_NX | Neutralize Cross-React Bind Antidrug Ab | ENDOGENOUS COAGULATION FACTOR VIII | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |
| 8 | ABC | IS | ABC-001 | 8 | A42839 | 4 | ADA_NX | Neutralize Cross-React Bind Antidrug Ab | ENDOGENOUS COAGULATION FACTOR VIII | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 150 | titer | 150 | 150 | titer | SERUM | HEMAGGLUTINATION INHIBITION ASSAY | 1 | VISIT 1 | 2017-07-27 |

## Example 3

This example shows data about ADA reaction against drug components.

This example shows the production of ADA in response to both the prodrug and its active metabolite. A prodrug is a compound that, after administration, is metabolized into a pharmacologically active drug. Note that, in this example, even though only confirmatory records are reported and shown, it is assumed that the screening step has also been performed.

**Rows 1-2:** Show the confirmation and quantification of the ADA against prodrug A.
**Rows 3-4:** Show the confirmation and quantification of the ADA against the active metabolite of prodrug A.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | ABC | IS | ABC-004 | 1 | J123 | 1 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-004 | 2 | J123 | 1 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 30 | titer | 30 | 30 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-004 | 3 | J123 | 2 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A ACTIVE METABOLITE | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 4 | ABC | IS | ABC-004 | 4 | J123 | 2 | ADA_BAB | Binding Antidrug Antibody | PRODRUG A ACTIVE METABOLITE | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 60 | titer | 60 | 60 | titer | SERUM | ELECTROCHEMILUMINESCENCE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |

## Example 4

This example shows data about ADA reaction against multiple epitopes of a drug molecule.

This example shows the production of ADA in response to the study biologic drug, peginterferon beta-1a; its active metabolite, active interferon beta 1a; and its immunogenic epitope, PEG epitope of peginterferon beta-1a. An immunogenic epitope of a biologic drug is a particular segment within the drug that is recognized by the immune system, specifically by antibodies, B cells, or T cells. This immunogenic epitope portion of the biologic drug is capable of inducing the production of and therefore the binding of ADAs.

This example also shows when tiered testing stops at the screening step (interferon beta1a assay) and goes straight to neutralizing antidrug antibody testing. Although this is unusual, it illustrates the flexibility of the fields ISTEST, ISBDAGNT, and ISTSTOPO to incorporate multiple options.

**Row 1:** Shows the presence of ADA against the active metabolite of peginterferon beta-1a, active interferon beta 1a, in subject ABC-007.
**Rows 2-3:** Show the screening and confirmation of ADA against the PEG epitope of peginterferon beta-1a in subject ABC-007.
**Rows 4-5:** Show the screen and quantification of neutralizing ADA against the whole molecule peginterferon beta-1a in subject ABC-007.
**Row 6:** Shows the absence of ADA against the active metabolite of peginterferon beta 1a, active interferon beta 1a portion, in subject ABC-008.
**Rows 7-9:** Show the screening, confirmation, and quantification of ADA against the PEG epitope of peginterferon beta-1a, in subject ABC-008.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | ABC | IS | ABC-007 | 1 | A1 | | ADA_BAB | Binding Antidrug Antibody | ACTIVE INTERFERON BETA 1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 2 | ABC | IS | ABC-007 | 2 | A1 | | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELISA | 1 | VISIT 1 | 2017-07-27 |
| 3 | ABC | IS | ABC-007 | 3 | A1 | | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA1A | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | NEGATIVE | | NEGATIVE | | | SERUM | ELISA | 1 | VISIT 1 | 2017-07-27 |
| 4 | ABC | IS | ABC-007 | 4 | A1 | | ADA_NAB | Neutralizing Binding Antidrug Antibody | PEGINTERFERON BETA1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | REPORTER GENE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 5 | ABC | IS | ABC-007 | 5 | A1 | | ADA_NAB | Neutralizing Binding Antidrug Antibody | PEGINTERFERON BETA1A | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 4.7 | titer | 4.7 | 4.7 | titer | SERUM | REPORTER GENE IMMUNOASSAY | 1 | VISIT 1 | 2017-07-27 |
| 6 | ABC | IS | ABC-008 | 6 | V4 | | ADA_BAB | Binding Antidrug Antibody | ACTIVE INTERFERON BETA 1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | NEGATIVE | | NEGATIVE | | | SERUM | IMMUNOASSAY | 1 | VISIT 1 | 2017-08-27 |
| 7 | ABC | IS | ABC-008 | 7 | V4 | | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA1A | SCREEN | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELISA | 1 | VISIT 1 | 2017-08-27 |
| 8 | ABC | IS | ABC-008 | 8 | V4 | | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA1A | CONFIRM | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | ELISA | 1 | VISIT 1 | 2017-08-27 |
| 9 | ABC | IS | ABC-008 | 9 | V4 | | ADA_BAB | Binding Antidrug Antibody | PEG EPITOPE OF PEGINTERFERON BETA1A | QUANTIFY | ANTIDRUG ANTIBODIES | HUMORAL IMMUNITY | 40 | titer | 40 | 40 | titer | SERUM | ELISA | 1 | VISIT 1 | 2017-08-27 |

## Example 5

This example illustrates how to represent both study vaccine-induced humoral (antibody) immunity, and immunogenicity responses not related to the study vaccine but which are also important for collection, specifically in vaccine trials.

In this case, the subject was administered with a human respiratory syncytial virus (RSV) vaccine and his protective antibody production against the major component of the study vaccine, RSV-protein B, was assessed. Detection and quantification of the anti-RSV-protein B antibody data from baseline to post-vaccination were collected and are represented below. At baseline, antibody against RSV-protein Z was detected in the same subject, which suggests either natural infection by or previous vaccination with RSV-protein B at the time of assessment. Even though immunity against RSV-protein B was not the interest of the RSV vaccine study, immunological data pertaining to RSV-protein B was collected for the subject.

This example illustrates the use of the CDISC-recommended ISCAT values "STUDY VACCINE-RELATED IMMUNOGENICITY" and "NON-STUDY-RELATED IMMUNOGENICITY" to distinguish between study vaccine-induced immunogenicity and immunogenicity findings unrelated to the study vaccine data collected during a vaccine study. ISCAT = "NON-STUDY-RELATED IMMUNOGENICITY" was developed to explicitly and purposefully indicate whether an observed immunity toward an antigen was not related to the study vaccine but rather was a result of natural infection or previous vaccination. Oftentimes, it is simply impossible to tell whether the antibody found in a subject is due to a natural infection or previous vaccination (or both) — yet this immunogenicity, unrelated to the study vaccine, is important for collection and assessment at the screening phase of the trial.

In this example, immune responses against RSV-protein Z were measured during the study. Because protein Z is not inserted into the vaccine vector, any immune response detected toward protein Z was not related to the study vaccine, although important for assessment and collected per the study protocol. In order to show that RSV-protein Z-induced antibody production was unrelated to the immunity solicited by the study vaccine RSV-protein B (ISCAT = "STUDY VACCINE-RELATED IMMUNOGENICITY"), the ISCAT for rows 3 and 4 is "NON-STUDY-RELATED IMMUNOGENICITY" (note: protein Z and protein B are examples, refer to controlled terminology for standard terms associated with ISBDAGNT).

**Rows 1-2:** Show the screening and quantification of microbial-induced immunoglobulin G (IgG) antibody against the RSV-protein B at baseline, prior to the administration of the study vaccine. ISBDAGNT="HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B" is the immunogenic target in the study vaccine that could potentially stimulate the production of antibodies. Note: ISCAT="STUDY VACCINE-RELATED IMMUNOGENICITY", even though at this point the study vaccine has not been administered to the subject; this is done prospectively to enable the grouping of baseline and treatment measurements.
**Rows 3-4:** Show the screening and quantification of microbial-induced IgG antibody against the RSV-protein Z at baseline. Note: Because RSV-protein Z is not the immunogenic target of interest in this vaccine study, ISCAT is populated with the value "NON-STUDY-RELATED IMMUNOGENICITY".
**Rows 5-7:** Show the titer of microbial-induced IgG antibody against the RSV-protein B, post-vaccination at visits 1, 2, and 3. These 3 records show the antibody titers had increased post-vaccination, presumably due to the stimulation from the RSV study vaccine. ISCAT is populated with the value "STUDY VACCINE-RELATED IMMUNOGENICITY".

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | SCREEN | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | IMMUNOASSAY | 1 | BASELINE | 2017-05-27 |
| 2 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:24 | titer | NA | | | SERUM | IMMUNOASSAY | 1 | BASELINE | 2017-05-27 |
| 3 | RSV1230 | IS | RSV1230-011 | 3 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN Z | SCREEN | NON-STUDY-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | POSITIVE | | POSITIVE | | | SERUM | IMMUNOASSAY | 1 | BASELINE | 2017-05-27 |
| 4 | RSV1230 | IS | RSV1230-011 | 4 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN Z | QUANTIFY | NON-STUDY-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:50 | titer | NA | | | SERUM | IMMUNOASSAY | 1 | BASELINE | 2017-05-27 |
| 5 | RSV1230 | IS | RSV1230-011 | 5 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:100 | titer | NA | | | SERUM | IMMUNOASSAY | 2 | VISIT 1 | 2017-07-27 |
| 6 | RSV1230 | IS | RSV1230-011 | 6 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:250 | titer | NA | | | SERUM | IMMUNOASSAY | 3 | VISIT 2 | 2017-08-27 |
| 7 | RSV1230 | IS | RSV1230-011 | 7 | 13668 | MBIGSAB | IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:500 | titer | NA | | | SERUM | IMMUNOASSAY | 4 | VISIT 3 | 2017-09-27 |

Thus far, all the IS tests illustrated are measurements of concentrations of a substance (e.g., antibody titer). However, some immunogenicity tests are actual counts of immune cells that secrete a particular substance. These tests are described by the combination of ISTEST (Immunogenicity Test or Examination Name) and ISMSCBCE (Molecule Secreted by Cells), where ISTEST identifies the type of cells that secrete a specific substance (e.g., antibody-secreting cells, cytokine-secreting cells) and ISMSCBCE names the substance (e.g., IgG antibody, interferon-gamma). The following 2 examples introduce the IS domain-specific variable, ISMSCBCE, and illustrate its use with ISTEST to represent a complete immunological analyte of interest.

## Example 6

This example shows data about the assessment of antibody-secreting cells (ASCs).

Traditional methods such as enzyme-linked immunosorbent assay (ELISA) that monitor humoral immune responses after immunization or infection typically only quantify specific antibody titers in serum. These methods do not provide any information about the actual number and location of the immune cells that secrete these antibodies or cytokines.

The enzyme-linked immunospot (ELISpot) assay is a method to detect and quantify analyte-secreting T or B cells. During ELISpot testing, a colored precipitate forms and appears as spots at the sites of analyte localization (analytes typically are cytokines or antibodies), with each individual spot representing an individual analyte-secreting cell. The spots can be counted with an automated ELISpot reader system or manually, using a stereomicroscope. This example shows how to represent the quantification of ASCs as the number of spots per million peripheral blood mononuclear cells (PBMC) as determined by B-cell ELISpot from a vaccine trial.

The IS domain-specific variable ISMSCBCE introduced in this example allows flexibility in data representation and post-coordination of the various secreted antibody types and their respective ASCs. This approach liberates the ISTEST variable from having to house precoordinated and thus hyperspecific values crafted based on secretion and cell types.

**Row 1:** Shows the total number of IgG ASCs from a subject's blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is represented by the variable ISMSCBCE (i.e. IGG antibody non-specific to any antigen).
**Row 2:** Shows the number of H1-specific IgG ASCs from the same blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is in ISMSCBCE (i.e. IgG antibody specific to H1 antigen).
**Row 3:** Shows the number of H3-specific IgG ASCs from the same subject's blood sample. In this case, ISTEST="Antibody-secreting Cells"; the entity secreted by the cells in ISTEST is in ISMSCBCE (i.e. IgG antibody specific to H3 antigen).

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISMSCBCE | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | ISDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|-------|
| 1 | INFLA456 | IS | INF02-01 | 1 | SAMPLBC001 | ABSCCL | Antibody-secreting Cells | IGG ANTIBODY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 2019 | SFC/10^6 PBMC | 2019 | 2019 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2011-06-08 |
| 2 | INFLA456 | IS | INF02-01 | 2 | SAMPLBC001 | ABSCCL | Antibody-secreting Cells | INFLUENZA H1-SPECIFIC IGG ANTIBODY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 626 | SFC/10^6 PBMC | 626 | 626 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2011-06-08 |
| 3 | INFLA456 | IS | INF02-01 | 3 | SAMPLBC001 | ABSCCL | Antibody-secreting Cells | INFLUENZA H3-SPECIFIC IGG ANTIBODY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 592 | SFC/10^6 PBMC | 592 | 592 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2011-06-08 |

## Example 7

This example shows data from the in vitro assessment and quantification of cytokine-secreting immune cells, expressed in number of spot-forming cells (SFC) per million peripheral blood mononuclear cells (PBMC) as determined by T-cell ELISpot from a vaccine trial.

Through vaccination, it is expected that cytokine secretion in immune cells is boosted whenever immune cells encounter the same virus and/or the previously exposed viral antigens. By increasing this cytokine secretion, immune cells aid in the host defense and protection against (re-)infections. In vaccine trials, this can be measured by isolating immune cells (e.g., PBMCs) from subjects at multiple time points during the course of the trial and restimulating them with the virus or its viral antigens in vitro.

In this example, PBMCs were isolated from a subject participating in a vaccine study for RSV and restimulated in vitro with either a RSV-antigen or without a stimulating agent. At baseline (i.e., before vaccination), the RSV antigen-stimulated PBMCs produced minimal number of interferon gamma, as expressed in interferon gamma-secreting cells quantified in the number of SFC/10^6 PBMC (row 2), as compared to no stimulation (row 1). Three weeks after vaccination, RSV-antigen stimulated PBMCs (row 4) showed significant increase in the number of interferon-gamma secreting cells compared to no stimulation (row 3) or baseline values (rows 1 and 2). This suggests immunological memory of the immune cells after encountering the same microorganism or its antigens, and the switch of cell state from resting to active.

**Rows 1-2:** Show the measurement of interferon gamma (ISMSCBCE) cytokine-secreting cells (ISTEST) at baseline either with no stimulation (row 1) or stimulated with the RSV-antigen (row 2) in ISCNDAGT.
**Rows 3-4:** Show the measurement of interferon gamma (ISMSCBCE) cytokine-secreting cells (ISTEST) 3 weeks after vaccination and restimulation in vitro with the RSV-antigen (row 4) in ISCNDAGT and no stimulation (row 3), respectively.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISMSCBCE | ISTCND | ISCNDAGT | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|--------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITHOUT STIMULATING AGENT | | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 5.1 | SFC/10^6 PBMC | 5.1 | 5.1 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 1 | BASELINE | 2017-05-27 |
| 2 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITH STIMULATING AGENT | RSV-EPITOPE B | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 10.5 | SFC/10^6 PBMC | 10.5 | 10.5 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 1 | BASELINE | 2017-05-27 |
| 3 | RSV1230 | IS | RSV1230-011 | 3 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITHOUT STIMULATING AGENT | | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 60.8 | SFC/10^6 PBMC | 60.8 | 60.8 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2 | VISIT 1 | 2017-06-27 |
| 4 | RSV1230 | IS | RSV1230-011 | 4 | 13668 | CYKSCCL | Cytokine-secreting Cells | INTERFERON GAMMA | WITH STIMULATING AGENT | RSV-EPITOPE B | STUDY VACCINE-RELATED IMMUNOGENICITY | CELLULAR IMMUNITY | 260.5 | SFC/10^6 PBMC | 260.5 | 260.5 | SFC/10^6 PBMC | PERIPHERAL BLOOD MONONUCLEAR CELL | ELISPOT | 2 | VISIT 1 | 2017-06-27 |

## Example 8

In vaccine studies, microneutralization assays are commonly used in assays to quantify viral-specific neutralizing antibodies in a subject's specimen that can block viral infection in vitro, and therefore provide a measure of vaccine efficacy. A neutralizing antibody is an antibody that binds to, blocks, and prevents non-self agents from infecting cells.

When immunizing a subject with a vaccine, the hope is that the vaccine will induce antiviral and humoral-protective antibody responses in the subject; with an effective vaccine, the quantity of virus-specific antibodies that are able to block viral infection are increased. To test the efficacy of a vaccine, a microneutralization test is performed by adding a vaccinated subject's serum and the virus of study interest to cell cultures in vitro. If neutralizing antibodies are present in the subject's serum post-vaccination, those antibodies will bind to, block, and prevent the virus from infecting cells in the culture plates. The neutralization titer is the specific dilution of the antibody that blocks viral infection of the cells. The 50% neutralization titer (also known as NT50), in the context of microneutralization assays, is defined as the antiviral antibody titer that blocks 50% of viral infection of the cells. **Note:** Some users may represent the 50% neutralization titer as "IC50 titer" or other test descriptors. CDISC recommends mapping all such values in the ISTSTDTL variable.

NHOID is populated with respiratory syncytial virus because this microorganism is the subject of the vaccine efficacy test.

NHOID, defined by the Non-host Organism Identifiers (OI) domain, should be used to map microorganisms that have been either experimentally determined in the course of a study or are previously known (e.g., lab strains used as reference in the study). In other words, NHOID is used when the study subject is the microorganism, and when the microorganism is present in the testing sample. In vaccine efficacy studies, a subject's post-immunization sera is often incubated with a microbial strain of interest, where the functional capacities of the vaccine-induced antibodies are measured through whether the antibodies can effectively stop (from infection), neutralize, and kill the study microorganism of interest, in vitro. Examples of such tests include microneutralization, hemagglutination inhibition, and opsonophagocytic-killing assays. These are tests that measure the direct effect of the antimicrobial antibodies on the microorganism; therefore, said microorganism is the study subject and should be mapped to NHOID.

This example uses data from the same RSV vaccine study, where the subject is being vaccinated with a viral vector containing RSV. The subject is tested before (baseline) and after vaccination (visits 1 and 2) to investigate whether the anti-RSV antibodies present in the subject's serum also have the ability to neutralize RSV infection in vitro.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | NHOID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISCAT | ISSCAT | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|-------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | RSV1230 | IS | RSV1230-011 | RESPIRATORY SYNCYTIAL VIRUS | 1 | 13668 | MBNAB | Neutralizing Microbial-induced Antibody | RESPIRATORY SYNCYTIAL VIRUS | NEUTRALIZING TITER 50% | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:40 | | 40 | 40 | titer | SERUM | MICRONEUTRALIZATION ASSAY | 1 | BASELINE | 2017-05-27 |
| 2 | RSV1230 | IS | RSV1230-011 | RESPIRATORY SYNCYTIAL VIRUS | 2 | 13668 | MBNAB | Neutralizing Microbial-induced Antibody | RESPIRATORY SYNCYTIAL VIRUS | NEUTRALIZING TITER 50% | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:80 | | 80 | 80 | titer | SERUM | MICRONEUTRALIZATION ASSAY | 2 | VISIT 1 | 2017-07-27 |
| 3 | RSV1230 | IS | RSV1230-011 | RESPIRATORY SYNCYTIAL VIRUS | 3 | 13668 | MBNAB | Neutralizing Microbial-induced Antibody | RESPIRATORY SYNCYTIAL VIRUS | NEUTRALIZING TITER 50% | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:200 | | 200 | 200 | titer | SERUM | MICRONEUTRALIZATION ASSAY | 3 | VISIT 2 | 2017-09-27 |

## Example 9

In vaccine trials, the OPK assay is used as a correlate for immunoprotectivity against antigens, by measuring the functional capacities of vaccine-induced antibodies.

Typically, this test is performed by incubating a subject's post-immunization sera with the bacterial strain of interest, phagocytes, and complement proteins. If antibacterial, functional antibodies are present in the serum, those antibodies will bind to the bacteria together with complement proteins. This subsequently targets the bacteria for opsonization, the ingestion and destruction of invading non-self agents by phagocytes. With vaccination, the quantity of bacterial-specific, functional antibodies are increased, leading to a decreased number of viable bacterial cells in the presence of phagocytes, functional antibodies, and complement. The assay read-out is expressed in by the opsonization index, which is calculated using linear interpolation of the serum dilution containing functional antibody killing the desired percentage (usually 50%) of the bacteria, using a specified algorithm.

NHOID is populated with Staphylococcus aureus 04-02981 because this strain of S. aureus is the subject of the vaccine efficacy test.

NHOID, defined by the Non-host Organism Identifiers (OI) domain, should be used to map microorganisms that have been either experimentally determined in the course of a study or are previously known (e.g., lab strains used as reference in the study). In other words, NHOID is used when the study subject is the microorganism, and when the microorganism is present in the testing sample. In vaccine efficacy studies, a subject's post-immunization sera is often incubated with a microbial strain of interest, where the functional capacities of the vaccine-induced antibodies are measured through whether the antibodies can effectively stop (from infection), neutralize, and kill the study microorganism of interest, in vitro. Examples of such tests include microneutralization, hemagglutination inhibition, and opsonophagocytic-killing assays. These are tests that measure the direct effect of the antimicrobial antibodies on the microorganism; therefore, said microorganism is the study subject and should be mapped to NHOID.

In this vaccine-study example, the subject is vaccinated with a vector containing S. aureus-epitope X (note: epitope X is an example, refer to controlled terminology for standard terms associated with ISBDAGNT). The subject is tested before (baseline) and after vaccination (visits 1 and 2) to investigate whether the vaccine-induced functional antibodies drive efficient complement deposition and subsequent opsonophagocytic killing of S. aureus, in vitro. The assay read-out is expressed by the opsonization index (ISTSTDTL), which is a unit-less test.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | NHOID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISCAT | ISSCAT | ISORRES | ISSTRESC | ISSTRESN | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|-------|---------|----------|--------|----------|----------|-------|--------|---------|----------|----------|--------|----------|----------|-------|-------|
| 1 | SAU1230 | IS | SAU1230-011 | STAPHYLOCOCCUS AUREUS 04-02981 | 1 | 13668 | MBFAB | Functional Microbial-induced Antibody | STAPHYLOCOCCUS AUREUS-EPITOPE X | OPSONIZATION INDEX | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 100 | 100 | 100 | SERUM | OPSONOPHAGOCYTIC KILLING ASSAY | 1 | BASELINE | 2017-05-27 |
| 2 | SAU1230 | IS | SAU1230-011 | STAPHYLOCOCCUS AUREUS 04-02981 | 2 | 13668 | MBFAB | Functional Microbial-induced Antibody | STAPHYLOCOCCUS AUREUS-EPITOPE X | OPSONIZATION INDEX | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1000 | 1000 | 1000 | SERUM | OPSONOPHAGOCYTIC KILLING ASSAY | 2 | VISIT 1 | 2017-07-27 |
| 3 | SAU1230 | IS | SAU1230-011 | STAPHYLOCOCCUS AUREUS 04-02981 | 3 | 13668 | MBFAB | Functional Microbial-induced Antibody | STAPHYLOCOCCUS AUREUS-EPITOPE X | OPSONIZATION INDEX | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 5000 | 5000 | 5000 | SERUM | OPSONOPHAGOCYTIC KILLING ASSAY | 3 | VISIT 2 | 2017-09-27 |

## Example 10

This example shows how to present data from an autoimmune disease study, specifically how to represent information from disease-specific autoantibody tests.

Sjogren's syndrome (SS) is a systemic autoimmune disease characterized by dry eyes and dry mouth. Diagnosis of SS is generally based on the detection of antinuclear antibodies (ANAs), that is, anti-Ro (SS-A) and anti-La (SS-B) antibodies.

**Rows 1-5:** Show the screening (row 1) and quantification (rows 2, 4) of ANAs. Rows 2 and 3 are grouped together using ISGRPID="1a"; this means the titer result in row 2 is specifically related to the particular nuclear staining pattern (i.e., speckled) finding in row 3. The speckled pattern of ANA is typically indicative of SS, systemic lupus, and mixed connective tissue disease. Rows 4 and 5 are grouped together using ISGRPID="1b"; this means the titer result in row 4 is specifically related to the nuclear staining pattern (i.e., nucleolar) finding in row 5. Rows 1 to 5 are grouped together with values starting with the number "1", indicating that these records are related. The antinuclear antibodies test is post-coordinated using ISGRPID and represented by both ISTEST="Autoantibody" and ISBDAGNT="NUCLEAR AUTOANTIGENS".
**Rows 6-11:** Show the screening and quantification of the various SS-specific autoantibodies. SS autoantigens are represented by the ISBDAGNT variable, whereas the ISTEST="Autoantibody".

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISTSTOPO | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|----------|----------|----------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | XYZ | IS | XYZ1234 | 1 | 19283746 | 1 | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | | SCREEN | POSITIVE | | POSITIVE | | | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 2 | XYZ | IS | XYZ1234 | 2 | 19283746 | 1a | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | | QUANTIFY | 1:340 | | 340 | 340 | titer | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 3 | XYZ | IS | XYZ1234 | 3 | 19283746 | 1a | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | STAINING PATTERN | | SPECKLED PATTERN | | SPECKLED PATTERN | | | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 4 | XYZ | IS | XYZ1234 | 4 | 19283746 | 1b | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | | QUANTIFY | 1:170 | | 170 | 170 | titer | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 5 | XYZ | IS | XYZ1234 | 5 | 19283746 | 1b | ATAB | Autoantibody | NUCLEAR AUTOANTIGENS | STAINING PATTERN | | NUCLEOLAR PATTERN | | NUCLEOLAR PATTERN | | | SERUM | FLUORESCENT IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 6 | XYZ | IS | XYZ1234 | 6 | 19283746 | 2 | ATAB | Autoantibody | SJOGRENS SS-A60 ANTIGEN | | SCREEN | POSITIVE | | POSITIVE | | | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 7 | XYZ | IS | XYZ1234 | 7 | 19283746 | 2 | ATAB | Autoantibody | SJOGRENS SS-A60 ANTIGEN | | QUANTIFY | 181 | U/mL | 181 | 181 | U/mL | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 8 | XYZ | IS | XYZ1234 | 8 | 19283746 | 3 | ATAB | Autoantibody | SJOGRENS SS-A52 ANTIGEN | | SCREEN | POSITIVE | | POSITIVE | | | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 9 | XYZ | IS | XYZ1234 | 9 | 19283746 | 3 | ATAB | Autoantibody | SJOGRENS SS-A52 ANTIGEN | | QUANTIFY | 51 | U/mL | 51 | 51 | U/mL | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 10 | XYZ | IS | XYZ1234 | 10 | 19283746 | 4 | ATAB | Autoantibody | SJOGRENS SS-B ANTIGEN | | SCREEN | POSITIVE | | POSITIVE | | | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |
| 11 | XYZ | IS | XYZ1234 | 11 | 19283746 | 4 | ATAB | Autoantibody | SJOGRENS SS-B ANTIGEN | | QUANTIFY | 169 | U/mL | 169 | 169 | U/mL | SERUM | MULTIPLEXED BEAD BASED IMMUNOASSAY | 1 | SCREENING | 2018-06-20 |

## Example 11

This example shows how to represent data from various allergy tests, specifically data from a mixed animal allergens test.

**Row 1:** Shows the detection of immunoglobulin E (IgE) antibody against multiple animal allergens. ISBDAGNT is used to house the generic but controlled value "ANIMAL MIX ANTIGENS, MULTIPLE".
**Rows 2-3:** Show the amount of IgE antibody against dog dander and its RAST classification score.
**Rows 4-5:** Show the amount of IgE antibody against cat dander and its RAST classification score.
**Rows 6-7:** Show the amount of IgE antibody against horse dander and its RAST classification score.
**Rows 8-9:** Show the amount of IgE antibody against cow dander and its RAST classification score.

**is.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTDTL | ISORRES | ISORRESU | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|----------|----------|---------|----------|----------|----------|----------|--------|----------|----------|-------|-------|
| 1 | XYZ | IS | XYZ1234 | 1 | 12453333 | ARIGEAB | Allergen-induced IgE Antibody | ANIMAL MIX ANTIGENS, MULTIPLE | | POSITIVE | | POSITIVE | | | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 2 | XYZ | IS | XYZ1234 | 2 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | DOG DANDER ANTIGEN | | 0.12 | U/mL | 0.12 | 0.12 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 3 | XYZ | IS | XYZ1234 | 3 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | DOG DANDER ANTIGEN | RAST SCORE | 0 | | 0 | 0 | | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 4 | XYZ | IS | XYZ1234 | 4 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | CAT DANDER ANTIGEN | | 0.19 | U/mL | 0.19 | 0.19 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 5 | XYZ | IS | XYZ1234 | 5 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | CAT DANDER ANTIGEN | RAST SCORE | 0 | | 0 | 0 | | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 6 | XYZ | IS | XYZ1234 | 6 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | HORSE DANDER ANTIGEN | | 44 | U/mL | 44 | 44 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 7 | XYZ | IS | XYZ1234 | 7 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | HORSE DANDER ANTIGEN | RAST SCORE | 4 | | 4 | 4 | | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 8 | XYZ | IS | XYZ1234 | 8 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | COW DANDER ANTIGEN | | 120 | U/mL | 120 | 120 | U/mL | SERUM | RIA | 1 | SCREENING | 2018-06-20 |
| 9 | XYZ | IS | XYZ1234 | 9 | 12456666 | ARIGEAB | Allergen-induced IgE Antibody | COW DANDER ANTIGEN | RAST SCORE | 6 | | 6 | 6 | | SERUM | RIA | 1 | SCREENING | 2018-06-20 |

The SUPPIS dataset shows the specific and individual animal allergens within the animal mixed antigens panel test.

**suppis.xpt**

| Row | STUDYID | DOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|--------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | DOG | CRF | |
| 2 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | CAT | CRF | |
| 3 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | HORSE | CRF | |
| 4 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISMIXCOP | Mixture Component | COW | CRF | |

Alternatively, instead of reporting the specific components of a mixed allergen panel, regional allergen mixes may also be reported by the specific regions/areas where they are predominant, as shown in the SUPPIS dataset below.

**suppis.xpt**

| Row | STUDYID | DOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|--------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | XYZ | IS | XYZ1234 | ISBDAGNT | 1 | ISALGREG | Allergen Mixture Region | CENTRAL CA, AREA 14 | CRF | |
