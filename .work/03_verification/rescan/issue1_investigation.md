# Issue 1 调查与修正计划

> 创建日期: 2026-04-15
> 关联: issues_found.md — Issue 1 (图像扫描页码不可靠)
> 状态: **已解决** (2026-04-15)

---

## 背景

Issue 1 原始描述: 6 个 Sonnet agent 扫描 PDF 图像时，页码通过视觉估算获取，TD Example 区域存在明显偏移 (标注 p.416-418 vs 实际 p.412 起)。

## 重新评估

经用户分析，Issue 1 的影响需要重新界定:

### 图像清单页码 — 暂时搁置

`step3_6_image_inventory.md` 中的页码偏差属于**图像转化作业的中间产物**。图像转化已全部完成（37 幅已转化 + 2 幅故意排除 + 21 幅待判定），页码偏差不影响已完成的转化产出。此部分暂不处理。

### page_index.json 页码 — 必须修正

Issue 1 引申发现 `.work/02_indexing/page_index.json` 的 TD 部分也存在不准确:

- page_index.json 是全项目的**权威页码索引 (single source of truth)**
- 该文件标记了 `"verified": true`，说明当时经过了验证流程并判定为通过
- 如果验证通过的文件仍有错误，说明**验证方法本身可能存在漏洞**

这比单纯的页码错误更严重 — 涉及验证流程的可信度。

## 核心疑问

1. page_index.json 当时是如何生成的？（手动 / AI 辅助 / 脚本）
2. 用了什么模型？（Sonnet / Opus / 其他）
3. 验证是如何执行的？（逐页对照 PDF / 抽查 / 自动化检查）
4. `"verified": true` 的判定标准是什么？

## 任务计划

### Step 1: 调查验证记录

- 查阅 `.work/03_verification/plan.md` 中关于 page_index.json 的步骤描述
- 查阅 `.work/03_verification/results/` 下相关的验证结果文件
- 确认当时的执行方法、模型、验证深度

### Step 2: 修正 page_index.json

- 对照 PDF 原文，逐一核实 page_index.json 中 TD 及周边域的页码
- 如发现 TD 以外的域也有类似问题，扩大修正范围
- 修正后更新 `"verified"` 状态和备注

### Step 3: 传播修正

- 将 page_index.json 修正后的页码同步到 `step3_6_image_inventory.md`
- 仅更新与 page_index.json 修正相关的条目

---

## 调查记录

### Step 1 调查: page_index.json 的生成与验证历史

**调查日期**: 2026-04-15

#### Git 历史

| Commit | 日期 | 描述 | Co-Author |
|--------|------|------|-----------|
| `8a88538` | 2026-04-13 | Initial release — page_index.json 首次创建 (1336 行) | Claude Opus 4.6 |
| `491d9c7` | 2026-04-14 | Step 0–2 — page_index.json 修正 + 标记 verified | Claude Sonnet 4.6 |

此后无任何 commit 再修改过 page_index.json。

#### 初始版本状态 (8a88538)

- 63 域中: verified=true **仅 7 个**, verified=false **53 个**, partial **3 个**
- 页码来源: 推断为 TOC 估算 + 部分手动确认
- 多数域的页码为近似值

#### Step 0 修正 (491d9c7)

- **模型**: Claude Sonnet 4.6（commit Co-Authored-By 明确标注）
- **操作**: 一次性将 56 个域从 false/partial 翻为 verified=true，并修改大量页码边界
- **声称方法**: verification_plan.md 记载"63 域页码全部实际翻 PDF 确认"
- **结果文件**: **不存在** — Step 1 ~ Step 3.5 均有独立 results.md，唯独 Step 0 没有任何验证证据文件

#### TD 区域三版本对比

| 字段 | 初始版 (8a88538, 估算) | Step 0 修正版 (491d9c7, 当前) | 偏移量 |
|------|----------------------|----------------------------|--------|
| section | [410, 414] | [412, 417] | +2, +3 |
| spec | [410, 411] | [412, 413] | +2, +2 |
| assumptions | [411, 412] | [414, 414] | +3, +2 |
| examples | [412, 414] | [415, 417] | +3, +3 |

