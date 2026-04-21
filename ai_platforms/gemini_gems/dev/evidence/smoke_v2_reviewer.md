# Phase 6.5 Gemini Gems · Node 4 Smoke v2 — Reviewer Report

> **Reviewer**: oh-my-claudecode:test-engineer (Rule D 第 15 种 subagent_type, 独立链)
> **Method**: 只读, 独立核查评分公允性 + CO-1/2/3 守约 + SDTM 事实 vs KB 源 + 04 业务弹药包 ROI
> **Date**: 2026-04-21
> **Scope**: Gemini smoke v2 10 题 (8/10 严格 / 8.5 宽 PASS scorer) + C 方案架构 + Phase 4 gate

## Review Verdict
**ADJUST** — confidence 82%

**Phase 4 gate 决定 = CONFIRM** (8/10 严格过阈, 进 Phase 4 合规).
**具体题目判定 = ADJUST 2 处**: (a) Q3 FAIL 性质判错了层 (SMOKE 判据本身与 KB 源冲突); (b) Q7 MHENRTPT vs MHENRF 不是"两者合法"打平, MHENRF 在本场景更准.

## Independent Scoring Matrix (盲判)

| Q | 主题 | Scorer | 独立 | 一致? | 判据命中 | FAIL 命中? | 说明 |
|---|---|:-:|:-:|:-:|:-:|:-:|---|
| Q1 | CM 2 条 | PASS | PASS | ✅ | 5/5 Req 齐 | N | 干净 PASS, 5 个 Req 比 SMOKE 判据更严格 |
| Q2 | AE SAE 7 子 | PASS | PASS | ✅ | 7/7 | N | 附 Core 属性对齐 KB |
| Q3 | LBNRIND 代号 | FAIL | **DISPUTE 判据 bug** | ⚠️ | 7/8 + CO-2 拒答 | **Y 但判据本身错** | 见下 Q3 专项 |
| Q4 | AESEV + Grade 5 | PASS | PASS (勉强) | ✅ | 三档对 + Grade 5 连锁 | **Grade 1→MILD 映射 Gemini 不给** | 见下 Q4 专项 |
| Q5 | PC LLOQ | PASS | PASS | ✅ | 5/5 | N | 典范 PASS |
| Q6 | ARMCD+换组 | PARTIAL | **FAIL (严) / PARTIAL (宽)** | 灰 | ACTARM 错层到 ADaM | **硬事实错, 触 FAIL 判据** | 见下 Q6 专项 |
| Q7 | MH+CM | PASS | PASS | ✅ | 两域 + ONGOING | **MHENRTPT ≠ MHENRF 偏好** | 见下 Q7 专项 |
| Q8 | ISO 8601 + STDY | PASS | PASS | ✅ | 6/6 | N | 对齐 KB ch04 §4.4.4 |
| Q9 | SUPPAE 例 | PASS | PASS | ✅ | 7/7 | N | QNAM=ISREAC 6 字符合规 |
| Q10 | RELREC vs SUPP | PASS | PASS | ✅ | 7/7 | N | 结构字段全对 |

**独立总分**: 严格二元 **8/10** (与 scorer 一致), 宽 **8.5**. **Phase 4 gate CONFIRM**.

## Q3/Q4/Q6/Q7 逐题争议裁决

### Q3 (DISPUTE scorer 对 FAIL 的归因, 但 verdict 不改)

**独立事实核查** (KB 三源交叉):
1. `LB/spec.md` L264 CDISC Notes: "Examples: **NORMAL, ABNORMAL, HIGH, LOW**" (全写)
2. `model/02_observation_classes.md` L168: --NRIND 示例 "NORMAL, HIGH, LOW" (全写)
3. `LB/assumptions.md` L7: "HIGH, LOW" (全写)
4. `terminology/core/general_part4.md` L63-72 C78736: submission values **ABNORMAL/HIGH/LOW/NORMAL** (全写)

**结论**: KB 源**四处一致**给长形式, 无任何 "H/N/L" 短码支撑. SMOKE_QUESTIONS_V2.md L73/L76 判据 "LBNRIND = H" + "写 HIGH/LOW = FAIL" **与 KB 源冲突**, 是**判据 bug**.

