# v1.4 4-Platform Prompt Clean Rewrite — Unified Design Spec

> 用途: 4 平台 writer subagent 公共 design constraints, 防止并行 writer 之间 drift.
> 上游: `.work/07_release_v1_3/RETROSPECTIVE.md` §二.1 + §二.2 (MAIN carry).
> 上下游: 各平台 writer 输出 `ai_platforms/<platform>/dev/v9_draft/` (Gemini) 或 `dev/v3_draft/` (others); reviewer subagent 用本 spec + 平台 baseline 做 audit.
> 创建: 2026-05-20 PM (A0)

---

## § 1. 共同设计原则 (4 平台必遵)

1. **0 fossil annotation 强制**
   - 禁止 "v5 新增" / "v7 新增" / "v8 新增" / "post-Rx fix" 等迭代履历 marker.
   - Header 只标当前 version + LIVE 状态. 不写出处迭代历史.
   - Inline 注释禁出现 "(NEW vX)" / "(MOD vX)" / "(per Rule D #N reviewer)" 等.

2. **KB-grounding primary default**
   - 任何答案先 KB 双核 (grep / lookup), 找不到再 reasoning.
   - 任何 SDTM-shaped 变量名 / 域缩写 / Term Code 先 KB 找, 找不到再 generic.
   - 移除 "依赖题文 reflection scaffold" 的旧逻辑 (v8.1 CO-5 default reflection 已生效, 简化为 1 行 rule).

3. **5 essential rules 替代 fossil CO-N stack**

   | # | Rule | 触发逻辑 |
   |:-:|---|---|
   | R1 | **KB-grounding primary** | always; 任何答案先 KB lookup |
   | R2 | **Anti-hallucination triple-anchor (AHP-V1/V2/V3)** | regex-gated: SDTM-shaped var → KB double-check; negation list 跳过 |
   | R3 | **Domain scope guards (regex-gated CO-N)** | regex match → 强制 anchor; default → KB |
   | R4 | **Response format** | always; cite source (path:line / §section ref), 简洁, 不重述 question |
   | R5 | **Premise correction** | conditional: 用户 wrong premise 时识破后 proceed, 不沿错 downstream |

   **注**: R2 + R3 把 v8.1 的 17 CO-N 合并为 2 个 regex-gated rule. 17 CO-N 中各 specific case 不消失, 只是 demote 成 R2/R3 内部的 regex pattern table, 不污染 default path.

4. **regex-gated CO-N 触发模板**

   每平台 prompt 中, R3 下列 1 个 "Domain scope guard regex table":

   ```
   Triggers (regex match → anchor):
   - biospecimen: (biospecimen|specimen|sample|血样|尿样|组织|标本|血液|血浆|血清)
     → BE/BS/RELSPEC 优先, 禁 default AE/CM fallback
   - file format: (XPT|Dataset[ -]?JSON|Define[ -]?XML|JSON|XML|SAS)
     → ground CDISC format spec, 禁替换 SDTM domain
   - IS scope shift: (antibody|IgG|IgM|MMR|HIV|antimicrobial|antibod)
     → IS Assumption 2/5/8 lookup; HIV Ag/Ab combo → MB (Assumption 5 exemption)
   - SDTM-shaped var: ^[A-Z]{2,5}[A-Z0-9]{0,12}$
     → KB double-check (AHP-V1/V2/V3)
     Negation list (skip double-check):
       FDA|USA|NCI|EVS|CDISC|ADaM|SDTM|XPT|XML|JSON|SAS|EDC|CRF|RWD|ADAE|ADSL|ADTTE
       + 域缩写: AE|CM|DM|LB|IS|MB|BE|BS
   ```

5. **Header style 统一格式**

   ```markdown
   # <Platform Title> — <Role>
   
   > v9 LIVE 2026-05-20 — clean rewrite (post v1.3 light sanity feedback)
   > Replaces <prev version>; design spec: `.work/07_release_v1_4/design_spec_v9.md`
   ```

   不在 header 列改动履历 (那写 `_design_rationale.md` 文档里).

