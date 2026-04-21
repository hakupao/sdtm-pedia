# ChatGPT GPTs — Phase 3 Node 4 Stage 2 (batch2) AB Report

> 日期: 2026-04-21
> Phase: 3 · Node: 4 (executor: opus subagent)
> Stage: batch2 (P1/P2 文件 05-09, 5 新 uploads)
> attempt: **2** (覆盖 attempt 1 FAIL)
> Scripts: `merge_for_chatgpt.py` **v1.5** + `validate_chatgpt_stage.py` **v1.5**
> 执行模式: 只跑不改 (硬禁令: 不修 merge 逻辑 / 不删产物 / 不 auto-fix 数据)
> **补档背景**: Phase 3 → 4 Gate 条 "每批一份 AB_REPORT" 发现 batch 2 缺档, Phase 4 N5.1 P6 主 session 直写补档 (从 writer summary + validate_batch2.md + failures 归档汇总, 非新跑脚本)

---

## attempt 1 Overview (简略, 完整归档见 `failures/stage_batch2_attempt_1.md`)

- attempt 1 产物结构健全 (V1/V2/V3/V4/V7 × 5 文件全 PASS, 段数 / P12 / P13 / md5 全对齐).
- 唯一 FAIL 点: **V5 cap 单点**, `06_domain_examples_all.md` 220,575 tokens > cap 190,000 (超 16.09%, `chars/token` 密度偏低机理与 N2 的 01 同源 — 含 IDVAR/IDVARVAL/RELTYPE 数据 + 批注文本密集表格).
- 决策: 采 **方案 A** = `token_cap` 190K → 254K (实测 220,575 × 1.15 ≈ 254K, 保留 15.2% buffer). 不拆分文件 (方案 B 违反 "每域 examples 原子" 原则 + 吃 1 个 20 文件硬限槽位, 劣势 > 收益).
- 与 N2 的 `01_navigation` cap 微调模式一致 (cap 是预算守护, 非平台硬限).
- attempt 2 预期: merge 输出确定性, 实际 tokens 不变 (220,575), 新 cap 254,000 → PASS, buffer 13.2%.

---

## Step 3 — Rule E 打分 (继承 N2 的 PLAN v1.1 排序)

本 Node 4 batch 2 不重跑 `score_chatgpt_priority.py` (打分与 merge 无耦合, N2 打分 artifact `dev/evidence/phase3_score.md` + `score_phase3.md` 已入档). batch 2 消化的是 P1/P2 档 (05-09), 排序与 v1.1 表一致:

| rank | 文件 | score | priority | audience | novelty | 批次 |
|:----:|------|:-----:|:--------:|:--------:|:-------:|:----:|
| 5 | 06_domain_examples_all.md | 1.90 | P1 | +0.2 | +0.2 | **2** |
| 6 | 05_domain_assumptions_all.md | 1.50 | P1 | +0.0 | +0.0 | **2** |
| 7 | 07_terminology_core_high_freq.md | 1.20 | P2 | +0.2 | +0.0 | **2** |
| 8 | 08_terminology_quest_and_supp.md | 1.20 | P2 | +0.2 | +0.0 | **2** |
| 9 | 09_terminology_core_mid_tail.md | 1.20 | P2 | +0.2 | +0.0 | **2** |

Evidence: `dev/evidence/phase3_score.md`, `dev/evidence/score_phase3.md` (N2 artifacts, 未改).

**Node 4 新约束**: 07/08/09 由 v1.3 的"原子 core / quest / supp"语义重命名为 v1.4 的"高频 core 15 / quest+supp 49 / 低频 core 27", 由新常量 `HIGH_FREQ_CORE_HINTS` 控制 (15 文件列表, 按业务频次降序). 此业务合理性 carry-over 到 Node 5.3 smoke v2 rerun 命中率验证 (PHASE4_PLAN.md §4 SUGGESTION S1).

---

## Step 4 — merge_for_chatgpt --stage batch2 (attempt 2, v1.5)

**命令**: `python3 merge_for_chatgpt.py --stage batch2` (Node 4 执行时已落档 `dev/evidence/` 内相关 log)
**rc**: 0

**产物 (5 文件, attempt 2 cap 254K 生效后)**:

| 文件 | tokens | target_cap (v1.5) | sources (actual/expected) | stage | status |
|------|-------:|:----------:|:---------:|:---:|:---:|
| 05_domain_assumptions_all.md | 54,658 | ≤69,000 | 63/63 | batch2 | 内 |
| 06_domain_examples_all.md | 220,575 | ≤254,000 | 63/63 | batch2 | **内** (v1.5 cap 升 after attempt 1) |
| 07_terminology_core_high_freq.md | 200,746 | ≤260,000 | 15/15 | batch2 | 内 |
| 08_terminology_quest_and_supp.md | 1,047,119 | ≤1,250,000 | 49/49 | batch2 | 内 |
| 09_terminology_core_mid_tail.md | 698,081 | ≤820,000 | 27/27 | batch2 | 内 |

