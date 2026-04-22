# NotebookLM Phase 3 P3.4 — Indexing smoke N=10 用户+Claude cowork 手顺

> **Node**: Phase 3 P3.4 (42 tile 全扫预览 + 10 题分布式问答 citation 精确回指)
> **前置**: P3.3 完成 (Custom mode active + H3 VERIFIED PASS + F-1 CLOSED, 2026-04-21)
> **执行者**: 用户 (Web UI 操作) + Claude cowork session (题设计 / 评分 / evidence 落盘 / _progress 更新)
> **估时**: ~1.5 h (42 tile 速扫 ~15 min + 10 题 Chat 问答 ~45 min + 评分 + evidence 落盘 ~30 min)
> **Checkpoint 级别**: **HARD** (silent fail 防线 + RAG 检索精度双验证, 不过 gate 不进 P3.4.5/P3.5/P3.6/P3.7)
> **下游**: P3.4.5 (Req 变量业务问答 N=10, Q1 红线**语义级**自证, Rule A 正本)
> **PLAN 引用**: `docs/PLAN.md` §6 P3.4 (M3 fix + S2 fix)
> **Evidence 归档**: `dev/evidence/indexing_smoke.md` (本手顺末尾模板)

---

## 背景 (≤300 字)

P3.2 完成 42/42 indexed + 5 tile 速览 PASS + Chat sanity (STUDYID Core=Req + citation) PASS.
P3.3 完成 Custom mode 激活 + H3 三档 per-chat-session 切换 VERIFIED PASS, 附带 finding F-1 (UI 表格渲染) 已 CLOSED (`minimal table test` 分支 a 命中, 归因模型偶发 single-line malformed 漂移, 不改 instructions.md), F-2 (同题 retry 非幂等) 挪 P3.8 A/B 评分规则.

**P3.4 目标**: 把 "42 source 全都 indexed 且 RAG 检索能精确回指每个 bucket" 作为 gate 锁死. 具体两件事:

1. **sub (a) 42-tile 全扫预览** — silent fail 第一道防线, 确认每个 tile 都有 metadata header + 正文可读 + 无截断.
2. **sub (b) 10 题分布式问答** — RAG 检索第二道防线, 题目精心挑选, 每题有**唯一期望 source bucket**, 看模型 citation 是否**精确回指**. M3 fix 要求 N=10 (不是 v1 的 N=3), S2 fix 要求至少 1 题打在 non-core domain (DD/HO/ML/BE/SS/UR/NV/FT 等 findings_other bucket 18-22 的冷区).

PASS 阈值: sub (a) 42/42 tile 无异常 AND sub (b) ≥9/10 citation 精确回指 (10/10 目标, ≥9 可接受). <8/10 触发 Phase A A3 cluster bucket 回炉 (红 path, 非预期).

**P3.4 不做的**: Req 变量业务问答 N=10 (挪 P3.4.5, 规则 A 正本) / Audio / Mind Map / Study Guide / A/B 15 题 / 分享档位切换.

---

## 环境固定参数

| 字段 | 值 |
|------|----|
| Notebook URL | https://notebooklm.google.com/notebook/3f87a93e-9a65-407e-8292-c28706fc6287 |
| Notebook name | `SDTM Knowledge Base` |
| 账号 | `bojiang.zhang.0904@gmail.com` (personal Gmail, Rule E ack) |
| Tier | Pro (Google AI Pro, PRO 徽章已见) |
| Source 数 | 42 (03 处锁定: My notebooks 卡片 / Chat 底部 / Studio 生成器) |
| Chat mode | Custom (instructions.md 9,011 chars, P3.3 已 Save) |
| instructions.md 快照 | `ai_platforms/notebooklm/current/instructions.md` |
| Uploads MANIFEST | `ai_platforms/notebooklm/current/uploads/MANIFEST.md` |

---

## 前置检查 (开工前 2 min, cowork session 跑)

cowork Claude 接手后, 先跑这 4 条, 全 PASS 才开始:

```bash
# 1. 确认分支干净 (或至少无 uploads/ 意外改动)
git -C /Users/bojiangzhang/MyProject/SDTM-compare status --short
# 期望: 干净, 或最多只有 .work/ evidence 类改动

# 2. 确认 42 个 uploads md 未变 (P3.2 基线锁定)
ls /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/notebooklm/current/uploads/*.md | wc -l
# 期望: 42

# 3. 确认 MANIFEST 顶栏仍是 42
head -10 /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/notebooklm/current/uploads/MANIFEST.md
# 期望: 含 "上传文件数: 42"

# 4. 确认 instructions.md 未变 (Custom mode 文本基线)
wc -c /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/notebooklm/current/instructions.md
# 期望: ~9011 chars (± 20)
```

