# T2 B-ch04 reviewer — attempt 3 复审 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

- 审查对象: `knowledge_base/chapters/ch04_general_assumptions.md` md5 `e11c6093560b572277b2bb5faa033b93` (vs 6fea563: +240/−168); attempt 2 终态由 `git show 6fea563 | patch evidence/failures/t2_B-ch04_attempt_2.patch` 重建, md5 `545883c1…` 一致, a2→a3 净 delta 242 行.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-ch04_reviewer_a3/`
- **verdict: CONDITIONAL** — writer 声明的 attempt 3 改动全部成立 (F1-F3、§4.4.10-§4.5.1 整节、标题、删除、D6 note); 但 reviewer 独立双向全扫在本批页 p22-59 内另发现 3 条 HIGH (1 处表格数值错、1 张 PDF 表整表缺、1 组伪造节号 KB 自写内容) + 3 条 MEDIUM 未标注 KB 自写. 全部是 base 就有、writer 未扫到的 (writer 扫描只覆盖 SENTENCE/LIST_ITEM/HEADING/CROSS_REF/NOTE, 且反向只扫了改写过的段落).

## 命令与结果 (可复跑; S = 上面 scratch)
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1
  → status {'UNPARSEABLE': 32, 'OK': 19, 'DIFF': 1}; DIFF = ch04:1307 eg.xpt Row 5/6 (T-1 已登记); pdf_only 落在 ig34 p22-59 的 = 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1
  → 全局 RED 15 条, 页码全不在 p22-59 (他批); ch04 对 base 回归仅 ig34_p0013_a019 (hit_any 变 ch02), norm 子串仍在 ch04 = True → 非回归
  → 本批 atoms+recheck 33 条不命中 = p43_a034 / p56_a005 / p56_a006 (预期 3); ch04 对 base 新命中 116
python3 tools/check_links.py | grep "broken relative"  → broken relative links: 18668 (live docs: 42) = 基线
锚点: grep -rn "ch04_general_assumptions(.md)?#|451-original|disease-milestone-naming|timing-relative-to-a-disease" (不截断) → 仓内 0 条 (只有 writer checkpoint 自述行); ch04 内 "](#" 0 条
正向全扫: p22-59 ig34 原子 SENTENCE/LIST_ITEM/HEADING/CROSS_REF/NOTE 839 条, norm 子串比 ch04 → 不命中 42 (= writer 38 + 4 条截断标记原子)
表格/代码原子扫: TABLE_ROW/TABLE_HEADER/CODE_LITERAL/FIGURE (writer 未扫) 去空白/竖线后比 ch04 → 76 条不命中, 逐条定性 (见 H1/H2/L4)
反向全扫: ch04 :1-1533 非表行按句切分, 去空白/连字符后比 p22-59 页文本 → 103 行有不命中句, 逐条定性 (见 H3/M1-M3/L1-L2)
G-TB6 delta: base→a3 新增 197 非空行 (表行 27); 非表 prose 逐句去空白/连字符比 PDF → 无出处仅 KB note 块内 3 条 Example applications (D6 已标) + 1 条 PDF 笔误更正 (occurrs→occurs)
渲染 (实际打开查看): -r 90 p46 / p49 / p51 / p28 / p40; -r 130 p41 (上半 + 表格区); 补充轮 -r 70-80 p23 / p34 / p43 / p44 / p47 / p48 / p50 / p52 (p53 只核文本)
```

