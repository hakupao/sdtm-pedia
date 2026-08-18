# doc 轨 U6 — 判库欠账重启修法 (仪器先行 + 确定性信号层) 收口证据

> 状态: **⛔ FAIL 收口 (条款 1 触发, 部分达成; 用户裁定保留信号层)** · 2026-08-17/18
> · 单元 = `DOC_TRACK_KICKOFF.md` §0′ 候选 #1 (代号 U6)
> spec `docs/superpowers/specs/2026-08-17-doc-track-u6-routing-debt-restart-design.md`
> · plan 同名 plans/ 文件 · 在 main 上就地执行 (无 worktree, 见 §3-0)
> 数据红线: 题集 / 题面 / run 产物 / 跑批日志全在 `data/study/` 与 `eval/` 的 gitignored 件里。
> **本文件零题面零真名, 只有题号、组名、判库取值、数字与命令。**

## 0. 一句话

Phase 0 的仪器修缮与新基线冻结全部达成 (254 题 / fatal 口径 250 / 三遍 254/254 全稳),
Phase 1 的确定性信号层 (widen-only) **路由侧零害但没修掉欠账**: 全闸 `rc=1`,
**条款 1 触发 (fatal 8/8/8, 要求 0)**, 条款 2/3/4/7 全 PASS。
判库欠账 **9 → 8 (修好 1 条 `u3_doc_02`), 而这必须与「`cdisc_sig` 在全部 254 题上零触发」同框读**
—— 8 条残余全部需要 study→both 方向, 而那个方向的信号一次都没 fire。
答题侧 spot-check 拿到本仓第一条**端到端实证**: `st01_v2_q07` 由判库拓宽后
**off judge 0.0×3 → on judge 1.0×3** (source_recall 0.0→1.0), 「判库欠账 → 答题损失」这条因果链
在单题上首次闭合。**本单元不得写成「验收通过」**: 预登记的 revert 未执行, 是用户裁定
「保留信号层 + 按部分达成 FAIL 诚实收口」的结果, 不是闸放行的结果。

## 1. 架构改动面

**生产改动面 = 4 个文件, +343 / −18 行** (`git diff --numstat 92bdbc1..256992b -- sdtm-rag/server`):

| 文件 | 行数 | 内容 |
|---|---|---|
| `server/routing_signals.py` | +205 (新建) | `RoutingSignals.widen_reason(routed, question) -> "study_sig"/"cdisc_sig"/None`; 冻结白名单 `WIDEN_REASONS` + 方向表 `WIDEN_REASON_BY_CORPUS`; 词表 `CDISC_STRUCT_TERMS` (8 条) + `_CT_CODE_RE` + `_DOMAIN_VAR_RE` (公开 KB 派生 60 域码 / 200 词根 / 98 单独变量); `build_signals` 生产与 eval 同源工厂 |
| `server/federation.py` | +73 / −3 | `decide_corpus(llm_router, question, signals)` 同源抽取 (生产 `retrieve(auto)` 与 eval 共用一条); 白名单闸 / 方向闸 / 异常旁路 (信号层异常 ⇒ 不拓宽 + 响亮 warning, 不穿透生产); 观测属性 `last_signal_widened` |
| `server/study_lookup.py` | +50 / −14 | G1: 新增只读 `strong_hit()` / `_channel_hits()` (①label / ②a 多 token 交集 / ③别名; 排除弱通道 ②b); **`resolve()` 行为逐位不变** (8127 条差分 IDENTICAL, `evidence/step_u6_g1_strong_channel.md`) |
| `server/main.py` | +15 / −1 | lifespan 接线: 复用同一份 S2 构造 signals; S2 关着时不挂整层并留 `signal_layer_off` warning |

**信号层在生产默认启用** (无 env 开关; `study_lookup_enabled` 为真即挂), widen-only ⇒ 构造上不产新 fatal。
⚠ **launchd 进程仍是旧代码**: 现役进程启动于 2026-08-07 18:02, 早于接线 commit `219af23` (2026-08-18),
即**线上此刻跑的还是无信号层的基线行为**。这是操作项不是缺陷 (见 §5-19)。

eval / 仪器侧 (各带测试):

1. `eval/run_routing_eval.py` (+109/−14): run 级 `meta` (A-3) · `--out-prefix` · 三遍守卫 (I-1) ·
   `by_group.passed` 移除 (I-4) · `--signal-layer {off,on}` · `FINAL_IDS` 3→4 题 + `load_v2_final` ·
   `EXPECTED_GROUP_SIZES` 合计 254
2. `eval/u6_gate_verdict.py` (+188, 新): 七条款判定, 条款 4/7 双列双闸, `validate_inputs` (I-2)
3. `eval/u6_answer_verdict.py` (+241, 新): E1 稳定半 ∪ 支配 · E4 并集闸 · I-1 结论词抑制 ·
   `divergent_readings`
4. `eval/u6_calibrate_signals.py` (+217, 新): 可见集标定台 (只读 legacy+dev, 零 LLM,
   离线模拟走 `decide_corpus` 本尊)
5. `eval/run_eval.py` (+32/−2): `--signal-layer` 透传 + 三道 usage 闸 + `summary.signal_layer` + 回执
6. `scripts/leakscan_evidence.py` (+161, 首次进 git): 题面泄漏扫描器, Task 0 修复环改 fail-closed

**历史件冻结不动**: `eval/u3_task8_verdict.py` / `eval/u5_verdict.py` 一字未改 (保 U3/U5 收口 §8 可重放);
`_ROUTER_SYSTEM` 一字未动 (本单元不走措辞层)。

gold 变更两处, **均在基线冻结前**: `u3_amb_06` gold `both→study` (出题侧盲判复核 + 用户裁定) ·
`st01_v2_q07` 入 final 组 (只报告不作判据)。

测试 1353 → **1699 passed** (+346)。

## 2. 数字

### 2.1 冻结基线 (Task 6, sha `1fe5cda`, 干净树)

| 项 | 值 (三遍逐格相同) |
|---|---|
| 全集 / fatal 口径 | 254 / **250** (= 254 − final 4) |
| `fatal_excl_final` | **9 / 9 / 9** |
| `legacy_exact` | 179 / 181 (floor 178) |
| 三遍稳定 | **254 / 254** |
| rc | 1 (欠账未修 = 本单元存在的理由) |

分组 (n · exact · fatal): legacy 181·179·0 / u1_doc 27·27·0 / final 4·0·4 (不计入判据) /
dev 12·12·0 / heldout 12·11·1 / distractor_cdisc 12·7·3 / ambiguous_both 6·1·5。

fatal 9 的构成: `both→study` 5 (`u3_amb_01..05`) · `cdisc→study` 3 (`u3_dist_07/10/11`) ·
`study→cdisc` 1 (`u3_doc_02`)。
⚠ 与 U3 期 fatal=10 的唯一差是 **`u3_amb_06` 的 gold 改判**, 不是路由行为变好 —— 该题三遍
`(gold, pred)` 均为 `('study','study')`, 改 gold 前是 fatal, 改后同一个预测就是正确答案。
**`ambiguous_both` 组 gold 已混合 (5 both + 1 study)**, 该组读数 (exact 1/6) 不得按「纯 both 组」解读。

### 2.2 全闸 (Task 10, sha `6b92857`, `--signal-layer on`) — 决定性闸

