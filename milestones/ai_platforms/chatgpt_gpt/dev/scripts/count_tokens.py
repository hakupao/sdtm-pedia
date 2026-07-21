#!/usr/bin/env python3
"""Token counter for SDTM Phase 6.5 ChatGPT GPTs stage verification.

Counts tokens in Markdown files using tiktoken's cl100k_base encoding,
aligned with the Claude v1/v2 惯例 (see claude_projects/archive/v1/scripts/
count_tokens.py). Reused verbatim for ChatGPT GPTs so batch 1/批 2 合并产物
the token numbers align with PLAN.md §2.4 estimates.

依据:
- PLAN.md §2.5 (脚本职责: count_tokens.py 测 token)
- PLAN.md §1.1 P1 量化 PASS: 每 Step 打印 `<file>: <N> tokens`

Phase: 3 (执行) · Node: 1 (仅写脚本, 不执行)

Usage:
    python3 count_tokens.py <path> [<path> ...] [--total-only]

- <path> as a file: prints "<file>: <N> tokens"
- <path> as a directory: recursively counts all .md files
- Multiple paths are combined into a single TOTAL
- --total-only suppresses per-file lines and prints only "TOTAL: <N>"

Read-only (P5): never modifies source files.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable

import tiktoken

ENCODING_NAME = "cl100k_base"


def iter_md_files(path: Path) -> Iterable[Path]:
    """Yield .md files under path (recursively) or the file itself."""
    if path.is_file():
        yield path
        return
    if path.is_dir():
        for md in sorted(path.rglob("*.md")):
            if md.is_file():
                yield md
        return
    print(f"error: path not found: {path}", file=sys.stderr)
    sys.exit(2)


def count_tokens(encoder: "tiktoken.Encoding", file_path: Path) -> int:
    text = file_path.read_text(encoding="utf-8", errors="strict")
    return len(encoder.encode(text))


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Count tokens in Markdown files using tiktoken cl100k_base."
    )
    parser.add_argument("paths", nargs="+", help="file(s) or directory(ies) to scan")
    parser.add_argument(
        "--total-only",
        action="store_true",
        help="print only the combined TOTAL line",
    )
    args = parser.parse_args(argv)

    encoder = tiktoken.get_encoding(ENCODING_NAME)

    total = 0
    file_count = 0
    for raw in args.paths:
        root = Path(raw)
        for md in iter_md_files(root):
            n = count_tokens(encoder, md)
            total += n
            file_count += 1
            if not args.total_only:
                print(f"{md}: {n} tokens")

    if args.total_only:
        print(f"TOTAL: {total}")
    elif file_count != 1:
        print(f"TOTAL: {total} tokens")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
