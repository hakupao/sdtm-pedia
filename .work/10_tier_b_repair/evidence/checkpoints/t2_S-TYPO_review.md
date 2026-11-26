# S-TYPO attempt 2 — Reviewer 报告 (2026-11-26)

> 状态: **CONDITIONAL** — KB 改动本身无缺陷 (独立断言 PASS + 37/37 渲染核对正确); 条件只针对门禁脚本 `typo_assert.py` 的盲区 (不带 `--plan` 时漏 4 类变异), 无需改 KB。
> 基线 HEAD 44fb042; reviewer = oh-my-claudecode:code-reviewer (opus); 独立脚本不 import writer 代码, 放 `scripts/t2s/review_S-TYPO/`; 输出目录用 `RV_OUT` 指定 (本次 = scratch `t2s_S-TYPO_reviewer/out2`)。

## 1. 独立校验 (`rv_check.py`, 对每个改动文件与 `git show HEAD:` 逐行比)

复跑: `RV_OUT=<dir> python3 .work/10_tier_b_repair/scripts/t2s/review_S-TYPO/rv_check.py knowledge_base` → `PASS`, violations 0

| 断言 | 结果 |
|---|---|
| (a) 改动行: 主控批准的 7 处固定替换 (硬编码, 不读 writer fixed.jsonl) 后, 闭表归一 + 去空白后与原行逐字相同; 空白变化只在 – / — 旁; 非空白字符数不变 | PASS: 51 文件 / 154 行; 逐字符变化 335 (`"`→`“` 139, `"`→`”` 135, `'`→`’` 55, `-`→`–` 5, `—`→`–` 1) + 删空格 10 + `...`→`…` 4 + 固定 7 = 356, 与 writer 计数一致 |
| (b) 标题行 / 整行粗体伪标题 / KB note / 代码块 / 行内代码 / URL / 链接目标 / HTML 注释 / `--VAR` / 列表符 / 表格竖线 未改 | PASS |
| (b) registry span: 按 kb_file 取全部 270 条, 每个 span 在全文件的出现次数不变, 且每个改动行内 span 出现次数不变 | PASS (含 B-IS T-6 ×3 行、B-MK T-1 ×2 行、B-TA T-4) |
| (c) 改动文件 ⊆ chapters/domains/model; 无增删文件; 工作树其它改动只有 trace.jsonl | PASS (model/ 0 改动) |
| (d) spec.md `(SHORT) Cxxxx` 与 DOMAIN 块未变 | PASS (本批改动无 spec.md) |

另: writer 门禁 `typo_assert.py knowledge_base --plan S-TYPO.plan.jsonl` → PASS (51 / 154 / 0); writer.jsonl 356 行 = plan 356 行, 全部 REPLACED。

## 2. 方向正确性

**全量方向启发式** (`rv_dir2.py`, 对全部 329 处弯引号按左右邻字判开/闭/撇号): 326 符合; 3 处不符, 逐一核 PDF:
- MH/assumptions.md:27 `History“` 与 `History,“` (闭位写成开引号 “): **PDF p173 渲染确为 “ (原文印刷错误)**, writer 照 PDF, 符合 U1。同行 PDF 是 `History, “` (逗号后有空格), KB 无空格 — 不属本批闭表, 建议 T4 知悉 (LOW)。
- ch08:42 `CMGRPID=“COMBO`: 开引号在 `=` 后, 正确。PDF p428 同页 Rows 4-6 用直引号 `"COMBO THPY 2"`、Rows 10-12 用弯引号, KB ch08:38 保持直、:42 改弯 — 与 PDF 逐句一致 (writer 窗口匹配区分正确)。

**分层渲染抽样** (`rv_sample.py`, seed 20261126, pdftotext -bbox 定位 + pdftoppm 250dpi 裁图目视; 37 处, 全部与 PDF 字形一致):

