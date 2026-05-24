"""API routes for SDTM RAG Q&A + Dataset Validation (Phase 1B + 1C)."""
from __future__ import annotations

import time
from typing import Literal

import structlog
from pydantic import BaseModel, Field
from fastapi import APIRouter, Request, HTTPException, UploadFile, File, Form

log = structlog.get_logger()
api_router = APIRouter(prefix="/api")

VALID_MODELS = {"default", "hard", "light"}


# ── Request / Response models ────────────────────────────────────────────

class MessageItem(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(max_length=50000)


class AskRequest(BaseModel):
    question: str = Field(max_length=10000)
    domain: str | None = None
    file_type: str | None = None
    model: str = "default"
    history: list[MessageItem] = Field(default_factory=list)
    top_k: int | None = Field(None, ge=1, le=100)


class SourceItem(BaseModel):
    chunk_id: str
    source: str
    domain: str | None
    file_type: str | None
    section: str | None
    similarity: float
    text_preview: str


class AskResponse(BaseModel):
    answer: str
    sources: list[SourceItem]
    model_used: str
    usage: dict | None = None


class InfoResponse(BaseModel):
    collection_name: str
    chunk_count: int
    default_model: str
    fallback_model: str
    top_k: int


# ── Endpoints ────────────────────────────────────────────────────────────

@api_router.get("/health")
def health():
    return {"status": "ok"}


@api_router.get("/info", response_model=InfoResponse)
def info(request: Request):
    rag = request.app.state.rag
    s = request.app.state.settings
    return InfoResponse(
        collection_name=s.collection_name,
        chunk_count=rag.collection.count(),
        default_model=s.default_model,
        fallback_model=s.fallback_model,
        top_k=s.top_k,
    )


@api_router.post("/ask", response_model=AskResponse)
def ask(body: AskRequest, request: Request):
    rag = request.app.state.rag
    llm_router = request.app.state.llm_router
    t0 = time.perf_counter()

    if not body.question.strip():
        raise HTTPException(status_code=422, detail="question must not be empty")

    if body.model not in VALID_MODELS:
        raise HTTPException(
            status_code=422,
            detail=f"model must be one of {VALID_MODELS}",
        )

    log.info("ask", question=body.question[:100], model=body.model, domain=body.domain)

    try:
        chunks = rag.retrieve(
            body.question,
            domain=body.domain,
            file_type=body.file_type,
            top_k=body.top_k,
        )
    except Exception as e:
        log.error("retrieve_failed", error=str(e), exc_info=True)
        raise HTTPException(status_code=502, detail="Retrieval service temporarily unavailable.")

    context = rag.format_context(chunks)
    history_dicts = [{"role": m.role, "content": m.content} for m in body.history]
    messages = rag.build_messages(body.question, context, history_dicts or None)

    try:
        response = llm_router.completion(model=body.model, messages=messages)
    except Exception as e:
        log.error("llm_failed", error=str(e), model=body.model, exc_info=True)
        raise HTTPException(status_code=502, detail="LLM service temporarily unavailable.")

    answer = response.choices[0].message.content or ""
    model_used = getattr(response, "model", None) or body.model
    usage = None
    if response.usage:
        usage = {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        }

    sources = [
        SourceItem(
            chunk_id=c.chunk_id,
            source=c.source,
            domain=c.domain,
            file_type=c.file_type,
            section=c.section,
            similarity=c.similarity,
            text_preview=c.text[:300],
        )
        for c in chunks
    ]

    elapsed = time.perf_counter() - t0
    log.info(
        "ask_done",
        chunks=len(chunks),
        model_used=model_used,
        tokens=usage.get("total_tokens") if usage else None,
        elapsed_s=round(elapsed, 2),
    )

    return AskResponse(
        answer=answer,
        sources=sources,
        model_used=model_used,
        usage=usage,
    )


# ── Dataset Validation (Phase 1C) ─────────────────────────────────────


@api_router.post("/validate")
async def validate_dataset(
    request: Request,
    file: UploadFile = File(...),
    domain: str | None = Form(None),
    dm_file: UploadFile | None = File(None),
    semantic_review: str = Form("true"),
):
    """Validate an SDTM dataset against KB specs + optional RAG semantic review."""
    from scripts.parse_dataset import parse_bytes, ParseError
    from server.validator import validate
    from server.reviewer import review
    from server.report import FullReport, generate_json

    spec_loader = request.app.state.spec_loader
    t0 = time.perf_counter()

    data = await file.read()
    filename = file.filename or "upload.csv"
    log.info("validate_start", filename=filename, size=len(data), domain=domain)

    try:
        df, meta = parse_bytes(data, filename)
    except ParseError as e:
        raise HTTPException(status_code=422, detail=str(e))

    effective_domain = domain or meta.domain
    if not effective_domain:
        raise HTTPException(
            status_code=422,
            detail="Cannot detect domain. Provide 'domain' parameter or include DOMAIN column.",
        )

    dm_df = None
    if dm_file:
        dm_data = await dm_file.read()
        dm_filename = dm_file.filename or "dm.csv"
        try:
            dm_df, _ = parse_bytes(dm_data, dm_filename)
        except ParseError as e:
            raise HTTPException(status_code=422, detail=f"DM file error: {e}")

    val_result = validate(df, effective_domain, spec_loader, dm_df=dm_df)

    run_semantic = semantic_review.lower() in ("true", "1", "yes")
    review_result = None
    if run_semantic:
        try:
            rag = request.app.state.rag
            llm_router = request.app.state.llm_router
            review_result = review(
                df, effective_domain, meta.variables, rag,
                model="hard", llm_router=llm_router,
            )
        except Exception as e:
            log.error("semantic_review_failed", error=str(e))
            from server.reviewer import ReviewResult, SemanticFinding
            review_result = ReviewResult(
                domain=effective_domain,
                findings=[SemanticFinding(
                    "WARN", "business_rule",
                    "Semantic review failed",
                    "The LLM-based review could not be completed. Rule-based results are still valid.",
                )],
            )

    full = FullReport(
        domain=effective_domain,
        file_path=filename,
        row_count=meta.row_count,
        col_count=meta.col_count,
        completeness_pct=val_result.completeness_pct,
        validation=val_result,
        review=review_result,
    )

    elapsed = time.perf_counter() - t0
    log.info("validate_done", domain=effective_domain, errors=full.total_errors,
             warnings=full.total_warnings, elapsed_s=round(elapsed, 2))

    return generate_json(full)
