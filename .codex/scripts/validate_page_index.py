#!/usr/bin/env python3
"""Validate Phase 2 page_index.json structure and range logic."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PAGE_INDEX = REPO_ROOT / ".work" / "page_index.json"
DEFAULT_REPORT = REPO_ROOT / ".codex" / "reports" / "phase2-page-index-validation.md"


def is_range(value) -> bool:
    return (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(item, int) for item in value)
    )


def validate_range(name: str, value, total_pages: int) -> List[str]:
    if not is_range(value):
        return [f"{name}: invalid range format: {value!r}"]
    start, end = value
    errors = []
    if start < 1 or end < 1 or start > total_pages or end > total_pages:
        errors.append(f"{name}: page out of bounds: {value!r}")
    if start > end:
        errors.append(f"{name}: invalid range order: {value!r}")
    return errors


def validate_page_index_data(data: Dict[str, dict]) -> dict:
    errors: List[str] = []
    warnings: List[str] = []

    for top_key in ("_meta", "chapters", "shared_specs", "domains", "model"):
        if top_key not in data:
            errors.append(f"missing top-level key: {top_key}")

    meta = data.get("_meta", {})
    total_pages = int(meta.get("total_pages", 0) or 0)
    if total_pages <= 0:
        errors.append("_meta.total_pages must be a positive integer")

    for chapter_name, payload in data.get("chapters", {}).items():
        pages = payload.get("pages")
        errors.extend(validate_range(f"chapters.{chapter_name}.pages", pages, total_pages))

    for shared_name, payload in data.get("shared_specs", {}).items():
        pages = payload.get("pages")
        errors.extend(validate_range(f"shared_specs.{shared_name}.pages", pages, total_pages))

    model = data.get("model", {})
    if not isinstance(model.get("files", {}), dict):
        errors.append("model.files must be a mapping")
    for file_name, payload in model.get("files", {}).items():
        pages = payload.get("pages")
        errors.extend(validate_range(f"model.files.{file_name}.pages", pages, total_pages))

    for domain, payload in data.get("domains", {}).items():
        if not isinstance(payload, dict):
            errors.append(f"domains.{domain}: expected object")
            continue
        for key in ("section", "spec", "assumptions", "examples"):
            if key not in payload:
                errors.append(f"domains.{domain}: missing key {key}")
                continue
            if payload[key] is None and key == "spec":
                continue
            errors.extend(validate_range(f"domains.{domain}.{key}", payload[key], total_pages))

        if all(key in payload and is_range(payload[key]) for key in ("spec", "assumptions", "examples")):
            spec = payload["spec"]
            assumptions = payload["assumptions"]
            examples = payload["examples"]
            if spec[0] > assumptions[0]:
                errors.append(f"domains.{domain}: spec starts after assumptions")
            note = str(payload.get("note", "")).lower()
            shared_examples = "share" in note or "shared" in note or "embedded" in note
            if assumptions[0] > examples[0] and not shared_examples:
                errors.append(f"domains.{domain}: assumptions start after examples")
            if spec[1] > examples[1] and examples[0] >= assumptions[0]:
                warnings.append(f"domains.{domain}: spec extends beyond examples end")

    return {
        "errors": errors,
        "warnings": warnings,
        "summary": {
            "domains": len(data.get("domains", {})),
            "chapters": len(data.get("chapters", {})),
            "shared_specs": len(data.get("shared_specs", {})),
            "model_files": len(model.get("files", {})) if isinstance(model.get("files", {}), dict) else 0,
        },
    }


def write_report(result: dict, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Phase 2 Page Index Validation",
        "",
        "## Summary",
        "",
        f"- Domains indexed: {result['summary']['domains']}",
        f"- Chapters indexed: {result['summary']['chapters']}",
        f"- Shared specs indexed: {result['summary']['shared_specs']}",
        f"- Model files indexed: {result['summary']['model_files']}",
        f"- Errors: {len(result['errors'])}",
        f"- Warnings: {len(result['warnings'])}",
        "",
        "## Errors",
        "",
    ]
    if result["errors"]:
        lines.extend([f"- {item}" for item in result["errors"]])
    else:
        lines.append("- None")

    lines.extend(["", "## Warnings", ""])
    if result["warnings"]:
        lines.extend([f"- {item}" for item in result["warnings"]])
    else:
        lines.append("- None")

    lines.extend(["", "## Raw JSON", "", "```json", json.dumps(result, indent=2), "```", ""])
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-index", type=Path, default=DEFAULT_PAGE_INDEX)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    data = json.loads(args.page_index.read_text(encoding="utf-8"))
    result = validate_page_index_data(data)
    write_report(result, args.report)
    print(f"Page index validation report written to {args.report}")
    print(json.dumps(result["summary"], indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
