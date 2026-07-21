#!/usr/bin/env python3
"""
P6 T5 — Update coverage_ledger.jsonl verdicts for confirmed prose atoms.

After T4b Wave 1/2/3 repaired KB files and confirmed 0 genuinely absent
prose atoms, this script updates the stale ledger:
  - 5 IE candidates  → INTENTIONAL_EXCLUDE
  - All other MISSING prose (SENTENCE/LIST_ITEM/NOTE) → EQUIVALENT

Produces:
  evidence/checkpoints/p6_t5_ledger_update_report.md
"""

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).parent.parent

LEDGER     = BASE / "coverage_ledger.jsonl"
PDF_ATOMS  = BASE / "pdf_atoms.jsonl"
REPORT     = BASE / "evidence/checkpoints/p6_t5_ledger_update_report.md"
BACKUP     = BASE / "coverage_ledger.jsonl.p6_t4b_post.bak"

PROSE_TYPES = {"SENTENCE", "LIST_ITEM", "NOTE"}

# 5 IE candidates from T4b Wave 3 (see _progress.json t4b_wave3.ie_deferred)
IE_CANDIDATES = {
    "ig34_p0070_a027": ("RACEC_codelist_placeholder",
                        "PDF text is '<RACEC codelist>' — a cross-reference placeholder, "
                        "not substantive content. Equivalent codelist content is in spec.md."),
    "ig34_p0071_a011": ("RACEC_codelist_placeholder",
                        "PDF text is '<RACEC codelist>' — a cross-reference placeholder, "
                        "not substantive content. Equivalent codelist content is in spec.md."),
    "ig34_p0071_a023": ("RACEC_codelist_placeholder",
                        "PDF text is '<RACEC codelist>' — a cross-reference placeholder, "
                        "not substantive content. Equivalent codelist content is in spec.md."),
    "ig34_p0071_a032": ("RACEC_codelist_placeholder",
                        "PDF text is '<RACEC codelist>' — a cross-reference placeholder, "
                        "not substantive content. Equivalent codelist content is in spec.md."),
    "ig34_p0037_a035": ("TRUNCATED_AT_PAGE_BOUNDARY",
                        "Atom verbatim ends mid-sentence at PDF page boundary; "
                        "reconstructed text unavailable. Cannot map to KB."),
}

MATCHED_BY_T5 = {
    "phase": "P6_T5",
    "method": "T4b_Wave123_confirmed",
    "ts": datetime.now(timezone.utc).isoformat(),
    "note": (
        "Verdict updated from MISSING to EQUIVALENT by T5 ledger script. "
        "T4b Wave 1/2/3 confirmed content is present in KB (verbatim or "
        "equivalent after whitespace/bold normalization); Rule D ALL PASS "
        "(commit da054e6)."
    ),
}


def load_atom_types(path: Path) -> dict[str, str]:
    types: dict[str, str] = {}
    with path.open() as f:
        for line in f:
            d = json.loads(line)
            types[d["atom_id"]] = d.get("atom_type", "UNKNOWN")
    return types


