# P0 Pilot T1 v1.1 Regression — 收官摘要

> 日期: 2026-04-24
> 范围: T1 only (SDTM_v2.0.pdf p.50 × model/04_associated_persons.md 38 行)
> **Gate verdict**: ✅ **PASS (Rule D 85% > 80% 门槛, 8/8 v1.1 fix 全部 PASS)**

---

## v1 vs v1.1 对比

| 指标 | v1 | v1.1 | Δ |
|---|---|---|---|
| PDF atoms | 17 | 21 | +4 (M1 + M2) |
| MD atoms | 25 | 21 | -4 (TABLE_HEADER 合并 -1 + PARAGRAPH 合并 -3) |
| Forward EXACT | 4 | 0 | -4 (v1.1 EQUIVALENT 阈值更严, N4 接受) |
| Forward EQUIVALENT | 4 | 12 | +8 |
| Forward PARTIAL | 8 | 1 | -7 (M3 阈值; 4 移到 TABLE_SIMPLIFIED) |
| Forward MISSING | 1 | 4 | +3 (M3 降级, 更严) |
| Forward TABLE_SIMPLIFIED | (不存在) | 4 | 新 verdict |
| Reverse SOURCED | 18 | 16 | -2 |
| Reverse SYNTHESIZED | 6 | 3 | -3 (细分到 EDITORIAL_ADDITION) |
| Reverse EDITORIAL_ADDITION | (不存在) | 1 | 新 verdict |
| Rule D accuracy | 70% FAIL | **85% PASS** | +15pp |

---

## Fix 验证结果

| ID | 描述 | 验证 |
|---|---|---|
| H1 | matcher discrepancy 禁外部知识 | ✅ C55361 消失 |
| H2 | 正反向 ledger 一致 | ✅ (soft, N2 留下 follow-up) |
| H3 | KEYWORD 字面化 | ✅ 0 个误标 |
| M1 | PDF writer 抽表前 caption HEADING | ✅ a014 新增 |
| M2 | PDF writer 段落全句 | ✅ a011/a012/a013 补齐 |
| M3 | PARTIAL ≥0.50 硬 gate | ✅ 0 个违反 |
| TABLE_SIMPLIFIED | 新 verdict | ✅ 4 正确应用 |
| EDITORIAL_ADDITION | 新 verdict | ✅ 1 正确应用 |

---

## 新暴露 findings (N1-N4, defer v1.2)

- **N1 MEDIUM**: MD writer 造非枚举 `PARAGRAPH` × 3 处. Fix v1.2: enum validator + 硬拒.
- **N2 MEDIUM**: Reverse similarity 过宽. Fix v1.2: ≥0.50 语义 gate.
- **N3 LOW**: Heading EQUIVALENT 阈值过宽. Fix v1.2: ≥0.85 Jaccard.
- **N4 LOW**: EXACT 0/21 — 接受 EXACT 在此项目天然稀缺 (PDF vs markdown fence).

---

## Rule D roster 累计 (10/16)

1. `oh-my-claudecode:critic` (PLAN v0.2 审)
2. `oh-my-claudecode:verifier` (PLAN v0.3 审)
3. `Explore` (v1 PDF writer — v1.1 尝试失败)
4. `oh-my-claudecode:explore` (v1 + v1.1 MD writer)
5. `feature-dev:code-explorer` (v1 forward matcher)
6. `oh-my-claudecode:document-specialist` (v1 reverse matcher)
7. `oh-my-claudecode:code-reviewer` (v1 reviewer)
8. `oh-my-claudecode:executor` (v1.1 PDF writer + forward matcher)
9. `oh-my-claudecode:writer` (v1.1 reverse matcher)
10. `pr-review-toolkit:code-reviewer` (v1.1 reviewer)

池余 6 可用: superpowers:code-reviewer / feature-dev:code-reviewer / oh-my-claudecode:scientist / tracer / architect / planner / Plan / ai-slop-cleaner.

---

## Agent 行为观察 (跨 v1 + v1.1)

**失败模式**: Explore 家族 agent ("search specialist") 习惯性返回自然语言摘要, 忽略 "纯 JSONL 无 natural language" 指令. 即便 prompt 明言也不守.

**成功模式**: Executor / Writer 家族 (action-oriented) + Write tool 直写文件, 最终只回 "DONE" — 彻底绕过"叙述默认".

**P1 策略建议**: 对原子化 (writer) + 匹配 (matcher) 任务, **全部用 executor/writer 家族 + Write tool 直写**, 不要求最终消息包含数据. reviewer 任务可继续用 markdown 返回 (reviewer 本来就需要产报告).

**这是 P1 scale (535 pages × 20 agents / batch) 的关键运维 insight** — 否则 100+ 次 Explore 派发会有 >20% 纯叙述响应 lost 数据.

---

## P0 Pilot 整体结论

**T1 v1.1 ✅ PASS**. 方法论验证 + 7 subagent_type Rule D 链 + v1.1 prompt 升级 + 10 个 finding 全闭环.

下一步 (待用户):
- **路线 α (推荐)**: 扩 T2 (ch08 §8.2 × SDTMIG v3.4 p.428) + T3 (AE assumptions × p.137), 测 FIGURE/CROSS_REF/CODE_LITERAL/NOTE 4 种剩余原子类型. 约 20-30 min (writer×2 + matcher×2 = 4 agents × 2 target)
- **路线 β**: 接受 T1 PASS 作 schema 冻结证据, 直接进 P1 (PDF 535 页全量原子化). 高风险 — 原子类型未全测
- **路线 γ**: 今天到此, 明天推 T2+T3
