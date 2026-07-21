# Phase 1A.2 Prep — D-4 v2 修订 (bge-m3 主 + OpenAI 留接口暂不调)

> 実施: 2026-05-22 main session (1A.1 commit 3900b9e 后, 1A.2 启动前)
> 触発: ユーザー意思決定 2026-05-22 「OpenAI 留接口暂不使用, 只使用 DeepSeek V4 Pro」(D-3/D-4 同時 revision)
> 改訂類別: PLAN/EXECUTION_PLAN minor revision (D-4 v1 → v2); **PLAN 大版本不変 v0.2** (decision log 内エントリ更新)
> Owner: main session
> 状態: ✅ 改訂完了, 1A.2 实测准备就绪

---

## 0. ユーザー決定 (2026-05-22)

| 項目 | 元 (D-3 + D-4 v1) | **更新 (D-4 v2)** |
|------|------------------|--------------------|
| OpenAI API account | open 想定 (embedding 用) | **暂不开** (用户)|
| ChatGPT Plus 代理 | 不接入 | 保持不接入 |
| Embedding 主 | OpenAI text-embedding-3-small (1536d) | **bge-m3 (1024d, local)** ★ |
| Embedding fallback | bge-m3 | OpenAI text-embedding-3-small (留接口, 不調) |
| LLM 主答 | Anthropic Sonnet 4.6 (保持) | 保持 |
| LLM 複検 | deepseek-v4-flash 非思考 | **deepseek-v4-pro 非思考** (用户 V4-Pro key 取得) |
| LLM 難題 | Anthropic Opus 4.7 (保持) | 保持 |
| LLM 軽分類 | Anthropic Haiku 4.5 (保持) | 保持 |

ユーザー確認: "1. yes [embedding bge-m3], 2. 保留 [Anthropic chat 鎖]" 2026-05-22

---

## 1. 改訂対象 + 適用差分

### 1.1 PLAN.md (8 edits, 大版本 v0.2 維持; 单一 decision log + minor table 更新)

| § | 改訂内容 | 区分 |
|---|---------|------|
| **§4.1 数据层** | Embedding 行 改为 bge-m3 主 / OpenAI fallback 留接口暂不调 | 表更新 |
| **§4.2 LLM 表** | RAG 主答 fallback / 轻分类 fallback / 复检 主 全部 V4-Flash → V4-Pro 非思考 (3 处) | 表更新 |
| **§4.2 ChatGPT Plus block** | 整段改名 "OpenAI 决策 (D-3 + D-4 v2 联合)" + 加 "API account 暂不开, embedding 主路径改 bge-m3" 注 | block 更新 |
| **§4.4 R-8** | LiteLLM Issue #26395 影响 MED → **HIGH** (用户主用 V4-Pro); 缓解段加 "Phase 1A.2 跑非思考 2 轮 sanity" | 风险升级 |
| **§4.4 R-22 (新)** | bge-m3 本地 model 首次 ~2.5GB 下载 + Mac M-series MPS 推理速度未实测 + Docker torch CPU image ~800MB | 新风险 |
| **§5 Phase 1A 表** | 1A.2 sub 改 (V4-Flash → V4-Pro 非思考) + 加 1A.2.f bge-m3 sanity | step 加 |
| **§10 工期** | Phase 1A 3-4 d → **3.5-4.5 d** (+1A.2.f 0.2 d); Phase 1 TOTAL 13-17 → **13.5-17.5 d** | 工期微調 |
| **§11 Decisions Log** | D-4 → D-4 v1 superseded + D-4 v2 (bge-m3 主) 新追加 | 决策表更新 |

### 1.2 EXECUTION_PLAN.md (1 edit)

