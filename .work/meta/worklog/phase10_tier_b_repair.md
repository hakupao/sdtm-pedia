<!-- chain: B -->
# Phase 10 旁枝 — Tier B 内容补修 worklog (append-only)

## 2026-11-26 T2 全部完成 (60/60 批, 本地 commit, 未 push)
- 流程: 每批 writer (executor) → reviewer (code-reviewer) → auditor (verifier, Rule A seed 20261126); PASS 后主控按批本地 commit。证据: `.work/10_tier_b_repair/evidence/checkpoints/t2_B-*.md` + `audit_matrix.md` + `trace.jsonl`。
- 全局核查 (T2 收口): census 全量重跑 HEAD (501 表: OK 311 / DIFF 37 全部已登记或已人工 / UNPARSEABLE 149, 其中 60 张无逐格证据 = C3 待扫; C1 3 张 SE/TD 表头 PDF 笔误待补登 T-n) → `evidence/t2_census_global_triage.md`; fp 全局 60 条回归逐条定性 R4=0 (无真丢失), errata 已合并 → `evidence/t2_fp_expected_regressions.md`; 覆盖矩阵 (缺 Description 12 域 / spec 首句 17 / Assumptions 标题 14 / spec 脚注 58 / 未终版全扫文件 132) → `evidence/t2_coverage_matrix.md`。
- 用户规则级裁定 U1-U4 (排版字符照 PDF / spec 脚注进 spec.md + CT "*" / 章引言放该章首域 assumptions 顶部 / CRF ○□) → `evidence/checkpoints/t2_post_user_ack.md`。
- 范围外登记 O1-O53 → `work/out_of_scope_findings.md` (T4 用户裁定项散落, O25 汇总待生成)。
- 下一步: T2 后扫描批 (S-*, 按覆盖矩阵分组, 每文件一批) → T3 (ledger 回写) → T4 (总闸 + 用户裁定汇总 + 人工抽样) → push + 提醒 sdtm-rag。

## 2026-11-26 T2S 扫描批全部完成 (22/22, 本地 commit, 未 push)
- 新 brief `t2s_scan_writer_v1.0.md` / `t2s_scan_review_audit_v1.0.md`; 试点 S-EVT 后并行 ≤4 批; 每批 writer (executor) → reviewer (code-reviewer) → auditor (verifier, Rule A seed 20261126)。
- 用户裁定 U5 (CT 保留 C-code + PDF 短名 `(NY) C66742`) / U6 (DOMAIN CT = 域代码); 主控 U7/U8 (脚注位置 / 导航不 D6)。
- 域 / 章 / model 全扫: 覆盖矩阵全部文件 FINAL; spec.md 1917 变量对 PDF 逐字段核; S-CT 570 CT 格 + 59 DOMAIN; S-TYPO 356 处排版字符 (CRF ○□ 交 T4)。
- 两个脚本批按 advisor 意见先 dry-run, 断言均做变异测试 (S-CT 12 种 / S-TYPO 27+9 种), reviewer 各抓出一个断言盲区后补强。
- 产出 PDF_TYPO 登记表 270 条 + T4 用户裁定汇总 (O25)。范围外 O54-O62。
- 下一步 T3 (ledger 回写 + 重算) → T4 → push。

## 2026-11-27 T4.1 总闸 attempt 1 + T4.2 样本备齐 (等用户)
- 总闸 `feature-dev:code-reviewer` ×5 (本项目首次用): 分层样本 84 条 (PLAN 72 + 补充 SUPP 12, seed 20261127) 全部 HOLDS; 证据层判 **不通过 (CONDITIONAL)**: G-TB1/2 未过 (残留 `ig34_p0056_a006` + 三类无用户 ack), G-TB3 06 公式照套 strict 96.0741% < 99.02%, mapped 99.3578% 过但口径未经用户认可。报告 `.work/10_tier_b_repair/evidence/checkpoints/t4_gate_review.md`。
- 覆盖率下降分解: 319 行 "06 算覆盖 → 现标 ATOM_ERR/PDF_TYPO/FIG" 贡献约 −3.19pp; 若这 319 行仍算覆盖为 99.27% (`scripts/t4/t4_coverage_decomp.py`)。
- T4.2 人工抽样包 42 条 (正式 30 + 节锚无效风险层 12) 已备, 判定栏空; ATOM_ERR/PDF_TYPO/FIG 330 原子确认清单 `t4_ack_lists.md`; 用户裁定入口 `t4_user_decisions.md` §00 U-1~U-11。
- KB 冻结 (sdtm-rag 入库预演), 本日 KB 0 改动; 未 push、未打 tag。

