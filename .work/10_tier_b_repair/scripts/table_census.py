#!/usr/bin/env python3
"""T0.3b table census: KB markdown tables vs PDF page text (pdftotext -layout), row by row, cell by cell.
PDF side: a table = 'Row <VAR> ...' header (+ wrapped header lines) followed by records; a record starts with a
row number at column 0 and owns the indented continuation lines below it (wrapped cells). Tables broken by a page
break or by a repeated header are merged when the header is identical and the row number continues (+1).
Compare: KB table <-> PDF table paired one-to-one by header + best row agreement; rows keyed by the Row cell.
Per row, KB non-empty cells are tokenized and compared to the PDF record's tokens (strict, case-sensitive;
only NFKC / quote / dash variants unified). Single-line record under a single-line header: tokens placed into header
columns by x offset and compared cell by cell incl. empty cells ('columns'); otherwise exact token order ('order');
wrapped records: token multiset, PDF tokens split at a line-wrap after '-' or '_' re-joined ('multiset'). In
'order'/'multiset' modes empty cells are invisible, so a value moved into an empty neighbour cell is not detected and
swaps within a wrapped record are not detected (limitation; reviewer covers those rows manually).
Status per KB table: OK | OK_SUBSET (KB duplicate showing only some PDF rows, all equal) | DIFF | NO_PDF (no PDF table in range pairs with it) | UNPARSEABLE (no Row column).
PDF tables left unpaired are reported as PDF_ONLY; PDF tables the parser cannot read (vertically centred cells,
no record lines) are listed as PDF_UNPARSED -> manual cell-by-cell census by the reviewer (PLAN G-TB4). Exit 1 if any DIFF / PDF_ONLY (or, with --baseline, if the
report differs from the baseline report).
Usage (repo root):
  python3 -I .work/10_tier_b_repair/scripts/table_census.py --pages ig34:275-284 \
     --kb knowledge_base/domains/PC/examples.md knowledge_base/domains/PP/examples.md \
          knowledge_base/domains/PC/assumptions.md --out .work/10_tier_b_repair/work/census_BPCPP.json
"""
import argparse, collections, json, os, re, sys, unicodedata

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
W = f"{ROOT}/.work/10_tier_b_repair/work"
_TR = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-", "‐": "-", "‑": "-",
                     "−": "-", " ": " "})
FOOTER = re.compile(r"^(© \d{4} Clinical Data Interchange Standards Consortium|\d{4}-\d{2}-\d{2}\s*$)")
HEADER = re.compile(r"^\s{0,3}Row\s+[A-Z]")
RECORD = re.compile(r"^\s{0,3}(\d+)\s+\S")

def clean(s):
    return unicodedata.normalize("NFKC", s).translate(_TR)

def kb_cell(c):
    c = re.sub(r"<br\s*/?>", " ", c, flags=re.I)
    c = re.sub(r"\*\*|`", "", c).replace("\\|", "|")
    return clean(c).strip()

# ── PDF side ──────────────────────────────────────────────────────────────────
def pdf_lines(pages_dir, src, lo, hi):
    out = []  # (page, text)
    for p in range(lo, hi + 1):
        for ln in open(f"{pages_dir}/{src}_p{p:04d}.txt", encoding="utf-8").read().split("\n"):
            if FOOTER.match(ln.strip()):
                continue
            out.append((p, clean(ln.rstrip())))
    return out

