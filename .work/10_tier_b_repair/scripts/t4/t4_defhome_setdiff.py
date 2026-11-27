#!/usr/bin/env python3
"""R4 / R0 set diff of sdtm-rag _model_defhome between two KB roots (read-only; same rule as rag probe defhome_rules.py).
Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_defhome_setdiff.py <old_kb_root> <new_kb_root>"""
import re, sys
from pathlib import Path
from collections import defaultdict
def scan(K):
    t = defaultdict(set)
    for f in sorted((Path(K) / 'model').glob('*.md')):
        for raw in f.read_text(encoding='utf-8').splitlines():
            inner = [c.strip() for c in raw.split('|')][1:-1] if '|' in raw else []
            if len(inner) != 6: continue
            num, var, *_, notes = inner
            if not num.isdigit() or not re.fullmatch(r"(?:--)?[A-Z][A-Z0-9]*", var) or not notes or var.startswith('--'): continue
            t[var].add(f.name[:2])
    return t
def R0(fs): return sorted(fs)[0] if len(fs) == 1 else None
def R4(fs):
    if '02' in fs: return '02'
    rest = fs - {'06'} if len(fs) > 1 else fs
    return sorted(rest)[0] if len(rest) == 1 else None
o, n = scan(sys.argv[1]), scan(sys.argv[2])
for lab, R in (('R0', R0), ('R4', R4)):
    a = {v: R(f) for v, f in o.items() if R(f)}; b = {v: R(f) for v, f in n.items() if R(f)}
    print(f"{lab}: old {len(a)} new {len(b)} | added {dict(sorted((k, b[k]) for k in b.keys() - a.keys()))} | removed {sorted(a.keys() - b.keys())} | changed {dict(sorted((k, (a[k], b[k])) for k in a.keys() & b.keys() if a[k] != b[k]))}")
