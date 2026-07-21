#!/usr/bin/env python3
"""Catalog knowledge_base/domains/*/examples.md for Claude Projects (Phase 6.5 Step 8).

Emits a compressed directory file (target <=10000 tokens) at
ai_platforms/claude_projects/output/07_examples_catalog.md.

Strategy (per PLAN.md §3.2 D3 + §4.3.3):
- Drop all data tables and prose descriptions entirely.
- One-line summary (<=60 chars) per Example capturing key variables/scenario.
- Annotate EX/EC, MB/MS, TU/TR, PC/PP shared-example pairs.

Idempotence (P7):
- Timestamp in generated header is derived from max(mtime) of source files,
  not from datetime.now(), so running twice produces a byte-identical file.
- Source files are read-only (P5).

Fallback chain for content-free summaries (attempt 2):
1. prose keywords (scenario tags + var patterns) — existing logic
2. table column headers: domain-specific cols (skip STUDYID/DOMAIN/USUBJID/Row/
   <DOM>SEQ/EPOCH), take first 3
3. first data row: first 2 non-empty non-identifier cell values (<=40 chars each)
4. domain registry: hand-curated one-liners per domain
"""
from __future__ import annotations

import datetime as _dt
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DOMAINS_DIR = ROOT / "knowledge_base" / "domains"
OUT = ROOT / "ai_platforms" / "claude_projects" / "output" / "07_examples_catalog.md"

# Canonical domain order (alphabetical, matching directory listing)
DOMAINS = [
    "AE", "AG", "BE", "BS", "CE", "CM", "CO", "CP", "CV", "DA",
    "DD", "DM", "DS", "DV", "EC", "EG", "EX", "FA", "FT", "GF",
    "HO", "IE", "IS", "LB", "MB", "MH", "MI", "MK", "ML", "MS",
    "NV", "OE", "OI", "PC", "PE", "PP", "PR", "QS", "RE", "RELREC",
    "RELSPEC", "RELSUB", "RP", "RS", "SC", "SE", "SM", "SR", "SS",
    "SU", "SUPPQUAL", "SV", "TA", "TD", "TE", "TI", "TM", "TR",
    "TS", "TU", "TV", "UR", "VS",
]

# Shared-example pairs: (dom_a, dom_b, description_for_a, description_for_b)
SHARED_PAIRS = [
    ("EX", "EC",
     "Shares examples with EC (Exposure As Collected); see domain EC for collected-administration data and RELREC linkage.",
     "Shares examples with EX (Exposure); see domain EX for unmasked/actual drug data and RELREC linkage."),
    ("MB", "MS",
     "Shares examples with MS (Microbiology Susceptibility); see domain MS for susceptibility data from the same studies.",
     "Shares examples with MB (Microbiology Specimen); see domain MB for organism identification data from the same studies."),
    ("TU", "TR",
     "Shares examples with TR (Tumor Results); see domain TR for response/measurement data.",
     "Shares examples with TU (Tumor/Lesion Identification); see domain TU for lesion identification data."),
    ("PC", "PP",
     "Shares examples with PP (Pharmacokinetic Parameters); see domain PP for derived PK parameters and RELREC methods.",
     "Shares examples with PC (Pharmacokinetic Concentrations); see domain PC for concentration data and RELREC method descriptions."),
]

# Build lookup: dom -> sharing note
_SHARING_NOTE: dict[str, str] = {}
for _a, _b, _note_a, _note_b in SHARED_PAIRS:
    _SHARING_NOTE[_a] = _note_a
    _SHARING_NOTE[_b] = _note_b


# ---------------------------------------------------------------------------
# Domain registry: fallback description when all extraction fails
# ---------------------------------------------------------------------------

