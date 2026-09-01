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
