# T2 B-EC reviewer — attempt 1

> reviewer: oh-my-claudecode:code-reviewer (opus), 独立于 writer. base f22fe60 (HEAD 7a2f326 不含 EC/EX 改动). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-EC_reviewer/`

**Verdict: PASS**

## 命令 / 关键输出 (可复跑, 工作目录 repo 根, S=上述 scratch)
- md5 (与 writer 报告一致): EC/examples `10c53276…`, EC/assumptions `35046d35…`, EX/examples `33e7ebcb…`
- `git diff HEAD --stat -- knowledge_base/`: 本批只有 EC/assumptions +10, EC/examples 1+/133-, EX/examples 1+/1-; 其余 (RP/TA/TU/VS) 属他批并行未提交, 非本批.
- D2 逐行: `git show f22fe60:knowledge_base/domains/EC/examples.md` 每个非空行 strip 后查是否在现 EX/examples.md 行集合 → **24 行不在 EX** (writer 写 22, 少数了 2 条表分隔线 :33/:109; 内容判定不受影响). 其余 EC 行在 EX 逐字存在.
- table_census (manifest EC/examples p107-120): `KB tables: 0; status: {}` (EC 已无表, 跳过; PDF_ONLY 为全局列表). 补跑 EX/examples p111-120: `status {'UNPARSEABLE': 11, 'OK': 19, 'DIFF': 1}; diffs 3` = B-EX review 已登记 T-1 (relrec Row 号), 与 B-EX 一致 → 保留副本未变坏.
- fp 隔离: kbA = 工作树 KB 但 3 个本批文件回退 HEAD; kbB = 工作树 KB. `fp_match.py --kb-root $S/kbX --baseline work/fp_baseline.jsonl` 两边 exit 1, regress 各 48 条且集合完全相同 (A-only/B-only 空); verdict 变化 0; lost hit_target 0 / lost hit_any 0; 43 条 p111-119 原子 hit_target 由 EC→EX (预期, 仍命中) → **EC+EX 回归 0**.
- `python3 -I tools/check_links.py` → `broken relative links: 18668 (live docs: 42)` (= 基线 42).

## (1) D2 去重 — 24 条 EC-only 行逐条对 PDF

| EC 行 (base) | 内容 | 判定 | 证据 (PDF 页) |
|---|---|---|---|
| 1 | `# EC — Examples` | 结构, 保留未动 | — |
| 3 | "Note: Examples for EX and EC are shared…" | KB 导航, 被新交叉引用取代 | — |
| 32-33 | Ex2 ec.xpt 表头/分隔 (无 VISITNUM) | EC 错 | p112 表头 "…ECLAT VISITNUM VISIT EPOCH…"; EX:86 有 VISITNUM |
| 34-36 | Ex2 3 行 (缺 VISITNUM=3) | EC 错 | p112 行 1/2 "LEFT 3 VISIT 3", "CENTER 3"; EX:88-90 |
| 40 | Ex3 首段缺尾句 | EC 截断 | p113 l9 "The subject in this example took:"; EX:111 全 |
| 59 | Ex5 段缺尾句 | EC 截断 | p114 l33 "This use of time-point variables is novel…"; EX:192 全 |
| 87 | Ex6 Row2 ECDOSFRM=CAPSULE | EC 错 | p116 l14-15 Row2 ECDOSU/ECDOSFRM 均 "TABLET, COATED"; EX:266 |
| 88, 90 | Ex6 "3-12 / 14-24 …" 省略行 | KB 自写占位 (PDF 为逐行完整数据) | p116 l16 起 Row 3 完整; EX:267 起完整 |
| 92 | "See [EX Examples]… Example 6…" | KB 导航 | — |
| 100 | Ex7 Rows 1,3,5 缺第二句 | EC 截断 | p118 l20 "Scheduled dose is represented in…"; EX:360 有该句 |
| 102 | Ex7 Rows 2,4 缺第二句 | EC 截断 | p118 l21 "Actual doses are represented using dose in mL…"; EX:362 |
| 108-109 | Ex7 表头/分隔: EPOCH 在 VISITNUM 前 | EC 错 | p118 l24 列序 "ECADJ VISITNUM VISIT EPOCH"; EX:368 |
| 110-115 | Ex7 6 行 EPOCH="VISIT TREATMENT" + 列序 | EC 错 (解析串列致) | p118 l25-33 EPOCH "TREATMENT"; EX:370-375 |
| 119 | Ex8 首段缺 Note 句 | EC 截断 | p119 l28 "…not consistent with current CDASH standards."; EX:418 |

