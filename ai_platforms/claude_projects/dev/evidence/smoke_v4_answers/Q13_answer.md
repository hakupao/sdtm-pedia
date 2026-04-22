# Claude Projects — Q13 (R1 smoke v4.0)

> **题库版本**: v4.0
> **执行时间**: 2026-04-22 晚 11:17 PM
> **会话 URL**: https://claude.ai/chat/7d4fde53-19d2-4e66-ac87-253e6b4f893f
> **会话标题**: "SDTM在观察性研究和真实世界数据中的实现指南"
> **Model**: Opus 4.7 Adaptive + **web fetch** CDISC Observational v1.0 PDF
> **Thinking**: 4 block (验证 KB → 查 CDISC → fetch PDF → 验证 NS fabricated)
> **题类**: Q13 — RWD/Observational + ARMCD + NS premise trap

---

## 模型 raw 回答 (要点)

> "这份 'Considerations for SDTM Implementation in Observational Studies and RWD v1.0' **不在本 Project 知识库内**. 我先核查 Project 内 assumptions/terminology 锚点, 再用 web 核查该文档真实内容, 特别验证 (c) 里的 'NS' 说法."

### (a) Conformance rule 失效 (Observational v1.0 §3)

**v1.0 §3 把失效规则明确列为两层 + 3 类主题**:

**Dataset 级失效** (§3.1): TA / TE / SE / AE / LB / VS / EX / DS 数据集可能直接缺失. DM / TS 建议保留.

**Variable 级失效** (§3.2, 含明确 Rule ID):

| 失效类 | 变量 | Rule ID / Core | 失效原因 |
|---|---|---|---|
| Trial Design 结构 | EPOCH (TA), VISITNUM, ARM/ARMCD, ACTARM/ACTARMCD, ACTARMUD | CG0009, CG0016, CG0523, CG0524 | 无规程 arm/epoch/visit; "visit" 概念 RWD 不成立 |
| Reference 时间轴 | RFSTDTC, RFENDTC, RFXSTDTC, RFXENDTC, RFICDTC, RFPENDTC | CG0016 | 无统一 reference period; 只有出生年/参与起始月-年等不完整日期, --DY 无法推导 |
| FDA-expected Demographics | SITEID (Req), AGE, RACE | CG0014, CG0016 | RWD 可能无 site 概念; race 未按 FDA standard values 采集 |

v1.0 明确说这些不是规则缺陷而是**场景不适配**, 目前只能在 **SDRG** 中逐条说明; CORE 引擎未来可能允许按 "observational" profile 关闭这些规则.

### (b) ARM/ARMCD/ARMNRS (v1.0 §2.3 三条互斥路径)

关键: "arm" 在观察性研究里被**重新解释为 cohort**, 不是强行 null.

| 场景 | ARM/ARMCD | ACTARM/ACTARMCD | ARMNRS | TS 配套 |
|---|---|---|---|---|
| Cohort / Case-control 有队列 | cohort 名 (SMOKER/NONSMOKE, OCCUR/NOTOCCUR) | 同 | null | TSPARMCD=NCOHORT (队列数) |
| 无 arm 也无 cohort | null | null | 填 ARMNRS | — |
| ECA (External Control Arm) | ARM="External control", ARMCD="ECA" | 同 | null | TSPARMCD=STYPE="EXTERNAL CONTROL ARM" (非 CT, SDRG) |

**ARMNRS CT 值** (C142179, Extensible=Yes):
| Code | Submission Value |
|---|---|
| C49628 | SCREEN FAILURE |
| C142239 | NOT ASSIGNED |
| C142238 | ASSIGNED, NOT TREATED |
| C142240 | UNPLANNED TREATMENT |

**关键**: v1.0 本身**没有**为观察性研究新增 ARMNRS term. Cohort 示例 1 (COHORT-001) 干脆**不 null 化 ARM** 用 SMOKER/NONSMOKE 填充, 不触发 ARMNRS.

### (c) SUPPQUAL/NSV + NS premise (3-source 端到端检索)

**SUPPQUAL/NSV 完全仍适用**. v1.0 §3.2 RACE 失效处明确说 sponsor 应使用 **CRACE (Collected Race) 和 CETHNIC (Collected Ethnicity) NSV fallback** — 典型 NSV 用法.

**"NS (Non-Standard Domain)" — 不存在, fabricated 概念**:

