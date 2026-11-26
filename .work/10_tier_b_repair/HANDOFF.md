# 10_tier_b_repair — 主控 handoff (压缩/换 session 时先读)
> 更新: 2026-11-26. 本文件只记"在途状态 + 主控规程", 规则本体见 PLAN.md / subagent_prompts/t2_dispatch_notes.md / evidence/checkpoints/t1_user_ack.md (R1-R4, D1-D7).

## 每批流程 (主控只派发/裁定/提交, 不写 KB)
writer (oh-my-claudecode:executor, opus) → reviewer (oh-my-claudecode:code-reviewer) → auditor (oh-my-claudecode:verifier).
writer 在 reviewer PASS 后再改 → 回 reviewer 复审 delta 才派 auditor. auditor PASS → 主控 `git add` 本批 kb_files + 证据 + audit_matrix/trace/errata → 本地 commit (不 push; T4 后统一 push).
派发 prompt 模板: 见已提交的 t2_B-*.md 同类; writer 必读 t2_writer_v1.0.md + t2_dispatch_notes.md + batch json + t1_user_ack.md.
范围外发现 → work/out_of_scope_findings.md (O1-O25); 原子抽错 → work/t1_errata.json `t3_atom_err`; target 迁移 → `t3_target_remap`; T4 用户裁定项散落各 checkpoint, T4 前汇总 (O25).
check_links live docs 基线 42 (汇总行走 stderr: `2>&1 | grep "live docs"`); evidence 里 md 链接写法须反引号.

## 状态 (2026-11-26 晚): T2S 扫描批 21/23 完成 (本地 commit, 未 push; 领先 origin ~88 commit)
- 扫描批流程: brief `subagent_prompts/t2s_scan_writer_v1.0.md` + `t2s_scan_review_audit_v1.0.md`; 每批派发 prompt 存 `subagent_prompts/t2s/<批>_<role>_a1.md`; 用户/主控裁定 U1-U8 见 `evidence/checkpoints/t2_post_user_ack.md`, 批中主控口径追加在 `subagent_prompts/t2_dispatch_notes.md` 末尾 (T2S 段之后各条).
- 已提交 (writer→reviewer→auditor 全 PASS): S-EVT S-INT S-FND S-SPC1 S-SPC2 S-HOST S-TDM S-TUFA S-SPREL S-CH1 S-CH4 S-CH8 S-CH10 S-MOD1 S-MOD2 S-MOD3 S-SPEC1..4.
- 覆盖矩阵 (`scripts/t2s/t2_coverage_matrix.py`, `MATRIX_TAG=<tag>` 输出到 scratch): 全部 domains/chapters/model 文件 FINAL; 残留 fn 缺口 3 个均假阳 (DI 无 spec 表 / ML O61 / SE O58).
- 共用工具: `scripts/t2s/{sc2.py,sc2w.py,speccmp2.py}` (spec 表 bbox 比对; 各有盲区, 交叉用 + 计数闸; 旧 speccmp.py 有 4 种失效勿用).
## 下一步 (advisor 2026-11-26 意见, 必须照做)
1. **S-CT** (`work/t2_batches/S-CT.json`): 先 **dry-run 只出报告不写**: 每变量 CT 单元格分类 (1:1 / 数量不符 / KB 空 PDF 有名 / KB 有码 PDF 空或 * / 名对应别的码); 短名以 PDF 单元格为准, xlsx 只作交叉核; 同一 dry-run 用修正版解析器对 S-EVT…S-SPREL 各域 spec.md 全字段重比 (那些批用过有缺陷的 speccmp.py), 报非 U5/U6 差异. 非 1:1 类先定规则 (多则问用户) 再授权写. tools/ web/src 无 Controlled Terms 解析器; push 时提醒 sdtm-rag CT 字段格式变了.
2. **S-TYPO** (`work/t2_batches/S-TYPO.json`): 先建 PDF_TYPO/T-n 登记表 (= O25 汇总底稿) 作 do-not-touch 清单; 断言改为 "每个 diff 都是闭表替换, 无非空白字符增删" (比 alnum-equal 严); ○□/上标 pdftotext 给不出 → 枚举清单对渲染; 只在文件自身页范围内找、多命中一致即可; 报覆盖率 (已解决行 / 含排版字符行); fp_match 与矩阵对排版盲, 不作闸; Rule A 按替换类分层抽.
3. 两批新断言都做变异测试 (retrospective 规则 5): 植入 alnum 改动 / 删连字符 / 改标题 / 改 `--VAR` / 改 T-n 段 / S-CT 改非 CT 行, 闸必须红. 变换与断言脚本放 `scripts/t2s/` (提交), 不放 session scratch.
## 之后: T3 (ledger 回写; t3_recompute 前先减去 `work/t2_fp_expected_regressions.jsonl`) → T4 (O25 用户裁定汇总: 含各批 "照录 + T4" 项、TR T-5 TAETORD、TD U-1 every 24 weeks、UR U-1/O55 per per、O56 PP 摘要节、O60 标题口径统一; O51 Mermaid; Chain D; 人工 30 抽样) → push + 提醒 sdtm-rag
