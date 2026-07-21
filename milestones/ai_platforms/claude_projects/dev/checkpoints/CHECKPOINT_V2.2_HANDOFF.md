# Stage v2.2 Cowork 自动执行手册

> **给 Claude Cowork (computer-use / browser 模式) 执行的自动化任务.**
> Cowork 亲自点浏览器上传 1 个新文件 + 更新 Instructions + 跑 4 题 A/B 测试, 返回结构化报告.
> 用户只需把本文件全文作为 prompt 交给 cowork, 然后等结果.

---

## 背景 (≤ 80 字)

Stage v2.2 给 v2 Project 加一个文件 `09_examples_data_high.md` = 112,697 tokens (28 高频域 examples 数据表全量). 已知 token 超 v2 原计划 50K 硬 cap 到 2.25×, 用户 Option A 接受 (总 RAG 容量 ~3-4M, 占比 3.2%). 需回答: T13 (DM Ex1 数据) / T14 (EX 剂量调整 Example) 能否直接原文命中 + T1/T11 回归是否稳。

---

## 你 (Cowork) 的任务

在 **已存在的 v2 Project** (名称 `SDTM-Knowledge-v2`) 下:
1. Project Knowledge 新增上传 **1 个文件**: `output_v2/09_examples_data_high.md`
2. 覆盖更新 Project Instructions, 粘贴最新 `output_v2/system_prompt_v2.md` 全文
3. 跑 4 题 A/B 测试
4. 返回 Markdown 结构化报告

**权限假设**: 同 v2.1 handoff (已登录 claude.ai, 有 browser / computer-use 工具).

**工作目录**: `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/`

---

## Step 1: 进入现有 v2 Project

1. 打开 `https://claude.ai`
2. 确认已登录
3. 进入 **Projects** 列表, 打开已存在的 `SDTM-Knowledge-v2` (v2.1 已建的那个, 含 9 文件)

若找不到 v2 Project, 停下问用户。

---

## Step 2: 覆盖 Project Instructions (同步 v2.2 增量)

1. 打开 Instructions 编辑区
2. 读 `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/system_prompt_v2.md`
3. **全文覆盖粘贴** (整段替换, 不要 append)
4. 保存

注: 这一版比 v2.1 多了 `<!-- stage v2.2 begin -->` 段 (Examples 查询优先级 09 > 07).

---

## Step 3: 上传 1 个新文件到 Project Knowledge

找到 Project Knowledge → Add content → 选本地文件上传:

| # | 绝对路径 | 大小 (tokens) |
|---|---------|--------------|
| 1 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/09_examples_data_high.md` | **112,697** |

**合计 (v2.2 终态)**: 10 文件 / **318,592 tokens** (v2.1 9 文件 205,895 + 1 新文件 112,697).

**绝对不要上传** (meta 文件):
- `upload_manifest_v2.md`
- `test_results_v2.md`
- `rag_decay_curve.md`
- `CHECKPOINT_V2.1_HANDOFF.md`
- `CHECKPOINT_V2.2_HANDOFF.md` (本文件)
- `STAGE_V2.1_AB_REPORT.md`
- `evidence_v2/` 目录下任何文件

**不要重复上传 v2.1 的 9 文件**: 它们已在 Project, 覆盖会浪费 indexing。

---

## Step 4: 等 indexing 完成, 记 capacity %

1. 上传 09 后等 indexing (通常 30s-3min, 因 112K 大文件可能略慢)
2. 等 status 变成 ready
3. 读 Project Knowledge 使用率 (v2.1 时是 13%, v2.2 预期 ~20-22%)
4. 记下 capacity 百分比 + indexing 用时

---

## Step 5: 跑 4 题 A/B 测试

在 **同一 v2 Project** (SDTM-Knowledge-v2) 下**新开一个对话**, 跑以下 4 题:

### T13 (新增, 批 2 目标): DM Example 1 的完整数据是什么?
期望: 能原文引用 **dm.xpt** 数据表 (多行多列), 不再给兜底 "需查 examples/".

### T14 (新增, 批 2 目标): EX 剂量调整 Example 的数据怎么写?
期望: 能原文引用 ex.xpt 或 exd.xpt 表格 (含 EXDOSE / EXDOSU / EXDOSFRM 等), 覆盖"剂量调整"场景的 Example.

### T1 (回归): AE.AEDECOD 的 Core 属性是什么?
期望: 与 v2.1 答案一致 (不衰减).

### T11 (回归): ch08 §8.3 RELREC 数据集关系示例完整流程?
期望: 与 v2.1 答案一致 (不衰减, ch08 全文在 02_chapters.md 没变).

**对每题**:
1. 发问题原文
2. 等完整回答
3. 保存回答 (复制到内部记录)
4. 继续下一题

---

## Step 6: 评估每题精度

| 精度标签 | 说明 |
|---------|-----|
| **持平** | v2.1 和 v2.2 答案同质 |
| **↑** | v2.2 比 v2.1 更精确 |
| **↓** | v2.2 比 v2.1 差 (变糊 / 截断 / 拒答) |

对 T13/T14 额外:
- **PASS**: 给出完整、有来源依据的数据表 (能引用 DM/EX examples.md 原文)
- **FAIL**: 兜底模板 / 拒答 / 只说路径不给数据

对 T1/T11 额外:
- **持平/稳定** 或 **↑**: 符合预期
- **↓**: 回归衰减 ⚠️, 主控会立即停

---

## Step 7: 返回最终报告

```markdown
# Stage v2.2 A/B 测试报告

