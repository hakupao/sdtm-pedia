# T2 B-TA reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: CONDITIONAL** — 叙述 / 表格 / 删除 / PDF_TYPO / fp / census / links 全部通过; 唯一阻断项 = Mermaid 图中标签与 PDF 图不一致 (dispatch notes "图逻辑/标签须与 PDF 一致"; 分支/顺序逻辑全部一致). 修正清单见末节 (纯标签替换, 不涉及正文).

审查范围: `git diff 466e0c3 -- knowledge_base/domains/TA/` (只 TA; 其他目录 diff 属并行批 / 已提交批, 不在本审范围). TA/spec.md 未改.
真值: `work/pdf_pages/ig34_p0382-0402.txt` + 渲染 (scratch `t2_B-TA_reviewer/p-382..401.png` 90dpi, `h-400/h-401.png` 150dpi).

### 命令 (可复跑; S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-TA_reviewer)
```
pdftoppm -f 382 -l 401 -r 90 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p ; pdftoppm -f 400 -l 401 -r 150 -png ... $S/h
python3 -I -c "...manifest..."   # 同 prompt
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  → exit 1; "KB tables: 15; status: {'UNPARSEABLE': 8, 'OK': 7}; PDF_ONLY: 332; cells compared: 1221; diffs: 0"
  exit 1 来自全局 PDF_ONLY; 页码落在 p382-404 的 PDF_ONLY = 0 (p380-381 属 ch08/RELREC, p405-409 属 B-TE/TV)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  → RED, 48 回归; 按页: p118/174/215/218/254-263/363-374 = 并行批 (AE/GF/ch04/MB/MS/FA 等), TA 页段仅 ig34_p0396_a009
隔离复核 (只换 TA 两文件): cp -R knowledge_base $S/before/; git show 466e0c3:knowledge_base/domains/TA/{assumptions,examples}.md > $S/before/...
python3 -I .../fp_match.py --kb-root $S/before/knowledge_base --out $S/fp_before_iso.jsonl   → exit 0
python3 -I .../fp_match.py --out $S/fp_after_iso.jsonl --baseline $S/fp_before_iso.jsonl --regress-out $S/fp_regress_iso.jsonl
  → "regressions=1 new_hits=42"; "REGRESS ig34_p0396_a009 EQUIVALENT §7.2.1 Trial Arms (TA) – Example 4"
  a009 = 原子抽取错: 原子 "arrow represents this rule", PDF p396 文本与渲染均为 "represented this rule" (grep -c → 1). 预期回归, 接受.
17 atoms 目标文件直查 (norm(verbatim) in TA 两文件): 17/17 HIT.
python3 -I $S/tools/scan2.py 382 402 knowledge_base/domains/TA/assumptions.md knowledge_base/domains/TA/examples.md > $S/scan2.txt   (双向逐句; 97 行全读)
python3 tools/check_links.py | grep "live docs"  → "broken relative links: 18668 (live docs: 42)"
```

