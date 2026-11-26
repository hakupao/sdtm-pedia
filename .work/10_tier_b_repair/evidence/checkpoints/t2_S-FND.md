# T2S S-FND writer checkpoint (扫描批: EG / OE / UR / PE / SS + DA §6.3 引言)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `056d8cc`; 本批 18 文件改前对 HEAD 干净 (`git status --short knowledge_base/domains/{EG,OE,UR,PE,SS,DA}` 空). 其他域的工作区改动 (AG/EC/EX/PR …) 属并行批, 未触碰.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-FND_writer/`
  (base/ = `git show HEAD:` 副本; kbbase/ = `git archive HEAD`; apply_fnd.py 精确替换 + 命中次数断言; spec_cmp.py (原子) + speccmp_bbox.py (`pdftotext -bbox` 词框分列) 两法逐变量逐字段;
  scan.py PDF→KB; rscan.py KB→PDF; census_before/after.json; fp_before/after.jsonl; 渲染 p180 顶部, p186/299/313/316/343 左半 (CT 列), p302/303/304/305/192 整页, p316 PEORRES 局部)
- md5 before → after (前 8 位): DA/assumptions `79a8536a`→`cbed1029` (22→26 行); EG/assumptions `cfe168a0`→`132c1460` (32→36); EG/spec `d914ea8d`→`10a42421` (431→433);
  OE/assumptions `0536f847`→`58fb55cd` (7→17); OE/spec `99736a4c`→`7f72bab2` (501→503); UR/assumptions `913a2a49`→`75a66455` (3→13); UR/spec `f8398b19`→`8324030c` (417→419);
  PE/assumptions `e5178219`→`10489294` (31→39); PE/spec `889b7d8a`→`d4cc1f33` (296→298); SS/assumptions `c4d51730`→`a8102f94` (10→20); SS/examples `f0ed4f7b`→`ccde0a8c` (13→15); SS/spec `faad87ed`→`092786f8` (224→226).
  未动: EG/examples, OE/examples, UR/examples, PE/examples, DA/examples, DA/spec.

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| domains/EG | §6.3.3 | 185-193 | **185-192** | p185 上部 dd.xpt / ds.xpt / relrec.xpt + 叙述属 §6.3.2 DD Ex2 (a001-a017), 标题 a018 起; p192 止于 Ex4 eg.xpt; **p193 首行即 `6.3.4 Inclusion/Exclusion Criteria Not Met (IE)`** → p193 无 EG 内容. json `pdf_ranges` hi=193 供 reviewer 用时注意 |
| domains/OE | §6.3.7.5 | 298-305 | **298-305** | p298 上部 NV Ex2 (nv.xpt + 叙述) 属 §6.3.7.4, 标题 a023 起 (页底仅标题 + Description); p305 上部 Ex4 suppoe/ae 属 OE, 中部 `6.3.7.6 Reproductive System Findings (RP)` 起别节 |
| domains/UR | §6.3.7.8 | 312-315 | **312-315** | p312 上部 RE Ex2 (suppre/di) 属 §6.3.7.7, 标题 a011 起; p315 上部 UR Ex1/Ex2 表属 UR, 中部 `6.3.8 Physical Examination (PE)` 起别节 |
| domains/PE | §6.3.8 | 315-318 | **315-318** | p315 上部 UR 表别节; p318 下部 `6.3.9 Questionnaires, Ratings, and Scales (QRS) …` 起别节 |
| domains/SS | §6.3.11 | 342-344 | **342-344** | p342 上部 SC Ex2/Ex3 属 §6.3.10; p344 下部 `6.3.12 Tumor/Lesion Domains` 起别节 |
| DA (narrow) | §6.3 引言 | p180 | **p180 顶部** | `6.3 Models for Findings Domains` 标题 + 1 句 (以冒号结尾), 其后直接 `6.3.1` (渲染确认 **PDF 冒号后无域列表**, 与 §6.2 不同; 不按 §6.2 类比补列表) |

