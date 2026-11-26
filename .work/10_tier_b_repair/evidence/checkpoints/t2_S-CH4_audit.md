# T2S S-CH4 auditor checkpoint (Rule A)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

**Verdict: PASS** — 独有信息丢失 0, 忠实度错误 0 (N=30, seed 20261126).

- 对象: `git diff HEAD -- knowledge_base/chapters/ch04_general_assumptions.md` (1566→1584 行; md5 `40832488e41bf01dd3dd5b6b54e56b06` = reviewer 复核终态). 工作树另有 model/02 改动属并行批, 不计. narrow_files 空.
- 先独立判 (抽样 + 反扫 + 渲染 + diff 逐条) 后才读 `t2_S-CH4.md` / `t2_S-CH4_review.md`; 结论一致.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH4_auditor/` (`sample.py` / `look.py` / `rev.py` / `div.py`; 渲染 p25/30/32/35/38/40/44/46/47/51/54/55/56/59 @110dpi).

### 抽样 (可复跑: `python3 -I $S/sample.py`, 在 repo 根)
- P = `work/pdf_atoms.jsonl` 中 ig34, atom_type ∈ SENTENCE/LIST_ITEM/NOTE/CROSS_REF/TABLE_ROW, 页 22-59, parent_section 以 "§4" 开头 (p21 §3.2 / p60 §5 不在页范围; p22-59 无别节原子), 去 ledger INTENTIONAL_EXCLUDE (29) → |P| = 889. intros 无.
- C = writer.jsonl 中 action ∉ {VERIFIED, SKIPPED_PDF_TYPO} 且 pdf_page 非空的页 (23/25/26/30/31/32/33/35/36/39/40/43/44/46/47/51/52/55/56) 上的 P 原子 = 430.
- N = min(30, max(20, ceil(88.9)), 889) = 30; C 抽 ceil(N/3)=10, P−C 抽 20. `random.Random(20261126)`.

| # | atom_id | PDF 页 + 摘要 | KB ch04:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0023_a021 | p23 拆分域规则 1: DOMAIN 值一致 | :73 | 否 | 是 | §4.1.7 | 逐字 |
| 2 | ig34_p0025_a033 | p25 qssw.xpt Row 9 (TABLE_ROW) | :139 | 否 | 是 | §4.1.7.1 | 渲染逐格 15/15 (原子抽取漏 QSSEQ "9"/QSLOBXFL "Y", KB 与渲染一致) |
| 3 | ig34_p0032_a004 | p32 EXADJ CRF "Insufficient Response" (TABLE_ROW) | :411 | 否 | 是 | §4.2.7.1 | 渲染逐格 2/2; 选项符号 [ ] vs PDF 圆形 = U4 归 S-TYPO |
| 4 | ig34_p0035_a001 | p35 "For example," | :559 | 否 | 是 | §4.2.8.2 | 逗号同 PDF (本批改动) |
| 5 | ig34_p0035_a025 | p35 QNAM/QLABEL 可能需更具体 | :586 | 否 | 是 | §4.2.8.3 | 逐字 |
| 6 | ig34_p0039_a027 | p39 ISO 8601 截断示例表引句 | :764 | 否 | 是 | §4.4.2 | 逐字 |
| 7 | ig34_p0040_a007 | p40 连字符表示缺失中间分量 | :785 | 否 | 是 | §4.4.2 | 逐字 |
| 8 | ig34_p0046_a005 | p46 日期作结果的建模方法 | :1066 | 否 | 是 | §4.4.9 | 逐字 |
| 9 | ig34_p0046_a018 | p46 VS 时间点表 Row 2 (TABLE_ROW) | :1098 | 否 | 是 | §4.4.10 | 渲染逐格 6/6 |
| 10 | ig34_p0047_a005 | p47 "For instance:" | :1117 | 否 | 是 | §4.4.10 | KB 自造标签已删 (D2), 句末 "For instance:" 同 PDF; 其后 4 项圆点列表同 PDF |
| 11 | ig34_p0027_a006 | p27 QNAM.XVAR 命名 | :206 | 否 | 是 | §4.1.9 | 逐字 (PDF `") ."` 空格 = T-10) |
| 12 | ig34_p0028_a006 | p28 "CD" 后缀短名 | :245 | 否 | 是 | §4.2.1 | 逐字 |
| 13 | ig34_p0031_a018 | p31 --CAT/--SCAT 由 sponsor 定义 | :391 | 否 | 是 | §4.2.6 | 逐字 |
| 14 | ig34_p0033_a028 | p33 --TERM / --PRESP | :521 | 否 | 是 | §4.2.7.3 | 逐字 |
| 15 | ig34_p0036_a010 | p36 TSPARMCD TTYPE 例 | :632 | 否 | 是 | §4.2.8.4 | 逐字 |
| 16 | ig34_p0038_a005 | p38 AE 原始/修改/标准值表行 (TABLE_ROW) | :697 | 否 | 是 | §4.3.6 | 渲染逐格 4/4 (DS 行修改列空同 PDF) |
| 17 | ig34_p0038_a033 | p38 [T] 时间标识 | :732 | 否 | 是 | §4.4.1 | 逐字 |
| 18 | ig34_p0038_a036 | p38 [ss] 秒 | :735 | 否 | 是 | §4.4.1 | 逐字 |
| 19 | ig34_p0039_a026 | p39 年 4 位, 其余补零 | :762 | 否 | 是 | §4.4.2 | 逐字 |
| 20 | ig34_p0040_a003 | p40 不确定区间表 Row 2 (TABLE_ROW) | :781 | 否 | 是 | §4.4.2 | 渲染逐格 3/3; 表头首格空同 PDF |
| 21 | ig34_p0040_a005 | p40 不确定区间表 Row 4 (TABLE_ROW) | :783 | 否 | 是 | §4.4.2 | 渲染逐格 3/3 |
| 22 | ig34_p0045_a004 | p45 "Prior" 筛选前 | :1022 | 否 | 是 | §4.4.7 | 逐字 (PDF 双空格) |
| 23 | ig34_p0045_a014 | p45 CMENTPT = 末次访视日期 | :1031 | 否 | 是 | §4.4.7 | 逐字 |
| 24 | ig34_p0046_a004 | p46 高中毕业日期 | :1064 | 否 | 是 | §4.4.9 | 逐字 |
| 25 | ig34_p0048_a039 | p48 里程碑可在入组前 | :1185 | 否 | 是 | §4.4.11 | 逐字 |
| 26 | ig34_p0048_a045 | p48 非所有研究有里程碑 | :1187 | 否 | 是 | §4.4.11 | 逐字 |
| 27 | ig34_p0049_a023 | p49 FAOBJ 为里程碑 | :1209 | 否 | 是 | §4.4.11 | 逐字 |
| 28 | ig34_p0052_a009 | p52 原因可能未收集 | :1278 | 否 | 是 | §4.5.1.2 | 逐字 |
| 29 | ig34_p0056_a003 | p56/p55 QLABEL = 原变量标签 | :1411 (+ 约定表 :1479) | 否 | 是 | §4.5.3.2 | 逐字; 约定表 (渲染 p56) 列头 4 格 + 3 行 × 4 格一致, KB 自造 Convention 列已删 |
| 30 | ig34_p0059_a029 | p59 ABLFL 行 (TABLE_ROW) | :1573 | 否 | 是 | §4.5.9 | 渲染逐格 5/5 |

独有信息丢失 = 0; 忠实度错误 = 0.

### 另查
- gaps / intros / footnote_moves: 本批 json 均空 (无域 spec.md), 无需落地核.
- diff 逐条 (渲染核): p23 URL 括号 + ")." 同 PDF; p25-26 6 个 "Dataset for …" 标题与 xpt 名分两行同 PDF; p26 "natural key for the MK domain." 句号同 PDF; p30 层级码块缩进 (DOMAIN 与 STUDYID 齐) / "For the subject" 等无冒号 / 1. 编号 / i.-iii. 同 PDF; p31 --LNKID/--LNKGRP 1./2. 同 PDF; p32-33 CRF 表头 "Options" (KB 自造) → 空; p35-36 "For example,"; p39 "e.g. 2001-…" 照 PDF (PDF 合法写法, 主控 S-CH4 口径); p39-40 表头 "#" → 空同 PDF; 8 个 KB 自造粗体标签 (p35 Example 1-3 / p43 ×2 / p47 / p55 / p56) 删除后紧随文字均为 PDF 原句, p35 PDF 无 "Example n" 标签 (渲染核); p44/p46/p51 图题行补入 (PDF 有 "Figure. …"); p44 Mermaid 节点文字与图框一致, 图注与图内文字框逐字一致 ("The medical event…"); p47 4 场景改圆点同 PDF; p52-54 "Example n" + 数据集名行同 PDF; p56 约定表删 KB 自造首列 (D2; 行信息由 PDF 列头承载); O19 附录 D2: EX/examples.md:239 ("The following CRFs show data for 2 subjects.", ## Example 6) 与 MB/examples.md:156/158 (RELSPEC Row 1 / Rows 2-6, ### Example 3) 原文在位, 两个交叉引用锚点有效, 无入站链接指向被删附录标题.
- 反向 KB→PDF 全文件扫 (`python3 -I $S/rev.py` 对 p22-59 文本 + `div.py` 定位分歧): 未命中全部定性 — (a) 导航: H1/Source 行/`## Overview`/`## Appendix` + 2 行交叉引用/"xx.xpt:" 标签 (U8); (b) D6 块 (:7 :17 :50-56 :260-273 :533-544 :824-830 :894 :905 :906 :936-941 :957-964 :981-984 :1003-1015 :1076-1090 :1255-1261 :1305), 内容核无与 PDF 矛盾 (:957 AFTER 条件与 p44 列表一致; :1015 图注 = p44 图内文字); (c) 已登记 PDF_TYPO: :668 T-3 "appears in", :932 T-8 撇号, :1122 T-9 "(–TPTREF", :1195 T-4 "occurrs", :1344 T-5 EGSTRESC, eg.xpt 行号 T-1 (渲染 p54: PDF 4,6,5,7 与 Row 5/6 说明矛盾); (d) 多行单元格 pdftotext 串列 (QS/MK/日期/约定/baseline/suppmh/suppae 表) — 渲染逐格一致; (e) CRF 选项符号 [ ] (U4) 与 dash 类 (:1101 U+2212 "VSDTC−VSRFTDTC", :1485/:1514 "Qualifiers -- SUPP--" vs PDF en dash) → S-TYPO 范围. **无 PDF 出处且未 D6 的解释性内容 = 0.**
- 位置: 30 样本全部在 PDF 所属节对应 KB 节下 (按 KB 标题行映射核).
- 授权范围: 本批改动只在 `knowledge_base/chapters/ch04_general_assumptions.md`; narrow_files 空.
- G-TB8: trace 有 T2S.S-CH4 writer (`oh-my-claudecode:executor`, 08:02:22Z + delta 08:08:09Z) + reviewer (`oh-my-claudecode:code-reviewer`, PASS, 08:15:01Z, 在 writer delta 之后) subagent_done; `agent: main` 本批记录 0. 当前文件 md5 = reviewer 记录终态.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (= 基线 42).
- 与 writer/reviewer 对照 (判完后读): T-1~T-10 登记、D2 标签删除 8 项、census (OK 19 / UNP 38 / DIFF 1 = T-1)、LOW L-1~L-4 与本审一致; 无分歧. 观察 (不阻断): :906 D6 以列表项嵌入 PDF 列表 (既有, 同 reviewer L-2); 附录交叉引用措辞 "for this text" 指代已删内容, 可在 T3 统一措辞.
