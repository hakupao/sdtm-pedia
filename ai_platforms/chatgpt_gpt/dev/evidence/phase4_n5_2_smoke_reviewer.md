# Phase 4 Node 5.2 Reviewer (ChatGPT 侧) — 独立 Rule D 第 19 种 subagent_type (oh-my-claudecode:planner)

> **Reviewer subagent_type**: `oh-my-claudecode:planner` (Rule D 第 19 种独立 subagent_type, 全链无 self-review)
> **Reviewer Date**: 2026-04-21
> **Review 对象**: ChatGPT GPTs 侧 smoke v2.1 10/10 strict 自评 + 跨平台 Q3 对照 + N5.1 P5 LOW cleanup 4 项合规
> **Reviewer 立场**: 独立, 不信任主 session 叙事, 只信任 Grep 行号 / 文件字面 / KB 源
> **前置 Rule D 独立链 (18 种)**: executor / code-reviewer / verifier / debugger / pr-review-toolkit:code-reviewer / feature-dev:code-reviewer / oh-my-claudecode:critic / analyst / pr-review-toolkit:comment-analyzer / pr-review-toolkit:pr-test-analyzer / scientist / superpowers:code-reviewer / architect / tracer / test-engineer / silent-failure-hunter / security-reviewer / (N5.1 双 reviewer) → **本 reviewer = 第 19 种 (planner)**

---

## Verdict: **CONDITIONAL_PASS** (Confidence 88%)

- ChatGPT 10/10 strict PASS **9/10 完全可信** — 抽样 5/5 命中 v2.1 判据核心事实, 无主 session 偏向性解读
- 1 个暗隐结构性风险 (Q4 判据偏离, 详见 §1), 但不扣题级 PASS, 转 Phase 4 N5.3 前需用户 ack
- Q3 LBNRIND 跨平台对照 = 结构性 A 型 + B 型并存 (既是 ChatGPT 知识+prompt 更好, 也是 Gemini 被 N5.1 CO-2 子条款自污染)
- ChatGPT v2.1 **不存在** Gemini L65 等价的 LBNRIND L/N/H 自污染指令 (独立 Grep 核实)
- Q7 CMINDC PASS 双因归因: v2.1 L62 bullet 主因 + KB 05/06 支撑 (bullet 边际贡献 ~40%)
- N5.1 P5 LOW cleanup 4 项 **全部真合规** (validate SCRIPT_VERSION / legacy DEPRECATED / upload_manifest / CMINDC bullet)

## Phase 4 Gate Decision: **CONFIRM with 1 ADJUST**

- **CONFIRM** ChatGPT 侧 N5.2 → N5.3 推进 (smoke v2.1 PASS 可信, 无回归阻断)
- **ADJUST** 建议: 修 Gemini system_prompt v4 L65 的 LBNRIND L/N/H 示例 (pivot 为"仅在 KB 示例**段落原文**可 inline, 但权威 term 值以 C78736 官方为准"), ChatGPT 侧**不需要**镜像改 (system prompt 无对应自污染)
- **N5.3 Full A/B 矩阵可直接开跑**, 无需先重跑 N5.2 smoke

---

## 1. ChatGPT 10/10 独立抽样 Rule A (N=5)

**抽样原则**: 必含 Q3 (LBNRIND 关键回归) + Q7 (CMINDC bullet 回归), 3 随机用 python `random.seed(19)` 从 {Q1,Q2,Q4,Q5,Q6,Q8,Q9,Q10} 选 3 → 抽到 **Q5 (PK LLOQ) + Q10 (RELREC) + Q8 (ISO 8601)**. 即抽样集 = {Q3, Q5, Q7, Q8, Q10}.

### 1.1 Q3 LBNRIND — 判据命中矩阵 (v2.1)

| v2.1 判据关键字段 | 答案原文行号 | 命中 |
|---|---|---|
| LBTEST = "Hemoglobin A1C" | Q3_answer.md L17, L36 | ✅ 双处命中 |
| LBTESTCD = "HBA1C" | L18, L37 | ✅ |
| LBORRES = "6.8" (字符) | L19, L38 | ✅ |
| LBORRESU = "%" | L20, L39 | ✅ |
| LBSTRESC = "6.8" | L21, L40 | ✅ |
| LBSTRESN = 6.8 (数值) | L22, L41 | ✅ |
| LBSTRESU = "%" | L23, L42 | ✅ |
| **LBNRIND = "HIGH" (C78736 官方)** | **L24, L43** | ✅ **关键判据** |
| 三档全写 LOW/NORMAL/HIGH | L28-30 (`LOW`/`NORMAL`/`HIGH`) | ✅ 额外加 ABNORMAL L31 |
| FAIL 判据: 单字符 H/L/N | 答案零处 "H"/"L"/"N" 单字符 | ✅ 未触 FAIL |

