# T4.1 Q9 扩检 — 包 6 结果 (Q9_IG34_EQUIV, Q128-Q153, 26 条)

- 审查者: `oh-my-claudecode:tracer` (opus), 只读角色
- 时间 (UTC): 2026-11-27T05:03:28Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_q9_extension_v1.0.md` (冲突处优先) + `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`
- 看过的渲染页: SDTMIG v3.4 p190 (pdftoppm -r 200, 临时目录); p141 / p271 已渲染备用, 文本层已足够判定, 未另读
- 文本层: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0019, p0112, p0114, p0115, p0141, p0153, p0190, p0201, p0260, p0271, p0277, p0278, p0282, p0283, p0329, p0330, p0351, p0350, p0356, p0357, p0449, p0450, p0451`
- 用过的命令: `sed -n` / `grep -n` 读 PDF 文本层与 KB 文件; `grep` 查 `work/t2_pdf_typo_registry.jsonl`; `pdftoppm -r 200 -f N -l N -png` (输出到 scratchpad `q9_6/`); `awk` 计算 KB 行号
- 包内 KB 指针为 (无) 或 fuzzy 的条目 (Q132-Q135, Q137-Q147) 均已在所属域 / 章节文件重新定位, 下表行号为本人定位结果

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| Q128 | `ig34_p0019_a028` | Q9_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0019.txt:47-49`; `knowledge_base/chapters/ch03_submitting_data.md:71` | 实为逐字, 7 格全对. "per per visit" 为 PDF 原样, 已登记 `B-ch03 T-3 (ch03)` (照录) |
| Q129 | `ig34_p0112_a011` | 同 | EQUIVALENT | HOLDS | `ig34_p0112.txt:12` (EX Example 2 Exposure CRF); `knowledge_base/domains/EX/examples.md:70` | 实为逐字, 位于 Example 2 CRF 表 |
| Q130 | `ig34_p0114_a010` | 同 | EQUIVALENT | HOLDS | `ig34_p0114.txt:12` (Example 4 ex.xpt r5); `knowledge_base/domains/EX/examples.md:164` | 实为逐字, 15 格全对 |
| Q131 | `ig34_p0115_a033` | 同 | EQUIVALENT | HOLDS | `ig34_p0115.txt:39` (Example 6, Subject 56789001 CRF Day 3); `knowledge_base/domains/EX/examples.md:250` | 实为逐字, 10 格全对, Period 1/2 并排结构保留 (:244) |
| Q132 | `ig34_p0141_a003` | 同 | EQUIVALENT | HOLDS | `ig34_p0141.txt:3-5`; `knowledge_base/domains/AE/examples.md:15` | KB 26 格与 PDF 全对 (AEDECOD "Headache", AEENDY "-1", RECOVERED/RESOLVED). 原子漏 AEDECOD / AEENDY 属原子抽取问题, 不影响 KB |
| Q133 | `ig34_p0153_a0017` | 同 | EQUIVALENT | HOLDS | `ig34_p0153.txt:17-19`; `knowledge_base/domains/CE/examples.md:81` | KB 把该问题 3 个选项 (□ Casting/immobilization / □ Traction / □ Surgery) 合并在一格, 信息等价; 字形 □ 与 PDF 一致 (原子写成 "o", 属抽取问题) |
| Q134 | `ig34_p0190_a005` | 同 | EQUIVALENT | HOLDS | `ig34_p0190.txt:7-8` + 渲染页 p190; `knowledge_base/domains/EG/examples.md:27` | 24 格逐格比对一致: EGXFN "PQW436789-07.xml" (渲染页确认是 Q, 原子 "P0W" 是抽错), VISIT "Screening 1" (渲染页确认), EGCLSIG 空 |
| Q135 | `ig34_p0201_a010` | 同 | EQUIVALENT | HOLDS | `ig34_p0201.txt:42-43`; `knowledge_base/domains/CP/spec.md:158-165` | 名称 / 标签 / Char / Record Qualifier / Perm / Notes 全对. PDF 写 "...for the binding agent specified in CPBDAGNT.", KB 同; 原子写成 "measurement defined in CPBDAGNT" 属抽错 |
| Q136 | `ig34_p0260_a025` | 同 | EQUIVALENT | HOLDS | `ig34_p0260.txt:32` (suppbe.xpt r8); `knowledge_base/domains/MB/examples.md:135` | 实为逐字, 10 格全对, 在 MB/MS 例节的 suppbe 表 |
| Q137 | `ig34_p0271_a012` | 同 | EQUIVALENT | HOLDS | `ig34_p0271.txt:24-25`; `knowledge_base/domains/PC/examples.md:58` | 31 列逐格一致 (PCSTRESN 空, PCSTAT 空, PCENDTC 空, PCEVLINT 空; A554134-21, 2001-02-12T08:00, 2001-02-11T08:00) |
| Q138 | `ig34_p0278_a012` | 同 | EQUIVALENT | HOLDS | `ig34_p0278.txt:12` (Ex1 Method B r10); `knowledge_base/domains/PC/examples.md:100` | 实为逐字. 注: 包内指针指向 PP/examples.md (错), 正确位置在 PC/examples.md §6.3.5.9.3 Example 1 Method B |
| Q139 | `ig34_p0278_a025` | 同 | EQUIVALENT | HOLDS | `ig34_p0278.txt:25` (Ex1 Method B r23); `knowledge_base/domains/PC/examples.md:113` | 实为逐字; RELID "1" 与 PDF 表一致 (PDF 引言写 rows 14-26 RELID "2", 表里写 1, KB 随表) |
| Q140 | `ig34_p0278_a043` | 同 | EQUIVALENT | HOLDS | `ig34_p0278.txt:47` (Ex1 Method C r10); `knowledge_base/domains/PC/examples.md:136` | 实为逐字 |
| Q141 | `ig34_p0278_a048` | 同 | EQUIVALENT | HOLDS | `ig34_p0278.txt:52` (Ex1 Method C r15); `knowledge_base/domains/PC/examples.md:141` | 实为逐字 |
| Q142 | `ig34_p0283_a024` | 同 | EQUIVALENT | HOLDS | `ig34_p0283.txt:30` (Ex4 Method D r12); `knowledge_base/domains/PC/examples.md:458` | 实为逐字 |
| Q143 | `ig34_p0283_a032` | 同 | EQUIVALENT | HOLDS | `ig34_p0283.txt:38` (Ex4 Method D r20); `knowledge_base/domains/PC/examples.md:466` | 实为逐字 |
| Q144 | `ig34_p0283_a033` | 同 | EQUIVALENT | HOLDS | `ig34_p0283.txt:39` (Ex4 Method D r21); `knowledge_base/domains/PC/examples.md:467` | 实为逐字 |
| Q145 | `ig34_p0283_a052` | 同 | EQUIVALENT | HOLDS | `ig34_p0283.txt:58` (Ex4 Method D r40); `knowledge_base/domains/PC/examples.md:486` | 实为逐字 |
| Q146 | `ig34_p0329_a024` | 同 | EQUIVALENT | HOLDS | `ig34_p0329.txt:39-42` + 续行 `ig34_p0330.txt:3-7`; `knowledge_base/domains/RS/spec.md:86-93` | 名称 / 标签 / Char / (ONCRTSCD) / Topic / Req / Notes 全对, 例值 "SYMPTDTR" 与 PDF 一致 (原子 "SYMPDTR" 抽错); p330 续行也在 KB. KB 受控术语多一个 C-code "C96782", 是全 KB spec 的统一做法 (如 TR spec), 不算改值 |
| Q147 | `ig34_p0351_a018` | 同 | EQUIVALENT | HOLDS | `ig34_p0351.txt:43`; `knowledge_base/domains/TR/spec.md:239-246` | 名称 / 标签 / Char / Timing / Perm / Notes 全对, 位于 TR spec (§6.3.12.2) |
| Q148 | `ig34_p0357_a018` | 同 | EQUIVALENT | HOLDS | `ig34_p0357.txt:47-48` (Example 3 tr.xpt r19); `knowledge_base/domains/TR/examples.md:88` | 23 格逐格一致 (R1-NEW01, ACE IMAGING, INDEPENDENT ASSESSOR, RADIOLOGIST 1, 2010-02-18, 46; 空格位置相同) |
| Q149 | `ig34_p0448_a020` | 同 | EQUIVALENT | HOLDS | `ig34_p0449.txt:20`; `knowledge_base/chapters/ch10_appendices.md:184` | 实为逐字, 在 Appendix D 表 (:169/:175 起) |
| Q150 | `ig34_p0448_a023` | 同 | EQUIVALENT | HOLDS | `ig34_p0449.txt:23`; `knowledge_base/chapters/ch10_appendices.md:187` | 实为逐字 |
| Q151 | `ig34_p0448_a040` | 同 | EQUIVALENT | HOLDS | `ig34_p0449.txt:40`; `knowledge_base/chapters/ch10_appendices.md:204` | 实为逐字 |
| Q152 | `ig34_p0449_a016` | 同 | EQUIVALENT | HOLDS | `ig34_p0450.txt:16`; `knowledge_base/chapters/ch10_appendices.md:227` | 实为逐字 |
| Q153 | `ig34_p0450_a005` | 同 | EQUIVALENT | HOLDS | `ig34_p0451.txt:5`; `knowledge_base/chapters/ch10_appendices.md:263` | 实为逐字 |

注: Q149-Q153 的原子页号比文本层页号小 1 (原子 p448 → 文本 p449 等), 是原子页号的偏移, 内容定位无歧义.

## 计数

| 层 | HOLDS | NOT_HOLD_R1 | NOT_HOLD | UNVERIFIABLE | 合计 |
|---|---|---|---|---|---|
| Q9_IG34_EQUIV | 26 | 0 | 0 | 0 | 26 |

TOC 条目: 0 条.

## 原子抽取问题 (不影响判定, 供台账参考)
- Q132 原子漏 AEDECOD "Headache" 与 AEENDY "-1"
- Q133 原子把 □ 写成 "o"
- Q134 原子 EGXFN 写 "P0W436789-07.xml" (PDF 为 PQW), VISIT 写 "Screening" (PDF 为 "Screening 1")
- Q135 原子 Notes 末句写 "measurement defined in CPBDAGNT" (PDF 为 "binding agent specified in CPBDAGNT")
- Q146 原子例值写 "SYMPDTR" (PDF 为 "SYMPTDTR")

## 样本外发现的 KB 内容问题
无. (顺带核到 PC/examples.md Example 1 Method A r3 的 IDVAR、Method B r13/r26 的 RDOMAIN 与 PDF 不同, 但已登记为 PDF 笔误 `B-PCPP T-1` / `T-2` / `T-3` (KB 写正确值), 不算问题.)
