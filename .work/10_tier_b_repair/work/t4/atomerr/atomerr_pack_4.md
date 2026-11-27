# T4 加查包 4 — ATOM_ERR (S1-R1) (20 条, 全检; 编号 E64-E83)

> 由 `scripts/t4/t4_atomerr_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 E).

### E64. `ig34_p0337_a003` — ae:S1R1_ATOM_ERR

- PDF 页 337 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.2 Clinical Classifications Use Case`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-RS audit: verbatim 与 PDF 页文本不符 实为 p336 CC 3c; KB 与页文本一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RS_audit.md:11 (页级行; 该批以范围/页号记这组原子)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
If a clinical classification uses a source value by comparing it to a range (e.g., "2-5", ">-3"), then the source value will exist only in the source domain; the range is represented in the corresponding RS record in RSORRES and RSORRESRU.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0336.txt` 第 34-35 行 (自动定位, 词覆盖 0.969; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 33|                  RSORRESU populated to agree with the units shown on the clinical classification instrument, which may be different from the sponsor’s usual practice for original and standard units.
 34|             c.   If a clinical classification uses a a source value by comparing it to a range (e.g., "2-5", ">3"), then the source value will exist only in the source domain; the range is represented in the corresponding RS
 35|                  record in RSORRES and RSORRESU.
 36|             d.   In all cases, RSSTRESC/RSSTRESN should be populated with the assigned ordinal score as indicated on the instrument.
~~~~

KB 现文: `knowledge_base/domains/RS/assumptions.md:81-81` (来源: fuzzy locate (score 0.969)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  81|    c. If a clinical classification uses a source value by comparing it to a range (e.g., "2-5", ">3"), then the source value will exist only in the source domain; the range is represented in the corresponding RS record in RSORRES and RSORRESU.
~~~~

### E65. `ig34_p0337_a006` — ae:S1R1_ATOM_ERR

- PDF 页 337 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.2 Clinical Classifications Use Case`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RS_audit.md:11 (页级行; 该批以范围/页号记这组原子)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The name of a QRS instrument is described under the variable --CAT in the relevant QRS domain (i.e., FT, QS, RS), and may be either abbreviations or longer names. For example, "ADAS-Cog", "BPI SHORT FORM", and "APACHE II" are all --CATs which are shortened names for the instruments they represent, whereas "al STAIR ASCEND" is the FTCAT for the instrument of the same name. Sponsors should always reference CDISC Controlled Terminology.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0337.txt` 第 3-6 行 (自动定位, 词覆盖 0.982; 版式以原 PDF 为准):

~~~~
  2| use case of RS):
  3|      1.   The name of a QRS instrument is described under the variable --CAT in the relevant QRS domain (i.e., FT, QS, RS), and may be either abbreviations or
  4|           longer names. For example, "ADAS-COG", "BPI SHORT FORM", and "APACHE II" are all --CATs which are shortened names for the instruments
  5|           they represent, whereas "4 STAIR ASCEND" is the FTCAT for the instrument of the same name. Sponsors should always reference CDISC Controlled
  6|           Terminology.
  7|           a.   The QRS Naming Rules for --CAT, --TEST, and --TESTCD and the list of QRS instruments that have published CDISC Controlled Terminology
~~~~

KB 现文: `knowledge_base/domains/FT/assumptions.md:38-38` (来源: fuzzy locate (score 0.982)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  38| 1. The name of a QRS instrument is described under the variable --CAT in the relevant QRS domain (i.e., FT, QS, RS), and may be either abbreviations or longer names. For example, "ADAS-COG", "BPI SHORT FORM", and "APACHE II" are all --CATs which are shortened names for the instruments they represent, whereas "4 STAIR ASCEND" is the FTCAT for the instrument of the same name. Sponsors should always reference CDISC Controlled Terminology.
~~~~

### E66. `ig34_p0337_a015` — ae:S1R1_ATOM_ERR

- PDF 页 337 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.2 Clinical Classifications Use Case`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RS_audit.md:11 (页级行; 该批以范围/页号记这组原子)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
There are cases where QRS CRFs do not include numeric "standardized responses" assigned to text responses (e.g., mild, moderate, severe being 1, 2, 3). It is clearly in everyone's best interest to include the numeric "standardized responses" in the SDTMIG QRS dataset. This is only done when the numeric "standardized response" are documented in the QRS CRF instructions, a user manual, a website specific to the QRS instrument, or another reference document that provides a clear explanation and rationale for providing them in the SDTMIG QRS dataset.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0337.txt` 第 17-20 行 (自动定位, 词覆盖 0.984; 版式以原 PDF 为准):

