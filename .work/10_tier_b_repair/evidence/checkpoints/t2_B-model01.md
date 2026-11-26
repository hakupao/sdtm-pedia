# T2 B-model01 — writer checkpoint

## attempt 1

- base HEAD: `ae17f74ac45c244b2e34afa8a15ec6b02acf23b3`; kb_file md5 before `8fe190292925ed917aac571a7f9de826` → after `e31323a17de1f977e4fe5df9090cef2c`
- 输入: batch json (26 atoms + 2 t2_recheck) + D5 (sv20_p0004_a016) + R1 + dispatch notes R3 (批内叙述缺失一并补)
- 真值: `work/pdf_pages/sv20_p0004-0009.txt` + pdftoppm 渲染 p4-p7 (scratch)
- 口径: §1 Introduction p4-p7 **整节**逐字补 (1.1-1.4 + 1.4 下 3 个无编号小标题), 不止 22 句 — 只补 atoms 会留下残缺节; 超出 atoms[] 的 64 条记为 R3 新增. 层级仿 `chapters/ch01_introduction.md` (`## 1.1`, 无编号小标题 `###`), 与同文件 `## 2.1` 同级; `## 1 Introduction` 用 PDF 原标题. 未改 H1 / Source 行 / 已有标题.
- 格式化: 仅合并换行、去折行 (`-\n-BEATNO`→`--BEATNO`, `--\nMETHOD`→`--METHOD`)、项目符号→`- `; 弯/直引号按 PDF 文本层原样.

### 变更清单

