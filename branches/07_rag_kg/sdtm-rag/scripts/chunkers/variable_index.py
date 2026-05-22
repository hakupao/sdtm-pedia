"""VariableIndexChunker — single-file chunker for knowledge_base/VARIABLE_INDEX.md.

Phase 1A.3 Batch C.

Structure (1A.0 verified):
  §一 通用变量 (## 一、...)                 → 1 chunk
  §二 领域专属变量 (## 二、..., 63 H3 sections)
       Each H3 like "### AE — Adverse Events (Events)" → 1 chunk per domain
                                                       → 63 chunks
  §三 CDISC CT 交叉引用 (## 三、...)        → 1 chunk (no sub-headings; single big table)

Total chunks: 1 + 63 + 1 = 65.

Per-H3 domain code parsed from text before " — ", cdisc_class from "(...)"
parenthetical (e.g. "AE" + "Events").
"""

from __future__ import annotations

import re
from pathlib import Path

from .base import BaseChunker, Chunk, heading_positions

# Detect §一 / §二 / §三 H2 boundaries (CJK numerals).
_SECTION_H2_RE = re.compile(r"^##\s+(一|二|三)、(.+?)\s*$", re.MULTILINE)

# Parse H3 like "AE — Adverse Events (Events)".
# Groups: 1=domain code, 2=label, 3=class (in parens, optional).
_DOMAIN_H3_RE = re.compile(r"^\s*([A-Z][A-Z0-9]+)\s+—\s+(.+?)(?:\s+\(([^)]+)\))?\s*$")


def _parse_domain_h3(heading: str) -> tuple[str | None, str | None]:
    """Return (domain_code, cdisc_class) from H3 heading text.

    Returns (None, None) if heading doesn't match expected pattern.
    """
    m = _DOMAIN_H3_RE.match(heading)
    if m:
        return m.group(1), m.group(3)  # class may be None if no parens
    return None, None


class VariableIndexChunker(BaseChunker):
    """Chunk VARIABLE_INDEX.md into §一 (1) + §二 (63 by domain) + §三 (1)."""

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

        # ── §一 chunk: from §一 start to §二 start (or §三/EOF if no §二) ─────
        if yi_start is not None:
            yi_end = er_start if er_start is not None else (san_start if san_start is not None else len(text))
            yi_text = text[yi_start:yi_end]
            chunks.append(
                self._new_chunk(
                    source=str(file_path),
                    text=yi_text,
                    chunk_index=chunk_idx,
                    domain=None,
                    section="§一 通用变量",
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

        # ── §三 chunk: single chunk (table has no internal headings) ─────────
        if san_start is not None:
            san_text = text[san_start:]
            chunks.append(
                self._new_chunk(
                    source=str(file_path),
                    text=san_text,
                    chunk_index=chunk_idx,
                    domain=None,
                    section="§三 CT 交叉引用",
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

        return chunks
