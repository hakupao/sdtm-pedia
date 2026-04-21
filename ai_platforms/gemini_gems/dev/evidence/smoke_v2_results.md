# SDTM Expert Smoke v2 — Gemini Gems

> Run date: 2026-04-21
> Platform: https://gemini.google.com/u/1/gem/3b572e310813 (SDTM Expert Custom Gem, C 方案)
> Account: Google AI Pro (bojiang.zhang.0904@gmail.com)
> Reasoning mode: Pro (Gemini 3 Pro)
> Questions source: `ai_platforms/SMOKE_QUESTIONS_V2.md` v2.0
> Runner: MCP agent (Cowork via Chrome extension), each Q in a fresh conversation (gem root URL navigate → Pro mode → JS paste → send)
> Submission method: Chrome MCP `javascript_tool` + `document.execCommand('insertText')` + dispatch `InputEvent` for Angular ngModel sync + click `button.send-button.submit`

---

## 题目提交协议 (稳定版)

**坑点 1 (Q3 踩过)**: 直接 `execCommand('insertText')` → `editor.innerText` 对, 但 Quill/Angular ngModel 未同步, click 发送 → 发空. 解决: paste 后 `editor.dispatchEvent(new InputEvent('input', { bubbles: true, data: q, inputType: 'insertText' }))` 再 `classList.remove('ql-blank')` → 清 `ql-blank` 类标志 → Angular 识别为非空.

**坑点 2 (Q6 踩过)**: 同一个 `javascript_tool` 块里 paste + send 仍会有微小的 ngModel race (send click 执行时 Angular 还未完成 dirty check), 导致发空引起 Gem 只做 auto-init. 解决: **JS paste 与 UI click 分离**, 中间插 `wait duration=2`, 让 Angular 完成 dirty check cycle 后再点发送.

**坑点 3 (各题)**: 每次 `navigate` 到 gem root, Pro mode 会重置为 Fast; 需手动 click Fast dropdown → select Pro.

**坑点 4 (Q2/Q3 观察)**: Gem 在 fresh navigate 后有**自动 acknowledgment turn** (gem 自述"SDTM Expert Mode Activated"作为 turn 1), 实际用户问题是 turn 2+. 这是 gem 内置行为, 答题质量不受影响.

**验证每次提交**: 完成后 `get_page_text` 抓 `<main>` 全文确认用户消息内容与原题一致, gem 答复完整.

---

## Gemini 10 题 对话 URL + 收割状态

| Q | Conversation URL | 模式 | 答案状态 | Verdict |
|---|---|:---:|---|:---:|
| Q1 | https://gemini.google.com/u/1/gem/3b572e310813/0c1ab80ef7914247 | Pro | ✅ 已收割 | **PASS** |
| Q2 | https://gemini.google.com/u/1/gem/3b572e310813/598a34d0c35117ca | Pro | ✅ 已收割 | **PASS** |
| Q3 | https://gemini.google.com/u/1/gem/3b572e310813/77c617999fcf105f | Pro | ✅ 已收割 | **FAIL** |
| Q4 | https://gemini.google.com/u/1/gem/3b572e310813/4ccf7e3a6135571d | Pro | ✅ 已收割 | **PASS** |
| Q5 | https://gemini.google.com/u/1/gem/3b572e310813/638763801f4535a7 | Pro | ✅ 已收割 | **PASS** |
| Q6 | https://gemini.google.com/u/1/gem/3b572e310813/97bbcb182bdc7643 | Pro | ✅ 已收割 | **PARTIAL** |
| Q7 | https://gemini.google.com/u/1/gem/3b572e310813/466f26cb2a8a3f56 | Pro | ✅ 已收割 | **PASS** |
| Q8 | https://gemini.google.com/u/1/gem/3b572e310813/84127d4e253dedf4 | Pro | ✅ 已收割 | **PASS** |
| Q9 | https://gemini.google.com/u/1/gem/3b572e310813/f32e029135f71e1a | Pro | ✅ 已收割 | **PASS** |
| Q10 | https://gemini.google.com/u/1/gem/3b572e310813/cf10a3d03d44ed44 | Pro | ✅ 已收割 | **PASS** |

每题完整答案见 `ai_platforms/gemini_gems/dev/evidence/smoke_v2_answers/Qx_answer.md`.

