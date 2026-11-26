# T2S S-MOD2 writer checkpoint (扫描批: model/02_observation_classes.md, 源 SDTM v2.0)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `669405f`; 改前文件 md5 `2180f14252707992e232175953dd0e5d` (= HEAD, 316 行) → 改后 `ec1887ae0f7e9c798411bfa767c9d5db` (389 行).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-MOD2_writer/`
  (base.md = 改前副本; rows.py = 原子表行解析; **bbox_tbl.py = `pdf_bbox/sv20_p00NN.tsv` 词框按表头 x 分列, 每行 12 列** (不依赖原子); pdf_tabs.json = 5 张 PDF 表 bbox 解析结果; gen.py = 生成改后文件 (逐行断言 #/Type 与 PDF 一致); verify.py = 改后 KB 全部表格 # / Variable / Label / Type / Format / Role 逐格对 bbox; scan.py = 非表原子 PDF→KB; notes.py / celltab.py = Key Notes 格分类; 渲染 p11-p39 全部 29 页 80dpi `p-NN.png` 逐页目视)
- 真值顺序: 渲染图 > bbox 分列 > layout 文本 > 原子. 原子错 1 处: `sv20_p0037_a001` (--CHDY) Label 原子作 "Day of Obs Relative to Challenge Agent", bbox + 渲染 p37 均为 "Day of Obs **Rel** to Challenge Agent" (= KB, 未改).

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| model/02_observation_classes.md | §3 + §3.1 (3.1.1-3.1.5) | 11-39 | **11-39** | p11 顶部 `3 Study Subject Data` (a001), 同页 `3.1 The General Observation Classes` (a014); p39 = Timing 表末行 48 --PDUR, 页下部空白; p40 首行 `3.2 Special-purpose Domains` (layout `sv20_p0040.txt`) → 不归本批. p10 末为 §2 内容 |

### 口径
- **R1 (t1_user_ack)**: v2.0 变量表行 model/ 收 5 列 (#/Variable/Label/Type/Role) 认 IE, 缺列 (Format/Variable(s) Qualified/Usage Restrictions/Variable C-code/Definition/Notes/Examples) 不补. R1 豁免的是**列**, 不是行: 5 列 floor 以内 KB 必须有且与 PDF 一致 → (1) Findings 表 KB 只收 16/100 行且拆成 4 张无 # 子表 → 按规则 3 重建为 1 张 100 行表; (2) Timing 7 张子表缺 Role 列 → 补 Role (全为 Timing); (3) FA 表缺 # → 补.
- Role 写法沿用 model/ 约定 `Role (Variable(s) Qualified)` (多个用 `/`, O35/O38 已挂 T4), 但括注内容须与 PDF Qualified 全列一致.
- 既有 Format 列 (Date/Time 子表) 属已收列 → 值照 PDF.
- Key Notes / Notes 列 (KB 自写, 混合 PDF Definition/Notes/Examples/Usage Restrictions, 不对应任何单一 PDF 列): R1 未裁, 先例分歧 (O35 挂 T4; B-model06 M-2b 是 KB 列 = PDF Notes 列时才恢复原文). 本 attempt 只做: 逐格分类 (见逐格表) + **与 PDF 矛盾的 6 格 D2 改为 PDF 原文**; 其余列改造与否 → 需主控定 M-1. Findings 新增 84 行的 Key Notes 填 PDF Usage Restrictions 原文 (与本文件 INT/EVT/ID/TIM 各表 Key Notes 一律承载 Usage Restrictions 的既有惯例一致; 无 Usage 的行留空, 不自写) → 需主控定 M-2.
- D6 措辞 `> KB note (not in SDTM v2.0):`.

### 双向全扫 — 逐页日志
方法: PDF→KB 非表原子 (HEADING/SENTENCE/LIST_ITEM, 53 条) = scan.py 归一子串 → 改后 **HIT 53 MISS 0** (改前 HIT 43 MISS 10). 表行 = bbox 分列 (每页 12 列) 逐格对 KB, 改后 verify.py **1059 格 0 DIFF**, 6 表行序全与 PDF 一致 (INT 43 / EVT 56 / FND 100 / FA 1 / ID 16 / TIM 48 = 264 行); 每页渲染目视核. KB→PDF = 逐行读改后全文: 非 PDF 内容只有 H1/Source 行、KB 分组小标题 (`### Topic and Qualifier Variables (N variables)`、Timing 7 个 `###`)、2 处 D6 KB note、Key Notes 列 (M-1).

| 页 | 节 | PDF→KB: 句/列表/标题 原子 数 / 命中 / 缺→已补; 表行 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 11 | §3 / §3.1 | 32 / 32 / 0 | :5-31 逐字 (B-model01 已修); 无出处 0 | — | a032 句跨页 (p12 a001 续), 合并后命中 |
| 12 | §3.1 尾 / §3.1.1 | 4 / 4 / 1→1 (a004 表题); 表行 12 | :33 :35 一致; 旧 `**Structure:** One Record per…` 为 a004 改写 → D2 删 (D-1) | INT 1-12 逐格一致 | 表题插 :39 |
| 13 | §3.1.1 | 0 / 0 / 0; 表行 12 | INT 13-24 | 逐格一致 | --FTDOSD Key Notes 矛盾 → D2 (#C-2) |
| 14 | §3.1.1 | 0; 表行 15 | INT 25-39 | 逐格一致 | --METHOD / --VAMT Key Notes 矛盾 → D2 (#C-3/#C-4); --ADJ 例子跨 p15 |
| 15 | §3.1.1 尾 / §3.1.2 | 2 / 2 / 1→1 (a006 表题); 表行 12 (INT 40-43, EVT 1-8) | 旧 EVT `**Structure:**` → D2 删 (D-2) | 逐格一致 (本页双表头, bbox 后段列位以首表头为准, 后 8 行 Usage/C-code 粘连, 已对渲染) | 表题插 :91 |
| 16 | §3.1.2 | 0; 表行 13 | EVT 9-21 | 逐格一致 | |
| 17 | §3.1.2 | 0; 表行 15 | EVT 22-36 | 逐格一致 | --ACNDEV Key Notes "AE domain only" 但 PDF Usage 空 → D2 (#C-5) |
| 18 | §3.1.2 | 0; 表行 10 | EVT 37-46 | 逐格一致 | |
| 19 | §3.1.2 | 0; 表行 5 | EVT 47-51 | 逐格一致 | |
| 20 | §3.1.2 尾 / §3.1.3 | 2 / 2 / 1→1 (a007 表题); 表行 6 (EVT 52-56, FND 1) | 旧 FND `**Structure:**` → D2 删 (D-3) | 逐格一致 | 表题插 :158 |
| 21 | §3.1.3 | 0; 表行 4 | FND 2-5 (3-5 新增) | 逐格一致 | |
| 22 | §3.1.3 | 0; 表行 7 | FND 6-12 (全新增) | 逐格一致 | |
| 23 | §3.1.3 | 0; 表行 2 | FND 13-14 (新增) | 逐格一致 | |
| 24 | §3.1.3 | 0; 表行 11 | FND 15-25 (新增) | 逐格一致 | |
| 25 | §3.1.3 | 0; 表行 8 | FND 26-33 (28/29/33 既有) | 逐格一致 | --ORRESU Role 括注补全; --ORNRLO Label 改 |
| 26 | §3.1.3 | 0; 表行 7 | FND 34-40 | 逐格一致 | --ORNRHI / --STRESC Label 改; --STRESU Role 括注补全 (8 个) |
| 27 | §3.1.3 | 0; 表行 10 | FND 41-50 | 逐格一致 | --STNRLO/--STNRHI/--STNRC/--NRIND Label 改 |
| 28 | §3.1.3 | 0; 表行 14 | FND 51-64 (新增) | 逐格一致 | |
| 29 | §3.1.3 | 0; 表行 12 | FND 65-76 (66/68/69 既有) | 逐格一致 | --SPCUFL Key Notes '"Y" or null' 与 PDF Notes ("N"/null) 矛盾 → D2 (#C-6); --SPEC/--SPCCND 例值无 PDF 依据 (M-1) |
| 30 | §3.1.3 | 0; 表行 10 | FND 77-86 (新增) | 逐格一致 | 旧 "Additional Findings-specific Variables include …" 占位删 (D-6) |
| 31 | §3.1.3 | 0; 表行 9 | FND 87-95 (新增) | 逐格一致 | |
| 32 | §3.1.3 尾 / §3.1.3.1 / §3.1.4 | 8 / 8 / 4→4 (a006 标题, a007 句, a009 表题, a008 既有); 表行 6 (FND 96-100, FA 1) | 旧 `### Findings About (Subtype)` + 改写 2 句 → D2 删 (D-7/D-8); §3.1.4 :275-277 逐字 | FND 96-100 / FA 1 逐格一致 | --OBJ Notes 格 = PDF Notes 逐字 |
| 33 | §3.1.4 | 1 / 1 / 1→1 (a001 表题); 表行 9 | ID 1-9 | 逐格一致 | 表题插 :279 |
| 34 | §3.1.4 尾 / §3.1.5 | 3 / 3 / 2→2 (a009 句恢复原文, a010 补); 表行 7 | 旧 a009 尾 "(48 variables):" KB 拼接 → 恢复 PDF 句 (D-9) | ID 10-16 逐格一致 | |
| 35 | §3.1.5 | 1 / 1 / 1→1 (a001 表题); 表行 12 | TIM 1-12; D6 KB note :306 (子表拆分说明) | 逐格一致 (补 Role; --DTC/--STDTC/--ENDTC Format 改) | |
| 36 | §3.1.5 | 0; 表行 11 | TIM 13-23 | 逐格一致 | |
| 37 | §3.1.5 | 0; 表行 7 | TIM 24-30 | 逐格一致 | --CHDY Label = "Rel" (原子错, 见上) |
| 38 | §3.1.5 | 0; 表行 11 | TIM 31-41 | 逐格一致 | --STRF/--ENRF/--STRTPT/--ENRTPT Notes 值列举无 PDF 依据 (M-1) |
| 39 | §3.1.5 | 0; 表行 7 | TIM 42-48 | 逐格一致 | --PDUR Label 改; --PTFL/--PDUR Notes 补全 Usage 域列表 |

### 变更清单
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | model/02:39 | pdf:p12:sv20_p0012_a004 | INSERTED | 表题 `**Interventions—Topic and Qualifier Variables—One Record per …**` | 12 |
| 2 | model/02:91 | pdf:p15:sv20_p0015_a006 | INSERTED | 表题 `**Events—…—One Record per Event**` | 15 |
| 3 | model/02:158 | pdf:p20:sv20_p0020_a007 | INSERTED | 表题 `**Findings—…—One Record per Finding**` | 20 |
| 4 | model/02:160-261 | pdf:p20-32:Findings 表 100 行 | TABLE_REBUILT | 4 张子表 (16 行, 无 #, 2 张无 Type/Role) + 占位句 → 单表 100 行 `# / Variable / Label / Type / Role / Key Notes`, 行序 = PDF; 新增 84 行 | 20-32 |
| 5 | model/02:198 | pdf:p26:FND 37 --STRESC | REPLACED | Label "Character Result/Finding in Std Format" → "Result or Finding in Standard Format" | 26 |
| 6 | model/02:194/195 | pdf:p25-26:FND 33/34 | REPLACED | --ORNRLO/--ORNRHI Label "Reference Range … in Orig Unit" → "Normal Range Lower/Upper Limit-Original Units" | 25-26 |
| 7 | model/02:202/203 | pdf:p27:FND 41/42 | REPLACED | --STNRLO/--STNRHI Label "Reference Range …-Std Units" → "Normal Range Lower/Upper Limit-Standard Units" | 27 |
| 8 | model/02:204 | pdf:p27:FND 43 --STNRC | REPLACED | "Reference Range for Char Rslt-Std Units" → "Normal Range for Character Results" | 27 |
| 9 | model/02:207 | pdf:p27:FND 46 --NRIND | REPLACED | "Reference Range Indicator" → "Normal/Reference Range Indicator" | 27 |
| 10 | model/02:190 | pdf:p25:FND 29 --ORRESU | REPLACED | Role "(--ORRES)" → "(--ORRES/--ORNRLO/--ORNRHI/--ORREF)" | 25 |
| 11 | model/02:201 | pdf:p26:FND 40 --STRESU | REPLACED | Role "(--STRESC/--STRESN)" → 8 个 Qualified 全列 | 26 |
| 12 | model/02:263 | pdf:p32:sv20_p0032_a006 | INSERTED | `### 3.1.3.1 Findings About Events or Interventions` (取代 KB 自拟 `### Findings About (Subtype)`, 全仓入站锚点 0) | 32 |
| 13 | model/02:265 | pdf:p32:sv20_p0032_a007 | INSERTED | FA 首句原文 (旧改写 2 句 D2 删, a008 原句保留) | 32 |
| 14 | model/02:267 | pdf:p32:sv20_p0032_a009 | INSERTED | 表题 `**Findings About—Additional Qualifier Variables**` | 32 |
| 15 | model/02:269-271 | pdf:p32:FA 表 | REPLACED | 补 `#` 列 (1) | 32 |
| 16 | model/02:279 | pdf:p33:sv20_p0033_a001 | INSERTED | 表题 `**All Observation Classes—Identifiers**` | 33 |
| 17 | model/02:302 | pdf:p34:sv20_p0034_a009 | REPLACED | 句尾 KB 拼接 " (48 variables):" → PDF 原句 "…implementation guides." | 34 |
| 18 | model/02:302 | pdf:p34:sv20_p0034_a010 | INSERTED | "See Section 3.2, Special-purpose Domains, for additional guidance …" | 34 |
| 19 | model/02:304 | pdf:p35:sv20_p0035_a001 | INSERTED | 表题 `**All Observation Classes—Timing Variables**` | 35 |
| 20 | model/02:306 | KB_AUTHORED | D6 | `> KB note (not in SDTM v2.0):` 说明 KB 把 PDF 单表拆成 7 张子表 (行号随 PDF) | 35 |
| 21 | model/02:310-389 | pdf:p35-39:TIM 48 行 Role | REPLACED | 7 张子表补 Role 列 (全 "Timing") | 35-39 |
| 22 | model/02:326-328 | pdf:p35:TIM 10-12 Format | REPLACED | "ISO 8601" → "ISO 8601 datetime or interval" ×3 | 35 |
| 23 | model/02:389 | pdf:p39:TIM 48 --PDUR | REPLACED | Label "Planned Duration of Observation" → "Planned Duration" | 39 |
| 24 | model/02:388/389 | pdf:p39:TIM 47/48 Usage | REPLACED | Notes "Only in Findings class specimen-based domains" → 补 ": BS, CP, GF, IS, LB, MB, MS, MI, PC, PP" (R2 截断) | 39 |
| 25 | model/02:156 | KB_AUTHORED | D6 | "The Findings class has the largest number of variables…" 加 `> KB note (not in SDTM v2.0):`; 尾 "Key variable groups include:" 删 (D-4) | — |
| C-1 | model/02:51 | pdf:p12:INT 9 --REASOC | REPLACED (D2) | Key Notes "Reason the **event** did or did not occur" (本表为 Interventions) → PDF Notes 原文 "--REASOC is the reason the intervention …" | 12 |
| C-2 | model/02:63 | pdf:p13:INT 21 --FTDOSD | REPLACED (D2) | "Multiplier for the value represented by --DOSE and --DOSU" (语义倒置) → PDF Notes "The quantity given for the multiplier of --TDOSD." | 13 |
| C-3 | model/02:71 | pdf:p14:INT 29 --METHOD | REPLACED (D2) | '"INFUSION", "INTRAVENOUS"' (把 ROUTE 值当 METHOD 例) → PDF Examples '"INFUSION" when ROUTE is "INTRAVENOUS"' (+ 原 Usage 保留) | 14 |
| C-4 | model/02:79 | pdf:p14:INT 37 --VAMT | REPLACED (D2) | "Amount of diluent; not diluent amount alone" (自相矛盾) → PDF Definition + Notes 原文 | 14 |
| C-5 | model/02:129 | pdf:p17:EVT 35 --ACNDEV | REPLACED (D2) | "AE domain only" (PDF Usage Restrictions 空, 渲染 p17 核) → PDF Definition 原文 | 17 |
| C-6 | model/02:230 | pdf:p29:FND 69 --SPCUFL | REPLACED (D2) | '"Y" or null' (PDF: "N" 不可用 / null 可用) → PDF Notes 原文 | 29 |

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | :152-261 §3.1.3 | 4 张子表 + 4 个粗体组名 + 占位句 → 1 张 100 行表 (# 1-100 = PDF); 既有 16 行 Key Notes 原样随行迁入 (--SPCUFL 除外, C-6) | 规则 3 + R1 (5 列 floor 内行缺 = REAL_GAP) |
| S-2 | :263-271 FA | KB 自拟 H3 → PDF H3 `3.1.3.1 …`; 表加 # 列 | S-TDM 冗余标题口径 (入站锚点 0); 规则 3 |
| S-3 | :306-389 Timing | 7 张子表各加 Role 列; 子表 `###` 标题保留 (规则 6) 并加 D6 说明 | R1 5 列 floor |
| S-4 | :39/:91/:158/:267/:279/:304 | 6 个 PDF 表题 (粗体行) 插在表前 | B-model06 #12 先例 |

### 删除清单 (D2)
| # | 位置 (改前行) | 删除内容 (摘要) | 原因 | 保留 |
|---|---|---|---|---|
| D-1 | :37 | `**Structure:** One Record per Constant-dosing Interval or Intervention Episode` | a004 表题的残留改写 (该行不承载其他原子) | :39 PDF 表题 |
| D-2 | :89 | `**Structure:** One Record per Event` | 同上 (a006) | :91 |
| D-3 | :154 | `**Structure:** One Record per Finding` | 同上 (a007) | :158 |
| D-4 | :158 尾 | "Key variable groups include:" | KB 占位, 所指子表已并表 | :156 D6 句其余部分 |
| D-5 | :160-194 | 4 个粗体组名 (Topic / Result / Normal Range / Specimen-related Variables) + 4 张子表表头 | 并表 (S-1); 16 行数据全部迁入单表, 无信息丢失 (旧 Label 4 类为 SDTMIG 标签, 已按 v2.0 改) | :160-261 |
| D-6 | :196 | "**Additional Findings-specific Variables** include --LOINC … --LNKID, --LNKGRP, and many domain-specific variables." | KB 占位; 且把 Identifier 变量 --LNKID/--LNKGRP 列为 Findings 变量 = 与 PDF 矛盾 | 单表 100 行 / §3.1.4 表 |
| D-7 | :198 | `### Findings About (Subtype)` | 被 PDF 标题取代; `grep -rnE "02_observation_classes(\.md)?#" knowledge_base docs web/src tools .work/AGENT_GUIDE.md README.md` 无输出 (未截断) | :263 |
| D-8 | :200 前 2 句 | "The Findings About observation class is a subtype … It utilizes the Findings general observation class variables with the addition of the --OBJ variable." | a007 的 R2 残留改写 | :265 |
| D-9 | :233 尾 | " (48 variables):" | KB 拼进 PDF 句 | :302 PDF 句; 计数仍见 :306 KB note |
| D-10..15 | 原 :51 :63 :71 :79 :129 :194 | 6 格 Key Notes 旧值 | 与 PDF 矛盾 (C-1..C-6) | 同格 PDF 原文 |

### D6 标注清单
- :156 Findings 引言句 (KB 自写, 不矛盾).
- :306 Timing 子表拆分说明 (KB 新写, 说明结构差异).
- 未标: Key Notes 列 (待 M-1); `### Topic and Qualifier Variables (N variables)` ×3 与 Timing `###` ×7 (纯导航标题, 规则 6); H1 / `Source:` 行 (导航).

### PDF_TYPO
- 无. (原子错 sv20_p0037_a001 见上, 非 PDF 错.)

### census_items 处理 (15 张 C3 UNPARSEABLE → 改后 12 张)
| census (HEAD 行) | 改后位置 | 处理 | 逐格结果 |
|---|---|---|---|
| :41 INT | :41 (43 行) | 渲染 p12-15 逐格 | 核心 5 列 215 格一致; Key Notes D2 4 格 |
| :93 EVT | :93 (56 行) | 渲染 p15-20 | 核心 280 格一致; Key Notes D2 1 格 |
| :162 FND Topic / :169 Result / :179 Normal / :190 Specimen | 并入 :160 (100 行) | 渲染 p20-32 | 改前: Label 7 格 + Role 2 格与 PDF 不符, 84 行缺 → 改后 500 格一致 |
| :202 FA | :269 (1 行) | 渲染 p32 | 补 #; 其余一致 (Notes = PDF Notes 逐字) |
| :212 ID | :281 (16 行) | 渲染 p33-34 | 80 格一致 |
| :237 :251 :259 :279 :289 :302 :310 Timing ×7 | :310 :324 :332 :352 :362 :375 :383 | 渲染 p35-39 | 改前: Format 3 格 + Label 1 格不符, Role 列缺 → 改后 # / Variable / Label / Type / (Format) / Role 全一致 |
- `table_census.py --manifest $S/manifest.json` (sv20 11-39) → `KB tables: 12; status: {'UNPARSEABLE': 12}; diffs: 0` GREEN (census 读不到 v2.0 表, 逐格以下表 + 渲染为准).

### 逐格表 (改后每行一行; 核心格 = # / Variable / Label / Type / [Format] / Role 对 bbox + 渲染)
Key Notes 分类: 逐字 = KB 格为 PDF 该行某列原文子串; 部分逐字+简写; KB 简写 (不矛盾); KB 自写, 无 PDF 依据 (不矛盾); D2 改; PDF Usage Restrictions 原文 (新增行); 空.

| 表 | KB 行 (改后) | # | Variable | PDF 页 | 核心格 | Key Notes / Notes | 本批处理 |
|---|---|---|---|---|---|---|---|
| §3.1.1 Interventions | 43 | 1 | --TRT | p12 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 44 | 2 | --MODIFY | p12 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 45 | 3 | --DECOD | p12 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 46 | 4 | --MOOD | p12 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 47 | 5 | --CAT | p12 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 48 | 6 | --SCAT | p12 | 一致 | 部分逐字+简写 | — |
| §3.1.1 Interventions | 49 | 7 | --PRESP | p12 | 一致 | 部分逐字+简写 | — |
| §3.1.1 Interventions | 50 | 8 | --OCCUR | p12 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 51 | 9 | --REASOC | p12 | 一致 | D2 改 (原格与 PDF 矛盾) | — |
| §3.1.1 Interventions | 52 | 10 | --STAT | p12 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 53 | 11 | --REASND | p12 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 54 | 12 | --CNTMOD | p12 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 55 | 13 | --EPCHGI | p13 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 56 | 14 | --INDC | p13 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 57 | 15 | --CLAS | p13 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 58 | 16 | --CLASCD | p13 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 59 | 17 | --DOSE | p13 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 60 | 18 | --DOSTXT | p13 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 61 | 19 | --DOSU | p13 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 62 | 20 | --TDOSD | p13 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 63 | 21 | --FTDOSD | p13 | 一致 | D2 改 (原格与 PDF 矛盾) | — |
| §3.1.1 Interventions | 64 | 22 | --DOSFRM | p13 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 65 | 23 | --DOSFRQ | p13 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 66 | 24 | --DOSTOT | p13 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 67 | 25 | --DOSRGM | p14 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 68 | 26 | --ROUTE | p14 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 69 | 27 | --LOT | p14 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 70 | 28 | --LOC | p14 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 71 | 29 | --METHOD | p14 | 一致 | D2 改 (原格与 PDF 矛盾) | — |
| §3.1.1 Interventions | 72 | 30 | --LAT | p14 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 73 | 31 | --DIR | p14 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 74 | 32 | --PORTOT | p14 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 75 | 33 | --FAST | p14 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 76 | 34 | --PSTRG | p14 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 77 | 35 | --PSTRGU | p14 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 78 | 36 | --TRTV | p14 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 79 | 37 | --VAMT | p14 | 一致 | D2 改 (原格与 PDF 矛盾) | — |
| §3.1.1 Interventions | 80 | 38 | --VAMTU | p14 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 81 | 39 | --ADJ | p14 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 82 | 40 | --RSDISC | p15 | 一致 | 逐字 | — |
| §3.1.1 Interventions | 83 | 41 | --USCHFL | p15 | 一致 | 部分逐字+简写 | — |
| §3.1.1 Interventions | 84 | 42 | --RSTIND | p15 | 一致 | 部分逐字+简写 | — |
| §3.1.1 Interventions | 85 | 43 | --RSTMOD | p15 | 一致 | 部分逐字+简写 | — |
| §3.1.2 Events | 95 | 1 | --TERM | p15 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 96 | 2 | --MODIFY | p15 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 97 | 3 | --LLT | p15 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 98 | 4 | --LLTCD | p15 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 99 | 5 | --DECOD | p15 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 100 | 6 | --EVDTYP | p15 | 一致 | 部分逐字+简写 | — |
| §3.1.2 Events | 101 | 7 | --PTCD | p15 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 102 | 8 | --HLT | p15 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 103 | 9 | --HLTCD | p16 | 一致 | 逐字 | — |
| §3.1.2 Events | 104 | 10 | --HLGT | p16 | 一致 | 逐字 | — |
| §3.1.2 Events | 105 | 11 | --HLGTCD | p16 | 一致 | 逐字 | — |
| §3.1.2 Events | 106 | 12 | --CAT | p16 | 一致 | 逐字 | — |
| §3.1.2 Events | 107 | 13 | --SCAT | p16 | 一致 | 部分逐字+简写 | — |
| §3.1.2 Events | 108 | 14 | --PRESP | p16 | 一致 | 逐字 | — |
| §3.1.2 Events | 109 | 15 | --OCCUR | p16 | 一致 | 逐字 | — |
| §3.1.2 Events | 110 | 16 | --REASOC | p16 | 一致 | 逐字 | — |
| §3.1.2 Events | 111 | 17 | --STAT | p16 | 一致 | 逐字 | — |
| §3.1.2 Events | 112 | 18 | --REASND | p16 | 一致 | 逐字 | — |
| §3.1.2 Events | 113 | 19 | --BODSYS | p16 | 一致 | 逐字 | — |
| §3.1.2 Events | 114 | 20 | --BDSYCD | p16 | 一致 | 部分逐字+简写 | — |
| §3.1.2 Events | 115 | 21 | --SOC | p16 | 一致 | 部分逐字+简写 | — |
| §3.1.2 Events | 116 | 22 | --SOCCD | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 117 | 23 | --CNTMOD | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 118 | 24 | --EPCHGI | p17 | 一致 | 空 | — |
| §3.1.2 Events | 119 | 25 | --LOC | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 120 | 26 | --LAT | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 121 | 27 | --DIR | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 122 | 28 | --PORTOT | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 123 | 29 | --PARTY | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 124 | 30 | --PRTYID | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 125 | 31 | --SEV | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 126 | 32 | --SER | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 127 | 33 | --ACN | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 128 | 34 | --ACNOTH | p17 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 129 | 35 | --ACNDEV | p17 | 一致 | D2 改 (原格与 PDF 矛盾) | — |
| §3.1.2 Events | 130 | 36 | --REL | p17 | 一致 | 逐字 | — |
| §3.1.2 Events | 131 | 37 | --RLDEV | p18 | 一致 | 逐字 | — |
| §3.1.2 Events | 132 | 38 | --RELNST | p18 | 一致 | 逐字 | — |
| §3.1.2 Events | 133 | 39 | --PATT | p18 | 一致 | 逐字 | — |
| §3.1.2 Events | 134 | 40 | --OUT | p18 | 一致 | 逐字 | — |
| §3.1.2 Events | 135 | 41 | --SCAN | p18 | 一致 | 部分逐字+简写 | — |
| §3.1.2 Events | 136 | 42 | --SCONG | p18 | 一致 | 部分逐字+简写 | — |
| §3.1.2 Events | 137 | 43 | --SDISAB | p18 | 一致 | 逐字 | — |
| §3.1.2 Events | 138 | 44 | --SDTH | p18 | 一致 | 逐字 | — |
| §3.1.2 Events | 139 | 45 | --SHOSP | p18 | 一致 | 逐字 | — |
| §3.1.2 Events | 140 | 46 | --SLIFE | p18 | 一致 | 逐字 | — |
| §3.1.2 Events | 141 | 47 | --SOD | p19 | 一致 | 逐字 | — |
| §3.1.2 Events | 142 | 48 | --SMIE | p19 | 一致 | 逐字 | — |
| §3.1.2 Events | 143 | 49 | --SINTV | p19 | 一致 | 部分逐字+简写 | — |
| §3.1.2 Events | 144 | 50 | --UNANT | p19 | 一致 | 逐字 | — |
| §3.1.2 Events | 145 | 51 | --RLPRT | p19 | 一致 | 部分逐字+简写 | — |
| §3.1.2 Events | 146 | 52 | --RLPRC | p20 | 一致 | 部分逐字+简写 | — |
| §3.1.2 Events | 147 | 53 | --CONTRT | p20 | 一致 | 逐字 | — |
| §3.1.2 Events | 148 | 54 | --TOX | p20 | 一致 | 逐字 | — |
| §3.1.2 Events | 149 | 55 | --TOXGR | p20 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 150 | 56 | --USCHFL | p20 | 一致 | 逐字 | — |
| §3.1.3 Findings | 162 | 1 | --TESTCD | p20 | 一致 | 空 | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 163 | 2 | --TEST | p21 | 一致 | 空 | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 164 | 3 | --SBMRKS | p21 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 165 | 4 | --CELSTA | p21 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 166 | 5 | --CSMRKS | p21 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 167 | 6 | --CNTMOD | p22 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 168 | 7 | --EPCHGI | p22 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 169 | 8 | --TSTCND | p22 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 170 | 9 | --CNDAGT | p22 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 171 | 10 | --BDAGNT | p22 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 172 | 11 | --ABCLID | p22 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 173 | 12 | --MRKSTR | p22 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 174 | 13 | --GATE | p23 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 175 | 14 | --GATDEF | p23 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 176 | 15 | --TSTOPO | p24 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 177 | 16 | --MSCBCE | p24 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 178 | 17 | --AGENT | p24 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 179 | 18 | --CONC | p24 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 180 | 19 | --CONCU | p24 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 181 | 20 | --MODIFY | p24 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 182 | 21 | --TSTDTL | p24 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 183 | 22 | --SPTSTD | p24 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 184 | 23 | --CAT | p24 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 185 | 24 | --SCAT | p24 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 186 | 25 | --TSTPNL | p24 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 187 | 26 | --POS | p25 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 188 | 27 | --BODSYS | p25 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 189 | 28 | --ORRES | p25 | 一致 | KB 简写 (不矛盾) | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 190 | 29 | --ORRESU | p25 | 一致 | 空 | Role 括注→PDF Qualified 全列; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 191 | 30 | --RESSCL | p25 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 192 | 31 | --RESTYP | p25 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 193 | 32 | --COLSRT | p25 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 194 | 33 | --ORNRLO | p25 | 一致 | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 195 | 34 | --ORNRHI | p26 | 一致 | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 196 | 35 | --ORREF | p26 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 197 | 36 | --LLOD | p26 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 198 | 37 | --STRESC | p26 | 一致 | 逐字 | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 199 | 38 | --IMPLBL | p26 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 200 | 39 | --STRESN | p26 | 一致 | KB 简写 (不矛盾) | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 201 | 40 | --STRESU | p26 | 一致 | 空 | Role 括注→PDF Qualified 全列; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 202 | 41 | --STNRLO | p27 | 一致 | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 203 | 42 | --STNRHI | p27 | 一致 | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 204 | 43 | --STNRC | p27 | 一致 | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 205 | 44 | --STREFC | p27 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 206 | 45 | --STREFN | p27 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 207 | 46 | --NRIND | p27 | 一致 | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 208 | 47 | --RESCAT | p27 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 209 | 48 | --INHERT | p27 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 210 | 49 | --GENREF | p27 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 211 | 50 | --CHROM | p27 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 212 | 51 | --SYM | p28 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 213 | 52 | --SYMTYP | p28 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 214 | 53 | --GENLOC | p28 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 215 | 54 | --GENSR | p28 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 216 | 55 | --SEQID | p28 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 217 | 56 | --PVRID | p28 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 218 | 57 | --COPYID | p28 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 219 | 58 | --CHRON | p28 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 220 | 59 | --DISTR | p28 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 221 | 60 | --RESLOC | p28 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 222 | 61 | --STAT | p28 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 223 | 62 | --REASND | p28 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 224 | 63 | --XFN | p28 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 225 | 64 | --NAM | p28 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 226 | 65 | --LOINC | p29 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 227 | 66 | --SPEC | p29 | 一致 | KB 自写, 无 PDF 依据 (不矛盾) | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 228 | 67 | --ANTREG | p29 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 229 | 68 | --SPCCND | p29 | 一致 | KB 自写, 无 PDF 依据 (不矛盾) | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 230 | 69 | --SPCUFL | p29 | 一致 | D2 改 (原格与 PDF 矛盾) | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 231 | 70 | --LOC | p29 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 232 | 71 | --LAT | p29 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 233 | 72 | --DIR | p29 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 234 | 73 | --PORTOT | p29 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 235 | 74 | --METHOD | p29 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 236 | 75 | --RUNID | p29 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 237 | 76 | --ANMETH | p29 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 238 | 77 | --TMTHSN | p30 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 239 | 78 | --LEAD | p30 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 240 | 79 | --CSTATE | p30 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 241 | 80 | --LOBXFL | p30 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 242 | 81 | --BLFL | p30 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 243 | 82 | --FAST | p30 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 244 | 83 | --DRVFL | p30 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 245 | 84 | --EVAL | p30 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 246 | 85 | --EVALID | p30 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 247 | 86 | --ACPTFL | p30 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 248 | 87 | --TOX | p31 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 249 | 88 | --TOXGR | p31 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 250 | 89 | --SEV | p31 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 251 | 90 | --CLSIG | p31 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 252 | 91 | --DTHREL | p31 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 253 | 92 | --LLOQ | p31 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 254 | 93 | --ULOQ | p31 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 255 | 94 | --REASPF | p31 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 256 | 95 | --EXCLFL | p31 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 257 | 96 | --REASEX | p32 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 258 | 97 | --USCHFL | p32 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 259 | 98 | --REPNUM | p32 | 一致 | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 260 | 99 | --RSTIND | p32 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 261 | 100 | --RSTMOD | p32 | 一致 | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3.1 FA | 271 | 1 | --OBJ | p32 | 一致 | 逐字 | 补 # 列 |
| §3.1.4 Identifiers | 283 | 1 | STUDYID | p33 | 一致 | 空 | — |
| §3.1.4 Identifiers | 284 | 2 | DOMAIN | p33 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 285 | 3 | USUBJID | p33 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 286 | 4 | POOLID | p33 | 一致 | 逐字 | — |
| §3.1.4 Identifiers | 287 | 5 | SPDEVID | p33 | 一致 | 空 | — |
| §3.1.4 Identifiers | 288 | 6 | NHOID | p33 | 一致 | 逐字 | — |
| §3.1.4 Identifiers | 289 | 7 | FETUSID | p33 | 一致 | 逐字 | — |
| §3.1.4 Identifiers | 290 | 8 | FOCID | p33 | 一致 | 逐字 | — |
| §3.1.4 Identifiers | 291 | 9 | --SEQ | p33 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 292 | 10 | --GRPID | p34 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 293 | 11 | --REFID | p34 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 294 | 12 | --RECID | p34 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 295 | 13 | --SPID | p34 | 一致 | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 296 | 14 | --LNKID | p34 | 一致 | KB 自写, 无 PDF 依据 (不矛盾) | — |
| §3.1.4 Identifiers | 297 | 15 | --LNKGRP | p34 | 一致 | KB 自写, 无 PDF 依据 (不矛盾) | — |
| §3.1.4 Identifiers | 298 | 16 | --BEATNO | p34 | 一致 | 逐字 | — |
| §3.1.5 Timing | 312 | 1 | VISITNUM | p35 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 313 | 2 | VISIT | p35 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 314 | 3 | VISITDY | p35 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 315 | 4 | TAETORD | p35 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 316 | 5 | EPOCH | p35 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 317 | 6 | RPHASE | p35 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 318 | 7 | RPPLDY | p35 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 319 | 8 | RPPLSTDY | p35 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 320 | 9 | RPPLENDY | p35 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 326 | 10 | --DTC | p35 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing; Format→"ISO 8601 datetime or interval" |
| §3.1.5 Timing | 327 | 11 | --STDTC | p35 | 一致 | 逐字 | 补 Role=Timing; Format→"ISO 8601 datetime or interval" |
| §3.1.5 Timing | 328 | 12 | --ENDTC | p35 | 一致 | 空 | 补 Role=Timing; Format→"ISO 8601 datetime or interval" |
| §3.1.5 Timing | 334 | 13 | --DY | p36 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 335 | 14 | --STDY | p36 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 336 | 15 | --ENDY | p36 | 一致 | 空 | 补 Role=Timing |
| §3.1.5 Timing | 337 | 16 | --NOMDY | p36 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 338 | 17 | --NOMLBL | p36 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 339 | 18 | --RPDY | p36 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 340 | 19 | --RPSTDY | p36 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 341 | 20 | --RPENDY | p36 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 342 | 21 | --XDY | p36 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 343 | 22 | --XSTDY | p36 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 344 | 23 | --XENDY | p36 | 一致 | 空 | 补 Role=Timing |
| §3.1.5 Timing | 345 | 24 | --CHDY | p37 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 346 | 25 | --CHSTDY | p37 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 347 | 26 | --CHENDY | p37 | 一致 | 空 | 补 Role=Timing |
| §3.1.5 Timing | 348 | 27 | --DUR | p37 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 354 | 28 | --TPT | p37 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 355 | 29 | --TPTNUM | p37 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 356 | 30 | --ELTM | p37 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 357 | 31 | --TPTREF | p38 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 358 | 32 | --RFTDTC | p38 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 364 | 33 | --STRF | p38 | 一致 | KB 自写, 无 PDF 依据 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 365 | 34 | --ENRF | p38 | 一致 | KB 自写, 无 PDF 依据 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 366 | 35 | --EVLINT | p38 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 367 | 36 | --EVINTX | p38 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 368 | 37 | --STRTPT | p38 | 一致 | KB 自写, 无 PDF 依据 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 369 | 38 | --STTPT | p38 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 370 | 39 | --ENRTPT | p38 | 一致 | KB 自写, 无 PDF 依据 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 371 | 40 | --ENTPT | p38 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 377 | 41 | MIDS | p38 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 378 | 42 | RELMIDS | p39 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 379 | 43 | MIDSDTC | p39 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 385 | 44 | --STINT | p39 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 386 | 45 | --ENINT | p39 | 一致 | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 387 | 46 | --DETECT | p39 | 一致 | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 388 | 47 | --PTFL | p39 | 一致 | 逐字 | 补 Role=Timing; Notes 补全 Usage 域列表 |
| §3.1.5 Timing | 389 | 48 | --PDUR | p39 | 一致 | 逐字 | 补 Role=Timing; Label→"Planned Duration"; Notes 补全 Usage 域列表 |

### 需主控定 (本 attempt 未改; M-1 决定 attempt 1 是否终版)
- **M-1 Key Notes / Notes 列 (共 264 格, 分类计数: 逐字 75 / 部分逐字+简写 14 / KB 简写 66 / KB 自写无 PDF 依据 8 / D2 已改 6 / 新增行 Usage 原文 36 / 空 59)**. 该列不对应任何单一 PDF 列 (混合 Definition / Notes / Examples / Usage Restrictions). 分三类 (同 B-model06 M-2 形状):
  - M-1a 逐字 / 部分逐字 / 简写且不矛盾 (155 格): 建议默认 **每张表上方加一行 `> KB note (not in SDTM v2.0): The Key Notes column summarizes the PDF Definition / Notes / Examples / Usage Restrictions columns.`** (D6, 不逐格改写); 备选 = 按 PDF Notes 列逐字恢复 (B-model06 M-2b 式, ~180 格, 且 Definition/Examples/Usage 内容会丢).
  - M-1b KB 自写无 PDF 依据 8 格 (FND --SPEC "BLOOD"/"TISSUE", --SPCCND "HEMOLYZED"/"LIPEMIC"; TIM --STRF/--ENRF/--STRTPT/--ENRTPT 值列举 (SDTMIG 口径, v2.0 无); ID --LNKID "dataset-to-dataset" / --LNKGRP "Used with RELREC"): 建议 **改为 PDF Examples/Notes 原文** (或随 M-1a 统一 D6).
  - M-1c 已按 D2 改的 6 格 (C-1..C-6) 若主控不同意 "矛盾即改", 可回退到 D6.
- **M-2** Findings 新增 84 行 Key Notes 填 PDF Usage Restrictions 原文 (36 格有值, 48 空). 依据: 本文件其余各表 Key Notes 一律带 Usage Restrictions (INT/EVT/ID/TIM 全部有 Usage 的行均已含, --PTFL/--PDUR 截断已补全). 如主控要求新增行 Key Notes 全空, 回退即可.
- **M-3** (规则 6, 记录) KB 自拟标题保留未改: H1 "Sections 3-3.1: …"; `### Topic and Qualifier Variables (43/56/100 variables)` ×3; Timing `### Visit and Epoch Variables` 等 7 个. PDF 无对应 (PDF 用表题行, 已补).
- **M-4** (R1, 记录) Timing 表 PDF Format 列有值的行在无 Format 列的子表 (--DUR / --ELTM / --RFTDTC / --EVLINT / MIDSDTC / --STINT / --ENINT / --PDUR) 未补 Format 列 (R1 缺列不补); 其中 --DUR/--ELTM/--EVLINT/--STINT/--ENINT 的 Notes 格写的正是 Format 值, --RFTDTC Notes "ISO 8601" 为 Format 截断.

### 范围外发现
- 原子错: `sv20_p0037_a001` Label "Relative" (PDF "Rel"); `sv20_p0015_a008-a015` 等 p15 双表头页原子无误 (bbox 本页 Usage/C-code 列粘连是 bbox 分列假阳, 已对渲染). 不影响 KB.
- 无其他 KB 文件需改.

### 验证 (S = scratchpad/t2s_S-MOD2_writer, 均在改后运行)
- `python3 -I $S/scan.py knowledge_base/model/02_observation_classes.md` → `HIT 53 MISS 0` (改前 HIT 43 MISS 10, 10 条 = 6 表题 + FA 标题/首句 + Timing a009/a010)
- `python3 -I $S/bbox_tbl.py $S/bbox_rows.json && python3 -I $S/cmp.py $S && python3 -I $S/verify.py $S` → `INT rows 43 ordered True` / `EVT rows 56` / `FND rows 100` / `ID rows 16` / `TIM rows 48` / `FA rows 1` 全 ordered True; `cells checked 1059 diffs 0`
- `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` → `KB tables: 12; status: {'UNPARSEABLE': 12}; diffs: 0` GREEN
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → RED (回退全 ig34, 并行批); `grep -c '"sv20' $S/fp_regress.jsonl` = **0**
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`
- 渲染: `pdftoppm -f 11 -l 39 -r 80 -png source/cdisc/SDTM_v2.0.pdf $S/p`, 29 页逐页目视.

### git diff --stat
```
 knowledge_base/model/02_observation_classes.md | 309 +++++++++++++++----------
 1 file changed, 191 insertions(+), 118 deletions(-)
```

### attempt 1 补充 (同 attempt, KB 未再改; 以本节为准修正上文)
1. **自证说明**: `verify.py` 的 1059 格 0 DIFF 对 FND 100 行与 TIM Label/Format/Role 是**同源自比** (gen.py 与 verify.py 都读 `pdf_tabs.json`), 只证明生成无误, 不证明 bbox 解析正确. 独立核 = `python3 -I $S/indep.py` (改后 KB 核心格 vs `pdf_atoms.jsonl` TABLE_ROW 原子, 不经 bbox) → `rows 264 cells 1059 diffs 1`, 唯一 DIFF = KB:345 --CHDY Label vs 原子 sv20_p0037_a001 ("Relative"), 渲染 p37 = "Rel" = KB → 原子错. 两种独立来源 (bbox 词框 / 原子抽取) + 29 页渲染目视三方一致.
2. **逐格表 "核心格" 列**: 上文逐格表该列为常量, 作废; 以下方 "逐格表 v2" 为准, 由 `python3 -I $S/celltab.py $S` 逐行计算 (KB 格分别对 bbox 与原子比较, 输出 "一致 (原子同)" 或差异).
3. **TABLE_HEADER 原子 6 条** (p12 a005 / p15 a007 / p20 a008 / p32 a010 / p33 a002 / p35 a002): PDF 12 列表头 `# | Variable Name | Variable Label | Type | Format | Role | Variable(s) Qualified | Usage Restrictions | Variable C-code | Definition | Notes | Examples`; KB 表头 `# | Variable | Label | Type | [Format] | Role | Key Notes/Notes` = R1 5 列精简版 + KB 自写列. 列名简写 (Variable/Label vs Variable Name/Variable Label) 为 model/ 全目录约定, 未改 (并行批 S-MOD1/S-MOD3 同约定) → 并入 M-3 记录.
4. **D-1..D-3 (`**Structure:**` 行) 与 B-model06 先例的差异**: B-model06 #15/#17/#19 对 `**Structure:**` 行是 D6 保留, 因该文件 PDF 表题不含 "One Record per…"; 本文件 PDF 表题 (a004/a006/a007) 本身就含 "One Record per …", Structure 行是表题的残留改写 → 按 R2 残留改写口径 D2 删. 请主控据此对齐 S-MOD1 / S-MOD3 (若其 PDF 表题含 record 结构, 同删; 否则 D6).
5. **EVT 1-8 (p15) Key Notes 分类手工更正**: p15 双表头, bbox 后段列错位, 上文逐格表对这 8 行的分类来自错位文本. 按渲染 p15 更正: --TERM → 逐字 (PDF Definition); --LLT / --LLTCD / --PTCD / --HLT → 部分逐字+简写 (Usage 逐字 + Definition 简写); --MODIFY / --DECOD → KB 简写; --EVDTYP → 部分逐字+简写. **M-1 计数更正为: 逐字 76 / 部分逐字+简写 18 / KB 简写 61 / KB 自写无 PDF 依据 8 / D2 已改 6 / 新增行 Usage 原文 36 / 空 59 (= 264)**; M-1a = 155 格不变.
6. **KB→PDF 反向扫描命令**: `python3 -I $S/rscan.py` (改后 KB 非表格行逐句, 在 sv20 p11-39 layout 文本归一后查) → `HIT 56 NOPDF 19`; 19 条 = H1 2 段 + Source 行 2 段 + `###` KB 分组标题 10 个 + 2 处 D6 KB note (4 段) + :31 一句 (跨 p11/p12 页脚, layout 被页脚隔断; 正向 scan.py 已命中 a032+p12 a001). 无其他无出处行.

### 逐格表 v2 (以此为准; `python3 -I $S/celltab.py $S` 输出)
| 表 | KB 行 (改后) | # | Variable | PDF 页 | 核心格 (bbox / 原子) | Key Notes / Notes | 本批处理 |
|---|---|---|---|---|---|---|---|
| §3.1.1 Interventions | 43 | 1 | --TRT | p12 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 44 | 2 | --MODIFY | p12 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 45 | 3 | --DECOD | p12 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 46 | 4 | --MOOD | p12 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 47 | 5 | --CAT | p12 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 48 | 6 | --SCAT | p12 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.1 Interventions | 49 | 7 | --PRESP | p12 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.1 Interventions | 50 | 8 | --OCCUR | p12 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 51 | 9 | --REASOC | p12 | 一致 (原子同) | D2 改 (原格与 PDF 矛盾) | — |
| §3.1.1 Interventions | 52 | 10 | --STAT | p12 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 53 | 11 | --REASND | p12 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 54 | 12 | --CNTMOD | p12 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 55 | 13 | --EPCHGI | p13 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 56 | 14 | --INDC | p13 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 57 | 15 | --CLAS | p13 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 58 | 16 | --CLASCD | p13 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 59 | 17 | --DOSE | p13 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 60 | 18 | --DOSTXT | p13 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 61 | 19 | --DOSU | p13 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 62 | 20 | --TDOSD | p13 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 63 | 21 | --FTDOSD | p13 | 一致 (原子同) | D2 改 (原格与 PDF 矛盾) | — |
| §3.1.1 Interventions | 64 | 22 | --DOSFRM | p13 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 65 | 23 | --DOSFRQ | p13 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 66 | 24 | --DOSTOT | p13 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 67 | 25 | --DOSRGM | p14 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 68 | 26 | --ROUTE | p14 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 69 | 27 | --LOT | p14 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 70 | 28 | --LOC | p14 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 71 | 29 | --METHOD | p14 | 一致 (原子同) | D2 改 (原格与 PDF 矛盾) | — |
| §3.1.1 Interventions | 72 | 30 | --LAT | p14 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 73 | 31 | --DIR | p14 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 74 | 32 | --PORTOT | p14 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 75 | 33 | --FAST | p14 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 76 | 34 | --PSTRG | p14 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 77 | 35 | --PSTRGU | p14 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 78 | 36 | --TRTV | p14 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 79 | 37 | --VAMT | p14 | 一致 (原子同) | D2 改 (原格与 PDF 矛盾) | — |
| §3.1.1 Interventions | 80 | 38 | --VAMTU | p14 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 81 | 39 | --ADJ | p14 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.1 Interventions | 82 | 40 | --RSDISC | p15 | 一致 (原子同) | 逐字 | — |
| §3.1.1 Interventions | 83 | 41 | --USCHFL | p15 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.1 Interventions | 84 | 42 | --RSTIND | p15 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.1 Interventions | 85 | 43 | --RSTMOD | p15 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 95 | 1 | --TERM | p15 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 96 | 2 | --MODIFY | p15 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 97 | 3 | --LLT | p15 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 98 | 4 | --LLTCD | p15 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 99 | 5 | --DECOD | p15 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 100 | 6 | --EVDTYP | p15 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 101 | 7 | --PTCD | p15 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 102 | 8 | --HLT | p15 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 103 | 9 | --HLTCD | p16 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 104 | 10 | --HLGT | p16 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 105 | 11 | --HLGTCD | p16 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 106 | 12 | --CAT | p16 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 107 | 13 | --SCAT | p16 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 108 | 14 | --PRESP | p16 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 109 | 15 | --OCCUR | p16 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 110 | 16 | --REASOC | p16 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 111 | 17 | --STAT | p16 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 112 | 18 | --REASND | p16 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 113 | 19 | --BODSYS | p16 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 114 | 20 | --BDSYCD | p16 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 115 | 21 | --SOC | p16 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 116 | 22 | --SOCCD | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 117 | 23 | --CNTMOD | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 118 | 24 | --EPCHGI | p17 | 一致 (原子同) | 空 | — |
| §3.1.2 Events | 119 | 25 | --LOC | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 120 | 26 | --LAT | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 121 | 27 | --DIR | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 122 | 28 | --PORTOT | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 123 | 29 | --PARTY | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 124 | 30 | --PRTYID | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 125 | 31 | --SEV | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 126 | 32 | --SER | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 127 | 33 | --ACN | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 128 | 34 | --ACNOTH | p17 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 129 | 35 | --ACNDEV | p17 | 一致 (原子同) | D2 改 (原格与 PDF 矛盾) | — |
| §3.1.2 Events | 130 | 36 | --REL | p17 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 131 | 37 | --RLDEV | p18 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 132 | 38 | --RELNST | p18 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 133 | 39 | --PATT | p18 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 134 | 40 | --OUT | p18 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 135 | 41 | --SCAN | p18 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 136 | 42 | --SCONG | p18 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 137 | 43 | --SDISAB | p18 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 138 | 44 | --SDTH | p18 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 139 | 45 | --SHOSP | p18 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 140 | 46 | --SLIFE | p18 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 141 | 47 | --SOD | p19 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 142 | 48 | --SMIE | p19 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 143 | 49 | --SINTV | p19 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 144 | 50 | --UNANT | p19 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 145 | 51 | --RLPRT | p19 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 146 | 52 | --RLPRC | p20 | 一致 (原子同) | 部分逐字+简写 | — |
| §3.1.2 Events | 147 | 53 | --CONTRT | p20 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 148 | 54 | --TOX | p20 | 一致 (原子同) | 逐字 | — |
| §3.1.2 Events | 149 | 55 | --TOXGR | p20 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.2 Events | 150 | 56 | --USCHFL | p20 | 一致 (原子同) | 逐字 | — |
| §3.1.3 Findings | 162 | 1 | --TESTCD | p20 | 一致 (原子同) | 空 | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 163 | 2 | --TEST | p21 | 一致 (原子同) | 空 | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 164 | 3 | --SBMRKS | p21 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 165 | 4 | --CELSTA | p21 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 166 | 5 | --CSMRKS | p21 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 167 | 6 | --CNTMOD | p22 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 168 | 7 | --EPCHGI | p22 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 169 | 8 | --TSTCND | p22 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 170 | 9 | --CNDAGT | p22 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 171 | 10 | --BDAGNT | p22 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 172 | 11 | --ABCLID | p22 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 173 | 12 | --MRKSTR | p22 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 174 | 13 | --GATE | p23 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 175 | 14 | --GATDEF | p23 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 176 | 15 | --TSTOPO | p24 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 177 | 16 | --MSCBCE | p24 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 178 | 17 | --AGENT | p24 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 179 | 18 | --CONC | p24 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 180 | 19 | --CONCU | p24 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 181 | 20 | --MODIFY | p24 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 182 | 21 | --TSTDTL | p24 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 183 | 22 | --SPTSTD | p24 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 184 | 23 | --CAT | p24 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 185 | 24 | --SCAT | p24 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 186 | 25 | --TSTPNL | p24 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 187 | 26 | --POS | p25 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 188 | 27 | --BODSYS | p25 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 189 | 28 | --ORRES | p25 | 一致 (原子同) | KB 简写 (不矛盾) | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 190 | 29 | --ORRESU | p25 | 一致 (原子同) | 空 | Role 括注→PDF Qualified 全列; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 191 | 30 | --RESSCL | p25 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 192 | 31 | --RESTYP | p25 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 193 | 32 | --COLSRT | p25 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 194 | 33 | --ORNRLO | p25 | 一致 (原子同) | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 195 | 34 | --ORNRHI | p26 | 一致 (原子同) | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 196 | 35 | --ORREF | p26 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 197 | 36 | --LLOD | p26 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 198 | 37 | --STRESC | p26 | 一致 (原子同) | 逐字 | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 199 | 38 | --IMPLBL | p26 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 200 | 39 | --STRESN | p26 | 一致 (原子同) | KB 简写 (不矛盾) | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 201 | 40 | --STRESU | p26 | 一致 (原子同) | 空 | Role 括注→PDF Qualified 全列; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 202 | 41 | --STNRLO | p27 | 一致 (原子同) | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 203 | 42 | --STNRHI | p27 | 一致 (原子同) | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 204 | 43 | --STNRC | p27 | 一致 (原子同) | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 205 | 44 | --STREFC | p27 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 206 | 45 | --STREFN | p27 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 207 | 46 | --NRIND | p27 | 一致 (原子同) | KB 简写 (不矛盾) | Label→PDF; 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 208 | 47 | --RESCAT | p27 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 209 | 48 | --INHERT | p27 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 210 | 49 | --GENREF | p27 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 211 | 50 | --CHROM | p27 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 212 | 51 | --SYM | p28 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 213 | 52 | --SYMTYP | p28 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 214 | 53 | --GENLOC | p28 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 215 | 54 | --GENSR | p28 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 216 | 55 | --SEQID | p28 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 217 | 56 | --PVRID | p28 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 218 | 57 | --COPYID | p28 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 219 | 58 | --CHRON | p28 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 220 | 59 | --DISTR | p28 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 221 | 60 | --RESLOC | p28 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 222 | 61 | --STAT | p28 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 223 | 62 | --REASND | p28 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 224 | 63 | --XFN | p28 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 225 | 64 | --NAM | p28 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 226 | 65 | --LOINC | p29 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 227 | 66 | --SPEC | p29 | 一致 (原子同) | KB 自写, 无 PDF 依据 (不矛盾) | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 228 | 67 | --ANTREG | p29 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 229 | 68 | --SPCCND | p29 | 一致 (原子同) | KB 自写, 无 PDF 依据 (不矛盾) | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 230 | 69 | --SPCUFL | p29 | 一致 (原子同) | D2 改 (原格与 PDF 矛盾) | 并入单表, 补 #/Type/Role |
| §3.1.3 Findings | 231 | 70 | --LOC | p29 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 232 | 71 | --LAT | p29 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 233 | 72 | --DIR | p29 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 234 | 73 | --PORTOT | p29 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 235 | 74 | --METHOD | p29 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 236 | 75 | --RUNID | p29 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 237 | 76 | --ANMETH | p29 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 238 | 77 | --TMTHSN | p30 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 239 | 78 | --LEAD | p30 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 240 | 79 | --CSTATE | p30 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 241 | 80 | --LOBXFL | p30 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 242 | 81 | --BLFL | p30 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 243 | 82 | --FAST | p30 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 244 | 83 | --DRVFL | p30 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 245 | 84 | --EVAL | p30 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 246 | 85 | --EVALID | p30 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 247 | 86 | --ACPTFL | p30 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 248 | 87 | --TOX | p31 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 249 | 88 | --TOXGR | p31 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 250 | 89 | --SEV | p31 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 251 | 90 | --CLSIG | p31 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 252 | 91 | --DTHREL | p31 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 253 | 92 | --LLOQ | p31 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 254 | 93 | --ULOQ | p31 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 255 | 94 | --REASPF | p31 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 256 | 95 | --EXCLFL | p31 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 257 | 96 | --REASEX | p32 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 258 | 97 | --USCHFL | p32 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 259 | 98 | --REPNUM | p32 | 一致 (原子同) | 空 | 新增行 (FND 重建) |
| §3.1.3 Findings | 260 | 99 | --RSTIND | p32 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3 Findings | 261 | 100 | --RSTMOD | p32 | 一致 (原子同) | PDF Usage Restrictions 原文 | 新增行 (FND 重建) |
| §3.1.3.1 FA | 271 | 1 | --OBJ | p32 | 一致 (原子同) | 逐字 | 补 # 列 |
| §3.1.4 Identifiers | 283 | 1 | STUDYID | p33 | 一致 (原子同) | 空 | — |
| §3.1.4 Identifiers | 284 | 2 | DOMAIN | p33 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 285 | 3 | USUBJID | p33 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 286 | 4 | POOLID | p33 | 一致 (原子同) | 逐字 | — |
| §3.1.4 Identifiers | 287 | 5 | SPDEVID | p33 | 一致 (原子同) | 空 | — |
| §3.1.4 Identifiers | 288 | 6 | NHOID | p33 | 一致 (原子同) | 逐字 | — |
| §3.1.4 Identifiers | 289 | 7 | FETUSID | p33 | 一致 (原子同) | 逐字 | — |
| §3.1.4 Identifiers | 290 | 8 | FOCID | p33 | 一致 (原子同) | 逐字 | — |
| §3.1.4 Identifiers | 291 | 9 | --SEQ | p33 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 292 | 10 | --GRPID | p34 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 293 | 11 | --REFID | p34 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 294 | 12 | --RECID | p34 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 295 | 13 | --SPID | p34 | 一致 (原子同) | KB 简写 (不矛盾) | — |
| §3.1.4 Identifiers | 296 | 14 | --LNKID | p34 | 一致 (原子同) | KB 自写, 无 PDF 依据 (不矛盾) | — |
| §3.1.4 Identifiers | 297 | 15 | --LNKGRP | p34 | 一致 (原子同) | KB 自写, 无 PDF 依据 (不矛盾) | — |
| §3.1.4 Identifiers | 298 | 16 | --BEATNO | p34 | 一致 (原子同) | 逐字 | — |
| §3.1.5 Timing | 312 | 1 | VISITNUM | p35 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 313 | 2 | VISIT | p35 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 314 | 3 | VISITDY | p35 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 315 | 4 | TAETORD | p35 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 316 | 5 | EPOCH | p35 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 317 | 6 | RPHASE | p35 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 318 | 7 | RPPLDY | p35 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 319 | 8 | RPPLSTDY | p35 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 320 | 9 | RPPLENDY | p35 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 326 | 10 | --DTC | p35 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing; Format→"ISO 8601 datetime or interval" |
| §3.1.5 Timing | 327 | 11 | --STDTC | p35 | 一致 (原子同) | 逐字 | 补 Role=Timing; Format→"ISO 8601 datetime or interval" |
| §3.1.5 Timing | 328 | 12 | --ENDTC | p35 | 一致 (原子同) | 空 | 补 Role=Timing; Format→"ISO 8601 datetime or interval" |
| §3.1.5 Timing | 334 | 13 | --DY | p36 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 335 | 14 | --STDY | p36 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 336 | 15 | --ENDY | p36 | 一致 (原子同) | 空 | 补 Role=Timing |
| §3.1.5 Timing | 337 | 16 | --NOMDY | p36 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 338 | 17 | --NOMLBL | p36 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 339 | 18 | --RPDY | p36 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 340 | 19 | --RPSTDY | p36 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 341 | 20 | --RPENDY | p36 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 342 | 21 | --XDY | p36 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 343 | 22 | --XSTDY | p36 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 344 | 23 | --XENDY | p36 | 一致 (原子同) | 空 | 补 Role=Timing |
| §3.1.5 Timing | 345 | 24 | --CHDY | p37 | 一致 (原子 DIFF Label: 原子错, 渲染=KB) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 346 | 25 | --CHSTDY | p37 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 347 | 26 | --CHENDY | p37 | 一致 (原子同) | 空 | 补 Role=Timing |
| §3.1.5 Timing | 348 | 27 | --DUR | p37 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 354 | 28 | --TPT | p37 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 355 | 29 | --TPTNUM | p37 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 356 | 30 | --ELTM | p37 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 357 | 31 | --TPTREF | p38 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 358 | 32 | --RFTDTC | p38 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 364 | 33 | --STRF | p38 | 一致 (原子同) | KB 自写, 无 PDF 依据 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 365 | 34 | --ENRF | p38 | 一致 (原子同) | KB 自写, 无 PDF 依据 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 366 | 35 | --EVLINT | p38 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 367 | 36 | --EVINTX | p38 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 368 | 37 | --STRTPT | p38 | 一致 (原子同) | KB 自写, 无 PDF 依据 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 369 | 38 | --STTPT | p38 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 370 | 39 | --ENRTPT | p38 | 一致 (原子同) | KB 自写, 无 PDF 依据 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 371 | 40 | --ENTPT | p38 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 377 | 41 | MIDS | p38 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 378 | 42 | RELMIDS | p39 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 379 | 43 | MIDSDTC | p39 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 385 | 44 | --STINT | p39 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 386 | 45 | --ENINT | p39 | 一致 (原子同) | KB 简写 (不矛盾) | 补 Role=Timing |
| §3.1.5 Timing | 387 | 46 | --DETECT | p39 | 一致 (原子同) | 逐字 | 补 Role=Timing |
| §3.1.5 Timing | 388 | 47 | --PTFL | p39 | 一致 (原子同) | 逐字 | 补 Role=Timing; Notes 补全 Usage 域列表 |
| §3.1.5 Timing | 389 | 48 | --PDUR | p39 | 一致 (原子同) | 逐字 | 补 Role=Timing; Label→"Planned Duration"; Notes 补全 Usage 域列表 |

## attempt 1 delta (主控裁定 M-1 / M-2 / M-3 / M-4 / D-1..D-3, 2026-11-26)
- md5 `ec1887ae…` → `b19bf1ffb56455a4e39b7feb01ead309` (389 → 399 行). 只加 D6 标注行, 表格单元格未动.

### M-1 执行: D6 列说明 (照实写列来源, 不说 "verbatim")
| # | KB 行 (改后) | 表 | 标注 |
|---|---|---|---|
| A-1 | :41 | §3.1.1 Interventions (Key Notes) | Key Notes 列 condenses PDF Definition / Notes / Examples / Usage Restrictions, not verbatim |
| A-2 | :95 | §3.1.2 Events (Key Notes) | 同上 |
| A-3 | :164 | §3.1.3 Findings (Key Notes) | 同上 + 补一句: 没有原 KB 注的行逐字承载 PDF Usage Restrictions (PDF 无则空) (= M-2 保留) |
| A-4 | :287 | §3.1.4 Identifiers (Notes 列, 与 Key Notes 同性质) | 同上措辞, 列名 Notes |
| A-5 | :316 | §3.1.5 Timing 7 子表 (Notes 列) | 与 :314 子表拆分说明同一引用块; 列来源另含 PDF Format (--DUR / --ELTM / --EVLINT / --STINT / --ENINT / --RFTDTC 的 Notes 值即 Format) |
- 未标: §3.1.3.1 FA 表 Notes 格 = PDF Notes 逐字 (不是缩写).
- 说明: 裁定原文写 "含 Key Notes 列的表"; ID 与 Timing 的 Notes 列同样是 KB 缩写, 且 8 个无依据格中有 6 个在这两张表 (要 "保留在 D6 下" 就须有 D6), 所以一并标注. 若主控只要 3 张, 删 A-4/A-5 即可.

### M-1 八个 "无 PDF 依据" 格逐格判 (对渲染页)
| KB 行 | 变量 | KB 格 | PDF 该行 (摘要) | 判定 | 处理 |
|---|---|---|---|---|---|
| :233 | FND --SPEC | "BLOOD", "URINE", "TISSUE" | p29 Def: 生物体取样材料类型; Ex: "SERUM", "PLASMA", "URINE", "DNA", "RNA" | 不矛盾 (BLOOD/TISSUE 也是样本材料, 仅非 PDF 例) | 保留, D6 (A-3) |
| :235 | FND --SPCCND | "HEMOLYZED", "LIPEMIC" | p29 Def: 样本物理状态/质量; Ex: "CLOUDY" | 不矛盾 (同类状态值) | 保留, D6 (A-3) |
| :304 | ID --LNKID | Used with RELREC dataset-to-dataset linking | p34 Def: 把一个域的记录链到另一域 1+ 条记录; Notes: 一对一或一对多 | 不矛盾 (跨域链接; 未与 PDF 冲突) | 保留, D6 (A-4) |
| :305 | ID --LNKGRP | Used with RELREC to link groups of records | p34 Def: 把一组记录链到另一域记录; Notes: 通常多对一 | 不矛盾 | 保留, D6 (A-4) |
| :372 | TIM --STRF | BEFORE, DURING, DURING/AFTER, AFTER, UNKNOWN | p38 Def: 相对研究参考期的开始特征; 无值列举 | 不矛盾 (v2.0 不列值) | 保留, D6 (A-5) |
| :373 | TIM --ENRF | Same values as --STRF | p38 同型 (结束) | 不矛盾 | 保留, D6 (A-5) |
| :376 | TIM --STRTPT | BEFORE, COINCIDENT, AFTER, UNKNOWN | p38 Def: 相对参考时间点的开始特征; Notes: 参考点在 --STTPT | 不矛盾 | 保留, D6 (A-5) |
| :378 | TIM --ENRTPT | BEFORE, COINCIDENT, AFTER, ONGOING, UNKNOWN | p38 同型 (结束), 参考点在 --ENTPT | 不矛盾 | 保留, D6 (A-5) |
- 结论: 8 格都不矛盾 → 0 格 D2 改, 8 格保留在 D6 下.

### M-2 / M-3 / M-4 / D-1..D-3
- M-2 保留 (未改); M-3 / M-4 已记录, 不改; D-1..D-3 已获同意.

### 复跑 (S = scratchpad/t2s_S-MOD2_writer)
- `python3 -I $S/scan.py knowledge_base/model/02_observation_classes.md` → `HIT 53 MISS 0`
- `python3 -I $S/indep.py` → `rows 264 cells 1059 diffs 1` (仍只有原子错 --CHDY)
- `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_delta.json` → `KB tables: 12; status: {'UNPARSEABLE': 12}; diffs: 0` GREEN
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`
- `git diff --stat -- knowledge_base/model/02_observation_classes.md` → `1 file changed, 200 insertions(+), 117 deletions(-)`
- 行号更正 (上表 TIM 四行): --STRF :374, --ENRF :375, --STRTPT :378, --ENRTPT :380 (上表写的 :372/:373/:376/:378 有误; jsonl 同四条以此为准). `grep -n "| --STRF \|| --ENRF \|| --STRTPT \|| --ENRTPT " knowledge_base/model/02_observation_classes.md` 核.

## attempt 2 (reviewer CONDITIONAL F-1; 2026-11-26)
- md5 `b19bf1ff…` → `795c8d061c9418a5add217bfae797cf6` (仍 399 行). 只替换 5 行 D6 列说明, 表格单元格未动.
- :41 / :95 / :164 / :287 / :316 逐字替换为 `t2_S-MOD2_review.md` F-1 段给出的文字 (:287 列名用 Notes; :164 加 "domain restriction / blank cell" 句; :316 用 Timing 版). 措辞已核, 照用, 未改写: 该列为 KB 编写, 多数格引用或缩写 PDF 列, 部分格 (8 个无依据格及同类格) 是 KB 自加. :164 后句与 reviewer 的 `usage.py` 结果相符 (84/84 新增行 = PDF Usage 原文; 52 个空格其 PDF Usage 也空).
- 替换前每行都断言过: 以 `> KB note (not in SDTM v2.0):` 开头且含 "condenses".
- 复跑: `git diff --stat -- knowledge_base/model/02_observation_classes.md` → `1 file changed, 200 insertions(+), 117 deletions(-)`; `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`.
