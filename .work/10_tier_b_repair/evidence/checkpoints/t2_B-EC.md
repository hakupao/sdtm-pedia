# T2 B-EC writer checkpoint — attempt 1

- base HEAD: `f22fe6027a04c5efe09c7885f6d472b913bf3b42`
- kb_files: `knowledge_base/domains/EC/examples.md` — md5 before `90525b2374799438952bdf44183e6ae7` (135 行) → after `10c53276d937a10dd789508c4d61422e` (3 行)
- 依据: B-EX review 归属结论 (§6.1.3.3 共享例子归 EX); 本批 notes; dispatch notes "跨文件重复例子" D2.
- PDF 结构核对 (ig34 p101-121 标题扫描): §6.1.3.1 EX p104 / §6.1.3.2 EC p107 / §6.1.3.3 "Exposure/Exposure as Collected Examples" p111-120 (Ex1-8). **无 EC 专属例子** — EC 的全部例子都在共享 §6.1.3.3 中, 无需保留任何 EC-only PDF 内容.

## EC 副本 vs 已提交 EX 副本 逐行 diff (EC 有而 EX 无的行)

脚本: EC 每个非空行 strip 后查是否在 EX/examples.md 行集合中. 不在 EX 的 22 行全部人工核对:

| EC 行 (base) | 内容 | 判定 | 依据 |
|---|---|---|---|
| 1 | `# EC — Examples` | 保留 (标题) | — |
| 3 | "Note: Examples for EX and EC are shared…" | 替换为交叉引用 | 导航句 |
| 32-36 | Ex2 ec.xpt 表头+3 行: 无 VISITNUM 列, VISIT 列 | EC 错 (census DIFF), EX:86-90 已有 VISITNUM=3 | p112 layout 表头含 VISITNUM |
| 40 | Ex3 首段 (缺 "The subject in this example took:") | EC 截断; EX:111 是超集 | p113 |
| 59 | Ex5 段 (缺 "This use of time-point variables is novel…") | EC 截断; EX:192 是超集 | p114-115 |
| 87 | Ex6 Row 2 ECDOSFRM=CAPSULE | EC 错; EX:266 = TABLET, COATED | p116 |
| 88, 90 | Ex6 "3-12 / 14-24 …" 省略行 | KB 自写缩写占位, 非 PDF; EX:267 起有完整行 | p116-117 |
| 92 | "See [EX Examples]… Example 6 for the complete…" | KB 导航 | — |
| 100, 102 | Ex7 Rows 1,3,5 / 2,4 说明 (各缺第二句) | EC 截断; EX:360/362 是超集 | p117-118 |
| 108-115 | Ex7 ec.xpt: 列序 EPOCH 在 VISITNUM 前, EPOCH="VISIT TREATMENT" | EC 错 (census DIFF); EX:368-375 列序 VISITNUM/VISIT/EPOCH, EPOCH=TREATMENT | p118 layout |
| 119 | Ex8 首段 (缺 "Note: This method of data collection design is not consistent with current CDASH standards.") | EC 截断; EX:418 是超集 | p119 |

结论: EC 有而 EX 无的内容全部是 EC 的截断/错值/KB 自写占位或导航; **无 PDF 内容是 EX 缺而 EC 有** → 无需向 EX 报缺. 其余 EC 行在 EX 中逐字存在. EC 缺 Example 4 (EX:148 有).

## 变更清单

| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | EC/examples.md:3 | D2 去重 (整组 §6.1.3.3 例子) | REPLACED | 行 3-135 (Ex1-3,5-8 全部叙述+ec.xpt 表) → 一行 `> See …(../EX/examples.md) for this example set (…§6.1.3.3…)` | 111-120 |
| 2 | (deleted) | census:EC/examples.md:32 (lines 34,35,36) Ex2 | 由 D2 删除处理; 正确值在 EX:86-90 | 缺 VISITNUM → EX 已修 | 112 |
| 3 | (deleted) | census:EC/examples.md:108 (lines 110-115) Ex7 | 由 D2 删除处理; 正确值在 EX:368-375 | EPOCH 列序/值 → EX 已修 | 118 |
| 4 | (deleted) | unparseable EC/examples.md:84 Ex6 | 由 D2 删除; 未改表, 无需逐格 | EX:233 起 Ex6 为保留副本 | 116-117 |

atoms[] = 0, t2_recheck = 0, pdf_only = 0.

## 删除清单 (D2)

