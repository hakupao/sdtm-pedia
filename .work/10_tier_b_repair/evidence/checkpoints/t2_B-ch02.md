# T2 B-ch02 writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `553b14bbe405fbdc7fb8e752ffd845169d78f11f`
- md5 ch02 before `81065328f17cbd0aa2c5141bc9b6d6eb` → after `ecd032ca63278c3c2fcc533745799263`
- kb_files: 仅 `knowledge_base/chapters/ch02_fundamentals.md`. scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_Bch02_writer/` (ch02_before.md, kbA/kbB 隔离副本, fpA/fpB.jsonl, p11-p15 渲染)
- **RELOCATE 归属**: 本批 `delete_only_source_lines` 为空、无 RELOCATE 原子 → §6.4.2 搬迁的**两侧都不归本批**; 删除侧在 B-FA.json `delete_only_source_lines` (ch02 lines_at_base 219/227, 带 anchors). 本批未碰 ch02 FA 参考节 (改后 :204 起). 因本批插删, 行号已偏移: anchor "2. A split FA domain following" 现 **:213**, "- The DOMAIN value is sponsor-defined" 现 **:221** → B-FA 须按 anchors 定位.
- 真值: p11-p16 页面文本 + p11/p15 渲染 (80dpi). 原子 verbatim 只作检索键 (p12_a001 从句中开始, p13_a025 截在页尾, a012 含双空格).
- 编辑方式: 按行判定 — 单原子错述行原位替换为同一 PDF 句; 多原子行/表先在 PDF 位置插入完整 PDF 原文 (含未分诊的同段兄弟原子, R3), 再按 D2 删去已被逐字覆盖的旧改写/表. 承载判定用 triage kb_loc (triage_merged.json), 删除前确认该行所有映射原子改后均逐字命中.
- 排版: PDF 不换行连字符 (U+2011 ‑‑MODIFY/‑‑LOINC/‑‑ORNRLO/‑‑DOSE, 2‑character) 写成 ASCII "-" (KB 通行写法, fp 归一化等价); 折行 `--\nSTRESN`/`-\n-TEST`/`data-\nexchange`/`cancer-\nvocabulary`/`special-\npurpose` 已合并; p14 弯引号 “efficacy” 与 “--“ 照录; p11 a018 句末无句点照录.
- 所有 `#`/`##`/`###` 标题文字与层级不变 (grep '^#' 前后 diff 为空).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | ch02:25 | ig34_p0011_a007 | INSERTED | :25 段末补 'A role determines ... how it can be used.' | 11 |
| 2 | ch02:39 | ig34_p0011_a014 | INSERTED | 小标题下补引导句 '...categorized into 5 subclasses:' | 11 |
| 3 | ch02:42 | ig34_p0011_a016 | REPLACED | 子类表 Result 行 → PDF bullet (补 'They answer the question...'; 'Result Qualifiers are' 穷举) | 11 |
| 4 | ch02:47 | ig34_p0011_a020 | REPLACED | Example 标签+4 bullet → PDF 段落原文 (补 'term for the adverse event') | 11 |
| 5 | ch02:47 | ig34_p0011_a022 | REPLACED | 同上段 (补 'study day of the start of the event') | 11 |
| 6 | ch02:47 | ig34_p0011_a023 | INSERTED | 段末补 'Additional Timing and Qualifier variables could be included...' | 11 |
| 7 | ch02:51 | ig34_p0011_a025 | INSERTED | §2.2 首句补 | 11 |
| 8 | ch02:51 | ig34_p0011_a027 | INSERTED | 补 'The logic of the relationship may pertain...' | 11 |
| 9 | ch02:53 | ig34_p0011_a029 | REPLACED | '(DOMAIN) used in 4 ways' → PDF 原句 (补 'used consistently throughout the submission') | 11 |
| 10 | ch02:53 | ig34_p0012_a001 | REPLACED | 4 用法列表 → PDF 句, 补 '(see Section 8, Representing Relationships and Data)' | 12 |
| 11 | ch02:55 | ig34_p0012_a004 | INSERTED | 补 'Each dataset is described by metadata definitions...' | 12 |
| 12 | ch02:55 | ig34_p0012_a005 | REPLACED | 'Metadata are described in a Define-XML document' → PDF 原句 (data definition document; to regulatory authorities) | 12 |
| 13 | ch02:55 | ig34_p0012_a006 | INSERTED | 补 Define-XML standard 规定元数据属性句 (含 URL) | 12 |
| 14 | ch02:57 | ig34_p0012_a008 | REPLACED | 'of each variable ... for its use' → 'provide a general description for each variable' | 12 |
| 15 | ch02:63 | ig34_p0012_a014 | INSERTED | 补 'The lists of variables allowed ... found in the SDTM.' | 12 |
| 16 | ch02:65 | ig34_p0012_a015 | REPLACED | GOC 表 Interventions 行 → PDF bullet (study drug / CM 两情形; e.g. 非 i.e.) | 12 |
| 17 | ch02:66 | ig34_p0012_a016 | REPLACED | GOC 表 Events 行 → PDF bullet (randomization / during / prior to trial) | 12 |
| 18 | ch02:71 | ig34_p0012_a018 | REPLACED | 补 'appropriate to a specific collection of data' / 'according to these descriptions' | 12 |
| 19 | ch02:71 | ig34_p0012_a019 | REPLACED | 补 'typically' / 'usually' 限定, 'general observation class' | 12 |
| 20 | ch02:82 | ig34_p0013_a001 | REPLACED | §2.4 表 Study Reference 行 → PDF bullet (全称 + 'provide structures ... used in subject data') | 13 |
| 21 | ch02:88 | ig34_p0013_a008 | INSERTED | 补 'Final domains will be published only in an SDTM implementation guide...' | 13 |
| 22 | ch02:96 | ig34_p0013_a014 | REPLACED | 补 'by specific domain assumptions' | 13 |
| 23 | ch02:97 | ig34_p0013_a015 | REPLACED | '— use SUPP--' 改写 → PDF 三句 (preceding 3 bullets / Section 8.4 / SDTM continues to evolve) | 13 |
| 24 | ch02:98 | ig34_p0013_a016 | REPLACED | 补 'Their metadata should not be changed.' | 13 |
| 25 | ch02:100 | ig34_p0013_a018 | REPLACED | Permissible 拆成 bullet + 子 bullet; Define-XML no-data 句从 :102 移回此子 bullet (PDF 位置) | 13 |
| 26 | ch02:122 | ig34_p0013_a025 | REPLACED | 子 bullet 改写 → PDF 原文 (e.g., electrocardiogram / and so on, as appropriate / Examples of different topics) | 13 |
| 27 | ch02:124 | ig34_p0014_a003 | INSERTED | step 1 下补 'How collected data are used ...' 子 bullet (BP→VS / 肝功能→LB); 旧 Key rules :149 删 (D-13) | 14 |
| 28 | ch02:126 | ig34_p0014_a005 | INSERTED | step 1 下补 domain pair 子 bullet 全文; 旧 Key rules :150-151 删 (D-13) | 14 |
| 29 | ch02:127 | ig34_p0014_a006 | REPLACED | step 2 → PDF 原文 (wiki URL / since the last published version / may be used as custom domains) | 14 |
| 30 | ch02:128 | ig34_p0014_a007 | REPLACED | step 3 'Follow these steps:' → PDF 原文 (无合适模型时选 GOC; As illustrated in the following figure) | 14 |
| 31 | ch02:133 | ig34_p0014_a012 | REPLACED | step e → PDF 原文 (CT 链接 / 申请 URL / 一致使用 / 禁用码) | 14 |
| 32 | ch02:43 | ig34_p0011_a017 | INSERTED | t2_recheck: 随子类 5 bullet 逐字落地 ('equivalent terms'); 偏离 'recheck 不改', reviewer 定 | 11 |

