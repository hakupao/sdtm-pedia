# T4 加查 ATOM_ERR (S1-R1) 全检 — 包 4 (E64-E83) 结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 新实例, 只读
- 日期时间 (UTC): 2026-11-27T14:11:39Z
- 口径: `.work/10_tier_b_repair/subagent_prompts/t4/t4_atomerr_s1r1_v1.0.md` + `t4_supp_fullcheck_v1.0.md` "背景" / "判定口径"
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`, Read 工具 `pages`): 336, 337, 338, 339, 342, 347, 348, 360, 361, 373, 374, 396, 419; p360 另用 `pdftoppm -r 300` 放大 (输出在 session scratchpad, 不在仓库)
- 用过的命令: `grep` 查 `work/t2_pdf_typo_registry.jsonl` (页 336-419 与 STRNC / 6.4.4. / "a a source" 等 token); `cat -n work/pdf_pages/ig34_p0336..0339.txt`; `grep -n` / `sed -n` 定位 `knowledge_base/domains/{RS,SC,TU,VS,FA,TA,TS}/*.md`; `pdftoppm -r 300 -f 360 -l 360 -png ...`; `date -u +%Y-%m-%dT%H:%M:%SZ`
- 说明: E65-E71 属 §6.3.9.3.2 (RS 临床分类用例 + QRS 共享 assumptions), 包里 KB 指针给的是 `FT/assumptions.md` (FT 副本); 本表 ② 以所属域 `knowledge_base/domains/RS/assumptions.md` (`## QRS Shared Assumptions`, 第 84 行起) 为准, 自行 grep 定位.

## 逐条判定

| # | atom_id | 判定 | ① 原子 vs PDF (差在哪; PDF 文件:行 或 渲染页) | ② KB vs PDF (KB 文件:行) | 说明 |
|---|---|---|---|---|---|
| E64 | ig34_p0337_a003 | HOLDS | 原子 id 标 p337, 但 p337 无此句; 内容实为 p336 CC 3c (`ig34_p0336.txt:34-35`, 渲染 p336). 原子 ">-3" vs PDF ">3"; 原子 "RSORRESRU" vs PDF "RSORRESU"; 原子 "uses a source" vs PDF "uses a a source" | `knowledge_base/domains/RS/assumptions.md:81` 与 PDF 一致, 唯 "a a" 写成 "a" | 涉登记 B-RS T-3: PDF 印 "uses a a source value", KB 为 "uses a source value", handling "KB 写正确值" (重复词). 其余 ">3" / "RSORRESU" 与 PDF 一致 |
| E65 | ig34_p0337_a006 | HOLDS | 原子 "ADAS-Cog" vs PDF "ADAS-COG"; 原子 "al STAIR ASCEND" vs PDF "4 STAIR ASCEND" (`ig34_p0337.txt:3-6`, 渲染 p337) | `knowledge_base/domains/RS/assumptions.md:88` 逐字一致 | 无 |
| E66 | ig34_p0337_a015 | HOLDS | 原子 "numeric "standardized response" are documented" 漏 s; PDF "numeric “standardized responses” are documented" (`ig34_p0337.txt:17-20`, 渲染 p337) | `knowledge_base/domains/RS/assumptions.md:99` 逐字一致 (含弯引号) | 引号弯直差异不计, 判据是漏 s |
| E67 | ig34_p0338_a002 | HOLDS | 原子 "sponsor's case management process reduced to the score"; PDF "sponsor-data management processes related to the score" (`ig34_p0338.txt:1-2`, 渲染 p338) | `knowledge_base/domains/RS/assumptions.md:107` 逐字一致 | 无 |
| E68 | ig34_p0338_a003 | HOLDS | 原子 "their cRF process" vs PDF "eCRF"; 原子 "will not be flagged" vs PDF "not flagged"; 原子漏整句 "When subtotal and total scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y"." 及 "However," (`ig34_p0338.txt:3-7`, 渲染 p338) | `knowledge_base/domains/RS/assumptions.md:108` 逐字一致 | 无 |
| E69 | ig34_p0338_a010 | HOLDS | 原子重复拼接 "If the verbatim item in the study metadata. If the verbatim item text…", "SSORRES", 漏 "see Section 4 of the QRS supplement", "Observation-class Findings"; PDF 见 `ig34_p0338.txt:19-22` (渲染 p338) | `knowledge_base/domains/RS/assumptions.md:118` 逐字一致 | 无 |
| E70 | ig34_p0338_a013 | HOLDS | 原子 "standardized value" vs PDF "values"; "SDTMIG for FT" vs "SDTMIG FT"; "any QRS instruments" vs "any QRS instrument" (`ig34_p0338.txt:28-31`, 渲染 p338) | `knowledge_base/domains/RS/assumptions.md:123` 逐字一致 | 无 |
| E71 | ig34_p0339_a001 | HOLDS | 原子 "may be added to any QRS domain. In general, identifiers should be considered generated observation class qualifiers that are generally not used"; PDF "may be added to a QRS domain, but the following qualifiers would generally not be used"; 原子 "--BODYSYS" vs PDF "--BODSYS" (`ig34_p0339.txt:2-4`, 渲染 p339) | `knowledge_base/domains/RS/assumptions.md:128` 与 PDF 一致, 唯 "--STRNC" 写成 "--STNRC" | 涉登记 B-RS T-6 (RS 副本): PDF 印 "--STRNC", KB 为 "--STNRC", handling "KB 写正确值" (同节 DR 11 与 spec 为 --STNRC) |
| E72 | ig34_p0342_a004 | HOLDS | 表头逐格: 第 10 格原子 "SCORESU", PDF "SCORRESU"; 其余 16 格一致 (`ig34_p0342.txt:9`, 渲染 p342) | `knowledge_base/domains/SC/examples.md:32` 17 格逐格一致 | 无 |
| E73 | ig34_p0347_a003 | HOLDS | 原子 "for use with TULORRES"; PDF "TUORRES" (`ig34_p0347.txt:13-14`, 渲染 p347) | `knowledge_base/domains/TU/assumptions.md:34` 逐字一致 (该行前两句) | 无 |
| E74 | ig34_p0348_a010 | HOLDS | 原子 "these TUTEST will be included"; PDF "these TUTESTs will be included" (`ig34_p0348.txt:38-41`, 渲染 p348) | `knowledge_base/domains/TU/assumptions.md:76` 逐字一致 | 无 |
| E75 | ig34_p0360_a021 | HOLDS | 逐格: 原子 VSDY 空, PDF VSDY "1"; 原子 VSTPT "BASELINE", PDF VSTPT "BASELINE 1" (折行); 其余 23 格一致 (`ig34_p0360.txt:35-36`, 渲染 p360 放大) | `knowledge_base/domains/VS/examples.md:17` 25 格逐格一致 (VSDY 1, VSTPT BASELINE 1, VSTPTNUM 1) | 无 |
| E76 | ig34_p0360_a022 | HOLDS | 逐格: 原子 VSDY 空, PDF "1"; 原子 VSTPT "BASELINE", PDF "BASELINE 2"; 其余一致 (`ig34_p0360.txt:37-38`, 渲染 p360 放大) | `knowledge_base/domains/VS/examples.md:18` 逐格一致 (VSLOBXFL Y, VSDTC 1999-06-19T09:00, VSTPTNUM 2) | 无 |
| E77 | ig34_p0360_a023 | HOLDS | 逐格: 原子 VSDY 空, PDF "1"; 原子 VSTPT "BASELINE", PDF "BASELINE 1"; 其余一致 (`ig34_p0360.txt:39-40`, 渲染 p360 放大) | `knowledge_base/domains/VS/examples.md:19` 逐格一致 (DIABP, 44, 08:45, VSTPTNUM 1) | 无 |
| E78 | ig34_p0360_a024 | HOLDS | 逐格: 原子 VSDY 空, PDF "1"; 原子 VSTPT "BASELINE", PDF "BASELINE 2"; 其余一致 (`ig34_p0360.txt:41-42`, 渲染 p360 放大) | `knowledge_base/domains/VS/examples.md:20` 逐格一致 (DIABP, 48, Y, 09:00, VSTPTNUM 2) | 无 |
| E79 | ig34_p0361_a016 | HOLDS | 原子 "use an evaluation interval, the timing variables"; PDF "use an evaluation interval, so the timing variables" (`ig34_p0361.txt:36-39`, 渲染 p361) | `knowledge_base/domains/FA/assumptions.md:15` 与 PDF 一致, 唯 "Section 6.4.4.," 写成 "Section 6.4.4," | 涉登记 B-FA T-2: PDF 印 "Section 6.4.4.," (多余句点), KB 为 "Section 6.4.4,", handling "KB 写正确值". 其余含 "so" 逐字一致 |
| E80 | ig34_p0373_a021 | HOLDS | 表头逐格: 末格原子 "FAEVINTX", PDF "FAEVLINT"; 其余 18 格一致 (`ig34_p0373.txt:27`, 渲染 p373) | `knowledge_base/domains/FA/examples.md:239` 19 格逐格一致 | 无 (叙述句 FAEVINTX 属另一原子, 登记 B-FA T-9, 不在本条) |
| E81 | ig34_p0374_a011 | HOLDS | 渲染 p374: CRF 表为两层表头, 上层 = 左 4 列合并空格 + 跨 Visit 2-6 的 "At each visit, record the maximum severity…"; 下层 = AE ID / Adverse Event / Start Date / End Date / Visit 2-6. 原子把下层前 4 格与上层跨列文字并成一行, 且漏 Visit 2-6 五格 (`ig34_p0374.txt:21-22`) | `knowledge_base/domains/FA/examples.md:263` (4 空格 + 跨列文字 + 4 空格) 与 `:265` (9 格 AE ID…Visit 6) 两行表头, 内容与列位与渲染一致 | 合并单元格在 Markdown 中拆为空格, 属表格归一化, 无信息丢失 |
| E82 | ig34_p0396_a009 | HOLDS | 原子 "arrow represents this rule"; PDF "arrow represented this rule" (`ig34_p0396.txt:19-20`, 渲染 p396) | `knowledge_base/domains/TA/examples.md:672` 逐字一致 (该行首句) | 无 |
| E83 | ig34_p0419_a004 | HOLDS | 原子 "are within a dataset"; PDF "are within a subject" (`ig34_p0419.txt:11-14`, 渲染 p419) | `knowledge_base/domains/TS/assumptions.md:41` 逐字一致 | 无 |

## 计数

- HOLDS: 20
- NOT_HOLD: 0
- UNVERIFIABLE: 0
- 涉登记: E64 (B-RS T-3), E71 (B-RS T-6 RS 副本), E79 (B-FA T-2)
- 没看渲染页只看文本层: 无 (20 条全部对照渲染页)

## 样本外发现的 KB 内容问题

无. (顺带看到 `knowledge_base/domains/FT/assumptions.md:78` 的 "--STNRC" 对 PDF p323 "--STRNC", 已登记 B-RS T-6 (FT 副本), 不算新问题.)
