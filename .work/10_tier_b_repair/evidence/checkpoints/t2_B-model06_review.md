# T2 B-model06 — reviewer checkpoint

## attempt 1 (审 writer attempt 1+2 终态)

- reviewer: `oh-my-claudecode:code-reviewer` (opus), 与 writer (executor) 不同 agent / invocation。base = `HEAD`, 文件 `knowledge_base/model/06_relationship_datasets.md` (md5 终态见 writer `328c4e55…`)。
- 源: SDTM v2.0 (`source/cdisc/SDTM_v2.0.pdf`) p64-69 (p64 = §6 起, p70 = §7 起; 完整节页范围)。
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-model06_reviewer/`

### verdict: **PASS**

无 HIGH/CRITICAL; 2 条 LOW 观察 (KB 自写 D6 内容, 非本批回归, 不阻塞, 建议并入 T4)。

### 命令与关键输出 (可复跑, S = 上述 scratch)

| 命令 | exit / 关键输出 |
|---|---|
| `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` | exit 0; `KB tables: 9; status: {'UNPARSEABLE': 9}; diffs: 0` GREEN (全 UNPARSEABLE → 下方人工逐格) |
| `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` | RESULT: RED, 51 回归; `grep -c sv20 $S/fp_regress.jsonl` = 0 (全为 ig34 他批, 不计本批) |
| `python3 -I $S/scan.py` (sv20 p64-69 全部非 TABLE_ROW 原子 `norm(verbatim) in norm(KB)`) | SENTENCE 20/20 HIT, LIST_ITEM 9/9 HIT, HEADING 7 HIT / 8 MISS (章节标题 6, 6.1-6.7 = M-1 主控裁定不改), TABLE_HEADER 7 MISS (KB 列集为 R1 子集, 预期) |
| `python3 -I $S/notes.py` (KB 每个非空 Notes 格 ⊂ 对应 TABLE_ROW 原子) | 19 格中 16 IN; 3 NOTIN = :37 USUBJID / :38 APID / :39 POOLID (R1 IE 行, M-2a 主控裁定维持, 不计) |
| `pdftoppm -f N -l N -r 110 -png source/cdisc/SDTM_v2.0.pdf $S/pN` (N=64..69) | 6 页渲染图全部打开目视逐格核 (见下表) |
| `python3 tools/check_links.py 2>&1 \| grep "live docs"` | `broken relative links: 18668 (live docs: 42)` = 基线 42 |

### 问题表

| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| model/06:46-55 RELTYPE Combinations (D6 #16) | D6 不矛盾 (LOW, conf MEDIUM, 非阻塞) | KB 自写表以 "record relates to record" 释义, 并单列 MANY/ONE; PDF 只说 RELTYPE 标识层级、"only necessary when identifying a relationship between datasets"; SDTMIG ch08 列 3 种组合 (ONE/ONE、ONE/MANY、MANY/MANY) 且为 dataset 级。与 SDTM v2.0 不构成直接矛盾, D6 标注已加; 本批未改其内容。建议 T4: 换为指向 `chapters/ch08_relationships.md` 的交叉引用或删 | p65 RELTYPE Notes "values are only necessary when identifying a relationship between datasets" |
| model/06:193 Summary SUPP-- "Subject-level? Yes" (D6 #22) | D6 不矛盾 (LOW, conf LOW, 非阻塞) | SUPP-- 也含 APID / POOLID (AP 与 pool 级), "Yes" 是简化; writer 对 POOLDEF 删 "(nonclinical)" 的同一逻辑下 SUPP-- 也可视为不完整。非本批改动格。建议 T4 一并定 Summary 表是否保留 | p65-66 SUPP-- APID/POOLID 行 |

FAIL / CONDITIONAL 项: 无。

### 人工逐格表 (触碰的 unparseable 表, 对渲染图; KB 列 = #/Variable/Label/Type/Role/Notes)

**RELREC :33 (p64-65)**

| # | Variable | Label | Type | Role | Notes | 判定 |
|---|---|---|---|---|---|---|
| 1 | STUDYID | 一致 | 一致 | 一致 | PDF 空 / KB 空 | 一致 |
| 2 | RDOMAIN | 一致 | 一致 | 一致 | 逐字 (含句号) | 一致 |
| 3 | USUBJID | 一致 | 一致 | 一致 | PDF 空 / KB 自写 "Null for dataset-level relationships" | M-2a 裁定维持, 不计 |
| 4 | APID | 一致 | 一致 | 一致 | KB 截断 ("a group, or a pool…"; 缺 POOLDEF 句) | M-2a 裁定维持, 不计 |
| 5 | POOLID | 一致 | 一致 | 一致 | PDF 空 / KB 自写 "For pooled subject data" | M-2a 裁定维持, 不计 |
| 6 | SPDEVID | 一致 | 一致 | 一致 | 空/空 | 一致 |
| 7 | IDVAR | 一致 | 一致 | 一致 | 逐字 | 一致 (Examples "--SEQ and --GRPID" R1 缺列, M-3) |
| 8 | IDVARVAL | 一致 | 一致 | 一致 | 逐字 (含 "If --SEQ is…" 句) | 一致 |
| 9 | RELTYPE | 一致 | 一致 | Record Qualifier 一致 | 逐字 (含 "However, values are only necessary…") | 一致 |
| 10 | RELID | 一致 | 一致 | Record Qualifier 一致 | 逐字 3 句 | 一致 |

**SUPP-- :71 (p65-66)**

| # | Variable | Label | Type | Role | Notes | 判定 |
|---|---|---|---|---|---|---|
| 1 | STUDYID | 一致 | 一致 | 一致 | 空/空 | 一致 |
| 2 | RDOMAIN | 一致 | 一致 | 一致 | 逐字 | 一致 |
| 3 | USUBJID | 一致 | 一致 | 一致 | 空/空 | 一致 |
| 4 | APID | 一致 | 一致 | 一致 | 逐字 (跨 p65/p66 拼合, 含 "see Section 6.3, Pool Definition Dataset, and Section 4, Associated Persons Data") | 一致 |
| 5 | POOLID | 一致 | 一致 | 一致 | PDF 文本在 Definition 列 (渲染确认), Notes 空 / KB 空 | 一致 |
| 6 | SPDEVID | 一致 | 一致 | 一致 | 空/空 | 一致 |
| 7 | IDVAR | 一致 | 一致 | 一致 | 逐字 | 一致 |
| 8 | IDVARVAL | 一致 | 一致 | 一致 | 逐字 | 一致 |
| 9 | QNAM | 一致 | 一致 | Topic 一致 | 逐字 5 句 (直引号 "1TEST", pdftotext 亦为 ASCII 0x22) | 一致 |
| 10 | QLABEL | 一致 | 一致 | Synonym Qualifier (PDF Qualified=QNAM 未写括号) | 逐字 3 句 | 一致 (括号约定 M-4, 主控裁定不计) |
| 11 | QVAL | 一致 | 一致 | Result Qualifier 一致 | 逐字 | 一致 |
| 12 | QORIG | 一致 | 一致 | Record Qualifier 一致 | 逐字 | 一致 |
| 13 | QEVAL | 一致 | 一致 | Record Qualifier 一致 | 逐字 2 句 | 一致 (Examples R1 缺列, M-3) |

**POOLDEF :101 (p67; 仅加表题)** 4 行 Variable/Label/Type/Role 全一致 (无 Notes 列, R1)。

**RELSUB :118 (p67)**: 1-4 行一致; 5 SREL Label "Subject Relationship" = 渲染 p67 (改前 "Subject, Device, or Study Relationship" 错) → 一致; Role Record Qualifier 一致。

**DR :136 (p68; 仅加表题)** 4 行全一致。

**APRELSUB :155 (p68-69)**: 1 STUDYID 一致; 2 APID Label "Associated Persons Identifier" = 渲染 p69 → 一致; 3 RSUBJID / 4 RDEVID / 5 SREL ("Subject, Device, or Study Relationship", Record Qualifier) 一致。

**RELSPEC :173 (p69)**

| # | Variable | Label | Type | Role | Notes | 判定 |
|---|---|---|---|---|---|---|
| 1 | STUDYID | 一致 | Char | Identifier | 空/空 | 一致 |
| 2 | USUBJID | 一致 | Char | Identifier | 空/空 | 一致 |
| 3 | REFID | Reference ID 一致 | Char | Identifier | PDF Notes 空 (C82531 在 C-code 列) / KB 空 | 一致 |
| 4 | SPEC | Specimen Type 一致 | Char | Variable Qualifier (REFID) | PDF Notes 空 (C70713 在 C-code 列) / KB 空 | 一致 (括号 M-4 不计) |
| 5 | PARENT | Specimen Parent 一致 | Char | Identifier | 逐字 (含句号) | 一致 |
| 6 | LEVEL | Specimen Level 一致 | Num | Variable Qualifier (REFID) | 逐字 (含句号) | 一致 (括号 M-4 不计) |

**RELTYPE Combinations :50 / Summary :190**: KB 自写表, 无 PDF 对应; 已 D6 标注 (见问题表 LOW 2 条); Summary POOLDEF 格 "Yes (nonclinical)" → "Yes" 删扩写成立 (PDF p67 RELSUB POOLID 注 "POOLDEF records must exist for each subject in the pool", p64 APID 注 pool → POOLDEF, 均非仅 nonclinical)。

### G-TB6 反向溯源 (diff 每条新增/改动行)

| KB 行 | 内容 | 出处 |
|---|---|---|
| :9-17 | Overview 列表 9 项 (含 2 子项) | p64 逐字 (scan LIST_ITEM 9/9 HIT; "in a pool." 句号保留) |
| :25-27 | §6.1 Structure + 描述 | D6 标注 (KB 自写, 不与 PDF 矛盾: 与 p64 列表 2 类关系相容) |
| :31 / :69 / :99 / :116 / :134 / :153 / :171 | 7 个表题 | p64/p65/p67/p67/p68/p68/p69 粗体表题逐字 |
| :36 / :41-44 | RELREC Notes | p64-65 逐字 (见上表) |
| :48 | RELTYPE 表 D6 行 | 结构/标注行, 签字 |
| :61 | §6.2 句 | p65 逐字 (PDF 为框注) |
| :63-65 | §6.2 Structure + 描述 | D6, 不矛盾 |
| :74 / :76 / :79-85 | SUPP-- Notes | p65-66 逐字 |
| :89 | Naming Convention | D6; PDF p65 把命名交给 SDTMIG/SENDIG/SDTMIG-AP, 不矛盾 |
| :95 | §6.3 句 | p67 逐字 |
| :97 / :114 / :132 / :151 / :167-169 | Structure 行 / §6.7 描述 | D6, 不矛盾 (§6.7 "specimen lineage" 与 PARENT/LEVEL 注相容) |
| :112 | §6.4 3 句 | p67 逐字 |
| :124 | RELSUB SREL Label | p67 渲染 |
| :130 | §6.5 3 句 | p68 逐字 |
| :147 / :149 | §6.6 两段 9 句 | p68 逐字; 渲染确认 PDF 在 "supplemental qualifiers." 后分段 |
| :158 | APRELSUB APID Label | p69 渲染 |
| :177-180 | RELSPEC Notes | p69 (REFID/SPEC 空, PARENT/LEVEL 逐字) |
| :182 | 交叉引用 | 纯导航; 目标 `model/01_concepts_and_terms.md:90` (节 `### Changes to Datasets and Variables`, :86, 文件内唯一) 有原文, 与 PDF p6 §1.4 逐字一致 (sv20_p0006.txt:30-32) |
| :188 | Summary D6 行 | 结构/标注行, 签字 |
| :194 | POOLDEF "Yes" | 删扩写 (D-7) |

