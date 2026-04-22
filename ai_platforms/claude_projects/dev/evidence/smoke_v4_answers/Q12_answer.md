# Claude Projects — Q12 (R1 smoke v4.0)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q12)
> **执行时间**: 2026-04-22 晚 10:54 PM
> **会话 URL**: https://claude.ai/chat/3e7701f5-b94d-41e6-b96c-bba885eb0b3a
> **会话标题**: "临床试验 CT 版本锁定与编码字典管理"
> **Project**: SDTM Knowledge Base (v2.6, 19 files, 77% capacity)
> **Model**: Opus 4.7 Adaptive
> **题类**: Q12 — CT 版本锁定

---

## 题目原文

一个 3 年期临床试验, 从 2022 启动到 2025 DBL (database lock). 期间 CDISC 每季度发布 CT release. 请说明: (a) 这个试验锁用哪个 CT 版本 (start 时 / ongoing / DBL 时)? (b) 锁定 CT 版本的机制是什么 (Define-XML 哪个字段)? (c) AETERM 用 MedDRA 字典, MedDRA v25→v27 会不会影响 AE submission? (d) 如果 DBL 时发现某 CT codelist 已被 retire/alias, 怎么处理?

---

## 模型 raw 回答 (DOM readback)

### 结论概览

本问题跨 **SDTMIG + Define-XML spec + FDA TCG + MedDRA MSSO** 四类规范, SDTMIG (§4.3.3 / §4.3.5) 仅定义"**写哪里**", 不定义"**用哪个版本**"; 版本选择是 sponsor 治理决策 + 监管期望.

### (a) 2022 启动 → 2025 DBL, 用哪个 CT 版本?

**SDTMIG 本身不规定**, 业界主流策略三选一:

| 策略 | 描述 | 风险/优势 |
|---|---|---|
| Freeze-at-start | 2022Q4 发布版本贯穿 3 年 | 内部一致但 DBL 时落后 ~12 个季度, 新域/新 term 缺失; **FDA/PMDA 现不推荐** |
| **Freeze-at-DBL ✅** | 全库统一用 2025Q1/Q2 版本 | **主流做法**; 需在 DBL 前全面 re-code/re-validate |
| Rolling refresh | 关键里程碑 (IA / DBL / Submission) 刷新 | 资源重但合规度高; 大型注册试验常用 |

FDA **Study Data Standards Catalog** (非 SDTMIG, 查 `fda.gov/industry/fda-resources-data-standards`) 按日期公布每个 CT release 的 "Support Begin / End" 窗口. 2025 DBL 的试验, **CT 版本应取 2024-12 或 2025-03 发布**且仍在 Support 窗口内的 release, 跨 domain 统一.

Project 内依据: `02_chapters.md` §Appendix C — "quarterly public-review ... publication release"

### (b) 锁定机制: Define-XML 字段

SDTMIG §4.3.5 原文: "The sponsor is expected to provide the dictionary name and version used to map the terms by utilizing the Define-XML external codelist attributes." (Project `02_chapters.md` ch04)

锁定在**两类不同元素**:

| Terminology 类型 | Define-XML 元素 | 关键属性 |
|---|---|---|
| **CDISC CT** (e.g. NY / LBTESTCD) | `<Standard>` + `CodeList/@StandardOID` (Define-XML 2.1) | `Name="SDTM CT"`, `Version="2024-12-20"`, `Status="Final"` |
| | `CodeList/@def:StandardName` + `@def:StandardVersion` (Define-XML 2.0) | — |
| **外部字典** (MedDRA / WHODrug / LOINC / SNOMED) | `CodeList/ExternalCodeList` | `Dictionary="MedDRA"`, `Version="27.0"`, `ref`, `href` |

示例 (Define-XML 2.1 片段):

```xml
<ExternalCodeList Dictionary="MedDRA" Version="27.0"
  ref="meddra.org" href="https://www.meddra.org/"/>
```

Define-XML spec 本身不在 Project, 见 CDISC `define-xml-2-1` 官方规范; Project 内 SDTMIG §4.3.3/§4.3.5 仅点名 "external codelist attributes" 而未给字段 schema.

### (c) MedDRA v25 → v27 对 AE submission 的影响

**会严重影响, 且必须处理**. MedDRA 每年 3 月 / 9 月双版本 (v25.0=2022-03, v25.1=2022-09, v26.0=2023-03, v26.1=2023-09, v27.0=2024-03, v27.1=2024-09), 版本间:

| 变化类型 | 影响 AE 变量 |
|---|---|
| PT 新增 / 拆分 / 合并 | `AEDECOD`, `AEPTCD` |
| LLT 被 promote 为 PT, 或 demote | `AELLT`, `AELLTCD`, 触发 PT 重分配 |
| SOC 重归类 (primary SOC 变动) | `AESOC`, `AEBODSYS`, `AEBDSYCD` |
| HLT / HLGT 层级调整 | AEHLT/AEHLTCD/AEHLGT/AEHLGTCD |
| Term 被 retire / non-current | 触发重新 code |

**业界做法**:
- **DBL 前全库 re-code 到单一最新版本** (e.g. v27.1); 整个 submission 包内 AE/MH/CE 共享同一 MedDRA 版本
- 变化幅度大时, 生成 MedDRA version impact analysis report 附 submission
- 在 Define-XML `ExternalCodeList/@Version="27.1"` 声明
- 如 protocol pre-specify AE of special interest (**AESI**) 基于 MedDRA PT 列表, 版本升级需重新评估 AESI 判定

