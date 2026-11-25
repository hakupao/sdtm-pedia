# FP sample for t1_census_full.md §1: python3 -I .work/10_tier_b_repair/scripts/helpers/fp_sample.py (repo root)
import json, random, re
TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
d = json.load(open(f"{TB}/work/census_full.json"))
cells = [(t, x) for t in d["tables"] for x in t.get("diffs", []) if x["type"] == "CELL"]
random.seed(20261126)
for t, x in random.sample(cells, 20):
    flat = re.sub(r"\s+", "", " ".join(open(f"{TB}/work/pdf_pages/{t['pdf_src']}_p{p:04d}.txt").read() for p in t["pdf_pages"]))
    pin = x["pdf"] is None or re.sub(r"\s+", "", x["pdf"]) in flat
    print(f'{t["file"][15:]}:{x["kb_line"]} r{x["kb_row"]}/{x["pdf_row"]} {x["col"]} kb={(x["kb"] or "")[:45]!r} '
          f'pdf={(x["pdf"] if x["pdf"] is not None else "<no col>")[:45]!r} p{t["pdf_pages"]} pdfval_on_page={pin}')