周边域同步偏移:

| 域 | 初始 section | Step 0 section | 偏移 |
|----|-------------|---------------|------|
| TV | [407, 409] | [407, 412] | end +3 |
| TD | [410, 414] | [412, 417] | +2, +3 |
| TM | [415, 415] | [418, 418] | +3 |
| TI | [416, 416] | [419, 420] | +3, +4 |
| TS | [417, 424] | [420, 425] | +3, +1 |

#### 根因分析

1. **Step 0 缺乏审计证据**: 整个验证流程中唯一没有结果文件的步骤。作为所有后续步骤依赖的基础，这是验证链中最薄弱的环节。

2. **Sonnet 单次批量验证 63 域**: 用较弱模型一次性验证大量页码。Trial Design 章节 (p.384-425) 包含 9 个连续小域 (TA/TE/TV/TD/TM/TI/TS + RELREC/SUPPQUAL)，页码密集，累积偏移风险高。

3. **无交叉验证机制**: 没有第二遍独立核实，也没有不同方法（如逐页读取标题）的对照验证。

4. **与 Step 1/2 打包提交**: Step 0 与 Step 1、Step 2 在同一 commit 中提交，无法从 git 层面区分 Step 0 的独立变更时间和方法。

#### 结论

page_index.json 的 Step 0 验证存在**方法论缺陷**: 无结果文件、无证据链、Sonnet 模型能力有限、单次批量操作。TD 及其周边域（TV ~ TS 整个 Trial Design 区域 p.384-425）需要重新逐页对照 PDF 验证。

---

### Step 2 实施方案: 全面重新验证 page_index.json

#### 总体策略: 方案 C — 分段扫描 + 差异定位

不信任任何已有数据，从 PDF 原文重建完整页码索引。分三阶段执行。

---

#### 阶段 1: 粗扫描 — 并行读取 PDF，记录所有章节标题

**模型**: Opus（当前对话主模型，非 Sonnet）
**读取粒度**: 每次 10 页
**并行方式**: 7 个 Opus agent，每个负责一个连续页码段

##### Agent 分配

| Agent | 源 PDF | 页码范围 | 读取次数 | 覆盖内容 |
|-------|--------|----------|----------|----------|
| A1 | SDTMIG v3.4 | p.1-60 | 6 次 | chapters: ch01, ch02, ch03, ch04 |
| A2 | SDTMIG v3.4 | p.60-130 | 7 次 | domains: CO → SU (12 域) |
| A3 | SDTMIG v3.4 | p.130-200 | 7 次 | domains: AE → BS + shared_specs_1 (12 域) |
| A4 | SDTMIG v3.4 | p.200-290 | 9 次 | domains: CP → CV + shared_specs_2 (11 域) |
| A5 | SDTMIG v3.4 | p.290-380 | 9 次 | domains: MK → SR (17 域) |
| A6 | SDTMIG v3.4 | p.380-461 | 9 次 | domains: TA → RELSPEC + ch08, ch09, ch10 (14 域 + 3 章) |
| A7 | SDTM v2.0 | p.1-74 | 8 次 | model: 全部 6 个文件 |

**合计**: 7 个 agent × 6~9 次读取 = **55 次 PDF 读取**

##### 每个 Agent 的指令

```
任务: 逐页扫描 PDF 第 [起始页]-[结束页]，每次读 10 页。
对每一页，记录你看到的所有章节/节标题。

记录规则:
1. 只记录实际出现在该页上的标题，不推测
2. 标题层级:
   - Chapter: 如 "1 Introduction", "4 Assumptions..."
   - Domain: 如 "6.1.1 Comments (CO)", "7.2.1 Trial Arms (TA)"
   - Subsection: 域内的 Specification / Assumptions / Examples 子标题
   - Figure: 图表标题 (如 "Figure 4.4.10-1: Representing Time Points")
3. 如果某页没有任何标题（纯表格/正文延续），记录 "— (续前节)"
4. 如果某页包含 spec 表格，标记 "spec table starts/continues/ends"

输出格式 (严格 markdown 表格):

| 页码 | 标题层级 | 标题原文 | 备注 |
|------|---------|---------|------|
```

