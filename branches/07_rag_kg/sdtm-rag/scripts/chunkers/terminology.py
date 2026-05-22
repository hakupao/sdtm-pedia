"""TerminologyChunker — part vs codelist mode dispatcher for terminology/*.md.

Phase 1A.3 Batch C.

L-5 (locked by 1A.0.a): terminology/core part files
  - H2 count == 1 AND filename matches `*_part<N>.md` → **part mode**
    (whole file = 1 chunk, part_index from filename)
  - H2 count > 1 OR not part-named → **codelist mode**
    (one chunk per H2; parse "## Name (Cxxxx)" → section=name, ct_code=Cxxxx)

Edge case (1A.0.a verified): lb_part4.md has 2 H2 codelists, so it MUST go
through codelist mode (NOT part mode) — H2>1 branch handles this.

domain = None for terminology (codelists are not 1-to-1 with domains; some
codelists are shared across domains).
"""

from __future__ import annotations

import re
from pathlib import Path

from .base import BaseChunker, Chunk, heading_positions

# Match a terminology H2 heading like `Adverse Event Severity (C66769)`.
# Group 1 = name (lazy), group 2 = Cxxxxx code.
_CODELIST_HEADING_RE = re.compile(r"^(.*?)\s*\((C\d+)\)\s*$")

# Match `_partN` suffix in filename stem to extract N.
_PART_SUFFIX_RE = re.compile(r"_part(\d+)$")


def _parse_codelist_heading(heading: str) -> tuple[str, str | None]:
    """Return (name, ct_code or None). Falls back to (heading, None) if no Cxxxx code."""
    m = _CODELIST_HEADING_RE.match(heading)
    if m:
        return m.group(1).strip(), m.group(2)
    return heading.strip(), None


def _parse_part_index(stem: str) -> int | None:
    m = _PART_SUFFIX_RE.search(stem)
    return int(m.group(1)) if m else None


class TerminologyChunker(BaseChunker):
    """Chunk a terminology/**/*.md file: part mode or codelist mode (L-5)."""

    file_type = "terminology"

    def chunk(self, file_path: Path) -> list[Chunk]:
        text = file_path.read_text(encoding="utf-8")
        h2s = heading_positions(text, 2)
        stem = file_path.stem
        part_idx = _parse_part_index(stem)

        # ── Part mode: H2 == 1 AND filename has _partN suffix ────────────────
        if len(h2s) == 1 and part_idx is not None:
            return [
                self._new_chunk(
                    source=str(file_path),
                    text=text,
                    chunk_index=0,
                    domain=None,
                    section=stem,
                    cdisc_class=None,
                    cdisc_section_id=None,
                    example_index=None,
                    sub_label=None,
                    has_mermaid=None,
                    has_table=None,
                    ct_code=None,
                    ct_extensible=None,
                    part_index=part_idx,
                    table_chunk_idx=None,
                )
            ]

        # ── Codelist mode: one chunk per H2 (incl. H2>1 part files like lb_part4) ─
        if not h2s:
            # Pathological case: no H2 at all → whole file as 1 chunk
            return [
                self._new_chunk(
                    source=str(file_path),
                    text=text,
                    chunk_index=0,
                    domain=None,
                    section=stem,
                    cdisc_class=None,
                    cdisc_section_id=None,
                    example_index=None,
                    sub_label=None,
                    has_mermaid=None,
                    has_table=None,
                    ct_code=None,
                    ct_extensible=None,
                    part_index=part_idx,
                    table_chunk_idx=None,
                )
            ]

        chunks: list[Chunk] = []
        for i, (start, heading) in enumerate(h2s):
            end = h2s[i + 1][0] if i + 1 < len(h2s) else len(text)
            chunk_text = text[start:end]
            name, ct_code = _parse_codelist_heading(heading)
            chunks.append(
                self._new_chunk(
                    source=str(file_path),
                    text=chunk_text,
                    chunk_index=i,
                    domain=None,
                    section=name,
                    cdisc_class=None,
                    cdisc_section_id=None,
                    example_index=None,
                    sub_label=None,
                    has_mermaid=None,
                    has_table=None,
                    ct_code=ct_code,
                    ct_extensible=None,  # deferred: no reliable signal yet
                    part_index=part_idx,
                    table_chunk_idx=None,
                )
            )
        return chunks
