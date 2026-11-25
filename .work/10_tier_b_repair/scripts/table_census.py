#!/usr/bin/env python3
"""Table census v2 (T0.3b / G-TB4): KB markdown "Row" tables vs PDF tables, cell by cell, positional by column.
v1 (scripts/archive/table_census_v1.py) read pdftotext -layout text; its multiset/order fallbacks passed swapped or
moved values, it keyed rows on the Row number, and paired tables by best similarity only (T1 false-OK modes b/c/d).
v2 changes:
- PDF side = word bounding boxes (pdftotext -bbox, cached under work/pdf_bbox/, gitignored). Header words give the
  column x-starts; every data word goes to the column whose x-start is the closest one at or left of it, so empty
  cells and wrapped (multi-line) cells are compared positionally. Vertically centred tables (words above the first
  row number) are PDF_UNPARSED (manual census).
- Columns are mapped by index along the ordered header (equal column count) or by header-name sequence alignment
  (different count); header renames / reorders are reported once per table as HEADER diffs.
- Rows are aligned as ordered sequences by content (DP; row-number equality is a bonus, not the key), so a PDF that
  skips a row number does not shift the whole table, and duplicate KB row numbers are not silently dropped.
  Row-number disagreements are reported as a diff in column "Row".
- Pairing key = (example label, dataset caption, ordinal within the example); a KB table may only pair with a PDF table
  whose known keys agree. Keyed pairs have no similarity floor (a badly corrupted copy is DIFF, not NO_PDF).
  Every KB table is checked: tables left over after one-to-one pairing are compared as KB duplicates (kb_duplicate).
Cell equality: whitespace-collapsed strings equal; else equal after removing all whitespace (counted as ws_only:
PDF line-wrap joins are ambiguous, e.g. 'CD56-' + 'FSC SSC'). NFKC + quote/dash unification only.
A KB row whose cell count differs from its header is a ROW_SHAPE diff; absent KB cells compare as missing.
Status per KB table: OK | OK_SUBSET (KB duplicate showing only some PDF rows, all equal) | DIFF | NO_PDF |
UNPARSEABLE (no Row column / non-numeric Row cell). PDF tables never paired -> PDF_ONLY. Exit 1 if any DIFF / NO_PDF /
PDF_ONLY (or, with --baseline, if the report differs from the baseline report).
Usage (repo root):
  python3 -I .work/10_tier_b_repair/scripts/table_census.py --pages ig34:275-284 --kb knowledge_base/domains/PC/examples.md \
      ... --out <json>                          # one page range for all --kb files (T0/T0.4 style)
  python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest <json> --out <json>
      # manifest: [{"file": "knowledge_base/...", "src": "ig34", "lo": 60, "hi": 62}, ...]; the whole PDF of each src
      # is parsed once, each KB file pairs only with PDF tables touching its own range (+-3 pages); PDF_ONLY is global.
"""
import argparse, collections, html, json, os, re, subprocess, sys, unicodedata

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
W = f"{ROOT}/.work/10_tier_b_repair/work"
PDFS = {"ig34": f"{ROOT}/source/cdisc/SDTMIG v3.4 (no header footer).pdf", "sv20": f"{ROOT}/source/cdisc/SDTM_v2.0.pdf"}
NPAGES = {"ig34": 461, "sv20": 74}
_TR = str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-", "‐": "-", "‑": "-",
                     "−": "-", " ": " "})
FOOTER = re.compile(r"^(© \d{4} Clinical Data Interchange Standards Consortium|\d{4}-\d{2}-\d{2}$|Page \d+$)")
EXAMPLE = re.compile(r"^Example\s+(\d+[A-Za-z]?)\b")
DSCAP = re.compile(r"^([a-z][a-z0-9]*\.xpt)$")
SECTION = re.compile(r"^(\d+(?:\.\d+){1,6})\s+[A-Z§]")
IDENT = re.compile(r"^([A-Z][A-Z0-9_]*|…|\.\.\.|Row)$")
PAREN = re.compile(r"^\(?[A-Za-z0-9_.#/-]*\)?$")

