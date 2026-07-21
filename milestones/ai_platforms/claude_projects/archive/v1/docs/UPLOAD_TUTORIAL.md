# Claude Project 上传教程（Step 13-14 操作手册）

> 本文档是 Phase 6.5 Claude Projects 压缩部署后的**手工上传与测试**完整操作指南。
> 对应 PLAN.md §7.4 Step 13 (手动上传) + Step 14 (Layer 2 测试矩阵)。
> 前置条件: Step 1-12 已完成，`output/` 目录包含 11 个 .md 文件，`upload_manifest.md` 显示 Layer 1 10/10 PASS。

---

## 0. 前置清单

打开终端，确认 11 个文件齐备：

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare
ls -la ai_platforms/claude_projects/output/*.md
```

应看到：

| 序 | 文件 | Tokens | 上传目标 |
|:-:|------|-------:|----------|
| 00 | `00_routing.md` | 2,657 | Project Knowledge |
| 01 | `01_index.md` | 1,562 | Project Knowledge |
| 02 | `02_chapters.md` | 44,874 | Project Knowledge |
| 03 | `03_model.md` | 17,689 | Project Knowledge |
| 04 | `04_variable_index.md` | 14,938 | Project Knowledge |
| 05 | `05_mega_spec.md` | 65,993 | Project Knowledge |
| 06 | `06_assumptions.md` | 17,509 | Project Knowledge |
| 07 | `07_examples_catalog.md` | 4,295 | Project Knowledge |
| 08 | `08_terminology_map.md` | 20,536 | Project Knowledge |
| -- | `system_prompt.md` | 1,983 | **粘贴到 Instructions** |
| -- | `upload_manifest.md` | 1,460 | （仅作自查，不上传） |

**合计上传内容: 192,036 tokens**（上限 200K，留 ~4% buffer）

---

## 1. 创建 Claude Project

1. 打开浏览器访问 [claude.ai](https://claude.ai)
2. 登录账号（需 **Claude Pro / Team / Enterprise** 订阅，Free 账户不支持 Projects）
3. 左侧边栏找到 **Projects** → 点击 **Create Project** (或 "+" 新建)
4. **Project 名称**: 填写 `SDTM Expert v3.4`（或你习惯的名字）
5. **Project 描述**（可选）: `SDTM (Study Data Tabulation Model) 领域专家，基于 CDISC SDTMIG v3.4 + SDTM v2.0 压缩知识库`
6. 点击 **Create Project** 确认

---

## 2. 配置 Project Instructions（System Prompt）

1. 在 Project 页面找到 **Set custom instructions** 或 **Project Instructions** 区域
2. 打开本地文件:
   ```bash
   cat /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output/system_prompt.md
   ```
3. 全选复制 `system_prompt.md` 的**全部内容**（从 `# SDTM Expert — Project Instructions` 到文末 "坦诚边界 > 臆造补全"）
4. 粘贴到 Project Instructions 输入框
5. 点击 **Save / 保存** 确认

> ⚠️ `system_prompt.md` 是 Markdown 格式，Claude 支持渲染。粘贴后可在预览中看到 7 个小节结构。

---

## 3. 上传 Project Knowledge（9 个文件）

1. 在 Project 页面找到 **Project knowledge** / **Add content** / **上传文件** 区域
2. 方式一（推荐）— **拖拽上传**:
   - 打开 Finder，定位到 `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output/`
   - **按住 Cmd** 多选以下 9 个文件:
     ```
     00_routing.md
     01_index.md
     02_chapters.md
     03_model.md
     04_variable_index.md
     05_mega_spec.md
     06_assumptions.md
     07_examples_catalog.md
     08_terminology_map.md
     ```
   - 拖拽到 Project knowledge 区域
3. 方式二 — **点击选择上传**: 在 UI 点 "+" 或 "Upload files"，在对话框里多选这 9 个文件

4. **不要上传** `system_prompt.md`（已在 Instructions 里）和 `upload_manifest.md`（自查用）

---

## 4. 验证容量与结构

### 4.1 检查容量百分比

上传完后，Claude Project UI 会显示 **"Project capacity: XX%"** 或类似字样（通常在 Knowledge 区域底部）。

**预期值**: 95-98%（192K tokens / 200K 上限）

- 若显示 **>99%**: 🚨 立即停手，不要做 Step 5 测试 → 告诉我
  - 备选方案: 从 `08_terminology_map.md` 或 `07_examples_catalog.md` 重跑更激进版本
- 若显示 **95-98%**: ✅ 正常，进入 Step 5
- 若显示 **<95%**: ⚠️ tokenizer 差异比预期大，但可继续

### 4.2 基础 smoke test

在 Project 内新建对话，发送一个超简单问题：

```
列出你拥有的文件，每个文件一句话说明它是做什么的。
```

**预期行为**: Claude 应该列出 9 个文件（00-08）+ 引用 Instructions 里的"文件索引"表。如果 Claude 说"我没有文件"或少列出某个文件，检查上传是否漏。

---

## 5. Layer 2 测试矩阵（T1-T8）

在 Project 内建**一个新对话**（避免污染 smoke test）。按顺序跑以下 8 个测试，每个都记录 Claude 的回答。

### T1: 变量精确查询

**提问**:
> AE 域中 AEDECOD 变量的 Core 属性是什么？请引用依据。

**期望行为**:
- 答: **Expected** (Req)
- 引用 `05_mega_spec.md` 中 AE 行
- 提到源路径 `domains/AE/spec.md`

---

### T2: 规则推导（跨文件）

**提问**:
> 如果受试者的不良事件严重程度在研究过程中发生变化，应该如何记录？

**期望行为**:
- 引用 `06_assumptions.md` 中 AE 相关假设
- 提到 `AEGRPID` 用于分组相关 AE 记录
- 可能引用 `02_chapters.md` ch04 或 AE assumptions 的时间变量规则

---

### T3: 跨域关联（4 方法）

**提问**:
> PC (Pharmacokinetic Concentrations) 和 PP (Pharmacokinetic Parameters) 两个域之间，通过 RELREC 关联有几种方法？请说明每种方法。

**期望行为**:
- 答: **4 种 (Method A/B/C/D)**
- 引用 `07_examples_catalog.md` 中 PC/PP 共享 examples 条目
- 坦诚告知"具体数据在 `knowledge_base/domains/PC/examples.md`"（因为数据表不在 Project）

---

### T4: 反向查询

**提问**:
> SDTMIG v3.4 中有哪些域包含 EPOCH 变量？

**期望行为**:
- 答: **44 个域**（AE, AG, CE, CM, CP, CV, DA, DS, DV, EC, EG, EX, FA, FT, HO, IE, IS, LB, MB, MH, MI, MK, ML, MS, NV, OE, PC, PE, PP, PR, QS, RE, RP, RS, SC, SE, SR, SS, SU, TA, TR, TU, UR, VS）
- 引用 `04_variable_index.md` 通用变量段

---

### T5: 路由准确性（SUPP--）

**提问**:
> 如何判断一个非标准变量应该提交到 SUPP-- 数据集还是作为标准变量？

**期望行为**:
- 引用 `02_chapters.md` ch08 (Relationships) 的 §8.4
- 提到 "When NOT to use SUPP--" 规则
- 可能引用 `06_assumptions.md` 相关说明

---

### T6: 边界 — Examples 具体数据

**提问**:
> AE Example 2 的具体数据长什么样？请给出完整数据表。

**期望行为**:
- 引用 `07_examples_catalog.md` 中 AE Example 2 一句话描述（如 "prespecified AE (AEPRESP=Y) + FA linkage"）
- **明确告知**: "**具体数据表不在本 Project**，请到 `knowledge_base/domains/AE/examples.md Example 2` 查看"
- ⚠️ 如果 Claude 编造数据，此测试 **FAIL**

---

### T7: 边界 — Terminology Term 值

**提问**:
> CT Code C66742 对应的 codelist 有哪些具体值？

**期望行为**:
- 引用 `08_terminology_map.md` 中 `C66742 | No Yes Response` 映射
- **明确告知**: "**具体 Term 值（如 Y/N/U/NA）不在本 Project**，请到 `terminology/core/general_part4.md` 查看"
- ⚠️ 如果 Claude 编造 Term 值，此测试 **FAIL**

---

### T8: 边界 — 不编造

**提问**:
> CV 域的所有变量的取值范围都是什么？

**期望行为**:
- 从 `05_mega_spec.md` 列出 CV 的变量名和 Role/Core/CT
- **明确告知**: "变量定义在 Project 内，但**具体取值范围（Term 值）需查 `terminology/` 或 `knowledge_base/domains/CV/spec.md` 源文件**"
- 回答格式应是"我有这个 + 我没有这个"的诚实边界划分

---

## 6. 记录测试结果

每跑一个 T*，把 Claude 的回答（或截图链接）贴到 `ai_platforms/claude_projects/output/test_results.md`（若无则创建）。

模板：

```markdown
# Layer 2 Test Results (Step 14)

> 执行日期: YYYY-MM-DD
> 测试执行者: <你的名字>
> Claude Project: SDTM Expert v3.4
> Project 实际容量: XX%

## T1: 变量精确查询
- 问题: "AE.AEDECOD 的 Core 属性是什么？"
- Claude 回答: <粘贴原文, 或截图链接>
- 期望: Expected / 引用 05_mega_spec.md
- 判定: **PASS / FAIL**
- 备注: (如有)

## T2: 规则推导
- 问题: ...
- Claude 回答: ...
- 判定: ...

## ... T3-T8 同格式

## 汇总

| 测试 | 结果 | 备注 |
|:-:|:-:|------|
| T1 | PASS/FAIL | |
| T2 | ... | |
| ... | | |

**总计**: X/8 PASS

## 如 FAIL 的分析
- 根因: (System Prompt 不够明确? / 文件压太狠? / Claude 行为异常?)
- 修复建议: (改 Step 11 System Prompt / 重跑某 Step / 其他)
```

完成后告诉我测试结果，我会进入 Phase 6.5 Claude 路线的**完结归档**（§7.9）。

---

## 7. 异常处理

### 场景 A: Project 容量显示 >100% 或上传失败
- **立即停手**，不要继续测试
- 告诉主控 "容量超限 X%"
- 主控可回退到 Step 6/7/8/9 做更激进压缩（Mega Spec Level 4, Notes 整删可节省 7K+）

### 场景 B: Claude 找不到某个文件
- 检查 Project Knowledge 区是否 9 个文件全在
- 若缺某个，重新上传
- 若 Claude 仍答"没有"，可能是 Instructions 里路径写错了 → 检查 `system_prompt.md` 文件索引表

### 场景 C: T6/T7/T8 边界测试 FAIL（Claude 编造数据）
- 根因通常是 **System Prompt 的边界模板不够显眼**
- 修复: 重跑 Step 11，把 4 个边界模板放到 Instructions 最显眼位置
- 重新粘贴到 Claude Project Instructions

### 场景 D: T1-T5 功能测试 FAIL（查询不准）
- 根因可能是文件压太狠，信息丢失
- 对应 Step:
  - T1 FAIL → 检查 Step 6 Mega Spec
  - T2 FAIL → 检查 Step 7 assumptions
  - T3 FAIL → 检查 Step 8 examples catalog
  - T4 FAIL → 检查 Step 5 var_index
  - T5 FAIL → 检查 Step 3 chapters (ch08)
- 可回退具体 Step 重跑

### 场景 E: 回滚/重新上传
- 不要删 Project（保留对话历史）
- 在 Knowledge 区删某个文件 + 重新上传新版
- **不要动 `system_prompt.md` Instructions 内容**（除非 System Prompt 本身要改）

---

## 8. 完成后

执行完 T1-T8 全部 PASS 后:

1. 记录 `output/test_results.md`
2. 告诉主控 "T1-T8 全部 PASS"
3. 主控进入 PLAN §7.9 完结归档:
   - 更新 `worklog.md` + `PROGRESS.md` + `MANIFEST.md` + ROADMAP
   - Commit + push
   - 进入下一阶段（ChatGPT GPT 路线）
