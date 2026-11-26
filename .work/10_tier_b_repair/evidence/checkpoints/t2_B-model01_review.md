# T2 B-model01 — reviewer verdict

## attempt 1

**Verdict: CONDITIONAL** (KB 改动本身全部有出处、无回退; t2_recheck 2 条判 REAL_GAP + 同表/同段 R2 遗留短语 → 见修正清单)

- reviewer: oh-my-claudecode:code-reviewer (独立于 writer); base ae17f74; 只审 `knowledge_base/model/01_concepts_and_terms.md` (md5 应为 writer 续改后 bf7e9212…)
- 真值: `work/pdf_pages/sv20_p0004..0010.txt` + pdftoppm 渲染 p5/p8/p9 (scratch)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-model01_reviewer/`

### 命令与结果 (可复跑; S=上面 scratch)
| 命令 | exit | 关键输出 |
|---|---|---|
| `table_census.py --manifest $S/manifest.json --out $S/census_after.json` | 0 | `KB tables: 2; status: {'UNPARSEABLE': 2}; PDF_ONLY: 0` GREEN (两表均人工核, 见下) |
| `fp_match.py --out $S/fp_after.jsonl --baseline work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` | 1 | RED; 回退全为 ig34 p0257-0263 (并行 MB/MS 批); `grep -c sv20 $S/fp_regress.jsonl` = **0** |
| `python3 tools/check_links.py \| grep "broken relative links"` | 0 | `broken relative links: 18668 (live docs: 42)` ≤ 42 ✓ |
| `python3 -I $S/scan.py 4,5,6,7 5 108` / `8 110 152` / `9,10 154 217` | 0 | 双向逐句扫描 (归一化空白/Markdown/破折号/折行连字符), 结果见下 |

### (1) §1 Introduction 双向逐句 (pp4-7 ↔ KB :5-108)
- PDF→KB: p4-p7 全部句子 / 列表项 / 3 个无编号小标题命中且顺序一致; 唯一 MISS = p6 "still listed in Section 3, Associated Persons Data" (= T-1 改值, 预期). 脚本报的 4 个 ORDER 为重复子串假阳性 (SENDIG 前缀出现 2 次; "Section 3.1.x …" 在 p5 已出现), 已对 diff 逐段目视复核顺序 = PDF.
- KB→PDF: :5-108 每句均在 PDF 中; 唯一 NOSRC = :94 "Section 4" (T-1). 无自造句.
- 标题: `## 1 Introduction` / `## 1.1 Purpose` / `## 1.2 Implementation Advice for this Model` / `## 1.3 Relationship to Prior CDISC Models` / `## 1.4 Significant Changes from Prior Versions` / `### Reorganization of Content` / `### Changes to Structures of Tables` / `### Changes to Datasets and Variables` — 与渲染 p4/p5/p6 逐字一致 (3 个粗体无编号小标题 → ###).
- p8 §2 引言 (:112-120): PDF→KB 全命中 (含 a004 "(see Concept Map, below)", a006 后两句, a007-a009); KB→PDF 全有出处. "subjects — which … animals — or" 空格破折号为原有格式, 非改动.

### (2) H1 / Source / `## 2`
- :1 H1 "Sections 1-2: Introduction; Model Concepts and Terms – Organization of the SDTM" = PDF 两节原标题 (p4 "1 Introduction", p8 "2 Model Concepts…SDTM", en dash) ✓
- :3 "Sections 1-2 (Pages 4-10)" ✓ (p4 起, §2.2 止于 p10)
- :110 `## 2 Model Concepts and Terms – Organization of the SDTM` = p8 标题逐字 ✓; :154 `## 2.1` 移到 Concept Map 后 = PDF 2.1 起于 p9 ✓ (原文字不变, 仍为 em dash, 见 L-1)

