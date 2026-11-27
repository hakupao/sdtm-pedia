# T4 加查 ATOM_ERR (S1-R1) — 包 1 结果 (E1-E21)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 新实例, 只读
- 日期时间: 2026-11-27T14:11:59Z (`date -u +%Y-%m-%dT%H:%M:%SZ`; 开工时 2026-11-27T14:10:36Z)
- brief: `subagent_prompts/t4/t4_atomerr_s1r1_v1.0.md` (+ `t4_supp_fullcheck_v1.0.md` 背景 / 判定口径)
- 样本包: `work/t4/atomerr/atomerr_pack_1.md`
- 看过的渲染页 (SDTMIG v3.4, 200 dpi 全页): p9, p18, p56, p79, p86, p122, p123, p124, p133, p150, p153, p154
- 用过的命令:
  - `pdftoppm -r 200 -f N -l N -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" <scratchpad>/r/pN` (N = 上列 12 页; 输出在系统临时目录, 未入仓库), 再用 Read 看 PNG
  - KB 定位: `grep -n "<原文片段>" knowledge_base/...` (ch01 / ch03 / ch04 / SE / SV / ML / SU / CE 各文件), `sed -n` 看所属节标题与表头
  - 原子原件核对 (E12): `grep '"ig34_p0124_a001"' archive/deep_verification/pdf_atoms.jsonl` 与 `work/t4/atomerr/atomerr_sample.jsonl`
  - 登记核对: `grep 'B-CE' work/t2_pdf_typo_registry.jsonl`

## 逐条判定

