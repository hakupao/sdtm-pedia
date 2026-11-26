# T2 B-TS writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `b0932182fdeb0139a0d6b1dae9c3f77321901294` (TS 文件改前 `git diff --quiet -- knowledge_base/domains/TS` = clean)
- md5: TS/assumptions.md `15531f015ae0fbf81617c8bef3bdccea` → `4cede4e83540558e4d3854f59624e5e4` (106 → 115 行); TS/examples.md `f58e91d345b89a4f7c8d8ab1d370bf3e` → `1f30220b5f753ec9d2201a3732a8a66f` (151 行不变); TS/spec.md 未动 `3061e2e2739822f99c723877c9eff798`
- 白名单: assumptions.md + examples.md (batch json); 主控授权的 Description/Overview + spec 首句 (BE/CM 先例)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TS_writer/` (assumptions.before.md, examples.before.md, p417-p425 渲染 110dpi, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl, scan.py (初版), scan2.py (复跑用))
- 本批 atoms 1 (REAL_GAP) / t2_recheck 0; census DIFF 2 表 (3 CELL, KB 行 24/47/121); pdf_only 0; unparseable 2 (assumptions.md:35 / :67 基线行号).
- **节页范围核 (O20)**: §7.4.2 TS = p417 下半 (标题 "7.4.2 Trial Summary (TS)" + Description/Overview + Specification 首句 + spec 表) → p418 (spec 续 + Assumptions 1-10) → p419 (Assumptions 11-18) → p420-423 (Examples 1-4) → p424-425 上半 (§7.4.2.1 Use of Null Flavor; p425 中部起 §7.5). batch pdf_ranges lo=419 **不全**, 实际 **p417-425**; 本批全扫与 census manifest 均用 417-425. p417 无节引言 NOTE (渲染图核).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | TS/assumptions.md:65 | ig34_p0424_a002 | INSERTED | 首句补 ISO 21090 括注 (Health Informatics – Harmonized data types…; iso.org URL); 引号改 PDF 弯引号 | 424 |
| 2 | TS/examples.md:24 | census:examples.md:24:14:TSVAL | REPLACED | TITLE 删多出的 "Neurofibromatosis " (KB "Subjects with Neurofibromatosis Epilepsy due to…") → PDF "Subjects with Epilepsy due to Neurofibromatosis" | 420 |
| 3 | TS/examples.md:47 | census:examples.md:47:37:TSVCDREF | REPLACED | 空 → `ISO 8601` (渲染图 Row 37) | 421 |
| 4 | TS/examples.md:121 | census:examples.md:121:7:TSVAL | REPLACED | 空 → `PHASE IB TRIAL` (渲染图 Row 7; TSVALCD/REF/VER PDF 为空, 照录) | 422 |
| 5 | TS/assumptions.md:3-5 | Description/Overview (主控授权) | INSERTED | 新增 `## TS – Description/Overview` + p417 首段 2 句逐字; 原 :3 段 (第 2 段) 保留于其下 | 417 |
| 6 | TS/assumptions.md:9-13 | spec 首句 (主控授权) | INSERTED | 新增 `## TS – Specification` + `ts.xpt, Trial Summary — Trial Design. One record per trial summary parameter value, Tabulation.` + `## TS – Assumptions` (BE/CM 结构) | 417 |
| 7 | TS/assumptions.md:17 | R3 新增 (Assumption 2 词替换) | REPLACED | "under which conditions" → PDF "under which circumstances" | 418 |
| 8 | TS/assumptions.md:33 | R3 新增 (Assumption 10 引号) | REPLACED | 直引号 "null flavor," → PDF 弯引号 “null flavor,” | 418 |
| 9 | TS/assumptions.md:41 | R3 新增 (Assumption 13 KB 增词) | REPLACED | "any block of records in the TS dataset" → PDF "…in the dataset" | 419 |
| 10 | TS/assumptions.md:59 | R3 新增 (Assumption 17 丢短语, R2) | REPLACED | "would have TSVAL be null" → PDF "would have no trial indication; TSVAL would be null" | 419 |
| 11 | TS/assumptions.md:67 | R3 新增 (§7.4.2.1 第 2 段, ig34_p0424_a005-a008 改写) | REPLACED | KB 改写段 (含 PDF 无的 "no maximum … ISO 8601 representation" 句、"upper and lower age limits") 整段 → PDF 原段逐字 | 424 |
| 12 | TS/assumptions.md:69 | R3 新增 (§7.4.2.1 第 3 段, ig34_p0424_a009-a014 改写) | REPLACED | KB 改写段 ("before extending their use to subject data"/"beyond the available resources" 等, 与 PDF 语义不同) → PDF 原段逐字 | 424 |
| 13 | TS/assumptions.md:73 | R3 新增 (表标题行 ig34_p0424_a016) | REPLACED | `NullFlavor Enumeration (OID: …)` → PDF `NullFlavor Enumeration. OID: …` | 424 |
| 14 | TS/assumptions.md:90 | R3 新增 (p425 WARNING, ig34_p0425_a002) | REPLACED | KB 表前引用块 WARNING (第 2 句 PDF 无: "maximum age limit … elderly population") 删; PDF WARNING 原文 (2 句) 放入 MSK 行 Definition 格 (`<br>` 后粗体), 依据: p425 渲染图该 WARNING 为分页后续行, 列 1-3 空, 紧接 p424 末行 MSK | 424-425 |
| 15 | TS/assumptions.md:91 | R3 新增 (ig34_p0425_a003 NA 行) | INSERTED | 补表行 `2 / NA / Not applicable / No proper value is applicable in this context (e.g., …)` | 425 |
| 16 | TS/assumptions.md:113 | R3 新增 (ig34_p0425_a022 level 2 段) | REPLACED | KB 改写 (Invalid/Other/no information 三分, 与 PDF 不同) → PDF 原句 (not applicable vs applicable but masked, unknown, or invalid …) | 425 |
| 17 | TS/assumptions.md:115 | R3 新增 (ig34_p0425_a024 levels 3-4 段) | REPLACED | "PINF means that the maximum age is positive infinity, i.e., there is no maximum age" → PDF "…there is information about the maximum age, but it is not something that can be expressed, as in the ISO8601…" | 425 |
| 18 | TS/examples.md:76 | PDF_TYPO T-1 (Ex2 Row 1 TSPARM) | REPLACED | PDF `Trial Type` → KB `Trial Title` (见 T-1) | 421 |
| 19 | TS/examples.md:86 | R3 新增 (Ex3 Row 1 词替换) | REPLACED | "(the null flavor that means …)" → PDF "(the null value that means …)" | 422 |
| 20 | TS/examples.md:99 | R3 新增 (Ex4 引言词替换) | REPLACED | "This example uses TSGRPID" → PDF "This example shows use of TSGRPID" | 422 |

