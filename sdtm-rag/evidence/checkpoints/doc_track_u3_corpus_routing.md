# doc 轨 U3 — 判库欠账 (corpus routing) 收口证据

> 状态: **FAIL 收口** (2026-08-14, 用户裁定) —— Task 8 全闸条款 1 触发 (fatal 9 ≠ 0),
> 按 spec §7 触发后果「修法退回」执行, prompt 改动已 revert (`c754bed`), 生产行为回到基线。
> 分支 `doc-track-u3` · spec `docs/superpowers/specs/2026-08-13-doc-track-u3-corpus-routing-design.md`
> · plan 同名 plans/ 文件 · 失败归档 `evidence/failures/u3_task8_attempt_1.md` (规则 B)
> 数据红线: 题集 / 题面全在 `data/study/` (gitignored)。**本文件零题面正文, 只有 id 与数字。**

## 1. 架构改动面

**最终生产改动面 = 零。** Task 7 曾改 `server/federation.py` `_ROUTER_SYSTEM`
(规则 1 排除条款 + 规则 3 `both` 判据 + 兜底句重写, `2c060a5..35d717a`, 共 5 轮);
Task 8 全闸条款 1 触发后, 用户裁定退回, 两文件已还原至 `1690d38` (Task 7 前)。

**本单元存续产物** (不随退回撤销):
- 路由 gold 扩到手順書型: 新写 42 题 + 确定性 dev/heldout 划分 (12/12/12/6), gold 红线闸 `eval/lint_gold.py` 扩展
- `both` 档三档确定性尺子 (只量不改): `evidence/checkpoints/doc_track_u3_both_ruler.md`
- 基线冻结仪器: `eval/run_routing_eval.py` 全 253 题三遍跑批 + `u3_baseline_run_{1,2,3}.json` (gitignored, 本地)
- 六条条款判定脚本: `eval/u3_task8_verdict.py` (plan Task 8 Step 3 + spec §7.1 多数类基线并排)

## 2. 数字

### 2.1 both 尺子 (Task 2, 三遍全一致, 详见 both_ruler 检查点)

doc 侧 1.0000 (结构恒等, 非测得稳健性); cards 侧 0.8750 → 0.8229 (−5.21pt, 归因闭合 4 题);
该代价当前**悬着未付** (脆弱 4 题现无一被判到 `both`)。

### 2.2 Task 8 全闸六条条款 (Task 7 终态 prompt, 三遍 253/253 零漂移)

| # | 条款 | 结果 | 判定 |
|---|---|---|---|
| 1 | 每遍 fatal=0 且 legacy ≥ 178 | fatal=**9** (三遍同), legacy 179/181 | **⛔ 触发** |
| 2 | heldout ≥ dev − 25pt | dev 100% / heldout 91.67%, gap 8.33pt | 未触发 |
| 3 | dev ≥ 10/12 | 12/12 | 未触发 |
| 4 | distractor 较基线降 ≤ 1 | 7/12 → 7/12, drop 0 | 未触发 |
| 5 | final 只报告 | q15 study✓ / q17✗ / q53✗ (基线 0/3 → 1/3) | 已报告 |
| 6 | 三遍不一致点名 | unstable = 0 | 未触发 |

⚠ spec §7.1: dev/heldout 多数类基线各 100%, 条款 2/3 单独零判别力, 引用必须连同条款 1/4。
新写 42 题多数类 57.1%; 全 253 题多数类 cdisc 64.4%。

**改动面**: 全 253 题仅 4 题预测变化 —— 修好 `q15`(final)/`amb_03`/`amb_05`, 变坏 `dist_05`
(both→study, **非致命错变致命错**); `u3_doc_02`(规则 1 唯一 held-out 目标)纹丝不动。
fatal 10 → 9, 修 2 坏 1, 距 0 相差 9 —— 非边缘情形。明细见失败归档。

