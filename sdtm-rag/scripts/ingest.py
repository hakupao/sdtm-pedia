"""ingest.py — Phase 1A.5 offline full-KB ingest pipeline.

Refs:
- PLAN §6 (chunker dispatch) + §7 (Chunk metadata) + §4.4 (R-16 backup, R-18 KB SHA trigger)
- EXECUTION_PLAN §1A.5.a (ingest_full)
- D-4 v3: embedding = OpenAI text-embedding-3-small (1536d, cloud API via LiteLLM)

Pipeline:
  1. Scan KB_ROOT → bucket files by file_type via detect_file_type()
     - INDEX.md / ROUTING.md skipped (system prompt only)
  2. Dispatch each file to CHUNKER_REGISTRY[file_type] → flat list of Chunk
  3. Backup existing data/chroma/ (if non-empty payload) → data/chroma_backup_<ts>/
     then reset only collection 'sdtm_kb_v1' (--full-reset wipes the whole dir)
  4. Embed all chunk texts via OpenAI text-embedding-3-small (LiteLLM, batch=100)
  5. PersistentClient → collection 'sdtm_kb_v1', add(embeddings, documents, metadatas, ids)
  6. Write data/chroma/ingested_at_commit.txt (R-18)
  7. Print per-file_type chunk counts, total tokens, wallclock, persist size

Run:
  python3 scripts/ingest.py [--retrieval-sanity]
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# Repo paths (script lives at sdtm-rag/scripts/ingest.py)
SDTM_RAG_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = SDTM_RAG_ROOT.parent  # sdtm-rag → repo root
KB_ROOT = REPO_ROOT / "knowledge_base"
CHROMA_DIR = SDTM_RAG_ROOT / "data" / "chroma"

# Inject sdtm-rag root so `from scripts.chunkers import ...` resolves.
sys.path.insert(0, str(SDTM_RAG_ROOT))

import chromadb  # noqa: E402
import litellm  # noqa: E402

from scripts.chunkers import CHUNKER_REGISTRY, Chunk  # noqa: E402
from scripts.chunkers.base import count_tokens, kb_commit_sha  # noqa: E402

COLLECTION_NAME = "sdtm_kb_v1"
EMBED_MODEL_NAME = "text-embedding-3-small"
EMBED_DIM = 1536
EMBED_BATCH_SIZE = 100  # OpenAI supports up to 2048 inputs per call; 100 is conservative
EMBED_MAX_TOKENS = 8191  # text-embedding-3-small hard limit


# ── File-type detection (PLAN §6 + task spec) ─────────────────────────────
def detect_file_type(p: Path) -> str | None:
    """Map a KB file to its chunker file_type, or None if not chunked.

    System-prompt files (INDEX.md / ROUTING.md) → None (system prompt only).
    Unknown paths → None (skipped with WARN).
    """
    rel = p.relative_to(KB_ROOT).as_posix()
    if rel in ("INDEX.md", "ROUTING.md"):
        return None  # system prompt only, not chunked
    if rel == "VARIABLE_INDEX.md":
        return "variable_index"
    if rel.startswith("domains/"):
        fname = p.name
        if fname == "spec.md":
            return "spec"
        if fname == "assumptions.md":
            return "assumptions"
        if fname == "examples.md":
            return "examples"
        return None
    if rel.startswith("model/"):
        return "model"
    if rel.startswith("chapters/"):
        return "chapter"
    if rel.startswith("terminology/"):
        return "terminology"
    return None


# ── Chroma metadata coercion ──────────────────────────────────────────────
def _coerce_metadata(meta: dict) -> dict:
    """Chroma metadata only accepts str/int/float/bool/None.

    F-15: schema keeps all fields with None for non-applicable; Chroma 1.5.x
    accepts None natively. Drop keys with None value to keep records compact and
    avoid coercion of optional fields to empty strings.
    """
    out: dict = {}
    for k, v in meta.items():
        if v is None:
            continue
        if isinstance(v, (str, int, float, bool)):
            out[k] = v
        else:
            out[k] = str(v)
    return out


# ── R-16 backup of existing Chroma data ───────────────────────────────────
def backup_existing_chroma(chroma_dir: Path) -> Path | None:
    """If chroma_dir has any non-trivial payload (beyond .gitkeep), copy to backup dir.

    Returns the backup path or None if nothing to back up.
    """
    if not chroma_dir.exists():
        return None
    items = [p for p in chroma_dir.iterdir() if p.name != ".gitkeep"]
    if not items:
        return None
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_dir = chroma_dir.parent / f"chroma_backup_{ts}"
    backup_dir.mkdir(parents=True, exist_ok=False)
    for p in items:
        dst = backup_dir / p.name
        if p.is_dir():
            shutil.copytree(p, dst)
        else:
            shutil.copy2(p, dst)
    return backup_dir


def reset_collection(chroma_dir: Path, name: str) -> None:
    """Drop one collection only; siblings (study_*) in the same dir stay intact."""
    client = chromadb.PersistentClient(path=str(chroma_dir))
    existing = [c.name for c in client.list_collections()]
    if name in existing:
        client.delete_collection(name)


def reset_chroma_dir(chroma_dir: Path) -> None:
    """Remove all items in chroma_dir except .gitkeep (after backup).

    Destructive across collections — only reachable via --full-reset.
    """
    if not chroma_dir.exists():
        chroma_dir.mkdir(parents=True, exist_ok=True)
        return
    for p in chroma_dir.iterdir():
        if p.name == ".gitkeep":
            continue
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()


# ── Directory size helper ─────────────────────────────────────────────────
def dir_size_bytes(path: Path) -> int:
    total = 0
    for root, _dirs, files in os.walk(path):
        for f in files:
            fp = Path(root) / f
            try:
                total += fp.stat().st_size
            except OSError:
                pass
    return total


def fmt_bytes(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


# ── Chunking pass ─────────────────────────────────────────────────────────
def collect_chunks() -> tuple[list[Chunk], dict[str, int], list[Path]]:
    """Walk KB_ROOT, dispatch each file by file_type, return (chunks, per-type counts, unknown skipped)."""
    chunkers_cache: dict[str, object] = {}
    all_chunks: list[Chunk] = []
    per_type_counts: dict[str, int] = defaultdict(int)
    per_type_file_counts: dict[str, int] = defaultdict(int)
    unknown_skipped: list[Path] = []
    system_prompt_skipped: list[Path] = []

    md_files = sorted(KB_ROOT.rglob("*.md"))
    print(f"[scan] {len(md_files)} .md files under {KB_ROOT}")
    for p in md_files:
        ft = detect_file_type(p)
        if ft is None:
            rel = p.relative_to(KB_ROOT).as_posix()
            if rel in ("INDEX.md", "ROUTING.md"):
                system_prompt_skipped.append(p)
            else:
                unknown_skipped.append(p)
            continue
        cls = CHUNKER_REGISTRY.get(ft)
        if cls is None:
            print(f"[WARN] no chunker registered for file_type={ft} ({p.relative_to(KB_ROOT)})")
            unknown_skipped.append(p)
            continue
        chunker = chunkers_cache.get(ft)
        if chunker is None:
            chunker = cls(KB_ROOT)
            chunkers_cache[ft] = chunker
        chunks = chunker.chunk(p)
        all_chunks.extend(chunks)
        per_type_counts[ft] += len(chunks)
        per_type_file_counts[ft] += 1

    print(f"[scan] system-prompt skipped: {[p.name for p in system_prompt_skipped]}")
    if unknown_skipped:
        print(f"[WARN] unknown file_type, skipped {len(unknown_skipped)} files:")
        for p in unknown_skipped[:10]:
            print(f"        - {p.relative_to(KB_ROOT)}")

    print("[chunks] per-type counts:")
    for ft in sorted(per_type_counts.keys()):
        print(
            f"  {ft:>15}: {per_type_counts[ft]:>5} chunks "
            f"from {per_type_file_counts[ft]:>3} files"
        )
    print(f"  {'TOTAL':>15}: {len(all_chunks):>5} chunks "
          f"from {sum(per_type_file_counts.values()):>3} files")
    return all_chunks, dict(per_type_counts), unknown_skipped


# ── Embedding pass ────────────────────────────────────────────────────────
def _truncate_for_embedding(text: str, max_tokens: int = EMBED_MAX_TOKENS) -> tuple[str, bool]:
    """Truncate text to max_tokens using tiktoken cl100k_base. Returns (text, was_truncated)."""
    tok_count = count_tokens(text)
    if tok_count <= max_tokens:
        return text, False
    import tiktoken
    enc = tiktoken.get_encoding("cl100k_base")
    token_ids = enc.encode(text)[:max_tokens]
    return enc.decode(token_ids), True


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Batch-embed raw texts via OpenAI text-embedding-3-small (D-4 v3, LiteLLM).

    Batching is token-aware: each API call stays under 250K total tokens
    (OpenAI limit is 300K; 250K gives headroom for tokenizer divergence).
    """
    MAX_BATCH_TOKENS = 250_000
    n = len(texts)
    result_embs: list[list[float]] = [None] * n  # type: ignore[list-item]
    truncated_indices: list[int] = []
    t0 = time.perf_counter()

    # Pre-truncate and collect texts + token counts
    prepared: list[tuple[str, int]] = []
    for i, raw_text in enumerate(texts):
        text, was_truncated = _truncate_for_embedding(raw_text)
        if was_truncated:
            truncated_indices.append(i)
        tok = min(count_tokens(text), EMBED_MAX_TOKENS)
        prepared.append((text, tok))

    # Build token-aware batches
    i = 0
    while i < n:
        batch_texts: list[str] = []
        batch_start = i
        batch_tokens = 0
        while i < n and len(batch_texts) < EMBED_BATCH_SIZE:
            text, tok = prepared[i]
            if batch_tokens + tok > MAX_BATCH_TOKENS and batch_texts:
                break
            batch_texts.append(text)
            batch_tokens += tok
            i += 1
        # Retry on OpenAI TPM rate limit (429): the limit is per-minute rolling,
        # so back off and retry the same batch rather than aborting the whole ingest
        # mid-way (the reset already ran, so a crash here leaves the collection empty).
        for _attempt in range(6):
            try:
                response = litellm.embedding(model=EMBED_MODEL_NAME, input=batch_texts)
                break
            except Exception as exc:
                msg = str(exc).lower()
                if ("rate" in msg or "429" in msg or "too many" in msg) and _attempt < 5:
                    wait = min(60, 15 * (2 ** _attempt))
                    print(f"[embed] rate limit at {i}/{n}; waiting {wait}s (attempt {_attempt+1})...")
                    time.sleep(wait)
                else:
                    raise
        for item in response.data:
            result_embs[batch_start + item["index"]] = item["embedding"]
        print(f"[embed] {i}/{n} chunks embedded ({len(batch_texts)} in batch, {batch_tokens:,} tok)")

    elapsed = time.perf_counter() - t0
    print(
        f"[embed] {n} chunks in {elapsed:.1f}s "
        f"({elapsed / max(n, 1) * 1000:.1f} ms/chunk avg)"
    )
    if truncated_indices:
        print(f"[embed] WARNING: {len(truncated_indices)} chunks truncated to {EMBED_MAX_TOKENS} tokens:")
        for idx in truncated_indices:
            print(f"        - [{idx}] ({count_tokens(texts[idx])} tok)")
    if result_embs and result_embs[0] is not None:
        if len(result_embs[0]) != EMBED_DIM:
            raise RuntimeError(
                f"embedding dim mismatch: got {len(result_embs[0])}, expected {EMBED_DIM}"
            )
    if any(e is None for e in result_embs):
        missing = sum(1 for e in result_embs if e is None)
        raise RuntimeError(f"{missing} chunks were not embedded")
    return result_embs  # type: ignore[return-value]


