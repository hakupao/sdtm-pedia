"""Phase 3 sharing — shared-password login gate + hardening (DEPLOY_PLAN §3).

Everything here is OFF unless explicitly enabled in settings, so importing/wiring it is a
no-op for the current localhost service. At go-live (after IT signoff) the service-dir
.env flips auth_enabled / rate_limit_enabled / sanitize_errors on together.

Design constraints:
- The chat UI streams via SSE (StreamingResponse). All custom middleware here is therefore
  PURE ASGI (operating on scope/receive/send), NOT BaseHTTPMiddleware — the latter buffers
  the response body and breaks streaming. Starlette's built-in SessionMiddleware is also
  pure ASGI, so the whole stack is streaming-safe.
- Plain HTTP over the LAN (no TLS, §1): the session cookie cannot be Secure (it would never
  be sent) — HttpOnly + SameSite=Lax only. The shared password and cookie travel in
  cleartext on the LAN; this is the accepted residual risk of the §1 "shared password"
  decision (mitigation path = VPN / TLS / Cloudflare Tunnel, §6 roadmap).
"""
from __future__ import annotations

import hashlib
import html
import math
import os
import secrets
import time
from urllib.parse import quote

import structlog
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

log = structlog.get_logger()

# ── Password hashing (scrypt, stdlib — no new dependency) ───────────────────
# Single shared password, not a user table; scrypt with these fixed params is ample.
# Format stored in .env: "<salt_hex>$<hash_hex>". Changing params invalidates old hashes
# (just regenerate with scripts/gen_password_hash.py).
_SCRYPT = {"n": 2**14, "r": 8, "p": 1, "maxmem": 2**26, "dklen": 32}


def hash_password(password: str) -> str:
    salt = os.urandom(16)
    dk = hashlib.scrypt(password.encode("utf-8"), salt=salt, **_SCRYPT)
    return f"{salt.hex()}${dk.hex()}"


def verify_password(password: str, stored: str) -> bool:
    """Constant-time verify against a "salt_hex$hash_hex" string. Any malformed stored
    value returns False (never raises)."""
    try:
        salt_hex, hash_hex = stored.split("$", 1)
        if not salt_hex or not hash_hex:
            return False
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(hash_hex)
        dk = hashlib.scrypt(password.encode("utf-8"), salt=salt, **_SCRYPT)
        return secrets.compare_digest(dk, expected)
    except (ValueError, AttributeError):
        return False


# ── Helpers ─────────────────────────────────────────────────────────────────

def _client_ip(scope, trust_forwarded: bool) -> str:
    if trust_forwarded:
        for k, v in scope.get("headers", []):
            if k == b"x-forwarded-for":
                return v.decode("latin1").split(",")[0].strip() or "unknown"
    client = scope.get("client")
    return client[0] if client else "unknown"


def _safe_next(raw: str | None) -> str:
    """Open-redirect guard: only allow a local absolute path. Reject scheme-relative
    (//host), backslash tricks (/\\host), and any control/whitespace char — browsers strip a
    leading TAB/LF/CR/space before parsing, so '/\\t//evil' or '/ //evil' would otherwise be
    read as scheme-relative -> external. Defense-in-depth even though Starlette percent-quotes
    the Location header; the function now does what its contract says regardless of downstream."""
    if not raw or not raw.startswith("/"):
        return "/"
    if raw.startswith("//") or raw.startswith("/\\"):
        return "/"
    if any(ch < " " or ch == "\x7f" for ch in raw):  # any control char (covers TAB/LF/CR)
        return "/"
    if len(raw) >= 2 and raw[1] == " ":  # leading space right after the first '/'
        return "/"
    return raw


# ── Security headers (pure ASGI; streaming-safe) ────────────────────────────
# Strict CSP: the chat UI loads only same-origin assets (vendored marked/dompurify/
# highlight + app.js) — no inline scripts, no external origins. 'unsafe-inline' is granted
# to styles only (highlight theme + the minimal inline login-page style). This is
# defense-in-depth atop DOMPurify (which already strips active content from model output).
_CSP = (
    "default-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'; "
    "object-src 'none'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; "
    "script-src 'self'; connect-src 'self'"
)