### 问题表
| ref | 检查项 | 问题 | 证据 (PDF 页 + ≤25 词) |
|---|---|---|---|
| examples.md:753 | Mermaid 标签 (Ex7 Prospective) | epoch 名 "Follow-up Epoch" | p400/p401 图: 列头 "Follow Epoch" |
| examples.md:763-764 | Mermaid 标签 | "If progression" | p400 图: "If disease progression" (两处) |
| examples.md:765 | Mermaid 标签 | "Not eligible for surgery" | p400 图: "If not eligible for surgery" |
| examples.md:585-586 | Mermaid 标签 (Ex5 Retrospective) | "Rest A" / "Rest B" | p397 图: 两行均为 "Rest" ("Drug A | Rest", "B | Rest") |
| examples.md:663-664 | Mermaid 标签 (Ex6 Retrospective) | "Rest A"/"Rest B" + "(3-week cycles)"/"(4-week cycles)" | p398 图: "Rest"; 注 "Total length Drug A cycle: 3 weeks" / "Total length Drug B cycle: 4 weeks" |
| examples.md:39-41, 163-165, 304-309, 422-423, 561-562, 639-640 | Mermaid 标签 (Study Schema 边) | 边标签 "Randomized to …" / "P-5-10…" / "Response: Open A/Rescue" 非 PDF 图内容 (取自 ta.xpt / KB 自造) | p387/389/392/394/397/398 图: 仅 "Randomization" 注释 (Ex3 另有 "Response Evaluation") |
| (非阻断) examples.md:217-219, 348-350, 454-456, 772-774 | 图缺失 | Ex2/3/4/7 Retrospective 只有 KB note 文字, 无图; p401 图注 "*Disease evaluation earlier…" 第 3 处无落点 | FIGURE 原子口径 (同 ch02 p15), 不判缺 |
| (非阻断) examples.md:782 | Ex7 TDM CR 行 | PDF CR 两个 "Chemo" 为跨列宽格 (跨 3-5w Rest+Surgery / 4-6w Rest+Chemo+Chemo); KB 左对齐到第 4、5 格 | p401; Markdown 无跨列, 同 Ex6 B 行惯例, 接受 |
| (非阻断) assumptions.md:3, :74, :152 | KB 自拟 H2 | "Trial Design Model Overview (§7.1)" / "Trial Arms and Trial Elements (§7.2)" / "TA-Specific Assumptions" 与 PDF 标题不同 (writer X-4 只提了 §7.1); 节号真实存在, 非伪节号; 纯导航 | p382 "7.1 Introduction to Trial Design Model Datasets"; p384 "7.2 Experimental Design (TA and TE)", "TA – Assumptions" |
| (非阻断) assumptions.md:40 | Concept 表 Treatments 格 | PDF 格内 3 个 bullet 被拍平成连续句; 文字逐句齐全 (未触碰, 既有) | p383 |
| (延后) assumptions.md:102-150 | X-1 | TE Issues (p405-407) 跨文件重复 → B-TE 处理, 本批不判 | — |

无 G-TB6 无出处正文: 双向扫描 KB→PDF 未命中的全部是 KB 自拟标题、2 条交叉引用、D6 `KB note` 行 (29 条, 逐条核不矛盾, 见下) 与 X-1 段; PDF→KB 未命中只有 spec 表 (属 spec.md)、TDM 表 (另行逐格)、T-2 (KB 有意补句点)、p402 TE Overview (B-TE).

### (1) 叙述逐句 (scan2 双向 + 逐段对渲染)
- Ex1 :49 :74 :102 :124 :134 / Ex2 :154 :169 :215 :221 :253 :263 / Ex3 :295 :317 :346 :352 :375 :386 / Ex4 :452 :514 :523 / Ex5 :552 :572 :596 :605 / Ex6 :630 :650 :674 :683 / Ex7 :710 :712 :732 :734 :770 / Issues :811-823 — 全部逐句命中 PDF, 位置 = PDF 图前/图后顺序一致.
- Ex5 :552 "the total length of the cycle is the same for both treatments" = p397 (旧 KB "cycle lengths differ" 已删, O10 修正). ✓
- Ex7 :712 "chemotherapy and radiotherapy plus surgery (CRS)" (旧 "radiotherapy only (R)" 已删); "will receive further chemotherapy" (旧 "further evaluation" 已删); 补 "but does include a text-based representation …" / "All subjects receive induction …" / "After induction chemotherapy and radiation …". ✓ p399
- Ex7 :710 "nothing like a one-to-one match between the elements" / "periods of time that will be compared in analyses of the trial" (旧 KB 自造 "Section 7.1.2" 交叉引用已删). ✓ p399
- §7.2 引言 assumptions.md:76/:78 = p384 两段逐字; spec 首句 :92 "ta.xpt, Trial Arms — Trial Design. One record per planned Element per Arm, Tabulation." = p384 逐字; 标题样式与本文件其他 `### §7.2.1 Trial Arms (TA) – …` 一致 (CM 先例为 `## CM – Specification`, 层级随文件). ✓
- 单词级恢复: examples.md:5 "assigned to the arm"; assumptions.md:170 "degree of similarity across arms"; :811 "a branch in the trial design appears"; :819 "first branch point in a trial"; :823 "will be included in the comparison"; :523 "represented this rule". 均 = PDF. ✓

