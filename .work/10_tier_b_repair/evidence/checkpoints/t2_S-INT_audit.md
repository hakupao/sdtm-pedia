# T2S.S-INT Auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus), 2026-11-26. 先独立判, 判完才读 `t2_S-INT.md` / `t2_S-INT_review.md`. 只读 KB.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-INT_auditor/`

**Verdict: PASS** — 独有丢失 0, 忠实度错误 0 (N=30).

## 抽样 (可复跑; repo 根执行 `python3 -I $S/sample.py`)
```
P = pdf_atoms 中 ig34, atom_type ∈ {SENTENCE, LIST_ITEM, NOTE, CROSS_REF, TABLE_ROW},
    页 ∈ sections 范围且 parent_section 前缀属该节: AG 92-97 "§6.1.1 " / PR 125-128 "§6.1.5 " /
    103-120 "§6.1.3 " | "§6.1.3.1 " | "§6.1.3.2 " | "§6.1.3.3 " (边界页 §6.1.2 CM p103 / §6.1.4 / §6.1.6 原子排除),
    减 ledger INTENTIONAL_EXCLUDE (本范围实减 4), 并入 intro §6.1 ig34_p0092_a003 (§6.1.3 intro a021/a022 已由前缀纳入).
writer 页 W = S-INT.writer.jsonl pdf_page 集合 {92,93,94,96,103,104,105,107,108,109,111,112,114,115,116,118,119,125,126,127}; C = P ∩ W 页.
N = min(30, max(20, ceil(0.1*|P|)), |P|); rng = random.Random(20261126); s1 = rng.sample(C, ceil(N/3)); s2 = rng.sample(sorted(P - s1), N - |s1|)
```
结果: |P| = 518, |C| = 397, N = 30 (writer 页 10 + 其余 20), seed = 20261126.

