# Stage v2.6 Cowork 自动执行手册 (⚠️ v2 终态 HARD CHECKPOINT, 取代 G4)

> **给 Claude Cowork (computer-use / browser 模式) 执行.**
> Cowork 亲自点浏览器上传 **2 个新文件** + 更新 Instructions + 跑 **T1-T22 全 22 题** A/B + **T-core-reb/T-supp-reb 2 题优先级验证**, 返回结构化报告.

---

## 背景 (≤ 150 字)

**v2.6 是用户优先级重平衡批** (取代 v2.5 作为 v2 终态). 用户 2026-04-20 ack 子目录优先级修订: **core > supplementary > questionnaires** (工作语境, 非 SDTM 标准). v2.5 按域引用次数排名导致反转 — quest 覆盖最高 (55.8%, 用户最不重要) 而 supp 覆盖最低 (25.0%, 用户第二重要). 方案 B 执行: 拉 rank >500 的 **209 个 core+supp uncovered codelist** (68 core + 141 supp) 作 v2.6 tail tier.

本批上传 **2 个新文件** 合计 **188,981 tokens**:
- `13a_terminology_tail_core.md` (68 codelist / 145,787 tokens, **含 6 个 MedDRA 级巨型 codelist 以 Deferred to Phase 7 RAG stub 呈现** — 非 inline Term 表)
- `13c_terminology_tail_supp.md` (141 codelist / 43,194 tokens, 全 inline)

**不含 13b** (questionnaires 按用户优先级明示排除于本批). v2 累计 **19 上传文件 / 1,286,161 tokens ≈ 85.7% of 1.5M C12** (headroom ~214K / 14.3%).

**覆盖率重平衡效果**:
| 子目录 | v2.5 | v2.6 | 用户优先级 |
|---|---:|---:|---|
| **core** | 53.7% (79/147) | **99.3% (146/147)**¹ | 🥇 最重要 |
| **supplementary** | 25.0% (47/188) | **100.0% (188/188)** | 🥈 第二 |
| questionnaires | 55.8% (374/670) | 55.8% (374/670, 未变) | 🥉 最不重要 |

¹ 1 个 core 未算"完整 inline"是 giant C85491 (1,639 terms, MedDRA-like), 以 Deferred stub 形式存在, 查 Term 需走源路径.

---

## 你 (Cowork) 的任务

在**已存在的 v2 Project** (`SDTM-Knowledge-v2`) 下:
1. Project Knowledge 新增上传 **2 个文件** (13a + 13c)
2. 覆盖更新 Project Instructions, 粘贴最新 `output_v2/system_prompt_v2.md` 全文 (比 v2.5 多 `<!-- stage v2.6 begin -->` 段)
3. 跑 **T1-T22 全 22 题** A/B 测试 + **T-core-reb/T-supp-reb 2 题优先级验证**
4. 返回 Markdown 结构化报告

**权限假设/目录**: 同 v2.5 handoff

---

## Step 1: 进入现有 v2 Project

1. 打开 `https://claude.ai`
2. 进入 **Projects** 列表, 打开 `SDTM-Knowledge-v2` (v2.5 已在, 含 17 上传文件)

---

## Step 2: 覆盖 Project Instructions

1. Instructions 编辑区
2. 读 `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/system_prompt_v2.md`
3. **全文覆盖粘贴**
4. 保存

注: 新增 `<!-- stage v2.6 begin -->` 段, 核心变化:
- CT Code 查询优先级升级为: `11a/11b/11c (high full 4 列) > 12a/12b/12c (mid 3 列) > 13a/13c (tail 3 列 + 6 giants stub) > 08 (名称映射)`
- tail tier 的 6 个 Deferred giants (C65047/C67154/C85491/C85494/C120527/C120528) 查询时需声明"该 codelist 在 Project 中以 Deferred stub 呈现, Term 完整表在源路径 knowledge_base/terminology/core/*.md"
- 13b 不存在于本 Project (questionnaires 按用户优先级排除)

---

## Step 3: 上传 2 个新文件到 Project Knowledge

