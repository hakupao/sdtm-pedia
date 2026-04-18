# Stage v2.1 Cowork 自动执行手册

> **给 Claude Cowork (computer-use / browser 模式) 执行的自动化任务.**
> Cowork 会亲自点击浏览器, 完成上传 + 测试, 返回报告.
> 用户只需把本文件全文作为 prompt 交给 cowork, 然后等结果.

---

## 你 (Cowork) 的任务

在用户的浏览器里自动完成 Claude.ai Project 的创建、文件上传、跑 12 题 A/B 测试, 然后返回结构化 Markdown 报告.

**权限假设**: 你有 browser / computer-use 工具, 能打开浏览器 / 点击 / 输入 / 上传文件 / 读取页面内容. 用户已登录 claude.ai 账号 (如果没登录, 请用户先登录, 不要自己尝试 login).

**工作目录**: `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/`

---

## 背景 (≤ 80 字)

SDTM 临床数据标准知识库项目. v1 是压缩版 (192K tokens, 已部署), v2.1 是全展开版 (205,895 tokens, 9 个上传文件). 需要对比两版在 12 题上的精度, 以决定是否继续后续批次.

---

## Step 1: 打开 claude.ai 并确认已登录

1. 打开浏览器 (Chrome / Safari 均可), 访问 `https://claude.ai`
2. 确认顶部能看到用户头像 (已登录状态). 若未登录, **停下提示用户手动登录**, 登录完再继续.
3. 点左侧导航的 **Projects** 菜单进入 Projects 列表页

---

## Step 2: 新建 Project

1. 点 **+ New Project** 按钮 (通常在右上角)
2. Project name: `SDTM-Knowledge-v2`
3. Description: 留空或填 "SDTMIG v3.4 full-expansion batch 1 (chapters restored)"
4. 点 Create / 确认

进入新 Project 页面.

---

## Step 3: 配置 Project Instructions

1. 在 Project 页面找 **Instructions** 编辑区 (或 "Custom Instructions" / "System prompt" 入口)
2. 读取本地文件 (用你的文件读工具):
   ```
   /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/system_prompt_v2.md
   ```
3. 把该文件**全文**粘贴到 Instructions 字段
4. 保存 (点 Save / Update / Apply)

**注意**: Instructions ≠ Project Knowledge. 这一步是文本粘贴到 Instructions, 不是文件上传.

---

## Step 4: 上传 9 个 .md 到 Project Knowledge

在 Project 页面找 **Project Knowledge** / **Add content** / **Upload files** 入口.

依次上传以下 **9 个文件** (全是本地绝对路径):