结构行签字: 7 个表题 (PDF 原有)、:48/:188 D6 单行标注、:182 交叉引用。无新增标题 / 锚点; 原有标题 (`## 6.x …`、`### Variables (N variables)`、`### RELTYPE Combinations`、`### Naming Convention`) 未变。无出处的新增词句: 0。

### 删除清单逐条确认

| # | 确认 |
|---|---|
| D-1 | 旧 Overview 7 项改写列表 → 已由 p64 原列表取代; 无原子丢失 (scan LIST_ITEM 全 HIT) ✔ |
| D-2 | POOLDEF 旧描述 (含 "nonclinical" 限定, 与 p67 不符) ✔ |
| D-3 | RELSUB 旧描述 → p67 3 句取代 ✔ |
| D-4 | DR 旧描述 → p68 3 句取代 ✔ |
| D-5 | APRELSUB 旧描述 → p68 9 句取代 ✔ |
| D-6 | RELSPEC **Note:** → model/01:90 原文存在, 一行交叉引用 ✔ |
| D-7 | Summary " (nonclinical)" 与 PDF 矛盾 ✔ |
| D-8 | SUPP-- QNAM/QLABEL/QVAL/QORIG/QEVAL 改写短句 (含 KB 自写 QORIG 值列举) → PDF 原文取代 ✔ |
| D-9 | RELSPEC REFID/SPEC Notes 里的 C-code → PDF 渲染确认属 C-code 列, Notes 空 ✔ |
diff 中除上述 9 项外无其他删除行 (`git diff HEAD -- knowledge_base/model/06_relationship_datasets.md` 全量阅读)。