### 2.3 退回验证 (2026-08-14, 可复跑)

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2   # → 1259 passed
./.venv/bin/python -m eval.run_routing_eval --runs 3            # 三遍
# routing_run_{1,2,3}.json 与 u3_baseline_run_{1,2,3}.json 比对: summary 相同 + 逐题 pred 零差异
```

结果: pytest **1259 passed**; 三遍复跑与冻结基线**逐题 EXACT MATCH** (fatal=10, 253/253 稳定)。

## 3. 触发 / 豁免

- **条款 1 触发, 无豁免**。spec §1.6 事前登记的灰色情形 (唯一剩 `u3_doc_02`) 未达到 —— 实剩 9 个。
- 用户裁定 (2026-08-14): 三选一 (退回 / 换实现方开 attempt 2 / 带限制豁免收口) 中选**退回**。
- 阈值 / `score_run` fatal 定义 / gold 全程一字未动 (条款 1 附带禁令遵守)。
- 条款 5 纪律已执行: 看过 final/heldout 结果后未再改 prompt; 本 controller session 已见
  held-out 题面 (取证需要), **若未来开新 attempt, 实现方必须是全新 session** (spec §6.2 防线 2)。

## 4. 三方核验 (Task 9, 规则 D 五方不同 session, 2026-08-14 用户点单执行)

核验对象 = 存续产物 + Task 8 数字 (FAIL 收口后由用户定范围)。执行序: 审查方 + 抽检方 A
并行 (均只读) → 抽检方 B 单独跑 (变异会临时改文件)。

| 方 | subagent_type | 结论 | 报告 |
|---|---|---|---|
| 审查方 | code-reviewer (opus) | **Approve with findings: 0 Critical / 4 Important / 5 Minor** | `.superpowers/sdd/2026-08-13-doc-track-u3-corpus-routing/task-9-review.md` (gitignored, 本地落盘) |
| 抽检方 A | debugger (opus) | Task 8 **全部 10 项声称复现, 0 不复现** (算术零错); 新 finding 7 条 (2 HIGH / 3 MED / 2 LOW), 全在判据/证据设计层 | `evidence/step_u3_audit.md` (进 git) |
| 抽检方 B | test-engineer (opus) | **69 变异: 首轮 KILLED 56 / SURVIVED 11 → 补 10 断言 (16 case) 后 SURVIVED 0**; 两大缺口 (判定脚本零测试 / Task 5 红线修法无回归守卫) 均当场补上 | `evidence/step_u3_audit_mutation.md` (进 git) |
| controller | 本 session | 非自洽复算全对上 (组数直数 253 / base fatal 10 / after 9 / revert EXACT MATCH); 抽验 M43 变异真红; 两份进 git 报告独立泄漏扫描 (448 敏感串 + held-out 词表) **零真实泄漏** | 本文件 + SDD progress.md |
| 出题方 / 划分方 | scientist / 另 session | Task 4/5 已隔离执行 (见 §10 台账) | Task 4 prompt 归档 + `test_u3_gold_redline.py` |

审查方必答三问的答案 (机制层, 详见其报告 §2):
1. **规则文本散文层 pattern-level, 但有效层 example-level** —— 实测词表绑定力: 规则 2
   词表内 29 题 0 判 cdisc; gold=both 带映射词 5/5 vs 不带 0/6。词表是三选一决策结构的必然产物。
2. fatal 减法 (减 `final` 组) 本身无漏; 漏在**条款 4 的 exact 口径** (见 §6-6) 与
   **u1_doc 组 study→both 漂移真空** (见 §6-9)。
3. 代码阅读层无「该红不红」; 反向发现 I-4 (`by_group[*].passed` 用无条款使用的 0.95)。

核验后基线: pytest 1259 → **1275 passed** (+16 = 抽检方 B 补的断言与新测试模块
`test_u3_task8_verdict.py`)。findings 处置 = **记已知限制 + 给下一单元硬约束 (§9), 本单元不修**
—— 审查方自评四条 Important 均不影响 FAIL 收口结论的正确性, 它们全作用在「下一轮怎么判」上,
应在重启修法单元之前处理; 若用户要现在修, 属新单元范围。

## 5. 业务结论与遗留

1. **判库欠账仍在**: fatal 10 个原样 (both→study 6 / cdisc→study 3 / study→cdisc 1),
   动机题 q17/q53 仍错。修复路径经一整轮 pattern-level 尝试未达标, 提示盲写概念对
   held-out 形态的覆盖上限, 或需要不同的机制 (非 prompt 措辞层)。
2. **尺子盲区 (遗留待裁定)**: 条款 4 用 exact 口径, 抓不到「非致命错→致命错」型回归
   (`dist_05` 实证被 7/12 持平掩盖)。未来单元若重启修法, 建议先裁定是否改用 fatal 口径。
3. **Task 7 仪器盲区是设计使然**: 可见集 193 (legacy+dev) 出口绿 ≠ 全闸绿, 防对症下药的
   代价就是全闸才见真章。本次流程按设计走完, 闸如实拦下 —— 流程本身工作正常。
4. spec §9「不能证明什么」全部仍然成立 (逐条见 §7)。

## 6. 已知限制 (每条注明它看不见什么)

1. **席位不对称未改**: `federation.py` 的 `k_each=8` 只作用于 cards, `study_corpus.py` 的
   `doc_seats` 不随缩放 ⇒ `both` 下 doc 在 study 半边占比 35% → 50%。本单元只量不改
   (spec §2)。看不见: `both` 档的真实席位代价是否来自这个不对称。
2. **held-out 只有 12 题, 且与 dev 章几乎不重叠** (19 章中仅 5 章两组都有; 抽检 A-5)
   ⇒ 条款 2 的 gap 是低分辨率读数。看不见: 章间泛化。
3. **答题侧未测**: 全部数字是检索/判库侧。看不见: 判库对答案质量的影响 (判库准确率 ≠ 答案质量)。
4. **`both` 真实触发率未测**: doc 30 题在 `auto` 下从不触发 `both`; B2 的 −5.21pt 代价
   悬着未付 (脆弱 4 题现无一被判到 `both`)。看不见: `both` 档在生产里实际发生什么。
5. **`final` 三题不计入 fatal 口径** (条款 5 只报告)。看不见: 这三题上的回归不拦闸。
6. **条款 4 的 exact 口径对「非致命错 → 致命错」恶化零敏感** (抽检 A-1 HIGH; `dist_05`
   实证被 7/12 持平掩盖; 极端情形 12 题全致命化仍持平)。审查方补充: 同一口径还**误杀真改善**
   (`dist_07/10/11` study→both, 实测)。尺子方向本身错了 —— 改法 (fatal 计数或 fatal+exact
   双列) 待用户裁定, 本单元不动阈值与口径 (spec §7 禁令)。
7. **条款 2/3 单独零判别力** (抽检 A-2 HIGH): 「一律 study」常量规则即可满足, 且 heldout 上
   常量还赢真实路由器 8.33pt。多数类基线并排是强制的 (spec §7.1), 单独引用 dev/heldout 数字
   等同报多数类基线。
8. **run json 无 run 级元数据**, 「三遍」对事后读者不可证伪 (抽检 A-3; mtime 旁证已归档,
   非指控)。看不见: 产物与跑批的绑定。
9. **u1_doc 27 题的 study→both 漂移方向上, 六条条款零检出** (审查 I-3): 修法受力方向上有
   一整组真空 (对照: legacy 的 178 floor 挡的正是同种漂移)。
10. **仪器残缺已知未修**: `--runs 0/1` 也打印「三遍一致」且 rc=0 (审查 I-1, 实测探针);
    `u3_task8_verdict.py` 无输入校验 (审查 I-2, baseline=after 拷贝错则条款 4 必 PASS ——
    零测试一半已由抽检方 B 补 9 case 钉住, 校验缺口仍在); `by_group[*].passed` 用无条款
    使用的 0.95 阈值, 与条款 5/条款 2 的判定矛盾 (审查 I-4, 误导性字段)。
11. **审查方报告不进 git** (`.superpowers/` gitignored), 只在本地落盘; 本文件摘录其结论。

## 7. 本单元明确不能证明什么 (spec §9)

- **不能**证明生产 `auto` 下答案质量变好 —— 判库准确率不是答案质量
- **不能**证明 `both` 档是对的席位配置 —— 只量不改
- **不能**证明新触发条件对**未来**的手順書题泛化 —— held-out 只有 12 题
- **不能**证明答题侧不受影响 —— 答题侧仪器 (kickoff #4) 未做, 全距 6.25pt
- **不能**证明 27.42% 未章节化原文 (C1 L1) 相关的问题变得可答 —— 本单元不碰语料
- 追加 (spec §7.1 处置 #3): 条款 2/3 的数字**不得单独引用**, 必须连同条款 1/4 与多数类基线

## 8. 复跑命令 (逐字, 在 `sdtm-rag/` 下)

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2   # → 1275 passed (2026-08-15 实测)
./.venv/bin/python -m eval.run_routing_eval --runs 3            # rc=1 是预期 (基线 fatal=10)
./.venv/bin/python eval/u3_task8_verdict.py                     # 六条条款判定 (读 u3_{baseline,after}_run_*.json)
./.venv/bin/python -m eval.compare_runs data/study/st01/eval/runs/u3_both_docs_r{1,2,3}.json
./.venv/bin/python -m eval.compare_runs data/study/st01/eval/runs/u3_both_cards_r{1,2,3}.json
```

