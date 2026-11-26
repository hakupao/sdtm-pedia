# T2S.S-EVT Auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus), 2026-11-26. 先独立判, 判完才读 `t2_S-EVT.md` / `t2_S-EVT_review.md`. 只读 KB.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-EVT_auditor/`

**Verdict: PASS** — 独有丢失 0, 忠实度错误 0 (N=30).

## 抽样 (可复跑; repo 根执行 `python3 -I $S/sample.py`)
```
P = pdf_atoms 中 ig34, atom_type ∈ {SENTENCE, LIST_ITEM, NOTE, CROSS_REF, TABLE_ROW},
    页 ∈ sections 范围 (AE 133-142 / DS 155-167) 且 parent_section 以 "§6.2.1 " / "§6.2.4 " 开头 (边界页 §6.1.6/§6.2.3/§6.2.5 原子排除),
    减 ledger INTENTIONAL_EXCLUDE (本范围 IE 原子均非 P 类型, 实减 0), 并入 intros ig34_p0133_a011..a018 (a010 为 HEADING).
writer 页 = S-EVT.writer.jsonl pdf_page 集合 {133,134,135,136,137,139,142,155,156,157,165,166}; C = P 中落在 writer 页的原子.
N = min(30, max(20, ceil(0.1*|P|)), |P|); rng = random.Random(20261126); s1 = rng.sample(C, ceil(N/3)); s2 = rng.sample(sorted(P - s1), N - |s1|)
```
结果: |P| = 460, |C| = 240, N = 30 (writer 页 10 + 其余 20), seed = 20261126.

## 样本判定 (TABLE_ROW 已对 110dpi 渲染逐格: p160/p162/p164/p166; spec 行对 pdftotext -layout 逐列)
| # | atom_id | PDF 页:摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0156_a0002 | 156: spec EPOCH 行 | DS/spec.md:104 | 否 | 是 | 是 | CT 记 C99079 = U5 归 S-CT, 不计 |
| 2 | ig34_p0155_a0022 | 155: spec DSSEQ 行 | DS/spec.md:32 | 否 | 是 | 是 | 7 列一致 |
| 3 | ig34_p0133_a021 | 133: AE Description 句 | AE/assumptions.md:17 | 否 | 是 | 是 | 逐字 |
| 4 | ig34_p0157_a0013 | 157: 3d-ii no reason → DSTERM = DSDECOD | DS/assumptions.md:34 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0157_a0025 | 157: 4c EPOCH 取自 TA (Section 7.2.1) | DS/assumptions.md:41 | 否 | 是 | 是 | 交叉引用在 |
| 6 | ig34_p0134_a014 | 134: spec AELLT 行 | AE/spec.md:95 | 否 | 是 | 是 | MedDRA |
| 7 | ig34_p0166_a0020 | 166: ta.xpt r7 ABC/SCRN/Randomized to ABC | DS/examples.md:361 | 否 | 是 | 是 | 渲染逐格一致 |
| 8 | ig34_p0137_a015 | 137: 2b AEMODIFY permissible | AE/assumptions.md:29 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0139_a008 | 139: 7a "Serious?" No/Yes 例句 | AE/assumptions.md:57 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0157_a0017 | 157: 4b DSSTDTC documents… | DS/assumptions.md:38 | 否 | 是 | 是 | 逐字 |
| 11 | ig34_p0141_a007 | 141: Ex3 叙述 (FA 探询, AEPRESP, RELREC) | AE/examples.md:21 | 否 | 是 | 是 | 逐字含 Section 6.4 |
| 12 | ig34_p0163_a0002 | 163: Ex9 多份知情同意 | DS/examples.md:192 | 否 | 是 | 是 | 逐字 |
| 13 | ig34_p0162_a0026 | 162: Ex8 r4 BLINDED DRUG A / TREATMENT 2 | DS/examples.md:186 | 否 | 是 | 是 | 渲染逐格一致 |
| 14 | ig34_p0155_a0019 | 155: spec STUDYID 行 | DS/spec.md:5 | 否 | 是 | 是 | |
| 15 | ig34_p0136_a007 | 136: spec AEUNANT 行 (21 CFR 812.3(s)) | AE/spec.md:410 | 否 | 是 | 是 | CT C66742 = U5 |
| 16 | ig34_p0157_a0027 | 157: 5 SDS Team 1 DSDECOD/事件 | DS/assumptions.md:43 | 否 | 是 | 是 | |
| 17 | ig34_p0156_a0020 | 156: 2b-i STUDY PARTICIPATION | DS/assumptions.md:18 | 否 | 是 | 是 | |
| 18 | ig34_p0141_a022 | 141: "Example 4" | AE/examples.md:48 | 否 | 是 | 是 | 标题 |
| 19 | ig34_p0160_a0023 | 160: Ex3 r5 789102 FOLLOW-UP 2004-12-28 | DS/examples.md:83 | 否 | 是 | 是 | 渲染逐格 |
| 20 | ig34_p0166_a0006 | 166: te.xpt r4 FU | DS/examples.md:347 | 否 | 是 | 是 | 渲染逐格; TEDUR 空 |
| 21 | ig34_p0137_a007 | 137: spec AEENRF 行 | AE/spec.md:518 | 否 | 是 | 是 | CT C66728 = U5 |
| 22 | ig34_p0160_a0019 | 160: Ex3 r1 789101 TREATMENT 2004-09-12 | DS/examples.md:79 | 否 | 是 | 是 | 渲染逐格 |
| 23 | ig34_p0163_a0016 | 163: Ex10 Row 1 screening element | DS/examples.md:216 | 否 | 是 | 是 | |
| 24 | ig34_p0161_a0011 | 161: Ex5 MDR-TB 叙述 | DS/examples.md:118 | 否 | 是 | 是 | 逐字 (含 PDF 原文残句) |
| 25 | ig34_p0167_a0003 | 167: Ex12 Rows 1-2 | DS/examples.md:391 | 否 | 是 | 是 | |
| 26 | ig34_p0157_a0026 | 157: 5 ICH E3 两段引文 | DS/assumptions.md:43 | 否 | 是 | 是 | 开引号 “ 本批补; 其余直/弯引号差 = 排版 (S-TYPO) |
| 27 | ig34_p0157_a0019 | 157: 4b DSSTDTC = Epoch 完成日 | DS/assumptions.md:38 | 否 | 是 | 是 | |
| 28 | ig34_p0164_a0013 | 164: ta.xpt r6 DG2INDG/DRUG2 | DS/examples.md:254 | 否 | 是 | 是 | 渲染逐格 |
| 29 | ig34_p0157_a0004 | 157: 3a CT depends on DSCAT | DS/assumptions.md:27 | 否 | 是 | 是 | |
| 30 | ig34_p0157_a0006 | 157: 3b-i COMPLETED from NCOMPLT | DS/assumptions.md:29 | 否 | 是 | 是 | |

