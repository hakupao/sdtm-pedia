"""
P7 Human Sampling — Stratified random sample generator
Output: evidence/checkpoints/p7_sample_sheet.md

Stratification plan (60 atoms):
  EXACT          12
  EQUIVALENT     18
  PARTIAL        12
  INTENTIONAL_EXCLUDE  8
  MISPLACED       4
  ERROR           4
  MISSING         2  (all 9 are FIGURE-deferred; take first 2)
  TOTAL          60
"""

import json
import random
import sys
from pathlib import Path
from collections import defaultdict

SEED = 20260512
BASE = Path(__file__).parent.parent

LEDGER   = BASE / "coverage_ledger.jsonl"
PDF_ATOMS = BASE / "pdf_atoms.jsonl"
MD_ATOMS  = BASE / "md_atoms.jsonl"
OUT_MD    = BASE / "evidence/checkpoints/p7_sample_sheet.md"

STRATA = {
    "EXACT": 12,
    "EQUIVALENT": 18,
    "PARTIAL": 12,
    "INTENTIONAL_EXCLUDE": 8,
    "MISPLACED": 4,
    "ERROR": 4,
    "MISSING": 2,
}

def load_jsonl(path):
    rows = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            key = obj.get("atom_id") or obj.get("pdf_atom_id")
            rows[key] = obj
    return rows

def main():
    print("Loading ledger …", flush=True)
    pdf_map  = load_jsonl(PDF_ATOMS)
    md_map   = load_jsonl(MD_ATOMS)

    buckets = defaultdict(list)
    with open(LEDGER, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            v = rec.get("verdict", "")
            if v in STRATA:
                buckets[v].append(rec)

    print("Verdict counts:", {k: len(v) for k, v in buckets.items()})

    rng = random.Random(SEED)
    sample = []
    for verdict, n in STRATA.items():
        pool = buckets[verdict]
        chosen = rng.sample(pool, min(n, len(pool)))
        sample.extend(chosen)

    print(f"Total sampled: {len(sample)}")

    # Build output
    lines = []
    lines.append("# P7 人工抽样复检工作表\n")
    lines.append(f"> 生成时间: 2026-05-12  |  总计: {len(sample)} 原子  |  seed={SEED}\n")
    lines.append("> **用户复检说明**: 每条原子阅读「PDF 原文」和「匹配 KB 内容」，在「你的判定」栏填 `CORRECT` 或 `WRONG: <建议verdict>`\n")
    lines.append("> 误判容限: ≤3/60 → PASS；4+ → 需 root cause 分析\n\n")
    lines.append("---\n\n")

    # Group by verdict for readability
    by_verdict = defaultdict(list)
    for rec in sample:
        by_verdict[rec["verdict"]].append(rec)

    verdict_order = ["EXACT", "EQUIVALENT", "PARTIAL", "MISPLACED", "ERROR", "INTENTIONAL_EXCLUDE", "MISSING"]
    atom_num = 0

    for verdict in verdict_order:
        recs = by_verdict.get(verdict, [])
        if not recs:
            continue
        lines.append(f"## {verdict} ({len(recs)} atoms)\n\n")

        for rec in recs:
            atom_num += 1
            aid = rec["pdf_atom_id"]
            pa  = pdf_map.get(aid, {})
            source    = pa.get("source", "?")
            page      = pa.get("page", "?")
            atype     = pa.get("atom_type", "?")
            section   = pa.get("parent_section", "?")
            verbatim  = pa.get("verbatim", "(verbatim not found)")

            # Matched KB atoms
            md_ids = rec.get("md_atom_ids", [])
            kb_parts = []
            for mid in md_ids[:3]:  # show up to 3 matches
                ma = md_map.get(mid, {})
                kb_verbatim = ma.get("verbatim", "(not found)")
                kb_file = ma.get("file", "?")
                kb_parts.append(f"  - `{mid}` [{kb_file}]\n    > {kb_verbatim[:200]}")
            kb_block = "\n".join(kb_parts) if kb_parts else "  _(no matched KB atoms)_"

            excl = rec.get("exclusion_reason", "")
            disc = rec.get("discrepancy", "")
            sim  = rec.get("similarity_score")
            sim_str = f"{sim:.3f}" if sim is not None else "—"

            lines.append(f"### #{atom_num} `{aid}`\n")
            lines.append(f"- **Source**: {source} p.{page}  |  **Type**: {atype}  |  **Section**: {section}\n")
            lines.append(f"- **Verdict**: `{verdict}`  |  **Similarity**: {sim_str}\n")
            if disc:
                lines.append(f"- **Discrepancy**: {disc}\n")
            if excl:
                lines.append(f"- **Exclusion reason**: {excl}\n")
            lines.append(f"\n**PDF 原文**:\n> {verbatim[:400]}\n")
            lines.append(f"\n**匹配 KB 内容**:\n{kb_block}\n")
            lines.append(f"\n**你的判定**: ______\n\n---\n\n")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("".join(lines), encoding="utf-8")
    print(f"Written: {OUT_MD}")

if __name__ == "__main__":
    main()
