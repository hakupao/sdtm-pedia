# T2 B-MB auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

- 对象: `knowledge_base/domains/MB/examples.md` md5 `8dd0a3281433fd51392fd5a7aa62f937` (307 行), diff vs `97e1895` (git diff --stat: 1 file, 仅 MB/examples.md)
- 独立判定: 先按 PDF 渲染页 (pdftoppm -r 130, p256-263) + `work/pdf_pages` 判, 判完才对照 writer/reviewer checkpoint.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-MB_auditor/` (sample.json, cells.txt, fp_after/regress.jsonl, base.md, p-256..263.png)

### 1. Prose 抽检 (G-TB5)
命令: `t2_auditor_v1.0.md` 抽样块原样, `b="B-MB"; seed=20261126` → `$S/sample.json`
结果: **C=3, P=61, N=10** (C 全抽 3 = min(|C|, ceil(N/2)); P−C 抽 7 未改动对照原子)

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0263_a001 (C) | p263:1 DI 句 (device used row 3 MB / rows 3-4 MS → DI domain) | MB/examples.md:263 | 否 | 是 | 是 (Ex3, di.xpt 前) | 逐字; 规范化后与 PDF 页文本一致 |
| 2 | ig34_p0263_a006 (C) | p263:7 RELREC 说明 2 句 (--LNKID/--LNKGRP; --REFID NAAT) | MB/examples.md:272 | 否 | 是 | 是 (relrec.xpt 前) | 逐字 |
| 3 | ig34_p0261_a014 (C, LIST_ITEM VALUE_DIFF) | p261:22 Ex3 MB Row 1 (AFB stain; MBSPCCND concentrated; MBGRPID→row 2) | MB/examples.md:227 | 否 | 是 | 是 | MBSPCCND 拼写与 PDF 渲染一致 |
| 4 | ig34_p0260_a027 | p260:35 BS Row 1 (total volume lavage fluid; BSREFID=BEREFID; parent) | MB/examples.md:193 | 否 | 是 | 是 (bs.xpt 前) | 对照原子, 逐字 |
| 5 | ig34_p0261_a002 | p261:3 RELSPEC Row 1 (original parent; PARENT blank) | MB/examples.md:210 | 否 | 是 | 是 (relspec.xpt 前) | writer 新增 atom, 逐字 |
| 6 | ig34_p0256_a006 | p256:11 MS 假设 3.b (same sample many events → --LNKID) | MS/assumptions.md:27 (另 MB/assumptions.md:28) | 否 | 是 | 是 (PDF 属 §6.3.5.7.2 MS) | 不在本批 kb_files, 未改动; ledger EXACT |
| 7 | ig34_p0263_a016 | p263:19 Ex4 引言 (contaminated culture; 8-hour pooled sputum; MBDTC/MBENDTC) | MB/examples.md:287 | 否 | 是 | 是 (### Example 4) | 逐字 (含 PDF 原文 "This example below how" 照录) |
| 8 | ig34_p0257_a002 | p257:3 Ex1 third method macro broth dilution; MSAGENT; MSCONC/MSCONCU | MB/examples.md:32 | 否 | 是 | 是 (Ex1) | 逐字 |
| 9 | ig34_p0257_a004 | p257:7 Ex1 Rows 5-6 (Local Lab XYZ susceptible 0.5 ug/dL / resistant amoxicillin) | MB/examples.md:36 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0260_a028 | p260:37 BS Rows 2-6 (volume of each aliquot) | MB/examples.md:195 | 否 | 是 | 是 | 逐字 |

**独有丢失 0/10, 忠实度错 0/10.**
(C = atoms[] 中 prose 原子 3 条: p0263_a001, p0263_a006, p0261_a014; 其余 9 条为表格原子, 由 §2 渲染全格核覆盖.)

### 2. 表格 10 格随机复核 (渲染图人工核)
命令: 解析 KB 全部 `**xxx.xpt**` 表的非 Row 格, `random.Random(20261126).sample(cells,10)` → `$S/cells.txt`

| # | 表 (KB 行) | 格 | KB 值 | PDF 渲染 | 判 |
|---|---|---|---|---|---|
| 1 | Ex3 mb.xpt (:244) r2 | DOMAIN | MB | p262 MB | 一致 |
| 2 | Ex3 bs.xpt (:206) r6 | BSDTC | 2011-01-17T06:00 | p260 同 | 一致 |
| 3 | Ex1 ms.xpt (:45) r2 | MSTEST | Microbial Susceptibility | p257 同 | 一致 |
| 4 | Ex1 ms.xpt (:50) r7 | MSSEQ | 7 | p257 7 | 一致 |
| 5 | Ex2 ms.xpt (:143) r8 | MSTESTCD | MICROSUS | p259 同 | 一致 |
| 6 | Ex3 be.xpt (:169) r3 | BESEQ | 3 | p260 3 | 一致 |
| 7 | Ex2 mb.xpt (:116) r8 | MBDTC | 2005-07-06T08:00 | p258 同 | 一致 |
| 8 | Ex2 ms.xpt (:143) r8 | MSSTRESU | (空) | p259 空 | 一致 |
| 9 | Ex1 ms.xpt (:52) r9 | MSCONC | (空) | p257 空 | 一致 |
| 10 | Ex3 bs.xpt (:201) r1 | BSLOC | STOMACH | p260 同 | 一致 |

随机样本偏易, 另对重建/新增表做全格人工核 (渲染图):
- Ex3 mb.xpt (:241-248, p262): 24 列表头顺序、6 行全部格一致 (含 ZIEHL NEELSEN ACID FAST STAIN、CONCENTRATED r1-2、SPDEVID ABC765 r3、r5 147/CFU/Qn/14700/14700/CFU/mL、MBLOC 全 STOMACH、VISIT WEEK 1).
- Ex3 suppmb (:252-259): 值与行序一致; Row 列 5/6 vs PDF 7/8 = 登记 T-1.
- di.xpt (:265-270, p263): 2 行 × 8 列全一致. relrec.xpt (:274-283, p263): 6 行 × 8 列全一致.
- Ex4 mb.xpt (:295-298, p263): 值一致 (VISIT WEEK 5); 表头 MBGRPID / MBSTRESN 对应 PDF 印刷 MBGPRID / MBTRESN = 登记 T-2 / T-3.
- Ex1 ms.xpt r3 MSORRES/MSSTRESC=1, r9 MSSTRESC 空 (p257) 一致; Ex2 mb VISIT "VISIT 1/2/3" (p258) 一致; Ex3 be r4 BEREFID 100.3, r10 BELNKID 空 (p260) 一致.
**表格格错 0.**

### 3. D2 去重删除抽检 (删除行无独有 PDF 内容)
命令: base = `git show 97e1895:knowledge_base/domains/MB/examples.md`; 候选 = base :3-110 ∪ :123-139 (D-1..D-4, 不含 MOVED M-1/M-2) 中非空、非分隔行、且不在改后文件逐字出现的行 → 39 行; `random.Random(20261126).sample(rem,10)`.

| # | base 行 | 内容摘要 | 判 | 依据 |
|---|---|---|---|---|
| 1 | :7 | Ex1 MS 叙述合并段 | 改写 (错) | 副本 1 把 MSGRPID 句挪到 disk diffusion 前、删 epsilometer 的 "such as susceptible…"; PDF 原序原文在 :20-32 |
| 2 | :11 | Ex1 mb 表头 (多 MBTSTDTL, MBNAM 错位) | 错值 | p256 表头无 MBTSTDTL; 正确表头在 :15 |
| 3 | :14 | Ex1 mb r2 (DETECTION/PRESENT/2005-06-19) | 错值 | p256 r2 = ENTEROCOCCUS FAECALIS / 2005-07-21; 正确行 :18 |
| 4 | :55 | Ex2 **Rows 1-2:** 说明 | 重复 (仅格式) | 同文在 :95 |
| 5 | :56 | Ex2 **Rows 3-4:** 说明 | 重复 (仅格式) | 同文在 :97 |
| 6 | :63 | Ex2 mb 表头 (多 MBSPEC) | 错值 | p258 无 MBSPEC 列; 正确表头 :107 |
| 7 | :66 | Ex2 mb r2 (空 MBSPEC 错位) | 错值 | p258 r2; 正确行 :110 |
| 8 | :80 | `## Example 3` 标题 | 重复 | 保留 `### Example 3` :147 |
| 9 | :86 | Ex3 --DTC 句 + 附挂 MBGRPID 句 | 改写+误挂 | PDF p259 原文 "(MB and MS)." 在 :153; MBGRPID 句属 p261 Row 4, 在 :233 |
| 10 | :94 | **Row 10:** 100.1 concentrated | 重复 (仅格式) | :161 |

