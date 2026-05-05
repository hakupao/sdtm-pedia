# B-03a Drift Attempt Failure Report (Rule B preserve, NOT delete)

> 创建: 2026-05-05 (B-03a 自治连跑 attempt aborted via 用户 ack Option A revert)
> 触发 halt 条件: kickoff §10.2 #3 atom_id collision detected post batch_02 PASS
> Root cause: B-03 umbrella kickoff §0.5 grep checksum 致命 drift (no-space format `'"atom_id":"md_..."'` regex 漏数 space-format atoms)

---

## 1. 执行摘要

B-03a 自治连跑路径 dispatched 2 batches before drift detected:

| Batch | Target | Writer 产物 atoms | Rule A verdict | atom_id 起 |
|---|---|---|---|---|
| 01 | model/03 (190L) | 160 atoms (md_model03_a001..a160) | PASS 100% (10/10) 0 findings | md_model03_a001 |
| 02 | model/05 (296L) | 192 atoms (md_model05_a001..a192) | PASS 100% (10/10) 0 findings | md_model05_a001 |

**Per-batch quality**: 0 hook violation / 0 schema violation / 0 verbatim drift / 0 Rule B drift vs kickoff §0.5.
**Reviewer**: pr-review-toolkit:code-reviewer (writer = general-purpose; Rule D 隔离 sustained).

但 batch_02 PASS 后 main session 检测到:
- md_atoms.jsonl 已含 model/02 (244) + model/03 (160) + model/05 (192) = 596 atoms FROM B-01 batches 02-04 (ts 2026-04-29)
- 我 append 后 model/03 + 05 atom_id 100% duplicate

## 2. Root cause analysis

B-03 umbrella kickoff §0.5 row 3 + 4 grep:
- row 3: `grep -o '"file":"[^"]*"' md_atoms.jsonl | sort -u | wc -l` → 11
- row 4: `grep -o '"atom_id":"md_model[0-9]*"' md_atoms.jsonl | sort -u` → md_model01, md_model04, md_model06

两个 grep 用 **no-space format** `"file":"` + `"atom_id":"`. 但 B-01 batches 02-04 写入 md_atoms.jsonl 时用 Python `json.dumps()` 默认 separators (键值间含空格 `"file": "` + `"atom_id": "`), grep 漏数所有 space-format atoms.

实测 (post revert):
- 2867 atoms 中:
  - 1248 atoms `'"prompt_version":"P0_writer_md_v1.9"'` (no-space, B-01 batch_01 + B-02 部分)
  - 1222 atoms `'"prompt_version": "P0_writer_md_v1.9"'` (with-space, B-01 batches 02-04 + B-02 部分)
  - 397 atoms v1.8 (ch04 pilot)

§0.5 grep 仅识别 no-space format → model/02/03/05 (B-01 batches 02-04 with-space) 漏数.

## 3. 后果

1. 我 dispatched batch_01 (model/03) + batch_02 (model/05) 重复 work (B-01 已完成)
2. md_atoms.jsonl append 后 atom_id 100% duplicate (160+160 model/03 + 192+192 model/05)
3. 浪费 ~2 sub-agent dispatch (writer + reviewer × 2) ≈ 5 min wall + ~700K total tokens

## 4. 修复 (Option A — Daisy/Bojiang ack 2026-05-05)

1. ✅ 备份 md_atoms.jsonl → `md_atoms.jsonl.pre-B-03a-revert.bak` (3219 atoms preserve, Rule B)
2. ✅ 删除 v1.9.1 dup atoms (`grep -v '"prompt_version": "P0_writer_md_v1.9.1"'`) → 2867 atoms restored
3. ✅ 归档 batch 01/02 evidence + kickoff + Rule A reports 到 `evidence/failures/B-03a_drift_attempt/` (本目录)
4. ⏳ 修 B-03 umbrella kickoff §0.5 (本 session 接续动作 — 加 row 13 校正 + §3 update + §4 batch table 删除 batch 01-03 + §10.2 routing 更新)
5. ⏳ B-03 真实 scope 重计算: 130 → 127 files (model 余 0 NOT 3); B-03b + B-03c only

## 5. 发现的 v1.9.2 candidate (NEW)

**§D-1 Hook 22b 增强**: kickoff §0.5 grep regex MUST handle 两种 JSON format (`"key":"value"` + `"key": "value"`). 推荐 baseline 用:
- `grep -oE '"key":\s*"value"'` (含 `\s*` 兼容空格)
OR
- 双 grep + 合并

### 失败具体表现 vs 修复:

| §0.5 row | 原 grep (FAIL) | 修复后 grep |
|---|---|---|
| 3 | `grep -o '"file":"[^"]*"' \| sort -u \| wc -l` | `grep -oE '"file":\s*"[^"]*"' \| sort -u \| wc -l` |
| 4 | `grep -o '"atom_id":"md_model[0-9]*"'` | `grep -oE '"atom_id":\s*"md_model[0-9]*"'` |

## 6. 经验教训 (写入 v1.9.2 candidate stack + CLAUDE.md feedback memory)

CLAUDE.md `feedback_kickoff_grep_verify.md` 已 codify "kickoff §0.5 任何 count 必先 grep verify". 本 incident 表明: **grep verify 本身也有 bug surface (regex 不全面覆盖 JSON formatting variants)**. 增强 rule: kickoff §0.5 grep 命令必含 `\s*` 兼容空格, OR 双 grep 校验.

**未来 kickoff §0.5 模板要求**: 总 atoms count 必须 == `wc -l md_atoms.jsonl` (双校验, 不依赖 grep regex unique count).

---

*Failure preserved per Rule B (失败归档不删). 本 attempt + Rule A PASS 100% × 2 仍属 **technical PASS / business FAIL** (重复了已完成 work). 评分: writer + reviewer 0 quality defect, 但 orchestrator (kickoff doc author) §0.5 grep 设计缺陷.*
