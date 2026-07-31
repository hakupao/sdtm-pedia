"""ConfigurationReport (Viedoc 导出 xlsx) 确定性解析器. 零 LLM."""
from __future__ import annotations

from typing import Any


def _cell(v: Any) -> str:
    return "" if v is None else str(v).strip()


def read_sheet_records(ws, *, has_section_row: bool = True) -> list[dict[str, Any]]:
    """表头 → [{'分组::列名': str, '_row': int}]; 全空行跳过, 短行补空串.

    has_section_row=True:  三行表头 (行1 sheet名 / 行2 分组, 空白前向填充 / 行3 列名), 数据自行 4 起.
    has_section_row=False: 两行表头 (行1 sheet名 / 行2 列名), 分组名取 sheet 名, 数据自行 3 起.
                           真实 Code lists sheet 即此形态.
    """
    rows = ws.iter_rows(values_only=True)
    next(rows)                                   # 行1: sheet 名, 丢弃
    sections_raw: tuple = next(rows) if has_section_row else ()
    colnames = next(rows)
    keys: list[str] = []
    cur = "" if has_section_row else ws.title
    for i, c in enumerate(colnames):
        section = _cell(sections_raw[i]) if i < len(sections_raw) else ""
        if section:
            cur = section
        keys.append(f"{cur}::{_cell(c)}")
    first_data_row = 4 if has_section_row else 3
    records: list[dict[str, Any]] = []
    for i, row in enumerate(rows, start=first_data_row):
        values = [_cell(v) for v in row[: len(keys)]]
        values += [""] * (len(keys) - len(values))   # 短行补齐, 否则 zip 静默丢 key
        if not any(values):
            continue
        rec: dict[str, Any] = dict(zip(keys, values))
        rec["_row"] = i
        records.append(rec)
    return records
