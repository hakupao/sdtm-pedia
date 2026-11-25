"""Writes evidence/checkpoints/t1_census_full.md from work/census_full.json (counts/locations only). Run: python3 -I <this> (any cwd)."""
import collections, hashlib, json
TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
d = json.load(open(f"{TB}/work/census_full.json")); man = json.load(open(f"{TB}/work/census_full_manifest.json"))
per = collections.OrderedDict()
for t in d["tables"]:
    e = per.setdefault(t["file"][15:], collections.Counter())
    e["tables"] += 1; e[t["status"]] += 1; e["cells"] += t.get("cells_compared", 0); e["diffs"] += len(t.get("diffs", []))
    e["unp_rows"] += t["n_rows"] if t["status"] == "UNPARSEABLE" else 0; e["dup"] += bool(t.get("kb_duplicate"))
for m in man:
    per.setdefault(m["file"][15:], collections.Counter())
T = collections.Counter()
for v in per.values(): T.update(v)
dt = collections.Counter(x["type"] for t in d["tables"] for x in t.get("diffs", []))
rows = len({(t["file"], t["line"], x.get("kb_line")) for t in d["tables"] for x in t.get("diffs", []) if x["type"] == "CELL"})
ws = sum(t.get("ws_only_cells", 0) for t in d["tables"])
main = ["| 文件 | 表 | OK | DIFF | NO_PDF | 不可机检 (行) | 比对格 | diff 条目 |", "|---|--:|--:|--:|--:|--:|--:|--:|"]
main += [f"| {f} | {v['tables']} | {v['OK'] + v['OK_SUBSET']} | {v['DIFF']} | {v['NO_PDF']} | {v['UNPARSEABLE']} ({v['unp_rows']}) | {v['cells']} | {v['diffs']} |"
         for f, v in sorted(per.items()) if v["tables"]]
notab = [f for f, v in per.items() if not v["tables"]]
po = ["| PDF 页 | 节 | Example | 数据集 | 行数 |", "|---|---|---|---|--:|"] + \
     [f"| {','.join(map(str, p['pages']))} | {p['sec']} | {p['ex']} | {p['ds']} | {p['n_rows']} |" for p in d["pdf_only"]]
pu = ["| PDF 页 | Example | 数据集 | 原因 | 行数 |", "|---|---|---|---|--:|"] + \
     [f"| {','.join(map(str, p['pages']))} | {p['ex']} | {p['ds']} | {p['reason']} | {p['n_rows']} |" for p in d["pdf_unparsed"]]
nop = ["| KB 表 | Example | 数据集 | 行数 |", "|---|---|---|--:|"] + \
      [f"| {t['file'][15:]}:{t['line']} | {t['ex']} | {t['ds']} | {t['n_rows']} |" for t in d["tables"] if t["status"] == "NO_PDF"]
md5 = hashlib.md5(open(f"{TB}/work/census_full.json", "rb").read()).hexdigest()
npdf = len({(t.get("pdf_src"), tuple(t.get("pdf_pages") or [])) for t in d["tables"] if t.get("pdf_pages")}) + len(d["pdf_only"])
json.dump({"totals": dict(T), "diff_types": dict(dt), "rows_with_cell_diff": rows, "ws_only": ws, "md5": md5},
          open(f"{TB}/work/scratch/census_fix/summary.json", "w"), indent=1)
