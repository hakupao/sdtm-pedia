#!/usr/bin/env python3
"""
P6 T1: MISSING atom stratification script.
Reads coverage_ledger.jsonl and section_coverage.jsonl,
classifies each MISSING atom into one of 5 buckets:
  IE_version_mismatch  - sv20 superseded content
  IE_spec_table        - variable spec table rows (REDUNDANT_WITH_SPEC)
  IE_editorial         - editorial/structural atoms
  HIGH_content_gap     - in SKELETON_ONLY or STRUCTURE_DRIFTED sections
  MEDIUM_partial       - remaining MISSING in other sections

Outputs: evidence/checkpoints/p6_missing_stratification.json
"""

import json
import re
from pathlib import Path
from collections import defaultdict, Counter

BASE = Path(__file__).parent.parent

# ── Load pdf_atoms lookup: atom_id → parent_section, atom_type, page ──────

atom_meta = {}  # atom_id -> {parent_section, atom_type, page}
with open(BASE / "pdf_atoms.jsonl") as f:
    for line in f:
        if not line.strip():
            continue
        a = json.loads(line)
        atom_meta[a["atom_id"]] = {
            "parent_section": a.get("parent_section", ""),
            "atom_type": a.get("atom_type", ""),
            "page": a.get("page", 0),
        }

# ── Load section_coverage ──────────────────────────────────────────────────

section_verdict = {}   # section_id -> aggregate_verdict
section_title = {}

with open(BASE / "section_coverage.jsonl") as f:
    for line in f:
        if not line.strip():
            continue
        s = json.loads(line)
        sid = s["section_id"]
        # There may be duplicate section_ids with different titles; take first
        if sid not in section_verdict:
            section_verdict[sid] = s["aggregate_verdict"]
            section_title[sid] = s.get("section_title", "")

HIGH_VERDICTS = {"SKELETON_ONLY", "STRUCTURE_DRIFTED"}

# ── sv20 superseded sections (SDTM v2.0 content wholly or mostly replaced) ─
# These are sections where the KB chose to represent the ig34 version only.
# All MISSING atoms from sv20 source are VERSION_MISMATCH candidates.
SV20_SUPERSEDED_SECTIONS = {
    "sv20_§1.4", "sv20_§2.2", "sv20_§3", "sv20_§3.1",
    "sv20_§3.1.1", "sv20_§3.1.2", "sv20_§3.1.3", "sv20_§3.1.3.1",
    "sv20_§3.1.4", "sv20_§3.1.5", "sv20_§3.2", "sv20_§3.2.1",
    "sv20_§3.2.2", "sv20_§3.2.3", "sv20_§3.2.3.3", "sv20_§3.2.3.4",
    "sv20_§4", "sv20_§5.1.4", "sv20_§5.1.7", "sv20_§5.2.1",
    "sv20_§5.2.2", "sv20_§6", "sv20_§6.2", "sv20_§6.3",
    "sv20_§6.4", "sv20_§6.5", "sv20_§7", "sv20_§8",
}

# ── Spec-table sections (variable specifications covered by spec.md/xlsx) ──
SPEC_TABLE_SECTIONS = {
    "ig34_RELREC_Specification", "ig34_RELSPEC_Specification",
    "ig34_RELSUB_Specification", "ig34_SR_Specification",
    "ig34_SS_Specification", "ig34_TU_Specification",
    "ig34_VS_Specification",
    "ig34_§7.2.1",   # Trial Arms (TA) – Specification
    "ig34_§7.2.2",   # Trial Elements (TE) – Specification
    "ig34_§7.3.1",   # Trial Visits (TV) – Specification
    "ig34_§7.3.2",   # Trial Disease Assessments (TD) – Specification
    "ig34_§7.4.1",   # Trial Inclusion/Exclusion Criteria (TI) – Specification
    "ig34_§7.4.2",   # Trial Summary (TS) – Specification
}

# ── Editorial/structural sections ─────────────────────────────────────────
EDITORIAL_SECTIONS = {
    "ig34_§0",          # Cover + ToC (multiple entries)
    "ig34_Appendix_A_CDISC_SDS_Team",
    "sv20_§0",
}

EDITORIAL_KEYWORDS = {
    "appendix a", "cdisc sds team", "cover", "table of contents",
    "acknowledgement", "foreword", "preface",
}

def is_editorial(atom_id: str, parent_section: str, page: int) -> bool:
    if atom_id.startswith("ig34") and page <= 3:
        return True
    if atom_id.startswith("sv20") and page <= 2:
        return True
    ps_lower = parent_section.lower()
    return any(kw in ps_lower for kw in EDITORIAL_KEYWORDS)


# ── Main stratification ────────────────────────────────────────────────────

buckets = defaultdict(list)
section_to_bucket = defaultdict(Counter)

