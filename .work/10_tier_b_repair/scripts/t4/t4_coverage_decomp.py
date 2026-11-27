#!/usr/bin/env python3
"""G-TB3 decomposition: pre-T3 ledger (06 formula 99.02%) -> final ledger strict / mapped, per-row (06 counted per row).
06 formula: covered = EXACT+EQUIVALENT+PARTIAL+MISPLACED; denominator = rows - IE. strict keeps the 06 denominator;
mapped also drops ATOM_ERR/PDF_TYPO/FIGURE_DEFERRED. Rows are compared by position (T3 only rewrote rows in place and
appended at the end).
T4 W3: + U-1 B line (ATOM_ERR+PDF_TYPO counted covered, FIGURE_DEFERRED uncovered; strict denominator) and the content
metric (EXACT+EQUIVALENT over the mapped denominator). Optional argv[1] = ledger to read instead of the working ledger.
Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_coverage_decomp.py [ledger.jsonl]
"""
import collections, json, sys

W = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair/work"
lj = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
pre, now = lj(f"{W}/coverage_ledger.wc.pre_t3.jsonl"), lj(sys.argv[1] if len(sys.argv) > 1 else f"{W}/coverage_ledger.wc.jsonl")
COV, NEW, IE = {"EXACT", "EQUIVALENT", "PARTIAL", "MISPLACED"}, {"ATOM_ERR", "PDF_TYPO", "FIGURE_DEFERRED"}, "INTENTIONAL_EXCLUDE"
g = lambda v: "cov" if v in COV else "new" if v in NEW else "ie" if v == IE else "unc"
assert all(a["pdf_atom_id"] == b["pdf_atom_id"] for a, b in zip(pre, now))
pairs = [(g(a["verdict"]), g(b["verdict"])) for a, b in zip(pre, now)] + [("(appended)", g(b["verdict"])) for b in now[len(pre):]]
c = collections.Counter(p for p in pairs if p[0] != p[1])
num0 = sum(1 for a in pre if g(a["verdict"]) == "cov")
den0 = sum(1 for a in pre if g(a["verdict"]) != "ie")
num1 = sum(1 for b in now if g(b["verdict"]) == "cov")
den_s = sum(1 for b in now if g(b["verdict"]) != "ie")
den_m = sum(1 for b in now if g(b["verdict"]) not in ("ie", "new"))
print(f"pre-T3 (06 formula): {num0}/{den0} = {num0 / den0 * 100:.4f}%")
print(f"final strict       : {num1}/{den_s} = {num1 / den_s * 100:.4f}%")
print(f"final mapped       : {num1}/{den_m} = {num1 / den_m * 100:.4f}%")
num_b = num1 + sum(1 for b in now if b["verdict"] in ("ATOM_ERR", "PDF_TYPO"))
print(f"final U-1 B        : {num_b}/{den_s} = {num_b / den_s * 100:.4f}%  (ATOM_ERR+PDF_TYPO covered, FIGURE_DEFERRED uncovered)")
num_c = sum(1 for b in now if b["verdict"] in ("EXACT", "EQUIVALENT"))
print(f"content EXACT+EQUIV: {num_c}/{den_m} = {num_c / den_m * 100:.4f}%  (mapped denominator)")
print("group transitions (cov=EXACT/EQUIV/PARTIAL/MISPLACED, unc=MISSING/ERROR, new=ATOM_ERR/PDF_TYPO/FIG):")
for k, v in sorted(c.items(), key=lambda x: -x[1]):
    print(f"  {k[0]:>10} -> {k[1]:<4} {v}")
cn = c[("cov", "new")]
print(f"counterfactual strict if the {cn} cov->new rows had stayed covered: {(num1 + cn)}/{den_s} = {(num1 + cn) / den_s * 100:.4f}%")
print("still-counted-as-covered under 06 formula in final ledger:",
      dict(collections.Counter(b["verdict"] for b in now if b["verdict"] in {"PARTIAL", "MISPLACED"})),
      "| uncovered:", dict(collections.Counter(b["verdict"] for b in now if g(b["verdict"]) == "unc")))