| file:line (base) | 原因 | 保留副本位置 |
|---|---|---|
| EC/examples.md:3 | KB 导航 Note, 由新交叉引用替代 | EC/examples.md:3 (新) |
| EC/examples.md:5-22 (Ex1) | D2 跨文件重复 | EX/examples.md:5 起 |
| EC/examples.md:24-36 (Ex2) | D2 重复 + EC 表错 | EX/examples.md:59 起 |
| EC/examples.md:38-53 (Ex3) | D2 重复 + 首段截断 | EX/examples.md:109 起 |
| EC/examples.md:55-70 (Ex5) | D2 重复 + 段截断 | EX/examples.md:165 起 |
| EC/examples.md:72-92 (Ex6) | D2 重复 + Row2 错值 + KB 省略占位行 + 导航句 | EX/examples.md:233 起 |
| EC/examples.md:94-115 (Ex7) | D2 重复 + 表列序/EPOCH 错 + 说明截断 | EX/examples.md:325 起 |
| EC/examples.md:117-135 (Ex8) | D2 重复 + 首段截断 | EX/examples.md:416 起 |

入链检查: `grep -rn "EC/examples" knowledge_base docs web/src` 仅 INDEX.md:60 (文件级) 与 EX/examples.md:3 (文件级), 无锚点链接 → 删除 `## Example N` 标题不断链. `python3 tools/check_links.py` → `live docs: 42` (= 基线).

## PDF_TYPO
无.

## 范围外发现
- O-EC1: `EC/assumptions.md` 缺 §6.1.3.2 Description/Overview 叙述与 spec 首句 ("ec.xpt, Exposure as Collected — Interventions. One record per …", p107 line 19); 文件直接从 Assumptions 1 开始. 非本批 kb_files → 报主控 (O15/O16).
- O-EC2: `EX/examples.md:3` KB note 仍写 `See also [EC Examples](../EC/examples.md)`, 现 EC 已改为指回 EX 的交叉引用 (互指, 非断链). 是否删该句由主控定 (EX 不在本批).

## 触碰过的 unparseable 表
EC/examples.md:84 (Ex6 ec.xpt) — 整表删除 (D2), 未编辑单元格.

## git diff --stat
```
 knowledge_base/domains/EC/examples.md | 134 +---------------------------------
 1 file changed, 1 insertion(+), 133 deletions(-)
```

## attempt 1 续 (主控扩 kb_files: + EC/assumptions.md, EX/examples.md)

- md5: EC/assumptions.md `9468f594bd7880e488628a5353d8ba1a` → `35046d35f91ffbb0f333b126e8dcb631`; EX/examples.md `f5643b21b9dff82d6bef884cb830273a` → `33e7ebcb258e9e5da296a2ba5f4f7484`.

| # | kb_file:line (改后) | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 5 | EC/assumptions.md:3-5 | O-EC1 | INSERTED | `## EC – Description/Overview` + 描述句 (逐字) | 107 |
| 6 | EC/assumptions.md:7-9 | O-EC1 | INSERTED | `## EC – Specification` + spec 首句 "ec.xpt, Exposure as Collected — Interventions. One record per …per mood, Tabulation." (逐字) | 107 |
| 7 | EC/assumptions.md:11 | O-EC1 | INSERTED | `## EC – Assumptions` 标题 (PDF 原标题 p109; 按 CM/SC 惯例分节; 既有 H1 未动) | 109 |
| 8 | EX/examples.md:3 | O-EC2 | REPLACED | KB note 句尾 `See also [EC Examples](…)` → "; EC/examples.md points here." (去链接, 消除互指循环; EX 其余未动) | — |

- EC/assumptions.md 双向扫描 (p109 "EC – Assumptions" 起 – p110): KB→PDF 逐行 norm 后子串匹配, 0 缺; PDF→KB 人工对 1(a-c)/2/3(a i-ii, b-e)/4(a-c)/5(a-b)/6/7(a-b), 全部逐字在 KB, 无遗漏、无 KB 自写内容.
- fp 回归: HEAD 版 3 文件 vs 现版 (其余 KB 相同) 跑 `scripts/fp_match.py --baseline work/fp_baseline.jsonl`: 两边 regress 均 48 条 (全为 HEAD 既有, 页 p011-p039x, 含 p0118_a017 PARTIAL 既有), 新增 0 / hit_target 翻转 0 → EC+EX 回归 0.
- `python3 tools/check_links.py` → live docs: 42 (基线).
- git diff --stat: EC/assumptions.md +10; EC/examples.md 1+/133-; EX/examples.md 1+/1-.
