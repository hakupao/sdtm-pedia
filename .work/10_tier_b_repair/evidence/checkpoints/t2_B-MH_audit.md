# T2 B-MH auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

**verdict: PASS** — 独有丢失 0, 忠实度错误 0 (主样本 10 + 补抽 11); 10 seeded 改动格 + 4d 表对渲染一致; D-1..D-3 无 PDF 内容丢失; G-TB8 通过.

- 审查对象: KB 终态 md5 assumptions `c4469c2749e81dd20d713d7bd04d6e8a` / examples `216c920a870d40a08430b12f2a0d3e77` (= writer 续 2 / reviewer 续 签字值). `git diff --stat 259cd49 -- knowledge_base/domains/MH/` = 2 files, 38+/32-.
- 独立方法: 原 PDF `source/cdisc/SDTMIG v3.4 (no header footer).pdf` 重新 `pdftotext` (非 layout) + `pdftoppm -r 110` 渲染 p171-178; 未读 writer/reviewer 结论前先判. scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-MH_auditor/` (sample.json, chk.py, cells.txt, fp.jsonl, fp_regress.jsonl, p171-178.txt, r*.png).

### 抽样
- 命令 = `subagent_prompts/t2_auditor_v1.0.md` §抽样 原样 (b="B-MH", seed=20261126), 输出 `$S/sample.json`.
- **C=0, P=28, N=10** (全部来自 P−C, 因 atoms/t2_recheck 均为 0).
- P 只覆盖 pdf_pages 175-178 (examples); 按派发要求另做 **补抽 11** (非随机, 定向): 新增 Description/Specification、全部 assumptions 改动原子 (2b/2d/3a.i/4a/6b)、未改对照 (4d/5a/7)、Ex1 Rows 4-5 (D-3). 另核 :53 KB note (KB→PDF).
- 判法: 原子 verbatim 先核在新 pdftotext 原页 (全部 True, p174_a0013 仅 "--\nSMIE" 折行); 再与 KB 行 (去 `**`/列表前缀/弯引号) 做整行相等比较 (`python3 -I $S/chk.py $S`).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0176_a0016 | p176 Ex3 "Rows 1-9: MHPRESP = "Y" indicates…queried" | examples:54 | 否 | 是 | 是 | 整行相等 |
| 2 | ig34_p0176_a0015 | p176 Ex3 引言 "medical history CRF where…solicited" | examples:52 | 否 | 是 | 是 | 整行相等 |
| 3 | ig34_p0175_a0003 | p175 Ex1 引言 "General Medical History CRF…ongoing question" | examples:5 | 否 | 是 | 是 | 整行相等 |
| 4 | ig34_p0177_a0011 | p177 Ex4 "Rows 1-2: subject XYZ-001-001 had type 1…" | examples:77 | 否 | 是 | 是 | 整行相等 |
| 5 | ig34_p0177_a0019 | p177 "Example 5" 标签 | examples:90 | 否 | 是 | 是 | `## Example 5` (导航格式) |
| 6 | ig34_p0175_a0004 | p175 Ex1 "Rows 1-3: …MHSCAT indicates the body system…"Ongoing" question" | examples:7 | 否 | 是 | 是 | 改动行 (D-2); 整行相等, 渲染一致 |
| 7 | ig34_p0175_a0018 | p175 Ex2 "In all of the records shown below, MHCAT…assumption 4" | examples:29 | 否 | 是 | 是 | 整行相等 |
| 8 | ig34_p0176_a0001 | p176 Ex2 "Rows 1-3: …further guidance on using --STRF and --ENRF" | examples:31 | 否 | 是 | 是 | 改动行 (补尾); 整行相等 |
| 9 | ig34_p0175_a0016 | p175 Ex2 bullet "A second CRF collected stroke history…" | examples:26 | 否 | 是 | 是 | `- ` 列表前缀 |
| 10 | ig34_p0177_a0021 | p177 Ex5 "Row 1: subject 203 had no respiratory infections…" | examples:94 | 否 | 是 | 是 | 整行相等 |
| S1 | ig34_p0171_a0010 | p171 Description "An events domain that contains…prior medical history" | assumptions:7 | 否 | 是 | 是 | 在新 `## MH – Description/Overview` (:5) 下 |
| S2 | ig34_p0171_a0012 | p171 spec 首句 "mh.xpt, Medical History — Events. One record per…" | assumptions:11 | 否 | 是 | 是 | 新增, 逐字; `## MH – Specification` :9 = p171 标题 |
| S3 | ig34_p0172_a0018 | p172 2b MHMODIFY "…The modified term is listed in MHMODIFY…" | assumptions:19 | 否 | 是 | 是 | 改动行, 整行相等 |
| S4 | ig34_p0173_a0002 | p173 2d MHBODSYS "…standard hierarchy." (无 "It is expected…") | assumptions:21 | 否 | 是 | 是 | D-1 删后整行相等 |
| S5 | ig34_p0173_a0006 | p173 3a.i "generic group such as "Medical History"…" | assumptions:26 | 否 | 是 | 是 | 改动行, 整行相等 |
| S6 | ig34_p0173_a0010 | p173 4a "…whether it occurred, respectively…" | assumptions:31 | 否 | 是 | 是 | 改动行, 整行相等 |
| S7 | ig34_p0174_a0012 | p174 6b "…MHSTDTC the date of diagnosis and MHENDTYP = "DIAGNOSIS"…" | assumptions:51 | 否 | 是 (登记) | 是 | 唯一差异 MHENDTYP→MHEVDTYP = T-1 (PDF_TYPO keep-correct, 依据由 PDF 自身确定: 同句/6a/p171 spec; 全 PDF 仅 p174 出现 MHENDTYP) |
| S8 | ig34_p0173_a0013 | p173 4d MHSTAT/MHREASND "…if all medications were collected as free text…" | assumptions:34 | 否 | 是 | 是 | 未改对照, 整行相等 |
| S9 | ig34_p0174_a0008 | p174 5a "Relative timing assessments…Section 4.4.7, Use of Relative Timing Variables." | assumptions:46 | 否 | 是 | 是 | 未改对照, 含交叉引用 |
| S10 | ig34_p0174_a0013 | p174 7. "…--SOD, --SMIE." | assumptions:55 | 否 | 是 | 是 | 未改对照; 14 个限定词逐个一致 |
| S11 | ig34_p0175_a0005 | p175 Ex1 "Rows 4-5: …start dates of MHEVDTYP = "SYMPTOM ONSET"…"CHF"" | examples:9 | 否 | 是 | 是 | D-3 删串入句后整行相等 |
| K1 | (KB→PDF) :53 D6 note | — | assumptions:53 | — | 不矛盾 | — | 前缀 `> KB note (not in SDTMIG):` 合规; 事实核: 全 PDF MHENDTYP 仅 p174; MHEVDTYP 见 p85/171/174/175/177/362/371; KB MH/spec.md:95 `### MHEVDTYP`, KB 全库无 MHENDTYP 变量定义 |

