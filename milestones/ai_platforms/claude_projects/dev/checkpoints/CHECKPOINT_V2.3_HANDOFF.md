# Stage v2.3 Cowork 自动执行手册

> **给 Claude Cowork (computer-use / browser 模式) 执行.**
> Cowork 亲自点浏览器上传 1 个新文件 + 更新 Instructions + 跑 4 题 A/B, 返回结构化报告.

---

## 背景 (≤ 80 字)

Stage v2.3 给 v2 Project 再加 1 个文件 `10_examples_data_others.md` = 48,897 tokens (35 剩余 SDTM 域 examples 数据表, 与 v2.2 09 零 overlap). 63 SDTM 域现在 examples 侧全覆盖. 需验证 T15 (RP) / T16 (FT) 能原文命中 + T3 (PC↔PP RELREC 4 方法) 与 T11 (ch08 §8.3 RELREC) 回归是否稳定.

---

## 你 (Cowork) 的任务

在**已存在的 v2 Project** (`SDTM-Knowledge-v2`) 下:
1. Project Knowledge 新增上传 **1 个文件**: `output_v2/10_examples_data_others.md`
2. 覆盖更新 Project Instructions, 粘贴最新 `output_v2/system_prompt_v2.md` 全文 (比 v2.2 多 `<!-- stage v2.3 begin -->` 段)
3. 跑 4 题 A/B 测试
4. 返回 Markdown 结构化报告

**权限假设/目录**: 同 v2.2 handoff

---

## Step 1: 进入现有 v2 Project

1. 打开 `https://claude.ai`
2. 进入 **Projects** 列表, 打开 `SDTM-Knowledge-v2` (v2.2 已在, 含 10 文件)

---

## Step 2: 覆盖 Project Instructions

1. Instructions 编辑区
2. 读 `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/system_prompt_v2.md`
3. **全文覆盖粘贴**
4. 保存

注: 新增 `<!-- stage v2.3 begin -->` 段 (Examples 查询优先级升级为 `09 > 10 > 07`).

---

## Step 3: 上传 1 个新文件到 Project Knowledge

| # | 绝对路径 | 大小 (tokens) |
|---|---------|--------------|
| 1 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/10_examples_data_others.md` | **48,897** |

**合计 (v2.3 终态)**: 11 文件 / **367,489 tokens** (v2.2 10 × 318,592 + 1 新 × 48,897).

**不要上传 meta**: 同 v2.2 list (含本 handoff 文件). 不要重传 v2.2 的 10 文件.

---

## Step 4: 等 indexing + 记 capacity %

v2.3 预期 capacity ~25-27% (v2.2 20% + 预测 +5-7pp, 基于 v2.1→v2.2 +7pp 规律).
记下实测百分比 + indexing 用时.

---

## Step 5: 跑 4 题 A/B 测试

在同一 v2 Project 开**新对话**, 依次问 4 题:

### T15 (新增, 批 3 目标): RP 域 Example 数据?
期望: 原文引用 rp.xpt 表格 (含 RPTEST 多参数, 妊娠史场景), 不再兜底. RP examples.md 只 1 个 Example.

### T16 (新增, 批 3 目标): FT 域 Example 数据?
期望: 原文引用 ft.xpt 表格 (功能测试含步态/平衡/力量评估). FT examples.md 只 1 个 Example.

### T3 (回归 — 关键修复期望): PC↔PP 通过 RELREC 关联的 4 种方法?
**v2.1/v2.2 时 v2 拒答** (边界模板触发, §6.3.5.9.3 未收录). 本批 PC/PP 已在 09 (批 2 D2, Method A-D 虽丢失层级但数据表完整). 期望 v2.3 能:
- 直接引用 09 里的 15 张 relrec.xpt 表格
- 若未能自动推导出 "Method A-D" 四种方法, 至少能列出 relrec 数据表示例
- 判定标准: **↑ vs v2.1/v2.2** (任何改善都算) 或 **持平** (仍拒答但不恶化) 或 **↓** (更差)

### T11 (回归): ch08 §8.3 RELREC 数据集关系示例完整流程?
期望: 与 v2.2 答案一致 (ch08 在 02_chapters.md 没变, 应 0 衰减).

---

## Step 6: 评估每题精度

| 精度标签 | 说明 |
|---------|-----|
| **持平** | v2.2 和 v2.3 答案同质 |
| **↑** | v2.3 比 v2.2 更精确 |
| **↓** | v2.3 比 v2.2 差 |

对 T15/T16 额外: PASS (完整表格) / FAIL (兜底).
对 T3 额外: v2 累积视角 — PASS 条件放宽为 "能引用 09 里的 relrec 表" / FAIL = "仍拒答或更糟".
对 T11 额外: 持平 / ↓ (若 ↓ 即 5 文件引入后的回归衰减).

---

## Step 7: 返回最终报告

```markdown
# Stage v2.3 A/B 测试报告

