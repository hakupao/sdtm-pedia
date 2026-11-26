# T2 B-NV — Rule A 独立抽检 (auditor)

> agent: oh-my-claudecode:verifier (opus) · base = HEAD `f45d915` (本批未提交; `git diff HEAD -- knowledge_base/domains/NV`) · seed 20261126

## attempt 1

### 抽样
- 命令: `python3 -I <scratch>/t2_B-NV_auditor/sample_v2.py <scratch>/t2_B-NV_auditor/pinfo2.json` (scratch = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad`).
  = 模板 `t2_auditor_v1.0.md` 原脚本, 两处按 dispatch/主控口径改:
  (1) 页范围 = p285-286 + p294-298 (`PAGES = {285,286,294..298}`, 替代 batch json `pdf_pages` [285,294,296]);
  (2) 额外剔除 `parent_section` ∉ {§6.3.7, §6.3.7.1, §6.3.7.4 NV} 的原子 (= §6.3.6 MO 框 p285_a002-a005 [O31] 与 OE p298_a025).
  模板默认排除: X (IE/IE ledger) 命中 p296_a005 (NV spec 脚注); OTH (别批) 命中 p286_a017 (CV Desc).
- C = 3 (p285_a009, p285_a010, p294_a013) · P = 53 · N = max(10, ceil(0.2×3)) = 10 · C 抽 min(3, ceil(10/2)) = 3 (全部) + P−C 抽 7.
- 样本: p285_a010, p294_a013, p285_a009, p297_a037, p298_a003, p285_a015, p296_a017, p296_a019, p298_a001, p296_a013.

### 逐样本 (独立判, 判完才对照 writer/reviewer)
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|-----------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0285_a010 (C) | p285:20-22 "CDISC CT of SDTM domain abbreviations and TA user guides may have examples of other body system domains…" | NV/assumptions.md:5 | 否 | 是 | 是 (§6.3.7 Overview) | 逐字 |
| 2 | ig34_p0294_a013 (C) | p294:33 NV Desc "findings domain… nervous system, including the brain, spinal cord…" | NV/assumptions.md:38 | 否 | 是 | 是 (NV – Description/Overview) | 逐字; 位于 Spec/Assumptions 之前 = PDF 顺序 |
| 3 | ig34_p0285_a009 (C) | p285:19-20 "Additional domains for other body systems are expected to be added in future versions…" | NV/assumptions.md:5 | 否 | 是 | 是 | 逐字 |
| 4 | ig34_p0297_a037 | p297 末 "In addition to interpreting each VEP component as normal or abnormal, the overall test for each eye may have an" (页界截断) | NV/examples.md:63 | 否 | 是 | 是 (Example 2) | 与 p298_a001 拼成全句 |
| 5 | ig34_p0298_a003 | p298 "SPDEVID allows the results to be related to both the VEP testing device and the checkerboard size." | NV/examples.md:65 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0285_a015 | p285:30-33 bullet 3 "variables included in the generic … table are those required or expected…" | NV/assumptions.md:13 | 否 | 是 | 是 (§6.3.7.1) | 逐字, 含 PDF 原文 "may included" 与句末无句号 (照录) |
| 7 | ig34_p0296_a017 | p296 "Rows 1-2: Show the SUVR findings based on a PET/CT scan for a subject." | NV/examples.md:9 | 否 | 是 | 是 (Example 1) | 逐字 |
| 8 | ig34_p0296_a019 | p296 "Rows 5-6: … based on an fluorodeoxyglucose (FDG)-PET scan…" | NV/examples.md:11 | 否 | 是 | 是 | KB "a fluorodeoxyglucose" = 冠词更正 (既有行, 本批未改), 无信息变化; 事后对照 = writer T-1 已登记, reviewer L-3 建议 T4 用户过目 |
| 9 | ig34_p0298_a001 | p298 "interpretation. … NVTESTCD/NVTEST should be equal to "INTP" … NVGRPID links the each VEP component…" | NV/examples.md:63 | 否 | 是 | 是 | 逐字 (含 PDF "the each") |
| 10 | ig34_p0296_a013 | p296 "SPDEVID shows the scanner used." | NV/examples.md:7 | 否 | 是 | 是 | 逐字 |

**独有信息丢失 0 / 忠实度错误 0 → PASS**

### 补充核验
- P 全 53 原子机械子串匹配 (`python3 -I <scratch>/t2_B-NV_auditor/mech.py <scratch>/t2_B-NV_auditor`, 归一破折号/空白/`**`/行标签): 52 命中, 1 未命中 = p296_a019 (T-1 冠词). 范围外发现 0.
- p286 通用表 (新增, assumptions.md:17-34) 对渲染图核 (`pdftoppm -f 286 -l 286 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf"`): 标题行 (含 "Version 3.3") + 表头 7 列 + 12 行全部逐格比对, 抽列举 ≥10 格: DOMAIN 受控 `--`; --TESTCD/--TEST 受控 `*`; --TEST Role "Synonym Qualifier"; --LOBXFL Role "Record Qualifier"/Core Exp; --DTC 受控 "ISO 8601 datetime or interval"; --DY Type Num/Core Exp; VISITNUM Exp; --SEQ 注 "(including decimals) and does not have to start at 1"; --STRESC 注 "NONE"/"NEG"/"NEGATIVE"; USUBJID Req; 脚注 ¹ 全文 — 0 差.
- examples.md:17 Row 1 NVORRES/NVSTRESC/NVSTRESN `.95` 对 p296 渲染 ✓. 另见 Row 2 NVSTRESN: PDF 空 (渲染 + `pdftotext -layout` 双证), KB `1.17` — 事后对照 = writer T-2 登记 (依据同行 NVSTRESC 数值 + p286 --STRESC 注), 合补充口径 "能由 PDF 自身确定 → 写正确值并登记" ✓.
- spec.md 未动 (`git diff --quiet HEAD -- knowledge_base/domains/NV/spec.md`; md5 `6b4d37aa…`). NV spec 表行属 spec.md, 不在本批 kb_files (writer F-2).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` = 基线 42.

### G-TB8
- trace.jsonl:212 writer `oh-my-claudecode:executor` subagent_done 04:30:15Z; :218 reviewer `oh-my-claudecode:code-reviewer` PASS 04:34:03Z. `agent: main` 记录 6 条, 无 NV/KB 写入.
- NV/assumptions.md, examples.md mtime 2026-11-26T04:27:56Z (< writer done < reviewer done); md5 `21f2e97e…` / `449c0939…` = writer/reviewer 记录的 after 值 → reviewer PASS 后无改动. ✓

### 结论
B-NV attempt 1: **PASS** (N=10, 丢失 0, 忠实 0; 范围外 0).
