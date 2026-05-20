# A2 — BECAT EXTRACTION prompt-KB 分叉修复 (D3)

> Date: 2026-05-20
> Phase: A — KB layer fixes
> Step: A2
> Predecessor: v1.2 KNOWN_LIMITATIONS.en §0 D3 (BECAT EXTRACTION prompt-KB 分叉)
> Decision: α (改 KB, default per PLAN.md § 5 决策点 1)
> Status: PASS (KB layer); 4-platform uploads grep deferred to Phase B

---

## 1. Carry 来源

v1.2 `KNOWN_LIMITATIONS.en` §0 (2026-05-19) 第 3 项 deferred:

> **BECAT EXTRACTION KB-prompt note** — v8.1 prompt L272 lists `"EXTRACTION"` among BECAT examples; KB BE / spec L111 only inlines three canonical examples (`COLLECTION`, `PREPARATION`, `TRANSPORT`). The deployed response correctly annotates it as sponsor-extensible, but a future prompt revision may add an explicit source citation to avoid prompt-KB drift.

## 2. 三方案对比 (PLAN.md A2 决策)

| 方案 | 改动 | 影响范围 | 工程量 | 风险 |
|---|---|---|:-:|---|
| **α (改 KB, 默认)** | BE/spec.md L111 加 EXTRACTION 作为 sponsor-extensible 第 4 例, 注明非 CDISC canonical | BE 单文件 + 1 句 | 极小 | 引入 KB 内有"非 PDF 来源"的 sponsor-extensible 说明 — 但已 explicit 标注, 不算 hallucination |
| β (改 prompt) | Gemini v8.2 patch L272 加 sponsor-extensible 注 | Gemini system_prompt 改 + 触发 dry-run + Rule D + re-promote | 中 (1 cycle) | 全平台中只 Gemini 一个有 EXTRACTION 引用, 不动其他 3 平台 |
| γ (双向标注) | KB 加 + prompt 加 KB-source 引用 | 双文件改 | 大 | 工程量大, 推迟 v1.4 |

**决策**: α — 理由:
1. PLAN.md § 5 决策点 1 默认 α
2. 工程量极小, 单文件 1 句变更
3. EXTRACTION 作为 sponsor-extensible 是行业事实 (DNA / 分子生物学 specimen processing 常用); KB 加 explicit 标注比绝对静默更有信息价值
4. KB 改后, 4 平台 rebuild (Phase B) 时所有 platform uploads 都会自动同步, 不需要单独动 Gemini prompt
5. 不引入"非 PDF 来源"的隐性内容 (新加文字明示"sponsor-extensible", "additional category values such as EXTRACTION...", 不是冒充 CDISC canonical)

## 3. 修复 (BE/spec.md L111)

### 3.1 改前 (1 行, L111)

```
- **CDISC Notes:** Used to define a category of topic-variable values. Example: COLLECTION, PREPARATION, TRANSPORT.
```

### 3.2 改后 (1 行, L111, 加长)

```
- **CDISC Notes:** Used to define a category of topic-variable values. Example: COLLECTION, PREPARATION, TRANSPORT (CDISC canonical examples per SDTMIG v3.4). BECAT is sponsor-extensible; additional category values such as EXTRACTION (e.g., for DNA / molecular-biology specimen processing) are routinely used in practice, provided they follow the same single-token, controlled-vocabulary convention.
```

### 3.3 改动分析

| 段 | 来源 | 验证 |
|---|---|---|
| `Used to define a category of topic-variable values. Example: COLLECTION, PREPARATION, TRANSPORT` | PDF p162 BE spec table (CDISC canonical, 未动) | byte-exact preserved |
| `(CDISC canonical examples per SDTMIG v3.4)` | 新加, 明确 3 例的来源标签 (PDF v3.4) | non-source 但合规标注 |
| `BECAT is sponsor-extensible` | 反映 CDISC 通用 BECAT pattern (--CAT 类变量惯例) | 行业惯例事实, 与 PDF 不矛盾 |
| `EXTRACTION (e.g., for DNA / molecular-biology specimen processing)` | sponsor-extensible 第 4 例, 与 Gemini v8.1 prompt L272 对齐 | 标 sponsor-extensible 非 CDISC canonical |
| `provided they follow the same single-token, controlled-vocabulary convention` | 反映 --CAT 类变量惯例 | 不引入新规则 |

## 4. Rule A 抽检 (Phase A 部分)

| # | Probe | Pre-fix | Post-fix | Verdict |
|:-:|---|---|---|:-:|
| A2.1 | grep `BECAT` in BE/spec.md | L111 single line, 3 canonical 例 | L111 single line, 3 canonical + 1 sponsor-extensible (EXTRACTION) + role label | ✅ KB updated |
| A2.2 | PDF p162 verbatim "COLLECTION, PREPARATION, TRANSPORT" still preserved | ✓ | ✓ (前半段未动) | ✅ no hallucination |
| A2.3 | grep `EXTRACTION` in BE/spec.md | 0 hit | 1 hit (L111) | ✅ added |
| A2.4 | Gemini v8.1 system_prompt L272 BECAT 段不需动 | "COLLECTION / PREPARATION / TRANSPORT / EXTRACTION" | (未动, 现 KB align 一致) | ✅ no drift |
| A2.5 (Phase B 后) | grep `EXTRACTION` in 4 平台 uploads | Pending Phase B rebuild | TBD | ⏳ deferred |
| A2.6 (Phase B 后) | grep `EXTRACTION` in chatgpt 05_assumptions / gemini 02_specs / claude mega_spec / notebooklm bucket | Pending Phase B rebuild | TBD | ⏳ deferred |

**Phase A 部分 (A2.1-A2.4): 4/4 PASS**.
Phase B 部分 (A2.5-A2.6): 2 probes pending — 计入 PLAN.md § 3 Rule A 表 A2 行 4 probes.

## 5. Carry status post-fix

- v1.2 KNOWN_LIMITATIONS §0 D3 (BECAT EXTRACTION 分叉): **RESOLVED at KB layer** ★
  - Phase B rebuild 后 4 平台 uploads 自动同步 → 全栈一致
  - Phase D KNOWN_LIMITATIONS §0 reconcile 时移出 D3 deferred
- Gemini v8.1 prompt: 不动, 当前 L272 "EXTRACTION" 引用现 KB-grounded

## 6. 下一步

- A3 — Tier B shall/must 高密度节修复 (D5/G3)
- 先扫 section_coverage.jsonl, 过滤 SIBLING_DROPPED + CONTENT_TRUNCATED, 统计 shall/must/required 关键词 ≥3 的节排序
