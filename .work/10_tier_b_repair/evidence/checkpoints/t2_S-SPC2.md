# T2S S-SPC2 writer checkpoint (扫描批: MB / MS / PC / PP)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `056d8cc`; 本批 12 文件改前与 HEAD 一致 (`git show HEAD:` 逐个 cmp). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPC2_writer/`
  (base/ = HEAD 副本; kbbase/ = `git archive HEAD`; apply_spc2.py 精确替换 + 命中次数断言; speccmp.py = bbox 词框分列逐变量逐字段; scan2.py = 原子 PDF→KB; lscan.py = layout 文本逐句 PDF→KB; rscan2.py = KB→PDF (仅 layout 页文本, 按域页范围); census_before/after.json; fp_before/after.jsonl; 渲染 p257/262/263/274/277/278 (110dpi) + p249/253/268/271 (90dpi))
- md5 after: MB/assumptions `a598140f…` (30→34 行); MB/spec `b3f7f47b…` (458→460); MS/assumptions `13db4f98…` (31→29); MS/examples `fd8a948c…` (81, 行数不变); MS/spec `79fa4aa2…` (587→589); PC/assumptions `f00ae3ee…` (119→123); PC/examples `ecbea2a1…` (497); PC/spec `74e05018…` (396→398); PP/assumptions `44564a3d…` (14→24); PP/examples `005a5c03…` (170); PP/spec `78c05498…` (264→266). MB/examples `a5b39219…` 未动.

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| domains/MB | §6.3.5.7 引言 + §6.3.5.7.1 | 248-252 | **248-252** | p248 上部 LB Ex4/Ex5 (a001-a022) 属 §6.3.5.6, 不归本批; §6.3.5.7 标题 a023 起; p252 中部 §6.3.5.7.2 标题 a015 止 |
| domains/MS | §6.3.5.7.2 | 252-256 | **252-256** | p256 中部 §6.3.5.7.3 标题 (a009) 止 |
| domains/MB+MS | §6.3.5.7.3 | 256-267 | **256-263** | p263 下部 `6.3.5.8 Microscopic Findings (MI)` (a028) 起为 MI; p264-266 全页、p267 上部 (a001-a015 MI Ex3) 均属 MI, 不归本批 |
| domains/PC | §6.3.5.9 / §6.3.5.9.1 | 267-271 | **267-271** | §6.3.5.9 标题 p267 a016 (下方直接 §6.3.5.9.1 标题, **§6.3.5.9 无引言正文, 0 原子确认**); p271 中部 §6.3.5.9.2 (a013) 止 |
| domains/PP | §6.3.5.9.2 | 271-275 | **271-275** | p275 中部 §6.3.5.9.3 (a012) 止 |
| domains/PC+PP | §6.3.5.9.3 | 275-285 | **275-284** | p285 首行即 `6.3.6 Morphology (MO)` → p285 无本节内容 |

### 双向全扫 — 逐页日志
方法: PDF→KB = 叙述以 lscan.py (layout 页文本逐句) 为准, 原子 scan2.py 辅助; 表格以 census (bbox) + 渲染为准; spec 表以 speccmp.py (bbox 词框分列, 逐变量逐字段) 为准. KB→PDF = rscan2.py (按域页范围, 仅 layout 文本, 不混原子) + speccmp 反向 (KB 变量集合 = PDF). 计数为改后; "原子数/命中" 为本节原子 (别节原子不计).
原子错 (atom verbatim 与 layout/渲染不符) 单列, 不算 KB 缺口.

