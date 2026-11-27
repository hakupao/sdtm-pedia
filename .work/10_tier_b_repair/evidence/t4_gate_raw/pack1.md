<!-- 原样誊录: feature-dev:code-reviewer (opus) 对 `work/t4/gate_pack_1.md` 的回复, 2026-11-27. 主控未改动内容. -->

## T4.1 总闸独立审：gate_pack_1 (21 条) 判定

21 条全部 HOLDS，没有 NOT_HOLD，也没有 UNVERIFIABLE。

核对方法：每条 PDF 原文都在 `.work/10_tier_b_repair/work/pdf_pages/` 页文本里用 Grep 和 Read 单独定位过，KB 行也在对应域 / 章节文件里重新 Grep 过，并读了上下文确认所在章节 / Example / Method 是对的，没有只看样本包里贴的摘录。21 条都只涉及空白、Markdown 管道 / 粗体 / 标题标记、列表符号和换行合并，没有引号、破折号或勾选符上的疑点，所以没有调渲染页。

### 1. 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF 文件:行 / 渲染页; KB 文件:行) | NOT_HOLD / UNVERIFIABLE 的原因 |
|---|---|---|---|---|---|---|
| 1 | ig34_p0016_a018 | PRESENT | EXACT | HOLDS | ig34_p0016.txt:20 ("extreme caution" 列表第 4 项); ch02_fundamentals.md:174 (同一列表, 167-174) | — |
| 2 | ig34_p0031_a028 | PRESENT | EXACT | HOLDS | ig34_p0031.txt:39; ch04_general_assumptions.md:403 | — |
| 3 | ig34_p0055_a003 | PRESENT | EXACT | HOLDS | ig34_p0055.txt:4-5; ch04_general_assumptions.md:1399 (在 §4.5.3.1 下, 1390) | — |
| 4 | ig34_p0103_a006 | PRESENT | EXACT | HOLDS | ig34_p0103.txt:7-10; CM/examples.md:82 (整段正则完全匹配, 计数 1) | — |
| 5 | ig34_p0117_a007 | PRESENT | EXACT | HOLDS | ig34_p0117.txt:39; EX/examples.md:331 | — |
| 6 | ig34_p0119_a006 | PRESENT | EXACT | HOLDS | ig34_p0119.txt:9; EX/examples.md:394 (前一句 392 与 PDF 第 8 行一致, 后接 VS 表头 396) | — |
| 7 | ig34_p0123_a019 | PRESENT | EXACT | HOLDS | ig34_p0123.txt:29-30; ML/examples.md:31 | — |
| 8 | ig34_p0184_a022 | PRESENT | EXACT | HOLDS | ig34_p0184.txt:30; DD/examples.md:25 (`## Example 2`, 下接 27 行与 PDF 第 31 行一致) | — |
| 9 | ig34_p0281_a023 | PRESENT | EXACT | HOLDS | ig34_p0281.txt:25 (Example 3 Method B 第 18 行); PC/examples.md:323 (Method B 表, 297-329) | — |
| 10 | ig34_p0282_a003 | PRESENT | EXACT | HOLDS | ig34_p0282.txt:4 (Example 3 Method D 续表第 8 行); PC/examples.md:367 (Method D 表, 351-388)。指针给的 98/160/313 是别的 Example / Method 里同值的行, 正确对应是 367 | — |
| 11 | ig34_p0440_a012 | PRESENT | EXACT | HOLDS | ig34_p0440.txt:18-19; RELSPEC/examples.md:40 | — |
| 12 | sv20_p0009_a006 | PRESENT | EXACT | HOLDS | sv20_p0009.txt:12-18; model/01_concepts_and_terms.md:160 (正则完全匹配, 计数 1) | — |
| 13 | ig34_p0010_a008 | REWRITE_OK | EXACT | HOLDS | ig34_p0010.txt:12-14; ch01_introduction.md:91 (Codelist 子列表, 层级与 PDF 一致) | — |
| 14 | ig34_p0011_a008 | REWRITE_OK | EXACT | HOLDS | ig34_p0011.txt:8; ch02_fundamentals.md:15 | — |
| 15 | ig34_p0012_a017 | REWRITE_OK | EXACT | HOLDS | ig34_p0012.txt:26-27; ch02_fundamentals.md:53 (只多了粗体) | — |
| 16 | ig34_p0012_a028 | REWRITE_OK | EXACT | HOLDS | ig34_p0012.txt:45-46; ch02_fundamentals.md:67 | — |
| 17 | ig34_p0043_a013 | REWRITE_OK | EXACT | HOLDS | ig34_p0043.txt:18; ch04_general_assumptions.md:934 (PDF 两行在 KB 里合成一段, 只是空白差异) | — |
| 18 | ig34_p0043_a023 | REWRITE_OK | EXACT | HOLDS | ig34_p0043.txt:32-33 (PDF 是 "CMSTRF.Some", 缺空格); ch04_general_assumptions.md:949 另起一段。缺空格已登记为 S-CH4 T-10e, 处理方式 "KB 写正确值" | — |
| 19 | ig34_p0044_a002 | REWRITE_OK | EXACT | HOLDS | ig34_p0044.txt:2; ch04_general_assumptions.md:966 | — |
| 20 | ig34_p0044_a004 | REWRITE_OK | EXACT | HOLDS | ig34_p0044.txt:4-5; ch04_general_assumptions.md:970 (第一组 "corresponds to the date of collection" 下, 968。976 是第二组, 措辞不同) | — |
| 21 | ig34_p0044_a013 | REWRITE_OK | EXACT | HOLDS | ig34_p0044.txt:20 (Example 1: Medical History); ch04_general_assumptions.md:990 (在 988 `**Example 1: Medical History**` 下, 后接 992-993 与 PDF 21-22 一致)。1019 和 1035 是其它 Example 的同名行 | — |

### 2. 计数

- HOLDS：21
- NOT_HOLD：0
- UNVERIFIABLE：0

### 3. 样本外发现的 KB 内容问题

无未登记的问题。

核对过程中看到 6 处 PDF 自身有问题的地方，都已在 `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` 登记，KB 现状与登记一致：

| 登记 id | KB 位置 | PDF 页 | PDF 写法 | 处理方式 |
|---|---|---|---|---|
| B-ch02 T-1 | ch02_fundamentals.md:176 | p16 | "Trials Sets domain" | 照录 |
| B-ch01 T-1 | ch01_introduction.md:85 | p10 | "a codelist not yet been developed" | KB 写正确值 ("has not yet been") |
| S-CH4 T-8 | ch04_general_assumptions.md:932 | p43 | `"ONGOING"'`, 多一个撇号 | KB 写正确值 |
| S-CH4 T-10d | ch04_general_assumptions.md:947 | p43 | "variables.As", 缺空格 | KB 写正确值 |
| S-SPC2 N-2 | PC/examples.md:333 | p281 | "PGRPID values" | 照录 |
| B-PCPP T-8 | PC/examples.md:284 | p280 | "DYIDRGX_A" (登记里注明同一问题共 2 处: _A / _HALF) | 照录 |

另外有一点与判定无关：第 10 条的自动指针 (98/160/313/367) 是按值匹配的，同一张 relrec 表的行在 PC/examples.md 里重复出现在多个 Method 中。脚本按值给出的指针不能区分它们，所以这一条是靠所在 Example / Method 自己定位到 367 的。
