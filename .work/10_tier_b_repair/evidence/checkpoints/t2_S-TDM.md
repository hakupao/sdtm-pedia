# T2S S-TDM writer checkpoint (扫描批: TA / TD / TM + §7.1-7.2 引言)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `0d0e813`; 本批 9 文件改前对 HEAD 干净 (`git status --short knowledge_base/domains/{TA,TD,TM}` 空). 其他域工作区改动 (CP/GF/IS/LB/MB/MS/PC/PP) 属并行批, 未触碰.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TDM_writer/`
  (base/ = `git show HEAD:` 副本; apply_tdm.py 精确替换 + 命中次数断言; scan.py 原子 PDF→KB; lscan.py layout 句 PDF→KB; rscan2.py KB→PDF (跳过 Mermaid 块, D6 块单列);
  speccmp_bbox.py (`pdftotext -bbox` 分列, 表头行改为须同行含 Core); concept_chk.py (Concept 表 bbox 右栏词序 diff); census_before/after.json; fp_before/after.jsonl;
  渲染 r382/383/389/391/393/396/397/398/401/412/413/414 整页 100dpi, ct385 CT 列局部)
- md5 before → after (前 8 位): TA/assumptions `e7234e69`→`d9411f19` (136→138 行); TA/spec `9ee685ab`→`64bc59f5` (111→113); TD/assumptions `4ff750cc`→`6ddf148c` (13→21);
  TD/examples `41f6541a`→`2e6e78f5` (165→171); TD/spec `cf29d319`→`e8191b41` (97→99); TM/assumptions `4493956f`→`0dc27f44` (11→15); TM/spec `ebd81f7a`→`9a8e8b9e` (64→66).
  未动: TA/examples (`a96c63b2`), TM/examples (`0dc69e90`).

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| TA 引言 | §7 / §7.1 (7.1.1-7.1.3) / §7.2 | 382-384 | **382 - 384 中部** | p382 顶 `7 Trial Design Model Datasets` (无正文章标题) + `7.1 …` (无正文, 直接 7.1.1); p384 中部 `7.2 Experimental Design (TA and TE)` + 2 段 |
| domains/TA | §7.2.1 | 384-402 | **384 下部 - 402 中部** | p384 `7.2.1 Trial Arms (TA)` 起; p402 上部 Ex7 ta.xpt r12-15 + §7.2.1.1 Issues 4 小节属 TA; p402 末 `7.2.2 Trial Elements (TE)` 起别节 (TE) |
| domains/TD | §7.3.2 | 410-415 | **410 下部 - 414** | p410 上部为 §7.3.1.1 TV Issues (Trial Visit Rules / Ranges / Contingent Visits), 标题 a025 起; **p415 首行即 `7.3.3 Trial Disease Milestones (TM)`** → p415 无 TD 内容, json hi=415 应为 414 |
| domains/TM | §7.3.3 | 415 | **415 上部** | p415 下部 `7.4 Trial Eligibility and Summary (TI and TS)` 起别节 |

### 双向全扫 — 逐页日志
方法: PDF→KB = (a) `work/pdf_atoms.jsonl` 该页全部原子 (含 TABLE_ROW/TABLE_HEADER/CODE_LITERAL/NOTE) 归一后在本域三文件查 (scan.py); (b) layout 文本按句切分去空白后查 (lscan.py, 补 p382-383 等原子外的句); spec 表行以 speccmp_bbox.py 逐变量逐字段为准. KB→PDF = assumptions/examples 逐句 (rscan2.py) 在 layout+原子中查; Mermaid 块与 D6 引用块单列; 表格走 census / 渲染逐格. 计数 = 改后 "页内本节原子 / 命中 / 本次补齐".

