# Claude Projects — 行进路线

> 状态: **已完成** (v1 2026-04-18 / v2 终态 v2.6 2026-04-20)
> 着重方向: 精确查询 + 规则推理
> 平台: Claude Pro — Projects
> **实际产出**: v1 192K tokens (9/9 PASS) → v2.6 1,286,161 tokens / 19 文件 / capacity 77% / 24/24 A/B PASS / 0 衰减全程
> **目录 reorg (2026-04-20)**: 重组为 current/docs/dev/archive 四层, 见 [README.md](README.md)
> **终态文档** (reorg 后路径):
> - [docs/PLAN_V2.md](docs/PLAN_V2.md) / [docs/RETROSPECTIVE_V2.md](docs/RETROSPECTIVE_V2.md) / [docs/rag_decay_curve.md](docs/rag_decay_curve.md) / [docs/phase7_handoff.md](docs/phase7_handoff.md)
> - [archive/RETROSPECTIVE.md](archive/RETROSPECTIVE.md) (v1 复盘) / [archive/v1/docs/PLAN.md](archive/v1/docs/PLAN.md) (v1 计划)

## 平台特性

- **检索方式**: 全量加载到上下文 — 修正: Claude Projects **paid 套餐会自动开 RAG 分片** (详见 `capacity_research.md`), 不是纯全量注入
- **容量限制**: UI 显示 Project Knowledge ~200K tokens, 但实测 paid 套餐支持 ~1.5M tokens (本次 v2.6 push 到 77% = 1.29M 仍零衰减)
- **上下文**: 全量可见, 精确度最高
- **分享**: 仅个人/组织内使用
- **适合**: 精确引用、规则推导、跨域关联分析、数据集校验讨论
- **已知不可靠项**: UI "Indexing" indicator 全程 gating 不准, 以"直接试问命中"判可用

## 内容策略 (v2.6 终态实际采用)

本节保留初版 "策略 A/B" 仅供参考. **实际实施从 200K → 1.29M tokens 演进**, 见 PLAN_V2.md + RETROSPECTIVE_V2.md.

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

> **执行后实际情况** (2026-04-17 → 2026-04-20):
> - v1 实际走"方案 B 二次创作压缩"压到 192K (12% capacity), 9 文件, 8/8 PASS, 不是原规划的策略 A
> - v2 扩容后推到 1.29M tokens (77% capacity), 19 文件, 24/24 PASS, 已远超原策略 A/B 规划
> - 结论: 原策略 A/B 是 200K 硬约束假设下的设计, 实测 RAG 自动分片后容量 ~10x, 策略完全改写

## 执行步骤 (原规划, 实际已完成)

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

## 验收标准 (v2.6 终态全部满足 ✓)

- [x] 变量定义查询 100% 准确 (T1 AEDECOD Core, T4 EPOCH 44 域, T12 §4.4 Timing 等)
- [x] 规则推导引用正确的 ch04 章节号 (T11 §8.3 RELREC, T12 §4.4.8 等)
- [x] 跨域查询能追踪 Cross References 到相关域 (T3 PC↔PP RELREC 4 方法 v2.4 显式 Method A-D)
- [x] 不在上下文中的内容不编造, 正确提示用户 (T18 AERELN 边界 / T22 C65047 giant stub / T6 AE Ex2 数据)
- [x] 新增 v2 目标: 63 域 examples 全覆盖 + top 200 + mid 300 + core/supp tail 全 inline
- [x] 新增 v2 目标: RAG 衰减曲线量化 (7 数据点, 拐点 ≥77% 未触)
- [x] 新增 v2 目标: Phase 7 handoff 可执行 (6 actionable + 5 问题 + 5 步待办)

## 后续可选扩展 (当前未排期)

- v2.7+: quest 覆盖从 55.8% 推到 ~80% (quest 是用户最低优先级, ROI 低, 默认不做)
- v2.8+: 推到 85-90% capacity 做 RAG 衰减拐点实验
- Claude × Phase 7 RAG 混合: Phase 7 自建 RAG 跑通后再评估
- 团队分享: Claude Projects share 链接需手动生成 (平台不支持自动化)
