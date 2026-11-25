#!/usr/bin/env python3
"""tools/check_links.py — report broken relative links in tracked Markdown files.

Usage:
  python3 tools/check_links.py            # list broken links, exit 1 if any
  python3 tools/check_links.py --json     # one JSON record per link (all links)

Checks inline links/images `[t](target)` and reference definitions `[x]: target`,
outside fenced code blocks and inline code. Skips URLs with a scheme, `#anchor`
and absolute `/paths`. A link is OK when its target (minus #fragment / ?query)
exists on disk relative to the file.
"""
import json
import os
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INLINE = re.compile(r"!?\[(?:[^\[\]]|\[[^\[\]]*\])*\]\(\s*(<[^>]*>|[^)\s]+(?:\([^)\s]*\)[^)\s]*)*)(?:\s+(?:\"[^\"]*\"|'[^']*'))?\s*\)")
REFDEF = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]*>|\S+)")
SKIP = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|#|/)", re.I)
CODE = re.compile(r"`+[^`]*`+")


def links(text):
    fence = None
    for no, line in enumerate(text.split("\n"), 1):
        m = re.match(r"^\s*(```+|~~~+)", line)
        if m:
            tok = m.group(1)[0] * 3
            if fence is None:
                fence = tok
            elif tok == fence:
                fence = None
            continue
        if fence:
            continue
        stripped = CODE.sub("", line)
        found = [m.group(1) for m in INLINE.finditer(stripped)]
        rm = REFDEF.match(stripped)
        if rm:
            found.append(rm.group(1))
        for i, t in enumerate(found):
            yield no, i, t


def target_path(raw):
    t = raw[1:-1] if raw.startswith("<") and raw.endswith(">") else raw
    if not t or SKIP.match(t):
        return None
    t = re.split(r"[#?]", t, 1)[0]
    return unquote(t) if t else None


def main():
    as_json = "--json" in sys.argv
    files = subprocess.run(["git", "ls-files", "-z", "*.md"], cwd=ROOT,
                           capture_output=True, check=True).stdout.decode().split("\0")
    broken = 0
    for f in filter(None, files):
        p = os.path.join(ROOT, f)
        if not os.path.isfile(p):
            continue
        with open(p, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for no, i, raw in links(text):
            t = target_path(raw)
            if t is None:
                continue
            res = os.path.normpath(os.path.join(os.path.dirname(f), t))
            ok = os.path.exists(os.path.join(ROOT, res))
            if as_json:
                print(json.dumps({"src": f, "line": no, "idx": i, "raw": raw,
                                  "resolved": res, "ok": ok}, ensure_ascii=False))
            elif not ok:
                print(f"{f}:{no}: {raw}")
            broken += not ok
    if not as_json:
        print(f"broken relative links: {broken}", file=sys.stderr)
    sys.exit(1 if broken and not as_json else 0)


if __name__ == "__main__":
    main()
