# T2 B-LB writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `97e18955346a42d29b1528c78d1d4b8d332d8137`
- md5 before: LB/assumptions.md `eefebeeaba1610ff0d6a96e54b06a3b6`; LB/examples.md `2953e31d91fe41a865f284cd37cbceef`
- md5 after: LB/assumptions.md `aa30eb75982af382ca8556861d5372a3`; LB/examples.md `496bb1298f9e69d0e7268a09f9340ace`
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_BLB_writer/`
  (census_before/after.json, pdf_tables.json (bbox parse p246-248), ex1/2/3.md, narr.py, renders ex1_*/t369_*/t496_* 400dpi, p-195/196 110dpi)
- 数据来源: Ex1-3 表由 `table_census.parse_pdf` (bbox) 生成, 逐 tile 对照 400dpi 渲染 (Ex1 三段 41 列 × 18 行, Ex2/Ex3 各两段) 人工核, 全部一致.
  通用规格表 p195-196 由 layout 文本手写, 再用独立的 bbox 按列切片脚本 (header x 起点 + 行首变量名 y) 逐格比对: 28/29 行 7 列完全一致,
  --DY 行因与脚注同框被切片脚本并入, 人工对 layout 文本核对一致. 叙述行用 narr.py (归一化去空白子串) 对 PDF 页文本复核, 全部命中.
- 原子 verbatim 不可信处 (未采用): a005 (Ex1 表头列序/列名错), a011 (Ex2 表头缺 LBLOINC), p196 a006 ("defined"; PDF 为 "derived").

### 变更清单

| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | LB/assumptions.md:9 | ig34_p0194_a022 | INSERTED | §6.3.5.1 引言句 | 194 |
| 2 | LB/assumptions.md:11 | ig34_p0195_a001 | INSERTED | bullet 1 (SDTMIG includes several domains…) | 195 |
| 3 | LB/assumptions.md:12 | ig34_p0195_a002 | INSERTED | bullet 2 ("--" placeholder) | 195 |
| 4 | LB/assumptions.md:13 | ig34_p0195_a003 | INSERTED | bullet 3 (req/exp/perm variables) | 195 |
| 5 | LB/assumptions.md:14 | ig34_p0195_a004 | INSERTED | 子 bullet o (additional variables w/ CT) | 195 |
| 6 | LB/assumptions.md:15 | ig34_p0195_a005 | INSERTED | 子 bullet o (Findings class permissible vars) | 195 |
| 7 | LB/assumptions.md:16 | ig34_p0195_a006 | INSERTED | 子 bullet o (identifier/timing vars) | 195 |
| 8 | LB/assumptions.md:22 | ig34_p0195_a009 | TABLE_REBUILT | 通用表 STUDYID | 195 |
| 9 | LB/assumptions.md:23 | ig34_p0195_a010 | TABLE_REBUILT | DOMAIN (CT "--") | 195 |
| 10 | LB/assumptions.md:24 | ig34_p0195_a011 | TABLE_REBUILT | USUBJID | 195 |
| 11 | LB/assumptions.md:25 | ig34_p0195_a012 | TABLE_REBUILT | --SEQ | 195 |
| 12 | LB/assumptions.md:26 | ig34_p0195_a013 | TABLE_REBUILT | --GRPID | 195 |
| 13 | LB/assumptions.md:27 | ig34_p0195_a014 | TABLE_REBUILT | --REFID | 195 |
| 14 | LB/assumptions.md:28 | ig34_p0195_a015 | TABLE_REBUILT | --TESTCD | 195 |
| 15 | LB/assumptions.md:29 | ig34_p0195_a016 | TABLE_REBUILT | --TEST | 195 |
| 16 | LB/assumptions.md:30 | ig34_p0195_a017 | TABLE_REBUILT | --CAT | 195 |
| 17 | LB/assumptions.md:31 | ig34_p0195_a018 | TABLE_REBUILT | --SCAT | 195 |
| 18 | LB/assumptions.md:32 | ig34_p0195_a019 | TABLE_REBUILT | --ORRES | 195 |
| 19 | LB/assumptions.md:34 | ig34_p0195_a021 | TABLE_REBUILT | --LLOD | 195 |
| 20 | LB/assumptions.md:36 | ig34_p0195_a023 | TABLE_REBUILT | --STRESN (折行 "--/STRESC" 合并为 --STRESC) | 195 |
| 21 | LB/assumptions.md:40 | ig34_p0196_a003 | TABLE_REBUILT | --NAM | 196 |
| 22 | LB/assumptions.md:41 | ig34_p0196_a004 | TABLE_REBUILT | --SPEC | 196 |
| 23 | LB/assumptions.md:42 | ig34_p0196_a005 | TABLE_REBUILT | --METHOD | 196 |
| 24 | LB/assumptions.md:43 | ig34_p0196_a006 | TABLE_REBUILT | --LOBXFL ("Operationally derived", 按页面非 atom) | 196 |
| 25 | LB/assumptions.md:44 | ig34_p0196_a007 | TABLE_REBUILT | --LLOQ | 196 |
| 26 | LB/assumptions.md:45 | ig34_p0196_a008 | TABLE_REBUILT | --ULOQ | 196 |
| 27 | LB/assumptions.md:48 | ig34_p0196_a011 | TABLE_REBUILT | VISITDY | 196 |
| 28 | LB/assumptions.md:50 | ig34_p0196_a013 | TABLE_REBUILT | --DY ("sponsor-defined" 保留连字符) | 196 |
| 29 | LB/examples.md:22-41 | ig34_p0247_a005 (+ pdf_only p247 lb.xpt) | TABLE_REBUILT | KB 自写斜体概述 (D2 删扩写, 见删除清单 X-1) → PDF 18 行 × 41 列整表 | 247 |
| 30 | LB/examples.md:52-56 | ig34_p0247_a011 | TABLE_REBUILT | Ex2 表头 29→34 列按 PDF; 3 行旧版 CREAT 数据 → PDF GLUC 数据 | 247 |
| 31 | LB/examples.md:67 | ig34_p0247_a020 | TABLE_REBUILT | Ex3 表头按 PDF (+LBRESSCL/LBRESTYP/LBORNRLO/LBORNRHI/LBSTNRLO/LBSTNRHI/LBLOBXFL, −LBMETHOD); PDF 表头 "LBSTRNHI" → 保留 LBSTNRHI (T-1) | 247 |
| 32 | LB/examples.md:69 | ig34_p0247_a021 | REPLACED | Ex3 r1: LBCAT 空→CHEMISTRY, Ord/PrThr, LBLOBXFL Y, LBDTC 09T10:00→19T04:00 | 247 |
| 33 | LB/examples.md:70 | ig34_p0247_a022 | REPLACED | Ex3 r2: LBCAT→CHEMISTRY, Ord/PrThr, LBDTC→1999-06-24T08:00 | 247 |

atoms 覆盖: 33/33 (REAL_GAP 29: INSERTED 7 + TABLE_REBUILT 22; VALUE_DIFF 4: TABLE_REBUILT 2 + REPLACED 2).

### 新增 atom 清单 (不在 atoms[], 按 dispatch notes "叙述缺失也补" / 整表补 / 结构行)

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| N1 | LB/assumptions.md:3 | ig34_p0194_a017 | INSERTED | `## §6.3.5 Specimen-based Findings Domains` (仿 NV §6.3.7; 未分诊, KB 全缺) | 194 |
| N2 | LB/assumptions.md:5 | ig34_p0194_a018/a019/a020 | INSERTED | §6.3.5 引言 3 句 (未分诊 ledger PARTIAL, KB 全缺) | 194 |
| N3 | LB/assumptions.md:7 | ig34_p0194_a021 | INSERTED | `## §6.3.5.1 Generic Specimen-based Lab Findings Domain Specification` | 194 |
| N4 | LB/assumptions.md:18 | ig34_p0195_a007 | INSERTED | 表标题行 `--.xpt, Generic Specimen-Based Laboratory Findings — …` (粗体) | 195 |
| N5 | LB/assumptions.md:20-21 | ig34_p0195_a008 (IE) | INSERTED | 表头 (结构行, reviewer 签字) | 195 |
| N6 | LB/assumptions.md:33,35,37-39,46,47,49 | p195 a020/a022/a024; p196 a001/a002/a009/a010/a012 | TABLE_REBUILT | 通用表其余 8 行 (--ORRESU, --STRESC, --STRESU, --STAT, --REASND, VISITNUM, VISIT, --DTC), 整表补 | 195-196 |
| N7 | LB/assumptions.md:52 | ig34_p0196_a014 | INSERTED | 通用表脚注 ¹ (与 LB 表脚注同文) | 196 |
| N8 | LB/assumptions.md:54 | ig34_p0245_a008 | INSERTED | `## LB – Assumptions` (PDF 标题; 防止原 LB 脚注+8 条假设落入 §6.3.5.1 节下; 仿 NV `## NV – Assumptions`) | 245 |
| N9 | LB/assumptions.md:73 | ig34_p0246_a003 (ledger EQUIVALENT) | REPLACED | 假设 8 变量列表补 "LBPOS, LBLOC, LBFAST," (KB 漏 3 个变量) | 246 |
| N10 | LB/examples.md:13 | ig34_p0246_a013 (ledger EQUIVALENT) | REPLACED | Ex1 Row 9 "set to indicate that" → "set to missing because" (KB 语义反转) | 246 |
| N11 | LB/examples.md:47 | ig34_p0247_a008 | REPLACED | Ex2 Row 1 LBRFDTC → LBRFTDTC | 247 |
| N12 | LB/examples.md:48 | ig34_p0247_a009 | REPLACED | Ex2 Rows 2-3 LBRFDTC → LBRFTDTC | 247 |
| N13 | LB/examples.md:86 | census examples.md:67 r3 LBLOBXFL | REPLACED | Ex4 r3 LBLOBXFL 空 → Y | 248 |
| N14 | LB/examples.md:90 | ig34_p0248_a012 (ledger EQUIVALENT) | REPLACED | Ex5 引言 "single binding agent" → "single agent" (KB 扩写词删除, D2 删扩写, 见 X-2) | 248 |
| N15 | LB/examples.md:92 | ig34_p0248_a013 (ledger EQUIVALENT) | REPLACED | Ex5 Row 1 "total of HGFR" → "total amount of HGFR" | 248 |

