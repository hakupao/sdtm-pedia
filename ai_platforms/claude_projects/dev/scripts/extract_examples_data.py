#!/usr/bin/env python3
"""Extract data-table-first examples for high-frequency SDTM domains (Phase 6.5 v2 Task D2).

For each domain in the batch-2 clean list (typically 28 domains), read
``knowledge_base/domains/<X>/examples.md`` and emit a compact "data-first"
variant that keeps:

- Domain-level title (renormalized to level-3: ``### <X> — Examples``)
- Each Example heading (``## Example N`` -> ``#### Example N``)
- The **first** description paragraph for each Example, capped at 2 lines
- Bold XPT/dataset filename markers (``**ae.xpt**``, ``**suppae.xpt**`` ...)
- Every markdown data table (pipe-tables with ``|---|`` separator rows)
- "shared with" / "see also" cross-reference notes at the top of the file
- ``### <sub-heading>`` subsections that sit immediately above a data table
  (e.g. "### PC-PP Relating Datasets", "### Example 1 (All PC records used)")

Drops:

- All other description paragraphs (beyond the 2-line first-description cap)
- ``**Row N:**`` / ``**Rows N-M:**`` row explanations (redundant with the table)
- Mermaid / non-table fenced code blocks, CRF narrative, ANNOTATION text
- Business-context prose in general

CLI
---

``--tier high --domain-list <path>``
    Parse ``<path>`` either as one-domain-per-line plain text, or as the D1
    ``## 最终清单`` markdown file; run the extractor over exactly those
    domains (deterministic sort).

``--tier others --exclude-list <path>``
    Same as above but run against every other SDTM domain not in the
    exclude list. D2 scope does not invoke this path; the flag exists so
    E1 can reuse this same script. (Implemented for completeness.)

Output
------

``ai_platforms/claude_projects/output_v2/09_examples_data_high.md``
(or ``10_examples_data_others.md`` for --tier others per PLAN_V2 §2.2).

Token guard rails (cl100k_base):

- Soft target: <= 30,000 tokens (warn to stdout only)
- Warning band: 30,000-50,000 tokens (warn to stderr, continue)
- Hard cap: > 50,000 tokens -> ``sys.exit(1)`` with EXCEED_HARD_CAP on stderr

Idempotent: the generated header timestamp is derived from the max mtime
of the source ``examples.md`` files (not wall-clock), so two runs against
unchanged sources produce byte-identical output.

Read-only for ``knowledge_base/``; writes only into ``output_v2/``.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

import tiktoken

# --- Paths ------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[3]
KB_DOMAINS = REPO_ROOT / "knowledge_base" / "domains"
OUTPUT_DIR = REPO_ROOT / "ai_platforms" / "claude_projects" / "output_v2"

ENCODING_NAME = "cl100k_base"

SOFT_TARGET = 30_000
HARD_CAP = 50_000

# Full SDTM domain list (mirrors scripts_v2/score_domains.py).
ALL_DOMAINS: list[str] = [
    "AE", "AG", "BE", "BS", "CE", "CM", "CO", "CP", "CV", "DA",
    "DD", "DM", "DS", "DV", "EC", "EG", "EX", "FA", "FT", "GF",
    "HO", "IE", "IS", "LB", "MB", "MH", "MI", "MK", "ML", "MS",
    "NV", "OE", "OI", "PC", "PE", "PP", "PR", "QS", "RE", "RELREC",
    "RELSPEC", "RELSUB", "RP", "RS", "SC", "SE", "SM", "SR", "SS", "SU",
    "SUPPQUAL", "SV", "TA", "TD", "TE", "TI", "TM", "TR", "TS", "TU",
    "TV", "UR", "VS",
]

# Regex: pipe-table separator row, e.g. ``|-----|---------|--------|``.
TABLE_SEP_RE = re.compile(r"^\s*\|[\s\-:|]+\|\s*$")
# Regex: line that *might* be a pipe-table body/header row.
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
# Regex: bold filename token such as ``**ae.xpt**`` or ``**suppae.xpt**``.
FILENAME_BOLD_RE = re.compile(r"^\*\*[a-z][a-z0-9_]*\.(xpt|csv|sas7bdat)\*\*\s*$")
# Regex: row-explanation lines like ``**Row 1:**`` or ``**Rows 3-5:**``.
ROW_EXPLAIN_RE = re.compile(r"^\*\*Rows?\s+[\d,\- ]+:\*\*")
# Regex: the ``## Example N`` heading.
EXAMPLE_HDR_RE = re.compile(r"^##\s+Example\b")
# Regex: any H3 subheading (``### ...``).
SUB_HDR_RE = re.compile(r"^###\s+")
# Regex: italic note line ``*...shared with...*`` or ``*...see also...*``.
CROSSREF_NOTE_RE = re.compile(
    r"^\*[^*].*(shared with|see also|combined examples)[^*]*\*\s*$",
    flags=re.IGNORECASE,
)
# Regex: code fence (``` or ```mermaid etc.); drop these entire blocks.
CODE_FENCE_RE = re.compile(r"^\s*```")


# --- Domain list parsing ----------------------------------------------------


def _parse_domain_list_file(path: Path) -> list[str]:
    """Parse ``path`` as either plain text (one domain per line) or the D1 md.

    Markdown rules: look for the first fenced ``` code block that appears after
    a heading matching ``## 最终清单`` (or any heading if none found). Inside
    that block, split on commas/whitespace and keep token-like uppercase ids.
    Plain-text rules: strip ``#`` comments; keep non-empty, uppercase tokens.
    """
    text = path.read_text(encoding="utf-8", errors="strict")

    # Try markdown code-block mode first.
    if "```" in text:
        # Prefer the code block directly under "## 最终清单" (Chinese) or
        # "## Final Clean List" (fallback); otherwise first fenced block.
        lines = text.splitlines()
        anchor_idx = -1
        for i, ln in enumerate(lines):
            if re.match(r"^##\s+(最终清单|Final\b.*[Ll]ist)", ln):
                anchor_idx = i
                break
        # Find the first ``` after the anchor; if no anchor, first ``` overall.
        start_search = anchor_idx if anchor_idx >= 0 else 0
        block: list[str] = []
        in_block = False
        for ln in lines[start_search:]:
            if CODE_FENCE_RE.match(ln):
                if in_block:
                    break
                in_block = True
                continue
            if in_block:
                block.append(ln)
        if block:
            raw = " ".join(block)
            tokens = re.split(r"[\s,]+", raw)
            parsed = [t.strip() for t in tokens if t.strip()]
            uppercase_tokens = [t for t in parsed if re.fullmatch(r"[A-Z][A-Z0-9]*", t)]
            if uppercase_tokens:
                return uppercase_tokens

    # Plain-text fallback: one domain per line, ignore blank + # comments.
    out: list[str] = []
    for ln in text.splitlines():
        ln = ln.split("#", 1)[0].strip()
        if not ln:
            continue
        # Allow comma-separated too.
        for tok in re.split(r"[\s,]+", ln):
            tok = tok.strip()
            if tok and re.fullmatch(r"[A-Z][A-Z0-9]*", tok):
                out.append(tok)
    return out


