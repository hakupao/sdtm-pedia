# T2S S-MOD1 writer checkpoint (扫描批: model/01 + model/03 + model/04, 源 SDTM v2.0)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `42fecd3`; 改前 md5 (= HEAD): model/01 `531c2d5459604aefdc238ff56eb92bef` (206 行) / model/03 `9247f1033a2f8a35b6907ba7d0d26a64` (190 行) / model/04 `fd158813254c0101a563e519f25a55b4` (38 行).
- scratch `S` = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-MOD1_writer/`
  (base_*.md = HEAD 副本; lines.py = bbox 按行重组; tbl.py = p40-50 bbox 多表解析 (每页表头 x 分 12 列) → pdf_tabs.json; cmp.py = KB 表核心格 #/Variable/Label/Type/Role(Qualified) 对 bbox; scan.py = PDF 非表原子 → KB 归一子串; rscan.py = KB 非表行逐句 → PDF layout 归一; 渲染 p8 (110 dpi + 250 dpi 图局部 fig-08.png)、p40-50 130 dpi `r-NN.png` 逐页目视)
- 真值顺序: 渲染图 > bbox 分列 > layout 文本 > 原子. 表题破折号: bbox 词框给 "-", layout 与渲染为 em dash "—" → 用 "—" (同 model/02).

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| model/01_concepts_and_terms.md | §1-§2 (1.1-1.4, 2, 2.1, 2.2) | 4-10 | **4-10** | p3 = 目录; p4 首行 `1 Introduction`; p7 仅 §1.4 末句; p8 `2 Model Concepts…` + Concept Map 图; p10 §2.2 止于页中; p11 首行 `3 Study Subject Data` → 不归本批 |
| model/03_special_purpose_domains.md | §3.2 (3.2.1-3.2.3.4) | 40-49 | **40-49** | p39 末 = §3.1.5 Timing 表 48 --PDUR; p40 首行 `3.2 Special-purpose Domains`; p49 SM 表止于页中, 下部空白; p50 首行 `4 Associated Persons Data` |
| model/04_associated_persons.md | §4 | 50 | **50** | p50 全页 = §4 (引言 + 3 项列表 + 2 段 + 表 + 末段); p51 首行 `5 Study-level Data` |

### 口径
- R1: v2.0 变量表 model/ 收 5 列 (#/Variable/Label/Type/Role), 缺列 (Format/Qualified/Usage/C-code/Definition/Notes/Examples) 不补; 5 列 floor 内须与 PDF 一致. Role 写法沿用 model/ 约定 `Role (Variable(s) Qualified)`, 多个用 `/` (PDF "AGE; AGETXT" → KB "AGE/AGETXT", 约定, 不改).
- S-MOD2 主控裁定 (model/ 通用): KB 自拟 Notes 列 → 表上方 D6 列说明 (措辞照实: quote / condense / supplement); 与 PDF 矛盾格 → PDF 原文 (D2); 无依据且不矛盾格留在 D6 下. PDF 表题含 "One Record per…" → KB `**Structure:**` 行 D2 删; 不含 → D6 保留 (`> KB note (not in SDTM v2.0): **Structure:** …`, 同 model/05 S-MOD3 写法).
- S-MOD2 review 教训: sv20 页 census/fp 为空比较 → 本批表格以 bbox 独立分列 (tbl.py) + 渲染逐格为准.
- 数字/编号标题: 既有 KB 标题不改 (规则 6); PDF 编号标题按 model/05 (S-MOD3) / model/02 (A2c-1) 先例补为既有 H2 下的 H3 (`### 3.2.1 Demographics`); 无 KB 承载的父节 §3.2.3 补为 H2.
- D6 措辞 `> KB note (not in SDTM v2.0):`.

## 段 1: model/01 (p4-10)

### 双向全扫 — 逐页日志 (model/01)
方法: PDF→KB `python3 -I $S/scan.py knowledge_base/model/01_concepts_and_terms.md 4 10` (sv20 p4-10 非表原子 HEADING/SENTENCE/LIST_ITEM/FIGURE) → 改后 **HIT 132 MISS 2** (共 134: HEADING 11 / SENTENCE 63 / LIST_ITEM 59 / FIGURE 1) (a020 = T-1 PDF_TYPO, a010 = FIGURE, 以 Mermaid + D6 承载); 改前 HIT 128 MISS 6 (另 4 = p9 a014-a017 子类表把 "X Qualifiers," 拆到 Subclass 格、删句末 ";"/"; and"). KB→PDF `python3 -I $S/rscan.py knowledge_base/model/01_concepts_and_terms.md 4 10` → HIT 161 NOPDF 20, 20 条 = H1/Source 4 段 + :77/:106 PDF 折行 "-\n-BEATNO" / "--\nMETHOD" (目视 p6 逐字一致) + :94 T-1 + 2 处 D6 (Mermaid 说明 4 段 + 子类例 6 段) + KB 导航标题 `### Variable Roles` / `### Qualifier Variable Subclasses`. 无其他无出处行.

