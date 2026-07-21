# Smoke Questions v2 — 双平台共享 (Node 4 重设)

> **版本**: v2.0 (draft 2026-04-21)
> **起因**: Node 3b 双平台 smoke 题 v1 设计根本性错误 — 字典式查询 + 位置探针 + 文件名引用, 非真实 SDTM 业务用户问法. 用户纠正反思后重做.
> **v2 设计原则**:
> 1. **零** filename 引用 (不出现 `04_terminology_core.md` / `02_domain_specs.md` 等)
> 2. **零** 位置描述 ("最前面 / 中段 / 末尾 / 第 N 条")
> 3. **零** 字典式查询 ("列 codelist 头 5 条 / 某 codelist 全部 Synonyms")
> 4. **全** 业务视角: SDTM 专家被 CDM / 统计程师 / 医学监查员 / 编程师问的真实问题
> 5. **对比可控**: 两平台跑**完全一样**的 10 题, 答案只要求对齐 SDTMIG v3.4 + SDTM v2.0 规则, 不考具体 NCI term 值
> 6. **Gemini 兼容**: Gemini C 方案舍弃 terminology 后, 10 题不依赖 codelist inline 值 (允许外部 NCI EVS 导航即可)
> 7. **ChatGPT 对应**: ChatGPT batch 2 含 assumptions + examples + terminology, 完全能答; 若 batch 2 未到位跑, 会因缺 assumptions/examples 而偏弱 (这本身是对比价值)

## 4 业务维度分布

| # | 维度 | 题数 | 说明 |
|---|------|:----:|------|
| I | **场景应用题** (SDTM 在特定临床业务场景下如何应用) | 3 | 合并用药拆记录 / SAE 住院 / 检验结果记录 |
| II | **规则判断题** (SDTM 规则/分类如何应用) | 3 | AESEV vs CTCAE / PK LLOQ 记法 / ARM-ARMCD 关系 |
| III | **EDC→SDTM 映射题** (源数据进 SDTM 时放哪) | 2 | 病史+仍服药双域 / 日期-时间精度 |
| IV | **域间鉴别题** (边界/依据) | 2 | SUPPAE 边界 / RELREC vs SUPP 选择 |

---

## 10 题全文 (双平台原封使用)

### I. 场景应用题 (3)

#### Q1. 合并用药同服两种降压药, CM 域记录拆分

> **题**: 受试者在同一天开始服用两种降压药 (氯沙坦 50 mg/日 + 氨氯地平 5 mg/日), 计划持续服用整个试验期, 目的是控制高血压. 请问在 SDTM CM 域里应该**拆成几条记录**? 每条记录**至少要填哪些 Core=Req 变量**? 简要说明字段含义 (不需要给具体 NCI Code).

**PASS 判据 (核心事实必中)**:
- 两条 CM 记录 (每个药各一条, 不能合并)
- 列出 CM Core=Req: `STUDYID` / `DOMAIN` (="CM") / `USUBJID` / `CMTRT` (治疗名) — 必含这 4 个
- 至少提到 `CMSEQ` (序列号) / `CMSTDTC` (开始日) / `CMINDC` (指征)
- 指征都是高血压 (反映同一业务场景但两条独立记录)

**FAIL 判据**:
- 合并成一条记录
- 错列 Req 变量 (比如把 CMCAT / CMSCAT 误列为 Req)
- 臆造不存在的变量名

#### Q2. AE 升 SAE, 住院相关 Serious 子变量填写

> **题**: 一位受试者服药后出现严重皮疹并因此住院 3 天治疗. Investigator 判断为药物相关的严重不良事件. 请问 SDTM AE 域中, 该如何记录这条事件的**严重性相关变量** (AESER 及其子变量)? 请列出需要填写的 SAE 判定类变量 (AESER / AESCONG / AESDISAB / AESHOSP / AESLIFE / AESDTH / AESMIE) 各自的含义和本例取值, "Y" 还是 "N"?

**PASS 判据**:
- AESER = Y (严重事件)
- AESHOSP = Y (导致住院)
- AESLIFE = N (非危及生命)
- AESDTH = N (非导致死亡)
- AESDISAB = N (非致残)
- AESCONG = N (非先天异常) / AESMIE = N (非重要医学事件, 住院已覆盖)
- 每个变量有简短中文/英文含义

**FAIL 判据**:
- AESER 填错 (未识别 SAE)
- AESHOSP 填 N
- 子变量缺失 >=2 个未说明

#### Q3. 实验室检验 HbA1c 超标, LB 域记录方式

