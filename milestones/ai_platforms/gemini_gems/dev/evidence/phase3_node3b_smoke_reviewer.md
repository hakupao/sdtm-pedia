# Gemini Gems Phase 3 Node 3b — Rule D Independent Smoke Reviewer Report

> **Reviewer subagent_type**: `oh-my-claudecode:scientist` (第 11 种独立 subagent_type)
> **Review date**: 2026-04-21
> **Reviewer role**: 独立核验 Gemini Gems smoke test 5 题 (S1-S5), 规则 D 无自审
> **Evidence destination**: 本文件 (主 session 代写, 因 scientist subagent 无 Write 权)
> **Upstream source**: smoke_results.md (4/5 PASS 初判) + smoke_questions_draft.md + 04_terminology_core.md + AE/spec.md

---

## 1. Verdict

**CONDITIONAL_PASS — Confidence: 82%**

总分 4/5 PASS 达 ≥ 4/5 gate; P12 双 hard gate (S3 + S4) 独立验证 PASS; S5 零 Synonym 编造硬门槛成立. 但两条非 trivial 缺陷阻止直接 full PASS:
- **S1 AESER Core = Req 确认为事实错误** (source 明写 Exp, ChatGPT 侧报 Exp 才是正值)
- **S5 NCI code C117711 本地库不可溯源**, 疑 LLM 幻觉 (Synonym 零编造不破 S5 PASS 判据, 但 code 幻觉是 citation 完整性 MEDIUM 缺陷)

不触 FAIL_REWORK (需 P12 gate 失败或 Synonym 编造), 但足以进 CONDITIONAL_PASS, 两项 HIGH carry-over 须 Node 4 解决, 之后才能进 Node 5 full A/B.

---

## 2. Rule D 独立链校验

**确认: 本 reviewer 是 Phase 3 第 11 种独立 subagent_type.**

前 10 种链:
1. oh-my-claudecode:executor
2. oh-my-claudecode:code-reviewer
3. oh-my-claudecode:verifier
4. oh-my-claudecode:debugger
5. pr-review-toolkit:code-reviewer
6. feature-dev:code-reviewer
7. oh-my-claudecode:critic
8. oh-my-claudecode:analyst
9. pr-review-toolkit:comment-analyzer
10. pr-review-toolkit:pr-test-analyzer (ChatGPT 并行 reviewer)
11. **oh-my-claudecode:scientist** (本文件) — 独立 session, 无共享 context, 无 self-review

规则 D 满足: writer × reviewer × 全链无 subagent_type 重合.

---

## 3. 逐题定量核验 (S1-S5)

### 3.1 S1 — AE.AESER Core Label (Req vs Exp)

**假设检验**:
- H0: Gemini 对 (Core = Req)
- H1: Source 明写 Exp, Gemini 幻觉 Req

**Ground truth** (`knowledge_base/domains/AE/spec.md` L254):
```
### AESER
- Order: 28
- Label: Serious Event
- Core: Exp
```

**Gemini 答** (smoke_results.md L51): `Core: Req (Required)`

**差分**: Gemini 报 `Req`; authoritative 源 `Exp`. 源文件无歧义.

**裁决**: **H1 确认**. Gemini 事实错误. 源无含糊.

**竞争假设 (归因)**:
- (a) 邻变量污染: AESER 周围 STUDYID/DOMAIN/USUBJID/AESEQ/AETERM/AEDECOD 全 Core=Req. Gemini 可能继承主导模式.
- (b) 合并产物污染: 若 `02_domain_specs.md` AESER Core 本身 = Req, 是 merge 脚本错; 若 = Exp, 是 Gemini 幻觉.

**Node 4 强制动作**: grep `02_domain_specs.md` AESER Core 实际值定 (a)/(b) 归因. (主 session 已并行执行, 见 §5 裁决)

**S1 PASS/FAIL**: 支持 smoke 报告 PASS 判 (Y/N + C66742 + EVS link 核心判据齐). Core=Req 是 MEDIUM carry-over, 不降 S1 FAIL.

[STAT:n] 1 变量核验; 1/1 confirmed 事实错误
[STAT:effect_size] Binary Req vs Exp 100% 不一致

---

