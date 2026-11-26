# T2S.S-SPC2 Auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus), 2026-11-26. 先独立判, 判完才读 `t2_S-SPC2.md` / `t2_S-SPC2_review.md`. 只读 KB.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPC2_auditor/` (sample.py / sample_P.py / reverse.py / reverse_raw.py / forward.py / 渲染 png)

**Verdict: PASS** — 独有丢失 0, 忠实度错误 0 (N=30).

## 抽样 (可复跑; repo 根执行 `python3 -I $S/sample.py`)
```
P = pdf_atoms 中 ig34, atom_type ∈ {SENTENCE, LIST_ITEM, NOTE, CROSS_REF, TABLE_ROW},
    页 ∈ sections 各范围 (MB 248-252 / MS 252-256 / PC 267-271 / PP 271-275 / §6.3.5.7.3 256-263 / §6.3.5.9.3 275-284)
    且 parent_section 以 "§<sec> " 开头 (边界页 §6.3.5.6 LB / §6.3.5.8 MI 原子排除);
    另并入 p248-263 中 parent = "§6.3.5.7 " 的 P 类原子 (= p248 §6.3.5.7 引言 a024 + p261-263 Example 3 续页原子, 原子库把父节记成 §6.3.5.7, 内容属 §6.3.5.7.3);
    减 ledger INTENTIONAL_EXCLUDE (实减 105). intros = [] (§6.3.5.9 引言 0 原子, p267 核实仅标题).
writer 页 = S-SPC2.writer.jsonl pdf_page 集合 {248,249,251,253,255,257,262,263,267,268,269,271,272,273,274,275,277,278,279,280}; C = P 中落在 writer 页的原子.
N = min(30, max(20, ceil(0.1*|P|)), |P|); rng = random.Random(20261126); s1 = rng.sample(C, ceil(N/3)); s2 = rng.sample(sorted(P - s1), N - |s1|)
```
结果: |P| = 755, |C| = 392, N = 30 (writer 页 10 + 其余 20), seed = 20261126.