| 条款 | 判定 | 关键数字 |
|---|---|---|
| 1 (主闸: 每遍 fatal=0 且 legacy ≥178) | ⛔ **触发** | fatal **8 / 8 / 8**; legacy 179×3 (达标半) |
| 2 (heldout 与 dev 差 ≤25pt) | PASS | dev 100.0% / heldout 91.67% (差 8.33pt) |
| 3 (dev exact ≥10/12) | PASS | dev_mean 12.0 |
| 4 (`distractor_cdisc` 双列双闸) | PASS | fatal 3.0→3.0; **exact 7.0→7.0** |
| 5 (final 组只报告) | (只报告) | 见 §2.3 |
| 6 (三遍稳定性, 只报告) | (只报告) | `clause6_unstable: []` = 254/254 全稳 |
| 7 (`u1_doc` 双列双闸) | PASS | fatal 0.0→0.0; **exact 27.0→27.0** |

`rc=1` 由条款 1 单独决定 (rc = 1/2/3/4/7 的合取)。判定脚本**正常退出并打全条款表**, 不是崩溃。

**引用纪律三条 (缺一即为不合格引用)**:
- **条款 2/3 不得单独引用**: dev / heldout 两组 gold **全部是 `study`**, 多数类基线 = 100%,
  一个恒答 `study` 的平凡判器满分 ⇒ 这两条单独看零判别力 (U3 §7.1 / 抽检 A-2)。
- **条款 4/7 的 fatal 半由构造保证**: widen-only 下 `pred=both` 永不计 fatal ⇒ 「不增」是构造结论
  不是实测结论; **判别力在 exact 半** (7.0→7.0 与 27.0→27.0 才是这两条闸真说了话的地方, spec §4.2 预登记)。
- **欠账 9→8 必须与「`cdisc_sig` 全集零触发」同框** (下表)。

### 2.3 欠账前后对照 (修好 1 / 仍在 8 / 新增 0)

```
baseline fatal (9): amb_01 amb_02 amb_03 amb_04 amb_05 dist_07 dist_10 dist_11 doc_02
after 三遍 (8)    : amb_01 amb_02 amb_03 amb_04 amb_05 dist_07 dist_10 dist_11
三遍全修好 (1)    : u3_doc_02        部分遍次修好 (0): []        新增 fatal (0): []
```

- `u3_doc_02` 属 **heldout** 组 (题号前缀 `u3_doc_` 与组名 `u1_doc` 不是一回事)。拓宽后
  gold=`study` 而 pred=`both` ⇒ **不再 fatal, 也不算 exact**: heldout exact 仍 11/12, fatal 1→0。
- **8 条残余的 baseline pred 全是 `study`**, 按方向表只接受 `cdisc_sig` 作拓宽依据,
  而 `cdisc_sig` 在全部 254 题上 fire **0 次** ⇒ **修法在这 8 条上根本没有触发, 不是触发了被闸拦下**。
- 条款 5 (final 组, 只报告不作判据): `docs_v1_q15/q17/q53` 三遍 `cdisc→cdisc` 未变;
  `st01_v2_q07` `cdisc→both` (信号层拓宽) ⇒ final 组 fatal 4→3。**该组不进 rc, 不得支持任何过闸结论。**

### 2.4 widen fire (逐题 pred 差分, 零题面)

| 信号 | 方向 | 本批 widen fire | 读数 |
|---|---|---|---|
| `study_sig` | cdisc → both | **2 次/遍** (`u3_doc_02` heldout + `st01_v2_q07` final) | 在封存组上确实会 fire |
| `cdisc_sig` | study → both | **0 次/遍** (全 254 题) | 含它本该发力的 8 条欠账题 |

三遍逐遍差异均为 2 题, **非 widen 形状 (收窄 / 换库) 0 条**; 全集 pred 分布
`{cdisc:162, both:9, study:83}` → `{cdisc:160, both:11, study:83}` —— `study` 计数一格未动,
是 `cdisc_sig` 零触发的独立佐证。两批各 254/254 三遍全稳; `fallback=0` 三遍 ⇒ 本批 `both` 不含兜底成分。
⚠ **口径限定**: 该计数是 **widen 读法**的 pred 差分 (run json 不落 `widened_by`), 不是仪器直读;
**detect 读法本批未测**, 「`cdisc_sig` 是死代码」这个更强的说法本单元**不支持** (可见集上它 detect 命中 104 次)。

### 2.5 可见集标定 (Task 9, 零 LLM, `accepted=True` rc=0)

| 轮 | 性质 | (a) legacy exact | (b) dev drop | (c) detect (study_sig / cdisc_sig) | widen fire |
|---|---|---|---|---|---|
| R0 | 词表轮 (起点 `[A-Z]{4,8}`) | ⛔ 179 → **167** (−12) | 0 | 16 / 117 | 6 / 6 |
| R1 | 词表锚定公开 KB 派生表 | ⛔ 179 → **173** (−6) | 0 | 16 / 104 | 6 / **0** |
| **G1** | **代码裁定 (非词表轮)**: study 信号收紧为 `strong_hit()` | ✅ 179 → **179** (Δ0) | ✅ 0 | ✅ **9 / 104** | **0 / 0** |

- 止步第 2 轮而非跑满 5 轮是**结构性**的: 剩余 6 分损失全在 `study_sig`, 其判据与本 task 三个旋钮
  (词表 / CT 码正则 / 变量形态正则) **无任何数据依赖** ⇒ 再跑三轮是把同一结论重打三遍。
- **(c) 必须连读法一起引**: 操作性读法取 `detect`, 因为 **widen 读法在可见集上与词表无关地不可满足** ——
  可见集里每道单库题都已判对, 任何 widen 恒 −1 exact, 而规则 (a)(b) 又要求零害 (推证见 Task 9 §4,
  R0 是它的实证: (c)-widen PASS 的代价恰是 (a) 掉 12 分)。
- **widen 四格全 0 = 零害已证, 有效完全未证**: 可见集上「信号真的会拓宽某题」结构上不可测。

### 2.6 答题侧 spot-check (Task 11, cards 48 计分 / 51 总, sha `2012258`, auto 档双臂各三遍)

`rc=0`, `verdict_word = cost_reported`。**可比池 = 稳定配对 45/48 (全 parse_ok 48/48)**,
引本节任何 pt 必须同句写这个池。

| 项 | 值 |
|---|---|
| E1 已确证代价 | **2.08pt** / `['st01_v11_q23r']` |
| E1 已确证收益 | **2.08pt** / `['st01_v2_q07']` |
| `paired_net_pt` | **0.00pt** (精确 0, 非 round 出来的 0) |
| `aggregate_mean_diff_pt` | **−1.16pt** (n=48) |
| `divergent_readings` | false —— **但这是 `paired_net` 恰为 0 造成的判定盲区, 不是两尺同向** (§5-2) |
| E4 并集 | 3 / 闸 9 (cards) PASS · `['st01_v11_q19','st01_v2_q14','st01_v2_q18']` |
| I1 judge 重判 | same_rate **0.9792** (47/48) ≥0.95 PASS; 唯一重判不复现题 = **`st01_v2_q03`** |

**`st01_v2_q07` — 端到端实证 (本单元最扎实的一条)**:

| 臂 | routed ×3 | source_recall ×3 | judge_fact_recall ×3 |
|---|---|---|---|
| off | `cdisc` ×3 | 0.0 ×3 | **0.0 / 0.0 / 0.0** |
| on | `both` ×3 | 1.0 ×3 | **1.0 / 1.0 / 1.0** |

判库拓宽 ⇒ gold 由零命中变全命中 ⇒ 答案由判 0 分变判满分, 三遍稳定且支配成立
(`max(off)=0.0 < min(on)=1.0`)。这是「判库欠账 → 答题损失」在单题上的**首次端到端闭合观测**
(U5 只观测到检索侧零命中, 答题侧当时未测)。⚠ 该题属条款 5「只报告」组, **单题点名不构成
「信号层修好了判库欠账」的总体结论** —— 全闸的答案是 `rc=1`。

