"""webchat 静态资源必须每次回源校验 (浏览器陈旧缓存缺陷)。

实测坐实的现场: 服务器吐的是新 app.js (27310 B, 含 selectable_models), 浏览器执行的
loadModelName 只有 428 字符 —— 一份连 #scope 都没有的旧版 (缓存里 16446 B); `performance`
里 HTML 与 app.js 的 transferSize 双双为 0 (零网络, 纯磁盘缓存命中)。Cmd+Shift+R 强刷后一切
正常 ⇒ 代码没问题, 是响应头没告诉浏览器"要来问一次"。

根因: `/` 的 FileResponse 与 `/static` 的 StaticFiles 都只发 ETag/Last-Modified, 不发
Cache-Control。缺 Cache-Control 的响应会触发浏览器的**启发式缓存** (惯例取 Last-Modified
age 的 10%), 于是一个放了两周的 app.js 能在部署后被本地缓存直接吃掉一天多都不回源。

这条缺陷骗人的地方: 模型下拉 + 三个勾选一起消失, 看起来像"新功能没上线"而不是"浏览器没去
拿新文件"。

两个方向都锁:
- `/` 与 `/static/*` 必须带能强制回源的 Cache-Control (no-cache), 且不能是 no-store ——
  no-store 会把缓存整个关掉, 每次全量重下; 要的是"必须校验, 命中则 304 空 body";
- `/api/*` 不许被顺手波及 —— 缓存策略是给静态壳子的, 不是给接口的。

每条都跑两遍配置: 默认态, 以及 go-live 真正在用的 auth_enabled=True 共享栈。只钉默认态的话,
守的是开发配置, 生产配置无人守。

⚠ 这一层只证明"服务器说对了话"。"浏览器真的照做了"由真浏览器端到端闸证明, 见
scripts/tests/test_webchat_cache_browser.py (未装 playwright 时可见地 skip)。
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from server import main as main_mod
from server.auth import hash_password
from server.config import Settings

_PASSWORD = "cache-gate-test-pw"


def _settings(**over) -> Settings:
    """联邦 / study 一律关掉: 本文件只关心静态壳子的响应头, 别把那几条 lifespan 拖进来。"""
    return Settings(**{"federation_enabled": False, "study_lookup_enabled": False,
                       "study_docs_enabled": False, **over})


@pytest.fixture(params=["auth_off", "auth_on"])
def webchat_client(request, tmp_path, monkeypatch):
    """把 _WEBCHAT_DIR 指到临时目录后再 create_app() —— 测的是生产接线本身 (mount + 首页
    路由), 不是一个长得像的复制品。TestClient 不进 with, 故不跑 lifespan (静态文件用不着
    RAG 引擎); /api/info 要读的 app.state.rag 用最小 stub 顶上。

    auth_on 这一遍就是 go-live 的形态 (deploy/README.md 的 0.0.0.0 + 登录门)。"""
    (tmp_path / "index.html").write_text("<!DOCTYPE html><title>t</title>", encoding="utf-8")
    (tmp_path / "app.js").write_text("window.x = 1;\n", encoding="utf-8")
    monkeypatch.setattr(main_mod, "_WEBCHAT_DIR", tmp_path)

    auth_on = request.param == "auth_on"
    over = dict(auth_enabled=True, session_secret="0" * 64,
                shared_password_hash=hash_password(_PASSWORD)) if auth_on else {}
    app = main_mod.create_app(_settings(**over))
    app.state.rag = SimpleNamespace(
        collection=SimpleNamespace(count=lambda: 0),
        structured_lookup_enabled=False, hybrid_enabled=False, hybrid_fusion=None,
        prompt_guardrail_enabled=False, web_search_enabled=False,
    )
    client = TestClient(app)
    if auth_on:
        # 登录门排在缓存策略前面: 没登录时壳子根本不是文件而是 302。先确认这个次序, 再登录,
        # 后面每条断言才是在对"真被服务出来的文件"说话。
        assert client.get("/", follow_redirects=False).status_code == 302
        assert client.post("/login", data={"password": _PASSWORD},
                           follow_redirects=False).status_code == 303
    return client


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


@pytest.mark.parametrize("conditional", ["If-None-Match", "If-Modified-Since"])
def test_static_still_answers_304_on_revalidation(webchat_client, conditional):
    """回源校验 ≠ 每次重传。文件没变时必须换回 304 空 body —— 这条同时证明 ETag /
    Last-Modified 通路没被响应头改动打断。

    两条条件请求路径都走一遍: starlette 的 is_not_modified 先看 If-None-Match, 没有才回落
    到 If-Modified-Since, 只钉前者会漏掉后半条分支。"""
    first = webchat_client.get("/static/app.js")
    validator = first.headers["etag" if conditional == "If-None-Match" else "last-modified"]
    second = webchat_client.get("/static/app.js", headers={conditional: validator})
    assert second.status_code == 304
    assert second.content == b""
    # 304 上也得带 Cache-Control, 否则浏览器刷新缓存条目时又退回启发式。
    assert "no-cache" in _cache_control(second).lower()


@pytest.mark.parametrize("path", ["/api/health", "/api/info"])
def test_api_responses_are_untouched(webchat_client, path):
    """反向钉: 缓存头只加给静态壳子。接口若被顺手加上 no-cache, 表面无害, 却是把一条没人
    要求的策略偷渡进了 API 契约。

    注意这不是"/api/* 一律无 Cache-Control"的全局不变量: server/router.py 的 SSE 流本来
    就自带一条合法的 no-cache (流式响应不能被缓存)。这里钉的是这两条普通 JSON 接口。"""
    r = webchat_client.get(path)
    assert r.status_code == 200
    assert "cache-control" not in {k.lower() for k in r.headers}


def test_boots_without_webchat_dir(tmp_path, monkeypatch):
    """_WEBCHAT_DIR.exists() 守卫语义: webchat/ 缺席时照常起, 只是没有壳子路由。"""
    monkeypatch.setattr(main_mod, "_WEBCHAT_DIR", tmp_path / "missing")
    client = TestClient(main_mod.create_app(_settings()))
    assert client.get("/").status_code == 404
    assert client.get("/api/health").status_code == 200
