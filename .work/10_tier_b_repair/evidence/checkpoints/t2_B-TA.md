# T2 B-TA writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `466e0c37c42d6df07aac77bea737a0c51bee19ef` (TA 目录改前与 HEAD 一致; 工作区另有并行批 AE/GF/ch04 等未提交改动, 已含在 before_root 镜像中, 对比只换 TA 两文件故不影响)
- md5 TA/assumptions.md: before `7f094b9baef016000afed0c3dc5c8635` → after `ea6bd5233aff46ae8b3d99ce9fc8cbd4` (204 → 178 行)
- md5 TA/examples.md: before `64499c2b898bdb345ab15decd71903c3` → after `904cfc00a3a689d947b6c374020cee02` (752 → 829 行)
- TA/spec.md 未改 (不在 kb_files).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-TA_writer/`
  (before_root/ = 改前全 KB 镜像; after_root/ = before_root + 仅 TA 两文件换成改后 (隔离并行批); tools/apply_ex.py = examples.md 全部替换, 每处 assert 旧文本唯一;
  tools/prose_scan.py = p382-402 双向句扫; del_ex2.txt / del_issues.txt = assumptions.md 两段 D2 去重前原文备份; img/ = p384-402 80dpi 渲染 + z401 (Ex7 TDM 200dpi))
- 数据来源: 叙述 = `pdf_pages/ig34_p0382-0402.txt` 逐字 (合并换行, 去折行连字符, 保留 PDF 弯引号); 图 / TDM = 渲染图.
- 扫描范围: p382-402 (§7.1 p382-384 无其他批覆盖, TA/assumptions.md 承载, 一并扫); TA/assumptions.md 的 §7.2.2.1 TE Issues (p405-407) 属 B-TE 页段, 只核对不改 (见范围外 X-1).

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | TA/assumptions.md:76 | ig34_p0384_a016 | INSERTED | §7.2 标题下补引言首段 ("This subsection contains the Trial Design datasets …") | 384 |
| 2 | TA/assumptions.md:78 | R3 (§7.2 引言第 2 段) | MOVED | "The TA and TE datasets are interrelated …" 从 `## TA-Specific Assumptions` 下 (原 :178) 移到 §7.2 引言 (PDF 位置); subject's → subject’s (PDF 弯撇) | 384 |
| 3 | TA/assumptions.md:90-92 | R3 spec 首句 (dispatch notes) | INSERTED | 新增 `### §7.2.1 Trial Arms (TA) – Specification` + "ta.xpt, Trial Arms — Trial Design. One record per planned Element per Arm, Tabulation." (仿 CM; 标题层级跟本文件 §7.2.1 同类节) | 384 |
| 4 | TA/assumptions.md:96 | D2 (Ex2 叙述副本) | REPLACED | `§7.2.1 … – Example 2` 节下 6 段 Ex2 叙述 (原 :88-98) → 一行交叉引用 `> See [examples.md#example-2]…`; 原文逐字已补入 examples.md Ex2 (#14-19); 标题保留 | 389-391 |
| 5 | TA/assumptions.md:100 | D2 (§7.2.1.1 副本) | REPLACED | `§7.2.1.1 … Distinguishing Between Branches and Transitions` 下 12 句 (原 :102-124) → 一行交叉引用 examples.md#distinguishing-between-branches-and-transitions; examples.md 那份已补全 (#44-46); 标题保留 | 402 |
| 6 | TA/assumptions.md:36 | R3 (Concept 表 Study cell 格) | REPLACED | "1 of 3 study treatments" → "one of 3"; "3 study cell associated" → "3 study cells" (PDF_TYPO T-1) | 382 |
| 7 | TA/assumptions.md:170 | R3 (assumption 9) | REPLACED | "degree of similarity of epochs across arms" → "degree of similarity across arms" (删 KB 多出的 "of epochs") | 386 |
| 8 | TA/examples.md:5 | R3 (p386_a010) | REPLACED | "assigned to an arm" → "assigned to the arm" | 386 |
| 9 | TA/examples.md:22 | KB_AUTHORED | ANNOTATED | Ex1 KB 摘要句加 `> KB note (not in SDTMIG):` (不矛盾) | 387 |
| 10 | TA/examples.md:49 | ig34_p0387_a012 | INSERTED | Prospective View 前补 "The next diagram for this trial shows the 3 epochs …" 整段 (3 句) | 387 |
| 11 | TA/examples.md:74 | ig34_p0388_a002 | INSERTED | Retrospective View 前补 "The next diagram can be thought of as the retrospective view …" 整段 (4 句) | 388 |
| 12 | TA/examples.md:102 | ig34_p0388_a004 | INSERTED | Blinded View 前补 "The next diagram shows the trial from the viewpoint of blinded participants …" 整段 (3 句) | 388 |
| 13 | TA/examples.md:124 | ig34_p0389_a002 | INSERTED | TDM 前补 "As illustrated in the following table, the columns of a trial design matrix …" 整段 (4 句) | 389 |
| 13b | TA/examples.md:134 | ig34_p0389_a008 | INSERTED | ta.xpt 前补 "For Example Trial 1, the conversion of the trial design matrix …" 整段 (7 句) | 389 |
| 14 | TA/examples.md:152 | KB_AUTHORED (Ex2 摘要) | D2 删 + ANNOTATED | 原句 "…with 7 epochs: Screening, 3 Treatment Epochs with 3 Rest (washout) Epochs…" 与 PDF 矛盾 (PDF 只有 First/Second Rest 2 个) → 删; 次句 "Each arm represents a different order of treatments." 不矛盾 → D6 保留 | 389-391 |
| 15 | TA/examples.md:154 | R3 (Ex2 叙述 1, 原在 assumptions.md:88) | INSERTED | Study Schema 前补 Ex2 首段 ("The following diagram for a crossover trial …") | 389 |
| 16 | TA/examples.md:169 | R3 (Ex2 叙述 2) | INSERTED | Prospective View 前补 "The next diagram for this crossover trial shows the prospective view …" | 390 |
| 17 | TA/examples.md:215 | R3 (Ex2 叙述 3) | INSERTED | "The next diagram shows the retrospective view of the trial." | 390 |
| 18 | TA/examples.md:221 | R3 (Ex2 叙述 4) | INSERTED | Blinded View 前补 "The last diagram for this trial shows the trial from the viewpoint of blinded participants. …" | 390 |
| 19 | TA/examples.md:253, :263 | R3 (Ex2 叙述 5/6) | INSERTED | TDM 前 "The following table illustrates …"; ta.xpt 前 "It is straightforward to produce the TA dataset …" | 391 |
| 20 | TA/examples.md:219 | KB_AUTHORED | D2 删 + ANNOTATED | Ex2 Retrospective View 文字替代: 首句 "Same structure as the Prospective View (one-to-one …)" 删 (PDF Prospective 为共用 Screen 块、Retrospective 每 arm 一块, 结构不同 → 矛盾, D-12); 次句 "Arm labels: P-L-H, L-P-H, L-H-P." 与图一致 → D6 | 390 |
| 21 | TA/examples.md:293 | KB_AUTHORED (Ex3 摘要) | ANNOTATED + D2 删 | 前 2 句 KB 摘要 → D6; 第 3 句 "TABRANCH is populated for 2 records … reflecting the 2 branch points" (p394 改写残句) 与第 4 句 (p394 原文, 已在 #25 补全段) → 删 | 392/394 |
| 22 | TA/examples.md:295 | R3 (Ex3 叙述 1) | INSERTED | Study Schema 前补 "Each of the paths for the trial …" 整段 | 392 |
| 23 | TA/examples.md:317 | R3 (Ex3 叙述 2) | REPLACED | "…how the initial group of subjects is divided at the point of randomization." (截断改写) → PDF 整段 (split into 2 treatment groups … 4 arms of this trial. The names … Example 7 in Section 5.2 …); "this trial The names" 补句点 (PDF_TYPO T-2) | 392 |
| 24 | TA/examples.md:346, :352 | R3 (Ex3 叙述 3/4) | INSERTED | Retrospective 前 "The next diagram shows the retrospective view. As with the first 2 …"; Blinded 前 "The last diagram for this trial … they see 2 possible element sequences." | 393 |
| 24b | TA/examples.md:375 | R3 (Ex3 叙述 5) | MOVED | "The trial design matrix for this trial can be constructed easily …" 从 Blinded View 前 (原 :313) 移到 Blinded 图之后 TDM 前 (PDF 位置); 移位非删除 | 393 |
| 25 | TA/examples.md:386 | R3 (Ex3 叙述 6) | INSERTED | ta.xpt 前 "Creating the TA dataset for this example trial is similarly straightforward. …" 整段 (3 句) | 394 |
| 26 | TA/examples.md:350 | KB_AUTHORED | ANNOTATED | Ex3 Retrospective 文字替代加 KB note | 393 |
| 27 | TA/examples.md:409, :413 | KB_AUTHORED | ANNOTATED | Ex4 摘要句 + "Maximum of 4 cycles assumed in this example." 加 KB note (不矛盾; PDF p395 同说 4) | 394-395 |
| 28 | TA/examples.md:452 | R3 (Ex4) | INSERTED | "The next diagram shows the retrospective view of this trial." | 395 |
| 29 | TA/examples.md:456 | KB_AUTHORED | ANNOTATED | Ex4 Retrospective 文字替代加 KB note | 395 |
| 30 | TA/examples.md:514 | ig34_p0396_a004 (+ a003) | REPLACED | "…with explicit repeats of elements shown." (截断) → PDF 整段 "…of the treatment and rest elements. As previously noted, the trial design matrix does not include information regarding when randomization occurs; similarly, …" | 396 |
| 31 | TA/examples.md:523 | R3 (Ex4 TA 段) | MOVED + REPLACED | "The TA dataset for this example trial requires the use of the TATRANS variable …" 从 TDM 段之前 (原 :460) 移到 TDM 表之后 ta.xpt 前 (PDF 顺序); "arrow represents this rule" → "represented" (PDF p396) | 396 |
| 32 | TA/examples.md:552 | ig34_p0397_a002 (+ a003/a004) | REPLACED | VALUE_DIFF: KB "Similar to Example 4 … Maximum of 3 cycles assumed. Different rest elements (RESTA, RESTB) are used for the 2 arms since cycle lengths differ." (末句与 PDF "total length of the cycle is the same" 相反) → PDF 首段 3 句逐字 | 397 |
| 33 | TA/examples.md:572 | ig34_p0397_a006, a007 | INSERTED | Retrospective 前 "The assumption of a one-to-one relationship … essentially the same as Trial 4. The next diagram shows the retrospective view of this trial." | 397 |
| 34 | TA/examples.md:596 | ig34_p0397_a010 | INSERTED | TDM 前 "The trial design matrix for this trial is almost the same as for Example Trial 4; …assumed to be 3." | 397 |
| 35 | TA/examples.md:605 | ig34_p0397_a015 | INSERTED | ta.xpt 前 "The TA dataset for this trial shown below corresponds to the trial design matrix." | 397 |
| 36 | TA/examples.md:630 | R3 (p398_a010/a011) | REPLACED | KB 改写 "An oncology trial with cycles of different lengths: … Maximum 4 cycles of Drug A, 3 cycles of Drug B." → PDF 首段 2 句 (D2 删改写残句, 见删除清单 D-5) | 398 |
| 37 | TA/examples.md:650 | ig34_p0398_a013, ig34_p0398_a014 | INSERTED | Retrospective 前补 3 句 ("The design of this trial is very similar …" / "The main difference is … 2 different rest elements …" / 下图引导句) | 398 |
| 38 | TA/examples.md:674 | R3 (p398_a017) | INSERTED | TDM 前 "The trial design matrix for this trial assumes … maximum of three cycles of drug B." | 398 |
| 39 | TA/examples.md:683 | ig34_p0398_a023, ig34_p0398_a024 (+ a022) | REPLACED + MOVED | KB 改写 "Because the treatment epoch for arm A has more elements than arm B, … Gaps in TAETORD values are acceptable." (原 :568, 在 Study Schema 前) → PDF 整段 (含 "(It would also be possible to assign a TAETORD value of 10 …)" 与 "The primary purpose of TAETORD …"), 放到 TDM 之后 ta.xpt 前 (PDF 位置) | 398 |
| 40 | TA/examples.md:710 | R3 (p399_a023/a024) | REPLACED | Ex7 首段: "no natural grouping of time periods across arms that corresponds to epochs as defined in Section 7.1.2 …" / "the major clinical phases of the trial" (KB 改写, 自造交叉引用) → PDF 原文 ("nothing like a one-to-one match between the elements …" / "periods of time that will be compared in analyses of the trial") | 399 |
| 41 | TA/examples.md:712 | ig34_p0399_a030 (+ a026-a029, a032) | REPLACED | Ex7 第 2 段: KB "radiotherapy only (R)" (错, PDF = chemotherapy and radiotherapy plus surgery (CRS)), "radiation treatment", "further evaluation instead", 缺 "but does include a text-based representation …"/"All subjects receive induction …"/"After induction chemotherapy and radiation …" → PDF 整段 10 句逐字 (O10 TA Ex7) | 399 |
| 42 | TA/examples.md:714 | R3 (p400_a002) | REPLACED | 原 :642 "Both the induction …" + :644 "This diagram also shows more detail …" (顺序倒、缺首句 "However, the objectives of the trial …") → PDF 整段 4 句 | 400 |
| 43 | TA/examples.md:718 | KB_AUTHORED (Mermaid) | ANNOTATED | "Study Schema (2-arm model)" Mermaid 无 PDF 对应图 (PDF 只有 5 options 图); 与 ta.xpt 一致不矛盾 → KB note "KB-drawn 2-arm schema based on the ta.xpt below; it is not a figure in the SDTMIG." **reviewer 注意**: PDF 中 "However, … as illustrated in the following diagram." 与 "The next diagram shows the prospective view …" 是相邻两段, 所指 = Prospective View 图; KB 自绘图 (沿用原位置) 现夹在两段之间, "the following diagram" 读起来会指向 KB 图. 是否把该 Mermaid 移到别处 / 删, 与 X-2 一并由主控定 | 400 |
| 43b | TA/examples.md:736 | R3 (p400_a008) | REPLACED | 原 :664 缺首句且 "subjects are evaluated for the possibility of surgery" 改写 → PDF 整段 ("The next diagram shows the prospective view of this trial. … when subjects who will skip forward are identified (i.e., …)") | 400 |
| 44 | TA/examples.md:770 | R3 (图注) | REPLACED | "> *Disease evaluation earlier, **Disease evaluation later" → 去 KB 多加的逗号, 星号转义 (PDF 图注原样) | 400 |
| 45 | TA/examples.md:772 | R3 (p400_a011, p401_a002) | REPLACED | 原 :699 截断 → PDF 整段 (补 "The fact that the elements in the study cell for the CR arm … is an artifact of the diagram conventions." 与 "…, and elements that line up on the same vertical line … within the study.") | 400-401 |
| 46 | TA/examples.md:776 | KB_AUTHORED | D2 删 + ANNOTATED | Ex7 Retrospective: 次句 "…reflecting different treatment durations between the 2 arms" 与 PDF ("an artifact of the diagram conventions") 矛盾 → 删; 首句 "Same epoch structure as the Prospective View." → D6 | 400-401 |
| 47 | TA/examples.md:782-785 | unparseable census :709 (Ex7 TDM) | TABLE_REBUILT | 原表头 8 格 / CR 行 7 格 / CRS 行 10 格 (损坏) → 10 列: `| | Screen | Induction | | Continuation ×5 | Follow-up |`; CR 两个 Chemo 左对齐 (同 Ex6 B 行惯例); CRS 9 格按 z401 渲染; PDF CRS 行末一个空格 (版面伪格, 无内容) 未复制 | 401 |
| 48 | TA/examples.md:813 | R3 (p402_a009) | REPLACED | "The rule underlying a branch appears" → "…a branch in the trial design appears" (R2 丢短语) | 402 |
| 49 | TA/examples.md:815, :817 | R3 (p402_a015-a018) | INSERTED | §7.2.1.1 补 2 段 ("In modeling a trial, …" / "Some trials refer to groups of subjects … 'cohorts,' …"); 原仅在 assumptions.md 副本 | 402 |
| 50 | TA/examples.md:821 | R3 (p402_a022) | REPLACED | "first branch point of an adaptive trial design" → "first branch point in a trial" | 402 |
| 51 | TA/examples.md:825 | R3 (Defining Epochs) | REPLACED | "will be in the same epoch" → "will be included in the comparison" | 402 |
| 52 | TA/examples.md (19 处) | Mermaid D6 + PDF 图逻辑核对 | ANNOTATED / REPLACED | 每个 Mermaid 前加 `> KB note (not in SDTMIG): the following Mermaid diagram is a KB rendering of the PDF figure "<PDF 图题>".` (:34 :53 :78 :106 :158 :173 :225 :299 :321 :356 :417 :433 :462 :494 :556 :576 :634 :654 :740). 逻辑修正 (对渲染): Ex2/Ex3/Ex4/Ex7 **Prospective View** PDF 为单一共用 Screen 块 (Ex3 另为单一 Drug A / Drug B 块), KB 原为每 arm 一个 → 改为单节点分叉; Ex2 Prospective/Blinded 的 epoch 标签 "1st/2nd Washout"、"1st Rest"、"Screening"、"Follow-up" → PDF "First/Second Rest Epoch"、"Screening Epoch"、"First/Second/Third Treatment Epoch"、"Follow-up Epoch". 其余 Mermaid (Ex1 全部, Ex2/Ex3 Study Schema, Ex3 Blinded, Ex4 Schema/Explicit Repeats/Blinded, Ex5, Ex6) 与渲染分支/顺序一致, 未改 | 387-401 |

- atoms 覆盖率自查: atoms 17 → 清单 atom 行: a016(#1) p387_a012(#10) p388_a002(#11) p388_a004(#12) p389_a002(#13) p389_a008(#13b) p396_a004(#30) p397_a006/a007(#33) p397_a010(#34) p397_a015(#35) p398_a013/a014(#37) p398_a023/a024(#39) p399_a030(#41) p397_a002(#32) = 17/17, 0 跳过.
- t2_recheck 0; census DIFF 0 / pdf_only 0 / pdf_unparsed 0.

### 新增 atom 清单 (R3, 不在 atoms[] 的批内叙述缺失 / 错值)
#2 #3 #6 #7 #8 #15-19 #22-25 #28 #31 #36 #38 #40 #42 #43b #44 #45 #48-51 (Ex2 6 段从 assumptions.md 补到 examples.md; Ex3 6 段; Ex7 首 4 段整体按 PDF 重写; Issues 2 段; 若干单词级改写恢复).

### unparseable 表 (8 张, census 不可机检; 人工对渲染)
| census ref | 表 | 处理 | 依据 |
|---|---|---|---|
| assumptions.md:31 | §7.1.2 Concept 表 | **触碰** (#6 Study cell 格 2 处); 其余 8 格逐句对 p382-383 layout: 除 #6 外 0 差异 (脚本: 每格句切 → norm 子串于 p382-383; PDF 定义列每行片段 → norm 子串于 KB) | p382-383 |
| examples.md:112 (现 :128) | Ex1 TDM | 未改; 与渲染一致 (Run-in 小写 i, PLACEBO/DRUG A/DRUG B 大写) | p389 |
| :225 (现 :257) | Ex2 TDM | 未改; 3×8 与渲染一致 | p391 |
| :336 (现 :379) | Ex3 TDM | 未改; 4×4 一致 | p393 |
| :466 (现 :518) | Ex4 TDM | 未改; 2 行各 10 格一致 (Treatment 跨 8 列 → KB 空表头格) | p396 |
| :538 (现 :600) | Ex5 TDM | 未改; Rest A/Rest B 一致 | p397 |
| :608 (现 :678) | Ex6 TDM | 未改; B 行 PDF 为跨列宽格, KB 左对齐 6 格 + 2 空 (惯例) | p398 |
| :709 (现 :782) | Ex7 TDM | **TABLE_REBUILT** (#47) | p401 z401 200dpi |
- reviewer 须对渲染逐格复核 assumptions.md:31 (#6) 与 Ex7 TDM (#47). 80dpi 页图 + layout 文本已够读 Ex1-6 TDM 各格, reviewer 若需可 ≥110dpi 重渲.
- ta.xpt 表 Ex1-Ex7 未改 (census 可机检, OK). p389 TABRANCH 原子 (p0389_a012/a013) 把 "Randomized to Placebo" 记在 Row 3, 渲染图在 Row 2 = KB 正确 → ATOM_ERR (lane notes 一致), 未改.

### 删除清单 (D2; reviewer 逐条确认)
| D | file:line (改前) | 内容 | 原因 | 保留副本 / 去向 |
|---|---|---|---|---|
| D-1 | assumptions.md:88-98 | Ex2 叙述 6 段 | D2 同文件副本去重: 原文在 assumptions.md 错位; PDF 所属 = TA Examples Ex2 | examples.md:154/169/215/221/253/263 (逐字); 原处留交叉引用 :96 |
| D-2 | assumptions.md:102-124 | §7.2.1.1 Distinguishing Between Branches and Transitions 12 句 | D2 去重; examples.md "## Trial Arms Issues" 承载 §7.2.1.1 全部 4 小节 (fp target = examples.md) | examples.md:813-817 (补全后逐字); 原处留交叉引用 :100 |
| D-3 | examples.md:134 首句 | "A crossover trial comparing 3 treatments … 3 Rest (washout) Epochs …" | 与 PDF 矛盾 (Rest epoch 为 2 个; 7 epochs 数不上) | 无 (PDF 叙述 #15-16 已覆盖) |
| D-4 | examples.md:259 第 3-4 句 | "TABRANCH is populated for 2 records in each arm reflecting the 2 branch points. Note also that the values of ARMCD, …" | 改写残句 + 原文重复 (不承载其他原子: p394 原子改后命中 #25) | examples.md:386 |
| D-5 | examples.md:566 | Ex6 KB 改写段 (3-week/4-week cycles … Maximum 4 cycles of Drug A, 3 cycles of Drug B) | R2 插入后的改写残句, 行内无其他 PRESENT 原子 (p398_a010/a011 改前未命中) | examples.md:630 + :674 |
| D-6 | examples.md:568 | "Because the treatment epoch … Gaps in TAETORD values are acceptable." | 改写残句, 位置错 | examples.md:683 (PDF 原文) |
| D-7 | examples.md:498 | Ex5 KB 摘要 3 句 | VALUE_DIFF 原子 a002 的旧值; 末句语义反 (O10) | examples.md:552/596 |
| D-8 | examples.md:638/640/642/644/664/699 | Ex7 旧改写段 | 被 PDF 原文整段替换 (VALUE/REWRITE) | examples.md:710/712/714/736/772 |
| D-9 | examples.md:703 次句 | "…reflecting different treatment durations between the 2 arms." | 与 PDF 矛盾 | 无 |
| D-10 | assumptions.md:178 | "The TA and TE datasets are interrelated …" | MOVED (同文件移位, 非删除) | assumptions.md:78 |
| D-12 | examples.md:193 首句 | "Same structure as the Prospective View (one-to-one relationship …)" | 与 PDF 图矛盾 (见 #20) | 无 |
| D-11 | examples.md:313 / :460 | Ex3 TDM 句 / Ex4 TA 段 | MOVED (同文件移位) | :375 / :523 |

### PDF_TYPO (登记; 依据 = PDF 自身)
| T | 位置 | PDF | KB 处理 | 依据 |
|---|---|---|---|---|
| T-1 | assumptions.md:36 (p382 Study cell) | "There would be 3 study cell associated" | 写 "3 study cells" | 同句前后 "study cells" 复数; 语法唯一 |
| T-2 | examples.md:317 (p392) | "resulting in the 4 arms of this trial The names" 缺句点 | 补 "." | 两个完整句, 句界明确 |
| T-3 | examples.md:295 (p392) | "(Open DRUG X and Rescue)" vs 同页图块 "Open A" / TDM "Open Drug A" | **照录 PDF** | 无法由 PDF 自身唯一确定 → T4 用户裁定 |
| T-4 | examples.md ta.xpt Ex2 Row 15 (p391) | TABRANCH "Randomized to 5 mg - 10 mg – Placebo" (后一处为 en dash) | KB 保持 "-" (未改; 同表其他行用 "-") | fp/census 归一化 –/- 等价, 仅登记 |
| T-5 | examples.md:317 (p392) | "Example 7 in Section 5.2, Demographics" vs §7.2.1.1 "See DM Example 3" | 照录 | PDF 内两处 DM 例号不同, 不能由本节确定 → T4 |

### fp_match (隔离: before_root vs after_root, 仅 TA 两文件不同)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-TA_writer
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/before_root/knowledge_base --out $S/fp_before.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/after_root/knowledge_base --out $S/fp_after.jsonl --baseline $S/fp_before.jsonl --regress-out $S/fp_regress.jsonl
python3 -I $S/tools/prose_scan2.py > $S/prose_scan_after.txt  # 改前: python3 -I $S/tools/prose_scan2.py $S/before_root/knowledge_base/domains/TA > $S/prose_scan_before.txt
```
- hit_target 3763 → 3804; **新命中 42** (17 atoms 全部 + p386_a010, p396_a003, p397_a003/a004, p398_a010/a011/a017/a022, p399_a023/a024/a026-a029/a032, p400_a002/a008/a011, p401_a002, p402_a009/a015-a018/a022).
- **回归 1 (预期, ATOM_ERR)**: `ig34_p0396_a009` — 原子文本 "arrow **represents** this rule", PDF p396 layout 与渲染均为 "represented" (`grep -c "represented this rule" work/pdf_pages/ig34_p0396.txt` → 1). KB 按 PDF 改 (#31) 导致原子不再命中. 非 PDF_TYPO, 是原子抽取错.
- T-1 (p382) / T-2 (p392) 改正无回归仅因 p382-393 叙述原子不在 fp inventory scope; 若以 `--scope all` 跑, 预期这 2 处原子不命中 (KB 有意偏离 PDF 笔误).
- p382-402 改后仍未命中 19: FIGURE 原子 16 (图以 Mermaid 呈现, 同 ch02 p15_a006 口径) + p389_a012/a013 (ATOM_ERR, 见上) + p396_a009 (ATOM_ERR).

### 双向扫描 (prose_scan2.py, p382-402 vs TA 两文件全文; 去编号 / "- " / bullet, 合并 em-dash 折行; 输出全文存 scratch prose_scan_after.txt (97 行) / prose_scan_before.txt (191 行), 未截断)
- census (table_census.py, B-TA manifest): before / after 同为 `KB tables 15: OK 7 (ta.xpt Ex1-7) / UNPARSEABLE 8 (Concept 表 + 7 TDM), cells 1221, diffs 0` (Ex7 TDM 重建后仍 UNPARSEABLE → 仅人工对渲染). 命令: `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json [--kb-root $S/before_root/knowledge_base] --out $S/census_{before,after}.json`
- PDF→KB 改后剩余 35 条全部为非缺口 (assumptions 1-12 / 10a-b 逐条命中; 仅 "TA – Assumptions TAETORD is an integer." 为标题拼行): 标题与正文被脚本拼行 (7 / 7.1 / 7.2 / 7.2.1 / Example N / 7.2.1.1 / 7.2.2), 列表 bullet 拼行, spec 表格残片 (属 spec.md), 图题 "Example Trial N, …" (现于 Mermaid D6 note 内), 图注 ×3 (KB 1 处, 另 2 图未复现), em-dash 折行空格伪差 (p387 "randomization— which", p395 "then— for"), T-1/T-2 (KB 有意改).
- KB→PDF 改后未命中: D6 KB note 29 处 (:22 :34 :53 :78 :106 :152 :158 :173 :219 (改后仅 Arm labels 句) :225 :293 :299 :321 :350 :356 :409 :413 :417 :433 :456 :462 :494 :556 :576 :634 :654 :718 :740 :776), 交叉引用 2 (assumptions :96 :100), 导航标签 "**Study Schema (2-arm model)**", 列表行 (脚本不剥 "- ", 内容已逐条核同 PDF), em-dash 伪差 (:49 :458), T-2 (:317), assumptions.md:102-150 TE Issues (p405-407 内容, 页段外, 见 X-1). 无其他 KB 自写正文.
- 未改 (仅格式): 部分既有行直引号 vs PDF 弯引号 (B-EG 口径).

### 范围外发现
- X-1 (主控定): TA/assumptions.md:102-150 `§7.2.2.1 Trial Elements Issues – …` 两节是 TE p405-407 内容, 与 TE/examples.md:65-85 跨文件重复, 两份各缺一部分 (TA 份缺 3-step 表, 末句 "The transition … 3-step process:" 后空; TE 份缺 "As illustrated in the table, executing a transition …" 起 5 句 + fragment 表说明). 按 D2 应由 B-TE 把 TE 份补全后, TA 份改一行交叉引用; 本批未动.
- X-2: PDF Ex7 图 "Study Schema with 5 "options"" (p400_a001) 在 KB 无对应 (KB 的 2-arm Mermaid 是自绘, 已 D6). 是否补图由主控定.
- X-3: O4 TAEFORD — `grep -rn TAEFORD knowledge_base` 0 命中; 原子编造, KB 无需改.
- X-4: assumptions.md 结构: `## Trial Design Model Overview (§7.1)` 等 KB 自拟 H2 与 PDF 标题 ("7.1 Introduction to Trial Design Model Datasets") 不同, 按规则 6 未改.

### 链接 / diff
- `python3 tools/check_links.py | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (基线 42, 未升; 新增 2 个同目录锚点链接).
```
 knowledge_base/domains/TA/assumptions.md |  48 ++------
 knowledge_base/domains/TA/examples.md    | 205 +++++++++++++++++++++----------
 2 files changed, 152 insertions(+), 101 deletions(-)
```

## attempt 1 续 (主控裁定 2026-11-26: X-1 转 B-TE 不动; X-2 重画 5 options 图)

- X-1: TA/assumptions.md:102-150 未动 (转 B-TE).
- X-2: 删 KB 自绘 "**Study Schema (2-arm model)**" + Mermaid (D-13; 原文备份 scratch del_ex7_2arm.txt); 在 Ex7 第 2 段 ("…might suggest that the trial has 5 arms.") 后 = PDF 图位置, 新增 examples.md:714-731: 标签 `**Study Schema with 5 "options"**` + D6 "KB rendering of the PDF figure \"Example Trial 7, RTOG 93-09 Study Schema with 5 \"options\"\"" + Mermaid + PDF 图注 (\*Disease evaluation earlier \*\*Disease evaluation later). 逻辑按 p400 渲染 (z400 160dpi): Screen →(Randomization) 两路 Chemo+Rad → Chemo+Rad* / Chemo+Rad**; 上路 (Evaluation for Disease Progression) → Follow ②, 或 Chemo+Boost → Chemo → Follow ⑤; 下路 (Evaluation for Disease Progression and Surgical Eligibility) → 3-5 w Rest → Surgery → 4-6 w Rest → Chemo → Chemo → Follow ③, 或 Chemo → Chemo → Follow ④, 或 Follow ①. "However … as illustrated in the following diagram." 现紧接 "The next diagram shows the prospective view …" 与 Prospective 图, 同 PDF.
- md5 examples.md after → `c05869b4d1b031559e9a04d59ad6d0a8` (行数见 wc); 删除清单追加 D-13 (2-arm Mermaid, KB 自写非 PDF 图, 主控裁定删).
- fp 隔离重跑: 回归仍仅 ig34_p0396_a009 (ATOM_ERR, 预期), new_hits 42 不变; p0400_a001 (5 options FIGURE 原子) 仍不命中 (FIGURE 原子口径). check_links live docs 42.

## attempt 2 (2026-11-26; reviewer CONDITIONAL 修正清单 ①②③; 只改 examples.md Mermaid 标签)

- 规则 B: attempt 1 归档 `evidence/failures/t2_B-TA_attempt_1.patch` (git diff 466e0c3 -- knowledge_base/domains/TA/, 709 行) + `t2_B-TA_attempt_1.md`.
- md5 examples.md → `bf0d29f2177f2cd57062b6324dbea19d` (827 行不变); assumptions.md 未动.
- ① Ex7 Prospective (:753/:763-765): epoch "Follow-up Epoch" → "Follow Epoch"; 边 "If progression" ×2 → "If disease progression"; "Not eligible for surgery" → "If not eligible for surgery" (p400).
- ② Ex5 Retro (:585-586) "Rest A"/"Rest B" → "Rest"; Ex6 Retro (:663-664) 同 + "(3-week cycles)"/"(4-week cycles)" → "Total length Drug A cycle: 3 weeks"/"Total length Drug B cycle: 4 weeks" (p397/p398 图).
- ③ Study Schema 边: Ex1 ×3 "Randomized to Placebo/Drug A/Drug B", Ex2 ×3 "P-5-10/5-P-10/5-10-P", Ex3/Ex4/Ex5/Ex6 ×8 "Randomized to A/B" → "Randomization"; Ex3 ×4 "Response: Open A/Rescue" → "Response Evaluation" (p387/389/392/394/397/398 图).
- 全 20 图节点/边标签再对渲染 (超出清单): Ex7 Prospective 节点 "Chemo+Rad"/"Chemo+Rad*"/"Chemo+Rad**"/"Chemo+Boost"/"3-5w Rest"/"4-6w Rest" → PDF 写法 "Chemo + Rad"/"Chemo + Rad*"/"Chemo + Rad**"/"Chemo + Boost"/"3-5 w Rest"/"4-6 w Rest" (p400). 其余图节点/epoch 名已与 PDF 一致 (Ex1 Screen/Run-In/Placebo/Drug A/Drug B/Study Drug + Screening/Run-In/Treatment Epoch; Ex2 Placebo/5 mg/10 mg/Rest/Follow/Drug + First…Third Treatment / First/Second Rest / Follow-up Epoch; Ex3 Screen/Drug A/Drug B/Open A/Rescue/Drug + Screening / Double Blind Treatment / Open Treatment Epoch; Ex4 Drug A/B/Rest/Follow/A/B/Rx + "Repeat until disease progression"/"If disease progression"; Ex5/6 Schema 周期注; Ex7 5 options). 保留的非 PDF 文字: Ex7 5 options 图 "Follow (option N)" 的 "option N" = PDF 右侧 Options 编号的转写 (reviewer 已 ✓); PDF 图中 arm 箭头 (Placebo/Drug A/P-L-H/A-Open/CR…) 未画, 属省略非矛盾.
- 验证: fp 隔离重跑 regressions=1 (仅 ig34_p0396_a009, 预期 ATOM_ERR), new_hits 42; check_links live docs 42.

## attempt 2 续 (reviewer 修正④: Mermaid 补 PDF 右侧 arm 箭头)

- md5 examples.md → `01bd3632c776b4bd7d7ba06bf17be0ef` (827 → 855 行); 只改 examples.md Mermaid, 每图块末加 `armX>"<PDF 箭头文字>"] -.-> <该行末节点>` (flag 形节点 = PDF 左指箭头).
- 13 图 / 28 箭头 (逐字照渲染): Ex1 Prosp + Retro: Placebo / Drug A / Drug B; Ex1 Blinded: Blind; Ex2 Prosp: P-L-H / L-P-H / L-H-P; Ex2 Blinded: Blind; Ex3 Prosp: A-Open / A-Rescue / B-Open / B-Rescue; Ex3 Blinded: Drug-Open A / Drug-Rescue (z393b 150dpi); Ex4 Prosp + Explicit Repeats: Drug A / Drug B; Ex4 Blinded: Blind; Ex5 Retro, Ex6 Retro: Drug A / Drug B; Ex7 Prosp: CR + "Chemotherapy and Radiation Arm", CRS + "Chemotherapy, Radiation and Surgery Arm" (z400b).
- (Ex2/Ex3/Ex4/Ex7 的 Retrospective 在 KB 为文字替代无 Mermaid, 故无箭头可补; "option N" 保留.)
- 验证: fp 隔离重跑 regressions=1 (仅 ig34_p0396_a009, 预期); check_links live docs 42.

## attempt 2 续 2 (reviewer 修正⑤: Ex2/Ex3/Ex4/Ex7 Retrospective 补 Mermaid)

- md5 examples.md → `a1a95b892cd9c2fbe77eb920f893e964` (855 → 983 行; Mermaid 20 → 24); 只改 examples.md.
- 新增 4 图 (每图前 D6 "KB rendering of the PDF figure" + 逐字图题; 结构照 Prospective, 但每臂单独 Screen 块; 元素顺序按 PDF 单元格; arm 箭头 + 文字):
  - Ex2 :229 "Example Trial 2, Crossover Trial Retrospective View" (p390): 3 行 Screen→Placebo/5 mg/5 mg→Rest→5 mg/Placebo/10 mg→Rest→10 mg/10 mg/Placebo→Follow; 箭头 P-L-H / L-P-H / L-H-P.
  - Ex3 :410 "Example Trial 3, Multiple Branches Retrospective View" (p393): 4 行 Screen→Drug A/Drug A/Drug B/Drug B→Open A/Rescue/Open A/Rescue; 箭头 A-Open / A-Rescue / B-Open / B-Rescue.
  - Ex4 :550 "Example Trial 4, Cyclical Chemotherapy Retrospective View" (p395): 2 行 Screen→"Drug A | Rest / Drug B | Rest, Repeat until disease progression"→Follow; 箭头 Drug A / Drug B.
  - Ex7 :897 "Example Trial 7, RTOG 93-09 Retrospective View" (p401): 2 行各自 Screen; 节点 / "If disease progression" ×2 / "If not eligible for surgery" / Follow Epoch FU / 箭头 CR + "Chemotherapy and Radiation Arm"、CRS + "Chemotherapy, Radiation and Surgery Arm"; 图后加图注 "\*Disease evaluation earlier \*\*Disease evaluation later".
- 删除清单追加 (被 Mermaid 替换的 KB 文字代替 note; 原文备份 scratch del_a2c2.txt):
  | D | 原位置 (attempt 2 续 时行号) | 内容 | 原因 |
  |---|---|---|---|
  | D-14 | examples.md:229 | `> KB note …: Arm labels: P-L-H, L-P-H, L-H-P.` | 由 PDF 图 Mermaid 取代 (箭头标签含同信息) |
  | D-15 | :365 | `> KB note …: Same epoch structure as Prospective View. 4 arms: A-Open (…)…` | 同上 |
  | D-16 | :475 | `> KB note …: Same epoch structure as the Prospective View: 2 arms (Drug A, Drug B) …` | 同上 |
  | D-17 | :802 | `> KB note …: Same epoch structure as the Prospective View.` | 同上 |
- 验证: fp 隔离重跑 regressions=1 (仅 ig34_p0396_a009, 预期); check_links live docs 42.

## attempt 3 (auditor FAIL M-1: 视图内 "Randomization" / "Response Evaluation" 注释缺失)

- 规则 B: attempt 2 归档 `evidence/failures/t2_B-TA_attempt_2.patch` (git diff 466e0c3 -- knowledge_base/domains/TA/, 951 行) + `t2_B-TA_attempt_2.md`.
- md5 examples.md → `a96c63b2822fe30b7621a293f40e2a15` (983 → 1023 行); 只改 examples.md Mermaid, 正文未动.
- 做法: 有注释的视图在块末加注释节点 `rand["Randomization"] -.-> <epoch subgraph>` (虚线指向随机化所在 epoch 的右边界 = PDF 箭头所指 epoch 分界; Ex1 为 Run-In Epoch 末, 其余为 Screening/Screen Epoch 末), Ex3 另加 `resp["Response Evaluation"] -.-> DB` (Double Blind Treatment Epoch 末); 注释节点虚线框样式. Schema 类图 PDF 的注释已作边标签 ("Randomization" / "Response Evaluation" / "Evaluation for …", attempt 2 ③), 不重复加.
- 逐张清单 (24 张; 行号 = 改后 ```mermaid 行; 依据 = 渲染图 img/p-387…p-401):

| # | 行 | 图题 | PDF 页 | PDF 注释 | 处理 |
|---|---|---|---|---|---|
| 1 | :36 | Ex1 Parallel Design Study Schema | 387 | Randomization | 已有 (3 条边标签) |
| 2 | :55 | Ex1 Prospective View | 388 | Randomization (Run-in/Treatment 分界) | 已补 → RE |
| 3 | :85 | Ex1 Retrospective View | 388 | Randomization | 已补 → RE |
| 4 | :118 | Ex1 Blinded View | 388 | Randomization | 已补 → RE |
| 5 | :173 | Ex2 Crossover Trial Study Schema | 389 | Randomization | 已有 (边标签) |
| 6 | :188 | Ex2 Prospective View | 390 | Randomization | 已补 → SE |
| 7 | :239 | Ex2 Retrospective View | 390 | Randomization | 已补 → SE |
| 8 | :292 | Ex2 Blinded View | 391 | Randomization | 已补 → SE |
| 9 | :369 | Ex3 Multiple Branches Study Schema | 392 | Randomization + Response Evaluation | 已有 (边标签) |
| 10 | :391 | Ex3 Prospective View | 392 | Randomization + Response Evaluation | 已补 → SE / DB |
| 11 | :428 | Ex3 Retrospective View | 393 | Randomization + Response Evaluation | 已补 → SE / DB |
| 12 | :468 | Ex3 Blinded View | 393 | Randomization + Response Evaluation | 已补 → SE / DB |
| 13 | :535 | Ex4 Cyclical Chemotherapy Study Schema | 394 | Randomization (+ Repeat until disease progression) | 已有 (边标签) |
| 14 | :551 | Ex4 Prospective View | 395 | Randomization | 已补 → SE |
| 15 | :578 | Ex4 Retrospective View | 395 | Randomization | 已补 → SE |
| 16 | :606 | Ex4 Retrospective View with Explicit Repeats | 395 | Randomization (+ If disease progression) | 已补 → SE |
| 17 | :642 | Ex4 Blinded View | 396 | Randomization (+ If disease progression) | 已补 → SE |
| 18 | :707 | Ex5 Different Chemo Durations Study Schema | 397 | Randomization (+ 周期注) | 已有 (边标签) |
| 19 | :727 | Ex5 Retrospective View | 397 | Randomization | 已补 → SE |
| 20 | :789 | Ex6 Different Cycle Durations Study Schema | 398 | Randomization (+ 周期注) | 已有 (边标签) |
| 21 | :809 | Ex6 Retrospective View | 398 | Randomization (+ 周期注) | 已补 → SE |
| 22 | :875 | Ex7 Study Schema with 5 "options" | 400 | Randomization + 2 个 Evaluation 注释 + Options | 已有 (边标签 + option N) |
| 23 | :897 | Ex7 RTOG-93-09 Prospective View | 400 | Randomization | 已补 → SE |
| 24 | :937 | Ex7 RTOG 93-09 Retrospective View | 401 | Randomization | 已补 → SE |

- 计数: `grep -c 'rand\["Randomization"\]'` = 17, `grep -c 'resp\["Response Evaluation"\]'` = 3; 无注释的图: 0 (24 张 PDF 图均带 Randomization 注释, 7 张 Schema 以边标签承载).
- 验证: fp 隔离重跑 regressions=1 (仅 ig34_p0396_a009, 预期 ATOM_ERR); check_links live docs 42.
