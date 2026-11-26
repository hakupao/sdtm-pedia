# T2S S-TUFA writer checkpoint (扫描批: TR / FA / SR; §6.3.12.3 共用例 TU 半只读)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base: 本批 9 文件改前 = HEAD (`0d0e813` 起; 期间 HEAD 进到 `8426871` (S-SPC2/S-SPC1), `git diff 0d0e813 HEAD -- domains/{TR,FA,SR,TU}` 为空). 工作区其他域改动属并行批, 未触碰. TU/* 未改.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TUFA_writer/`
  (kbbase/ = `git archive HEAD`; apply.py 精确替换 + 命中次数/块一致断言; scan.py/scan2.py PDF→KB (scan2 附 TU/VS/FA/SR 归属); rscan.py KB→PDF; speccmp_bbox.py (`pdftotext -bbox` 分列逐变量逐字段); vcheck.py (新增行对 layout 逐字); census_before/after.json; census_TU.json; fp_before/after.jsonl; 渲染 r352/355/356/357/358/364/367/369/371/372/373/374/378 (110dpi))
- md5 before → after (前 8 位): TR/assumptions `c4f681f0`→`41c21987` (27→43 行); TR/spec `7d4a72b6`→`9fa2c7dd`; FA/assumptions `7f72cfcc`→`2e130c42` (119→121); FA/spec `64bb7eb6`→`46855aa4`; SR/spec `357560ce`→`9a176e52`.
  未动 (全扫 0 缺口): TR/examples `415debd6`, FA/examples `f7178ec1`, SR/assumptions `07dc4c58`, SR/examples `7a922f67`.

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| domains/TR | §6.3.12.2 | 350-353 | **350-353 上部** | p350 顶即 `6.3.12.2` 标题 (§6.3.12.1 TU 止于 p349); p353 上部 asm 5-8 属 TR, 中部 `6.3.12.3 …Examples` 起共用例节 |
| TR+TU 共用 | §6.3.12.3 | 353-358 | **353 中部-358 上部** | p358 中部 `6.3.13 Vital Signs (VS)` 起别节 (VS 标题/Desc/spec 原子不归本批). TR 份 = Ex2 TR 叙述 (p354 下部) + tr.xpt (p355-356) + relrec (p356); Ex3 TR 叙述 + tr.xpt (p356-358) + relrec (p358). Ex1 全部、Ex2/Ex3 的 TU 叙述/tu/supptu 属 `TU/examples.md` (TU FINAL, 只读核) |
| domains/FA | §6.4 / §6.4.1-6.4.3 引言 + §6.4.4 | 364-375 | **361 下部-375 上部** | §6.4 标题在 p361 下部 (上部 VS Ex 表别节), FA 顶已承载 §6.4-§6.4.3 (B-FA 已补), 一并全扫; §6.4.4 标题 p364 下部; p375 下部 `6.4.5 Skin Response (SR)` 起别节 |
| domains/SR | §6.4.5 | 375-382 | **375 下部-381** | p375 上部 FA Ex6 属 FA; **p382 = `7 Trial Design Model Datasets` / §7.1, 无 SR 内容** → hi 应为 381 (json 多 1 页) |

### 双向全扫 — 逐页日志
方法: PDF→KB = `work/pdf_atoms.jsonl` 该页全部原子 (含 TABLE_ROW/TABLE_HEADER/CODE_LITERAL/NOTE/LIST_ITEM) 归一后查本域三文件 (scan2.py; 未命中再查 TU/VS/FA/SR 定归属), 未命中逐条分类; spec 表以 speccmp_bbox.py 逐变量逐字段为准 (页首行 bbox 漏取的 STUDYID / TRTESTCD / TRDY 人工对 layout). KB→PDF = assumptions/examples 逐句 (rscan.py) 在 layout + 原子中查; 数据表/CRF 对渲染逐格. 计数 = 改后 "该页原子 / 命中 / 本次补齐"; 别节原子单列不计缺口.

