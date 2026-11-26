# T2S.S-HOST Auditor (Rule A 独立抽检) — attempt 1

> agent: oh-my-claudecode:verifier (opus), 2026-11-26. 先独立判, 判完才读 `t2_S-HOST.md` / `t2_S-HOST_review.md`. 只读 KB.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-HOST_auditor/`

**Verdict: PASS** — 独有丢失 0, 忠实度错误 0 (抽样 N=20, 另 3 个未抽中原子补检 = P 全检 23/23).

## 抽样 (可复跑; repo 根执行 `python3 -I $S/sample.py`)
```
P = pdf_atoms 中 ig34, atom_type ∈ {SENTENCE, LIST_ITEM, NOTE, CROSS_REF, TABLE_ROW}, 且
    (p285 & parent_section 以 "§6.3.6 " 开头) ∪ (p415 & "§7.4 [") ∪ (p425-426 & "§7.5 "), 去 ledger INTENTIONAL_EXCLUDE.
    边界页别节排除 (p285 §6.3.7/§6.3.7.1; p415 §7.3.3 TM; p425 §7.4.2.1 NullFlavor). §7.3 引言 (p407) 为 O47/TV 宿主, 不入 P, 单独核假阳.
    intros = §6.3.6 (p285 a002-a005, 已在 P 内).