def hdr_cont(ws):
    """A wrapped header line: identifiers only, or a parenthesised note such as '(Example 1)'."""
    return all(IDENT.match(w[4]) or (PAREN.match(w[4]) and ("(" in w[4] or ")" in w[4] or w[4].isdigit())) for w in ws) \
        and any(IDENT.match(w[4]) or "(" in w[4] or ")" in w[4] for w in ws)

def clean(s):
    return unicodedata.normalize("NFKC", s).translate(_TR)

def wsn(s):
    return " ".join(s.split())

def kb_cell(c):
    c = re.sub(r"<br\s*/?>", " ", c, flags=re.I)
    c = re.sub(r"\*\*|`", "", c).replace("\\|", "|")
    return wsn(clean(c))

# ── PDF side: word boxes ─────────────────────────────────────────────────────────────────────────────────
WORD = re.compile(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)</word>')

def page_words(src, p, bbox_dir):
    path = f"{bbox_dir}/{src}_p{p:04d}.tsv"
    if not os.path.exists(path):
        os.makedirs(bbox_dir, exist_ok=True)
        out = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-bbox", PDFS[src], "-"],
                             capture_output=True, text=True, check=True).stdout
        with open(path + ".tmp", "w", encoding="utf-8") as f:
            for m in WORD.finditer(out):
                f.write("\t".join(m.groups()[:4]) + "\t" + clean(html.unescape(m.group(5))) + "\n")
        os.replace(path + ".tmp", path)
    ws = []
    for ln in open(path, encoding="utf-8"):
        a, b, c, d, t = ln.rstrip("\n").split("\t")
        ws.append((float(a), float(b), float(c), float(d), t))
    return ws

def page_lines(words):
    """Cluster words into visual lines (yMin within 1.5pt); each line = words sorted by x."""
    lines = []
    for w in sorted(words, key=lambda w: (w[1], w[0])):
        if lines and w[1] - lines[-1]["y"] <= 1.5:
            lines[-1]["w"].append(w)
        else:
            lines.append({"y": w[1], "w": [w]})
    for L in lines:
        L["w"].sort(key=lambda w: w[0])
        L["text"] = " ".join(w[4] for w in L["w"])
    return [L for L in lines if not FOOTER.match(L["text"])]

def header_columns(hwords):
    """Header words -> columns [(x_start, name)]: words sharing an x-start (+-2pt, wrapped header) form one column;
    words on one line closer than 3.5pt (one space) are one multi-word header cell."""
    cols = []
    for w in sorted(hwords, key=lambda w: (w[0], w[1])):
        c = next((c for c in cols if abs(c["x"] - w[0]) <= 2.0), None)
        if c is None:
            cols.append({"x": w[0], "w": [w]})
        else:
            c["w"].append(w)
    cols.sort(key=lambda c: c["x"])
    merged = []
    for c in cols:
        if merged:
            p = merged[-1]
            if any(abs(q[1] - w[1]) <= 1.5 and 0 <= w[0] - q[2] < 3.5 for q in p["w"] for w in c["w"]):
                p["w"] += c["w"]; continue
        merged.append(c)
    return [(c["x"], join_words(c["w"])) for c in merged]

def join_words(ws):
    """Words of one cell in reading order; a line wrap after '-', '_' or before '/' is joined without a space."""
    out, last_y = "", None
    for w in sorted(ws, key=lambda w: (round(w[1]), w[0])):
        t = w[4]
        if not out:
            out = t
        elif last_y is not None and abs(w[1] - last_y) > 1.5 and (out[-1] in "-_/" or t[0] == "/"):
            out += t
        else:
            out += " " + t
        last_y = w[1]
    return out

def cells_of(rec_words, cols):
    xs = [x for x, _ in cols]
    buckets = [[] for _ in xs]
    for w in rec_words:
        k = max([i for i, x in enumerate(xs) if x <= w[0] + 2.0] or [0])
        buckets[k].append(w)
    return [join_words(b) for b in buckets], [len({round(w[1]) for w in b}) > 1 for b in buckets]

