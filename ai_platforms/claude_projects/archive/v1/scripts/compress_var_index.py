#!/usr/bin/env python3
"""Compress knowledge_base/VARIABLE_INDEX.md for Claude Projects (Phase 6.5 Step 5).

Reads the 38k-token VARIABLE_INDEX.md and emits a compact routing-oriented
variable index (~15k tokens target) at
ai_platforms/claude_projects/output/04_variable_index.md.

Compression strategy (per PLAN §3.2 D7 + §4.3 + §7.4 Step 5):
- Section 1 (Common variables, 2+ domains): keep as a table but compact header
  and collapse 'all 63 domains' description.
- Section 2 (Domain-specific variables): CORE COMPRESSION POINT. Replace each
  per-domain table with a single inline line of VAR(Role/Core) triples, where
  Role/Core are short codes. The '*' suffix for cross-domain inconsistency is
  preserved.
- Section 3 (CT cross-reference): one line per CT code listing referring
  variables (space-separated, prefix + count).

Source is read-only (P5). Output is deterministic / idempotent (P7) - the
header timestamp is derived from the source mtime, not from datetime.now().
"""
from __future__ import annotations

import datetime as _dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "knowledge_base" / "VARIABLE_INDEX.md"
OUT = ROOT / "ai_platforms" / "claude_projects" / "output" / "04_variable_index.md"
SRC_REL = "knowledge_base/VARIABLE_INDEX.md"

# Role short codes (matches PLAN §3.2 D7 mapping).
ROLE_SHORT = {
    "Identifier": "Id",
    "Topic": "Tp",
    "Synonym Qualifier": "Sy",
    "Grouping Qualifier": "Gq",
    "Record Qualifier": "Rq",
    "Variable Qualifier": "Vq",
    "Result Qualifier": "Rs",
    "Timing": "Ti",
    "Timing Reference": "Tmr",
    "Rule": "Ru",
}

# Core short codes.
CORE_SHORT = {
    "Req": "R",
    "Exp": "E",
    "Perm": "P",
}

_STAR_RE = re.compile(r"\*$")


def _shorten_role(role: str) -> str:
    """Map a Role string (possibly with '*' suffix) to its short code."""
    star = "*" if _STAR_RE.search(role) else ""
    base = role.rstrip("*").strip()
    return ROLE_SHORT.get(base, base) + star


def _shorten_core(core: str) -> str:
    """Map a Core string (possibly with '*' suffix) to its short code."""
    star = "*" if _STAR_RE.search(core) else ""
    base = core.rstrip("*").strip()
    return CORE_SHORT.get(base, base) + star


def _parse_table_rows(lines: list[str]) -> list[list[str]]:
    """Parse a block of markdown table lines into data cell lists.

    Skips header row (the first pipe row before the separator) and the
    separator row. Each returned list has the row's cells stripped of
    outer pipes and whitespace.
    """
    rows: list[list[str]] = []
    seen_separator = False
    for ln in lines:
        if not ln.startswith("|"):
            continue
        # Separator row: | --- | --- | ...
        if re.match(r"^\|\s*[:\-]+\s*(\|\s*[:\-]+\s*)+\|?\s*$", ln):
            seen_separator = True
            # Reset rows - everything before the separator is header.
            rows = []
            continue
        if not seen_separator:
            # Header row; skip until we see the separator.
            continue
        # Strip outer pipes, then split.
        inner = ln.strip()
        if inner.startswith("|"):
            inner = inner[1:]
        if inner.endswith("|"):
            inner = inner[:-1]
        cells = [c.strip() for c in inner.split("|")]
        rows.append(cells)
    return rows


def _split_sections(text: str) -> tuple[list[str], dict[str, list[str]], list[str]]:
    """Split source into (common_table_rows, domain_blocks, ct_rows).

    - common_table_rows: raw table lines for section 1 (kept as-is, for
      minor reformat in build_output).
    - domain_blocks: {domain_code: list_of_raw_table_lines} for section 2.
    - ct_rows: raw table lines for section 3.
    """
    common_block: list[str] = []
    domain_blocks: dict[str, list[str]] = {}
    ct_block: list[str] = []

    section: str | None = None
    current_dom: str | None = None

    for line in text.splitlines():
        stripped = line.strip()
        # Top-level section switch.
        if stripped.startswith("## 一、"):
            section = "common"
            continue
        if stripped.startswith("## 二、"):
            section = "domain"
            continue
        if stripped.startswith("## 三、"):
            section = "ct"
            current_dom = None
            continue
        if stripped.startswith("## "):
            # other top-level section (使用说明 etc.)
            section = None
            continue

        if section == "common":
            common_block.append(line)
        elif section == "domain":
            m = re.match(r"^###\s+([A-Z]+)\b", stripped)
            if m:
                current_dom = m.group(1)
                domain_blocks.setdefault(current_dom, [])
                continue
            if current_dom is not None:
                domain_blocks[current_dom].append(line)
        elif section == "ct":
            ct_block.append(line)

    return common_block, domain_blocks, ct_block