_DOMAIN_REGISTRY: dict[str, str] = {
    "AE": "adverse events with MedDRA coding",
    "AG": "allergen/agent administration (bronchial challenge)",
    "BE": "bioelectrical findings with device linkage",
    "BS": "biospecimen findings",
    "CE": "clinical events with prespecified checklist",
    "CM": "concomitant/prior medications",
    "CO": "comments linked across domains",
    "CP": "cell phenotyping (flow cytometry) findings",
    "CV": "cardiovascular findings",
    "DA": "drug accountability (dispensed/returned)",
    "DD": "death details (cause/location)",
    "DM": "demographics and disposition",
    "DS": "disposition events and protocol milestones",
    "DV": "protocol deviations",
    "EC": "exposure as collected (actual administration)",
    "EG": "ECG findings",
    "EX": "exposure (planned/unmasked drug data)",
    "FA": "findings about events/interventions",
    "FT": "functional tests",
    "GF": "genomic/genetic findings",
    "HO": "healthcare encounters",
    "IE": "inclusion/exclusion criteria",
    "IS": "immunogenicity specimen assessments",
    "LB": "laboratory test results",
    "MB": "microbiology specimen findings",
    "MH": "medical history",
    "MI": "microscopic findings",
    "MK": "musculoskeletal/connective tissue findings",
    "ML": "meal data (nutrition)",
    "MS": "microbiology susceptibility results",
    "NV": "nervous system findings",
    "OE": "ophthalmic examinations",
    "OI": "ophthalmic device findings",
    "PC": "pharmacokinetic concentrations",
    "PE": "physical examination findings",
    "PP": "pharmacokinetic parameters",
    "PR": "procedures performed",
    "QS": "questionnaire/rating scale scores",
    "RE": "respiratory system findings",
    "RELREC": "related records linkage dataset",
    "RELSPEC": "related specimens linkage",
    "RELSUB": "related subjects linkage",
    "RP": "reproductive system findings",
    "RS": "disease response and clin classification",
    "SC": "subject characteristics",
    "SE": "subject elements (treatment periods)",
    "SM": "study medications (trial arms)",
    "SR": "skin response findings",
    "SS": "subject status assessments",
    "SU": "substance use (tobacco/alcohol/drugs)",
    "SUPPQUAL": "supplemental qualifiers dataset",
    "SV": "subject visits (actual dates)",
    "TA": "trial arms definition",
    "TD": "trial disease assessments definition",
    "TE": "trial elements definition",
    "TI": "trial inclusion/exclusion criteria",
    "TM": "trial disease milestones definition",
    "TR": "tumor results (response/measurements)",
    "TS": "trial summary parameters",
    "TU": "tumor/lesion identification",
    "TV": "trial visits definition",
    "UR": "urinary system findings",
    "VS": "vital signs measurements",
}

# ---------------------------------------------------------------------------
# Key-variable extraction helpers
# ---------------------------------------------------------------------------

# Variables of interest to surface in one-liners (ordered by significance)
_VAR_PATTERNS = [
    # Domain-specific grouping / linking
    r'\b[A-Z]{2,4}GRPID\b',
    r'\b[A-Z]{2,4}LNKID\b',
    r'\b[A-Z]{2,4}REFID\b',
    r'\bRELREC\b',
    r'\bRELSPEC\b',
    r'\bRELSUB\b',
    # Prespecified / occurrence
    r'\b[A-Z]{2,4}PRESP\b',
    r'\b[A-Z]{2,4}OCCUR\b',
    # Important qualifiers
    r'\b[A-Z]{2,4}MODIFY\b',
    r'\bAEMODIFY\b',
    r'\bAESER\b',
    r'\bAEENRF\b',
    r'\b[A-Z]{2,4}ENRF\b',
    r'\b[A-Z]{2,4}ENTY\b',
    r'\b[A-Z]{2,4}STRF\b',
    r'\bAEPREASP\b',
    # Device-related
    r'\bAERLPRC\b', r'\bAERLPRT\b', r'\bAERELDEV\b', r'\bAEACNDEV\b',
    # MedDRA / coding
    r'\bMedDRA\b',
    # Laterality / location
    r'\b[A-Z]{2,4}LAT\b', r'\b[A-Z]{2,4}LOC\b',
    # Severity
    r'\b[A-Z]{2,4}SEV\b',
    # SUPPQUAL variables
    r'\bSUPP[A-Z]{2,4}\b',
    r'\bQNAM\b',
    # Timing relative refs
    r'\b[A-Z]{2,4}TPT\b', r'\b[A-Z]{2,4}TPTNUM\b',
]
_VAR_RE = re.compile('|'.join(_VAR_PATTERNS))

