# T2S.S-TDM Auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus), 2026-11-26. 先独立判, 判完才读 `t2_S-TDM.md` / `t2_S-TDM_review.md`. 只读 KB.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TDM_auditor/`

**Verdict: PASS** — 独有丢失 0, 忠实度错误 0 (N=30).

## 抽样 (可复跑; repo 根执行 `python3 -I $S/sample.py`)
```
P = pdf_atoms 中 ig34, atom_type ∈ {SENTENCE, LIST_ITEM, NOTE, CROSS_REF, TABLE_ROW}, 页 ∈ sections 范围, 且 parent_section 归属:
    TA 7.2.1 p384-402 = "§7.2.1" + [空格/./结尾] (含 §7.2.1.1 Trial Arms Issues); TD 7.3.2 p410-414; TM 7.3.3 p415;
    "7.1-7.2" p382-384 = "§7.1*" 或 "§7.2 <非[>" (§7.2 引言; 排除 §7.2.2 TE / §7.3.1.1 TV / §7.4 等边界页别节原子).
    减 ledger INTENTIONAL_EXCLUDE (实减 30); intros 空.
writer 页 = S-TDM.writer.jsonl pdf_page 集合 {382-385,389,391,393,396-398,401,410-415}; C = P 中落在 writer 页的原子.
N = min(30, max(20, ceil(0.1*|P|)), |P|); rng = random.Random(20261126); s1 = rng.sample(C, ceil(N/3)); s2 = rng.sample(sorted(P - s1), N - |s1|)
```
结果: |P| = 354, |C| = 230, N = 30 (writer 页 10 + 其余 20), seed = 20261126. 机械匹配: `python3 -I $S/match.py $S` (30/30 唯一或正确节命中).

## 样本判定 (TABLE_ROW 对 110dpi 渲染逐格: p391/393/396/397/414)
| # | atom_id | PDF 页:摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0396_a028 | 396: Ex4 ta r13 B/REST/If disease progression… | TA/examples.md:690 | 否 | 是 | 是 | 渲染逐格 |
| 2 | ig34_p0396_a020 | 396: Ex4 ta r5 A/REST | TA/examples.md:682 | 否 | 是 | 是 | 渲染逐格 |
| 3 | ig34_p0382_a012 | 382: §7.1.1 decision rules 句 | TA/assumptions.md:19 | 否 | 是 | 是 | 逐字 |
| 4 | ig34_p0398_a015 | 398: Ex6 "next diagram … retrospective view" | TA/examples.md:803 | 否 | 是 | 是 | Ex6 段 |
| 5 | ig34_p0401_a009 | 401: Ex7 TA 2-arm | TA/examples.md:981 | 否 | 是 | 是 | |
| 6 | ig34_p0383_a012 | 383: §7.1.3 Trial Disease Milestones 项 | TA/assumptions.md:50 | 否 | 是 | 是 | |
| 7 | ig34_p0414_a016 | 414: TD Ex3 td r3 ANCH2DT/P0D/P12W/17 | TD/examples.md:171 | 否 | 是 | 是 | 渲染逐格 |
| 8 | ig34_p0391_a012 | 391: Ex2 ta r2 P-5-10/P/TREATMENT 1 | TA/examples.md:338 | 否 | 是 | 是 | 渲染逐格 |
| 9 | ig34_p0391_a021 | 391: Ex2 ta r11 5-P-10/P | TA/examples.md:347 | 否 | 是 | 是 | 渲染逐格 |
| 10 | ig34_p0398_a022 | 398: Ex6 TAETORD 10 vs 8 | TA/examples.md:840 | 否 | 是 | 是 | |
| 11 | ig34_p0391_a028 | 391: Ex2 ta r18 5-10-P/10 mg | TA/examples.md:354 | 否 | 是 | 是 | 渲染逐格 |
| 12 | ig34_p0414_a003 | 414: TD Ex3 首句 | TD/examples.md:153 | 否 | 是 | 是 | 同行 "restarted)." = TD T-2 |
| 13 | ig34_p0413_a008 | 413: TD Ex2 Row 2 | TD/examples.md:98 | 否 | 是 | 是 | "+ 1 week" 照 PDF (本批改) |
| 14 | ig34_p0396_a008 | 396: Ex4 矩阵 B 行 | TA/examples.md:670 | 否 | 是 | 是 | 渲染逐格 |
| 15 | ig34_p0386_a004 | 386: asm 10a EPOCH 编号 | TA/assumptions.md:131 | 否 | 是 | 是 | |
| 16 | ig34_p0398_a024 | 398: TAETORD 主要目的 | TA/examples.md:840 | 否 | 是 | 是 | |
| 17 | ig34_p0397_a004 | 397: Ex5 cannot be blinded | TA/examples.md:701 | 否 | 是 | 是 | |
| 18 | ig34_p0393_a010 | 393: Ex3 矩阵 B-Open A | TA/examples.md:499 | 否 | 是 | 是 | 渲染逐格 |
| 19 | ig34_p0402_a014 | 402: §7.2.1.1 Example Trial 4 1-4 cycles | TA/examples.md:1007 | 否 | 是 | 是 | `## Trial Arms Issues` 下; asm 有指针 |
| 20 | ig34_p0387_a002 | 387: Examples 引言 blinded 图项 | TA/examples.md:14 | 否 | 是 | 是 | |
| 21 | ig34_p0402_a010 | 402: branch no "if" clause | TA/examples.md:1007 | 否 | 是 | 是 | |
| 22 | ig34_p0415_a003 | 415: TM Description 句 | TM/assumptions.md:5 | 否 | 是 | 是 | |
| 23 | ig34_p0402_a029 | 402: Defining Epochs unblinded | TA/examples.md:1019 | 否 | 是 | 是 | |
| 24 | ig34_p0398_a023 | 398: 括号句 TAETORD 10 for arm B | TA/examples.md:840 | 否 | 是 | 是 | |
| 25 | ig34_p0398_a011 | 398: Ex6 3-week/4-week cycles | TA/examples.md:783 | 否 | 是 | 是 | |
| 26 | ig34_p0397_a022 | 397: Ex5 ta r5 RESTA | TA/examples.md:768 | 否 | 是 | 是 | 渲染逐格 |
| 27 | ig34_p0397_a024 | 397: Ex5 ta r7 RESTA TATRANS 空 | TA/examples.md:770 | 否 | 是 | 是 | 渲染逐格 |
| 28 | ig34_p0391_a016 | 391: Ex2 ta r6 10 mg TREATMENT 3 | TA/examples.md:342 | 否 | 是 | 是 | 渲染逐格 |
| 29 | ig34_p0401_a002 | 401: 图不按比例句 | TA/examples.md:931 | 否 | 是 | 是 | |
| 30 | ig34_p0384_a023 | 384: Description 第 2 项 | TA/assumptions.md:86 | 否 | 是 | 是 | |

