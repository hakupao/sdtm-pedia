# 03 前置调研 — 八问八答模板

平台未知行为的主动探查. Phase 1 必做 (Tier 2/3) 或简化为 3 问 (Tier 1).

---

## 为什么要做调研

AI 平台的官方文档常常漏掉关键量化定义 (e.g. Claude Projects 的 "capacity %" 官方从未公开精确公式). PLAN 如果基于错误假设, 执行一半才发现偏差, 回滚成本极高.

**反例**: Claude v1 基于 "200K 硬约束" 假设做压缩设计, Step 14 上传后 UI 显示 12%, 差 8 倍 — 这就是漏掉调研的代价 (详见 `claude_projects/docs/capacity_research.md`).

---

## 八问八答模板 (填空)

> 每问**必附官方文档链接或社区实测链接**. 无来源的断言视为 hallucinate, 不采信.

### Q1: 平台 "capacity" / "limit" 的官方定义是什么?

**答**:

**来源**:
- [官方文档链接]
- [社区实测链接]

---

### Q2: 当前容量上限是多少? 不同套餐差异?

**答**: (填下表)

| 套餐 | Context window | Knowledge 容量 | RAG 扩展 | 文件数 | 单文件大小 |
|------|---------------|---------------|---------|--------|-----------|
| Free | | | | | |
| Pro/Plus | | | | | |
| Team | | | | | |
| Enterprise | | | | | |

**来源**: [链接]

---

### Q3: 历史上限调整过吗?

**答**: (查 release notes / changelog)

**来源**: [链接]

---

### Q4: 文件是全量注入 context 还是 RAG 检索?

**答**: (两种模式都存在? 阈值?)

| 模式 | 触发条件 | 检索方式 |
|------|---------|---------|
| 小项目 | (e.g. 总内容 < context window) | 全量注入 |
| 大项目 | (e.g. 超过 context window) | RAG 分片 |

**来源**: [链接]

---

### Q5: UI 上的 "Indexing" / 状态指示器是否可靠?

**答**: (可靠 / 不可靠 / 仅某些场景可靠)

**实测方法**: 上传后立即提问新文件内容, 看是否命中 vs 状态指示器显示什么.

**来源**: [链接 + 本次实测记录]

---

### Q6: 本平台的 Knowledge 和其他机制 (API / Memory / Persistent Storage) 是同一概念吗?

**答**: (区分开)

| 功能 | 位置 | 对象 | 用途 | 是否本次使用 |
|------|------|------|------|-------------|
| Knowledge / Project Files | | | | |
| API Files | | | | |
| Memory | | | | |
| Custom Instructions | | | | |

**来源**: [链接]

---

### Q7: 分享机制: 个人 / 团队 / 公开哪些支持?

**答**:

| 分享模型 | 支持? | 限制 |
|---------|------|------|
| 私有 (仅自己) | | |
| 团队内共享 | | |
| 组织内共享 | | |
| 公开链接 | | |
| Marketplace 发布 | | |

**来源**: [链接]

---

### Q8: 本地 token 统计 和 平台 UI token 统计 一致吗? (Calibration 偏差)

**答**: (做一次 known-N calibration)

**Calibration 实验** (推荐做):

1. 在空白平台实例上传一个已知 N tokens (e.g. 50K) 的简单 .md 文件
2. 记 UI 显示的 capacity % (e.g. 5%)
3. 推导 UI token 比例系数: `k = (100% capacity 对应 tokens) / (50K / 5%)`
4. 换 2 组不同 N (100K, 200K) 重复, 验证 k 稳定性

**本次实测结果**:
- k = ... (e.g. ~1.00 线性 or ~0.14x subsublinear)
- 偏差原因推测: (e.g. UI 元数据 / 内部索引开销)

**来源**: 本次 calibration 实验

---

## 对 PLAN 的修订

调研完成后, 把对原 PLAN 假设的修订**集中列**在本文件末尾:

| # | 原假设 | 调研后事实 | 修订 |
|---|-------|-----------|------|
| 1 | (e.g. "容量 200K 硬约束") | (e.g. "paid 套餐 RAG 自动扩 10x") | PLAN §1 去掉 "<200K" gate, 改为容量 0% → 90% 分批扩容 |
| 2 | ... | ... | ... |

---

## Tier 1 简化版 (3 问)

如果 Tier 1 小平台跳过完整八问, 至少答 3 问:

1. **容量上限是什么单位, 多少?** (文件数 / tokens / MB)
2. **分享机制最高能到什么? (私有 / 团队 / 公开)**
3. **索引指示器可靠吗? (需不需要等)**

---

## 输出

填完的文件放: `<platform>/docs/research.md` 或 `<platform>/docs/capacity_research.md`.

在 PLAN §1 或 §0 修订记录里**显式引用本文件**, 证明 PLAN 决策有事实基础.

---

## 示例: Claude Projects 八问八答 (已做, 供参考)

见 `claude_projects/docs/capacity_research.md`. 典型发现:

- **Q1 回答**: Anthropic 从未公开量化定义. 百分比条不是 200K 刻度.
- **Q4 回答**: paid 套餐自动开 RAG, 本地 tiktoken 192K 显示 12%, 推算分母约 3-4M tokens 等值
- **Q5 回答**: Indexing indicator 全程不可信, 以"直接试问命中"判可用
- **对 PLAN 的修订**: 原 PLAN "200K 硬约束" 假设错误, 改为 5 批 + 1 重平衡批渐进到 77% capacity

---

*来源: claude_projects/docs/capacity_research.md 格式 + v1 G3 缺口暴露.*
