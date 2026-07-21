# Q14 (I1 — AE+CE+MH 同事件 + DS 死亡 + 跨域时间对齐)

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e84368-2684-83a9-8583-abef0193a541
> 提交时间: 2026-04-22
> Verdict: **PASS**
> 思考时长: 3m 3s

## 完整回答 (要点摘录)

### 结论先说

- 案例里 Visit 5 新发 STEMI **主落点通常是 AE**; 只有当方案把 MI / MACE / 心血管结局定义为 clinical event / endpoint 时, 才会另外进 CE
- **MH 只适合放研究开始前已存在的病史**, 不适合放 Visit 5 才发生的新发 STEMI
- "死亡"在这种场景下通常**不只一个域**:
  - DS: 记录受试者研究参与的终止/结局
  - DM: 记录受试者是否死亡及死亡日期时间
  - AE: 如果死亡由 AE 导致, 或"致死的那个医学事件"本身就是 AE, 也应记录
- DS "死亡"场景:
  - DS.DSCAT = "DISPOSITION EVENT"
  - DS.DSDECOD = "DEATH"
  - 常见还有 DS.DSSCAT = "STUDY PARTICIPATION"
- 时间对齐按变量语义, 不机械填一样

### (a) 心梗记在哪些域? AE/CE/MH 业务边界

**SDTMIG 把 AE/MH/CE 视为概念上相近的一组事件数据**, 差别主要在:
- 事件是研究前还是研究中开始
- 该事件在本研究里是否被视为监管上要报告的 AE

**1) AE 本案例默认主域**: AE 用于记录研究中收集的 AE; 范围与方案要求一致, sponsor 定义"一个 AE 事件"如何成记录.

**2) MH 不适合本例**: MH 是 Medical History, 用于研究**开始前**已存在的病史; Visit 5 新发 STEMI 是研究中事件, 不进 MH.

**3) CE 仅当方案把 MI/MACE 定为 endpoint 时**: CE 是 Clinical Events; sponsor 把心血管结局作为 adjudicated CV endpoint 收集时, 才在 CE 里同时建模 (与 AE 并存).

### (b) 死亡同时记 AE 和 DS 还是只一个

**通常不是只一个, 而是按用途分开记**:

**1) DS 应有**: SDTMIG 长期随访例子明确说, 若受试者生存状态 = "dead":
- 在 DS 中创建 study discontinuation / disposition 记录
- 同时在 DM 中填 DTHDTC 和 DTHFL

**2) AE 若死亡由 AE 导致, AE 也应有**:
- 若心衰是致死事件, 应有一条 AE = heart failure
- 用 **AESDTH = "Y"** + **AEOUT = "FATAL"** 表达 fatal AE

**3) 若方案把死亡作为 CE endpoint, CE 也可能有**: CE assumptions 明确举例某些研究把 death 本身作为 clinical event/endpoint 收集.

**本例最常见建模**:
- AE: STEMI (Visit 5, 住院) + Heart failure (Visit 7, fatal)
- DS: 研究参与因死亡终止
- DM: DTHFL, DTHDTC
- CE: 仅在方案要求记录 adjudicated CV endpoint 时再加

### (c) DS 域 DSDECOD vs DSCAT 在死亡场景下值

**两变量不是一回事**:
- **DS.DSCAT**: 大类 / category
- **DS.DSDECOD**: 标准化后的 disposition term

**DS assumptions 规定**:
- 当 **DSCAT = "DISPOSITION EVENT"** 时, DSTERM 放完成或未完成的原始/收集文本, **DSDECOD 用相应 controlled terminology**
- DSSTDTC 表示 disposition event 发生时间

**死亡场景具体值**:
- DS.DSCAT = "DISPOSITION EVENT"
- DS.DSDECOD = "DEATH"
- DS.DSSCAT = "STUDY PARTICIPATION" (常见)

### (d) 跨域 ISO 8601 时间对齐 (AE.AESTDTC vs DS.DSSTDTC vs DM.DTHDTC)

**变量语义**:
- AE.AESTDTC = AE 开始时间
- DS.DSSTDTC = disposition event 发生时间 (点事件)
- DM.DTHDTC = 实际死亡时间

