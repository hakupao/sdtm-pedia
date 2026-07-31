"""embed_texts 复用重构测试 (Task 9): 批次切分 + 维度 + 顺序。"""

from __future__ import annotations

from unittest.mock import patch

from scripts.ingest import EMBED_DIM, embed_texts


class _FakeResp:
    """Mimic litellm.embedding response: .data 为 dict 列表, 含 index/embedding。"""

    def __init__(self, texts: list[str]):
        self.data = [
            {"index": i, "embedding": [float(i)] * EMBED_DIM}
            for i, _ in enumerate(texts)
        ]


def test_embed_texts_batches_of_100():
    calls = []

    def fake_embedding(model, input):
        calls.append(len(input))
        return _FakeResp(input)

    with patch("scripts.ingest.litellm.embedding", side_effect=fake_embedding):
        out = embed_texts([f"t{i}" for i in range(150)])

    assert len(out) == 150
    assert calls == [100, 50]
    assert all(len(v) == EMBED_DIM for v in out)


def test_embed_texts_preserves_order():
    """response.data[i]['index'] 是批内偏移, 结果须落回全局位置。"""

    def fake_embedding(model, input):
        # 乱序返回, 逼迫实现依赖 index 而非枚举顺序
        resp = _FakeResp(input)
        resp.data = list(reversed(resp.data))
        return resp

    with patch("scripts.ingest.litellm.embedding", side_effect=fake_embedding):
        out = embed_texts([f"t{i}" for i in range(150)])

    # 第 j 个批内元素的 fake embedding 值 = 批内偏移
    assert [v[0] for v in out] == [float(i % 100) for i in range(150)]


def test_embed_texts_empty():
    with patch("scripts.ingest.litellm.embedding", side_effect=AssertionError):
        assert embed_texts([]) == []