- **独有丢失 0 / 21; 忠实度错误 0 / 21** (T-1 为登记的 PDF_TYPO, 非忠实度错误).

### 补充: MH 段全量原子句级扫描 (PDF→KB, p171 a0008 至 p178 DV 前, 非表格原子)
- 未命中 5, 全部已知: p0172_a0013 ×2 (spec 表脚注, 属 spec.md, O-MH-1 范围外); p0173_a0007 (T-3 标点); p0174_a0012 (T-1); p0175_a0001 HEADING "MH – Examples" (KB H1 `# MH — Examples` 导航). 无新丢失.

### 删除核 (D-1..D-3)
| D | 删除内容 | PDF 核 | 结论 |
|---|---|---|---|
| D-1 | 2d 句尾 "It is expected that this variable will be populated." | p173 2d (渲染+文本) 无此句; 原子 a0002 与 KB :21 整行相等 | 无 PDF 内容丢失 |
| D-2 | Ex1 "MHSCAT displays the body systems specified on the CRF" / "Ongoing at Study Start" | p175 Ex1 为 "indicates the body system for which the event was collected" / "Ongoing"; 旧短语属 p176 Ex2, KB examples:31 仍在 | 无丢失 |
| D-3 | Ex1 Rows 4-5 "MHSTDTC was populated with the date and time at which the event occurred." | p175 Ex1 无; 属 p176 Ex2 Row 4, KB examples:33 仍在 | 无丢失 |

