#!/usr/bin/env python3
"""T4 W3 (主控决定 3): the 14 CE p153 atoms whose rule became 'T1-two-agent+T2-rework' after the U-9a CRF glyph change.
Per atom: the B-CE table block named by t3_writeback (t1_kb_loc_check.block) in the current KB; every alnum token of
norm(atom verbatim) must occur in that block (CRF glyphs ○/□/[ ]/( ) carry no alnum token). Also reports the 302ec4c kb_loc
line vs its current best line. The extractor renders the CRF option glyph as a lone letter 'o' at the start of a cell
('| o Fall |'); that token is not content: it is checked as "the block carries a CRF glyph ○/□" instead. Read-only. Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_ce_p153_check.py
"""
import json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "t3"))
from t3_common import ROOT, W, lj, norm
A = {x["atom_id"]: x for x in lj(f"{W}/pdf_atoms.jsonl")}
D = json.load(open(f"{W}/t3_writeback_decisions.json"))
ids = sorted(i for i, d in D.items() if i.startswith("ig34_p0153_") and d["rule"] == "T1-two-agent+T2-rework")
TOK = lambda s: re.findall(r"[a-z0-9]+", norm(s))
bad = []
for i in ids:
    st = D[i]["evidence"]["t1_kb_loc_check"]
    f, hn = st["head_line"].rsplit(":", 1)
    L = open(f"{ROOT}/{f}", encoding="utf-8").read().splitlines()
    lo, hi = st["block"]
    blk = set(TOK("\n".join(L[lo - 1:hi])))
    v = re.sub(r"(^|\|)\s*o\s+", r"\1 ", A[i]["verbatim"])          # leading CRF glyph rendered as 'o'
    glyph = v != A[i]["verbatim"]
    gl_ok = not glyph or any(g in "\n".join(L[lo - 1:hi]) for g in "○□")
    miss = [t for t in TOK(v) if t not in blk] + ([] if gl_ok else ["<CRF glyph ○/□>"])
    ok = not miss
    bad += [] if ok else [i]
    print(f"{i}\t{'OK' if ok else 'MISS'}\tblock {f.split('knowledge_base/')[1]}:{lo}-{hi}\tbest {hn}\tfix {st['fix_row'].split('/')[-1]} ({st['batch']}, review {st['review_status']})\t"
          f"tokens {len(TOK(v))} glyph {'○/□ ok' if glyph and gl_ok else '-' if not glyph else 'MISSING'} missing {miss}\tatom {A[i]['verbatim'][:70]!r}")
print(f"atoms {len(ids)}; all tokens in B-CE block: {len(ids) - len(bad)}; missing: {bad}")
sys.exit(1 if bad or len(ids) != 14 else 0)
