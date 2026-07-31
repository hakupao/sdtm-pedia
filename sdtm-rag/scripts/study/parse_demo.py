"""DEMO 导出 xlsx → item 实例值采样 (去重保序, 空值跳过). 零 LLM."""
from __future__ import annotations

from pathlib import Path

import openpyxl

_SKIP_SHEETS = {"README", "Items", "CodeLists"}


def sample_demo_values(
    demo_path: Path, known_item_oids: set[str], max_per_item: int = 5,
) -> tuple[dict[str, list[str]], list[str]]:
    wb = openpyxl.load_workbook(demo_path, read_only=True)
    samples: dict[str, list[str]] = {}
    unmatched: list[str] = []
    for ws in wb.worksheets:
        if ws.title in _SKIP_SHEETS:
            continue
        rows = ws.iter_rows(values_only=True)
        header = [str(c) if c is not None else "" for c in next(rows, [])]
        col_oids: list[str | None] = []
        for name in header:
            if name in known_item_oids:
                col_oids.append(name)
            else:
                if name:
                    unmatched.append(name)
                col_oids.append(None)
        for row in rows:
            for oid, v in zip(col_oids, row):
                if oid is None or v is None or str(v).strip() == "":
                    continue
                bucket = samples.setdefault(oid, [])
                sv = str(v).strip()
                if sv not in bucket and len(bucket) < max_per_item:
                    bucket.append(sv)
    return samples, sorted(set(unmatched))