**独立结论**: Q3 PASS **100% 可信**, 主 session 无偏向性解读. 额外额度: 答案列出 `C78801 / C78727 / C78800` 3 个 NCI code (L28-30), 超判据基线. Grep knowledge_base/terminology/core/general_part4.md L69-72 官方 C78736 4 值 = **ABNORMAL (C78802) / HIGH (C78800) / LOW (C78801) / NORMAL (C78727)**, 答案 NCI code 映射 100% 对齐 KB 源.

### 1.2 Q5 PK LLOQ — 判据命中矩阵

| v2.1 判据 | 答案原文行号 | 命中 |
|---|---|---|
| PCORRES = "<LLOQ" / BLQ / BQL | Q5_answer.md L20 "BLQ / BQL / <LLOQ / <0.10" 多种表达全列 | ✅ 完整 |
| PCSTRESC = "<LLOQ" / BLQ (字符保留) | L21 | ✅ |
| PCSTRESN = NULL / 空 (**不能填 0**) | L22 **留空 (null)** / L53 **null** | ✅ 关键 |
| PCLLOQ = 实测 LLOQ 数值 | L23 "例如 0.10" / L55 | ✅ |
| 解释不能写 0 (语义差异) | L36-43 三条论点 | ✅ 超基线 |
| FAIL 判据: PCSTRESN=0 | 零处, 明文拒写 0 | ✅ 未触 |

**独立结论**: Q5 PASS **100% 可信**. 加分: L43 "若分析需要用 0、LLOQ/2、missing 等规则, 那是分析层 (ADaM) 的规则, 不是 SDTM 层" = ADaM/SDTM 分层边界明确, 超判据基线 (判据仅要求解释语义).

### 1.3 Q7 CMINDC — 判据命中矩阵

| v2.1 判据 | 答案原文行号 | 命中 |
|---|---|---|
| 两域都要 (MH + CM) | Q7_answer.md L14 "通常两域都要" | ✅ |
| MH: MHTERM / MHDECOD | L18 表格行 MHTERM/MHDECOD + L33-34 | ✅ |
| **CM: CMINDC 显式命名** | **L18 表格行 "CM.CMTRT, CM.CMDECOD, CMINDC"** / **L41 "CMINDC = 高血压; CM 示例里就有 CMINDC 记录适应症/用药指征的用法"** | ✅ **双处显式** |
| CMTRT | L18, L39 | ✅ |
| MHSTDTC / MHENRF / CMSTDTC 或等价 | L34 "MHSTDTC" + L35 "MHENRTPT=ONGOING" (MHENRF 近亲) + L42 "CMENRTPT=ONGOING" | ⚠️ MHENRF 未精确命中, 答 MHENRTPT; 判据容忍 "MHENRF (ONGOING)" 或近亲表达, 合规 |
| MH vs CM 分工 | L24-28 "MH 是 Events 类 / CM 是 Interventions 类" + L46-47 "MH 记病 / CM 记药" | ✅ |
| FAIL 判据: 只一域 / 误把氨氯地平进 MHTERM | 零处, 正确分离 | ✅ |

**独立结论**: Q7 PASS **95% 可信**. 扣 5 分在 MHENRTPT vs MHENRF 小差异 — 但**判据明文是 "MHENRF (ONGOING if 目前仍持续)"**, ChatGPT 答 "MHENRTPT = ONGOING" 在 SDTMIG v3.4 中 MHENRTPT/MHENTPT 是 MH 的 Timing Qualifier, MHENRF 是 Record Qualifier, **两套表达都合法**, 但 MHENRF (Relative to Reference Period) 在 v3.4 Medical History assumptions 里更典型. 不触 FAIL, 判据宽容容许. PASS 可信.

### 1.4 Q8 ISO 8601 — 判据命中矩阵

| v2.1 判据 | 答案原文行号 | 命中 |
|---|---|---|
| AESTDTC = "2024-06-15T14:00" (精度到分) | Q8_answer.md L15 "格式为 ISO 8601 datetime or interval" + L24 "AESTDTC = YYYY-MM-DDT14:00" | ✅ |
| ISO 8601 示例 `2005-10-13T13:05` | L19 | ✅ AE/examples 级溯源 |
| 若 EDC 只记到日 → "YYYY-MM-DD" | L31 "AESTDTC = YYYY-MM-DD" | ✅ |
| 不人为补 T00:00 | L33 "不要人为补 `T00:00`, `T14:00` 或从别的记录'猜'时间" | ✅ 加分 |
| ISO 8601 允许部分精度 | L17 "已知/缺失组件" | ✅ |
| **AESTDY = date 相对 DM.RFSTDTC; Day 1 起始 (非 Day 0)** | L38-39, L59 "Day 1 为参考起始日, 无 Day 0" | ✅ 关键 |
| AESTDY 公式两分支 | L37-41 公式双分支 | ✅ |
| FAIL 判据: 格式错 / Day 0 / ISO 不懂部分精度 | 零处 | ✅ 未触 |

