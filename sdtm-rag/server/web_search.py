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
import threading
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
    # Task 4 把搜索放进 asyncio.to_thread ⇒ 跨请求会并发跑进线程池, 而 _bump_day 对
    # 类级状态做的是 read-modify-write (`+= 1` = LOAD/ADD/STORE 三步) 加日期翻转的
    # check-then-act。压测"零丢失"证明的只是窗口窄, 不是操作原子, 且"换 free-threaded
    # 构建时记得加锁"这类注释的历史命中率接近零 —— 所以直接上锁, 不留 TODO。
    _day_lock = threading.Lock()

    def __init__(self, settings, api_key: str | None = None) -> None:
        self.s = settings
        self.api_key = api_key if api_key is not None else os.getenv("TAVILY_API_KEY")
        self.searches_used = 0

    @classmethod
    def _bump_day(cls) -> int:
        today = _dt.date.today().isoformat()
        with cls._day_lock:          # 日期翻转的 check-then-act 与 += 1 必须在同一临界区内
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
        # 但 "results" 存在却不是 list (比如 Tavily 抽风返回字符串), 是结构异常, 与网络
        # 失败同级 —— 不校验的话下面 it.get(...) 会在非 dict 元素上抛 AttributeError 穿透出去,
        # 违反 §7 "降级不得抛异常" 的红线。
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
