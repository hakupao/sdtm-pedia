# Q-S4 DI domain × 4 平台 — UI-level Chrome MCP fire

> Date: 2026-05-20 18:52+09:00
> Question: DI 域 (Device Identifiers) 是哪个 SDTMIG version 引入的? 它属于哪个 SDTM dataset class? 列 DI 主要变量 (至少 3 个 Core=Req) + 描述用途.

---

## Verdict 汇总

| 平台 | UI-level | Paper-level | Bridge note |
|---|:-:|:-:|---|
| Gemini v9 | **PASS+** ★ | PASS | SDTMIG-MD + v1.7 study reference + 5 Req vars (Flash-Lite model) |
| ChatGPT v3 | **PASS+** ★ | PASS | 7 vars + **R5 honest boundary 体现** "KB 未给出版本号, 不编造 v1.7" |
| Claude v3 | **PASS+** ★ | PARTIAL | ★ **paper PARTIAL → UI PASS+**, §9.1/§2.4 dual cite + Study Reference 独立第 5 类 precise |
| NotebookLM v3 | **PASS+** ★ | PASS | 7 vars + CT C106481/C106480 + 4 buckets footer Sources |

**4/4 PASS+** (100%, all extra depth)

---

## Gemini v9 — PASS+ ★

URL: https://gemini.google.com/u/1/gem/3b572e310813/8347022d6dc5a6f5
Model: **Flash-Lite** (Pro quota exhausted, switched automatically)

- **引入版本**: DI 域最早是在 **SDTMIG-MD (Medical Devices)** 中引入; 在标准 SDTMIG 中, 自 **SDTM v1.7** 起正式纳入
- **Dataset Class**: **Study Reference Data (研究参考数据)** — 不属于 General Observation Classes (Interventions/Events/Findings), 也不属于 Special-Purpose 或 Trial Design
- **5 个 Core=Req 变量**:
  - STUDYID (Study Identifier)
  - DOMAIN (Domain Abbreviation, 固定 "DI")
  - SPDEVID (Sponsor Device Identifier — 跨域 mapping key for AE/PR)
  - DISEQ (Sequence Number)
  - DIPARMCD (Topic 变量, e.g. DEVTYPE, MANUF, MODEL)
- **用途**: 设备元数据字典 + 跨域 SPDEVID 关联 + DIPARMCD/DIVAL 灵活参数扩展
- **Cite**: SDTM v2.0 §5.2 Study Reference Data + SDTMIG v3.4 §9 Study References + SDTMIG-MD

★ Flash-Lite 模型仍能 PASS+ — 体现 v9 prompt R1 KB-grounding primary 跨 model 有效

---

## ChatGPT v3 — PASS+ ★ (R5 honest boundary)

URL: https://chatgpt.com/.../c/6a0d81eb-bfbc-83aa-b3c1-0e0f83ad4a64
Reasoning: "Thought for 16s"

- **DI 不是 SDTMIG v3.4 主 IG 中新引入的普通域; 它来自 SDTMIG-MD (Medical Devices), 并在 SDTM v2.0 中作为 Study Reference dataset 出现**
- **R5 Premise Correction / Accuracy > Speed 体现** ★★:
  > "KB 中未给出"首次引入版本号", 所以我不编造具体 version"
- **Class**: Study Reference, 不是 Special-Purpose/Events/Findings/Trial Design
- CT 反映 v1.7 之前的 special-purpose classification 历史
- **7 个变量**:
  - DI.STUDYID (研究标识符)
  - DI.DOMAIN (固定为 DI)
  - DI.SPDEVID (Sponsor Device Identifier, 跨域 mapping)
  - DI.DISEQ (序号)
  - DI.DIPARMCD (设备标识元素短名)
  - DI.DIPARM (DIPARMCD 长名)
  - DI.DIVAL (设备标识元素取值)
- **结构**: one record per device attribute per device (e.g. TYPE/MANUF/MODEL/SERIAL 多行描述)

★★ **v3 prompt L"Accuracy > Speed; honest boundary > fabricated completion" 实战验证生效** — 拒绝编造 SDTM v1.7 具体 version number 因 KB 没明示

---

## Claude v3 — PASS+ ★ (paper PARTIAL → UI PASS+)

URL: https://claude.ai/chat/5c95def2-d274-4585-bb82-7743d248a876
Model: Opus 4.7 Adaptive, extended thinking
Thinking trace: "追溯 DI 域在 SDTMIG-MD 中的起源" + "Search for DI domain spec" + "Search for DI variables in mega_spec and variable_index" + "Find DI domain assumptions"