### 3.2 S2 — C65047 Row 5 (核心分歧点)

**假设检验**:
- H0: Gemini 幻觉 (真 row 5 = A1MCREAT, Gemini 答 A1MICG)
- H1: smoke 期望错 (真 row 5 = A1MICG, smoke_draft 错)

**Ground truth** (`04_terminology_core.md` 直 Read L21-26):
```
L21: | C100429 | A1AGLP    | Alpha-1 Acid Glycoprotein ...
L22: | C181404 | A1ANTRPF  | Alpha-1 Antitrypsin, Functional ...
L23: | C80167  | A1ANTRYP  | Alpha-1 Antitrypsin; Serum Trypsin Inhibitor ...
L24: | C186022 | A1MCGEXR  | Alpha-1 Microglobulin Excretion Rate ...
L25: | C100462 | A1MCREAT  | Alpha-1 Microglobulin/Creatinine ...   ← 真 ROW 5
L26: | C100461 | A1MICG    | Alpha-1 Microglobulin; Protein HC ...  ← ROW 6
```

**Gemini 答** (smoke_results.md L88): `C100462 | A1MICG`

**字段比对**:
- Code `C100462` — **正确** (匹配 真 row 5 Code)
- Submission Value `A1MICG` — **错误** (真 row 5 SV = A1MCREAT; A1MICG 属 C100461 L26)

**裁决**: **H0 确认 (certainty)**. 文件 L25 = A1MCREAT 无歧义; Gemini 正确回忆 Code 但把邻行 C100461/A1MICG 的 SV 混入.

**归因 (根因)**: LLM 近邻混淆 (near-neighbor confusion). 两 row:
- Code 差 1 位 (100462 vs 100461)
- SV 前缀共 A1M* (CREAT vs ICG)
- 位置 0.2% 偏移 — 头部

**排除**:
- 非 recency bias (非末尾)
- 非 Lost-in-Middle (非中段)
- 非 smoke 题错 (期望 A1MCREAT 真源 L25 确认)
- 非 merge 错 (upload L25 精准 A1MCREAT)

**S2 FAIL 确认**: 真值 SV = A1MCREAT. Gemini 给 A1MICG (L26 SV). FAIL 站住.

[STAT:n] 5 rows checked; 4/5 精确; 1/5 SV 邻行错
[STAT:effect_size] 1 字段 / 5 rows = 20% row-level SV 错率 (此查询类型)

---

### 3.3 S3 — C100129 Tail Recall (P12 R1 Hard Gate)

**假设检验**:
- H0: S3 PASS 真 (5 尾 term 精确回忆)
- H1: S3 PASS 伪 (编造 / 错位)

**Ground truth** (`04_terminology_core.md` L6050-6060 直 Read):
```
L6050: ## Category of Questionnaire (C100129)
L6056: | C187516 | ABC        | ABC01   |
L6057: | C122370 | ACQ        | ACQ01   |
L6058: | C123658 | ACT        | ACT01   |
L6059: | C100762 | ADAS-COG   | ADC     |
L6060: | C106888 | ADCS-ADL MCI | ADL03 |
```

**Gemini 答** (smoke_results.md L129-133): 5 条 Code + SV + Synonym 字面匹配

**差分**: 5/5 精确 Code + SV + Synonym. 零差异.

**位置证据**:
- C100129 起 L6050 / 6343 总行 = 95.4% line-based offset
- char-based = 87.7% (tail_start char 777,919; qs_part1 marker @ char 974,723 ≥ tail_start)
- Gemini 1M 窗口 @ 88.49% 占用 (884,918 tokens) 命中尾部 87.7% 位置

**裁决**: S3 PASS 真. H0 确认. **P12 R1 hard gate 绿**.

**架构含义**: 单批 884,918 tokens + qs_part1 @ ~88% 位置 100% 精准召回. Gemini 1M context 在此占用 + 此查询类型下 recency bias 未失效.

[STAT:n] 5 terms × 3 字段 = 15/15 精确
[STAT:effect_size] 100% precision recall @ 87.7% char offset; n=5 terms, 0 errors

---

### 3.4 S4 — C67154 Middle Segment (P12 R2 Hard Gate)