## 必查项结论
| # | 项 | 结论 | 证据 |
|---|---|---|---|
| 1a | §4.4.10 四段新增 (ch04:1135-1141) | 逐字 = p48 | p48 "Within the context that defines uniqueness for a time point (which may include domain…" |
| 1b | §4.4.10 crossover 引导句 + 2 编号选项 + "Option 1/2" (ch04:1084-1089, 1112) | 逐字 = p47; 顺序 = PDF (4 条场景列表之后) | p47 "For instance, in a crossover trial with multiple doses on multiple days within each period" |
| 1c | §4.4.11 整节 (ch04:1143-1199) | 逐句 = p48-51 渲染 (3 个小标题同级粗体, 列表/子列表层级一致); "occurrs"→"occurs" 为 PDF 笔误更正 | p49 渲染 |
| 1d | 删 KB MIDS/RELMIDS/MIDSDTC 表 | 成立: 表格写 "RELMIDS is represented as ISO 8601 duration", PDF 原句相反 | p49 "It is similar to --ELTM, except that --ELTM is represented ISO 8601 duration." |
| 1e | §4.5.1 标题 + 4.5.1.1 (ch04:1203-1224) | 逐字 = p51-52; Mermaid 加 D6 note | p51 渲染 |
| 1f | 删 "3-level"/"Key rules"/"Tests Not Done" 摘要 | 信息点全部由 4.5.1.1 / 4.5.1.2 PDF 原文承载 (比较符号→STRESC、REASND、2 options、LBALL 例); "null when NOT DONE" 转 KB note :1226 | p51-52 |
| 1g | §4.4.8 LB 段 (ch04:1011) | 逐字 = p45, Note 句位置 = PDF (表前) | p45 "Note that --STDTC should not be used in the Findings general observation class" |
| 1h | §4.3.5 四条 (ch04:647-653) | bullet 正文逐字 = p37; 重复句删除正确 (PDF 只一遍); CMCLAS 合并正确. **但标题后缀 + 2 个子标题为 KB 自写, 见 M3** | p37 |
| 2 | 4 处标题 | "4.5.1 Original and Standardized Results of Findings and Tests Not Done" / "4.5.1.1 Original and Standardized Results" / "Disease Milestone Naming" / "Disease Milestone Name (MIDS)" 均 = PDF; 仓内无锚点引用 | p49, p51 |
| 3 | Genant / :645 去重 / 恢复短语 | 见下抽样表 (18 条) 全部一致 | — |
| 4 | attempt 3 删除清单 | 逐条对 diff: 全部属 D2 去重 / KB 扩写 / 与 PDF 矛盾; fp 对 base 无 ch04 回归; 无 PDF 内容丢失 | — |
| 5 | 3 条新 D6 note (:1034 / :1213 / :1226) | 均不与 PDF 矛盾, 前缀正确 (`> KB note (not in SDTMIG):`). :1226 与 p53-54 例子 (NOT DONE 行单位列均空) 一致. 措辞见 L5 | p46 / p51 渲染 |
| 6 | F1 / F2 / F3 | F1 ch04:866 "(see Section 7.3.1, Trial Visits)" ✓; F2 ch04:1366 "because they represent multiple values for a single variable." ✓; F3 ch04:1344 "(https://documentation.sas.com/)" ✓ | p42 / p55 / p54 |
| 7 | writer 剩余 38 条定性 | 37 条复核成立 (原子文本错 / PDF 笔误 / 标点格式 / 文件标题). writer 列表实际只列 37 个 ID, 漏列 ig34_p0057_a019 (原子 "SUPP--Datasets" vs PDF "SUPP-- Datasets", KB 用 "--" 代 en dash, 内容一致) → L3 | p57 |
| 8 | fp / census / live docs | 见上命令; 均达标. 注: census 对无 Row 列的表盲, 见 H1/H2 | — |

## 恢复短语抽样 (18 条, 对 pdf_pages + 渲染)
| ch04 | 内容 | PDF | 结果 |
|---|---|---|---|
| 66 | "The Findings About (FA) domain" | p23 | 一致 |
| 95 / 136 | "**QS Domains**" / "**SUPPQS Domains**" | p25:1, :46 | 一致 |
| 171 | "Define-XML document file" | p26 | 一致 |
| 198 | "Sharp/Genant Bone Erosion Score" | p27 文本 + p28 渲染 | 一致 |
| 376 | "see Section 8.4, Relating Non-standard Variable Values to a Parent Domain, and Appendix C1" | p31 | 一致 |
| 552 / 573 | "For example, a sponsor might conduct a study…" / "For example, if Abcicin…" | p35 | 一致 (KB 粗体标签保留) |
| 635 | "a reference to the controlled terminology … Define-XML document file … the submitted data" | p37 | 一致 |
| 675 | "In situations such as these" / "(--LOBXFL) variables" | p38 | 一致 |
| 730 | "referred to by ISO 8601 as" / "SDTM date field" | p39 | 一致 |
| 796 | "calendar weeks within the calendar year" | p41 渲染 | 一致 |
| 802 | "As is the case with the date/time representation, if no time component…(in addition to the missing time)" | p41 渲染 | 一致 |
| 835 | "the duration, "Pn…", is represented before the solidus" | p41 | 一致 |
| 907 / 909 | "Allowable values for --STRF / --ENRF are …" | p43 | 一致 |
| 1071 | "within a visit; as such, there is no dependence" | p46 渲染 | 一致 |
| 1351 | "See Section 6.3.4 …, assumption 3; and Section 7.4.1 …, assumption 5." | p55 | 一致 |
| 1455 | "is a record in the domain" | p57 | 一致 |
| 1482 | "The --PRESP variable has controlled terminology" | p57 | 一致 |
| 1520 | "--LOBXFL, with a core value of expected, was added" | p59 | 一致 |