### 双向全扫 — 逐页日志
方法: PDF→KB = `work/pdf_atoms.jsonl` 该页本域全部原子 (含 TABLE_ROW/TABLE_HEADER/CODE_LITERAL/NOTE) 归一后在本域三文件查 (scan.py), 未命中逐条分类; spec 表行以 **speccmp_bbox.py (词框分列, 逐变量逐字段)** 为准, 原子 spec_cmp.py 辅助 (原子在 p186/p300/p301 抽取错多). KB→PDF = assumptions/examples 逐句 (rscan.py) 在 layout 文本+原子中查; spec.md 用两法逐字段. 计数 = 改后 "本域原子数 / 命中 / 本次补齐".

| 页 | 节 | PDF→KB: 原子 / 命中 / 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 (未命中分类) |
|---|---|---|---|---|---|
| 180 | §6.3 引言 (narrow) | 2 / 2 / 2→2 | DA/asm:3-5 | — | 只做 json 指定一项; DA 其余未动 |
| 185 | §6.3.3 标题/Desc/Spec 首句/spec | 13 / 11 / 2→2 (Spec 标题 + 首句) | EG/asm 1-9 有出处; spec STUDYID..EGREFID 逐字段一致 | bbox 逐字段 | 未命中: a018 节号标题 (= H1 结构等价), a023 表头 (= spec 字段结构). DOMAIN CT `EG`/空 = U6 (S-CT) |
| 186 | spec | 15 / 5 / 2→2 (CT `*` ×2) | 一致 | bbox + 渲染 (CT 列) | 未命中: 表头; CT C-code 8 格 (U5); 原子抽取错 EGORRES (原子缺 "or QT PROLONGATION", layout/bbox 有), EGSTRESC (原子去掉 `"beats/min" .` 的空格), EGSTRESN (原子 "For" / PDF "Used for") |
| 187 | spec | 21 / 11 / 0 | 一致 | bbox | 未命中: 表头 + C-code 9 格 (U5); EGXFN/EGSPID 为页首行, bbox 漏取, 已人工对 layout 逐字段一致 |
| 188 | spec 尾 / 脚注 / asm 1-10a | 18 / 16 / 1→1 (脚注) | 一致 | bbox (EGELTM 页首行 bbox 漏, 人工逐字段一致) | 未命中: 表头; 脚注原子 "1In" 数字上标 → 已按 ¹ 补 (S-EVT 同) |
| 189 | asm 10b-11 / Ex1 叙述 | 12 / 12 / 0 | 一致 | — | |
| 190 | Ex1-Ex3 | 32 / 20 / 0 | 一致 | census Ex1/Ex2/Ex3 OK | 12 未命中 = 原子抽取错 (B-EG 已核: EGXFN "P0W…", VISIT 漏 "1", a027 漏 "10-second"; Ex1 由 B-EG 按 300dpi 渲染重建). 本次未重渲染 p190, 以 census OK 为据 |
| 191 | Ex3 | 30 / 30 / 0 | 一致 | census OK | |
| 192 | Ex4 | 10 / 7 / 0 | 一致 | census OK + 渲染整页 | 未命中: a002 表头原子, a006/a009 原子 "Single Beat Measurement" (渲染 "Single Measurement" = KB) |
| 298 | §6.3.7.5 标题 / Desc | 3 / 2 / 2→2 | OE/asm:3-5 | — | a023 节号标题 = H1 结构; NV 叙述/表别节 |
| 299 | Spec 首句 / spec | 25 / 19 / 5→5 (Spec 标题+首句, CT `*` ×3) | 一致 | bbox + 渲染 | 未命中: 表头, C-code 4 格 (U5), DOMAIN `OE` (U6); a010 OEGRPID 原子漏 "within a subject" (layout 有 = KB) |
| 300 | spec | 22 / 9 / 0 | 一致 | bbox | 未命中: C-code 12 格 (U5); a017 原子 "OEVALID" (PDF OEEVALID) 抽取错 |
| 301 | spec 尾 / 脚注 / asm / Ex1 叙述 | 18 / 8 / 1→1 (脚注) + A 标题 | OE/asm 13-17 一致 (asm 3 仅 "-- FAST" 断行) | bbox | 未命中: EPOCH C-code; 原子抽取错 a001/a005/a007/a008/a009 (TAETORD/OETPT/OEELTM/OETPTREF/OERFTDTC, layout+bbox = KB), a011-a013 (asm 原子乱码, layout = KB), a017/a018 (B-OE 已登记); 脚注 ¹ 写法 |
| 302 | Ex1-Ex2 | 29 / 26 / 0 | 一致 | census OK + 渲染整页 | 未命中: a005 原子 "OEEEXAM" (渲染 OEEXAM), a026/a027 原子 "HYPEREMIA" (渲染 HYPERMIA = KB) |
| 303 | Ex2 supp / Ex3 | 31 / 27 / 0 | 一致 | census OK + 渲染 | 未命中 a028-a031: pr.xpt 原子漏列/错值 (渲染 = KB, census OK) |
| 304 | Ex3 pr/di/relrec / Ex4 | 29 / 19 / 0 | 一致 | census_items 渲染逐格 (下) | 未命中: T-1/T-2 (a012, a026-a029), a020-a023 原子 "installation" (渲染 instillation = KB), a001 pr r5 / a005 di 表头 "DISEG" 原子错 |
| 305 | Ex4 supp/ae | 10 / 7 / 0 | 一致 | census OK + 渲染 | 未命中: a004/a007/a008 原子错 (渲染 = KB); RP 起别节 |
| 312 | §6.3.7.8 / Desc / Spec 首句 / spec | 17 / 14 / 4→4 | UR/asm:3-9 | bbox | 未命中: 节号标题 (H1 结构), 表头, DOMAIN `UR` (U6). Spec 首句 "per per" 照录 → U-1 |
| 313 | spec | 24 / 11 / 3→3 (CT `*` ×3) | 一致 | bbox + 渲染 | 未命中: C-code 13 格 (U5) |
| 314 | spec 尾 / 脚注 / asm / Ex1 叙述 | 21 / 19 / 1→1 (脚注) + A 标题 | 一致 | bbox | 未命中: EPOCH C-code; 脚注 ¹ 写法 |
| 315 | UR 表 / §6.3.8 / PE 前言 / Desc | UR 14/14/0; PE 12 / 12 / 2→2 | PE/asm 1-25 有出处 | census UR Ex1/Ex2 OK | PE CDASH 段 KB 拆成 6 段 (PDF 1 段), 文字逐字一致, 仅排版, 未动 |
| 316 | Spec 首句 / spec | 24 / 16 / 5→5 (Spec 标题+首句, CT `*` ×4) | 一致 (PELAT 改 T-1) | bbox + 渲染 (CT 列; PEORRES 局部) | 未命中: 表头, C-code 6 格 (U5), DOMAIN (U6); a017 PEORRES 原子 "should be NOT DONE" 抽取错 (渲染 "should be null" = KB); a015 PESCAT "–CAT" 仅排版 (S-TYPO); a023 PELAT 原子自带正确拼写 |
| 317 | spec 尾 / 脚注 / asm | 17 / 12 / 1→1 (脚注) | 一致 | bbox | 未命中: C-code 4 格 (U5); 脚注 ¹ 写法 |
| 318 | Ex1 | 13 / 13 / 0 | 一致 | census OK | QRS 起别节 |
| 342 | §6.3.11 / Desc / Spec 首句 / spec | 8 / 6 / 4→4 | SS/asm:3-9 | bbox | 未命中: 节号标题, DOMAIN `SS` (U6); SC Ex2/Ex3 别节 |
| 343 | spec / 脚注 / asm 1 | 23 / 16 / 2→2 (CT `*` ×2) + 脚注 + A 标题 | 一致 | bbox + 渲染 (CT 列 + 脚注) | 未命中: C-code 6 格 (U5); 脚注 ¹ 写法 |
| 344 | asm 2-4 / Ex1 | 14 / 14 / 1→1 (ss.xpt 标签) | 一致 | census OK | TU 起别节 |

