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
_REPO_ROOT = _SDTM_RAG_ROOT.parent.parent.parent  # sdtm-pedia repo root

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

    model_config = {"env_prefix": "SDTM_RAG_", "extra": "ignore"}

    @property
    def chroma_dir(self) -> Path:
        return _SDTM_RAG_ROOT / "data" / "chroma"

    @property
    def kb_root(self) -> Path:
        return _REPO_ROOT / "knowledge_base"


settings = Settings()