## 问题表 (全部在本批 kb_file + 本批页 p22-59 内; 均为 base 既有, 未被 attempt 1-3 扫到)
| ref | 严重度/置信 | 检查项 | 问题 | 证据 (PDF 页 + ≤25 词) |
|---|---|---|---|---|
| H1 ch04:814 | HIGH / HIGH | G-TB4 表格数值 (UNPARSEABLE, census 未比) | 时长示例表一行 KB 写 "14 days 2 hours 57 minutes \| P14DT2H57M", PDF 是 7 hours / P14DT7H57M (130dpi 渲染确认) | p41 表: "14 days 7 hours 57 minutes  P14DT7H57M" |
| H2 ch04:218 后 | HIGH / HIGH | R3 整表缺 (PDF_ONLY, census 因无 Row 列漏报) | p28 顶部 MK 示例表 (表头 7 列 + 1 行) KB 完全没有; 全 KB grep "PALM UP" 0 条 | p28: "SPDEVID MKTESTCD MKTEST MKLOC MKLAT MKMETHOD QNAM.MKHNDPOS / ACME3000 SGBESCR Sharp/Genant Bone Erosion Score METACARPOPHALANGEAL JOINT 1 LEFT X-RAY PALM UP" |
| H3 ch04:241-255 | HIGH / HIGH | KB→PDF 反向 (KB_AUTHORED, 伪造节号) | "#### 4.2.1.1 --TEST and --TESTCD Conventions (Findings)" / "4.2.1.2 --TRT …" / "4.2.1.3 --TERM …" 三个小节 + 7 条 bullet, SDTMIG v3.4 无此三节 (p28 §4.2.1 无子节), 无 D6 标注. 伪造节号与 PDF 结构矛盾 | p28 渲染: §4.2.1 后直接是 §4.2.2 |
| M1 ch04:790-795 | MEDIUM / HIGH | KB→PDF 反向 (KB_AUTHORED 插进 PDF 列表) | [Y][M][D][T][H][S] 6 条 designator bullet 不在 v3.4 (PDF 列表只有 [P] [n] [W]); 且把 [W] 挤到末尾, 列表顺序 ≠ PDF. 内容与 ISO 8601 不矛盾 | p40-41 渲染: "[P] (duration designator)…" → "[n] represents a positive number or zero." → "[W] is used as week designator…" |
| M2 ch04:7, 15 | MEDIUM / HIGH | KB→PDF 反向 (KB_AUTHORED 未标) | :7 "## Overview" 段 (2 句) PDF 无; :15 §4.1.1 PDF 段后追加 "The SDTM describes the general conceptual framework, including …" PDF 无 | p22: §4.1.1 只有 "Review the SDTM as well as this complete implementation guide before attempting to use any of the individual domain models." |
| M3 ch04:643, 645, 650 | MEDIUM / HIGH | 标题 ≠ PDF + KB 自写子标题 | 节标题 PDF 为 "4.3.5 Storing Controlled Terminology for Synonym Qualifier Variables", KB 加 "(MedDRA and WHODrug)"; 子标题 "MedDRA Coding (Events)" / "WHODrug Coding (Interventions)" PDF 无, 且把 "If a dictionary is multi-axial…" 的通用条款归到 MedDRA 名下 (轻度改义). 仓内无锚点引用, 可改 | p37: "4.3.5 Storing Controlled Terminology for Synonym Qualifier Variables" 后直接 4 条 bullet |
| L1 ch04:534 | LOW / HIGH | D2 残留改写 | "**Example 1:** A rash with locations on the face, neck, and chest:" 复述 :532 的 PDF 原句 | p35 |
| L2 ch04:89, 396 | LOW / HIGH | 词替换型改写 | "**Note:** Submission…" / "> **Note:** QNAM references…" 对 PDF "Note that submission…" / "Note that QNAM references…"; 这两行只承载各自 1 个原子 (p24_a012 / p32_a011), writer 理由 "都在承载其他原子的长行里" 对这两条不成立 → 按补充口径恢复 PDF 原词 | p24 / p32 |
| L3 checkpoint | LOW / HIGH | 文档 | writer "剩余 38 条" 列表只列 37 个 ID, 漏 ig34_p0057_a019 (KB 内容正确) | — |
| L4 ch04:185 | LOW / MEDIUM | PDF_TYPO 登记 | p26 代码行 "STUDYID, USUBJID, VISTNUM, MKTESTCD" 是 PDF 笔误, KB 写 VISITNUM 正确, 未登记 T-n | p26:55 |
| L5 ch04:1034, 1213 | LOW / MEDIUM | D6 措辞 | 说 "KB rendering of the PDF figure", 但 :1034 的变量表 (标签/例值) 和 :1219 ORRESU→STRESU 边、边标签不在 PDF 图里. 不矛盾; 建议写成 "KB rendering … with added …" | p46 / p51 渲染 |
| L6 ch04:1226 | LOW / LOW | 位置 | NOT DONE 的 KB note 放在 4.5.1.1 末尾, 内容属 4.5.1.2; 可移 | — |
| L7 ch04:869-872, 876-878 | LOW / MEDIUM | 格式 | §4.4.5 planned visits 列表顺序 PDF 为 VISITNUM → one-to-one → VISITDY, KB 为 VISITNUM → (KB note) → VISITDY → one-to-one; "**same value (e.g., 99)**" / "**not**" 为 KB 加粗 | p42 |
| L8 ch04:1534-1536 (批外页) | LOW / MEDIUM | 范围外 | "Appendix: Cross-References to Chapter 6 Examples" 引导句 "They illustrate how General Assumptions apply in practice." 等为 KB 自写未标 D6; 内容属 p115/p261, 交主控派给对应批 | — |
| L9 ch04:224, 374 | LOW / HIGH | 标题大小写 | "Variable-Naming" (PDF "Variable-naming"); "Non-Result" (PDF "Non-result") | p28 / p31 |