| 页 | 节 | PDF→KB: 原子 / 命中 / 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 (未命中分类) |
|---|---|---|---|---|---|
| 350 | §6.3.12.2 标题/Desc/Spec 首句/spec | 26 / 22 / 3→3 (D 标题, Spec 标题+首句) + 列表恢复 | TR/asm:1-19; KB 列表并句 → 恢复 5 bullet | bbox | 未命中: a001 节号标题 (= H1 结构), a017 表头, a020/a021 原子抽取错 (USUBJID "containing" / TRSEQ "or a subject"; layout+bbox = KB "involving" / "for a subject"); DOMAIN `TR` = U6 |
| 351 | spec | 22 / 9 / 0 | spec 一致 | bbox (TRTESTCD 页首人工) | 未命中 13 = U5 C-code 格 (TRTESTCD/TRTEST/TRORRESU/TRSTRESC/TRSTRESU/TRSTAT/TRMETHOD/TRLOBXFL/TRBLFL/TREVAL/TREVALID/TRACPTFL/EPOCH); TR 无 `*` 格 |
| 352 | spec 尾 / 脚注 / asm 1-4 | 10 / 9 / 2→2 (脚注, A 标题) | TR/asm 21-35 一致 | census_item 渲染 (下) | 未命中: a002 脚注 (原子 "1In" 数字上标, KB 照 PDF 写 ¹, 同 S-FND); asm 3 PDF 段内换行 "The sponsor…" KB 同段 (仅段落, 不改) |
| 353 | asm 5-8 / §6.3.12.3 / Ex1 (TU) | TR 4 / 4 / 0; TU 14 | TR/asm 37-43 一致 | — | TU 份 14 原子全在 TU/examples (scan2 归 [TU]); a009 "aorta-iliac" = B-TU T-1 (TU 已登记) |
| 354 | Ex1 supptu / Ex2 (TU) / Ex2 TR 叙述 | TR 5 / 5 / 0; TU 30 | TR/ex:5-13 一致 | — | TU 份 30 原子全在 TU/examples |
| 355 | Ex2 tr.xpt | 27 / 27 / 0 | 一致 | census_item 渲染逐行 (下) | — |
| 356 | Ex2 tr 尾 / relrec / Ex3 (TU) / Ex3 TR 叙述 / tr r1 | TR 15 / 14 / 0; TU 14 | TR/ex:47-70 一致 | 渲染 | a001 = B-TR T-3/T-4 (POOR IMAGEQUALITY 续行属 r26; r27 空) |
| 357 | Ex3 tr.xpt | 25 / 24 / 0 | 一致 | 渲染逐行 | a014 = B-TR T-2 (r15 TRSTRESC -60) |
| 358 | Ex3 tr 尾 / relrec / §6.3.13 (VS) | TR 14 / 14 / 0; VS 12 | TR/ex:95-110 一致 | 渲染 | VS 标题/Desc/spec 原子 12 别节 |
| 361 | VS Ex 表 / §6.4 / §6.4.1 | FA 9 / 7 / 0; VS 9 | FA/asm:1-17 一致 | — | a016/a017 = B-FA T-2 ("6.4.4.," → "6.4.4,") |
| 362 | §6.4.1 | 10 / 6 / 0 | FA/asm:13-39 一致 | — | a002/a006/a008 = B-FA T-2; a010 原子抽取错 ("thought to be", 渲染 "thought be" = KB, B-FA T-4) |
| 363 | §6.4.1 PtC / §6.4.2 | 19 / 18 / 0 | FA/asm:43-65 一致 | — | a008 = B-FA T-5 ("e.g," → "e.g.,") |
| 364 | §6.4.2 尾 / §6.4.3 / §6.4.4 / Desc | 22 / 21 / 0 | FA/asm:67-97 一致 | census_item 渲染 (下) | a020 `6.4.4 Findings About Events or Interventions (FA)` = KB 既有 `## §6.4.4 FA – Description/Overview` 合并标题 (规则 6 不改, 见需主控定 2) |
| 365 | Spec 首句 / spec | 22 / 16 / 2→2 (CT `*` ×2) | 一致 | bbox | 未命中: a004 表头, U5 5 格 (FATESTCD/FATEST/FAORRESU/FASTRESU/FASTAT); DOMAIN `FA` = U6 |
| 366 | spec 尾 / 脚注 / FA – Assumptions / asm 1-4 | 19 / 12 / 2→2 (脚注, A 标题) + 假设 1-6 归位 | FA/asm:103-116 一致 | bbox | 未命中: U5 6 格 (FALOC/FALAT/FALOBXFL/FABLFL/FAEVAL/EPOCH); a013 脚注上标写法 |
| 367 | asm 5-6 / Ex1 CRF | 19 / 19 / 0 | FA/ex:1-22 一致 | census_item 渲染 | — |
| 368 | Ex1 ce/ex/face | 22 / 22 / 0 | 一致 | census OK | — |
| 369 | Ex1 face/relrec / Ex2 CRF | 25 / 25 / 0 | 一致 | census OK + 渲染 | — |
| 370 | Ex2 ae/faae/relrec | 25 / 24 / 0 | 一致 | census OK | a021 = B-FA T-7 (parent CE → AE) |
| 371 | Ex3 CRF / mh | 23 / 23 / 0 | 一致 | census OK + 渲染 | — |
| 372 | suppmh / Ex4 CRF / faae | 29 / 29 / 0 | 一致 | census OK + 渲染 | — |
| 373 | Ex4 ae / Ex5 CRF / face | 29 / 28 / 0 | 一致 | census OK + 渲染 | a013 = B-FA T-9 (FAEVINTX → FAEVLINT) |
| 374 | Ex5 face 尾 / Ex6 CRF | 22 / 22 / 0 | 一致 (:283 D6 KB note, B-FA 已标) | census OK + 渲染 | — |
| 375 | Ex6 / §6.4.5 / SR Desc | 26 / 26 / 0 (FA 24 含 §6.4.5 标题 → FA 导航标题; SR a025/a026 2 在 SR/asm) | FA/ex:285-322; SR/asm:1-5 一致 | census OK | SR a025/a026 在 SR/asm (B-SR 已补); FA/asm:119-121 `## §6.4.5` + 交叉引用 = 导航 |
| 376 | SR Spec 首句 / spec | 26 / 16 / 0 | SR/asm:7-9 一致 | bbox | 未命中: a004 表头, U5 7 格 (SRTESTCD/SRTEST/SRORRESU/SRSTRESU/SRSTAT/SRSPEC/SRLOC), a014 SROBJ = B-SR T-1 (BAU mL), a010 原子抽取错 (原子 "SREFID", PDF/KB SRREFID); DOMAIN `SR` = U6; SR 无 `*` 格 |
| 377 | spec 尾 / 脚注 / SR asm 1-2 | 21 / 12 / 1→1 (脚注) | SR/asm:11-15 一致 | bbox | 未命中: U5 6 格 (SRLAT/SRMETHOD/SRLOBXFL/SRBLFL/SREVAL/EPOCH), a015 SRELTM = B-SR T-4 (EGTPTREF), a016 原子抽取错 (原子 "MANTOUX ADMINISTRATION", layout/KB "INTRADERMAL INJECTION"), a021 = B-SR T-3 (reactogencity) |
| 378 | asm 3-4 / Ex1 / Ex2 叙述 | 21 / 19 / 0 | SR/asm:17-19, SR/ex:1-30 一致 | census_item 渲染 | a017 = B-SR T-1; a020 原子含 PDF 杂空格 "IgG )" (KB "IgG)", 仅空白, 不登记) |
| 379 | Ex2 sr/ex | 23 / 22 / 0 | 一致 | census OK | a009 原子抽取错 (漏 "PAPULES", layout = KB) |
| 380 | Ex2 relrec / Ex3 | 35 / 34 / 0 | 一致 | census OK | a029 原子抽取错 ("IDRLIAM", layout p380:34 = KB IDRLDIAM) |
| 381 | Ex3 ag/relrec | 5 / 5 / 0 | 一致 | census OK | 页尾即 SR 止 |

