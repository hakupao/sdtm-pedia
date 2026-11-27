#!/usr/bin/env python3
"""G-TB6 reverse trace: every line added to knowledge_base/ since the pre-T2 baseline must come from the PDF.
Baseline = 302ec4c (parent of the first T2 batch commit 97e1895 B-PCPP; KB identical to 7819398).
Per added line (git diff -U0 <base>..<rev>), first class that applies:
  HEADING_PDF      markdown heading whose text (with / without '§n.n' numbering) is in the PDF
  HEADING_NOT_IN_PDF  heading text not in the PDF (KB structural heading or KB-made label) -> listed for review
  BLANK / STRUCT   blank, table separator, `**x.xpt**` label, '---', code fence, list stub
  MERMAID          line inside a ```mermaid block of the <rev> file (figure redraws; T2 reviewers checked vs PDF figure)
  XREF_D2          '> See [..](x.md) for this text' pointer left where a duplicate was removed (D2) / D7 source line
  KB_NOTE          line of a D6 '> KB note (not in SDTMIG)' blockquote, D7 '> Source text:', U8 '> Class:' / Cross References nav
  PDF_SUBSTR       norm(line minus list marker) ⊂ norm_pdf(source PDF, pages joined by ' ')
  PDF_LOOSE        same after removing spaces around '-' on both sides (PDF text layer '- -TEST', '-- ENRF')
  PDF_SENTENCES    every sentence (>= 4 words) of the line ⊂ PDF (loose)
  PDF_TYPO         line carries a registry kb_text_span for this file (T-n) and the rest is in the PDF / one page pair
  U_RULE           S-CT U5/U6: line with '(XX) Cnnnnn' C-codes; minus the C-codes it is in the PDF / one page pair
  SPEC_FIELD       spec.md '- **Field:** value' line whose value is in the PDF / its tokens on one page pair
  TABLE_TOKENS     table row: all alnum tokens occur on one PDF page pair (cell order/wrap; G-TB4 census owns the values)
  KB_NOTE_SCOPE    line covered by a D6 note's declared scope (KB-written column / KB-authored table / whole KB section / caption)
  PDF_DEHYPH       PDF text-layer line-wrap hyphen ('chara-cters') or '[n]' footnote refs: equal after dropping '-' both sides
  PDF_SEGMENTS     line = 2-3 maximal word runs (>= 5 words each) that are each PDF substrings (page break / footnote between)
  PDF_NEAR         >= 90% of the line's word 6-grams occur in the PDF (listed; NOT counted as traced)
  UNEXPLAINED      listed one by one
Source PDF: model/* -> sv20, else ig34.
Usage: python3 -I .work/10_tier_b_repair/scripts/t3/t3_reverse_trace.py [--base 302ec4c] [--rev HEAD] [--out JSON]
  --rev WORKTREE (T4 W3): diff <base> against the uncommitted working tree and read <rev> files from disk.
"""
import argparse, collections, glob, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t3_common import ROOT, W, lj, norm, norm_pdf

ap = argparse.ArgumentParser()
ap.add_argument("--base", default="302ec4c")
ap.add_argument("--rev", default="HEAD")
ap.add_argument("--out", default=f"{W}/scratch/t3/reverse_trace.json")
a = ap.parse_args()

loose = lambda s: re.sub(r"\s*-\s*", "-", s)
alnum = lambda s: set(re.findall(r"[a-z0-9]+", s))
pages = {}
for src in ("ig34", "sv20"):
    pages[src] = [norm_pdf(open(f, encoding="utf-8").read()) for f in sorted(glob.glob(f"{W}/pdf_pages/{src}_p*.txt"))]
corpus = {s: " ".join(p) for s, p in pages.items()}
corpus_l = {s: loose(c) for s, c in corpus.items()}
pair_toks = {s: [alnum(ps[k] + " " + (ps[k + 1] if k + 1 < len(ps) else "")) for k in range(len(ps))] for s, ps in pages.items()}
grams = {}
REG = collections.defaultdict(list)
for r in lj(f"{W}/t2_pdf_typo_registry.jsonl"):
    REG[r["kb_file"]].append(r)

