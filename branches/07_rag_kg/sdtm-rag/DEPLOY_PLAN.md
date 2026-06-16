# SDTM RAG 本地部署 + 多模型对比/裁判 — 需求 · 计划 · 落地方案

> 状态: **草案 v1**(2026-06-15 起草)
> 作用: 支撑后续逐阶段实施的主文档。每阶段完成后在 §3 勾选进度。
> 约定: 本文中文(工作文档);知识库内容仍英文。模型决策必须有 eval 数据支撑(规则 A)。

---

## 0. 背景与目标

**现状**
- RAG 服务 = FastAPI(`server/`) + ChromaDB(本地持久,`data/chroma`,4146 chunks @1536d) + BM25s(纯 CPU) + Streamlit UI(`ui/streamlit_app.py`)。
- 重 ML 全在云端:嵌入走 OpenAI `text-embedding-3-small`;生成走 litellm Router(default=Sonnet / hard=Opus / light=Haiku,fallback=deepseek-v4-pro)。
- 检索与生成在 `/api/ask` 中已干净分离(retrieve → format_context → build_messages → completion)。
- 硬件: Mac mini M4 基础款,10 核 CPU / 10 核 GPU / **16GB 统一内存** / 95GB 空闲盘;放公司、连公司网,可 24/7。

**本期目标**
1. 把服务在本机用 launchd 24/7 跑起来:**先 localhost 自用调优 → 再共享给同事**。
2. 新增「多模型对比」功能:**一个问题 → 3 个模型基于同一检索上下文并排作答**,提升对答案的信心、暴露分歧。
3. 在对比基础上加「第 4 个模型当裁判」:自动评出最佳答案 + 理由。

**非目标(本期明确不做)**
- 本地大模型推理(16GB 已两次崩溃验证扛不住;生成永远走云)。
- Neo4j 知识图谱(已 defer/close)。
- 公网对外(阶段 3 再单独处理,需 IT/安全签字)。

---

## 1. 全局锁定的设计决定

| 项 | 定为 | 理由 |
|---|------|------|
| 开发/源码位置 | repo 原地 `…/branches/07_rag_kg/sdtm-rag` | 调优在这,迭代快、相对路径现成 |
| 运行/服务位置 | **`~/sdtm-rag-service/`**(专用,阶段 3 启用) | 与活跃 git 树隔离,服务不被日常 git 操作搅乱 |
| knowledge_base | **复制进服务目录**(自包含) | 运行时注入 ROUTING.md+INDEX.md;复制后服务可整体独立/搬走 |
| 向量索引 | **复制现成 `data/chroma`,不重建** | 嵌入模型不变,DeepSeek 只换生成,旧索引照常有效 |
| 密钥 | 服务目录内 `.env`,`chmod 600`,不进 git | 权限最小 |
| 启动方式 | **LaunchAgent**(阶段 3 加自动登录) | 全程用户空间,不碰 root,最省心 |
| 端口/绑定 | API `8000` / UI `8501`;**阶段 0–2 绑 `127.0.0.1`**,阶段 3 才 `0.0.0.0` | 调优期 = 私人沙盒,零暴露 |
| 主力模型 | **默认 DeepSeek V4 Pro**(Anthropic credits 耗尽;用户 2026-06-15 定先用 DeepSeek);阶段 2 用 eval+对比再定是否充值上 Sonnet | 近满分标准,数据说话不拍脑袋 |
| Python 环境 | 服务目录内独立 `.venv`(`uv sync`) | 与 repo 互不干扰 |
| 发版动作 | `deploy.sh`(rsync repo→服务目录) | 有意识发版,不边改边漏 |

---

## 2. 功能需求:多模型对比 + 裁判

### 2.1 用户故事
- 我提一个问题 → 系统用 **3 个模型基于同一检索上下文** 各自作答,**三栏并排** → 三家一致我更有信心,三家分歧则提示需人工核。
- 我可开启「裁判」→ **第 4 个模型** 拿到「问题 + 同一 context + 3 份答案」→ 输出 **排名 + 每份点评 + 最佳**。

