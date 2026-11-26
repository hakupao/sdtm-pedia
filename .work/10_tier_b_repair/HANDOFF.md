# 10_tier_b_repair — 主控 handoff (压缩/换 session 时先读)
> 更新: 2026-11-26. 本文件只记"在途状态 + 主控规程", 规则本体见 PLAN.md / subagent_prompts/t2_dispatch_notes.md / evidence/checkpoints/t1_user_ack.md (R1-R4, D1-D7).

## 每批流程 (主控只派发/裁定/提交, 不写 KB)
writer (oh-my-claudecode:executor, opus) → reviewer (oh-my-claudecode:code-reviewer) → auditor (oh-my-claudecode:verifier).
writer 在 reviewer PASS 后再改 → 回 reviewer 复审 delta 才派 auditor. auditor PASS → 主控 `git add` 本批 kb_files + 证据 + audit_matrix/trace/errata → 本地 commit (不 push; T4 后统一 push).
派发 prompt 模板: 见已提交的 t2_B-*.md 同类; writer 必读 t2_writer_v1.0.md + t2_dispatch_notes.md + batch json + t1_user_ack.md.
范围外发现 → work/out_of_scope_findings.md (O1-O25); 原子抽错 → work/t1_errata.json `t3_atom_err`; target 迁移 → `t3_target_remap`; T4 用户裁定项散落各 checkpoint, T4 前汇总 (O25).
check_links live docs 基线 42 (汇总行走 stderr: `2>&1 | grep "live docs"`); evidence 里 md 链接写法须反引号.

## 状态 (2026-11-26): T2 完成 — 60/60 批本地 commit (未 push, 领先 origin ~70 commit)
- 全局核查: `evidence/t2_census_global_triage.md` (C3 60 张 UNPARSEABLE 无逐格证据: ch04 23 / model02 15 / EX 8 / model03 7 / ch10 5 / model04 1 / TR 1; C1 3 张 SE:44,:79 BIRTHDTC / TD:161 TDTGPAI 待补登 T-n), `evidence/t2_fp_expected_regressions.md` (60 条 R4=0, errata 已并入 t1_errata.json; 扫描批 reviewer 对 `work/t2_fp_expected_regressions.jsonl` diff, 不再各判 "他批"), `evidence/t2_coverage_matrix.md` (扫描范围)。
- 用户规则裁定 U1-U4: `evidence/checkpoints/t2_post_user_ack.md` (排版字符全照 PDF; spec 脚注进 spec.md + CT "*"; 章引言放该章首域 assumptions 顶部; CRF ○□)。
- 复跑脚本归档: `work/scratch/t2/agents/` (gitignored; 原 session scratchpad 副本) + `work/scratch/t2/global/`。
## 下一步: T2 后扫描批 (按覆盖矩阵 §7 分组, 每文件只进一批; writer/reviewer/auditor 同 T2 流程, brief 须加 U1-U4)
S-INT (AG PR EX EC; §6.1/§6.1.3 引言放首域) · S-EVT (AE DS; §6.2 引言) · S-SPC1 (CP GF IS LB) · S-SPC2 (MB MS PC PP) · S-FND (EG OE UR PE SS; §6.3 引言) · S-TUFA (TR FA SR) · S-TDM (TA TD TM; TD C1 T-n) · S-SPREL (SE RELREC RELSUB RELSPEC OI; SE C1 T-n; §9 引言放 DI 顶部) · S-CH (ch01/02/04/08/10; ch04 C3 23 表) · S-MODEL (model/01-05; C3) · S-SPEC (终版域 spec.md 全扫+脚注, U2) · S-TYPO (U1/U4 全库排版字符统一, 脚本+抽检) · S-HOST (TI §7.3 重复 / NV §6.3.6 MO 框)
## 之后: T3 (ledger 回写; t3_recompute 前先减去预期回归清单) → T4 (O25 用户裁定汇总含 "KB 写正确值" 项 + 一致性复核 NV an→a / TI that with vs MI / DV 照录; O51 Mermaid 渲染; Chain D; 人工 30 抽样) → push + 提醒 sdtm-rag
