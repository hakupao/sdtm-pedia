# T4 加查 ATOM_ERR (S1-R1) — 包 2 (E22-E42) 全检结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 新实例, 只读
- 日期时间: 2026-11-27T14:11:56Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- brief: `.work/10_tier_b_repair/subagent_prompts/t4/t4_atomerr_s1r1_v1.0.md` + `t4_supp_fullcheck_v1.0.md` (背景 / 判定口径)
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`, Read 工具 `pages`): 154, 155, 161, 167, 169, 179, 190, 199, 236, 238, 240, 241, 257, 258; 另 p241 SUPPIS 行用 `pdftoppm -r 400 -f 241 -l 241 -x 2300 -y 2060 -W 900 -H 110 -png` 放大 (输出在会话临时目录, 不在仓库)
- 用过的命令: `sed -n` 读 `work/pdf_pages/ig34_p0154/0190/0238/0240/0257.txt`; `grep -n` 在 `knowledge_base/domains/{CE,DS,HO,DV,EG,BS,IS,MS,MB}/*.md` 定位各行与表头; `grep -n` 查 `work/t2_pdf_typo_registry.jsonl`; `sed -n 29,30p ig34_p0169.txt / grep -o / xxd` 查连字符字节 (U+2011)
- 方法: 每条先对 PDF 渲染页 (表格行按表头逐格) 定 PDF 原文, 再与原子逐格比 (①), 再到所属 KB 文件 Grep 到实际行逐格比 (②). 包里 KB 指针 E22-E25、E36 偏了, 以下给的是自己定位到的行.

## 逐条判定

| # | atom_id | 判定 | ① 原子 vs PDF (差在哪; PDF 文件:行 或 渲染页) | ② KB vs PDF (KB 文件:行) | 说明 |
|---|---|---|---|---|---|
| E22 | `ig34_p0154_a0015` | HOLDS | 原子 USUBJID "ABC-US-701-002"; PDF 渲染页 154 ce.xpt Row 3 印 "ABC -US-701-002" (连字符前有可见空格; 文本层 `ig34_p0154.txt:24-25` 同). 值类代码少 1 个字符, 其余 16 格一致 | `knowledge_base/domains/CE/examples.md:125` 17 格逐格 = PDF (USUBJID 带空格; CEDTC 2006-10-23, CESTDTC 空, 与渲染页一致) | 包指针 `CE/examples.md:101` 是 MH 行, 偏. 关联登记 B-CE T-2 (handling 照录+T4): KB = PDF, 不属 KB≠PDF 情形. 注: 空格在代码值内部, 按 "值类一字符都要对" 计为原子差异, 非空白归一 |
| E23 | `ig34_p0154_a0029` | HOLDS | 原子 USUBJID "ABC-US-701-002"; PDF 渲染页 154 pr.xpt Row 1 "ABC -US-701-002" (`ig34_p0154.txt:44`). 其余 11 格一致 | `knowledge_base/domains/CE/examples.md:148` 12 格 = PDF | 包指针 :101 偏. 关联登记 B-CE T-2 (照录, KB = PDF) |
| E24 | `ig34_p0154_a0030` | HOLDS | 原子 USUBJID "ABC-US-701-002"; PDF 渲染页 154 pr.xpt Row 2 "ABC -US-701-002" (`ig34_p0154.txt:45`). 其余格一致 | `knowledge_base/domains/CE/examples.md:149` 12 格 = PDF | 包指针 :101 偏. 关联登记 B-CE T-2 (照录, KB = PDF) |
| E25 | `ig34_p0155_a0002` | HOLDS | 原子 USUBJID "ABC-US-701-002"; PDF 渲染页 155 pr.xpt Row 3 "ABC -US-701-002" (`ig34_p0155.txt:2`). 其余格一致 | `knowledge_base/domains/CE/examples.md:150` 12 格 = PDF | 包指针 :101 偏. 关联登记 B-CE T-2 (照录, KB = PDF) |
| E26 | `ig34_p0161_a0012` | HOLDS | 原子 "no record for DSCAT = "LEVOFLOXACIN""; PDF 渲染页 161 Row 1 印 "DSSCAT = "LEVOFLOXACIN"" (`ig34_p0161.txt:19`). 另 PDF 印 "first treatment epocch", 原子写 "epoch" | `knowledge_base/domains/DS/examples.md:120` 写 DSSCAT, 其余逐字 = PDF (PDF 的 **treatment** 粗体 KB 未加粗, 属归一); 唯一差 "epoch" vs PDF "epocch" | 涉登记 B-DS T-4: PDF 印 "epocch", KB 写 "epoch", 登记 handling "KB 写正确值". 原子与 PDF 的实质差 = DSCAT vs DSSCAT |
| E27 | `ig34_p0167_a0010` | HOLDS | 原子表头第 5 列 "DSEQ"; PDF 渲染页 167 ds.xpt 表头 "DSSEQ" (`ig34_p0167.txt:13`). 其余 11 列一致 | `knowledge_base/domains/DS/examples.md:405` 12 列逐列 = PDF (含 TAETORD), 位于 p167 那张表 | — |
| E28 | `ig34_p0169_a0011` | HOLDS | 原子 "--BODYS"; PDF 渲染页 169 HO Assumption 5 印 "--BODSYS" (`ig34_p0169.txt:30`). 其余变量清单一致 | `knowledge_base/domains/HO/assumptions.md:23` 逐字 = PDF ("--BODSYS"; PDF 折行 "--/SMIE" KB 连写为 "--SMIE", 属空白归一) | PDF 文本层 --SER/--SDTH/--BODSYS/--LOC/--SEV 用 U+2011 不断行连字符, KB 全为 ASCII "-"; 渲染页上两者字形相同, 按 brief 以渲染页为准不计差异 |
| E29 | `ig34_p0179_a0018` | HOLDS | 原子 DVTERM "...NO DOSE CALL PERFORMED" 无句点; PDF 渲染页 179 dv.xpt Row 1 印 "...CALL PERFORMED." (`ig34_p0179.txt:34`). 其余 8 格一致 | `knowledge_base/domains/DV/examples.md:17` 9 格 = PDF (带句点) | — |
| E30 | `ig34_p0190_a011` | HOLDS | 原子 EGXFN "P0W436789-07.xml" 且 VISIT "Screening"; PDF 渲染页 190 eg.xpt Row 9 印 "PQW436789-07.xml" 与 "Screening 1" (折行) (`ig34_p0190.txt:19-20`) | `knowledge_base/domains/EG/examples.md:33` 24 格逐格 = PDF (PQW436789-07.xml; Screening 1; EGDY -36) | — |
| E31 | `ig34_p0199_a003` | HOLDS | 原子 VISITDY 空; PDF 渲染页 199 bs.xpt Row 1 VISITDY = "1" (`ig34_p0199.txt:3`). 其余 20 格一致 | `knowledge_base/domains/BS/examples.md:17` 21 格 = PDF (VISIT Baseline / VISITNUM 1 / VISITDY 1) | — |
| E32 | `ig34_p0199_a004` | HOLDS | 原子 VISITDY 空; PDF 渲染页 199 Row 2 VISITDY = "1" (`ig34_p0199.txt:6`) | `knowledge_base/domains/BS/examples.md:18` 21 格 = PDF | — |
| E33 | `ig34_p0199_a005` | HOLDS | 原子 VISITDY 空; PDF 渲染页 199 Row 3 VISITDY = "1" (`ig34_p0199.txt:9`) | `knowledge_base/domains/BS/examples.md:19` 21 格 = PDF | — |
| E34 | `ig34_p0199_a006` | HOLDS | 原子 VISITDY 空; PDF 渲染页 199 Row 4 VISITDY = "1" (`ig34_p0199.txt:12`) | `knowledge_base/domains/BS/examples.md:20` 21 格 = PDF | — |
| E35 | `ig34_p0236_a008` | HOLDS | 原子表头 21 列, ISCAT 后直接 ISORRES, 缺 "ISSCAT"; PDF 渲染页 236 is.xpt 表头 22 列含 ISSCAT (`ig34_p0236.txt:21`) | `knowledge_base/domains/IS/examples.md:113` 22 列逐列 = PDF (无 ISORRESU, 与 PDF 同) | — |
| E36 | `ig34_p0238_a005` | HOLDS | 原子 Row 1 的 ISSEQ = "3"; PDF 渲染页 238 is.xpt Row 1 ISSEQ = "1" (`ig34_p0238.txt:7`). 其余 22 格一致 (5.1 / BASELINE / 2017-05-27) | `knowledge_base/domains/IS/examples.md:162` 23 格 = PDF Row 1 | 包指针 :163-164 是 Row 2/3, 偏; 实际行 :162 |
| E37 | `ig34_p0240_a011` | HOLDS | 原子 Row 4 列错位: ISTSTOPO 空, ISORRES 写 "QUANTIFY", ISORRESU 写 "1:170", 只有 1 个 "170" (缺 ISSTRESN). PDF 渲染页 240 Row 4: ISTSTOPO QUANTIFY / ISORRES 1:170 / ISSTRESC 170 / ISSTRESN 170 / ISSTRESU titer | `knowledge_base/domains/IS/examples.md:225` 22 格逐格 = PDF Row 4 | — |
| E38 | `ig34_p0241_a022` | HOLDS | 原子 QVAL "CENTRAL CA. AREA 14"; PDF 渲染页 241 suppis 放大 400dpi 确认是逗号 "CENTRAL CA, AREA 14" (`ig34_p0241.txt:34` 同) | `knowledge_base/domains/IS/examples.md:275` 11 格 = PDF (逗号) | — |
| E39 | `ig34_p0257_a010` | HOLDS | 原子 Row 3 MSORRES 空、MSSTRESC 空; PDF 渲染页 257 ms.xpt Row 3 MSORRES "1", MSSTRESC "1" (`ig34_p0257.txt:16`). 其余格一致 | `knowledge_base/domains/MS/examples.md:25` 22 格 = PDF (MSCONC/MSCONCU 空; 1 / ug/dL / 1 / 1 / ug/dL) | — |
| E40 | `ig34_p0258_a019` | HOLDS | 原子 VISIT "VISIT"; PDF 渲染页 258 mb.xpt Row 1 VISIT "VISIT 1" (折行, `ig34_p0258.txt:24-25`) | `knowledge_base/domains/MB/examples.md:76` 17 格 = PDF (VISIT 1) | — |
| E41 | `ig34_p0258_a020` | HOLDS | 原子 VISIT "VISIT"; PDF 渲染页 258 Row 2 "VISIT 1" (`ig34_p0258.txt:26-27`) | `knowledge_base/domains/MB/examples.md:77` 17 格 = PDF (CELL COUNT / 2+ / FEW / VISIT 1) | — |
| E42 | `ig34_p0258_a021` | HOLDS | 原子 VISIT "VISIT"; PDF 渲染页 258 Row 3 "VISIT 1" (`ig34_p0258.txt:28-29`) | `knowledge_base/domains/MB/examples.md:78` 17 格 = PDF (GMNROD / VISIT 1) | — |

## 计数

- HOLDS: 21
- NOT_HOLD: 0
- UNVERIFIABLE: 0
- 涉登记 (KB≠PDF 由已登记 PDF 笔误造成): E26 (B-DS T-4)
- 关联登记但 KB = PDF (照录, 非 KB≠PDF 情形, 供主控知悉): E22, E23, E24, E25 (B-CE T-2)
- 没看渲染页只看文本层的编号: 无 (21 条全部看过渲染页)

## 判定口径提示 (非改判, 供复核者参考)

- E22-E25 的 ① 依赖一个口径: 原子把 USUBJID 内部的空格 ("ABC -US-") 去掉. 本审按 "值类一字符都要对" 计为原子与 PDF 不符, 而非 "空白归一". 若协调方认为代码值内部空格也属空白归一, 这 4 条的 ① 会变为不成立.
- E28 的 ② 依赖 "U+2011 与 ASCII 连字符在渲染页同形, 不计差异".

## 样本外发现的 KB 内容问题

无. (顺看 p236 Ex5 Row 6/7 PDF STUDYID 印 "RSC1230", KB `knowledge_base/domains/IS/examples.md:120-121` 写 "RSV1230", 已登记 B-IS T-1 / T-2, 不是新问题.)