### (2) 人工逐格 (对渲染)
Concept 表 (assumptions.md:31-41, 对 p382-383 渲染; 每格逐句脚本 + 目视):
| 行 | 结果 |
|---|---|
| 表头 Concept / Definition | 一致 |
| Trial design / Epoch / Arm | 一致 |
| Study cell | 一致; "one of 3" = PDF; "3 study cells" = T-1 (PDF "3 study cell") |
| Element / Study cells and elements / Branch / Visit | 一致 |
| Treatments | 文字一致 (PDF 3 个 bullet 拍平, 既有, 非阻断) |

Ex7 TDM (examples.md:780-783, 对 h-401 150dpi):
| 行 | 格 1-10 | 结果 |
|---|---|---|
| 表头 | '' / Screen / Induction / '' / Continuation / '' / '' / '' / '' / Follow-up | 一致 (Induction 跨 2, Continuation 跨 5) |
| CR | **CR** / Screen / Initial Chemo + RT / Chemo + RT (non-Surgery) / Chemo / Chemo / '' / '' / '' / Off Treatment Follow-up | 内容一致; 两 Chemo 跨列宽格 → 左对齐 (惯例) |
| CRS | **CRS** / Screen / Initial Chemo + RT / Chemo + RT (Surgery) / 3-5 w Rest / Surgery / 4-6 w Rest / Chemo / Chemo / Off Treatment Follow-up | 一致 (PDF 行末空伪格不复制, 接受) |

Ex1-6 TDM (未改, census UNPARSEABLE → 对渲染): Ex1 :128 表头+3 行一致 (Run-in 小写 i, PLACEBO/DRUG A/DRUG B 大写); Ex2 :257 表头+3 行一致; Ex3 :379 表头+4 行一致; Ex4 :518 表头 (Treatment 跨 8)+2 行一致; Ex5 :600 表头 (跨 6)+2 行一致; Ex6 :678 A 行一致, B 行 6 格左对齐+2 空 (PDF 宽格, 惯例). ta.xpt Ex1-7 census OK diffs 0.

### (3) Mermaid (20 个 = 原 19 + 新 5 options; 每个前有 D6 `KB note … rendering of the PDF figure "<PDF 图题>"`, 20 个图题逐字 = PDF 图题)
| # | 行 | 图 | 逻辑 (分支/顺序) | 标签 |
|---|---|---|---|---|
| 1-4 | :36 :55 :80 :108 | Ex1 Schema/Prosp/Retro/Blinded | 一致 | Schema 边标签 "Randomized to …" 非图内容 (见修正 3) |
| 5 | :160 | Ex2 Schema | 一致 (3 臂序列) | 边标签 P-5-10 等非图内容 |
| 6-7 | :175 :227 | Ex2 Prosp/Blinded | 一致 (单 Screen 分叉) | epoch 名 = PDF ✓ |
| 8 | :301 | Ex3 Schema | 一致 | "Response: Open A/Rescue" 自造 |
| 9-10 | :323 :358 | Ex3 Prosp/Blinded | 一致 (单 Screen, 单 Drug A/B) | Double Blind / Open Treatment Epoch ✓ |
| 11-14 | :419 :435 :464 :496 | Ex4 | 一致 (3 条绿箭头自 rest1-3) | Schema 边标签 |
| 15 | :558 | Ex5 Schema | 一致; 周期注 3/3 weeks ✓ | 边标签 |
| 16 | :578 | Ex5 Retro | 一致 | **Rest A/Rest B ≠ PDF "Rest"** |
| 17 | :636 | Ex6 Schema | 一致; 3/4 weeks ✓ | 边标签 |
| 18 | :656 | Ex6 Retro | 一致 | **Rest A/B, "(n-week cycles)" ≠ PDF** |
| 19 | :718 | Ex7 5 options (新) | 一致: 上路 Chemo+Rad* → Follow② 或 Chemo+Boost→Chemo→Follow⑤; 下路 Chemo+Rad** → 3-5w Rest→Surgery→4-6w Rest→Chemo→Chemo→Follow③ / Chemo→Chemo→Follow④ / Follow①; 评估注释 ✓; 图注 :730 ✓ | ✓ |
| 20 | :740 | Ex7 Prosp | 一致 (单 Screen; CR/CRS 两路; 进展→FU; 不合格→第 1 个 Chemo) | **"Follow-up Epoch"/"If progression"/"Not eligible for surgery" ≠ PDF**; 图注 :768 ✓ |
- D-13 (删 KB 自绘 "Study Schema (2-arm model)"): PDF 无此图 (p399-401 只有 5 options / Prospective / Retrospective), 主控裁定删; 新 5 options 图放在 "…might suggest that the trial has 5 arms." 之后 = PDF 位置, "However … as illustrated in the following diagram." 现紧接 Prospective 段与图, 同 PDF. ✓

