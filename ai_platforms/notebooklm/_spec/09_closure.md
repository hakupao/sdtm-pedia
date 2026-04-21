# 09 收束 — 三件套 + Reorg

Phase 5 产出: RETROSPECTIVE / handoff / UPLOAD_TUTORIAL + 目录重组 + 上游更新.

---

## 收束三件套总览

| 件 | 位置 | 给谁看 | 强制程度 |
|----|------|-------|---------|
| RETROSPECTIVE.md | `docs/RETROSPECTIVE.md` | 下个类似项目负责人 | Tier 2/3 强制 (规则 C) |
| handoff.md | `docs/handoff.md` | 下游 (e.g. Phase N+1 启动者) | 有下游时强制 |
| UPLOAD_TUTORIAL.md | `current/UPLOAD_TUTORIAL.md` | 部署这个发布版的用户 | 强制 (有发布版必要) |

加上辅助:
- 目录 reorg 到四层 (参 `01_directory_structure.md`)
- `ROADMAP.md` 状态更新
- 上游 `ai_platforms/README.md` 总览表更新
- 项目 `CLAUDE.md` Key Paths 新增
- Git commit + push

---

## 件 1: RETROSPECTIVE.md (规则 C 三段式)

### 强制章节

```markdown
# <Platform> <Phase> — 复盘

> 范围: <start> → <end> (commits <...> → <...>)
> 产出: <核心 metric: tokens / 文件数 / A/B pass ratio>
> 状态: <终态名>

---

## 1. 保留下来的做法 (推广到其他项目)

| # | 做法 | 理由 |
|---|------|------|
| R1 | ... | ... |

## 2. 必须补上的 (本次暴露的缺口)

| # | 缺口 | 本次表现 | 补法 |
|---|------|---------|------|
| G1 | ... | ... | ... |

## 3. 关键决策复盘

### 3.1 <决策 1 名>

- **情景**: ...
- **决策**: ...
- **结果验证**: ...
- **教训**: ...

## 4. 可迁移规则 (评估是否新增到全局 CLAUDE.md)

- 候选规则 <X>: ...

## 5. 工作量数据

| 指标 | 值 |
|------|---|
| ... | ... |

## 6. 这次留下但不一定每次都做

- ...

## 7. 对后续项目的 actionable advice

- 1. ...
```

### 规则 C 要求

- Tier 2/3 项目收尾**必写**
- 至少三段: 保留 / 补上 / 决策复盘 (章节 1-3 强制)
- 章节 4-7 按 Tier 伸缩 (Tier 3 全写, Tier 2 至少写 5)

### 独立审阅 (规则 D)

RETROSPECTIVE 草稿 **不能主控自审**.

派发 reviewer subagent (不同 subagent_type), 输出 `dev/evidence/H<N>_reviewer.md`, verdict 必含:
- 三段式完备?
- 规则 A/B/C/D/E 全对照?
- 是否有数据缺口 / 自圆其说 / 遗漏重要决策?

Claude v2 范例: `claude_projects/dev/evidence/H1_reviewer.md` (code-reviewer subagent 7 checks, CONDITIONAL_PASS → PASS 修 2 MEDIUM + 3 LOW).

### 避坑

| 反例 | 问题 |
|------|------|
| 只写 "保留下来", 不写 "缺口" | 下个项目继续踩坑 |
| 缺口写 "下次更努力" 类虚话 | 不 actionable, 等于没写 |
| 决策复盘只列结果, 不解释 why | 复盘不能复现决策逻辑 |
| 写完即 PASS, 不找人审 | 违反规则 D, 可能漏盲点 |

---

## 件 2: handoff.md (向下游交接)

### 何时写

有 Phase N+1 / 下游项目依赖本次产出时. 无下游可跳过.

### 强制章节

```markdown
# <Phase N> → <Phase N+1> 交接

> 触发: <Phase N 终态>
> 下游: <Phase N+1 启动者 / 相关文档>

## 0. TL;DR (1 句话)

<一句话: 本次终态 + 给下游的最关键 actionable>

## 1. 核心数据点 (简版)

| 阶段 | tokens | 文件 | capacity | PASS | 备注 |

## 2. 关键发现 (下游必读)

### 2.1 <发现 1>
### 2.2 <发现 2>
...

## 3. 对下游的 actionable (列表, 每条一段)

### 3.1 <actionable 1>
### 3.2 <actionable 2>
...

## 4. 下游启动前待办 (建议顺序)

1. 读 <哪些文件>
2. 做 <哪些预实验>
3. 起草 <下游的哪些文档>

## 5. 未解决的问题 (Phase N+1 需要答)

1. Q: ...
2. Q: ...
```

