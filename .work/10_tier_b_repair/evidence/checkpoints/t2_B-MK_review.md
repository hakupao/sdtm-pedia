# T2 B-MK reviewer — attempt 1 (2026-11-26)

- reviewer: oh-my-claudecode:code-reviewer (opus); base = HEAD 884560f (本批未提交); writer 记录的 base 5440dc5 与 HEAD 间无 MK 提交, `git show HEAD:` md5 = writer "before" md5 (f199e776… / 9c2976de…) 一致.
- 改后 md5: examples.md `b8d525432dbb162f33c92238a800ac02`, assumptions.md `574bffa734b6e8d6025f59a647206ddd`, spec.md `974cac1f…` 未改 —— 与 writer 报告一致.
- MK 节 PDF 完整范围 (自行确认): ig34 p290 (§6.3.7.3 标题 / Description / spec 首句 / spec 表) – p291 (spec 表 + 脚注 1) – p292 (Assumptions 1-3, Ex1 叙述 + Rows) – p293 (Ex1 表, Ex2 叙述 + Rows, Ex2 表 r1-6) – p294 (Ex2 表 r7-16, 之后 §6.3.7.4 NV). spec 表 + 脚注属 spec.md (白名单外, 未改, 归 O15).

## Verdict: **PASS**

## 命令 (scratch = /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-MK_reviewer)
```
python3 -I -c "...dump pdf_ranges..." → $S/manifest.json   (ig34 290-294, MK/examples.md)
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  exit 1; "KB tables: 2; status: {'OK': 2}; PDF_ONLY: 337; cells compared: 608; diffs: 0"
  RED 仅因全局 PDF_ONLY; 页码落在 290-294 的 PDF_ONLY = 0; pdf_unparsed 只有 p274 / p342 (非本批)
  examples.md:17 Ex1 OK (ws_only 0); examples.md:49 Ex2 OK (ws_only 1 = T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  exit 1; RESULT: RED; REGRESS 30 条, 全在 p258-263 (MB/MS) 与 p363-364 (§6.4.2), 他批工作树改动; grep -cE 'p029[0-4]' fp_regress.jsonl = 0
python3 tools/check_links.py | tail -1  → live docs: 42 (= 基线)
```

## 1. 完整性
- atoms[] = 0, t2_recheck = 0 (无 R2 判定项).
- census DIFF 表 examples.md:49 的 kb_lines_with_diff 52/53/54/55/56/63 → writer #5-#10 全部处理, census_after = OK.
- 新增 atom (R3): #1 Description/Overview, #2 spec 首句, #3 `## MK – Assumptions` 标题, #4 Ex2 MKMETHOD 句 —— 全部核实 (见 G-TB6).

