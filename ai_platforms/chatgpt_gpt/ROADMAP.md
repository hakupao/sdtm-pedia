# ChatGPT GPTs — 行进路线

> 状态: **待开始** (范本就绪, 等 Phase 0 启动)
> 着重方向: 全量覆盖 + 团队分享 + Custom GPT Store 发布
> 平台: ChatGPT Plus / Team — GPTs (Custom GPTs)
> Tier 等级: **Tier 2** (预计 5-10 步, 1-2 天)
> 范本: [`../_template/`](../_template/) — 启动时读 [APPLY_CHECKLIST.md](../_template/APPLY_CHECKLIST.md)
> 平台特化画像: [docs/platform_profile.md](docs/platform_profile.md) (Phase 0 初稿)
>
> **终态文档** (Phase 5 收束后会有):
> - `docs/PLAN.md` / `docs/RETROSPECTIVE.md` / `current/UPLOAD_TUTORIAL.md` / `dev/test_results.md`

---

## 1. 平台特性 (Phase 0 初稿)

详见 [docs/platform_profile.md](docs/platform_profile.md). 核心要点:

- **检索方式**: 内置 RAG (File Search) — 自动 chunk + embeddings + 检索片段注入
- **文件限制**: **20 文件硬限** / 单文件 512MB / 总量无官方硬上限
- **上下文**: 检索到的片段注入 (非全量)
- **分享**: 私有 / 组织内 / 公开 GPT Store — **唯一可生成公开链接**的本系列平台
- **独有能力**: Conversation Starters / GPT Actions / Marketplace 发布

---

## 2. 内容策略 (Phase 2 初稿, 会在 PLAN 里迭代)

把 295 源文件合并为 **8-10 个文件** 以匹配 20 文件硬限:

| # | 目标文件 | 源 | 大小估算 | 优先级 |
|---|---------|---|--------:|-------|
| 1 | `navigation.md` | ROUTING + INDEX + VAR_INDEX | ~159 KB | P0 |
| 2 | `chapters_all.md` | chapters/ 6 文件合一 | ~246 KB | P0 |
| 3 | `model_all.md` | model/ 6 文件合一 | ~70 KB | P0 |
| 4 | `domain_specs_all.md` | 63 spec.md 合一 | ~672 KB | P0 |
| 5 | `domain_assumptions_all.md` | 63 assumptions.md 合一 | ~240 KB | P1 |
| 6 | `domain_examples_all.md` | 63 examples.md 合一 | ~661 KB | P1 |
| 7 | `terminology_core.md` | terminology/core/ | ~3.2 MB | P2 |
| 8 | `terminology_questionnaires.md` | terminology/questionnaires/ | ~3.8 MB | P2 |
| 9 | `terminology_supplementary.md` | terminology/supplementary/ | ~0.6 MB | P2 |

### 本平台独有约束 (P11)

在范本 P1-P10 之外, 本平台新增:

- **P11 合并粒度硬限**: 最终上传文件数 ≤ 20
- **P12 溯源标注强制**: 合并段必须用 `<!-- source: domains/AE/spec.md -->` 标注, 便于 chunker 不打断表格 + 模型引用时能指回源
- **P13 TableAware 分段**: 合并脚本必须用 md-heading 边界保护表格, 不得在 table row 中切

---

## 3. 执行步骤 (按范本 Phase 0-5)

- [ ] **Phase 0 启动** (范本 `02_workflow.md`): 填完 `docs/platform_profile.md` 剩余字段 + **用户确认业务优先级** (规则 E)
- [ ] **Phase 1 调研** (范本 `03_research.md`): 八问八答聚焦 OpenAI File Search RAG 机制
  - chunk 策略: size? overlap?
  - embeddings 模型: text-embedding-3-*?
  - 检索 top-K: 默认几个?
  - GPT Store 发布前是否需 review?
- [ ] **Phase 2 策略 + PLAN** (范本 `04_plan.md` + `05_solution.md`): 写 `docs/PLAN.md` + 设计 `merge_for_chatgpt.py`
- [ ] **Phase 3 落地** (预计 2 批):
  - Batch 1: P0 合并 (1-4) + smoke test 3-5 题
  - Batch 2: P1-P2 合并 (5-9) + 完整 A/B 矩阵
- [ ] **Phase 4 审查** (范本 `06_review.md`): 三 lane + 10-15 题 A/B 矩阵 (包含 Conversation Starters 预设命中率)
- [ ] **Phase 5 收束** (范本 `09_closure.md`): RETROSPECTIVE + UPLOAD_TUTORIAL + 发布决策 (Private / 团队 / GPT Store)

---

## 4. 预设 Conversation Starters (Phase 3 配置, 初稿)

```
1. "AE 域的 AESER 变量定义是什么? 有哪些允许值?"
2. "RELREC 是什么? 什么场景下需要用它?"
3. "PC 和 PP 域之间是什么关系? 如何关联?"
4. "ISO 8601 日期格式在 SDTM 中有什么特殊规则?"
```

---

## 5. ChatGPT GPTs 独特优势 (相对 Claude Projects)

1. **公开分享** — 可发布到 GPT Store, Claude Projects 不支持公开链接
2. **Custom Actions** — 可接外部 API (e.g. NCI EVS Browser 直连)
3. **Conversation Starters** — 降低新用户上手门槛
4. **20 文件硬限强制合并** — 相比 Claude 19 文件的实测留了对照基线

---

## 6. A/B 矩阵重点 (相对 Claude 的侧重差异)

| 维度 | Claude Projects | ChatGPT GPTs |
|------|-----------------|--------------|
| RAG 衰减 | 重点 (容量不透明) | 次要 (硬限清晰) |
| 跨 chunk 检索准确度 | 次要 (文件级索引) | **重点** (embeddings 检索, 表格易断) |
| 公开分享语气 | N/A | **重点** (Store 观众 vs 团队) |
| Conversation Starter 命中率 | N/A | **重点** (新用户首次体验) |
| 边界诚实 | 重点 | 重点 (继承 Claude 经验) |

---

## 7. 验收标准 (Phase 5 回填)

- [ ] 7 类路由问题 14/14 回答准确
- [ ] 引用变量名 / 域名 / 章节号 正确
- [ ] 术语查表返回完整 codelist 值
- [ ] 跨域关联查询找到相关 RELREC / SUPP 规则
- [ ] 边界题零臆造 (参照 Claude v2 T18/T22 验证模式)
- [ ] 4 个预设 Conversation Starters 首答 PASS

---

## 8. 失败模式预判 (Phase 0 初稿, 会在 research 后更新)

| 失败 | 缓解 |
|------|------|
| 合并后表格被 chunker 切断 | md-heading 分段 + TableAware (P13) |
| 跨 chunk 检索表格断裂 | Instructions 强调路由优先级 "数据查 `domain_examples_all.md`" |
| GPT Store 公开被意外搜索 | 先 Private 测试, 按需公开 |
| 20 文件合并后单文件 >512MB | terminology 再拆 (e.g. questionnaires 按字母分 2 文件) |

---

*来源: 原 ROADMAP (2026-04-16 编写) + 2026-04-20 按 `_template/` 升级.*
