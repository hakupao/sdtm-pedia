# Claude Projects — Q14 (I1 — AE+CE+MH 同事件 + DS 死亡跨域对齐)

> **Date**: 2026-04-22 晚 11:35 PM
> **Platform**: Claude Projects (SDTM Knowledge Base, v2.6 system_prompt, 19 files, Opus 4.7 Adaptive)
> **方法**: Chrome MCP cowork (ClipboardEvent paste + Enter)
> **生成时间**: ~3 min
> **Weekly limit**: 75% (未变)

---

## 题目原文 (v4.0)

受试者 Visit 5 突发心梗 (STEMI) 住院, 治疗 3 天出院, 在 Visit 7 因心衰死亡. 请回答:
(a) 这一系列事件里, 心梗本身可以同时记在哪些域 (AE / CE / MH)? 各自的业务边界什么?
(b) "死亡" 这个 terminal event 同时应该记 AE 和 DS 还是只一个?
(c) DS 域的 DSDECOD vs DSCAT 在"死亡"场景下值各是什么?
(d) 死亡时间的 ISO 8601 怎么跨域对齐 (AE.AESTDTC vs DS.DSSTDTC vs DM.DTHDTC)?

---

## Claude raw 回答 (DOM readback)

### 心梗 → 死亡场景的 SDTM 建模

> 整合SDTM域规范，厘清AE/CE/MH边界与死亡事件记录。

#### (a) 心梗 (Visit 5) 可以记在哪些域?

**结论**: 主域是 AE; CE 仅在特殊设计下并存; MH 不适用 (本次事件发生在研究期内)。

| 域 | 业务边界 | 本场景判定 |
|---|---|---|
| AE | "任何 untoward medical occurrence" in study period, 用于监管 AE/SAE 报告。STEMI 属于 SAE (住院 → AESHOSP=Y) | ✅ 必记 |
| CE | 非监管报告的临床事件: 疾病症状 / 预设疗效终点 (如 CV outcomes trial 的 MACE endpoint)。AE-SAE criteria 仍适用 --SER 变量 | ⚠️ 仅当 MI 是预设疗效终点 (如心血管结局研究) 才并存; 并存时 AE 仍然要记 |
| MH | 基线前的既往史 (before study start / informed consent) | ❌ 不适用; MH 仅记受试者入组前的 MI 病史 |

**关键判据** (CE assumption 1, §6.2.3):
> "The determination of events to be considered clinical events versus adverse events should be done carefully"
> "If any event is considered serious, then the serious variable (--SER)... apply"
> CE 典型用途: "episodes of symptoms of the disease under [study]" / "specific events as efficacy endpoints"

**实务建议**: 普通研究下 MI 只记 AE; 心血管结局研究下 MI 同时记 AE + CE, 用 RELREC 关联。

#### (b) 死亡事件: AE 和 DS 同时记录 (非二选一)

**结论**: AE + DS + DM 三者都必须更新; 可选 DD (死因细节); 用 RELREC 串联。

依据 SDTMIG §6.2.4 DS Example 4 + DM Example (Sudden Cardiac Death 场景):

| 域 | 目的 | 本场景记录 |
|---|---|---|
| AE | 致死 AE 事件本身 | 心衰 AE 记录: AEOUT="FATAL", AESDTH="Y", AESER="Y" |
| DS | 受试者研究参与状态终结 (disposition) | 一条 DSDECOD="DEATH" |
| DM | 人口学层的死亡标志 | DTHFL="Y", DTHDTC=<死亡日期> |
| DD | (可选) Death Details: 死因、死亡地点等裁定结果 | DDTESTCD="PRCDTH", DDORRES="Heart Failure" |
| RELREC | 串联上述记录 | DS.DSSEQ ↔ AE.AESEQ ↔ DD.DDSEQ same RELID |

CDISC 原文: "each of these domains serves a different purpose, even though the information is related" — 不是冗余。

#### (c) DS 在死亡场景下变量取值

基于 DS assumption 2 + 3 + Example 4:

| 变量 | 值 | 说明 |
|---|---|---|
| DSTERM | "Heart Failure" | 逐字 (verbatim) 填死亡原因, 即 CRF 上收集的文本 |
| DSDECOD | "DEATH" | 标准化值, 来自 NCOMPLT (**C66727**) codelist |
| DSCAT | "DISPOSITION EVENT" | 来自 **C74558**; 区分于 "PROTOCOL MILESTONE" / "OTHER EVENT" |
| DSSCAT | "STUDY PARTICIPATION" (推荐) | 明示是"研究参与"终结而非"study treatment"终结 |
| EPOCH | "TREATMENT" 或 "FOLLOW-UP" | 视死亡发生在哪个 epoch; Visit 7 通常仍在 TREATMENT epoch |
| DSSTDTC | ISO 8601 死亡日期 | 与 AE.AEENDTC / DM.DTHDTC 对齐 (见 d) |

**常见误区**:
- ❌ DSDECOD="ADVERSE EVENT" + DSTERM="Heart Failure" — 这是"因 AE 退出"(非致死性退出), 不是死亡
- ✅ DSDECOD="DEATH" + DSTERM="Heart Failure" — 死亡

#### (d) ISO 8601 死亡时间跨域对齐

三个变量必须指向同一死亡时刻, 精度 (日 vs 日+时) 应一致:

| 变量 | 含义 | 本场景值 (示例) |
|---|---|---|
| AE.AESTDTC | AE 起始时间 (心衰开始的时间, 不是死亡) | 2026-05-18 (Visit 7 发病日) |
| AE.AEENDTC | AE 结束时间 = 死亡时刻 (因 AEOUT=FATAL) | 2026-05-20T14:30 |
| DS.DSSTDTC | Disposition 事件发生时间 = 死亡时刻 | 2026-05-20T14:30 |
| DM.DTHDTC | 人口学记录的死亡日期/时间 | 2026-05-20T14:30 |

