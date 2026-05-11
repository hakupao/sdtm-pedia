#!/usr/bin/env python3
"""
P4a Ledger Merger
=================
Merges all completed batch_NNN_ledger.jsonl files into coverage_ledger.jsonl,
in canonical order (batch_001 → batch_125).

Also reports progress stats.

Usage:
  python3 scripts/p4a_merge_ledger.py [--dry_run]
  (Run from branches/06_deep_verification/ directory)
"""

import json, os, sys, glob, argparse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCHES_DIR = os.path.join(BASE, "evidence", "p4a_batches")
LEDGER_PATH = os.path.join(BASE, "coverage_ledger.jsonl")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry_run", action="store_true", help="Report only, do not write")
    parser.add_argument("--batch_size", type=int, default=100)
    parser.add_argument("--total_atoms", type=int, default=12487)
    args = parser.parse_args()

    # Find all completed ledger files
    pattern = os.path.join(BATCHES_DIR, "batch_*_ledger.jsonl")
    ledger_files = sorted(glob.glob(pattern))

    if not ledger_files:
        print("No ledger files found.")
        return

    print(f"Found {len(ledger_files)} ledger file(s)")

    all_entries = []
    verdict_counts = {}
    missing_batches = []
    errors = []

    for path in ledger_files:
        batch_id = os.path.basename(path).replace("_ledger.jsonl", "")
        entries = []
        with open(path, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    entries.append(obj)
                    v = obj.get("verdict", "UNKNOWN")
                    verdict_counts[v] = verdict_counts.get(v, 0) + 1
                except json.JSONDecodeError as e:
                    errors.append(f"{path}:{lineno}: {e}")

        all_entries.extend(entries)
        print(f"  {batch_id}: {len(entries)} entries")

    total = len(all_entries)
    pct = total / args.total_atoms * 100
    print(f"\nTotal entries: {total} / {args.total_atoms} ({pct:.1f}%)")
    print("Verdict distribution:")
    for v, c in sorted(verdict_counts.items(), key=lambda x: -x[1]):
        print(f"  {v:25s}: {c:5d} ({c/total*100:.1f}%)")

    if errors:
        print(f"\n[WARN] {len(errors)} JSON errors:")
        for e in errors[:5]:
            print(f"  {e}")

    if args.dry_run:
        print("\n[dry_run] No file written.")
        return

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        for entry in all_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"\nWrote {total} entries to {LEDGER_PATH}")


if __name__ == "__main__":
    main()