# --- Extraction -------------------------------------------------------------


def _strip_trailing_blank(buf: list[str]) -> list[str]:
    while buf and buf[-1].strip() == "":
        buf.pop()
    return buf


def _collect_table_block(lines: list[str], start: int) -> tuple[list[str], int]:
    """If ``lines[start]`` opens a pipe-table block, return (rows, next_idx).

    A pipe-table is a run of consecutive ``TABLE_ROW_RE`` lines that contains
    at least one ``TABLE_SEP_RE`` separator row. If the run does NOT contain
    a separator we treat it as regular prose (no extraction), and return
    ``([], start)`` so the caller keeps scanning.
    """
    j = start
    run: list[str] = []
    while j < len(lines) and TABLE_ROW_RE.match(lines[j]):
        run.append(lines[j])
        j += 1
    if any(TABLE_SEP_RE.match(r) for r in run) and len(run) >= 2:
        return run, j
    return [], start


def _first_description(lines: list[str], start: int) -> tuple[list[str], int]:
    """Return up to 2 lines of first-paragraph description starting at ``start``.

    Scans forward skipping blank lines, then collects until the next blank,
    but truncates the result to 2 lines. Returns (desc_lines, cursor_after).
    A "description" must be plain prose — skip lines that look like row
    explanations, bold filenames, headings, tables or code fences; in those
    cases return ``([], start)`` (no description available at this point).
    """
    j = start
    # Skip leading blanks to find paragraph start.
    while j < len(lines) and lines[j].strip() == "":
        j += 1
    if j >= len(lines):
        return [], j
    first = lines[j]
    # Must look like prose — not a row-explain, filename, heading, table, or code.
    if (
        ROW_EXPLAIN_RE.match(first)
        or FILENAME_BOLD_RE.match(first)
        or first.startswith("#")
        or TABLE_ROW_RE.match(first)
        or CODE_FENCE_RE.match(first)
    ):
        return [], start
    # Collect up to 2 lines of the paragraph.
    para: list[str] = []
    while j < len(lines) and lines[j].strip() != "" and len(para) < 2:
        if (
            ROW_EXPLAIN_RE.match(lines[j])
            or FILENAME_BOLD_RE.match(lines[j])
            or lines[j].startswith("#")
            or TABLE_ROW_RE.match(lines[j])
            or CODE_FENCE_RE.match(lines[j])
        ):
            break
        para.append(lines[j])
        j += 1
    # Advance past the rest of the paragraph so the outer loop skips it.
    while j < len(lines) and lines[j].strip() != "":
        j += 1
    return para, j


