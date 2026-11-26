# T2 checkpoint — B-TE (writer, attempt 1)

- base HEAD (start): `d33674e` (HEAD 运行中被他批推进到 `884560f`; `git diff --stat d33674e HEAD -- knowledge_base/domains/T{A,E}` 为空, 本批文件基线未变)
- base md5: TE/assumptions.md `d39fc8fd40f6c57168870991187ffb12`; TE/examples.md `a68e9b97c3643b97f0488e4dad43eb1c`; TA/assumptions.md `ea6bd5233aff46ae8b3d99ce9fc8cbd4`
- after md5: TE/assumptions.md `31755a61375a08e79f4bb7b3b9824d65`; TE/examples.md `caf18faeed5551832544a02ded3bb6f1`; TA/assumptions.md `e7234e69d34e4258d072f7a3fdd1c455`
- kb_files: TE/assumptions.md, TE/examples.md + 主控授权 TA/assumptions.md (仅 §7.2.2.1 TE Issues 块, X-1)
- 真值: `work/pdf_pages/ig34_p0402..0407.txt` + pdftoppm 渲染 p402-407 (r110), 逐格看图

## O20 页范围
TE 节实际 PDF 范围 = **p402 (底部 7.2.2 标题 + Description/Overview) – p407 (7.3 之前)**. batch json `pdf_ranges` 写 404-409 不对 (408-409 是 TV). 本批按 402-407 全扫; batch json 未改 (只登记), 供 O20 全检与 auditor 抽样用.

## 变更清单
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | TE/assumptions.md:13 | ig34_p0403_a011 | INSERTED | 补 "A valid element has a name that describes the purpose…conditions for leaving the element." | 403 |
| 2 | TE/assumptions.md:13 | NEW-1 (词替换) | REPLACED | "not a valid trial element" → "not a valid element" (恢复 PDF 原词; 只会提高该行其它原子匹配, 不删句) | 403 |
| 3 | TE/assumptions.md:11/13 | NEW-2 (段落) | REPLACED | ":11 一段拆为两段 (PDF "sequence of steps called elements." 后分段) | 403 |
| 4 | TE/assumptions.md:15-17 | NEW-3 (spec 首句) | INSERTED | 新增 `## TE — Specification` + "te.xpt, Trial Elements — Trial Design. One record per planned Element, Tabulation." (CM 先例) | 403 |
| 5 | TE/assumptions.md:19 | NEW-4 (标题) | INSERTED | 新增 `## TE — Assumptions` (PDF "TE – Assumptions"; 沿用本文件 "—" 风格) | 403 |
| 6 | TE/assumptions.md:27 | NEW-5 (assumption 4 尾) | INSERTED | 补 2 句 "For example, every arm of a trial that involves treating disease episodes… might be randomization." | 404 |
| 7 | TE/assumptions.md:45 | NEW-6 (assumption 13) | REPLACED | "element and WBC counts have recovered" → "element and after WBC values have recovered" | 404 |
| 8 | TE/assumptions.md:47 | NEW-7 (assumption 14, D2 删扩写) | REPLACED | "expressed in ISO 8601 format." → "expressed in ISO 8601." | 404 |
| 9 | TE/assumptions.md:49 | ig34_p0404_a012 | INSERTED | 补 "For instance, a washout with a fixed duration of 14 days is different from…after 14 days otherwise." | 404 |
| 10 | TE/examples.md:63 | NEW-8 (结构) | REPLACED | "The choice of elements…" 段缩进 4 格, 归入 item 3 (PDF 渲染在 c. 下缩进) | 406 |
| 11 | TE/examples.md:82 | NEW-9 (3-step 表 Row 2) | REPLACED | "If there is a branch at this point" → "If there is a branch point at this point" | 406 |
| 12 | TE/examples.md:87-95 | NEW-10 (叙述, 原只在 TA 副本) | INSERTED | 补 "As illustrated in the table…" / "It can be useful…" / "However, such a working dataset…" / "The following table shows a fragment…" / "Note that" + 2 bullets | 406 |
| 13 | TE/examples.md:97-100 | pdf_only:p407:special.xpt | TABLE_REBUILT | 整表补: 标题 `**special.xpt**` + 10 列表头 (Row ARM EPOCH TAETORD ELEMENT TESTRL TEENRL TEDUR TABRANCH TATRANS) | 407 |
| 14 | TE/examples.md:101 | ig34_p0407_a003 | INSERTED | Row 1: A / Screen / 1 / Screen / Informed Consent / Screening assessments…Element / (空) / Randomized to A / (空) | 407 |
| 15 | TE/examples.md:102 | ig34_p0407_a004 | INSERTED | Row 2: A / Treatment / 2 / Trt A / First dose of treatment in Element, where drug is Treatment A / 5 days after start of Element / P5D / 空 / 空 | 407 |
| 16 | TE/examples.md:103 | ig34_p0407_a005 | INSERTED | Row 3: A / Treatment / 3 / Rest / Last dose of previous treatment cycle + 24 hrs / 16 days after start of Element and WBC recovers / 空 / 空 / If disease progression, go to Follow-up Epoch | 407 |
| 17 | TE/examples.md:104 | ig34_p0407_a006 | INSERTED | Row 4: 同 Row 2, TAETORD 4 | 407 |
| 18 | TE/examples.md:106 | NEW-11 (叙述, 原只在 TA 副本) | INSERTED | 补 "Note that rows 2 and 4…" 段 (3 句) | 407 |
| 19 | TA/assumptions.md:102-108 | X-1 (D2 去重) | REPLACED | TA §7.2.2.1 两小节正文 → 各一行交叉引用到 `../TE/examples.md#…` (标题保留, 见删除清单) | 406-407 |

