# T2 B-TS auditor checkpoint (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

- 对象: `git diff HEAD -- knowledge_base/domains/TS/` (assumptions.md md5 `4cede4e83540558e4d3854f59624e5e4`, examples.md md5 `1f30220b5f753ec9d2201a3732a8a66f`; = writer/reviewer 记录值). spec.md 无 diff.
- 独立判定顺序: 先抽样 + 逐条/全量比对 PDF 与渲染图, 判完后才读 writer 报告对照 (一致).
- PDF: `source/cdisc/SDTMIG v3.4 (no header footer).pdf`; 页范围 = TS 全节 p417 (§7.4.2 起, 剔 §7.4.1 TI 原子) — p425 (§7.5 前, 剔 §7.5 原子). batch pdf_pages (420-424) 不全, 按口径扩到全节.
- 纠正记录: 首次抽样误用 p418-425 (漏 p417 TS Description 原子), 已改为 p417-425 剔 TI 后重抽; 下表以重抽结果为准.

### 抽样命令 (seed 20261126)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TS_auditor
python3 -I $S/sample.py > $S/sample.json   # = t2_auditor_v1.0 模板, 仅改: pdf 页集 = 417..425 且 parent_section 不含 "(TI)"、不以 "§7.5" 开头
```
结果: C=1 (ig34_p0424_a002), P=83, N=10 (C 1 + P−C 9).

### 样本判定
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0424_a002 (C) | p424:2-3 TSVALNF 基于 ISO 21090 null flavor, 括注标准全名 + iso.org URL | assumptions.md:65 | 否 | 是 | 是 (§7.4.2.1 Use of Null Flavor) | 括注+URL 已补, 弯引号同 PDF; 逐字 |
| 2 | ig34_p0424_a013 | p424:20-22 null flavors 可用于其他场合, 但此时 "extremely disruptive and premature" | assumptions.md:69 | 否 | 是 | 是 | 原 KB 改写 "beyond the available resources" 已恢复 PDF 原句 |
| 3 | ig34_p0417_a022 | p417:27-28 For example, TS 记录 trial phase / protocol title / objectives | assumptions.md:7 | 否 | 是 | 是 (Description/Overview) | 逐字 |
| 4 | ig34_p0425_a023 | p425 levels 3 and 4 provide successively more information | assumptions.md:115 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0418_a011 | p418 Assumption 5 TSPARM/TSPARMCD 列表在 CDISC CT + cancer.gov URL | assumptions.md:23 | 否 | 是 | 是 | 逐字含 URL |
| 6 | ig34_p0422_a004 | p422:3-4 Ex3: TSVAL null 时 TSVALCD 亦 null, TSVCDREF/TSVCDVER 不指定 | examples.md:84 | 否 | 是 | 是 (Example 3) | 逐字 |
| 7 | ig34_p0422_a013 | p422 Ex4 Rows 1-6: 全试验参数, TSGRPID null | examples.md:101 | 否 | 是 | 是 (Example 4) | 逐字 |
| 8 | ig34_p0419_a019 | p419 Assumption 18 REGID 取 registry 赋值 (ClinicalTrials.gov, EudraCT) | assumptions.md:61 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0425_a021 | p425 "It merely confirms that the primary piece of data is null." | assumptions.md:111 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0418_a014 | p418 Assumption 8 TS codetable URL / recipients 可指定 CT / FDA Data Standards Catalog | assumptions.md:29 | 否 | 是 | 是 | 逐字 |

**独有丢失 0/10, 忠实度错误 0.**

### 补充: P 全 83 原子机械匹配 (规范化子串, 原子 verbatim → KB 两文件)
- 82/83 命中 (所在行均在 PDF 所属节). 未命中 1: ig34_p0419_a004 — 原子 verbatim 误抽 "within a dataset", `pdftotext -layout` p419 与 KB:41 均为 "within a subject" → 原子抽取错 (已登记), KB 正确.
- 反向 (KB 两文件全部非表格/非标题行 → PDF p417-425 规范化全文): 仅 2 行不命中, 均为 PDF 断行连字符 (`special-\npurpose`, `subject-\nlevel`) 造成, 人工核一致; KB 无自写叙述.

### 补充: §7.4.2.1 Use of Null Flavor 逐句核 (全量)
- p424 4 段 14 句 (a002-a015) ↔ assumptions.md:65/67/69/71 共 14 句, 逐句规范化子串全部命中 (含 ISO 括注+URL、"P43Y for 43 years old, P6M for 6 months old"、"recognize this special term as an exception…"、"in a limited setting"、"see wide use in the clinical data…"、"help in the interpretation of a missing value"、"extremely disruptive and premature"、"evaluate their usefulness in a concrete setting").
- p425 表后 "The numbers in column 1…" (:93), 层级列表 15 项层次与 p425 渲染一致 (:95-109), 3 段 6 句 (a020-a025) ↔ :111/:113/:115 全部逐字.
- 删除的 KB 改写 (D-3..D-7: "no ISO 8601 representation of no maximum"、"before extending their use to subject data"、"beyond the available resources"、"related controlled terminology"、level 2 Invalid/Other 三分、"maximum age is positive infinity"、WARNING 第 2 句 "elderly population") 在 PDF p424-425 均无对应 / 与 PDF 矛盾 → 删除正确, 无 PDF 信息随之丢失.

### 补充: NullFlavor 表 (assumptions.md:73-91) 对 p424-425 110dpi 渲染
- 标题行 `NullFlavor Enumeration. OID: 2.16.840.1.113883.5.1008` = 渲染. 15 行顺序/Rank/Code/Display Name 全部 = 渲染 (NI1 INV2 OTH3 PINF4 NINF4 UNC3 DER3 UNK2 ASKU3 NAV4 NASK3 QS3 TRC3 MSK2 NA2).
- 抽格 (≥5): (1) QS Display Name "Sufficient quantity" (渲染两行 "Sufficient / quantity"); (2) QS Definition 全文含 "Add 10 mg of ingredient X … to 100 ml" + "QS"; (3) NAV Rank 4 / "Temporarily unavailable"; (4) MSK Definition 2 句 + p425 续行 WARNING 粗体 2 句 (含 "Its primary purpose is for those circumstances…without providing any detail") — 渲染 p425 续行列 1-3 空, 属 MSK 格, KB 用 `<br>` 并入合理; (5) NA 行 2/NA/Not applicable/"No proper value is applicable in this context (e.g., last menstrual period for a male)."; (6) OTH Definition "(e.g., concept not provided by required code system)". 全部一致; 15 行 Definition 机械子串比对仅 QS 1 句因 layout 折行 ("makes / quantity / up") 不命中, 渲染目视一致.
- 表头 `| Rank | Code | Display Name | Definition |` 为 KB 自写纯结构行 (PDF 无列名), 按主控裁定保留不标 D6 — 认可.

### 补充: examples.md 4 格改动对 PDF
- Ex1 Row 14 TSVAL "…Subjects with Epilepsy due to Neurofibromatosis" = p420; Ex1 Row 37 `ISO 8601` 在 TSVCDREF 列 (p421 layout 列位 156 = 同页 CDISC CT 列位) ; Ex4 Row 7 TSVAL `PHASE IB TRIAL`, TSVALCD/REF/VER 空 = p422; Ex2 Row 1 TSPARM `Trial Title` (PDF `Trial Type`) = 已登记 T-1, PDF 自身可定 (TSPARMCD=TITLE、Ex1 Row 14 / Ex4 Row 1、Row 1 说明 "Shows the trial title") — 认可.
- 授权范围: 新增 `## TS – Description/Overview` (p417 2 句逐字) / `## TS – Specification` + spec 首句逐字 / `## TS – Assumptions` = CM 先例结构; 无授权外改动.

### G-TB8
- trace.jsonl: T2.B-TS writer `oh-my-claudecode:executor` subagent_done 04:44:29Z; reviewer `oh-my-claudecode:code-reviewer` subagent_done 04:52:02Z verdict PASS; 无 `agent: main` 的 B-TS 记录.
- 时序: TS/assumptions.md mtime 04:42:01Z、examples.md 04:43:09Z 均早于 reviewer 完成; 现 md5 = reviewer 复核 md5 → reviewer 后无 KB 改动. PASS.

### 对照 writer 报告 (判完后读)
- writer 20 处改动 / D-1..D-7 / T-1..T-7 / Q-1 (NA 行) / p0419_a004 原子错, 与本 audit 独立结论一致; 无新增分歧.

### 其他
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (基线 42, 未升).
- 范围外发现: 无新增 (writer F-1 spec.md 归 O15).

### 判定
- 独有丢失 0, 忠实度错 0 → **PASS**.