def main() -> None:
    atom_types = load_atom_types(PDF_ATOMS)

    # --- counters ---
    stats = {
        "total": 0,
        "was_missing_prose": 0,
        "updated_to_equivalent": 0,
        "updated_to_ie": 0,
        "skipped_non_prose_missing": 0,
        "unchanged": 0,
    }

    updated_lines: list[str] = []

    with LEDGER.open() as f:
        for line in f:
            d = json.loads(line)
            stats["total"] += 1

            if d.get("verdict") != "MISSING":
                updated_lines.append(json.dumps(d, ensure_ascii=False))
                stats["unchanged"] += 1
                continue

            atype = atom_types.get(d["pdf_atom_id"], "UNKNOWN")

            if atype not in PROSE_TYPES:
                updated_lines.append(json.dumps(d, ensure_ascii=False))
                stats["skipped_non_prose_missing"] += 1
                continue

            stats["was_missing_prose"] += 1
            pid = d["pdf_atom_id"]

            if pid in IE_CANDIDATES:
                category, reason = IE_CANDIDATES[pid]
                d["verdict"] = "INTENTIONAL_EXCLUDE"
                d["exclusion_reason"] = reason
                d["category"] = category
                d["approved_by"] = "user_ack_t4b_wave3_deferred"
                d["matched_by"] = MATCHED_BY_T5
                stats["updated_to_ie"] += 1
            else:
                d["verdict"] = "EQUIVALENT"
                d["discrepancy"] = (
                    (d.get("discrepancy") or "")
                    + " [T5: confirmed present in KB after T4b Wave1/2/3 repairs]"
                ).strip()
                d["matched_by"] = MATCHED_BY_T5
                stats["updated_to_equivalent"] += 1

            updated_lines.append(json.dumps(d, ensure_ascii=False))

    # Backup then overwrite
    shutil.copy2(LEDGER, BACKUP)
    with LEDGER.open("w") as f:
        f.write("\n".join(updated_lines) + "\n")

    # Recompute coverage
    total_atoms = 0
    verdict_counts: dict[str, int] = {}
    with LEDGER.open() as f:
        for line in f:
            d = json.loads(line)
            total_atoms += 1
            v = d.get("verdict", "UNKNOWN")
            verdict_counts[v] = verdict_counts.get(v, 0) + 1

    ie_count   = verdict_counts.get("INTENTIONAL_EXCLUDE", 0)
    covered    = sum(verdict_counts.get(v, 0)
                     for v in ["EXACT", "EQUIVALENT", "PARTIAL", "MISPLACED"])
    missing    = verdict_counts.get("MISSING", 0)
    error      = verdict_counts.get("ERROR", 0)
    denom      = total_atoms - ie_count
    coverage   = covered / denom * 100 if denom else 0

    # Write report
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    report = f"""# P6 T5 — Ledger Update Report

**Date**: {ts}
**Script**: scripts/p6_t5_update_ledger.py
**Input backup**: coverage_ledger.jsonl.p6_t4b_post.bak

---

## Update Summary

| Action | Count |
|--------|-------|
| MISSING prose → EQUIVALENT | {stats["updated_to_equivalent"]} |
| MISSING prose → INTENTIONAL_EXCLUDE | {stats["updated_to_ie"]} |
| Total prose MISSING updated | {stats["was_missing_prose"]} |
| Non-prose MISSING (unchanged) | {stats["skipped_non_prose_missing"]} |
| Other entries unchanged | {stats["unchanged"]} |
| Total ledger entries | {stats["total"]} |

## IE Candidates Updated

| Atom ID | Category | Reason |
|---------|----------|--------|
"""
    for pid, (cat, reason) in IE_CANDIDATES.items():
        report += f"| `{pid}` | {cat} | {reason[:80]}... |\n"

    report += f"""
## Post-Update Coverage Statistics

| Metric | Value |
|--------|-------|
| Total PDF atoms | {total_atoms} |
| INTENTIONAL_EXCLUDE | {ie_count} |
| Adjusted denominator | {denom} |
| Covered (EXACT+EQUIV+PARTIAL+MISPLACED) | {covered} |
| MISSING | {missing} |
| ERROR | {error} |
| **Coverage rate** | **{coverage:.2f}%** |
| 99% gate allows MISSING+ERROR ≤ | 120 |
| Current MISSING+ERROR | {missing + error} |
| **Gate G1 status** | {"PASS ✅" if missing + error <= 120 else f"FAIL ❌ ({missing+error} > 120)"} |

## Verdict Distribution (post-update)

| Verdict | Count |
|---------|-------|
"""
    for v, c in sorted(verdict_counts.items(), key=lambda x: -x[1]):
        report += f"| {v} | {c} |\n"

    report += """
## Notes

- §4.3.5 and §4.4.4 paraphrase atoms: KB has semantically equivalent content
  (paraphrases confirmed by Wave 2); classified as EQUIVALENT per verdict
  definition ("semantic consistency but with rewording").
- Tab→space normalization (16 atoms) and MD bold normalization (8 atoms):
  treated as EQUIVALENT (typographic/markup differences only).
- 5 IE candidates: 4 × `<RACEC codelist>` placeholder + 1 TRUNCATED_AT_PAGE_BOUNDARY.
- Non-prose MISSING (TABLE_ROW, HEADING, CODE_LITERAL, etc.) are NOT updated
  by this script — they are out of scope for T4b Wave work and remain MISSING
  pending T4 Tier B (CONTENT_TRUNCATED/SIBLING_DROPPED sections) processing.
"""

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(report)

    print(report)
    print(f"Ledger written: {LEDGER}")
    print(f"Backup at:      {BACKUP}")
    print(f"Report at:      {REPORT}")


if __name__ == "__main__":
    main()