### (4) 删除清单签字
| D | 判定 | 去向 / 依据 |
|---|---|---|
| D-1 assumptions Ex2 6 段 | ✓ | examples.md:154/169/215/221/253/263 逐字 (scan 命中); 原处一行交叉引用 assumptions.md:96 (D2 去重, 允许) |
| D-2 assumptions §7.2.1.1 12 句 | ✓ | examples.md:811/813/815 逐字 (含补全的 2 段); 交叉引用 :100 |
| D-3 Ex2 摘要首句 | ✓ | "7 epochs … 3 Rest (washout) Epochs" 与 p390 图 (First/Second Rest 共 2 个) 矛盾 |
| D-4 Ex3 摘要 3-4 句 | ✓ | = examples.md:386 (p394 原文) |
| D-5 Ex6 改写段 | ✓ | :630 + :674 原文 |
| D-6 Ex6 TAETORD 改写 | ✓ | :683 原文 (含括号句) |
| D-7 Ex5 摘要 | ✓ | :552/:596; 末句与 p397 相反 |
| D-8 Ex7 旧改写段 | ✓ | :710/:712/:732/:734/:770 原文 |
| D-9 Ex7 retro 次句 | ✓ | 与 p400 "an artifact of the diagram conventions" 矛盾 |
| D-10 / D-11 | ✓ | 同文件移位 (assumptions :78; examples :375/:523), 非删除 |
| D-12 Ex2 retro 首句 | ✓ | "Same structure as the Prospective View" 与 p390 图 (Prosp 单 Screen, Retro 每臂一块) 不一致 |
| D-13 2-arm Mermaid | ✓ | 见 (3) |
无 PDF 支撑内容丢失 (PDF→KB 扫描 p382-402 叙述 0 缺).

### (5) PDF_TYPO
| T | 判定 |
|---|---|
| T-1 "3 study cell" → cells | ✓ 同句/同格复数, PDF 自身可定 |
| T-2 补句点 | ✓ 两句界明确 |
| T-3 "(Open DRUG X and Rescue)" 照录 | ✓ 无法自定 → T4 |
| T-4 Ex2 Row 15 en dash | ✓ 同表其他行 "-", 登记 |
| T-5 "Example 7 in Section 5.2" 照录 | ✓ 与 §7.2.1.1 "DM Example 3" 冲突无法自定 → T4 |

### (6) D6 KB note 逐条 (不矛盾确认)
:22 Ex1 摘要 ✓ (3 epochs、Run-In 末随机 = p387-389); :152 "Each arm represents a different order of treatments" ✓ (p389); :219 "Arm labels: P-L-H, L-P-H, L-H-P" ✓ (p390 图箭头标签); :293 Ex3 摘要 ✓ (4 arms = ta.xpt ARM); :350 ✓ (p393 图); :409 :413 :456 ✓ (p394-395, 最多 4 周期); :774 ✓; 20 条 Mermaid D6 ✓.