---

## PASS/FAIL 汇总

**计分**: **8 PASS + 1 PARTIAL (0.5) + 1 FAIL = 8.5/10 (总分 9.0 当 PARTIAL 算 PASS, 8.0 当 PARTIAL 算 FAIL)**

**严格二元判定 (PARTIAL 计为 FAIL)**: **8/10 PASS**

| # | 业务维度 | 题目主题 | Verdict | 关键判据命中 | 失误点/差异 |
|---|---|---|:---:|---|---|
| Q1 | 场景→域映射 | CM 合并用药同服两药 → 2 条记录 | PASS | 2 条拆分 + STUDYID/DOMAIN/USUBJID/CMSEQ/CMTRT 全列 + CMINDC/CMSTDTC/CMENRTP 辅助变量 | — |
| Q2 | 场景→域映射 | AE SAE 7 子变量 Y/N | PASS | AESER=Y + AESHOSP=Y + 其 5 个 N + 区分 seriousness/severity + Core=Exp/Perm 提示 | — |
| Q3 | 场景→域映射 | LB HbA1c 8 变量 + NRIND 代号 | **FAIL** | 7/8 变量对 (LBTESTCD=HBA1C / LBORRES=6.8 / LBSTRESN=6.8 等); **LBNRIND 按 CO-2 拒答具体代号**, 指向 NCI EVS C78736 | **题目明确要"代号是什么" → gem 按 CO-2 规则不 inline CT term → 评分为 FAIL** (跨平台差异: ChatGPT 答 "HIGH" 也 FAIL, 两平台失败方向不同但都未命中 H/N/L) |
| Q4 | 规则/约束 | AESEV 三档 + CTCAE 对应 + Grade 5 | PASS | MILD/MODERATE/SEVERE 三档对 + 区分 AESEV/AETOXGR (严重性 vs 毒性) + Grade 5 → AESDTH=Y + AESER=Y + AEOUT=FATAL | 与 ChatGPT 不同: Gemini 推荐 **不映射** CTCAE→AESEV (Grade 填 AETOXGR, AESEV 留空), ChatGPT 给了 1→MILD/2→MODERATE/3-4→SEVERE 映射表. Gemini 的"不映射"更符合 SDTM "如实 tabulation" 原则 |
| Q5 | 规则/约束 | PC LLOQ 不能写 0 | PASS | PCORRES="< 0.1"/"BQL" + PCSTRESC 保留 "<" + PCSTRESN=Null + PCLLOQ=实测值 + 解释真实性/bias/ADaM imputation 三点 | — |
| Q6 | 规则/约束 | ARMCD vs ARM + 中途换组 | **PARTIAL** | ARMCD 短码 ≤20 字符 ✅ + ARM human-readable ≤200 ✅ + DM/SE/TA 三域职责✅ + DM = 计划组别 + SE = 实际经历 | **未点名 ACTARM/ACTARMCD SDTM 变量** (答案把 "actual" 放在 ADaM TRTP/TRTA 或 EX 域, 而 SDTM 自己有 ACTARM 变量对). 概念上 planned-vs-actual 分离对, 但变量命名错层 (放到 ADaM 而非 DM 兄弟变量) |
| Q7 | EDC→SDTM | 病史+仍服药 → MH + CM | PASS | 两域都要 ✅ + MH 记"高血压"/CM 记"氨氯地平" + MHENRTP=ONGOING + CMONGO=Y + Events vs Interventions 类别说明 + 额外提 RELREC 关联 (bonus) | Gemini 用 MHENRTP 而 SMOKE PASS 判据要求 MHENRF (两者都是合法 Timing 变量但语义略不同; 不触发 FAIL 判据) |
| Q8 | EDC→SDTM | ISO 8601 精度 + AESTDY | PASS | AESTDTC=YYYY-MM-DDThh:mm (如 EDC 精确) + 只记到日则 YYYY-MM-DD + 严禁补 00:00 + AESTDY = (date - RFSTDTC) + 1 if ≥, else 减 + **无 Day 0** + 部分精度 ISO 8601 允许 | — |
| Q9 | 域间鉴别 | SUPPAE + QNAM/QLABEL/QVAL 例子 | PASS | SUPPAE 存非标 Qualifier ✅ + 例: QNAM=ISREAC / QLABEL=Injection Site Reaction / QVAL=Y + QNAM ≤ 8 字符 规则 + 完整结构字段 (RDOMAIN/IDVAR/IDVARVAL/QORIG/QEVAL) | — |
| Q10 | 域间鉴别 | RELREC vs SUPPAE/SUPPCM | PASS | 选 **RELREC** ✅ + RELREC = 跨记录 vs SUPP-- = 单记录非标补充 + 本场景两条独立记录的关联 + 业务映射 IDVAR=AESEQ/CMSEQ + RELTYPE=CAUSAL 示例 | — |

