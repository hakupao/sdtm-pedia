# AI 平台部署 — Phase 6.5

> **状态**: 4 平台部署中 + smoke v4 评测框架完成 (2026-04-22 PM)
> - Claude Projects: v2.6 完成 (1.29M tokens, 77%, 24/24 smoke v2 PASS)
> - ChatGPT GPTs: N5.3 bank v3.2 已跑 (14/14 或 12+2subst)
> - Gemini Gems: N5.3 已跑 (7/10)
> - NotebookLM: P3.8 完成 (9/10 strict PASS, 42 sources + Custom mode)
> - **smoke v3 整块 SUPERSEDED 2026-04-22** (Q10 SUPPTS / Q13 NS / Q8 LBNRIND/AETERM 判据基于错前提) → 升级到 **smoke v4.0**

## 本目录唯一 smoke 评测入口

- **[SMOKE_V4.md](SMOKE_V4.md)** — 4 平台 smoke v4 唯一入口 (1019 行, 3 合 1):
  - **§1 R1 执行 Plan**: 4 平台跑题顺序 / 前置状态 / 每平台手顺 / 阈值 / 评分 / R1→R2 gate
  - **§2 17 题题库 v4.0**: Q1-Q14 (核心 + ChatGPT 专属) + AHP1-3 (anti-hallucination probe)
  - **§3 跨平台对比矩阵**: 17 行 × 4 列骨架, R1 跑完填

## 背景

Phase 1-6 已产出 293 个结构化 Markdown 文件 (63 域 × 3 + 91 terminology + 12 model/chapters + 3 导航文件)。
Phase 7 (自建 RAG) 尚待实施。Phase 6.5 = 利用 AI 平台快速让知识库可用, 并通过 smoke test 跨平台对比业务问答质量。

## 知识库体量

| 内容层 | 文件数 | 大小 | 估算 tokens |
|--------|--------|------|-------------|
| terminology | 91 | 7.6 MB | ~1,892K |
| domain specs | 63 | 672 KB | ~168K |
| domain assumptions | 63 | 240 KB | ~60K |
| domain examples | 63 | 661 KB | ~165K |
| chapters | 6 | 246 KB | ~62K |
| model | 6 | 70 KB | ~18K |
| 导航层 | 3 | 159 KB | ~40K |
| **总计** | **295** | **9.6 MB** | **~2,400K** |

## 四平台分工

| 平台 | 着重方向 | 内容策略 | Tier | smoke v4 阈值 | 状态 |
|------|---------|---------|------|:---:|------|
| **Claude Projects** | 精确查询 + 规则推理 | 19 文件 / 1.29M tokens / 77% | 3 | ≥10/13 (77%, 首测) | 部署完成, v3 未跑, R1 首测 |
| **ChatGPT GPTs** | 全量 + Store 发布 | 9 文件 / N5.3 bank v3.2 | 2 | ≥12/17 (71%) | N5.3 完成, R1 跑 v4.0 |
| **Gemini Gems** | 大范围探索 | 4 文件 / v5 system prompt | 1-2 | ≥9/13 (70%) | N5.3 完成, R1 跑 v4.0 |
| **NotebookLM** | 1 notebook × ≤50 sources | 42 sources / Custom mode 9011 chars | 2 (Pro) | ≥11/13 (85%, R1 容错 ≥10/13) | P3.8 完成 9/10 |

**平台入口**:
- 🟢 Claude Projects → [claude_projects/current/UPLOAD_TUTORIAL.md](claude_projects/current/UPLOAD_TUTORIAL.md) (v2.6 发布版)
- 🟢 ChatGPT GPTs → [chatgpt_gpt/README.md](chatgpt_gpt/README.md)
- 🟢 Gemini Gems → [gemini_gems/README.md](gemini_gems/README.md)
- 🟢 NotebookLM → [notebooklm/README.md](notebooklm/README.md)
- 📐 通用部署范本 → [_template/README.md](_template/README.md) (10 维度规范)

## ai_platforms/ 目录结构 (2026-04-22 整理后)