| # | kb_file:line (改后) | atom_id | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | model/01:9 | sv20_p0004_a003 | INSERTED | R1 §1 | 4 |
| 2 | model/01:9 | sv20_p0004_a005 | INSERTED | R1 §1 | 4 |
| 3 | model/01:11 | sv20_p0004_a007 | INSERTED | R1 §1 | 4 |
| 4 | model/01:11 | sv20_p0004_a008 | INSERTED | R1 §1 | 4 |
| 5 | model/01:11 | sv20_p0004_a009 | INSERTED | R1 §1 | 4 |
| 6 | model/01:15 | sv20_p0004_a011 | INSERTED | R1 §1 | 4 |
| 7 | model/01:15 | sv20_p0004_a012 | INSERTED | R1 §1 | 4 |
| 8 | model/01:15 | sv20_p0004_a013 | INSERTED | R1 §1 | 4 |
| 9 | model/01:15 | sv20_p0004_a015 | INSERTED | R1 §1 | 4 |
| 10 | model/01:17 | sv20_p0004_a018 | INSERTED | R1 §1 | 4 |
| 11 | model/01:17 | sv20_p0004_a019 | INSERTED | R1 §1 | 4 |
| 12 | model/01:20 | sv20_p0004_a020 | INSERTED | R1 §1 | 4 |
| 13 | model/01:20 | sv20_p0004_a021 | INSERTED | R1 §1 | 4 |
| 14 | model/01:20 | sv20_p0004_a022 | INSERTED | R1 §1 | 4 |
| 15 | model/01:24 | sv20_p0004_a023 | INSERTED | R1 §1 | 4 |
| 16 | model/01:26 | sv20_p0004_a024 | INSERTED | R1 §1 | 4 |
| 17 | model/01:27 | sv20_p0004_a025 | INSERTED | R1 §1 | 4 |
| 18 | model/01:32 | sv20_p0005_a002 | INSERTED | R1 §1 | 5 |
| 19 | model/01:32 | sv20_p0005_a003 | INSERTED | R1 §1 | 5 |
| 20 | model/01:34 | sv20_p0005_a005 | INSERTED | R1 §1 | 5 |
| 21 | model/01:38 | sv20_p0005_a008 | INSERTED | R1 §1 | 5 |
| 22 | model/01:38 | sv20_p0005_a009 | INSERTED | R1 §1 | 5 |
| 23 | model/01:116 | sv20_p0008_a007 | INSERTED | REAL_GAP | 8 |
| 24 | model/01:120 | sv20_p0008_a009 | INSERTED | REAL_GAP | 8 |
| 25 | model/01:178 | sv20_p0009_a018 | REPLACED | R2: Variable Qualifiers 行 Purpose 格改为 PDF 原文 (旧改写格 D2 删, 见删除清单 D-2) | 9 |
| 26 | model/01:112 | sv20_p0008_a004 | INSERTED | R2: 补 "(see Concept Map, below)"; 旧改写句被原句取代 (删除清单 D-1) | 8 |
| 27 | model/01:15 | sv20_p0004_a016 | INSERTED | D5 | 4 |
| 28 | model/01:5 | sv20_p0004_a001 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 4 |
| 29 | model/01:7 | sv20_p0004_a002 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 4 |
| 30 | model/01:9 | sv20_p0004_a004 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 4 |
| 31 | model/01:11 | sv20_p0004_a006 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 4 |
| 32 | model/01:13 | sv20_p0004_a010 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 4 |
| 33 | model/01:15 | sv20_p0004_a014 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 4 |
| 34 | model/01:17 | sv20_p0004_a017 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 4 |
| 35 | model/01:28 | sv20_p0004_a026 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 4 |
| 36 | model/01:30 | sv20_p0005_a001 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 37 | model/01:32 | sv20_p0005_a004 | INSERTED | §1.3 整节逐字一并补 (原判 REWRITE_OK @ :102 Note, 未动 :102) | 5 |
| 38 | model/01:36 | sv20_p0005_a006 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 39 | model/01:38 | sv20_p0005_a007 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 40 | model/01:40 | sv20_p0005_a010 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 41 | model/01:42 | sv20_p0005_a011 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 42 | model/01:44 | sv20_p0005_a012 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 43 | model/01:45 | sv20_p0005_a013 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 44 | model/01:46 | sv20_p0005_a014 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 45 | model/01:47 | sv20_p0005_a015 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 46 | model/01:48 | sv20_p0005_a016 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 47 | model/01:49 | sv20_p0005_a017 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 48 | model/01:51 | sv20_p0005_a018 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 49 | model/01:51 | sv20_p0005_a019 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 50 | model/01:53 | sv20_p0005_a020 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 51 | model/01:55 | sv20_p0005_a021 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 52 | model/01:57 | sv20_p0005_a022 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 53 | model/01:58 | sv20_p0005_a023 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 54 | model/01:59 | sv20_p0005_a024 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 55 | model/01:60 | sv20_p0005_a025 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 56 | model/01:61 | sv20_p0005_a026 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 57 | model/01:62 | sv20_p0005_a027 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 58 | model/01:63 | sv20_p0005_a028 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 59 | model/01:64 | sv20_p0005_a029 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 60 | model/01:65 | sv20_p0005_a030 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 61 | model/01:66 | sv20_p0005_a031 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 62 | model/01:67 | sv20_p0005_a032 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 5 |
| 63 | model/01:69 | sv20_p0006_a001 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 64 | model/01:71 | sv20_p0006_a002 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 65 | model/01:72 | sv20_p0006_a003 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 66 | model/01:73 | sv20_p0006_a004 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 67 | model/01:74 | sv20_p0006_a005 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 68 | model/01:75 | sv20_p0006_a006 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 69 | model/01:77 | sv20_p0006_a007 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 70 | model/01:77 | sv20_p0006_a008 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 71 | model/01:79 | sv20_p0006_a009 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 72 | model/01:81 | sv20_p0006_a010 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 73 | model/01:82 | sv20_p0006_a011 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 74 | model/01:84 | sv20_p0006_a012 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 75 | model/01:86 | sv20_p0006_a013 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 76 | model/01:88 | sv20_p0006_a014 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 77 | model/01:88 | sv20_p0006_a015 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 78 | model/01:90 | sv20_p0006_a016 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 79 | model/01:90 | sv20_p0006_a017 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 80 | model/01:92 | sv20_p0006_a018 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 81 | model/01:94 | sv20_p0006_a019 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 82 | model/01:94 | sv20_p0006_a020 | INSERTED | PDF_TYPO T-1: PDF "Section 3, Associated Persons Data" → KB 写 Section 4 | 6 |
| 83 | model/01:96 | sv20_p0006_a021 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 84 | model/01:47 | sv20_p0006_a022 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 85 | model/01:47 | sv20_p0006_a023 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 86 | model/01:47 | sv20_p0006_a024 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 87 | model/01:101 | sv20_p0006_a025 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 88 | model/01:102 | sv20_p0006_a026 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 89 | model/01:104 | sv20_p0006_a027 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 90 | model/01:106 | sv20_p0006_a028 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 6 |
| 91 | model/01:108 | sv20_p0007_a001 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 7 |
| 92 | model/01:114 | sv20_p0008_a006 | INSERTED | R3 新增: 原子后两句 (3 general observation classes…Section 3.2) KB 缺, 接在 :114 段尾 | 8 |
| 93 | model/01:118 | sv20_p0008_a008 | INSERTED | R3 新增 (§1 整节逐字补, 非 atoms[] 原子) | 8 |
| 94 | model/01:- | sv20_p0009_a016 | NOT_TOUCHED_T2_RECHECK | t2_recheck: writer 不改, reviewer 定 | 9 |
| 95 | model/01:- | sv20_p0009_a019 | NOT_TOUCHED_T2_RECHECK | t2_recheck: writer 不改, reviewer 定 | 9 |

