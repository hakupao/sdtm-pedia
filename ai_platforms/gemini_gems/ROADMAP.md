# Gemini Gems — 行进路线

> 状态: **待开始** (范本就绪, 等 Phase 0 启动)
> 着重方向: 大范围探索 + 全域对比 + 长上下文全量
> 平台: Gemini Advanced — Gems
> Tier 等级: **Tier 1-2** (预计 3-8 步, 半天-1 天; 本系列最轻量平台)
> 范本: [`../_template/`](../_template/) — 启动时读 [APPLY_CHECKLIST.md](../_template/APPLY_CHECKLIST.md)
> 平台特化画像: [docs/platform_profile.md](docs/platform_profile.md) (Phase 0 初稿)
>
> **终态文档** (Phase 5 收束后会有):
> - `docs/PLAN.md` / `docs/RETROSPECTIVE.md` / `current/UPLOAD_TUTORIAL.md` / `dev/test_results.md`

---

## 1. 平台特性 (Phase 0 初稿)

详见 [docs/platform_profile.md](docs/platform_profile.md). 核心要点:

- **检索方式**: 全量加载到超长上下文 (1M+ tokens). **无 RAG, 无检索**
- **容量限制**: 单文件数百 MB, 上下文窗口 1M tokens
- **上下文**: 全量可见, 窗口最大
- **分享**: **仅个人使用** (不支持团队 / 公开)
- **独有能力**: 全域对比 / 大规模模式识别 / 跨域探索性查询 (Claude/ChatGPT 都做不到)

---

## 2. 内容策略 (Phase 2 初稿, 会在 PLAN 里迭代)

1M 窗口可容纳全部核心知识 (~513K tokens), 甚至含部分 terminology.

| 内容 | tokens | 包含 |
|------|-------|------|
| chapters/ (6 文件) | ~62K | 全部 |
| model/ (6 文件) | ~18K | 全部 |
| 导航层 (ROUTING/INDEX/VAR_INDEX) | ~40K | 全部 |
| 63 spec.md | ~168K | 全部 |
| 63 assumptions.md | ~60K | 全部 |
| 63 examples.md | ~165K | 全部 |
| **核心合计** | **~513K** | — |
| terminology/core/ (高频) | ~200K | 可选 |
| **含高频术语合计** | **~713K** | 仍在 1M 窗口内 |

**合并粒度**: 3-5 个主题文件 (单批全上)

| # | 目标文件 | 内容 |
|---|---------|------|
| 1 | `core_reference.md` | chapters + model + 导航层 (~120K tokens) |
| 2 | `domain_specs.md` | 63 spec.md (~168K tokens) |
| 3 | `domain_knowledge.md` | 63 assumptions + 63 examples (~225K tokens) |
| 4 | `terminology_core.md` | 高频 codelist (~200K tokens, 可选) |

### 本平台独有约束 (P11-P12)

- **P11 单批到位**: 1 批上传全部文件, **不需要**渐进拐点测试 (相对 Claude 5+1 批)
- **P12 全量注入 ≠ 零衰减**: 虽然无 RAG, 但**长上下文末尾召回**可能衰减 (Gemini 类平台已知问题), A/B 必验末尾内容

---

## 3. 执行步骤 (按范本 Phase 0-5, 压缩版)

- [ ] **Phase 0 启动** (范本 `02_workflow.md`): 填完 `docs/platform_profile.md` + **用户确认优先级** (规则 E)
- [ ] **Phase 1 调研** (范本 `03_research.md`, 3 问简化版):
  - 1M 窗口是否真的全量可用, 有无 chunk 退化?
  - 长上下文末尾召回衰减程度?
  - Gems 分享/协作限制官方文档?
- [ ] **Phase 2 策略 + PLAN** (范本 `04_plan.md` + `05_solution.md`): 写 `docs/PLAN.md` + 设计 `merge_for_gemini.py` (可复用 ChatGPT 合并脚本)
- [ ] **Phase 3 落地** (1 批即全上):
  - 合并生成 3-5 主题文件
  - 一次性上传到 Gem
  - 终态 A/B
