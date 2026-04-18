# Claude Projects "Capacity" 调研报告

> 创建日期: 2026-04-18
> 触发: Step 14 容量实测显示 12%, 与 PLAN 预期 95-98% 偏差 8 倍
> 调研者: Claude (document-specialist subagent)
> 用途: 修订 PLAN.md "200K 硬约束" 假设, 指导 Phase 7 扩容决策

---

## 1. 触发问题

PLAN.md §1.2 / 附录 A 假设 "Claude Project 容量上限 ~200K tokens"。Step 13 上传 9 个文件 (本地 tiktoken 实测 192,036 tokens) 后, UI 显示 **"12% of project capacity used"**, 而非预期的 95-98%。差 8 倍。

---

## 2. 核心结论 (TL;DR)

**Anthropic 从未公开 "project capacity" 的精确定义。** 200K = 100% 的假设错误。基于社区实测推算, capacity 分母约 **3-4M tokens 等值** (73K tokens 实测显示 2%)。192K 显示 12% 与新模型吻合。

---

## 3. 八问八答 (附官方来源)

### Q1: "Project capacity" 的官方定义是什么?

官方文档**没给量化定义**。RAG 文章只说 "total content must fit within Claude's context window" + "visual indicator showing project is RAG-enabled", 未解释百分比怎么算。

