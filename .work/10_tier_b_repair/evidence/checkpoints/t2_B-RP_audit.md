# T2 B-RP auditor — attempt 1 (oh-my-claudecode:verifier, opus, 2026-11-26)

## 抽样 (Rule A)
- 命令: `subagent_prompts/t2_auditor_v1.0.md` 抽样脚本原样, 仅加一行 `J["pdf_pages"] = [305, 306, 307]` (dispatch: P = RP 全节页 p305-307); 输出 `scratchpad/t2_B-RP_auditor/sample.json`
- seed=20261126; C=1, P=11, N=10 (=max(10, ceil(0.2×1)), ≤|P|); C 抽 1 + P−C 抽 9 (含 OE 对照 2 条)

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0305_a013 (C) | p305:19 RP Description/Overview 句 "A findings domain that contains physiological and morphological findings…" | RP/assumptions.md:5 | 否 | 是 (逐字) | 是 (`## RP – Description/Overview`, 位于 Specification 前, 同 PDF 顺序) | 本批新增 |
| 2 | ig34_p0307_a001 | p307:1 Assumption 3a, RP Codetable + CT URL | RP/assumptions.md:18 | 否 | 是 (含 URL) | 是 (3 的子项 a) | |
| 3 | ig34_p0305_a001 | p305:1 OE: ocular comfort 数值量表见 supp qualifier | OE/examples.md:147 | 否 | 是 | 是 | 对照, kb_files 外 |
| 4 | ig34_p0305_a005 | p305:6 OE: 眼部 AE 入 AE 域, 单眼事件用 FOCID | OE/examples.md:155 | 否 | 是 | 是 | 对照, kb_files 外 |
| 5 | ig34_p0306_a026 | p306:51 Assumption 3, RP tests/responses/units 分 codelist | RP/assumptions.md:17 | 否 | 是 | 是 | |
| 6 | ig34_p0305_a015 | p305:21 spec 首句 rp.xpt…One record per finding…per subject, Tabulation | RP/assumptions.md:9 | 否 | 是 (逐字) | 是 (Description 与 Assumptions 之间, 合 CM/IS 先例) | |
| 7 | ig34_p0306_a025 | p306:50 Assumption 2, 生殖相关用药入 CM; see Section 6.1.2 | RP/assumptions.md:15 | 否 | 是 (含交叉引用) | 是 | |
| 8 | ig34_p0307_a005 | p307:6 Example 1 引导句 (screening/visit 1/visit 2, 2 subjects) | RP/examples.md:5 | 否 | 是 | 是 | |
| 9 | ig34_p0306_a024 | p306:48 Assumption 1, 生殖能力/生殖史 (e.g. 3 例) | RP/assumptions.md:13 | 否 | 是 (仅 ’→' 字形) | 是 | |
| 10 | ig34_p0306_a022 | p306:42 spec 表脚注 "In this column, an asterisk (*)…" | 无 (RP/spec.md 缺) | 范围外 | — | — | 归属 spec.md (不在 kb_files); 全库 domains/*/spec.md 0/64 含此脚注 → 已登记 O26 (并 O15/O24), 不计本批 |

- 本批独有丢失: **0**; 忠实度错误: **0**; 范围外发现 1 (a022, 已有 O26, 不新增)
- 反向 (KB→PDF): RP/assumptions.md 全 20 行、examples.md 全 31 行均有 PDF 出处, 无 KB 自写扩写.

## Ex1 rp.xpt 渲染格核 (p307, pdftoppm -r 150, seed 20261126)
抽 4/7 RPDTC 修正格 + 6 随机格, 全对:
r16 RPDTC 2009-03-09 ✓; r19 RPDTC 2009-03-09 ✓; r11 RPDTC 2008-04-16 ✓; r17 RPDTC 2009-03-09 ✓; r9 RPTEST "Pregnant During the Study" ✓; r10 RPTESTCD CHILDPOT ✓; r19 RPORRES N ✓; r7 RPORRESU 空 ✓; r19 USUBJID 2324-P0002 ✓; r18 RPDY -10 ✓ → 10/10

## 其他
- KB diff `git diff f22fe60 -- knowledge_base/domains/RP/`: assumptions +4 行 (Description 节), examples 7 格 RPDTC; 无其他改动.
- fp 隔离: `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl; grep -cE 'p030[5-7]|RP/' $S/fp_regress.jsonl` → 0 (全局 RED 来自他批 §6.4.2 未提交改动)
- `python3 tools/check_links.py` → live docs 42 (不升)
- G-TB8: trace 有 writer executor (L176, L178 续) + reviewer code-reviewer PASS (L182, 03:31:15Z); 无 `agent: main` 写 RP. mtime: examples.md 03:27:02Z, assumptions.md 03:28:45Z, 均早于 reviewer PASS → reviewer PASS 后无 writer 改动. **OK**

## 结论: **PASS**