> **题**: 受试者空腹 HbA1c 检验结果为 6.8%, 参考范围 4.0-6.0%, 实验室标注为"高". 请说明 SDTM LB 域中, 这次检验应该如何填写以下变量: `LBTEST` (检验名) / `LBTESTCD` (检验代码) / `LBORRES` (原始结果) / `LBORRESU` (原始单位) / `LBSTRESC` (标准化字符结果) / `LBSTRESN` (标准化数值) / `LBSTRESU` (标准化单位) / `LBNRIND` (参考范围指示)? 指出 `LBNRIND` 的三挡分类 (低 / 正常 / 高) 用什么代号.

**PASS 判据** (v2.1 2026-04-21 修订, 见文末变更记录):
- LBTEST = "Hemoglobin A1C" (或接近, 字符串 label)
- LBTESTCD = "HBA1C"
- LBORRES = "6.8" (字符)
- LBORRESU = "%"
- LBSTRESC = "6.8" / LBSTRESN = 6.8 (数值)
- LBSTRESU = "%" (或单位换算后的标准化单位)
- LBNRIND = **"HIGH"** (对齐 CDISC CT C78736 官方 submission value; 三档 **HIGH / LOW / NORMAL** 全写, 另有 ABNORMAL)

**FAIL 判据**:
- LBNRIND 答错值 (比如"H"/"L"/"N" 单字符非 CDISC CT C78736 官方 submission value; 或"高/低/正常"中文)
- LBORRES 和 LBSTRESN 类型弄混 (LBORRES 是字符, LBSTRESN 必须数值)
- 忘记 LBSTRESC vs LBSTRESN 区分

---

### II. 规则判断题 (3)

#### Q4. AESEV 三档 vs CTCAE Grade 映射

> **题**: SDTMIG v3.4 中, AE 域的 AESEV (Severity) 变量有几档取值? 和肿瘤试验常用的 CTCAE Grade 1-5 如何对应? 如果 EDC 里只收到 Investigator 填的 CTCAE Grade, AESEV 该怎么填? Grade 5 对应什么特殊处理?

**PASS 判据**:
- AESEV 三档: MILD / MODERATE / SEVERE (SDTMIG v3.4 标准三档)
- 对应关系: Grade 1 → MILD; Grade 2 → MODERATE; Grade 3-4 → SEVERE
- Grade 5 = 死亡 → AESEV 一般填 SEVERE 但 **AESDTH=Y** (Grade 5 是死亡不是严重性档位, 要走 AESDTH)
- 说明 AESEV 不等于 Serious (AESER), 是不同维度

**FAIL 判据**:
- 误列 AESEV 档位 (比如写 Grade 1-5 直接塞 AESEV)
- 混淆 AESEV (严重性) 与 AESER (是否 Serious)
- Grade 5 说错 (不识别是死亡)

#### Q5. PK 采样 LLOQ 以下值的记录

> **题**: 药代动力学 (PK) 研究中, 采样点的血药浓度检测值低于实验室定量下限 (LLOQ). 按 SDTMIG v3.4 PC 域 assumptions, 应该如何填写 `PCORRES` (原始结果) / `PCSTRESN` (标准数值) / `PCSTRESC` (标准字符) / `PCLLOQ` (定量下限)? 为什么不能直接写 0?

**PASS 判据**:
- PCORRES = "<LLOQ" (字符串, 带 "<" 符号)
- PCSTRESC = "<LLOQ" (字符标准化保留)
- PCSTRESN = NULL / 空 (数值列不能填, 因为 "<LLOQ" 不是数值)
- PCLLOQ = 实测 LLOQ 数值 (比如 0.5 ng/mL)
- 解释: 写 0 会误导后续 PK 统计 (AUC 会偏低), `<LLOQ` 保留不确定性

**FAIL 判据**:
- PCSTRESN 填 0 或 LLOQ 值
- PCORRES 写"BLQ"但未提 `<LLOQ` 约定
- 不解释为什么不填 0

#### Q6. DM.ARMCD vs DM.ARM 关系 + 中途换组

> **题**: 解释 DM 域的 `ARMCD` (Arm Code, 分组代号) 和 `ARM` (Arm Description, 分组描述) 的关系 (哪个是短代号, 哪个是 human-readable). 如果受试者因盲态问题在 Week 4 从 Arm A 转到 Arm B, 这个信息应该记录在 DM / SE / TA 哪个域? 分别说明各自的职责.