def parse_pdf(src, pages, bbox_dir):
    """Stream lines over pages -> tables. A table = 'Row <IDENT> ...' header line (+ wrapped header lines) then records;
    a record starts with a number at the Row column x and owns the following lines with no word in the Row column.
    A table continues across a page break (repeated identical header, or records at the same Row x)."""
    tables, cur, ctx = [], None, {"ex": None, "ds": None, "sec": None, "ord": collections.Counter()}
    def close():
        nonlocal cur
        if cur:
            tables.append(cur)
        cur = None
    for p in pages:
        lines = page_lines(page_words(src, p, bbox_dir))
        skip, last_y = 0, None
        for i, L in enumerate(lines):
            ws, t = L["w"], L["text"]
            if i < skip:
                continue                                         # wrapped header line already consumed
            if cur and cur["recs"] and last_y is not None and L["y"] - last_y > 30:
                close()                                          # large vertical gap ends the table
            last_y = L["y"]
            is_hdr = len(ws) >= 3 and ws[0][4] == "Row" and IDENT.match(ws[1][4] or "")
            no_row = False      # some PDF tables have no 'Row' header word (e.g. p142): STUDYID header + numbered records
            if not is_hdr and len(ws) >= 3 and ws[0][4] == "STUDYID" and all(IDENT.match(w[4]) for w in ws) and i + 1 < len(lines):
                nx = lines[i + 1]["w"][0]
                if re.fullmatch(r"\d+", nx[4]) and nx[0] < ws[0][0] - 3 and lines[i + 1]["y"] - L["y"] < 12:
                    is_hdr = no_row = True
            if is_hdr:
                hdr_words = list(ws) if not no_row else [(nx[0], L["y"], nx[0] + 10, L["y"] + 8, "Row")] + list(ws)
                ws = hdr_words
                c1 = header_columns(hdr_words)
                if cur and cur["recs"] and [n for _, n in c1] == cur["hdr1"] and len(c1) == len(cur["cols"]):
                    # repeated header (e.g. next page): first line only; lines above the next row number are that
                    # record's vertically centred cells (p356 TRREASND), not wrapped header words
                    skip = i + 1
                    cur["cols"] = c1; cur["row_x"] = ws[0][0]; cur["pages"] = sorted(set(cur["pages"]) | {p})
                    cur["after_hdr"], cur["pending"] = True, []
                    continue
                j = i + 1          # wrapped header lines: identifier-only, directly below, nothing in the Row column
                while j < len(lines) and lines[j]["y"] - lines[j - 1]["y"] < 11 and \
                        lines[j]["w"][0][0] > ws[0][0] + 6 and hdr_cont(lines[j]["w"]):
                    hdr_words += lines[j]["w"]; j += 1
                cols = header_columns(hdr_words)
                names = [n for _, n in cols]
                skip = j
                if cur and names == cur["hdr"]:                 # repeated header -> same table, new x offsets
                    cur["cols"] = cols; cur["row_x"] = ws[0][0]; cur["pages"] = sorted(set(cur["pages"]) | {p})
                    continue
                close()
                key = (ctx["sec"], ctx["ex"], ctx["ds"])
                ctx["ord"][key] += 1
                cur = {"src": src, "page": p, "pages": [p], "hdr": names, "hdr1": [n for _, n in c1], "cols": cols, "row_x": ws[0][0],
                       "recs": [], "no_row_hdr": no_row, "after_hdr": False, "pending": [], "pre_attached": 0,
                       "centered": False, "ex": ctx["ex"], "ds": ctx["ds"], "sec": ctx["sec"], "ord": ctx["ord"][key]}
                ctx["ds"] = None
                continue
            if cur:
                first = ws[0]
                if cur["row_x"] - 1.5 <= first[0] < (cur["cols"][1][0] - 2.0 if len(cur["cols"]) > 1 else cur["row_x"] + 6) \
                        and re.fullmatch(r"\d+", first[4]):
                    cur["recs"].append({"n": int(first[4]), "words": ws[1:], "orphan": cur["pending"], "cols": cur["cols"], "page": p})
                    cur["pre_attached"] += bool(cur["pending"]); cur["after_hdr"], cur["pending"] = False, []
                    cur["pages"] = sorted(set(cur["pages"]) | {p})
                    continue
                if len(cur["cols"]) > 1 and first[0] > cur["cols"][1][0] - 2.0:
                    if cur["after_hdr"]:
                        cur["pending"] += ws
                    elif cur["recs"]:
                        cur["recs"][-1]["words"] += ws
                    else:
                        cur["centered"] = True; cur.setdefault("pre", []).extend(ws)
                    continue
                close()
            m = EXAMPLE.match(t)
            if m and len(ws) <= 3:
                ctx["ex"], ctx["ds"] = m.group(1).lower(), None
            elif DSCAP.match(t):
                ctx["ds"] = t
            elif SECTION.match(t) and ws[0][0] < 80:
                ctx["sec"], ctx["ex"], ctx["ds"] = SECTION.match(t).group(1), None, None
        # page end: keep cur open (table may continue on next page)
    close()
    # Words between a repeated (page-break) header and the next row number are either that record's vertically
    # centred cells (p356) or the previous record's cell continued from the previous page (p358). Both readings are
    # kept (rows = geometric default, rows_alt = flipped); compare() uses whichever agrees better with the KB.
    # Default reading per orphan (geometry): previous record if its cells in the orphan's columns are all non-empty
    # (a wrapped cell continued over the page break), else the next record (a vertically centred cell); ties keep it.
    def col_idx(w, cols):
        return max([k for k, (x, _) in enumerate(cols) if x <= w[0] + 2.0] or [0])
    for tb in tables:
        dflt = {}
        for i, r in enumerate(tb["recs"]):
            if r.get("orphan") and i > 0:
                prev = tb["recs"][i - 1]
                pc = {col_idx(w, prev["cols"]) for w in prev["words"]}
                dflt[i] = all(col_idx(w, r["cols"]) in pc for w in r["orphan"])
        for key, flip in (("rows", False), ("rows_alt", True)):
            words = [list(r["words"]) for r in tb["recs"]]
            for i, r in enumerate(tb["recs"]):
                if r.get("orphan"):
                    to_prev = dflt.get(i, False) != flip and i > 0
                    if to_prev:      # words from the next page: shift y so they read after the previous page's lines
                        words[i - 1] += [(w[0], w[1] + 10000, w[2], w[3] + 10000, w[4]) for w in r["orphan"]]
                    else:
                        words[i] += r["orphan"]
            tb[key] = []
            for r, w in zip(tb["recs"], words):
                cells, wrapped = cells_of(w, r["cols"][1:])
                tb[key].append({"n": r["n"], "cells": cells, "wrapped": any(wrapped), "page": r["page"]})
        tb["has_orphans"] = any(r.get("orphan") for r in tb["recs"])
        tb["hdr_cells"] = tb["hdr"][1:]
    return tables

