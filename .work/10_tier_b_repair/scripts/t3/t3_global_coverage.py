#!/usr/bin/env python3
"""G-TB3 global coverage, 06 formula (archive p6_t5_nonprose_update_report.md):
  coverage = (EXACT + EQUIVALENT + PARTIAL + MISPLACED) / (rows - INTENTIONAL_EXCLUDE), counted per ledger row.
New T3 classes: 'strict' counts ATOM_ERR/PDF_TYPO/FIGURE_DEFERRED as uncovered (in denominator, not numerator);
'mapped' excludes them from the denominator like IE (06 had no such classes). Also reports per-id (last row wins)
variants because the ledger has 11 duplicated ids. stock t3_recompute logic is not touched.
Usage: python3 -I .work/10_tier_b_repair/scripts/t3/t3_global_coverage.py <ledger.jsonl> [...]
"""
import collections, json, sys

COVER = {"EXACT", "EQUIVALENT", "PARTIAL", "MISPLACED"}
NEW = {"ATOM_ERR", "PDF_TYPO", "FIGURE_DEFERRED"}

def rate(vs):
    c = collections.Counter(vs)
    n, ie, new = sum(c.values()), c["INTENTIONAL_EXCLUDE"], sum(c[k] for k in NEW)
    cov = sum(c[k] for k in COVER)
    strict = cov / (n - ie)
    mapped = cov / (n - ie - new)
    return c, n, ie, new, cov, strict, mapped

for p in sys.argv[1:]:
    rows = [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
    for label, vs in (("per-row", [r["verdict"] for r in rows]),
                      ("per-id", list({r["pdf_atom_id"]: r["verdict"] for r in rows}.values()))):
        c, n, ie, new, cov, s, m = rate(vs)
        print(f"{p.split('/')[-1]} [{label}] rows={n} IE={ie} new={new} covered={cov} "
              f"strict={cov}/{n - ie}={s * 100:.4f}% mapped={cov}/{n - ie - new}={m * 100:.4f}% "
              f"MISSING+ERROR={c['MISSING'] + c['ERROR']} dist={dict(sorted(c.items()))}")