**`st01_v11_q23r` — 代价题, 但机制上不可能来自信号层**: 两臂 `routed` 六次全 `study`
(信号层未触碰), judge off 1.0×3 → on 0.0×3。主证据是机制而非指纹: `self.signals` 在
`server/federation.py` 全文除 `__init__` 外只出现一次 (传进 `decide_corpus`), 不进任何 retrieve /
`format_context` / `build_messages` ⇒ 两臂 `routed` 相同即检索输入与 system prompt 构造上相同。
判词**未改未豁免**: `confirmed_cost_ids` 照原样成立 —— 判定脚本是冻结件。该题至此**第四次出现**
(U2 条款 3 驱动题 → U5 E4 不可判池 → 本轮已确证代价题)。

其余读数: 检索脆弱 4 题两臂 24 次判库**全判 `study`** (U5 §2.3 同向, 样本翻倍), source_recall 两臂
均 1.0×3, 脆弱性未在答题侧显形 (⚠ 与 U5 的 q14/q21 读数不可比: 那是强制 both 档反事实, 本轮是 auto 档)。
source_recall cards: off 0.8542×3 / on 0.8750×3 (**两臂各自三遍零方差**), 差 +2.08pt **全部来自 q07**。
judge_avg: off 0.8542/0.8819/0.8819 (极差 **2.77pt**) vs on 0.8611/0.8715/0.8507 (极差 2.08pt)
—— **同配置跨遍极差 2.77pt > 两臂均值差 1.16pt**, 聚合口径本轮承载不了这个量级的结论 (U5 §2.4 同款)。
`routed_fallback` 306 行全 False, ⚠ 而 off 臂的 `st01_v2_q07` 正是判 `cdisc` 且 gold 零命中的
**路由打空**题 —— **fallback 只捕获异常不捕获错判**, 「全 False」不得读作「路由健康」。

### 2.7 测试计数链

`1353` (T0 自检) → 1362 / **1367** (T1+fix) → 1415 / 1432 (T2+fix) → **1440** / 1442 (T3+addendum) →
1495 / 1497 (T5+fix) → 1526 (T7) → 1573 / 1586 (T8+fix) → 1628 / 1641 (T9 标定台+G1) →
1650 / 1654 (T11+fix) → **1699** (T12 补杀波 +45)。
终值本 task 复跑实测: `1699 passed in 39.86s`, rc=0, HEAD `256992b` 干净树。

## 3. 触发 / 裁定

### 3-0 单元级裁定链 (全部先于其结果, 逐条在 SDD ledger)

| # | 裁定 | 裁定方 | 依据 / 代价若错 |
|---|---|---|---|
| 1 | 在 main 就地执行不开 worktree | 用户批准 | 本仓 U1-U5 惯例 + launchd 与 gitignored 数据绑定本 checkout; 代价 = main 上留待 revert 的 commit (退回预登记已覆盖) |
| 2 | `u3_amb_06` gold `both→study` | **用户** (2026-08-18) | 出题侧隔离方盲判 (未拿到任何路由行为信息, 防按结果定 gold) 按冻结判据「答案是否**必须**用到标准侧事实」判 study; `amb_01/04` 维持 both。复核方同时明示读法差异 (若判据放宽成「须声明合规」则本题也可判 both) |
| 3 | 反 cherry-pick 闸走显式豁免表 | controller | 不回改 U3 出题方签名的 draft (回改 = 伪造历史); `USER_RULED_GOLD_OVERRIDES` 断言 draft 原值防豁免表过期, 未登记偏差照红 |
| 4 | **G1 强通道** (study 信号由 `resolve` 任意命中 → `strong_hit`) | controller (spec §5.1 标定授权) | R1 已实测规则 (a) 在词表旋钮内**不可能**达标 (−6 分全在 study 侧弱通道 ②b); 代价若错 = 强通道在封存组不 fire, 欠账修不掉 → Task 10 闸如实拦 (**此代价已实测发生**) |
| 5 | **(c) 取 detect 读法**, 双数字并列 | controller | 否则激励倒置 (为活性检查保留有害弱通道); widen 读法结构性不可满足 (§2.5) |
| 6 | 信号层异常语义 = 咨询点捕获 + 不拓宽 + 响亮 warning | controller | 不穿透生产, 与 federation「异常降级 both」哲学的分歧点显式裁定; 信号全哑由条款 1 兜底 |
| 7 | **Task 10 处置 = 保留信号层 + FAIL 诚实收口** | **用户** (2026-08-18, **覆盖预登记**) | 预登记写「任一条款触发 ⇒ Phase 1 代码全部 revert」, 实测失败形态是「零伤害部分达成」而非预登记设想的修坏型; controller 上报三选项后用户裁定保留。引用纪律随裁定一起定死 (见 §0) |
| 8 | 抽检 B 的 F08 记账不改 (采纳 B 主张) | controller | 低危 + fail-loud + 需构造性输入才显形, 与刚关掉的 29 条不是一个量级; 入 §5-9 已知限制 |

### 3-1 闸的实际触发

- **条款 1 触发** (fatal 8 ≠ 0, 三遍逐位同, 距 0 非边缘)。条款 2/3/4/7 全 PASS, 254/254 三遍稳定。
- 规则 B 失败归档已落盘 `evidence/failures/u6_task10_attempt_1.md` (输入 / 产物 / 技术判定 /
  业务判定 / 下一 attempt 输入 / 处置裁定五段齐)。
- **未做**: revert (用户裁定覆盖) · 改阈值 · 改 gold · 改词表 · 重跑追数字。三遍就是三遍。
- Task 9 词表迭代 2 轮 (预登记上限 5), 提前收敛于结构性理由; G1 属代码改动不计词表轮次。
- 一处跑批命令 rc 未捕获已如实记账 (zsh 的管道状态数组是 `$pipestatus`, `${PIPESTATUS[0]}` 取空),
  **不影响判据** —— 判据 rc 出自 `u6_gate_verdict` 而非跑批命令。

## 4. 三方核验 (规则 D, 五方不同 session)

| 方 | subagent_type | 结论 | 报告 |
|---|---|---|---|
| 实现方 ×12 | executor (opus) | T0-T11 各 1 独立 session + T12 补杀波; 7 个修复环 (T0×2 / T1 / T2 / T5 / T8 / T11) + T9 的 BLOCKED→G1 轮 | `.superpowers/sdd/…` (gitignored) |
| 任务审查方 ×11 | code-reviewer (opus) | 逐 task + 逐修复轮 scoped 复审; 一次审查方失联 (T3 三次空闲零正文) 判失联后**重派全新 session** (`u6-t3-review2`, 同三份盘上输入) 而非放行 | 同上 |
| 出题侧复核方 | 独立 session (盲判) | amb 三题: `amb_01` 维持 both / `amb_04` 维持 both / `amb_06` 建议 study (附读法差异声明); 初稿含真实标识符, 进 git 前就地匿名化 + gitignored 对照表 | `evidence/u6_amb_gold_review.md` |
| 抽检方 A | debugger (opus) | **5/5 声称全复现, 0 条不一致** (Fraction 精确算术 + 异源写法, 一切自 254 条 `detail` 现算而非读 `summary`); 7 findings (F-1 HIGH 流程 / F-2·F-3 MED 结构盲点 / F-4~F-7 LOW 文本) | `evidence/step_u6_audit.md` (进 git) |
| 抽检方 B | test-engineer (opus) | 235 变异 → KILLED 197 / SURVIVED 38 (8 等价 + 1 弱设计); 29 条构成 15 findings (F-01 HIGH 词表零阴性对照)。**补杀波后复验 39 条 → 29/29 全转杀**, 终态存活 = **8 等价 + F08** (低危 fail-loud); harness 自证四条 (S0 compile 闸 / S1 阳性 / S2 阴性 / S3 锚点) 新树重证 | `evidence/step_u6_audit_mutation.md` (进 git) |
| controller | 本 session | 亲手复算第五方: after fatal 8×3 自 detail 现算逐 id 同 / widen 差分恰 2 (`doc_02`+`q07`, 均 cdisc→both) / q07 judge 0.0×3→1.0×3 / q23r 1.0×3→0.0×3 (两臂内部各自稳定, 双峰反向) / cost=gain=2.0833pt (Fraction) —— 全部与各方声称一致 | 本文件 + SDD ledger |

