# T4.1 第三轮补检 原始结果 — 包 12 (R3_HEADING, T275-T299, 25 条)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T06:38:04Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` § R3_HEADING (后者优先)
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`): p61, p280, p384
- 文本层: `.work/10_tier_b_repair/work/pdf_pages/ig34_p{0043,0061,0085,0101,0102,0131,0132,0137,0150,0179,0191,0194,0227,0235,0237,0265,0267,0270-0283,0384,0404,0405,0415}.txt`
- 用过的命令 (均只读):
  - `grep -n '^#' knowledge_base/domains/<域>/{assumptions,examples,spec}.md` (逐文件列标题)
  - `sed -n` 对照 PDF 标题行后 2 行与 KB 标题行后 3 行 (核标题下正文是该节)
  - `grep -rn 'Only some records in PC were used' knowledge_base` (T299 定位)
  - `grep -n 'Example\|^6\.3\.5\.9\|Relating' pdf_pages/ig34_p027*.txt ig34_p028[0-3].txt`
  - `od -c` 核破折号字形: PDF "CO – Examples" 为 en dash (U+2013); KB `# CO — Examples` 为 em dash (U+2014); KB `## SU – Assumptions` 为 en dash

## 判定说明 (口径应用)
- 终态 EXACT 的 "X – Examples" 类原子, KB 唯一对应标题是文件 H1 `# X — Examples` (en dash → em dash)。本层口径把 "–" 写成 "—" 列为 **等价** 级的排版差异 (EQUIVALENT 的 HOLDS 条件), 而 EXACT 的 HOLDS 只豁免节号写法 / `#` 层级 / 粗体, 字符替换不在豁免内 → 按口径从严判 **HOLDS_AS_EQUIV** (内容成立, 标签级别应为 EQUIVALENT)。同文件夹内没有逐字 "X – Examples" 标题 (已 grep)。
- 终态 EXACT 的 "X – Assumptions" 类, KB 另有 `## X – Assumptions` (en dash, 逐字) → HOLDS。

