# T4.1 第三轮补检 — 包 11 (R3_HEADING, T250-T274) 审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T06:36:42Z (`date -u` 实取)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` (R3_HEADING 层; 认可写法: 域文件 `# 域代码 — 域名` 不带节号; 标题追加域代码后缀 U-10①; "–"/"—" 排版差异算等价)
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`): p140, p198, p281, p298
- 文本层: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0010/0011/0038/0041/0060/0074/0075/0076/0119/0140/0148/0198/0217/0239/0252/0256/0277-0284/0298/0311/0321/0329/0356/0358/0364.txt`
- 用过的命令: `grep -n "^#" knowledge_base/domains/<域>/*.md`; `grep -n "<标题文字>" knowledge_base/chapters/*.md`; `grep -rn "Method D" knowledge_base/domains/PC ...`; `grep -n "^Example\|^Method" ig34_p027*.txt ig34_p028*.txt`; `sed -n A,Bp <KB 文件>` (核标题下正文是否为该节); 渲染页用 Read(pages=N)
- 所有条目终态均为 EQUIVALENT (无 EXACT 条目, 故无 HOLDS_AS_EQUIV 适用)

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| T250 | `ig34_p0010_a017` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0010.txt:30` "1.5 Known Issues"; KB `knowledge_base/chapters/ch01_introduction.md:101` "## 1.5 Known Issues" | 实为逐字; 下接 "Derived Records and the use of --DRVFL" 与 PDF 同 |
| T251 | `ig34_p0011_a024` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0011.txt:39` "2.2 Datasets and Domains"; KB `knowledge_base/chapters/ch02_fundamentals.md:35` "## 2.2 Datasets and Domains" | 实为逐字; 正文首句一致 |
| T252 | `ig34_p0038_a017` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0038.txt:26` "4.4 Actual and Relative Time Assumptions"; KB `knowledge_base/chapters/ch04_general_assumptions.md:713` 同文 | 实为逐字; 正文首句一致 |
| T253 | `ig34_p0041_a043` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0041.txt:47` "4.4.4 Use of the Study Day Variables"; KB `knowledge_base/chapters/ch04_general_assumptions.md:871` "### 4.4.4 Use of the Study Day Variables" | 实为逐字; 正文首句一致 |
| T254 | `ig34_p0060_a004` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0060.txt:5` "5.1 Comments (CO)"; KB `knowledge_base/domains/CO/assumptions.md:7` "## 5.1 Comments (CO)" | 实为逐字 |
| T255 | `ig34_p0060_a005` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0060.txt:6` "CO – Description/Overview"; KB `knowledge_base/domains/CO/assumptions.md:9` "### CO – Description/Overview" | 实为逐字 |
| T256 | `ig34_p0076_a001` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0076.txt:1` "CRF Metadata" (属 Example 6, 起于 `ig34_p0074.txt:42`; p75 为 ASIAN/BLACK 子类 aCRF); KB `knowledge_base/domains/DM/examples.md:328` "**CRF Metadata**" (在 `## Example 6` 行 280 下, 表首行 RACE01 Order 3 与 PDF 同) | 粗体标签代替标题层级, 文字一致; 包给的 :176 属 Example 4, 对应处是 :328 |
| T257 | `ig34_p0119_a021` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0119.txt:26` "Example 8"; KB `knowledge_base/domains/EX/examples.md:418` "## Example 8" | 实为逐字; 下接正文 "In this example, a 100 mg tablet..." 与 PDF 同 |
| T258 | `ig34_p0140_a009` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0140.txt:23` / 渲染 p140 "AE – Examples"; KB `knowledge_base/domains/AE/examples.md:1` "# AE — Examples" | "–"→"—" 排版差异, 等价 |
| T259 | `ig34_p0140_a010` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0140.txt:24` "Example 1"; KB `knowledge_base/domains/AE/examples.md:3` "## Example 1" | 实为逐字; 正文对应 |
| T260 | `ig34_p0140_a012` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0140.txt:29` / 渲染 p140 粗体 "Rows 1-2:" (Example 1 内); KB `knowledge_base/domains/AE/examples.md:7` "**Rows 1-2:** Show examples of modifying..." | 粗体行首标签, 文字一致; :23 属 Example 2, 非对应处 |
| T261 | `ig34_p0148_a013` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0148.txt:19` "6.2.3 Clinical Events (CE)"; KB `knowledge_base/domains/CE/spec.md:1` "# CE — Clinical Events" (正文 `knowledge_base/domains/CE/assumptions.md:3` "## CE – Description/Overview" 起) | 认可写法 `# 域代码 — 域名` (问题 6 = A); 包给的 VARIABLE_INDEX 指针不采用 |
| T262 | `ig34_p0198_a015` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0198.txt:33` / 渲染 p198 "BS – Example" (单数); KB `knowledge_base/domains/BS/examples.md:1` "# BS — Examples" (下接 :3 "## Example 1", 正文为 RNA integrity 例) | 差异仅 "–"→"—" 与单复数 (Example→Examples), 信息等价 |
| T263 | `ig34_p0217_a009` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0217.txt:40` "Example 7"; KB `knowledge_base/domains/CP/examples.md:241` "## Example 7" | 实为逐字; 下接 "This example shows data from a monocyte target occupancy assay..." 与 PDF 同 |
| T264 | `ig34_p0239_a006` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0239.txt:16` "Example 9"; KB `knowledge_base/domains/IS/examples.md:189` "## Example 9" | 实为逐字; 正文 OPK assay 句一致 |
| T265 | `ig34_p0252_a016` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0252.txt:12` "MS – Description/Overview"; KB `knowledge_base/domains/MS/assumptions.md:3` "## MS – Description/Overview" | 实为逐字; 正文首句一致 |
| T266 | `ig34_p0256_a010` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0256.txt:19` "Example 1" (§6.3.5.7.3 MB/MS Examples 下); KB `knowledge_base/domains/MB/examples.md:5` "### Example 1" (在 :3 "## §6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples" 下; 正文 Enterococcus faecalis 句一致) | 实为逐字; 包给的 `domains/CM/examples.md:3` 指针错 (CM 非本节), 正确位置为 MB |
| T267 | `ig34_p0281_a045` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0281.txt:53` / 渲染 p281 粗体 "Method D (One to One, Using PCSEQ and PPSEQ)" (属 Example 3, 起于 `ig34_p0280.txt:39`); KB `knowledge_base/domains/PC/examples.md:351` "#### Method D (One to One, Using PCSEQ and PPSEQ)" (在 :274 "### Example 3" 下; Rows 1-17 / 18-29 说明与 relrec 行 1 一致) | 实为逐字; 包无指针, 自行定位; §6.3.5.9.3 为 PC/PP 共用节, KB 放 PC (PP/examples.md:3 有说明指向), 位置可接受 |
| T268 | `ig34_p0298_a023` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0298.txt:34` / 渲染 p298 "6.3.7.5 Ophthalmic Examinations (OE)"; KB `knowledge_base/domains/OE/spec.md:1` "# OE — Ophthalmic Examinations" (正文 `knowledge_base/domains/OE/assumptions.md:3` "## OE – Description/Overview" 起, 首句一致) | 认可写法 `# 域代码 — 域名`; 包无指针, 自行定位 |
| T269 | `ig34_p0311_a020` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0311.txt:22` "Example 2"; KB `knowledge_base/domains/RE/examples.md:40` "## Example 2" | 实为逐字; FEV1 4 attempts 正文一致 |
| T270 | `ig34_p0321_a001` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0321.txt:1` "FT – Assumptions"; KB `knowledge_base/domains/FT/assumptions.md:26` "## FT – Assumptions" | 实为逐字; 下接 "The following assumptions are unique to the FT domain:" |
| T271 | `ig34_p0329_a005` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0329.txt:9` "RS – Description/Overview"; KB `knowledge_base/domains/RS/assumptions.md:3` "## RS – Description/Overview" | 实为逐字; 正文首句一致 |
| T272 | `ig34_p0356_a008` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0356.txt:15` "Example 3" (§6.3.12.3 TU/TR Examples); KB `knowledge_base/domains/TU/examples.md:76` "## Example 3" (正文 RECIST 1.1 句一致) | 实为逐字; 包给的 `domains/CM/examples.md:41` 指针错, 正确位置为 TU |
| T273 | `ig34_p0358_a008` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0358.txt:22` "relrec.xpt" (TU/TR Example 3, TU–TR 关系); KB `knowledge_base/domains/TR/examples.md:105` "**relrec.xpt**" (前句 "The relationship between the TU and TR records is represented in RELREC.", 表 2 行 TULNKID/ONE、TRLNKID/MANY 与 PDF 同) | 粗体标签, 文字一致; 包给的 `domains/RELREC/examples.md` 指针不是该处 |
| T274 | `ig34_p0364_a020` | R3_HEADING | EQUIVALENT | HOLDS | PDF `ig34_p0364.txt:40` "6.4.4 Findings About Events or Interventions (FA)"; KB `knowledge_base/domains/FA/assumptions.md:95` "## §6.4.4 Findings About Events or Interventions (FA)" (下接 :97 "## FA – Description/Overview") | 实为逐字 (节号 `§` 前缀不算差异); 包给的 VARIABLE_INDEX 指针不采用 |

## 计数 (R3_HEADING, 25 条)

| 判定 | 数 |
|---|---|
| HOLDS | 25 |
| HOLDS_AS_EQUIV | 0 |
| NOT_HOLD_SELF | 0 |
| NOT_HOLD | 0 |
| UNVERIFIABLE | 0 |

## 样本外发现的 KB 内容问题

无 (KB 内容方面)。另记包指针问题 (非 KB 问题, 仅供脚本参考): T256 指针含 Example 4 的 :176; T260 含 Example 2 的 :23; T266 / T272 指到 `domains/CM/examples.md` (错域); T273 指到 `domains/RELREC/examples.md` 而非 `domains/TR/examples.md:105`。
