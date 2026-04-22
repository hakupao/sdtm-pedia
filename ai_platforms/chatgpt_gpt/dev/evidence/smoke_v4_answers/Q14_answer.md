# ChatGPT GPTs — Q14 (I1 — AE+CE+MH 同事件 + DS 死亡跨域对齐)

> **Date**: 2026-04-22 晚
> **Platform**: ChatGPT (SDTM Expert GPT, system_prompt v2, 9-file KB batch 2)
> **Mode**: Extended reasoning
> **方法**: Chrome MCP cowork (ClipboardEvent paste + Enter)
> **生成时间**: 4m 50s (extended reasoning chain)

---

## 题目原文 (v4.0)

受试者 Visit 5 突发心梗 (STEMI) 住院, 治疗 3 天出院, 在 Visit 7 因心衰死亡. 请回答:
(a) 这一系列事件里, 心梗本身可以同时记在哪些域 (AE / CE / MH)? 各自的业务边界什么?
(b) "死亡" 这个 terminal event 同时应该记 AE 和 DS 还是只一个?
(c) DS 域的 DSDECOD vs DSCAT 在"死亡"场景下值各是什么?
(d) 死亡时间的 ISO 8601 怎么跨域对齐 (AE.AESTDTC vs DS.DSSTDTC vs DM.DTHDTC)?

---

## ChatGPT raw 回答 (DOM readback)

### 结论先行

在你这个案例里，**Visit 5 的 STEMI（心梗）本身首选记在 AE；是否还要同时进 CE，取决于 protocol 是否把它定义成 clinical event / endpoint；不应记成 MH（除非说的是既往或研究开始前已存在的心梗/冠心病史）**。

而**"死亡"不是只记一个域**：只要它导致受试者终止研究参与，**DS 一定要有**；如果死亡同时又是某个不良事件的结局，则 **AE 也要反映 fatal outcome**。DM 里还要补 **DTHDTC / DTHFL**。这些域表达的是不同语义，不是重复。

### (a) STEMI 本身可同时记哪些域？业务边界是什么？

#### 1) AE — 可以，而且在你这个场景通常应当记

AE.AETERM / AE.AEDECOD 用来表示 on-study adverse event。AE assumptions 明确说，AE 收的是受试者用药后出现的 "untoward medical occurrence"，但 **AE 的收集范围要与 protocol 一致**；赞助方也可以按方案**不把某些 efficacy endpoint 收进 AE**。

对你的案例，Visit 5 突发 STEMI 且住院 3 天，通常会是一个 AE 记录，例如：
- AE.AETERM = collected verbatim term
- AE.AEDECOD = coded term (如 ST elevation myocardial infarction)
- AE.AESER = Y
- AE.AESHOSP = Y
- AE.AESTDTC = STEMI 实际起始日期/时间
- AE.AEENDTC = 出院/缓解/事件结束日期时间 (若已结束)

AE 的 Outcome CT 里包含 **FATAL**，所以若某 AE 以死亡告终，**AE.AEOUT** 可取 FATAL；死亡结果也可由 **AE.AESDTH** 标识。

#### 2) CE — 也可以，但前提是它被 protocol 定义为 clinical event / endpoint

CE assumptions 说得很直接：**clinical event 和 adverse event 的划分要谨慎决定**；**protocol 定义为 clinical event 且不视为 AE 的事件，应放 CE**。同时，某些研究会把 **TIA / stroke / death** 这类事件作为 **efficacy endpoint** 进 CE。

所以，Visit 5 的 STEMI 在下面两种情况下可以进 CE：
- 它是方案预先定义的 cardiovascular clinical event
- 它是 endpoint adjudication / efficacy endpoint 事件

并且如果 CE 里的事件被视为 serious，CE 也要带 serious 变量和 serious flags (即 CE 可用 AE 模型里的 serious 相关变量)。

#### 3) MH — 这个 Visit 5 新发 STEMI 不应记

通则明确说，**AE、MH、CE 本质上都是 event 型数据，区别主要在于：事件开始时间相对 study start 的位置，以及它是否被视为本研究的 regulatory-reportable AE**。

因此：
- **研究开始前就存在**的既往心梗 / 冠心病 / 心衰病史 → **MH**
- **Visit 5 新发** STEMI → 不是 MH

若受试者基线已有冠心病或既往 MI，可在 MH.MHTERM / MH.MHDECOD 表示既往史；但 **Visit 5 这次急性发作** 仍应另记 AE 或 CE，不要拿 MH 顶替。MH 还支持 "active/ongoing" 这类既往且仍存在的状态。

#### 实务判断

- STEMI at Visit 5: **AE** 必记
- 若 protocol 把 MI 定义为 cardiovascular endpoint: 再记 **CE**
- **MH** 只放既往 MI / CAD / CHF 病史，不放这次 Visit 5 新发 STEMI

### (b) "死亡"这个 terminal event 是 AE+DS，还是只一个？

