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


# ---- P3: 维度闸 / 429 重试 / 截断 / 缺失闸 (旧账覆盖) ----

def test_embed_dim_mismatch_raises():
    class _BadResp:
        def __init__(self, texts):
            self.data = [{"index": i, "embedding": [0.0] * 8}
                         for i, _ in enumerate(texts)]

    with patch("scripts.ingest.litellm.embedding",
               side_effect=lambda model, input: _BadResp(input)):
        try:
            embed_texts(["a", "b"])
            raise AssertionError("expected RuntimeError")
        except RuntimeError as e:
            assert "dim" in str(e)


def test_embed_retries_on_429():
    attempts = []

    def flaky(model, input):
        attempts.append(1)
        if len(attempts) < 3:
            raise Exception("429 Too Many Requests, rate limit")
        return _FakeResp(input)

    sleeps = []
    with patch("scripts.ingest.litellm.embedding", side_effect=flaky), \
         patch("scripts.ingest.time.sleep", side_effect=sleeps.append):
        out = embed_texts(["a", "b"])

    assert len(out) == 2 and len(attempts) == 3
    assert sleeps == [15, 30]          # 指数退避 15*2^n, 上限 60


def test_embed_non_rate_error_raises_immediately():
    def broken(model, input):
        raise Exception("invalid api key")

    with patch("scripts.ingest.litellm.embedding", side_effect=broken), \
         patch("scripts.ingest.time.sleep") as sl:
        try:
            embed_texts(["a"])
            raise AssertionError("expected raise")
        except Exception as e:
            assert "invalid api key" in str(e)
    sl.assert_not_called()


def test_embed_truncation_warns(capsys):
    long_text = "token " * 9000          # > EMBED_MAX_TOKENS=8191
    with patch("scripts.ingest.litellm.embedding",
               side_effect=lambda model, input: _FakeResp(input)):
        out = embed_texts([long_text, "short"])
    assert len(out) == 2
    assert "truncated" in capsys.readouterr().out


def test_embed_missing_embedding_raises():
    class _DropResp:
        def __init__(self, texts):
            self.data = [{"index": i, "embedding": [0.0] * EMBED_DIM}
                         for i, _ in enumerate(texts) if i != 1]

    with patch("scripts.ingest.litellm.embedding",
               side_effect=lambda model, input: _DropResp(input)):
        try:
            embed_texts(["a", "b", "c"])
            raise AssertionError("expected RuntimeError")
        except RuntimeError as e:
            assert "not embedded" in str(e)


def test_embed_429_exhaustion_raises():
    def always_429(model, input):
        raise Exception("429 Too Many Requests")

    sleeps = []
    with patch("scripts.ingest.litellm.embedding", side_effect=always_429), \
         patch("scripts.ingest.time.sleep", side_effect=sleeps.append):
        try:
            embed_texts(["a"])
            raise AssertionError("expected raise after retries exhausted")
        except Exception as e:
            assert "429" in str(e)
    assert sleeps == [15, 30, 60, 60, 60]      # min(60, 15*2^n), 第 6 次尝试后不再退避


def test_embed_dim_mismatch_in_tail_raises():
    """维度闸必须全量检查, 不能只看首元素 (后半批坏也要拦)."""
    class _TailBadResp:
        def __init__(self, texts):
            self.data = [
                {"index": i,
                 "embedding": [0.0] * (8 if i == len(texts) - 1 else EMBED_DIM)}
                for i, _ in enumerate(texts)
            ]

    with patch("scripts.ingest.litellm.embedding",
               side_effect=lambda model, input: _TailBadResp(input)):
        try:
            embed_texts(["a", "b", "c"])
            raise AssertionError("expected RuntimeError")
        except RuntimeError as e:
            assert "dim" in str(e)
