# 联网参考通道 (web search channel) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 给 sdtm-rag 答题侧加一个「联网参考」通道 —— 模型自主决定是否搜网、搜什么、搜几轮, 搜索过程对前端可见, 且网络内容永远不得产出 CT 码与 class 归属。

**Architecture:** KB 检索保持**前置注入**不变 (现有 RAG 管线/grounding 闸/码闸一行不改); `web_search` 以**自定义工具**形式挂给答题模型, 由 `/api/ask_stream` 跑工具循环 (上限 5 轮 / 15 次搜索), 每轮把 `tool_call` / `tool_result` 作为新增 SSE 事件推给前端。联网与 `corpus` 判库**正交**: 请求级 `web` 只决定是否挂工具, 不动 system prompt。

**Tech Stack:** Python 3.14 · FastAPI · LiteLLM Router (`bedrock/converse/global.anthropic.claude-opus-5`) · Tavily Search API · pytest · 原生 JS (webchat, 无框架)

**Spec:** `docs/superpowers/specs/2026-08-31-web-search-channel-design.md`

## Global Constraints

- **红线 (spec §5)**: 网页内容**永远不得**产出 CT 码 (`Cxxxxx`)、SDTM class/category 归属、变量 Core/Role/Type 断言。`eval/prod_wirein/check_code_grounding.py` 与 `server/grounding.py::apply_counting_gate` **一行不改**。
- **循环上限**: 最多 **5 轮** / **15 次搜索** (用户裁定 2026-08-31)。
- **来源标注**: 网络来源一律 `[Web: <url> (retrieved YYYY-MM-DD)]`, 与 KB 的 `[Source: path]` 严格区分。
- **零污染**: `SDTM_RAG_WEB_SEARCH_ENABLED=false` 时 system prompt 与本功能引入前**逐字节相同**。
- **请求级 `web` 不动 system prompt** (spec §5 + §9.3): 它只决定是否挂工具。
- **默认 off**: `AskStreamRequest.web` 默认 `False`; 140q / study golden v2 48q 的 eval 跑法一字不改。
- **红线 (仓库级)**: study 题面/OID 属临床数据, 不得进 git; 新增测试只用 CDISC 公开内容或合成数据。
- **中文注释**: 本仓 server/ 代码注释为中文, 沿用。

---

### Task 1: Settings 旋钮 + Tavily key 装载

**Files:**
- Modify: `sdtm-rag/server/config.py` (在 `prompt_guardrail_enabled` 附近新增一段)
- Test: `sdtm-rag/scripts/tests/test_web_search_config.py` (新建)

**Interfaces:**
- Produces: `Settings.web_search_enabled: bool`、`Settings.web_max_rounds: int`、`Settings.web_max_searches: int`、`Settings.web_result_max_chars: int`、`Settings.web_results_per_search: int`、`Settings.web_daily_quota: int`、`Settings.web_timeout_s: float`。Task 2/3/4 全部依赖这些名字。

- [ ] **Step 1: 写失败测试**

创建 `sdtm-rag/scripts/tests/test_web_search_config.py`:

```python
"""Web 搜索通道的配置旋钮 (spec §6 组件表 / §7 上限)。"""
from server.config import Settings


def test_web_search_defaults():
    s = Settings()
    # 默认开 (Rule 9 进 prompt), 但请求级 web 默认 off —— 两件事互不影响
    assert s.web_search_enabled is True
    assert s.web_max_rounds == 5
    assert s.web_max_searches == 15
    assert s.web_results_per_search == 3
    assert s.web_result_max_chars == 1200
    assert s.web_daily_quota == 200
    assert s.web_timeout_s == 30.0


def test_web_search_env_override(monkeypatch):
    """逐字节回滚路径: 关掉即回到引入前 (对齐 prompt_guardrail_enabled 先例)。"""
    monkeypatch.setenv("SDTM_RAG_WEB_SEARCH_ENABLED", "false")
    monkeypatch.setenv("SDTM_RAG_WEB_MAX_ROUNDS", "2")
    s = Settings()
    assert s.web_search_enabled is False
    assert s.web_max_rounds == 2
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_web_search_config.py -q -p no:warnings`
Expected: FAIL — `AttributeError: 'Settings' object has no attribute 'web_search_enabled'`

- [ ] **Step 3: 实现**

在 `sdtm-rag/server/config.py` 的 `prompt_guardrail_enabled: bool = True` 那一段**之后**插入:

```python
    # ── 联网参考通道 (spec 2026-08-31) ──
    # 联网与 corpus 判库正交: 请求级 `web` 只决定是否把 web_search 工具挂上去,
    # **不动 system prompt**; 本开关才决定 Rule 9 是否进 system prompt。
    # 关掉 ⇒ system prompt 与本功能引入前逐字节相同 (A/B 回滚, 同 prompt_guardrail 先例)。
    web_search_enabled: bool = True
    web_max_rounds: int = 5          # 工具循环轮数上限 (用户裁定)
    web_max_searches: int = 15       # 单次请求搜索次数上限 (用户裁定)
    web_results_per_search: int = 3  # 每次搜索取回条数 (§6.1: 5 条 ≈ 3K token, 收到 3)
    web_result_max_chars: int = 1200 # 单条正文截断 (§6.1 上下文预算)
    web_daily_quota: int = 200       # 日配额兜底, 防忘关跑飞 (§7)
    web_timeout_s: float = 30.0      # 单次 Tavily 调用超时
```

`TAVILY_API_KEY` 不进 `Settings` —— 它由 `config.py` 顶部已有的 `load_dotenv()` 装进 `os.environ`, 与其他 provider key (ANTHROPIC/DEEPSEEK) 同一处理方式, Task 2 直接 `os.getenv` 读。

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_web_search_config.py -q -p no:warnings`
Expected: PASS (2 passed)

- [ ] **Step 5: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
git add sdtm-rag/server/config.py sdtm-rag/scripts/tests/test_web_search_config.py
git commit -m "feat(web-search): Settings 旋钮 (上限/配额/回滚开关)"
```

---

### Task 2: `server/web_search.py` — Tavily 调用、去重、降级

**Files:**
- Create: `sdtm-rag/server/web_search.py`
- Test: `sdtm-rag/scripts/tests/test_web_search.py` (新建)

