# T4.1 补检 — 包 5/8 (TRIAGE_ATOM_ERR, 全局 #109-#132) 审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus, 只读独立审查; 与 T1/T2/T3 及总闸角色不同)
- 时间: 2026-11-27T04:53:53Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 判定口径: `.work/10_tier_b_repair/subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` (ATOM_ERR 两半都核: ① 原子 ≠ PDF; ② KB = PDF; 表格行逐格)
- 看过的渲染页 (SDTMIG v3.4 `source/cdisc/SDTMIG v3.4 (no header footer).pdf`): p170 (Read pages), p192 (Read pages), p226 (pdftoppm -r 300, 切 6 块逐块看), p389 (pdftoppm -r 250 整页)
- 文本层: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0169.txt`, `ig34_p0170.txt`, `ig34_p0192.txt`, `ig34_p0226.txt`, `ig34_p0389.txt`
- 用过的命令 (临时文件均在 scratchpad `supp5/`, 未写仓库):
  - `pdftoppm -q -r 300 -f 226 -l 226 -x {0|1400|2800} -y {150|1250} -W 1450 -H 1150 -png -singlefile "source/cdisc/SDTMIG v3.4 (no header footer).pdf" <scratch>/c226_XX`
  - `pdftoppm -r 250 -f 389 -l 389 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" <scratch>/p389`
  - `grep -n "" knowledge_base/domains/HO/examples.md`; `grep -n "STUDY01 | EG | 2324-P0001 | [3-7] |" knowledge_base/domains/EG/examples.md`; `grep -n "EX1 | TA\|Run-In\|^## " knowledge_base/domains/TA/examples.md`
  - `python3 -I <scratch>/scripts/gf_cmp.py`: 按 p226 渲染页**人工转录**的 32 列 × 16 行 + 表头, 与 `knowledge_base/domains/GF/examples.md` 第 86 行起的表逐格精确比对 → 表头 + 16 行全部 OK (0 差异)
  - `grep -n "REHABILIATION\|p0170\|p0226\|p0192\|p0389" .work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl`

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| 109 | `ig34_p0169_a0029` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | PDF 渲染 p170 Ex1 ho.xpt row 10 / `ig34_p0170.txt:13`; KB `knowledge_base/domains/HO/examples.md:30` | ① 原子 HOENDTC=`2011-10-16`, PDF=`2011-10-15`; 原子多一空列 (HOTERM 后 `\| \|`); 另原子页号记为 p169, 但该表行实际在 p170 (p169 只有 Ex1 叙述 Rows 1-8). ② KB 10 格 = PDF (ABC/HO/ABC123105/2/HOSPITAL/TREATMENT/2011-10-11/2011-10-15/HODUR 空) |
| 110 | `ig34_p0170_a0004` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p170 Ex2 ho.xpt 表头 / `ig34_p0170.txt:38`; KB `HO/examples.md:61` | ① 原子在 HOTERM 后多一空列, 且 `HOSTRTPT` ≠ PDF `HOENRTPT`. ② KB 表头 11 列 = PDF |
| 111 | `ig34_p0170_a0006` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p170 Ex2 row 2 / `ig34_p0170.txt:40`; KB `HO/examples.md:64` | ① 原子 HOTERM=`INTENSIVE CARE UNIT`/HOSTDTC=`2011-06-10 T 10:00`/HOENDTC=`2011-06-10` + 多空列; PDF = `ICU`/`2011-06-08T11:00`/`2011-06-09T14:30`. ② KB 逐格 = PDF (HOENRTPT/HOENTPT 空) |
| 112 | `ig34_p0192_a006` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p192 row 4 / `ig34_p0192.txt:9-10`; KB `knowledge_base/domains/EG/examples.md:106` (Example 4) | ① 原子 EGTEST=`RR Interval, Single Beat Measurement`, PDF=`RR Interval, Single Measurement` (渲染页确认无 Beat). ② KB 22 格 = PDF (679/msec/679/679/msec/12 LEAD STANDARD/LEAD II/空/1/SCREENING/-7/2014-02-11T14:32:13.3) |
| 113 | `ig34_p0192_a009` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p192 row 7 / `ig34_p0192.txt:15-16`; KB `EG/examples.md:109` | ① 同 112, 原子多 `Beat`. ② KB 逐格 = PDF (661…; EGDTC 2014-02-11T15:32:14.2) |
| 114 | `ig34_p0226_a008` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 gf.xpt 表头; KB `knowledge_base/domains/GF/examples.md:86` | ① 原子缺 SPDEVID、GFSTRESN; `GFSRPD`≠GFGRPID, `GFTSTOTL`≠GFTSTDTL, `GFORRESC`≠GFORRESU, `GFSEMREF`≠GFGENREF, `GFCHRCN`≠GFCHROM, `GFSTMYTP`≠GFSYMTYP. ② KB 32 列表头 = PDF (脚本比对 OK) |
| 115 | `ig34_p0226_a009` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 1; KB `GF/examples.md:88` | ① 原子缺 SPDEVID/GFGRPID 值, `ABU3908AS2`(PDF `ABU3908A52`), `1s37d5`(PDF `hs37d5`), GFCHROM 空 (PDF 7), `ENST00000466554.1`(PDF `ENST00000646664.1`), `.fasta.gz`(PDF `.fastq.gz`), VISITDY 空 (PDF 1). ② KB 32 格 = PDF |
| 116 | `ig34_p0226_a010` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 2; KB `GF/examples.md:89` | ① 同 115 系统性错 + GFORRESU `-MBP` / GFSTRESU `MBP` (PDF 均 `/MBP`). ② KB 逐格 = PDF |
| 117 | `ig34_p0226_a011` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 3; KB `GF/examples.md:90` | ① 同 115 + 单位 `71P4` (PDF `/10^6`). ② KB 逐格 = PDF |
| 118 | `ig34_p0226_a012` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 4; KB `GF/examples.md:91` | ① 同 116 (`-MBP`/`MBP`). ② KB 逐格 = PDF |
| 119 | `ig34_p0226_a013` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 5; KB `GF/examples.md:92` | ① 同 115 + 缺 GFSTRESN 格 (原子 `0.37 \| % \| 0.37 \| %`, PDF 0.37/%/0.37/0.37/%). ② KB 逐格 = PDF |
| 120 | `ig34_p0226_a014` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 6; KB `GF/examples.md:93` | ① 同 115 系统性错. ② KB 逐格 = PDF (GFSTRESN/GFSTRESU 空, 与渲染页一致) |
| 121 | `ig34_p0226_a015` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 7; KB `GF/examples.md:94` | ① 同 115 + `ENST00000396615.5` (PDF `ENST00000396861.5`), 缺 GFSTRESN. ② KB 逐格 = PDF |
| 122 | `ig34_p0226_a016` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 8; KB `GF/examples.md:95` | ① 同 121 + `-MBP`/`MBP`. ② KB 逐格 = PDF |
| 123 | `ig34_p0226_a017` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 9; KB `GF/examples.md:96` | ① 同 121 + `71P4` (PDF `/10^6`). ② KB 逐格 = PDF |
| 124 | `ig34_p0226_a018` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 10; KB `GF/examples.md:97` | ① 同 122. ② KB 逐格 = PDF (521.716) |
| 125 | `ig34_p0226_a019` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 11; KB `GF/examples.md:98` | ① 同 121 (ABU3908AS2/1s37d5/ENST00000396615.5/fasta/缺 SPDEVID/VISITDY 空). ② KB 逐格 = PDF |
| 126 | `ig34_p0226_a020` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 12; KB `GF/examples.md:99` | ① 同 121. ② KB 逐格 = PDF (yes/空/yes/空/空) |
| 127 | `ig34_p0226_a021` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 13; KB `GF/examples.md:100` | ① 原子 GFGRPID=3 (PDF 1), 结果 `0.056299177` 丢负号 (PDF `-0.056299177`, 渲染页负号在单元格上一行), `GRCH38g12` (PDF `GRCh38.p12`), 缺 SPDEVID, VISITDY 空. ② KB 逐格 = PDF (GFCHROM/GFXFN 空, 与渲染页一致) |
| 128 | `ig34_p0226_a022` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 14; KB `GF/examples.md:101` | ① 同 127 (GFGRPID 3≠1, 丢负号 -0.046787999, GRCH38g12, 并少 GFCHROM 空格). ② KB 逐格 = PDF |
| 129 | `ig34_p0226_a023` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 15; KB `GF/examples.md:102` | ① 原子 GFTSTDTL=`GENETIC TRANSCRIPTION INDICATOR` (PDF `…INTERPRETATION`), GFANMETH=`GENE SIGNATURE` (PDF `IFN-1 GENE SIGNATURE`), GRCH38g12, 缺 SPDEVID. ② KB 逐格 = PDF |
| 130 | `ig34_p0226_a024` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p226 row 16 / `ig34_p0226.txt:58-59`; KB `GF/examples.md:103` | ① 原子 GFTSTDTL=`GENETIC TRANSCRIPTION SCORE` (PDF `SCORE`), GFORRES 空 + 值 `1.120819661` (PDF `-1.126819661`), GFANMETH `8N-1 GENE SIGNATURE` (PDF `IFN-1 …`). ② KB 逐格 = PDF |
| 131 | `ig34_p0389_a012` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p389 ta.xpt row 2 / `ig34_p0389.txt:27`; KB `knowledge_base/domains/TA/examples.md:154` | ① 原子 TABRANCH 空, PDF=`Randomized to Placebo`. ② KB 11 格 = PDF. 注: 包给的 KB 指针 (`TA/examples.md:123`, Mermaid) 偏, 实际承载在 154 行 |
| 132 | `ig34_p0389_a013` | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | 渲染 p389 row 3 / `ig34_p0389.txt:28`; KB `TA/examples.md:155` | ① 原子 TABRANCH=`Randomized to Placebo`, PDF 空 (原子把 row 2 的值错挪到 row 3). ② KB 11 格 = PDF (TABRANCH/TATRANS 空, TREATMENT). 包给的指针 124 行偏, 实际 155 行 |

## 计数

| 层 | 条数 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE |
|---|---|---|---|---|---|
| TRIAGE_ATOM_ERR | 24 | 24 | 0 | 0 | 0 |
| 合计 | 24 | 24 | 0 | 0 | 0 |

层通过条件 (NOT_HOLD 0 且 UNVERIFIABLE 0): **满足**.

附记 (不影响判定):
- #109 原子页号 p169 与实际 p170 不符, 属原子抽取层的另一处错, 不影响 ATOM_ERR 成立.
- #131/#132 样本包自动 KB 指针指向 Mermaid 图区块 (123/124 行), 真正承载行是 154/155; 台账 kb_loc 若沿用 123/124, 建议后续核正 (只记录).

## 样本外发现的 KB 内容问题

无新问题. 顺带核对: `knowledge_base/domains/HO/examples.md:25` 写 `REHABILITATION FACILITY`, PDF p170 Ex1 row 5 为 `REHABILIATION FACILITY` — 已登记 PDF 笔误 `B-HO T-1` (`.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl:98`, handling "KB 写正确值"), 按登记处理, 不算问题.
