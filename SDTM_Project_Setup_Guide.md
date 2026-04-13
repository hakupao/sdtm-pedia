# SDTM Mapping Expert — 搭建指南

> 本文档指导如何使用 `knowledge_base/` 目录中的文件搭建 Claude Project。
> 最后更新：2026-04-13

---

## 1. 项目概述

**目标**：在 Claude chat 中新建一个 Project，作为你的 SDTM Mapping Expert，覆盖以下场景：
- SDTM Mapping 开发参考
- SDTM 合规审查
- SDTM 概念学习
- Controlled Terminology 查询

**标准版本**：SDTM IG v3.4 + SDTM v2.0
**语言**：中英混合（中文解释 + 英文术语）
**知识库**：`knowledge_base/` 目录，共 293 个 Markdown 文件

---

## 2. 操作步骤

### Step 1：新建 Project

1. 打开 [claude.ai](https://claude.ai)
2. 左侧栏找到 **Projects** → 点击 **+ Create project**
3. **Project name**：`SDTM Mapping Expert`
4. **Description**：`SDTM IG v3.4 & SDTM v2.0 标准查询专家。支持 domain mapping 参考、变量定义查询、Controlled Terminology 验证、合规审查及概念解释。覆盖全部 63 个 domains，中英混合回答。`

### Step 2：设置 Instructions

1. 进入 Project 后，点击右上角 **设置图标** 或 Project 页面的 **Set custom instructions**
2. 将 `SDTM_Project_Instructions.md` 文件中代码块里的内容 **完整复制粘贴** 到 Instructions 输入框
3. 保存

### Step 3：上传 Knowledge Base 文件

这是最关键的一步。所有文件来自 `knowledge_base/` 目录。进入 Project Knowledge 区域，按以下优先级上传：

#### 优先级 1 — 全局索引 + 模型 + 通用章节（13 个文件）

```
knowledge_base/INDEX.md                          ← 全局索引导航

knowledge_base/model/concepts_and_terms.md       ← 变量角色、限定符子类
knowledge_base/model/observation_classes.md       ← Interventions/Events/Findings 模型
knowledge_base/model/special_purpose_domains.md   ← DM/CO/SE/SV/SM 模型
knowledge_base/model/associated_persons.md        ← AP 域规则
knowledge_base/model/study_level_data.md          ← Trial Design 模型
knowledge_base/model/relationship_datasets.md     ← RELREC/SUPP--/RELSUB 模型

knowledge_base/chapters/ch01_introduction.md
knowledge_base/chapters/ch02_fundamentals.md
knowledge_base/chapters/ch03_submitting_data.md
knowledge_base/chapters/ch04_general_assumptions.md  ← 含 ISO 8601、Study Day、SUPP 规则
knowledge_base/chapters/ch08_relationships.md
knowledge_base/chapters/ch10_appendices.md
```

#### 优先级 2 — 高频 Domain 三件套（每个 domain 含 spec + assumptions + examples）

以下为最常查询的 domain，每个上传 3 个文件：

| Domain | 说明 | 上传文件 |
|--------|------|---------|
| DM | Demographics | `domains/DM/spec.md` `assumptions.md` `examples.md` |
| AE | Adverse Events | `domains/AE/spec.md` `assumptions.md` `examples.md` |
| CM | Concomitant Medications | `domains/CM/spec.md` `assumptions.md` `examples.md` |
| LB | Laboratory Tests | `domains/LB/spec.md` `assumptions.md` `examples.md` |
| VS | Vital Signs | `domains/VS/spec.md` `assumptions.md` `examples.md` |
| EX | Exposure | `domains/EX/spec.md` `assumptions.md` `examples.md` |
| MH | Medical History | `domains/MH/spec.md` `assumptions.md` `examples.md` |
| DS | Disposition | `domains/DS/spec.md` `assumptions.md` `examples.md` |
| EG | ECG Test Results | `domains/EG/spec.md` `assumptions.md` `examples.md` |
| PE | Physical Examination | `domains/PE/spec.md` `assumptions.md` `examples.md` |
| SC | Subject Characteristics | `domains/SC/spec.md` `assumptions.md` `examples.md` |
| SV | Subject Visits | `domains/SV/spec.md` `assumptions.md` `examples.md` |
| SE | Subject Elements | `domains/SE/spec.md` `assumptions.md` `examples.md` |
| IE | Inclusion/Exclusion | `domains/IE/spec.md` `assumptions.md` `examples.md` |
| SUPPQUAL | Supplemental Qualifiers | `domains/SUPPQUAL/spec.md` `assumptions.md` `examples.md` |
| RELREC | Related Records | `domains/RELREC/spec.md` `assumptions.md` `examples.md` |

共 48 个文件（16 domain × 3）

#### 优先级 3 — 受控术语（按需选择）

```
knowledge_base/terminology/core/ae.md                ← AE 相关 codelists
knowledge_base/terminology/core/dm.md                ← DM 相关
knowledge_base/terminology/core/disposition.md       ← Disposition 相关
knowledge_base/terminology/core/interventions.md     ← CM/PR/SU 等相关
knowledge_base/terminology/core/vs.md                ← Vital Signs
knowledge_base/terminology/core/eg_part1.md          ← ECG (part 1-3)
knowledge_base/terminology/core/lb_part1.md          ← Laboratory (part 1-4)
knowledge_base/terminology/core/general_part1.md     ← 通用 codelists (part 1-5)
knowledge_base/terminology/core/special_purpose.md   ← 特殊用途域
knowledge_base/terminology/core/trial_design.md      ← Trial Design
knowledge_base/terminology/core/findings_about.md    ← FA/SR 相关
```

> 注意：terminology/ 中有 91 个文件，部分文件较大。先上传以上常用文件，其余按需补充。

#### 优先级 4 — 其余 Domain 三件套

剩余 47 个 domain 的三件套（141 个文件）：
AG, BE, BS, CE, CO, CP, CV, DA, DD, DV, EC, FA, FT, GF, HO, IS, MB, MI, MK, ML, MS, NV, OE, OI, PC, PP, PR, QS, RE, RELSPEC, RELSUB, RP, RS, SM, SR, SS, SU, TA, TD, TE, TI, TM, TR, TS, TU, TV, UR

每个 domain 上传 `domains/[DOMAIN]/spec.md`、`assumptions.md`、`examples.md` 三个文件。

> **注意**：Claude Project 的 Knowledge Base 有文件大小和数量限制。如果遇到限制：
> - 优先上传 **优先级 1 和 2** 的文件（61 个文件，覆盖核心需求）
> - Terminology 文件较大，根据常用 domain 选择性上传
> - 如果空间不够，可以先跳过优先级 4 的小众 domain

### Step 4：验证 Project 是否工作

创建完成后，在 Project 中开一个新 chat，测试以下问题：

1. **变量查询**：`AE domain 有哪些 Required 变量？`
   → 应引用 domains/AE/spec.md 中 Core = Req 的变量
2. **业务规则**：`DM 的 RFSTDTC 怎么填？`
   → 应引用 domains/DM/assumptions.md 中的相关规则
3. **Mapping 问题**：`我有一个 source 字段叫 "Medication Name"，应该 map 到 CM 的哪个变量？`
   → 应综合 domains/CM/spec.md + assumptions.md 回答
4. **Terminology 查询**：`SEX codelist 有哪些可选值？`
   → 应引用 terminology/core/dm.md 中的 Sex codelist
5. **概念解释**：`SDTM 的 Findings class 和 Events class 有什么区别？`
   → 应引用 model/observation_classes.md
6. **实现示例**：`EX 的剂量调整怎么表示？`
   → 应引用 domains/EX/examples.md 中的数据表

如果都能正确引用 knowledge base 内容回答，说明 Project 配置成功。

---

## 3. 文件清单

### 源文件 → 知识库映射

| 源文件 | 说明 | 产出文件 |
|--------|------|---------|
| SDTMIG_v3.4.xlsx | 变量元数据 | `domains/*/spec.md` (63 个) |
| SDTM Terminology.xlsx | 受控术语 | `terminology/core/` (42) + `questionnaires/` (43) + `supplementary/` (6) |
| SDTMIG v3.4 PDF | 实施指南 | `domains/*/assumptions.md` (63) + `domains/*/examples.md` (63) + `chapters/` (6) |
| SDTM_v2.0.pdf | 数据模型 | `model/` (6) |

### 产出统计

| 类别 | 数量 |
|------|------|
| Domain 三件套 (spec + assumptions + examples) | 63 × 3 = 189 |
| Terminology | 91 |
| Model | 6 |
| Chapters | 6 |
| INDEX.md | 1 |
| **总计** | **293** |

---

## 4. 建议补充的资源

你目前的资料已经覆盖了 SDTM 的核心内容，但以下资源可以进一步增强：

### 可以补充的（如果你有访问权限）：
1. **CDASH IG v2.2** — 数据采集标准，可以建立 CRF → SDTM 的映射参考
2. **最新 Controlled Terminology** — 当前知识库基于 2022-09-30 版，CDISC 每季度更新
3. **Define-XML** 规范 — 如果你需要生成 define.xml
4. **Pinnacle 21 / OpenCDISC Validation Rules** — 合规检查的具体规则列表

---

## 5. 后续可以做的事

- [ ] 将你项目特定的 **Mapping Specification** 也加入 Knowledge Base
- [ ] 如果有 sponsor-specific 的 SDTM 要求或 annotation，也可以上传
- [ ] 定期更新 Controlled Terminology（CDISC 大约每季度发布一次更新）
- [ ] 如果获取到 CDASH 资料，用同样的方式转换为 markdown 后上传

---

*文档创建于 2026-04-07 | 更新于 2026-04-13 | 基于 SDTM IG v3.4 + SDTM v2.0*
