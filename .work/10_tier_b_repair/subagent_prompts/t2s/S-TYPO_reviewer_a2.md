批次 S-TYPO (T2-post 全库排版字符脚本批), attempt 2 (写入). 角色: reviewer.
工作目录 repo 根 `/Volumes/DevSSD/Project/sdtm-pedia`。读: `.work/10_tier_b_repair/subagent_prompts/t2s_scan_review_audit_v1.0.md` Reviewer 段 (按脚本批适配), `evidence/checkpoints/t2_post_user_ack.md` (U1/U4), `HANDOFF.md` 下一步第 2-3 条, writer 报告 `evidence/checkpoints/t2_S-TYPO_dryrun.md` + `t2_S-TYPO.md`, `work/t2_batches/S-TYPO.{plan,fixed,residual,writer}.jsonl`, `work/t2_pdf_typo_registry.jsonl`。改动未提交: `git diff HEAD -- knowledge_base/` (51 文件 154 行 356 处)。
主控裁定: registry span 不动 (含 B-IS T-6/B-TA T-4/B-MK T-1); ch04 两处 `--`→`–` + 一处 U+2212→`-` 并入 (已批, writer 已改); CRF 符号全部移出 (交 T4); 13 行多命中不一致不改; ch08 粗体伪标题移出; 标题行不动。
你的任务 (独立, 不信 writer):
1. 读 `scripts/t2s/typo_assert.py`, 找盲区。**自己写**独立校验 (不 import writer 代码): 对每个改动文件与 `git show HEAD:<f>` 逐行比, 断言 (a) 每个改动行去掉闭表字符替换后与原行逐字相同、无非空白字符增删; (b) 无标题行 / 代码 / URL / `--VAR` / registry span (按 kb_file + 片段全部出现位置) 被改; (c) 改动文件 ⊆ chapters/domains/model; (d) spec.md 的 `(SHORT) Cxxxx` / DOMAIN 值未变。
2. **方向正确性**: 抽 ≥ 30 处替换 (按类分层: dq 开/闭 ≥10、sq ≥6、em 空格 ≥4、dash ≥4、… ≥2、¹ ≥2、ch04 3 处全核) 对 PDF 渲染页核目标字形 (开/闭引号方向尤其要看: 撇号 vs 右单引号、行首引号)。
3. 在 scratch KB 副本复跑至少 4 种变异 (含 "开引号写成闭引号" 与 "改 registry span"), 断言须 FAIL; 若漏 → CONDITIONAL。
4. check_links live docs 42。
输出 `evidence/checkpoints/t2_S-TYPO_review.md` (PASS / CONDITIONAL+修正清单) + trace 一行 (step T2S.S-TYPO)。scratch `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TYPO_reviewer/`。只读 KB; 禁止 stash/checkout/reset/commit。回主控 ≤ 8 行。