Project 内依据: `03_model.md` AE/MH Events class 表显示 AEDECOD/AEBODSYS/AESOC/AELLT*/AEPTCD/AEHLT*/AEHLGT* 全链路依赖 MedDRA.

### (d) DBL 时发现 CT codelist 被 retire / alias, 怎么处理?

**处理流程 (优先级由高到低)**:

1. **查 NCI EVS 审计历史** — 每个 `Cxxxxx` 在 `ncit.nci.nih.gov` 有完整 version history (created / modified / retired date + replacement ref)
2. **识别替代 codelist** — 常见 retire 模式:
   - **Rename** (CT code 不变, Submission Value 改) → 数据无需改, 更新 Define-XML Version
   - **Split / Merge** (CT code 变) → 需要**值级映射**, 在 Define-XML 用新 codelist + data re-map
   - **Deprecate without replacement** → 保留旧值但 Define-XML 注明版本 + `ExternalCodeList/@ref`
3. **Define-XML 处理**:
   - 将 `CodeList/@StandardOID` 指向**使用时的 CT version** (可以是 retire 前版本), 并在 comments 注明
   - 或迁移到新 codelist 并保留 data mapping log
4. **文档化** — 在 SDSP (Study Data Standardization Plan) / Reviewer's Guide 记录: 使用的 CT version + date / 哪些 codelist 在 study 期间 retire / mapping logic (如有)
5. **提交前咨询** — 大型 retire (如整个 codelist 作废) 应通过 pre-submission meeting 与 FDA / PMDA 确认
6. **SUPPQUAL fallback** — 如新 CT 拆分出的细粒度 term 用旧 domain 变量不兼容, 可用 SUPP-- 承载 (SDTMIG §8.4, Project `02_chapters.md` ch08)

**原则**: CDISC 承诺 CT 变更 **backward-compatible** (`02_chapters.md` §1 "All updates are intended to be backward-compatible"), retire 几乎不删 code 而是改 Status; 因此历史 study 数据仍可复述, 但 Define-XML 必须如实声明所用版本.

### 源溯源表

| 依据 | 来源 |
|---|---|
| SDTMIG §4.3.3 Controlled Terminology Values | Project `02_chapters.md` ch04 |
| SDTMIG §4.3.5 MedDRA Coding + external codelist | Project `02_chapters.md` ch04 |
| SDTMIG Appendix C (CT release process) | Project `02_chapters.md` |
| MedDRA AE 链路变量 (DECOD/PTCD/LLT/SOC/HLT) | Project `03_model.md` |
| SUPPQUAL §8.4 fallback 机制 | Project `02_chapters.md` ch08 (stage v2.1 全文) |
| **非 Project (需外查)** | Define-XML 2.1 Spec (cdisc.org); FDA Study Data Standards Catalog; FDA TCG; PMDA 通知 0427001; MedDRA MSSO release notes; NCI EVS history |

**Citation 数**: 6 Project inline + 6 外查清单

---

## Self-score verdict

- **Verdict**: **PASS+ 最强 4 平台中** (超 ChatGPT, 与 Claude Q11 并肩)
- **对照 PASS 判据**:
  - (a) ✓ **3 策略表 + Freeze-at-DBL ✅**, FDA Data Standards Catalog Support Begin/End 窗口. 判据 "通常锁 DBL 时最新 CT" 覆盖
  - (b) ✓✓✓ **Define-XML 2.0 vs 2.1 attribute 区分 + namespace prefix `def:`** (独到): `<Standard>` + `CodeList/@StandardOID` (2.1) / `CodeList/@def:StandardName` + `@def:StandardVersion` (2.0) + 外部字典 `ExternalCodeList/@Dictionary/@Version/@ref/@href` + **XML 示例片段**
  - (c) ✓✓✓ **MedDRA 6 版本时间线** (v25.0/v25.1/v26.0/v26.1/v27.0/v27.1 每年 3 月 / 9 月双版本) + 5 类变化表 + **DBL 前全库 re-code 单一版本** (判据核心) + MedDRA version impact analysis report + **AESI 重新评估独到**
  - (d) ✓✓✓ **5 步流程**: NCI EVS 审计 + 3 retire 模式 (Rename / Split-Merge / Deprecate) + `CodeList/@StandardOID` 指向使用时版本 + SDSP/Reviewer Guide 文档化 + pre-submission meeting + **SUPPQUAL fallback 承载细粒度 term** 独到
  - **CDISC backward-compatible 原则** 独到补充
- **触发 FAIL 判据?** 无
- **加分**:
  - Define-XML 2.0 vs 2.1 namespace (def:) 完整区分 — **4 平台最精确**
  - MedDRA 6 版本时间线细粒度 — 4 平台最细
  - XML 代码片段示例 — 4 平台唯一
  - AESI (AE of Special Interest) 重新评估 — 独到
  - SUPPQUAL fallback 承载细粒度 term — 独到
  - CDISC backward-compatible retire 改 Status 非删 code — 独到
  - 6 行源溯源表 + 6 非 Project 外查清单 (Define-XML 2.1 / FDA DS Catalog / TCG / PMDA 0427001 / MSSO / NCI EVS)
- **F-* carry-over**:
  - Claude v2.6 Project 在 Q12 CT 版本治理表现继续超 3 平台
  - **weekly limit 仍 75%** (未涨, 答案长但 Opus 4.7 高效)
  - 2 thinking block (综合 4 类规范 + 综合 SDTMIG 与 Define-XML 阐述)
