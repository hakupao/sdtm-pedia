# T2S.S-FND Auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus), 2026-11-26. 先独立判, 判完才读 `t2_S-FND.md` / `t2_S-FND_review.md`. 只读 KB.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-FND_auditor/` (sample.py / judge.py / reverse.py / reverse2.py / forward.py + 渲染 png)

**Verdict: PASS** — 独有丢失 0, 忠实度错误 0 (N=30).

## 抽样 (可复跑; repo 根执行 `python3 -I $S/sample.py`)
```
P = pdf_atoms 中 ig34, atom_type ∈ {SENTENCE, LIST_ITEM, NOTE, CROSS_REF, TABLE_ROW},
    页 ∈ sections 范围 (EG 185-192 / OE 298-305 / UR 312-315 / PE 315-318 / SS 342-344)
    且 parent_section 以 "§<sec> " 或 "<XX> – " 开头 (SS 原子 parent 记为 "SS – Specification" 等, 故加后者; 边界页 DD/NV/RP/RE/QRS/SC/TU 原子排除),
    减 ledger INTENTIONAL_EXCLUDE (实减 25: SS spec 行 p342-343、OE p305 RP 行等), 并入 intro ig34_p0180_a0002 (a0001 为 HEADING).
writer 页 = S-FND.writer.jsonl pdf_page 集合 {180,185,186,188,298,299,301,304,312,313,314,315,316,317,342,343,344}; C = P 中落在 writer 页的原子.
N = min(30, max(20, ceil(0.1*|P|)), |P|); rng = random.Random(20261126); s1 = rng.sample(C, ceil(N/3)); s2 = rng.sample(sorted(P - s1), N - |s1|)
```
结果: |P| = 391 (EG 129 / OE 132 / UR 63 / PE 54 / SS 12 / intro 1), |C| = 219, N = 30 (writer 页 10 + 其余 20), seed = 20261126.
注: pdf_atoms 原子文本有抽取噪声 (OETPT "alphanumeric code", EGSTRESN "For continuous", OEEEXAM, "installation", OE Ex2 行错位等), 一律以 PDF 文本层 + 渲染为真值判定.

