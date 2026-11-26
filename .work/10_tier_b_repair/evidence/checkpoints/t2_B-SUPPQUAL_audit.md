# T2 B-SUPPQUAL auditor (Rule A) — attempt 1

> agent: oh-my-claudecode:verifier (opus); 与 writer (executor) / reviewer (code-reviewer) 不同 subagent_type。先独立判, 后对照 writer/reviewer 报告。

## 抽样
- 主抽样: `t2_auditor_v1.0.md` 抽样脚本, 改动: files = SUPPQUAL/{assumptions,spec,examples}.md (本批实际改动全部), pages = 431-434 (§8.4 完整页范围; batch pdf_ranges 430-432 偏移, O20)。
  结果 seed = 20261126; C = 0; P = 86; N = 10。样本中 5 条属同页 §8.3.1 (p431) / §8.5 (p434), 不可能落在 SUPPQUAL → 作为对照 (不计分)。
- 补抽 (计分): P 限 parent_section 以 §8.4 开头 → P84 = 56; 同 seed 重抽 N = 10 (与主抽样重叠 p0433_a021)。计分样本 = 主抽样 §8.4 内 5 条 ∪ 补抽 10 条 = 14 条唯一。
- 另: P84 全 56 原子机械匹配 (引号/dash/省略号/粗体/空白规范化子串, SUPPQUAL 三文件拼接 与 ch08 各查一次)。
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SUPPQUAL_auditor/` (sample.json, sample84.json, pg-433.png, pg-434.png 110dpi)

```
# 主抽样 = 模板脚本, 仅替换: files={3 个 SUPPQUAL 文件}; pdf_pages 条件改 a["page"] in {431,432,433,434} 且 atom_id 以 ig34 开头
# 补抽:
P84 = sorted(a for a in Plist if A[a]["parent_section"].startswith("§8.4")); random.Random(20261126).sample(P84, 10)
pdftoppm -f 433 -l 434 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/pg
```

## 样本判定 (计分 14 条; 每条 SUPPQUAL 与 ch08 都核, 仅 SUPPQUAL 计分)
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0433_a030 | p433:43 Ex2 引言 "illustrates how the language used for a questionnaire…" | SUPPQUAL/examples.md:20; ch08:237 | 否 | 是 | 是 (Example 2) | 逐字 |
| 2 | ig34_p0433_a021 | p433:31 Ex1 "The 2 rows of suppae.xpt add qualifying information… (RDOMAIN = "AE")" | examples.md:9; ch08:228 | 否 | 是 | 是 (Example 1) | 逐字 |
| 3 | ig34_p0432_a014 | p432:23 spec 首句后半 "One record per supplemental qualifier per related parent domain record(s), Tabulation." | assumptions.md:17; ch08:195 | 否 | 是 | 是 (Supplemental Qualifiers (SUPP--) 节) | 逐字 (本批 R3 新增) |
| 4 | ig34_p0433_a003 | p433:6 "All records in the SUPP-- datasets must have a value for QVAL." | assumptions.md:21; ch08:214 | 否 | 是 | 是 (§8.4.1 表后) | 逐字 |
| 5 | ig34_p0432_a004 | p432:5 objective vs subjective data 定义 | assumptions.md:9; ch08:187 | 否 | 是 | 是 (§8.4 引言) | 逐字 |
| 6 | ig34_p0433_a008 | p433:13 "Additional QNAM values may be created as needed… CDISC Notes for QVAL." | assumptions.md:25; ch08:218 | 否 | 是 | 是 | 逐字 (本批 R3 新增) |
| 7 | ig34_p0433_a006 | p433:9 "See Section 4.5.3, Text Strings that Exceed…200 characters" | assumptions.md:23; ch08:216 | 否 | 是 | 是 | 逐字, 交叉引用完整 (本批 R3 新增) |
| 8 | ig34_p0431_a026 | p431:39 "represented as separate SUPP-- datasets… (see Section 8.4.2…)" | assumptions.md:5; ch08:183 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0433_a019 | p433:28 "These examples llustrate how a set of SUPP-- datasets…" | examples.md:5; ch08:226 | 否 | 是 | 是 (§8.4.3 引言) | PDF 拼写错 llustrate → KB illustrate (PDF_TYPO T-1, 已登记, 依据拼写) |
| 10 | ig34_p0433_a023 | p433:33 "IDVARVAL specifies the value of the key variable within the parent AE record…" | examples.md:9; ch08:228 | 否 | 是 | 是 | 逐字 |
| 11 | ig34_p0431_a029 | p431:43 "Data that represent separate observations should be treated as separate observations." | assumptions.md:7; ch08:185 | 否 | 是 | 是 | 逐字 |
| 12 | ig34_p0432_a010 | p432:14 "necessary to ensure that reviewers can join/merge/transpose…" | assumptions.md:11; ch08:189 | 否 | 是 | 是 | 逐字 |
| 13 | ig34_p0432_a013 | p432:22 "supp--.xpt, Supplemental Qualifiers for [domain name] — Relationship." | assumptions.md:17; ch08:195 | 否 | 是 | 是 | 逐字, U+2014 em dash 与 PDF 同 (本批 R3 新增) |
| 14 | ig34_p0432_a006 | p432:7 subjective QEVAL 角色 (e.g., "SPONSOR", "ADJUDICATION COMMITTEE") | assumptions.md:9; ch08:187 | 否 | 是 | 是 | 逐字 |

### 对照 (主抽样中非 §8.4 原子, 不计分; 均不属本批 kb_files)
| atom_id | PDF 页:行 + 摘要 | KB | 判 |
|---|---|---|---|
| ig34_p0431_a011 | p431:14 §8.3.1 "--LNKID variable is used as the key…" | ch08:167 | 逐字在 |
| ig34_p0431_a017 | p431 §8.3.1 "The possible combinations are:" | ch08:169 | 逐字在 |
| ig34_p0434_a022 | p434:34 §8.5 list 1 (subject in general → RDOMAIN/IDVAR/IDVARVAL null) | ch08:267 | 逐字在 |
| ig34_p0434_a024 | p434:40 §8.5 list 3 (specific domain records) | ch08:269 | 逐字在 |
| ig34_p0434_a028 | p434:48 §8.5 "As with Supplemental Qualifiers (SUPP--) and Related Records (RELREC), --GRPID…" | ch08:276 | 逐字在 |

## 全 P84 机械匹配 (56 原子)
- SUPPQUAL 与 ch08 均命中: 52。未命中 4 条均可解释:
  - ig34_p0432_a026 spec 表脚注 ¹ → SUPPQUAL/spec.md 无 (spec 脚注 O15, 按指令不计); ch08:210 有 (`^1^` 记法差, 文本一致)。
  - ig34_p0433_a017 "…SQAPFAMH." PDF 缺右括号 → KB 两处补 ")" (PDF_TYPO T-3, 已登记, 依据括号配对)。
  - ig34_p0433_a019 llustrate (T-1, 同上 #9)。
  - ig34_p0433_a034 SUPPQUAL 命中; ch08:237 em dash 两侧多空格 "questionnaires — Brief" (排版 O40, 范围外, 不计)。
- 另 PDF Ex2 标题仅 "Example" (p433 渲染确认) → KB `## Example 2` (T-2, 已登记)。