- Gemini 按 CO-2 拒答具体 term, 恰好回避了这个坑
- Verdict 保留 FAIL (CO-2 拒答让"用户问代号"体验断了, 与 scorer 定义一致)
- 但**真正的问题是 SMOKE 判据错**, 不是 gem 设计错

### Q4 (CONFIRM PASS 但 scorer 偏宽)

- KB `AE/spec.md` L246 AESEV CDISC Notes Examples: "MILD, MODERATE, SEVERE" ✅
- SMOKE L90 明文要求 "Grade 1 → MILD; Grade 2 → MODERATE; Grade 3-4 → SEVERE" (**强制映射**)
- Gemini 答 "**不推算, AESEV 留空, Grade 填 AETOXGR**" — **字面违反 SMOKE 判据但合 SDTMIG 'tabulate 不 derive' 原则**
- **裁决**: PASS 可接受 (学术严格), 但 scorer 偏宽. ChatGPT 给映射表 (业务实用派) vs Gemini 建议留空 (学术严格派), 是 SDTM 教学中的真实分歧.

### Q6 (ADJUST scorer PARTIAL → 倾向 **FAIL**, 但接受 PARTIAL)

**独立事实核查**:
- `DM/spec.md` L230/239: **ACTARMCD / ACTARM 是 DM 域 Permissible 变量** ✅ (非 ADaM, 非 EX)
- `DM/assumptions.md` L12-18: 规定 ACTARMCD 与 ARMCD 逻辑关系
- **ACTARM 不在 ADaM, 不在 EX 域 — Gemini 错层是硬事实错**

SMOKE FAIL 判据 L128: "不识别 ACTARM (Actual Arm) 概念". Gemini 表达了 planned-vs-actual 概念, 但**把 SDTM 变量名甩给 ADaM**, 是**命名层级错**. 严判 FAIL, 宽判 PARTIAL. scorer PARTIAL 可接受但偏宽.

### Q7 (ADJUST — MHENRF > MHENRTPT)

**独立事实核查**:
- `MH/spec.md` L221/230: MHENRF + MHENRTPT 两变量都存在
- `MH/assumptions.md` §34a: "**MHENRF may be used when this relative timing assessment is coincident with the start of the study reference period for the subject (RFSTDTC). MHENRTPT and MHENTPT may be used when 'Ongoing' is relative to another date such as the screening visit date.**"

**题目场景**: "目前仍在服药" (ongoing relative to RFSTDTC) → **MHENRF 是规范首选**, MHENRTPT 是自定义参考点才用.

- scorer L60 "两者都是合法 Timing 变量, 不触发 FAIL" 技术上对, **但忽略了 KB assumption §a 的偏好规则**
- Verdict 不改 PASS (弱判) / borderline PASS (严判)
- Phase 4 建议在 04 加补丁: "ongoing-with-RFSTDTC 默认走 --ENRF; 自定义参考点才走 --ENRTPT/--ENTPT"

## CO-1/CO-2/CO-3 守约矩阵

| CO | 守约程度 | smoke 证据 | 问题 |
|---|---|---|---|
| **CO-1** (AE Core Anchor) | **严守** | Q2 AESER=Exp + 6 子=Perm; Q4 AESEV=Perm + AETOXGR=Perm + "AE Core 不规则"; Q8 AESTDTC=Exp | 无问题, KB 全核对一致 |
| **CO-2** (NCI EVS Guard) | **灰度 (实际合规)** | Q3 严守拒答 H/N/L; Q4 inline MILD/MODERATE/SEVERE; Q2 inline Y/N | **边界语义不清**: gem 实际逻辑是 "KB CDISC Notes Examples 里有的可 inline, 无原文必外导" — 是**合规**的, 但 system_prompt CO-2 段没明写此细则. 用户看到 Q3 严 Q4 松会疑惑 |
| **CO-3** (Source Citation) | **严守** | Q1-Q10 全有源路径, Q6/Q8 带 §号 | 格式粒度微不一 (部分 §变量, 部分 §号), Phase 4 可规范 |

