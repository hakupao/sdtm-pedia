# doc 轨 U5 — both 答题侧代价 + 答题侧仪器 收口证据

> 状态: **DONE (有条件)** · 2026-08-16/17 · 单元 = `DOC_TRACK_KICKOFF.md` §0′ 候选 #3+#4 合并 (代号 U5)
> spec `docs/superpowers/specs/2026-08-16-doc-track-u5-both-answer-cost-design.md` (含修正案 1/2)
> · plan 同名 plans/ 文件 · 分支 `doc-track-u5`
> 数据红线: 题集 / 题面 / run 产物 / 跑批日志全在 `data/study/` (gitignored)。**本文件零题面零真名, 只有题号与数字。**

## 0. 一句话

答题侧仪器建成 (judge 重判同分率 1.0/1.0 = judge 零噪声; 同配置逐题稳定性 + 双向对照 1.0/0.0),
`both` 两方向答题侧代价在冻结判定下 **E2 = cheap_on_this_ruler (rc=0, 无闸触发)** ——
但**必须连同双口径读**: 该判词只在**可比池** (cards 41/48 · docs 29/30) 内成立, 抽检 A 的
最坏界并列尺子确认 **2 题稳健退化 (2.08pt, `st01_v2_q14`/`st01_v2_q21`)**, 聚合均值方向为
**−0.69pt**。最扎实的一条合法结论: **生产 auto 实际判到 both 的 5 题全在可比池且两侧同分 ⇒
现行 router 已在用的那点 both 是免费的**。auto 触发分布从演绎升级为逐题观测 (逐位复现 U3)。

## 1. 架构改动面

**生产改动面 = `server/federation.py` 2 行零行为观测属性** (`last_route_fallback`, 只写不读,
spec 修正案 1)。其余全在 eval 侧, 各带测试:

1. run 产物 `results[*]` 逐题 `routed` + `routed_fallback` (attach 长度闸 fail-loud) —
   修掉 both_ruler §5-8/§5-11 两条仪器缺口
2. `eval/rejudge_run.py` — judge 重判探针 (orig parse-fail 出分母 / judge_model 断言 /
   rejudge 侧 parse_fail 对称计数)
3. `eval/u5_verdict.py` — 六段确定性判定 (阈值冻结 + 字面断言兜底; 闸键集断言 / 极性内容断言 /
   controls 信息量闸 / 行数与 judge 断言 / E2 按代价集合空判)

测试 1275 → **1353 passed** (+78 = 判定 36 + rejudge 9 + 观测字段 8 + 抽检 B 补网 25)。
gold / 阈值 / router / 席位 / 题集全程一字未动。

## 2. 数字

### 2.1 仪器读数 (I 闸, 全过, rc=0)

| 闸 | 判据 (冻结) | 实测 | 判定 |
|---|---|---|---|
| I1 judge 重判 | 同分率 ≥ 0.95 | cards **1.0** (48/48) · docs **1.0** (30/30), parse_fail 全 0 | PASS |
| I2 逐题稳定性 | 不稳定 ≤ 7/48, ≤ 4/30 | cards_study **5** / cards_both **4** / docs_study **1** / docs_both **0** | PASS |
| I3 双向对照 | 阳 ≥0.80 且 阴 ≤0.20 | 阳 **1.0/1.0** · 阴 **0.0/0.0** (parse_ok 24/24) | PASS |

judge 重判 1.0 ⇒ **答题侧全部不稳定性来自生成侧, 不是 judge 侧** (⚠ 依据 1 份答案集外推,
抽检 A F-3)。三遍答案文本 cards 0/48 相同 ⇒ 三遍是真实重采样非缓存重放。

### 2.2 效应 (E 规则, 冻结口径) — **必须双口径同框引用**

