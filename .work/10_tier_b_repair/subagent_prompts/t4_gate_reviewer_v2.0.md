# T4.1 总闸独立审 brief v2.0 — attempt 2 (feature-dev:code-reviewer, 新实例)
<!-- chain: E (plans) -->
> v1.0 (attempt 1) 保留不改 (规则 B). 本次: 复判**证据层** (G-TB1..9) + 样本层延续性 + 裁定来源是否足够. 只读: 不改任何文件, 不 commit; 结果以回复正文返回, 主控原样誊入 `evidence/checkpoints/t4_gate_review.md` §attempt 2. 主控不改判 (规则 D).

## 背景 (只给事实)
- 仓库 `/Volumes/DevSSD/Project/sdtm-pedia`, 项目目录 `.work/10_tier_b_repair/`. 标签定义、PDF 路径、文本层见 `subagent_prompts/t4_gate_reviewer_v1.0.md` "背景" 节. 闸定义: `PLAN.md` §5.1 (G-TB1..9), §5.0 范围, T4.1/T4.2 行.
- attempt 1: `evidence/checkpoints/t4_gate_review.md` (样本 84/84 HOLDS; 证据层 CONDITIONAL, 原文 `evidence/t4_gate_raw/evidence_layer.md`; 缺口清单 §5).
- attempt 1 之后发生的事 (HEAD = `d3f2ea9`, 未 push):
  1. **裁定**: `evidence/checkpoints/t4_user_decisions.md` §000. 这些裁定由协调 bot「sdtm开发」在主人委托下作出 (委托原话与日期见 §000), **不是主人逐条裁定**. U-6 (T4.2 人工闸) 不在委托内.
  2. **T4.2 人工闸**: 主人本人 (经协调方转达) 把口径从 "主人判 30 条" 改为 "AI 预筛 42 条 + 主人抽查 6 条", 主人判 6/6 内容正确. 登记 `evidence/checkpoints/t4_human_verdicts.md` (含来源可核性说明); 预筛 `t4_human_prescreen.md` + `t4_human_prescreen_postthaw.md`.
  3. **解冻前只读核查**: U-5 C7 38 条全检 `t4_u5_c7_fullcheck.md`; U-7 逐行复核 `t4_u7_rowcheck.md`.
  4. **唯一一次解冻改 KB** (`a59c2d3`): 规格 `subagent_prompts/t4/t4_thaw_spec_v1.0.md`; writer `t4_thaw_W1.md` `t4_thaw_W2.md` `t4_thaw_W3.md` (W3 含主控五项决定); reviewer `t4_thaw_review.md` (KB) `t4_thaw_review_ledger.md` (台账); auditor `t4_thaw_audit.md`. 下游说明 `t4_downstream_notes.md` 末节.
  5. 确认清单 `t4_ack_lists.md` (已重生成, 含 "决定来源" 列); trace `trace.jsonl`.

## 你要判的
A. **G-TB1..G-TB9 逐条**: MET / MET_WITH_CONDITION / NOT_MET, 每条给依据 (文件:行或命令输出). 关键数要自己复算或复跑, 不采信报告:
   - ledger (`work/coverage_ledger.wc.jsonl`) 的标签计数、G-TB1 残留、G-TB2 (范围内口径 = U-3 代裁 A; 并列字面严格数)、G-TB3 四口径 (strict / mapped / **U-1 代裁 B 口径: ATOM_ERR+PDF_TYPO 算覆盖、FIG 算未覆盖** / 内容 EXACT+EQUIV), 对照 PLAN 字面 "≥ 99.02% 且不下降".
   - `python3 tools/check_links.py 2>&1 | grep "live docs"`; `bash .work/10_tier_b_repair/scripts/t3/t3_mutation.sh` (真 KB md5 前后不变); `t0_mutation.sh` 现状 (W3 称既有 MISMATCH, 核其说法).
   - G-TB4: 解冻后 census (`work/t4/census_full_thaw.json` vs `census_full_head.json`) 的变化是否都有归因 / PDF_TYPO 登记例外; attempt 1 的 "C3 剩余表无结案清单" 条件是否仍开着 (如实判).
   - G-TB8: trace 中解冻轮是否 writer / reviewer / auditor 三个不同 subagent_type; 有无主会话写 KB 的迹象 (`git log -p a59c2d3 --stat` 只能证明提交者, 如实写局限).
B. **样本层延续性**: attempt 1 的 84 条样本 (`work/t4/gate_sample.jsonl`, 包 `work/t4/gate_pack_{1..4}.md`) 是在解冻前 KB 上判的. 找出解冻后 KB 文字或 ledger 标签有变的样本 (自己写脚本比), 对这些逐条重判 HOLDS / NOT_HOLD / UNVERIFIABLE (看渲染页); 未变的注明 "沿用 attempt 1".
C. **裁定来源**: (1) 委托代裁 (§000) 是否足以作为 G-TB1 "用户 ack" 与 G-TB3 口径 "用户认可" 的记录; (2) T4.2 "预筛 42 + 主人抽查 6" 是否足以关闭 PLAN T4.2 hard 闸; (3) 人工判定的来源可核性 (仓内无主人原话独立凭证). 每项判 足够 / 不足 / 需主人确认, 写理由. 你判断不足就如实写, 这本身是交付物.
D. attempt 1 §5 列的其它缺口 (C3 结案清单、pre_existing 58 条、FIG 11 条、规则 0 抽中等): 逐条现状 (已关 / 仍开 / 不适用).

## 输出 (中文, ≤ 150 行)
1. 总结论: **PASS / CONDITIONAL / FAIL** (先定口径: 任一 G-TB NOT_MET 或任一样本 NOT_HOLD → 不 PASS; C 项任一 "不足" → 至多 CONDITIONAL, 写明还缺什么).
2. G-TB 表 `闸 | 判定 | 依据 | 条件/缺口`.
3. 样本层: 变化样本表 + 计数.
4. C 项三问的判断.
5. D 项缺口现状表.
6. 复跑命令与关键输出.