> 执行日期: YYYY-MM-DD HH:MM
> Capacity (v2.3): XX%  (v2.2 参照: 20%)

## 上传确认
- [x] 10_examples_data_others.md 上传
- [x] system_prompt_v2.md 覆盖
- [x] Indexing 完成

## 4 题结果明细

### T15. RP 域 Example 数据
- **v2.2 答案**: (兜底, 未覆盖)
- **v2.3 答案**: [完整]
- **精度**: ↑ / 持平
- **T15 判定**: PASS / FAIL
- 说明: ...

### T16. FT 域 Example 数据
(同 T15 模板)

### T3. PC↔PP RELREC 4 方法 (v2.1 ↓ 历史)
- **v1 答案**: 声明不在 Project, 重建 3+1 方法 (推测)
- **v2.1 答案**: 严格拒答 (边界触发)
- **v2.2 答案**: (预期同 v2.1, 09 有 PC 数据但丢失 Method A-D 分层, 不确定能否自动恢复)
- **v2.3 答案**: [完整]
- **精度 vs v2.2**: ↑ / 持平 / ↓
- **说明**: 能否从 09 的 15 张 relrec.xpt 推导出 Method A-D? 还是仍给拒答?

### T11. ch08 §8.3 RELREC (回归)
(同 v2.2 模板, 期望 0 衰减)

## 汇总矩阵

| # | 题目简称 | 精度 vs v2.2 | PASS? |
|---|---------|------------|-------|
| T15 | RP Example | ↑/持平 | PASS/FAIL |
| T16 | FT Example | ↑/持平 | PASS/FAIL |
| T3 | PC↔PP RELREC 4 方法 (重测) | ↑/持平/↓ | — (观察变化) |
| T11 | ch08 §8.3 RELREC | 持平/↓ | — |

## 汇总
- 回归衰减 ↓ 数: N / 2 (T3, T11)
- 新增 PASS: K / 2 (T15, T16)
- 新增 FAIL: L / 2

## 关键观察
- T3 变化分析: 是否能从 09 的 PC relrec 数据推导出 Method A-D?
- T15/T16 是否命中 10 (新增) 而非兜底?
- capacity 爬升曲线是否匹配预期?

## 异常/警告
- 或 "无异常"
```

---

## 决策矩阵 (供主控参考)

| Cowork 报告 | 主控决策 |
|------------|---------|
| T11 无 ↓, T15+T16 ≥1 PASS | 继续 Task F1 (批 4 terminology 高频) |
| T11 无 ↓, T15+T16 全 FAIL | 回退 E1 调整算法 (低概率, 已见命中 09 的先例) |
| T11 有 ↓ | 立即停 (唯一回归衰减敏感题), 报告用户 |
| T3 出现任何改善 | 记入 RAG decay curve 作正向数据点 |
| 用户要暂停 | 暂停 |

---

## 不要做

- 不要自行登录 claude.ai
- 不要编造 Claude 的回答
- 不要修改 output_v2/ 任何 .md
- 不要跳题
- 不要上传 meta 文件或重传 v2.2 的 10 文件
- 不要延长 Instructions (只粘 system_prompt_v2 原文)

---

## 完成信号

给出结构化报告 → 主控按决策矩阵进 F1 (批 4 terminology 高频) 或回退.