| 层 | N | 样本 (KB 位置 → PDF 页) | 结论 |
|---|---:|---|---|
| dq 开 “ | 6 | MH as:27 (p173), DS as:32 (p157), LB as:66 (p245), ch10:430 (p461), QS as:30 (p326), MH as:31 (p173) | 6/6 |
| dq 闭 ” | 6 | FA ex:302 (p375, `stools.”`), AE as:44 (p138), RELREC ex:42 (p430), QS as:33 (p327, `”-type`), PP as:19/20 (p272) | 6/6 |
| sq ’ | 6 | FT as:55 (p322), DS ex:73 (p160), ch08:232 (p433 `variables’` 复数所有格), IS ex:135 (p237), EG ex:58 (p190), ch04:504 (p33) | 6/6, 均为 U+2019 撇号形, 无 ‘ |
| em 删空格 | 4 | NV ex:61 ×3, NV ex:37 (p297, `(75-100)—are` / `eye—including` / `records—specifically`) | 4/4 PDF 两侧无空格, 仍为 em dash |
| dash | 6 | MK ex:51/55 (p293 `51–75%`), MK ex:60 (p294 `26–50%`), SUPPQUAL ex:20 + ch08:241 (p433 `Scale–Cognitive`), ch04:194 (p26 链接 `Submissions – Dataset`, em→en) | 6/6; 同格 `MILD-MODERATE` 保持连字符正确 |
| … | 4 (全部) | ch04:863/869 (p41 `"Pn…"`), SUPPQUAL as:11 + ch08:191 (p432 `STUDYID…QNAM`) | 4/4; p41 引号 PDF 为直引号, KB 保持直引号正确 |
| ¹ | 2 | ch08:212 (p432), ch08:438 (p439) | 2/2 上标 1 紧贴 `In` |
| ch04 固定 3 处 | 3 (全部) | ch04:1101 (p46 `VSDTC-VSRFTDTC` 连字符), ch04:1485 (p56) / 1514 (p57) `Supplemental Qualifiers – SUPP-- Datasets` | 3/3 |

## 3. 变异测试 (scratch KB 副本 = 工作树副本 + 单点植入; `rv_mutate.py`)

复跑: `RV_OUT=<dir> python3 .work/10_tier_b_repair/scripts/t2s/review_S-TYPO/rv_mutate.py`

| # | 植入 | writer assert (无 --plan) | writer assert --plan | rv_check | rv_dir2 |
|---|---|---|---|---|---|
| V0 | 正对照 | PASS | PASS | PASS | PASS |
| V1 | 开引号写成闭 (MH as:31 `“Y”`→`”Y”`) | **PASS (漏)** | FAIL | PASS | FAIL |
| V2 | registry span B-IS T-6 `-`→`–` (闭表内合法) | FAIL | FAIL | FAIL | — |
| V3 | registry span B-MK T-1 第 2 处 `76-95`→`76–95` | FAIL | FAIL | FAIL | — |
| V4 | 撇号写成左单引号 (DS ex:73) | **PASS (漏)** | FAIL | PASS | FAIL |
| V5 | 标题 ch04:290 直→弯 | FAIL | FAIL | FAIL | — |
| V6 | 粗体伪标题 TA ex:871 直→弯 | **PASS (漏)** | FAIL | FAIL | — |
| V7 | 行内代码 PP ex:163 | FAIL | FAIL | FAIL | FAIL |
| V8 | `--VAR`→`–VAR` (AE as:78) | FAIL | FAIL | FAIL | — |
| V9 | 闭引号写成开 (DS as:32 `EVENT”`→`EVENT“`) | **PASS (漏)** | FAIL | PASS | FAIL |

("—" = 该脚本不管此类, PASS 属预期。) reviewer 组合 (rv_check + rv_dir2) 9/9 FAIL; writer `--plan` 9/9 FAIL。

**盲区结论**: `typo_assert.py` 只校验 "同类替换", **不校验方向** (“↔”、’↔‘ 任意互换都放行), 也不把整行 `**…**` 粗体伪标题当标题保护 (只在 typo_plan 侧排除)。`--plan` 模式能抓到, 但它只证明 "树 == HEAD + plan", plan 自身方向错误无门禁兜底 — 本批靠窗口匹配 + 本 reviewer 全量方向启发式 + 37 渲染样本证明 plan 方向无误。writer 自报的 23 个变异无一覆盖方向互换 (M9 是跨类)。