| 页 | 节 | PDF→KB: 原子数 / 命中 / 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 248 | §6.3.5.7 引言 / §6.3.5.7.1 Description | 4 / 3 / 3 句→已补 (a024 原 PARTIAL) | MB/asm 1-9 全有出处 | — | a025 `6.3.5.7.1 …` = MB H1 结构等价; LB 别节 22 原子不计 |
| 249 | MB Spec 首句 / spec | 21 / 14 / 2→2 (S 首句 + 标题; CT `*` 2) | spec STUDYID..MBSTRESC 逐字段一致 | speccmp 17 变量; 渲染 90dpi (`*` 2 格) | 未命中: a003 表头 (结构等价); a010 MBREFID / a019 MBORRES = 原子错 (渲染: 无 "a"、含 KLEBSIELLA, KB=渲染); 其余 = C-code (U5) / DOMAIN (U6) |
| 250 | spec | 25 / 12 / 0 | 一致 | speccmp 25 变量 | 13 未命中全为 C-code (U5) |
| 251 | spec 尾 / 脚注 / asm 1-2 | 30 / 27 / 1→1 (脚注 a005) | MB/asm 1-2 一致 | speccmp 5 变量 | a002 MBELTM 原子错 (layout = KB); a005 = ¹/1 上标写法; a022 原子错 ("; " vs ", ", layout = KB) |
| 252 | asm 3-4 / §6.3.5.7.2 / MS Description / Spec / spec | 30 / 23 / 0 | MB/asm 3-4、MS/asm 1-9 一致 | speccmp 9 变量 | a011 原子错 ("assigned to" vs layout "assigned in" = KB); a015 = MS H1; a025/a026/a029/a030 原子错 (speccmp 逐字段一致) |
| 253 | MS spec | 36 / 25 / 2→2 (CT `*` MSCAT/MSSCAT) | 一致 | speccmp 18 变量; 渲染 90dpi | 未命中 = C-code (U5) + 原子错 (MSSTAT/MSSTRESC 等, speccmp 一致) |
| 254 | MS spec | 48 / 33 / 0 | 一致 | speccmp 24 变量 | 未命中 = C-code (U5) 14 + MSANMETH 原子错 |
| 255 | MS spec 尾 / 脚注 / asm 1 | 42 / 41 / 1→1 (脚注由 asm MOVED 到 spec) | 一致 | speccmp 10 变量 | a021 = ¹/1 上标写法 |
| 256 | MS asm 1.b.i-5 / §6.3.5.7.3 / Ex1 | 23 / 22 / 0 | MS/asm、MB/ex Ex1 一致 | mb.xpt census OK | a007 = MS T-5 (PDF 漏 "be") |
| 257 | Ex1 / Ex2 | 30 / 30 / 0 | MS/ex Ex1、MB/ex 一致 | ms.xpt 渲染逐格 (下); relrec/be census OK | MS/ex:11 跨 p256-257 句渲染一致 |
| 258 | Ex2 | 29 / 29 / 0 | 一致 | census OK | |
| 259 | Ex2 / Ex3 | 21 / 21 / 0 | 一致 | census OK | |
| 260 | Ex3 | 36 / 36 / 0 | 一致 | census OK | |
| 261 | Ex3 | 18 / 18 / 0 | 一致 | census OK | MB T-4 (sputum) 照录 |
| 262 | Ex3 | 30 / 30 / 0 | MS/ex:65 MSCONCU = MS T-2 | suppmb/ms/suppms 渲染逐格 (下) | |
| 263 | Ex3 尾 / Ex4 | 27 / 26 / 0 | 一致 | di/relrec census OK; Ex4 mb/suppmb 渲染逐格 (下) | a020 表头 = MB T-2/T-3; a028 起 MI 别节 |
| 264-266 | (MI) | 别节 | — | — | 全页 §6.3.5.8 |
| 267 | §6.3.5.9 / PC Description / Spec / spec | 13 / 11 / 2→2 (a018 标题 + a019 句, gap D) | PC/asm 1-9 有出处 (:5 → D6) | speccmp 6 变量 | a017 = PC H1; a022 表头结构等价 |
| 268 | PC spec | 19 / 10 / 2→2 (CT `*` PCCAT/PCSCAT) | 一致 | speccmp 19 变量; 渲染 90dpi | 未命中 = C-code (U5) + a003 PCTEST 原子错 |
| 269 | spec 尾 / 脚注 / asm / PC – Examples | 23 / 21 / 1→1 (脚注 a017) | PC/asm 1-3、PC/ex:7 一致 | speccmp 16 变量 | a017 = ¹/1 上标写法 |
| 270 | PC Ex1 | 32 / 12 / 0 | PC/ex:9-23 一致 | pc.xpt census OK | 20 未命中 = 原子错 (A854134, census bbox = KB A554134) |
| 271 | PC Ex1 尾 / §6.3.5.9.2 / PP Description / Spec / spec | 30 / 13 / 4→4 (a014-a017, gaps D/S) + CT `*` 2 | PP/asm 1-9 有出处 | pc.xpt census OK; speccmp; 渲染 90dpi | 12 pc 行原子错 ("A554134- 19" 分词); a013 = PP H1; a025/a026/a030 = C-code |
| 272 | PP spec 尾 / 脚注 / asm 1-3 | 23 / 18 / 2→2 (脚注 a016 + `## PP – Assumptions` a017) | PP/asm 一致 | speccmp 10 变量 (STUDYID/PPSTRESC bbox 漏读, 改用 layout 文本核: 一致) | 未命中 = C-code (U5) |
| 273 | asm 4-5 / PP – Examples / Ex1 / Ex2 | 37 / 36 / 0 | PP/ex 原 :5 "Due to space limitations…" 无出处 → 删 (S-1) | Ex1 pp census OK | a037 = PCPP T-9 (pre-corrdinating) |
| 274 | Ex2 / Ex3 | 29 / 28 / 0 | 一致; `**supppp.xpt**` 表前短标签 (PDF 无, 纯导航, B-PCPP O-d) | Ex2 pp + supppp 渲染逐格 (下); Ex3 census OK | a021 = T₁/T₂ 下标 vs KB T1/T2 (排版) |
| 275 | Ex3 尾 / §6.3.5.9.3 | 29 / 29 / 0 | PC/asm 23-49 一致 | relrec census OK | |
| 276 | PC dataset | 30 / 27 / 0 | 一致 | pc.xpt census OK | 3 未命中 = 原子错 (census OK) |
| 277 | PP dataset / Ex1 A / B | 30 / 30 / 0 | 一致 | pp census OK; Method A relrec 渲染逐格 (下) | |
| 278 | Ex1 B / C / D | 60 / 59 / 1→1 (Rows 1-19 句, 改正) | PC/ex:146 原有扩写 → 改 (#15) | Method B relrec 渲染逐格 (下); C/D census OK | a051 原子 verbatim = 旧错 KB 文本 (fp 预期回归) |
| 279 | Ex1 D 尾 / Ex2 A / B | 57 / 57 / 0 | PC/ex:213 `"10" through "12"` vs PDF 缺开引号 = T-10 | census OK | |
| 280 | Ex2 C / D / Ex3 A | 47 / 46 / 1→1 (Method D 句引号) | PC/ex:250 改 (#16, T-11) | census OK | a014 原子 verbatim = 旧错 KB 文本; T-8/T-8b 照录 |
| 281 | Ex3 B / C / D | 54 / 54 / 0 | 一致 (PDF "PP records with PCSEQ"、"PGRPID" 照录) | census OK | |
| 282 | Ex3 D 尾 / Ex4 A | 52 / 52 / 0 | 一致 | census OK | |
| 283 | Ex4 A 尾 / D | 58 / 58 / 0 | 一致 | census OK | |
| 284 | Ex4 D 尾 / Conclusions / Suggestions | 15 / 15 / 0 | PC/asm 101-123 一致 | census OK | |
| 285 | (MO) | 别节 | — | — | |

- spec.md 非变量行 (KB→PDF): H1、`> Class: … | Structure: …`、`---`、`## Cross References` 块 = 纯导航 (U8), 不标 D6.
- 四域 spec 变量集合与 PDF 一致 (MB 47 / MS 61 / PC 41 / PP 26), 顺序一致; Label/Type/Role/Core/CDISC Notes 全一致; CT 列剩余差异仅 DOMAIN (U6) 与 C-code 记法 (U5), 归 S-CT 批.
- lscan.py 的叙述级残留 (全部已逐条核): 表名粘连、跨页/跨行 "--\nLNKID"、"organisms—\nincluding" 换行伪差、MS T-5、MS T-2、PCPP T-9/T-10; 余 0.

### spec.md Controlled Terms `*` (PDF `*` 格; layout `grep "Char \*"` + 渲染)
| 域 | 变量 | PDF 页 | KB 改后行 |
|---|---|---|---|
| MB | MBCAT / MBSCAT | 249 | spec.md:126 / :135 |
| MS | MSCAT / MSSCAT | 253 | spec.md:144 / :153 |
| PC | PCCAT / PCSCAT | 268 | spec.md:90 / :99 |
| PP | PPCAT / PPSCAT | 271 | spec.md:72 / :81 |
- `grep -c "Char \*"` 在 p249-255/267-272 合计 8, 与上表 8 格一致.

### census_items 逐格 (渲染, 110dpi)
| 表 | 渲染 | 结果 |
|---|---|---|
| MB/examples.md:198 suppmb Ex3 p262 | p262 | 6 行 × 10 列逐格一致, 仅 Row 列 PDF 1,2,3,4,7,8 / KB 5,6 = MB T-1 (复核成立) |
| MB/examples.md:241 Ex4 mb p263 | p263 | 2 行 × 23 列逐格一致; 表头 PDF MBGPRID / MBTRESN = MB T-2 / T-3 (KB MBGRPID / MBSTRESN, 复核成立) |
| MS/examples.md:21 Ex1 ms p257 | p257 | 10 行 × 22 列逐格一致, 仅 r9 MSSTRESC PDF 空 / KB 25 = MS T-1 |
| MS/examples.md:78 suppms Ex3 p262 | p262 | 2 行 × 10 列一致, 仅 IDVAR PDF MBREFID / KB MSREFID = MS T-3 (keep-correct); QNAM MSMEDTYPE 照录 (MS T-4) |
| PC/examples.md:75 Ex1 Method A relrec p277 | p277 | 4 行 × 8 列一致, 仅 r3 IDVAR PDF PPGRPID / KB PCGRPID = PCPP T-1 |
| PC/examples.md:89 Ex1 Method B relrec p278 | p278 | 26 行 × 8 列一致 (RELID 全为 1, 照 PDF = T-4 文字/表矛盾照录); r13/r26 RDOMAIN PDF PC / KB PP = T-2/T-3 |
| PP/examples.md:52 Ex2 pp p274 (NO_PDF, 改前 :54) | p274 | 7 行 × 20 列逐格一致, 仅 r6/r7 PPSEQ PDF 1/2 / KB 6/7 = PCPP T-5 |
| PP/examples.md:66 supppp p274 (改前 :68) | p274 | 7 行 × 11 列逐格一致 (r7 QORIG 空); 表头 PDF DOMAIN / KB RDOMAIN = T-6; census 其余 34 diffs = 居中表解析器列错位 |
| PP/examples.md:120 Method 映射表 (UNPARSEABLE, KB_AUTHORED) | p275-276 方法列表 | 4 行 A/B/C/D × 基数/PC 侧/PP 侧 IDVAR 与 PDF 列表一致; 现处于 :114 D6 标注范围内 |
- table_census.py (pdf_ranges): before = after `KB 表 44: OK 35 / DIFF 7 / NO_PDF 1 / UNPARSEABLE 1, diffs 44`; DIFF 7 全为上表登记项 (含 PCPP T-6 + 解析器 34).

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | MB/assumptions.md:5 | ig34_p0248_a024 | INSERTED | §6.3.5.7 引言段末追加 3 句 (MB domain is used for… / MS is used for… / All non-host…—…—…); 原首句不动 | 248 |
| 2 | MB/assumptions.md:11-13 | ig34_p0249_a001/a002 | INSERTED | `## MB – Specification` + spec 首句 (gap S; CM 先例) | 249 |
| 3-4 | MB/spec.md:126/:135 | pdf:p249 MBCAT/MBSCAT CT | REPLACED | Controlled Terms 空 → `*` | 249 |
| 5 | MB/spec.md:429 | ig34_p0251_a005 | INSERTED | `> ¹In this column…` (U2/U7, `---` 后、Cross References 前; gap F) | 251 |
| 6-7 | MS/spec.md:144/:153 | pdf:p253 MSCAT/MSSCAT CT | REPLACED | 空 → `*` | 253 |
| 8 | MS/spec.md:555 | ig34_p0255_a021 | MOVED | 脚注由 MS/assumptions.md (base :11) 迁入 spec.md (U2 footnote_moves); 上标 `1In` → `¹In` (PDF 为上标) | 255 |
| 9 | MS/assumptions.md (base :11-12) | ig34_p0255_a021 (源) | DELETED | 先插后删, 迁移源行 + 空行 | 255 |
| 10 | PC/assumptions.md:5 | KB_AUTHORED | REPLACED | "This section covers the PC and PP domains." 加 `> KB note (not in SDTMIG):` 前缀 (D6; p267 §6.3.5.9 无正文) | 267 |
| 11 | PC/assumptions.md:7-9 | ig34_p0267_a018/a019 | INSERTED | `## PC – Description/Overview` + 定义句 (gap D) | 267 |
| 12-13 | PC/spec.md:90/:99 | pdf:p268 PCCAT/PCSCAT CT | REPLACED | 空 → `*` | 268 |
| 14 | PC/spec.md:375 | ig34_p0269_a017 | INSERTED | 脚注 (gap F) | 269 |
| 15 | PC/examples.md:146 | pdf:p278 Method D Rows 1-19 (原子 ig34_p0278_a051 抄自旧 KB) | REPLACED | 删 KB 多出的 `and "10" through "12"` 与 "individual" (PP 前), `"1 through 7"` → `"1" through "7"` = p278 原句 (渲染确认) | 278 |
| 16 | PC/examples.md:250 | pdf:p280 Ex2 Method D | REPLACED | `"1 through 7"` → `"1" through "7"` (PDF `"1 through "7"`, 见 T-11) | 280 |
| 17 | PC/examples.md:213 | pdf:p279 Ex2 Method B | SKIPPED_PDF_TYPO | KB `"10" through "12",` 保留 (PDF 缺开引号, T-10) | 279 |
| 18 | PP/assumptions.md:3-11 | ig34_p0271_a014..a017, ig34_p0272_a017 | INSERTED | `## PP – Description/Overview` + 句; `## PP – Specification` + spec 首句; `## PP – Assumptions` (gaps D/S/A) | 271-272 |
| 19-20 | PP/spec.md:72/:81 | pdf:p271 PPCAT/PPSCAT CT | REPLACED | 空 → `*` | 271 |
| 21 | PP/spec.md:240 | ig34_p0272_a016 | INSERTED | 脚注 (gap F) | 272 |
| 22 | PP/examples.md (base :5-6) | S-1 | DELETED | "Due to space limitations, …" 整句删 (见结构改动 S-1) | 273 |
| 23 | PP/examples.md:106 | O14 / KB_AUTHORED | REPLACED | "The shared PP dataset contains 12 rows …" 加 D6 前缀 | 277 |
| 24 | PP/examples.md:114 | O14 / KB_AUTHORED | INSERTED | 快速参考节标题下加一行 D6 标注, 声明范围 = 该标题至文件末尾全部 (映射表/row form/改写的 Rows 说明/节选 relrec) | 275-279 |
| 25-27 | MS/examples.md:3, PC/examples.md:3, PP/examples.md:3 | KB_AUTHORED | REPLACED | `*Note: … share a combined examples section …*` → `> KB note (not in SDTMIG): …` (文字不变; EX/examples.md:3 先例) | — |
- 新增 atom 清单 (R3, gaps 之外): #15 #16 (p278/p280 叙述改正). 其余均属 gaps / intro (§6.3.5.7 PARTIAL) / footnote / footnote_moves / O14.

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | PP/examples.md base :5 (+ 空行) | 删 "Due to space limitations, not all expected or permissible findings variables are included…" | PDF p273 `PP – Examples` 标题后直接 `Example 1`; `grep -n "space limitations" ig34_p0271..0275.txt` 0 命中, 全批页范围仅 p269:47 (PC – Examples, 已在 PC/examples.md:7). 属 PC 句误挂 PP → 授权第 1/3 条 "PDF 无此条" 删除 |
| S-2 | MB/assumptions.md:11; PC/assumptions.md:7; PP/assumptions.md:3/7/11 | 新增 5 个 `## XX – …` 标题 | gaps D/S/A; CM/DS 先例 |
| S-3 | MS 脚注 | assumptions → spec (MOVED) | U2 footnote_moves |
| S-4 | MS/PC/PP examples.md:3 | 斜体 Note → D6 引用块 | D6 (B-MS 曾按纯导航保留; 本批统一按 EX 先例标注, 见需主控定 #3) |
| S-5 | PP/examples.md:114 | 新增 D6 范围标注行 | O14 |

### 删除清单
| # | 原位置 (base) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | PP/examples.md:5-6 | 无 | S-1, PP 节 PDF 无此句 | PDF 原句在 PC/examples.md:7 (p269) |
| D-2 | MS/assumptions.md:11-12 脚注 | MS/spec.md:555 | MOVED 源行 | MS/spec.md:555 |
| D-3 | PC/examples.md:146 `and "10" through "12"` / "individual" | 无 | VALUE_DIFF 旧值替换 (KB 从 Ex2 句串入) | — |
| D-4 | spec 8 格 CT 空值 | `*` | U2 | — |

### D6 / KB_AUTHORED
| 位置 | 内容 | 处理 |
|---|---|---|
| PC/assumptions.md:5 | §6.3.5.9 下 KB 自写概述句 | D6 前缀 (不矛盾: §6.3.5.9 下确为 PC、PP 两域) |
| PP/examples.md:106 | 共享 PP 表概述 (12 行 / Day 1、8 / 4 列 PPGRPID) | D6 前缀 (不矛盾, p277 表核) |
| PP/examples.md:114-170 | §6.3.5.9.3 PP 侧快速参考全节 | :114 一行 D6 标注, 范围到文件末尾 (B-PCPP C-5..C-15 已逐条核不矛盾; D-3/D-4/D-5 矛盾句已删) |
| MS/PC/PP examples.md:3 | 合并 examples 节说明 | D6 前缀 |
| MS/examples.md:9 | 既有 D6 | 不变 |
- 纯导航保留不标: MB/examples.md:20/:91/:207、MS/examples.md:7/:36/:60、PP/examples.md:108 (`> See […](…)` 交叉引用); PP/examples.md:110 斜体导航句; PP/examples.md:64 `**supppp.xpt**` 表前短标签; 四域 spec `> Class|Structure` 行与 Cross References (U8).
- O14 (B-PCPP 的 PP/examples.md KB_AUTHORED 回补 D6) → 本批 #23/#24 关闭.

### PDF_TYPO (复核沿用编号; 新增 2)
- MB (t2_B-MB): T-1 suppmb Row 7/8→5/6; T-2 MBGPRID; T-3 MBTRESN→MBSTRESN; T-4 "sputum" 照录 — p262/p263 渲染复核成立.
- MS (t2_B-MS): T-1 r9 MSSTRESC 25; T-2 MSCONU→MSCONCU (MS/examples.md:65); T-3 suppms IDVAR→MSREFID; T-4 QNAM MSMEDTYPE 照录; T-5 "should only populated" (MS/assumptions.md:27) — 复核成立.
- PCPP (t2_B-PCPP): T-1..T-9 (含 T-8b) 复核成立 (T-1/T-2/T-3/T-5/T-6 渲染; T-4 p277 文字 vs p278 表 RELID 全 1 渲染确认; T-8/T-8b/T-9 layout).
- **PCPP T-10 (新)**: PC/examples.md:213 (p279 Ex2 Method B) PDF `"10" through 12",` 缺开引号; KB 保留 `"10" through "12",` — 依据: 同句前半 `"1" through "7"`、p280 同型句均成对引号, 可由 PDF 自身确定.
- **PCPP T-11 (新)**: PC/examples.md:250 (p280 Ex2 Method D) PDF `"1 through "7"` (引号错位); KB 原为 `"1 through 7"` (亦非 PDF), 改为正确值 `"1" through "7"` — 依据: p278 Ex1 Method D 同型句 `"1" through "7"`、p280 Method C 同例同 PP 集合 `"1" through "7"`.
- 未登记的排版差: p274 Ex3 T₁/T₂ 下标 vs KB T1/T2 (非 U1/U4 字符类, 不改); MB asm 1.a.i/1.c.ii 弯引号 (U1, 归 S-TYPO).

### 范围外 / out_of_scope 处理
- O14 → 关闭 (见上). 批次 out_of_scope 列表为空.
- 新范围外: 无. 原子抽取错 (供 T3 台账): ig34_p0249_a010/a019, p0251_a002/a022, p0252_a011/a025/a026/a029/a030, p0253_a031 等 MS spec 行, p0268_a003, p0270_a013..a032, p0271_a001..a012, p0276_a009/a014/a017, p0278_a051, p0280_a014 (后两条 verbatim 抄自旧错 KB).

### 需主控定
1. PP/examples.md:112 标题 `## §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)`: KB 自写标题带真实节号; 规则 6 未改. 备选: 去节号, 或按 "KB 自写摘要与 PDF 重复 → 交叉引用" 整节换一行指针 (本批按 O14 走 D6 保留).
2. MB/examples.md:3 标题 "Microbiology Specimen **and** Microbiology Susceptibility Examples" vs PDF "…Specimen**/**Microbiology…"; 规则 6 未改.
3. 三处 `*Note:*` 改 D6 (S-4) 与 B-MS "纯导航保留" 先例不一致, 请确认统一口径.
4. T-11 取 "正确值" 而非照录 PDF 错位引号, 请确认.

### fp_match (before = kbbase HEAD; after = 工作区, 含并行批改动)
- 汇总 hit_target 4041 → 4041, hit_any 4701 → 4701 (并行批增减抵消, 未拆).
- 本批相关逐原子变化: 新命中 ig34_p0248_a024 (any → MB/assumptions)、ig34_p0267_a019 (target → PC/assumptions); 预期回归 2: **ig34_p0255_a021** (target MS/assumptions → None; 脚注已 MOVED 到 MS/spec.md, ledger 目标待 T3 改指) 、**ig34_p0278_a051** (verbatim = 旧错 KB 文本, KB 已按 p278 渲染改正). 其余脚注类原子 hit_any 由 MS/assumptions 转为 PC/spec (同文异处, 仍命中). EG/CP/IS/LB/GF 变化来自并行批.

### 验证命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPC2_writer
for d in MB:249,250,251 MS:252,253,254,255 PC:267,268,269 PP:271,272; do python3 -I $S/speccmp.py $S ${d%%:*} ${d#*:} | grep -v " OK$"; done   # 剩 DOMAIN (U6) + C-code (U5); PP STUDYID/PPSTRESC bbox 漏读
K=knowledge_base/domains
python3 -I $S/rscan2.py 248-252,256-263 $K/MB/assumptions.md $K/MB/examples.md   # 同式: MS 252-263 / PC 267-271,275-284 / PP 271-284
python3 -I $S/lscan.py MB,MS 248 263 ; python3 -I $S/lscan.py PC,PP 267 284   # layout 逐句 PDF→KB
python3 -I $S/scan2.py MB,MS 248 263 ; python3 -I $S/scan2.py PC,PP 267 284     # 原子 PDF→KB
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # OK 35 / DIFF 7 / NO_PDF 1 / UNPARSEABLE 1, diffs 44 (全 T-n)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbbase/knowledge_base --out $S/fp_before.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat (本批 12 文件)
```
 knowledge_base/domains/MB/assumptions.md |  6 +++++-
 knowledge_base/domains/MB/spec.md        |  6 ++++--
 knowledge_base/domains/MS/assumptions.md |  2 --
 knowledge_base/domains/MS/examples.md    |  2 +-
 knowledge_base/domains/MS/spec.md        |  6 ++++--
 knowledge_base/domains/PC/assumptions.md |  6 +++++-
 knowledge_base/domains/PC/examples.md    |  6 +++---
 knowledge_base/domains/PC/spec.md        |  6 ++++--
 knowledge_base/domains/PP/assumptions.md | 10 ++++++++++
 knowledge_base/domains/PP/examples.md    |  8 ++++----
 knowledge_base/domains/PP/spec.md        |  6 ++++--
 11 files changed, 44 insertions(+), 20 deletions(-)
```
- writer.jsonl: `work/t2_batches/S-SPC2.writer.jsonl`. action `DELETED` / `VERIFIED` 语义同 S-EVT.

### 更正 (同 attempt, 自查后)
- lscan.py 已在改后工作区重跑 (`$S/lscan_after_MBMS.txt` / `$S/lscan_after_PCPP.txt`). 残留全部已归类: 别节 (p248 LB Ex4/Ex5、p263 下部与 p267 上部 MI); spec 表列文字粘连 (p249-255/267-272, 以 speccmp 为准); 标题与首句/表名粘连 (§6.3.5.7.1、MB/MS/PC/PP – Specification 行、`Method X … Rows n:`); 换行伪差 (p248 "organisms—\nincluding"、"--\nLNKID"); 登记 typo: MS T-5 (p256)、MS T-2 (p262)、PCPP T-9 (p273)、T-10 (p279)、**T-11 (p280, 改后 KB 为正确值, 故 lscan 现报该句)**. 无未归类残留. 上文 "lscan 残留 … 余 0" 一句以此为准.
- U+2011 检查: `grep -c "‑"` p248/p249/p267/p271/p272 均 0 → 本批插入句 (drug-susceptibility / non-host / time-concentration / concentration-time) 的连字符与 PDF 同为 U+002D.
- 逐页日志更正: p249 speccmp 变量 **18** (非 17); p251 **4** (非 5); p271 **11** (bbox 10 + STUDYID 用 layout 核); p272 **15** (bbox 14 + PPSTRESC 用 layout 核). p269 未命中 a006 = EPOCH C-code (U5); p271 a019 = 表头 (结构等价).
- MB T-4 ("sputum", p261) 为 layout 文本复核, 非 p262/p263 渲染.
- 变更计数: 编号 27 项 = 实改 26 + SKIPPED_PDF_TYPO 1 (#17).
- 既有标题 `## 6.3.5.7 Microbiology Domains` (MB/assumptions.md:3) 与 `## 6.3.5.9 Pharmacokinetics Domains` (PC/assumptions.md:3) 无 `§` 前缀 (与 NV/FT 先例不同), 规则 6 未改, 与需主控定 #2 同类记录.
- fp 预期回归 2 条 (ig34_p0255_a021 MOVED; ig34_p0278_a051 verbatim 抄自旧 KB) 需主控并入 `work/t2_fp_expected_regressions.jsonl` 供 reviewer fp 闸使用.

## attempt 1 delta (主控裁定 1-4)
- 裁定 1 (dispatch notes "KB 自写的伪节号"): PP/examples.md:112 `## §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)` → `## RELREC Method Quick Reference (PP-side view)` (REPLACED; 内容仍在 :114 D6 标注范围内).
  预检 `grep -rn -i "quick-reference\|RELREC Method Quick Reference" knowledge_base/` 除该标题本行外 0 命中 → 无指向旧锚点的链接, 直接改标题.
- 裁定 2: MB/examples.md:3 "and" vs "/"、`## 6.3.5.7` / `## 6.3.5.9` 缺 `§` → 规则 6 不改, 已记录.
- 裁定 3: 解释性 `*Note:*` → D6 (本批 S-4 做法确认); 纯导航 "See … for …" 不标.
- 裁定 4: T-11 写正确值, 确认.
- PP/examples.md md5 → 见下行命令; check_links live docs 42.
- PP/examples.md md5 after delta: `6610077bf3b7e79a2e2bfdf358707d82` (170 行不变).

## attempt 1 delta 2 (reviewer L-1)
- PP/examples.md:106 D6 句 REPLACED, 依据 p277 PP 表 (渲染 p277-277.png): 12 行; PPTESTCD = TMAX/CMAX/AUCALL/LAMZHL/VZO/CLO; PPCAT 全为 "DRUG X"; PPNOMDY 1 (r1-6) / 8 (r7-12); 表头 4 列 PPGRPID (Example 1)…(Example 4).
  - 删 "(STUDYDRUG analyte)": STUDYDRUG 是 PC 表 PCTEST 值, PP 表无.
  - "the 4 RELREC method examples" → "1 for each of Examples 1-4 of Section 6.3.5.9.3": 列对应 Example 1-4, 不对应 Method A-D (p276 "4 --GRPID columns, 1 for each of the example situations").
- L-2 按主控不改. PP/examples.md md5 `383ff50c1524fb58a3560c76e496b04f` (170 行不变); check_links live docs 见下.
