# 本地 Docker Compose 部署 — 修复/加固 + 实服 e2e 验证 (① 部署)

> 状态: **部署内容已就绪 + 实服 e2e 证过; 容器构建待用户在 Docker 主机上跑** (2026-06-15)
> 范围: H-2 本地优先 Docker Compose 自托管 (云部署 defer). 单用户/单租户 (--workers 1).

## 现状判定

部署产物 (Dockerfile + docker-compose.yml) Phase 1A (05-22) 已脚手架, 但**从未真正构建/跑过**
(H-2 部署 defer)。本轮: 修 + 加固 + **用实服 e2e 证明可部署内容真能跑** (本机无 docker, 容器构建
交用户在 Docker 主机执行)。

## 修复 / 加固

| 项 | 改动 | 原因 |
|----|------|------|
| **Dockerfile 构建 bug** | `pip install .` 前先 `COPY` 源码包 (server/scripts/ui/eval + pyproject + README) | 原顺序在只有 pyproject.toml 时 `pip install .` → setuptools 找不到声明的包, **构建必失败** |
| 镜像瘦身 | 新增 `.dockerignore` (排除 .venv/data/evidence/eval 产物/.git/.env) + 不再 `COPY . /app` | data/KB 运行时 bind-mount, 不烘进镜像; secrets 经 env_file 注入永不入镜像 |
| compose 健康检查 | api 加 `healthcheck` (curl /api/health, start_period 20s) + ui `depends_on: api: service_healthy` | ui 等 api 就绪 (RAG init ~0.7s) 才起, 避免 race |

## 验证

| 闸 | 方法 | 结果 |
|----|------|------|
| compose YAML | python yaml 解析 | valid, healthcheck/depends_on 正确 |
| Dockerfile COPY 路径 | 逐一 exist 检查 | 6/6 OK |
| 包可解析 | `import server.main, structured_lookup, scripts.spec_loader, ui.streamlit_app` | OK |
| **实服 e2e (核心)** | `.venv` uvicorn 起真服务 (非 TestClient) → /health /info /ask | **全过** ↓ |
| 容器构建 (`docker compose up --build`) | — | **本机无 docker, 待用户在 Docker 主机跑** |

### 实服 e2e 详情 (本机 uvicorn :8077, 生产配置)
- 启动: `chunks=4146 collection=sdtm_kb_v1 hybrid=True structured_lookup=True prompt_guardrail=True rag_init_s=0.72` — 三杠杆默认全开。
- `/api/health` → `{"status":"ok"}`; `/api/info` → 杠杆态全 true。
- `/api/ask` "What does RDOMAIN identify...": 真实准确答案 (two-character domain code of parent record(s)),
  **sources 含 `model/06_relationship_datasets.md`** (今天新建的 (d) 通道 gold 文件经实服检索命中);
  `model_used=deepseek-v4-pro` (Anthropic credits 耗尽 → Router 自动回退, 实证 fallback 生效)。
- **意义**: 首次以**实服** (非 eval harness/TestClient) 验证全栈 (检索杠杆 + (d) 通道 + 答题护栏 + fallback) 端到端可服务。

## 待用户执行 (容器构建, 本机无 docker)

在 Docker 主机 (Docker + Compose v2) 于 `branches/07_rag_kg/sdtm-rag/`:
```bash
docker compose up --build -d                 # api :8000 + ui :8501
curl -fsS http://localhost:8000/api/health   # 期望 {"status":"ok"}
# chroma: 复用挂入的 ./data/chroma (4146 chunks, 无需重 ingest) 或 docker compose exec api python scripts/ingest.py
```
注: OPENAI_API_KEY 硬必需 (embedding 无 fallback); DeepSeek 为当前实际主答; 详 README "Quick Start — Docker Compose"。

## 改动文件
- `Dockerfile` (构建顺序修复 + 瘦身) / `docker-compose.yml` (healthcheck + depends_on healthy) / `.dockerignore` (新增) / `README.md` (Docker 段重写 + env 必需性校正)
