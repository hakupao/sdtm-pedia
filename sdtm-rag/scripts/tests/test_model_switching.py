"""多模型切换 (U1) 的闸。spec docs/superpowers/specs/2026-09-01-model-switching-design.md"""
from server.config import Settings


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
