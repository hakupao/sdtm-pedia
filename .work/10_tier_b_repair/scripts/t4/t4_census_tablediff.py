#!/usr/bin/env python3
"""Per-table comparison of full-KB census runs across commits (T4.1 attempt-2 gap: G-TB4 "合计相同不等于差异集相同").
Inputs (all produced read-only by scripts/table_census.py --manifest work/census_full_manifest.json):
  work/scratch/t4/census_hist/census_<rev>.json + the KB tree of that rev under work/scratch/t4/census_hist/kb_<rev>/
  (git archive <rev> knowledge_base | tar -x); HEAD = the working tree.
Pairing across commits is never by line number: (0) byte-identical table text in the same file; (1) key = (file,
normalised header, ex, ds) when unique, by text similarity when the key repeats; (2) leftovers in the same file by
table-body similarity (>= 0.6); the rest are reported as removed / added.
For every pair: status, census diff set (kb_row, col, kb, pdf), n_rows, and an md5 of the table text (so a changed
UNPARSEABLE table is visible even though the census cannot compare it).
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_census_tablediff.py  -> work/t4/census_tablediff.json
"""
import collections, difflib, hashlib, json, os, re, subprocess

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
TB = f"{ROOT}/.work/10_tier_b_repair"
H = f"{TB}/work/scratch/t4/census_hist"
REVS = ["50c3958", "00a2e93", "HEAD"]
kb_root = lambda rev: f"{ROOT}/knowledge_base" if rev == "HEAD" else f"{H}/kb_{rev}/knowledge_base"


def table_text(rev, t):
    p = os.path.join(kb_root(rev), t["file"].split("knowledge_base/", 1)[1])
    L = open(p, encoding="utf-8").read().split("\n")
    i = t["line"] - 1
    out = []
    while i < len(L) and L[i].lstrip().startswith("|"):
        out.append(L[i].strip())
        i += 1
    return "\n".join(out)


def load(rev):
    r = json.load(open(f"{H}/census_{rev}.json"))
    for t in r["tables"]:
        t["text"] = table_text(rev, t)
        t["md5"] = hashlib.md5(t["text"].encode()).hexdigest()
        t["dset"] = sorted({(str(d.get("type")), str(d.get("kb_row")), str(d.get("col")), str(d.get("kb")), str(d.get("pdf")))
                            for d in t.get("diffs", [])})
    return r


def nh(h):
    return re.sub(r"\s+", " ", re.sub(r"[\[\]()○□☐☑✓xX]", "", h or "")).strip().lower()


def pair(A, B):
    """[(a, b)], removed, added"""
    pairs, ua, ub = [], [], []
    # pass 0: tables whose text is byte-identical in the same file pair first (in order of appearance), so an unchanged
    # table can never be cross-paired with a changed neighbour that happens to share its header key
    ia, ib = collections.defaultdict(list), collections.defaultdict(list)
    for t in A:
        ia[(t["file"], t["md5"])].append(t)
    for t in B:
        ib[(t["file"], t["md5"])].append(t)
    done_a, done_b = set(), set()
    for k in ia:
        for x, y in zip(ia[k], ib.get(k, [])):
            pairs.append((x, y)); done_a.add(id(x)); done_b.add(id(y))
    A = [t for t in A if id(t) not in done_a]
    B = [t for t in B if id(t) not in done_b]
    ka, kb = collections.defaultdict(list), collections.defaultdict(list)
    for t in A:
        ka[(t["file"], nh(t["header"]), t.get("ex"), t.get("ds"))].append(t)
    for t in B:
        kb[(t["file"], nh(t["header"]), t.get("ex"), t.get("ds"))].append(t)
    for k in sorted(set(ka) | set(kb), key=str):
        a, b = ka.get(k, []), kb.get(k, [])
        if len(a) == len(b) == 1:
            pairs += list(zip(a, b))
        else:  # same key more than once (or different multiplicity): align by text similarity, not by position
            used = set()
            for x in a:
                best = max(((difflib.SequenceMatcher(None, x["text"], y["text"]).ratio(), j) for j, y in enumerate(b) if j not in used),
                           default=(0, None))
                if best[1] is not None and best[0] >= 0.6:
                    used.add(best[1])
                    pairs.append((x, b[best[1]]))
                else:
                    ua.append(x)
            ub += [y for j, y in enumerate(b) if j not in used]
    rem, used = [], set()
    for x in ua:  # leftovers: same file, body similarity
        best = max(((difflib.SequenceMatcher(None, x["text"], y["text"]).ratio(), j) for j, y in enumerate(ub)
                    if j not in used and y["file"] == x["file"]), default=(0, None))
        if best[1] is not None and best[0] >= 0.6:
            used.add(best[1])
            pairs.append((x, ub[best[1]]))
        else:
            rem.append(x)
    return pairs, rem, [y for j, y in enumerate(ub) if j not in used]