def embed_chunks(chunks: list[Chunk]) -> list[list[float]]:
    """Batch-embed all chunks (thin wrapper over embed_texts)."""
    return embed_texts([c.text for c in chunks])


# ── Chroma persist ────────────────────────────────────────────────────────
def persist_to_chroma(
    chroma_dir: Path,
    chunks: list[Chunk],
    embeddings: list[list[float]],
) -> None:
    client = chromadb.PersistentClient(path=str(chroma_dir))
    # Recreate collection (fresh ingest)
    existing = [c.name for c in client.list_collections()]
    if COLLECTION_NAME in existing:
        client.delete_collection(COLLECTION_NAME)
    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    ids = [
        f"{Path(c.source).relative_to(KB_ROOT).as_posix()}#{c.chunk_index}"
        for c in chunks
    ]
    documents = [c.text for c in chunks]
    metadatas = [_coerce_metadata(c.to_metadata()) for c in chunks]

    # Chroma 1.5.x add() — single bulk call works for ~5K, but slice for safety log
    CHUNK_BATCH = 1000
    for start in range(0, len(chunks), CHUNK_BATCH):
        end = min(start + CHUNK_BATCH, len(chunks))
        collection.add(
            ids=ids[start:end],
            documents=documents[start:end],
            embeddings=embeddings[start:end],
            metadatas=metadatas[start:end],
        )
        print(f"[chroma] added {end}/{len(chunks)}")
    print(f"[chroma] collection '{COLLECTION_NAME}' total = {collection.count()}")


