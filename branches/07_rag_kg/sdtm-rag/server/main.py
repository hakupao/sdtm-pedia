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

from scripts.spec_loader import SpecLoader
from server.auth import install_security
from server.config import settings
from server.llm_config import create_router
from server.rag import RAGEngine
from server.router import api_router

structlog.configure(
    wrapper_class=structlog.make_filtering_bound_logger(
        logging.getLevelName(settings.log_level)
    ),
)
log = structlog.get_logger()


def maybe_build_answerer(s):
    """Build the structured-answer channel when enabled, else None. Kept tiny and
    pure so it unit-tests without spinning up FastAPI/RAGEngine (lifespan is heavy)."""
    if not s.structured_answer_enabled:
        return None
    from server.meta_store import MetaStore
    from server.structured_answer import StructuredAnswerer
    return StructuredAnswerer(MetaStore(s.meta_path))


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Read the ONE settings object the factory installed on app.state (create_app sets it
    # before startup). Routes also read request.app.state.settings, so middleware, routes,
    # RAG, and the LLM router all derive from the same config — create_app(custom) is fully
    # consistent, not split-brain between the security stack and the request path.
    s = app.state.settings
    log.info(
        "startup",
        chroma=str(s.chroma_dir),
        kb=str(s.kb_root),
        model=s.default_model,
    )
    t_rag = time.perf_counter()
    app.state.rag = RAGEngine(
        chroma_dir=s.chroma_dir,
        kb_root=s.kb_root,
        collection_name=s.collection_name,
        embedding_model=s.embedding_model,
        top_k=s.top_k,
        # P1 retrieval levers (validated combination, default on; see config.py).
        structured_lookup_enabled=s.structured_lookup_enabled,
        hybrid_enabled=s.hybrid_enabled,
        hybrid_fusion=s.hybrid_fusion,
        hybrid_alpha=s.hybrid_alpha,
        hybrid_pool=s.hybrid_pool,
        # Answer-side trust guardrail (system-prompt grounding rules; default on).
        prompt_guardrail_enabled=s.prompt_guardrail_enabled,
    )
    rag_init_s = round(time.perf_counter() - t_rag, 2)  # incl. BM25 index build when hybrid on
    app.state.llm_router = create_router(s)
    app.state.answerer = maybe_build_answerer(s)
    if app.state.answerer is not None:
        log.info("structured_answer_enabled")
    app.state.spec_loader = SpecLoader(s.kb_root)
    log.info("spec_loader", domains=len(app.state.spec_loader.domains),
             codelists=len(app.state.spec_loader.codelists))
    count = app.state.rag.collection.count()
    # Guard the one documented foot-gun: hybrid-on with structured_lookup-off is the
    # known-bad config (P1 measured single_domain 96->83). A half-applied env rollback
    # (disable S1 only, leave hybrid on) would silently land here, so warn loudly. This
    # lives in the production boot path only — eval ablations legitimately test hybrid
    # alone via run_eval flags and must stay unconstrained.
    if s.hybrid_enabled and not s.structured_lookup_enabled:
        log.warning(
            "hybrid_without_structured_lookup",
            note="known single_domain regression (96->83); enable structured_lookup, "
                 "or disable BOTH levers for plain cosine",
        )
    log.info(
        "ready",
        collection=s.collection_name,
        chunks=count,
        structured_lookup=s.structured_lookup_enabled,
        hybrid=s.hybrid_enabled,
        hybrid_fusion=s.hybrid_fusion,
        prompt_guardrail=s.prompt_guardrail_enabled,
        rag_init_s=rag_init_s,
    )
    yield
    log.info("shutdown")


_WEBCHAT_DIR = Path(__file__).resolve().parent.parent / "webchat"


def create_app(app_settings=None) -> FastAPI:
    """Build the FastAPI app. A factory (not a bare module global) so the phase-3 security
    stack is wired from explicit settings and tests can construct apps with custom config.
    Production uses the module-level `app = create_app()` with the global settings.

    `app_settings` defaults to the module global at CALL time (not import time). It is set on
    app.state so the lifespan + every route read the SAME object — passing custom settings
    here configures the whole app, not just the middleware."""
    app_settings = app_settings or settings
    application = FastAPI(
        title="SDTM RAG Q&A Service",
        description="SDTM knowledge base semantic search and Q&A (Phase 1B)",
        version="0.1.0",
        lifespan=lifespan,
    )
    application.state.settings = app_settings  # single config source (lifespan + routes read this)
    application.include_router(api_router)

    # Static hosting for the ChatGPT-style chat UI (DESIGN_chat_ui.md §1). `/static` and
    # `GET /` do not collide with the api_router's `/api/*` prefix. Guard with exists() so
    # a missing webchat/ during build-out never crashes boot.
    if _WEBCHAT_DIR.exists():
        application.mount("/static", StaticFiles(directory=str(_WEBCHAT_DIR)), name="static")

        @application.get("/")
        def chat_index():
            return FileResponse(str(_WEBCHAT_DIR / "index.html"))

    # Phase 3 sharing: login gate + rate limit + security headers (all OFF by default; see
    # server/auth.install_security and config.py). Added last so it wraps routes + static.
    install_security(application, app_settings)
    return application


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server.main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
