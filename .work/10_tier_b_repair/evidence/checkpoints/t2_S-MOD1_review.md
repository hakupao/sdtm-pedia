# T2S S-MOD1 review (model/01 + model/03 + model/04, 源 SDTM v2.0 p4-10 / p40-49 / p50)

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: CONDITIONAL** — 内容层面全部通过 (叙述双向全扫 0 缺 0 无出处; 106 行 530 核心格独立 layout 解析 + 渲染逐格 0 实差; Mermaid 与 PDF 图边/方向/配色一致; D-1..D-28 删除、S-1..S-8 结构、C-1..C-7 D2、T-1 逐条签字成立). 唯一修正项: model/03 SE 表 D6 列说明措辞 "most cells" 不属实 (MEDIUM, 1 行可执行修正, 见 F-1).

- 审查对象: 工作树 md5 model/01 `0a4855b8fd85e1c44974c1266b9362ec` (209 行) / model/03 `a7ee1b7a9a129d70e97d7178d2f5c7c2` (222 行) / model/04 `d2069187643d961bbde102a1b3aa39ad` (44 行) = writer attempt 1 delta 终态. 基线 `git show HEAD:<file>` (存 `$S/base_*.md`). `git diff HEAD --stat` 中其余 18 个 KB 文件 (model/05, domains/*) 为他批, 不计; narrow_files 空 → 授权范围 OK.
- scratch `$S` = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-MOD1_reviewer/`
- 独立方法 (不用 writer 的 bbox/tbl.py/cmp.py/atoms/celltab): `pdftotext -layout` (`$S/l01.txt` p4-10, `$S/l03.txt` p40-49, `$S/l04.txt` p50); 叙述 `$S/prose_scan.py` (PDF 行→KB) + `$S/rscan.py` (KB 行→PDF); 表 `$S/laycols2.py` (按每段表头行列起点逐词归列; 修正两行表头 "Variable/Label" 与段落行止表); 渲染 `pdftoppm -r 110` p9 / p40-49, `-r 130` p50, `-r 160` p8 全部目视.

### 页范围复核 (O20)
| 单元 | 结论 | 依据 |
|---|---|---|
| model/01 | p4-10 | p4 首行 `1 Introduction`; p10 §2.2 止于页中; p11 首行 `3 Study Subject Data` |
| model/03 | p40-49 | p39 末 = §3.1.5 --PDUR 行; p40 首 `3.2 Special-purpose Domains`; p49 SM 表后空白 |
| model/04 | p50 | p50 全页 §4; p51 首 `5 Study-level Data` |

### 命令与结果 (repo 根, 可复跑)
| 命令 | 结果 |
|---|---|
| `python3 -I $S/prose_scan.py $S/l01.txt knowledge_base/model/01_concepts_and_terms.md` | `HIT 217 MISS 1`; MISS = p6 "It is still listed in Section 3, Associated Persons Data." (T-1, KB 写 Section 4); 对 base → `HIT 208 MISS 10` |
| 同上 model/03 (`$S/l03.txt`) | `HIT 40 MISS 0` (base `HIT 6 MISS 34`) |
| 同上 model/04 (`$S/l04.txt`) | `HIT 16 MISS 0` (base `HIT 4 MISS 12`) |
| `python3 -I $S/rscan.py $S/l01.txt knowledge_base/model/01_concepts_and_terms.md` (全量, 未截断) | NOPDF = :1 H1 / :3 Source / :77 :106 :114 :158 :191 (PDF 折行连字符 "-\n-BEATNO" "--\nMETHOD" "Special-\npurpose" "data-\nexchange" 与 `\f` 换页; 去折行/去 `\f` 后复核 5 行均逐字命中) / :94 T-1 / :124 D6 / :156 :170 KB 导航 H3 / :180-185 D6 / Mermaid 块 |
| 同上 model/03 | NOPDF = H1/Source/`## Overview`/5 个 `### Variables (N variables)`/`### Key Reference Date Variables` + 10 行 D6 (:15 :21 :66 :85 :119 :125 :151 :176 :203 :209); 其余 HIT 26 |
| 同上 model/04 | NOPDF = H1/Source/`## Overview`/`### AP Domain Rules`/`### Key Principles`/`### Variables Used in…` + D6 2 块 (:17-19, :27-29) + :21 交叉引用 |
| `cat l03 l04 > l0304; python3 -I $S/laycols2.py $S/l0304.txt $S/kb0304.md $S/laycols.json` | `pdf rows 106 kb rows 106` / `cells 530 diffs 5`: AGEU Role `AGE; AGETXT`→`AGE/AGETXT` (R1/model 约定) + DMDY / IDVAR 的 Label/Role 各吸入下页续表头 "Name Label"/"Qualified" (解析器伪差, 渲染 p44 确认 KB 正确) → **实差 0** |
| 同上对 `$S/base0304.md` | `kb rows 102` (AP 旧表无 # 列不入计) / 实差 2 = RPATHCD Label、SVREASOC Label (= V-1/V-2, 改后消失) |
| `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` | exit 0; `PDF tables parsed: 0 … KB tables: 8; status: {'UNPARSEABLE': 8}; cells compared: 0` GREEN — **0 格空比较, 无证明力** |
| `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline … --regress-out $S/fp_regress.jsonl` | RESULT RED, regress 72 (与 S-MOD3 时同数, 全为他批 ig34 页); sv20 p4-10 / p40-50 回归 0 — sv20 节原子不在 fp 口径内, **无证明力** |
| `grep -rnE "0[34]_(special_purpose_domains\|associated_persons)(\.md)?#" knowledge_base web/src tools docs` | 0 命中 (D-23..D-28 删标题无断链); 锚点 slug grep 同范围 0 |
| `python3 tools/check_links.py 2>&1 \| grep "live docs"` | `broken relative links: 18668 (live docs: 42)` |

### 逐页双向全扫 (reviewer 自计)
| 页 | PDF→KB (叙述行 HIT/MISS) | KB→PDF 无出处 | 表 (逐格) | 备注 |
|---|---|---|---|---|
| 4 | 全 HIT | 0 | — | 6 IG + 3 项列表 + URL 逐字 |
| 5 | 全 HIT | 0 | — | 11 列名列表 |
| 6 | 1 MISS = T-1 | :94 T-1 | — | 其余逐字 |
| 7 | 全 HIT | 0 | — | |
| 8 | 全 HIT; 图 → Mermaid | :124 D6 | 图逐边 (下) | 斜体 "observations"/"domain" KB 为粗体: 既有强调, S-CH1 不计 |
| 9 | 全 HIT (含 5 项子类列表恢复 "X Qualifiers," 起句与 ";"/"; and") | :156 :170 导航, :180-185 D6 | p9 为列表 (渲染 r-09) → census :176 表关闭 | |
| 10 | 全 HIT | 0 | — | |
| 40 | 全 HIT (§3.2 / §3.2.1 标题 + 段落 + 表题) | :15 :21 D6 | DM 1-6 逐格一致 (渲染 r-40) | |
| 41 | — | :66 D6 (汇总表) | DM 7-13 一致 (r-41) | |
| 42 | — | — | DM 14-26 一致 (r-42); AGEU Qualified "AGE; AGETXT" = R1 写法 | |
| 43 | — | — | DM 27-37 一致 (r-43); RPATHCD Label "Planned Repro Path Code" ✓ | |
| 44 | 全 HIT (§3.2.2 段 + "See the implementation guides…" + 表题) | :85 D6 | DM 38 / CO 1-8 一致 (r-44) | |
| 45 | 全 HIT (§3.2.3 + §3.2.3.1 段) | :119 D6 | CO 9-15 一致 (r-45) | |
| 46 | 全 HIT (SE 表题 + §3.2.3.2 段) | :125 D6 (F-1) | SE 1-13 一致 (r-46) | |
| 47 | 全 HIT (SJ 表题 + §3.2.3.3 段) | :151 D6 | SJ 1-10 一致 (r-47) | PDF §3.2.3.2 无 "See the implementation guides" 句, KB 亦无 ✓ |
| 48 | 全 HIT (SV 表题) | :176 D6 | SV 1-16 一致 (r-48); SVREASOC Label "Reason for Occur Value" ✓ | |
| 49 | 全 HIT (§3.2.3.4 + 2 句 + 表题) | :203 :209 D6 | SM 1-10 一致 (r-49) | |
| 50 | 全 HIT (标题 + 引言 + 3 项列表 + SDTMIG-AP 段含 URL + 表前段 + 表题 + 末段) | D6 2 块 + :21 交叉引用 | AP 1-4 (#/Var/Label/Type/Role + Notes 逐字) 一致 (r-50) | |

### 逐格表 (核心 5 格 #/Variable/Label/Type/Role; 来源 `$S/laycols.json` + 渲染目视)
| 表 | 行 | 结果 |
|---|---|---|
| DM | 1-38 | 190 格一致 (AGEU Role R1 写法; RPATHCD Label 已改正) |
| CO | 1-15 | 75 格一致 |
| SE | 1-13 | 65 格一致 |
| SJ | 1-10 | 50 格一致 |
| SV | 1-16 | 80 格一致 (SVREASOC Label 已改正) |
| SM | 1-10 | 50 格一致 |
| AP | 1-4 | 20 格一致; Notes 4 格 = PDF Notes 逐字 (含 RSUBJID 第 3 句, SREL 3 句) |
| Key Reference Date (KB 汇总) | 8 | Description 8 格 = PDF DM Label 逐字; Typical Use: RFENDTC / RFPENDTC = PDF Notes 逐字; RFSTDTC (p40 Notes + p44 DMDY Notes) / RFXSTDTC / RFXENDTC (p41 Definition) / RFCSTDTC / RFCENDTC (p41 Notes) / RFICDTC (p41 Definition) 不矛盾 → D6 (P-6) 成立 |

Notes 列非空格 (50 格) 逐格对 PDF Format / Usage / Notes / Examples (`$S/laycols.json` 全量打印):
- 逐字或简写 PDF: DM DOMAIN/SUBJID/RFSTDTC/RFENDTC/RFICDTC/RFPENDTC/DTHDTC/DTHFL/INVID/INVNAM/AGE/RACE/ETHNIC/SPECIES/STRAIN/SBSTRAIN/ACTARMCD/ACTARM/ARMNRS/RPATHCD/COUNTRY; SE DOMAIN/SEUPDES; SJ 全 8 格; SV DOMAIN; SM DOMAIN/MIDS; AP 4 格.
- = PDF Variable C-code: SE TAETORD C83438 / EPOCH C71738 (r-46 确认).
- KB 自写不矛盾 (D6 下): DM AGETXT / AGEU / SEX / ARMCD / SETCD (M-2 主控已裁); SE ETCD; SM MIDSTYPE (TM p58 Topic = MIDSTYPE).

### D2 改格 C-1..C-7 签字
| # | 旧 KB | 新值 | 判 |
|---|---|---|---|
| C-1 / C-6 RFENDTC | "Usually date of last dose" | PDF Notes 首句 | ✓ PDF: "Usually equivalent to … ended the trial"; last exposure 仅 "Often" 之一 → 旧值矛盾 |
| C-2 AGE | "Numeric age at RFSTDTC" | PDF Notes 逐字 | ✓ PDF Def "at a specific point in time defined for the trial"; 旧值把时点限定为 RFSTDTC (偏义). 新值逐字, 无风险 (主控 M-5 已裁保留) |
| C-3 ARMNRS | "When arm assignment is not possible" | PDF Notes 首句 | ✓ PDF 例 "NOT TREATED"/"UNPLANNED TREATMENT" 为已分配情形 → 矛盾 |
| C-5 MIDS | "Unique name linking to TM" | PDF Notes 逐字 | ✓ p58 TM "One Record per Disease Milestone Type", Topic = MIDSTYPE, 无 MIDS |
| C-7 RFPENDTC (汇总表) | "Completion/withdrawal date" | PDF Notes 逐字 | ✓ PDF Def "last contact with or information about a subject" ≠ completion/withdrawal (偏义); 新值逐字 |
| C-4 | "Not for human clinical trials" ×4 | "Not in human clinical trials" | ✓ = PDF Usage 原词 (p42-43) |
| V-1 / V-2 | RPATHCD / SVREASOC Label | PDF Label | ✓ r-43 / r-48 |

### Concept Map Mermaid (渲染 p8 160 dpi `$S/p-08.png`)
| 元素 | PDF | KB 改后 | 判 |
|---|---|---|---|
| SDTM includes → | Subject / AP / Study-Level / Relationship (4) | 同 | ✓ |
| Subject Data include → | GOC + Special Purpose | 同 | ✓ |
| AP Data include → | GOC + Special Purpose (2 箭头汇入) | `AP --> GOC/SPD` | ✓ |
| Study-Level include → | Trial Design Model + Study Reference Datasets | 同 | ✓ |
| GOC include → | Events / Interventions / Findings | 同 | ✓ |
| subtype of | 箭头 Findings About → Findings | `FA -->|subtype of| FI` | ✓ 方向正确 |
| 绿 (individually specified) | Relationship / Special Purpose / Trial Design / Study Reference | `:::individual` 同 4 个 | ✓ |
| 黄 (extensible) | Events / Interventions / Findings / Findings About | `:::extensible` 同 4 个 | ✓ |
| 灰 (无图例) | SDTM / Subject / AP / Study-Level / GOC | 无 class | ✓ |
| 节点文字 | 13 个 | 13 个逐字 (空格已恢复) | ✓ |
| 图例 | 2 条 | :124 D6 内逐字 | ✓ |

### 删除清单签字 (D-1..D-28)
| # | 判 | 依据 |
|---|---|---|
| D-1 / D-2 | ✓ | 旧 Key 说 "Green filled box = Extensible" 与 PDF (绿 = individually specified) 矛盾 → D2; 图例现由 :124 承载 |
| D-3 / D-4 | ✓ | 子类表→ PDF 列表 (p9 列表, 规则 3); Examples 列 5 格原样迁入 :180-185 D6, 逐个对 model/02 Role 列不矛盾 (--CAT/--SCAT Grouping; --ORRES/--STRESC/--STRESN Result; --MODIFY/--DECOD/--TEST Synonym; --REASND/--SLIFE/--BLFL/--POS/--LOC/--SPEC/--NAM Record; --ORRESU/--ORNRHI/--ORNRLO/--DOSU Variable) |
| D-5 | ✓ | 旧 DM 首 2 句为 PDF 首 2 句的改写; PDF 原句已逐字在 :13, 无独有信息 |
| D-6 | ✓ | 旧 SE 段 = PDF 段改写 (缺 "(see Section 5.1.1, …)"); PDF 段 :115 逐字; "(blocks of time)" → :119 D6 |
| D-7 / D-9 / D-12 / D-14 | ✓ | PDF 表题含 "One Record per…" (S-MOD2 裁定); D-12 旧 "actual or planned visit" 还与 PDF 表题 "per Subject Visit" 不符 |
| D-8 / D-11 / D-13 | ✓ | R2 残留改写, PDF 段已逐字 (:145 / :168 / :199); D-13 例列表 → :203 D6 |
| D-10 | ✓ | "Not for use with human clinical trials" 由 :145 PDF 括注 "(not for use with human clinical trials)" 逐字承载 |
| D-15 | ✓ | "AP rules:" → PDF "AP rules, including:" (:9) |
| D-16 | ✓ | p6 §1.4 内容的跨文件改写副本 (且旧 "Section 3" 无 T-1 处理), 按 "跨文件重复留 PDF 所属节" 留 model/01:94, model/04:21 一行交叉引用 (锚点 `#changes-to-datasets-and-variables` 存在于 model/01 `### Changes to Datasets and Variables`, check_links 42 不升) |
| D-17 | ✓ | RSUBJID/RDEVID/SREL 释义 = 同文件 PDF 表 Notes 的重复, 表内现逐字 |
| D-18 | ✓ | "conform to the same general observation class models (Interventions, Events, Findings)" 与 PDF "either general observation class structures or special-purpose domain structures" 矛盾 → D2 |
| D-19 | ✓ | R2 残留, PDF SDTMIG-AP 段 :25 逐字 |
| D-20 | ✓ | "includes all variables from the general observation classes" 与 PDF (表只列 4 个附加标识变量) 矛盾 → D2; PDF 段 :33 逐字 |
| D-21 / D-22 | ✓ | Notes 单列恢复 PDF 逐字 / C-格见上 |
| D-23..D-28 | ✓ | 6 个 KB H2 (`## Demographics (DM)` / `## Comments (CO)` / `## Subject Elements (SE)` / `## Subject Repro Stages` / `## Subject Visits (SV)` / `## Subject Disease Milestones (SM)`) 与紧邻 PDF 编号标题同义; 入站锚点 0 (上表 grep) → S-TDM 条成立. K-1 (`## Overview` ×2) / K-2 (`### AP Domain Rules` / `### Key Principles`) 非同义导航, 按主控裁定保留 |

### 结构改动签字 (S-1..S-8)
- S-1 子类表→列表 ✓ (p9 为列表); S-2 Mermaid ✓; S-3 编号标题 ✓ (经 delta 后层级: `## 3.2.1` / `## 3.2.2` / `## 3.2.3` > `### 3.2.3.1-4`, `## Overview` > `### 3.2` — 与 PDF 层级相容; model/04 `## Overview` > `### 4 …` 同 S-MOD3 先例); S-4 `## 3.2.3` 有正文父节 ✓ (S-INT); S-5 / S-6 Structure 处理 ✓; S-7 model/04 按 PDF 顺序 ✓ (引言 → 3 项列表 → [KB 导航 + D6 + 交叉引用] → SDTMIG-AP 段 → [D6] → 表前段 → 表题 → 表 → 末段, PDF 句序未被打乱); S-8 AP 表 +# ✓ (R1 5 列 floor).

### D6 清单签字 (措辞属实 + 不矛盾)
| # | 位置 | 判 |
|---|---|---|
| M-2 | 01:124 | ✓ 图例逐字, 页码 p8 正确 |
| M-4 | 01:180-185 | ✓ 不矛盾 (见 D-3/D-4) |
| P-4 | 03:15 DM Structure | ✓ PDF 表题无结构句 |
| P-5 | 03:21 DM Notes 列 | ✓ 28 个非空格中 23 个引/简写 PDF Format/Notes/Usage, 5 个 KB 自写 (AGETXT/AGEU/SEX/ARMCD/SETCD) → "most … some cells add KB wording or example values" 属实 |
| P-6 | 03:66 汇总表 | ✓ 见逐格表 |
| P-8 | 03:85 CO Structure + 释义 | ✓ 不矛盾 |
| P-12 | 03:119 "Elements are blocks of time." | ✓ 不矛盾 |
| **P-13** | **03:125 SE Notes 列** | **✗ 措辞不属实 (F-1)**: 非空 5 格 = DOMAIN / SEUPDES (引 PDF Notes) + TAETORD / EPOCH (C-code) + ETCD (KB), "most cells quote or condense the PDF Notes column" 实为 2/5 |
| P-15 | 03:151 SJ | ✓ DOMAIN 简写 Notes, 其余 7 个非空格 = PDF Usage 逐字 |
| P-17 | 03:176 SV | ✓ 仅 DOMAIN 非空 |
| P-19 | 03:203 SM 例 | ✓ 不矛盾 (PDF 例 "HYPOGLYCEMIC EVENT" 为类型例) |
| P-20 | 03:209 SM | ✓ DOMAIN/MIDS 引 Notes, MIDSTYPE KB |
| A-4 | 04:17-19 | ✓ 不矛盾 (PDF: AP 为前缀; APID 必有) |
| A-7 | 04:27-29 | ✓ 不矛盾 (PDF: 其他通用假设适用 AP) |

### PDF_TYPO
- T-1 (沿用 B-model01) model/01:94 PDF p6 "still listed in Section 3, Associated Persons Data" → KB "Section 4": ✓ PDF 自身可定 — §3 = Study Subject Data (p11 标题), "Associated Persons Data" = §4 (p50 标题; p5 两处 "Section 4, Associated Persons Data"; p8 "described in Section 4, Associated Persons Data"). 按 PDF_TYPO 取舍规则写正确值并登记, 成立.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| F-1 (MEDIUM, 置信 HIGH) | D6 措辞属实 (S-MOD2 review 教训) | model/03:125 "most cells quote or condense the PDF Notes column" — SE Notes 列非空 5 格中只有 DOMAIN/SEUPDES 来自 PDF Notes | p46: DOMAIN "2-character abbreviation, which must be "SE""; SEUPDES "Used only if ETCD has the value of "UNPLAN"" |
| O-1 (LOW, 不要求修) | 观察 | M-4 例块 "--MODIFY, --DECOD (for --TRT or --TERM)" 未提 --MODIFY 在 Findings 中限定 --ORRES (p9 正文已述), 属不完整非矛盾; "--DOSU (Variable Qualifier of --DOSE)" 同 (model/02 为 --DOSE/--DOSTXT/--DOSTOT). 既有内容原样迁入, D6 下可接受 | model/02 Role 列 |
| O-2 (LOW, 不要求修) | 观察 | model/04 `### AP Domain Rules` 下现仅 D6 + 交叉引用 (主控 K-2 已裁保留) | — |

### CONDITIONAL 修正清单 (writer attempt 2, 仅 1 项)
1. model/03:125 改为: `> KB note (not in SDTM v2.0): The Notes column is KB-written: the DOMAIN and SEUPDES cells quote or condense the PDF Notes column, the TAETORD and EPOCH cells give the PDF Variable C-code, and the ETCD cell adds KB wording not given in SDTM v2.0.` (其余不动). 改后回 reviewer 复审 delta (仅此行 + md5).

## attempt 2 复审 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** — F-1 已关闭.
- model/03 md5 `df5c9199aa3f4a754cfe7bbc855be7c7` (222 行). 对 attempt 1 审时副本 (`$S/a1_03.md`, md5 `a7ee1b7a…` = 当时工作树) 执行 `diff $S/a1_03.md knowledge_base/model/03_special_purpose_domains.md` → 仅 `125c125`, 1 删 1 增.
- :125 逐字等于 attempt 1 修正清单给出的文字 (Python 字符串全等 True); 属实: SE Notes 列非空 5 格 = DOMAIN / SEUPDES (PDF Notes, p46) + TAETORD C83438 / EPOCH C71738 (PDF Variable C-code) + ETCD (KB 自写).
- model/01 `0a4855b8…` / model/04 `d2069187…` md5 与 attempt 1 审时一致, 未改.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42`.