### 2.2 功能需求 (FR)
- **FR1** 检索只跑一次,3 个生成模型共用同一 context(公平对比的前提)。
- **FR2** 3 个模型**并行**调用(`asyncio.gather` + `litellm.acompletion`),总耗时 ≈ 最慢家。
- **FR3** 三栏并排:每栏 = 模型名 + 答案 + badge(延迟 / tokens / 估算成本)。
- **FR4** Sources 三家共用,只展示一次。
- **FR5** 裁判模式(开关):第 4 模型对 3 份**匿名**答案(A/B/C)评分 → 排名 + 点评 + 最佳;结果再映射回真实模型名展示。
- **FR6** 单模型模式保留(日常用);对比/裁判是可选开关。
- **FR7** **每个模型位置均可自定义**(对比 3 路 + 裁判 = 4 个槽):每个槽接受任意 litellm 模型串,`.env` 配默认值、UI sidebar 可临时覆盖。**本期不固定具体型号** —— 参考默认为 Anthropic 一路 + OpenAI 一路 + DeepSeek 一路 + 裁判一路,具体型号随时改。

### 2.3 非功能需求 (NFR)
- **NFR1 成本**:对比 = 3×;裁判再 +1×。~300 题/月下可忽略(全用也才几美元/月)。**默认日常单模型**,对比/裁判按需开。
- **NFR2 失败隔离**:某家超时/报错 → 其余两家照常出,该栏显示错误,不拖垮整请求。
- **NFR3 速率限制**:三家独立;429 各自 backoff(复用现有重试)。
- **NFR4 延迟**:生成并行 ≈ 最慢家;裁判串行在 3 家之后(多 1 跳)。
- **NFR5 可观测**:每模型记录 latency / tokens / cost / error 入日志。

### 2.4 数据流
```
question
  └─ rag.retrieve(...)            # ① 一次
       └─ format_context          # ②
            └─ build_messages     # ③(三家共用同一份 messages)
                 ├─► 并行 ┬ M1(Anthropic)  ─┐
                 │        ├ M2(OpenAI)      ─┤→ answers[ {model,answer,usage,latency,cost,error?} ]
                 │        └ M3(DeepSeek)    ─┘
                 └─►(可选)judge(question, context, answers[A/B/C 匿名])
                          → { ranking, best_model, per-answer comment }
  └─ UI: 三栏并排 + 共用 Sources + 裁判结论
```

### 2.5 API 契约(新增端点,复用现有检索)
- **`POST /api/ask_compare`**
  - 请求: `{ question, models:[str], top_k, domain?, file_type?, history?, judge?:{enabled:bool, model:str} }`
  - 响应:
    ```json
    {
      "sources": [ ... ],
      "answers": [
        {"model":"...", "answer":"...", "usage":{...}, "latency_ms":1234, "cost_usd":0.05, "error":null}
      ],
      "judge": {
        "ranking":[{"model":"...","rank":1,"comment":"..."}],
        "best_model":"...", "rationale":"..."
      }
    }
    ```
  - 复用 `rag.retrieve / format_context / build_messages`;仅生成步骤改为并行多模型 + 可选裁判。

### 2.6 裁判设计
- **匿名化**:把 3 份答案标为 A/B/C 喂给裁判,**隐藏模型品牌**,避免裁判偏向某家;展示时再映射回真实名。
- **裁判 prompt**:给「问题 + 同一 context + 3 份匿名答案」,要求对照 context 评 **准确性 / 完整性 / 接地性(是否只用 context、有无编造)**,输出可解析 JSON `{ranking, best, per-answer comment}`(用 structured output / JSON 模式)。
- **裁判模型**:默认 Opus(质量最高,当裁判最稳);可配。
- **定位**:裁判**是辅助参考,不是终判** —— 裁判本身也可能错,与项目「语义抽检」文化一致,关键决策仍以人工 + eval 为准。

### 2.7 UI(Streamlit)
- sidebar 加模式开关:**Single / Compare**(radio);Compare 下再有「Enable Judge」勾选。
- **每个模型槽可编辑**:sidebar 暴露对比 3 路 + 裁判共 4 个模型串输入框(预填 `.env` 默认值),用户随时改,不写死。
- Compare:`st.columns(3)`,每栏 header(模型)+ 答案 + caption(latency/tokens/cost);底部共用 Sources expander。
- Judge:答案区下方「Judge」块 = 最佳标记 + 排名表 + 每份点评。
- 顺手修文案:旧 "default=Sonnet" 标签更新为真实映射。

---

## 3. 部署四阶段(执行稿 + 进度)

> 阶段 0–2 全程 `127.0.0.1` 私有;对比/裁判功能在阶段 2 开发。每项做完打勾。

