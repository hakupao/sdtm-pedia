"""LiteLLM Router configuration (PLAN §4.2, R-8).

Model groups:
- "default": Sonnet primary -> DeepSeek non-thinking fallback
- "hard": Opus (complex semantic review / dataset validation)
- "light": Haiku (intent classification / routing)
"""
from __future__ import annotations

from litellm import Router

from server.config import Settings


def create_router(s: Settings) -> Router:
    model_list = [
        {
            "model_name": "default",
            "litellm_params": {"model": s.default_model},
        },
        {
            "model_name": "default-fallback",
            "litellm_params": {"model": s.fallback_model},
        },
        {
            "model_name": "hard",
            "litellm_params": {"model": s.hard_model},
        },
        {
            "model_name": "light",
            "litellm_params": {"model": s.light_model},
        },
    ]
    return Router(
        model_list=model_list,
        fallbacks=[{"default": ["default-fallback"]}],
        num_retries=1,
        timeout=120,
    )
