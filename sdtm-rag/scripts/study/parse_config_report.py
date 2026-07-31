"""ConfigurationReport (Viedoc 导出 xlsx) 确定性解析器. 零 LLM."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import openpyxl


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


@dataclass(frozen=True)
class FormDef:
    oid: str
    name: str
    summary_format: str
    description: str
    in_use: str
    row: int
    is_trailer: bool = False   # Viedoc 表尾脚注行 (oid 含空格 / In use 空), 真实 form 21 个均非此形态


@dataclass(frozen=True)
class ItemRow:
    row: int
    form_oid: str
    form_name: str
    row_type: str          # 'Item group' | 'Item' | 'Trailer' (表尾脚注, 白名单外归一化)
    group_oid: str
    group_name: str
    item_oid: str
    data_type: str
    required: bool
    min_length: str
    max_length: str
    data_checks: str
    system_checks: str
    label: str
    control_type: str
    choices: str
    unit: str
    description: str
    instructions: str
    visible_condition: str
    output_field_id: str
    output_field_label: str
    raw: dict = field(repr=False)


@dataclass(frozen=True)
class Codelist:
    oid: str
    data_type: str
    entries: list


def _req(rec: dict, key: str) -> str:
    if key not in rec:
        raise KeyError(f"{key} (available: {sorted(k for k in rec if k != '_row')[:8]}...)")
    return rec[key]


def parse_forms(path: Path) -> list[FormDef]:
    wb = openpyxl.load_workbook(path, read_only=True)
    out: list[FormDef] = []
    for r in read_sheet_records(wb["Forms"]):
        oid = _req(r, "General::Id")
        in_use = r.get("General::In use", "")
        out.append(FormDef(
            oid=oid, name=r.get("General::Name", ""),
            summary_format=r.get("General::Summary format", ""),
            description=r.get("General::Description", ""),
            in_use=in_use, row=r["_row"],
            is_trailer=(" " in oid or not in_use),
        ))
    return out


def parse_items(path: Path) -> list[ItemRow]:
    wb = openpyxl.load_workbook(path, read_only=True)
    out: list[ItemRow] = []
    for r in read_sheet_records(wb["Items and Groups"]):
        raw_type = r.get("Type and container::Field type", "")
        out.append(ItemRow(
            row=r["_row"],
            form_oid=_req(r, "Type and container::Form ID"),
            form_name=r.get("Type and container::Form Name", ""),
            row_type=raw_type if raw_type in ("Item", "Item group") else "Trailer",
            group_oid=r.get("Type and container::Item group ID", ""),
            group_name=r.get("Type and container::Item group name", ""),
            item_oid=_req(r, "Validation::Item ID"),
            data_type=r.get("Validation::Data type", ""),
            required=r.get("Validation::Required field", "") == "X",
            min_length=r.get("Validation::Minimum length", ""),
            max_length=r.get("Validation::Max length", ""),
            data_checks=r.get("Validation::Data checks", ""),
            system_checks=r.get("Validation::System checks", ""),
            label=r.get("General::Field label", ""),
            control_type=r.get("General::Control Type", ""),
            choices=r.get("General::Choices", ""),
            unit=r.get("General::Measurement Unit", ""),
            description=r.get("General::Description", ""),
            instructions=r.get("General::Instructions for user", ""),
            visible_condition=r.get("Visibility::Show on simple condition", ""),
            output_field_id=r.get("Output::Output Field ID", ""),
            output_field_label=r.get("Output::Output Field Label", ""),
            raw={k: v for k, v in r.items() if k != "_row"},
        ))
    return out


def parse_codelists(path: Path) -> dict[str, Codelist]:
    wb = openpyxl.load_workbook(path, read_only=True)
    grouped: dict[str, Codelist] = {}
    for r in read_sheet_records(wb["Code lists"], has_section_row=False):
        oid = _req(r, "Code lists::OID")
        cl = grouped.setdefault(
            oid, Codelist(oid=oid, data_type=r.get("Code lists::Data Type", ""), entries=[])
        )
        cl.entries.append((r.get("Code lists::Code value", ""), r.get("Code lists::Code text", "")))
    return grouped
