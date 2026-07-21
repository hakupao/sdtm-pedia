#!/usr/bin/env python3
"""
P4a Batch Pre-processor
=======================
Joins p3_candidates.jsonl with pdf_atoms.jsonl + md_atoms.jsonl verbatim,
and writes per-batch input files for P4a matcher agents.

Output per batch: evidence/p4a_batches/batch_NNN_input.jsonl
Each line: one atom with pdf_verbatim + candidates[].md_verbatim pre-joined.

FIGURE atoms: verbatim truncated to first 200 chars per PLAN Appendix B / v0.4 Fix Gap 3.

Usage:
  python3 scripts/p4a_build_batches.py [--range START-END] [--batch_size 100]

Run from branches/06_deep_verification/ directory.
"""

import json
import os
import sys
import argparse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_jsonl_lookup(path, key_field):
    lookup = {}
    with open(path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"[WARN] {path}:{lineno} JSON error: {e}", file=sys.stderr)
                continue
            k = obj.get(key_field)
            if k:
                lookup[k] = obj
    return lookup


def truncate_verbatim(verbatim, atom_type, max_chars=200):
    if atom_type == "FIGURE" and verbatim and len(verbatim) > max_chars:
        return verbatim[:max_chars] + " [TRUNCATED:FIGURE]"
    return verbatim


def build_batches(range_start, range_end, batch_size, outdir, candidates_path, pdf_atoms_path, md_atoms_path):
    print(f"Loading pdf_atoms lookup from {pdf_atoms_path} ...")
    pdf_lookup = load_jsonl_lookup(pdf_atoms_path, "atom_id")
    print(f"  -> {len(pdf_lookup)} pdf atoms loaded")

    print(f"Loading md_atoms lookup from {md_atoms_path} ...")
    md_lookup = load_jsonl_lookup(md_atoms_path, "atom_id")
    print(f"  -> {len(md_lookup)} md atoms loaded")

    print(f"Reading candidates from {candidates_path} ...")
    all_candidates = []
    with open(candidates_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                all_candidates.append(json.loads(line))
    total = len(all_candidates)
    print(f"  -> {total} candidate rows loaded")

    os.makedirs(outdir, exist_ok=True)

    batch_num = 1
    written_batches = 0
    missing_pdf = 0
    missing_md_candidate = 0

    for batch_start in range(0, total, batch_size):
        batch_rows = all_candidates[batch_start:batch_start + batch_size]
        batch_label = f"batch_{batch_num:03d}"

        if batch_num < range_start:
            batch_num += 1
            continue
        if batch_num > range_end:
            break

        outpath = os.path.join(outdir, f"{batch_label}_input.jsonl")
        with open(outpath, "w", encoding="utf-8") as out:
            for row in batch_rows:
                pdf_atom_id = row["pdf_atom_id"]
                pdf_atom_type = row.get("pdf_atom_type", "SENTENCE")

                # Look up pdf atom for verbatim + page + figure_ref
                pdf_atom = pdf_lookup.get(pdf_atom_id, {})
                if not pdf_atom:
                    missing_pdf += 1

                pdf_verbatim_raw = pdf_atom.get("verbatim", "")
                pdf_verbatim = truncate_verbatim(pdf_verbatim_raw, pdf_atom_type)
                figure_ref = pdf_atom.get("figure_ref", None)

                # Build enriched candidates
                enriched_candidates = []
                for cand in row.get("candidates", []):
                    md_atom_id = cand["md_atom_id"]
                    md_atom = md_lookup.get(md_atom_id, {})
                    if not md_atom:
                        missing_md_candidate += 1

                    md_verbatim_raw = md_atom.get("verbatim", "")
                    md_verbatim = truncate_verbatim(md_verbatim_raw, pdf_atom_type)

                    enriched_candidates.append({
                        "md_atom_id": md_atom_id,
                        "md_file": cand.get("md_file", md_atom.get("file", "")),
                        "md_atom_type": cand.get("md_atom_type", md_atom.get("atom_type", "")),
                        "md_parent_section": md_atom.get("parent_section", ""),
                        "md_verbatim": md_verbatim,
                        "score": cand.get("score"),
                        "match_basis": cand.get("match_basis", ""),
                    })

                out_row = {
                    "pdf_atom_id": pdf_atom_id,
                    "pdf_atom_type": pdf_atom_type,
                    "pdf_source": row.get("pdf_source", ""),
                    "pdf_page": pdf_atom.get("page"),
                    "pdf_parent_section": row.get("pdf_parent_section", pdf_atom.get("parent_section", "")),
                    "pdf_verbatim": pdf_verbatim,
                    "figure_ref": figure_ref,
                    "candidates": enriched_candidates,
                    "candidate_count": len(enriched_candidates),
                    "zero_candidate": len(enriched_candidates) == 0,
                }
                out.write(json.dumps(out_row, ensure_ascii=False) + "\n")

        written_batches += 1
        print(f"  Wrote {batch_label} ({len(batch_rows)} atoms) -> {outpath}")
        batch_num += 1

    print(f"\nDone: {written_batches} batches written to {outdir}/")
    if missing_pdf:
        print(f"[WARN] {missing_pdf} pdf_atom_id(s) not found in pdf_atoms lookup")
    if missing_md_candidate:
        print(f"[WARN] {missing_md_candidate} md_atom_id(s) not found in md_atoms lookup")


def parse_range(range_str):
    parts = range_str.split("-")
    if len(parts) == 2:
        return int(parts[0]), int(parts[1])
    return int(parts[0]), int(parts[0])


def main():
    parser = argparse.ArgumentParser(description="Build P4a batch input files")
    parser.add_argument("--candidates", default=os.path.join(BASE, "p3_candidates.jsonl"))
    parser.add_argument("--pdf_atoms", default=os.path.join(BASE, "pdf_atoms.jsonl"))
    parser.add_argument("--md_atoms", default=os.path.join(BASE, "md_atoms.jsonl"))
    parser.add_argument("--batch_size", type=int, default=100)
    parser.add_argument("--range", default="1-125", dest="batch_range",
                        help="Batch range to generate, e.g. '1-25' or '26-50'")
    parser.add_argument("--outdir", default=os.path.join(BASE, "evidence", "p4a_batches"))
    args = parser.parse_args()

    range_start, range_end = parse_range(args.batch_range)
    print(f"Building batches {range_start}-{range_end} (size={args.batch_size}) -> {args.outdir}")
    build_batches(range_start, range_end, args.batch_size, args.outdir,
                  args.candidates, args.pdf_atoms, args.md_atoms)


if __name__ == "__main__":
    main()
