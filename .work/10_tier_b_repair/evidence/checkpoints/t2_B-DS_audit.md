# T2 B-DS auditor 报告 (Rule A 独立抽检)

## attempt 1
- agent: oh-my-claudecode:verifier (opus); 2026-11-26; KB 基线 `git diff c3b7b56 -- knowledge_base/domains/DS/` (仅 examples.md, +55/-55)
- 先独立判 (PDF 文本 + 渲染页), 判完才对照 writer checkpoint 的 N-/D-/T- 编号.

### 抽样
- 命令: `t2_auditor_v1.0.md` §抽样 脚本原样 (b=B-DS, seed=20261126), 输出 scratch `t2_B-DS_auditor/sample.json`
- 结果: C=0 (本批 atoms/t2_recheck 为空), P=51, N=10 (全部取自 P−C 对照)
- 补抽 (主控指示): 改动叙述 N-1..N-12 全部 12 组逐句核; 另对 p158-167 DS 节全部 106 个 prose 原子做全量规范化子串 + 顺序/所属 Example 校验 (`chk.py`/`order.py`), 并反向把 KB 每句 prose 对 PDF p158-167 原文 (反查 KB 自写/改写).

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---------|------------------|--------------|-------|-------|-------|------|
| 1 | ig34_p0163_a0019 | 163 Ex10 TE 说明 Row 6: follow-up element | DS/examples.md:222 | 否 | 是 | 是 (Ex10 te 前) | 逐字 |
| 2 | ig34_p0163_a0017 | 163 Ex10 Rows 2, 3: DRUG1/DRUG2 元素, 首治疗 epoch | :218 | 否 | 是 | 是 | 逐字 |
| 3 | ig34_p0159_a0027 | 159 Ex2 EPOCH 作为 timing 变量, 表示终止所在 epoch | :49 | 否 | 是 | 是 | 逐字 |
| 4 | ig34_p0166_a0007 | 166 Ex11 "TA dataset shows the trial design" | :349 | 否 | 是 | 是 (ta.xpt 前) | 逐字 |
| 5 | ig34_p0166_a0010 | 166 Ex11 ABC arm 弃 C 后转 AB 或 follow-up (N-9 改动) | :349 | 否 | 是 | 是 | 写手补回, 逐字 |
| 6 | ig34_p0161_a0004 | 161 Ex4 DS/AE 关系在 RELREC | :105 | 否 | 是 | 是 (ae 后 relrec 前) | 逐字 |
| 7 | ig34_p0162_a0018 | 162 Ex8 盲法双药研究导语 3 句 | :173 | 否 | 是 | 是 | 逐字 |
| 8 | ig34_p0162_a0020 | 162 Ex8 Rows 3, 6: 每治疗 epoch 的研究参与处置 | :177 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0166_a0008 | 166 Ex11 screening 元素从 0 编号 | :349 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0162_a0001 | 162 Ex6 Row 3: 最终研究完成 (STUDY PARTICIPATION) | :144 | 否 | 是 | 是 (Ex6) | 逐字 |

补抽 N-1..N-12 (改动集): :15 / :87 / :89 / :122 / :175 / :307 / :313 / :336 / :349 / :371 / :393 / :395+:399 — 12 组全部与 PDF p158/160/161/162/165/166/167 逐字一致且位于 PDF 所属 Example/Row (N-10 段已在 ta.xpt 后; N-12 三句已归 Row 6, "follow-up epoch" 照 PDF).
全量扫: 106 原子中 101 规范化后逐字命中且顺序单调、所属 Example 与 PDF 一致; 未命中 5 = p158_a0001-a0004 (DS assumptions 5-6, 属 `DS/assumptions.md`:35-41, 非本批文件, 已在) + p161_a0012 (原子抽取把 DSSCAT 误录成 DSCAT; 渲染页为 DSSCAT, KB :120 与 PDF 一致, 原子错非 KB 错). 反向扫: KB prose 不在 PDF 的句子只有登记的 T-3 (:89 DSSTDTC)、T-4 (:120 epoch)、T-6 (:241 DG2INDG)、T-5 (:377 received), 均为 PDF 印刷错的合理更正 (依据见 writer T 表), 无 KB 自写扩写.

- **独有信息丢失: 0**; **忠实度错误: 0**; 位置错误: 0.

### 表格 10 随机改动格 (seed 20261126, 从 diff 47 条格级改动抽; 对 pdftoppm -r110 渲染页目视)
| KB 行 | 格 | 改后值 | PDF 渲染 | 结果 |
|---|---|---|---|---|
| :31 | Ex1 r7 DSSTDTC | 2003-11-20 | p159 r7 2003-11-20 | OK |
| :37 | Ex1 r13 DSSEQ | 3 | p159 r13 3 | OK |
| :38 | Ex1 r14 DSSEQ | 2 | p159 r14 2 | OK |
| :231 | Ex10 te r4 TESTRL 句点 | "...with Drug 1." | p163 r4 带句点 | OK |
| :294 | Ex10 se r1 整行 (补 ELEMENT 列) | SCREEN/Screen/02-02/02-14 | p165 r1 | OK |
| :296 | Ex10 se r3 整行 | DG1INDG/Drug 1 + Investigational Drug/03-14/04-24 | p165 r3 | OK |
| :322 | Ex10 ds r4 DSSTDTC | 2016-03-14 | p165 r4 | OK |
| :327 | Ex10 ds r9 DSSTDTC | 2016-02-20 | p165 r9 | OK |
| :385 | Ex11 se r3 SEUPDES 空 / TAETORD 2 | 列移位修正 | p166 r3 | OK |
| :386 | Ex11 se r4 SEUPDES 空 / TAETORD 6 | 列移位修正 | p166 r4 | OK |
另: :292 表头 SESEQ (PDF SDSEQ, T-1) 与 :346 "is AB +C" (PDF 无 is, T-2) 为登记 PDF_TYPO, 按 dispatch notes 取舍规则 (同文件 Ex11 se 表头 / 同表 r2 平行句) 可由 PDF 自身确定, 不计忠实度错误.

### D-1..D-5 删除核对
diff 中被删的 prose 只有: D-1 拼接句 (AB 句头 + ABC 句尾), D-2 错句 "A and B stopped after cycle 2 due to toxicity" (PDF: C 在 cycle 2 停 / A+B 在 cycle 3 因进展停, 已原位补全), D-3 Row 4 尾部 3 句 (已移至 Row 6, PDF 所属), D-4 乱序句 (PDF 原文已替换), D-5 "and AE record is represented" (恢复 PDF "and in the AE record was represented"). 每条删除内容的 PDF 对应信息均在 KB 现存 (全量扫 101/101 命中佐证), **未删除任何 PDF 支撑内容**.

### G-TB8
trace `T2.B-DS`: writer `oh-my-claudecode:executor` subagent_done ✓; reviewer `oh-my-claudecode:code-reviewer` subagent_done PASS ✓; 无 `agent: main` 写 KB 记录 ✓.

### 结论: **PASS** (丢失 0 / 忠实 0; 10 格 0 错; D-1..D-5 无误删)
- 范围外观察: 无 (p161_a0012 原子文本 DSCAT 为 P0 抽取错, 建议台账侧修正, 不影响 KB).
