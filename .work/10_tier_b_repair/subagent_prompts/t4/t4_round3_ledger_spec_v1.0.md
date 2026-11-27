# T4 问题 A 改台账 (R3L) — writer 规格 v1.0 (预备稿; **仅在主人直接回答 A1 之后才派发**)

<!-- chain: E (plans) -->
> 状态: 预备 (2026-11-27). 主人尚未回答问题 A; 本规格在他答 A1 之前**不执行**, 答 A2 或别的则作废 (保留不删).
> 用途: 把 4 条多标的 PDF_TYPO 改回 EXACT. 依据: 第三轮审查者 `evidence/t4_round3_raw/` (R3_PDF_TYPO 层 NOT_HOLD 4 条) 与总闸 attempt 3 审查者的独立复核 (`evidence/t4_gate_raw/attempt3_report.md` "样本里仍未处理的 NOT_HOLD" 表) — 两位独立审查者结论一致, 本批不再另设语义 auditor.
> writer = `oh-my-claudecode:executor` (opus); reviewer = `oh-my-claudecode:code-reviewer` (复跑逐行核; 规则 D). 主控不写台账.
> **KB 冻结**: `knowledge_base/` 一个字节都不许改 (`git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`). `archive/`、`releases/` 不碰. 不 git add / commit / push (主控提交).

## 0. 先读
`evidence/checkpoints/t4_round2_ledger_W.md` (上一批 R2L 的机制、命令序列 §0、小修一节) 与 `subagent_prompts/t4/t4_round2_ledger_spec_v1.0.md` §3 (守则). 本批沿用同一套机制与守则, 只是清单不同.

## 1. 要改的标签 (只这 4 条)
`work/t4/supp/relabel_pending.json` 里 `group` = `typo-overlabel` 的 4 条: `ig34_p0412_a006`、`ig34_p0412_a007`、`ig34_p0412_a008`、`ig34_p0413_a010`; 现标签 PDF_TYPO → EXACT.
- 这 4 条现在是怎么被判成 PDF_TYPO 的 (哪条规则、挂哪个登记 id), 先查清并写进 checkpoint; 改法要从**成因**下手 (例如把它们从该登记的命中范围里排除, 或加逐原子条目), 不要在 writeback 之后再覆盖标签.
- 改完后这 4 条必须由现有的 EXACT 判定路径得出 (KB 逐字承载; `t3_direct_hit.py` 对它们的独立命中检查要过), 不是凭清单硬写 EXACT. 若其中任何一条在现有机制下得不出 EXACT (例如指纹不命中) → 停下来写明, 不要绕过.
- 决定来源写 "owner <日期> 问题 A = A1 (`evidence/checkpoints/t4_owner_confirmation.md`)"; 证据指针指向该条的 `raw`.
- 登记表 `S-TDM TD T-1` / `T-4` 两行本身不删 (笔误是真的, 只是不在这 4 条原子里); 若登记行里有把这 4 条列为受影响原子的字段, 更正并用 `t4_r2l_fix` 式的字段记 before → after.
- **不许动**: `ig34_p0293_a038` (问题 B; 除非派发消息另有说明) 以及这 4 条之外任何原子的标签.

## 2. 守则与验收 (做不到任何一条就停下来写明)
- 改前备份工作台账到 `work/coverage_ledger.wc.pre_r3l.jsonl` (入库; 规则 B). 改前 md5 应为 `16024ac09721cb3f8519cd68fa455196`.
- 逐行 diff (按位置对齐, 断言 `pdf_atom_id` 相同): 标签变化的行**恰好**是这 4 条, 方向 PDF_TYPO → EXACT; 其它行若有变化只能是不改标签的字段, 逐类列出条数与原因. 清单存 `work/t4/r3l_ledger_diff.txt` (入库).
- 行数 12492 不变; 整套从源头跑两遍 md5 一致, 报出新 md5.
- 终态计数: PDF_TYPO 174 → **170**, EXACT 4706 → **4710**, 其余各类不变.
- `t4_coverage_decomp.py` 四个数等于 `work/t4/supp/scenarios.json` 最后一项 (预演): U-1 B 9860/9933 = 99.2651% (不变), strict 9493/9933 = 95.5703%, mapped 与内容指标见该文件. 不等 → 说明哪里不同, 不要调数字.
- `s0_classify.py` NEW 0 / BAD 0; `t3_direct_hit.py` GREEN (报出新的 TB / stock / pre_existing 数); `t3_recompute.py` 范围内 174 节残留 0、G-TB1 174/174、G-TB2 字面 157/174.
- `scripts/t4/t4_ack_lists.py` 重生成 `evidence/checkpoints/t4_ack_lists.md`: PDF_TYPO 170, "(未归因)" 0.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` = 42.
- `bash scripts/t3/t3_mutation.sh`: M0 / M2 / M7 GREEN, M1 / M3-M6 RED, 真 KB md5 前后一致 (靶子失效要写明, 不自行换靶).
- 结束时 `git status --short knowledge_base archive releases` 为空; `git rev-parse HEAD:knowledge_base` 不变.
- **不要跑** `scripts/t4/t0_mutation_head.sh`、`t4_gate_prerun.sh`、`t4_supp_report.py` (主控在 reviewer 通过后做), 不要跑 / import `t4_sample.py`、`t4_render.py`.

## 3. 交付
- checkpoint `evidence/checkpoints/t4_round3_ledger_W.md` (中文; 路径用反引号): 4 条的成因、改法与改的文件、§2 每条验收的命令与输出、逐行 diff 汇总、没做 / 撤回的项、已知局限.
- 失败或中途停: `evidence/failures/step_T4_R3L_attempt_1.md` (输入 / 产物 / 技术判定 / 业务判定 / 下一 attempt 输入).
- 回复正文: 新台账 md5、4 条是否全部落地、清单外有无变化、各验收项结果、checkpoint 路径.