## 2. G-TB4 表格 (独立方法: 110 dpi 渲染 p293/p294 逐格目视, 非 census 自比)
| 表 | 行 | 结果 |
|---|---|---|
| Ex1 mk.xpt (examples.md:17-35, 16 行 × 18 列) | r1-16 | 全部一致 (STUDYID…MKDTC; r9-10 NOT DONE 无 REASND; r13-14 JOINT NOT EVALUABLE) |
| Ex2 r1 | MKORRES "MODERATE; 51-75% LOSS OF JOINT SPACE", MKLOC "INTERPHALANGEAL JOINT 1" | 一致 (PDF 用 en dash, 见 L-2) |
| Ex2 r2 | MKORRES "MODERATE-SEVERE; 76-95% LOSS OF JOINT SPACE" | 一致 (PDF "MODERATE- SEVERE;" 同一行带空格 = T-1); MKLOC "INTERPHALANGEAL JOINT 1" 一致 |
| Ex2 r3 | MKSTAT NOT DONE; MKREASND "AMPUTATION/MISSING ANATOMY/JOINT REPLACEMENT/SURGICAL ALTERATION"; MKLOC "PROXIMAL INTERPHALANGEAL JOINT 2 OF THE HAND" | 一致 (REASND 见 T-2) |
| Ex2 r4 | SEVERE; PARTIAL OR EQUIVOCAL ANKYLOSIS / 3.5 / PROXIMAL INTERPHALANGEAL JOINT 2 OF THE HAND / LEFT | 一致 |
| Ex2 r5 | MODERATE; 51-75% … / 2 / PROXIMAL INTERPHALANGEAL JOINT 3 OF THE HAND / RIGHT | 一致 |
| Ex2 r6 | NOT DONE / INADEQUATE IMAGE QUALITY / PROXIMAL INTERPHALANGEAL JOINT 3 OF THE HAND / LEFT | 一致 |
| Ex2 r7 | MODERATE-SEVERE; 76-95% … / 2.5 / METACARPOPHALANGEAL JOINT 1 / RIGHT | 一致 |
| Ex2 r8 | SEVERE; PARTIAL OR EQUIVOCAL ANKYLOSIS / 3.5 / MCP JOINT 1 / LEFT | 一致 |
| Ex2 r9 | NOT DONE / INADEQUATE IMAGE QUALITY / MCP JOINT 2 / RIGHT | 一致 |
| Ex2 r10 | MILD-MODERATE; 26-50% … / 1.5 / MCP JOINT 2 / LEFT | 一致 (PDF "26–" 折行) |
| Ex2 r11 | NORMAL / 0 / MCP JOINT 3 / RIGHT | 一致 |
| Ex2 r12 | NOT DONE / AMPUTATION/MISSING ANATOMY/JOINT REPLACEMENT/SURGICAL ALTERATION / MCP JOINT 3 / LEFT | 一致 |
| Ex2 r13 | SEVERE; COMPLETE LOSS OF JOINT SPACE, DISLOCATION WITH EROSION / 3 / MCP JOINT 4 / RIGHT | 一致 (本批修正) |
| Ex2 r14-16 | SEVERE; PARTIAL…/3.5; QUESTIONABLE/0.5; NORMAL/0; MCP JOINT 4 L / 5 R / 5 L | 一致 |
| Ex2 公共列 r1-16 | XYZ / MK / XYZ-002 / SEQ=Row / SGJSNSCR / Sharp/Genant JSN Score / X-RAY / INDEPENDENT ASSESSOR / READER 1 / 4 / WEEK 12 / 2013-08-12 | 一致 |

PDF_TYPO 依据核对 (是否由 PDF 自身确定):
- T-1 r2 MKORRES: 渲染图 p293 r2 "MODERATE- SEVERE;" 在同一行内带空格 (非折行) → PDF 自身印刷差; 同表 r7 同分值 2.5 (p294) 写 "MODERATE-SEVERE;" → 可由 PDF 自身确定. 成立.
- T-2 r3 MKREASND: p293 该格在 "REPLACEMENT/" 后折行至 "SURGICAL ALTERATION" (渲染可见), 是折行歧义而非确证的空格; r12 (p294) 同值单行 "REPLACEMENT/SURGICAL" → 由 PDF 自身确定无空格. KB 值成立; writer 理由 "疑为真空格" 属推测, 不影响结论 (L-1).

## 3. G-TB6 反向溯源 (diff 每条新增/改动行)
| diff 行 | 出处 | 结果 |
|---|---|---|
| assumptions.md `## MK – Description/Overview` | p290 节标题 "MK – Description/Overview" | 结构行, 签字 (CM 先例同格式) |
| assumptions.md 定义句 | p290 "A findings domain that contains physiological and morphological findings related to the system of muscles…" | 逐字 (norm 命中) |
| assumptions.md `## MK – Specification` | p290 "MK – Specification" | 结构行, 签字 |
| assumptions.md "mk.xpt, Musculoskeletal System Findings — Findings. One record per assessment per visit per subject, Tabulation." | p290 | 逐字 |
| assumptions.md `## MK – Assumptions` | p292 "MK – Assumptions" | 结构行, 签字 |
| assumptions.md 删除 "4. The method used to obtain the image is represented in MKMETHOD = "X-RAY"." | PDF Assumptions (p292) 只有 1-3; 该句属 Ex2 叙述 p293 | D2 删除成立; 文本保留于 examples.md:42, 位置 = PDF 原位 ("…first reader." 之后, "The scoring method…" 之前) |
| examples.md:42 插入 MKMETHOD 句 | p293 "The method used to obtain the image is represented in MKMETHOD = "X-RAY"." | 逐字, 位置正确 |
| examples.md:52/53/54/55/56/63 | p293-294 渲染 | 见 G-TB4, 全一致 |
无出处词句: 0.

