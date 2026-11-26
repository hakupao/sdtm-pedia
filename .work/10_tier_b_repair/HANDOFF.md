# 10_tier_b_repair — 主控 handoff (压缩/换 session 时先读)
> 更新: 2026-11-26. 本文件只记"在途状态 + 主控规程", 规则本体见 PLAN.md / subagent_prompts/t2_dispatch_notes.md / evidence/checkpoints/t1_user_ack.md (R1-R4, D1-D7).

## 每批流程 (主控只派发/裁定/提交, 不写 KB)
writer (oh-my-claudecode:executor, opus) → reviewer (oh-my-claudecode:code-reviewer) → auditor (oh-my-claudecode:verifier).
writer 在 reviewer PASS 后再改 → 回 reviewer 复审 delta 才派 auditor. auditor PASS → 主控 `git add` 本批 kb_files + 证据 + audit_matrix/trace/errata → 本地 commit (不 push; T4 后统一 push).
派发 prompt 模板: 见已提交的 t2_B-*.md 同类; writer 必读 t2_writer_v1.0.md + t2_dispatch_notes.md + batch json + t1_user_ack.md.
范围外发现 → work/out_of_scope_findings.md (O1-O25); 原子抽错 → work/t1_errata.json `t3_atom_err`; target 迁移 → `t3_target_remap`; T4 用户裁定项散落各 checkpoint, T4 前汇总 (O25).
check_links live docs 基线 42 (汇总行走 stderr: `2>&1 | grep "live docs"`); evidence 里 md 链接写法须反引号.

## 已提交批 (见 git log "Tier B batch")
## 在途 (2026-11-26; 已提交 33 批, 最新 B-SM)
- B-NV: reviewer PASS → auditor 在跑 (L-3: T-1 冠词错是否算 PDF_TYPO → T4 一并看) (主控认可 R3 补 p286 §6.3.7.1 通用表, LB 先例; F-1→O31) (共用 brief = subagent_prompts/t2_writer_common_brief.md: assumptions.md 仅 Desc/spec 首句/节引言 NOTE 授权)
- B-model05 / B-CV / B-DM / B-RS: writer 在跑
## 待开 (按 order): B-TS B-model06 B-CE ... B-SUPPQUAL(D7) ... B-SC (其余见 work/t2_batches/)
## T2 后: O15/O16/O17/O18/O20/O24 全域扫描小批 (Description/Overview, spec 首句, §6.x 类引言, 漏页, spec.md 记法) → T3 (ledger 回写 + t3_atom_err + target_remap) → T4 (总闸 + T4 用户裁定汇总 + 人工 30 抽样) → push + 提醒 sdtm-rag
