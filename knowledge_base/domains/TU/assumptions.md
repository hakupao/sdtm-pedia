# TU — Assumptions

A findings domain that represents data that uniquely identifies tumors, lesions, or locations of interest under study. The TU domain represents data that uniquely identifies tumors, lesions, or locations of interest (e.g., tumors, cardiovascular culprit lesions, organs, bone marrow, other sites of disease such as lymph nodes). Commonly, tumors/lesions/locations of interest are identified by an investigator and/or independent assessor and classified according to the disease assessment criteria. For example, an oncology study using RECIST criteria would identify target, non-target, and new tumors.

1. The TU domain should contain only 1 record for each unique tumor/lesion/location of interest identified by an assessor (e.g., investigator, independent assessor) per medical evaluator. The initial identification of a tumor/lesion/location of interest is done once, usually at baseline (e.g., identification of target and non-target tumors/lesions) or first appearance of new tumor/lesion. The identification information, including the location description, must not be repeated for every visit. A record is required in TU to identify and create the TULNKID when there are associated records in TR with matching TRLNKID. The following are examples of when post-baseline records might be included in the TU domain:
    a. A new tumor/lesion may emerge at any time during a study; therefore, a new post-baseline record would represent the identification of the new tumor/lesion.
    b. If a tumor/lesion identified at baseline subsequently splits into separate distinct tumors/lesions, then additional post-baseline records can be included to distinctly identify the split tumors/lesions.
    c. In situations where a re-baseline of targets and non-targets is required (e.g., a cross-over study), then a separate set of target and non-target tumors/lesions might be identified and those identification records would be represented.

2. TRLNKID is used to relate an identification record in the TU domain to assessment records in the Tumor/Lesion Results (TR) domain. The organization of data across the TU and TR domains requires a linking mechanism. The TULNKID variable is used to provide a unique code for each identified tumor/lesion. The values of TULNKID are compound values that may carry the following information: an indication of the role (or assessor) providing the data record, when it is someone other than the principal investigator; an indication of whether the data record is for a target or non-target tumor/lesion; a tracking identifier or number; and an indication of whether the tumor/lesion has split (see assumption 3 for details on splitting). A RELREC relationship record can be created to describe the link, probably as a dataset-to-dataset link.

    TUTESTCD/TUTEST values for this domain are published as Controlled Terminology. For some TUTESTCD/TUTEST values, CDISC CT includes codelists for use with TUORRES. The associations between the test values and results are in the Oncology codetable, which, along with the CT Rules for Oncology, is available at https://www.cdisc.org/standards/terminology/controlled-terminology.

    During the course of a trial, a tumor/lesion identified at baseline might split into one or more distinct tumors/lesions, or 2 or more tumors/lesions might merge to form a single tumor/lesion. The following example shows the preferred approach for representing split lesions in TU. However, the approach depends on how the data for split and merged tumors/lesions are captured. The preferred approach requires the measurements of each distinct tumor/lesion to be captured individually.

    Example target tumor T04, identified at the screening visit, splits into 2 at week 16. Two new records are created with TUTEST = "Tumor Split"; TULNKID reflects the split by adding 0.1 and 0.2 to the original TULNKID value.

    | TULNKID | TUTESTCD | TUTEST | TUORRES | VISIT |
    |---------|----------|--------|---------|-------|
    | T01 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
    | T02 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
    | T03 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
    | T04 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
    | NT01 | TUMIDENT | Tumor Identification | NON-TARGET | SCREEN |
    | NT02 | TUMIDENT | Tumor Identification | NON-TARGET | SCREEN |
    | T04.1 | TUSPLIT | Tumor Split | TARGET | WEEK 16 |
    | T04.2 | TUSPLIT | Tumor Split | TARGET | WEEK 16 |
    | NEW01 | TUMIDENT | Tumor Identification | NEW | WEEK 32 |

    If the data collection does not support this approach (i.e., measurements of split tumors/lesions are reported as a summary under the "parent" tumor/lesion), then it may not be possible to include a record in the TU domain. In this situation, the assessments of split and merge tumors/lesions would be represented only in the TR domain.

