"""sdtm-rag chunker package — Phase 1A.3 implementation complete.

8 modules: 1 base + 7 file-type-specific chunkers, each subclasses BaseChunker
and produces Chunk instances per PLAN §7 metadata schema (18 fields).

Config locks (1A.0.b/c verified, phase_1a_0_sanity.md §4):
- L-1 mermaid 状态机 (0 嵌套)
- L-2 GFM pipe-table 简单 regex (0 HTML)
- L-3 tiktoken cl100k_base 实测强制
- L-4 chapters/ >=50KB 强制 ^### 切
- L-5 terminology core part H2=1 -> part 模式 / H2>1 -> codelist 模式

Phase 1A.3 batch ownership:
- main session: base.py
- Batch A executor (sonnet): spec.py + assumptions.py + model.py
- Batch B executor (opus): examples.py (domain-aware + mermaid/table protection)
- Batch C executor (opus): chapters.py + terminology.py + variable_index.py

Integration smoke (1A.3 closure): 10/10 samples PASS.
Phase 1A.4 (test-engineer) writes comprehensive test suite next.
"""

from __future__ import annotations

from .assumptions import AssumptionsChunker
from .base import (
    BaseChunker,
    Chunk,
    count_tokens,
    find_mermaid_blocks,
    find_table_blocks,
    heading_positions,
    is_inside_block,
    kb_commit_sha,
)
from .chapters import ChaptersChunker
from .examples import ExamplesChunker
from .model import ModelChunker
from .spec import SpecChunker
from .terminology import TerminologyChunker
from .variable_index import VariableIndexChunker

# Registry: file_type → chunker class. Used by ingest.py to dispatch.
CHUNKER_REGISTRY: dict[str, type[BaseChunker]] = {
    SpecChunker.file_type: SpecChunker,
    AssumptionsChunker.file_type: AssumptionsChunker,
    ModelChunker.file_type: ModelChunker,
    ExamplesChunker.file_type: ExamplesChunker,
    ChaptersChunker.file_type: ChaptersChunker,
    TerminologyChunker.file_type: TerminologyChunker,
    VariableIndexChunker.file_type: VariableIndexChunker,
}

__all__ = [
    "AssumptionsChunker",
    "BaseChunker",
    "CHUNKER_REGISTRY",
    "ChaptersChunker",
    "Chunk",
    "ExamplesChunker",
    "ModelChunker",
    "SpecChunker",
    "TerminologyChunker",
    "VariableIndexChunker",
    "count_tokens",
    "find_mermaid_blocks",
    "find_table_blocks",
    "heading_positions",
    "is_inside_block",
    "kb_commit_sha",
]
