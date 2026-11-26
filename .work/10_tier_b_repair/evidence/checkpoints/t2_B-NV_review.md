# T2 B-NV reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS** (0 FAIL 项; 0 CONDITIONAL 修正项; LOW 观察 3 条不阻断)

- base = HEAD `eb13510` (本批未提交); NV md5 复核与 writer 一致: assumptions.md `21f2e97e…`, examples.md `449c0939…`, spec.md 未动 `6b4d37aa…`
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-NV_reviewer/`
- 渲染: p285/286/294/295/296/297/298 @130dpi (`pdftoppm -r 130`); 人工读图 p286 (通用表) + p296 (Ex1 nv.xpt)

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-NV_reviewer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-NV.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
#  exit 1; "KB tables: 5; status: {'UNPARSEABLE': 1, 'DIFF': 1, 'OK': 3}; diffs: 1"
#  DIFF = examples.md:18 Row 2 NVSTRESN kb=1.17 pdf="" (= T-2, 已登记); UNPARSEABLE = assumptions.md:19 新增通用表 (人工核见下)
#  本批 PDF 页 (285-286, 294-298) 内 pdf_only 仅 mk.xpt Ex2 p293-294 (MK 批, 非本批); pdf_unparsed 仅 p274/p342 (非本批)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
#  RESULT: RED, 49 regress; 全部 baseline 命中文件为 ch02/MB/MS/FA/CP/RE/TA/EX/MH/model02 (他批在途/已提交改动), 0 条落在 NV 文件或 p285-286/p294-298
python3 -I $S/fwd_rev.py      # PDF 原子 (p285-286, 294-298) → NV assumptions+examples, fp_match.norm 子串
python3 -I $S/rev.py $S       # KB 两文件逐句/逐格 → pdftotext -raw p285-298 归一文本
python3 tools/check_links.py 2>&1 | grep "live docs"   # broken relative links: 18668 (live docs: 42) = 基线 42
```

### 1. 完整性 (atoms / census)
| ref | writer action | 复核 | KB 证据 |
|---|---|---|---|
| ig34_p0285_a009 | INSERTED | norm 命中 ✔ | assumptions.md:5 |
| ig34_p0285_a010 | INSERTED | norm 命中 ✔ | assumptions.md:5 |
| ig34_p0294_a013 | INSERTED | norm 命中 ✔; 位于 `## NV – Description/Overview` 下 | assumptions.md:36-38 |
| census examples.md:17 NVORRES/NVSTRESC/NVSTRESN | REPLACED 0.95→.95 | p296 渲染 Row 1 三格均 ".95" ✔ | examples.md:17 |
| census examples.md:18 NVSTRESN | SKIPPED_PDF_TYPO T-2 | 成立 (见 PDF_TYPO) | examples.md:18 |
- t2_recheck = [] → R2 recheck 无条目.
- R3 新增 3 项 (spec 首句 / 第 5 bullet / p286 通用表) 均 norm 命中: p285_a017, p286_a001-a014, p294_a012/a014/a015/a016 全 True.

### 2. G-TB4 表格 — p286 通用规格表人工逐格 (渲染图 p286, 对 assumptions.md:17-34)
| 位置 | Name | Label | Type | CT/Format | Role | CDISC Notes | Core | 结论 |
|---|---|---|---|---|---|---|---|---|
| title :17 | — | — | — | — | — | "--.xpt, Body System-Based Morphology/Physiology — Findings, Version 3.3. One record per finding per visit per subject, Tabulation." | — | 一致 (PDF 粗体, KB 粗体) |
| 表头 :19 | Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format¹ | Role | CDISC Notes | Core | 一致 (7 列, 列序同) |
| :21 | STUDYID | Study Identifier | Char | 空 | Identifier | Unique identifier for a study. | Req | 一致 |
| :22 | DOMAIN | Domain Abbreviation | Char | -- (PDF 超链接下划线) | Identifier | Two-character abbreviation … | Req | 一致 |
| :23 | USUBJID | Unique Subject Identifier | Char | 空 | Identifier | Identifier used to uniquely identify … involving the product. | Req | 一致 |
| :24 | --SEQ | Sequence Number | Num | 空 | Identifier | … (or within a parameter, in the case of the Trial Summary domain) … start at 1. | Req | 一致 |
| :25 | --TESTCD | Short Name of Measurement, Test or Exam | Char | * | Topic | … up to 8 characters. / Subject to Domain-specific test code controlled terminology. | Req | 一致 (格内换行合并为空格) |
| :26 | --TEST | Name of Measurement, Test or Examination | Char | * | Synonym Qualifier | Long name for --TESTCD. / Subject to Domain-specific … | Req | 一致 (同上) |
| :27 | --ORRES | Result or Finding in Original Units | Char | 空 | Result Qualifier | Result of the measurement or finding as originally received or collected. | Exp | 一致 |
| :28 | --STRESC | Result or Finding in Standard Format | Char | 空 | Result Qualifier | Contains the result value … copied or derived from --ORRES in a standard format … as "NEGATIVE". | Exp | 一致 (逗号位置照录) |
| :29 | --LOBXFL | Last Observation Before Exposure Flag | Char | 空 | Record Qualifier | Operationally derived indicator … should be "Y" or null. | Exp | 一致 |
| :30 | VISITNUM | Visit Number | Num | 空 | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. | Exp | 一致 |
| :31 | --DTC | Date/Time of Collection | Char | ISO 8601 datetime or interval | Timing | Collection date and time of an observation. | Exp | 一致 |
| :32 | --DY | Study Day of Collection | Num | 空 | Timing | … relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain. | Exp | 一致 ("sponsor-\ndefined" 折行连字符保留) |
| 脚注 :34 | — | — | — | — | — | "¹In this column, an asterisk (*) indicates … enclosed in parentheses." | — | 一致 |
- 12 行 × 7 列 = 84 格 + title + 表头 7 格 + 脚注: **0 差异**. 独立方法 = 渲染图目读 + `pdftotext -layout` 列位 (非 census bbox 自比). 格式同 LB/assumptions.md:18-52 先例 (粗体 title + 7 列 + `>` 脚注).
- Ex1 nv.xpt (p296 渲染逐格): 6 行 × 20 列, 除 Row 2 NVSTRESN (PDF 空 / KB 1.17 = T-2) 外一致. suppnv/relrec (p297)、Ex2 nv (p298): census OK + `pdftotext -layout` 逐行比对一致.

