# T4 加查 ATOM_ERR (S1-R1) — 包 3 结果 (E43-E63, 21 条)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读, 新实例
- 日期时间 (UTC): 2026-11-27T14:10:11Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- brief: `.work/10_tier_b_repair/subagent_prompts/t4/t4_atomerr_s1r1_v1.0.md` + `t4_supp_fullcheck_v1.0.md` (背景 / 判定口径)
- 样本包: `.work/10_tier_b_repair/work/t4/atomerr/atomerr_pack_3.md`
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`, Read 带 pages): 258, 260, 263, 274, 278, 289, 301, 304, 307, 322, 327, 336; 另用 pdftoppm 放大: p289 (CV 行 5-8, 300dpi 裁切, 核 "Cross-sec." 句点), p307 (RP 表左右两段, 200dpi 裁切, 核 RPSTRESN / VISIT / VISITDY 列)
- 用过的命令 (临时文件只在 session scratchpad):
  - `sed -n A,Bp .work/10_tier_b_repair/work/pdf_pages/ig34_pNNNN.txt` (p258/260/263/274/278/289/301/304/307/322/327/336/337)
  - `grep -n` 定位 KB: `knowledge_base/domains/{MB,PP,PC,CV,OE,RP,FT,QS,RS}/*.md`
  - `python3 -I cmp.py` (PDF 行拼接 + 空白/粗体/弯直引号归一后与 KB 行逐字比; OE r1-2 / OE r3 / FT 7 / QS 7 / RS 3b / PC Method D 均 EQUAL; OE p304 Row 1-4 vs KB 133-136 均 True)
  - `pdftoppm -r 300 -f 289 -l 289 -x 300 -y 1700 -W 2100 -H 500 -png ...`; `pdftoppm -r 200 -f 307 -l 307 -x 0 -y 0 -W 2200 -H 700 -png ...`; `pdftoppm -r 200 -f 307 -l 307 -x 1800 -y 440 -W 1000 -H 200 -png ...`
  - `grep -n` `.work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` (p263 表头 / p336 3c)
  - `grep -n '"ig34_p0337_a00[1-4]"' .work/10_tier_b_repair/work/coverage_ledger.wc.jsonl` (只读, 核 E63 页归属)

## 逐条判定

| # | atom_id | 判定 | ① 原子 vs PDF (差在哪; PDF 文件:行 或 渲染页) | ② KB vs PDF (KB 文件:行) | 说明 |
|---|---|---|---|---|---|
| E43 | ig34_p0258_a022 | HOLDS | VISIT 列原子写 "VISIT", PDF 为 "VISIT 1" (同格折行); 其余 16 格一致. `ig34_p0258.txt:30-31`; 渲染 p258 mb.xpt row 4 | `knowledge_base/domains/MB/examples.md:79` 逐格 = PDF (VISIT 1) | |
| E44 | ig34_p0258_a023 | HOLDS | VISIT 原子 "VISIT", PDF "VISIT 1". `ig34_p0258.txt:32-33`; 渲染 p258 row 5 (MBTSTDTL 空也一致) | `knowledge_base/domains/MB/examples.md:80` 逐格 = PDF | |
| E45 | ig34_p0258_a024 | HOLDS | VISIT 原子 "VISIT", PDF "VISIT 1". `ig34_p0258.txt:34-35`; 渲染 p258 row 6 | `knowledge_base/domains/MB/examples.md:81` 逐格 = PDF | |
| E46 | ig34_p0260_a009 | HOLDS | BEREFID 原子 "100", PDF row 4 为 "100.3". `ig34_p0260.txt:14`; 渲染 p260 be.xpt row 4 | `knowledge_base/domains/MB/examples.md:116` 逐格 = PDF (表头 :110 列序一致, BELNKID / BEENDTC 空) | 包内 KB 指针 :340 偏, 实际在 :116 |
| E47 | ig34_p0260_a015 | HOLDS | BELNKID 原子 "3", PDF row 10 该格为空. `ig34_p0260.txt:20`; 渲染 p260 row 10 BELNKID 空 | `knowledge_base/domains/MB/examples.md:122` 逐格 = PDF (BELNKID 空) | 包内 KB 指针 :346 偏, 实际在 :122 |
| E48 | ig34_p0263_a021 | HOLDS | VISIT 原子 "WEEK 1", PDF "WEEK 5" (折行). `ig34_p0263.txt:26-28`; 渲染 p263 Ex4 row 1 | `knowledge_base/domains/MB/examples.md:243` 逐格 = PDF (WEEK 5; MBORRESU / MBSTRESN / MBSTRESU 空) | 同表表头 MBGPRID / MBTRESN 为已登记 PDF 笔误 (B-MB T-2 / T-3), 不属本原子 |
| E49 | ig34_p0263_a022 | HOLDS | VISIT 原子 "WEEK 1", PDF "WEEK 5". `ig34_p0263.txt:29-31`; 渲染 p263 row 2 | `knowledge_base/domains/MB/examples.md:244` 逐格 = PDF | |
| E50 | ig34_p0274_a019 | HOLDS | 原子 QORIG 多 "Collected"; PDF row 7 QORIG 空 (QVAL = SINGLE DOSE). `ig34_p0274.txt:35`; 渲染 p274 SUPPPP row 7 | `knowledge_base/domains/PP/examples.md:74` 逐格 = PDF (QORIG / QEVAL 空) | |
| E51 | ig34_p0278_a051 | HOLDS | 原子多 "and \"10\" through \"12\"" 与 "individual PP", 且写 "1 through 7" 引号位置错; PDF: PCSEQ "1" through "12" and PP records ... "1" through "7". `ig34_p0278.txt:57-58`; 渲染 p278 Method D | `knowledge_base/domains/PC/examples.md:146` 逐字 = PDF (在 Method D 标题 :144 下) | 包内无 KB 指针; 自行 Grep 在 PC/examples.md 定位到 :146 |
| E52 | ig34_p0289_a024 | HOLDS | CVTEST 原子 "Cross-sec" 无句点; PDF "Minor Axis Cross-sec. Diameter, MVS". `ig34_p0289.txt:47-50`; p289 300dpi 裁切确认句点 | `knowledge_base/domains/CV/examples.md:31` 逐格 = PDF | |
| E53 | ig34_p0289_a025 | HOLDS | CVTEST 原子 "Cross-sec" 无句点; PDF "Major Axis Cross-sec. Diameter, MVS". `ig34_p0289.txt:51-54`; p289 裁切确认 | `knowledge_base/domains/CV/examples.md:32` 逐格 = PDF | |
| E54 | ig34_p0301_a017 | HOLDS | 原子漏 ", using OETESTCD=\"INTP\"", 多出 PDF 无的 OEDTC="2012-01-19" (p3xx 文本层均无此串). `ig34_p0301.txt:40-41`; 渲染 p301 | `knowledge_base/domains/OE/examples.md:7` 归一后逐字 = PDF | |
| E55 | ig34_p0301_a018 | HOLDS | 原子漏 "OEORRES and OESTRESC. This" 与 "spot" ("red visible"). `ig34_p0301.txt:42-44`; 渲染 p301 | `knowledge_base/domains/OE/examples.md:8` 归一后逐字 = PDF | |
| E56 | ig34_p0304_a020 | HOLDS | 原子 "installation", PDF "instillation". `ig34_p0304.txt:23`; 渲染 p304 Example 4 Row 1 | `knowledge_base/domains/OE/examples.md:133` 逐字 = PDF | |
| E57 | ig34_p0304_a021 | HOLDS | 原子 "post-installation", PDF "post-instillation". `ig34_p0304.txt:24`; 渲染 p304 Row 2 | `knowledge_base/domains/OE/examples.md:134` 逐字 = PDF | |
| E58 | ig34_p0304_a022 | HOLDS | 原子 "installation", PDF "instillation". `ig34_p0304.txt:25`; 渲染 p304 Row 3 | `knowledge_base/domains/OE/examples.md:135` 逐字 = PDF | |
| E59 | ig34_p0304_a023 | HOLDS | 原子 "post-installation", PDF "post-instillation". `ig34_p0304.txt:26`; 渲染 p304 Row 4 | `knowledge_base/domains/OE/examples.md:136` 逐字 = PDF | |
| E60 | ig34_p0307_a008 | HOLDS | RPSTRESN 原子为空, PDF row 1 RPSTRESN = 1 (原子 19 格中第 11 格空). `ig34_p0307.txt:9-10`; p307 200dpi 裁切 (RPSTRESN 1; VISIT SCREENING; VISITDY 1) | `knowledge_base/domains/RP/examples.md:11` 逐格 = PDF (表头 :9 列序一致) | |
| E61 | ig34_p0322_a013 | HOLDS | 原子漏 "see Section 4 of the QRS supplement. See" (原子直接 "; see Section 4.5.3"). `ig34_p0322.txt:27-30`; 渲染 p322 第 7 条 | `knowledge_base/domains/FT/assumptions.md:68` 归一后逐字 = PDF | |
| E62 | ig34_p0327_a015 | HOLDS | 原子漏 "; see Section 4 of the QRS supplement" (原子 "study metadata. See Section 4.5.3"). `ig34_p0327.txt:31-34`; 渲染 p327 第 7 条 | `knowledge_base/domains/QS/assumptions.md:49` 归一后逐字 = PDF | |
| E63 | ig34_p0337_a002 | HOLDS | 原子挂在 p337, 但 p337 无此句 (p337 为 QRS Shared Assumptions); 内容实为 p336 RS CC 假设 3b, 且原子写 "RSORRESRU" (PDF "RSORRESU")、"practice or original" (PDF "practice for original"). `ig34_p0336.txt:32-33`; 渲染 p336 | `knowledge_base/domains/RS/assumptions.md:80` 归一后逐字 = PDF p336 3b (弯引号 ’ 归一) | |

## 计数

- HOLDS: 21
- NOT_HOLD: 0
- UNVERIFIABLE: 0
- 涉登记编号: 无 (本包 21 条均不涉 `t2_pdf_typo_registry.jsonl` 登记)
- 没看渲染页只看文本层的编号: 无 (21 条均对照了渲染页)

## 样本外发现的 KB 内容问题

无. (顺带看到的 PDF 笔误均已登记且 KB 按登记处理: p263 Ex4 表头 MBGPRID / MBTRESN → `knowledge_base/domains/MB/examples.md:241` 写 MBGRPID / MBSTRESN, 登记 B-MB T-2 / T-3; p336 RS 3c "uses a a source" → `knowledge_base/domains/RS/assumptions.md:81` 写 "uses a source", 登记 B-RS T-3.)

附注 (非判定): 包内 KB 指针偏 / 缺的条目: E46 (:340 → 实际 :116), E47 (:346 → 实际 :122), E51 (无 → 实际 `knowledge_base/domains/PC/examples.md:146`).
