# Stage v2.1 用户操作手册 (Cowork 可执行版)

> 给 Claude Cowork / 另一个 Claude session 执行用的 standalone 指令手册.
> 目的: 在 claude.ai 新建第二个 Project (SDTM-Knowledge-v2), 上传 v2.1 扩容版知识库, 跑 12 题 A/B 测试, 返回结构化报告.

---

## 角色与目标

你 (Cowork Claude) 的任务:

1. 帮用户在 claude.ai 网页端新建一个 Project (名称: `SDTM-Knowledge-v2`)
2. 配置 Project Instructions (从指定文件粘贴)
3. 上传 9 个 .md 文件到 Project Knowledge
4. 等 indexing 完成, 记录 capacity %
5. 跑 12 题 A/B 测试, 把 v1 Project 答案 (用户已有) 和 v2 Project 答案对比
6. 返回结构化测试报告 (Markdown)

**注意**: 你不能代替用户点击 claude.ai UI — 上传和发消息都需要用户亲自操作. 你的任务是**指引 + 评估**, 不是代跑.

---

## 背景 (≤ 100 字)

这是一个 SDTM (Study Data Tabulation Model) 临床数据标准知识库项目. v1 是"压缩版" (192K tokens), v2.1 是"全展开版" (205,895 tokens, 9 个上传文件, 002_chapters.md 由压缩 44,874 → 全展开 60,716 tokens, +35.3%). 需要对比两个版本在 12 个典型问题上的精度差异.

---

## Step 1: 新建 Project

请用户在 claude.ai 顶部 Projects 页面点 "+ New Project", 名称填 `SDTM-Knowledge-v2`, 描述可留空.

---

## Step 2: Project Instructions

请用户打开本地文件:
```
/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/system_prompt_v2.md
```

把全文内容 (约 1,983 tokens) 复制粘贴到新 Project 的 **Instructions** 字段. 不是 Project Knowledge, 是 Instructions!

---

## Step 3: 上传 9 个 .md 到 Project Knowledge

请用户把以下 **9 个文件** 从本地上传到 Project Knowledge:

| # | 本地文件 | 大小 (tokens) |
|---|---------|-------|
| 1 | `output_v2/00_routing.md` | 2,657 |
| 2 | `output_v2/01_index.md` | 1,562 |
| 3 | `output_v2/02_chapters.md` | **60,716** ← v2.1 新版 |
| 4 | `output_v2/03_model.md` | 17,689 |
| 5 | `output_v2/04_variable_index.md` | 14,938 |
| 6 | `output_v2/05_mega_spec.md` | 65,993 |
| 7 | `output_v2/06_assumptions.md` | 17,509 |
| 8 | `output_v2/07_examples_catalog.md` | 4,295 |
| 9 | `output_v2/08_terminology_map.md` | 20,536 |

**合计上传: 205,895 tokens (9 个文件)**

**绝对不要上传** (meta 文件, 只供主控用):
- `upload_manifest_v2.md`
- `test_results_v2.md`
- `rag_decay_curve.md`
- `CHECKPOINT_V2.1_HANDOFF.md` (本文件)
- `evidence_v2/` 目录全部

绝对路径参考 (Mac):
`/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/`

---

## Step 4: 等 indexing + 记 capacity %

上传完成后, claude.ai 会对文件做 indexing. 等 UI 显示 "ready" 或索引完成标志. 记下 Project UI 顶部显示的 **capacity 百分比** (例如 "Project Knowledge used: 82%").

**把这个百分比填到后续报告的 `capacity` 字段**.

---

## Step 5: 跑 12 题 A/B 测试

在新 v2 Project 的对话中, **每题一条消息**, 把问题原文发出去, 记录完整回答. 然后如果用户还没跑过 v1 Project 的, 也在 v1 Project (名称 `SDTM-Knowledge` 或类似) 跑一遍同样 12 题做对比.

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

## Step 6: 评估每题精度

对每题, 对比 v1 答案 vs v2.1 答案, 从以下 4 类选一个:

| 精度标签 | 说明 |
|---------|-----|
| **持平** | v2.1 和 v1 答案同质, 都正确 |
| **↑ (上升)** | v2.1 比 v1 更精确 (如原文引用 vs 含糊) |
| **↓ (衰减)** | v2.1 比 v1 差 (回答变糊 / 截断 / 拒答) |
| **N/A** | 两个都 FAIL, 或题目不适用本阶段 |

