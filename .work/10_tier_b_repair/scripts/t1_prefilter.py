#!/usr/bin/env python3
"""T1.1 deterministic prefilter (PLAN §4 T1.1, §5.0, B5). Read-only on KB / archive.
One row per §5.0 gap atom (1,459) + manual scope items. Per atom: fingerprint hit location (file:line, inside the
target section or not), spec-row compare vs domains/XX/spec.md (name/label/type/core, B5), census row status
(table_census.py, Row-style example tables only), primary KB unit, PDF page, prefilter_class (mutually exclusive,
priority order PRIO) and prefilter_suggest (a hint for T1.2; every atom still gets an LLM class).
No PDF verbatim is written (CDISC copyright; work/pdf_pages and pdf_atoms are gitignored).
Usage (repo root):
  python3 -I .work/10_tier_b_repair/scripts/t1_prefilter.py            # runs census units, writes work/triage_prefilter.jsonl
  python3 -I .work/10_tier_b_repair/scripts/t1_prefilter.py --no-census-run   # reuse work/census_t1/*.json
"""
import argparse, bisect, collections, glob, json, os, re, subprocess, sys, unicodedata

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
TB = f"{ROOT}/.work/10_tier_b_repair"
W = f"{TB}/work"
sys.path.insert(0, f"{TB}/scripts")          # -I drops the script dir from sys.path
from fp_match import norm, norm_pdf          # noqa: E402  (verified T0.4 normaliser; do not fork)

TERMINAL = {"EXACT", "EQUIVALENT", "INTENTIONAL_EXCLUDE", "ATOM_ERR", "PDF_TYPO", "FIGURE_DEFERRED"}
ISSUE5_MAIN = ("ig34", "§6.3.5.9.3 Relating PP Records to PC Records")
SPEC_CORE = ("Req", "Exp", "Perm")
MIN_FP_LEN = 40                               # shorter normalised verbatims hit trivially -> no PRESENT suggestion
PRIO = ["FIGURE", "SPEC_HEADER", "SPEC_MATCH", "SPEC_MISMATCH", "CENSUS_DIFF", "FP_HIT_SECTION",
        "FP_HIT_FILE_OUTSIDE_SECTION", "FP_HIT_SHORT", "CENSUS_OK", "FP_HIT_ELSEWHERE", "SPEC_NOT_FOUND",
        "NO_TARGET", "ATOM_NOT_ON_PAGE", "NO_HIT"]
SUGGEST = {"FIGURE": "FIGURE", "SPEC_HEADER": "IE_CAND", "SPEC_MATCH": "IE_CAND", "SPEC_MISMATCH": "VALUE_DIFF",
           "CENSUS_DIFF": "VALUE_DIFF", "FP_HIT_SECTION": "PRESENT", "FP_HIT_FILE_OUTSIDE_SECTION": "RELOCATE",
           "CENSUS_OK": "PRESENT", "FP_HIT_ELSEWHERE": "RELOCATE", "NO_TARGET": "LOCATE",
           "ATOM_NOT_ON_PAGE": "ATOM_ERR"}

def lj(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]

def ws(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s)).strip()

def cells_of(v):
    v = v.strip()
    if v.startswith("|"): v = v[1:]
    if v.endswith("|"): v = v[:-1]
    return [ws(c) for c in v.split("|")]

def is_spec(a):  # identical to t0_inventory.kind()=="spec" so the 452 stays comparable
    v = a["verbatim"].strip().strip("|").strip(); cells = [x.strip() for x in v.split("|")]
    return (a["atom_type"] == "TABLE_HEADER" and "Variable Label" in v) or \
           (a["atom_type"] == "TABLE_ROW" and bool(cells) and cells[-1] in SPEC_CORE)

