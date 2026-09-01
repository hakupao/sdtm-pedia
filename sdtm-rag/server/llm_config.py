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
    # 用户可选模型: 每个 SelectableModel 派生一个同名组 (spec §3.3)。与上面四个内部组
    # 并存 —— default/hard/light 是内部用途 (判库/改写), 不受用户选择影响 (C1)。
    model_list += [
        {"model_name": m.id, "litellm_params": {"model": m.model}}
        for m in s.selectable_models
    ]
    return Router(
        model_list=model_list,
        fallbacks=[{"default": ["default-fallback"]}],
        num_retries=1,
        timeout=120,
    )


INTERNAL_GROUPS = ("default", "default-fallback", "hard", "light")


def known_model_groups(s: Settings) -> set[str]:
    """Router 会有的全部组名。

    `create_router` 与 `/api/ask_stream` 的白名单校验**共用**本函数, 故"能选的"与
    "能调的"不存在两份定义。校验端不读 `llm_router.model_list` 是有意的: 仓库里 4 个
    测试文件约 15 处假 Router 都没有该属性, 而用 getattr 兜底会造出"没有 model_list
    就不校验"的静默旁路。等式由下面的闸钉住。
    """
    return set(INTERNAL_GROUPS) | {m.id for m in s.selectable_models}
