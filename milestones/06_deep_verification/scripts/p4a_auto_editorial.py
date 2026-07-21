#!/usr/bin/env python3
"""
P4a Auto-classifier for INTENTIONAL_EXCLUDE (EDITORIAL_META / VERSION_MISMATCH)

Handles atoms that are provably editorial and need no AI judgment:
  - §0 [Cover] / §0 [Table of Contents] atoms → EDITORIAL_META
  - Version statement atoms (detected by verbatim pattern) → EDITORIAL_META

Writes: evidence/p4a_batches/batch_NNN_ledger.jsonl for each processed batch.
Also appends batch_quality_sample to trace.jsonl.

Usage:
  python3 scripts/p4a_auto_editorial.py --batches 1-3
  (Run from branches/06_deep_verification/ directory)
"""

import json, os, sys, argparse
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EDITORIAL_SECTION_PREFIXES = ("§0",)

EDITORIAL_VERBATIM_PATTERNS = (
    "Version 3.4 (Final)",
    "Version 2.0 (Final)",
    "Effective Date:",
    "Copyright",
    "Developed by the CDISC",
    "CDISC Submission Data Standards",
    "Prepared by:",
    "Revision History",
    "Table of Contents",
)


def is_editorial(row):
    section = row.get("pdf_parent_section", "")
    if any(section.startswith(p) for p in EDITORIAL_SECTION_PREFIXES):
        return True
    verbatim = row.get("pdf_verbatim", "")
    if any(p.lower() in verbatim.lower() for p in EDITORIAL_VERBATIM_PATTERNS):
        return True
    return False


def make_ledger_entry(row, batch_id):
    return {
        "pdf_atom_id": row["pdf_atom_id"],
        "md_atom_ids": [],
        "verdict": "INTENTIONAL_EXCLUDE",
        "similarity_score": None,
        "discrepancy": None,
        "exclusion_reason": f"Editorial/structural content from {row.get('pdf_parent_section','?')} — not included in KB by design",
        "category": "EDITORIAL_META",
        "approved_by": "pre-approved-category",
        "matched_by": {
            "subagent_type": "script/p4a_auto_editorial",
            "batch_id": batch_id,
            "prompt_version": "p4a_auto_editorial_v1.0",
            "ts": datetime.now(timezone.utc).isoformat(),
        },
    }


def process_batch(batch_num, outdir, trace_path):
    batch_id = f"batch_{batch_num:03d}"
    input_path = os.path.join(BASE, "evidence", "p4a_batches", f"{batch_id}_input.jsonl")
    output_path = os.path.join(BASE, "evidence", "p4a_batches", f"{batch_id}_ledger.jsonl")

    if not os.path.exists(input_path):
        print(f"[SKIP] {input_path} not found", file=sys.stderr)
        return 0, 0

    rows = []
    with open(input_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))

    non_editorial = [r for r in rows if not is_editorial(r)]
    if non_editorial:
        print(f"[WARN] batch_{batch_num:03d}: {len(non_editorial)} non-editorial atoms found "
              f"(auto-script only handles editorial; these will be MISSING in output).", file=sys.stderr)
        print(f"       Non-editorial sections: {set(r['pdf_parent_section'] for r in non_editorial)}", file=sys.stderr)

    entries = []
    for row in rows:
        if is_editorial(row):
            entries.append(make_ledger_entry(row, batch_id))
        else:
            # Non-editorial in an otherwise-editorial batch: mark as pending
            # This shouldn't happen for batches 001-002 but guard defensively
            entries.append({
                "pdf_atom_id": row["pdf_atom_id"],
                "md_atom_ids": [],
                "verdict": "MISSING",
                "similarity_score": None,
                "discrepancy": "PENDING: non-editorial atom in auto-editorial batch; re-process with AI agent",
                "exclusion_reason": None,
                "category": None,
                "approved_by": None,
                "matched_by": {
                    "subagent_type": "script/p4a_auto_editorial",
                    "batch_id": batch_id,
                    "prompt_version": "p4a_auto_editorial_v1.0",
                    "ts": datetime.now(timezone.utc).isoformat(),
                },
            })

    with open(output_path, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    editorial_count = sum(1 for e in entries if e["verdict"] == "INTENTIONAL_EXCLUDE")
    print(f"  {batch_id}: {len(entries)} atoms → {editorial_count} INTENTIONAL_EXCLUDE → {output_path}")

    # Append batch_quality_sample to trace.jsonl
    ts = datetime.now(timezone.utc).isoformat()
    trace_event = {
        "ts": ts,
        "phase": "P4a",
        "slot": "batch_quality_sample",
        "batch_id": batch_id,
        "subagent_type": "script/p4a_auto_editorial",
        "prompt_version": "p4a_auto_editorial_v1.0",
        "stats": {
            "total": len(entries),
            "EXACT": 0,
            "EQUIVALENT": 0,
            "PARTIAL": 0,
            "MISPLACED": 0,
            "MISSING": len([e for e in entries if e["verdict"] == "MISSING"]),
            "ERROR": 0,
            "INTENTIONAL_EXCLUDE": editorial_count,
        },
        "samples": [
            {"pdf_atom_id": e["pdf_atom_id"], "verdict": e["verdict"], "top1_score": None}
            for e in entries[:5]
        ],
    }
    with open(trace_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(trace_event, ensure_ascii=False) + "\n")

    return len(entries), editorial_count


def parse_range(s):
    parts = s.split("-")
    return int(parts[0]), int(parts[-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batches", default="1-2", help="Batch range e.g. '1-2'")
    args = parser.parse_args()

    start, end = parse_range(args.batches)
    trace_path = os.path.join(BASE, "trace.jsonl")
    print(f"Auto-classifying editorial atoms for batches {start}-{end}")
    total_atoms = total_editorial = 0
    for b in range(start, end + 1):
        a, e = process_batch(b, os.path.join(BASE, "evidence", "p4a_batches"), trace_path)
        total_atoms += a
        total_editorial += e
    print(f"\nTotal: {total_atoms} atoms, {total_editorial} INTENTIONAL_EXCLUDE")


if __name__ == "__main__":
    main()