| 口径 | cards 方向 (study→both) | docs 方向 |
|---|---|---|
| **E1 配对 (冻结判定用)** | 代价 **0.00pt / 0 题**; 收益 **+2.78pt / 2 题** (`st01_v2_q08` 0→1, `st01_v2_q19` 0.6667→1); n_compared **41/48** | 代价 0 / 收益 0; n_compared **29/30** |
| **最坏界 (抽检 A 并列)** | 代价 **2.08pt / 2 题** (`st01_v2_q14` 0.3333×3 vs study min 0.6667; `st01_v2_q21` 0.0×3 vs study min 0.6667); 收益同 2 题不变 | 0 / 0 |
| **三遍聚合均值** | study 0.8843 vs both 0.8773 = **−0.69pt** | +0.56pt (全来自不可判 1 题) |

- **E2 判词 = `cheap_on_this_ruler`**。引用纪律 (审查方清单): 判词必须连同「可比池 41/48」
  同句出现; 配对口径与聚合口径的 **−3.47pt 差额 100% 落在被排除的 7 题不可判池** (审查 C1 =
  抽检 A F-1, 两方独立同机制) ⇒ **这把尺子对最坏界确认的 2 题回归不敏感**, 稳定性过滤天然
  偏向删掉代价信号 (5 道均值净负题 5/5 全在被删池, 4 道净正题只删 2)。
- **E4 不可判池**: cards 7 题 (`st01_v11_q23r` · `st01_v2_q03/q06/q14/q18/q21/q22`) ·
  docs 1 题 (`docs_v1_q41`)。q23r 又来了 (U2 条款 3 的驱动题)。并集占比 14.6% **从未被任何
  闸检验** (I2 闸的是逐配置 10.4%/8.3%, 审查 C2)。
- **E3 传导** (检索侧 4 脆弱题, both_ruler §2.3 → 答题侧): `st01_v11_q19` (检索 −0.5) 稳定
  1.0=1.0 **未传导**; `st01_v2_q15` (−0.5) 稳定 0.6667=0.6667 **未传导**; `st01_v2_q14` (检索
  gold 全丢) 与 `st01_v2_q21` 冻结判定下**不可判** (study 侧三遍不稳), **按最坏界已传导**
  (见上表)。q14 在 both 下检索 gold 零命中仍稳定答出 0.3333 ⇒ 有 fact 不经 gold 检索也能答
  (模型先验或旁块, 未溯源)。

### 2.3 触发率 (Task 6, 演绎 → 观测)

- auto 判库分布三遍逐位复现 U3 §4.1: cards **45 study / 5 both / 1 cdisc** · docs **27/0/3**;
  81 题 × 3 遍逐题零漂移 (n=3 只给上界)。
- `routed_fallback` **243/243 全 False** — 首次从落盘产物直接复核 (U3 只能 grep 不可落盘日志)。
  ⚠ 引用限定 (抽检 A F-2): 其中 **4 题路由打空** (`st01_v2_q07` + `docs_v1_q15/q17/q53` 判
  cdisc 且 gold 零命中, 三遍稳定) 而 fallback 不触发 — **fallback 只捕获异常, 不捕获错判**,
  「全 False」不得读作「路由健康」。docs auto 0.900 vs 强制 0.999+; 这就是判库欠账 10pt 本体。
- 脆弱 4 题 auto 下 **12/12 全判 study** — U3 §4.2 演绎升级为直接观测: **−5.21pt 检索代价
  生产一分未付**仍成立。5 道 auto-both 题具名 (`st01_v11_q17` · `st01_v2_q01/q04/q12/q13`),
  全在可比池两侧同分。
- 生产日志照录: `logs/api.launchd.log` 仅 **7 条** federation_routed (2026-08-04~07),
  0 both, 全 fallback=False — **线上触发率无数据可言, 无结论**。
- both 档 token 代价 (次级观测): cards +53% / docs +56% (context 8+8+8 vs 15+8)。

### 2.4 历史锚点

M1 (cards@study) 三遍 0.8681/0.9028/0.8819 与 U2 ON 臂 (0.8542/0.8819) 同区间;
同配置跨遍极差 cards study **3.47pt** — 再次实证均值口径承载不了 3pt 级结论 (U2 §8-1),
本单元逐题配对设计正为此而立。⚠ 2.78pt (逐题配对) 与 3.47pt (聚合极差) **不同口径,
互比大小任何方向都错** (审查 I-4)。

