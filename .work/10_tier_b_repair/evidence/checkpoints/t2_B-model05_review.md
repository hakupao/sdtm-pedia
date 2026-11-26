# T2 B-model05 — reviewer checkpoint

## attempt 1 (审 writer attempt 1+2 终态)

- agent: oh-my-claudecode:code-reviewer (opus), 与 writer 不同 invocation. KB 只读.
- 对象: `knowledge_base/model/05_study_level_data.md` md5 `b01d929e0c3718c8d176d90f7c4c598d` (= writer attempt 2 终态); `git diff HEAD` 本文件 +111/-74.
- 源: `source/cdisc/SDTM_v2.0.pdf` p51-63 (§5 起 p51, p64 为 §6) — layout 文本 `work/pdf_pages/sv20_p0051-0063.txt` + 渲染图 110dpi p53/p58/p59/p60/p62/p63 (scratch).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-model05_reviewer/`

### verdict: **PASS**

无 HIGH/MEDIUM 问题; 2 条 LOW 仅建议 (不阻断).

### 命令 (repo 根; S = 上述 scratch)
| 命令 | exit / 关键输出 |
|---|---|
| `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` | exit 0; `KB tables: 13; status: {'UNPARSEABLE': 13}; PDF_ONLY: 0; diffs: 0` GREEN (全 unparseable → 人工核见下) |
| `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` | RED, 51 条回退全为 ig34 (他批); `grep -c sv20 $S/fp_regress.jsonl` = 0; `grep -c 05_study $S/fp_regress.jsonl` = 0; baseline 命中 model/05 的 15 个原子 (13 sv20 + ig34_p0441_a004/a005) verdict 全不变 |
| `python3 -I $S/scan.py` (KB→PDF: KB 每个非表/非代码句, 归一化后为 PDF p51-63 子串) | NOSRC 仅: :1 文件标题 / :3 Source 行 / :5 `## Overview` / :11 `## 5.1` / 13 个域节 `###` 标题 (O35) + 6 条 D6 (:72 :213 :261 :279 :299 :317) |
| `python3 -I $S/rscan.py` (PDF→KB: p51-63 每条非表格行, 归一化后为 KB 子串) | MISS 仅 15 条节号标题 (5 / 5.1 / 5.1.1.1 / 5.1.1.2 / 5.1.2 / 5.1.3.1 / 5.1.3.2 / 5.1.4.1-3 / 5.1.5-5.1.7 / 5.2.1 / 5.2.2) = O35 既有标题, 主控裁不改 |
| pdf_atoms.jsonl p51-63 `norm(verbatim) in norm(KB)` (fp_match.norm) | SENTENCE 42/42、LIST_ITEM 12/12、NOTE 3/3 全命中; HEADING 17 命中 / 15 未中 (同上 O35); FIGURE 2 = Mermaid 图 (人工核); TABLE_ROW/HEADER 为 12 列原子, 另核 |
| 表格原子 5 列独立核 (TABLE_ROW `#/Variable/Label/Type/Role(+Variable(s) Qualified 括注)` 按表序对 KB 13 张表) | `13 13` / `bad 0` (行数、5 列全一致; Role 括注有/无两种写法均接受, O35-c) |
| `python3 tools/check_links.py 2>&1 \| grep "live docs"` | `broken relative links: 18668 (live docs: 42)` = 基线 |

### 5 atoms
| atom | KB 行 | 判定 |
|---|---|---|
| sv20_p0056_a019 / a020 / a022 | :160 | 逐字, 位于 TD 节 (R1-TD), 与 a021 同段; PDF p56 该段为独立段 (前行短行收尾) ✓ |
| sv20_p0051_a008 | :17 | 逐字含 "(animal developmental and reproductive toxicology studies; …)" ✓ |
| sv20_p0051_a013 | :23 | 逐字含 "(e.g., for study arms, visits, and eligibility criteria)" ✓ |