- spec.md 非变量行 (KB→PDF): H1、`> Class: … | Structure: …`、`---`、`## Cross References` 块 → U8 导航, 不标 D6.
- KB→PDF (rscan.py, 改后): EG/UR/PE/SS 0 行无出处; OE 1 行 = asm 3 PDF 断行 "-- FAST" (非差异).
- 汇总已补 (原子/格计): DA 2, EG 5 (Spec 标题+句 2, CT 2, 脚注 1), OE 9 (D 2, S 2, A 1, CT 3, 脚注 1), UR 9 (同 OE), PE 9 (D 2, S 2, CT 4, 脚注 1) + T-1, SS 9 (D 2, S 2, A 1, CT 2, 脚注 1, ss.xpt 1). 余下未命中全部为: 别节 / 结构等价 (节号标题、表头) / 原子抽取错 / 已登记 T-n / U5 C-code / U6 DOMAIN / 脚注上标写法.

### spec.md Controlled Terms 逐变量 (bbox 分列 + layout `Char *` grep + 渲染 CT 列三法)
- `*` 格: PDF 14 = KB 改后 14 (EG: EGCAT EGSCAT; OE: OETSTDTL OECAT OESCAT; UR: URTSTDTL URCAT URSCAT; PE: PETESTCD PETEST PECAT PESCAT; SS: SSCAT SSSCAT). 其余 spec 页 (185/187/188/300/301/312/314/317/342) layout grep 与 bbox 均 0 个 `*`.
- 非 CT 字段 (Label/Type/Role/Core/CDISC Notes): EG 40+4 (页首行 STUDYID/EGSPID/EGXFN/EGELTM 人工) / OE 52 / UR 43 / PE 30 / SS 22 变量全一致, 唯一差异 PELAT Notes (T-1, 已改). 变量顺序全同.
- U6 (S-CT, 未改): DOMAIN ×5. U5 (S-CT, 未改): EG 19 / OE 22 / UR 18 / PE 10 / SS 8 格 C-code vs PDF 括号短名.

