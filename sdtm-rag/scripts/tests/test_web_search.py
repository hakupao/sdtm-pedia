"""web_search 通道: 去重 / 截断 / 降级 / 配额 (spec §6.1 §7)。

红线: 本文件只用公开 CDISC 相关的合成数据, 不含任何 study 题面或 OID。
"""
import json

import pytest

from server.config import Settings
from server.web_search import (WEB_TOOL_SPEC, WebRef, WebSearcher, normalize_url,
                               render_tool_result)


@pytest.fixture(autouse=True)
def _reset_daily_quota():
    """WebSearcher 的日配额是**类级**状态 (进程内累计) —— 不重置会跨测试污染:
    排在 test_quota_exceeded 之前的每个 search() 都会把计数推高, 那条断言必挂。"""
    WebSearcher._day, WebSearcher._day_used = "", 0
    yield
    WebSearcher._day, WebSearcher._day_used = "", 0


def _payload(results):
    return {"results": results}


class _FakeResp:
    def __init__(self, data, status=200):
        self._data, self.status_code = data, status

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        return self._data


def _searcher(monkeypatch, responder):
    s = Settings()
    sr = WebSearcher(s, api_key="tvly-test")
    monkeypatch.setattr("server.web_search.requests.post", responder)
    return sr


def test_normalize_url_dedup_key():
    # §6.1 实测: 同一篇文章的 www 与非 www 会各占一坑
    assert normalize_url("https://www.example.com/a/") == normalize_url("http://example.com/a")


def test_search_dedups_www_variants(monkeypatch):
    sr = _searcher(monkeypatch, lambda *a, **k: _FakeResp(_payload([
        {"url": "https://www.bioforumgroup.com/x", "title": "T", "content": "C1"},
        {"url": "https://bioforumgroup.com/x", "title": "T", "content": "C2"},
        {"url": "https://phuse.org/p.pdf", "title": "P", "content": "C3"},
    ])))
    refs, status = sr.search("q")
    assert status == "ok"
    assert [r.url for r in refs] == ["https://www.bioforumgroup.com/x", "https://phuse.org/p.pdf"]


def test_search_truncates_content(monkeypatch):
    sr = _searcher(monkeypatch, lambda *a, **k: _FakeResp(_payload([
        {"url": "https://e.com/1", "title": "T", "content": "x" * 5000},
    ])))
    refs, _ = sr.search("q")
    assert len(refs[0].content) == Settings().web_result_max_chars


def test_search_respects_results_per_search(monkeypatch):
    many = [{"url": f"https://e.com/{i}", "title": "T", "content": "c"} for i in range(10)]
    sr = _searcher(monkeypatch, lambda *a, **k: _FakeResp(_payload(many)))
    refs, _ = sr.search("q")
    assert len(refs) == Settings().web_results_per_search


def test_search_failure_degrades_not_raises(monkeypatch):
    def boom(*a, **k):
        raise TimeoutError("timeout")
    sr = _searcher(monkeypatch, boom)
    refs, status = sr.search("q")
    assert refs == [] and status == "failed"   # §7: 失败不得 500


def test_search_malformed_json_degrades(monkeypatch):
    sr = _searcher(monkeypatch, lambda *a, **k: _FakeResp({"unexpected": 1}))
    refs, status = sr.search("q")
    assert refs == [] and status == "ok"       # 结构合法但空结果, 不算失败


def test_search_results_not_a_list_degrades(monkeypatch):
    # "results" 键存在但值不是 list (Tavily 抽风) —— 结构异常, 与网络失败同级, 不得抛异常
    sr = _searcher(monkeypatch, lambda *a, **k: _FakeResp(_payload("some string")))
    refs, status = sr.search("q")
    assert refs == [] and status == "failed"


def test_search_skips_non_dict_elements(monkeypatch):
    # 混了坏元素的合法列表: 跳过坏的, 保留好的, 不因为一个坏元素判 failed
    sr = _searcher(monkeypatch, lambda *a, **k: _FakeResp(_payload(
        [123, {"url": "https://e.com/1", "title": "T", "content": "c"}])))
    refs, status = sr.search("q")
    assert [r.url for r in refs] == ["https://e.com/1"]
    assert status == "ok"


def test_missing_key_disabled(monkeypatch):
    # 本机 .env 里跑着真的 TAVILY_API_KEY (dotenv 在 import server.config 时已灌入
    # os.environ), api_key=None 的"无 key"语义靠 delenv 隔离, 而非改实现的 fallback 逻辑
    # (那段 fallback 是生产態故意要的: 不传 api_key 时吃环境变量)。
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    sr = WebSearcher(Settings(), api_key=None)
    refs, status = sr.search("q")
    assert refs == [] and status == "disabled"


def test_quota_exceeded(monkeypatch):
    monkeypatch.setenv("SDTM_RAG_WEB_DAILY_QUOTA", "1")   # 经 env 而非改实例, 不依赖 Settings 可变性
    sr = WebSearcher(Settings(), api_key="tvly-test")
    monkeypatch.setattr("server.web_search.requests.post",
                        lambda *a, **k: _FakeResp(_payload([{"url": "https://e.com/1",
                                                             "title": "T", "content": "c"}])))
    assert sr.search("q1")[1] == "ok"
    assert sr.search("q2")[1] == "quota_exceeded"


def test_searches_used_counts_only_real_calls(monkeypatch):
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)  # 同上: 隔离本机 .env 里的真 key
    sr = WebSearcher(Settings(), api_key=None)
    sr.search("q")
    assert sr.searches_used == 0   # disabled 不计次


def test_tool_spec_shape():
    fn = WEB_TOOL_SPEC["function"]
    assert WEB_TOOL_SPEC["type"] == "function"
    assert fn["name"] == "web_search"
    assert fn["parameters"]["required"] == ["query"]


def test_render_tool_result_carries_url_and_date():
    refs = [WebRef(url="https://e.com/1", title="T", content="C", retrieved_at="2026-08-31")]
    payload = json.loads(render_tool_result(refs, "ok"))
    assert payload["status"] == "ok"
    assert payload["results"][0]["url"] == "https://e.com/1"
    assert payload["results"][0]["retrieved_at"] == "2026-08-31"


def test_render_tool_result_failure_tells_model():
    payload = json.loads(render_tool_result([], "failed"))
    assert payload["status"] == "failed"
    assert payload["results"] == []