双向全扫 (含表格原子, 不截断):
- PDF→KB: p290 标题后叙述 + p292 + p293 Ex2 叙述共 41 句, 脚本 `norm(s) in norm(KB)` 未命中 2 条, 均为抽取伪差: (a) 节标题粘连定义句 (定义句单独核命中), (b) assumption 3 PDF 折行 "-- STREFC" (单独核 "--ORREF, --STREFC, --STREFN." 命中). Rows 说明 5 条全命中. 表格原子见 G-TB4 (Ex1 16 行 / Ex2 16 行全一致).
- KB→PDF: MK/examples.md + MK/assumptions.md 全文件非表格行逐句回查 p290/292/293, 唯一未命中 = assumption 3 (同上 "-- STREFC" 折行伪差). 结构/导航行: `# MK — Examples`, `# MK — Assumptions`, `## Example 1/2`, `**mk.xpt**`, `**Rows …:**` 粗体 —— 纯导航/PDF 标签, 签字; 无 KB 自写解释性内容 → 本批无 D6 标注需求 (确认: 文件中无 `KB note` 行, 也无应加而未加的).
- 未纳入: spec 表 p290-291 (含脚注 1) 属 spec.md, 白名单外, 未改 —— 移交 O15 (writer F-2 同).

## 4. 位置 / 5. 无副作用
- 新增内容在 CM 先例位置 (Description/Overview → Specification → Assumptions); 原 1-3 条文本与编号未变.
- `git diff HEAD --stat -- knowledge_base/` 中 MK 以外文件 (BE/TA/TE/TU) 属他批 (TA/assumptions.md 记于 t2_B-TE.md), 非本批.
- MK 改动只在 examples.md (白名单) + assumptions.md (主控授权: Description/spec 首句/Assumptions 小标题 + D2 删第 4 条); 无授权外改动; spec.md 未改.
- 锚点: assumption 4 删除后 grep `domains/MK/assumptions.md#` 与 "assumption 4" 在 knowledge_base/ 无引用; 标题 `# MK — Assumptions` 未变.

## 问题表 (均不阻塞)
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| L-1 T-2 | PDF_TYPO 依据 | writer 称 "疑为真空格"; 实为 "/" 后折行歧义, 应记为折行/空白归一项而非 PDF 印刷错. KB 值正确 | p293 r3 "ANATOMY/JOINT REPLACEMENT/ ⏎ SURGICAL ALTERATION"; p294 r12 "REPLACEMENT/SURGICAL" |
| L-2 Ex2 MKORRES 范围 | 字符口径 | PDF 用 en dash "51–75%" "76–95%" "26–50%", KB 全文件 hyphen (0 个 en dash); 既有口径, census 归一, 未登记为词替换项. 建议主控在全局口径中确认 (非本批改动) | p293 r1 "MODERATE; 51–75%" |
| L-3 p293 Ex2 第 2 段 | 叙述 | "Sharp/Genant and Sharp/van der Heijde" 在 PDF 为蓝色链接样式, `pdftohtml -xml` 未抽到 URI, 无可补可见文本; KB 文字逐字齐全 | p293 |

## R2 recheck
无 (t2_recheck = 0).

## 结论
PASS: census 2 表 OK (608 格 diffs 0), 渲染逐格独立复核 32 行一致; diff 新增/改动 10 处全部有 PDF 出处, 无出处 0; 删除的 assumption 4 确非 PDF Assumptions 内容且原位保留; check_links live docs 42.
