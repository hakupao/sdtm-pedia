"""S3 long-name attribution probe.

For each question in a test set (optionally filtered by id prefix/list), show
exactly which StructuredLookup channel fires:

  - code-token domains   (2-letter/short code present in the query)
  - long-name domains    (S3: VARIABLE_INDEX §二 long-name matcher)
  - term/dist intent     (S1 terminology / distribution channels)
  - resolve() output     (final union-add targets)

Purpose: deterministic attribution for the v3 long-name single questions —
if a question has NO code-token match and resolve() returns a domains/<CODE>/
spec.md, the ONLY path that produced it is the S3 long-name matcher.

Run from sdtm-rag/:
  .venv/bin/python eval/probe_s3_longname.py eval/test_set_v3.yml --ids q128-q140
  .venv/bin/python eval/probe_s3_longname.py eval/test_set_v3.yml            # all questions
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from server.config import settings  # noqa: E402
from server.meta_store import MetaStore  # noqa: E402
from server.structured_lookup import (
    _QUERY_VAR_TOKEN_RE,  # noqa: E402
    StructuredLookup,  # noqa: E402
)


def parse_ids(spec: str) -> set[str]:
    """'q128-q140' or 'q128,q130' -> explicit id set."""
    ids: set[str] = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part[1:]:
            lo, hi = part.split("-")
            prefix = lo.rstrip("0123456789")
            lo_n, hi_n = int(lo[len(prefix):]), int(hi[len(prefix):])
            ids.update(f"{prefix}{n}" for n in range(lo_n, hi_n + 1))
        else:
            ids.add(part)
    return ids


def main() -> int:
    parser = argparse.ArgumentParser(description="S3 long-name attribution probe")
    parser.add_argument("test_set")
    parser.add_argument("--ids", default=None, help="e.g. q128-q140 or q128,q130")
    parser.add_argument("--output", default=None, help="save probe table as JSON")
    args = parser.parse_args()

    with open(args.test_set, encoding="utf-8") as f:
        questions = yaml.safe_load(f)
    if args.ids:
        wanted = parse_ids(args.ids)
        questions = [q for q in questions if q["id"] in wanted]

    lookup = StructuredLookup(Path(settings.kb_root), MetaStore(settings.meta_path))
    rows: list[dict] = []
    for q in questions:
        query = q["question"]
        ql = query.lower()
        code_domains = [
            tok for tok in _QUERY_VAR_TOKEN_RE.findall(query)
            if tok in lookup.domain_to_spec
        ]
        longname_domains = lookup._query_longname_domains(query)
        named_vars = lookup._query_variables(query)
        dist = lookup._is_distribution_intent(query, ql)
        targets = lookup.resolve(query)
        rows.append({
            "id": q["id"],
            "category": q["category"],
            "code_token_domains": code_domains,
            "longname_domains": longname_domains,
            "named_variables": named_vars,
            "dist_intent": dist,
            "resolve_targets": targets,
            "s3_attributable": bool(longname_domains) and not code_domains,
            "expected_sources": q.get("expected_sources", []),
        })

    print(f"{'id':<6} {'cat':<14} {'code-tok':<10} {'longname':<14} {'s3?':<4} resolve")
    for r in rows:
        print(
            f"{r['id']:<6} {r['category'][:13]:<14} "
            f"{','.join(r['code_token_domains']) or '-':<10} "
            f"{','.join(r['longname_domains']) or '-':<14} "
            f"{'YES' if r['s3_attributable'] else '-':<4} "
            f"{r['resolve_targets']}"
        )

    n_s3 = sum(1 for r in rows if r["s3_attributable"])
    print(f"\n{len(rows)} questions probed; S3 long-name channel fired (no code token): {n_s3}")

    if args.output:
        Path(args.output).write_text(
            json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"Saved to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
