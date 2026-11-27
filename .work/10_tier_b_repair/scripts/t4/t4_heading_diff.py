#!/usr/bin/env python3
"""Markdown heading diff of knowledge_base/ between two revisions (default kb-2026.11.25 -> HEAD), per file:
removed / added headings (multiset; fenced code ignored) + the commits that touched the file (batch name from subject).
Read-only (git show). -> stdout.
Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_heading_diff.py [OLD] [NEW] > out.txt
  NEW = WORKTREE (T4 W3): read the uncommitted working tree (tracked knowledge_base/*.md on disk); commits listed up to HEAD.
"""
import collections, os, re, subprocess, sys

old = sys.argv[1] if len(sys.argv) > 1 else "kb-2026.11.25"
new = sys.argv[2] if len(sys.argv) > 2 else "HEAD"
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout


def files(rev):
    if rev == "WORKTREE":
        return {f for f in git("ls-files", "knowledge_base").split() if f.endswith(".md") and os.path.exists(f)}
    return {f for f in git("ls-tree", "-r", "--name-only", rev, "knowledge_base").split() if f.endswith(".md")}


def heads(rev, f):
    out, fence = [], False
    for l in (open(f, encoding="utf-8").read() if rev == "WORKTREE" else git("show", f"{rev}:{f}")).splitlines():
        if l.startswith("```"):
            fence = not fence
        elif not fence and re.match(r"^#{1,6} ", l):
            out.append(l.strip())
    return out


fo, fn = files(old), files(new)
print(f"# knowledge_base heading diff {old} -> {new}")
print(f"files removed: {sorted(fo - fn)}; files added: {sorted(fn - fo)}")
nf = nr = na = 0
for f in sorted(fo & fn):
    a, b = heads(old, f), heads(new, f)
    ca, cb = collections.Counter(a), collections.Counter(b)
    rem = list(dict.fromkeys(h for h in a if cb[h] < ca[h]))
    add = list(dict.fromkeys(h for h in b if ca[h] < cb[h]))
    if not (rem or add):
        continue
    nf, nr, na = nf + 1, nr + len(rem), na + len(add)
    commits = [l for l in git("log", "--format=%h %s", f"{old}..{'HEAD' if new == 'WORKTREE' else new}", "--", f).splitlines()]
    tags = ", ".join(f"{c.split()[0]} {m.group(1)}" for c in commits if (m := re.search(r"batch (\S+)", c)))
    print(f"\n## {f} (headings {len(a)} -> {len(b)}; commits: {tags or '-'})")
    for h in rem:
        print(f"  - {h}")
    for h in add:
        print(f"  + {h}")
print(f"\nfiles with heading changes {nf}; removed {nr}; added {na}")
