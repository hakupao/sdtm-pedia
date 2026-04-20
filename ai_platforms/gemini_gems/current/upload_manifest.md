# Gemini Gems — Upload Manifest (Phase 3 Node 3)

> 状态: **Ready to Upload (单批即终态, PLAN §5 P11)**
> 最后更新: 2026-04-20
> 实测 tokens 来源: `dev/evidence/_progress.json` phases.3_execute.nodes.N2_scripts_run.product_stats (规则 P3, 去 `~` 前缀 = 实测)
> 总计: **1 批 = 4 文件 / 4 占用 / 10 文件硬限 / 6 spare**
> 上游 evidence: `dev/evidence/validate_all_attempt2.log` (rc=0) + `dev/evidence/step_node2_audit.md` (Rule A N=5 PASS) + `dev/evidence/phase3_node2_attempt2_ab_reviewer.md` (17/17 VERIFIED)

---

## 上传顺序

按 PLAN §3.1 position_fit + §2.4 位置策略:

1. `01_core_reference.md` — 导航层, 头部 position 0.9
2. `02_domain_specs.md` — 63 spec, 前中段 position 0.7
3. `03_domain_knowledge.md` — assumptions+examples, 中段 position 0.7
4. `04_terminology_core.md` — 高频 codelist, 尾部 position 0.9 (recency bias)

**Gemini 平台特性**: 无 RAG, 无 indexing, 上传后秒级就绪; **上传顺序影响 Gem Knowledge 列表显示顺序, 进而影响全量注入时的上下文位置** (PLAN §2.4). 因此严格按 01→02→03→04 顺序上传。

---

## 文件清单

| # | 文件 | tokens (实测) | target | deviation | sources | 主要内容 | 备注 |
|---|------|---:|---:|---:|---:|---------|------|
| 01 | `01_core_reference.md` | 124,512 | 120,000 | +3.76% | 15 | chapters (ch01-ch10) + SDTM v2.0 Model + 导航/路由层 | PASS 常态 |
| 02 | `02_domain_specs.md` | 185,785 | 168,000 | +10.59% | 63 | 63 域 spec.md (字母序) | PASS 常态 |
| 03 | `03_domain_knowledge.md` | 275,318 | 225,000 | **+22.36%** | 126 | 63 域 assumptions + examples | **WARN (用户 Q3=接受)**; 泛域召回风险 Node 5 A/B 监测 |
| 04 | `04_terminology_core.md` | 299,303 | 200,000 | **+49.65%** | 5 | 高频 codelist (lb_part2 / lb_part3 / oncology_part1 / interventions / qs_part1) | **WARN (Node 3 新增)**; V6 tail markers 3/3 (onc @795,262 / intv @884,851 / qs @974,723, 全 ≥ tail_start 777,919); Node 5 后决策扩 budget 或拆 04a/04b |

**总 tokens**: **884,918** / 900,000 WARN 阈值 / 1,000,000 HARD FAIL 阈值 (余 **15,082 tokens** 响应 buffer)

**Context window 占用**: 88.49% (884,918 / 1,000,000), 预留 11.51% 响应空间; 符合 PLAN §5 ≤900K WARN 阈, 高于原 target ≤800K 但在用户 Q3=接受决策下放行。

---

## V6 末尾召回锚点 (P12 hard checkpoint evidence)

> Phase 3 Node 3a reviewer M2 R2 升级独立段落声明 (原嵌在表格备注).

| 字段 | 值 | 说明 |
|------|---:|------|
| 总 chars | 1,111,314 | 04_terminology_core.md 产物字节数 |
| tail_start (后 30% 门槛) | **777,919 chars** (70% 位置) | V6 判定 tail_start = len × 0.7 |
| marker 1 (oncology_part1) | **795,262 chars** | tail_start + 17,343, offset 71.56% ✅ |
| marker 2 (interventions) | **884,851 chars** | tail_start + 106,932, offset 79.62% ✅ |
| marker 3 (qs_part1) | **974,723 chars** | tail_start + 196,804, offset 87.71% ✅ |
| **V6 判定** | **PASS 3/3** | 3 个 terminology source marker 全部 ≥ tail_start, 满足 PLAN §1.3 P12 要求 "≥3 段 in tail 30%" |

**意义**: 这 3 个 marker 是 smoke S3/S4 末尾召回 hard checkpoint 的物理依据; tail_start=777,919 等价于 **line 4440** (6343 行中 70% 位置). smoke S3 选 qs_part1 (tail_start 后 196K chars), S4 选 lb_part3 (落非首非尾中段约 40% 位置) 覆盖 recency vs middle 对比验证.

**来源**: `dev/evidence/validate_all_attempt2.log` + `_progress.json.phases.3_execute.nodes.N2_scripts_run.product_stats.04_terminology_core.md` (v6_tail_markers=3 / tail_start=777919).

---

## Node 2 → Node 3 carry-over (全部 Node 3b 或 Node 4+ 处理, 不本 Node 3a writer 处理)