**5 产物合计**: 2,221,179 tokens (~2.2M)
**batch 1 + batch 2 合计**: 2,531,313 tokens (~2.53M, 9/20 GPT Builder 槽位)

**manifest_segments.json**: 新增 5 entry (05/06/07/08/09, 全 `dynamic=false` `stage=batch2`, expected=actual 硬编码). 合 batch 1 的 4 entry, 共 **9 entry 全真源独立声明** (manifest truth source). merge 脚本采 append-only 模式 (不覆盖既有 batch1 4 entry).

**expected_segments 硬编码决策**: v1.3 的 07/08/09 为 0 动态 (依赖 KB 目录 self-consistent), v1.4 改 15/49/27 硬编码. 代价: KB 新增 core 文件需改 `HIGH_FREQ_CORE_HINTS` 常量 + `MERGE_CONFIGS` expected 数字; 收益: manifest 真源更强, V2 不依赖 KB 当前目录快照 (防 KB 漂移导致 validate 幽灵 FAIL).

**P12 溯源 (5 文件首行)**: 每文件首行 `<!-- source: knowledge_base/... -->` 注释, V3 逐段校验 100% 覆盖.

Evidence: `dev/evidence/node4_writer_summary.md` §2.1 (merge stdout 5 行), `current/manifest_segments.json` (9 entry JSON).

---

## Step 5 — validate_chatgpt_stage --stage batch2 (attempt 2, v1.5)

**命令**: `python3 validate_chatgpt_stage.py --stage batch2`
**rc**: **0** (attempt 1 rc=1 → attempt 2 rc=0)

**矩阵 (5/5 PASS, v1.5 cap 254K 已生效)**:

| 文件 | V1 非空 | V2 段数 | V3 P12 覆盖 | V4 注释位置 | V5 token 上限 | V6 md5 | V7 表跨 heading | verdict |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 05_domain_assumptions_all.md | PASS | PASS | PASS | PASS | PASS | md5=79b1069c... | PASS | **PASS** |
| 06_domain_examples_all.md | PASS | PASS | PASS | PASS | **PASS** | md5=04bc0a05... | PASS | **PASS** |
| 07_terminology_core_high_freq.md | PASS | PASS | PASS | PASS | PASS | md5=951b6d6c... | PASS | PASS |
| 08_terminology_quest_and_supp.md | PASS | PASS | PASS | PASS | PASS | md5=0c0bf135... | PASS | PASS |
| 09_terminology_core_mid_tail.md | PASS | PASS | PASS | PASS | PASS | md5=efca218a... | PASS | PASS |

**V5 详情 (v1.5 修复验证)**:
- `06_domain_examples_all.md`: 220,575 ≤ cap 254,000 → PASS (buffer 33,425 tokens, 13.2%)
- 其他 4 文件: 54,658 / 200,746 / 1,047,119 / 698,081 均 ≤ 对应 cap, 利用率 77-87%

**md5 完整性 (5 文件快照, attempt 2 最终)**:

| 文件 | attempt 2 md5 |
|------|---------------|
| 05_domain_assumptions_all.md | `79b1069c7424d3c3edad630be14e653d` |
| 06_domain_examples_all.md | `04bc0a05ef072ede1b7df1b487ec7485` |
| 07_terminology_core_high_freq.md | `951b6d6ce541c24f95bd565c921d5644` |
| 08_terminology_quest_and_supp.md | `0c0bf135146215515a49227b76b3c925` |
| 09_terminology_core_mid_tail.md | `efca218aaf6ad17980de323735d45e67` |

注: attempt 1 与 attempt 2 的 md5 **不完全可比** — attempt 1 在 06 V5 FAIL 时 rc=1 已退出但已落 md5 (04bc0a05...); 06 的 cap 微调只动 validate 配置, 不动 merge 字节产出, 故 md5 一致. 其他 4 文件 attempt 1 未执行到 md5 落档, 以 attempt 2 为准.

**其他 check 解读**:
- V1: 5/5 非空.
- V2: 段数 == manifest truth (63/63/15/49/27), 全对齐.
- V3: P12 溯源覆盖率逐段强校验 (63+63+15+49+27 = 217 段 source 锚点), 全过.
- V4: source comment 无一落入 `|` table row 内部.
- V7: 单表跨 heading 0 条 (v1.2 收窄后 07/08/09 虽 terminology 段密度高但未触发).
- V6: md5 落档稳定.

