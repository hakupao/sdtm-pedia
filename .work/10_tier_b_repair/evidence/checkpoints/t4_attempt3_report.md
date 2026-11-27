# T4 attempt 3 主控汇报 (交协调方)

<!-- chain: E (plans) -->
> 状态: **T4.1 总闸: attempt 3 本身 = CONDITIONAL (唯一挡闸项 = 问题 A); 主人直接回答 A1 并经 R3L 改 4 条之后, delta 闸审 = PASS** (2026-11-27). T4.2 已按主人改定的口径关闭. 未 push, 未打 kb tag, 未做 T4.3. KB 全程没有改.
> 写作者 = 接手主控 (任务 `task_d444a180bef8`). 本文是索引式汇报, 结论都指向独立审查者的原文; 主控没有改判. 路径省略前缀 `.work/10_tier_b_repair/`.

## 1. 任务一: attempt 2 所列缺口 (不需要主人就能关的)

| 缺口 | 结论 | 证据 | 谁判的 |
|---|---|---|---|
| C3 逐表结案清单 | 已关: 60 张 = 49 已结 + 4 解冻轮改符号 + 7 批内重建 | `evidence/checkpoints/t4_c3_closeout.md` §5; `work/t4/c3_closeout.json` | 独立审查 A (`oh-my-claudecode:verifier`, `evidence/t4_gap_review_raw/review_a.md`: 独立配对 53 / 53, 12 张表重新逐格对渲染) → 总闸 attempt 3 判已关 |
| census 变化逐表说明 | 已关: 三时点 (`50c3958` / `00a2e93` / HEAD) 逐表配对, KB 表 501 / 500 / 497 | 同上 §3 / §4; `work/t4/census_tablediff.json` | 同上 |
| t0 baseline 过期 / 在 HEAD 重跑变异 | 已关: 原基线生成于 T0 的 KB, 所以过期; 现 KB 上另建基线 (`work/t4/t0_head/`, T0 基线不覆盖) 后重证 13 例全部施加、红绿全对 (ALL MATCH). 改台账两次之后各重建并重跑一次, 仍 ALL MATCH | `evidence/checkpoints/t4_t0_refresh.md` (§6 / §7 = 两次重建); `evidence/checkpoints/t0_mutation_head.log`; 脚本 `scripts/t4/t0_mutation_head.sh` | 独立审查 A (自己复跑 + 反向验证 2 组) → 总闸 attempt 3 判已关. **如实**: M4a 换了靶 (M-8, 主人已追认); 两次重建没有再送独立审查 (脚本与用例未改) |
| "规则 0 抽中" 各类补抽或全检 | 已关 (全检), 并引出下面 §2 的扩检 | `evidence/checkpoints/t4_supp_fullcheck.md`; 原始结果 `evidence/t4_supp_raw/` 等四个目录 | 审查者 `oh-my-claudecode:tracer`; 对汇总的独立审查 B / C (`oh-my-claudecode:code-reviewer`, `review_b.md` / `review_c.md`) → 总闸 attempt 3 判已关 |
| ATOM_ERR / PDF_TYPO 补抽 | **部分关** (总闸 attempt 3 的判断): PDF_TYPO 每一条都被独立审查者看过; ATOM_ERR 的 S1-R1 类 157 条里约 83 条没有被单独逐条看过 (既有状态) | `evidence/t4_gate_raw/attempt3_report.md` D 项; **后续见 §7** (加查: 确切 77 条, 全检 83 → 1 条不成立, 待主人定) | 总闸 attempt 3 |
| 文档一致性 | 已关; attempt 3 另指出 5 处、delta 另指出 8 处过期文字, 文字类都已改, 2 处在台账辅助字段里的记为已知 | `evidence/checkpoints/t4_gate_review.md` "§attempt 3" 与 "§attempt 3 delta" 的主控处理 | 两位总闸审查者 |
| PLAN 修订稿 | 已关: `PLAN.md` v1.4.1 → v1.4.3 (FIG 11、T4.2 口径、G-TB3 口径注、Q9 已触发、现值) | `PLAN.md` 状态行 / §5.1 口径注 / Changelog | 总闸 attempt 3 判已关 |

## 2. 补抽结果 (四轮独立审查共 885 条; 没有查出 KB 内容写错, 查出的是台账标签不准)

