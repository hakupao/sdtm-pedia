# ChatGPT GPT — 行进路线

> 状态: **待开始**
> 着重方向: 全量覆盖 + 团队分享
> 平台: ChatGPT Plus/Team — GPTs (Custom GPTs)

## 平台特性

- **检索方式**: 内置 RAG（自动分片 → Embedding → 检索相关片段）
- **文件限制**: 20 个文件，单文件可达 512MB，总量无硬性上限
- **上下文**: 检索到的片段注入上下文，非全量
- **分享**: 可发布为公开/团队/私有 GPT
- **适合**: 大文件量、术语查表、团队共享

## 内容策略

将 295 个文件合并为 **8-10 个文件**上传:

| # | 文件名 | 来源 | 大小 | 优先级 |
|---|--------|------|------|--------|
| 1 | `navigation.md` | ROUTING.md + INDEX.md + VARIABLE_INDEX.md | ~159 KB | P0 |
| 2 | `chapters_all.md` | chapters/ 6 文件合一 | ~246 KB | P0 |
| 3 | `model_all.md` | model/ 6 文件合一 | ~70 KB | P0 |
| 4 | `domain_specs_all.md` | 63 个 spec.md 合一 | ~672 KB | P0 |
| 5 | `domain_assumptions_all.md` | 63 个 assumptions.md 合一 | ~240 KB | P1 |
| 6 | `domain_examples_all.md` | 63 个 examples.md 合一 | ~661 KB | P1 |
| 7 | `terminology_core.md` | terminology/core/ 42 文件合一 | ~3.2 MB | P2 |
| 8 | `terminology_questionnaires.md` | terminology/questionnaires/ 43 文件合一 | ~3.8 MB | P2 |
| 9 | `terminology_supplementary.md` | terminology/supplementary/ 6 文件合一 | ~0.6 MB | P2 |

## 执行步骤

### Step 1: 编写合并脚本 (Python)

- [ ] 编写 `merge_for_chatgpt.py`
- [ ] 每个合并段标注原文件路径 (`<!-- source: domains/AE/spec.md -->`)
- [ ] 合并后文件自动校验: 段数 == 源文件数
- [ ] 输出到 `output/`

### Step 2: 编写 GPT Instructions

- [ ] 基于 ROUTING.md 编写 System Prompt
- [ ] 定义角色: SDTM 标准咨询专家
- [ ] 定义回答规则: 引用具体变量名、指向域名、标注 PDF 来源
- [ ] 特别处理: 跨域查询指导 (PC↔PP, EX↔EC, TU↔TR, FA↔源域)
- [ ] 保存为 `output/instructions.md`

### Step 3: 上传 + 配置

- [ ] 在 ChatGPT 创建 GPT
- [ ] 上传 P0 文件 (1-4) 并测试基础查询
- [ ] 上传 P1 文件 (5-6) 并测试 assumptions/examples 查询
- [ ] 上传 P2 文件 (7-9) 并测试术语查询
- [ ] 配置 Conversation Starters (预设问题)

### Step 4: 测试 + 调优

- [ ] 测试 7 类路由问题各 2 例 (14 题)
- [ ] 测试跨域关联查询 (3 题)
- [ ] 记录检索质量问题
- [ ] 调优 Instructions 中的检索提示
- [ ] 决定是否发布为公开/团队 GPT

## 预设对话启动器 (Conversation Starters)

```
1. "AE 域的 AESER 变量定义是什么？有哪些允许值？"
2. "RELREC 是什么？什么场景下需要用它？"
3. "PC 和 PP 域之间是什么关系？如何关联？"
4. "ISO 8601 日期格式在 SDTM 中有什么特殊规则？"
```

## 验收标准

- [ ] 7 类路由问题 14/14 回答准确
- [ ] 引用的变量名/域名正确
- [ ] 术语查表返回正确的 codelist 值
- [ ] 跨域关联查询能找到相关 RELREC/SUPP 规则
