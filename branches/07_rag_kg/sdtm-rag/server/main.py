"""FastAPI application entry point (Phase 1B).

Run:
  uvicorn server.main:app --reload          (dev)
  uvicorn server.main:app --host 0.0.0.0    (Docker)
"""
from __future__ import annotations

import logging
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI

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


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info(
        "startup",
        chroma=str(settings.chroma_dir),
        kb=str(settings.kb_root),
        model=settings.default_model,
    )
    app.state.rag = RAGEngine(
        chroma_dir=settings.chroma_dir,
        kb_root=settings.kb_root,
        collection_name=settings.collection_name,
        embedding_model=settings.embedding_model,
        top_k=settings.top_k,
    )
    app.state.llm_router = create_router(settings)
    app.state.settings = settings
    count = app.state.rag.collection.count()
    log.info("ready", collection=settings.collection_name, chunks=count)
    yield
    log.info("shutdown")


app = FastAPI(
    title="SDTM RAG Q&A Service",
    description="SDTM knowledge base semantic search and Q&A (Phase 1B)",
    version="0.1.0",
    lifespan=lifespan,
)
app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "server.main:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
