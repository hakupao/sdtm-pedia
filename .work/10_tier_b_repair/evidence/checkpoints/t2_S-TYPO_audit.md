# S-TYPO attempt 2 — Auditor 报告 (Rule A, 2026-11-26)

> 状态: **PASS** — 30/30 样本字形 (含开/闭方向) 与 PDF 渲染一致, 行内除排版字符外与 HEAD 逐字相同; 残余抽查 10/10 判断成立, 漏改 0。
> auditor = oh-my-claudecode:verifier (opus); 基线 HEAD 44fb042; 先独立判, 判完才读 writer / reviewer 报告。只读 KB。

## 0. 复跑命令

```
cd /Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair
python3 scripts/t2s/review_S-TYPO/audit_sample.py            # 分层抽样 30 + 残余 10 (seed 20261126)
python3 scripts/t2s/typo_assert.py                            # -> changed files 51, changed lines 154, violations 0, PASS
python3 scripts/t2s/typo_assert.py --plan work/t2_batches/S-TYPO.plan.jsonl   # -> 同上 PASS
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"; pdftotext -raw -enc UTF-8 -f N -l N "$P" -   # 字符第二来源
pdftotext -bbox -f N -l N "$P" bb.html; pdftoppm -f N -l N -r 400 -x .. -y .. -W .. -H .. -png "$P" crop   # 裁图目视
cd ../.. && python3 tools/check_links.py 2>&1 | grep "live docs"   # -> live docs: 42
```

## 1. 总体与分层

总体 = plan.jsonl 全部 356 处 (= writer.jsonl 356; 断言确认树 == HEAD + plan)。类分布: dq 开 139 / dq 闭 135 / sq 55 / em 删空格 10 / dash 6 (hyphen→en 5 + em→en 1) / … 4 / ¹ 4 / ch04 固定 3 (minus 1 + dashpair 2)。
分层配额 (brief): dq 开 6 / dq 闭 6 / sq 6 / em 删空格 3 / dash 3 / … 2 / ¹ 2 / ch04 固定 1 = 29, 余 1 从其余随机 (落在 sq)。N=30, seed 20261126。

## 2. 样本结果 (字形 = PDF 渲染裁图 400dpi + pdftotext -raw 字符; 行一致 = 去排版归一后与 HEAD 行逐字相等)

| # | 层 | KB 位置 | PDF 页 | PDF 字形 (渲染) | 方向 | 行一致 |
|---|---|---|---|---|---|---|
| 318 | dq开 | TA/assumptions:136 | 386 | `called “TREATMENT”.` | ✓ | ✓ |
| 293 | dq开 | SE/assumptions:52 | 81 | `generally “derived”` | ✓ | ✓ |
| 26 | dq开 | ch04:1215 | 50 | `such as “AT DISCHARGE”` | ✓ | ✓ |
| 58 | dq开 | ch08:325 | 436 | `A “Yes” answer` | ✓ | ✓ |
| 197 | dq开 | LB/assumptions:66 | 245 | `(e.g., “YELLOW”, “AMBER”)` | ✓ | ✓ |
| 215 | dq开 | MH/assumptions:27 | 173 | `“General Medical History“` (PDF 原文闭位印 “) | ✓ 照 PDF | ✓ |
| 147 | dq闭 | DS/assumptions:32 | 157 | `DSCAT = “OTHER EVENT”,` | ✓ | ✓ |
| 200 | dq闭 | LB/assumptions:66 | 245 | `“AMBER”)` | ✓ | ✓ |
| 74 | dq闭 | ch10:430 | 461 | `CDISC’s copyright.”` | ✓ | ✓ |
| 286 | dq闭 | SE/assumptions:18 | 79 | `“Day within Element”` | ✓ | ✓ |
| 236 | dq闭 | MS/assumptions:15 | 255 | `“RESISTANT”.` | ✓ | ✓ |
| 162 | dq闭 | FA/examples:302 | 375 | `“Watery stools.”` | ✓ | ✓ |
| 209 | sq | MH/assumptions:19 | 172 | raw `sponsor’s procedures` (裁图为同页另一处 sponsor’s, 同字形) | ✓ | ✓ |
| 311 | sq | SUPPQUAL/examples:9 | 433 | `variables’ names` | ✓ | ✓ |
| 86 | sq | AE/assumptions:41 | 138 | `sponsor’s data management` | ✓ | ✓ |
| 349 | sq | TV/assumptions:11 | 407 | `subject’s actual visits` (同页另有 2 处直 `subject's`, 非本句) | ✓ | ✓ |
| 273 | sq | QS/assumptions:36 | 327 | raw `instrument’s CT` | ✓ | ✓ |
| 250 | sq | OI/assumptions:23 | 442 | `organism’s identity` | ✓ | ✓ |
| 192 | sq | IS/examples:171 | 238 | `subject’s specimen` | ✓ | ✓ |
| 242 | em空格 | NV/examples:61 | 297 | `eye—including` 无空格 | ✓ | ✓ |
| 245 | em空格 | NV/examples:61 | 297 | `(75-100)—are` 无空格 | ✓ | ✓ |
| 240 | em空格 | NV/examples:37 | 297 | `records—specifically` 无空格 | ✓ | ✓ |
| 230 | dash | MK/examples:51 | 293 | `51–75%` en | ✓ | ✓ |
| 231 | dash | MK/examples:55 | 293 | `51–75%` en | ✓ | ✓ |
| 55 | dash | ch08:241 | 433 | `Scale–Cognitive` en; `ADAS-Cog` 与 `Alzheimer's` PDF 亦为 hyphen/直撇, KB 未动 ✓ | ✓ | ✓ |
| 7 | … | ch04:863 | 41 | `"Pn…"` (引号 PDF 直, KB 保持直) | ✓ | ✓ |
| 47 | … | ch08:191 | 432 | `(STUDYID…QNAM)` | ✓ | ✓ |
| 48 | ¹ | ch08:212 | 432 | 上标 ¹ 紧贴 `In` | ✓ | ✓ |
| 70 | ¹ | ch08:363 | 438 | 上标 ¹ 紧贴 `In` | ✓ | ✓ |
| 9 | ch04固定 | ch04:1101 | 46 | `VSDTC-VSRFTDTC.` hyphen | ✓ | ✓ |