## 样本判定 (TABLE_ROW 对 130dpi 渲染逐格: p257/258/262/271/273/274/275/276/278; relrec 行对 pdftotext -layout 逐列)
| # | atom_id | PDF 页:摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0277_a017 | 277: Ex1 首句 "All PC records used…" | PC/examples.md:64 | 否 | 是 | 是 | 逐字, §6.3.5.9.3 Example 1 下 |
| 2 | ig34_p0275_a027 | 275: Method A 列表项 | PC/assumptions.md:46 | 否 | 是 | 是 | 逐字 (PC-PP Relating Records) |
| 3 | ig34_p0249_a018 | 249: spec MBSCAT 行 | MB/spec.md:131-138 | 否 | 是 | 是 | CT `*` 本批补; 7 列一致 |
| 4 | ig34_p0279_a015 | 279: Ex1 Method D relrec r21 PCSEQ 14 RELID 2 | PC/examples.md (Ex1 D 表) | 否 | 是 | 是 | 逐列 |
| 5 | ig34_p0279_a044 | 279: Ex2 Method B 句 | PC/examples.md:213 | 否 | 是 | 是 | PDF `12"` 缺开引号, KB 补 (T-10, 可自证) |
| 6 | ig34_p0257_a009 | 257: MS Ex1 r2 Sponsor Drug SUSCEPTIBLE | MS/examples.md:24 | 否 | 是 | 是 | 渲染逐格一致 |
| 7 | ig34_p0272_a021 | 272: PP asm 3a PKUNIT | PP/assumptions.md:18 | 否 | 是 | 是 | 弯/直引号 = 排版 (S-TYPO) |
| 8 | ig34_p0273_a018 | 273: PP Ex1 r9 DAY1_MET AUCALL 147.35 | PP/examples.md:24 | 否 | 是 | 是 | 渲染逐格一致 |
| 9 | ig34_p0279_a023 | 279: Ex1 Method D r29 PCSEQ 22 RELID 2 | PC/examples.md (Ex1 D 表) | 否 | 是 | 是 | |
| 10 | ig34_p0271_a011 | 271: PC Ex1 r31 DRGA_MET PLASMA 3.73 | PC/examples.md:57 | 否 | 是 | 是 | 原子串行 (A554134-19/日期取自上行); 渲染: A554134-21, PCDTC 2001-02-12T08:00, PCENDTC 空 = KB |
| 11 | ig34_p0282_a019 | 282: Ex3 Method D r24 PCSEQ 7 RELID 2 | PC/examples.md (Ex3 D 表) | 否 | 是 | 是 | |
| 12 | ig34_p0282_a013 | 282: Ex3 Method D r18 PCSEQ 1 RELID 2 | PC/examples.md (Ex3 D 表) | 否 | 是 | 是 | |
| 13 | ig34_p0272_a001 | 272: spec PPSTRESC 行 | PP/spec.md:104-111 | 否 | 是 | 是 | 渲染一致 |
| 14 | ig34_p0257_a017 | 257: MS Ex1 r10 Amoxicillin RESISTANT DISK DIFFUSION | MS/examples.md:32 | 否 | 是 | 是 | 渲染逐格 |
| 15 | ig34_p0276_a022 | 276: pc.xpt (All Examples) r16 | PC/assumptions.md:76 | 否 | 是 | 是 | 渲染逐格 (09:45/75 min/4/PT1H15M) |
| 16 | ig34_p0274_a001 | 274: PP Ex2 Row 5 Ratio AUC | PP/examples.md:47 | 否 | 是 | 是 | 逐字 |
| 17 | ig34_p0270_a006 | 270: PC Ex1 Rows 5-6 specimen properties | PC/examples.md:17 | 否 | 是 | 是 | 逐字 |
| 18 | ig34_p0280_a014 | 280: Ex2 Method D 句 | PC/examples.md:250 | 否 | 是 | 是 | PDF `"1 through "7"` 缺引号, KB 补 (T-11, 主控裁定 4) |
| 19 | ig34_p0258_a021 | 258: MB Ex2 r3 GMNROD DETECTION | MB/examples.md:78 | 否 | 是 | 是 | 渲染: VISIT 1 (原子截成 "VISIT") |
| 20 | ig34_p0280_a005 | 280: Ex2 Method C r1 PCGRPID DY1_DRGX | PC/examples.md:239 | 否 | 是 | 是 | |
| 21 | ig34_p0282_a044 | 282: Ex4 Method A r9 PPGRPID AUC RELID 3 | PC/examples.md (Ex4 A 表) | 否 | 是 | 是 | |
| 22 | ig34_p0280_a046 | 280: Ex3 Method A r4 PCGRPID DY1_DRGX_A RELID 2 | PC/examples.md:294 | 否 | 是 | 是 | |
| 23 | ig34_p0276_a020 | 276: pc.xpt r14 | PC/assumptions.md:74 | 否 | 是 | 是 | 渲染逐格 |
| 24 | ig34_p0276_a008 | 276: pc.xpt r2 | PC/assumptions.md:62 | 否 | 是 | 是 | 原子 Ex4 列误为 DY1_DRGX; 渲染 = DY1_DRGX_A = KB |
| 25 | ig34_p0283_a036 | 283: Ex4 Method D r24 PPSEQ 2 RELID 2 | PC/examples.md (Ex4 D 表) | 否 | 是 | 是 | |
| 26 | ig34_p0274_a029 | 274: PP Ex3 r5 LAMZHL 7.74 | PP/examples.md:91 | 否 | 是 | 是 | 渲染逐格; PPSTINT/PPENINT 空 |
| 27 | ig34_p0275_a003 | 275: PP Ex3 r8 PPSEQ 15 TMAX DAY 14 | PP/examples.md:94 | 否 | 是 | 是 | 渲染逐格 |
| 28 | ig34_p0262_a013 | 262: suppmb r2 MBMICERT DEFINITIVE | MB/examples.md:201 | 否 | 是 | 是 | 渲染逐格 |
| 29 | ig34_p0279_a006 | 279: Ex1 Method D r12 PCSEQ 12 RELID 1 | PC/examples.md (Ex1 D 表) | 否 | 是 | 是 | |
| 30 | ig34_p0256_a003 | 256: MS asm 2 MSDTC | MS/assumptions.md:21 | 否 | 是 | 是 | 逐字 |

独有丢失 0 / 30; 忠实度错误 0 / 30; 位置错误 0.

