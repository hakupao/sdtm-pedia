# T2 B-ch03 reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- 对象: `knowledge_base/chapters/ch03_submitting_data.md` (git diff HEAD; 改后 md5 `ce391485beb5525ecb245aaba39bc835` = writer 报告值). PDF §3 = p17-21 (p16 末为 §2.7, p22 起 §4; 与 writer 核定一致).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-ch03_reviewer/` (p17_21.txt layout 文本, raw.txt, all.txt, lay.py/lay2.py, bidi.py, p17-p21 渲染 120dpi, census_after.json, fp_after.jsonl, fp_regress.jsonl)
- 工作树其他改动 (SC/SUPPQUAL/TI/TV) 属别批, 未计入; 本批只触碰 ch03 一份文件.

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-ch03_reviewer
P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1; KB tables: 1; status {'UNPARSEABLE': 1}; diffs 0 -> 预期 (ch03:22 为 unparseable, 转人工)
pdftotext -f 17 -l 21 -layout "$P" $S/p17_21.txt
python3 -I $S/lay2.py $S/p17_21.txt knowledge_base/chapters/ch03_submitting_data.md
  # 独立方法 (layout 字符列位 + 页内表头列定位, 非 writer 的 bbox): pdf rows 63 / kb rows 63; diffs 2 (BE Keys / FT Keys = T-1/T-2)
pdftotext -f 17 -l 21 "$P" $S/raw.txt; python3 -I $S/bidi.py $S/raw.txt knowledge_base/chapters/ch03_submitting_data.md
  # 叙述双向 (严格: 弯引号/破折号不归一): 只剩标题拼接伪 MISS + KB:3 Source 导航行, 无真实缺失/多出
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # 全局 RESULT: RED, regressions 60 条, 页码全在 118-396 (他批) -> p17-21 回归 0
  # p17-21 原子 156: hit_target 153 (baseline 145); 不命中 3 = p18_a012 (BE T-1), p18_a036 (FT T-2), p18_a046 (MB, 见下)