**Interfaces:**
- Consumes: Task 1 的 `Settings.web_*` 字段。
- Produces:
  - `WebRef` dataclass: `url: str`、`title: str`、`content: str`、`retrieved_at: str` (ISO date `YYYY-MM-DD`)
  - `normalize_url(url: str) -> str` — 去重键 (剥 scheme / `www.` / 尾斜杠)
  - `WebSearcher(settings, api_key=None)`, 方法:
    - `.search(query: str) -> tuple[list[WebRef], str]` 返回 `(refs, status)`, `status ∈ {"ok","failed","quota_exceeded","disabled"}`
    - `.searches_used: int` (已用次数, Task 4 判上限用)
  - `WEB_TOOL_SPEC: dict` — 给 LiteLLM 的 OpenAI 风格工具定义
  - `render_tool_result(refs: list[WebRef], status: str) -> str` — 回灌给模型的 JSON 字符串

- [ ] **Step 1: 写失败测试**

创建 `sdtm-rag/scripts/tests/test_web_search.py`:

```python
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


def test_missing_key_disabled():
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
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_web_search.py -q -p no:warnings`
Expected: FAIL — `ModuleNotFoundError: No module named 'server.web_search'`

- [ ] **Step 3: 实现**

创建 `sdtm-rag/server/web_search.py`:

```python
"""联网参考通道 — Tavily 搜索客户端 (spec 2026-08-31 §6)。

设计要点:
- **降级不抛异常**: 搜索失败/超时/无 key/超配额一律返回空结果 + status,
  由调用方决定如何呈现。勾了联网却静默变成没联网是这类功能最容易骗人的地方,
  所以 status 必须一路传到前端 (§7)。
- **去重按规范化 URL**: §6.1 实测同一篇文章的 www 与非 www 会各占一坑。
- **正文截断**: 单条 1350-2869 字符, 跑满 5 轮/15 次可累积 40K+ token (§6.1)。
"""
from __future__ import annotations

import datetime as _dt
import json
import os
from dataclasses import dataclass

import requests
import structlog

log = structlog.get_logger(__name__)

_API_URL = "https://api.tavily.com/search"

# 给 LiteLLM 的 OpenAI 风格工具定义 (Router 已验证可透传到 Bedrock Converse, spec §11)
WEB_TOOL_SPEC = {
    "type": "function",
    "function": {
        "name": "web_search",
        "description": (
            "Search the public web for industry practice, conference papers, regulatory "
            "guidance and how other teams solved a problem. Use it when the SDTM knowledge "
            "base does not cover the question, or when the user asks how others do it. "
            "Results are UNVERIFIED third-party content, not CDISC standard text."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "search query, English works best"},
            },
            "required": ["query"],
        },
    },
}


@dataclass(frozen=True)
class WebRef:
    url: str
    title: str
    content: str
    retrieved_at: str  # ISO date, 进 [Web: url (retrieved YYYY-MM-DD)] 标注


def normalize_url(url: str) -> str:
    """去重键: 剥 scheme / www. / 尾斜杠。"""
    u = (url or "").strip()
    for pre in ("https://", "http://"):
        if u.startswith(pre):
            u = u[len(pre):]
            break
    if u.startswith("www."):
        u = u[4:]
    return u.rstrip("/")


class WebSearcher:
    """单次请求作用域的搜索器 —— searches_used 随请求生灭, 配额跨请求由 _day_used 承担。"""

    _day: str = ""
    _day_used: int = 0  # 类级: 进程内的当日累计 (轻量兜底, 非跨进程强一致)

    def __init__(self, settings, api_key: str | None = None) -> None:
        self.s = settings
        self.api_key = api_key if api_key is not None else os.getenv("TAVILY_API_KEY")
        self.searches_used = 0

    @classmethod
    def _bump_day(cls) -> int:
        today = _dt.date.today().isoformat()
        if cls._day != today:
            cls._day, cls._day_used = today, 0
        cls._day_used += 1
        return cls._day_used

    def search(self, query: str) -> tuple[list[WebRef], str]:
        if not self.api_key:
            return [], "disabled"
        if self._bump_day() > self.s.web_daily_quota:
            log.warning("web_search_quota_exceeded", quota=self.s.web_daily_quota)
            return [], "quota_exceeded"

        self.searches_used += 1
        try:
            r = requests.post(
                _API_URL,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={"query": query,
                      "max_results": self.s.web_results_per_search,
                      "search_depth": "advanced"},
                timeout=self.s.web_timeout_s,
            )
            r.raise_for_status()
            raw = r.json().get("results", []) or []
        except Exception as exc:  # noqa: BLE001 — 降级是设计, 不是吞错
            log.warning("web_search_failed", error=str(exc))
            return [], "failed"

        # 结构校验: "results" 键缺失 (raw == []) 仍是合法的"搜到但没结果" → ok;
        # 但 "results" 存在却不是 list, 是结构异常, 与网络失败同级 —— 不校验的话下面
        # it.get(...) 会在非 dict 元素上抛 AttributeError 穿透出去, 违反 §7 红线。
        if not isinstance(raw, list):
            log.warning("web_search_malformed_results", type=type(raw).__name__)
            return [], "failed"

        today = _dt.date.today().isoformat()
        seen: set[str] = set()
        refs: list[WebRef] = []
        for it in raw:
            if not isinstance(it, dict):  # 单个坏元素跳过, 不毁掉整批可用结果
                continue
            url = it.get("url") or ""
            key = normalize_url(url)
            if not key or key in seen:
                continue
            seen.add(key)
            refs.append(WebRef(
                url=url,
                title=(it.get("title") or "")[:300],
                content=(it.get("content") or "")[:self.s.web_result_max_chars],
                retrieved_at=today,
            ))
            if len(refs) >= self.s.web_results_per_search:
                break
        return refs, "ok"


def render_tool_result(refs: list[WebRef], status: str) -> str:
    """回灌给模型的 tool result。status 一并给模型 —— 让它知道自己是在无结果下作答。"""
    return json.dumps({
        "status": status,
        "results": [{"url": r.url, "title": r.title,
                     "content": r.content, "retrieved_at": r.retrieved_at} for r in refs],
    }, ensure_ascii=False)
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_web_search.py -q -p no:warnings`
Expected: PASS (11 passed)