- spec.md 非变量行 (KB→PDF): H1、`> Class: … | Structure: …`、`---`、`## Cross References` 块 → U8 导航, 不标 D6.
- KB→PDF (rscan.py, 改后) 无出处行全部已分类: TR/ex:3 (TU↔TR 互引, 导航); FA/asm:15/17/23/31/35/50 (= B-FA T-2/T-5 已改正值); FA/asm:121 (§6.4.5 交叉引用, 导航); FA/ex:118/228 (T-7/T-9); FA/ex:283 (D6, 已标); SR/asm:15 (T-3); SR/ex:27 (PDF 杂空格).
- §6.3.12.3 TU 份只读核: `table_census.py --pages ig34:353-356 --kb TU/examples.md` → tu/supptu 5 表全 OK (PDF_ONLY 仅 TR 表, 在 TR/examples); rscan TU/examples 仅 :5 导航与 :13 T-1. TU 无需改.

### spec.md Controlled Terms 逐变量 (bbox 分列 + layout `Char  *\*` grep 三页组)
- `*` 格: PDF 2 = KB 改后 2 (FA: FACAT FASCAT). TR (p350-352) / SR (p376-377) layout grep 与 bbox 均 0 个 `*`.
- 非 CT 字段 (Label/Type/Role/Core/CDISC Notes): TR 32 (STUDYID/TRTESTCD/TRDY 页首行人工) / FA 30 / SR 39 变量, 顺序全同; 唯一差异 = SR SROBJ (B-SR T-1) 与 SRELTM (B-SR T-4), 均既有登记.
- U6 (S-CT, 未改): DOMAIN ×3. U5 (S-CT, 未改): TR 13 / FA 11 / SR 13 格 C-code vs PDF 括号短名.

