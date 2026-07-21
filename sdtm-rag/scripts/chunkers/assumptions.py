"""AssumptionsChunker — one chunk for intro + one chunk per numbered item.

Phase 1A.3 Batch A.

Numbered item detection: regex `^(\\d+)\\.\\s` (re.MULTILINE).
Tables inside a numbered item stay within that item's byte slice (no further splitting).
"""

from __future__ import annotations

import re
from pathlib import Path

from .base import BaseChunker, Chunk

_ITEM_RE = re.compile(r"^(\d+)\.\s", re.MULTILINE)


class AssumptionsChunker(BaseChunker):
    """Chunk a domain assumptions.md file.

    Layout:
      - Chunk 0: text before first numbered item (section="overview"); omitted if empty.
      - Chunk N: each numbered item (section="item_<n>", where n is the item number).
    """

    file_type = "assumptions"

    def chunk(self, file_path: Path) -> list[Chunk]:
        text = file_path.read_text(encoding="utf-8")
        domain = file_path.parent.name  # e.g. "AE"

        matches = list(_ITEM_RE.finditer(text))
        chunks: list[Chunk] = []
        chunk_idx = 0

        # --- Overview chunk (text before first numbered item) ---
        if matches:
            overview_text = text[: matches[0].start()].strip()
        else:
            overview_text = text.strip()

        if overview_text:
            chunks.append(
                self._new_chunk(
                    source=str(file_path),
                    text=overview_text,
                    chunk_index=chunk_idx,
                    domain=domain,
                    section="overview",
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

        # --- One chunk per numbered item ---
        for i, m in enumerate(matches):
            item_num = m.group(1)
            start = m.start()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            item_text = text[start:end].strip()
            chunks.append(
                self._new_chunk(
                    source=str(file_path),
                    text=item_text,
                    chunk_index=chunk_idx,
                    domain=domain,
                    section=f"item_{item_num}",
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
