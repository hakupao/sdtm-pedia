# Claude Projects — SDTM 知识库

## 我想做什么?

### 部署一个可用的 SDTM Claude Project
→ 直接去 [**current/**](current/), 读 [UPLOAD_TUTORIAL.md](current/UPLOAD_TUTORIAL.md).

### 理解这套知识库怎么做出来的 (方法论参考)
→ 去 [**docs/**](docs/) 看开发计划、复盘、RAG 衰减数据.

### 考古 / 复盘 / 贡献改进
→ 去 [**dev/**](dev/) (过程产物) 或 [**archive/**](archive/) (早期迭代归档).

---

## 目录结构 (面向用户 vs 面向开发者)

```
claude_projects/
├── README.md                         ← 本文件
├── ROADMAP.md                        项目路线历程
│
├── 🟢 current/                       发布版 (用户视角, 无版本号)
│   ├── UPLOAD_TUTORIAL.md            ★ 完整部署教程
│   ├── README.md                     发布版总览 + 能力范围
│   ├── uploads/                      19 个知识库文件 (1.29M tokens)
│   ├── system_prompt.md              Custom Instructions
│   └── upload_manifest.md            清单 + token 统计
│
├── 🟡 docs/                          方法论文档 (开发者视角)
│   ├── PLAN_V2.md                    开发计划
│   ├── RETROSPECTIVE_V2.md           复盘
│   ├── rag_decay_curve.md            RAG 质量 vs 规模曲线 (7 数据点)
│   ├── phase7_handoff.md             交接给 Phase 7 自建 RAG
│   └── capacity_research.md          容量调研
│
├── 🔵 dev/                           开发过程产物 (复盘/考古)
│   ├── scripts/                      构建脚本
│   ├── evidence/                     trace + progress + subagent prompts
│   ├── ab_reports/                   A/B 测试报告
│   ├── checkpoints/                  自动执行 handoff
│   └── test_results.md               完整回归矩阵 (部署后自查用)
│
└── ⚫ archive/                       早期迭代归档 (只读)
    ├── RETROSPECTIVE.md              早期迭代复盘 (规则 A/B/C/D 源头)
    └── v1/                           第一版全部产物 (冻结)
```

---

## 对外 vs 对内的两种视角

这个目录服务两类人:

**面向用户/部署者**: 只需要看 [current/](current/). 发布版是**无版本概念的单一产物**, 跟着 UPLOAD_TUTORIAL 走即可. 不需要知道 v1/v2 是什么.

**面向开发者/复盘者**: [docs/](docs/) + [dev/](dev/) + [archive/](archive/) 是开发过程的完整记录, 保留版本号 (v1/v2) 是为了复盘时能区分不同开发迭代. 这些文件对用户部署没有影响.

---

## 关键事实 (发布版)

- 知识库覆盖: CDISC SDTM v3.4 — 63 域 spec + assumptions + examples (100%) + 6 章 chapters + 885 个 inline codelist (占 1005 总数的 88%, 剩余 12% 为 MedDRA 级 giants 和 questionnaires 长尾, 走 Deferred stub 或 Phase 7)
- 总量: ~1,286,161 tokens / 19 个 `.md` 文件
- Claude Project capacity 实测: **77%** (需要 Pro 及以上套餐)
- 部署后测试基线: 24 题回归矩阵 24/24 PASS (详见 [dev/test_results.md](dev/test_results.md))

---

## 订阅套餐与 Project 分享能力 (重要)

**本仓库提供的是"自建 Project 的素材包 + 教程", 不是一个可以被直接分享使用的 Claude Project 链接.** 原因来自 Anthropic 的套餐限制:

| 套餐 | 能创建 Project | 能**分享** Project 给他人 | 本仓库的使用方式 |
|------|---------------|-------------------------|-----------------|
| Free | ✅ (2026-02 起开放) | ❌ | 跟着 [UPLOAD_TUTORIAL.md](current/UPLOAD_TUTORIAL.md) 自建 (容量/上下文会受限) |
| Pro | ✅ | ❌ | 跟着教程自建, 推荐路径 |
| Max (5x / 20x) | ✅ | ❌ | 跟着教程自建, 和 Pro 一样, Max 只给更多配额不给分享功能 |
| Team | ✅ | ✅ (可设为组织内公开或邀请制) | 一位成员按教程建好后, 可直接 Share 给同团队其他成员 |
| Enterprise | ✅ | ✅ (同 Team, 加 SSO / 角色权限等) | 同 Team |

**关键结论**:
1. Free / Pro / Max 用户**无法把自己建好的 Project 分享给别人使用**. 每位用户都必须按照 `current/UPLOAD_TUTORIAL.md` 的步骤, 在自己账号里各自新建一次 Project (上传同一份 `uploads/` + 同一份 `system_prompt.md`).
2. Team / Enterprise 用户可以由一人建好后, 在组织内共享 (公开 / 邀请制), 其他成员无需重复上传.
3. 所以本仓库对 **Free/Pro/Max 用户而言是"配方"**, 对 **Team/Enterprise 用户而言是"一次构建, 全组织复用"的源材料**.

配方 vs 成品的区别, 直接决定了你把这个仓库交给别人时该说什么 — 交给个人订阅用户时, 要明确告诉他"需要你自己账号里跟着教程建一次", 不要误以为能收到一个现成链接.

权威来源:
- [Manage project visibility and sharing — Claude Help Center](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing)
- [Collaborate with Claude on Projects — Anthropic](https://www.anthropic.com/news/projects)
- [Team plan — Claude](https://claude.com/pricing/team)

---

## 后续

- 本发布版是完整终态, 短期内无重大升级计划
- 长尾 302 个 codelist (296 questionnaires + 6 giants) 归属项目的 Phase 7 自建 RAG (设计见本项目 `docs/DESIGN_RAG_KG.md`)
- 如需 API 可调用版本、团队分享、或推高 capacity 覆盖率, 参考 [docs/phase7_handoff.md](docs/phase7_handoff.md) 的后续建议

---

## 目录演进说明 (2026-04-20)

本目录在 2026-04-20 从混乱平铺结构重组为当前四层 (current/docs/dev/archive), 主要目的:
1. 给用户/部署者一个无歧义的入口 (`current/`)
2. 剥离内部开发视角的版本号叙事到 `docs/` `dev/` `archive/`
3. 保证对外只暴露"发布版"概念

开发者如果要看原始平铺结构, 参考 git log `Phase 6.5 v2 reorg-A` commit (`87573bd`) 的 rename 记录, 或读 [dev/README.md](dev/README.md) 的路径映射表.
