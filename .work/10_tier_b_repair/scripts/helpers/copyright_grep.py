"""Copyright grep: committable files under .work/10_tier_b_repair (git ls-files + untracked non-ignored) vs PDF text.
A hit = a run of >= N consecutive normalised words (lowercase alnum tokens) that also occurs in the PDF
(pdftotext raw order + work/pdf_pages layout order).
Each hit span is classed also-in-KB (its first N-gram occurs in knowledge_base/**.md, already public) or PDF-only.
Run from .work/10_tier_b_repair: python3 -I scripts/helpers/copyright_grep.py [N]"""
import collections, glob, hashlib, json, re, sys, unicodedata
N = int(sys.argv[1]) if len(sys.argv) > 1 else 30
R = "/Volumes/DevSSD/Project/sdtm-pedia"; TB = f"{R}/.work/10_tier_b_repair"
def toks(s):
    return re.findall(r"[a-z0-9]+", unicodedata.normalize("NFKC", s).lower())
def shingles(ws):
    return {hash(" ".join(ws[i:i + N])) for i in range(len(ws) - N + 1)}
pdf = set()
for f in ("ig34", "sv20"):
    pdf |= shingles(toks(open(f"{TB}/work/scratch/census_fix/raw/{f}.txt", encoding="utf-8").read()))
for f in sorted(glob.glob(f"{TB}/work/pdf_pages/*.txt")):     # layout (row-major) page text: table rows read across
    pdf |= shingles(toks(open(f, encoding="utf-8").read()))
kb = set()
for f in glob.glob(f"{R}/knowledge_base/**/*.md", recursive=True):
    kb |= shingles(toks(open(f, encoding="utf-8").read()))
files = [l.strip() for l in open(f"{TB}/work/scratch/census_fix/committable.txt") if l.strip()]
res = {}
for rel in files:
    try:
        raw = open(f"{TB}/{rel}", encoding="utf-8").read()
    except (UnicodeDecodeError, FileNotFoundError):
        continue
    if rel.endswith((".json", ".jsonl")):
        raw = raw.replace("\\n", " ").replace('\\"', '"')
    ws = toks(raw)
    hits = [i for i in range(len(ws) - N + 1) if hash(" ".join(ws[i:i + N])) in pdf]
    spans, cur = [], None
    for i in hits:
        if cur and i <= cur[1] + 1:
            cur[1] = i
        else:
            cur = [i, i]; spans.append(cur)
    if spans:
        kbn = sum(hash(" ".join(ws[a:a + N])) in kb for a, _ in spans)
        res[rel] = {"spans": len(spans), "also_in_kb": kbn, "pdf_only": len(spans) - kbn,
                    "max_words": max(b - a + N for a, b in spans), "words_in_spans": sum(b - a + N for a, b in spans)}
json.dump(res, open(f"{TB}/work/scratch/census_fix/copyright_N{N}.json", "w"), indent=1)
print(f"N={N} files scanned {len(files)}; files with hits {len(res)}")
for k, v in sorted(res.items(), key=lambda x: -x[1]["spans"]):
    print(f"  {k}: {v}")
