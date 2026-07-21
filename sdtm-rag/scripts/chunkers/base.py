"""Base chunker classes + Chunk metadata schema.

Phase 1A.3 — main session writes this; Batch A/B/C executors implement file-type-specific
chunkers on top.

References:
- PLAN.md §6 (chunker implementation) + §7 (metadata schema)
- evidence/checkpoints/phase_1a_0_sanity.md §4 — chunker config locks (1A.3 writer 必准拠):
  - L-1: mermaid 状态机 (0 嵌套 verified) — 进入 ```mermaid 跳到下一个 ``` 退出, 不用 stack
  - L-2: GFM pipe-table 简单 regex (0 HTML rowspan/colspan/<table>)
  - L-3: tiktoken cl100k_base 实测强制 (char/4 偏差最大 23.6%, 不允许 char/4)
  - L-4: chapters/ ≥ 50KB 强制 `^### ` 切 (ch04 §4.4 = 9598 cl100k > 8191 embedding limit)
  - L-5: terminology core part 文件 H2=1 → part 模式 / H2>1 → codelist 模式
- F-15: schema 字段约定 — 所有字段 fill, 不适用时存 None (Chroma null vs missing 行为不同)
"""

from __future__ import annotations

import re
import subprocess
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

import tiktoken

_ENC = tiktoken.get_encoding("cl100k_base")


def count_tokens(text: str) -> int:
    """L-3: tiktoken cl100k_base 实测. 不允许 char/4 (1A.0.c 实测偏差最大 23.6%)."""
    return len(_ENC.encode(text))


def kb_commit_sha(kb_root: Path) -> str:
    """R-7/R-18: KB git HEAD SHA for reingest trigger detection."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=kb_root,
            capture_output=True,
            text=True,
            check=True,
            timeout=5,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
        return "unknown"


_MERMAID_FENCE = re.compile(r"^```mermaid\b", re.MULTILINE)
_CLOSE_FENCE = re.compile(r"^```\s*$", re.MULTILINE)


def find_mermaid_blocks(text: str) -> list[tuple[int, int]]:
    """L-1 状态机: return (start, end) byte offsets for ```mermaid ... ``` blocks.

    0 嵌套 verified by 1A.0.b (29 mermaid / 58 fence in 5 files, all balanced).
    Inclusive of opening/closing fence lines.
    """
    blocks: list[tuple[int, int]] = []
    cursor = 0
    while True:
        m = _MERMAID_FENCE.search(text, cursor)
        if not m:
            break
        start = m.start()
        close = _CLOSE_FENCE.search(text, m.end())
        if not close:
            break  # unmatched (defensive; should not happen per 1A.0)
        blocks.append((start, close.end()))
        cursor = close.end()
    return blocks


_PIPE_LINE_RE = re.compile(r"^\|.*\|\s*$")
_TABLE_SEP_RE = re.compile(r"^\|[\s\-:|]+\|\s*$")


def find_table_blocks(text: str) -> list[tuple[int, int]]:
    """L-2 simple regex: return (start, end) byte offsets for GFM pipe-table blocks.

    0 HTML rowspan/colspan/<table> verified by 1A.0.b — only GFM pipe-table syntax.
    Detection: continuous |...| lines with separator |---|---| on the second row.
    """
    lines = text.splitlines(keepends=True)
    offsets = [0]
    for ln in lines:
        offsets.append(offsets[-1] + len(ln))

    blocks: list[tuple[int, int]] = []
    i = 0
    while i < len(lines):
        cur = lines[i].rstrip("\n")
        if _PIPE_LINE_RE.match(cur) and i + 1 < len(lines):
            nxt = lines[i + 1].rstrip("\n")
            if _TABLE_SEP_RE.match(nxt):
                start_line = i
                j = i + 2
                while j < len(lines) and _PIPE_LINE_RE.match(lines[j].rstrip("\n")):
                    j += 1
                blocks.append((offsets[start_line], offsets[j]))
                i = j
                continue
        i += 1
    return blocks


def is_inside_block(pos: int, blocks: list[tuple[int, int]]) -> bool:
    for s, e in blocks:
        if s <= pos < e:
            return True
    return False


def heading_positions(text: str, level: int) -> list[tuple[int, str]]:
    """Return (byte_offset, heading_text) for each ATX heading of given level (1-6).

    `heading_text` is the line content after the leading `#` chars (stripped).
    Headings inside protected blocks (mermaid/table) are NOT excluded here; caller filters.
    """
    pattern = re.compile(rf"^{'#' * level}\s+(.+?)\s*$", re.MULTILINE)
    return [(m.start(), m.group(1)) for m in pattern.finditer(text)]


@dataclass
class Chunk:
    """Chunk metadata schema (PLAN §7).

    F-15 v0.2 lock: 所有字段 fill, 不适用存 None — 不省略.
    PLAN spec 用 'class' 字段; 此处 Python reserved word → field 名 `cdisc_class`,
    to_metadata() 在导出时 rename → 'class' to match Chroma metadata convention.
    """

    source: str
    text: str
    chunk_index: int
    file_type: str

    domain: str | None = None
    cdisc_class: str | None = None
    section: str | None = None
    cdisc_section_id: str | None = None
    example_index: int | None = None
    sub_label: str | None = None
    has_mermaid: bool | None = None
    has_table: bool | None = None
    ct_code: str | None = None
    ct_extensible: bool | None = None
    part_index: int | None = None
    table_chunk_idx: int | None = None
    chunk_size_tokens: int | None = None

    kb_commit_sha: str | None = None
    ingest_at: str | None = None

    def to_metadata(self) -> dict:
        """Export to Chroma-friendly metadata dict (rename cdisc_class -> class; drop 'text')."""
        d = asdict(self)
        d.pop("text")
        d["class"] = d.pop("cdisc_class")
        return d


class BaseChunker(ABC):
    """Base for file-type-specific chunkers.

    Subclasses set `file_type` (class attribute) and implement `chunk(file_path)`.
    Use `_new_chunk(**fields)` to auto-fill kb_commit_sha + ingest_at + chunk_size_tokens.
    """

    file_type: str = "unknown"

    def __init__(self, kb_root: Path) -> None:
        self.kb_root = Path(kb_root)
        self._kb_sha: str | None = None
        self._ingest_at: str = date.today().isoformat()

    @property
    def kb_sha(self) -> str:
        if self._kb_sha is None:
            self._kb_sha = kb_commit_sha(self.kb_root)
        return self._kb_sha

    @abstractmethod
    def chunk(self, file_path: Path) -> list[Chunk]:
        """Parse file_path → list of Chunk."""
        raise NotImplementedError

    def _new_chunk(self, **kwargs) -> Chunk:
        kwargs.setdefault("kb_commit_sha", self.kb_sha)
        kwargs.setdefault("ingest_at", self._ingest_at)
        kwargs.setdefault("file_type", self.file_type)
        if "chunk_size_tokens" not in kwargs and "text" in kwargs:
            kwargs["chunk_size_tokens"] = count_tokens(kwargs["text"])
        return Chunk(**kwargs)
