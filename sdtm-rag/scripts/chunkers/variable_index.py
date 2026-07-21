"""VariableIndexChunker — single-file chunker for knowledge_base/VARIABLE_INDEX.md.

Phase 1A.3 Batch C; re-chunking fix (per-row §一/§三 splitting).

Structure:
  §一 通用变量 (## 一、...)                 → 1 chunk PER common-variable row
       GFM table `变量名|域数|出现的域|Label|Type|Role|Core` (24 data rows)
       → 24 chunks, each a natural-language rendering of one variable.
  §二 领域专属变量 (## 二、..., 63 H3 sections)
       Each H3 like "### AE — Adverse Events (Events)" → 1 chunk per domain
                                                       → 63 chunks (UNCHANGED)
  §三 CDISC CT 交叉引用 (## 三、...)        → 1 chunk PER CT-code row
       GFM table `CT Code|引用数|引用此 CT 的变量` (135 data rows)
       → 135 chunks, each naming a codelist + its referencing variables.

Total chunks: 24 + 63 + 135 = 222.

Per-H3 domain code parsed from text before " — ", cdisc_class from "(...)"
parenthetical (e.g. "AE" + "Events").

Rationale: the original single §一/§三 chunks were GIANT tables whose embeddings
were diluted; per-row chunks put the right content into top-15 retrieval.
"""

from __future__ import annotations

import re
from pathlib import Path

from .base import BaseChunker, Chunk, heading_positions

# Detect §一 / §二 / §三 H2 boundaries (CJK numerals).
_SECTION_H2_RE = re.compile(r"^##\s+(一|二|三)、(.+?)\s*$", re.MULTILINE)

# Validate a §三 CT Code cell (e.g. C66742); rejects header leaks / malformed rows.
_CT_CODE_RE = re.compile(r"^C\d+$")

# Parse H3 like "AE — Adverse Events (Events)".
# Groups: 1=domain code, 2=label, 3=class (in parens, optional).
_DOMAIN_H3_RE = re.compile(r"^\s*([A-Z][A-Z0-9]+)\s+—\s+(.+?)(?:\s+\(([^)]+)\))?\s*$")

# GFM table separator row like `|---|---|` (also matches `:--:` alignment).
_GFM_SEP_RE = re.compile(r"^\|[\s\-:|]+\|?\s*$")


def _parse_domain_h3(heading: str) -> tuple[str | None, str | None]:
    """Return (domain_code, cdisc_class) from H3 heading text.

    Returns (None, None) if heading doesn't match expected pattern.
    """
    m = _DOMAIN_H3_RE.match(heading)
    if m:
        return m.group(1), m.group(3)  # class may be None if no parens
    return None, None


def _parse_gfm_data_rows(section_text: str) -> list[list[str]]:
    """Return data rows (each a list of stripped cell strings) from a GFM table.

    Skips the header row and the `|---|` separator row. A data row is any line
    starting with `|` that follows the separator. Robust to trailing pipes and
    surrounding whitespace.
    """
    rows: list[list[str]] = []
    seen_separator = False
    for raw in section_text.splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            continue
        if _GFM_SEP_RE.match(line):
            seen_separator = True
            continue
        if not seen_separator:
            # This is the header row (first pipe line before the separator).
            continue
        # Split on `|`, drop the empty leading/trailing cells from outer pipes.
        cells = [c.strip() for c in line.split("|")]
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]
        rows.append(cells)
    return rows