**抽检 A 的两条方法学自曝** (不是被发现的, 是自己写出来的): ① 并发隔离协调令到达时第 4/5 条已跑完,
逐条交代读数可归因性 (第 4 条按 import 图不可能受影响 + 前后两次树快照; 第 5 条在 controller 划出
保证窗口后补跑, 出处由「跑批前干净」升级为「全程干净」, 三遍 1654 零漂移); ② 报告初稿自己触发过一次
min_len=12 泄漏 (解释假阳性时把被解释的英文串写了进来), 改写后复扫 rc=0。
**抽检 B 的自曝**: harness 中途真坏过一次 (撞 `git checkout` 的 index.lock 返回 128), 由「每条变异前
先做净树自检」当场拦停整组, 无一条结果被脏树污染; `restore()` 随后改为重试 6 次 + 以 `git status` 复核。

## 5. 已知限制 (每条注明它看不见什么)

**判定 / 仪器设计类 (交下一单元, 本单元冻结期不修)**

1. **支配尺子对双峰题有假阳性路径** (Task 11 §6 实证): 一道题在两臂**输入完全相同**时仍可能各自
   三遍稳定落在相反值上, 于是被判「已确证代价/收益」。n=3 下一道 p≈0.5 的双峰题出现 3/3 相反形态的
   概率约 1/32。**看不见**: 代价集合里哪些是机制性的、哪些是采样巧合 —— 判定产物本身不区分,
   必须靠逐题输入同一性核验 (本轮是手工做的, 脚本没做)。
2. **`divergent_readings` 在 `paired_net == 0` 时天然失效**: 判据是
   `abs(agg)>eps and abs(net)>eps and 符号相反`, 本轮 net 是**精确 0** (抽检 A 用 Fraction 确认非近零),
   合取项第二半为假 ⇒ 无论 agg 什么符号都判 false。而「代价与收益各一题恰好抵消」正是最容易出现
   net=0 的形态。**看不见**: aggregate(−1.16pt) 与 paired(0.00pt) 的读数落差。
3. **`dominance_only_ids` 为空是本轮巧合** (两题同时满足稳定配对与支配)。**看不见**: 该字段本轮
   没有判别力, 不能据此说「支配尺子与稳定半一致」。
4. **`u6_gate_verdict` 只读 `summary`, 从不校验 `summary` 与 `detail` 自洽** (抽检 A F-2, MED):
   条款 1/2/3/4/7 全部取自 `summary.by_group`, 唯一读 `detail` 的是只报告项。若某份 run json 的
   summary 被写歪 / 手工编辑 / 两份拼接, 闸会原样继承并照常打全绿条款表。**本次实测 0 处不符**
   (抽检 A 自 detail 现算六份产物每一格, 与 summary 及 gate.json 三方对撞零不一致) ⇒ 是结构盲点
   不是已发生的错误。**看不见**: 这层无任何测试拦; 而红线又要求含题面的 `detail` 不进 git,
   人工复核天然只能看 summary。建议修法 (A 已证不到 20 行): `validate_inputs` 加自 detail 重算的离线自检。
5. **条款 2/3 只吃 after 批, 连「有没有喂对批次」都判别不出** (抽检 A F-3, MED): 本批 baseline 与
   after 的 dev / heldout 读数逐格相同 (dev 12/12, heldout 11/12, 三遍皆然) ⇒ 若把 baseline 误当
   after 传进去, 这两条款输出一字不差。**本次影响 = 无** (出处校验独立排除: 两批 `git_rev` /
   `generated_at` 两项互异; `signal_layer` 为 after 批独有键 (=on), baseline 批产于该键落地前**无此键** (缺席即 off, 判别力更强); gate.json 的逐题 `fatal_ids` 与 after 批 detail 逐条相等)。
   ⚠ 这与「多数类基线 ⇒ 零判别力」是**两件事**: 那条说「过闸不代表路由变好」, 这条说「过闸不代表量的是 after」。
6. **widen 计数是 pred 差分不是仪器直读**: run json 的 `detail` 不落 `widened_by`
   (`decide_corpus` 第三个返回值在 eval 侧被丢弃, 只有生产 `retrieve` 留观测字段)。**看不见**:
   「判库自身漂移恰好产生同一形状」在原理上排除不掉 —— 支撑只有两批各 254/254 三遍全稳这一**观测**。
7. **detect 读法在全闸批未测**: 只知道 `cdisc_sig` 改判 0 次, 不知道它的探针在这 254 题上命中过几次。
   **看不见**: 「fire 0 次」只在 widen 读法下成立; Task 9 的 detect 数字 (9 / 104) 只在可见集上,
   与全闸批不是同一批题, **两者不可相加也不可互证**。
8. **答题 run 产物无 `generated_at` / `git_rev`** (Task 1 的 A-3 修缮只覆盖了路由侧):
   Task 11 的跑批时刻只能用**文件 mtime** (会被下一次同名跑批抹掉) + 本文件记账。臂别本身是产物
   自证的 (`summary.signal_layer`)。抽检 A 交叉核验了 mtime 与 evidence 记载六份全吻合, 但明确降级
   为「产物未被重跑覆盖」而非「证明了跑批时刻」。**看不见**: 出处缺口原样存在。
9. **`u6_calibrate_signals.load_base_preds` 的合法 pred 集两个方向都没有锚** (抽检 B F08, 终态存活):
   放宽 (多收一个非法值) 与收紧 (连合法的 `both` 也拒) 两种变异都不红; 守卫本体有锚 (整条拆掉即红)。
   **严重度低且方向安全**: 收紧形态一跑真实基线就当场炸 (fail-loud), 放宽形态需 run json 里恰好
   出现那个字面值才显形。controller 采纳 B 的主张**记账不改**。**看不见**: 「哪些 pred 算合法」无字面断言。
10. **F-05 的根因仍在** (抽检 B): `routing_signals._norm` 是自检闸
    (`test_terms_are_already_in_matching_normal_form`) 的量尺, 却**不在生产路径上**
    (`_cdisc_signal` 走内联的 `_nfkc` + `.lower()`)。补杀波已给 `_norm` 本身补锚
    (`test_norm_is_nfkc_plus_lowercase`), 但「闸量的是副本」这个结构没变 —— 真收口须让
    `_cdisc_signal` 改调 `_norm`, 那是**生产路径改动**, 本单元未授权。
11. **B22 的两行休眠代码无人看守**: `compare_arms` 稳定半的 cost/gain 差式在当前实现下被
    `cost.update(dom_cost)` 逐键覆盖成同值 ⇒ 结构冗余, 不可能有独立测试锚。若将来支配定义放宽
    (如允许档内不稳定的贴边情形), 这两行会**突然重新生效且无人看守**。
12. **词表冻结闸改变了缺口形状而非消灭语义判据** (抽检 B §9.7): C06-C10 现由语义层 (黑名单 + 阴性
    参数化) 与冻结层 (`test_frozen_lexicon_and_patterns_are_literal` 把词表与正则钉成字面) 两层拦住,
    **冻结层是主力**。将来一次正当的重新标定, 改词表的人必须同时改那条字面断言, 而那一刻语义上
    唯一的守门人仍是黑名单。

**标定 / 覆盖类**

