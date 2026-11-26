# T2 review — B-TV (reviewer, attempt 1)

- reviewer: oh-my-claudecode:code-reviewer (opus), 独立于 writer
- base = HEAD; 本批文件 md5 与 writer 报告一致: TV/assumptions.md `623db433598155fbab78ae9f3f1b1b92`, TV/examples.md `0ca60cdd0e4488c093b09df07fcc7443`; TV/spec.md 无 diff
- 页范围: 认可 writer O20 — TV 节 = p407 下半 (7.3) – p410 上半 (7.3.2 TD 前); batch json pdf_ranges 409-412 错

## verdict: **CONDITIONAL** (1 项修正: Mermaid 漏画 PDF 图中的 Randomization 与 arm 行)

## 命令 (S = scratchpad `t2_B-TV_reviewer/`)
- census: manifest `[{"file":"knowledge_base/domains/TV/examples.md","src":"ig34","lo":407,"hi":410}]` → `table_census.py` → `KB tables: 2; status: {'OK': 2}; cells compared: 60; diffs: 0` (exit 1 仅因全局 PDF_ONLY 337; 本批页 p407-410 的 PDF 表 = TE special.xpt (p407, 属 TE) + TV spec 表 (属 spec.md) + 2 张 tv.xpt (KB 已有, OK))
- fp_match: `RESULT: RED` 全局 60 条回归, 页码均不在 p407-410 (MI/MB 等他批) → 本批 0 回归
- 直查目标: `norm(a020) in norm(TV/assumptions.md)` = True (fp verdict 仍标 PARTIAL 系 md_atoms 未重生成, 文本已逐字命中 :19)
- 其他本批页非 EXACT/EQUIV: p0409_a007 FIGURE MISSING (图, 见问题 1); a011/a018 `tv.xpt` CODE_LITERAL norm 命中; p0410_a023 norm 命中 examples.md:88
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (未升)
- 渲染: `pdftoppm -f 409 -l 409 -r 110 -png` 读图核图/表

## 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| examples.md:13-36 (NEW-6 Mermaid) | Mermaid 与 PDF 图逻辑一致 | **[MEDIUM, 须修]** PDF 图含 3 行 arm 元素 (Screen→Run-In→Placebo / Drug A / Drug B) 与 "Randomization" 箭头指向 Run-In/Treatment 边界; Mermaid 只画 3 epoch + 5 旗, 未画 arm 行与 Randomization. 声称 "KB rendering of the PDF figure" 却丢了分支点; TV 全文无 Randomization. TA/examples.md:75 同图族先例画了 `rand["Randomization"] -.-> RE` | p409 图: "Randomization" 红箭头; 3 行 Screen / Run-In / Placebo·Drug A·Drug B |
| assumptions.md:3 标题 "(TV, TD, TM)" | G-TB6 结构行 | [LOW, 不阻塞] PDF "(TV, TD, and TM)"; 导航标题, 规则不改锚点, 保留 | p407 "7.3 Schedule for Assessments (TV, TD, and TM)" |
| examples.md:64 "## Trial Visits Issues" | 结构行 | [LOW] PDF 有节号 7.3.1.1; 导航标题保留 | p409 |

## CONDITIONAL 修正清单 (writer attempt 2)
1. TV/examples.md Mermaid (:13-36): 按 PDF p409 图补 (a) 3 行 arm 元素序列 Screen → Run-In → Placebo / Drug A / Drug B (可按 TA/examples.md Prospective View 写法), (b) `Randomization` 节点指向 Run-In→Treatment 边界 (TA:75 写法). 保留 :11 的 D6 标注. 修后图下 :38 KB note 若与图重复可不动 (不矛盾).
   - 改后回 reviewer 复审 delta.

## 逐条核 writer 8 处改动
| # | 位置 | 判定 |
|---|---|---|
| 1 | assumptions.md:19 a020 | 逐字 = p407 "Protocols define visits in order to describe assessments and procedures…at the visits." 位置在 Description 末, 正确 |
| 2 | assumptions.md:15 Description 首句 | 逐字 = p407 |
| 3 | assumptions.md:21-23 `## TV – Specification` + spec 首句 | 逐字 = p407 "tv.xpt, Trial Visits — Trial Design. One record per planned Visit per Arm, Tabulation."; 标题用 "–" 与本文件其他标题及 PDF 一致 (CM 先例同) |
| 4 | assumptions.md:37 "visit ends" | = p408 assumption 5 |
| 5 | examples.md:7 D6 | KB 自写, 与 TA Example Trial 1 (3 arms) 一致, 不矛盾 → D6 正确 |
| 6 | examples.md:9 图题 | = p409 图题全文 |
| 7 | examples.md:11 D6 Mermaid 标注 | 措辞同 TA 先例, 正确; 但图内容不全 → 问题 1 |
| 8 | examples.md:38 D6 | "Visit 2/3 spans…; 3 arms share the same visit schedule" 与 p409 叙述 + 图 + Assumption 1 不矛盾 → D6 正确 |

## 表前标签裁定 (主控指定)
`**tv.xpt (specific timings)**` / `**tv.xpt (loosely described timings)**` (:42, :52): 判 **纯导航, 保留, 不加 D6**. 理由: PDF 两表同名 "tv.xpt", 括号仅区分两张同名表, 用词取自紧邻 PDF 句 (:40 "provided specific timings" / "described only loosely"), 不引入新信息, 不矛盾; `tv.xpt` 本身 norm 命中 (a011/a018). 属 dispatch notes "表前短标签" 类.

