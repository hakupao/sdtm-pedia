# 阶段 3 共享 — go-live runbook

> DEPLOY_PLAN.md §3。本目录的脚本/模板**已写好但未激活**。真正对外 (绑 `0.0.0.0` / pmset /
> 防火墙) 是 **go-live 动作**, 硬阻塞在 **IT 内网 IP/主机名 + 安全签字** (用户侧)。
> 工程件 (登录门/限流/错误脱敏/安全头) 已在 localhost 建好测好审过 (`PLAN_phase3_share.md`)。

## 残余风险 (须知)

公司网**纯 HTTP (无 TLS)**: 共享口令与 session cookie 明文过网、可嗅探; cookie 无法设
`Secure`。这是 §1 锁定「FastAPI 共享口令」的固有取舍。更强方案 (VPN / TLS / Cloudflare
Tunnel) 见 DEPLOY_PLAN §6 路线图。**口令请用长随机串** (限流 30/min 已挡暴力, 但口令熵是底线)。

## 前置 (用户侧, go-live 硬阻塞)

1. 找 IT 要**固定内网 IP/主机名** + **数据出境/公司网跑服务的安全签字**。
2. 确认公司是否允许自动登录 (LaunchAgent = 登录时自起)。若禁自动登录, 改用 LaunchDaemon
   (DEPLOY_PLAN §7 开放项)。

## go-live 步骤

```bash
cd branches/07_rag_kg/sdtm-rag

# 1. 预演 (不改任何文件)
./deploy/deploy.sh --dry-run

# 2. 真正同步到服务目录 + uv sync (首次会 seed 一个 ~/sdtm-rag-service/.env 模板)
./deploy/deploy.sh

# 3. 填服务目录 .env 的密钥 (chmod 600 已自动设)
#    - 4 个 provider key 从 repo .env 拷过去
#    - 生成登录口令哈希 + session secret:
python -m scripts.gen_password_hash    # 按提示输口令, 把 3 行粘进 ~/sdtm-rag-service/.env

# 4. 安装 go-live 版 api LaunchAgent (--host 0.0.0.0, 指服务目录)
cp deploy/com.sdtmrag.api.service.plist.template ~/Library/LaunchAgents/com.sdtmrag.api.plist
launchctl bootout  gui/$(id -u)/com.sdtmrag.api 2>/dev/null || true   # 卸旧 (bootout 异步, 失败重试)
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.sdtmrag.api.plist
#    8501 Streamlit Compare/Judge 的 plist 不动 (保持 127.0.0.1, 开发者私用)。

# 5. 验证: 登录门生效
curl -s http://127.0.0.1:8000/api/health            # {"status":"ok"} (health 豁免鉴权)
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8000/api/info   # 401 (未登录)
#    浏览器开 http://<主机名>:8000/ → 跳登录页 → 输口令 → 进聊天。

# 6. 不睡 + 断电自启 + 防火墙 (系统级, 需要时按公司策略)
sudo pmset -c sleep 0 disablesleep 1 autorestart 1      # 接电时不睡, 断电恢复自启
#    macOS 防火墙: 系统设置 → 网络 → 防火墙 → 允许 uvicorn/python 入站 (或关防火墙按 IT 指示)

# 7. 把 http://<主机名>:8000/ 发同事
```

## 发版更新 (上线后)

```bash
cd branches/07_rag_kg/sdtm-rag
./deploy/deploy.sh                                  # 同步最新代码/索引
launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api  # 重载服务
```

## 回滚

```bash
# 关对外, 退回 localhost: 用 repo 内原 plist 重新指回 127.0.0.1 (git 历史里), 或:
launchctl bootout gui/$(id -u)/com.sdtmrag.api
#  + 在 ~/sdtm-rag-service/.env 设 SDTM_RAG_AUTH_ENABLED=false 可临时关登录门 (调试用)。
```

## 文件清单

| 文件 | 作用 |
|------|------|
| `deploy.sh` | rsync repo→`~/sdtm-rag-service/` + `uv sync` (additive, 不碰 .env/.venv) |
| `.env.service.template` | 服务目录 .env 模板 (key/路径/auth/限流) |
| `com.sdtmrag.api.service.plist.template` | go-live api LaunchAgent (0.0.0.0:8000, 指服务目录) |
| `../scripts/gen_password_hash.py` | 生成口令 scrypt 哈希 + session secret |
