# ChatGPT GPTs — Q12 (R1 smoke v4.0)

> **题库版本**: v4.0 (`ai_platforms/SMOKE_V4.md §2` Q12)
> **执行时间**: 2026-04-22 晚 (之前 session 已跑)
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83fdf-5248-83a8-9f9e-20290097d9b5
> **会话标题**: "临床试验 CT 版本问题"
> **system_prompt**: v2 (7568 bytes, N5.2 lock)
> **题类**: Q12 — CT 版本锁定 + Define-XML + MedDRA

---

## 题目原文

一个 3 年期临床试验, 从 2022 启动到 2025 DBL (database lock). 期间 CDISC 每季度发布 CT release. 请说明: (a) 这个试验锁用哪个 CT 版本 (start 时 / ongoing / DBL 时)? (b) 锁定 CT 版本的机制是什么 (Define-XML 哪个字段)? (c) AETERM 用 MedDRA 字典, MedDRA v25→v27 会不会影响 AE submission? (d) 如果 DBL 时发现某 CT codelist 已被 retire/alias, 怎么处理?

---

## 模型 raw 回答 (DOM readback)

> "我先把问题拆成 4 个点: CT 版本选择、Define-XML 锁定机制、MedDRA 升版影响、以及 retire/alias 的处理."
>
> "我已经找到两条关键硬依据: 一是 SDTMIG 明确要求把'本研究实际允许的 CT 值'写进 Define-XML; 二是外部字典如 MedDRA 的名称和版本要通过 Define-XML external codelist attributes 声明."

### (a) CT 版本选择

SDTMIG v3.4 **没有规定**"必须用开组时 CT"或"必须用 DBL 当季最新 CT". 它要求的是: 在 Define-XML 里提交本研究采用的 CT (或其引用), 并把本研究的 permissible value set 写清楚. 也就是说, **真正被"锁定"的是提交包里的 study-specific CT snapshot, 而不是试验开始日期本身**. 实践上, 3 年期研究通常会在 final SDTM / DBL / submission cut 选定一个版本并全研究一致使用, 而不是最终包里混用多个季度的 release.

源溯源: `knowledge_base/chapters/ch01_introduction.md`, `knowledge_base/chapters/ch04_general_assumptions.md`

### (b) Define-XML 锁定机制

锁定机制在 Define-XML 的 **external codelist**. 对外部字典 (如 MedDRA), SDTMIG 明确说要用 **Define-XML external codelist element / attributes** 提供字典名称和版本; 对 CT, 一般要在 Define-XML 中包含 controlled terminology 或其 reference, 并列出本研究允许值集合. SDTMIG 给到的表述是"external codelist element"/"external codelist attributes", **但没有展开到具体 XML attribute 名称**; 那个精确字段名属于 Define-XML 规范本身, 而不是 SDTMIG 文本.

源溯源: `knowledge_base/chapters/ch04_general_assumptions.md`, `knowledge_base/domains/AE/spec.md`, `knowledge_base/domains/AE/assumptions.md`

### (c) MedDRA v25→v27 影响

**先纠正一个常见说法**: **AETERM 不是 MedDRA 编码字段, AETERM 是 verbatim (原始报告词); MedDRA 影响的是 AEDECOD、AELLT/AELLTCD、AEPTCD、AEHLT/AEHLTCD、AEHLGT/AEHLGTCD 等字典派生字段**.

所以 MedDRA v25 → v27 当然可能影响 AE submission 内容: PT/LLT/SOC 映射可能变化, 进而影响 AEDECOD、AEBODSYS、层级字段、汇总计数和 reviewer 看到的分组. 但从 SDTM 结构合规看, **关键不是"必须 v27", 而是全研究一致并且在 Define-XML 里准确声明所用字典名和版本**. 如果在 DBL 前决定从 v25 全量重编到 v27, 可以; 但**应全研究统一重编, 并同步更新 metadata / reviewer guide**.

源溯源: `knowledge_base/domains/AE/spec.md`, `knowledge_base/domains/AE/assumptions.md`, `knowledge_base/chapters/ch04_general_assumptions.md`

### (d) retire/alias 处理

