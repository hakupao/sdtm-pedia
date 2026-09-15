"""报告自证闸: run 报告必须**自己说清**它是怎么跑出来的。

⚠ 本文件零真实 LLM / chroma 调用 —— RAGEngine / run_evaluation / print_summary 全桩掉。

守两个已发生的事故 (evidence/checkpoints/verified_spotcheck_2026-09.md):

**V-1**: `check_code_grounding.py` 重建上下文时写死 `structured_lookup=ON, hybrid=ON`,
而生成时两者都关 ⇒ 判 ungrounded 用的 top-15 不是模型看见的那个 ⇒ 8 条全是假阳性。
根因是**报告没落盘检索实参**, 事后只能靠翻 log 猜。⇒ 报告必须记 `retrieval_levers`。

**V-2**: 生成调用从不设 max_tokens ⇒ 吃 provider 默认值 ⇒ 各模型截断率不同, 且**静默**。
⇒ 报告必须记 `max_tokens` 与撞顶的题 id。

⛔ `retrieval_levers` 记的是**引擎实收值**, 不是 args —— 与 run_eval.py 既有的
`prompt_guardrail` / `web_search` 同一约定 (注入点漏改时读 args 会落一个标着 ON
实际 OFF 的标签, 事后无从分辨)。
"""
from __future__ import annotations

import json

import pytest

from eval import run_eval


@pytest.fixture
def report(tmp_path, monkeypatch):
    """跑 main() 并返回落盘的报告 dict。results 由调用方指定。"""
    test_set = tmp_path / "ts.yml"
    test_set.write_text(
        "- id: q1\n  question: hi\n  category: concept\n  expected_facts: []\n"
        "  expected_sources: ['stub.md']\n",
        encoding="utf-8",
    )

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        """检索 lever 的**实收值**刻意与 args 相反, 用来钉住"记引擎不记 args"。"""

        def __init__(self, **kwargs):
            self.collection = FakeCollection()
            self.rerank_model = kwargs["rerank_model"]
            self.rerank_candidates = kwargs["rerank_candidates"]
            self.expansion_model = kwargs["expansion_model"]
            self.expansion_n_queries = kwargs["expansion_n_queries"]
            self.hybrid_fusion = kwargs["hybrid_fusion"]
            self.hybrid_alpha = kwargs["hybrid_alpha"]
            self.web_search_enabled = kwargs["web_search_enabled"]
            self.prompt_guardrail_enabled = kwargs["prompt_guardrail_enabled"]
            self.top_k = kwargs["top_k"]
            # 实收值 != args: 命令行没给 --hybrid / --structured-lookup / --rerank
            self.structured_lookup_enabled = True
            self.hybrid_enabled = True
            self.rerank_enabled = True
            self.query_expansion = "hyde"
            # T4: 实收值刻意与注入值相反 (settings 默认 True), 钉住"记引擎不记 settings"
            self.domain_definition_seat = False
            # T5: 同上, 实收值刻意与注入值相反 (settings 默认 True ⇒ 会注入一个对象)
            self.domain_expander = None
            # T6: 同上, 实收值刻意与注入值相反 (settings 默认 True)
            self.bm25_query_stopwords = False

    def _run(results: list[dict], extra_args: list[str] | None = None) -> dict:
        out = tmp_path / "report.json"
        monkeypatch.setattr(run_eval, "RAGEngine", FakeEngine)
        monkeypatch.setattr(run_eval, "run_evaluation", lambda *a, **k: results)
        monkeypatch.setattr(
            run_eval, "print_summary", lambda *a, **k: {"verdict": "PASS"}
        )
        run_eval.main([str(test_set), "--retrieval-only", "--output", str(out),
                       *(extra_args or [])])
        return json.loads(out.read_text())

    return _run


def test_report_records_the_engines_actual_retrieval_levers(report):
    """V-1 闸: lever 取自**引擎**。

    分辨力: fixture 的 FakeEngine 把四个 lever 都设成 True/"hyde", 而命令行一个
    对应 flag 都没给 ⇒ 若实现改成读 args, 这四条断言会全变成 False/"none" 而红。
    """
    levers = report([])["summary"]["retrieval_levers"]

    assert levers["structured_lookup"] is True
    assert levers["hybrid"] is True
    assert levers["rerank"] is True
    assert levers["query_expansion"] == "hyde"


def test_report_records_the_domain_definition_seat_lever(report):
    """T4 fix 1: 保底席也是重建上下文的必需实参 —— 少了它, 事后按报告重建会用
    `RAGEngine` 的默认值 (True) 去还原一份 seat=OFF 的旧报告, top5 对不上而炸。

    分辨力: FakeEngine 把实收值设成 False, 而注入值来自 settings (默认 True) ⇒
    若实现改成读 settings, 这条断言会变 True 而红。
    """
    assert report([])["summary"]["retrieval_levers"]["domain_definition_seat"] is False


def test_report_records_the_bm25_query_stopwords_lever(report):
    """T6: 查询侧 BM25 停用泛用语也是重建上下文的必需实参 —— 少了它, 事后按报告重建会用
    `RAGEngine` 的默认值 (True) 去还原一份实际停用表不同的旧报告, top5 对不上而炸。

    分辨力: FakeEngine 把实收值设成 False, 而注入值来自 settings (默认 True) ⇒
    若实现改成读 settings, 这条断言会变 True 而红。
    """
    assert report([])["summary"]["retrieval_levers"]["bm25_query_stopwords"] is False


def test_report_records_top_k_alongside_the_levers(report):
    """top_k 也是重建上下文的必需实参 —— 少了它同口径重建仍然重建不出来。"""
    levers = report([], ["--top-k", "7"])["summary"]["retrieval_levers"]

    assert levers["top_k"] == 7


def test_report_records_max_tokens(report):
    """V-2 闸: 事后要能回答"这轮的上限是多少" —— 不落盘就只能猜 provider 默认值。"""
    summary = report([])["summary"]

    assert summary["max_tokens"] == run_eval.MAX_TOKENS


def test_report_lists_answers_that_hit_the_token_cap(report):
    """V-2 闸: 截断不能静默。

    分辨力: q2 差一个 token 没撞顶, 必须**不**在列表里。
    """
    results = [
        {"id": "q1", "usage": {"completion_tokens": run_eval.MAX_TOKENS}},
        {"id": "q2", "usage": {"completion_tokens": run_eval.MAX_TOKENS - 1}},
    ]

    assert report(results)["summary"]["truncated"] == ["q1"]


def test_truncation_is_shouted_to_stdout_not_only_buried_in_json(report, capsys):
    """⛔ 只写进 JSON 不够: 2026-09-02 那轮的报告里 usage 一直都在, 但没人看,
    截断是事后人工比对才发现的。跑的人当场必须看见。"""
    report([{"id": "q1", "usage": {"completion_tokens": run_eval.MAX_TOKENS}}])

    out = capsys.readouterr().out
    assert "TRUNCAT" in out.upper()
    assert "q1" in out