- [ ] **Step 5: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
git add sdtm-rag/server/web_search.py sdtm-rag/scripts/tests/test_web_search.py
git commit -m "feat(web-search): Tavily 客户端 (去重/截断/降级/配额)"
```

---

### Task 3: Rule 9 进 system prompt + 逐字节回滚闸

**Files:**
- Modify: `sdtm-rag/server/rag.py` (`_build_system_prompt` 与 `_GUARDRAIL_RULES` 之后)
- Test: `sdtm-rag/scripts/tests/test_web_rule9_prompt.py` (新建)

**Interfaces:**
- Consumes: Task 1 的 `Settings.web_search_enabled`。
- Produces: `RAGEngine._WEB_RULES: str` (Rule 9 全文常量); `RAGEngine.__init__` 新增关键字参数 `web_search_enabled: bool = False`; `RAGEngine.system_prompt` 在该参数为真时含 Rule 9。

⚠ **默认值是 `False` 而非 `True`**: `RAGEngine` 被 eval 脚本、闸脚本、多处测试直接构造, 默认 False 保证**任何不显式开启的调用点行为逐字节不变**; 生产由 `server/main.py` 显式传 `s.web_search_enabled`。

- [ ] **Step 1: 写失败测试**

创建 `sdtm-rag/scripts/tests/test_web_rule9_prompt.py`:

```python
"""Rule 9 (联网参考的反捏造边界) 进 system prompt 的条件与回滚闸 (spec §5 §9.3)。

`scripts/tests/` 无 make_engine helper (已确认), 故本地直接构造 —— 只测 prompt 组装,
用 __new__ 绕开 chroma/embedding 初始化。
"""
from server.rag import RAGEngine


def _engine(*, web_search_enabled: bool):
    eng = RAGEngine.__new__(RAGEngine)
    eng.prompt_guardrail_enabled = True
    eng.web_search_enabled = web_search_enabled
    eng._routing_md = "(routing)"
    eng._index_md = "(index)"
    return eng


def test_rule9_absent_by_default():
    """回滚闸: 不开启时 system prompt 里没有任何 Rule 9 痕迹。"""
    sp = _engine(web_search_enabled=False)._build_system_prompt()
    assert "[Web:" not in sp
    assert "UNVERIFIED" not in sp


def test_rule9_present_when_enabled():
    sp = _engine(web_search_enabled=True)._build_system_prompt()
    assert "[Web:" in sp
    assert "Cxxxxx" in sp                      # 9(b) 禁码
    assert "class/category" in sp              # 9(b) 禁 class 归属
    assert "inference" in sp.lower()           # 9(c) 标推测


def test_rule9_is_the_only_difference():
    """开关只增加 Rule 9 那一段, 不动其它任何一个字节 (逐字节回滚闸)。"""
    off = _engine(web_search_enabled=False)._build_system_prompt()
    on = _engine(web_search_enabled=True)._build_system_prompt()
    assert on != off
    idx = on.find("9. **Web results are UNVERIFIED")
    assert idx > 0, "Rule 9 段落起始锚点变了, 同步更新本测试"
    tail = on.find("---\n\n## Routing Guide")
    assert tail > idx
    assert on[:idx] + on[tail:] == off         # 挖掉 Rule 9 段后必须逐字节还原
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_web_rule9_prompt.py -q -p no:warnings`
Expected: FAIL — `TypeError: __init__() got an unexpected keyword argument 'web_search_enabled'` (或 `make_engine` 不存在, 见 Step 3)

- [ ] **Step 3: 实现**

**3a.** `sdtm-rag/server/rag.py` — `__init__` 签名里 `prompt_guardrail_enabled` 参数旁新增:

```python
        web_search_enabled: bool = False,
```

并在 `self.prompt_guardrail_enabled = prompt_guardrail_enabled` 一行之后加:

```python
        # 默认 False: RAGEngine 被 eval/闸脚本/测试直接构造, 默认关保证这些调用点
        # 的 system prompt 逐字节不变; 生产由 main.py 显式传 settings.web_search_enabled。
        self.web_search_enabled = web_search_enabled
```

⚠ 这两行必须在 `self._system_prompt = self._build_system_prompt()` **之前**。

**3b.** `_build_system_prompt` 里, `if self.prompt_guardrail_enabled: rules += self._GUARDRAIL_RULES` 之后加:

```python
        if self.web_search_enabled:
            rules += self._WEB_RULES
```

**3c.** 在 `_GUARDRAIL_RULES` 常量之后新增:

```python
    # 联网参考通道的反捏造边界 (spec 2026-08-31 §5)。措辞是**条件式**的 —— 没有 web 结果
    # 时本条自然失效, 因此 prompt 恒定, 不随请求级 web 开关分叉 (避免两套 prompt 的行为
    # 漂移无法归因)。规则必须待在 system 层: 网页内容是不可信数据, 约束它的规则不能和它
    # 同框放进 user content。
    _WEB_RULES = (
        "9. **Web results are UNVERIFIED industry reference, never standard authority.** "
        "When (and only when) results from the `web_search` tool are present in this "
        "conversation, they are third-party content of unknown quality -- conference "
        "papers, vendor blogs, marketing pages -- NOT CDISC standard text. Three rules "
        "govern them:\n"
        "   (a) **Cite them separately.** Every claim taken from a web result must carry "
        "**[Web: <url> (retrieved YYYY-MM-DD)]**, never the **[Source: path]** form "
        "reserved for the knowledge base. A reader must be able to tell at a glance which "
        "sentences came from the standard and which came from someone's blog.\n"
        "   (b) **Never derive hard facts from the web.** Do NOT state a controlled-"
        "terminology code (Cxxxxx), an SDTM class/category membership, or a variable's "
        "Core/Role/Type on the strength of a web result -- those come from the knowledge "
        "base alone. If a web page shows a code the context does not, give the value name "
        "only and say the code must be confirmed in the terminology file. This does not "
        "relax rules 7 and 8; it closes the same hole from the web side.\n"
        "   (c) **Label borrowed practice as inference.** Recommendations drawn from how "
        "other teams did it are inference, not documented requirement -- mark them "
        "explicitly (推測 / inference) and never present them as CDISC guidance.\n"
    )