def extract_domain(domain: str, text: str) -> str:
    """Compress one domain's ``examples.md`` into the data-first variant.

    Structure of output (all relative to a ``### <DOMAIN> — Examples`` header
    emitted by the caller):

    - optional cross-ref note lines near the top of the source
    - for each Example block (``## Example N``):
        - ``#### Example N``
        - first-description (<=2 lines) if one is present
        - any bold filename markers + their following data tables
        - ``### sub-heading`` subsections that directly precede a data table
    """
    lines = text.splitlines()
    n = len(lines)

    # --- Pass 1: locate cross-ref notes before the first "## Example" --------
    i = 0
    # Skip the domain-level "# X — Examples" line if present (we emit our own).
    if i < n and lines[i].startswith("# "):
        i += 1
    preamble_notes: list[str] = []
    while i < n and not EXAMPLE_HDR_RE.match(lines[i]):
        ln = lines[i]
        if CROSSREF_NOTE_RE.match(ln.strip()):
            preamble_notes.append(ln.strip())
        i += 1

    # --- Pass 2: walk Example blocks -----------------------------------------
    out: list[str] = []
    in_code_fence = False
    # `pending_sub_header` holds a "### ..." line that we have not decided to
    # keep yet; we emit it only when an immediately-following data table or
    # filename marker justifies its presence.
    pending_sub_header: str | None = None

    # Current example heading emission state: we emit the "#### Example N" lazy,
    # only after we've successfully pulled at least one kept element (desc,
    # table, filename). This avoids empty headers in degenerate cases.
    current_example_header: str | None = None
    example_header_emitted = False
    first_desc_consumed_for_current_example = False

    def _emit_example_header_if_needed() -> None:
        nonlocal example_header_emitted
        if current_example_header is not None and not example_header_emitted:
            if out and out[-1].strip() != "":
                out.append("")
            out.append(current_example_header)
            out.append("")
            example_header_emitted = True

    while i < n:
        ln = lines[i]

        # Track (and drop) any fenced code block entirely.
        if CODE_FENCE_RE.match(ln):
            in_code_fence = not in_code_fence
            i += 1
            continue
        if in_code_fence:
            i += 1
            continue

        # Example header: flush state, start a new example scope.
        if EXAMPLE_HDR_RE.match(ln):
            # Strip trailing blanks in current output before starting next block.
            _strip_trailing_blank(out)
            out.append("")
            # Remap "## Example N ..." -> "#### Example N ..."
            current_example_header = "#### " + ln[len("## "):].strip()
            example_header_emitted = False
            first_desc_consumed_for_current_example = False
            pending_sub_header = None
            i += 1
            # Try to consume the first description for this example.
            desc, new_i = _first_description(lines, i)
            if desc:
                _emit_example_header_if_needed()
                for d in desc:
                    out.append(d)
                out.append("")
                first_desc_consumed_for_current_example = True
                i = new_i
            continue

        # Sub-heading (### ...): buffer; emit only if a table/filename follows.
        if SUB_HDR_RE.match(ln):
            pending_sub_header = ln.rstrip()
            i += 1
            continue

        # Bold filename marker: keep, and emit any pending sub-header.
        if FILENAME_BOLD_RE.match(ln):
            _emit_example_header_if_needed()
            if pending_sub_header is not None:
                if out and out[-1].strip() != "":
                    out.append("")
                out.append(pending_sub_header)
                out.append("")
                pending_sub_header = None
            if out and out[-1].strip() != "":
                out.append("")
            out.append(ln.rstrip())
            out.append("")
            i += 1
            continue

        # Pipe table block: keep verbatim (preserving column alignment).
        table, new_i = _collect_table_block(lines, i)
        if table:
            _emit_example_header_if_needed()
            if pending_sub_header is not None:
                if out and out[-1].strip() != "":
                    out.append("")
                out.append(pending_sub_header)
                out.append("")
                pending_sub_header = None
            if out and out[-1].strip() != "":
                out.append("")
            for row in table:
                out.append(row.rstrip())
            out.append("")
            i = new_i
            continue

        # Row-explanation line: drop.
        if ROW_EXPLAIN_RE.match(ln):
            i += 1
            continue

        # Cross-ref note that occurs mid-file: keep.
        if CROSSREF_NOTE_RE.match(ln.strip()):
            _emit_example_header_if_needed()
            out.append(ln.rstrip())
            i += 1
            continue

        # Anything else (narrative, list bullets, etc.): drop.
        # A pending sub-header that never found a table gets discarded.
        if pending_sub_header is not None and ln.strip() == "":
            # still waiting — blank line can occur between ### and a table
            i += 1
            continue
        # Drop the pending sub-header: it didn't precede a data table.
        pending_sub_header = None
        i += 1

    # Drop trailing blanks.
    _strip_trailing_blank(out)

    # If no content was produced (edge case: some examples.md files are
    # narrative-only with no tables), degrade to a single placeholder line.
    if not out and not preamble_notes:
        return "(no data tables in source)\n"

    parts: list[str] = []
    if preamble_notes:
        parts.extend(preamble_notes)
        parts.append("")
    parts.extend(out)
    return "\n".join(p for p in parts).rstrip() + "\n"


