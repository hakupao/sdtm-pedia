#!/usr/bin/env python3
"""Validate Phase 3 output inventory and shared-domain completeness."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PAGE_INDEX = REPO_ROOT / ".work" / "page_index.json"
DEFAULT_DOMAINS_ROOT = REPO_ROOT / "knowledge_base" / "domains"
DEFAULT_REPORT = REPO_ROOT / ".codex" / "reports" / "phase3-inventory-validation.md"
SHARED_EXAMPLE_PAIRS: Tuple[Tuple[str, str], ...] = (
    ("EX", "EC"),
    ("MB", "MS"),
    ("PC", "PP"),
    ("TU", "TR"),
)


def load_page_index(path: Path) -> Dict[str, dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def file_size(path: Path) -> int:
    return path.stat().st_size if path.exists() else 0


def audit_inventory(
    page_index: Dict[str, dict],
    domains_root: Path,
    min_size_bytes: int = 32,
    shared_pairs: Iterable[Tuple[str, str]] = SHARED_EXAMPLE_PAIRS,
) -> dict:
    domains = sorted(page_index.get("domains", {}).keys())
    errors: List[str] = []
    warnings: List[str] = []
    completed = 0

    for domain in domains:
        domain_dir = domains_root / domain
        assumptions_path = domain_dir / "assumptions.md"
        examples_path = domain_dir / "examples.md"
        present = True

        for path in (assumptions_path, examples_path):
            if not path.exists():
                errors.append(f"{domain}: missing {path.name}")
                present = False
                continue
            size = file_size(path)
            if size == 0:
                errors.append(f"{domain}: empty file {path.relative_to(domains_root.parent)}")
            elif size < min_size_bytes:
                warnings.append(
                    f"{domain}: suspiciously small file {path.relative_to(domains_root.parent)} ({size} bytes)"
                )

        if present and assumptions_path.exists() and examples_path.exists():
            completed += 1

    for left, right in shared_pairs:
        left_examples = domains_root / left / "examples.md"
        right_examples = domains_root / right / "examples.md"
        if left_examples.exists() != right_examples.exists():
            errors.append(f"shared pair mismatch: {left}/{right} examples presence differs")

    return {
        "errors": errors,
        "warnings": warnings,
        "summary": {
            "domain_count": len(domains),
            "completed_domains": completed,
            "missing_or_incomplete_domains": len(domains) - completed,
            "shared_pairs_checked": len(tuple(shared_pairs)),
        },
    }


def write_report(result: dict, report_path: Path) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Phase 3 Inventory Validation",
        "",
        "## Summary",
        "",
        f"- Domains expected: {result['summary']['domain_count']}",
        f"- Domains complete: {result['summary']['completed_domains']}",
        f"- Domains incomplete: {result['summary']['missing_or_incomplete_domains']}",
        f"- Shared pairs checked: {result['summary']['shared_pairs_checked']}",
        f"- Errors: {len(result['errors'])}",
        f"- Warnings: {len(result['warnings'])}",
        "",
        "## Errors",
        "",
    ]
    lines.extend([f"- {item}" for item in result["errors"]] or ["- None"])
    lines.extend(["", "## Warnings", ""])
    lines.extend([f"- {item}" for item in result["warnings"]] or ["- None"])
    lines.extend(["", "## Raw JSON", "", "```json", json.dumps(result, indent=2), "```", ""])
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--page-index", type=Path, default=DEFAULT_PAGE_INDEX)
    parser.add_argument("--domains-root", type=Path, default=DEFAULT_DOMAINS_ROOT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--min-size-bytes", type=int, default=32)
    args = parser.parse_args()

    result = audit_inventory(
        load_page_index(args.page_index),
        args.domains_root,
        min_size_bytes=args.min_size_bytes,
    )
    write_report(result, args.report)
    print(json.dumps(result["summary"], indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
