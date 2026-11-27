# T4.1 第二轮补检 — TYPO_SIB 包 5 (R78-R90) 独立审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:38:27Z (`date -u`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round2_v1.0.md` (TYPO_SIB 层)
- 看过的渲染页: SDTMIG v3.4 p277、p278 (Read pages)；p357 上半页 (pdftoppm -r 220 裁切)；p147 (pdftoppm -r 250 整页 + 下半页裁切)。其余页 (p262/263/266/267/279/280/281/420/421/433) 用文本层判定, 文本层列对齐清楚、无歧义。
- 用过的命令 (均只读; 图片输出到 scratchpad `r2_s3/`):
  - `grep -E '"id": ?"(B-MB T-1|B-MI T-1|B-PCPP T-[123]|S-SPC2 PCPP T-11|B-TR T-2|B-TS T-1|B-SUPPQUAL T-1|B-BE T-3)"' work/t2_pdf_typo_registry.jsonl`
  - `cat -n work/pdf_pages/ig34_p0{147,262,263,277,278,279,281,421}.txt`; `grep -n 'MIDRV' ig34_p026[5-8].txt`; `grep -n 'llustrat' ig34_p043[2-4].txt`; `grep -n 'through' ig34_p0280.txt`
  - `python3` 读 `work/pdf_atoms.jsonl` 取 p277/p278/p279/p147 原子 verbatim
  - KB: `sed -n` `knowledge_base/domains/{MB,PC,TS,MI,TR,BE}/examples.md`; `grep -rn` `Rows 18-29` / `llustrat` / `298B1-1R` / `298R1-1R0`
  - `pdftoppm -r 220 -f 357 -l 357 -x 0 -y 0 -W 2700 -H 1000 -png`; `pdftoppm -r 250 -f 147 -l 147 [-x 0 -y 750 -W 1800 -H 1200] -png`
  - `grep -E '"ig34_p0147_a02[56]"' work/coverage_ledger.wc.jsonl`

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| R78 | `ig34_p0263_a013` | TYPO_SIB | EXACT | NOT_AFFECTED | `ig34_p0263.txt:15` (Ex3 relrec r5 `5 ABC MB MBREFID ONE C`); `knowledge_base/domains/MB/examples.md:228` | 登记 B-MB T-1 的跳号在 **p262** suppmb 表 (Row 列印 1,2,3,4,7,8; `ig34_p0262.txt:22-27`), KB `MB/examples.md:204-205` 写 5/6。本原子是 p263 relrec 第 5 行, PDF 本来就印 "5", KB 逐格一致 (USUBJID / IDVARVAL / RELTYPE 空格一致)。 |
| R79 | `ig34_p0266_a016` | TYPO_SIB | EXACT | NOT_AFFECTED | `ig34_p0266.txt:25` (Ex2 表头含 `MIDRVFL`); `knowledge_base/domains/MI/examples.md:27` | 登记 B-MI T-1 的 `MIDRVL` 在 **p267** Ex3 表头 (`ig34_p0267.txt:8`, KB `MI/examples.md:50`)。本原子是 p266 Ex2 表头, PDF 印 MIDRVFL, KB 18 列逐字一致。 |
| R80 | `ig34_p0277_a025` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | `ig34_p0277.txt:26` + 渲染 p277 (Method A r2 `PP / PPGRPID / DY1DRGX / 1`); `knowledge_base/domains/PC/examples.md:78` | 候选登记 T-2/T-3 是 **p278** Method B r13/r26 的 RDOMAIN。本原子是 p277 Method A 第 2 行, PDF 与 KB 逐格一致。注: 包里 KB 指针 (`PP/examples.md:14-17`) 是误定位, 实际承载在 `PC/examples.md` §6.3.5.9.3 段。 |
| R81 | `ig34_p0277_a026` | TYPO_SIB | EQUIVALENT | **TYPO_AFFECTED** | `ig34_p0277.txt:27` + 渲染 p277: Method A r3 印 `PC … PPGRPID DY8_DRGX … 2`; `knowledge_base/domains/PC/examples.md:79` 写 `PCGRPID` | 登记 `B-PCPP T-1`。PDF 片段 "3 ABC-123 PC ABC-123-0001 PPGRPID DY8_DRGX"; KB 改为 PCGRPID, 其余格一致。原子 verbatim 已被抽取时 "顺手改对" 成 PCGRPID。 |
| R82 | `ig34_p0278_a015` | TYPO_SIB | EQUIVALENT | **TYPO_AFFECTED** | `ig34_p0278.txt:15` + 渲染 p278: Method B r13 印 `PC … PPGRPID DY1DRGX … 1`; `knowledge_base/domains/PC/examples.md:103` 写 RDOMAIN `PP` | 登记 `B-PCPP T-2`。PDF 片段 "13 ABC-123 PC ABC-123-0001 PPGRPID DY1DRGX"; KB 只改 RDOMAIN, 其余格 (IDVARVAL DY1DRGX / RELID 1) 与 PDF 一致。 |
| R83 | `ig34_p0278_a028` | TYPO_SIB | EQUIVALENT | **TYPO_AFFECTED** | `ig34_p0278.txt:28` + 渲染 p278: Method B r26 印 `PC … PPGRPID DY1DRGX … 1`; `knowledge_base/domains/PC/examples.md:116` 写 RDOMAIN `PP` | 登记 `B-PCPP T-3`。PDF 片段 "26 ABC-123 PC ABC-123-0001 PPGRPID DY1DRGX"; KB 只改 RDOMAIN, IDVARVAL (DY1DRGX) 与 RELID (1) 照 PDF (见样本外发现 1)。 |
| R84 | `ig34_p0278_a042` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | `ig34_p0278.txt:46` + 渲染 p278 (Method C r9 `PC PCGRPID DY8_DRGX 2`); `knowledge_base/domains/PC/examples.md:135` | 登记 T-1 是 p277 Method A r3 (见 R81)。本原子是 p278 Method C 第 9 行, PDF 本来就印 PCGRPID, KB 逐格一致。 |
| R85 | `ig34_p0279_a007` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | `ig34_p0279.txt:8` (Method D r13 `PP PPSEQ 1 1`); `knowledge_base/domains/PC/examples.md:165` | 登记 T-2 是 p278 Method B r13。本原子是 p279 Method D r13 (行号相同但不同表), PDF 印 PP, KB 一致。 |
| R86 | `ig34_p0281_a047` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | `ig34_p0281.txt:56-57` (Ex3 Method D "Rows 18-29 … "1" through "7" …", 引号完整); `knowledge_base/domains/PC/examples.md:354` | 登记 S-SPC2 PCPP T-11 的引号错位在 **p280** Ex2 Method D (`ig34_p0280.txt:18` `"1 through "7"`), KB `PC/examples.md:250`。本原子 PDF 引号正确, KB 354 行与 PDF 逐字一致 (仅换行合并 + 列表符)。包内 "KB 现文 (无)" 是未定位, KB 实有。 |
| R87 | `ig34_p0357_a014` | TYPO_SIB | EQUIVALENT | **TYPO_AFFECTED** | `ig34_p0357.txt:34` + 渲染 p357 裁切: Ex3 r15 TRORRES -50 / TRSTRESC **-60** / TRSTRESN -50; `knowledge_base/domains/TR/examples.md:84` TRSTRESC 写 `-50` | 登记 `B-TR T-2`。PDF 片段 "PCBSD … -50 % -60 -50 %"; 其余格 (TRTEST 全称、ACE IMAGING、INDEPENDENT ASSESSOR、RADIOLOGIST 1、40、WEEK 6, 空 TRLNKID/TRMETHOD/日期/DY) 一致。原子 verbatim 保留了 -60 (此条抽取未被改对)。 |
| R88 | `ig34_p0357_a015` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | `ig34_p0357.txt:39-42` (Ex3 r16 PCNSD `-50 % -50 -50 %`); `knowledge_base/domains/TR/examples.md:85` | 笔误在相邻的 r15 (R87)。r16 PDF 三值都是 -50, KB 逐格一致。 |
| R89 | `ig34_p0420_a019` | TYPO_SIB | EXACT | NOT_AFFECTED | `ig34_p0420.txt:25-27` (Ex1 r14 `TITLE Trial Title …`); `knowledge_base/domains/TS/examples.md:24` | 登记 B-TS T-1 的 "Trial Type" 在 **p421** Ex2 r1 (`ig34_p0421.txt:41`, KB `TS/examples.md:76`)。本原子是 p420 Ex1 r14, PDF 印 Trial Title, KB 逐格一致 (TSVAL 换行合并)。 |
| R90 | `ig34_p0433_a030` | TYPO_SIB | EQUIVALENT | NOT_AFFECTED | `ig34_p0433.txt:43` ("This example illustrates how the language …"); `knowledge_base/domains/SUPPQUAL/examples.md:20`, `knowledge_base/chapters/ch08_relationships.md:241` | 登记 B-SUPPQUAL T-1 的 "llustrate" 在同页 **第 28 行** 另一句 ("These examples llustrate how a set of SUPP-- …")。本句 PDF 印 illustrates, KB 两处逐字一致。 |