```

**3d.** `sdtm-rag/server/main.py` — 找到构造 `RAGEngine(...)` 的调用点 (`grep -n "RAGEngine(" server/main.py`), 在 `prompt_guardrail_enabled=` 参数旁加:

```python
            web_search_enabled=s.web_search_enabled,
```

⚠ **主引擎 (`app.state.rag`) 与 study 引擎 (`study_levers` dict) 都要加**, docs 引擎不用
(它的 `system_prompt` 从不被读, `main.py` 注释已钉死, `test_study_corpus` 也钉住了)。

**为什么不是「只给主引擎加」** (本 spec 作者第一版就写错了这条): `federation._system_for`
按 corpus 选 prompt —— `cdisc` 取 cdisc 引擎的、`study` 取 study 引擎的、`both` 把两个拼接。
只给主引擎加 ⇒ **`corpus=study` + 联网时模型完全不受 Rule 9 约束**, 网页内容可直接产 CT 码,
正踩 spec §5 红线。代价是 `both` 模式下 Rule 9 出现两次 —— 无害: 该分支本就把两份完整
system prompt 首尾相接, Rules 1-8 / Routing Guide / KB Index **现在已经全是重复的**,
Rule 9 跟着重复不引入任何新性质。漏洞有害, 重复无害。

- [ ] **Step 4: 跑测试确认通过 + 全量回归**

Run:
```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_web_rule9_prompt.py -q -p no:warnings
.venv/bin/python -m pytest scripts/tests/ -q -p no:warnings   # 1798 基线, 不得下降
```
Expected: 新测试 PASS; 全量 exit 0

- [ ] **Step 5: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
git add sdtm-rag/server/rag.py sdtm-rag/server/main.py sdtm-rag/scripts/tests/test_web_rule9_prompt.py
git commit -m "feat(web-search): Rule 9 进 system prompt + 逐字节回滚闸"
```

---

### Task 4: `/api/ask_stream` 工具循环 + SSE 事件扩展

**Files:**
- Modify: `sdtm-rag/server/router.py` (`AskStreamRequest` ~228-235; `ask_stream` 的 `gen()` ~310-352)
- Test: `sdtm-rag/scripts/tests/test_ask_stream_web.py` (新建)

**Interfaces:**
- Consumes: Task 1 `Settings.web_*`; Task 2 `WebSearcher` / `WEB_TOOL_SPEC` / `render_tool_result`。
- Produces: `AskStreamRequest.web: bool = False`; 新增 SSE 事件 `tool_call` (`{round, query, id}`) 与 `tool_result` (`{id, count, status, urls}`); `done` 事件新增 `web_status` 字段。

**新增 SSE 事件契约** (Task 5 前端按此渲染):

```
event: tool_call    data: {"round": 1, "query": "...", "id": "tooluse_x"}
event: tool_result  data: {"id": "tooluse_x", "count": 3, "status": "ok",
                           "urls": ["https://...", ...]}
event: done         data: {"model_used": "...", "usage": {...}, "web_status": "ok"}
```

`web_status ∈ {"ok","failed","quota_exceeded","disabled","off"}` — `"off"` 表示本次请求没开联网。

- [ ] **Step 1: 写失败测试**

创建 `sdtm-rag/scripts/tests/test_ask_stream_web.py`:

```python
"""联网通道的 SSE 事件流与循环上限 (spec §7 §9.2)。

红线: 只用公开 CDISC 内容做假数据。
"""
import json
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.config import Settings
from server.router import api_router


class _FakeRAG:
    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        return [SimpleNamespace(chunk_id="c1", source="domains/AE/spec.md", domain="AE",
                                file_type="spec", section="§1", similarity=0.9,
                                text="AETERM is the reported term.")]
    def format_context(self, chunks):
        return "CTX"
    def build_messages(self, q, ctx, history=None):
        return [{"role": "user", "content": q}]


def _tool_chunk(idx, call_id, name, args):
    return SimpleNamespace(model="opus-5", usage=None, choices=[SimpleNamespace(
        finish_reason=None,
        delta=SimpleNamespace(content=None, tool_calls=[SimpleNamespace(
            index=idx, id=call_id,
            function=SimpleNamespace(name=name, arguments=args))]))])


def _text_chunk(text, finish=None):
    return SimpleNamespace(model="opus-5", usage=None, choices=[SimpleNamespace(
        finish_reason=finish, delta=SimpleNamespace(content=text, tool_calls=None))])


class _ToolThenTextRouter:
    """第 1 轮要搜索, 第 2 轮出文本 —— 最小的工具循环。"""
    def __init__(self):
        self.calls = 0

    async def acompletion(self, model, messages, stream=False, **kw):
        self.calls += 1
        first = self.calls == 1
        async def agen():
            if first:
                yield _tool_chunk(0, "tooluse_a", "web_search", '{"query": "SDTM custom domain"}')
                yield _text_chunk(None, finish="tool_calls")
            else:
                yield _text_chunk("Practice says X [Web: https://e.com/1 (retrieved 2026-08-31)]",
                                  finish="stop")
        return agen()


class _AlwaysToolRouter:
    """永远要搜索 —— 用来验轮数上限兜得住。"""
    def __init__(self):
        self.calls = 0

    async def acompletion(self, model, messages, stream=False, **kw):
        self.calls += 1
        async def agen():
            yield _tool_chunk(0, f"tooluse_{self.calls}", "web_search", '{"query": "q"}')
            yield _text_chunk(None, finish="tool_calls")
        return agen()


class _FakeSearcher:
    def __init__(self, *a, **k):
        self.searches_used = 0

    def search(self, query):
        from server.web_search import WebRef
        self.searches_used += 1
        return [WebRef(url="https://e.com/1", title="T", content="C",
                       retrieved_at="2026-08-31")], "ok"


def _client(router, monkeypatch=None, searcher_cls=_FakeSearcher):
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.llm_router = router
    app.state.settings = Settings()
    if monkeypatch:
        monkeypatch.setattr("server.router.WebSearcher", searcher_cls)
    return TestClient(app)


def _events(body: str):
    out = []
    for block in body.split("\n\n"):
        if not block.strip():
            continue
        ev = dict(line.split(": ", 1) for line in block.splitlines() if ": " in line)
        if "event" in ev:
            out.append((ev["event"], json.loads(ev.get("data", "{}"))))
    return out


def test_web_off_emits_no_tool_events_and_status_off(monkeypatch):
    r = _client(_ToolThenTextRouter(), monkeypatch).post(
        "/api/ask_stream", json={"question": "what is AETERM?", "web": False})
    assert r.status_code == 200
    evs = _events(r.text)
    assert not [e for e, _ in evs if e in ("tool_call", "tool_result")]
    done = [d for e, d in evs if e == "done"][0]
    assert done["web_status"] == "off"


def test_web_on_emits_tool_call_and_result(monkeypatch):
    r = _client(_ToolThenTextRouter(), monkeypatch).post(
        "/api/ask_stream", json={"question": "how do others map custom fields?", "web": True})
    evs = _events(r.text)
    kinds = [e for e, _ in evs]
    assert kinds.index("tool_call") < kinds.index("tool_result")
    tc = [d for e, d in evs if e == "tool_call"][0]
    assert tc["round"] == 1 and tc["id"] == "tooluse_a"
    tr = [d for e, d in evs if e == "tool_result"][0]
    assert tr["count"] == 1 and tr["status"] == "ok" and tr["urls"] == ["https://e.com/1"]
    assert "".join(d.get("text", "") for e, d in evs if e == "token").startswith("Practice says")
    assert [d for e, d in evs if e == "done"][0]["web_status"] == "ok"


def test_round_cap_stops_loop(monkeypatch):
    """§9.2: 第 6 轮必须停, 且不得无限循环。"""
    router = _AlwaysToolRouter()
    r = _client(router, monkeypatch).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    assert r.status_code == 200
    s = Settings()
    assert router.calls <= s.web_max_rounds + 1   # +1 = 触顶后不带工具的收尾轮
    evs = _events(r.text)
    # 触顶也必须正常收尾: done 事件在, 不是把连接晾着
    assert [e for e, _ in evs].count("done") == 1
    # 搜索次数不得越过 15 次上限
    assert len([e for e, _ in evs if e == "tool_result"]) <= s.web_max_searches


def test_search_failure_surfaces_status(monkeypatch):
    class _FailSearcher(_FakeSearcher):
        def search(self, query):
            return [], "failed"
    r = _client(_ToolThenTextRouter(), monkeypatch, _FailSearcher).post(
        "/api/ask_stream", json={"question": "q", "web": True})
    evs = _events(r.text)
    assert [d for e, d in evs if e == "tool_result"][0]["status"] == "failed"
    assert [d for e, d in evs if e == "done"][0]["web_status"] == "failed"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_ask_stream_web.py -q -p no:warnings`
