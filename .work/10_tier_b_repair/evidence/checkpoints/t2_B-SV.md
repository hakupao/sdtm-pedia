# T2 B-SV writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `a4c935920433a331e0350ea4230817402e16841e`; 基线取 `git show HEAD:<file>` (改前 SV 三文件与 HEAD 一致)
- md5: SV/assumptions.md `f4316cc31ce4b2bddbb1d8a33729fb22` → `5d7f4b1b8167fbd88a482e0c893c73fb` (53 → 57 行); SV/examples.md `569f3e307ae2e66390d20364084e2efd` → `7c5768b9d360118efc89d0f22ac115d5` (95 行不变); SV/spec.md 未动 `2208d850b2dd4ed2c242e3f0e9af42b3`
- 白名单: examples.md (batch json) + assumptions.md (通用授权: Description/Overview + spec 首句 + 节引言 NOTE; 追加授权: assumptions 列表逐词偏差)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SV_writer/` (p86/p88/p90 渲染 110dpi)
- 本批 atoms 0 / t2_recheck 0; census DIFF 1 表 (1 CELL, KB 行 53); pdf_only 0; unparseable 0; notes O33.
- 页范围核 (O20): SV 节 = p86 中部 "5.5 Subject Visits (SV)" (p86 上部为 SM Ex 尾 ce.xpt, 不碰) → Description/Overview + spec 首句 + spec 表 (p86-87) → Assumptions 1-6 (p87) → 6 续-16 (p88) → Examples Ex1 tv/ds (p89) → ds 续 + sv Rows 1-8 (p90) → sv Rows 9-15 (p91); p92 起 §6 AG. batch lo/hi = 86-91 **完整覆盖** (`pdf_pages` 89-90 仅 census 表页). PDF 节内无节引言 NOTE.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | SV/assumptions.md:5 | ig34_p0086_a003 (O33) | INSERTED | 补 Description 首句 "A special purpose domain that contains information for each subject's actual and planned visits." (独立段, 照 PDF) | 86 |
| 2 | SV/assumptions.md:7 | ig34_p0086_a004 (O33) | INSERTED | 补 "The Subject Visits domain consolidates … (VISITNUM and possibly VISIT and/or VISITDY)." (段首) | 86 |
| 3 | SV/assumptions.md:7 | ig34_p0086_a005 (O33) | INSERTED | 补 "Unless the beginning and end of each visit is collected, … involve derivations." | 86 |
| 4 | SV/assumptions.md:7 | ig34_p0086_a006 (O33) | INSERTED | 补 "In a simple case, … single date for a visit." | 86 |
| 5 | SV/assumptions.md:7 | ig34_p0086_a007 (O33) | INSERTED | 补 "When there are multiple dates and/or date/times … may be more complex." 其后接原有 "The method for deriving …" (a008/a009 不动) | 86 |
| 6 | SV/assumptions.md:9 | ig34_p0086_a011 (O33, 改义) | REPLACED | "planned but not completed visits" → "planned but not expected visits due to a subject not completing the study" (渲染图为准; 原子 verbatim 同错); 原 "The SV dataset provides …" 起另起段 (PDF 为第 3 段) | 86 |
| 7 | SV/assumptions.md:51 | R3/追加授权 (assumption 15b 逐词) | REPLACED | "information about the visit was collected" → "…was recorded" (PDF p88 15b; 同条前句 "data was collected" 不动) | 88 |
| 8 | SV/examples.md:53 | census:examples.md:53:6:DSSTDY | REPLACED | `28` → `26` (渲染图 p90 ds Row 6 DSSTDY = 26; 与 sv Row 15 SVSTDY 26 同日 2020-03-16 一致) | 90 |
| 9 | SV/examples.md:40 | R3 扫描 (Ex1 ds 说明 Row 5) | SKIPPED_PDF_TYPO | PDF "Shows informed consent for subject 101" 句末无句点 → KB 保留句点 (T-1) | 89 |

- 覆盖率自查: atoms 0; census 1 格 = #8; O33 = #1-6; R3 新增 #7; PDF_TYPO #9.
- spec 首句 (assumptions.md:13) 已逐字存在, 未改.

### 删除清单
- D-1 SV/assumptions.md 原第 5 行内短语 "planned but not completed visits" (改义改写, 由 #6 PDF 原文替换). 该短语仅承载 a011 (a010 "The SV dataset provides …"/a012 "Comparison of the values …" 句未动), 不承载其他原子. 无其他删除.

### census 表处理
| census ref | 处理 | 改后 |
|---|---|---|
| examples.md:46 Ex1 ds.xpt (1 CELL, 行 53) | #8 | 预期 OK |
| tv.xpt (:19) / sv.xpt (:79) | census OK; 渲染图 p89-91 人工逐格复核一致 | OK |

### 双向全扫 (p86-91)
- PDF→KB: 脚本 (规范化引号/空白/列表号, 按句切分) 将 p86-90 叙述句逐句查 KB assumptions+examples; 改后仅余 (a) spec 表行/脚注 (在 spec.md, 不在本批), (b) 与标题粘连的切分伪差 (Assumption 1、Ex1 首句, 人工确认在 KB), (c) #9 PDF_TYPO. tv/ds/sv 三表对 p89-91 渲染/layout 逐格一致 (除 #8 已修).
- KB→PDF: assumptions.md 全文 (Description 3 段、spec 首句、Assumptions 1-16 含 4a-d/15a-f) 与 examples.md 全文 (引言、行说明、3 表) 逐句对 PDF, 除 #6/#7/#8 外无 KB 多出/自写内容; 无 D6 项.
- spec.md (白名单外) 顺带核: 17 变量 Label/Type/Role/Core/Notes 与 p86-87 一致.

### PDF_TYPO 清单
- T-1 (p89 Ex1 ds 说明 "Row 5"): 句末缺句点; 同组 Row 1-6 说明均以句点结尾 → KB 保留句点.

### 范围外发现
- F-1 SV/spec.md 缺 spec 表脚注 1 ("In this column, an asterisk (*) indicates …", p87). CM/spec.md 亦无 → 全域同类, 归 O26 spec 脚注扫描 (DEFERRED). 未改.
- F-2 SV/assumptions.md:9 "subject's" ×2 为直撇号, PDF p86 第 3 段为弯撇号 (第 1 段 PDF 本身为直撇号) → O40 全局口径, 未改.

### 需主控定
- 无.

### unparseable 表
- 未触碰任何 unparseable 表 (本批无).

### git diff --stat
```
 knowledge_base/domains/SV/assumptions.md | 8 ++++++--
 knowledge_base/domains/SV/examples.md    | 2 +-
 2 files changed, 7 insertions(+), 3 deletions(-)
```
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)`
