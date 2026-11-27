# T4 第二轮改台账 (R2L) — writer 规格 v1.0

<!-- chain: E (plans) -->
> 用途: 把仓库主人 2026-11-27 在主控聊天里直接定的标签改动落到工作台账. 主人原话与逐项登记: `evidence/checkpoints/t4_owner_confirmation.md` 第二轮一节; 提问页: `evidence/checkpoints/t4_owner_decisions_round2.md`.
> writer = `oh-my-claudecode:executor` (opus). 之后由 `oh-my-claudecode:code-reviewer` 复跑逐行核、`oh-my-claudecode:verifier` 审计 (规则 D). 主控不写台账.
> **KB 冻结**: `knowledge_base/` 一个字节都不许改 (`git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`; 下游 sdtm-rag 正在这棵树上预演). `archive/`、`releases/` 不碰. 不 git add / commit / push (主控提交).

## 0. 先读
1. `evidence/checkpoints/t4_thaw_W3.md` 的 "C. attempt 1 续" 一节 (C1-C7): 上一次改台账用的机制 — `scripts/t3/s0_classify.py` 逐原子条目、`scripts/t3/t3_errata_build.py` 的 `T4_U7_REG` 表、`work/t3_k3b_out_of_scope_keep.json` (范围外, U-8)、`scripts/t3/t3_writeback.py`、以及 `evidence/checkpoints/t3_recompute.md` §A4.5 的整套复跑命令序列.
2. `evidence/checkpoints/t4_relabel_pending.md` 与机读清单 `work/t4/supp/relabel_pending.json` (82 条; 每条有 `atom_id` / `now` / `to` / `group` / `raw` (独立审查者原始结果的文件:行) / PDF_TYPO 的带 `registry`).
3. `evidence/checkpoints/t4_supp_fullcheck.md` §4 / §4b / §6 (背景与要补的登记项).

## 1. 要改的标签 (只这 78 条; 清单以 `relabel_pending.json` 为准)

| group | 条数 | 现标签 → 新标签 | 主人的决定 |
|---|--:|---|---|
| `R1-row` | 51 | EQUIVALENT 49 / EXACT 2 → INTENTIONAL_EXCLUDE | 问题 1 = A |
| `v2.0-TOC` | 2 | EQUIVALENT → INTENTIONAL_EXCLUDE | 问题 2 = A |
| `registered-typo` | 19 | EXACT 9 / EQUIVALENT 10 → PDF_TYPO (登记 id 见 `registry` 字段) | 问题 3 = A |
| `registered-typo-oos` | 6 | EXACT 1 / EQUIVALENT 5 → PDF_TYPO (范围外; 登记 id 见 `registry`) | 问题 7b = A |

**不许动**: `typo-overlabel` 组的 4 条 (`ig34_p0412_a006` / `a007` / `a008`、`ig34_p0413_a010`) — 主人还没答, 维持 PDF_TYPO; `ig34_p0293_a038` 维持 PDF_TYPO; 以及清单之外的任何原子的标签.

写法要求:
- IE 的 53 条: `verdict` = `INTENTIONAL_EXCLUDE`, `category` = `VERSION_MISMATCH`; `exclusion_reason` 与 `approved_by` 的格式比照台账里现有的 Tier B T1 IE 行 (例如 `sv20_p0064_a017`), 但写明这次的来源: R1-row 组用 "Tier B T4 round-2 IE (VERSION_MISMATCH; R1-row: KB 精简列一致, PDF 其它列未收)", v2.0-TOC 组用 "Tier B T4 round-2 IE (VERSION_MISMATCH; v2.0 目录条目, 对应章节 KB 未收)"; `approved_by` = "owner 2026-11-27: evidence/checkpoints/t4_owner_confirmation.md 第二轮 (问题 1 = A)" / "(问题 2 = A)"; 每条的证据指针指向它的 `raw`.
- PDF_TYPO 的 25 条: 走与解冻轮相同的 R2 / registry 机制 (范围内 19 条比照 `T4_U7_REG`; 范围外 6 条比照 U-8 的 keep 机制), 每条绑定 `registry` 字段给的那个登记 id, 运行时断言该 id 在 `work/t2_pdf_typo_registry.jsonl` 里存在; 决定来源写 "owner 2026-11-27 问题 3 = A" / "问题 7b = A"; 证据指针指向 `raw`.
- 具体放进哪个数据文件 / 哪张表由你按现有机制定, 但必须: ① 数据与规则分开 (清单进数据文件, 不要在脚本里硬编码 78 个 id — 脚本读 `work/t4/supp/relabel_pending.json` 或你生成的派生数据文件均可); ② 整套复跑 (§A4.5 序列) 从源头跑两遍, 台账 md5 一致; ③ 不依赖上一轮产物.