## 3. 触发 / 豁免

**六条 I/E 闸无一触发** (rc=0), 无豁免事项。阈值 / 判定规则自 T3 冻结后一字未动
(字面断言测试兜底); T5 跑批后发现的判定设计缺陷 (F-1/C1/C2/I-1) **按 spec §5.3-2 一律不修**,
全部记 §5 已知限制交下一单元。

## 4. 三方核验 (规则 D, 五方不同 session)

| 方 | subagent_type | 结论 | 报告 |
|---|---|---|---|
| 实现方 ×5 | executor (opus) | T1-T7 (T1×1+修复3轮 / T2×1+3轮 / T3×1+3轮 / T4/T5/T6 各1) | `.superpowers/sdd/...(gitignored)` |
| 任务审查 ×8 | code-reviewer (opus) | 逐 task + 逐修复轮 scoped 复审 | 同上 |
| 收口审查方 | code-reviewer (opus) | **条件通过**: 判定链 vs spec §5 零偏离; 2C/4I/3M (C1 双口径反向 / C2 并集未闸 / I-1 latent / I-2 变异存活→B 已杀 / I-3 强制档≠生产档 / I-4 口径不可比) + 引用纪律 11 条越界清单 | task-8-review.md (gitignored, 本文件摘录) |
| 抽检方 A | debugger (opus) | **64 项声称 64 项复现 0 不一致** (Fraction 精确算术, 异源写法) + 7 findings (F-1/F-2 HIGH) | `evidence/step_u5_audit.md` (进 git) |
| 抽检方 B | test-engineer (opus) | **148 变异 → 终态 SURVIVED 0** (108 杀 + 补 25 case 转杀 35 + 等价 4); 冻结期存活清单 **0**; M-B 分歧解开 = PYTHONHASHSEED 掷硬币覆盖 | `evidence/step_u5_audit_mutation.md` (进 git) |
| controller | 本 session | q14/q21 最坏界 + q08 收益逐遍亲手复现; 四 control 产物复读; 红线扫描零命中 | 本文件 + SDD ledger |

## 5. 已知限制 (每条注明它看不见什么)

**判定设计类 (T5 后发现, 冻结不修, 重启相关单元前先处理)**
1. **E1 稳定性过滤偏向删代价信号** (A F-1 / 审查 C1): 两档分值不同的题天然更易档内不稳定,
   过滤精准删掉信号本体。看不见: 不可判池里的真实回归 (最坏界已确认 2 题 2.08pt)。
2. **E4 并集从未被闸** (审查 C2): I2 逐配置各 ≤15%, 并集 14.6% 无闸, 零重叠时可到 29.2%。
   看不见: 跨配置合计的不可判规模。
3. **I-1 latent**: I1 失守路径下产物仍写 `cheap_on_this_ruler` 结论词 (仅加 advisory flag),
   违 spec §5.1 字面。本轮 I1 PASS 未触发。看不见: 未来降级跑该字段会误导只读 E2 的人。
4. **I3 浮点边界**: 生产 avg 未 round, 数学恰等阈值时浮点落错侧 → 假 rc=2 (安全侧假警报)。
   复现: `python -c "print(sum([0,0,0,0,0.4,0.8])/6 > 0.20)"` → True。
5. **对照家族错绑无内容级闸** (极性有): `docs_positive.json` 塞给 `--controls-cards-pos`
   只污染 I3.avg 标签, 不动判定 (两家族同阈值)。看不见: 归档标签的家族可信度。
6. **N1 只查 ≥1 行 parse 成功不查比例**; **M4 只查表头 judge_model 不查逐行**。

**测量覆盖类**
7. **probe 只覆盖 6 份答案集里的 1 份, 且 39/48 原分 = 1.0 天花板** (A F-3): 「judge 零噪声」
   的判别力实际来自 9 个非满分项。看不见: 其余 5 份答案集上的 judge 行为。