独有丢失 0 / 30; 忠实度错误 0 / 30; 位置错误 0.

## 另查
- **intros §6.2** (p133 a010..a018): AE/assumptions.md:3-13 逐字 (标题 + 1 句 + 7 项), 位于 host 顶部, 标题格式同 LB/FT/NV `## §6.x` 先例. ✔
- **gaps**: AE F 脚注 AE/spec.md:546; DS D (:3-5) / S (:7-9) / A (:11) / F (DS/spec.md:150) 逐字对 p155/p156/p137. 两处脚注均在最后变量块之后、`## Cross References` 之前 (U7). ✔
- **CT `*`**: pdftotext -layout p133-137 CT 列为 `*` 的变量 = AECAT/AESCAT/AEBODSYS/AEREL/AERLDEV/AEPATT/AERLPRT/AERLPRC/AETOXGR (9), KB `Controlled Terms:** *` 恰为此 9; DS p155-156 无 `*`. ✔
- **spec 变量完整性**: AE PDF 60 变量 = KB 60 (`diff` 0); DS 16 = 16.
- **DS 原 assumption 7 删除**: PDF p156-158 列表止于 6; 原句是 p166 TA 叙述的改写且 "follow some other defined protocol" 与 PDF "or follow-up" 矛盾; PDF 原句在 DS/examples.md:349 → 删除合规 (D2).
- **DS 词级改动** (2b DSSCAT / 3b-ii codelist / 3d 去 "DSTERM and") 均与 p156-157 一致.
- **反向 KB→PDF 全文件句/格扫** (6 文件, `python3 -I $S/reverse.py` + 去空白格比对): 未命中仅 (a) `**CRF: AE Seriousness Classification**` 表前标签 (U8 导航); (b) 已登记 PDF_TYPO: AE Ex5 T-1 AEENDTC / T-2 SEQUELAE / T-3 "related to the device"; DS T-2 TESTRL "is" / T-4 epocch / T-5 recieved; (c) pdftotext 折行/连字伪阴性 (AERLPRC "device-related", AEENRTPT, 折行日期, 均目视逐字一致). 无 PDF 出处且未 D6 的行 = 0.
- **授权范围**: `git diff HEAD --stat -- knowledge_base/` 仅 AE/DS 的 assumptions.md + spec.md 4 文件 (∈ kb_files), narrow_files 空. ✔
- **G-TB8**: trace 有 writer (executor) 06:25 + delta 06:31、reviewer (code-reviewer, PASS) 06:37; KB 文件 mtime 最晚 06:31:33 < reviewer 完成, 无 reviewer 后改动; 无 agent main 写 KB. ✔
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).

## 对照 writer / reviewer (判完后读)
与 reviewer PASS 结论一致 (DS asm 7 删除依据、T-n 清单、脚注位置、CT `*` 9 项). 无分歧.
