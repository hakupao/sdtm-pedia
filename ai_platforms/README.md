# AI 平台部署 — Phase 6.5

> 状态: **进行中** (Claude 完成 + reorg 到 current/docs/dev/archive / ChatGPT + Gemini 待开始, 最后更新 2026-04-20 晚)
> 目标: 将 SDTM 知识库部署到三大 AI 平台，让知识库立即可用
> Claude 线路完结状态: v1 (192K, 9/9 PASS) + v2 终态 v2.6 (1.29M, 24/24 PASS, capacity 77%) 全部 push 到 main, 长尾 302 codelist 明确归 Phase 7 RAG
> **Claude 目录 reorg 后新入口**: [claude_projects/README.md](claude_projects/README.md)

## 背景

Phase 1-6 已产出 293 个结构化 Markdown 文件（63 域 × 3 + 91 terminology + 12 model/chapters + 3 导航文件）。
Phase 7 (自建 RAG) 尚待实施。在此之前，利用现有 AI 平台快速让知识库可用。

## 知识库体量

| 内容层 | 文件数 | 大小 | 估算 tokens | 说明 |
|--------|--------|------|-------------|------|
| terminology | 91 | 7.6 MB | ~1,892K | Codelist 值表，占总量 79% |
| domain specs | 63 | 672 KB | ~168K | 变量定义 (xlsx 生成，含 Cross References) |
| domain assumptions | 63 | 240 KB | ~60K | 业务规则 |
| domain examples | 63 | 661 KB | ~165K | 数据集示例 |
| chapters | 6 | 246 KB | ~62K | IG 通用规则 (ch01-ch10) |
| model | 6 | 70 KB | ~18K | SDTM v2.0 模型 |
| 导航层 (INDEX/ROUTING/VAR_INDEX) | 3 | 159 KB | ~40K | AI 检索入口 |
| **总计** | **295** | **9.6 MB** | **~2,400K** | — |
| **去掉 terminology** | **204** | **2.0 MB** | **~512K** | **核心知识** |

## 三平台分工

| 平台 | 着重方向 | 内容策略 | 目标用户 | Tier | 状态 |
|------|---------|---------|---------|------|------|
| **Claude Projects** | 精确查询 + 规则推理 | 发布版 1.29M tokens / 19 文件 / capacity 77% | 自己日常使用 | 3 | **发布版完成** (2026-04-20) |
| **ChatGPT GPTs** | 全量覆盖 + 团队分享 + Store 发布 | 8-10 合并文件 (~9.6MB), 2 批到位 | 团队 + 外部 | 2 | **待开始** (范本就绪 2026-04-20) |
| **Gemini Gems** | 大范围探索 + 全域对比 | 3-5 合并文件 (~513K tokens), 1 批全上 | 自己深度分析 | 1-2 | **待开始** (范本就绪 2026-04-20) |

**平台入口** (所有平台都走四层 `current/docs/dev/archive` 结构):

- 🟢 **Claude Projects 发布版** → [claude_projects/current/UPLOAD_TUTORIAL.md](claude_projects/current/UPLOAD_TUTORIAL.md)
- 🟡 **Claude Projects 方法论** → [claude_projects/docs/](claude_projects/docs/) (PLAN / 复盘 / RAG 衰减曲线 / Phase 7 交接)
- 🔜 **ChatGPT GPTs 入口** → [chatgpt_gpt/README.md](chatgpt_gpt/README.md) + [chatgpt_gpt/ROADMAP.md](chatgpt_gpt/ROADMAP.md) + [chatgpt_gpt/docs/platform_profile.md](chatgpt_gpt/docs/platform_profile.md)
- 🔜 **Gemini Gems 入口** → [gemini_gems/README.md](gemini_gems/README.md) + [gemini_gems/ROADMAP.md](gemini_gems/ROADMAP.md) + [gemini_gems/docs/platform_profile.md](gemini_gems/docs/platform_profile.md)
- 📐 **通用部署范本** → [_template/README.md](_template/README.md) (10 维度 / 启动 checklist / 继承 Claude v2 方法论)

## 目录结构

```
ai_platforms/
├── README.md                              ← 本文件（总览）
├── 📐 _template/                          ← 通用部署范本 (10 维度规范)
│   ├── README.md                          范本入口
│   ├── APPLY_CHECKLIST.md                 新平台启动清单
│   └── 00-09_*.md                         10 个维度规范文档
│
├── claude_projects/                       v2.6 终态 (2026-04-20)
│   ├── README.md / ROADMAP.md
│   ├── 🟢 current/                        发布版 (19 文件 + system_prompt + UPLOAD_TUTORIAL)
│   ├── 🟡 docs/                           方法论 (PLAN_V2 + RETROSPECTIVE_V2 + rag_decay_curve + phase7_handoff + capacity_research)
│   ├── 🔵 dev/                            过程产物 (scripts + evidence + ab_reports + checkpoints + test_results)
│   └── ⚫ archive/                        历史归档 (v1 冻结 + RETROSPECTIVE 顶层)
│
├── chatgpt_gpt/                           待开始 (范本就绪)
│   ├── README.md / ROADMAP.md
│   ├── 🟢 current/                        占位 (等 Phase 3 产出发布版)
│   ├── 🟡 docs/                           platform_profile.md (Phase 0 初稿)
│   ├── 🔵 dev/                            占位 (启动后填)
│   └── ⚫ archive/                        占位 (暂无历史)
│
└── gemini_gems/                           待开始 (范本就绪)
    ├── README.md / ROADMAP.md
    ├── 🟢 current/                        占位
    ├── 🟡 docs/                           platform_profile.md (Phase 0 初稿)
    ├── 🔵 dev/                            占位
    └── ⚫ archive/                        占位
```

## 依赖关系

- 前置: Phase 6 P0-P2 已完成（ROUTING.md、Cross References、VARIABLE_INDEX.md 已生成）
- 后续: Phase 7 自建 RAG 不受影响，两条路线并行
- System Prompt 设计可复用到 Phase 7 的 prompt engineering

## 关键设计原则

1. **ROUTING.md 是 System Prompt 的骨架** — 7 类问题路由规则直接嵌入
2. **内容分层** — 核心知识 (specs + chapters + model) 优先，terminology 按平台容量决定
3. **合并文件保留溯源** — 每个合并段落标注原文件路径，方便回溯
4. **System Prompt 三平台统一核心 + 平台特化** — 共享 SDTM 领域知识定义，各自适配平台能力