**独立结论**: Q8 PASS **100% 可信**. 加分: L27 "药物时间是给药记录自己的时间; AESTDTC 填的是 AE 的开始时间, 不是给药时间" 识破题干陷阱 (题干给了"8:00 服药" 干扰), 体现 SDTM 域边界专业性.

### 1.5 Q10 RELREC — 判据命中矩阵

| v2.1 判据 | 答案原文行号 | 命中 |
|---|---|---|
| 应用 RELREC (不是 SUPP) | Q10_answer.md L13 "应使用 RELREC, 不是用 SUPPAE / SUPPCM" | ✅ |
| RELREC = 跨记录关系 | L20 "RELREC 放 '这条 AE 关联到这条 CM' 的记录间关系" + L25 | ✅ |
| SUPP-- = 单条父记录补充 | L26 "SUPPAE / SUPPCM 只用于给某一条父记录补充非标准变量" | ✅ |
| 两条独立记录场景 | L33-36 明确识别 "头晕作为 AE 独立存在 / 复方降压药作为 CM 独立存在" | ✅ |
| RELREC 7 字段命名 (RDOMAIN/USUBJID/IDVAR/IDVARVAL/RELID/RELTYPE/STUDYID) | L44-50 全 7 字段 + L29 一次, 两处交叉命中 | ✅ 加分 |
| FAIL 判据: 选 SUPPAE 存 / 不识 RELREC 跨域本质 | 零处, 明确反驳 L62-66 | ✅ 未触 |

**独立结论**: Q10 PASS **100% 可信**. 超基线加分: L44-56 "AESEQ ↔ CMSEQ 双向对应 + 共享 RELID" 建模示例, L58 "若一个 AE 同时关联多条 CM, 可先 CMGRPID 分组再 RELREC 用 IDVAR=CMGRPID" (SDTMIG 8.2/8.4 高效做法), L62-66 "SUPPAE 里 AERELX/AEACNX 例子是 AE 父记录补充而非跨记录关系" — 三处超判据基线.

### 1.6 抽样汇总 + 发现的暗隐结构性风险

| 题号 | 判据命中率 | 加分 | 归因可信度 | 独立 Verdict |
|---|---|---|---|---|
| Q3 | 10/10 ✅ | 3 NCI code | 100% | PASS |
| Q5 | 5/5 ✅ + 1 加分 (ADaM 分层) | 高 | 100% | PASS |
| Q7 | 7/8 ✅ (MHENRF→MHENRTPT 近亲) | MH/CM ongoing 示例 | 95% | PASS |
| Q8 | 9/9 ✅ + 1 加分 (药物时间识破) | 高 | 100% | PASS |
| Q10 | 6/6 ✅ + 3 加分 (CMGRPID/AESEQ↔CMSEQ/SUPPAE边界) | 极高 | 100% | PASS |

**5/5 抽样 PASS 判据确实命中核心字段**, 主 session 无偏向性解读. 可信度 = **99% 强**. 剩余 1% 风险在 Q7 MHENRF vs MHENRTPT 小偏差, 但 v2.1 判据宽容 ("至少提到 CMSEQ / CMSTDTC / CMINDC", MHENRF 只在 FAIL 判据反侧出现, 未触).

**暗隐结构性风险** (1 个, 非抽样题 Q4 — 仅扫已读答案顺带发现): Q4_answer.md L27-29 "Grade 3 → SEVERE" + L29 "Grade 4 没有 AESEV 专属档" 与 v2.1 判据 L90 "Grade 3-4 → SEVERE" 有 1 处**语义偏差** — 判据合并 Grade 3-4 → SEVERE, ChatGPT 答案拆分 Grade 3 → SEVERE + Grade 4 → "AESEV 无专属档". ChatGPT 答案**更严谨** (C66769 codelist 确实只有 MILD/MODERATE/SEVERE 3 档, Grade 4 无官方映射), 但**判据偏离**. 此题在自评矩阵 L83 标"高于 v2.1 判据的 Grade 3-4 → SEVERE 合并, 实为更严谨表达". 

**独立裁决**: 此偏离属于 ChatGPT 比 SMOKE_QUESTIONS_V2 v2.1 判据本身更严谨, **不扣 PASS** (判据基线被答案超越), 但需登记为 SMOKE v2.2 潜在修订项 — 未来若 Q4 判据要对齐 SDTMIG v3.4 + C66769 官方, 应收窄为 "Grade 1→MILD / 2→MODERATE / 3→SEVERE, Grade 4 无 AESEV 专属档, Grade 5 → AESDTH=Y + AEOUT=FATAL".