8. **I3 对照只验 0/1 端点** (A F-4): E1 信号大半在 0.3333-0.75 中间分值区, 刻度间等距性未验。
9. **强制档 ≠ 生产档** (审查 I-3): 48 题全 both 是生产从未出现的反事实; 收益题与不可判池在
   auto 下**全判 study**。看不见: 放宽 router 后的真实混合分布。
10. **单模型单温度单 judge** (Bedrock sonnet / deepseek temp 0); judge 粗网格未修
    (fact gold 现状, 与 U1/U2 可比性优先)。换模型可能翻转。
11. **pt 分母 (48/30) 与比较集 (41/29) 不同源** (A F-7): 跨单元比 pt 须附 n_compared。
12. **I2 的「全 parse_ok」合取项本轮空转** (468 行全 True, A F-5): 是「未触发」不是「防线已验」。
13. **rejudge/main 级测试的零 LLM 是桩保护的** (守卫回归时零网络红, 但 socket 级禁网 fixture
    未建, Task 2 backlog)。

## 6. 本单元明确不能证明什么 (spec §8 + 审查方越界清单)

- **不能**说「both 零代价 / 免费」不带可比池限定 — 合法句式:「cards 41/48 与 docs 29/30
  可比池内已确证代价 0; 最坏界并列尺子确认 2 题 2.08pt」
- **不能**证明「both 不值得」(收益侧出局, 单库题集, both_ruler §5-10) — **也不能**反向拿
  +2.78pt 证明「both 更好 / 应放宽 router」: E2 明文收益不阻塞判定; 且全量强制 both 的聚合
  读数是 −0.69pt, 取 +2.78 是只取同一批数据有利的一半
- **不能**把 2.78pt 与 3.47pt 互比 (口径不同)
- **不能**对 E4 的 8 道不可判题任一单题下结论
- **不能**说「线上触发率 5/51」(那是 eval 题集分布) / 「14.6% 过了 I2 闸」(并集没闸)
- **不能**证明换模型 / 换温度 / 换 judge 下成立; **不能**证明判库正确性有变化 (router 未动);
  **不能**证明 N=8 / 现行席位最优
- **放宽 router 仍是新单元**, 须自带 U3 存续的 253 题路由闸 + 六条条款全套判据

## 7. 业务结论 (给判库修法线的前置判断, kickoff §0′ #1)

1. **「both 便宜 ⇒ 放宽 router」未获干净支持**: 冻结判词 cheap 只在可比池成立, 最坏界 2.08pt
   代价恰落在检索侧脆弱题上 (q14/q21 = 检索丢分**确实传导**到答题的两例), 聚合方向 −0.69pt。
   修法线的必要性**没有被解除**。
2. **现行触发面上的 both 是免费的** (最扎实结论): auto 实判 both 的 5 题两侧同分。
   ⇒ 修法方向如果只是「让该去 both 的题去 both」而非「把 study 题推去 both」, 答题侧无已证代价。
3. **判库欠账 10pt 本体再次现形**: `docs_v1_q15/q17/q53` + `st01_v2_q07` 路由打空 (gold 零命中)
   且 fallback 结构上捕获不到错判 — 修它要动 router 判据, 与 U3 §9 硬前置对齐。
4. 答题侧仪器已建立且判别力有实证 (I1 1.0 / 双向对照 1.0/0.0 / 逐题稳定集), 但 §5-1/2 的
   设计缺陷须在重启测量前修 (属判据变更, 需新单元 + 用户裁定)。

