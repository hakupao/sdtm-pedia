# T4.1 第二轮补检包 5 — TYPO_SIB (13 条; 编号 R78-R90)

> 由 `scripts/t4/t4_round2_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 R).

### R78. `ig34_p0263_a013` — r2:TYPO_SIB

- PDF 页 263 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-MB`
- 登记 `B-MB T-1`: PDF 写 "Ex3 suppmb Row 列 1,2,3,4,7,8" → KB 写 "5, 6" (处理: KB 写正确值; 依据: Row 跳号, 行内容按 PDF; KB `knowledge_base/domains/MB/examples.md:204`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5 | ABC | MB | | MBREFID | | ONE | C
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0263.txt` 第 15-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| 4        ABC       MS              MSLNKID           ONE                     B
 15| 5        ABC       MB              MBREFID           ONE                     C
 16| 6        ABC       MS              MSREFID           MANY                    C
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:228` (来源: decision.evidence.hit):

~~~~
 228| | 5 | ABC | MB | | MBREFID | | ONE | C |
~~~~

### R79. `ig34_p0266_a016` — r2:TYPO_SIB

- PDF 页 266 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.8 Microscopic Findings (MI)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-MI T-1`: PDF 写 "Ex3 表头 MIDRVL" → KB 写 "MIDRVFL" (处理: KB 写正确值; 依据: Ex2 同列 MIDRVFL; --DRVFL; KB `knowledge_base/domains/MI/examples.md:50`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row | STUDYID | DOMAIN | USUBJID | MISEQ | MIGRPID | MITESTCD | MITEST | MITSTDTL | MIORRES | MISTRESC | MISTRESN | MISPEC | MILOC | MIMETHOD | MIDRVFL | VISIT | MIDTC
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0266.txt` 第 25-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24| mi.xpt
 25| Row STUDYID DOMAIN USUBJID MISEQ MIGRPID MITESTCD MITEST                 MITSTDTL        MIORRES MISTRESC   MISTRESN MISPEC MILOC  MIMETHOD MIDRVFL VISIT     MIDTC
 26| 1   ABC     MI     ABC-    1     1       ESTRCPT Estrogen                ALLRED          3       3          3        TISSUE BREAST IHC              SCREENING 2001-
~~~~

KB 现文: `knowledge_base/domains/MI/examples.md:27` (来源: live valid_hits):

~~~~
  27| | Row | STUDYID | DOMAIN | USUBJID | MISEQ | MIGRPID | MITESTCD | MITEST | MITSTDTL | MIORRES | MISTRESC | MISTRESN | MISPEC | MILOC | MIMETHOD | MIDRVFL | VISIT | MIDTC |
~~~~

### R80. `ig34_p0277_a025` — r2:TYPO_SIB

- PDF 页 277 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 1`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-PCPP T-2`: PDF 写 "Method B r13 RDOMAIN PC" → KB 写 "PP" (处理: KB 写正确值; 依据: IDVAR PPGRPID / IDVARVAL 为 PP 侧; KB `knowledge_base/domains/PC/examples.md:103`)
- 登记 `B-PCPP T-3`: PDF 写 "Method B r26 RDOMAIN PC" → KB 写 "PP" (处理: KB 写正确值; 依据: 同 T-2; KB `knowledge_base/domains/PC/examples.md:116`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0277.txt` 第 26-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25| 1     ABC-123    PC         ABC-123-0001    PCGRPID     DY1_DRGX                  1
 26| 2     ABC-123    PP         ABC-123-0001    PPGRPID     DY1DRGX                   1
 27| 3     ABC-123    PC         ABC-123-0001    PPGRPID     DY8_DRGX                  2
~~~~

KB 现文: `knowledge_base/domains/PP/examples.md:14-17` (来源: fuzzy locate (score 0.875)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  14| | Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | VISITNUM | VISIT | PPDTC | PPRFTDTC |
  15| |-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|----------|
  16| | 1 | ABC-123 | PP | ABC-123-0001 | 1 | DAY1_PAR | TMAX | Time of CMAX | DRUG A PARENT | 1.87 | h | 1.87 | 1.87 | h | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
  17| | 2 | ABC-123 | PP | ABC-123-0001 | 2 | DAY1_PAR | CMAX | Max Conc | DRUG A PARENT | 44.5 | ug/L | 44.5 | 44.5 | ug/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
~~~~

### R81. `ig34_p0277_a026` — r2:TYPO_SIB

- PDF 页 277 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 1`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-PCPP T-1`: PDF 写 "Method A r3 IDVAR PPGRPID" → KB 写 "PCGRPID" (处理: KB 写正确值; 依据: RDOMAIN PC 配 PCGRPID 值; KB `knowledge_base/domains/PC/examples.md:79`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
3 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY8_DRGX | | 2
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0277.txt` 第 25-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24| Row   STUDYID    RDOMAIN    USUBJID         IDVAR       IDVARVAL      RELTYPE     RELID
 25| 1     ABC-123    PC         ABC-123-0001    PCGRPID     DY1_DRGX                  1
 26| 2     ABC-123    PP         ABC-123-0001    PPGRPID     DY1DRGX                   1
 27| 3     ABC-123    PC         ABC-123-0001    PPGRPID     DY8_DRGX                  2
 28| 4     ABC-123    PP         ABC-123-0001    PPGRPID     DY8DRGX                   2
~~~~

KB 现文: `knowledge_base/domains/PP/examples.md:17-18` (来源: fuzzy locate (score 0.556)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  17| | 2 | ABC-123 | PP | ABC-123-0001 | 2 | DAY1_PAR | CMAX | Max Conc | DRUG A PARENT | 44.5 | ug/L | 44.5 | 44.5 | ug/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
  18| | 3 | ABC-123 | PP | ABC-123-0001 | 3 | DAY1_PAR | AUCALL | AUC All | DRUG A PARENT | 294.7 | h*mg/L | 294.7 | 294.7 | h*mg/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
~~~~

### R82. `ig34_p0278_a015` — r2:TYPO_SIB

- PDF 页 278 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 1`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-PCPP T-2`: PDF 写 "Method B r13 RDOMAIN PC" → KB 写 "PP" (处理: KB 写正确值; 依据: IDVAR PPGRPID / IDVARVAL 为 PP 侧; KB `knowledge_base/domains/PC/examples.md:103`)
- 登记 `B-PCPP T-3`: PDF 写 "Method B r26 RDOMAIN PC" → KB 写 "PP" (处理: KB 写正确值; 依据: 同 T-2; KB `knowledge_base/domains/PC/examples.md:116`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
13 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0278.txt` 第 15-15 行 (自动定位, 词覆盖 0.875; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 14| 12     ABC-123     PC          ABC-123-0001    PCSEQ     12                     1
 15| 13     ABC-123     PC          ABC-123-0001    PPGRPID   DY1DRGX                1
 16| 14     ABC-123     PC          ABC-123-0001    PCSEQ     13                     1
~~~~

KB 现文: `knowledge_base/domains/PP/examples.md:28-28` (来源: fuzzy locate (score 0.75)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  28| | 13 | ABC-123 | PP | ABC-123-0001 | 13 | DAY11_PAR | TMAX | Time of CMAX | DRUG A PARENT | 1.91 | h | 1.91 | 1.91 | h | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
~~~~

### R83. `ig34_p0278_a028` — r2:TYPO_SIB

- PDF 页 278 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 1`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-PCPP T-2`: PDF 写 "Method B r13 RDOMAIN PC" → KB 写 "PP" (处理: KB 写正确值; 依据: IDVAR PPGRPID / IDVARVAL 为 PP 侧; KB `knowledge_base/domains/PC/examples.md:103`)
- 登记 `B-PCPP T-3`: PDF 写 "Method B r26 RDOMAIN PC" → KB 写 "PP" (处理: KB 写正确值; 依据: 同 T-2; KB `knowledge_base/domains/PC/examples.md:116`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
26 | ABC-123 | PP | ABC-123-0001 | PPGRPID | DY1DRGX | | 1
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0278.txt` 第 28-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27| 25     ABC-123     PC          ABC-123-0001    PCSEQ     24                     1
 28| 26     ABC-123     PC          ABC-123-0001    PPGRPID   DY1DRGX                1
 29| 
 30| 
 31| Method C (Many to One, Using PCGRPID and PPSEQ)
 32| Rows 1-8:    The relationship with RELID = "1" includes all PC records with a PCGRPID = "DY1_DRGX" and PP
 33|              records with PPSEQ values "1" through "7".
~~~~

KB 现文: `knowledge_base/domains/PP/examples.md:14-16` (来源: fuzzy locate (score 0.75)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  14| | Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | VISITNUM | VISIT | PPDTC | PPRFTDTC |
  15| |-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|----------|
  16| | 1 | ABC-123 | PP | ABC-123-0001 | 1 | DAY1_PAR | TMAX | Time of CMAX | DRUG A PARENT | 1.87 | h | 1.87 | 1.87 | h | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
~~~~

### R84. `ig34_p0278_a042` — r2:TYPO_SIB

- PDF 页 278 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 1`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-PCPP T-1`: PDF 写 "Method A r3 IDVAR PPGRPID" → KB 写 "PCGRPID" (处理: KB 写正确值; 依据: RDOMAIN PC 配 PCGRPID 值; KB `knowledge_base/domains/PC/examples.md:79`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
9 | ABC-123 | PC | ABC-123-0001 | PCGRPID | DY8_DRGX | | 2
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0278.txt` 第 46-46 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 45| 8      ABC-123     PP          ABC-123-0001    PPSEQ     7                      1
 46| 9      ABC-123     PC          ABC-123-0001    PCGRPID   DY8_DRGX               2
 47| 10     ABC-123     PP          ABC-123-0001    PPSEQ     8                      2
~~~~

KB 现文: `knowledge_base/domains/PP/examples.md:17-20` (来源: fuzzy locate (score 0.556)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  17| | 2 | ABC-123 | PP | ABC-123-0001 | 2 | DAY1_PAR | CMAX | Max Conc | DRUG A PARENT | 44.5 | ug/L | 44.5 | 44.5 | ug/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
  18| | 3 | ABC-123 | PP | ABC-123-0001 | 3 | DAY1_PAR | AUCALL | AUC All | DRUG A PARENT | 294.7 | h*mg/L | 294.7 | 294.7 | h*mg/L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
  19| | 4 | ABC-123 | PP | ABC-123-0001 | 4 | DAY1_PAR | LAMZHL | Half-Life Lambda z | DRUG A PARENT | 0.75 | h | 0.75 | 0.75 | h | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
  20| | 5 | ABC-123 | PP | ABC-123-0001 | 5 | DAY1_PAR | VZO | Vz Obs | DRUG A PARENT | 10.9 | L | 10.9 | 10.9 | L | PLASMA | 1 | DAY 1 | 2001-03-01 | 2001-02-01T08:00 |
~~~~

### R85. `ig34_p0279_a007` — r2:TYPO_SIB

- PDF 页 279 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 1`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-PCPP T-2`: PDF 写 "Method B r13 RDOMAIN PC" → KB 写 "PP" (处理: KB 写正确值; 依据: IDVAR PPGRPID / IDVARVAL 为 PP 侧; KB `knowledge_base/domains/PC/examples.md:103`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
13 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 | | 1
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0279.txt` 第 8-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7| 12     ABC-123    PC          ABC-123-0001    PCSEQ    12                       1
  8| 13     ABC-123    PP          ABC-123-0001    PPSEQ    1                        1
  9| 14     ABC-123    PP          ABC-123-0001    PPSEQ    2                        1
~~~~

KB 现文: `knowledge_base/domains/PP/examples.md:28-28` (来源: fuzzy locate (score 0.857)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  28| | 13 | ABC-123 | PP | ABC-123-0001 | 13 | DAY11_PAR | TMAX | Time of CMAX | DRUG A PARENT | 1.91 | h | 1.91 | 1.91 | h | PLASMA | 2 | DAY 11 | 2001-03-01 | 2001-02-11T08:00 |
~~~~

### R86. `ig34_p0281_a047` — r2:TYPO_SIB

- PDF 页 281 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 3`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-SPC2 PCPP T-11`: PDF 写 ""1 through "7" (引号错位)" → KB 写 ""1" through "7"" (处理: KB 写正确值; 依据: p278 Ex1 Method D 同型句; KB `knowledge_base/domains/PC/examples.md:250`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 18-29:	The relationship with RELID "2" includes PC records with PCSEQ values of "1" through "7" and "10" through "12" and PP records with PPSEQ values "4" and "5".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0281.txt` 第 56-57 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 55|                  PP records with PPSEQ values "1" through "3" and "6" and "7".
 56| Rows 18-29: The relationship with RELID "2" includes PC records with PCSEQ values of "1" through "7" and
 57|             "10" through "12" and PP records with PPSEQ values "4" and "5".
 58| relrec.xpt
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### R87. `ig34_p0357_a014` — r2:TYPO_SIB

- PDF 页 357 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-TR T-2`: PDF 写 "Ex3 r15 TRSTRESC -60" → KB 写 "-50" (处理: KB 写正确值; 依据: 同行 TRORRES/TRSTRESN -50; KB `knowledge_base/domains/TR/examples.md:84`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 15 | ABC | TR | 55555 | 15 | TARGET | A2 | | PCBSD | Percent Change From Baseline in Sum of Diameters | -50 | % | -60 | -50 | % | ACE IMAGING | | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0357.txt` 第 32-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31|                                                                                Change From                                                                     IMAGING             ASSESSOR      1
 32|                                                                                Nadir in Sum
 33|                                                                                of Diameters
 34| 15    ABC      TR      55555    15     TARGET    A2                   PCBSD    Percent          -50               %        -60               -50      %        ACE                 INDEPENDENT   RADIOLOGIST   40      WEEK 6
 35|                                                                                Change From                                                                     IMAGING             ASSESSOR      1
 36|                                                                                Baseline in
 37|                                                                                Sum of
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:84-89` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  84| | 15 | ABC | TR | 55555 | 15 | TARGET | A2 | | PCBSD | Percent Change From Baseline in Sum of Diameters | -50 | % | -50 | -50 | % | ACE IMAGING | | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
  85| | 16 | ABC | TR | 55555 | 16 | TARGET | A2 | | PCNSD | Percent Change From Nadir in Sum of Diameters | -50 | % | -50 | -50 | % | ACE IMAGING | | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
  86| | 17 | ABC | TR | 55555 | 17 | NON-TARGET | A2 | R1-NT01 | TUMSTATE | Tumor State | ABSENT | | ABSENT | | | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-19 | 47 |
  87| | 18 | ABC | TR | 55555 | 18 | NON-TARGET | A2 | R1-NT02 | TUMSTATE | Tumor State | ABSENT | | ABSENT | | | ACE IMAGING | MRI | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-18 | 46 |
  88| | 19 | ABC | TR | 55555 | 19 | NEW | A2 | R1-NEW01 | TUMSTATE | Tumor State | EQUIVOCAL | | EQUIVOCAL | | | ACE IMAGING | CT SCAN | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-18 | 46 |
  89| | 20 | ABC | TR | 55555 | 20 | TARGET | A3 | R1-T01 | DIAMETER | Diameter | 7 | mm | 7 | 7 | mm | ACE IMAGING | MRI | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 | 88 |
~~~~

### R88. `ig34_p0357_a015` — r2:TYPO_SIB

- PDF 页 357 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-TR T-2`: PDF 写 "Ex3 r15 TRSTRESC -60" → KB 写 "-50" (处理: KB 写正确值; 依据: 同行 TRORRES/TRSTRESN -50; KB `knowledge_base/domains/TR/examples.md:84`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 16 | ABC | TR | 55555 | 16 | TARGET | A2 | | PCNSD | Percent Change From Nadir in Sum of Diameters | -50 | % | -50 | -50 | % | ACE IMAGING | | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0357.txt` 第 39-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38|                                                                                Diameters
 39| 16    ABC      TR      55555    16     TARGET    A2                   PCNSD    Percent          -50               %        -50               -50      %        ACE                 INDEPENDENT   RADIOLOGIST   40      WEEK 6
 40|                                                                                Change From                                                                     IMAGING             ASSESSOR      1
 41|                                                                                Nadir in Sum
 42|                                                                                of Diameters
 43| 17    ABC      TR      55555    17     NON-      A2         R1-NT01   TUMSTATE Tumor State      ABSENT                     ABSENT                              ACE       CT SCAN   INDEPENDENT   RADIOLOGIST   40      WEEK 6    2010-   47
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:85` (来源: live valid_hits):

~~~~
  85| | 16 | ABC | TR | 55555 | 16 | TARGET | A2 | | PCNSD | Percent Change From Nadir in Sum of Diameters | -50 | % | -50 | -50 | % | ACE IMAGING | | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |
~~~~

### R89. `ig34_p0420_a019` — r2:TYPO_SIB

- PDF 页 420 · 原子类型 TABLE_ROW · 所在节 `§7.4.2 Trial Summary (TS) – Examples`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-TS T-1`: PDF 写 "Ex2 r1 TSPARM Trial Type" → KB 写 "Trial Title" (处理: KB 写正确值; 依据: TSPARMCD=TITLE; Ex1/Ex4 同码; Row 1 说明; KB `knowledge_base/domains/TS/examples.md:76`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
14 | XYZ | TS | 1 |  | TITLE | Trial Title | A 24 Week Study of Oral Gabapentin vs. Placebo as add-on Treatment to Phenytoin in Subjects with Epilepsy due to Neurofibromatosis |  |  |  | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0420.txt` 第 25-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24| 13  XYZ     TS     1             TINDTP   Trial Intent Type                        TREATMENT                                                   C49656         CDISC CT           2011-06-10
 25| 14  XYZ     TS     1             TITLE    Trial Title                              A 24 Week Study of Oral Gabapentin vs. Placebo
 26|                                                                                    as add-on Treatment to Phenytoin in Subjects with
 27|                                                                                    Epilepsy due to Neurofibromatosis
 28| 15       XYZ    TS        1                 TPHASE       Trial Phase               Phase II Trial                                              C15601         CDISC CT           2011-06-10
~~~~

KB 现文: `knowledge_base/domains/TS/examples.md:24` (来源: live valid_hits):

~~~~
  24| | 14 | XYZ | TS | 1 | | TITLE | Trial Title | A 24 Week Study of Oral Gabapentin vs. Placebo as add-on Treatment to Phenytoin in Subjects with Epilepsy due to Neurofibromatosis | | | | |
~~~~

### R90. `ig34_p0433_a030` — r2:TYPO_SIB

- PDF 页 433 · 原子类型 SENTENCE · 所在节 `§8.4.3 SUPP-- Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-SUPPQUAL T-1`: PDF 写 "llustrate" → KB 写 "illustrate" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/domains/SUPPQUAL/examples.md:5`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example illustrates how the language used for a questionnaire might be represented.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0433.txt` 第 43-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 42| Example
 43| This example illustrates how the language used for a questionnaire might be represented. The parent domain
 44| (RDOMAIN) is QS, and IDVAR is QSCAT. QNAM holds the name of the supplemental qualifier variable being
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:241` (来源: live valid_hits):

~~~~
 241| **Example 2:** This example illustrates how the language used for a questionnaire might be represented. The parent domain (RDOMAIN) is QS, and IDVAR is QSCAT. QNAM holds the name of the supplemental qualifier variable being defined (QSLANG). The language recorded in QVAL applies to all of the subject’s records, where IDVAR (QSCAT) equals the value specified in IDVARVAL. In this case, IDVARVAL has values for 2 questionnaires—Brief Pain Inventory (BPI) and Alzheimer's Disease Assessment Scale–Cognitive Subscale (ADAS-Cog)—for 2 separate subjects. QVAL identifies the questionnaire language version (French or German) for each subject.
~~~~