class VariableIndexChunker(BaseChunker):
    """Chunk VARIABLE_INDEX.md into §一 (24 per-variable) + §二 (63 by domain) + §三 (135 per-CT-code)."""

    file_type = "variable_index"

    def chunk(self, file_path: Path) -> list[Chunk]:
        text = file_path.read_text(encoding="utf-8")

        # Find §一 / §二 / §三 H2 boundaries
        section_marks: dict[str, tuple[int, str]] = {}
        for m in _SECTION_H2_RE.finditer(text):
            section_marks[m.group(1)] = (m.start(), m.group(0).rstrip())

        chunks: list[Chunk] = []
        chunk_idx = 0

        # Determine boundaries in document order
        ordered = sorted(section_marks.values(), key=lambda x: x[0])
        if not ordered:
            # Fallback: whole file as 1 chunk
            return [
                self._new_chunk(
                    source=str(file_path),
                    text=text,
                    chunk_index=0,
                    domain=None,
                    section="whole_file",
                    cdisc_class=None,
                    cdisc_section_id=None,
                    example_index=None,
                    sub_label=None,
                    has_mermaid=None,
                    has_table=None,
                    ct_code=None,
                    ct_extensible=None,
                    part_index=None,
                    table_chunk_idx=None,
                )
            ]

        yi_start = section_marks.get("一", (None, ""))[0]
        er_start = section_marks.get("二", (None, ""))[0]
        san_start = section_marks.get("三", (None, ""))[0]

        # ── §一 chunks: one per common-variable row ──────────────────────────
        # GFM columns: 变量名 | 域数 | 出现的域 | Label | Type | Role | Core
        if yi_start is not None:
            yi_end = er_start if er_start is not None else (san_start if san_start is not None else len(text))
            yi_text = text[yi_start:yi_end]
            for cells in _parse_gfm_data_rows(yi_text):
                if len(cells) < 7:
                    continue  # malformed row; skip defensively
                var_name, dom_count, domains, label, vtype, role, core = cells[:7]
                row_text = (
                    f"{var_name} ({label}) — {role} variable, type {vtype}, "
                    f"Core {core}. Appears in {dom_count} SDTM domains: {domains}."
                )
                chunks.append(
                    self._new_chunk(
                        source=str(file_path),
                        text=row_text,
                        chunk_index=chunk_idx,
                        domain=None,
                        section=f"§一 通用变量: {var_name}",
                        cdisc_class=None,
                        cdisc_section_id=None,
                        example_index=None,
                        sub_label=None,
                        has_mermaid=None,
                        has_table=None,
                        ct_code=None,
                        ct_extensible=None,
                        part_index=None,
                        table_chunk_idx=None,
                    )
                )
                chunk_idx += 1

        # ── §二 chunks: one per H3 domain section ────────────────────────────
        if er_start is not None:
            er_end = san_start if san_start is not None else len(text)
            er_slice = text[er_start:er_end]
            # Find H3s within §二 slice (positions are slice-local)
            h3s_local = heading_positions(er_slice, 3)
            for i, (h3_start_local, h3_heading) in enumerate(h3s_local):
                h3_end_local = (
                    h3s_local[i + 1][0] if i + 1 < len(h3s_local) else len(er_slice)
                )
                h3_text = er_slice[h3_start_local:h3_end_local]
                domain_code, cdisc_class = _parse_domain_h3(h3_heading)
                chunks.append(
                    self._new_chunk(
                        source=str(file_path),
                        text=h3_text,
                        chunk_index=chunk_idx,
                        domain=domain_code,
                        section=h3_heading,
                        cdisc_class=cdisc_class,
                        cdisc_section_id=None,
                        example_index=None,
                        sub_label=None,
                        has_mermaid=None,
                        has_table=None,
                        ct_code=None,
                        ct_extensible=None,
                        part_index=None,
                        table_chunk_idx=None,
                    )
                )
                chunk_idx += 1

        # ── §三 chunks: one per CT-code row ──────────────────────────────────
        # GFM columns: CT Code | 引用数 | 引用此 CT 的变量 (域.变量名)
        if san_start is not None:
            san_text = text[san_start:]
            for cells in _parse_gfm_data_rows(san_text):
                if len(cells) < 3:
                    continue  # malformed row; skip defensively
                ct_code, ref_count, ref_vars = cells[:3]
                if not _CT_CODE_RE.match(ct_code):
                    continue  # skip header leak / malformed rows (Rule-D MED)
                row_text = (
                    f"CT Code {ct_code} — controlled terminology codelist "
                    f"referenced by {ref_count} variable(s): {ref_vars}."
                )
                chunks.append(
                    self._new_chunk(
                        source=str(file_path),
                        text=row_text,
                        chunk_index=chunk_idx,
                        domain=None,
                        section=f"§三 CT 交叉引用: {ct_code}",
                        cdisc_class=None,
                        cdisc_section_id=None,
                        example_index=None,
                        sub_label=None,
                        has_mermaid=None,
                        has_table=None,
                        ct_code=ct_code,
                        ct_extensible=None,
                        part_index=None,
                        table_chunk_idx=None,
                    )
                )
                chunk_idx += 1

        return chunks
