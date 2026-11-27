# 10_tier_b_repair — 主控 handoff (压缩/换 session 时先读)
> 更新: 2026-11-27 下午 (接手主控: attempt 2 缺口补做后; **最新状态看文末 "T4 接手主控" 一节**, 上面各节是历史). 本文件只记"在途状态 + 主控规程", 规则本体见 PLAN.md / subagent_prompts/t2_dispatch_notes.md / evidence/checkpoints/t1_user_ack.md (R1-R4, D1-D7).

## 每批流程 (主控只派发/裁定/提交, 不写 KB)
writer (oh-my-claudecode:executor, opus) → reviewer (oh-my-claudecode:code-reviewer) → auditor (oh-my-claudecode:verifier).
writer 在 reviewer PASS 后再改 → 回 reviewer 复审 delta 才派 auditor. auditor PASS → 主控 `git add` 本批 kb_files + 证据 + audit_matrix/trace/errata → 本地 commit (不 push; T4 后统一 push).
派发 prompt 模板: 见已提交的 t2_B-*.md 同类; writer 必读 t2_writer_v1.0.md + t2_dispatch_notes.md + batch json + t1_user_ack.md.
范围外发现 → work/out_of_scope_findings.md (O1-O25); 原子抽错 → work/t1_errata.json `t3_atom_err`; target 迁移 → `t3_target_remap`; T4 用户裁定项散落各 checkpoint, T4 前汇总 (O25).
check_links live docs 基线 42 (汇总行走 stderr: `2>&1 | grep "live docs"`); evidence 里 md 链接写法须反引号.

## 状态 (2026-11-26 晚): **T3 完成; T2S 全部完成 — 22/22 扫描批本地 commit (未 push)**
- 已提交 (writer→reviewer→auditor 全 PASS): S-EVT S-INT S-FND S-SPC1 S-SPC2 S-HOST S-TDM S-TUFA S-SPREL S-CH1 S-CH4 S-CH8 S-CH10 S-MOD1 S-MOD2 S-MOD3 S-SPEC1..4 S-CT (U5/U6 脚本批) S-TYPO (U1 排版脚本批)。
- 扫描批口径: brief `subagent_prompts/t2s_scan_writer_v1.0.md` / `t2s_scan_review_audit_v1.0.md`; 批中主控裁定在 `subagent_prompts/t2_dispatch_notes.md` 末尾; 用户/主控规则 U1-U8 在 `evidence/checkpoints/t2_post_user_ack.md`。
- 覆盖矩阵 (`scripts/t2s/t2_coverage_matrix.py`): 全部 domains/chapters/model 文件 FINAL; 残留 fn 缺口 3 个均假阳 (DI 无 spec 表 / ML O61 / SE O58)。
- 脚本 (已提交): `scripts/t2s/` — spec 比对 sc2/sc2w/speccmp2, CT ct_extract/ct_apply/ct_assert, 排版 typo_plan/typo_assert(--plan)/typo_mutate, reviewer 独立校验 review_S-TYPO/。
- T4 底稿: `work/t2_pdf_typo_registry.jsonl` (270 条 PDF_TYPO/T-n) + `evidence/checkpoints/t4_user_decisions.md` (O25 用户裁定汇总, 含 S-TYPO 追加项: CRF ○□ 口径、MH `History“`、残余 230 行)。
## T3 完成 (2026-11-26): attempt 4 PASS (attempt 1-3 FAIL 归档 `evidence/failures/step_T3_attempt_*.md`)
- 结果摘要: `evidence/checkpoints/t3_recompute.md` §0 顶部 (最终有效 = attempt 4); 审计 `evidence/step_T3_audit.md`; 复跑入口 §A4.5.
- 终态 EXACT 1016 / EQUIV 54 / IE 494 / ATOM_ERR 197 / PDF_TYPO 122 / FIG 11; 残留 1 (`ig34_p0056_a006` pending_user). G-TB2 170/174, G-TB3 99.3578%, live docs 42.
- 之后跑 fp_match 必加 `--sections work/section_coverage.wc.baseline.jsonl`.
## (历史) T4 attempt 1 阶段 (2026-11-27): T4.1 attempt 1 = **不通过 (CONDITIONAL)**; T4.2 样本已备; **全部等用户裁定**
- KB 冻结中 (sdtm-rag 用 00a2e93 内容做入库预演): 本阶段 **不改 `knowledge_base/`**, 不 push, 不打 kb tag, 不做 T4.3.
- 总闸: `evidence/checkpoints/t4_gate_review.md` (主控誊录 + 计数); 审查原文 `evidence/t4_gate_raw/{pack1..4,evidence_layer}.md`; brief `subagent_prompts/t4_gate_reviewer_v1.0.md`.
  - 样本 84/84 HOLDS (正式 72 + 补充 SUPP 12; seed 20261127). 证据层: G-TB1/2 NOT_MET (残留 p0056_a006 + 三类无 ack)、G-TB3 字面 NOT_MET (strict 96.0741%) / mapped 99.3578% 过但无用户认可.