### 阶段 0 — 冒烟测试(repo 原地 · 手动 · localhost)
目标:先证明端到端能跑,最便宜地挖坑。
- [x] 我:查 `.env`(4 key 全 SET:ANTHROPIC/DEEPSEEK/OPENAI/COHERE,值未打印)— 2026-06-15
- [x] 我:`uv sync` 完成;`data/chroma` 索引确认 **4146 chunks**(ingested marker `total_chunks=4146`, `text-embedding-3-small`, 1536d)
- [x] 我:手动起 api(`uv run uvicorn server.main:app --host 127.0.0.1 --port 8000`)+ ui(`streamlit … --server.address 127.0.0.1 --server.port 8501 --server.headless true`);日志落 `logs/api_smoke.log` / `logs/ui_smoke.log`
- [x] 我:`curl /api/health` = `{"status":"ok"}`;`/api/info` = 4146 chunks + structured_lookup/hybrid(rrf)/guardrail 全 ON
- [x] 我(代跑端到端冒烟):`POST /api/ask`「AE/AETERM」答案接地正确(15 sources, AE/spec.md + assumptions.md),`model_used=deepseek-v4-pro` — **实测 Anthropic credits 耗尽→DeepSeek 自动回退**生效
- [ ] 你:开 `localhost:8501` 在浏览器问一题 + 试一次 Validation(key 已全齐,无需补)
- **验收**:health OK ✅、info 显示 4146 chunks ✅、问答有合理答案+引用 ✅(API 侧已证;UI 侧待你浏览器确认)。**坏了在这修。**

### 阶段 1 — 本机常驻(launchd · 仍 localhost)
目标:不用手动开;崩了自起、开机自启;仍只你能访问。
- [x] 我:写 2 个 LaunchAgent plist(`~/Library/LaunchAgents/com.sdtmrag.{api,ui}.plist`,绑 127.0.0.1,RunAtLoad+KeepAlive+ThrottleInterval 10,日志落 `logs/{api,ui}.launchd.log`,WorkingDirectory=sdtm-rag)— **直连 `.venv/bin/{uvicorn,streamlit}`,不走 `uv run`**:uv run 是父(uv)+子(server)两进程,launchd 只盯父进程,子进程崩了不会重启;直连后 launchd 直接盯真服务(PPID=1),崩溃即自起 — 2026-06-15
- [x] 我:`launchctl bootstrap gui/$(id -u)` 加载(坑:bootout 异步,需轮询确认卸载完 + 重试 bootstrap,否则 `Bootstrap failed: 5: I/O error`)
- [x] 我:默认模型切 DeepSeek(`.env` `SDTM_RAG_DEFAULT_MODEL=deepseek/deepseek-v4-pro`,主力+自重试 fallback)
- [ ] 你:(可选)重启电脑或重新登录验证自恢复(LaunchAgent = **登录时**自起;无人值守的开机自启属阶段 3 自动登录)
- **验收**:health OK ✅、`/api/info` default=deepseek + 4146 chunks ✅、kill 监听进程→launchd 自起(70991→71267 实证)✅、`localhost:8501` ok ✅。

### 阶段 2 — 调优 + 多模型对比/裁判开发(仍 localhost)★核心
目标:私有状态下打磨到满意,并**用数据定主力模型**。
实现 + 验证 + 双独立审阅(规则 D)证据 → `evidence/checkpoints/phase2_compare_judge.md`。
- [x] 我:实现 `/api/ask_compare`(§2.5)+ 并行三模型 + 裁判(§2.6)— `server/compare.py`+`cost.py`+`router.py`; 端到端实测 FR1/FR2/NFR2/FR3/FR5 全 PASS(2026-06-16)
- [x] 我:Streamlit 加 Single/Compare/Judge UI(§2.7)— `ui/streamlit_app.py`(模式开关 + 三栏 badge + 共用 Sources + 裁判区)
- [x] 我:改掉过时 UI 文案("default=Sonnet" → 真实映射 + /api/info 预填)
- [x] 我:双独立审阅(code-reviewer 并发/正确性 + security-reviewer 匿名/注入)均 SHIP, 8 项加固已落
- [x] 我:DeepSeek vs Sonnet `--judge` 全量对比(140 题, 同条件配对)— Sonnet 96.0% vs DeepSeek 93.6%(判官均值), Sonnet 9.7x 成本(绝对值小), 强在枚举题; 证据 `evidence/checkpoints/phase2_model_comparison.md`
- [x] 你+我:拍板主力模型 — **维持 DeepSeek-v4-pro 默认**(2026-06-16, 基于 140 题 eval + 抽检; Sonnet 留 hard 档/Compare 手动)。产出 `evidence/checkpoints/phase2_model_comparison.md`
- [ ] 你:(可选)用 Compare 在真实问题上肉眼对比;拿真数据集试 Validation
- **验收**:对比三栏正确 ✅、失败隔离生效 ✅、裁判输出可解析 ✅、eval 达标(DeepSeek 96.6% / Sonnet 97.8% 均 PASS)+ 主力已拍板 ✅ → **阶段 2 核心收口**;阶段 3 共享前补 SEC MED(错误串 sanitize)+ host/限流(见 model_comparison 同目录 compare_judge §4 延后项)。