| 源 | "NS" 作为 domain 是否出现 |
|---|---|
| Project KB (SDTMIG v3.4 + SDTM v2.0, 63 域 + Appendix B abbreviations) | ❌ 仅有 **NSV = Non-standard variable** (ch02 Appendix B) |
| CDISC Observational v1.0 PDF (Appendix B Glossary, 全文 §1-§4) | ❌ Glossary 仅列 ADaM/CDASH/CORE/Domain/ECA/NSV 等, **无 "NS" 或 "Non-Standard Domain" 条目** |
| 整份 v1.0 "nonstandard" 只出现 1 次 | 指 CRACE/CETHNIC — 仍是 **NSV 概念**, 非新 domain |

SDTM 生态唯一"非标准"机制是 **NSV**. Domain 层机制是既有的 **Custom Domain** (sponsor 2-letter 如 ZX 基于某 GOC), **从未叫 "NS domain"**.

v1.0 §1 开头明确自称 "not a standard. The content is informative, not normative" — 没有在 domain 层引入任何新机制.

### (d) SUPPDM observational 用法

| QNAM | QLABEL | 来源 |
|---|---|---|
| CRACE | Collected Race | v1.0 §3.2 (RACE fallback, FDA race 不能满足时) |
| CETHNIC | Collected Ethnicity | v1.0 §3.2 |
| (延伸) data 来源标识 / source system / 数据版本 | — | FDA RWD 指南 Appendix Table 1-2 |
| (延伸) cohort 辅助属性 (如 smoking pack-years 分组) | — | v1.0 cohort 主标识放 ARM, 辅助维度未规范, 典型落 SUPPDM 或 Findings |

**边界**: v1.0 没明确强制 SUPPDM vs 直接把 CRACE/CETHNIC 加到 DM. 若数据是**收集时就非 FDA standard**且值列表不可控 (如注册表自由文本 race), **走 SUPPDM (QNAM/QVAL/QORIG) 比直接加列更合适, 因为可承载 QORIG="COLLECTED" 语义**.

### 源溯源

- v1.0 条款: `https://www.cdisc.org/sites/default/files/2024-02/Considerations%20for%20SDTM%20Implementation%20in%20Observational%20Studies%20and%20Real-World%20Data%20v1.0.pdf` (Feb 2024 Final, 18 pp)
- ARMNRS CT 4 值: Project `knowledge_base/terminology/core/dm.md` (C142179, Extensible=Yes)
- DM assumptions: `knowledge_base/domains/DM/assumptions.md` §4
- NS 否证: Project `02_chapters.md` (SDTMIG Appendix B) + v1.0 Appendix B 全文双侧检索, 均无命中

---

## Self-score verdict

- **Verdict**: **PASS+ 最强 4 平台中 (web fetch + 3-source + 具体 Rule ID/C-code)**
- **对照 PASS 判据**:
  - (a) ✓✓✓ **Rule ID 具体 (CG0009/CG0014/CG0016/CG0523/CG0524)** + Dataset-level + Variable-level 2 层分类 + SDRG 解释路径 + CORE 引擎未来 "observational" profile
  - (b) ✓✓✓ **v1.0 §2.3 三条互斥路径** (cohort / no arm / ECA) + **ARMNRS C142179 4 值具体 C-codes 列全** + TSPARMCD=NCOHORT/STYPE 补充 + "v1.0 没为 observational 新增 ARMNRS term" 精确
  - (c) ✓✓✓ **NS premise 3-source 端到端检索否证** (Project KB / v1.0 PDF / SDTM 生态) + "nonstandard 在 v1.0 只出现 1 次指 CRACE/CETHNIC 是 NSV 非 domain" + v1.0 §1 "not a standard" 声明 + NSV/Custom Domain 2 路径正确
  - (d) ✓ CRACE + CETHNIC v1.0 显式 + 延伸推理 + **QORIG="COLLECTED" 语义独到**
- **加分** (4 平台中唯一):
  - **Web fetch 真实 PDF** (CDISC v1.0 URL)
  - **3-source crosscheck** (Project KB / v1.0 PDF / SDTM 生态)
  - **具体 Rule ID + C-codes** (CG0009 + C142239/C142238/C142240 + C49628)
  - v1.0 §1 "not a standard" 声明引用
  - QORIG="COLLECTED" SUPPDM vs DM 直接加列 的 SDTM 层语义区分
- **F-* carry-over**:
  - Claude Opus 4.7 Adaptive **web fetch + project KB crosscheck** 是独一无二 pattern
  - Weekly limit 仍 75% (未涨) — Opus 高效
  - 这是 Q11 + Q12 + Q13 3 题 PASS+ 最强 连续
