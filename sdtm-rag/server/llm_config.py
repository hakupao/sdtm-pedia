"""LiteLLM Router configuration (PLAN §4.2, R-8).

Model groups:
- "default": Sonnet primary -> DeepSeek non-thinking fallback
- "hard": Opus (complex semantic review / dataset validation)
- "light": Haiku (intent classification / routing)
"""
from __future__ import annotations

from litellm import Router

from server.config import Settings, SelectableModel


INTERNAL_GROUPS = ("default", "default-fallback", "hard", "light")


def _validated_selectable_models(s: Settings) -> list[SelectableModel]:
    """`s.selectable_models`, 但先 fail-loud 挡住与 INTERNAL_GROUPS 撞名的 id。

    撞名不是假设性风险: litellm `Router` 允许同一 `model_name` 出现多次并把它们
    当同一组的多个 deployment 做 load-balance (实测 `get_model_ids("hard")` 会
    返回两个)。一旦撞名, 判库(light)/检索改写(hard/default) 就会被用户选的答题
    模型悄悄混进去, 且不会有任何测试变红 —— 静默打破 spec C1。selectable_models
    还能被 `SDTM_RAG_SELECTABLE_MODELS` 在运行时用 JSON 覆盖, 所以只在测试里挡
    默认配置不够, 必须在这个两处 (`create_router` / `known_model_groups`) 共用
    的读取点上就地拒绝。
    """
    collisions = {m.id for m in s.selectable_models} & set(INTERNAL_GROUPS)
    if collisions:
        raise ValueError(
            f"selectable_models 里的 id {sorted(collisions)} 与内部组 "
            f"{INTERNAL_GROUPS} 撞名 —— 会被 litellm Router 当同一组的额外 "
            "deployment 合并 load-balance, 静默打破 C1 (判库/检索改写不受用户 "
            "选择影响)。请换一个不冲突的 id。"
        )
    return s.selectable_models


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
        for m in _validated_selectable_models(s)
    ]
    return Router(
        model_list=model_list,
        fallbacks=[{"default": ["default-fallback"]}],
        num_retries=1,
        timeout=120,
    )


def known_model_groups(s: Settings) -> set[str]:
    """Router 会有的全部组名 —— Task 5 白名单校验读的"意图"侧。

    `create_router` 与 `/api/ask_stream` 的白名单校验**共用**本函数, 故"能选的"与
    "能调的"不存在两份定义。校验端不读 `llm_router.model_list` 是有意的: 仓库里 4 个
    测试文件约 15 处假 Router 都没有该属性, 而用 getattr 兜底会造出"没有 model_list
    就不校验"的静默旁路。

    注意本函数的边界: 它不防"派生逻辑本身漂移"(例如 `create_router` 和这里同时手滑
    把 `m.id` 写成 `m.label`) —— 那种漂移会让"意图"与"事实"错得一致, 靠等式闸测不
    出来, 真正防住它的是直接锚定字面量的
    `test_router_derives_a_group_per_selectable_model` /
    `test_router_group_maps_to_the_configured_model_string`。本函数只保证"校验端
    读到的意图"与"Router 实际构造出的事实"这两份独立计算不会各走各的, 那条等式由
    `test_known_groups_equals_what_router_actually_has` 钉住。
    """
    return set(INTERNAL_GROUPS) | {m.id for m in _validated_selectable_models(s)}
