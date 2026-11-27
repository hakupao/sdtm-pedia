# T4 解冻轮 W2 (规格 §2: 结构 / 标题 / D6) — writer checkpoint
<!-- chain: E (plans) -->
> 状态: **已写入 knowledge_base (未 commit)**, 2026-11-27, writer oh-my-claudecode:executor (opus), attempt 1. 不自评 PASS.
> 规格: `subagent_prompts/t4/t4_thaw_spec_v1.0.md` §2; 依据: `t4_user_decisions.md` §000 / §1 A5 表, `work/out_of_scope_findings.md` O35/O38/O41/O48/O56/O60, `t2_dispatch_notes.md` (D6 / S-MOD2 / S-MOD3 / S-TDM / S-INT 口径).
> 基线: HEAD 3a24a1c (KB 索引 md5 `29eaa90f82530add622432f9987e2850`, 未变) + W1 未提交改动. W2 前树快照 `work/scratch/t4/W2_writer/kb_w1/`, HEAD 展开副本 `kb_head/` (`git archive HEAD knowledge_base | tar -x`), W2 前 KB diff `pre_W2_full.diff`.
> 本 writer 亲自看过的渲染页: sv20 p54、p55、p59、p60、p64、p65、p66; SDTMIG p152. 其余 PDF 页 (sv20 p51-53/p56-58/p61-63/p67-69 的标题与 Qualified 列, SDTMIG p15-16、p256、p277-281、p344、p364、p382、p384、p415、p427、p431) 只核了文本层 `work/pdf_pages/`.
> W1 改动保全: W1 的 61 条 `+` 行在 W2 后树中全部仍在 (`python3 -I .work/10_tier_b_repair/work/scratch/t4/W2_writer/w1_preserve.py` → `W1 + lines 61 missing 0`); W2 改动 13 个文件, 其中 FA/assumptions、PP/examples、CE/examples、PC/examples 与 W1 重叠, 重叠文件的 W1 行未动.

## 1. 变更清单 (W2 部分; 行号 = 终态)

| 项 | 文件:行 | before → after 摘要 | PDF 页 | 入站链接 |
|---|---|---|---|---|
| A5-1 | model/05:29 :45 :89 :109 :140 :158 :178 | 7 个四级节 `### 5.1.x.y …` → `#### 5.1.x.y …` (文字不变). "补 PDF 节号 + 原名" 已由 S-MOD3 S-1/M-1 完成 (15 个标题 = PDF 编号原标题 + 保留的 "(XX)"), 本轮核对一致, 未再改字 | sv20 p51-58 | 0 (见 §3) |
| A5-2 | model/05:97-99, :117-119 | TT/TP 表列名 `Notes` → `Usage Restrictions`; 表上 KB note 改写: "表只在 5 个基本列外加 PDF Usage Restrictions 列; rows 3-7 (TP 3-10) 为其值; 例外: DOMAIN 格 "TT"/"TP" 不是 Usage Restrictions 值 (该 PDF 格空), 是 PDF Notes 列的缩写" | sv20 p54-55 渲染 (DOMAIN 行 Usage Restrictions 空, Notes "…must be "TT"" / "…"TP"") | 0 |
| A5-3 | model/05:213-229 | TS 表加第 6 列 `Usage Restrictions`; #9 TSVALCD / #10 TSVCDREF / #11 TSVCDVER 填 `Not in nonclinical trials`, #1-#8 空; 表上新增 KB note (同 TT/TP 式, 不含 DOMAIN 例外句). `#` 编号未动 | sv20 p59-60 渲染 (三格均三行 "Not in / nonclinical / trials") | 0 |
| A5-4 | model/06:75 | QLABEL Role `Synonym Qualifier` → `Synonym Qualifier (QNAM)` (PDF Variable(s) Qualified = QNAM). model/05 17 个 Synonym/Variable Qualifier 括注逐个对 PDF Qualified 列核对, 已一致, 不改; model/06 其余 Role 无 Qualified 值 | sv20 p66 渲染; p51-62 文本层 | — |
| A5-5 | model/06:5, :23 :52 :86 :103 :121 :138 :158 | `## Overview` → `## 6 Datasets for Representing Relationships`; 6.1-6.5/6.7 加 "Dataset" (如 `## 6.1 Related Records Dataset (RELREC)`); 6.6 `Associated Persons Related Subjects (APRELSUB)` → `Associated Persons Relationships (APRELSUB)`. "(XX)" 按 S-MOD3 规则保留. **H1 决定**: H1 `# SDTM v2.0 — Chapter 6: Datasets for Representing Relationships` 不改 (已含 PDF 章名; 按 S-MOD2 M-3 / model/05 先例 "H1 + `## 5 Study-level Data`" 同式, 把 PDF 章标题落在 `##` 而非改 H1) — 请主控/reviewer 确认 | sv20 p64 渲染; p65-69 文本层 (p65-66 另渲染) | 0 |
| A5-6 | model/06:33 (新) | RELREC 表上新增 `> KB note (not in SDTM v2.0): the Notes cells of USUBJID and POOLID in the table below are KB-authored; these PDF Notes cells are blank.` 两格内容不动 (不清空) | sv20 p64-65 渲染 (USUBJID/POOLID Notes 空) | — |
| A5-7 | model/06:40 | RELREC APID Notes 由截断句补为 PDF 全文 (两句: 单人/群组/池 + "若 APID 指池须有 POOLDEF 记录 (see Section 6.3 …, Section 4 …)"); 与 SUPP-- APID 格同文 | sv20 p64 渲染 | — |
| A5-8 | model/06:48 (原 :46-:55) | 删 `### RELTYPE Combinations` + KB note + 4 行 KB 自写表 → 一行 `> See [ch08_relationships.md §8.3.1](…#831-relrec-dataset-relationship-example) for the dataset-level RELTYPE combinations (SDTMIG v3.4).` (ch08 §8.3.1 列 ONE/ONE、ONE/MANY、MANY/MANY 3 种数据集级组合) | IG p431 §8.3.1 (KB ch08:171-179) | 标题 `RELTYPE Combinations` 入站 0 |
| A5-8 | model/06:186 | Summary 表 SUPP-- "Subject-level?" 格 `Yes` → `Parent record (USUBJID, APID, POOLID, or SPDEVID)` (= sv20 SUPP-- 表 4 个标识变量) | sv20 p65-66 | — |
| A5-9 | domains/TI/assumptions.md:3 | `## §7.4 Trial Eligibility and Summary (TI, TS) — Introduction` → `## §7.4 Trial Eligibility and Summary (TI and TS)` | IG p415 | 0 |
| A5-10 | domains/PP/examples.md:112 (原 :112-:170) | 删 `## RELREC Method Quick Reference (PP-side view)` 整节 (含 D6 note、Method 映射表、4 个 Method 小节、Method C 简表、阅读说明; 59 行) → 一行 `> See [PC/examples.md](../PC/examples.md#63593-relating-pp-records-to-pc-records--worked-examples) for the RELREC Methods A-D worked examples (SDTMIG v3.4 §6.3.5.9.3).` :110 既有斜体指针未动 (范围外 O65). 删前核: 该节 bullet 句是 PC/examples.md :70-:147 中 PDF 句的改写 (PDF 原句均在 PC 侧), 无仅由此节承载的 PDF 内容 | IG p277-279 | 标题入站 0; 新链接锚点 = PC/examples.md:60 标题 slug |
| A5-11 TA | domains/TA/assumptions.md:3, :74 | `## Trial Design Model Overview (§7.1)` → `## §7.1 Introduction to Trial Design Model Datasets`; `## Trial Arms and Trial Elements (§7.2)` → `## §7.2 Experimental Design (TA and TE)`. :80-:106 同型合并标题不在列项, 未改 (O66) | IG p382, p384 | 0 |
| A5-11 FA | domains/FA/assumptions.md:95-97 | `## §6.4.4 FA – Description/Overview` 拆为 `## §6.4.4 Findings About Events or Interventions (FA)` + 空行 + `## FA – Description/Overview` (+2 行). 层级: 与同文件 §6.4.x / `FA – Specification` 同为 `##`. S-INT "无正文章级标题不落地" 只管 §5/§6/§7 章级; 本处是域级节 (同文件 `## §6.4.5 Skin Response (SR)` 先例, 其下也只有指针), 故按 A5-11 "PDF 原标题" 落地 | IG p364 (连续两行标题) | 0 |
| A5-11 MB | domains/MB/examples.md:3 | `## §6.3.5.7.3 Microbiology Specimen and Microbiology Susceptibility Examples` → `## §6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples` | IG p256 | 0 (入站 `MB/examples.md#example-1..3` 指 `### Example N`, 未变) |
| A5-11 SS | domains/SS/examples.md:3 | `##### Example 1` → `## Example 1` (只改层级; 同其他域 examples.md; 不加 `## SS – Examples`, 同 U-10⑦ 口径) | IG p344 | 0 (slug `example-1` 不变) |
| A5-13 | domains/RELREC/assumptions.md:5 | `> KB note (not in SDTMIG): the next paragraph and list are from …` → `> Note: the next paragraph and list are from the SDTMIG v3.4 §8 introduction (p427).` (A5-14 来源说明类; 消除 "not in / from" 字面矛盾) | IG p427 | — |
| A5-14 | 5 行 (见 §2) | 来源/位置说明类 `> KB note (not in SDTMIG):` → `> Note:` | — | — |
| A5-12 / A5-15 | — | = A, 未改 | — | — |
| U-10② | domains/CE/examples.md:39 | `**CRF: CE Example 2 — Clinical Events with Severity**` → `**CRF**` (PDF 同位置标签 "CRF", 渲染 p152 确认; 写法选 `**CRF**` 照 PDF 无冒号, 库内另有 4 处 `**CRF:**` 体例, 未统一) | IG p152 渲染 | 0. 同型 :7 / :70 未改 (O64) |
| U-10③ | chapters/ch02_fundamentals.md:158 / :167 | 不改: PDF p15-16 §2.7 同位置只有正文句, 无标签/标题 → 保留, 不加 D6, 登记 **O63** (同型 :133 / :178 一并记) | IG p15-16 | — |
| 台账 | `work/t2_pdf_typo_registry.jsonl` 行 140 (B-PCPP T-6) | `span_count_in_file` 2→1, `span_lines_in_file` [66,152]→[66], 加 `t4_w2_note` (A5-10 删掉的简表表头曾是第 2 处 `\| RDOMAIN \|`; 目标行 :66 不变). 其余 271 行逐字节不变 (改前副本 `scratch/t4/W2_writer/registry.pre_W2.jsonl`); 逐条核: W2 只改变了这 1 条登记的 span 命中行 | — | — |