def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True).stdout

WT = a.rev == "WORKTREE"
show = lambda f: open(f"{ROOT}/{f}", encoding="utf-8").read() if WT else git("show", f"{a.rev}:{f}")
diff = git("diff", "-U0", a.base, "--", "knowledge_base/") if WT else git("diff", "-U0", f"{a.base}..{a.rev}", "--", "knowledge_base/")
added, f, ln = [], None, 0
for l in diff.splitlines():
    if l.startswith("+++ "):
        f = l[6:] if l.startswith("+++ b/") else None
    elif l.startswith("@@"):
        ln = int(re.search(r"\+(\d+)", l).group(1))
    elif l.startswith("+") and f:
        added.append((f, ln, l[1:]))
        ln += 1

ctx = {}
def file_ctx(f):
    """line no -> 'MERMAID' | 'CODE' | 'KB_NOTE' from the <rev> version of f."""
    if f not in ctx:
        m, fence, note = {}, None, False
        for n, l in enumerate(show(f).splitlines(), 1):
            s = l.strip()
            if s.startswith("```"):
                fence = None if fence else ("MERMAID" if s.startswith("```mermaid") else "CODE")
                continue
            if fence:
                m[n] = fence
                continue
            if s.startswith(">"):
                if re.match(r">\s*(KB note \(not in SDTM(?:IG| v2\.0)\)|Source text:|Class:)", s):
                    note = True
                if note:
                    m[n] = "KB_NOTE"
            else:
                note = False
        ctx[f] = m
    return ctx[f]

STRUCT = re.compile(r"^\s*($|(?:\|\s*)+$|#{1,6}\s|\|?\s*:?-{3,}|-{3,}\s*$|```|\*\*[\w.]+\.xpt\*\*\s*$|[-*]\s*$|\d+\.\s*$)")
NAV = re.compile(r"^\s*(\*\*Cross Reference|[-*]\s*\[[^\]]*\]\([^)]*\.md[^)]*\)\s*$|Source: SDTM|(?:[-*]\s*)?>\s*KB note \(not in SDTM(?:IG| v2\.0)\))")
XREF = re.compile(r"^\s*>\s*(?:See|Source text:)\s.*\]\([^)]*\.md")  # D2/D7 dedup pointer to the kept copy
CCODE = re.compile(r"\bC\d{4,6}\b")
LIST = re.compile(r"^\s*(?:[-*+]|\d+[.)]|[a-z][.)]|o)\s+")
FIELD = re.compile(r"^\s*-\s*\*\*([^*]+):\*\*\s*(.*)$")
nl = lambda raw: norm(LIST.sub("", raw, count=1).replace("**", ""))  # drop bold marks so '**X**,' -> 'X,' (norm would leave 'x ,')

def in_pdf(src, v):
    return bool(v) and (v in corpus[src] or loose(v) in corpus_l[src])

def on_pair(src, text):
    t = alnum(text)
    return bool(t) and any(t <= ps for ps in pair_toks[src])

def sentences(t):
    return [s for s in re.split(r"(?<=[.;:])\s+", t) if len(s.split()) >= 4]

corpus_dh = {s_: re.sub(r"\s+", " ", re.sub(r"[\u00b9\u00b2\u00b3]", " ", c)).replace("-", "") for s_, c in corpus_l.items()}
detail_note = {}
D6_SCOPE = re.compile(r"KB note \(not in SDTM(?:IG| v2\.0)\):.*(column is KB-written|table is KB-authored|table below is KB-authored|sub-tables|"
                      r"is a KB summary|entire section|diagram and caption)", re.I)