### 新增/恢复句 (14 条旧 IE R3 + R2 恢复) — 全部逐字
p52 a009 (:49 独立段 ✓)、p53 a006-a009 (:68/:70)、p54 a004/a005 (:89)、p55 a013/a015 (:130/:134)、p56 a003-a005 (:140)、p56 a021 (:160)、p58 a010 (:192); R2 恢复 p51 a004/a011/a014/a015/a017/a019、p52 a006/a010、p54 a001/a003/a008/a009/a020、p55 a001/a014/a016/a017、p56 a002/a006/a018、p57 a001/a013、p58 a001/a009/a011、p59 a004-a006、p60 a004/a005、p61 a002-a005/a007/a009、p62 a003-a005 — 双向扫描逐行命中, 无扩写. `*taxa*` 仅首处斜体, 与渲染 p62 一致.

### 新组标题 (结构行签字)
| KB 行 | 内容 | PDF | 签字 |
|---|---|---|---|
| :25 | `### 5.1.1 Trial Arms and Trial Elements` | p51 原标题 | ✓ |
| :85 | `### 5.1.3 Trial Repro Stages and Trial Repro Paths` | p54 原标题 | ✓ |
| :130 | `### 5.1.4 Trial Planned Data Collection` | p55 原标题 | ✓ |
| :33 :51 :70 :97 :115 :142 :162 :180 :194 :211 :233 :265 :303 | 13 个粗体表题 | 各页表题逐字 (— 照 PDF) | ✓ |
| :277 :315 | Concept Map 题注 (". " 照 PDF) | p62 / p63 | ✓ |
| 表头/分隔线 13 组 | 未改 | — | ✓ |
既有标题文字/层级未改 (O35-a, 主控裁定不作为本批问题).

