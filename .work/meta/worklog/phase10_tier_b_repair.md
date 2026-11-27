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