# ── KB side ──────────────────────────────────────────────────────────────────────────────────────────────
def parse_kb_tables(path, rel):
    tables, block, start = [], [], None
    lines = open(path, encoding="utf-8").read().split("\n")
    stack, ds, ordc = [], None, collections.Counter()       # heading stack [(level, ex, sec)]
    def ctx():
        ex = next((e for _, e, _ in reversed(stack) if e), None)
        sec = next((s for _, _, s in reversed(stack) if s), None)
        return ex, sec
    for i, ln in enumerate(lines + [""], 1):
        if ln.lstrip().startswith("|"):
            if not block:
                start = i
            block.append(ln)
            continue
        if len(block) >= 2 and re.match(r"^\s*\|[\s:|-]+\|\s*$", block[1]):
            cells = lambda r: [kb_cell(c) for c in re.split(r"(?<!\\)\|", r.strip())[1:-1]]
            ex, sec = ctx()
            key = (tuple(stack), ds)
            ordc[key] += 1
            tables.append({"file": rel, "line": start, "header": cells(block[0]),
                           "rows": [(start + 2 + k, cells(r)) for k, r in enumerate(block[2:])],
                           "ex": ex, "ds": ds, "sec": sec, "ord": ordc[key]})
            ds = None
        block = []
        h = re.match(r"^(#{1,6})\s+(.*)$", ln)
        b = re.match(r"^\*\*(Example\s+\d+[A-Za-z]?)[^*]*\*\*\s*$", ln.strip())
        if h or b:
            lvl, txt = (len(h.group(1)), h.group(2)) if h else (7, b.group(1))
            while stack and stack[-1][0] >= lvl:
                stack.pop()
            em = re.search(r"\bExample\s+(\d+[A-Za-z]?)\b", txt)
            sm = re.match(r"^§?(\d+(?:\.\d+){1,6})\b", txt)
            stack.append((lvl, em.group(1).lower() if em else None, sm.group(1) if sm else None))
            ds = None
            continue
        m = re.match(r"^\s*\*{0,2}`?([a-z][a-z0-9]*\.xpt)`?\*{0,2}\s*:?\s*$", ln)
        if m:
            ds = m.group(1)
    return tables