| # | 绝对路径 | 大小 (tokens) | 内容 |
|---|---------|--------------:|------|
| 1 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/13a_terminology_tail_core.md` | **145,787** | 68 core tail codelist (62 inline 3-col Term 表 + 6 Deferred stubs, 覆盖 C85491/C65047/C67154 等 MedDRA 级 giants) |
| 2 | `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/13c_terminology_tail_supp.md` | **43,194** | 141 supp tail codelist (全 inline 3-col, 含 Blood Pressure / Route of Administration / Lab Test Code 等 supp subdir 剩余) |

**合计 (v2.6 终态)**: **19 上传文件 / 1,286,161 tokens** (v2.5 17×1,097,180 + 2 新×188,981).

**不要上传 meta**: 同 v2.5 list 扩展. 不要上传:
- 本 handoff 文件 (CHECKPOINT_V2.6_HANDOFF.md)
- STAGE_V2.* 或 CHECKPOINT_V2.* 系列
- rag_decay_curve / test_results / upload_manifest / _progress / trace / evidence_v2/*
- **特别: 不要上传 13b_terminology_tail_questionnaires.md (本文件不存在 by design)**

不要重传 v2.5 的 17 文件.

---

## Step 4: 等 indexing + 记 capacity %

**预期 capacity ~63-68%** (v2.5 ~55% + 188.9K/16K-per-pp ≈ +12pp).

⚠️ **本批 indexing 可能最慢** (累计 1.29M tokens, 接近 C12 85.7%). 如 indicator >60 分钟仍显示 "Indexing", 沿用 v2.5 策略尝试提问, 命中即证可用.

记下:
- 实测 capacity %
- Indexing 指示器用时
- 任何异常

---

## Step 5: 跑 T1-T22 全 22 题 + T-core-reb/T-supp-reb A/B 测试

**v2.6 是真正的 v2 终态** (取代 v2.5 G4), 必须跑全 22 题 + 2 题优先级验证.

在同一 v2 Project 开**新对话** (建议分 4-5 轮, 一次一题避免上下文污染).

### v1 baseline 已 PASS 的 T1-T8 (8 题回归)

#### T1. AE.AEDECOD 的 Core 属性是什么?
期望: Core=Req, §4.3.6 三元, AEPTCD 配套. 持平 v2.5.

#### T2. DM.SEX codelist 有哪些值?
期望: 4 terms (M/F/U/UNDIFFERENTIATED), Source 标 **11a**.

#### T3. PC↔PP 通过 RELREC 关联的 4 种方法?
期望: Method A/B/C/D + relrec.xpt 数据表. 持平 v2.5 (v2.3/v2.4/v2.5 连续 ↑ 数据点).

#### T4. SE 域的 Topic Variable 是什么?
期望: ETCD, §7.4.3.

#### T5. Assumption 如何处理受试者退出?
期望: DS.DSDECOD + DSSTDTC, §4.2.4.

#### T6. ECG Waveform 如何记录?
期望: EG 域 + EGTESTCD, §6.3.1.

#### T7. CT Code C66742 有哪些具体值?
期望: 完整 4 Term + 41 Related Domains, Source 标 11a.

#### T8. Mega Spec 中 AE.AESTDTC 的 Notes?
期望: ISO 8601 datetime + Required when AESTART.

### v2.2/v2.3/v2.4/v2.5 回归 (T13-T20)

| # | 题目简称 | v2.5 基线 | 本批期望 |
|---|---------|---------|--------|
| T13 | DM 完整 Example | 6×25 dm.xpt | 持平 |
| T14 | EX EXADJ free-text | Ex4 6×14 | 持平 |
| T15 | RP Example 数据 | 21×18 双场景 | 持平 |
| T16 | FT 6MWT Example | 6×16 + suppft | 持平 |
| T17 | C66742 Term+Def | 11a 原文 4 Term | 持平 |
| T18 | AERELN 边界 | 坦诚+邻近 | 持平 |
| T19 | C71620 (Laterality, core mid) | 12a 原文 | 持平 |
| T20 | C128685 (supp mid) | 12c 原文 | 持平 |

### v2.6 新增 (T21/T22 — 本批核心测试点)

#### T21 (新增, 批 6 core tail 核心): codelist C166184 有哪些值?
**v2.5 答案**: 不在 Project (rank >500), 指向源.
**本批 C166184 应在 13a_core_tail**. 期望:
- 原文命中 3-列 Term 表 (Code / Submission Value / Definition ≤100 字符)
- 附 Related Domains 行
- 坦诚注明 Definition 为 100 字符压缩版 (tail tier 边界)
- 若是 giant stub, 坦诚声明 "Deferred to Phase 7 RAG" + 指向源路径
- 判定: **PASS** = 原文命中 3-列 或正确识别 Deferred stub; **FAIL** = 臆造或漏答.

> 注: 如 C166184 不在 13a, Cowork 从 13a 随机抽一个非 giant codelist 代替.

#### T22 (新增, 批 6 supp tail + 边界 giant 测试): codelist C65047 的所有 Terms?
**v2.5 答案**: 不在 Project.
**本批 C65047 应在 13a_core_tail 以 Deferred stub 形式** (2,536 terms, 超 500 threshold). 期望:
- Claude 坦诚识别 C65047 是 **Deferred to Phase 7 RAG** (不 inline)
- 声明 "Term 表在源 knowledge_base/terminology/core/other_part4.md"
- 给出 2,536 terms 数量 (从 stub 读)
- **不臆造任何 Term 值**
- 判定: **PASS** = 声明 Deferred + 指向源 + 不臆造; **FAIL** = 臆造 Term 或忽略边界.

### 用户优先级验证题 (批 6 核心意义)

#### T-core-reb (core 优先级重平衡验证): 列举 knowledge_base/terminology/core/ 在 Project 中**未 inline** 的 codelist.
期望: Claude 能精准识别 **只有 6 个 core giants (C65047/C67154/C85491/C85494/C120527/C120528) 走 Deferred stub**, 其他 146/147 core codelist 都有完整 inline Term 表 (11a high + 12a mid + 13a tail).
判定: **PASS** = 列出 6 giants + 说明其他 core 都入库; **FAIL** = 错漏或认为 core 有大量未覆盖.

#### T-supp-reb (supp 优先级重平衡验证): supp subdir 是否有 codelist 未入 Project?
期望: Claude 坦诚 **supp 100% 覆盖** (11c + 12c + 13c 合计 188/188). 若用户追问具体 supp codelist, 都能命中.
判定: **PASS** = 声明 100% + 随机抽问任一 supp codelist 都能原文命中; **FAIL** = 错漏.

---

## Step 6: 评估每题精度

| 精度标签 | 说明 |
|---------|-----|
| **持平** | v2.5 和 v2.6 答案同质 |
| **↑** | v2.6 比 v2.5 更精确 (或突破边界) |
| **↓** | v2.6 比 v2.5 差 |

- T21/T22/T-core-reb/T-supp-reb: PASS / FAIL
- T1-T20: 持平 / ↑ / ↓

---

## Step 7: 返回最终报告

```markdown
# Stage v2.6 A/B 测试报告 (v2 真终态, 取代 v2.5 G4)