### 规则

- 不要复述 RETROSPECTIVE 的内容 (handoff 只写 actionable)
- 每个 actionable 明示"下游做什么"
- 预估下游读完需要的时间 (<20 分钟 / <1 小时 / 半天)

### 范例

`claude_projects/docs/phase7_handoff.md` — 9668 bytes, 6 actionable + 5 未解 Q + 5 步待办, 下游 Phase 7 启动时直接读.

---

## 件 3: UPLOAD_TUTORIAL.md (用户视角 10 章节)

### 位置

`<platform>/current/UPLOAD_TUTORIAL.md`

### 强制章节 (10 章节)

```markdown
# <Platform> Project 制作教程 — <Knowledge Base Name> 发布版

> 从零开始搭建一个能查 <domain> 标准的 <Platform> Project.
> 读完本教程你会得到: ...
> 总耗时: <N> 分钟.

---

## 0. 前置要求
- 订阅级别 / 网页访问 / 本地 clone 等

## 1. 新建 <Platform> Project
- 命名 / Description / 访问权限

## 2. 配置 System Prompt (Custom Instructions)
- 完整复制 `current/system_prompt.md`

## 3. 上传 N 个知识库文件
- 拖拽/选择 / 文件清单 / 常见问题

## 4. 等待 Indexing (或不等)
- 本平台 Indexing 是否可靠 / 多久 / 能否立即试问

## 5. Smoke Test (3-5 题快速验证)
- 最简 3-5 题, 确认基础路由工作

## 6. 完整 A/B 回归 (可选, 深度用户)
- 指引到 `dev/test_results.md` 24 题完整矩阵

## 7. 排错手册
- Indexing 卡住? / 某类问题拒答? / 文件超容量?

## 8. 升降级
- 如何从老版本 Project 替换到本版?
- 如何降级到更小版本 (如容量不够)?

## 9. 团队分享 (如平台支持)
- 链接生成 / 权限设置

## 10. 后续
- 知识库更新时如何重部署
- 相关下游文档
```

### 去版本化 (关键)

- 文件名 / 图片 / 截图都**不能**出现 `v1`/`v2` 之类的内部版本号
- 发布版本身就叫"发布版", 不叫 "v2.6"
- 如果教程要提当前版本号, 放到 `README.md §关键事实` 而非 tutorial 标题

### 30-90 分钟可落地

验证方法: 让一个**从未参与本项目的人**按 tutorial 走一遍, 能否独立跑通.

### 范例

`claude_projects/current/UPLOAD_TUTORIAL.md` — 10 章节齐全, 含 §7 排错手册 + §8 升降级.

---

## 件 4: ROADMAP.md 状态更新

### 修改点

打开本平台的 `ROADMAP.md`, 改:

```diff
- > 状态: **待开始**
+ > 状态: **已完成** (<date>)
+ > **实际产出**: <tokens> / <files> / <capacity>% / <ab_pass_ratio>
+ > **终态文档**: docs/RETROSPECTIVE.md / docs/handoff.md (如有) / current/UPLOAD_TUTORIAL.md
```

保留原"预计策略 A/B"段供对照, **不要删**, 加一行 "实际执行" 说明偏差 (e.g. Claude ROADMAP 保留了原策略 A/B, 加了"实际实施从 200K → 1.29M tokens 演进, 见 PLAN_V2.md").

---

## 件 5: 目录 Reorg 到四层

参 `01_directory_structure.md` 的 reorg 操作:

- [ ] `mkdir current docs dev archive`
- [ ] `git mv` 最终产物到 `current/uploads/` + 去版本号重命名
- [ ] `git mv` 开发产物到 `dev/` + 保留 hardcoded 路径
- [ ] `git mv` 历史版本到 `archive/v<N-1>/`
- [ ] 写 `dev/README.md` 路径映射表
- [ ] 写 `archive/README.md` 冻结声明
- [ ] 写 `docs/` headers "post-reorg note" (内部路径为 reorg 前语境)

