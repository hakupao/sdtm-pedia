# T4.1 第三轮补检包 8 — R3_PDF_TYPO (25 条; 编号 T176-T200)

> 由 `scripts/t4/t4_round3_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 T).

### T176. `ig34_p0174_a0012` — r3:R3_PDF_TYPO

- PDF 页 174 · 原子类型 LIST_ITEM · 所在节 `§6.2.6 Medical History (MH)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-MH`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T2 global fp audit R2: B-MH T-1 PDF_TYPO 第二处 MHENDTYP→MHEVDTYP (原子=PDF) | errata: t3_atom_err | in_atom_err=False in_remap=False; 出处 `.work/10_tier_b_repair/evidence/t2_fp_expected_regressions.md:53`
- 登记 `B-MH T-1`: PDF 写 "MHENDTYP = "DIAGNOSIS"" → KB 写 "MHEVDTYP" (处理: KB 写正确值; 依据: 同句前半/6a/spec; MHENDTYP 非变量; KB `knowledge_base/domains/MH/assumptions.md:51`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
b. When data collected about an event includes 2 different dates that could be considered the start or end of an event, then an MH record will be created for each. For example, if data collection included both a date of onset of symptoms and a date of diagnosis, there would be 2 records for the event, one with MHSTDTC the date of onset of symptoms and MHEVDTYP = "SYMPTOMS" and a second with MHSTDTC the date of diagnosis and MHENDTYP = "DIAGNOSIS". In such a case, it is recommended that the 2 records be linked by means such as a common value of MHSPID or MHGRPID.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0174.txt` 第 25-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24|                to be used to populate the start and/or end date; otherwise, it should be null.
 25|           b.   When data collected about an event includes 2 different dates that could be considered the start or end of an event, then an MH record will be
 26|                created for each. For example, if data collection included both a date of onset of symptoms and a date of diagnosis, there would be 2 records for the
 27|                event, one with MHSTDTC the date of onset of symptoms and MHEVDTYP = "SYMPTOMS" and a second with MHSTDTC the date of diagnosis
 28|                and MHENDTYP = "DIAGNOSIS". In such a case, it is recommended that the 2 records be linked by means such as a common value of MHSPID
 29|                or MHGRPID.
 30|      7.   Any identifiers, timing variables, or Events general observation-class qualifiers may be added to the MH domain, but the following Qualifiers would
~~~~

KB 现文: `knowledge_base/domains/MH/assumptions.md:51` (来源: registry B-MH T-1 kb_line_now):

~~~~
  51|    b. When data collected about an event includes 2 different dates that could be considered the start or end of an event, then an MH record will be created for each. For example, if data collection included both a date of onset of symptoms and a date of diagnosis, there would be 2 records for the event, one with MHSTDTC the date of onset of symptoms and MHEVDTYP = "SYMPTOMS" and a second with MHSTDTC the date of diagnosis and MHEVDTYP = "DIAGNOSIS". In such a case, it is recommended that the 2 records be linked by means such as a common value of MHSPID or MHGRPID.
~~~~

### T177. `ig34_p0190_a017` — r3:R3_PDF_TYPO

- PDF 页 190 · 原子类型 LIST_ITEM · 所在节 `§6.3.3 ECG Test Results (EG)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-EG`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A3-5 B-EG T-3 investigation→investigator | errata: t3_atom_err | new_target: domains/EG/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:22`
- 登记 `B-EG T-3`: PDF 写 "principal investigation" → KB 写 "principal investigator (同表 EGEVAL)" (处理: KB 写正确值; 依据: 表 EGEVAL=PRINCIPAL INVESTIGATOR; 改正属语义改写; KB `knowledge_base/domains/EG/examples.md:42`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-3: Show interpretations performed by the principal investigation on three different occasions. The ECG at Visit "SCREEN 2" has been flagged as the last observation before start of study treatment.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0190.txt` 第 32-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| necessary, by a cardiologist. EGGRPID is used to group the overall assessments collected on each ECG.
 32| Rows 1-3:          Show interpretations performed by the principal investigation on three different occasions. The ECG at Visit "SCREEN 2" has been flagged as the last observation before start of study treatment.
 33| Rows 4-5:          Show interpretations of the same ECG by both the investigator and a cardiologist. EGGRPID has been used to group these two records to emphasize their relationship.
~~~~

KB 现文: `knowledge_base/domains/EG/examples.md:42` (来源: registry B-EG T-3 kb_line_now):

~~~~
  42| **Rows 1-3:** Show interpretations performed by the principal investigator on three different occasions. The ECG at Visit "SCREEN 2" has been flagged as the last observation before start of study treatment.
~~~~

### T178. `ig34_p0198_a014` — r3:R3_PDF_TYPO

- PDF 页 198 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.2 Biospecimen Findings (BS)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-BS`
- 登记 `B-BS T-3`: PDF 写 "--STRNLO" → KB 写 "--STNRLO" (处理: KB 写正确值; 依据: Findings 通用变量名 --STNRLO; KB `knowledge_base/domains/BS/assumptions.md:23`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5. The following variables generally would not be used in BS: --POS, --ORNLO, --ORNHI, --STRNLO, --STNRHI, --STNRC, --NRIND, --LEAD, --CSTATE, --ACPTFL, --FAST, --TOX, --TOXGR, --SEV, --DTHREL.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0198.txt` 第 31-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 30|            that variable, but which further qualifies BSLOC instead of BSSPEC.
 31|      5.    The following variables generally would not be used in BS: --POS, --ORNLO, --ORNHI, --STRNLO, --STNRHI, --STNRC, --NRIND, --LEAD, --
 32|            CSTATE, --ACPTFL, --FAST, --TOX, --TOXGR, --SEV, --DTHREL.
 33| BS – Example
~~~~

KB 现文: `knowledge_base/domains/BS/assumptions.md:23` (来源: registry B-BS T-3 kb_line_now):

~~~~
  23| 5. The following variables generally would not be used in BS: --POS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --LEAD, --CSTATE, --ACPTFL, --FAST, --TOX, --TOXGR, --SEV, --DTHREL.
~~~~

### T179. `ig34_p0200_a006` — r3:R3_PDF_TYPO

- PDF 页 200 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `S-SPC1`
- 原子抽错登记: R2 → PDF_TYPO; 依据: S-SPC1 CP T-17 PDF_TYPO sting→string | errata: t3_atom_err | new_target: domains/CP/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:24`
- 登记 `S-SPC1 CP T-17`: PDF 写 "marker sting" → KB 写 "marker string" (处理: KB 写正确值; 依据: 同节 marker string 多处; KB `knowledge_base/domains/CP/assumptions.md:40`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Used in accordance with this guidance, the complete marker sting information provided in the --MRKSTR variable reflects the operational (i.e., laboratory-specific) definition of the test measurement.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0200.txt` 第 10-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  9| determining whether tests are truly comparable.
 10| Used in accordance with this guidance, the complete marker sting information provided in the --MRKSTR variable reflects the operational (i.e., laboratory-
 11| specific) definition of the test measurement. Together with the gating information provided in the --GATE and --GATEDEF variables, --MRKSTR values help to
 12| ensure that proper groupings and comparisons are made across tests by preserving nuanced details that may affect the interpretation of test results. To facilitate