### census_items 逐格 (渲染 110dpi)
| # | 表 | PDF | 结果 |
|---|---|---|---|
| 1 | TR/assumptions.md:31-33 (HEAD :15) asm 4 例表 | p352 | 表头 8 列 + r1 (T01 / DIAMETER / Diameter / TOO SMALL TO MEASURE / mm / 5 / 5 / mm) 一致 |
| 2 | FA/assumptions.md:83-87 (HEAD :97) FATESTCD/FATEST | p364 | 表头 + OCCUR/SEV/TOXGR 3 行 × 2 格一致 |
| 3 | FA/examples.md:7 Ex1 CRF | p367 | 13 行一致 (表题; xx; 两 DD-MMM-YYYY HH:MM; 3 时点 × (分隔行/Severity/症状 4 项 ○ No ○ Yes)); 症状同格多行 KB 并 1 行, 粗体未保留, 文字无丢 |
| 4 | FA/examples.md:76 Ex2 CRF | p369 | 11 行一致 (Macules…Scars × ○ 0 … ○ >300); 填空线长度属版面 |
| 5 | FA/examples.md:133 Ex3 CRF 上半 | p371 | Date of assessment / Date of diagnosis / "During the past 6 months…" 一致; PDF 为单表 (表题行 + 3 列), KB 拆为 `###` 表题 + 2 表 (基线既有, B-FA review 已核), 文字无丢 |
| 6 | FA/examples.md:138 Ex3 CRF 下半 | p371 | 表头 + 5 症状行一致 (Early morning stiffness 行 "If yes, what was its average daily duration? ___Hours ___Minutes") |
| 7 | FA/examples.md:176 Ex4 CRF | p372 | 一致 (3 症状 PDF 同格 → KB 3 行; ○ No ○ Yes ○ Not Done) |
| 8 | FA/examples.md:219 Ex5 CRF | p373 | 表头 2 行 + 3 症状行 × 5 列一致; 灰底格未表达 |
| 9 | FA/examples.md:263 Ex6 纸质 CRF | p374 | 9 列: 合并标题行 / AE ID…Visit 6 / 3 数据行 ○ Mild ○ Moderate ○ Severe 一致 |
| 10 | FA/examples.md:273 AE 模块 | p374 | 4 列 + 空行一致 |
| 11 | FA/examples.md:279 严重度模块 | p374 | 3 列 + 1 行一致 |
| 12 | SR/examples.md:14 Ex1 sr.xpt | p378 | 8 行 × 17 列: 仅 r7 SROBJ PDF "0.15 BAU mL" / KB "BAU/mL" = **B-SR T-1 沿用**; 其余 135 格一致 |
| 13 | TR/examples.md:17 Ex2 tr.xpt | p355-356 | 27 行逐行一致 (PDF Row 1-11, 13-28 ↔ KB 1-27); 差异仅 Row/TRSEQ 16 行 × 2 = **B-TR T-1 沿用**; r25 TRREASND 跨页 "NOT ASSESSABLE: POOR IMAGEQUALITY" = T-3; r26 (PDF 27) NT01 结果/状态空 = B-TR review T-4 裁定 (PDF 忠实) |
| 14 | TR/examples.md:68 Ex3 tr.xpt | p356-358 | 32 行逐行一致; 仅 r15 TRSTRESC PDF -60 / KB -50 = **B-TR T-2 沿用** |
- table_census.py (本批 manifest, TR hi 改 358): before = after `KB tables 37 / OK 23 / DIFF 3 / UNPARSEABLE 11, cells 3207, diffs 34` (= TR T-1 32 + TR T-2 1 + SR T-1 1). 本批 KB 文件 PDF_ONLY 0 (manifest 页内 PDF_ONLY 均为 TU / VS 别节表).

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | TR/assumptions.md:3 | ig34_p0350_a002 | INSERTED | `## TR – Description/Overview` (gap D) | 350 |
| 2 | TR/assumptions.md:5-7 | ig34_p0350_a003/a004 | REPLACED | Description 首句单独成段 (PDF 两段), 文字不变 | 350 |
| 3 | TR/assumptions.md:7-13 | ig34_p0350_a006..a011 | REPLACED | "…following information: a unique…, test and result, …, and timing information." → 冒号 + 5 项 bullet (去 KB 自加的逗号与 "and") | 350 |
| 4 | TR/assumptions.md:17-19 | ig34_p0350_a015/a016 | INSERTED | `## TR – Specification` + tr.xpt 首句 (gap S) | 350 |
| 5 | TR/assumptions.md:21 | ig34_p0352_a003 | INSERTED | `## TR – Assumptions` (gap A) | 352 |
| 6 | TR/spec.md:294 | ig34_p0352_a002 | INSERTED | `> ¹In this column, …` (最后变量块 `---` 后, Cross References 前; U7) | 352 |
| 7 | FA/assumptions.md:103 | ig34_p0366_a014 | INSERTED | `## FA – Assumptions` (gap A) | 366 |
| 8 | FA/assumptions.md:105-116 | ig34_p0366_a015..p0367_a003 | MOVED | 假设 1-6 (HEAD :3-15, 文件顶 §6.4 之前) 原样移到 `## FA – Specification` 之后、`## §6.4.5` 之前 (= PDF p366-367 顺序) | 366-367 |
| 9-10 | FA/spec.md:90/99 | pdf:p365 CT | REPLACED | FACAT / FASCAT CT 空 → `*` | 365 |
| 11 | FA/spec.md:276 | ig34_p0366_a013 | INSERTED | 脚注 (gap F) | 366 |
| 12 | SR/spec.md:357 | ig34_p0377_a018 | INSERTED | 脚注 (gap F) | 377 |
- 新插入文字逐字核 (vcheck.py): `git diff -U0` 每个 `+` 行去 Markdown 前缀 (¹→1) 后在本域页 layout 文本 (仅空白归一, 不归一 dash/引号) 中查, 全部命中 (en dash – / em dash — 为 PDF 原字符); 唯一不适用 = 2 行 `Controlled Terms: *` (字段值, 由 bbox 核).
- 新增 atom 清单 (gaps 之外): #3 (列表恢复, R2 改写); #8 (顺序归位); #2 (段落拆分随 #1 一并).

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | TR/assumptions.md:3/17/21 | 新增 `## TR – Description/Overview`、`## TR – Specification`、`## TR – Assumptions` | gaps D/S/A (OE/UR/SS 先例) |
| S-2 | TR/assumptions.md:9-13 | 逗号句 → 5 项 bullet 列表 | p350 PDF 为 • 列表 |
| S-3 | FA/assumptions.md:103-116 | 新增 `## FA – Assumptions` + **整条移位**: 假设 1-6 (含 4a/5a) 从文件顶移到 FA – Specification 之后; 块逐字节一致 (apply.py 断言 count==1), 0 字改动 | PDF 顺序: §6.4 (p361) → §6.4.4 Desc (p364) → Spec (p365) → Assumptions (p366-367); 授权 1 挪位 + dispatch "同文件内顺序/归节" 条 |
- 锚点: `grep -rn "FA/assumptions.md#\|TR/assumptions.md#\|SR/assumptions.md#" knowledge_base` 0 处; 既有标题文字均未改.
- 无整条 assumption 增删 / 拆合.