with open(BASE / "coverage_ledger.jsonl") as f:
    for line in f:
        if not line.strip():
            continue
        r = json.loads(line)
        if r.get("verdict") != "MISSING":
            continue

        atom_id = r["pdf_atom_id"]
        meta = atom_meta.get(atom_id, {})
        parent_section = meta.get("parent_section", "")
        atom_type = meta.get("atom_type", "")
        page = meta.get("page", 0)

        ps_norm = parent_section.strip()
        source_prefix = "sv20" if atom_id.startswith("sv20") else "ig34"

        # Check IE_version_mismatch: sv20 atoms
        if source_prefix == "sv20":
            buckets["IE_version_mismatch"].append({
                "atom_id": atom_id,
                "parent_section": parent_section,
                "reason": "sv20 source — VERSION_MISMATCH candidate (SDTM v2.0 superseded by v3.4)",
            })
            continue

        # Check IE_editorial
        if is_editorial(atom_id, parent_section, page):
            buckets["IE_editorial"].append({
                "atom_id": atom_id,
                "parent_section": parent_section,
                "reason": "Editorial/structural content — EDITORIAL_META candidate",
            })
            continue

        # Check IE_spec_table: parent_section ends with "– Specification"
        # (exact domain spec tables covered by xlsx-derived spec.md)
        # Pattern: "DOMAIN – Specification" or "§X.Y Title (XX) – Specification"
        is_spec = bool(re.search(r"[–\-]\s*Specification\s*$", parent_section))
        if is_spec:
            buckets["IE_spec_table"].append({
                "atom_id": atom_id,
                "parent_section": parent_section,
                "reason": "Variable specification table — REDUNDANT_WITH_SPEC candidate (spec.md xlsx-derived covers this)",
            })
            continue

        # Check HIGH_content_gap: look up section verdict via parent_section
        # parent_section format: "§X.Y.Z [Title]" — extract section number
        matched_verdict = None
        sec_num_match = re.match(r"(§[\d\.]+)", ps_norm)
        if sec_num_match:
            sec_num = sec_num_match.group(1).rstrip(".")
            candidate_key = f"{source_prefix}_{sec_num}"
            matched_verdict = section_verdict.get(candidate_key)

        if matched_verdict in HIGH_VERDICTS:
            buckets["HIGH_content_gap"].append({
                "atom_id": atom_id,
                "parent_section": parent_section,
                "section_verdict": matched_verdict,
                "reason": f"Section verdict {matched_verdict} — real content gap",
            })
        else:
            buckets["MEDIUM_partial"].append({
                "atom_id": atom_id,
                "parent_section": parent_section,
                "section_verdict": matched_verdict or "unknown",
                "reason": "Remaining MISSING in non-HIGH section",
            })

# ── Summary ────────────────────────────────────────────────────────────────

summary = {
    "total_missing": sum(len(v) for v in buckets.values()),
    "buckets": {k: len(v) for k, v in buckets.items()},
    "ie_total": (
        len(buckets["IE_version_mismatch"])
        + len(buckets["IE_spec_table"])
        + len(buckets["IE_editorial"])
    ),
    "ie_existing": 394,
}
summary["ie_new_total"] = summary["ie_total"]
summary["ie_grand_total"] = summary["ie_existing"] + summary["ie_new_total"]
summary["new_denominator"] = 12093 - summary["ie_new_total"]
gap_after_ie = (
    2502 - summary["ie_new_total"]  # remaining MISSING after IE
    + 93   # ERROR (unchanged)
)
summary["remaining_missing_after_ie"] = 2502 - summary["ie_new_total"]
summary["remaining_error"] = 93
summary["gap_after_ie"] = gap_after_ie
summary["projected_coverage_after_ie"] = round(
    (summary["new_denominator"] - gap_after_ie) / summary["new_denominator"] * 100, 1
) if summary["new_denominator"] > 0 else 0

output_path = BASE / "evidence" / "checkpoints" / "p6_missing_stratification.json"
output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w") as f:
    json.dump({
        "summary": summary,
        "bucket_details": {k: v for k, v in buckets.items()},
    }, f, indent=2, ensure_ascii=False)

print("=== P6 T1: MISSING Stratification ===")
print(f"Total MISSING: {summary['total_missing']}")
print()
print("Bucket breakdown:")
for bucket, count in summary["buckets"].items():
    print(f"  {bucket}: {count}")
print()
print(f"IE candidates (new): {summary['ie_total']}")
print(f"  IE_version_mismatch: {len(buckets['IE_version_mismatch'])}")
print(f"  IE_spec_table:       {len(buckets['IE_spec_table'])}")
print(f"  IE_editorial:        {len(buckets['IE_editorial'])}")
print()
print(f"After IE expansion:")
print(f"  New denominator: {summary['new_denominator']}")
print(f"  Remaining MISSING: {summary['remaining_missing_after_ie']}")
print(f"  Remaining ERROR:   {summary['remaining_error']}")
print(f"  Gap to 99%:        {summary['gap_after_ie'] - int(summary['new_denominator'] * 0.01)} atoms (still need repair)")
print(f"  Projected coverage: {summary['projected_coverage_after_ie']}%")
print()
print(f"Output: {output_path}")
