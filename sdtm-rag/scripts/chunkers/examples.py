"""ExamplesChunker — domain-aware chunking of domains/*/examples.md files.

Phase 1A.3 Batch B (★ HIGH-RISK per PLAN §4.4 R-1 / R-2).

Heading level varies by domain:
  - Flat H2 style (TA / IS / DS / EX / DM / MB / most domains):
      `## Example N` (+ optional trailing `## Trial Arms Issues` etc.) — 1 chunk per H2.
  - Nested H4 style (PC only, per chunker_feasibility §3.2 + 1A.0.a):
      `## §6.3.5.9.3 ...` → `### Example N` → `#### Method A/B/C/D` — 1 chunk per H4 Method.
      PC Example 4 has only Method A + D (not all 4), so H4 count = 14 (not 16).

Heading-level detection rule (lightweight heuristic, single pass):
  - If H4 count >= 2 AND any H4 text starts with "Method " → use H4 level (PC nested).
  - Else → use H2 level (flat).

Locks honored (per evidence/checkpoints/phase_1a_0_sanity.md §4):
  - L-1 mermaid: status-machine via base.find_mermaid_blocks (0 nesting verified).
  - L-2 GFM pipe-table: simple regex via base.find_table_blocks.
  - L-3 token count: BaseChunker._new_chunk auto-fills via tiktoken cl100k_base.

Headings that fall inside a protected (mermaid/table) block are defensively dropped
(should not happen per 1A.0.b, but cheap insurance).
"""

from __future__ import annotations

import re
from pathlib import Path

from .base import (
    BaseChunker,
    Chunk,
    find_mermaid_blocks,
    find_table_blocks,
    heading_positions,
    is_inside_block,
)

# §-prefix CDISC section id (e.g., "§6.3.5.9.3"). Captures up to the trailing space.
_SECTION_ID_RE = re.compile(r"^(§[\d.]+)\b")

# "Example N" — extracts the trailing index (allows leading prefix text).
_EXAMPLE_INDEX_RE = re.compile(r"\bExample\s+(\d+)\b", re.IGNORECASE)

# "Method X" — captures the letter token (A/B/C/D...).
_METHOD_RE = re.compile(r"\bMethod\s+([A-Z][A-Za-z0-9]*)\b")


def _parse_example_index(text: str) -> int | None:
    m = _EXAMPLE_INDEX_RE.search(text)
    return int(m.group(1)) if m else None


def _parse_sub_label(text: str) -> str | None:
    m = _METHOD_RE.search(text)
    return f"Method {m.group(1)}" if m else None


def _parse_section_id(text: str) -> str | None:
    m = _SECTION_ID_RE.match(text)
    return m.group(1) if m else None


def _range_contains_block(
    start: int, end: int, blocks: list[tuple[int, int]]
) -> bool:
    """True if any block overlaps the [start, end) byte range."""
    for bs, be in blocks:
        if bs < end and be > start:
            return True
    return False


def _filter_protected(
    headings: list[tuple[int, str]],
    blocks: list[tuple[int, int]],
) -> list[tuple[int, str]]:
    """Drop heading positions that fall inside any protected block (defensive)."""
    if not blocks:
        return headings
    return [(pos, txt) for pos, txt in headings if not is_inside_block(pos, blocks)]