class SecurityHeadersMiddleware:
    def __init__(self, app):
        self.app = app
        self._headers = [
            (b"content-security-policy", _CSP.encode("latin1")),
            (b"x-content-type-options", b"nosniff"),
            (b"x-frame-options", b"DENY"),
            (b"referrer-policy", b"no-referrer"),
        ]

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        async def send_wrapper(message):
            if message["type"] == "http.response.start":
                headers = message.setdefault("headers", [])
                present = {k.lower() for k, _ in headers}
                for k, v in self._headers:
                    if k not in present:
                        headers.append((k, v))
            await send(message)

        return await self.app(scope, receive, send_wrapper)


# ── Rate limiting (hand-rolled per-IP token bucket; pure ASGI) ──────────────

class TokenBucketLimiter:
    """In-memory per-key token bucket. Single-process / single-event-loop (§1): there is no
    await between read and write of a bucket, so the asyncio event loop serializes access —
    no lock needed. `allow` returns (ok, retry_after_seconds)."""

    def __init__(self, per_min: int, burst: int):
        self.rate = per_min / 60.0  # tokens per second
        self.burst = max(1, burst)
        self._buckets: dict[str, tuple[float, float]] = {}
        self._calls = 0

    def allow(self, key: str) -> tuple[bool, float]:
        now = time.monotonic()
        tokens, last = self._buckets.get(key, (float(self.burst), now))
        tokens = min(self.burst, tokens + (now - last) * self.rate)
        self._maybe_prune(now)
        if tokens >= 1.0:
            self._buckets[key] = (tokens - 1.0, now)
            return True, 0.0
        self._buckets[key] = (tokens, now)
        retry = (1.0 - tokens) / self.rate if self.rate > 0 else 60.0
        return False, retry

    def _maybe_prune(self, now: float) -> None:
        # Bound memory: every 1000 calls, drop buckets idle long enough to have refilled
        # fully (they're indistinguishable from a fresh key, so dropping them is lossless).
        self._calls += 1
        if self._calls % 1000:
            return
        idle = self.burst / self.rate if self.rate > 0 else 3600.0
        self._buckets = {
            k: (t, ts) for k, (t, ts) in self._buckets.items() if now - ts < idle
        }


class RateLimitMiddleware:
    # 静态壳子整体豁免: 前端拆成 ES 模块后, 冷加载一次 `/` 就是 ~16 个请求 (`/` + style.css
    # + app.js + 7 个 `/static/js/*.js` + vendor), 远超 BURST=10, 于是每次刷新都有几个模块
    # 随机吃 429, 页面起不来 —— 而这些是一次页面加载的固定开销, 不是攻击面。静态壳子按设计
    # 发 no-cache (必须回源校验), 缓存并不能把请求数压下去。真正要挡的 `/api/*` 一个不放。
    def __init__(self, app, *, limiter: TokenBucketLimiter, trust_forwarded: bool = False,
                 exempt: tuple[str, ...] = ("/api/health", "/"),
                 exempt_prefixes: tuple[str, ...] = ("/static/",)):
        self.app = app
        self.limiter = limiter
        self.trust_forwarded = trust_forwarded
        self.exempt = set(exempt)
        self.exempt_prefixes = tuple(exempt_prefixes)

    def _is_exempt(self, path: str) -> bool:
        return path in self.exempt or path.startswith(self.exempt_prefixes)

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http" or self._is_exempt(scope["path"]):
            return await self.app(scope, receive, send)
        ip = _client_ip(scope, self.trust_forwarded)
        ok, retry = self.limiter.allow(ip)
        if ok:
            return await self.app(scope, receive, send)
        resp = PlainTextResponse(
            "Too Many Requests", status_code=429,
            headers={"Retry-After": str(int(math.ceil(retry)))},
        )
        return await resp(scope, receive, send)