### D6 逐条确认 (10 处)

| # | KB 行 | 结论 |
|---|---|---|
| 1 | :25-27 §6.1 | 不矛盾 ✔ |
| 2 | :48 RELTYPE 表 | 不与 SDTM v2.0 直接矛盾 ✔ (LOW 观察见问题表) |
| 3 | :63-65 §6.2 | 不矛盾 ✔ |
| 4 | :89 Naming Convention | 不矛盾 ✔ |
| 5-9 | :97/:114/:132/:151/:167 Structure | 不矛盾 ✔ |
| 10 | :167-169 §6.7 描述 (与 Structure 同块) | 不矛盾 ✔ |
| (+) | :188 Summary | 删 "(nonclinical)" 后不矛盾 ✔ (LOW 观察 SUPP-- "Yes") |
措辞均为 `> KB note (not in SDTM v2.0):` (model/ 口径) ✔。

### 双向全扫 p64-69

- PDF→KB: 叙述/列表原子 29/29 HIT; 标题 8 MISS 均 M-1 (裁定不改); 表格原子逐格见上 (Label/Type/Role/Notes), 缺列 (Format/Qualified/C-code/Definition/Examples) 属 R1 不收; POOLDEF/RELSUB/DR/APRELSUB 无 Notes 列按 R1 不补。
- KB→PDF: 全文件 198 行逐行读; 非 PDF 内容 = D6 标注块、导航 (H1、Source 行、`## Overview`、`### Variables (N)`、`---`、:182 交叉引用)、M-2a 三格 (裁定不计)。无未标注的自写解释。

### 白名单 / 副作用

- 本批只改 `knowledge_base/model/06_relationship_datasets.md`; 工作树其他 KB 改动 (CE/DA/DD/DM/FT/TS、model/05) 属并行批, 不计。model/01 无改动 (交叉引用目标未被动)。
- R2 recheck: `t2_recheck[]` 为空, 无。