13. **封存组在标定期完全不可见**, 且两次「只窄不宽」有方向性代价: R1 词表是 R0 的真子集,
    G1 强通道是「resolve 任意命中」的真子集 ⇒ 封存组上**只可能少 fire**。若某道 distractor/ambiguous
    题原本靠宽正则或弱通道 ②b 才被拓宽, 这两步会把它丢掉。**这是预登记规则 (a) 逼出来的取舍,
    且本轮实测为已发生** (8 条零触发)。
14. **`_SDTM_STANDALONE_VARS` 含 9 个通用英文词形** (公开 KB §1 共通变量的机械派生产物), 仅在
    全大写且前后无 ASCII 字母数字时匹配; **可见集零误触, 封存组上不可测**。删除会破坏可复算性, 故保留记账。
15. **标定用单份基线** (`u6_baseline_run_1.json`; 三遍逐题一致故单份与三遍等价, 但若将来基线不再全稳须重算);
    **离线模拟 ≠ 真跑** (假设 router 在 after 批给出与冻结基线逐题相同的判定; Task 10 的三遍 +
    `clause6_unstable` 是这条假设的检验处, 本轮通过)。
16. **spec §5.4 顶层指标未闭合**: 「docs 侧 auto 相对强制 study 的 `source_recall` 差 −10pt → 0」
    要求 docs 侧 auto 与强制档对跑, **本单元两侧都没跑** (Task 11 只跑 cards 双臂, 强制档没跑)。
    可由构造推导的部分: docs 答题集 30 题与路由 gold 逐字对应 (u1_doc 27 + final 3), 这 30 题的
    widen 计数三遍全 0, 且 `docs_v1_q15/q17/q53` 三遍 `cdisc→cdisc` 未变 ⇒ **判库逐题相同 ⇒ 该 −10pt
    差本单元一分未动**。⚠ 这是**检索输入层面的构造性结论**, 不许写成「docs 侧信号层无代价」——
    Task 11 §6 恰好量出输入完全相同的一题两臂仍可差 1.0 分 (2.08pt)。
17. **只测 cards 一侧 48 题, 单模型单温度单 judge** (答题 Bedrock sonnet / judge deepseek temp 0);
    spot-check 范围外的题未测。换模型可能翻转。
18. **judge 侧不再是零噪声**: rejudge 探针只覆盖 6 份答案集里的 1 份, 且 same_rate 由 U5 的 1.0
    掉到 **0.9792** (唯一重判不复现题 = **`st01_v2_q03`**, 抽检 A 建议点名以便下游追踪)。
    **看不见**: 其余 5 份答案集上的 judge 行为。
19. **检索非逐位可复现**: `st01_v11_q04` / `st01_v2_q01` / `st01_v2_q12` 三题 top5 顺序跨遍抖动
    (near-tie), 三题六次读数全 1.0 未受影响。⚠ 抽检 A 更正了原措辞: off 臂**只有 `q04` 一题漂**,
    另两题只在 on 臂漂 ⇒ 「与臂无关」只对 `q04` 成立 (n=3 也不足以断言)。
20. **8 条未修的原因是「没触发」而非「触发了但判错」**: 这是从方向表 + fire 计数推出的机制结论。
    至于**为什么** `cdisc_sig` 在这 8 条题面上不命中 (词表缺哪类词形), 需要读题面才能回答,
    红线禁止, 故本单元不作诊断。

**生产 / 流程类**

21. **launchd 现役进程仍是旧代码** (启动 2026-08-07, 早于接线 commit `219af23`) ⇒ 信号层虽默认启用,
    **线上此刻未通电**。复核: `ps -eo pid,lstart,command | grep uvicorn`。这是待办操作项 (重启即生效),
    也意味着**本单元的一切读数都来自 eval 侧, 线上行为未变**。
22. **`route_corpus` 的 `exc_info` 渗漏面未硬化** (Task 8 裁定不动): 该处每次 router 异常触发都会把
    题面写进本机 `logs/api.launchd.log`; 判定理由是 `route_corpus` 属冻结区且日志非 git 红线对象。
    审查方复核确认风险描述属实且更宽 (异常 + JSON 不合法两路都漏)。**看不见**: 本地日志侧无闸。
    (信号层自己那条 warning 已按红线只带三个受控字段, 有 `test_rendered_warning_has_no_question_text` 钉住。)
23. **规则 D 五方共用一个工作树** (抽检 A F-1, HIGH 流程): 抽检期间变异方约每分钟换一次变异体,
    与全量测试 39–44 秒的时长同量级 ⇒ 复算方**自行守候取不到两端全干净的窗口** (实测四次失败),
    最终靠 controller 停下变异方划出保证窗口才取到。**看不见**: 共享树下任一方的「实测」读数
    都归因不到确定的代码状态。

**勘误 (抽检 A F-4~F-7, 签名件不改, 以本段处理)**

24. `u6_task9_calibration.md` §3-1/§3-2/§3-3 标注「逐字」的 stdout 有一处誊抄删字:
    `c_both_signals_alive_widen ... (仅报告, 见模块 docstring 的不可满足性推证)` 被抄成 `... (仅报告)`。
    抽检核过该串由**唯一**动过该文件的 commit `4e252bb` 引入, 早于该 evidence 自称的取值 sha `8dcb622`
    ⇒ 是誊抄不是代码漂移, **全部数字与判定词不受影响**。记录理由: 「逐字」在本仓是承重词。
25. `u6_task10_gate.md` §13 的题号盘点句列了该文件里并不存在的两个题号 (只出现在盘点句自身),
    属从别处誊抄的残留; 不影响泄漏结论 (该文件 leakscan 实跑 CLEAN rc=0)。
26. `u6_task11_spotcheck.md` §13-2 第 7 条「与臂无关」过度概括 → 见本节第 19 条。
27. 派单复述的测试计数链是**摘要不是完整台账**, 至少缺 `1367` 与 `1440` 两站 (抽检 A 从 commit
    message 扫出); 终值 1699 不受影响 (§2.7 已按完整链写)。

## 6. 本单元明确不能证明什么 (spec §8 预登记 + 各方越界清单)

- **不能**写成「验收通过 / 修法成功」—— 全闸 `rc=1`, 条款 1 触发; 预登记的 revert 未执行是**用户裁定**
  的结果, 不是闸放行的结果。合法句式:「条款 1 触发, 零害部分达成, 用户裁定保留信号层」。
- **不能**单独说「欠账 9→8」—— 必须同句写「`cdisc_sig` 在全部 254 题上零触发, 8 条残余需要的正是它」。
- **不能**拿 `st01_v2_q07` 的端到端修复论证「判库欠账修好了」: 该题属条款 5 只报告组, 全闸答案是 `rc=1`。
- **不能**说「信号层在答题侧净收益 / 净代价」: 判词是 `cost_reported`, 代价与收益各 1 题恰好抵消,
  且代价题经核验**输入未被信号层触碰**, 收益题属只报告组。任何 pt 都须带「可比池 45/48」。
- **不能**拿 −1.16pt 的聚合读数下结论 (同配置跨遍极差 2.77pt > 该差)。
- **不能**说「docs 侧实测无代价」(未跑, 只有构造性 Δ0); **不能**说 spec §5.4 指标已闭合。
- **不能**说「`cdisc_sig` 是死代码」(可见集上 detect 命中 104 次); 也**不能**说它「活着」——
  两种读法量的是两件事, 且不同批题。
- **不能**说「fallback 全 False = 路由健康」(fallback 只捕获异常不捕获错判, off 臂 q07 即打空未触发)。
- **不能**单独引用条款 2/3 (多数类基线 100%, 且连喂错批次都判别不出); **不能**把条款 4/7 的 fatal 半
  当实测证据 (widen-only 下由构造保证)。
