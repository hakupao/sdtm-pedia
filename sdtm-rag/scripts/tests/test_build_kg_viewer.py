import json
from scripts import build_kg_viewer as V


def test_build_data_includes_implicit(tmp_path, monkeypatch):
    fake = {"meta": {"domains": ["PR", "TR"]},
            "edges": [{"source": "PR", "target": "TR", "kind": "data_flow", "directed": True,
                       "relation": "x", "confidence": 0.8, "verified": True,
                       "evidence": {"quote": "q", "source_file": "f", "line": 1}}]}
    impl_path = tmp_path / "impl.json"
    impl_path.write_text(json.dumps(fake), encoding="utf-8")
    monkeypatch.setattr(V, "IMPL_PATH", impl_path)

    data = V.build_data()
    assert data["implicit"]["edges"][0]["kind"] == "data_flow"


def test_build_data_implicit_none_when_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(V, "IMPL_PATH", tmp_path / "does_not_exist.json")

    data = V.build_data()
    assert data["implicit"] is None


def test_pan_reset_does_not_kill_node_click():
    # 全局 pointerup 先于 startDrag 内注册的 up() 执行 (window 上按注册顺序);
    # 若它重置 drag, up() 的 if(drag) 恒 false → openPanel/expandNode 永不触发.
    pan_reset = next(line for line in V.TEMPLATE.splitlines()
                     if "pointerup" in line and "pan=null" in line)
    assert "drag" not in pan_reset


def test_layout_comes_to_rest():
    # alpha 带 0.02 永久下限时模拟永不停 → 节点持续乱动;
    # 必须衰减穿过 ALPHA_MIN 并让 frame 停止 tick (交互反加热恢复).
    assert "alpha=0.02" not in V.TEMPLATE
    assert "running&&alpha>ALPHA_MIN" in V.TEMPLATE


def test_explore_seed_and_auto_expand():
    # explore 独立种子默认 TU (AE 无隐性边覆盖, 开箱即空); fresh 进入自动展开一跳.
    assert 'seed:"TU"' in V.TEMPLATE
    assert "vExplore(cur.seed" in V.TEMPLATE
    assert "expandNode(cur.seed" in V.TEMPLATE


def test_expand_anchors_accumulate():
    # spec §5: 展开按 硬边邻居 > 高置信推断邻居 优先级 (不变); 且展开必须设置
    # exploreAnchor, 供 exploreTargets() 分派到锚定累积 (旧节点原位不动, 新
    # 节点落 anchor 周围空槽), 消除"点一下到处飞"的爆炸感.
    fn = V.TEMPLATE.split("function expandNode(code)")[1].split("\n}")[0]
    assert "relBySrc" in fn and "confidence" in fn      # 展开优先级不变
    assert "exploreAnchor" in fn                        # 锚定累积语义