### R2 recheck
t2_recheck[] 为空 → 无判定项.

### G-TB6 结构行签字
新增 `### §7.2.1 Trial Arms (TA) – Specification` (assumptions.md:90) ✓; 交叉引用 assumptions.md:96 / :100 (目标锚 `examples.md#example-2`、`examples.md#distinguishing-between-branches-and-transitions` 均存在) ✓; 新标签 `**Study Schema with 5 "options"**` examples.md:714 ✓ (= PDF 图题片段); 20 条 Mermaid D6 行 ✓; 图注 :730 :768 ✓; Ex7 TDM 表头/分隔线 :780-781 ✓. 其余标题未变 (diff 只有 Specification 一个新标题).

### CONDITIONAL 修正清单 (writer attempt 2; 只改 examples.md Mermaid 标签, 改后回 reviewer 复审 delta)
1. Ex7 Prospective (:740-766): `FE["Follow-up Epoch"]` → `FE["Follow Epoch"]`; `"If progression"` ×2 → `"If disease progression"`; `"Not eligible for surgery"` → `"If not eligible for surgery"`.
2. Ex5 Retrospective (:585-586): `Rest A` / `Rest B` → `Rest`. Ex6 Retrospective (:663-664): `Rest A`/`Rest B` → `Rest`; `(3-week cycles)` / `(4-week cycles)` → PDF 注 "Total length Drug A cycle: 3 weeks" / "Total length Drug B cycle: 4 weeks" (可仿 Ex6 Schema 的 note 节点).
3. Study Schema 边标签与 PDF 图对齐: Ex1 (:39-41) / Ex3 (:304-305) / Ex4 (:422-423) / Ex5 (:561-562) / Ex6 (:639-640) 的 `"Randomized to …"` 与 Ex2 (:163-165) 的 `"P-5-10"` 等 → `"Randomization"` (或去标签); Ex3 (:306-309) `"Response: Open A"` / `"Response: Rescue"` → `"Response Evaluation"`. (低严重度, 但同属 "标签须与 PDF 一致", 一并修.)

## attempt 2 复审 (delta; 2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: CONDITIONAL** (①②③ 全部修对; 但按主控口径 "PDF 图有对应文字/箭头则应补", 各视图右侧 arm 箭头标签 PDF 有字 → 须补)

命令: attempt 1 版本复原 = `git archive 466e0c3 knowledge_base/domains/TA | tar x` + `git apply evidence/failures/t2_B-TA_attempt_1.patch` → `diff` 当前 examples.md (assumptions.md 无变化). delta 共 13 处, 全部在 mermaid 块内.
| delta 行 | 新标签 | PDF 渲染 | 结果 |
|---|---|---|---|
| :39-41 / :163-165 / :304-305 / :422-423 / :561-562 / :639-640 | "Randomization" | p387/389/392/394/397/398 图注释 "Randomization" | 一致 |
| :306-309 | "Response Evaluation" | p392 "Response Evaluation" | 一致 |
| :585-586 | "Drug A \| Rest" / "B \| Rest" | p397 retro | 一致 |
| :663-664 | Rest + "Total length Drug A cycle: 3 weeks" / "…Drug B cycle: 4 weeks" | p398 retro 注 | 一致 |
| :746-751 | "Chemo + Rad" / "Chemo + Rad*" / "Chemo + Rad**" / "Chemo + Boost" / "3-5 w Rest" / "4-6 w Rest" | p400 prosp (h-400) | 一致 |
| :753 | "Follow Epoch" | p400 | 一致 |
| :763-765 | "If disease progression" ×2 / "If not eligible for surgery" | p400 | 一致 |
保留项判定:
- Ex7 5 options "Follow (option N)": PDF 图右侧 "Options" 列编号 ①-⑤ 的转写 → 可接受.
- arm 箭头未画: PDF 图中均为带字箭头 → 按口径**应补** (修正 ④).
fp 隔离 (baseline = $S/fp_before_iso.jsonl): regressions=1 仅 ig34_p0396_a009 (预期); check_links live docs 42.