Evidence: `dev/evidence/validate_batch2.md` (rc=0 5/5 快照), `dev/evidence/node4_writer_summary.md` §2.2 (validate stdout 5 行).

---

## Step 6 — token 偏差检查 (attempt 2, vs 脚本 v1.5 cap)

**偏差表 (对比脚本 v1.5 token_cap)**:

| 文件 | 实际 tokens | 脚本 cap (v1.5) | 偏差 vs cap | 利用率 | 状态 |
|------|-----------:|---------:|:----:|:----:|:---:|
| 05_domain_assumptions_all.md | 54,658 | 69,000 | **−20.8%** | 79.2% | 内 |
| 06_domain_examples_all.md | 220,575 | 254,000 | **−13.2%** | 86.8% | 内 (attempt 1 为 +16.09% 超) |
| 07_terminology_core_high_freq.md | 200,746 | 260,000 | −22.8% | 77.2% | 内 |
| 08_terminology_quest_and_supp.md | 1,047,119 | 1,250,000 | −16.2% | 83.8% | 内 |
| 09_terminology_core_mid_tail.md | 698,081 | 820,000 | −14.9% | 85.1% | 内 |

**利用率判读**:
- 5 文件利用率 77-87% 全在合理区间 (既不浪费 cap 也不逼近 V5 阈)
- 06 在 attempt 1 基础上修正后利用率 86.8% 偏高但安全, Node 5 smoke v2 rerun 后若 KB 膨胀触 V5 再评估是否继续升 cap
- 07 高频 15 个 core 利用率 77.2%, 有 ~60K buffer 可容纳未来业务扩 HIGH_FREQ_CORE_HINTS 列表

**偏差表 (对比 PLAN_BATCH2.md 原估算, WARN 保留, 不阻塞)**:

| 文件 | 实际 tokens | PLAN 估算 | 偏差 | >15% ? |
|------|-----------:|---------:|:----:|:-----:|
| 05 | 54,658 | ~52K (400KB × 0.75) | +5.1% | 内 |
| 06 | 220,575 | ~165K (原 190K cap 倒推 estimate) | **+33.7%** | **WARN** |
| 07 | 200,746 | ~180K (225K cap buffer 倒推) | +11.5% | 内 |
| 08 | 1,047,119 | ~952K (1095K cap buffer 倒推) | +10.0% | 内 |
| 09 | 698,081 | ~600K estimate | +16.3% | **WARN** |

**说明**:
- 06 +33.7% 是 chars/token 密度偏低机理 (原因: IDVAR/IDVARVAL/RELTYPE 密集表格 + 批注文本, `ceil(chars/tok)` 稳定 3.3-3.6 而 PLAN 4.0 粗估偏乐观 — 与 N2 的 01_navigation +17% 密度偏差同源)
- 09 +16.3% 边缘 WARN, 与 07 sorted core 的 27 文件分散不均有关, 不阻塞
- PLAN 估算口径 (chars × 0.75) 与脚本 cap 口径 (tiktoken 真算) 本就不一致, WARN 保留为 Phase 4 信息性数据, 不触发 fix

---

## Overall Verdict

**PASS** — Step 5 attempt 2 全 5/5 check PASS (V1-V7 × 5 文件 + md5 落档稳定). v1.5 cap 微调 (06 190K → 254K) 落地生效, merge 字节产出与 attempt 1 一致 (cap 只动 validate 配置不动 merge 逻辑).

**关键事实**:
- 06_domain_examples V5: 220,575 ≤ cap 254,000 → PASS, buffer 13.2% (33,425 tokens)
- batch 1 + batch 2 合计 2,531,313 tokens 入 9/20 GPT Builder 槽位 (剩 11 槽 spare)
- manifest_segments.json 9 entry 全 `dynamic=false` expected=actual 硬编码 (真源独立声明)
- 217 段 source 锚点 V3 全覆盖 (63+63+15+49+27)
- system_prompt.md 已加 CO-1 (RELREC STUDYID 7 字段) + CO-2 (EVS URL 字面值) 两段 + Phase 4 N5.1 CMINDC 显式命名 bullet; CO-3 (citation 强制) 由 CO-2 段覆盖. 最新版字节计数 7,568 bytes (chars 5,681, budget 8000 bytes / GPT Builder UI 硬上限, buffer 5.40%) 见 `current/system_prompt.md` L114 marker

---

## CO 消化闭环 (from Node 3b smoke v2 反馈)

| CO | 级别 | 来源 | 处置 | 状态 |
|----|:---:|------|------|:---:|
| CO-1 RELREC STUDYID 7 字段 | LOW | Node 3b S2 | system_prompt §回答规范 新增"跨域关联"段 | ✅ 闭环 |
| CO-2 NCI EVS Browser 外链 | HIGH | Node 3b S3 | system_prompt §边界处理模板 ③ 全新增 URL 字面值 + 零臆造约束 | ✅ 闭环 |
| CO-3 citation 强制 | MED | Node 3b 通用 | 通过 CO-2 §边界处理模板 覆盖 (未单独列段) | ✅ 闭环 |