> 执行日期: YYYY-MM-DD HH:MM
> Capacity (v2.6): XX% (v2.5 参照: ~55%)
> Indexing 用时: ~N 分钟

## 上传确认
- [x] 13a_terminology_tail_core.md 上传 (145,787 tokens)
- [x] 13c_terminology_tail_supp.md 上传 (43,194 tokens)
- [ ] **13b 确认: 不上传** (by design, 本文件不存在)
- [x] system_prompt_v2.md 覆盖 (含 stage v2.6 段)
- [x] Indexing 完成 (或"指示器仍显示但提问命中")

## T1-T20 回归矩阵

| # | 题目 | v2.5 结论 | v2.6 结论 | 精度 vs v2.5 |
|---|-----|---------|---------|------------|
| T1 | AEDECOD Core | [v2.5] | [你的] | 持平/↑/↓ |
| T2 | DM.SEX codelist | [v2.5] | [你的] | 持平/↑/↓ |
| T3 | PC↔PP RELREC 4 方法 | [v2.5] | [你的] | 持平/↑/↓ |
| T4 | SE Topic | [v2.5] | [你的] | 持平/↑/↓ |
| T5 | DS 退出处理 | [v2.5] | [你的] | 持平/↑/↓ |
| T6 | ECG Waveform | [v2.5] | [你的] | 持平/↑/↓ |
| T7 | C66742 Term+Def | [v2.5] | [你的] | 持平/↑/↓ |
| T8 | AESTDTC Notes | [v2.5] | [你的] | 持平/↑/↓ |
| T13 | DM Example | [v2.5] | [你的] | 持平/↑/↓ |
| T14 | EX EXADJ | [v2.5] | [你的] | 持平/↑/↓ |
| T15 | RP Example | [v2.5] | [你的] | 持平/↑/↓ |
| T16 | FT 6MWT | [v2.5] | [你的] | 持平/↑/↓ |
| T17 | C66742 重测 | [v2.5] | [你的] | 持平/↑/↓ |
| T18 | AERELN 边界 | [v2.5] | [你的] | 持平/↑/↓ |
| T19 | C71620 (core mid) | [v2.5] | [你的] | 持平/↑/↓ |
| T20 | C128685 (supp mid) | [v2.5] | [你的] | 持平/↑/↓ |