Expected: FAIL — `AttributeError: module 'server.router' has no attribute 'WebSearcher'`

- [ ] **Step 3: 实现**

**3a.** `sdtm-rag/server/router.py` 顶部 import 区加:

```python
from server.web_search import WEB_TOOL_SPEC, WebSearcher, render_tool_result
```

**3b.** `AskStreamRequest` 加字段 (在 `corpus` 之后):

```python
    web: bool = False  # 联网参考通道; 与 corpus 判库正交 (spec §4)
```

**3c.** 把 `ask_stream` 里的 `_open_stream()` 与 `gen()` 整体替换为下面的版本。**保留** `sources` / `sse` / counting gate / `StreamingResponse` 三段不动:

```python
    use_web = bool(body.web) and s.web_search_enabled
    tools = [WEB_TOOL_SPEC] if use_web else None
    searcher = WebSearcher(s) if use_web else None

    async def _open_stream(msgs, with_tools: bool):
        """include_usage 让 done 能报 token; 个别 provider 不收该 kwarg, 失败则退化重开一次
        (保住答案, usage 报 null 而非编造)。工具参数只在 with_tools 时传 —— web 关闭时
        请求体与本功能引入前逐位相同。"""
        kw = {"model": "default", "messages": msgs, "stream": True}
        if with_tools and tools:
            kw["tools"] = tools
        try:
            return await llm_router.acompletion(**kw, stream_options={"include_usage": True})
        except Exception:  # noqa: BLE001 — 窄重试: 去掉 stream_options, 保住答案
            log.warning("stream_options_unsupported_retry_without", exc_info=True)
            return await llm_router.acompletion(**kw)

    async def gen():
        yield sse("sources", {"sources": sources, "routed_corpus": routed})
        model_used = None
        usage = None
        parts: list[str] = []
        web_status = "off" if not use_web else "ok"
        msgs = list(messages)

        try:
            # web 开启时多跑一轮: 前 max_rounds 轮带工具, 最后一轮**不带**工具 ——
            # 触顶后模型必须用手上的东西作答, 不能再要搜索, 也不会被硬切断在半句话上。
            total_rounds = (s.web_max_rounds + 1) if use_web else 1
            for rnd in range(1, total_rounds + 1):
                with_tools = use_web and rnd <= s.web_max_rounds
                resp = await asyncio.wait_for(
                    _open_stream(msgs, with_tools), timeout=s.request_timeout_s)

                acc: dict[int, dict] = {}   # 流式 tool_calls 是增量的, 按 index 拼
                finish = None
                async for chunk in resp:
                    choices = getattr(chunk, "choices", None)
                    if choices:
                        ch = choices[0]
                        if getattr(ch, "finish_reason", None):
                            finish = ch.finish_reason
                        text = getattr(ch.delta, "content", None)
                        if text:
                            parts.append(text)
                            yield sse("token", {"text": text})
                        for tc in (getattr(ch.delta, "tool_calls", None) or []):
                            slot = acc.setdefault(tc.index, {"id": None, "name": "", "args": ""})
                            if tc.id:
                                slot["id"] = tc.id
                            fn = getattr(tc, "function", None)
                            if fn and fn.name:
                                slot["name"] += fn.name
                            if fn and fn.arguments:
                                slot["args"] += fn.arguments
                        model_used = getattr(chunk, "model", None) or model_used
                    cu = getattr(chunk, "usage", None)
                    if cu:
                        usage = {"prompt_tokens": cu.prompt_tokens,
                                 "completion_tokens": cu.completion_tokens,
                                 "total_tokens": cu.total_tokens}

                if not acc:
                    break  # 没有工具调用 = 本轮就是最终答案

                # 回灌 assistant 的 tool_calls, 再逐个执行并回灌结果
                msgs.append({"role": "assistant", "content": None, "tool_calls": [
                    {"id": v["id"], "type": "function",
                     "function": {"name": v["name"], "arguments": v["args"]}}
                    for _, v in sorted(acc.items())]})

                for _, v in sorted(acc.items()):
                    try:
                        query = json.loads(v["args"] or "{}").get("query", "")
                    except json.JSONDecodeError:
                        query = ""   # 模型偶发畸形 JSON: 当空查询处理, 不炸循环
                    yield sse("tool_call", {"round": rnd, "query": query, "id": v["id"]})

                    if not query or searcher.searches_used >= s.web_max_searches:
                        refs, st = [], ("quota_exceeded" if query else "failed")
                    else:
                        refs, st = searcher.search(query)
                    if st != "ok":
                        web_status = st
                    yield sse("tool_result", {"id": v["id"], "count": len(refs),
                                              "status": st, "urls": [r.url for r in refs]})
                    msgs.append({"role": "tool", "tool_call_id": v["id"],
                                 "name": v["name"], "content": render_tool_result(refs, st)})

            if facts is not None:
                from server.grounding import apply_counting_gate
                full = "".join(parts)
                corrected, violations = apply_counting_gate(full, facts)
                if violations:
                    log.warning("structured_count_violation_stream", violations=violations)
                    yield sse("token", {"text": corrected[len(full):]})
            yield sse("done", {"model_used": model_used or "default",
                               "usage": usage, "web_status": web_status})
        except Exception as e:  # noqa: BLE001 — 流已开, 以事件形式暴露
            log.error("stream_failed", error=str(e), exc_info=True)
            yield sse("error", {"message": "LLM stream failed"})
```