**CO-2 边界应显式化**:
- **允许 inline**: KB CDISC Notes Examples 字段出现的 term 值 (AESEV "MILD/MODERATE/SEVERE"、AESER "Y/N")
- **必须外导**: KB 未原文列的 term 值 (C78736 完整列表 / C66769 全部 term)
- 当前 gem 行为已符合此边界, 只需把隐性规则**写进 system_prompt CO-2 段**.

## SDTM 事实抽检

| 事实 | Gemini 答 | KB 源 | 一致? |
|---|---|---|:-:|
| AESER Core | Exp | AE/spec.md:254 | ✅ |
| 6 SAE 子 Core | Perm | AE/spec.md:344/354/362/371/380/398 | ✅ |
| AESEV Core | Perm | AE/spec.md:245 | ✅ |
| AESEV 三档值 | MILD/MODERATE/SEVERE | AE/spec.md:246 | ✅ |
| AETOXGR Core | Perm | AE/spec.md:452 | ✅ |
| **ACTARM/ACTARMCD 归属** | **ADaM/EX** | **DM/spec.md:230/239 (DM 域 Permissible)** | **❌ 硬错** |
| LBNRIND 示例 | CO-2 拒答 | LB/spec.md:264 全写 | — (拒答非错答) |
| AESTDY "no day 0, +1 if ≥" | 符 | ch04 §4.4.4 + L832 | ✅ |
| RELREC 字段 | 全列 | RELREC/spec.md | ✅ |
| MHENRF vs MHENRTPT | 用 MHENRTPT | MH/assumptions §34a (MHENRF 偏好 RFSTDTC) | ⚠️ 次优 |

**1 硬事实错 (Q6 ACTARM) + 1 次优选择 (Q7 MHENRTPT)**. 其余 8 题 SDTM 事实全对.

## 04 业务弹药包效益 (smoke v2 实证)

**命中 04 (Gemini 答案显式引)**: Q2 (§1.2 AE) / Q8 (§9.6 Timing) / Q9 (§1.10 SUPP) / Q10 (§1.10+§4.1 RELREC)

**Miss 04 (仅引 01/02/03)**: Q1 / Q3 / Q4 / Q5 / Q6 / Q7 **6 题**

**Q6 为什么 04 没挽救**: gem 只引 DM spec + assumptions §4, **未命中 04 任何 DM 场景段** — 04 §1.26 DM 速查若存在 ACTARM 条目, 该项就会救回. 这是 **04 覆盖缺口**.

**ROI 评估**: 04 命中率 **4/10 = 40%**, 偏低. 主要在"跨域鉴别 + 特定场景"发挥, 在"规则判断 + EDC→SDTM 映射"主战场**基本没参战**. Node 4 reviewer MED-1 说的 "04 偏薄需扩" 本次 smoke **实证了**.

## Smoke 方法学评估

**MCP 工具链**: Quill ngModel race 在 Q3/Q6 踩两次, 稳定后其他题顺畅. 建议 Phase 4 封装 `gemini_submit_stable.js` helper 避免重踩.

**答题正确性验证**: `get_page_text` 抓 `<main>` 验证**提交成功 + 答案完整**, 但**没有自动化"答案 vs KB 源"抽检**. Q6 错层靠人眼 + 独立 reviewer 回查 KB 才发现. Phase 4 建议加"关键变量名 grep 回查"半自动化步骤.

**10 题覆盖维度**: 场景 3 + 规则 3 + 映射 2 + 鉴别 2 = 10 基本合格. 漏测:
- **全域扫描类** ("哪些域用 EPOCH?") — Gemini 1M multi-needle 理论弱区, 需实测
- **反向变量查** ("DD 域哪个变量记死亡原因?") — 测 VARIABLE_INDEX 有效性
- **超界查询** — 测 CO-4 边界模板 ③ 是否触发

Phase 4 回归题库建议从 10 扩到 20-25 题.

## 8 vs 8.5 判分口径建议

**建议严格二元 8/10** 作为 exit 判定. 理由:
1. **可比性**: 与 ChatGPT 严格二元 9/10 同口径
2. **Phase 4 触发点**: 8/10 + 2 carry-over (Q3 判据 + Q6 ACTARM) 已 actionable, 宽 8.5 模糊 Q6 严重性
3. **回归基线**: Phase 4 A/B 需硬阈值, PARTIAL 计法不稳定
4. **Gate 机制**: 双平台锁步要求机械判, 严格二元更利 gate