- [ ] **Phase 4 审查** (范本 `06_review.md`): 10 题 A/B (侧重全域对比 + 末尾召回)
- [ ] **Phase 5 收束** (范本 `09_closure.md`): RETROSPECTIVE + UPLOAD_TUTORIAL

**预计壁钟**: 半天-1 天 (Tier 1-2, 相比 Claude ~3 天轻量很多)

---

## 4. Gemini Gems 独特优势 (相对 Claude/ChatGPT)

1. **全域 assumptions + examples 同时在上下文** — Claude/ChatGPT 做不到 (容量不够或 RAG 不会同时命中)
2. **跨域模式识别** — "哪些域有共享 examples section?" 可以直接回答
3. **大规模对比** — "比较 Events 类 7 个域的 assumptions 结构差异" 一次出答案
4. **探索性查询** — 不确定答案在哪个文件时, Gemini 可全量搜索

---

## 5. A/B 矩阵重点 (Phase 2 设计, 初稿)

| 维度 | Claude | ChatGPT | **Gemini** |
|------|--------|---------|-----------|
| RAG 衰减 | 重点 | 次要 | N/A (无 RAG) |
| 跨 chunk 检索 | 次要 | 重点 | N/A |
| **全域对比** | 次要 | 次要 | **重点** (本平台独有) |
| **跨域模式识别** | 有限 | 有限 | **重点** |
| **长上下文末尾召回** | N/A | N/A | **重点** (Gemini 已知衰减区) |
| 边界诚实 | 重点 | 重点 | 重点 (继承) |

### Phase 2 A/B 矩阵初稿 (10 题)

1. 全域变量分布: "所有域中哪些使用了 EPOCH 变量? 列出 Core 属性差异"
2. 跨域 assumptions 搜索: "哪些域的 assumptions 提到了 RELREC?"
3. 共享 section 识别: "哪些域的 examples 中包含 SUPP 补充数据集?"
4. 模式识别: "EX/EC, MB/MS, TU/TR, PC/PP 四对域的 examples section 有什么相似结构?"
5. 长上下文末尾: 末段某 codelist 精确 Term (检验末尾召回)
6. 跨域推理: "比较 Events 类 7 个域的 assumptions 结构"
7. 规则推导 (继承 Claude): PC↔PP RELREC 4 种方法
8. 边界诚实 (继承 Claude): AERELN codelist 全部 Synonyms (应声明未收录)
9. 变量定义精确查询: AESER 允许值
10. Codelist 全表 (如 core/ 已 inline): C66742 完整 Term 表

---

## 6. 验收标准 (Phase 5 回填)

- [ ] 全域变量分布查询准确 (对比 VARIABLE_INDEX.md)
- [ ] 跨域 assumptions 搜索结果完整
- [ ] examples 模式识别能发现共享 section (EX/EC, MB/MS, TU/TR, PC/PP)
- [ ] 长上下文下回答质量不降级 (末尾召回 PASS)
- [ ] 边界题零臆造

---

## 7. 失败模式预判 (Phase 0 初稿)

| 失败 | 缓解 |
|------|------|
| 长上下文末尾召回衰减 | 关键内容前置 (导航层放头部, terminology 尾部) |
| 1M 窗口接近上限后响应变慢 / truncate | Phase 3 上传后测极长查询响应时间 |
| 上下文稀释 (太多无关内容同时在) | Instructions 强调 "按子段引用, 不要全扫" |
| 跨域推理硬编码 (Gemini hallucinate 倾向) | A/B 必含"零臆造"测试题 |

---

## 8. 后续可选扩展 (未排期)

- **terminology 全量注入**: 若 1M 窗口余量够, 可把 ~1.9M 的 terminology 也塞一部分进去 (需拆 2 个 Gem 或按套餐升级)
- **Gems 分享**: 若官方开放分享机制 (当前仅个人), 按需重部署

---

*来源: 原 ROADMAP (2026-04-16 编写) + 2026-04-20 按 `_template/` 升级.*
