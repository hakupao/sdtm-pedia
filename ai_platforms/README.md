# AI 平台部署 — Phase 6.5

> 状态: **进行中** (2026-04-16)
> 目标: 将 SDTM 知识库部署到三大 AI 平台，让知识库立即可用

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

| 平台 | 着重方向 | 内容策略 | 目标用户 |
|------|---------|---------|---------|
| **Claude Projects** | 精确查询 + 规则推理 | 精选核心 (~200K tokens) | 自己日常使用 |
| **ChatGPT GPTs** | 全量覆盖 + 团队分享 | 合并文件全量上传 (~9.6MB) | 团队 + 外部 |
| **Gemini Gems** | 大范围探索 + 全域对比 | 核心全量 (~512K tokens) | 自己深度分析 |

## 目录结构

```
ai_platforms/
├── README.md                          ← 本文件（总览）
├── chatgpt_gpt/
│   ├── ROADMAP.md                     行进路线
│   └── output/                        合并后的上传文件
│       ├── instructions.md            GPT Instructions (System Prompt)
│       ├── chapters_all.md            6 章合一
│       ├── model_all.md               6 文件合一
│       ├── domain_specs_all.md        63 spec 合一
│       ├── domain_assumptions_all.md  63 assumptions 合一
│       ├── domain_examples_all.md     63 examples 合一
│       ├── navigation.md              ROUTING + INDEX + VARIABLE_INDEX 合一
│       └── terminology_*.md           术语文件 (分 3-4 文件)
├── claude_projects/
│   ├── ROADMAP.md                     行进路线
│   └── output/
│       ├── system_prompt.md           Project Instructions
│       └── (精选文件，可直接上传)
└── gemini_gems/
    ├── ROADMAP.md                     行进路线
    └── output/
        ├── instructions.md            Gem Instructions
        └── (合并文件)
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