---

## Q3 FAIL 详情 (Gemini CO-2 vs SMOKE PASS 判据冲突)

**题目原文 (SMOKE_QUESTIONS_V2.md line 64)**:
> 指出 `LBNRIND` 的三挡分类 (低 / 正常 / 高) 用什么代号.

**PASS 判据** (SMOKE_QUESTIONS_V2.md line 73):
> LBNRIND = "H" (High; 三档 L / N / H)

**FAIL 判据** (line 76):
> LBNRIND 三档说错 (比如写"HIGH"/"LOW"而非"H"/"L")

**Gemini 实答** (Q3_answer.md):
> 本 Gem C 方案决策不 inline codelist Term 具体值. CT Code `C78736` 对应 codelist 英文名: `<Reference Range Indicator>` (据本 Gem 索引核实). Term 值查询: 请查 NCI EVS Browser: https://evsexplore.semantics.cancer.gov/evsexplore/ 搜索 C78736. 本 Gem 不 inline Term 值以保业务场景完整覆盖, 不记忆/生成 NCI Code.

**失误性质**: **Gemini C 方案 CO-2 守则主动拦截了对 CT Term 具体值的作答**. 这不是"答错代号", 而是"按设计拒答". 设计上是为了防止 NCI Code 幻觉, 但在用户明确问代号时形成用户体验问题.

**跨平台差异**:
- ChatGPT Q3: 给了具体代号但全写 "HIGH/LOW/NORMAL" (应为 H/L/N 短码) — **硬规则答错**.
- Gemini Q3: 拒答具体代号, 指向 NCI EVS — **按设计逃避**.
- 两平台在同一题上都 FAIL, 但失败方式不同:
  - ChatGPT = 知识准确性问题 (记忆了错误的 codelist values)
  - Gemini = 产品设计 tradeoff (CO-2 为可靠性牺牲了应答完整性)

---

## Q6 PARTIAL 详情 (ACTARM/ACTARMCD 漏掉)

**PASS 判据**: 答案含 ACTARM / ACTARMCD vs ARM / ARMCD 区分.
**FAIL 判据**: 不识别 ACTARM (Actual Arm) 概念.

**Gemini 实答**:
> "如果受试者最初被随机化到 Arm A，尽管后来发生了非计划转换，在 DM 中通常仍记录 ARMCD = 'A'。SDTMIG 规定 DM.ARM 反映的是随机化时的计划组别。对于实际接受的治疗与计划不符，应通过 **ADaM 的 TRTP/TRTA 变量或 SDTM 的 EX 域（暴露）**来区分。"

**失误性质**: Planned-vs-Actual 概念对, 但 Gemini 把 "Actual" 责任错层到 **ADaM TRTP/TRTA 或 EX 域**, 没有识别出 SDTM DM 域本身就有 **ACTARM / ACTARMCD** 这对变量. 这是 SDTM 标准知识错点 — ACTARM/ACTARMCD 是 SDTMIG v3.4 DM 域 Permissible 变量, 专门用于 "Actual Arm" 记录, 不是 ADaM 才有.

**判定**: 不触发 "不识别 ACTARM 概念" 的 FAIL (因答案体现了 planned/actual 分离思维), 但触发 "ACTARM/ACTARMCD 命名缺失" — 故判 **PARTIAL** (0.5).

---

## CO-1 / CO-2 / CO-3 三硬约束验证

这是 Gemini C 方案 Tier 1 的核心设计约束, 用 smoke v2 做横向验证:

| 约束 | 定义 | smoke v2 命中情况 | 结论 |
|------|------|-------------------|:----:|
| **CO-1** | AE Core Anchor: 不推断 AE 域 Core 属性, 逐变量 grep spec | Q2 (AE SAE) 显式列 "AESER Exp / 6 子变量 Perm"; Q4 (AESEV) 提 "CO-1 提示 AE Core 不规则"; Q8 (AESTDTC/AESTDY) 列属性表 | ✅ 严格遵守 |
| **CO-2** | NCI EVS Guard: 不 inline CT term, 只返 codelist name + NCI EVS 链接 | Q3 LBNRIND: 拒答 H/L/N, 指向 C78736; Q4 AESEV: 拒答 MILD/MODERATE/SEVERE 具体值来源? 答案给了 "MILD/MODERATE/SEVERE" 作为标准三档 (*CT 值 inline*!) | ⚠️ **Q4 inline 了 MILD/MODERATE/SEVERE** (CO-2 边界模糊: 这些值是否算 CT inline? 它们是 AESEV codelist 的值) |
| **CO-3** | Source Citation: 每结论必附 knowledge_base/... 源路径 | Q1-Q10 每题末尾都有 "源路径: knowledge_base/..." 标注, Q6/Q8 甚至列章节号 | ✅ 严格遵守 |

**CO-2 的"Q4 inline MILD/MODERATE/SEVERE"观察**: 这可能是 gem 对 CO-2 的实际执行有**灰度**. Q3 严格拒答, Q4 则直接给出三档值. 推测原因: Q4 的 MILD/MODERATE/SEVERE 很可能出现在 gem 的 knowledge_base/domains/AE/spec.md 或 assumptions 原文里被当"参考值", 而 Q3 的 H/N/L 在 Gemini C 方案舍弃 terminology 后没有原文支撑, 故 gem 严守 CO-2. **这是 C 方案舍弃 terminology 导致的覆盖缺口**.

---

## 跨平台对比 — ChatGPT GPTs vs Gemini Gems

| # | 题 | ChatGPT | Gemini | 差异分析 |
|---|---|:---:|:---:|---|
| Q1 | CM 2 条 | PASS | PASS | 两平台都正确拆分 + 列 Core=Req |
| Q2 | AE SAE | PASS | PASS | 两平台 Y/N 判定一致 + 都区分 seriousness/severity |
| Q3 | LB NRIND | **FAIL** (答 HIGH/LOW/NORMAL) | **FAIL** (按 CO-2 拒答) | **两平台同题 FAIL, 失败方式不同**: ChatGPT 是知识错 (错码值), Gemini 是设计守则 (拒答以防幻觉) |
| Q4 | AESEV-CTCAE | PASS (给映射表) | PASS (建议不映射) | 两种技术路径, 都合 SDTM 原则; Gemini "不映射 → AETOXGR" 方案更学术严格, ChatGPT "1→MILD..." 更业务实用 |
| Q5 | PC LLOQ | PASS | PASS | 两平台答 PCORRES=<LLOQ + PCSTRESN=Null + 解释 bias, 一致 |
| Q6 | ARMCD/ARM + 换组 | PASS (含 ACTARM/ACTARMCD) | **PARTIAL** (漏 ACTARM) | **Gemini 独漏点**: 把 actual arm 责任错放到 ADaM, 未识别 SDTM DM 域的 ACTARM/ACTARMCD 变量 |
| Q7 | MH + CM | PASS | PASS | 两平台都答两域 + ONGOING 语义 |
| Q8 | ISO 8601 + STDY | PASS | PASS | 两平台算法一致 + 都说无 Day 0 + 部分精度 |
| Q9 | SUPPAE 例 | PASS (给 4 场景) | PASS (给 1 个完整例) | ChatGPT 列了 AESOSP/MIE/HIGH RISK FOR ADDITIONAL THROMBOSIS 4 场景, Gemini 给单一 ISREAC 例, 两边都命中判据 |
| Q10 | RELREC vs SUPP | PASS | PASS | 两平台答一致: 选 RELREC + 差异解释 + IDVAR/IDVARVAL 字段 |

**综合**: 两平台各以 9/10 (ChatGPT) vs 8.5/10 (Gemini) 过阈值. 失败点结构性不同:
- **ChatGPT 弱点**: 硬 CT codelist 短码容易错 (Q3 LBNRIND).
- **Gemini 弱点**: (a) CO-2 拒答 CT 具体值对"用户要代号"场景体验差 (Q3); (b) SDTM vs ADaM 变量归属混淆 (Q6 ACTARM 错层).
- **共同强项**: 规则推理 (Q4 Q5 Q8) + 业务场景 (Q1 Q2 Q7) + 鉴别判断 (Q9 Q10) 全对.