### 删除清单逐条确认
| # | 删除内容 | 确认 |
|---|---|---|
| D-1 | :17 旧列表项缺括注 | R2 残留, PDF 原文在 :17 ✓ |
| D-2 | :23 旧句缺 e.g. 括注 | ✓ (:23) |
| D-3 | "(TDM)" | PDF p51 无此缩写 ✓ |
| D-4 | TE "Describes the basic building blocks …" | KB 改写, 原句 :31 在 ✓ |
| D-5/6/9/10/13/15/17 | TE/TA/TT/TP/TD/TM/TI `**Structure:**` | 与 PDF 表题等价, 表题逐字在 :33/:51/:97/:115/:162/:180/:194 ✓ (主控 #7) |
| D-12 | TV "One record per planned Visit per Arm" | 把 PDF p56 条件情形 ("In the case where visits vary for each arm") 写成无条件结构, 与 PDF 矛盾 → 删正确 ✓ |
| D-8 / D-19 | TX / TS Structure | attempt 2 撤回, 改为 D6 (:72 / :213) ✓ |
| D-7 | TX "… pooled analysis groups" | PDF 无, 原句 :68 在 ✓ |
| D-11 / D-14 / D-16 / D-18 | TV / TM / TI / TS 改写句 | 原句 :140 / :178 / :192 / :209 在 ✓ |
| D-20 | AC Structure | 与 PDF 表题逐字相同, 表题 :233 在 ✓ |
| D-21 | 5.2 改写句 + 行内列举 | 原句 + 2 项列表 :254-257 ✓ |
| D-22 | DI "Used to identify the devices…" | 原句 :263 ✓ |
| D-23 | OI "…such as bacteria and viruses" + "The taxa used … needs of the study." | PDF 无 "bacteria and viruses"; 原句 :301 ✓ |
git diff `^-` 另含 `### Trial Reproductive Stages (TT)` / `### Device Identifiers (DI)` / `### Non-host Organism Identifiers (OI)`: diff 对齐假象, 原文在 :91/:259/:297 未改 ✓.

### D6 逐条确认 (措辞 `> KB note (not in SDTM v2.0):` ✓)
| KB 行 | 内容 | PDF 依据 | 判定 |
|---|---|---|---|
| :72 | TX "One record per Trial Set parameter per Trial Set" | p53 表题 "One Record per Trial Set Parameter"; SETCD Identifier "trial set for which parameters are being submitted" | 不矛盾 ✓ |
| :213 | TS "One record per trial summary parameter value" | p59 "1 record for each trial summary characteristic"; TSSEQ/TSGRPID Identifier | 不矛盾 (附加粒度) ✓ |
| :261 | DI "One record per device attribute per device" | p61 DISEQ "uniqueness within a parameter within a device (SPDEVID)" | 不矛盾 ✓ |
| :299 | OI "One record per taxon per non-host organism" | p62 OISEQ "within a parameter within an organism (NHOID)" | 不矛盾 ✓ |
| :279 / :317 | Mermaid rendering 注 | 见下 | ✓ |

### Mermaid vs PDF 图 (渲染 p62 / p63 人工核)
| 图 | 节点 | 边 | 判定 |
|---|---|---|---|
| DI (p62) | Study / Device / Identifying Characteristic / identifier (SPDEVID) / parameter (DIPARM, DIPARMCD) / value (DIVAL) | Study-involves→Device; Device-has one or more→IC; Device-has→identifier; IC-is represented using→parameter; parameter-has→value | 与图一致 ✓ |
| OI (p63) | Study / Non-Host Organism / Taxon / identifier (NHOID) / parameter (OIPARM, OIPARMCD) / value (OIVAL) | 同构 | 与图一致 ✓ |
位置: DI 图在 DI 表后 (p61 表 → p62 图), OI 图在 OI 表后 (p62 表 → p63 图) ✓.

### 人工逐格 (改动的 11 个 Label 格, 对渲染图)
| 表 | 变量 | KB Label | 渲染 PDF | 判定 |
|---|---|---|---|---|
| TX p53 | TXPARM | Trial Set Parameter | Trial Set Parameter | 一致 |
| TX p53 | TXVAL | Trial Set Parameter Value | Trial Set Parameter Value | 一致 |
| TI p58 | IETESTCD | Inclusion/Exclusion Criterion Short Name | 同 | 一致 |
| TI p58 | IETEST | Inclusion/Exclusion Criterion | 同 | 一致 |
| TI p58 | IECAT | Inclusion/Exclusion Category | 同 | 一致 |
| TI p58 | IESCAT | Inclusion/Exclusion Subcategory | 同 | 一致 |
| TI p59 | TIRL | Inclusion/Exclusion Criterion Rule | 同 | 一致 |
| TS p59 | TSPARM | Trial Summary Parameter | 同 | 一致 |
| TS p59 | TSVCDREF | Name of the Reference Terminology | 同 | 一致 |
| TS p60 | TSVCDVER | Version of the Reference Terminology | 同 | 一致 |
| OI p62 | NHOID | Non-Host Organism Identifier | 同 (大写 H) | 一致 |
触碰 4 张表 (TX/TI/TS/OI) 其余全部格 (#/Variable/Type/Role) 对渲染图逐行: 一致. AC (p60) / TM (p58) 渲染图顺带核: 一致. 未触碰 TE/TA/TT/TP/TV/TD/DI 对 layout 文本 + 原子 5 列核: 一致 (bad 0).

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| :261 / :299 vs :72 / :213 | 一致性 (LOW, 建议) | DI/OI 的 D6 Structure 注在节标题下、PDF 引言之前; TX/TS 的在 PDF 表题与表之间. 位置不统一, 且 TX/TS 把 PDF 表题与表隔开 | 无 PDF 矛盾; 可选统一到表题前或引言后 |
| :213 | D6 内容 (LOW, 建议) | "per … parameter value" 与 PDF 表题 "per Trial Summary Parameter" 字面不同, 读者可能误以为与 PDF 冲突; 主控已裁保留 | p59 "1 record for each trial summary characteristic" |

### 范围 / 副作用
- 本批只改 `knowledge_base/model/05_study_level_data.md`; 工作树其他 KB 改动 (DM/RS/TS/model06) 属他批.
- 标题/锚点未改 (新增 3 个组标题除外); 全仓无 `05_study_level_data` 锚点引用 (writer 已核).
- 主控裁定不改项 (O35: 标题/层级、TT/TP Notes 列、TS Usage Restrictions、Role 括注) 未作为问题.