run 产物均 gitignored 本地件; 缺失时按 plan Task 2/6/8 的命令重生成 (三遍纪律不可省)。

## 9. 给下一单元的硬约束

1. **重启修法前先处理审查方 4 Important 与抽检 A 的 2 HIGH** (§6-6/7/9/10) —— 它们全作用在
   「下一轮怎么判」上; 条款 4 口径改法 (fatal 计数或双列) 是其中唯一动尺子的, 须用户裁定。
2. **`both` 代价未知是这条线的真正前置** (审查方机制层结论 #2): 全套判据把 `both` 当「更宽但
   安全」, 若答题侧实测 `both` 便宜, 正确动作是**放宽 router 而非磨尖它**, 整条修法线可能失去
   必要性。先补 `crowding_and_gold_integrity.md` 自述的那个未知 (答题侧仪器, kickoff #4)。
3. **措辞杠杆已到底** (机制层结论 #3): prompt 已含最强形式兜底指令而模型不执行 (三遍零方差),
   五轮重构净动 3 题。下一轮若仍走 prompt 措辞层, 先说明凭什么认为还有行程; 审查方的决策结构
   探针 (三选一 → 两次二值取并集, 零措辞改动) amb fatal 6→3 但打坏 `ja_supp_b01` 且触发
   条款 4 口径 —— **有信息量的失败, 不可原样采纳**。
4. **实现方必须全新 session** —— 本 controller 与三个核验 session 均已见 held-out 题面
   (spec §6.2 防线 2)。
5. **`u3_amb_01/04/06` 的 gold 应人工复核** (审查方点名: 两种独立决策形式都判不需要 cdisc 侧)
   —— 复核属出题侧, 须在冻结新基线之前做, 不许在看过 prompt 效果后改。
6. **gold / 阈值 / `score_run` fatal 定义仍一字不许动** (spec §7); `LEGACY_EXACT_FLOOR = 178`。

## 10. 任务台账

| Task | 内容 | 状态 |
|---|---|---|
| 1-6 | 尺子 / gold / 划分 / 基线冻结 | DONE (存续) |
| 7 | prompt 两方向同修 (5 轮) | DONE 后被裁定退回 (`c754bed`) |
| 8 | 全闸六条条款判定 | DONE — 条款 1 触发, 归档 + 上报 + 退回 |
| 9 | 三方核验 (规则 D 五方) | DONE 2026-08-14 (`01ff795`) — 见 §4; findings 处置 = 记限制 (§6) + 硬约束 (§9) |
| 10 | 收尾 (checkpoint 补完 / kickoff / PROGRESS / worklog / AGENT_GUIDE) | DONE 2026-08-15 (本 commit) |
