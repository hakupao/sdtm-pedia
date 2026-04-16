# Claude Projects — 行进路线

> 状态: **待开始**
> 着重方向: 精确查询 + 规则推理
> 平台: Claude Pro — Projects

## 平台特性

- **检索方式**: 全量加载到上下文（不做 RAG 分片）
- **容量限制**: Project Knowledge 约 200K tokens (~50 万英文字符)
- **上下文**: 全量可见，精确度最高
- **分享**: 仅个人/组织内使用
- **适合**: 精确引用、规则推导、跨域关联分析、数据集校验讨论

## 内容策略

Project Knowledge 约 200K tokens，需要精选内容。

### 策略 A: 最大化覆盖 (~288K tokens，需实测是否超限)

| 内容 | tokens | 包含 |
|------|--------|------|
| chapters/ (6 文件) | ~62K | 全部 |
| model/ (6 文件) | ~18K | 全部 |
| ROUTING.md | ~3K | 全部 |
| INDEX.md | ~3K | 全部 |
| VARIABLE_INDEX.md | ~34K | 全部 |
| 63 个 spec.md | ~168K | 全部 (含 Cross References) |
| **合计** | **~288K** | — |

如超限，降级方案:
- 去掉 VARIABLE_INDEX.md → ~254K tokens
- 仍超则去掉低频域 spec.md (OI, RELSUB, RELSPEC, SS 等)

### 策略 B: 保守精简 (~120K tokens)

| 内容 | tokens | 包含 |
|------|--------|------|
| chapters/ | ~62K | 全部 |
| model/ | ~18K | 全部 |
| ROUTING.md + INDEX.md | ~6K | 全部 |
| 高频域 spec.md (20-30 域) | ~40-60K | AE, CM, DM, DS, EG, EX, LB, MH, VS, PE 等 |
| **合计** | **~106-146K** | — |

### 推荐: 先试策略 A，超限则降级

## 执行步骤

### Step 1: 编写 Project Instructions (System Prompt)

- [ ] 角色定义: SDTM/CDISC 标准专家
- [ ] 嵌入 ROUTING.md 的 7 类路由规则（压缩版）
- [ ] 回答规范: 引用变量名 + 域名 + 章节号 + 页码
- [ ] 跨域查询指导
- [ ] 处理知识边界: assumptions/examples/terminology 不在上下文时的提示语
- [ ] 保存为 `output/system_prompt.md`

### Step 2: 准备上传文件

- [ ] 直接使用 knowledge_base/ 中的原文件（无需合并）
- [ ] 按策略 A 清单逐个上传
- [ ] 如遇容量限制，记录实际上限并降级到策略 B
- [ ] 记录最终上传文件清单

### Step 3: 创建 Project

- [ ] 在 Claude 创建新 Project
- [ ] 粘贴 System Prompt
- [ ] 上传 Project Knowledge 文件
- [ ] 测试基础查询

### Step 4: 测试 + 调优

- [ ] 测试精确查询: 变量定义、Core/Role 属性
- [ ] 测试规则推导: "如果 AE 有多个严重程度变化，应该如何记录？"
- [ ] 测试跨域分析: "PC 和 PP 如何通过 RELREC 关联？有几种方法？"
- [ ] 测试边界情况: 查询 terminology (不在上下文中) 时是否正确提示
- [ ] 调优 System Prompt

## Claude Projects 的独特优势

1. **ROUTING.md 完美适配** — 全量上下文 + 路由规则 = 精准定位
2. **规则推导** — ch04 General Assumptions 全在上下文中，可以做复杂推理
3. **Cross References 链式追踪** — spec.md 末尾的交叉引用可以直接跳转
4. **VARIABLE_INDEX 反向查询** — "哪些域有 EPOCH 变量？" 直接查表

## 验收标准

- [ ] 变量定义查询 100% 准确（上下文中有 spec.md）
- [ ] 规则推导引用正确的 ch04 章节号
- [ ] 跨域查询能追踪 Cross References 到相关域
- [ ] 不在上下文中的内容(terminology/examples)不编造，而是提示用户
