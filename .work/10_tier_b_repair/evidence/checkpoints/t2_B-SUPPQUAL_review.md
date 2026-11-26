# T2 B-SUPPQUAL — reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base = HEAD; 范围 = `git diff HEAD -- knowledge_base/domains/SUPPQUAL/` (3 文件, +23/-7); ch08_relationships.md 未改 (`git status --short` 空)。工作树其他 M 文件属他批, 不计。
- 节页范围: §8.4 = p431 (节标题 + 2 段) → p434 (§8.4.4 末; 其后 §8.5)。batch pdf_ranges 430-432 不全 (O20), 本 reviewer 用 431-434 自建 manifest。
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SUPPQUAL_reviewer/` (manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl, p-432/433/434.png 110dpi)

### 命令 / 关键输出
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SUPPQUAL_reviewer
python3 -I -c "import json;json.dump([{'file':'knowledge_base/domains/SUPPQUAL/examples.md','src':'ig34','lo':431,'hi':434}],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1: status {'OK': 1, 'NO_PDF': 1}; cells compared 22; diffs 0. suppae(:13) OK; suppqs(:24) NO_PDF
  # 本批页 PDF_ONLY: p431 relrec.xpt (属 §8.3.1 RELREC, 非本批) + p434 suppqs.xpt (= KB :24 那张, PDF 标题 "Example" 缺编号致未配对) → 人工逐格见下
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # 全局 RESULT: RED (他批在途); grep -cE 'p043[1-4]|SUPPQUAL' $S/fp_regress.jsonl = 0
  # p431-434: EXACT 31 / EQUIVALENT 4 / PARTIAL 7 (p0433_a021-024, a033-035; baseline 同为 PARTIAL, 非回归)
直接目标文件核 (norm(verbatim) in norm(SUPPQUAL 三文件拼接)): p431-434 全部原子; 未命中项逐条解释见下
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```

### 1. 完整性 (writer 变更清单逐条核)
| # | 核结果 | 证据 |
|---|---|---|
| 1 Source 行 ×3 | OK; 格式 = `RELSPEC/assumptions.md:3`; 节号覆盖正确 (assumptions 含 §8.4 引言/§8.4.1 表后段/§8.4.2/§8.4.4; examples §8.4.3; spec §8.4.1) | KB 导航行 |
| 2 --GRPID 段 | OK 逐字 | p432 "Just as use of the optional grouping identifier variable (--GRPID)…" |
| 3 `## Supplemental Qualifiers (SUPP--)` + spec 首句 | OK; 标题 = PDF §8.4.1 原小标题 (去编号, 同文件惯例); 首句逐字 | p432 "supp--.xpt, Supplemental Qualifiers for [domain name] — Relationship." |
| 4 See Section 4.5.3 段 | OK 逐字 | p433 |
| 5 See Appendix C1 段 | OK 逐字 | p433 |
| 6 §8.4.2 末 3 句 | OK 逐字 (+T-3 右括号) | p433 "In cases where data about associated persons have been collected…" |
| 7 parent dataset | OK | p434 "contained within a parent dataset" |
| 8 AESOSP (正文) | OK | p433 "(AESOSP and AETRTEM)" |
| 9-10 suppae 3 格 | OK (census OK diffs 0 + 渲染核) | p433 表 |
| 11 (ADAS-Cog) | OK; 表内 IDVARVAL ADAS-COG 保持 = PDF | p433 / p434 |
| 12 Additional examples 句 | OK 逐字 | p434 "domain examples, such as in Section 5.2 Demographics" |
| 13 spec 10 变量 | 我独立逐变量对 p432 渲染图核, 全一致 (见下表) | p432 |
| 14 suppqs 44 格 | 我独立对 p434 渲染逐格核, 全一致 (见下表) | p434 |
- atoms 0 / t2_recheck 0 → 无 R2 recheck 项。

### 2. G-TB4 人工逐格
**suppae.xpt (p433 渲染; census 也 OK)**
| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL | 判 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1996001 | AE | 99-401 | AESEQ | 1 | AESOSP | Other Medically Important SAE | Spontaneous Abortion | CRF | (空) | 一致 |
| 2 | 1996001 | AE | 99-401 | AESEQ | 1 | AETRTEM | Treatment Emergent Flag | N | Derived | SPONSOR | 一致 |