# ── compare ──────────────────────────────────────────────────────────────────────────────────────────────
def norm_h(s):
    return re.sub(r"\s+", "", s)

def col_map(kh, ph):
    """KB column index -> PDF column index (or None): by index when the counts are equal and index mapping agrees on
    at least as many header names as a header-name sequence alignment; otherwise the alignment (values follow the
    header name; a KB column missing in the PDF maps to None)."""
    import difflib
    sm = difflib.SequenceMatcher(a=[norm_h(x) for x in kh], b=[norm_h(x) for x in ph], autojunk=False)
    m = [None] * len(kh)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            m[a + k] = b + k
    if len(kh) == len(ph) and sum(norm_h(x) == norm_h(y) for x, y in zip(kh, ph)) >= sum(v is not None for v in m):
        return list(range(len(kh)))
    return m

def cell_eq(a, b):
    if a == b:
        return "eq"
    if re.sub(r"\s+", "", a) == re.sub(r"\s+", "", b):
        return "ws"
    return None

def row_cmp(kcells, prow, cmap):
    """Positional compare of KB data cells (no Row cell) with a PDF record. -> (n_equal, n_cols, diffs, n_ws)."""
    eq, ws, diffs = 0, 0, []
    kcells = list(kcells) + [None] * (len(cmap) - len(kcells))   # KB row shorter than its header: missing cells
    for k, kc in enumerate(kcells):
        j = cmap[k] if k < len(cmap) else None
        pc = prow["cells"][j] if j is not None and j < len(prow["cells"]) else None
        if kc is None:                                  # absent KB cell: equal only if the PDF cell is empty too
            r = None if pc else "eq"
        else:
            r = cell_eq(kc, pc) if pc is not None else (None if kc else "eq")
        if r:
            eq += 1; ws += r == "ws"
        else:
            diffs.append((k, kc, pc))
    used = {j for j in cmap if j is not None}       # PDF columns absent from the KB header: a non-empty PDF value is a diff
    for j, pc in enumerate(prow["cells"]):
        if j not in used and pc:
            diffs.append((("pdf", j), None, pc))
    return eq, max(1, len(kcells)), diffs, ws

def align_rows(krows, prows, cmap):
    """Order-preserving alignment of KB rows to PDF records (DP). Match score = cell agreement (+0.05 tie-break if row
    numbers equal: content decides, so renumbered rows do not drag the alignment); a pair is allowed if agreement >= 0.5
    or the row numbers are equal. Returns list of (ki|None, pj|None)."""
    nk, npd = len(krows), len(prows)
    sc = [[None] * npd for _ in range(nk)]
    for i, (_, kc) in enumerate(krows):
        for j, pr in enumerate(prows):
            eq, n, _, _ = row_cmp(kc[1:], pr, cmap)
            s, same = eq / n, kc[0] == str(pr["n"])
            if s >= 0.5 or same:
                sc[i][j] = s + (0.05 if same else 0)
    D = [[0.0] * (npd + 1) for _ in range(nk + 1)]
    for i in range(nk - 1, -1, -1):
        for j in range(npd - 1, -1, -1):
            best = max(D[i + 1][j], D[i][j + 1])
            if sc[i][j] is not None:
                best = max(best, sc[i][j] + D[i + 1][j + 1])
            D[i][j] = best
    out, i, j = [], 0, 0
    while i < nk and j < npd:
        if sc[i][j] is not None and abs(D[i][j] - (sc[i][j] + D[i + 1][j + 1])) < 1e-9:
            out.append((i, j)); i += 1; j += 1
        elif abs(D[i][j] - D[i + 1][j]) < 1e-9:
            out.append((i, None)); i += 1
        else:
            out.append((None, j)); j += 1
    out += [(k, None) for k in range(i, nk)] + [(None, k) for k in range(j, npd)]
    return out, sum(sc[a][b] for a, b in out if a is not None and b is not None)

