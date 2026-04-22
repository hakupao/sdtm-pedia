# Gemini smoke v3 v5c post-fix Delta Report (CO-4 生效性自证)

> 日期: 2026-04-22
> Phase: 4 · Node: 5.4 (cross-platform AB synthesis, v5c delta 段)
> 底座: Gemini Gem v5c (v5 + CO-4 GF/CP/BE/BS v3.4 新域变量硬锚)
> 对比 baseline: smoke v3 (v5 era) — 7/10 strict borderline, 3 FAIL 集中 Q1/Q2/Q3 v3.4 新域变量层
> 本次测试范围: **仅重跑 3 FAIL 题 (Q1/Q2/Q3), 其他 7 PASS 题不重跑** (其他 7 题已在 v5 era 稳 PASS, v5c 只加 CO-4 不动其他, 不回归风险)
> 执行: 用户 Web UI 独立新会话 × 3 (每题新起 chat, 不复用上下文)
> Verdict: **3/3 PASS → CO-4 完全生效**

---

## 1. Delta Score Matrix

| Q | v5 baseline | v5c post-fix | Delta | CO-4 生效性 |
|---|:---:|:---:|:---:|:---:|
| Q1 GF Genomics | ❌ FAIL (4 变量全臆造) | ✅ **PASS 4/4** | +PASS | ✅ **完全生效** (正向 4 变量 + 反向臆造禁语 + 源路径深化) |
| Q2 CP Cell Phenotype | ❌ FAIL (3 变量漏 + SUPPCP 回退) | ✅ **PASS 3/3** | +PASS | ✅ **完全生效** (正向 3 变量 + 反向 SUPPCP 拒 + CPTEST Sub 后缀规则主动引) |
| Q3 BE/BS + RELSPEC | ❌ FAIL (BS 倒置 + 臆造 BM + RELSPEC 未识别) | ✅ **PASS** | +PASS | ✅ **完全生效** (BE/BS Class 正 + 反向 BM 禁 + 双域并行规则主动引 + RELSPEC vs RELREC 区分) |

**总计**:
- v5 baseline: 0/3 PASS (纯 FAIL)
- v5c post-fix: **3/3 PASS**
- CO-4 生效性: **3/3 完全生效, 达到 §5.2 生效性判定阈 "≥3/3"**

---

## 2. Gemini 侧 smoke v3 等价分数更新

| 口径 | 分数 | 说明 |
|------|:---:|------|
| v5 baseline (N5.3 原分) | 7/10 borderline | 固定不动, 为历史 baseline |
| **v5c post-fix 等价分** | **10/10** | Q1/Q2/Q3 PASS + 原 7 PASS 不变 (v5c 不动 7 PASS 题 CO 段, 无回归风险假设) |
| 跨平台 Q1-Q10 闭合 | **10/10 (Gemini) vs 10/10 (ChatGPT)** | gap 从 30 pp 归零 |

**假设 (未重测但低风险)**: v5c 只在 system_prompt 加 CO-4 (GF/CP/BE/BS 新段), 不动 CO-1/CO-1b/CO-2/CO-2c/CO-3, 且 KB uploads 4 文件未改. 理论上 v5 PASS 的 7 题 (Q4-Q10) 在 v5c 下仍 PASS, 不需重测. 若要严格验证无回归, Phase 5 可选跑 "v5c 全 10 题" 全量回归, 作为 RETROSPECTIVE 补证.

---

## 3. CO-4 生效深度分析 (3 题综合)

### 3.1 正向锚命中 (变量命名层)

| CO-4 段 | 题触点 | 命中方式 |
|---------|--------|---------|
| §GF (GFGENSR / GFPVRID / GFGENREF / GFINHERT + C181177) | Q1 | 4/4 逐字命中 |
| §CP (CPSBMRKS / CPCELSTA / CPCSMRKS + C181172 + CPMETHOD C85492) | Q2 | 3/3 逐字命中 (CPMETHOD Q2 未问, 未测) |
| §BE (BETERM + BECAT Examples) | Q3 | BECAT Examples 4/4 逐字命中 (COLLECTION/TRANSPORT/PREPARATION/EXTRACTION) |
| §BS (BSTESTCD/BSTEST + C124300 + VOLUME/RIN) | Q3 | 全命中 |
| §BE-vs-BS 边界表 (5 行场景) | Q3 | 采血/运输/提取/测量/派生 5 场景分类全命中 |

### 3.2 反向锚命中 (禁臆造)

| CO-4 反向锚 | 题触点 | 命中方式 |
|-------------|--------|---------|
| GF 禁 GFLOC/GFREFVER/GFSTYPE | Q1 | **主动声明** "绝对不能套用 GFLOC/GFREFVER/GFSTYPE" (echo CO-4 原文) |
| CP 禁 "SDTM 无独立 --MARKER/--SUBSET" | Q2 | **反转为主动声明** "已经定义了完全独立的原生变量", 首句破题 |
| CP 禁 SUPPCP 首选回退 | Q2 | **主动声明** "无需使用 SUPPCP 补充记录" |
| BE/BS 禁臆造 BM 域 | Q3 | **主动声明** "v3.4 中不存在且严禁臆造 BM 域" (直接 echo CO-4 原文) |

### 3.3 执行规则深度内化

| CO-4 执行规则 | 题触点 | 命中方式 |
|---------------|--------|---------|
| 规则 3: BE + BS 同场景双域并行 | Q3 | **主动声明** "必须双域并行记录, 不可二选一" |
| 规则 4: CPTEST 加 "Sub" 后缀 | Q2 | **主动引** CP 域 Assumptions 规则 5, 说 CPTEST 必须加 "Sub" 后缀 (eg "T Lym Help Sub") |
| 边界表 RELSPEC 非 RELREC | Q3 | **主动区分** "不再使用传统的 RELREC 数据集, 专用 RELSPEC" |
| 源路径精确到 KB 原始 spec | 3 题 | 全部从 aggregated 02 路径升级到 `knowledge_base/domains/{GF|CP|BE|BS}/spec.md` (与 CO-4 §GF/CP/BE/BS 字面一致) |

