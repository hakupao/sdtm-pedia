# C2R N5 卡片层接地闸 — 回扫验证 attempt 1 FAIL (2026-09-14)

> 归档理由: 规则 B。PLAN §10「闸回扫」两判据: 召回 **PASS** (已知真阳性 1/1, 另抓 1 条预登记外真阳性); 假阳性**字面口径 7 > 5 = FAIL**。判据未改。
> 判分: `evidence/step_c2r_n5_scan_audit.md` (独立 judge); 真值 gitignored `data/study/st01/eval/runs/c2r_n5_scan_audit_detail.md`。

## 输入
- 闸 `scripts/study/c2r_eval/check_card_grounding.py` (复审后版本; 复审条件 PASS: 3 MAJOR 修毕, 8 条规则留一消融真阳性全部存活, 变异 11 杀 9)。验证集 = 全部 c2r run 5 目录 56 份 289 单元, 零 LLM。
- 闸的演化 (写进这里是为了让「对症下药」可审): 首跑标红 61 → 六条 pattern 级规则 (form OID 不当实体 / 兄弟卡片项目 = 文书名 / 括注内严格边界 / 题面+附页文本层入文脈 / 『頁索引』切分 / 否定同小句) → 9。每条规则的消融数据在复审报告 (checkpoint §2)。

## 产物
| 类 | 计数 |
|---|---|
| SOURCE_GROUNDED / SIBLING_NAMED | 201 / 16 |
| CONTEXT_MISCITED (标红) | **9** |
| UNGROUNDED / BAD_SOURCE | 0 / 0 |
| NEGATED / NO_ENTITY | 6 / 57 |

标红 9 条 judge 逐条核: 真阳性 2 (已知 1 + 新 1: 被引卡「30 个随访活动全非表示」被推广到另两个项目组, 真值 28/30 显示, 反证在同 run 上下文且被同答案上文引过) / **CITATION_ERROR 3** (主张真, 出典挂错; 真源都在文脈) / 纯假阳性 4 (跨语料比对句 1, 位置指称 1, 单元切分吞画面句 2)。

## 技术判定
- 召回: 1/1 PASS; 新真阳性与已知同型不同壳 (卡片层过度推广), 闸第一轮就抓到预登记外的一条。
- NEGATED 6/6 核真; SOURCE_GROUNDED 随机 10/10 (seed 20260914) 核真, 本次抽样无漏网。
- 假阳性: 字面口径 (「被闸标而核验为真」) = 3 + 4 = **7 > 5**。窄口径 (整类排除 CITATION_ERROR) = 4 ≤ 5。**翻转只能靠整类排除, 不能靠个别归类**。

## 业务判定 (FAIL)
- 按预登记字面 FAIL。CITATION_ERROR 是否算假阳性是 PLAN 所有者的裁定 (用户), 不由 writer/judge 决定; 裁定前本单元的闸验证状态 = FAIL。
- 2 条「单元切分吞画面句」是机械缺口: 「画面では…」句无画面出典标记, 被并入后面的卡片出典单元。属可修 pattern (画面句以「画面では / 画面上」等开头且无出典 → 不归卡片单元), 但**本轮不改** (改了要重新判); 留给 attempt 2 预登记。

## 下一 attempt 输入
1. 用户裁定 CITATION_ERROR 口径 (计入 / 不计入 / 单列报告不计预算)。
2. 若需 attempt 2: 预登记「画面句不归卡片单元」规则 + 复扫 + judge 只核 delta。
3. 闸的判别力边界 (judge §6): 只在「OID 不在被引文件」一维有效; 「OID 在被引卡里但关系说反」零样本, 漏检率不可测 —— 写进 checkpoint 诚实边界, 不当作已覆盖。