> 执行日期: YYYY-MM-DD HH:MM
> 执行者: Claude Cowork
> v2 Project: SDTM-Knowledge-v2 (v2.2 态)
> Capacity (v2.2): XX%  (v2.1 参照: 13%)
> Indexing 用时: X 分钟
> 总测试用时: X 分钟

## 上传确认
- [x] 09_examples_data_high.md 上传成功
- [x] system_prompt_v2.md 覆盖到 Instructions
- [x] Indexing 完成

## 4 题结果明细

### T13. DM Example 1 完整数据
- **v2.1 答案**: (兜底 / 待记录)
- **v2.2 答案**: [完整原文]
- **精度**: 持平 / ↑ / ↓
- **T13 判定**: PASS / FAIL
- **说明**: ...

### T14. EX 剂量调整 Example
- **v2.1 答案**: ...
- **v2.2 答案**: ...
- **精度**: ...
- **T14 判定**: PASS / FAIL
- **说明**: ...

### T1. AEDECOD Core (回归)
- **v2.1 答案**: ...
- **v2.2 答案**: ...
- **精度**: 持平 / ↓
- **说明**: ...

### T11. ch08 §8.3 RELREC (回归)
- **v2.1 答案**: ...
- **v2.2 答案**: ...
- **精度**: 持平 / ↓
- **说明**: ...

## 汇总矩阵

| # | 题目简称 | 精度 vs v2.1 | 新增 PASS? |
|---|---------|------------|-----------|
| T13 | DM Ex1 数据 | ↑/持平 | PASS/FAIL |
| T14 | EX 剂量调整 | ↑/持平 | PASS/FAIL |
| T1 | AEDECOD Core | 持平/↓ | — |
| T11 | ch08 §8.3 RELREC | 持平/↓ | — |

## 汇总
- 回归衰减 ↓ 数: **N**
- 新增 PASS: **K/2**
- 新增 FAIL: **L/2**

## 关键观察 (2-3 句)
...

## 异常/警告
- 或 "无异常"
```

---

## 决策矩阵 (供主控参考, Cowork 不用判)

| Cowork 报告 | 主控决策 |
|------------|---------|
| T1/T11 无 ↓, T13+T14 ≥1 PASS | 继续 Task E1 (批 3 examples 剩余域) |
| T1/T11 无 ↓, T13+T14 全 FAIL | 回退 D2 调整算法 (如 row-cap 或重抽 description) |
| T1/T11 有 1 题 ↓ | 报告用户, 询问是否续 |
| T1/T11 有 2 题 ↓ | 立即停, v2.2 视为 v2 终态 |
| 用户要暂停 | 暂停 |

---

## 不要做

- 不要自行登录 claude.ai
- 不要编造 Claude 的回答
- 不要修改 output_v2/ 任何 .md
- 不要跳题 (4 题全跑)
- 不要上传 meta 文件
- 不要重传 v2.1 的 9 文件

---

## 完成信号

给出结构化报告后, 用户把报告粘贴给主控 Claude, 主控继续 Task E1 或其他分支。

**准备好了就开始 Step 1.**
