# T2 B-LB reviewer verdict

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**VERDICT: CONDITIONAL** — 1 处必改 (脚注重复, 裁定 b); 其余全部通过.

### 修正清单 (writer attempt 2 / 主控直接执行均可)

1. `knowledge_base/domains/LB/assumptions.md:56-57` 删除 (第二条 `> ¹In this column, an asterisk (*) …` 及其后空行). 结果顺序:
   通用表 (:22-50) → 脚注 :52 → `## LB – Assumptions` :54 → `1. This domain captures …`.
   理由: p196 (通用表→脚注) 与 p245 (LB 表→脚注→"LB – Assumptions") 两处 PDF 顺序都由 "脚注在标题前" 一条满足; 文字逐字相同, 无信息丢失;
   p245_a007 (NOTE, target assumptions.md) 删后仍由 :52 命中 (norm 子串, 已验). 不加 `## LB – Specification` 指针 (LB 规格表在 spec.md, 本批非白名单; 加了仍是两份相同脚注).
   删后无需重跑 census (该行不在任何表内); 主控复核 fp_match LB lost = [] 即可.

### 命令 (repo 根; S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-LB_reviewer)

| 命令 | exit / 关键输出 |
|---|---|
| `table_census.py --manifest $S/manifest.json --out $S/census_after.json` | 0; `status: {'UNPARSEABLE': 1, 'OK': 4, 'DIFF': 1}; cells compared: 1040; diffs: 1` (DIFF = examples.md:67 HEADER LBSTNRHI vs PDF LBSTRNHI = T-1) |
| `fp_match.py --out $S/fp_after.jsonl --baseline work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` | RESULT: RED, regressions=11 — 全部 ig34_p0257-p0263 (baseline hit_target = MB/examples.md, B-MB 并行批), **LB 回归 0** (LB 命中 baseline 129 → after 274, lost=[]) |
| `python3 tools/check_links.py` | `live docs: 42` (≤ 42) |
| `pdftoppm -r 110` p194-196,245-248 + `-r 400 -x -y -W -H` 裁 Ex1/Ex2/Ex3 各 4 tile (坐标取自 `pdftotext -bbox`) | 人工逐格见下 |
| `$S/cellcheck.py $S/p195_196.raw.txt assumptions.md 22 50` (pdftotext -raw, 去空白子串) | 29 行 × 7 格 全 ok |
| fp_match.norm 直查 atoms 原文 ∈ 目标文件 | 全命中; p195_a004/005/006 MISS 仅因 atom verbatim 带 PDF 子弹符 "o " (atom 伪迹), KB :14-16 去符号后与 PDF 一致 |

### 问题表

| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| assumptions.md:56 | 位置 / 裁定 b | 与 :52 逐字相同的脚注相隔 4 行重复 | p245 "¹In this column, an asterisk (*) indicates…" 紧接 "LB – Assumptions"; p196 同文紧接通用表 |

无其他缺陷.

### 人工逐格 — p195-196 通用规格表 (assumptions.md:20-50, census UNPARSEABLE; 渲染 110dpi 目视 + raw 文本子串双法)

表标题 :18 / 表头 :20 一致. 每行 7 格 (Name|Label|Type|CT|Role|Notes|Core):