### 删除清单
| # | 位置 | 原因 |
|---|---|---|
| D-1 | FA/assumptions.md HEAD :3-15 | 移位源 (S-3, 先插后删, 不留指针) |
| D-2 | TR/assumptions.md HEAD :3 "…information: a unique…, and timing information." 句尾 | 由 PDF 列表原文替换 (#3), 仅去 KB 自加逗号/"and" |
| D-3 | FA/spec.md:90/99 空 CT | → `*` (U2), 旧值替换 |
- 无 D2 删除, 无 "PDF 无此条" 整条删除.

### D6 / KB_AUTHORED
- 无新增 D6. 既有: FA/examples.md:283 `> KB note (not in SDTMIG):` (B-FA 已标, 内容与 p374-375 不矛盾). 纯导航保留: TR/examples.md:3 TU↔TR 互引 + `## Example 2/3 (continued from TU)` 标题; FA/assumptions.md:119-121 `## §6.4.5 Skin Response (SR)` + `> See …` 交叉引用 (B-SR #21); 各 spec.md `> Class|Structure` 行与 Cross References (U8).

### PDF_TYPO (全部沿用, 本批无新增)
| T | 位置 | 状态 |
|---|---|---|
| TR T-1 | TR/ex Ex2 Row/TRSEQ 跳 12 (32 格) | KB 连续值, 沿用 (`t2_B-TR.md`); p355-356 渲染复核成立 |
| TR T-2 | TR/ex:84 Ex3 r15 TRSTRESC -60 | KB -50, 沿用; p357 渲染复核 |
| TR T-3 / T-4 | TR/ex:43 "POOR IMAGEQUALITY" / :44 NT01 空 | 沿用 (T-4 已由 B-TR review 裁定 PDF 忠实) |
| TU T-1 | TU/ex:13 aorta-iliac (TU 文件, 只读) | 沿用 (`t2_B-TU.md`) |
| FA T-1..T-10 | FA/asm §6.4.1, FA/ex | 沿用 (`t2_B-FA.md` + 续); T-2/T-5/T-7/T-9 KB 改正值, T-3/T-4/T-6/T-8/T-10 照录 T4 |
| SR T-1..T-4 | SR/ex:22 + SR/spec SROBJ (BAU mL); SR/ex Ex3 SRDTC (T4); SR/asm reactogencity; SR/spec SRELTM EGTPTREF | 沿用 (`t2_B-SR.md`) |
- 观察 (未登记, 未改): p351 TAETORD CDISC Notes "Epoch associated with the date/time at which the assessment was made." 与变量 Label (Planned Order of Element within Arm) 不符 (FA/SR 同变量为 "Number that gives the planned order…"); KB = PDF 照录. 见需主控定 1.

### 范围外 / out_of_scope
- json out_of_scope 为空. 新范围外: 无.
- 原子抽取错 (T3 台账): ig34_p0350_a020/a021, p0362_a010, p0376_a010, p0377_a016, p0378_a020 (杂空格), p0379_a009, p0380_a029.

### 需主控定
1. TR/spec.md TAETORD CDISC Notes 照录 PDF p351 (内容像是抄自另一变量); 是否按 "PDF 自身可定" 改为 FA/SR 同变量措辞并登记 T-n, 还是照录 + T4 用户裁. 本批未改.
2. FA/assumptions.md:95 既有标题 `## §6.4.4 FA – Description/Overview` 合并了 PDF 两级标题 (`6.4.4 Findings About Events or Interventions (FA)` + `FA – Description/Overview`); 规则 6 禁改标题文字, 未动.
3. S-TUFA.json SR `pdf_ranges`/sections hi=382 应为 381 (p382 = §7); TR sections hi=353 仅指 §6.3.12.2, 本批 TR 全扫用 350-358 (manifest 已按此改).

### 验证命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TUFA_writer
for p in 350 351 352 365 366 376 377; do pdftotext -f $p -l $p -bbox "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/bb_$p.html; done
python3 -I $S/speccmp_bbox.py $S TR 350,351,352 | grep -v " OK$"; python3 -I $S/speccmp_bbox.py $S FA 365,366 | grep -v " OK$"; python3 -I $S/speccmp_bbox.py $S SR 376,377 | grep -v " OK$"   # 仅余 ct: U5/U6 + SR T-1/T-4
python3 -I $S/scan2.py TR 350 358 TU,VS; python3 -I $S/scan2.py FA 361 375 VS,SR; python3 -I $S/scan2.py SR 375 381 FA
D=knowledge_base/domains; python3 -I $S/rscan.py TR 350 358 $D/TR/assumptions.md $D/TR/examples.md; python3 -I $S/rscan.py FA 361 375 $D/FA/assumptions.md $D/FA/examples.md; python3 -I $S/rscan.py SR 375 381 $D/SR/assumptions.md $D/SR/examples.md
python3 -I $S/vcheck.py     # 新增行逐字 (仅 2 行 CT * 不适用)
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 23 / DIFF 3 / UNPARSEABLE 11, diffs 34 (全 T-n)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbbase/knowledge_base --out $S/fp_before.jsonl; python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl
#  本批页 (p350-358, 361-381) 台账原子 389: 回归 0, 新命中 0. 全量另有 8 条回归在 p199-255 (kbbase 早于已提交的 S-SPC1/S-SPC2, 非本批)
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/FA/assumptions.md | 30 ++++++++++++++++--------------
 knowledge_base/domains/FA/spec.md        |  6 ++++--
 knowledge_base/domains/SR/spec.md        |  2 ++
 knowledge_base/domains/TR/assumptions.md | 18 +++++++++++++++++-
 knowledge_base/domains/TR/spec.md        |  2 ++
 5 files changed, 41 insertions(+), 17 deletions(-)
```
- writer.jsonl: `work/t2_batches/S-TUFA.writer.jsonl` 26 行 (改动 12 项; census_items 14 行 VERIFIED / SKIPPED_PDF_TYPO).

## attempt 1 delta (主控裁定后, 2026-11-26)
- 裁定: (1) TAETORD 照录 + T-n (T4); (2) FA `## §6.4.4 FA – Description/Overview` 合并标题按规则 6 不改, 仅记录; (3) json 已由主控改 (SR hi=381, TR 350-358). **KB 未改** (TR/spec md5 仍 `9fa2c7dd`).

| T | 位置 | PDF | KB | 依据 | 状态 |
|---|---|---|---|---|---|
| TR T-5 (新, T4) | TR/spec.md:264 TAETORD CDISC Notes | p351 "Epoch associated with the date/time at which the assessment was made." | 照录 PDF | 与同行 Label "Planned Order of Element within Arm" 不符; 正确措辞无法仅由该表唯一确定. 候选值 = 他域 TAETORD Notes PDF 原文 "Number that gives the planned order of the element within the arm." (p366 FA, p377 SR) | 照录, **T4 用户裁定** |
- 复跑: `grep -n "TAETORD" -A1 .work/10_tier_b_repair/work/pdf_pages/ig34_p03{51,66,77}.txt`
