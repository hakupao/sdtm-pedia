# Stage v2.5 Cowork 自动执行手册 (⚠️ v2 终态 HARD CHECKPOINT)

> **给 Claude Cowork (computer-use / browser 模式) 执行.**
> Cowork 亲自点浏览器上传 **3 个新文件** + 更新 Instructions + 跑 **T1-T20 全 20 题** A/B, 返回结构化报告.

---

## 背景 (≤ 120 字)

Stage v2.5 给 v2 Project 再加 **3 个文件** (按 terminology subdir 拆分, mid tier) 合计 **377,939 tokens**: `12a_terminology_mid_core.md` (50 codelist/130.0K) + `12b_terminology_mid_questionnaires.md` (222 codelist/224.7K) + `12c_terminology_mid_supp.md` (28 codelist/23.3K). 覆盖 rank 201-500 的 **300 个中频 codelist** 压缩版 Term 值 (3-列: Code / Submission Value / Definition ≤100 字符, 不含 Synonyms/NCI 链接). v2 累计 **17 上传文件 / 1,097,180 tokens**, capacity 约 55-58% (v2.4 43% + ~+15pp). 本批是 **v2 终态**, 所以必须跑 T1-T20 全 20 题.

⚠️ **关键优先级修订 (用户 2026-04-20 ack)**: `core > supplementary > questionnaires` 是用户工作语境的重要度 (非 SDTM 标准定义). 当前按域引用次数排名的 F1/G1 导致 questionnaires 过度覆盖 (55.8%) 而 supplementary 覆盖不足 (25.0%). 本批测试请补充 **core + supp 边界题** 作 v2.6 再平衡输入.

---

## 你 (Cowork) 的任务

在**已存在的 v2 Project** (`SDTM-Knowledge-v2`) 下:
1. Project Knowledge 新增上传 **3 个文件** (12a/12b/12c)
2. 覆盖更新 Project Instructions, 粘贴最新 `output_v2/system_prompt_v2.md` 全文 (比 v2.4 多 `<!-- stage v2.5 begin -->` 段)
3. 跑 **T1-T20 全 20 题** A/B 测试 (新 2 + 回归 18)
4. 返回 Markdown 结构化报告

**权限假设/目录**: 同 v2.4 handoff

---

## Step 1: 进入现有 v2 Project

1. 打开 `https://claude.ai`
2. 进入 **Projects** 列表, 打开 `SDTM-Knowledge-v2` (v2.4 已在, 含 14 上传文件)

---

## Step 2: 覆盖 Project Instructions

1. Instructions 编辑区
2. 读 `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/system_prompt_v2.md`
3. **全文覆盖粘贴**
4. 保存

注: 新增 `<!-- stage v2.5 begin -->` 段, 核心变化:
- CT Code 查询优先级升级: `11a/11b/11c (high full Term 4 列) > 12a/12b/12c (mid 压缩 Term 3 列) > 08 (映射)`
- mid tier 不含 Synonyms, 如需 Synonyms 指向源 `knowledge_base/terminology/**/*.md`
- 子目录路由同 11 系: core→a / questionnaires→b / supplementary→c

---

## Step 3: 上传 3 个新文件到 Project Knowledge

