"""多模型切换 (U1) 的闸。spec docs/superpowers/specs/2026-09-01-model-switching-design.md"""
import pytest

from server.config import Settings, SelectableModel


def test_selectable_models_defaults():
    """四个候选全部在, 且 id 唯一 —— id 是 Router 组名与前端提交值的共用键,
    重复会让 Router 后写覆盖先写而 UI 毫无察觉。"""
    s = Settings()
    ids = [m.id for m in s.selectable_models]
    assert ids == ["opus-5", "sonnet-5", "gpt-terra", "gpt-sol"]
    assert len(set(ids)) == len(ids)


def test_selectable_models_all_on_bedrock():
    """C3: GPT 与 Claude 不得走用户个人 API。"""
    s = Settings()
    for m in s.selectable_models:
        assert m.model.startswith("bedrock/"), f"{m.id} 不走 Bedrock: {m.model}"


def test_only_opus5_is_verified():
    """verified 语义 = 该模型跑过反捏造抽检并通过。目前只有 opus-5 验过 ——
    sonnet-5 是 Claude 不代表验过, 两个方向都钉住, 免得有人顺手全填 true。"""
    s = Settings()
    v = {m.id: m.verified for m in s.selectable_models}
    assert v["opus-5"] is True
    assert v["sonnet-5"] is False
    assert v["gpt-terra"] is False
    assert v["gpt-sol"] is False


def _group_names(router):
    """Router 已知的组名集合。model_list 是构造时传入的那份, 逐项取 model_name。"""
    return {m["model_name"] for m in router.model_list}


def test_router_derives_a_group_per_selectable_model():
    from server.llm_config import create_router
    s = Settings()
    names = _group_names(create_router(s))
    for m in s.selectable_models:
        assert m.id in names, f"Router 缺少组 {m.id}"


def test_router_keeps_internal_groups():
    """C1: 判库(light)/hard/default 是内部用途, 不受用户选择影响, 必须仍在。"""
    from server.llm_config import create_router
    names = _group_names(create_router(Settings()))
    assert {"default", "default-fallback", "hard", "light"} <= names


def test_known_groups_equals_what_router_actually_has():
    """裁定 F-1 的补偿闸: 给『校验端读 known_model_groups (意图)』与『Router 是事实』
    这层关系上闸, 二者必须逐项相等。不需要任何假 Router。

    这条**不防派生逻辑本身漂移**: 若 create_router 与 known_model_groups 两处同时
    手滑把 m.id 写成 m.label, 两边算出来的错法一致, 本测试照绿。真正锚定字面量、
    防住这种 co-drift 的是 test_router_derives_a_group_per_selectable_model 和
    test_router_group_maps_to_the_configured_model_string。"""
    from server.llm_config import create_router, known_model_groups
    s = Settings()
    assert known_model_groups(s) == {m["model_name"] for m in create_router(s).model_list}
    assert len(known_model_groups(s)) >= 8, "抽取端失效: 集合为空时上面的等式恒真"


def test_router_group_maps_to_the_configured_model_string():
    """方向钉: 组名对了但指向错模型, 上面两条照样绿。"""
    from server.llm_config import create_router
    s = Settings()
    by_name = {m["model_name"]: m["litellm_params"]["model"] for m in create_router(s).model_list}
    for m in s.selectable_models:
        assert by_name[m.id] == m.model


def test_create_router_succeeds_when_no_id_collision():
    """两个方向之一: 默认配置的 id 不撞内部组, 正常构造不该被误伤。"""
    from server.llm_config import create_router
    create_router(Settings())  # 不应抛


def test_create_router_raises_on_internal_group_collision():
    """另一个方向: selectable id 撞上 INTERNAL_GROUPS (如 "light") 时必须 fail-loud。

    litellm Router 允许同一 model_name 出现两次并当同一组的多个 deployment 做
    load-balance —— 撞名会让判库(light)悄悄混进用户选的答题模型, 静默打破 C1,
    且没有任何既有测试会变红。selectable_models 还能被 SDTM_RAG_SELECTABLE_MODELS
    在运行时注入, 只挡默认配置不够, 必须在构造时就拒绝。"""
    from server.llm_config import create_router
    s = Settings(selectable_models=[
        SelectableModel(id="light", label="撞名", model="bedrock/x", verified=False),
    ])
    with pytest.raises(ValueError, match="light"):
        create_router(s)


def test_known_model_groups_raises_on_internal_group_collision():
    """同一防线在 known_model_groups 这条路径上也要生效 —— Task 5 的白名单校验
    走的正是这个函数, 不经过 create_router。"""
    from server.llm_config import known_model_groups
    s = Settings(selectable_models=[
        SelectableModel(id="hard", label="撞名", model="bedrock/x", verified=False),
    ])
    with pytest.raises(ValueError, match="hard"):
        known_model_groups(s)


def test_registration_makes_tools_supported_for_gpt():
    """LiteLLM 1.88.1 的 bedrock allowlist 不认 openai.*, 不注册就拒收 tools ——
    联网通道对 GPT 直接不可用。裸 boto3 已实测工具调用本身通 ⇒ 这是客户端元数据缺口。
    ⚠ 注册 key 必须**去掉 bedrock/ 前缀**, 用错前缀是静默无效 (spec §4.2)。"""
    import litellm
    from server.llm_config import register_selectable_model_capabilities
    register_selectable_model_capabilities(Settings())
    for mid in ["converse/global.openai.gpt-5.6-terra", "converse/global.openai.gpt-5.6-sol"]:
        assert litellm.supports_function_calling(model=mid, custom_llm_provider="bedrock_converse")


def test_registration_reports_non_bedrock_models():
    """闸 6 (C3): config.py 里三个 Claude 的硬编码默认值是 anthropic/ 直连, 只靠 .env
    改写且无任何校验 ⇒ .env 一缺就静默走直连。两个方向都钉。"""
    from server.llm_config import register_selectable_model_capabilities
    assert register_selectable_model_capabilities(Settings()) == []
    bad = Settings(selectable_models=[
        {"id": "x", "label": "X", "model": "anthropic/claude-opus-5", "verified": False}])
    assert register_selectable_model_capabilities(bad) == ["x"]


def test_verify_reports_empty_after_successful_registration():
    """spec §4.2 启动期自检: register 之后回查, 正常路径必须为空 —— 既包括注册后
    变 True 的 GPT 系, 也包括在 litellm bedrock allowlist 里原生就是 True 的 Claude
    系 (不注册也通过 allowlist)。两类模型都不该被自检误报。"""
    from server.llm_config import (
        register_selectable_model_capabilities,
        verify_selectable_model_capabilities,
    )
    s = Settings()
    register_selectable_model_capabilities(s)
    assert verify_selectable_model_capabilities(s) == []


def test_verify_flags_a_model_whose_registration_never_happened():
    """自检真的会抓: 用一个专造的、别处从未注册过的 bedrock key (不依赖源码变异,
    也不依赖测试执行顺序) 验证 supports_function_calling 仍为 False 时会被 flag。
    这是"注册未生效"在自检里的直接复现 —— 与控制器实测的『去掉 removeprefix 导致
    静默无效』是同一条检测路径, 只是不需要真的改坏源码就能钉住。"""
    from server.llm_config import verify_selectable_model_capabilities
    s = Settings(selectable_models=[
        SelectableModel(id="never-registered", label="从未注册",
                         model="bedrock/converse/global.openai.gpt-9.9-never-registered",
                         verified=False),
    ])
    assert verify_selectable_model_capabilities(s) == ["never-registered"]
