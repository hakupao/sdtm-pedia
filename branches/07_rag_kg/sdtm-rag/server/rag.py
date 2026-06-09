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
    via_lookup: bool = False  # S1: chunk union-added by deterministic structured-lookup


class RAGEngine:
    # When structured-lookup resolves to EXACTLY ONE domain spec.md (a pure
    # single-domain query, e.g. "the required variables in DM"), inject this many of
    # that file's chunks instead of just the single best one, so the answering model
    # has enough variable rows to ENUMERATE rather than punt. See
    # _apply_structured_lookup for the rationale and the narrow trigger condition.
    _SINGLE_DOMAIN_SPEC_CHUNKS = 4

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
        structured_lookup_enabled: bool = False,
        hybrid_enabled: bool = False,
        hybrid_fusion: str = "rrf",
        hybrid_alpha: float = 0.5,
        hybrid_pool: int = 30,
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

        # S1 structured lookup: deterministic var/CT-code -> gold file resolution,
        # union-added ahead of cosine for query classes embeddings can't reach.
        self.structured_lookup_enabled = structured_lookup_enabled
        self._structured_lookup = None
        if structured_lookup_enabled:
            from server.structured_lookup import StructuredLookup  # lazy: off by default

            self._structured_lookup = StructuredLookup(kb_root)

        # S2 hybrid BM25: lexical retrieval over the SAME 4146 chunks already in the
        # collection (no re-ingest, no embedding change), additively fused with dense
        # cosine so literal-token hits (domain/relationship/variable names) that
        # cosine buries get re-floated WITHOUT demoting cosine's existing wins.
        if hybrid_fusion not in ("rrf", "weighted"):
            raise ValueError(f"hybrid_fusion must be rrf|weighted, got {hybrid_fusion}")
        self.hybrid_enabled = hybrid_enabled
        self.hybrid_fusion = hybrid_fusion
        self.hybrid_alpha = hybrid_alpha  # weighted only: dense weight (1-alpha=BM25)
        # Fusion pool depth per list. 30 (vs k=15) is the robust empirical sweet
        # spot on v2: deep enough to fuse the literal-token golds BM25 surfaces
        # (q09/q10/q32/q33 spec rows, concept q38/q39), shallow enough that deep
        # BM25 tail noise does not re-float and displace already-found golds.
        # Pools 50/75/100 each regressed >=1 question (q38/q08) for at most one
        # marginal gain (q73), so a deeper pool is NOT robust — kept at 30.
        self.hybrid_pool = hybrid_pool
        self._bm25 = None
        self._bm25_chunk_ids: list[str] = []
        self._bm25_chunk_meta: dict[str, dict] = {}
        if hybrid_enabled:
            self._build_bm25_index()

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

        # Embed the ORIGINAL query at most once and reuse the vector across the
        # dense search and every S1 lookup search (each previously re-embedded the
        # identical query text — up to ~6 redundant OpenAI round-trips per call).
        # Skipped only on the pure-hyde path with no S1, where the original query is
        # never searched (hyde embeds the hypothetical doc instead).
        need_q_emb = self._structured_lookup is not None or self.query_expansion != "hyde"
        q_emb = self._embed_query(query) if need_q_emb else None

        # T4 query expansion: rewrite the query, keep cosine ordering.
        if self.query_expansion == "multiquery":
            queries = self._expand_queries(query)
            # each sub-query retrieves a deeper slice so RRF has signal to fuse;
            # the original query (queries[0]) reuses the precomputed embedding.
            per_q = max(k, 30)
            result_lists = [
                self._search(q, per_q, where, query_embedding=(q_emb if q == query else None))
                for q in queries
            ]
            cosine = self._rrf_fuse(result_lists, k)
        elif self.query_expansion == "hyde":
            hypo = self._hypothetical_doc(query)
            cosine = self._search(hypo, k, where)[:k]
        elif self.query_expansion == "hyde_rrf":
            # Augment, not replace: fuse the original query's cosine hits with the
            # HyDE doc's hits so easy categories keep their strong baseline ranking.
            hypo = self._hypothetical_doc(query)
            per_q = max(k, 30)
            lists = [
                self._search(query, per_q, where, query_embedding=q_emb),
                self._search(hypo, per_q, where),
            ]
            cosine = self._rrf_fuse(lists, k)
        elif self.hybrid_enabled:
            # S2 hybrid: dense top-N + BM25 top-N, additively fused (RRF/weighted).
            # Both lists are deeper than k so a chunk that is strong in EITHER signal
            # surfaces; fusion is additive so a chunk strong in BOTH is reinforced
            # (the structured spec chunks the literal-token questions need).
            pool = max(k, self.hybrid_pool)
            dense = self._search(query, pool, where, query_embedding=q_emb)
            bm25 = self._bm25_search(query, pool, where)
            cosine = self._hybrid_fuse(dense, bm25, k)
        else:
            # Single-query path (+ optional T2 rerank). When rerank is on, pull a
            # wide candidate pool, then let the reranker pick k. Pool never < k.
            pool = max(self.rerank_candidates, k) if self.rerank_enabled else k
            chunks = self._search(query, pool, where, query_embedding=q_emb)
            if self.rerank_enabled and chunks:
                cosine = self._rerank(query, chunks, k)
            else:
                cosine = chunks[:k]

        if self._structured_lookup is not None:
            return self._apply_structured_lookup(query, cosine, where, k, query_embedding=q_emb)
        return cosine[:k]

    def _apply_structured_lookup(
        self,
        query: str,
        cosine: list[RetrievedChunk],
        where: dict | None,
        k: int,
        query_embedding: list[float] | None = None,
    ) -> list[RetrievedChunk]:
        """S1 union-add: resolve gold files deterministically, pull the single most
        query-relevant chunk from each, prepend them, then fill with cosine results
        (de-duped) up to k. Lookup chunks go first so they cannot be crowded out;
        cosine ordering of everything else is preserved. No-op when resolve()=[].
        `query_embedding` (the precomputed original-query vector) is reused for every
        per-file lookup search so S1 adds no extra embedding round-trips."""
        targets = self._structured_lookup.resolve(query)
        if not targets:
            return cosine[:k]

        # Single-domain enrichment: when resolve() returns exactly ONE target and it
        # is a domain's spec.md, this is a pure single-domain ask ("required variables
        # in DM"). Injecting only the single best spec chunk lets hybrid/relationship
        # chunks crowd the remaining per-variable spec rows out of top-k, so the model
        # can't enumerate and punts (observed q02 regression). Inject several chunks
        # from that one file instead. Multi-target queries keep 1 chunk per file so
        # they never flood. Source recall is unchanged (the gold file is found either
        # way) — this only enriches composition for the answering model.
        single_spec = len(targets) == 1 and self._is_domain_spec(targets[0])

        lookup_chunks: list[RetrievedChunk] = []
        for rel_path in targets:
            n = self._SINGLE_DOMAIN_SPEC_CHUNKS if single_spec else 1
            for chunk in self._lookup_chunks_for_file(
                query, rel_path, n, query_embedding=query_embedding
            ):
                chunk.via_lookup = True
                lookup_chunks.append(chunk)

        if not lookup_chunks:
            return cosine[:k]

        merged: list[RetrievedChunk] = []
        seen_ids: set[str] = set()
        for ch in lookup_chunks + cosine:
            if ch.chunk_id in seen_ids:
                continue
            seen_ids.add(ch.chunk_id)
            merged.append(ch)
        return merged[:k]

    @staticmethod
    def _is_domain_spec(rel_path: str) -> bool:
        """True for a domains/<CODE>/spec.md path (the per-variable spec file)."""
        return rel_path.startswith("domains/") and rel_path.endswith("/spec.md")

    def _lookup_chunks_for_file(
        self, query: str, rel_path: str, n: int,
        query_embedding: list[float] | None = None,
    ) -> list[RetrievedChunk]:
        """Up to `n` best (highest query-cosine) chunks whose source is exactly
        `rel_path`. Filters Chroma on the absolute source path, reusing the precomputed
        query embedding (no fresh embedding call) so the injected chunks are the most
        relevant slices of that file. Empty list if the file has no chunks."""
        abs_source = str((self.kb_root / rel_path).resolve())
        return self._search(query, n, {"source": abs_source}, query_embedding=query_embedding)

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

    def _embed_query(self, text: str) -> list[float]:
        """Embed `text` via the configured embedding model. Factored out so the
        original query's vector can be computed once per retrieve() call and reused
        by the dense search and every S1 lookup (which otherwise each re-embed the
        identical query). Deterministic for a given input, so reuse is exact.

        This is now the single chokepoint for all query-embedding traffic, so it
        carries the same 429 backoff as _llm/_rerank: rate-limit errors retry with
        exponential backoff, other errors re-raise immediately (the /ask handler
        turns the propagated failure into a visible 502, never a silent degrade)."""
        for attempt in range(5):
            try:
                resp = litellm.embedding(model=self.embedding_model, input=[text])
                return resp.data[0]["embedding"]
            except Exception as exc:
                msg = str(exc).lower()
                if ("rate" in msg or "429" in msg or "too many" in msg) and attempt < 4:
                    time.sleep(min(60, 10 * (2 ** attempt)))
                    continue
                raise

    def _search(
        self,
        query_text: str,
        n: int,
        where: dict | None,
        query_embedding: list[float] | None = None,
    ) -> list[RetrievedChunk]:
        """Cosine-search Chroma for up to `n` chunks. Embeds `query_text` unless a
        precomputed `query_embedding` is supplied (reused to avoid redundant calls)."""
        query_emb = (
            query_embedding if query_embedding is not None else self._embed_query(query_text)
        )

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

    # ---- S2 hybrid BM25 -----------------------------------------------------

    def _build_bm25_index(self) -> None:
        """Build a BM25 inverted index over the chunks ALREADY in the collection.

        Pulls all documents + metadata via collection.get() (no re-ingest, no
        embedding touch), tokenizes the chunk texts, and indexes them. The aligned
        chunk_id list lets _bm25_search map BM25 doc indices back to chunk_ids; the
        metadata cache lets it build RetrievedChunk objects without a second query.
        """
        import bm25s  # lazy: only required when hybrid is on

        got = self.collection.get(include=["documents", "metadatas"])
        ids = got["ids"]
        docs = got["documents"]
        metas = got["metadatas"]

        self._bm25_chunk_ids = list(ids)
        self._bm25_chunk_meta = {
            cid: {"text": docs[i], "meta": metas[i]} for i, cid in enumerate(ids)
        }
        corpus_tokens = bm25s.tokenize(docs, show_progress=False)
        self._bm25 = bm25s.BM25()
        self._bm25.index(corpus_tokens, show_progress=False)

    def _bm25_search(
        self, query_text: str, n: int, where: dict | None
    ) -> list[RetrievedChunk]:
        """Lexical BM25 retrieval over the indexed chunks; up to `n` results.

        `where` (domain/file_type) is applied as a post-filter so BM25 obeys the
        same scoping as dense search. similarity carries the BM25 score so fusion
        and display have a value (it is NOT a cosine; only used for ranking signal).
        """
        import bm25s  # lazy

        query_tokens = bm25s.tokenize(query_text, show_progress=False)
        # over-fetch so the post-filter still yields ~n survivors
        k = min(len(self._bm25_chunk_ids), max(n * 4, n))
        results, scores = self._bm25.retrieve(
            query_tokens, k=k, show_progress=False
        )

        out: list[RetrievedChunk] = []
        for doc_idx, score in zip(results[0], scores[0], strict=False):
            chunk_id = self._bm25_chunk_ids[doc_idx]
            entry = self._bm25_chunk_meta[chunk_id]
            meta = entry["meta"]
            if where and not self._meta_matches_where(meta, where):
                continue
            source_raw = meta.get("source", "")
            try:
                source = Path(source_raw).relative_to(self.kb_root).as_posix()
            except (ValueError, TypeError):
                source = source_raw
            out.append(
                RetrievedChunk(
                    chunk_id=chunk_id,
                    source=source,
                    domain=meta.get("domain"),
                    file_type=meta.get("file_type"),
                    section=meta.get("section"),
                    similarity=round(float(score), 4),
                    text=entry["text"],
                )
            )
            if len(out) >= n:
                break
        return out

    @staticmethod
    def _meta_matches_where(meta: dict, where: dict) -> bool:
        """Replicate the (small) subset of Chroma `where` filters we emit
        (_build_where only produces flat eq conditions and a top-level $and)."""
        if "$and" in where:
            return all(
                RAGEngine._meta_matches_where(meta, cond) for cond in where["$and"]
            )
        return all(meta.get(key) == val for key, val in where.items())

    def _hybrid_fuse(
        self,
        dense: list[RetrievedChunk],
        bm25: list[RetrievedChunk],
        k: int,
    ) -> list[RetrievedChunk]:
        """Additively fuse dense + BM25 rankings. RRF (default, parameter-free) or
        weighted (min-max normalized, dense weight = alpha). Additive, never
        replacement: a chunk strong in EITHER list ranks; strong in BOTH is
        reinforced. Returns top-k, preferring the dense copy for display."""
        best: dict[str, RetrievedChunk] = {}
        for ch in dense + bm25:
            # keep dense copy when both present (carries the cosine similarity)
            best.setdefault(ch.chunk_id, ch)
        for ch in dense:
            best[ch.chunk_id] = ch  # dense copy wins display

        if self.hybrid_fusion == "rrf":
            c = 60
            scores: dict[str, float] = {}
            for lst in (dense, bm25):
                for rank, ch in enumerate(lst):
                    scores[ch.chunk_id] = scores.get(ch.chunk_id, 0.0) + 1.0 / (c + rank + 1)
        else:  # weighted: min-max normalize each list's scores, then alpha-blend
            scores = {}
            for lst, weight in ((dense, self.hybrid_alpha), (bm25, 1.0 - self.hybrid_alpha)):
                if not lst:
                    continue
                vals = [c.similarity for c in lst]
                lo, hi = min(vals), max(vals)
                span = hi - lo or 1.0
                for ch in lst:
                    norm = (ch.similarity - lo) / span
                    scores[ch.chunk_id] = scores.get(ch.chunk_id, 0.0) + weight * norm

        ranked = sorted(scores, key=lambda cid: scores[cid], reverse=True)
        return [best[cid] for cid in ranked[:k]]

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
