"""
P6 T3: Reclassify UNSOURCED_CANDIDATE atoms in reverse_ledger.jsonl

Steps:
  1. Auto-SYNTHESIZED by atom_type (HEADING, TABLE_HEADER, CROSS_REF, FIGURE)
  2. Auto-SYNTHESIZED by file pattern (VARIABLE_INDEX.md, INDEX.md, ROUTING.md)
  3. Re-fuzzy match with threshold 0.50 against pdf_atoms
  4. Pattern-based SYNTHESIZED (Source:, .xpt, pipe-heavy, section nav)
  5. Remainder → UNSOURCED_MANUAL
"""

import json
import re
import shutil
import sys
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

BASE = Path("/Users/bojiangzhang/MyProject/sdtm-pedia/branches/06_deep_verification")
LEDGER     = BASE / "reverse_ledger.jsonl"
MD_ATOMS   = BASE / "md_atoms.jsonl"
PDF_ATOMS  = BASE / "pdf_atoms.jsonl"
BACKUP     = BASE / "reverse_ledger.jsonl.p6_t3_pre.bak"
EVIDENCE   = BASE / "evidence" / "checkpoints" / "p6_t3_classification_report.json"

FUZZY_THRESHOLD    = 0.50
MIN_VERBATIM_LEN   = 10
PDF_SAMPLE_CAP     = 500
PIPE_THRESHOLD     = 5
STRUCTURAL_TYPES   = {"HEADING", "TABLE_HEADER", "CROSS_REF", "FIGURE"}
SKIP_FILE_PATTERNS = {"VARIABLE_INDEX.md", "INDEX.md", "ROUTING.md"}
TS_NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_jsonl(path):
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def ratio(a, b):
    return SequenceMatcher(None, a, b, autojunk=False).ratio()


def is_skip_file(filename):
    name = Path(filename).name
    return name in SKIP_FILE_PATTERNS


def is_pattern_synthesized(verbatim):
    """Step 4 pattern checks."""
    v = verbatim.strip()
    # Starts with "Source:"
    if v.startswith("Source:"):
        return "pattern:starts_with_Source:"
    # Ends with .xpt reference
    if re.search(r'\b\w+\.xpt\b', v):
        return "pattern:xpt_reference"
    # ≥5 pipe characters → example data row
    if v.count("|") >= PIPE_THRESHOLD:
        return "pattern:pipe_data_row"
    # Pure section navigation line: bold marker like **2.3** or **A.1.2**
    if re.fullmatch(r'\*\*[\dA-Z]+(?:\.\d+)*\*\*.*', v):
        return "pattern:section_nav_bold"
    return None


