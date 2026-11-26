# T2 B-TS reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS** (0 阻断项; 2 条 LOW 记录, 不需 writer 修)

- 对象: `git diff HEAD -- knowledge_base/domains/TS/` (assumptions.md md5 `4cede4e8…` / examples.md `1f30220b…` = writer 报告值); TS/spec.md 无 diff. 工作树中 DM/RS/model05/model06 为他批, 不计.
- 节页范围核: §7.4.2 TS = p417 下半 – p425 上半 (p425 中部起 §7.5), writer 所报 417-425 成立; p417 节标题与 Description 间无引言 NOTE (渲染图核).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TS_reviewer/`

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TS_reviewer
python3 -I -c "import json;json.dump([{'file':f,'src':'ig34','lo':417,'hi':425} for f in ['knowledge_base/domains/TS/assumptions.md','knowledge_base/domains/TS/examples.md']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
#   exit 1: KB tables 6: OK 3 (Ex1/Ex3/Ex4) / DIFF 1 (examples.md:76 TSPARM kb 'Trial Title' pdf 'Trial Type' = T-1, 预期) / UNPARSEABLE 2 (assumptions.md:45, :75)
#   pdf_only 落在 417-425 的仅 p417 ti.xpt (属 TI 域 §7.4.1, 非本批); pdf_unparsed = p274/p342 (他批)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
#   RESULT: RED (51 行全为他批页); grep -E '"ig34_p04(1[7-9]|2[0-5])|domains/TS/' fp_regress.jsonl → 0 行 (exit 1)
#   p417-425 hit_target 为空的 17 条: p0424_a017-a030 + p0425_a003 (NullFlavor 表行, verbatim 带 "Row N |" 前缀, 人工逐格见下),
#   p0420_a035 (页脚版权), p0419_a004 (原子误抽 "within a dataset"; PDF p419 为 "within a subject", KB:41 一致 → 原子错)
python3 -I $S/scan.py      # 独立双向句级扫描 (PDF p417-425 layout txt ↔ KB 两文件, 规范化引号/折行连字符)
#   KB→PDF: 非表行 KB-ONLY 0 (仅文件 H1 标题)
#   PDF→KB: 残余 MISS 全为 TI 节 (p417 上半) / spec 表 (spec.md 范围) / 例表行与表文本粘连 / §7.5 — 粘连块内叙述 (Ex1-4 引言、Row 说明、"The numbers in column 1…"、NullFlavor 末段) 逐条人工查 KB 均在
for p in 417 419 420 421 422 424 425; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### 逐条核 writer 20 处改动
| # | KB 行 | 判定 | 依据 (PDF 页) |
|---|---|---|---|
| 1 | A:65 | 一致 | p424 "ISO 21090 standard (Health Informatics – Harmonized data types for information exchange; https://www.iso.org/standard/35646.html)"; 弯引号同 PDF |
| 2 | E:24 | 一致 | p420 Row 14 "…in Subjects with Epilepsy due to Neurofibromatosis" |
| 3 | E:47 | 一致 | p421 渲染图 Row 37 TSVCDREF 列 = ISO 8601 |
| 4 | E:121 | 一致 | p422 渲染图 Row 7 TSVAL = PHASE IB TRIAL, TSVALCD/REF/VER 空 |
| 5 | A:3-7 | 一致 | p417 Description 2 句逐字 + 第 2 段原文; 位置同 BE/CM 先例 |
| 6 | A:9-13 | 一致 | p417 "ts.xpt, Trial Summary — Trial Design. One record per trial summary parameter value, Tabulation." |
| 7 | A:17 | 一致 | p418 "under which circumstances" |
| 8 | A:33 | 一致 | p418 弯引号 “null flavor,” |
| 9 | A:41 | 一致 | p419 "any block of records in the dataset" |
| 10 | A:59 | 一致 | p419 "would have no trial indication; TSVAL would be null" |
| 11 | A:67 | 一致 (逐句人工) | p424 第 2 段 4 句逐字: "arose when it was realized…", "(e.g., P43Y for 43 years old, P6M for 6 months old)", "recognize this special term as an exception…", "Therefore…" |
| 12 | A:69 | 一致 (逐句人工) | p424 第 3 段 6 句逐字: "in a limited setting", "see wide use in the clinical data…", "help in the interpretation of a missing value", "extremely disruptive and premature", "evaluate their usefulness in a concrete setting" |
| 13 | A:73 | 一致 | p424/p425 表标题行 "NullFlavor Enumeration. OID: 2.16.840.1.113883.5.1008" |
| 14 | A:90 | 一致 | p425 WARNING 2 句 (见逐格表) |
| 15 | A:91 | 一致 | p425 "2 NA Not applicable No proper value is applicable in this context (e.g., last menstrual period for a male)." |
| 16 | A:113 | 一致 | p425 level 2 句逐字 |
| 17 | A:115 | 一致 | p425 "…there is information about the maximum age, but it is not something that can be expressed, as in the ISO8601…" |
| 18 | E:76 | T-1 依据成立 | 见 PDF_TYPO 表 |
| 19 | E:86 | 一致 | p422 "(the null value that means "positive infinity")" |
| 20 | E:99 | 一致 | p422 "This example shows use of TSGRPID…" |

§7.4.2.1 D-3..D-7: 被删 KB 改写句 (age limits 讨论 / "no ISO 8601 representation of 'no maximum'" / "before extending their use to subject data" / "beyond the available resources" / WARNING 第 2 句 "maximum age limit … elderly population" / level 2 "Invalid/Other/no information" 三分 / "maximum age is positive infinity, i.e., there is no maximum age") — 逐句对 p424-425: PDF 均无, 且语义与 PDF 不同 → 删除正当; 改后 4 段逐字 = PDF (未采信 fp EQUIVALENT).

### 人工逐格: assumptions.md:75 NullFlavor 表 (p424-425 渲染图 110dpi)
PDF 表为 4 列无列名, 表标题行 "NullFlavor Enumeration. OID: …" 跨列 (p425 重复). 列对应: 列1 层级数字 / 列2 代码 / 列3 名称 / 列4 定义.
| KB 行 | Rank | Code | Display Name | Definition | 结果 |
|---|---|---|---|---|---|
| :77 | 1 | NI | No information | The value is exceptional … default exceptional value. | 一致 |
| :78 | 2 | INV | Invalid | …constrained value domain of a variable. | 一致 |
| :79 | 3 | OTH | Other | …(e.g., concept not provided by required code system). | 一致 |
| :80 | 4 | PINF | Positive infinity | Positive infinity of numbers | 一致 |
| :81 | 4 | NINF | Negative infinity | Negative infinity of numbers | 一致 |
| :82 | 3 | UNC | Unencoded | …(usually in original Text). | 一致 |
| :83 | 3 | DER | Derived | …(usually an expression is provided directly). | 一致 |
| :84 | 2 | UNK | Unknown | A proper value is applicable, but not known. | 一致 |
| :85 | 3 | ASKU | Asked but unknown | …(e.g., patient was asked but didn't know). | 一致 |
| :86 | 4 | NAV | Temporarily unavailable | …expected to be available later. | 一致 |
| :87 | 3 | NASK | Not asked | …(e.g., patient was not asked). | 一致 |
| :88 | 3 | QS | Sufficient quantity | …"Add 10 mg of ingredient X, 50 mg of ingredient Y, and sufficient quantity of water to 100 ml"… | 一致 |
| :89 | 3 | TRC | Trace | …too small to be quantified. | 一致 |
| :90 | 2 | MSK | Masked | 原定义 2 句 + `<br>` + 粗体 WARNING 2 句 | 一致 (见注) |
| :91 | 2 | NA | Not applicable | No proper value is applicable in this context (e.g., last menstrual period for a male). | 一致 |
- 行数 15 = PDF 15 行, 行序一致. 注 (MSK/WARNING): p425 WARNING 位于重复表标题后一行, 列 1-3 空, 列 4 粗体居中 —— 为 p424 末行 MSK 的分页续格 (列 1-3 空无独立代码, 且内容 "Use of this null flavor…" 指代 MSK); 并入 MSK Definition 格成立. 原表前 KB 引用块 WARNING 已删, 无重复.
- assumptions.md:45 (Assumption 13 剂量表, 未触碰) 顺带对 p419 渲染/layout 核 5 行 × 5 列一致.
- examples.md 4 张例表: Ex1 Row 14/37、Ex2 Row 1、Ex4 Row 7 对 p420-422 渲染图核 (独立于 census bbox 解析); 其余行 census OK + 渲染图抽看列序/列数一致.

### PDF_TYPO 依据核
| T | 位置 | 处理 | 依据核 |
|---|---|---|---|
| T-1 | E:76 | 改 `Trial Title` | 成立: p421 渲染图 PDF 写 "Trial Type"; PDF 自身可定 —— 同 TSPARMCD=TITLE 在 Ex1 Row 14 (p420)、Ex4 Row 1 (p422) 均 "Trial Title", Assumption 9 (p418) "TSPARMCD = "TITLE" (Trial Title)", Ex2 Row 1 说明 "Shows the trial title" |
| T-2 | A:43 | 照录 + T4 | 成立: p419 正文 "Dose" vs 表 DOSE |
| T-3 | A:43/48/50 vs E:146/150 | 照录 + T4 | 成立: p419 DOSFREQ vs p423 DOSFRQ, PDF 内无法定 |
| T-4 | A:57 vs E:38 | 照录 + T4 | 成立: p419 OUTMSPR vs p420 OUTMSPRI |
| T-5 | A:65 | 照录 + T4 | 成立: "among its 14 terms" vs 表 15 行 |
| T-6 | A:115 | 照录 + T4 | 成立: p425 "MAXAGE case" vs 参数 AGEMAX |
| T-7 | A:106 | 照录 + T4 | 成立: p425 列表 "Quantity sufficient" vs 表 "Sufficient quantity" |
- Q-1 (NA 行, ig34_p0425_a003): p425 渲染图该行明确属 NullFlavor 表 (表标题下, 层级 2), 非 spec 表行; R4 IE 理由误, 补入成立.

### R2 recheck
batch json `t2_recheck` = 0 条, 无.

### G-TB6 结构行签字
- A:3 `## TS – Description/Overview`, A:9 `## TS – Specification`, A:13 `## TS – Assumptions` (BE/CM 先例) — 签字.
- A:73 表标题行 (PDF 原文, 加粗为格式) — 签字.
- A:75-76 `| Rank | Code | Display Name | Definition |` + 分隔线 — KB 自写列名 (基线已有, 本批未改), 作 Markdown 必需表头的结构行签字; 见 LOW-1.
- A:90 `<br>` + `**…**` (PDF 粗体) — 格式, 签字.
- 新增/改动行无出处词句: 0.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| LOW-1 A:75 | G-TB6 / D6 | 表头列名 Rank/Code/Display Name/Definition 为 KB 自写 (PDF 无列名); 与 B-AE 先例 (以 PDF 首行内容作表头) 不完全同型. 属纯结构/导航, 与 PDF 不矛盾 ("column 1 … hierarchy" 可支撑列 1 语义), 判可保留不加 D6 标注; 若主控要统一口径, 可在表上方加 `> KB note (not in SDTMIG): column headers added by KB.` | p424 表仅跨列标题 "NullFlavor Enumeration. OID: …" |
| LOW-2 A:63 | 位置 (信息) | `### Use of Null Flavor` (PDF §7.4.2.1, 为 §7.4.2 子节) 现位于新增 `## TS – Assumptions` 之下, 层级上像 Assumptions 子节; 按规则标题不改, 仅记录, 供 O-级结构整理参考 | p424 "7.4.2.1 Use of Null Flavor" |

### 范围 / 副作用
- KB diff 只涉 TS/assumptions.md + TS/examples.md (白名单); assumptions.md 在 batch kb_files 内, 全文可改; spec.md 未动.
- 原有标题、锚点未改; 例表其他已有正确行未改坏 (census Ex1/Ex3/Ex4 OK).
- check_links live docs 42 (基线 42).