- 用户待裁 (唯一入口): `evidence/checkpoints/t4_user_decisions.md` **§00 U-1~U-11** (口径/残留/父节/C 层/三类 ack/人工抽样/A-B 表/范围外 4/S-TYPO/KB 观察项/Mermaid); 三类逐条 `evidence/checkpoints/t4_ack_lists.md`; 人工抽样 `evidence/checkpoints/t4_human_sample.md` (42 条, 判定栏空).
- 复跑: `python3 -I $T/scripts/t4/t4_sample.py && python3 -I $T/scripts/t4/t4_render.py` (注意: render 会整体重写 t4_human_sample.md, 有用户判定后不要再跑或先誊出); `t4_ack_lists.py`; `t4_coverage_decomp.py`. HEAD 复跑结果 (live docs 42 / t3_mutation 同 T3 / census OK311 DIFF37 diffs144) 见 gate_review §3.
- 用户裁定回来后: ① 按 U-2/U-8 改 ledger (走 writer→reviewer, 主控不写); ② KB 解冻后按 U-7/U-9/U-10 改 KB (正常批流程); ③ 证据层审查者建议的补强 (pre_existing 58 条单独核、C7 38 条 ATOM_ERR 全检、FIG 11 条、C3 表结案清单、文档状态行过期) 视用户 U-5 选择做; ④ T4.1 attempt 2 (同角色 feature-dev:code-reviewer, 新实例) → T4.3 (Chain D + RETROSPECTIVE + push + kb tag + 提醒 sdtm-rag).
- 风险提示: 下一个会话若重跑 `t4_render.py` 会覆盖用户在 t4_human_sample.md 的勾选.
## T4 现状 (2026-11-27 晚, 新 session 主控): **T4.1 attempt 2 = 不通过 (CONDITIONAL)**; KB 已解冻改完一次 (本地, 未 push)
- 裁定 = 协调 bot「sdtm开发」委托代裁 (非主人逐条), `evidence/checkpoints/t4_user_decisions.md` §000; 主控实施决定 M-1..M-7 单列 §000b (不在委托内, 待追认).
- 提交: `3a24a1c` 解冻前只读核查 (U-5 38/38、U-6 预筛 42/42、U-7 复核 21 B / 5 回 A / B 组 15 维持, Mermaid 42/42); `a59c2d3` 解冻轮 (KB 25 文件 +118/−179; W1/W2/W3 executor → reviewer ×2 code-reviewer → auditor verifier 全 PASS; 证据 `t4_thaw_*.md`); `d3f2ea9` 下游说明 + 状态行; 其后 attempt 2 誊录提交.
- 终值: ledger md5 `60729f7b64b7c1dfaf2174e394f6dd9c`; 残留 0; G-TB2 174/174 [严格 157]; G-TB3 strict 95.8041 / mapped 99.3561 / U-1 B 99.2690 / 内容 90.6948; live docs 42; t3_mutation M0/2/7 绿 M1/3-6 红; t0_mutation MISMATCH (既有, T0 baseline 过期).
- T4.2: 主人 (经协调方转达) 改口径为 "AI 预筛 42 + 主人抽查 6", 判 6/6 → `t4_human_verdicts.md`; 6 条解冻后未变. **勿重跑 `t4_render.py`** (包头已加指针; 模板 `scripts/t4/t4_human_header.md` 同步).
- 总闸 attempt 2: `t4_gate_review.md` §attempt 2; 缺: 主人确认 U-1 口径 / T4.2 口径 / M-1..M-7 + 仓内可核原话; C3 逐表结案清单; t0 baseline 刷新; pre_existing 58 / FIG 11 / 规则 0 抽中类; PLAN FIG 12→11 与 T4.2 口径修订; audit_matrix T3/T4 行.
- 下游: `t4_downstream_notes.md` 末节 (rag R4 只多 TSVALCD/TSVCDREF/TSVCDVER; 标题变动 8 文件; 勿改用 R4n).
- 禁止仍有效: 不 push、不打 kb tag、不做 T4.3.
- 门禁说明: HEAD 上 `typo_assert --plan` (86 violations) 与 `ct_assert` (期望计数写死于 S-CT 前) **按设计 FAIL**, 不是回归; 拆分证明与逐条归因见 `evidence/checkpoints/t4_thaw_W1.md` / `t4_thaw_review.md` §7.
- 已知未修 (记后续): trace 中本 session 追加行的时间戳为事后取整回填 (06:00Z / 12:00Z, 总闸 attempt 2 已指出); `t4_ack_lists.md` 把 p0362_a010 记在 U-7 名下 (实为主控决定 M-4); registry B-IS T-6 页号写 p241 应为 p239 (W1 发现); audit_matrix 缺 U-5 / 解冻轮 / attempt 2 行; MK 表 en dash (代裁 Q3); O63-O67; TT/TP DOMAIN 格 (M-2).
- 汇报文件: `evidence/checkpoints/t4_attempt2_report.md`.
- **2026-11-27 主人本人确认** U-1 口径 / T4.2 方案 / 追认 M-1..M-7 / §000 委托代裁全部 → `evidence/checkpoints/t4_owner_confirmation.md`; PLAN 升 v1.4 (T4.2 行改口径, FIG 12→11). 仍开: C3 逐表结案清单、t0 baseline 刷新、pre_existing 58 / FIG 11 / 规则 0 抽中类、audit_matrix 行 → 然后 T4.1 attempt 3.
## T4 接手主控 (2026-11-27 下午, 新 session): attempt 2 缺口已补做; **等主人第二轮回答**, 之后改台账 → 总闸 attempt 3
- 入口: `evidence/checkpoints/t4_owner_decisions_round2.md` (给主人的一页, 第 3 稿, 问题 1-9, 含 4a-4d / 7a-7b). **不按委托代裁处理; 主人答复前不改台账.** 主人会在主控聊天里直接回答 → 原话逐字追加到 `t4_owner_confirmation.md` 新增一节, 并填该页末尾的 "主人选" 栏.
- 上一轮四件事 (U-1 口径 / T4.2 方案及 6 条 / M-1..M-7 / 委托本身): 以 `t4_owner_confirmation.md` (`c555bd8`, 上一任主控会话记录的主人直接确认) 为准往下走 (协调方 2026-11-27 指示, 原文留档 `t4_coordinator_note_20261127.md`); 局限照其自述保留, 由总闸 attempt 3 判断.
- 三轮独立核查 (都是 `oh-my-claudecode:tracer`, 原始结果在 `evidence/t4_supp_raw/`、`t4_q9_raw/`、`t4_round2_raw/`; 汇总 `t4_supp_fullcheck.md`):
  - 补检 203 全检: **PRE_EXISTING 层 2 条 NOT_HOLD → 触发 Q9**; 其余 9 个非空层通过. 归档 `evidence/failures/step_T4.SUPP_attempt_1.md`.
  - Q9 扩检 192: sv20 旧 EQUIVALENT 127 全检 → 51 条不成立 (标签问题, 非 KB 错); ig34 旧 EQUIVALENT 2207 抽 65 → 0 错.
  - 第二轮 175: 跨文档指针 27 全检 → 无内容错 (3 条标题口径); 已登记笔误的同类原子 103 全检 → 15 条应为 PDF_TYPO; PDF_TYPO 抽 45 → 0 错.