N9-N15 为单项行内错词, 按 B-PCPP 先例 (O-b, 叙述 PPRFDTC→PPRFTDTC) 原地 REPLACED, 未用"插入原文于改写句后" (否则同一 Row 说明出现两条互相矛盾的句子). 请主控/reviewer 确认此口径.
通用表每行 PDF 页: STUDYID…--STRESU (16 行) = p195; --STAT…--DY (13 行) = p196 (逐行见 writer.jsonl). KB 表内不加页码注释 (避免 KB 自写文字).

### census 表处理

| census ref (before 行号) | 处理 | after |
|---|---|---|
| examples.md:33 Ex2 lb.xpt (105 diffs; kb_lines 35-37) | 整表按 PDF 重建 (表头 + 3 行全格) | :52 OK (102 格) |
| examples.md:48 Ex3 lb.xpt (10 diffs; kb_lines 50-51) | 整表按 PDF 重建 | :67 DIFF 1 = HEADER LBSTNRHI vs PDF LBSTRNHI (T-1, 预期残留) |
| examples.md:63 Ex4 lb.xpt (1 diff; kb_line 67) | r3 LBLOBXFL → Y | :82 OK (66 格) |
| pdf_only p247 Ex1 lb.xpt (18 行) | 在 Ex1 位置补整表 (表头 + 18 行, 含 Row 列), 表前保留 `**lb.xpt**` | :22 OK (738 格) |
| examples.md:80 Ex5 | 未动 | :99 OK |
| (p241 is.xpt / suppis.xpt ×2 PDF_ONLY) | 页范围溢出, 属 IS 批, 不处理 | — |
| assumptions.md:20 通用规格表 (新增) | 无 Row 列 → census UNPARSEABLE; **reviewer 须对 p195/p196 渲染逐格人工核** | UNPARSEABLE |