## 计数 (TYPO_SIB 层, 本包 13 条)

| 判定 | 条数 | 编号 |
|---|---|---|
| TYPO_AFFECTED | 4 | R81, R82, R83, R87 |
| NOT_AFFECTED | 9 | R78, R79, R80, R84, R85, R86, R88, R89, R90 |
| NOT_HOLD | 0 | — |
| UNVERIFIABLE | 0 | — |

本包无 UNVERIFIABLE / NOT_HOLD。TYPO_AFFECTED 4 条按 brief 后果并入待改标签清单 (现标签 EQUIVALENT → 应为 PDF_TYPO), 交主人裁定。

## 反向核对: 登记 B-BE T-3 实际影响的全部表格行 (PDF p147)

登记: `pdf_value` = "Ex2 bs r3-4 BSREFID 298B1-1R0", `kb_value` = "298R1-1R0", note "2 格 (bs r3/r4)"。

逐表核对 p147 (文本层 `ig34_p0147.txt` + 渲染页 p147 250dpi) 与 `knowledge_base/domains/BE/examples.md`, 以及 p146 be 表:

| 表 | 行 | PDF 印 | KB 写 | 受影响? | atom_id |
|---|---|---|---|---|---|
| bs.xpt | r3 (BSREFID) | `298B1-1R0` (`ig34_p0147.txt:30`) | `298R1-1R0` (`BE/examples.md:124`) | **是** | `ig34_p0147_a025` |
| bs.xpt | r4 (BSREFID) | `298B1-1R0` (`ig34_p0147.txt:31`) | `298R1-1R0` (`BE/examples.md:125`) | **是** | `ig34_p0147_a026` |
| suppbe.xpt | r3 IDVARVAL | `298R1-1R0` (`:15`) | `298R1-1R0` (`:105`) | 否 (PDF 本来正确) | `ig34_p0147_a013` |
| relspec.xpt | r3 REFID; r4-r6 PARENT | `298R1-1R0` (`:42-45`) | `298R1-1R0` (`:140-143`) | 否 | `ig34_p0147_a036`..`a039` |
| be.xpt (p146) | r4 BEREFID | `298R1-1R0` (`ig34_p0146.txt:39`) | `298R1-1R0` (`:85`) | 否 | (p146 原子, 不在本页) |