# Scenario-type keywords
_SCENARIO_KEYWORDS = [
    (r'\bprespecified\b', 'prespecified'),
    (r'\bpre-specified\b', 'prespecified'),
    (r'\bserious\b', 'serious'),
    (r'\bongoing\b', 'ongoing'),
    (r'\bgroup(?:ed|ing)\b', 'grouped'),
    (r'\bsupplement(?:al|ary)?\b', 'supplemental'),
    (r'\bnon-?occurrence\b', 'non-occurrence'),
    (r'\bmissed\s+dos(?:e|ing)\b', 'missed-dose'),
    (r'\bscreen\s+failure\b', 'screen-failure'),
    (r'\brandomiz\b', 'randomization'),
    (r'\bplacebo\b', 'placebo'),
    (r'\bblinded?\b', 'blind'),
    (r'\bdouble.blind\b', 'double-blind'),
    (r'\bopen.label\b', 'open-label'),
    (r'\bdevice\b', 'device'),
    (r'\bimplant\b', 'implant'),
    (r'\bsupplement(?:al|ary)?\b', 'SUPPQUAL'),
    (r'\brelat(?:e|ed|ing)\b', 'related'),
    (r'\bMedDRA\b', 'MedDRA'),
    (r'\bcod(?:e|ed|ing)\b', 'coded'),
    (r'\bunmask\b', 'unmasked'),
    (r'\bpharmacokinetic\b', 'PK'),
    (r'\btumor\b', 'tumor'),
    (r'\blesion\b', 'lesion'),
    (r'\bmicrobiology\b', 'microbiology'),
    (r'\bsusceptib\b', 'susceptibility'),
    (r'\bspecimen\b', 'specimen'),
    (r'\bexposure\b', 'exposure'),
    (r'\bconcomitant\b', 'concomitant'),
    (r'\bvital\s+sign\b', 'vitals'),
    (r'\bECG\b', 'ECG'),
    (r'\blaborator(?:y|ies)\b', 'lab'),
    (r'\bHbA1c\b', 'HbA1c'),
    (r'\bPCR\b', 'PCR'),
    (r'\bDNA\b', 'DNA'),
]
_SCENARIO_RES = [(re.compile(p, re.IGNORECASE), label) for p, label in _SCENARIO_KEYWORDS]


def _extract_variables(text: str) -> list[str]:
    """Return unique variable names found in text (preserving order)."""
    seen: set[str] = set()
    result: list[str] = []
    for m in _VAR_RE.finditer(text):
        v = m.group()
        if v not in seen:
            seen.add(v)
            result.append(v)
    return result


def _extract_scenario_tags(text: str) -> list[str]:
    """Return unique scenario labels found in text (preserving order of first match)."""
    seen: set[str] = set()
    result: list[str] = []
    for regex, label in _SCENARIO_RES:
        if regex.search(text) and label not in seen:
            seen.add(label)
            result.append(label)
    return result


# Common identifier columns to skip when extracting table-header fallback
_SKIP_COLS = frozenset({"ROW", "STUDYID", "DOMAIN", "USUBJID", "EPOCH"})
# Regex: <DOM>SEQ pattern (2-8 uppercase letters followed by SEQ)
_SEQ_RE = re.compile(r'^[A-Z]{2,8}SEQ$')


def _extract_table_headers(text: str, dom: str) -> list[str]:
    """Extract domain-specific column names from the first markdown table header row.

    Skip Row/STUDYID/DOMAIN/USUBJID/EPOCH/<DOM>SEQ.
    Return up to 3 meaningful column names.
    """
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith('|'):
            continue
        # Skip separator rows
        if re.match(r'^\|[-| :]+\|', stripped):
            continue
        # Parse header cells
        cells = [c.strip() for c in stripped.split('|') if c.strip()]
        result: list[str] = []
        for col in cells:
            col_upper = col.upper()
            if col_upper in _SKIP_COLS:
                continue
            if _SEQ_RE.match(col_upper):
                continue
            result.append(col)
            if len(result) >= 3:
                break
        if result:
            return result
    return []


