# T2S S-MOD3 writer checkpoint (扫描批: model/05_study_level_data.md, 源 SDTM v2.0)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `b80d263`; 改前文件 md5 `b01d929e0c3718c8d176d90f7c4c598d` (= HEAD = B-model05 a2 终态, 333 行).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-MOD3_writer/` (S)
  (base.md = HEAD 副本; bbox_tbl.py = `pdf_bbox/sv20_p00NN.tsv` 词框按表头 x 分列, 每页多表头分段; cmp.py = KB 表 5 列 vs bbox; indep.py = KB 表 5 列 vs `pdf_atoms.jsonl` TABLE_ROW (不经 bbox); p-51..p-63.png = 110 dpi 渲染)
- 真值顺序: 渲染图 > bbox 分列 > layout 文本 > 原子.

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| model/05_study_level_data.md | §5 (5.1-5.2.2) | 51-63 | **51-63** | p51 首行 `5 Study-level Data` (sv20_p0051_a001); p50 末为 §4 AP 关系段 (`sv20_p0050.txt`); p63 仅 OI Concept Map 图; p64 首行 `6 Datasets for Representing Relationships` → 不归本批 |
- 改后 md5 `804e1689331606688a748ca68c5e5c8f` (333 行; 删 2 行 D6 Structure 各带空行 = -4, 加 2 行 D6 Notes 列说明各带空行 = +4).