def commits(a, b, f):
    out = subprocess.check_output(["git", "-C", ROOT, "log", "--reverse", "--format=%h %s", f"{a}..{b}", "--", f], text=True)
    return [l[:110] for l in out.strip().split("\n") if l]


brief = lambda t: dict(file=t["file"], line=t["line"], header=t["header"][:90], ex=t.get("ex"), ds=t.get("ds"),
                       status=t["status"], n_rows=t["n_rows"], n_diffs=len(t["dset"]), md5=t["md5"])
C = {rev: load(rev) for rev in REVS}
res: dict = dict(revs=REVS, summary={}, steps=[])
for rev in REVS:
    r = C[rev]
    res["summary"][rev] = dict(kb_tables=len(r["tables"]), status=dict(collections.Counter(t["status"] for t in r["tables"])),
                               diffs=sum(len(t.get("diffs", [])) for t in r["tables"]), pdf_only=len(r["pdf_only"]),
                               pdf_unparsed=len(r["pdf_unparsed"]),
                               pdf_only_list=[dict(ds=p.get("ds"), ex=p.get("ex"), pages=p.get("pages")) for p in r["pdf_only"]])
for a, b in zip(REVS, REVS[1:]):
    pairs, rem, add = pair(C[a]["tables"], C[b]["tables"])
    ch, meta_only = [], []
    for x, y in pairs:
        meta = lambda t: (t.get("ex"), t.get("ds"), t.get("pdf_ex"), t.get("pdf_ds"), tuple(t.get("pdf_pages") or []), t.get("kb_duplicate"))
        kinds = [k for k, c in (("status", x["status"] != y["status"]), ("diffset", x["dset"] != y["dset"]),
                                ("n_rows", x["n_rows"] != y["n_rows"]), ("text", x["md5"] != y["md5"])) if c]
        if not kinds and meta(x) != meta(y):   # same text / status / diffs, but the census paired it differently
            F = ("ex", "ds", "pdf_ex", "pdf_ds", "pdf_pages", "kb_duplicate")
            meta_only.append(dict(file=x["file"], a_line=x["line"], b_line=y["line"], status=y["status"],
                                  changes={f: [m, n] for f, m, n in zip(F, meta(x), meta(y)) if m != n}))
        if kinds:
            la, lb = x["text"].split("\n"), y["text"].split("\n")
            ops = [o for o in difflib.SequenceMatcher(None, la, lb, autojunk=False).get_opcodes() if o[0] != "equal"]
            samp = ""
            if ops:
                _, i1, i2, j1, j2 = ops[0]
                o, n = (la[i1] if i2 > i1 else ""), (lb[j1] if j2 > j1 else "")
                cs = [c for c in difflib.SequenceMatcher(None, o, n, autojunk=False).get_opcodes() if c[0] != "equal"]
                samp = "; ".join(f"`{o[c[1]:c[2]][:40]}` → `{n[c[3]:c[4]][:40]}`" for c in cs[:3]) if o and n else ("+ " + n[:60] if n else "- " + o[:60])
            ch.append(dict(kinds=kinds, a=brief(x), b=brief(y), lines_removed=sum(o[2] - o[1] for o in ops),
                           lines_added=sum(o[4] - o[3] for o in ops), sample=samp,
                           diff_removed=[d for d in x["dset"] if d not in y["dset"]],
                           diff_added=[d for d in y["dset"] if d not in x["dset"]], commits=commits(a, b, x["file"])))
    step: dict = dict(a=a, b=b, paired=len(pairs), unchanged=len(pairs) - len(ch), changed=ch, meta_only=meta_only,
                map={f"{x['file']}:{x['line']}": dict(to=f"{y['file']}:{y['line']}", text_changed=x["md5"] != y["md5"]) for x, y in pairs},
                removed=[dict(brief(t), commits=commits(a, b, t["file"])) for t in rem],
                added=[dict(brief(t), commits=commits(a, b, t["file"])) for t in add])
    res["steps"].append(step)
    kc = collections.Counter(k for c in ch for k in c["kinds"])
    print(f"{a} -> {b}: paired {len(pairs)} (unchanged {step['unchanged']}), changed {len(ch)} {dict(kc)}, removed {len(rem)}, added {len(add)}")
    print("   pairing-metadata-only changes:", len(meta_only), dict(collections.Counter(k for m in meta_only for k in m["changes"])))
    print("   status moves:", dict(collections.Counter((c["a"]["status"], c["b"]["status"]) for c in ch if "status" in c["kinds"])))
    print("   changed tables by status (text changed):", dict(collections.Counter(c["b"]["status"] for c in ch if "text" in c["kinds"])))
os.makedirs(f"{TB}/work/t4", exist_ok=True)
json.dump(res, open(f"{TB}/work/t4/census_tablediff.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
for rev in REVS:
    print(rev, {k: v for k, v in res["summary"][rev].items() if k != "pdf_only_list"})