## 表格补核 (suppqs census NO_PDF; 对 p434 110dpi 渲染)
- suppqs.xpt 4 行 × 11 列 = 44 格逐格对渲染图: 全一致 (≥5 格要求满足; 关键格 Row2 IDVARVAL ADAS-COG, Row3 USUBJID 99-802, Row3 QVAL GERMAN, Row1 QLABEL Questionnaire Language, 各行 QORIG CRF / QEVAL 空)。SUPPQUAL/examples.md:26-29 与 ch08:243-246 同。
- suppae.xpt (p433 渲染, O2 改动格): Row1 QNAM AESOSP / QLABEL "Other Medically Important SAE" / Row2 QNAM AETRTEM / QEVAL SPONSOR — 全一致 (examples.md:15-16, ch08:234-235)。

## diff 范围核
`git diff HEAD -- knowledge_base/domains/SUPPQUAL/` (+23/-7) 逐 hunk 对 writer 清单: Source 行 ×3 (D7); R3 插入 5 处 (--GRPID 段、§8.4.1 小标题+spec 首句、4.5.3 段、C1 段、§8.4.2 末 3 句); 短语级 3 处 (parent dataset、ADAS-Cog、"domain examples, such as in Section 5.2 Demographics"); O2 正文 AESOSP + 表 3 格。无清单外改动; 新增小标题为 PDF 原有 §8.4.1 标题 (去编号, 同文件惯例)。ch08 未改。

## 结果
- 独有信息丢失: 0 / 14 (对照 5 条 0 丢失; 全 P84 0 丢失)
- 忠实度错误: 0
- 范围外: ch08:237 em dash 空格 (O40 排版); spec.md 缺脚注 ¹ / CT 列 `*` 记法 (O15, 已由 writer/reviewer 登记)。均不计本批。
- G-TB8: trace 本批有 writer `oh-my-claudecode:executor` subagent_done (05:08:29Z) 与 reviewer `oh-my-claudecode:code-reviewer` subagent_done PASS (05:12:12Z); 无 `agent: main` 写 KB 记录; SUPPQUAL 三文件 mtime 05:06:38Z < writer done < reviewer PASS (终态经 reviewer)。
- 对照 writer/reviewer 报告 (判后): 与 writer 清单 14 项、PDF_TYPO T-1..T-3、reviewer 渲染核结论一致, 无分歧。
- live docs: 见下行 (基线 42)。

**verdict: PASS**
- `python3 tools/check_links.py 2>&1 | grep "live docs"` (repo 根) → `broken relative links: 18668 (live docs: 42)` = 基线 42。
