# T2S.S-MOD1 Auditor (Rule A) — attempt 1 (批次 attempt 2 终态)

> agent: oh-my-claudecode:verifier (opus); brief `subagent_prompts/t2s_scan_review_audit_v1.0.md` Auditor 段 + `t2_auditor_v1.0.md`; seed 20261126; 2026-11-26.
> 对象: `knowledge_base/model/01_concepts_and_terms.md` (sv20 p4-10), `model/03_special_purpose_domains.md` (p40-49), `model/04_associated_persons.md` (p50); `git diff HEAD` 未提交. 源 `source/cdisc/SDTM_v2.0.pdf` (PDF 页 = 印刷页).
> census / fp_match 对 sv20 无证明力, 本审不采用; 表格以 110dpi 渲染逐格为准. 先独立判 (下方全部), 判完才读 `t2_S-MOD1.md` / `t2_S-MOD1_review.md`.

## 抽样 (可复跑)
脚本 `$S/sample.py` (S=scratchpad/t2s_S-MOD1_auditor; 从 repo 根 `python3 -I $S/sample.py`), 同 S-MOD3 写法, 节号 "1-2" 展开为 1/2:
- P = pdf_atoms 中 sv20_, 各 sections 页范围, atom_type ∈ SENTENCE/LIST_ITEM/NOTE/CROSS_REF/TABLE_ROW, parent_section 节号 ∈ {1, 1.x, 2, 2.x} (p4-10) / {3.2, 3.2.x} (p40-49) / {4} (p50), 去 ledger INTENTIONAL_EXCLUDE; intros 空.
- P_raw 270, 去 IE 88 → |P| = 182. writer.jsonl 涉及页 = p6/8/9/40-50 → W = 133.
- N = min(30, max(20, ceil(0.1×182)), 182) = 20; writer 页取 ceil(N/3)=7, 余 13 从 P 余集随机.
- 样本: writer 7 = p0047_a010, p0046_a019, p0006_a009, p0008_a003, p0043_a011, p0044_a013, p0042_a007; 随机 13 = p0047_a007, p0047_a006, p0009_a005, p0005_a007, p0042_a008, p0009_a018, p0006_a019, p0045_a013, p0005_a014, p0045_a007, p0047_a015, p0046_a006, p0042_a006.

