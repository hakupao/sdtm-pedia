# 10_tier_b_repair — 主控 handoff (压缩/换 session 时先读)
> 更新: 2026-11-26. 本文件只记"在途状态 + 主控规程", 规则本体见 PLAN.md / subagent_prompts/t2_dispatch_notes.md / evidence/checkpoints/t1_user_ack.md (R1-R4, D1-D7).

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
## 下一步: T4 (总闸 feature-dev:code-reviewer + `t4_user_decisions.md` 逐条 A/B + 人工 30 抽样 + Chain D) → push + KB tag + 提醒 sdtm-rag
- T4 须并入: PDF_TYPO/ATOM_ERR/FIG 用户 ack; 风险层 `work/t3_t4_risk_anchorless.txt` (508 条节锚无效 EXACT) 加一层人工抽样; 范围外 `work/t3_t4_k3b_out_of_scope.txt`; keep 清单 p0412_a008/p0342_a007 定位行 (低).
