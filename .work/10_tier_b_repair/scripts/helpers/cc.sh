census_check() {  # report baseline kind args...  kind: cell FILE LINE KBROW COL | row FILE LINE KBROW | pdfonly DS EX |
                  #   only1 FILE LINE COL KBVAL | pair FILE LINE PDFEX ONLY_DS ONLY_EX
  $PY - "$@" <<'EOF'
import json, sys
rep, base, kind, *a = sys.argv[1:]
R, B = json.load(open(rep)), json.load(open(base))
def tab(r, f, ln): return next((t for t in r["tables"] if t["file"].endswith(f) and t["line"] == int(ln)), None)
if kind == "cell":
    f, ln, row, col = a
    hit = lambda r: [d for d in (tab(r, f, ln) or {}).get("diffs", []) if d.get("kb_row") == row and d.get("col") == col]
    ok = bool(hit(R)) and not hit(B); print("  assert cell", f, ln, "row", row, col, "->", hit(R)[:1], "| in baseline:", bool(hit(B)))
elif kind == "row":
    f, ln, row = a
    hit = lambda r: [d for d in (tab(r, f, ln) or {}).get("diffs", []) if d.get("kb_row") == row]
    ok = bool(hit(R)) and not hit(B); print("  assert row", f, ln, "row", row, "->", hit(R)[:2], "| in baseline:", bool(hit(B)))
elif kind == "pair":   # real-KB property (no baseline condition): table FILE:LINE pairs with a PDF table of example EX,
    f, ln, ex, ods, oex = a      # and PDF table (ODS, OEX) is PDF_ONLY
    t = tab(R, f, ln) or {}; po = [p for p in R["pdf_only"] if p["ds"] == ods and p["ex"] == oex]
    ok = t.get("pdf_ex") == ex and bool(po)
    print("  assert pair", f, ln, "-> pdf_ex", t.get("pdf_ex"), t.get("pdf_pages"), "| PDF_ONLY", ods, oex, "->", [p["pages"] for p in po])
elif kind == "pdfonly":
    ds, ex = a
    hit = lambda r: [p for p in r["pdf_only"] if p["ds"] == ds and p["ex"] == ex]
    ok = bool(hit(R)) and not hit(B); print("  assert pdf_only", ds, "ex", ex, "->", hit(R)[:1], "| in baseline:", bool(hit(B)))
elif kind == "only1":
    f, ln, col, kv = a
    t = tab(R, f, ln) or {}
    cells = [d for d in t.get("diffs", []) if d["type"] == "CELL" and d["col"] != "Row"]
    unm = [d for d in t.get("diffs", []) if d["type"] in ("KB_ROW_UNMATCHED", "PDF_ROW_MISSING")]
    ok = len(cells) == 1 and cells[0]["col"] == col and cells[0]["kb"] == kv and len(unm) == 1
    print("  assert only1", f, ln, "non-Row cell diffs:", [(d["kb_row"], d["col"], d["kb"], d["pdf"]) for d in cells][:4],
          "| unmatched rows:", [(d["type"], d.get("kb_row"), d.get("pdf_row")) for d in unm])
print("  ASSERT", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
EOF
}