**对齐原则**:
- DS.DSSTDTC 与 DM.DTHDTC 在"死亡即终止研究参与"时**通常应一致**
- AE.AESTDTC 只有在"致死事件本身"开始于死亡当时才会一样 (一般 ≠ DTHDTC)

**情形 A (题面最像): STEMI 3 天后已恢复出院, 后来另起心衰并死亡**
- AE 记录 1 (STEMI):
  - AESTDTC = Visit 5 onset
  - AEENDTC = 出院/MI episode 结束时间
  - AESHOSP = "Y"
- AE 记录 2 (Heart failure):
  - AESTDTC = Visit 7 前/当次发作时间
  - AEOUT = "FATAL"
  - AESDTH = "Y"
  - AEENDTC 可为死亡时间
- DS: DSSTDTC = 实际死亡时间
- DM: DTHDTC = 实际死亡时间
- 对齐: **DS.DSSTDTC = DM.DTHDTC**, 但 AE(STEMI).AESTDTC ≠ DTHDTC; AE(Heart failure).AEENDTC 可能 = DTHDTC

**情形 B: STEMI 持续恶化直到死亡, 中间无真正 resolution**:
- 一条 AE(STEMI) 从 Visit 5 持续到死亡
- AESTDTC = STEMI onset / AEOUT = FATAL / AESDTH = Y / AEENDTC = DTHDTC
- DSSTDTC = DTHDTC

**精度一致性原则**:
- 若只有日期: 各域填 `2026-05-12`
- 若知到分钟: 各域填 `2026-05-12T14:35`
- 不应出现 DM.DTHDTC = `2026-05-12T14:35` 但 DS.DSSTDTC = `2026-05-12` (除非源数据精度真不同)

### 一句话判定

- STEMI (Visit 5 新发) 默认进 AE, 不进 MH; 若方案把 MI 当 endpoint, 再加 CE
- 死亡通常同时反映在 AE (若 fatal AE) / DS (研究参与终止) / DM (死亡日期/标志)
- DS 场景: DSDECOD=DEATH, DSCAT=DISPOSITION EVENT, 常见 DSSCAT=STUDY PARTICIPATION
- DSSTDTC 与 DTHDTC 通常对齐到实际死亡时间; AESTDTC 只表示 AE 起始, 不必等于死亡时间

## 判据对齐

- (a) **AE / MH / CE 三域边界完整** ✓ (AE 默认主域 / MH 仅研究前 / CE 仅方案 endpoint); 主动指出 MH 不适合 Visit 5 新发事件 ✓
- (b) **死亡跨 AE+DS+DM 三域协同** ✓; AESDTH=Y + AEOUT=FATAL 双字段 ✓; DTHFL+DTHDTC 双字段 ✓; CE 仅 endpoint 时 ✓
- (c) DSCAT=DISPOSITION EVENT + DSDECOD=DEATH + DSSCAT=STUDY PARTICIPATION ✓; 二者职责区分 (大类 vs 标准化 term) ✓
- (d) **三变量语义全对** ✓ (AE 开始 / DS 点事件 / DM 实际死亡); DS.DSSTDTC = DM.DTHDTC 对齐规则 ✓; AE.AESTDTC 不一定等于 DTHDTC (按事件性质) ✓
- bonus: **情形 A vs 情形 B 双场景建模** (恢复后另起致死事件 vs 持续恶化致死) ✓
- bonus: **ISO 8601 跨域精度一致性原则** ✓ (date-only vs minute precision 跨域不混)
- bonus: AESHOSP=Y 住院字段在 STEMI 例子中明示 ✓
- bonus: 一句话判定收尾 (4 条) 极清晰 ✓

源溯源命中:
- `knowledge_base/chapters/ch04_general_assumptions.md`
- `knowledge_base/domains/CE/assumptions.md`
- `knowledge_base/domains/AE/assumptions.md`
- `knowledge_base/domains/DS/assumptions.md`
- `knowledge_base/domains/DM/assumptions.md`

## 归因

PASS — Pure generalization. 5 域 (AE/CE/MH/DS/DM) 跨域协同 + ISO 8601 精度对齐 + 4 子问题全完整. **(d) 情形 A vs 情形 B 双场景建模 + ISO 8601 跨域精度一致性原则**是非 trivial 加分项 (普通 LLM 易给单一对齐答案). 思考 3m 3s 与多域建模一致.
