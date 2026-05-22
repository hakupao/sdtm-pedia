"""SpecChunker — one chunk per variable (H3 heading) in domain spec.md files.

Phase 1A.3 Batch A.
"""

from __future__ import annotations

from pathlib import Path

from .base import BaseChunker, Chunk, heading_positions


class SpecChunker(BaseChunker):
    """Chunk a domain spec.md file: one chunk per H3 variable heading."""

    file_type = "spec"

    def chunk(self, file_path: Path) -> list[Chunk]:
        text = file_path.read_text(encoding="utf-8")
        domain = file_path.parent.name  # e.g. "AE"

        h3s = heading_positions(text, 3)
        if not h3s:
            return []

        chunks: list[Chunk] = []
        for i, (start, section) in enumerate(h3s):
            end = h3s[i + 1][0] if i + 1 < len(h3s) else len(text)
            chunk_text = text[start:end]
            chunks.append(
                self._new_chunk(
                    source=str(file_path),
                    text=chunk_text,
                    chunk_index=i,
                    domain=domain,
                    section=section,
                    # fields not applicable to spec
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
        return chunks
