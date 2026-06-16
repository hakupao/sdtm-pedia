"""Phase 3 sharing — login gate + hardening (DEPLOY_PLAN §3).

Covers: password hashing, the auth gate (401 for /api/*, 302 for HTML, health/login
exempt), session login/logout round-trip, open-redirect guard, the per-IP token-bucket
rate limiter, security headers, SSE pass-through (middleware must not break streaming),
and the compare error-string sanitizer.
"""
from __future__ import annotations

import asyncio

import pytest
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, StreamingResponse
from fastapi.testclient import TestClient

from server.auth import (
    LoginThrottle,
    TokenBucketLimiter,
    _safe_next,
    hash_password,
    install_security,
    sanitize_compare_errors,
    verify_password,
)
from server.compare import ModelAnswer
from server.config import Settings

# ── Password hashing ──────────────────────────────────────────────────────

def test_hash_verify_roundtrip():
    h = hash_password("correct horse battery staple")
    assert "$" in h  # salt$hash
    assert verify_password("correct horse battery staple", h) is True
    assert verify_password("wrong", h) is False


def test_hash_is_salted_unique():
    # Same password -> different stored hash (random salt), both verify.
    a, b = hash_password("pw"), hash_password("pw")
    assert a != b
    assert verify_password("pw", a) and verify_password("pw", b)


def test_verify_rejects_garbage_stored():
    for bad in ["", "nodollar", "$", "a$", "$b", "x$y$z"]:
        assert verify_password("pw", bad) is False


# ── App factories ───────────────────────────────────────────────────────────

def _auth_settings(**over) -> Settings:
    base = dict(
        auth_enabled=True,
        session_secret="0" * 64,
        shared_password_hash=hash_password("s3cret-pw"),
        rate_limit_enabled=False,
        security_headers_enabled=True,
    )
    base.update(over)
    return Settings(**base)


def _app(settings: Settings) -> FastAPI:
    app = FastAPI()

    @app.get("/")
    def index():
        return PlainTextResponse("CHAT SHELL")

    @app.get("/api/health")
    def health():
        return {"status": "ok"}

    @app.get("/api/info")
    def info():
        return {"default_model": "deepseek/deepseek-v4-pro"}

    @app.get("/api/sse")
    def sse():
        async def gen():
            for i in range(3):
                yield f"chunk{i}\n"
        return StreamingResponse(gen(), media_type="text/event-stream")

    install_security(app, settings)
    return app


# ── Auth gate ────────────────────────────────────────────────────────────────

def test_health_exempt_no_auth():
    c = TestClient(_app(_auth_settings()))
    r = c.get("/api/health")
    assert r.status_code == 200 and r.json()["status"] == "ok"


def test_api_unauthenticated_401():
    c = TestClient(_app(_auth_settings()))
    r = c.get("/api/info")
    assert r.status_code == 401


def test_html_unauthenticated_redirects_to_login():
    c = TestClient(_app(_auth_settings()), follow_redirects=False)
    r = c.get("/")
    assert r.status_code in (302, 303, 307)
    assert "/login" in r.headers["location"]


def test_login_page_served_without_auth():
    c = TestClient(_app(_auth_settings()))
    r = c.get("/login")
    assert r.status_code == 200
    assert "password" in r.text.lower()


def test_login_wrong_password_rejected():
    c = TestClient(_app(_auth_settings()), follow_redirects=False)
    r = c.post("/login", data={"password": "nope"})
    # stays unauthenticated (re-render with error or 401, NOT a redirect to /)
    assert r.status_code in (200, 401, 403)
    # and we still cannot reach protected content
    assert c.get("/api/info").status_code == 401


def test_login_then_access_then_logout():
    c = TestClient(_app(_auth_settings()), follow_redirects=False)
    r = c.post("/login", data={"password": "s3cret-pw"})
    assert r.status_code in (302, 303)
    # authenticated now
    assert c.get("/api/info").status_code == 200
    assert c.get("/").status_code == 200
    # logout drops it
    c.post("/logout")
    assert c.get("/api/info").status_code == 401


def test_login_open_redirect_guard():
    c = TestClient(_app(_auth_settings()), follow_redirects=False)
    for evil in ["//evil.com", "https://evil.com", "http:/evil", "/\\evil.com"]:
        r = c.post(f"/login?next={evil}", data={"password": "s3cret-pw"})
        loc = r.headers.get("location", "/")
        assert loc.startswith("/") and not loc.startswith("//"), f"open redirect via {evil}: {loc}"
        c.post("/logout")


def test_login_next_local_path_honored():
    c = TestClient(_app(_auth_settings()), follow_redirects=False)
    r = c.post("/login?next=/api/info", data={"password": "s3cret-pw"})
    assert r.headers["location"] == "/api/info"


def test_auth_disabled_is_passthrough():
    # auth_enabled False -> no gate, no /login route added, current behavior intact.
    app = _app(Settings(auth_enabled=False, rate_limit_enabled=False))
    c = TestClient(app)
    assert c.get("/api/info").status_code == 200
    assert c.get("/").status_code == 200


# ── SSE pass-through (middleware must not buffer/break streaming) ──────────────

