# T2 B-model05 — writer checkpoint

## attempt 1

- base HEAD `b0932182fdeb0139a0d6b1dae9c3f77321901294`; kb_file `knowledge_base/model/05_study_level_data.md` md5 `0951e8582518f69e54f7b92c59ab2830` → `ca13d82f43a3665d1a362cd61d2412aa`
- 页范围核 (O20): §5 起于 p51 (`sv20_p0051.txt` "5 Study-level Data"; p50 为 §4 AP), p64 起 §6 "Datasets for Representing Relationships" → **完整节 = p51-p63**, 与 batch pdf_ranges 51-63 一致 (pdf_pages 51/56 仅原子页).
- 真值: `work/pdf_pages/sv20_p0051-0063.txt` (layout, 表格 5 列逐格用列位置核) + pdftoppm 80dpi 渲染 p51/p61/p62/p63 (scratch).
- 口径 (仿 B-model01 attempt 2 先例): 5 atoms 之外, 对 p51-63 全部叙述原子做双向扫描, R2 改写/缺失一律按 PDF 逐字恢复 (R3); 旧改写句在不承载其他原子时 D2 删 (删除清单). 未改任何既有标题文字/层级; 新增 3 个组标题用 PDF 原标题 (`### 5.1.1` / `### 5.1.3` / `### 5.1.4`, 与同文件域节同级 `###`). PDF 表题 (如 "Trial Elements—One Record per Trial Element") 以粗体行补在各表前, 取代 KB 自写 `**Structure:**` 行.
- 格式化: 仅合并换行、项目符号→`- `、粗体、`*taxa*` 斜体照 PDF; 直引号照文本层.

