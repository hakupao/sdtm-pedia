<!-- chain: F (深度验证旁枝链 v2)
  修改本文件后, 必须检查:
  → _progress.json                       (程序化进度)
  → evidence/checkpoints/                (每 phase 快照)
  → ../03_verification/issues_found.md   (问题回流, 继续编号 Issue 5+)
  → ../meta/worklog.md                   (工作日志)
-->

# 06 Deep Verification — Word-Level PDF→KB Audit

> 创建: 2026-04-24
> 状态: **DRAFT v0.6** — P0 Pilot ✅ PASS + P1 batch 01-34 cumulative **8552 atoms / 340 页 (61.8% of 535) / 1 dropout / 50 repair cycles across 18 batches / 92 findings**; schema v1.2 frozen; **v1.4 prompts active 2026-04-28** (4 prompts P0_writer_pdf/md/matcher/reviewer 24 round 5+6+7 candidates absorbed N1-N14 EMERGENCY-CRITICAL — Rule D reviewer #44 omc:document-specialist AUDIT verdict PASS 22/22 + v1.3 archived to `archive/v1.3_final_2026-04-28/`); multi-session 7 rounds COMPLETED (~10-12 hours wall savings vs serial baseline / 0 quality regression / 0 cross-round Rule D collision / 24 AUDIT-mode pivots cumulative); 待用户 ack v0.6
> 历史: v0.4 (post verifier v0.3) → v0.5 (post P0 Pilot 收官 + T2b FIGURE 补测) → **v0.6** (post v1.4 cut 2026-04-28 + multi-session round 7 closure + cleanup)
> Tier: **3** (>15 step, 多 session, 高 stakes, 不计时间成本)
> 旁枝定位: 独立于 `.work/03_verification/` (Step 0-4 已全部 PASS), 本工程为"字面级"深审, 发现的问题走 Issue 5+ 回流修复

---

## 0. Charter

### 0.1 目的 (Why)

以 **PDF 原文为 ground truth**, 按 **语义原子** 将 535 页源逐条拆解, 与 `knowledge_base/` 建立 **双向 coverage ledger**, 回答:

- **PDF → MD**: 每个 PDF 原子是否在 KB 中有落点 (EXACT / EQUIVALENT / PARTIAL / MISSING / ERROR / INTENTIONAL_EXCLUDE)
- **MD → PDF**: 每个 KB 原子是否有真实源 (SOURCED / UNSOURCED / HALLUCINATED / SYNTHESIZED)

产物是一份 **机器可查、字面可 diff 的账本**, 任何后续争议可回查字面依据.

### 0.2 范围 (Scope)

**In-scope** (141 份 AI 提取的 md, 实测 2026-04-24, v0.3 Fix F-1):

- `source/SDTM_v2.0.pdf` (74 页)
- `source/SDTMIG v3.4 (no header footer).pdf` (461 页)
- `knowledge_base/` AI 提取的 md (总 141):
  - `domains/*/assumptions.md` × **63** (v0.2 写 61 错)
  - `domains/*/examples.md` × 63
  - `model/*.md` × 6
  - `chapters/*.md` × 6
  - **top-level × 3** (`INDEX.md` / `ROUTING.md` / `VARIABLE_INDEX.md` — AI 或 AI 脚本产物, 用户 2026-04-24 拍板谨慎纳入)
- 60 幅已转化图像的页码 / 字面精确化 (Issue 1 遗留)

**Out-of-scope** (本工程不审):

- `knowledge_base/domains/*/spec.md` × 63 — xlsx 脚本派生 + 历史校验 PASS
- `knowledge_base/terminology/` × 91 — xlsx 脚本派生
- `ai_platforms/` 下产物 — Phase 6.5 独立分支
- PDF 版式元素 (页眉, 页脚, 页码数字)

**盘点自检**: 141 in-scope + 63 spec + 91 terminology = **295 md 全覆盖** (`find knowledge_base -name "*.md" | wc -l` 实测), 无遗漏.

### 0.3 成功标准 (Exit)

三条 gate 同时 PASS:
1. **覆盖率**: PDF 原子 ≥ **99%** 有 verdict (入 MD 或显式 INTENTIONAL_EXCLUDE 含理由)
2. **人工抽样**: 用户随机分层抽 **≥ 50** 原子独立复检, 误判率 < **5%**
3. **独立复核**: Rule D reviewer (不同 `subagent_type`) PASS

### 0.4 非目标

- 不重做 Step 0-4 (既有账本原样保留为历史层)
- 不追求 "PDF 100% 转入 MD" (允许显式排除, 但必须有理由)
- 不优化 KB 写作风格 — 只审字面覆盖

---

## 1. 定位 vs 既有工作

| 维度 | Step 0-4 (已完成) | 本工程 06 Deep Verification |
|---|---|---|
| 方向 | MD-centric ("md 对不对") | PDF-centric ("每字每句去向") |
| 粒度 | 节级 / 要点级 | 语义原子级 (字面 verbatim) |
| 审阅模型 | agent 按页码均分 (Issue 3 暴露盲区) | 1 页 = 1 agent; 1 原子比对 = 1 micro-agent |
| 产物 | 修复后 PASS 报告 + TRACEABILITY.md 页级映射 | JSONL 双向账本 + 字面 verbatim |
| 对 KB 影响 | 直接修 KB | 发现问题走 Issue 5+, 独立 writer/reviewer 修 |

---

## 2. 硬规则 (不变量 IR1-IR8)

与全局 CLAUDE.md `<personal_operating_principles>` 规则 A/B/C/D 及 OMC `<operating_principles>` 相容.

| ID | 规则 | 理由 |
|---|---|---|
| **IR1** | 单次 subagent 输入 ≤ **1 PDF 页** 或 **1 md 节 (≤300 行)** | context 越大质量越崩; 拒绝 "一个 agent 吃 20 页" |
| **IR2** | 最小单元 = **语义原子**, 非段落、非页 | 防止 "3 页长段 = 1 unit" 造成的稀释 |
| **IR3** | Writer ≠ Reviewer, **不同 subagent_type**; 每 phase ≥ 3 种 slot; **batch 粒度 = 100 原子** (v0.3 Fix F-4), 批间 writer_type 循环轮换 | 同 ctx 自审无效 (Rule D); 5000+ 规模下 per-batch 可落地, per-atom 池不够 |
| **IR4** | 失败 attempt 归档 `evidence/failures/` 不删 | Rule B 强制 |
| **IR5** | 每个原子必带 `verbatim` 原文 + `page` + `parent_section` + `extracted_by` | 字面可 diff, 可溯源 |
| **IR6** | 每个比对必有 `verdict ∈ {EXACT, EQUIVALENT, PARTIAL, MISSING, ERROR, INTENTIONAL_EXCLUDE}` | 杜绝模糊 "大体 OK" |
| **IR7** | 每 phase Rule A 语义抽检样本 ≥ **30** (压缩/改写率高按 N 样本独审) | 结构 PASS ≠ 语义 PASS |
| **IR8** | 每次 subagent 调用都写 `trace.jsonl` (type / prompt_hash / input_hash / output_hash / verdict) | 可回溯, 可复现 |

**违反任一 IR → 该 phase 不得进 gate**.

---

## 3. 原子类型表 (ATOM_TYPE 枚举)

| ATOM_TYPE | 定义 | 典型粒度 | PDF 形态 | MD 形态 |
|---|---|---|---|---|
| `SENTENCE` | 1 句独立规则/定义/事实句 | 1 句 | 正文句子 | md 段中的 1 句 |
| `LIST_ITEM` | 1 个编号/项目列表项 | 1 项 | "1. ..." / "- ..." | "- ..." |
| `TABLE_ROW` | 数据表 1 行 (非变量 spec) | 1 行 | PDF 表 1 行 | md table 1 行 |
| `TABLE_HEADER` | 表列头集合 | 1 原子/表 | PDF 表头 | md table 头 |
| `CODE_LITERAL` | 1 个 C-code / 字符串常量 | 1 字面 | "C66742" | 同 |
| `CROSS_REF` | 1 个交叉引用 pointer | 1 指针 | "See §4.2.1" | 同 |
| `FIGURE` | 1 幅图 (+ 每节点/边/标签子原子可选 L2 拆) | 1 图 | PDF 嵌入图 | Mermaid 或表 |
| `HEADING` | 节标题 (结构锚) | 1 标题 | "4.2.1 Domain Name" | md `## 4.2.1 ...` |
| `NOTE` | 脚注、[CDISC Notes]、方框注 | 1 条 | 编辑注 | md 注释行 |

**粒度决策规则**:
- 长陈述 "X shall Y when Z and W" → **不**拆成 "X shall Y" / "when Z" / "and W", 保为 1 个 SENTENCE (保语义原子性)
- 项目列表内句 → LIST_ITEM 作外层容器; 若内含多规则, 可选 L2 拆成 sub-SENTENCE
- 图像原子化: 默认 1 幅图 = 1 FIGURE 原子, 含 `describes_text` 字段回文; 决策树类 L2 可拆节点集

**估算总原子数**: 535 页 × ~10 atoms/页 ≈ **5000–7000**
(PDF 中 spec 表按 `TABLE_ROW` 原子化, 1 变量行 = 1 原子; xlsx 派生的 `knowledge_base/domains/*/spec.md` 不在本工程范围, 由已有脚本校验)

---

### 3.1 Section-level 聚合 — 三类失效模式检测 (用户 v0.1 review 反馈核心)

**原子级 verdict 不足以捕获用户真正担忧的三类 KB 失效**:

| 失效模式 | 表现 | 为什么原子级单独看不出 |
|---|---|---|
| **CONTENT_TRUNCATED** | 大段文字被简化 | 少数原子 EQUIVALENT 混过, 整段占比不够也能遮掩 |
| **SKELETON_ONLY** | 多级标题只剩标题没有内容 | HEADING 匹配过了, 子内容全 MISSING 不聚合看不出 |
| **SIBLING_DROPPED** | 多级子标题只有第一个还存在 | §X.1 PASS 遮蔽 §X.2 – §X.N 缺失 |

**解决方案**: 在 P4a (原子匹配) 完成后执行 P4b (section 聚合), 按 HEADING 原子树归并, 计算每节的 coverage density 和 child-section 完整性. Schema 见 §4.5, 流程见 §5 P4b, gate 见 §9.2. **这是 PLAN v0.1 → v0.2 最重要的架构追加**.

---

## 4. 数据模型 (JSONL Schema)

### 4.1 `pdf_atoms.jsonl`

```jsonc
{
  "atom_id": "ig34_p0425_a012",
  "source": "SDTMIG_v3.4",
  "page": 425,
  "page_region": "top|middle|bottom|full",
  "parent_section": "§8.2.1 RELREC",
  "atom_type": "SENTENCE",
  "verbatim": "RELREC is used to represent any relationship ...",
  "normalized": null,
  "figure_ref": null,
  "cross_refs": [],
  "extracted_by": {
    "subagent_type": "oh-my-claudecode:explore",
    "prompt_hash": "sha256:...",
    "ts": "2026-04-24T14:00:00Z"
  }
}
```

### 4.2 `md_atoms.jsonl`

```jsonc
{
  "atom_id": "md_ch08_a042",
  "file": "knowledge_base/chapters/ch08_relationships.md",
  "line_start": 120,
  "line_end": 123,
  "parent_section": "## §8.2.1 RELREC",
  "atom_type": "SENTENCE",
  "verbatim": "RELREC represents relationships between ...",
  "extracted_by": { "subagent_type":"...", "prompt_hash":"...", "ts":"..." }
}
```

### 4.3 `coverage_ledger.jsonl`

```jsonc
{
  "pdf_atom_id": "ig34_p0425_a012",
  "md_atom_ids": ["md_ch08_a042"],          // 空数组 = MISSING
  "verdict": "EQUIVALENT",
  "similarity_score": 0.92,                 // optional fuzzy score
  "discrepancy": "md omits '...' clause",   // 仅非-EXACT 时填
  "exclusion_reason": null,                 // 仅 INTENTIONAL_EXCLUDE 时填
  "matched_by": { "subagent_type":"...", "prompt_hash":"...", "ts":"..." },
  "audited_by": [{"subagent_type":"...", "ts":"...", "verdict":"CONFIRM|OVERRIDE"}]
}
```

### 4.4 verdict 枚举

**正向 (PDF → MD)**:

| verdict | 语义 |
|---|---|
| `EXACT` | 字面相同 或 规范同义 (如 `Req` vs `Required`) |
| `EQUIVALENT` | 语义一致但有改写 |
| `PARTIAL` | md 只覆盖了 pdf 原子的一部分 |
| `MISPLACED` | **md 含原子文本 (EXACT/EQUIVALENT) 但 parent_section 与 PDF 不符** (v0.3 Fix F-2, Issue 4 §8.4.4 教训) |
| `MISSING` | md 找不到该原子内容 |
| `ERROR` | md 内容与 pdf 冲突 (错误事实, 幽灵变量) |
| `INTENTIONAL_EXCLUDE` | 故意未入 md (必须填 exclusion_reason 并登记白名单, 见 Appendix D) |

**匹配算法强制 (v0.3)**: P4a prompt 必检 `pdf_parent_section` vs `md_parent_section` 对齐; 不对齐但文本匹配者单起 `MISPLACED` verdict, 自动开 Issue 5+.

**反向 (MD → PDF)**:

| verdict | 语义 |
|---|---|
| `SOURCED` | md 原子在 pdf 可找到源 |
| `UNSOURCED` | md 有但 pdf 无, 需判定是否 "合理推断" or 幻觉 |
| `HALLUCINATED` | pdf 无且不合理 |
| `SYNTHESIZED` | 作者合成 (如 Mermaid 图、Examples 结构重组) |

### 4.5 `section_coverage.jsonl` (新增, v0.2 核心)

由 P4b 从 `pdf_atoms.jsonl` + `coverage_ledger.jsonl` 聚合而成. 按 HEADING 原子构建 PDF 节树, 每节产 1 条记录:

```jsonc
{
  "section_id": "ig34_§4.2.7",
  "section_title": "Submitting Free Text",
  "pdf_page_range": [28, 30],
  "pdf_atom_count": 34,                 // 该节所有非-HEADING 原子
  "md_target_files": ["chapters/ch04_general_assumptions.md"],
  "md_atom_count_matched": 8,           // verdict ∈ {EXACT, EQUIVALENT}
  "md_atom_count_partial": 2,           // verdict = PARTIAL
  "md_atom_count_missing": 24,          // verdict = MISSING
  "coverage_density": 0.235,            // matched / pdf_atom_count
  "child_sections": {
    "§4.2.7.1 Text Case": "MATCHED",
    "§4.2.7.2 Quotation Marks": "MATCHED",
    "§4.2.7.3 Special Characters": "MISSING",      // 子标题 PDF 有但 MD 无
    "§4.2.7.4 Foreign Language": "SKELETON_ONLY"   // 子标题在 MD 但内容 0 覆盖
  },
  "aggregate_verdict": "CONTENT_TRUNCATED",
  "failure_patterns": ["CONTENT_TRUNCATED", "SIBLING_DROPPED"],
  "aggregated_by": { "phase":"P4b", "ts":"..." }
}
```

**aggregate_verdict 枚举** (v0.3 加 `STRUCTURE_DRIFTED` + 优先级决策表 + 关键词升级规则 Fix F-3):

| verdict | 判定规则 | 对应担忧 |
|---|---|---|
| `FULL_COVERAGE` | coverage_density ≥ 0.95 且所有 child_sections = `MATCHED` 且 MISPLACED 原子率 < 5% | — |
| `MOSTLY_COMPLETE` | coverage_density ∈ [0.80, 0.95) **且无 shall/must 关键词丢失** | — |
| `CONTENT_TRUNCATED` | coverage_density ∈ [0.20, 0.80), HEADING 匹配; **或 MOSTLY_COMPLETE 触发关键词升级** | 大段简化 |
| `SKELETON_ONLY` | coverage_density < 0.20, HEADING 匹配 | 只剩标题 |
| `SIBLING_DROPPED` | 任一 child_section ∈ {`MISSING`, `SKELETON_ONLY`, `CONTENT_TRUNCATED<0.60`} | 子标题只剩第一个 |
| `STRUCTURE_DRIFTED` | 该节 md_atom 中 **≥10% 源自 PDF 其他节** (MISPLACED 聚合) | Issue 4 式错位 (v0.3) |
| `HEADING_MISSING` | 父 HEADING 原子未匹配 | 整节丢失 |
| `ORPHANED` | MD heading 无对应 PDF section (反向聚合) | 幻觉节 |

**MOSTLY_COMPLETE 关键词升级规则 (v0.4 分层, Fix NF-2)**:

若该节 `md_atom_count_missing` 中 ≥1 个 SENTENCE 原子 verbatim 命中以下清单, 按 Level 处理:

**Level 1 — 强制降级** (命中任一即降到 `CONTENT_TRUNCATED` 进 gate):
`shall` | `shall not` | `must` | `MUST` | `must not` | `required` | `is required` | `are required` | `is not permitted` | `is prohibited` | `not permitted` | `may not`

**Level 2 — 标记抽检** (命中不自动降级, 标 `keyword_flag` 字段入 `section_coverage.jsonl`; §9.2 抽检条款对应覆盖):
`should` | `only` | `except` | `no longer` | `cannot` | `not allowed`

**同时命中**: 优先执行 Level 1 降级 (Level 2 flag 仍并存记录).

**aggregate_verdict 优先级决策表 (v0.3 Fix F-3, 多 pattern 同时命中取优先级最差者作单值 `aggregate_verdict`)**:

```
STRUCTURE_DRIFTED > HEADING_MISSING > SKELETON_ONLY > SIBLING_DROPPED > CONTENT_TRUNCATED > MOSTLY_COMPLETE > FULL_COVERAGE
```

**child_sections 状态枚举** (v0.3 四值化 Fix F-3, 替代 v0.2 二值):
`MATCHED` | `MISSING` | `SKELETON_ONLY` | `CONTENT_TRUNCATED`

一节可同时打多个 `failure_patterns` (如既 CONTENT_TRUNCATED 又 SIBLING_DROPPED), `aggregate_verdict` 按上述优先级决策表取单值.

---

## 5. Phase 骨架

| Phase | 目标 | 并行 | 预估 session | Exit gate |
|---|---|---|---|---|
| **P0 Pilot** | 工具/schema 端到端跑通 1 小文件 | 串行 | 1 | pilot ledger 完整 + Rule D PASS + schema 冻结 |
| **P1 PDF 原子化** | 535 页拆原子 | 1 页 = 1 agent, 批 ~20 | 3–5 | 100% 页覆盖 + 30 页 Rule A 独审一致率 ≥90% |
| **P2 MD 原子化** | 136 md 拆原子 | 1 文件 = 1 agent (大文件切段) | 1–2 | 100% 文件覆盖 |
| **P3 索引构建** | 脚本建 md 原子倒排 (token + n-gram) | 纯脚本 | 0.5 | 每 PDF 原子可查 top-5 候选 |
| **P4a 正向匹配 PDF→MD** | 每 PDF 原子 verdict | 1 原子 = 1 micro-agent | 4–6 | 100% PDF 原子 verdict 存 + 50 样本 Rule A PASS |
| **P4b Section 聚合** | HEADING 树归并, 产 `section_coverage.jsonl`, 检测三类失效 | 脚本 + 1 reviewer agent 抽查 | 0.5 | 每 PDF 节有 aggregate_verdict; 0 节 `SKELETON_ONLY` 未登记解释 |
| **P5 反向匹配 MD→PDF** | 每 MD 原子回源 | 同 P4a | 2–3 | 100% MD 原子 verdict 存 |
| **P6 Triage + Repair** | MISSING/ERROR → Issue 5+ | writer/reviewer 分离 | 2–4 | 覆盖率 ≥99% + Issue 全 closed |
| **P7 人工抽样 + Retro** | 用户抽 50+ 原子 + RETROSPECTIVE | 用户为主 | 1 | 误判 <5% + Retro 归档 |

**每 phase 收尾强制 (v0.4 Fix Gap 7, Tier 3 template §6)**: 写 `phase_report` 事件到 `trace.jsonl` (字段: `phase_id` + `summary` + `gate_status` + `evidence_refs` + `ts`). 无 phase_report 的 phase 视为未完成, 不得进下一 phase.

**总估**: 14–22 sessions 分布数周 (已接受 "不计成本").

### 5.1 P0 Pilot 细化 (最优先, v0.3 扩 3 target Fix F-5)

**Target 集合** (覆盖 9 种原子类型中 ≥6 种):

| # | md | PDF | 覆盖原子类型 |
|---|---|---|---|
| **T1** | `knowledge_base/model/04_associated_persons.md` (38 行, 实测) | `SDTM_v2.0.pdf` p.50 | SENTENCE / LIST_ITEM / TABLE_ROW / HEADING |
| **T2** | `knowledge_base/chapters/ch08_relationships.md` §8.2 前 ~50 行 | `SDTMIG v3.4.pdf` p.425 附近 | + FIGURE + CROSS_REF |
| **T3** | `knowledge_base/domains/AE/assumptions.md` 前 ~30 行 | `SDTMIG v3.4.pdf` AE 章一页 | + CODE_LITERAL + NOTE |

**合计**: ~118 行 md × 3 页 PDF ≈ **原子量 50-80**, 足够冻结 schema + 测到 6/9 原子类型.

**Steps** (3 target 并行, 每 target 独立 agent 组):

1. 派 subagent_type A (`Explore`) 各读 3 份 PDF 页 → 产 `evidence/checkpoints/p0_{T1|T2|T3}_pdf_atoms.jsonl`
2. 派 subagent_type B (另一 explore 型) 各读 3 份 md → 产 `evidence/checkpoints/p0_{T1|T2|T3}_md_atoms.jsonl`
3. 手工 (或小脚本) 建极简索引
4. 派 15–30 个 micro-agent 并行做正向匹配 → 追加到 `p0_ledger.jsonl`
5. 派 15–30 个 micro-agent 并行做反向匹配
6. 派 subagent_type C (`oh-my-claudecode:code-reviewer`) Rule D 独审每 target 抽 10 原子 = **30 原子**
7. 产 `evidence/checkpoints/p0_pilot_report.md` — 含 **9 种原子类型实测覆盖表** / 工具问题登记 / schema 调整记录
8. 用户 review → gate

**Gate** (v0.3 加原子覆盖 + drift 校准, Fix F-5 / F-7):
- 工具链无报错
- **9 种原子类型至少 6 种在 pilot 被实测到且 schema 能容纳**
- schema 可满足实际数据 (如 `FIGURE` 需 L2 拆节点, `LIST_ITEM` 嵌套需 `parent_item_id` 指针等)
- **subagent_type drift 校准**: 3 种 writer type 各跑 T1 同一 10 原子, 一致率 ≥80% 才冻结 schema
- Rule D reviewer CONDITIONAL_PASS 或以上
- 用户 ack "pilot 看起来合理"

**P0 Pilot 附加产物 (v0.4 Fix Gap 8 + verifier Patch C 合并)**:
- `tree_validator.py` 单元测试 **5 case**: (a) 正常 tree (b) OCR typo HEADING (c) orphan child (父 HEADING MISSING) (d) missing parent (跳级) (e) sibling_index 乱序
- FIGURE 原子 P4a 输入截断策略实测 (T2 RELREC figure 作测)
- `_progress.json` `recovery_hint` 字段工程专用模板 (见 §10)
- Appendix D 批量预审批 category 首批条目草案 (供用户一次性 ack)

### 5.2 P1-P7 细化 (Pilot 后再展开)

Pilot 完成后本 PLAN 升 v0.2, P1-P7 各自写独立 sub-plan: `plans/P1_pdf_atomization.md` 等. 这是为了避免一次性规划过细, 实际执行与初计划偏离 (前车之鉴 Issue 3).

---

## 6. 并行 & context-hygiene 细则

### 6.1 任务切片

- **P1**: 535 页 → 535 task; 每 task 1 页 PDF → JSONL 输出
- **P2**: **141 md → 141 task** (v0.3 Fix F-1; 大文件如 ch04 ~1395 行预切 ≤300 行段, 每段 1 task)
- **P4a**: 5000+ PDF 原子 → 5000+ micro-task; 每 task 输入 = 1 原子 verbatim + top-5 md 候选 + **PDF 页号 (仅锚, 不传页文本全文, v0.3 消除 Ambiguity Risk #3)**
- **P5**: 5000+ MD 原子 → 5000+ micro-task
- **批次粒度** (v0.3 Fix F-4): P4a/P5 按 **每 100 原子 = 1 batch**, 每 batch 分配 `(writer_type, reviewer_type)` 对; batch 间 writer_type 循环轮换 (见 §8 roster). trace.jsonl 记 `batch_id`.

### 6.2 单 agent 输入上限

| 任务 | 最大上下文 | 说明 |
|---|---|---|
| P1 原子化 | 1 PDF 页 + schema 说明 | ~5 KB schema + ~2 KB 页文本 |
| P2 原子化 | ≤ 300 行 md + schema | ~15 KB |
| P4/P5 比对 | 1 原子 + 5 候选 + schema | ~3 KB |

**绝对禁止**: 给 agent 2+ PDF 页、10+ md 段、完整 schema 全文.

### 6.3 prompt 模板 & 归档

- 所有 subagent prompt 存 `subagent_prompts/{phase}_{slot}_vN.md`
- prompt 含: 任务定义 / 输入契约 / 输出 JSONL schema / 严格 verdict 规则 / 失败模板
- prompt 变更需 bump version, 旧版本移 `subagent_prompts/archive/`

### 6.4 trace.jsonl 字段

```jsonc
{
  "ts":"...", "phase":"P4", "slot":"forward_match",
  "subagent_type":"Explore",
  "input_atom_id":"ig34_p0425_a012",
  "input_hash":"sha256:...",
  "output_hash":"sha256:...",
  "verdict":"EQUIVALENT",
  "model":"opus|sonnet|haiku",
  "tokens_in":null, "tokens_out":null,
  "status":"ok|failed|retry"
}
```

---

## 7. Rule 合规清单 (A/B/C/D/E)

| Rule | 条款 | 本 PLAN 的落地 |
|---|---|---|
| **A** | 语义抽检强制 (压缩 >50% 或改写 >50% 做 N 样本独审) | 每 phase IR7 ≥30 样本; `audit_matrix.md` 记录 |
| **B** | 失败归档不删 | `evidence/failures/` 存失败 attempt, 含输入/产物/判定/下次输入 |
| **C** | Retro 强制 | P7 `RETROSPECTIVE.md` 三段; 每 phase 小结入 `evidence/checkpoints/` |
| **D** | 审阅隔离 (writer ≠ reviewer, 不同 subagent_type) | 每 phase ≥3 slot, 见 §8 roster |
| **E** | 跨平台 / 跨模态 cross-check | 本工程对 PDF 采用 multimodal Read (视觉 + 文字) + 对 md 用纯文本 Read, 天然双通道 |

---

## 8. Rule D Subagent Slot Roster (候选池)

每 phase 至少 3 种不同 `subagent_type`. 推荐池:

| Slot 角色 | 候选 subagent_type |
|---|---|
| **Writer (原子化)** | `Explore` / `oh-my-claudecode:explore` / `feature-dev:code-explorer` |
| **Reviewer (独审)** | `oh-my-claudecode:code-reviewer` / `oh-my-claudecode:critic` / `pr-review-toolkit:code-reviewer` / `superpowers:requesting-code-review` |
| **Aggregator (合并/triage)** | `oh-my-claudecode:verifier` / `feature-dev:code-reviewer` |
| **Scientist (Rule A 抽样)** | `oh-my-claudecode:scientist` |
| **Tracer (歧义/冲突)** | `oh-my-claudecode:tracer` |
| **Architect (schema 调整)** | `oh-my-claudecode:architect` |
| **Planner (Phase 间协调)** | `oh-my-claudecode:planner` / `Plan` |

**使用规则 (v0.3 batch 粒度化 Fix F-4)**:
- Writer/Reviewer 在 **batch 粒度** (每 100 原子 = 1 batch) 切换, 非 per-atom.
- 每 batch = 1 writer_type + ≥1 reviewer_type; batch 内 writer ≠ reviewer (硬).
- Batch 间 writer_type 循环轮换, 连续两 batch 不得同 type (池 ≥5 种 → 轮换周期 ≥5 batch).
- `trace.jsonl` 必记 `batch_id` + `subagent_type` + `role` (writer/reviewer) 以便事后审 Rule D 链条.

**池扩充 (v0.3 补齐 ≥15 种 Fix F-4)**:
- Writer 池新增: `oh-my-claudecode:document-specialist` (多模态 PDF 读)
- Reviewer 池新增: `oh-my-claudecode:verifier` (从 Aggregator 重分), `superpowers:requesting-code-review`, `pr-review-toolkit:code-reviewer`
- Aggregator 池新增: `feature-dev:code-explorer`
- 专项: `oh-my-claudecode:ai-slop-cleaner` (专治 AI 过度简化, 用于 P6 triage)

**去重盘点表 (v0.4 Fix NF-3, 证实 ≥15 种独立 subagent_type)**:

| # | subagent_type | 角色允许 | 状态 |
|---|---|---|---|
| 1 | `Explore` | Writer | 可用 |
| 2 | `oh-my-claudecode:explore` | Writer | 可用 |
| 3 | `feature-dev:code-explorer` | Writer / Aggregator | 可用 |
| 4 | `oh-my-claudecode:document-specialist` | Writer (多模态 PDF) | 可用 |
| 5 | `oh-my-claudecode:code-reviewer` | Reviewer | 可用 |
| 6 | `oh-my-claudecode:critic` | Reviewer | **已用 v0.2 审** |
| 7 | `oh-my-claudecode:verifier` | Reviewer | **已用 v0.3 审** |
| 8 | `pr-review-toolkit:code-reviewer` | Reviewer | 可用 |
| 9 | `superpowers:code-reviewer` | Reviewer | 可用 |
| 10 | `feature-dev:code-reviewer` | Reviewer / Aggregator | 可用 |
| 11 | `oh-my-claudecode:scientist` | Scientist (Rule A 抽样) | 可用 |
| 12 | `oh-my-claudecode:tracer` | Tracer | 可用 |
| 13 | `oh-my-claudecode:architect` | Architect (schema 调整) | 可用 |
| 14 | `oh-my-claudecode:planner` | Planner | 可用 |
| 15 | `Plan` | Planner | 可用 |
| 16 | `oh-my-claudecode:ai-slop-cleaner` | P6 Triage 专项 | 可用 |

**独立 type 总数 = 16 (≥ 15 目标满足 + 1 备份 buffer)**. 已用 2 / 可用 14.

**累积目标**: 全工程 P0-P7 烧 **≥ 15 种独立 subagent_type** (每 phase ≥3 种; phase 间可复用, phase 内不复用).

**run-time roster 表** (参考 Phase 6.5 retro 28-slot 累计模式, 运行时维护在 `audit_matrix.md`):

| slot # | subagent_type | phase | role | batch_ids | ts |
|---|---|---|---|---|---|
| 1 | `oh-my-claudecode:critic` | P0 Review (v0.2 审) | reviewer | — | 2026-04-24 |
| 2 | (待派: 第二 critic, 换 type) | P0 Review (v0.3 审) | reviewer | — | pending |
| ... | (P0-P7 增量追加) | | | | |

---

## 9. 抽样 & Exit Gate 定量

### 9.1 每 phase Rule A 抽样

| Phase | N 样本 | 抽样单位 | 一致率阈值 |
|---|---|---|---|
| P0 | 3 writer type × T1 同 10 原子 = 30 原子 | verdict + subagent_type drift | ≥80% type 间一致 (v0.3 Fix F-7) |
| P1 | 30 页 | 整页原子集 vs 独立 re-atomize | ≥90% 原子一致 |
| P2 | 30 md 段 | 段原子集 vs 独立 re-atomize | ≥90% |
| P4a | **100 原子 分层 (HEADING/SENTENCE/TABLE_ROW/LIST_ITEM/CODE_LITERAL 各 20)** (v0.3 Fix F-8) | verdict | ≥95% 一致 |
| P4a-drift | **每 300 原子 (3 batch) 抽 10 原子**, 3 writer type 平行判; **每 batch 末额外写 5 原子 `batch_quality_sample` 到 trace.jsonl 作快检** (v0.4 加密 Gap 2) | verdict | ≥80% 一致, 否则暂停 |
| P4b | **30 section (含高风险区 ch04/ch08/ch10 各 ≥10 节)** (v0.3 Fix F-8) | aggregate_verdict | ≥95% 一致 |
| P5 | **100 原子** (v0.3 Fix F-8) | verdict | ≥95% |
| P6 | 全部修复 | 修复前后 verdict diff | 100% 从 MISSING/ERROR/MISPLACED → EXACT/EQUIVALENT |

### 9.2 工程级 Exit Gate (重申 §0.3 + section-level + v0.3 补强)

- PDF 原子覆盖率 ≥ 99% (原子级)
- **0 节标 `SKELETON_ONLY`** 未在 INTENTIONAL_EXCLUDE 白名单
- **0 节标 `SIBLING_DROPPED`** 未登记 Issue (子标题缺失必须开 Issue 5+)
- **0 节标 `STRUCTURE_DRIFTED`** 未修复 (v0.3 Fix F-2)
- `CONTENT_TRUNCATED` 节全部有修复记录 (Issue closed)
- **`MOSTLY_COMPLETE` 节抽样 ≥20%**, 命中 shall/must 关键词丢失者升级 Issue (v0.3 Fix F-3)
- 用户人工抽 **≥100 原子 (分层)** + **≥30 section 聚合 (含高风险区)** 误判率 <5% (v0.3 Fix F-8)
- Rule D reviewer 独立 PASS

### 9.3 Hard Stop 条件 (任一触发 → 暂停工程, 升 PLAN 版本)

- 某 phase Rule A 一致率 <80% → 工具 / schema / prompt 有系统问题
- subagent 失败率 >15% → 需改 prompt 或切 subagent_type
- `trace.jsonl` 出现 1 次 "写入脏数据" (不合 schema) → 立即 halt, 人工 review
- **用户阶段性抽检连续两 phase 误判率 >5%** → halt, 重评阈值 (v0.3 Fix F-9)
- **P4a/P5 任一 phase 连续 2 session 完成率 <5%** (卡死信号) → halt (v0.3 Fix F-9)
- **trace.jsonl 连续 ≥3 条写入失败** → halt, 审 trace pipeline (v0.3 Fix F-9)
- **subagent_type drift >20%** (P4a-drift 抽样) → halt, 调 prompt (v0.3 Fix F-7)

---

## 10. 目录 & 产物

```
.work/06_deep_verification/
├── PLAN.md                            ← 本文件
├── _progress.json                     ← 程序化进度
├── schema/
│   ├── atom_schema.json               (P0 冻结)
│   └── ledger_schema.json             (P0 冻结)
├── plans/                             (P1-P7 sub-plan, P0 后产)
│   ├── P1_pdf_atomization.md
│   ├── P2_md_atomization.md
│   └── ...
├── evidence/
│   ├── checkpoints/                   (每 phase 产出快照)
│   │   ├── p0_pilot_report.md
│   │   ├── p1_summary.md
│   │   └── ...
│   └── failures/                      (Rule B 归档)
│       └── {phase}_attempt_{N}.md
├── pdf_atoms.jsonl                    ← P1 产物 (增量)
├── md_atoms.jsonl                     ← P2 产物
├── coverage_ledger.jsonl              ← P4+P5 产物
├── discrepancies.md                   ← P6 triage
├── subagent_prompts/
│   ├── P0_writer_v1.md
│   ├── P0_reviewer_v1.md
│   └── archive/
├── trace.jsonl                        ← 全 subagent trace
├── audit_matrix.md                    ← Rule A 每 phase 抽检矩阵
└── RETROSPECTIVE.md                   ← P7 终态
```

**`_progress.json` 必备 schema 片段 (v0.4 Fix NF-1, Tier 3 template §5 强制)**:

```jsonc
{
  "project": "06_deep_verification",
  "tier": 3,
  "plan_version": "v0.4-DRAFT",
  "status": "planning|P0|P1|...|completed|halted",
  "current_phase": "...",
  "recovery_hint": "下一步恢复: (1) 读 PLAN.md §0 Charter + 本文件 current_phase; (2) 检查 evidence/checkpoints/ 最新产物; (3) 查 trace.jsonl 尾行 ts & status; (4) 若 status=halted 看 failures/ 最新 attempt; (5) Rule D roster 已烧 slot 见 rule_d_slot_roster_used",
  "last_checkpoint": "evidence/checkpoints/...",
  "last_trace_entry_ts": "...",
  "charter_gates": { "pdf_atom_coverage_pct": null, "user_sample_error_rate": null, "rule_d_reviewer_pass": false },
  "phases": { "P0_pilot": {...}, "P1_pdf_atomization": {...}, ... },
  "open_items": [...],
  "rule_d_slot_roster_used": ["oh-my-claudecode:critic", "oh-my-claudecode:verifier"],
  "trace_entries": 0
}
```

---

## 11. 风险登记

| # | 风险 | 影响 | 缓解 |
|---|---|---|---|
| R1 | PDF OCR / 多列排版导致原子分错 | P1 原子质量 | Rule A 30 页抽检 + 失败归档重跑 |
| R2 | 图像原子无法精确 verbatim | FIGURE 原子匹配困难 | Mermaid 节点 + 标签作子原子 + 独立 reviewer 视觉复核 |
| R3 | md 改写率高导致 EQUIVALENT 多于 EXACT, 抽检成本大 | P4 | EQUIVALENT 也要 diff 原文; Rule A 必查抽样 |
| R4 | subagent cost 爆表 (5000+ 调用) | 预算/时间 | 用户已接受; micro-agent 模式本身 token 少, 实际成本可控 |
| R5 | PDF 页码与 physical page 有偏移 (Issue 1 先例) | 溯源错锚 | 原子化 agent 必须返回 "页顶首句 verbatim" 作锚, 脚本校验 |
| R6 | schema 需求在 P1 中期才发现改动 | 返工 | P0 Pilot 专为此 — pilot 后冻结 schema; 若 P1 中途要改需 bump version 并回填 |
| R7 | 用户抽检反馈慢 → 项目拖慢 | 时间 | 每 phase gate 强制 ≥1 周期用户 review; 允许 async |
| R8 | 修复引入新错误 | 回归 | P6 修复必经 writer/reviewer 分离 + 修复前后 verdict diff 入 ledger |
| R9 | **section tree parse 失败** (HEADING 原子 typo/OCR 错 → P4b 树 build silent broken) (v0.3 Fix F-6) | SIBLING_DROPPED 聚合失效 | P1 agent 对 HEADING 原子额外填 `heading_level` + `sibling_index`; P4b 前过 `tree_validator.py` 校验 ∀ parent 有 ≥1 child 或明示 leaf |
| R10 | **subagent_type verdict drift** (同 prompt 不同 type 判据不一致) (v0.3 Fix F-7) | ledger 不一致 | P0 校准 ≥80% 才冻; P4a 每 1000 原子抽 30 原子三型平行判; drift >20% halt |
| R11 | **md 修复后行号大量偏移, md_atoms.jsonl 失效** (v0.3 回归盲区) | ledger 失效 | P6 修复后受影响文件重跑 md 原子化; 影响 >30% 触发 full rebuild |
| R12 | **tree_validator.py 本身失效** (v0.4 Fix Gap 8, R9 唯一防线的 meta-risk) | SIBLING_DROPPED 检测静默失败 | P0 Pilot 产物含 5 case 单元测试; P4b 启动前脚本必过 self-test |
| R13 | **run-time roster 维护断层** (v0.4 Fix verifier Gap, 操作者忘记在 trace 写 subagent_type) | Rule D 链条事后无法验证 | trace.jsonl schema 增强: `subagent_type` 字段 NOT NULL, 写入 validator 拒绝空值 |
| R14 | **白名单审批绕过** (v0.4 Fix verifier Gap, reviewer agent 偷偷自批) | INTENTIONAL_EXCLUDE 滥用 | 白名单条目必有 `approved_by: user` (非 agent); 定期 grep `approved_by: agent` 零容忍; 预批 category 仅限 VERSION_MISMATCH + EDITORIAL_META 白名单 |

---

## 12. 当前 Open Items

| # | Item | Owner | 状态 |
|---|---|---|---|
| O1 | 本 PLAN 过 Rule D 独立 reviewer (不同 subagent_type, 建议 `oh-my-claudecode:critic`) | 主 session | 待派发 |
| O2 | 用户 review PLAN v0.1 | Daisy | 待 |
| O3 | P0 Pilot 启动 | 待 O1+O2 PASS | blocked |
| O4 | `schema/atom_schema.json` 最终版 | P0 | P0 产物 |
| O5 | `subagent_prompts/P0_writer_v1.md` | P0 启动前 | 待 |

---

## 13. Changelog

| Version | Date | Change |
|---|---|---|
| v0.1 | 2026-04-24 | Initial DRAFT, 8 决策点已过用户预审 |
| v0.2 | 2026-04-24 | 用户 v0.1 review 反馈折合: (1) drop `VARIABLE_FIELD` (逐字过细, 用户关注的是 "逐行"); (2) 新增 §3.1 + §4.5 + P4b + §9.2 **section-level 聚合** 抓三类失效 (CONTENT_TRUNCATED / SKELETON_ONLY / SIBLING_DROPPED); (3) P4 拆成 P4a (原子匹配) + P4b (section 聚合); (4) 每 phase Rule A 样本加 P4b 30 section 一行 |
| v0.3 | 2026-04-24 | Rule D critic v0.2 review CONDITIONAL_PASS 78/100 的 **5 blocking 全 fix**: F-1 数字盘点实测 (136→141 + top-level 3 纳入 + 38 行纠正 + 295 全覆盖自检); F-2 加 `MISPLACED` verdict + `STRUCTURE_DRIFTED` aggregate (吸收 Issue 4 §8.4.4 教训); F-3 aggregate 优先级表 + MOSTLY_COMPLETE shall/must 关键词升级 + child_sections 四值化; F-4 Rule D **per-batch 100 原子** 粒度 + 池扩 ≥15 种 + run-time roster 表; F-5 P0 Pilot **扩 3 target** 覆盖 ≥6 种原子. **Non-blocking 吸收**: F-6 section tree 校验 R9 + P1 HEADING 加 heading_level/sibling_index; F-7 subagent drift R10 + P0 校准 + P4a-drift 抽样; F-8 抽样 50→100 原子 + 20→30 section 高风险分层; F-9 Hard Stop 追 4 条; F-11 文末版本号. **Gap 补**: MISPLACED 自动开 Issue (Appendix C); INTENTIONAL_EXCLUDE 白名单文件 (Appendix D); Rule D run-time roster 模板. **Ambiguity 消**: P4a 输入 "PDF 仅锚非全文"; IR3 "3 slot" 角色 vs type 明示 |
| v0.4 | 2026-04-24 | 第二 Rule D verifier v0.3 review CONDITIONAL_PASS 88/100 全 findings 吸收: **NF-1** `_progress.json` schema 片段 + `recovery_hint` 字段 (§10); **NF-2** 关键词**分 Level 1/2** (Level 1 强制降级: shall/shall not/must/MUST/must not/required/is required/are required/is not permitted/is prohibited/not permitted/may not; Level 2 标记抽检: should/only/except/no longer/cannot/not allowed); **NF-3** §8 **去重盘点 16 种独立 subagent_type 表** (≥15 目标满足); **Gap 1** MISPLACED ↔ STRUCTURE_DRIFTED 去重 (原子层 tracking comment / 聚合层父 Issue / <10% 但 ≥3 MISPLACED 独立 MEDIUM 汇总); **Gap 2 (HIGH)** P4a-drift 间隔 **1000→300 原子** + 每 batch 末 `batch_quality_sample` 5 原子快检; **Gap 3** FIGURE 原子 P4a 输入截断 (verbatim 前 200 字符 + figure_ref 锚, 全量 Mermaid 仅驻 ledger); **Gap 6** Appendix D 批量预审批 category (VERSION_MISMATCH + EDITORIAL_META 一次批 / REDUNDANT_WITH_SPEC + FIGURE_ALREADY_CONVERTED 逐条); **Gap 7** 每 phase 末写 `phase_report` 到 trace.jsonl; **Gap 8** P0 Pilot 附加产物 (validator 5 case 测试 + FIGURE 输入截断实测 + recovery_hint 模板 + 预审批 category 首批草案); 新增 **R12/R13/R14** (tree_validator 失效 / roster 断层 / 白名单绕过). **Rule D 链饱和**: slot #1 critic + slot #2 verifier, 不派第三 reviewer |
| **v0.5** | **2026-04-24** | **P0 Pilot 收官 + T2b FIGURE 补测吸收**: (1) **P0 Pilot ✅ PASS** (3 target T1/T2/T3 + T2b figure 补测, 9/9 atom_type 覆盖, 257 atoms + 229 ledger entries, 2 reviewer PASS 85%+81.25%); (2) **v1.2 schema frozen** (`schema/atom_schema.json` + `schema/ledger_schema.json` JSON Schema 2020-12, forward 8+1 verdict + reverse 5 verdict); (3) **v1.2 6 硬 gate 实战 PASS** (H1' dataset CODE_LITERAL / H2' reverse forward-aware / N1 9-enum / N2 reverse ≥0.50 / N3 heading Jaccard ≥0.85 / FIGURE schema 容纳); (4) **新 verdict 正式成文** (`EDITORIAL_CORRECTION` forward M1' PDF typo 场景 + `TABLE_SIMPLIFIED` formalized + `EDITORIAL_ADDITION` reverse md 元数据); (5) **运维硬约束**: writer/matcher 全用 `oh-my-claudecode:executor`/`writer` 家族 + Write tool 直写, 禁 `Explore` 家族 (20%+ 丢 JSONL drift, 证据 `evidence/failures/v1.1_attempt_pdf_writer_Explore.md`); (6) **Rule D roster 烧 11/16**, 余 5 (superpowers:code-reviewer / scientist / tracer / architect / ai-slop-cleaner, 另 planner/Plan); (7) **新 findings**: F-T1-5 (PDF AP 表 12→5 列) + M2' (CM examples CMDOSE 19→100 数据错) 证明原子级字面审方法论 work, 是 Step 0-4 Phase 审没审出来的; F-T2b-1 LOW (MD 用 bold 表 figure caption 而非 heading, P1 抽样统计后决定 v1.3 补规则); (8) **P1 sub-plan 就绪**: `plans/P1_pdf_atomization.md` v0.1 DRAFT, 535 页 ÷ ~55 batch, batch=100 原子, 每 3 batch drift 校准, 每 30 页 Rule A 30 原子独审 ≥90% gate |

---

## Appendix A. 与 `.work/03_verification/` 的隔离协议

- **不修改** `.work/03_verification/` 下任何文件
- 本工程发现的 KB 问题 → 新开 `Issue 5` (或 6/7...) 登记到 `.work/03_verification/issues_found.md` 的 **继续编号**
- 修复时 Chain B (work log → progress.json → docs/PROGRESS.md) 照常触发
- 旧账本 `step1-4_*.md` 保持 frozen 作历史层

## Appendix B. PDF 读取工具约定

- 首选 Read tool `pages` 参数, **每次 ≤ 1 页** (IR1)
- 若页内容过密 (>50 行), 切分为上/下半页处理, `verbatim` 字段含该半页首末 5 字符作锚
- Read 获得 multimodal 返回 (文字 + 视觉): 视觉只用于 FIGURE 原子或排版判定, 不作文字 verbatim 来源 (避免 OCR 引入差异)
- **FIGURE 原子 `verbatim` 字段填充约定 (v0.3 补 gap)**: 若图已有 Mermaid 源 (`knowledge_base/` 已转化) → 填 Mermaid 源码; 否则填 `[FIGURE: 简述节点 + 边, 视觉判读]`; 永不填 OCR 结果. `figure_ref` 字段额外填 `pdf_page + 视觉区域` 作锚.
- **FIGURE 原子 P4a 匹配输入策略 (v0.4 Fix Gap 3, 防 Mermaid 源码打爆 IR1)**: P4a micro-agent 匹配 FIGURE 原子时 **不**传入全量 `verbatim` (Mermaid 可达 400+ 行). 输入改为: (a) `verbatim` 前 200 字符作语义指纹 + (b) `figure_ref` (pdf_page + 区域) 作锚 + (c) md 候选 top-5 figure 段同样前 200 字符截断. 全量 Mermaid 仅驻 ledger, 不进 context. 若 reviewer 需全量对比, 单独派一次 `oh-my-claudecode:document-specialist` 专项比对 (L2 深审, 非常规 P4a 流程).

---

## Appendix C. Issue 回流流程 (v0.3 补 gap)

本工程发现的 KB 问题走 Issue 5+, 回流到 `.work/03_verification/issues_found.md`. 自动开 Issue 触发表:

| 触发 verdict | 自动开 Issue | Issue 默认严重度 |
|---|---|---|
| `MISSING` (非 INTENTIONAL_EXCLUDE) | YES | HIGH |
| `ERROR` | YES | HIGH |
| `MISPLACED` | YES | MEDIUM |
| `PARTIAL` | 批量聚合, 每节一条 | MEDIUM |
| aggregate `SKELETON_ONLY` | YES | HIGH |
| aggregate `SIBLING_DROPPED` | YES | HIGH |
| aggregate `STRUCTURE_DRIFTED` | YES | HIGH |
| aggregate `CONTENT_TRUNCATED` | YES | MEDIUM |
| `MOSTLY_COMPLETE` 命中 shall/must 关键词 | YES (强制降级) | MEDIUM |
| 反向 `HALLUCINATED` | YES | HIGH |
| 反向 `UNSOURCED` (非 SYNTHESIZED) | 抽查决定 | LOW-MEDIUM |

**MISPLACED ↔ STRUCTURE_DRIFTED 去重规则 (v0.4 Fix Gap 1, 防 Issue 追踪器污染)**:

- **原子层 `MISPLACED`**: **不**开独立 Issue; 仅作 `tracking_comment` 写入 `coverage_ledger.jsonl` 的 `discrepancy` 字段 + 在 `discrepancies.md` 聚合表登记
- **聚合层 `STRUCTURE_DRIFTED`**: 开 1 条**父 Issue** (HIGH), body 引用该节下所有 MISPLACED 原子 id 清单 (同 Issue 4 §8.4.1/8.4.4 父子模式)
- **例外**: 某节 MISPLACED 率 <10% 未触发 STRUCTURE_DRIFTED 但含 ≥3 个 MISPLACED 原子 → 开 1 条 MEDIUM 独立汇总 Issue (非父子)

**Issue 模板** (沿用 Issue 1-4 既有风格):
- Issue NN: [一句话标题]
- 发现方式: phase + ledger_entry_id + subagent_type
- 问题描述 + 证据 (引用 `pdf_atom_id` / `md_atom_id` verbatim)
- 根因分析
- 修复计划 (Issue 5+ 共用 writer/reviewer 分离模板)

回流后 Chain B (work log → progress.json → docs/PROGRESS.md) 照常触发.

## Appendix D. INTENTIONAL_EXCLUDE 白名单机制 (v0.3 补 gap)

**文件**: `.work/06_deep_verification/intentional_exclude_whitelist.md` (工程启动时为空)

**字段**: `pdf_atom_id | exclusion_reason | category | approved_by | ts`

**常见 category**:
- `VERSION_MISMATCH` (SDTM v2.0 内容被 SDTMIG v3.4 取代)
- `REDUNDANT_WITH_SPEC` (PDF 正文与 xlsx spec 重复)
- `EDITORIAL_META` (封面/目录/致谢)
- `FIGURE_ALREADY_CONVERTED` (Mermaid 已存其他位置)

**审批流 (v0.4 分层, Fix Gap 6 防逐条 ack bottleneck)**:

**批量预审批 category** (工程启动时用户一次性批):
- `VERSION_MISMATCH` (SDTM v2.0 内容被 SDTMIG v3.4 取代) — 预计 ≥20 条
- `EDITORIAL_META` (封面/目录/致谢/版本说明页) — 预计 ≥15 条

**逐条审批 category** (每条需用户 ack):
- `REDUNDANT_WITH_SPEC` (PDF 正文与 xlsx spec 重复)
- `FIGURE_ALREADY_CONVERTED` (Mermaid 已存其他位置)

**通用规则**:
- 任何 `INTENTIONAL_EXCLUDE` verdict **必须对应本文件一条记录** (自动生成 + 批量预批或用户逐条 ack)
- reviewer agent **不得自批**, 除非 category 已预批
- 白名单条目加入前过一遍 Rule D 独立审查 (不同 subagent_type)
- 预批 category 的批准在 `intentional_exclude_whitelist.md` 头部登记 (日期 + 用户 ack + reviewer)

---

END of DRAFT v0.4
