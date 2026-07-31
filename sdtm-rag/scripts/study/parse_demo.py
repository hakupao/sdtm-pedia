"""DEMO 导出 xlsx → item 实例值采样 (去重保序, 空值跳过). 零 LLM, 零模糊匹配.

真实 DEMO 结构 (Task 6 侦察): sheet 名 = form OID (21/21 吻合), form sheet 首行为列头,
但**列头是日文 label 而非 Item OID** (直配命中率仅 1%). 故按三路合并解析, 全程限定在
sheet 名给出的 form 作用域内, 并要求候选唯一 —— 多候选一律跳过, 不猜.
"""
from __future__ import annotations

import collections
from pathlib import Path
from typing import Any

import openpyxl

_SKIP_SHEETS = {"README", "Items", "CodeLists"}
_ITEMS_SHEET = "Items"


def _cell(v: Any) -> str:
    return "" if v is None else str(v).strip()


def _load_items_dict(wb) -> dict[str, set[str]]:
    """DEMO 自带的 Items 字典 sheet (单行表头 ID/Label/...) → label → {ID}."""
    if _ITEMS_SHEET not in wb.sheetnames:
        return {}
    rows = wb[_ITEMS_SHEET].iter_rows(values_only=True)
    header = [_cell(c) for c in next(rows, [])]
    try:
        i_id, i_label = header.index("ID"), header.index("Label")
    except ValueError:
        return {}
    out: dict[str, set[str]] = collections.defaultdict(set)
    for row in rows:
        oid = _cell(row[i_id]) if i_id < len(row) else ""
        label = _cell(row[i_label]) if i_label < len(row) else ""
        if oid and label:
            out[label].add(oid)
    return out


def sample_demo_values(
    demo_path: Path, catalog_items: list[dict], max_per_item: int = 5,
) -> tuple[dict[str, list[str]], dict]:
    """DEMO 各 form sheet 采样实例值.

    catalog_items: catalog.json 的 items (用 item_oid / form_oid / label 三键).
    列头解析顺序 (均限定在 sheet 名对应的 form 作用域内, 先命中先定):
      (a) 列头 == item_oid 直配; (b) DEMO Items 字典 Label→ID; (c) form 域内 label 精确匹配.
    某路给出恰 1 个候选即解析; >1 记 ambiguous 并跳过该列; 三路皆 0 记 unmatched.
    返回 (item_oid → 去重实例值列表, resolution stats).
    """
    scope_by_form: dict[str, set[str]] = collections.defaultdict(set)
    label_by_form: dict[str, dict[str, set[str]]] = collections.defaultdict(
        lambda: collections.defaultdict(set)
    )
    for it in catalog_items:
        oid, form = _cell(it.get("item_oid")), _cell(it.get("form_oid"))
        if not oid or not form:
            continue
        scope_by_form[form].add(oid)
        label = _cell(it.get("label"))
        if label:
            label_by_form[form][label].add(oid)

    samples: dict[str, list[str]] = {}
    stats: dict[str, Any] = {
        "resolved_direct": 0, "resolved_items_dict": 0, "resolved_label": 0,
        "ambiguous": 0, "unmatched": 0, "unknown_sheets": 0, "per_sheet": {},
    }

    wb = openpyxl.load_workbook(demo_path, read_only=True)
    try:
        items_dict = _load_items_dict(wb)
        for ws in wb.worksheets:
            if ws.title in _SKIP_SHEETS:
                continue
            if ws.title not in scope_by_form:
                stats["unknown_sheets"] += 1   # sheet 名不是 catalog form OID: 静默失效观测哨
            scope = scope_by_form.get(ws.title, set())
            rows = ws.iter_rows(values_only=True)
            header = [_cell(c) for c in next(rows, [])]
            col_oids: list[str | None] = []
            resolved_here = 0
            for name in header:
                if not name:
                    col_oids.append(None)
                    continue
                oid = None
                for key, cand in (
                    ("resolved_direct", {name} & scope),
                    ("resolved_items_dict", items_dict.get(name, set()) & scope),
                    ("resolved_label", label_by_form.get(ws.title, {}).get(name, set())),
                ):
                    if not cand:
                        continue
                    if len(cand) == 1:
                        oid = next(iter(cand))
                        stats[key] += 1
                        resolved_here += 1
                    else:
                        stats["ambiguous"] += 1
                    break
                else:
                    stats["unmatched"] += 1
                col_oids.append(oid)
            stats["per_sheet"][ws.title] = resolved_here

            for row in rows:
                for oid, v in zip(col_oids, row):
                    if oid is None:
                        continue
                    sv = _cell(v)
                    if not sv:
                        continue
                    bucket = samples.setdefault(oid, [])
                    if sv not in bucket and len(bucket) < max_per_item:
                        bucket.append(sv)
    finally:
        wb.close()      # read_only 模式持有文件句柄, Task 7 会循环调用
    return samples, stats