- **MEDIUM-M1 (critic)**: `dev/scripts/merge_for_gemini.py` budget 90K → 100K (headroom 6.73% → 16.06%, 不改 selected 集合) — **Node 4 前脚本改 + 重跑 validate 确认产物 md5 稳定, 本 Node 3a 不改脚本**
- **LOW-L1 (critic)**: `dev/scripts/merge_for_gemini.py` L352-355 inline 注释 marker 顺序 stale (intv/onc → 实际 onc/intv) — **Node 4 前修, 非功能错**
- **LOW-L2 (critic)**: ChatGPT 侧 Rule A N=5 audit 未做 — **本 Node 3 主 session 当场做 (不阻塞 writer), 落 `ai_platforms/chatgpt_gpt/dev/evidence/step_node2_audit.md`**
- **LOW-WARN (AB reviewer)**: 03 +22.36% + 04 +49.65% — 用户 Q3=接受; **Node 5 A/B 专项监测 (泛域召回 + 末尾召回 T-tail)**
- **LOW-AUDIT-A1 (audit)**: `general_part1` / `is_domain_part2` 未入 selected → 泛域召回风险, Node 5 A/B 后决策是否扩 budget 到 160K; **本 manifest 登记, Node 5 跟进**
- **LOW-1 (AB reviewer)**: `dev/evidence/validate_single_batch.md` V3 判定行 "884,918 ≤ target" 描述笔误 (884K > 800K target, PASS 因 < 900K WARN 阈, rc=0 正确) — **本 Node 3 主 session 当场修, 非本 writer 职责**

---

## 上传操作步骤 (用户侧, Phase 3b 执行)

1. 访问 `gemini.google.com` (需 Google AI Pro 订阅, profile A section)
2. 左侧导航 → **"Gems"** → **"New Gem"** (或 "Create a Gem")
3. **Name**: `SDTM Expert`
4. **Description**: `CDISC SDTMIG v3.4 + SDTM v2.0 Expert — variable definitions, rule reasoning, cross-domain comparison, and terminology lookup (~140 chars)` (≤ 280 字符上限)
5. **Custom Instructions**: 打开 `current/system_prompt.md`, 全文拷贝粘贴到 Gem Instructions 输入框
6. **Knowledge**: 按**上传顺序** (01 → 02 → 03 → 04) 拖拽或点 "Add Knowledge" → 选择本地 device 路径 `ai_platforms/gemini_gems/current/uploads/0{1..4}*.md` (device 上传路径满足 profile F-5 分享条件, 未来若要 link share 无需切换)
7. **Save Gem** — Gemini 无 indexing, 秒级就绪, 不需要等 "Processing" 指示
8. 进 Gem Preview 对话框 → 按 `dev/evidence/smoke_questions_draft.md` 顺序跑 5 题 smoke
9. 回报 smoke 结果到 session, 主 session 派 Rule D reviewer + 准备 commit C3b

---

## 发布决策 (Phase 3 Node 3b 不必决, Phase F1 再决)

默认 **Private** (仅本人). Phase F1 用户 ack 后可选:
- **选项 A (推荐默认)**: 保持 Private, 仅个人深度使用
- **选项 B (可选扩展)**: "Link share with colleagues" — 定向/内部传播, 给同事 (Viewer 权限). profile E section + 2025-09-18 Sharing Gems 发布支持.

**不走 GPT Store 广播路径** — 这是 ChatGPT 平台独有 (Rule E Q1=C), Gemini 的"公开"语义 = 分享链接给同事 (CLAUDE.md + _progress.json publish_scope_semantics_clarification_2026-04-20).

---

## 原始 Merge Fragments (脚本自动 append, 保留供回溯)

<!-- merge fragment: 2026-04-20T08:55:50Z -->
## Merge run at 2026-04-20T08:55:50Z (attempt_1 — FAIL, V6 tail 0/3)

| 文件 | 源文件数 | tokens | target | 位置策略 |
|------|---------:|-------:|-------:|---------|
| 01_core_reference.md | 15 | 124,512 | ≤120,000 | 前置 (导航层防 Lost-in-Middle) |
| 02_domain_specs.md | 63 | 185,785 | ≤168,000 | 中段 (字母序, 依赖 query anchor) |
| 03_domain_knowledge.md | 126 | 275,318 | ≤225,000 | 中段 (assumptions 先, examples 后) |
| 04_terminology_core.md | 1 | 111,771 | ≤200,000 | 末尾 (recency bias + P12 hard checkpoint) |

> attempt_1 归档: `dev/evidence/failures/stage_phase3_attempt_1.md`

<!-- merge fragment: 2026-04-20T09:38:54Z -->
## Merge run at 2026-04-20T09:38:54Z (attempt_2 — PASS, V6 tail 3/3)

| 文件 | 源文件数 | tokens | target | 位置策略 |
|------|---------:|-------:|-------:|---------|
| 01_core_reference.md | 15 | 124,512 | ≤120,000 | 前置 (导航层防 Lost-in-Middle) |
| 02_domain_specs.md | 63 | 185,785 | ≤168,000 | 中段 (字母序, 依赖 query anchor) |
| 03_domain_knowledge.md | 126 | 275,318 | ≤225,000 | 中段 (assumptions 先, examples 后) |
| 04_terminology_core.md | 5 | 299,303 | ≤200,000 | 末尾 (recency bias + P12 hard checkpoint) |

> attempt_2 terminal log: `dev/evidence/merge_all_attempt2.log` + `dev/evidence/validate_all_attempt2.log` (rc=0)