### 表格: 10 seeded 改动格 + 全部改动格目视 (110dpi 渲染)
- 改动格总体 36 (Ex1 11 / Ex2 17 / Ex3 3 / Ex4 2 / Ex5 3), `random.Random(20261126).sample(…,10)` → `$S/cells.txt`:

| # | 表 | 行 | 格 | KB | 渲染 | 结论 |
|---|---|---|---|---|---|---|
| 1 | Ex3 (p177) | 8 | MHOCCUR | Y | Y | ✓ |
| 2 | Ex3 (p177) | 4 | MHREASND | 空 | 空 | ✓ |
| 3 | Ex1 (p175) | 1 | MHENTPT | 2004-09-18 | 2004-09-18 | ✓ |
| 4 | Ex1 (p175) | 2 | MHENTPT | 2004-09-18 | 2004-09-18 | ✓ |
| 5 | Ex2 (p176) | 3 | MHOCCUR | 空 | 空 | ✓ |
| 6 | Ex1 (p175) | 5 | MHEVDTYP | DIAGNOSIS | DIAGNOSIS | ✓ |
| 7 | Ex2 (p176) | 5 | MHPRESP | Y | Y | ✓ |
| 8 | Ex1 (p175) | 3 | MHSTDTC | 空 | 空 | ✓ |
| 9 | Ex3 (p177) | 4 | VISITNUM | 1 | 1 | ✓ |
| 10 | Ex2 (p176) | 8 | MHOCCUR | N | N | ✓ |

- 未入 seeded 样本但已目视: Ex1 表头 15 列含 MHEVDTYP (MHDECOD 后) ✓, r4 SYMPTOM ONSET ✓; Ex2 表头列序 MHSCAT, MHPRESP, MHOCCUR, MHBODSYS ✓, r1-3 MHBODSYS ✓; Ex4 r1/r4 MHOCCUR Y ✓; Ex5 r4 MHENRTPT/MHENTPT 空 ✓, r1 MHDTC `2019-011-02` = PDF 照录 (T-2, T4 用户裁定项) ✓.
- **4d 表 (assumptions:36-41, UNPARSEABLE) 对 p174 渲染逐格**: 表头 Situation / Value of MHPRESP / Value of MHOCCUR / Value of MHSTAT ✓; 4 行 (空空空 / Y Y 空 / Y N 空 / Y 空 NOT DONE) ✓.

### fp 回归 (独立复跑)
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → exit 1 (全局 RED), regress 48; 其中 MH (p171-178 / domains/MH) **仅 ig34_p0174_a0012** (T-1, 预期). 其余 47 属他批页.

### G-TB8
- trace.jsonl: T2.B-MH writer `oh-my-claudecode:executor` subagent_done (02:51:36Z) ✓; reviewer `oh-my-claudecode:code-reviewer` a1 PASS (03:10:01Z) + 续 签字 a2 PASS (03:11:34Z) ✓; 无 `agent: main` 写 KB 记录 ✓.
- 时序: examples.md mtime 03:10:26Z (续 2 T-2 照录) < reviewer 续 签字 03:11:34Z ✓; 签字 md5 = 当前 md5 ✓.
- 观察 (非阻断): writer 续 (M-1, assumptions mtime 03:03:29Z) 与 续 2 (T-2) 未各自在 trace 记 subagent_done (B-ch08 有 "回填 (主控)" 先例); 内容已在 checkpoint + writer.jsonl (41 行) 记录. 建议主控回填.

### 汇总
独有丢失 0, 忠实度错误 0 → **PASS**. 范围外: O-MH-1 (spec.md p171-172 spec 表行/脚注) 维持 writer 登记, 不计本批. T4 待用户: T-2 (Ex5 r1 MHDTC 2019-011-02 照录).
