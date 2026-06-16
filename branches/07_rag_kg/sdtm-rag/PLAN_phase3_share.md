# 阶段 3 共享 — 工程件实现计划 (build-to-localhost, 不翻对外)

> 状态: **工程件 DONE + 规则 D 三审 + 全 finding 已修** (2026-06-16) · Tier 2 · DEPLOY_PLAN §3 阶段 3
> 证据: `evidence/checkpoints/phase3_share_hardening.md` · retro `RETROSPECTIVE_phase3_share.md` · 进度 `_progress_phase3_share.json`. go-live 系统动作未做 (待 IT)。
> 范围决策 (用户 2026-06-16): **只做能在 localhost 完整测+审阅的工程件; 不真正翻 0.0.0.0 / pmset / 防火墙** (那些是 go-live 动作, 硬阻塞在 IT 内网 IP + 安全签字)。
> 三决策 (用户确认): 登录门 = **Starlette SessionMiddleware + 口令哈希存 .env**; 限流 = **手写内存版 per-IP 令牌桶**; 范围 = **localhost 可测 + 审阅**。

## 关键约束 / 设计基线

- **纯 HTTP over LAN (无 TLS)**: 共享口令 + session cookie 明文过网、可嗅探; cookie 不能设 `Secure` (只 HttpOnly + SameSite=Lax)。这是 §1 锁定「FastAPI 共享口令」的固有残余风险, 缓解路径 (VPN / Cloudflare Tunnel / TLS) 在 §6 路线图。**记入已知限制**。
- **SSE 流式**: chat UI 走 `/api/ask_stream` 的 `StreamingResponse`。所有自写中间件 **必须是纯 ASGI middleware** (不能用 `BaseHTTPMiddleware` — 它会缓冲/破坏流式)。Starlette 内置 `SessionMiddleware` 是纯 ASGI, 流式安全。
- **不扰动现存 localhost 服务**: 所有新开关默认 **OFF/安全** (`auth_enabled=False` / `rate_limit_enabled=False` / `sanitize_errors=False`)。launchd plist 无 `--reload`, 编辑文件不触发热重载; 现役 8000 不受影响, 直到手动 kickstart (本次不做)。安全响应头默认 ON (无害、好实践)。
- **fail-loud**: `auth_enabled=True` 但缺 `session_secret` 或 `shared_password_hash` → 启动即抛, 绝不静默放行。

## 文件改动清单

| 文件 | 改动 | 测试 |
|------|------|------|
| `server/config.py` | 加 auth/限流/sanitize/timeout 开关 + `kb_root`/`chroma_dir` env 覆盖 (解 §7 开放项) | — |
| `server/auth.py` (新) | `hash_password`/`verify_password` (scrypt, 无新依赖) + 3 个纯 ASGI 中间件 (SecurityHeaders / RateLimit / AuthGate) + 登录路由 + `install_security(app, settings)` | `test_auth_gate.py` / `test_rate_limit.py` / `test_security_headers.py` |
| `server/main.py` | 调 `install_security(app, settings)`; 重构出 `create_app(settings)` 工厂 | (经上面间接覆盖) |
| `server/router.py` | `/api/ask_compare` 错误串按 `sanitize_errors` 脱敏 + 外层 `asyncio.wait_for` 超时上限 | `test_error_sanitize.py` |
| `webchat/{app.js,index.html,style.css}` | Stop/Abort + 重试; topbar 读 `/api/info` default_model | 浏览器 smoke (Rule A 截图) |
| `deploy/deploy.sh` (新) | rsync app+data/chroma+kb → `~/sdtm-rag-service/` + `uv sync` (**写好不激活**) | `--dry-run` 验证 |
| `deploy/com.sdtmrag.api.service.plist.template` (新) | 服务目录版, `--host 0.0.0.0` + go-live 环境变量 (**模板, 不安装**) | — |
| `deploy/README.md` (新) | go-live runbook (含 IT 阻塞项 + pmset/防火墙手册步骤) | — |

## 任务序列 (TDD where practical)

1. **PLAN + 读 compare.py** ✅
2. **config.py**: 新开关 + kb/chroma 覆盖。
3. **auth.py (TDD)**: 先写 hash/verify + 中间件 + 登录路由的失败测试 → 实现 → 绿。重点测: 未登录 `/api/*`→401 / HTML→302; 已登录放行; `/api/health` 永远放行; 口令错→拒 + 常量时间; open-redirect 守卫 (`next` 仅本地路径); 令牌桶补充/拒绝/429+Retry-After; 安全头齐全 (CSP/nosniff/frame); **SSE 不被中间件破坏** (流式响应穿过 SecurityHeaders/RateLimit/AuthGate 仍逐帧)。
4. **main.py**: `create_app` 工厂 + `install_security`。
5. **router.py**: compare 错误脱敏 + 外层超时 (+ test_error_sanitize)。
6. **chat UI 延后项**: Stop/重试 + topbar /info。
7. **deploy/**: deploy.sh + plist 模板 + runbook (不激活)。
8. **验证**: 全量 pytest + ruff + `uvx pip-audit` + localhost 临时实例 smoke (auth on, 127.0.0.1:80xx, 不碰 8000)。
9. **规则 D 独立审阅** (Workflow, 异 subagent_type): security-reviewer (鉴权/会话/注入/明文风险) + code-reviewer (中间件顺序/令牌桶并发/正确性) + critic (回归: 不破 /api/ask·ask_stream·ask_compare·Streamlit·现有测试)。修 BLOCKER/HIGH。
10. **收口**: evidence checkpoint + RETROSPECTIVE + worklog/progress/commit。

## 验收标准

- auth on 时: 未登录只能见 `/login`; 错误口令被拒; 登录后 chat UI + /api/* 正常; SSE 流式不被破坏; logout 生效。
- 限流 on 时: 超速 → 429 + Retry-After; health 豁免。
- sanitize on 时: compare 单栏错误对客户端为通用串, 详情仍在服务日志。
- 安全头: 所有响应含 CSP + nosniff + frame-ancestors none。
- chat UI: 生成中可停止 + 出错可重试; topbar 显示真实 default_model。
- 全量 pytest 绿 (含新测) + ruff clean + pip-audit 结果归档。
- deploy.sh `--dry-run` 正确; plist 模板就绪但未安装。
- 规则 D 双/三审 SHIP, BLOCKER/HIGH 清零。
- **未做 (go-live, 待 IT)**: 真翻 0.0.0.0 / pmset / 防火墙 / 安装服务目录 plist / 激活 deploy.sh。