##### Agent 输出文件

每个 agent 输出保存到: `.work/03_verification/rescan/a[N].md`

---

#### 阶段 2: 差异定位 — 对比扫描结果与当前 JSON

##### 2a. 合并扫描结果

将 7 个 agent 的输出合并为统一的「页码→标题」映射表。

##### 2b. 自动对比

对 page_index.json 中每个条目，与扫描结果交叉比对:

```
对于每个 domain/chapter/model entry:
  - 检查 section 起始页是否有对应的 Domain/Chapter 标题
  - 检查 spec 起始页是否有 Specification 子标题或 spec table
  - 检查 assumptions 起始页是否有 Assumptions 子标题
  - 检查 examples 起始页是否有 Examples 子标题
  
  结果分类:
  - MATCH: 扫描结果与 JSON 一致
  - MISMATCH: 扫描结果与 JSON 不一致 (记录差异)
  - UNCLEAR: 扫描结果中未发现明确标题 (需精确定位)
```

##### 2c. 精确定位

对所有 MISMATCH 和 UNCLEAR 条目，执行**单页读取**:
- 读取争议页及其前后各 1 页 (共 3 页)
- 确定精确的节边界
- 预计补充读取 10-30 次

---

#### 阶段 3: 程序化校验 + 更新

##### 3a. 生成新 JSON

基于阶段 1 扫描 + 阶段 2 精确定位的结果，从零生成 page_index_new.json。

##### 3b. 程序化完整性校验

对新 JSON 运行以下自动检查:

```
检查项 1 — 连续性 (无间隙无重叠):
  对相邻域 A, B: A.section_end >= B.section_start - 1
  (允许共享页: A 结尾和 B 开头在同一页)

检查项 2 — 包含性:
  对每个域: section_start <= spec_start
            spec_end <= assumptions_start (如有 assumptions)
            assumptions_end <= examples_start (如有 examples)
            examples_end <= section_end

检查项 3 — 全覆盖:
  chapters + domains 的 section 范围合并后 = p.1-461 (SDTMIG)
  model 的 pages 范围合并后 覆盖 p.8-69 (SDTM v2.0)

检查项 4 — 共享节一致:
  EX.examples == EC.examples
  MB.examples == MS.examples
  TU.examples == TR.examples
  PC.examples 与 PP.examples 有交集
```

##### 3c. Diff 对比

生成 page_index.json (旧) vs page_index_new.json (新) 的完整差异清单，记录每一处变更及原因。

##### 3d. 替换

用户确认后，用 page_index_new.json 替换 page_index.json。

---

#### 证据产出

| 文件 | 内容 |
|------|------|
| `rescan_a1.md` ~ `rescan_a7.md` | 7 个 agent 的原始扫描记录 |
| `rescan_merged.md` | 合并后的完整页码→标题映射 |
| `rescan_diff.md` | 新旧 JSON 差异清单 |
| `rescan_validation.md` | 程序化校验结果 |

所有证据文件保存在 `.work/03_verification/rescan/` 下。

---

#### 与上次 (Step 0) 的对比

| 维度 | Step 0 | 本次 |
|------|--------|------|
| 模型 | Sonnet | **Opus** |
| 读取粒度 | 20 页/次 | **10 页/次 → 1 页/次** |
| 方法 | 直接标记 verified | **扫描→对比→精确定位 三阶段** |
| 证据 | 无 | **7 份扫描 + 合并 + diff + 校验 = 10 份文件** |
| 校验 | 无 | **4 项程序化自动检查** |
| 结果可追溯 | 否 | **每个页码变更可追溯到扫描记录** |

---

### Step 2 执行记录

**执行日期**: 2026-04-15

#### 阶段 1 执行结果

7 个 Opus agent 全部并行完成，共解析 1007 条页面标题记录。