**删除导致的独有信息丢失 0/10.**

### 4. fp_match 回归集
命令: `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → RESULT RED, regressions 13.
- 与 `work/t1_errata.json` `t3_atom_err` (12 条) 比: missing = ∅; extra = {ig34_p0215_a018} — §6.3.5.3 CP Rows 19-32, targets CP/assumptions.md + CP/examples.md (并行批 B-CP 的工作树改动), **非 MB**.
- **MB 范围内回归集 = t3_atom_err 12 条, 完全相等.** 已渲染核: p257 ms r3 MSORRES=1、p258 VISIT 1/2/3、p260 BEREFID 100.3/BELNKID 空、p263 WEEK 5、Ex4 表头 → KB 现值按 PDF, 回归原因为 atom verbatim 抄自旧 KB 错值 (T3 回写).

### 5. 其他
- check_links: `python3 tools/check_links.py | tail -1` → live docs 42 (基线 42).
- G-TB8: trace.jsonl 本批有 executor subagent_done (行 50, 57) 与 code-reviewer subagent_done (行 55, PASS); 无 `agent: main` 写 MB 的记录. **通过.**
- 观察 (不计 FAIL): ig34_p0256_a006 在 MB/assumptions.md:28 与 MS/assumptions.md:27 两处重复 (MS 假设被复制到 MB), 范围外, 非本批文件.

### 判定
独有丢失 0, 忠实度错 0, 表格错 0, 删除丢失 0, fp 回归集 = 预期 12 → **PASS**
