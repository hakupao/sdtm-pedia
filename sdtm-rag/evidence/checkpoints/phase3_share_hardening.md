# 阶段 3 共享 — 工程件实现 + 硬化 证据

> 日期: 2026-06-16 · DEPLOY_PLAN §3 · Tier 2 · 计划 `PLAN_phase3_share.md`
> 范围 (用户决策): **build-to-localhost + 审阅, 不翻对外** (go-live 硬阻塞在 IT 内网 IP+签字)。
> 状态: **工程件 DONE + 规则 D 三审 + 全部 finding 已修**。go-live 系统动作未做 (待 IT)。

## 1. 交付物

| 项 | 文件 | 状态 |
|----|------|------|
| 登录门 (共享口令 + 签名 cookie) | `server/auth.py` (新) | DONE, 默认 OFF |
| per-IP 限流 (令牌桶) | `server/auth.py` `TokenBucketLimiter`/`RateLimitMiddleware` | DONE, 默认 OFF |
| 登录暴力锁 (失败计数, 指数退避) | `server/auth.py` `LoginThrottle` | DONE (规则 D MED 修) |
| 错误串脱敏 | `server/router.py` `sanitize_compare_errors` + `/api/ask_compare` | DONE, 默认 OFF |
| 外层 asyncio 超时上限 | `server/router.py` (`ask_compare` fan-out + `ask_stream` open) | DONE |
| 安全响应头 (CSP/nosniff/frame/referrer) | `server/auth.py` `SecurityHeadersMiddleware` | DONE, 默认 **ON** |
| config 开关 + kb/chroma 覆盖 (§7 开放项) | `server/config.py` | DONE |
| create_app 工厂 (单配置源) | `server/main.py` | DONE (规则 D MED 修) |
| chat UI: Stop/Abort + 重试 | `webchat/app.js` + `style.css` | DONE |
| chat UI: topbar 读 `/api/info` default_model | `webchat/app.js` | DONE |
| deploy.sh (rsync→服务目录 + uv sync) | `deploy/deploy.sh` | DONE (**写好不激活**) |
| go-live plist 模板 (0.0.0.0) + env 模板 + runbook | `deploy/*` | DONE (**模板, 未安装**) |
| 口令哈希 CLI | `scripts/gen_password_hash.py` | DONE |
| pip-audit | `evidence/checkpoints/phase3_share_pip_audit.txt` | DONE (修 starlette CVE) |

**关键设计基线**:
- 所有自写中间件 = **纯 ASGI** (非 BaseHTTPMiddleware) → 不破坏 SSE 流式。
- 全开关默认 OFF/安全 → 现役 launchd:8000 localhost 不受影响 (实测仍 healthy)。
- 纯 HTTP over LAN: cookie HttpOnly+SameSite=Lax (不能 Secure); 明文嗅探 = 已知残余风险 (缓解路径 §6)。

## 2. 验证

### 2.1 单测 (TDD)
- `scripts/tests/test_phase3_security.py` (新): 哈希往返/盐唯一/畸形拒绝, 认证门 (401//api, 302/HTML, health·login 豁免), 登录/登出, open-redirect 守卫 (含控制符/空白), SSE 穿透中间件, 安全头, 令牌桶, 登录暴力锁 429, 错误脱敏, fail-loud 配置。
- 全量 `pytest -q` **全绿** (含上面 + 既有 chat UI stream 测 + 检索/对比/校验全栈)。
- `ruff check` 新文件**全清**; `router.py` 新增 `except TimeoutError` 0 UP041 (规则 D LOW 修); 其余 router.py lint 为既有 (out of scope)。

### 2.2 活体 smoke (Rule A 独立样本, 临时实例 127.0.0.1:8033/8034, **不碰 launchd:8000**)
- v1 (8033, auth+限流): health=ok / info 无 cookie=401 / `GET /`=302→/login / GET /login=200+密码框+CSP+nosniff+X-Frame-Options / 错口令=401 / 对口令=303 (`next` 被尊重) / info 带 cookie=200 / **SSE 真 DeepSeek 621 token 帧穿过全中间件, 0 error** (纯 ASGI 不破流式实证)。
- v2 (8034, 修后含 LoginThrottle + create_app 重构): **boot health=ok** (证 create_app+lifespan `s=app.state.settings` 修生效) / info=401 / 对口令=303+info 200+logout 303 / **错口令×7 = 401×5 → 429×2** (暴力锁实证) / **锁定中对口令仍=429** (throttle 先于 verify)。
- 两次 smoke 后 launchd:8000 `/api/health`=ok (现役未受扰)。

### 2.3 pip-audit
- BEFORE: 3 vulns (chromadb CVE-2026-45829; starlette CVE-2026-54282/54283)。
- ACTION: pin `starlette>=1.3.1` → 1.2.1→1.3.1 (fastapi→0.136.3), 全量 pytest 重过。
- AFTER: 仅 chromadb CVE-2026-45829 (无修复版本) → **ACCEPTED/MONITORED** (只读·进程内·登录门后·内网)。详 `phase3_share_pip_audit.txt`。

## 3. 规则 D 独立审阅 (Workflow, 3 lens, 异 subagent_type, 独立 context)

writer = 主 session; reviewers = `security-reviewer` / `code-reviewer` / `critic` (各自 fresh context)。三份 verdict 均 **FIX_RECOMMENDED, 0 BLOCKER / 0 HIGH**。security lens 对抗式探了 path-trick 绕过 / open-redirect 变体 / 暴力 / XFF 伪造 / CSP 覆盖, 确认无可利用绕过。

| # | sev | lens | 结论 | 处置 |
|---|-----|------|------|------|
| 1 | MED | sec | 登录无暴力锁 (30/min/IP 无限猜) | **修**: `LoginThrottle` 失败计数+指数退避; 活体实证 401×5→429 |
| 2 | MED | sec | session 7d 无短期上限, `ts` 写而不用 | **修**: TTL→12h (itsdangerous 服务端强制); 删死字段 `ts`; 文档化 secret 轮换=全局撤销 |
| 3 | MED | code+critic | create_app(app_settings) 与 lifespan 全局 settings 分裂 | **修**: `state.settings=app_settings` + lifespan 读 `app.state.settings`; 签名 `None`+`or settings` 避免 import 期捕获 |
| 4 | LOW | sec | `_safe_next` 控制符/空白可过 (被 Starlette quote 中和) | **修**: 拒控制符 + 首位空白; 函数符合其契约 |
| 5 | LOW | critic | 新增 2 处 UP041 (`except asyncio.TimeoutError`) | **修**: → `except TimeoutError` |
| 6 | LOW | critic | deploy 模板硬编码 /Users/bojiangzhang 路径 | **修**: 模板用 `__SERVICE_DIR__` 占位, deploy.sh seed 时 sed 替换为 $DEST |
| 7 | LOW | critic | deploy.sh --dry-run 无 -v 不显变更 | **修**: dry-run 加 `-v --itemize-changes` |
| 8 | MED | critic | Tier-2 证据/retro/progress 缺 | **修**: 本文件 + pip_audit.txt + RETROSPECTIVE_phase3_share.md + _progress.json |

修后全部 finding 闭环; 全量 pytest + ruff 重过 + 活体 v2 smoke 重证。

## 4. 未做 (go-live, 待用户侧 IT)
真翻 `0.0.0.0` / `pmset` 禁睡 / macOS 防火墙 / 安装服务目录 plist / 激活 deploy.sh — 全是 go-live 系统动作, 硬阻塞在 **IT 内网 IP/主机名 + 安全签字**。步骤已写进 `deploy/README.md` runbook。
