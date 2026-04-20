#!/usr/bin/env python3
"""Catalog knowledge_base/terminology/ into a compact mapping table (Phase 6.5 Step 9).

Reads the 91 terminology markdown files (1944K tokens total) and emits a one-line-per-codelist
mapping at ai_platforms/claude_projects/output/08_terminology_map.md. Target: <=15K tokens
(99% compression — the actual Term rows are the heavy bytes and are dropped on purpose).

Compression strategy (per PLAN.md 4.3.4 / D4):
- Parse each codelist header `## <Name> (Cxxxxx)` + `Extensible: Yes|No` line + table rows.
- Emit ONE row per codelist: | CT Code | Name | Data Type | Ext | Terms | Related Domain(s) | Source File |
- Drop every Term value (Code / Submission Value / Synonym / Definition).
- Related Domain inferred from filename via SUBDIR_DOMAIN_MAP.
- Data Type is always "Char" (CDISC controlled terminology is text-only by design).

Source is read-only (P5). Output is deterministic (P7: idempotent, uses source file mtime
instead of datetime.now()).
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC_DIR = ROOT / "knowledge_base" / "terminology"
OUT = ROOT / "ai_platforms" / "claude_projects" / "output" / "08_terminology_map.md"

SUBDIRS = ("core", "questionnaires", "supplementary")

# Map filename stem -> Related Domain(s). core/ has the most variance; questionnaires and
# supplementary are uniform.
CORE_DOMAIN_MAP: dict[str, str] = {
    "ae": "AE",
    "cp_part1": "CP",
    "cp_part2": "CP",
    "disposition": "DS",
    "dm": "DM",
    "eg_part1": "EG",
    "eg_part2": "EG",
    "eg_part3": "EG",
    "findings_about": "FA",
    "general_part1": "Cross-domain",
    "general_part2": "Cross-domain",
    "general_part3": "Cross-domain",
    "general_part4": "Cross-domain",
    "general_part5": "Cross-domain",
    "gf": "GF",
    "interventions": "CM/EX/EC/PR/SU",
    "is_domain_part1": "IS",
    "is_domain_part2": "IS",
    "lb_part1": "LB",
    "lb_part2": "LB",
    "lb_part3": "LB",
    "lb_part4": "LB",
    "mi": "MI",
    "microbiology_part1": "MB/MS",
    "microbiology_part2": "MB/MS",
    "microbiology_part3": "MB/MS",
    "oi": "OI",
    "oncology_part1": "TU/TR/RS",
    "oncology_part2": "TU/TR/RS",
    "other_part1": "Cross-domain",
    "other_part2": "Cross-domain",
    "other_part3": "Cross-domain",
    "other_part4": "Cross-domain",
    "other_part5": "Cross-domain",
    "pk_part1": "PC/PP",
    "pk_part2": "PC/PP",
    "pk_part3": "PC/PP",
    "pk_part4": "PC/PP",
    "qs_part1": "QS",
    "special_purpose": "DM/CO/SE/SM/SV",
    "trial_design": "TA/TD/TE/TI/TM/TS/TV",
    "vs": "VS",
}

# Regex: codelist heading like "## Action Taken with Study Treatment (C66767)"
HEADING_RE = re.compile(r"^##\s+(?P<name>.+?)\s+\((?P<code>C\d+)\)\s*$")
# Regex: "Extensible: Yes" or "Extensible: No"
EXT_RE = re.compile(r"^Extensible:\s*(Yes|No)\s*$", re.IGNORECASE)
# Regex: data row starting with "| Cxxxxx |" (excludes header + divider)
DATA_ROW_RE = re.compile(r"^\|\s*C\d+\s*\|")


def related_domain_for(path: Path) -> str:
    """Infer Related Domain(s) from a terminology file path."""
    subdir = path.parent.name
    stem = path.stem
    if subdir == "core":
        return CORE_DOMAIN_MAP.get(stem, "Cross-domain")
    if subdir == "questionnaires":
        return "QS"
    if subdir == "supplementary":
        return "Cross-domain"
    return "Cross-domain"


def format_terms(n: int) -> str:
    """Bucket term counts to reduce jitter (but mapping is lossless-per-codelist)."""
    if n <= 0:
        return "0"
    if n < 10:
        return str(n)
    if n < 50:
        return str(n)
    if n < 100:
        return str(n)
    if n < 500:
        return f"{n}"
    if n < 1000:
        return "500+"
    return "1000+"


def parse_file(path: Path) -> list[dict]:
    """Parse one terminology markdown file into a list of codelist records."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    records: list[dict] = []

    current: dict | None = None
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            # Close out previous codelist
            if current is not None:
                records.append(current)
            current = {
                "code": m.group("code"),
                "name": m.group("name").strip(),
                "ext": "",
                "terms": 0,
            }
            continue
        if current is None:
            continue
        m_ext = EXT_RE.match(line)
        if m_ext:
            current["ext"] = "Y" if m_ext.group(1).lower() == "yes" else "N"
            continue
        if DATA_ROW_RE.match(line):
            current["terms"] += 1
    if current is not None:
        records.append(current)
    return records