---

## 退出阈值决策

**标准 (SMOKE_QUESTIONS_V2.md line 215)**:
- ≥ 8/10 PASS → 进 Phase 4 (回归 + 完整 A/B)
- 7/10 PASS → CONDITIONAL_PASS, 列 carry-over Phase 4 前修
- ≤ 6/10 PASS → FAIL_REWORK

**Gemini 本次**: 严格二元 8/10 PASS (Q3 FAIL, Q6 PARTIAL 算 FAIL) → ✅ **达标进 Phase 4**

**Phase 4 待办项** (源于本次 smoke):
1. **Q3 LBNRIND 覆盖**: 考虑在 04 业务弹药包补一个 "CT term 值即便 CO-2 拒答也要给路径" 的业务补丁 (或弱化 CO-2 在"用户明确问代号"场景的边界).
2. **Q6 ACTARM 错层**: 在 02 spec 加一条 "DM 域 ACTARM/ACTARMCD 是 SDTM Permissible 变量, 非 ADaM" 的硬提示.
3. **其他 8 题不复测** (PASS 已证达标).

---

## 本次 session 技术教训

1. **Gemini Quill 编辑器 paste + 发送时机**: `execCommand('insertText')` + `InputEvent('input')` 后必须 **等 2 秒让 Angular 完成 dirty-check**, 再 UI click send. 否则 send 会抓到 ngModel 未同步的空值, Gem 回 auto-init 而非答题. Q3 Q6 各踩过一次.
2. **Gem auto-init 是固有行为**: fresh navigate + 发问 → Gem 首 turn 可能是"SDTM Expert Mode Activated"的 self-intro, 用户问题实际是 turn 2+. 不影响评分但影响 conversation URL 的 turn index.
3. **Pro mode 重置**: 每次 navigate 到 gem 根 URL, 模式回到 Fast, 需手动切换 Pro (2 次 click: dropdown → Pro option).
4. **收割方式**: `get_page_text` 抓 `<main>` 最可靠, 单次调用即可拿到用户问+gem 答完整文本, 远优于 `javascript_tool` 取 DOM (可能被 Cookie/长文过滤截断).
5. **10 题 session 长度**: ~80-100 tool calls, context ~5K+ tokens; 单 session 可承载 10 题完整走完, 无需 subagent 接力.

---

## Session 状态

- Gemini Gems Smoke v2 收割 + 评分 = **完成** (2026-04-21)
- 决策 = **Phase 4 进行** (8.5/10 严格 8/10, 达标)
- Phase 4 Gemini 待办 = Q3 CO-2 边界 + Q6 ACTARM 错层 (两处精修)
- 跨平台对比完成: ChatGPT 9/10 vs Gemini 8.5/10, 两平台都过阈值, Phase 4 可并行

## 双平台 smoke v2 汇总

**ChatGPT 9/10 PASS** (Q3 LBNRIND 短码错 HIGH/LOW/NORMAL)
**Gemini 8.5/10** (严格二元 8/10; Q3 CO-2 拒答 FAIL + Q6 ACTARM 错层 PARTIAL)

**跨平台 FAIL 差异**:
- 同一题 Q3 两平台都 FAIL, 但失败模式结构性不同 (ChatGPT 知识错 vs Gemini 守则守约)
- Gemini 额外 Q6 PARTIAL 为 C 方案舍弃 terminology 的衍生影响 (ACTARM 定义所在的 02/03 文件未显式展开"DM 域本身拥有 ACTARM/ACTARMCD"硬规则)
- ChatGPT 其余 8 题全 PASS 提示 batch 2 策略 (含 assumptions + examples + terminology) 在"基础 SDTM 规则判断"覆盖更广
- Gemini 其余 7 题 (Q2/Q4/Q5/Q7/Q8/Q9/Q10) PASS 证明 C 方案 (4 文件 + 业务弹药包) 在场景/规则/鉴别三大维度足够支撑

**结论**: 两平台都达 ≥8/10 阈值 → 进 Phase 4 完整 A/B 回归
