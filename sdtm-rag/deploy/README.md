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
cd sdtm-rag

# 1. 预演 (不改任何文件)
./deploy/deploy.sh --dry-run

# 2. 真正同步到服务目录 + uv sync (首次会 seed 一个 ~/MyProject/sdtm-rag-service/.env 模板)
./deploy/deploy.sh

# 3. 填服务目录 .env 的密钥 (chmod 600 已自动设)
#    - 4 个 provider key 从 repo .env 拷过去
#    - 生成登录口令哈希 + session secret:
python -m scripts.gen_password_hash    # 按提示输口令, 把 3 行粘进 ~/MyProject/sdtm-rag-service/.env

# 4. 安装 go-live 版 api LaunchAgent (--host 0.0.0.0, 指服务目录)
cp deploy/com.sdtmrag.api.service.plist.template ~/Library/LaunchAgents/com.sdtmrag.api.plist
launchctl bootout  gui/$(id -u)/com.sdtmrag.api 2>/dev/null || true   # 卸旧 (bootout 异步, 失败重试)
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.sdtmrag.api.plist
#    8501 Streamlit Compare/Judge 的 plist 不动 (保持 127.0.0.1, 开发者私用)。

# 5. 验证: 服务真的起来了 (不是崩溃重启循环)
launchctl list | grep com.sdtmrag.api                # 第 2 列 last-exit-status 必须是 0
#    非 0 → 看 logs/api.launchd.log。最常见死因: chroma 里存的 source 是**构建树**的
#    绝对路径, 而 SDTM_RAG_KB_ROOT 指到了服务目录 → S1 的 VI section 映射建不出来 →
#    lifespan 预热 raise → 启动失败 (KeepAlive 会每 10s 重试一次, 端口始终拒连)。
#    解法: 在服务目录重灌索引 (.venv/bin/python -m scripts.ingest), 别只 rsync data/chroma。
#    这条闸是有意的: 同样的错配在旧版本下会静默退化成纯 cosine, 服务照常出答案。

