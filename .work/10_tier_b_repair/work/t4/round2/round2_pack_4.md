# T4.1 第二轮补检包 4 — TYPO_SIB (25 条; 编号 R53-R77)

> 由 `scripts/t4/t4_round2_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 R).

### R53. `ig34_p0206_a005` — r2:TYPO_SIB

- PDF 页 206 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-SPC1 CP T-16b`: PDF 写 "asm 4 CPSCMRKS ×3" → KB 写 "CPCSMRKS" (处理: KB 写正确值; 依据: spec 变量 CPCSMRKS; KB `knowledge_base/domains/CP/assumptions.md:58`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
8. Recommended formatting of marker string variables CPMRKSTR, CPSBMRKS, and CPCSMRKS: The marker string variables provide critical information for defining a test. Although there are no current plans to control their values through CDISC Controlled Terminology codelists, adherence to the following formatting guidelines helps to preclude ambiguities that can lead to uncertainty in uniquely understanding a test and its associated result.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0206.txt` 第 20-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19|           in CPMRKSTR.
 20| 8.   Recommended formatting of marker string variables CPMRKSTR, CPSBMRKS, and CPCSMRKS: The
 21|      marker string variables provide critical information for defining a test. Although there are no current plans
 22|      to control their values through CDISC Controlled Terminology codelists, adherence to the following
 23|      formatting guidelines helps to preclude ambiguities that can lead to uncertainty in uniquely understanding a
 24|      test and its associated result.
 25|      a.   Marker strings do not contain delimiting characters (e.g., ",", space, "/", "|") to separate individual
~~~~

KB 现文: `knowledge_base/domains/CP/assumptions.md:78` (来源: live valid_hits):

~~~~
  78| 8. Recommended formatting of marker string variables CPMRKSTR, CPSBMRKS, and CPCSMRKS: The marker string variables provide critical information for defining a test. Although there are no current plans to control their values through CDISC Controlled Terminology codelists, adherence to the following formatting guidelines helps to preclude ambiguities that can lead to uncertainty in uniquely understanding a test and its associated result.
~~~~

### R54. `ig34_p0211_a012` — r2:TYPO_SIB

- PDF 页 211 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | IM001-123 | CP | 0005 00542 | 1 |  | LYM | Lymphocytes |  |  | CD45+FSC SSC | LEUK | CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3500 | 10^6/L | 3500 | 10^6/L | 3500 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0211.txt` 第 32-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| Row   STUDYID   DOMAIN   USUBJID   CPSEQ    CPGRPID   CPTESTCD   CPTEST        CPCELSTA    CPCSMRKS   CPMRKSTR            CPGATE   CPGATDEF     CPCAT               CPTSTPNL    CPORRES   CPORRESU   CPSTRESC   CPSTRESU   CPSTRESN   CPRESSCL       CPRESTYP        CPSPEC   CPMETHOD    CPDTC
 32| 1     IM001-    CP       0005      1                  LYM        Lymphocytes                          CD45+FSC SSC        LEUK     CD45+        IMMUNOPHENOTYPING   LYM         3500      10^6/L     3500       10^6/L     3500       QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
 33|       123                00542                                                                                                                                      APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 34|                                                                                                                                                                     COUNT
 35| 2     IM001-    CP       0005      2        1         LYM        Lymphocytes                          CD45+7AAD-FSC SSC   LEUK,    CD45+7AAD-   IMMUNOPHENOTYPING   LYM         3325      10^6/L     3325       10^6/L     3325       QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:87` (来源: live valid_hits):

~~~~
  87| | 1 | IM001-123 | CP | 0005 00542 | 1 | | LYM | Lymphocytes | | | CD45+FSC SSC | LEUK | CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3500 | 10^6/L | 3500 | 10^6/L | 3500 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

### R55. `ig34_p0211_a013` — r2:TYPO_SIB

- PDF 页 211 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | IM001-123 | CP | 0005 00542 | 2 |  | LYM | Lymphocytes |  |  | CD45+7AAD-FSC SSC | LEUK, VIABLE | CD45+7AAD- | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3325 | 10^6/L | 3325 | 10^6/L | 3325 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0211.txt` 第 34-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 33|       123                00542                                                                                                                                      APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 34|                                                                                                                                                                     COUNT
 35| 2     IM001-    CP       0005      2        1         LYM        Lymphocytes                          CD45+7AAD-FSC SSC   LEUK,    CD45+7AAD-   IMMUNOPHENOTYPING   LYM         3325      10^6/L     3325       10^6/L     3325       QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
 36|       123                00542                                                                                            VIABLE                                    APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 37|                                                                                                                                                                     COUNT
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:88-88` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  88| | 2 | IM001-123 | CP | 0005 00542 | 2 | 1 | LYM | Lymphocytes | | | CD45+7AAD-FSC SSC | LEUK, VIABLE | CD45+7AAD- | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3325 | 10^6/L | 3325 | 10^6/L | 3325 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

### R56. `ig34_p0211_a014` — r2:TYPO_SIB

- PDF 页 211 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | IM001-123 | CP | 0005 00542 | 3 | 1 | LYS | Lym Sub | VIABLE | 7AAD- | CD45+7AAD- | LYM | FSC SSC/CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3325 | 10^6/L | 3325 | 10^6/L | 3325 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0211.txt` 第 37-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36|       123                00542                                                                                            VIABLE                                    APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 37|                                                                                                                                                                     COUNT
 38| 3     IM001-    CP       0005      3        1         LYS        Lym Sub       VIABLE      7AAD-      CD45+7AAD-          LYM      FSC          IMMUNOPHENOTYPING   LYM         3325      10^6/L     3325       10^6/L     3325       QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
 39|       123                00542                                                                                                     SSC|CD45+                        APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 40|                                                                                                                                                                     COUNT
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:89-89` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  89| | 3 | IM001-123 | CP | 0005 00542 | 3 | 1 | LYS | Lym Sub | VIABLE | 7AAD- | CD45+7AAD- | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3325 | 10^6/L | 3325 | 10^6/L | 3325 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

### R57. `ig34_p0211_a015` — r2:TYPO_SIB

- PDF 页 211 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | IM001-123 | CP | 0005 00542 | 4 | 1 | LYS | Lym Sub | NON-VIABLE | 7AAD+ | CD45+7AAD+ | LYM | FSC SSC/CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 175 | 10^6/L | 175 | 10^6/L | 175 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0211.txt` 第 40-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39|       123                00542                                                                                                     SSC|CD45+                        APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 40|                                                                                                                                                                     COUNT
 41| 4     IM001-    CP       0005      4        1         LYS        Lym Sub       NON-        7AAD+      CD45+7AAD+          LYM      FSC          IMMUNOPHENOTYPING   LYM         175       10^6/L     175        10^6/L     175        QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
 42|       123                00542                                                 VIABLE                                              SSC|CD45+                        APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 43|                                                                                                                                                                     COUNT
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:90-90` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  90| | 4 | IM001-123 | CP | 0005 00542 | 4 | 1 | LYS | Lym Sub | NON-VIABLE | 7AAD+ | CD45+7AAD+ | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 175 | 10^6/L | 175 | 10^6/L | 175 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

### R58. `ig34_p0211_a016` — r2:TYPO_SIB

- PDF 页 211 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 5 | IM001-123 | CP | 0005 00542 | 5 | 1 | LYS | Lym Sub | APOPTOTIC | ANXV+ | CD45+ANXV+ | LYM | FSC SSC/CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 700 | 10^6/L | 700 | 10^6/L | 700 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0211.txt` 第 42-44 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 41| 4     IM001-    CP       0005      4        1         LYS        Lym Sub       NON-        7AAD+      CD45+7AAD+          LYM      FSC          IMMUNOPHENOTYPING   LYM         175       10^6/L     175        10^6/L     175        QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
 42|       123                00542                                                 VIABLE                                              SSC|CD45+                        APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 43|                                                                                                                                                                     COUNT
 44| 5     IM001-    CP       0005      5        1         LYS        Lym Sub       APOPTOTIC   ANXV+      CD45+ANXV+          LYM      FSC          IMMUNOPHENOTYPING   LYM         700       10^6/L     700        10^6/L     700        QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
 45|       123                00542                                                                                                     SSC|CD45+                        APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:91-91` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  91| | 5 | IM001-123 | CP | 0005 00542 | 5 | 1 | LYS | Lym Sub | APOPTOTIC | ANXV+ | CD45+ANXV+ | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 700 | 10^6/L | 700 | 10^6/L | 700 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

### R59. `ig34_p0212_a002` — r2:TYPO_SIB

- PDF 页 212 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 7 | IM001-123 | CP | 0005 00542 | 7 | 6 | LYS | Lym Sub | VIABLE; APOPTOTIC | ANXV- | CD45+7AAD-ANXV+ | LYM | FSC SSC/CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 665 | 10^6/L | 665 | 10^6/L | 665 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0212.txt` 第 4-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3|       123                00542                                  Sub/Lym                             SSC                            SSC|CD45+                       APOPTOSIS                                                                        FRACTION                 CYTOMETRY   16T04:20
  4|                                                                                                                                                                    COUNT
  5| 7     IM001-    CP       0005      7       1         LYS        Lym Sub      VIABLE;     7AAD-      CD45+7AAD-ANXV+       LYM      FSC         IMMUNOPHENOTYPING   LYM         665       10^6/L     665        10^6/L     665        QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
  6|       123                00542                                               APOPTOTIC   ANXV+                                     SSC|CD45+                       APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
  7|                                                                                                                                                                    COUNT
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:93-93` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  93| | 7 | IM001-123 | CP | 0005 00542 | 7 | 1 | LYS | Lym Sub | VIABLE; APOPTOTIC | 7AAD-ANXV+ | CD45+7AAD-ANXV+ | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 665 | 10^6/L | 665 | 10^6/L | 665 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

### R60. `ig34_p0212_a003` — r2:TYPO_SIB

- PDF 页 212 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 8 | IM001-123 | CP | 0005 00542 | 8 | 6 | LYSLY | Lym Sub/Lym | VIABLE; APOPTOTIC | ANXV- | CD45+7AAD-ANXV+/CD45+FSC SSC |  | FSC SSC/CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 20 | % | 20 | % | 20 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0212.txt` 第 8-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7|                                                                                                                                                                    COUNT
  8| 8     IM001-    CP       0005      8       1         LYSLY      Lym          VIABLE;     7AAD-      CD45+7AAD-            LYM      FSC         IMMUNOPHENOTYPING   LYM         20        %          20         %          20         QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
  9|       123                00542                                  Sub/Lym      APOPTOTIC   ANXV+      ANXV+/CD45+FSC SSC             SSC|CD45+                       APOPTOSIS                                                                        FRACTION                 CYTOMETRY   16T12:20
 10|                                                                                                                                                                    COUNT
 11| 9     IM001-    CP       0005      9       2         LYS        Lym Sub      VIABLE      7AAD-      CD45+7AAD-            LYM      FSC         IMMUNOPHENOTYPING   LYM         3325      10^6/L     3325       10^6/L     3325       QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
 12|       123                00542                                                                                                     SSC|CD45+                       APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:93-94` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  93| | 7 | IM001-123 | CP | 0005 00542 | 7 | 1 | LYS | Lym Sub | VIABLE; APOPTOTIC | 7AAD-ANXV+ | CD45+7AAD-ANXV+ | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 665 | 10^6/L | 665 | 10^6/L | 665 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
  94| | 8 | IM001-123 | CP | 0005 00542 | 8 | 1 | LYSLY | Lym Sub/Lym | VIABLE; APOPTOTIC | 7AAD-ANXV+ | CD45+7AAD-ANXV+/CD45+FSC SSC | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 20 | % | 20 | % | 20 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

### R61. `ig34_p0212_a004` — r2:TYPO_SIB

- PDF 页 212 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 9 | IM001-123 | CP | 0005 00542 | 9 | 2 | LYS | Lym Sub | VIABLE | 7AAD- | CD45+7AAD- | LYM | FSC SSC/CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3325 | 10^6/L | 3325 | 10^6/L | 3325 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0212.txt` 第 10-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  9|       123                00542                                  Sub/Lym      APOPTOTIC   ANXV+      ANXV+/CD45+FSC SSC             SSC|CD45+                       APOPTOSIS                                                                        FRACTION                 CYTOMETRY   16T12:20
 10|                                                                                                                                                                    COUNT
 11| 9     IM001-    CP       0005      9       2         LYS        Lym Sub      VIABLE      7AAD-      CD45+7AAD-            LYM      FSC         IMMUNOPHENOTYPING   LYM         3325      10^6/L     3325       10^6/L     3325       QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
 12|       123                00542                                                                                                     SSC|CD45+                       APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 13|                                                                                                                                                                    COUNT
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:95-95` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  95| | 9 | IM001-123 | CP | 0005 00542 | 9 | 2 | LYS | Lym Sub | VIABLE | 7AAD- | CD45+7AAD- | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 3325 | 10^6/L | 3325 | 10^6/L | 3325 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

### R62. `ig34_p0212_a005` — r2:TYPO_SIB

- PDF 页 212 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 10 | IM001-123 | CP | 0005 00542 | 10 | 2 | LYS | Lym Sub | NON-VIABLE | 7AAD+ | CD45+7AAD+ | LYM | FSC SSC/CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 175 | 10^6/L | 175 | 10^6/L | 175 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0212.txt` 第 13-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12|       123                00542                                                                                                     SSC|CD45+                       APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 13|                                                                                                                                                                    COUNT
 14| 10    IM001-    CP       0005      10      2         LYS        Lym Sub      NON-        7AAD+      CD45+7AAD+            LYM      FSC         IMMUNOPHENOTYPING   LYM         175       10^6/L     175        10^6/L     175        QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
 15|       123                00542                                               VIABLE                                                SSC|CD45+                       APOPTOSIS                                                                        CONCENTRATION            CYTOMETRY   16T12:20
 16|                                                                                                                                                                    COUNT
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:96-96` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  96| | 10 | IM001-123 | CP | 0005 00542 | 10 | 2 | LYS | Lym Sub | NON-VIABLE | 7AAD+ | CD45+7AAD+ | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 175 | 10^6/L | 175 | 10^6/L | 175 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

### R63. `ig34_p0213_a010` — r2:TYPO_SIB

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | ABC-123 | CP | ABCD-001-001 | 3 | 1 | MNS | Mono Sub | NON-PROLIFERATING | Ki67- |  | CD14+Ki67- | MONO FSC+SSC+CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 344 | 10^6/L | 344 | 10^6/L | 344 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 25-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24|                          001-001                                                                                                                                                                                                                                              CONCENTRATION            CYTOMETRY     16T08:00
 25| 3     ABC-123   CP       ABCD-     3       1         MNS        Mono Sub                   NON-            Ki67-      CD14+Ki67-              MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTES    344       10^6/L     344        10^6/L     344        QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 26|                          001-001                                                           PROLIFERATING                                                                                                                                                                      CONCENTRATION            CYTOMETRY     16T08:00
 27| 4     ABC-123   CP       ABCD-     4       1         MNSMN      Mono                       PROLIFERATING   Ki67+      CD14+Ki67+/CD14+        MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTES    12.69     %          12.69      %          12.69      QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:131-131` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 131| | 3 | ABC-123 | CP | ABCD-001-001 | 3 | 1 | MNS | Mono Sub | | NON-PROLIFERATING | Ki67- | CD14+Ki67- | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 344 | 10^6/L | 344 | 10^6/L | 344 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

### R64. `ig34_p0213_a015` — r2:TYPO_SIB

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 8 | ABC-123 | CP | ABCD-001-001 | 8 | 2 | MNS | Mono Sub | CDxx+CDyy- |  |  | CD14+CDxx+CDyy- | MONO FSC+SSC+CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 368 | 10^6/L | 368 | 10^6/L | 368 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 35-36 行 (自动定位, 词覆盖 0.97; 版式以原 PDF 为准):

~~~~
 34| 7     ABC-123   CP       ABCD-     7       2         MONO       Monocytes                                             CD14+                   MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     394       10^6/L     394        10^6/L     394        QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 35|                          001-001                                                                                                                                                            CD SUBSETS                                                                        CONCENTRATION            CYTOMETRY     16T08:00
 36| 8     ABC-123   CP       ABCD-     8       2         MNS        Mono Sub      CDxx+CDyy-                              CD14+CDxx+CDyy-         MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     366       10^6/L     366        10^6/L     366        QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 37|                          001-001                                                                                                                                                            CD SUBSETS                                                                        CONCENTRATION            CYTOMETRY     16T08:00
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:136-136` (来源: fuzzy locate (score 0.97)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 136| | 8 | ABC-123 | CP | ABCD-001-001 | 8 | 2 | MNS | Mono Sub | CDxx+CDyy- | | | CD14+CDxx+CDyy- | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 366 | 10^6/L | 366 | 10^6/L | 366 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

### R65. `ig34_p0213_a016` — r2:TYPO_SIB

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 9 | ABC-123 | CP | ABCD-001-001 | 9 | 2 | MNS | Mono Sub | CDxx-CDyy+ |  |  | CD14+CDxx-CDyy+ | MONO FSC+SSC+CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 20 | 10^6/L | 20 | 10^6/L | 20 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 37-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36| 8     ABC-123   CP       ABCD-     8       2         MNS        Mono Sub      CDxx+CDyy-                              CD14+CDxx+CDyy-         MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     366       10^6/L     366        10^6/L     366        QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 37|                          001-001                                                                                                                                                            CD SUBSETS                                                                        CONCENTRATION            CYTOMETRY     16T08:00
 38| 9     ABC-123   CP       ABCD-     9       2         MNS        Mono Sub      CDxx-CDyy+                              CD14+CDxx-CDyy+         MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     20        10^6/L     20         10^6/L     20         QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 39|                          001-001                                                                                                                                                            CD SUBSETS                                                                        CONCENTRATION            CYTOMETRY     16T08:00
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:137-137` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 137| | 9 | ABC-123 | CP | ABCD-001-001 | 9 | 2 | MNS | Mono Sub | CDxx-CDyy+ | | | CD14+CDxx-CDyy+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 20 | 10^6/L | 20 | 10^6/L | 20 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

### R66. `ig34_p0213_a019` — r2:TYPO_SIB

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 12 | ABC-123 | CP | ABCD-001-001 | 12 | 3 | MNS | Mono Sub | CDxx+CDyy+ | APOPTOTIC | ANXV+ | CD14+CDxx+CDyy-ANXV+ | MONO FSC+SSC+CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 5 | 10^6/L | 5 | 10^6/L | 5 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 44-45 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 43|                          001-001                                Sub/Mono                                              CDyy+/CD14+                                                           CD SUBSETS                                                                        FRACTION                 CYTOMETRY     16T08:00
 44| 12    ABC-123   CP       ABCD-     12      3         MNS        Mono Sub      CDxx+CDyy-   APOPTOTIC       ANXV+      CD14+CDxx+CDyy-         MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTE     5         10^6/L     5          10^6/L     5          QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 45|                          001-001                                                                                      ANXV+                                                                 CD SUBSETS                                                                        CONCENTRATION            CYTOMETRY     16T08:00
 46| 
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:140-140` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 140| | 12 | ABC-123 | CP | ABCD-001-001 | 12 | 3 | MNS | Mono Sub | CDxx+CDyy- | APOPTOTIC | ANXV+ | CD14+CDxx+CDyy-ANXV+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTE CD SUBSETS | 5 | 10^6/L | 5 | 10^6/L | 5 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

### R67. `ig34_p0225_a012` — r2:TYPO_SIB

- PDF 页 225 · 原子类型 SENTENCE · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-GF T-1`: PDF 写 "inheritabilty" → KB 写 "inheritability" (处理: KB 写正确值; 依据: p225 Ex2 拼作 inheritability; KB `knowledge_base/domains/GF/examples.md:5`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example shows findings from an assessment of a known single nucleotide variant in gene ABCG2 using wet laboratory methodology real-time polymerase chain reaction. Findings from this assessment show the genotypes from DNA extracted from the blood of 3 individuals, each with a different genotype at the genetic locus of interest. Because the DNA specimen was extracted from normal blood, the inheritability of the variation is considered to be in the germline.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0225.txt` 第 45-47 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 44| Example 2
 45| This example shows findings from an assessment of a known single nucleotide variant in gene ABCG2 using wet laboratory methodology real-time polymerase chain reaction. Findings from this assessment show the
 46| genotypes from DNA extracted from the blood of 3 individuals, each with a different genotype at the genetic locus of interest. Because the DNA specimen was extracted from normal blood, the inheritability of the
 47| variation is considered to be in the germline.
 48| Row 1:                     Shows a subject genotype which is homozygous for the variant nucleotide in the reference sequence.
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:52` (来源: live valid_hits):

~~~~
  52| This example shows findings from an assessment of a known single nucleotide variant in gene ABCG2 using wet laboratory methodology real-time polymerase chain reaction. Findings from this assessment show the genotypes from DNA extracted from the blood of 3 individuals, each with a different genotype at the genetic locus of interest. Because the DNA specimen was extracted from normal blood, the inheritability of the variation is considered to be in the germline.
~~~~

### R68. `ig34_p0236_a002` — r2:TYPO_SIB

- PDF 页 236 · 原子类型 SENTENCE · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-IS T-3`: PDF 写 "NON-STUDY RELATED IMMUNOGENICITY" → KB 写 "NON-STUDY-RELATED" (处理: KB 写正确值; 依据: 同表 ISCAT 与叙述 3 处; KB `knowledge_base/domains/IS/examples.md:108`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example illustrates the use of the CDISC-recommended ISCAT values "STUDY VACCINE-RELATED IMMUNOGENICITY" and "NON-STUDY-RELATED IMMUNOGENICITY" to distinguish between study vaccine-induced immunogenicity and immunogenicity findings unrelated to the study vaccine data collected during a vaccine study. ISCAT = "NON-STUDY-RELATED IMMUNOGENICITY" was developed to explicitly and purposefully indicate whether an observed immunity toward an antigen was not related to the study vaccine but rather was a result of natural infection or previous vaccination. Oftentimes, it is simply impossible to tell whether the antibody found in a subject is due to a natural infection or previous vaccination (or both)—yet this immunogenicity, unrelated to the study vaccine, is important for collection and assessment at the screening phase of the trial.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 3-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| vaccine study, immunological data pertaining to RSV-protein B was collected for the subject.
  3| This example illustrates the use of the CDISC-recommended ISCAT values "STUDY VACCINE-RELATED IMMUNOGENICITY" and "NON-STUDY-RELATED IMMUNOGENICITY" to distinguish between
  4| study vaccine-induced immunogenicity and immunogenicity findings unrelated to the study vaccine data collected during a vaccine study. ISCAT = "NON-STUDY-RELATED IMMUNOGENICITY" was
  5| developed to explicitly and purposefully indicate whether an observed immunity toward an antigen was not related to the study vaccine but rather was a result of natural infection or previous vaccination. Oftentimes,
  6| it is simply impossible to tell whether the antibody found in a subject is due to a natural infection or previous vaccination (or both)—yet this immunogenicity, unrelated to the study vaccine, is important for collection
  7| and assessment at the screening phase of the trial.
  8| In this example, immune responses against RSV-protein Z were measured during the study. Because protein Z is not inserted into the vaccine vector, any immune response detected toward protein Z was not related
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:103` (来源: live valid_hits):

~~~~
 103| This example illustrates the use of the CDISC-recommended ISCAT values "STUDY VACCINE-RELATED IMMUNOGENICITY" and "NON-STUDY-RELATED IMMUNOGENICITY" to distinguish between study vaccine-induced immunogenicity and immunogenicity findings unrelated to the study vaccine data collected during a vaccine study. ISCAT = "NON-STUDY-RELATED IMMUNOGENICITY" was developed to explicitly and purposefully indicate whether an observed immunity toward an antigen was not related to the study vaccine but rather was a result of natural infection or previous vaccination. Oftentimes, it is simply impossible to tell whether the antibody found in a subject is due to a natural infection or previous vaccination (or both)—yet this immunogenicity, unrelated to the study vaccine, is important for collection and assessment at the screening phase of the trial.
~~~~

### R69. `ig34_p0236_a003` — r2:TYPO_SIB

- PDF 页 236 · 原子类型 SENTENCE · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-IS T-3`: PDF 写 "NON-STUDY RELATED IMMUNOGENICITY" → KB 写 "NON-STUDY-RELATED" (处理: KB 写正确值; 依据: 同表 ISCAT 与叙述 3 处; KB `knowledge_base/domains/IS/examples.md:108`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this example, immune responses against RSV-protein Z were measured during the study. Because protein Z is not inserted into the vaccine vector, any immune response detected toward protein Z was not related to the study vaccine, although important for assessment and collected per the study protocol. In order to show that RSV-protein Z-induced antibody production was unrelated to the immunity solicited by the study vaccine RSV-protein B (ISCAT = "STUDY VACCINE-RELATED IMMUNOGENICITY"), the ISCAT for rows 3 and 4 is "NON-STUDY-RELATED IMMUNOGENICITY" (note: protein Z and protein B are examples, refer to controlled terminology for standard terms associated with ISBDAGNT).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 8-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7| and assessment at the screening phase of the trial.
  8| In this example, immune responses against RSV-protein Z were measured during the study. Because protein Z is not inserted into the vaccine vector, any immune response detected toward protein Z was not related
  9| to the study vaccine, although important for assessment and collected per the study protocol. In order to show that RSV-protein Z-induced antibody production was unrelated to the immunity solicited by the study
 10| vaccine RSV-protein B (ISCAT = "STUDY VACCINE-RELATED IMMUNOGENICITY"), the ISCAT for rows 3 and 4 is “NON-STUDY-RELATED IMMUNOGENICITY” (note: protein Z and protein B are
 11| examples, refer to controlled terminology for standard terms associated with ISBDAGNT).
 12| Rows 1-2:          Show the screening and quantification of microbial-induced immunoglobulin G (IgG) antibody against the RSV-protein B at baseline, prior to the administration of the study vaccine.
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:105` (来源: live valid_hits):

~~~~
 105| In this example, immune responses against RSV-protein Z were measured during the study. Because protein Z is not inserted into the vaccine vector, any immune response detected toward protein Z was not related to the study vaccine, although important for assessment and collected per the study protocol. In order to show that RSV-protein Z-induced antibody production was unrelated to the immunity solicited by the study vaccine RSV-protein B (ISCAT = "STUDY VACCINE-RELATED IMMUNOGENICITY"), the ISCAT for rows 3 and 4 is “NON-STUDY-RELATED IMMUNOGENICITY” (note: protein Z and protein B are examples, refer to controlled terminology for standard terms associated with ISBDAGNT).
~~~~

### R70. `ig34_p0236_a009` — r2:TYPO_SIB

- PDF 页 236 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-IS`
- 登记 `B-IS T-1`: PDF 写 "Ex5 r6 STUDYID RSC1230" → KB 写 "RSV1230" (处理: KB 写正确值; 依据: 同列其余 RSV1230; USUBJID RSV1230-011; KB `knowledge_base/domains/IS/examples.md:120`)
- 登记 `B-IS T-2`: PDF 写 "Ex5 r7 STUDYID RSC1230" → KB 写 "RSV1230" (处理: KB 写正确值; 依据: 同 T-1; KB `knowledge_base/domains/IS/examples.md:121`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | 1 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | SCREEN | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | POSITIVE | POSITIVE | | | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 22-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 21| Row STUDYID DOMAIN USUBJID           ISSEQ   ISREFID ISGRPID   ISTESTCD ISTEST               ISBDAGNT                  ISTSTOPO ISCAT                   ISSCAT     ISORRES ISSTRESC ISSTRESN ISSTRESU ISSPEC ISMETHOD VISITNUM VISIT    ISDTC
 22| 1   RSV1230 IS     RSV1230-          1       13668   1         MBIGGAB Microbial-induced     HUMAN RESPIRATORY         SCREEN   STUDY VACCINE-RELATED   HUMORAL    POSITIVE POSITIVE                  SERUM ELISA     1        BASELINE 2017-
 23|                    011                                                  IgG Antibody         SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                        05-27
 24|                                                                                              B
 25| 2        RSV1230   IS     RSV1230-   2       13668   1         MBIGGAB   Microbial-induced   HUMAN RESPIRATORY         QUANTIFY STUDY VACCINE-RELATED   HUMORAL    1:25     25         25    titer    SERUM   ELISA   1        BASELINE 2017-
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:115` (来源: decision.evidence.hit):

~~~~
 115| | 1 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | 1 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | SCREEN | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | POSITIVE | POSITIVE | | | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
~~~~

### R71. `ig34_p0236_a011` — r2:TYPO_SIB

- PDF 页 236 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-IS`
- 登记 `B-IS T-3`: PDF 写 "NON-STUDY RELATED IMMUNOGENICITY" → KB 写 "NON-STUDY-RELATED" (处理: KB 写正确值; 依据: 同表 ISCAT 与叙述 3 处; KB `knowledge_base/domains/IS/examples.md:108`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | 2 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN Z | SCREEN | NON-STUDY-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | POSITIVE | POSITIVE | | | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 28-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27|                                                                                              B
 28| 3        RSV1230   IS     RSV1230-   1       13668   2         MBIGGAB   Microbial-induced   HUMAN RESPIRATORY         SCREEN   NON-STUDY-RELATED       HUMORAL    POSITIVE POSITIVE                  SERUM   ELISA   1        BASELINE 2017-
 29|                           011                                            IgG Antibody        SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                        05-27
 30|                                                                                              Z
 31| 4        RSV1230   IS     RSV1230-   2       13668   2         MBIGGAB   Microbial-induced   HUMAN RESPIRATORY         QUANTIFY NON-STUDY-RELATED       HUMORAL    1:120    120        120   titer    SERUM   ELISA   1        BASELINE 2017-
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:117` (来源: decision.evidence.hit):

~~~~
 117| | 3 | RSV1230 | IS | RSV1230-011 | 1 | 13668 | 2 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN Z | SCREEN | NON-STUDY-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | POSITIVE | POSITIVE | | | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
~~~~

### R72. `ig34_p0236_a013` — r2:TYPO_SIB

- PDF 页 236 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-IS`
- 登记 `B-IS T-1`: PDF 写 "Ex5 r6 STUDYID RSC1230" → KB 写 "RSV1230" (处理: KB 写正确值; 依据: 同列其余 RSV1230; USUBJID RSV1230-011; KB `knowledge_base/domains/IS/examples.md:120`)
- 登记 `B-IS T-2`: PDF 写 "Ex5 r7 STUDYID RSC1230" → KB 写 "RSV1230" (处理: KB 写正确值; 依据: 同 T-1; KB `knowledge_base/domains/IS/examples.md:121`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 5 | RSV1230 | IS | RSV1230-011 | 1 | 13669 | | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:90 | 90 | 90 | titer | SERUM | ELISA | 2 | VISIT 1 | 2017-07-27 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 34-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 33|                                                                                              Z
 34| 5        RSV1230   IS     RSV1230-   1       13669             MBIGGAB   Microbial-induced   HUMAN RESPIRATORY         QUANTIFY STUDY VACCINE-RELATED   HUMORAL    1:90     90         90    titer    SERUM   ELISA   2        VISIT 1    2017-
 35|                           011                                            IgG Antibody        SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                          07-27
 36|                                                                                              B
 37| 6        RSC1230   IS     RSV1230-   2       13670             MBIGGAB   Microbial-induced   HUMAN RESPIRATORY         QUANTIFY STUDY VACCINE-RELATED   HUMORAL    1:220    220        220   titer    SERUM   ELISA   3        VISIT 2    2017-
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:119` (来源: decision.evidence.hit):

~~~~
 119| | 5 | RSV1230 | IS | RSV1230-011 | 1 | 13669 | | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:90 | 90 | 90 | titer | SERUM | ELISA | 2 | VISIT 1 | 2017-07-27 |
~~~~

### R73. `ig34_p0261_a010` — r2:TYPO_SIB

- PDF 页 261 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-MB T-1`: PDF 写 "Ex3 suppmb Row 列 1,2,3,4,7,8" → KB 写 "5, 6" (处理: KB 写正确值; 依据: Row 跳号, 行内容按 PDF; KB `knowledge_base/domains/MB/examples.md:204`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5 | ABC | ABC-01-101 | 100.4 | LAVAGE FLUID | 100 | 2
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0261.txt` 第 13-13 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12| 4      ABC         ABC-01-101    100.3    LAVAGE FLUID      100         2
 13| 5      ABC         ABC-01-101    100.4    LAVAGE FLUID      100         2
 14| 6      ABC         ABC-01-101    100.5    LAVAGE FLUID      100         2
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:168` (来源: live valid_hits):

~~~~
 168| | 5 | ABC | ABC-01-101 | 100.4 | LAVAGE FLUID | 100 | 2 |
~~~~

### R74. `ig34_p0262_a003` — r2:TYPO_SIB

- PDF 页 262 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-MB`
- 登记 `B-MB T-2`: PDF 写 "Ex4 表头 MBGPRID" → KB 写 "MBGRPID" (处理: KB 写正确值; 依据: 标准变量名; KB `knowledge_base/domains/MB/examples.md:241`)
- 登记 `B-MB T-3`: PDF 写 "Ex4 表头 MBTRESN" → KB 写 "MBSTRESN" (处理: KB 写正确值; 依据: spec 无 MBTRESN; r2 值=MBSTRESC 数值; KB `knowledge_base/domains/MB/examples.md:241`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row | STUDYID | DOMAIN | USUBJID | SPDEVID | MBSEQ | MBGRPID | MBLNKGRP | MBREFID | MBTESTCD | MBTEST | MBTSTDTL | MBORRES | MBORRESU | MBRSLSCL | MBSTRESC | MBSTRESN | MBSTRESU | MBLOC | MBSPCCND | MBMETHOD | VISITNUM | VISIT | MBDTC
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0262.txt` 第 4-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3| mb.xpt
  4| Row   STUDYID   DOMAIN   USUBJID   SPDEVID   MBSEQ    MBGRPID   MBLNKGRP   MBREFID   MBTESTCD    MBTEST                 MBTSTDTL     MBORRES     MBORRESU      MBRSLSCL   MBSTRESC   MBSTRESN     MBSTRESU    MBLOC         MBSPCCND       MBMETHOD             VISITNUM   VISIT   MBDTC
  5| 1     ABC       MB       ABC-01-             1        1                    100.1     AFB         Acid-Fast Bacilli      DETECTION    PRESENT                   Ord        PRESENT                             STOMACH       CONCENTRATED   ZIEHL NEELSEN ACID   1          WEEK    2011-01-
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:187` (来源: decision.evidence.hit):

~~~~
 187| | Row | STUDYID | DOMAIN | USUBJID | SPDEVID | MBSEQ | MBGRPID | MBLNKGRP | MBREFID | MBTESTCD | MBTEST | MBTSTDTL | MBORRES | MBORRESU | MBRSLSCL | MBSTRESC | MBSTRESN | MBSTRESU | MBLOC | MBSPCCND | MBMETHOD | VISITNUM | VISIT | MBDTC |
~~~~

### R75. `ig34_p0262_a008` — r2:TYPO_SIB

- PDF 页 262 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-MB T-1`: PDF 写 "Ex3 suppmb Row 列 1,2,3,4,7,8" → KB 写 "5, 6" (处理: KB 写正确值; 依据: Row 跳号, 行内容按 PDF; KB `knowledge_base/domains/MB/examples.md:204`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5 | ABC | MB | ABC-01-101 | | 5 | 2 | | 100.3 | MTB | Mycobacterium tuberculosis | COLONY COUNT | 147 | CFU | Qn | 14700 | 14700 | CFU/mL | STOMACH | | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0262.txt` 第 13-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12|                          101                                                                     tuberculosis                                                                                                                              SOLID                           1       17T06:00
 13| 5     ABC       MB       ABC-01-             5        2         1          100.3     MTB         Mycobacterium          COLONY       147         CFU           Qn         14700      14700        CFU/mL      STOMACH                      MICROBIAL CULTURE,   1          WEEK    2011-01-
 14|                          101                                                                     tuberculosis           COUNT                                                                                                              SOLID                           1       17T06:00
 15| 6     ABC       MB       ABC-01-             6        2         1          100.3     MTB         Mycobacterium          COLONY       2+                        Ord        2+                                  STOMACH                      MICROBIAL CULTURE,   1          WEEK    2011-01-
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:193-193` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 193| | 5 | ABC | MB | ABC-01-101 | | 5 | 2 | 1 | 100.3 | MTB | Mycobacterium tuberculosis | COLONY COUNT | 147 | CFU | Qn | 14700 | 14700 | CFU/mL | STOMACH | | MICROBIAL CULTURE, SOLID | 1 | WEEK 1 | 2011-01-17T06:00 |
~~~~

### R76. `ig34_p0262_a019` — r2:TYPO_SIB

- PDF 页 262 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-MS T-2`: PDF 写 "Rows 3-4 MSCONU" → KB 写 "MSCONCU" (处理: KB 写正确值; 依据: 同句前文与 Rows 1-2; KB `knowledge_base/domains/MS/examples.md:65`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-2: Show phenotypic testing results on 2 separate culture plates: 1 with medium containing rifampicin (row 1) and 1 with medium containing isoniazid (row 2). MSAGENT is populated with the name of the drug being used in the susceptibility test. The variables MSCONC and MSCONCU represent the concentration and units of the drug being used. The culture start and stop dates are represented in BE and can be linked to MS by BELNKID and MSLNKID.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0262.txt` 第 32-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| results may be categorized as susceptible or resistant. In this example, the variable NHOID (Non-host Organism Identifier) is populated with the name of the organism that is the subject of the test.
 32| Rows 1-2:        Show phenotypic testing results on 2 separate culture plates: 1 with medium containing rifampicin (row 1) and 1 with medium containing isoniazid (row 2). MSAGENT is populated with the name of
 33|                  the drug being used in the susceptibility test. The variables MSCONC and MSCONCU represent the concentration and units of the drug being used. The culture start and stop dates are represented in BE
 34|                  and can be linked to MS by BELNKID and MSLNKID.
 35| Rows 3-4:        Show genotypic susceptibility testing results on the same aliquot from a NAAT that looks for mutations that confer resistance to 2 drugs. MSAGENT should be populated with the name of the drug
~~~~

KB 现文: `knowledge_base/domains/MS/examples.md:64` (来源: live valid_hits):

~~~~
  64| **Rows 1-2:** Show phenotypic testing results on 2 separate culture plates: 1 with medium containing rifampicin (row 1) and 1 with medium containing isoniazid (row 2). MSAGENT is populated with the name of the drug being used in the susceptibility test. The variables MSCONC and MSCONCU represent the concentration and units of the drug being used. The culture start and stop dates are represented in BE and can be linked to MS by BELNKID and MSLNKID.
~~~~

### R77. `ig34_p0262_a022` — r2:TYPO_SIB

- PDF 页 262 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-MS T-2`: PDF 写 "Rows 3-4 MSCONU" → KB 写 "MSCONCU" (处理: KB 写正确值; 依据: 同句前文与 Rows 1-2; KB `knowledge_base/domains/MS/examples.md:65`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row | STUDYID | DOMAIN | USUBJID | SPDEVID | NHOID | MSSEQ | MSREFID | MSLNKID | MSTESTCD | MSTEST | MSAGENT | MSCONC | MSCONCU | MSORRES | MSSTRESC | MSSPEC | MSLOC | MSMETHOD | MSDTC
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0262.txt` 第 39-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38| ms.xpt
 39| Row STUDYID DOMAIN USUBJID             SPDEVID NHOID                           MSSEQ MSREFID MSLNKID MSTESTCD MSTEST                              MSAGENT MSCONC MSCONCU MSORRES                        MSSTRESC
 40|                                                                                                                                                                                                                MSSPEC                  MSLOC   MSMETHOD                        MSDTC
 41| 1   ABC     MS     ABC-01-                     MYCOBACTERIUM                   1     100.4   2       MICROSUS Microbial                           Rifampicin 1   ug/mL   RESISTANT                      RESISTANT
~~~~

KB 现文: `knowledge_base/domains/MS/examples.md:69` (来源: live valid_hits):

~~~~
  69| | Row | STUDYID | DOMAIN | USUBJID | SPDEVID | NHOID | MSSEQ | MSREFID | MSLNKID | MSTESTCD | MSTEST | MSAGENT | MSCONC | MSCONCU | MSORRES | MSSTRESC | MSSPEC | MSLOC | MSMETHOD | MSDTC |
~~~~