def compare(k, p):
    if p.get("has_orphans"):              # page-break orphan words: pick the reading that agrees better with the KB
        a, b = compare1(k, p, p["rows"]), compare1(k, p, p["rows_alt"])
        r = a if a["sim"] >= b["sim"] else b
        r["orphan_reading"] = "geometric default" if r is a else "flipped (KB agrees better)"
        return r
    return compare1(k, p, p["rows"])

def compare1(k, p, prows):
    kh, ph = k["header"][1:], p["hdr_cells"]
    cmap = col_map(kh, ph)
    diffs, cells, wsc = [], 0, 0
    hd = []
    for a, b in enumerate(cmap):
        if b is None or norm_h(kh[a]) != norm_h(ph[b]):
            hd.append({"idx": a + 1, "kb": kh[a], "pdf": ph[b] if b is not None else None})
    used = {b for b in cmap if b is not None}
    hd += [{"idx": None, "kb": None, "pdf": ph[b]} for b in range(len(ph)) if b not in used]
    if hd:
        diffs.append({"type": "HEADER", "cols": hd})
    pairs, total = align_rows(k["rows_c"], prows, cmap)
    renum = 0
    for a, b in pairs:
        if b is None:
            diffs.append({"type": "KB_ROW_UNMATCHED", "kb_row": k["rows_c"][a][1][0], "kb_line": k["rows_c"][a][0]}); continue
        pr = prows[b]
        if a is None:
            diffs.append({"type": "PDF_ROW_MISSING", "pdf_row": pr["n"], "pdf_page": pr["page"]}); continue
        line, kc = k["rows_c"][a]
        eq, n, dd, ws = row_cmp(kc[1:], pr, cmap)
        cells += len(kc); wsc += ws
        if len(kc) != len(k["header"]):
            diffs.append({"type": "ROW_SHAPE", "kb_row": kc[0], "pdf_row": pr["n"], "kb_line": line, "kb_cells": len(kc), "header_cells": len(k["header"])})
        if kc[0] != str(pr["n"]):
            renum += 1
            diffs.append({"type": "CELL", "kb_row": kc[0], "pdf_row": pr["n"], "kb_line": line, "col": "Row", "kb": kc[0], "pdf": str(pr["n"])})
        for c, kv, pv in dd:
            if isinstance(c, tuple):                 # PDF-only column
                diffs.append({"type": "CELL", "kb_row": kc[0], "pdf_row": pr["n"], "kb_line": line, "col": ph[c[1]],
                              "col_idx": None, "kb": None, "pdf": pv, "wrapped": pr["wrapped"]})
                continue
            diffs.append({"type": "CELL", "kb_row": kc[0], "pdf_row": pr["n"], "kb_line": line, "col": kh[c] if c < len(kh) else f"(extra col {c + 2})",
                          "col_idx": c + 2, "kb": kv, "pdf": pv, "wrapped": pr["wrapped"]})   # kb None = KB cell absent
    sim = total / max(1, len(k["rows_c"]), len(prows))
    return {"diffs": diffs, "cells": cells, "ws_only": wsc, "renumbered": renum, "sim": sim}