def main():
    # --- Backup ---
    if not BACKUP.exists():
        shutil.copy2(LEDGER, BACKUP)
        print(f"Backup created: {BACKUP}")
    else:
        print(f"Backup already exists: {BACKUP} (skipping overwrite)")

    # --- Load ledger ---
    print("Loading reverse_ledger.jsonl ...", flush=True)
    ledger = load_jsonl(LEDGER)
    total_ledger = len(ledger)
    unsourced_indices = [i for i, e in enumerate(ledger)
                         if e.get("reverse_verdict") == "UNSOURCED_CANDIDATE"]
    print(f"  Total ledger entries : {total_ledger}")
    print(f"  UNSOURCED_CANDIDATE  : {len(unsourced_indices)}", flush=True)

    # --- Load md_atoms into dict (atom_id → entry) ---
    print("Loading md_atoms.jsonl ...", flush=True)
    md_dict = {}
    for a in load_jsonl(MD_ATOMS):
        md_dict[a["atom_id"]] = a

    # --- Load pdf_atoms ---
    print("Loading pdf_atoms.jsonl ...", flush=True)
    pdf_list = load_jsonl(PDF_ATOMS)
    # Build section → pdf atom list for fast same-section lookup
    pdf_by_section = {}
    for a in pdf_list:
        sec = a.get("parent_section", "")
        pdf_by_section.setdefault(sec, []).append(a)
    pdf_flat = [(a["atom_id"], a.get("verbatim", ""), a.get("parent_section", ""))
                for a in pdf_list]
    print(f"  PDF atoms loaded     : {len(pdf_flat)}", flush=True)

    # --- Counters ---
    counts = {
        "SYNTHESIZED_structural_type":  0,
        "SYNTHESIZED_skip_file":        0,
        "SOURCED_P4A_MISSED_T3":        0,
        "SYNTHESIZED_pattern":          0,
        "UNSOURCED_MANUAL":             0,
    }
    unsourced_manual_ids = []
    reclassified = 0

    # --- Process each UNSOURCED_CANDIDATE ---
    for idx in unsourced_indices:
        entry = ledger[idx]
        atom_id = entry["md_atom_id"]
        md_atom  = md_dict.get(atom_id, {})
        atom_type   = md_atom.get("atom_type", entry.get("atom_type", ""))
        file_path   = md_atom.get("file", entry.get("file", ""))
        verbatim    = md_atom.get("verbatim", entry.get("verbatim_preview", ""))
        parent_sec  = md_atom.get("parent_section", entry.get("parent_section", ""))

        new_verdict = None
        detail      = None

        # Step 1 — structural type
        if atom_type in STRUCTURAL_TYPES:
            new_verdict = "SYNTHESIZED"
            detail      = f"auto:structural_type:{atom_type}"
            counts["SYNTHESIZED_structural_type"] += 1

        # Step 2 — skip file pattern
        elif is_skip_file(file_path):
            new_verdict = "SYNTHESIZED"
            detail      = f"auto:skip_file:{Path(file_path).name}"
            counts["SYNTHESIZED_skip_file"] += 1

        # Step 3 — re-fuzzy at 0.50
        elif len(verbatim) >= MIN_VERBATIM_LEN:
            vlen = len(verbatim)
            best_ratio  = 0.0
            best_pdf_id = None

            # First: same parent_section
            same_sec_atoms = pdf_by_section.get(parent_sec, [])
            for pa in same_sec_atoms:
                pv = pa.get("verbatim", "")
                if len(pv) < MIN_VERBATIM_LEN:
                    continue
                r = ratio(verbatim, pv)
                if r > best_ratio:
                    best_ratio  = r
                    best_pdf_id = pa["atom_id"]
                if best_ratio >= 1.0:
                    break

            # Then: global search (sampled by similar length ±50%)
            if best_ratio < FUZZY_THRESHOLD:
                lo, hi = int(vlen * 0.5), int(vlen * 1.5)
                candidates = [(pid, pv, _sec)
                              for pid, pv, _sec in pdf_flat
                              if lo <= len(pv) <= hi]
                # Cap to PDF_SAMPLE_CAP
                if len(candidates) > PDF_SAMPLE_CAP:
                    step = len(candidates) // PDF_SAMPLE_CAP
                    candidates = candidates[::step][:PDF_SAMPLE_CAP]
                for pid, pv, _sec in candidates:
                    if len(pv) < MIN_VERBATIM_LEN:
                        continue
                    r = ratio(verbatim, pv)
                    if r > best_ratio:
                        best_ratio  = r
                        best_pdf_id = pid
                    if best_ratio >= 1.0:
                        break

            if best_ratio >= FUZZY_THRESHOLD:
                new_verdict = "SOURCED_P4A_MISSED_T3"
                detail      = f"fuzzy_t3:ratio={best_ratio:.3f}:pdf_atom={best_pdf_id}"
                counts["SOURCED_P4A_MISSED_T3"] += 1

        # Step 4 — pattern-based SYNTHESIZED
        if new_verdict is None:
            pat = is_pattern_synthesized(verbatim)
            if pat:
                new_verdict = "SYNTHESIZED"
                detail      = pat
                counts["SYNTHESIZED_pattern"] += 1

        # Step 5 — UNSOURCED_MANUAL
        if new_verdict is None:
            new_verdict = "UNSOURCED_MANUAL"
            detail      = "needs_human_or_agent_review"
            counts["UNSOURCED_MANUAL"] += 1
            unsourced_manual_ids.append(atom_id)

        # Update ledger entry
        entry["reverse_verdict"] = new_verdict
        entry["detail"]          = detail
        entry["classified_by"]   = {
            "phase":  "P6_T3",
            "method": "script/p6_t3_unsourced_classify.py",
            "ts":     TS_NOW,
        }
        entry.pop("needs_agent_review", None)
        reclassified += 1

    # --- Write updated ledger ---
    print("Writing updated reverse_ledger.jsonl ...", flush=True)
    with open(LEDGER, "w", encoding="utf-8") as fh:
        for entry in ledger:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"  Written {total_ledger} entries.", flush=True)

    # --- Verify final verdict distribution ---
    final_counts = {}
    for entry in ledger:
        v = entry.get("reverse_verdict", "")
        final_counts[v] = final_counts.get(v, 0) + 1

    # --- Write evidence report ---
    report = {
        "generated_by": "p6_t3_unsourced_classify.py",
        "ts": TS_NOW,
        "total_ledger": total_ledger,
        "total_unsourced_candidate_input": len(unsourced_indices),
        "reclassified": reclassified,
        "reclassification_counts": counts,
        "final_verdict_distribution": final_counts,
        "unsourced_manual_ids": unsourced_manual_ids,
        "unsourced_manual_count": len(unsourced_manual_ids),
    }
    EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    with open(EVIDENCE, "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=2)
    print(f"Evidence written: {EVIDENCE}", flush=True)

    # --- Print summary ---
    print("\n" + "="*60)
    print("P6 T3 RECLASSIFICATION SUMMARY")
    print("="*60)
    print(f"Input UNSOURCED_CANDIDATE  : {len(unsourced_indices)}")
    print(f"Reclassified               : {reclassified}")
    print()
    print("Reclassification breakdown:")
    for k, v in counts.items():
        print(f"  {k:<35} : {v:>5}")
    print()
    print("Final verdict distribution (all ledger entries):")
    for k, v in sorted(final_counts.items(), key=lambda x: -x[1]):
        print(f"  {k:<35} : {v:>5}")
    print()
    print(f"UNSOURCED_MANUAL (need review) : {len(unsourced_manual_ids)}")
    if len(unsourced_manual_ids) <= 20:
        for aid in unsourced_manual_ids:
            print(f"  {aid}")
    else:
        print(f"  (see evidence report for full list)")
    print("="*60)


if __name__ == "__main__":
    main()
