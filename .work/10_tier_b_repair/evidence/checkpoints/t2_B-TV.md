# T2 checkpoint — B-TV (writer, attempt 1)

- base HEAD: `a4c9359`; base md5: TV/assumptions.md `b494e1bc0180bdfa60cb681e4de2e10c`, TV/examples.md `fc84f5bc338cb19a4b538df7fefcf1b1`
- after md5: TV/assumptions.md `623db433598155fbab78ae9f3f1b1b92`, TV/examples.md `0ca60cdd0e4488c093b09df07fcc7443`; TV/spec.md 未动
- kb_files: TV/examples.md + 主控通用授权 TV/assumptions.md (Description/spec 首句/§7.3 引言 + assumptions 逐词修)
- TI/assumptions.md: 按主控指示只读, 未改
- 真值: `work/pdf_pages/ig34_p0407..0410.txt` + pdftoppm r110 渲染 p407-410 (表格/图对图核)

## O20 页范围
TV 节实际 PDF 范围 = **p407 下半 (7.3 标题起) – p410 上半 (7.3.2 TD 之前)**. 其中 §7.3 引言 + 7.3.1 Description/spec 首句 p407, spec 表 p407-408, Assumptions p408, Examples p409, 7.3.1.1 Issues p409-410.
batch json `pdf_ranges` 写 409-412 不对 (p410 下半-412 属 TD). 本批按 407-410 全扫; batch json 未改 (只登记, O20).

## 变更清单
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | TV/assumptions.md:19 | ig34_p0407_a020 | INSERTED | Description 末补 "Protocols define visits in order to describe assessments and procedures…at the visits." | 407 |
| 2 | TV/assumptions.md:15 | NEW-1 (Description 首句) | INSERTED | 补 "A trial design domain that contains the planned order and number of visits in the study within each arm." | 407 |
| 3 | TV/assumptions.md:21-23 | NEW-2 (spec 首句) | INSERTED | 新增 `## TV – Specification` + "tv.xpt, Trial Visits — Trial Design. One record per planned Visit per Arm, Tabulation." (TE/CM 先例; 本文件标题用 "–") | 407 |
| 4 | TV/assumptions.md:37 | NEW-3 (assumption 5 逐词) | REPLACED | "information about visit end times because" → "information about visit ends because" | 408 |
| 5 | TV/examples.md:7 | NEW-4 (D6) | REPLACED | KB 自写 "This example is based on TA Example Trial 1…" 加前缀 `> KB note (not in SDTMIG):` (与 p409 图一致: 3 arms Placebo/Drug A/Drug B) | 409 |
| 6 | TV/examples.md:9 | NEW-5 (图题) | REPLACED | `**Parallel Design Planned Visits**` → `**Example Trial 1, Parallel Design Planned Visits**` (PDF 图题全文) | 409 |
| 7 | TV/examples.md:11 | NEW-6 (D6 Mermaid) | INSERTED | Mermaid 前加 `> KB note (not in SDTMIG): the following Mermaid diagram is a KB rendering of the PDF figure "…Planned Visits".` (TA/examples 措辞) | 409 |
| 8 | TV/examples.md:38 | NEW-7 (D6) | REPLACED | 图下 KB 自写说明 blockquote 加前缀 `KB note (not in SDTMIG):` | 409 |

