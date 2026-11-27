# T4.1 第二轮补检 — PDF_TYPO 层 包 7 (R116-R135) 独立审查结果

- 审查者: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T05:37:05Z (`date -u` 实取)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` 背景/判定口径 + `subagent_prompts/t4/t4_supp_round2_v1.0.md` § PDF_TYPO (HOLDS = ① PDF 该处确有登记问题 ② KB 与登记 handling 一致 ③ 其余内容 KB=PDF)
- 看过的渲染页: SDTMIG v3.4 p355, p356 (Read pages 参数; 核 TR Ex2 Row/TRSEQ 跳 12、各格列归属、p356 续行 TRREASND "POOR IMAGEQUALITY")
- 用过的命令:
  - 登记读取: `python3 -c "...json.loads(l) for l in open('t2_pdf_typo_registry.jsonl') if id in ids..."` (15 个 id 全取)
  - 句子类逐词比对 (引号/空白/`**`/`|`/`•` 归一后 difflib 词级 opcodes): `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/r2_p2/cmp.py`
  - 表格: `cat work/pdf_pages/ig34_p0355.txt`, `head -30 ig34_p0356.txt`, `sed -n 12,30p ig34_p0419.txt` 对 `sed -n 1,50p knowledge_base/domains/TR/examples.md`、`sed -n 40,58p knowledge_base/domains/TS/assumptions.md` 逐格比
  - 登记依据旁证: `grep -n FAEV ig34_p0373.txt ig34_p0374.txt`; `grep -ln OUTMSPRI ig34_p04*.txt` (p420); `grep -n "Associated Persons\|Section 4" sv20_p0005/6/8.txt`; `grep -rn "Trial Sets" sv20_p005*.txt`
  - R130 登记归属: `t3_writeback_decisions.json` 查 `ig34_p0355_a027` / `a015` 的 `evidence.registry`

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| R116 | `ig34_p0372_a013` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0372.txt:16-17`; `domains/FA/examples.md:183` | 登记 `B-FA T-8`: PDF "used to populated FADTC" 确有; KB "populate"; 词级比对仅此 1 处差异 |
| R117 | `ig34_p0373_a013` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0373.txt:18` (表头 :27 及 p374:1 均为 FAEVLINT); `domains/FA/examples.md:228` | 登记 `B-FA T-9`: 叙述 FAEVINTX vs 同例表列 FAEVLINT 确有不一致; KB FAEVLINT; 其余逐词一致 |
| R118 | `ig34_p0419_a006` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0419.txt:16-17`; `domains/TS/assumptions.md:43` | 登记 `B-TS T-2` ("Dose"→"DOSE", 表内为 DOSE) + `B-TS T-3` (DOSFREQ→DOSFRQ); 原子句内仅这 2 处差异, 均已登记 |
| R119 | `ig34_p0419_a011` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0419.txt:22`; `domains/TS/assumptions.md:48` | 登记 `B-TS T-3`: PDF 表行 `1 / A / DOSFREQ / Dosing Frequency / BID`; KB `1 / A / DOSFRQ / Dosing Frequency / BID`; 5 格中仅 TSPARMCD 差, 已登记 (pack 指针给的是 :43 叙述行, 实际表行在 :48) |
| R120 | `ig34_p0419_a017` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0419.txt:37-43` (OUTMSPRI 见 p420); `domains/TS/assumptions.md:57` | 登记 `B-TS T-4`: PDF "OUTMSPR"; KB "OUTMSPRI"; 其余逐词一致 |
| R121 | `ig34_p0016_a019` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0016.txt:22` (sv20 p53 §5.1.2 "Trial Sets"); `chapters/ch02_fundamentals.md:176` | 登记 `B-ch02 T-1`: "Trials Sets"→"Trial Sets"; 其余一致 |
| R122 | `ig34_p0218_a017` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0218.txt:26-28`; `domains/CP/examples.md:271` | 登记 `B-CP T-4`: 段末逗号→句点; 其余逐词一致 (含 PDF 原有 "REPNUM"、"used the same manner" 照录) |
| R123 | `ig34_p0237_a018` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0237.txt:36-39`; `domains/IS/examples.md:153` | 登记 `B-IS T-5`: KB 补 "in"; 其余逐词一致 |
| R124 | `ig34_p0355_a015` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0355.txt:29-30` + 渲染页 p355; `domains/TR/examples.md:31` | 登记 `B-TR T-1`: 渲染页确认 Row 11→13 跳 12; PDF Row/TRSEQ 14 → KB 13; 其余 21 格 (TARGET/A2/T04.2/DIAMETER/Diameter/7/mm/7/7/mm/空/空/PHOTOGRAPHY/INVESTIGATOR/40/WEEK 6/2010-02-20/48 等) 逐格一致 |
| R125 | `ig34_p0355_a016` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0355.txt:31-32` + 渲染页; `domains/TR/examples.md:32` | 登记 `B-TR T-1`: PDF 15 → KB 14; SUMDIAM / Sum of Diameter / 30 mm ×3 / TRLNKID、TRMETHOD、TRDTC、TRDY 空 逐格一致 |
| R126 | `ig34_p0355_a018` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0355.txt:37-38` + 渲染页; `domains/TR/examples.md:34` | 登记 `B-TR T-1`: PDF 17 → KB 16; LNSTATE / Lymph Node State / PATHOLOGICAL (ORRES、STRESC) / 单位与 STRESN 空 逐格一致 |
| R127 | `ig34_p0355_a021` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0355.txt:48-51` + 渲染页; `domains/TR/examples.md:37` | 登记 `B-TR T-1`: PDF 20 → KB 19; PCNSD / Percent Change Nadir in Sum of Diam / -52 % ×3 逐格一致 |
| R128 | `ig34_p0355_a022` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0355.txt:52-53` + 渲染页; `domains/TR/examples.md:38` | 登记 `B-TR T-1`: PDF 21 → KB 20; NON-TARGET/A2/NT01/TUMSTATE/Tumor State/PRESENT/PRESENT/CT SCAN/INVESTIGATOR/40/WEEK 6/2010-02-18/46 逐格一致 |
| R129 | `ig34_p0355_a026` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0355.txt:60-61` + 渲染页; `domains/TR/examples.md:42` | 登记 `B-TR T-1`: PDF 25 → KB 24; A3/T03/DIAMETER/NOT DONE/SCAN NOT PERFORMED/MRI/60/WEEK 12, 结果与日期格空 逐格一致 |
| R130 | `ig34_p0355_a027` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0355.txt:62-63` + `ig34_p0356.txt:2-3` + 渲染页 p355/p356; `domains/TR/examples.md:43` | 登记 `B-TR T-3`: 该行 TRREASND 跨页, p356 续行 "POOR IMAGEQUALITY" (缺空格) 确有; KB "NOT ASSESSABLE: POOR IMAGE QUALITY"。另: Row/TRSEQ PDF 26 → KB 25 属 `B-TR T-1` (该登记 32 格覆盖 KB r12-r27), 但本原子 decisions `evidence.registry` 只列 T-3, 未列 T-1 — 差异已登记, 不影响判定, 仅指针不全。其余格 (A3/T04/DIAMETER/NOT DONE/PHOTOGRAPHY/INVESTIGATOR/60/WEEK 12) 一致 (pack 给的 KB :43 正确) |
| R131 | `ig34_p0363_a008` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0363.txt:19-23`; `domains/FA/assumptions.md:50` | 登记 `B-FA T-5`: "(e.g," → "(e.g.,"; 其余逐词一致 (项目符号 • → `-`) |
| R132 | `ig34_p0412_a009` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0412.txt:16-17`; `domains/TD/examples.md:40` | 登记 `S-TDM TD T-1`: "assessments.." → 单句点; KB 行 40 即该句所在段, 定位正确; 其余一致 |
| R133 | `ig34_p0414_a006` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0414.txt:9-11`; `domains/TD/examples.md:153` | 登记 `S-TDM TD T-2`: "restarted)." → "restarted."; KB 行 153 即该段, 定位正确; 其余一致 |
| R134 | `ig34_p0436_a022` | PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0436.txt:46-50`; `chapters/ch08_relationships.md:328` | 登记 `B-ch08 T-6`: "coded)." → "coded."; 第 1 列 "Is verbatim text collected and then coded?" 与第 2 格首个 bullet 其余逐词一致 (同格第二个 bullet "A No answer…" 不属本原子) |
| R135 | `sv20_p0006_a020` | PDF_TYPO | PDF_TYPO | HOLDS | `sv20_p0006.txt:36` (p5:22,24 及 p8:22 均 "Section 4, Associated Persons Data"); `model/01_concepts_and_terms.md:94` | 登记 `B-model01 T-1`: "Section 3"→"Section 4"; 其余逐词一致 |

## 计数

| 判定 | 数 |
|---|---|
| HOLDS | 20 |
| NOT_HOLD | 0 |
| UNVERIFIABLE | 0 |

层 (PDF_TYPO, 本包 20 条): NOT_HOLD 0, UNVERIFIABLE 0。

## 附注 (不影响判定)
- R130 `ig34_p0355_a027`: decisions `evidence.registry` 仅 `["B-TR T-3"]`, 漏列同样作用于本原子 Row/TRSEQ 格的 `B-TR T-1`; 建议补全指针 (台账不由本审查改)。
- R119 / R124-R129 pack 自动给的 KB 行号是登记的 `kb_line_now` (TS :43 / TR :30), 除 R130 外与原子实际所在行不同; 实际行已在上表列出。

## 样本外发现的 KB 内容问题
无。