## 2. 同批要做的登记更正 (都只动 `work/` 下的数据文件与脚本, 不动 KB)
1. `work/t2_pdf_typo_registry.jsonl` 页号: `B-IS T-6` `pdf_page` 241 → 239 (依据 `work/pdf_pages/ig34_p0239.txt:35/39/43`); `B-CP T-5` 211 → 212 (依据 `evidence/t4_round2_raw/pack_sib2_1.md` 附注; 自己再对 `work/pdf_pages/ig34_p0212.txt` 核一次).
2. 登记表补两条 "PDF 自身不一致" (主人问题 9 = A; `handling` = `照录`, 不改 KB): ① SDTM v2.0 p69 (§6.6) SREL 行 Notes 写 "…the subject or pool identified in RDEVID" vs p50 同句写 "…the device identified in RDEVID" — KB 只收了 p50 那句 (`knowledge_base/model/04_associated_persons.md` AP 表 SREL 行), p69 那句 KB 未收 (§6.6 表只有精简列); ② SDTMIG p440 图中 SPC-003 标 "(Brain)" vs 同页表格 "TISSUE" — KB 两处照录 (`knowledge_base/domains/RELSPEC/examples.md`). 字段比照登记表里现有的 `照录` 行; id 自拟 (例如 `T4R2 sv20 N-1`、`T4R2 RELSPEC N-1`), `t4_decision` 写 "owner 2026-11-27 问题 9 = A (补登记)".
3. 登记文字 / 指针 (审查者指出的不准之处; **只在不改变任何原子标签的前提下做**, 见 §3 的守则): `B-CP T-3` 的 `pdf_value` (实际问题是 "(e.g.," 未闭合, 不是多一个括号; 依据 `evidence/t4_round3_raw/pack_8.md`); `S-SPC1 CP T-16a` 补记第二处未闭合引号 `"CD278+`; `S-SPC2 N-1` / `N-2`、`B-NV N-1` / `N-2` 的 `basis` 里 "照录" 字样与 `handling` = "KB 写正确值" 矛盾 → 改 `basis` 文字; `B-SUPPQUAL T-1` 的位置清单补 `chapters/ch08_relationships.md:228`. 决策表登记指针: `ig34_p0355_a027` 与 p356 第 27 行那条原子补 `B-TR T-1`; `pack_8.md` 指出的 3 条漏列第二个登记 id (T178 / T183 / T200 对应的原子). 这一项里任何一条做了会导致别的原子标签变化的, **撤回那一条并在报告里写明**, 不要为了它改规则.
4. `scripts/t4/t4_ack_lists.py`: 新进入 PDF_TYPO 的 25 条 "决定来源" 标为 "主人 2026-11-27 第二轮 问题 3 = A" / "问题 7b = A" (指向 `t4_owner_confirmation.md`), 然后重生成 `evidence/checkpoints/t4_ack_lists.md`; 断言无 "(未归因)".

## 3. 守则与验收 (做不到任何一条就停下来写明, 不要绕过)
- **改动集守则**: 改前先备份 `work/coverage_ledger.wc.jsonl` (到 `work/coverage_ledger.wc.pre_r2l.jsonl`, 入库; 规则 B). 改后逐行 diff (按 `pdf_atom_id`): 标签变化的行必须**恰好**是 §1 的 78 条, 方向与清单一致; 其它行若有变化, 只能是 "规则名 / 证据指针 / checkpoint 行号" 之类不改标签的字段, 并逐类列出条数与原因. 出现清单外的标签变化 → 查明是 §2 哪一条登记更正引起的, 撤回那条更正; 仍消不掉 → 停.
- 台账行数不变 (12492); 重复 id 的 11 个不受影响.
- 整套从源头跑两遍, 台账 md5 一致, 报出新 md5.
- `s0_classify.py`: NEW 0 / BAD 0. `t3_direct_hit.py`: GREEN (注意: 2 条 EXACT → IE 与 10 条 EXACT → PDF_TYPO 会改变它统计的 EXACT 数, 报出新数).
- `t3_recompute.py`: §5.0 范围 174 节 residual_gap 0, G-TB1 174/174, G-TB2 字面 157/174 (应不变; 变了要解释).
- `scripts/t4/t4_coverage_decomp.py` 的四个数必须等于主控在台账副本上预演的值 (`work/t4/supp/scenarios.json` 里 "三组都改 + 范围外已登记笔误同类 6 条" 那一项): U-1 B 9860/9933 = 99.2651%, strict 9489/9933 = 95.5301%, mapped 与内容指标见该文件. 不等 → 说明哪里不同, 不要调数字.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` = 42.
- `bash scripts/t3/t3_mutation.sh`: M0 / M2 / M7 GREEN, M1 / M3-M6 RED, 真 KB md5 前后一致 (若某个变异靶子因这次改标失效, 写明, 不要自行换靶).
- 结束时: `git status --short knowledge_base archive releases` 为空; `git rev-parse HEAD:knowledge_base` 不变; 工作树里 KB 无未提交改动.
- **不要跑** `scripts/t4/t0_mutation_head.sh` (改台账后它的基线要重建, 由主控在 reviewer 通过后做), 不要跑 / import `scripts/t4/t4_sample.py`、`t4_render.py`, 不要重跑 `t4_supp_report.py` 等会重写证据文件的脚本.

## 4. 交付
- checkpoint `evidence/checkpoints/t4_round2_ledger_W.md` (中文; 路径用反引号, 不写 Markdown 链接): 做了什么 (按 §1 / §2 分项, 每项用了哪个机制、改了哪些文件)、§3 每条验收的命令与输出、逐行 diff 的汇总表 (标签变化 78 条按 group 计数; 非标签字段变化按类计数)、撤回 / 没做的项与原因、已知局限. 逐行 diff 清单存 `work/t4/r2l_ledger_diff.txt` (入库).
- 失败或中途停: 写 `evidence/failures/step_T4_R2L_attempt_1.md` (输入 / 产物 / 技术判定 / 业务判定 / 下一 attempt 输入), 已有的失败数据不删.
- 回复正文: 新台账 md5、78 条是否全部按清单落地、清单外有无变化、§2 各项做了哪些 / 撤回哪些、各验收项结果、checkpoint 路径.
