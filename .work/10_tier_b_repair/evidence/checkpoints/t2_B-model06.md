# T2 B-model06 — writer checkpoint

## attempt 1

- base HEAD `a2739dd5`; kb_file `knowledge_base/model/06_relationship_datasets.md` md5 `139b62a1fec97412a848efc90c1243b2` → `9bb7f3ef27afd64eeb519365942540cf`
- 页范围核定: SDTM v2.0 §6 起 p64 (标题 "6 Datasets for Representing Relationships"), p70 起 §7 → 完整节页范围 **p64-69** (= batch json pdf_ranges). p63 为 §4 Concept Map 图页, 不属本章.
- 真值: `work/pdf_pages/sv20_p0064-0069.txt` + pdftoppm 渲染 p64-p69 (全部 6 页已打开目视) (scratch `t2_B-model06_writer/`) 核表格单元.
- 口径: 3 atoms 所在 §6.6 两段 (a012-a020, 9 句) 整段逐字补 (只补 3 句会使 "However, this approach…" 等无前文); 其余节叙述按 R3 逐字补; R2 残留改写句 (fp_baseline 无原子命中本文件任何行) 按 D2 删; KB 自写且不矛盾 → D6 `> KB note (not in SDTM v2.0):`.

### 变更清单

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | model/06:147 | sv20_p0068_a012 | INSERTED | §6.6 段 1 首句 "To justify collection of AP data…" | 68 |
| 2 | model/06:149 | sv20_p0068_a019 | INSERTED | §6.6 段 2 "The APRELSUB dataset, which parallels…" | 68 |
| 3 | model/06:149 | sv20_p0068_a020 | INSERTED | §6.6 段 2 末句 "…is required for studies in which SREL values of MULTIPLE appear…" | 68 |
| 4 | model/06:147 | sv20_p0068_a013-a016 | INSERTED | R3 新增: §6.6 段 1 其余 4 句 (ledger INTENTIONAL_EXCLUDE) | 68 |
| 5 | model/06:149 | sv20_p0068_a017-a018 | INSERTED | R3 新增: §6.6 段 2 前 2 句 (ledger INTENTIONAL_EXCLUDE) | 68 |
| 6 | model/06:9-17 | sv20_p0064_a004-a012 | REPLACED | R2/R3: Overview 7 项改写列表 → PDF 原列表 (含 Related Records 下 2 子项 a005/a006, Supplemental 项丢失尾部); 旧列表 D2 删 (D-1) | 64 |
| 7 | model/06:61 | sv20_p0065_a008 | INSERTED | R3: §6.2 "For information on the naming of supplemental qualifier datasets…" | 65 |
| 8 | model/06:95 | sv20_p0067_a002 | INSERTED | R3: §6.3 "This dataset identifies individual subjects included in a pool…"; 旧改写句 D2 删 (D-2) | 67 |
| 9 | model/06:112 | sv20_p0067_a010-a012 | INSERTED | R3: §6.4 3 句 (related subjects / pregnant women / genetically based diseases); 旧改写句 D2 删 (D-3) | 67 |
| 10 | model/06:130 | sv20_p0068_a002-a004 | INSERTED | R3: §6.5 3 句 (DR special-purpose domain…); 旧改写句 D2 删 (D-4) | 68 |
| 11 | model/06 原 :133 (已删, 无改后行) | (§6.6 旧改写句) | D2 删 | "Links associated persons to subjects." 被 a012-a020 取代 (D-5) | 68 |
| 12 | model/06:31/69/99/116/134/153/171 | sv20_p0064_a015, p0065_a009, p0067_a003, p0067_a013, p0068_a005, p0068_a021, p0069_a006 | INSERTED | R3: 表前 PDF 原表题 (`**RELREC Dataset**` 等 7 个) | 64-69 |
| 13 | model/06:124 | sv20_p0067_a019 (RELSUB SREL Label) | REPLACED | VALUE_DIFF: "Subject, Device, or Study Relationship" → "Subject Relationship" (渲染 p67 确认) | 67 |
| 14 | model/06:158 | sv20_p0069_a001 (APRELSUB APID Label) | REPLACED | VALUE_DIFF: "Associated Person Identifier" → "Associated Persons Identifier" (渲染 p69 确认) | 69 |
| 15 | model/06:25-27 | KB_AUTHORED §6.1 Structure + 描述句 | D6 | 加 `> KB note (not in SDTM v2.0):` (PDF §6.1 无叙述) | - |
| 16 | model/06:48 | KB_AUTHORED RELTYPE Combinations 表 | D6 | 表上方单行标注 (不矛盾: PDF 只说值为 ONE/MANY) | 65 |
| 17 | model/06:63-65 | KB_AUTHORED §6.2 Structure + 描述句 | D6 | 标注 | - |
| 18 | model/06:89 | KB_AUTHORED Naming Convention 段 | D6 | 标注 (PDF 把命名交给 IG, 不矛盾) | 65 |
| 19 | model/06:97/114/132/151/167 | KB_AUTHORED 各节 `**Structure:**` 行 | D6 | 标注 | - |
| 20 | model/06:167-169 | KB_AUTHORED §6.7 描述句 | D6 | 与 Structure 同一引用块标注 (PDF §6.7 无叙述) | - |
| 21 | model/06:182 | KB 自写 **Note:** (RELSPEC 新增于 v2.0) | REPLACED (D2 去重) | 为 PDF p6 §1.4 段的改写, 原文已在 model/01:90 → 换一行交叉引用 (D-6) | 6 |
| 22 | model/06:188 | KB_AUTHORED Summary 表 | D6 | 表上方单行标注 | - |
| 23 | model/06:194 | Summary 表 POOLDEF 格 | D2 删扩写 | "Yes (nonclinical)" → "Yes": PDF p64-69 APID 注 "If APID identifies a pool, POOLDEF records must exist" (AP 池, 非仅 nonclinical), p67 RELSUB POOLID 注 "If POOLID is entered, POOLDEF records must exist…" (人体试验 RELSUB 亦用); POOLDEF 无 Usage Restrictions → 与 PDF 矛盾 (D-7) | 64-67 |

