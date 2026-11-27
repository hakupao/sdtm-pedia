# T4.1 第二轮补检包 b2 — TYPO_SIB2 (20 条; 编号 S21-S40)

> 由 `scripts/t4/t4_round2b_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号前缀 S.

### S21. `ig34_p0213_a014` — r2:TYPO_SIB2

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 7 | ABC-123 | CP | ABCD-001-001 | 7 | 2 | MONO | Monocytes |  |  |  | CD14+ | FSC+SSC+CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 394 | 10^6/L | 394 | 10^6/L | 394 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 34-35 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 33|                                                                 NonProlif
 34| 7     ABC-123   CP       ABCD-     7       2         MONO       Monocytes                                             CD14+                   MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     394       10^6/L     394        10^6/L     394        QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 35|                          001-001                                                                                                                                                            CD SUBSETS                                                                        CONCENTRATION            CYTOMETRY     16T08:00
 36| 8     ABC-123   CP       ABCD-     8       2         MNS        Mono Sub      CDxx+CDyy-                              CD14+CDxx+CDyy-         MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     366       10^6/L     366        10^6/L     366        QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:135-135` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 135| | 7 | ABC-123 | CP | ABCD-001-001 | 7 | 2 | MONO | Monocytes | | | | CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 394 | 10^6/L | 394 | 10^6/L | 394 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

### S22. `ig34_p0213_a017` — r2:TYPO_SIB2

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 10 | ABC-123 | CP | ABCD-001-001 | 10 | 2 | MNSMN | Mono Sub/Mono | CDxx+CDyy- |  |  | CD14+CDxx+CDyy-/CD14+ | CD14+CDxx+CDyy-/CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 93.00 | % | 93.00 | % | 93.00 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 40-41 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39|                          001-001                                                                                                                                                            CD SUBSETS                                                                        CONCENTRATION            CYTOMETRY     16T08:00
 40| 10    ABC-123   CP       ABCD-     10      2         MNSMN      Mono          CDxx+CDyy-                              CD14+CDxx+CDyy-         MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     93.00     %          93.00      %          93.00      QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 41|                          001-001                                Sub/Mono                                              /CD14+                                                                CD SUBSETS                                                                        FRACTION                 CYTOMETRY     16T08:00
 42| 11    ABC-123   CP       ABCD-     11      2         MNSMN      Mono          CDxx-CDyy+                              CD14+CDxx-              MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     5.00      %          5.00       %          5.00       QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:138-138` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 138| | 10 | ABC-123 | CP | ABCD-001-001 | 10 | 2 | MNSMN | Mono Sub/Mono | CDxx+CDyy- | | | CD14+CDxx+CDyy-/CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 93.00 | % | 93.00 | % | 93.00 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

### S23. `ig34_p0213_a018` — r2:TYPO_SIB2

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 11 | ABC-123 | CP | ABCD-001-001 | 11 | 2 | MNSMN | Mono Sub/Mono | CDxx-CDyy+ |  |  | CD14+CDxx-CDyy-/CD14+ | CD14+CDxx-CDyy-/CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 5.00 | % | 5.00 | % | 5.00 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 41-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 40| 10    ABC-123   CP       ABCD-     10      2         MNSMN      Mono          CDxx+CDyy-                              CD14+CDxx+CDyy-         MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     93.00     %          93.00      %          93.00      QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 41|                          001-001                                Sub/Mono                                              /CD14+                                                                CD SUBSETS                                                                        FRACTION                 CYTOMETRY     16T08:00
 42| 11    ABC-123   CP       ABCD-     11      2         MNSMN      Mono          CDxx-CDyy+                              CD14+CDxx-              MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     5.00      %          5.00       %          5.00       QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 43|                          001-001                                Sub/Mono                                              CDyy+/CD14+                                                           CD SUBSETS                                                                        FRACTION                 CYTOMETRY     16T08:00
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:139-139` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 139| | 11 | ABC-123 | CP | ABCD-001-001 | 11 | 2 | MNSMN | Mono Sub/Mono | CDxx-CDyy+ | | | CD14+CDxx-CDyy+/CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 5.00 | % | 5.00 | % | 5.00 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

### S24. `ig34_p0256_a007` — r2:TYPO_SIB2

