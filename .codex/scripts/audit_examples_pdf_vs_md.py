#!/usr/bin/env python3
"""Audit Phase 3 examples markdown against source PDF ranges."""

from __future__ import annotations

import argparse
import difflib
import json
import re
import subprocess
from pathlib import Path
from typing import Dict, List


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PAGE_INDEX = REPO_ROOT / ".work" / "page_index.json"
DEFAULT_PDF = REPO_ROOT / "source" / "SDTMIG v3.4 (no header footer).pdf"
DEFAULT_DOMAINS_ROOT = REPO_ROOT / "knowledge_base" / "domains"
DEFAULT_REPORT = REPO_ROOT / ".codex" / "reports" / "phase3-examples-validation.md"

EXAMPLE_HEADING_RE = re.compile(r"(?m)^#{2,3}\s+(Example [^\n]+)$")
DATASET_NAME_RE = re.compile(r"\*\*[^*\n]*?([A-Za-z0-9_-]+\.xpt)[^*\n]*\*\*")
UPPER_TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9/_-]{1,}\b")
DATE_TOKEN_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2})?\b")
PDF_EXAMPLE_HEADING_RE = re.compile(r"(?m)^\s*Example\s+\d+\b")
HEADER_TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]{2,}\b")
TOKEN_STOPWORDS = {"ROW", "ROWS", "EXAMPLE", "DOMAIN", "NOTE", "NOTES"}


def normalize_text(text: str) -> str:
    normalized = text.replace("\u2013", "-").replace("\u2014", "-")
    normalized = normalized.replace("\u2018", "'").replace("\u2019", "'")
    normalized = normalized.replace("\u201c", '"').replace("\u201d", '"')
    normalized = re.sub(r"[ \t]+", " ", normalized)
    normalized = re.sub(r"\n{2,}", "\n", normalized)
    return normalized.strip()


def extract_examples_section(text: str, domain: str | None = None) -> str:
    source = text.replace("\f", "\n")
    start_patterns = []
    if domain:
        start_patterns.append(rf"{re.escape(domain)}\s*[–-]\s*Examples")
    start_patterns.extend(
        [
            r"(?m)^\s*Examples\s*$",
            r"(?m)^\s*Example\s+1\b",
            r"(?m)^\s*Example\s+\d+\b",
        ]
    )

    start = 0
    for pattern in start_patterns:
        match = re.search(pattern, source, flags=re.IGNORECASE)
        if match:
            start = match.start()
            break
    return source[start:].strip()


def extract_example_headings(text: str) -> List[str]:
    return EXAMPLE_HEADING_RE.findall(text)


def extract_dataset_names(text: str) -> List[str]:
    seen = []
    for name in DATASET_NAME_RE.findall(text):
        if name not in seen:
            seen.append(name)
    return seen


def extract_pdf_dataset_names(text: str) -> List[str]:
    seen = []
    for name in re.findall(r"\b([A-Za-z0-9_-]+\.xpt)\b", text):
        lower = name.lower()
        if lower not in seen:
            seen.append(lower)
    return seen


def split_markdown_row(line: str) -> List[str]:
    line = line.strip().strip("|")
    return [cell.strip() for cell in line.split("|")]


def parse_markdown_tables(text: str) -> List[dict]:
    tables: List[dict] = []
    current_dataset: str | None = None
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        dataset_match = DATASET_NAME_RE.search(line)
        if dataset_match:
            current_dataset = dataset_match.group(1)
            i += 1
            continue

        if (
            current_dataset
            and line.startswith("|")
            and i + 1 < len(lines)
            and lines[i + 1].lstrip().startswith("|-")
        ):
            headers = split_markdown_row(line)
            row_count = 0
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                row_count += 1
                j += 1
            tables.append(
                {
                    "dataset_name": current_dataset,
                    "headers": headers,
                    "row_count": row_count,
                }
            )
            i = j
            continue
        i += 1
    return tables


def extract_key_tokens(text: str) -> List[str]:
    tokens = {
        token.upper()
        for token in UPPER_TOKEN_RE.findall(text)
        if token.upper() not in TOKEN_STOPWORDS
    }
    tokens.update(DATE_TOKEN_RE.findall(text))
    return sorted(tokens)


def extract_header_tokens(headers: List[str]) -> List[str]:
    tokens = []
    for header in headers:
        for token in HEADER_TOKEN_RE.findall(header.upper()):
            if token not in TOKEN_STOPWORDS:
                tokens.append(token)
    return sorted(set(tokens))


def build_markdown_example_signature(text: str) -> dict:
    content = extract_examples_section(text)
    tables = parse_markdown_tables(content)
    return {
        "example_count": len(extract_example_headings(content)),
        "dataset_names": extract_dataset_names(content),
        "tables": tables,
        "key_tokens": extract_key_tokens(content),
    }


