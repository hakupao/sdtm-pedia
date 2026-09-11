#!/usr/bin/env python3
"""生成 runs/c2r_v3/INDEX.md (gitignored, 允许真值)。"""
import json
from pathlib import Path

import sys
RUNS = Path(__file__).resolve().parents[3] / "data/study/st01/eval/runs" / (sys.argv[1] if len(sys.argv) > 1 else "c2r_v3")
QS = json.loads((RUNS.parent / "c2r_v3" / "questions.json").read_text())
QMAP = {**QS["T"], **QS["N"]}

L = ["# C2R V3 原始 run 索引 (gitignored — 含题面真值, 不进 git)", "",
     "> 生成: `scripts/study/c2r_eval/gen_index.py` · 汇总掩码版见 `evidence/checkpoints/c2r_v3_eval.md`",
     "> 文件结构: `_meta` (arm/model/qid/status/attempts/wall_s) + `request` + `response` (完整 AskResponse)",
     "> 命名: `<arm>_<model>_<qid>.json`; arm A = flag OFF (:8010), arm B = `SDTM_RAG_PDF_CONTEXT_ENABLED=true` (:8011)",
     "", "## 题面真值 (qid → 原文)", "", "| qid | 题面 |", "|---|---|"]
for q, t in QMAP.items():
    L.append(f"| {q} | {t} |")

L += ["", "## 原始 run 文件", "",
      "| 文件 | arm | model | qid | status | wall_s | pdf_trigger | pdf_pages | answer 字符数 |",
      "|---|---|---|---|---|---|---|---|---|"]
n = 0
for f in sorted(RUNS.glob("*.json")):
    if f.name == "questions.json":
        continue
    d = json.loads(f.read_text()); m, r = d["_meta"], d.get("response", {})
    pages = r.get("pdf_pages") or []
    pgs = "; ".join("{} p.{}".format(x["pdf"], x["page"]) for x in pages) or "-"
    L.append("| `{}` | {} | {} | {} | {} | {} | {} | {} | {} |".format(
        f.name, m["arm"], m["model_id"], m["qid"], m["status"], m["wall_s"],
        r.get("pdf_trigger"), pgs, len(r.get("answer", "") or "")))
    n += 1
fails = sorted((RUNS / "failures").glob("*.json"))
L += ["", f"合计 {n} 个成功 run + {len(fails)} 个失败 run (`failures/`)。", ""]
if fails:
    L.append("## 失败 run (规则 B: 保留不删)")
    L.append("")
    for f in fails:
        d = json.loads(f.read_text()); m = d["_meta"]
        L.append(f"- `failures/{f.name}` — {m['arm']}/{m['model_id']}/{m['qid']} "
                 f"attempts={json.dumps(m['attempts'], ensure_ascii=False)}")
else:
    L.append("失败 run: 无。")
(RUNS / "INDEX.md").write_text("\n".join(L) + "\n")
print(f"INDEX.md written: {n} runs, {len(fails)} failures")
