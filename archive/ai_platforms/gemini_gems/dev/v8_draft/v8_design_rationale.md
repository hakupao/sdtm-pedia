# Gemini v8 System Prompt — Design Rationale

> 起草: 2026-05-19 (R3 测试后 immediate follow-up)
> Writer: Claude main session (claude-opus-4-7)
> 基线: `ai_platforms/gemini_gems/current/system_prompt.md` v7.1 LIVE (423 行)
> v8 cut signal: SMOKE_V4 R3 (2026-05-19) Gemini 13/17, 4 FAIL — 见 `.work/07_release_v1_1/r3/{r3_matrix,R3_RETROSPECTIVE}.md`
> Reviewer §5 reference: `.work/07_release_v1_1/r3/evidence/_reviews/r3_review.md` (oh-my-claudecode:scientist, R3 Rule D #15)

---

## R3 4 FAIL → v8 4 prong 一对一映射

| R3 FAIL | 题文要点 | Gemini 跑题答 | v7.1 缺失锚 | v8 prong | 目标行为 |
|---|---|---|---|---|---|
| **Q3** BE/BS/RELSPEC | PGx 样本 BS-001 采血/运输/DNA 提取 + VOLUME/RIN + 派生关系 | AE/AESEV/AEGRPID (1541 chars off-topic) | CO 锚不含 biospecimen 关键词触发器 | **Prong 1 (CO-4 入口守门)** | 关键词命中 → 锚 BE/BS/RELSPEC, 切断 AE/CM fallback |
| **Q4 Scenario A** | 麻疹 IgG 1:128 滴定 (study unrelated) | LB ❌ (应 IS per v3.4 assumption 2) | v3.3→v3.4 IS scope shift 锚不在 CO-1 系列 | **Prong 3 (CO-1e IS scope shift)** | anti-microbial antibody → IS 不论 timing, sticky anchor 防退化 |
| **Q11** Dataset-JSON v1.1 vs XPT v5 | 文件格式痛点对比 + FDA timeline | AE/CM (1436 chars off-topic) | CO 锚不含文件格式 ground rule | **Prong 2 (CO-2f 文件格式)** | XPT/Dataset-JSON/Define-XML → ground CDISC 格式 spec, 禁替换 SDTM domain |
| **AHP1** LBCLINSIG | 短题文 plain factual: "LBCLINSIG 是什么 Core?" | CM 多药+MH 协同 (1485 chars off-topic) | AHP-V1 触发依赖题文 reflection scaffold ("如果你听说过 X"); plain factual 漏触发 | **Prong 4 (CO-5 default reflection)** | 题文 SDTM-shaped identifier 即触发, 不依赖 scaffold |

---

## Reviewer §5 4-finding 与 v8 prong 对照 (per `_reviews/r3_review.md`)

| Reviewer Finding | Priority | v8 Prong | 实施位置 |
|---|:---:|:---:|---|
| 1. Off-topic on BE/BS/RELSPEC (Q3) — add CO-N: biospecimen → BE/BS/RELSPEC, 不走 AE/CM | HIGH | Prong 1 | CO-4 顶部新增 "入口守门" 段 |
| 2. Off-topic on Dataset-JSON (Q11) — file format → ground in CDISC published standards, 不替换 SDTM domain content | MEDIUM (bonus 范围) | Prong 2 | CO-2 段新增 sub-clause CO-2f |
| 3. IS scope shift not stable (Q4-A) — v3.4 IS assumption 2, anti-microbial antibody → IS regardless of timing | HIGH (R2 修过的退回) | Prong 3 | CO-1 段新增 sub-clause CO-1e |
| 4. Reflection prompt dependency (AHP1) — 系统级 default behavior: SDTM variable name 询问, 先 verify exists in KB | HIGH | Prong 4 | CO-5 共同执行规则 #1 + 工作流程 Step 1 + AHP-V1 触发条件 三处协同改 |

---

## 4 Prong 具体改动详述

### Prong 1: CO-4 入口守门 (biospecimen keyword guard)

**位置**: `system_prompt_v8.md` CO-4 段顶部, 在原 "强制约束" 段之**前**插入新守门段.

**关键词触发器** (任一命中即触发):
- 中文: `生物样本` / `采血` / `分装` / `样本制备` / `样本运输` / `样本派生`
- 英文: `biospecimen` / `blood sample` / `aliquot` / `DNA extraction` / `RNA extraction` / `specimen derivation` / `PGx specimen` / `biorepository`

**强制锚** (按命中关键词类型分):
| 关键词类型 | 锚到域 | 关键变量 |
|---|---|---|
| 采集/运输/制备/提取**行为** | **BE** (Biospecimen Events) | BECAT="COLLECTION/TRANSPORT/PREPARATION/EXTRACTION" |
| 样本**测量值** (体积/RIN) | **BS** (Biospecimen Findings) | BSTESTCD="VOLUME/RIN" |
| 样本**派生/层级关系** | **RELSPEC** (Related Specimens) | REFID/PARENT/LEVEL |

**Anti-fallback**: 默认 AE/CM/LB/DM 兜底路径**禁止**. 若问题混合临床事件 + 样本, 必双域并行 (BE + AE/CM 不二选一).

**触发优先级**: 在 CO-4 GF/CP/BE/BS 详细变量表之**前** trigger. 即使题文未显式提 BE/BS/RELSPEC 域名, 关键词命中即锚.

**评估**: Gemini Pro 1M 窗口对显式 keyword trigger 比 abstract 概念锚响应好, 此守门通过 keyword 词典化实现"前 attention"硬锚.

### Prong 2: CO-2f 文件格式 ground rule

**位置**: `system_prompt_v8.md` CO-2e 后, CO-2c 前, 插入新 sub-clause CO-2f.

**关键词触发器**:
- 格式名: `XPT` / `SAS Transport v5` / `Dataset-JSON` / `Dataset JSON v1.1` / `Define-XML` / `Define-XML v2.1`
- 中文格式相关: `数据集格式` / `提交格式` / `传输格式`
- 痛点描述: `Unicode` / `8-char limit` / `200-char limit`
- 外部规范: `FDA Data Catalog` / `Pinnacle 21 file format`

**强制规则 (4 条)**:
1. **Ground 在 CDISC 公布格式规范**: XPT v5 / Dataset-JSON v1.1 / Define-XML v2.1 三者关系明示
2. **禁止替换为 SDTM domain content**: AE/CM/SUPPQUAL 等讨论与文件格式问题**无关**
3. **KB 边界声明**: KB 不 inline 文件格式 spec, 明示边界 + 指向 CDISC 官方
4. **跑题守门**: 答完 response 主体扫. 若主体是 SDTM domain 但题文是文件格式 → 删除全篇重答

**评估**: Q11 是 bonus 题 (Gemini 弱项 Q11-Q14), 但跑题答 AE/CM 是 hallucination 而非 "KB 不在线" punt — 必修.

### Prong 3: CO-1e IS scope shift v3.3 → v3.4 (sticky anchor)

**位置**: `system_prompt_v8.md` CO-1d 后, CO-2 前, 插入新 sub-clause CO-1e.

**核心规则**: SDTMIG v3.4 IS assumption 2 — anti-microbial antibody (麻疹/HIV/HCV/COVID 抗体) 不论 timing 全归 **IS**, 不归 LB, 不归 MB.

**Trap 场景表** (题文含此类描述必识破):
| 场景 | 正确域 | 关键变量 | v3.3 旧 path (禁) |
|---|:---:|---|:---:|
| 麻疹 IgG 1:128 滴定 | IS | ISBDAGNT=MEASLES VIRUS | ❌ LB |
| HBsAb / HCV Ab | IS | ISBDAGNT=HBV/HCV | ❌ LB |
| COVID-19 spike IgG | IS | ISBDAGNT=SARS-CoV-2 | ❌ LB |
| ADA (Anti-Drug Antibody) | IS | ISTSTOPO=SCREEN/CONFIRM/QUANTIFY | ❌ LB |
| Mtb 培养 | MB | MCORGIDN / MBMETHOD | (MB 正确) |
| HIV Ag/Ab combo (4th gen) | **MB** | MBTESTCD / MBORRES=reactive/non-reactive | ❌ IS / ❌ LB (Assumption 5 exemption per KB) |

**例外** (v8.1 reviewer reconcile 修正):
- **HIV Ag/Ab combo (4th gen)** → **MB** (Microbiology Specimen) 域, **per KB IS Assumption 5**. v8 初稿误写"可归 LB", 已修正为 MB. (HIV Ag/Ab combo 是 detection assay 性质, 不细化宿主免疫反应特征.)
- **细胞因子 / 趋化因子 / 补体测定** → **LB** (per KB IS Assumption 6)
- **ISTSTOPO 三层** SCREEN/CONFIRM/QUANTIFY → **per KB IS Assumption 8** (v8 初稿误标 Assumption 7a, 已修正).

**Sticky 设计**: R3 显示 v7.1 reset 后 Gemini 退回 v3.3 LB 路径 — 即 R2 修过仍不稳. v8 把此锚设为 **default behavior**, 不依赖题文措辞, 防 R2 fix decay.

**评估**: 这是 R3 最 strict signal — R2 修过的退回 = prompt-level memory 不稳, 需 sticky reinforcement.

### Prong 4: CO-5 default reflection (variable name regex trigger)

**位置 (3 处协同改)**:
1. **CO-5 共同执行规则 #1** — 主改动: 题文中**任何**满足 `^[A-Z]{2,5}[A-Z0-9]{0,12}$` 形态的 identifier 即触发 KB 双核, 不论题文 phrasing
2. **工作流程 Step 1** — 强化: 答题第一动作 = regex 扫所有 SDTM-shaped identifier 候选, 对**每一个**(不挑选不过滤) 跑双核. 未命中走 AHP-V1 路径, 命中走 Step 2 主答
3. **AHP-V1 触发条件** — 显式: v8 触发**不**等 reflection scaffold. AHP1 (LBCLINSIG) v7.1 漏触发 = v8 default 改动直接修复对象

**新增第 7 条 (跑题守门)**: 答完扫全文主体讨论域 vs 题文显式提及域是否一致. 不一致 = off-topic event → 删除全篇重答. R3 三次跑题 (Q3 / Q11 / AHP1) 直接修.

**评估**: 这是 R3 最 deep 的 prompt-architecture 改动. 从 "依赖题文 scaffold trigger" 改为 "regex-based default trigger" — 削减 prompt-injection-style 攻击面, 更稳健.

---

## v8 vs v7.1 改动量估算

| 段 | v7.1 行 | v8 行 | Delta | 性质 |
|---|---:|---:|---:|---|
| Header (title + cut signal block) | 1 | 8 | +7 | meta 标签 |
| CO-1 系列 (CO-1/CO-1b/CO-1c/CO-1d/**CO-1e**) | 1-111 | 1-180 | +~70 | **新 CO-1e** |
| CO-2 系列 (CO-2/CO-2e/**CO-2f**/CO-2c) | 113-141 | 180-230 | +~50 | **新 CO-2f** |
| CO-4 (入口守门 + 原变量表) | 143-206 | 230-310 | +~25 | **守门段** |
| CO-5 (AHP-V1 + 共同执行规则) | 208-269 | 310-395 | +~30 | **3 处协同改** |
| 工作流程 Step 1 | 405 | 460 | +1 (改写) | regex 强化 |
| 其余段落 | — | — | 0 | 完全不变 |
| **总计** | 423 | ~600 | **+~177 行 (+42%)** | 4 prong fix |

**风险**: v8 比 v7.1 +42% 长度, Gemini context window 仍宽裕 (1M 总, KB 注入 ~616K = 62%, prompt 部分 ~30K vs 19K), 不构成性能瓶颈.

---

## 预期 v8 dry-run outcome (4 fail 题)

| 题 | v7.1 R3 | v8 期望 | 改动 prong | 验证锚点 |
|---|:---:|:---:|:---:|---|
| Q3 BE/BS/RELSPEC | FAIL (答 AE) | **PASS** | Prong 1 | response 含 BE/BECAT/BS/BSTESTCD/RELSPEC 不含 AE/AESEV |
| Q4 Scenario A 麻疹 IgG | FAIL (答 LB) | **PASS** | Prong 3 | Scenario A 答 IS + ISBDAGNT=MEASLES VIRUS + ISORRES="1:128" |
| Q11 Dataset-JSON | FAIL (答 AE/CM) | **PASS or PARTIAL** | Prong 2 | response 含 XPT v5 8-char/200-char/no Unicode/external metadata 痛点 + Dataset-JSON v1.1 features + Define-XML 互补; (b) FDA timeline 可能 PARTIAL (KB 不全) |
| AHP1 LBCLINSIG | FAIL (答 CM/MH) | **PASS+** | Prong 4 | response 显式 "LBCLINSIG 非 v3.4 standard variable; LBCLSIG (8-char) 是标准; 或走 SUPP-- NSV" |

**预期总分**: Gemini v8 R3-equivalent = **17/17 (4 fail 修复全 PASS, 13 原 PASS 维持)**. 若 AHP1 升 PASS+ + Q11 走 PARTIAL (KB 限制), 实际可能落在 **16-17/17**.

**Caveat**: 实测必须在 Gemini Gem 上部署 v8 prompt + rebuild + 跑 4 题 (而非 17 全题, 节省 cycle). 此 dry-run 是 prompt-level 分析, 实战 verdict 需 Chrome MCP 验证.

---

## 风险与未尽事项

**1. ChatGPT 13 PASS+ > Claude 11 PASS+ trend (reviewer §3 observation)**

R3 显示 ChatGPT R3 PASS+ count 反超 Claude (R1 时 Claude 主导). 这**不是** v8 prompt 修的范围 (是 ChatGPT/Claude 各自的 prompt evolution 议题), 但反映:
- ChatGPT v2.2 prompt cycle 引入的 active correction / clinical pointer 已超 Claude v2.6
- Claude v2.6 在 Q14-type 多域题 response 长度偏薄 (1704 chars)
→ 留 v1.2 cycle Claude/ChatGPT 单独议题, 不在 v8 scope.

**2. NotebookLM PUNT 评分规则修订 (R3 RETRO §二 缺口 4)**

NotebookLM Q9 PUNT (Pinnacle 21 in-KB-only 拒答) = policy-correct 但被压低 0 分. R3 RETRO §二 缺口 4 已记, 待 v1.2 spec 修订 (PUNT-correct = 0.5).  
→ 不在 v8 prompt scope, 是评分规则 + NotebookLM v3 prompt scope.

**3. R3 vs R1 题库版本 noise (Q3 v3.2 → v4.0)**

R3 Q3 是 v4.0 BE/BS/RELSPEC 题 (与 R1 v3.2 DM ARMCD 不同). v8 修的是 v4.0 题, 不是 R1 题. matrix 已 inline 标注但易误读.  
→ R4 前必须 r3_kickoff.md 与 SMOKE_V4 §2 v4.0 题对齐. 不在 v8 scope.

**4. v8 prompt 长度 +42% 是否影响 Gemini attention recall**

v8 prompt ~30K tokens (v7.1 ~19K). KB 注入 ~616K. 总 prompt+KB 约 646K, 占 1M 上下文 65%, 仍宽裕. Multi-needle attention recall 在长 prompt 下可能 ~60% (Gemini 1M known), 但 v8 改动主要 reinforce 现有锚, 不依赖 long-range needle recall — 风险可控.

**5. Sticky anchor decay 风险 (R2 fix 退回观察)**

R3 显示 Q4-A R2 修过的退回. 提示 prompt-level memory 不稳, 即使 v8 加 sticky anchor, R4/R5 测试可能再退回. → 长期解需要测试 cycle 持续 monitor + 周期性 regression check, 不能单靠 prompt fix.

---

## 后续动作

1. **Reviewer subagent 审 v8 4-prong changes** (Rule D, different lane than main session writer): 建议 subagent_type `pr-review-toolkit:code-reviewer` 或 `oh-my-claudecode:critic`, run_in_background
2. **Dry-run 4 fail 题 dispatch** (Phase 2): Chrome MCP 部署 v8 prompt + 跑 Q3/Q4-A/Q11/AHP1 4 题, 验证 PASS, 若 PASS 走 v1.2 cycle 整合
3. **若 dry-run PASS**, cut v1.2 release tag `v1.2-gemini-prompt`; **若 partial**, 迭代 v8.1
4. **更新 SYNC_BOARD** "允许下一动作" 段, _progress.json 加 v8_draft 工程记录
5. **不在此 cycle 触发**: 4 平台同步 cut v1.2 (因 v8 仅 Gemini, 其他 3 平台 R3 全 PASS 或在 KB 限制, 不需要 prompt 改); v1.2 cut 单独议题, 由用户决策

---

*Design rationale 完成 2026-05-19. Writer 主 session.*

---

## 附录: v8 → v8.1 reviewer reconcile (2026-05-19 post-reviewer)

Reviewer `pr-review-toolkit:code-reviewer` (Rule D #16) 给出 PASS_WITH_OBSERVATIONS verdict, 6 项修复 (2 HIGH + 2 MEDIUM + 2 LOW) 已在 `system_prompt_v8.md` 全 apply:

| Fix | 类型 | 位置 | 改动 |
|---|:--:|---|---|
| **H1** | HIGH (factual) | system_prompt L138-148 + rationale 例外段 + trap 表 | HIV Ag/Ab combo: LB → **MB** (KB IS Assumption 5) |
| **H2** | HIGH (architecture) | CO-5 共同执行规则 #1 (L362) + 工作流程 Step 1 (L505) | 加 CO-2f 优先级 gate: 文件格式题不走 AHP-V1 路径 |
| **M1** | MEDIUM (regex) | CO-5 共同执行规则 #1 (L361) + 工作流程 Step 1 (L504) | regex 加否定清单 (FDA/CDISC/XPT/JSON 等非 SDTM 缩写跳过) + 域缩写跳过 |
| **M2** | MEDIUM (verbose) | 工作流程 Step 1 (L506) | 候选数限制: ≥ 5 时只扫题文显式提及 3-5 个 |
| **L1** | LOW (numbering) | system_prompt L142, L148, L160 | ISTSTOPO Assumption 7a → **Assumption 8** (per KB) |
| **L2** | LOW (CT note) | CO-4 入口守门 (L223) | BECAT EXTRACTION 注 "sponsor-extensible, 非 CT 锁定" |

**v8.1 line count**: 516 → 525 (+9 lines, +1.7%)
**reviewer evidence**: `ai_platforms/gemini_gems/dev/v8_draft/evidence/v8_reviewer_audit.md` (149 lines)
**dry-run gate**: H1+H2 不阻塞 dry-run (Q4-A 是麻疹非 HIV; Q11 CO-2f 优先实测验证). dry-run PASS 后即可 cut v1.2.