### 阶段 3 — 共享(部署专用目录 + 对外 + 加锁)
> **状态: 工程件 DONE + 规则 D 三审 (2026-06-16, localhost)**;**go-live 仍待 IT 内网 IP/主机名 + 安全签字**。
> **已定决策**: ① 对外面 = **8000 的 ChatGPT 风格 chat UI**(已建成上线 localhost,见 `PLAN_chat_ui.md`);8501 Streamlit Compare/Judge **保持 localhost** 当开发者工具,不对外。② 登录门 = **FastAPI 共享口令**(登录表单 + 签名 session cookie 中间件,最轻、公司网内即可、无需额外服务/IT)。
> **本期工程件 (localhost 可测+审, 全开关默认 OFF)**: 登录门(`server/auth.py`)+ per-IP 限流 + 登录暴力锁(`LoginThrottle`)+ 错误脱敏 + 外层 asyncio 超时 + 安全头(CSP/nosniff/frame)+ chat UI Stop·重试·topbar 读 `/api/info` + `deploy/`(deploy.sh + 0.0.0.0 plist 模板 + env 模板 + runbook,**写好不激活**)+ `scripts/gen_password_hash.py` + pip-audit(**修 starlette CVE**,pin `starlette>=1.3.1`;chromadb CVE 无修待监控)。中间件全为**纯 ASGI**(不破 SSE,621 token 帧活体实证)。实现 `PLAN_phase3_share.md`,证据 `evidence/checkpoints/phase3_share_hardening.md`,retro `RETROSPECTIVE_phase3_share.md`。**go-live 系统动作(翻 0.0.0.0 / pmset / 防火墙 / 装服务目录 plist)未做**。

目标:同事稳定访问,且安全合规。
- [x] 我:写 `deploy.sh`(rsync app+data/chroma+kb→`~/sdtm-rag-service/`,`uv sync`)— DONE,`--dry-run` 验证;**未激活**
- [x] 我:go-live launchd 模板(`deploy/com.sdtmrag.api.service.plist.template`,指服务目录、**chat UI 绑 `0.0.0.0`**,8501 仍 127.0.0.1)— **模板写好,未安装**;实际安装+自动登录 = go-live(runbook)
- [x] 我:登录门 = **FastAPI 共享口令**(`server/auth.py`:Starlette SessionMiddleware + scrypt 哈希;覆盖 `GET /` + `/api/*`,health/login 豁免)— DONE,活体实测通过
- [x] 我:安全硬化:错误串 sanitize、per-IP 限流、asyncio 外层超时、pip-audit(修 starlette CVE);+ 延后 chat UI 项(Stop/Abort+重试、topbar 读 `/api/info`、CSP + `X-Content-Type-Options`)— DONE;**加固**:登录暴力锁 + session TTL 12h(规则 D)
- [ ] 我:`pmset` 禁睡眠+断电自启;macOS 防火墙放行 — **go-live 系统动作**,步骤已写进 `deploy/README.md`,未执行
- [ ] 你:找 IT 要**固定内网 IP/主机名** + **IT/安全签字**(公司网跑服务 + 数据出境)— **go-live 硬阻塞**
- [ ] 你:把地址发同事
- **验收**:同事访问 `http://<主机名>:8000`(chat UI)、登录、能用;重启自恢复。

---

## 4. 落地方案 / 实现拆解(开发用任务清单)

| 任务 | 文件 | 内容 | 依赖 |
|------|------|------|------|
| T1 | `server/config.py` | 加 `compare_models: list[str]`、`judge_model: str`、OpenAI 生成模型项 | — |
| T2 | `server/compare.py`(新) | async 并行调用 `litellm.acompletion`,逐家收集 answer/usage/latency/error;失败隔离 | T1 |
| T3 | `server/cost.py`(新) | 按 (model, usage) 估算 `cost_usd`,内置价格表(见 §8) | — |
| T4 | `server/compare.py` | 裁判函数:匿名化 A/B/C + 结构化 JSON 输出 + 映射回模型名 | T2 |
| T5 | `server/router.py` | 新增 `/api/ask_compare` 端点 + Pydantic 请求/响应模型;复用 retrieve/format/build | T2,T4 |
| T6 | `ui/streamlit_app.py` | Single/Compare/Judge 开关 + 三栏 + badge + 裁判区;修文案 | T5 |
| T7 | `eval/`(可选) | 复用对比逻辑做离线批量三模型对比,补充阶段 2 决策 | T2 |
| T8 | 部署脚本 | `deploy.sh` + 2 个 LaunchAgent plist 模板 | 阶段 1/3 |