~~~~

KB 现文: `knowledge_base/domains/CP/assumptions.md:40` (来源: registry S-SPC1 CP T-17 kb_line_now):

~~~~
  40| Used in accordance with this guidance, the complete marker string information provided in the --MRKSTR variable reflects the operational (i.e., laboratory-specific) definition of the test measurement.
~~~~

### T180. `ig34_p0200_a007` — r3:R3_PDF_TYPO

- PDF 页 200 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `S-SPC1`
- 原子抽错登记: R2 → PDF_TYPO; 依据: S-SPC1 CP T-21 PDF_TYPO --GATEDEF→--GATDEF | errata: t3_atom_err | new_target: domains/CP/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:25`
- 登记 `S-SPC1 CP T-21`: PDF 写 "--BNDAGT / --GATEDEF ×2 / CPBNDAGT" → KB 写 "--BDAGNT / --GATDEF / CPBDAGNT" (处理: KB 写正确值; 依据: spec 变量 CPBDAGNT/CPGATDEF; p208 列名; KB `knowledge_base/domains/CP/assumptions.md:24`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Together with the gating information provided in the --GATE and --GATEDEF variables, --MRKSTR values help to ensure that proper groupings and comparisons are made across tests by preserving nuanced details that may affect the interpretation of test results.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0200.txt` 第 11-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 10| Used in accordance with this guidance, the complete marker sting information provided in the --MRKSTR variable reflects the operational (i.e., laboratory-
 11| specific) definition of the test measurement. Together with the gating information provided in the --GATE and --GATEDEF variables, --MRKSTR values help to
 12| ensure that proper groupings and comparisons are made across tests by preserving nuanced details that may affect the interpretation of test results. To facilitate
 13| these objectives and to enable accurate cross-study comparisons and data-mining efforts, it is recommended that --MRKSTR values conform as closely as
~~~~

KB 现文: `knowledge_base/domains/CP/assumptions.md:24` (来源: registry S-SPC1 CP T-21 kb_line_now):

~~~~
  24| New variables include --SBMRKS (Sublineage Marker String), --CELSTA (Cell State), --CSMRKS (Cell State Marker String), --TSTCND (Test Condition), --CNDAGT (Test Condition Agent), --BDAGNT (Binding Agent), --ABCLID (Antibody Clone Identifier), --MRKSTR (Marker String), --GATE (Gate Name), --GATDEF (Gate Definition), --SPTSTD (Sponsor Test Description), --TSTPNL (Test Panel), --RESSCL (Result Scale), and --RESTYP (Result Type).
~~~~

### T181. `ig34_p0206_a001` — r3:R3_PDF_TYPO

- PDF 页 206 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `S-SPC1`
- 原子抽错登记: R2 → PDF_TYPO; 依据: S-SPC1 CP T-21 PDF_TYPO CPBNDAGT→CPBDAGNT | errata: t3_atom_err | new_target: domains/CP/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:26`
- 登记 `S-SPC1 CP T-21`: PDF 写 "--BNDAGT / --GATEDEF ×2 / CPBNDAGT" → KB 写 "--BDAGNT / --GATDEF / CPBDAGNT" (处理: KB 写正确值; 依据: spec 变量 CPBDAGNT/CPGATDEF; p208 列名; KB `knowledge_base/domains/CP/assumptions.md:24`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
included in another variable, such as CPBNDAGT and/or CPTSTPNL (refer to examples). CDISC will continue to develop examples for other use cases as they are identified and modeled.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0206.txt` 第 1-2 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1|           included in another variable, such as CPBNDAGT and/or CPTSTPNL (refer to examples). CDISC will
  2|           continue to develop examples for other use cases as they are identified and modeled.
  3| 7.   Specifying viability:
~~~~

KB 现文: `knowledge_base/domains/CP/assumptions.md:24` (来源: registry S-SPC1 CP T-21 kb_line_now):

~~~~
  24| New variables include --SBMRKS (Sublineage Marker String), --CELSTA (Cell State), --CSMRKS (Cell State Marker String), --TSTCND (Test Condition), --CNDAGT (Test Condition Agent), --BDAGNT (Binding Agent), --ABCLID (Antibody Clone Identifier), --MRKSTR (Marker String), --GATE (Gate Name), --GATDEF (Gate Definition), --SPTSTD (Sponsor Test Description), --TSTPNL (Test Panel), --RESSCL (Result Scale), and --RESTYP (Result Type).
~~~~

### T182. `ig34_p0206_a003` — r3:R3_PDF_TYPO

- PDF 页 206 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `S-SPC1`
- 原子抽错登记: R2 → PDF_TYPO; 依据: S-SPC1 CP T-18 PDF_TYPO CSMRKS→CPCSMRKS | errata: t3_atom_err | new_target: domains/CP/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:27`
- 登记 `S-SPC1 CP T-18`: PDF 写 "7a CPCELSTA and CSMRKS" → KB 写 "CPCSMRKS" (处理: KB 写正确值; 依据: 同段其后 3 处; spec; KB `knowledge_base/domains/CP/assumptions.md:75`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
a. Because the majority of cell phenotyping tests of interest are for viable cells, the word "Viable" is not generally included in the test name (CPTEST) and usually does not need to be explicitly stated in CPCELSTA. Because populating CPCELSTA and CSMRKS with viability information necessitates appending the "Sub" suffix to the value in CPTEST (assumption 5), it is recommended that CPCELSTA and CPCSMRKS generally not be used unless a selective viability stain was included in the test in order to differentiate the record for viable cells from record(s) for cells in a different vital state. For example, when viable cells are being compared to apoptotic and/or non-viable cells, it is necessary to differentiate those records using CPCELSTA and CPCSMRKS. In such cases where CPCELSTA and CPCSMRKS are populated, the "Sub" suffix is appended to the value in CPTEST (assumption 5).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0206.txt` 第 4-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3| 7.   Specifying viability:
  4|      a.   Because the majority of cell phenotyping tests of interest are for viable cells, the word "Viable" is not
  5|           generally included in the test name (CPTEST) and usually does not need to be explicitly stated in
  6|           CPCELSTA. Because populating CPCELSTA and CSMRKS with viability information necessitates
  7|           appending the "Sub" suffix to the value in CPTEST (assumption 5), it is recommended that
  8|           CPCELSTA and CPCSMRKS generally not be used unless a selective viability stain was included in
  9|           the test in order to differentiate the record for viable cells from record(s) for cells in a different vital
 10|           state. For example, when viable cells are being compared to apoptotic and/or non-viable cells, it is
 11|           necessary to differentiate those records using CPCELSTA and CPCSMRKS. In such cases where
 12|           CPCELSTA and CPCSMRKS are populated, the "Sub" suffix is appended to the value in CPTEST
 13|           (assumption 5).
~~~~

KB 现文: `knowledge_base/domains/CP/assumptions.md:75` (来源: registry S-SPC1 CP T-18 kb_line_now):