独有丢失 0 / 30; 忠实度错误 0 / 30; 位置错误 0.

## 另查
- **P 全量机械正扫** (`python3 -I $S/fullP.py $S`): 354 中 347 命中; 7 未命中逐条处置: p385 a001/a004 = spec 行 (KB spec 为字段格式, 逐字段对 layout 一致; ARMCD Notes 跨页); p389 a012/a013 = 原子错 (TABRANCH 串行, layout/KB 均为 r2 "Randomized to Placebo"); p396 a009 = 原子错 ("represents", 渲染 p396 为 "represented" = KB); p411 a009 / p415 a012 脚注 = "1In"/"¹In" 写法差.
- **gaps**: TA A (`## TA – Assumptions` :110) + F (TA/spec.md:96); TD D/S/A (TD/assumptions.md:3-11, Description 句与 spec 首句逐字对 p410) + F (TD/spec.md:87); TM A (TM/assumptions.md:11, 另补 S 标题 :7) + F (TM/spec.md:51). 三处脚注逐字对 p385/p411/p415, 均在最后变量块之后、`## Cross References` 之前 (U7). ✔
- **CT `*`**: pdftotext -layout p384-385 CT 列 `*` = ARMCD/ARM/ETCD/ELEMENT (4) = KB 4; TD/TM PDF 无 `*`, KB 无. EPOCH C99079 / TMRPT C66742 / DOMAIN 空 = U5/U6 归 S-CT, 不计. 变量数 TA 10 / TD 9 / TM 5 = PDF.
- **TD 改动逐项对 p410-414 渲染/文字**: asm 1 "within oncology" + 末 3 句、asm 2 "e.g." 无逗号、"+ 1 week"/"- 3 days"、"start of period 2"、Ex3 bullet 3 "every 24 weeks" + 末句 (PDF 原文; 与图/表 12 周矛盾 = PDF 内部不一致, 已登记 TD U-1 → T4)、TD 顶段删除 (D-1: 为 asm 1 改写副本, asm 1 已逐字承载). ✔
- **Mermaid (TD Ex1-3 对 r412/r413/r414; TA Ex6 两图对 r398)**: 节点顺序/分组/锚点/schedule 区间与 PDF 图一致; TD Period 2 / Extension 刻度 X8-X32 / X12-X48 与 PDF 一致; "et cetera, until disease progression or death" 照图. 均有 D6 注. TA Ex6 schema 对 B 也画了 repeat 边 (PDF schema 只画一条弧线, 但退省图两臂均 "Repeat until disease progression"), 逻辑不矛盾, 不计.
- **反向 KB→PDF 全 9 文件** (`python3 -I $S/reverse.py $S`, -raw 去非字母数字比对): 未命中仅 (a) 导航: `> See …` 指针 ×4、`> Class|Structure` 行、Cross References 块 (U8); (b) D6 标注块 (TA ex 22/165/361/525/529 解释性注经核与 PDF 不矛盾; Mermaid 前注 + TD 粗体图题由 D6 注覆盖); (c) U5 C-code; (d) TA asm:36 "3 study cells" = 已登记 TA T-1; (e) ARMCD Notes 跨页伪阴性. 无 PDF 出处且未 D6 的行 = 0.
- **授权范围**: `git diff HEAD --stat -- knowledge_base/domains/{TA,TD,TM}` = 7 文件 (TA asm/spec, TD asm/ex/spec, TM asm/spec) ⊂ kb_files; narrow_files 空. `## TA-Specific Assumptions` 删除: `grep -rn "ta-specific-assumptions|TA-Specific" knowledge_base web/src` = 0 入站, 符合 S-TDM 主控口径.
- **G-TB8**: trace 有 writer (executor) 07:28:52Z + delta 07:29:51Z、reviewer (code-reviewer, PASS, 含 D-5) 07:35:50Z; KB 文件最晚 mtime 16:29:51 JST = 07:29:51Z < reviewer 完成; 无 agent main 写 KB. ✔
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).
- 观察 (不计): §7.1/§7.2 KB 自拟 H2 标题文字 ≠ PDF (B-TA X-4, 主控已裁规则 6 不改); TM `## TM — Description/Overview` 用 em dash (既有, S-TYPO).

## 对照 writer / reviewer (判完后读)
与 writer 登记 (TA T-1 study cells、TD T-1..T-4、U-1..U-3、原子错 p396_a009) 及 reviewer PASS (CT * 4=4、脚注 U7、Mermaid 3 图、D-1/D-5) 一致. 无分歧.
