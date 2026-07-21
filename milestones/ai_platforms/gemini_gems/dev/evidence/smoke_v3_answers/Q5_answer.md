# Q5 — Gemini SDTM Expert 回答 (B2 — FA vs QS vs CE 三场景)

> 期望核心: A=FA (DAS28 → FAOBJ 指向 MH) + B=QS (SF-36) + C=CE (dizziness 未达 AE 阈值)
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/630f80fa72e0114b
> 时间: 2026-04-22
> Mode: Thinking (Gemini 3 Thinking, 非 Pro — 误触; Thinking 属高阶模式, 作为 Pro 替代有效)

## 完整回答

根据 SDTMIG v3.4 及知识库中的域定义与业务场景规则，针对这三个 EDC 收集场景的映射建议如下：

### 场景 A：既往病史（MH）记录的量化评分（DAS28）

(i) 域名：FA (Findings About)

(ii) 理由：DAS28 评分是对已存在的既往病史（Rheumatoid Arthritis）进行的后续量化评估。根据 FA 域的定义，它专门用于收集关于已在其他域（如 AE, MH, CM）中记录的事件或干预措施的发现（Findings）。在此场景下，FA 通过 --OBJ 指向 "RHEUMATOID ARTHRITIS"，并通过 --LNKID 或 --LNKGRP 与 MH 域的具体记录关联。

(iii) Topic 变量值示例：FATEST = "DAS28 Score"（或具体的子项，如 "Number of Tender Joints"）。

源路径：knowledge_base/domains/FA/spec.md 及 knowledge_base/domains/FA/assumptions.md
段落：Assumptions Section 1 ("FA is intended to collect findings about an event or intervention already captured in another domain.")

### 场景 B：SF-36 生活质量问卷评分

(i) 域名：QS (Questionnaires)

(ii) 理由：SF-36 是临床试验中标准的受试者自评问卷（Quality of Life Questionnaire）。SDTMIG 明确规定，所有问卷、评分量表（Rating Scales）或分级评价的数据应存入 QS 域，除非该量表在其他专门域（如评价反应的 RS 域）有明确定义。

(iii) Topic 变量值示例：QSTEST = "SF-36 Physical Functioning Domain Score"（SF-36 的 8 个维度之一）。

源路径：knowledge_base/domains/QS/spec.md 及 04_business_scenarios_and_cross_domain.md
段落：04 §1.21 ("Questionnaires (QS) - Standard tools like SF-36, EQ-5D.")

### 场景 C：未达到 AE 报告阈值的临床事件

(i) 域名：CE (Clinical Events)

(ii) 理由：受试者自诉的 "头晕" 属于临床事件。由于研究者判定其未达到 AE 报告标准，因此不能放入 AE 域。CE 域专门用于捕获那些既不是 AE（未达标），也不是 MH（发生在研究开始后），且不属于处置（DS）或暴露（EX）的临床事件。这在记录"感兴趣但不构成 AE 的事件"时非常典型。

(iii) Topic 变量值示例：CETERM = "DIZZINESS"。

源路径：knowledge_base/domains/CE/spec.md 及 04_business_scenarios_and_cross_domain.md
段落：04 §1.5 ("Non-AE clinical events (CE) - Subjective reports not meeting AE criteria.")

### 总结表

| 场景 | 目标域 | 核心逻辑 | 关键变量 |
|------|--------|----------|----------|
| A (DAS28) | FA | 针对 MH 记录的追加 Findings | FATEST, FAOBJ |
| B (SF-36) | QS | 标准问卷/量表数据 | QSTEST, QSCAT |
| C (Dizziness) | CE | 记录了但未达 AE 标准的事件 | CETERM, CESEV |

## 判据对齐

| 维度 | 期望 | 实际 | Hit |
|------|------|------|-----|
| A (DAS28 → FA + FAOBJ 指 MH) | FA + FATEST + FAOBJ/LNKID 指向 MH | FA + FATEST="DAS28 Score" + FAOBJ="RHEUMATOID ARTHRITIS" + LNKID/LNKGRP 关联 | ✅ |
| B (SF-36 → QS) | QS + QSTESTCD + QSCAT="SF-36" | QS + QSTEST="SF-36 Physical Functioning Domain Score" + QSCAT 暗示 | ✅ |
| C (轻微头晕 → CE) | CE + CETERM | CE + CETERM="DIZZINESS" | ✅ |

## Verdict

**PASS** — 3/3 场景域全对 + FA 通过 FAOBJ 指向 MH 记录 + QS 明确 SF-36 标准化问卷 + CE 明确非 AE 阈值. 本题为 borderline (04 §1.19 QS vs FA 有基础), Gemini 在 B/C 场景各引用 04 §1.21 / §1.5 — **弹药包直接命中协助**. A 场景 FA 指向 MH (非 AE) 的业务推理自洽, 未走入 04 §1.19 主覆盖的 "FA→AE" 路径, 显示 generalization 有效.

- 04 引用: 2 次 (§1.21 QS / §1.5 CE). 本题属 borderline 题, 04 弹药包作为辅助命中但 FA→MH 方向是 generalization 补强
- CO-2 触发: 无
- Score: 1 / 1
