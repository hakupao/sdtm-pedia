#!/usr/bin/env python3
"""Take a subagent's final reply verbatim out of its session transcript (rule D: the main controller stores the
reviewer's text unchanged). Usage: python3 -I t4_extract_reply.py <agent transcript .jsonl> <out.md> <header file>
The header (written by the main controller) is put above a `---` line; everything below it is the reply, unedited.
"""
import json, sys

src, out, hdr = sys.argv[1:4]
last = None
for line in open(src, encoding="utf-8"):
    try:
        d = json.loads(line)
    except ValueError:
        continue
    m = d.get("message") or {}
    if d.get("type") == "assistant" and m.get("role") == "assistant":
        t = "".join(c.get("text", "") for c in m.get("content", []) if isinstance(c, dict) and c.get("type") == "text")
        if t.strip():
            last = t
assert last, "no assistant text found"
open(out, "w", encoding="utf-8").write(open(hdr, encoding="utf-8").read().rstrip("\n") + "\n\n---\n\n" + last.strip("\n") + "\n")
print(len(last), "chars ->", out)