- PDF 页 256 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.7.2 Microbiology Susceptibility (MS)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-MS T-5`: PDF 写 "It should only populated" → KB 写 "should only be populated" (处理: KB 写正确值; 依据: 缺动词; KB `knowledge_base/domains/MS/assumptions.md:27`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
4. NHOID is a sponsor-defined, intuitive name of the non-host organism being tested. It should only populated with values representing what is known about the identity of the organism before the results of the test are determined. It should therefore never be used as a qualifier of result.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0256.txt` 第 13-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12|                  LNKID.
 13|      4.     NHOID is a sponsor-defined, intuitive name of the non-host organism being tested. It should only populated with values representing what is known
 14|             about the identity of the organism before the results of the test are determined. It should therefore never be used as a qualifier of result.
 15|      5.     Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MS domain, but the following variables would
~~~~

KB 现文: `knowledge_base/domains/MS/assumptions.md:27-27` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  27| 4. NHOID is a sponsor-defined, intuitive name of the non-host organism being tested. It should only be populated with values representing what is known about the identity of the organism before the results of the test are determined. It should therefore never be used as a qualifier of result.
~~~~

### S25. `ig34_p0257_a014` — r2:TYPO_SIB2

- PDF 页 257 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-MS T-1`: PDF 写 "Ex1 r9 MSSTRESC 空" → KB 写 "25" (处理: KB 写正确值; 依据: 同行 MSORRES/MSSTRESN 25; r7 同式; KB `knowledge_base/domains/MS/examples.md:31`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
7 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 3 | 7 | SPEC01 | 2 | DIAZOINH | Diameter of the Zone of Inhibition | Sponsor Drug | | | 23 | mm | 23 | 23 | mm | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-26T08:00
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0257.txt` 第 24-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23|                    002             FAECALIS                                                           Susceptibility                                                                                             XYZ         DILUTION         19T08:00
 24| 7   ABC     MS     ABC-001-        ENTEROCOCCUS          3            7     SPEC01  2        DIAZOINH Diameter of the      Sponsor                      23            mm       23            23         mm       LOCAL LAB   DISK DIFFUSION   2005-06-
 25|                    002             FAECALIS                                                           Zone of Inhibition   Drug                                                                                  XYZ                          26T08:00
 26| 8   ABC     MS     ABC-001-        ENTEROCOCCUS          3            8     SPEC01  2        MICROSUS Microbial            Sponsor                      SUSCEPTIBLE            SUSCEPTIBLE                       LOCAL LAB   DISK DIFFUSION   2005-06-
~~~~

KB 现文: `knowledge_base/domains/MS/examples.md:29` (来源: live valid_hits):

~~~~
  29| | 7 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 3 | 7 | SPEC01 | 2 | DIAZOINH | Diameter of the Zone of Inhibition | Sponsor Drug | | | 23 | mm | 23 | 23 | mm | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-26T08:00 |
~~~~

### S26. `ig34_p0262_a007` — r2:TYPO_SIB2