---

## 5. 整体验收标准
- 一题 → 三栏三答案,**context 完全相同**,badge(延迟/token/成本)正确。
- 某家失败不影响其余两家(失败隔离)。
- 裁判输出**可解析**的排名 + 理由 + 最佳。
- launchd:进程被杀自起、开机自启。
- 阶段 2:eval 分数达你的标准 + Compare 抽查满意 → 定下主力模型。
- 阶段 3:同事可访问 + 登录门生效 + 重启自恢复。

---

## 6. 路线图(上线后继续展开)

| 方向 | 时机 | 做法 |
|------|------|------|
| 发版更新 | 每次 repo 调好 | 跑 `deploy.sh` 同步 → 服务重载 |
| 备份 | 常态 | 定期备份 `data/chroma` + `.env`(已有 chroma_backup 习惯) |
| 质量回归 | 改模型/prompt 后 | 重跑 `--judge` eval 守住分数 |
| 监控 | 想更省心 | 日志轮转 + 每日健康 ping |
| 远程访问 | 同事要出公司用 | 公司 VPN 或 Cloudflare Tunnel(IT 签字) |
| 界面升级 | 同事嫌简陋 | 美化 Streamlit,或 Astro 站直接调 API |
| 省成本 | 量涨 | 稳定 system prompt 开 prompt caching |
| 搬云/扩容 | 要更高可用 | 同套 `deploy.sh`+服务化平移到 $5–15/月 云主机(launchd→systemd) |

---

## 7. 待确认 / 开放问题
- [ ] **各模型槽的默认值**(对比 3 路 + 裁判)填什么 —— **全部可在 `.env`/UI 自定义,本期不决定、不阻塞开发**(先留参考默认占位即可)。
- [ ] **knowledge_base 路径**的确切 config 变量名(搭建阶段 0 时确认)。
- [x] **登录门方案** → **已定 (用户 2026-06-16): FastAPI 共享口令**(登录表单 + 签名 session cookie 中间件,加在 8000 chat UI;最轻、公司网内即可、无需 IT)。备选(反代 + SSO / Cloudflare Access)留待若 IT 有更高要求时再评。
- [ ] **自动登录 vs LaunchDaemon**(阶段 3;若公司禁自动登录则用 LaunchDaemon)。

---

## 8. 风险与对策
| 风险 | 对策 |
|------|------|
| DeepSeek 当主力质量未知 | 切换前必跑 eval(规则 A);Compare 肉眼复核;不达标退回 Sonnet/混合 |
| 对比/裁判成本 3–4× | 默认单模型,对比/裁判按需开;量小可忽略 |
| 数据出境 + 公司网跑服务 | 阶段 3 前过 IT/安全;必要时改 OpenRouter 代理换数据路径 |
| Mac mini 单点可用性 | 家用级可用性;搬云预案已留(设计可移植) |
| 裁判偏置 | 答案匿名 A/B/C;裁判定位为辅助参考非终判 |

---

## 9. 成本价格表(用于 badge / cost.py,2026-06)
| 模型 | 输入 $/1M | 输出 $/1M | 来源 |
|------|-----------|-----------|------|
| Claude Sonnet 4.6 | 3.00 | 15.00 | Anthropic(权威) |
| Claude Opus 4.7 | 5.00 | 25.00 | Anthropic(权威) |
| Claude Haiku 4.5 | 1.00 | 5.00 | Anthropic(权威) |
| DeepSeek V4 Pro | 0.435 | 0.87 | 官方 2026 永久降价 |
| (自定义/其他模型) | 见 `cost.py` 价格表 | | 未列出的模型 cost 显示 "—" |
| text-embedding-3-small | 0.02 | — | OpenAI(约值) |

> 模型槽可自定义(FR7),`cost.py` 维护一张可扩展价格表;表中没有的模型,badge 成本显示 "—" 而非报错。

> 实测每题 ≈ 15k 输入 / 0.5k 输出(top_k=15 + 整文件 system prompt 注入)。