### 变更清单

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | model/05:154 | sv20_p0056_a019 | INSERTED | R1-TD: oncology 依从性句, 接 TD 首句后 | 56 |
| 2 | model/05:154 | sv20_p0056_a020 | INSERTED | R1-TD: TD 评估 assessment time bias 句 | 56 |
| 3 | model/05:154 | sv20_p0056_a022 | INSERTED | R1-TD: RECIST / PFS 句 | 56 |
| 4 | model/05:17 | sv20_p0051_a008 | REPLACED | 补 "(animal developmental and reproductive toxicology studies; …)"; 该行仅承载 a008, 旧改写行被取代 (D-1) | 51 |
| 5 | model/05:23 | sv20_p0051_a013 | REPLACED | 补 "(e.g., for study arms, visits, and eligibility criteria)"; 该行仅承载 a013 (D-2) | 51 |
| 6 | model/05:154 | sv20_p0056_a021 | INSERTED | **旧 IE (P6 VERSION_MISMATCH) → R1-TD 推出**: 位于 a020 与 a022 之间, 不补则段落断裂; 主控可否决 | 56 |
| 7 | model/05:13 | sv20_p0051_a004 | REPLACED | R2: 去 KB 自加 "(TDM)" (D-3); 同行 a005 逐字保留 | 51 |
| 8 | model/05:20 | sv20_p0051_a011 | REPLACED | R2: "expressed as parameters" → "expressed as a series of parameters" | 51 |
| 9 | model/05:25-27 | sv20_p0051_a014, a015 | INSERTED | R3: 新增 `### 5.1.1 Trial Arms and Trial Elements` + 引言句 | 51 |
| 10 | model/05:31 | sv20_p0051_a017 | REPLACED | R2: "Describes the basic building blocks…" → PDF "Trial Elements describes the periods of times…" (D-4); a018 逐字保留 | 51 |
| 11 | model/05:33 | sv20_p0051_a019 | INSERTED | PDF 表题; 取代 `**Structure:** One record per planned Element` (D-5) | 51 |
| 12 | model/05:47 | sv20_p0052_a006 | REPLACED | R2: 句首 "Describes" → "Trial Arms describes" | 52 |
| 13 | model/05:47 | sv20_p0052_a009 | INSERTED | **旧 IE → R3 补**: "Note that although the same element … TABRANCH and TATRANS." | 52 |
| 14 | model/05:49 | sv20_p0052_a010 | INSERTED | PDF 表题; 取代 Structure 行 (D-6) | 52 |
| 15 | model/05:66 | sv20_p0053_a006, a007, a008 | REPLACED | **旧 IE → R3 补** 3 句; KB 自写 "Describes sets of subjects … pooled analysis groups" 删 (D-7) | 53 |
| 16 | model/05:68 | sv20_p0053_a009 | INSERTED | **旧 IE → R3 补** PDF 表题; 取代 Structure 行 "per Trial Set parameter per Trial Set" (D-8) | 53 |
| 17 | model/05:78 | sv20_p0053_a017 | REPLACED | 表格: TXPARM Label "Trial Set Parameter Name" → "Trial Set Parameter" | 53 |
| 18 | model/05:79 | sv20_p0053_a018 | REPLACED | 表格: TXVAL Label "Parameter Value" → "Trial Set Parameter Value" | 53 |
| 19 | model/05:81-85 | sv20_p0054_a001, a002, a003 | INSERTED | R3: 新增 `### 5.1.3 Trial Repro Stages and Trial Repro Paths` + Note + a003 | 54 |
| 20 | model/05:85 | sv20_p0054_a004, a005 | INSERTED | **旧 IE → R3 补** 2 句 | 54 |
| 21 | model/05:91 | sv20_p0054_a008 | REPLACED | R2: 句首 "Describes" → "Trial Repro Stages describes" | 54 |
| 22 | model/05:93 | sv20_p0054_a009 | INSERTED | PDF 表题; 取代 Structure 行 (D-9) | 54 |
| 23 | model/05:109 | sv20_p0054_a020 | REPLACED | R2: 句首 "Describes" → "Trial Repro Paths describes" | 54 |
| 24 | model/05:111 | sv20_p0055_a001 | INSERTED | PDF 表题; 取代 Structure 行 (D-10) | 55 |
| 25 | model/05:126-132 | sv20_p0055_a013, a014, a015, a016, a017 | INSERTED | R3: 新增 `### 5.1.4 Trial Planned Data Collection` + 引言 + 3 项列表 (a013/a015 为旧 IE → R3 补) | 55 |
| 26 | model/05:136 | sv20_p0056_a002 | REPLACED | R2: "Describes the visits planned in the protocol, including…" → PDF 原句 (D-11) | 56 |
| 27 | model/05:136 | sv20_p0056_a003, a004, a005 | INSERTED | **旧 IE → R3 补** 3 句 | 56 |
| 28 | model/05:138 | sv20_p0056_a006 | INSERTED | PDF 表题; 取代 Structure 行 "per planned Visit per Arm" (D-12) | 56 |
| 29 | model/05:154 | sv20_p0056_a018 | REPLACED | R2: 句首 "Provides" → "Trial Disease Assessments provides" | 56 |
| 30 | model/05:156 | sv20_p0057_a001 | INSERTED | PDF 表题; 取代 Structure 行 (D-13) | 57 |
| 31 | model/05:172 | sv20_p0057_a013 | REPLACED | R2: "Describes the types of disease milestones…" → PDF 原句 (D-14) | 57 |
| 32 | model/05:174 | sv20_p0058_a001 | INSERTED | PDF 表题; 取代 Structure 行 (D-15) | 58 |
| 33 | model/05:186 | sv20_p0058_a009 | REPLACED | R2: "Describes the inclusion and exclusion criteria…" → PDF 原句 (D-16) | 58 |
| 34 | model/05:186 | sv20_p0058_a010 | INSERTED | **旧 IE → R3 补** | 58 |
| 35 | model/05:188 | sv20_p0058_a011 | INSERTED | PDF 表题; 取代 Structure 行 "per I/E criterion" (D-17) | 58 |
| 36 | model/05:194-198 | sv20_p0058_a015-a018, sv20_p0059_a001 | REPLACED | 表格: IETESTCD/IETEST/IECAT/IESCAT Label "Incl/Excl …" → "Inclusion/Exclusion …"; TIRL "Criterion Evaluation Rule" → "Inclusion/Exclusion Criterion Rule" | 58-59 |
| 37 | model/05:203 | sv20_p0059_a004, a005 | REPLACED | R2: "Contains summary information … (e.g., trial phase, objectives, design)" → PDF 2 句 (D-18) | 59 |
| 38 | model/05:205 | sv20_p0059_a006 | INSERTED | PDF 表题; 取代 Structure 行 "per trial summary parameter value" (D-19) | 59 |
| 39 | model/05:214,218,219 | sv20_p0059_a013, a017, sv20_p0060_a001 | REPLACED | 表格: TSPARM "…Parameter Name" → "Trial Summary Parameter"; TSVCDREF/TSVCDVER 补 "the" | 59-60 |
| 40 | model/05:223 | sv20_p0060_a004 | REPLACED | R2: "Each record contains" → "Each record in the Challenge Agent Characterization dataset contains"; a003 逐字保留 | 60 |
| 41 | model/05:225 | sv20_p0060_a005 | INSERTED | PDF 表题; 取代 Structure 行 (D-20) | 60 |
| 42 | model/05:246-249 | sv20_p0061_a002, a003, a004, a005 | REPLACED | R2: KB 改写句 "Study Reference datasets provide structures…" + 行内列举 → PDF 2 句 + 2 项列表 (D-21) | 61 |
| 43 | model/05:253 | KB_AUTHORED | REPLACED | D6: `**Structure:** One record per device attribute per device` (PDF 无 one-record-per) → `> KB note (not in SDTM v2.0):` 前缀 | - |
| 44 | model/05:255 | sv20_p0061_a007 | REPLACED | R2: "Used to identify the devices used in a study." → PDF a007 (D-22); a008 逐字保留 | 61 |
| 45 | model/05:257 | sv20_p0061_a009 | INSERTED | PDF 表题 "Device Identifiers Dataset" | 61 |
| 46 | model/05:269-285 | sv20_p0062_a001 | MOVED | Concept Map (DI) 移到 DI 表后 (PDF p62 顺序); 题注 ":"→"." 按 PDF; Mermaid 标签补丢失空格 ("has one or more" / "is represented using" / "Identifying Characteristic" / "identifier (SPDEVID)" 等); 加 D6 rendering 注 | 62 |
| 47 | model/05:291 | KB_AUTHORED | REPLACED | D6: OI `**Structure:**` 行加 KB note 前缀 | - |
| 48 | model/05:293 | sv20_p0062_a003 | REPLACED | R2: "Used to represent taxonomic information…" → PDF a003 (*taxa* 斜体照 PDF) (D-23); a004 由 KB 改写 "The taxa used depend…" 改为 PDF 原句 | 62 |
| 49 | model/05:295 | sv20_p0062_a005 | INSERTED | PDF 表题 "Non-host Organism Identifiers Dataset" | 62 |
| 50 | model/05:301 | sv20_p0062_a009 | REPLACED | 表格: NHOID Label "Non-host" → "Non-Host" (PDF 大写 H) | 62 |
| 51 | model/05:307-323 | sv20_p0063_a001 | MOVED | Concept Map (OI) 移到 OI 表后 (PDF p63); 题注 "."; Mermaid 标签补空格 ("Non-Host Organism" 等); D6 rendering 注 | 63 |