**不是只一个。通常是：DS 必有；AE 是否也有，取决于死亡是否是某个 AE 的结局。**

#### DS 一定要有

DS 用来表达 study participation / treatment disposition。长随访示例明确说：如果受试者 survival status = dead，**最终 disposition 要存入 DS；DM.DTHDTC 和 DM.DTHFL 必须适当填充**。

SS assumptions 也再次强调：如果 status = DEAD，**死亡日期放 DM，最终 disposition 放 DS**；SS 只放状态问题/回答本身。

#### AE 视情况也要有

如果 Visit 7 的心衰死亡是一个 adverse event 的结局，那么：
- 那个致死 AE (例如 HEART FAILURE) 要在 AE 里表达
- AE.AEOUT = FATAL
- AE.AESDTH = Y (若该变量被收集/使用)

#### 为什么这不算"重复"？

因为语义不同：
- **AE**：描述医学事件本身及其结局
- **DS**：描述受试者研究参与/治疗的 disposition
- **DM**：给出 subject-level 的死亡日期/死亡标志

DD assumptions 甚至明确说，**DD 域不是用来把 AE.AEOUT / AE.AESDTH / DS.DSTERM 再抄一遍的**；这些死亡相关信息本来就应分散在各自语义正确的标准域里。

#### 套到你的病例

- Visit 5: STEMI 作为 AE (±CE)
- Visit 7: HEART FAILURE 作为致死 AE (若按 AE 收集)，另加一条 DS 记录表示因死亡而结束 study participation，DM.DTHDTC = 实际死亡日期/时间

### (c) 死亡场景下，DSDECOD vs DSCAT 应填什么？

#### DSCAT

这里应是：**DS.DSCAT = "DISPOSITION EVENT"**。因为死亡导致的是 study participation / study treatment 的 disposition，不是 protocol milestone，也不是 "OTHER EVENT"。DS assumptions 对 DSCAT 的 3 类定义就是：**DISPOSITION EVENT / PROTOCOL MILESTONE / OTHER EVENT**。

#### DSSCAT

通常还应区分：
- **DS.DSSCAT = "STUDY PARTICIPATION"**: 表示整项研究参与因死亡终止
- 若研究还单独收 treatment disposition, 则可再有一条 DS.DSSCAT = "STUDY TREATMENT" (或具体 treatment 名称)

#### DSDECOD

DS assumptions 说：
- 当 DSCAT = "DISPOSITION EVENT" 时，DSTERM 放 "COMPLETED" 或未完成的具体 verbatim reason
- DSDECOD 用 **NCOMPLT** 的标准术语去标准化这个原因

所以在死亡场景下，模式应是：
- DS.DSTERM = collected verbatim (例如 DEATH 或 DIED DUE TO HEART FAILURE)
- DS.DSDECOD = 对应的标准 disposition term，通常会是 **DEATH**

**这里我需要坦诚一点**：本次检索命中了 DS 的规则，但没有把 NCOMPLT 值表片段本身打出来，所以我把 DSDECOD = DEATH 标成"通常应如此"，而不是假装我已经在术语表片段里直接看到了该值。基于 DS 业务规则，这个判断是高度一致的。

### (d) 死亡时间在 AE.AESTDTC / DS.DSSTDTC / DM.DTHDTC 之间怎么对齐？

#### 先给原则

**三者都用 ISO 8601 extended format**
- YYYY-MM-DD 或 YYYY-MM-DDThh:mm:ss
- 允许部分日期/时间，不知道的部分可截断或按 ISO 8601 规则表示不确定性

**三者语义不同，不要求机械相等**
- AE.AESTDTC = AE 的起始时间
- DS.DSSTDTC = disposition event 的发生时间
- DM.DTHDTC = 死亡本身的日期/时间

**Study day 算法要跨域一致**：所有 --DY / --STDY / --ENDY 都相对 DM.RFSTDTC 统一计算。

#### 具体到你的病例

##### 1) AE.AESTDTC

它应是 AE 开始时间，不是"死亡时间字段"。所以：
- Visit 5 的 STEMI 记录：AE.AESTDTC = STEMI 发作时间
- Visit 7 的致死 HEART FAILURE 记录 (若收 AE)：AE.AESTDTC = 心衰开始/恶化时间

只有当 AE term 本身就是 "DEATH" 时，AE.AESTDTC 才会等于死亡时间。否则，**fatal AE 的 AESTDTC 完全可以早于 DM.DTHDTC**。

##### 2) DM.DTHDTC

这是 subject-level 的实际死亡日期/时间。只要确认受试者 dead，就必须在 DM 填 DTHDTC / DTHFL。所以你这个例子里：DM.DTHDTC = Visit 7 死亡的真实日期/时间。

##### 3) DS.DSSTDTC

DS assumptions 说得很关键：DSSTDTC 是 disposition event 的时间，而且**不一定等于**导致停研那个观察在别的域里的日期/起止时间。它给过示例：**AE 在 6/1 开始，6/6 决定停药，AE 在 6/8 结束 — 这三者就不相等**。

