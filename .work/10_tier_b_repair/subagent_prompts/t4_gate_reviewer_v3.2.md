# T4.1 总闸 — 加查与 R4L 之后的 delta 闸审 brief v3.2 (feature-dev:code-reviewer, 新实例)
<!-- chain: E (plans) -->
> v1.0 / v2.0 / v3.0 / v3.1 保留不改 (规则 B). 本次范围**只限 "attempt 3 delta = PASS" 之后发生的变化**, 不重做已判的部分. 只读: 不改任何文件, 不 commit; 结果以回复正文返回, 主控原样存入 `evidence/t4_gate_raw/attempt3_delta2_report.md` 并誊入 `evidence/checkpoints/t4_gate_review.md`. 主控不改判 (规则 D).
> 本文只给事实与要判的问题, 不给预期结论. 你判断不足就如实写, 这本身是交付物.

## 背景 (只给事实)
- 仓库根即工作目录; 项目目录 `.work/10_tier_b_repair/` (下文路径省略此前缀). 标签定义、PDF 路径、文本层见 `subagent_prompts/t4_gate_reviewer_v1.0.md` "背景" 节; 闸定义 `PLAN.md` §5.1 及 "口径注".
- 先完整读两份原文: `evidence/t4_gate_raw/attempt3_report.md` (attempt 3 = CONDITIONAL; 其 D 项把 "ATOM_ERR / PDF_TYPO 补抽" 判为**部分关**: ATOM_ERR 的 S1-R1 类 157 条里约 83 条没被单独看过) 与 `evidence/t4_gate_raw/attempt3_delta_report.md` (delta = **PASS**; 把 "M-10 追认" 和 "约 83 条是否加一轮" 列为需主人但不挡闸).
- 那次 PASS 之后发生的事 (全部本地提交, 未 push; `knowledge_base/` 仍未改, `git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`):
  1. **加查** (主人选了 "加查", 经协调方转述): 汇总 `evidence/checkpoints/t4_atomerr_fullcheck.md` (主控写的, **没有送独立审查**). 筛法 `scripts/t4/t4_atomerr_sample.py`: S1-R1 157 条 = 此前已逐条判过 80 + 从未逐条判过 77; 全检 83 条 (77 + 6 盲复检). 口径 `subagent_prompts/t4/t4_atomerr_s1r1_v1.0.md` 在派发前提交 (`bf303d8`; `trace.jsonl` 的 `T4.AE` 行). 审查者 `oh-my-claudecode:tracer` ×4, 原始结果 `evidence/t4_atomerr_raw/pack_{1..4}.md`: HOLDS 82 / NOT_HOLD 1 / UNVERIFIABLE 0. NOT_HOLD = `ig34_p0124_a001` (标 ATOM_ERR; 审查者判原子没抽错、KB 逐字承载). 另一类型审查者 (`general-purpose`) 盲复看 5 条 `evidence/t4_atomerr_raw/second_look.md`. 按写死条款该轮记 "不通过", 归档 `evidence/failures/step_T4.AE_attempt_1.md`.
  2. **取决于口径的 8 条**: 登记 `B-CE T-2` 那组 (加查包里的 E18-E25) 原子与 PDF 只差 USUBJID 里的一个空格; 两位审查者判 HOLDS, 包 2 审查者写明 "若代码值内部的空格算空白归一则 ① 不成立". 主控列为问题 D, 没有裁 (汇总 §5a).
  3. **主人直接回答** (`evidence/checkpoints/t4_owner_confirmation.md` "消息 5", 逐字): 「C1、D1、追认 M-10」. 提问原文见同文件 "主控的第六次提问" / "第七次提问". 登记: `evidence/checkpoints/t4_user_decisions.md` §000c (问题 C / D / M-10 三行) 与 §000b (M-10). D1 的口径写在 §000c 问题 D 那一行, 并补进加查 brief 文末 "v1.0 之后的口径补注".
  4. **改台账 R4L** (提交 `65d6a0f`): `ig34_p0124_a001` ATOM_ERR → EXACT; 同批给 4 条 ATOM_ERR 行补登记指针 (只改 `evidence.registry`). 规格 `subagent_prompts/t4/t4_round4_ledger_spec_v1.0.md` (主人回答之前写成预备稿并提交, 回答之后只改了状态行); writer (`oh-my-claudecode:executor`) `evidence/checkpoints/t4_round4_ledger_W.md`; reviewer (`oh-my-claudecode:code-reviewer`) 报告原文 + 小修后的 delta 复审原文 + 主控的处理: `evidence/checkpoints/t4_round4_ledger_review.md`. 清单 `work/t4_r4l_relabel.json`; 改前备份 `work/coverage_ledger.wc.pre_r4l.jsonl`; 逐行 diff `work/t4/r4l_ledger_diff.txt`. **本批没有另设语义 auditor** (主控的理由: 这 1 条的语义已由加查的两位互不知情的审查者判过, 并交你这一轮再判).
  5. R4L 之后主控做的 (都**没有经过独立审查**): `scripts/t4/t4_supp_report.py` / `t4_r2l_sample_overlap.py` / `t4_gate_prerun.sh` / `t4_atomerr_report.py` / `t4_atomerr_coverage.py` 并入 R4L (前者改为以 `coverage_ledger.wc.pre_r4l.jsonl` 为 "R3L 之后的台账", 并断言工作台账 = 它 + R4L 清单); T0 变异基线第三次重建并重跑 (`evidence/checkpoints/t4_t0_refresh.md` §8); `PLAN.md` v1.4.4、`HANDOFF.md` (最后一节 = 现状)、`_progress.json`、`audit_matrix.md`、`t4_atomerr_fullcheck.md` §8 更新; 推送前检查脚本与预跑 `evidence/checkpoints/t4_prepush_check.md`.
