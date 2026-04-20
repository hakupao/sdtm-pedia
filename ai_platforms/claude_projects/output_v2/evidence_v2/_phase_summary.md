# Phase 6.5 Claude v2 — 全程总结 (_phase_summary)

> 本文件由 Phase H Task H4 生成, 作为 Phase 6.5 v2 的完结签收档案.

---

## 0. 一句话总结

Phase 6.5 Claude v2 从 2026-04-18 启动到 2026-04-20 终态 v2.6 完成, 6 批渐进 + 1 重平衡批, 19 真实上传文件 / 1,286,161 tokens / capacity 77% / 24/24 A/B PASS / 0 衰减, 长尾 302 codelist 归 Phase 7.

## 1. 时间线

| 日期 | 里程碑 | 主要产出 |
|------|-------|---------|
| 2026-04-18 | Phase 6.5 v2 启动 (v1 扩容决策) | v2 design spec + PLAN_V2.md 1852 行 + A1-A3 setup (baseline archive + scripts_v2 骨架) + B1-B4 基础 tooling (count_tokens 复用 + score_domains + score_codelists + build_v2_stage executor) |
| 2026-04-19 白天 | C1-C3 v2.1 chapters 全展开 | 02_chapters.md byte-exact expand, stage v2.1 build (205,895 tokens, capacity 13%), T1-T8 5↑/2 持平/1↓ (T3 边界), T9-T12 新 4/4 PASS |
| 2026-04-19 中午 | D1-D4 v2.2 examples 高频 28 域 | 09_examples_data_high.md 112,697 tokens, capacity 20%, T13/T14 新 2/2 PASS, T1/T11 持平 0 衰减 |
| 2026-04-19 下午 | E1-E4 v2.3 examples 其余 35 域 | 10_examples_data_others.md 48,897 tokens, capacity 23%, T15/T16 新 2/2 PASS, **T3 跨批正向激活** (v2.2 拒答 → v2.3 推导) |
| 2026-04-19 晚 | F1-F4 v2.4 terminology 高频 top 200 | 11a/11b/11c 三文件 351,752 tokens, capacity 43%, T17 从推测→11a 原文 ↑ 质变, T18 边界 PASS, **T3 三阶激活** (v2.4 显式 Method A-D), 11b 256K 单文件挤出假设反驳 |
| 2026-04-19 晚 handoff | G1 批 5 rank 201-500 准备 | score_codelists.py 幂等验证, G1_codelist_mid.txt 300 C-code |
| 2026-04-20 早 | G2 mid tier 实现 + G3 v2.5 build | extract_terminology_terms.py 加 tier='mid', 12a/12b/12c 三文件 377,939 tokens, stage v2.5 build 1,097,180 tokens, capacity 投影 73.1% |
| 2026-04-20 中 | 用户优先级重平衡触发 v2.6 追加批 | V6.1 tail list 209 codelist (68 core + 141 supp) + V6.2 tail extractor + 13a/13c 落盘 (188,981 tokens, 6 giants Deferred stub) |
| 2026-04-20 中 | V6.3 v2.6 stage build | build_v2_stage.py --stage v2.6, 19 真实上传 / 1,286,161 tokens, C12 PASS |
| 2026-04-20 下午 | V6.4 终态 hard checkpoint (Cowork Chrome MCP) | STAGE_V2.6_AB_REPORT.md: 24/24 PASS (T1-T20 + T21/T22 + T-core-reb/T-supp-reb), capacity 77% (超预测 14pp) |
| 2026-04-20 晚 | H1-H5 Phase H 收尾 | RETROSPECTIVE_V2 (Rule D 复核 PASS) + rag_decay_curve 终态 + phase7_handoff + Chain B/C/E 索引 + 本文件 + 最终 commit/push |

## 2. 总数据

| 指标 | 值 |
|------|---|
| 启动日期 | 2026-04-18 |
| 完成日期 | 2026-04-20 |
| Stages 完成 | **7** (v2.0 setup + v2.1 + v2.2 + v2.3 + v2.4 + v2.5 + v2.6; 其中 v2.5 未独立 A/B, 被 v2.6 合并) |
| Hard Checkpoints (acked) | **4 批内 ack** (v2.1/v2.2/v2.3/v2.4 via _progress.json.checkpoints_acked) + **1 终态 ack** (v2.6 via STAGE_V2.6_AB_REPORT 24/24 PASS) = 5 ack 决策点 |
| Subagent 调用 | **14** (executor 7 + reviewer 7), 全部 subagent_prompts/ 落盘 |
| 重试 (failures) | **1** (stage_v2.1_t3_regression.md, 保留不删) |
| Commits (Phase 6.5 v2, 本 session 内预期累计 ≥37) | 33 截止 V6.3 + H1-H5 predicted 4-5 额外 commits |
| A/B 测试题数 | **24** (T1-T22 + T-core-reb + T-supp-reb) |
| A/B 测试 PASS | **24/24 (100%)** |
| 回归衰减 ↓ | **0** (跨 6 批 + 1 重平衡批) |
| 跨批正向激活数据点 | **1** (T3 RELREC 4 方法, 三阶激活: v2.2 拒答 → v2.3 推导 → v2.4 显式) |
| 源文件污染 (knowledge_base/) | **0** (P5 强制只读全程生效) |
| 终态 tokens (real upload) | **1,286,161** (vs v1 192,036, **+571%**) |
| 终态 tokens (incl meta) | **1,336,360** |
| 终态文件数 (real upload) | **19** (vs v1 11 实体) |
| 终态文件数 (incl meta) | **32** |
| 终态 capacity (UI 实测) | **77%** (vs v1 12%, +65pp) |
| C12 hard cap (1.5M) headroom | real_upload 213,839 (14.3%) / incl_meta 163,640 (10.9%) |
| 终态覆盖率 (用户优先级) | core **99.3%** (146/147) / supp **100%** (188/188) / quest **55.8%** (374/670, 不扩容) |
| Long tail → Phase 7 RAG | **302** codelist (296 quest + 6 tail giants) |

