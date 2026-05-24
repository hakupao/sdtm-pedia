"""RAG engine: Chroma retrieval + context formatting + system prompt.

PLAN §5 Phase 1B.1-1B.2:
- ROUTING.md + INDEX.md whole-file system prompt injection (A-2)
- Chroma semantic Top-K=15 with optional metadata filters
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import chromadb
import litellm


@dataclass
class RetrievedChunk:
    chunk_id: str
    source: str
    domain: str | None
    file_type: str | None
    section: str | None
    similarity: float
    text: str


class RAGEngine:
    def __init__(
        self,
        chroma_dir: Path,
        kb_root: Path,
        collection_name: str,
        embedding_model: str,
        top_k: int = 15,
    ):
        self.client = chromadb.PersistentClient(path=str(chroma_dir))
        self.collection = self.client.get_collection(collection_name)
        space = (self.collection.metadata or {}).get("hnsw:space", "cosine")
        if space != "cosine":
            raise ValueError(f"Expected cosine distance, got {space}")
        self.kb_root = kb_root
        self.embedding_model = embedding_model
        self.top_k = top_k

        routing_path = kb_root / "ROUTING.md"
        index_path = kb_root / "INDEX.md"
        if not routing_path.exists():
            raise FileNotFoundError(f"ROUTING.md not found: {routing_path}")
        if not index_path.exists():
            raise FileNotFoundError(f"INDEX.md not found: {index_path}")

        self._routing_md = routing_path.read_text(encoding="utf-8")
        self._index_md = index_path.read_text(encoding="utf-8")
        self._system_prompt = self._build_system_prompt()

    @property
    def system_prompt(self) -> str:
        return self._system_prompt

    def _build_system_prompt(self) -> str:
        return (
            "You are an SDTM (Study Data Tabulation Model) knowledge base assistant.\n"
            "Answer questions based on the CDISC SDTMIG v3.4 knowledge base.\n\n"
            "## Rules\n"
            "1. Answer based on the provided context. "
            "If context is insufficient, say so explicitly.\n"
            "2. Cite sources using **[Source: path]** for each claim.\n"
            "3. Be precise and technical -- your audience knows SDTM.\n"
            "4. For variable definitions, include Label, Type, Role, Core, "
            "and Controlled Terms.\n"
            "5. For terminology questions, reference the codelist code "
            "(e.g., C66742).\n"
            "6. When multiple sources are relevant, synthesize across them.\n\n"
            "---\n\n"
            "## Routing Guide\n\n"
            f"{self._routing_md}\n\n"
            "---\n\n"
            "## Knowledge Base Index\n\n"
            f"{self._index_md}"
        )

    def retrieve(
        self,
        query: str,
        *,
        domain: str | None = None,
        file_type: str | None = None,
        top_k: int | None = None,
    ) -> list[RetrievedChunk]:
        k = top_k or self.top_k

        resp = litellm.embedding(model=self.embedding_model, input=[query])
        query_emb = resp.data[0]["embedding"]

        where: dict | None = None
        conditions: list[dict] = []
        if domain:
            conditions.append({"domain": domain})
        if file_type:
            conditions.append({"file_type": file_type})
        if len(conditions) == 1:
            where = conditions[0]
        elif len(conditions) > 1:
            where = {"$and": conditions}

        result = self.collection.query(
            query_embeddings=[query_emb],
            n_results=k,
            where=where,
            include=["documents", "metadatas", "distances"],
        )

        chunks: list[RetrievedChunk] = []
        if not result["ids"] or not result["ids"][0]:
            return chunks

        for i, chunk_id in enumerate(result["ids"][0]):
            dist = result["distances"][0][i]
            meta = result["metadatas"][0][i]
            text = result["documents"][0][i]
            source_raw = meta.get("source", "")
            try:
                source = Path(source_raw).relative_to(self.kb_root).as_posix()
            except (ValueError, TypeError):
                source = source_raw
            chunks.append(
                RetrievedChunk(
                    chunk_id=chunk_id,
                    source=source,
                    domain=meta.get("domain"),
                    file_type=meta.get("file_type"),
                    section=meta.get("section"),
                    similarity=round(1.0 - dist, 4),
                    text=text,
                )
            )
        return chunks

    def format_context(self, chunks: list[RetrievedChunk]) -> str:
        if not chunks:
            return "(No relevant context found in the knowledge base.)"
        parts: list[str] = []
        for i, c in enumerate(chunks, 1):
            header = f"### [{i}] {c.source}"
            if c.section:
                header += f" -- {c.section}"
            header += f"  (similarity: {c.similarity:.3f})"
            text = c.text if len(c.text) <= 4000 else c.text[:4000] + "\n...(truncated)"
            parts.append(f"{header}\n\n{text}")
        return "\n\n---\n\n".join(parts)

    def build_messages(
        self,
        question: str,
        context: str,
        history: list[dict] | None = None,
    ) -> list[dict]:
        messages: list[dict] = [{"role": "system", "content": self.system_prompt}]
        if history:
            messages.extend(history)
        user_content = (
            "## Retrieved Context\n\n"
            f"{context}\n\n"
            "---\n\n"
            f"## Question\n\n{question}"
        )
        messages.append({"role": "user", "content": user_content})
        return messages