writer 页 = S-HOST.writer.jsonl pdf_page {285, 407, 415}; C = P 中落在 writer 页的原子.
N = min(30, max(20, ceil(0.1*|P|)), |P|); rng = random.Random(20261126); s1 = rng.sample(C, ceil(N/3)); s2 = rng.sample(sorted(P - s1), N - |s1|)
```
结果: |P| = 23 (§6.3.6 4 + §7.4 引言 4 + §7.5 15), |C| = 8, N = 20 (writer 页 7 + 其余 13), seed = 20261126. 未抽中 3 个 (p415 a028, p426 a005, a009) 一并核 → 全检.

## 样本判定 (机械: `python3 -I $S/match.py $S/sample.json` 归一后子串命中; 再对 pdftotext -raw 句级比对 + p285 110dpi 渲染)
| # | atom_id | PDF 页:摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0415_a029 | 415: TI/TS 为方案表格式摘要 | TI/assumptions.md:10 | 否 | 是 | 是 | 逐字 |
| 2 | ig34_p0285_a005 | 285: 框段 2, 两版本并存时可用 MO 或体系域 | NV/assumptions.md:11 | 否 | 是 | 是 | 逐字 (2 句, "body-system based" 连字符照 PDF) |
| 3 | ig34_p0285_a002 | 285: 框标题 Domain Decommissioning Update | NV/assumptions.md:5 | 否 | 是 | 是 | 渲染为粗体, KB `**…**` 一致 |
| 4 | ig34_p0415_a026 | 415: "This section contains the TD datasets that describe:" | TI/assumptions.md:5 | 否 | 是 | 是 | 逐字 |
| 5 | ig34_p0415_a027 | 415: 受试者入选标准 (Section 7.4.1) | TI/assumptions.md:7 | 否 | 是 | 是 | 交叉引用在 |
| 6 | ig34_p0285_a003 | 285: MO 自 v3.4 退役 | NV/assumptions.md:7 | 否 | 是 | 是 | 逐字 |
| 7 | ig34_p0285_a004 | 285: 框段 1, v3.2 引入 MO 的背景与弃用决定 | NV/assumptions.md:9 | 否 | 是 | 是 | 逐字 5 句, 含 "in a future version of the SDTMIG" |
| 8 | ig34_p0426_a001 | 426: step 4 各 arm 的 element | TI/assumptions.md:45 | 否 | 是 | 是 | 逐字 |
| 9 | ig34_p0426_a004 | 426: step 7 比较 arm, 定义 epoch | TI/assumptions.md:48 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0426_a008 | 426: step 11 TI / TIVERS | TI/assumptions.md:52 | 否 | 是 | 是 | 逐字 |
| 11 | ig34_p0425_a030 | 425: step 1 流程图/schema | TI/assumptions.md:42 | 否 | 是 | 是 | 逐字 |
| 12 | ig34_p0425_a027 | 425: §7.5 首句 arm→element/epoch | TI/assumptions.md:40 | 否 | 是 | 是 | 逐字 |
| 13 | ig34_p0425_a032 | 425-426: step 3 多分支点 (跨页) | TI/assumptions.md:44 | 否 | 是 | 是 | 跨页两半合一, 逐字 |
| 14 | ig34_p0425_a031 | 425: step 2 决策规则 | TI/assumptions.md:43 | 否 | 是 | 是 | 逐字 |
| 15 | ig34_p0425_a029 | 425: 步骤可重叠/迭代 | TI/assumptions.md:40 | 否 | 是 | 是 | 逐字 |
| 16 | ig34_p0425_a028 | 425: 实际过程可偏离编号步骤 | TI/assumptions.md:40 | 否 | 是 | 是 | 逐字 |
| 17 | ig34_p0426_a006 | 426: step 9 TD 疾病评估 | TI/assumptions.md:50 | 否 | 是 | 是 | 逐字 |
| 18 | ig34_p0426_a003 | 426: step 6 split/lump | TI/assumptions.md:47 | 否 | 是 | 是 | 直引号 vs PDF 弯引号 = 既有排版 (S-TYPO), 不计 |
| 19 | ig34_p0426_a007 | 426: step 10 TM 触发 | TI/assumptions.md:51 | 否 | 是 | 是 | 逐字含 "pre- (e.g., …) or on-study" |
| 20 | ig34_p0426_a002 | 426: step 5 element 起点/时长 | TI/assumptions.md:46 | 否 | 是 | 是 | 逐字 |
| +1 | ig34_p0415_a028 | 415: 试验特征 (Section 7.4.2) | TI/assumptions.md:8 | 否 | 是 | 是 | 补检 |
| +2 | ig34_p0426_a005 | 426: step 8 visit | TI/assumptions.md:49 | 否 | 是 | 是 | 补检 |
| +3 | ig34_p0426_a009 | 426: step 12 TS | TI/assumptions.md:53 | 否 | 是 | 是 | 补检 |

独有丢失 0 / 23; 忠实度错误 0 / 23; 位置错误 0.

## 另查
- **intros §6.3.6** (U3/O31): NV/assumptions.md:3-11 位于 H1 之后、`## §6.3.7 …` (:13) 之前; 标题 + 粗体框标题 + 3 段与 p285 渲染逐字 (pdftotext -raw 句级全命中). ✔ gaps / footnote: 空 (本批无 spec.md).
- **反向 KB→PDF** (`python3 -I $S/reverse.py <pdf> <file> lo hi`): TI 全文件 vs p415-426 → 非标题行 26/26 OK; 未命中仅 H1 与 `## §7.4 … (TI, TS) — Introduction` / `## §7.5 …` 标题 (导航; "(TI, TS)" vs PDF "(TI and TS)" = O48 已登记, 规则 6). NV :1-24 → 非标题行全 OK. 无 PDF 出处且未 D6 的行 = 0.
- **§7.3 宿主假阳** (sections[0]): TI 中无 p407 §7.3 专属内容 (grep "healthcare facility|Trial Visits|7.3" 0 命中); TI:5 与 p407 a011 仅为与 p415 a026 逐字同句, 其后列表指向 7.4.1/7.4.2; §7.3 正身在 TV/assumptions.md:3-11. 假阳成立, TI 不改正确.
- **授权范围**: `git diff HEAD --stat -- knowledge_base/domains/NV knowledge_base/domains/TI` → 仅 NV/assumptions.md 10+/0-, 全部落在 narrow scope (§6.3.7 前插入 §6.3.6 节); TI 0 改. ✔
- **新插文字字符**: p285 框内无弯引号/dash/省略号, KB 新增行纯 ASCII, 无 U1 问题.
- **G-TB8**: trace 有 writer (executor, 07:27:46Z) + reviewer (code-reviewer, PASS, 07:30:58Z); NV mtime 16:26:48 +0900 = 07:26:48Z < reviewer 完成, 无 reviewer 后改动; 本批无 agent main 写 KB 记录. ✔
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `live docs: 42` (基线 42).

## 对照 writer / reviewer (判完后读)
与 writer (改动 5 INSERTED, TI 0 改, §7.3 假阳) 及 reviewer PASS 结论一致. 范围外: writer F-1 / reviewer L-1 (ch10_appendices.md MO 段 "deprecate MO in SDTMIG v3.4" 与 p285 不同) 交 S-CH, 不计本批. 无分歧.