| # | 绝对路径 | 大小 (tokens) | 内容 |
|---|---------|--------------:|------|
| 1 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/12a_terminology_mid_core.md` | **129,963** | 50 core mid codelist (Tumor Test Result / Microbiology Susc / ...) |
| 2 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/12b_terminology_mid_questionnaires.md` | **224,659** | 222 QRS Test Name/Code pair mid codelist |
| 3 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/12c_terminology_mid_supp.md` | **23,317** | 28 Device/Functional Test mid codelist |

**合计 (v2.5 终态)**: **17 上传文件 / 1,097,180 tokens** (v2.4 14×719,241 + 3 新×377,939).

**不要上传 meta**: 同 v2.4 list (不要上传本 handoff 文件 / STAGE_V2.* / CHECKPOINT_V2.* / rag_decay_curve / test_results / upload_manifest / _progress / trace / evidence_v2/*). 不要重传 v2.4 的 14 文件.

---

## Step 4: 等 indexing + 记 capacity %

**预期 capacity ~55-58%** (v2.4 43% + 377.9K/16K-per-pp ≈ +23.6pp).

⚠️ **本批 indexing 可能最慢** (累计 1.1M tokens, 12b 单文件 225K tokens 近 v2.4 11b 256K 量级). 如 indicator >50 分钟仍显示 "Indexing", 沿用 v2.4 策略尝试提问, 命中即证可用.

记下:
- 实测 capacity %
- Indexing 指示器用时 (大概观察)
- 任何异常 (上传失败 / 文件过大拒绝 / indexing 超时 / Claude 报错)

---

## Step 5: 跑 T1-T20 全 20 题 A/B 测试

**v2.5 是终态**, 所以必须跑全 20 题, **不是 6 题**.

在同一 v2 Project 开**新对话** (建议一次一题避免上下文污染, 或 4 题一组分 5 轮).

### v1 baseline 已 PASS 的 T1-T8 (8 题回归)

#### T1. AE.AEDECOD 的 Core 属性是什么?
期望: Core=Req, §4.3.6 三元, AEPTCD 配套. **最敏感深度回归题**.

#### T2. DM.SEX codelist 有哪些值?
期望: 4 terms (M/F/U/UNDIFFERENTIATED), Source 标 **11a (而非 08)**.

#### T3. PC↔PP 通过 RELREC 关联的 4 种方法?
期望: v2.4 显式 Method A/B/C/D + relrec.xpt 数据表 (持平或 ↑, **v2.3/v2.4 连续 ↑ 数据点**).

#### T4. SE 域的 Topic Variable 是什么?
期望: ETCD (Element Code), §7.4.3.

#### T5. Assumption 如何处理受试者退出?
期望: DS.DSDECOD + DSSTDTC, §4.2.4.

#### T6. ECG Waveform 如何记录?
期望: EG 域 + EGTESTCD, §6.3.1.

#### T7. CT Code C66742 有哪些具体值?
期望: 完整 4 Term 表 (N/NA/U/Y) + 41 Related Domains, Source 标 11a. (v2.4 已 ↑ 质变).

#### T8. Mega Spec 中 AE.AESTDTC 的 Notes?
期望: ISO 8601 datetime + Required when AESTART.

### v2.2 新增 T13/T14 (2 题回归)

#### T13. DM 域完整 Example 表?
期望: 6×25 dm.xpt + ARMNRS=SCREEN FAILURE, Source 标 09.

#### T14. EX 域的 EXADJ free-text 是什么?
期望: Ex4 6×14 ex.xpt + EXADJ free-text reason, Source 标 09.

### v2.3 新增 T15/T16 (2 题回归)

#### T15. RP 域 Example 数据?
期望: 完整 21×18 rp.xpt 双场景 (P0001 childbearing + P0002 post-menopausal) + RPDUR P3Y, Source 标 10.

#### T16. FT 域 6MWT Example + suppft 关联?
期望: 6×16 ft.xpt (SIXMW101-106) + suppft FTASSTDV=CANE, 引 06 QRS Naming Rules.

### v2.4 新增 T17/T18 (2 题回归)

#### T17. C66742 codelist 所有 Term 值 + Definition?
期望: 完整 4 Term + Definition + Extensible No + 41 Related Domains, Source 标 **11a**.

#### T18. AERELN codelist 全部 Synonyms (边界测试)?
期望: 坦诚 AERELN 不是 SDTMIG v3.4 标准 codelist + 列 AEREL/AERLDEV/AERELNST 系列 + 已发布 AE codelist + 指向源.

### v2.5 新增 T19/T20 (2 题 — 本批重点)

#### T19 (新增, 批 5 核心测试点, **core 优先级**): codelist C71620 有哪些值? (Laterality)
**预期 v2.4 答案**: 在 G1 audit 中 rank 显示, 但未在 F1/F2 top 200 → v2.4 Project 应答"不在 Project, 指向源路径".
**本批 C71620 应在 12a_core (rank 201-500)**. 期望 v2.5 能:
- 直接引用 12a_terminology_mid_core.md 里的 3-列 Term 表 (Code / Submission Value / Definition ≤100 字符)
- 附 Related Domains 行
- **坦诚注明 Definition 为 100 字符压缩版** (此为 mid tier 边界规则)
- 若用户追问 Synonyms, 必须指向源 `knowledge_base/terminology/core/*.md`
- 判定: **PASS** = 原文命中 3-列 + 声明压缩边界 + Synonyms 边界指向源; **FAIL** = 臆造 Synonyms 或未声明压缩边界.

#### T20 (新增, 批 5 核心测试点, **supplementary/边界测试**): codelist C128685 (Microbiology Interpretation) 有哪些值?
**预期 v2.4 答案**: 不在, 指向源.
**本批 C128685 在 12c_supp 或 12a_core** (需 Claude 判断子目录路由). 期望 v2.5 能:
- 原文命中 + 声明压缩边界 + Related Domains
- 判定: **PASS** = 原文命中 + 压缩边界; **FAIL** = 臆造.

> 注: T19/T20 具体 C-code 可由 Cowork 从 12a/12c 文件中抽 2 个 rank 靠前的核心 codelist 代替, 只要满足"原 v2.4 不在 + v2.5 在"即可.

### 深度回归增补 (v2.5 终态重点, **core/supp 优先级**)

#### T-core (user priority 追加题): 12a 核心 codelist 是否无 Synonyms + 定义截断正确?
随机抽 12a 里 1 个 codelist (如 C124309 Tumor Test Result), 问 "所有 Term 值 + Definition 完整版". 期望:
- 原文命中 3-列 表
- 声明 "Definition 为 100 字符词边界截断, 完整 Definition 见源 `knowledge_base/terminology/core/oncology_part2.md`"
- 不编造 Synonyms

#### T-supp (user priority 追加题): 12c supplementary 是否路由正确?
随机抽 12c 里 1 个 codelist, 问 "所有 Term 值". 期望:
- Claude 能识别 codelist 在 supplementary 子目录
- Source 标 12c_terminology_mid_supp.md
- 不把它误标在 12a 或 12b

---

## Step 6: 评估每题精度

| 精度标签 | 说明 |
|---------|-----|
| **持平** | v2.4 和 v2.5 答案同质 |
| **↑** | v2.5 比 v2.4 更精确 (或突破边界) |
| **↓** | v2.5 比 v2.4 差 |

- T19/T20/T-core/T-supp: PASS / FAIL
- T1-T18: 持平 / ↑ / ↓

---

## Step 7: 返回最终报告

```markdown
# Stage v2.5 A/B 测试报告 (v2 终态)

> 执行日期: YYYY-MM-DD HH:MM
> Capacity (v2.5): XX% (v2.4 参照: 43%)
> Indexing 用时: ~N 分钟 (或"仍显示但提问直接命中")

## 上传确认
- [x] 12a_terminology_mid_core.md 上传 (129,963 tokens)
- [x] 12b_terminology_mid_questionnaires.md 上传 (224,659 tokens)
- [x] 12c_terminology_mid_supp.md 上传 (23,317 tokens)
- [x] system_prompt_v2.md 覆盖
- [x] Indexing 完成 (或"指示器仍显示但提问命中")

## T1-T20 全结果

### v1 baseline 回归 (T1-T8)
| # | 题目简称 | v2.4 结论 | v2.5 结论 | 精度 vs v2.4 |
|---|---------|----------|----------|-------------|
| T1 | AEDECOD Core | Req + §4.3.5/4.3.6 + MedDRA | [你的答案] | 持平/↑/↓ |
| T2 | DM.SEX codelist | 4 terms (11a) | [你的答案] | 持平/↑/↓ |
| T3 | PC↔PP RELREC 4 方法 | Method A/B/C/D + relrec.xpt | [你的答案] | 持平/↑/↓ |
| T4 | SE Topic | ETCD §7.4.3 | [你的答案] | 持平/↑/↓ |
| T5 | DS 退出处理 | DSDECOD + DSSTDTC §4.2.4 | [你的答案] | 持平/↑/↓ |
| T6 | ECG Waveform | EG + EGTESTCD §6.3.1 | [你的答案] | 持平/↑/↓ |
| T7 | C66742 (CT Code) | 11a 原文 4 Term + 41 Related | [你的答案] | 持平/↑/↓ |
| T8 | AESTDTC Notes | ISO 8601 + Required when | [你的答案] | 持平/↑/↓ |

### v2.2 新增 (T13/T14)
| # | 题目简称 | v2.4 结论 | v2.5 结论 | 精度 |
|---|---------|----------|----------|------|
| T13 | DM 完整 Example | 6×25 dm.xpt | [你的答案] | 持平/↑/↓ |
| T14 | EX EXADJ free-text | Ex4 6×14 | [你的答案] | 持平/↑/↓ |

### v2.3 新增 (T15/T16)
| # | 题目简称 | v2.4 结论 | v2.5 结论 | 精度 |
|---|---------|----------|----------|------|
| T15 | RP Example | 21×18 双场景 | [你的答案] | 持平/↑/↓ |
| T16 | FT 6MWT Example | 6×16 + suppft | [你的答案] | 持平/↑/↓ |

### v2.4 新增 (T17/T18)
| # | 题目简称 | v2.4 结论 | v2.5 结论 | 精度 |
|---|---------|----------|----------|------|
| T17 | C66742 Term+Def | 11a 4 Term + 41 Related | [你的答案] | 持平/↑/↓ |
| T18 | AERELN 边界 | PASS (坦诚+邻近) | [你的答案] | 持平/↓ |

### v2.5 新增 (T19/T20 + user priority 追加)
| # | 题目简称 | v2.5 结论 | PASS/FAIL |
|---|---------|----------|-----------|
| T19 | C71620 Laterality (core mid) | [你的答案] | PASS/FAIL |
| T20 | C128685 (supp mid) | [你的答案] | PASS/FAIL |
| T-core | 12a 核心 codelist 压缩边界 | [你的答案] | PASS/FAIL |
| T-supp | 12c 路由正确性 | [你的答案] | PASS/FAIL |

## 汇总
- 回归 ↓ 数 (T1-T18): N / 18
- v2.5 新增 PASS: K / 4 (T19, T20, T-core, T-supp)
- 累计 PASS (全 20 题 + 2 user priority): ? / 22

## 关键观察 (3-5 条)
- 12b 225K 是否挤出 12a/12c 召回?
- C71620 / C128685 能否原文命中 + 声明压缩边界?
- 12c 路由到 supp 子目录是否正确?
- 1.1M token 累计下 05/09/02 老文件召回是否衰减?
- Capacity 爬升曲线是否匹配预期 ~55-58%?
- 用户优先级 core>supp>quest 对当前覆盖率的反馈信号 (questionnaires 过覆盖 vs supplementary 欠覆盖)

## 异常/警告
- 或 "无异常"
```

---

## 决策矩阵 (供主控参考)

| Cowork 报告 | 主控决策 |
|------------|---------|
| T1-T18 无 ↓ + T19+T20 ≥1 PASS + T-core/T-supp ≥1 PASS | 进入 Phase H 收尾 (H1 RETROSPECTIVE / H2 RAG 曲线 / H3 Chain 索引) |
| T1-T18 无 ↓ + T19+T20 全 FAIL | 不 blocking, 记入 rag_decay_curve 但进 Phase H |
| **T1-T18 有 ≥1 ↓** | **立即停, v2.5 视为衰减拐点, 主控调 reviewer 归因** |
| Capacity 与预期偏差 >5pp | 记入 rag_decay_curve 作数据点 |
| **用户优先级反馈 (core/supp 覆盖偏低)** | 主控评估是否在 Phase H 前插入 **v2.6 重平衡批次** (68 core uncovered + 141 supp uncovered 共 209 codelist 拉进来) |
| 用户要暂停 | 暂停 |

---

## 不要做

- 不要自行登录 claude.ai
- 不要编造 Claude 的回答
- 不要修改 output_v2/ 任何 .md
- 不要跳题
- 不要上传 meta 文件或重传 v2.4 的 14 文件
- 不要延长 Instructions (只粘 system_prompt_v2 原文)
- 不要把 T19/T20 伪装成已 PASS (mid tier 必须声明压缩边界)

---

## 完成信号

给出结构化报告 → 主控:
1. 写 `stage_v2.5_terminal.md` 终态 evidence (含 rag_decay_curve v2.4→v2.5 段)
2. 按决策矩阵判断是否进入 **v2.6 重平衡** 或直接 Phase H 收尾
3. Phase H 必做: H1 RETROSPECTIVE_V2 / H2 RAG 曲线 + phase7_handoff / H3 Chain B/C/E 索引 / H4 _phase_summary / H5 最终 commit