## 表格

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| T275 | `ig34_p0384_a018` | R3_HEADING | EQUIVALENT | HOLDS | PDF p384 渲染页 / `ig34_p0384.txt:30` "7.2.1 Trial Arms (TA)" (H2); KB `knowledge_base/domains/TA/assumptions.md:80` "### §7.2.1 Trial Arms (TA) – Description/Overview" (下接 PDF 同节 Description 正文 :82-88), 另 `knowledge_base/domains/TA/spec.md:1` "# TA — Trial Arms" (认可写法) | 节号+标题文字齐, 与下级小标题合并成一行 → 等价成立。包里 PDF 定位行 24 是正文引用, 实标题在行 30 |
| T276 | `ig34_p0404_a013` | R3_HEADING | EQUIVALENT | HOLDS | `ig34_p0404.txt:39` "TE – Examples"; KB `knowledge_base/domains/TE/examples.md:1` "# TE — Examples", 下文 :3 "Both of the trials in TA Examples 1 and 2 ..." = PDF :40 | – → — 排版差异, 等价 |
| T277 | `ig34_p0405_a001` | R3_HEADING | EQUIVALENT | HOLDS | `ig34_p0405.txt:1` "Example 1"; KB `knowledge_base/domains/TE/examples.md:5` "## Example 1", 下文 :7 = PDF :2 | 实为逐字 |
| T278 | `ig34_p0405_a020` | R3_HEADING | EQUIVALENT | HOLDS | `ig34_p0405.txt:27` "Example 3"; KB `knowledge_base/domains/TE/examples.md:34` "## Example 3", 下文 :36 = PDF :28 | 实为逐字 |
| T279 | `ig34_p0415_a002` | R3_HEADING | EQUIVALENT | HOLDS | `ig34_p0415.txt:2` "TM – Description/Overview"; KB `knowledge_base/domains/TM/assumptions.md:3` "## TM — Description/Overview", 下文 :5 = PDF :3 | – → — 排版差异, 等价 |
| T280 | `ig34_p0043_a009` | R3_HEADING | EXACT | HOLDS | `ig34_p0043.txt:11` "--STRF and --ENRF" (4.4.7 下); KB `knowledge_base/chapters/ch04_general_assumptions.md:930` "#### --STRF and --ENRF" (在 :928 "### 4.4.7 Use of Relative Timing Variables" 下), 下文 :932 = PDF :12 | 逐字 |
| T281 | `ig34_p0061_a015` | R3_HEADING | EXACT | HOLDS_AS_EQUIV | PDF p61 渲染页 / `ig34_p0061.txt:22` "CO – Examples"; KB `knowledge_base/domains/CO/examples.md:1` "# CO — Examples", 下接 :3 "## Example 1" + Row 1 正文 = PDF | KB 标题 en dash 写成 em dash, 非逐字; 内容成立 |
| T282 | `ig34_p0085_a008` | R3_HEADING | EXACT | HOLDS | `ig34_p0085.txt:12` "Example 1" (SM – Examples 下); KB `knowledge_base/domains/SM/examples.md:3` "## Example 1", 下文 :5 = PDF :13 | 逐字 |
| T283 | `ig34_p0101_a014` | R3_HEADING | EXACT | HOLDS_AS_EQUIV | `ig34_p0101.txt:15` "CM – Examples"; KB `knowledge_base/domains/CM/examples.md:1` "# CM — Examples", 下接 :3 "## Example 1" 正文 = PDF :17 | en dash → em dash, 非逐字; 内容成立 |
| T284 | `ig34_p0102_a009` | R3_HEADING | EXACT | HOLDS | `ig34_p0102.txt:13` "Example 3"; KB `knowledge_base/domains/CM/examples.md:41` "## Example 3", 下文 :43 = PDF :14 | 逐字 |
| T285 | `ig34_p0102_a025` | R3_HEADING | EXACT | HOLDS | `ig34_p0102.txt:29` "Example 4"; KB `knowledge_base/domains/CM/examples.md:61` "## Example 4", 下文 :63 = PDF :30 | 逐字 |
| T286 | `ig34_p0131_a004` | R3_HEADING | EXACT | HOLDS | `ig34_p0131.txt:12` "SU – Assumptions"; KB `knowledge_base/domains/SU/assumptions.md:11` "## SU – Assumptions" (en dash), 下文 item 1 = PDF :13 | 逐字 (另有 :1 文件 H1 `# SU — Assumptions`) |
| T287 | `ig34_p0132_a002` | R3_HEADING | EXACT | HOLDS_AS_EQUIV | `ig34_p0132.txt:3` "SU – Examples"; KB `knowledge_base/domains/SU/examples.md:1` "# SU — Examples", 下接 :3 "## Example 1" 正文 = PDF :5 | en dash → em dash, 非逐字; 内容成立 |
| T288 | `ig34_p0137_a011` | R3_HEADING | EXACT | HOLDS | `ig34_p0137.txt:31` "AE – Assumptions"; KB `knowledge_base/domains/AE/assumptions.md:23` "## AE – Assumptions", 下文 item 1 = PDF :32 | 逐字 |
| T289 | `ig34_p0150_a005` | R3_HEADING | EXACT | HOLDS | `ig34_p0150.txt:15` "CE – Assumptions"; KB `knowledge_base/domains/CE/assumptions.md:11` "## CE – Assumptions", 下文 item 1 = PDF :16 | 逐字 |
| T290 | `ig34_p0179_a0010` | R3_HEADING | EXACT | HOLDS_AS_EQUIV | `ig34_p0179.txt:25` "DV – Examples"; KB `knowledge_base/domains/DV/examples.md:1` "# DV — Examples", 下接 :3 "## Example 1" 正文 = PDF :27 | en dash → em dash, 非逐字; 内容成立 |
| T291 | `ig34_p0191_a022` | R3_HEADING | EXACT | HOLDS | `ig34_p0191.txt:45` "Example 4"; KB `knowledge_base/domains/EG/examples.md:89` "## Example 4", 下文 :91 = PDF :46 | 逐字 |
| T292 | `ig34_p0194_a007` | R3_HEADING | EXACT | HOLDS | `ig34_p0194.txt:15` "Example 1" (IE – Examples 下); KB `knowledge_base/domains/IE/examples.md:3` "## Example 1", 下文 :5 = PDF :16 | 逐字 (原子是 "Example 1", 不是 "IE – Examples") |
| T293 | `ig34_p0227_a001` | R3_HEADING | EXACT | HOLDS | `ig34_p0227.txt:1` "Example 4" (GF); KB `knowledge_base/domains/GF/examples.md:116` "## Example 4", 下文 :118 = PDF :2 | 逐字 |
| T294 | `ig34_p0235_a003` | R3_HEADING | EXACT | HOLDS | `ig34_p0235.txt:9` "Example 4" (IS); KB `knowledge_base/domains/IS/examples.md:69` "## Example 4", 下文 :71 = PDF :10 | 逐字 |
| T295 | `ig34_p0235_a026` | R3_HEADING | EXACT | HOLDS | `ig34_p0235.txt:42` "Example 5"; KB `knowledge_base/domains/IS/examples.md:97` "## Example 5", 下文 :99 = PDF :43 | 逐字 |
| T296 | `ig34_p0237_a015` | R3_HEADING | EXACT | HOLDS | `ig34_p0237.txt:30` "Example 7"; KB `knowledge_base/domains/IS/examples.md:147` "## Example 7", 下文 :149 = PDF :31 | 逐字 |
| T297 | `ig34_p0265_a017` | R3_HEADING | EXACT | HOLDS | `ig34_p0265.txt:37` "MI – Assumptions"; KB `knowledge_base/domains/MI/assumptions.md:13` "## MI – Assumptions", 下文 item 1 = PDF :38 | 逐字 |
| T298 | `ig34_p0267_a001` | R3_HEADING | EXACT | HOLDS | `ig34_p0267.txt:1` "Example 3" (MI); KB `knowledge_base/domains/MI/examples.md:41` "## Example 3", 下文 :43 = PDF :2 | 逐字 |
| T299 | `ig34_p0280_a034` | R3_HEADING | EXACT | HOLDS | PDF p280 渲染页 / `ig34_p0280.txt:39` "Example 3" (§6.3.5.9.3 Relating PP Records to PC Records 下, 正文 "Only some records in PC were used to calculate some parameters; time points 8 and 9 ..."); KB `knowledge_base/domains/PC/examples.md:274` "### Example 3" (在 :60 "## §6.3.5.9.3 Relating PP Records to PC Records — Worked Examples" 下), 下文 :276 = PDF :40-41 | 逐字。**包里指针错**: `PP/examples.md:76` 是 PP 域自己的 Example 3 (PDF p274, 正文 PPSTINT/AUCINT), 不是本节; 正确位置在 PC 目录 (§6.3.5.9.3 为 PC/PP 共用节, 仍属 SDTMIG 自己文档) |

## 计数
- HOLDS: 21
- HOLDS_AS_EQUIV: 4 (T281, T283, T287, T290)
- NOT_HOLD_SELF: 0
- NOT_HOLD: 0
- UNVERIFIABLE: 0
- 按终态: EQUIVALENT 5 条 (T275-T279) 全 HOLDS; EXACT 20 条 → HOLDS 16 / HOLDS_AS_EQUIV 4

## 样本外发现的 KB 内容问题
无内容缺失或错误。附注 (非样本判定, 供口径参考):
- `knowledge_base/domains/TA/assumptions.md:94` "### §7.2.1 Trial Arms (TA) – Example 2" 是 KB 自拟的指针型小标题 (正文只有一句 "See examples.md#example-2"), PDF 无此标题。
- 包 12 的 T299 自动指针跨了同名标题 (PP 域 Example 3 vs §6.3.5.9.3 Example 3); 同类 "Example N" 标题原子若只按指针核, 可能误判。
