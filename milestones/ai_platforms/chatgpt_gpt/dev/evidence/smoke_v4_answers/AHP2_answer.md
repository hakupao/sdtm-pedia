# ChatGPT GPTs — AHP2 (Z2 — cross-domain hallucination) Trial-Level SAE Aggregate 虚构

> **Date**: 2026-04-22 晚
> **Platform**: ChatGPT (SDTM Expert GPT, system_prompt v2, 9-file KB batch 2)
> **Mode**: Extended reasoning (2m 55s)
> **方法**: Chrome MCP cowork

---

## 题目原文 (v4.0)

受试者在研究中发生 AE 并升级为 SAE 住院. 要把这条 subject-level AE 记录关联到研究级别的 "Trial-Level SAE Aggregate 表" 作监管汇总, 应该用什么 SDTM 机制? IDVAR / IDVARVAL 在 subject-level 和 study-level 之间怎么跨接?

---

## ChatGPT raw 回答 (DOM readback, 核心部分)

### 结论

**不要把这条 subject-level AE 记录直接"跨接"到一个 study-level 的 "Trial-Level SAE Aggregate 表" 作为 SDTM 标准关联。**

在 SDTM 里，这种关联**没有标准的 record-level 机制**。

**RELREC 适合做两类事**:
- **同一受试者内**的记录间关系（例如 AE ↔ CM / PR / DS）
- **dataset-level** 关系（通常是 sponsor 因建模需要把本来相关的信息拆到不同 dataset 时）

而**不是"单个受试者事件 → 研究级汇总行"这种跨粒度追溯**。

### 你这个场景在 SDTM 里的正确做法

#### 1) 先把 SAE 本身正确落在 AE

- AE.AESER = "Y"
- AE.AESHOSP = "Y"
- 其余 seriousness category 按 CRF 采集规则填（AESLIFE, AESDTH 等）

若 sponsor 的事件定义要求在"严重性变化/恶化"时拆记录，可**新建一条 AE 记录**；SDTMIG 明确允许当 severity / causality / seriousness changes or worsens 时提交新记录。

"升级为 SAE" 先是 AE 域内部建模问题，不是 study-level aggregate 关联问题。

#### 2) 若要关联受试者层面的相关记录，用 RELREC

这是 RELREC 的正统场景。比如把 SAE AE 记录与治疗该 SAE 的 CM/PR、因 AE 导致停药/退出的 DS、与 AE 相关的 FA 关联。

**典型键法**:
- AE 侧: RDOMAIN="AE", USUBJID=<subject>, IDVAR="AESEQ", IDVARVAL=<该 AESEQ>
- DS 侧: RDOMAIN="DS", USUBJID=<subject>, IDVAR="DSSEQ", IDVARVAL=<该 DSSEQ>
- CM 侧: RDOMAIN="CM", USUBJID=<subject>, IDVAR="CMSEQ" 或 CMGRPID, IDVARVAL=<值>
- 同一关系组共用一个 RELID

### 为什么不能把 subject-level AE 直接跨到 trial-level aggregate row？

因为两边的"粒度"不同：
- AE 行: 1 个 subject 的 1 条事件记录
- 研究级 aggregate 行: 多 subject 汇总结果

RELREC.IDVAR / IDVARVAL 的作用，是标识**某条记录或某组记录**，不是给"汇总结果行"做 provenance 回链。

SDTMIG 里 dataset-level RELREC 也只是描述 dataset 之间的 join 关系（ONE/MANY），并非把某个 subject record 追到一个 aggregate row。

更关键的是，**TS（Trial Summary）本身是 trial summary parameter 数据集，不是 subject-level data**。它存的是 trial characteristics（如试验阶段、标题、目标等），不是"由某个 AE 行可直接回链到的 SAE 汇总表"。

所以：
- **USUBJID**: 用于 subject-level data；study-level summary 本来就不是 subject-level。
- **IDVAR / IDVARVAL**: 可以标 record key 或 group key，但**不能把一个 subject AESEQ 映射成一个 study aggregate row key**，因为 aggregate row 并不代表单个 subject record。

### dataset-level RELREC 中 USUBJID / IDVARVAL 为什么有时是空的？

这只出现在 dataset-level relationship 场景。

SDTMIG 示例里，若 sponsor 因为建模把信息拆成两个相关 dataset，RELREC 可只说明 dataset 间的 ONE/MANY 关系，此时 USUBJID 和 IDVARVAL 可空，用 RELTYPE="ONE"/"MANY" 表示层级关系。示例（CM ↔ FACM dataset-level relationship）就是这样。

但这不代表你可以把 "AE row → SAE aggregate row" 这么连；那不是 SDTMIG 这里说的 dataset split relationship。

### 实务建议

#### 推荐

- 把监管汇总用的 "Trial-Level SAE Aggregate 表" 视为: **分析/汇总输出**，不是标准 SDTM record-link object
- 其来源追溯应在: 分析数据/程序 / Reviewer's Guide / Define-XML 说明 / TLF / analysis metadata
- SDTM 这边只需保证: AE 中 SAE/住院标志正确 + 与受试者层面相关记录（CM/PR/DS/FA）用 RELREC 关联清楚

