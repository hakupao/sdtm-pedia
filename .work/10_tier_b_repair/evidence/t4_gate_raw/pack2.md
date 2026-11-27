<!-- 原样誊录: feature-dev:code-reviewer (opus) 对 `work/t4/gate_pack_2.md` 的回复, 2026-11-27. 主控未改动内容. -->

# T4.1 总闸审查结果：gate_pack_2（第 22-42 条，共 21 条）

21 条全部 HOLDS，KB 没有发现与 PDF 不符的地方。这次只读，没有改任何文件。

## 1. 逐条判定

PDF 页文本都在 `.work/10_tier_b_repair/work/pdf_pages/` 下；KB 路径都相对于 `knowledge_base/`。KB 行号均已用 Grep 重新定位，样本包给的指针全部准确。

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF 文件:行 / 渲染页; KB 文件:行) | NOT_HOLD / UNVERIFIABLE 的原因 |
|---|---|---|---|---|---|---|
| 22 | ig34_p0151_a0013 | REWRITE_OK | EXACT | HOLDS | ig34_p0151.txt:16-17 + 渲染页 151 (Rash 行 "Did it occur?" 格内上下两行 No/Yes，无勾选符)；domains/CE/examples.md:13 `\| Rash \| No  Yes \| \|` | — |
| 23 | ig34_p0153_a0009 | REWRITE_OK | EQUIVALENT | HOLDS | ig34_p0153.txt:6-9 + 渲染页 153 (○ Pathologic / Fall / Other trauma / Unknown)；CE/examples.md:77。KB 把 ○ 写成 `( )`，选项和顺序都一致 | — |
| 24 | ig34_p0153_a0019 | REWRITE_OK | EQUIVALENT | HOLDS | ig34_p0153.txt:17-19 + 渲染页 153 (□ Casting/immobilization / Traction / Surgery)；CE/examples.md:81。KB 把 □ 写成 `[ ]`，信息等价 | — |
| 25 | ig34_p0010_a025 | REAL_GAP | EXACT | HOLDS | ig34_p0010.txt:40-43 (文本层把 "--LNKID" 断成 "-\n-LNKID"，是版式断行)；chapters/ch01_introduction.md:109，Grep 全句命中 1 处 | — |
| 26 | ig34_p0014_a005 | REAL_GAP | EXACT | HOLDS | ig34_p0014.txt:13-20；chapters/ch02_fundamentals.md:98，Grep 全句正则命中，位于 §2.6 列表内 | — |
| 27 | ig34_p0029_a028 | REAL_GAP | EXACT | HOLDS | ig34_p0029.txt:42-44；chapters/ch04_general_assumptions.md:320，在 `### 4.2.5 Convention for Missing Values` (第 318 行) 下 | — |
| 28 | ig34_p0043_a034 | REAL_GAP | EQUIVALENT | HOLDS | ig34_p0043.txt:50 句子跨页接 ig34_p0044.txt:1-2 ("reference period, the timing variables … for each study.")；ch04_general_assumptions.md:955 完整逐字承载这个跨页句。原子在页边界被截断，标 EQUIVALENT 能成立 | — |
| 29 | ig34_p0045_a018 | REAL_GAP | EXACT | HOLDS | ig34_p0045.txt:16-17；ch04_general_assumptions.md:1038，前后列表项 (1037、1039) 与 PDF 顺序一致 | — |
| 30 | ig34_p0133_a021 | REAL_GAP | EXACT | HOLDS | ig34_p0133.txt:37-38；domains/AE/assumptions.md:17，在 `## AE – Description/Overview` 下 | — |
| 31 | ig34_p0185_a020 | REAL_GAP | EXACT | HOLDS | ig34_p0185.txt:24-25；domains/EG/assumptions.md:5，在 `## EG – Description/Overview` 下 | — |
| 32 | ig34_p0196_a004 | REAL_GAP | EXACT | HOLDS | ig34_p0196.txt:1-2 (表头列序) 与 :9-10；domains/LB/assumptions.md:41，7 列值都一致，表头 (第 20 行) 列序和 PDF 相同 | — |
| 33 | ig34_p0215_a014 | REAL_GAP | EXACT | HOLDS | ig34_p0215.txt:29-34；domains/CP/examples.md:194，Grep 全段正则命中 1 处 | — |
| 34 | ig34_p0263_a006 | REAL_GAP | EXACT | HOLDS | ig34_p0263.txt:7-8；domains/MB/examples.md:218，Grep 全句命中 1 处 | — |
| 35 | sv20_p0004_a012 | REAL_GAP | EXACT | HOLDS | sv20_p0004.txt:20；model/01_concepts_and_terms.md:15 (Grep 命中行) | — |
| 36 | sv20_p0004_a020 | REAL_GAP | EXACT | HOLDS | sv20_p0004.txt:33-34；model/01_concepts_and_terms.md:20，SENDIG 名称和 URL 都逐字一致，下一项 SENDIG-DART 顺序也对 | — |
| 37 | ig34_p0116_a013 | VALUE_DIFF | EQUIVALENT | HOLDS | ig34_p0116.txt:18-19 + 渲染页 116 (Row 4 的 ECTRT 为 "BOTTLE 2"、EPOCH 为 "TREATMENT 1")；domains/EX/examples.md:270，21 列都和渲染页一致。原子丢了 "2" 和 "1"，KB 是对的 | — |
| 38 | ig34_p0141_a007 | VALUE_DIFF | EXACT | HOLDS | ig34_p0141.txt:14-16 (PDF 中 If "Yes" 一处为弯引号)；domains/AE/examples.md:21，保留了同一个弯引号，在 `## Example 2` 下 | — |
| 39 | ig34_p0210_a002 | VALUE_DIFF | ATOM_ERR | HOLDS | ig34_p0210.txt:2 + 渲染页 210 表头列序为 …CPSTRESC \| CPSTRESU \| CPSTRESN…；原子把顺序错写成 CPSTRESC \| CPSTRESN \| CPSTRESU；domains/CP/examples.md:31 按 PDF 写对了 | — |
| 40 | ig34_p0210_a009 | VALUE_DIFF | EXACT | HOLDS | ig34_p0210.txt:15-16 + 渲染页 210 Row 7；CP/examples.md:39，19 列都一致 (64.8 \| % \| 64.8 \| % \| 64.8，以及 NUMBER FRACTION、FLOW CYTOMETRY、2021-08-16T04:20) | — |
| 41 | ig34_p0210_a018 | VALUE_DIFF | EXACT | HOLDS | ig34_p0210.txt:34-35 + 渲染页 210 Row 16 (CPORRESU、CPSTRESU 为空)；CP/examples.md:48 为 `0.62 \| \| 0.62 \| \| 0.62`，共 19 格，和表头一致 | — |
| 42 | ig34_p0225_a017 | VALUE_DIFF | EQUIVALENT | HOLDS | ig34_p0225.txt:52-61 + 渲染页 225 (Example 2 gf.xpt 的 3 行)；domains/GF/examples.md:62-66，在 `## Example 2` (第 50 行) 下，表头 29 列含 GFTSTDTL/GFSTREFC，3 行各值都一致 (REAL_TIME POLYMERASE CHAIN REACTION、2020-06-25、-3 等)。原子是图形式的摘要，表头写成 GFTSDTL/GFSTRESN，有抽错，KB 以表格完整承载 | — |

## 2. 计数

- HOLDS：21
- NOT_HOLD：0
- UNVERIFIABLE：0

## 3. 样本外发现的 KB 内容问题

无。

有两处不是 KB 内容问题，只是标签口径上的提示，供主控参考：

- **#37 和 #41 的原子本身抽错了**（#37 漏了 "2"/"1"；#41 多了一个空格），但终态标的是 EQUIVALENT / EXACT，而不是 ATOM_ERR。因为 KB 和 PDF 完全一致，按 brief 的定义这两个终态都成立；只是同类情况在 #39 标的是 ATOM_ERR，口径不统一。
- **#23、#24 的 CRF 勾选符**：KB 用 `( )` / `[ ]` 表示 PDF 里的 ○ / □。这和 commit bc4e42e 里 "CRF ○□ deferred to T4" 的说法对应。这里按信息等价判了 HOLDS；如果之后决定 KB 要逐字还原这两个符号，这两条的终态需要重新看。