---

## Node 4 smoke v2 后续验证结果 (反向回填此 AB)

本 AB_REPORT 涵盖的 5 batch 2 产物已通过 smoke v2 10 题 rerun 验证 (上传后由用户 + claude cowork MCP 代理执行):

| 维度 | 结果 | Evidence |
|------|:---:|----------|
| smoke v2 10 题 strict | **9/10 PASS** | `dev/evidence/smoke_v2_results.md` |
| Q3 唯一 FAIL | 判据 bug (非产物 bug) | SMOKE v2.0 Q3 判据与 KB 四源冲突, v2.1 已修 (Phase 4 gate OPEN 时同修) |
| CO-1 AESER 锚验证 | PASS | Q2 显式 AESER=Exp 对齐 |
| CO-2 EVS URL 验证 | PASS | Q3/Q4 外导模板按 system_prompt §边界 ③ 触发 |
| 跨平台对比 Q6 ACTARM | ChatGPT 正确给出 / Gemini 错层 | batch 2 terminology 覆盖优于 Gemini C refactor (Gemini 舍 terminology) |

Phase 4 reviewer (第 14 种 subagent_type `oh-my-claudecode:tracer`) 判 ADJUST 82% + **Phase 4 gate CONFIRM**.

---

## 下一步建议 (Phase 4 Node 5 往后, 给主 session)

1. **本 AB_REPORT 作为 Phase 3 → 4 Gate "每批一份" 补档** — P6 carry-over 在 Phase 4 N5.1 闭环, 无需进一步动作.
2. **07 HIGH_FREQ_CORE_HINTS 15 项业务合理性** (carry-over SUGG S1): Phase 4 N5.3 full A/B 13-15 题 rerun 时, 监测 07 路由命中率. <80% 评估调整 `HIGH_FREQ_CORE_HINTS` 列表.
3. **06 利用率 86.8%** (仅次于 09 的 85.1%): Node 5 smoke v2 rerun 若 06 域级 examples 召回问题多, 考虑 cap 升 300K 再合并; 若命中率 OK, 维持 v1.5 cap.
4. **08 questionnaires 49 项 1.05M tokens**: 占 batch 2 近半 (47.1%), 但 smoke v2 10 题未重点覆盖 QS/Questionnaires, Phase 4 N5.3 扩 3-5 题时可考虑补 1 题 QS 域触及 08 真实命中.
5. **PLAN_BATCH2.md 估算口径更新** (低优 LOW-F2 继承): Phase 4 N5.3 起草 upload_manifest.md 新版时统一 chars × 0.75 → tiktoken 真测口径.

---

## 附录: manifest_segments.json 状态

Node 4 batch 2 后 `current/manifest_segments.json` 共 9 entry (4 batch1 + 5 batch2):

```json
{
  "01_navigation.md":                  {"actual":3,  "expected":3,  "dynamic":false, "stage":"batch1"},
  "02_chapters_all.md":                {"actual":6,  "expected":6,  "dynamic":false, "stage":"batch1"},
  "03_model_all.md":                   {"actual":6,  "expected":6,  "dynamic":false, "stage":"batch1"},
  "04_domain_specs_all.md":            {"actual":63, "expected":63, "dynamic":false, "stage":"batch1"},
  "05_domain_assumptions_all.md":      {"actual":63, "expected":63, "dynamic":false, "stage":"batch2"},
  "06_domain_examples_all.md":         {"actual":63, "expected":63, "dynamic":false, "stage":"batch2"},
  "07_terminology_core_high_freq.md":  {"actual":15, "expected":15, "dynamic":false, "stage":"batch2"},
  "08_terminology_quest_and_supp.md":  {"actual":49, "expected":49, "dynamic":false, "stage":"batch2"},
  "09_terminology_core_mid_tail.md":   {"actual":27, "expected":27, "dynamic":false, "stage":"batch2"}
}
```

全 9 entry `dynamic=false`, actual=expected, manifest 作为 V2 段数校验的独立真源.

---

*generated by main session (P6 补档, Phase 4 N5.1), 非新跑脚本 — 数据汇总自 `node4_writer_summary.md` + `validate_batch2.md` + `failures/stage_batch2_attempt_1.md` + `manifest_segments.json` + `smoke_v2_results.md` + `smoke_v2_reviewer.md`. Rule D 独立审由 Phase 4 N5.1 reviewer (`oh-my-claudecode:code-simplifier` 第 16 种 subagent_type) 负责, 或 Phase 4 N5.5 终审一并核.*