def build_pdf_example_signature(text: str) -> dict:
    content = extract_examples_section(text)
    return {
        "example_count": len(PDF_EXAMPLE_HEADING_RE.findall(content)),
        "dataset_names": extract_pdf_dataset_names(content),
        "key_tokens": extract_key_tokens(content),
    }


def compare_examples_text(pdf_text: str, md_text: str, domain: str | None = None) -> dict:
    pdf_sig = build_pdf_example_signature(pdf_text)
    md_sig = build_markdown_example_signature(md_text)
    md_dataset_lc = {name.lower() for name in md_sig["dataset_names"]}
    missing_dataset_names = [name for name in pdf_sig["dataset_names"] if name.lower() not in md_dataset_lc]
    primary_dataset_names = [f"{domain.lower()}.xpt"] if domain else []
    missing_primary_dataset_names = [
        name for name in primary_dataset_names if name.lower() not in md_dataset_lc and name.lower() in pdf_sig["dataset_names"]
    ]

    missing_headers: List[str] = []
    normalized_pdf = normalize_text(extract_examples_section(pdf_text, domain=domain))
    pdf_token_set = set(pdf_sig["key_tokens"])
    for table in md_sig["tables"]:
        header_tokens = extract_header_tokens(table["headers"])
        missing_for_table = [token for token in header_tokens if token not in pdf_token_set]
        if header_tokens and len(missing_for_table) >= max(2, len(header_tokens) // 3):
            missing_headers.extend(missing_for_table)

    token_set = set(md_sig["key_tokens"])
    expected_tokens = set(pdf_sig["key_tokens"])
    missing_tokens = sorted(token for token in expected_tokens if token not in token_set)
    token_recall = 1.0 if not expected_tokens else (len(expected_tokens) - len(missing_tokens)) / len(expected_tokens)
    similarity = difflib.SequenceMatcher(
        None,
        normalized_pdf,
        normalize_text(extract_examples_section(md_text, domain=domain)),
    ).ratio()

    shared_continuation_mode = "continued from" in md_text.lower()

    flags: List[str] = []
    no_examples_note = "does not include specific dataset examples" in md_text.lower()
    if not no_examples_note and md_sig["example_count"] == 0 and pdf_sig["example_count"] > 0:
        flags.append("missing example headings")
    if missing_primary_dataset_names and not shared_continuation_mode and not no_examples_note:
        flags.append("missing dataset blocks")
    if token_recall < 0.35:
        flags.append("low key-token recall")
    if similarity < 0.2 and token_recall < 0.6:
        flags.append("low text similarity")

    return {
        "domain": domain,
        "pdf_example_count": pdf_sig["example_count"],
        "md_example_count": md_sig["example_count"],
        "dataset_names": md_sig["dataset_names"],
        "missing_dataset_names": missing_dataset_names,
        "missing_primary_dataset_names": missing_primary_dataset_names,
        "missing_headers": sorted(set(missing_headers)),
        "token_recall": round(token_recall, 4),
        "missing_key_tokens": missing_tokens[:50],
        "similarity": round(similarity, 4),
        "flags": flags,
    }


def extract_pdf_pages(pdf_path: Path, start: int, end: int) -> str:
    cmd = ["pdftotext", "-f", str(start), "-l", str(end), "-layout", str(pdf_path), "-"]
    completed = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return completed.stdout


def audit_examples(page_index: Dict[str, dict], pdf_path: Path, domains_root: Path) -> dict:
    results: List[dict] = []
    flagged: List[dict] = []

    for domain, payload in sorted(page_index.get("domains", {}).items()):
        section_range = payload.get("section")
        examples_range = payload.get("examples")
        if not section_range and not examples_range:
            continue
        if section_range and examples_range:
            page_span = [section_range[0], max(section_range[1], examples_range[1])]
        else:
            page_span = section_range or examples_range
        md_path = domains_root / domain / "examples.md"
        if not md_path.exists():
            flagged.append({"domain": domain, "flags": ["missing markdown file"]})
            continue

        pdf_text = extract_pdf_pages(pdf_path, page_span[0], page_span[1])
        md_text = md_path.read_text(encoding="utf-8")
        analysis = compare_examples_text(pdf_text, md_text, domain=domain)
        analysis["pages"] = page_span
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
        "# Phase 3 Examples Validation",
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
            lines.append(f"- {item['domain']}: {', '.join(item.get('flags', []))}")
    else:
        lines.append("- None")

    lines.extend(["", "## Per-Domain Metrics", ""])
    for item in result["results"]:
        lines.append(
            f"- {item['domain']}: examples pdf/md={item['pdf_example_count']}/{item['md_example_count']}, "
            f"datasets={len(item['dataset_names'])}, token_recall={item['token_recall']}, similarity={item['similarity']}"
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
    result = audit_examples(page_index, args.pdf, args.domains_root)
    write_report(result, args.report)
    print(json.dumps(result["summary"], indent=2))
    return 1 if result["flagged"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