## Open Questions
- H3 处理二选一请主控定: (a) D2 删整组 (节号伪造 = 与 PDF 结构矛盾; 内容是 KB 概括); (b) 去掉 "4.2.1.x" 节号, 降为 D6 KB note 块. reviewer 倾向 (a).
- M1: 6 条 designator 不在 v3.4 PDF 列表中 (来源未核). 建议 D6 标注 (单独引用块放在 PDF 三条之后) 或删; 不能留在 PDF 列表中间.

## CONDITIONAL 修正清单 (writer attempt 4; 每条改后复跑 fp / census / live docs, 并回给 reviewer 复审 delta)
1. H1: ch04:814 改为 `| 14 days 7 hours 57 minutes | P14DT7H57M |`.
2. H2: ch04:218 段后补 p28 表 (表头 SPDEVID | MKTESTCD | MKTEST | MKLOC | MKLAT | MKMETHOD | QNAM.MKHNDPOS; 1 行 ACME3000 | SGBESCR | Sharp/Genant Bone Erosion Score | METACARPOPHALANGEAL JOINT 1 | LEFT | X-RAY | PALM UP), 对渲染逐格; 主控把该表加进 census 人工清单.
3. H3: 按主控裁定删除或去节号 + D6.
4. M1: [Y][M][D][T][H][S] 6 条移出 PDF 列表, 恢复 PDF 顺序 [P] [n] [W]; 6 条改 D6 引用块或删.
5. M2: :7 Overview 段加 D6 前缀; :15 追加句从 PDF 段中拆出, 单独一行 D6 (或删).
6. M3: 标题恢复 "### 4.3.5 Storing Controlled Terminology for Synonym Qualifier Variables"; 删两个子标题.
7. L1/L2: :534 去复述 (只留 "**Example 1:**" 或删标签); :89 / :396 恢复 "Note that …" 原文.
8. L3/L4: checkpoint 补列 p57_a019; 登记 p26 "VISTNUM" PDF_TYPO.
9. 建议 (writer 自扫补漏): 正向扫描加上 TABLE_ROW / TABLE_HEADER / CODE_LITERAL 原子 (去空白/竖线比对), 并对 census UNPARSEABLE 的 32 张 ch04 表逐表对渲染 (H1 即出自 UNPARSEABLE 表).
L5-L7、L9 可选; L8 交主控.