**suppqs.xpt (p434 渲染; census NO_PDF)**
| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL | 判 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1996001 | QS | 99-401 | QSCAT | BPI | QSLANG | Questionnaire Language | FRENCH | CRF | (空) | 一致 |
| 2 | 1996001 | QS | 99-401 | QSCAT | ADAS-COG | QSLANG | Questionnaire Language | FRENCH | CRF | (空) | 一致 |
| 3 | 1996001 | QS | 99-802 | QSCAT | BPI | QSLANG | Questionnaire Language | GERMAN | CRF | (空) | 一致 |
| 4 | 1996001 | QS | 99-802 | QSCAT | ADAS-COG | QSLANG | Questionnaire Language | GERMAN | CRF | (空) | 一致 |
表头 11 列名与 PDF 一致。

**spec.md 10 变量 (p432 渲染; 字段块格式)**
| 变量 | Label | Type | CT (PDF → KB) | Role | Core | CDISC Notes | 判 |
|---|---|---|---|---|---|---|---|
| STUDYID | Study Identifier | Char | 空 → 空 | Identifier | Req | 逐字 | 一致 |
| RDOMAIN | Related Domain Abbreviation | Char | (DOMAIN) → C66734 | Identifier | Req | 逐字 | 一致 (CT 记法 O15) |
| USUBJID | Unique Subject Identifier | Char | 空 → 空 | Identifier | Req | 逐字 | 一致 |
| IDVAR | Identifying Variable | Char | * → 空 | Identifier | Exp | 逐字 | 一致 (* 记法 O15) |
| IDVARVAL | Identifying Variable Value | Char | 空 → 空 | Identifier | Exp | 逐字 | 一致 |
| QNAM | Qualifier Variable Name | Char | * → 空 | Topic | Req | 逐字 | 一致 (* 记法 O15) |
| QLABEL | Qualifier Variable Label | Char | 空 → 空 | Synonym Qualifier | Req | 逐字 | 一致 |
| QVAL | Data Value | Char | 空 → 空 | Result Qualifier | Req | 逐字 | 一致 |
| QORIG | Origin | Char | 空 → 空 | Record Qualifier | Req | 逐字 | 一致 |
| QEVAL | Evaluator | Char | (EVAL) → C78735 | Record Qualifier | Exp | 逐字 | 一致 (CT 记法 O15) |
Order 1-10 = PDF 行序。spec.md 未改动 (仅 Source 行)。

### 3. 双向全扫 (p431-434, 含表格原子)
- PDF→KB (pdf_atoms p431-434 全量, norm 判定): 未命中 SUPPQUAL 的仅为 — §8.3.1 / §8.5 原子 (非本节, p431 前半 / p434 后半); 节标题原子 (8.4 / 8.4.1-8.4.4, KB 去编号或 H1 代替, 导航); spec TABLE_HEADER/TABLE_ROW (字段块格式, 已逐格人工核); p432_a026 脚注 ¹ (spec.md 缺, 归 O15 记法, 见 L-1); p433_a017 (T-3 右括号); p433_a019 (T-1 llustrate)。叙述 0 缺。a034 en dash 差归 O40。
- KB→PDF (三文件逐句/逐格 vs p431-434 拼接 norm 文本): 未命中 = H1 / Source 行 / `## Example 2` (T-2) / T-1 / T-3 / Ex2 en dash (O40) / 表格折行格与 spec 字段值 (pdftotext 分栏折行; 已渲染核) / spec `> Class … Structure` 行 / Order 字段 / Cross References 导航 / assumptions:13 与 :37 (PDF 折行 "SUPP--⏎records" "special-⏎purpose" 拼接伪差, 人工核一致)。无自写解释性内容, 无 D6 项, 无伪节号。
- 粗体: §8.4.4 "should **not** be" = PDF 粗体 not (p434 渲染)。

