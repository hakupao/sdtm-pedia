# T4.1 补检结果 — 包 1/8 (PRE_EXISTING, 全局编号 1-29)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T04:52:06Z (`date -u` 实测, 开工时)
- brief: `.work/10_tier_b_repair/subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`; 样本包: `.work/10_tier_b_repair/work/t4/supp/supp_pack_1.md`
- 看过的渲染页 (SDTMIG v3.4 PDF 物理页): 32, 73, 76, 123, 141, 146 (上部 bs 表 + 下部 be 表), 147 (bs 表), 153, 182, 190, 191. 页 101 只看文本层 (版式简单, 行 7/8 各值单行无折行, 无歧义).
- 用过的命令 (临时文件在 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/supp1/`):
  - `pdftoppm -r 200 -f N -l N -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" pN` (N=32,141,146,147,182,190,191)
  - `pdftoppm -r 250 -f N -l N -x 0 -y Y -W 3500 -H H -png ...` 局部放大 (N=73,76,141,146,147,153)
  - Read 工具 `pages=123` 看渲染页
  - `cat/cut .work/10_tier_b_repair/work/pdf_pages/ig34_p{0072,0073,0076,0101,0141,0146,0147,0182}.txt`
  - `sed -n` 读 `knowledge_base/chapters/ch04_general_assumptions.md`, `knowledge_base/domains/{DM,CM,ML,AE,BE,CE,DA,EG}/examples.md`; `grep -n` 各域标题 / CRF Metadata 位置
  - `grep -n` 查 `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` (页 32/73/76/101/123/141/146/147/153/182/190/191 相关条目)

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 | 说明 |
|---|---|---|---|---|---|---|
| 1 | ig34_p0032_a013 | PRE_EXISTING | EXACT | HOLDS | 渲染页 32; `ig34_p0032.txt`:18-19; `knowledge_base/chapters/ch04_general_assumptions.md`:423 (§4.2.7.1 下, 标题在 :397) | 逐字一致. PDF "field :" 冒号前空格, KB "field:" — 属空白归一; 另已登记 `S-CH4 T-10c`. |
| 2 | ig34_p0073_a001 | PRE_EXISTING | EXACT | HOLDS | 渲染页 73 (顶部续行); `ig34_p0072.txt` 末 + `ig34_p0073.txt`:5-9; `knowledge_base/domains/DM/examples.md`:188 (Example 4) | 该原子是 CRACE01-CRACE04 行跨页续行 (CRF Completion Instructions 续 `"AMERICAN INDIAN OR ALASKA NATIVE". Check all that apply.`; SDTM Target Mapping 续 `SUPPDM.QLABEL = "Collected Race n" where n is the choice value.`). KB 把跨页行合并为一行, 两格续文逐字在对应格内, 其余格 (Text / SUPPDM.QVAL / (RACEC) / 值列表 / checkbox) 与 p72 一致. 原子 verbatim 把 p72 部分也拼进来, 属抽取方式问题. |
| 3 | ig34_p0076_a002 | PRE_EXISTING | EXACT | HOLDS | 渲染页 76 表头; `ig34_p0076.txt`:2-5; `knowledge_base/domains/DM/examples.md`:330 (Example 6 的 CRF Metadata; 包里指针 :178 是 Example 4 同构表头, 非本页那一处) | PDF 表头 14 列: CDASH Variable / Order / Question Text / Prompt / CRF Completion Instructions / Type / SDTMIG Target Variable / SDTM Target Mapping / Controlled Terminology Code List Name / Permissible Values / Pre-specified Value / Query Display / List Style / Hidden. KB :330 逐格一致. 原子 verbatim 抽错 (漏 "Permissible Values", 把 "Query Display" "List Style" 错切成 "Query Display Style" "List"), KB 按 PDF 写对. 标签级别严格说应为 ATOM_ERR, 内容无问题. |
| 4 | ig34_p0101_a030 | PRE_EXISTING | EXACT | HOLDS | `ig34_p0101.txt`:36; `knowledge_base/domains/CM/examples.md`:25 | PDF Row 7 = `7 ABC CM ABC-0002 1 ASPIRIN 100 mg QD 2004-01-01 2004-01-03`, KB :25 逐格一致. 原子 verbatim 抽错 (把行 8 的 BID / 2004-01-07 拼到行 7), 标签级别严格说应为 ATOM_ERR. |
| 5 | ig34_p0123_a009 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 123 Meal Log CRF 行 1; `knowledge_base/domains/ML/examples.md`:16 | 值全部一致 (2015 Jun 03 / 14:15 / CE001, 音量空). 差异: PDF 用粗体 "X Snack" 表示勾选、未选项只有文字; KB 写成 "[X] Snack \| [ ] Nutritional drink \| [ ] Meal", 增加了 "[ ]" 框记号 → 格式改写, 非逐字. |
| 6 | ig34_p0123_a010 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 123 行 2; ML/examples.md:17 | 同 #5: 勾选在 Nutritional drink, 8 oz / 2015 Sep 03 / 8:30 / CE002 一致; "[X]/[ ]" 记号为格式改写. |
| 7 | ig34_p0123_a011 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 123 行 3; ML/examples.md:18 | 同 #5: 勾选 Meal, 2015 Dec 31 / 19:00 / CE003 一致; 记号格式改写. |
| 8 | ig34_p0123_a016 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 123 DILI Meal CRF 行 1; ML/examples.md:27 | Wild mushrooms / X Yes / 2015 DEC 24 一致 (PDF "2015  DEC 24" 双空格属空白). PDF "X Yes" + "No", KB "[X] Yes \| [ ] No" → 记号格式改写. |
| 9 | ig34_p0123_a017 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 123; ML/examples.md:28 | Ackee fruit / X No / 日期空 一致; 记号格式改写. |
| 10 | ig34_p0123_a018 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 123; ML/examples.md:29 | Cycad seeds / X No / 日期空 一致; 记号格式改写. |
| 11 | ig34_p0141_a005 | PRE_EXISTING | EXACT | HOLDS | 渲染页 141 Example 1 ae.xpt 行 3; `ig34_p0141.txt`:9-11; `knowledge_base/domains/AE/examples.md`:17 | 26 格逐格比: AEMODIFY 空; AEOUT "RECOVERING/ RESOLVING" (折行) = KB "RECOVERING/RESOLVING"; 渲染页上 Y/Y 在 AESHOSP、AESLIFE 列, AESCONG/AESDISAB/AESDTH/AESMIE 空 — KB 同; TREATMENT / 2005-10-21 / AEENDTC 空 / 9 / AEENDY 空 / AFTER 一致. 原子 verbatim 把 Y/Y 错位到 AESCONG/AESDISAB, 属抽取错, KB 按 PDF 写对. |
| 12 | ig34_p0141_a013 | PRE_EXISTING | EXACT | HOLDS | `ig34_p0141.txt`:23-24; AE/examples.md:32 (Example 2) | 19 格逐格一致, AEENDTC = 2005-10-13T19:00 (PDF 两行拼接). 原子 verbatim 写成 "2005-10-19:00" 为抽取错, KB 正确. |
| 13 | ig34_p0146_a003 | PRE_EXISTING | EXACT | HOLDS | 渲染页 146 bs.xpt 行 1; `ig34_p0146.txt`:3-4; `knowledge_base/domains/BE/examples.md`:41 | 19 格一致: BSGRPID 空, BSREFID 1148.267, BSORRES 2 / cm3 / BSSTRESC 2 / BSSTRESN 2 / cm3, CEREBRAL AQUEDUCT, 1, 2005-03-20. 原子 verbatim 漏了 2/2/2 三个值 (抽取错). |
| 14 | ig34_p0146_a004 | PRE_EXISTING | EXACT | HOLDS | 渲染页 146 行 2; `ig34_p0146.txt`:5-6; BE/examples.md:42 | 一致: 267FF / 1148.267 / TEMP / Temperature / SPECIMEN HANDLING / -80 / C / -80 / -80 / C / BRAIN / CEREBRAL AQUEDUCT / 1 / 2005-03-20. 原子漏 BSSTRESN -80 (抽取错). |
| 15 | ig34_p0146_a030 | PRE_EXISTING | EXACT | HOLDS | 渲染页 146 be.xpt 行 4; `ig34_p0146.txt`:39; BE/examples.md:85 | 16 格一致: SPDEVID PURKIT, BEREFID 298R1-1R0, BEPRTYID 空, EXTRACTION, 2, 2010-04-01T11:50 / 2010-04-02T9:00 / 2010-04-05T13:50. 原子 "298R1-R0" 为抽取错. |
| 16 | ig34_p0147_a024 | PRE_EXISTING | EXACT | HOLDS | 渲染页 147 bs.xpt 行 2; `ig34_p0147.txt`:29; BE/examples.md:123 | 17 格一致: BSREFID 298B1-1, 7 / mL / 6 / 6 / mL / PLASMA / 2 / 2010-04-01T11:50. 原子 "298B1" 和空的 6/6 为抽取错. |
| 17 | ig34_p0147_a025 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 147 bs.xpt 行 3 (放大确认 BSREFID 印为 "298B1-1R0"); `ig34_p0147.txt`:30; BE/examples.md:124; registry `B-BE T-3` | 其余 16 格一致 (VOLUME / Volume / SPECIMEN MEASUREMENT / 6 / mL / 6 / 6 / mL / RNA / 2 / 2010-04-01T11:50). 唯一差异 BSREFID: PDF "298B1-1R0", KB "298R1-1R0" — 已登记 PDF 笔误 `B-BE T-3` (handling "KB 写正确值", 依据 be r4 / suppbe / relspec 均 298R1-1R0), 不算 NOT_HOLD. 但 KB ≠ PDF 字面, EXACT 不成立, 标签级别应为 PDF_TYPO (此处按口径归入 HOLDS_AS_EQUIV 登记). |
| 18 | ig34_p0153_a0002 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 153 Bone Fracture Assessment 第 1 行; `knowledge_base/domains/CE/examples.md`:74 | 内容一致 (问题 "Which fracture?", 两个 ○ 选项 Pre-study / On-study fracture, reference number + 填空线). 差异: PDF 两选项在同格内分两行, KB 合并为一格用双空格分隔; 填空线 PDF "number_____" (无空格、5 下划线), KB "number ___" (加空格、3 下划线) → 格式差, 非逐字. 原子 "o" 代替 "○" 为抽取问题. |
| 19 | ig34_p0182_a007 | PRE_EXISTING | EXACT | HOLDS | 渲染页 182 Example 1 行 2; `ig34_p0182.txt`:8; `knowledge_base/domains/DA/examples.md`:12 | 19 格一致 (XBYCC-E990A / A375827 / RETAMT / Bottle A / 5 / TABLET / 5 / 5 / TABLET / 2 / Study Med Period 1 / 2004-07-15). 原子多了空格位 (抽取错). |
| 20 | ig34_p0182_a009 | PRE_EXISTING | EXACT | HOLDS | 渲染页 182 Example 1 行 4; `ig34_p0182.txt`:10; DA/examples.md:14 | PDF 行 4 DAORRES/DASTRESC/DASTRESN = 0/0/0, KB :14 同 (0 \| TABLET \| 0 \| 0). 原子写 "10" 为抽取错 (混了行 5/6 的 10). |
| 21 | ig34_p0182_a016 | PRE_EXISTING | EXACT | HOLDS | 渲染页 182 Example 2 行 1; `ig34_p0182.txt`:19; DA/examples.md:26 | 17 格一致 (AB001 / DISPAMT / Dispensed Amount / Study Medication / Drug A / 1 / CONTAINER / 1 / 1 / CONTAINER / 1 / 2004-06-15). 原子漏 DASTRESU CONTAINER (抽取错). |
| 22 | ig34_p0182_a017 | PRE_EXISTING | EXACT | HOLDS | 渲染页 182 Example 2 行 2; `ig34_p0182.txt`:20; DA/examples.md:27 | 同 #21, AB002 / Drug B, 逐格一致. |
| 23 | ig34_p0182_a025 | PRE_EXISTING | EXACT | HOLDS | 渲染页 182 Example 3 行 1; `ig34_p0182.txt`:29; DA/examples.md:43 | 17 格一致 (DAGRPID 1, DASPID 1, PREPAMT, 100 mL 100 100 mL, 2017-05-19, 1). 原子漏 DAGRPID/DASPID (抽取错). |
| 24 | ig34_p0182_a026 | PRE_EXISTING | EXACT | HOLDS | 渲染页 182 Example 3 行 2; `ig34_p0182.txt`:30; DA/examples.md:44 | 一致 (1 / 1 / REMAMT / Remaining Amount / 15 / mL / 15 / 15 / mL / 2017-05-19 / 1). |
| 25 | ig34_p0182_a028 | PRE_EXISTING | EXACT | HOLDS | 渲染页 182 Example 3 行 4; `ig34_p0182.txt`:32; DA/examples.md:46 | 一致 (DAGRPID 2 / DASPID 2 / REMAMT / 25 / mL / 25 / 25 / mL / 2017-05-19 / 1). 原子 DASPID 空、多一个 25 为抽取错. |
| 26 | ig34_p0190_a014 | PRE_EXISTING | EXACT | HOLDS | 渲染页 190 Example 1 行 12; `ig34_p0190.txt`:26-27; `knowledge_base/domains/EG/examples.md`:36 | 24 格一致: EGCAT 空, SUPINE, ABNORMAL / 空 / ABNORMAL, EGSTRESN~EGCLSIG 全空 (含 EGXFN、EGNAM 空, 渲染页确认), VISITNUM 1, VISIT "Screening 1" (渲染页折行), 2003-04-15T11:58, -36. 原子把 VISIT 写成 "Screening" 漏 "1" 为抽取错. |
| 27 | ig34_p0191_a001 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 191 行 4; `ig34_p0191.txt`:2-3; EG/examples.md:67 | 所有值逐格一致 (2324-P0001 / 4 / QTAG / QT Interval, Aggregate / INTERVAL / SUPINE / 440 msec 440 440 msec / 12 LEAD STANDARD / LEAD II / 空 / 2 / VISIT 2 / 2014-03-22T10:00:21 / 1 HR / 1). 差异: PDF 省略列记号为单字符 "…" (U+2026), KB 写三个点 "..." — 不在允许的归一项内, 非逐字. |
| 28 | ig34_p0191_a003 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 191 行 6; `ig34_p0191.txt`:6-7; EG/examples.md:69 | 值逐格一致 (RRAG / RR Interval, Aggregate / 679 ×3 / 2014-03-22T10:01:35 / 1 HR / EGREPNUM 2). 差异同 #27: "…" → "...". |
| 29 | ig34_p0191_a005 | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | 渲染页 191 行 8; `ig34_p0191.txt`:10-11; EG/examples.md:71 | 值逐格一致 (QTAG / 389 ×3 / 2014-03-22T10:01:35 / 1 HR / 2). 差异同 #27: "…" → "...". |

## 计数

| 层 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE | 合计 |
|---|---|---|---|---|---|
| PRE_EXISTING | 18 | 11 | 0 | 0 | 29 |

- HOLDS (18): #1, 2, 3, 4, 11, 12, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26
- HOLDS_AS_EQUIV (11): #5-10 (ML 勾选记号 "[X]/[ ]" 改写), #17 (已登记 PDF 笔误 `B-BE T-3`, 应为 PDF_TYPO 标签), #18 (CE 两选项合格 + 填空线写法), #27-29 (EG "…" → "...")
- NOT_HOLD: 无; UNVERIFIABLE: 无 → 本层按 brief 口径通过 (NOT_HOLD 0 且 UNVERIFIABLE 0), 不触发 Q9 升级.

附注 (标签级别, 不影响内容判定): #3、#4 原子 verbatim 本身抽错 (#3 表头切分/漏列, #4 混行), KB 按 PDF 写对, 严格说标签应为 ATOM_ERR 而非 EXACT; #11-16、#19-26 原子也有漏格 / 错位 / 错值, 但 KB 都按 PDF 写对. 这解释了这批旧 EXACT 为何指纹复验 "命中不了": 指纹取自错误的原子文本, 而非 KB 缺内容.

## 样本外发现的 KB 内容问题

无实质内容问题 (不修, 仅记录格式观察):
- `knowledge_base/domains/CE/examples.md`:71-72 — KB 给 Bone Fracture Assessment 表加了 PDF 没有的表头行 "Question \| Response Options", 并把 PDF 表首行标题 "Bone Fracture Assessment" 移到粗体标题 "CRF: CE Example 3 — Bone Fracture Assessment" (PDF 页 153). 纯格式.
- `knowledge_base/domains/ML/examples.md`:14 — Meal Log CRF 表头 "Type" 在 PDF 是跨 3 列合并格, KB 写成 "Type \| \| \|" (PDF 页 123). 纯格式.