覆盖率: atoms[] 3 行 (#1-3) 全在; R3 新增 #4-#12 (原子 a013-a018, p64 a004-a012, p65 a008, p67 a002/a010-a012, p68 a002-a004, 7 个表题); VALUE_DIFF 2; D6 10 处 (#15-#20, #22; #19 含 5 行); D2 删 7 处 (D-1..D-7).
census: diff_tables / pdf_only / pdf_unparsed 均为空.

### 删除清单 (D2, reviewer 逐条确认)

| # | 位置 (原行) | 删除内容 (摘要) | 原因 | 保留 |
|---|---|---|---|---|
| D-1 | 原 :9-15 | Overview 7 项 "**X Dataset** — represents …" 改写列表 | R2 残留改写; 无 fp 原子命中 | :9-17 PDF 原列表 |
| D-2 | 原 :87 | "Defines which subjects belong to each pool (for nonclinical studies…)" | R2 残留改写 (且 "nonclinical" 限定与 PDF 不符) | :95 p67 a002 |
| D-3 | 原 :102 | "Describes relationships between subjects in a study (e.g., family relationships in genetic studies)." | R2 残留改写 | :112 p67 a010-a012 |
| D-4 | 原 :118 | "Links devices to subjects when the device is associated with a subject." | R2 残留改写 | :130 p68 a002-a004 |
| D-5 | 原 :133 | "Links associated persons to subjects." | R2 残留改写 | :147-149 p68 a012-a020 |
| D-6 | 原 :160 | **Note:** RELSPEC added in v2.0 / SDTMIG-PGx / SDTMIG v3.4 | 跨文件重复 (PDF 所属 = §1.4, model/01:90 逐字) | model/01:90; 此处一行交叉引用 |
| D-7 | 原 :170 Summary POOLDEF 格 | " (nonclinical)" | KB 扩写与 PDF 矛盾 | "Yes" |

### PDF_TYPO

- 无. (p69 APRELSUB SREL 注 "…to the subject or pool identified in RDEVID" 疑 PDF 原文措辞问题, 但该 Notes 列 KB 不收, 未登记.)

### 触碰过的 unparseable 表 (reviewer 须人工逐格对渲染)

- :120 RELSUB 表 (原 :104): 改 SREL Label 格 → 对 p67.
- :155 APRELSUB 表 (原 :135): 改 APID Label 格 → 对 p69.
- :190 Summary 表 (原 :166): 改 POOLDEF 格 (KB 自写表, 无 PDF 对应).
- 其余 6 张 (RELREC :33, RELTYPE :50, SUPP-- :71, POOLDEF :101, DR :136, RELSPEC :173) 只在表前加表题 / KB note 行, 单元格未动.

### 需主控定 (未改)

- M-1 (规则 6) 7 个节标题与 PDF 不同: `## 6.1 Related Records (RELREC)` vs PDF "6.1 Related Records Dataset"; 6.2-6.5、6.7 同型 (KB 用 "(CODE)" 后缀, PDF 用 "… Dataset"); `## 6.6 Associated Persons Related Subjects (APRELSUB)` vs PDF "6.6 Associated Persons Relationships" (名称本身不同). 另 H1 "Chapter 6: …" vs PDF "6 Datasets for Representing Relationships"; `## Overview` 无 PDF 对应. 锚点检查: `grep -rn "06_relationship_datasets[a-z._]*#" knowledge_base docs web/src tools .work/AGENT_GUIDE.md README.md` 无输出 (未截断).
- M-2 (R1 范围) RELREC / SUPP-- / RELSPEC 表的 Notes 列: 有截断/改写 (RELREC APID :38、IDVARVAL、RELTYPE 缺 "However, values are only necessary…"、RELID 缺后 3 句; SUPP-- QNAM/QLABEL/QVAL/QORIG/QEVAL 为简写, QORIG 列 "CRF/ASSIGNED/DERIVED" 为 KB 自写), KB 自写 (RELREC USUBJID "Null for dataset-level relationships"、POOLID "For pooled subject data", PDF 该格空), 以及 RELSPEC REFID/SPEC 的 Notes 格放的是 C-code (C82531/C70713, PDF 属 Variable C-code 列). 分三类, 各附建议默认:
  - M-2a R1 明确判 IE 的 6 行 (p64 a017/a019/a020, p65 a001/a002, p68 a023 → KB :35/:37-40/:157): 建议 **维持 IE 不改** (T1.4 已裁).
  - M-2b R1 未裁、Notes 为截断/改写的行 (RELREC IDVAR/IDVARVAL/RELTYPE/RELID; SUPP-- RDOMAIN/IDVAR/IDVARVAL/QNAM/QLABEL/QVAL/QORIG/QEVAL; RELSPEC PARENT/LEVEL): 建议 **按 PDF Notes 逐字恢复** (先例: B-model01 attempt 2 把子类表改写格恢复为 PDF 原文).
  - M-2c PDF Notes 格为空而 KB 有内容 (RELREC USUBJID/POOLID 自写句; RELSPEC REFID/SPEC 格里的 C-code): 建议 **自写句加 D6 标注 (或删), C-code 清空** (C-code 属 R1 不收的 Variable C-code 列).
  POOLDEF/RELSUB/DR/APRELSUB 表无 Notes 列 (按 R1 不补).
- M-4 RELSPEC 表 (:173) SPEC (:178) / LEVEL (:180) Role 格 "Variable Qualifier (REFID)" vs PDF Role "Variable Qualifier" + Variable(s) Qualified "REFID": 括号写法是 model/ 通用约定 (model/02 多处 "Synonym Qualifier (--TRT)" 等), 未改; 但本文件 SUPP-- QLABEL 行 (PDF Qualified=QNAM) 写纯 "Synonym Qualifier", 不一致. 建议: 维持约定, QLABEL 是否补 "(QNAM)" 由主控定.
- M-3 RELREC 表 IDVAR 行 PDF Examples "--SEQ and --GRPID"、SUPP-- QEVAL Examples 未收 (R1 缺列, 按 R1 不补), 列此备查.

### 范围外发现

- 无其他 (本文件全部 p64-69 非表原子已逐字在 KB, 节标题见 M-1).

### git diff --stat

```
 knowledge_base/model/06_relationship_datasets.md | 78 ++++++++++++++++--------
 1 file changed, 51 insertions(+), 27 deletions(-)
```

### 验证 (S = scratchpad/t2_B-model06_writer)

- 双向扫描 PDF→KB: `python3 -I $S/scan.py` (sv20 p64-69 全部非表原子 SENTENCE/LIST_ITEM/HEADING, 去空白/粗体, 判 KB 子串) → `HIT 36 MISS 8`, 8 MISS 全为章/节标题 ("6 Datasets…" + 6.1-6.7, 见 M-1). KB→PDF: 除 M-1/M-2 项外, 非 PDF 内容均已 D6 标注或为导航 (标题 / `### Variables (N variables)` / 交叉引用).
- 表格: `python3 -I $S/tblcheck.py` (7 张 PDF 对应表的 #/Variable/Label/Type/Role 对 TABLE_ROW 原子字段 0/1/2/3/5) → `kb tables 7 pdf tables 7` / `diffs 2` = RELSPEC :178/:180 Role 括号约定 (M-4); 改后 #13/#14 已无差异. 另 2 张 (RELTYPE、Summary) 为 KB 自写 (D6). 渲染 p64-p69 目视复核一致.
- `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census.json` → `KB tables: 9; status: {'UNPARSEABLE': 9}; diffs: 0` GREEN
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_reg.jsonl` → RED, 51 回退全为 ig34 (并行批); `grep -c sv20 $S/fp_reg.jsonl` = 0
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`

- 需主控定共 4 项 (M-1..M-4); trace 行 note 写 "3 需主控定" 早于 M-4 追加, trace append-only 不改, 以本行为准.

## attempt 2 (主控裁定: 只做 M-2b / M-2c)

- md5 `9bb7f3ef…` → `328c4e55502ef57bcd19a1aafab23aa5`; attempt 1 diff 存 scratch `attempt1.patch` (非失败, 仅续改留底). 累计 diff --stat: +69/-45.
- 真值: Notes 格取 `pdf_atoms.jsonl` TABLE_ROW 原子 Notes 字段, 并逐格对渲染 p64-p66/p69 确认该文本位于 PDF Notes 列 (非 Definition 列).
- M-1 / M-3 / M-4 按裁定未改 (O38 → T4).

### 变更清单 (Notes 列)

| # | kb_file:line | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| A2-1 | model/06:36 | sv20_p0064_a018 RELREC RDOMAIN | REPLACED (M-2b) | 补句末句号 | 64 |
| A2-2 | model/06:41 | sv20_p0065_a003 RELREC IDVAR | REPLACED (M-2b) | 补句末句号 | 65 |
| A2-3 | model/06:42 | sv20_p0065_a004 RELREC IDVARVAL | REPLACED (M-2b) | 补 "If --SEQ is the variable…" 句 | 65 |
| A2-4 | model/06:43 | sv20_p0065_a005 RELREC RELTYPE | REPLACED (M-2b) | 补 "However, values are only necessary…" | 65 |
| A2-5 | model/06:44 | sv20_p0065_a006 RELREC RELID | REPLACED (M-2b) | 补后 3 句 (same RELID related / sponsor chooses…) | 65 |
| A2-6 | model/06:74 | sv20_p0065_a012 SUPP-- RDOMAIN | REPLACED (M-2b) | 补句末句号 | 65 |
| A2-7 | model/06:76 | sv20_p0065_a014 SUPP-- APID | REPLACED (M-2b) | KB 空 → PDF Notes 全文 (APID pool / POOLDEF / Section 6.3, Section 4) | 65-66 |
| A2-8 | model/06:79 | sv20_p0066_a003 SUPP-- IDVAR | REPLACED (M-2b) | 补句末句号 | 66 |
| A2-9 | model/06:80 | sv20_p0066_a004 SUPP-- IDVARVAL | REPLACED (M-2b) | 补句末句号 | 66 |
| A2-10 | model/06:81 | sv20_p0066_a005 SUPP-- QNAM | REPLACED (M-2b) | "8-character name…" → PDF 全文 (5 句) | 66 |
| A2-11 | model/06:82 | sv20_p0066_a006 SUPP-- QLABEL | REPLACED (M-2b) | "Human-readable label…" → PDF 全文 (3 句) | 66 |
| A2-12 | model/06:83 | sv20_p0066_a007 SUPP-- QVAL | REPLACED (M-2b) | "The actual data value" → PDF 全文 | 66 |
| A2-13 | model/06:84 | sv20_p0066_a008 SUPP-- QORIG | REPLACED (M-2b) | 'Source of the data: "CRF"…' → PDF 全文 | 66 |
| A2-14 | model/06:85 | sv20_p0066_a009 SUPP-- QEVAL | REPLACED (M-2b) | "Role of the evaluator" → PDF 全文 (2 句) | 66 |
| A2-15 | model/06:179 | sv20_p0069_a012 RELSPEC PARENT | REPLACED (M-2b) | 补句末句号 | 69 |
| A2-16 | model/06:180 | sv20_p0069_a013 RELSPEC LEVEL | REPLACED (M-2b) | 补句末句号 | 69 |
| A2-17 | model/06:177 | sv20_p0069_a010 RELSPEC REFID | 清空 (M-2c) | Notes 格 "C82531" 删 (属 Variable C-code 列) | 69 |
| A2-18 | model/06:178 | sv20_p0069_a011 RELSPEC SPEC | 清空 (M-2c) | Notes 格 "C70713" 删 (同上) | 69 |

### 删除清单追加

| # | 位置 | 删除内容 | 原因 | 保留 |
|---|---|---|---|---|
| D-8 | :81-85 旧 Notes 5 格 | QNAM/QLABEL/QVAL/QORIG/QEVAL 改写短句 (含 KB 自写 QORIG 值列举 "CRF"/"ASSIGNED"/"DERIVED") | M-2b: 被 PDF 原文取代 (R2 残留改写); QORIG 值列举 PDF 无 | 同格 PDF 原文 |
| D-9 | :177/:178 Notes 格 | C82531 / C70713 | M-2c: C-code 误放 Notes | 无 (R1 不收 C-code 列) |

### 未改 / 说明

- M-2a 与 M-2c 重叠: RELREC USUBJID (:37 "Null for dataset-level relationships")、POOLID (:39 "For pooled subject data") 是 PDF 空格而 KB 有自写句, 但所在行是 R1 IE 6 行之一 (p64 a019 / p65 a001), 按 M-2a "维持不改" 优先, 未加 D6 标注 — 如需 D6 请主控指示. RELREC APID (:38, a020 截断) 同属 M-2a, 未改.
- SUPP-- POOLID (:77) Notes 空: notescheck 报 DIFF 系原子解析错位 (p66 a001 把 Definition 文本放进 Notes 字段); 渲染 p66 确认该文本在 Definition 列, PDF Notes 为空 → KB 空正确, 未改.
- 触碰的 unparseable 表 (reviewer 须对渲染图人工逐格): RELREC 表 (:33, 改 :36/:41-44)、SUPP-- 表 (:71, 改 :74/:76/:79-85)、RELSPEC 表 (:173, 改 :177-180).

### 验证 (S = scratchpad/t2_B-model06_writer)

- `python3 -I $S/edit2.py` 每格断言变量名与原子一致后替换; `python3 -I $S/notescheck.py` → 29 行中 25 EQ, 4 DIFF = :37/:38/:39 (M-2a 保留) + :77 (原子错位, 见上).
- `python3 -I $S/scan.py` → `HIT 36 MISS 8` (同 attempt 1, 8 个均为节标题 M-1)
- `python3 -I $S/tblcheck.py` → `diffs 2` (RELSPEC Role 括号约定 M-4, 不改)
- `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_a2.json` → `KB tables: 9; status: {'UNPARSEABLE': 9}; diffs: 0` GREEN
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_a2.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_reg_a2.jsonl` → RED, 51 回退全 ig34 (并行批); `grep -c sv20 $S/fp_reg_a2.jsonl` = 0
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`