## 样本判定 (TABLE_ROW: 例表对 110dpi 渲染逐格 p113/114/115/116/117/119/128; spec 行对 pdftotext -layout 逐列)
| # | atom_id | PDF 页:摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0115_a017 | 115: Ex5 ex.xpt r3 ABC5002 AM DRUG X 10 mg | EX/examples.md:221 | 否 | 是 | 是 | 渲染逐格一致 |
| 2 | ig34_p0114_a021 | 114: Ex5 CRF ABC5002 B/PM/1/2012-02-01/02-08 | EX/examples.md:185 | 否 | 是 | 是 | 渲染逐格 |
| 3 | ig34_p0092_a024 | 92: spec AGPRESP 行 | AG/spec.md:122-129 | 否 | 是 | 是 | CT C66742 = U5 归 S-CT |
| 4 | ig34_p0119_a017 | 119: Ex7 relrec "Row 6" VS VSLNKID ONE 1 | EX/examples.md:413 | 否 | 是 | 是 | KB Row 3 = 已登记 PDF_TYPO B-EX T-1 (行号 1,2,6,3,4,6) |
| 5 | ig34_p0125_a018 | 125: spec PRSCAT 行 (CT *) | PR/spec.md:104-111 | 否 | 是 | 是 | 本批补 `*` |
| 6 | ig34_p0094_a003 | 94: spec AGSTRTPT 行 (Section 4.4.7) | AG/spec.md:338-345 | 否 | 是 | 是 | CT C66728 = U5 |
| 7 | ig34_p0108_a019 | 108: spec ECFAST 行 | EC/spec.md:266-273 | 否 | 是 | 是 | |
| 8 | ig34_p0109_a012 | 109: EC asm 1 domain model as collected | EC/assumptions.md:13 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0119_a028 | 119: Ex8 "EC dataset shows administrations as collected" | EX/examples.md:433 | 否 | 是 | 是 | |
| 10 | ig34_p0107_a005 | 107: EX asm 6b --DOSTOT deprecation | EX/assumptions.md:45 | 否 | 是 | 是 | 逐字 |
| 11 | ig34_p0115_a027 | 115: Ex6 single-crossover 叙述 | EX/examples.md:237 | 否 | 是 | 是 | 逐字 |
| 12 | ig34_p0115_a021 | 115: Ex5 relrec one-to-one --LNKID | EX/examples.md:226 | 否 | 是 | 是 | |
| 13 | ig34_p0107_a001 | 107: EX asm 4b point-in-time EXSTDTC→EXENDTC | EX/assumptions.md:39 | 否 | 是 | 是 | |
| 14 | ig34_p0095_a003 | 95: AG asm AGTRT topic / ALBUTEROL 2 PUFF | AG/assumptions.md:28 | 否 | 是 | 是 | |
| 15 | ig34_p0109_a018 | 109: EC asm Values of ECMOOD | EC/assumptions.md:21 | 否 | 是 | 是 | |
| 16 | ig34_p0108_a008 | 108: spec ECDOSU 行 (Exp) | EC/spec.md:167-174 | 否 | 是 | 是 | CT C71620 = U5 |
| 17 | ig34_p0105_a012 | 105: spec EXTPTNUM 行 | EX/spec.md:302-309 | 否 | 是 | 是 | |
| 18 | ig34_p0113_a018 | 113: Ex3 ec.xpt r4 BOTTLE B Y/N ECDOSE 空 | EX/examples.md:129 | 否 | 是 | 是 | 渲染逐格 |
| 19 | ig34_p0119_a018 | 119: Ex7 relrec "Row 3" EC ECLNKGRP MANY 2 | EX/examples.md:414 | 否 | 是 | 是 | KB Row 4 = T-1 |
| 20 | ig34_p0095_a016 | 95: AG Ex Row 1 saline | AG/examples.md:7 | 否 | 是 | 是 | |
| 21 | ig34_p0113_a012 | 113: Ex3 "as collected, in tablets" | EX/examples.md:120 | 否 | 是 | 是 | |
| 22 | ig34_p0116_a012 | 116: Ex6 ec.xpt r3 | EX/examples.md:270 | 否 | 是 | 是 | 原子文本串行 (CAPSULE/07-02 错读为 r2 值); 渲染: CAPSULE/2002-07-02T07:30/2/2 = KB |
| 23 | ig34_p0128_a003 | 128: PR Ex1 r1 Wisdom Teeth Extraction | PR/examples.md:11 | 否 | 是 | 是 | 渲染逐格 |
| 24 | ig34_p0114_a003 | 114: Ex4 no EC needed 叙述 | EX/examples.md:154 | 否 | 是 | 是 | 逐字 |
| 25 | ig34_p0125_a020 | 125: spec PROCCUR 行 | PR/spec.md:122-129 | 否 | 是 | 是 | CT C66742 = U5 |
| 26 | ig34_p0109_a017 | 109: EC asm 3 ECMOOD permissible | EC/assumptions.md:20 | 否 | 是 | 是 | |
| 27 | ig34_p0109_a009 | 109: spec ECRFTDTC 行 | EC/spec.md:401-408 | 否 | 是 | 是 | |
| 28 | ig34_p0117_a001 | 117: Ex6 ec.xpt r23 | EX/examples.md:289 | 否 | 是 | 是 | 原子串行 (TABLET, CAPSULE / 13); 渲染: BOTTLE 1/CAPSULE/TREATMENT 2/11/11 = KB |
| 29 | ig34_p0108_a021 | 108: spec ECPSTRGU 行 | EC/spec.md:284-291 | 否 | 是 | 是 | CT C71620 = U5 |
| 30 | ig34_p0128_a031 | 128: PR Ex3 r3 Radiotherapy 300 cGy BONE | PR/examples.md:58 | 否 | 是 | 是 | 渲染逐格 |

独有丢失 0 / 30; 忠实度错误 0 / 30; 位置错误 0.