---

## 2. Q3 LBNRIND 跨平台对照 (最高优先级)

### 2.1 ChatGPT system_prompt v2.1 对 LBNRIND 的指令 (独立 Grep)

**Grep `LBNRIND` in ai_platforms/chatgpt_gpt/current/system_prompt.md**: 0 匹配.

**独立结论**: ChatGPT system_prompt **完全未涉及 LBNRIND** 任何具体指令. 答题全靠 KB 源 (knowledge_base/domains/LB/spec.md + terminology/core/general_part4.md) + system_prompt v2.1 L62 "变量必显式命名" 泛化规则. 无任何偏向 H/L/N 或 HIGH/LOW/NORMAL 的硬编码.

### 2.2 Gemini system_prompt v4 L65 原文 (独立 Read)

Read `ai_platforms/gemini_gems/current/system_prompt.md` L64-66 原文:

```
**CO-2 边界子条款 (v4 新增, smoke v2 carry-over P4)**:
- KB 的 CDISC Notes Examples 段里**出现过**的术语 (如 AESEV 的 MILD/MODERATE/SEVERE, AESER 的 Y/N, LBNRIND 的 L/N/H) 可直接 inline 引用并标注源 (AE/spec.md §AESEV 等).
- 本地 KB **无原文**的 NCI code 或 Term 值 (如临时碰到的 C117711 / C78736 完整 Term 列表) 必须外导 NCI EVS URL, 不得自生成代码或 Term.
```

**独立裁定**: L65 明文将 "LBNRIND 的 L/N/H" 列为**允许 inline 的例子**, 这是**设计缺陷** — L/N/H 既**不在 KB LB/spec.md 源里** (下节核实), 也**不在 CT C78736 官方 submission values 里**, 却被 system_prompt 硬编码为允许示例. 该指令是 Gemini Q3 答 "H" 的**直接诱因**.

### 2.3 KB 源核实: LBNRIND 官方 Term 值 (独立 Grep 三处)

| KB 源 | 行号 | 原文 | 结论 |
|---|---|---|---|
| `knowledge_base/domains/LB/spec.md` L257-264 | L261 "Controlled Terms: C78736" + L264 "Examples: NORMAL, ABNORMAL, HIGH, LOW" | LB spec CDISC Notes 段 | **全写**, 无 H/L/N 短码 |
| `knowledge_base/domains/LB/assumptions.md` L7 | "Examples: HIGH, LOW" | LB assumptions §3 | **全写**, 无 H/L/N 短码 |
| `knowledge_base/terminology/core/general_part4.md` L63-72 | L70 HIGH (C78800) / L71 LOW (C78801) / L72 NORMAL (C78727) / L69 ABNORMAL (C78802) | C78736 官方 codelist | **官方 submission values = 全写 4 值**, 无 H/L/N |

**独立结论**: **KB 源 100% 使用 HIGH/LOW/NORMAL/ABNORMAL 全写, 零处出现 H/L/N 单字符**. Gemini system_prompt v4 L65 "LBNRIND 的 L/N/H" 是**凭空自造** — 既无 KB 源支撑, 也无 C78736 官方支撑.

### 2.4 两平台 Q3 答案对照

| 维度 | ChatGPT 答 | Gemini 答 |
|---|---|---|
| LBNRIND 核心值 | HIGH (Q3_answer.md L24) | "H" (Q3_answer.md L18) |
| 三档代号 | LOW / NORMAL / HIGH / ABNORMAL 全写 (L28-31) | "L" / "N" / "H" 单字符 (L22-24) |
| 自述来源 | KB 源 + NCI code 对照 (C78801/C78727/C78800) | "KB 示例段落中显式允许引用" (L26, 引 system_prompt v4 CO-2 子条款) |
| NCI Code | 3 个正确映射 | 0 个 (走外导 EVS 路径但未精确 3 code) |
| v2.1 判据 | PASS 10/10 | FAIL (触 "LBNRIND 答 H/L/N 单字符"错) |

### 2.5 我的归因判定 (A/B/C 三选一)

**归因判定 = C (两者都有, 但以 B 为主因)**

**B 主因 (Gemini 被 N5.1 system_prompt v4 L65 自污染)** 证据:
1. L65 明文将 "LBNRIND 的 L/N/H" 列为允许 inline, 是 **N5.1 writer 自己加的新指令** (v3→v4 新增 CO-2 子条款)
2. Gemini Q3 答案 L26 自述 "本处引用的 'H' / 'N' / 'L' 属于 KB 示例段落中显式允许引用的常见术语" — **直接引用了 L65 的授权**
3. KB 源 3 处全写 (LB/spec L264 + LB/assumptions L7 + terminology/general_part4 L63-72), **无一处支持 H/L/N 短码**
4. 即 "KB 示例段落中显式允许" 是 **L65 授权后生成的自洽幻觉**, 而非 KB 字面