# 5b. 验证: 登录门生效
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
cd sdtm-rag
./deploy/deploy.sh                                  # 同步最新代码/索引
launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api  # 重载服务
```

### ⚠ 改了 webchat 前端就要通知同事强刷一次

改动落在 `webchat/` (index.html / app.js / style.css) 时, **重载服务不等于同事看得到**。
发完版在群里说一句: **访问页面后按 `Cmd+Shift+R` (Win: `Ctrl+F5`) 强刷一次**。

原因: 服务端已给 `/` 与 `/static/*` 发 `Cache-Control: no-cache` (每次回源校验), 但那**只对
修复之后才存进浏览器的缓存条目生效**。在此之前存下的条目仍按当初编造的启发式新鲜期
(约为 Last-Modified age 的 10%, 实际观察到 **≈3 天**) 存活 —— 这段时间里浏览器**连问都不会问**
服务器, 页面也不会给任何提示。

实测过的症状 (2026-09-02): 服务器已在发新文件, 浏览器执行的却是旧 app.js, `performance` 里
HTML 与 app.js 的 `transferSize` 双双为 0 (零网络)。表现是**新加的控件整排消失**, 看起来像
"新功能没上线"而不是"浏览器没去拿新文件" —— 不知道这条的人会去查后端。强刷一次即恢复。

回归闸: `scripts/tests/test_webchat_cache_headers.py` (响应头) 随全量常驻;
`scripts/tests/test_webchat_cache_browser.py` (真浏览器) 默认 skip, **改了 `webchat/` 后、
发版前手动跑一次**:

```bash
uv pip install --python .venv/bin/python playwright   # 只增不删; 别用 uv sync --extra,
                                                      # 它会按 lock 卸掉 boto3/pytest 等
.venv/bin/python -m pytest scripts/tests/test_webchat_cache_browser.py
```

为什么不常驻: 能让它变红的**代码回归** (有人把 `Cache-Control` 拿掉) 已被常驻的响应头闸抓住;
它的独有价值是抓**浏览器侧行为变了** (将来前面加反代/CDN、Chrome 缓存策略变动) —— 那类事件与
本仓的 commit 无关, 所以按时机跑, 不按 commit 跑。

## 回滚

```bash
# 关对外, 退回 localhost: 用 repo 内原 plist 重新指回 127.0.0.1 (git 历史里), 或:
launchctl bootout gui/$(id -u)/com.sdtmrag.api
#  + 在 ~/MyProject/sdtm-rag-service/.env 设 SDTM_RAG_AUTH_ENABLED=false 可临时关登录门 (调试用)。
```

## Neo4j 探索层 (SP4; 本机自用, 不进 go-live)

> 状态: 本机探索层。localhost-only (7474 Browser / 7687 bolt), 与 8000 生产服务零耦合 —
> Neo4j 挂/停/没装, 生产答题不受影响 (spec 硬约束, Gate 3 有停机 byte-identical 证据)。

```bash
# 1. 安装 (formula 自带 openjdk)
brew install neo4j

# 2. 首次: 生成密码进 .env (chmod 600, 不进 git), 设初始密码
PW=$(openssl rand -base64 24)   # 追加 NEO4J_URI/NEO4J_USER/NEO4J_PASSWORD 到 sdtm-rag/.env
neo4j-admin dbms set-initial-password "$PW"

# 3. heap 上限 1g —— 实测结论 (2026-07-08, brew neo4j 2026.05.0):
#    NEO4J_server_memory_heap_max__size 这类 docker-entrypoint.sh 风格的环境变量
#    注入约定只在官方 Docker 镜像里实现, 本机原生/brew launcher 不认
#    (CALL dbms.listConfig()/SHOW SETTINGS 验证回 NULL, JVM 命令行也无 -Xmx)。
#    真正生效方式是直接改 neo4j.conf:
echo 'server.memory.heap.max_size=1g' >> "$(dirname $(readlink -f $(which neo4j)))/../conf/neo4j.conf"
#    (本机路径: /opt/homebrew/Cellar/neo4j/<version>/libexec/conf/neo4j.conf;
#     plist 模板 EnvironmentVariables 里仍保留同名 env 行, 但那只是意图声明, 不生效)

# 4. 装载 launchd 服务
cp deploy/com.sdtmrag.neo4j.plist.template ~/Library/LaunchAgents/com.sdtmrag.neo4j.plist
launchctl bootout  gui/$(id -u)/com.sdtmrag.neo4j 2>/dev/null || true
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.sdtmrag.neo4j.plist

# 5. 验证 (heap 1g + localhost-only)
source <(grep '^NEO4J_' .env)
cypher-shell -a "$NEO4J_URI" -u "$NEO4J_USER" -p "$NEO4J_PASSWORD" \
  "SHOW SETTINGS YIELD name, value WHERE name = 'server.memory.heap.max_size' RETURN name, value;"
  # 期望: "server.memory.heap.max_size", "1.00GiB"
lsof -nP -iTCP:7474 -iTCP:7687 -sTCP:LISTEN   # 期望两端口都绑 127.0.0.1

# 6. 全量导入 / 重建 (KB 冻结, 低频; 幂等可重跑; build_neo4j.py/reconcile_neo4j.py 见 SP4 Task 3-5)
cd <sdtm-rag 根> && .venv/bin/python scripts/build_neo4j.py
.venv/bin/python scripts/reconcile_neo4j.py    # 对账门, exit 0 才算导入成功

# 7. 起停 / 重启 / 卸载
launchctl kickstart -k gui/$(id -u)/com.sdtmrag.neo4j   # 重启
launchctl bootout gui/$(id -u)/com.sdtmrag.neo4j        # 停 (生产不受影响)

# 8. Browser 探索: open http://127.0.0.1:7474 (登录 neo4j/$NEO4J_PASSWORD)
#    精选查询库: ../docs/cypher_cookbook.md (SP4 Task 6)
```

## 文件清单

| 文件 | 作用 |
|------|------|
| `deploy.sh` | rsync repo→`~/MyProject/sdtm-rag-service/` + `uv sync` (additive, 不碰 .env/.venv) |
| `.env.service.template` | 服务目录 .env 模板 (key/路径/auth/限流) |
| `com.sdtmrag.api.service.plist.template` | go-live api LaunchAgent (0.0.0.0:8000, 指服务目录) |
| `../scripts/gen_password_hash.py` | 生成口令 scrypt 哈希 + session secret |
| `com.sdtmrag.neo4j.plist.template` | 本机 Neo4j 探索层 LaunchAgent (localhost-only 7474/7687, heap 1g 走 neo4j.conf) |
| `../docs/cypher_cookbook.md` | 精选 Cypher 查询库 (SP4 Task 6) |