任一 FAIL → 停工, 回报主 session. 不进 P3.4.

---

## Step 1: sub (a) 42-tile 全扫预览 (~15 min, 用户执行)

### 1.1 打开 notebook

浏览器打开上方 Notebook URL, 登录 `bojiang.zhang.0904` 账号 (若 qq531458594 为默认, 头像下拉切账号). Sources 面板应显示 `42 sources`.

### 1.2 清单扫描 (42/42)

**用户动作**: 从 Sources 面板顶部往下, **每个 tile 都点开**看预览. 对每个 tile 勾 3 件事:

- [ ] **Metadata header**: 顶部应有 `# <bucket 名>` + `**Concept:**` + `**Bucket id:**` + `**Sources:**` (或类似 Source guide 自动生成的 metadata)
- [ ] **正文可读**: 非空白, 无乱码, 无明显截断 (特别关注 bucket 38 / 39 / 36 这几个 >150K words 的大 bucket)
- [ ] **Source guide**: NotebookLM 自动生成的摘要区应有内容 (不是 "Generating..." 卡住)

**清单** (对照 `current/uploads/MANIFEST.md` 顺序):

| # | Bucket | Words | 预览结果 (PASS / FAIL + 备注) |
|---|--------|------:|-------------------------------|
| 01 | `01_navigation_and_routing.md` | 2,145 | |
| 02 | `02_common_identifiers_and_timing.md` | 1,080 | |
| 03 | `03_sp_demographics_subject.md` | 10,619 | |
| 04 | `04_sp_se_sm_sv_co.md` | 9,417 | |
| 05 | `05_int_exposure_ex_ec.md` | 14,426 | |
| 06 | `06_int_concomitant_cm_ag_ml.md` | 11,070 | |
| 07 | `07_int_procedures_pr_su.md` | 6,168 | |
| 08 | `08_ev_adverse_ae.md` | 7,354 | |
| 09 | `09_ev_disposition_ds_dv_ce.md` | 13,732 | |
| 10 | `10_ev_history_mh_ho_be.md` | 11,141 | |
| 11 | `11_fnd_lab_lb.md` | 5,863 | |
| 12 | `12_fnd_vitals_vs_eg.md` | 9,238 | |
| 13 | `13_fnd_physical_exam_pe.md` | 2,147 | |
| 14 | `14_fnd_questionnaire_qs_ie.md` | 5,033 | |
| 15 | `15_fnd_biomarkers_mb_mi_ms_mk.md` | 19,585 | |
| 16 | `16_fnd_pharma_pc_pp.md` | 18,039 | |
| 17 | `17_fnd_oncology_tr_tu_rs_oe.md` | 22,769 | P3.2 已速览 PASS, 速扫再确认 |
| 18 | `18_fnd_device_da_dd_gf_is.md` | 22,622 | **关键 non-core bucket, 重点看** |
| 19 | `19_fnd_morphology_bs_cp_cv.md` | 16,007 | |
| 20 | `20_fnd_about_fa_sr.md` | 10,739 | |
| 21 | `21_fnd_other_nv_re_rp.md` | 10,817 | |
| 22 | `22_fnd_other_ss_ur_ft.md` | 7,649 | **关键 non-core bucket, 重点看** |
| 23 | `23_td_arms_ta_tv.md` | 9,078 | |
| 24 | `24_td_elements_te_tm_td.md` | 5,656 | |
| 25 | `25_td_meta_ti_ts_oi.md` | 7,498 | |
| 26 | `26_rel_relrec_relspec_relsub.md` | 3,627 | |
| 27 | `27_rel_suppqual.md` | 1,835 | |
| 28 | `28_ig_ch01_ch02_ch03.md` | 6,751 | |
| 29 | `29_ig_ch04_general_assumptions.md` | 20,315 | P3.2 已速览 PASS |
| 30 | `30_ig_ch08_ch10.md` | 12,933 | |
| 31 | `31_model_obs_classes.md` | 6,596 | |
| 32 | `32_model_concepts_study_rel.md` | 5,801 | |
| 33 | `33_ct_general.md` | 98,051 | 大 bucket, 注意看首末段无截断 |
| 34 | `34_ct_lb.md` | 129,606 | 大 bucket, 同上 |
| 35 | `35_ct_findings_eg_qs_vs_mi_ae_dispo.md` | 83,907 | 大 bucket, 同上 |
| 36 | `36_ct_specialized_micro_oncology_pk_is_cp.md` | 162,073 | **大 bucket, 32% of 500K cap, 重点看** |
| 37 | `37_ct_misc_int_dm_sp_td_gf_oi_other.md` | 88,232 | |
| 38 | `38_ct_questionnaires_part1_22.md` | **302,027** | P3.2 已速览 PASS, **最大 bucket (60% of cap)** 再确认 |
| 39 | `39_ct_questionnaires_part23_43.md` | 291,941 | **接近最大 bucket, 重点看** |
| 40 | `40_ct_supplementary.md` | 75,907 | |
| 41 | `41_variable_index.md` | 27,758 | |
| 42 | `42_req_variable_coverage_audit.md` | 4,833 | P3.2 已速览 PASS |

