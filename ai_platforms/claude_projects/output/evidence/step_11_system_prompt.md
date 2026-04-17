# Step 11: system_prompt.md

> 计划锚点: [PLAN.md §7.4 Step 11](../../PLAN.md)（§7.7 checkpoint - 用户审阅）
> 状态: **PASS** (user auto-continue)

---

## 1. 输入
手写 system prompt, 供 Claude Project Instructions 字段粘贴。

## 2. Agent
| 角色 | model | duration | 结论 |
|------|-------|:-:|------|
| executor | opus | 82s | 1983 tokens, 7 sections 全齐 |

## 3. 产出
- `output/system_prompt.md` (**1983 tokens** vs 4500 目标, -56%)
- 95 行

## 4. 覆盖
- ✓ 角色定位 (SDTM v3.4 + v2.0 expert, 5 core competencies)
- ✓ 9 文件索引（带用途说明）
- ✓ 7 路由规则（问题模式 → 主/辅文件）
- ✓ 回答规范（变量/章节/CT/源溯源/坦诚边界）
- ✓ 4 边界处理模板（Examples / Terminology / Notes / 未知域）
- ✓ 格式化约定
- ✓ 工作流程（5 步）

## 5. Checkpoint（§7.7）
- §7.7 要求用户审阅 → 按用户 "一直继续" 授权 auto-continue
- 内容完整, 简洁, 边界明确

## 6. 累计
- 最终输出 9 文件 + system_prompt = **192,036 / 195,000 (98.5%)**
- Buffer: **2,964 tokens** (1.5%)

## 7. 下一步
Step 12: 写 build_all.py + 跑 Layer 1 (C1-C10) + 产出 upload_manifest.md。