- **不能**把本轮 auto 档数字与 U5 强制 both 档数字互比 (口径不同)。
- **不能**证明信号层阈值 / 词表对未来题泛化 (标定集 = 可见集, held-out 仍只有 12 题);
  **不能**证明席位配置 / N=8 最优 (只加宽不调席); **不能**证明答案质量整体变好 (spot-check 范围外未测)。
- **不能**对 E4 的 3 道不可判题 (`q19` / `q14` / `q18`) 任一单题下结论。
- **放宽 router 仍是新单元** (U5 §9-4 原样)。

## 7. 业务结论

1. **判库欠账修法这一线, 确定性信号层只解决了「打空」形态, 没解决「该宽不宽」形态。**
   已修的 2 题 (`u3_doc_02` + `st01_v2_q07`) 都是 study-gold 被判 cdisc 的打空型, 由 `study_sig`
   (S2 结构命中) 接住; 而 8 条残余全是 study→both 方向, 需要 `cdisc_sig`, 它零触发。
   **这两个方向的难度不对称**: study 侧有 S2 这个确定性结构索引可依托, cdisc 侧只有词面。
2. **零害与有效在这份词表上不可兼得, 而这是结构性的**: 可见集 (legacy 181 + dev 12) 上
   fatal = 0 ⇒ **没有「gold 是 cdisc/both 而被判 study」的活正例**可供标定 cdisc 方向;
   预登记规则 (a) 的零害约束因此必然把词表推向零触发。重启这条线需要**新的标定源** ——
   或用户授权把部分封存组转可见, 或另找带该方向正例的题源。这不是多标几轮能解决的。
3. **「判库欠账 → 答题损失」的因果链首次被单题闭合** (`st01_v2_q07`: off judge 0.0×3 → on 1.0×3)。
   这条实证给整条修法线一个此前没有的价值锚: 之前只知道路由打空导致 gold 零命中 (检索侧),
   现在知道它确实一路传到答案分。**但 n=1**, 且该题属只报告组。
4. **Phase 0 的仪器与基线是本单元最确定的存续资产**: 254 题七条款闸 (含条款 4/7 双列双闸补上
   U3 的两处真空) · run 级出处 meta · 三遍守卫 · 可见集标定台 (零 LLM, 离线模拟走生产函数本尊) ·
   答题侧修订判定 (支配纳入 / 并集入闸 / 结论词抑制 / 双尺并列)。下一次修法无论走哪条路,
   都能被这套尺子诚实评估 —— 这正是 U3 收口写下的那句「修法失败 ≠ 单元失败」的第二次兑现。
5. **信号层留在生产是低风险的** (用户裁定): widen-only 构造上不产新 fatal, 全闸七组 exact 逐格未降,
   全集只改判 2 题且方向形状全部合规。⚠ 但**它此刻还没真正上线** (launchd 未重启, §5-21),
   且答题侧只在 cards 48 题上量过。

## 8. 复跑命令 (逐字, 在 `sdtm-rag/` 下)

```bash
# 0) 全量回归 (本 task 实测 2026-08-18: 1699 passed in 39.86s, HEAD 256992b 干净树)
./.venv/bin/python -m pytest -p no:warnings --tb=no -rN | tail -2
# ⚠ 命令行不要再给 -q: pyproject 已有 "-ra -q", 叠成 -qq 会吞掉汇总行 (抽检 A 踩过)

# 1) 冻结基线三遍 (走 Bedrock light, 约 8 分 30 秒 / 762 次调用; 预期 rc=1, fatal 9×3)
./.venv/bin/python -m eval.run_routing_eval --runs 3 --out-prefix u6_baseline_run

# 2) after 三遍 (信号层开; 约 9 分; 预期 rc=1, fatal 8×3)
./.venv/bin/python -m eval.run_routing_eval --runs 3 --out-prefix u6_after_run --signal-layer on

# 3) 七条款判定 (零 LLM, 秒级, 确定性)
./.venv/bin/python -m eval.u6_gate_verdict \
    --baseline data/study/st01/eval/runs/u6_baseline_run_1.json \
               data/study/st01/eval/runs/u6_baseline_run_2.json \
               data/study/st01/eval/runs/u6_baseline_run_3.json \
    --after    data/study/st01/eval/runs/u6_after_run_1.json \
               data/study/st01/eval/runs/u6_after_run_2.json \
               data/study/st01/eval/runs/u6_after_run_3.json \
    --output   data/study/st01/eval/runs/u6_gate.json
echo "rc=$?"          # 1 (条款 1 触发)

# 3b) 负例自检 (I-2 同内容拒收; 应 stderr 报「baseline 与 after 内容相同」且一行条款表都不打)
./.venv/bin/python -m eval.u6_gate_verdict \
    --baseline data/study/st01/eval/runs/u6_baseline_run_{1,2,3}.json \
    --after    data/study/st01/eval/runs/u6_baseline_run_{1,2,3}.json

# 4) 可见集标定台 (零 LLM, 确定性; 三条规则全过 rc=0, accepted=True)
./.venv/bin/python -m eval.u6_calibrate_signals \
      --baseline data/study/st01/eval/runs/u6_baseline_run_1.json
echo "rc=$?"          # 0

# 5) 答题侧双臂各三遍 (Bedrock; 跑批日志含题面, 只落 gitignored 目录)
for i in 1 2 3; do for ARM in off on; do
./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --hybrid --study-lookup --federated --corpus auto --study-docs --judge --temperature 0 \
  --full-answers --signal-layer $ARM \
  --output "data/study/st01/eval/runs/u6_spot_cards_${ARM}_r${i}.json" \
  > "data/study/st01/eval/logs/u6/cards_${ARM}_r${i}.log" 2>&1
done; done

# 6) rejudge 探针 (I-1 输入; 取 on 臂 r1 一份重判)
./.venv/bin/python -m eval.rejudge_run \
  data/study/st01/eval/runs/u6_spot_cards_on_r1.json \
  data/study/st01/eval/test_set_study_v2.yml \
  --output data/study/st01/eval/runs/u6_spot_probe_cards.json
# → n=48 same=47 same_rate=0.9792 orig_parse_fail=0 rejudge_parse_fail=0

# 7) 答题侧判定 (零 LLM, 确定性, 只读已落盘产物)
R=data/study/st01/eval/runs
./.venv/bin/python -m eval.u6_answer_verdict \
  --arm-a $R/u6_spot_cards_off_r1.json $R/u6_spot_cards_off_r2.json $R/u6_spot_cards_off_r3.json \
  --arm-b $R/u6_spot_cards_on_r1.json  $R/u6_spot_cards_on_r2.json  $R/u6_spot_cards_on_r3.json \
  --family cards --probe $R/u6_spot_probe_cards.json --output $R/u6_spot_verdict.json
echo "rc=$?"          # 0, verdict_word=cost_reported

# 8) 本文件红线自检 (引用 CLEAN 必须连阈值一起写)
./.venv/bin/python scripts/leakscan_evidence.py \
  evidence/checkpoints/doc_track_u6_routing_debt.md --min-len 12
echo "rc=$?"          # 0 = CLEAN, needle 集须为 6/6 (无 --allow-missing)
```

⚠ 复跑 1) / 2) 会**覆盖**同名 run 产物。答题 run 非确定 (`--temperature 0` 下 Bedrock 侧仍逐遍不同:
本轮 off/on 两臂三遍答案逐字相同各 **0/51**), 重跑数字会变, 判定按冻结规则重算;
判定脚本与标定台是确定性的, 可逐位复现。run 产物 / 跑批日志 / gold 全部 gitignored。

## 9. 给下一单元的硬约束