全文 grep: PDF p144-p148 中 `298B1-1R` 只出现在 bs r3、r4 两处; KB 中 `298B1-1R` 0 处。登记 `span_lines_in_file` 列的 85/105/140-143 只是 KB 同串出现位置, 不是笔误影响位置。

**结论: B-BE T-3 影响 2 个原子 = `ig34_p0147_a025` (bs r3) 与 `ig34_p0147_a026` (bs r4)。** 台账 (`coverage_ledger.wc.jsonl`) 里两者现均为 `EXACT`; 前一位审查者只点了 a025, **a026 (bs r4, RIN 行) 同样受影响, 尚未被确认**, 应一并进待改标签清单。

附带: `ig34_p0147_a025` 的原子 verbatim 本身另有抽错 (BSSTRESC / BSSTRESN 抽成空, PDF 与 KB 均为 6 / 6); `ig34_p0147_a024` verbatim 的 BSREFID 抽成 `298B1` 且 STRESC/STRESN 为空 (PDF 与 KB 为 `298B1-1`, 6, 6)。这只是原子抽取物问题, KB 按 PDF 写对, 不影响上面结论。

## 样本外发现 (只记录, 不修)

1. PDF p278 Method B relrec (`ig34_p0278.txt:16-28`, 渲染页确认): 叙述写 "Rows 14-26 … RELID "2" … PPGRPID = "DY8DRGX"", 但表 r14-r26 的 RELID 全印 1, r26 IDVARVAL 印 DY1DRGX。KB `PC/examples.md:104-116` 照 PDF 录 (RELID 1、DY1DRGX), 只按登记 T-3 改了 r26 RDOMAIN。这处 PDF 内部矛盾未见登记 (KB 与 PDF 一致, 不构成样本 NOT_HOLD); 是否补登记由主控定。
2. `knowledge_base/chapters/ch08_relationships.md:228` 也承载 p433 第 28 行那句, 写的是改正值 "illustrate"; 登记 B-SUPPQUAL T-1 的 `span_lines_in_file` 只列 `SUPPQUAL/examples.md` 的 5/20, 未列 ch08:228。对应原子 (p433 那一句) 若映射到 ch08, 也属该登记影响范围, 建议主控核对其标签。
3. 包内 R80-R85 的 "KB 现文" 指针指向 `knowledge_base/domains/PP/examples.md` (近似定位), 实际承载在 `knowledge_base/domains/PC/examples.md` §6.3.5.9.3 (行 60-190); 内容本身无误。