| KB 行 | Variable | Type / CT / Role / Core (对渲染图) | Label + Notes (子串+目视收尾) | 页 |
|---|---|---|---|---|
| 22 | STUDYID | Char / – / Identifier / Req | 一致 | 195 |
| 23 | DOMAIN | Char / -- / Identifier / Req | 一致 | 195 |
| 24 | USUBJID | Char / – / Identifier / Req | 一致 | 195 |
| 25 | --SEQ | Num / – / Identifier / Req | 一致 | 195 |
| 26 | --GRPID | Char / – / Identifier / Perm | 一致 | 195 |
| 27 | --REFID | Char / – / Identifier / Perm | 一致 | 195 |
| 28 | --TESTCD | Char / * / Topic / Req | 一致 | 195 |
| 29 | --TEST | Char / * / Synonym Qualifier / Req | 一致 | 195 |
| 30 | --CAT | Char / * / Grouping Qualifier / Perm | 一致 | 195 |
| 31 | --SCAT | Char / * / Grouping Qualifier / Perm | 一致 | 195 |
| 32 | --ORRES | Char / – / Result Qualifier / Exp | 一致 | 195 |
| 33 | --ORRESU | Char / * / Variable Qualifier / Perm | 一致 | 195 |
| 34 | --LLOD | Char / – / Variable Qualifier / Perm | 一致 | 195 |
| 35 | --STRESC | Char / – / Result Qualifier / Exp | 一致 | 195 |
| 36 | --STRESN | Num / – / Result Qualifier / Perm | 一致 ("--\nSTRESC" 折行合并为 --STRESC 正确) | 195 |
| 37 | --STRESU | Char / * / Variable Qualifier / Perm | 一致 | 195 |
| 38 | --STAT | Char / * / Record Qualifier / Perm | 一致 | 196 |
| 39 | --REASND | Char / – / Record Qualifier / Perm | 一致 | 196 |
| 40 | --NAM | Char / * / Record Qualifier / Perm | 一致 | 196 |
| 41 | --SPEC | Char / * / Record Qualifier / Perm | 一致 | 196 |
| 42 | --METHOD | Char / * / Record Qualifier / Perm | 一致 | 196 |
| 43 | --LOBXFL | Char / * / Record Qualifier / Perm | 一致 ("Operationally derived", atom 的 "defined" 不可信, writer 判断正确) | 196 |
| 44 | --LLOQ | Num / – / Variable Qualifier / Perm | 一致 | 196 |
| 45 | --ULOQ | Num / – / Variable Qualifier / Perm | 一致 | 196 |
| 46 | VISITNUM | Num / – / Timing / Perm | 一致 | 196 |
| 47 | VISIT | Char / – / Timing / Perm | 一致 | 196 |
| 48 | VISITDY | Num / – / Timing / Perm | 一致 | 196 |
| 49 | --DTC | Char / ISO 8601 datetime or interval / Timing / Perm | 一致 | 196 |
| 50 | --DY | Num / – / Timing / Perm | 一致 ("sponsor-defined" 复合词, 折行连字符保留正确) | 196 |

29/29 行 = PDF 29 行, 行序一致, 无多无漏.

### 人工逐格 — examples.md (p247, 400dpi tile 目视)

- Ex2 :52-56 — 表头 34 列顺序一致; 3 行 × 34 格 = 102 格全部一致 (GLUC/7·11·9 mg/dL/0.39·0.61·0.5 mmol/L/0.1/0.8/NORMAL/5792-7/TEST STRIP/LBLOBXFL r1=Y/INITIAL DOSING/LBDTC·LBENDTC/Pre-dose·0-8·8-16 hours…/-PT15M·PT8H·PT16H/Dosing/1999-06-19T08:00/Y).
- Ex3 :67-70 — 表头 29 列一致 (第 19 列 PDF 印 LBSTRNHI, KB LBSTNRHI = T-1 成立: 同表 LBSTNRLO 及 Ex1/Ex2 均 LBSTNRHI); 2 行 × 29 格全部一致 (CHEMISTRY, "-", Ord/PrThr, NEGATIVE, NOT DONE / NOT APPLICABLE (SUBJECT MALE), 2106-3, URINE, LBLOBXFL r1=Y, 1, BASELINE, 1999-06-19T04:00 / 1999-06-24T08:00, Y). PDF 无 LBMETHOD 列.
- Ex1 :22-41 — 要求 ≥30 随机格, 实际 41 列 × 18 行全部目视 (4 tile) 一致; 抽重点: r1 LBORRES 30 g/L→LBSTRESC 3.0 g/dL, LBSTNRHI 5; r4 LBCOLSRT "MEAN, ARITHMETIC" 374; r5 LBDRVFL Y; r8 LBLLOD "Detection limit <=0.01 ng/mL"; r9 LBPTFL 空 + LBPDUR PT24H; r14 LBSTNRLO/HI 5.00/9.00 且 LBSTRESN 空; r15 NOT DONE/INSUFFICIENT SAMPLE 全空结果; r16 LBORNRHI <200 / LBSTNRHI 199; r17 LBLOBXFL 空 LBFAST Y; r18 NEGATIVE to TRACE / ABNORMAL / LBCLSIG N; r1/r12 LBCLSIG N; r2 LBLOBXFL 空; r3 LBLOBXFL Y; r6 HIGH SENSITIVITY; r10 PLATELET RICH PLASMA. 全一致.
- Ex4 :86 r3 LBLOBXFL=Y — p248 layout 一致.

