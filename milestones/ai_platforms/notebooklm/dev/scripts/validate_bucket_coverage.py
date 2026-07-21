#!/usr/bin/env python3
"""validate_bucket_coverage.py — v1.3 M5 defensive check.

Goal: catch silent KB-vs-bucket-config drift before merge_sources.py runs.

Compares:
  • Every `knowledge_base/domains/<DOM>/<field>.md` file (spec/assumptions/examples).
  • Every file path listed under any bucket in `bucket_config.json`.

Fails (exit 1) on:
  • KB file missing from every bucket (silent miss — would never reach NotebookLM)
  • Bucket reference to a non-existent KB file (stale config after KB rename/delete)

Prints (info, exit 0) on:
  • Bucket-config self-consistency (all referenced files exist, all KB files reached).
  • Bucket name vs. files mismatch (e.g. bucket name promises "ti_ts_oi" but files include "di").

Use:
  python3 ai_platforms/notebooklm/dev/scripts/validate_bucket_coverage.py
  python3 ai_platforms/notebooklm/dev/scripts/validate_bucket_coverage.py --json     # machine output
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
KB_ROOT = REPO_ROOT / "knowledge_base"
DOMAINS_DIR = KB_ROOT / "domains"
BUCKET_CONFIG = Path(__file__).parent / "bucket_config.json"

# Fields the KB defines per domain (allow missing — e.g. DI has only assumptions.md)
DOMAIN_FIELDS = ("spec", "assumptions", "examples")


def collect_kb_files() -> set[str]:
    """All KB md paths (relative to knowledge_base/) that should appear in some bucket.

    Returns: relative paths like 'domains/AE/spec.md'.
    """
    out: set[str] = set()
    if not DOMAINS_DIR.is_dir():
        return out
    for dom in sorted(p.name for p in DOMAINS_DIR.iterdir() if p.is_dir()):
        for field in DOMAIN_FIELDS:
            fp = DOMAINS_DIR / dom / f"{field}.md"
            if fp.is_file():
                rel = fp.relative_to(KB_ROOT).as_posix()
                out.add(rel)
    return out


def collect_bucket_files(config: dict) -> dict[str, list[str]]:
    """For each bucket id, list its referenced file paths (rel to KB)."""
    out: dict[str, list[str]] = {}
    for b in config.get("buckets", []):
        out[b["id"]] = list(b.get("files", []))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    if not BUCKET_CONFIG.is_file():
        print(f"FATAL: bucket_config.json not found at {BUCKET_CONFIG}", file=sys.stderr)
        return 2

    config = json.loads(BUCKET_CONFIG.read_text(encoding="utf-8"))
    kb_files = collect_kb_files()
    bucket_files_by_id = collect_bucket_files(config)

    # Flatten: which file is in which bucket(s)
    file_to_buckets: dict[str, list[str]] = {}
    for bid, files in bucket_files_by_id.items():
        for f in files:
            file_to_buckets.setdefault(f, []).append(bid)

    # Check 1: KB files missing from every bucket
    missing_in_buckets = sorted(kb_files - set(file_to_buckets.keys()))

    # Check 2: bucket references to non-existent KB files
    referenced_files = set(file_to_buckets.keys())
    # only check referenced files under knowledge_base scope (skip absolute / non-KB)
    kb_scope = {f for f in referenced_files if f.startswith("domains/") or f in {
        "INDEX.md", "ROUTING.md", "VAR_INDEX.md", "VARIABLE_INDEX.md",
    } or f.startswith("chapters/") or f.startswith("model/") or f.startswith("terminology/")}
    nonexistent = []
    for f in sorted(kb_scope):
        if not (KB_ROOT / f).is_file():
            nonexistent.append(f)

    # Check 3: bucket name vs files heuristic — flag mismatches
    name_mismatches: list[dict] = []
    for b in config.get("buckets", []):
        name = b.get("name", "")
        bid = b["id"]
        files = b.get("files", [])
        # collect domain tokens in name (after id_)
        # crude tokenize: strip 'NN_' prefix and '.md' suffix; split by _
        slug = name
        if slug.startswith(f"{bid}_"):
            slug = slug[len(bid) + 1:]
        slug = slug.removesuffix(".md")
        slug_tokens = set(t.upper() for t in slug.split("_") if t)
        # collect domain codes from files
        file_domains: set[str] = set()
        for f in files:
            if f.startswith("domains/"):
                dom = f.split("/")[1]
                file_domains.add(dom.upper())
        # tokens in files but not in name
        missing_in_name = file_domains - slug_tokens
        if missing_in_name:
            name_mismatches.append({
                "bucket_id": bid,
                "bucket_name": name,
                "domains_in_files_not_in_name": sorted(missing_in_name),
            })

    if args.json:
        result = {
            "kb_files_total": len(kb_files),
            "bucket_count": len(bucket_files_by_id),
            "missing_in_buckets": missing_in_buckets,
            "nonexistent_references": nonexistent,
            "name_mismatches": name_mismatches,
            "verdict": (
                "FAIL" if (missing_in_buckets or nonexistent) else
                ("WARN" if name_mismatches else "PASS")
            ),
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("=== NotebookLM bucket_config.json validation (v1.3 M5) ===\n")
        print(f"KB files in scope (domains/*/<field>.md): {len(kb_files)}")
        print(f"Bucket count: {len(bucket_files_by_id)}\n")

        if missing_in_buckets:
            print(f"FAIL — {len(missing_in_buckets)} KB file(s) NOT covered by any bucket:")
            for f in missing_in_buckets:
                print(f"  - {f}")
            print()
        else:
            print(f"✓ All {len(kb_files)} KB domain files covered.\n")

        if nonexistent:
            print(f"FAIL — {len(nonexistent)} bucket reference(s) point to NON-EXISTENT files:")
            for f in nonexistent:
                print(f"  - {f}")
            print()
        else:
            print("✓ All bucket-referenced files exist in KB.\n")

        if name_mismatches:
            print(f"WARN — {len(name_mismatches)} bucket name/files MISMATCH (cosmetic):")
            for m in name_mismatches:
                print(f"  bucket {m['bucket_id']} name='{m['bucket_name']}': "
                      f"files include domains {m['domains_in_files_not_in_name']} not in name slug")
            print()
        else:
            print("✓ Bucket names align with file domain codes.\n")

        verdict = (
            "FAIL" if (missing_in_buckets or nonexistent) else
            ("WARN" if name_mismatches else "PASS")
        )
        print(f"=== Verdict: {verdict} ===")

    if missing_in_buckets or nonexistent:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