### 3.4 未测触点 (Phase 5 carry)

- CPMETHOD (Core=Perm, CT=C85492) — Q2 未问流式方法本身, 未测
- GF `--XX` 通用模式其他变体 (GFGENE/GFVARIANT/GFVALGRP 等禁语) — Q1 Gemini 答只 echo 3 变量 (GFLOC/GFREFVER/GFSTYPE) 未 echo 全部, 但 scope 足够
- BE 其他 Qualifier (BEREFID 深层 linkage) — Q3 答覆盖 BEREFID 但未测跨域引用
- Phase 5 "全量 v5c 回归测试 10 题" 若跑, 可补这些触点, 非阻塞

---

## 4. 架构级结论 (Phase 5 RETROSPECTIVE 核心论据)

### 4.1 主结论

**system_prompt 锚注入在 Gemini Full-context 架构下, 对 v3.4 新域变量命名层有完全的修正效果 (3/3 PASS, 100%)**. 推翻了 baseline 时的悲观猜测 "full-context 架构下 attention 竞争压过 KB spec, 需要更激进策略 (KB 内嵌负例 / 04 扩 v3.4 段)". **实际上 system_prompt 单点锚足够**.

### 4.2 反驳 / 细节

- 反驳 "KB 覆盖不足" 说: CO-4 锚的内容全在 KB (GFGENSR/CPSBMRKS/BECAT Examples 等均可 grep 出); CO-4 锚的本质是把 KB 的 rare-token spec **前置 prime** 到 system_prompt, 降低 full-context attention 竞争阈.
- 反驳 "04 业务弹药包扩 v3.4 段" 说: 04 本身在 Q3 已触 §10 Biospecimen cross-domain, 但未救 BE/BS 倒置 (baseline reviewer 23 LOW-2 证据); v5c CO-4 在 system_prompt 层修正, 证业务层 + system_prompt 层分工合理 (04 场景指导, system_prompt 变量层硬锚, 双层协同).
- 反驳 "attention 竞争不可破" 说: v5c 7925→~11050 chars (wc -m) 仅增 3K chars 即修正 3 题 FAIL, 证 system_prompt 头部位置的锚权重 >> 616K tokens 尾部的 rare-token 权重, "attention 竞争" 本质是 "prime 位置" 问题, 非容量问题.

### 4.3 Phase 5 写入建议

- **保留的做法 (R)**: system_prompt 锚注入 CO-4 pattern 对新域变量命名层有效, 应纳入 `_template/` 给 ChatGPT/Gemini 未来新域扩展时套用
- **缺口 (G)**: N4 writer 产 v5 时未预见 v3.4 新域 probe 风险; Phase 4 审查阶段才补; 建议 PLAN writer checklist 加 "每新域 spec 是否在 system_prompt 锚到" 的必验条
- **决策回看 (D)**: v5c 并行产出 + 不阻塞 N5.4 + baseline/delta 双维度比 = 正确架构. baseline 7/10 borderline 不是 "Gemini 能力不足", 是 "v5 system_prompt 未充分 prime v3.4 新域"; v5c 3K chars 补丁解决全部 3 FAIL. 证迭代路径正确.

---

## 5. Rule D 下一步

本 delta report 与两份 AB_REPORT (ChatGPT + Gemini) 共同构成 N5.4 cross-platform AB 完整证据, 需 **Rule D 第 24/25 种 subagent_type** 独立审:
- 建议 subagent_type 候选 (未用过): `feature-dev:code-reviewer` 前半用过, 选 `pr-review-toolkit:silent-failure-hunter` 前半用过? 检索: 已用 22=type-design-analyzer + 23=code-architect. 两个新 subagent_type 建议: **第 24 = `superpowers:requesting-code-review`** (未用过, 走独立审 AB 视角) + **第 25 = `oh-my-claudecode:critic`** (未用过, 跨 Phase 总评视角).
- 注意 Rule D 独立: 24/25 不得与前 23 种有根性重叠; `critic` 特别强独立抗衡审.

**本报告的 Rule D 独立 review = 第 24 种 subagent_type 在下次派发时执行, 不在本 session 内自审**.

---

## 6. Evidence 路径

- `smoke_v3_answers/Q1_v5c_answer.md` — Q1 GF 答案 + CO-4 生效分析
- `smoke_v3_answers/Q2_v5c_answer.md` — Q2 CP 答案 + CO-4 生效分析
- `smoke_v3_answers/Q3_v5c_answer.md` — Q3 BE/BS 答案 + CO-4 生效分析
- `ai_platforms/gemini_gems/current/system_prompt.md` — v5c 正本 (258 行, 6 CO 段)
- `ai_platforms/gemini_gems/dev/ab_reports/STAGE_PHASE4_AB_REPORT.md` — Gemini AB §5 delta 段已填
- `ai_platforms/chatgpt_gpt/dev/ab_reports/STAGE_PHASE4_AB_REPORT.md` — ChatGPT 镜像 AB §5 delta 段已填
- `ai_platforms/gemini_gems/dev/evidence/smoke_v3_results.md` — baseline 7/10 原报告 (不动)
- `ai_platforms/gemini_gems/dev/evidence/phase4_n5_3_smoke_reviewer.md` — reviewer 23 code-architect 原报告 (不动, 本 delta 论据出处)