### census_items 逐格 (渲染 p304 110dpi; T-2 依据 p305 100dpi)
| 表 | 行 | 结果 |
|---|---|---|
| OE/examples.md:121-124 relrec.xpt (Ex3) | 表头 | 8 列: 仅 col6 PDF `IDVARAL` / KB `IDVARVAL` = **T-1 沿用** (RELREC 标准变量名; 同文件 supp 表头均 IDVARVAL) |
| | r1 | XYZ / PR / 空 / PRLNKID / 空 / ONE / 13 — 一致 |
| | r2 | XYZ / OE / 空 / OELNKID / 空 / MANY / 13 — 一致 |
| OE/examples.md:140-145 oe.xpt (Ex4) | 表头 | 21 列一致 |
| | r1 | 除 OECAT (PDF OCCULAR COMFORT / KB OCULAR, **T-2 沿用**) 外 20 格一致 (OD, OESEQ 1, EYDCOMGR, 1/1/1, RIGHT, …T09:00, UPON INSTILLATION, 1) |
| | r2 | 同上, 仅 OECAT T-2 (OD, 2, 10/10/10, …T09:01, 1 MINUTE POST-INSTILLATION, 2) |
| | r3 | 同上, 仅 OECAT T-2 (OS, OESEQ 1 = PDF, U-1 沿用; LEFT; 2011-05-01T09:00) |
| | r4 | 同上, 仅 OECAT T-2 (OS, 2, 10/10/10, …T09:01) |
- T-2 依据复核: p305 suppoe IDVAR=OECAT 的 IDVARVAL = "OCULAR COMFORT" (渲染确认).
- table_census.py (本批 manifest, hi 已按 O20 改): before = after `KB tables 20 / OK 18 / DIFF 2, cells 2136, diffs 5` (= OE T-1 1 + T-2 4). 本批页内 PDF_ONLY 7 张 (p185 dd/ds/relrec §6.3.2; p298 nv §6.3.7.4; p312 suppre/di §6.3.7.7; p342 sc §6.3.10) 均别节. SS 表改后 census `ds` 由 None → ss.xpt.

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | DA/assumptions.md:3-5 | ig34_p0180_a0001/a0002 | INSERTED | H1 后 `## §6.3 Models for Findings Domains` + 引言句 (U3/O39) | 180 |
| 2 | EG/assumptions.md:7-9 | ig34_p0185_a021/a022 | INSERTED | `## EG – Specification` + eg.xpt 首句 (gap S) | 185 |
| 3-4 | EG/spec.md:108/117 | pdf:p186 CT | REPLACED | EGCAT / EGSCAT CT 空 → `*` | 186 |
| 5 | EG/spec.md:402 | ig34_p0188_a005 | INSERTED | `> ¹In this column, …` (最后变量块 `---` 后, Cross References 前; U7) | 188 |
| 6 | OE/assumptions.md:3-5 | ig34_p0298_a024/a025 | INSERTED | `## OE – Description/Overview` + 定义句 (gap D) | 298 |
| 7 | OE/assumptions.md:7-9 | ig34_p0299_a001/a002 | INSERTED | `## OE – Specification` + oe.xpt 首句 (gap S) | 299 |
| 8 | OE/assumptions.md:11 | pdf:p301 OE – Assumptions | INSERTED | `## OE – Assumptions` (gap A) | 301 |
| 9-11 | OE/spec.md:99/108/117 | pdf:p299 CT | REPLACED | OETSTDTL / OECAT / OESCAT 空 → `*` | 299 |
| 12 | OE/spec.md:474 | pdf:p301 脚注 | INSERTED | 脚注 (U7 位置) | 301 |
| 13 | UR/assumptions.md:3-5 | ig34_p0312_a012/a013 | INSERTED | `## UR – Description/Overview` + 定义句 | 312 |
| 14 | UR/assumptions.md:7-9 | ig34_p0312_a014/a016 | INSERTED | `## UR – Specification` + ur.xpt 首句 (含 PDF "per per", U-1) | 312 |
| 15 | UR/assumptions.md:11 | pdf:p314 UR – Assumptions | INSERTED | `## UR – Assumptions` | 314 |
| 16-18 | UR/spec.md:108/117/126 | pdf:p313 CT | REPLACED | URTSTDTL / URCAT / URSCAT 空 → `*` | 313 |
| 19 | UR/spec.md:393 | ig34_p0314_a010 | INSERTED | 脚注 | 314 |
| 20 | PE/assumptions.md:23-25 | ig34_p0315_a025/a026 | INSERTED | `## PE – Description/Overview` + 定义句 (Alignment 段之后, 同 PDF 顺序) | 315 |
| 21 | PE/assumptions.md:27-29 | ig34_p0316_a001/a003 | INSERTED | `## PE – Specification` + pe.xpt 首句 | 316 |
| 22-25 | PE/spec.md:63/72/90/99 | pdf:p316 CT | REPLACED | PETESTCD / PETEST / PECAT / PESCAT 空 → `*` | 316 |
| 26 | PE/spec.md:174 | pdf:p316 PELAT Notes | REPLACED | "laterallity" → "laterality" (PDF_TYPO PE T-1) | 316 |
| 27 | PE/spec.md:276 | ig34_p0317_a011 | INSERTED | 脚注 | 317 |
| 28 | SS/assumptions.md:3-5 | ig34_p0342_a019/a020 | INSERTED | `## SS – Description/Overview` + 定义句 | 342 |
| 29 | SS/assumptions.md:7-9 | ig34_p0342_a021/a022 | INSERTED | `## SS – Specification` + ss.xpt 首句 | 342 |
| 30 | SS/assumptions.md:11 | pdf:p343 SS – Assumptions | INSERTED | `## SS – Assumptions` | 343 |
| 31-32 | SS/spec.md:81/90 | pdf:p343 CT | REPLACED | SSCAT / SSSCAT 空 → `*` | 343 |
| 33 | SS/spec.md:204 | ig34_p0343_a021 | INSERTED | 脚注 | 343 |
| 34 | SS/examples.md:7 | ig34_p0344_a008 | INSERTED | Ex1 表前 `**ss.xpt**` (PDF 数据集标签; KB 313 处同写法) | 344 |
- 新插入文字逐字核: 脚本把 `git diff -U0` 每个 `+` 行 (去 `## `/`> `/`**` 前缀, ¹→1) 在对应页 layout 文本 (仅空白归一, 不归一 dash/引号) 中查, 全部命中, 唯一例外 #26 (T-1, 预期). em dash — 与 en dash – 均为 PDF 原字符.
- 新增 atom 清单 (R3, gaps 之外): #34 (ss.xpt 标签); #26 (T-1). 其余均属 gaps / intros / footnote / CT `*`.

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | DA/assumptions.md:3-5 | 新增 `## §6.3 …` 节 (§ 前缀同 AE §6.2 / NV / FT 先例) | U3, intros |
| S-2 | EG/assumptions.md:7 | 新增 `## EG – Specification` | gap S (CM/DS 先例: Description 与 Assumptions 之间) |
| S-3 | OE/UR/SS assumptions.md:3/7/11 | 各新增 Description/Overview、Specification、Assumptions 三个 `##` 标题 | gaps D/S/A |
| S-4 | PE/assumptions.md:23/27 | 新增 `## PE – Description/Overview`、`## PE – Specification` (位于 KB 既有 `### PE - Alignment …` 之后、`## PE – Assumptions` 之前 = PDF 顺序); 既有 `## 6.3.8 …` / `###` 标题未动 | gaps D/S |
| S-5 | SS/examples.md:7 | 新增 `**ss.xpt**` 标签行 | p344 a008 |
- 无整条 assumption 增删 / 挪位 / 拆合.

