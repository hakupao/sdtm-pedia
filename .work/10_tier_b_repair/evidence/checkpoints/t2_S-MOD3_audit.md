# T2S.S-MOD3 Auditor (Rule A) — attempt 1

> agent: oh-my-claudecode:verifier (opus); brief `subagent_prompts/t2s_scan_review_audit_v1.0.md` Auditor 段 + `t2_auditor_v1.0.md`; seed 20261126; 2026-11-26.
> 对象: `knowledge_base/model/05_study_level_data.md` (`git diff HEAD`, +28/-28), 源 SDTM v2.0 §5 p51-63 (`source/cdisc/SDTM_v2.0.pdf`, PDF 页 = 印刷页, 已渲染核 p51).
> 注意 (dispatch notes S-MOD2 review 教训): census / fp_match 对 sv20 无证明力, 本审不采用; 表格以渲染逐格为准.
> 先独立判 (下方全部), 判完才读 `t2_S-MOD3.md` / `t2_S-MOD3_review.md` 对照.

## 抽样 (可复跑)
脚本 `$S/sample.py` (S=scratchpad/t2s_S-MOD3_auditor; 从 repo 根 `python3 -I $S/sample.py`):
- P = pdf_atoms 中 sv20_, p51-63, atom_type ∈ SENTENCE/LIST_ITEM/NOTE/CROSS_REF/TABLE_ROW, parent_section 节号 = "5" 或以 "5." 开头 (p51-63 无别节原子), 去 ledger INTENTIONAL_EXCLUDE; intros 空.
- P_raw 167, 去 IE 15 → |P| = 152. writer.jsonl 涉及页 = p51-62 → writer 页原子 W = 152 (= P).
- N = min(30, max(20, ceil(0.1×152)), 152) = 20; writer 页取 ceil(N/3)=7, 余 13 从 P 余集随机. seed 20261126.
- 样本: writer 7 = p0060_a010, p0059_a016, p0051_a011, p0052_a004, p0056_a016, p0057_a007, p0055_a008; 随机 13 = p0057_a003, p0052_a016, p0059_a012, p0058_a007, p0056_a008, p0062_a008, p0053_a014, p0062_a004, p0059_a011, p0059_a008, p0058_a017, p0058_a018, p0055_a005.

## 样本判定 (TABLE_ROW 判据: R1 下 KB 5 列 = #/Variable/Label/Type/Role(+Variable(s) Qualified 括注); Format/UR/C-code/Definition/Notes/Examples 缺列不计 (TT/TP 例外: KB Notes 列须 = PDF UR). 全部对 130dpi 渲染逐格核)
| # | atom_id | PDF 页 + 摘要 | KB line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | sv20_p0060_a010 | p60 AC #4 ACGRPID / Group ID / Char / Identifier | :240 | 无 | 是 | §5.1.7 | 逐格一致 |
| 2 | sv20_p0059_a016 | p59 TS #9 TSVALCD / Parameter Value Code / Char / Result Qualifier; UR "Not in nonclinical trials" | :225 | 无 (R1) | 是 | §5.1.6 | 5 格一致; UR 属 R1 缺列 (见观察 O-1) |
| 3 | sv20_p0051_a011 | p51 §5.1 列表 "Other aspects of a study … (Section 5.1.6, Trial Summary Information)" | :20 | 无 | 是 | §5.1 | 逐字 |
| 4 | sv20_p0052_a004 | p52 TE #7 TEDUR / Planned Duration of Element / Char / Timing (Format ISO 8601 duration) | :43 | 无 (R1) | 是 | §5.1.1.1 | 5 格一致; Format 缺列 R1 |
| 5 | sv20_p0056_a016 | p56 TV #9 TVENRL / Visit End Rule / Char / Rule | :156 | 无 | 是 | §5.1.4.1 | 一致 |
| 6 | sv20_p0057_a007 | p57 TD #5 TDSTOFF / Offset from the Anchor / Char / Timing | :172 | 无 | 是 | §5.1.4.2 | 一致 |
| 7 | sv20_p0055_a008 | p55 TP #6 RSTGCD / Repro Stage Code / Char / Topic; UR Not in human clinical trials | :126 | 无 | 是 | §5.1.3.2 | 一致, Notes 列 = PDF UR |
| 8 | sv20_p0057_a003 | p57 TD #1 STUDYID / Study Identifier / Char / Identifier | :168 | 无 | 是 | §5.1.4.2 | 一致 |
| 9 | sv20_p0052_a016 | p52 TA #5 TAETORD / Planned Order of Element within Arm / Num / Timing | :59 | 无 | 是 | §5.1.1.2 | 一致 |
| 10 | sv20_p0059_a012 | p59 TS #5 TSPARMCD / Trial Summary Parameter Short Name / Char / Topic | :221 | 无 | 是 | §5.1.6 | 一致 |
| 11 | sv20_p0058_a007 | p58 TM #5 TMRPT / Disease Milestone Repetition Indicator / Char / Record Qualifier | :190 | 无 | 是 | §5.1.4.3 | 一致 |
| 12 | sv20_p0056_a008 | p56 TV #1 STUDYID | :148 | 无 | 是 | §5.1.4.1 | 一致 |
| 13 | sv20_p0062_a008 | p62 OI #2 DOMAIN / Domain Abbreviation / Char / Identifier | :308 | 无 | 是 | §5.2.2 | 一致 |
| 14 | sv20_p0053_a014 | p53 TX #4 SET / Set Description / Char / Synonym Qualifier, Qualified SETCD | :77 | 无 | 是 | §5.1.2 | 一致 (括注 SETCD) |
| 15 | sv20_p0062_a004 | p62 §5.2.2 句 "The taxa used for identification of a non-host organism depend on …" | :301 | 无 | 是 | §5.2.2 | 逐字 |
| 16 | sv20_p0059_a011 | p59 TS #4 TSGRPID / Group ID / Char / Identifier | :220 | 无 | 是 | §5.1.6 | 一致 |
| 17 | sv20_p0059_a008 | p59 TS #1 STUDYID | :217 | 无 | 是 | §5.1.6 | 一致 |
| 18 | sv20_p0058_a017 | p58 TI #5 IECAT / Inclusion/Exclusion Category / Char / Grouping Qualifier | :204 | 无 | 是 | §5.1.5 | 一致 |
| 19 | sv20_p0058_a018 | p58 TI #6 IESCAT / Inclusion/Exclusion Subcategory / Char / Grouping Qualifier | :205 | 无 | 是 | §5.1.5 | 一致 |
| 20 | sv20_p0055_a005 | p55 TP #3 RPATHCD / Planned Repro Path Code / Char / Topic; UR Not in human clinical trials | :123 | 无 | 是 | §5.1.3.2 | 一致 |