census before: DIFF 3 / OK 1 / PDF_ONLY 4 (其中本批 1), 116 diffs / 275 格; after: OK 4 / DIFF 1 / UNPARSEABLE 1 / PDF_ONLY 3 (均 IS), 1 diff / 1040 格.
命令: `python3 -I .work/10_tier_b_repair/scripts/table_census.py --pages ig34:241-248 --kb knowledge_base/domains/LB/examples.md knowledge_base/domains/LB/assumptions.md --out <scratch>/census_after.json`

### 删除清单

| # | file:line (before) | 原因 | 保留/替代位置 |
|---|---|---|---|
| X-1 | LB/examples.md:22 (1 行斜体 "*Note: The LB Example 1 table contains 18 rows and over 30 columns…*") | KB_AUTHORED 且与 PDF 矛盾 (列出 LBTOX/LBTOXGR/LBNAM/LBBLFL/LBENDTC 与 Monocytes, PDF 表均无; 漏 LBLOBXFL) → D2 删扩写 | 被 PDF Ex1 整表替代 (examples.md:22-41) |
| X-2 | LB/examples.md:71 词 "binding" ("single binding agent") | KB 扩写超出 PDF 原文 → D2 删扩写 | 同行, PDF 原文 "single agent" |
| X-3 | LB/examples.md:33-37 / 48-51 旧 Ex2/Ex3 表 | VALUE_DIFF 旧值被替换 (旧版数据 CREAT / 旧列); Ex3 删 KB-only LBMETHOD 列 (PDF 无此列) | 同位置 PDF 表 |