### 4. PDF_TYPO 依据核
| T | 判 | 依据 |
|---|---|---|
| T-1 llustrate → illustrate | 成立 (PDF 自身拼写错, 可定) | p433 "These examples llustrate how a set of SUPP-- datasets" |
| T-2 Example 缺编号 → `## Example 2` | 成立 (前一例为 Example 1, 顺序可定; KB 标题不改) | p433 "Example" |
| T-3 缺 ")" → 补 | 成立 (左括号 "(e.g., resulting…" 配对可定) | p433 "(e.g., resulting in the dataset name SQAPFAMH." |

### 5. G-TB6 结构行签字
- assumptions.md:3 Source 行 (D7 指定) — 签
- assumptions.md:15 `## Supplemental Qualifiers (SUPP--)` (PDF §8.4.1 原标题, 新增节标题) — 签
- examples.md:3 / spec.md:3 Source 行 — 签
- 其余新增/改动行均为 PDF 逐字文本 (上表 #2,#4-#12)。无出处词句: 0。

### 6. 位置 / 副作用
- --GRPID 段在 §8.4 引言末 (PDF p432 §8.4.1 标题前) ✓; 4 段 (record relates / QVAL / 4.5.3 / C1) 在 §8.4.1 标题下 = PDF 表后段 ✓; §8.4.2 补句在本节段尾 ✓。
- 已有标题/锚点未变; 无清单外删除; ch08 未动; check_links live docs 42 (基线 42)。

### 7. D7: ch08 §8.4 (:181-257) vs SUPPQUAL 改后 内容一致性
| 项 | ch08 | SUPPQUAL | 判 |
|---|---|---|---|
| §8.4 引言 4 段 / §8.4.1 表后 4 段 / §8.4.2 / §8.4.4 | 逐句同 | 逐句同 | 一致 |
| spec 表 10 变量 | 表格式 | 字段块 (CT 用 C-code) | 内容一致 (记法差 O15) |
| 脚注 ¹ | 有 (:210) | 无 | 差异 → L-1 (O15) |
| Ex1 正文 + 表 | AESOSP / AETRTEM / Other Medically Important SAE | 同 | 一致 |
| Ex2 正文 em dash | "questionnaires — Brief … (ADAS-Cog) — for" (两侧空格) | "questionnaires—Brief…(ADAS-Cog)—for" (= PDF) | ch08 排版差, 归 O40 |
| Ex 标题 | `**Example 1:**` / `**Example 2:**` 内联 | `## Example 1/2` | 导航格式差, 不计 |
| 表名 | `suppae.xpt:` | `**suppae.xpt**` | 格式差, 不计 |
| suppqs 4 行 / Additional examples / 8.4.4 bullets | 同 | 同 | 一致 |
结论: 内容层面两边一致, 无需改 ch08 内容; 仅排版/记法差 (O40 / O15)。

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| L-1 spec.md (无脚注) / p432_a026 | 完整 | [LOW, conf HIGH] spec 表脚注 ¹ "In this column, an asterisk (*)…" SUPPQUAL 三文件均无 (ch08:210 有)。主控已裁 spec CT 记法归 O15 → 不计本批, 登记供 O15 兜底 | p432 "In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology." |
| L-2 assumptions.md:17 | 格式 | [LOW, conf MEDIUM] PDF spec 首句为粗体, KB 为普通文本; 与 CM/RELSPEC/RELREC/CO 先例一致 → 不改 | p432 渲染粗体 |
| L-3 spec.md:5 Structure | 完整 | [LOW] Structure 省 ", Tabulation" — 全库 spec 统一格式, 首句全文已在 assumptions:17 → 不计 | p432 |
| L-4 ch08:237 | D7 | [LOW] em dash 两侧多空格 (ch08 侧), 归 O40 | p433 "questionnaires— Brief" |
| L-5 batch json | 范围 | pdf_ranges 430-432 偏移, 实为 431-434 (O20) — writer 已记 | — |

无 CRITICAL/HIGH/MEDIUM。

### 正面观察
- writer 变更清单与 diff 一一对应 (12 处 + 2 VERIFIED), 删除清单与 PDF_TYPO 依据完整。
- R3 补句全部逐字, 位置按 PDF 节序 (§8.4.1 表后段正确归入新 §8.4.1 标题下)。
- 正文 (ADAS-Cog) 与表内 ADAS-COG 分别保留 PDF 原样, 未"统一"误改。
