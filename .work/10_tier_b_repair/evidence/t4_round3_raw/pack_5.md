# T4.1 第三轮补检 — 包 5 (R3_IG34_EQUIV, T101-T125) 审查结果

- 审查者: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T06:35:52Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` (R3_IG34_EQUIV 层)
- 看过的渲染页: SDTMIG v3.4 p215 (左右两半, 300dpi 裁切)、p216 (表头 + 行 1-5, 300dpi 裁切)
- 用过的命令 (节选):
  - `sed -n` 读 `.work/10_tier_b_repair/work/pdf_pages/ig34_p0112/0113/0114/0115/0116/0119/0151/0200-0203/0215/0216/0237/0238/0239/0257/0260/0261/0262/0276.txt`
  - `sed -n` / `grep -n` 读 `knowledge_base/domains/{EX,CE,CP,IS,MS,MB,PC,PP}/*.md`
  - `grep -rn -e "All Examples" -e "123-0001-02" knowledge_base/` (定位 T125 的 PC 表)
  - `python3` 读 `work/pdf_atoms.jsonl` 中 `ig34_p0116_a017..a026` (核 T107 原子抽取物)
  - `grep` `work/coverage_ledger.wc.jsonl` (ig34_p0116_a020-a024)
  - `pdftoppm -r 300 -f 215 -l 215 -x .. -y .. -W .. -H .. -png` / 同 216 (输出在 scratchpad `r3_5/`)
  - `grep` `work/t2_pdf_typo_registry.jsonl` 按本包页号查登记 (只命中 p113 的 B-EX T-3, 不在样本原子内)

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| T101 | ig34_p0112_a028 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0112.txt:31-32 (ec.xpt 行 2); `knowledge_base/domains/EX/examples.md:91` | 实为逐字. 24 格逐格一致 (DRUG X / ABDOMINAL CAVITY / VISIT 3 / 2009-05-10 为 PDF 折行拼接) |
| T102 | ig34_p0113_a018 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0113.txt:20; `EX/examples.md:129` | 实为逐字. ECDOSE 空格两边一致 |
| T103 | ig34_p0114_a009 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0114.txt:11; `EX/examples.md:163` | 实为逐字. EXADJ 空 |
| T104 | ig34_p0115_a017 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0115.txt:18; `EX/examples.md:221` | 实为逐字 |
| T105 | ig34_p0115_a019 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0115.txt:20; `EX/examples.md:223` | 实为逐字 |
| T106 | ig34_p0116_a004 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0116.txt:1-5 (Subject 56789003 CRF 第 1 行); `EX/examples.md:252-257` | 实为逐字, 且在 "Subject 56789003" 小标题下 (位置对). 表头 "Bottle 1 # of capsules" 为 PDF 两行表头合并 |
| T107 | ig34_p0116_a022 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0116.txt:36-37 (ec.xpt 行 13); `EX/examples.md:279` | 原子抽错: 原子 "13 \| 56789001 \| 13 \| TABLET, CAPSULE \| 11T07:34 \| 11 \| 11" 在 PDF 中不存在 (同页 a017-a026 原子均为混抽). PDF 行 13 = 56789 EC 56789003 1 BOTTLE 1 Y Y 1 CAPSULE CAPSULE QD ORAL TREATMENT 1 2002-07-03T07:30 ×2 1 1 30 MINUTES PRIOR -PT30M STD BREAKFAST, KB:279 逐格一致; 邻行 12 (KB:278) 也与 PDF 一致 |
| T108 | ig34_p0119_a024 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0119.txt:29-30; `EX/examples.md:424-426` | 实为逐字 (Example 8 CRF 表 First/Last Dose Date) |
| T109 | ig34_p0151_a0018 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0151.txt:22-23; `CE/examples.md:16` | PDF 为 "Conjunctivitis / No / Yes" 选项 (Yes 在下一行), KB "No  Yes" 承载两个选项; 原子漏 Yes (原子抽错) |
| T110 | ig34_p0200_a012 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0200.txt:20; `CP/spec.md:5-12` | KB 以变量卡片形式承载: Label/Type/CT 空/Role/Core/Notes 七项全一致 |
| T111 | ig34_p0200_a017 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0200.txt:26; `CP/spec.md:50-57` | 同上, 各项一致 |
| T112 | ig34_p0201_a007 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0201.txt:26-30; `CP/spec.md:131-138` | Label/Char/(TESTCOND)/Variable Qualifier/Perm/Notes 全文一致 (含 PDF 原句 "is used distinguish", KB 照录); KB 另加 CT 代码 C181175 |
| T113 | ig34_p0202_a006 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0202.txt:19-22; `CP/spec.md:194-201` | Notes 第一段逐字, KB 同格还有 PDF 下一段 "An example of appropriate usage…" (PDF:23 起, 同一格) |
| T114 | ig34_p0203_a002 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0203.txt:4-5; `CP/spec.md:311-318` | 各项一致; KB 加 CT 代码 C71620 |
| T115 | ig34_p0203_a034 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0203.txt:48-49; `CP/spec.md:491-499` | 各项一致; KB 加 CT 代码 C99079 |
| T116 | ig34_p0215_a009 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p215 行 7 + ig34_p0215.txt:15-16; `CP/examples.md:185` | 原子抽错 (原子 "BLYH / 2046 / 07:31 / CPMRKSTR 带括号" 均与 PDF 不符). PDF 行 7 = seq 4, grp 2, BNSBN, "BLym Naive Sub/BLym Naive", APOPTOTIC, CD95+, "CD45+CD19+IgD+CD27-CD95+/CD45+CD19+IgD+CD27-", "CD95+ BLym Naive", "FSC+SSC+\|CD45+\|CD19+\|IgD+CD27-\|CD95+", IMMUNOPHENOTYPING, B CELL ACTIVATION, CD95 Expr BLym, 50.2, %, QUANTITATIVE, NUMBER FRACTION, 50.2, 50.2, %, BLOOD, FLOW CYTOMETRY, 2021-10-20T09:20:00; KB:185 26 格逐格一致 (管道符转义) |
| T117 | ig34_p0216_a003 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p216 行 1 + ig34_p0216.txt:3-5; `CP/examples.md:206-208` | 原子抽错 (原子 LYMONO、列错位). PDF 行 1 = LYMONOLE, Lym+Mono/Leuk, CPSBMRKS/CPCELSTA/CPCSMRKS 空, CD45+SSCmid/CD45+, LYM+MONO, SSCmid\|CD45+, %Lym+Mono/Leuk, IMMUNOPHENOTYPING, mDC AND pDC SUBSETS, 6.70, %, QUANTITATIVE, NUMBER FRACTION, 6.70, 6.70, %, BLOOD, FLOW CYTOMETRY, 2021-01-30T07:10:00; KB 表头 27 列与 PDF 同序, 行 1 逐格一致 |
| T118 | ig34_p0238_a007 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0238.txt:6 (表头), 15-17; `IS/examples.md:160-164` | 实为逐字. ISCNDAGT 空两边一致, VISITNUM 2 / VISIT 1 / 2017-08-27 一致 |
| T119 | ig34_p0239_a003 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0239.txt:2-6; `IS/examples.md:181-185` | 实为逐字 (表头 22 列同序) |
| T120 | ig34_p0257_a012 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0257.txt:13 (表头), 20-21; `MS/examples.md:21-27` | 实为逐字. MSGRPID / MSORRESU / MSSTRESN / MSSTRESU 空两边一致 |
| T121 | ig34_p0257_a029 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0257.txt:43-46; `MB/examples.md:38-42` | 实为逐字 (MB Example 2 的 be.xpt, 位置对) |
| T122 | ig34_p0257_a030 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0257.txt:47; `MB/examples.md:43` | 实为逐字 |
| T123 | ig34_p0260_a021 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0260.txt:23-28; `MB/examples.md:126-131` | 实为逐字 (suppbe.xpt 行 4) |
| T124 | ig34_p0262_a005 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0262.txt:4 (表头), 7-8; `MB/examples.md:186-190` | 原子漏 MBGRPID "1" (原子抽错); PDF 行 2 MBGRPID=1 (与行 1 同列对齐), KB:190 有 "1", 其余 23 格逐格一致 |
| T125 | ig34_p0276_a008 | R3_IG34_EQUIV | EQUIVALENT | HOLDS | ig34_p0276.txt:9-15; `knowledge_base/domains/PC/assumptions.md:55-62` | 包内指针 (PP/examples.md:93-95) 偏. 真实位置在 PC/assumptions.md "§6.3.5.9.3 Relating PP Records to PC Records" 节下 "PC Dataset for All Examples" 表 (PP/examples.md:104-108 有指向此表的指针); 行 2 实为逐字 (表头两行 "PCGRPID (Example 1)" 合并). 原子把第 4 个 PCGRPID 写成 DY1_DRGX (PDF 为 DY1_DRGX_A, 原子抽错), KB 与 PDF 一致 |

## 计数

| 层 | HOLDS | TYPO_AFFECTED | NOT_HOLD | UNVERIFIABLE |
|---|---|---|---|---|
| R3_IG34_EQUIV (T101-T125) | 25 | 0 | 0 | 0 |

- 其中 KB 行与 PDF 逐格一致 (实为逐字) 19 条: T101-T109, T116-T125; 非逐字但等价 6 条: T110-T115 (CP spec 表格行在 KB 改写为变量卡片格式, 各项值一致).
- 原子抽错 (KB 与 PDF 一致) 6 条: T107, T109, T116, T117, T124, T125.
- 本包无 KB≠PDF 差异, 故无需对照笔误登记.

## 样本外发现的 KB 内容问题

无 (本包涉及页上看到的 PDF 笔误 p113 "from ottles A, B and C" 已登记为 `B-EX T-3`, KB `EX/examples.md:118` 写 "bottles", 与登记 handling 一致).