对 T9-T12, 额外判定: **PASS** (v2.1 给出完整有依据答案) / **FAIL** (兜底模板 / 拒答 / RAG 未命中).

---

## Step 7: 返回结构化报告

请按以下 Markdown 模板返回完整报告 (注意: 这是你最终要交给主控的内容):

```markdown
# Stage v2.1 A/B 测试报告

> 执行日期: YYYY-MM-DD
> 新 Project: SDTM-Knowledge-v2
> Capacity: XX%

## 上传确认
- [x] 9 个 .md 文件全部上传
- [x] system_prompt_v2.md 粘贴到 Instructions
- [x] Indexing 完成
- 上传用时: X 分钟

## T1-T12 测试结果

| # | 题目 | v1 摘要 | v2.1 摘要 | 精度 | T9-12 PASS? |
|---|------|--------|----------|------|------------|
| T1 | AE.AEDECOD Core | [v1 一句话] | [v2 一句话] | 持平/↑/↓ | — |
| T2 | AE 严重程度变化 | ... | ... | ... | — |
| T3 | PC↔PP RELREC 4 方法 | ... | ... | ... | — |
| T4 | EPOCH 域列表 | ... | ... | ... | — |
| T5 | SUPP-- 判定规则 | ... | ... | ... | — |
| T6 | AE Example 2 数据 | ... | ... | ... | — |
| T7 | C66742 Term 值 | ... | ... | ... | — |
| T8 | CV 域变量范围 | ... | ... | ... | — |
| T9 | ch01 整体架构 | (期望 FAIL) | ... | ↑/持平/↓ | PASS/FAIL |
| T10 | ch02 §2.6 创建 domain | (期望 FAIL) | ... | ↑/持平/↓ | PASS/FAIL |
| T11 | ch08 §8.3 RELREC 示例 | ... | ... | ↑/持平/↓ | PASS/FAIL |
| T12 | ch10 附录 entity 列表 | (期望 FAIL) | ... | ↑/持平/↓ | PASS/FAIL |

## 汇总数据
- T1-T8 衰减题数 (↓): **N**
- T1-T8 上升题数 (↑): **M**
- T9-T12 PASS 数: **K/4**
- T9-T12 FAIL 数: **L/4**

## 关键观察 (1-3 句)
- [用户或你对 v2.1 相对 v1 的关键差异观察, 例如:
  "T11 ch08 §8.3 从 v1 的间接重建升级到 v2.1 原文精确引用"
  "T12 仍弱, ch10 附录格式 RAG 未完整抓到"
  "T6 AE Example 2 在两个 Project 都只给出结构不给具体数据, 需等 v2.2 examples 批"]

## 异常/警告
- [任何异常情况, 如:
  - Claude 拒答某题
  - 回答被 capacity 压缩截断
  - indexing 超过 10 分钟未完成
  - 其他]
  或写 "无异常"
```

---

## 决策矩阵 (给主控参考, 你不用决策)

主控会根据你的报告决定:

| 你的报告 | 主控决策 |
|---------|---------|
| T1-T8 全持平或 ↑, T9-T12 ≥1 PASS | 继续 Task D1 (批 2 examples 高频) |
| T1-T8 全持平, T9-T12 全 FAIL | 回退 C1 调整, 写 failure |
| T1-T8 中 1 题 ↓ | 汇报后问用户是否续 |
| T1-T8 中 ≥2 题 ↓ | **立即停**, v2.1 视为 v2 终态, 跳收尾 |
| 用户疲劳/暂停 | 暂停, 下次重启 |

---

## 不要做

- 不要替用户点击 UI (你做不到 — claude.ai Project 没公开 API)
- 不要跳过任何一题 (12 题必须全部问)
- 不要编造答案 (如实记录 Claude 的回答)
- 不要改 output_v2/ 下任何文件
- 不要泄露用户的 v1 答案 (除非用户主动提供)

---

## 完成信号

当你给出结构化报告后, 用户会把报告粘贴给主控 Claude. 主控会继续 Phase 6.5 v2 的 Task D1 或其他决策分支.

**你的报告是主控做决策的唯一输入, 请尽量完整准确.**
