"""API routes for SDTM RAG Q&A + Dataset Validation (Phase 1B + 1C)."""
from __future__ import annotations

import json
import time
from typing import Literal

import structlog
from pydantic import BaseModel, Field
from fastapi import APIRouter, Request, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse

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
    structured_lookup: bool
    hybrid: bool
    hybrid_fusion: str | None = None
    prompt_guardrail: bool
    # Phase 2 compare/judge defaults (UI prefills its model slots from these).
    compare_models: list[str] = Field(default_factory=list)
    judge_model: str | None = None


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
        structured_lookup=rag.structured_lookup_enabled,
        hybrid=rag.hybrid_enabled,
        hybrid_fusion=rag.hybrid_fusion if rag.hybrid_enabled else None,
        prompt_guardrail=rag.prompt_guardrail_enabled,
        compare_models=s.compare_models,
        judge_model=s.judge_model,
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


# ── Streaming single-model Q&A (chat UI; DESIGN_chat_ui.md §3) ─────────


class AskStreamRequest(BaseModel):
    question: str = Field(max_length=10000)
    history: list[MessageItem] = Field(default_factory=list)
    top_k: int | None = Field(None, ge=1, le=100)
    domain: str | None = None
    file_type: str | None = None


@api_router.post("/ask_stream")
async def ask_stream(body: AskStreamRequest, request: Request):
    """SSE 流式单模型问答 (DeepSeek V4 Pro via Router 'default'). 检索一次 (FR1),
    然后流式生成。检索失败在开流前返 502; 流中途失败发 error 事件。"""
    rag = request.app.state.rag
    llm_router = request.app.state.llm_router

    if not body.question.strip():
        raise HTTPException(status_code=422, detail="question must not be empty")

    try:
        chunks = rag.retrieve(
            body.question, domain=body.domain, file_type=body.file_type, top_k=body.top_k
        )
    except Exception as e:
        log.error("stream_retrieve_failed", error=str(e), exc_info=True)
        raise HTTPException(status_code=502, detail="Retrieval service temporarily unavailable.")

    context = rag.format_context(chunks)
    history_dicts = [{"role": m.role, "content": m.content} for m in body.history]
    messages = rag.build_messages(body.question, context, history_dicts or None)
    sources = [
        {"chunk_id": c.chunk_id, "source": c.source, "domain": c.domain,
         "file_type": c.file_type, "section": c.section,
         "similarity": c.similarity, "text_preview": c.text[:300]}
        for c in chunks
    ]

    def sse(event: str, data: dict) -> str:
        return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"

    async def _open_stream():
        # include_usage lets the `done` event report token counts. Some providers reject
        # the stream_options kwarg; if the open fails, retry once WITHOUT it so the answer
        # is preserved (usage then reported as null — never fabricated). DeepSeek (current
        # default) supports it; this guards a future provider swap. Iteration-time failures
        # are NOT retried (would risk double generation) — they fall to the except below.
        try:
            return await llm_router.acompletion(
                model="default", messages=messages, stream=True,
                stream_options={"include_usage": True},
            )
        except Exception:  # noqa: BLE001 — narrow retry: drop stream_options, keep the answer
            log.warning("stream_options_unsupported_retry_without", exc_info=True)
            return await llm_router.acompletion(model="default", messages=messages, stream=True)

    async def gen():
        yield sse("sources", {"sources": sources})
        model_used = None
        usage = None
        try:
            resp = await _open_stream()
            async for chunk in resp:
                choices = getattr(chunk, "choices", None)
                if choices:
                    text = getattr(choices[0].delta, "content", None)
                    if text:
                        yield sse("token", {"text": text})
                    model_used = getattr(chunk, "model", None) or model_used
                cu = getattr(chunk, "usage", None)
                if cu:
                    usage = {"prompt_tokens": cu.prompt_tokens,
                             "completion_tokens": cu.completion_tokens,
                             "total_tokens": cu.total_tokens}
            yield sse("done", {"model_used": model_used or "default", "usage": usage})
        except Exception as e:  # noqa: BLE001 — stream already open, surface as event
            log.error("stream_failed", error=str(e), exc_info=True)
            yield sse("error", {"message": "LLM stream failed"})

    return StreamingResponse(
        gen(), media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


# ── Multi-model compare + judge (Phase 2; DEPLOY_PLAN §2.5) ───────────


class JudgeConfig(BaseModel):
    enabled: bool = False
    model: str | None = None  # None -> settings.judge_model


class AskCompareRequest(BaseModel):
    question: str = Field(max_length=10000)
    models: list[str] | None = None  # None -> settings.compare_models
    domain: str | None = None
    file_type: str | None = None
    history: list[MessageItem] = Field(default_factory=list)
    top_k: int | None = Field(None, ge=1, le=100)
    judge: JudgeConfig = Field(default_factory=JudgeConfig)


class ModelAnswerItem(BaseModel):
    model: str
    answer: str
    usage: dict | None = None
    latency_ms: int
    cost_usd: float | None = None
    error: str | None = None


class JudgeRankItem(BaseModel):
    model: str
    rank: int
    comment: str


class JudgeResult(BaseModel):
    ranking: list[JudgeRankItem]
    best_model: str | None = None
    rationale: str


class AskCompareResponse(BaseModel):
    sources: list[SourceItem]
    answers: list[ModelAnswerItem]
    judge: JudgeResult | None = None


# Safety cap: at most this many generation models per compare request. The UI offers
# 3 slots; the cap guards an arbitrary API caller from fanning out an unbounded burst.
_MAX_COMPARE_MODELS = 6


@api_router.post("/ask_compare", response_model=AskCompareResponse)
async def ask_compare(body: AskCompareRequest, request: Request):
    """One question -> N models answer over the SAME retrieved context, side by side,
    with an optional anonymized judge. Reuses retrieve/format/build (FR1: retrieval runs
    ONCE), then fans generation out in parallel (FR2) with per-model failure isolation
    (NFR2). See server/compare.py."""
    from server.compare import run_compare, run_judge

    rag = request.app.state.rag
    s = request.app.state.settings
    t0 = time.perf_counter()

    if not body.question.strip():
        raise HTTPException(status_code=422, detail="question must not be empty")

    models = [m.strip() for m in (body.models or s.compare_models) if m and m.strip()]
    # De-dup, preserving order: identical slots would render indistinguishable columns
    # and map two judge labels back to the same model name (ambiguous "best"). Running
    # the same model twice for variance is not a goal here (compare is temperature-0-ish
    # and aims to expose CROSS-model disagreement).
    models = list(dict.fromkeys(models))
    if not models:
        raise HTTPException(status_code=422, detail="no models specified")
    if len(models) > _MAX_COMPARE_MODELS:
        raise HTTPException(
            status_code=422,
            detail=f"too many models ({len(models)} > {_MAX_COMPARE_MODELS})",
        )

    log.info("ask_compare", question=body.question[:100], models=models,
             judge=body.judge.enabled, domain=body.domain)

    # retrieve/format/build are SYNC and run inline on the event loop. Intentional for
    # the §1 single-user localhost deployment (retrieval is fast vs the LLM calls that
    # dominate). If this ever moves multi-user (§6 搬云), wrap retrieve in
    # asyncio.to_thread so one request's retrieval can't serialize others.
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

    answers = await run_compare(
        models, messages,
        timeout_s=s.compare_timeout_s, num_retries=s.compare_num_retries,
    )

    judge_result = None
    if body.judge.enabled:
        judge_model = body.judge.model or s.judge_model
        judge_raw = await run_judge(
            body.question, context, answers, judge_model,
            timeout_s=s.compare_timeout_s, num_retries=s.compare_num_retries,
        )
        if judge_raw:
            judge_result = JudgeResult(
                ranking=[JudgeRankItem(**r) for r in judge_raw["ranking"]],
                best_model=judge_raw["best_model"],
                rationale=judge_raw["rationale"],
            )

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
        "ask_compare_done",
        chunks=len(chunks),
        n_models=len(answers),
        n_errors=sum(1 for a in answers if a.error),
        judged=judge_result is not None,
        elapsed_s=round(elapsed, 2),
    )

    return AskCompareResponse(
        sources=sources,
        answers=[ModelAnswerItem(**vars(a)) for a in answers],
        judge=judge_result,
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