**PASS 判据**:
- ARMCD = 短代号 (比如 "A" / "PBO"), 最长 20 字符
- ARM = Full description (比如 "Drug 50 mg QD")
- ARMCD 是 TA (Trial Arms) 的键, DM.ARMCD 必须匹配 TA.ARMCD
- 中途换组: DM 只记**最终分组** (ACTARMCD / ACTARM); SE (Subject Elements) 记**实际经过的 element 序列**; TA 是**设计**非实际
- 答案含 ACTARM / ACTARMCD vs ARM / ARMCD 区分

**FAIL 判据**:
- ARMCD 和 ARM 哪个是代号说反
- 不识别 ACTARM (Actual Arm) 概念
- 把换组信息放 TA (TA 是设计不是实际)

---

### III. EDC→SDTM 映射题 (2)

#### Q7. 病史"高血压 10 年目前仍在服药", MH 还是 CM?

> **题**: EDC 系统里某字段值为 "病史: 高血压 10 年, 目前仍在服用氨氯地平 5 mg/日". 映射到 SDTM 时这条信息应该拆成哪些域的记录? 只进 MH? 只进 CM? 还是两域都要? 简要说明 MH 和 CM 的分工.

**PASS 判据**:
- **两域都要**:
  - MH 域: 记录病史"高血压", MHTERM / MHDECOD / MHSTDTC (病史起始) / MHENRF (ONGOING if 目前仍持续)
  - CM 域: 记录合并用药"氨氯地平", CMTRT / CMINDC (指征=高血压) / CMSTDTC (用药起始) / CMENRF (ONGOING if 仍在服药)
- MH 和 CM 各自职责: MH = 诊断/病史事实, CM = 实际用药
- 同一临床事件 (高血压) 在两域有不同视角记录

**FAIL 判据**:
- 只放一个域 (错漏)
- MH 和 CM 混淆 (比如把"氨氯地平"填进 MHTERM)
- 不解释"ONGOING" 的语义

#### Q8. 时间精度: 服药后 6 小时发 AE

> **题**: 受试者当天早 8:00 服药, 下午 2:00 发生头痛 (AE). EDC 里精确记录了时:分. SDTM AE 域的 `AESTDTC` (开始日期) 变量应该填什么? ISO 8601 精度是到日 (YYYY-MM-DD) 还是到分 (YYYY-MM-DDThh:mm)? 如果 EDC 只记到日, AESTDTC 怎么填? `--STDY` 类 Study Day 变量又是什么计算规则?

**PASS 判据**:
- ISO 8601 允许到分: AESTDTC = "2024-06-15T14:00" (精度允许到秒)
- 若 EDC 只记到日 → AESTDTC = "2024-06-15"
- ISO 8601 允许**部分精度** (精度降级保留)
- AESTDY = 相对 DM.RFSTDTC 的天数 (起始日当日 = Day 1 或 Day 0, SDTMIG 规定起始日为 Day 1), 负值表示研究前
- 说明 `--DY` 类变量计算规则: `AESTDY = AESTDTC_date - RFSTDTC_date + 1 (如果 AESTDTC >= RFSTDTC) / else = AESTDTC - RFSTDTC`

**FAIL 判据**:
- AESTDTC 格式错 (比如"06/15/2024"或"20240615")
- 不知道 ISO 8601 部分精度允许
- Day 0 vs Day 1 计算规则说错 (SDTM 规定 Day 1 为起始日非 Day 0)

---

### IV. 域间鉴别题 (2)

#### Q9. SUPPAE 边界: QNAM/QLABEL/QVAL 典型例子

> **题**: SUPPAE (Supplemental Qualifiers for AE) 的作用是什么? 什么情况下应该走 SUPPAE 而不是直接加 AE 域变量? 请举一个**典型例子**, 给出 QNAM / QLABEL / QVAL 三字段的完整示例 (场景自选, 无需 NCI Code).

**PASS 判据**:
- SUPPAE 存放**标准 AE 域未定义的补充变量** (非标准变量需要存 SUPP--)
- 标准 AE 变量**能放下的**不走 SUPPAE (避免重复)
- 典型例子 (其中一个合格即可):
  - QNAM="AERESPPD" / QLABEL="AE Respiration Pattern" / QVAL="Labored" (如果 EDC 收了"呼吸模式"但 AE 域无此变量)
  - QNAM="AECOV19" / QLABEL="AE Related to COVID-19" / QVAL="Y" (pandemic 场景新增, 非 SDTM 标准变量)
- QNAM 是短代号, QLABEL 是 label, QVAL 是实际值
- RDOMAIN / USUBJID / IDVAR / IDVARVAL 等键不用在自由解释里 (那些是 SUPPAE 内部必填结构变量, 可提但不是 example 核心)