→ 24/24 均为 EC 错值/截断/KB 自写占位/导航, **无一条是 PDF 有而 EX 缺的内容**. EC 原副本另缺 Example 4 (EX:148 有).
- PDF 结构 (p104-121 逐页标题): §6.1.3.1 EX p104 / §6.1.3.2 EC p107 (Description/Overview, Specification, p109 l28 Assumptions → p110) / §6.1.3.3 "Exposure/Exposure as Collected Examples" p111 Ex1 … p119 Ex8 / §6.1.4 ML p121. p107-110 内仅 CDISC Notes 中 "Example:" 字样, **无 EC 专属例子**. 归属 = EX (符合 B-EX review 裁定).
- 新 EC/examples.md:3 交叉引用: 节名 "Exposure/Exposure as Collected Examples" 与 p111 l1 逐字一致; "Examples 1-8" 与 p111-119 一致; 链接目标存在; 格式同 MS/PP 先例 (`> See …`), 纯导航不加 KB note (dispatch notes D6 范围). 签字.

## (2) EC/assumptions.md 新增 (G-TB6)

| 新行 | 内容 | 出处 | 判定 |
|---|---|---|---|
| :3 | `## EC – Description/Overview` | p107 l16 (PDF 标题) | 结构, 签字 |
| :5 | "An interventions domain that contains … as collected." | p107 l17 逐字 | 一致 |
| :7 | `## EC – Specification` | p107 l18 (PDF 标题) | 结构, 签字 |
| :9 | "ec.xpt, Exposure as Collected — Interventions. One record per … per mood, Tabulation." | p107 l19-20 逐字 (折行已合并) | 一致 |
| :11 | `## EC – Assumptions` | p109 l28 (PDF 标题) | 结构, 签字 |

- 位置: Description/Overview → Specification → Assumptions, 与 PDF 顺序及 CM/assumptions.md 先例一致; spec 表本体在 spec.md, 未动. 既有 H1 未动.
- 我方双向扫描 (脚本, fp_match.norm): PDF 侧 = p107 §6.1.3.2 起至 spec 表头 + p109 "EC – Assumptions" 后 + p110 (去页脚); KB→PDF 未命中仅 :1 H1 与 :11 标题 (切分点本身, 结构行); PDF→KB 67 句未命中 0. 人工复核 1(a-c)/2/3(a i-ii, b-e)/4(a-c)/5(a-b)/6/7(a-b) 全在且顺序一致, 无 KB 自写句.

## (3) EX/examples.md
- `git diff HEAD -- knowledge_base/domains/EX/examples.md` 仅 :3 一行改动 (±1). 新句: "…shared in Section 6.1.3.3 of the SDTMIG; EC/examples.md points here." 仍在 `> KB note (not in SDTMIG):` 内, 去掉了回指链接 → EC→EX 单向, 无循环指针. 节号 6.1.3.3 对 p111. 其余 EX 行未动 (census 结果与 B-EX review 一致佐证).

## (4) 无副作用
- 本批 diff 只涉及 3 个白名单文件; 删除的 `## Example N` 标题无入链 (`grep -rn 'EC/examples\|EC Examples' knowledge_base docs web/src` 仅 INDEX.md:60 文件级链接 + EX:3 纯文本).
- 触碰的 UNPARSEABLE 表 EC:84 (Ex6) 整表删除, 无单元格编辑; 保留副本 EX Ex6 属 B-EX 已审范围. 人工逐格: 不适用 (本批无新增/改动表格).
- R2 recheck: t2_recheck = 0. atoms = 0.

## 问题表

| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| writer 报告 "22 行" | 完整性 (LOW) | 实为 24 行 (漏计 :33/:109 分隔线); 判定不变, 不阻断 | 本报告 D2 脚本输出 count 24 |
| EX:360 (范围外, 信息) | — | 现 KB "Scheduled dose is represented in mg/kg"; PDF p118 l20 为 "mg/mL". 已在 B-EX (ae17f74) 提交, B-EX audit:50 建议 T4 登记; 非本批改动, 提醒主控确认 T4 登记是否已落 | p118 l20 "Scheduled dose is represented in mg/mL." |

无 FAIL / CONDITIONAL 项.