| # | 绝对路径 | 大小 (tokens) |
|---|---------|--------------|
| 1 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/00_routing.md` | 2,657 |
| 2 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/01_index.md` | 1,562 |
| 3 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/02_chapters.md` | **60,716** (v2.1 新) |
| 4 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/03_model.md` | 17,689 |
| 5 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/04_variable_index.md` | 14,938 |
| 6 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/05_mega_spec.md` | 65,993 |
| 7 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/06_assumptions.md` | 17,509 |
| 8 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/07_examples_catalog.md` | 4,295 |
| 9 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/08_terminology_map.md` | 20,536 |

**合计**: 9 文件 / **205,895 tokens**.

**绝对不要上传** (meta 文件):
- `upload_manifest_v2.md`
- `test_results_v2.md`
- `rag_decay_curve.md`
- `CHECKPOINT_V2.1_HANDOFF.md` (本文件)
- `evidence_v2/` 目录下任何文件

上传方式建议: 如果 claude.ai UI 支持多选, 一次选 9 个上传最省事; 如果只能逐个, 按上表顺序点 "Add content" → 选文件 → 上传.

---

## Step 5: 等 indexing 完成, 记 capacity %

1. 上传完成后 claude.ai 对文件 indexing (通常 1-5 分钟)
2. 等 Project UI 显示 "ready" / 索引完成标志 (或最后一个文件状态从 "processing" 变成 "ready")
3. 读取并**记录 Project Knowledge 使用率**, 通常显示为:
   - "Project Knowledge used: **XX%**" 或
   - "XX% of capacity" 或
   - progress bar 的百分比
4. 把 XX% 数字记下来, 写到最终报告的 `capacity` 字段

---

## Step 6: 跑 12 题 A/B 测试

在**新 v2 Project** (SDTM-Knowledge-v2) 下开启一个新对话 (Start new chat / + New chat).

**对每一题**:
1. 把问题原文发出去 (一题一条消息, 不要合并)
2. 等 Claude 完整回答
3. 读取并保存 Claude 的回答 (复制到你的内部记录)
4. 继续下一题

### T1-T8 回归题 (v1 已验证过)

- **T1**. AE.AEDECOD 的 Core 属性是什么?
- **T2**. AE 严重程度变化如何记录?
- **T3**. PC↔PP 通过 RELREC 关联的 4 种方法?
- **T4**. 哪些域有 EPOCH 变量?
- **T5**. 如何判断变量是否需要提交到 SUPP--?
- **T6**. AE Example 2 的具体数据是什么?
- **T7**. CT Code C66742 有哪些具体值?
- **T8**. CV 域所有变量值范围?

### T9-T12 v2.1 新增题 (针对 chapters 全展开收益)

- **T9**. ch01 SDTM 整体架构 + Foundational concepts?
- **T10**. ch02 §2.6 创建新 domain 的所有步骤?
- **T11**. ch08 §8.3 RELREC 数据集关系示例完整流程?
- **T12**. ch10 附录所有 entity 列表?

---

## Step 7: (可选) 在 v1 Project 跑同样 12 题

如果 Projects 列表里有 v1 的 Project (名称类似 `SDTM-Knowledge` / `SDTM-Knowledge-v1` — 请先问用户 v1 Project 的确切名称), **且用户确认要 A/B 对比**:

1. 切到 v1 Project 开启新对话
2. 跑同样 12 题, 记录 v1 答案

**若用户告知已有 v1 答案记录** (或不需要 v1 再跑一次), 跳过此步, v1 列在最终报告中标 "用户提供" 或空.

---

## Step 8: 评估每题精度

对每题做判定:

| 精度标签 | 说明 |
|---------|-----|
| **持平** | v2.1 和 v1 答案同质, 都正确 |
| **↑** | v2.1 比 v1 更精确 (如原文精确引用 vs 含糊概述) |
| **↓** | v2.1 比 v1 差 (回答变糊 / 截断 / 拒答 / 变空) |
| **N/A** | 两个都 FAIL, 或 v1 答案无记录 |

对 T9-T12 额外判定:
- **PASS**: v2.1 给出完整、有来源依据的答案 (如能引用 ch01/ch02/ch08/ch10 原文)
- **FAIL**: 兜底模板 / 拒答 / RAG 未命中 / 只说路径不给内容

---

## Step 9: 返回最终报告

所有测试完成后, 按以下 Markdown 模板返回完整报告. 这是你给主控的唯一输出:

```markdown
# Stage v2.1 A/B 测试报告

> 执行日期: YYYY-MM-DD HH:MM
> 执行者: Claude Cowork (browser automation)
> 新 Project: SDTM-Knowledge-v2
> v1 Project: [名称或 "未对比"]
> Capacity (v2): XX%
> Indexing 用时: X 分钟
> 总测试用时: X 分钟

## 上传确认
- [x] 9 个 .md 文件全部上传成功
- [x] system_prompt_v2.md 粘贴到 Instructions
- [x] Indexing 完成

## T1-T12 结果明细

### T1. AE.AEDECOD 的 Core 属性是什么?
- **v1 答案**: [完整或摘要]
- **v2 答案**: [完整]
- **精度**: 持平 / ↑ / ↓ / N/A
- **说明**: (1-2 句, 为何判这个精度)