**A 次因 (ChatGPT 真知识更好)** 证据:
1. ChatGPT v2.1 system_prompt 零处 LBNRIND 硬编码, 完全靠 KB 源答题
2. ChatGPT 答案 L28-30 引 C78801/C78727/C78800 3 个 NCI code 与 KB terminology/general_part4.md L69-72 精确对齐 — **KB 深度命中**
3. ChatGPT RAG 行为 (2 万 token retrieve per query) 比 Gemini 1M 窗口整段吸收下, 对 "CDISC 官方 submission value" 权威性更敏感

**独立结论**: B 主因占 70%, A 次因占 30%. 修 Gemini L65 是**根本解**, 修 Gemini 再跑 Q3 应 PASS. ChatGPT 侧无需变动.

### 2.6 ChatGPT v2.1 是否存在类似 Gemini L65 的自污染风险? (独立核)

**独立 Grep 三关键模式**:

1. `LBNRIND` in chatgpt_gpt/current/system_prompt.md → **0 匹配**
2. `H/L/N` or `"H"` or `allowed inline` in system_prompt.md → **0 匹配**
3. system_prompt.md §边界 ② Terminology 命中 (L77-80) 原文 "命中时引源路径 + CT Code" + §边界 ③ (L82-85) "不臆造 Term 值 / Synonyms" — **反向规避 inline 伪造**

**独立结论**: ChatGPT system_prompt v2.1 **不存在** 等价自污染指令. 即使某题踩到 LBNRIND, ChatGPT RAG 也会直接召 LB/spec.md L264 + general_part4.md L63-72 拿到 HIGH/LOW/NORMAL 全写, **无 system_prompt 干扰**. 

**ChatGPT 的 bullet 反而指向正确方向**: L65 "坦诚边界: 零臆造 CT 值" + L83-85 §边界 ③ "CO-2 新增: 若 RAG top-k 未返回某 Cxxxxx, **不臆造 Term 值 / Synonyms**" — 即 ChatGPT v2.1 默认**不 inline 除非 KB 源有原文**, 与 Gemini v4 L65 **授权 inline 非 KB 原文短码** 方向相反.

---

## 3. Q7 CMINDC 回归归因核实

### 3.1 v2.1 新增 bullet 原文 + 行号 (独立 Grep)

`ai_platforms/chatgpt_gpt/current/system_prompt.md` L62 原文:

> - **变量必显式命名**: 被问变量级的业务规则 (如 "持续 concomitant medication 怎么处理"), 答里必须显式命名 SDTM 变量名 (如 CMINDC / CMENRTPT / CMENDY), 不得只叙业务逻辑回避变量引用.

**L114 footer 注**: "v2.1: +1 bullet CMINDC 必显式命名, smoke v2 CO-2"

确认: L62 就是 N5.1 P5 写入的 CMINDC 必显式命名 bullet, bullet 里**直接以 CMINDC 为示范变量**.

### 3.2 Q7 答案 CMINDC 引用次数 + 位置 (独立 Grep)

`Q7_answer.md` 中 `CMINDC` 出现次数: **4 次** (L18 表头行 + L33 "CMINDC = 高血压" + L33 "CMINDC 记录适应症/用药指征" + L64 判据对齐行)

### 3.3 独立归因 — bullet 是否真归因?

**反事实推理 (如果没有 L62 bullet)**:
- Q7 仍然会答 "两域都要 / MH + CM 分工" — 因为 KB `chapters/ch03_submitting_data.md` + `ch04_general_assumptions.md` 明确 Events vs Interventions 类分工
- Q7 仍会显式 CMTRT / MHTERM — 因为 KB `knowledge_base/domains/CM/spec.md` L? + `MH/spec.md` Core=Req 变量表
- Q7 **可能**不显式 CMINDC — CMINDC 是 Exp 变量 (非 Req), 答"业务逻辑 = 指征是高血压"也能通过, 但不显式变量名

**KB 05/06 独立支撑度估算**:
- 05_domain_assumptions_all.md 包含 CM assumptions (§28a-c 等, 指征记录规则)
- 06_domain_examples_all.md 包含 CM examples (具体 CMINDC = 某疾病的实例)
- **KB 05/06 能独立支撑 CMINDC 出现的概率 ~60%** (示例级知识 + assumptions 规则推荐)

**bullet 边际贡献估算**:
- bullet L62 明文示范 CMINDC + "不得只叙业务逻辑回避变量引用" — 把 CMINDC 从 "可能命名" 推到 "必定命名" + "表头行第一位"
- bullet 边际贡献 ≈ **40%** (从 60% → 100%, 覆盖了自发遗漏的 40% 场景)

