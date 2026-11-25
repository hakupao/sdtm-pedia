#!/usr/bin/env python3
"""
P5 Reverse Matching: MD → PDF
For each MD atom, determine its reverse verdict:
  SOURCED / SOURCED_PARTIAL / SOURCED_MISPLACED / SOURCED_ERROR /
  SOURCED_P4A_MISSED / SYNTHESIZED / UNSOURCED_CANDIDATE

Input:  coverage_ledger.jsonl, md_atoms.jsonl, pdf_atoms.jsonl
Output: reverse_ledger.jsonl
"""

import json
import re
import sys
from collections import defaultdict, Counter
from difflib import SequenceMatcher
from datetime import datetime, timezone

COVERAGE_LEDGER = "coverage_ledger.jsonl"
MD_ATOMS = "md_atoms.jsonl"
PDF_ATOMS = "pdf_atoms.jsonl"
OUTPUT = "reverse_ledger.jsonl"

SYNTHESIZED_FILES = {
    "knowledge_base/VARIABLE_INDEX.md",
    "knowledge_base/INDEX.md",
    "knowledge_base/ROUTING.md",
}
SYNTHESIZED_TYPES = {"HEADING", "FIGURE", "TABLE_HEADER", "CROSS_REF"}
SYNTHESIZED_NOTE_PREFIXES = ("Source:", "See also:", "Reference:", "Cross-reference:")
EXAMPLES_PATTERN = re.compile(r"knowledge_base/domains/[A-Z]+/examples\.md$")
CHAPTERS_PATTERN = re.compile(r"knowledge_base/chapters/ch(\d+)")
FUZZY_THRESHOLD = 0.65

# Verbatim patterns that indicate editorial/structural SYNTHESIZED content
_SOURCE_HEADER_RE = re.compile(r"^Source:\s+SDTM(IG)?\s+v\d", re.IGNORECASE)
_BOLD_ONLY_RE = re.compile(r"^\*\*[^*]+\*\*$")
_DOMAIN_SPEC_HEADER_RE = re.compile(
    r"^[a-z]+\.xpt,\s+.+\s+—\s+.+\.\s+(One|Two|Multiple)\s+record"
)