1. **`cdisc_sig` 的标定困境是结构性的, 不是标定轮数不够**: 可见集 (legacy+dev) 上 fatal=0 ⇒
   **没有该方向的活正例**; 任何零害约束 (规则 a) 都会把词表推向零触发 —— 零害 ⇒ 零触发在这个可见集上
   几乎是等价的。重启这条线的前置条件是**新的标定源**: 或用户授权把部分封存组转可见 (代价 = 封存
   纪律破口, 须重新划分), 或引入带该方向正例的新题源。**不许在不解决这一点的前提下再标一轮。**
2. **8 条残余债全在 study→both 方向** (`u3_amb_01..05` + `u3_dist_07/10/11`)。修它属新单元,
   且**必须自带 U6 全套判据**: 254 题七条款 (含条款 4/7 双列双闸) + 新基线三遍重冻 + 可见集纪律
   (实现方全新 session 只见 legacy+dev) + 退回预登记。不许沿用本轮的 after 批作对照。
   下一步若要做误差分析 (mapping 类问句的词面特征在 U3 五轮措辞与本轮词表两条路上都没接住),
   **须先取得读封存题面的授权**, 且读过的人此后不得再做该组的实现或标定。
3. **`st01_v11_q23r` 双峰假阳性路径**: 支配尺子对生成侧双峰题的采样巧合**没有免疫力**
   (两臂输入逐位相同仍可被判「已确证代价」)。该题至此**第四次出现** ——
   **任何逐题结论先查它在不在池里**; 且下一版判定应把「逐题输入同一性核验」做进脚本
   (本轮是手工做的), 或至少对代价/收益集逐题打印两臂 `routed` 供人复核。
4. **`divergent_readings` 在 `paired_net` 恰为 0 时失效**, 而「代价收益各一题抵消」正是最常见的
   net=0 形态。修法: 合取项改为「两读数之一非零即比较」或对 net=0 单独出 `net_is_zero: true` 标记。
5. **并发隔离必须先于派出到达**: 「只读方并行 / 写树方串行」应写进未来 plan 的 Global Constraints,
   变异方走 `git worktree add` 隔离副本。本轮的教训是事后协调令只能记账不能补救 (抽检 A 实测四次
   守候都取不到干净窗口, 最终靠 controller 停下写树方划窗口)。任何「实测」读数在 evidence 里应
   同时附**跑批前后各一次** `git status --porcelain` 快照。
6. **任何 router 失败 traceback 贴进 checkpoint / 排障文之前必须洗题面** —— 红线会从日志绕道进 git。
   且 `route_corpus` 的 `exc_info` 渗漏面 (异常与 JSON 不合法两路) 至今未硬化, 属小硬化项,
   下一单元可顺手做 (改动落在冻结区, 须显式授权)。
7. **两处休眠隐患**: ① `routing_signals._norm` 仍是自检闸的副本而非生产路径量尺 —— 真收口须让
   `_cdisc_signal` 改调 `_norm` (生产路径改动, 须授权); ② `u6_answer_verdict` 稳定半那两行差式
   当前被支配并集逐键覆盖, 支配定义一旦放宽就会**突然重新生效且无人看守**。
8. **引用纪律 (审查方自检闸, 逐条)**: 本单元结论不得写「验收通过」· 欠账 9→8 必须与
   「`cdisc_sig` 全集零触发」同框 · q07 修复须写成「端到端实证 (off judge 0.0×3 → on 1.0×3)」·
   任何 pt 带「可比池 45/48」· 条款 2/3 不单独引用 · 条款 4/7 的 fatal 半标注「构造保证」·
   fallback 引用带「打空未触发」限定 · 强制档数字必须并列 auto 实测触发面 · leakscan CLEAN 必须连
   `min_len=12` 与 needle 集 6/6 一起写。
9. **词表若重新标定, 改的人必须同时改字面冻结断言, 并把新词表的出处写进 review** ——
   那一刻语义上唯一的守门人是黑名单 (抽检 B §9.7)。红的那一刻不是阻碍, 是要求你交代出处。
10. **`u6_gate_verdict` 应补 detail↔summary 自洽闸** (抽检 A F-2 建议, <20 行): 它是唯一决定单元
    成败的那把闸, 而红线又让人工复核天然看不见 detail 那层。

## 10. 任务台账

| Task | 内容 | 状态 |
|---|---|---|
| 0 | 开工自检 + 基线预跑三遍 | DONE (1353 / 4329·959·114 / 87.5% / fatal 10×3; 2 修复环 + leakscan 进 git 改 fail-closed) |
| 1 | `run_routing_eval` 仪器修缮 (A-3 meta / I-1 三遍守卫 / I-4 `by_group.passed` / `--out-prefix`) | DONE (1 修复环: `_git_rev` 改 describe --always --dirty) |
| 2 | `u6_gate_verdict` 七条款 (条款 4/7 双列双闸 + I-2 输入校验) | DONE (1 修复环: 异质 fixture 塌遍变异 3/3 转杀 + 批内去重闸) |
| 3 | `st01_v2_q07` 入 final 组 (254 题) | DONE (0 修复环 + controller 追加豁免表; 它主动抓到 gold 改动打红反 cherry-pick 闸, 刻意未顺手改绿) |
| 4 | amb 三题 gold 盲判复核 | DONE — 维持/维持/改 study; 用户裁定; 报告匿名化过红线 (980 标识符零命中) |
| 5 | `u6_answer_verdict` (E1 支配 / E4 并集闸 / I-1 抑制 / divergent) | DONE (1 修复环: 并集重叠边界用例 + caliber 标记 + stdout 红线哨兵) |
| 6 | **新基线三遍冻结 (Phase 0 收口硬闸)** | DONE — 254 / 250 / fatal 9×3 / legacy 179×3 / 254/254 全稳; 负例自检拒收成立 |
| 7 | `decide_corpus` 同源抽取 (行为不变的准备手术) | DONE (0 修复环; 192 组差分 0 diffs 实测行为不变) |
| 8 | `RoutingSignals` 双向信号 + 生产接线 | DONE (1 修复环: 方向四格锁 + 方向闸 + lower 闸 + warning 红线; 顺带修掉渲染层题面渗漏) |
| 9 | 可见集标定 | DONE — R0/R1 词表 2 轮 → BLOCKED (结构性) → **G1 强通道裁定** → 三规则全过, 信号层定义冻结 |
| 10 | **全闸三遍 (判决点)** | **FAIL — rc=1, 条款 1 触发** (fatal 8×3); 2/3/4/7 全 PASS; 规则 B 归档 + 用户裁定保留信号层 |
| 11 | 答题侧 spot-check (auto off vs on) | DONE — rc=0 `cost_reported`; q07 端到端修复实证; q23r 假阳性路径发现 (1 修复环) |
| 12 | 规则 D 三方核验 (五方) | DONE — A 5/5 全复现 + 7 findings; B 235 变异 → 补杀波 29/29 转杀 → 复验终态存活 8 等价 + F08; controller 复算全对上 |
| 13 | 收口 | DONE (本文件 + retro; kickoff / PROGRESS / worklog / CLAUDE.md 由 controller 同步) |

## 11. RETROSPECTIVE (规则 C)

### 11-1 保留下来的做法

1. **判据先于数据写死, 且 Phase 0 硬闸在 Phase 1 之前** —— 本单元最值钱的一条。条款 4/7 的双列双闸、
   E1 支配纳入、E4 并集入闸全部在任何跑批之前冻结, 于是 Task 10 的 `rc=1` 没有任何解释空间可争。
   对比 U3: 那次条款 4 的 exact 口径方向错, 是跑完才发现尺子对某类回归失明。
