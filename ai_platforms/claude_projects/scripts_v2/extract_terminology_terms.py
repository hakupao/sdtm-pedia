#!/usr/bin/env python3
"""Extract high-frequency SDTM controlled terminology codelists (Phase 6.5 v2 Task F2).

For each C-code in the input list, locate the codelist section across all files
under ``knowledge_base/terminology/{core,questionnaires,supplementary}/``, match
by ``## <Name> (<C-code>)`` heading, preserve the 4-column Term table, truncate
each Definition cell to <=200 characters. Derived "Related Domain" is emitted
as a single codelist-level metadata line (not repeated per-row), reducing
redundancy significantly for codelists referenced by many domains.

Output is split into 3 files by source subdirectory:

- ``11a_terminology_high_core.md`` — codelists from ``core/``
- ``11b_terminology_high_questionnaires.md`` — codelists from ``questionnaires/``
- ``11c_terminology_high_supp.md`` — codelists from ``supplementary/``

Within each file, codelists appear in F1 ranking order (input list order),
so higher-ranked codelists always come first regardless of subdir split.

Rules
-----

- Input order is preserved verbatim within each subdir file (stable, diff-friendly).
- If a codelist happens to span multiple files (same heading appears twice),
  aggregate all term rows under the first-found heading and dedupe by each
  term row's leftmost Code cell.
- ``(NCI)`` or other provenance tags count toward the 200-char Definition
  budget. Truncated cells get ``...`` appended.
- Related Domains renders as a comma-separated line after ``Extensible: Yes/No``.
  If none, renders ``Related Domains: —`` (em dash).
- Any C-code that can't be located is reported to stderr (non-fatal) and to
  an evidence failure file; the script still writes the output so the
  downstream reviewer can inspect.

CLI
---

``--tier high --list <path-to-F1_codelist_high.txt>``
    Read the C-code list, produce ``11a/11b/11c_terminology_high_*.md``.
    Definition cells capped at 200 chars; 4-column table with Synonyms.

``--tier mid --list <path-to-G1_codelist_mid.txt>``
    Read the C-code list, produce ``12a/12b/12c_terminology_mid_*.md``.
    Definition cells capped at 100 chars with word-boundary truncation;
    3-column table (Code / Submission Value / Definition). Synonyms and
    NCI Concept Description links are dropped to fit capacity budget.

Token guard rails (cl100k_base via tiktoken), applied per-file:

- Soft target: <= 200,000 tokens (info only)
- Warning band: 200,000-350,000 (stderr warn, continue)
- Hard cap: > 350,000 (stderr exceed, exit 1; files still written)

Idempotent: header timestamp derived from max mtime of sourced terminology +
domain spec files, so repeated runs against unchanged sources produce
byte-identical output.

Read-only on ``knowledge_base/`` (P5). Writes only into ``output_v2/``.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import re
import sys
from pathlib import Path

import tiktoken

# --- Paths ------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[3]
KB_TERM = REPO_ROOT / "knowledge_base" / "terminology"
KB_DOMAINS = REPO_ROOT / "knowledge_base" / "domains"
OUTPUT_DIR = REPO_ROOT / "ai_platforms" / "claude_projects" / "output_v2"
EVIDENCE_DIR = OUTPUT_DIR / "evidence_v2"
FAILURES_DIR = EVIDENCE_DIR / "failures"

TERM_SUBDIRS = ("core", "questionnaires", "supplementary")

# Map (tier, subdir) -> (file_suffix, file_num, title_label)
SUBDIR_META_BY_TIER: dict[str, dict[str, tuple[str, str, str]]] = {
    "high": {
        "core":           ("11a_terminology_high_core.md",
                           "11a",
                           "High-Frequency Codelists \u2014 core subdir (Stage v2.4)"),
        "questionnaires": ("11b_terminology_high_questionnaires.md",
                           "11b",
                           "High-Frequency Codelists \u2014 questionnaires subdir (Stage v2.4)"),
        "supplementary":  ("11c_terminology_high_supp.md",
                           "11c",
                           "High-Frequency Codelists \u2014 supplementary subdir (Stage v2.4)"),
    },
    "mid": {
        "core":           ("12a_terminology_mid_core.md",
                           "12a",
                           "Mid-Frequency Codelists \u2014 core subdir (Stage v2.5)"),
        "questionnaires": ("12b_terminology_mid_questionnaires.md",
                           "12b",
                           "Mid-Frequency Codelists \u2014 questionnaires subdir (Stage v2.5)"),
        "supplementary":  ("12c_terminology_mid_supp.md",
                           "12c",
                           "Mid-Frequency Codelists \u2014 supplementary subdir (Stage v2.5)"),
    },
}

# Backward-compatible alias (high-tier map); preserved for any external readers.
SUBDIR_META: dict[str, tuple[str, str, str]] = SUBDIR_META_BY_TIER["high"]

ENCODING_NAME = "cl100k_base"

# Per-file guard rails (relaxed from first run — user accepted generous budget).
SOFT_TARGET = 200_000
HARD_CAP = 350_000

DEFINITION_CHAR_LIMIT_HIGH = 200
DEFINITION_CHAR_LIMIT_MID = 100
# Back-compat alias; high tier default.
DEFINITION_CHAR_LIMIT = DEFINITION_CHAR_LIMIT_HIGH
TRUNCATE_MARKER = "..."

# Regex: codelist heading ``## <Name> (<C-code>)``.
CODELIST_HDR_RE = re.compile(r"^##\s+(.*?)\s+\((C\d+)\)\s*$")
# Regex: pipe-table separator row.
TABLE_SEP_RE = re.compile(r"^\s*\|[\s\-:|]+\|\s*$")
# Regex: pipe-table row (header or body).
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
# Regex: ``Extensible: Yes/No`` line.
EXTENSIBLE_RE = re.compile(r"^\s*Extensible:\s*(Yes|No)\s*$", flags=re.IGNORECASE)


# --- Terminology source indexing -------------------------------------------


def _iter_terminology_files() -> list[Path]:
    """Return all ``*.md`` files under ``knowledge_base/terminology/{sub}/``.

    Stable-sorted by (subdir, filename) so scan order is reproducible.
    """
    found: list[Path] = []
    for sub in TERM_SUBDIRS:
        d = KB_TERM / sub
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            found.append(p)
    return found


def _split_cell(row: str) -> list[str]:
    """Split a pipe-table row into trimmed cells.

    ``| a | b | c |`` -> ``["a", "b", "c"]``. Handles leading/trailing pipes
    and arbitrary interior whitespace.
    """
    s = row.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def _extract_codelist_section(
    lines: list[str], start: int
) -> tuple[str, list[list[str]], int]:
    """Pull ``(extensible_line, term_rows, next_idx)`` from a codelist section.

    ``start`` points at the codelist ``## ...`` heading. Scans until the next
    ``## `` heading or EOF. Inside, keeps:

    - the first ``Extensible: Yes|No`` line
    - the first pipe-table block (header + separator + body rows)

    ``term_rows`` is the list of BODY rows only (no header, no separator),
    each as ``[code, sub_value, synonyms, definition]``.
    """
    n = len(lines)
    i = start + 1
    extensible = ""
    table_rows_raw: list[str] = []
    in_table = False
    saw_separator = False

    while i < n:
        ln = lines[i]
        # Stop at next codelist heading.
        if ln.startswith("## "):
            break
        if not extensible:
            m = EXTENSIBLE_RE.match(ln)
            if m:
                value = m.group(1)
                extensible = f"Extensible: {value[0].upper() + value[1:].lower()}"
        if TABLE_ROW_RE.match(ln):
            if not in_table:
                in_table = True
                table_rows_raw = [ln]
            else:
                table_rows_raw.append(ln)
            if TABLE_SEP_RE.match(ln):
                saw_separator = True
        elif in_table:
            # Blank/non-pipe line after the table ends the block.
            if saw_separator:
                break
            # If we never saw a separator, this wasn't a real table; reset.
            in_table = False
            saw_separator = False
            table_rows_raw = []
        i += 1

    body: list[list[str]] = []
    if saw_separator and len(table_rows_raw) >= 2:
        sep_idx = next(
            (k for k, r in enumerate(table_rows_raw) if TABLE_SEP_RE.match(r)),
            -1,
        )
        if sep_idx >= 0:
            for raw in table_rows_raw[sep_idx + 1:]:
                cells = _split_cell(raw)
                # Pad / trim to 4 columns defensively.
                while len(cells) < 4:
                    cells.append("")
                body.append(cells[:4])

    return extensible, body, i


def build_codelist_index() -> dict[str, list[tuple[Path, int]]]:
    """Return ``{C-code: [(file_path, heading_line_index), ...]}`` index.

    Multiple entries per C-code are kept in the order first encountered, so the
    aggregation path is deterministic.
    """
    index: dict[str, list[tuple[Path, int]]] = {}
    for fp in _iter_terminology_files():
        try:
            text = fp.read_text(encoding="utf-8", errors="strict")
        except OSError:
            continue
        for i, ln in enumerate(text.splitlines()):
            m = CODELIST_HDR_RE.match(ln)
            if m:
                ccode = m.group(2)
                index.setdefault(ccode, []).append((fp, i))
    return index


# --- Domain index (for derived Related Domain metadata line) ---------------


def build_domain_index() -> dict[str, list[str]]:
    """Scan ``knowledge_base/domains/*/spec.md`` once; return ``{C-code: [dom]}``.

    Each spec.md is read once, C-codes are extracted with a simple ``C\d+``
    regex, and each match contributes ``dom_name`` to that code's list. Domain
    list per code is sorted + deduped at the end for stable output.
    """
    per_code: dict[str, set[str]] = {}
    if not KB_DOMAINS.is_dir():
        return {}
    pattern = re.compile(r"\bC\d{4,}\b")
    for dom_dir in sorted(KB_DOMAINS.iterdir()):
        if not dom_dir.is_dir():
            continue
        spec = dom_dir / "spec.md"
        if not spec.is_file():
            continue
        try:
            text = spec.read_text(encoding="utf-8", errors="strict")
        except OSError:
            continue
        dom_name = dom_dir.name
        seen_in_file: set[str] = set()
        for m in pattern.finditer(text):
            code = m.group(0)
            if code in seen_in_file:
                continue
            seen_in_file.add(code)
            per_code.setdefault(code, set()).add(dom_name)
    return {k: sorted(v) for k, v in per_code.items()}


# --- Codelist aggregation + rendering --------------------------------------


def _truncate_definition(text: str, tier: str = "high") -> str:
    """Truncate a definition cell with ``...`` based on tier budget.

    - ``tier="high"``: hard cap at 200 chars, simple suffix trim. Keeps all
      provenance tags (e.g. ``(NCI)``) inside the budget.
    - ``tier="mid"``: cap at 100 chars with word-boundary truncation. If the
      budgeted slice cuts a word, we back off to the nearest preceding space so
      the displayed prefix never ends mid-word.
    """
    if tier == "mid":
        limit = DEFINITION_CHAR_LIMIT_MID
    else:
        limit = DEFINITION_CHAR_LIMIT_HIGH

    if len(text) <= limit:
        return text

    keep = limit - len(TRUNCATE_MARKER)
    if keep <= 0:
        return TRUNCATE_MARKER

    # Default character-slice budget.
    prefix = text[:keep]

    if tier == "mid":
        # Back off to the last whitespace so the last word is not cut mid-token.
        space_idx = prefix.rfind(" ")
        # Only back off if we found a space AND it leaves a non-trivial prefix.
        # Guard: if the first `keep` chars contain no space at all, we fall
        # back to the raw slice rather than emptying the cell.
        if space_idx > 0:
            prefix = prefix[:space_idx]

    return prefix.rstrip() + TRUNCATE_MARKER


def _escape_cell(text: str) -> str:
    """Escape pipe characters so rendered rows don't corrupt the table."""
    return text.replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def aggregate_codelist(
    ccode: str,
    locations: list[tuple[Path, int]],
) -> tuple[str, str, str, list[list[str]], Path]:
    """Aggregate one codelist across its locations.

    Returns ``(name, ccode, extensible_line, term_rows, first_source_path)``.
    ``term_rows`` is deduped by the leftmost Code cell, in the order first seen.
    """
    first_path, first_line = locations[0]
    text = first_path.read_text(encoding="utf-8", errors="strict").splitlines()
    m = CODELIST_HDR_RE.match(text[first_line])
    name = m.group(1) if m else ccode
    extensible, first_body, _ = _extract_codelist_section(text, first_line)

    # Dedup key = Code cell (column 0).
    seen: set[str] = set()
    aggregated: list[list[str]] = []
    for row in first_body:
        key = row[0]
        if key and key not in seen:
            seen.add(key)
            aggregated.append(row)

    # Merge additional locations (multi-file codelists, e.g. split across parts).
    for extra_path, extra_line in locations[1:]:
        extra_text = extra_path.read_text(
            encoding="utf-8", errors="strict"
        ).splitlines()
        _, extra_body, _ = _extract_codelist_section(extra_text, extra_line)
        for row in extra_body:
            key = row[0]
            if key and key not in seen:
                seen.add(key)
                aggregated.append(row)

    return name, ccode, extensible, aggregated, first_path


def render_codelist(
    name: str,
    ccode: str,
    extensible: str,
    rows: list[list[str]],
    source_rel: str,
    related_domains: list[str],
    tier: str = "high",
) -> tuple[str, int]:
    """Render one codelist to markdown. Return (text, truncation_count).

    Format (refinement B, tier=high — 4 columns):
      <!-- source: ... -->
      ## Name (Cxxxxx)

      Extensible: Yes/No
      Related Domains: DOM1, DOM2, ... | —

      | Code | CDISC Submission Value | CDISC Synonym(s) | CDISC Definition |
      |------|----------------------|-------------------|------------------|
      | ... |

    Format (tier=mid — 3 columns, Synonyms dropped, Definition ≤ 100 chars,
    word-boundary truncation):

      | Code | CDISC Submission Value | CDISC Definition |
      |------|----------------------|------------------|
      | ... |

    ``truncation_count`` is the number of term rows whose Definition cell was
    truncated; used for the completion report.
    """
    out: list[str] = []
    out.append(f"<!-- source: {source_rel} -->")
    out.append(f"## {name} ({ccode})")
    out.append("")
    if extensible:
        out.append(extensible)

    # Related Domains as a single codelist-level metadata line (not per-row).
    related_str = ", ".join(related_domains) if related_domains else "\u2014"
    out.append(f"Related Domains: {related_str}")
    out.append("")

    if tier == "mid":
        out.append("| Code | CDISC Submission Value | CDISC Definition |")
        out.append("|------|----------------------|------------------|")
    else:
        out.append(
            "| Code | CDISC Submission Value | CDISC Synonym(s) | CDISC Definition |"
        )
        out.append(
            "|------|----------------------|-------------------|------------------|"
        )

    truncated = 0
    for row in rows:
        code, sub, syn, defn = row[0], row[1], row[2], row[3]
        new_defn = _truncate_definition(defn, tier=tier)
        if new_defn != defn:
            truncated += 1
        if tier == "mid":
            cells = [
                _escape_cell(code),
                _escape_cell(sub),
                _escape_cell(new_defn),
            ]
        else:
            cells = [
                _escape_cell(code),
                _escape_cell(sub),
                _escape_cell(syn),
                _escape_cell(new_defn),
            ]
        out.append("| " + " | ".join(cells) + " |")
    out.append("")
    return "\n".join(out), truncated


# --- Document assembly (per-subdir split) -----------------------------------


def _iso_from_mtimes(paths: list[Path]) -> str:
    """ISO-8601 UTC string from max mtime of the given paths."""
    mtimes = [p.stat().st_mtime for p in paths if p.is_file()]
    if not mtimes:
        return "1970-01-01T00:00:00Z"
    latest = max(mtimes)
    return _dt.datetime.fromtimestamp(latest, tz=_dt.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def _read_codelist_list(list_path: Path) -> list[str]:
    """Parse the codelist list file (plain text, one C-code per line).

    Ignores blank lines and ``#`` comments. Preserves input order.
    """
    out: list[str] = []
    for ln in list_path.read_text(encoding="utf-8", errors="strict").splitlines():
        ln = ln.split("#", 1)[0].strip()
        if not ln:
            continue
        if re.fullmatch(r"C\d+", ln):
            out.append(ln)
    return out


# CL record after resolution: all fields ready to render.
_CLRecord = tuple[str, str, str, list[list[str]], Path, list[str]]
# (name, ccode, extensible, rows, source_path, related_domains)


def resolve_codelists(
    codelists: list[str],
    cl_index: dict[str, list[tuple[Path, int]]],
    dom_index: dict[str, list[str]],
) -> tuple[list[_CLRecord], list[str]]:
    """Resolve all C-codes into render-ready records. Return (records, missing).

    Records are returned in the same order as ``codelists`` (F1 ranking order).
    """
    records: list[_CLRecord] = []
    missing: list[str] = []
    for ccode in codelists:
        locs = cl_index.get(ccode)
        if not locs:
            missing.append(ccode)
            continue
        name, cc, extensible, rows, first_path = aggregate_codelist(ccode, locs)
        related_domains = dom_index.get(ccode, [])
        records.append((name, cc, extensible, rows, first_path, related_domains))
    return records, missing


def _subdir_of(path: Path) -> str:
    """Return the subdir name (``core`` / ``questionnaires`` / ``supplementary``) for a path."""
    # The path is knowledge_base/terminology/<subdir>/<file>.md
    return path.parent.name


def build_subdir_documents(
    tier: str,
    records: list[_CLRecord],
    ts: str,
) -> dict[str, tuple[str, list[tuple[str, int, int, int]], list[tuple[str, int]]]]:
    """Build per-subdir documents from the ordered records list.

    Returns ``{subdir: (full_text, per_cl_summary, truncations)}``.
    Records within each subdir appear in their original F1 ranking order
    because we iterate ``records`` (already in rank order) and bin by subdir.
    """
    encoder = tiktoken.get_encoding(ENCODING_NAME)

    # Partition records into subdirs preserving order.
    subdir_records: dict[str, list[_CLRecord]] = {s: [] for s in TERM_SUBDIRS}
    for rec in records:
        _name, _cc, _ext, _rows, src_path, _rels = rec
        sub = _subdir_of(src_path)
        if sub in subdir_records:
            subdir_records[sub].append(rec)
        else:
            # Unexpected subdir — put in core as fallback.
            subdir_records["core"].append(rec)

    result: dict[str, tuple[str, list[tuple[str, int, int, int]], list[tuple[str, int]]]] = {}

    tier_meta = SUBDIR_META_BY_TIER.get(tier, SUBDIR_META_BY_TIER["high"])

    for sub in TERM_SUBDIRS:
        recs = subdir_records[sub]
        file_suffix, file_num, title_label = tier_meta[sub]

        out: list[str] = []
        out.append(
            f"<!-- generated by scripts_v2/extract_terminology_terms.py --tier {tier} "
            f"at {ts} -->"
        )
        out.append("")
        out.append(f"# {file_num} Terminology \u2014 {title_label}")
        out.append("")
        if tier == "mid":
            out.append(
                f"Mid-frequency CDISC controlled terminology codelists sourced from "
                f"``knowledge_base/terminology/{sub}/``. "
                "Each codelist keeps a compact 3-column Term table (Code / Submission "
                "Value / Definition) with Definitions truncated to 100 characters at "
                "word boundaries. Synonyms and NCI Concept Description links are "
                "omitted at this tier to fit the capacity budget. \"Related Domains\" "
                "is a codelist-level metadata line listing SDTM domains whose spec.md "
                "references the codelist C-code."
            )
        else:
            out.append(
                f"High-frequency CDISC controlled terminology codelists sourced from "
                f"``knowledge_base/terminology/{sub}/``. "
                "Each codelist preserves its 4-column Term table (Code / Submission Value / "
                "Synonyms / Definition) with Definitions truncated to 200 characters. "
                "\"Related Domains\" is a codelist-level metadata line listing SDTM domains "
                "whose spec.md references the codelist C-code."
            )
        out.append("")

        summary: list[tuple[str, int, int, int]] = []
        truncations: list[tuple[str, int]] = []
        first = True

        for name, cc, extensible, rows, src_path, related_domains in recs:
            rel_src = src_path.relative_to(REPO_ROOT).as_posix()
            if not first:
                out.append("---")
                out.append("")
            first = False
            rendered, truncated = render_codelist(
                name, cc, extensible, rows, rel_src, related_domains, tier=tier
            )
            out.append(rendered)
            tokens = len(encoder.encode(rendered))
            summary.append((cc, len(rows), tokens, len(related_domains)))
            if truncated:
                truncations.append((cc, truncated))

        # Normalize trailing blanks.
        while out and out[-1].strip() == "":
            out.pop()
        out.append("")

        result[sub] = ("\n".join(out), summary, truncations)

    return result


# --- Failure evidence -------------------------------------------------------


def write_failure_file(
    list_path: Path,
    missing: list[str],
    exit_code: int,
    stderr_tail: str,
    tier: str = "high",
) -> Path:
    """Write a 规则-B failure file for missing C-codes. Always safe to call.

    Failure filename includes the tier so high (F2) and mid (G2) attempts do
    not overwrite each other.
    """
    FAILURES_DIR.mkdir(parents=True, exist_ok=True)
    stage_label = "v2.4" if tier == "high" else "v2.5_g2"
    failure_path = FAILURES_DIR / f"stage_{stage_label}_attempt_1.md"
    md5 = hashlib.md5(
        list_path.read_bytes() if list_path.is_file() else b""
    ).hexdigest()
    header = "F2 executor" if tier == "high" else "G2 executor"
    content = [
        f"# Stage {stage_label} {header} failure report (attempt 1)",
        "",
        "## Input",
        f"- path: `{list_path}`",
        f"- md5: `{md5}`",
        "",
        "## Missing C-codes",
    ]
    if missing:
        for cc in missing:
            content.append(
                f"- `{cc}` \u2014 not found under "
                f"`knowledge_base/terminology/{{core,questionnaires,supplementary}}/*.md`"
            )
    else:
        content.append("- (none)")
    content.append("")
    content.append("## Exit")
    content.append(f"- exit code: `{exit_code}`")
    content.append("")
    content.append("## Stderr tail")
    content.append("```")
    content.append(stderr_tail.rstrip() or "(empty)")
    content.append("```")
    content.append("")
    content.append("## Suggested next attempt input")
    content.append(
        "- Re-run F1 scorer with broader terminology include path, or "
        "manually backfill the missing C-codes from the IG appendix."
    )
    content.append("")
    failure_path.write_text("\n".join(content), encoding="utf-8")
    return failure_path


# --- CLI entry point --------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, add_help=True)
    parser.add_argument("--tier", choices=("high", "mid"), required=True)
    parser.add_argument("--list", dest="list_path")
    args = parser.parse_args(argv)

    if not args.list_path:
        print(f"--tier {args.tier} requires --list <path>", file=sys.stderr)
        return 2
    list_path = Path(args.list_path).expanduser().resolve()
    if not list_path.is_file():
        print(f"--list not found: {list_path}", file=sys.stderr)
        return 2

    codelists = _read_codelist_list(list_path)
    if not codelists:
        print(f"no C-codes parsed from {list_path}", file=sys.stderr)
        return 2

    cl_index = build_codelist_index()
    dom_index = build_domain_index()

    records, missing = resolve_codelists(codelists, cl_index, dom_index)

    # Compute shared timestamp from all touched source files.
    touched_paths: list[Path] = [r[4] for r in records]
    for dom_dir in (sorted(KB_DOMAINS.iterdir()) if KB_DOMAINS.is_dir() else []):
        spec = dom_dir / "spec.md"
        if spec.is_file():
            touched_paths.append(spec)
    ts = _iso_from_mtimes(touched_paths)

    subdir_docs = build_subdir_documents(args.tier, records, ts)

    encoder = tiktoken.get_encoding(ENCODING_NAME)
    tag = f"[Tier {args.tier}]"
    tier_meta = SUBDIR_META_BY_TIER[args.tier]

    # Write all 3 output files.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    overall_exit = 0
    all_truncations: list[tuple[str, int]] = []

    for sub in TERM_SUBDIRS:
        full_text, summary, truncations = subdir_docs[sub]
        file_suffix, _file_num, _label = tier_meta[sub]
        out_path = OUTPUT_DIR / file_suffix
        out_path.write_text(full_text, encoding="utf-8")

        token_count = len(encoder.encode(full_text))
        cl_count = len(summary)
        print(
            f"{tag} {out_path.name}: {cl_count} codelists, {token_count} tokens "
            f"(soft <={SOFT_TARGET // 1000}K, hard <={HARD_CAP // 1000}K)"
        )

        # Per-codelist stderr summary.
        for ccode, term_count, tokens, rd_count in summary:
            print(f"{ccode}\t{term_count}\t{tokens}\t{rd_count}", file=sys.stderr)

        all_truncations.extend(truncations)

        if token_count > HARD_CAP:
            print(
                f"{tag} EXCEED_HARD_CAP [{sub}]: {token_count} > {HARD_CAP}",
                file=sys.stderr,
            )
            overall_exit = 1
        elif token_count > SOFT_TARGET:
            print(
                f"{tag} WARN [{sub}]: {token_count} tokens above soft target {SOFT_TARGET} "
                f"(continuing)",
                file=sys.stderr,
            )

    # Summary totals.
    included = len(records)
    print(f"{tag} codelists requested: {len(codelists)}")
    print(f"{tag} codelists included:  {included}")
    print(f"{tag} codelists missing:   {len(missing)}")
    if missing:
        print(f"{tag} missing C-codes: {', '.join(missing)}")

    # Top-3 truncation offenders.
    all_truncations.sort(key=lambda t: t[1], reverse=True)
    top3 = all_truncations[:3]
    if top3:
        trunc_desc = ", ".join(f"{cc}({n})" for cc, n in top3)
        print(f"{tag} top3 truncation impact: {trunc_desc}")

    # Delete the old single-file output if it still exists (cleanup from v1 run).
    # Only relevant for tier=high (legacy v1 file had no mid equivalent).
    if args.tier == "high":
        old_file = OUTPUT_DIR / "11_terminology_high.md"
        if old_file.exists():
            old_file.unlink()
            print(f"{tag} deleted legacy file: {old_file.name}")

    # Missing C-codes are reported but not a hard failure.
    if missing:
        write_failure_file(list_path, missing, overall_exit, "", tier=args.tier)

    return overall_exit


if __name__ == "__main__":
    sys.exit(main())
