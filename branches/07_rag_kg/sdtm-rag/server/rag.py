"""RAG engine: Chroma retrieval + context formatting + system prompt.

PLAN §5 Phase 1B.1-1B.2:
- ROUTING.md + INDEX.md whole-file system prompt injection (A-2)
- Chroma semantic Top-K=15 with optional metadata filters
"""
from __future__ import annotations

import copy
import sys
import time
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
    rerank_score: float | None = None  # T2: Cohere relevance score (None if rerank off)


class RAGEngine:
    def __init__(
        self,
        chroma_dir: Path,
        kb_root: Path,
        collection_name: str,
        embedding_model: str,
        top_k: int = 15,
        rerank_enabled: bool = False,
        rerank_model: str = "rerank-v3.5",
        rerank_candidates: int = 100,
        query_expansion: str = "none",
        expansion_model: str = "deepseek/deepseek-chat",
        expansion_n_queries: int = 4,
    ):
        self.client = chromadb.PersistentClient(path=str(chroma_dir))
        self.collection = self.client.get_collection(collection_name)
        space = (self.collection.metadata or {}).get("hnsw:space", "cosine")
        if space != "cosine":
            raise ValueError(f"Expected cosine distance, got {space}")
        self.kb_root = kb_root
        self.embedding_model = embedding_model
        self.top_k = top_k

        # T2 rerank: wide retrieve -> Cohere rerank -> top_k.
        self.rerank_enabled = rerank_enabled
        self.rerank_model = rerank_model
        self.rerank_candidates = rerank_candidates
        self._cohere = None
        if rerank_enabled:
            import cohere  # lazy: only required when rerank is on

            self._cohere = cohere.ClientV2()  # reads COHERE_API_KEY from env

        # T4 query expansion: rewrite the query (multiquery/hyde) before searching.
        # hyde_rrf fuses the ORIGINAL query's cosine hits with the HyDE doc's hits
        # (augment, not replace) so easy categories keep their baseline wins.
        if query_expansion not in ("none", "multiquery", "hyde", "hyde_rrf"):
            raise ValueError(
                f"query_expansion must be none|multiquery|hyde|hyde_rrf, got {query_expansion}"
            )
        self.query_expansion = query_expansion
        self.expansion_model = expansion_model
        self.expansion_n_queries = expansion_n_queries

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
        where = self._build_where(domain, file_type)

        # T4 query expansion: rewrite the query, keep cosine ordering.
        if self.query_expansion == "multiquery":
            queries = self._expand_queries(query)
            # each sub-query retrieves a deeper slice so RRF has signal to fuse
            per_q = max(k, 30)
            result_lists = [self._search(q, per_q, where) for q in queries]
            return self._rrf_fuse(result_lists, k)
        if self.query_expansion == "hyde":
            hypo = self._hypothetical_doc(query)
            return self._search(hypo, k, where)[:k]
        if self.query_expansion == "hyde_rrf":
            # Augment, not replace: fuse the original query's cosine hits with the
            # HyDE doc's hits so easy categories keep their strong baseline ranking.
            hypo = self._hypothetical_doc(query)
            per_q = max(k, 30)
            lists = [
                self._search(query, per_q, where),
                self._search(hypo, per_q, where),
            ]
            return self._rrf_fuse(lists, k)

        # Single-query path (+ optional T2 rerank). When rerank is on, pull a wide
        # candidate pool, then let the reranker pick k. Pool never smaller than k.
        pool = max(self.rerank_candidates, k) if self.rerank_enabled else k
        chunks = self._search(query, pool, where)
        if self.rerank_enabled and chunks:
            return self._rerank(query, chunks, k)
        return chunks[:k]

    @staticmethod
    def _build_where(domain: str | None, file_type: str | None) -> dict | None:
        conditions: list[dict] = []
        if domain:
            conditions.append({"domain": domain})
        if file_type:
            conditions.append({"file_type": file_type})
        if len(conditions) == 1:
            return conditions[0]
        if len(conditions) > 1:
            return {"$and": conditions}
        return None

    def _search(
        self, query_text: str, n: int, where: dict | None
    ) -> list[RetrievedChunk]:
        """Embed `query_text`, cosine-search Chroma, return up to `n` chunks."""
        resp = litellm.embedding(model=self.embedding_model, input=[query_text])
        query_emb = resp.data[0]["embedding"]

        result = self.collection.query(
            query_embeddings=[query_emb],
            n_results=n,
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

    def _rerank(
        self, query: str, chunks: list[RetrievedChunk], k: int
    ) -> list[RetrievedChunk]:
        """Cohere rerank the candidate pool by query relevance, keep top k.

        Returns shallow copies (never mutates the input chunks) with each copy's
        `rerank_score` set; original cosine `similarity` is preserved.

        Intentionally NO fallback to un-reranked results: if rerank keeps failing
        the exception propagates so a degraded run is never silently scored as if
        reranked. Rate-limit (429) errors are retried with exponential backoff
        (trial keys are throttled), other errors re-raise immediately.
        """
        resp = None
        for attempt in range(5):
            try:
                resp = self._cohere.rerank(
                    model=self.rerank_model,
                    query=query,
                    documents=[c.text for c in chunks],
                    top_n=min(k, len(chunks)),
                    max_tokens_per_doc=4096,  # pin behavior; chunks are <=~2.7k tok
                )
                break
            except Exception as exc:
                msg = str(exc).lower()
                is_rate = "rate" in msg or "429" in msg or "too many" in msg
                if is_rate and attempt < 4:
                    time.sleep(min(60, 10 * (2 ** attempt)))
                    continue
                raise

        reranked: list[RetrievedChunk] = []
        for item in resp.results:
            c = copy.copy(chunks[item.index])  # don't mutate shared chunk objects
            c.rerank_score = round(item.relevance_score, 4)
            reranked.append(c)
        return reranked

    # ---- T4 query expansion -------------------------------------------------

    _MULTIQUERY_SYS = (
        "You help search an SDTM (CDISC clinical data standard) knowledge base. "
        "Given a user question, write alternative search queries that together "
        "retrieve ALL relevant source documents. Decompose multi-part or cross-domain "
        "questions into focused sub-queries (one domain/concept each). Use precise SDTM "
        "terminology, variable names, and controlled-terminology codelist names where "
        "relevant. Output ONLY the queries, one per line, no numbering or commentary."
    )
    _HYDE_SYS = (
        "You write a short hypothetical passage that would directly answer a question "
        "about the SDTM (CDISC clinical data standard), as if extracted from the CDISC "
        "SDTMIG. 3-5 sentences. Use precise SDTM terminology, variable names, and "
        "controlled-terminology codelist codes (e.g. C66742) where applicable. Output "
        "only the passage."
    )

    def _llm(self, system: str, user: str) -> str:
        """Expansion LLM call with rate-limit retry/backoff (trial keys throttle).
        Non-rate errors re-raise immediately so the caller's fallback handles them."""
        for attempt in range(5):
            try:
                resp = litellm.completion(
                    model=self.expansion_model,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    temperature=0.0,
                )
                return resp.choices[0].message.content or ""
            except Exception as exc:
                msg = str(exc).lower()
                if ("rate" in msg or "429" in msg or "too many" in msg) and attempt < 4:
                    time.sleep(min(60, 10 * (2 ** attempt)))
                    continue
                raise

    def _expand_queries(self, query: str) -> list[str]:
        """LLM-decompose into sub-queries. Always includes the original query.

        On LLM/parse failure, degrades to [query] (plain single-query) and prints a
        VISIBLE warning to stderr — never silent. The degradation cannot inflate
        recall (fewer queries -> at most the cosine baseline), and the warning lets
        the eval log reveal if expansion was actually exercised.
        """
        queries = [query]
        try:
            want = max(1, self.expansion_n_queries - 1)
            out = self._llm(self._MULTIQUERY_SYS, f"Question: {query}\n\nWrite {want} queries.")
            for line in out.splitlines():
                line = line.strip().lstrip("0123456789.-) ").strip()
                if line and line.lower() != query.lower():
                    queries.append(line)
        except Exception as exc:
            print(f"[T4 multiquery fallback -> single-query] {exc}", file=sys.stderr)
        return queries[: self.expansion_n_queries]

    def _hypothetical_doc(self, query: str) -> str:
        """HyDE: LLM writes a hypothetical answer; embed THAT. Falls back to the raw
        query on failure (degrades to single-query) with a VISIBLE stderr warning."""
        try:
            hypo = self._llm(self._HYDE_SYS, f"Question: {query}").strip()
            return hypo or query
        except Exception as exc:
            print(f"[T4 hyde fallback -> raw query] {exc}", file=sys.stderr)
            return query

    def _rrf_fuse(
        self, result_lists: list[list[RetrievedChunk]], k: int, c: int = 60
    ) -> list[RetrievedChunk]:
        """Reciprocal Rank Fusion across per-sub-query result lists.

        score(doc) = sum over lists of 1/(c + rank). Keeps the highest-cosine copy
        of each chunk for context display. Returns top-k by fused score.
        """
        scores: dict[str, float] = {}
        best: dict[str, RetrievedChunk] = {}
        for lst in result_lists:
            for rank, ch in enumerate(lst):
                scores[ch.chunk_id] = scores.get(ch.chunk_id, 0.0) + 1.0 / (c + rank + 1)
                if ch.chunk_id not in best or ch.similarity > best[ch.chunk_id].similarity:
                    best[ch.chunk_id] = ch
        ranked = sorted(scores, key=lambda cid: scores[cid], reverse=True)
        return [best[cid] for cid in ranked[:k]]

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
