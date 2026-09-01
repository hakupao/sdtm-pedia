"""LiteLLM Router configuration (PLAN §4.2, R-8).

Model groups:
- "default": Sonnet primary -> DeepSeek non-thinking fallback
- "hard": Opus (complex semantic review / dataset validation)
- "light": Haiku (intent classification / routing)
"""
from __future__ import annotations

import litellm
from litellm import Router

from server.config import Settings, SelectableModel


INTERNAL_GROUPS = ("default", "default-fallback", "hard", "light")

# 内部组名 → Settings 上存它模型串的字段名。写成显式表而不是 f"{group}_model" 拼字符串:
# 拼名字在字段改名时不会报错, 只会静默少检一个模型 —— 正是闸 6 已经栽过一次的形状
# (它只扫 selectable_models, 而那四条硬编码全是 bedrock/, 于是默认配置下结构上不可能报警)。
# 表里缺项则 KeyError 当场炸在启动路径上, 比静默漏检好。
# 与 INTERNAL_GROUPS 的一一对应由 test_model_switching 钉住, 新增内部组必须同步这里。
_INTERNAL_GROUP_MODEL_FIELDS = {
    "default": "default_model",
    "default-fallback": "fallback_model",
    "hard": "hard_model",
    "light": "light_model",
}

# C3 检查豁免: fallback 默认就是 DeepSeek 个人流量, 用户已明确裁定接受 (spec §9 D4)。
# 把它纳入会产生恒定假阳性, 而一条长期喊狼来了的告警等于没有告警。
_C3_EXEMPT_GROUPS = ("default-fallback",)


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


def non_bedrock_model_groups(s: Settings) -> list[str]:
    """C3 闸 (spec §8 闸 6): 报出模型串**不走公司 Bedrock** 的全部 Router 组名。

    检查集合 = 内部组 (default/hard/light, 经 `_INTERNAL_GROUP_MODEL_FIELDS` 取字段)
    ∪ selectable_models, **不含** default-fallback (见 `_C3_EXEMPT_GROUPS`)。

    ⚠ 内部三组是这条闸的**主要**目标, 不是附带: spec §8 闸 6 的脚注点名的正是
    「`server/config.py` 里三个 Claude 模型的硬编码默认值是 `anthropic/` 直连,
    只有 `.env` 把它们改写成 Bedrock, 且无任何启动期校验」。selectable_models 那
    四条硬编码本来就全是 `bedrock/`, 只扫它们的话默认配置下返回值恒为 `[]` ——
    结构上不可能报警, 而闸要防的失败 (.env 缺一段、或两段并列时顺序一换) 全在
    内部三组上。`default` 组还是 `/api/ask`、eval 脚本、以及 Chat UI 在 /api/info
    加载失败时的降级落点。

    C3 与 C1 正交, 纳入 light/hard **不**触碰 C1: 本函数只读模型串判前缀、结果进
    ready 日志, 不往 model_list 加组、不进 known_model_groups、不进 /api/info、
    不碰答题请求的 `kw["model"]`。C1 管"谁能被用户切", C3 管"钱走谁的账"。

    返回组名列表; 空列表 = 全部合规。告警不阻止启动 (spec §8 闸 6)。
    """
    off = [
        g for g in INTERNAL_GROUPS
        if g not in _C3_EXEMPT_GROUPS
        and not getattr(s, _INTERNAL_GROUP_MODEL_FIELDS[g]).startswith("bedrock/")
    ]
    off += [m.id for m in _validated_selectable_models(s)
            if not m.model.startswith("bedrock/")]
    return off


def register_selectable_model_capabilities(s: Settings) -> None:
    """给可选模型补 LiteLLM 能力元数据。

    为什么需要: LiteLLM 的 bedrock provider allowlist 只认
    anthropic|mistral|cohere|meta.llama3-*|amazon.nova, 其余走 supports_function_calling()
    兜底, 而 registry 里没有 openai.gpt-5.6-* ⇒ 拒收 tools, 联网通道对 GPT 不可用。
    裸 boto3 Converse 已实测工具调用本身是通的 ⇒ 客户端元数据缺口, 非服务端限制。

    ⚠ 注册 key 必须是**去掉 bedrock/ 前缀**的形式 (litellm 内部就用这个查表)。
    用带前缀的 key 注册会**静默无效** —— 不报错, 直到有人开联网才炸。

    经 `_validated_selectable_models` 读取 (与 `create_router` / `known_model_groups`
    同一道 fail-loud 撞名闸), 不直接读 `s.selectable_models`。

    非 Bedrock 的模型跳过注册 (这里的元数据写死 `bedrock_converse` provider, 套到别的
    provider 上是错的)。它们的合规问题由 `non_bedrock_model_groups` 管 —— C3 告警是
    一个函数一个口径, 不在这里分一半出去。
    """
    info = {"litellm_provider": "bedrock_converse", "mode": "chat",
            "supports_function_calling": True}
    for m in _validated_selectable_models(s):
        if not m.model.startswith("bedrock/"):
            continue
        litellm.register_model({m.model.removeprefix("bedrock/"): dict(info)})


def verify_selectable_model_capabilities(s: Settings) -> list[str]:
    """spec §4.2 启动期自检: `register_model()` 跑过不等于生效 (实测带前缀的 key
    注册就是这样静默无效的) ——理由原文: 「注册失败的表现是『一切正常, 直到有人开
    联网』」。这里回查 litellm 是否真的认了每个 Bedrock 模型的 tool-calling 能力,
    而不是假定调用 `register_model()` 没抛异常就算数。

    逐模型独立回查 (而非"任意一个通过就算过"): Claude 系在 litellm bedrock
    allowlist 里原生认 `anthropic` 前缀, 不注册也是 True —— 若把检查做成"存在
    一个 True 即通过", 只要 Claude 天然为真, GPT 系注册悄悄失效也测不出来, 自
    检就形同虚设。故每个模型各自核对自己的 `supports_function_calling`, Claude
    天然为 True 不会被误报, 也不会因为它天然为真就让 GPT 那份检查跟着恒真。

    非 Bedrock 的模型不在本自检范围内 —— 那是 C3 (`register_selectable_model_
    capabilities` 的返回值) 管的另一个问题, 两者语义不混。

    返回注册后仍未生效 (`supports_function_calling` 为 False) 的模型 id;
    空列表 = 全部生效。
    """
    failed: list[str] = []
    for m in _validated_selectable_models(s):
        if not m.model.startswith("bedrock/"):
            continue
        key = m.model.removeprefix("bedrock/")
        if not litellm.supports_function_calling(model=key, custom_llm_provider="bedrock_converse"):
            failed.append(m.id)
    return failed