# ── KB index: per-file normalised text with offset -> line map ───────────────────────────────────────────
class KBFile:
    def __init__(self, path, rel):
        self.rel = rel
        raw = open(path, encoding="utf-8").read()
        self.lines = raw.split("\n")
        parts, self.starts, self.lno, pos = [], [], [], 0
        for i, ln in enumerate(self.lines, 1):
            n = norm(ln)
            if not n: continue
            self.starts.append(pos); self.lno.append(i); parts.append(n); pos += len(n) + 1
        self.text = " ".join(parts)
        self.exact = self.text == norm(raw)
        self.heads = [(i, len(m.group(1)), m.group(2).strip()) for i, ln in enumerate(self.lines, 1)
                      for m in [re.match(r"^(#{1,6})\s+(.*)$", ln)] if m]

    def line_at(self, off):
        return self.lno[bisect.bisect_right(self.starts, off) - 1]

    def find_all(self, v):
        out, i = [], self.text.find(v)
        while i >= 0:
            out.append(self.line_at(i)); i = self.text.find(v, i + 1)
        return out

    def section_range(self, num):
        """[[start, end], ...] for every heading whose text starts with section number `num` (e.g. 4.5.1.2);
        a number can head several KB sections (e.g. two '§7.2.2.1 Trial Elements Issues – ...' headings)."""
        if not num: return None
        out = []
        for j, (ln, lvl, txt) in enumerate(self.heads):
            if re.match(rf"^(§\s*)?{re.escape(num)}(?![\d.])", txt):
                end = next((l2 - 1 for l2, lv2, _ in self.heads[j + 1:] if lv2 <= lvl), len(self.lines))
                out.append([ln, end])
        return out or None

def sec_num(sk):
    m = re.match(r"^§\s*(\d+(?:\.\d+)*)", sk)
    return m.group(1) if m else None

def dom_abbr(sk, dom_dirs):
    for m in re.finditer(r"\(([A-Z]{2,7})\)|^([A-Z]{2,7})\s+[–-]|^§[\d.]+\s+\[?([A-Z]{2,7})\s+[–-]", sk):
        x = next(g for g in m.groups() if g)
        if x in dom_dirs: return x
    m = re.search(r"\(([A-Z]{2,7})\)", sk)
    return m.group(1) if m and m.group(1) in dom_dirs else None