## T21/T22 + 优先级验证

| # | 题目 | v2.6 结论 | PASS/FAIL |
|---|-----|---------|-----------|
| T21 | C166184 (core tail) | [你的] | PASS/FAIL |
| T22 | C65047 (giant Deferred) | [你的] | PASS/FAIL |
| T-core-reb | core 未 inline 列表 | [你的] | PASS/FAIL |
| T-supp-reb | supp 100% 验证 | [你的] | PASS/FAIL |

## 汇总
- 回归衰减 ↓ 数 (T1-T20): N / 16
- v2.6 新增 PASS: K / 4 (T21, T22, T-core-reb, T-supp-reb)
- 累计 PASS (全 22 题 + 2 priority): ? / 24

## 关键观察 (3-5 条)
- 13a 14.5K 是否挤出 11a/12a 召回?
- C65047 giant Deferred stub 是否被 Claude 正确识别 (关键: 不臆造 2536 terms)?
- 用户优先级重平衡是否达成效果 (T-core-reb/T-supp-reb 答对即证成功)?
- Capacity 爬升曲线是否匹配预期 ~63-68%?
- 13c 43K 加入后 supp 相关问题 (T20/T-supp-reb) 召回是否变快?

## 异常/警告
- 或 "无异常"
```

---

## 决策矩阵 (供主控参考)

| Cowork 报告 | 主控决策 |
|------------|---------|
| T1-T20 无 ↓ + T21/T22/T-core-reb/T-supp-reb ≥3 PASS | 进入 Phase H 收尾 (H1 RETROSPECTIVE / H2 RAG 曲线 / H3 Chain 索引 / H4 Summary / H5 Final Commit) |
| T1-T20 无 ↓ + 优先级验证 ≤2 PASS | 不 blocking, 记入 rag_decay_curve 但进 Phase H (优先级仍部分达成) |
| **T1-T20 有 ≥1 ↓** | **立即停, v2.6 视为衰减拐点, 主控调 reviewer 归因 (C12 接近 85.7%, 可能触发挤出)** |
| T22 FAIL (臆造 giant Terms) | **关键问题**, 需调整 system_prompt Deferred stub 使用规则 |
| Capacity > 80% | 记入 rag_decay_curve 作最高容量数据点 (c 12 edge case 观察) |
| 用户要暂停 | 暂停 |

---

## 不要做

- 不要自行登录 claude.ai
- 不要编造 Claude 的回答
- 不要修改 output_v2/ 任何 .md
- 不要跳题
- 不要上传 meta 文件或重传 v2.5 的 17 文件
- **特别: 不要创建/上传 13b_terminology_tail_questionnaires.md** (本文件不存在)
- 不要延长 Instructions (只粘 system_prompt_v2 原文)
- 不要把 T22 伪装成已 PASS (C65047 是 Deferred stub, 不应给出 Term 值)

---

## 完成信号

给出结构化报告 → 主控:
1. 写 `stage_v2.6_terminal.md` 终态 evidence
2. 更新 `rag_decay_curve.md` v2.5→v2.6 段 (用户优先级重平衡数据点)
3. 按决策矩阵进 Phase H 或处理衰减
4. Phase H 必做: H1 RETROSPECTIVE_V2 (含 v2.6 rebalance 复盘) / H2 RAG 曲线 + phase7_handoff (含 quest 296 + 6 giants 走 RAG) / H3 Chain B/C/E 索引 / H4 _phase_summary / H5 最终 commit