## G-TB4 人工逐格 (p409 渲染, 独立于 census)
| 表 | 行 | 结果 |
|---|---|---|
| tv.xpt #1 (:44-50) | Row 1-5 × 6 列 | 一致 (TVENRL R1/R4/R5 "1 hour after start of Visit"; R2 "30 minutes after start of Run-in Epoch"; R3 "1 hour after start of Treatment Epoch") |
| tv.xpt #2 (:54-60) | Row 1-5 × 6 列 | 一致 (R1/R4 TVENRL 空; R2/R3 折行单元格拼接一致; R5 "At Trial Exit") |

## 双向全扫 (p407 下半 – p410 上半, 含表格原子)
- PDF→KB: §7.3 引言 3 bullets + 末句 → assumptions.md:5-11 逐句一致 (仅 subject’s 弯引号样式); 7.3.1 Description 3 句 → :15/:17/:19; spec 首句 → :23; spec 变量表 + 脚注 ¹ (p407-408) 属 TV/spec.md, 不在本批范围 (writer F-1, 认可); Assumptions 1-6 (含 4a/4b) → :27-39 逐句一致; Examples 叙述 → examples.md:5/:40/:62 一致; 图题 → :9; 两 tv.xpt 表 → 逐格一致; 7.3.1.1 Issues 全部小节 (Identifying / Rules / Ranges / Contingent) → :66-88 逐句一致 (弯引号 “visit”/“visits”/“windows” 样式差). **唯一缺: 图中 arm 行 + Randomization (问题 1)**.
- KB→PDF: 全文件逐行: 标题/锚点 (导航)、3 处 D6 KB note、Mermaid 代码 (D6 下)、2 表前标签 (导航, 上判)、表头/分隔行; 其余正文行均有 PDF 出处. 无未标注 KB 自写正文.

## G-TB6 结构行签字
- assumptions.md:21 `## TV – Specification` (新增节标题, PDF 有对应 "TV – Specification") — 签字
- examples.md:9 图题行 (PDF 原文) — 签字
- 其余 diff 行均为正文/D6, 已逐条核

## 无副作用
- KB diff 中本批只动 TV/assumptions.md + TV/examples.md (他批文件不计); 无标题/锚点改动; assumptions 改动在主控授权内 (Description/spec 首句/逐词修).
- 完整性: atoms 1/1 (a020) 处理; t2_recheck 0; census diff 0.

## attempt 2 (delta 复审: 变更 #9 Mermaid)

### verdict: **PASS**

### 终态一致性
- `git diff HEAD -- knowledge_base/domains/TV` 全量看: assumptions.md md5 `623db433598155fbab78ae9f3f1b1b92` 与 attempt 1 一致; examples.md md5 `090fc8b76bd7099c0c96b2c5821ba3de`.
- examples.md 中 mermaid 块之前 (1-13 行) 与 attempt 1 审过的内容一致 (只有 #5/#6/#7 三处); `Two TV datasets…` 起至文件末与 HEAD 逐字一致 (`diff` → TAIL_SAME); 图下 D6 KB note (:57) 未动. 变化只在 mermaid 块 (:13-55).

### 对 p409 渲染逐节点/边核
| PDF 图元素 | Mermaid | 判定 |
|---|---|---|
| 3 epoch 列 Screening / Run-In / Treatment | subgraph SE/RE/TE "Screening Epoch"/"Run-In Epoch"/"Treatment Epoch" | 一致 |
| 3 行 arm 元素 Screen→Run-In→Placebo / Drug A / Drug B (自上而下) | S1→R1→P, S2→R2→A, S3→R3→B | 一致 (行序、元素名) |
| 右侧 arm 箭头 Placebo / Drug A / Drug B 指向各行 Treatment 元素 | armP/armA/armB `>"…"]` -.-> P/A/B | 一致 |
| Randomization 箭头指向 Run-In/Treatment 交界 | `rand["Randomization"] -.-> RE` | 近似 (Mermaid 无法指向边界), 同 TA/examples.md:75/108/131 先例, 接受 |
| 旗 1 Screening 起点; 2 跨 Screening/Run-In; 3 跨 Run-In/Treatment; 4、5 在 Treatment 内 | V1→SE; V2→SE+RE; V3→RE+TE; V4/V5→TE, 节点名 "1"-"5" | 一致 |
| 旗边标签 "1 wk / 2 wk after Treatment start" | 取自同页 tv.xpt TVSTRL Row 4/5, 处于 :11 D6 标注下 | 不矛盾, 接受 |

### Mermaid 语法
- 渲染器: 本 reviewer 尝试 `npx @mermaid-js/mermaid-cli` 也被权限拒绝, **未实际渲染**.
- 逐行对照 TA/examples.md 同类图 (Prospective/Retrospective View, :55-110): `graph LR` + `subgraph ID["标题"]`、链式边 `X --> Y --> Z`、旗形节点 `id>"…"] -.-> N`、`rand[...] -.-> 子图ID`、`style rand …stroke-dasharray:5 5` 写法均同 TA 先例; 新增写法 `((“n”))` 圆节点、`-.->|"…"|` 带标签虚线边、对子图 ID `style SE fill:…` 在 Mermaid flowchart 中均为合法语法 (其中前两个 HEAD 原图已用). 子图/节点 ID 无重名 (SE/RE/TE、S1-3、R1-3、P/A/B、armP/A/B、rand、V1-5). 判语法正确; 建议主控有渲染器时补一次实际渲染 (非阻塞).

### 其他
- G-TB6: :13-55 全部位于 :11 D6 标注下的 KB 重绘, 无出处要求之外的正文.
- 链接: `broken relative links: 18668 (live docs: 42)`