# ── R-18 commit stamp ─────────────────────────────────────────────────────
def write_ingest_stamp(
    chroma_dir: Path,
    total_chunks: int,
    kb_sha: str,
) -> Path:
    stamp = chroma_dir / "ingested_at_commit.txt"
    content = (
        f"kb_commit_sha={kb_sha}\n"
        f"ingested_at={datetime.now(timezone.utc).isoformat()}\n"
        f"total_chunks={total_chunks}\n"
        f"embedding_model={EMBED_MODEL_NAME}\n"
        f"embedding_dim={EMBED_DIM}\n"
    )
    stamp.write_text(content, encoding="utf-8")
    return stamp


# ── Retrieval sanity (Step 5) ─────────────────────────────────────────────
SANITY_QUERIES = [
    ("What is the AETERM variable?", "domains/AE/spec"),
    ("How does TA arm randomization work?", "domains/TA"),
    ("LBTESTCD codelist values for hematology", "terminology/core/lb_part"),
    ("What is USUBJID primary key constraint?", "DM/spec or chapters/ch04"),
    ("Method A in PC PP relating example", "domains/PC/examples"),
    ("DI device identifier assumptions", "domains/DI/assumptions"),
    ("Questionnaire ABCD-12 codelist", "terminology/questionnaires"),
    ("How to split SUPP-- domains", "chapters/ch08 or model"),
    ("Adverse Event Severity (C66769) values", "terminology/core/ae"),
    ("VARIABLE_INDEX AE entry", "VARIABLE_INDEX"),
]


