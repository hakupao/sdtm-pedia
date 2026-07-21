"""ModelChunker — one chunk per H2 section in model/*.md files.

Phase 1A.3 Batch A.

model/ files are not domain-specific; domain=None for all chunks.
"""

from __future__ import annotations

from pathlib import Path

from .base import BaseChunker, Chunk, heading_positions


class ModelChunker(BaseChunker):
    """Chunk a model/*.md file: one chunk per H2 section heading."""

    file_type = "model"

    def chunk(self, file_path: Path) -> list[Chunk]:
        text = file_path.read_text(encoding="utf-8")

        h2s = heading_positions(text, 2)
        if not h2s:
            # No H2s: yield entire file as a single chunk
            return [
                self._new_chunk(
                    source=str(file_path),
                    text=text,
                    chunk_index=0,
                    domain=None,
                    section=None,
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
        for i, (start, section) in enumerate(h2s):
            end = h2s[i + 1][0] if i + 1 < len(h2s) else len(text)
            chunk_text = text[start:end]
            chunks.append(
                self._new_chunk(
                    source=str(file_path),
                    text=chunk_text,
                    chunk_index=i,
                    domain=None,
                    section=section,
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