覆盖率: atoms[] 5 条 = #1-5; 其余 46 行为 R3 新增 / 表格格 / D6.

### 新增 atom 清单 (R3, 非 atoms[])
- 旧 ledger `INTENTIONAL_EXCLUDE / VERSION_MISMATCH` (P6 ack, 理由 "superseded by SDTMIG v3.4") 但实为 v2.0 叙述、本批补入: p52 a009; p53 a006/a007/a008/a009; p54 a004/a005; p55 a013/a015; p56 a003/a004/a005/a021; p58 a010. **共 14 条, 列给主控可否决** (R1 先例: §1 引言与 TD 句均由 IE 改 REAL_GAP).
- ledger EQUIVALENT/PARTIAL 但非逐字 (R2): p51 a004/a011/a014/a015/a017/a019; p52 a006/a010; p54 a001/a003/a008/a009/a020; p55 a001/a014/a016/a017; p56 a002/a006/a018; p57 a001/a013; p58 a001/a009/a011; p59 a004/a005/a006; p60 a004/a005; p61 a002-a005/a007/a009; p62 a003/a004/a005.

### 删除清单 (D2, reviewer 逐条确认)

| # | 位置 (base 行) | 删除内容 (摘要) | 原因 | 保留 |
|---|---|---|---|---|
| D-1 | :17 | 旧列表项 (缺 "animal developmental…" 括注) | R2 残留, 行仅承载 a008 | :17 PDF 原文 |
| D-2 | :23 | 旧句 (缺 e.g. 括注) | R2 残留, 行仅承载 a013 | :23 |
| D-3 | :13 | "(TDM)" | KB 自加缩写, PDF 无; 同行 a005 不受影响 | :13 |
| D-4 | :29 | "Describes the basic building blocks of a trial design — discrete periods…planned." | a017 的改写, 已由原句取代 | :31 |
| D-5..D-6, D-8..D-10, D-12, D-13, D-15, D-17, D-19, D-20 | :27, :43, :62, :79, :97, :118, :136, :154, :168, :185, :205 | `**Structure:** One record per …` 共 11 行 | PDF 表题 (HEADING 原子) 的改写/IG 化措辞, 已由 PDF 表题逐字取代 (TX "per Trial Set"、TV "per Arm"、TS "value"、TI "I/E" 与 PDF 不同) | 各表前 PDF 表题 |
| D-7 | :64 | "Describes sets of subjects that share common characteristics (e.g., treatment groups, pooled analysis groups)." | a006 的 KB 改写 ("pooled analysis groups" PDF 无, 与 "planned groups of subjects" 不一致) | :66 |
| D-11 | :120 | "Describes the visits planned in the protocol, including the planned order…" | a002 改写 | :136 |
| D-14 | :156 | "Describes the types of disease milestones that may occur in a study." | a013 改写 | :172 |
| D-16 | :170 | "Describes the inclusion and exclusion criteria for the trial." | a009 改写 | :186 |
| D-18 | :187 | "Contains summary information about the trial (e.g., trial phase, objectives, design)." | a004/a005 改写 | :203 |
| D-21 | :228 | "Study Reference datasets provide structures for representing…" + 行内 "identifiers for devices, and identifiers for non-host organisms." | a002-a005 改写 | :246-249 |
| D-22 | :234 | "Used to identify the devices used in a study." | a007 改写 | :255 |
| D-23 | :268 | "Used to represent taxonomic information for non-host organisms such as bacteria and viruses." + "The taxa used for identification depend on…" | a003/a004 改写 ("bacteria and viruses" PDF 无) | :293 |

