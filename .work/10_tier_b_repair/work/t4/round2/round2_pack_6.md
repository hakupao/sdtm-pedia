# T4.1 第二轮补检包 6 — PDF_TYPO (25 条; 编号 R91-R115)

> 由 `scripts/t4/t4_round2_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 R).

### R91. `ig34_p0018_a036` — r2:PDF_TYPO

- PDF 页 18 · 原子类型 TABLE_ROW · 所在节 `§3.2.1 Dataset-level Metadata`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-ch03`
- 登记 `B-ch03 T-2`: PDF 写 "FT Keys TESTCD" → KB 写 "FTTESTCD" (处理: KB 写正确值; 依据: FT spec; 同表 <XX>TESTCD; KB `knowledge_base/chapters/ch03_submitting_data.md:49`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
FT | Functional Tests | Findings | One record per Functional Test finding per time point per visit per subject | Tabulation | STUDYID, USUBJID, TESTCD, VISITNUM, FTTPTREF, FTTPTNUM | ft.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0018.txt` 第 44-46 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 43|                                              beat per visit per subject                      EGTPTNUM
 44| FT        Functional Tests      Findings     One record per Functional Test       Tabulation STUDYID, USUBJID,     ft.xpt
 45|                                              finding per time point per visit per            TESTCD, VISITNUM,
 46|                                              subject                                         FTTPTREF, FTTPTNUM
 47| GF        Genomics Findings     Findings     One record per finding per           Tabulation STUDYID, USUBJID,     gf.xpt
~~~~

KB 现文: `knowledge_base/chapters/ch03_submitting_data.md:49` (来源: registry B-ch03 T-2 kb_line_now):

~~~~
  49| | FT | Functional Tests | Findings | One record per Functional Test finding per time point per visit per subject | Tabulation | STUDYID, USUBJID, FTTESTCD, VISITNUM, FTTPTREF, FTTPTNUM | ft.xpt |
~~~~

### R92. `ig34_p0026_a037` — r2:PDF_TYPO

- PDF 页 26 · 原子类型 CODE_LITERAL · 所在节 `§4.1.9 [Assigning Natural Keys in the Metadata]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `K3b-registry` · 批 `B-ch04`
- 登记 `B-ch04 T-7`: PDF 写 "STUDYID, USUBJID, VISTNUM, MKTESTCD" → KB 写 "VISITNUM" (处理: KB 写正确值; 依据: 同页其余自然键行与 p27; KB `knowledge_base/chapters/ch04_general_assumptions.md:200`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
STUDYID, USUBJID, VISTNUM, MKTESTCD
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0026.txt` 第 55-55 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 54| Sponsor A chooses the following natural key for the MK domain:
 55|                                   STUDYID, USUBJID, VISTNUM, MKTESTCD
 56| Sponsor B collects data in such a way that the location (MKLOC and MKLAT) and method (MKMETHOD)
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:200` (来源: registry B-ch04 T-7 kb_line_now):

~~~~
 200| STUDYID, USUBJID, VISITNUM, MKTESTCD
~~~~

### R93. `ig34_p0049_a008` — r2:PDF_TYPO

- PDF 页 49 · 原子类型 SENTENCE · 所在节 `§4.4.11 [Disease Milestones and Disease Milestone Timing Variables]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-ch04`
- 登记 `B-ch04 T-4`: PDF 写 "occurrs" → KB 写 "occurs" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/chapters/ch04_general_assumptions.md:1195`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
If something that has been defined as a disease milestone for a particular study occurrs for a particular subject, it is represented as usual: in the appropriate findings, intervention, or events class record.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0049.txt` 第 11-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 10| Disease Milestone Name (MIDS)
 11| If something that has been defined as a disease milestone for a particular study occurrs for a particular subject, it is
 12| represented as usual: in the appropriate findings, intervention, or events class record. In addition, this record will
 13| include the MIDS timing variable, populated with the name of the disease milestone. The timing of a disease
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1195` (来源: registry B-ch04 T-4 kb_line_now):

~~~~
1195| If something that has been defined as a disease milestone for a particular study occurs for a particular subject, it is represented as usual: in the appropriate findings, intervention, or events class record. In addition, this record will include the MIDS timing variable, populated with the name of the disease milestone. The timing of a disease milestone is also represented in the special-purpose SM domain.
~~~~

### R94. `ig34_p0082_a025` — r2:PDF_TYPO

- PDF 页 82 · 原子类型 TABLE_HEADER · 所在节 `§5.3 [Subject Elements (SE)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `S-SPREL`
- 登记 `S-SPREL SE T-1`: PDF 写 "dm 表头 BIRTHDTC (p82-84)" → KB 写 "BRTHDTC" (处理: KB 写正确值; 依据: DM spec 与 DM 例均 BRTHDTC; KB `knowledge_base/domains/SE/examples.md:44`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row | USUBJID | SUBJID | RFSTDTC | RFENDTC | SITEID | INVNAM | BIRTHDTC | AGE | AGEU | SEX | RACE | ETHNIC | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD | COUNTRY
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0082.txt` 第 36-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35| dm.xpt
 36| Row USUBJID SUBJID RFSTDTC RFENDTC SITEID INVNAM BIRTHDTC AGE AGEU SEX RACE ETHNIC                         ARMCD ARM     ACTARMCD ACTARM ARMNRS ACTARMUD COUNTRY
 37| 1   789     001    2006-06- 2006-06- 01   SMITH, 1948-12-13 57 YEARS M WHITE HISPANIC OR                   IO    IV-     IO       IV-ORAL                USA
~~~~

KB 现文: `knowledge_base/domains/SE/examples.md:44-44` (来源: fuzzy locate (score 0.95)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  44| | Row | USUBJID | SUBJID | RFSTDTC | RFENDTC | SITEID | INVNAM | BRTHDTC | AGE | AGEU | SEX | RACE | ETHNIC | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD | COUNTRY |
~~~~

### R95. `ig34_p0124_a017` — r2:PDF_TYPO

- PDF 页 124 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-ML`
- 登记 `B-ML T-1`: PDF 写 "Ex2 r2 MLTRT WHTE MILK" → KB 写 "WHITE MILK" (处理: KB 写正确值; 依据: 同表 r8 / 叙述 white milk; KB `knowledge_base/domains/ML/examples.md:66`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2 | ABC123 | ML | ABC123-001 | 2 | WHTE MILK | 1 | WEEK 1 | 2015-09-09
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0124.txt` 第 35-35 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 34| 1        ABC123         ML       ABC123-001     1          FRUIT ROLLUP                         1            WEEK 1     2015-09-09
 35| 2        ABC123         ML       ABC123-001     2          WHTE MILK                            1            WEEK 1     2015-09-09
 36| 3        ABC123         ML       ABC123-001     3          PEANUT BUTTER SANDWICH               1            WEEK 1     2015-09-09
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:66` (来源: registry B-ML T-1 kb_line_now):

~~~~
  66| | 2 | ABC123 | ML | ABC123-001 | 2 | WHITE MILK | 1 | WEEK 1 | 2015-09-09 |
~~~~

### R96. `ig34_p0198_a020` — r2:PDF_TYPO

- PDF 页 198 · 原子类型 SENTENCE · 所在节 `§6.3.5.2 Biospecimen Findings (BS)`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `K3b-registry` · 批 `B-BS`
- 登记 `B-BS T-1a`: PDF 写 "rations" → KB 写 "ratios" (处理: KB 写正确值; 依据: 同句/上句均为 ratios 语境; KB `knowledge_base/domains/BS/examples.md:7`)
- 登记 `B-BS T-1b`: PDF 写 "may indicated" → KB 写 "may indicate" (处理: KB 写正确值; 依据: 情态动词后原形; KB `knowledge_base/domains/BS/examples.md:7`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-2: The A260/A280 and A260/A230 rations are used to determine the purity of the RNA sample. Any ratios outside of the accepted values may indicated contamination with protein or reagents used during the extraction process.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0198.txt` 第 37-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36| storage or isolation methods might compromise the usability of a sample.
 37| Rows 1-2:       The A260/A280 and A260/A230 rations are used to determine the purity of the RNA sample. Any ratios outside of the accepted values may
 38|                 indicated contamination with protein or reagents used during the extraction process.
 39| Row 3:          The amounts of both 28S and 18S ribosomal RNA are measured and then a ratio is calculated. Because values in --TESTCD cannot begin with a
~~~~

KB 现文: `knowledge_base/domains/BS/examples.md:7` (来源: registry B-BS T-1a kb_line_now):

~~~~
   7| **Rows 1-2:** The A260/A280 and A260/A230 ratios are used to determine the purity of the RNA sample. Any ratios outside of the accepted values may indicate contamination with protein or reagents used during the extraction process.
~~~~

### R97. `ig34_p0205_a005` — r2:PDF_TYPO

- PDF 页 205 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `S-SPC1`
- 登记 `S-SPC1 CP T-16b`: PDF 写 "asm 4 CPSCMRKS ×3" → KB 写 "CPCSMRKS" (处理: KB 写正确值; 依据: spec 变量 CPCSMRKS; KB `knowledge_base/domains/CP/assumptions.md:58`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
4. CPCELSTA is used in conjunction with CPCSMRKS. When CPCELSTA is populated, CPCSMRKS must also be populated. Conversely, when CPCSMRKS is populated, CPCELSTA must be populated.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0205.txt` 第 13-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12|         than derived; the Derived Flag (CPDRVFL) should be null for these results.
 13|    4.   CPCELSTA is used in conjunction with CPSCMRKS. When CPCELSTA is populated, CPSCMRKS must
 14|         also be populated. Conversely, when CPSCMRKS is populated, CPCELSTA must be populated.
 15|    5.   The combination of values in CPTEST, CPSBMRKS, CPCELSTA, and CPCSMRKS are used to uniquely
 16|         identify a test. When 1 or more of the variables CPSBMRKS, CPCELSTA, or CPCSMRKS are populated,
~~~~

KB 现文: `knowledge_base/domains/CP/assumptions.md:58` (来源: decision.evidence.hit):

~~~~
  58| 4. CPCELSTA is used in conjunction with CPCSMRKS. When CPCELSTA is populated, CPCSMRKS must also be populated. Conversely, when CPCSMRKS is populated, CPCELSTA must be populated.
~~~~

### R98. `ig34_p0213_a009` — r2:PDF_TYPO

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-CP`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC-123 | CP | ABCD-001-001 | 2 | 1 | MNS | MonoSub | PROLIFERATING | Ki67+ |  | CD14+Ki67+ | MONO FSC+SSC+CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 50 | 10^6/L | 50 | 10^6/L | 50 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 22-23 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 21| 1     ABC-123   CP       ABCD-     1       1         MONO       Monocytes                                             CD14+                   MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTES    394       10^6/L     394        10^6/L     394        QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 22|                          001-001                                                                                                                                                                                                                                              CONCENTRATION            CYTOMETRY     16T08:00
 23| 2     ABC-123   CP       ABCD-     2       1         MNS        MonoSub                    PROLIFERATING   Ki67+      CD14+Ki67+              MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTES    50        10^6/L     50         10^6/L     50         QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 24|                          001-001                                                                                                                                                                                                                                              CONCENTRATION            CYTOMETRY     16T08:00
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:130` (来源: registry B-CP T-6 kb_line_now):

~~~~
 130| | 2 | ABC-123 | CP | ABCD-001-001 | 2 | 1 | MNS | Mono Sub | | PROLIFERATING | Ki67+ | CD14+Ki67+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 50 | 10^6/L | 50 | 10^6/L | 50 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

### R99. `ig34_p0236_a014` — r2:PDF_TYPO

- PDF 页 236 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `K3b-registry` · 批 `B-IS`
- 登记 `B-IS T-1`: PDF 写 "Ex5 r6 STUDYID RSC1230" → KB 写 "RSV1230" (处理: KB 写正确值; 依据: 同列其余 RSV1230; USUBJID RSV1230-011; KB `knowledge_base/domains/IS/examples.md:120`)
- 登记 `B-IS T-2`: PDF 写 "Ex5 r7 STUDYID RSC1230" → KB 写 "RSV1230" (处理: KB 写正确值; 依据: 同 T-1; KB `knowledge_base/domains/IS/examples.md:121`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 6 | RSC1230 | IS | RSV1230-011 | 2 | 13670 | | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:220 | 220 | 220 | titer | SERUM | ELISA | 3 | VISIT 2 | 2017-08-27 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 36-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35|                           011                                            IgG Antibody        SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                          07-27
 36|                                                                                              B
 37| 6        RSC1230   IS     RSV1230-   2       13670             MBIGGAB   Microbial-induced   HUMAN RESPIRATORY         QUANTIFY STUDY VACCINE-RELATED   HUMORAL    1:220    220        220   titer    SERUM   ELISA   3        VISIT 2    2017-
 38|                           011                                            IgG Antibody        SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                          08-27
 39|                                                                                              B
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:120` (来源: registry B-IS T-1 kb_line_now):

~~~~
 120| | 6 | RSV1230 | IS | RSV1230-011 | 2 | 13670 | | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:220 | 220 | 220 | titer | SERUM | ELISA | 3 | VISIT 2 | 2017-08-27 |
~~~~

### R100. `ig34_p0247_a020` — r2:PDF_TYPO

- PDF 页 247 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.6 Laboratory Test Results (LB)`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `K3b-registry` · 批 `B-LB`
- 登记 `B-LB T-1`: PDF 写 "Ex3 表头 LBSTRNHI" → KB 写 "LBSTNRHI" (处理: KB 写正确值; 依据: 同表 LBSTNRLO 与 Ex1/Ex2; KB `knowledge_base/domains/LB/examples.md:67`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBCAT | LBORRES | LBORRESU | LBRESSCL | LBRESTYP | LBORNRLO | LBORNRHI | LBSTRESC | LBSTRESN | LBSTRESU | LBSTNRLO | LBSTNRHI | LBNRIND | LBSTAT | LBREASND | LBLOINC | LBSPEC | LBLOBXFL | VISITNUM | VISIT | LBDTC | LBPTFL |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0247.txt` 第 6-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5| lb.xpt
  6| Row   STUDYID   DOMAIN     USUBJID     LBSEQ    LBGRPID     LBTESTCD    LBTEST                        LBTSTCND          LBCAT            LBSCAT         LBORRES    LBORRESU     LBRESSCL       LBRESTYP                   LBCOLSRT            LBORNRLO         LBORNRHI   LBLLOD              LBSTRESC    LBSTRESN   LBSTRESU     LBSTNRLO        LBSTNRHI   LBSTNRC       LBNRIND      LBSTAT   LBREASND           LBLOINC   LBSPEC          LBMETHOD          LBTMTHSN         LBLOBXFL   LBFAST   LBDRVFL   LBCLSIG   VISITNUM     VISIT    LBDTC       LBPTFL       LBPDUR
  7| 1     ABC       LB         ABC-001-    1                    ALB         Albumin                                         CHEMISTRY                       30         g/L          QUANTITATIVE   MASS CONCENTRATION                             35               50                             3.0         3.0        g/dL         3.5             5                        LOW                                      2862-1    SERUM           ELECTROPHORESIS                    Y          Y                  N         1            Week     1999-06-    Y
~~~~

KB 现文: `knowledge_base/domains/LB/examples.md:67` (来源: decision.evidence.hit):

~~~~
  67| | Row | STUDYID | DOMAIN | USUBJID | LBSEQ | LBTESTCD | LBTEST | LBCAT | LBORRES | LBORRESU | LBRESSCL | LBRESTYP | LBORNRLO | LBORNRHI | LBSTRESC | LBSTRESN | LBSTRESU | LBSTNRLO | LBSTNRHI | LBNRIND | LBSTAT | LBREASND | LBLOINC | LBSPEC | LBLOBXFL | VISITNUM | VISIT | LBDTC | LBPTFL |
~~~~

### R101. `ig34_p0323_a006` — r2:PDF_TYPO

- PDF 页 323 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.1 Functional Tests (FT) — FT-Assumptions — QRS Shared Assumptions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-RS`
- 登记 `B-RS T-6 (FT 副本)`: PDF 写 "--STRNC" → KB 写 "--STNRC" (处理: KB 写正确值; 依据: 同节 DR 11 与 spec 为 --STNRC; KB `knowledge_base/domains/FT/assumptions.md:78`)
- 登记 `B-RS T-6 (RS 副本)`: PDF 写 "--STRNC" → KB 写 "--STNRC" (处理: KB 写正确值; 依据: 同节 DR 11 与 spec 为 --STNRC; KB `knowledge_base/domains/RS/assumptions.md:128`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
10.	Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STRNC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0323.txt` 第 11-13 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 10|                ii. Sponsors should always consult the published QRS supplements for guidance on submitting derived information in SDTMIG-based domains.
 11|      10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would
 12|          generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STRNC, --NRIND, --XFN, --LOINC, --SPEC, --
 13|          SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.
 14| FT – Examples
~~~~

KB 现文: `knowledge_base/domains/FT/assumptions.md:78-78` (来源: fuzzy locate (score 0.976)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  78| 10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.
~~~~

### R102. `ig34_p0353_a009` — r2:PDF_TYPO

- PDF 页 353 · 原子类型 SENTENCE · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-TU`
- 登记 `B-TU T-1`: PDF 写 "aorta-iliac vessel" → KB 写 "aorto-iliac" (处理: KB 写正确值; 依据: 同例叙述 + TULOC; KB `knowledge_base/domains/TU/examples.md:13`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-2:	Show the target lesion located in the infrarenal aorta and within the aorta-iliac vessel.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0353.txt` 第 21-21 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20| left popliteal artery.
 21| Rows 1-2:       Show the target lesion located in the infrarenal aorta and within the aorta-iliac vessel.
 22| Row 3:          Shows the PVI target limb in which the graft lesion is located identified by the investigator.
~~~~

KB 现文: `knowledge_base/domains/TU/examples.md:13` (来源: registry B-TU T-1 kb_line_now):

~~~~
  13| **Rows 1-2:** Show the target lesion located in the infrarenal aorta and within the aorto-iliac vessel.
~~~~

### R103. `ig34_p0377_a021` — r2:PDF_TYPO

- PDF 页 377 · 原子类型 LIST_ITEM · 所在节 `SR – Assumptions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-SR`
- 登记 `B-SR T-3`: PDF 写 "reactogencity" → KB 写 "reactogenicity" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/domains/SR/assumptions.md:15`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This domain is intended specifically for tests of the immune response to substances that are intended to provoke such a response (e.g., allergens used in allergy testing). SR is not intended for other injection-site reactions, including reactogencity events that may follow a vaccine administration.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0377.txt` 第 49-50 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 48|            FA.
 49|      2.    This domain is intended specifically for tests of the immune response to substances that are intended to provoke such a response (e.g., allergens used in
 50|            allergy testing). SR is not intended for other injection-site reactions, including reactogencity events that may follow a vaccine administration.
 51| 
~~~~

KB 现文: `knowledge_base/domains/SR/assumptions.md:15` (来源: registry B-SR T-3 kb_line_now):

~~~~
  15| 2. This domain is intended specifically for tests of the immune response to substances that are intended to provoke such a response (e.g., allergens used in allergy testing). SR is not intended for other injection-site reactions, including reactogenicity events that may follow a vaccine administration.
~~~~

### R104. `ig34_p0414_a013` — r2:PDF_TYPO

- PDF 页 414 · 原子类型 TABLE_HEADER · 所在节 `§7.3.2 Trial Disease Assessments (TD) – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `S-TDM`
- 登记 `S-TDM TD T-4`: PDF 写 "Ex3 表头 TDTGPAI" → KB 写 "TDTGTPAI" (处理: KB 写正确值; 依据: spec + Ex1/Ex2 表头; KB `knowledge_base/domains/TD/examples.md:167`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0414.txt` 第 29-29 行 (自动定位, 词覆盖 0.9; 版式以原 PDF 为准):

~~~~
 28| td.xpt
 29| Row       STUDYID   DOMAIN   TDORDER   TDANCVAR    TDSTOFF   TDTGPAI   TDMINPAI   TDMAXPAI   TDNUMRPT
 30| 1         ABC123    TD       1         ANCH1DT     P0D       P8W       P53D       P9W        6
~~~~

KB 现文: `knowledge_base/domains/TD/examples.md:50,102,167` (来源: decision.evidence.hit):

> 同一文件共 3 处逐字命中 (行 50, 102, 167); 请按 PDF 所在例/表判断对应的是哪一处

~~~~
  50| | Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
 102| | Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
 167| | Row | STUDYID | DOMAIN | TDORDER | TDANCVAR | TDSTOFF | TDTGTPAI | TDMINPAI | TDMAXPAI | TDNUMRPT |
~~~~

### R105. `ig34_p0427_a011` — r2:PDF_TYPO

- PDF 页 427 · 原子类型 LIST_ITEM · 所在节 `§8 [REPRESENTING RELATIONSHIPS AND DATA]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-ch08`
- 登记 `B-ch08 T-1`: PDF 写 "TWIN, DIZOGOTIC" → KB 写 "DIZYGOTIC" (处理: KB 写正确值; 依据: p439 relsub r4/r6; KB `knowledge_base/chapters/ch08_relationships.md:15`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Section 8.7, Relating Subjects, describes representing collected relationships between persons, both of whom are study subjects. For example: "MOTHER, BIOLOGICAL"; "CHILD, BIOLOGICAL"; "TWIN, DIZOGOTIC".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0427.txt` 第 24-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23|          general observation class domain.
 24|     •    Section 8.7, Relating Subjects, describes representing collected relationships between persons, both of
 25|          whom are study subjects. For example: "MOTHER, BIOLOGICAL"; "CHILD, BIOLOGICAL"; "TWIN,
 26|          DIZOGOTIC".
 27|     •    Section 8.8, Related Specimens, is a dataset used to represent relationships between specimens.
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:15` (来源: registry B-ch08 T-1 kb_line_now):

~~~~
  15| - Section 8.7, Relating Subjects, describes representing collected relationships between persons, both of whom are study subjects. For example: "MOTHER, BIOLOGICAL"; "CHILD, BIOLOGICAL"; "TWIN, DIZYGOTIC".
~~~~

### R106. `ig34_p0010_a002` — r2:PDF_TYPO

- PDF 页 10 · 原子类型 LIST_ITEM · 所在节 `§1.4.1 [How to Read a Domain Specification]`
- triage 类 **REWRITE_OK** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `S1-R2` · 批 `B-ch01`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-ch01 T-1: PDF 缺 has, KB 补; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ch01.md:98`
- 登记 `B-ch01 T-1`: PDF 写 "a codelist not yet been developed" → KB 写 "has not yet been" (处理: KB 写正确值; 依据: p49 同短语旁证; KB `knowledge_base/chapters/ch01_introduction.md:85`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The controlled terminology might be of a type that could be standardized, but for which a codelist not yet been developed.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0010.txt` 第 2-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1|                   •     The controlled terminology might be of a type that would inherently be sponsor-defined.
  2|                   •     The controlled terminology might be of a type that could be standardized, but for which a
  3|                         codelist not yet been developed.
  4|                   •     The controlled terminology might be terminology specified in value-level metadata.
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:85` (来源: registry B-ch01 T-1 kb_line_now):

~~~~
  85|       - The controlled terminology might be of a type that could be standardized, but for which a codelist has not yet been developed.
~~~~

### R107. `ig34_p0085_a010` — r2:PDF_TYPO

- PDF 页 85 · 原子类型 SENTENCE · 所在节 `§5.4 [Subject Disease Milestones (SM)]`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-SM`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-8 B-SM O32 SMDY→SMSTDY | errata: t3_atom_err | new_target: domains/SM/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:6`
- 登记 `B-SM O32`: PDF 写 "Row 1 叙述 SMDY" → KB 写 "SMSTDY (SM Assumption 3b + Rows 2-3 叙述)" (处理: KB 写正确值; 依据: 非 SM 变量 (疑 SMSTDY); 不能唯一确定 (O32); KB `knowledge_base/domains/SM/examples.md:7`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 1: Shows that subject 001's initial diagnosis of diabetes occurred in October 2005. Because this is a partial date, SMDY is not populated. No end date/time was recorded for this milestone.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0085.txt` 第 14-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13| In this study, the disease milestones of interest were initial diagnosis and hypoglycemic events, as shown in Section 7.3.3, Trial Disease Milestones, Example 1.
 14| Row 1:          Shows that subject 001's initial diagnosis of diabetes occurred in October 2005. Because this is a partial date, SMDY is not populated. No end
 15|                 date/time was recorded for this milestone.
 16| Rows 2-3:       Show that subject 001 had 2 hypoglycemic events. In this case, only start date/times have been collected. Because these date/times include full
~~~~

KB 现文: `knowledge_base/domains/SM/examples.md:7` (来源: registry B-SM O32 kb_line_now):

~~~~
   7| **Row 1:** Shows that subject 001's initial diagnosis of diabetes occurred in October 2005. Because this is a partial date, SMSTDY is not populated. No end date/time was recorded for this milestone.
~~~~

### R108. `ig34_p0198_a012` — r2:PDF_TYPO

- PDF 页 198 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.2 Biospecimen Findings (BS)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-BS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-BS review: PDF 'part the' (PDF_TYPO) 被抽成 'part of the'; KB 正确拼写; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-BS_review.md:54 (页级行; 该批以范围/页号记这组原子)`
- 登记 `B-BS T-2`: PDF 写 "part the SEND" → KB 写 "part of the SEND" (处理: KB 写正确值; 依据: 缺 of, 语法单值; KB `knowledge_base/domains/BS/assumptions.md:19`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
3. Non-genetic BSSPEC values are drawn from the SPEC (C77529) codelist, which is part of the SEND terminology listing. BSANTREG is used to further define BSSPEC when it is desirable to identify a specific region within an organ.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0198.txt` 第 25-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24|            PGx-related specimens.
 25|      2.    For biospecimens of genetic material, BSSPEC values are drawn from the GENSMP (C111114) codelist.
 26|      3.    Non-genetic BSSPEC values are drawn from the SPEC (C77529) codelist, which is part the SEND terminology listing. BSANTREG is used to further
 27|            define BSSPEC when it is desirable to identify a specific region within an organ.
 28|      4.    To adapt BS for use with the SDTMIG, use the SPECTYPE (C78734) codelist in BSSPEC, add --LOC, --LAT, --DIR, and --PORTOT as applicable,
~~~~

KB 现文: `knowledge_base/domains/BS/assumptions.md:19` (来源: decision.evidence.hit):

~~~~
  19| 3. Non-genetic BSSPEC values are drawn from the SPEC (C77529) codelist, which is part of the SEND terminology listing. BSANTREG is used to further define BSSPEC when it is desirable to identify a specific region within an organ.
~~~~

### R109. `ig34_p0199_a020` — r2:PDF_TYPO

- PDF 页 199 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `S-SPC1`
- 原子抽错登记: R2 → PDF_TYPO; 依据: S-SPC1 CP T-21 PDF_TYPO --BNDAGT/--GATEDEF→--BDAGNT/--GATDEF (spec 变量名) | errata: t3_atom_err | new_target: domains/CP/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:23`
- 登记 `S-SPC1 CP T-21`: PDF 写 "--BNDAGT / --GATEDEF ×2 / CPBNDAGT" → KB 写 "--BDAGNT / --GATDEF / CPBDAGNT" (处理: KB 写正确值; 依据: spec 变量 CPBDAGNT/CPGATDEF; p208 列名; KB `knowledge_base/domains/CP/assumptions.md:24`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
New variables include --SBMRKS (Sublineage Marker String), --CELSTA (Cell State), --CSMRKS (Cell State Marker String), --TSTCND (Test Condition), --CNDAGT (Test Condition Agent), --BNDAGT (Binding Agent), --ABCLID (Antibody Clone Identifier), --MRKSTR (Marker String), --GATE (Gate Name), --GATEDEF (Gate Definition), --SPTSTD (Sponsor Test Description), --TSTPNL (Test Panel), --RESSCL (Result Scale), and --RESTYP (Result Type).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0199.txt` 第 32-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| To provide the flexibility needed to report cell marker expression data, which can range widely in complexity, several new SDTM variables have been created. Most of the new variables are permissible, and are
 32| available as needed to fully define a test and/or to prevent ambiguity that could lead to misunderstanding or difficulty in interpreting the data. New variables include --SBMRKS (Sublineage Marker String), --
 33| CELSTA (Cell State), --CSMRKS (Cell State Marker String), --TSTCND (Test Condition), --CNDAGT (Test Condition Agent), --BNDAGT (Binding Agent), --ABCLID (Antibody Clone Identifier), --MRKSTR
 34| (Marker String), --GATE (Gate Name), --GATEDEF (Gate Definition), --SPTSTD (Sponsor Test Description), --TSTPNL (Test Panel), --RESSCL (Result Scale), and --RESTYP (Result Type). Definitions and
 35| appropriate use of these variables are provided in the Specification and Assumptions sections of this guidance and are illustrated in the examples for selected use cases.
~~~~

KB 现文: `knowledge_base/domains/CP/assumptions.md:24` (来源: registry S-SPC1 CP T-21 kb_line_now):

~~~~
  24| New variables include --SBMRKS (Sublineage Marker String), --CELSTA (Cell State), --CSMRKS (Cell State Marker String), --TSTCND (Test Condition), --CNDAGT (Test Condition Agent), --BDAGNT (Binding Agent), --ABCLID (Antibody Clone Identifier), --MRKSTR (Marker String), --GATE (Gate Name), --GATDEF (Gate Definition), --SPTSTD (Sponsor Test Description), --TSTPNL (Test Panel), --RESSCL (Result Scale), and --RESTYP (Result Type).
~~~~

### R110. `ig34_p0212_a012` — r2:PDF_TYPO

- PDF 页 212 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-CP`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec); 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CP.md:83`
- 登记 `B-CP T-15`: PDF 写 "叙述 CPGATEDEF (8 处)" → KB 写 "CPGATDEF" (处理: KB 写正确值; 依据: p202 spec 变量名 CPGATDEF; KB `knowledge_base/domains/CP/examples.md:71`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-3: Show use of CPCELSTA and CPCSMRKS to further subset the named cell population in CPTEST. In row 1, the total monocyte population, based on expression of CD14, is measured without any further subsetting. Rows 2 and 3 show that the monocyte population is further subdivided, based on the cell state, into "proliferating" and "non-proliferating" subpopulations as indicated by the CPCELSTA value. The value "Monocytes" in CPTEST for these rows is appended with "Sub" to "Monocytes Sub" to indicate that the record pertains to a subpopulation of monocytes (i.e., proliferating or non-proliferating). CPCELSTA is used to indicate that row 2 contains data for the proliferating subpopulation and row 3 contains data for the non-proliferating subpopulation. The CPCSMRKS variable is used to indicate that positive expression of the Ki67 marker (i.e., Ki67+) is used to identify the proliferating subpopulation and cells that do not express the Ki67 marker (i.e., Ki67-) is used to identify the non-proliferating subpopulation. The full set of markers used for the test are included in CPMRKSTR, and the cell gating strategy is identified in CPGATE and CPGATEDEF using the pipe character (|) to separate each level of the gate in CPGATEDEF.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0212.txt` 第 37-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36| each of the 2 records (i.e., "TLym Help 2 Sub"), and CPSBMRKS would contain "CDxx+CDyy-" in 1 of the records and "CDxx-CDyy+" in the other.
 37| Rows 1-3:        Show use of CPCELSTA and CPCSMRKS to further subset the named cell population in CPTEST. In row 1, the total monocyte population, based on expression of CD14, is measured without any
 38|                  further subsetting. Rows 2 and 3 show that the monocyte population is further subdivided, based on the cell state, into "proliferating" and "non-proliferating" subpopulations as indicated by the
 39|                  CPCELSTA value. The value "Monocytes" in CPTEST for these rows is appended with "Sub" to "Monocytes Sub" to indicate that the record pertains to a subpopulation of monocytes (i.e., proliferating
 40|                  or non-proliferating). CPCELSTA is used to indicate that row 2 contains data for the proliferating subpopulation and row 3 contains data for the non-proliferating subpopulation. The CPCSMRKS
 41|                  variable is used to indicate that positive expression of the Ki67 marker (i.e., Ki67+) is used to identify the proliferating subpopulation and cells that do not express the Ki67 marker (i.e., Ki67-) is used to
 42|                  identify the non-proliferating subpopulation. The full set of markers used for the test are included in CPMRKSTR, and the cell gating strategy is identified in CPGATE and CPGATEDEF using the pipe
 43|                  character (|) to separate each level of the gate in CPGATEDEF.
 44| Rows 4-5:        Show the proliferating (from row 2) and non-proliferating (from row 3) monocyte subpopulations expressed as a percentage of total monocytes (from row 1). The numerators in CPTEST for rows 4-5
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:71` (来源: registry B-CP T-15 kb_line_now):

~~~~
  71| **Rows 1-2:** Forward light scatter (FSC) and side scatter (SSC) are almost always applied as the first gating parameters to distinguish singlets and viable cells from doublets and debris. In row 1, a lymphocyte (LYM) count is reported which does not explicitly provide viability information. Nevertheless, it is generally assumed that FSC SSC gating is applied to exclude doublets, debris, and dead cells. Secondary FSC and SSC gating is then used to distinguish the lymphocyte population from other CD45+ leukocytes. In contrast, row 2 explicitly calls out cell viability based on the use of viability marker 7AAD to exclude cells that are in the process of dying (7AAD+). This is indicated in the Marker String (CPMRKSTR) and Gate Definition (CPGATDEF) variables. In addition, the term "VIABLE" is included in the gate name (CPGATE).
~~~~

### R111. `ig34_p0240_a004` — r2:PDF_TYPO

- PDF 页 240 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-IS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-IS T-4 PDF_TYPO nucleoar→nucleolar; S-SPC1 D2 删 IS/assumptions 附录副本, 现在 IS/examples.md:215 | errata: t3_atom_err (次: t3_target_remap→IS/examples.md) | new_target: domains/IS/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:30`
- 登记 `B-IS T-4`: PDF 写 "(i.e., nucleoar)" → KB 写 "nucleolar" (处理: KB 写正确值; 依据: 同表 r5 NUCLEOLAR PATTERN; KB `knowledge_base/domains/IS/examples.md:215`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-5:	Show the screening (row 1) and quantification (rows 2, 4) of ANAs. Rows 2 and 3 are grouped together using ISGRPID="1a"; this means the titer result in row 2 is specifically related to the particular nuclear staining pattern (i.e., speckled) finding in row 3. The speckled pattern of ANA is typically indicative of SS, systemic lupus, and mixed connective tissue disease. Rows 4 and 5 are grouped together using ISGRPID="1b"; this means the titer result in row 4 is specifically related to the nuclear staining pattern (i.e., nucleoar) finding in row 5. Rows 1 to 5 are grouped together using ISGRPID with values starting with the number "1", indicating that these records are related. The antinuclear antibodies test is post-coordinated and represented by both ISTEST="Autoantibody" and ISBDAGNT="NUCLEAR AUTOANTIGENS".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0240.txt` 第 5-9 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  4| anti-La (SS-B) antibodies.
  5| Rows 1-5:      Show the screening (row 1) and quantification (rows 2, 4) of ANAs. Rows 2 and 3 are grouped together using ISGRPID="1a"; this means the titer result in row 2 is specifically related to the particular
  6|                nuclear staining pattern (i.e., speckled) finding in row 3. The speckled pattern of ANA is typically indicative of SS, systemic lupus, and mixed connective tissue disease. Rows 4 and 5 are grouped
  7|                together using ISGRPID="1b"; this means the titer result in row 4 is specifically related to the nuclear staining pattern (i.e., nucleoar) finding in row 5. Rows 1 to 5 are grouped together using ISGRPID
  8|                with values starting with the number "1", indicating that these records are related. The antinuclear antibodies test is post-coordinated and represented by both ISTEST="Autoantibody" and
  9|                ISBDAGNT="NUCLEAR AUTOANTIGENS".
 10| Rows 6-11: Show the screening and quantification of the various SS-specific autoantibodies. SS autoantigens are represented by the ISBDAGNT variable, whereas the ISTEST="Autoantibody".
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:215` (来源: registry B-IS T-4 kb_line_now):

~~~~
 215| **Rows 1-5:** Show the screening (row 1) and quantification (rows 2, 4) of ANAs. Rows 2 and 3 are grouped together using ISGRPID="1a"; this means the titer result in row 2 is specifically related to the particular nuclear staining pattern (i.e., speckled) finding in row 3. The speckled pattern of ANA is typically indicative of SS, systemic lupus, and mixed connective tissue disease. Rows 4 and 5 are grouped together using ISGRPID="1b"; this means the titer result in row 4 is specifically related to the nuclear staining pattern (i.e., nucleolar) finding in row 5. Rows 1 to 5 are grouped together using ISGRPID with values starting with the number "1", indicating that these records are related. The antinuclear antibodies test is post-coordinated and represented by both ISTEST="Autoantibody" and ISBDAGNT="NUCLEAR AUTOANTIGENS".
~~~~

### R112. `ig34_p0262_a029` — r2:PDF_TYPO

- PDF 页 262 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-MS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-MS T-3: verbatim IDVAR=MBREFID 为 PDF 笔误, KB 改 MSREFID; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-MS.md:133`
- 登记 `B-MS T-3`: PDF 写 "suppms IDVAR MBREFID" → KB 写 "MSREFID" (处理: KB 写正确值; 依据: RDOMAIN=MS, IDVARVAL=ms MSREFID; KB `knowledge_base/domains/MS/examples.md:80`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
1 | ABC | MS | ABC-01-101 | MBREFID | 100.4 | MSMEDTYPE | Medium Type | LOWENSTEIN-JENSEN | Collected
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0262.txt` 第 54-54 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 53| Row    STUDYID       RDOMAIN   USUBJID           IDVAR     IDVARVAL   QNAM             QLABEL             QVAL                       QORIG
 54| 1      ABC           MS        ABC-01-101        MBREFID   100.4      MSMEDTYPE        Medium Type        LOWENSTEIN-JENSEN          Collected
 55| 2      ABC           MS        ABC-01-101        MBREFID   100.5      MSMEDTYPE        Medium Type        LOWENSTEIN-JENSEN          Collected
~~~~

KB 现文: `knowledge_base/domains/MS/examples.md:80` (来源: registry B-MS T-3 kb_line_now):

~~~~
  80| | 1 | ABC | MS | ABC-01-101 | MSREFID | 100.4 | MSMEDTYPE | Medium Type | LOWENSTEIN-JENSEN | Collected |
~~~~

### R113. `ig34_p0280_a040` — r2:PDF_TYPO

- PDF 页 280 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 3`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-PCPP`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-2 B-PCPP T-8 DYIDRGX_HALF→DY1DRGX_HALF | errata: t3_atom_err | new_target: domains/PC/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:68`
- 登记 `B-PCPP T-8`: PDF 写 "散文 DYIDRGX_A / DYIDRGX_HALF" → KB 写 "DY1DRGX_A / DY1DRGX_HALF (同页 relrec IDVARVAL)" (处理: KB 写正确值; 依据: 文本层即如此, 与表 DY1DRGX_* 不一致; KB `knowledge_base/domains/PC/examples.md:284`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 4-6: The relationship with RELID "2" includes only PC records with PCGRPID = "DY1_DRGX_A" and all PP records with PPGRPID = "DYIDRGX_HALF".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0280.txt` 第 53-54 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 52|              PP records with PPGRPID = "DYIDRGX_A".
 53| Rows 4-6:    The relationship with RELID "2" includes only PC records with PCGRPID = "DY1_DRGX_A" and
 54|              all PP records with PPGRPID = "DYIDRGX_HALF".
 55| relrec.xpt
~~~~

KB 现文: `knowledge_base/domains/PC/examples.md:284` (来源: registry B-PCPP T-8 kb_line_now):

~~~~
 284| - Rows 1-3: The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX_A", all PC records with PCGRPID = "DY1_DRGX_B" (which in this case is all the PP records for Day 1) and all PP records with PPGRPID = "DY1DRGX_A".
~~~~

### R114. `ig34_p0335_a015` — r2:PDF_TYPO

- PDF 页 335 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.1 Disease Response Use Case`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-RS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-RS T-7 PDF_TYPO 叙述 RSPLNKGRP→RSLNKGRP | errata: t3_atom_err | new_target: domains/RS/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:83`
- 登记 `B-RS T-7`: PDF 写 "叙述 RSPLNKGRP ×4" → KB 写 "RSLNKGRP" (处理: KB 写正确值; 依据: 表头/spec/DR 6a; KB `knowledge_base/domains/RS/examples.md:50`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 1:  Shows disease progression on or after a prior chemotherapy regimen. The date of progression is represented in RSDTC. RSENTPT and RSENRTPT represent that the disease progression was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the disease progression was unknown or not collected. RSPLNKGRP = "CM1" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM1".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0335.txt` 第 26-28 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25| This example shows best response and the overall response of progression to prior therapies and follow-up therapies.
 26| Row 1:         Shows disease progression on or after a prior chemotherapy regimen. The date of progression is represented in RSDTC. RSENTPT and RSENRTPT represent that the disease progression was prior to
 27|                screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the disease progression was unknown or not collected. RSPLNKGRP = "CM1" is used to link this record in RS to the
 28|                prior chemotherapy in CM where the CMLNKGRP = "CM1".
 29| Row 2:         Shows best response to prior chemotherapy regimen. The date of best response is represented in RSDTC. RSENTPT and RSENRTPT represent that the best response was prior to screening. RSCAT =
~~~~

KB 现文: `knowledge_base/domains/RS/examples.md:50` (来源: registry B-RS T-7 kb_line_now):

~~~~
  50| **Row 1:** Shows disease progression on or after a prior chemotherapy regimen. The date of progression is represented in RSDTC. RSENTPT and RSENRTPT represent that the disease progression was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the disease progression was unknown or not collected. RSLNKGRP = "CM1" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM1".
~~~~

### R115. `ig34_p0370_a021` — r2:PDF_TYPO

- PDF 页 370 · 原子类型 SENTENCE · 所在节 `FA – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-FA`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-FA T-7: PDF parent CE record → KB AE; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-FA.md:129`
- 登记 `B-FA T-7`: PDF 写 "linked to the parent CE record" → KB 写 "parent AE record" (处理: KB 写正确值; 依据: 同例 rash 记 AE, relrec RDOMAIN=AE (review C-3 改判); KB `knowledge_base/domains/FA/examples.md:118`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The FA records were linked to the parent CE record via the AE reference number, which was used to populate both AESPID and FASPID.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0370.txt` 第 26-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25| 
 26| The FA records were linked to the parent CE record via the AE reference number, which was used to populate both AESPID and FASPID.
 27| relrec.xpt
~~~~

KB 现文: `knowledge_base/domains/FA/examples.md:118` (来源: registry B-FA T-7 kb_line_now):

~~~~
 118| The FA records were linked to the parent AE record via the AE reference number, which was used to populate both AESPID and FASPID.
~~~~