**任一 FAIL 处理**:
- 空白 / 乱码 → 该 source 删, 单文件重传, 归档 `dev/evidence/failures/task_p3_4_attempt_<X>.md` (规则 B)
- Source guide 生成卡死 → 等 5 min, 仍卡升级 blocker, 回报主 session
- 大 bucket (38/39/36/34/33) 明显截断 → 拆 bucket (Phase A A3 回炉), **P3.4 红灯停**

### 1.3 落盘 sub (a) 结果

cowork Claude 收到用户填完的表 (或截屏 + 口头 "全 PASS") 后, 把结果总结到本手顺 Step 5 的 evidence 模板.

**Sub (a) PASS 判据**: 42/42 均无 FAIL.

---

## Step 2: sub (b) 10 题分布式问答 (~45 min, 用户 Chat 问, cowork 评分)

### 2.1 题库设计原则 (已预设, 用户 / cowork 不需再设计)

10 题遵守 PLAN §6 P3.4 (M3 + S2 fix) 规则:

- **首**: bucket 01 覆盖 1 题
- **末**: bucket 42 覆盖 1 题
- **中间 8 题**: 从 bucket 02-41 挑, 每题打**唯一期望 source**, 覆盖核心域 + non-core 域 + IG + CT + relationships + trial design
- **至少 1 题 non-core domain**: 本手顺预设 **2 题 non-core** (Q05 DD + Q06 SS, 双保险)
- **每题 PASS 判据**: 答案**内容正解** AND **inline citation 精确回指期望 source** (允许同时回指 1-2 个邻近 bucket, 但主期望 bucket 必须命中)
- **F-1 tolerance**: 若答案出现 single-line malformed pipe-table, **不因格式判 FAIL**, 只看**语义 + citation** (F-1 已 CLOSED, 接受模型偶发漂移; 若 10 题中 >3 题 malformed, 记录**频率**但不扣分)

### 2.2 10 题全文 (用户在 Chat 逐题原文问, 禁改字)

> ⚠️ **重要**: 每题开**新 chat session** 或至少 **clear 前题上下文** (避免 RAG chunk 窗口污染). Custom mode 保持激活.

---

#### Q01 [bucket 01 — 首 source]

**题**:
```
这个 SDTM 知识库 notebook 覆盖多少个 domain? 导航总入口和 Req 变量速查入口分别在哪个 source?
```

**期望 citation**: `[01_navigation_and_routing.md]` (主) + 允许附带 `[42_req_variable_coverage_audit.md]` (Req 速查)

**PASS 判据**:
- 答 63 domain (或 63/63)
- 导航入口明确回指 `01_navigation_and_routing.md`
- citation **精确回指 bucket 01** 作 primary source

**FAIL 判据**:
- 不提 63 domain (或错数)
- citation 只回指其他 bucket, 完全不引 01

---

#### Q02 [bucket 08 — AE 核心域]

**题**:
```
AE 域的 Core=Req 变量集合包含哪些? 请按 instructions.md 的 variable table 格式给出.
```

**期望 citation**: `[08_ev_adverse_ae.md]` (主)

**PASS 判据**:
- 列出 6 个 Req: STUDYID / DOMAIN / USUBJID / AESEQ / AETERM / AEDECOD
- AEDECOD CT=MedDRA
- citation 精确回指 `08_ev_adverse_ae.md`

**FAIL 判据**:
- 漏 Req (e.g., 丢 AESEQ 或 AEDECOD)
- 把 AESER 误列 Req (AESER 是 Exp, instructions.md 规则 5)
- citation 指向其他域 bucket

---

#### Q03 [bucket 11 — LB 核心域 + F-1 漂移窗口]

**题**:
```
LB 域的 LBNRIND 变量取值集合是什么? 给出 C-code 和各值的语义.
```

**期望 citation**: `[34_ct_lb.md]` (主, CT 源) + 允许附带 `[11_fnd_lab_lb.md]` (LB spec)