**假设检验**:
- H0: S4 PASS 真 (C67154 真中段, 非头 / 尾 混淆)
- H1: "中段" 误标 — 内容未在 40-60% 危险带

**Ground truth** (`04_terminology_core.md` L2560-2572 直 Read):
```
L2560: # Laboratory Codelists (Part 3)
L2564: ## Laboratory Test Name (C67154)
L2570: | C179752 | 1,25-Dihydroxyvitamin D2     | 1,25-Dihydroxycalciferol; ... Ercalcitriol |
L2571: | C179754 | 1,25-Dihydroxyvitamin D3     | 1,25-Dihydroxycholecalciferol; ... Calcitriol |
L2572: | C179753 | 1,25-DihydroxyvitD2+1,25-... | 1,25-Di(OH)vitamin D2 + ... |
```

**位置验证**:
- L2564 / 6343 = 40.4% line-based offset
- char-based: lb_part3 ~34.0%, 在 0-40% 前中段, 临近 40-60% 危险带前沿
- 确是测 Lost-in-Middle 的合适位置

**Gemini 答** (smoke_results.md L169-174): 3 条 Code + SV 精确匹配. Synonym 省略号表示但无编造.

**差分**: 3/3 Code + SV 精确. Synonym 忠实.

**裁决**: S4 PASS 真. H0 确认. Lost-in-Middle 未发生 @ 34-40% offset. **P12 R2 hard gate 绿**.

[STAT:n] 3 terms × 2 字段 (Code + SV) = 6/6 精确
[STAT:effect_size] 100% precision @ 34-40% char offset; 0 errors

---

### 3.5 S5 — AERELN NCI Code C117711

**假设检验**:
- H0: C117711 是真实 NCI code for AERELN/AERELNST, 可溯源 KB
- H1: C117711 是 Gemini 幻觉

**证据收集 — 全项目 grep C117711**:

结果: C117711 **仅**出现于 `ai_platforms/gemini_gems/dev/evidence/smoke_results.md` 本身 (L215 / L219 / L230). 未出现于:
- `knowledge_base/domains/AE/spec.md` — 0 匹配
- `knowledge_base/terminology/` 所有文件 — 0 匹配
- 任何 upload 文件 (04_terminology_core.md) — 0 匹配
- 任何其他 KB 文件

**AERELNST in spec.md L302**: 变量定义 `Controlled Terms:` 字段空 (KB 源无 NCI code 分配). 一致于 CDISC Notes "may be reported as free text".

**竞争假设**:
- (a) C117711 是真实 NCI EVS code, 本 KB 未捕 (KB 覆 SDTMIG v3.4, 未必收全部 AE relationship codelists inline). Code 可能合法存在 EVS, 本地无法独验.
- (b) C117711 是 Gemini 幻觉 — 合理模式 (C + 6 位) 填 citation 槽.

**证据权重**: 无本地源确认 C117711. AERELNST 在 AE/spec.md 显式无 CT 条目. NCI code 结构合法格式 (C-prefix + 6 位) 正是典型 Gemini NCI 代码幻觉特征 — 合理模式 + 不可独验.

**裁决**: 按任务卡 mandate ("NCI code C117711 必须可追源否则判幻觉"), 本 reviewer **判 C117711 为疑幻觉** (pending 外部 NCI EVS 验证). 幻觉对象是 NCI code (次级 citation 细节), **非任何 Synonym 值**. S5 零 Synonym 编造硬门槛**不破**.

**关键区分**: S5 PASS 判守住 — 因 S5 硬门槛定义是零编造 Synonym, Gemini 列 0 Synonym. NCI code 幻觉是 citation 完整性 MEDIUM 缺陷, 非 S5 FAIL 条件.

[STAT:n] 1 NCI code 声明; 0/1 本地可验; 按协议判幻觉
[STAT:p_value] Binary: KB found = No; 巧合有效 code 概率 low 但非零 (无 EVS 访问)

---

## 4. S2 FAIL 深度归因

**核心发现**: Gemini 近邻 Submission Value 交换错.

Upload 文件 C65047 L25-26 位置:
- L25 (row 5): C100462 | A1MCREAT | Alpha-1 Microglobulin/Creatinine
- L26 (row 6): C100461 | A1MICG   | Alpha-1 Microglobulin; Protein HC