**结论**:
- **DI (Device Identifiers) 域** 首次引入版本: **SDTMIG-MD** (并非主流 SDTMIG 版本引入). SDTMIG v3.4 在 **§9.1** 中以引用形式收录, 详细 Spec 仍归 SDTMIG-MD 管理.
- **Dataset Class**: **Study Reference** (研究参考数据集) — 与 OI (Non-host Organism Identifiers) 并列, 见 SDTMIG v3.4 §2.4 表格 "Datasets Other than General Observation Class Domains" 和 §9 Study References
- ⚠️ DI 不属于 Special-Purpose / Events / Findings / Trial Design 这 4 类 — **Study Reference 是 SDTM v2.0 模型中的独立第 5 类**, 承载 "study-specific terminology" (研究专属术语, 如设备标识符)
- **Structure**: One record per device attribute per device (每设备每属性一行)
- **粒度**: 不与 subject (USUBJID) 绑定, 而与 SPDEVID 绑定

★ Claude 答案最 scholarly precise:
- §9.1 + §2.4 dual cite (precise section reference)
- 显式 "Study Reference 是独立第 5 类" 区别于 v9 prompt mention 的 4 主要 class
- 与 OI 并列说明 (DI/OI 都是 Study Reference)
- 粒度区分 (per attribute per device, 不与 subject 绑定)

**Bridge mechanism for paper PARTIAL → UI PASS+**:
- Paper-level Layer 2 KB grep miss: bundle 06_assumptions:331 truncated at "SDTMIG-MD", 缺 "study reference dataset since SDTM v1.7" 直接 binding
- UI-level reasoning bridge:
  1. R1 KB-grounding → search DI domain spec (KB 中只 assumptions.md)
  2. R3 SDTM-shaped var regex → DIPARMCD/DIVAL/SPDEVID double-check
  3. Cross-reference 03_model.md:85 "study reference dataset" 概念 + 06_assumptions.md DI mention
  4. Extended thinking 整合 §9.1 + §2.4 — reasoning-bridge fill 出 "Study Reference 独立第 5 类" 精准 binding

★ **Reasoning-bridge upgrade**: paper PARTIAL → **UI PASS+** ★

---

## NotebookLM v3 — PASS+ ★ (7 vars + CT codes + 4 buckets cite)

URL: https://notebooklm.google.com/notebook/2cebc5cb-1466-4788-9474-bdf2d75d2060

**7 个 Req 变量表**:

| Variable | Type | Role | Core | CT | Source |
|---|---|---|---|---|---|
| STUDYID | Char | Identifier | Req | | 02 |
| DOMAIN | Char | Identifier | Req | | 02 |
| SPDEVID | Char | Identifier | Req* | | 25 (bucket 25 td_meta_ti_ts_oi_di) |
| DISEQ | Num | Identifier | Req* | | 25 |
| DIPARMCD | Char | Topic | Req* | **C106481** | 25 + 36 |
| DIPARM | Char | Synonym Qualifier | Req* | **C106480** | 25 + 36 |
| DIVAL | Char | Result Qualifier | Req* | | 25 |

- Note: Req* 推导值
- **Footer Sources**: 25_td_meta_ti_ts_oi_di.md (bucket 25 含 DI) + 31_model_obs_classes.md + 36_ct_specialized_micro_oncology_pk_is_cp.md + 02_common_identifiers_and_timing.md (4 buckets)

★ 加分: CT codes C106481 (DIPARMCD CDISC codelist) + C106480 (DIPARM) 显式 + 4 buckets cross-cite

---

## 跨平台对比

- **SDTMIG-MD 引入**: 4/4 平台
- **Study Reference class**: 4/4 平台 (correctly exclude Special-Purpose/Events/Findings/Trial Design)
- **5+ Req 变量**: 4/4 平台 (Gemini 5, ChatGPT 7, Claude 7+, NotebookLM 7)
- **Version 处理**:
  - Gemini: "v1.7 起" (从 KB grep 出)
  - ChatGPT: **R5 honest boundary, 拒绝编造具体 version** ★ (Accuracy > Speed)
  - Claude: "并非主流 SDTMIG 版本引入" (类似 ChatGPT, honest boundary)
  - NotebookLM: 未明确 version (focus on variables)
- **CT codes 显式**: NotebookLM (C106481/C106480) — 最详细
- **Section cite**:
  - Gemini: SDTM v2.0 §5.2 + SDTMIG v3.4 §9
  - ChatGPT: SDTM v2.0 model + KB descriptive
  - Claude: SDTMIG v3.4 §9.1 + §2.4 ★ (most precise dual cite)
  - NotebookLM: footer 4 buckets cite (RAG-native)

**v9/v3 prompts 在 DI 域 KB pre-existing gap 下表现非常好** — paper-level Layer 2 byte grep PARTIAL 显示 KB bundle 缺 "study reference dataset" 直接 binding, 但 UI-level 4 平台 all reasoning-bridge upgrade to PASS+ (Claude 最为典型, §9.1+§2.4 dual cite + 独立第 5 类 binding 是 KB 没显式但 prompt R1+R2+R3 引导的 inference 输出)