- 官方: [Uploading files to Claude](https://support.claude.com/en/articles/8241126-uploading-files-to-claude)
- 官方: [RAG for Projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)
- 第三方实测: [Simon Willison, June 2024](https://simonwillison.net/2024/Jun/25/claude-projects/)

### Q2: 当前 Projects 容量上限是多少?

| 套餐 | Context window | RAG 扩展 |
|------|----------------|---------|
| Free | 200K tokens (~500 页) | 无 (paid 才有 RAG) |
| **Pro / Max** | 200K tokens, **RAG 自动扩容到 10x** | 有 |
| Team / Enterprise | 200K tokens (部分模型 500K), RAG 10x | 有 |

注: capacity 百分比条**不是按 200K tokens 刻度计算**。

- 官方: [Context window on paid plans](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)
- 官方: [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)

### Q3: 历史上这个上限调整过吗?

**官方 release notes 中没有任何关于 project knowledge 容量变更的条目。** 没找到 "已从 200K 扩容到 1.5M" 的官方声明。

- 官方: [Release Notes](https://support.claude.com/en/articles/12138966-release-notes)

### Q4: 文件是全部注入 context window 还是 RAG 检索?

**两种模式都存在, 取决于项目规模:**

- **小项目 (未超 context window)**: 全部内容直接粘贴进 context, 每次对话完整注入
- **大项目 / 文件多**: 切换到 RAG, 用 "project knowledge search tool" 只检索相关片段。官方原话 "automatically activates when your project approaches or exceeds the context window limits"

→ "capacity" 在两种模式下语义不同:
- 小项目模式: 能塞进 context 的总 token 量
- RAG 模式: 索引集合规模

### Q5: UI 上的 "Indexing" 标签是什么含义?

**官方文档未明确解释。** RAG 文章只提 "visual indicator showing project is RAG-enabled", 没说 indexing 进行中和完成的行为差异。

社区观察 + 我们 Step 14 Smoke Test 实测: **"Indexing" 标签长时间不消失是前端 stale state, 后端检索已可用** (我们的 9 个文件全部能搜到)。

### Q6: Project Knowledge vs Files API vs Memory 是同一概念吗?

**不是。明确区分:**

| 功能 | 位置 | 对象 | 用途 |
|------|------|------|------|
| **Project Knowledge** | claude.ai 网页 UI | 消费者/团队 | Project 内上传, 跨对话持久化, **自动 RAG** |
| **Files API** | platform.claude.com API (beta) | API 开发者 | 上传获 file_id, Messages 请求复用, **不带 RAG** |
| **Memory** | claude.ai | 消费者 | 跨对话记住偏好, 与文件无关 |

Files API 限制: 单文件 ≤500MB, 组织总存 500GB, 内容按 input tokens 计费。

- 官方 Files API: [platform.claude.com/docs/en/build-with-claude/files](https://platform.claude.com/docs/en/build-with-claude/files)

### Q7: 单文件大小 / 文件数上限?

| 场景 | 单文件 | 文件数 |
|------|-------|-------|
| Claude.ai 单次对话 | 30MB | 20 个 |
| **Claude.ai Project Knowledge** | **30MB** | **无明确上限** (受 context window 约束) |
| Files API | 500MB | 受 500GB 总量约束 |

### Q8: 官方最佳实践建议?

只有泛泛建议: 用有意义文件名 / 同一 project 归组相关文档 / 提问时明确指定文档名。**没有 "不要超 X 文件 / Y tokens" 的具体阈值。**

- 官方: [Create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)

---

## 4. 关键社区证据

### 4.1 Simon Willison 实测 (2024-06)

Projects 发布时上传 ~693KB 文档, UI 显示 "63% of knowledge size used"。当时是**直接注入 context window 模式**, 63% ≈ 126K tokens (200K 基准)。

- 来源: [Simon Willison, June 2024](https://simonwillison.net/2024/Jun/25/claude-projects/)

### 4.2 GitHub Issue #25759 (2026-02) — **核心证据**

实测记录:
- 13 文件 / 73K tokens → UI 显示 **2%**, RAG 已激活
- 12 文件 / 73K tokens → UI 显示 **1%**, RAG 未激活

**反推**: 73K / 2% = **3,650,000 tokens (~3.65M)**

Anthropic 标 "invalid / not planned" 关闭, 无技术解释。

- 来源: [Issue #25759](https://github.com/anthropics/claude-code/issues/25759)

### 4.3 我们 Step 14 实测 (2026-04-17/18)

- 9 文件 / 192K tokens → UI 显示 **12%**, RAG 已激活
- 反推: 192K / 12% = **1,600,000 tokens (~1.6M)** 或更高

(与 #25759 的 3.65M 量级一致, 差异可能源于"capacity 同时受 token 和文件数双重影响"。)

---

## 5. 对 Phase 6.5 Claude 路线的影响

### 5.1 旧假设 vs 新认识

| 项 | 旧假设 (PLAN.md) | 新认识 (本研究) |
|---|---|---|
| 容量上限 | 200K tokens (硬约束) | RAG 模式下 ~3-4M tokens 等值 |
| 192K 实测 | 应显示 ~96% | 实测 12%, 符合 RAG 模型 |
| 检索机制 | 全量塞 context | **RAG 自动接管** (实测确认) |
| Phase 7 扩容空间 | 几乎没有 | **巨大 (剩余 ~88%)** |
| 边界模板必要性 | 必需 | 可保留作兜底, 但前提理由变了 |

### 5.2 PLAN.md 哪些假设站不住

1. **§1.2 "核心矛盾"** 表中 "200K tokens (硬约束)" → 应改为 "200K context window 限制, 但 paid 套餐 RAG 自动扩 10x"
2. **§3.3 Token 预算 "硬约束 ≤195K"** → 实际 ≤195K 不是硬约束,而是 "保证不触发 RAG 模式" 的软约束。我们已经触发 RAG 但工作正常
3. **§3.2 决策 D3/D4 (examples 降级 / terminology 降级)** → 动机段需要重写: 不是 "因为 200K 装不下", 而是 "因为价值密度低 + 当时不知道 RAG 容量"
4. **附录 A "Claude Project 容量: ~200K tokens"** → 应改为 "Project context window 200K, RAG 模式下索引容量 ~3-4M"

### 5.3 实际工作有没有失败?

**没有。** 即使前提假设错了, 压缩工作仍然成功:
- 9 文件全检索可达 (Smoke + T1-T8 全 PASS)
- 边界模板正确触发 (T6/T7/T8 标杆答案)
- System Prompt 路由规则有效

但代价是: **过度压缩**。examples 数据表 / terminology Term 值原文被剔除, T3/T6/T7 出现间接重建场景, 损失了"原文级精确度"。

---

## 6. 给 Phase 7 的建议

### 6.1 优先扩回的内容 (按性价比)

| # | 加回内容 | 理由 | 预计 token |
|---|---------|------|----------|
| 1 | ch06 完整 + ch08 §8.3 完整 | T3 暴露的间接重建场景 (PP↔PC RELREC) | +30-50K |
| 2 | examples 数据表 (有代表性的, 比如 AE/PC/PP/MB 的核心 Examples) | T6 可不再触发边界模板 | +50-100K |
| 3 | terminology Term 值原文 (高频 codelist 优先, 如 C66742/C71620/C74456) | T7/T8 可直接给精确值 | +200-500K |
| 4 | ch01/02/03/08/10 完整版 (撤销精简) | 提升路由准确性 | +30-50K |

总扩容 ~300-700K, 仍远低于 RAG 模式 ~3-4M 上限。**RAG 检索质量随集合增大可能下降**,需在 Phase 7 实测 T1-T8 + 新增测试样本验证。

### 6.2 必须保留的设计

- **System Prompt 边界处理模板** → 即使全文加回, 仍作为 "超纲问题" 兜底
- **源路径标注 (`<!-- source: ... -->`)** → 跨文件追溯刚需
- **System Prompt 路由规则** → RAG 检索基础上 + 显式路由提升精确度

### 6.3 需要进一步求证的疑点

1. **capacity 分母到底是 token 还是 storage (字节)?** 可对照实验: 传纯英文 vs 中英混合 vs 二进制附件, 看百分比变化
2. **RAG 检索质量随集合大小如何衰减?** 加回内容前必须建立 baseline (当前 T1-T8 PASS 状态), 扩容后回归测试
3. **"Indexing" 标签有没有真正完成的标志?** 长时间不消失到底影响什么
4. **是否值得发 support ticket 问 Anthropic 官方** capacity 计算公式? (低优先, 官方过往不回复此类问题, 见 Issue #25759)

---

## 7. 决策记录

基于本调研, 立即行动:

1. ✅ 归档本研究文档 (`capacity_research.md`)
2. ✅ 更新 PLAN.md §1.2 / §3.3 / 附录 A 的"200K 硬约束"前提说明 (postscript 形式, 不重写历史决策)
3. ✅ 更新 `CLAUDE.md` Key Paths 表加入本文档
4. ⏸ Phase 7 扩容方案 (待用户确认后启动, 不在本次操作范围)

---

## 附录: 完整官方来源清单

- [Uploading files to Claude](https://support.claude.com/en/articles/8241126-uploading-files-to-claude)
- [RAG for Projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)
- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [Create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [Context window on paid plans](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)
- [Files API docs](https://platform.claude.com/docs/en/build-with-claude/files)
- [Release Notes](https://support.claude.com/en/articles/12138966-release-notes)

非官方实测来源:

- [Simon Willison, June 2024 — Claude Projects launch analysis](https://simonwillison.net/2024/Jun/25/claude-projects/)
- [GitHub Issue #25759 — Project files switch to RAG at 2% capacity](https://github.com/anthropics/claude-code/issues/25759)