**FAIL 判据**:
- 把 AE 标准变量 (如 AESEV) 当 SUPPAE 示例 (错位)
- 臆造的 QNAM 用了 "AE" 前缀超 8 字符 (规则违反)
- 不解释 SUPPAE 的"非标存储"本质

#### Q10. RELREC vs SUPPAE/SUPPCM 选择

> **题**: 一位受试者的某次 AE (头晕) 被 Investigator 判定和某合并用药 (复方降压药) 引起的血压下降有关. 这种"AE 由 CM 引起"的关联, 应该用 RELREC (Related Records) 记录, 还是用 SUPPAE / SUPPCM 存储? 解释两者的差异 (RELREC 负责什么 / SUPPAE/SUPPCM 负责什么), 说明本场景的选择理由.

**PASS 判据**:
- 应用 **RELREC** (不是 SUPP)
- RELREC 负责**跨域记录**或**同域跨记录**之间的**关系/关联**
- SUPP-- 负责**对单条记录补充非标变量**, 不是跨记录关系
- 本场景 = 两条独立记录 (AE 一条 / CM 一条) 之间有**因果/关联**, 正是 RELREC 设计目的
- 答案可提 RELREC 典型字段: RDOMAIN / USUBJID / IDVAR / IDVARVAL / RELID / RELTYPE

**FAIL 判据**:
- 选 SUPPAE 存 (错位; SUPPAE 只解一域内补充)
- 不识别 RELREC 跨域关系本质
- 把 RELREC 和 SUPP-- 作用说反

---

## PASS 阈值 + 评分规则

- **总分**: 10 题 × (0/1/0.5) = 0 / 5 / 10
- **PASS 题**: 核心判据全中 + 无重大 FAIL 判据 → 1 分
- **PARTIAL 题**: 核心判据中 ≥ 50% + 0-1 个小缺漏 → 0.5 分
- **FAIL 题**: 核心判据缺 ≥ 50% 或触 FAIL 判据 → 0 分

**Exit 阈值**:
- ≥ 8/10 PASS → 直接进 Phase 4 (回归 + 完整 A/B)
- 7/10 PASS → CONDITIONAL_PASS, 列 carry-over Phase 4 前修
- ≤ 6/10 PASS → FAIL_REWORK, 系统性问题 (system_prompt / 上传策略)

## 双平台执行

1. **两平台 Gem/GPT 就绪后** (Gemini C 方案完成上传 + ChatGPT batch 2 完成上传), 用户侧 + MCP agent **同日** 跑完 10 题
2. 题目**原文复制** (禁改字, 禁加文件名提示, 禁加 "第几条" 之类)
3. 两平台答案各落盘:
   - `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v2_results.md`
   - `ai_platforms/gemini_gems/dev/evidence/smoke_v2_results.md`
4. 主 session 做**跨平台对比表** (每题两边答案并排 + PASS/FAIL 判定 + 差异分析)
5. Rule D 双 reviewer 独立验 (第 12 + 13 种 subagent_type)

## 变更/修订记录

| 日期 | 变更 | 原因 |
|-----|------|------|
| 2026-04-21 | v2 draft 建立, 10 题全业务维度 | Node 3b v1 smoke 被用户纠正: 字典查/位置描述/文件名引用 3 错. Gemini 舍弃 terminology 后, 只能跑不依赖 codelist inline 的业务题 |
| 2026-04-21 | **v2.1 修订 Q3 LBNRIND 判据** | Node 4 smoke 后双 reviewer 独立交叉发现 (tracer 第 14 种 + test-engineer 第 15 种 subagent_type): 原 Q3 PASS 判据 "LBNRIND = H" 与 FAIL 判据 "写 HIGH/LOW 而非 H/L" 与 KB 源四处 (`LB/spec.md` L264 + `model/02_observation_classes.md` L168 + `LB/assumptions.md` L7 + `terminology/core/general_part4.md` L63-72 C78736) 冲突. CDISC CT C78736 官方 submission values = **ABNORMAL/HIGH/LOW/NORMAL 全写**, 无 "H/N/L" 短码. 原 Node 4 smoke 按 v2.0 (错判据) 评分, 双平台 Q3 FAIL 保留不追溯; v2.1 起 Phase 4 回归 A/B 按新判据. ChatGPT 答 "HIGH/LOW/NORMAL" 在新判据下 PASS, Gemini CO-2 拒答在新判据下仍 FAIL (拒答设计本身). |

---

*v2 smoke 题 ack 路径: 用户 review 本文件 → ack 题目 → 并行做 Gemini C 方案重组 + ChatGPT batch 2 合并 → 两平台上传完成后同日跑 smoke → 对比 + Rule D reviewer*