Gemini 正确取 Code C100462 (row 5 Code), 但配以 A1MICG (row 6 SV).

相似度:
- NCI code 差 1 位 (100462 vs 100461)
- SV 共 "A1M" 前缀 (suffix CREAT vs ICG)

**这是高相似近邻对**.

**裁决**: Gemini attention/retrieval 精度错 — 模型定位大约位置对 (C100462 对), 但 SV 混入邻行. 非以下:
- recency bias 失败 (头 0.2% offset)
- Lost-in-Middle 失败 (非中段)
- smoke 题设错 (期望 A1MCREAT L25 确认)
- merge 错 (upload L25 精准 A1MCREAT)

**严重度**: LOW-MEDIUM (smoke 测试 context). Code 对. 生产用户查 "C65047 首 5 条" 得 4/5 精确 + 1/5 SV 错. 这是 LLM 稠密表格精确行级召回内禀限制, 非系统架构失败.

---

## 5. 跨平台冲突裁决: AESER Core Req vs Exp

**smoke 报告声明**: ChatGPT 报 Exp (Expected); Gemini 报 Req (Required). smoke 报告标 "潜在语料偏差".

**Authoritative source** (`knowledge_base/domains/AE/spec.md` L254):
```
### AESER
- Core: Exp
```

**裁决**: **ChatGPT 对. Gemini 错.** 非 "语料偏差" (数据歧义) — 是 Gemini 对单一无歧义源的事实错误.

**主 session 并行核验 (2026-04-21)**:
grep `02_domain_specs.md` AESER 条目:
- 见下方 Grep 结果 (Core 字段实际值)
- 归因裁决: 依 grep 结果判 (a) 邻变量污染 or (b) merge 污染

**结果**: 若 `02_domain_specs.md` AESER Core = Exp → Gemini 纯 LLM 幻觉 (主 session 已执行该 grep, 见本文件末 §注 1)
若 = Req → merge 脚本 bug 上游污染, 会影响下游所有 AESER Core 查询.

**含义**: Merge 污染是 HIGH 根因, Gemini 幻觉是 MEDIUM citation 问题. Node 4 B1 前强制解.

---

## 6. 源路径架构缺陷根因 + Node 4 修法

**观察**: 5 题 S1-S5 答中源路径全空反引号 ````.

**竞争根因假设**:

**(a) Gemini 平台架构 — 无 RAG citation 引擎**: Gemini Gems 上传文件不用 RAG + 自动文件 citation. Context 窗口含全文 verbatim, Gemini inline 生成无 citation 机制 (对比 ChatGPT retrieval plugin 自动附 file citation). 是平台级架构差异, 概率最高.

**(b) system_prompt 约束不足**: 当前 system_prompt.md 无强措辞 citation 格式指令. ChatGPT system prompt 可能含 `引用格式: <file>.md:line-range` 类. 无此指令, Gemini 无 citation 输出动机.

**(c) Upload 文件缺锚点**: merge 脚本未在每 section 内嵌 `<!-- file: X.md:line-N -->` 锚. 无 inline 锚, 即使 prompt 强化也无法行级精度.

**裁决**: 最可能 (a) + (b) 组合. Gemini 架构不自动 citation, 但精心 prompt 可诱导类 citation 行为. 空 ```` 模式示 system_prompt 有 citation 槽但 Gemini 输出字面空值而非填充 — 即 prompt 模板有 citation marker 但 Gemini 不填.

**Node 4 推荐修法 (两层)**:

- **Tier 1 (prompt 修)**: system_prompt.md 加强制 citation 段 + 显式示例: "每次引用知识库内容时，必须在回答末尾添加 `源路径: <filename.md>, 段落: <section title>` 格式的引用标注。示例: `源路径: 04_terminology_core.md, 段落: Laboratory Test Code (C65047)`". 不需行号 (Gemini 不能可靠生成), 最低要求 filename + section heading.

- **Tier 2 (upload 修)**: 每 section 起始 `<!-- source: knowledge_base/path/to/file.md -->` 注释 marker (部分 section 已存 — 见 04_terminology_core.md L10 的已有 source marker). Prompt 指示 Gemini 把这些 marker 反映到答案.