## 样本判定 (TABLE_ROW 对 130dpi 渲染逐格: p191/p192/p302/p304/p305/p315; spec 行对 pdftotext 逐列)
| # | atom_id | PDF 页:摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0313_a011 | 313: spec URSTAT 行 | UR/spec.md URSTAT 块 | 否 | 是 | 是 | CT C66789 vs (ND) = U5, 不计 |
| 2 | ig34_p0313_a003 | 313: spec URCAT 行, CT * | UR/spec.md URCAT 块 | 否 | 是 | 是 | CT `*` 本批补 |
| 3 | ig34_p0185_a029 | 185: spec EGGRPID 行 | EG/spec.md EGGRPID 块 | 否 | 是 | 是 | |
| 4 | ig34_p0315_a012 | 315: UR Ex2 r1 BLDFLRT 20 mL/min BILATERAL | UR/examples.md:31 | 否 | 是 | 是 | 渲染逐格一致 |
| 5 | ig34_p0316_a005 | 316: spec PE STUDYID 行 | PE/spec.md STUDYID 块 | 否 | 是 | 是 | |
| 6 | ig34_p0186_a012 | 186: spec EGSTRESN 行 | EG/spec.md:160-165 | 否 | 是 | 是 | 原子 "For…" 抽取错; 文本层 "Used for…" = KB |
| 7 | ig34_p0301_a016 | 301: OE Ex1 引言句 | OE/examples.md:5 | 否 | 是 | 是 | 逐字 |
| 8 | ig34_p0304_a009 | 304: di.xpt r4 SERIAL yyyyyy | OE/examples.md:115 | 否 | 是 | 是 | 渲染 yyyyyy (原子 yyyyy 抽取错) |
| 9 | ig34_p0315_a019 | 315: PE CDASH Best Practice 首句 | PE/assumptions.md:11 | 否 | 是 | 是 | 逐字 (段落拆分 = S-FND 主控口径不改) |
| 10 | ig34_p0299_a021 | 299: spec OEORNRHI 行 | OE/spec.md OEORNRHI 块 | 否 | 是 | 是 | |
| 11 | ig34_p0315_a026 | 315: PE Description 句 | PE/assumptions.md:25 | 否 | 是 | 是 | 本批补 (gap D), 位于 Alignment 段后 = PDF 顺序 |
| 12 | ig34_p0315_a022 | 315: worsening abnormalities → AE form | PE/assumptions.md:17 | 否 | 是 | 是 | 逐字 |
| 13 | ig34_p0300_a001 | 300: spec OESTNRHI 行 | OE/spec.md OESTNRHI 块 | 否 | 是 | 是 | |
| 14 | ig34_p0188_a015 | 188: EG asm 8 EGNRIND / Section 4.5.5 | EG/assumptions.md:28 | 否 | 是 | 是 | 交叉引用在 |
| 15 | ig34_p0303_a003 | 303: suppoe r1 OEEDILST DILATED | OE/examples.md:59 | 否 | 是 | 是 | 文本层逐格一致 |
| 16 | ig34_p0301_a005 | 301: spec OETPT 行 | OE/spec.md OETPT 块 | 否 | 是 | 是 | 原子 "alphanumeric code" 抽取错; 文本层 "elapsed time" = KB |
| 17 | ig34_p0192_a009 | 192: EG Ex4 r7 RRSM 661 | EG/examples.md:109 | 否 | 是 | 是 | 渲染 "RR Interval, Single Measurement" = KB, 22 列 |
| 18 | ig34_p0313_a012 | 313: spec URREASND 行 | UR/spec.md:201 | 否 | 是 | 是 | |
| 19 | ig34_p0189_a011 | 189: Ex1 Row 11 Technical Quality | EG/examples.md:17 | 否 | 是 | 是 | 逐字 |
| 20 | ig34_p0313_a007 | 313: spec URSTRESC 行 | UR/spec.md:156 | 否 | 是 | 是 | |
| 21 | ig34_p0316_a015 | 316: spec PESCAT 行, CT * | PE/spec.md PESCAT 块 | 否 | 是 | 是 | "–CAT"/"--CAT" 仅排版 (S-TYPO) |
| 22 | ig34_p0314_a001 | 314: spec UR TAETORD 行 | UR/spec.md:318 | 否 | 是 | 是 | |
| 23 | ig34_p0302_a029 | 302: OE Ex2 r8 CUPDISC 0.6 LEFT | OE/examples.md:51 | 否 | 是 | 是 | 渲染逐格 (RATIO/0.6/0.6/RATIO/INVESTIGATOR/SCREENING/2012-04-20); 原子错位 |
| 24 | ig34_p0302_a023 | 302: OE Ex2 r2 COLOR BLUE IRIS LEFT | OE/examples.md:45 | 否 | 是 | 是 | 渲染逐格 21 列; 原子错位 |
| 25 | ig34_p0317_a011 | 317: PE spec 脚注 1 | PE/spec.md:276 | 否 | 是 | 是 | 本批补, 最后变量块后 / Cross References 前 (U7) |
| 26 | ig34_p0302_a005 | 302: OE Ex1 r3 OEEXAM RED SPOT VISIBLE | OE/examples.md:16 | 否 | 是 | 是 | 渲染 OEEXAM = KB (原子 OEEEXAM 抽取错) |
| 27 | ig34_p0302_a009 | 302: suppoe r1 OEDIR1 SUPERIOR | OE/examples.md:24 | 否 | 是 | 是 | USUBJID "XXX- 450-110" PDF 内空格 = 排版 |
| 28 | ig34_p0191_a014 | 191: EG Ex3 r17 PRAG 179 2 HR | EG/examples.md:80 | 否 | 是 | 是 | 渲染逐格; "…" vs "..." 仅排版 |
| 29 | ig34_p0305_a004 | 305: suppoe OECAT OCULAR COMFORT OERESCRT 10-point VAS | OE/examples.md:153 | 否 | 是 | 是 | 渲染逐格一致 (原子乱序) |
| 30 | ig34_p0187_a018 | 187: spec EGDTC 行 | EG/spec.md:340 | 否 | 是 | 是 | |