本套 SDTMIG 文本里没有找到逐字规则; 基于 SDTMIG 原则的稳妥处理:

**不要在同一最终 submission 里混用 old term 和 alias/new preferred term**.

两种可接受治理路径:
1. **冻结旧版本**: 如果研究一直按某个 CT release / MedDRA version 编码, 提交时就继续用这个版本, 并在 Define-XML 明确声明
2. **全量重映射到新版本**: 在 DBL 前把全研究重映射到新的有效 term / preferred term, 再提交新版本

无论走哪条路, 都要保证 **Define-XML 所声明的版本与数据中实际使用的 term/code 一致**.

- 若某个 codelist term 在新 release 已 retire, 但它并不是本研究 planned/permissible value set 的一部分, 那就**不要**把它放进 Define-XML; SDTMIG 只要求写本研究的 permissible values, 不是把整本 codelist 全搬进去
- 若因为历史数据原因必须保留旧 term, **最安全的做法是**: 保留原 study CT version, 不做半途局部替换; 必要时在 **Define comments / cSDRG** 解释

源溯源: `knowledge_base/chapters/ch04_general_assumptions.md`

### 实务化判断表

| 问题 | 建议 |
|---|---|
| 研究 2022 启动, 2025 DBL, CT 每季发版 | 不要按季度混用进最终包; 在 final submission cut 选一个 **single frozen version** |
| Define-XML 记什么 | 本研究用的 CT/reference; 外部字典写 **name + version**; 只列 **study permissible values** |
| MedDRA 25→27 | 会影响 AEDECOD / hierarchy / summaries; 不是 AETERM 本身 |
| term retire/alias | 要么保旧版本全研究一致, 要么全研究重映射到新版本; **不要局部混搭** |

**Citation 数**: 5+ inline source comments + 4 源文件 (ch01/ch04/AE/spec/AE/assumptions)

---

## Self-score verdict

- **Verdict**: **PASS+** (AETERM premise correction bonus + 独到 CT snapshot 论点 + detailed cSDRG 治理路径)
- **对照 PASS 判据**:
  - (a) ✓ SDTMIG 不 mandate + **锁定是 study-specific CT snapshot 非试验开始日期** (独到 reframe) + 实践 final SDTM/DBL 单一版本全研究一致. 判据 "锁 DBL 时, 整个 submission 用单一 CT 版本" 覆盖
  - (b) ✓ Define-XML external codelist element / attributes + 外部字典 name+version. **诚实声明** "具体 XML attribute 名超 SDTMIG 文本 scope" (vs Gemini 补 Dictionary/Version 具体名)
  - (c) ✓✓✓ **AETERM premise correction**: "AETERM verbatim, MedDRA 影响 AEDECOD/AELLT/AEPTCD/..." (与 N5.2 system prompt 锚点强一致) + 全研究一致 + Define-XML 声明 + 重编统一 + metadata/reviewer guide 更新. 判据 "所有 AE 应 recode 到统一版本" 覆盖
  - (d) ✓ 2 治理路径 (冻结旧 / 全量重映射) + Define-XML 版本与数据一致 + retire 但非 permissible 不进 Define-XML + 保留旧 term 需 cSDRG 解释. 判据 "旧值保留 Reviewers Guide 说明" + "remap 所有相关值" 都覆盖
- **触发 FAIL 判据?** 无
- **加分**:
  - **AETERM vs AEDECOD premise correction** = anti-hallucination 锚点完美生效 (独到 4 平台中)
  - "study-specific CT snapshot 非试验开始日期" 精准 reframe
  - "只列 study permissible values 不搬整本 codelist" 独到
  - 4 行实务化判断表 (问题→建议对照) 工程价值高
  - 诚实声明 attribute 名超 SDTMIG 文本 scope
- **F-* carry-over**:
  - ChatGPT v2 system prompt Q12 表现强 (PASS+ 与 Claude/Gemini 并肩, NotebookLM 弱 PARTIAL)
  - 2 preface message (拆题 → 硬依据找到) + 结论 + 判断表 = 完整 4 步推理
  - 5 source comments inline + 4 文件源溯源