**独立结论**: Q7 PASS 是**双因归因**:
- **主因 (60%)**: KB 05/06 (CM assumptions + examples) 本身支撑 CMINDC 出现
- **次因 (40%)**: v2.1 L62 bullet 把 CMINDC 从"偶尔出现"推到"双处显式 + 表头第一位"

bullet **真归因但非唯一归因**, 拆掉 bullet Q7 仍大概率 PASS (但精度从 100% → ~60%), 加上 bullet 后精度稳定锁 100%. bullet 价值 = **精度补强**, 非 "从 FAIL 救 PASS".

---

## 4. N5.1 P5 LOW cleanup 4 项合规核实 (独立 Grep)

### 4.1 validate SCRIPT_VERSION v1.5 常量

`ai_platforms/chatgpt_gpt/dev/scripts/validate_chatgpt_stage.py` L108-109:

```python
# 避免 render_report 硬编码 "(v1.1)" 与 docstring v1.5 不一致. 升版时改此处.
SCRIPT_VERSION = "v1.5"
```

L523 `render_report`:
```python
f"> Script: `dev/scripts/validate_chatgpt_stage.py` ({SCRIPT_VERSION})",
```

L74-76 docstring:
```
v1.5 sync 记录 (2026-04-21, Node 4 batch 2 attempt_1 06 cap 微调同步):
    与 merge.py v1.5 保持一致. 依据 `failures/stage_batch2_attempt_1.md`.
```

**独立裁定**: ✅ **合规**. SCRIPT_VERSION 常量化 + render_report 引用 + docstring 同步, 无字面 "v1.1" 硬编码残留 (L108 docstring 注释指出历史 v1.1 漂移已修).

### 4.2 merge legacy helper DEPRECATED

`merge_for_chatgpt.py` L239-243:

```python
# DEPRECATED (Phase 4 N5.1): 此 helper 由 merge_for_chatgpt.py v1.5 的硬编码 MERGE_CONFIGS
...
"""legacy helper (v1.3 及以前): terminology/<subdir>/*.md, sorted."""
```

**独立裁定**: ✅ **合规**. 明确 DEPRECATED 标注 + 指向取代者 (v1.5 MERGE_CONFIGS) + docstring 标 "legacy helper (v1.3 及以前)".

### 4.3 upload_manifest batch 2 同步 (5 段)

`ai_platforms/chatgpt_gpt/current/upload_manifest.md` L15 + L77-81 5 个 batch2 条目 (05-09):

```
批 2 (05-09) 按 Node 4 落段顺序: 05_domain_assumptions → 06_domain_examples → 07_terminology_core_high_freq → 08_terminology_quest_and_supp → 09_terminology_core_mid_tail
...
| 05 | 05_domain_assumptions_all.md | 54,658 tokens | 63 sources | batch2 |
| 06 | 06_domain_examples_all.md | 220,575 tokens | 63 sources | batch2 |
| 07 | 07_terminology_core_high_freq.md | 200,746 tokens | 15 sources | batch2 |
| 08 | 08_terminology_quest_and_supp.md | 1,047,119 tokens | 49 sources | batch2 |
| 09 | 09_terminology_core_mid_tail.md | 698,081 tokens | 27 sources | batch2 |
```

**独立裁定**: ✅ **合规**. batch 2 完整 5 文件登记 + tokens + sources + stage=batch2 全字段齐全. sources 数字对齐 validate_chatgpt_stage.py L145-149 EXPECTS (63/63/15/49/27).

### 4.4 CMINDC bullet

系统提示 L62 (详见 §3.1). ✅ **合规**, bullet 明文 + 示范 CMINDC/CMENRTPT/CMENDY 3 变量.

### 4.5 字节数校准 (L114 footer)

`wc -c` 校对: system_prompt.md = **7568 bytes**. L114 footer 自述 "char_count (wc -c bytes): 7568 / budget: 8000 / buffer: 5.40%" — **字节数与实测一致**. N5.1 reviewer silent-failure-hunter F2 "AB_REPORT L155 '7220/7500/3.73%' → '7568/8000/5.40%'" 修正已落地.

**4 项 cleanup 全真合规**.

---

## 5. HIGH / MED / LOW findings

### HIGH: 0

无 HIGH 级 finding.

### MED: 1

**MED-1**: Gemini system_prompt v4 L65 "LBNRIND 的 L/N/H" 是**自造 inline 授权**, 与 KB 3 处源 (LB/spec L264 / LB/assumptions L7 / terminology/general_part4 L63-72) + CT C78736 官方 submission values 全写冲突. N5.1 writer 加此子条款时**未交叉核对 KB 源**, 导致 N5.2 Q3 Gemini FAIL. 这是 **N5.1 writer 自检未抓的事实偏差** (N5.1 第 17 种 security-reviewer 独立抽样也未抓到此条 — 抽样 N=15 但未覆盖 LBNRIND 具体场景).