class ExamplesChunker(BaseChunker):
    """Chunk a domains/*/examples.md file. Domain-aware (H2 flat vs H4 nested)."""

    file_type = "examples"

    def chunk(self, file_path: Path) -> list[Chunk]:
        text = file_path.read_text(encoding="utf-8")
        domain = file_path.parent.name  # e.g. "TA" / "PC" / "IS" / "DS"

        mermaid_blocks = find_mermaid_blocks(text)
        table_blocks = find_table_blocks(text)
        protected = mermaid_blocks + table_blocks

        h2s = _filter_protected(heading_positions(text, 2), protected)
        h3s = _filter_protected(heading_positions(text, 3), protected)
        h4s = _filter_protected(heading_positions(text, 4), protected)

        # Detect nested-H4 mode (PC style): >=2 H4 + any H4 text starts with "Method ".
        is_h4_mode = len(h4s) >= 2 and any(
            txt.startswith("Method ") for _, txt in h4s
        )

        if is_h4_mode:
            return self._chunk_h4_nested(
                file_path, text, domain, h2s, h3s, h4s, mermaid_blocks, table_blocks
            )
        return self._chunk_h2_flat(
            file_path, text, domain, h2s, mermaid_blocks, table_blocks
        )

    # ---- H2 flat (TA / IS / DS / EX / DM / MB / ...) ----
    def _chunk_h2_flat(
        self,
        file_path: Path,
        text: str,
        domain: str,
        h2s: list[tuple[int, str]],
        mermaid_blocks: list[tuple[int, int]],
        table_blocks: list[tuple[int, int]],
    ) -> list[Chunk]:
        if not h2s:
            return []

        chunks: list[Chunk] = []
        for i, (start, heading) in enumerate(h2s):
            end = h2s[i + 1][0] if i + 1 < len(h2s) else len(text)
            chunk_text = text[start:end]
            chunks.append(
                self._new_chunk(
                    source=str(file_path),
                    text=chunk_text,
                    chunk_index=i,
                    domain=domain,
                    section=heading,
                    cdisc_class=None,
                    cdisc_section_id=_parse_section_id(heading),
                    example_index=_parse_example_index(heading),
                    sub_label=None,
                    has_mermaid=_range_contains_block(start, end, mermaid_blocks),
                    has_table=_range_contains_block(start, end, table_blocks),
                    ct_code=None,
                    ct_extensible=None,
                    part_index=None,
                    table_chunk_idx=None,
                )
            )
        return chunks

    # ---- H4 nested (PC) ----
    def _chunk_h4_nested(
        self,
        file_path: Path,
        text: str,
        domain: str,
        h2s: list[tuple[int, str]],
        h3s: list[tuple[int, str]],
        h4s: list[tuple[int, str]],
        mermaid_blocks: list[tuple[int, int]],
        table_blocks: list[tuple[int, int]],
    ) -> list[Chunk]:
        # cdisc_section_id from first H2 (PC has 1 H2 "§6.3.5.9.3 ...").
        section_id = _parse_section_id(h2s[0][1]) if h2s else None

        # Sort H3/H4 by byte position to support generic mapping
        # (already sorted by re.finditer, but explicit for safety).
        h3s_sorted = sorted(h3s, key=lambda t: t[0])
        h4s_sorted = sorted(h4s, key=lambda t: t[0])

        # Build (h3_start, h3_end, h3_text) ranges
        h3_ranges: list[tuple[int, int, str]] = []
        for i, (s, t) in enumerate(h3s_sorted):
            e = h3s_sorted[i + 1][0] if i + 1 < len(h3s_sorted) else len(text)
            h3_ranges.append((s, e, t))

        def _h3_for(pos: int) -> str | None:
            """Return the H3 heading text whose range contains pos, else None."""
            for s, e, t in h3_ranges:
                if s <= pos < e:
                    return t
            return None

        chunks: list[Chunk] = []
        for i, (start, heading) in enumerate(h4s_sorted):
            end = h4s_sorted[i + 1][0] if i + 1 < len(h4s_sorted) else len(text)
            chunk_text = text[start:end]
            parent_h3 = _h3_for(start)
            example_index = (
                _parse_example_index(parent_h3) if parent_h3 else None
            )
            chunks.append(
                self._new_chunk(
                    source=str(file_path),
                    text=chunk_text,
                    chunk_index=i,
                    domain=domain,
                    section=heading,
                    cdisc_class=None,
                    cdisc_section_id=section_id,
                    example_index=example_index,
                    sub_label=_parse_sub_label(heading),
                    has_mermaid=_range_contains_block(start, end, mermaid_blocks),
                    has_table=_range_contains_block(start, end, table_blocks),
                    ct_code=None,
                    ct_extensible=None,
                    part_index=None,
                    table_chunk_idx=None,
                )
            )
        return chunks