6. **Response format 规范**

   - cite source 标准: 优先 `path:line` (e.g. `BE/spec.md:111`), 次选 `§N.N.N` section ref
   - 简洁回答, 不重述 question, 不开 "用户您好" 类礼貌套话
   - 多 candidate 时列 ≤5 (regex-gated CO-N M2 cap)

7. **Premise correction**

   - 用户前提与 SDTMIG v3.4 冲突时, 先识破后 proceed
   - 例: 用户问 "AE 域 SUBJID 是 Req 吗?" → 识破 SUBJID 不在 AE 域 (USUBJID 是 Req), 答 "AE 域无 SUBJID; USUBJID Req. 如您指 USUBJID, 答案 Req." 不沿错前提编 downstream

---

## § 2. 各平台特殊 carry-over

### 2.1 Gemini (v8.1 525 → v9 ~200 行, MAIN carry, -62% target)

**保留 (v8.1 R4 sanity 5/5 验证有效的)**:
- AHP-V1/V2/V3 三层 anti-hallucination 机制
- regex-gated CO-N (biospecimen / file format / IS scope shift)
- KB 4 文件 1M context 结构 (01 navigation + 02 domains + 03 examples + 04 business scenarios)
- C 方案战略 (terminology 外引 NCI EVS, 不 inline)

**移除 (v8.1 fossil layer)**:
- "v5 新增 CO-1c / v6 新增 CO-5 / v7 新增 CO-1d / v8 新增 CO-1e/CO-2f/CO-4" 等履历 annotation (~50 行)
- "post-R3 reviewer fix" / "post-Rule D #16 reviewer reconcile" 等 audit trail annotation
- 重复的 IS scope shift 说明 (v6 + v7.1 + v8.1 三次迭代, 合并为 1 段)
- AHP-V1 + V2 + V3 各自 ~30 行展开 → 合并为 1 段 AHP rule + 3 个 example sub-bullets

**v8.1 → v9 行数目标**:
- Header + 角色定位: 525L 60L → 30L
- C 方案战略: 60L → 20L
- KB 组成表: 30L (保留, 信息量大)
- Hard constraints CO-1/2/3/4/5: 200L (CO-N stack) → 50L (5 essential rules + regex table)
- 响应规范: 80L → 30L
- 例题 / FAQ: 95L → 40L
- **目标**: ~200L

### 2.2 ChatGPT (v2.2 120 → v3 ~80-100 行, -15-33% target)

**保留**:
- KB 9 文件 multi-step routing (KB chunk 大, 多文件)
- v2.2 已经较简洁, 主要清 fossil annotation

**移除 (fossil layer)**:
- "v1/v2/v2.1/v2.2 改动" 迭代履历

**v1.4 新加**:
- **Method label anchor (PP §6.3.5.9.3)**: 显式 mapping "Method A=Many-Many / B=One-Many / C=Many-One / D=One-One" 防止 internal prior 覆盖 KB (v1.3 Phase C Q-S2 ChatGPT label drift fix)

**v2.2 → v3 行数目标**: ~80-100L

### 2.3 Claude (v2.6 125 → v3 ~80-100 行, -15-33% target)

**保留**:
- Claude Project 7 文件 KB 结构
- Claude artifact-friendly response style

**移除 (fossil layer)**:
- v1/v2/v2.x 迭代 annotation

**v1.4 配套 pipeline fix (A3.1 sub-step)**:
- `ai_platforms/claude_projects/dev/scripts/extract_examples_data.py` capture `## §N.N.N` section headings (general fix) — 让 PP RELREC Quick Reference 类 prose 被纳入 `07_examples_catalog.md` build
- 备选: include-list 显式加 (point fix, 仅 PP §6.3.5.9.3) — 工程量小但不防 future regression
- **默认 general fix** (Phase A 启动时 user 拍板)