def _extract_first_row_values(text: str) -> list[str]:
    """Extract up to 2 non-empty, non-identifier cell values from the first data row."""
    _COMMON_IDS = {"ROW", "STUDYID", "DOMAIN", "USUBJID", "EPOCH"}
    # We need to identify which columns to skip: collect headers first
    header_cols: list[str] = []
    separator_seen = False
    results: list[str] = []

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith('|'):
            if header_cols:
                break  # left the table
            continue
        cells = [c.strip() for c in stripped.split('|') if c.strip()]
        if not header_cols:
            # First pipe row = header
            header_cols = [c.upper() for c in cells]
            continue
        if not separator_seen and re.match(r'^\|[-| :]+\|', stripped):
            separator_seen = True
            continue
        if separator_seen:
            # First data row
            for i, cell in enumerate(cells):
                if i >= len(header_cols):
                    break
                col = header_cols[i]
                if col in _COMMON_IDS:
                    continue
                if _SEQ_RE.match(col):
                    continue
                val = cell.strip()
                if not val or val == '|':
                    continue
                # Trim to 40 chars
                if len(val) > 40:
                    val = val[:37] + '...'
                results.append(val)
                if len(results) >= 2:
                    break
            break
    return results


def _count_data_rows(text: str) -> int:
    """Approximate row count from xpt table: count pipe-separated data rows (skip header/separator)."""
    rows = 0
    in_table = False
    header_seen = False
    sep_seen = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('|'):
            in_table = True
            if not header_seen:
                header_seen = True
            elif not sep_seen and re.match(r'^\|[-| :]+\|', stripped):
                sep_seen = True
            elif sep_seen:
                rows += 1
        else:
            if in_table:
                # table ended
                header_seen = False
                sep_seen = False
                in_table = False
    return rows


def _summarize_example(example_text: str, dom: str) -> tuple[str, int]:
    """Produce a <=60 char summary for one Example block.

    Returns (summary, tier) where tier is:
      1 = prose keywords
      2 = table column headers
      3 = first data row values
      4 = domain registry

    Fallback chain (stops at first non-empty result):
    1. prose scenario tags + variable patterns
    2. table column headers (domain-specific, skip identifiers)
    3. first data row values (first 2 non-empty non-identifier cells)
    4. domain registry one-liner
    """
    # Collect context: prose only (exclude table lines)
    prose_lines = []
    for line in example_text.splitlines():
        stripped = line.strip()
        if stripped.startswith('|') or (stripped.startswith('**') and '.xpt' in stripped):
            continue
        if stripped.startswith('**') and stripped.endswith('**'):
            # Row descriptions: strip but include content
            prose_lines.append(stripped.strip('*'))
        else:
            prose_lines.append(stripped)
    prose = ' '.join(prose_lines)

    # Count rows across all xpt tables in this example
    total_rows = _count_data_rows(example_text)
    row_suffix = f" ({total_rows} rows)" if total_rows > 0 else ""

    def _trim(s: str) -> str:
        return s[:57] + '...' if len(s) > 60 else s

    # --- Tier 1: prose keywords ---
    vars_found = _extract_variables(prose)
    vars_part = '+'.join(vars_found[:3]) if vars_found else ''
    tags = _extract_scenario_tags(prose)
    scenario_part = '/'.join(tags[:2]) if tags else ''

    parts = []
    if scenario_part:
        parts.append(scenario_part)
    if vars_part:
        parts.append(vars_part)

    if parts:
        return _trim(', '.join(parts) + row_suffix), 1

    # --- Tier 2: table column headers (markdown table or prose note) ---
    headers = _extract_table_headers(example_text, dom)
    if not headers:
        # Handle prose column-list notes: *(cp.xpt table contains N rows with columns including A, B, C.)*
        col_note_m = re.search(
            r'\*\(.*?columns[^:]*:?\s+([A-Z][A-Z0-9,\s]+)\.\)\*',
            example_text, re.IGNORECASE
        )
        if col_note_m:
            raw_cols = [c.strip() for c in col_note_m.group(1).split(',') if c.strip()]
            headers = [c for c in raw_cols
                       if c.upper() not in _SKIP_COLS and not _SEQ_RE.match(c.upper())][:3]
    if headers:
        return _trim('+'.join(headers) + row_suffix), 2

    # --- Tier 3: first data row values ---
    row_vals = _extract_first_row_values(example_text)
    if row_vals:
        vals_str = ', '.join(f'"{v}"' for v in row_vals)
        return _trim(vals_str + row_suffix), 3

    # --- Tier 4: domain registry ---
    desc = _DOMAIN_REGISTRY.get(dom, f"{dom} domain example")
    return _trim(desc + row_suffix), 4