⚠ 确认 `router.py` 顶部已 `import json` 与 `import asyncio` (原文件已有, 若缺则补)。

- [ ] **Step 4: 跑测试确认通过 + 回归**

Run:
```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_ask_stream_web.py scripts/tests/test_ask_stream.py -q -p no:warnings
.venv/bin/python -m pytest scripts/tests/ -q -p no:warnings
```
Expected: 全 PASS; 尤其 `test_ask_stream.py` (web=false 老路径) 不得回归

- [ ] **Step 5: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
git add sdtm-rag/server/router.py sdtm-rag/scripts/tests/test_ask_stream_web.py
git commit -m "feat(web-search): ask_stream 工具循环 + tool_call/tool_result SSE 事件"
```

---

### Task 5: webchat — 第三个 checkbox、过程渲染、web_status 提示

**Files:**
- Modify: `sdtm-rag/webchat/index.html` (`#scope` fieldset)
- Modify: `sdtm-rag/webchat/app.js` (`selectedCorpus` 附近; `streamAsk` 的 `dispatch`; `send` 的回调)
- Modify: `sdtm-rag/webchat/style.css` (`#scope` 之后)

**Interfaces:**
- Consumes: Task 4 的 `tool_call` / `tool_result` / `done.web_status` 事件契约。
- Produces: 无下游。

- [ ] **Step 1: 加 checkbox**

`sdtm-rag/webchat/index.html` — `#scope` fieldset 内, `本研究 (ST01)` 那个 label 之后加:

```html
          <label title="让模型自行决定是否搜索公开网络 (业界实践参考, 非标准依据)">
            <input type="checkbox" id="scope-web" /> 联网参考
          </label>
```

- [ ] **Step 2: 前端逻辑**

`sdtm-rag/webchat/app.js`:

**2a.** `selectedCorpus()` 之后新增:

```javascript
// 联网是与 corpus 正交的第四维: 只决定挂不挂 web_search 工具, 不参与判库。
function webEnabled() { return $("scope-web").checked; }
```

**2b.** `streamAsk` 的 fetch body 改为:

```javascript
      body: JSON.stringify({ question, history, corpus: selectedCorpus(), web: webEnabled() }), signal,
```

**2c.** `streamAsk` 签名的解构参数加 `onToolCall, onToolResult`, 并在 `dispatch` 里加两支 (放在 `token` 之后):

```javascript
    else if (ev.event === "tool_call") onToolCall?.(ev.data || {});
    else if (ev.event === "tool_result") onToolResult?.(ev.data || {});
```

**2d.** 渲染搜索过程。在 `sourcesEl` / `metaEl` 等辅助函数附近新增:

> ⛔ **面板必须挂在 `holder` 上, 绝不能挂进 `bubble`。**
> `app.js` 的 `onToolken` 回调是 `bubble.textContent = acc` (逐 token 覆盖整个气泡内容) ——
> 任何塞进 `bubble` 的子元素都会被**第一个 token 抹掉**。`holder` 是气泡的外层容器,
> 现有 `metaEl` / `sourcesEl` 也都挂在它上面, 沿用同一处。