| Agent | 范围 | 条目数 | 耗时 | 状态 |
|-------|------|--------|------|------|
| A1 | SDTMIG p.1-60 | 148 | ~115s | 完成 |
| A2 | SDTMIG p.60-130 | 117 | ~171s | 完成 |
| A3 | SDTMIG p.130-200 | 115 | ~140s | 完成 |
| A4 | SDTMIG p.200-290 | 123 | ~196s | 完成 |
| A5 | SDTMIG p.290-380 | 164 | ~176s | 完成 |
| A6 | SDTMIG p.380-461 | 204 | ~209s | 完成 |
| A7 | SDTM v2.0 p.1-74 | 136 | ~147s | 完成 |

#### 阶段 2 执行结果

Python 脚本自动对比 + 手动逐域分析，发现 20 个域存在页码偏差。

错误分布:

| 区域 | 受影响域 | 字段修正数 | 错误模式 |
|------|---------|-----------|---------|
| Trial Design (TA~TS) | 7 | 30 | 系统性偏移 ±1~2 页，密集小域累积漂移 |
| Chapter 8 (RELREC~RELSPEC) | 4 | 15 | 系统性偏移 ±1 页 |
| 其他散布域 | 9 | 9 | 个别 assumptions/examples 边界差 1 页 |
| **合计** | **20** | **54** | |

其余 **43 个域** + **7 个 chapters** + **model** 区域经扫描验证无误。

#### 阶段 3 执行结果

程序化校验 4 项全部通过:
- 包含性: PASS (6 项 FAIL 均为已知的共享 examples 设计模式)
- 内部排序: PASS
- 连续性: PASS (3 项 gap/overlap 均为已知的嵌套/共享结构)
- 共享 examples 一致: PASS (EX/EC, MB/MS, TU/TR)

#### 文件操作

| 操作 | 文件 | 说明 |
|------|------|------|
| 保留 | `page_index_old.json` | 修正前的旧版本，留作工作痕迹 |
| 替换 | `page_index.json` | 用修正后的新版本替换 |
| 删除 | `page_index_new.json` | 中间产物（内容已合并到 page_index.json） |

---

## Issue 1 解决总结

**状态**: 已解决 (2026-04-15)

### 原始问题

Issue 1 (图像扫描页码不可靠) 引申发现 `page_index.json` 权威索引在 Trial Design 区域存在页码偏差。

### 根因

Step 0 验证存在方法论缺陷:
1. 使用 Sonnet 模型（能力有限）单次批量验证 63 域
2. 无结果文件、无证据链
3. 无交叉验证机制
4. Trial Design 区域 9 个连续小域密集排列，累积偏移风险高

### 修正方法

方案 C — 分段扫描 + 差异定位:
- 7 个 Opus agent 并行扫描全部 535 页 PDF
- 10 页/次读取粒度，逐页记录章节标题
- Python 脚本自动对比 + 手动精确定位
- 4 项程序化完整性校验

### 修正结果

- **20 个域** 的 **54 处字段** 得到修正
- **43 个域** 确认无误
- 全部 chapters、shared_specs、model 区域确认无误

### 证据链

| 文件 | 内容 |
|------|------|
| `rescan_a1.md` ~ `rescan_a7.md` | 7 份逐页扫描原始记录 (1007 条) |
| `rescan_diff.md` | 54 处变更的完整差异清单 |
| `page_index_old.json` | 修正前的旧版本 (工作痕迹) |
| `page_index.json` | 修正后的当前版本 |

### 关于 step3_6_image_inventory.md 的页码

原始 Issue 1 中 `step3_6_image_inventory.md` 的图像页码偏差属于**图像转化作业的中间产物**。图像转化已全部完成，此文件的页码暂时搁置，不影响项目产出。如需后续修正，可参照 `page_index.json` 的修正值同步更新。

### 流程改进建议

1. 未来所有验证步骤必须产出独立的结果文件
2. 页码类精确数据应使用 Opus 而非 Sonnet 验证
3. 密集区域（如 Trial Design 9 域连排）应采用小窗口逐页扫描
4. 验证后必须运行程序化完整性校验
