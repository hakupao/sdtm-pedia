# T2S S-CH1 reviewer checkpoint (chapters ch01 / ch02)

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** — 独立证伪 writer "零缺口" 结论未成功: p7-16 双向全扫 PDF→KB 缺口 0, KB→PDF 无出处内容 0 (除已登记导航 / D6 / PDF_TYPO).

### 范围 / 授权
- `git diff HEAD -- knowledge_base/chapters/ch01_introduction.md knowledge_base/chapters/ch02_fundamentals.md` → 0 行 (空). narrow_files 无.
- 页范围复核: §1 = p7-10 (p7 首行 `1 Introduction`, p10 止于 §1.5); §2 = p11-16 (`pdftotext -f 16 -l 17 -layout` 显示 p16 末段 "…selected general observation class." 后接 `3 Submitting Data in Standard Format`). 与 writer 一致.

### 方法 (独立于 writer 的 wdiff/sent; scratch S = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH1_reviewer`)
1. 人工逐句通读: PDF 文本层 `work/pdf_pages/ig34_p0007..0016.txt` vs KB 全文 (`cat -n`, 未截断), 含列表层级 (• / o / ▪ / •) 与 a.-k. 编号.
2. 脚本 `$S/scripts/bidir.py` (自写): PDF layout 去列表符、行尾 `-` 直接拼接、U+2011/弯引号/en dash 归一; KB 去 `**`/反引号/行首 `#`/`>`/`-`/`N.`/`a.`.
   (a) 5-gram 双向集合差 (PDF→KB 逐页, KB→PDF 全文); (b) 全序列 difflib (autojunk=False) 列全部非 equal opcode, 判顺序.
3. 渲染: `pdftoppm -f 15 -l 16 -r 100` → p15 图 / p16 目视.
```
python3 -I $S/scripts/bidir.py knowledge_base/chapters/ch01_introduction.md 7 10
python3 -I $S/scripts/bidir.py knowledge_base/chapters/ch02_fundamentals.md 11 16 "3 Submitting Data in Standard Format"
```

### 逐页表 (自算)
| 页 | PDF tokens | PDF→KB 缺 5-gram 段 | 定性 | KB 对应行 |
|---|---|---|---|---|
| 7 | 424 | 1 | H1 "1 Introduction" ↔ KB H1/Source 行 (导航) | ch01:1-30 |
| 8 | 511 | 0 | — | ch01:30-53 |
| 9 | 536 | 0 | — | ch01:55-83 |
| 10 | 524 | 2 | T-1 "has" (:85)、T-2 MANY 分句 LNKID↔LNKGRP (:109) = 既有 keep-correct (t2_B-ch01 续签字) | ch01:84-109 |
| 11 | 599 | 3 | H1; KB 自拟 H3 插入 (:13, :23) 打断 5-gram | ch02:1-33 |
| 12 | 593 | 1 | D6 KB note (:55) 插入 | ch02:39-59 |
| 13 | 596 | 1 | KB H3 (:76) 插入 | ch02:61-94 |
| 14 | 604 | 0 | — | ch02:94-108 |
| 15 | 198 | 2 | 图题后 D6+Mermaid; KB H3 (:133) | ch02:109-150 |
| 16 | 196 | 3 | KB H3 (:158/:167/:178) 插入 | ch02:151-186 |

序列 difflib: ch01 非 equal 5 处 (H1/Source、+has、LNKID/LNKGRP 对调 2 token); ch02 11 处, **全部为 KB 侧 insert** (H1/Source/§1 交叉引用、7 个 KB H3、2 个 D6), **0 个 delete** → PDF 每个词按序在 KB.
KB→PDF 5-gram 缺段全部落在上述插入块与 T-1/T-2, 无其他.

### 表格 / CODE_LITERAL / 图
- 两章无表 / 无代码字面量. census: `table_census.py --manifest $S/manifest.json` exit 1 (全局 RED); KB tables 0; PDF_ONLY 页码 ∩ p7-16 = ∅; pdf_unparsed 仅 p274/p342 (他批).
- p15 图 (渲染核): Identifier AND Timing AND Topic&Qualifier; Topic&Qualifier 分 Interventions-/Events-/Findings-Specific (OR); Identifier/Timing 实线、三 Specific 虚线 → New Domain.
  ch02:117-127 Mermaid: A/B -- AND --> D; C → E/F/G; E/F/G -- OR --> D → 逻辑 = Identifier ∧ Timing ∧ (I ∨ E ∨ F), 分支/顺序一致; D6 标注 :115 在. 签字.
  (LOW 观察, 不计缺: PDF 第二个 "AND" 位于 Timing 与 Topic&Qualifier 之间, Mermaid 以 C 无直连边表达, 逻辑等价.)

### KB-only 内容逐条签字
| 行 | 内容 | 类别 | 签字 |
|---|---|---|---|
| ch01:1,3 / ch02:1,3 | H1 + `Source:` 行 | 导航 | OK |
| ch02:5,7 | §1 Context 标题 + 交叉引用 ch01 | 导航 (B-ch02 D2 产物) | OK |
| ch02:13,23,76,133,158,167,178 | KB 自拟 H3 | 导航, 与 PDF 不矛盾 (SEND-only / nonclinical only / not evaluated / when appropriate 均为 PDF 引导句复述) | OK |
| ch02:55 | D6 按类举例域 | 不矛盾 (EX/CM/PR, AE/DS/MH, LB/VS/EG 归类正确) | OK |
| ch02:115-127 | D6 + Mermaid | 见上 | OK |
| 结构/删除/D6 新增清单 | 无 | — | 无改动, 无需签字 |

### PDF_TYPO
沿用 ch01 T-1/T-2 (keep-correct, t2_B-ch01.md:96-97 依据), ch02 T-1 "Trials Sets" 照录 + T4 (ch02:176). 无新增.

### 强调格式
KB 多粗体 (ch02:11/27-31/37/51-53/80)、PDF "NEVER" 粗体+下划线 (p15/p16) — 按 S-CH1 主控裁定不计.

### fp_match
`fp_match.py --baseline work/fp_baseline.jsonl` exit 1 (全局 RED, regress 71); 含 ch01/ch02 或 ig34_p0007-0016 的回归 = 0.
p7-16 原子 186: hit_target 182; 未命中 3 = p10_a002 (T-1)、p10_a023 (T-2)、p15_a006 (FIGURE) 均预期; p9_a024 hit_any 为 LB (atom 缺逗号, B-ch01 audit:69 已定), 5-gram 显示 p9 全在 ch01.

### check_links
`python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (= 基线).

### 问题表
无阻断项. 修正清单: 无.