### T2. AE 严重程度变化如何记录?
...

### T3. ...
...

(T1-T12 全部)

## 汇总矩阵

| # | 题目简称 | 精度 | T9-T12 PASS? |
|---|---------|------|-------------|
| T1 | AEDECOD Core | 持平/↑/↓ | — |
| T2 | AE 严重度变化 | ... | — |
| T3 | RELREC 4 方法 | ... | — |
| T4 | EPOCH 域列表 | ... | — |
| T5 | SUPP-- 判定 | ... | — |
| T6 | AE Ex2 数据 | ... | — |
| T7 | C66742 值 | ... | — |
| T8 | CV 域变量 | ... | — |
| T9 | ch01 架构 | ... | PASS/FAIL |
| T10 | ch02 §2.6 | ... | PASS/FAIL |
| T11 | ch08 §8.3 RELREC | ... | PASS/FAIL |
| T12 | ch10 附录 entity | ... | PASS/FAIL |

## 汇总数据
- T1-T8 衰减 (↓) 数: **N**
- T1-T8 上升 (↑) 数: **M**
- T1-T8 持平数: **P**
- T9-T12 PASS 数: **K/4**
- T9-T12 FAIL 数: **L/4**

## 关键观察 (2-4 句)
- 例如: "T11 ch08 §8.3 RELREC 在 v2.1 直接原文引用 4 种方法完整表格; v1 只能拼出 3 种 + 含糊描述第 4 种, 属明显 ↑"
- 例如: "T6 AE Example 2 两版都未给具体数据表 (目前 07_examples_catalog 是目录不是数据), 预期要等 v2.2 批次补全"
- 例如: "T12 ch10 附录 entity 在 v2.1 能给出 Appendix A-D 清单但不能给全部 entity 明细, 部分 PASS"

## 异常/警告
- [列出任何异常, 如:
  - Claude 拒答某题
  - 回答被 capacity 压缩截断
  - indexing 超过 10 分钟未完成
  - 某个文件上传失败 (即使重试)
  - UI 响应慢 / 错误提示]
- 或写 "无异常"

## 浏览器截图 (可选)
- 如果你的工具支持, 附 2-3 张关键截图:
  1. Project Knowledge capacity 百分比
  2. 某一题回答示例 (挑 T11 最有信息量的)
  3. (可选) 上传文件列表
```

---

## 决策矩阵 (供主控参考, 你不用判断)

主控收到你的报告后会按下表决策, 不需要你选, 你只给事实:

| 你的报告 | 主控决策 |
|---------|---------|
| T1-T8 无 ↓, T9-T12 ≥1 PASS | 继续 Task D1 (批 2 examples 高频) |
| T1-T8 无 ↓, T9-T12 全 FAIL | 回退 C1 调整算法 |
| T1-T8 有 1 题 ↓ | 报告用户, 询问是否续 |
| T1-T8 有 ≥2 题 ↓ | 立即停, v2.1 视为 v2 终态 |
| 用户要暂停 | 暂停 |

---

## 不要做

- **不要自行登录** claude.ai. 若未登录, 停下提示用户手动登录.
- **不要编造 Claude 的回答**. 如实记录 UI 上看到的内容, 即使是 "I don't know" / 拒答.
- **不要修改** output_v2/ 下任何 .md 文件.
- **不要跳题**. 12 题必须全部跑完, 除非用户中途喊停.
- **不要上传 meta 文件** (upload_manifest / test_results / rag_decay_curve / evidence_v2 / 本 handoff 文件).
- **不要延长 Instructions** — 只粘贴 system_prompt_v2.md 的原文, 不加你自己的话.

---

## 完成信号

给出结构化报告后, 用户会把报告粘贴给主控 Claude. 主控继续 Phase 6.5 v2 Task D1 或其他分支.

**准备好了就开始 Step 1.**
