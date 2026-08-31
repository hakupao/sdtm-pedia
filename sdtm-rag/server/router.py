"""API routes for SDTM RAG Q&A + Dataset Validation (Phase 1B + 1C)."""
from __future__ import annotations

import asyncio
import datetime
import json
import time
from typing import Literal

import structlog
from fastapi import APIRouter, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from server.web_search import WEB_TOOL_SPEC, WebSearcher, render_tool_result

log = structlog.get_logger()
api_router = APIRouter(prefix="/api")

VALID_MODELS = {"default", "hard", "light"}

# 单库 RAGEngine.format_context 在零 chunk 时返回的哨兵句 (server/rag.py)。联邦层的
# format_context 两组都空时返回空串 —— 空 context 会让模型以为"上下文段落缺失"而自由
# 发挥, 所以联邦路径在这里补回同一句, 与单库路径逐字节一致 (漂移由测试钉住)。
_NO_CONTEXT = "(No relevant context found in the knowledge base.)"

# 联网失败的严重度序 (F-10): 一次都没成功时报"最严重"的那个, 而不是"最后一个"。
# disabled (没配 key, 永远不会成) > quota_exceeded (今天的预算用光) > failed (可能是瞬时的)。
# 只有真打了网的尝试才进这张表 —— 模型自己出错 (bad_query / unknown_tool) 不算联网失败。
_WEB_FAIL_RANK = {"disabled": 3, "quota_exceeded": 2, "failed": 1}


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
    # Plan B 联邦: auto = LLM 判库; 显式值绕过路由 (federation 关时该字段无作用)
    corpus: Literal["auto", "cdisc", "study", "both"] = "auto"


class SourceItem(BaseModel):
    chunk_id: str
    source: str
    domain: str | None
    file_type: str | None
    section: str | None
    similarity: float
    text_preview: str
    corpus: str | None = None  # 联邦路径下 "cdisc"|"study"; 单库路径 None


class AskResponse(BaseModel):
    answer: str
    sources: list[SourceItem]
    model_used: str
    usage: dict | None = None
    routed_corpus: str | None = None  # 实际检索的库; federation 关时 None


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
    # 索引新鲜度 (运维闸): 默认 None 而非 True —— 判不出来时说"新鲜"比没有该字段更糟
    index_fresh: bool | None = None
    index_freshness_reason: str | None = None
    federation: bool = False  # Plan B: 双库联邦是否已构建


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
        # 启动时算好存在 app.state, 避免每次 /info 都重扫 KB 目录
        index_fresh=getattr(request.app.state, "index_fresh", None),
        index_freshness_reason=getattr(request.app.state, "index_freshness_reason", None),
        federation=getattr(request.app.state, "federation", None) is not None,
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

    fed = getattr(request.app.state, "federation", None)
    routed: str | None = None
    try:
        if fed is not None:
            chunks, routed = fed.retrieve(
                body.question, corpus=body.corpus, top_k=body.top_k,
                domain=body.domain, file_type=body.file_type,
            )
        else:
            chunks = rag.retrieve(
                body.question,
                domain=body.domain,
                file_type=body.file_type,
                top_k=body.top_k,
            )
    except Exception as e:
        log.error("retrieve_failed", error=str(e), exc_info=True)
        raise HTTPException(status_code=502, detail="Retrieval service temporarily unavailable.") from e

    answerer = getattr(request.app.state, "answerer", None)
    if routed == "study":
        answerer = None  # CDISC 专用事实通道, study 单库路由下必须静默跳过
    try:
        facts = answerer.resolve(body.question) if answerer else None
    except Exception:
        log.warning("structured_answer_resolve_failed", exc_info=True)
        facts = None

    engine = fed if fed is not None else rag
    context = engine.format_context(chunks)
    if fed is not None and not context:
        context = _NO_CONTEXT
    if facts is not None:
        from server.structured_answer import augment_context
        context = augment_context(facts, context)

    history_dicts = [{"role": m.role, "content": m.content} for m in body.history]
    if fed is not None:
        messages = fed.build_messages(body.question, context, history_dicts or None,
                                      corpus=routed or body.corpus)
    else:
        messages = rag.build_messages(body.question, context, history_dicts or None)

    try:
        response = llm_router.completion(model=body.model, messages=messages)
    except Exception as e:
        log.error("llm_failed", error=str(e), model=body.model, exc_info=True)
        raise HTTPException(status_code=502, detail="LLM service temporarily unavailable.") from e

    answer = response.choices[0].message.content or ""
    if facts is not None:
        from server.grounding import apply_counting_gate
        answer, violations = apply_counting_gate(answer, facts)
        if violations:
            log.warning("structured_count_violation", violations=violations)
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
            corpus=getattr(c, "corpus", None) or None,
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
        routed_corpus=routed,
    )