### (3) R2 修正与删除
| ref | 判定 | 证据 |
|---|---|---|
| p8 a004 (:112) | OK | "a collection of observations on a particular topic (see Concept Map, below)." 逐字 |
| D-1 (:112 句号) | OK | 旧改写句仅缺括号, 已被原句取代, 无信息丢失 |
| p9 a018 / D-2 (:182 Purpose) | OK | 格 = p9 "used to further modify or describe 1 or more … the laterality of an anatomic location)." 逐字; 旧改写格删除正确 |
| D-3 (:180 删 ", --LOINC") | OK, 真矛盾 | p6: "--LOINC … was changed from Synonym Qualifier of --TESTCD to Record Qualifier"; p29 变量表 --LOINC Role = "Record Qualifier". KB 列为 Synonym Qualifier 例 = 与 PDF 矛盾 → D2 删除成立 |

### (4) T-1 (p6 a020 "Section 3" → KB "Section 4")
- 可由 PDF 自身确定: p5 两处 "Section 4, Associated Persons Data"、p8 "described in Section 4, Associated Persons Data"; §3 = Study Subject Data (p5). 按 PDF_TYPO 取舍规则写正确值 + 登记 ✓

### (5) Define-XML
- :158 = p9 "…Define-XML specification, available at https://www.cdisc.org/standards/data-exchange/define-xml." 逐字 (PDF 折行 "data-\nexchange" 为 URL 内连字符, 正确合并) ✓
- :197 尾句 = p9-10 "…(e.g., integer, float, date, datetime); see the Define-XML specification for information about how to represent SDTM types using Define-XML data types." 逐字 ✓; 同行仍缺句首 "Note that" (见修正 #3)

### (6) 人工逐格: Qualifier Variable Subclasses 表 (:176-182) vs 渲染 p9 (PDF 为项目列表, 非表)
| 行 | Subclass 格 | Purpose 格 | Examples 格 (KB 自写, 对 p9/p6/p26-30 变量表 Role) |
|---|---|---|---|
| Grouping | 一致 | 差异: 缺 "(e.g., categories or subcategories)"; "used to group"→"Group" (原有改写) | 一致 (--SCAT Role=Grouping) |
| Result | 一致 | 差异: 缺 "and that answer the question raised by the topic variable" (原有改写) | 一致 |
| Synonym | 一致 | 差异: 缺 "(e.g., coded version of a verbatim topic variable or the name associated with a test code)" (= recheck a016) | 一致 (--MODIFY/--DECOD Synonym of --TRT/--TERM; --TEST Synonym of --TESTCD); --LOINC 已删 ✓ |
| Record | 一致 | 差异: 缺 ", rather than describing a particular variable within a record (e.g., for a lab test, the specimen type and the name of lab that performed the test)" (原有改写) | 一致 (--POS/--LOC/--BLFL/--NAM/--SPEC Role=Record; AESLIFE 为 AE 专用, --SLIFE Role=Record) |
| Variable | 一致 | **一致** (本批改格, 逐字) | 一致 (--DOSU Variable of --DOSE; --ORNRLO 等 Variable) |
- 表头 `| Subclass | Purpose | Examples |` + 分隔线: 结构行, 原有未动.
- 2.2 表 (:203-215, UNPARSEABLE #2): 本批未触碰; 已知为改写体 (见 O-r2).

### (7) D6 标注 :174
- 位置: 引导句与表之间, 表上方单独一行 → 符合 D6 "在其上方单独一行标注"; 只标 Examples 列 (Purpose 列来自 PDF) 正确.
- 措辞: 固定前缀 `> KB note (not in SDTMIG):` 照 D6 原样; 但本文件源为 SDTM v2.0 不是 SDTMIG → L-2 (主控定是否改 "(not in SDTM v2.0)").
- 不矛盾核查: Examples 列逐格见 (6), 除已删 --LOINC 外均与 PDF 变量表 Role 一致 ✓

### G-TB6 结构行签字
`:1 H1` ✓ · `:3 Source` ✓ · `:5 ## 1 Introduction` ✓ · `:7 ## 1.1` ✓ · `:13 ## 1.2` ✓ · `:30 ## 1.3` ✓ · `:36 ## 1.4` ✓ · `:40 ### Reorganization of Content` ✓ · `### Changes to Structures of Tables` ✓ · `### Changes to Datasets and Variables` ✓ · `:110 ## 2` ✓ · `:154 ## 2.1` (移动, 文字不变) ✓ · `:174 KB note` ✓ (D6). 新增/改动正文行 0 条无出处 (T-1 除外, 已登记). 锚点: writer 称无锚点引用 model/01, 复核 INDEX.md:17 / ROUTING.md:83,143 为文件级链接 ✓.

### R2 recheck
| atom | 判定 | KB 证据 | PDF (≤25 词) |
|---|---|---|---|
| sv20_p0009_a016 | **REAL_GAP** | :180 Purpose "Specify an alternative name for a particular variable in an observation" 缺 e.g. 括号; Examples 列为 KB 自写具体变量, 不能代替 PDF 概念示例 | p9 "(e.g., coded version of a verbatim topic variable or the name associated with a test code)" |
| sv20_p0009_a019 | **REAL_GAP** | 全 KB 无此句 (fp hit_any=None); :201 "Tables in the SDTM v2.0 document include the following variable metadata" 不给 "for the standard variables" 与交叉引用; 靠所在节隐含 = R2 REAL_GAP | p9 "The SDTM includes variable metadata for the standard variables; variable metadata attributes are described in Section 2.2, Table Structure." |

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| a016 :180 | R2 | REAL_GAP, 见上 | p9 |
| a019 (应在 :182 表后、:184 前) | R2 | REAL_GAP, 见上 | p9 |
| :197 | R2 / 本批已改行 | 缺句首 "Note that" (writer 已列范围外, 但该行本批已改) | p9 "Note that the SDTM type specified in this document…" |
| :178 / :179 / :181 Purpose | R2 / R3 同表 | 原有改写丢短语 (见 (6)); 同表 Variable 行已逐字, 现同表口径不一 | p9 |
| L-1 :154 | 标题 | `## 2.1 … — Variables` em dash, PDF / 新 `## 2` 用 en dash (原有, 未动) | p9 "2.1 Model Concepts and Terms – Variables" |
| L-2 :174 | D6 措辞 | "not in SDTMIG" 对 SDTM v2.0 文件不准确 (D6 固定前缀) | - |
| L-3 :122 | 标题 | "Concept Map:" vs PDF "Concept Map." (原有) | p8 |

### CONDITIONAL 修正清单 (writer attempt 2, 仅改 model/01)
1. :180 Synonym Qualifiers Purpose 格 → 换为 p9 a016 原文 "specifying an alternative name for a particular variable in an observation (e.g., coded version of a verbatim topic variable or the name associated with a test code)" (同 a018 做法; 旧改写格 D2 删).
2. 在 :182 表后、`### Domain Codes` 前插入 p9 a019 原句 "The SDTM includes variable metadata for the standard variables; variable metadata attributes are described in Section 2.2, Table Structure."
3. :197 "The SDTM type specified…" → "Note that the SDTM type specified…".
4. :178 / :179 / :181 Purpose 格分别换为 p9 a014 / a015 / a017 原文 (去掉句末 ";"/"; and"), 与 a018 行口径一致 (R2 + R3 同表).
5. (可选, 主控定) L-1 :154 em dash → en dash; L-2 KB note 括注措辞.
- 改后复跑: fp_match sv20 回退 0; check_links live docs ≤ 42.

### 范围外 (登记, 未要求本批改)
- O-r1: :162-168 5 roles 列表为改写体 (丢 "such as those that"、"the subject involved in the study" 等), R2 下应为 REAL_GAP; 非本批 atoms.
- O-r2: :201-217 §2.2 表 Description 列 + Note 段为改写体 (如 Usage Restrictions 缺 "in a particular kind of trial, a particular class, or a particular domain"); 非本批 atoms.
- O-r3: :184-193 Domain Codes 段来源为 sv20 p11, 超出 Source 行 "Pages 4-10"; 本批未动.

## attempt 2 复审

**Verdict: PASS** (附 1 条待执行裁定 R-1: 删 model/02:41; 单行 D2 删除, 主控用 grep 核即可, 不需再复审)

- 范围: model/01 (md5 4567b9ae…) + model/02 (d4f124b0…), base ae17f74; 真值 sv20 p4-p12 文本 + 渲染 p9/p10/p11.
| 命令 | exit | 关键输出 |
|---|---|---|
| `fp_match.py --out $S/fp_a2.jsonl --baseline work/fp_baseline.jsonl --regress-out $S/fp_reg_a2.jsonl` | 1 | RED 仅并行批 ig34; `grep -c sv20 $S/fp_reg_a2.jsonl` = **0** |
| `table_census.py --manifest $S/manifest2.json` (model/01 p8-10 + model/02 p11-12) | 0 | GREEN; 余下 UNPARSEABLE 是子类表 + model/02 原有变量表 (本批未动) |
| `python3 tools/check_links.py \| grep "broken relative links"` | 0 | `live docs: 42` ✓ |
| `$S/scan.py` 双向扫描: 4-7 / 8 / 9-10 (model/01) + 11 (model/02 :1-36), KBF 环境变量指定文件 | 0 | 见下 |

### (1) 修正清单 #1-#4 + L-1/L-2
- #1 :180、#4 :178/:179/:181: Purpose 格 = p9 a016/a014/a015/a017 原文逐字 (只去了项名前缀和句末 ";"/"; and"), 对渲染 p9 逐格一致 ✓; Examples 列未动 ✓
- #2 :184 a019 原句逐字, 位于表后、DOMAIN 段前 = PDF p9 顺序 ✓; #3 :188 "Note that…" ✓
- L-1 :154 en dash ✓; L-2 :174 `> KB note (not in SDTM v2.0):` ✓
### (2) O-r1 / O-r2 / :114
- :164-168 5 roles = p9 项目列表逐字 (粗体是格式, 不算内容) ✓; §2.2 :190-204 = p10 引导句 + 11 项 + 2 句段落逐字, 结构与渲染 p10 一致 (PDF 是列表, 不是表) ✓; :114 "subjects—which … animals—or" = p8 ✓
- D-8/D-9 删掉的是旧改写行; 只丢了 KB 自写的 "`Char` or `Num`" 和 "(Identifier, Topic, Timing, etc.)"。这两处在 p9 原文 (character or numeric / 5 roles) 已有, 不需 D6 保留 ✓
### (3) model/02
- `### 3 Study Subject Data` / `### 3.1 The General Observation Classes` = p11 标题逐字 ✓; :7-35 正文对 p11-p12 a002 双向: PDF→KB 0 MISS, KB→PDF 只有 H1/Source/Overview 结构行 ✓
- D-10 (Overview 旧 2 段): 每个信息点在 p11 原文里都有 (3 类 / 2 种数据集 / 共享 identifier+timing) → 无损 ✓
- D-11 (model/01 Domain Codes 3 块): 2 字符码、DOMAIN 的 3 种用途、RDOMAIN、`--` 前缀、domain-specific 都在 model/02 :15-33 原文里 → 无损; model/01 不再有残留, 也不留指针 ✓
- L-4 (LOW, 不阻断): model/02 `### 3`/`### 3.1` 挂在 `## Overview` 下, 但 `## 3.1.1` 是 ## 级 → 3.1.1 标题级别比 3.1 高, 层级倒置。为保锚点可以接受, 主控知悉即可。
### (4) 裁定 R-1
- PDF 只在 §3.1 列表第 1 项 (p11) 有 Interventions 定义句; §3.1.1 (p12) 标题后直接接表名, 没有这句 → 按 D2 **留 model/02:23 (列表项), 删 model/02:41**。:41 前的 `**Structure:**` 行保留。3.1.2 / 3.1.3 下没有同类重复 (grep "Observation Class represents" 只命中 :23-25 和 :41)。
### (5) 双向全扫 sv20 pp4-12a002
- 唯一 KB≠PDF = :94 T-1 (已登记); 遗留 L-3 (:122 "Concept Map:" vs PDF "Concept Map.", 原有, LOW); 其余新增/改动行没有无出处内容。

## attempt 2 续 2 复审

**Verdict: CONDITIONAL** (本次 3 处 delta 都对, 但 reviewer 撤回 attempt 2 复审里的一句错误结论 → 再补 2 行 D2 删除)
- R-1 ✓: model/02 原 :41 已删, :23 列表项留着, `**Structure:**` 行留着。L-3 ✓: model/01:122 "### Concept Map. Relationships Between SDTM Domains" = p8。L-4 ✓: model/02 `## 3` (:7) / `## 3.1` (:19) 与 `## 3.1.1` (:37) 同级, 标题文字未改。
- **更正**: attempt 2 复审写的 "3.1.2/3.1.3 下没有同类重复" 是错的 (当时 grep 输出被 head 截断)。实测 `grep -n "Observation Class represents" knowledge_base/model/02_observation_classes.md` → :23-25 (列表) + **:93** (`## 3.1.2` 下, 与 :24 同文) + **:160** (`## 3.1.3` 下, 与 :25 同义, "ECG testing" 是改写)。PDF p15 `3.1.2` / p20 `3.1.3` 标题后直接接表名, 没有这两句 → 同 R-1, 按 D2 删。
- 修正清单: (R-2) 删 model/02:93 及其后空行; (R-3) 删 model/02:160 及其后空行。两处 `**Structure:**` 行都留。删后主控 grep 核 "Observation Class represents" 只命中 :23-25 即可。
- `fp_match.py --out $S/fp_a2c2.jsonl --baseline work/fp_baseline.jsonl --regress-out $S/fp_reg_a2c2.jsonl` exit 1 (只有并行批 ig34), `grep -c sv20` = **0**; `python3 tools/check_links.py | grep "broken relative links"` → live docs 42 ✓

## 续3+续4 签字

**Verdict: PASS**
- 续3: model/02 原 :93/:160 已删; `grep -n "Observation Class represents" knowledge_base/model/02_observation_classes.md` 只命中 :21-23 (§3.1 列表); `**Structure:**` 行留在 :89 / :154 ✓
- 续4: H1 "Sections 3-3.1: Study Subject Data; The General Observation Classes" = p11 两个标题 "3 Study Subject Data"、"3.1 The General Observation Classes" 逐字 ✓; Source "Sections 3-3.1 (Pages 11-39)" ✓; 空的 `## Overview` 已删, `## 3` (:5) / `## 3.1` (:17) 与 `## 3.1.1`-`## 3.1.5` 同级 ✓
- 锚点: `grep -rn -E "02_observation_classes(\.md)?#|#overview" knowledge_base docs web/src tools .work/AGENT_GUIDE.md README.md` 无输出 (未截断); INDEX.md:18、ROUTING.md:38/86 是文件级链接 ✓ (INDEX "Ch3.1" 描述在白名单外, 未改)
- `fp_match.py --out $S/fp_c34.jsonl --baseline work/fp_baseline.jsonl --regress-out $S/fp_reg_c34.jsonl` exit 1 (只有并行批 ig34), `grep -c sv20` = **0**; `python3 tools/check_links.py | grep "broken relative links"` → live docs 42 ✓
