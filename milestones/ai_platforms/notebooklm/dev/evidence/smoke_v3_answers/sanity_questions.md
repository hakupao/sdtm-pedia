# NotebookLM — P3.8 Sanity 3 Questions

> Date: 2026-04-22
> Account: bojiang.zhang.0904@gmail.com
> Notebook: SDTM Knowledge Base (42/42 sources, Chat Custom mode, custom instructions 8924/10000 chars)

---

## Q_sanity_1: AESER 的 Core 属性是 Req 还是 Exp?

**Answer**:

> AESER 的 Core 属性是 Exp（Expected），而不是 Req [1]。
>
> 变量详情：
> - Label: Serious Event [1]
> - Type: Char [1]
> - Role: Record Qualifier [1]
> - Core: Exp [1]
> - Controlled Terminology: C66742 [1] （允许的值为 Y / N [1]）
> - Purpose: 用于指示该不良事件是否为严重不良事件（Is this a serious event?） [1]。
>
> Boundary note: AESER 常常被误认为是必填项（Req），但按照标准它实际上是 Exp [1]。在 AE 域中，真正的 Req（Required）核心变量集合仅有以下 6 个：STUDYID, DOMAIN, USUBJID, AESEQ, AETERM, AEDECOD [144, 145, 146, 147, 148, 08_ev_adverse_ae.md]。

**Verdict**: PASS — 答 Exp 命中, 期望底座稳。

---

## Q_sanity_2: LBNRIND 的 submission values 有哪些?

**Answer**:

> LBNRIND (Reference Range Indicator) 的 Type 为 Char, Role 为 Variable Qualifier, Core 级别为 Exp, 受控术语 (Controlled Terminology) 为 C78736, 其用途是指示测量值相对于参考范围 (如 LBORNRLO / LBORNRHI 或 LBSTNRLO / LBSTNRHI) 的位置关系 [1]。
>
> 根据 CDISC 标准, 该变量的有效 Submission Values 包含以下四项 [2]:
> - ABNORMAL
> - HIGH
> - LOW
> - NORMAL
>
> 边界说明 (Boundary note):
> - 必须始终拼写出完整的单词, 严禁使用简写 (如绝对不可使用 H/L/N) [34_ct_lb.md]。
> - LBNRIND 仅指示数值落在参考范围之内或之外的相对客观位置, 不能用于指示结果的临床意义 (Clinical Significance) [1]。

**Verdict**: PASS — 4 个全写值 + C78736 + 严禁简写 boundary note 全命中。

---

## Q_sanity_3: CMINDC 用于哪种场景?

**Answer**:

> CMINDC 用于记录受试者接受特定伴随用药或治疗的适应症 (即给予该药物的医学状况或原因) [1, 2]。
>
> Variables involved: CMINDC | Char | Record Qualifier | Perm | (无) [41_variable_index.md]
>
> 具体应用场景与业务规则:
> 1. 记录医学状况/给药原因: 在 Interventions (干预) 一般观察类中, 当申办方需要收集"为何给予该干预"时, 使用 --INDC 变量 (在 CM 域即为 CMINDC) [1]。
> 2. 处理包含 "Other, specify" 的 CRF 数据: 当 CRF 上的适应症是一个带有 "Other, specify" 的勾选列表 (例如, 止痛药适应症选了 "OTHER", 并手写了 "Broken arm") 时, 申办方有多种处理方式:
>    - 若申办方希望对 CMINDC 维持严格的预设受控术语: 可将 CMINDC 赋值为 "OTHER" 或医学编码后的 "FRACTURE", 并将手写文本 ("BROKEN ARM") 存入补充限定词数据集 SUPPCM 中 (QNAM = "CMINDOTH") [3]。
>    - 若申办方不要求对该字段维持受控术语: 可以直接将合并后的具体文本 ("BROKEN ARM") 填入 CMINDC 中, 此时不需要使用 SUPPCM [3]。
>
> 您是否还需要了解 CM 域中与用药相关的其他"原因"变量 (例如用于记录剂量调整原因的 CMADJ, 或记录由于未进行评估而导致数据缺失原因的 CMREASND)?

**Verdict**: PASS — 显式命名 CMINDC = concomitant medication indication (合并用药指征), 引用 41_variable_index.md citation, 含 SUPPCM/CMINDOTH 高级语义。

---

## Sanity 总结

**3/3 PASS** — 底座 (instructions.md + 42 buckets indexing + Custom mode) 仍然全部稳, 可进 Step 3 跑 Q1-Q10。

| Q | Topic | Verdict |
|---|---|---|
| Q_sanity_1 | AESER Core=Exp | ✅ PASS |
| Q_sanity_2 | LBNRIND values | ✅ PASS |
| Q_sanity_3 | CMINDC scenario | ✅ PASS |
