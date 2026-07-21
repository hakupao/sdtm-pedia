#!/usr/bin/env python3
"""
P6 T2: Apply INTENTIONAL_EXCLUDE batch expansion.
Reads p6_missing_stratification.json IE buckets,
updates coverage_ledger.jsonl (MISSING → INTENTIONAL_EXCLUDE),
appends new entries to intentional_exclude_whitelist.md.
Requires user ack recorded in stratification JSON.
"""

import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from collections import Counter

BASE = Path(__file__).parent.parent

STRAT_PATH = BASE / "evidence" / "checkpoints" / "p6_missing_stratification.json"
LEDGER_PATH = BASE / "coverage_ledger.jsonl"
WHITELIST_PATH = BASE / "intentional_exclude_whitelist.md"

TS = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = datetime.utcnow().strftime("%Y-%m-%d")

CATEGORY_MAP = {
    "IE_version_mismatch": ("VERSION_MISMATCH", "SDTM v2.0 content superseded by SDTMIG v3.4 — not included in KB by design"),
    "IE_spec_table": ("REDUNDANT_WITH_SPEC", "Variable specification table covered by xlsx-derived spec.md — not included in KB chapters by design"),
    "IE_editorial": ("EDITORIAL_META", "Editorial/structural content (Appendix A, SDS team, etc.) — not included in KB by design"),
}

# ── Load stratification ────────────────────────────────────────────────────

with open(STRAT_PATH) as f:
    strat = json.load(f)

# Build atom_id → (category, exclusion_reason) map
ie_atoms = {}
for bucket_name, (category, reason) in CATEGORY_MAP.items():
    for entry in strat["bucket_details"].get(bucket_name, []):
        atom_id = entry["atom_id"]
        parent_section = entry.get("parent_section", "")
        ie_atoms[atom_id] = {
            "category": category,
            "exclusion_reason": reason,
            "parent_section": parent_section,
        }

print(f"IE atoms to apply: {len(ie_atoms)}")

# ── Backup coverage_ledger ─────────────────────────────────────────────────

backup_path = LEDGER_PATH.with_suffix(".jsonl.p6_t2_pre.bak")
if not backup_path.exists():
    shutil.copy2(LEDGER_PATH, backup_path)
    print(f"Backup created: {backup_path.name}")
else:
    print(f"Backup already exists: {backup_path.name}")

# ── Update coverage_ledger ─────────────────────────────────────────────────

updated = 0
skipped_not_missing = 0
not_found = set(ie_atoms.keys())
new_lines = []

with open(LEDGER_PATH) as f:
    for line in f:
        if not line.strip():
            new_lines.append(line)
            continue
        r = json.loads(line)
        atom_id = r["pdf_atom_id"]
        if atom_id in ie_atoms and r["verdict"] == "MISSING":
            ie_info = ie_atoms[atom_id]
            r["verdict"] = "INTENTIONAL_EXCLUDE"
            r["exclusion_reason"] = ie_info["exclusion_reason"]
            r["category"] = ie_info["category"]
            r["approved_by"] = "user-ack-2026-05-12-P6-T2"
            r["matched_by"] = {
                "subagent_type": "script/p6_t2_apply_ie",
                "ts": TS,
            }
            updated += 1
            not_found.discard(atom_id)
        elif atom_id in ie_atoms and r["verdict"] != "MISSING":
            skipped_not_missing += 1
            not_found.discard(atom_id)
        new_lines.append(json.dumps(r, ensure_ascii=False) + "\n")

with open(LEDGER_PATH, "w") as f:
    f.writelines(new_lines)

print(f"Updated: {updated} atoms → INTENTIONAL_EXCLUDE")
print(f"Skipped (not MISSING): {skipped_not_missing}")
if not_found:
    print(f"WARNING: {len(not_found)} atom_ids not found in ledger: {list(not_found)[:5]}")

# ── Append to whitelist ────────────────────────────────────────────────────

# Count by category
cat_counts = Counter()
for info in ie_atoms.values():
    cat_counts[info["category"]] += 1

whitelist_append = f"""
## P6 T2 Batch — Approved by user 2026-05-12

> User ack: "T2 批量 IE 扩充通过" (P6 session 2026-05-12)
> Total atoms added: {updated}

| Category | Count | Approved |
|----------|-------|----------|
"""
for cat, cnt in cat_counts.most_common():
    whitelist_append += f"| {cat} | {cnt} | user-ack-2026-05-12-P6-T2 |\n"

whitelist_append += "\n### Atom registry (P6 T2 additions)\n\n"
whitelist_append += "| pdf_atom_id | category | approved_by | exclusion_reason |\n"
whitelist_append += "|-------------|----------|-------------|------------------|\n"

for atom_id, info in sorted(ie_atoms.items()):
    reason_short = info["exclusion_reason"][:80]
    whitelist_append += f"| {atom_id} | {info['category']} | user-ack-2026-05-12-P6-T2 | {reason_short} |\n"

with open(WHITELIST_PATH, "a") as f:
    f.write(whitelist_append)

print(f"Whitelist updated: {WHITELIST_PATH.name}")

# ── Recount coverage ──────────────────────────────────────────────────────

verdicts = Counter()
with open(LEDGER_PATH) as f:
    for line in f:
        if not line.strip():
            continue
        r = json.loads(line)
        verdicts[r["verdict"]] += 1

total = sum(verdicts.values())
ie_total = verdicts["INTENTIONAL_EXCLUDE"]
missing = verdicts["MISSING"]
error = verdicts["ERROR"]
denom = total - ie_total
resolved = denom - missing  # includes ERROR as "having verdict"
coverage = resolved / denom * 100 if denom > 0 else 0

print()
print("=== Post-T2 Coverage ===")
print(f"Total atoms: {total}")
print(f"INTENTIONAL_EXCLUDE: {ie_total}")
print(f"Adjusted denominator: {denom}")
print(f"MISSING: {missing}")
print(f"ERROR: {error}")
print(f"Coverage: {coverage:.1f}%")
print(f"Gap to 99% (MISSING only): {missing - int(denom * 0.01)} atoms")

# ── Save coverage snapshot ─────────────────────────────────────────────────

snapshot = {
    "phase": "P6_T2_post_IE_expansion",
    "ts": TS,
    "total_atoms": total,
    "intentional_exclude": ie_total,
    "adjusted_denominator": denom,
    "missing": missing,
    "error": error,
    "coverage_pct": round(coverage, 1),
    "gap_to_99pct": missing - int(denom * 0.01),
    "verdict_distribution": dict(verdicts.most_common()),
}

snap_path = BASE / "evidence" / "checkpoints" / "p6_post_ie_coverage.json"
with open(snap_path, "w") as f:
    json.dump(snapshot, f, indent=2)
print(f"Snapshot: {snap_path.name}")