**PASS 判据**:
- 全写: **HIGH / LOW / NORMAL / ABNORMAL** (instructions.md 规则 6, 禁 H/L/N 短码)
- C-code: **C78736**
- citation 精确回指 `34_ct_lb.md` 或 `11_fnd_lab_lb.md` 其一 (两者都允许 PASS)

**FAIL 判据**:
- 写 H/L/N 短码
- C-code 错或缺
- citation 指向无关 bucket

---

#### Q04 [bucket 29 — IG ch04 权威规则]

**题**:
```
SDTMIG v3.4 关于 Study Day 的规则是什么? Day 1 和 Day 0 是否同义?
```

**期望 citation**: `[29_ig_ch04_general_assumptions.md]` (主, ch04 是 authoritative 源)

**PASS 判据**:
- Day 1 = 第一剂日 (first dose day)
- **明确说无 Day 0** (instructions.md 规则 9)
- Day 1 前为 -1, -2, ...
- citation 精确回指 `29_ig_ch04_general_assumptions.md`

**FAIL 判据**:
- 说 Day 0 = 第一剂日
- citation 指向其他 IG bucket (ch01/02/03 或 ch08/10)

---

#### Q05 [bucket 18 — DD non-core domain ★ S2 fix 必跑]

**题**:
```
DD (Death Details) 域用来记录什么? 请给出该域的 Topic 变量 (--TESTCD / --TEST 类) 及其 Core 属性.
```

**期望 citation**: `[18_fnd_device_da_dd_gf_is.md]` (主, DD 在 findings_device 合并 bucket)

**PASS 判据**:
- DD 用于记录死亡详情 (death details / cause of death finding)
- 指出 DDTESTCD / DDTEST 是 Topic, Core 属性 (Req 或根据 spec)
- citation **精确回指 bucket 18**

**FAIL 判据**:
- "未收录" (RAG 在 non-core bucket 召回失败, **严重信号**, 触发 P3.4 红灯)
- citation 指向 DM 或其他错 bucket
- 臆造变量名

---

#### Q06 [bucket 22 — SS non-core domain ★ S2 fix 双保险]

**题**:
```
SS (Subject Status) 域的用途是什么? 它和 DS (Disposition) 域的区别在哪?
```

**期望 citation**: `[22_fnd_other_ss_ur_ft.md]` (主, SS) + 允许附带 `[09_ev_disposition_ds_dv_ce.md]` (DS 对比)

**PASS 判据**:
- SS = Subject Status, 记录受试者在特定时间点的状态 (findings 类, 周期性采集)
- DS = Disposition, 记录受试者试验处置事件 (events 类, 一次性)
- **citation 必含 bucket 22** (SS 主 source)

**FAIL 判据**:
- 把 SS 当 events 类
- citation 只回指 DS bucket, 不引 22

---

#### Q07 [bucket 26 — Relationships]

**题**:
```
RELREC 和 RELSPEC 的区别是什么? 分别用于什么关联场景?
```

**期望 citation**: `[26_rel_relrec_relspec_relsub.md]` (主) + 允许附带 `[30_ig_ch08_ch10.md]` (IG ch08 关系章)

**PASS 判据**:
- RELREC = 跨域或同域跨记录的 record-to-record 关系 (键 RELID/RELTYPE)
- RELSPEC = specimen-to-specimen 关系
- citation **精确回指 bucket 26**

**FAIL 判据**:
- 混淆二者用途
- citation 指向 SUPPQUAL (27) 或其他

---

#### Q08 [bucket 38 — 大 bucket 边界 CT questionnaires]

**题**:
```
SDTM CT 中 AJCC 分期问卷 (tumor staging) 对应的 codelist 属于哪类? notebook 里这个内容在哪个 source?
```

**期望 citation**: `[38_ct_questionnaires_part1_22.md]` (主, AJCC 属于 questionnaires part 1-22)

**PASS 判据**:
- AJCC 属于 CT questionnaires (临床术语问卷类 codelist)
- citation **精确回指 bucket 38** (302K 最大 bucket, 边界测试)

**FAIL 判据**:
- 把 AJCC 归入 CT core 或 CT specialized
- citation 指向 bucket 36 (specialized oncology) 或其他
- 注: 若答 "未收录" 且模型解释 "302K 超出 context", **记红 flag** (大 bucket indexing 可能有问题)

---

#### Q09 [bucket 41 — VARIABLE_INDEX]

**题**:
```
SDTMIG v3.4 里总共有多少个变量? VARIABLE_INDEX 在哪个 source?
```

**期望 citation**: `[41_variable_index.md]` (主)

**PASS 判据**:
- 1,523 变量 (instructions.md 首段原文)
- citation **精确回指 bucket 41**

**FAIL 判据**:
- 变量总数错 (非 1,523 ± 少许)
- citation 指向 01 或其他 bucket