**Claude 经验**: reorg-A + reorg-B + fix 三个 commit (参 `87573bd` → `bf8fcf0`).

---

## 件 6: 上游索引更新

### `ai_platforms/README.md`

更新总览表格:

```diff
- | <Platform> | 待开始 |
+ | <Platform> | **发布版完成** (<date>) |
```

### 项目 `CLAUDE.md` Key Paths

新增入口:

```diff
+ | Phase 6.5 <Platform> 当前可部署 | `ai_platforms/<platform>/current/` |
+ | Phase 6.5 <Platform> 部署教程 | `ai_platforms/<platform>/current/UPLOAD_TUTORIAL.md` |
+ | Phase 6.5 <Platform> 方法论 | `ai_platforms/<platform>/docs/` |
```

### `.work/MANIFEST.md` + `.work/meta/worklog.md` + `docs/PROGRESS.md`

按项目 CLAUDE.md `## Session Wrap-up` 段的 checklist 操作 (Chain B).

---

## 件 7: Git Commit + Push

- 单个收束 commit, 不拆
- commit message 包含: tokens / files / pass ratio / 触发规则
- push 到 main

```bash
git add <platform>/
git commit -m "$(cat <<'EOF'
<Platform> v<N> closure: <tokens>/<files>/<capacity>%/<pass_ratio> + reorg

- current/: 发布版去版本号
- docs/: RETROSPECTIVE + handoff + (research)
- dev/: scripts + evidence (L1/L2/L3) + ab_reports + checkpoints
- archive/: v<N-1> 冻结

规则 C 产物 + Rule D 独立复核 PASS.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
git push origin main
```

---

## Tier 伸缩

| 件 | Tier 1 | Tier 2 | Tier 3 |
|----|--------|--------|--------|
| RETROSPECTIVE | 一段话 (规则 C 不强制 Tier 1) | 三段式 (§1-§3) | 七章完整 (§1-§7) |
| handoff | 跳过 (如无下游) | 一页 (TL;DR + 3 actionable) | 完整 (§1-§5) |
| UPLOAD_TUTORIAL | 一页 quickstart | 10 章节完整 | 10 章节 + 团队协作段 + API 集成段 |
| Reorg | 建议但不强制 | 强制 | 强制 |
| 上游索引更新 | 只更项目 README | 完整 4 文件 | 完整 + migration note |

---

## 反例 (应避免)

| 反例 | 问题 |
|------|------|
| RETROSPECTIVE 和 handoff 内容重复 | 单一 source of truth 破坏 |
| UPLOAD_TUTORIAL 里出现 `v2.6` 这种内部版本号 | 用户困惑 "v1 v3 在哪" |
| Reorg 改脚本路径 | 破坏 dev/ 的时间快照性质 |
| 收束后忘更新 `ai_platforms/README.md` | 总览表过时, 新来的找不到入口 |
| 多 commit 拆收束变更 | PR 审阅困难, history 碎 |
| handoff 写"下次加油" 不 actionable | 等于没写 |
| RETROSPECTIVE 主控自审 | 违反规则 D |

---

## 终态验收 checklist

收束 commit 前自检:

- [ ] `docs/RETROSPECTIVE.md` 三段式完整, 独立 reviewer PASS
- [ ] `docs/handoff.md` 如有下游, TL;DR + actionable 齐
- [ ] `current/UPLOAD_TUTORIAL.md` 10 章节, 可让新人独立跑通
- [ ] `current/` 完全去版本号
- [ ] `ROADMAP.md` 状态更新
- [ ] 四层目录 reorg 完成
- [ ] `dev/README.md` 路径映射表齐
- [ ] `archive/README.md` 冻结声明齐
- [ ] 上游 `ai_platforms/README.md` 总览表更新
- [ ] 项目 `CLAUDE.md` Key Paths 新增入口
- [ ] `.work/MANIFEST.md` + worklog + PROGRESS.md 更新 (Chain B)
- [ ] Git status 无 untracked / modified
- [ ] Push 无冲突

全部打钩 → 终态.

---

*来源: claude_projects v2 Phase H 收束 (UPLOAD_TUTORIAL 10 章节 + reorg 三 commit + H1-H5 task 序列).*
