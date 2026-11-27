# T4 解冻轮 KB diff 独立复核 (reviewer)
<!-- chain: E (plans) -->
> 状态: **PASS** (2026-11-27). 审查者 `oh-my-claudecode:code-reviewer` (opus), 只读; 主控原样誊录回复要点 (未改判, 规则 D). 被审 = 工作树相对 HEAD `3a24a1c` 的 knowledge_base/ 全部改动 + registry / S-TYPO.fixed / out_of_scope 改动. 复核产物 `work/scratch/t4/review/` (gitignored).
> 审查者自报: 曾误把一个临时脚本复制进 `scripts/t2s/`, 几秒内删除, `git status -- scripts` 为空.

## 结论: PASS
26 个 KB 文件全部 hunk 归入规格条目, 规格外 KB 改动 0; 核过的改后值都与 PDF 渲染页 / rowcheck 单值依据一致; 规格要求不改的位置均未改; 下游约束保持 (model 6 格行只新增 TS 三行, 另两行改动属 A5-4/A5-7 授权); 两个门禁 FAIL 经复现属结构性. 问题 6 条均 LOW.

## 问题表
| # | 严重度 | 文件:行 | 问题 | 建议 |
|---|---|---|---|---|
| 1 | LOW | `work/t2_batches/S-TYPO.fixed.jsonl` (+58) | 58 个 CRF 位置追加进 typo_assert 放行清单 (符合 S-TYPO 机制, typo_assert.py:5/107 读此清单), 规格未明写; CRF 计划由 scratch 脚本生成, 未走 typo_plan.py | 主控追认 |
| 2 | LOW | `knowledge_base/model/06_relationship_datasets.md:191` | KB 自写 Summary 表 (有 D6) 仍写 "AP Related Subjects", 与改后 6.6 标题 "Associated Persons Relationships" (sv20 p68) 不一致 | 后续, 记 O 号 |
| 3 | LOW | `knowledge_base/domains/PP/examples.md:110/112` | 原斜体指针与新交叉引用都指向 PC examples, 重复 (W2 已登记 O65) | 后续合并 |
| 4 | LOW | 改成 `> Note:` 的 5 行 (EX:5、MS:3、PC:3、PP:3、RELREC:5) | 不再走 t3_reverse_trace KB_NOTE 豁免与 typo 不动区; W3 预计多 5 行 NOPDF | W3 逐条列原因, 不算回归 |
| 5 | LOW | `domains/MS/examples.md:3`、`domains/PC/examples.md:3` | 除位置说明外带组织性描述, 边界分类, 按 "只说明来源/位置" 判仍成立 | 可接受 |
| 6 | LOW | rag `defhome_rules` R4n 列 | TS 加第 6 列后空 Notes 的 6 行 (TSSEQ/TSGRPID/TSPARMCD/TSPARM/TSVAL/TSVALNF) 在 R4n 下计入; rag 采用的 R4 只加 3 行 | downstream notes 注明, 提醒 rag 勿改用 R4n |

## 必做项摘要 (审查者原述压缩)
1. diff 记账: U-7 21 行 (A1 2 / A2 11 / A3 8)、A6 2、CRF 58、A5-1..11/13/14、U-10② (CE:39); 规格外 KB 改动 0. 不改项确认未改: A2-12 (TR/spec:264)、A3-24 (DS:345-346, TE:43)、A3-28 (ch10:386)、A3-31/32 (SE/SM spec:39)、A5-12、A5-15、B-MK T-1 (MK:53/62)、ML `[X]`/`[ ]`、全部 Mermaid 块.
2. U-7 + A6: 21 行旧值在文本层逐个找到, p165/p280/p281/p419 + A6 p239/p391 看渲染页; 改后值 = rowcheck 精确改法, 副本 PC:285/:300/:334、TS:48/:50 都改; A2-16 = "PC records with PCGRPID"; 全库旧串 grep 0. IS 3 格 "AUREUS–EPITOPE X" (p239 en dash); TA:351 "5 mg - 10 mg – Placebo" (p391 仅第二处 en dash).
3. CRF: CE p152 ○18, p153 ○15 □6 (=39); ch04 p32 坏字形 3 + ○6, p33 ○10 (=19); 合计 58 = 计划 58 行; 渲染逐一一致.
4. A5: model/05 15 个标题 (sv20 p51-69) 与 6/6.1-6.7 标题一致; TI p415、TA p382/p384、FA §6.4.4 p364、MB p256、SS p344 一致; TT/TP 列名与 note (p54-55)、TS 第 6 列 (p59-60)、APID 补句 (p64 逐字)、USUBJID/POOLID PDF Notes 确空 (p64-65)、QLABEL Qualified=QNAM (p66). 改/删标题入站链接 (knowledge_base web/src tools docs) 命中 0; 新锚点 PC/examples.md:60 与 ch08 `831-relrec-dataset-relationship-example` 存在; A5-8 删 KB 自写表, A5-10 删除段内容在 PC/examples.md:68-147, 无 PDF 内容丢失.
5. A5-14: 5 条改 `> Note:` 均只说来源/位置; D6 170 → 165 (−2 随删除段, +2 新增, −5 改前缀); 保留前缀抽 ≥25 条分类合理.
6. 下游: defhome_rules HEAD 副本 vs 工作树: R0 64→67, R4 72→75, 新增只有 TSVALCD/TSVCDREF/TSVCDVER; spec.md 未改, Controlled Terms 行不变; model `#` 未变.
7. 门禁: `typo_assert --plan` FAIL 86 条 (tree≠HEAD+plan 25 / registry span 24 / 字母改动 23 / 标题 6 / kbnote 4 / 行数 4), 每条对到 U-7/A6/W2 结构改动, CRF 违规 0 → "只容排版字符故必然 FAIL" 成立. `ct_assert` 在 HEAD 副本即 exit 1 (期望计数写死), 现多 25 条 "非 spec.md 文件与 HEAD 不同", notes 59 不变 → 成立. check_links live docs 42.

## 规格外改动
- KB 内: 无.
- KB 外 (主控追认): `S-TYPO.fixed.jsonl` +58; registry B-PCPP T-6 span 2→1 (A5-10 连带); out_of_scope O63-O66 (规格 §2.15 授权).

## 主控追认 (2026-11-27)
- 问题 #1 追认: S-TYPO.fixed 追加 58 行 (append-only, 原 7 行未动) 与 scratch 生成 CRF 计划 (typo_plan.py 规划模式会覆盖 S-TYPO fixed/residual), 接受. 门禁替代证明 = W1 拆分验证 (只放 CRF 时 PASS / 撤回 32 处后 PASS) + 本 reviewer 逐条归因.
- 问题 #2/#3 登记后续 (O67 / O65); #4 交 W3; #6 写入 downstream notes.
- W2 (b) TT/TP DOMAIN 格挂在 Usage Restrictions 列下 (note 写明例外): 清空会改 rag 所读内容, 本次保留, 记后续.