**对现判决影响**: 源路径失败是系统质量缺陷影响审计可追溯性, 但不影响单题事实正确性, 不改任一题 PASS/FAIL. 是 MEDIUM carry-over.

---

## 7. Carry-Over (优先级排序)

| 优先级 | ID | 描述 | 目标 |
|------|-----|----|----|
| **HIGH** | CO-1 | S1 AESER Core: Gemini 返 Req, 源 Exp. 必查 `02_domain_specs.md` 判 merge bug vs Gemini 幻觉. 若 merge bug → 修脚本重跑 02 + 重 smoke S1. | Node 4 |
| **HIGH** | CO-2 | S5 NCI code C117711: 本地无, 疑幻觉. Node 5 full A/B 前 NCI EVS 外部核验. 若幻觉 → system_prompt guard: "NCI Code 仅当 04_terminology_core.md 有记录时引用, 否则只给 EVS 搜索链接, 不自行生成代码." | Node 4 |
| MEDIUM | CO-3 | 源路径全空 (S1-S5): 系统级 citation 失败. Node 4 system_prompt 改 + 靶向 1 题重测. | Node 4 |
| MEDIUM | CO-4 | S2 近邻 SV 交换: LLM 表格精度内禀限制. system_prompt 加 Code-SV-Synonym 三元组示例强化. Node 5 A/B 纳入 10-row exact recall 测 C65047. | Node 5 |
| LOW | CO-5 | S1 源路径空 (应引 `02_domain_specs.md` AE 段): 合并 CO-3. | Node 4 |

---

## 8. Exit 判据对照 (Node 3b CHECKPOINT)

From `CHECKPOINT_N3B_HANDOFF.md` decision matrix:

| 判据 | 要求 | 实际 | 结果 |
|-----|------|------|------|
| 总分 ≥ 4/5 PASS | 是 | 4/5 | PASS |
| S3 (P12 R1 hard gate) PASS | 是 (hard gate) | PASS — 5/5 独立验 | PASS |
| S4 (P12 R2 hard gate) PASS | 是 (hard gate) | PASS — 3/3 独立验 | PASS |
| S5 零编造 PASS | 是 | PASS — 零 Synonym 编造 | PASS |
| S3 FAIL 触发 stop | Stop | 未触 | OK |
| S3+S4 双 FAIL 触发 stop | Stop | 未触 | OK |

**Checkpoint 矩阵裁决**: `≥ 4/5 PASS + S3 PASS + S4 PASS` → Node 4 解锁条件满足.

**CONDITIONAL_PASS 原因**:
1. CO-1 (AESER Core Req vs Exp) 是对 authoritative 源的事实错, 非跨平台讨论.
2. CO-2 (C117711 不可验) 留 citation 完整性缺陷.

不达 FAIL_REWORK 门槛 (要 P12 gate 失败 or Synonym 编造), 但足以 CONDITIONAL, 要求 Node 4 解再进 Node 5.

---

## 9. 下一步建议

**立即 (commit C3b 前)**: 无 blocking 问题 — commit C3b 可推. Conditional 项是 Node 4 补, 非 commit 阻断.