## 另查
- **intros**: §6.1 (p92 a002 标题 + a003 句, 句末 "include:" 后 PDF 本身无列表, 照录) → AG/assumptions.md:3-5 host 顶部; §6.1.3 (p103 a020 + a021/a022) → EX/assumptions.md:3-5 host 顶部. 逐字 (脚本 substring 核 FOUND). ✔
- **DSAF / 首句 (gaps)**: AG (p92 a005-a009, p94 a008)、PR (p125 a002-a005, p127 a001)、EX (p104 a002-a006, p105 a017) 均在 assumptions.md Description/Overview 与 Assumptions 之间, 逐字 FOUND; EC 原有 DSA 逐字 FOUND (p107 a010/a012).
- **脚注 (U2/U7)**: AG :375 / PR :411 / EX :339 / EC :411, 逐字 (PDF 上标 1 → ¹), 均位于最后变量块 `---` 之后、`## Cross References` 之前. ✔
- **CT `*`**: `pdftotext -layout` 的 `(Char|Num) +\*` 变量 = AG {AGDECOD, AGCAT, AGSCAT, AGCLAS, AGCLASCD}, EX {EXTRT, EXCAT, EXSCAT, EXADJ}, EC {ECTRT, ECCAT, ECSCAT}, PR {PRCAT, PRSCAT}; KB `Controlled Terms:** *` 完全相同 (14/14). 变量数 AG 41 / PR 45 / EX 37 / EC 45 KB=PDF (原子名差异 PRGRID/EXRFDTC/EXTPREF 为原子抽取错, layout 核 PDF = KB).
- **§6.1.3.3 标题**: EX/examples.md:3 `## §6.1.3.3 …` (S-INT 主控口径), EC/examples.md 为一行交叉引用 (导航). §6 章标题不落地 (主控口径).
- **AG examples SDTM-MD → SDTMIG-MD**: p96 原文 "See the SDTMIG-MD" ✔. **EX Ex2 CRF Injection 1-3 去粗体**: p112 渲染非粗体 ✔; Ex7 CRF 粗体 = PDF 选中项粗体 (p118 渲染) ✔.
- **反向 KB→PDF 全 12 文件句/格扫** (`python3 -I $S/reverse.py` 与 `-raw` 版 `$S/reverse_raw.py`): -raw 版未命中仅 (a) U8 导航 (`> Class|Structure`、Cross References 块、EC/examples.md:3 交叉引用); (b) U5 C-code; (c) 已登记 PDF_TYPO: B-EX "ottles"→bottles (p113)、T-6 mg/mL→mg/kg (p118)、T-2 "--LNKID, ." (p119); (d) markdown 粗体切分伪阴性 (EX ex.md:350). AG :363 重复句 = PDF p94 原文即重复, 照录. 无 PDF 出处且未 D6 的行 = 0.
- **新 PDF_TYPO**: EX T-7 (p107 item 5 末尾串入 "Additional interventions qualifiers", 与 item 6 标题重复) / T-8 (–PRESP → --PRESP) layout 核实; PR T-1 未逐条复核 (非样本).
- **授权范围**: `git diff HEAD --stat -- knowledge_base/domains/{AG,PR,EX,EC}` = 9 文件 ⊂ kb_files, narrow_files 空. ✔
- **G-TB8**: trace 有 writer (executor) 06:54:45Z + delta 06:59:29Z、reviewer (code-reviewer, PASS) 07:06:30Z; KB 文件 mtime 最晚 06:59:17Z (EX/examples.md) < reviewer 完成; 本批无 agent main 记录. ✔
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).

## 对照 writer / reviewer (判完后读)
与 reviewer PASS 结论一致 (CT `*` 14/14、4 处脚注位置、DSAF/intro 落地、EX T-1..T-6 沿用、新 T-7/T-8/PR T-1 成立、census DIFF 仅 T-1). 本 auditor 额外记录: p116 a012 / p117 a001 原子文本串行 (渲染证明 KB 正确), 不影响结论. 无分歧.
