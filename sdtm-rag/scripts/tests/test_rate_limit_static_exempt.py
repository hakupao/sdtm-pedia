"""限流不能把静态壳子算进配额 (模块化前端冷加载被 429 打死的生产缺陷)。

实测坐实的现场: webchat 前端拆成 ES 模块后, 冷加载一次 `/` 是 ~16 个请求 (`/` +
`/static/style.css` + `/static/app.js` + 7 个 `/static/js/*.js` + vendor + `/api/info`)。
`RateLimitMiddleware` 按 IP 记每一个 HTTP 请求, 配额是 BURST=10 / PER_MIN=30, 豁免表里只有
一条精确路径 `/api/health` ⇒ 每次刷新都有 2-3 个模块文件随机吃 429, 页面根本起不来。

缓存救不了: 静态壳子按设计发 `Cache-Control: no-cache` (见
scripts/tests/test_webchat_cache_headers.py), 每次都必须回源校验, 请求数一个不少。

这条缺陷骗人的地方: 挂掉的模块是随机的 (谁排在 burst 耗尽之后谁死), 表现像"前端偶发白屏 /
某个功能时有时无", 而不是"限流配额算错了对象"。

两个方向都锁:
- `/` 与 `/static/*` 是一次页面加载的固定开销, 不是攻击面, 必须整体豁免;
- `/api/*` 不许被顺手波及 —— 限流真正要挡的是接口 (LLM 调用有成本), 豁免若漏进 `/api/`,
  这个中间件就等于没装。
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from server import main as main_mod
from server.config import Settings

# 生产配额, 原样照抄 —— 用更小的数字能让测试更快红, 但守的就不是生产那条线了。
_BURST = 10
_PER_MIN = 30


def _settings(**over) -> Settings:
    """联邦 / study 一律关掉: 本文件只关心限流中间件, 别把那几条 lifespan 拖进来。

    auth_enabled 保持默认的 False 即可: install_security 的接线次序是
    SecurityHeaders -> RateLimit -> Session -> AuthGate -> route, 限流排在登录门**之前**,
    所以豁免行为与登录与否无关, 不需要再跑一遍 auth_on。"""
    return Settings(**{"rate_limit_enabled": True, "rate_limit_per_min": _PER_MIN,
                       "rate_limit_burst": _BURST, "federation_enabled": False,
                       "study_lookup_enabled": False, "study_docs_enabled": False, **over})


@pytest.fixture
def client(tmp_path, monkeypatch):
    """把 _WEBCHAT_DIR 指到临时目录后再 create_app() —— 测的是生产接线本身 (mount + 首页
    路由 + install_security), 不是一个长得像的复制品。TestClient 不进 with, 故不跑 lifespan;
    /api/info 要读的 app.state.rag 用最小 stub 顶上。

    `js/a.js` 是关键: 拆模块后新增的正是这层子目录, 只钉 `/static/app.js` 会漏掉它。"""
    (tmp_path / "index.html").write_text("<!DOCTYPE html><title>t</title>", encoding="utf-8")
    (tmp_path / "app.js").write_text("window.x = 1;\n", encoding="utf-8")
    (tmp_path / "js").mkdir()
    (tmp_path / "js" / "a.js").write_text("export const a = 1;\n", encoding="utf-8")
    monkeypatch.setattr(main_mod, "_WEBCHAT_DIR", tmp_path)

    app = main_mod.create_app(_settings())
    app.state.rag = SimpleNamespace(
        collection=SimpleNamespace(count=lambda: 0),
        structured_lookup_enabled=False, hybrid_enabled=False, hybrid_fusion=None,
        prompt_guardrail_enabled=False, web_search_enabled=False,
    )
    # raise_server_exceptions=False: 断言只看状态码, 路由内部若出错也不该把限流这条闸的
    # 结论换成一个 traceback。
    return TestClient(app, raise_server_exceptions=False)


@pytest.mark.parametrize("path", ["/", "/static/app.js", "/static/js/a.js"])
def test_static_shell_never_429s_past_burst(client, path):
    """40 次 >> BURST=10: 若静态资源仍进桶, 第 11 次起必 429。一个 TestClient ⇒ 同一个
    client IP ⇒ 同一个桶, 三条路径各自跑满 40 次都不许掉一个。"""
    codes = [client.get(path).status_code for _ in range(40)]
    assert set(codes) == {200}, f"{path} 被限流吃掉: {sorted(set(codes))}"


def test_api_still_rate_limited(client):
    """反向钉: 豁免只给静态壳子。若前缀匹配写宽了 (比如空前缀 / 把 `/api/` 也放行),
    这个中间件就形同虚设 —— 这条测试必须在那时红。"""
    codes = [client.get("/api/info").status_code for _ in range(12)]
    assert 429 not in codes[:_BURST], f"burst 内不该 429: {codes[:_BURST]}"
    assert 429 in codes[_BURST:], f"burst 耗尽后必须 429, 实际: {codes}"