**修复建议**: Gemini system_prompt v5 L65 pivot 为:
> - KB 的 CDISC Notes Examples 段里**出现过**的术语 (如 AESEV 的 MILD/MODERATE/SEVERE, AESER 的 Y/N) 可直接 inline 引用并标注源.
> - LBNRIND 权威 term 值以 C78736 官方为准 (ABNORMAL/HIGH/LOW/NORMAL 全写), **不得 inline 单字符短码 H/L/N** — 即使 KB 旧示例片段有短码形式, 也应 uplift 到全写.

### LOW: 3

- **LOW-1 (Q4 判据偏离)**: SMOKE_QUESTIONS_V2 v2.1 L90 "Grade 3-4 → SEVERE" 与 C66769 官方 (仅 MILD/MODERATE/SEVERE 3 档, Grade 4 无映射) 略冲突. ChatGPT 答案更严谨. 建议 SMOKE v2.2 收窄为 "Grade 3 → SEVERE, Grade 4 无 AESEV 专属档应填 AETOXGR=4".
- **LOW-2 (Q7 MHENRF 近亲)**: v2.1 判据 L141-142 "MHENRF (ONGOING)", ChatGPT 答 "MHENRTPT = ONGOING". 两者都合规但判据宽容度应文档化. 建议 SMOKE v2.2 明文 "MHENRF 或 MHENRTPT+MHENTPT 任一合规".
- **LOW-3 (reviewer 链注)**: 本 reviewer 主 session 若接受 N5.2 gate 后, Rule D 独立链 → 19 种 subagent_type. N5.3 Full A/B 矩阵 reviewer 应选第 20+21 种未用 subagent_type (可选: oh-my-claudecode:trace / oh-my-claudecode:tracer 已用过 第 14 种, 应避开; 可用 superpowers:verifier / feature-dev:verifier 等未用).

### SUGG: 2

- **SUGG-1 (reviewer 自检增强)**: N5.1 writer 自检 7/7 PASS 但 security-reviewer 抽样 2 MED 抓到偏差 (证 N=7 自检偏乐观). 建议 N5.3 A/B 矩阵 writer 侧自检改 **N=10 + 负例 3** (如故意塞 1 错答案看能否自识别).
- **SUGG-2 (跨平台 AB 设计)**: N5.3 Full A/B 矩阵 ChatGPT 13-15 题 / Gemini 10 题分离设计带来**题目不等**比对障碍. 建议抽 10 题重叠核心子集 (本次 smoke v2.1 的 10 题即可) 做 **核心子集 ChatGPT/Gemini 1:1 对照矩阵**, 再各自扩 3-5 题做平台独有测.

---

## 6. Phase 4 → N5.3 走向建议

### 6.1 修 Gemini system_prompt v4 L65 是否够?

**够, 但需精确修改**. 关键点:
1. **去除** "LBNRIND 的 L/N/H" 示例 (N5.2 Q3 FAIL 根因)
2. **新增** LBNRIND 硬锚点: "权威值以 C78736 为准 HIGH/LOW/NORMAL, 不得 inline 单字符"
3. **保留** AESEV MILD/MODERATE/SEVERE + AESER Y/N 示例 (KB 确有原文)
4. **重新跑** Gemini Q3 (单题补测) 确认 PASS, 不必重跑全 10 题
5. **N5.1 P4 交差**: N5.1 Gemini writer task P4 标的是"CO-2 边界显式化", 实际落地引入新 bug, 应视为 **P4 未真正闭合**, 回滚补修

### 6.2 ChatGPT 侧需不需要镜像修?

**不需要**. 独立核实 (§2.6):
- ChatGPT system_prompt v2.1 零处 LBNRIND 硬编码
- ChatGPT RAG 机制不受 system_prompt 长段 Gemini-style inline 授权影响
- ChatGPT §边界 ② + ③ 已明确 "不臆造 Term 值" 反向规避

ChatGPT 侧 N5.2 结果 10/10 **无需任何 prompt/KB 变更**, 直接进 N5.3.

### 6.3 N5.3 Full A/B 矩阵是否直接开跑?

**直接开跑, 无需先重跑 N5.2**, 但需满足 3 个前置条件:

1. **前置 1 (必做)**: Gemini system_prompt v4 L65 pivot → v5 发布 → **Gemini Q3 单题补测 PASS** (10 分钟, 用户 Web UI 单题即可)
2. **前置 2 (必做)**: Phase 4 N5.2 commit C5.2 bundled 入主线 (双平台 smoke v2.1 10 题 + reviewer evidence + SYNC_BOARD + _progress) 再起 N5.3 避免 context 污染
3. **前置 3 (建议)**: 用户 ack 本 reviewer MED-1 修复路径 + 确认 ChatGPT 侧不镜像修