- PDF 页 262 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-MB T-1`: PDF 写 "Ex3 suppmb Row 列 1,2,3,4,7,8" → KB 写 "5, 6" (处理: KB 写正确值; 依据: Row 跳号, 行内容按 PDF; KB `knowledge_base/domains/MB/examples.md:204`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
4 | ABC | MB | ABC-01-101 | | 4 | 2 | 1 | 100.3 | MTB | Mycobacterium tuberculosis | DETECTION | PRESENT | | Ord | PRESENT | | | STOMACH | | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0262.txt` 第 11-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 10|                          101                                                                     Tuberculosis Complex                                                                                                                      AMPLIFICATION TEST              1       17T06:00
 11| 4     ABC       MB       ABC-01-             4        2         1          100.3     MTB         Mycobacterium          DETECTION    PRESENT                   Ord        PRESENT                             STOMACH                      MICROBIAL CULTURE,   1          WEEK    2011-01-
 12|                          101                                                                     tuberculosis                                                                                                                              SOLID                           1       17T06:00
 13| 5     ABC       MB       ABC-01-             5        2         1          100.3     MTB         Mycobacterium          COLONY       147         CFU           Qn         14700      14700        CFU/mL      STOMACH                      MICROBIAL CULTURE,   1          WEEK    2011-01-
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:192` (来源: live valid_hits):

~~~~
 192| | 4 | ABC | MB | ABC-01-101 | | 4 | 2 | 1 | 100.3 | MTB | Mycobacterium tuberculosis | DETECTION | PRESENT | | Ord | PRESENT | | | STOMACH | | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00 |
~~~~

### S27. `ig34_p0262_a009` — r2:TYPO_SIB2

- PDF 页 262 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-MB T-1`: PDF 写 "Ex3 suppmb Row 列 1,2,3,4,7,8" → KB 写 "5, 6" (处理: KB 写正确值; 依据: Row 跳号, 行内容按 PDF; KB `knowledge_base/domains/MB/examples.md:204`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
6 | ABC | MB | ABC-01-101 | | 8 | 2 | | 100.3 | MTB | Mycobacterium tuberculosis | COLONY COUNT | 2+ | | Ord | 2+ | | | STOMACH | | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0262.txt` 第 15-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14|                          101                                                                     tuberculosis           COUNT                                                                                                              SOLID                           1       17T06:00
 15| 6     ABC       MB       ABC-01-             6        2         1          100.3     MTB         Mycobacterium          COLONY       2+                        Ord        2+                                  STOMACH                      MICROBIAL CULTURE,   1          WEEK    2011-01-
 16|                          101                                                                     tuberculosis           COUNT                                                                                                              SOLID                           1       17T06:00
 17| 
 18| 
 19| 
 20| suppmb.xpt
 21| Row    STUDYID       RDOMAIN   USUBJID           IDVAR     IDVARVAL    QNAM            QLABEL                                QVAL                                                                                                  QORIG
 22| 1      ABC           MB        ABC-01-101        MBSEQ     2           MBQSCAL         Quantification Scale                  Smear Quantification: Centers for Disease Control Method for Carbol Fuchsin Staining (1000X)          Collected
 23| 2      ABC           MB        ABC-01-101        MBSEQ     3           MBMICERT        Microbial Identification Certainty    DEFINITIVE                                                                                            Collected
 24| 3      ABC           MB        ABC-01-101        MBSEQ     4           MBMICERT        Microbial Identification Certainty    PRESUMPTIVE                                                                                           Collected
 25| 4      ABC           MB        ABC-01-101        MBREFID   100.3       MBMEDTYP        Medium Type                           MIDDLEBROOK 7H10 AGAR                                                                                 Collected
 26| 7      ABC           MB        ABC-01-101        MBSEQ     6           MBQSCAL         Quantification Scale                  Solid Media Result: Centers for Disease Control (CDC) Quantification Scale                            Collected
 27| 8      ABC           MB        ABC-01-101        MBSEQ     5           MBDILFCT        Dilution Factor                       10^-2                                                                                                 Collected
 28| 
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:194-194` (来源: fuzzy locate (score 0.958)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 194| | 6 | ABC | MB | ABC-01-101 | | 6 | 2 | 1 | 100.3 | MTB | Mycobacterium tuberculosis | COLONY COUNT | 2+ | | Ord | 2+ | | | STOMACH | | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00 |
~~~~

### S28. `ig34_p0279_a035` — r2:TYPO_SIB2

- PDF 页 279 · 原子类型 SENTENCE · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-PCPP T-8b`: PDF 写 "Ex3 引言 DYDRGX_HALF" → KB 写 "DY1DRGX_HALF (同页 relrec)" (处理: KB 写正确值; 依据: 应为 DY1DRGX_HALF, 不单值; KB `knowledge_base/domains/PC/examples.md:278`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example uses --GRPID values in the PCGRPID (Example 2) and PPGRPID (Example 2) columns. Note that for the 2 excluded PC records, PCGRPID = "EXCLUDE"; for other PC records, PCGRPID = "DY1_DRGX".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0279.txt` 第 38-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37| not used for any pharmacokinetic parameters.
 38| This example uses --GRPID values in the PCGRPID (Example 2) and PPGRPID (Example 2) columns. Note that
 39| for the 2 excluded PC records, PCGRPID = "EXCLUDE"; for other PC records, PCGRPID = "DY1_DRGX".
 40| All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### S29. `ig34_p0281_a046` — r2:TYPO_SIB2

- PDF 页 281 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 3`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-SPC2 PCPP T-11`: PDF 写 ""1 through "7" (引号错位)" → KB 写 ""1" through "7"" (处理: KB 写正确值; 依据: p278 Ex1 Method D 同型句; KB `knowledge_base/domains/PC/examples.md:250`)
- 登记 `S-SPC2 N-1`: PDF 写 "PP records with PCSEQ values" → KB 写 "PC records with PCSEQ (:299/:300; span 另匹配本就正确的 :438-:441)" (处理: KB 写正确值; 依据: 应为 PC records (PCSEQ 属 PC), 照录; KB `knowledge_base/domains/PC/examples.md:299`)
- 登记 `S-SPC2 N-2`: PDF 写 "PP records with PGRPID values" → KB 写 "all PC records with PCGRPID value(s) (:333/:334; 同页 relrec RDOMAIN=PC, IDVAR=PCGRPID)" (处理: KB 写正确值; 依据: 应为 PPGRPID, 照录; KB `knowledge_base/domains/PC/examples.md:333`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-17:	The relationship with RELID "1" includes PC records with PCSEQ values of "1" through "12" and PP records with PPSEQ values "1" through "3" and "6" and "7".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0281.txt` 第 54-55 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 53| Method D (One to One, Using PCSEQ and PPSEQ)
 54| Rows 1-17:       The relationship with RELID "1" includes PC records with PCSEQ values of "1" through "12" and
 55|                  PP records with PPSEQ values "1" through "3" and "6" and "7".
 56| Rows 18-29: The relationship with RELID "2" includes PC records with PCSEQ values of "1" through "7" and
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### S30. `ig34_p0296_a017` — r2:TYPO_SIB2

- PDF 页 296 · 原子类型 LIST_ITEM · 所在节 `§6.3.7.4 Nervous System Findings (NV)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-NV T-1`: PDF 写 "an fluorodeoxyglucose" → KB 写 "a fluorodeoxyglucose" (处理: KB 写正确值; 依据: 冠词; KB `knowledge_base/domains/NV/examples.md:11`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-2:   Show the SUVR findings based on a PET/CT scan for a subject.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0296.txt` 第 26-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25| and therefore to which biomarker the findings pertain. NVDTC corresponds to the date of the PET or PET/CT procedure from which these results were obtained.
 26| Rows 1-2:       Show the SUVR findings based on a PET/CT scan for a subject.
 27| Rows 3-4:       Show the SUVR findings based on a PET/CT scan for a subject.
~~~~

KB 现文: `knowledge_base/domains/NV/examples.md:9` (来源: live valid_hits):

~~~~
   9| **Rows 1-2:** Show the SUVR findings based on a PET/CT scan for a subject.
~~~~

### S31. `ig34_p0296_a018` — r2:TYPO_SIB2

- PDF 页 296 · 原子类型 LIST_ITEM · 所在节 `§6.3.7.4 Nervous System Findings (NV)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-NV T-1`: PDF 写 "an fluorodeoxyglucose" → KB 写 "a fluorodeoxyglucose" (处理: KB 写正确值; 依据: 冠词; KB `knowledge_base/domains/NV/examples.md:11`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 3-4:   Show the SUVR findings based on a PET/CT scan for a subject.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0296.txt` 第 27-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26| Rows 1-2:       Show the SUVR findings based on a PET/CT scan for a subject.
 27| Rows 3-4:       Show the SUVR findings based on a PET/CT scan for a subject.
 28| Rows 5-6:       Show the SUVR findings based on an fluorodeoxyglucose (FDG)-PET scan for a subject.
~~~~

KB 现文: `knowledge_base/domains/NV/examples.md:10` (来源: live valid_hits):

~~~~
  10| **Rows 3-4:** Show the SUVR findings based on a PET/CT scan for a subject.
~~~~

### S32. `ig34_p0297_a037` — r2:TYPO_SIB2

- PDF 页 297 · 原子类型 SENTENCE · 所在节 `§6.3.7.4 Nervous System Findings (NV)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-NV N-2`: PDF 写 "links the each" → KB 写 "links each (删 the)" (处理: KB 写正确值; 依据: PDF 语法, 照录; KB `knowledge_base/domains/NV/examples.md:63`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In addition to interpreting each VEP component as normal or abnormal, the overall test for each eye may have an [TRUNCATED_AT_PAGE_BOUNDARY]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0297.txt` 第 41-44 行 (自动定位, 词覆盖 0.87; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 40| In this example, a VEP component is considered abnormal if it falls outside of 3 standard deviations from the normative lab mean. These low and high values are stored in NVORNRLO and NVORNRHI,
 41| respectively, and the interpretation of each VEP component is represented in NVNRIND. In addition to interpreting each VEP component as normal or abnormal, the overall test for each eye may have an
 42| 
 43| 
 44| © 2021 Clinical Data Interchange Standards Consortium, Inc. All rights reserved                                                                                                                                     Page 297
 45| 2021-11-29
~~~~

KB 现文: `knowledge_base/domains/NV/examples.md:63-63` (来源: fuzzy locate (score 0.826)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  63| In this example, a VEP component is considered abnormal if it falls outside of 3 standard deviations from the normative lab mean. These low and high values are stored in NVORNRLO and NVORNRHI, respectively, and the interpretation of each VEP component is represented in NVNRIND. In addition to interpreting each VEP component as normal or abnormal, the overall test for each eye may have an interpretation. In this scenario, NVTESTCD/NVTEST should be equal to "INTP" (Interpretation) and NVORRES should represent whether the overall test in each eye is normal or abnormal. NVGRPID links each VEP component to the overall interpretation.
~~~~

### S33. `ig34_p0357_a013` — r2:TYPO_SIB2

- PDF 页 357 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-TR T-2`: PDF 写 "Ex3 r15 TRSTRESC -60" → KB 写 "-50" (处理: KB 写正确值; 依据: 同行 TRORRES/TRSTRESN -50; KB `knowledge_base/domains/TR/examples.md:84`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 14 | ABC | TR | 55555 | 14 | TARGET | A2 | | ACNSD | Absolute Change From Nadir in Sum of Diameters | -25 | mm | -25 | -25 | mm | ACE IMAGING | | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0357.txt` 第 30-33 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 29|                                                                                State                                                                           IMAGING             ASSESSOR      1
 30| 14    ABC      TR      55555    14     TARGET    A2                   ACNSD    Absolute         -25               mm       -25               -25      mm       ACE                 INDEPENDENT   RADIOLOGIST   40      WEEK 6
 31|                                                                                Change From                                                                     IMAGING             ASSESSOR      1
 32|                                                                                Nadir in Sum
 33|                                                                                of Diameters
 34| 15    ABC      TR      55555    15     TARGET    A2                   PCBSD    Percent          -50               %        -60               -50      %        ACE                 INDEPENDENT   RADIOLOGIST   40      WEEK 6
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:83` (来源: live valid_hits):

~~~~
  83| | 14 | ABC | TR | 55555 | 14 | TARGET | A2 | | ACNSD | Absolute Change From Nadir in Sum of Diameters | -25 | mm | -25 | -25 | mm | ACE IMAGING | | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
~~~~

### S34. `ig34_p0419_a005` — r2:TYPO_SIB2

- PDF 页 419 · 原子类型 SENTENCE · 所在节 `§7.4.2 Trial Summary (TS) – Assumptions`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-TS T-2`: PDF 写 "TSPARMCD = "Dose"" → KB 写 "DOSE (TSPARMCD CT C25488)" (处理: KB 写正确值; 依据: 大小写不一致; KB `knowledge_base/domains/TS/assumptions.md:43`)
- 登记 `B-TS T-3`: PDF 写 "DOSFREQ" → KB 写 "DOSFRQ (TSPARMCD CT C89081; 叙述 + 表 2 格共 3 处)" (处理: KB 写正确值; 依据: 两处互异; KB `knowledge_base/domains/TS/assumptions.md:43`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0419.txt` 第 15-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14|     includes multiple records for the same parameter.
 15|     For example, if a trial compared administration of a total daily dose given once a day to that dose split over
 16|     2 administrations, the TS dataset might include the following records. There are 2 records each for
 17|     TSPARMCD = "Dose" and TSPARMCD = "DOSFREQ". Records with the same TSGRPID are associated
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:43` (来源: live valid_hits):

~~~~
  43|     For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records. There are 2 records each for TSPARMCD = "DOSE" and TSPARMCD = "DOSFRQ". Records with the same TSGRPID are associated with each other. In this example, dose units are the same for both administration schedules, so only 1 record for DOSU is needed.
~~~~

### S35. `ig34_p0419_a007` — r2:TYPO_SIB2

- PDF 页 419 · 原子类型 SENTENCE · 所在节 `§7.4.2 Trial Summary (TS) – Assumptions`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-TS T-2`: PDF 写 "TSPARMCD = "Dose"" → KB 写 "DOSE (TSPARMCD CT C25488)" (处理: KB 写正确值; 依据: 大小写不一致; KB `knowledge_base/domains/TS/assumptions.md:43`)
- 登记 `B-TS T-3`: PDF 写 "DOSFREQ" → KB 写 "DOSFRQ (TSPARMCD CT C89081; 叙述 + 表 2 格共 3 处)" (处理: KB 写正确值; 依据: 两处互异; KB `knowledge_base/domains/TS/assumptions.md:43`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Records with the same TSGRPID are associated with each other.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0419.txt` 第 17-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 16|     2 administrations, the TS dataset might include the following records. There are 2 records each for
 17|     TSPARMCD = "Dose" and TSPARMCD = "DOSFREQ". Records with the same TSGRPID are associated
 18|     with each other. In this example, dose units are the same for both administration schedules, so only 1 record
 19|     for DOSU is needed.
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:43` (来源: live valid_hits):

~~~~
  43|     For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records. There are 2 records each for TSPARMCD = "DOSE" and TSPARMCD = "DOSFRQ". Records with the same TSGRPID are associated with each other. In this example, dose units are the same for both administration schedules, so only 1 record for DOSU is needed.
~~~~

### S36. `ig34_p0419_a008` — r2:TYPO_SIB2

- PDF 页 419 · 原子类型 SENTENCE · 所在节 `§7.4.2 Trial Summary (TS) – Assumptions`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-TS T-2`: PDF 写 "TSPARMCD = "Dose"" → KB 写 "DOSE (TSPARMCD CT C25488)" (处理: KB 写正确值; 依据: 大小写不一致; KB `knowledge_base/domains/TS/assumptions.md:43`)
- 登记 `B-TS T-3`: PDF 写 "DOSFREQ" → KB 写 "DOSFRQ (TSPARMCD CT C89081; 叙述 + 表 2 格共 3 处)" (处理: KB 写正确值; 依据: 两处互异; KB `knowledge_base/domains/TS/assumptions.md:43`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this example, dose units are the same for both administration schedules, so only 1 record for DOSU is needed.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0419.txt` 第 18-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17|     TSPARMCD = "Dose" and TSPARMCD = "DOSFREQ". Records with the same TSGRPID are associated
 18|     with each other. In this example, dose units are the same for both administration schedules, so only 1 record
 19|     for DOSU is needed.
 20|      TSSEQ                 TSGRPID               TSPARMCD               TSPARM                    TSVAL
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:43` (来源: live valid_hits):

~~~~
  43|     For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records. There are 2 records each for TSPARMCD = "DOSE" and TSPARMCD = "DOSFRQ". Records with the same TSGRPID are associated with each other. In this example, dose units are the same for both administration schedules, so only 1 record for DOSU is needed.
~~~~

### S37. `ig34_p0425_a023` — r2:TYPO_SIB2

- PDF 页 425 · 原子类型 SENTENCE · 所在节 `§7.4.2.1 Use of Null Flavor`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-TS T-6`: PDF 写 "MAXAGE case" → KB 写 "AGEMAX (TSPARMCD CT C49694)" (处理: KB 写正确值; 依据: PDF 内不一致; KB `knowledge_base/domains/TS/assumptions.md:115`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The values at levels 3 and 4 provide successively more information about the situation.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0425.txt` 第 29-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28| to be represented in the primary piece of data).
 29| The values at levels 3 and 4 provide successively more information about the situation. For example, for the
 30| MAXAGE case that provided the impetus for the creation of the TSVALNF variable, the value PINF means that
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:115` (来源: live valid_hits):

~~~~
 115| The values at levels 3 and 4 provide successively more information about the situation. For example, for the AGEMAX case that provided the impetus for the creation of the TSVALNF variable, the value PINF means that there is information about the maximum age, but it is not something that can be expressed, as in the ISO8601 quantity of time format required for populating TSVAL. The null flavor PINF provides the most complete information possible in this case (i.e., that the maximum age for the study is unbounded).
~~~~

### S38. `ig34_p0425_a025` — r2:TYPO_SIB2

- PDF 页 425 · 原子类型 SENTENCE · 所在节 `§7.4.2.1 Use of Null Flavor`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-TS T-6`: PDF 写 "MAXAGE case" → KB 写 "AGEMAX (TSPARMCD CT C49694)" (处理: KB 写正确值; 依据: PDF 内不一致; KB `knowledge_base/domains/TS/assumptions.md:115`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The null flavor PINF provides the most complete information possible in this case (i.e., that the maximum age for the study is unbounded).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0425.txt` 第 32-33 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| there is information about the maximum age, but it is not something that can be expressed, as in the ISO8601
 32| quantity of time format required for populating TSVAL. The null flavor PINF provides the most complete
 33| information possible in this case (i.e., that the maximum age for the study is unbounded).
 34| 
~~~~

KB 现文: `knowledge_base/domains/TS/assumptions.md:115` (来源: live valid_hits):

~~~~
 115| The values at levels 3 and 4 provide successively more information about the situation. For example, for the AGEMAX case that provided the impetus for the creation of the TSVALNF variable, the value PINF means that there is information about the maximum age, but it is not something that can be expressed, as in the ISO8601 quantity of time format required for populating TSVAL. The null flavor PINF provides the most complete information possible in this case (i.e., that the maximum age for the study is unbounded).
~~~~

### S39. `ig34_p0433_a031` — r2:TYPO_SIB2

- PDF 页 433 · 原子类型 SENTENCE · 所在节 `§8.4.3 SUPP-- Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-SUPPQUAL T-1`: PDF 写 "llustrate" → KB 写 "illustrate" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/domains/SUPPQUAL/examples.md:5`)
- 登记 `B-ch08 T-5`: PDF 写 "标签 Example (无编号)" → KB 写 "Example 2" (处理: KB 写正确值; 依据: 前例为 Example 1; KB `knowledge_base/chapters/ch08_relationships.md:241`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The parent domain (RDOMAIN) is QS, and IDVAR is QSCAT.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0433.txt` 第 43-44 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 42| Example
 43| This example illustrates how the language used for a questionnaire might be represented. The parent domain
 44| (RDOMAIN) is QS, and IDVAR is QSCAT. QNAM holds the name of the supplemental qualifier variable being
 45| defined (QSLANG). The language recorded in QVAL applies to all of the subject’s records, where IDVAR
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:241` (来源: live valid_hits):

~~~~
 241| **Example 2:** This example illustrates how the language used for a questionnaire might be represented. The parent domain (RDOMAIN) is QS, and IDVAR is QSCAT. QNAM holds the name of the supplemental qualifier variable being defined (QSLANG). The language recorded in QVAL applies to all of the subject’s records, where IDVAR (QSCAT) equals the value specified in IDVARVAL. In this case, IDVARVAL has values for 2 questionnaires—Brief Pain Inventory (BPI) and Alzheimer's Disease Assessment Scale–Cognitive Subscale (ADAS-Cog)—for 2 separate subjects. QVAL identifies the questionnaire language version (French or German) for each subject.
~~~~

### S40. `ig34_p0433_a032` — r2:TYPO_SIB2

- PDF 页 433 · 原子类型 SENTENCE · 所在节 `§8.4.3 SUPP-- Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-SUPPQUAL T-1`: PDF 写 "llustrate" → KB 写 "illustrate" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/domains/SUPPQUAL/examples.md:5`)
- 登记 `B-ch08 T-5`: PDF 写 "标签 Example (无编号)" → KB 写 "Example 2" (处理: KB 写正确值; 依据: 前例为 Example 1; KB `knowledge_base/chapters/ch08_relationships.md:241`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
QNAM holds the name of the supplemental qualifier variable being defined (QSLANG).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0433.txt` 第 44-45 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 43| This example illustrates how the language used for a questionnaire might be represented. The parent domain
 44| (RDOMAIN) is QS, and IDVAR is QSCAT. QNAM holds the name of the supplemental qualifier variable being
 45| defined (QSLANG). The language recorded in QVAL applies to all of the subject’s records, where IDVAR
 46| (QSCAT) equals the value specified in IDVARVAL. In this case, IDVARVAL has values for 2 questionnaires—
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:241` (来源: live valid_hits):

~~~~
 241| **Example 2:** This example illustrates how the language used for a questionnaire might be represented. The parent domain (RDOMAIN) is QS, and IDVAR is QSCAT. QNAM holds the name of the supplemental qualifier variable being defined (QSLANG). The language recorded in QVAL applies to all of the subject’s records, where IDVAR (QSCAT) equals the value specified in IDVARVAL. In this case, IDVARVAL has values for 2 questionnaires—Brief Pain Inventory (BPI) and Alzheimer's Disease Assessment Scale–Cognitive Subscale (ADAS-Cog)—for 2 separate subjects. QVAL identifies the questionnaire language version (French or German) for each subject.
~~~~