---

#### Q10 [bucket 42 — 末 source, Req 审计元 source]

**题**:
```
这个 notebook 里独立 Req 变量总数是多少? "Req 变量零漏集" 的断言原文在哪?
```

**期望 citation**: `[42_req_variable_coverage_audit.md]` (主)

**PASS 判据**:
- 176 独立 Req 变量 (9 通用 + 167 领域专属)
- "零漏集" / "∅ gap" 原文引用
- citation **精确回指 bucket 42**

**FAIL 判据**:
- 答 100-120 (PLAN 旧估, 实际 176)
- citation 指向其他 bucket

---

### 2.3 评分规则

- 每题 **0 / 0.5 / 1** 三档:
  - **1.0 PASS**: 内容正解 + citation 精确回指期望 bucket
  - **0.5 PARTIAL**: 内容正解但 citation 指向邻近 bucket (只限题中明示 "允许附带" 的情形, e.g., Q03 回指 bucket 11 而非 34 仍算 1.0; 但若 Q08 回指 bucket 36 而非 38 只算 0.5)
  - **0.0 FAIL**: 内容错 OR citation 完全错位 OR "未收录"
- 总分 / 10

### 2.4 Exit 阈值

| 总分 | 处置 |
|------|------|
| **10/10** | 目标值, **P3.4 sub (b) 直接 PASS**, 进 P3.4.5 |
| **9/10** | 可接受 PASS, 记录 0.5 题具体细节, 进 P3.4.5 |
| **8/10** | CONDITIONAL_PASS, 主 session 评估 0.5/FAIL 题是否集中 (某 bucket 多次出错?), 决定是否回 Phase A A3 |
| **<8/10** | **FAIL_REWORK**, 系统性问题, 触发 `cluster_req_variables.py` 重跑 + bucket 边界调整, P3.4 红灯回炉 |

### 2.5 F-1 漂移 / F-2 幂等性统计

顺手记录 (**不影响 PASS 判定**, 为 P3.8 A/B 评分规则做信号):
- 10 题中多少题出现 single-line malformed pipe-table? (预期 ≤3 题, >3 回报主 session)
- 10 题中多少题给出 follow-up 反问? (Custom mode 规则 12)

---

## Step 3: 落盘 evidence (~15 min, cowork 执行)

cowork Claude 创建 `ai_platforms/notebooklm/dev/evidence/indexing_smoke.md`, 按下面模板填:

```markdown
# Phase 3 P3.4 — Indexing smoke N=10

> **日期**: <YYYY-MM-DD HH:MM>
> **执行者**: 用户 (Web UI 问答) + cowork Claude (设计/评分/落盘)
> **Notebook**: SDTM Knowledge Base (42/42 indexed, P3.2 基线)
> **Chat mode**: Custom (instructions.md 9,011 chars, P3.3 Save 后未动)
> **前置 commit**: <执行前 git rev-parse HEAD 的 7 位>
> **手顺**: dev/checkpoints/CHECKPOINT_P3.4_HANDOFF.md

---

## Step 1 sub (a): 42-tile 全扫预览

| 总 tile 数 | 异常数 | 大 bucket (>150K) 重点核验 | 结论 |
|-----------|-------|----------------------------|------|
| 42 | <N> | 33/34/35/36/38/39 全 PASS / 列 FAIL | PASS / FAIL |

**异常详情** (如无填 "无"):
- <Bucket 编号>: <现象> → <处置 (retry / 归档 / 升级 blocker)>

---

## Step 2 sub (b): 10 题分布式问答

| Q | Bucket | 期望 citation | 用户答案摘录 (≤80 字) | 实际 citation | 内容正解? | Citation 精度? | 分 |
|---|--------|--------------|----------------------|---------------|----------|---------------|----|
| Q01 | 01 | [01_navigation...] | "本 notebook 覆盖 63 domain..." | [01][42] | ✅ | ✅ 精确 | 1.0 |
| Q02 | 08 | [08_ev_adverse_ae...] | | | | | |
| Q03 | 11 or 34 | [34_ct_lb] (或 11) | | | | | |
| Q04 | 29 | [29_ig_ch04...] | | | | | |
| Q05 | 18 | [18_fnd_device...] ★ non-core | | | | | |
| Q06 | 22 | [22_fnd_other_ss...] ★ non-core | | | | | |
| Q07 | 26 | [26_rel_relrec...] | | | | | |
| Q08 | 38 | [38_ct_questionnaires...] ★ 大 bucket | | | | | |
| Q09 | 41 | [41_variable_index] | | | | | |
| Q10 | 42 | [42_req_variable...] | | | | | |

**总分**: <N> / 10

**Non-core bucket 命中** (Q05 + Q06): <PASS / FAIL 计数>
**大 bucket 38 命中** (Q08): PASS / FAIL — 关键 indexing 边界信号

**F-1 漂移统计**: <N> / 10 题出现 single-line malformed (F-1 已闭合, 只记录不扣分)
**F-2 幂等性抽查** (可选, 同题问 2 次看语义漂移率): <若跑了填, 未跑填 N/A>

---

## Step 3: Exit 决策

- Exit 阈值命中: PASS / CONDITIONAL_PASS / FAIL_REWORK
- 失败 / PARTIAL 题归因:
  - Q<N>: <具体原因 — bucket 设计 / RAG 召回 / instructions.md 约束 / 其他>

## Rule 合规自检

| Rule | 状态 |
|------|------|
| A 语义抽检 | N/A (Rule A 正本在 P3.4.5 N=10 Req 业务问答, 本步 N=10 是 indexing smoke 非压缩/改写抽检) |
| B 失败归档 | 失败 tile / 失败题若有, 归档 `failures/task_p3_4_attempt_<X>.md` / 无失败填 ✅ |
| D 写审分离 | P3.4 UI + cowork 评分, 不占 Rule D 链 subagent_type slot (cumulative 保持 9) |
| E 用户优先级 | personal Gmail + Pro + Web UI 全生效 ✅ |

## 下游 handoff

P3.4 hard checkpoint 状态: PASS / CONDITIONAL_PASS / FAIL

如 PASS → 进 P3.4.5 (Q1 红线**语义级**自证, Rule A 正本 N=10 Req 业务问答)
如 CONDITIONAL_PASS → 主 session 评估是否补题 / 进 P3.4.5
如 FAIL → 回 Phase A A3 cluster bucket 重跑 + 归档 attempt_<X>

---

*evidence 落盘日期: <YYYY-MM-DD>. 来源: 用户 Web UI 问答 + cowork Claude 评分 + 本手顺 §2.2 十题原文 + instructions.md 判据对照.*
```