### 口径
- R1: 5 列 floor (#/Variable/Label/Type/Role) 内必须与 PDF 一致; Format/Qualified/Usage/C-code/Definition/Notes/Examples 缺列不补.
- Role 括注沿用 model/ 约定 `Role (Variable(s) Qualified)`, 括注内容须与 PDF Qualified 全列一致 (S-MOD2 口径) → 本文件 9 格缺括注补 (O35-4).
- 标题: S-TDM 主控口径 (补 PDF 原标题 + 全仓无入站锚点的 KB 自拟同义标题删除) + S-MOD2 S-2 先例 (model/02 `### Findings About (Subtype)` → `### 3.1.3.1 …`). 只换文字, **层级不动** (S-FND: 既有层级不一致不改). H1 与 `Source:` 行保留 (S-MOD2 M-3).
  入站锚点核: `grep -rnE "05_study_level_data(\.md)?#" knowledge_base docs web/src tools .work/AGENT_GUIDE.md README.md METHODOLOGY.md` → 无输出 (rc=1, 未截断); 该文件仅被 INDEX/ROUTING/8 个 domains spec.md 以整文件链接引用.
- `**Structure:**` 残留: S-MOD2 model/ 通用条 — PDF 表题含 "One Record per…" → D2 删 (TX/TS); PDF 表题无 (DI "Device Identifiers Dataset" / OI "Non-host Organism Identifiers Dataset") → D6 保留.
- TT/TP 表 "Notes" 列 (KB 列名与 PDF Notes 列同名, 但 3-7/3-10 行装的是 PDF Usage Restrictions, DOMAIN 行装 PDF Notes 的域代码) = 不对应单一 PDF 列的 KB 汇总列 → S-MOD2 model/ 通用条: 表上方加一行 D6, 格不改 (逐格: 无矛盾格).
- D6 措辞 `> KB note (not in SDTM v2.0):`.

### 双向全扫 — 逐页日志
方法: PDF→KB 非表原子 (HEADING/SENTENCE/LIST_ITEM/NOTE, 89 条) = `scan.py` 归一子串 → 改后 **HIT 89 MISS 0** (改前 HIT 74 MISS 15, 15 = 编号标题); `order.py` 全部非表 + 表行原子按 PDF 顺序在 KB 中单调出现 → `order bad 0`. 表行 (110 行 × 5 列 = 550 格) = `cmp.py` (bbox 分列) 与 `indep.py` (原子, 不经 bbox) 两独立来源 → 改后均 `cells 550 diffs 0` (改前均 9 DIFF = 9 个 Role 括注); 每页 110 dpi 渲染逐行目视 (13 页). KB→PDF = `rscan.py` 改后 KB 非表格行逐句在 sv20 p51-63 layout 文本查 → `HIT 97`, NOPDF 仅 H1 / Source 行 / 6 处 D6 KB note (TT/TP 列说明 2、DI/OI Structure 2、Mermaid 注 2) / 2 段 mermaid 代码. TABLE_HEADER 原子 13 条: PDF 12 列, KB = R1 5 列 (+TT/TP Notes) → R1 IE, 列名简写 (Variable/Label) 为 model/ 全目录约定未改. FIGURE 原子 2 条: 题注逐字在 :277 / :315, Mermaid 对渲染图核 (见下).

| 页 | 节 | PDF→KB: 句/列表/标题/NOTE 原子 数 / 命中 / 缺→已补; 表行 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 51 | §5 / §5.1 / §5.1.1 / §5.1.1.1 | 19 / 19 / 3→3 (a001 `5 Study-level Data`, a003 `5.1 The Trial Design Model`, a016 `5.1.1.1 Trial Elements` 标题); 表行 3 (TE 1-3) | :5-33; `## Overview` / `## 5.1 Trial Design Model` / `### Trial Elements (TE)` 被 PDF 标题取代 (D-1..D-3) | TE 1-3 一致 | 列表 7 项逐字; a019 表题 :33 |
| 52 | §5.1.1.1 尾 / §5.1.1.2 | 6 / 6 / 1→1 (a005 `5.1.1.2 Trial Arms`); 表行 10 (TE 4-7, TA 1-6) | :45-51; `### Trial Arms (TA)` → D-4 | TE 4-7 / TA 1-6 一致; TE ELEMENT、TA ARM 补括注 | "*arm*" 斜体 = 强调差异 (S-CH1, 不改) |
| 53 | §5.1.1.2 尾 / §5.1.2 | 5 / 5 / 1→1 (a005 `5.1.2 Trial Sets`); 表行 12 (TA 7-10, TX 1-8) | :66-70; `### Trial Sets (TX)` → D-5; TX D6 Structure 行 → D2 删 (D-16) | 一致; TA ELEMENT、TX TXPARM 补括注 | |
| 54 | §5.1.3 / §5.1.3.1 / §5.1.3.2 | 11 / 11 / 2→2 (a006 `5.1.3.1 Trial Repro Stages`, a018 `5.1.3.2 Trial Repro Paths`); 表行 7 (TT 1-7) | :83-113; `### Trial Reproductive Stages (TT)` / `(TP)` → D-6/D-7; :97 D6 Notes 列说明新增 | TT 一致 (Notes 列 = PDF Usage / DOMAIN 域代码, 见逐格表) | 3 处 Note 框 = KB `**Note:**` 逐字 |
| 55 | §5.1.3.2 尾 / §5.1.4 | 6 / 6 / 0; 表行 10 (TP 1-10) | :115-138; :117 D6 Notes 列说明新增 | TP 一致 | a001 表题 :115 |
| 56 | §5.1.4.1 / §5.1.4.2 | 12 / 12 / 2→2 (a001 `5.1.4.1 Trial Visits`, a017 `5.1.4.2 Trial Disease Assessments`); 表行 9 (TV) | :140-162; `### Trial Visits (TV)` / `(TD)` → D-8/D-9 | TV 一致; VISIT、ARM 补括注 | TD 两段 (a018 / a019-a022) 分段同 PDF |
| 57 | §5.1.4.2 尾 / §5.1.4.3 | 3 / 3 / 1→1 (a012 `5.1.4.3 Trial Disease Milestones`); 表行 9 (TD) | :164-180; `### Trial Disease Milestones (TM)` → D-10 | TD 一致 | |
| 58 | §5.1.4.3 尾 / §5.1.5 | 4 / 4 / 1→1 (a008 `5.1.5 Trial Inclusion/Exclusion Criteria`); 表行 11 (TM 1-5, TI 1-6) | :182-196; `### … (TI)` → D-11 | TM / TI 1-6 一致; TI IETEST 补括注 | |
| 59 | §5.1.5 尾 / §5.1.6 | 4 / 4 / 1→1 (a003 `5.1.6 Trial Summary Information`); 表行 12 (TI 7-8, TS 1-10) | :209-213; `### Trial Summary (TS)` → D-12; TS D6 Structure 行 → D2 删 (D-17) | 一致; TS TSPARM 补括注 | TS Usage "Not in nonclinical trials" 3 格 = R1 缺列 (O35-3) |
| 60 | §5.1.6 尾 / §5.1.7 | 4 / 4 / 1→1 (a002 `5.1.7 Challenge Agent Characterization`); 表行 13 (TS 11, AC 1-12) | :229-233; `### … (AC)` → D-13 | 一致; AC ACPARM 补括注 | |
| 61 | §5.2 / §5.2.1 | 9 / 9 / 1→1 (a006 `5.2.1 Device Identifiers Dataset`); 表行 7 (DI) | :252-265; `### Device Identifiers (DI)` → D-14; :261 D6 Structure 保留 | DI 一致 | |
| 62 | §5.2.1 图 / §5.2.2 | 4 / 4 / 1→1 (a002 `5.2.2 Non-host Organism Identifiers Dataset`) + FIGURE a001; 表行 7 (OI) | :277-299; `### Non-host … (OI)` → D-15; :279 Mermaid D6; :299 D6 Structure 保留 | OI 一致; DI Concept Map 6 节点 5 边 = 渲染 | *taxa* 斜体同 PDF |
| 63 | §5.2.2 图 | FIGURE a001 | :315-333 Mermaid D6 | OI Concept Map 6 节点 5 边 = 渲染 | 图题在框内, KB 题注逐字 |

### 变更清单
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | model/05:5 | pdf:p51:sv20_p0051_a001 | REPLACED | `## Overview` → `## 5 Study-level Data` | 51 |
| 2 | model/05:11 | pdf:p51:sv20_p0051_a003 | REPLACED | `## 5.1 Trial Design Model` → `## 5.1 The Trial Design Model` | 51 |
| 3 | model/05:29 | pdf:p51:sv20_p0051_a016 | REPLACED | `### Trial Elements (TE)` → `### 5.1.1.1 Trial Elements` | 51 |
| 4 | model/05:45 | pdf:p52:sv20_p0052_a005 | REPLACED | `### Trial Arms (TA)` → `### 5.1.1.2 Trial Arms` | 52 |
| 5 | model/05:66 | pdf:p53:sv20_p0053_a005 | REPLACED | `### Trial Sets (TX)` → `### 5.1.2 Trial Sets` | 53 |
| 6 | model/05:89 | pdf:p54:sv20_p0054_a006 | REPLACED | `### Trial Reproductive Stages (TT)` → `### 5.1.3.1 Trial Repro Stages` | 54 |
| 7 | model/05:109 | pdf:p54:sv20_p0054_a018 | REPLACED | `### Trial Reproductive Paths (TP)` → `### 5.1.3.2 Trial Repro Paths` | 54 |
| 8 | model/05:140 | pdf:p56:sv20_p0056_a001 | REPLACED | `### Trial Visits (TV)` → `### 5.1.4.1 Trial Visits` | 56 |
| 9 | model/05:158 | pdf:p56:sv20_p0056_a017 | REPLACED | `### Trial Disease Assessments (TD)` → `### 5.1.4.2 Trial Disease Assessments` | 56 |
| 10 | model/05:178 | pdf:p57:sv20_p0057_a012 | REPLACED | `### Trial Disease Milestones (TM)` → `### 5.1.4.3 Trial Disease Milestones` | 57 |
| 11 | model/05:192 | pdf:p58:sv20_p0058_a008 | REPLACED | `### Trial Inclusion/Exclusion Criteria (TI)` → `### 5.1.5 Trial Inclusion/Exclusion Criteria` | 58 |
| 12 | model/05:209 | pdf:p59:sv20_p0059_a003 | REPLACED | `### Trial Summary (TS)` → `### 5.1.6 Trial Summary Information` | 59 |
| 13 | model/05:229 | pdf:p60:sv20_p0060_a002 | REPLACED | `### Challenge Agent Characterization (AC)` → `### 5.1.7 Challenge Agent Characterization` | 60 |
| 14 | model/05:259 | pdf:p61:sv20_p0061_a006 | REPLACED | `### Device Identifiers (DI)` → `### 5.2.1 Device Identifiers Dataset` | 61 |
| 15 | model/05:297 | pdf:p62:sv20_p0062_a002 | REPLACED | `### Non-host Organism Identifiers (OI)` → `### 5.2.2 Non-host Organism Identifiers Dataset` | 62 |
| 16 | model/05:40 | pdf:p52:sv20_p0052_a001 | REPLACED | TE ELEMENT Role → `Synonym Qualifier (ETCD)` | 52 |
| 17 | model/05:58 | pdf:p52:sv20_p0052_a015 | REPLACED | TA ARM Role → `Synonym Qualifier (ARMCD)` | 52 |
| 18 | model/05:61 | pdf:p53:sv20_p0053_a001 | REPLACED | TA ELEMENT Role → `Synonym Qualifier (ETCD)` | 53 |
| 19 | model/05:80 | pdf:p53:sv20_p0053_a017 | REPLACED | TX TXPARM Role → `Synonym Qualifier (TXPARMCD)` | 53 |
| 20 | model/05:151 | pdf:p56:sv20_p0056_a011 | REPLACED | TV VISIT Role → `Synonym Qualifier (VISITNUM)` | 56 |
| 21 | model/05:154 | pdf:p56:sv20_p0056_a014 | REPLACED | TV ARM Role → `Synonym Qualifier (ARMCD)` | 56 |
| 22 | model/05:203 | pdf:p58:sv20_p0058_a016 | REPLACED | TI IETEST Role → `Synonym Qualifier (IETESTCD)` | 58 |
| 23 | model/05:222 | pdf:p59:sv20_p0059_a013 | REPLACED | TS TSPARM Role → `Synonym Qualifier (TSPARMCD)` | 59 |
| 24 | model/05:242 | pdf:p60:sv20_p0060_a012 | REPLACED | AC ACPARM Role → `Synonym Qualifier (ACPARMCD)` | 60 |
| 25 | (base :72-73) | KB_AUTHORED:TX_structure | DELETED | D6 `**Structure:** One record per Trial Set parameter per Trial Set` + 空行 | 53 |
| 26 | (base :213-214) | KB_AUTHORED:TS_structure | DELETED | D6 `**Structure:** One record per trial summary parameter value` + 空行 | 59 |
| 27 | model/05:97 | KB_AUTHORED:TT_notes_col | INSERTED | D6: TT Notes 列来源说明 | 54 |
| 28 | model/05:117 | KB_AUTHORED:TP_notes_col | INSERTED | D6: TP Notes 列来源说明 | 55 |

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | :5 :11 :29 :45 :66 :89 :109 :140 :158 :178 :192 :209 :229 :259 :297 | 15 个 KB 自拟标题文字 → PDF 原编号标题 (层级不动: §5 / 5.1 `##`, 其余 `###`) | S-TDM + S-MOD2 S-2; 入站锚点 0 (见口径) |
| S-2 | :97 / :117 | TT/TP 表上方各加 1 行 D6 列说明 | S-MOD2 model/ 通用条 (KB 汇总列) |
| S-3 | base :72 / :213 | 删 TX/TS D6 Structure 行 | S-MOD2 model/ 通用条 (表题含 One Record per → D2) |

### 删除清单 (D2)
| # | 位置 (base 行) | 删除内容 (摘要) | 原因 | 保留 |
|---|---|---|---|---|
| D-1 | :5 | `## Overview` | KB 自拟标题, 被 PDF `5 Study-level Data` 取代 (同位置同级; 入站锚点 0) | :5 |
| D-2 | :11 | `## 5.1 Trial Design Model` | 缺 "The", 被 PDF 标题取代 | :11 |
| D-3..D-15 | :29 :45 :66 :91 :109 :138 :156 :176 :190 :207 :229 :259 :297 | 13 个 `### <域名> (XX)` 自拟标题 (TT/TP 用 "Reproductive", TS 缺 "Information", DI/OI 缺 "Dataset") | 被 PDF 编号标题取代; 域代码 `(XX)` 随之去掉 (见需主控定 M-1) | 同行改后 |
| D-16 | :72 (+:73 空行) | TX `> KB note …: **Structure:** One record per Trial Set parameter per Trial Set` | PDF 表题 a009 "Trial Sets—One Record per Trial Set Parameter" 已含记录结构 → S-MOD2 model/ 通用条 D2; **撤 B-model05 a2 主控裁定 #7 的 D6 保留** | :70 PDF 表题 |
| D-17 | :213 (+:214 空行) | TS `> KB note …: **Structure:** One record per trial summary parameter value` | 同上 (a006 "Trial Summary—One Record per Trial Summary Parameter") | :211 PDF 表题 |

### D6 标注清单
- 新增: :97 TT Notes 列说明; :117 TP Notes 列说明 (列格逐格: STUDYID 空 = PDF Notes/Usage 均空; DOMAIN `"TT"`/`"TP"` = PDF Notes 域代码; 其余行 = PDF Usage 逐字; 0 矛盾格).
- 保留 (B-model05 已过 reviewer): :261 DI Structure / :299 OI Structure (PDF 表题无 One Record per); :279 / :317 Mermaid rendering 注.
- 未标: H1 / `Source:` 行 / `---` 分隔 (导航).

### PDF_TYPO
- 无 (KB 承载列). 附记: p54 TT DOMAIN 行 PDF Definition 列误抄 STUDYID 定义 ("A sequence of characters used by the sponsor…"), 该列 R1 不收, KB 不受影响.

### census_items 处理 (13 张 C3 UNPARSEABLE, 改后仍 13 张)
| census (HEAD 行) | 改后表头行 | 表 | PDF 页 | 处理 | 逐格结果 |
|---|---|---|---|---|---|
| :35 | :35 | TE (7 行) | 51-52 | 渲染 + bbox + 原子 | 35 格一致 (改后); ELEMENT 补括注 |
| :53 | :53 | TA (10) | 52-53 | 同 | 50 格一致; ARM / ELEMENT 补括注 |
| :74 | :72 | TX (8) | 53 | 同 | 40 格一致; TXPARM 补括注 |
| :99 | :99 | TT (7, +Notes) | 54 | 同 | 35 格一致 + Notes 7 格见逐格表 |
| :117 | :119 | TP (10, +Notes) | 55 | 同 | 50 格一致 + Notes 10 格 |
| :144 | :146 | TV (9) | 56 | 同 | 45 格一致; VISIT / ARM 补括注 |
| :164 | :166 | TD (9) | 57 | 同 | 45 格一致 |
| :182 | :184 | TM (5) | 58 | 同 | 25 格一致 (TMDEF 括注 MIDSTYPE 既有) |
| :196 | :198 | TI (8) | 58-59 | 同 | 40 格一致; IETEST 补括注 |
| :215 | :215 | TS (11) | 59-60 | 同 | 55 格一致; TSPARM 补括注 |
| :235 | :235 | AC (12) | 60 | 同 | 60 格一致; ACPARM 补括注 (ACVALU (ACVAL) 既有) |
| :267 | :267 | DI (7) | 61 | 同 | 35 格一致 |
| :305 | :305 | OI (7) | 62 | 同 | 35 格一致 |
- `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` → `KB tables: 13; status: {'UNPARSEABLE': 13}; … diffs: 0` / `RESULT: GREEN` (census 读不到 v2.0 表, 逐格以下表 + 渲染为准).

### 逐格表 (改后每行一行; `python3 -I $S/celltab.py $S knowledge_base/model/05_study_level_data.md $S/base.md` 逐行计算; Label/Type 列 = #/Variable/Label/Type 4 格同时对 bbox 与原子; Role 列分别对 bbox / 原子; 渲染 110 dpi 逐行目视 13 页全部一致)
| 表 (census HEAD 行) | KB 行 (改后) | # | Variable | PDF 页 | Label/Type | Role (含括注) vs bbox | vs 原子 | Notes 列 (TT/TP) | 本批处理 |
|---|---|---|---|---|---|---|---|---|---|
| TE (:35) | 37 | 1 | STUDYID | p51 | 一致 | 一致 | 一致 | - | - |
| TE (:35) | 38 | 2 | DOMAIN | p51 | 一致 | 一致 | 一致 | - | - |
| TE (:35) | 39 | 3 | ETCD | p51 | 一致 | 一致 | 一致 | - | - |
| TE (:35) | 40 | 4 | ELEMENT | p52 | 一致 | 一致 | 一致 | - | Role 补括注 (ETCD) |
| TE (:35) | 41 | 5 | TESTRL | p52 | 一致 | 一致 | 一致 | - | - |
| TE (:35) | 42 | 6 | TEENRL | p52 | 一致 | 一致 | 一致 | - | - |
| TE (:35) | 43 | 7 | TEDUR | p52 | 一致 | 一致 | 一致 | - | - |
| TA (:53) | 55 | 1 | STUDYID | p52 | 一致 | 一致 | 一致 | - | - |
| TA (:53) | 56 | 2 | DOMAIN | p52 | 一致 | 一致 | 一致 | - | - |
| TA (:53) | 57 | 3 | ARMCD | p52 | 一致 | 一致 | 一致 | - | - |
| TA (:53) | 58 | 4 | ARM | p52 | 一致 | 一致 | 一致 | - | Role 补括注 (ARMCD) |
| TA (:53) | 59 | 5 | TAETORD | p52 | 一致 | 一致 | 一致 | - | - |
| TA (:53) | 60 | 6 | ETCD | p52 | 一致 | 一致 | 一致 | - | - |
| TA (:53) | 61 | 7 | ELEMENT | p53 | 一致 | 一致 | 一致 | - | Role 补括注 (ETCD) |
| TA (:53) | 62 | 8 | TABRANCH | p53 | 一致 | 一致 | 一致 | - | - |
| TA (:53) | 63 | 9 | TATRANS | p53 | 一致 | 一致 | 一致 | - | - |
| TA (:53) | 64 | 10 | EPOCH | p53 | 一致 | 一致 | 一致 | - | - |
| TX (:74) | 74 | 1 | STUDYID | p53 | 一致 | 一致 | 一致 | - | - |
| TX (:74) | 75 | 2 | DOMAIN | p53 | 一致 | 一致 | 一致 | - | - |
| TX (:74) | 76 | 3 | SETCD | p53 | 一致 | 一致 | 一致 | - | - |
| TX (:74) | 77 | 4 | SET | p53 | 一致 | 一致 | 一致 | - | - |
| TX (:74) | 78 | 5 | TXSEQ | p53 | 一致 | 一致 | 一致 | - | - |
| TX (:74) | 79 | 6 | TXPARMCD | p53 | 一致 | 一致 | 一致 | - | - |
| TX (:74) | 80 | 7 | TXPARM | p53 | 一致 | 一致 | 一致 | - | Role 补括注 (TXPARMCD) |
| TX (:74) | 81 | 8 | TXVAL | p53 | 一致 | 一致 | 一致 | - | - |
| TT (:99) | 101 | 1 | STUDYID | p54 | 一致 | 一致 | 一致 | 空 (PDF Usage 空) | - |
| TT (:99) | 102 | 2 | DOMAIN | p54 | 一致 | 一致 | 一致 | = PDF Notes 域代码 | - |
| TT (:99) | 103 | 3 | RSTGCD | p54 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TT (:99) | 104 | 4 | RSTAGE | p54 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TT (:99) | 105 | 5 | TTSTRL | p54 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TT (:99) | 106 | 6 | TTENRL | p54 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TT (:99) | 107 | 7 | TTDUR | p54 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TP (:117) | 121 | 1 | STUDYID | p55 | 一致 | 一致 | 一致 | 空 (PDF Usage 空) | - |
| TP (:117) | 122 | 2 | DOMAIN | p55 | 一致 | 一致 | 一致 | = PDF Notes 域代码 | - |
| TP (:117) | 123 | 3 | RPATHCD | p55 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TP (:117) | 124 | 4 | RPATH | p55 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TP (:117) | 125 | 5 | TPSTGORD | p55 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TP (:117) | 126 | 6 | RSTGCD | p55 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TP (:117) | 127 | 7 | RSTAGE | p55 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TP (:117) | 128 | 8 | TPBRANCH | p55 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TP (:117) | 129 | 9 | RPHASE | p55 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TP (:117) | 130 | 10 | RPRFDY | p55 | 一致 | 一致 | 一致 | = PDF Usage | - |
| TV (:144) | 148 | 1 | STUDYID | p56 | 一致 | 一致 | 一致 | - | - |
| TV (:144) | 149 | 2 | DOMAIN | p56 | 一致 | 一致 | 一致 | - | - |
| TV (:144) | 150 | 3 | VISITNUM | p56 | 一致 | 一致 | 一致 | - | - |
| TV (:144) | 151 | 4 | VISIT | p56 | 一致 | 一致 | 一致 | - | Role 补括注 (VISITNUM) |
| TV (:144) | 152 | 5 | VISITDY | p56 | 一致 | 一致 | 一致 | - | - |
| TV (:144) | 153 | 6 | ARMCD | p56 | 一致 | 一致 | 一致 | - | - |
| TV (:144) | 154 | 7 | ARM | p56 | 一致 | 一致 | 一致 | - | Role 补括注 (ARMCD) |
| TV (:144) | 155 | 8 | TVSTRL | p56 | 一致 | 一致 | 一致 | - | - |
| TV (:144) | 156 | 9 | TVENRL | p56 | 一致 | 一致 | 一致 | - | - |
| TD (:164) | 168 | 1 | STUDYID | p57 | 一致 | 一致 | 一致 | - | - |
| TD (:164) | 169 | 2 | DOMAIN | p57 | 一致 | 一致 | 一致 | - | - |
| TD (:164) | 170 | 3 | TDORDER | p57 | 一致 | 一致 | 一致 | - | - |
| TD (:164) | 171 | 4 | TDANCVAR | p57 | 一致 | 一致 | 一致 | - | - |
| TD (:164) | 172 | 5 | TDSTOFF | p57 | 一致 | 一致 | 一致 | - | - |
| TD (:164) | 173 | 6 | TDTGTPAI | p57 | 一致 | 一致 | 一致 | - | - |
| TD (:164) | 174 | 7 | TDMINPAI | p57 | 一致 | 一致 | 一致 | - | - |
| TD (:164) | 175 | 8 | TDMAXPAI | p57 | 一致 | 一致 | 一致 | - | - |
| TD (:164) | 176 | 9 | TDNUMRPT | p57 | 一致 | 一致 | 一致 | - | - |
| TM (:182) | 186 | 1 | STUDYID | p58 | 一致 | 一致 | 一致 | - | - |
| TM (:182) | 187 | 2 | DOMAIN | p58 | 一致 | 一致 | 一致 | - | - |
| TM (:182) | 188 | 3 | MIDSTYPE | p58 | 一致 | 一致 | 一致 | - | - |
| TM (:182) | 189 | 4 | TMDEF | p58 | 一致 | 一致 | 一致 | - | - |
| TM (:182) | 190 | 5 | TMRPT | p58 | 一致 | 一致 | 一致 | - | - |
| TI (:196) | 200 | 1 | STUDYID | p58 | 一致 | 一致 | 一致 | - | - |
| TI (:196) | 201 | 2 | DOMAIN | p58 | 一致 | 一致 | 一致 | - | - |
| TI (:196) | 202 | 3 | IETESTCD | p58 | 一致 | 一致 | 一致 | - | - |
| TI (:196) | 203 | 4 | IETEST | p58 | 一致 | 一致 | 一致 | - | Role 补括注 (IETESTCD) |
| TI (:196) | 204 | 5 | IECAT | p58 | 一致 | 一致 | 一致 | - | - |
| TI (:196) | 205 | 6 | IESCAT | p58 | 一致 | 一致 | 一致 | - | - |
| TI (:196) | 206 | 7 | TIRL | p59 | 一致 | 一致 | 一致 | - | - |
| TI (:196) | 207 | 8 | TIVERS | p59 | 一致 | 一致 | 一致 | - | - |
| TS (:215) | 217 | 1 | STUDYID | p59 | 一致 | 一致 | 一致 | - | - |
| TS (:215) | 218 | 2 | DOMAIN | p59 | 一致 | 一致 | 一致 | - | - |
| TS (:215) | 219 | 3 | TSSEQ | p59 | 一致 | 一致 | 一致 | - | - |
| TS (:215) | 220 | 4 | TSGRPID | p59 | 一致 | 一致 | 一致 | - | - |
| TS (:215) | 221 | 5 | TSPARMCD | p59 | 一致 | 一致 | 一致 | - | - |
| TS (:215) | 222 | 6 | TSPARM | p59 | 一致 | 一致 | 一致 | - | Role 补括注 (TSPARMCD) |
| TS (:215) | 223 | 7 | TSVAL | p59 | 一致 | 一致 | 一致 | - | - |
| TS (:215) | 224 | 8 | TSVALNF | p59 | 一致 | 一致 | 一致 | - | - |
| TS (:215) | 225 | 9 | TSVALCD | p59 | 一致 | 一致 | 一致 | - | - |
| TS (:215) | 226 | 10 | TSVCDREF | p59 | 一致 | 一致 | 一致 | - | - |
| TS (:215) | 227 | 11 | TSVCDVER | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 237 | 1 | STUDYID | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 238 | 2 | DOMAIN | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 239 | 3 | ACSEQ | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 240 | 4 | ACGRPID | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 241 | 5 | ACPARMCD | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 242 | 6 | ACPARM | p60 | 一致 | 一致 | 一致 | - | Role 补括注 (ACPARMCD) |
| AC (:235) | 243 | 7 | ACVAL | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 244 | 8 | ACVALU | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 245 | 9 | ACVALNF | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 246 | 10 | ACVALCD | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 247 | 11 | ACVCDREF | p60 | 一致 | 一致 | 一致 | - | - |
| AC (:235) | 248 | 12 | ACVCDVER | p60 | 一致 | 一致 | 一致 | - | - |
| DI (:267) | 269 | 1 | STUDYID | p61 | 一致 | 一致 | 一致 | - | - |
| DI (:267) | 270 | 2 | DOMAIN | p61 | 一致 | 一致 | 一致 | - | - |
| DI (:267) | 271 | 3 | SPDEVID | p61 | 一致 | 一致 | 一致 | - | - |
| DI (:267) | 272 | 4 | DISEQ | p61 | 一致 | 一致 | 一致 | - | - |
| DI (:267) | 273 | 5 | DIPARMCD | p61 | 一致 | 一致 | 一致 | - | - |
| DI (:267) | 274 | 6 | DIPARM | p61 | 一致 | 一致 | 一致 | - | - |
| DI (:267) | 275 | 7 | DIVAL | p61 | 一致 | 一致 | 一致 | - | - |
| OI (:305) | 307 | 1 | STUDYID | p62 | 一致 | 一致 | 一致 | - | - |
| OI (:305) | 308 | 2 | DOMAIN | p62 | 一致 | 一致 | 一致 | - | - |
| OI (:305) | 309 | 3 | NHOID | p62 | 一致 | 一致 | 一致 | - | - |
| OI (:305) | 310 | 4 | OISEQ | p62 | 一致 | 一致 | 一致 | - | - |
| OI (:305) | 311 | 5 | OIPARMCD | p62 | 一致 | 一致 | 一致 | - | - |
| OI (:305) | 312 | 6 | OIPARM | p62 | 一致 | 一致 | 一致 | - | - |
| OI (:305) | 313 | 7 | OIVAL | p62 | 一致 | 一致 | 一致 | - | - |

### 需主控定 (已按下列默认执行; 每条可一步回退)
- **M-1 域代码随标题丢失**: 13 个 `### … (XX)` 换成 PDF 编号标题后, 标题里不再有 TE/TA/TX/TT/TP/TV/TD/TM/TI/TS/AC/DI/OI 代码 (正文仅 TE 有 `"TE"`; TT/TP/各表 DOMAIN 行不全含代码). 若需保留检索性, 备选 = 每节标题下加一行 `> KB note (not in SDTM v2.0): domain code XX.` (D6). 回退 = 按 jsonl HEADING 行恢复旧标题.
- **M-2 层级扁平 (O35-1 剩余项)**: 5.1.1.1-2 / 5.1.3.1-2 / 5.1.4.1-3 共 7 个四级节与父节同为 `###` (S-FND: 既有层级不改). 改 `####` 无锚点风险, 待主控/T4 定.
- **M-3 TX/TS Structure 删除撤回 B-model05 a2 #7**: 按 S-MOD2 model/ 通用条 (表题含 One Record per → D2). 若主控维持 #7, 恢复 base :72 / :213 两行即可.
- **M-4 TS Usage Restrictions (O35-3)**: TSVALCD / TSVCDREF / TSVCDVER 的 "Not in nonclinical trials" 未补 (R1 缺列不补; TS 表无 KB 汇总列可承载). TT/TP 的同类值留在 Notes 列 (D6 已说明), 两处承载不一致 → T4.
- O35-2 (TT/TP Notes 列) 已按 D6 处理; O35-4 (Role 括注) 已补齐 → O35 只余 M-2 / M-4.

### 范围外发现
- 无 KB 文件需改. (fp 观察: `ig34_p0441_a002/a003/a007` 的 hit_any 由 ch10 / None 变为 `domains/DI/assumptions.md` — 来自并行批 DI §9 引言, 非本批.)

### 验证 (S = scratchpad/t2s_S-MOD3_writer, 均在改后运行, repo 根)
- `python3 -I $S/scan.py knowledge_base/model/05_study_level_data.md` → `HIT 89 MISS 0` (对 `$S/base.md` → `HIT 74 MISS 15`, 15 = 编号标题)
- `python3 -I $S/order.py knowledge_base/model/05_study_level_data.md $S` → `order bad 0`
- `python3 -I $S/bbox_tbl.py $S/bbox_rows.json && python3 -I $S/cmp.py $S knowledge_base/model/05_study_level_data.md` → `tables kb 13 pdf 13` / `cells 550 diffs 0` (改前 9)
- `python3 -I $S/indep.py knowledge_base/model/05_study_level_data.md` → `tables kb 13 atoms 13 rows 110 110` / `cells 550 diffs 0` (改前 9)
- `python3 -I $S/rscan.py knowledge_base/model/05_study_level_data.md` → `HIT 97`; NOPDF = H1 / Source / D6 ×6 / mermaid 代码 (未截断全量输出已核)
- `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` → `KB tables: 13; status: {'UNPARSEABLE': 13}; … diffs: 0` / `RESULT: GREEN`
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → RED (71 回退, 全为并行批 ig34); 按 "baseline 命中/目标含 model/05" 的 180 个原子过滤: 回退 **0**, sv20 回退 0; 其中 28 个 sv20 原子 hit_target None → model/05 (改善, 标题补入后命中).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`
- 渲染: `pdftoppm -f 51 -l 63 -r 110 -png source/cdisc/SDTM_v2.0.pdf $S/p`, 13 页逐页目视 (表 110 行、2 张 Concept Map).

### git diff --stat
```
 knowledge_base/model/05_study_level_data.md | 56 ++++++++++++++---------------
 1 file changed, 28 insertions(+), 28 deletions(-)
```
- 机器可读: `work/t2_batches/S-MOD3.writer.jsonl` 41 行 = 15 HEADING + 9 Role + 2 DELETED + 2 D6 INSERTED + 13 census VERIFIED.

### attempt 1 更正 (同 attempt, KB / jsonl 未再改; 以本节为准)
1. **逐页日志原子数**: 上表手填有 2 处误记. 脚本重算 (`python3 -I -c` 按 `pdf_atoms.jsonl` sv20 p51-63 非 TABLE_ROW/TABLE_HEADER/FIGURE 计数) → p51 19 / p52 6 / p53 5 / **p54 12** (上表写 11) / p55 6 / p56 12 / p57 3 / **p58 5** (上表写 4) / p59 4 / p60 4 / p61 9 / p62 4 = **89** (= scan.py HIT 89). 各页命中数同此 (MISS 0).
2. **fp 归因**: "28 个 sv20 原子 hit_target None → model/05 (标题补入后命中)" 归因有误. 这 28 个全是 SENTENCE/LIST_ITEM (B-model05 恢复的叙述句与列表项), 无 HEADING 原子; fp_baseline 早于 B-model05, 故变化**非本批所致**. 本批 15 个 HEADING 原子不在变化列表中 (fp_match 不以它们判回退). 结论不变: model/05 相关 180 原子回退 0.

## attempt 1 delta (主控裁定 M-1..M-4, 2026-11-26)
- md5 `804e1689…` → `88d0db4cc8858975bb3f1dc0748d020d` (333 行不变). 只做 M-1.
- **M-1**: 13 个 `###` PDF 编号标题后追加检索导航用域代码 (不加 D6): :29 (TE) / :45 (TA) / :66 (TX) / :89 (TT) / :109 (TP) / :140 (TV) / :158 (TD) / :178 (TM) / :192 (TI) / :209 (TS) / :229 (AC) / :259 (DI) / :297 (OI). 删除清单 D-3..D-15 相应更正为 "标题文字按 PDF 改, 域代码保留".
- M-2 层级扁平不改 (O35-1 剩余); M-3 同意 (D-16/D-17 维持); M-4 不补 (O35-3). 均仅记录.
- 复跑 (S = scratchpad/t2s_S-MOD3_writer, repo 根): `python3 -I $S/scan.py knowledge_base/model/05_study_level_data.md` → `HIT 89 MISS 0`; `python3 -I $S/order.py knowledge_base/model/05_study_level_data.md $S` → `order bad 0`; `python3 -I $S/cmp.py $S knowledge_base/model/05_study_level_data.md` → `cells 550 diffs 0`; `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42`; `git diff --stat` → `28 insertions(+), 28 deletions(-)`.