独有丢失 0 / 30; 忠实度错误 0 / 30; 位置错误 0.

## 另查
- **intro §6.3** (p180 a0001 标题 + a0002 句): DA/assumptions.md:3-5 逐字, 在 `# DA — Assumptions` 之后、`## DA – Description/Overview` 之前 (U3); PDF 句末冒号后无列表 (p180 文本层直接接 6.3.1), KB 同. DA diff 仅此 4 行 (narrow 合规). ✔
- **gaps** 逐字 (对 p185/188/298/299/301/312/314/315/316/317/342/343 文本层, 含续行): EG S (asm:7-9) + F; OE D/S/A + F; UR D/S/A + F (首句 "per per" 照录 = U-1 T4); PE D/S + F; SS D/S/A + F. 5 个脚注均位于最后变量块 `---` 之后、`## Cross References` 之前 (U7). ✔
- **CT `*`**: 文本层 spec 页 CT 列为 `*` 的变量 = EG {EGCAT, EGSCAT} / OE {OETSTDTL, OECAT, OESCAT} / UR {URTSTDTL, URCAT, URSCAT} / PE {PETESTCD, PETEST, PECAT, PESCAT} / SS {SSCAT, SSSCAT} = 14; KB `Controlled Terms:** *` 恰为此 14. 页内无其他 `*` 行. ✔
- **spec 变量完整性/顺序**: EG 44 / OE 52 / UR 43 / PE 30 / SS 22, PDF 与 KB 变量序列一致 (diff 0).
- **PE T-1** laterallity→laterality: p316 文本层确为 "laterallity"; 同行 Label "Laterality" → PDF 自身可定, 合规. **OE census_items** T-1 IDVARAL / T-2 OCCULAR×4: p304 渲染确认 PDF 原值, KB 正确值 (同文件 supp 表头 IDVARVAL; p305 suppoe "OCULAR COMFORT") 合规.
- **SS/examples.md** 新增 `**ss.xpt**` 表前标签 = p344 原有 (U8 导航).
- **反向 KB→PDF 全文件扫** (15 kb_files, Cross References 前; `reverse.py` 句/格 → `reverse2.py` 保序 token 复核): 未命中仅 (a) `> Class: … | Structure:` 行 (U8 导航); (b) PE T-1 laterality (已登记); (c) C-code/Order 字段 (U5 / KB 元数据, 不计). 无 PDF 出处且未 D6 的行 = 0; 本批文件无 `KB note` 行.
- **正向 P prose 全 114 原子机械匹配** (`forward.py`): 100 精确; 14 未命中 = 脚注上标 "1In"→"¹In" ×5 + 原子抽取噪声 9 (EG Ex3 "10-second" 缺词, OE asm 1-3 / Ex1 Rows 折行, "installation") — 均对文本层/渲染逐字确认 KB 一致.
- **授权范围**: `git diff HEAD --stat -- knowledge_base/domains/{EG,OE,UR,PE,SS,DA}` = 12 文件, 均 ∈ kb_files 或 narrow_files. ✔
- **G-TB8**: trace 有 writer (executor) 06:55:38Z、reviewer (code-reviewer, PASS) 07:07:49Z; 本批 KB 文件 mtime 最晚 06:51:24Z < reviewer 完成; 无 agent main 写 KB. ✔
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).

## 对照 writer / reviewer (判完后读)
与 reviewer PASS 一致 (CT `*` 14/14、5 域变量、T-1/U-1 依据、census_items 渲染、无出处 0). reviewer L-1 (UR/spec.md:3 Class 行同含 "per per") 同意随 U-1 一并裁. 无分歧.
观察 (不阻断): `evidence/audit_matrix.md` 仅 1 行 (S-INT auditor 行), 与根 `audit_matrix.md` 分裂, 主控可合并.