def keys_ok(k, p):
    for f in ("ex", "ds"):
        if k[f] and p[f] and k[f] != p[f]:
            return False
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", help="src:lo-hi, e.g. ig34:275-284 (all --kb files)")
    ap.add_argument("--kb", nargs="+", default=[])
    ap.add_argument("--manifest")
    ap.add_argument("--kb-root", default=f"{ROOT}/knowledge_base", help="KB root (paths are re-rooted here)")
    ap.add_argument("--bbox-dir", default=f"{W}/pdf_bbox")
    ap.add_argument("--out", required=True)
    ap.add_argument("--baseline")
    a = ap.parse_args()
    if a.manifest:
        man = json.load(open(a.manifest, encoding="utf-8")); full = True
    else:
        src, rng = a.pages.split(":"); lo, hi = map(int, rng.split("-"))
        man = [{"file": f, "src": src, "lo": lo, "hi": hi} for f in a.kb]; full = False
    srcs = sorted({m["src"] for m in man})
    pdf = []
    for s in srcs:
        pages = range(1, NPAGES[s] + 1) if full else range(min(m["lo"] for m in man if m["src"] == s),
                                                             max(m["hi"] for m in man if m["src"] == s) + 1)
        pdf += parse_pdf(s, pages, a.bbox_dir)
    unparsed = [t for t in pdf if not t["rows"] or t["centered"]]
    pdf = [t for t in pdf if t not in unparsed]

    kbt = []
    for m in man:
        rel = m["file"][len("knowledge_base/"):] if m["file"].startswith("knowledge_base/") else m["file"]
        for t in parse_kb_tables(os.path.join(a.kb_root, rel), "knowledge_base/" + rel):
            t["m"] = m
            t["parseable"] = bool(t["header"]) and t["header"][0] == "Row" and bool(t["rows"]) and \
                all(r and r[0].isdigit() for _, r in t["rows"])
            t["rows_c"] = t["rows"]
            kbt.append(t)

    cands = []
    for i, k in enumerate(kbt):
        if not k["parseable"]:
            continue
        m = k["m"]
        for j, p in enumerate(pdf):
            if p["src"] != m["src"] or not any(m["lo"] - 3 <= pg <= m["hi"] + 3 for pg in p["pages"]) or not keys_ok(k, p):
                continue
            keyed = sum(bool(k[f] and p[f] and k[f] == p[f]) for f in ("ex", "ds"))
            r = compare(k, p)
            if keyed < 2 and r["sim"] < 0.5:
                continue
            sec_ok = int(bool(k["sec"] and p["sec"] and (p["sec"].startswith(k["sec"]) or k["sec"].startswith(p["sec"]))))
            cands.append(((-keyed, -sec_ok, -(k["ord"] == p["ord"]), -r["sim"], abs(i - j)), i, j, r))
    cands.sort(key=lambda c: c[0])
    pair_k, pair_p, dup = {}, {}, set()
    for _, i, j, r in cands:
        if i not in pair_k and j not in pair_p:
            pair_k[i], pair_p[j] = (j, r), i
    for _, i, j, r in cands:
        if i not in pair_k:
            pair_k[i] = (j, r); dup.add(i)
    # a KB table paired one-to-one with a clearly worse candidate than its best one is a duplicate of the best one
    best = {}
    for c in cands:
        if c[1] not in best or (c[0][0], -c[3]["sim"]) < (best[c[1]][0][0], -best[c[1]][3]["sim"]):
            best[c[1]] = c
    for i, (j, r) in list(pair_k.items()):
        b = best[i]
        if b[2] != j and b[0][0] <= -sum(bool(kbt[i][f] and pdf[j][f] and kbt[i][f] == pdf[j][f]) for f in ("ex", "ds")) \
                and b[3]["sim"] > r["sim"] + 0.1:
            if pair_p.get(j) == i:
                del pair_p[j]
            pair_k[i] = (b[2], b[3]); dup.add(i)

    report = {"version": 2, "pages": a.pages, "manifest": a.manifest, "kb_files": [m["file"] for m in man], "tables": [],
              "pdf_only": [], "pdf_unparsed": [{"src": t["src"], "pages": t["pages"], "header": t["hdr"][:12], "n_rows": len(t["recs"]),
                                                "ex": t["ex"], "ds": t["ds"],
                                                "reason": "vertically centred cells" if t["centered"] else "no record lines"}
                                               for t in unparsed]}
    for i, k in enumerate(kbt):
        ent = {"file": k["file"], "line": k["line"], "n_rows": len(k["rows"]), "header": " | ".join(k["header"])[:120],
               "ex": k["ex"], "ds": k["ds"]}
        if not k["parseable"]:
            ent["status"] = "UNPARSEABLE"
        elif i not in pair_k:
            ent["status"] = "NO_PDF"
        else:
            j, r = pair_k[i]
            p = pdf[j]
            lo, hi = k["m"]["lo"], k["m"]["hi"]
            diffs, oor = [], []
            pn = [x["n"] for x in p["rows"]]
            for d in r["diffs"]:          # KB rows beyond a page range that cuts the PDF table are not diffs
                if not full and d["type"] == "KB_ROW_UNMATCHED" and \
                        ((int(d["kb_row"]) < min(pn) and p["pages"][0] == lo) or (int(d["kb_row"]) > max(pn) and p["pages"][-1] == hi)):
                    oor.append(int(d["kb_row"])); continue
                diffs.append(d)
            subset = i in dup and diffs and all(d["type"] == "PDF_ROW_MISSING" for d in diffs)
            ent.update({"status": "OK_SUBSET" if subset else ("DIFF" if diffs else "OK"), "kb_duplicate": i in dup,
                        "pdf_src": p["src"], "pdf_pages": p["pages"], "pdf_ex": p["ex"], "pdf_ds": p["ds"], "pdf_rows": len(p["rows"]),
                        "pdf_no_row_header": p["no_row_hdr"], "pdf_rows_centred_after_page_break": p["pre_attached"], "orphan_reading": r.get("orphan_reading"), "cells_compared": r["cells"], "ws_only_cells": r["ws_only"], "rows_renumbered": r["renumbered"],
                        "sim": round(r["sim"], 3), "rows_out_of_page_range": oor, "diffs": diffs})
        report["tables"].append(ent)
    for j, p in enumerate(pdf):
        if j not in pair_p:
            report["pdf_only"].append({"src": p["src"], "pages": p["pages"], "ex": p["ex"], "ds": p["ds"], "sec": p["sec"],
                                       "header": " ".join(p["hdr"])[:120], "n_rows": len(p["rows"])})

    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    C = collections.Counter(t["status"] for t in report["tables"])
    print(f"PDF tables parsed: {len(pdf)} (+{len(unparsed)} unparsed); KB tables: {len(kbt)}; status: {dict(C)}; "
          f"PDF_ONLY: {len(report['pdf_only'])}; cells compared: {sum(t.get('cells_compared', 0) for t in report['tables'])}; "
          f"diffs: {sum(len(t.get('diffs', [])) for t in report['tables'])}")
    if not full:
        for t in report["tables"]:
            if t["status"] not in ("OK", "UNPARSEABLE"):
                print(f"  {t['status']:<11} {t['file']}:{t['line']} rows={t['n_rows']} ex={t['ex']} ds={t['ds']} -> {t.get('pdf_pages')} {t['header'][:50]}")
                for d in t.get("diffs", [])[:8]:
                    print("      ", d)
        for p in report["pdf_only"]:
            print("  PDF_ONLY   ", p)
        for p in report["pdf_unparsed"]:
            print("  PDF_UNPARSED (manual census)", p)
    rc = 1 if (C["DIFF"] or C["NO_PDF"] or report["pdf_only"]) else 0
    if a.baseline:
        base = json.load(open(a.baseline, encoding="utf-8"))
        same = all(base.get(x) == report[x] for x in ("tables", "pdf_only", "pdf_unparsed"))
        print(f"BASELINE {a.baseline}: {'identical' if same else 'DIFFERS'}")
        if not same:
            bt = {(t["file"], t["line"]): t for t in base["tables"]}
            for t in report["tables"]:
                b = bt.get((t["file"], t["line"]))
                if b != t:
                    new = [d for d in t.get("diffs", []) if d not in (b or {}).get("diffs", [])]
                    print("  CHANGED", t["file"], t["line"], t["status"], new[:5])
            if base["pdf_only"] != report["pdf_only"]:
                print("  CHANGED pdf_only", [p for p in report["pdf_only"] if p not in base["pdf_only"]][:5])
        rc = 0 if same else 1
    print("RESULT:", "RED" if rc else "GREEN")
    sys.exit(rc)

if __name__ == "__main__":
    main()