- 覆盖率自查: atoms 1 = #1; census 3 格 = #2-4 (全部改为 PDF 值); 授权项 2 (#5-6); R3 新增 13 (#7-17, #19-20); PDF_TYPO 1 (#18).

### census 表处理

| census ref | 处理 | 改后 census |
|---|---|---|
| examples.md:9 Ex1 ts.xpt (2 CELL, KB 24/47) | #2 #3 | OK |
| examples.md:113 Ex4 ts.xpt (1 CELL, KB 121) | #4 | OK |
| examples.md:74 Ex2 ts.xpt | 原 census OK; #18 T-1 改为正确值 | DIFF 1 (= T-1, 预期残留) |
| examples.md:92 Ex3 ts.xpt | census OK; 渲染图核一致 | OK |

census_after (manifest lo=417 hi=425): KB tables 6 → OK 3 / DIFF 1 (T-1) / UNPARSEABLE 2; 全部 4 张例表对 110dpi 渲染 (p420-423) 逐格人工核: 表头/列序/列数/Row 列一致, 除 T-1 外 0 差.

### 触碰的 unparseable 表
- **assumptions.md:75 (基线 :67, NullFlavor 表) — 已触碰**: 标题行改 PDF 写法 (#13)、MSK 格追加 WARNING (#14)、新增 NA 行 (#15). 改后 15 行 = PDF p424-425 15 行 (NI…MSK 14 + NA), 渲染图逐格核 Rank/Code/Display Name/Definition 一致. reviewer 须逐格人工核.
  - 表头 `| Rank | Code | Display Name | Definition |` 为 KB 自写结构行 (PDF 只有跨列标题 "NullFlavor Enumeration. OID: …", 无列名); 按 B-AE 先例 (PDF 无表头, KB 首行作 Markdown 表头 = 结构行) 保留, 列为 KB_AUTHORED 导航, 不加 D6 标注 — reviewer 定.
- assumptions.md:45 (基线 :35, Assumption 13 剂量表) — **未触碰**; 已对 p419 渲染图逐格核 5 行一致.

### PDF_TYPO / PDF 自相不一致清单 (KB = PDF 原文的均未改, 交 T4)
- **T-1 (改)**: p421 Ex2 Row 1 TSPARMCD=TITLE 但 TSPARM=`Trial Type`. 正确值由 PDF 自身确定: Ex1 Row 14、Ex4 Row 1 TITLE ↔ `Trial Title`; Ex2 Row 1 说明 "Shows the trial title"; 同表无 TTYPE. → KB `Trial Title`.
- T-2 (未改, T4): Assumption 13 正文 `TSPARMCD = "Dose"` vs 同例表 `DOSE` — 大小写不一致, 正文照录.
- T-3 (未改, T4): Assumption 13 `DOSFREQ` (正文+表) vs Ex4 Rows 32/36 `DOSFRQ` — 两处互异, PDF 自身无法定, 照录.
- T-4 (未改, T4): Assumption 16 `OUTMSPR` vs Ex1 Row 28 `OUTMSPRI` — 两处互异, 照录.
- T-5 (未改, T4): §7.4.2.1 "among its 14 terms" vs 表 15 行 (含 NA) — 照录.
- T-6 (未改, T4): levels 3-4 段 "MAXAGE case" vs 参数名 AGEMAX — 照录.
- T-7 (未改, T4): 层级列表 "Quantity sufficient" vs 表 QS "Sufficient quantity" — 照录.
- 说明: Ex4 Row 7 `PHASE IB TRIAL` 无 TSVALCD/TSVCDREF/TSVCDVER (他行 TPHASE 有 C15602) — PDF 原样, 非可证错误, 照录.

### 新增 atom 清单 (R3)
- #7-17, #19-20 (13 处). 其中 #11/#12/#16/#17 涉及 fp_baseline 判 EQUIVALENT 的原子 (p424_a005-a014, p425_a022/a024): 人工逐句比对, KB 为语义不同的改写 (见删除清单), fp 尺度过宽.

### 删除清单
| # | 原位置 (基线) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:24/:47/:121/:76 旧值; :86/:99 旧词 | 同行 | VALUE_DIFF / 词替换旧值替换 (#2-4, #18-20) | — |
| D-2 | assumptions.md:7/:23/:31/:49 旧词句 | 同行 | 词替换 / KB 增词 / R2 丢短语恢复 PDF (#7-10) | — |
| D-3 | assumptions.md:57 整段改写 | :67 PDF 原段 | 改写段与 PDF 矛盾 (age limits 讨论、PDF 无的 "no maximum" ISO 句); 该行仅承载 p424_a005-a008 (均由 PDF 原段覆盖) → D2 删 | — |
| D-4 | assumptions.md:59 整段改写 | :69 PDF 原段 | 改写与 PDF 语义不同 ("before extending … subject data", "beyond the available resources", "learn about … related controlled terminology"); 仅承载 p424_a009-a014 → D2 删 | — |
| D-5 | assumptions.md:65 WARNING 引用块 | :90 MSK 格 | 第 2 句 PDF 无且与 PDF 矛盾 (PDF 第 2 句为 "Its primary purpose …") → D2 删扩写; 第 1 句随 PDF 原文移入 MSK 格 | — |
| D-6 | assumptions.md:104 level 2 句 | :113 | 改写内容与 PDF 矛盾 → D2 删 | — |
| D-7 | assumptions.md:106 PINF 释义半句 | :115 | "maximum age is positive infinity, i.e., there is no maximum age" 与 PDF 释义不同 → D2 删, 恢复 PDF | — |

### 双向全扫 (含表格原子)
- PDF→KB: p417 (§7.4.2 起) — p425 (§7.5 前) 叙述按句规范化子串比对 (`scan2.py`): 改后叙述 0 缺; 残余 MISS 全为 spec 表 (属 spec.md, 范围外) / 标题 / 表行 layout 折行 / 列表符号, 表行另对渲染图人工核. p418-419 Assumptions 1-18 (含 12 NOTE、13 表) 逐句在 assumptions.md.
- KB→PDF: `scan2.py` 对两文件全部非表格行按句查 PDF (p417-425 规范化文本): KB-ONLY 0; 表格行对渲染图人工核; 全文件每行有 PDF 对应; 无伪节号; 无其他 KB 自写解释性内容 (除 NullFlavor 表头结构行, 见上). `### Use of Null Flavor` (PDF "7.4.2.1 Use of Null Flavor") 按规则 6 未改.

### 范围外发现
- F-1: TS/spec.md (p417-418 spec 表) 不在白名单, 未核 → 归 O15 spec 扫描.
- F-2 (流程): fp_baseline 对 §7.4.2.1 多条语义不同的改写句判 EQUIVALENT (p424_a005-a014, p425_a002/a022/a024), 对 NA 行 p425_a003 判 INTENTIONAL_EXCLUDE (理由误写为 "spec 表行"). 他批 EQUIVALENT 判定可能同样过宽, 建议主控评估.
- F-3 (已核 `scripts/fp_match.py`): `verdict` 字段取自固定 ledger (`coverage_ledger.wc.jsonl`), 不随 KB 变; 实时信号是 `hit_target` (PDF atom verbatim 规范化后在现 KB 文件的子串命中). 本批 p417-425 共 128 原子: hit_target 改后 111, **新增命中 19 / 丢失 0** (新增含 p0424_a002 本 atom、p0424_a005-a014、p0424_a016、p0425_a001/a002/a022/a024、p0417_a018/a019、p0418_a008、p0419_a018、p0420_a019). 余 17 未命中: p0424_a017-a030 + p0425_a003 = NullFlavor 表行 (atom verbatim 带 "Row N |" 前缀, 结构性不可子串命中; 已对渲染图逐格核)、p0420_a035 页脚版权行、p0419_a004 (atom verbatim 误抽为 "within a dataset", PDF 渲染与 KB 均为 "within a subject"; atom 抽取错, KB 正确).

### 需主控定
- Q-1: #15 补 NA 行 (ig34_p0425_a003) — 该原子在 R4 已 ack 的 IE 清单中 (fp 理由误写为 "Domain variable specification table row"; 实为 §7.4.2.1 NullFlavor 表第 15 行, Ex3/Ex4 Row 17 均用 NA). 已补; 若主控维持 IE → 回退: 删 assumptions.md:91 一行.
- Q-2: #18 T-1 把 census 原 OK 的 Ex2 Row 1 TSPARM 从 PDF 值 `Trial Type` 改为 `Trial Title` (依据 PDF 补充口径 "正确值能由 PDF 自身确定"). 若主控要求照录 → 回退: examples.md:76 `Trial Title` → `Trial Type`, T-1 改登 T4.
- 其他: T-2..T-7 照录 PDF, 交 T4; NullFlavor 表头结构行保留方式由 reviewer 确认.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TS_writer
python3 -I -c "import json;json.dump([{'file':f,'src':'ig34','lo':417,'hi':425} for f in ['knowledge_base/domains/TS/assumptions.md','knowledge_base/domains/TS/examples.md']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # KB tables 6: OK 3 / DIFF 1 (T-1) / UNPARSEABLE 2
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -E 'p04(1[7-9]|2[0-5])|TS/' $S/fp_regress.jsonl   # 0 (51 行均他批页)
python3 -I $S/scan2.py   # 双向: PDF->KB 残余 MISS 全为 spec 表 (spec.md)/例表行 layout/标题/列表符号; KB->PDF (非表行) KB-ONLY 0
for p in 417 418 419 420 421 422 423 424 425; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### git diff --stat
```
 knowledge_base/domains/TS/assumptions.md | 35 ++++++++++++++++++++------------
 knowledge_base/domains/TS/examples.md    | 12 +++++------
 2 files changed, 28 insertions(+), 19 deletions(-)
```
