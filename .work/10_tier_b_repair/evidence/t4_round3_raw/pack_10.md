# T4.1 第三轮补检 — 包 10 (R3_PDF_TYPO, T226-T249, 24 条) 审查结果

- 审查者: `oh-my-claudecode:tracer` (opus), 只读角色
- 时间: 2026-11-27T06:40:40Z (`date -u`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` 的 R3_PDF_TYPO 层 (三件事: ① PDF 该处确有登记所说的问题; ② KB 现状与登记 handling 一致; ③ 其余内容 KB 与 PDF 一致)
- 看过的渲染页 (SDTMIG v3.4 物理页): 355, 356, 419, 457 (110 dpi); 412, 413, 414 (200 dpi 裁切)
- 用过的命令:
  - `pdftoppm -r 110 -f N -l N -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" <scratch>/pN` (N = 355 356 412 413 414 419 457); `pdftoppm -r 200` (412-414) + `sips -c` 裁切
  - `cat -n .work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` / `p0356` / `p0412` / `p0413` / `p0414`
  - `sed -n` / `grep -n` 看 KB: `domains/TR/examples.md:1-50`, `domains/SR/spec.md:326-342`, `domains/TD/examples.md:38-52,95-106,150-172`, `domains/TS/assumptions.md:41-52,113-116`, `chapters/ch08_relationships.md:30-46,222-229,371-374`, `domains/RELSUB/assumptions.md:27-30`, `chapters/ch10_appendices.md:350-353,383-389`
  - Python: 按 id 取 `work/t2_pdf_typo_registry.jsonl` 登记; 遍历 `work/coverage_ledger.wc.jsonl` 看 p355/356/412/413/414 各原子终态; 对句子类原子把 PDF 文本层 (去换行) 套用登记改正后检查是否为 KB 行子串 (difflib 列差异)
  - `grep -n '"Dose"\|DOSE' work/t2_pdf_typo_registry.jsonl`

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 | 说明 |
|---|---|---|---|---|---|---|
| T226 | `ig34_p0355_a017` | R3_PDF_TYPO | PDF_TYPO | HOLDS | PDF 渲染页 355 Row 16 (文本层 `ig34_p0355.txt:33-36`); KB `knowledge_base/domains/TR/examples.md:33` (KB Row 15) | 登记 `B-TR T-1`。① 渲染页确认 PDF Ex2 编号 11→13 跳过 12 (Row 与 TRSEQ 同跳); ② KB 连续编号, PDF Row/TRSEQ 16 → KB 15; ③ 其余 21 格 (ABC/TR/44444/TARGET/A2/空/SUMNLNLD/Sum Diameters of Non Lymph Node Tumors/18/mm/18/18/mm/空…/INVESTIGATOR/40/WEEK 6/空/空) 逐格一致。包内 KB 指针 (第 30 行) 偏, 实际对应第 33 行 |
| T227 | `ig34_p0355_a019` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染页 355 Row 18 (`ig34_p0355.txt:39-42`); KB `TR/examples.md:35` (KB Row 17) | `B-TR T-1`: 18→17; ACNSD / Absolute Change Nadir in Sum of Diam / -32 / mm / -32 / -32 / mm / INVESTIGATOR / 40 / WEEK 6 逐格一致 |
| T228 | `ig34_p0355_a020` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染页 355 Row 19 (`ig34_p0355.txt:43-47`); KB `TR/examples.md:36` (KB Row 18) | `B-TR T-1`: 19→18; PCBSD / Percent Change From Baseline in Sum of Diameter / -52 / % / -52 / -52 / % 等逐格一致 |
| T229 | `ig34_p0355_a023` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染页 355 Row 22 (`ig34_p0355.txt:54-55`); KB `TR/examples.md:39` (KB Row 21) | `B-TR T-1`: 22→21; NON-TARGET / A2 / NT02 / TUMSTATE / Tumor State / PRESENT / PRESENT / MRI / INVESTIGATOR / 40 / WEEK 6 / 2010-02-19 / 47 逐格一致 |
| T230 | `ig34_p0355_a024` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染页 355 Row 23 (`ig34_p0355.txt:56-57`); KB `TR/examples.md:40` (KB Row 22) | `B-TR T-1`: 23→22; TARGET / A3 / T01 / DIAMETER / Diameter / 0 / mm / 0 / 0 / mm / CT SCAN / INVESTIGATOR / 60 / WEEK 12 / 2010-04-02 / 88 逐格一致 |
| T231 | `ig34_p0355_a025` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染页 355 Row 24 (`ig34_p0355.txt:58-59`); KB `TR/examples.md:41` (KB Row 23) | `B-TR T-1`: 24→23; T02 / 6 / mm / 6 / 6 / mm / CT SCAN / … / WEEK 12 / 2010-04-02 / 88 逐格一致 |
| T232 | `ig34_p0356_a001` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染页 356 顶部续行 + Row 27 (`ig34_p0356.txt:2-5`), 渲染页 355 Row 26 (`ig34_p0355.txt:62-63`); KB `TR/examples.md:44` (KB Row 26), `TR/examples.md:43` (KB Row 25) | 登记 `B-TR T-3` (+ 应同时引 `B-TR T-1`)。① 渲染页: p356 表头下有一条无行号续行, TRREASND 格印 "POOR IMAGEQUALITY" (缺空格, T-3 成立), 该续行实为 PDF Row 26 "NOT ASSESSABLE:" 跨页续接 (KB Row 25 = "NOT ASSESSABLE: POOR IMAGE QUALITY", 已改正) — 本原子抽取把该续行并入 Row 27, 即原子 verbatim 行归属抽错, 但该片段在本原子 PDF 跨度内; ② KB 写正确值 "POOR IMAGE QUALITY" (位于 KB Row 25); ③ PDF Row 27 其余: Row/TRSEQ 27 → KB 26 (= 已登记 `B-TR T-1`), NON-TARGET / A3 / NT01 / TUMSTATE / Tumor State / TRSTAT·TRREASND 空 / CT SCAN / INVESTIGATOR / 60 / WEEK 12 / 2010-04-02 / 88 逐格一致。备注: 本原子登记指针只写 T-3, 应补 T-1 |
| T233 | `ig34_p0356_a002` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染页 356 Row 28 (`ig34_p0356.txt:6-7`); KB `TR/examples.md:45` (KB Row 27) | `B-TR T-1`: 28→27; NON-TARGET / A3 / NT02 / TUMSTATE / Tumor State / NOT DONE / SCAN NOT PERFORMED / MRI / INVESTIGATOR / 60 / WEEK 12 / 日期·DY 空 逐格一致 (原子 verbatim 列错位, 以 PDF 为准) |
| T234 | `ig34_p0362_a010` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0362.txt:47-52`; KB `knowledge_base/domains/FA/assumptions.md:39` | `B-FA T-4`: PDF "thought be related" 确在 (文本层 50 行); KB "thought to be related"; 套改正后 PDF 全文为 KB 行子串 |
| T235 | `ig34_p0363_a009` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0363.txt:24-26`; KB `domains/FA/assumptions.md:51` | `B-FA T-6`: "may provided" → "may provide"; 其余逐字 |
| T236 | `ig34_p0377_a015` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0377.txt:34-37`; KB `domains/SR/spec.md:329-336` | `B-SR T-4`: PDF 第一例 "indicated by EGTPTREF" 确在; KB 改 SRTPTREF; Label "Planned Elapsed Time from Time Point Ref" / Char / ISO 8601 duration / Timing / Perm / Notes 其余逐字一致 |
| T237 | `ig34_p0412_a006` | R3_PDF_TYPO | PDF_TYPO | NOT_HOLD | 渲染页 412 (`ig34_p0412.txt:14`); KB `domains/TD/examples.md:40` | ① 不成立: 登记 `S-TDM TD T-1` 的 "assessments.." 在下一句 "The offset variable … assessments.." (原子 `ig34_p0412_a009`), 本原子 "This example shows a study where … course of the study." PDF 无该问题。KB 逐字承载本句, KB 无错; 标签级别问题, 终态应为 EXACT (嵌在合并段落内) |
| T238 | `ig34_p0412_a007` | R3_PDF_TYPO | PDF_TYPO | NOT_HOLD | 渲染页 412 (`ig34_p0412.txt:14-15`); KB `TD/examples.md:40` | 同 T237: 本句 "In this example, there are 3 distinct disease-assessment schedule patterns." PDF 无登记笔误; KB 逐字。KB 无错, 终态应为 EXACT (T3 前即 EXACT) |
| T239 | `ig34_p0412_a008` | R3_PDF_TYPO | PDF_TYPO | NOT_HOLD | 渲染页 412 (`ig34_p0412.txt:15-16`); KB `TD/examples.md:40` | 同 T237: "A single anchor date variable (TDANCVAR) provides the anchor date for each pattern." PDF 无登记笔误; KB 逐字。KB 无错, 终态应为 EXACT |
| T240 | `ig34_p0413_a010` | R3_PDF_TYPO | PDF_TYPO | NOT_HOLD | 渲染页 413 Ex2 td.xpt 表头 (`ig34_p0413.txt:21`); 渲染页 414 Ex3 表头 (`ig34_p0414.txt:29`); KB `TD/examples.md:102` | ① 不成立: 本原子是 p413 **Example 2** 表头, 渲染页印 "TDTGTPAI" (正确); 登记 `S-TDM TD T-4` 的 "TDTGPAI" 在 p414 **Example 3** 表头 (对应原子 `ig34_p0414_a013`, KB 第 167 行)。KB 第 102 行与 PDF 逐字一致, KB 无错; 终态应为 EXACT (T3 前即 EXACT) |
| T241 | `ig34_p0414_a008` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染页 414 (`ig34_p0414.txt:13-15`); KB `TD/examples.md:157` | `S-TDM TD T-3`: 渲染页确认 "( i.e., week 8" 括号后有空格; KB "(i.e., week 8"; 其余逐字 (含 "- 3 days and + 1 week") |
| T242 | `ig34_p0419_a013` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染页 419 表第 4 行 (`ig34_p0419.txt:24`); KB `domains/TS/assumptions.md:50` | `B-TS T-3`: PDF "DOSFREQ" → KB "DOSFRQ"; 2 / B / Dosing Frequency / Q24H 逐格一致。包内 KB 指针 (43 行) 是叙述句, 表格行实为 50 行 |
| T243 | `ig34_p0425_a024` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0425.txt:29-32`; KB `TS/assumptions.md:115` | `B-TS T-6`: "MAXAGE case" → "AGEMAX case"; 其余逐字 |
| T244 | `ig34_p0428_a006` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0428.txt:20-21`; KB `chapters/ch08_relationships.md:36` | `B-ch08 T-2`: "GMGRPID" → "CMGRPID"; 其余逐字 (KB 加粗 "Rows 1-3:" 不算差异) |
| T245 | `ig34_p0428_a008` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0428.txt:23-25`; KB `ch08_relationships.md:40` | `B-ch08 T-2` (第 2 处): "with GMGRPID" → "with CMGRPID"; 其余逐字。包内 KB 指针 (36 行) 偏, 实为 40 行 |
| T246 | `ig34_p0433_a017` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0433.txt:24-25`; KB `ch08_relationships.md:224` | `B-ch08 T-3`: "SQAPFAMH." → "SQAPFAMH)."; 其余逐字 |
| T247 | `ig34_p0433_a019` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0433.txt:28-29`; KB `ch08_relationships.md:228` | `B-ch08 T-4`: "llustrate" → "illustrate"; 其余逐字 |
| T248 | `ig34_p0438_a019` | R3_PDF_TYPO | PDF_TYPO | HOLDS | `ig34_p0438.txt:45-49`; KB `domains/RELSUB/assumptions.md:29` 与 `chapters/ch08_relationships.md:373` | `B-REL T-9` / `B-ch08 T-9`: PDF 句末无句号; 两处 KB 副本都补了句号; 其余逐字 |
| T249 | `ig34_p0457_a004` | R3_PDF_TYPO | PDF_TYPO | HOLDS | 渲染页 457 6.4.3 行 (`ig34_p0457.txt:27-30`); KB `chapters/ch10_appendices.md:387` | `S-CH10 T-2`: 渲染页确认 "--TETM"; KB "--TERM"。Section Name 渲染页为 "Variables Unique to Findings About" (原子 verbatim 多抽了 "Events or Interventions", 原子抽错), KB 与 PDF 一致; Change 文本其余逐字 |

注: T232 依据列中 KB 行号以此为准 — PDF Row 27 ↔ KB Row 26 在 `TR/examples.md:44`; "POOR IMAGE QUALITY" 改正值在 KB Row 25 `TR/examples.md:43`。

## 计数 (R3_PDF_TYPO 层, 24 条)

| 判定 | 条数 | 编号 |
|---|---|---|
| HOLDS | 20 | T226-T236, T241-T249 |
| NOT_HOLD | 4 | T237, T238, T239, T240 |
| UNVERIFIABLE | 0 | — |

4 条 NOT_HOLD 全是**标签级别**问题 (① 不成立: 登记的笔误不在本原子内, 而在同段 / 另一例的相邻原子), KB 内容与 PDF 逐字一致, KB 无错; 终态应改为 EXACT。

## 附带记录 (不计入判定)

- T232 的登记指针应补 `B-TR T-1` (Row/TRSEQ 27→26); 原子 verbatim 把 p356 跨页续行 "POOR IMAGEQUALITY" 归入 Row 27, 实属 Row 26 (KB Row 25)。
- 同段其它原子的 PDF_TYPO 归属值得主控顺查 (未审, 仅提示): 台账里 `ig34_p0412_a009` (真正含 "assessments..") 与 `ig34_p0414_a013` (真正含 "TDTGPAI") 也是 PDF_TYPO, 二者应成立; `ig34_p0414_a006` 亦为 PDF_TYPO, 不在本包。
- p419 叙述 `TSPARMCD = "Dose"` vs KB "DOSE" 已登记为 `B-TS T-2`, 不是新问题。

## 样本外发现的 KB 内容问题

无。