def test_sse_streams_through_auth_and_headers():
    c = TestClient(_app(_auth_settings()))
    c.post("/login", data={"password": "s3cret-pw"})
    r = c.get("/api/sse")
    assert r.status_code == 200
    assert "chunk0" in r.text and "chunk2" in r.text
    assert r.headers["content-type"].startswith("text/event-stream")


# ── Security headers ──────────────────────────────────────────────────────────

def test_security_headers_present():
    c = TestClient(_app(_auth_settings()))
    r = c.get("/login")  # exempt path still gets headers
    assert "content-security-policy" in {k.lower() for k in r.headers}
    assert r.headers.get("x-content-type-options") == "nosniff"
    csp = r.headers["content-security-policy"]
    assert "default-src 'self'" in csp
    assert "frame-ancestors 'none'" in csp


def test_security_headers_can_disable():
    c = TestClient(_app(_auth_settings(security_headers_enabled=False)))
    r = c.get("/login")
    assert "content-security-policy" not in {k.lower() for k in r.headers}


# ── Rate limiter ───────────────────────────────────────────────────────────────

def test_token_bucket_allows_burst_then_denies():
    # burst=2, no refill within the test window (per_min=1 -> 1 token / 60s)
    lim = TokenBucketLimiter(per_min=1, burst=2)
    ok1, _ = lim.allow("ip1")
    ok2, _ = lim.allow("ip1")
    ok3, retry = lim.allow("ip1")
    assert ok1 and ok2 and not ok3
    assert retry > 0  # Retry-After hint
    # a different IP has its own bucket
    ok_other, _ = lim.allow("ip2")
    assert ok_other


def test_rate_limit_middleware_429_and_health_exempt():
    c = TestClient(_app(_auth_settings(rate_limit_enabled=True, rate_limit_per_min=1, rate_limit_burst=2)))
    # health is exempt -> never 429 even when hammered
    for _ in range(6):
        assert c.get("/api/health").status_code == 200
    # /login (unauthenticated, but rate-limited): burst 2 then 429
    codes = [c.get("/login").status_code for _ in range(4)]
    assert 429 in codes
    r429 = next(r for r in (c.get("/login") for _ in range(4)) if r.status_code == 429)
    assert "retry-after" in {k.lower() for k in r429.headers}


# ── Compare error sanitizer ─────────────────────────────────────────────────────

def _ans(model, err):
    return ModelAnswer(model=model, answer="" if err else "ok", usage=None,
                       latency_ms=1, cost_usd=None, error=err)


def test_sanitize_compare_errors_on():
    answers = [_ans("m1", "AuthenticationError: credit balance too low for org_xyz"),
               _ans("m2", None)]
    out = sanitize_compare_errors(answers, enabled=True)
    assert out[0].error is not None
    assert "credit balance" not in out[0].error
    assert "org_xyz" not in out[0].error
    assert out[1].error is None  # successful answer untouched


def test_sanitize_compare_errors_off_keeps_detail():
    answers = [_ans("m1", "AuthenticationError: credit balance too low")]
    out = sanitize_compare_errors(answers, enabled=False)
    assert "credit balance too low" in out[0].error


# ── Fail-loud config validation ────────────────────────────────────────────────

def test_install_security_requires_secret_when_auth_on():
    app = FastAPI()
    with pytest.raises(RuntimeError):
        install_security(app, Settings(auth_enabled=True, session_secret="", shared_password_hash=""))


def test_event_loop_available():
    # guard: pytest-asyncio config sane (other suites rely on it)
    assert asyncio.get_event_loop_policy() is not None


# ── _safe_next open-redirect guard (control/whitespace, Rule-D LOW) ────────────

def test_safe_next_rejects_control_whitespace_and_scheme_relative():
    for evil in ["/\t//evil.com", "/\n//evil.com", "/\r//evil.com", "/ //evil.com",
                 "//evil.com", "/\\evil.com", "\t/x", "http://evil"]:
        assert _safe_next(evil) == "/", f"should reject: {evil!r}"
    assert _safe_next("/api/info") == "/api/info"
    assert _safe_next("/") == "/"
    assert _safe_next(None) == "/"


# ── Login brute-force throttle (Rule-D MEDIUM) ─────────────────────────────────

def test_login_throttle_locks_after_failures_and_success_clears():
    t = LoginThrottle(max_fails=3, base_lockout_s=30.0)
    t.record_failure("ip")
    t.record_failure("ip")
    assert t.check("ip")[0] is True            # 2 fails -> not yet locked
    t.record_failure("ip")                     # 3rd -> locked
    ok, retry = t.check("ip")
    assert ok is False and retry > 0
    assert t.check("other")[0] is True         # per-IP isolation
    t.record_success("ip")                     # success clears the lock
    assert t.check("ip")[0] is True


def test_login_endpoint_429_after_repeated_failures():
    c = TestClient(_app(_auth_settings()), follow_redirects=False)  # rate-limit off here
    codes = [c.post("/login", data={"password": "nope"}).status_code for _ in range(8)]
    assert 401 in codes  # early failures are normal rejects
    assert 429 in codes  # after max_fails the IP is locked out
    # a correct password while locked is still refused (throttle precedes verify)
    assert c.post("/login", data={"password": "s3cret-pw"}).status_code == 429