### 删除清单
| # | 位置 | 原因 |
|---|---|---|
| D-1 | 14 处 spec CT 空值 | → `*` (U2), 旧值替换 |
| D-2 | PE/spec.md:174 "laterallity" | VALUE_DIFF 旧值替换 (T-1) |
- 无 D2 删除, 无 "PDF 无此条" 整条删除.

### D6 / KB_AUTHORED
- 无新增 D6. 全扫未发现 KB 自写解释性内容 (rscan 0). 纯导航保留: 各 spec.md `> Class|Structure` 行与 Cross References (U8); PE/assumptions `## 6.3.8 Physical Examination (PE)` 为 PDF 节标题 (非自写).

### PDF_TYPO
| T | 位置 | PDF | KB | 依据 | 状态 |
|---|---|---|---|---|---|
| PE T-1 (新) | PE/spec.md:174 PELAT CDISC Notes | "laterallity" | laterality | 同行 Label "Laterality"; OE/UR 同变量 Notes 为 "laterality" (p300/p313) | 本批改 KB, 登记 |
| UR U-1 (新, T4) | UR/assumptions.md:9 spec 首句 | "per location per per visit" | 照录 PDF | 正确措辞 (少一词或多一 per) 无法由 PDF 自身唯一确定 (OE 同位为 "per time point") | 照录, 交 T4 用户裁 |
| EG T-1..T-3 | EG/examples.md 叙述 (FINDINGS / SCREEN 2 / investigation) | — | 照录 PDF | 见 `t2_B-EG.md` | 沿用, 未变 |
| OE T-1 / T-2 / U-1 | relrec IDVARAL / OCCULAR ×4 / OESEQ 1,2,1,2 | — | T-1/T-2 KB 正确值, U-1 照录 | 见 `t2_B-OE.md`; 本次 p304/p305 渲染复核仍成立 | 沿用 |
- 观察 (非 typo, 未改): §6.3 引言 PDF 以冒号结尾而无域列表 (p180 渲染确认); KB 照 PDF 只补句子.

