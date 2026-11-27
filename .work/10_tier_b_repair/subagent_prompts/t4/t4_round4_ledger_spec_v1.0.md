# T4 问题 C 改台账 (R4L) — writer 规格 v1.0 (预备稿; **仅在主人直接回答 C1 之后才派发**)

<!-- chain: E (plans) -->
> 状态: **生效** — 主人 2026-11-27 直接回答 「C1、D1、追认 M-10」 (原话与时间: `evidence/checkpoints/t4_owner_confirmation.md` 消息 5; 收到时间 2026-11-27T14:41:14Z). (写成预备稿时主人尚未回答; 规格正文在他回答之后没有改.) 问题 D = D1: `B-CE T-2` 那 8 条维持 ATOM_ERR, 本批不动.
> 用途: 把 1 条多标的 ATOM_ERR (`ig34_p0124_a001`) 改回 EXACT. 依据: 加查的两位互不知情的独立审查者结论一致 — `evidence/t4_atomerr_raw/pack_1.md` (E12, `oh-my-claudecode:tracer`) 与 `evidence/t4_atomerr_raw/second_look.md` (E12, `general-purpose`): 原子与 PDF p124 `ml.xpt` 第 2 行逐格一致 (没抽错), KB `knowledge_base/domains/ML/examples.md:42` 与 PDF 逐字一致. 汇总 `evidence/checkpoints/t4_atomerr_fullcheck.md` §3 / §4. 本批不另设语义 auditor (语义已由这两位独立判过); 改完后由总闸角色的新实例对这一处再判.
> writer = `oh-my-claudecode:executor` (opus); reviewer = `oh-my-claudecode:code-reviewer` (复跑逐行核; 规则 D). 主控不写台账.
> **KB 冻结**: `knowledge_base/` 一个字节都不许改 (`git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`). `archive/`、`releases/`、`web/` 不碰. 不 git add / commit / push (主控提交).

## 0. 先读
`evidence/checkpoints/t4_round3_ledger_W.md` (上一批 R3L 的机制、命令序列 §0、坑) 与 `subagent_prompts/t4/t4_round2_ledger_spec_v1.0.md` §3 (守则). 本批沿用同一套机制与守则, 只是清单与成因不同. `HANDOFF.md` 里 "坑" 一条必读 (`t3_build_keep.py` 不要重跑; `t3_writeback.py` 先写台账后断言, 断言失败要从备份还原; 整链顺序用 `work/scratch/t4/r3l/run_chain.sh`, 先跑 `scripts/t4/t4_r3l_build.py`).

## 1. 要改的标签 (只这 1 条)
`ig34_p0124_a001`: 现标签 ATOM_ERR (规则 `S1-R1`) → EXACT.
- 成因先查清并写进 checkpoint. 主控已知的线索 (自己核实, 不要照抄): 标签出自 `evidence/checkpoints/t2_B-ML_review.md:70` 的一句顺带话 → `work/t1_errata.json` 的 `t3_atom_err` → `scripts/t3/t3_errata_build.py` → `work/t3_errata.json#atom_err/ig34_p0124_a001` (`atom_in_pdf` = false: K4 的子串复核对每格折行的表格行测不出来) → `t3_writeback.py` 的 S1-R1 优先于逐字命中. 台账这一行自带 `hit_file` = `knowledge_base/domains/ML/examples.md`, `hit_lines` = [42], `prev_verdict` = EXACT.
- 改法要从**成因**下手 (把这一条从原子抽错登记里撤掉, 例如在 `t3_errata_build.py` 里加一个有出处的逐原子撤销, 数据与规则分开, 比照 R3L 的做法另存清单 `work/t4_r4l_relabel.json`), 不要在 writeback 之后再覆盖标签. `work/t1_errata.json` 按约定只读, 不改.
- 改完后这 1 条必须由现有的 EXACT 判定路径得出 (KB 逐字承载; `t3_direct_hit.py` 对它的独立命中检查要过), 不是凭清单硬写 EXACT. 在现有机制下得不出 EXACT → 停下来写明, 不要绕过.
- 撤销要带断言: 被撤的原子当前确实是 "只因这条 errata 才成为 ATOM_ERR" (撤销清单里的 id 不在 `atom_err` 里、或撤掉后没落到 EXACT → 报错), 防止清单过期后悄悄失效.
- 决定来源写 "owner <日期> 问题 C = C1 (`evidence/checkpoints/t4_owner_confirmation.md`)"; 证据指针指向两位审查者的结果文件.
- **不许动**: `B-CE T-2` 那 8 条 (问题 D; 派发消息另有说明除外)、`ig34_p0293_a038`, 以及这 1 条之外任何原子的标签.
- 同批顺带 (只补指针, 不改标签; 做不到就写明不做): 4 条 ATOM_ERR 行的登记指针 `evidence.registry` 现为空, 补上 — `ig34_p0161_a0012` → `B-DS T-4`; `ig34_p0337_a003` → `B-RS T-3`; `ig34_p0339_a001` → `B-RS T-6`; `ig34_p0361_a016` → `B-FA T-2` (依据 `evidence/checkpoints/t4_atomerr_fullcheck.md` §5b; 机制比照 R2L 的 "5 条原子补登记指针"). 若补指针会让这 4 条的标签或允许集发生变化 → 不补, 写明原因.