def load_jsonl(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def build_reverse_idx(ledger_rows):
    """md_atom_id -> list of (pdf_atom_id, verdict)"""
    idx = defaultdict(list)
    for entry in ledger_rows:
        v = entry.get("verdict", "")
        for mid in entry.get("md_atom_ids", []):
            idx[mid].append((entry["pdf_atom_id"], v))
    return idx


def build_pdf_section_idx(pdf_atoms):
    """(source, parent_section) -> list of pdf_atom dicts (non-HEADING only)"""
    idx = defaultdict(list)
    for atom in pdf_atoms:
        if atom.get("atom_type") == "HEADING":
            continue
        source = "sv20" if atom["atom_id"].startswith("sv20_") else "ig34"
        key = (source, atom.get("parent_section", ""))
        idx[key].append(atom)
    return idx


def build_sv20_global_pool(pdf_atoms):
    """All non-HEADING sv20 pdf_atoms for section-agnostic fuzzy match (model/* fallback)."""
    return [a for a in pdf_atoms
            if a["atom_id"].startswith("sv20_") and a.get("atom_type") != "HEADING"]


def build_ig34_chapter_pools(pdf_atoms):
    """section-prefix → list of ig34 pdf_atoms for chapters/* global fuzzy fallback.
    Key = '§N' where N is the chapter number (matches §4, §8, etc.)."""
    pools = defaultdict(list)
    for a in pdf_atoms:
        if a["atom_id"].startswith("sv20_") or a.get("atom_type") == "HEADING":
            continue
        sec = a.get("parent_section", "")
        m = re.match(r"§(\d+)", sec)
        if m:
            pools[f"§{m.group(1)}"].append(a)
    return pools


def md_source_key(md_atom):
    """Infer source for md_atom based on file path (sv20 vs ig34)."""
    f = md_atom["file"]
    if "model/" in f:
        return "sv20"
    return "ig34"


MODEL_PATTERN = re.compile(r"knowledge_base/model/")


def fuzzy_similarity(a, b):
    return SequenceMatcher(None, a[:300], b[:300]).ratio()


def classify_md_atom(md_atom, reverse_idx, pdf_section_idx, sv20_global_pool, ig34_chapter_pools):
    mid = md_atom["atom_id"]
    atom_type = md_atom.get("atom_type", "")
    file_path = md_atom.get("file", "")
    verbatim = md_atom.get("verbatim", "")
    v_stripped = verbatim.strip()

    # --- Step 1: reverse_idx lookup ---
    if mid in reverse_idx:
        verdicts = [v for _, v in reverse_idx[mid]]
        if "EXACT" in verdicts or "EQUIVALENT" in verdicts:
            return "SOURCED", None
        if "PARTIAL" in verdicts:
            return "SOURCED_PARTIAL", None
        if "MISPLACED" in verdicts:
            return "SOURCED_MISPLACED", None
        if "ERROR" in verdicts:
            return "SOURCED_ERROR", None
        return "SOURCED_OTHER", None

    # --- Step 2: auto SYNTHESIZED rules ---
    if file_path in SYNTHESIZED_FILES:
        return "SYNTHESIZED", "auto:synthesized_file"
    if atom_type in SYNTHESIZED_TYPES:
        return "SYNTHESIZED", f"auto:synthesized_type:{atom_type}"
    if atom_type == "NOTE":
        for prefix in SYNTHESIZED_NOTE_PREFIXES:
            if v_stripped.startswith(prefix):
                return "SYNTHESIZED", f"auto:note_metadata:{prefix}"
    if atom_type == "TABLE_ROW" and EXAMPLES_PATTERN.match(file_path):
        if verbatim.count("|") >= 5:
            return "SYNTHESIZED", "auto:examples_data_row"
    # Metadata source-header annotations added by KB author ("Source: SDTMIG v3.4 …")
    if _SOURCE_HEADER_RE.match(v_stripped):
        return "SYNTHESIZED", "auto:source_header_annotation"
    # Bold-only section navigation anchors ("**RELREC — Description/Overview**")
    if _BOLD_ONLY_RE.match(v_stripped):
        return "SYNTHESIZED", "auto:bold_only_nav_anchor"
    # Domain spec overview summaries ("relrec.xpt, Related Records — …")
    if _DOMAIN_SPEC_HEADER_RE.match(v_stripped):
        return "SYNTHESIZED", "auto:domain_spec_overview_header"

    # --- Step 3a: section-scoped fuzzy lookup ---
    source = md_source_key(md_atom)
    parent_section = md_atom.get("parent_section", "")
    candidates = pdf_section_idx.get((source, parent_section), [])

    best_sim = 0.0
    best_pdf_id = None
    for pdf_atom in candidates:
        sim = fuzzy_similarity(verbatim, pdf_atom.get("verbatim", ""))
        if sim > best_sim:
            best_sim = sim
            best_pdf_id = pdf_atom["atom_id"]

    if best_sim >= FUZZY_THRESHOLD:
        return "SOURCED_P4A_MISSED", best_pdf_id

    # --- Step 3b: global sv20 fuzzy fallback for model/* atoms ---
    # sv20 section-key format differs from md_atoms — must search all sv20 atoms
    if MODEL_PATTERN.match(file_path) and sv20_global_pool:
        for pdf_atom in sv20_global_pool:
            sim = fuzzy_similarity(verbatim, pdf_atom.get("verbatim", ""))
            if sim > best_sim:
                best_sim = sim
                best_pdf_id = pdf_atom["atom_id"]
        if best_sim >= FUZZY_THRESHOLD:
            return "SOURCED_P4A_MISSED", best_pdf_id

    # --- Step 3c: chapter-prefix ig34 fallback for chapters/* atoms ---
    # Handles cases where same-section key matched nothing due to section header format
    ch_m = CHAPTERS_PATTERN.match(file_path)
    if ch_m and ig34_chapter_pools:
        ch_key = f"§{ch_m.group(1)}"
        for pdf_atom in ig34_chapter_pools.get(ch_key, []):
            sim = fuzzy_similarity(verbatim, pdf_atom.get("verbatim", ""))
            if sim > best_sim:
                best_sim = sim
                best_pdf_id = pdf_atom["atom_id"]
        if best_sim >= FUZZY_THRESHOLD:
            return "SOURCED_P4A_MISSED", best_pdf_id

    # --- Step 4: UNSOURCED_CANDIDATE ---
    return "UNSOURCED_CANDIDATE", None


def main():
    print("Loading data...", file=sys.stderr)
    ledger = load_jsonl(COVERAGE_LEDGER)
    md_atoms = load_jsonl(MD_ATOMS)
    pdf_atoms = load_jsonl(PDF_ATOMS)

    print(f"  coverage_ledger: {len(ledger)} entries", file=sys.stderr)
    print(f"  md_atoms: {len(md_atoms)}", file=sys.stderr)
    print(f"  pdf_atoms: {len(pdf_atoms)}", file=sys.stderr)

    reverse_idx = build_reverse_idx(ledger)
    pdf_section_idx = build_pdf_section_idx(pdf_atoms)
    sv20_global_pool = build_sv20_global_pool(pdf_atoms)
    ig34_chapter_pools = build_ig34_chapter_pools(pdf_atoms)
    print(f"  sv20 global pool size: {len(sv20_global_pool)}", file=sys.stderr)
    print(f"  ig34 chapter pools: {sorted(ig34_chapter_pools.keys())[:10]}...", file=sys.stderr)

    print("Classifying md_atoms...", file=sys.stderr)
    verdict_counter = Counter()
    unsourced_candidates = []
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    with open(OUTPUT, "w") as out:
        for i, md_atom in enumerate(md_atoms):
            if i % 1000 == 0:
                print(f"  {i}/{len(md_atoms)}...", file=sys.stderr)

            verdict, detail = classify_md_atom(md_atom, reverse_idx, pdf_section_idx, sv20_global_pool, ig34_chapter_pools)
            verdict_counter[verdict] += 1

            entry = {
                "md_atom_id": md_atom["atom_id"],
                "file": md_atom["file"],
                "atom_type": md_atom.get("atom_type"),
                "parent_section": md_atom.get("parent_section"),
                "verbatim_preview": md_atom.get("verbatim", "")[:100],
                "reverse_verdict": verdict,
                "detail": detail,
                "classified_by": {
                    "phase": "P5",
                    "method": "script/p5_reverse_match.py",
                    "ts": ts,
                },
            }

            if verdict == "UNSOURCED_CANDIDATE":
                unsourced_candidates.append(md_atom["atom_id"])
                entry["needs_agent_review"] = True

            out.write(json.dumps(entry) + "\n")

    # --- Stats ---
    print("\n=== P5 Reverse Matching Results ===")
    print(f"Total md_atoms processed: {len(md_atoms)}")
    print()
    for v, c in sorted(verdict_counter.items(), key=lambda x: -x[1]):
        pct = c / len(md_atoms) * 100
        print(f"  {v}: {c} ({pct:.1f}%)")

    print(f"\nUNSOURCED_CANDIDATE (needs agent review): {len(unsourced_candidates)}")

    # Unsourced breakdown by type
    uc_set = set(unsourced_candidates)
    uc_atoms = [a for a in md_atoms if a["atom_id"] in uc_set]
    by_type = Counter(a["atom_type"] for a in uc_atoms)
    print("\nUNSOURCED_CANDIDATE by atom_type:")
    for k, v in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")

    by_file = Counter(a["file"] for a in uc_atoms)
    print("\nUNSOURCED_CANDIDATE top files:")
    for k, v in by_file.most_common(15):
        print(f"  {k}: {v}")

    print(f"\nOutput written to: {OUTPUT}")
    print(f"Total lines: {len(md_atoms)}")


if __name__ == "__main__":
    main()