## G-TB6 结构行签字 (attempt 3 delta)
新增/改动标题 4 条 (见必查 2) ✓; "lb.xpt" 数据集名行 (:882, p42 原有) ✓; "Option 1" / "Option 2" (p47-48 原有) ✓; "**Example 1/2/3**" 标签 (p55-56 原有 "Example n") ✓; D6 note 行 3 条 ✓; 删除的表头/分隔行 (KB MIDS 表) ✓.
attempt 3 新增非表 prose 112 行: 无出处 0 (D6 note 除外; "occurs" 为 PDF 笔误更正).

## Positive
- §4.4.11 / §4.5.1 整节替换干净, 小标题层级、子列表与 PDF 渲染一致; 删除 KB 表时正确识别出 RELMIDS/ELTM 的反向错误.
- F1-F3 全部补齐; 删除项都有去向, fp 无回归; 标题改动前查了锚点.

## 补充核查 (同一 reviewer, advisor 提示后补跑; 2026-11-26)
命令: ch04 :1-1533 每个表行逐格去空白/竖线/连字符后比 p22-59 页文本 (KB→PDF, 原先反向扫跳过了表行) → 有不命中格的行 64; 逐行定性: 多数是 PDF 单元格折行 / ½ ¼ 写法 / 已知原子错; 以下为实质问题. 另补看渲染 p23 / p34 / p43 / p44 / p47 / p48 / p50 / p52, 原文对比结论不变 (p47 "For trials with many time points…" 与 "For instance, in a crossover trial…" 在 PDF 是两段, KB 合为一段, 仅格式).

| ref | 严重度/置信 | 检查项 | 问题 | 证据 (PDF 页 + ≤25 词) |
|---|---|---|---|---|
| H4 ch04:497-508 | HIGH / HIGH | KB→PDF 图 (KB_AUTHORED Mermaid, 未标 D6) | "Decision Tree for Populating --OBJ" 的 Mermaid 分支与 PDF 图相反: PDF 根节点先问 "Parent record exists?", Yes→"Topic variable coded?" (Yes→--DECOD / No→topic variable value), No→"Name of event or intervention coded?" (Yes→coded value / No→verbatim value); KB 先问 "Topic variable coded?", 再在 No 分支问 Parent record, 得出 "无 parent record → 用 topic variable value" 这种自相矛盾的路径. 注: 原子 p34_a012 的图描述也写错, 以渲染为准 | p34 渲染: 根框下方中间菱形 "Parent record exists?", 左 Yes "Topic variable coded?", 右 No "Name of event or intervention coded?" |
| M4 ch04:42-47 | MEDIUM / HIGH | KB→PDF 表 (KB_AUTHORED 未标) | Core 值三行表 PDF 无 (p23 是 Required / Expected / Permissible 三条 bullet); PDF 的 Required 定义句只放在表格单元格里, PDF bullet 顺序 Required→Expected→Permissible 被打乱. 表中其余格内容与 PDF 不矛盾 | p23 渲染: "A Required variable is any variable that is basic to the identification of a data record…" 为第一条 bullet |
| M5 ch04:902-905 | MEDIUM / HIGH | KB→PDF 表 (KB_AUTHORED 未标) | --STRF/--ENRF "Variable / Allowable Values / Purpose" 表 PDF 无; 内容与 p43 叙述一致 | p43 渲染无表 |
| M6 ch04:921-926 | MEDIUM / HIGH | KB→PDF 表 (KB_AUTHORED 未标) | --STRTPT/--STTPT/--ENRTPT/--ENTPT 表 PDF 无; "--STRTPT: BEFORE, COINCIDENT, AFTER, UNKNOWN" 不分情形, 而 PDF 规定参考点 = 采集日时 "AFTER is not a valid value" → 简化易误读, 建议 D6 标注并注明 AFTER 仅在参考点早于采集日时可用 (或删) | p44: "AFTER is not a valid value in this case because it would represent an event after the date of collection." |
| L10 ch04:1300 | LOW / HIGH | 词替换 | Example 2 Row 1 "A numeric value was collected" vs PDF "A numeric result was collected" (T 登记只覆盖 LBSTRESC→EGSTRESC); 该行只承载 p53_a023 → 恢复 "result". 修正上文必查 7: writer 剩余定性 37 条中 p53_a023 只部分成立 | p53: "Row 1: A numeric result was collected in standard units." |
| L11 ch04:818-819 | LOW / HIGH | 格式 | "12 1/4" / "4 1/2" vs PDF "12¼" / "4 ½"; 信息等价, 可选 | p41 渲染 |
| L12 ch04:616 | LOW / HIGH | 格式 | "> **Note:**" 标签 PDF 无 (PDF 为 §4.3 首段) | p36 |
| L13 ch04:1242-1243 | LOW / HIGH | 格式 | PDF 编号选项 "1. 2." 写成 bullet | p52 渲染 |