## 样本判定 (TABLE_ROW: R1 下 KB 5 列 #/Variable/Label/Type/Role(+Qualified 括注), 缺列不计; KB Notes 列在 D6 下核"不矛盾". 全部对渲染逐格)
| # | atom_id | PDF 页 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | sv20_p0047_a010 | p47 SJ #8 SJENDTC / End Date/Time of Repro Stage / Char / Timing; UR Not in human | 03:162 | 无 (R1) | 是 | §3.2.3.2 | 5 格一致, Notes = UR |
| 2 | sv20_p0046_a019 | p46 §3.2.3.2 "Because actual data does not always follow the plan … (SJUPDES)" | 03:145 | 无 | 是 | §3.2.3.2 | 逐字 |
| 3 | sv20_p0006_a009 | p6 "Usage Restrictions previously mentioned only in the SDTMIG and/or … (SENDIG) were added:" | 01:79 | 无 | 是 | §1.4 | 逐字 |
| 4 | sv20_p0008_a003 | p8 §2 "The model is built around the concept of observations …" | 01:112 | 无 | 是 | §2 | 逐字 (PDF 斜体/KB 粗体, S-CH1 不计) |
| 5 | sv20_p0043_a011 | p43-44 DM #37 DMDTC / Date/Time of Collection / Char / Timing | 03:61 | 无 (R1) | 是 | §3.2.1 | 一致 |
| 6 | sv20_p0044_a013 | p44 CO #5 POOLID / Pool Identifier / Char / Identifier | 03:97 | 无 (R1) | 是 | §3.2.2 | 一致 (CO 表无 Notes 列, PDF Notes 属 R1 缺列) |
| 7 | sv20_p0042_a007 | p42 DM #20 AGETXT / Age Text / Char / Record Qualifier | 03:44 | 无 (R1) | 是 | §3.2.1 | 5 格一致; Notes "Used when exact age is unknown; e.g., \"18-25\"" 在 D6 (:21) 下, 与 PDF Notes 不矛盾 |
| 8 | sv20_p0047_a007 | p47 SJ #5 RSTGCD / Repro Stage Code / Char / Topic | 03:159 | 无 (R1) | 是 | §3.2.3.2 | 一致 |
| 9 | sv20_p0047_a006 | p47 SJ #4 SJSEQ / Sequence Number / Num / Identifier | 03:158 | 无 (R1) | 是 | §3.2.3.2 | 一致 |
| 10 | sv20_p0009_a005 | p9 "A role describes the type of information conveyed …" | 01:160 | 无 | 是 | §2.1 | 逐字 |
| 11 | sv20_p0005_a007 | p5 "The SDTM has been designed for backward compatibility …" | 01:38 | 无 | 是 | §1.4 | 逐字 |
| 12 | sv20_p0042_a008 | p42 DM #21 AGEU / Age Units / Char / Variable Qualifier, Qualified "AGE; AGETXT" | 03:45 | 无 (R1) | 是 | §3.2.1 | 一致 (括注分隔符 "/" vs ";" 仅记法); Notes 例值在 D6 下 |
| 13 | sv20_p0009_a018 | p9 "Variable Qualifiers used to further modify or describe 1 or more …" | 01:178 | 无 | 是 | §2.1 | 逐字 |
| 14 | sv20_p0006_a019 | p6 "The variable APID was removed from Section 3.1.4 …" | 01:94 | 无 | 是 | §1.4 | 逐字 (后句 a020 = T-1, 见下) |
| 15 | sv20_p0045_a013 | p45 §3.2.3.1 "Subject Elements describes the actual order of elements …" | 03:115 | 无 | 是 | §3.2.3.1 | 逐字 |
| 16 | sv20_p0005_a014 | p5 列表 "The table contained in Variables Used in Associated Persons Data is now in Section 4 …" | 01:46 | 无 | 是 | §1.4 | 逐字 |
| 17 | sv20_p0045_a007 | p45 CO #14 CODTC / Date/Time of Comment / Char / Timing | 03:106 | 无 (R1) | 是 | §3.2.2 | 一致 |
| 18 | sv20_p0047_a015 | p47 "Planned trial visits are described in the Trial Design Model (see Section 5.1.4.1, Trial Visits)." | 03:168 | 无 | 是 | §3.2.3.3 | 逐字含交叉引用 |
| 19 | sv20_p0046_a006 | p46 SE #4 SESEQ / Sequence Number / Num / Identifier | 03:132 | 无 (R1) | 是 | §3.2.3.1 | 一致 |
| 20 | sv20_p0042_a006 | p42 DM #19 AGE / Age / Num / Record Qualifier | 03:43 | 无 (R1) | 是 | §3.2.1 | 一致; Notes = PDF Notes 逐字 |

**独有信息丢失 0 / 20; 忠实度错误 0 / 20; 位置错误 0.**