# ── Streaming single-model Q&A (chat UI; DESIGN_chat_ui.md §3) ─────────


class AskStreamRequest(BaseModel):
    question: str = Field(max_length=10000)
    history: list[MessageItem] = Field(default_factory=list)
    top_k: int | None = Field(None, ge=1, le=100)
    domain: str | None = None
    file_type: str | None = None
    corpus: Literal["auto", "cdisc", "study", "both"] = "auto"
    web: bool = False  # 联网参考通道; 与 corpus 判库正交 (spec §4)


@api_router.post("/ask_stream")
async def ask_stream(body: AskStreamRequest, request: Request):
    """SSE 流式单模型问答 (DeepSeek V4 Pro via Router 'default'). 检索一次 (FR1),
    然后流式生成。检索失败在开流前返 502; 流中途失败发 error 事件。"""
    rag = request.app.state.rag
    llm_router = request.app.state.llm_router
    s = request.app.state.settings

    if not body.question.strip():
        raise HTTPException(status_code=422, detail="question must not be empty")

    fed = getattr(request.app.state, "federation", None)
    routed: str | None = None
    try:
        if fed is not None:
            chunks, routed = fed.retrieve(
                body.question, corpus=body.corpus, top_k=body.top_k,
                domain=body.domain, file_type=body.file_type,
            )
        else:
            chunks = rag.retrieve(
                body.question, domain=body.domain, file_type=body.file_type, top_k=body.top_k
            )
    except Exception as e:
        log.error("stream_retrieve_failed", error=str(e), exc_info=True)
        raise HTTPException(status_code=502, detail="Retrieval service temporarily unavailable.") from e

    answerer = getattr(request.app.state, "answerer", None)
    if routed == "study":
        answerer = None  # CDISC 专用事实通道, study 单库路由下必须静默跳过
    try:
        facts = answerer.resolve(body.question) if answerer else None
    except Exception:
        log.warning("structured_answer_resolve_failed", exc_info=True)
        facts = None

    engine = fed if fed is not None else rag
    context = engine.format_context(chunks)
    if fed is not None and not context:
        context = _NO_CONTEXT
    if facts is not None:
        from server.structured_answer import augment_context
        context = augment_context(facts, context)

    history_dicts = [{"role": m.role, "content": m.content} for m in body.history]
    if fed is not None:
        messages = fed.build_messages(body.question, context, history_dicts or None,
                                      corpus=routed or body.corpus)
    else:
        messages = rag.build_messages(body.question, context, history_dicts or None)
    sources = [
        {"chunk_id": c.chunk_id, "source": c.source, "domain": c.domain,
         "file_type": c.file_type, "section": c.section,
         "similarity": c.similarity, "text_preview": c.text[:300],
         "corpus": getattr(c, "corpus", None) or None}
        for c in chunks
    ]

    def sse(event: str, data: dict) -> str:
        return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"

    use_web = bool(body.web) and s.web_search_enabled
    tools = [WEB_TOOL_SPEC] if use_web else None
    searcher = WebSearcher(s) if use_web else None

    async def _open_stream(msgs, with_tools: bool):
        """include_usage 让 done 能报 token; 个别 provider 不收该 kwarg, 失败则退化重开一次
        (保住答案, usage 报 null 而非编造)。开流失败才重试 —— 迭代中途失败不重试 (会重复生成),
        由下面的 except 兜。工具参数只在 with_tools 时传 —— web 关闭时请求体与本功能引入前
        逐位相同。"""
        kw = {"model": "default", "messages": msgs, "stream": True}
        if with_tools and tools:
            kw["tools"] = tools
        try:
            return await llm_router.acompletion(**kw, stream_options={"include_usage": True})
        except Exception:  # noqa: BLE001 — 窄重试: 去掉 stream_options, 保住答案
            log.warning("stream_options_unsupported_retry_without", exc_info=True)
            return await llm_router.acompletion(**kw)

    async def gen():
        yield sse("sources", {"sources": sources, "routed_corpus": routed})
        model_used = None
        parts: list[str] = []   # 跨轮全文, 只给 counting gate 用
        # 每轮都是一次独立计费的 API 调用 —— usage 必须跨轮累加, 只报最后一轮会系统性低报
        # 成本。某轮走了 stream_options 窄重试就拿不到 usage; 那种情况打 partial 标记:
        # 部分数据比没有有用, 但不能把"缺了一轮"呈现成一个看起来完整的总量。
        usage_total = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        usage_seen = False
        usage_missing = False
        web_ok = 0
        web_fail: str | None = None   # 最严重的一次联网失败 (见 _WEB_FAIL_RANK)
        if not body.web:
            web_status = "off"
        elif not s.web_search_enabled:
            # 用户勾了联网、服务端关着 —— 报 off 会让界面一声不吭, 那正是最骗人的失败模式。
            web_status = "disabled"
        else:
            web_status = "ok"
        msgs = list(messages)

        try:
            # web 开启时多跑一轮: 前 max_rounds 轮带工具, 最后一轮**不带**工具 ——
            # 触顶后模型必须用手上的东西作答, 不能再要搜索, 也不会被硬切断在半句话上。
            total_rounds = (s.web_max_rounds + 1) if use_web else 1
            for rnd in range(1, total_rounds + 1):
                with_tools = use_web and rnd <= s.web_max_rounds
                # 开流的外层上限 (REV MED-b): provider 连接挂死时以 error 事件收场, 不把
                # SSE 连接晾着。流中途**不**包 wait_for —— 单一 deadline 会截断健康的长答案。
                resp = await asyncio.wait_for(
                    _open_stream(msgs, with_tools), timeout=s.request_timeout_s)

                acc: dict[int, dict] = {}   # 流式 tool_calls 是增量的, 按 index 拼
                round_parts: list[str] = []  # 本轮文本, 回灌 assistant 消息用
                cu_round = None
                async for chunk in resp:
                    choices = getattr(chunk, "choices", None)
                    if choices:
                        ch = choices[0]
                        # 是否继续循环只看 acc 是否攒到工具调用, 不看 finish_reason ——
                        # 各 provider 的收尾理由字段并不统一, acc 是唯一可靠的信号。
                        text = getattr(ch.delta, "content", None)
                        if text:
                            parts.append(text)
                            round_parts.append(text)
                            yield sse("token", {"text": text})
                        for tc in (getattr(ch.delta, "tool_calls", None) or []):
                            # index / id 一律 getattr 兜底: 缺字段的 delta 若让
                            # AttributeError 穿透, 用户拿到的是 "LLM stream failed",
                            # 整个答案丢光 —— 这比少拼一个分片严重得多。
                            slot = acc.setdefault(getattr(tc, "index", 0),
                                                  {"id": None, "name": "", "args": ""})
                            tc_id = getattr(tc, "id", None)
                            if tc_id and not slot["id"]:
                                slot["id"] = tc_id          # 取首个非空
                            fn = getattr(tc, "function", None)
                            if fn and getattr(fn, "name", None) and not slot["name"]:
                                slot["name"] = fn.name      # 取首个非空: 有 provider 每片都重发
                            if fn and getattr(fn, "arguments", None):
                                slot["args"] += fn.arguments  # 只有 arguments 是真分片
                        model_used = getattr(chunk, "model", None) or model_used
                    cu = getattr(chunk, "usage", None)
                    if cu:
                        cu_round = cu

                if cu_round is not None:
                    usage_seen = True
                    usage_total["prompt_tokens"] += getattr(cu_round, "prompt_tokens", None) or 0
                    usage_total["completion_tokens"] += (
                        getattr(cu_round, "completion_tokens", None) or 0)
                    usage_total["total_tokens"] += getattr(cu_round, "total_tokens", None) or 0
                else:
                    usage_missing = True

                # 没有工具调用 = 本轮就是最终答案; 本轮压根没挂工具 (web 关闭, 或已是收尾轮)
                # 也一律当最终答案 —— 没挂工具就不该解释工具调用, 更不该为它烧一次配额。
                if not acc or not with_tools:
                    break

                # 回灌 assistant 本轮的文本 + tool_calls。content 不能硬写 None —— 模型调
                # 工具前说的话已经流给用户了, 不回灌它就"忘了"自己说过什么, 最终答案会重复一遍。
                round_text = "".join(round_parts)
                msgs.append({"role": "assistant", "content": round_text or None, "tool_calls": [
                    {"id": v["id"], "type": "function",
                     "function": {"name": v["name"], "arguments": v["args"]}}
                    for _, v in sorted(acc.items())]})

                for _, v in sorted(acc.items()):
                    try:
                        query = json.loads(v["args"] or "{}").get("query", "")
                    except json.JSONDecodeError:
                        query = ""   # 模型偶发畸形 JSON: 当空查询处理, 不炸循环
                    yield sse("tool_call", {"round": rnd, "query": query, "id": v["id"]})

                    if v["name"] != "web_search":
                        # 工具分发不能"名字不管一律当 web_search"。模型点名不存在的工具就
                        # 如实告诉它, 不执行、不烧配额 —— 这是安全边界, 不只是健壮性。
                        refs, st = [], "unknown_tool"
                        content = json.dumps(
                            {"status": st, "results": [],
                             "error": f"No tool named {v['name']!r}. Only 'web_search' exists."},
                            ensure_ascii=False)
                    elif not query:
                        # 模型给了畸形/空 query: 是**模型**出错不是**联网**出错, 不能让用户
                        # 看到"联网失败"。如实标在这一条上, 不动 web_status。
                        refs, st = [], "bad_query"
                        content = json.dumps(
                            {"status": st, "results": [],
                             "error": "tool call carried no usable 'query' argument."},
                            ensure_ascii=False)
                    elif searcher.searches_used >= s.web_max_searches:
                        refs, st = [], "quota_exceeded"
                        content = render_tool_result(refs, st)
                    else:
                        # searcher.search 是同步 requests.post, 单次最长 web_timeout_s,
                        # 单请求可跑 web_max_searches 次 —— 直接调会把整个 event loop
                        # (所有并发 SSE 流 + 健康检查) 占死几分钟。本服务是 LAN 共享的。
                        refs, st = await asyncio.to_thread(searcher.search, query)
                        content = render_tool_result(refs, st)

                    if st == "ok":
                        web_ok += 1
                    elif st in _WEB_FAIL_RANK and (
                            web_fail is None or _WEB_FAIL_RANK[st] > _WEB_FAIL_RANK[web_fail]):
                        web_fail = st

                    yield sse("tool_result", {"id": v["id"], "count": len(refs),
                                              "status": st, "urls": [r.url for r in refs]})
                    msgs.append({"role": "tool", "tool_call_id": v["id"],
                                 "name": v["name"], "content": content})

            # 全成 -> ok; 有成有败 -> partial; 一次没成 -> 最严重的那个失败状态。
            # 逐条的失败细节不丢, 它已经在每条 tool_result 事件里。
            if web_fail is not None:
                web_status = "partial" if web_ok else web_fail

            # counting gate: 拼出来的答案与可核验的计数矛盾时, 在 done 之前补发一段修正 token
            if facts is not None:
                from server.grounding import apply_counting_gate
                full = "".join(parts)
                corrected, violations = apply_counting_gate(full, facts)
                if violations:
                    log.warning("structured_count_violation_stream", violations=violations)
                    yield sse("token", {"text": corrected[len(full):]})

            usage = None
            if usage_seen:
                usage = dict(usage_total)
                if usage_missing:
                    usage["partial"] = True   # 有轮次没拿到 usage, 总量不完整, 必须标明
            yield sse("done", {"model_used": model_used or "default",
                               "usage": usage, "web_status": web_status})
        except Exception as e:  # noqa: BLE001 — 流已开, 以事件形式暴露
            log.error("stream_failed", error=str(e), exc_info=True)
            yield sse("error", {"message": "LLM stream failed"})

    return StreamingResponse(
        gen(), media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


# ── Dogfood failure capture (⚑ in chat UI -> append to backlog file) ──


class FlagRequest(BaseModel):
    question: str = Field("", max_length=10000)
    answer: str = Field("", max_length=50000)
    note: str = Field("", max_length=2000)
    model: str | None = Field(None, max_length=120)


@api_router.post("/flag")
def flag(body: FlagRequest, request: Request):
    """Append a flagged Q/A + note to the dogfood backlog (settings.dogfood_log_path).
    Single-user localhost tool: turns weak answers into a durable, prioritisable list
    instead of forgotten frustration. The file is a personal local log (not rendered to
    other users), so raw markdown in the fields is acceptable; the answer is wrapped in a
    <details> block so it can't bleed into the heading structure."""
    s = request.app.state.settings
    path = s.dogfood_log_path
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    note = body.note.strip() or "(no note)"
    entry = (
        f"\n## {ts}" + (f" · {body.model}" if body.model else "") + "\n\n"
        f"**Q:** {body.question.strip()}\n\n"
        f"**Note:** {note}\n\n"
        f"<details><summary>answer</summary>\n\n{body.answer.strip()}\n\n</details>\n\n---\n"
    )
    try:
        new = not path.exists()
        with path.open("a", encoding="utf-8") as f:
            if new:
                f.write(
                    "# Dogfood failure log\n\n"
                    "> chat UI 里 ⚑ 标记的答错/答弱例 + 期望, 作优先级 backlog "
                    "(append-only, 规则 B 失败不删)。\n"
                )
            f.write(entry)
    except OSError as e:
        log.error("flag_write_failed", error=str(e), path=str(path))
        raise HTTPException(status_code=500, detail="Could not write the flag log.") from e
    log.info("flag", question=body.question[:100], note=note[:120], path=str(path))
    return {"ok": True}


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
    from server.auth import sanitize_compare_errors
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
        raise HTTPException(status_code=502, detail="Retrieval service temporarily unavailable.") from e

    context = rag.format_context(chunks)
    history_dicts = [{"role": m.role, "content": m.content} for m in body.history]
    messages = rag.build_messages(body.question, context, history_dicts or None)

    # Outer ceiling over the whole parallel fan-out (REV MED-b): per-model timeout is
    # compare_timeout_s; this guards the request from exceeding request_timeout_s even if a
    # provider ignores its own timeout. wait_for cancels the pending gather on expiry.
    try:
        answers = await asyncio.wait_for(
            run_compare(
                models, messages,
                timeout_s=s.compare_timeout_s, num_retries=s.compare_num_retries,
            ),
            timeout=s.request_timeout_s,
        )
    except TimeoutError:
        log.error("ask_compare_timeout", request_timeout_s=s.request_timeout_s, models=models)
        raise HTTPException(status_code=504, detail="Compare request timed out.") from None

    judge_result = None
    if body.judge.enabled:
        judge_model = body.judge.model or s.judge_model
        try:
            judge_raw = await asyncio.wait_for(
                run_judge(
                    body.question, context, answers, judge_model,
                    timeout_s=s.compare_timeout_s, num_retries=s.compare_num_retries,
                ),
                timeout=s.request_timeout_s,
            )
        except TimeoutError:
            log.warning("judge_timeout", request_timeout_s=s.request_timeout_s)
            judge_raw = None
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

    # Sanitize client-facing per-model error strings when sharing (SEC MED). Done AFTER the
    # judge + the n_errors log so neither loses the real upstream detail (still in the log).
    answers = sanitize_compare_errors(answers, s.sanitize_errors)

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
    from scripts.parse_dataset import ParseError, parse_bytes
    from server.report import FullReport, generate_json
    from server.reviewer import review
    from server.validator import validate

    spec_loader = request.app.state.spec_loader
    t0 = time.perf_counter()

    data = await file.read()
    filename = file.filename or "upload.csv"
    log.info("validate_start", filename=filename, size=len(data), domain=domain)

    try:
        df, meta = parse_bytes(data, filename)
    except ParseError as e:
        raise HTTPException(status_code=422, detail=str(e)) from e

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
            raise HTTPException(status_code=422, detail=f"DM file error: {e}") from e

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


@api_router.post("/validate-study")
async def validate_study(
    request: Request,
    files: list[UploadFile] = File(...),
):
    """Validate a multi-domain SDTM study: per-domain rule validation + SP5 graph
    checks (impact/completeness/CT-cascade) over the whole submission. Study-level is
    deterministic rule + graph checks only (no per-domain semantic LLM review)."""
    import pandas as pd

    from scripts.parse_dataset import ParseError, parse_bytes
    from server.config import settings
    from server.graph_engine import GraphEngine
    from server.graph_validator import run_graph_checks
    from server.meta_store import MetaStore
    from server.report import FullReport, generate_study_json
    from server.validator import validate

    spec_loader = request.app.state.spec_loader
    t0 = time.perf_counter()

    per_dataset: list[FullReport] = []
    frames: dict[str, pd.DataFrame] = {}  # domain -> DataFrame (for graph checks)
    for uf in files:
        data = await uf.read()
        fname = uf.filename or "upload.csv"
        try:
            df, meta = parse_bytes(data, fname)
        except ParseError as e:
            raise HTTPException(status_code=422, detail=f"{fname}: {e}") from e
        dom = (meta.domain or "").upper()
        if not dom:
            raise HTTPException(
                status_code=422,
                detail=f"{fname}: cannot detect domain (need a DOMAIN column).",
            )
        val = validate(df, dom, spec_loader)
        per_dataset.append(FullReport(
            domain=dom, file_path=fname, row_count=meta.row_count,
            col_count=meta.col_count, completeness_pct=val.completeness_pct,
            validation=val, review=None,
        ))
        frames[dom] = df

    engine = getattr(request.app.state, "graph_engine", None)
    if engine is None:  # bare-app / test path without lifespan
        engine = GraphEngine(MetaStore(settings.meta_path))
    graph_findings = run_graph_checks(frames, engine)
    out = generate_study_json(per_dataset, graph_findings)

    log.info("validate_study_done", n=len(files), verdict=out["study_verdict"],
             elapsed_s=round(time.perf_counter() - t0, 2))
    return out