diff <(grep '^#' knowledge_base/chapters/ch03_submitting_data.md) <(git show HEAD:knowledge_base/chapters/ch03_submitting_data.md | grep '^#')   # 空, 标题未动
pdftotext -f 453 -l 453 -layout "$P" $S/p453.txt; grep -n -A8 "^3.2 " $S/p453.txt   # D-2 依据
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42 (基线 42)
```

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | 1-6 | 无阻断问题 | — |
| T-4 (ISSCMBCL) | PDF_TYPO 依据 (LOW, 信息) | 照录 + T4 正确. 补充给 T4 裁定参考: v3.4 IS 新增变量含 `ISMSCBCE` (p456 Changes 表), 与 `ISSCMBCL` 字形近似, 但 PDF 自身无法断定即其笔误 → 维持照录 | p456 "Added 6 new variables: ISBDAGNT, ISMSCBCE, ISTSTOPO, ISTSTCND, ISCNDAGT, and NHOID." |

### D2 删除逐条核
| # | 内容 | 判定 | 依据 |
|---|---|---|---|
| D-1 | "Dataset definition metadata should include:" + bullet | 成立 | 已由 :16 PDF 原句 (含 "as shown in Section 3.2.1, Dataset-level Metadata") 替代, p17 |
| D-2 | **Note:** "In the event that no records are present … should not be described in the Define-XML document." | **成立** | p453 Changes 表 §3.2 行: "Removed the following paragraph as there are now guidelines in the MSG v2.0 and the Define-XML v2.1 standard: \"In the event that no records…\"" — v3.4 已删除该段, p17-21 亦无; KB 保留即把 v3.3 废止文字当现行 (与 PDF 矛盾) → D2 删 |
| D-3 | "The Dataset-level Metadata table provides examples of dataset structures:" | 成立 | KB 自写表前占位句, p17 无对应 (补充口径 "KB 自写占位句 → 删") |
| D-4 | EG Keys 末 ", EGREPNUM" | 成立 | p18 渲染 EG Keys 止于 EGTPTNUM |
| D-5 | #8-16 旧改写文字 | 成立 | 同位置已为 PDF 原文, fp 本页回归 0 |

### PDF_TYPO 依据核
| T | PDF | KB | 核验 | 判定 |
|---|---|---|---|---|
| T-1 | p18 BE Keys `BESDTC` | `BESTDTC` | 全文 `BESDTC` 仅 p18; `BESTDTC` 见 p144-147 (BE spec/例) 等 8 页 → PDF 自身可定 | 维持 KB 正确值 + 登记, 同意主控裁定 |
| T-2 | p18 FT Keys `TESTCD` | `FTTESTCD` | `FTTESTCD` 见 p319/p323 (FT spec); 同表 Findings 行均 `<XX>TESTCD` → 可定 | 同上 |
| T-3 | p19 UR Structure "per location per per visit" | 照录 | p312 UR spec 首句同为 "per per visit" (全文仅 p19/p312 两处), 缺词或衍词不可定 | 照录 + T4, 同意 |
| T-4 | p18 IS Keys `ISSCMBCL` | 照录 | 全文仅 p18; IS spec 无 ISSCM* 变量; 原 KB `ISSCMBDL` 全文 0 处 | 照录 + T4, 同意 (见上表补充) |
| (其他 Keys 改) | CO `CODTC` / IS `ISTSTOPO` / RS `RSTPTNUM` | — | `COOTC`/`ISSTOPO`/`RSPTPNUM` 全文 0 处; 新值与 p17-19 渲染一致 | REPLACED 正确 |

### G-TB4 人工逐格表 (ch03:22-86, 63 行 × 7 列; 对 p17-p20 120dpi 渲染逐格目视 + layout 列位独立比对)
列: Dataset / Description / Class / Structure / Purpose / Keys / Location. Purpose 列 63 行均 "Tabulation" 一致; Location 列 63 行均 `<ds>.xpt` 一致.

| KB 行 | Dataset | Description | Class | Structure | Keys | 结论 |
|---|---|---|---|---|---|---|
| 24 | CO | 一致 | 一致 | 一致 | 一致 (CODTC, p17) | 一致 |
| 25 | DM | 一致 | 一致 | 一致 | 一致 | 一致 |
| 26 | SE | 一致 | 一致 | 一致 | 一致 | 一致 |
| 27 | SM | 一致 | 一致 | 一致 | 一致 | 一致 |
| 28 | SV | 一致 | 一致 | 一致 | 一致 | 一致 |
| 29 | AG | 一致 | 一致 | 一致 | 一致 | 一致 |
| 30 | CM | 一致 | 一致 | 一致 (constant-dosing 折行连字符合并) | 一致 | 一致 |
| 31 | EC | 一致 | 一致 | 一致 | 一致 | 一致 |
| 32 | EX | 一致 | 一致 | 一致 | 一致 | 一致 |
| 33 | ML | 一致 | 一致 | 一致 | 一致 | 一致 |
| 34 | PR | 一致 | 一致 | 一致 | 一致 | 一致 |
| 35 | SU | 一致 | 一致 | 一致 | 一致 | 一致 |
| 36 | AE | 一致 | 一致 | 一致 | 一致 | 一致 |
| 37 | BE | 一致 | 一致 | 一致 | PDF BESDTC / KB BESTDTC | 差异 = T-1 (登记) |
| 38 | CE | 一致 | 一致 | 一致 | 一致 | 一致 |
| 39 | DS | 一致 | 一致 | 一致 | 一致 | 一致 |
| 40 | DV | 一致 | 一致 | 一致 | 一致 | 一致 |
| 41 | HO | 一致 | 一致 | 一致 | 一致 | 一致 |
| 42 | MH | 一致 | 一致 | 一致 | 一致 | 一致 |
| 43 | BS | 一致 | 一致 | 一致 | 一致 | 一致 |
| 44 | CP | 一致 | 一致 | 一致 ("timepoint" 连写同 PDF) | 一致 | 一致 |
| 45 | CV | 一致 | 一致 | 一致 | 一致 | 一致 |
| 46 | DA | 一致 | 一致 | 一致 | 一致 | 一致 |
| 47 | DD | 一致 | 一致 | 一致 | 一致 | 一致 |
| 48 | EG | 一致 | 一致 | 一致 | 一致 (止于 EGTPTNUM) | 一致 |
| 49 | FT | 一致 | 一致 | 一致 | PDF TESTCD / KB FTTESTCD | 差异 = T-2 (登记) |
| 50 | GF | 一致 | 一致 | 一致 | 一致 | 一致 |
| 51 | IE | 一致 | 一致 | 一致 | 一致 | 一致 |
| 52 | IS | 一致 | 一致 | 一致 | 一致 (ISSCMBCL, ISTSTOPO; T-4 照录) | 一致 |
| 53 | LB | 一致 | 一致 | 一致 | 一致 | 一致 |
| 54 | MB | 一致 | 一致 | 一致 ("microbiology specimen finding") | 一致 | 一致 (fp a046 不命中为原子抽取漏 "specimen", KB 与渲染一致) |
| 55 | MI | 一致 | 一致 | 一致 | 一致 | 一致 |
| 56 | MK | 一致 | 一致 | 一致 | 一致 | 一致 |
| 57 | MS | 一致 | 一致 | 一致 | 一致 | 一致 |
| 58 | NV | 一致 | 一致 | 一致 | 一致 | 一致 |
| 59 | OE | 一致 | 一致 | 一致 | 一致 (14 项) | 一致 |
| 60 | PC | 一致 | 一致 | 一致 | 一致 | 一致 |
| 61 | PE | 一致 | 一致 | 一致 | 一致 | 一致 |
| 62 | PP | 一致 | 一致 | 一致 | 一致 | 一致 |
| 63 | QS | 一致 | 一致 | 一致 | 一致 | 一致 |
| 64 | RE | 一致 | 一致 | 一致 | 一致 | 一致 |
| 65 | RP | 一致 | 一致 | 一致 | 一致 (含 DOMAIN) | 一致 |
| 66 | RS | 一致 | 一致 | 一致 | 一致 (RSTPTREF, RSTPTNUM, RSEVAL, RSEVALID) | 一致 |
| 67 | SC | 一致 | 一致 | 一致 (句末 "." 同 PDF) | 一致 | 一致 |
| 68 | SS | 一致 | 一致 | 一致 | 一致 | 一致 |
| 69 | TR | 一致 | 一致 | 一致 | 一致 | 一致 |
| 70 | TU | 一致 | 一致 | 一致 | 一致 | 一致 |
| 71 | UR | 一致 | 一致 | 一致 ("per per", T-3 照录) | 一致 | 一致 |
| 72 | VS | 一致 | 一致 | 一致 | 一致 | 一致 |
| 73 | FA | 一致 | 一致 (Findings About) | 一致 | 一致 | 一致 |
| 74 | SR | 一致 | 一致 (Findings About) | 一致 | 一致 | 一致 |
| 75 | TA | 一致 | 一致 | 一致 | 一致 | 一致 |
| 76 | TD | 一致 | 一致 | 一致 | 一致 | 一致 |
| 77 | TE | 一致 | 一致 | 一致 | 一致 | 一致 |
| 78 | TI | 一致 | 一致 | 一致 | 一致 | 一致 |
| 79 | TM | 一致 | 一致 | 一致 | 一致 | 一致 |
| 80 | TS | 一致 | 一致 | 一致 | 一致 | 一致 |
| 81 | TV | 一致 | 一致 | 一致 | 一致 | 一致 |
| 82 | RELREC | 一致 | 一致 | 一致 | 一致 | 一致 |
| 83 | RELSPEC | 一致 | 一致 | 一致 | 一致 | 一致 |
| 84 | RELSUB | 一致 | 一致 | 一致 | 一致 | 一致 |
| 85 | SUPP-- | 一致 | 一致 | 一致 | 一致 | 一致 |
| 86 | OI | 一致 | 一致 | 一致 | 一致 | 一致 |

行集合双向: PDF 63 = KB 63, 行序一致, 表头 7 列名/列序一致. 差异仅 2 格 (T-1/T-2, 登记的 PDF_TYPO).

### 叙述双向全扫 (p17-21, 独立脚本, 含表格原子见上)
- PDF→KB: 全部句子命中 (仅剩 PDF 标题与下一句拼接造成的伪 MISS 6 处, 逐条人工确认所在句在 KB 均逐字存在). "Relating Non-standard …" PDF 折行连字符, KB 正确.
- KB→PDF: 仅 `:3 Source: …` (导航) 与 `:110 ---` (分隔线) 无 PDF 对应; 无 KB 自写解释性内容, 无伪节号, D6 无适用项.
- 字符级: `sponsor’s actual` (:20) / `“unnatural”` (:98) 弯引号、`classes—typically` (:16) em dash 与 PDF 一致; `sponsor's database` (:100) PDF 为直撇, KB 一致.
- 位置: "In addition, comments can also be provided where needed." 移至 §3.2 段末 = PDF 句序; Conformance 10 条 bullet = PDF bullet.

### R2 recheck
- `t2_recheck[]` 为空, 无条目.

### G-TB6 新增/改动行签字 (diff +27 行)
- 内容行 (逐条在 p17-21 找到出处): :7, :9, :10, :16, :20, :24, :48, :52, :66, :71, :92, :98, :100, :106, :116-125 — 全部有出处, 无自造.
- 结构行: :96 `**Definitions**` (PDF p20 粗体小标题 "Definitions", 签字); :97/:99 空行 (段落分隔, 签字). 无新增标题/锚点.
- 无出处词句: 0.

### 结论
atoms 1/1 正确 (CODTC); O5 全表 63 行逐格核 → 仅 T-1/T-2 登记差异; R3 叙述 9 处改动全部逐字回到 PDF; D-2 删除依据 (p453) 成立; 无授权外改动. PASS.
