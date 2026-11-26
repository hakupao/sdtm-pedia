# T2 B-MK writer — attempt 1 (2026-11-26)

- base HEAD: `5440dc5510f79e2edfb4a10b61fc4b37df700cb5`
- md5 before: MK/examples.md `f199e776bacd4829ca11b7c46f42fd7a`; MK/assumptions.md `9c2976de33b1ec8f39f34ea094669d18`; MK/spec.md `974cac1f345b3af2213ae4b2a296b5e6` (未改)
- md5 after: MK/examples.md `b8d525432dbb162f33c92238a800ac02`; MK/assumptions.md `0c34aafa1d8b2c8e1ae25a08c5120cda`
- 白名单: `knowledge_base/domains/MK/examples.md`; 主控授权 `MK/assumptions.md` 仅 Description/Overview + spec 首句 (CM/SC 先例, 逐字)
- pdf_ranges 核对 (O20): ig34 p290-294 覆盖完整 MK 节: p290 = §6.3.7.3 标题 + Description/Overview + Specification 首句 + 规格表起; p291 规格表续; p292 Assumptions 1-3 + Ex1 叙述; p293 Ex1 表 + Ex2 叙述 + Ex2 表 r1-6; p294 Ex2 表 r7-16, 随后 §6.3.7.4 NV. 范围充分.
- atoms[] = 0, t2_recheck = 0; census DIFF 表 1 张 (examples.md:49, 6 行).
- 真值: `work/pdf_pages/ig34_p0290-0294.txt` + pdftoppm 渲染 p293/p294 (110 dpi 全页 + p293 Ex2 表 250 dpi 放大).

## 变更清单

| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | MK/assumptions.md:3-5 | R3 新增 (Description/Overview) | INSERTED | 新增 `## MK – Description/Overview` + 定义句 (findings domain … muscles, tendons, ligaments …) | p290 |
| 2 | MK/assumptions.md:7-9 | R3 新增 (spec 首句) | INSERTED | 新增 `## MK – Specification` + "mk.xpt, Musculoskeletal System Findings — Findings. One record per assessment per visit per subject, Tabulation." | p290 |
| 3 | MK/assumptions.md:11 | 结构 (CM 先例) | INSERTED | 新增 `## MK – Assumptions` 小标题 (PDF p292 原标题), 分隔原 1-3 条; 原 `# MK — Assumptions` 不动 | p292 |
| 4 | MK/examples.md:42 | R3 新增 (Ex2 叙述漏句) | INSERTED | 在 "…performed by the first reader." 后补 PDF 句 "The method used to obtain the image is represented in MKMETHOD = "X-RAY"." | p293 |
| 5 | MK/examples.md:52 | census:MK/examples.md:52:2:MKORRES | REPLACED | "…51-75% LOSS…" → "MODERATE-SEVERE; 76-95% LOSS OF JOINT SPACE" (连字符空格见 T-1) | p293 |
| 6 | MK/examples.md:53 | census:MK/examples.md:53:3:MKLOC | REPLACED | "PROXIMAL INTERPHALANGEAL JOINT 2" → + " OF THE HAND"; 同行 MKREASND "REPLACEMENT/ SURGICAL" → "REPLACEMENT/SURGICAL" (T-2) | p293 |
| 7 | MK/examples.md:54 | census:MK/examples.md:54:4:MKLOC | REPLACED | "INTERPHALANGEAL JOINT 2 OF THE HAND" → 前加 "PROXIMAL " | p293 |
| 8 | MK/examples.md:55 | census:MK/examples.md:55:5:MKLOC | REPLACED | "PROXIMAL INTERPHALANGEAL JOINT 3" → + " OF THE HAND" | p293 |
| 9 | MK/examples.md:56 | census:MK/examples.md:56:6:MKLOC | REPLACED | "PROXIMAL INTERPHALANGEAL JOINT 3" → + " OF THE HAND" | p293 |
| 10 | MK/examples.md:63 | census:MK/examples.md:63:13:MKORRES | REPLACED | "SEVERE; LOSS OF JOINT SPACE, DISLOCATION, EROSION" → "SEVERE; COMPLETE LOSS OF JOINT SPACE, DISLOCATION WITH EROSION" | p294 |

