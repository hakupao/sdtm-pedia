#!/usr/bin/env python3
"""S0 probe: for atoms given on argv, best KB line among candidate files (baseline target + its domain dir),
word-level diff atom vs KB line, and whether each side's diff tokens are in PDF pages p-1..p+1."""
import sys, json, glob, os, difflib
TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"; ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
sys.path.insert(0, f"{TB}/scripts")
from fp_match import norm, norm_pdf, lj
A = {a["atom_id"]: a for a in lj(f"{TB}/work/pdf_atoms.jsonl")}
B = {r["atom_id"]: r for r in lj(os.environ.get("FP_BASE", f"{TB}/work/fp_baseline.jsonl"))}
def pdf(p):
    return norm_pdf("\n".join(open(f, encoding="utf-8").read() for q in (p-1, p, p+1)
                    for f in [f"{TB}/work/pdf_pages/ig34_p{q:04d}.txt"] if os.path.exists(f)))
for i in sys.argv[1:]:
    a = A[i]; v = norm(a["verbatim"]); P = pdf(a["page"]); bt = B[i]["hit_target"]
    files = sorted(glob.glob(f"{ROOT}/{os.path.dirname(bt)}/*.md"))
    best = max(((difflib.SequenceMatcher(None, v, norm(l), autojunk=False).ratio(), f, n+1, l)
                for f in files for n, l in enumerate(open(f, encoding="utf-8").read().splitlines()) if len(l.strip()) > 20))
    kl = norm(best[3]); aw, kw = v.split(), kl.split()
    diff = [(" ".join(aw[a1:a2]), " ".join(kw[b1:b2])) for t, a1, a2, b1, b2 in
            difflib.SequenceMatcher(None, aw, kw, autojunk=False).get_opcodes() if t != "equal"]
    print(json.dumps(dict(atom_id=i, page=a["page"], base=bt, best=f"{os.path.relpath(best[1], ROOT)}:{best[2]}", ratio=round(best[0], 3),
        atom_in_pdf=v in P, v_in_bestfile=v in norm(open(best[1], encoding="utf-8").read()),
        diff=[(x, y, (x in P) if x else None, (y in P) if y else None) for x, y in diff[:8]]), ensure_ascii=False))