def _build_common_section(block_lines: list[str]) -> list[str]:
    """Rebuild section 1 as a compact table.

    Source row: | VAR | count | domain-list | Label | Type | Role | Core |
    Output:     | VAR | N | domains | Label | T | Role | Core |
      - Role/Core shortened, '*' preserved.
      - Type compressed to single char (C/N).
      - 'all 63 domains' note collapsed.
    """
    rows = _parse_table_rows(block_lines)
    out: list[str] = []
    out.append("## 1. Common variables (2+ domains, 24)")
    out.append("")
    out.append("| Var | N | Domains | Label | T | Role | Core |")
    out.append("|---|---|---|---|---|---|---|")
    for r in rows:
        if len(r) < 7:
            continue
        var, count, doms, label, typ, role, core = r[:7]
        # Collapse the 'all 63 domains' wording to save tokens.
        if doms.startswith("所有域") or doms == "所有域":
            doms = "ALL 63"
        # Compress 'Char'/'Num' to C/N.
        t = "C" if typ.strip() == "Char" else ("N" if typ.strip() == "Num" else typ.strip())
        out.append(
            f"| {var} | {count} | {doms} | {label} | {t} | {_shorten_role(role)} | {_shorten_core(core)} |"
        )
    out.append("")
    return out


def _build_domain_section(domain_blocks: dict[str, list[str]]) -> tuple[list[str], int]:
    """Rebuild section 2 as one compact line per domain."""
    out: list[str] = []
    out.append("## 2. Domain-specific variables (1499 vars across domains)")
    out.append("")
    out.append(
        "Format: `DOM: VAR(Role/Core), ...`  Role/Core codes at end of file."
    )
    out.append("")

    domains_covered = 0
    for dom in sorted(domain_blocks.keys()):
        rows = _parse_table_rows(domain_blocks[dom])
        if not rows:
            continue
        domains_covered += 1
        triples: list[str] = []
        for r in rows:
            if len(r) < 4:
                continue
            # Columns: VAR | Label | Type | Role | Core | CT
            var = r[0]
            role = r[3] if len(r) > 3 else ""
            core = r[4] if len(r) > 4 else ""
            triples.append(f"{var}({_shorten_role(role)}/{_shorten_core(core)})")
        if not triples:
            continue
        out.append(f"### {dom}")
        out.append(", ".join(triples))
        out.append("")
    return out, domains_covered


def _build_ct_section(block_lines: list[str]) -> list[str]:
    """Rebuild section 3 as compact one-line-per-CT entries.

    Source row: | CT Code | count | var-list (possibly truncated) |
    Output:     `- CT_CODE (N): VAR1, VAR2, ...`
    """
    rows = _parse_table_rows(block_lines)
    out: list[str] = []
    out.append("## 3. CT cross-reference (135 CT codes)")
    out.append("")
    for r in rows:
        if len(r) < 3:
            continue
        code, count, var_list = r[:3]
        out.append(f"- {code} ({count}): {var_list}")
    out.append("")
    return out


def _build_footer() -> list[str]:
    """Role/Core mapping legend - must appear once at end (not per line)."""
    return [
        "## Legend",
        "",
        "**Role**: Id=Identifier, Tp=Topic, Sy=Synonym Qualifier, "
        "Gq=Grouping Qualifier, Rq=Record Qualifier, Vq=Variable Qualifier, "
        "Rs=Result Qualifier, Ti=Timing, Tmr=Timing Reference, Ru=Rule",
        "",
        "**Core**: R=Req, E=Exp, P=Perm",
        "",
        "**Type** (section 1 only): C=Char, N=Num",
        "",
        "**Asterisk (`*`)**: value differs across domains; shown value is the "
        "most common one.",
        "",
    ]


def build_output(src_text: str, src_mtime: float) -> str:
    common_block, domain_blocks, ct_block = _split_sections(src_text)

    ts = _dt.datetime.utcfromtimestamp(src_mtime).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = []
    lines.append(f"<!-- generated by scripts/compress_var_index.py (source mtime: {ts}) -->")
    lines.append(f"<!-- source: {SRC_REL} -->")
    lines.append("")
    lines.append("# SDTM Variable Index (Compressed)")
    lines.append("")
    lines.append(
        "Reverse index of 1,523 variables across 63 domains. Use to locate "
        "`variable -> domain`, or `CT code -> variables`. See Legend at end."
    )
    lines.append("")

    lines.extend(_build_common_section(common_block))
    dom_lines, domains_covered = _build_domain_section(domain_blocks)
    lines.extend(dom_lines)
    lines.extend(_build_ct_section(ct_block))
    lines.extend(_build_footer())

    # Sanity trailer (informational, deterministic).
    lines.append(f"<!-- domains covered: {domains_covered} -->")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    if not SRC.is_file():
        print(f"error: source not found: {SRC}", file=sys.stderr)
        return 2
    src_text = SRC.read_text(encoding="utf-8")
    src_mtime = SRC.stat().st_mtime
    output = build_output(src_text, src_mtime)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(output, encoding="utf-8")
    print(f"wrote {OUT} ({len(output)} chars, {len(output.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
