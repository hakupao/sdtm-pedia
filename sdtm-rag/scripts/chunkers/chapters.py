"""ChaptersChunker — size-aware chunker for knowledge_base/chapters/*.md.

Phase 1A.3 Batch C.

L-4 (locked by 1A.0.c HIGH): chapters/ ≥ 50KB 强制 `^### ` 切 (ch04 §4.4 alone = 9598
cl100k tokens > 8191 embedding limit). Three-tier size policy:
  - size_bytes > 50KB → split by `^### ` (H3)
  - 20KB < size_bytes ≤ 50KB → split by `^## ` (H2)
  - size_bytes ≤ 20KB → whole file = 1 chunk

cdisc_section_id parsed from heading prefix when it matches `\\d+(\\.\\d+){1,3}`,
e.g. `### 4.1.1 Review Study Data ...` → section_id = "4.1.1".

domain = None (chapters are not domain-specific).
"""

from __future__ import annotations

import re
from pathlib import Path

from .base import BaseChunker, Chunk, heading_positions

_SECTION_ID_RE = re.compile(r"^(\d+(?:\.\d+){0,3})\s+")


def _parse_section_id(heading: str) -> str | None:
    m = _SECTION_ID_RE.match(heading)
    return m.group(1) if m else None


class ChaptersChunker(BaseChunker):
    """Chunk a chapters/*.md file with size-aware policy (L-4)."""

    file_type = "chapter"

    def chunk(self, file_path: Path) -> list[Chunk]:
        text = file_path.read_text(encoding="utf-8")
        size_bytes = file_path.stat().st_size

        if size_bytes > 50 * 1024:
            level = 3  # ★ L-4 lock: >50KB MUST split by ### (ch04 case)
        elif size_bytes > 20 * 1024:
            level = 2
        else:
            # Whole file = 1 chunk
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

        headings = heading_positions(text, level)
        if not headings:
            # No heading at requested level → fall back to whole-file
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

        chunks: list[Chunk] = []
        for i, (start, section) in enumerate(headings):
            end = headings[i + 1][0] if i + 1 < len(headings) else len(text)
            chunk_text = text[start:end]
            chunks.append(
                self._new_chunk(
                    source=str(file_path),
                    text=chunk_text,
                    chunk_index=i,
                    domain=None,
                    section=section,
                    cdisc_class=None,
                    cdisc_section_id=_parse_section_id(section),
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
        return chunks