def d6_scope(f, n):
    """D6 note whose declared scope covers line n: 'X column is KB-written' / 'table is KB-authored' (same table block,
    note directly above the table), 'this entire section … to the end of the file' (any later line), Mermaid 'caption'
    (first non-blank line after the diagram). Returns 'file:line' of the note or None."""
    L = show(f).splitlines()
    j = n - 2
    while j >= 0 and L[j].lstrip().startswith("|"):
        j -= 1
    if L[n - 1].lstrip().startswith("|"):
        while j >= 0 and (not L[j].strip() or L[j].lstrip().startswith(">")):
            if D6_SCOPE.search(L[j]) and not re.search(r"entire section|caption", L[j]):
                return f"{f}:{j + 1}"
            j -= 1
    for k in range(n - 2, -1, -1):
        if D6_SCOPE.search(L[k]) and "entire section" in L[k] and "end of the file" in L[k]:
            return f"{f}:{k + 1}"
    if L[n - 1].lstrip().startswith("|"):  # 'In the timing sub-tables, the Notes column is KB-written': until next '## '
        for k in range(n - 2, -1, -1):
            if L[k].startswith("## "):
                break
            if D6_SCOPE.search(L[k]) and "sub-tables" in L[k]:
                return f"{f}:{k + 1}"
    k = n - 2
    while k >= 0 and not L[k].strip():
        k -= 1
    if k >= 0 and L[k].strip() == "```":
        for m in range(k - 1, max(-1, k - 80), -1):
            if D6_SCOPE.search(L[m]) and "caption" in L[m]:
                return f"{f}:{m + 1}"
    return None

def segments(src, v, min_run=5, max_runs=3):
    """line = <= 3 maximal word runs, each >= 5 words and each a PDF substring (paragraph split by a page break,
    footnote or interposed table in the text layer)."""
    w, i, runs = v.split(), 0, 0
    while i < len(w):
        j = i + 1
        while j <= len(w) and " ".join(w[i:j]) in corpus[src]:
            j += 1
        if j - 1 - i < min_run:
            return False
        runs, i = runs + 1, j - 1
    return 1 < runs <= max_runs

def near(src, v, k=6):
    w = v.split()
    if len(w) < k + 2:
        return False
    if src not in grams:
        cw = corpus[src].split()
        grams[src] = {" ".join(cw[j:j + k]) for j in range(len(cw) - k + 1)}
    g = [" ".join(w[j:j + k]) for j in range(len(w) - k + 1)]
    return sum(x in grams[src] for x in g) / len(g) >= 0.9

