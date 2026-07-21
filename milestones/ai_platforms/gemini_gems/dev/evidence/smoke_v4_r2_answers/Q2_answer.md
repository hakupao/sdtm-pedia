# Gemini Gems — Q2 CP 域 CD4+ T ACTIVATED (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/882fe0ff57990046
> **题类**: Q2 (A2 v3.4 新域 CP)
> **R1 baseline**: PASS

## Raw 回答 (DOM 原文)

**域**: **CP (Cell Phenotype Findings)** ✓

- (a) **Topic**: CPTESTCD / CPTEST (Core: Req)
- (b) **命名群**: CPTEST="T Lym Help"; **子集**: CPTEST 加 "Sub" 后缀 (T Lym Help Sub) + **CPSBMRKS** (Sublineage Marker String, Perm) 存 marker 组合 "CD4+Ki67+"
- (c) **CPCELSTA** (Cell State, Perm) = "ACTIVATED" (CT **C181172**); **CPCSMRKS** (Cell State Marker String, Perm) = "Ki67+" 定义 activation
- (d) **CPMETHOD** (Perm) = "FLOW CYTOMETRY" (CT **C85492**)
- (e) LB = 传统生化/血液学/尿分析/CBC (无活性化学/电解质/全血); CP = 活细胞表型 via marker 定义. 原则: 多 marker 定义复杂亚群/功能状态 → CP 优先.

**源路径**: knowledge_base/domains/CP/spec.md §CPTEST/CPSBMRKS/CPCELSTA/CPCSMRKS + CP/assumptions.md + NCI EVS Browser (C181172/C85492 外链合规)

## Self-score verdict

**PASS+** — 核心 5 子问 (abcde) 全对 + 域 ✓ + 双 CT code ✓ (C181172 + C85492) + Sub 后缀 ✓ + CPSBMRKS vs CPCELSTA vs CPCSMRKS 三变量精确区分 (R1 pitfall 避开) + NCI EVS 外链合规 (CO-2 遵守).

**R1 vs R2**: 对齐 PASS/PASS+. v6 CO-4 CP 段保留 R1 效果, 无 regression.