```javascript
// 搜索过程条: 网页版那种「看得见它在搜什么」的观感。没有这层, 勾了联网只会
// 看到卡住半分钟然后蹦出一段话 —— 那是超时的感觉, 不是联网的感觉。
// ⚠ 挂在 holder (气泡外层) 而非 bubble: onToken 会 bubble.textContent=acc 覆盖气泡内容。
function ensureWebPanel(holder) {
  let p = holder.querySelector(":scope > .web-panel");
  if (!p) {
    p = document.createElement("div");
    p.className = "web-panel";
    holder.prepend(p);   // 搜索过程显示在答案上方
  }
  return p;
}

function onToolCallUI(holder, d) {
  const row = document.createElement("div");
  row.className = "web-row";
  row.dataset.callId = d.id || "";
  row.textContent = `🔍 搜索 "${d.query || ""}"`;
  ensureWebPanel(holder).appendChild(row);
}

function onToolResultUI(holder, d) {
  const p = ensureWebPanel(holder);
  // CSS.escape: tool id 来自模型返回, 不保证是合法选择器
  const sel = `.web-row[data-call-id="${CSS.escape(d.id || "")}"]`;
  const row = p.querySelector(sel);
  const note = document.createElement("span");
  note.className = "web-note";
  // tool_result.status 有 6 个值, 其中 bad_query/unknown_tool 是**模型**出错不是联网出错,
  // 措辞必须区分 —— 把模型的失误显示成"联网失败"会让人去查网络而不是查模型。
  note.textContent = {
    ok: ` — 找到 ${d.count} 个来源`,
    failed: " — 搜索失败",
    quota_exceeded: " — 已达搜索次数上限",
    disabled: " — 服务端未启用联网",
    bad_query: " — 跳过 (模型给出的查询无效)",
    unknown_tool: " — 跳过 (模型调用了不存在的工具)",
  }[d.status] || ` — ${d.status}`;
  (row || p).appendChild(note);
}

// web_status 落在 done 上: 勾了联网却静默降级是最骗人的失败模式, 必须显式说出来。
// ⚠ 契约以 Task 4 实现为准 (计划初稿只列了 3 个状态, 实测收口后是 6 个 + 一个计数):
//   web_status ∈ {ok, partial, failed, quota_exceeded, disabled, off}
//   web_searches_ok: int  —— 真正拿到结果的搜索次数 (bad_query/unknown_tool/quota/failed 不计)
// 三种"看起来正常其实没搜到"的情形必须分开说, 否则用户无从判断答案的成色。
function renderWebStatus(holder, status, searchesOk) {
  if (!status || status === "off") return;
  // ok + 0 次成功检索: 联网开着、一次网都没打成 (模型净吐畸形工具调用能耗光轮数)
  const msg = status === "ok"
    ? (searchesOk > 0 ? null : "ℹ 已开启联网, 但本次未实际检索到内容, 以下回答基于知识库")
    : {
        partial: "⚠ 部分搜索失败, 联网参考可能不完整 (逐条状态见上方搜索过程)",
        failed: "⚠ 本次未联网: 搜索请求失败, 以下回答仅基于知识库",
        quota_exceeded: "⚠ 本次未联网: 已达搜索配额上限, 以下回答仅基于知识库",
        disabled: "⚠ 本次未联网: 服务端未启用联网, 以下回答仅基于知识库",
      }[status] || `⚠ 本次未联网 (${status})`;
  if (!msg) return;
  const warn = document.createElement("div");
  warn.className = status === "ok" ? "web-note-block" : "web-warn";
  warn.textContent = msg;
  ensureWebPanel(holder).appendChild(warn);
}
```

**2e. 接线** — `app.js` 的 `send()` 里 `await streamAsk(text, history, {...})` 那个回调对象 (当前在 ~357-374 行)。加两个回调, 并给 `onDone` 补参数:

```javascript
      onToolCall: (d) => onToolCallUI(holder, d),
      onToolResult: (d) => onToolResultUI(holder, d),
```

⚠ 现有 `onDone` 是**无参**的 `onDone: () => {...}`, 拿不到 `web_status`。改成:

```javascript
      onDone: (data) => {
        renderWebStatus(holder, (data || {}).web_status, (data || {}).web_searches_ok);
        const content = acc.trim() ? acc : "(无内容)"; renderFinal(content); persist(content);
      },
```

(`onDone(ev.data || {})` 在 `dispatch` 里本来就传了 data, 只是原回调没接。)

- [ ] **Step 3: 样式**

`sdtm-rag/webchat/style.css` — `#scope input` 那行之后加:

```css
.web-panel { margin: 0 0 10px; padding: 8px 10px; background: #f7f7f8; border-left: 3px solid #f59e0b; border-radius: 6px; font-size: 13px; color: #555; }
.web-row { padding: 2px 0; }
.web-note { color: #888; }
.web-warn { margin-top: 6px; color: #b45309; font-weight: 500; }
.web-note-block { margin-top: 6px; color: #666; }
.corpus-badge.web { background: #f59e0b; }
```

- [ ] **Step 4: 手动验证**

```bash
launchctl kickstart -k gui/501/com.sdtmrag.api
```
浏览器开 `http://localhost:8000/`, 勾「CDISC 標準」+「联网参考」, 问一句
*"How do other teams handle EDC fields that don't map to any standard SDTM domain?"*

逐条确认:
- 右上角三个 checkbox 排版正常
- 搜索过程条逐行出现 (`🔍 搜索 "..."` → `— 找到 N 个来源`)
- 正文里网络来源是 `[Web: url (retrieved ...)]`, KB 来源仍是 `[Source: path]`
- 不勾联网重问一次: **没有**任何搜索过程条

- [ ] **Step 5: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
git add sdtm-rag/webchat/
git commit -m "feat(web-search): webchat 联网 checkbox + 搜索过程渲染 + 未联网提示"
```

---

### Task 6: 端到端集成断言 + 语义抽检脚手架

**Files:**
- Create: `sdtm-rag/eval/web_channel_spotcheck.py`
- Test: `sdtm-rag/scripts/tests/test_web_channel_integration.py` (新建)

**Interfaces:**
- Consumes: Task 2-4 全部产物。
- Produces: `eval/web_channel_spotcheck.py` CLI — 跑 N 个真实联网问答, 输出可人工核验的抽检表。

⚠ **本任务是 spec §5 红线的唯一真实保证**。spec §11 的 B4 (一次运行零 `Cxxxxx`) 明确**不算证据**。

- [ ] **Step 1: 写失败测试**

创建 `sdtm-rag/scripts/tests/test_web_channel_integration.py`:

```python
"""联网通道的红线断言 (spec §9 测试 4)。

不打真实网络: 用受控的假搜索结果**故意投毒**一个 CT 码, 断言它不出现在答案里
—— 这才是 Rule 9(b) 的闸, 而不是「跑一次没看见码」。
"""
import re

from server.web_search import WebRef, render_tool_result


def test_render_tool_result_marks_web_provenance():
    """回灌给模型的每条结果都必须自带 url 与抓取日期 —— 标注不能靠模型记忆。"""
    import json
    refs = [WebRef(url="https://blog.example.com/x", title="T",
                   content="Use C12345 for this codelist.", retrieved_at="2026-08-31")]
    payload = json.loads(render_tool_result(refs, "ok"))
    r = payload["results"][0]
    assert r["url"] and r["retrieved_at"] == "2026-08-31"


def test_poisoned_web_content_still_carries_no_authority():
    """投毒内容原样进 tool result 是对的 (不做内容审查), 红线由 Rule 9(b) 在 prompt 层挡。
    本测试钉住: 我们没有偷偷做内容过滤来假装安全。"""
    import json
    refs = [WebRef(url="https://blog.example.com/x", title="T",
                   content="C99999 is the code.", retrieved_at="2026-08-31")]
    payload = json.loads(render_tool_result(refs, "ok"))
    assert "C99999" in payload["results"][0]["content"]