# --- Document assembly ------------------------------------------------------


def _iso_from_mtimes(paths: list[Path]) -> str:
    """Build an ISO-8601 UTC string from max mtime of the given paths.

    Falls back to a fixed sentinel if no paths exist, so the header stays
    deterministic even when all source files are missing (pathological).
    """
    mtimes = [p.stat().st_mtime for p in paths if p.is_file()]
    if not mtimes:
        return "1970-01-01T00:00:00Z"
    latest = max(mtimes)
    return _dt.datetime.fromtimestamp(latest, tz=_dt.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def build_document(tier: str, domains: list[str]) -> tuple[str, list[str]]:
    """Return (full_text, missing_domains).

    ``full_text`` is the complete examples-data payload for the given tier
    (``09_examples_data_high.md`` or ``10_examples_data_others.md``).
    ``missing_domains`` lists domains whose ``examples.md`` did not exist.
    """
    domains = sorted(set(domains))
    src_paths = [KB_DOMAINS / d / "examples.md" for d in domains]
    ts = _iso_from_mtimes(src_paths)

    if tier == "high":
        file_num, tier_label, stage_tag = "09", "High-Frequency Domains", "Stage v2.2"
    else:
        file_num, tier_label, stage_tag = "10", "Others-Tier Domains", "Stage v2.3"
    out: list[str] = []
    out.append(
        f"<!-- generated by scripts_v2/extract_examples_data.py --tier {tier} at {ts} -->"
    )
    out.append("")
    out.append(f"# {file_num} Examples Data — {tier_label} ({stage_tag})")
    out.append("")
    out.append(
        "Data-table-first extraction of `knowledge_base/domains/<X>/examples.md`. "
        "Each Example keeps its first-description (<=2 lines) and every data table "
        "verbatim; row-by-row prose and narrative business context are removed."
    )
    out.append("")

    missing: list[str] = []
    first = True
    for d in domains:
        src = KB_DOMAINS / d / "examples.md"
        if not first:
            out.append("---")
            out.append("")
        first = False
        rel_src = f"knowledge_base/domains/{d}/examples.md"
        out.append(f"<!-- source: {rel_src} -->")
        out.append(f"### {d} — Examples")
        out.append("")
        if not src.is_file():
            missing.append(d)
            out.append("(no examples file)")
            out.append("")
            continue
        raw = src.read_text(encoding="utf-8", errors="strict")
        body = extract_domain(d, raw)
        out.append(body.rstrip())
        out.append("")

    # Normalize trailing blanks.
    while out and out[-1].strip() == "":
        out.pop()
    out.append("")
    return "\n".join(out), missing


# --- CLI entry point --------------------------------------------------------


def _resolve_domains(args: argparse.Namespace) -> list[str]:
    if args.tier == "high":
        if not args.domain_list:
            raise SystemExit("--tier high requires --domain-list <path>")
        path = Path(args.domain_list).expanduser().resolve()
        if not path.is_file():
            raise SystemExit(f"--domain-list not found: {path}")
        parsed = _parse_domain_list_file(path)
        if not parsed:
            raise SystemExit(f"no domains parsed from {path}")
        return parsed
    # tier == "others": everything in ALL_DOMAINS minus the exclude list.
    if not args.exclude_list:
        raise SystemExit("--tier others requires --exclude-list <path>")
    path = Path(args.exclude_list).expanduser().resolve()
    if not path.is_file():
        raise SystemExit(f"--exclude-list not found: {path}")
    excluded = set(_parse_domain_list_file(path))
    return [d for d in ALL_DOMAINS if d not in excluded]


def _output_path(tier: str) -> Path:
    if tier == "high":
        return OUTPUT_DIR / "09_examples_data_high.md"
    return OUTPUT_DIR / "10_examples_data_others.md"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, add_help=True)
    parser.add_argument("--tier", choices=("high", "others"), required=True)
    parser.add_argument("--domain-list", dest="domain_list")
    parser.add_argument("--exclude-list", dest="exclude_list")
    args = parser.parse_args(argv)

    domains = _resolve_domains(args)
    full_text, missing = build_document(args.tier, domains)

    out_path = _output_path(args.tier)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(full_text, encoding="utf-8")

    encoder = tiktoken.get_encoding(ENCODING_NAME)
    token_count = len(encoder.encode(full_text))

    included = len(sorted(set(domains)))
    tag = f"[Tier {args.tier}]"
    print(
        f"{tag} {out_path.name}: {token_count} tokens "
        f"(target <={SOFT_TARGET // 1000}K, hard <={HARD_CAP // 1000}K)"
    )
    print(f"{tag} domains included: {included}")
    missing_repr = ", ".join(missing) if missing else "none"
    print(f"{tag} domains missing examples.md: {missing_repr}")

    if token_count > HARD_CAP:
        print(
            f"{tag} EXCEED_HARD_CAP: {token_count} > {HARD_CAP}",
            file=sys.stderr,
        )
        return 1
    if token_count > SOFT_TARGET:
        print(
            f"{tag} WARN: {token_count} tokens above soft target {SOFT_TARGET} "
            f"(continuing; hand-off to main controller for review)",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