def iter_source_files() -> list[Path]:
    files: list[Path] = []
    for sub in SUBDIRS:
        d = SRC_DIR / sub
        if not d.is_dir():
            continue
        files.extend(sorted(d.glob("*.md")))
    return files


def source_mtime_stamp(files: list[Path]) -> str:
    """Return most recent source mtime as an ISO-like date for the header comment.

    Using source mtime (not datetime.now()) keeps the output deterministic for idempotency.
    """
    if not files:
        return "unknown"
    mt = max(f.stat().st_mtime for f in files)
    return datetime.fromtimestamp(mt, tz=timezone.utc).strftime("%Y-%m-%d")


def sanitize(text: str) -> str:
    """Make a cell safe for a markdown table: collapse whitespace, escape pipes."""
    return re.sub(r"\s+", " ", text).replace("|", "\\|").strip()


def build_output() -> tuple[str, dict]:
    files = iter_source_files()
    stamp = source_mtime_stamp(files)

    # Group records by (subdir, filename). Each file = one section; the section header
    # carries Related Domain + Source File, so each row only needs CT/Name/Ext/Terms.
    grouped: list[tuple[Path, str, list[dict]]] = []
    total_codelists = 0
    domain_specific = 0
    for f in files:
        recs = parse_file(f)
        if not recs:
            continue
        related = related_domain_for(f)
        grouped.append((f, related, recs))
        total_codelists += len(recs)
        if related and related != "Cross-domain":
            domain_specific += len(recs)

    lines: list[str] = []
    lines.append(
        f"<!-- generated by scripts/catalog_terminology.py (source mtime: {stamp}) -->"
    )
    lines.append(
        f"<!-- {len(files)} files -> {total_codelists} codelists; Term values intentionally omitted -->"
    )
    lines.append("")
    lines.append("# SDTM Controlled Terminology Map")
    lines.append("")
    lines.append(
        "Index of 1,005 CDISC SDTM CT codelists. Data Type is always Char. For specific "
        "Term values look up the Source File under `knowledge_base/terminology/`."
    )
    lines.append("")
    lines.append(
        "Columns: **CT**=codelist NCI code, **Name**=codelist name, **Ext**=extensible (Y/N), "
        "**Tm**=term count. Related Domain is in each section heading. Cross-domain = applies "
        "to many domains."
    )
    lines.append("")

    # Row format (tight): `CT_CODE E|F TERMS NAME` per line, no bullet marker.
    # Source file is the enclosing `### ` heading, which also carries the Related Domain.
    # No inline filename tag per row (extra tag added ~1 token * 1005 rows = 1K tokens).
    lines.append(
        "Row format: `CT_CODE E|F TERMS NAME`  (E=extensible, F=fixed). Source file and "
        "Related Domain are in the enclosing `### ` heading."
    )
    lines.append("")

    last_subdir: str | None = None
    subdir_titles = {
        "core": "## Core (terminology/core/) -- Related Domain varies per file",
        "questionnaires": "## Questionnaires (terminology/questionnaires/) -- all QS",
        "supplementary": "## Supplementary (terminology/supplementary/) -- Cross-domain",
    }
    for path, related, recs in grouped:
        subdir = path.parent.name
        if subdir != last_subdir:
            lines.append(subdir_titles.get(subdir, f"## {subdir}"))
            lines.append("")
            last_subdir = subdir

        lines.append(f"### `{path.name}` -> {related}")
        for rec in recs:
            ext_mark = "E" if rec["ext"] == "Y" else ("F" if rec["ext"] == "N" else "?")
            lines.append(
                f"{rec['code']} {ext_mark} {format_terms(rec['terms'])} "
                f"{sanitize(rec['name'])}"
            )
        lines.append("")

    stats = {
        "files": len(files),
        "codelists": total_codelists,
        "domain_mapped_specific": domain_specific,
        "domain_mapped_ratio": (domain_specific / total_codelists) if total_codelists else 0.0,
    }
    return "\n".join(lines) + "\n", stats


def main() -> int:
    if not SRC_DIR.is_dir():
        print(f"error: source dir not found: {SRC_DIR}", file=sys.stderr)
        return 2
    output, stats = build_output()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(output, encoding="utf-8")
    print(
        f"wrote {OUT} ({len(output)} chars, {len(output.splitlines())} lines, "
        f"{stats['codelists']} codelists from {stats['files']} files, "
        f"domain-specific coverage={stats['domain_mapped_specific']}/"
        f"{stats['codelists']})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