md = f"""# T1 全量只读 census (Q9 扩展) — table_census v2

<!-- chain: E (plans) -->
> 状态: **已完成** (2026-11-26); 执行: `oh-my-claudecode:executor` (opus); 只读 (KB / archive / releases 未动; 真 KB md5 `5ae88550…` 前后一致, 见 `t0_mutation_v3.log`).
> 输出: `work/census_full.json` (md5 `{md5}`), manifest `work/census_full_manifest.json`. 本文件只含计数、位置与少量单元格值, 无 PDF 原文段落.
> 生成: `python3 -I .work/10_tier_b_repair/scripts/helpers/census_md.py`.

## 0. 复跑

```bash
cd /Volumes/DevSSD/Project/sdtm-pedia
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest .work/10_tier_b_repair/work/census_full_manifest.json \\
  --out .work/10_tier_b_repair/work/census_full.json      # 首次运行生成 work/pdf_bbox/ (gitignored); exit 1 = 有 DIFF (预期)
python3 -I .work/10_tier_b_repair/scripts/helpers/fp_sample.py   # §1 误报抽样 (seed 20261126)
```

范围: `domains/*/examples.md` + `domains/*/assumptions.md` (63 域; DI 无页码且无表) + `chapters/*.md` (6) + `model/*.md` (6) = {len(man)} 文件.
页码取 `.work/02_indexing/page_index.json` (域 = section/spec/assumptions/examples 并集), 配对容差 ±3 页 (例: TM 的 page_index 写 p417, 表实在 p415).
整本 PDF (ig34 461 页 / sv20 74 页) 一次解析, PDF_ONLY 全局计算 (避免按单元跑时邻域表的假 PDF_ONLY).

## 1. 总计

| 项 | 数 |
|---|--:|
| KB 表 (markdown) | {T['tables']} |
| 可机检 (Row 列) | {T['tables'] - T['UNPARSEABLE']} = OK {T['OK'] + T['OK_SUBSET']} + DIFF {T['DIFF']} + NO_PDF {T['NO_PDF']} (其中 KB 重复副本 {T['dup']}) |
| 不可机检 (UNPARSEABLE: 无 Row 列, 多为 chapter/model/assumptions 的说明/变量表) | {T['UNPARSEABLE']} 张 / {T['unp_rows']} 行 → 被 T2 触碰时 reviewer 人工逐格 |
| 比对单元格 | {T['cells']} |
| diff 条目 | {T['diffs']} = CELL {dt['CELL']} + HEADER {dt['HEADER']} + ROW_SHAPE {dt.get('ROW_SHAPE', 0)} + PDF 行缺 {dt['PDF_ROW_MISSING']} + KB 行多 {dt['KB_ROW_UNMATCHED']} |
| 有 CELL diff 的 KB 行 | {rows} |
| PDF_ONLY (KB 缺整表) | {len(d['pdf_only'])} |
| PDF_UNPARSED (垂直居中, 人工逐格) | {len(d['pdf_unparsed'])} |

误报抽检: 随机 20 条 CELL diff (`fp_sample.py`, seed 20261126; 输出 `work/scratch/census_fix/fp_sample.txt`).
7 条回 PDF (版面文本 + 词框) 直接核对, 全是真差异: AE:96 AEENDTC (PDF 2018, KB 2013), DM:11 RFXSTDTC, OE:15 OEMETHOD (KB 多 BIOMICROSCOPY),
DS:346 TESTRL (KB 多 "is"), EG:29 EGDTC (KB 2003-04-36), MB:154 MBSPCCND (KB 表头列名不符致空), TR:97 TRTEST (PDF 自身截成 "Diam" → PDF_TYPO 候选);
其余 13 条落在 lane 笔记已判错的表 (PP Ex1 用了 Ex3 数据 ×5, GF Ex1/Ex3 ×6, LB Ex1 ×2), 未逐格复核, 不计入误报率.
直接核对 7 条误报 0 (样本小; 误报率只能说未见, 不给区间).
已知"真但未必要改"的 diff: TR Ex2 PDF 跳 Row 12, KB 连续编号 → `Row` 列 16 条差异 (PDF_TYPO 候选); 折行连接歧义按相等计的格 (ws_only) {ws}.

## 2. 每文件

{chr(10).join(main)}

无表文件 ({len(notab)}): {', '.join(notab)}

## 3. PDF_ONLY (KB 没有对应表)

{chr(10).join(po)}

## 4. NO_PDF (KB 表找不到 PDF 对应) / PDF_UNPARSED (人工逐格)

{chr(10).join(nop)}

{chr(10).join(pu)}

## 5. 与 v1 的关系

- B-PCPP (p275-284): v2 复现 v1 全部 42 处 DIFF (按表+行对照 0 丢失), 粒度细到格 (54 条); v1 的 13 张 OK 表 v2 仍 OK.
- EG / CP / TR / MB 四个 T1 单元: v1 的 DIFF 行 v2 全部保留; 表面"丢失"的 3 处均为表达方式变化 — TR Ex2 v1 的 row 28 "KB 缺行" 现为
  行号对齐 (KB 12-27 ↔ PDF 13-28, `Row` 列 diff); MB:162 v1 的 row 7/8 缺行现为 KB 5/6 ↔ PDF 7/8 行号 diff; MB:229 由 DIFF 变 OK (v1 误配 Ex3 relrec, 见 `t0_mutation.md` §6).
"""
open(f"{TB}/evidence/checkpoints/t1_census_full.md", "w").write(md)
print(dict(T), dict(dt), rows, md5)