| # | atom_id | 判定 | ① 原子 vs PDF (差在哪; PDF 文件:行 或 渲染页) | ② KB vs PDF (KB 文件:行) | 说明 |
|---|---|---|---|---|---|
| E1 | ig34_p0009_a024 | HOLDS | 原子 "Codelist or Format" 缺逗号; PDF "Controlled Terms, Codelist, or Format" (ig34_p0009.txt:43; 渲染 p9 列表项确有逗号) | `knowledge_base/chapters/ch01_introduction.md:81` 逐字一致, 在 §1.4.1 (行 70 起) | |
| E2 | ig34_p0018_a046 | HOLDS | 原子 Structure 格 "per microbiology finding" 漏 "specimen"; PDF "One record per microbiology specimen finding per time point per visit per subject" (ig34_p0018.txt:61-64; 渲染 p18 MB 行); 其余 6 格一致 | `knowledge_base/chapters/ch03_submitting_data.md:54` 7 格逐格一致, 在 §3.2.1 (行 18) | |
| E3 | ig34_p0056_a006 | HOLDS | 原子第 1 格缺句点, 第 2/3 格漏 "to improve readability." , 第 4 格 "Not applicable" 缺句点; PDF 4 格见 ig34_p0056.txt:37-40, 渲染 p56 表第 3 行 | `knowledge_base/chapters/ch04_general_assumptions.md:1478` 4 格逐格一致, 在 §4.5.3.2 (行 1401) 的 4 列表内 | 包内 KB 指针 ch04:1362 偏, 实际在 1478 |
| E4 | ig34_p0079_a004 | HOLDS | 原子 "through the study elements of the trial"; PDF "through the epochs and elements of the trial" (ig34_p0079.txt:13; 渲染 p79) | `knowledge_base/domains/SE/assumptions.md:7` 逐字一致 (该文件 "SE – Description/Overview" 节) | |
| E5 | ig34_p0079_a006 | HOLDS | 原子 "definitions of ELEMENT values"; PDF "definitions (TESTRL values)" (ig34_p0079.txt:15-16; 渲染 p79) | `knowledge_base/domains/SE/assumptions.md:11` 逐字一致 | |
| E6 | ig34_p0079_a009 | HOLDS | 原子 "the – DTC" (en dash + 空格); PDF "the --DTC" (双连字符, 无空格) (ig34_p0079.txt:21; 渲染 p79 第 1 个圆点项) | `knowledge_base/domains/SE/assumptions.md:17` 逐字一致 ("--DTC") | 变量名记号字符不同, 非引号 / 空白归一 |
| E7 | ig34_p0079_a010 | HOLDS | 原子 "Such variables can relate" 多 "can", 且 "(–DY)"; PDF "Such variables relate" 与 "(--DY)" (ig34_p0079.txt:23-25; 渲染 p79 第 2 个圆点项) | `knowledge_base/domains/SE/assumptions.md:18` 逐字一致 (弯引号同 PDF) | |
| E8 | ig34_p0086_a011 | HOLDS | 原子 "planned but not completed visits."; PDF "planned but not expected visits due to a subject not completing the study." (ig34_p0086.txt:19-21; 渲染 p86) | `knowledge_base/domains/SV/assumptions.md:9` 逐字一致 (SV Description/Overview 节) | |
| E9 | ig34_p0122_a015 | HOLDS | 原子 "CDISC/NCIBI codelist"; PDF "CDISC/NCI codelist" (ig34_p0122.txt:33; 渲染 p122 表下脚注) | `knowledge_base/domains/ML/spec.md:339` 逐字一致 (前置上标 ¹ 对应 PDF 脚注号) | |
| E10 | ig34_p0122_a017 | HOLDS | 原子 "items that would not be represented in other domains"; PDF "items that would be represented in other domains" (ig34_p0122.txt:37; 渲染 p122 Assumption 1) | `knowledge_base/domains/ML/assumptions.md:13` 逐字一致 | |
| E11 | ig34_p0123_a012 | HOLDS | 原子 "add a row. ADD ROW" (句点); PDF "Click here to add a row: ADD ROW" (冒号) (ig34_p0123.txt:19; 渲染 p123 Meal Log CRF 末行) | `knowledge_base/domains/ML/examples.md:19` "Click here to add a row: **ADD ROW**" 一致 (粗体归一) | |
| E12 | ig34_p0124_a001 | NOT_HOLD | 原子 18 格与 PDF 逐格一致: MLDTC 空 / MLSTDTC 2015-09-03T08:30 / MLENDTC 空 / MLEVLINT 空 / RELMIDS LAST MEAL PRIOR TO / MIDS HYPO2 / MIDSDTC 2015-09-03T17:00 (ig34_p0124.txt:1-5; 渲染 p124 Row 2) | `knowledge_base/domains/ML/examples.md:42` 18 格逐格一致 (表头 行 40 前后 18 列) | `①不成立`. PDF: MIDSDTC "2015-09-03T17:00", 其余格见左. 原子: 同 PDF, MIDSDTC "2015-09-03T17:00" 未截断 (`archive/deep_verification/pdf_atoms.jsonl` 原件亦同). KB: 同 PDF. 按标签定义 KB 对 PDF 为逐字 (EXACT). 登记依据 "MIDSDTC 截断" 在原子原件中找不到 |
| E13 | ig34_p0133_a003 | HOLDS | 原子 21 格 (多 3 个空格 / 多一个 "2006-01-01", 串列); PDF 18 列: SUSTDTC 空 / SUENDTC 空 / SUSTTPT 2006-01-01 / SUSTRTPT BEFORE / SUENTPT 2006-01-01 / SUENRTPT ONGOING (ig34_p0133.txt:2-4; 渲染 p133 Row 1) | `knowledge_base/domains/SU/examples.md:37` 18 格逐格一致 (表头 行 35, 18 列) | |
| E14 | ig34_p0150_a007 | HOLDS | 原子 "may not be considered as adverse events"; PDF "may not be considered to be adverse events" (ig34_p0150.txt:21; 渲染 p150 1.a) | `knowledge_base/domains/CE/assumptions.md:14` 逐字一致 | 原子 "(a)" 与 PDF "a." 只是编号格式, 不计 |
| E15 | ig34_p0150_a008 | HOLDS | 原子 "signs of symptomatology" / "serious adverse event flag (--SER)" / 旗标列表 "--SCAT, --SCOD, --SDTH, --SDHSP, --SLIFE, --SOD, --SMIE"; PDF "signs or symptoms" / "serious variable (--SER)" / "--SCAN, --SCONG, --SDTH, --SHOSP, --SDISAB, --SLIFE, --SOD, --SMIE" (ig34_p0150.txt:23-25; 渲染 p150 1.b) | `knowledge_base/domains/CE/assumptions.md:15` 逐字一致 (PDF 行末 "--" 折行接 "SLIFE", KB 作 "--SLIFE", 属折行归一) | |
| E16 | ig34_p0150_a009 | HOLDS | 原子 "death would also be a record in the Disposition (DS) domain"; PDF "death would also be a reason for study discontinuation in the Disposition (DS) domain" (ig34_p0150.txt:28-29; 渲染 p150 1.c) | `knowledge_base/domains/CE/assumptions.md:16` 逐字一致 | |
| E17 | ig34_p0150_a012 | HOLDS | 原子 CEOCCUR 格为 "Y"; PDF 该行 3 个值格全空 (ig34_p0150.txt:35; 渲染 p150 表第 1 数据行 "Spontaneously reported event occurrence" 后无值) | `knowledge_base/domains/CE/assumptions.md:22` 4 格逐格一致 (3 值格空; 表头 行 20) | |
| E18 | ig34_p0153_a0034 | HOLDS | 原子 USUBJID "ABC-US-701-002"; PDF "ABC -US-701-002" (带空格) (ig34_p0153.txt:38-41; 渲染 p153 mh.xpt Row 1 可见空格); 其余 17 格一致 | `knowledge_base/domains/CE/examples.md:101` 18 格逐格一致 (含 "ABC -US-701-002") | 涉登记 B-CE T-2. PDF 印 "ABC -US-701-002" (带空格); KB 写 "ABC -US-701-002" (照录); 登记 handling "照录+T4" |
| E19 | ig34_p0154_a0002 | HOLDS | 原子 USUBJID "ABC-US-701-002"; PDF "ABC -US-701-002" (ig34_p0154.txt:1-4; 渲染 p154 mh.xpt Row 2); 其余格一致 (MHSPID / MHLAT / MHCONTRT / MHSTDTC / MHEVLINT 空, MHDTC 2006-05-13) | `knowledge_base/domains/CE/examples.md:102` 18 格逐格一致 | 涉登记 B-CE T-2. PDF 印 "ABC -US-701-002"; KB 写 "ABC -US-701-002" (照录); handling "照录+T4". 包内 KB 指针 :101 是 Row 1, 本行实为 :102 |
| E20 | ig34_p0154_a0013 | HOLDS | 原子 USUBJID "ABC-US-701-002"; PDF "ABC -US-701-002" (ig34_p0154.txt:17-20; 渲染 p154 ce.xpt Row 1); 其余格一致 (CEGRPID / CESCAT 空) | `knowledge_base/domains/CE/examples.md:123` 17 格逐格一致 (表头 行 121) | 涉登记 B-CE T-2. PDF 印 "ABC -US-701-002"; KB 写 "ABC -US-701-002" (照录); handling "照录+T4". 包内 KB 指针 :101 偏, 实为 :123 |
| E21 | ig34_p0154_a0014 | HOLDS | 原子 USUBJID "ABC-US-701-002"; PDF "ABC -US-701-002" (ig34_p0154.txt:21-23; 渲染 p154 ce.xpt Row 2); 其余格一致 (FIBULA / LEFT / N / 2006-10-23 / 2006-10-15) | `knowledge_base/domains/CE/examples.md:124` 17 格逐格一致 | 涉登记 B-CE T-2. PDF 印 "ABC -US-701-002"; KB 写 "ABC -US-701-002" (照录); handling "照录+T4". 包内 KB 指针 :101 偏, 实为 :124 |

## 计数

- HOLDS: 20
- NOT_HOLD: 1 (E12, `①不成立`; KB 对 PDF 为 EXACT)
- UNVERIFIABLE: 0
- 涉登记 (B-CE T-2): E18, E19, E20, E21
- 没看渲染页只看文本层的编号: 无 (21 条全部对过渲染页)

## 样本外发现的 KB 内容问题

无.
