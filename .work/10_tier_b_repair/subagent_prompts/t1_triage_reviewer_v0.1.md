# T1 Triage Reviewer Prompt v0.1 (DRAFT) — subagent_type: oh-my-claudecode:critic

## 任务
独立复核分诊结果 `{{triage_output_path}}`. 你与分诊 writer 是不同 agent, 只看其输出与原始材料 (PDF 原页 + KB).

## 范围
- REAL_GAP / VALUE_DIFF / ATOM_ERR / REWRITE_OK: **100% 复核**
- PRESENT / IE_CAND: 按种子 `{{seed}}` 随机抽 20%
- 重点: REWRITE_OK 是否真的无信息丢失 (逐信息点对); PRESENT 是否只是"相似"而非"同义"

## 输出
- 每条复核: `{"atom_id", "writer_class", "reviewer_class", "agree": bool, "reason"}`
- 汇总: 一致率 (按 class); 抽检段不一致率 > 5% → 该包整体 FAIL, 全量重分诊
- 不要修改任何文件.