### 修正清单追加 (接上文 1-9)
10. H4: 按 p34 渲染重建 Mermaid (根 → Parent record exists? → Yes: Topic variable coded? → Yes --DECOD / No topic variable value; No: Name of event or intervention coded? → Yes coded value / No verbatim value), 图上方加 `> KB note (not in SDTMIG): the following Mermaid diagram is a KB rendering of the PDF figure (Figure. Decision Tree for Populating --OBJ).`
11. M4: 恢复 PDF Required bullet (放 Expected 前); Core 表加 D6 标注 (或删, 若信息全由三条 bullet 承载).
12. M5 / M6: 两张表加 D6 标注; M6 注明 AFTER 的适用情形或删表.
13. L10: :1300 "value" → "result".

### 计数更正
HIGH 4 (H1-H4) / MEDIUM 6 (M1-M6) / LOW 13 (L1-L13). verdict 仍为 **CONDITIONAL**.

## attempt 4 复审 (2026-11-26, 同一 reviewer lane, oh-my-claudecode:code-reviewer / opus)

- 对象: ch04 md5 `4ea2579c4a8b7229a433d75e9c44cf92` (vs base +323/−230); a3→a4 delta = `diff -U0 $S/a3.md $S/a4.md` 205 行, 逐 hunk 核.
- **verdict: PASS** (无 HIGH/MEDIUM 残留; 1 条 LOW 观察, 不阻断).

### 命令 (S 同上, 输出不截断)
```
table_census --manifest $S/manifest.json --out $S/census_a4.json   # exit 1 (全局 RED)
  → status {'UNPARSEABLE': 38, 'OK': 19, 'DIFF': 1}; DIFF 只有 ch04:1328 (T-1); pdf_only 落在 p22-59 = []
fp_match --out $S/fp_a4.jsonl --baseline fp_baseline.jsonl --regress-out $S/fp_regress_a4.jsonl   # exit 1
  → 全局 REGRESS 15, p22-59 内 0; ch04 对 base 只有 ig34_p0013_a019 (hit_any 记 ch02, norm 子串仍在 ch04 = True); 对 a3 丢失 0; 本批不命中 = p43_a034 / p56_a005 / p56_a006 (预期 3)
python3 tools/check_links.py | grep "broken relative" → broken relative links: 18668 (live docs: 42)
反向复扫 (正文逐句 + 表格逐格, 跳过 KB note 块/代码围栏/标题) → 剩余不命中行全部可归类: KB note 下的汇总表 (Core / --STRF / --STRTPT / §4.4.10 变量表)、PDF 单元格折行 (qspi / suppqspi / MK / 日期表 / suppmh / 基线表)、CRF "[ ]" 样式、导航标签、已登记笔误 (:651 / :1176 / :1321 / :1480)、:60 URL 括号写法. 未发现新的未标注 KB 解释句
```

