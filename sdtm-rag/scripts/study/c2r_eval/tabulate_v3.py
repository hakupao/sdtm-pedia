#!/usr/bin/env python3
"""C2R V3 汇总 (零 LLM, 纯确定性). 只读 runs/c2r_v3/*.json, 输出掩码安全的表.

不打印题面、不打印答案正文, 只打印 arm/model/qid/规则/页号/计数/长度/墙钟/布尔标志。
"""
import json, re
from pathlib import Path

import sys
RUNS = Path(__file__).resolve().parents[3] / "data/study/st01/eval/runs" / (sys.argv[1] if len(sys.argv) > 1 else "c2r_v3")
EXPECT_MODEL = {"opus-5": "claude-opus-5", "gpt-terra": "gpt-5.6-terra", "gpt-sol": "gpt-5.6-sol"}
rows = []
for f in sorted(RUNS.glob("*.json")):
    if f.name == "questions.json":
        continue
    d = json.loads(f.read_text())
    m, r = d["_meta"], d.get("response", {})
    ans = r.get("answer", "") or ""
    pages = r.get("pdf_pages") or []
    rows.append({
        "file": f.name, "arm": m["arm"], "model": m["model_id"], "qid": m["qid"],
        "status": m["status"], "wall": m["wall_s"],
        "trigger": r.get("pdf_trigger"),
        "pages": ";".join(f"{p['pdf']} p.{p['page']}" for p in pages) or "-",
        "npages": len(pages),
        "corpus": r.get("routed_corpus"), "model_used": r.get("model_used"),
        "model_ok": EXPECT_MODEL.get(m["model_id"], "?") in (r.get("model_used") or ""),
        "trunc": r.get("truncated"), "cont": r.get("continue_rounds"),
        "cont_err": r.get("continue_error"),
        "len": len(ans),
        "visual": "画面目視判読" in ans,
        "cite": bool(re.search(r"\[Source:", ans)),
        "nsrc": len(r.get("sources") or []),
        "ptok": (r.get("usage") or {}).get("prompt_tokens"),
    })

def dump(title, rs, cols):
    print(f"\n### {title}")
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join("---" for _ in cols) + "|")
    for x in rs:
        print("| " + " | ".join(str(x[c]) for c in cols) + " |")

T = [r for r in rows if r["qid"].startswith("T")]
N = [r for r in rows if r["qid"].startswith("N")]
dump("N 组 (arm B, opus-5) — 期待 trigger 全 null",
     sorted(N, key=lambda r: r["qid"]),
     ["qid", "arm", "model", "trigger", "npages", "corpus", "nsrc", "len", "wall"])
dump("T 组 arm B — 触发 / 页",
     sorted([r for r in T if r["arm"] == "B"], key=lambda r: (r["qid"], r["model"])),
     ["qid", "model", "trigger", "npages", "pages", "corpus", "visual", "cite", "len", "wall"])
dump("T 组 A vs B — 长度 / 墙钟",
     sorted(T, key=lambda r: (r["qid"], r["model"], r["arm"])),
     ["qid", "model", "arm", "len", "wall", "ptok", "visual", "cite", "trunc", "cont", "model_ok"])
print("\n### 异常汇总")
bad = [r for r in rows if r["status"] != 200 or not r["model_ok"] or r["cont_err"]]
print("无" if not bad else "\n".join(
    f"- {r['file']}: status={r['status']} model_used={r['model_used']} cont_err={r['cont_err']}" for r in bad))
print(f"\n总记录 {len(rows)} (T {len(T)} / N {len(N)}); failures/ 目录 "
      f"{len(list((RUNS/'failures').glob('*.json')))} 个")
