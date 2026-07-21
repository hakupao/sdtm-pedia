# Q5 (B2 — FA vs QS vs CE 边界) 三场景域映射

> Date: 2026-04-22 / Account: bojiang.zhang.0904@gmail.com / Fresh chat

---

## 题

以下 3 条 EDC 收集信息, 分别映射到 FA / QS / CE 哪个 SDTM 域?
- 场景 A: 受试者有既往 MH "类风湿性关节炎 15 年", 研究者在 Visit 4 对这条既往 MH 记录做量化评分 (用 28-joint tender/swollen count, 记 DAS28 评分 4.2). 这是对既往 MH 记录的量化 findings (非针对 AE).
- 场景 B: 受试者在 Visit 4 填 SF-36 生活质量问卷, 8 个维度每个打分.
- 场景 C: 受试者自诉 Visit 5 出现轻微头晕 (dizziness, 30 秒自愈), 研究者记录但不认为需医疗处理, 未达 AE 报告阈值.

每个场景: (i) 域名 + (ii) 理由 + (iii) Topic 变量值示例.

## NotebookLM 答 (full text)

这三个场景分别对应不同的 SDTM 域。以下是具体的映射结果、业务规则理由以及 Topic 变量的示例说明：

### 场景 A: 对既往 MH 的特定访视量化评分

映射结果: **FA (Findings About Events or Interventions)**

(i) 域名: FA (Findings About Events or Interventions)
(ii) 理由: FA 域用于存储关于某个事件 (Events) 或干预 (Interventions) 的发现 (Findings), 特别是当这些"发现"无法直接在原事件域中记录时 [1]。本场景中, 类风湿性关节炎是一个长期的既往病史事件 (记录在 MH 域中)。当在 Visit 4 这个特定时间点对该疾病的严重程度或体征 (如 28 关节计数、DAS28 评分) 进行"快照式"的量化评估时, 由于评估的时间点与该事件整体的发生时间不同, 符合 FA 域"基于特定时间点对某事件进行发现评估"的建模标准 [2]。
(iii) Topic 变量值示例:
- FA 域的 Topic 变量是 `FATESTCD` (Core: Req, Role: Topic) [3]
- 由于是对特定事件的评估, 还必须配合记录修饰词 `FAOBJ` (Object of the Observation, Core: Req) 来指明对象 [4]
- 示例: `FATESTCD` = `SEV` (Severity/Intensity) 或具体的评分短名, `FATEST` = `Severity/Intensity`, 同时 `FAOBJ` = `RHEUMATOID ARTHRITIS` [5]

### 场景 B: 填写 SF-36 生活质量问卷并打分

映射结果: **QS (Questionnaires)**

(i) 域名: QS (Questionnaires)
(ii) 理由: QS 属于 Findings 观察类, 专门用于存储已命名的、独立的问卷工具 (Instruments) 数据 [1]。这些问卷具有定义的标准结构、格式和内容, 通常包含概念相关的项目并产生量化得分 [1]。SF-36 是受 CDISC 控制术语严格支持的标准问卷, 必须存放在 QS 中 [6]。
(iii) Topic 变量值示例:
- QS 域的 Topic 变量是 `QSTESTCD` (Core: Req, Role: Topic) [7]
- 示例: 根据 NCI EVS 受控术语表, 若记录总分或维度分, 可使用 `QSTESTCD` = `SF36112`, 对应 `QSTEST` = `SF361-Physical Functioning 0-100 Score` (生理机能 0-100 评分); 若记录具体的单题, 可为 `QSTESTCD` = `SF36101`, 对应 `QSTEST` = `SF361-In General You Say Your Health Is` [8]

### 场景 C: 不构成 AE 的轻微头晕记录

映射结果: **CE (Clinical Events)**

(i) 域名: CE (Clinical Events)
(ii) 理由: CE 域用于记录研究中感兴趣但未被分类为不良事件 (Adverse Events, AE) 的临床事件 [1]。SDTMIG 明确指出, 对于某些构成体征或症状 (signs and symptoms) 但不满足 AE 报告阈值或定义的事件, 如果在临床上仍需要收集 (例如自诉症状或轻微发作), 应作为临床事件记录在 CE 域中 [9]。
(iii) Topic 变量值示例:
- CE 域的 Topic 变量是 `CETERM` (Core: Req, Role: Topic) [10]
- 示例: `CETERM` = `MILD DIZZINESS` 或 `DIZZINESS` (收集的原始报告术语) [10], 同时可配合标准字典派生变量 `CEDECOD` (Core: Perm, Role: Synonym Qualifier) = `Dizziness` 共同展示 [11]

## Verdict

| Criterion | Required | Got | Status |
|---|---|---|:---:|
| Scenario A → FA (quantification of MH event) | FA + FAOBJ pointing to MH event, NOT QS | FA + FATESTCD=SEV + FAOBJ=RHEUMATOID ARTHRITIS + 明确"对既往 MH 的快照评估" | ✅ |
| Scenario B → QS (SF-36 questionnaire) | QS + QSTESTCD | QS + QSTESTCD=SF36112/SF36101 + NCI EVS CT 引用 | ✅ |
| Scenario C → CE (subthreshold event) | CE + CETERM, NOT AE | CE + CETERM=DIZZINESS + 明确"未达 AE 报告阈值, signs and symptoms 落 CE" | ✅ |
| 边界辨别 (FA 不是 QS, CE 不是 AE) | 三域明确区分 | FA 强调"对既往事件的快照评估", QS 强调"已命名独立问卷工具", CE 强调"未达 AE 阈值" | ✅ |
| Topic 变量值示例齐全 | 三场景各含 Topic | FATESTCD/FAOBJ + QSTESTCD + CETERM/CEDECOD 全 | ✅ |

**Verdict**: ✅ **PASS** (1 / 1) — 5 项判据全中。Scenario A 正确识别 FA 域 (FAOBJ 指 MH 事件, 不混 QS); Scenario B 正确识别 QS (NCI EVS SF36112/SF36101 受控术语); Scenario C 正确识别 CE (signs and symptoms 子阈值场景明文)。加分: FAOBJ Required + QS NCI EVS 引用 + CE/AE 阈值边界明文。无 FAIL 触发。
