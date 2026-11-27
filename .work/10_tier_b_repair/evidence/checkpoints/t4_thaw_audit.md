# T4 解冻轮 独立 auditor
<!-- chain: E (plans) -->
> 状态: **PASS** (2026-11-27). 审查者 `oh-my-claudecode:verifier` (opus), 只读; 主控誊录要点, 未改判. 复核产物 `work/scratch/t4/audit/` (kb.diff / sample.py / mech.py / mmd/).

## 结论
KB 样本 30/30 成立 (无内容与 PDF 不符、无 PDF 内容丢失); 台账样本 15/15 成立; 机械核 (a)-(f) 全过; 规格外改动 1 组 (U-6 人工闸记录文件, 不涉及 KB / 台账), 交主控追认 / 总闸判断.

## 抽样 (N 先定)
- `git diff HEAD -U0 -- knowledge_base` 72 hunk, `random.seed(20261128)`; 分层: CRF 8 hunk / 前缀 5 / A5 结构 33 / 值改 26 → 抽 值 10 / CRF 6 / A5 10 / 前缀 4. 台账: 58 个标签/规则变化 id 抽 15.
- KB 30 条: 值 10 (ch02:176、ch04:863、DS/ex:87、NV/as:23、NV/ex:63、PC/ex:284-285、SM/ex:7、TA/ex:351、TS/as:50、TS/as:57) / CRF 6 (ch04:410-412 p32、:472-476 p33、:506-510 p33、CE:43-46 p152、CE:74、CE:79-83 p153) / A5 10 (FA/as:95-97 p364、PP/ex:112、TI/as:3 p415、model/05:97 sv20 p54、:140、:158 sv20 p56、:215 TS 第 6 列 sv20 p59-60、model/06:33 sv20 p64-65、:75 QLABEL sv20 p66、:138 6.5 sv20 p68) / 前缀 4 (MS:3、PC:3、PP:3、RELREC/as:5) — 全部 ✓.
- 台账 15 条: p0016_a019、p0056_a006 (U-2)、p0153_a0006/0007/0018、p0190_a017、p0275_a019、p0277_a020/a023、p0278_a034/a040、p0280_a040、p0281_a032、p0298_a001、p0362_a010 — 全部 ✓.

## 问题
| # | 严重度 | 位置 | 问题 | 建议 |
|--:|---|---|---|---|
| 1 | MEDIUM (规格外) | `t4_human_sample.md` / `scripts/t4/t4_human_header.md` 状态行、新增 `t4_human_verdicts.md`、`t4_human_prescreen_postthaw.md` | U-6 人工闸记录, 不属 thaw 规格 §1-§3; 授权来源只有文件自述, 仓内无可核原话; 不涉及 KB/台账 | 主控追认或拆提交; 授权是否足够由总闸 attempt 2 判断 |
| 2 | LOW | ledger p0153 14 行 | evidence 出处仍写 T2 rework, 实为 T4 CRF (同 reviewer-L #1) | 后续 |
| 3 | LOW | `model/06:191` | "AP Related Subjects" 与 6.6 标题不一致 (O67) | 后续 |
| 4 | 说明 | p0362_a010 | K4 口径 ATOM_ERR / K3b(b) 口径 PDF_TYPO; 现状 = 主控决定 2 | 不阻塞 |

## 机械核
- (a) 不改位置全未改: 改动 25 文件不含 TR/spec、TE、SE/SM spec、ch10、ch08、MK、ML; DS/ex 只改 87/294/298; ML 0 行; 改动文件内 31 个 Mermaid 块与 HEAD 逐字相同.
- (b) spec.md 0 改动 (Controlled Terms 0); model/05 110 行、model/06 47 行 `#` 列与 HEAD 逐行相同.
- (c) 29 个旧标题 slug 入站链接 0 (MB/ex `#example-1~3` 仍在); 新锚点 PC `63593-…--worked-examples`、ch08 `831-relrec-dataset-relationship-example` 存在.
- (d) `broken relative links: 18668 (live docs: 42)`.
- (e) `mermaid blocks OK 42 FAIL 0`.
- (f) defhome: R0 64→67, R4 72→75; R4 只新增 TSVALCD/TSVCDREF/TSVCDVER (→05), 删 0 改 0.
- 台账 md5 `60729f7b64b7c1dfaf2174e394f6dd9c`; 12492 行 (11 个 atom_id 重复, HEAD 既有); 58 标签变化 + 20 仅指针. 四口径自算: strict 9567/9986 = 95.8041% / mapped 9567/9629 = 99.3561% / U-1 B 9913/9986 = 99.2690% / 内容 8733/9629 = 90.6948%.
- CRF: 新增 ○/□ CE 39 + ch04 19 = 58, 删 `( )`/`[ ]` 58, 计划 58 行. registry 270→272.
- 证据 md 链接: 未包反引号的 6 个均在代码块内 (check_links 跳过).

## 主控追认 (2026-11-27)
- 问题 #1: U-6 文件属协调方 2026-11-27 转达的主人决定 (orca 消息 "主人已判 6 条抽查都对；T4.2 的登记方式和解冻后核对", 协调方称主人在待办项上本人选择, 非 bot 代裁). 主控据该消息登记, **仓内无主人原话的独立凭证** —— 已在 `t4_human_verdicts.md` 写明, 交总闸 attempt 2 判断. 与解冻轮同一提交 (只涉记录文件).
