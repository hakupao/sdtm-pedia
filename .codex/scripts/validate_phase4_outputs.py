#!/usr/bin/env python3
"""Validate Phase 4 model/chapter outputs and spot-check source anchors."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Dict, List


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PAGE_INDEX = REPO_ROOT / ".work" / "page_index.json"
DEFAULT_SDTMIG_PDF = REPO_ROOT / "source" / "SDTMIG v3.4 (no header footer).pdf"
DEFAULT_SDTM_PDF = REPO_ROOT / "source" / "SDTM_v2.0.pdf"
DEFAULT_REPORT = REPO_ROOT / ".codex" / "reports" / "phase4-validation.md"

PHASE4_CONFIG = {
    "chapters": {
        "directory": REPO_ROOT / "knowledge_base" / "chapters",
        "pdf": DEFAULT_SDTMIG_PDF,
        "anchors": {
            "ch01_introduction": ["Purpose", "Organization of this Document"],
            "ch02_fundamentals": ["Observations and Variables", "General Observation Classes"],
            "ch03_submitting_data": ["Dataset-level Metadata", "Primary Keys"],
            "ch04_general_assumptions": ["Splitting Domains", "SDTM Core Designations"],
            "ch08_relationships": ["RELREC", "Supplemental Qualifiers"],
            "ch10_appendices": ["Glossary", "Controlled Terminology"],
        },
    },
    "model": {
        "directory": REPO_ROOT / "knowledge_base" / "model",
        "pdf": DEFAULT_SDTM_PDF,
        "anchors": {
            "concepts_and_terms": ["Model Concepts and Terms", "Table Structure"],
            "observation_classes": ["Interventions Observation Class", "Events Observation Class"],
            "special_purpose_domains": ["Demographics", "Comments"],
            "associated_persons": ["Associated Persons", "APID"],
            "study_level_data": ["Trial Design Model", "Trial Arms"],
            "relationship_datasets": ["Related Records", "Supplemental Qualifiers"],
        },
    },
}


def normalize_text(text: str) -> str:
    normalized = text.lower()
    normalized = normalized.replace("\u2013", "-").replace("\u2014", "-")
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.strip()


def contains_all_anchors(text: str, anchors: List[str]) -> bool:
    haystack = normalize_text(text)
    return all(normalize_text(anchor) in haystack for anchor in anchors)


def extract_pdf_pages(pdf_path: Path, start: int, end: int) -> str:
    completed = subprocess.run(
        ["pdftotext", "-f", str(start), "-l", str(end), "-layout", str(pdf_path), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def validate_phase4_outputs(page_index: Dict[str, dict]) -> dict:
    errors: List[str] = []
    warnings: List[str] = []
    checked_files: List[dict] = []

    for section_name, config in PHASE4_CONFIG.items():
        entries = (
            page_index.get("chapters", {})
            if section_name == "chapters"
            else page_index.get("model", {}).get("files", {})
        )
        for stem, payload in sorted(entries.items()):
            md_path = config["directory"] / f"{stem}.md"
            pages = payload["pages"]
            anchors = config["anchors"].get(stem, [])
            if not md_path.exists():
                errors.append(f"{section_name}.{stem}: missing markdown file")
                continue
            md_text = md_path.read_text(encoding="utf-8")
            if len(md_text.strip()) < 200:
                warnings.append(f"{section_name}.{stem}: markdown file is unusually small")

            pdf_text = extract_pdf_pages(config["pdf"], pages[0], pages[1])
            matched = contains_all_anchors(pdf_text, anchors) if anchors else True
            if not matched:
                warnings.append(f"{section_name}.{stem}: one or more source anchors not found in pdf range")

            checked_files.append(
                {
                    "section": section_name,
                    "file": stem,
                    "pages": pages,
                    "anchors": anchors,
                    "anchor_match": matched,
                    "line_count": len(md_text.splitlines()),
                }
            )

    return {
        "errors": errors,
        "warnings": warnings,
        "checked_files": checked_files,
        "summary": {
            "files_checked": len(checked_files),
            "errors": len(errors),
            "warnings": len(warnings),
        },
    }


def write_report(result: dict, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Phase 4 Validation",
        "",
        "## Summary",
        "",
        f"- Files checked: {result['summary']['files_checked']}",
        f"- Errors: {result['summary']['errors']}",
        f"- Warnings: {result['summary']['warnings']}",
        "",
        "## Errors",
        "",
    ]
    lines.extend([f"- {item}" for item in result["errors"]] or ["- None"])
    lines.extend(["", "## Warnings", ""])
    lines.extend([f"- {item}" for item in result["warnings"]] or ["- None"])
    lines.extend(["", "## File Checks", ""])
    for item in result["checked_files"]:
        lines.append(
            f"- {item['section']}/{item['file']}.md: pages={item['pages']}, "
            f"anchor_match={item['anchor_match']}, lines={item['line_count']}"
        )
    lines.extend(["", "## Raw JSON", "", "```json", json.dumps(result, indent=2), "```", ""])
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-index", type=Path, default=DEFAULT_PAGE_INDEX)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    page_index = json.loads(args.page_index.read_text(encoding="utf-8"))
    result = validate_phase4_outputs(page_index)
    write_report(result, args.report)
    print(json.dumps(result["summary"], indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