~~~~
 16|                they are used.
 17|      3.   There are cases where QRS CRFs do not include numeric “standardized responses” assigned to text responses (e.g., mild, moderate, severe being 1, 2,
 18|           3). It is clearly in everyone's best interest to include the numeric “standardized responses” in the SDTMIG QRS dataset. This is only done when the
 19|           numeric “standardized responses” are documented in the QRS CRF instructions, a user manual, a website specific to the QRS instrument, or another
 20|           reference document that provides a clear explanation and rationale for providing them in the SDTMIG QRS dataset.
 21|      4.   Sponsors should always consult published QRS supplements for guidance on submitting derived information in a SDTMIG QRS domain. Derived
~~~~

KB 现文: `knowledge_base/domains/FT/assumptions.md:49-49` (来源: fuzzy locate (score 0.984)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  49| 3. There are cases where QRS CRFs do not include numeric “standardized responses” assigned to text responses (e.g., mild, moderate, severe being 1, 2, 3). It is clearly in everyone's best interest to include the numeric “standardized responses” in the SDTMIG QRS dataset. This is only done when the numeric “standardized responses” are documented in the QRS CRF instructions, a user manual, a website specific to the QRS instrument, or another reference document that provides a clear explanation and rationale for providing them in the SDTMIG QRS dataset.
~~~~

### E67. `ig34_p0338_a002` — ae:S1R1_ATOM_ERR

- PDF 页 338 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.2 Clinical Classifications Use Case`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RS_audit.md:14 (页级行; 该批以范围/页号记这组原子)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The QRS instrument subtotal or total score, which is the sum of the numeric responses for an instrument, is populated in --ORRES, --STRESC, and --STRESN. It is considered a captured subtotal or total score without any knowledge of the sponsor's case management process reduced to the score.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0338.txt` 第 1-12 行 (自动定位, 词覆盖 0.971; 版式以原 PDF 为准):

~~~~
  1|           b.   The QRS instrument subtotal or total score, which is the sum of the numeric responses for an instrument, is populated in --ORRES, --STRESC, and
  2|                --STRESN. It is considered a captured subtotal or total score without any knowledge of the sponsor-data management processes related to the score.
  3|                 i. If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their eCRF process to derive subtotal
  4|                    and total scores. An investigator-derived score written on a CRF will be considered a captured score and not flagged. When subtotal and total
  5|                    scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y". However, when the subtotal and total scores are received from a
  6|                    central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for
  7|                    Variables).
  8|      5.   The variable --REPNUM variable is populated when there are multiple repeats of the same question. When records are related to the first trial of the
  9|           question, the variable --REPNUM should be set to "1". When records are related to the second trial of the same question, --REPNUM should be set to
 10|           "2", and so forth.
 11|      6.   The actual version number of an instrument is represented in the --CAT value as designated by the QRS Terminology Team. If it is determined that this
 12|           is not the case for an instrument:
 13|           a.   Notify the QRS Terminology Team that the instrument has a specific or multiple version numbers. This team will assist in providing an resolution
~~~~

KB 现文: `knowledge_base/domains/FT/assumptions.md:55-58` (来源: fuzzy locate (score 0.971)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  55|       iii. QRS subtotal, total, etc. scores not listed on the CRF, but known to be included in eData by sponsors are considered as captured data, are included in the instrument’s controlled terminology. The QRS instrument’s CT is considered extensible for this case and the subtotal or total score should be requested to be added.
  56|          1. Any imputations/calculations done to numeric “standardized responses” to produce the total score via transforming numeric “standardized responses” in any way would be done as ADaM derivations.
  57|    b. The QRS instrument subtotal or total score, which is the sum of the numeric responses for an instrument, is populated in --ORRES, --STRESC, and --STRESN. It is considered a captured subtotal or total score without any knowledge of the sponsor-data management processes related to the score.
  58|       i. If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their eCRF process to derive subtotal and total scores. An investigator-derived score written on a CRF will be considered a captured score and not flagged. When subtotal and total scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y". However, when the subtotal and total scores are received from a central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).
~~~~

### E68. `ig34_p0338_a003` — ae:S1R1_ATOM_ERR

- PDF 页 338 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.2 Clinical Classifications Use Case`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RS_audit.md:14 (页级行; 该批以范围/页号记这组原子)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their cRF process to derive subtotal and total scores. An investigator-derived score written on a CRF will be considered a captured score and will not be flagged. When subtotal and total scores are received from a central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0338.txt` 第 3-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2|                --STRESN. It is considered a captured subtotal or total score without any knowledge of the sponsor-data management processes related to the score.
  3|                 i. If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their eCRF process to derive subtotal
  4|                    and total scores. An investigator-derived score written on a CRF will be considered a captured score and not flagged. When subtotal and total
  5|                    scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y". However, when the subtotal and total scores are received from a
  6|                    central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for
  7|                    Variables).
  8|      5.   The variable --REPNUM variable is populated when there are multiple repeats of the same question. When records are related to the first trial of the