# T4 W3 (主控决定 4): explicit exemption list for the 5 A5-14 '> Note:' lines, anchored by file + full line text
NOTE_EX = {(e["file"], e["text"]) for e in json.load(open(f"{W}/t4_note_exempt.json", encoding="utf-8"))["entries"]}
NOTE_EX_HIT = collections.Counter()
res, detail = collections.Counter(), collections.defaultdict(list)
for f, n, raw in added:
    src = "sv20" if f.startswith("knowledge_base/model/") else "ig34"
    c = file_ctx(f).get(n)
    v = nl(raw)
    if not raw.strip():
        cls = "BLANK"
    elif c == "MERMAID":
        cls = "MERMAID"
    elif re.match(r"^\s*#{1,6}\s", raw):
        h = re.sub(r"^\s*#{1,6}\s*", "", raw).replace("**", "")
        cands = {nl(h), nl(h.lstrip("§")), nl(re.sub(r"^§?[\d.]+\s*", "", h)), nl(re.sub(r"\s*\(p\.?\s*\d+\)\s*$", "", h))}
        cls = "HEADING_PDF" if any(x and in_pdf(src, x) for x in cands) else "HEADING_NOT_IN_PDF"
    elif STRUCT.match(raw):
        cls = "STRUCT"
    elif in_pdf(src, v):
        cls = "PDF_SUBSTR" if v in corpus[src] else "PDF_LOOSE"
    elif XREF.match(raw):
        cls = "XREF_D2"
    elif c == "KB_NOTE" or NAV.match(raw):
        cls = "KB_NOTE"
    elif (f, raw) in NOTE_EX:
        cls = "NOTE_EXEMPT"
        NOTE_EX_HIT[(f, raw)] += 1
    elif re.match(r"^\s*-\s*\*\*Controlled Terms:\*\*\s*\*\s*$", raw):
        cls = "U_RULE"  # U2: CT column '*' copied from PDF
    elif sentences(v) and all(in_pdf(src, s) for s in sentences(v)):
        cls = "PDF_SENTENCES"
    else:
        cls, is_row = None, raw.lstrip().startswith("|")
        spans = {norm(x) for r in REG.get(f, []) for x in [r["kb_text_span"], *str(r["kb_value"]).split(" / ")]
                 if len(norm(x)) >= 3 and norm(x) in v}
        if spans:
            vv = v
            for sp in sorted(spans, key=len, reverse=True):
                vv = re.sub(rf"(?<![a-z0-9]){re.escape(sp)}(?![a-z0-9])", " | ", vv)
            rest = [x.strip() for x in vv.split("|") if len(x.strip().split()) >= 3]
            if (rest and all(in_pdf(src, x) for x in rest)) or on_pair(src, vv):
                cls = "PDF_TYPO"
        fm = FIELD.match(raw)
        if not cls and CCODE.search(raw):
            v2 = nl(CCODE.sub(" ", fm.group(2) if fm else raw))
            if in_pdf(src, v2) or on_pair(src, v2):
                cls = "U_RULE"
        if not cls and fm:
            val = norm(fm.group(2))
            if in_pdf(src, val) or on_pair(src, val):
                cls = "SPEC_FIELD"
        if not cls and is_row and on_pair(src, v):
            cls = "TABLE_TOKENS"
        if not cls:
            d6 = d6_scope(f, n)
            if d6:
                cls = "KB_NOTE_SCOPE"
                detail_note[(f, n)] = d6
        if not cls:
            vd = re.sub(r"\[\d+\]", " ", v)                       # '[1]' footnote refs (PDF superscripts)
            vd = re.sub(r"\s+", " ", loose(vd)).replace("-", "")
            if vd in corpus_dh[src] or (sentences(vd) and all(x in corpus_dh[src] for x in sentences(vd))):
                cls = "PDF_DEHYPH"
        if not cls and segments(src, v):
            cls = "PDF_SEGMENTS"
        if not cls and near(src, v):
            cls = "PDF_NEAR"
        cls = cls or "UNEXPLAINED"
    res[cls] += 1
    if cls not in ("BLANK", "STRUCT", "PDF_SUBSTR", "HEADING_PDF"):
        detail[cls].append(dict(file=f, line=n, text=raw[:300], **({"d6_note": detail_note[(f, n)]} if (f, n) in detail_note else {})))
traced = sum(v for k, v in res.items() if k not in ("PDF_NEAR", "UNEXPLAINED"))
TIER = {"PDF (strict substring tier)": ("PDF_SUBSTR", "PDF_LOOSE", "PDF_SENTENCES", "PDF_SEGMENTS", "HEADING_PDF"),
        "brief buckets (structural / PDF_TYPO / U-rule)": ("BLANK", "STRUCT", "PDF_TYPO", "U_RULE"),
        "added buckets (writer-defined; reviewer to sample)": ("TABLE_TOKENS", "SPEC_FIELD", "MERMAID", "KB_NOTE", "KB_NOTE_SCOPE", "NOTE_EXEMPT", "XREF_D2", "HEADING_NOT_IN_PDF"),
        "not traced": ("PDF_NEAR", "UNEXPLAINED")}
for k, cs in TIER.items():
    print(f"  {k}: {sum(res[c] for c in cs)}  " + ", ".join(f"{c}={res[c]}" for c in cs))
json.dump(dict(base=a.base, rev=a.rev, counts=res, detail=detail), open(a.out, "w"), ensure_ascii=False, indent=1)
print(f"base={a.base} rev={a.rev} added_lines={len(added)} traced={traced} ({traced / len(added) * 100:.2f}%)")
print("by class:", dict(sorted(res.items(), key=lambda x: -x[1])))
print("NOT traced: PDF_NEAR", res["PDF_NEAR"], "UNEXPLAINED", res["UNEXPLAINED"], "-> details", os.path.relpath(a.out, ROOT))
bad_ex = [k for k in NOTE_EX if NOTE_EX_HIT[k] != 1] if a.rev == "WORKTREE" or NOTE_EX_HIT else []
print("NOTE_EXEMPT list:", len(NOTE_EX), "entries, hits", sum(NOTE_EX_HIT.values()), "| entries not hit exactly once:", bad_ex)
sys.exit(1 if bad_ex else 0)