3. For some response criteria (e.g., Lugano, Kumar IMWG 2016), tumors are assessed by location of interest. A record is required in TU in order to link the assessments of the particular location of interest in TR. In TULNKID = "L01", the spleen is identified as a location of interest using computerized tomography (CT) scan. In TULNKID = "L04", the whole body is identified as a location of interest using positron emission tomography (PET) scan.

    | TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TUMETHOD |
    |---------|----------|--------|---------|-------|----------|
    | L01 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | SPLEEN | CT SCAN |
    | L02 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | LIVER | CT SCAN |
    | L03 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | BONE MARROW | PET SCAN |
    | L04 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | BODY | PET SCAN |

4. During the course of a trial, when a new tumor/lesion is identified, information about that new tumor/lesion may be collected to different levels of detail. For example, if anatomical location of a new tumor/lesion is not collected, TULOC will be blank. All new tumors/lesions are to be represented in TU and TR domains.

5. The additional anatomical location variables --LAT, --DIR, --PORTOT were added from the SDTM. These extra variables allow for more detailed information to be collected that further clarifies the value of the TULOC variable.

6. In the oncology setting, when a new tumor is identified, a record must be included in both the TU and TR domains. At a minimum, the TR record would contain TRLNKID = "NEW0" and TRTESTCD = "TUMSTATE" and TRORRES = "PRESENT" for unequivocal new tumors. The TU record may contain different levels of detail depending upon the data collection methods employed. Although it is possible that a sponsor may have a different chosen method, the following are the most common scenarios:
    a. The occurrence of a new tumor/lesion is the sole piece of information that a sponsor collects, because this is a sign of disease progression; no further details are required. In such cases, a record would be created where TUTEST = "Tumor Identification" and TUORRES = "NEW", and the identifier, TULNKID, would be populated in order to link to the associated information in the TR domain.
    b. The occurrence of a new tumor/lesion and the anatomical location of that newly identified tumor/lesion are the only collected pieces of information. In this case, it is expected that a record would be created where TUTEST = "Tumor Identification" and TUORRES = "NEW"; the TULOC variable would be populated with the anatomical location information (the additional location variables may be populated depending on the level of detail collected), and the identifier, TULNKID, would be populated in order to link to the associated information in the TR domain.
    c. The sponsor records the occurrence of a new tumor/lesion to the same level of detail as target tumors/lesions. For example, with the occurrence of a new tumor, its anatomical location and its measurement might be recorded. In this case, it is expected that a record would be created where TUTEST = "Tumor Identification" and TUORRES = "NEW". The TULOC variable would be populated with the anatomical location information (the additional location variables may be populated depending on the level of detail collected) and the identifier, TULNKID, would be populated in order to link to the associated information in the TR domain. In this scenario, measurements/assessments would also be recorded in the TR domain.