**对齐规则**:
- 必须完全一致: **DM.DTHDTC == DS.DSSTDTC == AE.AEENDTC** (当 AE 致死时)
- **AE.AESTDTC ≠ 死亡时刻**: 是事件开始的时间 (可能早于死亡几小时到几天)
- **精度约束**: 三者应使用相同的 ISO 8601 granularity — 若 DM.DTHDTC 精确到分钟, AE.AEENDTC 和 DS.DSSTDTC 也应精确到分钟

**易混变量**:
- **DS.DSDTC** = 记录采集日期 (可能晚于实际死亡, 若数据事后录入)
- **DD.DDDTC** = DD 记录的 collection date (死因裁定日期, 通常晚于 DTHDTC)

**参考示例** (来自 DM "Sudden Cardiac Death" Example):
```
AE.AESTDTC = 2011-01-10   ← 事件起
AE.AEENDTC = 2011-01-10   ← 事件终 = 死亡
DS.DSSTDTC = 2011-01-10   ← disposition 发生
DD.DDDTC   = 2011-01-12   ← 死因记录采集 (晚 2 天, ≠ 死亡时刻!)
DM.DTHDTC  = 2011-01-10   ← 与 AE.AEENDTC / DS.DSSTDTC 一致
```

### 源溯源

- knowledge_base/domains/AE/spec.md + assumptions.md (§6.2.1)
- knowledge_base/domains/CE/assumptions.md (§6.2.3, AE vs CE 判据)
- knowledge_base/domains/DS/spec.md + assumptions.md + Example 4 (§6.2.4)
- knowledge_base/domains/MH/assumptions.md (§6.2.7)
- knowledge_base/domains/DM/examples.md (Sudden Cardiac Death 多域联动示例)
- knowledge_base/model/03_special_purpose_domains.md (DM.DTHDTC/DTHFL 定义)

---

## Self-score verdict

**PASS+ 最强 (4 平台中)**

### 逐判据对照

| 判据 | Claude 答 | 判 |
|---|---|---|
| (a) AE 识别 on-study SAE | AESHOSP=Y ✓ | PASS |
| (a) AE/MH/CE timing 边界 | 3 域完整表 + 业务边界 + §6.2.3 citation ✓ | PASS+ |
| (a) 本题 STEMI 归属判断 | "普通研究仅 AE, CV outcomes 研究 AE+CE with RELREC" 实务建议 | PASS+ |
| (b) 死亡非互斥 AE+DS | AE+DS+DM+DD 四域 + RELREC 串联 (超判据) | PASS+ |
| (c) DSDECOD=DEATH + C66727 | ✓ NCOMPLT codelist | PASS |
| (c) DSCAT=DISPOSITION EVENT + C74558 | ✓ + 区分 PROTOCOL MILESTONE/OTHER EVENT | PASS+ |
| (c) DSTERM="Heart Failure" verbatim | **bonus** 精确区分 DSTERM vs DSDECOD | PASS+ |
| (c) 常见误区 ADVERSE EVENT vs DEATH | **独到** 避坑 note | PASS+ |
| (d) 日级对齐公式 | DM.DTHDTC==DS.DSSTDTC==AE.AEENDTC ✓ | PASS+ |
| (d) AESTDTC ≠ 死亡时刻 | **独到** 精确区分 AE.AESTDTC (事件起) vs AE.AEENDTC (事件终=死亡) | PASS+ |
| (d) 精度 granularity 一致 | "若 DM 精确到分钟, 三者都要" 业界精确 | PASS+ |
| (d) DS.DSDTC vs DSSTDTC / DD.DDDTC | **独到** 易混变量区分 | PASS+ |
| (d) Sudden Cardiac Death 示例 | **独到** 具体 ISO 8601 日期 + DD.DDDTC 晚 2 天 | PASS+ |

### 要点

- **最强**: 4 部分全部 Markdown 表格化, 结构清晰
- **独到**: DD (Death Details) 域 + DDTESTCD="PRCDTH" + DDORRES="Heart Failure" 精确
- **独到**: RELREC DS.DSSEQ ↔ AE.AESEQ ↔ DD.DDSEQ same RELID 串联机制
- **独到**: DS Example 4 / DM Sudden Cardiac Death Example 具体源定位
- **独到**: AE.AESTDTC ≠ 死亡时刻 的精确区分 (业界常犯错, 判据未列但正确)
- **独到**: DS.DSDTC (记录采集日期) vs DSSTDTC (事件日期) 精度易混变量警示
- **独到**: EPOCH="TREATMENT" or "FOLLOW-UP" 补充
- **独到**: 常见误区 DSDECOD="ADVERSE EVENT" vs "DEATH" 避坑 note
- **容错**: 精度 granularity 一致 (未要求 strict time-level equal)

### FAIL 判据触发?

全部 NO:
- "三域都记同一事件" → NO (分 timing + 业务规则)
- "AE/MH/CE 绝对互斥" → NO (给入组前 MH 例外 + CV 结局 CE 并存)
- 死亡只记 AE → NO (AE+DS+DM 必联动)
- DSDECOD 自定义 term → NO (DEATH/C66727)
- 日期不一致 → NO (给对齐公式)
- time-level 严格相等 → **NO** (用 "precision granularity 一致", 正确容错)

### Verdict: **PASS+ 最强 (4 平台中)** (判据全中 + 7 个 bonus 独到点 + Sudden Cardiac Death 示例)
