# T4.1 总闸独立审 brief v3.0 — attempt 3 (feature-dev:code-reviewer, 新实例)
<!-- chain: E (plans) -->
> v1.0 (attempt 1)、v2.0 (attempt 2) 保留不改 (规则 B). 本次: 复判**证据层** (G-TB1..9) + 样本层延续性 + 裁定来源是否足够 + attempt 2 所列缺口的现状. 只读: 不改任何文件, 不 commit; 结果以回复正文返回, 主控原样誊入 `evidence/checkpoints/t4_gate_review.md` §attempt 3. 主控不改判 (规则 D).
> 本文只给事实与要判的问题, 不给预期结论. 你判断不足就如实写, 这本身是交付物.

## 背景 (只给事实)
- 仓库 `/Volumes/DevSSD/Project/sdtm-pedia`, 项目目录 `.work/10_tier_b_repair/` (下文路径省略此前缀). 标签定义、PDF 路径、文本层见 `subagent_prompts/t4_gate_reviewer_v1.0.md` "背景" 节. 闸定义: `PLAN.md` §5.1 (G-TB1..9 及其下 "口径注"), §5.0 范围, T4.1 / T4.2 行.
- attempt 1 / attempt 2 的结论与缺口: `evidence/checkpoints/t4_gate_review.md` (attempt 2 在 "§attempt 2" 一节; 归档 `evidence/failures/step_T4.1_attempt_2.md`).
- `knowledge_base/` 自 attempt 2 以来**没有改过** (`git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`; 下游在这棵树上预演, 冻结). attempt 2 之后改的只有台账、登记表、脚本与文档.
- attempt 2 之后发生的事 (全部本地提交, 未 push; 交接摘要在 `HANDOFF.md` 最后两节):
  1. **上一任主控会话记录的主人确认**: `evidence/checkpoints/t4_owner_confirmation.md` 第一节 (提交 `c555bd8`). 记录人是上一任主控会话; 接手主控与协调方都没有在别处再看到那条原文. 协调方对此的说明原文: `evidence/checkpoints/t4_coordinator_note_20261127.md` (经消息通道, 是转达).
  2. **接手主控补做 attempt 2 的缺口**: G-TB4 C3 逐表结案 + census 三时点逐表说明 `evidence/checkpoints/t4_c3_closeout.md`; G-TB9 在现 KB 上重证 `evidence/checkpoints/t4_t0_refresh.md` (日志 `evidence/checkpoints/t0_mutation_head.log`); "0 抽中" 各类全检及其引出的 Q9 扩检、第二轮、第三轮 — 汇总 `evidence/checkpoints/t4_supp_fullcheck.md`, 原始结果 `evidence/t4_supp_raw/`、`evidence/t4_q9_raw/`、`evidence/t4_round2_raw/`、`evidence/t4_round3_raw/` (审查者 `oh-my-claudecode:tracer`; 共 885 条), 归档 `evidence/failures/step_T4.SUPP_attempt_1.md`; 对主控这几份产出的独立审查原文 `evidence/t4_gap_review_raw/review_{a,b,c}.md`.
  3. **主人第二轮**: 提问页 `evidence/checkpoints/t4_owner_decisions_round2.md` (第 3 稿). 主人在接手主控的聊天里直接发了三条消息, 逐字记录、主控两次提问的要点、逐项登记都在 `t4_owner_confirmation.md` "第二轮" 一节; 裁定表 `evidence/checkpoints/t4_user_decisions.md` §000c; 主控实施决定 §000b (M-1 ~ M-9).
  4. **改台账 (R2L, 提交 `5d7e4cb`)**: 78 条标签 (53 → INTENTIONAL_EXCLUDE, 25 → PDF_TYPO) + 登记表 272 → 274 行 + 9 行登记更正 + 5 条原子补登记指针. 规格 `subagent_prompts/t4/t4_round2_ledger_spec_v1.0.md`; writer (`oh-my-claudecode:executor`) `evidence/checkpoints/t4_round2_ledger_W.md`; reviewer (`oh-my-claudecode:code-reviewer`) `evidence/checkpoints/t4_round2_ledger_review.md`; auditor (`oh-my-claudecode:verifier`) `evidence/checkpoints/t4_round2_ledger_audit.md`. 清单 `work/t4_r2l_relabel.json`; 改前备份 `work/coverage_ledger.wc.pre_r2l.jsonl`; 逐行 diff `work/t4/r2l_ledger_diff.txt`.
  5. R2L 之后主控做的: `scripts/t4/t4_supp_report.py` 改为在改前备份上预演并核对工作台账, 重生成 `t4_supp_fullcheck.md` (§1-§6) 与 `t4_relabel_pending.md`; T0 变异基线重建并重跑 (`t4_t0_refresh.md` §6); `PLAN.md` v1.4.2、`HANDOFF.md`、`_progress.json`、`audit_matrix.md` 更新; 确认清单 `evidence/checkpoints/t4_ack_lists.md` 由 writer 重生成.
