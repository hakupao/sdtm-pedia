# T2 B-TV auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus); 与 writer (executor) / reviewer (code-reviewer) 不同; 先独立判, 判完才对照 writer/reviewer 报告。
> 基线 `git diff HEAD -- knowledge_base/domains/TV/` (本批未提交)。只读 KB。

## 抽样
- 标准命令 (pdf_pages=[407], kb_files=examples.md) 只得 P=12 且含 p407 a007-a009 (TE 例子 Note, 非本域) → 按 brief "抽样页范围 = 本域完整 PDF 节页范围" 改用:
  pages={407,408,409,410}, kb_files ∪ `knowledge_base/domains/TV/assumptions.md` (本批实际改动), 去掉 p407 a001-a009 (TE) 与 p410 a025+ (TD); 其余逻辑 (X/IEL/OTH 剔除、N 公式、seed、抽样顺序) 与模板一致。
  脚本与输出: scratchpad `t2_B-TV_auditor/sample2.json` (seed 20261126)。剔除: X = ig34_p0408_a006 (spec 表脚注 NOTE); OTH = 无。
- **seed = 20261126; C = 1 (ig34_p0407_a020); P = 51; N = 10** (C 抽 1 + P−C 抽 9)。
- 样本: p407_a020, p409_a033, p407_a013, p410_a012, p410_a015, p407_a018, p409_a006, p409_a009, p410_a013, p408_a015

## 逐样本判 (PDF 真值 = pdftotext p407-410 + p409 渲染)
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0407_a020 (C, REAL_GAP) | p407:39 Protocols define visits to describe assessments/procedures at the visits | TV/assumptions.md:19 | 否 | 是 | 是 (TV – Description/Overview 末句) | 逐字; HEAD 中缺, 本批补入 |
| 2 | ig34_p0409_a033 | p409:45-p410:1 "A trial visit also" (跨页句首) | TV/examples.md:87 | 否 | 是 | 是 (Identifying Trial Visits) | 与 p410_a001 续句合为完整句, 逐字 |
| 3 | ig34_p0407_a013 | p407:27-28 §7.3 引言 bullet 2: efficacy assessment schedule (Section 7.3.2, TD) | TV/assumptions.md:8 | 否 | 是 | 是 (§7.3 引言) | 逐字, 交叉引用保留 |
| 4 | ig34_p0410_a012 | p410:18 timings of visits may be expressed in terms not easily quantified | TV/examples.md:99 | 否 | 是 | 是 (Trial Visit Rules) | 逐字 |
| 5 | ig34_p0410_a015 | p410:21-22 trial start rule value "On the day of, but before, …Treatment Epoch" | TV/examples.md:99 | 否 | 是 | 是 | 逐字含引号值 |
| 6 | ig34_p0407_a018 | p407:36 TV 首句: trial design domain, planned order/number of visits within each arm | TV/assumptions.md:15 | 否 | 是 | 是 (Description/Overview 首句) | 逐字; 本批补入 |
| 7 | ig34_p0409_a006 | p409:4-7 transition events (eligibility→visit 2; first dose→visit 3) | TV/examples.md:5 | 否 | 是 | 是 (Example 1 引言) | 逐字 |
| 8 | ig34_p0409_a009 | p409:14-15 first TV dataset = idealized, specific timings | TV/examples.md:59 | 否 | 是 | 是 (图后、表前) | 逐字 |
| 9 | ig34_p0410_a013 | p410:18-20 baseline visit: randomized, given drug, first dose at bedtime | TV/examples.md:99 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0408_a015 | p408:53-58 Assumption 6: VISITNUM valid values; see Section 5.5; VISIT pairing | TV/assumptions.md:39 | 否 | 是 | 是 (TV – Assumptions 6) | 逐字, "see Section 5.5, Subject Visits" 保留 |

**独有信息丢失 = 0/10; 忠实度错误 = 0/10; 位置错误 = 0。**

## 附加核查
- **P 全 51 原子机械匹配** (引号/空白归一, 去列表编号): 51/51 在 TV/assumptions.md ∪ TV/examples.md 中逐字命中, 0 MISS。
- **本批改动逐条对 PDF**:
  - Description 首句 (a018) + 末句 (a020) 逐字; spec 首句 = p407:41 逐字; 标题 `TV – Description/Overview` / `TV – Specification` U+2013、spec 句 U+2014 码位与 PDF 一致; 位置 Description 与 Assumptions 之间 (CM/IS 先例)。
  - Assumption 5 "visit end times" → "visit ends" = p408:47 逐字 (词级修, 授权内)。
  - 图题 `Example Trial 1, Parallel Design Planned Visits` = p409:9 逐字。
  - diff 仅触及授权范围 (Description/Overview、spec 首句、assumption 5 词级、examples 图题/D6/Mermaid); §7.3 引言 (assumptions.md:3-11) 本批未改且与 p407:23-32 逐字。
- **Mermaid vs p409 渲染图** (r=200 逐节点/边): 3 epoch 列 (Screening/Run-In/Treatment) ✓; 3 行 Screen→Run-In→{Placebo, Drug A, Drug B} ✓; 右侧 3 个 arm 箭头 Placebo/Drug A/Drug B 指向对应 Treatment 单元 ✓; 旗 1 在 Screening 起点, 2 跨 Screen/Run-In 边界, 3 跨 Run-In/Treatment 边界, 4、5 在 Treatment 内 ✓ (与 p409:3-7 叙述和两张 tv.xpt TVSTRL 一致); Randomization: PDF 红箭头指向 Run-In 列右缘 (Run-In/Treatment 边界下方), Mermaid `rand -.-> RE` 为 TA 先例近似 → 按 brief 接受。PDF 的 "Visit numbers →" 侧标未画, 属纯标注, 不影响逻辑。旗边标签 "1 wk / 2 wk after Treatment start" 与表 Row 4/5 一致, 且在 D6 标注图内。
- **3 条 D6 (`> KB note (not in SDTMIG):`)** 与 PDF 不矛盾:
  1. "based on TA Example Trial 1, Parallel Design with 3 arms (Placebo, Drug A, Drug B)" — 与图题 "Example Trial 1, Parallel Design" 及图中 3 arm 一致; TA/examples.md:22 同口径。
  2. Mermaid 为 PDF 图 KB 重绘 — 标注措辞符合口径。
  3. "Visit 2 spans Screen→Run-In (confirmation of eligibility); Visit 3 spans Run-In→Treatment (first dose); 3 arms share the same visit schedule" — 前两句复述 p409:4-7; 第三句与 PDF 两张 tv.xpt 无 ARMCD (各 arm 同一日程, 符合 Assumption 1) 一致。
- **范围外**: p407 a007-a009 (TE 例子 Note) 在 TE/examples.md 命中 1 处, 不属本批, 无发现。
- **G-TB8**: trace.jsonl 283/301 (executor a1/a2)、299/306 (code-reviewer a1 CONDITIONAL → a2 PASS, writer a2 delta 已回 reviewer 复审) 均在; `"agent": "main"` 记录 6 条, 其中 B-TV 0 条 → 无主控写 KB。
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` = 基线 42。

## 对照 (判完后)
writer `t2_B-TV.md` / reviewer `t2_B-TV_review.md` 声明的改动 (1 atom + 7 NEW, Mermaid 补全) 与本审独立结论一致; 无分歧。

## 结论
**PASS** — Rule A N=10 seed=20261126: 丢失 0, 忠实 0 (P 全 51 原子机械匹配 0 缺失)。
