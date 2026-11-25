#!/usr/bin/env python3
"""READ-ONLY floor estimator for Phase 6.5 Step 9 (08_terminology_map.md).

Measures the token cost of 5 optimization variants WITHOUT touching the
existing output file. All variants rebuild from source (knowledge_base/terminology/)
using tiktoken cl100k_base (same encoder as count_tokens.py, matches PLAN.md baselines).

Variants tested:
  baseline:  current output format (already-deployed one) for sanity check
  1: drop "Data Type" column          -- N/A, already dropped (sanity)
  2: bucketize Terms (<10, 10-50, 50-500, 500+)
  3: drop Related Domain (remove "-> XX" from section headings)
  4: abbreviate common words in Name (Code->Cd, Value->Val, Test->Ts, Submission->Sub, etc.)
  5: 5-col compact "Cxxxx|E|F|Terms|Name" single-row (no section grouping)

Also reports per-component token split: headers+narrative, section headings,
row bodies (code+mark+terms prefix), name strings.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

import tiktoken

ROOT = Path("/Users/bojiangzhang/MyProject/SDTM-compare")
SRC_DIR = ROOT / "knowledge_base" / "terminology"
CURRENT_OUT = ROOT / "ai_platforms" / "claude_projects" / "output" / "08_terminology_map.md"
SUBDIRS = ("core", "questionnaires", "supplementary")

CORE_DOMAIN_MAP: dict[str, str] = {
    "ae": "AE", "cp_part1": "CP", "cp_part2": "CP", "disposition": "DS", "dm": "DM",
    "eg_part1": "EG", "eg_part2": "EG", "eg_part3": "EG",
    "findings_about": "FA",
    "general_part1": "Cross-domain", "general_part2": "Cross-domain",
    "general_part3": "Cross-domain", "general_part4": "Cross-domain",
    "general_part5": "Cross-domain",
    "gf": "GF", "interventions": "CM/EX/EC/PR/SU",
    "is_domain_part1": "IS", "is_domain_part2": "IS",
    "lb_part1": "LB", "lb_part2": "LB", "lb_part3": "LB", "lb_part4": "LB",
    "mi": "MI", "microbiology_part1": "MB/MS", "microbiology_part2": "MB/MS",
    "microbiology_part3": "MB/MS",
    "oi": "OI", "oncology_part1": "TU/TR/RS", "oncology_part2": "TU/TR/RS",
    "other_part1": "Cross-domain", "other_part2": "Cross-domain",
    "other_part3": "Cross-domain", "other_part4": "Cross-domain",
    "other_part5": "Cross-domain",
    "pk_part1": "PC/PP", "pk_part2": "PC/PP", "pk_part3": "PC/PP", "pk_part4": "PC/PP",
    "qs_part1": "QS", "special_purpose": "DM/CO/SE/SM/SV",
    "trial_design": "TA/TD/TE/TI/TM/TS/TV", "vs": "VS",
}

HEADING_RE = re.compile(r"^##\s+(?P<name>.+?)\s+\((?P<code>C\d+)\)\s*$")
EXT_RE = re.compile(r"^Extensible:\s*(Yes|No)\s*$", re.IGNORECASE)
DATA_ROW_RE = re.compile(r"^\|\s*C\d+\s*\|")

enc = tiktoken.get_encoding("cl100k_base")

def tok(s: str) -> int: return len(enc.encode(s))

def related_domain_for(p: Path) -> str:
    sub = p.parent.name
    if sub == "core": return CORE_DOMAIN_MAP.get(p.stem, "Cross-domain")
    if sub == "questionnaires": return "QS"
    return "Cross-domain"

def parse_file(path: Path) -> list[dict]:
    records: list[dict] = []
    current: dict | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEADING_RE.match(line)
        if m:
            if current is not None: records.append(current)
            current = {"code": m.group("code"), "name": m.group("name").strip(),
                       "ext": "", "terms": 0}
            continue
        if current is None: continue
        m_ext = EXT_RE.match(line)
        if m_ext:
            current["ext"] = "Y" if m_ext.group(1).lower() == "yes" else "N"
            continue
        if DATA_ROW_RE.match(line): current["terms"] += 1
    if current is not None: records.append(current)
    return records

def iter_files() -> list[Path]:
    out: list[Path] = []
    for s in SUBDIRS:
        d = SRC_DIR / s
        if d.is_dir(): out.extend(sorted(d.glob("*.md")))
    return out

def sanitize(t: str) -> str:
    return re.sub(r"\s+", " ", t).replace("|", "\\|").strip()

def terms_str_current(n: int) -> str:
    # Current logic: just str(n) unless 500-1000 -> "500+", ≥1000 -> "1000+"
    if n < 500: return str(n)
    if n < 1000: return "500+"
    return "1000+"

def terms_str_bucket(n: int) -> str:
    if n <= 0: return "0"
    if n < 10: return "<10"
    if n < 50: return "10-50"
    if n < 500: return "50-500"
    return "500+"

def abbreviate(name: str) -> str:
    repl = [
        (r"\bSubmission Value\b", "SubVal"),
        (r"\bTest Code\b", "TestCd"),
        (r"\bTest Name\b", "TestNm"),
        (r"\bTest Method\b", "TestMth"),
        (r"\bResponse\b", "Resp"),
        (r"\bCategory\b", "Cat"),
        (r"\bSubcategory\b", "SubCat"),
        (r"\bAction Taken\b", "Action"),
        (r"\bQualifier\b", "Qlf"),
        (r"\bIdentifier\b", "ID"),
        (r"\bQuestionnaire\b", "Qnr"),
        (r"\bAssessment\b", "Assmt"),
        (r"\bRelationship\b", "Rel"),
        (r"\bDirectionality\b", "Dir"),
        (r"\bEvaluator\b", "Evl"),
    ]
    s = name
    for pat, r in repl: s = re.sub(pat, r, s)
    return s

def build_grouped() -> list[tuple[Path, str, list[dict]]]:
    out = []
    for f in iter_files():
        recs = parse_file(f)
        if recs: out.append((f, related_domain_for(f), recs))
    return out

# Common narrative header (same across variants for fair comparison)
NARR = [
    "<!-- generated by scripts/catalog_terminology.py (source mtime: 2026-04-13) -->",
    "<!-- 91 files -> 1005 codelists; Term values intentionally omitted -->",
    "",
    "# SDTM Controlled Terminology Map",
    "",
    "Index of 1,005 CDISC SDTM CT codelists. Data Type is always Char. For specific "
    "Term values look up the Source File under `knowledge_base/terminology/`.",
    "",
    "Columns: **CT**=codelist NCI code, **Name**=codelist name, **Ext**=extensible (Y/N), "
    "**Tm**=term count. Related Domain is in each section heading. Cross-domain = applies "
    "to many domains.",
    "",
    "Row format: `CT_CODE E|F TERMS NAME`  (E=extensible, F=fixed). Source file and "
    "Related Domain are in the enclosing `### ` heading.",
    "",
]
SUBDIR_TITLES = {
    "core": "## Core (terminology/core/) -- Related Domain varies per file",
    "questionnaires": "## Questionnaires (terminology/questionnaires/) -- all QS",
    "supplementary": "## Supplementary (terminology/supplementary/) -- Cross-domain",
}

def render(grouped, *, bucket=False, drop_domain=False, abbrev=False, flat=False) -> str:
    lines = list(NARR)
    if flat:
        # Single flat table, no section groups, pipe-delimited 5 cols: code|E/F|terms|name|src
        lines.append("| CT | X | Tm | Name | Src |")
        lines.append("|---|---|---|---|---|")
        for path, related, recs in grouped:
            src = path.name
            for rec in recs:
                ext_mark = "E" if rec["ext"] == "Y" else ("F" if rec["ext"] == "N" else "?")
                tstr = terms_str_bucket(rec["terms"]) if bucket else terms_str_current(rec["terms"])
                name = abbreviate(sanitize(rec["name"])) if abbrev else sanitize(rec["name"])
                lines.append(f"| {rec['code']} | {ext_mark} | {tstr} | {name} | {src} |")
        return "\n".join(lines) + "\n"

    last_subdir = None
    for path, related, recs in grouped:
        sd = path.parent.name
        if sd != last_subdir:
            lines.append(SUBDIR_TITLES.get(sd, f"## {sd}"))
            lines.append("")
            last_subdir = sd
        hd = f"### `{path.name}`" + ("" if drop_domain else f" -> {related}")
        lines.append(hd)
        for rec in recs:
            ext_mark = "E" if rec["ext"] == "Y" else ("F" if rec["ext"] == "N" else "?")
            tstr = terms_str_bucket(rec["terms"]) if bucket else terms_str_current(rec["terms"])
            name = abbreviate(sanitize(rec["name"])) if abbrev else sanitize(rec["name"])
            lines.append(f"{rec['code']} {ext_mark} {tstr} {name}")
        lines.append("")
    return "\n".join(lines) + "\n"

def main():
    # Read actual current output to confirm measurement matches user's 20,536 figure
    actual = CURRENT_OUT.read_text(encoding="utf-8")
    actual_tok = tok(actual)
    print(f"ACTUAL current output: {actual_tok} tokens ({len(actual)} chars, {len(actual.splitlines())} lines)")
    print()

    grouped = build_grouped()
    total_recs = sum(len(r) for _, _, r in grouped)
    print(f"Parsed {len(grouped)} files, {total_recs} codelist records")
    print()

    # Component breakdown on actual output
    import collections
    header_lines = []
    section_lines = []
    row_lines = []
    name_only_tokens = 0
    code_prefix_tokens = 0
    for line in actual.splitlines():
        if line.startswith("<!--") or line.startswith("# ") or line.startswith("## ") \
                or line.startswith("### ") or line.startswith("Columns:") \
                or line.startswith("Row format:") or line.startswith("Index of") \
                or not line.strip():
            if line.startswith("### "): section_lines.append(line)
            elif line.startswith("## "): section_lines.append(line)
            else: header_lines.append(line)
        elif re.match(r"^C\d+ [EF?] ", line):
            row_lines.append(line)
            m = re.match(r"^(C\d+ [EF?] \S+ )(.*)$", line)
            if m:
                code_prefix_tokens += tok(m.group(1))
                name_only_tokens += tok(m.group(2))
        else:
            header_lines.append(line)

    hdr_tok = tok("\n".join(header_lines))
    sec_tok = tok("\n".join(section_lines))
    row_tok = tok("\n".join(row_lines))
    print(f"Component breakdown (actual output):")
    print(f"  Header/narrative lines: {hdr_tok} tokens")
    print(f"  Section headings ({len(section_lines)}): {sec_tok} tokens")
    print(f"  Data rows ({len(row_lines)}): {row_tok} tokens")
    print(f"    - Code+mark+terms prefix sum: {code_prefix_tokens} tokens")
    print(f"    - Name strings sum:           {name_only_tokens} tokens")
    print()

    # Variant 0: rebuild baseline (sanity)
    base = render(grouped)
    base_tok = tok(base)
    print(f"V0 rebuild baseline:        {base_tok} tokens (delta vs actual: {base_tok-actual_tok:+d})")

    # Variant 1: N/A — Data Type column already dropped. Report hypothetical cost
    # of re-adding "Char" per row as baseline for the question.
    # (Can't "save" what isn't there; we report 0 savings and explain.)
    print(f"V1 drop Data Type column:   N/A (already dropped -- 'Data Type=Char' never emitted per row)")

    # Variant 2: bucketized terms
    v2 = render(grouped, bucket=True)
    v2_tok = tok(v2)
    print(f"V2 bucketize Terms:         {v2_tok} tokens (save {base_tok-v2_tok:+d})")

    # Variant 3: drop Related Domain from headings
    v3 = render(grouped, drop_domain=True)
    v3_tok = tok(v3)
    print(f"V3 drop Related Domain:     {v3_tok} tokens (save {base_tok-v3_tok:+d})")

    # Variant 4: abbreviate common words in Name
    v4 = render(grouped, abbrev=True)
    v4_tok = tok(v4)
    print(f"V4 abbreviate Name words:   {v4_tok} tokens (save {base_tok-v4_tok:+d})")

    # Variant 5: flat 5-col table (no per-file sections)
    v5 = render(grouped, flat=True, bucket=True)
    v5_tok = tok(v5)
    print(f"V5 flat 5-col table+bucket: {v5_tok} tokens (save {base_tok-v5_tok:+d})")

    # Combinations
    v2_4 = render(grouped, bucket=True, abbrev=True)
    v2_4_tok = tok(v2_4)
    print(f"V2+V4 combined:             {v2_4_tok} tokens (save {base_tok-v2_4_tok:+d})")

    v2_3 = render(grouped, bucket=True, drop_domain=True)
    v2_3_tok = tok(v2_3)
    print(f"V2+V3 combined:             {v2_3_tok} tokens (save {base_tok-v2_3_tok:+d})")

    v2_3_4 = render(grouped, bucket=True, drop_domain=True, abbrev=True)
    v2_3_4_tok = tok(v2_3_4)
    print(f"V2+V3+V4 combined:          {v2_3_4_tok} tokens (save {base_tok-v2_3_4_tok:+d})")

    # Measure pure floor: just "Cxxxxx NAME" with nothing else
    floor_lines = []
    for _, _, recs in grouped:
        for rec in recs:
            floor_lines.append(f"{rec['code']} {sanitize(rec['name'])}")
    floor_only = "\n".join(floor_lines) + "\n"
    floor_tok = tok(floor_only)
    print(f"\nAbsolute floor (code+name only, no Ext/Terms/headers): {floor_tok} tokens")

    # Name-only floor (pure NCI names, the "uncompressible" claim)
    names_only = "\n".join(sanitize(r["name"]) for _, _, recs in grouped for r in recs) + "\n"
    names_tok = tok(names_only)
    print(f"Names only (pure NCI names):                           {names_tok} tokens")

    # Codes only
    codes_only = "\n".join(r["code"] for _, _, recs in grouped for r in recs) + "\n"
    codes_tok = tok(codes_only)
    print(f"Codes only (1005 Cxxxxx):                              {codes_tok} tokens")

if __name__ == "__main__":
    main()