- **你没有 Bash.** 需要复跑的命令已由主控在提交 `a88a585` 上串行跑好, 原样输出在 `work/t4/gate_prerun.log` (脚本 `scripts/t4/t4_gate_prerun.sh`; 日志头写有当时的 HEAD、KB 树、台账 md5). 该提交之后的提交只加了这份日志、本 brief、trace 行, 并给 `t4_supp_report.py` 的一句汇总措辞加了时点说明后重生成两份汇总 (台账、登记表、其它脚本与数据未变; 日志末尾有各数据文件的 md5 可对). 数字请尽量用 Grep / Read 自己核 (例如对 `work/coverage_ledger.wc.jsonl` 按 `"verdict": "…"` 计数), 核不了的标明 "[读日志]" 或 "[采信]".

## 没有经过独立审查的东西 (如实列出, 由你决定怎么对待)
- 给主人的一页 `t4_owner_decisions_round2.md` 第 3 稿 (第 1、2 稿各被审过一次, 第 3 稿是照审查意见改的, 改完没有再送审).
- R2L 之后的 T0 基线重建与重跑 (`t4_t0_refresh.md` §6; 脚本与用例未改).
- R2L 之后主控改的 `scripts/t4/t4_supp_report.py` 与重生成的两份汇总; 新脚本 `scripts/t4/t4_r2l_sample_overlap.py`; `scripts/t4/t4_gate_prerun.sh` 新增的几段.
- `HANDOFF.md` / `PLAN.md` v1.4.2 / `_progress.json` / `audit_matrix.md` 的这次更新.

## 未决项 (主控没有替任何人定; 每一条请判 "挡闸 / 不挡闸, 记为已知局限 / 需主人", 写理由)
1. 问题 A: 第三轮查出 4 条**多标**的 PDF_TYPO (`ig34_p0412_a006` / `a007` / `a008`、`ig34_p0413_a010`; 审查者判其自身 PDF 原文无笔误、KB 与 PDF 逐字一致, 应为 EXACT). 主人被问后只回了「继续」, 没有选; 现仍为 PDF_TYPO. 改回对 U-1 B 口径无影响, strict 口径 +4 条 (`work/t4/supp/scenarios.json` 最后一项).
2. 问题 B: `ig34_p0293_a038` (登记 `B-MK T-2`) 第三轮审查者判 UNVERIFIABLE (折行处无法判定有没有空格); 主人未答; 现为 PDF_TYPO.
3. M-9 (R2L 落地时的机制选择, `t4_user_decisions.md` §000b) 待主人追认. M-7 里那处 "p0362_a010 归 M-4" 的更正发生在第一节所记的确认之后.
4. `t4_owner_confirmation.md` 第一节的局限 (一个词加多选勾选、无截图、记录人是上一任会话), 以及第二轮三条原话 (「可以没问题」/「是，都按建议」/「继续」) 能否覆盖登记的 13 个小问 — 请读原文自己判.
5. 第一节里主人确认 U-1 口径时写的现值是 99.2690% / strict 95.8041% (改前台账); R2L 之后是 99.2651% / 95.5301%. 第二轮那一页给他看过各选法的预演数字表.
6. 抽样而非全检的部分: SDTMIG 范围内 06 旧 EQUIVALENT 2207 条共抽 215 条 (0 不成立); 标题类旧标签 316 条审过 71 条; 笔误同类的宽筛候选 (范围内 169 / 范围外 142) 未审 (主人 4d = A); 范围外跨文档指针 146 条不动 (主人 7a = C).
7. 约 80 条 "标签级别" 后续项 (内容成立, 只是 EXACT / EQUIVALENT / ATOM_ERR 之间的级别; `t4_supp_fullcheck.md` §6) 与审查者顺带记录的 KB 观察项 (`work/out_of_scope_findings.md` O68-O71; KB 冻结, 只记录).
8. `trace.jsonl` 里上一任会话的整点时间戳无法还原 (attempt 2 G-TB8 已指出); 接手主控追加的行用真实时钟.