错误 0/30 (独有信息丢失 0, 忠实度错 0)。

## 3. 残余清单抽查 (1091 条, random.sample 10, seed 20261126)

| idx | 位置 | 残余原因 | 判断 |
|---|---|---|---|
| 972/64/165/596/460/213/835 | TR/BE/DA/NV/LB/EC/SM spec.md Cross References 行 `— …` | kb_nav zero_hit | 成立: KB 自写导航 (U8), PDF 无此文字 |
| 911 | TA/examples:356 `5-10-P` / `5mg-10mg-Placebo` | inconsistent | 成立: p391/392 raw + layout 均为 hyphen (`5-10-P`, `5mg-10mg`), KB 已是 hyphen, 不改无损 |
| 665 | PP/examples:123 `One-to-Many` | zero_hit | 成立: KB 自写 anti-drift 映射表; PDF p277/279/281 为 `One to Many` (无连字符), 非排版问题 |
| 603 | OE/assumptions:1 `# OE — Assumptions` | heading blocked | 成立: 标题不改 (O60/T4) |

漏改 0/10。

## 4. 断言与门禁 (独立跑)

- `typo_assert.py` 两种模式 (无 `--plan` = 闭表 + 保护位 + 方向; `--plan` = 另要求树 == HEAD + plan): 均 `changed files 51, changed lines 154, violations 0, PASS`。
- 自做变异 (scratch 副本): TA as:136 开引号改闭 → 无 `--plan` 模式 FAIL (quote direction) ✓。另植入 "一对引号只改一半 (LB as:66 开引号回退为直)" → 无 `--plan` 模式不报 (闭表同类 + 方向只查弯引号), 仅 `--plan` 能抓。[LOW] 属 "改少" 而非 "改错", 内容不失真; 正式门禁应固定带 `--plan` 跑。
- KB 外工作树改动仅 trace.jsonl / t4_user_decisions.md (非本批授权冲突); diff 只落 chapters/domains (model 0)。
- live docs = 42 ✓。G-TB8: trace 有本批 writer (executor a1/a2) 与 reviewer (code-reviewer a2 CONDITIONAL → 复审 PASS) subagent_done ✓。

## 5. 与 writer / reviewer 报告对照 (判完后读)

计数 356/154/51 与类分布一致; reviewer 37 渲染样本与本审样本部分重叠 (MH as:27、DS as:32、LB as:66、FA ex:302、NV ex:61/37、MK ex:51/55、ch08:241/191/212、ch04:1101), 结论一致; 本审独立新增 TA/SE/ch04:1215/ch08:325/ch10/MS/MH:19/SUPPQUAL ex:9/AE/TV/QS/OI/IS ex:171 等。MH as:27 反向引号照 PDF 复刻, 同意 reviewer 建议 T4 登记 PDF_TYPO 由用户定。

## 6. 结论

技术判定 **PASS** (错误 0/30, 漏改 0/10, 断言 0 违例)。业务判定待主控。
