# T2S S-MOD3 review (model/05_study_level_data.md, 源 SDTM v2.0 §5 p51-63)

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** — 叙述 95 行 / 19 标题 / 110 表行 550 格 (含 9 个新增 Role 括注) 独立核全部一致; 15 标题逐字 = PDF + 域代码; 删除 17 条、结构 3 条、D6 2 条逐条签字; 2 张 Mermaid = PDF 图. 无阻断项, 仅 LOW 观察 (不要求修).

- 审查对象: 工作树 md5 `88d0db4cc8858975bb3f1dc0748d020d` (333 行, = writer delta 终态) vs `git show HEAD:knowledge_base/model/05_study_level_data.md` (333 行). `git diff HEAD --stat` 本文件 +28/-28; 工作树其他 20 个 KB 文件为他批 (model/01/03/04, domains/*/spec.md), 不计. narrow_files 空.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-MOD3_reviewer/` (下称 $S)
- 独立方法 (不用 writer 的 bbox / atoms / celltab): `pdftotext -layout -f 51 -l 63 source/cdisc/SDTM_v2.0.pdf $S/lay.txt`; `$S/laycols.py` 按每段表头行列起点逐词归列 (Char/Num 判 Type, 标签溢出 Type 列的词归 Label, 去 `\f` 与页眉页脚); 叙述 `$S/prose_scan.py` (PDF 行→KB) 与 `$S/rscan.py` (KB 行→PDF); 13 页 110 dpi 渲染 (`pdftoppm -f 51 -l 63 -r 110 -png`) 逐页目视.

### 命令与结果 (repo 根, 可复跑)
| 命令 | 结果 |
|---|---|
| `python3 -I $S/prose_scan.py $S/lay.txt knowledge_base/model/05_study_level_data.md` | 改后 `prose lines HIT 95 MISS 0`; 对 `$S/base.md` → `HIT 80 MISS 15` (15 = 编号标题, 正是本批补的) |
| `python3 -I $S/rscan.py $S/lay.txt knowledge_base/model/05_study_level_data.md` | `HIT 71`; NOPDF = :1 H1 / :3 Source / :97 :117 D6 Notes 列说明 / :261 :299 D6 Structure / :279 :317 D6 Mermaid 注 / 2 段 mermaid 代码 (全量输出, 未截断) |
| `python3 -I $S/laycols.py $S/lay.txt knowledge_base/model/05_study_level_data.md $S/laycols.json` | `pdf rows 110 kb rows 110` / `cells 550 diffs 0` |
| 同上对 `$S/base.md` | `cells 550 diffs 9` = 恰为 9 个 Role 括注 (ELEMENT×2/ARM×2/TXPARM/VISIT/IETEST/TSPARM/ACPARM) |
| PDF Variable(s) Qualified 非空行 (laycols.json) | 17 行; KB Role 括注 17 处 (8 既有 + 9 新增), 且无 PDF 空 Qualified 而 KB 带括注者 (逐格精确比) |
| `python3 -I $S/celltab.py $S/laycols.json knowledge_base/model/05_study_level_data.md $S/base.md` | 逐格表 110 行, DIFF 0 (下附) |
| `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` | exit 0; `PDF tables parsed: 0 … KB tables: 13; status: {'UNPARSEABLE': 13}; cells compared: 0` GREEN — **0 格空比较, 无证明力** |
| `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` | RESULT RED, regress 72 条, sv20/model05 相关 0; fp_after sv20 p51-63 原子 120 条: 散文 42 (SENTENCE 31/LIST_ITEM 9/NOTE 2) 全命中 model/05; TABLE_ROW 70 / TABLE_HEADER 8 hit None (12 列行对 5 列 KB 不可匹配) → **表格无证明力**, 以 laycols + 渲染为准 |
| `grep -rnE "05_study_level_data(\.md)?#" knowledge_base web/src tools docs .work/AGENT_GUIDE.md README.md METHODOLOGY.md releases` | 无输出 rc=1 (未截断) → 0 入站锚点; 整文件引用 11 个文件, 不受标题改动影响 |
| `python3 tools/check_links.py 2>&1 \| grep "live docs"` | `broken relative links: 18668 (live docs: 42)` (写本文件后复跑同) |

### 页范围复核
`work/pdf_pages/sv20_p0050.txt` 末段为 §4 Associated Persons Relationships 叙述; `sv20_p0064.txt` 首行 `6 Datasets for Representing Relationships`; p51 首行 `5 Study-level Data`, p63 仅 OI Concept Map → 本批 = p51-63, 与 writer 一致.

### 双向全扫 — 逐页 (reviewer 自计; 叙述行 = layout 非表行, 标题含)
| 页 | PDF→KB 叙述/标题 | 表行 → KB | KB→PDF | 备注 |
|---|---|---|---|---|
| 51 | H `5`/`5.1`/`5.1.1`/`5.1.1.1` + 2 段 + 7 bullet + 1 段 + TE 引言 + 表题 → :5-:33 全命中 | TE 1-3 一致 | :5-:33 逐字 | 7 bullet 交叉引用 "(Section 5.1.x, …)" 全保留 |
| 52 | H `5.1.1.2` + 2 段 + 表题 → :45-:51 | TE 4-7, TA 1-6 一致 | 逐字 | PDF *arm* 斜体, KB 无 = 强调差异 (S-CH1 不计) |
| 53 | H `5.1.2` + 1 段 + 表题 → :66-:70 | TA 7-10, TX 1-8 一致 | 逐字 | |
| 54 | H `5.1.3`/`5.1.3.1`/`5.1.3.2` + 3 Note 框 + 3 段 + 表题 → :83-:113 | TT 1-7 一致 (+Notes 列) | 逐字; :97 D6 | Note 框 → `**Note:**` 逐字 |
| 55 | 表题 + H `5.1.4` + 1 段 + 3 bullet → :115, :132-:138 | TP 1-10 一致 (+Notes 列) | 逐字; :117 D6 | |
| 56 | H `5.1.4.1`/`5.1.4.2` + 1+2 段 + 表题 → :140-:162 | TV 1-9 一致 | 逐字 | |
| 57 | 表题 + H `5.1.4.3` + 1 段 → :164, :178-:180 | TD 1-9 一致 | 逐字 | |
| 58 | 表题 + H `5.1.5` + 1 段 + 表题 → :182, :192-:196 | TM 1-5, TI 1-6 一致 | 逐字 | |
| 59 | H `5.1.6` + 1 段 + 表题 → :209-:213 | TI 7-8, TS 1-10 一致 | 逐字 | TS Usage "Not in nonclinical trials" = R1 缺列 (O35-3/M-4, T4) |
| 60 | H `5.1.7` + 1 段 + 表题 → :229-:233 | TS 11, AC 1-12 一致 | 逐字 | |
| 61 | H `5.2`/`5.2.1` + 2 段 + 2 bullet + 表题 → :252-:265 | DI 1-7 一致 | 逐字; :261 D6 | |
| 62 | 图题 + H `5.2.2` + 1 段 + 表题 → :277, :297-:303 | OI 1-7 一致 | 逐字; :279 :299 D6 | *taxa* 斜体同 PDF |
| 63 | 图题 → :315 | — | :317 D6 + mermaid | |
合计: PDF 叙述/标题行 95 → MISS 0; 表行 110 → 550 格 diff 0; KB 非表行 71 HIT + 8 导航/D6 行 + 2 mermaid 块.

### 标题 (15 条替换) 逐字核
KB 19 个 `##`/`###` 标题去掉尾部 ` (XX)` 后按序 == PDF §5 全部 19 个编号标题 (脚本断言 `True`, 含未改的 5.1.1 / 5.1.3 / 5.1.4 / 5.2). 15 条替换签字:
| # | 行 | KB 改后 | PDF (页) | 签字 |
|---|---|---|---|---|
| 1 | :5 | `## 5 Study-level Data` | p51 | ✔ |
| 2 | :11 | `## 5.1 The Trial Design Model` | p51 | ✔ |
| 3 | :29 | `### 5.1.1.1 Trial Elements (TE)` | p51 | ✔ |
| 4 | :45 | `### 5.1.1.2 Trial Arms (TA)` | p52 | ✔ |
| 5 | :66 | `### 5.1.2 Trial Sets (TX)` | p53 | ✔ |
| 6 | :89 | `### 5.1.3.1 Trial Repro Stages (TT)` | p54 | ✔ |
| 7 | :109 | `### 5.1.3.2 Trial Repro Paths (TP)` | p54 | ✔ |
| 8 | :140 | `### 5.1.4.1 Trial Visits (TV)` | p56 | ✔ |
| 9 | :158 | `### 5.1.4.2 Trial Disease Assessments (TD)` | p56 | ✔ |
| 10 | :178 | `### 5.1.4.3 Trial Disease Milestones (TM)` | p57 | ✔ |
| 11 | :192 | `### 5.1.5 Trial Inclusion/Exclusion Criteria (TI)` | p58 | ✔ |
| 12 | :209 | `### 5.1.6 Trial Summary Information (TS)` | p59 | ✔ |
| 13 | :229 | `### 5.1.7 Challenge Agent Characterization (AC)` | p60 | ✔ |
| 14 | :259 | `### 5.2.1 Device Identifiers Dataset (DI)` | p61 | ✔ |
| 15 | :297 | `### 5.2.2 Non-host Organism Identifiers Dataset (OI)` | p62 | ✔ ("Non-host" 小写 h 同 PDF) |
- 域代码 (XX) 13 处 = 各节 DOMAIN 行 PDF Notes "must be "XX"" 的代码 (渲染核), 符合 S-MOD3 主控条 (导航保留, 不 D6). 0 入站锚点 (上表 grep).

### 删除清单 (17 条) 签字
| # | 内容 | 依据 | 签字 |
|---|---|---|---|
| D-1 | `## Overview` | 同位置由 PDF `5 Study-level Data` 取代; 0 入站锚点 | ✔ |
| D-2 | `## 5.1 Trial Design Model` | PDF 有 "The" | ✔ |
| D-3..D-15 | 13 个 KB 自拟 `### <名> (XX)` 标题文字 | 改为 PDF 编号原标题 + 保留 (XX) (delta M-1); TT/TP "Reproductive"→PDF "Repro", TS 补 "Information", DI/OI 补 "Dataset" | ✔ 13/13 |
| D-16 | TX `> KB note …: **Structure:** One record per Trial Set parameter per Trial Set` | PDF p53 表题 "Trial Sets—One Record per Trial Set Parameter" 已含记录结构 → S-MOD2 model/ 通用条 D2 (主控 M-3 同意) | ✔ |
| D-17 | TS `> KB note …: **Structure:** One record per trial summary parameter value` | PDF p59 表题 "Trial Summary—One Record per Trial Summary Parameter" → 同上 | ✔ |
- DI / OI Structure D6 (:261 / :299) 保留正确: PDF 表题仅 "Device Identifiers Dataset" / "Non-host Organism Identifiers Dataset", 无 One Record per; 内容与 PDF 不矛盾 (DISEQ "uniqueness within a parameter within a device"; OISEQ 同型) ✔.

### 结构改动 / D6 签字
| # | 位置 | 改动 | 核 | 签字 |
|---|---|---|---|---|
| S-1 | 15 标题 | 文字 → PDF 编号标题, 层级不动 | 见上 | ✔ |
| S-2 / D6 | :97 TT | "the Notes column below is not the PDF Notes column: rows 3-7 carry the PDF Usage Restrictions value (…); the DOMAIN row carries the domain code from the PDF Notes column." | 逐格: # 3-7 (RSTGCD…TTDUR) KB = PDF Usage "Not in human clinical trials" 5/5; DOMAIN `"TT"` = PDF Notes "must be "TT"" 的代码; STUDYID 空 = PDF Usage/Notes 均空. 措辞属实, 无编辑历史式措辞, 无矛盾格 | ✔ |
| S-2 / D6 | :117 TP | 同上, rows 3-10 | # 3-10 (RPATHCD…RPRFDY) 8/8 = PDF Usage; DOMAIN `"TP"` = PDF Notes 代码; STUDYID 空 | ✔ |
| S-3 | base :72-73 / :213-214 | 删 TX/TS Structure D6 | = D-16/D-17 | ✔ |
| Mermaid | :279-:295 DI | 6 节点 (Study/Device/Identifying Characteristic/identifier (SPDEVID)/parameter (DIPARM, DIPARMCD)/value (DIVAL)), 5 边 involves / has one or more / has / is represented using / has, 方向与 p62 图一致; D6 注页码 p62 正确 | ✔ |
| Mermaid | :319-:333 OI | 6 节点 (Study/Non-Host Organism/Taxon/identifier (NHOID)/parameter (OIPARM, OIPARMCD)/value (OIVAL)), 5 边同构, = p63 图; D6 注页码 p63 正确 | ✔ |

### 问题表
| ref | 检查项 | 问题 | 证据 | 严重度 |
|---|---|---|---|---|
| L-1 | 结构 | 5.1.1.1-2 / 5.1.3.1-2 / 5.1.4.1-3 与父节同为 `###` (层级扁平) | PDF 四级编号; S-FND "既有层级不改", writer M-2 已记 O35-1 | LOW, 不阻断 (T4) |
| L-2 | R1 缺列承载不一致 | TS TSVALCD/TSVCDREF/TSVCDVER 的 Usage "Not in nonclinical trials" 无 KB 承载, 而 TT/TP 同类值在 Notes 列 | p59-60 Usage 列; R1 缺列不补, 主控 M-4 已裁 | LOW, 不阻断 (O35-3/T4) |
| L-3 | D6 措辞 (可选) | :97/:117 "is not the PDF Notes column" 后又说 DOMAIN 行取自 PDF Notes, 读来略绕; 内容属实 | 逐格见上 | LOW, 可选润色, 不要求改 |
| L-4 | writer 报告 | 逐页日志手填原子数 2 处误记, 已在 "更正" 节自纠 (p54 12 / p58 5); fp 归因已自纠 | writer 报告 :261-262 | 信息 |

### 逐格表 (改后 110 行; # / Variable / Label / Type / Role(+Qualified) 对 $S/laycols.json 精确比; 渲染列 = 13 页 110 dpi 逐行目视)
| 表 | KB 行 | # | Variable | Label | Type | Role (+Qualified) | Notes 列 (TT/TP) | 渲染 | 本批 |
|---|---|---|---|---|---|---|---|---|---|
| TE | 37 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| TE | 38 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| TE | 39 | 一致 | ETCD | 一致 | 一致 | 一致 | - | 一致 | - |
| TE | 40 | 一致 | ELEMENT | 一致 | 一致 | 一致 | - | 一致 | Role 补括注 |
| TE | 41 | 一致 | TESTRL | 一致 | 一致 | 一致 | - | 一致 | - |
| TE | 42 | 一致 | TEENRL | 一致 | 一致 | 一致 | - | 一致 | - |
| TE | 43 | 一致 | TEDUR | 一致 | 一致 | 一致 | - | 一致 | - |
| TA | 55 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| TA | 56 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| TA | 57 | 一致 | ARMCD | 一致 | 一致 | 一致 | - | 一致 | - |
| TA | 58 | 一致 | ARM | 一致 | 一致 | 一致 | - | 一致 | Role 补括注 |
| TA | 59 | 一致 | TAETORD | 一致 | 一致 | 一致 | - | 一致 | - |
| TA | 60 | 一致 | ETCD | 一致 | 一致 | 一致 | - | 一致 | - |
| TA | 61 | 一致 | ELEMENT | 一致 | 一致 | 一致 | - | 一致 | Role 补括注 |
| TA | 62 | 一致 | TABRANCH | 一致 | 一致 | 一致 | - | 一致 | - |
| TA | 63 | 一致 | TATRANS | 一致 | 一致 | 一致 | - | 一致 | - |
| TA | 64 | 一致 | EPOCH | 一致 | 一致 | 一致 | - | 一致 | - |
| TX | 74 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| TX | 75 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| TX | 76 | 一致 | SETCD | 一致 | 一致 | 一致 | - | 一致 | - |
| TX | 77 | 一致 | SET | 一致 | 一致 | 一致 | - | 一致 | - |
| TX | 78 | 一致 | TXSEQ | 一致 | 一致 | 一致 | - | 一致 | - |
| TX | 79 | 一致 | TXPARMCD | 一致 | 一致 | 一致 | - | 一致 | - |
| TX | 80 | 一致 | TXPARM | 一致 | 一致 | 一致 | - | 一致 | Role 补括注 |
| TX | 81 | 一致 | TXVAL | 一致 | 一致 | 一致 | - | 一致 | - |
| TT | 101 | 一致 | STUDYID | 一致 | 一致 | 一致 | 空=PDF Usage 空 | 一致 | - |
| TT | 102 | 一致 | DOMAIN | 一致 | 一致 | 一致 | = PDF Notes 域代码 | 一致 | - |
| TT | 103 | 一致 | RSTGCD | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TT | 104 | 一致 | RSTAGE | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TT | 105 | 一致 | TTSTRL | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TT | 106 | 一致 | TTENRL | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TT | 107 | 一致 | TTDUR | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TP | 121 | 一致 | STUDYID | 一致 | 一致 | 一致 | 空=PDF Usage 空 | 一致 | - |
| TP | 122 | 一致 | DOMAIN | 一致 | 一致 | 一致 | = PDF Notes 域代码 | 一致 | - |
| TP | 123 | 一致 | RPATHCD | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TP | 124 | 一致 | RPATH | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TP | 125 | 一致 | TPSTGORD | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TP | 126 | 一致 | RSTGCD | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TP | 127 | 一致 | RSTAGE | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TP | 128 | 一致 | TPBRANCH | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TP | 129 | 一致 | RPHASE | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TP | 130 | 一致 | RPRFDY | 一致 | 一致 | 一致 | = PDF Usage | 一致 | - |
| TV | 148 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| TV | 149 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| TV | 150 | 一致 | VISITNUM | 一致 | 一致 | 一致 | - | 一致 | - |
| TV | 151 | 一致 | VISIT | 一致 | 一致 | 一致 | - | 一致 | Role 补括注 |
| TV | 152 | 一致 | VISITDY | 一致 | 一致 | 一致 | - | 一致 | - |
| TV | 153 | 一致 | ARMCD | 一致 | 一致 | 一致 | - | 一致 | - |
| TV | 154 | 一致 | ARM | 一致 | 一致 | 一致 | - | 一致 | Role 补括注 |
| TV | 155 | 一致 | TVSTRL | 一致 | 一致 | 一致 | - | 一致 | - |
| TV | 156 | 一致 | TVENRL | 一致 | 一致 | 一致 | - | 一致 | - |
| TD | 168 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| TD | 169 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| TD | 170 | 一致 | TDORDER | 一致 | 一致 | 一致 | - | 一致 | - |
| TD | 171 | 一致 | TDANCVAR | 一致 | 一致 | 一致 | - | 一致 | - |
| TD | 172 | 一致 | TDSTOFF | 一致 | 一致 | 一致 | - | 一致 | - |
| TD | 173 | 一致 | TDTGTPAI | 一致 | 一致 | 一致 | - | 一致 | - |
| TD | 174 | 一致 | TDMINPAI | 一致 | 一致 | 一致 | - | 一致 | - |
| TD | 175 | 一致 | TDMAXPAI | 一致 | 一致 | 一致 | - | 一致 | - |
| TD | 176 | 一致 | TDNUMRPT | 一致 | 一致 | 一致 | - | 一致 | - |
| TM | 186 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| TM | 187 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| TM | 188 | 一致 | MIDSTYPE | 一致 | 一致 | 一致 | - | 一致 | - |
| TM | 189 | 一致 | TMDEF | 一致 | 一致 | 一致 | - | 一致 | - |
| TM | 190 | 一致 | TMRPT | 一致 | 一致 | 一致 | - | 一致 | - |
| TI | 200 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| TI | 201 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| TI | 202 | 一致 | IETESTCD | 一致 | 一致 | 一致 | - | 一致 | - |
| TI | 203 | 一致 | IETEST | 一致 | 一致 | 一致 | - | 一致 | Role 补括注 |
| TI | 204 | 一致 | IECAT | 一致 | 一致 | 一致 | - | 一致 | - |
| TI | 205 | 一致 | IESCAT | 一致 | 一致 | 一致 | - | 一致 | - |
| TI | 206 | 一致 | TIRL | 一致 | 一致 | 一致 | - | 一致 | - |
| TI | 207 | 一致 | TIVERS | 一致 | 一致 | 一致 | - | 一致 | - |
| TS | 217 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| TS | 218 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| TS | 219 | 一致 | TSSEQ | 一致 | 一致 | 一致 | - | 一致 | - |
| TS | 220 | 一致 | TSGRPID | 一致 | 一致 | 一致 | - | 一致 | - |
| TS | 221 | 一致 | TSPARMCD | 一致 | 一致 | 一致 | - | 一致 | - |
| TS | 222 | 一致 | TSPARM | 一致 | 一致 | 一致 | - | 一致 | Role 补括注 |
| TS | 223 | 一致 | TSVAL | 一致 | 一致 | 一致 | - | 一致 | - |
| TS | 224 | 一致 | TSVALNF | 一致 | 一致 | 一致 | - | 一致 | - |
| TS | 225 | 一致 | TSVALCD | 一致 | 一致 | 一致 | - | 一致 | - |
| TS | 226 | 一致 | TSVCDREF | 一致 | 一致 | 一致 | - | 一致 | - |
| TS | 227 | 一致 | TSVCDVER | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 237 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 238 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 239 | 一致 | ACSEQ | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 240 | 一致 | ACGRPID | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 241 | 一致 | ACPARMCD | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 242 | 一致 | ACPARM | 一致 | 一致 | 一致 | - | 一致 | Role 补括注 |
| AC | 243 | 一致 | ACVAL | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 244 | 一致 | ACVALU | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 245 | 一致 | ACVALNF | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 246 | 一致 | ACVALCD | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 247 | 一致 | ACVCDREF | 一致 | 一致 | 一致 | - | 一致 | - |
| AC | 248 | 一致 | ACVCDVER | 一致 | 一致 | 一致 | - | 一致 | - |
| DI | 269 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| DI | 270 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| DI | 271 | 一致 | SPDEVID | 一致 | 一致 | 一致 | - | 一致 | - |
| DI | 272 | 一致 | DISEQ | 一致 | 一致 | 一致 | - | 一致 | - |
| DI | 273 | 一致 | DIPARMCD | 一致 | 一致 | 一致 | - | 一致 | - |
| DI | 274 | 一致 | DIPARM | 一致 | 一致 | 一致 | - | 一致 | - |
| DI | 275 | 一致 | DIVAL | 一致 | 一致 | 一致 | - | 一致 | - |
| OI | 307 | 一致 | STUDYID | 一致 | 一致 | 一致 | - | 一致 | - |
| OI | 308 | 一致 | DOMAIN | 一致 | 一致 | 一致 | - | 一致 | - |
| OI | 309 | 一致 | NHOID | 一致 | 一致 | 一致 | - | 一致 | - |
| OI | 310 | 一致 | OISEQ | 一致 | 一致 | 一致 | - | 一致 | - |
| OI | 311 | 一致 | OIPARMCD | 一致 | 一致 | 一致 | - | 一致 | - |
| OI | 312 | 一致 | OIPARM | 一致 | 一致 | 一致 | - | 一致 | - |
| OI | 313 | 一致 | OIVAL | 一致 | 一致 | 一致 | - | 一致 | - |

### 结论
PASS. 无 CONDITIONAL 修正项; L-1/L-2 已在 O35 / T4 登记, L-3 可选.
