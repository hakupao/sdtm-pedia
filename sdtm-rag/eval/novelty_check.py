"""Novelty check for blind-authored eval questions (Rule D process fix, 2026-07-07).

Blind writers given the same need card converge on similar phrasings across rounds,
which silently weakens a "fresh held-out" gate (found in the AGG Rule D review: r3
overlapped r1/r2 on 4 verbatim + ~7 near-verbatim questions). This gadget measures
content-word Jaccard similarity of each candidate question against a corpus of prior
questions and flags convergent ones so the gate can be run on a genuinely novel subset.

Usage:
  .venv/bin/python eval/novelty_check.py CANDIDATES.json PRIOR1.yml [PRIOR2.yml ...]

CANDIDATES.json = {"id": "question", ...}; PRIOR files = yml lists with `question:`
fields or json {"id": "question"} maps. Threshold 0.6 (>= flagged as convergent).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

_STOP = {"the", "a", "an", "of", "in", "to", "that", "which", "what", "whats", "is",
         "are", "do", "does", "can", "you", "me", "any", "there", "and", "or", "for",
         "with", "by", "on", "it", "its", "how", "many", "much", "i", "im", "hey",
         "sdtm", "domains", "domain", "datasets", "dataset", "variables", "variable",
         "vars", "codelist", "codelists", "one", "ones"}
# Domain nouns are stopworded deliberately: every question in this corpus mentions
# variables/domains/codelists, so they carry no novelty signal.

_THRESHOLD = 0.6


def content_words(q: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", q.lower()) if w not in _STOP}


def load_prior(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        return sorted(json.loads(text).items())
    rows = yaml.safe_load(text)
    return [(r.get("id", "?"), r["question"]) for r in rows if isinstance(r, dict) and "question" in r]


def main() -> int:
    cands = sorted(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")).items())
    prior: list[tuple[str, str]] = []
    for p in sys.argv[2:]:
        prior.extend(load_prior(Path(p)))

    flagged = 0
    for cid, cq in cands:
        cw = content_words(cq)
        best_sim, best_id, best_q = 0.0, "", ""
        for pid, pq in prior:
            pw = content_words(pq)
            union = cw | pw
            sim = len(cw & pw) / len(union) if union else 0.0
            if sim > best_sim:
                best_sim, best_id, best_q = sim, pid, pq
        verdict = "CONVERGENT" if best_sim >= _THRESHOLD else "novel"
        if verdict == "CONVERGENT":
            flagged += 1
        print(f"{cid}: {verdict}  (max jaccard {best_sim:.2f} vs {best_id}: {best_q[:60]})")
    print(f"\n{len(cands) - flagged}/{len(cands)} novel (threshold {_THRESHOLD})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