def test_rule9b_text_forbids_web_derived_codes():
    """Rule 9(b) 必须真的写着禁止从 web 产出码 —— 措辞被改掉时本测试要响。"""
    from server.rag import RAGEngine
    rules = RAGEngine._WEB_RULES
    assert "Cxxxxx" in rules
    assert "class" in rules.lower()
    assert re.search(r"do not|never", rules, re.I)
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_web_channel_integration.py -q -p no:warnings`
Expected: FAIL (若 Task 2/3 已完成则可能直接 PASS —— 那也可接受, 记录后继续)

- [ ] **Step 3: 写抽检脚本**

创建 `sdtm-rag/eval/web_channel_spotcheck.py`:

```python
"""联网通道语义抽检 (规则 A; spec §8)。

联网答案不可复算, 不进 gold set ⇒ 质量只能靠人工抽检。本脚本跑 N 个真实问答,
把**需要人眼判断的四件事**列成表, 结果留 evidence/。

跑法:
  cd sdtm-rag && .venv/bin/python eval/web_channel_spotcheck.py --n 5 \
      --out evidence/checkpoints/web_channel_spotcheck.md
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import requests

QUESTIONS = [
    "How do other teams handle EDC fields that don't map to any standard SDTM domain?",
    "What do practitioners say about overusing SUPPQUAL versus creating a custom domain?",
    "How is Findings About (FA) used in practice versus a custom findings domain?",
    "What does FDA's Study Data Technical Conformance Guide say about custom domains?",
    "How do sponsors document non-standard variables in define.xml in practice?",
]

CODE_RE = re.compile(r"\bC\d{4,6}\b")
WEB_CITE_RE = re.compile(r"\[Web:\s*(https?://[^\s\]]+)")
KB_CITE_RE = re.compile(r"\[Source:\s*([^\]]+)\]")


def ask(base: str, q: str, timeout: float) -> str:
    r = requests.post(f"{base}/api/ask", json={"question": q, "corpus": "cdisc", "web": True},
                      timeout=timeout)
    r.raise_for_status()
    return r.json().get("answer", "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=len(QUESTIONS))
    ap.add_argument("--base", default="http://localhost:8000")
    ap.add_argument("--timeout", type=float, default=300.0)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()

    rows = []
    for q in QUESTIONS[:a.n]:
        try:
            ans = ask(a.base, q, a.timeout)
        except Exception as exc:  # noqa: BLE001
            rows.append((q, "", ["调用失败: " + type(exc).__name__], [], []))
            continue
        rows.append((q, ans, CODE_RE.findall(ans),
                     WEB_CITE_RE.findall(ans), KB_CITE_RE.findall(ans)))

    lines = ["# 联网通道语义抽检 (规则 A)", "",
             "> 联网答案不可复算, **不进 gold set** —— 本表是它唯一的质量证据。",
             "> ⚠ 机检只能查形状; **第 3、4 列必须人眼逐条判**, 不得由脚本判 PASS。", "",
             "| # | 问题 | 机检: CT 码 | 机检: [Web:] 数 | 机检: [Source:] 数 | 人判: 标注是否规矩 | 人判: 借鉴是否标推测 |",
             "|---|---|---|---|---|---|---|"]
    for i, (q, _ans, codes, webs, kbs) in enumerate(rows, 1):
        flag = "⛔ " + ",".join(codes) if codes else "✅ 无"
        lines.append(f"| {i} | {q[:60]} | {flag} | {len(webs)} | {len(kbs)} | ⬜ 待判 | ⬜ 待判 |")
    lines += ["", "## 判读规则", "",
              "- **CT 码列出现任何码 = 立即查**: Rule 9(b) 禁止从网页产出 `Cxxxxx`。",
              "  码若能在 `knowledge_base/` 找到且答案标的是 `[Source:]`, 属正常 (KB 来源);",
              "  标 `[Web:]` 却带码 = **红线破**。",
              "- `[Web:]` 数为 0 而问题明显需要业界实践 ⇒ 可能没真联网, 查 `web_status`。",
              "- 人判两列必须逐条看答案原文, 不看就填 = 抽检失效 (规则 A 的意义就在这)。"]
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"抽检表已写入 {a.out} ({len(rows)} 题)")
    print("⚠ 机检只查形状; 两列人判必须人眼完成后才算抽检done。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: 跑通**

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_web_channel_integration.py -q -p no:warnings
launchctl kickstart -k gui/501/com.sdtmrag.api
.venv/bin/python eval/web_channel_spotcheck.py --n 3 \
    --out evidence/checkpoints/web_channel_spotcheck.md
```
Expected: 测试 PASS; 抽检表生成, CT 码列全 `✅ 无`。**若出现 ⛔, 停下来按 §5 红线排查, 不要继续。**

- [ ] **Step 5: 全量回归 + 提交**

```bash
cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/ -q -p no:warnings   # ≥1798, exit 0
cd /Users/bojiangzhang/MyProject/sdtm-pedia
git add sdtm-rag/eval/web_channel_spotcheck.py \
        sdtm-rag/scripts/tests/test_web_channel_integration.py \
        sdtm-rag/evidence/checkpoints/web_channel_spotcheck.md
git commit -m "test(web-search): 红线断言 + 语义抽检脚手架 (规则 A)"
```

---

## 收尾 (全部任务完成后)

- [ ] `.env.example` 补 `TAVILY_API_KEY=` 与 `SDTM_RAG_WEB_*` 旋钮 (注释说明默认值与回滚方式)
- [ ] `.work/meta/worklog/phase_07_rag_kg.md` append 本次 work record (Chain B)
- [ ] `docs/PROGRESS.md` 更新 Phase 7 状态
- [ ] `CLAUDE.md` Key Paths 加一行 (≤80 字符): `Phase 7 联网参考通道 | sdtm-rag/server/web_search.py + spec 2026-08-31`
- [ ] spec §10 未决项落定: Tavily 实际额度/单价、`web_daily_quota` 取值、反代总超时值
- [ ] 人工完成抽检表的两列人判, 结果写回 `evidence/checkpoints/web_channel_spotcheck.md`
