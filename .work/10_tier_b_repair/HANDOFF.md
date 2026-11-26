# 10_tier_b_repair — 主控 handoff (压缩/换 session 时先读)
> 更新: 2026-11-26. 本文件只记"在途状态 + 主控规程", 规则本体见 PLAN.md / subagent_prompts/t2_dispatch_notes.md / evidence/checkpoints/t1_user_ack.md (R1-R4, D1-D7).

## 每批流程 (主控只派发/裁定/提交, 不写 KB)
writer (oh-my-claudecode:executor, opus) → reviewer (oh-my-claudecode:code-reviewer) → auditor (oh-my-claudecode:verifier).
writer 在 reviewer PASS 后再改 → 回 reviewer 复审 delta 才派 auditor. auditor PASS → 主控 `git add` 本批 kb_files + 证据 + audit_matrix/trace/errata → 本地 commit (不 push; T4 后统一 push).
派发 prompt 模板: 见已提交的 t2_B-*.md 同类; writer 必读 t2_writer_v1.0.md + t2_dispatch_notes.md + batch json + t1_user_ack.md.
范围外发现 → work/out_of_scope_findings.md (O1-O25); 原子抽错 → work/t1_errata.json `t3_atom_err`; target 迁移 → `t3_target_remap`; T4 用户裁定项散落各 checkpoint, T4 前汇总 (O25).
check_links live docs 基线 42 (汇总行走 stderr: `2>&1 | grep "live docs"`); evidence 里 md 链接写法须反引号.

## 已提交批 (见 git log "Tier B batch")
## 在途 (2026-11-26; 已提交 43 批, 最新 B-FT)
- writer 共用 brief: subagent_prompts/t2_writer_common_brief.md; reviewer/auditor 共用 brief: subagent_prompts/t2_reviewer_common_brief.md
- B-CE: writer 完成 (O4 关闭, O10 CE Ex2 已修; CRF 描述名按 B-AE L-2 保留) → reviewer CONDITIONAL (C-1 Ex1 CRF / C-2 Ex2 日期格 / C-3 USUBJID 空格照录+T4) → writer a2 在跑
- B-CM: writer a2 完成 (2c 末句 D2 删, 副本 spec.md:84) → reviewer 在跑
- B-QS: reviewer PASS → auditor 在跑
- B-HO: reviewer PASS → auditor 在跑
- B-MI: reviewer PASS (O43 T4) → auditor 在跑
- B-CO / B-DV / B-IE / B-ML: writer 在跑
## 待开 (按 order): B-SU B-SV(O33) B-TI B-TV B-ch03 B-DI ... B-SUPPQUAL(D7) ... B-SC (其余见 work/t2_batches/)
## T2 后: O15/O16/O17/O18/O20/O24 全域扫描小批 (Description/Overview, spec 首句, §6.x 类引言, 漏页, spec.md 记法) → T3 (ledger 回写 + t3_atom_err + target_remap) → T4 (总闸 + T4 用户裁定汇总 + 人工 30 抽样) → push + 提醒 sdtm-rag