# ── Auth gate (pure ASGI; reads scope["session"] set by SessionMiddleware) ──

class AuthGateMiddleware:
    def __init__(self, app, *, exempt: tuple[str, ...] = ("/api/health", "/login", "/logout")):
        self.app = app
        self.exempt = set(exempt)

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http" or scope["path"] in self.exempt:
            return await self.app(scope, receive, send)
        session = scope.get("session") or {}
        if session.get("auth") is True:
            return await self.app(scope, receive, send)
        if scope["path"].startswith("/api/"):
            resp = JSONResponse({"detail": "authentication required"}, status_code=401)
        else:
            nxt = quote(scope["path"], safe="/")
            resp = RedirectResponse(url=f"/login?next={nxt}", status_code=302)
        return await resp(scope, receive, send)


# ── Login brute-force throttle (failure-based, per-IP) ──────────────────────

class LoginThrottle:
    """Per-IP lockout that counts only FAILED logins, independent of the general request
    rate limit. Legitimate users (correct password) are never penalized; after `max_fails`
    consecutive failures an IP is locked out with exponential backoff. This protects the
    single shared secret (the whole security boundary) against online guessing far more
    tightly than the generous 30/min request limit would. Same single-event-loop, no-lock
    model as TokenBucketLimiter."""

    def __init__(self, max_fails: int = 5, base_lockout_s: float = 30.0,
                 max_lockout_s: float = 3600.0):
        self.max_fails = max_fails
        self.base = base_lockout_s
        self.cap = max_lockout_s
        self._state: dict[str, tuple[int, float]] = {}  # ip -> (consecutive_fails, locked_until)
        self._calls = 0

    def check(self, key: str) -> tuple[bool, float]:
        _, until = self._state.get(key, (0, 0.0))
        now = time.monotonic()
        return (False, until - now) if until > now else (True, 0.0)

    def record_failure(self, key: str) -> None:
        now = time.monotonic()
        fails = self._state.get(key, (0, 0.0))[0] + 1
        until = now + min(self.cap, self.base * (2 ** (fails - self.max_fails))) \
            if fails >= self.max_fails else 0.0
        self._state[key] = (fails, until)
        self._maybe_prune(now)

    def record_success(self, key: str) -> None:
        self._state.pop(key, None)

    def _maybe_prune(self, now: float) -> None:
        # Bound memory: every 1000 calls drop entries not currently locked (an unlocked
        # entry is equivalent to a fresh key — dropping it just resets a benign counter).
        self._calls += 1
        if self._calls % 1000:
            return
        self._state = {k: v for k, v in self._state.items() if v[1] > now}


# ── Login routes ────────────────────────────────────────────────────────────

_LOGIN_PAGE = """<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SDTM 知识库助手 · 登录</title>
<style>
  body {{ font-family: -apple-system, "PingFang SC", sans-serif; background: #f7f7f8;
         display: flex; min-height: 100vh; margin: 0; align-items: center; justify-content: center; }}
  form {{ background: #fff; padding: 32px; border-radius: 12px; border: 1px solid #e5e5e5;
          width: 320px; display: flex; flex-direction: column; gap: 14px; }}
  h1 {{ font-size: 17px; margin: 0 0 4px; color: #333; }}
  input {{ padding: 12px; border: 1px solid #d0d0d0; border-radius: 8px; font-size: 15px; }}
  button {{ padding: 12px; border: none; border-radius: 8px; background: #19c37d; color: #fff;
            font-size: 15px; cursor: pointer; }}
  .err {{ color: #c00; font-size: 13px; margin: 0; }}
</style></head><body>
<form method="post" action="/login?next={next_attr}">
  <h1>SDTM 知识库助手</h1>
  {error_block}
  <input type="password" name="password" placeholder="访问口令" autofocus required>
  <button type="submit">登录</button>
</form></body></html>"""


