#!/usr/bin/env python3
"""
P4b Section Aggregation Script
Input:  pdf_atoms.jsonl, coverage_ledger.jsonl, md_atoms.jsonl
Output: section_coverage.jsonl

Produces one entry per PDF section with:
  - coverage_density (EXACT+EQUIVALENT / total content atoms)
  - child_sections status (MATCHED | MISSING | SKELETON_ONLY | CONTENT_TRUNCATED)
  - aggregate_verdict (priority table from PLAN §4.5)
  - failure_patterns list (may be multiple)
  - keyword_flag (level1/level2 if shall/must/should detected in MISSING atoms)
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

BASE = "branches/06_deep_verification"

# ── Level-1 keywords (shall/must) → force CONTENT_TRUNCATED if in MISSING atom
LEVEL1_KW = {
    "shall", "shall not", "must", "must not", "required",
    "is required", "are required", "is not permitted",
    "is prohibited", "not permitted", "may not", "MUST",
}
# ── Level-2 keywords (should/only/etc.) → flag only, no auto-downgrade
LEVEL2_KW = {"should", "only", "except", "no longer", "cannot", "not allowed"}

# ── aggregate_verdict priority (lowest index = highest priority)
VERDICT_PRIORITY = [
    "STRUCTURE_DRIFTED",
    "HEADING_MISSING",
    "SKELETON_ONLY",
    "SIBLING_DROPPED",
    "CONTENT_TRUNCATED",
    "MOSTLY_COMPLETE",
    "FULL_COVERAGE",
]


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return rows


def atom_source(atom_id: str) -> str:
    return "sv20" if atom_id.startswith("sv20") else "ig34"


def parse_section_number(section_key: str):
    """'§4.2.7 [Title]' → '4.2.7'; returns None if not §-numbered."""
    m = re.match(r"^§([0-9.]+)", section_key)
    return m.group(1) if m else None


def parse_section_title(section_key: str) -> str:
    """'§4.2.7 [Title]' → 'Title'; fallback = full key."""
    m = re.search(r"\[([^\]]+)\]", section_key)
    return m.group(1) if m else section_key


def make_section_id(source: str, section_key: str) -> str:
    num = parse_section_number(section_key)
    if num:
        return f"{source}_§{num}"
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", section_key).strip("_")[:50]
    return f"{source}_{slug}"


def check_keywords(verbatim: str):
    """Returns ('level1'|'level2'|None, matched_keyword)."""
    if not verbatim:
        return None, None
    lo = verbatim.lower()
    for kw in LEVEL1_KW:
        if kw.lower() in lo:
            return "level1", kw
    for kw in LEVEL2_KW:
        if kw.lower() in lo:
            return "level2", kw
    return None, None


def direct_children(num: str, all_nums: set) -> list:
    """Return sorted list of nums that are direct children of num."""
    prefix = num + "."
    out = []
    for n in all_nums:
        if n.startswith(prefix):
            tail = n[len(prefix):]
            if "." not in tail:
                out.append(n)
    return sorted(out)


# ─────────────────────────────────────────────────────────────────────────────
# Load
# ─────────────────────────────────────────────────────────────────────────────

print("Loading pdf_atoms.jsonl …", flush=True)
pdf_atoms = load_jsonl(f"{BASE}/pdf_atoms.jsonl")
print(f"  {len(pdf_atoms):,} atoms")

print("Loading coverage_ledger.jsonl …", flush=True)
ledger = {e["pdf_atom_id"]: e for e in load_jsonl(f"{BASE}/coverage_ledger.jsonl")}
print(f"  {len(ledger):,} ledger entries")

print("Loading md_atoms.jsonl …", flush=True)
md_file_map = {a["atom_id"]: a.get("file", "") for a in load_jsonl(f"{BASE}/md_atoms.jsonl")}
print(f"  {len(md_file_map):,} md atoms")

# ─────────────────────────────────────────────────────────────────────────────
# Group atoms: key = (source, parent_section)
# ─────────────────────────────────────────────────────────────────────────────

section_atoms: dict[tuple, list] = defaultdict(list)
for a in pdf_atoms:
    src = atom_source(a["atom_id"])
    section_atoms[(src, a["parent_section"])].append(a)

all_section_keys = list(section_atoms.keys())   # list of (source, key)
print(f"\nTotal (source, section) groups: {len(all_section_keys)}")

# Build num → (source, key) index for §-numbered sections
num_to_section: dict[tuple, tuple] = {}  # (source, num) → (source, key)
for src, sk in all_section_keys:
    num = parse_section_number(sk)
    if num:
        num_to_section[(src, num)] = (src, sk)

all_nums_by_src: dict[str, set] = defaultdict(set)
for (src, num) in num_to_section:
    all_nums_by_src[src].add(num)

# ─────────────────────────────────────────────────────────────────────────────
# Per-section stats helper
# ─────────────────────────────────────────────────────────────────────────────

def section_stats(content_atoms):
    """
    Returns dict with verdict counts, coverage_density, misplaced_rate,
    keyword_flag, missing_verbatims, md_files.
    """
    counts = defaultdict(int)
    md_files = set()
    missing_verbatims = []
    misplaced_count = 0

    for a in content_atoms:
        entry = ledger.get(a["atom_id"])
        v = entry["verdict"] if entry else "MISSING"
        counts[v] += 1
        if v in ("EXACT", "EQUIVALENT") and entry:
            for mid in entry.get("md_atom_ids", []):
                f = md_file_map.get(mid, "")
                if f:
                    md_files.add(f)
        if v == "MISSING":
            missing_verbatims.append(a.get("verbatim", ""))
        if v == "MISPLACED":
            misplaced_count += 1

    total = len(content_atoms)
    matched = counts["EXACT"] + counts["EQUIVALENT"]
    density = matched / total if total > 0 else None
    misplaced_rate = misplaced_count / total if total > 0 else 0.0

    # Keyword detection: scan MISSING atom verbatims
    keyword_flag = None
    keyword_example = None
    for verbatim in missing_verbatims:
        kl, kw = check_keywords(verbatim)
        if kl == "level1":
            keyword_flag, keyword_example = "level1", kw
            break
        if kl == "level2" and keyword_flag is None:
            keyword_flag, keyword_example = "level2", kw

    return {
        "total": total,
        "matched": matched,
        "partial": counts["PARTIAL"],
        "missing": counts["MISSING"],
        "misplaced": misplaced_count,
        "error": counts["ERROR"],
        "intentional_exclude": counts["INTENTIONAL_EXCLUDE"],
        "density": density,
        "misplaced_rate": misplaced_rate,
        "keyword_flag": keyword_flag,
        "keyword_example": keyword_example,
        "md_files": md_files,
    }


def child_status_from_density(density, child_total):
    """Map density to 4-value child-section status enum."""
    if child_total == 0:
        return "MISSING"
    if density is None:
        return "MISSING"
    if density >= 0.80:
        return "MATCHED"
    if density < 0.20:
        return "SKELETON_ONLY"
    return "CONTENT_TRUNCATED"


def compute_verdict_and_patterns(stats, child_statuses, heading_missing):
    """
    Compute (aggregate_verdict, failure_patterns) following PLAN §4.5 priority table.
    child_statuses: list of status strings from child_sections dict values.
    """
    patterns = set()
    density = stats["density"] if stats["density"] is not None else 1.0
    total = stats["total"]

    # STRUCTURE_DRIFTED: ≥10% MISPLACED
    if stats["misplaced_rate"] >= 0.10:
        patterns.add("STRUCTURE_DRIFTED")

    # HEADING_MISSING
    if heading_missing:
        patterns.add("HEADING_MISSING")

    # SKELETON_ONLY (this section)
    if total > 0 and density < 0.20:
        patterns.add("SKELETON_ONLY")

    # SIBLING_DROPPED: any child MISSING, SKELETON_ONLY, or CONTENT_TRUNCATED
    # (PLAN: CONTENT_TRUNCATED < 0.60 triggers; we treat all CONTENT_TRUNCATED
    #  as potential trigger since we don't re-compute density here)
    for cs in child_statuses:
        if cs in ("MISSING", "SKELETON_ONLY", "CONTENT_TRUNCATED"):
            patterns.add("SIBLING_DROPPED")
            break

    # CONTENT_TRUNCATED (this section)
    if total > 0 and 0.20 <= density < 0.80:
        if "SKELETON_ONLY" not in patterns:
            patterns.add("CONTENT_TRUNCATED")

    # Keyword upgrade: MOSTLY_COMPLETE + Level-1 keyword → CONTENT_TRUNCATED
    if density >= 0.80 and stats["keyword_flag"] == "level1":
        patterns.add("CONTENT_TRUNCATED")

    # Determine single aggregate_verdict by priority
    if not patterns:
        if total == 0:
            # Structural-only section (only HEADINGs) — verdict from children
            if not child_statuses:
                verdict = "FULL_COVERAGE"
            elif all(cs == "MATCHED" for cs in child_statuses):
                verdict = "FULL_COVERAGE"
            elif any(cs in ("MISSING", "SKELETON_ONLY") for cs in child_statuses):
                verdict = "SIBLING_DROPPED"
            else:
                verdict = "MOSTLY_COMPLETE"
        elif density >= 0.95:
            if not child_statuses or all(cs == "MATCHED" for cs in child_statuses):
                verdict = "FULL_COVERAGE"
            else:
                verdict = "MOSTLY_COMPLETE"
        else:
            verdict = "MOSTLY_COMPLETE"
    else:
        verdict = "FULL_COVERAGE"  # will be overridden
        for p in VERDICT_PRIORITY:
            if p in patterns:
                verdict = p
                break

    return verdict, sorted(patterns)


# ─────────────────────────────────────────────────────────────────────────────
# Main loop
# ─────────────────────────────────────────────────────────────────────────────

ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
output_entries = []

for src, sk in sorted(all_section_keys, key=lambda x: (x[0], x[1])):
    atoms_here = section_atoms[(src, sk)]
    content_atoms = [a for a in atoms_here if a["atom_type"] != "HEADING"]
    heading_atoms = [a for a in atoms_here if a["atom_type"] == "HEADING"]

    stats = section_stats(content_atoms)

    # Page range
    pages = [a.get("page") for a in atoms_here if a.get("page")]
    page_range = [min(pages), max(pages)] if pages else [None, None]

    # ── Child sections (§-numbered only)
    child_sections_dict: dict[str, str] = {}
    child_densities: dict = {}
    num = parse_section_number(sk)
    if num:
        child_nums = direct_children(num, all_nums_by_src[src])
        for cnum in child_nums:
            ckey = num_to_section.get((src, cnum))
            if not ckey:
                continue
            c_atoms_here = section_atoms[ckey]
            c_content = [a for a in c_atoms_here if a["atom_type"] != "HEADING"]
            c_stats = section_stats(c_content)
            status = child_status_from_density(c_stats["density"], c_stats["total"])
            child_title = parse_section_title(ckey[1])
            child_sections_dict[child_title] = status
            child_densities[child_title] = c_stats["density"]

    # ── HEADING_MISSING detection
    # Find the HEADING atom in the parent section that defines THIS section
    heading_missing = False
    if num and "." in num:
        parent_num = num.rsplit(".", 1)[0]
        parent_key = num_to_section.get((src, parent_num))
        if parent_key:
            parent_atoms = section_atoms[parent_key]
            parent_headings = [a for a in parent_atoms if a["atom_type"] == "HEADING"]
            section_title_str = parse_section_title(sk)
            for h in parent_headings:
                if h.get("verbatim", "").strip() == section_title_str.strip():
                    entry = ledger.get(h["atom_id"])
                    if entry and entry.get("verdict") == "MISSING":
                        heading_missing = True
                    break

    # ── Aggregate verdict
    child_status_values = list(child_sections_dict.values())
    aggregate_verdict, failure_patterns = compute_verdict_and_patterns(
        stats, child_status_values, heading_missing
    )

    entry = {
        "section_id": make_section_id(src, sk),
        "source": src,
        "section_key": sk,
        "section_title": parse_section_title(sk),
        "pdf_page_range": page_range,
        "pdf_atom_count": stats["total"],
        "md_target_files": sorted(stats["md_files"]),
        "md_atom_count_matched": stats["matched"],
        "md_atom_count_partial": stats["partial"],
        "md_atom_count_missing": stats["missing"],
        "md_atom_count_misplaced": stats["misplaced"],
        "md_atom_count_error": stats["error"],
        "md_atom_count_intentional_exclude": stats["intentional_exclude"],
        "coverage_density": round(stats["density"], 4) if stats["density"] is not None else None,
        "misplaced_rate": round(stats["misplaced_rate"], 4),
        "child_sections": child_sections_dict,
        "aggregate_verdict": aggregate_verdict,
        "failure_patterns": failure_patterns,
        "keyword_flag": stats["keyword_flag"],
        "keyword_example": stats["keyword_example"],
        "heading_missing_detected": heading_missing,
        "aggregated_by": {
            "phase": "P4b",
            "script": "scripts/p4b_section_aggregate.py",
            "ts": ts,
        },
    }
    output_entries.append(entry)

# ─────────────────────────────────────────────────────────────────────────────
# Report
# ─────────────────────────────────────────────────────────────────────────────

from collections import Counter

total_sections = len(output_entries)
vc = Counter(e["aggregate_verdict"] for e in output_entries)
fc = Counter(fp for e in output_entries for fp in e["failure_patterns"])

print(f"\n{'='*60}")
print(f"P4b Aggregation complete: {total_sections} sections")
print(f"{'='*60}")
print("\nAggregate verdict distribution:")
for v in VERDICT_PRIORITY:
    c = vc.get(v, 0)
    bar = "█" * (c * 30 // max(vc.values(), default=1))
    print(f"  {v:<22} {c:4d}  {bar}")

print("\nFailure pattern counts:")
for fp, c in fc.most_common():
    print(f"  {fp:<22} {c}")

skeleton = [e for e in output_entries if e["aggregate_verdict"] == "SKELETON_ONLY"]
heading_miss = [e for e in output_entries if e["heading_missing_detected"]]
sibling_drop = [e for e in output_entries if "SIBLING_DROPPED" in e["failure_patterns"]]
struct_drift = [e for e in output_entries if "STRUCTURE_DRIFTED" in e["failure_patterns"]]
kw_level1 = [e for e in output_entries if e["keyword_flag"] == "level1"]

print(f"\nKey counts:")
print(f"  SKELETON_ONLY sections:    {len(skeleton)}")
print(f"  HEADING_MISSING sections:  {len(heading_miss)}")
print(f"  SIBLING_DROPPED sections:  {len(sibling_drop)}")
print(f"  STRUCTURE_DRIFTED sections:{len(struct_drift)}")
print(f"  Level-1 keyword flag:      {len(kw_level1)}")

# Gate check per PLAN §9.2
print(f"\n{'='*60}")
print("P4b Gate pre-check:")
gate_pass = True
if skeleton:
    print(f"  ⚠ {len(skeleton)} SKELETON_ONLY sections (need INTENTIONAL_EXCLUDE or Issue)")
    gate_pass = False
else:
    print("  ✅ 0 SKELETON_ONLY (gate §9.2 condition met)")
if sibling_drop:
    print(f"  ⚠ {len(sibling_drop)} SIBLING_DROPPED sections (need Issues)")
if struct_drift:
    print(f"  ⚠ {len(struct_drift)} STRUCTURE_DRIFTED sections (need repair)")

# ─────────────────────────────────────────────────────────────────────────────
# Write output
# ─────────────────────────────────────────────────────────────────────────────

out_path = f"{BASE}/section_coverage.jsonl"
with open(out_path, "w", encoding="utf-8") as f:
    for e in output_entries:
        f.write(json.dumps(e, ensure_ascii=False) + "\n")

print(f"\n✅ Wrote {out_path} ({total_sections} lines)")
