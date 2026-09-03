"""V-2 闸: 生成调用的 `max_tokens` 必须**显式钉死**, 并且截断必须被检出。

⚠ 本文件零真实 LLM 调用 —— 测的是纯函数。

背景 (V-2, 见 evidence/checkpoints/verified_spotcheck_2026-09.md):
`run_eval.py` 的 comp_kwargs 原来只放 `messages` (+ 可选 temperature), **从不设 max_tokens**
⇒ 实收值是 litellm 对各 provider 的默认值 (Bedrock Converse = 4096)。
不同 provider 默认值不同 ⇒ 四模型跑下来是**不同的截断率**, 而截断会少发码
⇒ 话痨模型在 (a) 层显得更干净。这是跨模型比较的系统性混淆。

更坏的是它**静默**: 2026-09-02 那轮 opus-5 的 q36/q83 撞满 4096 被截断, 报告里没有任何
提示, 是人工比对 completion_tokens 才发现的。所以本文件守两件事:
  1. max_tokens 进得了 comp_kwargs (口径统一);
  2. 撞顶的答案会被检出 (截断不再静默)。
"""
from eval.run_eval import build_completion_kwargs, find_truncated


def test_completion_kwargs_pins_max_tokens_even_without_temperature():
    """⛔ 这条守的是 V-2 本身: 不显式给 max_tokens 就会吃 provider 默认值。

    温度是可选的 (paired run 才给 0.0), 所以拿"没给温度"这一支来钉 —— 它是最容易
    被写成"只放 messages"的那一支。
    """
    kw = build_completion_kwargs(messages=[{"role": "user", "content": "hi"}],
                                 temperature=None, max_tokens=8192)

    assert kw["max_tokens"] == 8192
    assert kw["messages"] == [{"role": "user", "content": "hi"}]
    assert "temperature" not in kw


def test_completion_kwargs_keeps_temperature_when_given():
    """温度那一支不能被 max_tokens 的加入挤掉 (paired run 靠 temperature=0.0 保确定性)。"""
    kw = build_completion_kwargs(messages=[], temperature=0.0, max_tokens=4096)

    assert kw["temperature"] == 0.0
    assert kw["max_tokens"] == 4096


def test_find_truncated_flags_answers_that_hit_the_cap():
    """撞顶 = completion_tokens 等于 max_tokens ⇒ 答案很可能被切在句中。

    分辨力: q02 (4095) 与 q03 (0 tokens) 都**不该**上榜 —— 若实现写成 `>=` 之外的
    任何宽松比较 (比如 `> max_tokens * 0.9`), q02 会跟着上榜, 这条就红。
    """
    results = [
        {"id": "q01", "usage": {"completion_tokens": 4096}},
        {"id": "q02", "usage": {"completion_tokens": 4095}},
        {"id": "q03", "usage": {"completion_tokens": 0}},
        {"id": "q04", "usage": {"completion_tokens": 4096}},
    ]

    assert find_truncated(results, max_tokens=4096) == ["q01", "q04"]


def test_find_truncated_is_empty_when_nothing_hits_the_cap():
    """没截断时必须是空 —— 空列表是"这轮干净"的证据, 不能靠"没打印"来暗示。"""
    results = [{"id": "q01", "usage": {"completion_tokens": 1538}}]

    assert find_truncated(results, max_tokens=8192) == []


def test_find_truncated_ignores_entries_without_usage():
    """retrieval-only / 生成失败的条目没有 usage —— 不能因此炸, 也不能算成截断。"""
    results = [
        {"id": "q01"},
        {"id": "q02", "usage": {}},
        {"id": "q03", "usage": {"completion_tokens": 8192}},
    ]

    assert find_truncated(results, max_tokens=8192) == ["q03"]


def test_generation_call_actually_receives_max_tokens(monkeypatch):
    """⛔ 接线闸: 纯函数对了但调用点没用上, V-2 照样复发。

    这条直接钉 `litellm.completion` 实收的 kwargs —— 把调用点改回
    `comp_kwargs = {"messages": messages}` 就会红。
    """
    from eval import run_eval

    captured: dict = {}

    class _Usage:
        prompt_tokens, completion_tokens, total_tokens = 10, 20, 30

    class _Msg:
        content = "AE is an Events domain."

    class _Choice:
        message = _Msg()

    class _Resp:
        choices = [_Choice()]
        usage = _Usage()

    def fake_completion(**kwargs):
        captured.update(kwargs)
        return _Resp()

    monkeypatch.setattr(run_eval.litellm, "completion", fake_completion)

    class FakeEngine:
        def retrieve(self, q, top_k=None):
            return []

        def format_context(self, chunks):
            return "ctx"

        def build_messages(self, question, context):
            return [{"role": "user", "content": question}]

    run_eval.run_evaluation(
        [{"id": "q1", "question": "hi", "category": "concept", "expected_facts": [],
          "expected_sources": ["stub.md"]}],
        rag=FakeEngine(),
        direct_model="fake/model",
    )

    assert captured["max_tokens"] == run_eval.MAX_TOKENS