## 你要判的
A. **G-TB1..G-TB9 逐条**: MET / MET_WITH_CONDITION / NOT_MET, 每条给依据 (文件:行, 或日志里的命令与输出). 至少核:
   - 台账标签计数; G-TB1 残留与三类 (ATOM_ERR / PDF_TYPO / FIGURE_DEFERRED) "每条有登记 + 用户 ack" 的现状 (`t4_ack_lists.md` 的 "决定来源" 列; 上面未决项 1 / 2 对 G-TB1 意味着什么由你判); G-TB2 (范围内口径与字面值); G-TB3 四口径对照 PLAN 字面 "≥ 99.02% 且不下降" 与口径注.
   - G-TB4: `t4_c3_closeout.md` 是否关掉了 attempt 2 的 "C3 逐表结案清单仍缺" 与 "census 变化未逐表说明"; 抽几张表自己对一下 (`work/t4/c3_closeout.json`、`work/t4/census_tablediff.json`).
   - G-TB5: `audit_matrix.md` 是否齐; 规则 A 的抽检在 R2L 上有没有做、N 是否事先定.
   - G-TB6: 日志里的反向溯源输出.
   - G-TB7: 日志里的 live docs.
   - G-TB8: R2L 的 writer / reviewer / auditor 是否三个不同 subagent_type (`trace.jsonl` 的 `T4.R2L.*` 行); 主控有没有自己写台账的迹象 (如实写你能证明到哪一步).
   - G-TB9: `t3_mutation` 与 `t0_mutation_head` 在现状上的输出 (日志); `t4_t0_refresh.md` 的换靶 (M-8) 与 §6 重建.
B. **样本层延续性**: attempt 1 / 2 的 84 条样本 (`work/t4/gate_sample.jsonl`) 与 T4.2 的 42 条 (`work/t4/human_sample.jsonl`; 主人抽查的 6 条见 `evidence/checkpoints/t4_human_verdicts.md`) — R2L 改的 78 条 + 5 条指针行与它们的交集见日志 "R2L change set … overlap" 一段 (脚本 `scripts/t4/t4_r2l_sample_overlap.py`), 请自己用 Grep 抽核几条. 有交集的逐条重判; 没有的注明沿用. 另请从 78 条里**自己挑至少 8 条** (四组都要有: R1-row / v2.0-TOC / registered-typo / registered-typo-oos; 清单 `work/t4_r2l_relabel.json`) 对照 PDF 文本层 `work/pdf_pages/` 与 KB 文件判新标签是否成立 (HOLDS / NOT_HOLD / UNVERIFIABLE); 文本层判不了的 (需要看渲染页) 如实标 UNVERIFIABLE 并说明, 不要猜.
C. **裁定来源**: (1) 上一轮四件事 (U-1 口径 / T4.2 方案及 6 条 / M-1..M-7 / 委托本身) 的记录是否足以作为 G-TB1 "用户 ack"、G-TB3 口径 "用户认可"、T4.2 hard 闸关闭的依据; (2) 第二轮三条原话是否足以支撑已执行的 78 条改标与登记的各项 (未决项 4); (3) attempt 2 判 "不足" 的 "人工判定来源可核性" 现在怎样. 每项判 足够 / 不足 / 需主人确认, 写理由.
D. **attempt 2 "仍开 / 部分关" 各项的现状** (已关 / 部分关 / 仍开 / 不适用), 逐条给依据: C3 逐表结案清单; census 汇总变化逐表说明; t0_mutation 在现 KB 的重证; pre_existing 58 条单独核; FIG 11 条逐条核; "规则 0 抽中" 各类; ATOM_ERR / PDF_TYPO 补抽; PLAN 修订 (FIG 12 → 11、T4.2 口径、G-TB3 口径); audit_matrix 缺行; 文档之间互相矛盾之处 (attempt 2 指出 `t4_user_decisions.md` 状态与 `t4_human_verdicts.md` 自相矛盾; 另请自己找有没有新的矛盾或过期数字: 现值 99.2651% / 95.5301% / PDF_TYPO 174 / 登记表 274 行 / 台账 md5 `16024ac0…`; 历史时点的数字带着时点说明的不算过期).
E. 上面 "没有经过独立审查的东西" 与 "未决项" 逐条的处置意见.

## 判定口径 (派发前写死, 不因结果改)
- 任一 G-TB 判 NOT_MET, 或任一样本 / 你自己挑的改标原子判 NOT_HOLD → 不 PASS.
- C 项任一 "不足", 或任一未决项你判 "挡闸" → 至多 CONDITIONAL, 写明还缺什么、由谁补 (主人 / 主控 / 独立审查).
- 你判 "需主人" 但不挡闸的事项单列, 供主控转给主人.
- PASS 的含义仅限 T4.1 总闸; push、打 tag、T4.3 都不在本次范围内.

## 输出 (中文, ≤ 200 行)
1. 总结论: **PASS / CONDITIONAL / FAIL** + 一段话理由.
2. G-TB 表 `闸 | 判定 | 依据 | 条件 / 缺口`.
3. 样本层: 交集核对结果 + 你自己挑的改标原子逐条表 + 计数.
4. C 项三问的判断.
5. D 项缺口现状表.
6. E: 未审项与未决项的处置表 (`项 | 挡闸? | 理由 | 由谁补`).
7. 你自己核过的数字 / 位置清单 (标 [自算 Grep] / [读日志] / [采信]), 以及你没能核的东西.