atoms 覆盖: atoms[]=0 (无原子行). census: 唯一 DIFF 表 examples.md:49 的 kb_lines_with_diff 52/53/54/55/56/63 全部处理 (#5-#10). pdf_only = 0, pdf_unparsed = 0, unparseable = 0.

新增 atom 清单 (R3 叙述/结构): #1, #2, #3, #4.

## PDF_TYPO 清单

| T# | 位置 | PDF 原样 | KB 写法 | 依据 |
|---|---|---|---|---|
| T-1 | Ex2 r2 MKORRES (p293) | "MODERATE- SEVERE;" (连字符后有空格; 渲染图同一行可见, 非折行) | "MODERATE-SEVERE;" | 同表 r7 同分值 2.5 写 "MODERATE-SEVERE;" (p294), 可由 PDF 自身确定 |
| T-2 | Ex2 r3 MKREASND (p293) | "REPLACEMENT/ SURGICAL" (疑为真空格: 同宽列 r12 未在 "/" 后断行, 说明 "/" 后无断点, r3 断行处应有空格) | "REPLACEMENT/SURGICAL" | 同表 r12 同值无空格 (p294), 可由 PDF 自身确定; 原 KB 本来就带空格, census 判 ws_only, 不影响 |

范围/字符口径: PDF 范围用 en dash ("51–75%", "76–95%", "26–50%"); KB 全表一致用 hyphen, census 已归一; 本批新改格沿用文件内 hyphen 口径, 未改动其余行的 dash.

## 预期 fp/census 回归 (由 PDF_TYPO 修正引起)

- 实跑 `python3 .work/10_tier_b_repair/scripts/table_census.py --pages ig34:290-294 --kb knowledge_base/domains/MK/examples.md --out <scratch>/census.json` → 2 表 OK, 608 格, diffs 0, GREEN (Ex2 ws_only_cells=1, 即 T-1/T-2 类空白差).
- 实跑 `python3 .work/10_tier_b_repair/scripts/fp_match.py --scope all --out <scratch>/fp.jsonl --baseline work/fp_baseline.jsonl --regress-out <scratch>/regress.jsonl` → MK 节 (p290-294) 112 原子无 miss, regress 文件中无 p0290-p0294/MK 条目; 整体 RED 的 48 条 REGRESS 均为其它页 (如 §6.4.2 p363-364, 工作树中他批未提交改动), 与本批无关.
- 结论: T-1/T-2 预期 fp 回归 = 0 (fp/census 都做空白归一). 若 reviewer 用不归一空白的逐字比对, 会在 r2 MKORRES、r3 MKREASND 看到 1 空格差, 属已登记 PDF_TYPO.

## 双向全扫 (p290-294)

- PDF→KB: p290 标题行 / Description / spec 首句 → assumptions.md (#1-#3); 规格表 p290-291 属 spec.md (白名单外), 仅做变量清单比对: 42 变量 STUDYID…MKRFTDTC 顺序完全一致, 未逐格核 CDISC Notes. p292 Assumptions 1-3 = assumptions.md 1-3 逐字. Ex1 3 段叙述 + 3 条 Rows 说明 = examples.md:5-13 逐字; Ex1 表 16 行 × 18 列对渲染逐格一致. Ex2 2 段叙述 (缺 1 句已补 #4) + 2 条 Rows 说明 = :38-45; Ex2 表 16 行 × 20 列对渲染逐格 (改后) 一致.
- KB→PDF: examples.md 全文件每句/每行均在 p292-294 找到出处; 标题 `# MK — Examples` / `## Example n` / `**mk.xpt**` / `**Rows …:**` 粗体为纯导航. assumptions.md 第 4 条无 PDF Assumptions 对应 → 见范围外 F-1.

## 范围外发现

- F-1 `knowledge_base/domains/MK/assumptions.md` 第 4 条 "The method used to obtain the image is represented in MKMETHOD = "X-RAY"." — PDF Assumptions 只有 1-3 (p292); 此句是 Ex2 叙述 (p293) 被挪到 Assumptions 并编号. 本批已在 examples.md:42 原位补回; assumptions.md 第 4 条不在授权范围 (仅 Description/spec), 未删. 建议主控授权作为 RELOCATE 源行删除 (或 D2 删扩写).
- F-2 `MK/spec.md` 顶部 "> Class: Findings | Structure: …" 为 KB 摘要行 (与 PDF 首句不矛盾); 规格表 CDISC Notes 未逐格核 (白名单外).

## 删除清单

无 (仅 VALUE_DIFF 旧值替换).

## 触碰过的 unparseable 表

无.

## git diff --stat

```
 knowledge_base/domains/MK/assumptions.md | 10 ++++++++++
 knowledge_base/domains/MK/examples.md    | 14 +++++++-------
 2 files changed, 17 insertions(+), 7 deletions(-)
```

## attempt 1 续 (主控裁定后, 2026-11-26)

- `## MK – Assumptions` 标题: 主控接受 (CM 先例).
- F-1 → D2 删除 MK/assumptions.md 第 4 条 (原 :18-19, 空行 + "4. The method used to obtain the image … MKMETHOD = "X-RAY".").
- F-2 → 归 O15 spec 扫描, 本批不动 spec.md.

### 删除清单

| # | file:line (删前) | 内容摘要 | 原因 | 保留副本位置 |
|---|---|---|---|---|
| D-1 | MK/assumptions.md:18-19 | 第 4 条 "The method used to obtain the image is represented in MKMETHOD = "X-RAY"." | D2: PDF Assumptions 只有 1-3 (p292); 该句属 Ex2 叙述 (p293), 被挪入并编号 | MK/examples.md:42 (PDF 原位, 本批 #4 已补) |

- 锚点/编号影响: 第 4 条是末条, 无后续编号; grep `knowledge_base/` 无指向 "assumption 4" 的引用, 文件仅被 INDEX.md:96 整文件链接, 无锚点影响.
- md5 after: MK/assumptions.md `574bffa734b6e8d6025f59a647206ddd`; examples.md `b8d525432dbb162f33c92238a800ac02` (不变).
- 重跑: census (`table_census.py --pages ig34:290-294 --kb knowledge_base/domains/MK/examples.md`) 2 表 608 格 diffs 0 GREEN; fp_match (`--scope all --baseline work/fp_baseline.jsonl`) MK 节 112 原子 hit True 71 / None 41 / miss 0, regress 48 条中 p290-294/MK 为 0; `python3 tools/check_links.py` → live docs: 42.
- git diff --stat: assumptions.md 12 (+10/-2), examples.md 14 (+7/-7); 2 files, 17 insertions, 9 deletions.