def parse_pdf_tables(lines):
    tables, cur, rec, gap_text = [], None, None, False
    def close():
        nonlocal cur, rec
        if cur and (cur["rows"] or cur["hdr_lines"]):
            tables.append(cur)                         # header-only tables kept -> reported as PDF_UNPARSED
        cur, rec = None, None
    for p, ln in lines:
        if not ln.strip():
            if cur and cur["rows"]:
                cur["ended_blank"] = True
            continue
        if HEADER.match(ln):
            hdr = [ln]
            if cur and cur["rows"] and ln.split() == cur["hdr_lines"][0].split():
                rec, cur["in_hdr"] = None, True          # repeated header (same table, maybe next page)
                cur["cur_hdr"] = ln                      # its column offsets may differ -> used for later rows
                cur["ended_blank"] = False
                if p not in cur["pages"]:
                    cur["pages"].append(p)
                continue
            close()
            cur = {"page": p, "pages": [p], "hdr_lines": hdr, "rows": collections.OrderedDict(), "in_hdr": True, "cur_hdr": ln, "rec_hdr": {},
                   "ended_blank": False, "after_text": gap_text}
            gap_text = False
            continue
        if cur is None:
            gap_text = True
            continue
        m = RECORD.match(ln)
        if m:
            n = int(m.group(1))
            if cur.get("ended_blank") and cur["rows"]:
                close(); gap_text = True
                continue
            cur["in_hdr"] = False
            if ln.startswith(" "):
                cur["centered"] = True                 # indented row no. = vertically centred cells (pre-lines)
            rec = [ln]
            cur["rows"][n] = rec
            cur["rec_hdr"][n] = cur["cur_hdr"]
            continue
        if ln.startswith("  ") and not cur.get("ended_blank"):
            if cur["in_hdr"] and not cur["rows"]:
                cur["hdr_lines"].append(ln)
            elif rec is not None:
                rec.append(ln)
            continue
        close(); gap_text = True
    close()
    # merge page-broken fragments: same header, no text between, rows continue
    merged = []
    for t in tables:
        if merged and not t["after_text"] and t["hdr_lines"][0].split() == merged[-1]["hdr_lines"][0].split() \
                and min(t["rows"]) == max(merged[-1]["rows"]) + 1:
            merged[-1]["rows"].update(t["rows"])
            merged[-1]["rec_hdr"].update(t["rec_hdr"])
            merged[-1]["pages"] += t["pages"]
            continue
        merged.append(t)
    return merged

def rec_tokens(rec_lines):
    """Tokens of a PDF record; tokens wrapped after '-'/'_' re-joined with the column-aligned continuation."""
    first = rec_lines[0]
    spans = [(m.start(), m.group()) for m in re.finditer(r"\S+", first)]
    rest = []
    for ln in rec_lines[1:]:
        rest.append([(m.start(), m.group()) for m in re.finditer(r"\S+", ln)])
    toks = [t for _, t in spans]
    pending = [(x, t) for x, t in spans]
    for line in rest:
        nxt = []
        for x, t in line:
            # find a token from the previous visual line in the same column that ended with '-' or '_'
            j = next((k for k, (px, pt) in enumerate(pending) if abs(px - x) <= 2 and pt[-1] in "-_"), None)
            if j is not None:
                px, pt = pending[j]
                toks.remove(pt)
                toks.append(pt + t)
                pending[j] = (px, pt + t)
                nxt.append((px, pt + t))
            else:
                toks.append(t)
                nxt.append((x, t))
        pending = nxt + [pp for pp in pending if pp not in nxt]
    return toks

def hdr_tokens(lines):
    return rec_tokens(lines)

# ── KB side ───────────────────────────────────────────────────────────────────
def parse_kb_tables(path):
    tables, block, start = [], [], None
    lines = open(path, encoding="utf-8").read().split("\n")
    for i, ln in enumerate(lines + [""], 1):
        if ln.lstrip().startswith("|"):
            if not block:
                start = i
            block.append(ln)
            continue
        if len(block) >= 2 and re.match(r"^\s*\|[\s:|-]+\|\s*$", block[1]):
            cells = lambda r: [kb_cell(c) for c in re.split(r"(?<!\\)\|", r.strip())[1:-1]]
            tables.append({"file": path, "line": start, "header": cells(block[0]),
                           "rows": [cells(r) for r in block[2:]]})
        block = []
    return tables

def kb_tokens(cells):
    return [t for c in cells for t in c.split()]

# ── compare ───────────────────────────────────────────────────────────────────
def col_starts(hdr_lines, ncols):
    """Header column start offsets for a single-line header; None if they cannot be matched to ncols."""
    if len(hdr_lines) != 1:
        return None
    h = hdr_lines[0]
    for pat in (r"\S+(?: \S+)*", r"\S+"):         # cells split by 2+ spaces, else by any space
        st = [m.start() for m in re.finditer(pat, h)]
        if len(st) == ncols:
            return st
    return None

