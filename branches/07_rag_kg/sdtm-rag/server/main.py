"""FastAPI application entry point (Phase 1B).

Run:
  uvicorn server.main:app --reload          (dev)
  uvicorn server.main:app --host 0.0.0.0    (Docker)
"""
from __future__ import annotations

import logging
import time
from contextlib import asynccontextmanager
from pathlib import Path

import structlog
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from server.config import settings
from server.llm_config import create_router
from server.rag import RAGEngine
from server.router import api_router
from scripts.spec_loader import SpecLoader

structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(
        logging.getLevelName(settings.log_level)
    ),
)
log = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info(
        "startup",
        chroma=str(settings.chroma_dir),
        kb=str(settings.kb_root),
        model=settings.default_model,
    )
    t_rag = time.perf_counter()
    app.state.rag = RAGEngine(
        chroma_dir=settings.chroma_dir,
        kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model,
        top_k=settings.top_k,
        # P1 retrieval levers (validated combination, default on; see config.py).
        structured_lookup_enabled=settings.structured_lookup_enabled,
        hybrid_enabled=settings.hybrid_enabled,
        hybrid_fusion=settings.hybrid_fusion,
        hybrid_alpha=settings.hybrid_alpha,
        hybrid_pool=settings.hybrid_pool,
        # Answer-side trust guardrail (system-prompt grounding rules; default on).
        prompt_guardrail_enabled=settings.prompt_guardrail_enabled,
    )
    rag_init_s = round(time.perf_counter() - t_rag, 2)  # incl. BM25 index build when hybrid on
    app.state.llm_router = create_router(settings)
    app.state.settings = settings
    app.state.spec_loader = SpecLoader(settings.kb_root)
    log.info("spec_loader", domains=len(app.state.spec_loader.domains),
             codelists=len(app.state.spec_loader.codelists))
    count = app.state.rag.collection.count()
    # Guard the one documented foot-gun: hybrid-on with structured_lookup-off is the
    # known-bad config (P1 measured single_domain 96->83). A half-applied env rollback
    # (disable S1 only, leave hybrid on) would silently land here, so warn loudly. This
    # lives in the production boot path only — eval ablations legitimately test hybrid
    # alone via run_eval flags and must stay unconstrained.
    if settings.hybrid_enabled and not settings.structured_lookup_enabled:
        log.warning(
            "hybrid_without_structured_lookup",
            note="known single_domain regression (96->83); enable structured_lookup, "
                 "or disable BOTH levers for plain cosine",
        )
    log.info(
        "ready",
        collection=settings.collection_name,
        chunks=count,
        structured_lookup=settings.structured_lookup_enabled,
        hybrid=settings.hybrid_enabled,
        hybrid_fusion=settings.hybrid_fusion,
        prompt_guardrail=settings.prompt_guardrail_enabled,
        rag_init_s=rag_init_s,
    )
    yield
    log.info("shutdown")


app = FastAPI(
    title="SDTM RAG Q&A Service",
    description="SDTM knowledge base semantic search and Q&A (Phase 1B)",
    version="0.1.0",
    lifespan=lifespan,
)
app.include_router(api_router)

# Static hosting for the ChatGPT-style chat UI (DESIGN_chat_ui.md §1). `/static` and
# `GET /` do not collide with the api_router's `/api/*` prefix. The webchat/ dir may not
# exist yet during incremental build-out, so guard with exists() — files added later
# (Tasks 3-5) light this up automatically with no further code change.
_WEBCHAT_DIR = Path(__file__).resolve().parent.parent / "webchat"
if _WEBCHAT_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(_WEBCHAT_DIR)), name="static")

    @app.get("/")
    def chat_index():
        return FileResponse(str(_WEBCHAT_DIR / "index.html"))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server.main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