7. The acceptance flag variable (TUACPTFL) identifies records that have been determined to be the accepted assessments/measurements by an independent assessor. This flag would be provided by an independent assessor and when multiple evaluators (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provide assessments or evaluations at the same time point or an overall evaluation. This flag should not be used by a sponsor for any other purpose. It is not expected that the TUACPTFL flag would be populated by the sponsor; instead, that type of record selection should be handled in the analysis dataset (ADaM).

8. The evaluator-specified variable TUEVALID is used in conjunction with TUEVAL to provide additional detail regarding who is providing tumor identification information (e.g., TUEVAL = "INDEPENDENT ASSESSOR", TUEVALID = "RADIOLOGIST 1"). The TUEVALID variable is subject to controlled terminology. **Note:** TUEVAL must also be populated when TUEVALID is populated.

9. If indicator questions for specific types of tumor or lesions are collected (e.g., Does the subject have target tumors? Does the subject have any non-targets? Did the subject have metastatic disease at screening?), then these TUTESTs will be included in TU. If indicator questions are not collected, do not introduce them into TU.

    This example shows indicator TUTESTs for a subject with non-target lesions only.

    | TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TUMETHOD |
    |---------|----------|--------|---------|-------|----------|
    | | NTIND | Non-Target Indicator | Y | | CT SCAN |
    | | TIND | Target Indicator | N | | CT SCAN |
    | NT01 | TUMIDENT | Tumor Identification | NON-TARGET | LUNG | CT SCAN |

    This example shows indicator TUTESTs for the identification of the sites of metastatic disease sites at baseline.

    | TULNKID | TUTESTCD | TUTEST | TUORRES | TUSTAT | TULOC | TUMETHOD | VISIT |
    |---------|----------|--------|---------|--------|-------|----------|-------|
    | | METIND | Metastatic Tumor Site Indicator | Y | | LIVER | CT SCAN | BASELINE |
    | | METIND | Metastatic Tumor Site Indicator | N | | BRAIN | MRI | BASELINE |
    | | METIND | Metastatic Tumor Site Indicator | NOT DONE | | PLEURAL CAVITY | | BASELINE |

10. Disease recurrence can be represented in the TU domain as an identification for the appearance of new tumors. The TUTEST Disease Recurrence Relative Location is used identify the region or relative location for the disease recurrence. The image identifier is in TUREFID and may match a PRREFID in the Procedures (PR) domain. The PR domain would contain the scans performed per protocol at each assessment; only when new tumors appear would records be included in TU.

    This example shows disease recurrence data in an adjuvant breast cancer study where the subject was initially diagnosed with cancer in the left breast only. This example shows a case where disease recurrence was identified in various locations. TUTEST=Disease Recurrence Relative Location is used to identify the reference location of the recurrence (e.g., LOCAL, REGIONAL, DISTANT, LOCOREGIONAL). A local disease recurrence was identified in the left breast, regional disease recurrence was identified in the ipsilateral internal mammary and the ipsilateral infraclavicular nodes, distant disease recurrence was identified in the liver and colon, and contralateral disease recurrence was identified in the right breast.

    | TUREFID | TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TULAT | TUMETHOD |
    |---------|---------|----------|--------|---------|-------|-------|----------|
    | IMG-00007 | LOC01 | DRCRLLTC | Disease Recurrence Relative Location | LOCAL | BREAST | LEFT | CT SCAN |
    | IMG-00007 | REG01 | DRCRLLTC | Disease Recurrence Relative Location | REGIONAL | INTERNAL MAMMARY LYMPH NODE | | CT SCAN |
    | IMG-00007 | REG02 | DRCRLLTC | Disease Recurrence Relative Location | REGIONAL | INFRACLAVICULAR LYMPH NODE | | CT SCAN |
    | IMG-00007 | DIS01 | DRCRLLTC | Disease Recurrence Relative Location | DISTANT | LIVER | | CT SCAN |
    | IMG-00007 | DIS02 | DRCRLLTC | Disease Recurrence Relative Location | DISTANT | COLON | | CT SCAN |
    | IMG-00007 | CON01 | DRCRLLTC | Disease Recurrence Relative Location | CONTRALATE RAL | BREAST | RIGHT | CT SCAN |

11. The following proposed supplemental qualifiers would be used for oncology studies to represent information regarding previous irradiation of a tumor when that information is captured in association with a specific tumor.

    | QNAM | QLABEL | Definition |
    |------|--------|------------|
    | TUPREVIR | Previously Irradiated | Indication of previous irradiation to a tumor |
    | TUPREISP | Irradiated then Subsequent Progression | Indication of documented progression subsequent to irradiation |

12. When additional data are collected about a procedure used for tumor/lesion identification, the data about the procedure are stored in the PR domain; the link between the tumor/lesion identification and the procedure should be recorded using RELREC.

13. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the TU domain, but the following qualifiers would not generally be used: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.