完整标题 old → new 表 (给 W3 / heading_diff):

| 文件 | 旧 | 新 |
|---|---|---|
| model/05 | `### 5.1.1.1 Trial Elements (TE)` 等 7 个 (5.1.1.1-2 / 5.1.3.1-2 / 5.1.4.1-3) | 同文字 `####` |
| model/06 | `## Overview` | `## 6 Datasets for Representing Relationships` |
| model/06 | `## 6.1 Related Records (RELREC)` | `## 6.1 Related Records Dataset (RELREC)` |
| model/06 | `## 6.2 Supplemental Qualifiers (SUPP--)` | `## 6.2 Supplemental Qualifiers Dataset (SUPP--)` |
| model/06 | `## 6.3 Pool Definition (POOLDEF)` | `## 6.3 Pool Definition Dataset (POOLDEF)` |
| model/06 | `## 6.4 Related Subjects (RELSUB)` | `## 6.4 Related Subjects Dataset (RELSUB)` |
| model/06 | `## 6.5 Device-subject Relationships (DR)` | `## 6.5 Device-subject Relationships Dataset (DR)` |
| model/06 | `## 6.6 Associated Persons Related Subjects (APRELSUB)` | `## 6.6 Associated Persons Relationships (APRELSUB)` |
| model/06 | `## 6.7 Related Specimens (RELSPEC)` | `## 6.7 Related Specimens Dataset (RELSPEC)` |
| model/06 | `### RELTYPE Combinations` | (删) |
| TI/assumptions | `## §7.4 Trial Eligibility and Summary (TI, TS) — Introduction` | `## §7.4 Trial Eligibility and Summary (TI and TS)` |
| TA/assumptions | `## Trial Design Model Overview (§7.1)` | `## §7.1 Introduction to Trial Design Model Datasets` |
| TA/assumptions | `## Trial Arms and Trial Elements (§7.2)` | `## §7.2 Experimental Design (TA and TE)` |
| FA/assumptions | `## §6.4.4 FA – Description/Overview` | `## §6.4.4 Findings About Events or Interventions (FA)` + `## FA – Description/Overview` |
| MB/examples | `## §6.3.5.7.3 Microbiology Specimen and Microbiology Susceptibility Examples` | `## §6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples` |
| SS/examples | `##### Example 1` | `## Example 1` |
| PP/examples | `## RELREC Method Quick Reference (PP-side view)` + 5 个 `###` 子标题 | (删) |

