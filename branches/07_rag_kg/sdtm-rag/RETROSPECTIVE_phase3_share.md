# RETROSPECTIVE — 阶段 3 共享 工程件 (DEPLOY_PLAN §3)

> 2026-06-16 · Tier 2 · 范围: build-to-localhost + 审阅 (不翻对外, go-live 待 IT)。

## 1. 保留下来的做法 (what worked, keep doing)

- **先确认 3 个安全决策再动手** (范围/登录门机制/限流实现) — 一次 AskUserQuestion 批量问, 给推荐项让用户确认即可。安全敏感任务开头花 30 秒对齐, 省掉后面返工。
- **纯 ASGI 中间件而非 BaseHTTPMiddleware** — 项目有 SSE 流式端点, BaseHTTPMiddleware 会缓冲破流。开工前先识别这条约束, 写进 PLAN 基线, 避免了一个隐蔽的大坑。活体 621 token 帧穿透实证。
- **全开关默认 OFF / 安全头默认 ON** — 现役 localhost 服务零扰动, 新代码可在 localhost 完整测+审, 翻开关即 go-live。"建好但不激活"让高风险部署变成低风险增量。
- **TDD + 活体 smoke 双轨** — pytest (TestClient, 合成 SSE 路由证穿透) + 临时真实例 (真 DeepSeek 流式 + 登录流 + 暴力锁)。合成测覆盖逻辑分支, 活体证"中间件真不破真流式 / create_app+lifespan 真能 boot"。
- **规则 D 三 lens 异 subagent_type Workflow** — security / code-correctness / critic-regression 各自 fresh context。security lens 对抗式探绕过 (path-trick/open-redirect 变体/XFF), 比单审更狠; critic lens 抓到我自己漏的 Tier-2 证据缺口。writer≠reviewer 严格隔离。
- **pip-audit 当真做并据此行动** — 不是走过场: 真发现 starlette CVE 且修 (pin→re-lock→re-test), chromadb 无修则显式 triage 为 ACCEPTED/MONITORED 而非装看不见。

## 2. 必须补上的缺口 (gaps surfaced, fix next time / carry)

- **首版漏了登录暴力锁** — 我先只做了通用限流 (30/min), 没想到对"单一共享口令"而言 30/min/IP 仍是无限在线猜测。security lens 抓到。教训: **共享口令 = 整个安全边界, 失败侧节流要比正常流量严得多**, 下次设计认证一开始就分离"失败计数锁"与"通用限流"。
- **create_app 工厂"半契约"** — 我加了 `app_settings` 参数让安全栈可配, 但 lifespan 仍闭包全局 settings, 路由从 `app.state.settings` 读 → 自定义配置只生效一半 (split-brain)。两个 lens 都点名。教训: **工厂要么真正贯通单配置源 (state 设一次, 所有人读它), 要么别提供参数**, 别留"看着能配实则分裂"的陷阱。
- **新代码 lint 自检不彻底** — `except asyncio.TimeoutError` 在 py3.11+ 是 UP041, 我声称"新文件 clean"却漏了 router.py 新增行。教训: 改完跑 ruff 要覆盖**所有改动文件**, 不只新建文件。
- **`_safe_next` 文档与实现不符** — docstring 说拒 backslash/scheme-relative, 实现漏控制符/空白 (虽被 Starlette quote 中和)。教训: 安全守卫函数**让实现真满足其契约**, 别依赖下游某个行为兜底 (一次 upstream 行为变更就破)。
- **Tier-2 收尾物没在收尾前补齐** — evidence/retro/progress 是 critic lens 提醒才补。教训: PLAN 里写了"步骤8验证/步骤10收口"就该按序做, 别等审阅提醒。

## 3. 关键决策复盘

- **D1 登录门 = Starlette SessionMiddleware + scrypt 哈希 (vs 手写 HMAC / 明文)**: 选内置 SessionMiddleware (itsdangerous 已是传递依赖, 零新依赖, 久经考验) + scrypt (stdlib, 无依赖)。手写签名会自背攻击面。✅ 对; 副产物=session TTL/撤销受 SessionMiddleware 模型约束 (无服务端 store), 用短 TTL (12h) + secret 轮换缓解。
- **D2 限流/暴力锁 = 手写内存令牌桶 + 失败计数锁 (vs slowapi)**: 单机小团队, 手写无新依赖、pip-audit 面更小、契合单事件循环无锁模型。✅ 对; 多 worker (§6 搬云) 需换共享状态, 已注释标记。
- **D3 范围 = build-to-localhost 不翻对外**: 把高风险不可逆系统动作 (0.0.0.0/pmset/防火墙) 与可测可审的代码件分离, 后者本期做满+审满, 前者打包成 runbook 等 IT。✅ 对 — 让"部署"在没有 IT 签字时也能推进到"一键可上线"。
- **D4 pip-audit 发现 starlette CVE 选择升级而非记录忽略**: CVE 在认证层依赖的 web 框架, 有修复版。升级 (1.2.1→1.3.1, fastapi 连带→0.136.3) + 全量 retest 通过。✅ 对 — 近满分质量条下, 认证边界的依赖 CVE 该修就修, 不留给 go-live。
- **D5 纯 HTTP over LAN 残余风险显式承认而非假装解决**: 锁定方案 (FastAPI 共享口令) 本就明文过网, cookie 不能 Secure。不强行上 TLS (那是 §6 路线), 而是: 短 TTL + 强口令要求 (CLI 硬闸 <8 拒/<16 警) + 暴力锁 + runbook 写明缓解路径。**诚实标注残余风险, 给缓解阶梯**, 比假装零风险好。