## 2. 守则与验收 (做不到任何一条就停下来写明)
- 改前备份工作台账到 `work/coverage_ledger.wc.pre_r4l.jsonl` (入库; 规则 B). 改前 md5 应为 `438098704becc84eda01a925b80defaa`.
- 改任何输入之前先跑一遍整链, 确认台账仍为 `43809870…` (基线可复现).
- 逐行 diff (按位置对齐, 断言 `pdf_atom_id` 相同): 标签变化的行**恰好**是这 1 条, 方向 ATOM_ERR → EXACT; 其它行若有变化只能是不改标签的字段 (预期只有上面 4 条的登记指针), 逐类列出条数与原因. 清单存 `work/t4/r4l_ledger_diff.txt` (入库).
- 行数 12492 不变; 整套从源头跑两遍 md5 一致, 报出新 md5.
- 终态计数: ATOM_ERR 197 → **196**, EXACT 4710 → **4711**, 其余各类不变 (PDF_TYPO 170 / EQUIVALENT 3949 / IE 2559 / FIG 11).
- `t4_coverage_decomp.py` 四个数等于预演 (`python3 -I .work/10_tier_b_repair/scripts/t4/t4_atomerr_coverage.py` 输出的 `C1` 行, 须在改台账**之前**跑一次留底): U-1 B 9860/9933 = 99.2651% (不变), strict 9494/9933 = 95.5804%, mapped 9494/9556 = 99.3512%, 内容 8660/9556 = 90.6237%. 不等 → 说明哪里不同, 不要调数字.
- `s0_classify.py` NEW 0 / BAD 0; `t3_direct_hit.py` GREEN (报出新的 TB / stock / pre_existing 数); `t3_recompute.py` 范围内 174 节残留 0、G-TB1 174/174、G-TB2 字面 157/174.
- `scripts/t4/t4_ack_lists.py` 重生成 `evidence/checkpoints/t4_ack_lists.md`: ATOM_ERR 196, "(未归因)" 0.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` = 42.
- `bash scripts/t3/t3_mutation.sh`: M0 / M2 / M7 GREEN, M1 / M3-M6 RED, 真 KB md5 前后一致 (靶子失效要写明, 不自行换靶).
- 对新加的撤销断言做变异 (至少: 清单里放一个不在 `atom_err` 的 id → 报错; 放一个撤掉后得不出 EXACT 的 id → 报错), 变异后从备份还原并再跑一遍整链确认 md5.
- 结束时 `git status --short knowledge_base archive releases web` 为空; `git rev-parse HEAD:knowledge_base` 不变.
- **不要跑** `scripts/t4/t0_mutation_head.sh`、`t4_gate_prerun.sh`、`t4_supp_report.py` (主控在 reviewer 通过后做), 不要跑 / import `t4_sample.py`、`t4_render.py`; 不要重跑 `t4_atomerr_sample.py` (它断言旧台账 md5; 改台账后按设计会失败).

## 3. 交付
- checkpoint `evidence/checkpoints/t4_round4_ledger_W.md` (中文; 路径用反引号; **不写本机绝对路径**, 一律写相对仓库根的路径): 成因、改法与改的文件、§2 每条验收的命令与输出、逐行 diff 汇总、没做 / 撤回的项、已知局限. 不给自己判 PASS.
- 失败或中途停: `evidence/failures/step_T4_R4L_attempt_1.md` (输入 / 产物 / 技术判定 / 业务判定 / 下一 attempt 输入).
- 回复正文: 新台账 md5、这 1 条是否落地、清单外有无变化、各验收项结果、checkpoint 路径.