- 待改标签 **72 条** (`t4_relabel_pending.md`; 51 变量表行 + 2 目录条目 → IE, 19 → PDF_TYPO). 台账副本预演: U-1 B 99.2690 → 99.2651, strict 95.8041 → 95.5905 (`work/t4/supp/scenarios.json`). **台账未改** (md5 `60729f7b…`).
- G-TB4: `t4_c3_closeout.md` = census 三时点逐表比对 (50c3958 / 00a2e93 / HEAD: KB 表 501 / 500 / 497) + C3 60 张逐表结案. 脚本 `scripts/t4/t4_census_tablediff.py` → `t4_c3_closeout.py` → `t4_c3_report.py`.
- G-TB9: `t4_t0_refresh.md` — 现 KB 上重证 ALL MATCH (`scripts/t4/t0_mutation_head.sh`; 基线 `work/t4/t0_head/`, **T0 基线不覆盖**; M4a 换靶 = M-8 待追认). 基线绑定当前 KB + 台账: **改台账后必须重跑 `--make-baseline` 再跑变异**.
- 对主控这一轮产出的独立审查: `evidence/t4_gap_review_raw/review_a.md` (verifier: T0 + C3, CONDITIONAL, HIGH 0) / `review_b.md` (code-reviewer: 汇总 + 一页 + 文档, CONDITIONAL, HIGH 4 → 已按意见追加第二轮并重写) / `review_c.md` (code-reviewer 新实例 delta 复审: CONDITIONAL, HIGH 4 → 已照改; **第 3 稿未再送审**); 处理记录在各文档文末. 已知未做: 范围外笔误同类 6 条未经 tracer 确认、TYPO 宽筛候选 (范围内 169 / 范围外 142) 未审、标题类 305 条未审 — 都列在一页里等主人定.
- 文档更正: ack 清单 p0362_a010 归 M-4 (`t4_ack_lists.py` MAIN_CTRL); `t4_user_decisions.md` 状态行按确认层级重写 + §000b 加 M-8; PLAN v1.4.1 (闸表下加口径注, Q9 已触发); `audit_matrix.md` 补 T3 / U-5 / U-7 / U-6 / T4.2 / 解冻轮 / attempt 2 / 补检 / Q9 / 第二轮 / C3 行.
- **未做 (留到改台账那一批)**: registry 页号 `B-IS T-6` 241 → 239、`B-CP T-5` 211 → 212 (页号参与登记匹配 `t3_errata_build.py:150` / `t3_writeback.py:404`, 单改有改变台账的风险); 登记指针补全 (`t4_supp_fullcheck.md` §6). trace 里上一任会话的整点时间戳 (06:00Z / 12:00Z) 无法还原, 保持原样; 本会话追加行用真实 `date -u`.
- 总闸 attempt 3 用的预跑脚本已备: `scripts/t4/t4_gate_prerun.sh` (审查角色 `feature-dev:code-reviewer` 没有 Bash, 需要的复跑输出事先跑好). **不要与别的变异脚本同时跑** (共用 `work/scratch/` 下的 KB 副本).
- 脚本坑: **不要 import / 重跑 `t4_sample.py`、`t4_render.py`** (模块级写 gate / human 样本文件); 补检 / Q9 / 第二轮脚本是 exec 它们的定义段. 写含 heredoc 的 shell 脚本用写文件工具, 不要外层再套 heredoc.
- 禁止仍有效: 不 push、不打 kb tag、不做 T4.3; KB 冻结 (`git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`). 同一工作树若出现不是自己做的新提交 → 先停下来告诉协调方.