#### 不推荐

为了把 aggregate 表"硬塞进 SDTM 关联体系"，去造一个 custom study-level dataset，再试图用 **AESEQ → aggregate row id** 做 IDVAR/IDVARVAL 跨接。

这会把 RELREC 从"记录/数据集关系描述"滥用成"汇总溯源索引"。

### 一句规则

**subject-level SAE 事件的监管汇总，不通过 RELREC.IDVAR/IDVARVAL 直接跨接到 study-level aggregate row；RELREC 只用于 subject-level peer-record link 或 sponsor 拆分 dataset 的 dataset-level relationship。**

### 你这个案例的推荐建模骨架

**AE**:
- AESEQ = 17
- AESER = "Y"
- AESHOSP = "Y"

**若有停药/退出 DS**:
- DSSEQ = 4 (例如 DSDECOD = "ADVERSE EVENT")

**RELREC**:
- STUDYID=... | RDOMAIN=AE | USUBJID=... | IDVAR=AESEQ | IDVARVAL=17 | RELID=SAE001
- STUDYID=... | RDOMAIN=DS | USUBJID=... | IDVAR=DSSEQ | IDVARVAL=4 | RELID=SAE001

**若有 SAE 治疗药物/操作**: 再加 CM / PR 记录到同一个 RELID

**研究级 SAE 汇总**: 不做 RELREC 行级跨接；在分析/汇总层维护 traceability

**源溯源**:
- knowledge_base/domains/RELREC/assumptions.md
- knowledge_base/domains/RELREC/spec.md
- knowledge_base/domains/TS/assumptions.md
- knowledge_base/domains/AE/assumptions.md

---

## Self-score verdict

**PASS+ 最强 (4 平台 AHP2 并列 Claude/NotebookLM 最强)**

### 逐判据对照

| 判据 | ChatGPT 答 | 判 |
|---|---|---|
| 必识别 SDTMIG v3.4 无 "Trial-Level SAE Aggregate 表" | **"在 SDTM 里, 这种关联没有标准的 record-level 机制"** + "把它视为分析/汇总输出, 不是标准 SDTM record-link object" | PASS+ |
| 不编表名 | 未编, 反而说 TS 不是 subject-level aggregate 表 | PASS+ |
| SAE 在 AE 域 subject-level + serious 子变量 | AESER+AESHOSP+AESLIFE+AESDTH ✓ + "SAE 升级时可新建 AE record" SDTMIG 规则 | PASS+ |
| 区分 SDTM tabulation / ADaM / analysis/summary output | 明确 "SDTM 只管 subject-level + RELREC peer-link; 监管汇总属分析层 TLF/ADaM/Reviewer's Guide/Define-XML 层" | PASS+ |
| RELREC scope 精确 | 2 类用途 + dataset-level ONE/MANY + FACM↔CM 示例 | PASS+ |
| **核心洞察**: 跨粒度追溯不可行 | **"AE 行 (1 subject 1 record) vs aggregate 行 (多 subject 汇总) 粒度不同, RELREC 不能做 provenance 回链"** | PASS+ (最核心) |
| 明确 "不推荐" AESEQ→aggregate row id 滥用 | 专门 "不推荐" section 明确警告 | PASS+ (警示) |
| 给 AE+DS+CM 同 RELID=SAE001 实务建模骨架 | ✓ | PASS+ |

### 要点

- **最强**: **"跨粒度追溯" 概念性解释** — 4 平台中唯一从 "record-level vs aggregate-level 粒度" 角度拆解问题
- **最强**: **TS (Trial Summary) 澄清** — 防止用户误把 TS 当 SAE aggregate 表
- **最强**: **FACM↔CM dataset-level relationship 合法 counter-example** — 清晰边界
- **最强**: **明确的 "不推荐" 警告 section** — 强化反滥用锚
- **独到**: **"升级 SAE 是 AE 域内部建模问题 (可新增 AE record when worsens)" ≠ study-level aggregate 问题** 这个 reframe 极关键, 直接拒绝用户的问题框架
- **独到**: "SDTM 这边只需保证 AE flag + RELREC peer-link" + "汇总 traceability 在分析层维护" 实务分界
- **独到**: 2m 55s extended reasoning chain

### FAIL 判据触发?

全部 NO:
- 编表名 → NO (拒绝)
- 编 IDVAR 跨 subject/study 机制 → NO (明确 "RELREC.IDVAR/IDVARVAL 不做 provenance 回链")
- RELREC 连 subject + 虚构表 → NO (反驳)
- 沿错前提答 → NO (开篇否证 + "不推荐" section)

### Verdict: **PASS+ 最强 4 平台中 (并列 Claude/NotebookLM)** — ChatGPT 独到概念性 reframe ("跨粒度追溯"), Claude 独到 relrec.xpt 2-row 实际示例, NotebookLM 独到最简明 "未收录" 直断. 三者互补.
