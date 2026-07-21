# P7 人工抽样报告

> 日期: 2026-05-12
> 阶段: P7_human_sampling
> 抽样工作表: `evidence/checkpoints/p7_sample_sheet.md` (seed=20260512)

---

## 1. 抽样结果

| 指标 | 值 |
|------|-----|
| 总抽样量 | 60 原子 |
| 分层方式 | 按 verdict 分层 (EXACT/EQUIV/PARTIAL/MISPLACED/ERROR/IE/MISSING) |
| 用户判定 CORRECT | 27 / 60 (45.0%) |
| 用户判定 WRONG | 33 / 60 (55.0%) |

---

## 2. Option C 重分析：内容问题 vs 标签问题

P7 Gate 定义为「KB 内容误判率 <5%」（Option C 重新定义，经用户 2026-05-12 ack）。

对 33 个 WRONG 逐一分析：

| 分类 | 数量 | 说明 |
|------|------|------|
| 标签问题 (LABEL) | 31 | verdict 类别不够精确，但 KB 内容本身正确或不需覆盖 |
| 内容问题 (CONTENT) | 2 | KB 确实缺失相关内容 |

**内容误判率: 2/60 = 3.3% → Gate P7-G1 PASS ✅**

---

## 3. LABEL 问题主要模式

| 模式 | 案例数 | 说明 |
|------|--------|------|
| 变量规格表行应为 IE (REDUNDANT_WITH_SPEC) | 12 | P4a 对规格表行 IE 分类不彻底，改打成 PARTIAL/EQUIV/ERROR |
| 同例表不同行 (同表内容匹配精度不足) | 6 | 匹配到相同 example 表但行序号/数据不同 |
| 完全错误 KB 匹配 | 5 | P4a 低相似度匹配到语义无关内容 |
| EXACT/EQUIV/PARTIAL 边界 (格式差异) | 4 | 列表编号、markdown 格式、截断显示 |
| 其他边界 (MISPLACED 误用、sv20 VERSION_MISMATCH) | 4 | — |

---

## 4. CONTENT 问题详情 (2 条)

| # | Atom ID | 说明 |
|---|---------|------|
| #28 | ig34_p0278_a040 | §6.3.5.9.3 PP RELREC linking 例 (PPSEQ=6, USUBJID=ABC-123-0001) 未入 KB PP examples |
| #30 | ig34_p0278_a035 | §6.3.5.9.3 同上 (PPSEQ=1) |

两条均来自同一小节同一例子，属同一内容缺口。已登记为 follow-up (OA-4)。

---

## 5. Gate 结论

| Gate | 判定 | 依据 |
|------|------|------|
| P7-G1 内容误判率 <5% | ✅ PASS | 2/60 = 3.3% |
| P7-G2 RETROSPECTIVE.md | ⬜ 待完成 | 见 RETROSPECTIVE.md |
| P7-G3 Rule D reviewer | ⬜ 待完成 | 独立 critic 审阅 |

---

## 6. 用户 ack

- 2026-05-12: 用户完成 60 原子人工复检
- 2026-05-12: 用户选择 Option C (KB 内容误判率)作为 P7-G1 判定标准
