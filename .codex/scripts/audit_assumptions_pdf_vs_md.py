#!/usr/bin/env python3
"""Audit Phase 3 assumptions markdown against source PDF ranges."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
from pathlib import Path
from typing import Dict, Iterable, List


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PAGE_INDEX = REPO_ROOT / ".work" / "page_index.json"
DEFAULT_PDF = REPO_ROOT / "source" / "SDTMIG v3.4 (no header footer).pdf"
DEFAULT_DOMAINS_ROOT = REPO_ROOT / "knowledge_base" / "domains"
DEFAULT_REPORT = REPO_ROOT / ".codex" / "reports" / "phase3-assumptions-validation.md"

TOP_LEVEL_NUMBER_RE = re.compile(r"(?m)(?:^\s*|(?<=\s))(\d+\.)\s+")
NESTED_ALPHA_RE = re.compile(r"(?m)^\s*([a-z]\.)\s+")
NESTED_ROMAN_RE = re.compile(r"(?m)^\s*((?:i|ii|iii|iv|v|vi|vii|viii|ix|x)\.)\s+", re.IGNORECASE)
ANCHOR_TOKEN_RE = re.compile(
    r"\b(?:[A-Z]{2,}[A-Z0-9]*|[A-Z]{1,2}[A-Z0-9]{2,}|[A-Z]{2,}\/[A-Z]{2,}|--[A-Z]+)\b"
)
ANCHOR_STOPWORDS = {
    "CDISC",
    "SDTM",
    "SDTMIG",
    "ISO",
    "CHAR",
    "NUM",
    "ROLE",
    "TYPE",
    "CORE",
    "EXP",
    "PERM",
    "REQ",
    "VARIABLE",
    "LABEL",
    "FORMAT",
    "CONTROLLED",
    "TERMS",
    "NOTES",
    "DESCRIPTION",
    "OVERVIEW",
    "SPECIFICATION",
    "ASSUMPTIONS",
    "EXAMPLES",
}


def normalize_text(text: str) -> str:
    normalized = text.replace("\u2013", "-").replace("\u2014", "-")
    normalized = normalized.replace("\u2018", "'").replace("\u2019", "'")
    normalized = normalized.replace("\u201c", '"').replace("\u201d", '"')
    normalized = re.sub(r"[ \t]+", " ", normalized)
    normalized = re.sub(r"\n{2,}", "\n", normalized)
    return normalized.strip()


def extract_assumptions_section(text: str, domain: str | None = None) -> str:
    source = text.replace("\f", "\n")
    start_patterns = []
    if domain:
        start_patterns.append(rf"{re.escape(domain)}\s*[–-]\s*Assumptions")
    start_patterns.extend(
        [
            r"(?m)^\s*Assumptions\s*$",
            r"(?m)^\s*1\.\s+",
        ]
    )

    start = 0
    for pattern in start_patterns:
        match = re.search(pattern, source, flags=re.IGNORECASE)
        if match:
            start = match.start()
            break

    tail = source[start:]
    end_patterns = []
    if domain:
        end_patterns.append(rf"{re.escape(domain)}\s*[–-]\s*Examples")
    end_patterns.extend(
        [
            r"(?m)^\s*Examples\s*$",
            r"(?m)^\s*Example\s+1\b",
            r"(?m)^\s*[A-Z0-9./ -]+Examples\s*$",
        ]
    )
    end = len(tail)
    for pattern in end_patterns:
        match = re.search(pattern, tail, flags=re.IGNORECASE)
        if match and match.start() > 0:
            end = min(end, match.start())
    return tail[:end].strip()


def extract_numbered_markers(text: str) -> List[str]:
    markers: List[str] = []
    markers.extend(TOP_LEVEL_NUMBER_RE.findall(text))
    markers.extend(NESTED_ALPHA_RE.findall(text))
    markers.extend(NESTED_ROMAN_RE.findall(text))
    return markers


def extract_anchor_tokens(text: str, domain: str | None = None) -> List[str]:
    tokens = {
        token.upper()
        for token in ANCHOR_TOKEN_RE.findall(text)
        if token.upper() not in ANCHOR_STOPWORDS and len(token) >= 4
    }
    return sorted(tokens)


def anchor_recall(expected_tokens: Iterable[str], observed_text: str) -> tuple[float, List[str]]:
    observed = set(extract_anchor_tokens(observed_text))
    expected = set(expected_tokens)
    missing = sorted(token for token in expected if token not in observed)
    recall = 1.0 if not expected else (len(expected) - len(missing)) / len(expected)
    return recall, missing


def analyze_assumptions_text(pdf_text: str, md_text: str, domain: str | None = None) -> dict:
    assumptions_pdf_text = extract_assumptions_section(pdf_text, domain=domain)
    assumptions_md_text = extract_assumptions_section(md_text, domain=domain)
    normalized_pdf = normalize_text(assumptions_pdf_text)
    normalized_md = normalize_text(assumptions_md_text)

    pdf_markers = extract_numbered_markers(assumptions_pdf_text)
    md_markers = extract_numbered_markers(assumptions_md_text)
    expected_tokens = extract_anchor_tokens(assumptions_pdf_text, domain=domain)
    recall, missing_tokens = anchor_recall(expected_tokens, assumptions_md_text)
    similarity = difflib.SequenceMatcher(None, normalized_pdf, normalized_md).ratio()

    return {
        "domain": domain,
        "pdf_numbered_count": len(pdf_markers),
        "md_numbered_count": len(md_markers),
        "pdf_nested_count": sum(1 for marker in pdf_markers if not marker[0].isdigit()),
        "md_nested_count": sum(1 for marker in md_markers if not marker[0].isdigit()),
        "anchor_token_count": len(expected_tokens),
        "anchor_recall": round(recall, 4),
        "missing_anchor_tokens": missing_tokens,
        "similarity": round(similarity, 4),
        "flags": build_assumptions_flags(
            len(pdf_markers),
            len(md_markers),
            recall,
            similarity,
        ),
    }


def build_assumptions_flags(
    pdf_numbered_count: int,
    md_numbered_count: int,
    recall: float,
    similarity: float,
) -> List[str]:
    flags: List[str] = []
    if md_numbered_count + 1 < pdf_numbered_count:
        flags.append("numbered-item loss suspected")
    if recall < 0.6:
        flags.append("anchor recall below threshold")
    if similarity < 0.35 and not (recall >= 0.95 and pdf_numbered_count <= 3):
        flags.append("low text similarity")
    return flags


def extract_pdf_pages(pdf_path: Path, start: int, end: int) -> str:
    cmd = ["pdftotext", "-f", str(start), "-l", str(end), "-layout", str(pdf_path), "-"]
    completed = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return completed.stdout


def audit_assumptions(page_index: Dict[str, dict], pdf_path: Path, domains_root: Path) -> dict:
    results: List[dict] = []
    flagged: List[dict] = []

    for domain, payload in sorted(page_index.get("domains", {}).items()):
        section_range = payload.get("section") or payload.get("assumptions")
        if not section_range:
            continue
        md_path = domains_root / domain / "assumptions.md"
        if not md_path.exists():
            flagged.append({"domain": domain, "flags": ["missing markdown file"]})
            continue

        pdf_text = extract_pdf_pages(pdf_path, section_range[0], section_range[1])
        md_text = md_path.read_text(encoding="utf-8")
        analysis = analyze_assumptions_text(pdf_text, md_text, domain=domain)
        analysis["pages"] = section_range
        results.append(analysis)
        if analysis["flags"]:
            flagged.append(analysis)

    return {
        "results": results,
        "flagged": flagged,
        "summary": {
            "domains_checked": len(results),
            "flagged_domains": len(flagged),
        },
    }


def write_report(result: dict, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Phase 3 Assumptions Validation",
        "",
        "## Summary",
        "",
        f"- Domains checked: {result['summary']['domains_checked']}",
        f"- Flagged domains: {result['summary']['flagged_domains']}",
        "",
        "## Flagged Domains",
        "",
    ]
    if result["flagged"]:
        for item in result["flagged"]:
            flags = ", ".join(item.get("flags", [])) or "none"
            lines.append(f"- {item['domain']}: {flags}")
    else:
        lines.append("- None")

    lines.extend(["", "## Per-Domain Metrics", ""])
    for item in result["results"]:
        lines.append(
            f"- {item['domain']}: numbered pdf/md={item['pdf_numbered_count']}/{item['md_numbered_count']}, "
            f"anchor_recall={item['anchor_recall']}, similarity={item['similarity']}"
        )

    lines.extend(["", "## Raw JSON", "", "```json", json.dumps(result, indent=2), "```", ""])
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-index", type=Path, default=DEFAULT_PAGE_INDEX)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--domains-root", type=Path, default=DEFAULT_DOMAINS_ROOT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    page_index = json.loads(args.page_index.read_text(encoding="utf-8"))
    result = audit_assumptions(page_index, args.pdf, args.domains_root)
    write_report(result, args.report)
    print(json.dumps(result["summary"], indent=2))
    return 1 if result["flagged"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
