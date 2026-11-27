# T4.1 第三轮补检 — 包 1 (R3_IG34_EQUIV, T1-T25) 独立审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T06:37:11Z (`date -u`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` (R3_IG34_EQUIV 层)
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`, Read 带 pages): p70, p71, p75, p400
- 文本层: `ig34_p0009/0046/0070-0076/0113/0114-0116/0123-0124/0141-0142/0227-0228/0233-0234/0247-0248/0254/0263.txt`
- 用过的命令: `sed -n` / `grep -n` 对 PDF 文本层与 `knowledge_base/` 文件逐段比对; `grep -n` 查 `work/t2_pdf_typo_registry.jsonl`; `date -u +%Y-%m-%dT%H:%M:%SZ`

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| T1 | `ig34_p0046_a017` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0046.txt:25`; `knowledge_base/chapters/ch04_general_assumptions.md:1097` | 实为逐字; 时间点表 6 格逐格一致 (1 / 30 MIN / PT30M / DOSE ADMINISTRATION / 2006-08-01T08:00 / 2006-08-01T08:30), 位于 §4.4.10 时间点段 |
| T2 | `ig34_p0046_a021` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0046.txt:27`; `ch04_general_assumptions.md:1099` | 实为逐字; 行 3 逐格一致 (PT1H30M / 09:32) |
| T3 | `ig34_p0073_a014` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0073.txt:42,47`; `knowledge_base/domains/DM/examples.md:196,204` | 实为逐字; p73 为 DM Example 4, 正文句内 "dm.xpt" 与表名 dm.xpt 两处 KB 均有, 位于 Example 4 |
| T4 | `ig34_p0075_a015` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p75 (Example 6 aCRF 图 "CRACE05-CRACE10" 标签); `DM/examples.md:311,326,340` | 包内 KB 指针指向 Example 4 (L170/190), 本原子属 Example 6 (p75); Example 6 段 KB 注 L326 "(CRACE05-CRACE10)"、Mermaid L311 "CRACE05-10"、元数据表 L340 均承载 |
| T5 | `ig34_p0116_a008` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0116.txt:9-10`; `knowledge_base/domains/EX/examples.md:261-263` | 实为逐字; §6.1.3.3 为 EX/EC 合并节, KB 放在 EX/examples.md Example 6 (EC/examples.md:3 指引过去), 前句 "The EC dataset shows administrations as collected." 一致 |
| T6 | `ig34_p0124_a014` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0124.txt:31-32`; `knowledge_base/domains/ML/examples.md:59-61` | 实为逐字; Example 2 |
| T7 | `ig34_p0142_a013` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0142.txt:1`; `knowledge_base/domains/AE/examples.md:56` | 实为逐字; AE Example 4 表名 (跨页), KB 在 Example 4 Rows 说明之后 |
| T8 | `ig34_p0228_a004` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0228.txt:6`; `knowledge_base/domains/GF/examples.md:161` | 实为逐字; GF Example 5 (包内指针 L25/60/84 是 Example 1-3, 非本处) |
| T9 | `ig34_p0234_a020` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0234.txt:5`; `knowledge_base/domains/IS/examples.md:38` | 实为逐字; IS Example 2 Rows 7-8 说明之后 |
| T10 | `ig34_p0248_a006` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0248.txt:6`; `knowledge_base/domains/LB/examples.md:80` | 实为逐字; LB Example 4 (包内指针 L20/50/65 是 Example 1-3) |
| T11 | `ig34_p0254_a002` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0254.txt:4-5`; `knowledge_base/domains/MS/spec.md:248-255` | 原子属 MS spec 表行 (包内指针指向 examples, 偏); KB spec 逐格一致: MSNAM / Laboratory/Vendor Name / Char / (空) / Record Qualifier / CDISC Notes 原文 / Perm |
| T12 | `ig34_p0263_a007` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0263.txt:7-9`; `knowledge_base/domains/MB/examples.md:218-220` | 实为逐字; MB/MS Example 3 RELREC (包内指针 AG/examples.md 是别域, 偏); 前句与 6 行表逐格一致 |
| T13 | `ig34_p0263_a024` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0263.txt:33-34`; `MB/examples.md:246-248` | 实为逐字; MB Example 4 suppmb.xpt (包内 L85/196 是 Example 2/3) |
| T14 | `ig34_p0400_a009` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p400 下图; `knowledge_base/domains/TA/examples.md:893-929` | KB 以 Mermaid 再现 "Prospective View": 4 epoch、上臂 Chemo+Rad→Chemo+Rad*→Chemo+Boost→Chemo→FU、下臂 Chemo+Rad→Chemo+Rad**→3-5w Rest→Surgery→4-6w Rest→Chemo→Chemo→FU、两处 "If disease progression" 跳转、"If not eligible for surgery" 跳到第一个 Chemo、CR/CRS 臂名、脚注 *Disease evaluation earlier **Disease evaluation later 全部与图一致, 无矛盾。小差: 图中 Randomization 箭头指向 Screen/Induction 分界, KB 画成指向 Screen Epoch 子图 (示意性, 不判矛盾) |
| T15 | `ig34_p0009_a017` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0009.txt:35`; `knowledge_base/chapters/ch01_introduction.md:74` | 实为逐字; §1.4.1 列表项 |
| T16 | `ig34_p0009_a020` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0009.txt:38`; `ch01_introduction.md:77` | 实为逐字 |
| T17 | `ig34_p0061_a002` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0061.txt:2-4`; `knowledge_base/domains/CO/assumptions.md:19` | 实为逐字; 原子只抽了第 1 句, KB 含该项全部两句 |
| T18 | `ig34_p0070_a018` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p70 (Example 4 aCRF 第 7 行: 徽标 RACE07 RACE, 选项 UNKNOWN, <RACE codelist>); `DM/examples.md:124,166,186` | 原子抽错 ("RAC607 BAC" 为 "RACE07 RACE" 的 OCR 乱码); KB Example 4: Mermaid R7 "UNKNOWN"、注 "RACE07: UNKNOWN"、元数据行 RACE07 → RACE, 代码表 (RACE), 值 UNKNOWN, 信息点齐 |
| T19 | `ig34_p0070_a023` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p70 (CRACE01-CRACE04 子图选项 ALASKA NATIVE); `DM/examples.md:134,168` | KB Example 4 Mermaid SC1 与注中均有 ALASKA NATIVE |
| T20 | `ig34_p0071_a006` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p71 (Example 4 ASIAN 子图选项 ASIAN INDIAN); `DM/examples.md:135,170,190` | KB Example 4 Mermaid SC2、注、元数据行均有 |
| T21 | `ig34_p0075_a020` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p75 (Example 6 ASIAN 子图选项 CHINESE); `DM/examples.md:311,340` | 包内指针是 Example 4; 本原子属 Example 6, KB Example 6 Mermaid SC1 / 元数据行均有 CHINESE |
| T22 | `ig34_p0075_a021` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p75 (Example 6 选项 JAPANESE); `DM/examples.md:311,340` | 同上 (文本层未定位, 渲染页确认在图内) |
| T23 | `ig34_p0075_a033` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p75 (Example 6 BLACK OR AFRICAN AMERICAN 子图选项 BLACK); `DM/examples.md:312,342` | KB Example 6 Mermaid SC2 与 CRACE11-CRACE17 元数据行均有 BLACK |
| T24 | `ig34_p0113_a010` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0113.txt:12`; `knowledge_base/domains/EX/examples.md:117` | 实为逐字; EX Example 3 (下一项 PDF "ottles" 笔误已登记 B-EX T-3, 不属本原子) |
| T25 | `ig34_p0141_a025` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0141.txt:43`; `knowledge_base/domains/AE/examples.md:54` | 实为逐字 (仅加粗); AE Example 4 |

## 计数 (R3_IG34_EQUIV, 25 条)

| 判定 | 数 |
|---|---|
| HOLDS | 25 (其中实为逐字 16, 见下注) |
| TYPO_AFFECTED | 0 |
| NOT_HOLD | 0 |
| UNVERIFIABLE | 0 |

注: "实为逐字" 条目 = T1, T2, T3, T5, T6, T7, T8, T9, T10, T12, T13, T15, T16, T17, T24, T25 共 16 条; 其余 9 条 (T4, T11, T14, T18-T23) 为等价承载 (Mermaid / 注 / 元数据表 / spec 字段式)。原子抽错: T18。

## 样本外发现的 KB 内容问题

无新问题。顺带核对到的 PDF 笔误均已登记: p113 "ottles" (B-EX T-3)、p263 MB Example 4 表头 "MBGPRID" (B-MB T-2)、"MBTRESN" (B-MB T-3)。另: 包内 KB 指针偏差 (T4/T8/T10/T11/T12/T13/T21-T22 指到同域别的例子、别域或别文件) 属脚本定位问题, 非 KB 问题。
