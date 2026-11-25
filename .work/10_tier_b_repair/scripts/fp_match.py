#!/usr/bin/env python3
"""T0.3b fingerprint matcher: is each PDF atom's verbatim (normalized) present in the KB?
Per atom: hit in its target files (ledger md_atom_ids files ∪ section md_target_files), hit anywhere in KB,
and whether the verbatim is on its PDF page (page p ∪ p+1, de-hyphenated) — the last is an ATOM_ERR signal.
Red/green: with --baseline, exit 1 if any atom that hit its target in the baseline no longer does (regression).
Usage (repo root):
  python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out .work/10_tier_b_repair/work/fp_baseline.jsonl
  python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root <copy> --out <new.jsonl> \
      --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out <regress.jsonl>
Never writes knowledge_base/ or archive/.
"""
import argparse, collections, glob, html, json, os, re, sys, unicodedata

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
TB = f"{ROOT}/.work/10_tier_b_repair"
W = f"{TB}/work"

_TR = str.maketrans({"‘": "'", "’": "'", "‚": "'", "′": "'", "“": '"', "”": '"', "„": '"', "″": '"',
                     "–": "-", "—": "-", "‐": "-", "‑": "-", "−": "-", "•": " ", "▪": " ", "◦": " ",
                     " ": " ", "\t": " "})

def norm(s):
    """t0_inventory.norm() + tabs/nbsp, bold/italic/code, curly quotes/dashes, table pipes, links, <br>, entities."""
    s = html.unescape(unicodedata.normalize("NFKC", s)).translate(_TR)
    s = re.sub(r"<br\s*/?>", " ", s, flags=re.I)
    s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)          # [text](url) -> text
    s = re.sub(r"[*_`|>#\\~]", " ", s)                         # bold/italic/code/pipes/quote/heading/escapes
    return re.sub(r"\s+", " ", s).strip().lower()

def norm_pdf(s):
    s = re.sub(r"(\w)-\n\s*(\w)", r"\1-\2", s)                 # keep hyphen, join wrapped hyphenated tokens
    return norm(s)

def lj(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb-root", default=f"{ROOT}/knowledge_base")
    ap.add_argument("--atoms", default=f"{W}/pdf_atoms.jsonl")
    ap.add_argument("--ledger", default=f"{W}/coverage_ledger.wc.jsonl")
    ap.add_argument("--md-atoms", default=f"{W}/md_atoms.jsonl")
    ap.add_argument("--sections", default=f"{W}/section_coverage.wc.jsonl", help="for md_target_files")
    ap.add_argument("--scope", default=f"{TB}/inventory.jsonl", help="sections to check; 'all' = every section")
    ap.add_argument("--pdf-pages", default=f"{W}/pdf_pages")
    ap.add_argument("--out", required=True)
    ap.add_argument("--baseline")
    ap.add_argument("--regress-out")
    a = ap.parse_args()
    kb_root = os.path.abspath(a.kb_root)
    for p in (a.out, a.regress_out or ""):
        if p and (os.path.abspath(p).startswith(f"{ROOT}/archive") or os.path.abspath(p).startswith(f"{ROOT}/knowledge_base")):
            sys.exit(f"refuse to write {p}")

    # KB files keyed by path relative to the KB root's parent, i.e. "knowledge_base/..." (matches md_atoms 'file')
    kb = {}
    for p in glob.glob(f"{kb_root}/**/*.md", recursive=True):
        kb["knowledge_base/" + os.path.relpath(p, kb_root)] = norm(open(p, encoding="utf-8").read())
    kb_all = "\n".join(kb.values())

    sec_targets = {(r["source"], r["section_key"]): r.get("md_target_files") or [] for r in lj(a.sections)}
    scope = None if a.scope == "all" else {(r["source"], r["section_key"]) for r in lj(a.scope)} | \
        {("ig34", "§6.3.5.9.3 Relating PP Records to PC Records")}
    ledger = {e["pdf_atom_id"]: e for e in lj(a.ledger)}
    md_file = {m["atom_id"]: m.get("file", "") for m in lj(a.md_atoms)}
    page_cache = {}
    def page(src, p):
        if (src, p) not in page_cache:
            fp = f"{a.pdf_pages}/{src}_p{p:04d}.txt"
            page_cache[(src, p)] = open(fp, encoding="utf-8").read() if os.path.exists(fp) else ""
        return page_cache[(src, p)]

    out, pair_cache = [], {}
    for at in lj(a.atoms):
        src = at["atom_id"].split("_")[0]
        key = (src, at["parent_section"])
        if at["atom_type"] == "HEADING" or (scope is not None and key not in scope):
            continue
        e = ledger.get(at["atom_id"]) or {}
        tg = sorted({md_file.get(m, "") for m in e.get("md_atom_ids", [])} - {""} | set(sec_targets.get(key, [])))
        v = norm(at["verbatim"])
        hit_t = next((f for f in tg if v and v in kb.get(f, "")), None)
        hit_any = hit_t or (next((f for f, t in kb.items() if v in t), None) if v and v in kb_all else None)
        pg = at.get("page")
        if pg is not None and (src, pg) not in pair_cache:
            pair_cache[(src, pg)] = norm_pdf(page(src, pg) + "\n" + page(src, pg + 1))
        in_pdf = bool(v) and pg is not None and v in pair_cache[(src, pg)]
        out.append({"atom_id": at["atom_id"], "source": src, "section_key": at["parent_section"],
                    "atom_type": at["atom_type"], "verdict": e.get("verdict", "MISSING"), "targets": tg,
                    "hit_target": hit_t, "hit_any": hit_any, "in_pdf_page": in_pdf})
    with open(a.out, "w", encoding="utf-8") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    C = collections.Counter
    print(f"atoms checked: {len(out)}  kb files: {len(kb)}  kb_root: {kb_root}")
    print("hit_target:", sum(1 for r in out if r["hit_target"]), " hit_any:", sum(1 for r in out if r["hit_any"]),
          " absent:", sum(1 for r in out if not r["hit_any"]), " in_pdf_page:", sum(r["in_pdf_page"] for r in out))
    print("hit_target by ledger verdict:", dict(C(r["verdict"] for r in out if r["hit_target"])))
    rc = 0
    if a.baseline:
        base = {r["atom_id"]: r for r in lj(a.baseline)}
        cur = {r["atom_id"]: r for r in out}
        reg = [cur[i] for i in cur if base.get(i, {}).get("hit_target") and not cur[i]["hit_target"]]
        new = [i for i in cur if cur[i]["hit_target"] and not base.get(i, {}).get("hit_target")]
        print(f"BASELINE {a.baseline}: regressions={len(reg)} new_hits={len(new)}")
        for r in reg[:30]:
            print("  REGRESS", r["atom_id"], r["verdict"], r["section_key"][:60])
        if a.regress_out:
            with open(a.regress_out, "w", encoding="utf-8") as f:
                for r in reg:
                    f.write(json.dumps({"atom_id": r["atom_id"], "verdict": r["verdict"]}) + "\n")
        rc = 1 if reg else 0
        print("RESULT:", "RED" if rc else "GREEN")
    sys.exit(rc)

if __name__ == "__main__":
    main()