### 修正 ④ (writer attempt 3; 只改 examples.md mermaid, 每图在末节点后加 arm 箭头标签节点, 如 `P --- armP(["Placebo"])`, 文字逐字照 PDF)
- Ex1 Prosp/Retro (:55/:80): Placebo / Drug A / Drug B; Ex1 Blinded (:108): Blind
- Ex2 Prosp (:175): P-L-H / L-P-H / L-H-P; Ex2 Blinded (:227): Blind
- Ex3 Prosp (:323): A-Open / A-Rescue / B-Open / B-Rescue; Ex3 Blinded (:358): Drug-Open A / Drug-Rescue
- Ex4 Prosp/Explicit Repeats (:435/:464): Drug A / Drug B; Ex4 Blinded (:496): Blind
- Ex5 Retro (:578), Ex6 Retro (:656): Drug A / Drug B
- Ex7 Prosp (:740): CR ("Chemotherapy and Radiation Arm") / CRS ("Chemotherapy, Radiation and Surgery Arm")
- (可选同批) Prosp/Retro/Blinded 视图的 "Randomization" 注释 (Ex3 另 "Response Evaluation") 在 PDF 有字, 可作注释节点补上.

## attempt 2 续 复审 (修正 ④ delta; 2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: CONDITIONAL** (④ 全部正确; 剩修正 ⑤ = 4 个 Retrospective 视图补 Mermaid)

命令: `grep -n -E '^\s+arm[A-Za-z0-9_]*[>\[(]' knowledge_base/domains/TA/examples.md` → 28 行, 分布在 13 个 Mermaid; 逐个对渲染 (p388/390/391/392/393/395/396/397/398 90dpi, h-400 150dpi):
| 行 | 图 | 箭头标签 | PDF | 结果 |
|---|---|---|---|---|
| :72-74 / :103-105 | Ex1 Prosp / Retro | Placebo / Drug A / Drug B | p388 | 一致 |
| :126 | Ex1 Blinded | Blind | p388 | 一致 |
| :220-222 | Ex2 Prosp | P-L-H / L-P-H / L-H-P | p390 | 一致 |
| :261 | Ex2 Blinded | Blind | p391 | 一致 |
| :355-358 | Ex3 Prosp | A-Open / A-Rescue / B-Open / B-Rescue | p392 | 一致 |
| :388-389 | Ex3 Blinded | Drug-Open A / Drug-Rescue | p393 | 一致 |
| :467-468 / :507-508 | Ex4 Prosp / Explicit Repeats | Drug A / Drug B | p395 | 一致 |
| :533 | Ex4 Blinded | Blind | p396 | 一致 |
| :616-617 / :696-697 | Ex5 / Ex6 Retro | Drug A / Drug B | p397 / p398 | 一致 |
| :792-793 | Ex7 Prosp | CR + "Chemotherapy and Radiation Arm" / CRS + "Chemotherapy, Radiation and Surgery Arm" | p400 | 一致 |
箭头方向 (标签 → 臂末节点) = PDF 左指箭头; 指向节点正确. "option N" 保留可接受 (见 attempt 2 复审).
fp 隔离 (baseline $S/fp_before_iso.jsonl): regressions=1 仅 ig34_p0396_a009 (预期); check_links live docs 42.