---

## Step 4: 更新 _progress.json + git commit (~10 min, cowork 执行)

cowork Claude 在 evidence 落盘后做:

### 4.1 更新 `dev/evidence/_progress.json`

在 `phase_states.3_execute` 下添加 `p3_4_completion` 节点 (紧接现有 `p3_3_completion`):

```json
"p3_4_completion": {
  "date": "<YYYY-MM-DD>",
  "executor": "user (Web UI 42-tile preview + 10 Q&A) + cowork Claude (design/scoring/evidence)",
  "evidence": "dev/evidence/indexing_smoke.md",
  "sub_steps": {
    "a_42_tile_preview": "PASS (42/42 no anomaly) / FAIL with detail",
    "b_10_question_smoke": {
      "total_score": "<N>/10",
      "non_core_bucket_hits": "<Q05 DD + Q06 SS PASS/FAIL>",
      "large_bucket_38_hit": "<Q08 PASS/FAIL, 大 bucket indexing boundary signal>",
      "f_1_malformed_drift_count": "<N>/10",
      "exit_verdict": "PASS / CONDITIONAL_PASS / FAIL_REWORK"
    }
  },
  "rule_compliance": {
    "rule_A_note": "Rule A 正本在 P3.4.5 N=10 Req 业务问答, P3.4 sub (b) N=10 是 indexing smoke 非压缩抽检",
    "rule_B_failures_dir_empty": true,
    "rule_D_chain_unchanged_9": "P3.4 是 UI 工具级 + cowork 评分级, 不占 subagent_type slot",
    "rule_E_personal_gmail_pro_webui": "PASS"
  },
  "carry_over_to_p3_4_5": [
    "若 Q05/Q06 non-core bucket PASS, 为 P3.4.5 Req 语义抽检提供先验信心 (findings_other bucket 的 RAG 召回能过关)",
    "若 Q08 大 bucket 38 PASS, 证明 302K bucket indexing 未截断, P3.4.5 可选取 questionnaires 类 Req 变量入抽检池"
  ],
  "ready_for_p3_4_5": true
}
```

同时把 `current_phase` 从 `3_execute_p3.3_done_ready_for_p3.4` 改为 `3_execute_p3.4_done_ready_for_p3.4.5`, `last_update` 改 `YYYY-MM-DD_phase3_p3.4_done_ready_for_p3.4.5`, `phase_states.3_execute.status` 改 `p3_4_done_ready_for_p3_4_5`, `phase_3_entry_gate_status` 更新.

### 4.2 失败路径处置

