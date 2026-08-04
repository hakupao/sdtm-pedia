"""Application settings (pydantic-settings, loaded from .env).

PLAN §4 decision table + .env.example define all knobs.
API keys are loaded into os.environ via dotenv for LiteLLM auto-detection.
App settings use SDTM_RAG_ prefix.
"""
from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

_SDTM_RAG_ROOT = Path(__file__).resolve().parent.parent
_REPO_ROOT = _SDTM_RAG_ROOT.parent  # sdtm-pedia repo root

load_dotenv(_SDTM_RAG_ROOT / ".env")


class Settings(BaseSettings):
    # LLM models (PLAN §4.2 D-2)
    default_model: str = "anthropic/claude-sonnet-4-6"
    fallback_model: str = "deepseek/deepseek-v4-pro"
    hard_model: str = "anthropic/claude-opus-4-7"
    light_model: str = "anthropic/claude-haiku-4-5"

    # Embedding (D-4 v3: OpenAI cloud)
    embedding_model: str = "text-embedding-3-small"
    embedding_dim: int = 1536

    # RAG
    top_k: int = 15
    collection_name: str = "sdtm_kb_v1"

    # ── Plan B 联邦路由 (spec docs/superpowers/specs/2026-08-04-plan-b-federated-routing-design.md) ──
    # 默认关; Phase 1 全部 eval 闸过绿后翻 True (含义: 服务启动时构建 study 引擎 + 联邦层)。
    federation_enabled: bool = False
    study_collection_name: str = "study_st01"
    # study 侧 KB 根。RAGEngine 要求 kb_root 下直接躺着 ROUTING.md + INDEX.md, 而 study 侧这两个
    # 文件与 959 张卡同在 cards/ (scripts/study/paths.py: cards_dir = out_dir / "cards"), 所以根
    # 指到 cards/ 而不是 st01/ —— 指错时开着 federation 启动即 FileNotFoundError。仿 kb_root 的
    # 默认构造方式从模块级根常量拼出; 服务目录自包含部署用 SDTM_RAG_STUDY_KB_ROOT 覆盖。
    study_kb_root: Path = _SDTM_RAG_ROOT / "data" / "study" / "st01" / "cards"

    # Rerank (T2, PLAN §5 1B.2): wide retrieve -> Cohere rerank -> top_k.
    # COHERE_API_KEY read from env (LiteLLM-style provider key, no SDTM_RAG_ prefix).
    # NOTE: T2 ablation (2026-06-08) found rerank degrades source recall on this KB
    # (demotes structured spec.md). Kept off by default; see eval/ablation_retrieval_2026-06-08.md.
    rerank_enabled: bool = False
    rerank_model: str = "rerank-v3.5"
    rerank_candidates: int = 100  # candidate pool size before rerank (T1: ~100 needed)

    # Query expansion (T4): improve cosine recall by rewriting the query, NOT by
    # reordering results. "multiquery" = LLM decomposes -> per-subquery search -> RRF
    # fuse. "hyde" = LLM writes a hypothetical answer, embed that. Generic prompts
    # (not tuned to any eval set). expansion_model uses an existing cloud key.
    query_expansion: str = "none"  # none | multiquery | hyde
    expansion_model: str = "deepseek/deepseek-chat"
    expansion_n_queries: int = 4  # multiquery: original + (n-1) generated sub-queries

    # ── P1 retrieval levers (validated combination, default ON in production) ──
    # S1 + S2 are the validated P1 query-condition-routing combination (retrieval-
    # only v2 102q: single 100 / cross 96 / concept 100 / mixed 100 / overall 99.0%,
    # 2026-06-09). They MUST ship together: hybrid alone demotes single_domain
    # (96→83); only S1's deterministic prepend + routing keeps the combination
    # stable. Each is env-overridable (SDTM_RAG_STRUCTURED_LOOKUP_ENABLED=false /
    # SDTM_RAG_HYBRID_ENABLED=false) for an instant rollback to plain cosine.

    # Structured lookup (S1): deterministic var/CT-code -> gold-file resolution on a
    # non-vector channel (spec.md xref + VARIABLE_INDEX), union-added ahead of cosine
    # for terminology/distribution queries embeddings can't reach. Zero side effect
    # (union-add, capped at top_k), so safe to default on.
    structured_lookup_enabled: bool = True

    # Hybrid BM25 (S2): lexical retrieval over the SAME indexed chunks (bm25s, pure
    # CPU arithmetic — no neural model), additively fused with dense cosine so
    # literal domain/relationship/variable-name hits that cosine buries re-float
    # without demoting cosine's wins. RRF is parameter-free; the weighted path's
    # alpha is the dense weight (1-alpha goes to BM25).
    hybrid_enabled: bool = True
    hybrid_fusion: str = "rrf"  # rrf | weighted
    hybrid_alpha: float = 0.5
    hybrid_pool: int = 30  # per-list fusion pool depth (v2 robust sweet spot; deeper adds tail noise)

    # ── Answer-side trust guardrail (system-prompt only; orthogonal to retrieval) ──
    # Two grounding rules appended to the system prompt that forbid the answering
    # model from emitting content the retrieved context does not contain:
    #   (1) never output a controlled-terminology code (Cxxxxx) not present verbatim
    #       in context — fixes per-value CT-code fabrication (q90/q91/q93, where the
    #       model copied one code then guessed the rest by incrementing);
    #   (2) never assert a domain's SDTM class/category unless context states it —
    #       fixes special-purpose misclassification of relationship datasets (q37).
    # These are answer-side defects present OFF and ON the retrieval levers, surfaced
    # by the P1 wire-in Rule A semantic judge; substring fact-recall is blind to them.
    # Env-overridable (SDTM_RAG_PROMPT_GUARDRAIL_ENABLED=false) for an A/B rollback;
    # when off, the system prompt is byte-identical to the pre-guardrail production one.
    prompt_guardrail_enabled: bool = True

    # ── Structured answer channel (SP2): deterministic count/enumerate/attribute/CT
    # answers from data/meta/meta.yaml, injected as an authoritative context block +
    # a counting grounding gate. Orthogonal to retrieval (Phase 1 never touches
    # retrieve()). Default ON: validated by the OFF-vs-ON paired eval (v3 140q,
    # 2026-06-20) — q103/q104 green, zero retrieval regression, 0 gate violations
    # (gate v2) + Rule D APPROVE + Rule A PASS. Env-overridable for instant rollback
    # (SDTM_RAG_STRUCTURED_ANSWER_ENABLED=false).
    structured_answer_enabled: bool = True

    # SP3: deterministic relationship/impact/aggregate graph answers from meta.yaml,
    # merged into the structured-answer injection. Default ON after validation
    # (140q zero-pollution=0 + composite ON==OFF byte-identical + Rule D APPROVE);
    # env-overridable (SDTM_RAG_GRAPH_ANSWER_ENABLED=false) for rollback.
    graph_answer_enabled: bool = True

    # AGG: aggregate metadata channel (variables-in-min-domains / most-shared
    # codelists), split out of SP3 after the KG value eval (its only positive niche).
    # Default ON since 2026-07-07 (five AGG gates passed, see
    # evidence/checkpoints/agg_channel_summary.md); env override:
    # SDTM_RAG_AGGREGATE_ANSWER_ENABLED.
    aggregate_answer_enabled: bool = True

    # ── Multi-model compare + judge (Phase 2; DEPLOY_PLAN §2.5–2.7) ──
    # One question → these N models answer over the SAME retrieved context (FR1),
    # shown side-by-side; an optional judge scores the anonymized answers (FR5).
    # FR7: every slot is env/UI-overridable and accepts ANY litellm model string.
    # These are REFERENCE PLACEHOLDERS — DEPLOY_PLAN §7 marks slot defaults as
    # explicitly non-binding (one Anthropic + one OpenAI + one DeepSeek for vendor
    # diversity). Override via .env using JSON list syntax, e.g.
    #   SDTM_RAG_COMPARE_MODELS=["deepseek/deepseek-v4-pro","openai/gpt-4o"]
    # (pydantic-settings parses complex fields as JSON); the UI sidebar exposes a
    # friendly per-slot text box that does not require touching .env.
    compare_models: list[str] = [
        "deepseek/deepseek-v4-pro",
        "openai/gpt-4o",
        "anthropic/claude-sonnet-4-6",
    ]
    # Judge model (DEPLOY_PLAN §2.6). Default = deepseek/deepseek-chat so the judge
    # is runnable TODAY (Anthropic credits exhausted, 2026-06-15). §2.6 prefers Opus
    # for judge quality once credits return — set SDTM_RAG_JUDGE_MODEL then.
    judge_model: str = "deepseek/deepseek-chat"
    # Per-model generation timeout (s): one slow/hung vendor must not stall the whole
    # parallel request beyond this (NFR2/NFR4). Each model also gets one retry.
    compare_timeout_s: float = 120.0
    compare_num_retries: int = 1

    # Server
    log_level: str = "INFO"
    # Loopback by default (DEPLOY_PLAN §1: 阶段 0–2 绑 127.0.0.1, zero exposure). The
    # launchd plists already pass --host 127.0.0.1 explicitly; this default makes a bare
    # `python -m server.main` safe too. Set SDTM_RAG_HOST=0.0.0.0 explicitly for the
    # phase-3 shared/container binding (which also adds the §7 login gate).
    host: str = "127.0.0.1"
    port: int = 8000

    # ── Phase 3 sharing: login gate + hardening (DEPLOY_PLAN §3) ──
    # Every knob below defaults OFF/permissive so the current localhost dev + launchd
    # service are byte-unchanged. They are flipped ON together at go-live (after IT
    # signoff) via the service-dir .env (see deploy/). Building + testing them here
    # touches no live behavior. SECURITY HEADERS are the one exception — default ON
    # (harmless on localhost, good practice everywhere).

    # Shared-password login gate. When auth_enabled, requests to GET / and /api/* (except
    # /api/health and the /login,/logout routes) require a signed session cookie obtained
    # by POSTing the shared password to /login. The password is stored ONLY as a scrypt
    # hash (server/auth.hash_password -> "salt_hex$hash_hex"); generate via
    # `python -m scripts.gen_password_hash`. session_secret signs the cookie (itsdangerous
    # via Starlette SessionMiddleware) — set to >=32 random bytes hex. Both MUST be set
    # when auth_enabled or the app refuses to start (fail-loud, never silent allow-all).
    auth_enabled: bool = False
    shared_password_hash: str = ""
    session_secret: str = ""
    # 12h. The itsdangerous-signed cookie's max_age is the SERVER-enforced absolute session
    # cap (Starlette rejects an older signed session — the client cannot extend it). A short
    # window limits replay of a sniffed cookie (plain-HTTP-on-LAN residual risk). Rotating
    # SDTM_RAG_SESSION_SECRET is the only revocation lever and is global (logs everyone out).
    session_max_age_s: int = 43200
    session_cookie_name: str = "sdtm_session"

    # Error-string sanitization (SEC MED, deferred from phase 2). On localhost the upstream
    # error text ("credit balance too low") is USEFUL to the single operator, so default
    # OFF. At go-live (shared) set true: /api/ask_compare per-model errors collapse to a
    # generic string for the client; the full detail stays in the server log.
    sanitize_errors: bool = False

    # Per-IP rate limit (hand-rolled in-memory token bucket; no new dep). Applies to all
    # HTTP except /api/health. burst = bucket capacity (max instantaneous), per_min = refill
    # rate. Generous for humans, throttles brute-force / runaway scripts. Single-process /
    # single Mac mini scope (§1); a multi-worker move (§6) would need shared state.
    rate_limit_enabled: bool = False
    rate_limit_per_min: int = 30
    rate_limit_burst: int = 10
    # Trust X-Forwarded-For for the client IP. FALSE by default: §1 serves 8000 directly
    # (no reverse proxy), so the socket peer IS the client and a spoofed XFF must be ignored.
    # Set true ONLY behind a trusted reverse proxy that overwrites the header (§6).
    rate_limit_trust_forwarded: bool = False

    # Security response headers (CSP / X-Content-Type-Options / frame-ancestors etc.).
    # Default ON — the chat UI loads only same-origin assets (vendored marked/dompurify/
    # highlight + app.js), so a strict CSP is defense-in-depth atop DOMPurify.
    security_headers_enabled: bool = True

    # Outer ceiling (s) on a single async /api request's generation phase, on top of
    # litellm's per-call timeout. Guards an unbounded wait if a provider hangs without
    # honoring its own timeout (REV MED-b). Applied to /api/ask_compare's fan-out and the
    # /api/ask_stream open step.
    request_timeout_s: float = 180.0

    # Self-contained service dir overrides (DEPLOY_PLAN §1 + §7 open item): deploy.sh
    # copies knowledge_base/ and data/chroma into ~/MyProject/sdtm-rag-service/ so the service no
    # longer depends on the repo tree. Set SDTM_RAG_KB_ROOT / SDTM_RAG_CHROMA_DIR there.
    # Empty (default) = use the repo-relative paths below (dev / current localhost).
    kb_root_override: str = ""
    chroma_dir_override: str = ""
    dogfood_log_override: str = ""

    model_config = {"env_prefix": "SDTM_RAG_", "extra": "ignore"}

    @property
    def chroma_dir(self) -> Path:
        return Path(self.chroma_dir_override) if self.chroma_dir_override else _SDTM_RAG_ROOT / "data" / "chroma"

    @property
    def kb_root(self) -> Path:
        return Path(self.kb_root_override) if self.kb_root_override else _REPO_ROOT / "knowledge_base"

    @property
    def meta_path(self) -> Path:
        return _SDTM_RAG_ROOT / "data" / "meta" / "meta.yaml"

    @property
    def dogfood_log_path(self) -> Path:
        # Append-only backlog of chat answers flagged as wrong/weak (⚑ in the chat UI).
        return (
            Path(self.dogfood_log_override)
            if self.dogfood_log_override
            else _SDTM_RAG_ROOT / "dogfood_failures.md"
        )


settings = Settings()