atoms 覆盖: 6/6 (a011, a012, a003-a006) 全部 INSERTED. pdf_only 1/1 (special.xpt, 4 行) 已补. census diff_tables = 0.
新增 atom 清单 (R3, 不在 atoms[]): NEW-1 … NEW-11 (上表 #2-8, #10-12, #18).

## 表格逐格 (special.xpt, 对 p407 渲染)
- 空格依渲染: Row1 TEDUR/TATRANS 空; Row2/4 TABRANCH/TATRANS 空; Row3 TEDUR/TABRANCH 空. layout 文本把 "Treatment 2" 串在一起, 以渲染为准拆为 EPOCH=Treatment, TAETORD=2.
- 表名: 渲染为 `special.xpt` (census ds 同). Row 号 PDF 为粗体, 按本文件其它表惯例不加粗.

## 触碰过的 unparseable 表
- TE/examples.md:79 (3-step 表, census 不可机检): 只改 Row 2 一格 ("branch" → "branch point"). 其余格已对 p406 渲染逐格核过一致 (表头 "How step question is answered by information in the TA datasets" 一致). reviewer 须对渲染逐格复核.

## PDF_TYPO / T4 登记 (照录 PDF, 未改)
- T-1 (T4 用户裁定): p407 special.xpt Row 2/4 TESTRL "First dose of treatment **in** Element, where drug is Treatment A"; 同页表下叙述引用为 "First dose of treatment Element, …", TE Ex3 Row 2 (p405) 亦无 "in". 表/叙述自相矛盾 (叙述称 TE 变量值 "exactly the same"). 照录表值.
- T-2 (T4 用户裁定): p407 Row 3 TEENRL "16 days after start of Element and WBC recovers" vs TE Ex3 Row 4 (p405) "At least 16 days after start of Element and WBC recovered". 片段表与 Ex3 多处不同且方式不一, 无唯一确定的正确值 → 照录, 不部分修正.

## 删除清单 (D2)
| file:line (base) | 内容 | 原因 | 保留副本位置 |
|---|---|---|---|
| TA/assumptions.md:104-122 | §7.2.2.1 Distinguishing Elements… 正文 10 句 (逐句一段) | D2 去重: PDF p406 属 §7.2.2.1 (TE) | TE/examples.md:67-73 |
| TA/assumptions.md:126-150 | §7.2.2.1 Transitions Between Elements 正文 (3-step 引句、Note、4 句、Note that + 2 bullets、rows 2 and 4 段 3 句); 原无 3-step 表与 special.xpt 表 | D2 去重: PDF p406-407 属 §7.2.2.1 (TE) | TE/examples.md:77-106 |

- 两个 TA 标题 (`### §7.2.2.1 Trial Elements Issues – Distinguishing…` / `– Transitions Between Elements`) **保留未删**, 每个下面一行 `> See [...](../TE/examples.md#…) for this text.` — 仿 TA/assumptions.md:94-100 既有写法, 保锚点 (规则 6). 与主控 "一行交叉引用" 的差异: 两小节各一行, 共 2 行.
- 删除前 diff: 脚本逐行 (引号归一化) 比 TA:102-150 每句 → 补全后 TE/examples.md, 全部 IN_TE, 0 MISSING. 唯一差异 = 引号样式 (TA:122 用弯引号 “Treatment effect”, TE 用直引号; PDF 为弯引号) — 不影响内容, 不改.
- 锚点 grep (未截断): `grep -rn -i -E "distinguishing-elements|transitions-between-elements|7-2-2-1|trial-elements-issues|TA/assumptions.md#"` 全仓 (除 releases/archive/.git) → 0 命中; 标题文本 "Trial Elements Issues" 在 knowledge_base/docs/.work 中除被改块外无引用.

## 双向全扫 (p402-407)
- PDF→KB: Description/Overview (p402) 一致; p403 Overview 4 段 (补 a011 + 分段); spec 首句补 (spec 表属 spec.md, 不在 kb_files, 未核 → 已由 O15/O21 类扫描兜底); assumptions 1-15 (补 4 尾、13 改、14 改、15 补); TE Examples 引言、Ex1/Ex2/Ex3 三表逐格对渲染一致 (Ex3 Row1/Row4 TEDUR 空一致); §7.2.2.1 Granularity 1-3 + a-c 一致; Distinguishing 4 段一致; Transitions 3-step 表 (改 1 格) + 余下叙述 + special.xpt 已补.
- KB→PDF: TE/assumptions.md、TE/examples.md 全文件每句均在 PDF p402-407 找到 (改后); 无 KB 自写内容. 标题 "## Trial Elements Issues" (PDF "7.2.2.1 Trial Elements Issues") 为导航, 保留.
- 引号: KB 多处直引号 vs PDF 弯引号 (assumption 1/5/13, examples:73) — 样式差, 未改.

## 范围外发现
- F-1: TE/spec.md (p403 spec 表 + 脚注 ¹) 不在本批 kb_files, 未核 → 并入 O15/O24/O26 spec 扫描.
- F-2: B-TE.json pdf_ranges 404-409 错 (应 402-407) → O20.

## 链接检查
- `python3 tools/check_links.py | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`; 改前同值 42 (未升). 新交叉引用 `../TE/examples.md#…` 未进坏链清单.
- ⚠ 过程事故: 为取改前基线, 我在共享工作树执行了 `git stash` + `git stash pop` (约数秒). pop 无冲突, `git stash list` 为空, 本批文件 md5 与改后一致; 但该窗口内其它并行 agent 若读写工作树可能看到被暂存的状态 → 主控请核对并行批 (BE/MK/TU 等) 的工作树改动完整.

## git diff --stat
```
 knowledge_base/domains/TA/assumptions.md | 46 ++------------------------------
 knowledge_base/domains/TE/assumptions.md | 18 +++++++++----
 knowledge_base/domains/TE/examples.md    | 25 +++++++++++++++--
 3 files changed, 38 insertions(+), 51 deletions(-)
```