| 页 | 节 | PDF→KB: 句/列表/标题 原子数, 命中, 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 4 | §1 / 1.1 / 1.2 | 全命中, 0 缺 | :5-28 逐字 (B-model01 补); 无出处 0 | — | 6 个 IG 链接 + 3 项列表逐字 |
| 5 | §1.3 / 1.4 | 全命中, 0 缺 | :30-67; 无出处 0 | — | 11 列名列表 = PDF 列表 (非表) |
| 6 | §1.4 | 全命中 (a020 改值) | :69-106; :94 T-1 | — | T-1 沿用 B-model01 登记 |
| 7 | §1.4 尾 | 1/1/0 | :108 | — | |
| 8 | §2 + Concept Map | 全命中; FIGURE a010 → Mermaid 重绘 | :110-152; Mermaid 与 PDF 图不一致 4 处 → 按 PDF 改 (#M-1); 旧 `> **Key:**` 行与 PDF 图例矛盾 → D2 (D-1); 加 D6 (#M-2) | 图逐边/逐色对 250 dpi 渲染 (见下) | |
| 9 | §2.1 | 全命中 (改后); a014-a017 1→已修 4 | :154-188; 子类表 → PDF 列表 (#M-3), Examples 列 → D6 (#M-4) | census C3 :176 子类表 → 已改为列表, 不再是表 | |
| 10 | §2.1 尾 / §2.2 | 全命中, 0 缺 | :188 尾句 + :190-209 = 引导句 + 11 项列表 + 段落逐字 | — | §2.2 为列表 (B-model01 a2 已改) |

### Concept Map 逐元素核 (渲染 p8 250 dpi, `$S/fig-08.png`)
| 元素 | PDF | 旧 KB Mermaid | 改后 |
|---|---|---|---|
| 节点文字 | "Study Data Tabulation Model" 等 13 个 | 换行处丢空格 ("TabulationModel", "forSubject" 等) | 恢复空格, 13 节点名 = PDF |
| SDTM includes → 4 | Subject / AP / Study-Level / Relationship | 同 | 同 |
| Subject Data include → | GOC + Special Purpose | 同 | 同 |
| AP Data include → | GOC + Special Purpose (两箭头) | **缺** | 补 `AP -->|include| GOC/SPD` |
| Study-Level include → | Trial Design Model + Study Reference Datasets | 同 | 同 |
| GOC include → | Events / Interventions / Findings | 同 | 同 |
| subtype of | 箭头 Findings About → Findings (箭头指向 Findings) | `FI --> FA` (方向反) | `FA -->|subtype of| FI` |
| 颜色 (图例) | 绿 = Group of individually specified datasets: Relationship / Special Purpose / Trial Design / Study Reference; 黄 = Extensible set…: Events / Interventions / Findings / Findings About; 其余 5 个灰底无图例 | RD/GOC/SPD/EV/IV/FI/FA/TDM 全标 "extensible" 绿, SRS 无 | `individual` (绿) 4 个 + `extensible` (黄) 4 个, 其余无 class |
| 图例文字 | 2 条 (上) | `> **Key:** Plain box = Group…; Green filled box = Extensible…` (与 PDF 配色矛盾) | D2 删, 图例文字并入 D6 说明行 |

### 变更清单 (model/01)
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| M-1 | model/01:126-152 | pdf:p8:sv20_p0008_a010 (FIGURE) | REPLACED | Mermaid 按 PDF 图改: 节点名补空格; 补 AP→GOC/SPD 两边; subtype 方向改 FA→FI; classDef 改为 individual(绿)/extensible(黄) 按 PDF 配色; 删 `%% Key` 注释 | 8 |
| M-2 | model/01:124 | KB_AUTHORED | D6 | `> KB note (not in SDTM v2.0): Mermaid rendering of the PDF figure "Concept Map. Relationships Between SDTM Domains" (p8). PDF key: …` (图例 2 条为 PDF 图内文字) | 8 |
| M-3 | model/01:174-178 | pdf:p9:sv20_p0009_a014-a018 | TABLE_REBUILT (表→列表) | `Subclass/Purpose/Examples` 3 列表 → PDF 5 项列表逐字 (恢复 "X Qualifiers," 起句、句末 ";" / "; and" / "."); 规则 3 跟 PDF 走 (同 B-model01 a2 §2.2 先例, S-CH4 自造列口径) | 9 |
| M-4 | model/01:180-185 | KB_AUTHORED (旧 Examples 列) | D6 | 旧 Examples 列 5 格原样迁入表下 D6 引用块 (每 subclass 一行); 逐格对 model/02 Role 列不矛盾 (--SLIFE Record Qualifier → AESLIFE; --LOINC 已于 B-model01 删) | 9 |
| M-5 | model/01:94 | pdf:p6:sv20_p0006_a020 | VERIFIED (SKIPPED_PDF_TYPO, 沿用 T-1) | "Section 4" 保留 | 6 |

### 结构改动清单 (model/01)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | :174-185 | 子类 3 列表 (表头 + 5 行) + 表上 D6 "Examples column is KB-authored" → 5 项列表 + D6 例子块 | 规则 3 (PDF 为列表) + S-CH4 (自造列 → 表下 D6) |
| S-2 | :124-152 | Mermaid 重写 (边/色/节点名) | dispatch "PDF 图的 Mermaid 重绘须与 PDF 图逻辑一致" |

### 删除清单 (model/01)
| # | 原位置 (HEAD) | 内容 | 原因 | 保留/替代 |
|---|---|---|---|---|
| D-1 | :152 | `> **Key:** Plain box = Group of individually specified datasets. Green filled box = Extensible set…` | 与 PDF 图例矛盾 (PDF: 绿 = individually specified; 黄 = extensible) → D2 | :124 D6 内 PDF 图例原文 |
| D-2 | :126-128 | Mermaid `%% Key:` 3 行注释 | 同 D-1 矛盾 | 同上 |
| D-3 | :174 | `> KB note (not in SDTM v2.0): The Examples column is KB-authored.` | 所指列已移出 (表→列表) | :180 新 D6 块 |
| D-4 | :176-182 | 子类表表头/分隔/5 行 | 由 PDF 列表 (逐字) + D6 例子块取代, 无信息丢失 | :174-185 |

### PDF_TYPO (model/01)
| # | 位置 | PDF | KB | 依据 |
|---|---|---|---|---|
| T-1 (沿用 B-model01) | model/01:94 (sv20_p0006_a020) | "still listed in Section 3, Associated Persons Data" | Section 4 | p5 两处 + p8 均为 "Section 4, Associated Persons Data"; §3 = Study Subject Data |

### census_items (model/01)
| census | 处理 |
|---|---|
| `model/01_concepts_and_terms.md:176` (C3 UNPARSEABLE, Subclass/Purpose/Examples) | PDF p9 为列表非表 → 改为列表 (M-3), 逐项对渲染 p9 (`pdftoppm -f 9 -l 9 -r 110 -png source/cdisc/SDTM_v2.0.pdf $S/p` → `$S/p-09.png`, PDF 列表无粗体, KB 粗体为既有强调, S-CH1 口径不改) / layout 一致; 表不再存在, census 项关闭. Examples 列 5 格逐格见 M-4 |

- md5 改后 `0a4855b8fd85e1c44974c1266b9362ec` (209 行); `git diff --stat -- knowledge_base/model/01_concepts_and_terms.md` → `1 file changed, 32 insertions(+), 29 deletions(-)`

## 段 2: model/03 (p40-49) + 段 3: model/04 (p50)

### 双向全扫 — 逐页日志 (model/03, model/04)
方法: PDF→KB `python3 -I $S/scan.py knowledge_base/model/03_special_purpose_domains.md 40 49` → 改后 **HIT 41 MISS 0** (非表原子 41 = HEADING 14 / SENTENCE 27; 改前 HIT 8 MISS 33); `… model/04_associated_persons.md 50 50` → 改后 **HIT 16 MISS 0** (HEADING 2 / SENTENCE 11 / LIST_ITEM 3; 改前 HIT 4 MISS 12). 表行: `python3 -I $S/tbl.py $S/pdf_tabs.json` (bbox 独立分列, 7 表 106 行) + `python3 -I $S/cmp.py $S` → **cells 530 diffs 0** (改前 526 格 2 DIFF; AP 表补 # 列后 +4 格); 另以 pdf_atoms TABLE_ROW (107 原子, a001 p45 为 IDVAR 续行) 对 bbox 核 #/Name/Label/Type/Role/Qualified/Usage/C-code → 106/106 行 0 差 (两种抽取一致); 每页 130 dpi 渲染目视 (`$S/r-40.png`…`r-50.png`). 注: 原子 sv20_p0050_a016-a019 把 AP 表 Notes 文字放在 Definition 列, 渲染 p50 确认在 Notes 列 (原子列位错, 不影响 KB).
KB→PDF `python3 -I $S/rscan.py knowledge_base/model/03_special_purpose_domains.md 40 49` → HIT 44 NOPDF 34; 34 段 = H1/Source 3 + KB 导航标题 (`## Overview` / `## Comments (CO)` / `## Subject Elements (SE)` / `## Subject Visits (SV)` / `## Subject Disease Milestones (SM)` / 6 个 `### Variables (N variables)` / `### Key Reference Date Variables`) + 10 处 D6 (各 1-2 段). model/04 → HIT 18 NOPDF 16 = H1/Source 3 + 导航标题 4 + D6 2 块 (6 段) + 交叉引用 1 行 (2 段). 无其他无出处行.

| 页 | 节 | PDF→KB: 句/列表/标题 原子数, 命中, 缺→已补; 表行 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格) | 备注 |
|---|---|---|---|---|---|
| 40 | §3.2 / §3.2.1 | 10 / 10 / 7→7 (a001 标题, a003 "(see Section 3.2.1, Demographics)", a005 标题, a006/a007/a010 句, a011 表题); 表行 6 | :5-23; 旧 DM 首 2 句 (a006/a007 改写) → D2 (D-5); Structure 行 → D6 (#P-4) | DM 1-6 逐格一致; RFENDTC Notes D2 (#C-1) | |
| 41 | §3.2.1 | 0; 表行 7 | DM 7-13 | 逐格一致 | |
| 42 | §3.2.1 | 0; 表行 13 | DM 14-26 | 逐格一致; AGE Notes D2 (#C-2); SPECIES/STRAIN "Not for"→"Not in" (#C-4) | |
| 43 | §3.2.1 | 0; 表行 11 | DM 27-37 | 逐格一致 (RPATHCD Label 改 #V-1); ARMNRS Notes D2 (#C-3); SETCD Notes 无依据 (M-2) | |
| 44 | §3.2.1 尾 / §3.2.2 | 6 / 6 / 5→5 (a002 标题, a003/a004/a006 句, a007 表题; a005 既有); 表行 9 (DM 38, CO 1-8) | :81-93; 旧 CO 首句 (KB 自写) + Structure → D6 (#P-5) | DM 38 / CO 1-8 逐格一致 | |
| 45 | §3.2.2 尾 / §3.2.3 / §3.2.3.1 | 8 / 8 / 7→7 (a009 标题, a010/a011 句, a012 标题, a013/a014/a016 句); 表行 7 (CO 9-15) | :113-125 新增 §3.2.3 H2; 旧 SE 首句 → PDF 句 (D-6), "(blocks of time)" → D6 (#P-6) | CO 9-15 逐格一致 | a015 句 (SEUPDES) 既有 |
| 46 | §3.2.3.1 尾 / §3.2.3.2 | 4 / 4 / 4→4 (a001 表题, a016 标题, a017/a018 句); 表行 13 | 旧 SE Structure → D2 (D-7); 旧 SJ 首句 / Structure / **Note:** → D2 (D-8/D-9/D-10) | SE 1-13 逐格一致 | a019 句 既有 |
| 47 | §3.2.3.2 尾 / §3.2.3.3 | 5 / 5 / 5→5 (a001 表题, a013 标题, a014/a015/a017 句); 表行 10 | 旧 SV 首句 / Structure → D2 (D-11/D-12) | SJ 1-10 逐格一致 | a016 句 既有 |
| 48 | §3.2.3.3 | 1 / 1 / 1→1 (a001 表题); 表行 16 | | SV 1-16 逐格一致 (SVREASOC Label 改 #V-2) | |
| 49 | §3.2.3.4 | 4 / 4 / 4→4 (a001 标题, a002/a003 句, a004 表题); 表行 10 | 旧 SM 首句 → PDF 句 (D-13), 例列表 → D6 (#P-7); Structure → D2 (D-14) | SM 1-10 逐格一致; MIDS Notes D2 (#C-5) | |
| 50 | §4 | 16 / 16 / 12→12 (a001 标题, a004 句尾 "including:", a005-a007 列表, a008/a009 段, a010-a013 段, a014 表题); 表行 4 | model/04 全文重排: 旧 KB 列表/原则 → D6 或 D2 (见删除清单 D-15..D-20) | AP 1-4 表重建 (+# 列; Notes = PDF Notes 逐字) | a002/a003/a020/a021 既有 |

### 变更清单 (model/03, model/04)
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| P-1 | model/03:7 | pdf:p40:sv20_p0040_a001 | INSERTED | `### 3.2 Special-purpose Domains` (H3, `## Overview` 下) | 40 |
| P-2 | model/03:9 | pdf:p40:sv20_p0040_a003 | REPLACED (插入短语) | 补 "(see Section 3.2.1, Demographics)" | 40 |
| P-3 | model/03:13,15 | pdf:p40:a005/a006/a007/a010 | INSERTED | `### 3.2.1 Demographics` + DM 段落改为 PDF 原文 (首 2 句 PDF 原句 + 补末句 "See the respective implementation guides …") | 40 |
| P-4 | model/03:17 | KB_AUTHORED | D6 | DM `**Structure:** One record per subject` → `> KB note (not in SDTM v2.0): **Structure:** …` (PDF 表题无 "One Record per") | 40 |
| P-5 | model/03:21,23 | pdf:p40:a011 + KB_AUTHORED | INSERTED + D6 | 表题 `**Subject Demographics Domain Variables**`; Notes 列 D6 说明 | 40 |
| P-6 | model/03:68 | KB_AUTHORED (census :60) | D6 | Key Reference Date 表上方 D6 (表为 KB 汇总; Description 列 = PDF Label; Typical Use 为 KB 写, RFENDTC/RFPENDTC 引 PDF Notes) | 40-41 |
| P-7 | model/03:83,85,87 | pdf:p44:a002/a003/a004/a006 | INSERTED | `### 3.2.2 Comments` + PDF 段落 (首句 "Comments are collected during the conduct of many studies."、"These are normally supplied …") + "See the implementation guides …" | 44 |
| P-8 | model/03:89 | KB_AUTHORED | D6 | CO `**Structure:**` 行 + 旧首句 "…used to capture free-text comments that are not a part of normal domain data." 合入一行 D6 (PDF 表题无 "One Record per") | 44 |
| P-9 | model/03:93 | pdf:p44:a007 | INSERTED | 表题 `**Comments Domain Variables**` | 44 |
| P-10 | model/03:113,115 | pdf:p45:a009/a010/a011 | INSERTED | 新增 H2 `## 3.2.3 Subject Summary Domains` + 2 句 (S-INT 口径: 有正文父节补 H2) | 45 |
| P-11 | model/03:119,121,123 | pdf:p45:a012/a013/a014/a016 | INSERTED | `### 3.2.3.1 Subject Elements` + PDF 段落 (替旧改写句) + "See the implementation guides …" | 45 |
| P-12 | model/03:125 | KB_AUTHORED | D6 | 旧 "(blocks of time)" 释义 → `> KB note …: Elements are blocks of time.` | — |
| P-13 | model/03:129,131 | pdf:p46:a001 + KB_AUTHORED | INSERTED + D6 | 表题 `**Subject Elements—One Record per Actual Element per Subject**`; Notes 列 D6 | 46 |
| P-14 | model/03:151,153 | pdf:p46:a016/a017/a018 | INSERTED | `### 3.2.3.2 Subject Repro Stages` + PDF 段落 (含 "(not for use with human clinical trials)" 与 "(see Section 5.1.3.1, Trial Repro Stages)") | 46 |
| P-15 | model/03:157,159 | pdf:p47:a001 + KB_AUTHORED | INSERTED + D6 | 表题 `**Subject Repro Stages—One Record per Actual Repro Stage per Subject**`; Notes 列 D6 | 47 |
| P-16 | model/03:176,178,180 | pdf:p47:a013/a014/a015/a017 | INSERTED | `### 3.2.3.3 Subject Visits` + PDF 段落 + "See the implementation guides …" | 47 |
| P-17 | model/03:184,186 | pdf:p48:a001 + KB_AUTHORED | INSERTED + D6 | 表题 `**Subject Visits—One Record per Subject Visit, per Subject**`; Notes 列 D6 | 48 |
| P-18 | model/03:209,211,213 | pdf:p49:a001/a002/a003 | INSERTED | `### 3.2.3.4 Subject Disease Milestones` + PDF 句 + "See the implementation guides …" | 49 |
| P-19 | model/03:215 | KB_AUTHORED | D6 | 旧 "(e.g., diagnosis, progression, relapse, remission)" → D6 例子行 | — |
| P-20 | model/03:219,221 | pdf:p49:a004 + KB_AUTHORED | INSERTED + D6 | 表题 `**Subject Disease Milestones—One Record per Disease Milestone, per Subject**`; Notes 列 D6 | 49 |
| V-1 | model/03:61 | pdf:p43:sv20_p0043 RPATHCD (row 35) col Label | REPLACED | "Reproductive Pathway Code" → "Planned Repro Path Code" | 43 |
| V-2 | model/03:197 | pdf:p48:SVREASOC (row 8) col Label | REPLACED | "Reason for Occurrence Value" → "Reason for Occur Value" | 48 |
| C-1 | model/03:32 | pdf:p40-41:RFENDTC Notes | REPLACED (D2) | "Usually date of last dose" → PDF Notes 首句 "Usually equivalent to the date/time when a subject was determined to have ended the trial." | 40 |
| C-2 | model/03:45 | pdf:p42:AGE Notes | REPLACED (D2) | "Numeric age at RFSTDTC" → PDF Notes "May be derived as (RFSTDTC-BRTHDTC), but BRTHDTC may not be available …" | 42 |
| C-3 | model/03:58 | pdf:p43:ARMNRS Notes | REPLACED (D2) | "When arm assignment is not possible" → PDF Notes 首句 "The reason why the actual arm variables are null or why both …" | 43 |
| C-4 | model/03:51-53,61 | pdf:p42-43:Usage (SPECIES/STRAIN/SBSTRAIN/RPATHCD) | REPLACED (词替换) | "**Not for human clinical trials**" → "**Not in human clinical trials**" (PDF Usage 原词; 粗体为既有强调, 未动) | 42-43 |
| C-5 | model/03:229 | pdf:p49:MIDS Notes | REPLACED (D2) | "Unique name linking to TM" → PDF Notes 原文 "Name of the specific disease milestone. For … sequence number." | 49 |
| C-6 | model/03:73 | pdf:p40-41:RFENDTC Notes (KB 汇总表) | REPLACED (D2) | Typical Use "Usually last dose date" → 同 C-1 PDF 句 | 40 |
| C-7 | model/03:79 | pdf:p41:RFPENDTC Notes (KB 汇总表) | REPLACED (D2) | Typical Use "Completion/withdrawal date" → PDF Notes "Should correspond to the last known date of contact." | 41 |
| A-1 | model/04:7 | pdf:p50:sv20_p0050_a001 | INSERTED | `### 4 Associated Persons Data` (H3, `## Overview` 下) | 50 |
| A-2 | model/04:9 | pdf:p50:a004 | REPLACED (插入短语) | 句尾 "AP rules:" → "AP rules, including:" | 50 |
| A-3 | model/04:11-13 | pdf:p50:a005/a006/a007 | INSERTED | PDF 3 项列表逐字 | 50 |
| A-4 | model/04:17-19 | KB_AUTHORED | D6 | `### AP Domain Rules` 下 Prefix convention / APID 第 1 句 → D6 引用块 (不矛盾) | — |
| A-5 | model/04:21 | 交叉引用 (D2 替代) | INSERTED | `> See [01…#changes-to-datasets-and-variables] for the removal of APID from Section 3.1.4; RSUBJID, RDEVID, and SREL are described in the table below.` (导航, 不 D6) | 6 / 50 |
| A-6 | model/04:25 | pdf:p50:a008/a009 | INSERTED | SDTMIG-AP 段 (含 URL) 逐字, 置 `### Key Principles` 下 | 50 |
| A-7 | model/04:27-29 | KB_AUTHORED | D6 | Key Principles 2 条 (同变量/角色/CT 适用; 非 core SDTMIG) → D6 | — |
| A-8 | model/04:33 | pdf:p50:a010-a013 | INSERTED (替 D2) | "The variables in the following table are used in AP domains. …" 段逐字 | 50 |
| A-9 | model/04:35 | pdf:p50:a014 | INSERTED | 表题 `**Associated Persons—Additional Identifier Variables**` | 50 |
| A-10 | model/04:37-42 | pdf:p50:a015-a019 + census :31 | TABLE_REBUILT | 补 `#` 列 (1-4); Notes 列 = PDF Notes 逐字 (RSUBJID 补第 3 句; SREL 3 句恢复 PDF 原文, 旧简写 D2) — 列 = 单一 PDF 列, 不加 D6 (B-model06 M-2b 式) | 50 |

### 结构改动清单 (model/03, model/04; reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-3 | model/03 各域 H2 下 | 插入 PDF 编号标题 H3 ×7 (`### 3.2` / `3.2.1` / `3.2.2` / `3.2.3.1`-`3.2.3.4`); 既有 H2 (`## Demographics (DM)` 等) 不动 | 规则 6 + model/05 (S-MOD3) / model/02 A2c-1 先例 |
| S-4 | model/03:113 | 新增 H2 `## 3.2.3 Subject Summary Domains` (+2 句) 于 `## Subject Elements (SE)` 前 | S-INT 口径 (有正文父节补 H2) |
| S-5 | model/03 4 处 | SE/SJ/SV/SM `**Structure:**` 行删, 原位改为 PDF 表题 (在 `### Variables` 下) | S-MOD2 主控裁定 (表题含 "One Record per" → D2) |
| S-6 | model/03 DM/CO | `**Structure:**` 行移到 PDF 段落之后并转 D6 | S-MOD2 裁定 (表题无 "One Record per" → D6) |
| S-7 | model/04 全文 | 重排为 PDF 顺序: 引言 + 3 项列表 → (KB D6 + 交叉引用) → SDTMIG-AP 段 → (KB D6) → 表前段 → 表题 → 表 → 末段; KB 标题 `### AP Domain Rules` / `### Key Principles` / `### Variables Used in Associated Persons Data` 保留 (规则 6) | brief 授权 1 |
| S-8 | model/04 表 | 5 列 → 6 列 (+#), 4 行 | R1 5 列 floor (# 列) |

### 删除清单 (model/03, model/04; reviewer 逐条确认)
| # | 原位置 (HEAD) | 内容 | 原因 | 保留/替代 |
|---|---|---|---|---|
| D-5 | model/03:13 前 2 句 | "The Demographics domain includes a set of essential standard variables … It is the parent domain to which all other observations are linked." | R2 残留改写 (a006/a007 已逐字补); 行内无其他原子 | :15 PDF 原句 |
| D-6 | model/03:101 | SE 旧段 3 句 ("Describes the actual Elements (blocks of time) experienced by each subject during the study." + 缺 "(see Section 5.1.1, …)" 的第 2 句 + 第 3 句) | R2 残留改写 (a013/a014 已补) | :121 PDF 句; "(blocks of time)" → D6 :125 |
| D-7 | model/03:99 | `**Structure:** One record per actual Element per subject` | PDF 表题含 "One Record per…" (S-MOD2 裁定) | :129 表题 |
| D-8 | model/03:127 | SJ 旧段 "Describes the actual order of repro stages …" | R2 残留改写 (a017/a018 已补) | :153 |
| D-9 | model/03:123 | `**Structure:** One record per Actual Repro Stage per Subject` | 同 D-7 | :157 表题 |
| D-10 | model/03:125 | `**Note:** Not for use with human clinical trials.` | 与 PDF a017 括注同义, 现已逐字承载 (R2 残留) | :153 "(not for use with human clinical trials)" |
| D-11 | model/03:148 | SV 旧段 "Describes the actual study visits experienced by each individual subject. …" | R2 残留改写 (a014/a015 已补) | :178 |
| D-12 | model/03:146 | `**Structure:** One record per actual or planned visit per subject` | 同 D-7 (且 "actual or planned" 与 PDF 表题 "per Subject Visit" 不同) | :184 表题 |
| D-13 | model/03:175 | SM 旧句 "Records the disease milestones experienced by each subject (e.g., …)." | R2 残留改写 (a002 已补); 例列表 → D6 :215 | :211 |
| D-14 | model/03:173 | `**Structure:** One record per Disease Milestone per subject` | 同 D-7 | :219 表题 |
| D-15 | model/04:7 尾 | "…specific AP rules:" (冒号版) | 由 PDF 句 "…AP rules, including:" 取代 | model/04:9 |
| D-16 | model/04:13 后半 | "APID was removed from Section 3.1.4 (Identifiers for All Classes) because APID is only allowed in AP domains. It is still listed in Section 3 as an identifier." | p6 §1.4 内容的跨文件改写副本, 且 "Section 3" 与 PDF p5/p8 "Section 4" 矛盾 (T-1) → D2, 留 PDF 所属 model/01:94 | model/04:21 交叉引用 |
| D-17 | model/04:15-18 | "Linking variables" 3 子项 (RSUBJID / RDEVID / SREL 释义) | KB 摘要与 PDF 表 Notes 重复 (同文件), 留 PDF 表 | model/04:21 交叉引用 + 表 :39-42 |
| D-18 | model/04:22 | Key Principles "AP domains conform to the same general observation class models (Interventions, Events, Findings) used for subject data" | 与 PDF 矛盾 (PDF: GOC 结构 **或 special-purpose 结构**), 且为 a002 改写 → D2 | model/04:9 PDF 原句 |
| D-19 | model/04:24 | Key Principles "Additional guidance for implementing AP domains is provided in … (SDTMIG-AP)" | R2 残留改写 (a008 已逐字补) | model/04:25 |
| D-20 | model/04:29 | "The table of variables used in Associated Persons Data includes all variables from the general observation classes, with the addition of AP-specific identifiers:" | 与 PDF 矛盾 (表只含 4 个附加标识变量; PDF 句为 "The variables in the following table are used in AP domains.") → D2 | model/04:33 PDF 段 |
| D-21 | model/04:34/36 Notes 格 | RSUBJID 缺第 3 句的旧格; SREL 简写格 ("…relationship to the subject or pool… If both are null…") | 列 = PDF Notes 单列, 恢复逐字 (B-model06 M-2b) | 同格 PDF 原文 |
| D-22 | model/03 4 格 + 汇总表 2 格 | C-1/C-2/C-3/C-5/C-6/C-7 旧值 | 与 PDF 矛盾 → D2 | 同格 PDF Notes 原文 |

### D6 标注清单 (本批新增; reviewer 逐条确认不矛盾)
| # | 位置 | 内容 | 不矛盾核查 |
|---|---|---|---|
| M-2 | model/01:124 | Mermaid 重绘说明 + PDF 图例 | 图例文字 = PDF 图内 2 条 |
| M-4 | model/01:180-185 | 5 子类例变量 | 逐个对 model/02 Role 列 (= PDF p12-39) 一致 |
| P-4 | model/03:17 | DM Structure "One record per subject" | PDF 表题无结构句; DM 每受试者 1 条, 与 p40 "1 standardized set of observations" 不冲突 |
| P-5 | model/03:23 | DM Notes 列说明 | 逐格见逐格表 (D2 3 格已改) |
| P-6 | model/03:68 | Key Reference Date 汇总表 | Description 列 8 格 = PDF Label 逐字; Typical Use: RFSTDTC "Usually first dose; basis for study day calculation" (PDF RFSTDTC Notes + DMDY Notes "reference start date is RFSTDTC") / RFXSTDTC / RFXENDTC / RFCSTDTC / RFCENDTC (= PDF Definition 简写) / RFICDTC "Consent date" 不矛盾; RFENDTC / RFPENDTC 已 D2 (C-6/C-7) |
| P-8 | model/03:89 | CO Structure + "free-text comments that are not a part of normal domain data" | PDF 无对应, 不冲突 (COVAL = The text of the comment) |
| P-12 | model/03:125 | Elements are blocks of time | 不冲突 |
| P-13/15/17/20 | model/03:131/159/186/221 | SE/SJ/SV/SM Notes 列说明 (按实际来源写: Notes 引/缩写, SE 含 C-code, SJ 含 Usage) | 逐格见逐格表 |
| P-19 | model/03:215 | SM 例: diagnosis, progression, relapse, remission | PDF 只给 "HYPOGLYCEMIC EVENT" 例; 列举不冲突 |
| A-4 | model/04:17-19 | AP prefix + APDM 例; APID 代替 USUBJID | PDF a006 "AP will be the prefix for the domain and dataset name"; a007 APID 必有 — 不冲突 |
| A-7 | model/04:27-29 | 同变量/角色/CT 适用; 非 core SDTMIG | PDF a009 "all other general assumptions … apply to AP data"; SDTMIG-AP 为独立 IG — 不冲突 |
- 未标 (导航): H1 / `Source:` 行; `## Overview`、各域 H2、`### Variables (N variables)`、`### Key Reference Date Variables`、`### AP Domain Rules` / `### Key Principles` / `### Variables Used in Associated Persons Data` 标题; model/04:21 交叉引用.

### PDF_TYPO
- 本段无新增 (T-1 见段 1; model/04 旧文 "Section 3" 已随 D-16 删除).

### census_items 处理 (model/03 7 张 + model/04 1 张, 均 C3 UNPARSEABLE)
| census (HEAD 行) | 改后行 | 方法 | 结果 |
|---|---|---|---|
| model/03:17 DM (#/Var/Label/Type/Role/Notes) | :25 (38 行) | bbox + 原子双抽取 + 渲染 p40-44 逐格 | 核心 190 格一致 (RPATHCD Label 改); Notes D2 3 格 + 词替换 4 格 |
| model/03:60 Key Reference Date (Variable/Description/Typical Use) | :70 (8 行) | 对 DM 表 PDF 行 (渲染 p40-41) | Description 8 格 = PDF Label; Typical Use D2 2 格, 其余不矛盾 → D6 (P-6) |
| model/03:79 CO | :95 (15 行) | 同上, 渲染 p44-45 | 核心 75 格一致 |
| model/03:105 SE | :133 (13 行) | 渲染 p46 | 核心 65 格一致 |
| model/03:131 SJ | :161 (10 行) | 渲染 p47 | 核心 50 格一致 |
| model/03:152 SV | :188 (16 行) | 渲染 p48 | 核心 80 格一致 (SVREASOC Label 改) |
| model/03:179 SM | :223 (10 行) | 渲染 p49 | 核心 50 格一致; MIDS Notes D2 |
| model/04:31 AP | :37 (4 行) | 渲染 p50 | 重建 (+#); 核心 20 格 + Notes 4 格 = PDF 逐字 |

### 逐格表 (改后每行一行; `python3 -I $S/celltab.py $S` 输出, 存 `$S/celltab.md`)
| 表 | KB 行 | # | Variable | PDF 页 | 核心格 (#/Var/Label/Type/Role) | Notes 格分类 | 本批处理 |
|---|---|---|---|---|---|---|---|
| DM | 27 | 1 | STUDYID | p40 | 一致 | 空 | — |
| DM | 28 | 2 | DOMAIN | p40 | 一致 | 逐字 (PDF Notes) | — |
| DM | 29 | 3 | USUBJID | p40 | 一致 | 空 | — |
| DM | 30 | 4 | SUBJID | p40 | 一致 | 逐字 (PDF Notes) | — |
| DM | 31 | 5 | RFSTDTC | p40 | 一致 | KB 简写 (= PDF Notes "Usually equivalent to … first exposed to study treatment") | — |
| DM | 32 | 6 | RFENDTC | p40-41 | 一致 | D2 已改 → PDF Notes 首句 (旧 "Usually date of last dose" 与 PDF "Usually … determined to have ended the trial" 矛盾) | Notes 改 |
| DM | 33 | 7 | RFXSTDTC | p41 | 一致 | 空 | — |
| DM | 34 | 8 | RFXENDTC | p41 | 一致 | 空 | — |
| DM | 35 | 9 | RFCSTDTC | p41 | 一致 | 空 | — |
| DM | 36 | 10 | RFCENDTC | p41 | 一致 | 空 | — |
| DM | 37 | 11 | RFICDTC | p41 | 一致 | 逐字 (PDF Usage) | — |
| DM | 38 | 12 | RFPENDTC | p41 | 一致 | 逐字 (PDF Usage) | — |
| DM | 39 | 13 | DTHDTC | p41 | 一致 | 逐字 (PDF Usage) | — |
| DM | 40 | 14 | DTHFL | p42 | 一致 | 部分逐字 (PDF Notes "Y" or null + Usage) | — |
| DM | 41 | 15 | SITEID | p42 | 一致 | 空 | — |
| DM | 42 | 16 | INVID | p42 | 一致 | 逐字 (PDF Usage) | — |
| DM | 43 | 17 | INVNAM | p42 | 一致 | 逐字 (PDF Usage) | — |
| DM | 44 | 18 | BRTHDTC | p42 | 一致 | 空 | — |
| DM | 45 | 19 | AGE | p42 | 一致 | D2 已改 → PDF Notes 原文 (旧 "Numeric age at RFSTDTC" 把 PDF Def "specific point in time defined for the trial" 限定为 RFSTDTC) | Notes 改 |
| DM | 46 | 20 | AGETXT | p42 | 一致 | KB 简写 + KB 例值 "18-25" (PDF 无例; Format number-number, 不矛盾) | — |
| DM | 47 | 21 | AGEU | p42 | 一致 | KB 自写例值 (PDF Examples 空; 不矛盾) | — |
| DM | 48 | 22 | SEX | p42 | 一致 | KB 自写 (不矛盾) | — |
| DM | 49 | 23 | RACE | p42 | 一致 | 逐字 (PDF Usage) | — |
| DM | 50 | 24 | ETHNIC | p42 | 一致 | 逐字 (PDF Usage) | — |
| DM | 51 | 25 | SPECIES | p42 | 一致 | Usage 原词 (词替换已恢复: Not for → Not in) | Notes 改 |
| DM | 52 | 26 | STRAIN | p42-43 | 一致 | Usage 原词 (同上) | — |
| DM | 53 | 27 | SBSTRAIN | p43 | 一致 | Usage 原词 (同上) | — |
| DM | 54 | 28 | ARMCD | p43 | 一致 | KB 自写 (不矛盾; PDF Notes "Limited to 20 characters.") | — |
| DM | 55 | 29 | ARM | p43 | 一致 | 空 | — |
| DM | 56 | 30 | ACTARMCD | p43 | 一致 | 逐字 (PDF Usage) | — |
| DM | 57 | 31 | ACTARM | p43 | 一致 | 逐字 (PDF Usage) | — |
| DM | 58 | 32 | ARMNRS | p43 | 一致 | D2 已改 → PDF Notes 首句 (旧 "When arm assignment is not possible" 与 PDF 例值 NOT TREATED / UNPLANNED TREATMENT 矛盾) | Notes 改 |
| DM | 59 | 33 | ACTARMUD | p43 | 一致 | 空 | — |
| DM | 60 | 34 | SETCD | p43 | 一致 | KB 自写, 无 PDF 依据 ("Use with extreme caution"; PDF Usage 空) — 不矛盾, 留 D6 下 (见 需主控定 M-2) | — |
| DM | 61 | 35 | RPATHCD | p43 | 一致 | Usage 原词 (同上) | Label 改为 PDF |
| DM | 62 | 36 | COUNTRY | p43 | 一致 | Format + Usage 逐字 | — |
| DM | 63 | 37 | DMDTC | p43-44 | 一致 | 空 | — |
| DM | 64 | 38 | DMDY | p44 | 一致 | 空 | — |
| CO | 97 | 1 | STUDYID | p44 | 一致 | (无 Notes 列) | — |
| CO | 98 | 2 | DOMAIN | p44 | 一致 | (无 Notes 列) | — |
| CO | 99 | 3 | RDOMAIN | p44 | 一致 | (无 Notes 列) | — |
| CO | 100 | 4 | USUBJID | p44 | 一致 | (无 Notes 列) | — |
| CO | 101 | 5 | POOLID | p44 | 一致 | (无 Notes 列) | — |
| CO | 102 | 6 | SPDEVID | p44 | 一致 | (无 Notes 列) | — |
| CO | 103 | 7 | COSEQ | p44 | 一致 | (无 Notes 列) | — |
| CO | 104 | 8 | IDVAR | p44-45 | 一致 | (无 Notes 列) | — |
| CO | 105 | 9 | IDVARVAL | p45 | 一致 | (无 Notes 列) | — |
| CO | 106 | 10 | COREF | p45 | 一致 | (无 Notes 列) | — |
| CO | 107 | 11 | COVAL | p45 | 一致 | (无 Notes 列) | — |
| CO | 108 | 12 | COEVAL | p45 | 一致 | (无 Notes 列) | — |
| CO | 109 | 13 | COEVALID | p45 | 一致 | (无 Notes 列) | — |
| CO | 110 | 14 | CODTC | p45 | 一致 | (无 Notes 列) | — |
| CO | 111 | 15 | CODY | p45 | 一致 | (无 Notes 列) | — |
| SE | 135 | 1 | STUDYID | p46 | 一致 | 空 | — |
| SE | 136 | 2 | DOMAIN | p46 | 一致 | 逐字 (PDF Notes "must be "SE"") | — |
| SE | 137 | 3 | USUBJID | p46 | 一致 | 空 | — |
| SE | 138 | 4 | SESEQ | p46 | 一致 | 空 | — |
| SE | 139 | 5 | ETCD | p46 | 一致 | KB 自写 (不矛盾: ETCD 值来自 TE) | — |
| SE | 140 | 6 | ELEMENT | p46 | 一致 | 空 | — |
| SE | 141 | 7 | TAETORD | p46 | 一致 | = PDF Variable C-code | — |
| SE | 142 | 8 | EPOCH | p46 | 一致 | = PDF Variable C-code | — |
| SE | 143 | 9 | SESTDTC | p46 | 一致 | 空 | — |
| SE | 144 | 10 | SEENDTC | p46 | 一致 | 空 | — |
| SE | 145 | 11 | SESTDY | p46 | 一致 | 空 | — |
| SE | 146 | 12 | SEENDY | p46 | 一致 | 空 | — |
| SE | 147 | 13 | SEUPDES | p46 | 一致 | KB 简写 (PDF Notes "Used only if ETCD has the value of …") | — |
| SJ | 163 | 1 | STUDYID | p47 | 一致 | 空 | — |
| SJ | 164 | 2 | DOMAIN | p47 | 一致 | 逐字 (PDF Notes) | — |
| SJ | 165 | 3 | USUBJID | p47 | 一致 | 空 | — |
| SJ | 166 | 4 | SJSEQ | p47 | 一致 | 逐字 (PDF Usage) | — |
| SJ | 167 | 5 | RSTGCD | p47 | 一致 | 逐字 (PDF Usage) | — |
| SJ | 168 | 6 | RSTAGE | p47 | 一致 | 逐字 (PDF Usage) | — |
| SJ | 169 | 7 | SJSTDTC | p47 | 一致 | 逐字 (PDF Usage) | — |
| SJ | 170 | 8 | SJENDTC | p47 | 一致 | 逐字 (PDF Usage) | — |
| SJ | 171 | 9 | RPHASE | p47 | 一致 | 逐字 (PDF Usage) | — |
| SJ | 172 | 10 | SJUPDES | p47 | 一致 | 逐字 (PDF Usage) | — |
| SV | 190 | 1 | STUDYID | p48 | 一致 | 空 | — |
| SV | 191 | 2 | DOMAIN | p48 | 一致 | 逐字 (PDF Notes) | — |
| SV | 192 | 3 | USUBJID | p48 | 一致 | 空 | — |
| SV | 193 | 4 | VISITNUM | p48 | 一致 | 空 | — |
| SV | 194 | 5 | VISIT | p48 | 一致 | 空 | — |
| SV | 195 | 6 | SVPRESP | p48 | 一致 | 空 | — |
| SV | 196 | 7 | SVOCCUR | p48 | 一致 | 空 | — |
| SV | 197 | 8 | SVREASOC | p48 | 一致 | 空 | Label 改为 PDF |
| SV | 198 | 9 | SVCNTMOD | p48 | 一致 | 空 | — |
| SV | 199 | 10 | SVEPCHGI | p48 | 一致 | 空 | — |
| SV | 200 | 11 | VISITDY | p48 | 一致 | 空 | — |
| SV | 201 | 12 | SVSTDTC | p48 | 一致 | 空 | — |
| SV | 202 | 13 | SVENDTC | p48 | 一致 | 空 | — |
| SV | 203 | 14 | SVSTDY | p48 | 一致 | 空 | — |
| SV | 204 | 15 | SVENDY | p48 | 一致 | 空 | — |
| SV | 205 | 16 | SVUPDES | p48 | 一致 | 空 | — |
| SM | 225 | 1 | STUDYID | p49 | 一致 | 空 | — |
| SM | 226 | 2 | DOMAIN | p49 | 一致 | 逐字 (PDF Notes) | — |
| SM | 227 | 3 | USUBJID | p49 | 一致 | 空 | — |
| SM | 228 | 4 | SMSEQ | p49 | 一致 | 空 | — |
| SM | 229 | 5 | MIDS | p49 | 一致 | D2 已改 → PDF Notes 原文 (旧 "Unique name linking to TM" 与 PDF 不符: 链 TM 的是 MIDSTYPE) | Notes 改 |
| SM | 230 | 6 | MIDSTYPE | p49 | 一致 | KB 自写 (不矛盾) | — |
| SM | 231 | 7 | SMSTDTC | p49 | 一致 | 空 | — |
| SM | 232 | 8 | SMENDTC | p49 | 一致 | 空 | — |
| SM | 233 | 9 | SMSTDY | p49 | 一致 | 空 | — |
| SM | 234 | 10 | SMENDY | p49 | 一致 | 空 | — |
| AP | 39 | 1 | APID | p50 | 一致 | 逐字 (PDF Notes) | 表重建 (+# 列, Notes 恢复 PDF 原文) |
| AP | 40 | 2 | RSUBJID | p50 | 一致 | 逐字 (PDF Notes) | 表重建 (+# 列, Notes 恢复 PDF 原文) |
| AP | 41 | 3 | RDEVID | p50 | 一致 | 逐字 (PDF Notes) | 表重建 (+# 列, Notes 恢复 PDF 原文) |
| AP | 42 | 4 | SREL | p50 | 一致 | 逐字 (PDF Notes) | 表重建 (+# 列, Notes 恢复 PDF 原文) |
- 分类计数 (106 行): 空 44 / 逐字 26 (+部分逐字 1) / Usage 原词恢复 4 / Format+Usage 逐字 1 / = PDF C-code 2 / KB 简写或自写不矛盾 9 (其中无 PDF 依据 1 = SETCD) / D2 已改 4 / 无 Notes 列 (CO) 15.

### 需主控定 (本 attempt 已按默认处理, 可回退)
- **M-1 Key Reference Date Variables 表 (model/03:66-79)**: PDF 无此表; 内容 = DM 表 8 个参考日期变量的 Label + KB "Typical Use". 本 attempt 默认 D6 保留 (P-6) 并 D2 改 2 格矛盾值 (C-6/C-7). 备选 = 按 "KB 自写摘要与 PDF 内容重复 → 交叉引用" 整表删并改一行指向上方 DM 表.
- **M-2 DM SETCD Notes "Use with extreme caution"** (model/03:60): PDF Usage 空, Notes 为 "Defined by the sponsor (see Section 5.1.2, Trial Sets). Maximum of 8 characters. …", 无此警示. 判为无依据但不矛盾 → 留 D6 下 (同 S-MOD2 M-1b 8 格处理). 备选 = 改为 PDF Notes 原文.
- **M-3 model/04 `### AP Domain Rules` / `### Key Principles` 两节**: 余下内容全为 D6 (2 + 2 条) + 1 行交叉引用; 标题按规则 6 保留. 若主控认为这两个 KB 标题下已无 PDF 内容可承载, 可删 `### AP Domain Rules` 标题 (无入站锚点; `grep -rn "04_associated_persons.md#"` 仓内 knowledge_base/web 无命中).
- **M-4 标题层级**: model/03 PDF 编号标题按 S-MOD3 (model/05) 补为 H3 挂在既有 KB H2 下, §3.2.3 父节为 H2. model/02 在 HEAD 已是编号 H2 (`## 3 Study Subject Data`, 无 `## Overview`). 由此产生 KB H2 + PDF H3 同义对 (最明显 `## Subject Repro Stages` → `### 3.2.3.2 Subject Repro Stages`; 另 DM/CO/SE/SV/SM 与 model/04 `## Overview` → `### 4 …`): 若主控按 S-TDM 冗余标题口径处理 (无入站锚点即删 KB 标题, 本 3 文件仓内无 `#` 锚点入站), 可删 KB H2 并把 PDF 标题升为 H2; 本批未做.

- **M-5 D2 改格 C-1..C-7 (7 格) 可回退 D6**: 判矛盾依据 — C-1/C-6 RFENDTC: PDF Notes "Usually equivalent to … determined to have ended the trial", last exposure 仅 "Often" 之一, 与 KB "Usually … last dose" 直接冲突; C-3 ARMNRS: PDF 例值 "NOT TREATED" / "UNPLANNED TREATMENT" 是已分配 arm 的情形, 与 KB "When arm assignment is not possible" 冲突; C-5 MIDS: sv20 p58 TM 表为 "One Record per Disease Milestone Type", 以 MIDSTYPE 为 Topic, 不含 MIDS, 与 KB "linking to TM" 冲突; C-2 AGE (把 PDF Def "a specific point in time defined for the trial" 限定为 RFSTDTC) 与 C-7 RFPENDTC ("Completion/withdrawal date" vs PDF "last known date of contact") 属收窄/偏义, 非字面冲突 — 主控若只认字面冲突, C-2/C-7 回退为原 KB 值留 D6 下.

### 范围外发现
- O-a (证据侧, 非 KB): `work/pdf_atoms.jsonl` 原子 sv20_p0050_a016-a019 把 AP 表 Notes 文字放在 Definition 列 (渲染 p50 为 Notes 列); 不影响 KB, 仅提示 reviewer 勿以原子列位为准.
- 无其他 (未碰批外文件; `git diff --stat` 中 model/05 为并行批 S-MOD3 改动).

### 验证 (S = scratchpad/t2s_S-MOD1_writer, 均在改后运行, 工作目录 repo 根)
- `python3 -I $S/scan.py knowledge_base/model/01_concepts_and_terms.md 4 10 | tail -1` → `HIT 132 MISS 2` (a020 T-1 / a010 FIGURE)
- `python3 -I $S/scan.py knowledge_base/model/03_special_purpose_domains.md 40 49 | tail -1` → `HIT 41 MISS 0`
- `python3 -I $S/scan.py knowledge_base/model/04_associated_persons.md 50 50 | tail -1` → `HIT 16 MISS 0`
- `python3 -I $S/rscan.py knowledge_base/model/0X_….md <lo> <hi>` → model/01 `HIT 161 NOPDF 20`; model/03 `HIT 44 NOPDF 34`; model/04 `HIT 18 NOPDF 16` (NOPDF 全为 H1/Source/导航标题/D6/交叉引用/PDF 折行, 见上)
- `python3 -I $S/tbl.py $S/pdf_tabs.json && python3 -I $S/cmp.py $S | tail -1` → `cells 530 diffs 0`
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`
- md5 改后: model/01 `0a4855b8fd85e1c44974c1266b9362ec` (209 行) / model/03 `26d0e4d591903315ee09157488972b8e` (234 行) / model/04 `d2069187643d961bbde102a1b3aa39ad` (44 行)

### git diff --stat
```
 knowledge_base/model/01_concepts_and_terms.md      | 61 +++++++-------
 knowledge_base/model/03_special_purpose_domains.md | 96 ++++++++++++++++------
 knowledge_base/model/04_associated_persons.md      | 44 +++++-----
 3 files changed, 127 insertions(+), 74 deletions(-)
```

### 汇总
- 改动 44 条 (model/01 5 含 1 VERIFIED; model/03 29 = P-1..P-20 + V-1/V-2 + C-1..C-7; model/04 A-1..A-10 = 10; jsonl 按原子拆 76 行) [trace 行 note 写 "改动 47" 为计数笔误, 以此为准]; 结构改动 8 (S-1..S-8); 删除 22 条 (D-1..D-22); D6 新增 14 处; PDF_TYPO 1 (T-1 沿用); 范围外 1 (证据侧); 需主控定 4 (M-1..M-4).

### attempt 1 补充 (同 attempt, 交付前自查)
- model/03:159 SJ Notes 列 D6 措辞改为 "the other non-blank cells quote the PDF Usage Restrictions column" (STUDYID/USUBJID 格为空, 原措辞不属实). md5 → `26d0e4d591903315ee09157488972b8e` (234 行, 上文验证段已更新).
- 复跑: scan model/03 `HIT 41 MISS 0`; rscan `HIT 44 NOPDF 34`; cmp `cells 530 diffs 0`; check_links `live docs: 42`; diff --stat 不变 (`3 files changed, 127 insertions(+), 74 deletions(-)`).
- 补渲染 p9 (census :176 列表核), 见 census_items 段; 新增 需主控定 M-5 (D2 7 格判据与可回退项), M-4 补 S-TDM 冗余标题选项.

## attempt 1 delta (主控裁定 M-1 / M-2 / M-4 / M-5, 2026-11-26)
- md5 model/03 `26d0e4d5…` → `a7ee1b7a9a129d70e97d7178d2f5c7c2` (234 → 222 行); model/01 / model/04 未动.

### M-1 确认: Key Reference Date 汇总表 = D6 保留 (非完全重复)
- 该表不与 PDF 任何表完全重复: Description 列 8 格 = PDF DM 表 Variable Label 逐字, 但 Typical Use 列为 KB 写, PDF 无此列 (PDF Definition/Notes 文字不同), 且 PDF 无 "参考日期变量" 子表. → 不属 "完全重复 → D2 交叉引用", 维持 D6 (P-6).
- 逐格不矛盾核 (改后): RFSTDTC "Usually first dose; basis for study day calculation" (p40 Notes "Usually equivalent to … first exposed to study treatment"; p44 DMDY Notes "reference start date is RFSTDTC") / RFENDTC = PDF Notes 首句 (C-6) / RFXSTDTC "First exposure to study treatment" / RFXENDTC "Last exposure …" (p41 Definition) / RFCSTDTC / RFCENDTC "First/Last exposure to challenge agent" (p41 Notes) / RFICDTC "Consent date" (p41 Definition) / RFPENDTC = PDF Notes (C-7). 8 格均不矛盾.

### M-2: SETCD 留 D6 下, 不改. M-5: C-2 / C-7 保留 D2 改正, 不回退.

### M-4 执行 (S-TDM 冗余标题条)
入站链接核: `for f in 03_special_purpose_domains 04_associated_persons; do grep -rn "$f.md#\|$f#" knowledge_base web/src tools docs; done` → 0 命中; 锚点 slug grep (`demographics-dm|comments-co|subject-elements-se|subject-visits-sv|subject-disease-milestones-sm|subject-repro-stages|ap-domain-rules|key-principles`) 同范围 → 0 命中.
| # | 原位置 (delta 前) | KB 标题 | 紧邻 PDF 标题 | 判定 | 处理 |
|---|---|---|---|---|---|
| D-23 | model/03:11 | `## Demographics (DM)` | `### 3.2.1 Demographics` | 同义, 0 入站 | 删 KB 标题行; PDF 标题升 H2 `## 3.2.1 Demographics` (本 attempt 新插标题, 非既有锚点) |
| D-24 | model/03:81 | `## Comments (CO)` | `### 3.2.2 Comments` | 同义, 0 入站 | 删; PDF 标题升 H2 |
| D-25 | model/03:117 | `## Subject Elements (SE)` | `### 3.2.3.1 Subject Elements` | 同义, 0 入站 | 删; PDF 标题留 H3 (挂 `## 3.2.3`, 与 PDF 层级一致) |
| D-26 | model/03:149 | `## Subject Repro Stages` | `### 3.2.3.2 Subject Repro Stages` | 同义, 0 入站 | 删; 留 H3 |
| D-27 | model/03:174 | `## Subject Visits (SV)` | `### 3.2.3.3 Subject Visits` | 同义, 0 入站 | 删; 留 H3 |
| D-28 | model/03:207 | `## Subject Disease Milestones (SM)` | `### 3.2.3.4 Subject Disease Milestones` | 同义, 0 入站 | 删; 留 H3 |
| K-1 | model/03:5 / model/04:5 | `## Overview` | `### 3.2 Special-purpose Domains` / `### 4 Associated Persons Data` | 非同义 (通用导航词) | 保留, 报告 |
| K-2 | model/04:15 / :23 | `### AP Domain Rules` / `### Key Principles` | 无紧邻 PDF 标题 (下接 D6 / PDF 段) | 不满足 "与紧邻 PDF 原标题同义" | 保留, 报告 (0 入站, 主控若要删可直接删) |
- 内容行一律未动. 改后标题结构: `## Overview` > `### 3.2`; `## 3.2.1` / `## 3.2.2` / `## 3.2.3` > `### 3.2.3.1-4`; 各 `### Variables (N variables)` / `### Key Reference Date Variables` 保留 (规则 6).

### 复跑 (S = scratchpad/t2s_S-MOD1_writer)
- scan model/03 `HIT 41 MISS 0`; rscan `HIT 42 NOPDF 30` (少 4 个 KB 导航 H2 段; SE/SJ 等 H2 无标点不被 rscan 拆出者计入 HIT); cmp `cells 530 diffs 0`; `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42`
- `git diff --stat -- knowledge_base/model/0[134]*.md` → `3 files changed, 121 insertions(+), 80 deletions(-)`
- 改后 model/03 行号整体前移 (D-23..D-28 删 6 标题行 + 6 空行); 上文变更清单 / 逐格表行号为 delta 前值, 以内容定位.

## attempt 2 (reviewer F-1, 2026-11-26)
- model/03:125 SE Notes 列 D6 照 review F-1 原文替换: "most cells quote or condense the PDF Notes column" → "the DOMAIN and SEUPDES cells quote or condense the PDF Notes column" (其余不动). 核: SE Notes 非空 5 格 = DOMAIN / SEUPDES (PDF Notes) + TAETORD / EPOCH (C-code) + ETCD (KB); 其余 8 格空 → 新句属实, 无需再改.
- md5 model/03 `a7ee1b7a…` → `df5c9199aa3f4a754cfe7bbc855be7c7` (222 行); model/01 / model/04 未动.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`