~~~~

KB 现文: `knowledge_base/domains/FT/assumptions.md:58-58` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  58|       i. If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their eCRF process to derive subtotal and total scores. An investigator-derived score written on a CRF will be considered a captured score and not flagged. When subtotal and total scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y". However, when the subtotal and total scores are received from a central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).
~~~~

### E69. `ig34_p0338_a010` — ae:S1R1_ATOM_ERR

- PDF 页 338 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.2 Clinical Classifications Use Case`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RS_audit.md:14 (页级行; 该批以范围/页号记这组原子)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
If the variable --TEST is represented with verbatim text >40 characters, represent the abbreviated meaningful text in --TEST within 40 characters and describe the full text of the item in the study metadata. If the verbatim item in the study metadata. If the verbatim item text in the study metadata is >200 characters, represent the abbreviated meaningful text in SSORRES within the 200 characters and describe the full text in the study metadata; see Section 4.5.3, Text Strings that Exceed the Maximum Length for General Observation-class Findings. For further information.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0338.txt` 第 19-22 行 (自动定位, 词覆盖 0.952; 版式以原 PDF 为准):

~~~~
 18|           d.   The sponsor is expected to provide information about the scoring rules in the metadata.
 19|      7.   If the variable --TEST is represented with verbatim text >40 characters, represent the abbreviated meaningful text in --TEST within 40 characters and
 20|           describe the full text of the item in the study metadata. If the verbatim item response (e.g., --QSORRES) is >200 characters, represent the abbreviated
 21|           meaningful text in QSORRES within the 200 characters and describe the full text in the study metadata; see Section 4 of the QRS supplement. See
 22|           Section 4.5.3, Text Strings that Exceed the Maximum Length for General Observation-class Domain Variables, for further information.
 23|           a.   The instrument’s annotated CRF can also be used as a reference for the full text in both of these situations.
~~~~