| 轮 | 条数 | 结果 |
|---|--:|---|
| 补检 ("0 抽中" 各类全检) | 203 | 成立 171 / 内容成立但标签级别偏高 30 / **不成立 2** (06 时期的旧 "逐字有" 标签) → 触发 PLAN Q9 |
| Q9 扩检 | 192 | SDTM v2.0 旧 "等价" 127 条全检 → 51 条不成立 (49 条变量表行 / 表头 + 2 条目录条目); SDTMIG 旧 "等价" 抽 65 条 → 0 不成立 |
| 第二轮 | 175 | 跨文档指针 27 全检 → 无内容错 (3 条标题口径); 已登记笔误的同类原子 103 全检 → 15 条应为 "PDF 笔误"; "PDF 笔误" 抽 45 → 0 不成立 |
| 第三轮 (主人选的追加审查) | 315 | SDTMIG 旧 "等价" 再抽 150 → 0 不成立 (累计 215 条 0 错, 95% 上界约 1.4%, 不是全检); "PDF 笔误" 剩下 99 全看 → 94 成立 / 4 多标 / 1 判不了; 标题类抽 60 → 内容全成立; 范围外笔误同类 6 → 全部确认 |

由此改台账两批共 **82 条** (清单 `evidence/checkpoints/t4_relabel_pending.md`, 全部已执行):
- **R2L, 78 条** (提交 `5d7e4cb`): 53 条 → "有意不收", 25 条 → "PDF 笔误". 执行者 `oh-my-claudecode:executor` → 结构审查 `oh-my-claudecode:code-reviewer` PASS + delta PASS → 语义抽检 `oh-my-claudecode:verifier` 33 / 33. `evidence/checkpoints/t4_round2_ledger_W.md` / `t4_round2_ledger_review.md` / `t4_round2_ledger_audit.md`.
- **R3L, 4 条** (提交 `d794fb6`): 4 条多标的 "PDF 笔误" → "逐字有". 执行者 → 结构审查 PASS (隔离副本整链三遍 + 7 个变异). `evidence/checkpoints/t4_round3_ledger_W.md` / `t4_round3_ledger_review.md`. **没有另设语义抽检** (这 4 条的语义由第三轮审查者、总闸 attempt 3 审查者、delta 审查者各自独立复核过).
- 两批清单外的标签变化都是 0. 台账 md5: `60729f7b…` → `16024ac0…` → `438098704becc84eda01a925b80defaa`.

现值 (`python3 -I .work/10_tier_b_repair/scripts/t4/t4_coverage_decomp.py`): 过闸口径 U-1 B 9860/9933 = **99.2651%** (闸线 99.0192%); strict 9493/9933 = 95.5703%; mapped 99.3511%; 内容指标 90.6227%. 范围内 174 节残留 0. 历史: attempt 2 时 99.2690% / 95.8041%.

## 3. 主人原话 (都是主人直接在接手主控聊天里发的普通消息; 逐字记录, 没有改写或补全)

文件: `evidence/checkpoints/t4_owner_confirmation.md` (第一节 = 上一任主控会话的记录, 来源与局限照其自述; "第二轮" 一节 = 本会话).
- 消息 1 「可以没问题」 — 范围不明, 主控没有当作逐项回答, 逐项列出 13 个小问的建议选项后追问.
- 消息 2 「是，都按建议」 — 登记为 13 个小问全选建议项 (1A / 2A / 3A / 4a-B / 4b-B / 4c-B / 4d-A / 5 追认 M-8 / 6A / 7a-C / 7b-A / 8A / 9A).
- 消息 3 「继续」 — 没有回答问题 A / B; 主控登记为未答, 没有替他选.
- 消息 4 「A1、B1、追认 M-9」 — 4 条多标改回 EXACT; 判不了的 1 条维持并写明; 追认 M-9.
- 没有任何一项选了要改 KB 的选项 (1B / 6B / 8B 都没选). 逐项登记: `evidence/checkpoints/t4_user_decisions.md` §000c; 主控实施决定 §000b (M-1 ~ M-10).

## 4. 总闸结论 (照实写成两步, 不压成一个词)

1. **attempt 3 = CONDITIONAL** (`feature-dev:code-reviewer` 新实例; 原文 `evidence/t4_gate_raw/attempt3_report.md`; 归档 `evidence/failures/step_T4.1_attempt_3.md`): G-TB1 ~ G-TB9 无 NOT_MET (MET 4 / 带条件 5); 自挑 10 条改标全成立; 裁定来源三问都判 "足够, 带已公开的局限"; 唯一挡闸项 = 问题 A (4 条多标的 "PDF 笔误", 当时主人未答).
2. 主人答 A1 → R3L → **delta 闸审 = PASS** (另一个 `feature-dev:code-reviewer` 新实例; 原文 `evidence/t4_gate_raw/attempt3_delta_report.md`): 挡闸项已关, 4 条文本层重判 4 / 4 成立, 没有哪条闸变坏, 没有新的挡闸项.

