"""ConfigurationReport (Viedoc 导出 xlsx) 确定性解析器. 零 LLM."""
from __future__ import annotations

from typing import Any


def _cell(v: Any) -> str:
    return "" if v is None else str(v).strip()


def read_sheet_records(ws) -> list[dict[str, Any]]:
    """三行表头 (sheet名/分组/列名) → [{'分组::列名': str, '_row': int}]; 全空行跳过."""
    rows = ws.iter_rows(values_only=True)
    next(rows)                                   # 行1: sheet 名, 丢弃
    sections_raw = next(rows)
    colnames = next(rows)
    keys: list[str] = []
    cur = ""
    for s, c in zip(sections_raw, colnames):
        if _cell(s):
            cur = _cell(s)
        keys.append(f"{cur}::{_cell(c)}")
    records: list[dict[str, Any]] = []
    for i, row in enumerate(rows, start=4):
        values = [_cell(v) for v in row[: len(keys)]]
        if not any(values):
            continue
        rec: dict[str, Any] = dict(zip(keys, values))
        rec["_row"] = i
        records.append(rec)
    return records