~~~~
  75|    a. Because the majority of cell phenotyping tests of interest are for viable cells, the word "Viable" is not generally included in the test name (CPTEST) and usually does not need to be explicitly stated in CPCELSTA. Because populating CPCELSTA and CPCSMRKS with viability information necessitates appending the "Sub" suffix to the value in CPTEST (assumption 5), it is recommended that CPCELSTA and CPCSMRKS generally not be used unless a selective viability stain was included in the test in order to differentiate the record for viable cells from record(s) for cells in a different vital state. For example, when viable cells are being compared to apoptotic and/or non-viable cells, it is necessary to differentiate those records using CPCELSTA and CPCSMRKS. In such cases where CPCELSTA and CPCSMRKS are populated, the "Sub" suffix is appended to the value in CPTEST (assumption 5).
~~~~

### T183. `ig34_p0206_a009` — r3:R3_PDF_TYPO

- PDF 页 206 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `S-SPC1`
- 登记 `S-SPC1 CP T-19`: PDF 写 "8d CPTEST, CPSMRKS, and CPCELSTA" → KB 写 "CPSBMRKS" (处理: KB 写正确值; 依据: spec CPMRKSTR Notes 同列; KB `knowledge_base/domains/CP/assumptions.md:82`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
d. The order of markers within a string is consistent across similar tests, generally proceeding in the order that defines the cell hierarchy from highest to lowest, followed by additional non-lineage-defining markers, and ending with cell state and viability markers. This order maintains alignment with how a test is identified using the ordered combination of CPTEST, CPSMRKS, and CPCELSTA. For example, a test for proliferating viable activated central memory helper T-lymphocytes would be operationally defined in CPMRKSTR as similar to "CD45+CD3+CD19-CD4+CD8-CD197+CD45RA-CD278+Ki67+7AAD-", where the order of markers in the string is "CD45" (leukocyte), "CD3+CD19- (T lymphocyte), "CD4+CD8-" (helper), "CD197+CD45RA-" (central memory), "CD278+" (activated), Ki67+ (proliferating), 7AAD- (viable). Corresponding to this marker-based definition of the test, and using the appropriate Controlled Terminology terms, CPTEST is "TLym Help Cen Mem Sub", CPCELSTA is "ACTIVATED; PROLIFERATING", and CPCSMRKS is "CD278+Ki67+". If the sponsor also chose to include the viability status as a cell state in addition to the activation and proliferative states, CPCELSTA would be similar to "ACTIVATED; PROLIFERATING; VIABLE" and the corresponding CPCSMRKS value would be "CD278+Ki67+7AAD-". In this example, the named cell population in CPTEST has not been further divided into an unnamed sublineage based on additional sublineage markers; therefore, CPSBMRKS is null.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0206.txt` 第 37-50 行 (自动定位, 词覆盖 0.914; 版式以原 PDF 为准):

~~~~
 36|      d.   The order of markers within a string is consistent across similar tests, generally proceeding in the order
 37|           that defines the cell hierarchy from highest to lowest, followed by additional non-lineage-defining
 38|           markers, and ending with cell state and viability markers. This order maintains alignment with how a
 39|           test is identified using the ordered combination of CPTEST, CPSMRKS, and CPCELSTA. For
 40|           example, a test for proliferating viable activated central memory helper T-lymphocytes would be
 41|           operationally defined in CPMRKSTR as similar to "CD45+CD3+CD19-CD4+CD8-CD197+CD45RA-
 42|           CD278+Ki67+7AAD-", where the order of markers in the string is "CD45" (leukocyte), "CD3+CD19-
 43|           (T lymphocyte), "CD4+CD8-" (helper), "CD197+CD45RA-" (central memory), "CD278+ (activated),
 44|           Ki67+ (proliferating), 7AAD- (viable). Corresponding to this marker-based definition of the test, and
 45|           using the appropriate Controlled Terminology terms, CPTEST is "TLym Help Cen Mem Sub",
 46|           CPCELSTA is "ACTIVATED; PROLIFERATING", and CPCSMRKS is "CD278+Ki67+". If the
 47|           sponsor also chose to include the viability status as a cell state in addition to the activation and
 48|           proliferative states, CPCELSTA would be similar to "ACTIVATED; PROLIFERATING; VIABLE"
 49|           and the corresponding CPCSMRKS value would be "CD278+Ki67+7AAD-". In this example, the
 50|           named cell population in CPTEST has not been further divided into an unnamed sublineage based on
 51|           additional sublineage markers; therefore, CPSBMRKS is null.
~~~~

KB 现文: `knowledge_base/domains/CP/assumptions.md:82-82` (来源: fuzzy locate (score 0.991)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  82|    d. The order of markers within a string is consistent across similar tests, generally proceeding in the order that defines the cell hierarchy from highest to lowest, followed by additional non-lineage-defining markers, and ending with cell state and viability markers. This order maintains alignment with how a test is identified using the ordered combination of CPTEST, CPSBMRKS, and CPCELSTA. For example, a test for proliferating viable activated central memory helper T-lymphocytes would be operationally defined in CPMRKSTR as similar to "CD45+CD3+CD19-CD4+CD8-CD197+CD45RA-CD278+Ki67+7AAD-", where the order of markers in the string is "CD45" (leukocyte), "CD3+CD19-" (T lymphocyte), "CD4+CD8-" (helper), "CD197+CD45RA-" (central memory), "CD278+" (activated), Ki67+ (proliferating), 7AAD- (viable). Corresponding to this marker-based definition of the test, and using the appropriate Controlled Terminology terms, CPTEST is "TLym Help Cen Mem Sub", CPCELSTA is "ACTIVATED; PROLIFERATING", and CPCSMRKS is "CD278+Ki67+". If the sponsor also chose to include the viability status as a cell state in addition to the activation and proliferative states, CPCELSTA would be similar to "ACTIVATED; PROLIFERATING; VIABLE" and the corresponding CPCSMRKS value would be "CD278+Ki67+7AAD-". In this example, the named cell population in CPTEST has not been further divided into an unnamed sublineage based on additional sublineage markers; therefore, CPSBMRKS is null.
~~~~

### T184. `ig34_p0211_a004` — r3:R3_PDF_TYPO

- PDF 页 211 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-CP`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec); 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CP.md:80`
- 登记 `B-CP T-15`: PDF 写 "叙述 CPGATEDEF (8 处)" → KB 写 "CPGATDEF" (处理: KB 写正确值; 依据: p202 spec 变量名 CPGATDEF; KB `knowledge_base/domains/CP/examples.md:71`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-2: Forward light scatter (FSC) and side scatter (SSC) are almost always applied as the first gating parameters to distinguish singlets and viable cells from doublets and debris. In row 1, a lymphocyte (LYM) count is reported which does not explicitly provide viability information. Nevertheless, it is generally assumed that FSC SSC gating is applied to exclude doublets, debris, and dead cells. Secondary FSC and SSC gating is then used to distinguish the lymphocyte population from other CD45+ leukocytes. In contrast, row 2 explicitly calls out cell viability based on the use of viability marker 7AAD to exclude cells that are in the process of dying (7AAD+). This is indicated in the Marker String (CPMRKSTR) and Gate Definition (CPGATEDEF) variables. In addition, the term "VIABLE" is included in the gate name (CPGATE).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0211.txt` 第 10-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  9| illustrated in the example using CPCELSTA and CPCSMRKS variables also apply to more complex tests where the biological state of the cell population is considered to be integral to the test.
 10| Rows 1-2:        Forward light scatter (FSC) and side scatter (SSC) are almost always applied as the first gating parameters to distinguish singlets and viable cells from doublets and debris. In row 1, a lymphocyte
 11|                  (LYM) count is reported which does not explicitly provide viability information. Nevertheless, it is generally assumed that FSC SSC gating is applied to exclude doublets, debris, and dead cells.
 12|                  Secondary FSC and SSC gating is then used to distinguish the lymphocyte population from other CD45+ leukocytes. In contrast, row 2 explicitly calls out cell viability based on the use of viability
 13|                  marker 7AAD to exclude cells that are in the process of dying (7AAD+). This is indicated in the Marker String (CPMRKSTR) and Gate Definition (CPGATEDEF) variables. In addition, the term
 14|                  "VIABLE" is included in the gate name (CPGATE).
 15| Rows 3-4:        Illustrate using CPCELSTA and CPCSMRKS to provide (1) the cell state descriptor in CPCELSTA, and (2) the markers used to define the cell state in CPCSMRKS. These variables further define
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:71` (来源: registry B-CP T-15 kb_line_now):

~~~~
  71| **Rows 1-2:** Forward light scatter (FSC) and side scatter (SSC) are almost always applied as the first gating parameters to distinguish singlets and viable cells from doublets and debris. In row 1, a lymphocyte (LYM) count is reported which does not explicitly provide viability information. Nevertheless, it is generally assumed that FSC SSC gating is applied to exclude doublets, debris, and dead cells. Secondary FSC and SSC gating is then used to distinguish the lymphocyte population from other CD45+ leukocytes. In contrast, row 2 explicitly calls out cell viability based on the use of viability marker 7AAD to exclude cells that are in the process of dying (7AAD+). This is indicated in the Marker String (CPMRKSTR) and Gate Definition (CPGATDEF) variables. In addition, the term "VIABLE" is included in the gate name (CPGATE).
~~~~

### T185. `ig34_p0213_a002` — r3:R3_PDF_TYPO

- PDF 页 213 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **REAL_GAP** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `S1-R2` · 批 `B-CP`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec); 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CP.md:30`
- 登记 `B-CP T-15`: PDF 写 "叙述 CPGATEDEF (8 处)" → KB 写 "CPGATDEF" (处理: KB 写正确值; 依据: p202 spec 变量名 CPGATDEF; KB `knowledge_base/domains/CP/examples.md:71`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 7-9: Show use of CPSBMRKS to further subset the named cell population in CPTEST into sublineages based on expression of additional markers CDxx and CDyy. In row 7, the total monocyte population, based on expression of CD14, is measured without any further subsetting. Rows 8 and 9 show that this monocyte population is further subdivided into two distinct sublineages, based on expression of CDxx and CDyy. Because those sublineages do not have established names, they are distinguished from one another using the CPSBMRKS variable. The value of "Monocytes" in the CPTEST variable for these rows is appended with the "Sub" suffix to "Monocytes Sub". The CPSBMRKS variable is used to indicate that row 8 contains data for the CDxx+CDyy- monocyte sublineage and row 9 contains data for the CDxx-CDyy+ sublineage. The full set of markers used for the test are included in CPMRKSTR, and the cell gating strategy is identified in CPGATE and CPGATEDEF using the pipe character (|) to separate each level of the gate in CPGATEDEF.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 6-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5|                      CPSTRESU, but did include it as the Result Type in CPRESTYP.
  6| Rows 7-9:            Show use of CPSBMRKS to further subset the named cell population in CPTEST into sublineages based on expression of additional markers CDxx and CDyy. In row 7, the total monocyte population,
  7|                      based on expression of CD14, is measured without any further subsetting. Rows 8 and 9 show that this monocyte population is further subdivided into two distinct sublineages, based on expression of
  8|                      CDxx and CDyy. Because those sublineages do not have established names, they are distinguished from one another using the CPSBMRKS variable. The value of "Monocytes" in the CPTEST variable
  9|                      for these rows is appended with the "Sub" suffix to "Monocytes Sub". The CPSBMRKS variable is used to indicate that row 8 contains data for the CDxx+CDyy- monocyte sublineage and row 9
 10|                      contains data for the CDxx-CDyy+ sublineage. The full set of markers used for the test are included in CPMRKSTR, and the cell gating strategy is identified in CPGATE and CPGATEDEF using the
 11|                      pipe character (|) to separate each level of the gate in CPGATEDEF.
 12| Rows 10-11: Show the monocyte sublineages defined in rows 8-9 expressed as a percentage of total monocytes (row 7). The numerators in CPTEST for rows 10-11 use the named cell population appended with
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:71` (来源: registry B-CP T-15 kb_line_now):

~~~~
  71| **Rows 1-2:** Forward light scatter (FSC) and side scatter (SSC) are almost always applied as the first gating parameters to distinguish singlets and viable cells from doublets and debris. In row 1, a lymphocyte (LYM) count is reported which does not explicitly provide viability information. Nevertheless, it is generally assumed that FSC SSC gating is applied to exclude doublets, debris, and dead cells. Secondary FSC and SSC gating is then used to distinguish the lymphocyte population from other CD45+ leukocytes. In contrast, row 2 explicitly calls out cell viability based on the use of viability marker 7AAD to exclude cells that are in the process of dying (7AAD+). This is indicated in the Marker String (CPMRKSTR) and Gate Definition (CPGATDEF) variables. In addition, the term "VIABLE" is included in the gate name (CPGATE).
~~~~

### T186. `ig34_p0215_a017` — r3:R3_PDF_TYPO

- PDF 页 215 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **REAL_GAP** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-CP`
- 登记 `B-CP T-3`: PDF 写 "(e.g., CD40+ in rows 15-16 in addition to … marker(s))." → KB 写 "…rows 15-16) in addition to … marker(s)." (处理: KB 写正确值; 依据: 同段 Rows 7-10 平行句括号位置; KB `knowledge_base/domains/CP/examples.md:200`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 15-18: Illustrate how CPSPTSTD might preface the name of a cell population with cell sublineage marker(s) (e.g., CD40+ in rows 15-16 in addition to non-cell state, non-sublineage marker(s)). Rows 17-18 additionally show that the lab/sponsor uses CPSPTSTD to identify the target cell population by name when it is not in CPTEST, such as when the test is for quantitative single marker expression (CD40 Expression in rows 17-18).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0215.txt` 第 39-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38| Rows 11-14: Same as rows 7-10, except here the cell state activation marker for the CD303+ pDC cell subset and the single marker expression measurement is CD80.
 39| Rows 15-18: Illustrate how CPSPTSTD might preface the name of a cell population with cell sublineage marker(s) (e.g., CD40+ in rows 15-16 in addition to non-cell state, non-sublineage marker(s). Rows 17-18
 40|             additionally show that the lab/sponsor uses CPSPTSTD to identify the target cell population by name when it is not in CPTEST, such as when the test is for quantitative single marker expression
 41|             (CD40 Expression in rows 17-18).
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:200` (来源: registry B-CP T-3 kb_line_now):

~~~~
 200| **Rows 15-18:** Illustrate how CPSPTSTD might preface the name of a cell population with cell sublineage marker(s) (e.g., CD40+ in rows 15-16) in addition to non-cell state, non-sublineage marker(s). Rows 17-18 additionally show that the lab/sponsor uses CPSPTSTD to identify the target cell population by name when it is not in CPTEST, such as when the test is for quantitative single marker expression (CD40 Expression in rows 17-18).
~~~~

### T187. `ig34_p0217_a015` — r3:R3_PDF_TYPO

- PDF 页 217 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-CP`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec); 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CP.md:85`
- 登记 `B-CP T-15`: PDF 写 "叙述 CPGATEDEF (8 处)" → KB 写 "CPGATDEF" (处理: KB 写正确值; 依据: p202 spec 变量名 CPGATDEF; KB `knowledge_base/domains/CP/examples.md:71`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 1:	The sponsor chose to submit only the final calculated result for target occupancy as reported by the lab, i.e., records used for the calculation were not submitted. The CPMRKSTR variable includes markers identifying the cell population (CD45+CD14+) and the target of interest (CDxx) on which occupancy was measured. CPGATE contains the name of the gate used to virtually isolate the cell population of interest and CPGATEDEF contains the gate definition or gating strategy. Note in this example that the CDxx marker, although it is the target of interest for the test, is not part of the string used to formally identify the named portion of the cell population. As a result, the sponsor chose to report the penultimate gate, which does not include the target marker of interest (CDxx). Because the target of interest for which occupancy was measured is not part of the test name, it is identified in CPBDAGNT and/or another variable (e.g. CPTSTPNL).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0217.txt` 第 47-51 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 46| associated with undesirable side effects or safety risks, are likely to be a concern.
 47| Row 1:               The sponsor chose to submit only the final calculated result for target occupancy as reported by the lab, i.e., records used for the calculation were not submitted. The CPMRKSTR variable includes
 48|                      markers identifying the cell population (CD45+CD14+) and the target of interest (CDxx) on which occupancy was measured. CPGATE contains the name of the gate used to virtually isolate the cell
 49|                      population of interest and CPGATEDEF contains the gate definition or gating strategy. Note in this example that the CDxx marker, although it is the target of interest for the test, is not part of the string
 50|                      used to formally identify the named portion of the cell population. As a result, the sponsor chose to report the penultimate gate, which does not include the target marker of interest (CDxx). Because the
 51|                      target of interest for which occupancy was measured is not part of the test name, it is identified in CPBDAGNT and/or another variable (e.g. CPTSTPNL).
 52| Row 2:               Same as row 1 except that the sponsor chose to use CPGATE and CPGATDEF to report information for the final gate rather than the penultimate gate. In this example, the CDxx marker (the target of
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:71` (来源: registry B-CP T-15 kb_line_now):

~~~~
  71| **Rows 1-2:** Forward light scatter (FSC) and side scatter (SSC) are almost always applied as the first gating parameters to distinguish singlets and viable cells from doublets and debris. In row 1, a lymphocyte (LYM) count is reported which does not explicitly provide viability information. Nevertheless, it is generally assumed that FSC SSC gating is applied to exclude doublets, debris, and dead cells. Secondary FSC and SSC gating is then used to distinguish the lymphocyte population from other CD45+ leukocytes. In contrast, row 2 explicitly calls out cell viability based on the use of viability marker 7AAD to exclude cells that are in the process of dying (7AAD+). This is indicated in the Marker String (CPMRKSTR) and Gate Definition (CPGATDEF) variables. In addition, the term "VIABLE" is included in the gate name (CPGATE).
~~~~

### T188. `ig34_p0218_a014` — r3:R3_PDF_TYPO

- PDF 页 218 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-CP`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec); 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CP.md:308`
- 登记 `B-CP T-15`: PDF 写 "叙述 CPGATEDEF (8 处)" → KB 写 "CPGATDEF" (处理: KB 写正确值; 依据: p202 spec 变量名 CPGATDEF; KB `knowledge_base/domains/CP/examples.md:71`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Other variables such as CPMRKSTR, CPGATE, and CPGATEDEF are used to identify the cell population on which the binding of interest was measured.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0218.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| Since the example is measuring binding and not a cell population per se, the Sublineage Marker String (CPSBMRKS), Cell State (CPCELSTA), and Cell State Marker String (CPCSMRKS) are not used and are not
 20| included. Other variables such as CPMRKSTR, CPGATE, and CPGATEDEF are used to identify the cell population on which the binding of interest was measured. In addition, the Sponsor Test Description
 21| (CPSPTSTD) and Test Panel (CPTSTPNL) variables may be helpful for identifying a specific cell population.
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:71` (来源: registry B-CP T-15 kb_line_now):

~~~~
  71| **Rows 1-2:** Forward light scatter (FSC) and side scatter (SSC) are almost always applied as the first gating parameters to distinguish singlets and viable cells from doublets and debris. In row 1, a lymphocyte (LYM) count is reported which does not explicitly provide viability information. Nevertheless, it is generally assumed that FSC SSC gating is applied to exclude doublets, debris, and dead cells. Secondary FSC and SSC gating is then used to distinguish the lymphocyte population from other CD45+ leukocytes. In contrast, row 2 explicitly calls out cell viability based on the use of viability marker 7AAD to exclude cells that are in the process of dying (7AAD+). This is indicated in the Marker String (CPMRKSTR) and Gate Definition (CPGATDEF) variables. In addition, the term "VIABLE" is included in the gate name (CPGATE).
~~~~

### T189. `ig34_p0220_a001` — r3:R3_PDF_TYPO

- PDF 页 220 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-CP`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec); 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CP.md:95`
- 登记 `B-CP T-15`: PDF 写 "叙述 CPGATEDEF (8 处)" → KB 写 "CPGATDEF" (处理: KB 写正确值; 依据: p202 spec 变量名 CPGATDEF; KB `knowledge_base/domains/CP/examples.md:71`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
CPGATEDEF contains the gate definition/gating strategy. Note that in this example the CD99 marker, although it is the target of interest for the test, it is not part of the marker string used to identify the named portion of the cell population on which the test was performed.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0220.txt` 第 1-2 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1|                      CPGATEDEF contains the gate definition/gating strategy. Note that in this example the CD99 marker, although it is the target of interest for the test, it is not part of the marker string used to identify the
  2|                      named portion of the cell population on which the test was performed. As a result, the sponsor chose to report the penultimate gate, which does not include the target marker of interest (CD99). Because
  3|                      the target of interest for which occupancy was measured is not part of the test name (CPTEST), it is identified using CPBDAGNT and/or as part of the panel name in CPTSTPNL. The CPCAT and
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:71` (来源: registry B-CP T-15 kb_line_now):

~~~~
  71| **Rows 1-2:** Forward light scatter (FSC) and side scatter (SSC) are almost always applied as the first gating parameters to distinguish singlets and viable cells from doublets and debris. In row 1, a lymphocyte (LYM) count is reported which does not explicitly provide viability information. Nevertheless, it is generally assumed that FSC SSC gating is applied to exclude doublets, debris, and dead cells. Secondary FSC and SSC gating is then used to distinguish the lymphocyte population from other CD45+ leukocytes. In contrast, row 2 explicitly calls out cell viability based on the use of viability marker 7AAD to exclude cells that are in the process of dying (7AAD+). This is indicated in the Marker String (CPMRKSTR) and Gate Definition (CPGATDEF) variables. In addition, the term "VIABLE" is included in the gate name (CPGATE).
~~~~

### T190. `ig34_p0224_a013` — r3:R3_PDF_TYPO

- PDF 页 224 · 原子类型 SENTENCE · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-GF`
- 登记 `B-GF T-1`: PDF 写 "inheritabilty" → KB 写 "inheritability" (处理: KB 写正确值; 依据: p225 Ex2 拼作 inheritability; KB `knowledge_base/domains/GF/examples.md:5`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example shows findings from an assessment of single nucleotide and copy number variation generated from biocomputational analysis with wet laboratory methodology targeted genome sequencing. Findings from this assessment show variation from DNA extracted from an individual's tumor tissue. As the DNA specimen was extracted from tumor tissue, the inheritabilty of the variation is considered to be somatic.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0224.txt` 第 22-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 21| Example 1
 22| This example shows findings from an assessment of single nucleotide and copy number variation generated from biocomputational analysis with wet laboratory
 23| methodology targeted genome sequencing. Findings from this assessment show variation from DNA extracted from an individual's tumor tissue. As the DNA
 24| specimen was extracted from tumor tissue, the inheritabilty of the variation is considered to be somatic.
 25| Row 1:         Shows the predicted amino acid change due to the single nucleotide variant.
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:5` (来源: registry B-GF T-1 kb_line_now):

~~~~
   5| This example shows findings from an assessment of single nucleotide and copy number variation generated from biocomputational analysis with wet laboratory methodology targeted genome sequencing. Findings from this assessment show variation from DNA extracted from an individual's tumor tissue. As the DNA specimen was extracted from tumor tissue, the inheritability of the variation is considered to be somatic.
~~~~

### T191. `ig34_p0225_a019` — r3:R3_PDF_TYPO

- PDF 页 225 · 原子类型 SENTENCE · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `writer-Tn-registry` · 批 `B-GF`
- 登记 `B-GF T-3`: PDF 写 "respresented" → KB 写 "represented" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/domains/GF/examples.md:70`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example shows transcription levels of genes ACTB and GAPDH and summarized scores from the transcription levels. Transcription levels and scores were determined using biocomputational analysis with wet laboratory methodology targeted transcriptome sequencing. Specific formulas used in biocomputational analyses to generate normalized and summarized score results are rerspresented when applicable.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0225.txt` 第 65-66 行 (自动定位, 词覆盖 0.975; 版式以原 PDF 为准):

~~~~
 64| Example 3
 65| This example shows transcription levels of genes ACTB and GAPDH and summarized scores from the transcription levels. Transcription levels and scores were determined using biocomputational analysis with wet
 66| laboratory methodology targeted transcriptome sequencing. Specific formulas used in biocomputational analyses to generate normalized and summarized score results are respresented when applicable.
 67| 
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:70` (来源: registry B-GF T-3 kb_line_now):

~~~~
  70| This example shows transcription levels of genes ACTB and GAPDH and summarized scores from the transcription levels. Transcription levels and scores were determined using biocomputational analysis with wet laboratory methodology targeted transcriptome sequencing. Specific formulas used in biocomputational analyses to generate normalized and summarized score results are represented when applicable.
~~~~

### T192. `ig34_p0227_a018` — r3:R3_PDF_TYPO

- PDF 页 227 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-GF`
- 登记 `B-GF T-2`: PDF 写 "MBTEST Microbial Organism Idenitifcation" → KB 写 "…Identification" (处理: KB 写正确值; 依据: 同页叙述明载 MBTEST 值; KB `knowledge_base/domains/GF/examples.md:145`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | INFLU122 | MB | INF01-01 | 1 | INFLU0101 | MCORGIDN | Microbial Organism Identification | INFLUENZA A VIRUS SUBTYPE H3N2 | INFLUENZA A VIRUS SUBTYPE H3N2 | MUCUS | NOSTRIL | NUCLEIC ACID AMPLIFICATION TEST | 1 | BASELINE | 2020-06-11 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0227.txt` 第 26-31 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25| Tests that diagnose or identify the presence of an infectious agent in a subject sample are represented in the MB domain, regardless of the methodology used. In this example, the subject was diagnosed with influenza
 26| A H3N2 via a nucleic acid amplification test (NAAT) at the baseline visit. MBTEST = "Microbial Organism Identification" because the assay does not specifically test for the presence of 1 organism or subtype to the
 27| exclusion of all others.
 28| mb.xpt
 29| Row STUDYID DOMAIN USUBJID MBSEQ MBREFID MBTESTCD MBTEST                                     MBORRES                              MBSTRESC                              MBSPEC MBLOC   MBMETHOD                        VISITNUM VISIT    MBDTC
 30| 1   INFLU122 MB    INF01-01 1    INFLU0101 MCORGIDN Microbial Organism                       INFLUENZA A VIRUS SUBTYPE            INFLUENZA A VIRUS SUBTYPE             MUCUS  NOSTRIL NUCLEIC ACID AMPLIFICATION      1        BASELINE 2020-06-
 31|                                                     Idenitifcation                           H3N2                                 H3N2                                                 TEST                                              11
 32| 
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:145` (来源: decision.evidence.hit):

~~~~
 145| | 1 | INFLU122 | MB | INF01-01 | 1 | INFLU0101 | MCORGIDN | Microbial Organism Identification | INFLUENZA A VIRUS SUBTYPE H3N2 | INFLUENZA A VIRUS SUBTYPE H3N2 | MUCUS | NOSTRIL | NUCLEIC ACID AMPLIFICATION TEST | 1 | BASELINE | 2020-06-11 |
~~~~

### T193. `ig34_p0228_a002` — r3:R3_PDF_TYPO

- PDF 页 228 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-GF`
- 登记 `B-GF T-5`: PDF 写 "Row 1 句末无句号" → KB 写 "有句号" (处理: KB 写正确值; 依据: 同列其他 Row 说明均句号; KB `knowledge_base/domains/GF/examples.md:157`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 1:	Shows the result of a targeted test to detect a single nucleotide polymorphism in the influenza neuraminidase gene known to confer resistance to the drug oseltamivir. The result (R292R) indicates that the amino acid residue R (arginine) at position 292 remains unchanged at the baseline visit
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0228.txt` 第 2-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| GFLNKID serves as the link between this dataset and the MS dataset which follows.
  2| Row 1:          Shows the result of a targeted test to detect a single nucleotide polymorphism in the influenza neuraminidase gene known to confer resistance to the drug oseltamivir. The result (R292R) indicates that
  3|                 the amino acid residue R (arginine) at position 292 remains unchanged at the baseline visit
  4| Rows 2-3:       Show the results of the same targeted test at the day 2 and day 5 visits. The results (R292K) show that a mutation has occurred at position 292 from the amino acid R (arginine) to the amino acid K
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:157` (来源: decision.evidence.hit):

~~~~
 157| **Row 1:** Shows the result of a targeted test to detect a single nucleotide polymorphism in the influenza neuraminidase gene known to confer resistance to the drug oseltamivir. The result (R292R) indicates that the amino acid residue R (arginine) at position 292 remains unchanged at the baseline visit.
~~~~

### T194. `ig34_p0228_a009` — r3:R3_PDF_TYPO

- PDF 页 228 · 原子类型 SENTENCE · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-GF`
- 登记 `B-GF T-4`: PDF 写 "GFLINKID matches MSLNKID" → KB 写 "GFLNKID" (处理: KB 写正确值; 依据: gf 表头、relrec IDVAR、p228 首句; KB `knowledge_base/domains/GF/examples.md:169`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The susceptibility data stemming from this genetic testing above are represented in MS (see Section 6.3.5.7.2, Microbiology Susceptibility, assumption 1b). GFLNKID matches MSLNKID to connect the records in GF with the corresponding conclusion regarding susceptibility in MS. As above, NHOID is used to indicate that influenza A H3N2 is the focus of these records. MSAGENT represents the drug to which the results of susceptible or resistant pertain.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0228.txt` 第 7-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6| gf.xpt
  7| Row STUDYID DOMAIN USUBJID GFSEQ GFREFID     NHOID                      GFLNKID   GFTESTCD GFTEST                  GFTSTDTL                   GFORRES GFSTRESC GFSYM GFGENLOC GFSEQID GFSPEC GFMETHOD VISITNUM VISIT    GFDTC
  8| 1   INFLU122 GF    INF01-01 1    INFLU0101.1 INFLUENZA A                GF-MS-    SNV      Single Nucleotide       PREDICTED AMINO ACID       R292R   R292R    NA    292      U43427  RNA             1        BASELINE 2020-06-
  9|                                              H3N2                       01                 Variation               CHANGE                                                                                               11
 10| 2   INFLU122 GF    INF01-01 2    INFLU0102   INFLUENZA A                GF-MS-    SNV      Single Nucleotide       PREDICTED AMINO ACID       R292K   R292K    NA    292      U43427  RNA             2        DAY 2    2020-06-
 11|                                              H3N2                       02                 Variation               CHANGE                                                                                               12
 12| 3   INFLU122 GF    INF01-01 3    INFLU0103   INFLUENZA A                GF-MS-    SNV      Single Nucleotide       PREDICTED AMINO ACID       R292K   R292K    NA    292      U43427  RNA             3        DAY 5    2020-06-
 13|                                              H3N2                       03                 Variation               CHANGE                                                                                               15
 14| 
 15| The susceptibility data stemming from this genetic testing above are represented in MS (see Section 6.3.5.7.2, Microbiology Susceptibility, assumption 1b). GFLINKID matches MSLNKID to connect the records in
 16| GF with the corresponding conclusion regarding susceptibility in MS. As above, NHOID is used to indicate that influenza A H3N2 is the focus of these records. MSAGENT represents the drug to which the results of
 17| susceptible or resistant pertain.
 18| Row 1:          Shows the influenza extracted from the subject at the baseline visit is susceptible to oseltamivir.
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:169` (来源: decision.evidence.hit):

~~~~
 169| The susceptibility data stemming from this genetic testing above are represented in MS (see Section 6.3.5.7.2, Microbiology Susceptibility, assumption 1b). GFLNKID matches MSLNKID to connect the records in GF with the corresponding conclusion regarding susceptibility in MS. As above, NHOID is used to indicate that influenza A H3N2 is the focus of these records. MSAGENT represents the drug to which the results of susceptible or resistant pertain.
~~~~

### T195. `ig34_p0236_a005` — r3:R3_PDF_TYPO

- PDF 页 236 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-IS`
- 登记 `B-IS T-3`: PDF 写 "NON-STUDY RELATED IMMUNOGENICITY" → KB 写 "NON-STUDY-RELATED" (处理: KB 写正确值; 依据: 同表 ISCAT 与叙述 3 处; KB `knowledge_base/domains/IS/examples.md:108`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 3-4:	Show the screening and quantification of microbial-induced IgG antibody against the RSV-protein Z at baseline. Note: Because RSV-protein Z is not the immunogenic target of interest in this vaccine study, ISCAT is populated with the value "NON-STUDY RELATED IMMUNOGENICITY".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 16-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15|                    baseline and treatment measurements.
 16| Rows 3-4:          Show the screening and quantification of microbial-induced IgG antibody against the RSV-protein Z at baseline. Note: Because RSV-protein Z is not the immunogenic target of interest in this vaccine
 17|                    study, ISCAT is populated with the value "NON-STUDY RELATED IMMUNOGENICITY".
 18| Rows 5-7:          Show the titer of microbial-induced IgG antibody against the RSV-protein B, post-vaccination at visits 1, 2, and 3. These 3 records show the antibody titers had increased post-vaccination, presumably
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:108` (来源: registry B-IS T-3 kb_line_now):

~~~~
 108| **Rows 3-4:** Show the screening and quantification of microbial-induced IgG antibody against the RSV-protein Z at baseline. Note: Because RSV-protein Z is not the immunogenic target of interest in this vaccine study, ISCAT is populated with the value "NON-STUDY-RELATED IMMUNOGENICITY".
~~~~

### T196. `ig34_p0236_a015` — r3:R3_PDF_TYPO

- PDF 页 236 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `K3b-registry` · 批 `B-IS`
- 登记 `B-IS T-1`: PDF 写 "Ex5 r6 STUDYID RSC1230" → KB 写 "RSV1230" (处理: KB 写正确值; 依据: 同列其余 RSV1230; USUBJID RSV1230-011; KB `knowledge_base/domains/IS/examples.md:120`)
- 登记 `B-IS T-2`: PDF 写 "Ex5 r7 STUDYID RSC1230" → KB 写 "RSV1230" (处理: KB 写正确值; 依据: 同 T-1; KB `knowledge_base/domains/IS/examples.md:121`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 7 | RSC1230 | IS | RSV1230-011 | 3 | 13671 | | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:500 | 500 | 500 | titer | SERUM | ELISA | 4 | VISIT 3 | 2017-09-27 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 39-41 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38|                           011                                            IgG Antibody        SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                          08-27
 39|                                                                                              B
 40| 7        RSC1230   IS     RSV1230-   3       13671             MBIGGAB   Microbial-induced   HUMAN RESPIRATORY         QUANTIFY STUDY VACCINE-RELATED   HUMORAL    1:500    500        500   titer    SERUM   ELISA   4        VISIT 3    2017-
 41|                           011                                            IgG Antibody        SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                          09-27
 42|                                                                                              B
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:120` (来源: registry B-IS T-1 kb_line_now):

~~~~
 120| | 6 | RSV1230 | IS | RSV1230-011 | 2 | 13670 | | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:220 | 220 | 220 | titer | SERUM | ELISA | 3 | VISIT 2 | 2017-08-27 |
~~~~

### T197. `ig34_p0257_a016` — r3:R3_PDF_TYPO

- PDF 页 257 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-MS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-MS T-1: MSSTRESC PDF 空, KB 保留 25; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-MS.md:115`
- 登记 `B-MS T-1`: PDF 写 "Ex1 r9 MSSTRESC 空" → KB 写 "25" (处理: KB 写正确值; 依据: 同行 MSORRES/MSSTRESN 25; r7 同式; KB `knowledge_base/domains/MS/examples.md:31`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
9 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 4 | 9 | SPEC01 | 2 | DIAZOINH | Diameter of the Zone of Inhibition | Amoxicillin | | | 25 | mm | | 25 | mm | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-26T08:00
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0257.txt` 第 28-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27|                    002             FAECALIS                                                           Susceptibility       Drug                                                                                  XYZ                          26T08:00
 28| 9   ABC     MS     ABC-001-        ENTEROCOCCUS          4            9     SPEC01  2        DIAZOINH Diameter of the      Amoxicillin                  25            mm                     25         mm       LOCAL LAB   DISK DIFFUSION   2005-06-
 29|                    002             FAECALIS                                                           Zone of Inhibition                                                                                         XYZ                          26T08:00
 30| 10  ABC     MS     ABC-001-        ENTEROCOCCUS          4            10    SPEC01  2        MICROSUS Microbial            Amoxicillin                  RESISTANT              RESISTANT                         LOCAL LAB   DISK DIFFUSION   2005-06-
~~~~

KB 现文: `knowledge_base/domains/MS/examples.md:31` (来源: registry B-MS T-1 kb_line_now):

~~~~
  31| | 9 | ABC | MS | ABC-001-002 | ENTEROCOCCUS FAECALIS | 4 | 9 | SPEC01 | 2 | DIAZOINH | Diameter of the Zone of Inhibition | Amoxicillin | | | 25 | mm | 25 | 25 | mm | LOCAL LAB XYZ | DISK DIFFUSION | 2005-06-26T08:00 |
~~~~

### T198. `ig34_p0262_a020` — r3:R3_PDF_TYPO

- PDF 页 262 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-MS`
- 登记 `B-MS T-2`: PDF 写 "Rows 3-4 MSCONU" → KB 写 "MSCONCU" (处理: KB 写正确值; 依据: 同句前文与 Rows 1-2; KB `knowledge_base/domains/MS/examples.md:65`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 3-4: Show genotypic susceptibility testing results on the same aliquot from a NAAT that looks for mutations that confer resistance to 2 drugs. MSAGENT should be populated with the name of the drug whose action is affected by the mutation being tested for. However, because the drug is not used in the test, MSCONC and MSCONCU should be null. These results are represented in MS because the only result given is in terms of resistant/susceptible; no genetic results are reported.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0262.txt` 第 33-37 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32| Rows 1-2:        Show phenotypic testing results on 2 separate culture plates: 1 with medium containing rifampicin (row 1) and 1 with medium containing isoniazid (row 2). MSAGENT is populated with the name of
 33|                  the drug being used in the susceptibility test. The variables MSCONC and MSCONCU represent the concentration and units of the drug being used. The culture start and stop dates are represented in BE
 34|                  and can be linked to MS by BELNKID and MSLNKID.
 35| Rows 3-4:        Show genotypic susceptibility testing results on the same aliquot from a NAAT that looks for mutations that confer resistance to 2 drugs. MSAGENT should be populated with the name of the drug
 36|                  whose action is affected by the mutation being tested for. However, because the drug is not used in the test, MSCONC and MSCONU should be null. These results are represented in MS because the
 37|                  only result given is in terms of resistant/susceptible; no genetic results are reported.
 38| ms.xpt
~~~~

KB 现文: `knowledge_base/domains/MS/examples.md:65` (来源: decision.evidence.hit):

~~~~
  65| **Rows 3-4:** Show genotypic susceptibility testing results on the same aliquot from a NAAT that looks for mutations that confer resistance to 2 drugs. MSAGENT should be populated with the name of the drug whose action is affected by the mutation being tested for. However, because the drug is not used in the test, MSCONC and MSCONCU should be null. These results are represented in MS because the only result given is in terms of resistant/susceptible; no genetic results are reported.
~~~~

### T199. `ig34_p0262_a030` — r3:R3_PDF_TYPO

- PDF 页 262 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `S1-R2` · 批 `B-MS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-MS T-3: verbatim IDVAR=MBREFID 为 PDF 笔误, KB 改 MSREFID; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-MS.md:62 (T-n 行; 原子 id 未出现在该文件)`
- 登记 `B-MS T-3`: PDF 写 "suppms IDVAR MBREFID" → KB 写 "MSREFID" (处理: KB 写正确值; 依据: RDOMAIN=MS, IDVARVAL=ms MSREFID; KB `knowledge_base/domains/MS/examples.md:80`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2 | ABC | MS | ABC-01-101 | MBREFID | 100.5 | MSMEDTYPE | Medium Type | LOWENSTEIN-JENSEN | Collected
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0262.txt` 第 55-55 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 54| 1      ABC           MS        ABC-01-101        MBREFID   100.4      MSMEDTYPE        Medium Type        LOWENSTEIN-JENSEN          Collected
 55| 2      ABC           MS        ABC-01-101        MBREFID   100.5      MSMEDTYPE        Medium Type        LOWENSTEIN-JENSEN          Collected
 56| 
~~~~

KB 现文: `knowledge_base/domains/MS/examples.md:80` (来源: registry B-MS T-3 kb_line_now):

~~~~
  80| | 1 | ABC | MS | ABC-01-101 | MSREFID | 100.4 | MSMEDTYPE | Medium Type | LOWENSTEIN-JENSEN | Collected |
~~~~

### T200. `ig34_p0263_a020` — r3:R3_PDF_TYPO

- PDF 页 263 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-MB`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-MB T-3: verbatim MBTRESN 为 PDF 印刷错, KB 改 MBSTRESN 后不命中 (预期); 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-MB.md:145`
- 登记 `B-MB T-3`: PDF 写 "Ex4 表头 MBTRESN" → KB 写 "MBSTRESN" (处理: KB 写正确值; 依据: spec 无 MBTRESN; r2 值=MBSTRESC 数值; KB `knowledge_base/domains/MB/examples.md:241`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row | STUDYID | DOMAIN | USUBJID | MBSEQ | MBREFID | MBGRPID | MBTESTCD | MBTEST | MBTSTDTL | MBORRES | MBORRESU | MBRSLSCL | MBSTRESC | MBTRESN | MBSTRESU | MBSPEC | MBLOC | MBMETHOD | VISITNUM | VISIT | MBDTC | MBENDTC
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0263.txt` 第 25-25 行 (自动定位, 词覆盖 0.957; 版式以原 PDF 为准):

~~~~
 24| mb.xpt
 25| Row STUDYID DOMAIN USUBJID             MBSEQ MBREFID MBGPRID MBTESTCD MBTEST                           MBTSTDTL        MBORRES MBORRESU MBRSLSCL MBSTRESC MBTRESN MBSTRESU MBSPEC MBLOC MBMETHOD    VISITNUM VISIT MBDTC      MBENDTC
 26| 1   ABC     MB     ABC-01-             1     600     1       MTB      Mycobacterium                    DETECTION       PRESENT          Ord      PRESENT                   SPUTUM LUNG  MICROBIAL   5        WEEK 2011-03-    2011-03-
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:241` (来源: registry B-MB T-3 kb_line_now):

~~~~
 241| | Row | STUDYID | DOMAIN | USUBJID | MBSEQ | MBREFID | MBGRPID | MBTESTCD | MBTEST | MBTSTDTL | MBORRES | MBORRESU | MBRSLSCL | MBSTRESC | MBSTRESN | MBSTRESU | MBSPEC | MBLOC | MBMETHOD | VISITNUM | VISIT | MBDTC | MBENDTC |
~~~~