誊录: `evidence/checkpoints/t4_gate_review.md` "§attempt 3" 与 "§attempt 3 delta". 两位审查者都没有 Bash: 复跑输出由主控事先跑好 (`work/t4/gate_prerun.log`), 他们的数字分别标了自算 / 读日志 / 采信; 渲染页他们都没看.

## 5. 仍开但不挡闸 (如实)

- **M-10** (R3L 落地时的机制选择, 含 "这 4 条没另设语义抽检, trace 里这一批只有两类审查角色") 待主人追认; delta 审查者把后一点记在 G-TB8 的字面条件下. 已在聊天里告诉主人 (记录在 `t4_owner_confirmation.md` "主控的第四次告知").
- ATOM_ERR 的 S1-R1 类约 83 条没有被单独逐条看过 — 是否加一轮由主人定 (协调方已说会转告; 主人还没表态, 没做). **后续: 主人选了加查, 已做, 见 §7.**
- 抽样而非全检: SDTMIG 旧 "等价" 2207 条抽 215; 标题类 71 / 316; 笔误同类宽筛候选 (范围内 169 / 范围外 142) 未审 (主人 4d = A); 范围外跨文档指针 146 条不动 (主人 7a = C).
- 约 80 条 "标签级别" 后续项 (内容成立); KB 观察项 O68-O71 只记录没修 (KB 冻结).
- 两次 T0 基线重建未送独立审查; 给主人的一页第 3 稿未再送审; 主人确认记录的形式局限 (短句 + 选项清单, 无截图); 上一任会话的 trace 整点时间戳无法还原.
- 台账辅助字段两处已知: `ig34_p0412_a006` / `a008` 还留着 06 时期的 `discrepancy` 文字; R3L / R2L 新写行的 `ts` 沿用固定值 (早于主人决定日, 决定日期另记在证据字段里).

## 6. 状态 (命令可复跑)

- `git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a` (与任务开始时相同; `git status --short knowledge_base archive releases` 为空). `knowledge_base/`、`archive/`、`releases/`、sdtm-rag 仓都没碰.
- 未 push: `git status -sb` 显示 `main...origin/main [ahead N]` (本报告提交前 N = 123; 最终值与最终提交号见 `worker_done` 消息).
- 未打 tag: `git for-each-ref --sort=-creatordate refs/tags | head -1` 最新一个仍是 `kb-2026.11.25` (2026-11-25), 早于本任务.
- 任务基线 `d46f8af` 之后本地共 20 多个提交, 其中 `c555bd8` 是上一任主控会话的, 其余是本会话的 (`git log --oneline d46f8af..HEAD`).
- 未做 T4.3. 交接: `HANDOFF.md` 最后一节; 进度 `_progress.json`; `docs/PROGRESS.md`.

## 7. 后续: ATOM_ERR 加查 (2026-11-27 夜; 新会话主控, 任务 `task_5b6b27f6c68d`)

- §1 表里 "ATOM_ERR / PDF_TYPO 补抽 = 部分关" 与 §5 第 2 条的后续. 主人选了 "加查" (协调方转述). 汇总: `evidence/checkpoints/t4_atomerr_fullcheck.md`.
- 确切条数 77 (不是约 83; 83 = 157 − 74, 没扣总闸样本 5 条和预筛 1 条). 全检 83 条 (77 首次 + 6 盲复检), 审查者 `oh-my-claudecode:tracer` ×4: **成立 82 / 不成立 1 / 判不了 0**.
- 不成立: `ig34_p0124_a001` — 标的是 "原子抽错", 实际原子没抽错、KB 逐字承载, 应为 "逐字有". 第二位不同类型的审查者 (`general-purpose`) 盲判相同. 不是 KB 内容错.
- 另有 8 条 (`B-CE T-2` 那组) 判的是成立, 但取决于一条口径 (代码值内部的一个空格算不算空白归一), 审查者点名要上面定 → 问题 D, 主控没裁.
- 台账**没改**, KB 没改. 问题 C (C1 改回 EXACT / C2 维持) 与问题 D (D1 维持 / D2 改 EXACT / D3 改 PDF_TYPO) 等主人直接定. 数字影响 (副本实算): 过闸口径不变 99.2651%; strict 95.5703% → 95.5804%.
- 这一项从 "部分关" 改成什么状态: 由总闸角色或协调方判, 主控不判.
- 本节与 `t4_atomerr_fullcheck.md` 是主控写的, 没有送独立审查.
- M-10: 本会话开头又问了一次, **主人未答** (`t4_owner_confirmation.md` "第三个会话" 一节).