### PDF_TYPO

| T# | 位置 | 说明 |
|---|---|---|
| T-1 | p247 Ex3 表头第 19 列 "LBSTRNHI" | PDF 拼写错 (应为 LBSTNRHI, 同表 LBSTNRLO 与 Ex1/Ex2 均为 LBSTNRHI); KB 保留 LBSTNRHI; census 残留 1 HEADER diff |

非 typo 但需注意 (按 PDF 原样保留, 未归一化): Ex3 LBRESSCL/LBRESTYP 印为 "Ord"/"PrThr" (Ex1/Ex2 为 ORDINAL / PRESENCE OR THRESHOLD 全称); Ex1 r1 LBORRESU g/L → LBSTRESU g/dL 且数值 30→3.0 (PDF 原样).

### 范围外发现

- 无 (本批文件内发现的叙述差异均已按 dispatch notes 处理, 列于 N9-N15). assumptions.md:70 "…submission value in the CDISC Unit codelist." narr 检查 MISS 系 p245/p246 跨页拼接, 非差异.

### 触碰过的 unparseable 表

- LB/assumptions.md:20-50 通用规格表 (新增, 无 Row 列) — reviewer 人工逐格 (渲染 p195/p196).

### git diff --stat -- knowledge_base/domains/LB/

```
 knowledge_base/domains/LB/assumptions.md | 55 +++++++++++++++++++++++++++++++-
 knowledge_base/domains/LB/examples.md    | 51 +++++++++++++++++++----------
 2 files changed, 89 insertions(+), 17 deletions(-)
```

### 复跑命令 (repo 根; S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_BLB_writer)

- PDF 表解析: `python3 -I $S/dump.py $S/pdf_tables.json` → `python3 -I $S/gen_tables.py $S` (生成 ex1/2/3.md, 再人工贴入 KB)
- 通用表独立逐格: `python3 -I $S/colcheck.py` → 期望 `29 29 bad 1 ['--DY In this column,']` (--DY 行与脚注同框, 人工核过)
- 叙述子串核: `python3 -I $S/narr.py knowledge_base/domains/LB/examples.md 246,247,248` (期望无输出);
  `python3 -I $S/narr.py knowledge_base/domains/LB/assumptions.md 194,195,196` (行 1-52 无 MISS) / `… 245,246` (仅 :70 跨页 MISS)
- census: 见上 census 段命令.

### 需主控裁定 / 补充记录

- 结构决定: `## LB – Assumptions` (:54) 置于原 LB 规格脚注 `> ¹In this column…` (:56) **之前**; PDF 顺序为脚注在前、标题在后. 原脚注本是 LB 规格表 (p245) 的孤儿脚注, 现与新增通用表脚注 (:52) 文字相同、相隔 4 行. 未删 (非授权删除), 请主控定是否保留/调序.
- N9-N15 行内 REPLACED 口径 (见上).
- X-1 Ex1 斜体概述按 D2 删扩写删除.

## attempt 1 续 (reviewer CONDITIONAL 必改项, 主控转达)

| # | file:line (before) | 原因 | 保留位置 |
|---|---|---|---|
| X-4 | LB/assumptions.md:56-57 (`> ¹In this column…` 孤儿 LB 规格脚注 + 其后空行) | D2 去重: 与新增通用表脚注 (:52) 逐字相同 | :52 |

- 删后顺序: 通用表 → 脚注 :52 → `## LB – Assumptions` :54 → 假设 1 :56. md5 after: assumptions.md `10a137d1cbad1e7abd1166259dc10b13` (examples.md 不变).
- 复跑: census (同上命令) → OK 4 / DIFF 1 (T-1) / UNPARSEABLE 1, 1 diff / 1040 格, 不变;
  `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root knowledge_base --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → 12 REGRESS 全在 p257-263 (MB, 并行批 B-MB 的改动), LB 回归 0;
  `python3 tools/check_links.py` → `broken relative links: 18668 (live docs: 42)`.
