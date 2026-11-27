# 10_tier_b_repair — 主控 handoff (压缩/换 session 时先读)
> 更新: 2026-11-27 (T4.1 attempt 1 后). 本文件只记"在途状态 + 主控规程", 规则本体见 PLAN.md / subagent_prompts/t2_dispatch_notes.md / evidence/checkpoints/t1_user_ack.md (R1-R4, D1-D7).

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
## T4 在途 (2026-11-27): T4.1 attempt 1 = **不通过 (CONDITIONAL)**; T4.2 样本已备; **全部等用户裁定**
- KB 冻结中 (sdtm-rag 用 00a2e93 内容做入库预演): 本阶段 **不改 `knowledge_base/`**, 不 push, 不打 kb tag, 不做 T4.3.
- 总闸: `evidence/checkpoints/t4_gate_review.md` (主控誊录 + 计数); 审查原文 `evidence/t4_gate_raw/{pack1..4,evidence_layer}.md`; brief `subagent_prompts/t4_gate_reviewer_v1.0.md`.
  - 样本 84/84 HOLDS (正式 72 + 补充 SUPP 12; seed 20261127). 证据层: G-TB1/2 NOT_MET (残留 p0056_a006 + 三类无 ack)、G-TB3 字面 NOT_MET (strict 96.0741%) / mapped 99.3578% 过但无用户认可.
- 用户待裁 (唯一入口): `evidence/checkpoints/t4_user_decisions.md` **§00 U-1~U-11** (口径/残留/父节/C 层/三类 ack/人工抽样/A-B 表/范围外 4/S-TYPO/KB 观察项/Mermaid); 三类逐条 `evidence/checkpoints/t4_ack_lists.md`; 人工抽样 `evidence/checkpoints/t4_human_sample.md` (42 条, 判定栏空).
- 复跑: `python3 -I $T/scripts/t4/t4_sample.py && python3 -I $T/scripts/t4/t4_render.py` (注意: render 会整体重写 t4_human_sample.md, 有用户判定后不要再跑或先誊出); `t4_ack_lists.py`; `t4_coverage_decomp.py`. HEAD 复跑结果 (live docs 42 / t3_mutation 同 T3 / census OK311 DIFF37 diffs144) 见 gate_review §3.
- 用户裁定回来后: ① 按 U-2/U-8 改 ledger (走 writer→reviewer, 主控不写); ② KB 解冻后按 U-7/U-9/U-10 改 KB (正常批流程); ③ 证据层审查者建议的补强 (pre_existing 58 条单独核、C7 38 条 ATOM_ERR 全检、FIG 11 条、C3 表结案清单、文档状态行过期) 视用户 U-5 选择做; ④ T4.1 attempt 2 (同角色 feature-dev:code-reviewer, 新实例) → T4.3 (Chain D + RETROSPECTIVE + push + kb tag + 提醒 sdtm-rag).
- 风险提示: 下一个会话若重跑 `t4_render.py` 会覆盖用户在 t4_human_sample.md 的勾选.