def compare_row(kb_cells, rec, hdr_lines):
    """Single-line record + single-line header: tokens assigned to header columns by x offset, compared
    cell by cell INCLUDING empty cells ('columns'); if offsets unusable: token order ('order');
    wrapped record: token multiset ('multiset')."""
    kt = kb_tokens(kb_cells)
    if len(rec) == 1:
        st = col_starts(hdr_lines, len(kb_cells))
        if st:
            cols = [[] for _ in st]
            for m in re.finditer(r"\S+", rec[0]):
                j = max([k for k, x in enumerate(st) if x <= m.start() + 2] or [0])
                cols[j].append(m.group())
            pc = [" ".join(c) for c in cols]
            kc = [" ".join(c.split()) for c in kb_cells]
            bad = [(k, kc[k], pc[k]) for k in range(len(st)) if kc[k] != pc[k]]
            return not bad, [f"col{k + 1}={a!r}" for k, a, _ in bad], [f"col{k + 1}={b!r}" for k, _, b in bad], "columns"
        pt = rec[0].split()
        return kt == pt, " ".join(kt), " ".join(pt), "order"
    pt = rec_tokens(rec)
    ck, cp = collections.Counter(kt), collections.Counter(pt)
    return ck == cp, sorted((ck - cp).elements()), sorted((cp - ck).elements()), "multiset"

def row_hdr(t, n):
    """Header lines governing record n (single-line header: the most recent repeat of it)."""
    return [t["rec_hdr"][n]] if len(t["hdr_lines"]) == 1 else t["hdr_lines"]