def _render_login(next_raw: str | None, error: bool = False) -> HTMLResponse:
    next_attr = html.escape(_safe_next(next_raw), quote=True)
    error_block = '<p class="err">口令错误，请重试。</p>' if error else ""
    page = _LOGIN_PAGE.format(next_attr=next_attr, error_block=error_block)
    status = 401 if error else 200
    return HTMLResponse(page, status_code=status)


def build_auth_router(settings) -> APIRouter:
    router = APIRouter()
    throttle = LoginThrottle()

    @router.get("/login")
    def login_form(request: Request):
        if request.session.get("auth") is True:
            return RedirectResponse(_safe_next(request.query_params.get("next")), status_code=302)
        return _render_login(request.query_params.get("next"))

    @router.post("/login")
    def login_submit(request: Request, password: str = Form(...)):
        ip = request.client.host if request.client else "unknown"
        ok, retry = throttle.check(ip)
        if not ok:  # locked out after repeated failures (brute-force guard)
            log.warning("login_throttled", ip=ip, retry_s=round(retry))
            return PlainTextResponse(
                "Too many failed attempts. Try again later.", status_code=429,
                headers={"Retry-After": str(int(math.ceil(retry)))},
            )
        if verify_password(password, settings.shared_password_hash):
            throttle.record_success(ip)
            request.session["auth"] = True
            log.info("login_ok", ip=ip)
            return RedirectResponse(_safe_next(request.query_params.get("next")), status_code=303)
        throttle.record_failure(ip)
        log.warning("login_failed", ip=ip)
        return _render_login(request.query_params.get("next"), error=True)

    @router.post("/logout")
    def logout(request: Request):
        request.session.clear()
        return RedirectResponse("/login", status_code=303)

    return router


# ── Wiring ───────────────────────────────────────────────────────────────────

def install_security(app, settings) -> None:
    """Attach the phase-3 middleware stack to `app` per settings. Middleware added LAST is
    OUTERMOST, so adding in the order below yields the inbound call order:
        SecurityHeaders -> RateLimit -> Session -> AuthGate -> route
    (headers wrap every response incl. 429/401/302; rate-limit throttles before auth so
    login brute-force is capped; session is loaded before the gate reads it)."""
    if settings.auth_enabled:
        if not settings.session_secret or not settings.shared_password_hash:
            raise RuntimeError(
                "auth_enabled=True requires SDTM_RAG_SESSION_SECRET and "
                "SDTM_RAG_SHARED_PASSWORD_HASH to be set (fail-loud, no silent allow-all)."
            )
        app.include_router(build_auth_router(settings))
        app.add_middleware(AuthGateMiddleware)
        app.add_middleware(
            SessionMiddleware,
            secret_key=settings.session_secret,
            session_cookie=settings.session_cookie_name,
            max_age=settings.session_max_age_s,
            same_site="lax",
            https_only=False,  # plain HTTP over LAN (§1); cannot require Secure
        )

    if settings.rate_limit_enabled:
        limiter = TokenBucketLimiter(settings.rate_limit_per_min, settings.rate_limit_burst)
        app.add_middleware(
            RateLimitMiddleware,
            limiter=limiter,
            trust_forwarded=settings.rate_limit_trust_forwarded,
        )

    if settings.security_headers_enabled:
        app.add_middleware(SecurityHeadersMiddleware)


# ── Compare error sanitizer (SEC MED, deferred from phase 2) ────────────────

def sanitize_compare_errors(answers, enabled: bool):
    """When sharing (enabled), collapse each per-model error to a generic client-facing
    string — the full upstream text (e.g. 'credit balance too low') already went to the
    server log in compare._one_completion. No-op (returns as-is) on localhost dev so the
    operator keeps the useful diagnostic detail."""
    if not enabled:
        return answers
    for a in answers:
        if a.error:
            a.error = "Model temporarily unavailable."
    return answers