2. **预登记「失败区间」而不只是预登记「成功标准」**: Task 9 派出前登记的预期区间被实测**部分推翻**
   (预期 `cdisc_sig` 可能修 ≤8 条, 实测 0; 预期 `study_sig` 因 U1 语域不相交可能不 fire, 实测 fire 2 次),
   而正因为写在前面, 这个推翻本身成了可引用的信息, 而不是事后叙事。
3. **零 LLM 的标定台买到了「照现状必不过」这个结论** (Task 9 R1 的 BLOCKED), 花的是几秒钟而不是
   762 次 Bedrock 调用。**离线模拟走生产函数本尊** (`_ReplayRouter` 喂冻结 pred 进 `decide_corpus`)
   而不是自抄一份 widen 逻辑, 是这条捷径能被信任的唯一理由 —— 且该等价性有可执行的锚 (变异 F25 被杀)。
4. **出题侧盲判隔离**: 派单**刻意不含** U3 探针的结论 (那是 router 行为信息, 写进去就等于按结果定 gold),
   复核方只拿冻结判据盲判。结果之一 (`amb_06` 改 study) 直接改变了基线 fatal 数, 若不隔离,
   这个改动会永远背着「为了让数字好看」的嫌疑。
5. **变异测试 harness 先自证再用** (S0 compile 闸 / S1 阳性 / S2 阴性 / S3 锚点), 且在补杀波后的
   新树上**重证一遍**而不是沿用昨天的结论。A17 那格尤其说明问题: 加固改掉了原锚点,
   若 harness 静默跳过, 那条变异会被记成「已修」而实际从未施加。
6. **抽检方自曝失误的文化**: A 自曝协调令时序与自己触发的一次泄漏; B 自曝 harness 真坏过一次、
   自曝一条变异设计得太弱、自曝「我原本的推断被实测推翻」(F-12 由低升中)。这些自曝比结论本身更值钱。

### 11-2 必须补上的缺口

1. **规则 D 五方共用一个工作树是本轮最大的流程缺陷** (抽检 A F-1, HIGH)。写树方 (变异) 与只读方
   (复算) 并行, 导致复算方四次守候都取不到干净窗口。**隔离要求必须先于派出到达** ——
   事后协调令只能记账不能补救。修法已写进 §9-5。
2. **「唯一决定成败的那把闸」自身缺一层自洽校验**: `u6_gate_verdict` 只读 `summary`,
   而红线又让人工复核只能看 summary ⇒ 这层盲点无人可见也无测试可拦。这与 U3 retro 写下的
   「闸的代码要与生产代码同等对待」是同一条教训的**下一层**: 光有测试还不够, 还要问「这把闸
   对哪类输入错误失明」。
3. **仪器修缮做了一半**: A-3 的 run 级 meta 只落到路由侧, 答题侧 `run_eval` 产物至今无
   `generated_at` / `git_rev` ⇒ Task 11 的六份产物只能靠 mtime + 自报追溯。当时的边界划分是
   「本单元只修 U3 点名的仪器」, 但同一条缺陷在答题侧同样成立, 应当一并修。
4. **eval 侧丢掉了 `widened_by`**: `decide_corpus` 返回了它, 生产留了观测属性, 唯独 eval 侧丢弃 ⇒
   widen 计数只能靠 pred 差分, 永远差一层构造保证。这属于 Task 7 设计时的一处省略,
   代价在 Task 10 才显形。
5. **词表 / 正则这类「标定件」在测试上是天然弱项**: 它们的全部价值在「不该 fire 时不 fire」,
   而 TDD 的自然形状是写阳性用例。抽检 B 的 F-01 (五条变异全绿) 说明**阴性对照必须写进 plan 的
   验收条款**, 不能指望实现方自发去写。
6. **答题侧只跑了 cards 一侧**: docs 侧靠构造推导记账 (判库逐题相同 ⇒ 检索输入相同), 省下了 6 个
   Bedrock run, 但也让 spec §5.4 的顶层指标至今未闭合。这个取舍当时是对的 (FAIL 已定, 不宜再烧),
   但应在 plan 里就写成「条件分支」而不是临场决定。

### 11-3 关键决策复盘

1. **G1 是本单元最贵也最正确的一次裁定**。R1 已用零 LLM 证明「规则 (a) 在词表旋钮内不可能达标」,
   此时有三条路: 放宽规则 (a) (= 改判据, 自毁纪律)、宣布 BLOCKED 收工、或改代码把 study 信号收紧。
   选第三条并按 spec §5.1 的标定授权走完整的实现+审查 (8127 条 `resolve` 差分逐位不变),
   换来了可见集零害 —— **但也正是这次收紧, 连同 R1 的词表剪枝, 把修法面同步收窄到接不住欠账题**。
   Task 9 §7-3 当时就把这个「只窄不宽的方向性代价」记为**不可测**, Task 10 把它实测为**已发生**。
   复盘结论: 这个取舍没有更好的替代 (规则 a 是零害的唯一保证), 但**「零害约束会不会把修法面收窄到
   无效」这个问题, 应该在标定开始前就作为预登记风险写明**, 而不是在 BLOCKED 报告里才第一次出现。
2. **用户裁定「保留信号层 + FAIL 诚实收口」优于机械执行预登记的 revert**。预登记设想的失败形态是
   「修坏型」, 实测是「零伤害部分达成」—— 七组 exact 逐格未降、全集只改判 2 题、修好 1 条 fatal
   且带一条端到端实证。机械 revert 会把这些一起丢掉。**但预登记的价值不因被覆盖而降低**:
   正因为它写在前面, 「要不要保留」才成了一次显式的、留痕的用户裁定, 而不是一次事后合理化。
   代价已如实定价: 引用纪律必须写死 (不得称验收通过), 否则下一个人会把「保留」读成「通过」。
3. **把 `st01_v2_q07` 收进 final 组 (只报告不作判据) 是对的**。它是 U5 观测到的第四道打空题,
   若作判据就成了「按已知病例定尺子」; 作只报告, 它反而在 Task 11 给出了本单元唯一的端到端实证。
   **这条经验可推广: 动机题一律进只报告组。**
4. **「派了审查 ≠ 审过了」在本轮真的兑现了一次**: Task 3 的审查方三次空闲零正文, 两次催无果,
   判失联后**重派全新 session 用同三份盘上输入**, 而不是让它带着「已派审查」的记录过关。
   若当时放行, 后续所有关于 gold 变更的结论都会缺一方。
5. **抽检 B 的补杀波 (29/29 转杀, +45 测试) 是否值得**: 它把 15 条 findings 全部关掉且唯一源码改动
   经 sha256 证明 gate 产物位级不变。值得 —— 因为其中 F-01 (词表零阴性对照) 与 F-05 (自检闸量副本)
   都是「改坏了全绿」的形态, 而信号层要长期留在生产。**但留下的 F08 与 B22 说明: 补杀波关的是
   已发现的缺口, 关不掉「没人想到去变异的那一格」。**
6. **本单元没有走措辞层是对的**: U3 已用五轮实证「措辞杠杆已到底」(最强兜底指令三遍零方差不执行)。
   走确定性信号层至少让失败是**可归因的** —— 我们现在确切知道 8 条为什么没修好 (信号根本没触发),
   而不是又一次「模型就是不听」。**把不可归因的失败换成可归因的失败, 本身就是进展。**

---

## 操作项闭合 (2026-08-18, 收尾补记)

§1/§5 所记「launchd 现役进程早于接线 commit, 线上未通电」已闭合: 用户指示后
`launchctl kickstart -k gui/501/com.sdtmrag.api` 重启 (新进程 2026-08-18 19:14:11 起),
`/api/info` 200, 启动日志 `federation signal_layer=True study_lookup='959 items/1 aliases'`
—— widen-only 信号层自此在生产在线。复核命令:
`grep signal_layer sdtm-rag/logs/api.launchd.log | tail -1`。
