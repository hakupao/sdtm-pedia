#!/usr/bin/env python3
"""Merge 63 SDTM domain spec.md files into a single Mega Spec.

Phase 6.5 Claude Projects — Step 6 (PLAN.md §4.3.1 / §7.4).

Reads:  knowledge_base/domains/<DOM>/spec.md   (read-only, 63 files)
Writes: ai_platforms/claude_projects/output/05_mega_spec.md

Algorithm (base level):
  - Parse each spec.md into: (dom, full_name, class_line, variables[], xrefs{})
  - Emit per-domain section: H2 header + Specification table (7 cols) + Cross References
  - Notes truncated to 200 chars (hard cap). CT column keeps only Cxxxxx codes.
  - Cross References compacted from 4 sub-headings to 4 bold lines.

Output is deterministic (stable key order, source mtime timestamp).
Idempotent: two runs produce byte-identical output.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[3]
DOMAINS_DIR = REPO_ROOT / "knowledge_base" / "domains"
OUTPUT_FILE = (
    REPO_ROOT / "ai_platforms" / "claude_projects" / "output" / "05_mega_spec.md"
)

# 63 domains in canonical (alphabetical) order — discovered from
# knowledge_base/domains/ (frozen list; matches file system exactly).
DOMAINS = [
    "AE", "AG", "BE", "BS", "CE", "CM", "CO", "CP", "CV", "DA",
    "DD", "DM", "DS", "DV", "EC", "EG", "EX", "FA", "FT", "GF",
    "HO", "IE", "IS", "LB", "MB", "MH", "MI", "MK", "ML", "MS",
    "NV", "OE", "OI", "PC", "PE", "PP", "PR", "QS", "RE", "RELREC",
    "RELSPEC", "RELSUB", "RP", "RS", "SC", "SE", "SM", "SR", "SS",
    "SU", "SUPPQUAL", "SV", "TA", "TD", "TE", "TI", "TM", "TR",
    "TS", "TU", "TV", "UR", "VS",
]

# ---------------------------------------------------------------------------
# Compression parameters (base level; bumped by fallback loop)
# ---------------------------------------------------------------------------

NOTES_MAX_CHARS = 150       # fallback level 1 (base 200 -> 150)
DROP_GENERAL_MODEL = False  # fallback level 2
CT_COMPACT = False          # fallback level 3 (Cxxxxx (N vars))
DROP_NOTES_COL = False      # fallback level 4 (drop Notes column entirely)
SMART_NOTES = True          # level 5 (hybrid): keep only structured signals
# Fallback trigger: if SMART_NOTES result exceeds this, auto-fall-back to L4.
SMART_NOTES_FALLBACK_TOKENS = 66000
SMART_NOTES_CELL_CAP = 60   # hard cap per Notes cell

# ---------------------------------------------------------------------------
# Regex (module-level, reused)
# ---------------------------------------------------------------------------

RE_H1 = re.compile(r"^# ([A-Z]+)\s+—\s+(.+?)\s*$")
RE_H3 = re.compile(r"^### ([A-Z][A-Z0-9_]*)\s*$")
RE_BULLET = re.compile(r"^- \*\*([^:]+):\*\*\s*(.*?)\s*$")
RE_CT_CODE = re.compile(r"C\d{5,6}")
RE_CT_XREF_ENTRY = re.compile(
    r"^- \[(?P<name>.+?)\s*\((?P<code>C\d{5,6})\)\]\([^)]+\)\s*—\s*(?P<vars>.+?)\s*$"
)


def parse_spec(dom: str, path: Path) -> dict:
    """Parse a domains/<DOM>/spec.md into a structured dict."""
    text = path.read_text(encoding="utf-8", errors="strict")
    lines = text.splitlines()

    full_name = ""
    class_line = ""
    variables: list[dict] = []
    xrefs: dict[str, list[str]] = {
        "ct": [],
        "related": [],
        "general": [],
        "model": [],
    }

    # --- Split header / body / cross-refs ---
    idx = 0
    n = len(lines)

    # Header
    while idx < n and not lines[idx].startswith("# "):
        idx += 1
    if idx < n:
        m = RE_H1.match(lines[idx])
        if m:
            # source dom may be RELREC, etc. Header gives canonical name.
            full_name = m.group(2).strip()
        idx += 1

    # "> Class: ... | Structure: ..."
    while idx < n and not lines[idx].strip():
        idx += 1
    if idx < n and lines[idx].startswith("> "):
        class_line = lines[idx][2:].strip()
        idx += 1

    # --- Variable sections ---
    current: dict | None = None

    def flush():
        if current is not None:
            variables.append(current)

    while idx < n:
        line = lines[idx]
        # Stop variable parsing at the "## Cross References" heading
        if line.startswith("## Cross References"):
            flush()
            current = None
            idx += 1
            break

        m3 = RE_H3.match(line)
        if m3 and not line.startswith("### Controlled Terminology") \
                and not line.startswith("### Related Domains") \
                and not line.startswith("### General References") \
                and not line.startswith("### Model Definition"):
            flush()
            current = {
                "name": m3.group(1),
                "order": "",
                "label": "",
                "type": "",
                "ct_raw": "",
                "role": "",
                "core": "",
                "notes": "",
            }
            idx += 1
            continue

        if current is not None:
            mb = RE_BULLET.match(line)
            if mb:
                key = mb.group(1).strip()
                val = mb.group(2).strip()
                if key == "Order":
                    current["order"] = val
                elif key == "Label":
                    current["label"] = val
                elif key == "Type":
                    current["type"] = val
                elif key == "Controlled Terms":
                    current["ct_raw"] = val
                elif key == "Role":
                    current["role"] = val
                elif key == "Core":
                    current["core"] = val
                elif key == "CDISC Notes":
                    current["notes"] = val
        idx += 1
    else:
        # Fell off the end without hitting "## Cross References"
        flush()

    # --- Cross References body ---
    current_section: str | None = None
    while idx < n:
        line = lines[idx]
        s = line.strip()
        if s.startswith("### Controlled Terminology"):
            current_section = "ct"
        elif s.startswith("### Related Domains"):
            current_section = "related"
        elif s.startswith("### General References"):
            current_section = "general"
        elif s.startswith("### Model Definition"):
            current_section = "model"
        elif current_section and line.startswith("- "):
            xrefs[current_section].append(line[2:].rstrip())
        idx += 1

    return {
        "dom": dom,
        "full_name": full_name,
        "class_line": class_line,
        "variables": variables,
        "xrefs": xrefs,
    }


def extract_ct_code(ct_raw: str) -> str:
    """Extract a single CT code from 'Controlled Terms:' field.

    Rules:
      - empty/whitespace -> ""
      - contains Cxxxxx  -> first match
      - 'ISO 8601 ...'   -> "ISO 8601"  (keep semantic marker; short)
      - 'MedDRA'         -> "MedDRA"
      - otherwise        -> first token (trimmed to ≤12 chars)
    """
    s = (ct_raw or "").strip()
    if not s:
        return ""
    m = RE_CT_CODE.search(s)
    if m:
        return m.group(0)
    low = s.lower()
    if low.startswith("iso 8601"):
        return "ISO 8601"
    if low.startswith("meddra"):
        return "MedDRA"
    # Truncate any other tag
    return s[:12]


def compress_notes(notes: str, max_chars: int) -> str:
    """Flatten + trim notes for a table cell.

    - Collapse all whitespace (incl. newlines) to single spaces.
    - Escape '|' so the table stays valid.
    - Truncate to max_chars with '...' if exceeded.
    """
    if not notes:
        return ""
    # Collapse whitespace
    s = re.sub(r"\s+", " ", notes).strip()
    # Table-safe: escape pipes
    s = s.replace("|", "\\|")
    if len(s) > max_chars:
        # Try to cut at a sentence boundary within last 40 chars of the cap
        cut = s[:max_chars]
        # Prefer to end at a period; but don't lose 'See §X.Y' if it starts right after cap
        tail = s[max_chars : max_chars + 40]
        see_match = re.search(r"\bSee\s+Section\s+\d+(\.\d+)*", tail) or re.search(
            r"\bSee\s+§\d", tail
        )
        if see_match:
            # Keep cut + " ... " + the See-ref substring up to a reasonable end
            ref_start = see_match.start()
            ref_end = see_match.end() + 20  # small tail for rest of section ref
            suffix = tail[ref_start:ref_end].split(".")[0].rstrip(",; ")
            return cut.rstrip() + " ... " + suffix
        # Soft cut at last space
        last_space = cut.rfind(" ")
        if last_space > max_chars - 40:
            cut = cut[:last_space]
        return cut.rstrip(",; ") + "..."
    return s


# ---------------------------------------------------------------------------
# Smart Notes compaction (Level 5 / hybrid)
# ---------------------------------------------------------------------------

RE_SN_SECTION = re.compile(
    r"See\s+(?:Section\s+)?§?(\d+(?:\.\d+)+)",
    re.IGNORECASE,
)
RE_SN_DERIVED = re.compile(
    r"derived from\s+([A-Z][A-Z0-9_]*(?:[,/\s]+(?:and\s+)?[A-Z][A-Z0-9_]*)*)",
)
RE_SN_REQWHEN = re.compile(
    r"Required when\s+([^\.\n]+)",
    re.IGNORECASE,
)
RE_SN_ISO = re.compile(
    r"ISO\s*(?:8601|3166|4217|639|\d{3,5})(?:-\d+)?[^\.\n]*",
    re.IGNORECASE,
)
RE_SN_EXAMPLES = re.compile(
    r"Examples?:\s*(\"[^\"]+\"(?:\s*,\s*\"[^\"]+\"){0,4})",
)
RE_SN_VALIDVALS = re.compile(
    r"Valid values?\s+(?:are|is)\s+([^\.\n]+)",
    re.IGNORECASE,
)
RE_SN_SPONSOR = re.compile(
    r"(?i)\bsponsor(?:-defined|-specified)\b",
)
RE_SN_NOTALLOWED = re.compile(
    r"([^\.]*(?:not allowed|not submitted)[^\.\n]*)",
    re.IGNORECASE,
)


def _truncate(s: str, cap: int) -> str:
    s = s.strip()
    if len(s) <= cap:
        return s
    return s[: cap - 1].rstrip(",; ") + "…"


def smart_compact_notes(raw_notes: str) -> str:
    """Extract structured signals from a CDISC Notes string.

    Priority order (each hit independently contributes a fragment):
      1. §-section references      -> "See §X.Y.Z"
      2. "derived from <VARS>"     -> "derived from VARA, VARB"
      3. "Required when <cond>"    -> "Req when <cond>"
      4. ISO 8601 mentions         -> "ISO 8601 [type]"
      5. Examples: "A", "B", "C"   -> 'Ex: "A", "B", "C"'
      6. Valid values are ...      -> "Vals: ..."
      7. Sponsor-defined phrase    -> "sponsor-defined"
      8. not allowed/not submitted -> leading <=30 chars of the clause

    Fragments joined with "; ", each capped to its rule max, whole cell
    capped to SMART_NOTES_CELL_CAP (60) with trailing ellipsis when cut.
    """
    if not raw_notes:
        return ""
    # Flatten whitespace once
    text = re.sub(r"\s+", " ", raw_notes).strip()
    if not text:
        return ""

    fragments: list[str] = []

    # 1. Section reference (cap 15)
    m = RE_SN_SECTION.search(text)
    if m:
        fragments.append(_truncate(f"See §{m.group(1)}", 15))

    # 2. derived from <VARS> (cap 35 — preserves full var names like BRTHDTC)
    m = RE_SN_DERIVED.search(text)
    if m:
        vars_str = re.sub(r"\s+", " ", m.group(1)).strip().rstrip(",. ")
        fragments.append(_truncate(f"derived from {vars_str}", 35))

    # 3. Required when (cap 30)
    m = RE_SN_REQWHEN.search(text)
    if m:
        cond = m.group(1).strip().rstrip(",. ")
        fragments.append(_truncate(f"Req when {cond}", 30))

    # 4. ISO standard reference (short tag; cap 10)
    m = RE_SN_ISO.search(text)
    if m:
        # Extract just the ISO number+part (e.g. "3166-1", "8601", "4217")
        num_m = re.search(r"(?:8601|3166|4217|639|\d{3,5})(?:-\d+)?", m.group(0), re.IGNORECASE)
        iso_tag = f"ISO {num_m.group(0)}" if num_m else "ISO"
        fragments.append(iso_tag)

    # 5. Examples (1 item, cap 20). Examples are by far the most common hit
    # (~20% of all vars, 378 of 1917); emitting 2+ examples pushes total
    # tokens past the 66K fallback threshold. The 1st example preserves
    # the "unique" signal (e.g. "SUPINE" hints at posture vs free-text);
    # callers who need the full list should read the source spec.md.
    m = RE_SN_EXAMPLES.search(text)
    if m:
        ex_list = re.findall(r"\"([^\"]+)\"", m.group(1))
        if ex_list:
            fragments.append(_truncate(f'Ex: "{ex_list[0]}"', 20))

    # 6. Valid values (cap 30). Do not duplicate when Examples already
    # matched a clearly distinct segment.
    m = RE_SN_VALIDVALS.search(text)
    if m:
        vals = m.group(1).strip().rstrip(",. ")
        fragments.append(_truncate(f"Vals: {vals}", 30))

    # 7. Sponsor-defined: emit only when truly load-bearing, i.e. the phrase
    # is the primary semantic payload (e.g. "Sponsor-defined identifier.")
    # AND no other fragment fired. Otherwise the tag adds 15 tokens x 120+
    # vars for low signal (sponsor-defined RFSTDTC etc. is inferable from
    # context).
    if not fragments and RE_SN_SPONSOR.search(text):
        # Require the phrase to appear in the first 25 chars (i.e. the
        # sentence actually leads with it) to keep precision high.
        head = text[:25].lower()
        if "sponsor-defined" in head or "sponsor defined" in head:
            fragments.append("sponsor-defined")

    # 8. not allowed / not submitted (cap 30). Only if no earlier fragment
    # already captured a §-ref that supersedes the prohibition clause.
    if not any(f.startswith("See §") for f in fragments):
        m = RE_SN_NOTALLOWED.search(text)
        if m:
            clause = m.group(1).strip().rstrip(",. ")
            # Strip leading connective words like "and " / "but "
            clause = re.sub(r"^(and|but|;|,)\s+", "", clause, flags=re.IGNORECASE)
            fragments.append(_truncate(clause, 30))

    if not fragments:
        return ""

    # Dedup preserving order
    seen = set()
    dedup: list[str] = []
    for f in fragments:
        if f not in seen:
            dedup.append(f)
            seen.add(f)

    joined = "; ".join(dedup)
    # Hard cell cap
    if len(joined) > SMART_NOTES_CELL_CAP:
        joined = joined[: SMART_NOTES_CELL_CAP - 1].rstrip(",;:  ") + "…"
    # Table-safe
    return joined.replace("|", "\\|")


def render_specification_table(vars_: list[dict], drop_notes: bool) -> str:
    if drop_notes:
        header = "| # | Name | Label | Type | Role | Core | CT |"
        sep = "|---|------|-------|------|------|------|----|"
    else:
        header = "| # | Name | Label | Type | Role | Core | CT | Notes |"
        sep = "|---|------|-------|------|------|------|----|-------|"
    rows = [header, sep]
    for v in vars_:
        order = v.get("order", "") or ""
        name = v.get("name", "") or ""
        label = (v.get("label", "") or "").replace("|", "\\|")
        vtype = (v.get("type", "") or "").replace("|", "\\|")
        role = (v.get("role", "") or "").replace("|", "\\|")
        core = (v.get("core", "") or "").replace("|", "\\|")
        ct = extract_ct_code(v.get("ct_raw", ""))
        if drop_notes:
            rows.append(
                f"| {order} | {name} | {label} | {vtype} | {role} | {core} | {ct} |"
            )
        else:
            if SMART_NOTES:
                notes = smart_compact_notes(v.get("notes", ""))
            else:
                notes = compress_notes(v.get("notes", ""), NOTES_MAX_CHARS)
            rows.append(
                f"| {order} | {name} | {label} | {vtype} | {role} | {core} | {ct} | {notes} |"
            )
    return "\n".join(rows)


def render_ct_xref(ct_entries: list[str]) -> str:
    """Compact CT cross-ref lines into 'VAR→Cxxxxx' groups.

    Input entries look like:
      '[Name (Cxxxxx)](...link...) — VARA, VARB, VARC ... (13 total)'

    Output: groups variables per CT code, joins with '/', appends '(N)' when
    the source had 'N total'.

    When CT_COMPACT is enabled, collapses per-code entries to 'Cxxxxx (N vars)'.
    """
    by_code: dict[str, dict] = {}  # code -> {name, vars, total}
    for entry in ct_entries:
        m = RE_CT_XREF_ENTRY.match("- " + entry)
        if not m:
            # Fallback: just keep raw text
            by_code.setdefault("_raw", {"vars": [], "raw": []})["raw"].append(entry)
            continue
        code = m.group("code")
        vars_part = m.group("vars")
        # Extract "(N total)" if present
        total = None
        tm = re.search(r"\((\d+)\s+total\)", vars_part)
        if tm:
            total = int(tm.group(1))
            vars_part = vars_part[: tm.start()].rstrip(" .")
        # Strip trailing "..." when there's a total
        vars_part = re.sub(r"\s*\.\.\.\s*$", "", vars_part).strip()
        # Split on comma OR slash
        vars_list = [v.strip() for v in re.split(r"[,/]", vars_part) if v.strip()]
        d = by_code.setdefault(code, {"vars": [], "total": total})
        for v in vars_list:
            if v not in d["vars"]:
                d["vars"].append(v)
        if total and not d.get("total"):
            d["total"] = total

    parts = []
    for code, d in by_code.items():
        if code == "_raw":
            continue
        if CT_COMPACT:
            n = d.get("total") or len(d["vars"])
            parts.append(f"{code} ({n} vars)")
        else:
            vars_joined = "/".join(d["vars"])
            total = d.get("total")
            if total and total > len(d["vars"]):
                parts.append(f"{vars_joined}→{code} ({total})")
            else:
                parts.append(f"{vars_joined}→{code}")
    if not parts:
        return ""
    return ", ".join(parts)


def render_related(related: list[str]) -> str:
    """Flatten 'Related Domains' bullet list to one line, preserving semantics.

    Remove [Name](link) markup but keep domain codes and the human description.
    """
    out = []
    for entry in related:
        s = entry
        # Replace [TEXT](url) -> TEXT (keep visible text)
        s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
        # Trailing ')' artifacts, collapse whitespace
        s = re.sub(r"\s+", " ", s).strip()
        out.append(s)
    # Join each bullet with '. '
    joined = ". ".join(out)
    # Tidy double periods
    joined = re.sub(r"\.{2,}", ".", joined)
    if joined and not joined.endswith("."):
        joined += "."
    return joined


def render_general(general: list[str]) -> str:
    """Compact 'General References' to key labels.

    Each entry typically: '[General Assumptions (Ch4)](...) — variable naming, ...'
    We map to 'ch04', 'ch08', 'VARIABLE_INDEX'.
    """
    labels = []
    for entry in general:
        s = entry
        if "ch04" in s.lower() or "Ch4" in s or "Chapter 4" in s:
            labels.append("ch04 (naming/coding/timing)")
        elif "ch08" in s.lower() or "Ch8" in s or "Chapter 8" in s:
            labels.append("ch08 (RELREC/SUPPQUAL)")
        elif "variable_index" in s.lower() or "Variable Index" in s:
            labels.append("VARIABLE_INDEX")
        elif "ch10" in s.lower() or "Ch10" in s:
            labels.append("ch10")
        elif "ch01" in s.lower() or "Ch1" in s:
            labels.append("ch01")
        elif "ch02" in s.lower() or "Ch2" in s:
            labels.append("ch02")
        elif "ch03" in s.lower() or "Ch3" in s:
            labels.append("ch03")
        else:
            # Unknown entry: strip link markup, keep a short version
            s2 = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
            s2 = re.sub(r"\s*—.*$", "", s2).strip()
            if s2:
                labels.append(s2[:40])
    # Dedup preserving order
    seen = set()
    dedup = []
    for l in labels:
        if l not in seen:
            dedup.append(l)
            seen.add(l)
    return ", ".join(dedup)


def render_model(model: list[str]) -> str:
    """One-sentence pointer extracted from 'Model Definition'."""
    if not model:
        return ""
    s = model[0]
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def render_cross_references(xrefs: dict) -> str:
    lines = ["### Cross References"]
    ct_line = render_ct_xref(xrefs.get("ct", []))
    if ct_line:
        lines.append(f"- **CT:** {ct_line}")
    rel_line = render_related(xrefs.get("related", []))
    if rel_line:
        lines.append(f"- **Related:** {rel_line}")
    if not DROP_GENERAL_MODEL:
        gen_line = render_general(xrefs.get("general", []))
        if gen_line:
            lines.append(f"- **General:** {gen_line}")
        model_line = render_model(xrefs.get("model", []))
        if model_line:
            lines.append(f"- **Model:** {model_line}")
    return "\n".join(lines)


def render_domain(spec: dict) -> str:
    out = []
    rel_path = f"knowledge_base/domains/{spec['dom']}/spec.md"
    out.append(f"<!-- source: {rel_path} -->")
    out.append(f"## {spec['dom']} — {spec['full_name']}")
    if spec.get("class_line"):
        out.append(f"> {spec['class_line']}")
    out.append("")
    out.append("### Specification")
    out.append("")
    out.append(render_specification_table(spec["variables"], DROP_NOTES_COL))
    out.append("")
    out.append(render_cross_references(spec["xrefs"]))
    out.append("")
    return "\n".join(out)


def build_mega_spec(specs: list[dict], source_mtime_iso: str, total_vars: int) -> str:
    header = []
    header.append(
        f"<!-- generated by scripts/merge_specs.py (source mtime: {source_mtime_iso}) -->"
    )
    header.append(
        f"<!-- {len(specs)} domains merged from knowledge_base/domains/*/spec.md, "
        f"{total_vars} variables total -->"
    )
    header.append("")
    header.append("# SDTM Domain Specifications (Mega Spec)")
    header.append("")
    if DROP_NOTES_COL:
        cols_desc = (
            "Each domain has one H2 section containing a 7-column Specification table "
            "(# / Name / Label / Type / Role / Core / CT) and a compacted Cross "
            "References block. The CDISC Notes column was omitted to fit the Claude "
            "Project token budget; full Notes for every variable remain in the "
            "source `spec.md` listed in the `<!-- source: ... -->` comment above "
            "each domain and should be consulted for variable-specific guidance "
            "(coding rules, examples, §-references)."
        )
    elif SMART_NOTES:
        cols_desc = (
            "Each domain has an 8-column Specification table "
            "(#, Name, Label, Type, Role, Core, CT, Notes) plus a compacted "
            "Cross References block. Notes cells hold only structured signals "
            "extracted from the full CDISC Notes: section refs (`See §X.Y`), "
            "derivations (`derived from …`), conditions (`Req when …`), "
            "`ISO 8601`, `Ex:` / `Vals:` lists, `sponsor-defined`, and "
            "prohibition clauses (`not allowed` / `not submitted`). Pure "
            "prose is dropped; the full CDISC Notes for every variable live "
            "in the source `spec.md` identified by the `<!-- source: ... -->` "
            "comment above each domain and should be consulted whenever a "
            "Notes cell is empty or a variable-specific coding rule is needed."
        )
    else:
        cols_desc = (
            "Each domain has one H2 section containing an 8-column Specification "
            "table (# / Name / Label / Type / Role / Core / CT / Notes) and a "
            "compacted Cross References block. Notes are truncated; see source "
            "`spec.md` for full text."
        )
    header.append(
        "This file merges the 63 per-domain `spec.md` files into a single "
        f"reference. {cols_desc} "
        "CT column lists the CDISC NCI code (Cxxxxx) when applicable; otherwise "
        "`ISO 8601`, `MedDRA`, or blank. Chapter pointers in Cross References "
        "use short codes (ch04, ch08, VARIABLE_INDEX)."
    )
    header.append("")
    header.append("---")
    header.append("")

    sections = [render_domain(s) for s in specs]
    # Final single newline between sections
    body = "\n".join(sections)

    return "\n".join(header) + body


def compute_source_mtime(specs_paths: list[Path]) -> float:
    return max(p.stat().st_mtime for p in specs_paths)


def isoformat_mtime(mtime: float) -> str:
    from datetime import datetime, timezone

    return datetime.fromtimestamp(mtime, tz=timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def _count_cl100k_tokens(text: str) -> int | None:
    """Count tokens with cl100k_base. Returns None if tiktoken unavailable."""
    try:
        import tiktoken
    except Exception:
        return None
    try:
        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except Exception:
        return None


def main() -> int:
    global SMART_NOTES, DROP_NOTES_COL

    specs_paths = []
    for dom in DOMAINS:
        p = DOMAINS_DIR / dom / "spec.md"
        if not p.exists():
            print(f"error: missing spec.md for {dom}: {p}", file=sys.stderr)
            return 2
        specs_paths.append(p)

    specs = [parse_spec(dom, p) for dom, p in zip(DOMAINS, specs_paths)]
    total_vars = sum(len(s["variables"]) for s in specs)

    mtime = compute_source_mtime(specs_paths)
    mtime_iso = isoformat_mtime(mtime)

    content = build_mega_spec(specs, mtime_iso, total_vars)

    # Level 5 (hybrid smart notes) fallback: if the result blows past the
    # budget, rebuild at Level 4 (drop Notes column) deterministically.
    fallback_reason = ""
    if SMART_NOTES and not DROP_NOTES_COL:
        tok = _count_cl100k_tokens(content)
        if tok is not None and tok > SMART_NOTES_FALLBACK_TOKENS:
            fallback_reason = (
                f"smart-notes output {tok} tokens > "
                f"{SMART_NOTES_FALLBACK_TOKENS} budget"
            )
            SMART_NOTES = False
            DROP_NOTES_COL = True
            content = build_mega_spec(specs, mtime_iso, total_vars)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    # Ensure final newline for POSIX tooling
    if not content.endswith("\n"):
        content += "\n"
    OUTPUT_FILE.write_text(content, encoding="utf-8")

    if fallback_reason:
        print(f"[Step 6] fallback L4: {fallback_reason}")
    print(
        f"[Step 6] wrote {OUTPUT_FILE.relative_to(REPO_ROOT)} "
        f"({len(specs)} domains, {total_vars} variables)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