## 2026-11-27 答复 sdtm-rag 入库预演的 7 个问题 (只读)
- 文档 `.work/10_tier_b_repair/evidence/checkpoints/t4_downstream_notes.md`: CT 单元格 6 种形态与 "下游格式约定" (以后改格式先通知 sdtm-rag); `*` = SDTMIG §4.3.1 "CT 暂无" 标记; DOMAIN CT = 字面值; DM RFSTDTC/RFENDTC = Char 照 PDF p63; model 6 列行照 SDTM v2.0 (第 6 列为 KB 自写); kb-2026.11.25 以来节变动清单 (脚本 `scripts/t4/t4_heading_diff.py`); 示例标题格式 7 个文件有变 (PC `## PC – Examples`)。
- 新 KB 观察项 2 条记入 `t4_user_decisions.md` U-10 ⑥⑦。KB 未改, 未 push。

## 2026-11-27 T4 解冻轮 + 总闸 attempt 2 (上一任主控会话; 接手主控补记, 细节以 HANDOFF 为准)
- 委托代裁落实; 唯一一次解冻改 KB (`a59c2d3`, 25 文件; writer / reviewer / auditor 三个角色); 台账重跑后 U-1 B 口径 99.2690%, strict 95.8041%。
- T4.2 人工闸改为 "AI 预筛 42 + 主人抽查 6" (6/6 内容正确)。总闸 attempt 2 = 不通过 (CONDITIONAL): 来源可核性不足 + C3 结案清单 / T0 变异重证 / "0 抽中" 各类等缺口。
- 主人确认记录 `.work/10_tier_b_repair/evidence/checkpoints/t4_owner_confirmation.md` 第一节 (`c555bd8`)。

## 2026-11-27 T4 接手主控: 补 attempt 2 缺口 + 主人第二轮 + 改台账 + 总闸 attempt 3 (KB 全程冻结)
- 补缺口: C3 60 张表逐表结案 + census 三时点逐表说明 (`t4_c3_closeout.md`); T0 变异在现 KB 重证 ALL MATCH (`t4_t0_refresh.md`, 新脚本 `scripts/t4/t0_mutation_head.sh`); "0 抽中" 各类全检 203 条 → 2 条旧 EXACT 不成立 → 触发 PLAN Q9, 追加 Q9 扩检 192 / 第二轮 175 / 第三轮 315, 共 885 条独立审查 (`t4_supp_fullcheck.md`)。没有查出 KB 内容写错; 查出的是台账标签不准。
- 主人在主控聊天里直接回答第二轮 13 个小问 (全按建议; 原话逐字在 `t4_owner_confirmation.md` 第二轮一节); 问题 A / B 未答。
- 改台账 R2L (`5d7e4cb`): 78 条 (53 → INTENTIONAL_EXCLUDE, 25 → PDF_TYPO), executor → code-reviewer → verifier (33/33)。现值 U-1 B 99.2651% / strict 95.5301%; PDF_TYPO 174; 登记表 274 行。
- 总闸 attempt 3 (`feature-dev:code-reviewer`) = **不通过 (CONDITIONAL)**: 9 条闸无 NOT_MET, 裁定来源判足够; 唯一挡闸项 = 4 条多标的 PDF_TYPO 待主人选 (问题 A)。`t4_gate_review.md` §attempt 3; 归档 `evidence/failures/step_T4.1_attempt_3.md`。
- 未 push, 未打 kb tag, 未做 T4.3; KB 树 `63f857774a42cfaa71798705ad40ab51bc5e378a` 不变。
- (同日夜, 续) 主人直接回答 「A1、B1、追认 M-9」: 4 条多标的 PDF_TYPO 改回 EXACT (R3L, `d794fb6`; executor → code-reviewer PASS), 1 条判不了的维持并写明。现值 U-1 B 99.2651% / strict 95.5703%; PDF_TYPO 170; 待改清单 82 条全部已执行。
- attempt 3 的 delta 闸审 (另一个 `feature-dev:code-reviewer` 新实例) = **PASS** → **T4.1 总闸通过**。`t4_gate_review.md` "§attempt 3 delta"。不挡闸的未决: M-10 待主人追认; ATOM_ERR 约 83 条是否加一轮逐条审。
- 仍未 push, 未打 kb tag, 未做 T4.3; KB 树不变。

