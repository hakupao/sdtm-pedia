#!/usr/bin/env python3
"""T0.3 PDF page cache: pdftotext -layout once per PDF, split on form feed -> work/pdf_pages/{ig34,sv20}_pNNNN.txt
(gitignored: CDISC copyright). Asserts page counts 461 / 74, then spot-checks page alignment: for each sample page,
how many of that page's atoms (pdf_atoms.jsonl, non-FIGURE) are verbatim (normalized) on page p-1 / p / p+1.
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t0_pdf_pages.py
"""
import collections, json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fp_match import norm  # noqa: E402

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
W = f"{ROOT}/.work/10_tier_b_repair/work"
OUT = f"{W}/pdf_pages"
PDFS = [("ig34", f"{ROOT}/source/cdisc/SDTMIG v3.4 (no header footer).pdf", 461),
        ("sv20", f"{ROOT}/source/cdisc/SDTM_v2.0.pdf", 74)]
SAMPLE = [("ig34", 1), ("ig34", 278), ("ig34", 461), ("sv20", 1), ("sv20", 30), ("sv20", 74)]

os.makedirs(OUT, exist_ok=True)
for tag, pdf, n in PDFS:
    pages = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True, check=True).stdout.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    assert len(pages) == n, (tag, len(pages), n)
    for i, p in enumerate(pages, 1):
        with open(f"{OUT}/{tag}_p{i:04d}.txt", "w", encoding="utf-8") as f:
            f.write(p)
    print(f"{tag}: {len(pages)} pages (expected {n})")

A = collections.defaultdict(list)
for l in open(f"{W}/pdf_atoms.jsonl", encoding="utf-8"):
    a = json.loads(l)
    A[(a["atom_id"][:4], a["page"])].append(a)
def page(t, p):
    fp = f"{OUT}/{t}_p{p:04d}.txt"
    return norm(open(fp, encoding="utf-8").read()) if os.path.exists(fp) else ""
for t, p in SAMPLE:
    at = [a for a in A[(t, p)] if a["atom_type"] != "FIGURE"]
    hits = {q: sum(1 for a in at if norm(a["verbatim"]) in page(t, q)) for q in (p - 1, p, p + 1)}
    print(f"spot {t} p{p}: atoms={len(at)} hits p-1/p/p+1 = {hits[p - 1]}/{hits[p]}/{hits[p + 1]}")
