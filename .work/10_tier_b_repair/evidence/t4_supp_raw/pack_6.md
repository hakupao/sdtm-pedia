# T4.1 补检 结果 — 包 6/8 (#133-159, 27 条)

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T04:54:57Z (`date -u`)
- brief: `.work/10_tier_b_repair/subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`; 样本包: `.work/10_tier_b_repair/work/t4/supp/supp_pack_6.md`
- 看过的渲染页 (`source/cdisc/SDTMIG v3.4 (no header footer).pdf`, Read 带 pages): 39, 44, 48, 56, 57, 64, 115, 195, 196, 211, 247, 363, 364, 387, 388, 397, 398, 409, 440, 441
- 放大图 (临时目录 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/supp6/`): p247 Example 3 lb.xpt 两段裁切 (300 dpi), p277 pp.xpt 表头裁切 (300 dpi)
- 用过的命令: `pdftoppm -r 300 -f 247 -l 247 -x .. -y 2050 -W 1950 -H 230 -png`; `pdftoppm -r 300 -f 277 -l 277 -x 0 -y 0 -W 3400 -H 700 -png`; `grep -n` (KB 各文件 / `ig34_pNNNN.txt` / `t2_pdf_typo_registry.jsonl`); `sed -n` (KB 与 PDF 文本层区段); `git log --oneline -- knowledge_base/domains/TA/examples.md`; `git status --short knowledge_base` (KB 无未提交改动)
- 备注: 包里 FIG 层 KB 指针多为 T1 旧行号 (TA/examples.md 已因 B-TA / 解冻轮改过行号), 本审查一律以 HEAD 现文件重新定位.

## 逐条判定

| # | atom_id | 层 | 终态 | 判定 | 依据 | 说明 |
|---|---|---|---|---|---|---|
| 133 | ig34_p0044_a023 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p44 "Figure. Example of --ENRTPT and --ENTPT for Medical History" (时间轴示意图); `knowledge_base/chapters/ch04_general_assumptions.md:1001-1015` | 确为图. KB: 图题 + KB note + Mermaid + 图内注释文字斜体再现. 核对: 2002 框、MHENTPT 参照点框 "Assessment Date and Reference Time Point of 2006-11-02"、值框 MHDTC=2006-11-02 / MHSTDTC=2002 / MHENRTPT=ONGOING / MHENTPT=2006-11-02、注释句均与图一致; 边标签 "Medical event began" / "ONGOING beyond reference point" 为 KB note 已声明的添加, 与图 (实线到参照点、虚线箭头向右) 不矛盾 |
| 134 | ig34_p0387_a011 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p387 "Example Trial 1, Parallel Design Study Schema"; `knowledge_base/domains/TA/examples.md:32-47` | 确为图. KB: 小标题 "Study Schema" + KB note + Mermaid. 节点 Screen→Run-In→{Placebo, Drug A, Drug B}, 分支边标 Randomization, 与图一致 (3 臂、分支自 Run-In). Mermaid 填色与图 (粉/蓝/绿/黄/青) 不同, 属样式, 不是信息矛盾 |
| 135 | ig34_p0388_a001 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p388 上图 "Parallel Design Prospective View"; `knowledge_base/domains/TA/examples.md:51-77` | 确为图. KB: 小标题 + KB note + Mermaid. 3 epoch (Screening/Run-In/Treatment)、Screen 与 Run-In 各 1 块、Treatment 3 块、右侧 3 臂箭头、Randomization 注 — 与图一致. Randomization 指向 Run-In Epoch 子图 (图中箭头指 Run-In/Treatment 分界线), 属 Mermaid 近似, 不矛盾 |
| 136 | ig34_p0388_a003 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p388 中图 "Parallel Design Retrospective View"; `knowledge_base/domains/TA/examples.md:81-110` | 确为图. KB: 小标题 + KB note + Mermaid. 3×3 网格 (每臂 Screen→Run-In→Placebo/Drug A/Drug B)、右侧 3 臂箭头、Randomization 注, 与图一致 |
| 137 | ig34_p0388_a005 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p388 下图 "Parallel Design Blinded View" (包内 PDF 指针给的 p387 不对, 图在 p388); `knowledge_base/domains/TA/examples.md:114-133` | 确为图. KB: 小标题 + KB note + Mermaid. Screen→Run-In→Study Drug、Blind 箭头、Randomization 注, 与图一致 |
| 138 | ig34_p0397_a005 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p397 上图 "Example Trial 5, Different Chemo Durations Study Schema"; `knowledge_base/domains/TA/examples.md:703-719` | 确为图. KB: 小标题 + KB note + Mermaid. Screen 经 Randomization 分支到 Drug A→Rest→Follow 与 B→Rest→Follow; "Repeat until disease progression"; 注 "Total length Drug A cycle: 3 weeks" / "Total length Drug B cycle: 3 weeks" — 值与图一致. 图中弯箭头只画一条 (在 A 臂上方), KB 两臂各画一条重复边, 与正文 "treatment (A or B) and the rest ... repeated" 相符, 不矛盾 |
| 139 | ig34_p0397_a009 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p397 下图 "Example Trial 5, Cyclical Chemotherapy Retrospective View"; `knowledge_base/domains/TA/examples.md:723-747` | 确为图. KB: 小标题 + KB note + Mermaid. Screening Epoch 2×Screen; Treatment Epoch "Drug A \| Rest Repeat until disease progression" / "B \| Rest Repeat ..."; Follow-up Epoch 2×Follow; 臂 Drug A / Drug B; Randomization — 与图一致 (B 块标 "B" 也与图同) |
| 140 | ig34_p0398_a012 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p398 上图 "Example Trial 6, Different Cycle Durations Study Schema"; `knowledge_base/domains/TA/examples.md:785-801` | 确为图. KB: 小标题 + KB note + Mermaid. 结构同 Ex5; 注 Drug A 3 weeks / Drug B 4 weeks — 与图一致 |
| 141 | ig34_p0398_a016 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p398 下图 "Example Trial 6, Cyclical Chemotherapy Retrospective View"; `knowledge_base/domains/TA/examples.md:805-829` | 确为图. KB: 小标题 + KB note + Mermaid. 节点含 "Total length Drug A cycle: 3 weeks" / "Total length Drug B cycle: 4 weeks" (图中此二注确在 retrospective 图内), 其余结构与图一致 |
| 142 | ig34_p0409_a007 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p409 "Example Trial 1, Parallel Design Planned Visits"; `knowledge_base/domains/TV/examples.md:9-50` | 确为图. KB: 图题 (粗体) + KB note + Mermaid. 3 臂网格 + 5 个访视旗: 1 在 Screening、2 跨 Screening/Run-In、3 跨 Run-In/Treatment、4/5 在 Treatment — 与图一致. 边标签 "Start of Screen Epoch" / "1 wk after Treatment start" / "2 wk after Treatment start" 取自同页第 1 张 tv.xpt 的 TVSTRL, 图中无但不矛盾 |
| 143 | ig34_p0440_a009 | FIG | FIGURE_DEFERRED | HOLDS | 渲染页 p440 "Figure. Sample Specimen Relationship"; `knowledge_base/domains/RELSPEC/examples.md:9-38` | 确为图 (原子类型记 NOTE, 但内容是图). KB: 图题 + KB note + Mermaid. 6 节点 SPC-001(Tissue)、SPC-003(Brain)、SPC-001-A(Tissue)、SPC-001-B(Tissue)、SPC-003-A(RNA)、SPC-001-B-1(DNA), 边 001→001-A、001→001-B、001-B→001-B-1、003→003-A, 分 Level 1/2/3 — 与图逐项一致 |
| 144 | ig34_p0363_a014 | TRIAGE_RELOCATE | EXACT | HOLDS | 渲染页 p363 §6.4.2 列表项 2; `ig34_p0363.txt:37`; `knowledge_base/domains/FA/assumptions.md:60` | 逐字一致 ("2. A split FA domain following the guidance in Section 4.1.7, Splitting Domains:"), 位于 FA/assumptions.md `## §6.4.2 Naming Findings About Domains` 下, 位置正确 |
| 145 | ig34_p0364_a003 | TRIAGE_RELOCATE | EXACT | HOLDS | 渲染页 p364 §6.4.2 项 3 子项; `ig34_p0364.txt:5-6`; `knowledge_base/domains/FA/assumptions.md:68` | 逐字一致, 在 "3. Separate domains where:" 下, 位置正确 |
| 146 | ig34_p0364_a011 | TRIAGE_RELOCATE | EXACT | HOLDS | 渲染页 p364 §6.4.3 首段; `ig34_p0364.txt:18-20`; `knowledge_base/domains/FA/assumptions.md:79` | 逐字一致, 位于 `## §6.4.3 Variables Unique to Findings About` 下 |
| 147 | ig34_p0039_a014 | RULE_C1-manual-PDF+KB | EQUIVALENT | HOLDS | 渲染页 p39 §4.4.1 "Key aspects" 第 3 项; `ig34_p0039.txt:15-17`; `knowledge_base/chapters/ch04_general_assumptions.md:755` | 信息点: ① SDTM 与 SDTMIG 要求 ISO 8601 extended format ② 日期成分用连字符 ③ 时间成分用冒号 (原子止于此; 同项后句 basic format 不得使用亦在). KB 一个不少、无改义; 实际仅多粗体 "**extended format**", 近逐字, EQUIVALENT 偏保守但成立. 包内 KB 指针 721-723 不对, 实际在 755 |
| 148 | ig34_p0057_a001 | RULE_C1-manual-PDF+KB | EQUIVALENT | HOLDS | 渲染页 p56 §4.5.4 (该句在 p56 底部, 不在 p57); `ig34_p0056.txt:49-51`; `knowledge_base/chapters/ch04_general_assumptions.md:1485` | 信息点: ① QEVAL 可描述 SUPP-- 任一数据项的评估者 (另含 PDF 后续: 见 8.4.1、数据客观时非必需). KB 全句承载, 位于 `### 4.5.4` 下. 包内指针 1369 不对, 实际 1485. 原子页号记 57 与 PDF 实际 p56 不符 (台账元数据问题, 不影响 KB 判定) |
| 149 | ig34_p0441_a003 | RULE_C1-manual-PDF+KB | EQUIVALENT | HOLDS | 渲染页 p441 §9 Study References 引言; `ig34_p0441.txt:3`; `knowledge_base/domains/DI/assumptions.md:5` | 信息点: "The following situations have been identified thus far:" 及其后两项 (devices / non-host organisms, KB:7-8). KB 逐字承载, 位于 DI/assumptions.md `## §9 Study References` 下 (§9 章首, 紧接 9.1 DI), 位置合理. 包内指针 ch10_appendices.md:66 不对 |
| 150 | ig34_p0196_a006 | RULE_C7-K4-rereview | ATOM_ERR | HOLDS | 渲染页 p196 --LOBXFL 行; `ig34_p0196.txt:13-14`; `knowledge_base/domains/LB/assumptions.md:43` | ① 原子≠PDF: 原子 "Operationally **defined** indicator", PDF "Operationally **derived** indicator". ② KB=PDF 逐格: --LOBXFL / Last Observation Before Exposure Flag / Char / * / Record Qualifier / "Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null." / Perm — 7 格全一致, 位于 §6.3.5.1 通用规格表 |
| 151 | ig34_p0247_a021 | RULE_C7-K4-rereview | ATOM_ERR | HOLDS | 渲染页 p247 Example 3 lb.xpt Row 1 (300 dpi 放大); `ig34_p0247.txt:71-72`; `knowledge_base/domains/LB/examples.md:69` | ① 原子≠PDF: LBRESTYP 原子 "PtFtv" vs PDF "PrThr"; LBDTC 原子 "1999-05-15T04:00" vs PDF "1999-06-19T04:00". ② KB=PDF 29 格逐格: 1/ABC/LB/ABC-001-001/1/HCG/Choriogonadotropin Beta/CHEMISTRY/-/空/Ord/PrThr/空/空/NEGATIVE/空×7/2106-3/URINE/Y/1/BASELINE/1999-06-19T04:00/Y — 全一致. (同表表头 PDF "LBSTRNHI" 而 KB "LBSTNRHI", 已登记 `B-LB T-1`, 非本原子) |
| 152 | ig34_p0195_a004 | RULE_T2-fix+deltaRereviewPASS+auditPASS | EQUIVALENT | HOLDS | 渲染页 p195 §6.3.5.1 第 3 项子项 1; `ig34_p0195.txt:8`; `knowledge_base/domains/LB/assumptions.md:14` | 信息点: 各域含额外变量 / 有特定 CT codelist / 有域特定 Core 值. KB 逐字 (o 圆点改为嵌套 "-"), 层级保留, 位于 §6.3.5.1 |
| 153 | ig34_p0195_a005 | RULE_T2-fix+deltaRereviewPASS+auditPASS | EQUIVALENT | HOLDS | 渲染页 p195; `ig34_p0195.txt:9-10`; `knowledge_base/domains/LB/assumptions.md:15` | 信息点: Findings 类含额外 permissible 变量 / 可在表示 specimen-based lab findings 时加入. KB 逐字, 层级与位置正确 |
| 154 | ig34_p0195_a006 | RULE_T2-fix+deltaRereviewPASS+auditPASS | EQUIVALENT | HOLDS | 渲染页 p195; `ig34_p0195.txt:11-12`; `knowledge_base/domains/LB/assumptions.md:16` | 信息点: permissible identifier 与 timing 变量可加入 / 例: 关联记录标识、计划时间点、实际时间. KB 逐字, 位置正确 |
| 155 | ig34_p0211_a009 | RULE_T2-fix+deltaRereviewPASS+auditPASS | EQUIVALENT | HOLDS | 渲染页 p211 Rows 9-11 第 2 段; `ig34_p0211.txt:26-29`; `knowledge_base/domains/CP/examples.md:81` | 信息点: ① row 11 比值基于 row 9 viable 与 row 10 non-viable 计数 ② 故不宜用 CPCELSTA ③ viability 预协调进 CPTEST ④ 因细胞状态已预协调, 去掉 "Sub" ⑤ Test Name 为 "Lymphocytes Viable/Lymphocytes NonViable" 而非 "Lymphocytes Sub Viable/Lymphocytes Sub NonViable" ⑥ CPGRPID 把 row 11 与 rows 9、10 分组. KB 全部承载、值一致. 唯一差异: KB 补了 PDF 缺的闭括号 `NonViable").` — 已登记 PDF 笔误 `B-CP T-1` |
| 156 | ig34_p0277_a003 | RULE_T2-fix+deltaRereviewPASS+auditPASS | EQUIVALENT | HOLDS | 渲染页 p277 "Pharmacokinetic Parameters (PP) Dataset for All Examples" pp.xpt 表头 (300 dpi 放大) + `ig34_p0277.txt:3`; `knowledge_base/domains/PC/assumptions.md:86-90` | 20 个列名逐个比: Row/STUDYID/DOMAIN/USUBJID/PPSEQ/PPGRPID (Example 1)/(Example 2)/(Example 3)/(Example 4)/PPTESTCD/PPTEST/PPCAT/PPORRES/PPORRESU/PPSTRESC/PPSTRESN/PPSTRESU/PPSPEC/PPNOMDY/PPRFTDTC — 全一致, 顺序一致; 位于 PC/assumptions.md `## §6.3.5.9.3 Relating PP Records to PC Records` 下, 前有同名标题 "Pharmacokinetic Parameters (PP) Dataset for All Examples" + **pp.xpt**. 包内指针 PP/examples.md:112 只是交叉引用, 承载处在 PC/assumptions.md. 实际是逐字, EQUIVALENT 偏保守但成立 |
| 157 | ig34_p0048_a012 | RULE_T1-two-agent | EQUIVALENT | HOLDS | 渲染页 p48 §4.4.10 "Option 2" 表; `ig34_p0048.txt:9-12`; `knowledge_base/chapters/ch04_general_assumptions.md:1162-1165` | PDF 为合并单元格表: VISIT "PERIOD 1, DAY 5"、VISITNUM "4" 纵跨 6 行, --TPTREF "PM DOSE" 纵跨 3 行. 原子把合并值展开到 PRE-DOSE/1/PM DOSE 行. KB 用 "PERIOD 1, DAY 5 \| 4" 起组 (1162) + 组内留空, 1165 行 `\| \| \| PRE-DOSE \| 1 \| PM DOSE \|`. 信息点 VISIT/VISITNUM/--TPT/--TPTNUM/--TPTREF 五值都在, 组归属一致, 无改值 |
| 158 | ig34_p0064_a001 | RULE_T1-two-agent | EQUIVALENT | HOLDS | 渲染页 p64 首行 (ARMCD 跨页续行) + p63 `ig34_p0063.txt:48-51`; `knowledge_base/domains/DM/spec.md:219` | 信息点: ① ARMCD 长度为 20 的例 (续句) ② 未分配臂则 ARMCD null 且 ARMNRS 填 ③ 除多阶段臂分配研究外, 须为 TA 数据集中的 ARMCD 值. KB 把 p63+p64 两段合并为完整 CDISC Notes, 逐字 (仅多一空格), 位置在 DM spec ARMCD 下 |
| 159 | ig34_p0115_a030 | RULE_T1-two-agent | EQUIVALENT | HOLDS | 渲染页 p115 Example 6 Subject 56789001 CRF 表头; `ig34_p0115.txt:34-36`; `knowledge_base/domains/EX/examples.md:245-247` | PDF 两层表头: 第 1 层 "Period 1" (跨 5 列) / "Period 2" (跨 5 列); 第 2 层 Day / Bottle 1 # of capsules / Bottle 2 # of tablets / Start Date/Time / End Date/Time ×2. KB 以首行 `\| Period 1 \| \| \| \| \| Period 2 \| ...` + 第二行 10 个列名再现, 10 列逐个一致, 分组归属一致. 原子写成 "Period 1: Day" 等合并式, 信息同 |

## 计数

| 层 | 条数 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE |
|---|---|---|---|---|---|
| FIG | 11 | 11 | 0 | 0 | 0 |
| TRIAGE_RELOCATE | 3 | 3 | 0 | 0 | 0 |
| RULE_C1-manual-PDF+KB | 3 | 3 | 0 | 0 | 0 |
| RULE_C7-K4-rereview | 2 | 2 | 0 | 0 | 0 |
| RULE_T2-fix+deltaRereviewPASS+auditPASS | 5 | 5 | 0 | 0 | 0 |
| RULE_T1-two-agent | 3 | 3 | 0 | 0 | 0 |
| **合计** | **27** | **27** | **0** | **0** | **0** |

各层均 NOT_HOLD 0、UNVERIFIABLE 0 → 按 brief 层通过条件全部通过. 无 HOLDS_AS_EQUIV.

引用的已登记 PDF 笔误: `B-CP T-1` (#155), `B-LB T-1` (#151 同表表头, 非本原子).

## 样本外发现的 KB 内容问题

无 KB 内容错误. 仅记以下非 KB 观察 (不算判定, 不修):
1. 台账元数据: `ig34_p0057_a001` 的句子实际在 PDF p56 底部 (§4.5.4 首段), 原子页号 57 不准.
2. 包内 KB 指针: #133/#136-#141/#147/#148/#149/#156 的指针是 T1 旧行号或交叉引用处, 与 HEAD 实际承载位置不符 (本审查已自行重定位, 见上表).
3. PDF 自身不一致 (非 KB 问题): p440 图中 SPC-003 标 "(Brain)", 而同页 relspec.xpt Row 5 SPEC = "TISSUE"; KB `knowledge_base/domains/RELSPEC/examples.md:17` 与 `:50` 分别照录, 两处均与 PDF 一致. 如需处理, 可考虑登记.
4. TA Example 1 各 Mermaid 填色与 PDF 图不同 (`knowledge_base/domains/TA/examples.md:42-46`), 仅样式, 不承载信息.