若 Exit = FAIL_REWORK:
- 在 `_progress.json` 加 `phase_a_rework_triggered: true` + 原因
- 回主 session 决策, **不**自动跑 `cluster_req_variables.py` (需人工 ack bucket 调整方向)

### 4.3 Git commit (如 PASS 且用户 ack)

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare
git add ai_platforms/notebooklm/dev/evidence/indexing_smoke.md ai_platforms/notebooklm/dev/evidence/_progress.json
git status  # 确认只有这两文件
git diff --cached --stat  # 预审
git commit -m "$(cat <<'EOF'
Phase 6.5 NotebookLM: Phase 3 P3.4 完成 (indexing smoke N=10 PASS)

42-tile 全扫预览 42/42 + 10 题分布式问答 <N>/10 PASS (含 2 non-core bucket hit + 大 bucket 38 边界验证 PASS). P3.4.5 Req 语义抽检 gate OPEN.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

**不**自动 push, 等用户 ack 后再推.

---

## 失败回退决策树

| 症状 | 判定 | 动作 |
|------|------|------|
| sub (a) 某 tile 空白 / 乱码 | indexing silent fail (官方承认) | 删该 source + 单文件重传; 归档 `failures/task_p3_4_attempt_<X>.md` (规则 B) |
| sub (a) 大 bucket (38/39/36) 明显截断 | 500K cap 附近边界破 | **红灯停**, 回 Phase A A3 拆 bucket; **不跑** sub (b) |
| sub (b) 某题 "未收录" | 该 bucket RAG 召回失败 | 记 FAIL; 若 >2 题 "未收录", 触发 cluster 回炉 |
| sub (b) non-core bucket (Q05/Q06) 两题都 FAIL | findings_other 信号弱 | CONDITIONAL_PASS 最多; 回主 session 评估是否为这些 bucket 做 instructions.md 补强 (加 SS/DD 识别提示) |
| sub (b) 大 bucket 38 (Q08) FAIL 且答 "超出上下文" | 302K bucket 可能未完整 indexed | **红灯**, 主 session 决策拆 38/39 |
| sub (b) F-1 漂移 >5/10 题 | 模型输出格式稳定性差 | **不扣 PASS 分**, 但记录到 P3.8 A/B 风险条; 如 >8/10, 主 session 微调 instructions.md |
| 答案 citation 用了不存在的 bucket 名 | 模型幻觉 | FAIL 该题; 若 >1 题发生, 检查 instructions.md 规则 2 是否被压过 |
| 同 chat session 问到第 5-6 题后模型 "遗忘" 早期规则 | Chat context window 压力 | 开**新 chat session** (Custom mode 仍在), 续问剩余题 |

---

## 不在 P3.4 scope (明示)

P3.4 **只做** indexing smoke + RAG 精度两件事. 以下全挪下游:

- ❌ Req 变量业务问答 N=10 (Q1 红线**语义级**自证, Rule A **正本**) → **P3.4.5**
- ❌ Audio Overview × 3 (SAFETY / EFFICACY / PK Deep Dive) → **P3.5**
- ❌ Mind Map 生成 + 63 域 checklist → **P3.6**
- ❌ Study Guide × 3 (AE/LB/CM) → **P3.7**
- ❌ A/B 15 题 (10 SMOKE v2 + 5 独有) → **P3.8**
- ❌ 3 档分享切换演练 (Restricted / Anyone with link / Public / 回 Restricted) → **P3.9**
- ❌ F-2 同题 retry 幂等性补规则 → **P3.8 A/B 评分规则**
- ❌ `_template/` 11 条补丁 PR → **Phase 5**

**P3.4 只关注**: 42-tile 全 PASS + 10 题 ≥9/10 citation 精确回指.

---

## Rule D 合规说明

本 P3.4 是**用户 UI 工具级 + cowork 评分级动作**, 非 Writer / Reviewer 级产物, **不占用 Rule D 链 subagent_type slot**. cumulative 链保持 **9 种**.

下一 slot (**第 10 种 subagent_type**) 仍留给:
- P3.4.5 Req 语义抽检的独立 reviewer (若主 session 决定派 subagent 复核), 或
- Phase 4 跨平台对比的独立 reviewer.

**cowork Claude 必读**: 你的角色是**执行 + 评分**, 不是 Rule D reviewer. 评分基于本手顺 §2.2 预设判据, 不是独立 subagent_type 审核. 若评分过程发现判据本身有问题 (e.g., Q03 "允许附带" 宽容度不对), **上报主 session**, 不自作主张调整判据.

---

## 关联 Rule E / Q1 / Q2 / F-1 / F-2

