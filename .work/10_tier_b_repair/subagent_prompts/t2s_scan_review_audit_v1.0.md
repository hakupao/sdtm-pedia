# T2-post 扫描批 Reviewer / Auditor Brief v1.0 (主控 2026-11-26)

> 在 `t2_reviewer_v1.0.md` / `t2_auditor_v1.0.md` + `t2_reviewer_common_brief.md` + `t2_dispatch_notes.md` 之上, 覆盖原子驱动的部分. writer 授权见 `t2s_scan_writer_v1.0.md`.
> 工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`. 批次 json `work/t2_batches/<S-批>.json` (无 `atoms[]`; 有 `sections` / `gaps` / `intros` / `footnote` / `census_items` / `pdf_ranges`).
> scratch 只用 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_<S-批>_<role>/` (旧 session 路径作废). 只读 KB; 禁止 git stash/checkout/reset/commit. heredoc 一律 `<<'EOF'`.

## Reviewer (`oh-my-claudecode:code-reviewer`)
1. **独立双向全扫**: 对 `sections` 的完整页范围 (先复核 writer 的页范围结论) 逐页 PDF→KB 与 KB→PDF, 含表格原子; 不只核 writer 声明的改动. 证据写逐页表 (同 writer 格式), 自己的计数, 不抄 writer 的.
2. **gaps / intros / footnote / footnote_moves** 每项逐条核: 位置 (host 顶部 / spec.md 最后变量块之后、Cross References 之前, U7)、逐字、CT `*` 照录. 本批 spec.md 的 `Controlled Terms` 字段: 对 PDF spec 表 CT 列逐变量核 (渲染图), 列出全部变量的结果.
3. **census**: 用 `pdf_ranges` 跑 `table_census.py` (命令见 `t2_reviewer_v1.0.md`); `census_items` 每张表渲染逐格 (不采信 writer 结论), 逐格表进证据.
4. **结构改动清单 / 删除清单 / D6 清单** 逐条签字 (PDF 出处或无出处证据).
5. **排版字符**: 既有文字仅排版差异 (引号/dash/省略号/○□) 不算缺陷 (S-TYPO 负责); 新插入文字须照 PDF 原字符.
6. 授权范围: `git diff HEAD --stat -- knowledge_base/` 中本批改动只落在 `kb_files` + `narrow_files` (narrow 文件 diff 只能是 json 写明的那一项). 工作树可能有别批改动, 只看本批文件.
7. fp_match 回归: 先 diff `work/t2_fp_expected_regressions.jsonl` (已知预期回归不计); 本批文件新增 RED 逐条定性.
8. 输出 `evidence/checkpoints/t2_<S-批>_review.md` (PASS / CONDITIONAL+可执行修正清单 / FAIL) + trace 一行 (`"step": "T2S.<S-批>"`). `python3 tools/check_links.py 2>&1 | grep "live docs"` = 42 记录. 回主控 ≤ 10 行.

## Auditor (`oh-my-claudecode:verifier`, Rule A)
- 先独立判, 判完才读 writer/reviewer 报告.
- 总体 P = `work/pdf_atoms.jsonl` 中 atom_type ∈ SENTENCE / LIST_ITEM / NOTE / CROSS_REF / TABLE_ROW, 页码在 `sections` 各范围内且 `parent_section` 属于该节 (以节号前缀判, 边界页别节原子排除), 去 ledger INTENTIONAL_EXCLUDE. 再并入 `intros` 的原子.
- **N = min(30, max(20, ceil(0.1 × |P|)), |P|)**; 其中至少 1/3 取自 writer 改动行 (writer.jsonl 涉及的页) 上的原子, 其余 P 中随机. seed = `20261126`. 抽样脚本写进证据 (可复跑, 参考 `t2_auditor_v1.0.md` 的写法).
- 每样本判: 独有信息丢失 / 忠实 / 位置 (R2 口径). TABLE_ROW 样本须渲染原页逐格.
- 另做: `intros` 与 `gaps` 每项是否落地 (逐字 + 位置); 本批 kb_files 内任一行无 PDF 出处且未 D6 标注 → 计忠实度错误 (纯导航除外: 标题/锚点/交叉引用/`> Class|Structure` 行/Cross References 块/表前短标签如 `**CRF: …**`, U8). CT C-code 记法与 DOMAIN CT 空值不计 (U5/U6 归 S-CT).
- 任一丢失/忠实错误 > 0 → FAIL. 输出 `t2_<S-批>_audit.md` + `audit_matrix.md` 追加一行 (格式照 T2 行, 首列 `T2S.<S-批> auditor aN`) + trace 一行. G-TB8: trace 中本批有 writer + reviewer 的 subagent_done. 回主控 ≤ 8 行.