覆盖率: atoms[] 26 + D5 1 = 27 行全在表内 (#1-27); R3 新增 66 行 (#28-93, 含 §1 标题 7 个、p8 a006/a008); t2_recheck 2 行未改.

### 删除清单 (D2, reviewer 逐条确认)

| # | 位置 | 删除内容 (摘要) | 原因 | 保留 |
|---|---|---|---|---|
| D-1 | model/01:112 | 句末 "…on a particular topic." 的句号 (改写句被 PDF 原句吸收) | R2 残留改写句; 该行其它原子 (p8 a002/a003/a005 等) verbatim 不含被删部分 | 同处 PDF 原句 "…topic (see Concept Map, below)." |
| D-2 | model/01:178 Purpose 格 | "Further modify or describe a specific set of variables within an observation" | R2 残留改写; 该行仅承载 p9 a018 | PDF 原文 "used to further modify … anatomic location)." (Examples 列未动) |

### PDF_TYPO

| T | 位置 | PDF | KB | 依据 |
|---|---|---|---|---|
| T-1 | model/01:94 (sv20_p0006_a020) | "Section 3, Associated Persons Data" | Section 4 | 同 PDF p5 两处 (a013/a014) 及 p8 a007 均为 "Section 4, Associated Persons Data"; SDTM v2.0 §3 = Study Subject Data |

### 范围外发现 (未改)

- O-a: model/01 H1 "Chapter 2" 与 `Source: … Section 2 (Pages 8-10)` 现与新 §1 (p4-7) 不符; 改标题/Source 行属规则 6 风险, 主控定.
- O-b: §2 引言段 (PDF §2 正文, 位于 2.1 之前) 在 KB 里挂在 `## 2.1` 标题下 (:110-120), 且无 `## 2` 标题; 本次新增 p8 句同样落在该处 (PDF 顺序正确, 标题归属沿用 KB).
- O-c: :156 (原 :45) Define-XML 句缺 PDF "available at https://www.cdisc.org/standards/data-exchange/define-xml" (p9 a003, fp=EQUIVALENT); p10 a001 "see the Define-XML specification…" 尾句亦未见, 未核.
- O-d: Qualifier Subclasses 表 Examples 列 (KB 自写, PDF 无) 未加 D6 KB note 标注.

### 触碰过的 unparseable 表

- model/01:172 (原 :61) Qualifier Variable Subclasses 表: 仅改 Variable Qualifiers 行 Purpose 格 → reviewer 须人工核该格.

### git diff --stat

```
 knowledge_base/model/01_concepts_and_terms.md | 117 +++++++++++++++++++++++++-
 1 file changed, 114 insertions(+), 3 deletions(-)
```

### 自检命令

`python3` 扫 `work/pdf_atoms.jsonl` p4-p7 全部原子 + p8 a004/a006-a009 + p9 a018 的 verbatim (去空白/粗体) 是否为 KB 子串: 93/93 命中 (a020 为 T-1 改值, a018 去掉前缀 "Variable Qualifiers" 后命中).

## attempt 1 续 (主控裁定 a-d)

- md5 e31323a1… → `bf7e92123fd76767ace1b766d58f67cf`; 行号以下为续改后.

| # | 位置 | 裁定 | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| C-1 | model/01:1, :3 | (a) | REPLACED | H1 → "SDTM v2.0 — Sections 1-2: Introduction; Model Concepts and Terms – Organization of the SDTM"; Source → "Sections 1-2 (Pages 4-10)" | 4, 8 |
| C-2 | model/01:110 | (b) | INSERTED | 新增 `## 2 Model Concepts and Terms – Organization of the SDTM` (PDF 原标题, en dash); §2 引言 + Concept Map 挂其下 | 8 |
| C-3 | model/01:154 | (b) | MOVED | `## 2.1 Model Concepts and Terms — Variables` 原文字不变, 移到 Concept Map 之后、`### Variable Roles` 前 (PDF 2.1 起于 p9) | 9 |
| C-4 | model/01:158 | (c) sv20_p0009_a003 | INSERTED | Define-XML 句补 ", available at https://www.cdisc.org/standards/data-exchange/define-xml" | 9 |
| C-5 | model/01:197 | (c) sv20_p0010_a001 | REPLACED | "…date, datetime)." → "…datetime); see the Define-XML specification … Define-XML data types." | 10 |
| C-6 | model/01:174 | (d) D6 | INSERTED | 表上方 `> KB note (not in SDTMIG): The Examples column is KB-authored.` | - |
| C-7 | model/01:180 | (d) D2 | REPLACED | Synonym 行 Examples "--TEST, --LOINC (for --TESTCD)" → "--TEST (for --TESTCD)" | 6 |

- (d) 矛盾核查: Examples 列逐格对 PDF p9 子类定义 + p6 §1.4 + model/02 角色列. 唯一矛盾 = --LOINC 列为 Synonym Qualifier, 与 PDF p6 a027 (--LOINC 已改为 Record Qualifier) 冲突 → D2 删 (删除清单 D-3). 其余格 (--CAT/--SCAT, --ORRES/--STRESC/--STRESN, --MODIFY/--DECOD/--TEST, --REASND/AESLIFE/--BLFL/--POS/--LOC/--SPEC/--NAM, --ORRESU/--ORNRHI/--ORNRLO/--DOSU) 与 PDF / model/02 角色一致.
- 删除清单追加: | D-3 | model/01:180 | ", --LOINC" | KB 自写且与 PDF p6 矛盾 (D2) | 无 |
- 锚点: 全仓 (除 releases/ archive/) grep `01_concepts_and_terms(.md)?#` 无锚点引用; 引用 model/01 的 knowledge_base/INDEX.md、ROUTING.md、docs/TRACEABILITY.md 均为文件级链接, 未断. (INDEX/ROUTING 里若有 "Chapter 2" 描述属白名单外, 未改.)
- 范围外 (仍未改): :197 KB "The SDTM type specified…" 缺 PDF 句首 "Note that"; 2.1 下 5 roles / 子类表为 KB 改写体 (非本批 atoms).
- 验证:
  - `python3 tools/check_links.py | grep "broken relative links"` → `broken relative links: 18668 (live docs: 42)` (≤42 ✓)
  - `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → RED, 15 回退全为 ig34 p0257-0263 (并行 MB/MS 批); `grep -c sv20 fp_regress.jsonl` = 0 → model/01 范围 0 回退.

## attempt 2

- 归档: `evidence/failures/t2_B-model01_attempt_1.{patch,md}` (规则 B). 在工作区续改; md5 bf7e9212… → `01b3101934c70175555edcc44c9eab2d`; diff --stat 累计 +149/-34.

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| A2-1 | model/01:180 | sv20_p0009_a016 (recheck→REAL_GAP) | REPLACED | Synonym Purpose 格 → PDF 原文 (含 e.g. 括号); 旧改写格 D2 删 (D-4) | 9 |
| A2-2 | model/01:184 | sv20_p0009_a019 (recheck→REAL_GAP) | INSERTED | 表后、Domain Codes 前插原句 "The SDTM includes variable metadata…Section 2.2, Table Structure." | 9 |
| A2-3 | model/01:199 | sv20_p0009_a021 | REPLACED | 句首补 "Note that" | 9 |
| A2-4 | model/01:178/179/181 | sv20_p0009_a014/a015/a017 | REPLACED | Grouping/Result/Record Purpose 格 → PDF 原文 (去句末 ";"/"; and"); 旧改写格 D2 删 (D-5..D-7) | 9 |
| A2-5 | model/01:154 | L-1 | REPLACED | `## 2.1 … — Variables` em dash → en dash (PDF p9); 全仓 (除 releases/archive) 无该锚点引用 | 9 |
| A2-6 | model/01:174 | L-2 | REPLACED | D6 前缀 → `> KB note (not in SDTM v2.0):` | - |
| A2-7 | model/01:164-168 | O-r1 sv20_p0009_a008-a012 | REPLACED | 5 roles 编号改写列表 → PDF 项目列表逐字 (粗体保留); 旧改写 D2 删 (D-8); 该块只承载 a008-a012 | 9 |
| A2-8 | model/01:203-217 | O-r2 sv20_p0010_a003-a016 | REPLACED | §2.2 KB 两列表 + **Note:** 段 → PDF 原结构 (引导句 + 11 项列表 + 2 句段落) 逐字 (规则 3 跟 PDF 走: PDF 为列表非表); 旧表/Note 删 (D-9) | 10 |
| A2-9 | model/01:114 | sv20_p0008_a005 | REPLACED | "subjects — which … animals — or" → PDF "subjects—which … animals—or" (双向扫描发现的唯一残留差异) | 8 |

- O-r3 核查: p11 起为 `3 Study Subject Data` (PDF §3, p11 正文 "Each study subject domain dataset is distinguished by a unique 2-character code…" / "Domain-specific variables, a concept introduced in SDTM v1.5…") → **不属 §2**, Source 行不改 (仍 4-10). :186-195 `### Domain Codes` 前 3 块 (DOMAIN 3 用途 / `--` 前缀 / Domain-specific variables) 为 p11 §3 内容的改写, 挂在 2.1 下 = 错位; 后 2 段 (DOMAIN/RDOMAIN、SAS v5) 是 p9 §2.1 原文. 未动, 交主控 (候选: p11 改写块移至 model/02 §3 引言或按 D6/D2 处理).
- 删除清单追加: D-4..D-7 (:178-181 四个旧改写 Purpose 格), D-8 (:164-168 旧编号 5 roles 列表), D-9 (§2.2 旧 Column/Description 表 11 行 + 旧 **Note:** 段). 均由同处 PDF 原文取代, 无信息丢失 (旧表 "SAS data type: `Char` or `Num`" / "`--` prefix" 等 KB 自写细节一并去除 — PDF 列表无此信息, 不矛盾但属改写体, 按主控 O-r2 "按 PDF 原文恢复").
- census: 本批 unparseable 表从 2 张降为 1 张 (§2.2 表改为列表); 仍剩子类表, 须人工核.
- 验证 (S = scratchpad/t2_B-model01_writer):
  - `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_a2.json` → `KB tables: 1; status: {'UNPARSEABLE': 1}; PDF_ONLY: 0; diffs: 0` GREEN
  - `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_a2.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_reg_a2.jsonl` → RED, 15 回退全为 ig34 p0257-0263 (并行批); `grep -c sv20 $S/fp_reg_a2.jsonl` = 0
  - `python3 tools/check_links.py | grep "broken relative links"` → `broken relative links: 18668 (live docs: 42)`
  - 双向扫描: p8-p10 全部非图原子 verbatim (去空白/粗体/表格竖线; 子类项去 "X Qualifiers," 前缀与句末 ";"/"; and") 均为 KB 子串, 0 MISS.

## attempt 2 续 (O-r3 裁定: p11 归 model/02)

- kb_files 扩入 `knowledge_base/model/02_observation_classes.md` (主控). md5: model/01 01b31019… → `4567b9ae9b3fadfdc55445bfd802fa7a`; model/02 `d0069659b1def0a798aecf7610aa225d` → `d4f124b0bf299399ac23829682f61a0b`. Source 行两文件均未改 (model/01 4-10; model/02 11-39).
- 查重: model/02 原 `## Overview` 只有 2 段改写 (合并 p11 a015/a006、a019/a020, "Domains based on…share" 改写 "Datasets based on…"); p11 其余原文 (§3 引言、DOMAIN/RDOMAIN、`--` 前缀、root、domain-specific v1.5、p12 a002) 均无 → 按 "无" 分支: 补 model/02, 删 model/01 3 块 (RELOCATE, 无指针).

| # | 位置 (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| A2c-1 | model/02:7-41 (`## Overview` 下) | sv20_p0011_a001-a032 + p0012_a001-a002 | INSERTED | `### 3 Study Subject Data` + `### 3.1 The General Observation Classes` (PDF 原标题) 及全部正文/3 项列表逐字; `## Overview` 标题保留 (锚点不动) | 11-12 |
| A2c-2 | model/02 原 :7, :9 | Overview 2 段改写 | D2 删 (D-10) | R2 残留改写, 信息全被 A2c-1 原文覆盖; fp_baseline 无原子命中这两段 | 11 |
| A2c-3 | model/01 原 :186-195 | `### Domain Codes` 标题 + DOMAIN 3 用途列表 + `--` 前缀句 + **Domain-specific variables** 段 | MOVED (RELOCATE, D-11) | p11 §3/§3.1 内容的改写; 原文已在 model/02 A2c-1; 不留指针 | 11 |

- 保留: model/01 p9 原文 2 段 ("All datasets for data about individuals…", "The SDTM is structured so that…SAS v5…") 现紧接 a019 句之后, 在 `## 2.2` 前, 顺序 = PDF p9.
- 锚点: 全仓 (除 releases/archive) 无 `model/01…#domain-codes` / `model/02…#overview` 引用.
- 注: model/02 `## 3.1.1` 下 Interventions 定义句与 A2c-1 列表第 1 项同文 (原有, 3.1.1 无对应 PDF 句), 未动, 交 reviewer 判是否 D2 去重.
- 验证:
  - p11 全部原子 + p12 a002 verbatim 为 model/02 子串: 0 MISS (p12 a001 为 a032 跨页尾, 已含)
  - `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_a2c.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_reg_a2c.jsonl` → RED, 15 回退全为 ig34 p0257-0263 (并行批); `grep -c sv20` = 0
  - `python3 tools/check_links.py | grep "broken relative links"` → `broken relative links: 18668 (live docs: 42)`
  - `git diff --stat -- knowledge_base/model/` → 01 +/-192, 02 +/-30 (2 files, +176/-46)

## attempt 2 续 2 (reviewer PASS 后收尾)

- md5: model/01 → `531c2d5459604aefdc238ff56eb92bef`; model/02 → `2533042d40e8489996198e18896e316b`.

| # | 位置 (改后) | ref | action | 摘要 |
|---|---|---|---|---|
| R-1 | model/02 原 :41 (+其后空行) | Interventions 重复句 | D2 删 (D-12) | `## 3.1.1` 下 "The Interventions Observation Class represents…" 与 :23 列表项同文, 留 :23 (PDF p11 所属位置) |
| L-3 | model/01:122 | sv20_p0008 Concept Map 标题 | REPLACED | "Concept Map:" → "Concept Map." (PDF p8) |
| L-4 | model/02:7, :19 | 新增标题层级 | REPLACED | `### 3 Study Subject Data` / `### 3.1 The General Observation Classes` → `##` (与 `## 3.1.1` 同级); 既有标题文字未改 |

- 锚点: 全仓 (除 releases/archive) grep `model/0[12]…#` (concept-map / overview / 3-study / 31-the) 无引用.
- 验证:
  - `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_a2c2.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_reg_a2c2.jsonl` → RED, 15 回退全为 ig34 p0257-0263 (并行批); `grep -c sv20` = 0
  - `python3 tools/check_links.py | grep "broken relative links"` → `broken relative links: 18668 (live docs: 42)`
  - `git diff --stat -- knowledge_base/model/` → 2 files, +177/-49

## attempt 2 续 3 (reviewer 更正)

- model/02 md5 → `00146fbcca61f529bbf1026df381c69f`.
- 删除清单追加:
  - D-13 | model/02 原 :93 (+其后空行) | `## 3.1.2` 下 "The Events Observation Class represents…" | 与 :24 列表项同文, PDF p15 无此句 (D2) | 留 :24
  - D-14 | model/02 原 :160 (+其后空行) | `## 3.1.3` 下 "The Findings Observation Class represents…" | 与 :25 同义, PDF p20 无此句 (D2) | 留 :25
- 验证:
  - `grep -n "Observation Class represents" knowledge_base/model/02_observation_classes.md` → 仅 :23/:24/:25
  - fp_match (`--out $S/fp_a2c3.jsonl --regress-out $S/fp_reg_a2c3.jsonl`) → RED, 15 回退全为 ig34 p0257-0263 (并行批); `grep -c sv20` = 0
  - `python3 tools/check_links.py | grep "broken relative links"` → `broken relative links: 18668 (live docs: 42)`
  - `git diff --stat -- knowledge_base/model/` → 2 files, +177/-53

## attempt 2 续 4 (auditor O-1)

- model/02 md5 → `15682cb09de2806b06177ec25f386ffa`.
- :1 H1 "Chapter 3.1: The General Observation Classes" → "Sections 3-3.1: Study Subject Data; The General Observation Classes" (PDF p11 两节原标题); :3 Source "Section 3.1" → "Sections 3-3.1 (Pages 11-39)".
- 删空标题 `## Overview` (+空行) (D-15, 无内容). 锚点: `grep -rn "02_observation_classes(.md)?#overview"` 全仓 (除 releases/archive) 0 命中.
- 验证: fp_match (`--out $S/fp_a2c4.jsonl --regress-out $S/fp_reg_a2c4.jsonl`) → RED, 15 回退全为 ig34 p0257-0263 (并行批), `grep -c sv20` = 0; `python3 tools/check_links.py | grep "broken relative links"` → `broken relative links: 18668 (live docs: 42)`; `git diff --stat -- knowledge_base/model/` → 2 files, +178/-56.