## 另查
- **gaps**: MB S (MB/assumptions.md `## MB – Specification` + mb.xpt 首句, 对 p249 逐字) / MB F (MB/spec.md 末变量块后) ✔; PC D (PC/assumptions.md Description/Overview, p267 逐字) / F ✔; PP D / S / A 标题 (PP/assumptions.md:3-11, p271-272 逐字) / F ✔. 4 个脚注均在最后变量块 `---` 之后、`## Cross References` 之前 (U7), 文字对 p251/255/269/272 逐字.
- **footnote_moves**: MS/assumptions.md 原 `> 1In this column…` 已删, MS/spec.md 末尾补 ✔.
- **§6.3.5.7 引言**: MB/assumptions.md:5 对 p248 a024 三句逐字 (含 em dash —) ✔. §6.3.5.9 无引言正文 → PC/assumptions.md:5 KB 自写句已 D6 ✔.
- **CT `*`**: pdftotext -layout 各 spec 页 CT 列为 `*` 的变量 = MBCAT/MBSCAT, MSCAT/MSSCAT, PCCAT/PCSCAT, PPCAT/PPSCAT; KB `Controlled Terms:** *` 恰为此 8 个 (p271/272 渲染复核 PP). PP 变量 PDF 26 = KB 26.
- **PC Ex1 Method D 句改动** (PC/examples.md:146): p278 渲染 = "…"1" through "12" and PP records with PPSEQ values "1" through "7"." KB 现逐字一致 (原 KB 多出的 "and "10" through "12"" 为错误); 原子 ig34_p0278_a051 本身串入了 p280 文字, 以渲染为准.
- **删除**: PP/examples.md "Due to space limitations…" — p271-284 无此句 (仅 p269 PC, 在 PC/examples.md:7) → 删除合规.
- **反向 KB→PDF 全文件扫** (12 文件; `pdftotext -raw` 文本, `python3 -I $S/reverse_raw.py`): 未命中 36 条 = (a) "See … for …" 导航 (MB/examples :20/:91/:207, MS/examples :7/:36/:60, PP/examples :108/:110); (b) 跨页句伪阴性 (MS/examples :11/:65 句跨 p256/257 页脚); (c) 已登记 PDF_TYPO: MS T-2 MSCONU, MS T-5 "should only populated", PP T-9 pre-corrdinating; (d) PP/examples.md:116-170 全部在 :114 D6 "entire section" 标注范围内, 内容逐条核与 p275-279 不矛盾 (Method A-D 基数/IDVAR 对 p275-276 方法列表一致). 无 PDF 出处且未 D6 的行 = 0. spec.md 4 文件 -raw 下全命中.
- **正向 prose 机械匹配** (`python3 -I $S/forward.py $S`, P 中 SENTENCE/LIST_ITEM/NOTE/CROSS_REF 对 12 文件): 未命中 8 条全部定性 = 脚注上标 1 vs ¹ (3) / 已登记 T-5、T-9 / T₁ 下标 (排版) / 原子错 (p252_a011 "assigned to" 实为 "in", p278_a051 串文). 丢失 0.
- **授权范围**: `git diff HEAD --stat -- knowledge_base/domains/{MB,MS,PC,PP}` = 11 文件, 全在 kb_files, narrow_files 空 ✔.
- **G-TB8**: trace 有 writer (executor) 07:01:34 + delta 07:05:33 + delta 2 07:12:41, reviewer (code-reviewer, PASS) 07:11:00 + delta 2 复审 07:13:20; KB 文件 mtime 最晚 PP/examples.md 07:12:41 UTC < 末次 reviewer; 无 agent main 写 KB 记录 ✔.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).

## 观察 (不计缺陷)
- O-1: PP/examples.md 的 "RELREC Method Quick Reference (PP-side view)" 整节是 PC/examples.md 内容的 KB 摘要; dispatch notes "KB 自写摘要与 PDF 重复 → 交叉引用" 也可适用, 本批按主控裁定走 D6 整节标注保留 (writer checkpoint :156 已列备选). D6 标注在、内容不矛盾 → 不计忠实错误.
- O-2: 原子库错误 4 处 (p252_a011 / p271_a011 / p276_a008 / p278_a051), KB 与渲染一致; 原子库只读, 记此备查.

## 对照 writer / reviewer (判完后读)
与 reviewer PASS 结论一致 (T-10/T-11、D6 范围 :114、space limitations 删除、CT `*` 8 项、脚注位置). 无分歧.
