# T4.1 第三轮补检 — 包 7 (R3_PDF_TYPO, T151-T175) 独立审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间 (date -u): 2026-11-27T06:37:34Z
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` 的 R3_PDF_TYPO 层 (三件事: ① PDF 确有登记问题; ② KB 与 handling 一致; ③ 其余内容 KB = PDF, 表格行逐格)
- 看过的渲染页 (SDTMIG v3.4, 300 dpi 局部裁切): p10, p18, p41, p63, p68, p89, p107, p113, p115, p118, p119, p123, p132, p142 (两处: 表左半 + 表右半/Row 2 说明), p146 (两处), p152, p160, p165, p166, p170, p173
- 用过的命令:
  - `pdftotext -bbox -f N -l N "source/cdisc/SDTMIG v3.4 (no header footer).pdf" -` 定位词坐标; `pdftoppm -r 300 -f N -l N -x X -y Y -W W -H H -png -singlefile <pdf> <out>` 裁切 (脚本 `scratchpad/r3_7/crop.py`, 不在仓内)
  - 登记: `python3` 按 id 读 `work/t2_pdf_typo_registry.jsonl`; 决策: `work/t3_writeback_decisions.json`; 台账: `grep work/coverage_ledger.wc.jsonl`
  - KB: `sed -n` 读 `knowledge_base/domains/{DM,DS,HO,BE,MH}/...` 相关行; MH 引号字节: python `hex(ord(c))`

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 | 说明 |
|---|---|---|---|---|---|---|
| T151 | ig34_p0010_a023 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p10 (MANY → "--LNKID (and not --LNKGRP)"); `knowledge_base/chapters/ch01_introduction.md:109` | 登记 B-ch01 T-2. PDF 两句 ONE/MANY 都写 --LNKID, KB MANY 处改 --LNKGRP (and not --LNKID); 整段其余逐字一致 |
| T152 | ig34_p0018_a012 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p18 BE 行 Keys 格 "BESDTC"; `knowledge_base/chapters/ch03_submitting_data.md:37` | 登记 B-ch03 T-1. 其余 7 格 (BE / Biospecimen Events / Events / Structure / Tabulation / 其余 keys / be.xpt) 逐格一致 |
| T153 | ig34_p0041_a038 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p41 "foreword slash"; `knowledge_base/chapters/ch04_general_assumptions.md:863` | 登记 B-ch04 N-1 (handling KB 写正确值; basis 字段写 "照录" 是措辞残留, 以 handling 为准). KB "forward slash", 其余逐字 |
| T154 | ig34_p0063_a023 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p63 ETHNIC 行 "guidance¹" (RACE 行为 ²); `knowledge_base/domains/DM/spec.md:203-210`; 脚注 `DM/spec.md:294,296` | 登记 S-SPEC1 T-1. ¹ 是 "In this column, an asterisk…" 脚注, ² 才是 FDA guidance, 问题属实. KB 改 ². 其余格: Ethnicity / Char / (ETHNIC) / Record Qualifier / Notes / Perm 一致; KB 另加 NCI 码 C66790 与 Order 23 (KB spec 通用附加, 非改值) |
| T155 | ig34_p0068_a010 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p68 Ex1 Row 6 RACE 格 "…PACIFIC ISLANDERS"; `knowledge_base/domains/DM/examples.md:14` (表头 :6, 26 列) | 登记 B-DM T-2. 逐格比对 PDF Row 6: ABC123/DM/ABC12302002/02002/2006-02-03/2006-04-05/2006-02-03/2006-04-05/2006-01-10/2006-04-25/02/GONZALEZ, E/1956-05-05/49/YEARS/F/RACE/NOT HISPANIC OR LATINO/A/Drug A/A/Drug A/空/空/USA, KB 全同 (仅 RACE 末 S 去掉). 注: 原子抽错 (原子 verbatim 日期/INVNAM/BRTHDTC 与 PDF 不符), 不影响判定 |
| T156 | ig34_p0089_a026 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p89 Row 5 句末无句点 (Row 4/6 有); `knowledge_base/domains/SV/examples.md:40` | 登记 B-SV T-1. KB 补句点, 其余逐字 |
| T157 | ig34_p0107_a002 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p107 第 5 条末尾确实印有 "document.Additional interventions qualifiers", 下一行 "6. Additional interventions qualifiers"; `knowledge_base/domains/EX/assumptions.md:41,43` | 登记 S-INT EX T-7. 渲染页确认重复文字是可见印刷 (非文本层伪影). KB 第 5 条止于 "Define-XML document.", 第 6 条标题保留; 其余逐字 |
| T158 | ig34_p0113_a011 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p113 第 3 个 bullet "from ottles A, B and C"; `knowledge_base/domains/EX/examples.md:118` | 登记 B-EX T-3. KB "bottles", 其余逐字 |
| T159 | ig34_p0115_a009 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p115 "protocol specified unit"; `knowledge_base/domains/EX/examples.md:207` | 登记 B-EX T-4. KB "protocol-specified", 其余逐字 |
| T160 | ig34_p0118_a017 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p118 "Scheduled dose is represented in mg/mL."; `knowledge_base/domains/EX/examples.md:362` | 登记 B-EX T-6. KB "mg/kg", 同行 Rows 1, 3, 5 前半句一致 |
| T161 | ig34_p0119_a011 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p119 "using --LNKID, ."; `knowledge_base/domains/EX/examples.md:403` | 登记 B-EX T-2. KB "using --LNKID.", 其余逐字 |
| T162 | ig34_p0123_a005 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p123 "occurrence of of prespecified"; `knowledge_base/domains/ML/examples.md:8` | 登记 B-ML T-2. KB 去重词, 其余逐字 |
| T163 | ig34_p0132_a014 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p132 "(SUENTTP = "2006-01-01""; `knowledge_base/domains/SU/examples.md:19` | 登记 B-SU T-1. KB "SUENTPT", 其余 (SUSTTPT/SUSTRTPT/SUENRTPT 值、Section 4.4.7 引用) 逐字 |
| T164 | ig34_p0142_a012 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p142 Row 2 说明 "…probably related to the event."; `knowledge_base/domains/AE/examples.md:75` | 登记 B-AE T-3 (cat 知悉, 改词判断). KB "to the device", 其余逐字 |
| T165 | ig34_p0142_a014 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p142 Ex5 表头首格空白; `knowledge_base/domains/AE/examples.md:79` | 登记 B-AE T-4. KB 首格 "Row", 其后 29 个列名与 PDF 逐个一致 (STUDYID…AEENDY) |
| T166 | ig34_p0142_a015 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p142 Row 1 (左半 + 右半两张裁切): AESTDTC 2018-04-21, AEENDTC 2014-04-26, AESTDY 5, AEENDY 10; `knowledge_base/domains/AE/examples.md:81` | 登记 B-AE T-1. 逐格: T002/AE/002/HipX22/1/AE0099/Twisted left ankle/SPRAIN/ANKLE JOINT/LEFT/N/MILD/NONE/NOT RELATED/RECOVERED/RESOLVED/N/N/N/N/N/N/N/Y/N/Y/2018-04-21/[2014→2018]-04-26/5/10, KB 全同. 注: 原子抽错 (原子 AESER=Y、AESTDTC 2018-04-26、AESTDY 15 等与 PDF 不符) |
| T167 | ig34_p0142_a016 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p142 Row 2 AEOUT "RECOVERED/ RESOLVED WITH SEQUELLAE"; `knowledge_base/domains/AE/examples.md:82` | 登记 B-AE T-2. 逐格: …Y/MODERATE/REMOVED/PROBABLE/[SEQUELAE]/N/Y/Y/N/N/N/Y/Y/N/N/2018-05-01/2018-05-10/15/25, KB 全同 |
| T168 | ig34_p0146_a005 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p146 bs Row 3: BSORRES/BSSTRESC "DRY ICE/ISOPOPANOL", BSDTC "5-0"; `knowledge_base/domains/BE/examples.md:43` | 登记 B-BE T-1 + B-BE T-2. KB 两格改 ISOPROPANOL、BSDTC 改 2005-03-20 (同组 r1/r2 为 2005-03-20). 其余逐格: ABC134/BS/43871/3/267FF/1148.267/FFRZMAT/Flash Freeze Material/SPECIMEN HANDLING/空 BSORRESU/空 BSSTRESN/空 BSSTRESU/BRAIN/CEREBRAL AQUEDUCT/1 一致 |
| T169 | ig34_p0152_a0019 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p152 "Topic Variables,for" (渲染确认逗号后无空格, 非文本层丢空格); `knowledge_base/domains/CE/examples.md:54` | 登记 B-CE T-1. KB 补空格, 其余逐字 |
| T170 | ig34_p0160_a0026 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p160 "DS record and in the AE record"; `knowledge_base/domains/DS/examples.md:87` | 登记 B-DS U-4. KB 删 "in", 同段前句逐字 |
| T171 | ig34_p0160_a0028 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p160 "…ended. (DSDTDTC)."; `knowledge_base/domains/DS/examples.md:89` | 登记 B-DS T-3. KB "(DSSTDTC).", 其余逐字 |
| T172 | ig34_p0165_a0007 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p165 se Row 5 ETCD "SCREEN"; `knowledge_base/domains/DS/examples.md:298` (包内指针 :294 是 Row 1, 登记 span_lines [294, 298] 覆盖本行) | 登记 B-DS U-1. 逐格 Row 5: XYZ/SE/XYZ-767-002/1/[SCREEN→SCRN]/Screen/2016-02-04/2016-02-21/1/SCREENING, KB 全同 |
| T173 | ig34_p0166_a0035 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p166 "recieved"; `knowledge_base/domains/DS/examples.md:377` | 登记 B-DS T-5. KB "received", 其余逐字 |
| T174 | ig34_p0169_a0024 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p170 Ex1 ho Row 5 HOTERM "REHABILIATION FACILITY"; `knowledge_base/domains/HO/examples.md:25` | 登记 B-HO T-1. 逐格 Row 5: ABC/HO/ABC123102/3/[REHABILITATION] FACILITY/TREATMENT/2011-08-15/2011-08-20/空, KB 全同. 注: 原子严重抽错 — verbatim "5 / ABC123105 / 1 / GENERAL WARD / 2011-09-09…" 不对应 PDF 任一行 (拼了 Row 5 行号、Row 3 HOTERM、Row 6 日期), 原子页号 p169 而表在 p170; 按行号 5 + 登记 + 台账 discrepancy 对到 PDF p170 Row 5 核. 原子→行的映射依赖推断, 主控可自行复核 |
| T175 | ig34_p0173_a0007 | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染 p173 "“Allergy Medical History, “"; `knowledge_base/domains/MH/assumptions.md:27` | 登记 B-MH T-3. KB 去掉逗号后空格 → "“Allergy Medical History,“"; 按弯直引号归一 = 登记 kb_value "\"Allergy Medical History,\"". 注: KB 闭引号字节是 U+201C (左引号方向), 与 PDF 同句 "General Medical History“" 的同类方向错一样照录 (该处 KB = PDF, 未登记但不构成差异) |

## 计数

| 层 | HOLDS | NOT_HOLD | UNVERIFIABLE |
|---|---|---|---|
| R3_PDF_TYPO (T151-T175) | 25 | 0 | 0 |

## 样本外发现

- 无 KB 内容问题. 两点备注 (不算判定):
  - `knowledge_base/domains/MH/assumptions.md:27`: "General Medical History“" 与 "Allergy Medical History,“" 的闭引号都是 U+201C (PDF p173 原样); 若要求排版完美, 可作标签外观察项.
  - 原子抽错 (verbatim 与 PDF 不符) 出现在 T155 / T166 / T174, 已在说明栏注明; T174 程度最重 (原子内容不对应 PDF 任一行).