### 范围外 / out_of_scope
- O39: §6.3 章引言已补 (#1, DA host) → 关闭.
- OE 先前 O-OE-1 (OE Description + spec 首句缺) → 本批 #6/#7 关闭; EG X-1 (Description, B-EG 已补) / X-2 (spec 首句) → #2 关闭.
- 原子抽取错 (T3 台账): ig34_p0186_a009/a011/a012, p0299_a010, p0300_a017, p0301_a001/a005/a007/a008/a009/a011/a012/a013, p0302_a005/a026/a027, p0304_a020-a023, p0316_a017, p0192_a006/a009.
- 新范围外: 无.

### 需主控定
1. SS/examples.md:3 `##### Example 1` 标题层级与同类文件 (`## Example N`) 不一致; 规则 6 禁改标题层级 (锚点), 未动.
2. PE/assumptions.md CDASH 段 PDF 为 1 段, KB 拆 6 段 (文字逐字一致); 本批未合并 (仅排版), 如要求按 PDF 段落合并请指示.
3. S-FND.json `pdf_ranges` EG hi=193 应为 192 (p193 = IE); OE/UR/PE/SS 区间无误.

### 验证命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-FND_writer
for d p in EG 185,186,187,188 OE 299,300,301 UR 312,313,314 PE 316,317 SS 342,343; do python3 -I $S/speccmp_bbox.py $S $d $p | grep -v " OK$"; done   # 仅余 ct: U5/U6
for d lo hi in EG 185 192 OE 298 305 UR 312 315 PE 315 318 SS 342 344; do python3 -I $S/scan.py $d $lo $hi; python3 -I $S/rscan.py $d $lo $hi knowledge_base/domains/$d/assumptions.md knowledge_base/domains/$d/examples.md; done
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 18 / DIFF 2 / diffs 5 (全 T-n)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbbase/knowledge_base --out $S/fp_before.jsonl; python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl
#  本批页 (p180, 185-192, 298-305, 312-318, 342-344) 台账原子 246: 回归 0, 新命中 1 (ig34_p0185_a022); 全量回归 0
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/DA/assumptions.md |  4 ++++
 knowledge_base/domains/EG/assumptions.md |  4 ++++
 knowledge_base/domains/EG/spec.md        |  6 ++++--
 knowledge_base/domains/OE/assumptions.md | 10 ++++++++++
 knowledge_base/domains/OE/spec.md        |  8 +++++---
 knowledge_base/domains/PE/assumptions.md |  8 ++++++++
 knowledge_base/domains/PE/spec.md        | 12 +++++++-----
 knowledge_base/domains/SS/assumptions.md | 10 ++++++++++
 knowledge_base/domains/SS/examples.md    |  2 ++
 knowledge_base/domains/SS/spec.md        |  6 ++++--
 knowledge_base/domains/UR/assumptions.md | 10 ++++++++++
 knowledge_base/domains/UR/spec.md        |  8 +++++---
 12 files changed, 73 insertions(+), 15 deletions(-)
```
- writer.jsonl: `work/t2_batches/S-FND.writer.jsonl` 39 行 (改动 34 项, CT 逐格拆行; census_items 5 行 VERIFIED).

### 更正 (同 attempt, 自查后)
- **U5 C-code 计数更正** (上文 "EG 19 / OE 22 / UR 18 / PE 10 / SS 8" 误含 DOMAIN 与 `*` 行): 脚本按 speccmp_bbox 输出逐变量重分, CT 列完整划分 (和 = 变量数, 已断言):

| 域 | `*` | PDF 空 = KB 空 | 字面值一致 | U6 DOMAIN | U5 C-code (按页) | 合计 |
|---|---|---|---|---|---|---|
| EG | 2 | 22 | 3 (EGDTC / EGELTM / EGRFTDTC ISO 8601) | 1 | 16 (p186 7, p187 9) | 44 |
| OE | 3 | 26 | 3 (OEDTC / OEELTM / OERFTDTC) | 1 | 19 (p299 5, p300 13, p301 1) | 52 |
| UR | 3 | 21 | 3 (URDTC / URELTM / URRFTDTC) | 1 | 15 (p312 1, p313 13, p314 1) | 43 |
| PE | 4 | 15 | 1 (PEDTC) | 1 | 9 (p316 5, p317 4) | 30 |
| SS | 2 | 12 | 1 (SSDTC) | 1 | 6 (p343 6) | 22 |
  (EG 页首行 STUDYID / EGSPID / EGXFN / EGELTM bbox 未取, 人工对 layout 归入 "空" / "字面值".)
- **逐页日志更正**: p186 C-code 为 **7** 格 (非 8); p316 为 **5** (非 6); p299 为 **5** (非 4, FOCID 在 scan.py 中经逐格兜底误判命中); p300 13 / p313 13 同上表. DOMAIN 行在 scan.py 中经逐格兜底 "命中", 故 p185/p299/p312/p316/p342 的 "DOMAIN (U6) 未命中" 措辞应读作 "U6 差异 (scan.py 未报)"; p312 第 3 个未命中原子为 URTESTCD (C-code, U5). EGSPID 为 **p186** 页首行 (非 p187).
- **p190 已渲染** (`r190-190.png`, 100dpi): Ex1 12 行 (EGXFN PQW436789-07.xml, EGNAM Test Lab, VISIT Screening 1, r1 EGCLSIG N / r2 Y, r5/r6 EGDRVFL Y 等) 与 Ex2 5 行与 KB 一致; "以 census OK 为据" 改为渲染 + census 双据.
- **PE T-1 渲染**: p316 PELAT 行 150dpi 局部 (`pelat-316.png`) 确认 PDF CDISC Notes 为 "laterallity", 同行 Label "Laterality". 复跑: `grep -n laterallity .work/10_tier_b_repair/work/pdf_pages/ig34_p0316.txt` (1 行). `grep -rln laterallity knowledge_base/` 改后 0 → 无他处副本.
- base HEAD 复核: `git rev-parse --short HEAD` = `056d8cc` (未变).