## 8. 复跑命令 (逐字, 在 `sdtm-rag/` 下)

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2   # → 1353 passed (2026-08-17 实测)
# 判定 (确定性, 读已落盘产物):
R=data/study/st01/eval/runs
./.venv/bin/python -m eval.u5_verdict \
  --cards-study $R/u5_cards_study_r1.json $R/u5_cards_study_r2.json $R/u5_cards_study_r3.json \
  --cards-both  $R/u5_cards_both_r1.json  $R/u5_cards_both_r2.json  $R/u5_cards_both_r3.json \
  --docs-study  $R/u5_docs_study_r1.json  $R/u5_docs_study_r2.json  $R/u5_docs_study_r3.json \
  --docs-both   $R/u5_docs_both_r1.json   $R/u5_docs_both_r2.json   $R/u5_docs_both_r3.json \
  --probe-cards $R/u5_probe_cards.json --probe-docs $R/u5_probe_docs.json \
  --controls-docs-pos $R/u5_ctrl_docs_positive.json --controls-docs-neg $R/u5_ctrl_docs_negative.json \
  --controls-cards-pos $R/u5_ctrl_cards_positive.json --controls-cards-neg $R/u5_ctrl_cards_negative.json \
  --output $R/u5_verdict.json                                    # rc=0, E2=cheap_on_this_ruler
```

run 产物 gitignored 本地件; 缺失时按 plan Task 4/5/6 命令重生成 (答题侧非确定, 重跑数字会变,
判定按冻结规则重算)。跑批日志含题面, 只在 `data/study/st01/eval/logs/u5/`。

## 9. 给下一单元的硬约束

1. **可比池限定词入闸**: 任何引用 E2 判词的文句, 同句必须有「可比池 / 41/48」字样; 出现
   「零代价 / 免费 / cheap」而无池限定 = 收口不合格 (审查方自检闸)。
2. **重启答题侧测量前先修判定设计** (§5-1/2/3): E1 并列最坏界口径 (或把 `max(both3) <
   min(study3)` 题移入确认代价) · E4 并集入闸 · I-1 结论词抑制。属判据变更, 须用户裁定 +
   新基线冻结, 不许沿用本轮判定脚本原样重测。
3. **变异抽检必须覆盖合取/并集项的每一半** (审查 I-2 / 抽检 B pattern: 多族只测一族 ·
   多遍只测一遍 · 对调型); 变异 harness 必须 purge __pycache__ + compile 前置检查 (假阴性
   与假还原两个坑本单元都踩实了)。
4. **+2.78pt 禁止作为放宽 router 的论据** (机制层: 全量 both 聚合 −0.69pt, 取一半是选择性
   引用); 放宽 router = 新单元, 判据含 U3 253 题路由闸六条条款 + 本单元最坏界口径。
5. **「fallback 全 False」引用必须带「4 题路由打空未触发」限定** — 建议下一单元把
   「auto 相对强制 study 的 source_recall 差」列为显式指标 (docs 侧 −10pt 即判库欠账本体)。
6. **q23r 三度出现** (U2 条款 3 驱动题 → 本轮 E4 不可判): 该题是答题侧不稳定的常驻样本,
   任何逐题结论先查它在不在池里。

## 10. 任务台账

| Task | 内容 | 状态 |
|---|---|---|
| 0 | 自检 + 分支 | DONE (1275 / 4329·959·114 / 87.5%) |
| 1 | routed/fallback 观测字段 | DONE (1 修复轮; federation 2 行 + attach 闸) |
| 2 | rejudge 探针 | DONE (3 修复轮; orig parse-fail 出分母 / judge_model 断言 / _boom 桩) |
| 3 | u5_verdict 判定脚本 | DONE (3 加固轮; 36 例; 阈值冻结 + 字面断言) |
| 4 | I3 双向对照 | DONE — PASS 1.0/0.0×2, parse_ok 24/24 |
| 5 | 4×3 答题矩阵 + probe | DONE — 12 run ALL OK, parse_fail 全 0 |
| 6 | auto 触发观测 | DONE — 逐位复现 U3, fallback 243 False (带 4 题打空限定) |
| 7 | 判定执行 | DONE — rc=0, cheap_on_this_ruler (双口径并列见 §2.2) |
| 8 | 三方核验 (规则 D 五方) | DONE — A 64/64 + B 148 变异 SURVIVED 0 + 审查条件通过 |
| 9 | 收口 | DONE (本文件 + kickoff/PROGRESS/worklog/CLAUDE.md 同步) |
