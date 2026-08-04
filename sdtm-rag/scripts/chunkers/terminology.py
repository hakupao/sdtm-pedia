"""TerminologyChunker — part vs codelist mode dispatcher for terminology/*.md.

Phase 1A.3 Batch C; 1A.5 巨型 part fallback (PLAN §6.4) — lb_part2/3 N=100 row slicing.

L-5 (locked by 1A.0.a): terminology/core part files
  - H2 count == 1 AND filename matches `*_part<N>.md` → **part mode**
    - default: whole file = 1 chunk, part_index from filename
    - 1A.5 fallback (PLAN §6.4): if whole-file tokens > 6000, slice the single GFM
      pipe-table by N=100 row batches; each batch keeps header+separator prepended,
      pre-table prefix concatenated to chunk 0; metadata `table_chunk_idx=0,1,...`
      retains `part_index`.
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

from .base import BaseChunker, Chunk, count_tokens, find_table_blocks, heading_positions

# Match a terminology H2 heading like `Adverse Event Severity (C66769)`.
# Group 1 = name (lazy), group 2 = Cxxxxx code.
_CODELIST_HEADING_RE = re.compile(r"^(.*?)\s*\((C\d+)\)\s*$")

# Match `_partN` suffix in filename stem to extract N.
_PART_SUFFIX_RE = re.compile(r"_part(\d+)$")

# GFM table separator row like `|---|---|` (also matches `:--:` alignment).
_GFM_SEP_RE = re.compile(r"^\|[\s\-:|]+\|?\s*$")

# A CT-code cell in VARIABLE_INDEX.md §三 (e.g. C66769).
_CT_CODE_RE = re.compile(r"^C\d+$")

# PLAN §6.4 巨型 part 兜底门限 (cl100k tokens). 触发后按 N 行表切片.
_GIANT_PART_TOKEN_THRESHOLD = 6000
# 表切片每段行数 (PLAN §6.4 N=100).
_TABLE_ROW_BATCH = 100


def _parse_codelist_heading(heading: str) -> tuple[str, str | None]:
    """Return (name, ct_code or None). Falls back to (heading, None) if no Cxxxx code."""
    m = _CODELIST_HEADING_RE.match(heading)
    if m:
        return m.group(1).strip(), m.group(2)
    return heading.strip(), None


def _parse_part_index(stem: str) -> int | None:
    m = _PART_SUFFIX_RE.search(stem)
    return int(m.group(1)) if m else None


def _slice_giant_part_by_rows(
    text: str,
    table_start: int,
    table_end: int,
) -> list[str]:
    """Split a single-table giant part file into chunks of header+separator+N rows.

    Layout expected by 1A.5 fallback (verified for lb_part2/3, 1 GFM table):
      [pre_text] ... |hdr|...|\n|---|...|\n|row1|...|\n|row2|...|\n... [post_text]

    Returns list of chunk_text strings:
      - chunk 0: pre_text + header + separator + rows[0..N-1] + post_text_after_last_chunk? no
                Actually only chunk 0 carries pre_text; the *last* chunk carries post_text.
      - chunks 1..K-1: header + separator + next N rows (post_text appended only to last)
    """
    pre_text = text[:table_start]
    table_text = text[table_start:table_end]
    post_text = text[table_end:]

    table_lines = table_text.splitlines(keepends=True)
    # First non-empty line = header; second = separator; rest = data rows (last may be partial)
    # Strip trailing empty lines.
    while table_lines and table_lines[-1].strip() == "":
        table_lines.pop()
    if len(table_lines) < 2:
        # Defensive: not really a table — fallback to single chunk.
        return [text]
    header = table_lines[0]
    separator = table_lines[1]
    data_rows = table_lines[2:]
    if not data_rows:
        return [text]

    chunks: list[str] = []
    n_batches = (len(data_rows) + _TABLE_ROW_BATCH - 1) // _TABLE_ROW_BATCH
    for batch_idx in range(n_batches):
        start = batch_idx * _TABLE_ROW_BATCH
        end = min(start + _TABLE_ROW_BATCH, len(data_rows))
        batch_rows = "".join(data_rows[start:end])
        parts: list[str] = []
        if batch_idx == 0:
            parts.append(pre_text)
        parts.append(header)
        parts.append(separator)
        parts.append(batch_rows)
        if batch_idx == n_batches - 1:
            parts.append(post_text)
        chunks.append("".join(parts))
    return chunks


class TerminologyChunker(BaseChunker):
    """Chunk a terminology/**/*.md file: part mode or codelist mode (L-5)."""

    file_type = "terminology"

    def __init__(self, kb_root: Path) -> None:
        super().__init__(kb_root)
        # Lazy ct_code → "域.变量名, ..." map built from VARIABLE_INDEX.md §三.
        self._ct_usage: dict[str, str] | None = None

    @property
    def ct_usage_map(self) -> dict[str, str]:
        """ct_code → referencing-variable string, parsed from VARIABLE_INDEX.md §三.

        Built once and cached. Returns {} if VARIABLE_INDEX.md is missing.
        """
        if self._ct_usage is None:
            self._ct_usage = self._build_ct_usage_map()
        return self._ct_usage

    def _build_ct_usage_map(self) -> dict[str, str]:
        """Parse the §三 GFM table (CT Code | 引用数 | 引用此 CT 的变量) into a map."""
        var_index = self.kb_root / "VARIABLE_INDEX.md"
        if not var_index.exists():
            return {}
        text = var_index.read_text(encoding="utf-8")
        # Rule-D HIGH fix: scope the parse to §三 only, so §一/§二 rows can never
        # leak into the map even if a future schema change makes a variable name
        # match C\d+. Bail gracefully if §三 is absent.
        san = re.search(r"^##\s+(?:三、|3\.\s)", text, re.MULTILINE)
        if not san:
            return {}
        text = text[san.start():]
        usage: dict[str, str] = {}
        seen_separator = False
        for raw in text.splitlines():
            line = raw.strip()
            if not line.startswith("|"):
                continue
            if _GFM_SEP_RE.match(line):
                seen_separator = True
                continue
            if not seen_separator:
                continue  # header row(s) before any separator
            cells = [c.strip() for c in line.split("|")]
            if cells and cells[0] == "":
                cells = cells[1:]
            if cells and cells[-1] == "":
                cells = cells[:-1]
            if len(cells) < 3:
                continue
            ct_code, _ref_count, ref_vars = cells[0], cells[1], cells[2]
            if _CT_CODE_RE.match(ct_code) and ref_vars:
                usage[ct_code] = ref_vars
        return usage

    def chunk(self, file_path: Path) -> list[Chunk]:
        text = file_path.read_text(encoding="utf-8")
        h2s = heading_positions(text, 2)
        stem = file_path.stem
        part_idx = _parse_part_index(stem)

        # ── Part mode: H2 == 1 AND filename has _partN suffix ────────────────
        if len(h2s) == 1 and part_idx is not None:
            whole_tokens = count_tokens(text)
            # PLAN §6.4 巨型 part 兜底: tokens > 6000 → N=100 row table-slice.
            if whole_tokens > _GIANT_PART_TOKEN_THRESHOLD:
                tables = find_table_blocks(text)
                if len(tables) == 1:
                    table_start, table_end = tables[0]
                    chunk_texts = _slice_giant_part_by_rows(text, table_start, table_end)
                    if len(chunk_texts) > 1:
                        chunks: list[Chunk] = []
                        for idx, chunk_text in enumerate(chunk_texts):
                            chunks.append(
                                self._new_chunk(
                                    source=str(file_path),
                                    text=chunk_text,
                                    chunk_index=idx,
                                    domain=None,
                                    section=stem,
                                    cdisc_class=None,
                                    cdisc_section_id=None,
                                    example_index=None,
                                    sub_label=None,
                                    has_mermaid=None,
                                    has_table=True,
                                    ct_code=None,
                                    ct_extensible=None,
                                    part_index=part_idx,
                                    table_chunk_idx=idx,
                                )
                            )
                        return chunks
                # If table layout doesn't match expectation, fall through to 1-chunk part mode
                # (defensive — emit as-is, embedding will truncate; documented in evidence).
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
            # Enrich with which variable(s) use this codelist (generic, via §三 map).
            if ct_code is not None:
                used_by = self.ct_usage_map.get(ct_code)
                if used_by:
                    chunk_text = f"Used by variable(s): {used_by}.\n\n" + chunk_text
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