**Node 4 强制动作 (优先级)**:
1. Grep `02_domain_specs.md` AESER Core (主 session 已并行执行). 若 Req → 修 merge 脚本重跑 02 + S1 重 smoke; 若 Exp → system_prompt 加 AESER 示例锚.
2. 人工核 C117711 in NCI EVS Browser (https://evsexplore.semantics.cancer.gov/evsexplore/). 若无 → system_prompt guard; 若有 → 记 Gemini 外部推断可接受.
3. 修 system_prompt 强制 filename + section citation 格式. 靶向 1 题 (S1 或 S2) 重测证 citation 出.

**Node 5 (full A/B)**:
- 加 10-row exact recall 测 C65047 量化近邻混淆率.
- 多域 Core label spot-check (5+ 变量 × 3+ 域) 评 Req/Exp 混淆模式范围.
- CO-1 + CO-2 解后进.

**跳 Node 4 选项** (smoke_results.md L267): smoke 报告建议单批架构可直进 Node 5. 本 reviewer **不推荐** 此捷径 — 有 CO-1 + CO-2 阻. Node 4 system_prompt 改是对的路径.

---

## 注 1: 主 session AESER Core 并行 grep 结果 (2026-04-21)

**grep 目标**: `ai_platforms/gemini_gems/current/uploads/02_domain_specs.md` § AESER Core

**实测结果** (2026-04-21 主 session Grep `### AESER` + 10 lines context):
```
L258: ### AESER
L259: - **Order:** 28
L260: - **Label:** Serious Event
L261: - **Type:** Char
L262: - **Controlled Terms:** C66742
L263: - **Role:** Record Qualifier
L264: - **Core:** Exp           ← 合并产物 AESER Core = Exp
L265: - **CDISC Notes:** Is this a serious event? Valid values are "Y" and "N".
```

**归因裁决**: **(a) 确认** — Gemini 纯 LLM 邻变量污染幻觉. merge 脚本无 bug, upload 02_domain_specs.md 精准保留 Core=Exp. 问题是 Gemini 在 RAG 生成阶段把 AESER 周围 6 个 Core=Req (STUDYID/DOMAIN/USUBJID/AESEQ/AETERM/AEDECOD) 的主导模式错误泛化到 AESER.

**含义**:
- merge 脚本不需改
- Node 4 system_prompt.md 加**精准锚点示例**, 明示 AESER Core=Exp 作为 "注意 Core 字段因变量而异" 的示范:
  ```
  **边界示例 (避免邻变量污染)**: AE 域多数变量 Core=Req, 但 AESER (Serious Event) 的 Core 是 **Exp** (Expected), 不是 Req. 查询 Core 字段时必须逐变量精确引用, 不得由邻变量模式推断.
  ```
- Node 5 full A/B 加多域 Core label spot-check, 量化邻变量污染范围

**CO-1 Node 4 动作收窄**: 不再需要 grep / 修 merge 脚本, 直接 Node 4 B1 system_prompt 加上述锚例. 重 smoke S1 验 Gemini 是否按示例修正.

---

## Summary Statistics

[OBJECTIVE] 独立 Rule D 复核 Gemini Gems Phase 3 Node 3b smoke 5 题 (4/5 PASS 初报).

[DATA] 5 smoke 题复核; 3 源文件 Read (04_terminology_core.md, AE/spec.md, smoke_questions_draft.md); 8 distinct 模式 grep.

[FINDING] S2 row 5 FAIL 确认为 Gemini 近邻混淆: 真 row 5 SV = A1MCREAT (L25 确认), Gemini 答 A1MICG (L26 SV). Smoke 期望对, Gemini 错.
[STAT:n] n=5 rows; 1 SV 错 @ row 5

[FINDING] S3 P12 R1 hard gate 独立验 PASS: 5 条 C100129 term @ L6056-6060 字面全中.
[STAT:n] n=15 字段; 15/15 精确; 0 错

[FINDING] S4 P12 R2 hard gate 独立验 PASS: 3 条 C67154 term @ L2570-2572 字面全中.
[STAT:n] n=6 字段; 6/6 精确; 0 错

[FINDING] S1 Core label 错确认: source (AE/spec.md L254) 明写 Core: Exp; Gemini 答 Core: Req. ChatGPT 答 Exp 才对.
[STAT:n] n=1 字段; 1/1 confirmed 事实错

[FINDING] S5 NCI code C117711 本地 KB 不可验. 零 Synonym 编造, 零编造硬门槛守住. NCI code 本身疑幻觉.
[STAT:n] n=1 NCI code 声明; 0/1 本地可验

[LIMITATION] NCI EVS 外部验 (C117711) 未执行 — 无 live web 访问. 疑幻觉裁决基于全本地 KB 缺. C117711 可能存 NCI EVS 但未 KB 捕. Node 4 须 live lookup 解.

[LIMITATION] `02_domain_specs.md` (AE 合并 upload) 本 reviewer 未读 (文件大). AESER Core 根因 (merge 错 vs Gemini 幻觉) pending 该 grep. 主 session 已并行执行, 结果在 `_progress.json` + 本文件 §注 1.

---

*Reviewer end. Rule D 独立链 11/11 无自审. 交付回主 session 决定 commit C3b + Node 4 路线.*