| 关联项 | 本步执行要点 |
|--------|-------------|
| Rule E (personal Gmail + Pro + Web UI) | Step 1.1 确认账号 + tier, 非 Workspace/EDU |
| Q1 红线 (0 Req 丢失) | 本步**不**跑 Q1 语义自证 (挪 P3.4.5), 但 Q02/Q05/Q06/Q10 顺手测了**部分** Req 变量的 RAG 召回, 为 P3.4.5 提供先验 |
| Q2 质量第一 | 10 题逐题问, 不赶进度; 大 bucket (38) 若 indexing 卡, 优先等完再跑题 |
| F-1 (CLOSED) | 接受偶发 single-line malformed; 只看语义 + citation, 格式漂移**不扣分** |
| F-2 (待 P3.8) | 不在本步处理; 若顺手观察到同题 retry 漂移, 记一条 signal |

---

## 给 cowork Claude 的额外提示

1. **不要改 `instructions.md`** — P3.3 已锁定, F-1 已决定不改. 若 P3.4 中发现新的 instructions.md 问题, 记录到 evidence 的 "finding" 段, 交主 session 决策, **不自己 edit**.

2. **不要改 `uploads/*.md`** — P3.2 已锁定 42 基线. 若某 bucket 发现内容问题, 挪 Phase A A3 回炉路径 (红 path).

3. **不要自作主张派 subagent_type** — P3.4 不走 Rule D 链扩展. 若发现需要独立 reviewer, 回报主 session 决策派哪个 subagent_type.

4. **题目原文不能改字** — 用户必须**复制粘贴** §2.2 的 10 题, 不能换措辞 / 加提示 / 删限定. 这是对比 fairness 保证.

5. **用户可能问到第 5-6 题后 Chat session context 满** — 建议每 3-4 题开一次新 chat session (Custom mode 保持). 不算 FAIL, 是 NotebookLM context 限制.

6. **评分写进 evidence 要**写明**理由** — 不只写 PASS/FAIL, 要引用题中的 "PASS 判据 / FAIL 判据" 具体条.

7. **如你 (cowork) 对某题答案判定犹豫** — 在 evidence 加 "⚠️ 判定存疑, 待主 session ack" 标记, 不硬判.

---

## 估时与节奏建议

| 环节 | 估时 | 谁做 |
|------|:----:|------|
| 前置检查 (Step 0) | 2 min | cowork |
| 42-tile 全扫 (Step 1) | 15 min | 用户 |
| 10 题 Chat 问答 (Step 2) | 45 min | 用户 (问) + cowork (旁观评分) |
| Evidence 落盘 (Step 3) | 15 min | cowork |
| _progress.json 更新 + commit (Step 4) | 10 min | cowork |
| 用户 ack + push | 5 min | 用户 |
| **总计** | **~1.5 h** | |

Q2 保险 2x → 3 h 内可收, **不跨天**.

---

## 入口文件引用清单 (cowork 按需读)

| 文件 | 作用 |
|------|------|
| `ai_platforms/notebooklm/docs/PLAN.md` §6 P3.4 | 原始规格 (M3 fix + S2 fix) |
| `ai_platforms/notebooklm/dev/evidence/_progress.json` | P3.3 完成状态 / F-1 闭合记录 / carry_over_to_p3_4 清单 |
| `ai_platforms/notebooklm/dev/evidence/chat_mode_toggle_test.md` | P3.3 evidence + F-1 闭合 log + F-2 carry-over |
| `ai_platforms/notebooklm/current/uploads/MANIFEST.md` | 42 bucket 清单, 期望 citation 名字对照 |
| `ai_platforms/notebooklm/dev/evidence/source_mapping.md` | 每 bucket 覆盖的 domains / Req 变量 (判 citation 精度用) |
| `ai_platforms/notebooklm/current/instructions.md` | Custom mode 规则, PASS 判据依据 (规则 2 citation / 规则 5 Core / 规则 6 CT) |
| `ai_platforms/notebooklm/dev/evidence/req_vars_full_set.md` | 176 Req 变量全名单 (P3.4.5 才是正本用, P3.4 仅查 Q02 AE Req) |
| `.work/meta/retrospective.md` § 4 | 四条全局规则 (A/B/C/D) 必遵守 |
| `CLAUDE.md` Session Wrap-up | 收尾 Chain 规则 (P3.4 收尾走 Chain B) |

---

*本手顺产出日期: 2026-04-21. 来源: `docs/PLAN.md` §6 P3.4 (M3 + S2 fix) + `_progress.json` P3.3 carry_over_to_p3_4 + `chat_mode_toggle_test.md` F-1 CLOSED + `p3_2_upload_log.md` 42 基线. 参照 `CHECKPOINT_P3.2_HANDOFF.md` 手顺格式.*