## 2. A5-14 全量 D6 分类清单

判定口径: 只说明 "来源 / 位置 / 本节或本文件对应 PDF 哪里" → `> Note:`; KB 自写内容 (解释、补充值、C-code 说明、KB 自写表 / 图 / 列说明、Structure 行) → 保留原前缀; 拿不准 → 保留.
- 判 "来源/位置说明 → 改" 共 5 条: RELREC/assumptions:5 (来源 §8 引言 p427)、PC/examples:3、PP/examples:3、MS/examples:3、EX/examples:5 (这 4 条都写 "共用例节是 PDF 哪一节、各部分在哪个文件").
- PC/assumptions:5 ("This section covers the PC and PP domains") **保留**: 只概括本节内容, 不指出来源或位置; 与 ch04:7 ("This section describes … It covers …", 保留) 同型, 按 "拿不准保留" 同判. (attempt 1 内曾先改后撤回, 终态 = W2 前原样.)
- 刻意保留: model/02:314 ("PDF 是一张表, KB 拆成子表, 行号随 PDF") — 说明的是 KB 自己做的拆表 (KB 自写表结构), 属 "KB 自写表说明", 保留; TV/examples:7 ("本例基于 TA Example Trial 1 …") 含 KB 对设计的概括, 拿不准, 保留.
- 对账: W2 前 170 条 − 删 2 (model/06:48 随 A5-8, PP:114 随 A5-10) + 新增 2 (model/05:215 TS、model/06:33 RELREC) − 改 `> Note:` 5 = 终态 165 条 (脚本实数 `old 170 new 165 converted 5 deleted 2 added 2`). C-code note 59 条全部保留 (`ct_assert` notes 59 不变).
- 前缀依赖 (给 W3): `scripts/t3/t3_reverse_trace.py` 把 `> KB note (not in SDTM…)` 行判 KB_NOTE 豁免, `scripts/t2s/typo_assert.py` / `typo_plan.py` 把 `> KB note` 块视为不动区. 改为 `> Note:` 的 5 行今后不再走这两条豁免 (reverse_trace 会把它们当正文找 PDF 出处, 预计 5 行 NOPDF). sdtm-rag 代码无 "KB note" 依赖 (grep `--include="*.py"`, 排除 vendor/knowledge_base 副本, 0 命中).
- 复跑: `python3 -I .work/10_tier_b_repair/work/scratch/t4/W2_writer/d6_classify.py .work/10_tier_b_repair/work/scratch/t4/W2_writer/kb_w1 knowledge_base <out.md>` (表中 "W1 后行" = W2 前树行号).

