批次 S-CT (T2-post 全库脚本批, U5/U6), attempt 2 (写入). 角色: reviewer.
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。读: `.work/10_tier_b_repair/subagent_prompts/t2s_scan_review_audit_v1.0.md` Reviewer 段 (按脚本批适配), `evidence/checkpoints/t2_post_user_ack.md` (U5/U6), `subagent_prompts/t2_dispatch_notes.md` 末尾, writer 报告 `evidence/checkpoints/t2_S-CT_dryrun.md` + `t2_S-CT.md` + `work/t2_batches/S-CT.writer.jsonl`。改动未提交: `git diff HEAD --stat -- knowledge_base/` (63 个 spec.md)。主控裁定: U6 闸 59/59; KB note 只加含 C-code 的 59 个 spec.md; SR SRDY "sponsor- defined"→"sponsor-defined" 为唯一非 CT 行白名单 (SR T-5); 多 codelist 格 `(A) Cx; (B) Cy`。
你的任务 (独立, 不信 writer):
1. 通读 `scripts/t2s/ct_apply.py` 与 `ct_assert.py`, 判断断言是否真能证明 "只改了 CT 行 + note + 白名单行, 且 CT 行仅加前缀/补域代码" —— 找出断言的盲区 (例如: 是否核了短名本身正确? 是否核了 note 位置? 是否允许空白行变化?)。
2. **自己写**一个独立校验 (不 import writer 脚本): 对全部 63 个 spec.md 与 `git show HEAD:<file>` 逐行 diff, 断言改动集合; 对每个改后的 `(SHORT) Cxxxx`, 用 `source/cdisc/SDTM Terminology.xlsx` 独立查 C-code → codelist 短名 (CDISC Submission Value), 588/588 一致; DOMAIN 59 格 = 本域代码。
3. 抽 ≥ 20 个变量 (分层: 单 codelist / 多 codelist ≥3 / DOMAIN ≥3 / note 位置 ≥3 文件 / SR 白名单 1) 对 PDF 渲染页逐格核 CT 单元格括号短名与顺序。
4. writer 的变异测试表: 自己在 scratch KB 副本上复跑至少 3 种 (含 "改错一个短名"), 确认断言 FAIL; 若某种变异断言没抓到, 判 CONDITIONAL。
5. check_links live docs 42。
输出 `evidence/checkpoints/t2_S-CT_review.md` (PASS / CONDITIONAL + 修正清单) + trace 一行 (step T2S.S-CT)。scratch `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CT_reviewer/`。只读 KB; 禁止 stash/checkout/reset/commit; xlsx/PDF 内容不进证据 (≤25 词引文)。回主控 ≤ 8 行。