**独有信息丢失 0 / 20; 忠实度错误 0 / 20; 位置错误 0.**

## 超出样本的独立核
- 渲染逐格 (左 7 列, 130dpi): p51 (TE 1-3), p52 (TE 4-7, TA 1-6), p53 (TA 7-10, TX 1-8), p54 (TT 1-7), p55 (TP 1-10), p56 (TV 1-9), p57 (TD 1-9), p58 (TM 1-5, TI 1-6), p59 (TI 7-8, TS 1-10), p60 (TS 11, AC 1-12), p61 (DI 1-7), p62 (OI 1-7) = 13 表 110 行全看, #/Variable/Label/Type/Role 全一致; 9 处新增 Role 括注 (ETCD×2/ARMCD×2/TXPARMCD/VISITNUM/IETESTCD/TSPARMCD/ACPARMCD) 均 = PDF Variable(s) Qualified; 既有括注 SETCD/RSTGCD/RPATHCD/MIDSTYPE/ACVAL/DIPARMCD/OIPARMCD 一致.
- 正向机械扫 (`python3 -I $S/scan.py $S`, 规范化弯引号/dash/空白): §5 全部 SENTENCE/LIST_ITEM/NOTE/CROSS_REF/HEADING 原子 (含 IE 的叙述原子) 在 KB 中 0 未命中.
- 反向 KB→PDF (非表格、非 Mermaid 行对 pdftotext p51-63): 未命中仅 H1 + `Source:` 行 (导航)、13 个 `### <PDF 节号+标题> (XX)` (S-MOD3 主控定: 域代码为检索导航) 、6 条 `> KB note (not in SDTM v2.0):` (D6). 无 "无出处且未 D6" 行.
- D6 核: :97 / :117 Notes 列说明属实 (渲染 p54/p55 UR 列逐格 = "Not in human clinical trials", TT 3-7 / TP 3-10; DOMAIN Notes = `must be "TT"/"TP"`); :261/:299 DI/OI Structure 行保留合理 (PDF 表题无 "One Record per"); :279/:317 Mermaid 对渲染 p62/p63 两图节点/边/标签逻辑一致.
- D2 删除: TX/TS `**Structure:**` D6 行删除 — PDF 表题 (p53/p59 渲染) 含 "One Record per …", 符合 S-MOD2 model/ 通用条; 信息未丢.
- 标题替换: `grep -rn "05_study_level_data.md#" knowledge_base web/src tools docs` = 0 入站锚点; 文字 = PDF 原标题 (5 / 5.1 The Trial Design Model / 5.1.1.1-5.2.2).
- gaps / intros / footnote / footnote_moves: 本批均空, 无需落地.
- diff 授权范围: 本批改动只在 `knowledge_base/model/05_study_level_data.md` (model/01/03/04 为别批并行改动, 不计).
- KB 文件 mtime 08:27:55Z < reviewer 报告 08:32:58Z → 终态经 reviewer.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (基线).
- G-TB8: trace.jsonl L370/L371 writer (`oh-my-claudecode:executor`) subagent_done + L375 reviewer (`oh-my-claudecode:code-reviewer`) PASS; 无 agent main 写 KB 记录. 通过.

## 观察 (不阻断)
- O-1: TS TSVALCD/TSVCDREF/TSVCDVER 的 PDF UR "Not in nonclinical trials" 在 KB 无承载 (R1 缺列), 而 TT/TP 的 UR 在 Notes 列承载 — 两处不一致. 与 writer M-4 / O35-3 一致, 已归 T4.
- O-2: 四级节 (5.1.1.1 等 7 个) 与父节同为 `###` (writer M-2, S-FND 不改) — 层级非忠实度问题, 记录.

## 与 writer / reviewer 对照 (判完后读)
- writer `t2_S-MOD3.md` 改动/删除/D6 清单与本审独立结论一致; M-2/M-4 与本审 O-2/O-1 相同.
- reviewer `t2_S-MOD3_review.md` PASS (110 行 550 格 diff 0) 与本审渲染全表结论一致, 无分歧.

## 结论
**PASS** — Rule A N=20 (seed 20261126): 丢失 0, 忠实 0; 无出处未标注行 0; G-TB8 通过.