# ── spec.md parser ────────────────────────────────────────────────────────────────────────────────────────
def parse_spec(path):
    out, cur = {}, None
    for i, ln in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        m = re.match(r"^###\s+(\S+)\s*$", ln)
        if m: cur = {"line": i}; out.setdefault(m.group(1), cur); continue
        m = re.match(r"^- \*\*(Label|Type|Core):\*\*\s?(.*)$", ln)
        if m and cur is not None: cur[m.group(1).lower()] = ws(m.group(2))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=f"{W}/triage_prefilter.jsonl")
    ap.add_argument("--census-dir", default=f"{W}/census_t1")
    ap.add_argument("--no-census-run", action="store_true")
    a = ap.parse_args()
    for p in (a.out, a.census_dir):
        if os.path.abspath(p).startswith((f"{ROOT}/archive", f"{ROOT}/knowledge_base", f"{ROOT}/releases")):
            sys.exit(f"refuse to write {p}")

    atoms = lj(f"{W}/pdf_atoms.jsonl")
    ledger = {e["pdf_atom_id"]: e for e in lj(f"{W}/coverage_ledger.wc.jsonl")}
    md_file = {m["atom_id"]: m.get("file", "") for m in lj(f"{W}/md_atoms.jsonl")}
    sec_rows = {(r["source"], r["section_key"]): r for r in lj(f"{W}/section_coverage.wc.jsonl")}
    inv = lj(f"{TB}/inventory.jsonl")
    scope = {(r["source"], r["section_key"]) for r in inv} | {ISSUE5_MAIN}
    kbf = {}
    for p in sorted(glob.glob(f"{ROOT}/knowledge_base/**/*.md", recursive=True)):
        rel = "knowledge_base/" + os.path.relpath(p, f"{ROOT}/knowledge_base")
        kbf[rel] = KBFile(p, rel)
    bad = [r for r, f in kbf.items() if not f.exact]
    print(f"KB files {len(kbf)}; per-line index == norm(whole file): {len(kbf) - len(bad)}  (inexact: {bad[:5]})")
    dom_dirs = {os.path.basename(d) for d in glob.glob(f"{ROOT}/knowledge_base/domains/*") if os.path.isdir(d)}
    specs = {d: parse_spec(f"{ROOT}/knowledge_base/domains/{d}/spec.md") for d in dom_dirs
             if os.path.exists(f"{ROOT}/knowledge_base/domains/{d}/spec.md")}
    page_cache = {}
    def page_txt(src, p):
        if (src, p) not in page_cache:
            fp = f"{W}/pdf_pages/{src}_p{p:04d}.txt"
            page_cache[(src, p)] = open(fp, encoding="utf-8").read() if os.path.exists(fp) else ""
        return page_cache[(src, p)]

    # gap atoms + table context (last TABLE_HEADER of the same source in atom order; sub-section keys like
    # "... — Example 3" split one PDF table run, so do not key by section)
    gap, last_hdr, sec_all = [], {}, collections.defaultdict(list)
    for at in atoms:
        src = at["atom_id"].split("_")[0]; key = (src, at["parent_section"])
        sec_all[key].append(at)
        if at["atom_type"] == "TABLE_HEADER": last_hdr[src] = at
        if at["atom_type"] == "HEADING" or key not in scope: continue
        e = ledger.get(at["atom_id"]) or {}
        if e.get("verdict", "MISSING") in TERMINAL: continue
        gap.append((at, e, last_hdr.get(src) if at["atom_type"] == "TABLE_ROW" else None))
    assert len(gap) == 1459, len(gap)

    # primary KB unit per section (lane / batch key). Rule: domain dir named in the section key > file most used by
    # the section's ledger md_atom_ids among md_target_files > first md_target_file > parent section's unit.
    def unit_of(f):
        p = f.split("/"); return "/".join(p[:3]) if len(p) > 2 and p[1] == "domains" else f
    prim_memo = {}
    sec_tg = collections.defaultdict(set)                  # ledger-derived targets per section (fallback)
    for at, e, _ in gap:
        sec_tg[(at["atom_id"].split("_")[0], at["parent_section"])] |= {md_file.get(m, "") for m in e.get("md_atom_ids", [])} - {""}
    def primary(key):
        if key in prim_memo: return prim_memo[key]
        src, sk = key; r = sec_rows.get(key) or {}
        tg = r.get("md_target_files") or sorted(sec_tg.get(key, ()))
        if not tg and " — " in sk:                         # "§x.y Title — Example 3" -> parent "§x.y Title"
            pk = (src, sk.split(" — ")[0])
            if pk in sec_rows or pk in sec_tg: prim_memo[key] = primary(pk); return prim_memo[key]
        d = dom_abbr(sk, dom_dirs)
        res = f"knowledge_base/domains/{d}" if d else None
        if not res and tg:
            c = collections.Counter(unit_of(md_file.get(m, "")) for at in sec_all[key]
                                    for m in (ledger.get(at["atom_id"]) or {}).get("md_atom_ids", []) if md_file.get(m))
            c = {u: n for u, n in c.items() if u in {unit_of(t) for t in tg}}
            res = max(c, key=lambda u: (c[u], -[unit_of(t) for t in tg].index(u))) if c else unit_of(tg[0])
        if not res:
            num = sec_num(sk)
            while num and "." in num and not res:
                num = num.rsplit(".", 1)[0]
                pk = next((k for k in sec_rows if k[0] == src and sec_num(k[1]) == num), None)
                if pk: res = primary(pk)
        prim_memo[key] = res
        return res

    # ── census units: Row-style example table gap atoms, grouped by primary unit ─────────────────────────
    def row_style(at, hdr):
        return at["atom_type"] == "TABLE_ROW" and hdr is not None and cells_of(hdr["verbatim"])[:1] == ["Row"] \
            and bool(re.fullmatch(r"\d+", cells_of(at["verbatim"])[0] or ""))
    cu = collections.defaultdict(lambda: {"pages": set(), "files": set()})
    for at, e, hdr in gap:
        if not row_style(at, hdr): continue
        key = (at["atom_id"].split("_")[0], at["parent_section"]); u = primary(key)
        if not u: continue
        r = sec_rows.get(key) or {}
        lo, hi = (r.get("pdf_page_range") or [at["page"], at["page"]])
        cu[(key[0], u)]["pages"] |= {lo, hi, at["page"]}
        files = [f for f in kbf if unit_of(f) == u] if u.startswith("knowledge_base/domains/") else [u]
        cu[(key[0], u)]["files"] |= {f for f in files if not f.endswith("/spec.md")}
    os.makedirs(a.census_dir, exist_ok=True)
    census = {}
    for (src, u), d in sorted(cu.items()):
        name = f"{src}_{u.replace('knowledge_base/', '').replace('/', '_').replace('.md', '')}"
        outp = f"{a.census_dir}/{name}.json"
        pages = f"{src}:{min(d['pages'])}-{max(d['pages']) + 1}"
        if not a.no_census_run:
            r = subprocess.run([sys.executable, "-I", f"{TB}/scripts/table_census.py", "--pages", pages, "--kb",
                                *sorted(d["files"]), "--out", outp], cwd=ROOT, capture_output=True, text=True)
            if r.returncode not in (0, 1): print("CENSUS ERROR", name, r.stderr[-400:]); continue
        if os.path.exists(outp): census[(src, u)] = json.load(open(outp, encoding="utf-8"))
    print(f"census units run: {len(census)}/{len(cu)}  -> {a.census_dir}")

    bpcpp = json.load(open(f"{W}/census_BPCPP.json", encoding="utf-8"))   # T0.3b/T0.4-verified census, p275-284
    def census_row(src, u, at, hdr, tgt_files):
        """All KB tables (same page + header prefix + row n) are candidates. Several tables can share page and header
        (p278: PC/examples.md 36/72/98), so pick the candidate whose KB row n agrees best with the atom's cells;
        a tie between candidates with different row status -> row_status AMBIGUOUS (no class, no suggestion)."""
        rep = bpcpp if (src == "ig34" and 275 <= at["page"] <= 284) else census.get((src, u))
        if not rep: return None
        ac = cells_of(at["verbatim"]); n = int(ac[0]); hc = [norm(c) for c in cells_of(hdr["verbatim"])]
        aset = collections.Counter(norm(c) for c in ac if norm(c))
        cands = []
        for t in rep["tables"]:
            if at["page"] not in (t.get("pdf_pages") or []): continue
            kh = [norm(c) for c in t["header"].split(" | ")]
            m = min(len(kh), len(hc)) - 1                         # KB header string is cut at 120 chars
            if m < 2 or kh[:m] != hc[:m]: continue
            if n > (t.get("pdf_rows") or 0) and n not in {dd["row"] for dd in t.get("diffs", [])}: continue
            kf = kbf.get(t["file"]); kl = None
            if kf:   # KB row n of this table: scan the table block below its header line
                for li in range(t["line"] + 1, min(len(kf.lines), t["line"] + 400)):
                    ln = kf.lines[li]
                    if not ln.startswith("|"): break
                    if cells_of(ln)[:1] == [str(n)]: kl = li + 1; break
            kset = collections.Counter(norm(c) for c in cells_of(kf.lines[kl - 1]) if norm(c)) if kl else collections.Counter()
            score = sum((aset & kset).values()) / max(1, sum(aset.values()))
            df = [dd for dd in t.get("diffs", []) if dd.get("row") == n]
            cands.append({"file": t["file"], "table_line": t["line"], "kb_row_line": kl, "table_status": t["status"], "row": n,
                          "row_status": "DIFF" if df else "OK", "diff": df[0] if df else None,
                          "table_modes": sorted((t.get("row_modes") or {}).keys()), "cell_agreement": round(score, 3)})
        if not cands: return None
        # prefer the copy in the atom's own target files (a PDF table can have several KB copies, e.g. p277 pp.xpt in
        # PP/examples.md:112 (OK) and PC/assumptions.md:86 (DIFF)); then best cell agreement
        cands.sort(key=lambda c: (c["file"] not in tgt_files, -c["cell_agreement"]))
        k0 = (cands[0]["file"] not in tgt_files, cands[0]["cell_agreement"])
        ties = [c for c in cands if (c["file"] not in tgt_files, c["cell_agreement"]) == k0]
        best = dict(cands[0]); best["n_candidates"] = len(cands)
        if len({c["row_status"] for c in ties}) > 1: best["row_status"] = "AMBIGUOUS"
        if len(cands) > 1:
            best["other_candidates"] = [f"{c['file']}:{c['table_line']} {c['row_status']}" for c in cands[1:4]]
        return best

    # ── per atom ────────────────────────────────────────────────────────────────────────────────────────
    rows = []
    for at, e, hdr in gap:
        src = at["atom_id"].split("_")[0]; key = (src, at["parent_section"]); pg = at.get("page")
        r = sec_rows.get(key) or {}
        tg = sorted({md_file.get(m, "") for m in e.get("md_atom_ids", [])} - {""} | set(r.get("md_target_files") or []))
        u = primary(key)
        num = sec_num(at["parent_section"])
        sect_ranges = {f: kbf[f].section_range(num) for f in tg if f in kbf}
        v = norm(at["verbatim"])
        hits = {f: kf.find_all(v) for f, kf in kbf.items()} if v else {}
        hits = {f: ls for f, ls in hits.items() if ls}
        n_hits = sum(len(x) for x in hits.values())
        hit_t = next(((f, ls) for f, ls in hits.items() if f in tg), None)
        in_sec = None
        if hit_t:
            rg = sect_ranges.get(hit_t[0])
            in_sec_lines = [l for l in hit_t[1] if rg and any(a0 <= l <= a1 for a0, a1 in rg)]
            in_sec = bool(in_sec_lines) if rg else None          # None = no numbered heading -> file-level only
            hit_t_loc = f"{hit_t[0]}:{(in_sec_lines or hit_t[1])[0]}"
        else:
            hit_t_loc = None
        hit_any_loc = None if not hits else (hit_t_loc or f"{next(iter(hits))}:{next(iter(hits.values()))[0]}")
        pair = norm_pdf(page_txt(src, pg) + "\n" + page_txt(src, pg + 1)) if pg else ""
        in_pdf = bool(v) and v in pair
        alnum = lambda x: re.sub(r"[^0-9a-z]", "", x)            # line-wrap '--\nSTRESN' etc. defeat norm_pdf
        in_pdf_loose = bool(v) and alnum(v) in alnum(pair)
        spec = spec_detail = None
        if is_spec(at):
            if at["atom_type"] == "TABLE_HEADER":
                spec = "HEADER"
            else:
                c = cells_of(at["verbatim"]); name = c[0]
                d = dom_abbr(at["parent_section"], dom_dirs)
                cand = [d] if d else []
                cand += sorted(x for x in specs if name.startswith(x) and x not in cand)
                found = next(((x, specs[x][name]) for x in cand if x in specs and name in specs[x]), None)
                via = None if not found else ("section_domain" if found[0] == d else "name_prefix")
                if not found:   # fallback: any spec.md, prefer same label (flagged: section's own domain lacks it)
                    alls = sorted((x, specs[x][name]) for x in specs if name in specs[x])
                    found = next(((x, sx) for x, sx in alls if len(c) > 1 and sx.get("label") == c[1]), alls[0] if alls else None)
                    via = "any_spec_fallback" if found else None
                rowline = next((ws(l) for l in (page_txt(src, pg) + "\n" + page_txt(src, pg + 1)).split("\n")
                                if re.match(rf"^\s*{re.escape(name)}\s", l)), "") if pg else ""
                if not found:
                    spec = "NOT_FOUND"; spec_detail = {"name": name, "domains_tried": cand,
                                                       "name_on_pdf_page": bool(rowline)}
                else:
                    dd, s = found
                    av = {"name": name, "label": c[1] if len(c) > 1 else None, "type": c[2] if len(c) > 2 else None,
                          "core": c[-1]}
                    mm = [f for f in ("label", "type", "core") if av[f] is not None and av[f] != s.get(f)]
                    # which value is on the PDF row line (the line starting with the variable name)
                    def on(x):
                        return bool(x) and re.search(rf"(?<!\S){re.escape(x)}(?!\S)", rowline) is not None
                    sup = {f: {"atom": av[f], "kb": s.get(f),
                               "on_pdf_row_line": ("no_row_line" if not rowline else "both" if on(av[f]) and on(s.get(f)) else
                                                   "atom" if on(av[f]) else "kb" if on(s.get(f)) else "neither")}
                           for f in mm}
                    spec = "MATCH" if not mm else f"MISMATCH({','.join(mm)})"
                    spec_detail = {"spec_loc": f"knowledge_base/domains/{dd}/spec.md:{s['line']}", "fields": sup or None,
                                   "match_via": via, "section_domain": d}
        cen = census_row(src, u, at, hdr, set(tg)) if (u and row_style(at, hdr)) else None
        # class (first true in PRIO)
        vlen = len(v)
        flags = {
            "FIGURE": at["atom_type"] == "FIGURE",
            "SPEC_HEADER": spec == "HEADER",
            "SPEC_MATCH": spec == "MATCH",
            "SPEC_MISMATCH": bool(spec and spec.startswith("MISMATCH")),
            "CENSUS_DIFF": bool(cen and cen["row_status"] == "DIFF"),
            "FP_HIT_SECTION": bool(hit_t) and in_sec is not False and vlen >= MIN_FP_LEN,
            "FP_HIT_FILE_OUTSIDE_SECTION": bool(hit_t) and in_sec is False and vlen >= MIN_FP_LEN,
            "FP_HIT_SHORT": bool(hit_t) and vlen < MIN_FP_LEN,
            "CENSUS_OK": bool(cen and cen["row_status"] == "OK"),
            "FP_HIT_ELSEWHERE": bool(hits) and not hit_t,
            "SPEC_NOT_FOUND": spec == "NOT_FOUND",
            "NO_TARGET": not tg,
            "ATOM_NOT_ON_PAGE": at["atom_type"] in ("SENTENCE", "LIST_ITEM", "NOTE") and not in_pdf_loose,
            "NO_HIT": True,
        }
        cls = next(k for k in PRIO if flags[k])
        sug = SUGGEST.get(cls)
        if cls == "CENSUS_OK" and cen["table_modes"] != ["columns"]: sug = None      # multiset/order blind spots
        if cls == "FP_HIT_ELSEWHERE" and vlen < MIN_FP_LEN: sug = None
        if at["atom_type"] == "TABLE_HEADER" and sug in ("PRESENT", "RELOCATE"): sug = None     # generic headers
        if cls == "FP_HIT_ELSEWHERE" and all(f.startswith(("knowledge_base/terminology/", "knowledge_base/VARIABLE_INDEX",
                                                            "knowledge_base/INDEX")) for f in hits): sug = None   # calibration C05
        if cls == "SPEC_MATCH" and spec_detail.get("match_via") == "any_spec_fallback": sug = None
        if cls == "SPEC_MISMATCH" and all(x["on_pdf_row_line"] == "kb" for x in spec_detail["fields"].values()): sug = "ATOM_ERR"
        pdf_typo = False   # set by T1.2 writer; only MANUAL_02 is pre-flagged (T1.2 class set has no PDF_TYPO)
        rows.append({"atom_id": at["atom_id"], "manual": False, "source": src, "section_key": at["parent_section"],
                     "atom_type": at["atom_type"], "ledger_verdict": e.get("verdict", "MISSING"), "pdf_page": pg,
                     "primary_unit": u, "targets": tg, "target_section_lines": {f: rg for f, rg in sect_ranges.items() if rg},
                     "fp": {"v_len": vlen, "n_hits_kb": n_hits, "hit_target_loc": hit_t_loc, "hit_in_section": in_sec,
                            "hit_any_loc": hit_any_loc, "hit_files": sorted(hits)[:6]},
                     "in_pdf_page": in_pdf, "in_pdf_page_loose": in_pdf_loose, "spec_row": spec, "spec_detail": spec_detail, "census": cen,
                     "prefilter_class": cls, "prefilter_suggest": sug, "pdf_typo_suspect": pdf_typo})

    # ── manual scope items (user ack 2026-11-25, t0_user_ack.md) ─────────────────────────────────────────
    rows.append({"atom_id": "MANUAL_01", "manual": True, "source": "ig34", "section_key": "§6.3.5.9.2 [PP Examples] Example 1",
                 "atom_type": "TABLE", "pdf_page": 273, "primary_unit": "knowledge_base/domains/PP",
                 "targets": ["knowledge_base/domains/PP/examples.md"], "kb_loc": "knowledge_base/domains/PP/examples.md:16",
                 "issue": "KB Ex1 table (24 rows) looks like PDF Example 3 (DRUGA_DAY1 ...); PDF p273 Ex1 (DAY1_PAR ...) PDF_ONLY in census",
                 "evidence": "t0_mutation.md §4; work/scratch/census_p272_275.json", "prefilter_class": "MANUAL",
                 "prefilter_suggest": "VALUE_DIFF", "pdf_typo_suspect": False})
    rows.append({"atom_id": "MANUAL_02", "manual": True, "source": "ig34",
                 "section_key": "§6.3.5.9.3 Relating PP Records to PC Records — Example 1", "atom_type": "TEXT_VS_TABLE",
                 "pdf_page": 277, "primary_unit": "knowledge_base/domains/PC",
                 "targets": ["knowledge_base/domains/PC/examples.md", "knowledge_base/domains/PP/examples.md"],
                 "kb_loc": "knowledge_base/domains/PC/examples.md:36",
                 "issue": "p277 text: Rows 14-26 RELID '2', PPGRPID DY8DRGX; p278 table: rows 14-26 RELID 1, row 26 DY1DRGX; KB copies both",
                 "evidence": "t0_mutation.md §4", "prefilter_class": "MANUAL", "prefilter_suggest": "VALUE_DIFF",
                 "pdf_typo_suspect": True})

    with open(a.out, "w", encoding="utf-8") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # ── summary + self-checks ───────────────────────────────────────────────────────────────────────────
    C = collections.Counter
    auto = [r for r in rows if not r["manual"]]
    print(f"rows: {len(rows)} (gap atoms {len(auto)} + manual {len(rows) - len(auto)}) -> {a.out}")
    cc = C(r["prefilter_class"] for r in rows)
    print("prefilter_class (priority order, mutually exclusive):")
    for k in PRIO + ["MANUAL"]: print(f"  {k:30s} {cc.get(k, 0)}")
    assert sum(cc.values()) == len(rows)
    print("prefilter_suggest:", dict(C(r["prefilter_suggest"] for r in rows).most_common()))
    print("spec_row:", dict(C((r.get("spec_row") or "-").split("(")[0] for r in auto)),
          " mismatch fields:", dict(C(r["spec_row"] for r in auto if (r.get("spec_row") or "").startswith("MISMATCH"))))
    print("census rows attached:", sum(1 for r in auto if r["census"]), dict(C(r["census"]["row_status"] for r in auto if r["census"])),
          " multi-candidate:", sum(1 for r in auto if r["census"] and r["census"]["n_candidates"] > 1))
    print("spec MATCH via:", dict(C(r["spec_detail"]["match_via"] for r in auto if r.get("spec_row") == "MATCH")))
    print("pdf_typo_suspect:", sum(r["pdf_typo_suspect"] for r in rows))
    # reproduce inventory.md probe numbers on the 1,389 current-TierB subset (inventory uses old norm + section targets)
    cur = {(r["source"], r["section_key"]) for r in inv if r["verdict_current"] in ("SIBLING_DROPPED", "CONTENT_TRUNCATED")}
    inv_abs = {i for r in inv if (r["source"], r["section_key"]) in cur for i in r["probe_absent_atom_ids"]}
    sub = [r for r in auto if (r["source"], r["section_key"]) in cur]
    sid = {r["atom_id"] for r in sub}
    print(f"current TierB subset: {len(sub)} (expect 1389); inventory probe_absent {len(inv_abs)} (expect 944), "
          f"⊆ subset: {inv_abs <= sid}; spec among inv absent: {sum(1 for r in sub if r['atom_id'] in inv_abs and r['spec_row'])} (expect 452)")
    print(f"  this probe (fp_match norm, ledger+section targets): hit_target {sum(1 for r in sub if r['fp']['hit_target_loc'])}, "
          f"hit_any {sum(1 for r in sub if r['fp']['hit_any_loc'])}, absent {sum(1 for r in sub if not r['fp']['hit_any_loc'])}; "
          f"absent ⊆ inventory absent: {({r['atom_id'] for r in sub if not r['fp']['hit_any_loc']}) <= inv_abs}")

if __name__ == "__main__":
    main()