## 3. 关键决策回顾

1. **中庸策略 ~50% 而非 90%** (v2 design §1.4): 事实修正后合并为 5 批 (而非初版 6 批), 目标 ~50% 容量留 headroom 给 Phase 7. 实际执行 v2.5 build 达 73% (超中庸一点) → v2.6 重平衡后 77%, 仍远低于 85.7% C12 硬约束, 头部空间足够.
2. **用户优先级重平衡** (2026-04-20): 原 F1/G1 按域引用次数打分导致 quest (用户最低优先级) 覆盖最高, 与用户工作语境反向. 追加 v2.6 tail 批 (V6.1-V6.4) 对 core/supp 未覆盖 209 codelist 做 tail-tier 压缩, 而非全重跑. 成本 +188K tokens / ~1.5 小时壁钟, 终态 core 99.3% / supp 100% 达成. **教训固化为规则 E 候选**: 用户业务优先级必须在 PLAN §打分阶段就确认.
3. **Rule D 三 lane 严格执行全程**: Cowork writer (A/B 测试) + 主控 writer (脚本/产物/复盘) + 独立 reviewer subagent (code-reviewer 7 维度审 A/B 报告 + V6.2 extractor + H1 RETROSPECTIVE_V2) 三次 Rule D 独立复核, 全部过. 无自审污染.
4. **Deferred stub 模式验证 (T22 PASS)**: 6 tail giants (均 ≥500 terms, MedDRA-level) 走 1-行 stub + 源路径 + NCI EVS Browser 入口. T22 测试模型在 stub 上的行为: 精准识别 "超大规模未 inline" + 引源文件 + **零臆造 term**. Phase 7 RAG 可直接沿用此模式处理 MedDRA/WHODrug/LOINC/SNOMED 等超大表.
5. **Capacity 预测偏差 (G2 缺口)**: v2.6 本地 tiktoken 预测 63-68%, 实测 UI 77% (+9-14pp 超预期). UI token 统计含元数据/内部索引开销. Phase 7 首次上传前必须做 calibration 实验.

## 4. 完结信号 (6/6 达成)

- [x] output_v2/ 19 真实上传文件齐 (vs 原计划 16-18, 微超因为 v2.6 追加)
- [x] Layer 1 自动检查全 PASS (C12 hard cap / md5 幂等 / stage build rc=0 6 批全 PASS)
- [x] Layer 2 A/B 测试 24/24 PASS (远超 PLAN 最低 T1-T20 无 ↓ + 新批 ≥1 PASS 标准)
- [x] Chain B (worklog + PROGRESS) + Chain C (MANIFEST 新增产物注册) + Chain E (用户优先级重平衡驱动方案调整) 全走完
- [x] RETROSPECTIVE_V2.md 归档 (Rule C 强制, 过 Rule D 独立复核 PASS)
- [x] rag_decay_curve.md 7 数据点完整 (v1 baseline + v2.1-v2.6 含 v2.5 被合并标注)
- [x] phase7_handoff.md 输出 (6 actionable + 5 问题 + 5 步待办)

## 5. 交接清单 (Phase 7 启动前读)

优先级顺序 (建议 <2 小时可读完):

1. `ai_platforms/claude_projects/output_v2/phase7_handoff.md` (最短, actionable 密度最高)
2. `ai_platforms/claude_projects/output_v2/rag_decay_curve.md` (7 数据点 + 结论)
3. `ai_platforms/claude_projects/RETROSPECTIVE_V2.md` §3 关键决策复盘 (5 条)
4. `ai_platforms/claude_projects/output_v2/STAGE_V2.6_AB_REPORT.md` (24/24 PASS 基线)
5. `ai_platforms/claude_projects/output_v2/test_results_v2.md` (T1-T22 完整矩阵)

## 6. 本文件作用

- 作为 `_progress.json status=completed` 的人类可读快照
- 未来 Phase 7 回顾 Phase 6.5 v2 时的 entry point
- 未来其他项目做类似"渐进 RAG 扩容" 时的执行模式参考

---

*作者: 主控 (Claude Opus 4.7), 2026-04-20.*
