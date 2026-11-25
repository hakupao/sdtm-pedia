# T1.3 Triage Reviewer Prompt v1.0 — subagent_type: `oh-my-claudecode:critic` (opus)

> 替代 v0.1 (保留不删, 规则 B). 变更: 100% 复核集按 PLAN T1.3 补上 RELOCATE / FIGURE / LOCATE; 共用标定集;
> 写文件改用 Bash + python (critic 无 Write/Edit); 加确定性抽样与 FAIL 规则. 每次调用复核 **1 个 lane** (或主控指定的包集合).
> 主控填: `{{LANE}}` (A-D), `{{SEED}}` (整数, 写进 checkpoint).

## 0. 边界 (规则 D)
- 你与 T1.2 writer (`oh-my-claudecode:scientist`) 是不同 agent. 只看 writer 输出与原始材料, **不要**读 writer 的推理过程或报告文字来定结论.
- **只读**, 只允许写两个文件: `.work/10_tier_b_repair/work/triage/review_lane_{{LANE}}.jsonl` (只追加) 和抽样计划 `review_lane_{{LANE}}.plan.json` (§2 脚本生成); 都用 Bash + python `json.dumps`, 不手敲 JSON.
- 不改 `knowledge_base/`, `archive/`, `releases/`, 不改 writer 的 `lane_{{LANE}}.jsonl`.
- 引 PDF 原文 ≤ 25 词 (CDISC 版权).

## 1. 输入
- writer 输出: `work/triage/lane_{{LANE}}.jsonl`; 包: `work/t1_packs/pack_*.json` (lane = `lane_{{LANE}}`).
- 真值: `work/pdf_pages/*.txt`; 原子: `work/pdf_atoms.jsonl` (只当索引); 现 KB: `knowledge_base/**`; 预筛: `work/triage_prefilter.jsonl`.
- **标定集**: `subagent_prompts/t1_calibration.md` — 与 writer 同一份. 先读完.

## 2. 复核范围 (PLAN T1.3, §5.3)
- **100%**: `REAL_GAP, VALUE_DIFF, ATOM_ERR, REWRITE_OK, RELOCATE, FIGURE, LOCATE`, 以及所有 `manual: true` 条目和 `confidence = low` 的条目.
- **20% 抽样**: `PRESENT, IE_CAND`. 抽样必须可复现:
```bash
python3 - <<'EOF'
import json, random
B = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair/work"
rows = [json.loads(l) for l in open(f"{B}/triage/lane_{{LANE}}.jsonl")]
full = [r["atom_id"] for r in rows if r["class"] not in ("PRESENT", "IE_CAND") or r["confidence"] == "low" or r["atom_id"].startswith("MANUAL")]
rest = sorted(r["atom_id"] for r in rows if r["atom_id"] not in set(full))
pool = {c: sorted(r["atom_id"] for r in rows if r["atom_id"] in set(rest) and r["class"] == c) for c in ("PRESENT", "IE_CAND")}
rnd = random.Random({{SEED}})
sample = {c: sorted(rnd.sample(v, max(1, -(-len(v) // 5)))) if v else [] for c, v in pool.items()}
print("full", len(full), {c: len(v) for c, v in sample.items()})
json.dump({"seed": {{SEED}}, "full": full, "sample": sample}, open(f"{B}/triage/review_lane_{{LANE}}.plan.json", "w"), indent=1)
EOF
```

## 3. 每条怎么复核
1. 自己从 PDF 页 + KB 重新判一次 (先不看 writer 的 class), 再对照 writer.
2. 重点 (标定集对应条):
   - REWRITE_OK: 逐信息点对 — 任何一个信息点 (限定词 / 例外 / 数值 / 适用对象) 找不到 → 改 REAL_GAP (C02-C04).
   - PRESENT: 是"同义"还是只是"相似" (C04); 位置是否 PDF 实际所属节 (C10).
   - RELOCATE: 命中是否只是 terminology / 索引类文本 (C05); 是否只是原子节号 / 目标标签错 (C10).
   - IE_CAND: 按下方 IE_CAND 规则 (与 writer 同一条) 核; spec 行看四字段是否真全一致 (C06), 非 spec 行看类别是否在 whitelist 已 ack 类别里且同质.
   - VALUE_DIFF / ATOM_ERR: 以 PDF 原页为准分清是 KB 错还是原子抽错 (C07, C08); `pdf_typo_suspect` 是否有依据.
   - `kb_loc` 行号是否真指向该内容.
3. 不同意时给 `reviewer_class` + 理由 + 你的 `kb_loc`.

**IE_CAND 规则** (writer 与 reviewer 同一条): IE_CAND 只有两种来源:
  (a) 域 Specification 表行 / 表头: 表行要 `domains/XX/spec.md` 的 name / label / type / core 全一致 (预筛 `spec_row: MATCH` 且 `match_via` ≠ `any_spec_fallback`, 再核 PDF 行; C06); 表头 (`spec_row: HEADER`) 记 `SPEC_TABLE_HEADER`.
  (b) 原子明确属于 `archive/deep_verification/intentional_exclude_whitelist.md` 里**已经用户 ack 的类别** (如 EDITORIAL_META / VERSION_MISMATCH / REDUNDANT_WITH_SPEC / CODE_LITERAL_IE / STRUCTURAL_HEADING_IE / SPEC_TABLE_HEADER / STRUCTURAL_CHAPTER_HEADING 等, 以该文件表格为准), 且与该类已 ack 的样例同质.
  `reason` 必须以 `IE类别=<类别名>` 开头. 不允许发明新类别; 想 IE 但不在已 ack 类别里 → 判其它类 (通常 REAL_GAP / REWRITE_OK), 在 `reason` 写 "建议新 IE 类别: …" 交 T1.4.

## 4. 输出
每条复核一行, 追加到 `work/triage/review_lane_{{LANE}}.jsonl`:
```json
{"atom_id": "...", "writer_class": "REWRITE_OK", "reviewer_class": "REAL_GAP", "agree": false,
 "kb_loc": "knowledge_base/...:行 或 null", "reason": "缺: …", "scope": "full|sample"}
```
写法同 writer: `python3 - <<'EOF'` 里用 dict + `json.dumps`, 已写过的 atom_id 跳过 (resume).

## 5. 判定 (写进最终报告, 主控据此写 `evidence/checkpoints/t1_review.md`)
- 一致率: 按 writer class 分列 (full 段 / sample 段分开).
- **FAIL 规则**: sample 段 (PRESENT / IE_CAND) 不一致率 > 5% → 该类在该 lane **全量重分诊**; full 段的每条不一致都由主控按你的 `reviewer_class` 裁决或发回 writer, 不自动采纳.
- 列出: 不一致清单 (atom_id, writer → reviewer, 一句理由); 你认为标定集需要补的新规则 (pattern, 不是个例).
- 最终报告 ≤ 20 行.
