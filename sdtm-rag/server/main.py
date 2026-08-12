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
    """Build the SP2 structured answerer, the AGG aggregate answerer, and the SP3
    graph answerer (each flag-gated), composed so resolve() returns merged facts.
    Returns None if all are off. Kept tiny/pure so it unit-tests without spinning up
    FastAPI/RAGEngine."""
    answerers = []
    if s.structured_answer_enabled or s.graph_answer_enabled or s.aggregate_answer_enabled:
        from server.meta_store import MetaStore
        store = MetaStore(s.meta_path)
        engine = None
        if s.aggregate_answer_enabled or s.graph_answer_enabled:
            from server.graph_engine import GraphEngine
            engine = GraphEngine(store)
        if s.structured_answer_enabled:
            from server.structured_answer import StructuredAnswerer
            answerers.append(StructuredAnswerer(store))
        if s.aggregate_answer_enabled:
            from server.aggregate_answer import AggregateAnswerer
            answerers.append(AggregateAnswerer(engine))
        if s.graph_answer_enabled:
            from server.graph_answer import GraphAnswerer
            answerers.append(GraphAnswerer(engine))
    if not answerers:
        return None
    if len(answerers) == 1:
        return answerers[0]
    from server.structured_answer import CompositeAnswerer
    return CompositeAnswerer(answerers)


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
    if s.structured_lookup_enabled:
        # S1 的 VARIABLE_INDEX 字面 section 映射在启动期预热一次。
        # 这条不是性能优化, 是把失败点从请求期挪到部署动作: 映射依赖 chroma 元数据里的
        # source 绝对路径与 kb_root 对得上, 而 deploy.sh 把 data/chroma 与 knowledge_base
        # 一起拷到新目录时, chroma 里存的仍是构建树的路径 → 映射为空。若留到请求期才炸,
        # 每个 CT 码/分布类问句都会 502 (v3 题集 140 题里 71 题走这条路), 运维只看到
        # "偶发 502"; 在这里炸则 launchd 启动即失败, 写进 logs/api.launchd.log。
        # 预热成功后表已缓存, 请求期那条 raise 在 **server 路径下**不可达 —— 但
        # eval/run_eval.py 与 eval/prod_wirein/* 直接构造 RAGEngine, 不走 lifespan,
        # 仍会在跑批中途撞上它 (那对批处理正是想要的行为: 响亮, 且没有用户可 502)。
        # 故那条 raise 不是死代码, 删了 eval 侧就退回静默降级。
        vi_map = app.state.rag._vi_section_map()
        log.info("s1_vi_section_map", entries=len(vi_map))
    app.state.llm_router = create_router(s)
    app.state.federation = None
    # S2 只挂在 study 引擎上, 而 study 引擎只在联邦分支存在。先置空, 好让下面的 ready 日志
    # 报告"实际加载了什么"而不是"开关写了什么" —— 两者可以不一致 (见下方 elif)。
    study_lookup = None
    if s.federation_enabled:
        # study 引擎: S1 结构化直查是 CDISC 专用故恒关 (先例: run_eval --collection 同此);
        # S2 (study_lookup) 按 settings 开关注入; hybrid 沿用生产开关 (study 侧经
        # ja_tokenize 天然获得 CJK bigram)。
        # 配置错误 (collection 不存在/ROUTING.md 缺失) 一律 fail loud — 显式开着 federation
        # 却静默退化成单库, 比启动失败更危险。
        if s.study_lookup_enabled:
            from server.study_lookup import StudyLookup
            # catalog 缺失时这里响亮失败 — 开关开着但数据不在 = 配置错误, 不静默降级
            study_lookup = StudyLookup.from_paths(s.study_catalog_path, s.study_aliases_path)
        rag_study = RAGEngine(
            chroma_dir=s.chroma_dir,
            kb_root=s.study_kb_root,
            collection_name=s.study_collection_name,
            embedding_model=s.embedding_model,
            top_k=s.top_k,
            structured_lookup_enabled=False,
            study_lookup=study_lookup,
            hybrid_enabled=s.hybrid_enabled,
            hybrid_fusion=s.hybrid_fusion,
            hybrid_alpha=s.hybrid_alpha,
            hybrid_pool=s.hybrid_pool,
            prompt_guardrail_enabled=s.prompt_guardrail_enabled,
        )
        study_engine = rag_study
        if s.study_docs_enabled:
            # collection 缺失 = 配置错误, 响亮失败 (与 federation 同纪律): 显式开着 doc 通道
            # 却静默退化成纯卡片, 比启动失败更危险 —— 它表现为"接了线但一条 doc 都不出现"。
            rag_docs = RAGEngine(
                chroma_dir=s.chroma_dir,
                # docs/ 没有 ROUTING.md/INDEX.md, 而 kb_root 只进 system prompt 不参与检索;
                # 这里与 U1 测上界时逐字同一条路径, 数字因此可比。system_prompt 不被读 ——
                # StudyCorpusEngine 只用 cards 引擎那份 (test_study_corpus 已钉死)。
                kb_root=s.study_kb_root,
                collection_name=s.study_docs_collection_name,
                embedding_model=s.embedding_model,
                top_k=s.study_docs_seats,
                structured_lookup_enabled=False,
                hybrid_enabled=s.hybrid_enabled,
                hybrid_fusion=s.hybrid_fusion,
                hybrid_alpha=s.hybrid_alpha,
                hybrid_pool=s.hybrid_pool,
                prompt_guardrail_enabled=s.prompt_guardrail_enabled,
            )
            from server.study_corpus import StudyCorpusEngine
            study_engine = StudyCorpusEngine(rag_study, rag_docs, doc_seats=s.study_docs_seats)
            log.info("study_docs", collection=s.study_docs_collection_name,
                     seats=s.study_docs_seats, chunks=rag_docs.collection.count())
        from server.federation import FederatedEngine
        app.state.federation = FederatedEngine(
            app.state.rag, study_engine, app.state.llm_router, top_k=s.top_k
        )
        log.info(
            "federation",
            study_collection=s.study_collection_name,
            # 条数而非 ON/OFF: 别名表缺失走的是静默降级, "0 aliases" 是唯一的现场线索
            study_lookup=study_lookup.stats() if study_lookup is not None else "OFF",
        )
    elif s.study_lookup_enabled:
        # 开关开着却没有 study 引擎可挂 (典型: 临时关联邦调试, 忘了这条还开着)。不拒启动 ——
        # 但必须留声, 否则表现为"S2 开着却毫无效果"且零线索, 与 catalog 缺失响亮失败不一致。
        log.warning(
            "study_lookup_ignored",
            note="study_lookup_enabled=true 但 federation_enabled=false; S2 只挂在联邦的 "
                 "study 引擎上, 本次启动未加载",
        )
    if s.study_docs_enabled and not s.federation_enabled:
        log.warning(
            "study_docs_ignored",
            note="study_docs_enabled=true 但 federation_enabled=false; doc 通道只挂在联邦的 "
                 "study 引擎上, 本次启动未加载",
        )
    app.state.answerer = maybe_build_answerer(s)
    if app.state.answerer is not None:
        log.info(
            "answer_channels",
            structured=s.structured_answer_enabled,
            aggregate=s.aggregate_answer_enabled,
            graph=s.graph_answer_enabled,
        )
    app.state.spec_loader = SpecLoader(s.kb_root)
    log.info("spec_loader", domains=len(app.state.spec_loader.domains),
             codelists=len(app.state.spec_loader.codelists))
    # SP5 graph validator reference (over meta.yaml). Built once here so /validate-study
    # reuses it instead of re-parsing meta.yaml per request.
    from server.graph_engine import GraphEngine
    from server.meta_store import MetaStore
    app.state.graph_engine = GraphEngine(MetaStore(s.meta_path))
    log.info("graph_engine", domains=app.state.graph_engine.store.n_domains)
    # 索引陈旧闸: 灌库与重启都是人工动作, 没有闸就会漂 —— 实测部署索引曾把一个 KB 文件
    # 欠切 70% 且跨越 chunker 演进无人察觉 (CDISC recall 白丢 5.7pt)。算一次存 state,
    # /api/info 也读它。判不出来一律按陈旧 (fail loud), 但只告警不拒启动: 拒启会把
    # 一个可用但略旧的服务变成不可用的服务。
    from scripts.kb_freshness import check_freshness
    _fresh = check_freshness(s.chroma_dir / "ingested_at_commit.txt", s.kb_root)
    app.state.index_fresh = _fresh.fresh
    app.state.index_freshness_reason = _fresh.reason
    if not _fresh.fresh:
        log.error("index_stale", reason=_fresh.reason,
                  fix="python -m scripts.ingest, then restart")

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
        # 报告实际加载结果 (条数) 而非开关值: 开关开着但没加载是一条不会崩的失效路径
        study_lookup=study_lookup.stats() if study_lookup is not None else False,
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