```
ai_platforms/
├── README.md                         ← 本文件 (总览 + smoke v4 入口)
├── SMOKE_V4.md                       ← 4 平台 smoke v4 唯一入口 (R1 plan + 17 题 + 对比矩阵)
├── SYNC_BOARD.md                     ← ChatGPT+Gemini 双平台 Phase 锁步 board
│
├── 📐 _template/                     通用部署范本 (10 维度规范)
│
├── claude_projects/                  v2.6 终态完成
├── chatgpt_gpt/                      N5.3 bank v3.2 完成
├── gemini_gems/                      N5.3 完成
├── notebooklm/                       P3.8 完成 (9/10)
│
└── archive/smoke_history/            历史归档 (5 份 SUPERSEDED / work-done)
    ├── SMOKE_QUESTIONS_V2.md              v2 10 题 (SUPERSEDED by v3 → v4)
    ├── N5_3_QUESTIONS_DESIGN.md           v3 设计 rationale
    ├── SMOKE_V4_DESIGN_HANDOFF.md         v4 设计过程 handoff (work done 2026-04-22)
    ├── smoke_v3_audit_notes.md            第 11 种 subagent audit 证据 (Q10 SUPPTS baseline + 4 其他 findings)
    └── PHASE4_PLAN.md                     Phase 4 原 plan (被 SMOKE_V4.md §1 取代)
```

每个平台子目录都按 `current/docs/dev/archive` 四层结构, 详见各平台 README.md.

## Rule D chain cumulative 12 种 subagent_type (2026-04-22 闭合)

| # | subagent_type | 用途 | Phase |
|---|---|---|---|
| 1 | general-purpose | Phase 1 初始 | Phase 1 |
| 2 | oh-my-claudecode:verifier | Phase 1 | Phase 1 |
| 3 | oh-my-claudecode:executor | Phase 1 | Phase 1 |
| 4 | oh-my-claudecode:critic | Phase 1 | Phase 1 |
| 5 | oh-my-claudecode:analyst | R3 audit | Phase 2 |
| 6 | pr-review-toolkit:code-reviewer | 某处 | Phase 3 |
| 7 | feature-dev:code-architect | PLAN v1.1 writer | Phase 2 |
| 8 | oh-my-claudecode:architect | PLAN v2 reviewer 9th | Phase 2 |
| 9 | oh-my-claudecode:scientist | P3.4.5 reviewer 10th | Phase 3 |
| 10 | cross-chain aggregate | ChatGPT/Gemini 侧累计 | Phase 3-4 |
| **11** | **oh-my-claudecode:document-specialist** | **smoke v3.2 audit (404 行)** | **2026-04-22** |
| **12** | **feature-dev:code-reviewer** | **P3.8 reviewer (闭合 Rule D gap)** | **2026-04-22** |

第 13 种候选(Phase 4 总审): `pr-review-toolkit:type-design-analyzer` (预留给 smoke v4 R1/R2 meta-review)

## 关键设计原则

1. **ROUTING.md 是 System Prompt 的骨架** — 7 类问题路由规则直接嵌入
2. **内容分层** — 核心知识 (specs + chapters + model) 优先, terminology 按平台容量决定
3. **合并文件保留溯源** — 每个合并段落标注原文件路径, 方便回溯
4. **System Prompt 四平台统一核心 + 平台特化** — 共享 SDTM 领域知识定义, 各自适配平台能力
5. **smoke test 作为跨平台对比 ground truth** — Anti-hallucination probe (AHP) 测"给错前提能否纠错", 不只"给正确前提答对"
6. **Rule A/B/C/D 强制** — Writer/Reviewer 必须不同 subagent_type (chain cumulative 12 种)

## 依赖关系

- 前置: Phase 6 P0-P2 已完成 (ROUTING.md / Cross References / VARIABLE_INDEX.md)
- 后续: Phase 7 自建 RAG 不受 Phase 6.5 影响, 两条路线并行
- smoke v4 评测矩阵 (SMOKE_V4.md §3) 将作为 Phase 7 RAG baseline 对比基准