### 裁定: Ex2 / Ex3 / Ex4 / Ex7 Retrospective (examples.md:227 / :363 / :473 / :800) 文字代替
PDF p390 / p393 / p395 / p401 这 4 处都是图 (有图题、epoch 列、每臂一行、arm 箭头; Ex7 另有图注). 裁定 **补 Mermaid**, 不接受只用文字代替. 理由:
- KB 保留了 `**Retrospective View**` 标签, 同文件 Ex1/Ex5/Ex6 的 Retrospective 已画图, 口径应一致;
- 文字代替没有给出图里的信息: 每臂一个 Screen 块 (与 Prospective 共用一块不同, 即 D-12 的分歧点)、每个 study cell 内的元素序列; Ex7 Retro 的 epoch 列头与 Prospective 一致, 但 CR/CRS 两行元素现在没有落点;
- 成本低, 结构可直接按 Prospective 改.
修正 ⑤ (writer attempt 3, 只改 examples.md):
1. 4 处各加 D6 `> KB note (not in SDTMIG): the following Mermaid diagram is a KB rendering of the PDF figure "<图题>".`, 图题逐字: "Example Trial 2, Crossover Trial Retrospective View" / "Example Trial 3, Multiple Branches Retrospective View" / "Example Trial 4, Cyclical Chemotherapy Retrospective View" / "Example Trial 7, RTOG 93-09 Retrospective View".
2. 结构按 Prospective 改: 每臂单独一个 Screen 节点 (Ex2 3 个, Ex3 4 个, Ex4 2 个, Ex7 2 个); 其余节点、epoch 名、绿色跳转边 (Ex4 "Repeat until disease progression"; Ex7 "If disease progression" ×2 / "If not eligible for surgery") 与 Prospective 相同; arm 箭头: Ex2 P-L-H / L-P-H / L-H-P, Ex3 A-Open / A-Rescue / B-Open / B-Rescue, Ex4 Drug A / Drug B, Ex7 CR / CRS 带同样的臂说明.
3. Ex7 Retro 图后加图注 `> \*Disease evaluation earlier \*\*Disease evaluation later` (p401).
4. 现有文字代替 note (:229 "Arm labels…", Ex3 / Ex4 / Ex7 的 "Same epoch structure…") 改完后删掉, 与新图重复.

## attempt 2 续 2 复审 (修正 ⑤ delta; 2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

| 行 | 图 | 节点 / 边 / arm 箭头 | PDF 渲染 | 结果 |
|---|---|---|---|---|
| :229 | Ex2 Retro | 3 个 Screen; 3 行 Placebo-Rest-5 mg-Rest-10 mg-Follow / 5 mg-Rest-Placebo-Rest-10 mg-Follow / 5 mg-Rest-10 mg-Rest-Placebo-Follow; 7 个 epoch 名; P-L-H / L-P-H / L-H-P | p390 | 一致 |
| :410 | Ex3 Retro | 4 个 Screen; Drug A→Open A, Drug A→Rescue, Drug B→Open A, Drug B→Rescue; Screening / Double Blind Treatment / Open Treatment Epoch; A-Open / A-Rescue / B-Open / B-Rescue | p393 | 一致 |
| :550 | Ex4 Retro | 2 个 Screen; "Drug A \| Rest" / "Drug B \| Rest" + "Repeat until disease progression"; Follow; Drug A / Drug B | p395 | 一致 |
| :897 | Ex7 Retro | 2 个 Screen; Induction / Continuation 节点同 Prosp; 3 条跳转边; Follow Epoch; CR / CRS 带臂说明; 图注 | p401 (h-401) | 一致 |
- 4 个图都有 D6 note, 图题与 PDF 逐字一致. 文件中 Mermaid 共 24 个, 每个前都有 D6.
- D-14..D-17 (删掉的文字代替 note: "Arm labels…" 与 3 条 "Same epoch structure…"): 都是 KB 自写摘要, 不在 PDF 里, 信息现在由新图承载, 没有丢失 PDF 内容. 残留的 5 条非图 D6 (:22 :159 :349 :501 :505) 已在 attempt 1 核过, 不矛盾.
- fp 隔离 (baseline $S/fp_before_iso.jsonl): regressions=1, 仅 ig34_p0396_a009 (预期, ATOM_ERR); new_hits=82 (> attempt 1 的 42, 因为隔离 baseline 是早先的全库快照, 之后并行批又有新命中). check_links: live docs 42.