- 主人对发版的同意 (经协调方待办项转达, 不是在主控聊天里直接发的; 记录在 `t4_owner_confirmation.md` "主人对发版的同意"): 「直接发版，不用再问我」, 范围 = "这 1 条改完并复审通过" 这条路. **发不发版不由你判**; 你判的是 T4.1 总闸的当前结论, 以及有没有应在 push 之前处理的事项.
- **你没有 Bash.** 复跑输出已由主控在最新提交上串行跑好, 原样在 `work/t4/gate_prerun.log` (日志头有 HEAD、KB 树、台账 md5). 数字请尽量用 Grep / Read 自己核 (台账 `work/coverage_ledger.wc.jsonl` 很大, 不要整份读, 按 `"pdf_atom_id": "…"` 或 `"verdict": "…"` 定位 / 计数), 核不了的标 "[读日志]" 或 "[采信]".

## 你要判的
A. **`ig34_p0124_a001` 这一条**: (1) 主人的回答 (消息 5) 是否足以作为改标依据 — 读原文与提问自己判; (2) 台账里这一行现在的 `verdict`、判定规则、命中位置; 对照 PDF 文本层 `work/pdf_pages/ig34_p0124.txt` (表格每格折行, 注意按列对齐读) 与 `knowledge_base/domains/ML/examples.md` 第 38-43 行自己重判 "原子没抽错、KB 逐字承载、EXACT 成立" (HOLDS / NOT_HOLD / UNVERIFIABLE; 原子原文在 `work/pdf_atoms.jsonl` 按 atom_id Grep); (3) 读 `scripts/t3/t3_errata_build.py` 与 `scripts/t3/t3_writeback.py` 里 R4L 相关的代码段, 判断 "由现有判定路径得出、不是事后覆盖标签" 是否属实.
B. **R4L 有没有带来别的变化**: 用日志 "R2L + R3L + R4L change set" 一段与 `work/t4/r4l_ledger_diff.txt` 核 "标签变化恰好 1 条、另 4 行只改登记指针、其余行逐字节相同"; 自己用 Grep 抽核计数 (现值见下面 G); 4 条补的登记指针 (`ig34_p0161_a0012` → `B-DS T-4`; `ig34_p0337_a003` → `B-RS T-3`; `ig34_p0339_a001` → `B-RS T-6 (RS 副本)`; `ig34_p0361_a016` → `B-FA T-2`) 在登记表 `work/t2_pdf_typo_registry.jsonl` 里是否存在且对得上; R4L 的 writer / reviewer 是否不同 subagent_type (`trace.jsonl` 的 `T4.R4L.*` 行); reviewer 留下的 LOW 与主控的处理是否合理.
C. **G-TB1 ~ G-TB9 有没有哪条因加查 / R4L 变坏**: 对照前两份报告的 G-TB 判断, 只写有变化的闸与新依据 (日志里的 G-TB1 / 2 残留、G-TB3 四个数、direct_hit、census、t3 / t0 变异、反向溯源、live docs); 没变化的写 "沿用". G-TB8 (每批三个不同角色): R4L 这一批的情况请单独写明.
D. **"ATOM_ERR / PDF_TYPO 补抽" 那一项 (attempt 3 判 "部分关") 现在是什么状态** — 这是主控明确不自己判、留给你的:
   - 核加查的做法: 筛法与 157 = 74 + 6 + 77 的对账 (`work/t4/atomerr/atomerr_population.json`; 日志里 `t4_atomerr_report.py` / `t4_atomerr_coverage.py` 的输出); 口径是否确实在派发之前提交; 审查者类型是否独立; 盲复检 6 条与原判是否一致; 汇总里 "ATOM_ERR 197 / PDF_TYPO 170 每条都有逐条判定行" 的说法 (那是改台账之前的计数; 现在 ATOM_ERR 196).
   - **自己抽核**: 从 83 条里自选不少于 8 条 (须包含 `B-CE T-2` 那组里的 2 条、"涉登记" 的另 4 条里的 1 条、表格行与非表格行各若干), 用文本层与 KB 重判两半 (原子 ≠ PDF; KB = PDF), 列表给出你的判定与依据; 与审查者的判定不一致的单列.
   - 给出这一项的现状态: **已关 / 部分关 (写明还缺什么) / 仍开**.
