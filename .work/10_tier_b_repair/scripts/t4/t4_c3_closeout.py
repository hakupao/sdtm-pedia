#!/usr/bin/env python3
"""C3 close-out helper (G-TB4): map the 60 C3 UNPARSEABLE tables of the T2-end triage
(evidence/t2_census_global_triage.md §5, census at 50c3958) to their HEAD tables, and find for each HEAD table the
commit at which its current text first appeared (so a table edited after its cell-by-cell check is visible).
Needs work/t4/census_tablediff.json (scripts/t4/t4_census_tablediff.py). Read-only on KB / git.
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_c3_closeout.py  -> work/t4/c3_closeout.json
"""
import json, re, subprocess

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
TB = f"{ROOT}/.work/10_tier_b_repair"
BASE = "50c3958"
git = lambda *a: subprocess.check_output(["git", "-C", ROOT, *a], text=True)


def tables(text):
    """{table text: first line no} for every run of consecutive '|' lines."""
    out, cur, start = {}, [], 0
    for n, l in enumerate(text.split("\n") + [""], 1):
        if l.lstrip().startswith("|"):
            if not cur:
                start = n
            cur.append(l.strip())
        elif cur:
            out.setdefault("\n".join(cur), start)
            cur = []
    return out


D = json.load(open(f"{TB}/work/t4/census_tablediff.json"))
m1, m2 = D["steps"][0]["map"], D["steps"][1]["map"]
added1 = D["steps"][0]["added"]
c3 = []
for l in open(f"{TB}/evidence/t2_census_global_triage.md", encoding="utf-8"):
    m = re.match(r"\| (\d+) \| C3 \| UNPARSEABLE \| `([^`]+):(\d+)` \| ([^|]*)\|[^|]*\|([^|]*)\|", l)
    if m:
        c3.append(dict(n=int(m.group(1)), file="knowledge_base/" + m.group(2), line_t2end=int(m.group(3)),
                       pages=m.group(4).strip(), header=m.group(5).strip()))
assert len(c3) == 60, len(c3)
hist = {}


def first_seen(f, text):
    """(commit, subject) of the oldest commit in the unbroken run back from HEAD in which this exact table text exists."""
    if f not in hist:
        revs = git("log", "--format=%h\t%s", f"{BASE}..HEAD", "--", f).strip().split("\n")
        revs = [r.split("\t", 1) for r in revs if r] + [[BASE, "(T2 收尾基线, 未再改)"]]
        hist[f] = [(h, s, tables(git("show", f"{h}:{f}"))) for h, s in revs]
    last = None
    for h, s, tabs in hist[f]:
        if text not in tabs:
            break
        last = (h, s)
    return last


head_tabs = {}
rows = []
for c in c3:
    f, k = c["file"], f"{c['file']}:{c['line_t2end']}"
    a = m1.get(k)
    b = m2.get(a["to"]) if a else None
    if not b:
        rows.append(dict(c, fate="rebuilt_in_T2S" if not a else "removed_in_thaw", head=None))
        continue
    ln = int(b["to"].rsplit(":", 1)[1])
    if f not in head_tabs:
        head_tabs[f] = {v: t for t, v in tables(open(f"{ROOT}/{f}", encoding="utf-8").read()).items()}
    text = head_tabs[f][ln]
    h, s = first_seen(f, text)
    rows.append(dict(c, fate="kept", head=f"{f}:{ln}", n_lines=text.count("\n") + 1, text_since=h, text_since_subject=s[:90],
                     changed_T2S=a["text_changed"], changed_thaw=b["text_changed"]))
new = []
for t in added1:  # tables created by the scan batches in the C3 files (replacements of rebuilt tables)
    f = t["file"]
    b = m2.get(f"{f}:{t['line']}")
    ln = int(b["to"].rsplit(":", 1)[1])
    if f not in head_tabs:
        head_tabs[f] = {v: x for x, v in tables(open(f"{ROOT}/{f}", encoding="utf-8").read()).items()}
    text = head_tabs[f][ln]
    h, s = first_seen(f, text)
    new.append(dict(file=f, head=f"{f}:{ln}", header=t["header"], n_lines=text.count("\n") + 1, text_since=h, text_since_subject=s[:90]))
json.dump(dict(c3=rows, new_tables=new), open(f"{TB}/work/t4/c3_closeout.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
import collections
print("C3 60:", dict(collections.Counter(r["fate"] for r in rows)))
print("text since:", dict(collections.Counter((r["file"].split("/")[-1], r["text_since"], r["text_since_subject"][:50]) for r in rows if r["head"])))
print("new tables:", [(n["head"], n["n_lines"], n["text_since"]) for n in new])
