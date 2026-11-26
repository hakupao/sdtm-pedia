# T2 B-BS — Rule A 独立抽检 (auditor)

## attempt 1

- auditor: `oh-my-claudecode:verifier` (opus); 2026-11-26; prompt `subagent_prompts/t2_auditor_v1.0.md` + `t2_dispatch_notes.md`
- base: `git diff HEAD -- knowledge_base/domains/BS` (本批未提交); 判定先于阅读 writer/reviewer 报告 (仅在判完后对照 T-1/T-3 登记)
- 主控口径 override (写入抽样脚本): kb_files = `BS/examples.md` + `BS/assumptions.md` (授权); pdf_pages = BS 全节 p196-199
- 抽样命令: `python3 -I <scratch>/t2_B-BS_auditor/sample.py` (= v1.0 模板脚本 + 上述两行 override; scratch = session scratchpad `t2_B-BS_auditor/`), seed=20261126
- 结果: C=1, P=31, N=10 (C 抽 1 + P−C 抽 9)

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|-----------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0198_a020 (C) | p198 Ex1 "Rows 1-2": A260/A280 与 A260/A230 比值判 RNA 纯度; 超范围提示蛋白/试剂污染 | BS/examples.md:7 | 否 | 是 | 是 | PDF `rations` / `may indicated` 为拼写错 (渲染 p198 已核), KB `ratios` / `may indicate` 合 dispatch PDF_TYPO 口径 (T-1); 其余逐字 |
| 2 | ig34_p0198_a021 | p198 Ex1 "Row 3": 28S/18S 比值; --TESTCD 不能以数字开头故前缀 "I" | BS/examples.md:9 | 否 | 是 | 是 | 逐字 (与表 Row 3 BSTESTCD `I28S18S` 一致) |
| 3 | ig34_p0196_a016 | p196 §6.3.5.2 节引言: BE/BS/RELSPEC 自 SDTMIG-PGx (2015-05-26) 复制并小改 | BS/assumptions.md:3 | 否 | 是 | 是 | 新增内容, 逐字 |
| 4 | ig34_p0199_a012 | p199 §6.3.5.3 CP 概述: 不替代 LB 常规血液学, 也不用于显微/IHC 评估 | CP/assumptions.md:11 | 否 | 是 | 是 | 对照原子 (kb_files 外), 逐字, 在 CP Description/Overview 下 |
| 5 | ig34_p0199_a014 | p199 CP use case 1: 按表型/状态 marker 差异表达识别的细胞群 (正常及异常) | CP/assumptions.md:15 | 否 | 是 | 是 | 对照原子, 逐字 |
| 6 | ig34_p0196_a017 | p196 节引言: 为 SDTMIG v3.4 发布时退役 SDTMIG-PGx 而做 | BS/assumptions.md:3 | 否 | 是 | 是 | 新增内容, 逐字 |
| 7 | ig34_p0198_a013 | p198 Assumption 4: 改用 SPECTYPE (C78734), 加 --LOC/--LAT/--DIR/--PORTOT, 删 BSANTREG, 其值可放 SUPP 修饰 BSLOC | BS/assumptions.md:21 | 否 | 是 | 是 | 逐字 |
| 8 | ig34_p0198_a014 | p198 Assumption 5: BS 一般不用的 15 个变量清单 | BS/assumptions.md:23 | 否 | 是 | 是 | 15 变量齐、顺序同; PDF `--STRNLO` 为变量名拼错 (渲染已核), KB `--STNRLO` 合 PDF_TYPO 口径 (T-3) |
| 9 | ig34_p0199_a013 | p199 CP "The modeled use cases include measurement of" | CP/assumptions.md:13 | 否 | 是 | 是 | 对照原子, 逐字 |
| 10 | ig34_p0198_a011 | p198 Assumption 2: 遗传材料 BSSPEC 取 GENSMP (C111114) | BS/assumptions.md:17 | 否 | 是 | 是 | 逐字 |

- **独有丢失 0 / 忠实度错误 0 → PASS**

### 新增内容逐字核 (BS/assumptions.md, 对 p196 pdftotext + 码位)
- :3 节引言 3 句 (a016/a017/a018) 逐字; :5 `## BS – Description/Overview`、:9 `## BS – Specification`、:13 `## BS – Assumptions` 均为 PDF 原标题 (p196/p198), 连字符 U+2013 与 PDF 同; :7 Description 句 (a020) 逐字; :11 spec 首句含 U+2014 em dash, 与 PDF 同, 位置按 CM/IS 先例.
- BS 目录内无重复副本 (grep "minimally updated" / "biospecimen characteristics" 仅 assumptions.md 各 1 处; spec.md:3 为既有 Class/Structure 摘要行).

### P 全量旁证 (机械匹配, 归一空白/列表符)
- 31 原子中 27 精确命中 (BS/assumptions、BS/examples、CP/assumptions). 4 个未命中: p198_a020 (T-1)、p198_a014 (T-3) 为 PDF_TYPO 已人工判忠实; p196_a014 (§6.3.5.1 GF spec 脚注) 与 p198_a008 (BS spec 脚注 "1In this column, an asterisk (*) …") — 均属 spec.md (不在 kb_files), BS/GF/CP/LB spec.md 都无此脚注 → **范围外发现** (系统性, 同 B-MK auditor 记的 p0291_a025), 不计本批 FAIL.
- p198_a012 在 pdf_atoms 中被抽成 "part of the" (已知抽取缺陷); PDF 原页为 "part the" (渲染核), KB `part of the` 合 PDF_TYPO 口径 (T-2).

### 表格旁证 (非抽样范围, 仅核 diff)
- examples.md:17-20 改动 7 格 (BSTESTCD `A260A230`/`A260A280`/`I28S18S`, BSXFN `…3.4:7280912` ×4) 与 p199 pdftotext 一致.

### G-TB8
- trace.jsonl:208 writer `oh-my-claudecode:executor` subagent_done (04:26:52Z); :211 reviewer `oh-my-claudecode:code-reviewer` PASS (04:30:15Z); 无 `agent: main` 写 BS KB 记录.
- 当前 md5 assumptions `6a486d34…` / examples `09d77c52…` = writer checkpoint 报的 after 值; KB mtime 04:25Z 早于 review → reviewer 后无 KB 改动. spec.md 未动 (`e14a4461…`).

### live docs
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → 见下行 (基线 42)
- 实测: `broken relative links: 18668 (live docs: 42)` = 基线 42, 未升.