E. **问题 D 的处理是否足够**: 主人答 D1; 口径登记在 `t4_user_decisions.md` §000c 问题 D 行与加查 brief 文末补注. 判: 这条口径与标签定义、与登记 `B-CE T-2`、与两位审查者当时的判定是否自洽; 登记的位置与写法够不够让以后的审查者照此执行; 8 条维持 ATOM_ERR 有没有留下矛盾.
F. **M-10**: 主人的追认 (消息 5) 是否足以关掉 delta 报告里 G-TB8 的那个字面条件.
G. **文档一致性**: 这次更新有没有引入矛盾或过期数字. 现值: U-1 B 9860/9933 = 99.2651% / strict 9494/9933 = 95.5804% / mapped 9494/9556 = 99.3512% / 内容 8660/9556 = 90.6237% / EXACT 4711 / EQUIVALENT 3949 / IE 2559 / PDF_TYPO 170 / ATOM_ERR 196 / FIG 11 / 登记表 274 行 / 台账 md5 `eef9bb14e5afab7e68a231ddd18cfa1c`. 带时点说明的历史数字不算过期. 重点看 `PLAN.md` 状态行与口径注、`HANDOFF.md` 最后一节、`_progress.json`、`audit_matrix.md` 末几行、`t4_atomerr_fullcheck.md`、`t4_ack_lists.md` 头部、`docs/PROGRESS.md` 第 22 行附近.
H. **没有经过独立审查的东西** (逐条给处置: 挡闸 / 不挡闸记已知局限 / 需谁补): 主控写的加查汇总; R4L 之后的 T0 基线重建; 主控改的 5 份脚本与重生成的两份汇总; 推送前检查的口径 (不含用户名的机器路径由协调方裁定放行, 见 `t4_prepush_check.md`); R4L 没有单独的语义 auditor; 加查审查者没看的东西 (各 `pack_N.md` 文件头自述).
I. 前两份报告已判 "不挡闸, 记已知局限" 的各项 (抽样而非全检的几类、约 80 条标签级别项、KB 观察项 O68-O71、trace 整点时间戳、记录形式的局限) — 现状未变; 你若不同意其中任何一项, 请指出.

## 判定口径 (派发前写死, 不因结果改)
- 本次给出的是 **T4.1 总闸的当前结论** (attempt 3 + delta + 本次合并看):
  - **PASS**: A 的三问都成立; R4L 没有带来清单外的变化; 没有哪条 G-TB 变成 NOT_MET; 你自己重判的 `ig34_p0124_a001` 与抽核的各条里没有 "应改而未改" 的 NOT_HOLD (与审查者不一致的条目须逐条说明是否挡闸); D 项不是 "仍开"; 且你没有发现新的挡闸项.
  - **CONDITIONAL**: 上面任何一条不满足但可补, 或某个未决项你判 "挡闸" — 写明还缺什么、由谁补 (主人 / 主控 / 独立审查).
  - **FAIL**: 证据与声称不符 (例如台账实际变化与声称的不一致、标签是事后覆盖的、KB 被改过、口径是事后补的).
- "需主人但不挡闸" 的事项单列. 发现的过期文字 / 小矛盾按 LOW 列出 (不挡闸, 主控改).
- 另写一行: **有没有应在 push 之前处理的事项** (有 → 列出; 没有 → 写 "无").
- PASS 的含义仅限 T4.1 总闸.

## 输出 (中文, ≤ 140 行)
1. 总结论 **PASS / CONDITIONAL / FAIL** + 一段话理由; "push 之前须处理的事项" 一行.
2. A 项三问的结果 (含这条原子的 PDF 行与 KB 行依据).
3. B 项核对结果.
4. C 项: 有变化的闸表.
5. D 项: 做法核对 + 你抽核的表 (`编号 | atom_id | 审查者判定 | 你的判定 | 依据`) + 这一项的现状态.
6. E / F 项结论.
7. G 项: 过期 / 矛盾清单.
8. H / I 项处置表 (`项 | 挡闸? | 理由 | 由谁补`).
9. 你自己核过的数字 / 位置清单 (标 [自算 Grep] / [读日志] / [采信]), 以及没能核的东西.