| § | 改訂内容 |
|---|---------|
| §1A.2 表 | 1A.2.a 改: V4-Pro 非思考 2 轮 + V4-Pro 思考 1 轮 (single-turn verify Issue #26395 复现); 1A.2.d Router fallback chain 改用 V4-Pro 非思考; 加 1A.2.f bge-m3 sanity |

### 1.3 sdtm-rag/pyproject.toml (1 edit)

加 deps:
- `sentence-transformers>=3.0`
- `torch>=2.4`

OpenAI dep `openai>=1.50` 保留 (LiteLLM Router 内部 import + 留 base_url 接口)。

### 1.4 sdtm-rag/.env.example (1 block edit)

- `OPENAI_API_KEY` 注释化 (暂不用); 加 `OPENAI_API_BASE` 占位
- 加 `HUGGINGFACE_HUB_TOKEN` 注释占位 (gated model 用)
- `SDTM_RAG_FALLBACK_MODEL`: `deepseek/deepseek-v4-flash` → `deepseek/deepseek-v4-pro` 非思考
- `SDTM_RAG_EMBEDDING_MODEL`: `openai/text-embedding-3-small` → `BAAI/bge-m3`
- `SDTM_RAG_EMBEDDING_DIM`: `1536` → `1024`
- 加 `SDTM_RAG_EMBEDDING_DEVICE=mps` (Mac default; Linux Docker 用 cpu/cuda)

### 1.5 sdtm-rag/README.md (1 edit)

Environment Variables 表更新:
- `OPENAI_API_KEY`: ★ 必 → 暂不用 + "留接口预留" 说明
- `DEEPSEEK_API_KEY`: 可选 → **★ 必** (D-4 v2 用户主用 V4-Pro)
- 加 `SDTM_RAG_EMBEDDING_*` 3 行 (default = bge-m3 / 1024 / mps)
- 加 `SDTM_RAG_FALLBACK_MODEL` 注 (V4-Pro 非思考)

---

## 2. R-8 (LiteLLM Issue #26395) 影响重評価

### 2.1 元評価 (PLAN v0.2 §4.4)

| 影响 | 概率 | 重大性 | 缓解 |
|------|------|--------|------|
| RAG multi-turn 用 V4-Pro 会断 | 100% (Open) | MED | 主用 Sonnet, 复检用 V4-Flash 非思考; Phase 1A.2 跑 2 轮对话 sanity |

### 2.2 改訂評価 (D-4 v2 反映)

| 影响 | 概率 | 重大性 | 緩和 |
|------|------|--------|------|
| RAG multi-turn 用 V4-Pro 思考模式会断 | 100% (Open) | **HIGH** (用户主用 V4-Pro 后影响升级) | Phase 1A.2.a 跑 V4-Pro **非思考** 2 轮 sanity + V4-Pro 思考 1 轮 (verify bug 复现, 仅 single-turn); 全程 RAG 复检/fallback 强制非思考 (`reasoning_effort=null` または `thinking={"type": "disabled"}`); LiteLLM Router config 明示 `extra_body={"thinking": {"type": "disabled"}}` 防回归 |

### 2.3 R-22 (新規, bge-m3 local)

| # | 風險 | 影響 | 概率 | 重大性 | 緩和 | 検証 Phase |
|---|------|------|------|--------|------|------------|
| **R-22** (D-4 v2) | bge-m3 model 首次 ~2.5GB 下載 + Mac M-series MPS 推理速度未実測 + Docker torch CPU image ~800MB | Phase 1A.2 sanity 時間 + Docker build + ingest 耗時 | 100% | LOW-MED | 1A.2.f sanity 5 sample text 実測 (期待 <100ms/chunk on MPS); Docker build multi-stage defer (1A.5 後看 image 大小決定); HuggingFace mirror 候選 (中国大陆 access slow 時) | 1A.2 / 1A.5 |

---

## 3. 工期インパクト

| Phase | 元 (v0.2) | 改訂 (D-4 v2) | 差分 |
|-------|----------|---------------|------|
| Phase 1A.2 | 0.3 d | **0.5 d** | +0.2 d (1A.2.f bge-m3 sanity) |
| Phase 1A 合計 | 3-4 d | **3.5-4.5 d** | +0.2 d |
| Phase 1 TOTAL | 13-17 d | **13.5-17.5 d** | +0.5 d (含 bge-m3 ingest 慢 marginally + Docker build 慢) |

Phase 2 KG 無変化 (defer)。

---

## 4. PASS 五条 (本 prep step)

1. **evidence 存在** ✅ — 本文件 + ユーザー会話ログ (2026-05-22 三回 exchange)
2. **writer 産物合規** ✅ — PLAN/EXECUTION_PLAN/pyproject/env.example/README 一括更新, 各 file diff 互いに一貫
3. **独立 reviewer subagent PASS** ⚠️ deferred — 本 step は decision log + config update のみ (writer = main, 圧縮率 0, 設計変更小), Rule D 不強制. 1A.2 sanity 完成後 1A.3 chunker writer kickoff 前に critic 二審 (若必要)
4. **規則 A 抽検** N/A — 圧縮率 0
5. **用户 Bojiang 口頭 ack** ✅ — 2026-05-22 "1. yes [bge-m3], 2. 保留 [Anthropic 链]"

---

## 5. Next Action

1. ✅ PLAN/EXECUTION_PLAN/sdtm-rag config 改訂完了
2. ✅ 本 evidence 落档
3. ⏳ CHANGELOG.md + _progress.json 同步 (Chain 07_RAG)
4. ⏳ commit (改訂を 1 commit に纏める)
5. ⏳ ユーザー DeepSeek V4-Pro API key + ANTHROPIC API key を `.env` に書込后 1A.2 起動 (`executor` subagent kickoff)

---

## 付録: D-4 v2 と上流 design doc の関係

`docs/DESIGN_RAG_KG.md` §3.6 (Approved 2026-04-16) は "Provider-agnostic via LiteLLM, default OpenAI text-embedding-3-small" を書く。本 D-4 v2 は **upstream design doc から落地化偏離** (PLAN §1 ① embedding 偏離). 設計 doc は触らず, PLAN §1 偏離表に既に "A-1/A-2/A-3 ..." を載せている流れで `A-3` の Embedding 部分が今回升级.

設計文書側の改訂は不要 (PLAN 偏離表で吸収済). 但し EXECUTION_PLAN.md には 1A.2.f を明示加, この点は 1A.3 writer / 1A.4 reviewer に必達情報として下流に伝う.