## 2026-11-27 夜 T4 加查: ATOM_ERR (S1-R1) 里没被逐条看过的那批 (KB / 台账都没动)
- 主人选 "加查" (协调方转述). 筛法 `scripts/t4/t4_atomerr_sample.py`: S1-R1 157 = 已逐条判过 80 + 从未逐条判过 77 (总闸估 83 = 157 − 74)。
- 全检 83 条 (77 + 6 盲复检), `oh-my-claudecode:tracer` ×4: 成立 82 / 不成立 1 / 判不了 0。不成立 = `ig34_p0124_a001` (标 ATOM_ERR, 实为 EXACT); `general-purpose` 盲复看相同。汇总 `.work/10_tier_b_repair/evidence/checkpoints/t4_atomerr_fullcheck.md`; 归档 `evidence/failures/step_T4.AE_attempt_1.md`。
- 台账未改 (md5 `43809870…`); 问题 C (改回 EXACT / 维持) 与 M-10 追认都等主人直接答 — 本会话两项都问了, 未答。
- 未 push, 未打 kb tag, 未做 T4.3; KB 树 `63f857774a42cfaa71798705ad40ab51bc5e378a` 不变。

## 2026-11-27 夜 (续) 主人答 C1 / D1 / 追认 M-10 → 改台账 R4L (KB 没动)
- 主人在主控聊天里直接回答 「C1、D1、追认 M-10」 (逐字在 `.work/10_tier_b_repair/evidence/checkpoints/t4_owner_confirmation.md` 消息 5); 对发版的同意经协调方待办项转达 (同一文件)。
- R4L (`65d6a0f`): `ig34_p0124_a001` ATOM_ERR → EXACT (由 live-hit 判出), 4 条补登记指针; executor → code-reviewer PASS → 小修 → delta PASS。台账 `eef9bb14…`; 现值 U-1 B 99.2651% / strict 95.5804%; ATOM_ERR 196 / EXACT 4711。
- D1: `B-CE T-2` 那 8 条维持 ATOM_ERR, 口径 (值内空格算真实差异) 登记在 `t4_user_decisions.md` §000c。M-10 已追认。
- T0 变异基线第三次重建 ALL MATCH; 推送前检查脚本 `scripts/t4/t4_prepush_check.sh` 预跑无拦截项 (不含用户名的机器路径由协调方裁定放行)。

## 2026-11-28 (本地; UTC 2026-11-27) T4.3 收尾 + 发版
- 总闸: 加查与 R4L 之后的 delta 闸审 = **PASS** (`feature-dev:code-reviewer` 又一新实例; `evidence/t4_gate_raw/attempt3_delta2_report.md`); "ATOM_ERR / PDF_TYPO 补抽" 一项判 已关 (带局限)。需主人但不挡: M-11 追认、D1 的折行边界。
- Chain D: `.work/meta/mapping.md` 加 "Tier B 内容补修" 一节 → `docs/TRACEABILITY.md` 加 §7 → 本条。`RETROSPECTIVE.md` (三段 + 终态数字 + 已知局限)。
- 终值: KB 相对 `kb-2026.11.25` 改 193 文件; U-1 B 9860/9933 = 99.2651%; strict 9494/9933 = 95.5804%; mapped 9494/9556 = 99.3512%; 内容 8660/9556 = 90.6237%; 范围内 174 节残留 0; live docs 42。
- 推送前检查 (`scripts/t4/t4_prepush_check.sh`; 口径与输出 `evidence/checkpoints/t4_prepush_check.md`) → `git push origin main` → 标签 `kb-2026.11.28`。推送结果与网站核对记在 `evidence/checkpoints/t4_release.md`。
- 下游: sdtm-rag 的 "KB 更新" 由协调方另派, 变更要点 `evidence/checkpoints/t4_downstream_notes.md`。
