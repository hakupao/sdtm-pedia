# 10_tier_b_repair — 主控 handoff (压缩/换 session 时先读)
> 更新: 2026-11-26. 本文件只记"在途状态 + 主控规程", 规则本体见 PLAN.md / subagent_prompts/t2_dispatch_notes.md / evidence/checkpoints/t1_user_ack.md (R1-R4, D1-D7).

## 每批流程 (主控只派发/裁定/提交, 不写 KB)
writer (oh-my-claudecode:executor, opus) → reviewer (oh-my-claudecode:code-reviewer) → auditor (oh-my-claudecode:verifier).
writer 在 reviewer PASS 后再改 → 回 reviewer 复审 delta 才派 auditor. auditor PASS → 主控 `git add` 本批 kb_files + 证据 + audit_matrix/trace/errata → 本地 commit (不 push; T4 后统一 push).
派发 prompt 模板: 见已提交的 t2_B-*.md 同类; writer 必读 t2_writer_v1.0.md + t2_dispatch_notes.md + batch json + t1_user_ack.md.
范围外发现 → work/out_of_scope_findings.md (O1-O25); 原子抽错 → work/t1_errata.json `t3_atom_err`; target 迁移 → `t3_target_remap`; T4 用户裁定项散落各 checkpoint, T4 前汇总 (O25).
check_links live docs 基线 42 (汇总行走 stderr: `2>&1 | grep "live docs"`); evidence 里 md 链接写法须反引号.

## 状态 (2026-11-26 晚): **T2S 全部完成 — 22/22 扫描批本地 commit (未 push)**
- 已提交 (writer→reviewer→auditor 全 PASS): S-EVT S-INT S-FND S-SPC1 S-SPC2 S-HOST S-TDM S-TUFA S-SPREL S-CH1 S-CH4 S-CH8 S-CH10 S-MOD1 S-MOD2 S-MOD3 S-SPEC1..4 S-CT (U5/U6 脚本批) S-TYPO (U1 排版脚本批)。
- 扫描批口径: brief `subagent_prompts/t2s_scan_writer_v1.0.md` / `t2s_scan_review_audit_v1.0.md`; 批中主控裁定在 `subagent_prompts/t2_dispatch_notes.md` 末尾; 用户/主控规则 U1-U8 在 `evidence/checkpoints/t2_post_user_ack.md`。
- 覆盖矩阵 (`scripts/t2s/t2_coverage_matrix.py`): 全部 domains/chapters/model 文件 FINAL; 残留 fn 缺口 3 个均假阳 (DI 无 spec 表 / ML O61 / SE O58)。
- 脚本 (已提交): `scripts/t2s/` — spec 比对 sc2/sc2w/speccmp2, CT ct_extract/ct_apply/ct_assert, 排版 typo_plan/typo_assert(--plan)/typo_mutate, reviewer 独立校验 review_S-TYPO/。
- T4 底稿: `work/t2_pdf_typo_registry.jsonl` (270 条 PDF_TYPO/T-n) + `evidence/checkpoints/t4_user_decisions.md` (O25 用户裁定汇总, 含 S-TYPO 追加项: CRF ○□ 口径、MH `History“`、残余 230 行)。
## 下一步: T3 (PLAN §4 T3.1/T3.2, §5.2)
- T3.1 ledger 回写 (工作副本 `work/coverage_ledger.wc.jsonl`): 改动集 ⊆ 分诊集 + T2S 新增; 每条带 `matched_by.phase="TB"`。
- T3.2 重算 + 反向溯源: 先 fp_match 对所有指纹定的 EXACT/EQUIVALENT 在现 KB 复验; 减去 `work/t2_fp_expected_regressions.jsonl`; 注意 fp_match 归一化排版, S-TYPO 不影响。
## 之后: T4 (总闸 + `t4_user_decisions.md` 逐条让用户 A/B + 人工 30 抽样 + Chain D) → push (提醒 sdtm-rag: CT 字段格式改为 `(NY) C66742`、DOMAIN CT=域代码、排版字符照 PDF) + KB tag
