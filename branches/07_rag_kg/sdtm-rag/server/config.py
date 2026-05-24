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

    # Server
    log_level: str = "INFO"
    host: str = "0.0.0.0"
    port: int = 8000

    model_config = {"env_prefix": "SDTM_RAG_", "extra": "ignore"}

    @property
    def chroma_dir(self) -> Path:
        return _SDTM_RAG_ROOT / "data" / "chroma"

    @property
    def kb_root(self) -> Path:
        return _REPO_ROOT / "knowledge_base"


settings = Settings()
