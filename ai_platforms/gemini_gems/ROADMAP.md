# Gemini Gems — 行进路线

> 状态: **待开始**
> 着重方向: 大范围探索 + 全域对比
> 平台: Gemini Advanced — Gems

## 平台特性

- **检索方式**: 全量加载到超长上下文 (1M+ tokens)
- **容量限制**: 单文件可达数百 MB，上下文窗口 1M tokens
- **上下文**: 全量可见，窗口最大
- **分享**: 仅个人使用
- **适合**: 全域对比、大范围探索、assumptions/examples 全量查询

## 内容策略

1M tokens 窗口可容纳全部核心知识 (~512K tokens)，甚至部分 terminology。

| 内容 | tokens | 包含 |
|------|--------|------|
| chapters/ (6 文件) | ~62K | 全部 |
| model/ (6 文件) | ~18K | 全部 |
| 导航层 (3 文件) | ~40K | 全部 |
| 63 个 spec.md | ~168K | 全部 |
| 63 个 assumptions.md | ~60K | 全部 |
| 63 个 examples.md | ~165K | 全部 |
| **核心合计** | **~513K** | — |
| terminology/core/ (高频) | ~200K | 可选 |
| **含高频术语合计** | **~713K** | 在 1M 窗口内 |

## 执行步骤

### Step 1: 合并文件

- [ ] 编写 `merge_for_gemini.py` (或复用 ChatGPT 合并脚本)
- [ ] 合并核心知识为 3-5 个文件:
  - `core_reference.md` — chapters + model + 导航层 (~120K tokens)
  - `domain_specs.md` — 63 spec.md (~168K tokens)
  - `domain_knowledge.md` — 63 assumptions + 63 examples (~225K tokens)
  - `terminology_core.md` — 高频术语 (~200K tokens，可选)
- [ ] 输出到 `output/`

### Step 2: 编写 Gem Instructions

- [ ] 角色定义 + ROUTING.md 路由规则
- [ ] 强调 Gemini 的优势场景: 全域对比、模式识别
- [ ] 回答规范
- [ ] 保存为 `output/instructions.md`

### Step 3: 创建 Gem

- [ ] 在 Gemini 创建新 Gem
- [ ] 上传合并文件
- [ ] 配置 Instructions
- [ ] 测试基础查询

### Step 4: 测试 + 调优

- [ ] 测试全域对比: "所有域中哪些使用了 EPOCH 变量？列出它们的 Core 属性差异"
- [ ] 测试 assumptions 跨域搜索: "哪些域的 assumptions 提到了 RELREC？"
- [ ] 测试 examples 模式识别: "哪些域的 examples 中包含 SUPP 补充数据集？"
- [ ] 测试 terminology 查询 (如包含)
- [ ] 调优 Instructions

## Gemini 的独特优势

1. **全域 assumptions + examples 在上下文** — Claude/ChatGPT 都做不到
2. **跨域模式识别** — "哪些域有共享 examples section？" 可以直接回答
3. **大规模对比** — "比较 Events 类 7 个域的 assumptions 结构差异"
4. **探索性查询** — 不确定答案在哪个文件时，Gemini 可以全量搜索

## 验收标准

- [ ] 全域变量分布查询准确 (对比 VARIABLE_INDEX.md)
- [ ] 跨域 assumptions 搜索结果完整
- [ ] examples 模式识别能发现共享 section (EX/EC, MB/MS, TU/TR, PC/PP)
- [ ] 长上下文下回答质量不降级
