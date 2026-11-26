# T2 B-TI reviewer checkpoint

## attempt 1 (审 writer attempt 1+2 终态; oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base = HEAD (c11084b); 本批文件 md5: TI/assumptions.md `cf4905bc8d4d2acef3b092c897ceb871` (= writer attempt 2 声明), TI/examples.md `9ee76513092a9daa2511830efc4c0441` (未改), TI/spec.md 未改.
- `git diff --stat HEAD -- knowledge_base/domains/TI` → 仅 assumptions.md (12+/6-). 整个 KB diff 其余文件 (DI/DV/ML/SC/SU/SUPPQUAL/SV/TV) 属他批, 不计.
- 节页范围核: §7.4 引言 p415 末; §7.4.1 TI p416 – p417 上半 (p417 中起 §7.4.2 TS); §7.5 p425 末 – p426. batch pdf_ranges 418-419 偏移 → 本审 manifest 用 TI/examples 416-417 + TI/assumptions 415-426. 同 writer.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TI_reviewer/`

### 命令 (可复跑, 在 repo 根)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TI_reviewer
echo '[{"file":"knowledge_base/domains/TI/examples.md","src":"ig34","lo":416,"hi":417},{"file":"knowledge_base/domains/TI/assumptions.md","src":"ig34","lo":415,"hi":426}]' > $S/manifest.json
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
#   KB tables: 1; status: {'OK': 1}; cells compared: 42; diffs: 0. RESULT RED 仅因全局 PDF_ONLY; 落在 415-426 的 pdf_only 只有 p415 tm.xpt (TM 域, 非本批)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
#   RESULT: RED (全为他批页); grep -cE '"ig34_p04(1[5-7]|2[56])_|domains/TI/' $S/fp_regress.jsonl → 0
#   ig34_p0416_a006: hit_target = knowledge_base/domains/TI/assumptions.md (baseline hit_target null)
python3 -I $S/chk.py $S        # KB 行→PDF 归一化包含 + PDF 句→KB + RELOCATE 逐字比对 (HEAD vs 现)
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
pdftoppm -f N -l N -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/pN   # N = 416, 417, 425, 已目视
```

### 逐条核 writer 变更
| # | ref | 判定 | 证据 |
|---|---|---|---|
| 1 | assumptions.md:16-18 ig34_p0416_a006 | OK, 逐字 | p416 "A trial design domain that contains one record for each of the inclusion and exclusion criteria for the trial. This domain is not subject oriented." |
| 2 | :12 `## TI – Proposed Removal of Variable TIRL` + :14 段 | OK; 标题 = PDF 原小标题 (en dash 同 PDF); 段落与 HEAD 逐字相同 (Python 行级相等比对 True), 仅移位 | p416 首个小标题 |
| 3 | :20 "TI contains all …" | OK; 逐字未改 (行级相等 True), 归 Description/Overview 第 2 段 = PDF 顺序 | p416 Description/Overview 第 2 段 |
| 4 | :22-24 `## TI – Specification` + spec 首句 | OK 逐字 (含 em dash "—") | p416 "ti.xpt, Trial Inclusion/Exclusion Criteria — Trial Design. One record per I/E criterion, Tabulation." |
| 5 | :26 `## TI – Assumptions` | 标题文字/锚点不变, 现紧接 1-5 = PDF 顺序 | p416-417 |
| 7 | :40 §7.5 引言 3 段→1 段 (主控授权) | OK; 合并行 == HEAD 三行以单空格连接 (比对 True), 无字词改动; p425 渲染图确为单段 | p425 |
| 6 | examples.md:5 T-1 | 依据成立, 见下 |  |

- 无原处残留/重复: TIRL 段、"TI contains" 段各只出现 1 次; diff 无其他删除.
- 授权范围: 全部改动属 Description/Overview、spec 首句、节标题与 Description 间 PDF 原小标题 (含其段落同文件归节)、§7.5 合段 (主控 attempt 2 授权). 无列表 1-5 改动. 无授权外改动.

### T-1 (PDF_TYPO) 核依据
- p417 原文 (渲染图确认): "This example shows records for a trial that with 2 versions of inclusion/exclusion criteria." "that with" 不合语法, PDF 笔误.
- KB examples.md:5 "a trial with 2 versions" —— 本批未改 (HEAD 原值). 依据: 删掉多余 "that" 为最小修正; PDF 自身同型句 p182 "for a study with 2 study medications…" 支持 "a/study with N" 写法. 认可 KB 保留正确写法 + 登记 T-1.
- 注 (LOW): 另一可能修正 "a trial that has", 语义等同, 不影响信息点; 不需 T4 裁定.

### G-TB4 表格 / 人工逐格 (p417 ti.xpt, 110dpi 渲染)
表头 `Row | STUDYID | DOMAIN | IETESTCD | IETEST | IECAT | TIVERS` 一致.
| Row | KB vs PDF |
|---|---|
| 1 | XYZ / TI / INCL01 / Has disease under study / INCLUSION / 1 — 一致 |
| 2 | XYZ / TI / INCL02 / Age 21 or greater / INCLUSION / 1 — 一致 |
| 3 | XYZ / TI / EXCL01 / Pregnant or lactating / EXCLUSION / 1 — 一致 |
| 4 | XYZ / TI / INCL01 / Has disease under study / INCLUSION / 2.2 — 一致 |
| 5 | XYZ / TI / INCL02A / Age 18 or greater / INCLUSION / 2.2 — 一致 |
| 6 | XYZ / TI / EXCL01 / Pregnant or lactating / EXCLUSION / 2.2 — 一致 |
census 独立复跑: OK, 42 格 0 diff. 本批无 UNPARSEABLE / pdf_unparsed 表.

### 双向全扫 (p415 §7.4 起 – p417 §7.4.2 前; p425 §7.5 起 – p426)
- KB→PDF (TI/assumptions.md 53 行 + examples.md 全部非空非表行): 全部命中, 仅 MISS = 结构行 (文件标题 `# TI — Assumptions` / `# TI — Examples`、`## §7.4 … (TI, TS) — Introduction` (O48 不计)、`## §7.5 …` (前缀 §, 文字同 PDF)) + examples.md:5 (= T-1).
- PDF→KB: 叙述 0 缺. 残余 = 节号标题 "7.4 Trial Eligibility and Summary (TI and TS)" (O48)、"7.4.1 Trial Inclusion/Exclusion Criteria (TI)" (KB 以文件承载, 同 TS 等域惯例, 不计)、T-1 句、ti.xpt 表行 (逐格已核)、p416 spec 表 (属 TI/spec.md, 范围外, 归 O15).
- 弯引号 "split"/"lump" (p426 step 6) → O40 不计.
- KB 自写解释内容 / 伪节号: 无. D6 无适用项.

### G-TB6 结构行签字
- `## TI – Proposed Removal of Variable TIRL` (PDF p416 原小标题) — 签
- `## TI – Description/Overview` (PDF p416) — 签
- `## TI – Specification` (PDF p416) — 签
- `## TI – Assumptions` (原有, 位置下移, 文字不变) — 签
- 空行增减 (合段/新节) — 签
新增内容行 3 (a006 首段、spec 首句、合并 §7.5 段), 无出处 0.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无阻断项 | — |
| examples.md:5 | T-1 | (LOW, 信息性) 修正值有 "with"/"that has" 两种可能, 语义等同 | p417 "a trial that with 2 versions" |

### R2 recheck
t2_recheck = 0, 无.

### 范围外 (沿用 writer, 确认)
- F-1/F-4 → O48; 弯引号 → O40; TI/spec.md 未核 → O15.