### 3. G-TB6 反向溯源 (diff 新增/改动行)
| diff 行 | 内容 | 出处 |
|---|---|---|
| assumptions.md:5 (改) | 原 2 句 + a009 + a010 | p285 §6.3.7 段, 逐字 |
| :15 | 第 5 bullet | p285 §6.3.7.1 bullet 5, 逐字 |
| :16, :18, :33, :35, :37, :39, :41 | 空行 | 结构行 |
| :17 | 粗体 title | p286, 逐字 |
| :19 | 表头 | 结构行 (PDF 表头, 签字) |
| :20 | 分隔线 | 结构行 (签字) |
| :21-:32 | 12 行 | p286, 见上表 |
| :34 | 脚注 | p286, 逐字 |
| :36 | `## NV – Description/Overview` | 新增节标题 = PDF p294 小标题原文 (签字) |
| :38 | 定义句 | p294, 逐字 |
| :40 | `## NV – Specification` | 新增节标题 = PDF p294 小标题原文 (签字) |
| :42 | spec 首句 | p294, 逐字 (CM/MK/RE 先例同位置) |
| examples.md:17 (改) | `.95` ×3 | p296 渲染 Row 1 |
- 新增/改动行 30 行, **无出处 0**. 无 "Note:"/自造说明/扩写; 无 D6 内容.
- KB→PDF 全文件反向扫 (rev.py) 未命中仅: 4 个既有导航标题 (`# NV — Assumptions`, `## §6.3.7 … — Overview`, `## §6.3.7.1 …`, `# NV — Examples`; 未改动, 文字均源自 PDF 标题); examples.md:11 = T-1; examples.md:63 = p297→p298 跨页句 (被页脚打断, 全句在 PDF). 与 writer 一致.

### 4. 双向全扫 (PDF→KB, 含 TABLE_ROW/HEADER/CODE_LITERAL; p285-286 + p294-298)
- 未命中: p285_a001-a005 (§6.3.6 MO 框 = O31, 已登记 out_of_scope_findings.md:34); p286_a015-a019 (CV), p298_a023-a025 (OE) 他域; p294_a001-a010 (MK Ex2 表尾) 他域; p294_a011 `6.3.7.4 Nervous System Findings (NV)` 标题 → 由 spec.md:1 `# NV — Nervous System Findings` 承载 (导航惯例, 同他域); p294_a019-a028 / p295_a001-a027 / p296_a001-a004 = NV spec 表行 (spec.md, 白名单外, F-2 → O15); p296_a019 = T-1; p296_a023 = T-2; p297_a037 = 页界截断原子 (全句 examples.md:63).
- 结论: 本批白名单文件内 PDF 叙述/表格原子 **无遗漏**.

### 5. 位置 / 无副作用
- 顺序 = PDF 顺序: §6.3.7 → §6.3.7.1 (bullets → 通用表 → 脚注) → NV Description → NV Specification → NV Assumptions. ✔
- `git diff HEAD --stat -- knowledge_base/`: NV 仅 assumptions.md (+29/-1) / examples.md (+1/-1); 其余 BS/RE/SM 为他批在途改动, 与本批无关. 既有标题/锚点未改; Ex1 其余行未动. ✔
- delete_only_source_lines = [] ✔

### PDF_TYPO 核依据
| T | 位置 | PDF | KB | 判定 |
|---|---|---|---|---|
| T-1 | examples.md:11 (p296 "Rows 5-6") | "based on an fluorodeoxyglucose (FDG)-PET scan" | "a fluorodeoxyglucose" (既有, 未改) | 成立: 冠词错属 PDF 自身文字错误, 按 dispatch "PDF 自身拼写错 KB 保留正确" |
| T-2 | examples.md:18 Row 2 NVSTRESN (p296) | 空 (渲染图确认) | 1.17 | 成立: 正确值可由 PDF 自身确定 (同行 NVSTRESC=1.17 数值; Rows 1,3-6 NVSTRESN=NVSTRESC; p286 --STRESC 注 "if results are numeric, they should also be stored in numeric format in --STRESN") → 补充口径 "写正确值并登记" |

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无 FAIL / CONDITIONAL 项 | — |
| L-1 (LOW) | 宿主 | §6.3.7.1 通用表放在 NV/assumptions.md: 主控已认可, LB §6.3.5.1 先例; 他体系域 (CV/MK/OE/RE…) 无交叉引用 (F-3) | p285 "partial generic domain specification table" |
| L-2 (LOW) | 格式 | examples.md:37/:61 em dash 两侧空格、:61 直撇号 (PDF 弯撇号), 既有行未改; T1 判 EQUIVALENT, 不阻断 | p297 "records—specifically" |
| L-3 (LOW) | T-1 归类 | 冠词错归 "拼写错" 口径属扩展解释, 建议 T4 汇总时让用户一并过目 | p296 "an fluorodeoxyglucose" |

### R2 recheck
- t2_recheck = [] → 无.