### 裁定核验

| 裁定 | 项 | 结论 |
|---|---|---|
| a | N9 assumptions.md:73 | 同一 PDF 句 (p246 #8) 漏 "LBPOS, LBLOC, LBFAST,"; 原地补后与 PDF 一致; p246_a003 hit; LB 无回归 → 接受 |
| a | N10 examples.md:13 | 同句 "set to indicate that" vs PDF "set to missing because" (语义反转); p246_a013 hit → 接受 |
| a | N11/N12 examples.md:47-48 | 同句 LBRFDTC vs PDF LBRFTDTC; p247_a008/a009 hit → 接受 |
| a | N13 examples.md:86 | 表格格值, 非叙述; census OK → 接受 |
| a | N14 examples.md:90 | 同句, PDF "for a single agent." ; p248_a012 hit → 接受 |
| a | N15 examples.md:92 | 同句, PDF "total amount of HGFR"; p248_a013 hit → 接受 |
| a | 全部 | fp_match 本批两文件 lost=[] (其他原子无回归) |
| b | assumptions.md:52/:56 | 不可接受 → 见修正清单 1 |
| c | X-1 | 确认: 删除的斜体概述列 LBTOX/LBTOXGR/LBNAM/LBBLFL/LBENDTC 与 "Monocytes", p247 Ex1 表均无, 且漏 LBLOBXFL/LBGRPID 等 → 与 PDF 矛盾, D2 删除成立 |
| c | X-2 | 确认: p248 "LBBDAGNT variable for a single agent." KB "binding" 为扩写 |
| c | X-3 | 确认: 旧 Ex2 CREAT/2000-02-01 数据与 p247 GLUC 表完全不符; 旧 Ex3 LBMETHOD 列 PDF 无 |

### G-TB6 反向溯源 (diff 全部新增/改动行)

- 叙述/标题行 assumptions.md :3,5,7,9,11-16,18,52,54,73 — 归一化子串对 p194-196/p245-246 raw 文本全命中; examples.md :13,47,48,90,92 全命中.
- 表格行: assumptions.md :22-50 (29 行, 上表); examples.md :24-41 / :54-56 / :69-70 / :86 (逐格上述).
- 结构行签字: assumptions.md :20 表头、:21 分隔线; examples.md :22 / :52 / :67 表头, :23 / :53 / :68 分隔线; 新增节标题 :3 `## §6.3.5 …`、:7 `## §6.3.5.1 …`、:54 `## LB – Assumptions` (均为 PDF 标题, 仿 NV/GF/MS 先例) — 签字通过.
- 无出处词句: 0 (删 :56 后亦无).

### 其他
- 完整性: atoms 33/33 有 action; 无 SKIPPED; census 3 DIFF + 1 本批 pdf_only 全处理; p241 IS PDF_ONLY 属 IS, 不计.
- 无副作用: 本批 diff 只在 LB 两白名单文件; 其余 KB diff (CP/MB/TR) 为并行批. 标题/锚点未改 (新增节除外).
- R2 recheck: t2_recheck[] 为空.
- 范围外 (非阻断, 记录): LB/spec.md 无 "¹In this column" 脚注 (KB 结构惯例, 全库 spec.md 均无), 不在本批处理.