def _parse_examples(content: str, dom: str) -> list[tuple[int, str, int]]:
    """Parse examples.md content, return list of (example_num, summary, tier)."""
    # Split on ## Example N headings
    pattern = re.compile(r'^## Example\s+(\d+)', re.MULTILINE)
    splits = list(pattern.finditer(content))
    if not splits:
        return []

    results = []
    for i, m in enumerate(splits):
        num = int(m.group(1))
        start = m.end()
        end = splits[i + 1].start() if i + 1 < len(splits) else len(content)
        example_body = content[start:end]
        summary, tier = _summarize_example(example_body, dom)
        results.append((num, summary, tier))
    return results


def _get_source_mtime(path: Path) -> float:
    try:
        return path.stat().st_mtime
    except OSError:
        return 0.0


def _format_mtime(mtime: float) -> str:
    return _dt.datetime.fromtimestamp(mtime, tz=_dt.timezone.utc).strftime('%Y-%m-%d')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    # Collect all source files and max mtime
    source_files = []
    max_mtime = 0.0
    missing = []
    for dom in DOMAINS:
        src = DOMAINS_DIR / dom / "examples.md"
        if src.exists():
            source_files.append((dom, src))
            mt = _get_source_mtime(src)
            if mt > max_mtime:
                max_mtime = mt
        else:
            missing.append(dom)

    if missing:
        print(f"WARNING: missing examples.md for: {', '.join(missing)}", file=sys.stderr)

    mtime_str = _format_mtime(max_mtime) if max_mtime else "unknown"

    lines: list[str] = []

    # Header
    lines.append(f"<!-- generated by scripts/catalog_examples.py (source mtime: {mtime_str}) -->")
    lines.append(f"<!-- {len(DOMAINS)} domains × examples.md 降级为目录。详细数据见 knowledge_base/domains/<DOM>/examples.md -->")
    lines.append("")
    lines.append("# SDTM Examples Catalog")
    lines.append("")
    lines.append("## 说明")
    lines.append("")
    lines.append("本文件为 63 域 examples 目录，每 Example 一句话概括场景；**原始数据表在源文件中**。查具体数据用 source 路径。")
    lines.append("")

    total_examples = 0
    tier_counts: dict[int, int] = {1: 0, 2: 0, 3: 0, 4: 0}

    for dom, src in source_files:
        content = src.read_text(encoding="utf-8", errors="strict")
        examples = _parse_examples(content, dom)

        # Relative source path from repo root
        rel_src = src.relative_to(ROOT)

        lines.append(f"<!-- source: {rel_src.as_posix()} -->")
        lines.append(f"### {dom}")

        # Shared-example annotation
        if dom in _SHARING_NOTE:
            lines.append(f"> {_SHARING_NOTE[dom]}")

        if examples:
            for num, summary, tier in examples:
                lines.append(f"- Example {num}: {summary}")
                tier_counts[tier] = tier_counts.get(tier, 0) + 1
            total_examples += len(examples)
        else:
            lines.append("- (no ## Example headings found)")

        lines.append("")

    # Write output
    OUT.parent.mkdir(parents=True, exist_ok=True)
    output = '\n'.join(lines)
    OUT.write_text(output, encoding="utf-8")

    print(f"Written: {OUT}")
    print(f"Domains: {len(source_files)}/{len(DOMAINS)}")
    print(f"Total examples: {total_examples}")
    print(f"Fallback tiers: prose={tier_counts[1]}, table-headers={tier_counts[2]}, "
          f"row-values={tier_counts[3]}, domain-registry={tier_counts[4]}")
    if missing:
        print(f"Missing: {', '.join(missing)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