因此在死亡场景：
- 若**死亡本身就是研究参与终止的那个 disposition event**: DS.DSSTDTC 常常会与 DM.DTHDTC 相同
- 但若是**后续随访/电话联系时才确认死亡并做最终 disposition**: DS.DSSTDTC 可能等于最终 disposition/contact 的时间, 而 DM.DTHDTC 仍是实际死亡时间。长随访示例就明确把最终 disposition 放在最终 follow-up contact 的 DS 里。

### 这例最稳妥的建模图景

#### Visit 5

**AE: STEMI**
- AESTDTC = 发作时间
- AESER = Y
- AESHOSP = Y
- AEENDTC = 出院/结束时间

**CE**: 只有当 protocol 把 MI 定义成 clinical event / endpoint 时再加

**MH**: 不放这次新发 STEMI；只放既往 MI/CAD/CHF

#### Visit 7

**AE**: 若心衰是致死 AE，则单独一条 HEART FAILURE, AEOUT = FATAL, 必要时 AESDTH = Y

**DS**: 一条死亡导致的 disposition
- DSCAT = DISPOSITION EVENT
- DSSCAT = STUDY PARTICIPATION
- DSTERM = verbatim death reason
- DSDECOD = 对应标准 disposition term (通常 DEATH)

**DM**:
- DTHFL = Y
- DTHDTC = 实际死亡日期/时间

### 源溯源

- knowledge_base/domains/AE/assumptions.md
- knowledge_base/domains/CE/assumptions.md
- knowledge_base/domains/MH/assumptions.md
- knowledge_base/domains/DS/assumptions.md
- knowledge_base/domains/DD/assumptions.md
- knowledge_base/domains/SS/assumptions.md
- knowledge_base/chapters/ch04_general_assumptions.md

---

## Self-score verdict

**PASS+** (4-part 判据全中 + anti-hallucination boundary 坦诚)

### 逐判据对照

| 判据 | ChatGPT 答 | 判 |
|---|---|---|
| (a) AE 识别 on-study SAE | ✓ + AESER+AESHOSP+AEOUT+AESDTH 完整 | PASS |
| (a) AE/MH/CE timing 边界 | §ch04 通则 "event 型数据区别在 timing + regulatory-reportable 阈值" ✓ | PASS+ |
| (a) 本题心梗归属 | on-study 排 MH, AE 必记, CE 条件 (endpoint) | PASS+ |
| (b) 死亡非互斥 AE+DS | AE+DS+DM 三域 + DD "不是抄录 AEOUT/AESDTH" 独到 | PASS+ |
| (c) DSDECOD=DEATH + NCOMPLT | ✓ + **坦诚 boundary**: 未直接看到 NCOMPLT codelist 片段, 标"通常应如此" | PASS (带 anti-hallucination bonus) |
| (c) DSCAT=DISPOSITION EVENT | ✓ + 区分 PROTOCOL MILESTONE/OTHER EVENT | PASS+ |
| (c) DSSCAT=STUDY PARTICIPATION | **bonus 独到** 区分 STUDY TREATMENT | PASS+ |
| (c) DSTERM vs DSDECOD | ✓ verbatim vs standardized 区分 | PASS+ |
| (d) 三者语义不同 "不要求机械相等" | **独到** "三者语义不同, 不要求机械相等" 正确反判据过严 | PASS+ |
| (d) DS 示例 6/1→6/6→6/8 不相等 | **独到** 具体 DS assumption 示例 | PASS+ |
| (d) 死亡 vs 后续随访 disposition 场景 | **独到** 长随访场景 DS.DSSTDTC ≠ DM.DTHDTC | PASS+ |

### 要点

- **最强**: 同时给出 2 种死亡场景 (即时死亡 = DTHDTC / 后续随访确认 = DSSTDTC offset), 业界准确
- **最强**: AE.AESTDTC ≠ 死亡时间 的精确区分 (AE 起始 vs 结束)
- **独到**: Study day 算法 --DY/--STDY/--ENDY 相对 DM.RFSTDTC 统一
- **独到**: DD assumptions "不是抄录 AEOUT/AESDTH/DSTERM" 语义非重复
- **anti-hallucination bonus**: DSDECOD=DEATH 坦诚 "未直接在 codelist 片段打出, 基于规则判断"
- **实务建模图景**: Visit 5 + Visit 7 完整 2-层示例

### FAIL 判据触发?

全部 NO:
- "三域同事件记" → NO
- "AE/MH/CE 绝对互斥" → NO (MH 例外 + CE 条件并存)
- 死亡只记 AE → NO
- DSDECOD 自定义 → NO
- 日期不一致 → NO (给 2 种对齐场景)
- time-level 严格相等 → **NO** ("不要求机械相等" 正确容错)

### Verdict: **PASS+** (判据全中 + anti-hallucination boundary 诚实 + 独到的后续随访 DS scenario)