def score(kt, pt):
    """(exact rows, token similarity over overlapping rows)."""
    exact, inter, tot = 0, 0, 0
    for n, cells in kt["byrow"].items():
        if n in pt["rows"]:
            ok, *_ = compare_row(cells, pt["rows"][n], row_hdr(pt, n))
            exact += ok
            ck = collections.Counter(kb_tokens(cells))
            cp = collections.Counter(pt["rows"][n][0].split() if len(pt["rows"][n]) == 1 else rec_tokens(pt["rows"][n]))
            inter += sum((ck & cp).values()); tot += max(sum(ck.values()), sum(cp.values()))
    return exact, (inter / tot if tot else 0.0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", required=True, help="src:lo-hi, e.g. ig34:275-284")
    ap.add_argument("--kb", nargs="+", required=True)
    ap.add_argument("--kb-root", default=f"{ROOT}/knowledge_base", help="KB root (paths in --kb are re-rooted here)")
    ap.add_argument("--pdf-pages", default=f"{W}/pdf_pages")
    ap.add_argument("--out", required=True)
    ap.add_argument("--baseline")
    a = ap.parse_args()
    src, rng = a.pages.split(":"); lo, hi = map(int, rng.split("-"))
    pdf = parse_pdf_tables(pdf_lines(a.pdf_pages, src, lo, hi))
    unparsed = [t for t in pdf if not t["rows"] or t.get("centered")]
    pdf = [t for t in pdf if t not in unparsed]
    for t in pdf:
        t["hdr"] = hdr_tokens(t["hdr_lines"])

    kbt = []
    for rel in a.kb:
        rel = rel[len("knowledge_base/"):] if rel.startswith("knowledge_base/") else rel
        for t in parse_kb_tables(os.path.join(a.kb_root, rel)):
            t["file"] = "knowledge_base/" + rel
            kbt.append(t)
    for t in kbt:
        t["parseable"] = bool(t["header"]) and t["header"][0] == "Row" and all(r and r[0].isdigit() for r in t["rows"])
        t["byrow"] = {int(r[0]): r for r in t["rows"]} if t["parseable"] else {}

    # pairing: (1) one-to-one by (header equal, exact rows, similarity); (2) leftover KB tables may pair with an
    # already-paired PDF table as a KB-side duplicate (e.g. the same dataset shown in 2 KB files). Min similarity 0.6.
    cands = []
    for i, k in enumerate(kbt):
        if not k["parseable"]:
            continue
        kh = collections.Counter(kb_tokens(k["header"]))
        for j, p in enumerate(pdf):
            if not set(k["byrow"]) & set(p["rows"]):
                continue
            ex, sim = score(k, p)
            hdr_eq = kh == collections.Counter(p["hdr"])
            if sim >= 0.6:
                cands.append(((-ex, -sim, -int(hdr_eq), abs(i - j)), i, j))
    cands.sort()
    pair_k, pair_p, dup = {}, {}, set()
    for _, i, j in cands:
        if i not in pair_k and j not in pair_p:
            pair_k[i], pair_p[j] = j, i
    for _, i, j in cands:
        if i not in pair_k:
            pair_k[i] = j; dup.add(i)

    report = {"pages": a.pages, "kb_files": a.kb, "tables": [], "pdf_only": [],
              "pdf_unparsed": [{"pages": t["pages"], "header": t["hdr_lines"][0].split()[:12], "n_rows": len(t["rows"]),
                                "reason": "vertically centred cells (indented row no.)" if t["rows"] else "no record lines"}
                               for t in unparsed]}
    for i, k in enumerate(kbt):
        ent = {"file": k["file"], "line": k["line"], "n_rows": len(k["rows"]), "header": " | ".join(k["header"])[:120]}
        if not k["parseable"]:
            ent["status"] = "UNPARSEABLE"
        elif i not in pair_k:
            ent["status"] = "NO_PDF"
        else:
            p = pdf[pair_k[i]]
            first, last = min(p["rows"]), max(p["rows"])
            diffs, cells, out_of_range = [], 0, []
            if collections.Counter(kb_tokens(k["header"])) != collections.Counter(p["hdr"]):
                kh, ph = collections.Counter(kb_tokens(k["header"])), collections.Counter(p["hdr"])
                diffs.append({"row": "HEADER", "kb_only": sorted((kh - ph).elements()), "pdf_only": sorted((ph - kh).elements())})
            modes = collections.Counter()
            for n, cellsrow in k["byrow"].items():
                if n not in p["rows"]:
                    if (n < first and p["pages"][0] == lo) or (n > last and p["pages"][-1] == hi):
                        out_of_range.append(n)
                    else:
                        diffs.append({"row": n, "kb_only": "ROW", "pdf_only": []})
                    continue
                ok, ko, po, mode = compare_row(cellsrow, p["rows"][n], row_hdr(p, n))
                modes[mode] += 1
                cells += len(cellsrow)
                if not ok:
                    diffs.append({"row": n, "mode": mode, "kb_only": ko, "pdf_only": po})
            for n in p["rows"]:
                if n not in k["byrow"]:
                    diffs.append({"row": n, "kb_only": [], "pdf_only": "ROW"})
            subset = i in dup and diffs and all(d["pdf_only"] == "ROW" for d in diffs)
            ent.update({"status": "OK_SUBSET" if subset else ("DIFF" if diffs else "OK"), "kb_duplicate": i in dup,
                        "pdf_pages": p["pages"], "pdf_rows": len(p["rows"]),
                        "cells_compared": cells, "row_modes": dict(modes), "rows_out_of_page_range": out_of_range, "diffs": diffs})
        report["tables"].append(ent)
    for j, p in enumerate(pdf):
        if j not in pair_p:
            report["pdf_only"].append({"pages": p["pages"], "header": " ".join(p["hdr"])[:120], "n_rows": len(p["rows"])})

    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    C = collections.Counter(t["status"] for t in report["tables"])
    print(f"PDF tables parsed: {len(pdf)} (pages {a.pages}); KB tables: {len(kbt)}; status: {dict(C)}; "
          f"PDF_ONLY: {len(report['pdf_only'])}; cells compared: {sum(t.get('cells_compared', 0) for t in report['tables'])}")
    for t in report["tables"]:
        if t["status"] != "OK":
            print(f"  {t['status']:<11} {t['file']}:{t['line']} rows={t['n_rows']} {t['header'][:60]}")
            for d in t.get("diffs", [])[:8]:
                print("      ", d)
    for p in report["pdf_only"]:
        print("  PDF_ONLY   ", p)
    for p in report["pdf_unparsed"]:
        print("  PDF_UNPARSED (manual census)", p)
    rc = 1 if (C["DIFF"] or report["pdf_only"]) else 0
    if a.baseline:
        base = json.load(open(a.baseline, encoding="utf-8"))
        same = all(base.get(k) == report[k] for k in ("tables", "pdf_only", "pdf_unparsed"))
        print(f"BASELINE {a.baseline}: {'identical' if same else 'DIFFERS'}")
        if not same:
            bt = {(t["file"], t["line"]): t for t in base["tables"]}
            for t in report["tables"]:
                if bt.get((t["file"], t["line"])) != t:
                    print("  CHANGED", t["file"], t["line"], t["status"], [d for d in t.get("diffs", []) if d not in bt.get((t["file"], t["line"]), {}).get("diffs", [])][:5])
        rc = 0 if same else 1
    print("RESULT:", "RED" if rc else "GREEN")
    sys.exit(rc)

if __name__ == "__main__":
    main()