atoms 覆盖: 31/31 (INSERTED 11 / REPLACED 20) + t2_recheck 1 (#32).
**偏离说明 (#32 a017)**: writer prompt 规定 recheck 不改; 但子类 5 条 bullet 必须整体按 PDF 落地 (a016 在其中, 子类表整体被删), a017 的 'equivalent terms' 随之逐字恢复. 未单独为 a017 动任何文字; reviewer 定其 class.

### 新增 atom (R3, 不在 atoms 内; 改后均逐字命中)
p11: a006 a008 a009 a010 a011 a012 a013 a015 a017 a018 a019 a021 a026 a030 / p12: a002 a007 a013 a017 a020 a026 a027 a028 / p13: a010 a011 a012 a013 a019 a021 a023 / p14: a001 a002 a004 a008 a009 a010 a011 a013 a014 / p15: a001 a002 a003 / p16: a014 a019 (T-1 字形) a022.
要点: 角色 5 bullet 恢复 "of the observation (e.g., units, descriptive adjectives)"; §2.5 bullet 1 恢复 "Other Identifiers may be added as needed." 与 PDF 变量顺序 STUDYID, USUBJID, DOMAIN; step 1 子 bullet 'Do not create separate domains based on time' / CRF 条补 "as"; step a/b/c/d/f/g/i/j 补丢失短语 (f 'Replace all variable prefixes ...', j 'See Section 3.2 ...'); §2.6 引言段 (a021-a023); §2.7 三句 (p16 a014/a019/a022).

### 删除清单 (D2; reviewer 逐条确认)
| # | file:line (改前) | 被删内容 | 原因 | 保留/替代 (改后) |
|---|---|---|---|---|
| D-1 | ch02:29-33 | 角色编号列表 "**X variables** — ..." 5 行 | 同句错述 (丢 "of the observation (e.g., units, descriptive adjectives)", "an" vs "the") | 原位换 PDF bullet :31-35 |
| D-2 | ch02:37-43 | 子类表 (表头+5 行, KB 自写表) | 5 行全被 PDF bullet 逐字覆盖; Result 行把穷举写成 Examples 列, 与 PDF 'Result Qualifiers are' 不符 | :41-45 |
| D-3 | ch02:45-49 | "**Example:** ..." + 4 bullet | a020-a022 改写, 被 PDF 段落覆盖 | :47 |
| D-4 | ch02:53 | "A **domain** is a collection of ..." 段 | 同句错述 (丢 'defined as'), 换 PDF 段 (含 a025/a027 插入) | :51 |
| D-5 | ch02:55-59 | "(DOMAIN) used in 4 ways:" + 4 项编号列表 | a029/a030/a001 改写, 被 PDF 句覆盖 | :53 |
| D-6 | ch02:61 句 2 | "Metadata are described in a Define-XML document that is submitted with the data." | a005 错述 | :55 |
| D-7 | ch02:63 句 1 | "The SDTM lists only the name, label, and type of each variable, with a brief set of CDISC guidelines for its use." | a008 错述 (description→use) | :57; 同行 a009/a010 段移到 :59 (PDF 段序) |
| D-8 | ch02:65-69 | "Data represented in SDTM datasets include:" + 4 项 | a007 改写, 被 PDF 句覆盖 | :57 |
| D-9 | ch02:73 | "Most subject-level observations should be ..." | a013 错述 (丢 'collected during the study' 与 3 类名) | :63 |
| D-10 | ch02:75-79 | GOC 表 (KB 自写) | 3 行改写被 PDF bullet 覆盖; Interventions 行 'i.e.' 与 PDF 'e.g.' 矛盾 | :65-67; Examples 列 (PDF 无, 不矛盾) 按 D6 原文保留为 KB note :69 |
| D-11 | ch02:81, 83 | 两句改写 + "**Additional guidance** ... GOC is in Section 8.6.1" | a018/a019/a020 错述 | :71 (a021 交叉引用仍在) |
| D-12 | ch02:91-96 | §2.4 表 (KB 自写) | 4 行改写被 PDF bullet 覆盖 (Examples/Section 列内容均在 PDF 句内) | :79-82 |
| D-13 | ch02:102 句 1 | "The number of domains submitted should be based on ..." | PDF 位于 §2.6 引言 (p13 a022), 已插回 §2.6 | :119 (fp a022 仍命中) |
| D-14 | ch02:102 中句 | "Refer to the Define-XML standard ... no data availability." | PDF 位于 Permissible 子 bullet (a018) | :100 |
| D-15 | ch02:106-112 | 7 条编号规则 | 各条为同一 PDF bullet 的错述 → 原位换 PDF bullet/子 bullet | :94-101 |
| D-16 | ch02:128 | "Process for creating a custom domain (must be based on 1 of the 3 GOC):" | a021/a023 改写 | :119 |
| D-17 | ch02:130 尾句 | "Examples of distinct topics that warrant separate domains include ..." | p14_a001 改写, PDF 在子 bullet 内 | :122 |
| D-18 | ch02:131 | "Data should be grouped by topic and nature, not by collection method ..." | a025 改写 | :122 |
| D-19 | ch02:133-141, 143-144 | step 2/3 与 a-g, i, j 改写 | 同句错述 → 原位换 PDF | :127-138 |
| D-20 | ch02:147-151 | "**Key rules for custom domains:**" + 4 bullet | 全被 step 1 子 bullet (a002/a003/a005) 逐字覆盖 | :123-126 |
| D-21 | ch02:202, 206 后缀 | " — additionally requires the Trial Sets domain" / " — additionally requires the Pool Definition dataset" | 被插入的 PDF note 覆盖; SETCD/POOLID 项 (PRESENT) 保留 | :192/:194, :198/:200 |
另: :25 '**role**.' 与角色名去粗体 (Markdown 粗体贴标点使 fp 归一化不命中; 非内容).

### KB note (D6) 2 处
| ch02:line | 内容 | 依据 |
|---|---|---|
| 69 | GOC 表原 Examples 列原文 (EX/CM/PR; AE/DS/MH; LB/VS/EG) | PDF p12 无此清单, 不矛盾 |
| 105 | Mermaid 图上方一行: KB 版 PDF "Figure. Creating a New Domain" (PDF 在 step 3k 之后) | 图位置未移动 |

### PDF_TYPO
- T-1 (p16 a019): PDF "Trials Sets domain"; KB 写 "Trial Sets" (原 KB 亦如此). 依据: SDTM v2.0 p53 §5.1.2 标题 "Trial Sets"; SDTMIG v3.4 自身无该域名 → 按「补充口径」严格读属"不能由 PDF 自身确定", **请主控/T4 定**是否照录 "Trials Sets". 后果: p16_a019 fp 不命中 (预期).

### census / 不可机检表
- census: 本批 diff_tables / pdf_only / pdf_unparsed 均为 0.
- 触碰的 unparseable 表: ch02:37 (子类表)、:75 (GOC 表)、:91 (§2.4 表) — 三张均为 KB 自写、PDF 为 bullet 列表, 已删除并换 PDF bullet (D-2/D-10/D-12); **reviewer 须对 p11/p12/p13 渲染逐条人工核 bullet 文字**. ch02:165 (§2.7 SEND-only 表) 未改.

### fp_match (隔离副本, 只差 ch02)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_Bch02_writer
cp -R knowledge_base $S/kbA; cp $S/ch02_before.md $S/kbA/chapters/ch02_fundamentals.md; cp -R knowledge_base $S/kbB
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbA --out $S/fpA.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbB --out $S/fpB.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regress.jsonl
  → regressions=0 new_hits=75 RESULT: GREEN; hit_any 回归 0
```
- 本批 31 atoms + recheck a017: 全部 hit_target ch02. 新命中 75 = 31 atoms + 43 R3 + sv20_p0009_a013 (模型层同文).
- p11-p16 仍不命中 22: p15_a006 (FIGURE), p15_a010-a023 + p16_a001-a006 (§2.7 表格式, 范围外 #2), p16_a019 (T-1).
- `python3 tools/check_links.py` → `broken relative links: 18668 (live docs: 42)` = 基线.

### 范围外发现 (未改, 请主控定)
1. ch02:5-21 "Section 1 Context" (p7-10): 引导句后无内容 (如 "organized into the following sections:" / "guides are available at ...:" 后为空), 碎片化.
2. ch02:153-174 §2.7 SEND-only 表: PDF p15-16 为 "--USCHFL (Interventions, Events, Findings)" 式 bullet; 内容一致但 20 原子因格式不命中; :143-149 三句 PDF 引导句集中放在标题前而非各自列表前; :178 "See Section 9.2 ..." 同.
3. ch02:3 "Source: SDTMIG v3.4, Section 2 (Pages 13-20)" — 本 PDF (no header footer) 为 p11-16; 是否印刷页码待核.
4. Mermaid 图位置在 §2.6 开头, PDF 在 step 3k 后 (已 KB note 说明, 未移动).

### git diff --stat
```
 knowledge_base/chapters/ch02_fundamentals.md | 148 +++++++++++++--------------
 1 file changed, 71 insertions(+), 77 deletions(-)
```

## attempt 1 续 (writer 自查补正, 2026-11-26; KB 未再改, md5 仍 `ecd032ca63278c3c2fcc533745799263`)

### 反向逐字核 (KB→PDF)
命令 (repo 根): 用 fp_match.norm / norm_pdf, 把改后 ch02:23-139 及 :187/:194/:200 每行按句切分, 检查是否为 p11-p16 归一化文本的子串 (脚本内联于 writer 会话, 逻辑: `norm(sent) in norm_pdf(p11..p16)`; 跳过标题与 mermaid 节点行).
结果 miss 15, 全部可解释:
- :42 "--STRESN" / :43 "--TEST" / :44 "--POS": PDF 折行 `--\nSTRESN`、`-\n-TEST`、`--\nPOS`, norm_pdf 的去折行正则要求连字符前是字母, 归一化后多一空格; p11 渲染确认为连续的 --STRESN / --TEST / --POS → KB 正确.
- :69 KB note (D6) 8 段、:105 KB note 3 段、:108 `graph TD`: 非 PDF 文字, 预期.
- :194 "Trial Sets": T-1, 见下.
无其它 KB 自造文字.

### 渲染核
- p14 (130dpi 裁切): “efficacy” 弯引号、step f "(shown in the models as “--“)" 与 pdftotext 码位一致 (U+201C ×2), 照录; 子 bullet "o" 层级与 KB 缩进一致. p12/p13 子 bullet 层级 (Permissible 两条 "o") 按 layout 文本缩进核对.

### T-1 定案
- CT (source/cdisc/SDTM Terminology.xlsx sharedStrings) 无 "Trial Sets" / "Trials Sets" (TX 属 SEND).
- 但 SDTM v2.0 PDF (本项目真值源 sv20) p53 §5.1.2 标题即 "Trial Sets", p51 "(Section 5.1.2, Trial Sets)"; SDTMIG 此句引用的就是该模型域. → 正确值可由项目 PDF 真值确定, **KB 写 "Trial Sets"**, 登记 T-1 (依据 sv20 p51/p53). 若主控认为"PDF 自身"仅指 SDTMIG 本身, 则改为照录 "Trials Sets" 并转 T4.

### 措辞更正
- KB note :69 不是"原文保留": Examples 列 9 个域名原样, 但引导语 "Example domains by class — Interventions: …; Events: …; Findings: …" 为新写的框架文字 → **文字改动, 请 reviewer 确认**.
- 「新增 atom (R3)」节 "改后均逐字命中" 更正为: 除 p16_a019 (T-1 字形) 外均命中.
- writer.jsonl: 删去 `unparseable:ch02:165` 的 UNTOUCHED 行 (非法 action); 三条 `unparseable:` TABLE_REBUILT 行 note 改为"表已删除, 由 PDF bullet 替代".

### 需主控决定 (从范围外移入)
- §2.6 Mermaid 图位于节首, 而 step 3 原文 "As illustrated in the following figure" 与 PDF 图位置 (step 3k 之后) 均指向其后 → 是否把图 (连同 :105 KB note) 移到 :139 之后. 本批未移.

## attempt 1 续 2 (主控裁定执行, 2026-11-26)

- md5 after: `d5f9f9b1888b2e304e3104a3cf6cfa5e`; diff --stat: 1 file, +127 / −113. 标题文字/层级仍不变 (grep '^#' diff 为空).
- FA anchors 现位置: "2. A split FA domain following" **:233**, "- The DOMAIN value is sponsor-defined" **:241** (B-FA 按 anchors).

| # | 裁定 | kb 位置 (改后) | action | 摘要 |
|---|---|---|---|---|
| 1 | T-1 | ch02:212 | 照录 + T4 | SDTMIG v3.4 全部 461 页文本中无 "Trial Sets" (§7 无 TX 域; 仅 p16 "Trials Sets" 一处), 只有 SDTM v2.0 p51/p53 能确定 → KB 改为照录 "Trials Sets", **登记 T4 用户裁定项** (依据: sv20 p53 §5.1.2 标题 "Trial Sets"). p16_a019 现逐字命中 |
| 2 | Mermaid | ch02:149-163 | RELOCATE (同文件) | 图从 §2.6 节首移到 step 3k 之后 (PDF 原图位置); 前加 PDF 图题 "**Figure. Creating a New Domain**" (p15 a005, HEADING 原子), D6 标注改为 "KB rendering of the PDF figure above" |
| 3 | :3 页码 | ch02:3 | REPLACED | "Pages 13-20" → "Pages 11-16" (本 PDF 页码口径, 与 ch03 "17-21" / ch04 "22-59" 一致; §2 = p11-p16) |
| 4 | §1 引导句后为空 | ch02:11-22 | INSERTED (R3) | §1.2 "organized into the following sections:" 后补 p7 10 条 bullet 逐字 |
| 5 | 同上 | ch02:26-30 | INSERTED (R3) | §1.4 guides 句前补同句前半 "This implementation guide covers most data ..." (p9), 后补 SDTMIG-AP / -MD / -PGx 3 条 bullet 逐字 |
| 6 | 同上 | ch02:34-43 | INSERTED + 结构 | §1.4.1 三条孤立 bullet 按 PDF 层级恢复: Variable Label 下 2 个子项 (补 "Sponsors should create ..."), "This may be the same ..." 缩为其子项; "The name of an external code system ..." 挂回 "Controlled Terms, Codelist, or Format" > "Controlled Terms" 下, 并补同级 asterisk 项及其 3 个子项 (p10). 只摘该两父项, 其余 1.4.1 内容属 ch01 (B-ch01) |
| 7 | §2.7 表 | ch02:173-192 | TABLE_REBUILT → bullet | KB 两列表 (20 行) → PDF bullet "--USCHFL (Interventions, Events, Findings)" 等 20 条, 值逐行由原表转换, 与 p15-16 文本逐条一致 |
| 8 | §2.7 引导句 | ch02:171, 196, 216 | MOVED (同节) | 三句 PDF 引导句由节首集中处移回各自列表前 (PDF 位置); DM 段 "...where all subjects are human." 与 "See Section 9.2 ..." 合为 PDF 同段 |

### 删除清单 (续)
| # | file:line (续 1 后) | 被删内容 | 原因 | 替代 |
|---|---|---|---|---|
| D-22 | ch02:165-186 | §2.7 SEND-only 两列表 (表头+分隔+20 行) | PDF 为 bullet; 内容 1:1 转为 bullet | :173-192 |
| D-23 | ch02:105-117 (原位置) | Mermaid + KB note | 移位, 非删除 | :149-163 |

### 复验
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_Bch02_writer
cp knowledge_base/chapters/ch02_fundamentals.md $S/kbB/chapters/ch02_fundamentals.md
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbB --out $S/fpC.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regressC.jsonl
  → regressions=0 new_hits=96 RESULT: GREEN; hit_any 回归 0 (对改前副本)
python3 tools/check_links.py | grep 'live docs'  → broken relative links: 18668 (live docs: 42) = 基线
```
- p11-p16 仍不命中仅 1: p15_a006 (FIGURE 描述原子, 以 Mermaid 呈现). §2.7 20 原子 + p16_a019 现命中; §1 新命中 p9 a008/a010/a011/a026, p10 a001/a002.
- reviewer 人工核: §1 补入段 (p7/p9/p10 渲染) 与 §2.7 bullet (p15-16) 须对渲染逐条核; Mermaid 新位置对 p15.

## attempt 2 (auditor FAIL 后, 2026-11-26)

- 失败归档: `evidence/failures/t2_B-ch02_attempt_1.{patch,md}`.
- md5 `d5f9f9b1888b2e304e3104a3cf6cfa5e` → `af07c931748a64d1ef007227d1f00a8c`; diff --stat (vs 553b14b): 1 file, +104 / −126.

| # | 项 | kb 位置 (改后) | action | 摘要 |
|---|---|---|---|---|
| 1 | F1 | ch02:167 | REPLACED (标题括号) | "### Use with extreme caution (not fully evaluated for human clinical trials):" → "(not evaluated for use in human clinical trials):" — 取 p16 "have not been evaluated for use in human clinical trials". 无入链 (grep knowledge_base/web/docs 无 `ch02_fundamentals.md#` 锚点引用), check_links 不变 |
| 2 | §1 去重 (D2, 主控更正续2 #4-6) | ch02:5-7 | REPLACED → 交叉引用 | 保留 `## Section 1 Context (Reference Material)` 标题; 其下引导句 + 3 个 `### From §1.x` 小节 (含续2 补入的 bullet) 整块换为一行 `> See [Chapter 1](ch01_introduction.md) for SDTMIG v3.4 Section 1 (...)`. 原引导句为 KB 自写 (非 PDF §2 页), 一并并入引用 |

### 删除清单 (attempt 2)
| # | file:line (改前, 续2 终态) | 被删内容 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-24 | ch02:7 | "The following statements from Section 1 of the SDTMIG provide reference context ..." | KB 自写导航, 并入交叉引用 | — |
| D-25 | ch02:9-22 | §1.2 小标题 + 引导句 + 10 条章节 bullet | §1 属 ch01 (p7), D2 | ch01 §1.2 (B-ch01) |
| D-26 | ch02:24-30 | §1.4 小标题 + guides 句 + 3 条 bullet | 同上 (p9) | ch01 §1.4 (B-ch01) |
| D-27 | ch02:32-43 | §1.4.1 小标题 + 摘录 (Variable Label / Controlled Terms 层级) | 同上 (p9-10) | ch01 §1.4.1 (B-ch01) |
注: 3 个 `### From §1.x` 标题被删 (锚点无入链, 已 grep 核).

### 复验
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_Bch02_writer
cp knowledge_base/chapters/ch02_fundamentals.md $S/kbB/chapters/ch02_fundamentals.md
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbB --out $S/fpD.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regressD.jsonl
  → regressions=0 (hit_target) new_hits=96 GREEN; p11-16 不命中仅 p15_a006 (FIGURE)
python3 tools/check_links.py | grep 'live docs' → broken relative links: 18668 (live docs: 42) = 基线
```
- hit_any 回归 4 (预期, 均 target=ch01、hit_target 改前即 None): ig34_p0009_a009 / p0009_a020 / p0009_a021 / p0010_a004 — 改前只在 ch02 §1 摘录里命中; **须 B-ch01 在 ch01 补入** (主控已写入 B-ch01 notes). 续2 新增的 p9/p10 hit_any 亦随之撤回.
- FA anchors 现位置: "2. A split FA domain following" **:197**, "- The DOMAIN value is sponsor-defined" **:205**.

## attempt 2 续 (reviewer 复审 CONDITIONAL 修正, 2026-11-26)

- md5 `af07c931748a64d1ef007227d1f00a8c` → `4cc3de33cdbb3e103be04e31cc23cdd5`; diff --stat (vs 553b14b): 1 file, +108 / −130.

| # | kb 位置 | action | before → after | PDF 依据 |
|---|---|---|---|---|
| 1 | ch02:158 | REPLACED (KB 自写小标题补限定) | "Must NEVER be used in DM domain (SEND nonclinical only):" → "Must NEVER be used in DM domain for human clinical trials (SEND nonclinical only):" | p16 "must NEVER be used in the Demographics (DM) domain for human clinical trials" |
| 2 | ch02:178 | REPLACED (同上) | "May be used when appropriate:" → "May be used in human clinical trials when appropriate:" | p16 "may be used in human clinical trials when appropriate" |
锚点: grep knowledge_base/web/src/docs 无 `ch02_fundamentals.md#` 入链.

复验: `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbB --out $S/fpE.jsonl --baseline $S/fpA.jsonl` → regressions=0 new_hits=96 GREEN; p11-16 不命中仅 p15_a006 (FIGURE). `python3 tools/check_links.py | grep 'live docs'` → broken relative links: 18668 (live docs: 42) = 基线.