def run_retrieval_sanity(chroma_dir: Path) -> dict:
    client = chromadb.PersistentClient(path=str(chroma_dir))
    collection = client.get_collection(COLLECTION_NAME)
    results = []
    for q, expect in SANITY_QUERIES:
        response = litellm.embedding(model=EMBED_MODEL_NAME, input=[q])
        emb = [response.data[0]["embedding"]]
        res = collection.query(query_embeddings=emb, n_results=5)
        ids = res["ids"][0]
        dists = res["distances"][0]
        top1 = ids[0] if ids else "(none)"
        sim_top1 = 1.0 - dists[0] if dists else float("nan")
        # 评判: 看 top-1 路径是否包含 expect 关键词的"主路径段"
        ok = any(token in top1 for token in expect.split())
        results.append({
            "query": q,
            "expect": expect,
            "top1": top1,
            "sim_top1": sim_top1,
            "topk_ids": ids,
            "topk_sims": [1.0 - d for d in dists],
            "ok": ok,
        })
    return {"results": results}


# ── Main flow ─────────────────────────────────────────────────────────────
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Phase 1A.5 full-KB ingest")
    parser.add_argument(
        "--retrieval-sanity",
        action="store_true",
        help="After ingest, run 10-query retrieval sanity check",
    )
    parser.add_argument(
        "--skip-ingest",
        action="store_true",
        help="Skip chunk+embed+persist; only run --retrieval-sanity against existing Chroma",
    )
    parser.add_argument(
        "--full-reset",
        action="store_true",
        help="旧行为: 整目录清空 (会删除 study_* collection)",
    )
    args = parser.parse_args(argv)

    print(f"[setup] sdtm-rag root  = {SDTM_RAG_ROOT}")
    print(f"[setup] KB root        = {KB_ROOT}")
    print(f"[setup] Chroma dir     = {CHROMA_DIR}")
    print(f"[setup] embedding      = {EMBED_MODEL_NAME} dim={EMBED_DIM} (cloud API)")

    wall_t0 = time.perf_counter()

    if not args.skip_ingest:
        # ── R-16 backup ──
        backup = backup_existing_chroma(CHROMA_DIR)
        if backup:
            print(f"[R-16] backed up existing Chroma → {backup}")
        else:
            print(f"[R-16] no prior Chroma payload; skip backup")
        if args.full_reset:
            print("[reset] --full-reset: wiping whole Chroma dir (study_* included)")
            reset_chroma_dir(CHROMA_DIR)
        else:
            print(f"[reset] collection-level: '{COLLECTION_NAME}' only")
            reset_collection(CHROMA_DIR, COLLECTION_NAME)

        # ── Chunking ──
        chunks, per_type, _unknown = collect_chunks()
        if not chunks:
            print("[ERROR] no chunks produced; abort.")
            return 2
        total_tokens = sum((c.chunk_size_tokens or 0) for c in chunks)
        print(f"[chunks] total tokens = {total_tokens:,} "
              f"(avg {total_tokens // len(chunks)} tokens/chunk)")
        kb_sha = kb_commit_sha(KB_ROOT)
        print(f"[chunks] kb_commit_sha = {kb_sha}")

        # ── Embedding ──
        print(f"[embed] calling {EMBED_MODEL_NAME} API (batch_size={EMBED_BATCH_SIZE}) ...")
        embeddings = embed_chunks(chunks)

        # ── Chroma persist ──
        persist_to_chroma(CHROMA_DIR, chunks, embeddings)

        # ── R-18 stamp ──
        stamp_path = write_ingest_stamp(CHROMA_DIR, len(chunks), kb_sha)
        print(f"[R-18] ingest stamp -> {stamp_path}")

        size = dir_size_bytes(CHROMA_DIR)
        wall = time.perf_counter() - wall_t0
        print(f"[done] total files chunked, {len(chunks)} chunks, "
              f"{total_tokens:,} tokens, "
              f"wallclock {wall:.1f}s, Chroma {fmt_bytes(size)}")

    if args.retrieval_sanity:
        print()
        print("=" * 70)
        print("Retrieval sanity (10 queries)")
        print("=" * 70)
        sanity = run_retrieval_sanity(CHROMA_DIR)
        for r in sanity["results"]:
            verdict = "OK" if r["ok"] else "??"
            print(
                f"  [{verdict}] {r['query'][:48]:<48} "
                f"sim={r['sim_top1']:.3f} top1={r['top1']}"
            )
        ok_count = sum(1 for r in sanity["results"] if r["ok"])
        print(f"\nVerdict: {ok_count}/10 queries return expected-domain top-1")
    return 0


if __name__ == "__main__":
    sys.exit(main())
