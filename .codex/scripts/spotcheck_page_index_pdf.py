#!/usr/bin/env python3
"""Spot-check page_index.json against PDF anchor text."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Dict, List


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PAGE_INDEX = REPO_ROOT / ".work" / "page_index.json"
DEFAULT_PDF = REPO_ROOT / "source" / "SDTMIG v3.4 (no header footer).pdf"
DEFAULT_REPORT = REPO_ROOT / ".codex" / "reports" / "phase2-page-index-spotcheck.md"
DEFAULT_DOMAINS = ["DM", "AE", "EX", "EC", "MB", "MS", "PC", "PP", "TU", "TR"]


def normalize_text(text: str) -> str:
    normalized = text.lower()
    normalized = normalized.replace("\u2013", "-").replace("\u2014", "-")
    normalized = normalized.replace("\u2018", "'").replace("\u2019", "'")
    normalized = normalized.replace("\u201c", '"').replace("\u201d", '"')
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.strip()


def contains_anchor(text: str, anchors: List[str]) -> bool:
    haystack = normalize_text(text)
    return all(normalize_text(anchor) in haystack for anchor in anchors)


def build_domain_checks(page_index: Dict[str, dict], domains: List[str]) -> List[dict]:
    checks = []
    for domain in domains:
        payload = page_index["domains"].get(domain)
        if not payload:
            continue
        checks.append(
            {
                "domain": domain,
                "kind": "assumptions",
                "page": payload["assumptions"][0],
                "anchors": [domain, "Assumptions"],
            }
        )
        checks.append(
            {
                "domain": domain,
                "kind": "examples",
                "page": payload["examples"][0],
                "anchors": ["Example"],
            }
        )
    return checks


def extract_page_text(pdf_path: Path, page: int) -> str:
    cmd = ["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(pdf_path), "-"]
    completed = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return completed.stdout


def evaluate_checks(pdf_path: Path, checks: List[dict]) -> dict:
    results = []
    failures = []
    for check in checks:
        text = extract_page_text(pdf_path, check["page"])
        matched = contains_anchor(text, check["anchors"])
        item = {
            "domain": check["domain"],
            "kind": check["kind"],
            "page": check["page"],
            "anchors": check["anchors"],
            "matched": matched,
        }
        results.append(item)
        if not matched:
            failures.append(item)
    return {"results": results, "failures": failures}


def write_report(result: dict, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Phase 2 Page Index PDF Spotcheck",
        "",
        "## Summary",
        "",
        f"- Checks run: {len(result['results'])}",
        f"- Failed checks: {len(result['failures'])}",
        "",
        "## Detailed Results",
        "",
    ]
    for item in result["results"]:
        status = "PASS" if item["matched"] else "FAIL"
        lines.append(
            f"- {status}: {item['domain']} {item['kind']} page {item['page']} anchors={item['anchors']}"
        )

    lines.extend(["", "## Raw JSON", "", "```json", json.dumps(result, indent=2), "```", ""])
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-index", type=Path, default=DEFAULT_PAGE_INDEX)
    parser.add_argument("--pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--domains", nargs="*", default=DEFAULT_DOMAINS)
    args = parser.parse_args()

    page_index = json.loads(args.page_index.read_text(encoding="utf-8"))
    checks = build_domain_checks(page_index, args.domains)
    result = evaluate_checks(args.pdf, checks)
    write_report(result, args.report)
    print(f"PDF spotcheck report written to {args.report}")
    print(json.dumps({"checks": len(result["results"]), "failures": len(result["failures"])}, indent=2))
    return 1 if result["failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
