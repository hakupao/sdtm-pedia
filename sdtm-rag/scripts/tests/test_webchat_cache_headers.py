"""webchat 静态资源必须每次回源校验 (浏览器陈旧缓存缺陷)。

实测坐实的现场: 服务器吐的是新 app.js (27310 B, 含 selectable_models), 浏览器执行的却是
16446 B 的旧版; `performance` 里 HTML 与 app.js 的 transferSize 双双为 0 —— 零网络, 纯磁盘
缓存命中。Cmd+Shift+R 强刷后一切正常 ⇒ 代码没问题, 是响应头没告诉浏览器"要来问一次"。

根因: `/` 的 FileResponse 与 `/static` 的 StaticFiles 都只发 ETag/Last-Modified, 不发
Cache-Control。缺 Cache-Control 的响应会触发浏览器的**启发式缓存** (惯例取 Last-Modified
age 的 10%), 于是一个放了两周的 app.js 能在部署后被本地缓存直接吃掉一天多都不回源。

这条缺陷骗人的地方: 缓存里那份老到连 `#scope` 都没有, 三个勾选 + 新下拉一起消失, 看起来像
"新功能没上线"而不是"浏览器没去拿新文件"。

两个方向都锁:
- `/` 与 `/static/*` 必须带能强制回源的 Cache-Control (no-cache), 且不能是 no-store ——
  no-store 会把缓存整个关掉, 每次全量重下; 要的是"必须校验, 命中则 304 空body";
- `/api/*` 不许被顺手波及 —— 缓存策略是给静态壳子的, 不是给接口的。

⚠ 这一层只证明"服务器说对了话"。"浏览器真的照做了"由真浏览器端到端闸证明, 见
scripts/webchat_cache_e2e.py 的 runbook 与 .superpowers/sdd/2026-09-02-webchat-cache/report.md。
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from server import main as main_mod
from server.config import Settings


def _settings(**over) -> Settings:
    """联邦 / study 一律关掉: 本文件只关心静态壳子的响应头, 别把那几条 lifespan 拖进来。"""
    return Settings(**{"federation_enabled": False, "study_lookup_enabled": False,
                       "study_docs_enabled": False, **over})


@pytest.fixture
def webchat_client(tmp_path, monkeypatch):
    """把 _WEBCHAT_DIR 指到临时目录后再 create_app() —— 测的是生产接线本身 (mount + 首页
    路由), 不是一个长得像的复制品。TestClient 不进 with, 故不跑 lifespan (静态文件用不着
    RAG 引擎); /api/info 要读的 app.state.rag 用最小 stub 顶上。"""
    (tmp_path / "index.html").write_text("<!DOCTYPE html><title>t</title>", encoding="utf-8")
    (tmp_path / "app.js").write_text("window.x = 1;\n", encoding="utf-8")
    monkeypatch.setattr(main_mod, "_WEBCHAT_DIR", tmp_path)
    app = main_mod.create_app(_settings())
    app.state.rag = SimpleNamespace(
        collection=SimpleNamespace(count=lambda: 0),
        structured_lookup_enabled=False, hybrid_enabled=False, hybrid_fusion=None,
        prompt_guardrail_enabled=False, web_search_enabled=False,
    )
    return TestClient(app)


def _cache_control(response) -> str:
    return response.headers.get("cache-control", "")


@pytest.mark.parametrize("path", ["/", "/static/app.js"])
def test_shell_forces_revalidation(webchat_client, path):
    r = webchat_client.get(path)
    assert r.status_code == 200
    directives = {d.strip() for d in _cache_control(r).lower().split(",")}
    # no-cache = "可以存, 但每次用之前必须问一次"。max-age=0 + must-revalidate 也算等效,
    # 故按语义收而不是按字面串比。
    assert "no-cache" in directives or {"max-age=0", "must-revalidate"} <= directives, (
        f"{path} 的 Cache-Control 不足以强制回源: {_cache_control(r)!r}"
    )


@pytest.mark.parametrize("path", ["/", "/static/app.js"])
def test_shell_does_not_disable_caching_outright(webchat_client, path):
    """no-store 会让浏览器每次全量重下, 白白浪费带宽 —— 修的是陈旧, 不是把缓存砍了。"""
    assert "no-store" not in _cache_control(webchat_client.get(path)).lower()


def test_static_still_answers_304_on_revalidation(webchat_client):
    """回源校验 ≠ 每次重传。文件没变时带 If-None-Match 必须换回 304 空 body ——
    这条同时证明 ETag 通路没被响应头改动打断。"""
    first = webchat_client.get("/static/app.js")
    etag = first.headers["etag"]
    second = webchat_client.get("/static/app.js", headers={"If-None-Match": etag})
    assert second.status_code == 304
    assert second.content == b""
    # 304 上也得带 Cache-Control, 否则浏览器刷新缓存条目时又退回启发式。
    assert "no-cache" in _cache_control(second).lower()


@pytest.mark.parametrize("path", ["/api/health", "/api/info"])
def test_api_responses_are_untouched(webchat_client, path):
    """反向钉: 缓存头只加给静态壳子。接口若被顺手加上 no-cache, 表面无害, 却是把一条
    没人要求的策略偷渡进了 API 契约。"""
    r = webchat_client.get(path)
    assert r.status_code == 200
    assert "cache-control" not in {k.lower() for k in r.headers}


def test_boots_without_webchat_dir(tmp_path, monkeypatch):
    """_WEBCHAT_DIR.exists() 守卫语义: webchat/ 缺席时照常起, 只是没有壳子路由。"""
    monkeypatch.setattr(main_mod, "_WEBCHAT_DIR", tmp_path / "missing")
    client = TestClient(main_mod.create_app(_settings()))
    assert client.get("/").status_code == 404
    assert client.get("/api/health").status_code == 200