KB 现文: `knowledge_base/domains/FT/assumptions.md:68-68` (来源: fuzzy locate (score 0.952)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  68| 7. If the variable --TEST is represented with verbatim text >40 characters, represent the abbreviated meaningful text in --TEST within 40 characters and describe the full text of the item in the study metadata. If the verbatim item response (e.g., --QSORRES) is >200 characters, represent the abbreviated meaningful text in QSORRES within the 200 characters and describe the full text in the study metadata; see Section 4 of the QRS supplement. See Section 4.5.3, Text Strings that Exceed the Maximum Length for General Observation-class Domain Variables, for further information.
~~~~

### E70. `ig34_p0338_a013` — ae:S1R1_ATOM_ERR

- PDF 页 338 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.2 Clinical Classifications Use Case`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RS_audit.md:19`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
All standard QRS supplement development is coordinated with the CDISC SDS QRS Subteam as the governing body. The process involves drafting the controlled terminology and defining instrument-specific standardized value for qualifier, timing, and result variables to populate the SDTMIG for FT, QS, and RS domains. These supplements are developed based on user demand and therapeutic area standards development needs. Sponsors should always consult the CDISC website to review the terminology and supplements prior to modeling any QRS instruments.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0338.txt` 第 25-31 行 (自动定位, 词覆盖 0.983; 版式以原 PDF 为准):

~~~~
 24|      8.   --EVAL and --EVALID must not be used to model QRS data in SDTM. These variables have had various interpretations on QRS CRFs and were used
 25|           to represent a multitude of evaluator information about QRS instruments. This has made it more difficult for users of SDTM QRS data to interpret this
 26|           data and more difficult to pool data for analyses. If needed, supplemental qualifiers may be used to represent this data. Updated information on a
 27|           proposed solution to this issue will be posted on the CDISC QRS webpage (https://www.cdisc.org/standards/foundational/qrs).
 28|      9.   All standard QRS supplement development is coordinated with the CDISC SDS QRS Subteam as the governing body. The process involves drafting the
 29|           controlled terminology and defining instrument-specific standardized values for qualifier, timing, and result variables to populate the SDTMIG FT, QS,
 30|           and RS domains. These supplements are developed based on user demand and therapeutic area standards development needs. Sponsors should always
 31|           consult the CDISC website to review the terminology and supplements prior to modeling any QRS instrument.
 32|           a.   Sponsors may participate and/or request the development of additional QRS supplements and terminology through the CDISC SDS QRS subteam
~~~~

KB 现文: `knowledge_base/domains/FT/assumptions.md:71-73` (来源: fuzzy locate (score 0.983)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  71| 8. --EVAL and --EVALID must not be used to model QRS data in SDTM. These variables have had various interpretations on QRS CRFs and were used to represent a multitude of evaluator information about QRS instruments. This has made it more difficult for users of SDTM QRS data to interpret this data and more difficult to pool data for analyses. If needed, supplemental qualifiers may be used to represent this data. Updated information on a proposed solution to this issue will be posted on the CDISC QRS webpage (https://www.cdisc.org/standards/foundational/qrs).
  72| 
  73| 9. All standard QRS supplement development is coordinated with the CDISC SDS QRS Subteam as the governing body. The process involves drafting the controlled terminology and defining instrument-specific standardized values for qualifier, timing, and result variables to populate the SDTMIG FT, QS, and RS domains. These supplements are developed based on user demand and therapeutic area standards development needs. Sponsors should always consult the CDISC website to review the terminology and supplements prior to modeling any QRS instrument.
~~~~

### E71. `ig34_p0339_a001` — ae:S1R1_ATOM_ERR

- PDF 页 339 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.2 Clinical Classifications Use Case`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RS_audit.md:15 (页级行; 该批以范围/页号记这组原子)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Any identifiers, timing variables, or findings general observation class qualifiers may be added to any QRS domain. In general, identifiers should be considered generated observation class qualifiers that are generally not used: --POS, --BODYSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STRNC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0339.txt` 第 1-4 行 (自动定位, 词覆盖 0.881; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  1|                   ii. Sponsors should always consult the published QRS supplements for guidance on submitting derived information in SDTMIG-based domains.
  2|      10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would
  3|          generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STRNC, --NRIND, --XFN, --LOINC, --SPEC, --
  4|          SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.
  5| RS – Examples - Clinical Classifications
~~~~

KB 现文: `knowledge_base/domains/FT/assumptions.md:73-78` (来源: fuzzy locate (score 0.905)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  73| 9. All standard QRS supplement development is coordinated with the CDISC SDS QRS Subteam as the governing body. The process involves drafting the controlled terminology and defining instrument-specific standardized values for qualifier, timing, and result variables to populate the SDTMIG FT, QS, and RS domains. These supplements are developed based on user demand and therapeutic area standards development needs. Sponsors should always consult the CDISC website to review the terminology and supplements prior to modeling any QRS instrument.
  74|    a. Sponsors may participate and/or request the development of additional QRS supplements and terminology through the CDISC SDS QRS subteam and the Controlled Terminology QRS subteam.
  75|       i. Once generated, the QRS supplement is posted on the CDISC website (https://www.cdisc.org/standards/foundational/qrs).
  76|       ii. Sponsors should always consult the published QRS supplements for guidance on submitting derived information in SDTMIG-based domains.
  77| 
  78| 10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.
~~~~

### E72. `ig34_p0342_a004` — ae:S1R1_ATOM_ERR

- PDF 页 342 · 原子类型 TABLE_HEADER · 所在节 `SC – Examples`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: 原子表头 SCORESU; PDF p342 与 KB 均 SCORRESU | errata: t3_atom_err | new_target: domains/SC/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:88`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | SCSEQ | SCTESTCD | SCTEST | SCCAT | SCORRES | SCORESU | SCSTRESC | SCSTRESN | SCSTRESU | SCMETHOD | VISITNUM | SCDTC | SCDY |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0342.txt` 第 9-9 行 (自动定位, 词覆盖 0.941; 版式以原 PDF 为准):

~~~~
  8| sc.xpt
  9| Row STUDYID DOMAIN USUBJID SCSEQ               SCTESTCD    SCTEST           SCCAT           SCORRES SCORRESU SCSTRESC SCSTRESN SCSTRESU             SCMETHOD     VISITNUM   SCDTC    SCDY
 10|                                                           Estimated      PREGNANCY-
~~~~

KB 现文: `knowledge_base/domains/SC/examples.md:32-32` (来源: fuzzy locate (score 0.941)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  32| | Row | STUDYID | DOMAIN | USUBJID | SCSEQ | SCTESTCD | SCTEST | SCCAT | SCORRES | SCORRESU | SCSTRESC | SCSTRESN | SCSTRESU | SCMETHOD | VISITNUM | SCDTC | SCDY |
~~~~

### E73. `ig34_p0347_a003` — ae:S1R1_ATOM_ERR

- PDF 页 347 · 原子类型 SENTENCE · 所在节 `TU – Assumptions`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-TU audit: verbatim 'TULORRES' 为抽取错, PDF 文本层 TUORRES; KB 与 PDF 一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-TU_audit.md:21`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
TUTESTCD/TUTEST values for this domain are published as Controlled Terminology. For some TUTESTCD/TUTEST values, CDISC CT includes codelists for use with TULORRES.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0347.txt` 第 13-14 行 (自动定位, 词覆盖 0.947; 版式以原 PDF 为准):

~~~~
 12|      dataset link.
 13|      TUTESTCD/TUTEST values for this domain are published as Controlled Terminology. For some
 14|      TUTESTCD/TUTEST values, CDISC CT includes codelists for use with TUORRES. The associations
 15|      between the test values and results are in the Oncology codetable, which, along with the CT Rules for
~~~~

KB 现文: `knowledge_base/domains/TU/assumptions.md:34-34` (来源: fuzzy locate (score 0.947)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  34|     TUTESTCD/TUTEST values for this domain are published as Controlled Terminology. For some TUTESTCD/TUTEST values, CDISC CT includes codelists for use with TUORRES. The associations between the test values and results are in the Oncology codetable, which, along with the CT Rules for Oncology, is available at https://www.cdisc.org/standards/terminology/controlled-terminology. During the course of a trial, a tumor/lesion might split into one or more distinct tumors/lesions, or 2 or more tumors/lesions might merge to form a single tumor/lesion. The following example shows the preferred approach for representing split lesions in TU. However, the approach depends on how the data for split and merged tumors/lesions are captured. The preferred approach requires the measurements of each distinct tumor/lesion to be captured individually.
~~~~

### E74. `ig34_p0348_a010` — ae:S1R1_ATOM_ERR

- PDF 页 348 · 原子类型 LIST_ITEM · 所在节 `TU – Assumptions`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-TU audit: verbatim 'TUTEST' 为抽取错, PDF 文本层 TUTESTs; KB 与 PDF 一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-TU_audit.md:17`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
9. If indicator questions for specific types of tumor or lesions are collected (e.g., Does the subject have target tumors? Does the subject have any non-targets? Did the subject have metastatic disease at screening?), then these TUTEST will be included in TU. If indicator questions are not collected, do not introduce them into TU.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0348.txt` 第 38-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37|      terminology. Note: TUEVAL must also be populated when TUEVALID is populated.
 38| 9.   If indicator questions for specific types of tumor or lesions are collected (e.g., Does the subject have target
 39|      tumors? Does the subject have any non-targets? Did the subject have metastatic disease at screening?), then
 40|      these TUTESTs will be included in TU. If indicator questions are not collected, do not introduce them into
 41|      TU.
 42|      This example shows indicator TUTESTs for a subject with non-target lesions only.
 43|      TULNKID            TUTESTCD           TUTEST                 TUORRES       TULOC             TUMETHOD
 44|                         NTIND              Non-Target Indicator   Y                               CT SCAN
~~~~

KB 现文: `knowledge_base/domains/TU/assumptions.md:76-80` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  76| 9. If indicator questions for specific types of tumor or lesions are collected (e.g., Does the subject have target tumors? Does the subject have any non-targets? Did the subject have metastatic disease at screening?), then these TUTESTs will be included in TU. If indicator questions are not collected, do not introduce them into TU.
  77| 
  78|     This example shows indicator TUTESTs for a subject with non-target lesions only.
  79| 
  80|     | TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TUMETHOD |
~~~~

### E75. `ig34_p0360_a021` — ae:S1R1_ATOM_ERR

- PDF 页 360 · 原子类型 TABLE_ROW · 所在节 `§6.3.13 VS – Examples`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-VS audit: VSDY 读空 / VSTPT 截成 BASELINE; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-VS_audit.md:43`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | ABC | VS | ABC-001-001 | 1 | SYSBP | Systolic Blood Pressure | SITTING | 154 | mmHg | 154 | 154 | mmHg | | | ARM | LEFT | | 1 | Baseline | 1 | 1999-06-19T08:45 | | BASELINE | 1 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0360.txt` 第 35-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 34| Row STUDYID DOMAIN USUBJID         VSSEQ    VSTESTCD VSTEST            VSPOS      VSORRES VSORRESU VSSTRESC VSSTRESN VSSTRESU VSSTAT               VSREASND     VSLOC        VSLAT VSLOBXFL VISITNUM VISIT    VISITDY VSDTC            VSDY VSTPT       VSTPTNUM
 35| 1   ABC     VS     ABC-001-        1        SYSBP    Systolic Blood    SITTING    154     mmHg     154      154      mmHg                                       ARM          LEFT           1        Baseline 1       1999-06-         1    BASELINE    1
 36|                    001                               Pressure                                                                                                                                                         19T08:45              1
 37| 2   ABC     VS     ABC-001-        2        SYSBP    Systolic Blood    SITTING    152      mmHg        152         152        mmHg                              ARM          LEFT  Y        1        Baseline 1       1999-06-         1    BASELINE    2
~~~~

KB 现文: `knowledge_base/domains/VS/examples.md:17-17` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  17| | 1 | ABC | VS | ABC-001-001 | 1 | SYSBP | Systolic Blood Pressure | SITTING | 154 | mmHg | 154 | 154 | mmHg | | | ARM | LEFT | | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE 1 | 1 |
~~~~

### E76. `ig34_p0360_a022` — ae:S1R1_ATOM_ERR

- PDF 页 360 · 原子类型 TABLE_ROW · 所在节 `§6.3.13 VS – Examples`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-VS audit: VSDY 读空 / VSTPT 截成 BASELINE; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-VS_audit.md:43`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC | VS | ABC-001-001 | 2 | SYSBP | Systolic Blood Pressure | SITTING | 152 | mmHg | 152 | 152 | mmHg | | | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | | BASELINE | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0360.txt` 第 37-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36|                    001                               Pressure                                                                                                                                                         19T08:45              1
 37| 2   ABC     VS     ABC-001-        2        SYSBP    Systolic Blood    SITTING    152      mmHg        152         152        mmHg                              ARM          LEFT  Y        1        Baseline 1       1999-06-         1    BASELINE    2
 38|                    001                               Pressure                                                                                                                                                         19T09:00              2
 39| 3   ABC     VS     ABC-001-        3        DIABP    Diastolic Blood   SITTING    44       mmHg        44          44         mmHg                              ARM          LEFT           1        Baseline 1       1999-06-         1    BASELINE    1
~~~~

KB 现文: `knowledge_base/domains/VS/examples.md:18-18` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  18| | 2 | ABC | VS | ABC-001-001 | 2 | SYSBP | Systolic Blood Pressure | SITTING | 152 | mmHg | 152 | 152 | mmHg | | | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE 2 | 2 |
~~~~

### E77. `ig34_p0360_a023` — ae:S1R1_ATOM_ERR

- PDF 页 360 · 原子类型 TABLE_ROW · 所在节 `§6.3.13 VS – Examples`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-VS audit: VSDY 读空 / VSTPT 截成 BASELINE; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-VS_audit.md:43`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | ABC | VS | ABC-001-001 | 3 | DIABP | Diastolic Blood Pressure | SITTING | 44 | mmHg | 44 | 44 | mmHg | | | ARM | LEFT | | 1 | Baseline | 1 | 1999-06-19T08:45 | | BASELINE | 1 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0360.txt` 第 39-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38|                    001                               Pressure                                                                                                                                                         19T09:00              2
 39| 3   ABC     VS     ABC-001-        3        DIABP    Diastolic Blood   SITTING    44       mmHg        44          44         mmHg                              ARM          LEFT           1        Baseline 1       1999-06-         1    BASELINE    1
 40|                    001                               Pressure                                                                                                                                                         19T08:45              1
 41| 4   ABC     VS     ABC-001-        4        DIABP    Diastolic Blood   SITTING    48       mmHg        48          48         mmHg                              ARM          LEFT  Y        1        Baseline 1       1999-06-         1    BASELINE    2
~~~~

KB 现文: `knowledge_base/domains/VS/examples.md:19-19` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  19| | 3 | ABC | VS | ABC-001-001 | 3 | DIABP | Diastolic Blood Pressure | SITTING | 44 | mmHg | 44 | 44 | mmHg | | | ARM | LEFT | | 1 | Baseline | 1 | 1999-06-19T08:45 | 1 | BASELINE 1 | 1 |
~~~~

### E78. `ig34_p0360_a024` — ae:S1R1_ATOM_ERR

- PDF 页 360 · 原子类型 TABLE_ROW · 所在节 `§6.3.13 VS – Examples`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-VS audit: VSDY 读空 / VSTPT 截成 BASELINE; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-VS_audit.md:43`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | ABC | VS | ABC-001-001 | 4 | DIABP | Diastolic Blood Pressure | SITTING | 48 | mmHg | 48 | 48 | mmHg | | | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | | BASELINE | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0360.txt` 第 41-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 40|                    001                               Pressure                                                                                                                                                         19T08:45              1
 41| 4   ABC     VS     ABC-001-        4        DIABP    Diastolic Blood   SITTING    48       mmHg        48          48         mmHg                              ARM          LEFT  Y        1        Baseline 1       1999-06-         1    BASELINE    2
 42|                    001                               Pressure                                                                                                                                                         19T09:00              2
 43| 
~~~~

KB 现文: `knowledge_base/domains/VS/examples.md:20-20` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  20| | 4 | ABC | VS | ABC-001-001 | 4 | DIABP | Diastolic Blood Pressure | SITTING | 48 | mmHg | 48 | 48 | mmHg | | | ARM | LEFT | Y | 1 | Baseline | 1 | 1999-06-19T09:00 | 1 | BASELINE 2 | 2 |
~~~~

### E79. `ig34_p0361_a016` — ae:S1R1_ATOM_ERR

- PDF 页 361 · 原子类型 SENTENCE · 所在节 `§6.4.1 When to Use Findings About Events or Interventions`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-FA audit: 原子抽错; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-FA_audit.md:36`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
A finding that is about part of an event, rather than the event as a whole, meets this criterion for the use of FA. An assessment of an event that is not about the whole of an event may be a "snapshot," an assessment at a point in time, or a "slice," an assessment over a period of time (i.e., evaluation interval) during the event. In Section 6.4.4., Findings About Events or Interventions, Example 1 shows snapshot assessments at 3 points in time. The timing variables used to represent a snapshot assessment generally include FADTC, along with visit and time point variables as applicable, but not FAEVLINT or FAEVINTX. FA Example 5 shows assessments over 24-hour slices of the event. Slice assessments use an evaluation interval, the timing variables used would generally include FADTC and either FAEVLINT or FAEVINTX.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0361.txt` 第 36-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35| may be used to represent data about severity (or other properties) of the adverse event that have timing different from the medical condition as a whole.
 36| A finding that is about part of an event, rather than the event as a whole, meets this criterion for the use of FA. An assessment of an event that is not about the whole of an event may be a "snapshot," an assessment at
 37| a point in time, or a "slice," an assessment over a period of time (i.e., evaluation interval) during the event. In Section 6.4.4., Findings About Events or Interventions, Example 1 shows snapshot assessments at 3
 38| points in time. The timing variables used to represent a snapshot assessment generally include FADTC, along with visit and time point variables as applicable, but not FAEVLINT or FAEVINTX. FA Example 5
 39| shows assessments over 24-hour slices of the event. Slice assessments use an evaluation interval, so the timing variables used would generally include FADTC and either FAEVLINT or FAEVINTX.
 40| Repeated assessments of disease or treatment-related symptoms, particularly symptoms that are likely to be intermittent, generally produce results that apply to only part of an event; these are represented as findings
~~~~

KB 现文: `knowledge_base/domains/FA/assumptions.md:15-15` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  15| A finding that is about part of an event, rather than the event as a whole, meets this criterion for the use of FA. An assessment of an event that is not about the whole of an event may be a "snapshot," an assessment at a point in time, or a "slice," an assessment over a period of time (i.e., evaluation interval) during the event. In Section 6.4.4, Findings About Events or Interventions, Example 1 shows snapshot assessments at 3 points in time. The timing variables used to represent a snapshot assessment generally include FADTC, along with visit and time point variables as applicable, but not FAEVLINT or FAEVINTX. FA Example 5 shows assessments over 24-hour slices of the event. Slice assessments use an evaluation interval, so the timing variables used would generally include FADTC and either FAEVLINT or FAEVINTX.
~~~~

### E80. `ig34_p0373_a021` — ae:S1R1_ATOM_ERR

- PDF 页 373 · 原子类型 TABLE_HEADER · 所在节 `FA – Examples`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-FA audit: 原子抽错; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-FA_audit.md:58`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FATESTCD | FATEST | FAOBJ | FACAT | FAORRES | FAORRESU | FASTRESC | FASTRESN | FASTRESU | FASTAT | VISITNUM | VISIT | FADTC | FAEVINTX |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0373.txt` 第 18-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| criterion 2 data (“about” an event or intervention), having qualifiers that can be represented in Findings variables (e.g., units, method).
 18| This SDTM example represents data from 2 visits for 1 subject. FAEVINTX indicates that assessments were for the previous 24 hours.
 19| Rows 1-4:        Show the results for the vomiting tests at visit 1. Because the number of episodes was recorded as ">10", this is represented in FASTRESC but
 20|                  not in FASTRESN.
 21| Rows 5-7:        Show the results for the diarrhea tests at visit 1.
 22| Rows 8-10:       Show the results for the nausea tests at visit 1.
 23| Row 11:          Shows that vomiting did not occur in the 24 hours before visit 2; thus, volume, number of episodes, and severity were not applicable.
 24| Rows 12-14: Show the results for the diarrhea tests at visit 2.
 25| Row 15:          Indicates that the occurrence of nausea was not assessed at visit 2.
 26| face.xpt
 27| Row STUDYID DOMAIN USUBJID       FASEQ FATESTCD FATEST                  FAOBJ FACAT         FAORRES      FAORRESU FASTRESC    FASTRESN FASTRESU FASTAT     VISITNUM VISIT   FADTC   FAEVLINT
 28| 1   XYZ     FA     XYZ-701-      1     OCCUR    Occurrence              Vomiting GERD       Y                     Y                                        1        VISIT   2006-   -PT24H
~~~~

KB 现文: `knowledge_base/domains/FA/examples.md:239-239` (来源: fuzzy locate (score 0.947)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 239| | Row | STUDYID | DOMAIN | USUBJID | FASEQ | FATESTCD | FATEST | FAOBJ | FACAT | FAORRES | FAORRESU | FASTRESC | FASTRESN | FASTRESU | FASTAT | VISITNUM | VISIT | FADTC | FAEVLINT |
~~~~

### E81. `ig34_p0374_a011` — ae:S1R1_ATOM_ERR

- PDF 页 374 · 原子类型 TABLE_HEADER · 所在节 `FA – Examples`
- triage 类 **REWRITE_OK** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-FA: 原子把 AE ID 与合并格抽在同一行, 与渲染不符; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-FA.md:119`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| AE ID | Adverse Event | Start Date | End Date | At each visit, record the maximum severity of the adverse event since the last visit. |  |  |  |  |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0374.txt` 第 21-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20| A paper CRF to be updated at each visit might look like this:
 21|                                                 At each visit, record the maximum severity of the adverse event since the last visit.
 22| AE ID Adverse Event Start Date End Date Visit 2                         Visit 3        Visit 4          Visit 5        Visit 6
 23|                                                 ○ Mild                  ○ Mild         ○ Mild           ○ Mild         ○ Mild
~~~~

KB 现文: `knowledge_base/domains/FA/examples.md:263-265` (来源: near triage kb_loc knowledge_base/domains/FA/examples.md:264 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 263| | | | | | At each visit, record the maximum severity of the adverse event since the last visit. | | | | |
 264| |---|---|---|---|---|---|---|---|---|
 265| | AE ID | Adverse Event | Start Date | End Date | Visit 2 | Visit 3 | Visit 4 | Visit 5 | Visit 6 |
~~~~

### E82. `ig34_p0396_a009` — ae:S1R1_ATOM_ERR

- PDF 页 396 · 原子类型 SENTENCE · 所在节 `§7.2.1 Trial Arms (TA) – Example 4`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T2 global fp audit R1: 原子 `represents`; PDF p396 为 `represented this rule`, KB 同 (B-TA #31) | errata: t3_atom_err | in_atom_err=False in_remap=False; 出处 `.work/10_tier_b_repair/evidence/t2_fp_expected_regressions.md:53`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The TA dataset for this example trial requires the use of the TATRANS variable to represent the "repeat until disease progression" feature (the green "skip forward" arrow represents this rule in the diagrams).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0396.txt` 第 19-20 行 (自动定位, 词覆盖 0.963; 版式以原 PDF 为准):

~~~~
 18| 
 19| The TA dataset for this example trial requires the use of the TATRANS variable to represent the "repeat until
 20| disease progression" feature (the green "skip forward" arrow represented this rule in the diagrams). In the TA
 21| dataset, TATRANS is populated for each element with a green arrow in the diagram. In other words, if there is a
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:672-672` (来源: fuzzy locate (score 0.963)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 672| The TA dataset for this example trial requires the use of the TATRANS variable to represent the "repeat until disease progression" feature (the green "skip forward" arrow represented this rule in the diagrams). In the TA dataset, TATRANS is populated for each element with a green arrow in the diagram. In other words, if there is a possibility that a subject will, at the end of this element, skip forward to a later part of the arm, then TATRANS is populated with the rule describing the conditions under which a subject will go to a later element. If the subject always goes to the next element in the arm (see Example Trials 1-3), then TATRANS is null. The TA dataset presented below corresponds to the trial design matrix.
~~~~

### E83. `ig34_p0419_a004` — ae:S1R1_ATOM_ERR

- PDF 页 419 · 原子类型 LIST_ITEM · 所在节 `§7.4.2 Trial Summary (TS) – Assumptions`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-TS writer: 原子抽取错, KB 正确; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-TS.md:86`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
13. TS does not contain subject-level data, so there is no restriction analogous to the requirement in subject-level datasets that the blocks bound by TSGRPID are within a dataset. TSGRPID can be used to tie together any block of records in the dataset. TSGRPID is most likely to be used when the TS dataset includes multiple records for the same parameter.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0419.txt` 第 11-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 10| 
 11| 13. TS does not contain subject-level data, so there is no restriction analogous to the requirement in subject-
 12|     level datasets that the blocks bound by TSGRPID are within a subject. TSGRPID can be used to tie
 13|     together any block of records in the dataset. TSGRPID is most likely to be used when the TS dataset
 14|     includes multiple records for the same parameter.
 15|     For example, if a trial compared administration of a total daily dose given once a day to that dose split over
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:41-41` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  41| 13. TS does not contain subject-level data, so there is no restriction analogous to the requirement in subject-level datasets that the blocks bound by TSGRPID are within a subject. TSGRPID can be used to tie together any block of records in the dataset. TSGRPID is most likely to be used when the TS dataset includes multiple records for the same parameter.
~~~~