## 4. 修正清单 (CONDITIONAL 条件; 均为脚本, 不动 KB)

1. [MEDIUM] `scripts/t2s/typo_assert.py` `check_line`: 增方向断言 — 改动结果为 `“`/`‘` 时前邻须为行首/空白/`([{|*_—–/=`、后邻非空白; `”` 前邻非空白; `’` 前邻非空白; 白名单只放 PDF 已证的印刷错误位置 (MH/assumptions.md:27)。参考 `review_S-TYPO/rv_dir2.py`。
2. [LOW] 同脚本 `ctx_flags`: 整行 `^\s*\*\*[^*]+\*\*:?\s*$` 标为 heading (与 typo_plan 裁定 ⑤ 口径一致)。
3. [LOW] 同脚本变异集 `typo_mutate.py` 补 V1/V4/V6/V9 四个变异并确认红; 补后在 t2_S-TYPO.md §5 记录。
4. 修完后 KB 不需重写; 重跑 `typo_assert.py knowledge_base [--plan …]` 仍应 PASS。

## 5. 其它观察

- [LOW, T4 知悉] MH/assumptions.md:27 照 PDF 复刻了 PDF 原文的反向引号 `History“` (×2), 合 U1 字面口径但读者可能视为 KB 错误; 建议 T4 用户确认是否登记 PDF_TYPO。
- 裁定落实核验: CRF `( )`/`[ ]` 未改 (CE/ch04/ML diff 无括号变化); ch08:78/82 粗体伪标题未改; 三个 A6 registry span 字节不变; 13 行多命中不一致未改 (含 ch04:793, ch08:38 未入 plan)。
- 正面: plan/writer.jsonl/fixed.jsonl 逐处可追溯; 窗口匹配能区分同页直/弯混用 (p428); 固定清单位置替换后冻结, 防二次改写。
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` = 42 ✓

## attempt 2 复审 (assert hardening, 2026-11-26)

> 结论: **PASS** — §4 修正清单 1-3 已落实; KB 未动。

- **新断言代码已读** (`typo_assert.py` `quote_dir` + `QWL` + `ctx_flags`): 判 “/‘ 左邻非字母数字且右邻非空白, ” 左邻非空白且右邻非字母数字, ’ 左邻非空白; 不带 `--plan` 也生效。白名单只有 MH/assumptions.md:27, 最多放行 2 个且必须是 “。整行 `**…**` 记为 heading。规则覆盖了我在 rv_dir2 中用的判据 (更严: ” 右邻禁字母数字)。
- **变异复跑** (scratch 副本, `RV_OUT=<dir> python3 .work/10_tier_b_repair/scripts/t2s/review_S-TYPO/rv_mutate2.py`): 下列各项不带 `--plan` 与带 `--plan` 都 FAIL, 正对照 V0 两种模式都 PASS:
  - 原 4 项: V1 (MH as:31 开→闭)、V4 (DS ex:73 撇号→‘)、V6 (TA ex:871 粗体伪标题)、V9 (DS as:32 闭→开)
  - 新 5 项: N1 (ch08:232 行中复数所有格 `variables’`→`variables‘`)、N2 (FA ex:302 句号后闭→开)、N3 (白名单行 MH as:27 正确的 “→”, 白名单没被滥用)、N4 (ch08:42 `=“`→`=”`)、N5 (FT as:55 `’`→`”` 跨类)
- **正式断言两种模式**: `typo_assert.py` → PASS (51 / 154 / 0); 加 `knowledge_base --plan …/S-TYPO.plan.jsonl` (356 行) → PASS。
- **KB 与初审一致**: `rv_check.py` 仍是 51 文件 / 154 行 / 335 逐字符改动 + 7 固定处, PASS; `rv_dir2.py` PASS; `git diff HEAD -- knowledge_base | shasum` = `fcc298fca23b…`。
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → 42。