### PDF_TYPO
- 无.

### 触碰过的 unparseable 表 (reviewer 须对渲染逐格人工核)
- TX 表 (base :66, 改后 :70) — TXPARM / TXVAL Label 格.
- TI 表 (base :172, 改后 :190) — IETESTCD / IETEST / IECAT / IESCAT / TIRL Label 格.
- TS 表 (base :189, 改后 :207) — TSPARM / TSVCDREF / TSVCDVER Label 格.
- OI 表 (base :288, 改后 :297) — NHOID Label 格.
- DI 表 (base :254, 改后 :259) 与 OI 表整体随 Concept Map 换位, 表内容除 NHOID 外未改.
- 其余 8 张 (TE/TA/TT/TP/TV/TD/TM/AC) 5 列 (#/Variable/Label/Type/Role) 已逐格对 PDF (atoms + layout 列位置), 无差异, 未改.

### 需主控定 (未改)
1. 既有标题与 PDF 不同 (规则 6 未改): `## Overview` (KB 自写, PDF 为 "5 Study-level Data" 正文); `## 5.1 Trial Design Model` vs PDF "5.1 The Trial Design Model"; 域节 `### Trial Elements (TE)` 等缺 PDF 节号/原名 (5.1.1.1 Trial Elements … 5.2.2 Non-host Organism Identifiers Dataset, 共 13 个); 层级扁平 (5.1.1.x 与 5.1.1 同为 `###`). 全仓 (除 releases/archive) grep `05_study_level_data(.md)?#` = 0 处锚点引用, 改标题不断链.
2. TT/TP 表 "Notes" 列实承载 PDF "Usage Restrictions" 值 ("Not in human clinical trials"), DOMAIN 行 `"TT"`/`"TP"` 才是 PDF Notes 的摘要 → 列名与内容混装. 未改列结构.
3. TS 表缺 PDF Usage Restrictions "Not in nonclinical trials" (TSVALCD/TSVCDREF/TSVCDVER); TT/TP 有而 TS 无, 不一致. R1 "缺列不补" 下未补.
4. Role 列 "Synonym Qualifier (SETCD)" 式括注 (取自 PDF Variable(s) Qualified) 只在部分表出现 (TE ELEMENT / TA ARM / TV VISIT,ARM / TI IETEST / TS TSPARM / AC ACPARM / TX TXPARM 无括注). 未统一.
5. 14 条旧 IE → R3 补 (见新增 atom 清单) 是否保留; 尤其 TD a021 (R1-TD 是否涵盖).
6. 2 个 `**Structure:**` D6 行 (DI/OI) 为 IG 化措辞, PDF 无 one-record-per 表题: 保留 (D6) 或删.

### 范围外发现
- 无 (其他 KB 文件未查).

### git diff --stat
```
 knowledge_base/model/05_study_level_data.md | 177 ++++++++++++++++------------
 1 file changed, 103 insertions(+), 74 deletions(-)
```

### 验证 (S = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-model05_writer`)
- 双向扫描 `python3 -I $S/scan.py` (repo 根执行; 归一化空白/粗体/斜体): p51-63 全部 SENTENCE/LIST_ITEM/NOTE/HEADING 原子为 KB 子串, MISS 15 条全部为 HEADING 节号标题 (需主控定 #1, 既有标题未改); KB→PDF NOSRC 仅 :3 Source 行 (导航)、2 条 D6 Structure、2 条 D6 Mermaid 注与 mermaid 代码.
- `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` → `KB tables: 13; status: {'UNPARSEABLE': 13}; diffs: 0` GREEN (全 unparseable, 人工核见上).
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → RED, 51 条回退全为 ig34 (并行批); `grep -c sv20 $S/fp_regress.jsonl` = 0.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`.

### 更正 (attempt 1 内, 交 reviewer 前)

- **段落切分**: 按 layout 行宽核段落边界 (`sed -n 21,25p sv20_p0052.txt`、`sed -n 41,47p sv20_p0056.txt` 加 `awk '{print length}'`; 前行短行收尾 = 段落断开): TA "Note that although…" 与 TD "In oncology studies…" 在 PDF 是独立段落 → KB 各拆为新段. 其余插入段 (TX / 5.1.3 引言 / TV / TI / TS / AC / 5.2 / DI / OI) 在 PDF 为单段, 未拆. md5 → `ed15da82ac9307772cf2f4b1003bb692`; diff --stat `181 ++++++++++++++++------------`, `107 insertions(+), 74 deletions(-)`.
- **行号**: 上方变更清单的 "改后" 行号是切段前的; 切段后 base→now 偏移 = 原 ≥48 行 +2, 原 ≥155 行 +4. **以 `work/t2_batches/B-model05.writer.jsonl` 的 kb_line_after 为准** (已重算, 并逐条打印目标行首核对). 例: TA 表题 :51, TD 表题 :160, TS 表格 :218/:222/:223, OI Concept Map :311.
- **计数统一**: 变更清单 51 行 (多原子合并成行); jsonl 78 行 = 72 条 sv20 原子 ref (5 atoms[] + 67 R3/表格格) + 2 KB_AUTHORED (D6) + 4 unparseable 表. trace 行的 "5 + 61" 记数有误, 以本处为准 (trace append-only 不改).
- **fp 回退核 (删除行是否承载 ig34 原子)**:
  - `cd .work/10_tier_b_repair/work && python3 -I $S/fp_check.py $S` → baseline 中 hit_target/hit_any 为 model/05 的原子 15 个; 非 sv20 的只有 ig34_p0441_a004/a005, 两者 EQUIVALENT → EQUIVALENT (未退化); sv20 13 个 verdict 均未变 (脚本只打印变化或非 sv20 项, 无 sv20 输出).
  - `cd .work/10_tier_b_repair/work && python3 -I $S/ledger_check.py` → ledger 中挂 md_model05_ 的非 sv20 行: ig34_p0193_a001 (base :166 TI 标题, 未删)、ig34_p0382_a001 / p0383_a006 (:11 `## 5.1` 标题, 未删)、ig34_p0441_a001/a004/a005/a006/p0442_a001 (:226/:230/:264 标题, 未删)、**ig34_p0441_a003 (:228, 已删改写句)**、**ig34_p0441_a007 (:234, 已删改写句)**. 后两者 fp: a003 baseline/after 均 PARTIAL 且命中 `chapters/ch10_appendices.md` (不依赖 model/05); a007 baseline/after 均 PARTIAL、hit_any=None (从未被 model/05 命中). → 删除清单无需回退.
  - fp_match 全量 51 条 ig34 回退: 前缀 p011/p017/p021/p025/p026/p028/p031/p036/p037/p039, 均不在 model/05 的 15 个 baseline 命中原子内 (见上) → 与本批无关 (来自并行批改动, 本 writer 未核其具体来源).
- **表格核对 (更正措辞)**: 13 张表 (未触碰的为 9 张: TE/TA/TT/TP/TV/TD/TM/AC/DI, 前文 "8 张" 误记) 由 `python3 -I $S/table_check.py` (repo 根) 核: KB 每行 #/Variable/Label/Type/Role 对 PDF 原子逐字, Role 括注对 Variable(s) Qualified 列, 行数对 PDF (查 PDF 有而 KB 缺的行), 并以 layout 文本校验行首 (# + 变量名 + Label 首词) 与 Type / Role 首词 → `tables kb 13 pdf 13` / `bad 0`. Label 多行折行全文只由原子核; 11 个改动格另用 layout 多行折行目视核 (见变更清单 #17/#18/#36/#39/#50).
- **需主控定 追加**:
  7. 11 条 `**Structure:**` 行 (TE/TA/TX/TT/TP/TV/TD/TM/TI/TS/AC) 已删并由 PDF 表题取代 (D-5…D-20); 备选 = 保留为 D6 KB note. 其中 TX/TV/TI/TS 措辞与 PDF 表题实质不同 (IG 化).

## attempt 2 (主控裁定 #7: TX/TV/TI/TS 四条 Structure 行逐条判)

- md5 ed15da82… → `b01d929e0c3718c8d176d90f7c4c598d`; diff --stat 累计 `185 +++…`, `111 insertions(+), 74 deletions(-)`. 只动这 4 条; 其余裁定 (1-6, 7 中等价的 7 条) 按主控执行, KB 未再改.

| 行 | base 原文 (摘要) | PDF 表题 | 判据 | 处理 |
|---|---|---|---|---|
| TX (base :62) | One record per Trial Set parameter per Trial Set | Trial Sets—One Record per Trial Set Parameter | 多出 "per Trial Set": 表题未写, 但同表 SETCD (Identifier) + TXPARMCD (Topic) 本来就是一个 set 一个参数; PDF a007 也说一个 trial 可有多个 set → **不矛盾、有附加信息** | 恢复为 `> KB note (not in SDTM v2.0):`, 放在 :70 表题后 → **:72**; 撤回 D-8 |
| TV (base :118) | One record per planned Visit per Arm | Trial Visits—One Record per Planned Trial Visit | PDF a004/a005: 多数盲法试验所有 arm 访视时间相同, **只有访视因 arm 而异时**才 "a separate record per visit per arm". KB 把这个条件情形写成了无条件结构 → **与 PDF 矛盾** | 维持删除 (D-12) |
| TI (base :168) | One record per I/E criterion | Trial Inclusion/Exclusion—One Record per Trial Inclusion or Exclusion Criterion | 只是缩写, 与表题信息等价, 没有附加信息 → 属 "KB 摘要与 PDF 重复" | 维持删除 (D-17) |
| TS (base :185) | One record per trial summary parameter value | Trial Summary—One Record per Trial Summary Parameter | 多出 "value": 同表有 TSSEQ (Identifier) + TSGRPID, 一个参数可有多条值记录; PDF a004 "1 record for each trial summary characteristic" 并不排除这种情况 → **不矛盾、有附加信息** | 恢复为 KB note, 放在 :211 表题后 → **:213**; 撤回 D-19 |

- 删除清单更新: D-5…D-20 那一行里的 Structure 删除从 11 条减为 **9 条** (撤回 D-8 TX、D-19 TS); D-12 TV 维持, 理由改为 "与 PDF a004/a005 矛盾".
- writer.jsonl: kb_line_after 全部重算 (原 ≥71 行 +2, 原 ≥210 行再 +2), 逐条打印目标行首核对过; 追加 `KB_AUTHORED:TX_structure` (:72) 和 `KB_AUTHORED:TS_structure` (:213) 两行. 共 80 行.
- D6 Structure 行现有 4 条: TX :72 / TS :213 / DI :261 / OI :299.

### O35 登记建议文字 (供主控写入 `work/out_of_scope_findings.md`)
> O35 (B-model05, T4 用户裁定): `knowledge_base/model/05_study_level_data.md` 的 3 类遗留, 本批按规则 6 和 R1 "缺列不补" 未改.
> (a) 标题: `## Overview` 是 KB 自写标题; `## 5.1 Trial Design Model` 与 PDF "5.1 The Trial Design Model" 不一致; 13 个域节 `### Trial Elements (TE)` 等没有 PDF 节号/原名 (5.1.1.1 … 5.2.2); 5.1.1.x 与 5.1.1 同为 `###`, 层级是平的. 全仓无锚点引用, 但下游 sdtm-rag 可能按标题切块.
> (b) 表列: TT/TP 表的 "Notes" 列装的是 PDF "Usage Restrictions" 的值 ("Not in human clinical trials"), DOMAIN 行的 "TT"/"TP" 才是 PDF Notes 的摘要; TS 表没有 PDF Usage Restrictions "Not in nonclinical trials" (TSVALCD/TSVCDREF/TSVCDVER).
> (c) Role 列 "Synonym Qualifier (XXX)" 括注 (取自 PDF Variable(s) Qualified) 只有部分表有 (TX/TT/TP/TM/AC ACVALU/DI/OI 有; TE/TA/TV/TI/TS/AC ACPARM 没有), 写法不统一.

### 验证
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`.
- 本轮没有动正文句子和表格格, 双向扫描 / table_check 结论不变 (新增 2 行都是 D6 KB note).
