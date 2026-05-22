# branches/07_rag_kg/ — 改訂履歴

> 本ファイル管理 branches/07_rag_kg/ 配下のPhase / 産出物 / 決定の履歴.

---

## Phase 0 Research v0.1 (2026-05-22)
- 区分: 新規作成
- 内容: 旁枝骨架 (PLAN/EXECUTION_PLAN/_progress.json/research/evidence/prompts/) 創建. Phase 0 (調研 + PLAN 起草) 起動. T2 LLM provider 調研派遣 background document-specialist. T3 chunker feasibility 主 session 着手.
- 上流参照: `docs/DESIGN_RAG_KG.md` (2026-04-16 Approved) + `.work/05_rag_kg/session_2026-04-16_design.md`
- 触発: 用户「Phase 7 RAG+KG 启动」(2026-05-22)
- 着手 PASS 五条: 評価は Phase 0 終結時.

## Phase 0 Research v0.2 (2026-05-22, critic Rule D PASS 1 反映)
- 区分: 内容修正 + 構造修正 (事实错误修正)
- 触発: critic subagent (Rule D 异 type, writer=main session) 独立审 → CONDITIONAL_PASS verdict, 32 findings (3 HIGH / 7 MED / 6 LOW / 4 INFO)
- 修订内容:
  - **F-1 HIGH (PASS 术语)**: PLAN §9 加 "项目根 CLAUDE.md PASS 四条 + 本旁枝因 chunker 高压缩率加规则 A 抽检为第 5 条" 声明
  - **F-2 HIGH (事实错误)**: chunker_feasibility 4 处事实修正 — (a) lb_part4 漏列 (实测含 2 H2 codelist) (b) VARIABLE_INDEX §二 H3 24 → 63 (c) PC examples H4 16 → 14 (Example 4 仅有 Method A+D) (d) supplementary 文件命名 general_part* → supplementary_part1-6; 同时 domains 数 63 → 64 (含 DI/RELREC/RELSPEC/RELSUB; DI 仅 assumptions.md Issue 15 修复后); PLAN §3 / §6.5 同步
  - **F-3 HIGH (未验证项)**: PLAN §8 风险表加 R-13~R-21 (含 6 项 [UNVERIFIED] follow-up + 4 项运维 risk); 加 Phase 1A.0 sanity re-grep verify step
  - F-6 MED (V4 Pro Reasoner): EXECUTION_PLAN §1D.2 "V4 Pro Reasoner 思考模式" → "V4 Pro 非思考 single-turn" (避 LiteLLM Issue #26395)
  - F-7 MED (Haiku context): R-14 加, 1A.2.e 实测
  - F-8 MED (LiteLLM v1.84.0 breaking): 1A.2.d Router fallback sanity
  - F-9/F-10/F-11 MED (运维 risk): R-15 embedding rate limit + R-16 Chroma backup + R-17 .env 管理
  - F-14 MED (reingest trigger): R-18 server/main.py git HEAD 比对 + warn
  - F-19/F-20/F-21 MED (工期): Phase 1A 2.5-3 d → 3-4 d, Phase 1C 3.5-4 d → 5-6 d, Phase 1 总 10-13 d → 13-17 d
  - F-22 MED (并行注解): EXECUTION_PLAN §9 表加注解
  - F-23 MED (PASS 按 Phase 细分): EXECUTION_PLAN §11 新增, 含 1A/1B/1B5/1C/1D/收口 各 PASS 五条
  - F-24 MED (规则 A 抽检 N 明示): PLAN §9.4 细化 (a)chunker N≥10 (b)1B5/1D N=5 ground truth (c)1C N=5 错误标注
  - F-25 LOW (main session 矩阵注): EXECUTION_PLAN §2.1 加 `<main>` 注解
  - F-27 MED (1C reviewer.py 规则 A): PLAN §9.4 (d) 加 reviewer.py N≥5 user-data-row
  - F-32 INFO (06 P7 表述歧义): PLAN §0.1 "06 P7 99.02% coverage" → "06 P7 字段验证 atom coverage 99.02%"
- 落档 evidence: `evidence/review_pass_1.md` (critic 完整审查报告 + 32 findings 详表)
- 修订统计: chunker_feasibility 10 处 + PLAN 12 处 + EXECUTION_PLAN 9 处 = **31 处 Edit**
- 留 5 LOW (F-12/F-13/F-15/F-16/F-17) 待用户 ack 时决定是否当场修
- 作成: main session (Bojiang指示)
- 確認: critic subagent (Rule D 异 type, 已 PASS 1)
- 承認: Bojiang ack 2026-05-22 (PLAN OK + 同意 critic review + 5 LOW 当场修 + commit 可做)

## Phase 0 Research v0.2 final (2026-05-22, 5 LOW 当场修 + 用户全 ack)
- 区分: 内容修正 (LOW 收口)
- 修订内容:
  - F-12 LOW: PLAN §5 Phase 1C.1 已含 "100MB 上限 + chunksize=10000 流式" (v0.2 主修订时已加)
  - F-13 LOW: PLAN §0.2 Out-of-scope 明示 "Phase 1 单用户/单租户, FastAPI uvicorn --workers 1"
  - F-15 LOW: PLAN §7 metadata schema 加注 "不适用字段一律存 None, 不省略 (Chroma filter null vs missing 行为不同)"
  - F-16 LOW: EXECUTION_PLAN 1A.1.d pyreadstat sanity + sas7bdat fallback (v0.2 主修订已含)
  - F-17 LOW: PLAN R-21 Streamlit st.status/progress + 60s timeout (v0.2 主修订已含)
- 用户决策 ack: D-2 LLM 主力 (Sonnet 主+V4-Flash 复检+Opus 难题) + D-3 不接 Plus 代理 + D-4 text-embedding-3-small + D-5 KG defer (1D 后 gate) + D-6 chunker 三策略 + D-7 INDEX+ROUTING 整体注入 + D-8 eval 提前
- Phase 0 全闭环, Phase 1A.0 sanity 起步可启动
- 作成: main session
- 確認: critic Rule D PASS 1 (2026-05-22)
- 承認: Bojiang Zhang (2026-05-22 全 ack)
- commit: 0644b6c "07 RAG+KG Phase 0 Research closed — PLAN v0.2 + critic Rule D PASS 1 + 用户 ack"

## Phase 1A.0 Sanity Re-grep Verify (2026-05-22, R-13 6 项全 verify + chunker config lock)
- 区分: Phase 1A.0 着手 → 完了 (单 session 内)
- 触発: PLAN §5 Phase 1A.0 sanity 強制 + 用户「启动 Phase 1A.0 sanity」(2026-05-22)
- 主 session 直接執行 (Bash + Python tiktoken, 0.3 d 估 → 単 session 完了)
- R-13 6 項 verify 結果:
  - **項 1** supplementary_part 6 files = 188 H2 codelist (全 codelist 模式, 0 part 兜底)
  - **項 2** core/ part 31 files = 104 H2 (mixed: 13 part 模式 H2=1 占整 file / 18 codelist 模式 H2>1); core/ 単 file codelist 11 files = 42 H2
  - **項 3** questionnaires 43 files = 670 H2 codelist (codelist 級切分, 非 instrument 級)
  - **項 4** mermaid 嵌套: 29 mermaid / 58 fence 全 balanced, 0 嵌套 → 状态机実装
  - **項 5** 表格变体: 0 HTML rowspan/colspan/<table> → GFM pipe-table 簡単 regex 即可
  - **項 6** tiktoken 実測 5 chunk: ★ **HIGH C3 ch04 §4.4 = 9598 cl100k > 8191 embedding limit** + char/4 最大偏差 +23.6% (MB dense table)
- chunker config 5 項 lock (1A.3 writer 必準拠):
  - L-1 mermaid 状态机 (0 嵌套, 不用 stack)
  - L-2 GFM pipe-table 簡単 regex (0 HTML)
  - L-3 tiktoken cl100k_base 実測強制 (char/4 偏差 23.6% > 20% 容許帯)
  - L-4 chapters/ ≥ 50KB 強制 ^### 切 (ch04 §4.4 > 8K embedding limit)
  - L-5 terminology core part 文件 H2=1 → part 模式 / H2>1 → codelist 模式
- 総 chunk 数估算微調: chunker_feasibility v0.2 估 ~4368 → 実測 ~4304 (-1.5%, ±5% 容許内, 不修 v0.2 文档)
- 落档 evidence: `evidence/checkpoints/phase_1a_0_sanity.md` (17 KB) + `scripts/sanity_tiktoken.py` (4.9 KB, tiktoken 0.12.0)
- terminology H2 累計 (1A.0.a 全 grep): core/ 42 + core/part 104 + supplementary 188 + questionnaires 670 = **1004** (chunker_feasibility 估 1005, near-exact)
- 作成: main session
- 確認: PASS 五条 #3 reviewer deferred (本 step EXECUTION_PLAN §1A.0 不強制, Rule D 真審在 1A.3 chunker writer → code-reviewer 那步触发)
- 承認: Bojiang Zhang (2026-05-22 ack)
- next: 1A.1 (sdtm-rag/ 仓库脚手架 + R-17 .env hygiene + R-20 pyreadstat sanity)
- commit: 5c9bf38 "07 RAG+KG Phase 1A.0 sanity 完成 — R-13 6 项 verify + 5 chunker config lock"

## Phase 1A.1 sdtm-rag/ Scaffold (2026-05-22, 16 files + R-17 完備 + R-20 VERIFIED)
- 区分: Phase 1A.1 着手 → 完了 (単 session 内)
- 触発: ユーザー「commit + 1A.1 起動」(2026-05-22, 1A.0 commit 5c9bf38 后)
- 主 session 直接 Write + Bash (脚手架テンプレ作業, EXECUTION_PLAN §1A.1 owner)
- 1A.1.a 目录樹: PLAN §2.2 と一致 — `branches/07_rag_kg/sdtm-rag/{scripts/{chunkers,tests,shared},server,ui,eval,data/chroma}` + pyproject.toml (16 deps + 5 dev + 1 fallback) + Dockerfile (python:3.11-slim, gcc/g++/libxml2-dev/libssl-dev apt) + docker-compose.yml (api + ui services, KB read-only volume mount)
- 1A.1.b .gitignore + README: data/chroma + .env 三層 + python/IDE caches; README 7 段 (Architecture / Quick Start 2 path / Env Vars / PASS 五条 / chunker config L-1..L-5 ref)
- 1A.1.c R-17 .env hygiene: .env.example (3 LLM key + 1 Cohere optional + 8 app config 占位) + .gitignore 三層 (.env / .env.local / .env.*.local) + README Env Vars 段 + 漏洩時 rotate 手順
- 1A.1.d R-20 pyreadstat sanity (★ host 実測):
  - ❌ pyreadstat 1.3.5 (current) は Python ≥ 3.10 必要 (TypeAlias PEP 613); host Py 3.9.6 import fail
  - ✅ pyreadstat 1.2.9 (Py 3.9 backport) host XPT round-trip PASS (USUBJID+AETERM 2 行 byte-exact)
  - ✅ sas7bdat fallback import + class introspection OK (read-only, .xpt 非対応)
  - 結論: `pyproject.toml` `pyreadstat>=1.2` (lower-bound) で pip が Py バージョン自動解決. Docker Py 3.11 → 1.3.5, host Py 3.9 → 1.2.9. R-20 **VERIFIED + MITIGATED**.
- 16 files: pyproject.toml / Dockerfile / docker-compose.yml / .gitignore / .env.example / README.md / 7×__init__.py / scripts/tests/conftest.py / data/.gitkeep ×2
- 落档 evidence: `evidence/checkpoints/phase_1a_1_scaffold.md` (~9 KB, R-20 実測マトリックス含む)
- 作成: main session
- 確認: PASS 五条 #3 reviewer deferred (EXECUTION_PLAN §1A.1 不強制, 真審 1A.3 chunker writer 触発)
- 承認: pending Bojiang ack
- next: 1A.2 LiteLLM sanity (DeepSeek V4 Pro 2 ターン思考 + Sonnet 2 ターン + V4-Flash 非思考 + Router fallback + Haiku context window 実測)
- commit: 3900b9e "07 RAG+KG Phase 1A.1 scaffold — sdtm-rag/ 16 files + R-17 .env + R-20 VERIFIED"

## Phase 1A.2 Prep — D-4 v2 mini-revision (2026-05-22, bge-m3 主 + V4-Flash → V4-Pro 非思考)
- 区分: PLAN/EXECUTION_PLAN minor revision (decision log + table 更新, 大版本不変 v0.2)
- 触発: ユーザー意思決定 2026-05-22 「OpenAI 留接口暂不使用, 只使用 DeepSeek V4 Pro; embedding bge-m3 yes; Anthropic 保留」
- 上流: 元 D-3 (ChatGPT Plus 代理不接入) + 元 D-4 v1 (OpenAI text-embedding-3-small 主 + bge-m3 fallback)
- 改訂内容:
  - **D-4 v1 superseded → D-4 v2** ★: bge-m3 (1024d, local sentence-transformers) **主**, OpenAI text-embedding-3-small fallback (留接口暂不調)
  - **D-2 微調**: 複検モデル V4-Flash → **V4-Pro 非思考** (ユーザー V4-Pro key 持有); 主答 Sonnet + 難題 Opus + 軽分類 Haiku 不変
  - **R-8 重大性 MED → HIGH**: LiteLLM Issue #26395 ユーザー主用 V4-Pro 後影響升级; 全程 RAG 複検/fallback 強制非思考 (`extra_body={"thinking": {"type": "disabled"}}`)
  - **R-22 新規**: bge-m3 本地 model 首次 ~2.5GB 下載 + Mac M-series MPS 推理速度未実測 + Docker torch CPU image ~800MB; 1A.2.f 实测
- PLAN.md 8 edits: §4.1 (embedding 表 bge-m3 主) + §4.2 (LLM 表 3 处 V4-Flash → V4-Pro) + §4.2 (OpenAI 决策 block 改名 D-3+D-4 联合) + §4.4 (R-8 升级 + R-22 加 + 边注) + §5 (1A.2 加 1A.2.f bge-m3 + 0.3 → 0.5 d) + §10 (Phase 1A 3-4 d → 3.5-4.5 d, Phase 1 TOTAL 13-17 → 13.5-17.5 d) + §11 (D-2 微调 + D-3 ack + D-4 v1 superseded + D-4 v2 加 + D-5/6/7/8 ack date 更新)
- EXECUTION_PLAN.md 1 edit: §1A.2 表加 1A.2.f bge-m3 + V4 Pro 思考 → 非思考 全行
- sdtm-rag/pyproject.toml: 加 sentence-transformers>=3.0 + torch>=2.4
- sdtm-rag/.env.example: OPENAI_API_KEY 注釈化 (暂不用) + DEEPSEEK_API_KEY ★必 + FALLBACK_MODEL V4-Flash→V4-Pro + EMBEDDING_MODEL OpenAI→BAAI/bge-m3 + EMBEDDING_DIM 1536→1024 + EMBEDDING_DEVICE=mps 加 + HUGGINGFACE_HUB_TOKEN 占位
- sdtm-rag/README.md: Environment Variables 表更新 (OPENAI 暂不用 / DEEPSEEK ★必 / EMBEDDING_* 3 行加)
- 落档 evidence: `evidence/checkpoints/phase_1a_2_prep_d4_v2_revision.md` (~6KB, 含 R-8 重評価 + R-22 + 工期影响 + PASS 五条)
- 作成: main session
- 確認: PASS 五条 #3 reviewer deferred (decision log update, writer=main 圧縮率 0); 必要なら critic 二審
- 承認: Bojiang Zhang 2026-05-22 二回 ack ("1. yes [bge-m3], 2. 保留 [Anthropic]")
- next: ユーザー DeepSeek V4-Pro API key + ANTHROPIC API key を `branches/07_rag_kg/sdtm-rag/.env` に書込后 1A.2 起動 (`executor` subagent)

---