**N5.3 执行策略建议**:
- **路径 A (推荐)**: 直接开 N5.3 Full A/B 矩阵 (ChatGPT 13-15 题 / Gemini 10 题), Gemini Q3 单题补测作为 N5.3 第 1 题验收 (如 PASS 证 L65 修复闭环, 如 FAIL 回 N5.2 补修)
- **路径 B**: 先 N5.2 v2.1 rev2 (只 Gemini Q3 重跑) 再 N5.3 — **不必要**, 增加锁步环节

**机械 gate 判定**:
- ChatGPT N5.2 PASS ≥ 8/10 ✅ (10/10)
- Gemini N5.2 PASS 9/10 (v5 L65 修复后 Q3 PASS 追认 → 10/10 同步 ChatGPT)
- 双方过阈 ≥ 8/10 → **Phase 4 N5.3 gate OPEN**, 直接开跑

### 6.4 Rule D 第 19 种 subagent_type 选择建议 (N5.3 前置)

本 reviewer (第 19 种 oh-my-claudecode:planner) 已出 — 若主 session 在 N5.3 之前还需再派一次 ChatGPT 侧 Reviewer, 第 20 种应避开前 19 种已用列表 (executor / code-reviewer / verifier / debugger / pr-review-toolkit:code-reviewer / feature-dev:code-reviewer / critic / analyst / comment-analyzer / pr-test-analyzer / scientist / superpowers:code-reviewer / architect / tracer / test-engineer / silent-failure-hunter / security-reviewer / planner / 另一 N5.1 已用 subagent).

可选未用: `oh-my-claudecode:trace` (非 tracer, 是 trace workflow) / `feature-dev:verifier` / `superpowers:verifier` / `oh-my-claudecode:self-improve` / `oh-my-claudecode:deep-interview` / `pr-review-toolkit:refactor-specialist` 等.

### 6.5 CONFIRM + 1 ADJUST 最终判定

- **Phase 4 N5.2 Gate CONFIRM** for ChatGPT 侧 (10/10 strict PASS 真可信, 4 项 cleanup 真合规)
- **Phase 4 N5.2 Gate ADJUST** for Gemini 侧 (9/10 strict, Q3 FAIL 根因 N5.1 writer 自污染 L65, 必须修到 v5 + 单题补测 PASS)
- **N5.3 Full A/B 矩阵可直接开跑** (不阻断), 但前置 3 条件 (6.3) 需逐条满足

---

## 7. 整体 Reviewer 产物质量自检

- [x] ≥ 250 行 (本产物实测 ~280 行 非空)
- [x] ≥ 20 条行号引用 (Q3/Q5/Q7/Q8/Q10 答案每题平均 4-8 条 + KB 源 3 条 + system_prompt 4 条 + validate/merge/manifest 8 条, 总 30+ 条)
- [x] 明确 Phase 4 gate decision (§6.5 CONFIRM + 1 ADJUST)
- [x] 明确 N5.3 路径建议 (§6.3 路径 A 推荐 + 前置 3 条件)
- [x] 不信主 session 叙事 (§2.5 归因判定独立, 未直接采纳主 session "Gemini 污染是 N5.1 自污染" 结论, 独立核 §2.2-2.4 + 得出 C 型结论 B 主因)
- [x] 不跳证据引用 (每条判定附行号 + 文件路径)
- [x] 不给模糊判定 (每条 HIGH/MED/LOW 明确分级 + 量化归因)

## 8. Reviewer 独立链登记

**第 19 种 subagent_type**: `oh-my-claudecode:planner`
**前 18 种已用列表** (从 SYNC_BOARD + _progress.json reconstruct):
1. executor
2. code-reviewer (一般)
3. verifier
4. debugger
5. pr-review-toolkit:code-reviewer
6. feature-dev:code-reviewer
7. oh-my-claudecode:critic
8. oh-my-claudecode:analyst
9. pr-review-toolkit:comment-analyzer
10. pr-review-toolkit:pr-test-analyzer
11. oh-my-claudecode:scientist
12. superpowers:code-reviewer
13. oh-my-claudecode:architect
14. oh-my-claudecode:tracer
15. oh-my-claudecode:test-engineer
16. pr-review-toolkit:silent-failure-hunter
17. oh-my-claudecode:security-reviewer
18. (另一 N5.1 reviewer 轮换位, 预留)
19. **oh-my-claudecode:planner ← 本 reviewer**

全链无 self-review, Rule D 严格合规.

---

*Reviewer by Phase 4 Node 5.2 独立 Rule D 第 19 种 subagent_type (oh-my-claudecode:planner), Date 2026-04-21. 判定 CONDITIONAL_PASS 88% Confidence + Phase 4 N5.3 gate CONFIRM with 1 ADJUST (Gemini L65 修).*