### 修正清单落实
| ref | 结果 | 证据 |
|---|---|---|
| H1 | ch04:832 "14 days 7 hours 57 minutes \| P14DT7H57M" ✓; 整表 10×2 对 p41 130dpi 渲染逐格一致 (含 "12¼" / "4 ½") | p41 渲染 |
| H2 | ch04:223-225 MK 表 7 列×1 行与 p28 渲染逐格一致 (MKTEST / MKLOC 折行已合并) | p28 渲染 |
| H3 | 伪节号与 3 个小标题已删; 7 条合进一个 D6 块 (:248-261), 内容不与 p28 矛盾 (--TESTCD 8 字符与 PDF 一致) | p28 |
| H4 | Mermaid 逻辑 = p34 图: 根→Parent record exists?; Yes→Topic variable coded? (Yes --DECOD / No topic variable value); No→Name … coded? (Yes coded / No verbatim); 上方加 D6 | p34 渲染 |
| M1 | [P][n][W] 恢复 PDF 顺序; 6 条移到列表后的 D6 块 | p40-41 |
| M2 | :7 Overview 加 D6; :15 拆回 PDF 原句, :17 单独 D6 | p22 |
| M3 | 标题 = PDF; 两个子标题已删, 4 条连成一个列表 | p37 |
| M4 | Required / Expected / Permissible 三条 bullet + 3 条子 bullet = p23 层级与顺序; Core 表移到列表后加 D6 | p23 渲染 |
| M5 / M6 | 两表加 D6; M6 关于 AFTER 的说明与 p44 两种情形一致 | p43 / p44 渲染 |
| L1-L7, L9-L13 (12 条) | 全部落实 (L6 note 移到 4.5.1.2 末 :1284; L13 改编号; L10 "result"; L12 去 Note 标签; L2 恢复 "Note that"; L5 措辞已补); L8 批外已由主控转出 | diff |
| N1 | 缺项日期表 2 格 "2003-12-15T-:15" / "2003-12-15T13:-:17" = p40 渲染 | p40 渲染 |
| N2 | §4.2.7.1 5 张小表 (CMINDC ×3: OTHER / FRACTURE / BROKEN ARM; QNAM\|QLABEL\|QVAL ×2: CMINDOTH \| Other Indication \| BROKEN ARM) 与 p32 渲染逐格一致, 位置 = 各编号选项下 | p32 渲染 |

不可机检表 32→38: 新增 6 张 (MK 1 + §4.2.7.1 5) 已逐格人工核, 均一致; 另核了触碰过的时长表 / 日期表.

### writer 剩余归类抽核 (21 条, 独立对 pdf_pages / 渲染)
p40_a024 ("quantity of time", 原子错) / p41_a010 ("ISO 8601 representation") / p51_a014 (原子含西里尔 С) / p56_a001 / p57_a001 (PDF 带 "(see Section 8.4.1 …), but is not required") / p57_a015 (PDF "prespecified occurrences") / p58_a007 (PDF 带 "(1)… (2)…") / p59_a010 (PDF "until the subject dies") / p59_a025 / p37_a002 (PDF 少 "in", T-3) / p49_a008 (occurrs, T-4) / p57_a011 ("result or of", T-6) / p23_a010 (URL 括号写法) / p29_a030 (破折号空格) / p39_a016 ("e.g." 逗号) / p25_a015 (原子表头 QSTRESU, PDF/KB 为 QSSTRESU) / p47_a017 (原子每行重复 VISIT, PDF 仅块首) / p58_a017 (PDF "has no response") / p59_a030 (原子 "--BE … is required", PDF "ABLFL, but is not required") / p26_a037 (VISTNUM, T-7) / p32_a014 (CRF 样式) — 21/21 归类成立.

### LOW (观察, 不阻断)
- ch04:43-45 p23 渲染中 "Required" / "Expected" / "Permissible" 为粗体, KB 去掉了粗体 (原 KB 只粗了 Expected). 纯格式, 可选恢复.