## Findings

### HIGH (阻塞 Phase 4 或必修)

**H1. SMOKE_QUESTIONS_V2.md Q3 FAIL 判据与 KB 源冲突**
- KB 四源 (LB/spec.md + model/02 + LB/assumptions.md + general_part4.md) **一致给长写 HIGH/LOW/NORMAL**
- 题目 L76 FAIL 判据 "写 HIGH/LOW 而非 H/L" 与 KB 直接冲突
- Phase 4 必修: **放宽 Q3 判据接受 "HIGH/LOW/NORMAL" 为 PASS** (或保留但加注释"视 sponsor CT 实现"), 否则 Phase 4 回归 A/B 永远错判这道题

**与 ChatGPT tracer 独立同款发现**: 两位 reviewer 独立从不同 KB 源 + 不同 subagent_type 视角得出同一结论, **交叉验证强**.

### MEDIUM

- **M1. Q6 ACTARM 错层是硬 SDTM 知识错**, 不只是 PARTIAL. 04 业务弹药包必加 DM ACTARM/ACTARMCD 条目 + pitfall "不要说它们在 ADaM".
- **M2. CO-2 边界语义不明**, 应在 system_prompt CO-2 段加子条款 "KB CDISC Notes Examples 里有的 term 可 inline; 无原文必外导 NCI EVS".
- **M3. 04 弹药包覆盖缺口** — 10 题只 4 命中, Node 4 reviewer MED-1 "04 偏薄" 本次 smoke 实证. Phase 4 前扩到 50-60K.

### LOW

- **L1. Q7 MHENRF 偏好**: 04 可加 "ongoing-with-RFSTDTC 走 --ENRF" 微补丁.
- **L2. CO-3 源路径格式粒度不一**: Phase 4 规范统一.
- **L3. MCP submit helper 封装**: 避免重踩 Quill race.

## Rule D / Rule E 合规

- **Rule D**: 第 15 种 subagent_type (test-engineer), 与 scorer + writer + 第 14 种 (tracer) 独立. 只读未改. ✅
- **Rule E Q3=C (精确+全域)**: Q3 拒答体现精确优先. ✅
- **Rule E Q4 C 方案 (不 inline terminology)**: Q3 拒答体现. ✅
- **Rule E Q5=A (63 域平权)**: smoke 题分布 CM/AE/LB/PC/DM/MH/SUPPAE/RELREC, 无偏. ✅

## 对 Phase 4 的 Actionable Recommendations

1. **[HIGH 必修]** 校准 SMOKE_QUESTIONS_V2.md Q3 判据: 放宽接受 "HIGH/LOW/NORMAL" 为 PASS, 或改题目从"具体代号"变成"受控于哪个 codelist + 外引 NCI EVS" 以匹配 C 方案.
2. **[HIGH 必修]** 04 弹药包补 DM ACTARM 条目: 加 §X.X "DM planned vs actual arm 双变量对 (ARM/ARMCD + ACTARM/ACTARMCD 均在 DM)" + pitfall "不要说 ACTARM 在 ADaM".
3. **[MEDIUM]** CO-2 边界显式化到 system_prompt: 加子条款 "KB CDISC Notes Examples 里 term 可 inline; 无原文必外导 NCI EVS".
4. **[MEDIUM]** 04 扩到 50-60K (Node 4 reviewer MED-1 + 本次 smoke 共同指向): 加规则判断类 + ENRF 偏好 + 4-5 个高频 pitfall.
5. **[LOW]** 封装 `gemini_submit_stable.js` helper 供 Phase 4 回归批量跑.

## 结论

**最终裁决**: ADJUST (82% confidence). Gemini 过 **8/10 严格 PASS**, **Phase 4 gate CONFIRM**. 但 scorer 低估了一个判据 bug (Q3) 和一个事实错严重性 (Q6 硬知识错, 非只 PARTIAL). Phase 4 开跑前必修前 2 条 actionable. CO-2 边界和 04 扩容建议并入 Phase 4 前置.

**双平台锁步 gate 可放行**, 但 ChatGPT 9/10 也受同一判据 bug 影响 (Q3 H/N/L 判据错), 需同步修正.