## 超出样本的独立核
- 渲染逐格 (110dpi, `pdftoppm -f N -l N -r 110 -png source/cdisc/SDTM_v2.0.pdf $S/pN`): p40-44 DM 1-38, p44-45 CO 1-15, p46 SE 1-13, p47 SJ 1-10, p48 SV 1-16, p49 SM 1-10, p50 AP 1-4 = 7 表 106 行全看; 行数/顺序/#/Variable/Label/Type/Role/Qualified 括注全一致. AP Notes 4 格 = PDF Notes 逐字. 表题 (粗体行) 7 个 = PDF 表题.
- KB Notes 列 (D6 下) 逐格核不矛盾: DM 非空 26 格中约 21 格引/缩 PDF Format/Notes/UR, 其余 (SEX/ARMCD/SETCD/AGETXT/AGEU 例值) KB 自写不矛盾 → :21 "most … some cells add" 属实; SE :125 / SJ :151 / SV :176 / SM :209 列说明逐格属实 (SE TAETORD/EPOCH = PDF C-code C83438/C71738).
- 叙述正向机械扫 (`python3 -I $S/scan.py`, 规范化弯引号/dash/空白/链接): p4-10 + p40-50 全部 SENTENCE/LIST_ITEM/NOTE/CROSS_REF/HEADING 原子 187 条 (含 IE 叙述), 未命中 1 = sv20_p0006_a020 (T-1).
- 反向 KB→PDF (`python3 -I $S/rev.py $S`, 非表格行): 未命中仅 H1/`Source:`/`## Overview`/`### Variables (n variables)`/KB 导航 H3 (Variable Roles, Qualifier Variable Subclasses, Key Reference Date Variables, AP Domain Rules, Key Principles)、:21 model/04 一行交叉引用、D6 引用块 (01:124, 01:180-185; 03:15/21/66/85/119/125/151/176/203/209; 04:17-19/27-29), 及 01:77/:106/:114/:158/:191 (PDF 折行连字符/换页, 去折行后逐字命中) 与 01:94 T-1. 无 "无出处且未 D6" 行.
- T-1 (01:94 "Section 4"): PDF p6 写 "Section 3, Associated Persons Data"; PDF 自身可定 (p5 两处 + p8 "Section 4, Associated Persons Data"; §4 标题 p50) → KB 写正确值, 按 PDF_TYPO 规则成立, 不计.
- Mermaid (01:126-152) 对渲染 p8 原图: 节点 13 个文字一致; 边 includes×4 / SD include→GOC,SPD / AP include→GOC,SPD / SL include→TDM,SRS / GOC include→EV,IV,FI / FA subtype of→FI 全一致; 配色 = PDF 图例 (绿 = RD/SPD/TDM/SRS, 黄 = EV/IV/FI/FA, 其余无色); :124 D6 图例文字 = PDF 图内 Key 2 条.
- D2 删除 (diff `-` 行): 旧 RFENDTC/RFPENDTC/AGE/ARMNRS/MIDS 矛盾格、RPATHCD 错标签 "Reproductive Pathway Code"、SVREASOC 错标签、旧 `**Structure:**` 行 (SE/SJ/SV/SM 表题已含 "One Record per") 、model/04 旧改写段/表 — 删除内容均有 PDF 原文或表题承载, 无信息丢失.
- 入站锚点: `01_concepts_and_terms.md#changes-to-datasets-and-variables` (model/04:21, model/06:182) → 01:86 标题存在; 03/04 无入站锚点.
- gaps / intros / footnote_moves 均空; 本批无 spec.md.
- diff 授权范围: 本批改动只在 3 个 kb_files (narrow 空); 工作树其余 KB 改动为别批.
- 终态经 reviewer: model/03 mtime 17:40:44 (+09) < reviewer a2 报告 17:41:30; model/01 17:21 / model/04 17:25 早于 reviewer a1.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (基线).
- G-TB8: trace L372/L376/L382 writer (`oh-my-claudecode:executor`) subagent_done; L380 reviewer CONDITIONAL + L383 reviewer PASS (`oh-my-claudecode:code-reviewer`); 无 agent main 写 KB 记录. 通过.

## 观察 (不阻断)
- O-1: DM SETCD Notes "Use with extreme caution" (03:58) PDF 无依据 (PDF Notes "Defined by the sponsor … Maximum of 8 characters …"), 不矛盾, 在 D6 下 — 与 writer 需主控定 M-2 一致.
- O-2: model/03/04 KB `## Overview` + PDF 编号 H3 同义标题对 (writer M-4) — 层级/导航问题, 非忠实度.

## 与 writer / reviewer 对照 (判完后读)
- writer `t2_S-MOD1.md`: T-1、Mermaid M-1/M-2、子类表→列表 M-3/M-4、SETCD 无依据 (需主控定 M-2) 与本审独立结论一致. 需主控定 M-1..M-5 为可回退项, 不影响本审判定.
- reviewer `t2_S-MOD1_review.md` a1 CONDITIONAL (F-1 SE D6 措辞) → a2 PASS; 本审核 03:125 现文字属实, 无分歧.

**结论: PASS** (丢失 0 / 忠实 0, N=20, seed 20261126).