| 页 | 节 | PDF→KB: 原子 / 命中 / 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 (未命中分类) |
|---|---|---|---|---|---|
| 382 | §7 / §7.1 / 7.1.1 / 7.1.2 | 22 / 19 / 0 | TA/asm 3-29 有出处 | Concept 表 r1-r4: bbox 逐词 (concept_chk) | 未命中: a001 §7 章标题 (无正文, 章标题不落地 S-INT 口径), a002 §7.1 标题 (无正文; KB 自拟 `## Trial Design Model Overview (§7.1)`, 规则 6 不改), a022 Study cell 行 = T-1 (KB "3 study cells") |
| 383 | 7.1.2 表 / 7.1.3 | 11 / 11 / 0 | TA/asm 31-55 | Concept 表 r5-r9 bbox 逐词 + 渲染 | Treatments 格 PDF 内 3 个 bullet, KB 单格连写 (文字逐字一致) |
| 384 | 7.1.3 尾 / §7.2 / 7.2.1 Desc / Spec | 30 / 26 / 1→1 (ARMCD CT `*`) | TA/asm 57-92 | bbox + layout `Char *` | 未命中: a015 §7.2 标题 (KB 自拟 `## Trial Arms and Trial Elements (§7.2)`, 规则 6 不改, 需主控定 #2), a019/a026 Desc/Spec 标题 (KB `### §7.2.1 Trial Arms (TA) – Description/Overview` / `– Specification` 结构等价), a028 表头 (spec 字段结构) |
| 385 | spec 尾 / 脚注 / asm 1-7 | 18 / 15 / 4→4 (ARM/ETCD/ELEMENT CT `*`, 脚注) + A 标题 | TA/asm 110-124 一致 | bbox + 渲染 ct385 | 未命中: a001 ARMCD 行跨页 (p384/385 Notes 拼接后逐字一致, 人工), a008 EPOCH `(EPOCH)` vs C99079 = U5, a009 脚注原子 "1In" 写法 (已按 ¹ 补) |
| 386 | asm 8-12 / TA – Examples 引言 | 24 / 24 / 0 | TA/asm 126-136; TA/ex 1-18 | — | `TA – Examples` 标题 = ex H1 `# TA — Examples` 结构等价 (同 S-FND 口径) |
| 387 | Ex1 叙述 + 图 | 16 / 15 / 0 | TA/ex 20-34 | — | 未命中: a011 FIGURE (KB Mermaid + D6, B-TA 已核) |
| 388 | Ex1 图 ×3 | 8 / 5 / 0 | 一致 | — | 3 FIGURE (Mermaid D6) |
| 389 | Ex1 矩阵 / ta.xpt / Ex2 | 27 / 26 / 0 | 一致 | census ta OK (99 格); 矩阵渲染逐格 (下) | 1 FIGURE |
| 390 | Ex2 图 | 6 / 4 / 0 | 一致 | — | 2 FIGURE |
| 391 | Ex2 图 / 矩阵 / ta.xpt | 25 / 24 / 0 | 一致 | census ta OK (231 格; r15 en dash = B-TA T-4); 矩阵渲染 | 1 FIGURE |
| 392 | Ex2 ta 尾 / Ex3 | 9 / 7 / 0 | 一致 | census | a006 = T-2 (B-TA, KB 补句点), a005 FIGURE |
| 393 | Ex3 图 / 矩阵 | 11 / 9 / 0 | 一致 | 矩阵渲染逐格 | 2 FIGURE |
| 394 | Ex3 ta / Ex4 | 24 / 23 / 0 | 一致 | census ta OK (132 格) | 1 FIGURE |
| 395 | Ex4 图 | 8 / 5 / 0 | 一致 | — | 3 FIGURE |
| 396 | Ex4 图 / 矩阵 / ta.xpt | 31 / 29 / 0 | 一致 | census ta OK (220 格); 矩阵渲染 | a002 FIGURE; a009 原子 "represents" = ATOM_ERR (B-TA 已登记; 渲染 "represented" = KB) |
| 397 | Ex5 | 26 / 24 / 0 | 一致 | census ta OK (176 格, p397-398); 矩阵渲染 | 2 FIGURE |
| 398 | Ex5 ta 尾 / Ex6 | 21 / 19 / 0 | 一致 | 矩阵渲染 (B 行合并格) | 2 FIGURE |
| 399 | Ex6 ta / Ex7 | 25 / 25 / 0 | 一致 | census ta OK (198 格) | |
| 400 | Ex7 图 | 12 / 10 / 0 | 一致 (图注 ×3 = ex 887/929/970) | — | 2 FIGURE |
| 401 | Ex7 图 / 矩阵 / ta.xpt | 20 / 19 / 0 | 一致 | census ta OK (165 格, p401-402); 矩阵渲染 | 1 FIGURE |
| 402 | Ex7 ta 尾 / §7.2.1.1 | 36 / 33 / 0 | TA/ex 1003-1023 一致 | census | 未命中 a037-a039 = §7.2.2 TE 别节 |
| 410 | §7.3.2 标题 / Desc / Spec 首句 / spec | TD 6 / 2 / 4→4 (D 标题+句, S 标题+句) | TD/asm 3-9 | bbox | 上部 a001-a024 = §7.3.1.1 TV 别节; 未命中: a025 节号标题 (= spec.md H1 `# TD — Trial Disease Assessments` 结构等价), a030 表头 |
| 411 | spec / 脚注 / asm 1-3 | 13 / 13 / 4→4 (脚注, A 标题, asm1 末 3 句, asm2 "e.g.") | TD/asm 11-17; 原无标题顶段 → D-1 删 | bbox 9 变量全字段一致 | 脚注原子 "1In" 写法 (已按 ¹ 补, 改后 scan 仍报 = 写法差异); TDANCVAR Notes "must be a referenced" 照录 (TD U-2 观察) |
| 412 | asm 4-5 / TD – Examples / Ex1 | 15 / 14 / 2→2 (+ 1 week ×2) + Mermaid 标签/D6 | TD/ex 1-56 | census td OK (30 格) + 渲染 | a009 "assessments.." = TD T-1 (KB 单句点); a005 FIGURE (Mermaid, D6 新标, 逻辑核对见下) |
| 413 | Ex2 | 13 / 13 / 2→2 ("start of period 2", + 1 week) + 刻度 X8-X32 | TD/ex 58-108 | census td OK (20 格) + 渲染 | Row 2 文字 "-1 week and + 1 week" vs 表 P53D/P9W = PDF 内部不一致, 照录 (TD U-3 观察) |
| 414 | Ex3 | 16 / 13 / 4→4 (- 3 days / + 1 week ×3, 末句) + 刻度 X12-X48 | TD/ex 109-171 | census: 表头 TDTGPAI = TD T-4, 余 29 格一致 + 渲染 | a006 "restarted)." = TD T-2; a008 "( i.e.," = TD T-3; a010 "every 24 weeks" 照录 = TD U-1 (T4) |
| 415 | §7.3.3 / Desc / Spec / spec / 脚注 / asm / Ex1 | TM 24 / 20 / 3→3 (Spec 标题, A 标题, 脚注) | TM/asm 1-15; TM/ex 1-16 一致 | bbox 5 变量 + census tm OK (12 格) | 未命中: a001 节号标题 (H1 结构等价), a006 表头, a011 TMRPT `(NY)` vs C66742 = U5, a012 脚注 "1In" 写法; 下部 a025-a029 = §7.4 别节 |

- spec.md 非变量行 (KB→PDF): H1、`> Class: … | Structure: …`、`---`、`## Cross References` 块 → U8 导航, 不标 D6.
- KB→PDF (rscan2, 改后): TA 0 句无出处 (仅 assumptions:96/100/104/108 四个 `> See …` 交叉引用 = 导航, 及 ex:385 T-2 / ex:887/929/970 图注转义写法); TD 仅 3 个 D6 块 + 3 个 Mermaid 前粗体标签 (D6 块覆盖) + ex:153 (T-2) / ex:157 (T-3); TM 0.
- 汇总已补: TA 6 (A 标题 1, CT `*` 4, 脚注 1); TD 15 项 (D 2, S 2, A 1, asm1 3 句, asm2 1, 脚注 1, examples 文字 6 处 + 末句 1); TM 3 (Spec 标题, A 标题, 脚注). 余下未命中全部为: 别节 / 结构等价 (节号标题、表头、H1) / FIGURE (Mermaid D6) / 原子抽取错 / T-n / U5 C-code / U6 DOMAIN / 脚注上标写法.

### spec.md Controlled Terms 逐变量 (bbox 分列 + layout `Char *` grep + 渲染 ct385)
- `*` 格: PDF 4 = KB 改后 4 (TA: ARMCD ARM ETCD ELEMENT). TD (p410-411) / TM (p415) layout grep 与 bbox 均 0 个 `*`.
- 非 CT 字段 (Label/Type/Role/Core/CDISC Notes): TA 10 / TD 9 / TM 5 变量全一致 (ARMCD Notes 跨 p384/385, 拼接后人工逐字一致). 变量顺序全同.
- 字面值一致: TD TDSTOFF/TDTGTPAI/TDMINPAI/TDMAXPAI `ISO 8601 duration`.
- U6 (S-CT, 未改): DOMAIN ×3 (TA/TD/TM). U5 (S-CT, 未改): TA EPOCH `(EPOCH)`/C99079; TM TMRPT `(NY)`/C66742.

### census_items 逐格
| 表 | 结果 |
|---|---|
| TA/assumptions.md:31 Concept/Definition (9 行 × 2 列) | 概念列 9 格 = PDF 左栏 (bbox x<165) 逐词一致; 定义列: bbox 右栏 (p382-383) 1116 词 vs KB 1116 词, difflib 差异 11 处 = 10 处行序伪差 (粗体/斜体词 y 基线不同排序错位: arm / study cell / element / branch point / study cell treatment) + **T-1** ("3 study cell" → KB "3 study cells", B-TA 登记沿用); 渲染 r382/r383 复核 Treatments 格 3 bullet 文字一致 |
| TA/examples.md:141 Ex1 矩阵 (渲染 r389) | 表头 4 格 + 3 行 (Placebo/A/B × Screen/Run-in/PLACEBO·DRUG A·DRUG B) 一致 |
| TA/examples.md:325 Ex2 矩阵 (r391) | 表头 8 格 + 3 行 (P-5-10 / 5-P-10 / 5-10-P) 一致 |
| TA/examples.md:495 Ex3 矩阵 (r393) | 表头 4 格 + 4 行 (A-Open A / A-Rescue / B-Open A / B-Rescue) 一致 |
| TA/examples.md:667 Ex4 矩阵 (r396) | 表头 Screen / Treatment (跨 8 列) / Follow-up; A/B 两行各 10 格一致 (PDF 行标签不加粗, KB `**A**` 仅 Markdown 强调) |
| TA/examples.md:753 Ex5 矩阵 (r397) | Treatment 跨 6 列; A: Trt A/Rest A ×3, B: Trt B/Rest B ×3, Follow-up 一致 |
| TA/examples.md:835 Ex6 矩阵 (r398) | A: Trt A/Rest A ×4 一致; B: PDF 为合并格 (Rest B 加宽) 顺序 Trt B/Rest B ×3 + Follow-up, KB 同序, 末 2 格空补位 = 合并格的 Markdown 表达, 内容一致 |
| TA/examples.md:976 Ex7 矩阵 (r401) | CR: Initial Chemo + RT / Chemo + RT (non-Surgery) / Chemo / Chemo / Off Treatment Follow-up; CRS: … (Surgery) / 3-5 w Rest / Surgery / 4-6 w Rest / Chemo / Chemo / Off Treatment Follow-up — 一致 (PDF CRS 行尾多 1 空格属版式) |
| TD/examples.md:167 Ex3 td.xpt (C1) | 表头: PDF p414 `TDTGPAI` / KB `TDTGTPAI` = **TD T-4** (KB 不改); r1-r3 全 30 格一致 (渲染 r414) |
- table_census.py (本批 manifest, TA lo=382, TD/TM 未改): before = after `KB tables 19 / OK 10 / UNPARSEABLE 8 / DIFF 1, cells 1313, diffs 1` (= TD T-4). PDF_ONLY 均别节 (manifest 页段宽).

### TD Mermaid 图逻辑核对 (D6 新标注; 对渲染 r412/r413/r414)
- Ex1: ANCH1DT 锚 → Schedule 1 每 8 周 (8-48) → Schedule 2 每 12 周 (60-96) → Schedule 3 每 24 周 (120, 144, et cetera) — 与 PDF 图一致.
- Ex2: Period 1 (ANCH1DT, Schedule 1 每 8 周, 刻度 8-56 + et cetera); Period 2 (ANCH2DT, Schedule 2 每 8 周, 刻度 **X8-X32**) — KB 原 "+8 wks" 等改为 PDF 刻度名.
- Ex3: Double Blind Treatment (ANCH1DT, Schedule 1 每 8 周 8-48, Schedule 2 每 12 周 60-144 + et cetera); Extension Treatment (ANCH2DT, Schedule 3 每 12 周, 刻度 **X12-X48**) — 一致 (刻度名同上改).
- 三图 "et cetera" 标签: KB "... et cetera, untildisease progression or death" → PDF "et cetera, until disease progression or death".
- 粗体图题 "**Timeline Diagram — Example N: …**" 为 KB 自写 (PDF 图无题), 由同一 D6 注覆盖.

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | TA/assumptions.md:110 | pdf:p385 TA – Assumptions | INSERTED | `## TA – Assumptions` (gap A), 置于 KB 自拟 `## TA-Specific Assumptions` 之上 | 385 |
| 2-5 | TA/spec.md:27/36/54/63 | pdf:p384-385 CT | REPLACED | ARMCD / ARM / ETCD / ELEMENT CT 空 → `*` | 384-385 |
| 6 | TA/spec.md:96 | ig34_p0385_a009 | INSERTED | `> ¹In this column, …` (最后变量块 `---` 后, Cross References 前; U7) | 385 |
| 7 | TD/assumptions.md:3-5 | ig34_p0410_a026/a027 | INSERTED | `## TD – Description/Overview` + 定义句 (gap D) | 410 |
| 8 | TD/assumptions.md:7-9 | ig34_p0410_a028/a029 | INSERTED | `## TD – Specification` + td.xpt 首句 (gap S) | 410 |
| 9 | TD/assumptions.md:11 | pdf:p411 TD – Assumptions | INSERTED | `## TD – Assumptions` (gap A) | 411 |
| 10 | TD/assumptions.md:13 | ig34_p0411_a011 | INSERTED | asm 1 末补 3 句 ("TD has limited utility within oncology …") | 411 |
| 11 | TD/assumptions.md:3 (原) | KB 顶段 | DELETED | 见 D-1 | 411 |
| 12 | TD/assumptions.md:15 | ig34_p0411_a012 | REPLACED | "(e.g., ANCH1DT" → "(e.g. ANCH1DT" (PDF 逐字; 非拼写错, 不按 typo 处理) | 411 |
| 13 | TD/spec.md:87 | ig34_p0411_a009 | INSERTED | 脚注 | 411 |
| 14 | TD/examples.md:5 | pdf:p412 figure | INSERTED | D6 `> KB note (not in SDTMIG): the following label and Mermaid diagram are a KB rendering of the untitled PDF Example 1 figure (p412).` | 412 |
| 15 | TD/examples.md:32 | pdf:p412 figure | REPLACED | Mermaid ETC 标签 → "et cetera, until disease progression or death" | 412 |
| 16-17 | TD/examples.md:44/46 | ig34_p0412_a011/a012 | REPLACED | "+1 week" → "+ 1 week" (PDF 逐字, 渲染确认有空格) | 412 |
| 18 | TD/examples.md:58 | pdf:p413 figure | INSERTED | D6 (Example 2 figure, p413) | 413 |
| 19 | TD/examples.md:74/82-86 | pdf:p413 figure | REPLACED | ETC1/ETC2 标签同 #15; 刻度 "+8/+16/+24/+32 wks" → "X8/X16/X24/X32" | 413 |
| 20 | TD/examples.md:92 | ig34_p0413_a003 | REPLACED | "start of the period 2 treatment" → "start of period 2 treatment" | 413 |
| 21 | TD/examples.md:98 | ig34_p0413_a008 | REPLACED | "+1 week" → "+ 1 week" | 413 |
| 22 | TD/examples.md:109 | pdf:p414 figure | INSERTED | D6 (Example 3 figure, p414) | 414 |
| 23 | TD/examples.md:134/143-147 | pdf:p414 figure | REPLACED | ETC 标签; 刻度 "+12..+48 wks" → "X12..X48" | 414 |
| 24 | TD/examples.md:157 | ig34_p0414_a008 | REPLACED | "-3 days and +1 week" → "- 3 days and + 1 week" ("( i.e.," 见 T-3, 未改) | 414 |
| 25 | TD/examples.md:159 | ig34_p0414_a009 | REPLACED | "+1 week" → "+ 1 week" | 414 |
| 26 | TD/examples.md:161 | ig34_p0414_a010 | REPLACED | "repeats every 12 weeks" → "every 24 weeks" (照录 PDF, U-1); "+1" → "+ 1"; 末补 "The schematic shows that, for the third pattern, assessments will occur until disease progression; this therefore leaves the pattern open-ended." | 414 |
| 27 | TD/examples.md:40 | ig34_p0412_a009 | SKIPPED_PDF_TYPO | T-1 "assessments.." | 412 |
| 28 | TD/examples.md:153 | ig34_p0414_a006 | SKIPPED_PDF_TYPO | T-2 "restarted)." | 414 |
| 29 | TD/examples.md:167 | census 表头 col6 | SKIPPED_PDF_TYPO | T-4 TDTGPAI | 414 |
| 30 | TM/assumptions.md:7 | pdf:p415 TM – Specification | INSERTED | `## TM – Specification` (PDF 标题; 既有 `**tm.xpt, …**` 行未动) | 415 |
| 31 | TM/assumptions.md:11 | pdf:p415 TM – Assumptions | INSERTED | `## TM – Assumptions` (gap A) | 415 |
| 32 | TM/spec.md:51 | ig34_p0415_a012 | INSERTED | 脚注 | 415 |
- 新插入文字逐字核: `git diff -U0` 每个 `+` 行 (去 `## `/`> `/`**`/列表前缀, ¹→1, 跳过 Mermaid/D6/CT `*`) 按句在 p384-385/410-415 layout (仅空白归一) 中查, 全部命中; 唯一例外 TD asm 2 (既有直引号 "anchor" vs PDF 弯引号, 排版字符, S-TYPO; 归一引号后命中) 与 Ex3 bullet 1 ("( i.e." T-3, 预期).
- 新增 atom 清单 (R3, gaps 之外): #10 (asm1 3 句), #12, #16-17, #20-21, #24-26 (TD 叙述逐字), #30 (TM Spec 标题), #15/#19/#23 (图标签).

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | TA/assumptions.md:110 | 新增 `## TA – Assumptions`, 紧邻其下保留 KB 自拟 `## TA-Specific Assumptions` (规则 6 不改; 原标题不匹配矩阵 regex, gap A 不能靠它关闭) → 两个相邻 H2, 见需主控定 #1 | gap A |
| S-2 | TD/assumptions.md:3/7/11 | 新增 Description/Overview、Specification、Assumptions 三个 `##` 标题 + D/S 两句 | gaps D/S/A (OE/UR/SS 先例) |
| S-3 | TD/assumptions.md 原 :3 | 删除无标题顶段 (asm 1 的改写副本) | D-1 |
| S-4 | TD/assumptions.md:13 | asm 1 补全 (条目内追加 3 句, 非整条增删) | R2 |
| S-5 | TM/assumptions.md:7/11 | 新增 `## TM – Specification`、`## TM – Assumptions` (新标题用 PDF en dash; 既有 `## TM — Description/Overview` em dash 未动) | PDF 标题 / gap A |
| S-6 | TD/examples.md:5/58/109 | 三处 D6 注 (新增引用块行) | D6 |
- 无 assumptions 整条增删 / 挪位 / 拆合.

### 删除清单
| # | 位置 | 原因 | 保留副本 |
|---|---|---|---|
| D-1 | TD/assumptions.md 原 :3 (HEAD 行 3, 1 段 ~140 词) | KB 无标题顶段 = asm 1 改写副本 ("TD has limited utility **in** oncology …" vs PDF "within"); PDF p410-411 Description 段内容不同 (见 #7), 无此段出处. asm 1 补全 (#10) 后该段全部信息已由 asm 1 逐字承载 → D2 去重删除. fp_before: 该行不独占任何 hit_target 原子 (a011 当时未命中, 补全后命中) | TD/assumptions.md:13 (asm 1) |
| D-2 | TD/examples.md:161 "every 12 weeks" | 旧值替换为 PDF 值 (U-1) | — |
| D-3 | TD/examples.md 各处 "+1 week" / "-3 days" / "the period 2" / "(e.g.," / Mermaid 标签 | VALUE_DIFF 旧值替换 | — |
| D-4 | TA/spec.md 4 处 CT 空值 | → `*` | — |

### D6 / KB_AUTHORED
| # | 位置 | 内容 | 判定 |
|---|---|---|---|
| D6-1..3 | TD/examples.md:5/58/109 | 粗体图题 "Timeline Diagram — Example N: …" + Mermaid (PDF 图无题) | 不矛盾 (逻辑核对见上), 新加 KB note |
- TA: B-TA 已标 D6 全部沿用 (rscan2 列出 29 处 KB note, 未改); TM 无 KB 自写. 纯导航保留: 各 spec.md `> Class|Structure` 与 Cross References (U8); TA/assumptions `> See …` 交叉引用 4 处.

### PDF_TYPO
| T | 位置 | PDF | KB | 依据 | 状态 |
|---|---|---|---|---|---|
| TD T-1 (新) | TD/examples.md:40 Ex1 叙述末 | "assessments.." | 单句点 | 双句点为排印错, 句界唯一 | KB 正确值, 登记 |
| TD T-2 (新) | TD/examples.md:153 Ex3 叙述 | "is restarted)." | "restarted." | 同句无左括号 ("re-baselined, i.e., …" 未开括号), 多余右括号 | KB 正确值, 登记 |
| TD T-3 (新) | TD/examples.md:157 Ex3 bullet 1 | "( i.e., week 8" | "(i.e., week 8" | 括号内多空格; 同页/同节其余 "(i.e.," 均无空格 | KB 正确值, 登记 |
| TD T-4 (新, C1) | TD/examples.md:167 Ex3 td.xpt 表头 | TDTGPAI | TDTGTPAI | spec p411 变量名 + Ex1/Ex2 表头 + asm 4 "(TDTGTPAI)" | KB 正确值, 登记 |
| TD U-1 (新, T4) | TD/examples.md:161 Ex3 bullet 3 | "repeats every 24 weeks (week 120, week 144, etc.)" | 照录 PDF (改前 KB 为 "12 weeks") | PDF 图 Schedule 3 "every 12 weeks" 刻度 X12-X48 + 表 r3 TDTGTPAI P12W = 12; 但同句 "from week 96 … (week 120, week 144)" 只与 24 自洽 (疑整句沿用 Ex1) → 正确措辞无法由 PDF 唯一确定 | 照录, 交 T4 用户裁 (需主控定 #3) |
| TD U-2 (观察) | TD/spec.md TDANCVAR Notes | "This must be a referenced from the ADaM ADSL dataset" | 照录 (改前已同) | "be referenced" / "a reference" 二义 | 照录, 登记 |
| TD U-3 (观察) | TD/examples.md:98 Ex2 Row 2 | 文字 "limits of -1 week and + 1 week" vs 表 r2 P53D/P9W (= -3 days / +1 week) | 照录 | PDF 文字与表不一致, 非 KB 错 | 照录, 登记 |
| TA T-1 / T-2 / T-4 / ATOM_ERR p396_a009 | 见 `t2_B-TA.md` | — | — | 本次 bbox/渲染复核仍成立 | 沿用 |
| TA T-3 / T-5 (T4) | 见 `t2_B-TA.md` | — | 照录 | — | 沿用, 未变 |
- 注: "+ 1 week" / "- 3 days" (加空格) PDF 全节一致写法之一 (Ex1 bullet 1 "(-3 days, +1 week)" 无空格, KB 亦照录无空格), 渲染 r412/r414 确认, 按逐字改 KB, 不视为 typo.

### 范围外 / out_of_scope
- out_of_scope[]: 无.
- B-TA X-4 (KB 自拟 §7.1 / §7.2 H2 标题文字与 PDF 不同) 仍在, 规则 6 未改 → 需主控定 #2.
- 原子抽取错 (T3 台账): ig34_p0396_a009 (沿用); 脚注原子 "1In" 写法 (p385_a009 / p411_a009 / p415_a012).
- 新范围外: 无.

### 需主控定
1. TA/assumptions.md:110-112 现为 `## TA – Assumptions` + 紧接 `## TA-Specific Assumptions` 两个相邻 H2 (后者 KB 自拟, 规则 6 不改). 是否删去 KB 自拟标题 (`grep -rln ta-specific-assumptions knowledge_base web/src` = 0, 无入站锚点), 请指示.
2. TA/assumptions.md `## Trial Design Model Overview (§7.1)` / `## Trial Arms and Trial Elements (§7.2)` 为 KB 自拟标题, PDF 为 "7.1 Introduction to Trial Design Model Datasets" / "7.2 Experimental Design (TA and TE)" (B-TA X-4); 规则 6 未改.
3. TD U-1 (Ex3 bullet 3 "24 weeks" vs 图/表 12): 已照录 PDF, 交 T4 用户裁.
4. S-TDM.json `pdf_ranges` / sections TD hi=415 应为 414 (p415 = TM).

### 验证命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TDM_writer
python3 -I $S/speccmp_bbox.py $S TA 384,385 | grep -v " OK$"   # 仅 DOMAIN (U6), EPOCH (U5), ARMCD Notes 跨页 (人工一致)
python3 -I $S/speccmp_bbox.py $S TD 410,411 | grep -v " OK$"   # 仅 DOMAIN (U6)
python3 -I $S/speccmp_bbox.py $S TM 415 | grep -v " OK$"       # 仅 DOMAIN (U6), TMRPT (U5)
python3 -I $S/scan.py TA 382 402; python3 -I $S/scan.py TD 410 414; python3 -I $S/scan.py TM 415 415
python3 -I $S/lscan.py TD 410 414; python3 -I $S/lscan.py TA 382 402
python3 -I $S/rscan2.py TD 410 414 knowledge_base/domains/TD/assumptions.md knowledge_base/domains/TD/examples.md
python3 -I $S/concept_chk.py $S     # Concept 表: 11 处差异 = 行序伪差 + T-1
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 10 / UNPARSEABLE 8 / DIFF 1 (T-4)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl
#  本批页 (p382-402, 410-415) 台账原子 266: 回归 0, 新命中 2 (ig34_p0411_a011, a012); 全量回归 0 (fp_before 同时刻同树)
MATRIX_TAG=S-TDM python3 .work/10_tier_b_repair/work/scratch/t2/global/t2_coverage_matrix.py   # TA/TD/TM D/S/A/F 全 Y, 缺口 -
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/TA/assumptions.md |  2 ++
 knowledge_base/domains/TA/spec.md        | 10 ++++---
 knowledge_base/domains/TD/assumptions.md | 14 +++++++---
 knowledge_base/domains/TD/examples.md    | 46 ++++++++++++++++++--------------
 knowledge_base/domains/TD/spec.md        |  2 ++
 knowledge_base/domains/TM/assumptions.md |  4 +++
 knowledge_base/domains/TM/spec.md        |  2 ++
 7 files changed, 53 insertions(+), 27 deletions(-)
```
- writer.jsonl: `work/t2_batches/S-TDM.writer.jsonl` 40 行 (改动 32 项拆行 + census_items 8 行 VERIFIED).

## attempt 1 delta (主控裁定 2026-11-26)
- 裁定 (1): `grep -rn "ta-specific-assumptions\|TA-Specific" knowledge_base` (排除标题行本身) = 0 → 删除 TA/assumptions.md:112 `## TA-Specific Assumptions` 标题行 (连同其后空行); 其下列表 1-12 不动. `## TA – Assumptions` (:110) 后即接 asm 1.
- 删除清单追加: | D-5 | TA/assumptions.md 原 :112 `## TA-Specific Assumptions` | KB 自拟冗余标题, 与 PDF `TA – Assumptions` (:110) 重复; 无入站锚点 → D2 | 保留 :110 |
- 裁定 (2) §7.1/§7.2 KB 自拟标题: 规则 6 不改, 记录. (3) TD U-1 照录 + T4: 维持. (4) json TD hi=414: 主控已改.
- TA/assumptions.md 138 → 136 行. `python3 tools/check_links.py 2>&1 | grep "live docs"` = 42.