| # | 文件 | W1 后行 | 终态行 | 类别 | 改否 | 摘要 (≤12 词) |
|---|---|---|---|---|---|---|
| 1 | chapters/ch02_fundamentals.md | 55 | 55 | KB 自写: 解释/补充/摘要内容 | 保留 | Example domains by class — Interventions: Exposure (EX), Concomitant Medications (CM), Procedures |
| 2 | chapters/ch02_fundamentals.md | 115 | 115 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | The following Mermaid diagram is the KB rendering of the PDF figure |
| 3 | chapters/ch04_general_assumptions.md | 7 | 7 | KB 自写: 解释/补充/摘要内容 | 保留 | This section describes basic concepts, business rules, and assumptions that should be |
| 4 | chapters/ch04_general_assumptions.md | 17 | 17 | KB 自写: 解释/补充/摘要内容 | 保留 | The SDTM describes the general conceptual framework, including the general observation classes |
| 5 | chapters/ch04_general_assumptions.md | 50 | 50 | KB 自写: 表/列说明 | 保留 | summary table of the Core designations above. |
| 6 | chapters/ch04_general_assumptions.md | 260 | 260 | KB 自写: 解释/补充/摘要内容 | 保留 | topic/test variable conventions (KB summary). |
| 7 | chapters/ch04_general_assumptions.md | 533 | 533 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 8 | chapters/ch04_general_assumptions.md | 824 | 824 | KB 自写: 解释/补充/摘要内容 | 保留 | other ISO 8601 duration designators: |
| 9 | chapters/ch04_general_assumptions.md | 894 | 894 | KB 自写: 解释/补充/摘要内容 | 保留 | Partial dates should not be used to derive study day |
| 10 | chapters/ch04_general_assumptions.md | 905 | 905 | KB 自写: 解释/补充/摘要内容 | 保留 | VISITDY is the planned study day, not the actual study day; do |
| 11 | chapters/ch04_general_assumptions.md | 906 | 906 | KB 自写: 解释/补充/摘要内容 | 保留 | **VISIT**: character name of the visit from the protocol |
| 12 | chapters/ch04_general_assumptions.md | 936 | 936 | KB 自写: 表/列说明 | 保留 | summary table of --STRF / --ENRF (allowable values as stated below). |
| 13 | chapters/ch04_general_assumptions.md | 957 | 957 | KB 自写: 表/列说明 | 保留 | summary table of --STRTPT / --STTPT / --ENRTPT / --ENTPT. AFTER is |
| 14 | chapters/ch04_general_assumptions.md | 981 | 981 | KB 自写: 解释/补充/摘要内容 | 保留 | **Example applications:** |
| 15 | chapters/ch04_general_assumptions.md | 1003 | 1003 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram and caption are a KB rendering of the |
| 16 | chapters/ch04_general_assumptions.md | 1076 | 1076 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following variable table and Mermaid diagram are a KB rendering of |
| 17 | chapters/ch04_general_assumptions.md | 1255 | 1255 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 18 | chapters/ch04_general_assumptions.md | 1305 | 1305 | KB 自写: 解释/补充/摘要内容 | 保留 | --ORRES, --STRESC, and --STRESN are null when --STAT = "NOT DONE"; --ORRESU |
| 19 | chapters/ch08_relationships.md | 454 | 454 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 20 | domains/AE/spec.md | 548 | 548 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 21 | domains/AG/spec.md | 377 | 377 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 22 | domains/BE/spec.md | 231 | 231 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 23 | domains/BS/spec.md | 323 | 323 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 24 | domains/CE/spec.md | 296 | 296 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 25 | domains/CM/spec.md | 377 | 377 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 26 | domains/CO/spec.md | 125 | 125 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 27 | domains/CP/spec.md | 566 | 566 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 28 | domains/CV/spec.md | 386 | 386 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 29 | domains/DA/spec.md | 251 | 251 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 30 | domains/DD/spec.md | 116 | 116 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 31 | domains/DM/examples.md | 113 | 113 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 32 | domains/DM/examples.md | 159 | 159 | KB 自写: 解释/补充/摘要内容 | 保留 | The CRF presents 7 race questions (RACE01-RACE07) with checkbox options: |
| 33 | domains/DM/examples.md | 234 | 234 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 34 | domains/DM/examples.md | 255 | 255 | KB 自写: 解释/补充/摘要内容 | 保留 | The CRF collects ETHNIC (Hispanic or Latino / Not Hispanic or Latino) |
| 35 | domains/DM/examples.md | 290 | 290 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 36 | domains/DM/examples.md | 326 | 326 | KB 自写: 解释/补充/摘要内容 | 保留 | The CRF presents 7 race questions (RACE01-RACE07) with the same structure as |
| 37 | domains/DM/examples.md | 382 | 382 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 38 | domains/DM/examples.md | 414 | 414 | KB 自写: 解释/补充/摘要内容 | 保留 | The CRF presents 5 racial designations plus "Unknown" and "Other" options: |
| 39 | domains/DM/spec.md | 298 | 298 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 40 | domains/DS/spec.md | 152 | 152 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 41 | domains/DV/spec.md | 152 | 152 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 42 | domains/EC/spec.md | 413 | 413 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 43 | domains/EG/spec.md | 404 | 404 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 44 | domains/EX/examples.md | 5 | 5 | 位置说明 (EX/EC 共用 §6.1.3.3, EC 指向此处) | 改 `> Note:` | Examples for EX and EC are shared in Section 6.1.3.3 of the |
| 45 | domains/EX/spec.md | 341 | 341 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 46 | domains/FA/examples.md | 283 | 283 | KB 自写: 解释/补充/摘要内容 | 保留 | *The FA Example 6 CRF shows severity assessed at Visits 2-6 for |
| 47 | domains/FA/spec.md | 278 | 278 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 48 | domains/FT/spec.md | 350 | 350 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 49 | domains/GF/spec.md | 521 | 521 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 50 | domains/HO/spec.md | 260 | 260 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 51 | domains/IE/spec.md | 170 | 170 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 52 | domains/IS/spec.md | 494 | 494 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 53 | domains/LB/spec.md | 566 | 566 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 54 | domains/MB/spec.md | 431 | 431 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 55 | domains/MH/assumptions.md | 53 | 53 | KB 自写: 解释/补充/摘要内容 | 保留 | The SDTMIG v3.4 PDF prints "MHENDTYP" in this sentence; based on the |
| 56 | domains/MH/spec.md | 251 | 251 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 57 | domains/MI/spec.md | 341 | 341 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 58 | domains/MK/spec.md | 386 | 386 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 59 | domains/ML/spec.md | 341 | 341 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 60 | domains/MS/examples.md | 3 | 3 | 位置说明 (MB/MS 共用例节, MS 表在此, 其余见 MB) | 改 `> Note:` | MB and MS share a combined examples section (6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility |
| 61 | domains/MS/examples.md | 9 | 9 | KB 自写: 解释/补充/摘要内容 | 保留 | This example shows susceptibility testing results following organism identification. |
| 62 | domains/MS/spec.md | 557 | 557 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 63 | domains/NV/spec.md | 386 | 386 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 64 | domains/OE/spec.md | 476 | 476 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 65 | domains/OI/spec.md | 71 | 71 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 66 | domains/PC/assumptions.md | 5 | 5 | KB 自写: 解释/补充/摘要内容 | 保留 | This section covers the Pharmacokinetics Concentration (PC) and Pharmacokinetics Parameters (PP) domains. |
| 67 | domains/PC/examples.md | 3 | 3 | 位置说明 (PC/PP 共用例节, 各部分所在文件) | 改 `> Note:` | PC and PP share a combined examples section (§6.3.5.9.3 Relating PP Records |
| 68 | domains/PC/spec.md | 377 | 377 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 69 | domains/PE/spec.md | 278 | 278 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 70 | domains/PP/examples.md | 3 | 3 | 位置说明 (PC/PP 共用例节, PP 表在此, 其余见 PC) | 改 `> Note:` | PC and PP share a combined examples section (6.3.5.9.3 Relating PP Records |
| 71 | domains/PP/examples.md | 106 | 106 | KB 自写: 表/列说明 | 保留 | The shared PP dataset contains 12 rows showing PK parameters (PPTESTCD TMAX, |
| 72 | domains/PP/examples.md | 114 | — | A5-10 整节删除, 改为一行交叉引用 | 删 (随 A5-8/A5-10) | this entire section (from this heading to the end of the file, |
| 73 | domains/PP/spec.md | 242 | 242 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 74 | domains/PR/spec.md | 413 | 413 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 75 | domains/QS/spec.md | 323 | 323 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 76 | domains/RE/spec.md | 431 | 431 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 77 | domains/RELREC/assumptions.md | 5 | 5 | 来源说明 (以下段落/列表来自 §8 引言 p427) | 改 `> Note:` | the next paragraph and list are from the SDTMIG v3.4 §8 introduction |
| 78 | domains/RELREC/spec.md | 73 | 73 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 79 | domains/RELSPEC/examples.md | 11 | 11 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 80 | domains/RELSPEC/spec.md | 64 | 64 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 81 | domains/RELSUB/spec.md | 55 | 55 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 82 | domains/RP/spec.md | 332 | 332 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 83 | domains/RS/spec.md | 422 | 422 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 84 | domains/SC/spec.md | 224 | 224 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 85 | domains/SE/spec.md | 125 | 125 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 86 | domains/SR/spec.md | 359 | 359 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 87 | domains/SS/spec.md | 206 | 206 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 88 | domains/SU/spec.md | 341 | 341 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 89 | domains/SUPPQUAL/spec.md | 100 | 100 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 90 | domains/SV/spec.md | 152 | 152 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 91 | domains/TA/examples.md | 22 | 22 | KB 自写: 解释/补充/摘要内容 | 保留 | A simple parallel trial with 3 arms (Placebo, Drug A, Drug B), |
| 92 | domains/TA/examples.md | 34 | 34 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 93 | domains/TA/examples.md | 53 | 53 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 94 | domains/TA/examples.md | 83 | 83 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 95 | domains/TA/examples.md | 116 | 116 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 96 | domains/TA/examples.md | 165 | 165 | KB 自写: 解释/补充/摘要内容 | 保留 | Each arm represents a different order of treatments. |
| 97 | domains/TA/examples.md | 171 | 171 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 98 | domains/TA/examples.md | 186 | 186 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 99 | domains/TA/examples.md | 237 | 237 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 100 | domains/TA/examples.md | 290 | 290 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 101 | domains/TA/examples.md | 361 | 361 | KB 自写: 解释/补充/摘要内容 | 保留 | A trial with multiple branches: randomization at screening plus response evaluation after |
| 102 | domains/TA/examples.md | 367 | 367 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 103 | domains/TA/examples.md | 389 | 389 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 104 | domains/TA/examples.md | 426 | 426 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 105 | domains/TA/examples.md | 466 | 466 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 106 | domains/TA/examples.md | 525 | 525 | KB 自写: 解释/补充/摘要内容 | 保留 | A cyclical chemotherapy oncology trial with repeating treatment/rest elements until disease progression. |
| 107 | domains/TA/examples.md | 529 | 529 | KB 自写: 解释/补充/摘要内容 | 保留 | Maximum of 4 cycles assumed in this example. |
| 108 | domains/TA/examples.md | 533 | 533 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 109 | domains/TA/examples.md | 549 | 549 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 110 | domains/TA/examples.md | 576 | 576 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 111 | domains/TA/examples.md | 604 | 604 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 112 | domains/TA/examples.md | 640 | 640 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 113 | domains/TA/examples.md | 705 | 705 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 114 | domains/TA/examples.md | 725 | 725 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 115 | domains/TA/examples.md | 787 | 787 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 116 | domains/TA/examples.md | 807 | 807 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 117 | domains/TA/examples.md | 873 | 873 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 118 | domains/TA/examples.md | 895 | 895 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 119 | domains/TA/examples.md | 935 | 935 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 120 | domains/TA/spec.md | 98 | 98 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 121 | domains/TD/examples.md | 5 | 5 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following label and Mermaid diagram are a KB rendering of the |
| 122 | domains/TD/examples.md | 58 | 58 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following label and Mermaid diagram are a KB rendering of the |
| 123 | domains/TD/examples.md | 109 | 109 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following label and Mermaid diagram are a KB rendering of the |
| 124 | domains/TI/spec.md | 80 | 80 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 125 | domains/TM/spec.md | 53 | 53 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 126 | domains/TR/spec.md | 296 | 296 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 127 | domains/TS/spec.md | 107 | 107 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 128 | domains/TU/spec.md | 287 | 287 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 129 | domains/TV/examples.md | 7 | 7 | KB 自写: 解释/补充/摘要内容 | 保留 | This example is based on TA Example Trial 1, a Parallel Design |
| 130 | domains/TV/examples.md | 11 | 11 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | the following Mermaid diagram is a KB rendering of the PDF figure |
| 131 | domains/TV/examples.md | 57 | 57 | KB 自写: 解释/补充/摘要内容 | 保留 | Visit 2 spans the Screen → Run-In epoch transition (confirmation of eligibility). |
| 132 | domains/UR/spec.md | 395 | 395 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 133 | domains/VS/spec.md | 350 | 350 | KB 自写: C-code 说明 (ct_assert 计数 59) | 保留 | C-codes after the parenthesised codelist names are NCI codelist codes added by |
| 134 | model/01_concepts_and_terms.md | 124 | 124 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | Mermaid rendering of the PDF figure "Concept Map. Relationships Between SDTM Domains" |
| 135 | model/01_concepts_and_terms.md | 180 | 180 | KB 自写: 解释/补充/摘要内容 | 保留 | Example variables for each subclass: |
| 136 | model/02_observation_classes.md | 41 | [41, 95] | KB 自写: 表/列说明 | 保留 | The Key Notes column is KB-written: most cells quote or condense the |
| 137 | model/02_observation_classes.md | 95 | [41, 95] | KB 自写: 表/列说明 | 保留 | The Key Notes column is KB-written: most cells quote or condense the |
| 138 | model/02_observation_classes.md | 160 | 160 | KB 自写: 解释/补充/摘要内容 | 保留 | The Findings class has the largest number of variables due to the |
| 139 | model/02_observation_classes.md | 164 | 164 | KB 自写: 表/列说明 | 保留 | The Key Notes column is KB-written: most cells quote or condense the |
| 140 | model/02_observation_classes.md | 287 | 287 | KB 自写: 表/列说明 | 保留 | The Notes column is KB-written: most cells quote or condense the PDF |
| 141 | model/02_observation_classes.md | 314 | 314 | KB 自写: 表/列说明 | 保留 | The PDF presents the 48 timing variables as one table; the KB |
| 142 | model/02_observation_classes.md | 316 | 316 | KB 自写: 表/列说明 | 保留 | In the timing sub-tables, the Notes column is KB-written: most cells quote |
| 143 | model/03_special_purpose_domains.md | 15 | 15 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per subject |
| 144 | model/03_special_purpose_domains.md | 21 | 21 | KB 自写: 表/列说明 | 保留 | The Notes column is KB-written: most cells quote or condense the PDF |
| 145 | model/03_special_purpose_domains.md | 66 | 66 | KB 自写: 表/列说明 | 保留 | This table is a KB summary of the reference date variables in |
| 146 | model/03_special_purpose_domains.md | 85 | 85 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per comment per subject (or per study). The Comments |
| 147 | model/03_special_purpose_domains.md | 119 | 119 | KB 自写: 解释/补充/摘要内容 | 保留 | Elements are blocks of time. |
| 148 | model/03_special_purpose_domains.md | 125 | 125 | KB 自写: 表/列说明 | 保留 | The Notes column is KB-written: the DOMAIN and SEUPDES cells quote or |
| 149 | model/03_special_purpose_domains.md | 151 | 151 | KB 自写: 表/列说明 | 保留 | The Notes column is KB-written: the DOMAIN cell condenses the PDF Notes |
| 150 | model/03_special_purpose_domains.md | 176 | 176 | KB 自写: 表/列说明 | 保留 | The Notes column is KB-written: the DOMAIN cell condenses the PDF Notes |
| 151 | model/03_special_purpose_domains.md | 203 | 203 | KB 自写: 解释/补充/摘要内容 | 保留 | Examples of disease milestones: diagnosis, progression, relapse, remission. |
| 152 | model/03_special_purpose_domains.md | 209 | 209 | KB 自写: 表/列说明 | 保留 | The Notes column is KB-written: the DOMAIN and MIDS cells quote or |
| 153 | model/04_associated_persons.md | 17 | [17, 27] | KB 自写: 多行引用块 (下接 KB 列表) | 保留 |  |
| 154 | model/04_associated_persons.md | 27 | [17, 27] | KB 自写: 多行引用块 (下接 KB 列表) | 保留 |  |
| 155 | model/05_study_level_data.md | 97 | 97 | KB 自写: 表/列说明 (A5-2 措辞随列名改写) | 保留前缀, 措辞改 | the Notes column below is not the PDF Notes column: rows 3-7 |
| 156 | model/05_study_level_data.md | 117 | 117 | KB 自写: 表/列说明 (A5-2 措辞随列名改写) | 保留前缀, 措辞改 | the Notes column below is not the PDF Notes column: rows 3-10 |
| 157 | model/05_study_level_data.md | 261 | 263 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per device attribute per device |
| 158 | model/05_study_level_data.md | 279 | 281 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | Mermaid rendering of the PDF figure "Concept Map. Relationships Between Device Identifier |
| 159 | model/05_study_level_data.md | 299 | 301 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per taxon per non-host organism |
| 160 | model/05_study_level_data.md | 317 | 319 | KB 自写: PDF 图的 Mermaid/表格重绘说明 | 保留 | Mermaid rendering of the PDF figure "Concept Map. Relationships Between Non-host Organism |
| 161 | model/06_relationship_datasets.md | 25 | 25 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per related record, group of records, or dataset |
| 162 | model/06_relationship_datasets.md | 48 | — | A5-8 KB 自写 RELTYPE 表连同 note 删除, 改为 ch08 交叉引用 | 删 (随 A5-8/A5-10) | the RELTYPE combinations table below is KB-authored. |
| 163 | model/06_relationship_datasets.md | 63 | 56 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per supplemental qualifier per related parent domain record(s) |
| 164 | model/06_relationship_datasets.md | 89 | 82 | KB 自写: 解释/补充/摘要内容 | 保留 | Separate Supplemental Qualifier datasets of the form supp--.xpt are required (e.g., suppae.xpt, |
| 165 | model/06_relationship_datasets.md | 97 | 90 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per pooled subject per pool |
| 166 | model/06_relationship_datasets.md | 114 | 107 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per relationship per subject |
| 167 | model/06_relationship_datasets.md | 132 | 125 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per device-subject relationship |
| 168 | model/06_relationship_datasets.md | 151 | 144 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per associated person relationship |
| 169 | model/06_relationship_datasets.md | 167 | 160 | KB 自写: Structure 行 (KB 概括) | 保留 | **Structure:** One record per specimen identifier per subject |
| 170 | model/06_relationship_datasets.md | 188 | 181 | KB 自写: 表/列说明 | 保留 | this summary table is KB-authored. |

## 3. 入站链接核查 (改标题前后; 命令与原始输出)

结论: 被改 / 删的标题全库 0 入站锚点链接. 命中项全部指向未改动的锚点 (MB `### Example N`、TA/examples 标题), 删/改标题的旧 slug 0 命中. 新增两条链接的目标: `PC/examples.md:60` (slug `63593-relating-pp-records-to-pc-records--worked-examples`)、`ch08_relationships.md:156` (slug `831-relrec-dataset-relationship-example`); `check_links` 不校验锚点, slug 按 github-slugger 规则手算.

```
$ grep -rnE 05_study_level_data\.md#|06_relationship_datasets\.md# knowledge_base web/src tools docs
(exit 1)
$ grep -rnE TI/assumptions\.md#|TA/assumptions\.md#|FA/assumptions\.md#|MB/examples\.md#|SS/examples\.md#|PP/examples\.md#|CE/examples\.md# knowledge_base web/src tools docs
knowledge_base/domains/MS/examples.md:7:> See [MB Example 1](../MB/examples.md#example-1) for the example description and the mb.xpt and relrec.xpt tables of this example.
knowledge_base/domains/MS/examples.md:36:> See [MB Example 2](../MB/examples.md#example-2) for the example description and the be.xpt, suppbe.xpt, mb.xpt and suppmb.xpt tables of this example.
knowledge_base/domains/MS/examples.md:60:> See [MB Example 3](../MB/examples.md#example-3) for the example description and the be.xpt, suppbe.xpt, bs.xpt, relspec.xpt, mb.xpt, suppmb.xpt, di.xpt and relrec.xpt tables of this example.
knowledge_base/chapters/ch04_general_assumptions.md:1584:> See [../domains/MB/examples.md#example-3](../domains/MB/examples.md#example-3) for this text (SDTMIG v3.4 §6.3.5.7, RELSPEC rows, p261).
(exit 0)
$ grep -rnE \]\(assumptions\.md#|\]\(examples\.md# knowledge_base/domains/TI knowledge_base/domains/TA knowledge_base/domains/FA knowledge_base/domains/MB knowledge_base/domains/SS knowledge_base/domains/PP knowledge_base/domains/CE
knowledge_base/domains/TA/assumptions.md:96:> See [examples.md#example-2](examples.md#example-2) for this text.
knowledge_base/domains/TA/assumptions.md:100:> See [examples.md#distinguishing-between-branches-and-transitions](examples.md#distinguishing-between-branches-and-transitions) for this text.
(exit 0)
$ grep -rnE \]\(# knowledge_base/model/05_study_level_data.md knowledge_base/model/06_relationship_datasets.md knowledge_base/domains/TI knowledge_base/domains/TA knowledge_base/domains/FA knowledge_base/domains/MB knowledge_base/domains/SS knowledge_base/domains/PP knowledge_base/domains/CE
(exit 1)
$ grep -rniE quick-reference|reltype-combinations|trial-design-model-overview|trial-arms-and-trial-elements|7-4-trial|74-trial-eligibility|644-fa|microbiology-specimen-and knowledge_base web/src tools docs
(exit 1)
```

## 4. defhome 自查 (sdtm-rag 只读脚本)

命令: `/Volumes/DevSSD/Project/sdtm-rag/.venv/bin/python -I /Volumes/DevSSD/Project/sdtm-rag/.work/10_split_and_public/evidence/probes/defhome_rules.py .work/10_tier_b_repair/work/scratch/t4/W2_writer/kb_head/knowledge_base knowledge_base` (old = HEAD 展开副本, new = 工作树 W1+W2)

```
R0: old 64 new 67 chapters_new ['02', '03', '04', '05', '06']
R4: old 72 new 75 chapters_new ['02', '03', '04', '05', '06']
R4n: old 107 new 116 chapters_new ['02', '03', '04', '05', '06']
  R4 vs 旧KB现状(R0) 在旧KB上的差: +{'DOMAIN': '02', 'USUBJID': '02', 'POOLID': '02', 'TAETORD': '02', 'EPOCH': '02', 'RPHASE': '02', 'MIDS': '02', 'APID': '04'} -[] chg{}
  R4n vs 旧KB现状(R0) 在旧KB上的差: +{'STUDYID': '02', 'DOMAIN': '02', 'USUBJID': '02', 'POOLID': '02', 'SPDEVID': '02', 'TAETORD': '02', 'EPOCH': '02', 'RPHASE': '02', 'MIDS': '02', 'RFXSTDTC': '03', 'RFXENDTC': '03', 'RFCSTDTC': '03', 'RFCENDTC': '03', 'SITEID': '03', 'BRTHDTC': '03', 'ARM': '03', 'ACTARMUD': '03', 'DMDTC': '03', 'DMDY': '03', 'SESEQ': '03', 'ELEMENT': '03', 'SESTDTC': '03', 'SEENDTC': '03', 'SESTDY': '03', 'SEENDY': '03', 'SVPRESP': '03', 'SVOCCUR': '03', 'SVREASOC': '03', 'SVCNTMOD': '03', 'SVEPCHGI': '03', 'SVSTDTC': '03', 'SVENDTC': '03', 'SVSTDY': '03', 'SVENDY': '03', 'SVUPDES': '03', 'SMSEQ': '03', 'SMSTDTC': '03', 'SMENDTC': '03', 'SMSTDY': '03', 'SMENDY': '03', 'APID': '04', 'REFID': '06', 'SPEC': '06'} -[] chg{}
var old/R0 old/R4 old/R4n new/R0 new/R4 new/R4n
EPOCH - 02 02 - 02 02
TAETORD - 02 02 - 02 02
MIDS - 02 02 - 02 02
APID - 04 04 - 04 04
REFID - - 06 - - 06
SPEC - - 06 - - 06
VISIT 02 02 02 02 02 02
VISITNUM 02 02 02 02 02 02
VISITDY 02 02 02 02 02 02
RPPLDY 02 02 02 02 02 02
RPPLSTDY 02 02 02 02 02 02
RPPLENDY 02 02 02 02 02 02
MIDSDTC 02 02 02 02 02 02
RELMIDS 02 02 02 02 02 02
RSUBJID 04 04 04 04 04 04
RDEVID 04 04 04 04 04 04
SREL 04 04 04 04 04 04
USUBJID - 02 02 - 02 02
POOLID - 02 02 - 02 02
DOMAIN - 02 02 - 02 02
RPHASE - 02 02 - 02 02
RPATHCD - - - - - -
RSTGCD - - - - - -
RSTAGE - - - - - -
RDOMAIN 06 06 06 06 06 06
R4n 新增(相对 new R0): ['ACTARMUD', 'APID', 'ARM', 'BRTHDTC', 'DMDTC', 'DMDY', 'DOMAIN', 'ELEMENT', 'EPOCH', 'MIDS', 'POOLID', 'REFID', 'RFCENDTC', 'RFCSTDTC', 'RFXENDTC', 'RFXSTDTC', 'RPHASE', 'SEENDTC', 'SEENDY', 'SESEQ', 'SESTDTC', 'SESTDY', 'SITEID', 'SMENDTC', 'SMENDY', 'SMSEQ', 'SMSTDTC', 'SMSTDY', 'SPDEVID', 'SPEC', 'STUDYID', 'SVCNTMOD', 'SVENDTC', 'SVENDY', 'SVEPCHGI', 'SVOCCUR', 'SVPRESP', 'SVREASOC', 'SVSTDTC', 'SVSTDY', 'SVUPDES', 'TAETORD', 'TSGRPID', 'TSPARM', 'TSPARMCD', 'TSSEQ', 'TSVAL', 'TSVALNF', 'USUBJID']
```

逐键差 (`scratch/t4/W2_writer/defhome_diff.py`, 同两个参数, 用同一 rag venv 跑):

```
R0 added {'TSVALCD': '05', 'TSVCDREF': '05', 'TSVCDVER': '05'} removed [] changed {}
R4 added {'TSVALCD': '05', 'TSVCDREF': '05', 'TSVCDVER': '05'} removed [] changed {}
R4n added {'TSGRPID': '05', 'TSPARM': '05', 'TSPARMCD': '05', 'TSSEQ': '05', 'TSVAL': '05', 'TSVALCD': '05', 'TSVALNF': '05', 'TSVCDREF': '05', 'TSVCDVER': '05'} removed [] changed {}
```

- R0 / R4: 相对 HEAD **只多 TSVALCD / TSVCDREF / TSVCDVER → 05**, 无删除无改映射 (符合预期).
- R4n (不看 Notes 是否为空): 另多 TSSEQ / TSGRPID / TSPARMCD / TSPARM / TSVAL / TSVALNF → 05 — TS 表全表升为 6 格行、这 6 行第 6 格为空所致 (STUDYID / DOMAIN 原已在 R4n 归 02, 不变). rag 现用规则要求第 6 格非空, 不受影响; 若 rag 将来改用 R4n 口径须知会.
- 表行级 (`scratch/t4/W2_writer/model_rows.py`, 比较每行 内格数 / 第 6 格是否非空): model/*.md 数字首格行 527 → 527; 变化仅 TS 表 11 行 (5 格 → 6 格; #9-#11 非空, #1-#8 空). 其他 model 表行 (含 model/06 RELREC USUBJID/POOLID/APID、SUPP-- QLABEL、TT/TP) 内格数与第 6 格空否均不变; `#` 编号未动.

## 5. 断言

- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (≤ 42).
- `typo_assert.py knowledge_base --plan .work/10_tier_b_repair/work/t2_batches/T4-THAW.typo.plan.jsonl` → exit 1, `changed files 25, changed lines 67, violations 86` (W1 终态 16 / 61 / 65). 用打印全部的 scratch 副本 (`sed 's/errs\[:60\]/errs/'`) 与 W1 原文 `scratch/t4/W1_writer/typo_assert_final_all.txt` 做 comm: W2 新增 25 条, 全落在 W2 改的 13 个文件, 种类只有 `tree != HEAD + plan` / `changed heading line` (标题改动) / `changed kbnote line` (A5-14 改前缀) / `line count` (FA +2、PP −58、model/05 +2、model/06 −7) / PP `registry span count changed '| RDOMAIN |'` (A5-10 删简表表头, 见 §1 台账行); 消失 4 条 = FA:39/:51、PP:16/:19 的 W1 逐字符条目, 因该文件行数变了脚本改报 `line count` (W1 改动仍在, 见文首保全检查). 无 CRF / 排版字符相关违规. 门禁为排版闭表, 结构改动必然 FAIL, 本轮未改脚本、未追加 fixed 清单. 原文: `scratch/t4/W2_writer/typo_assert_after_W2_all.txt`, 新增清单 `typo_new_in_W2.txt`.
- `ct_assert.py` → exit 1, `got` 行与 W1 改前/改后**完全相同** (`notes: 59`), 差异只是 `non-spec.md file differs from HEAD` 由 16 条变 25 条 (加 W2 的 9 个新文件); spec.md 0 改动 (`git diff --name-only -- 'knowledge_base/domains/*/spec.md'` 为空). 原文 `scratch/t4/W2_writer/ct_assert_after_W2.txt`.
- Mermaid: W2 未触及任何围栏块 (对 W2 前/后树逐文件 difflib, 13 个改动文件 fenced-hunks 全为 0 (PC/assumptions 撤回前已同为 0); W2 diff 中 三连反引号 / mermaid / `-->` 命中 0) → 按规格 §2.16 不需重渲染, 未跑 `t4_mermaid_render.sh`.

## 6. `git diff --stat -- knowledge_base` (W1+W2 合计, 相对 HEAD)

```
 knowledge_base/chapters/ch02_fundamentals.md       |  2 +-
 .../chapters/ch04_general_assumptions.md           | 40 ++++++-------
 knowledge_base/domains/BS/assumptions.md           |  2 +-
 knowledge_base/domains/CE/examples.md              | 24 ++++----
 knowledge_base/domains/DS/examples.md              |  6 +-
 knowledge_base/domains/EG/examples.md              |  2 +-
 knowledge_base/domains/EX/examples.md              |  2 +-
 knowledge_base/domains/FA/assumptions.md           |  8 ++-
 knowledge_base/domains/FA/examples.md              |  2 +-
 knowledge_base/domains/IS/examples.md              |  6 +-
 knowledge_base/domains/MB/examples.md              |  2 +-
 knowledge_base/domains/MS/examples.md              |  2 +-
 knowledge_base/domains/NV/assumptions.md           |  2 +-
 knowledge_base/domains/NV/examples.md              |  2 +-
 knowledge_base/domains/PC/examples.md              | 16 +++---
 knowledge_base/domains/PP/examples.md              | 66 ++--------------------
 knowledge_base/domains/RELREC/assumptions.md       |  2 +-
 knowledge_base/domains/SM/examples.md              |  2 +-
 knowledge_base/domains/SS/examples.md              |  2 +-
 knowledge_base/domains/TA/assumptions.md           |  4 +-
 knowledge_base/domains/TA/examples.md              |  2 +-
 knowledge_base/domains/TI/assumptions.md           |  2 +-
 knowledge_base/domains/TS/assumptions.md           | 10 ++--
 knowledge_base/model/05_study_level_data.md        | 54 +++++++++---------
 knowledge_base/model/06_relationship_datasets.md   | 35 +++++-------
 25 files changed, 118 insertions(+), 179 deletions(-)
```

W2 单独 (W2 前树快照 → 终态, `git diff --no-index --stat .work/10_tier_b_repair/work/scratch/t4/W2_writer/kb_w1 knowledge_base`): 13 files, 57 insertions(+), 118 deletions(-) — CE 2、EX 2、FA/assumptions 4、MB 2、MS 2、PC/examples 2、PP 62、RELREC 2、SS 2、TA/assumptions 4、TI 2、model/05 54、model/06 35 (行数 = +/− 合计).

## 7. 范围外发现 (未改) / 需主控定
1. **O63** (U-10③ 登记): ch02:158/:167 KB 自拟 `###` 标题, PDF 同位置无标签; 同型 :133/:178. 保留, 不加 D6.
2. **O64**: CE/examples.md:7 / :70 与已改 :39 同型的 `**CRF: CE Example n — …**` (p151 标签 "CRF"; p153 表单题 "Bone Fracture Assessment"). 规格只列 :39.
3. **O65**: PP/examples.md:110 KB 既有斜体指针 ("See PC examples for …") 与 A5-10 新增交叉引用行内容重叠 (两行相邻). 规格只授权 :112 起整节.
4. **O66**: TA/assumptions.md:80-106 合并 / 自拟 `###` 标题 (`§7.2.1 Trial Arms (TA) – Description/Overview` 等), 同 FA §6.4.4 型, 不在 A5-11 列项.
5. **需主控定 (a)**: model/06 H1 未改 (理由见 §1 A5-5). 若要求 H1 字面改为 "6 Datasets for Representing Relationships", 则与 model/05 / model/02-04 H1 体例不一致.
6. **需主控定 (b)**: TT/TP 列改名后, DOMAIN 格 "TT"/"TP" 留在 `Usage Restrictions` 列下 (rag 读第 6 格非空, 清空会使 rag 映射变化, 故按规格只改 note 并写明例外). 若要彻底一致需同时与 sdtm-rag 协调.
7. **需主控定 (c)**: A5-14 改为 `> Note:` 的 5 行将失去 `t3_reverse_trace.py` KB_NOTE 豁免与 `typo_assert` 不动区待遇 (W3 重算时预计这 5 行出现在反向追踪 NOPDF 中).
8. sdtm-rag 对 "anti-drift / Quick Reference (PP / PP-side" 的全量 grep (含 py/yaml/yml/json/jsonl/md/toml, 仅排除 .venv, 未截断): `docs/evidence/checkpoints/` 5 个历史检索快照 JSON (记录过该 section 名, 非代码依赖) + `vendor/sdtm-pedia/` 子模块副本 30 个 (.work 12 / archive 8 / releases 9 / knowledge_base 1, 即本仓钉住版本的拷贝); `scripts/` `server/` `eval/` `tests/` `data/` 0 命中. A5-10 删节后该 section 在 rag 下次钉新 KB tag 时消失.
9. 台账: 仅 B-PCPP T-6 一条随 A5-10 更新 span 计数 (§1; 改前副本 `scratch/t4/W2_writer/registry.pre_W2.jsonl`). 复核命令 `python3 -I .work/10_tier_b_repair/work/scratch/t4/W2_writer/registry_span_delta.py` → 272 条中 span 命中行 W2 前后有变化的只有 `B-PCPP T-6 … [66, 152] -> [66]`.