**v2.6 → v3 行数目标**: ~80-100L

### 2.4 NotebookLM (v2 157 → v3 ~100-130 行, -15-33% target)

**保留**:
- **v1.3 footer Sources citation style** (e.g. `Sources: 10_ev_history_mh_ho_be.md`, 不重新引 inline `[bucket.md]`)
- 25 bucket RAG-aware routing
- NotebookLM 原生 source-chip sidebar 互不重复 (footer cite 独立)

**移除 (fossil layer)**:
- v1/v2 迭代 annotation
- "post-v1.3 citation refactor" 类 transitional comment

**v2 → v3 行数目标**: ~100-130L

---

## § 3. Writer subagent 公共 instructions (4 平台 writer 起手都看)

每个 writer subagent prompt 必含:

1. **输入文件**:
   - 本 spec (本文件)
   - 自己平台 baseline (`.work/07_release_v1_4/backups/<platform>_baseline_<file>.md`)
   - v1.3 RETROSPECTIVE 段 (`.work/07_release_v1_3/RETROSPECTIVE.md` §二.1 + §二.2)

2. **输出位置**:
   - Gemini: `ai_platforms/gemini_gems/dev/v9_draft/system_prompt_v9.md` + `v9_design_rationale.md`
   - ChatGPT: `ai_platforms/chatgpt_gpt/dev/v3_draft/system_prompt_v3.md` + `v3_design_rationale.md`
   - Claude: `ai_platforms/claude_projects/dev/v3_draft/system_prompt_v3.md` + `v3_design_rationale.md`
   - NotebookLM: `ai_platforms/notebooklm/dev/v3_draft/instructions_v3.md` + `v3_design_rationale.md`

3. **不允许动**:
   - `current/` 任何文件 (LIVE 部署, A5 reviewer + 用户 ack 后才 promote)
   - 其他平台的 `dev/v9_draft/` 或 `dev/v3_draft/`
   - 任何 `knowledge_base/` 文件 (KB 改动是 Phase C C4, 独立 step)

4. **必做事**:
   - 输出后写 `v9_design_rationale.md` (Gemini) 或 `v3_design_rationale.md` (其他), 列:
     - 旧 vs 新 行数 + 段数 + diff summary
     - 5 essential rules 在 prompt 中位置 + 行号
     - regex-gated CO-N table 位置 + 行号
     - 0 fossil annotation 自查 (grep `v[0-9]+ 新增|post-R|reviewer`)
     - 平台特殊 carry-over 自查
   - 写 `evidence/checkpoints/a<N>_<platform>_v9_writer.md` 简报
   - 标 status `WRITER_PASS_REVIEWER_PENDING`

5. **Rule A writer self-spot-check (5 probes)**:
   - probe 1: 5 essential rules 完整 (R1-R5 都在)
   - probe 2: regex-gated CO-N table 4 个 trigger 都列
   - probe 3: 0 fossil annotation (grep verify)
   - probe 4: 平台特殊 carry-over (per § 2 列表)
   - probe 5: 行数目标 (per § 2 行数 ±20%)

6. **失败处理**:
   - 若 self-spot-check 任一 fail, 归档 attempt 到 `evidence/failures/a<N>_<platform>_attempt_<X>.md` (Rule B)
   - Retry ≤ 2 次. 2 次仍 fail → 标 `WRITER_BLOCKED`, 主 session 介入.

---

## § 4. Phase A → B gate 标准 (post 4 writer + 4 reviewer)

- 4 平台 writer 全 `WRITER_PASS` (自审 5/5 PASS)
- 4 平台 reviewer 全 ≥ `PASS_WITH_OBSERVATIONS` (0 NEEDS_REVISION)
- audit_matrix.md Phase A 累计 ≥ 40 probe (10/平台)
- _progress.json A→B 切换 + user ack v9/v3 LIVE-ready