atoms 覆盖: 1/1 (a020 INSERTED). census diff_tables 0 / pdf_only 0 / unparseable 0.
新增 atom 清单 (R3, 不在 atoms[]): NEW-1 … NEW-7 (#2-8).

## Mermaid / D6 核对 (对 p409 渲染)
- PDF 图: 3 epoch 列 (Screening / Run-In / Treatment), 旗 1 在 Screening 起点, 2 跨 Screening→Run-In, 3 跨 Run-In→Treatment, 4/5 在 Treatment 内; 下方 3 行 arm (Placebo / Drug A / Drug B), Run-In 后 Randomization.
- KB Mermaid: V1 Start of Screen, V2 Screen→Run-In, V3 Run-In→Treatment, V4/V5 Treatment 内 (标签 "1 wk / 2 wk after Treatment start" 取自同页 tv.xpt TVSTRL) — 与图一致, 不矛盾; 未画 arm 行/Randomization (省略, 非矛盾). 图下说明句与图/叙述一致.

## 表格逐格 (p409 渲染)
- tv.xpt #1 (5 行) 与 #2 (5 行) 逐格一致; #2 Row1/Row4 TVENRL 空一致. 未改.
- 表前标签 `**tv.xpt (specific timings)**` / `**tv.xpt (loosely described timings)**`: PDF 均为 "tv.xpt"; 括号为 KB 导航区分标签, 按 D6 "表前短标签" 不标注, 保留并在此列出 (reviewer 定).

## 双向全扫 (p407 下半 – p410 上半)
- 方法: `$S/scan.py` (S = scratch `t2_B-TV_writer/`), 引号/空白归一化后句级子串比对, 双向; 表格与图对渲染人工核.
- PDF→KB: 未命中仅 (a) 标题与正文在 pdftotext 中粘连的伪差 (7.3 / 7.3.1 / TV – Examples / 图题 / 7.3.1.1 + 首句), 逐条人工确认 KB 有对应; (b) spec 变量表 + 脚注 ¹ (p407-408, 属 TV/spec.md, 不在 kb_files → F-1); (c) tv.xpt 表 (layout 折行, 已对渲染核). 改后其余每句命中.
- KB→PDF: 未命中仅 标题行 (导航)、D6 KB note 3 处、Mermaid 代码、表前标签、表分隔行、loose 表折行单元格 (渲染核一致). 无未标注的 KB 自写正文.
- 引号: KB 直引号 vs PDF 弯引号 (§7.3 引言 "subject’s", examples "visit"/"visits"/"windows") — 样式差, 按 B-TE 先例未改.
- 标题: `## §7.3 Schedule for Assessments (TV, TD, TM) — Introduction` (PDF "(TV, TD, and TM)") 与 `## Trial Visits Issues` (PDF "7.3.1.1 Trial Visits Issues") 为导航标题, 规则 6 不改锚点, 保留.

## §7.3 引言位置 (主控要求核)
- §7.3 引言 (p407: 3 bullets + "The Trial Visits (TV) and TD datasets…") 在 `TV/assumptions.md:3-11`, 对 PDF 逐句一致 (仅弯引号样式差).
- `TI/assumptions.md` 只读核: 其中是 `## §7.4 Trial Eligibility and Summary (TI, TS) — Introduction` (+ §7.5), **不含 §7.3 引言**; 全 KB grep §7.3 引言句仅 TV/assumptions.md 命中 → 无重复/缺失. B-TE auditor "§7.3 引言在 TI/assumptions.md" 的说法不准确 (实为 TV); 对 TI 无需动作.

## PDF_TYPO / 删除清单
- 无 PDF_TYPO; 无删除 (只有替换 #4/#6 的旧值).

## 范围外发现
- F-1: TV/spec.md (p407-408 spec 表 + 脚注 ¹) 不在 kb_files, 未核 → 并入 O15/O24/O26 spec 扫描.
- F-2: B-TV.json pdf_ranges 409-412 错 (应 407-410) → O20.

## 需主控定
- 无 (TI 无问题).

## 链接检查
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (未升).

## git diff --stat
```
 knowledge_base/domains/TV/assumptions.md | 10 +++++++++-
 knowledge_base/domains/TV/examples.md    |  8 +++++---
 2 files changed, 14 insertions(+), 4 deletions(-)
```

## attempt 2 (按 reviewer CONDITIONAL 问题 1; 2026-11-26T05:10:12Z)
- 只改 TV/examples.md:13-55 Mermaid 图; 其它行未动. after md5 examples.md `090fc8b76bd7099c0c96b2c5821ba3de`; assumptions.md 未动 (`623db433598155fbab78ae9f3f1b1b92`).

| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 9 | TV/examples.md:13-55 | NEW-6a (Mermaid 补全) | REPLACED | graph TD 只画 3 epoch + 5 旗 → graph LR: 3 epoch subgraph 内 3 行 arm 元素 (Screen → Run-In → Placebo / Drug A / Drug B) + 右侧 arm 标签箭头 + `rand["Randomization"] -.-> RE` (TA/examples.md:75 写法) + 旗 1-5 (节点名改为 PDF 旗号 "1"…"5", 边/标签不变) | 409 |

- 对 p409 渲染逐节点核: 3 epoch 列 Screening/Run-In/Treatment ✓; 每 epoch 3 个元素格 (Screen×3, Run-In×3, Placebo/Drug A/Drug B) ✓, 行序 Placebo/Drug A/Drug B 自上而下 ✓; 右侧 arm 箭头 Placebo/Drug A/Drug B 指向各行 Treatment 元素 ✓; Randomization 红箭头在 Run-In 右缘 (Run-In/Treatment 交界) — Mermaid 无法指向边界, 按 TA 先例指 RE subgraph ✓; 旗 1 Screening 起点, 2 跨 Screening/Run-In, 3 跨 Run-In/Treatment, 4/5 在 Treatment 内 ✓.
- D6 标注 :11 保留; :57 图下 KB note 未动 (与图不矛盾).
- 语法: 写法 (subgraph id 作边端点、链式边 `S1 --> R1 --> P`、`>"…"]` 旗形节点) 均同 TA/examples.md 已有图; 本地 mermaid-cli 渲染被权限拒绝, **未实际渲染** — reviewer 如需请用渲染器复核.
- live docs: 见下行.
broken relative links: 18668 (live docs: 42)