### 终态签字
B-TA 终态 = knowledge_base/domains/TA/examples.md md5 `a1a95b892cd9c2fbe77eb920f893e964`, assumptions.md md5 `ea6bd5233aff46ae8b3d99ce9fc8cbd4`. 下列内容 reviewer 已全部核过并签字:
- attempt 1 全审: 叙述双向扫描、表格逐格、D-1..D-13、T-1..T-5、D6;
- 修正 ①-⑤ 与 D-14..D-17.
待处理: X-1 转 B-TE; T-3 / T-5 交用户 T4 裁定. 此后 KB 若再改, 须回 reviewer 复审.

## attempt 3 复审 (auditor M-1 后; 2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

reviewer 自认缺陷: attempt 2 续复审把各视图的 "Randomization" 注释标成"可选", 与修正④ 的口径 ("PDF 图上有字就补") 不一致. auditor M-1 判得对.

命令: `grep -n -E 'rand|resp|PDF figure|^\`\`\`mermaid' knowledge_base/domains/TA/examples.md`; 逐块 `sed -n` 读 24 个 Mermaid, 对渲染 p387-401 (90dpi) 与 h-400/h-401 (150dpi).

### 注释逐张核对 (有无 / 位置 / 文字)
| 图 | 行 | KB | PDF 位置 | 结果 |
|---|---|---|---|---|
| Ex1 Prosp / Retro / Blinded | :75 / :108 / :131 | "Randomization" → RE (Run-In 右界) | p388: 箭头指 Run-In/Treatment 分界 | 一致 |
| Ex2 Prosp / Retro / Blinded | :229 / :282 / :317 | → SE | p390/391: Screening 右界 | 一致 |
| Ex3 Prosp / Retro / Blinded | :416-417 / :456-457 / :485-486 | Randomization → SE; Response Evaluation → DB | p392/393: Screening 右界; Double Blind 右界 | 一致 |
| Ex4 Prosp / Retro / Explicit / Blinded | :568 / :596 / :632 / :659 | → SE | p395/396 | 一致 |
| Ex5 Retro / Ex6 Retro | :745 / :827 | → SE | p397 / p398 | 一致 |
| Ex7 Prosp / Retro | :925 / :966 | → SE | p400 / p401 | 一致 |
| 7 张 Schema (Ex1-6 + Ex7 5 options) | 边标签 | "Randomization" (Ex3 另有 "Response Evaluation") | p387/389/392/394/397/398/400 | 一致 |

### 全量扫描: PDF 图上有文字, KB 图上没有 (24 张, 不限注释类)
逐张列出 PDF 图内全部文字 (图题、epoch 列头、元素块、arm 箭头及臂说明、Randomization / Response Evaluation、Repeat until disease progression、If disease progression、If not eligible for surgery、Total length … cycle、Evaluation for Disease Progression (and Surgical Eligibility)、Options ①-⑤、图注 *Disease evaluation earlier **Disease evaluation later), 与 KB 对照: **0 缺失**.
- Ex7 5 options 的 "Options" 列头 + 编号, 由 "Follow (option N)" 承载, 接受.
- 图题由 D6 note 承载: 24 个 Mermaid, 24 条 D6, 图题逐字一致.
- 图注 3 处 (p400×2 / p401) 都在.
反向 (KB 图上有, PDF 图上没有): 0. 结构用的边、节点 ID、style 行不算文字.

fp 隔离 (baseline $S/fp_before_iso.jsonl): regressions=1 仅 ig34_p0396_a009 (预期; new_hits=100, 因为并行批也在增长, 与 TA 无关). check_links: live docs 42. spec.md 未改.

### 终态签字 (取代 attempt 2 续 2 的签字)
B-TA 终态:
- knowledge_base/domains/TA/examples.md md5 `a96c63b2822fe30b7621a293f40e2a15`
- knowledge_base/domains/TA/assumptions.md md5 `ea6bd5233aff46ae8b3d99ce9fc8cbd4`
reviewer 已全部核过并签字:
- attempt 1 全审;
- 修正 ①-⑤;
- D-1..D-17;
- attempt 3 的注释补齐, 以及 24 张图全量清零.
待处理: X-1 转 B-TE; T-3 / T-5 交用户 T4 裁定. 此后 KB 若再改, 须回 reviewer 复审.
