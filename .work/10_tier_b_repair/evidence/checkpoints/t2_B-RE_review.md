# T2 B-RE reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: CONDITIONAL** — 表格 (census + 渲染图逐格) / 双向全扫 / 授权范围 / 无副作用 / links 全部通过; 唯一阻断项 = C-1 叙述 QNAM "IREEA2" 按 PDF_TYPO 取舍规则应写正确值并登记 (writer 未改也未登记).

### 输入与基线
- base = HEAD `eb13510` (RE 文件未提交); writer md5 声明复核一致: examples `032395…`→`40070b89…`, assumptions `e4165bb9…`→`330cf84b…`, spec.md `47514a45…` 未动 (`git diff HEAD --quiet -- knowledge_base/domains/RE/spec.md` = 0).
- RE 节页范围 (O20) 复核: p308 节标题 6.3.7.7 → p312 di.xpt 后接 6.3.7.8 UR; batch pdf_ranges 308-312 完整覆盖. p308 节标题与 Description 间无引言 NOTE.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-RE_reviewer/`

### 命令 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-RE_reviewer; mkdir -p $S
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-RE.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
#  -> KB tables: 6; status: {'OK': 6}; diffs: 0; exit 1 仅因全局 PDF_ONLY 333 (页 308-312 内 = 0; pdf_unparsed 仅 p274/p342, 非本批)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
#  -> RESULT: RED, regress 48; grep -cE 'p030[89]|p031[0-2]|domains/RE/' $S/fp_regress.jsonl = 0 (全为他批 §6.4.2 等)
pdftotext -f 308 -l 312 "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/raw.txt; python3 -I $S/scan.py $S; python3 -I $S/chk.py   # 双向全扫
for p in 310 311 312; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42 (= 基线; writer 记的 44 是 eb13510 修复前的瞬时值)
```
- fp_match RE 节 (§6.3.7.7) 原子: EXACT 12 / EQUIVALENT 34 / INTENTIONAL_EXCLUDE 21 / PARTIAL 28; PARTIAL 全为 p309-310 spec 表行 + p310 spec 脚注 NOTE (spec.md, 非本批白名单; 已归 O24/O15). baseline 同节 EXACT 12 / EQUIVALENT 43 / PARTIAL 28 / IE 21 (总 104 不变, 无本批回归).

### 问题表
| ref | 检查项 | 问题 | 证据 (PDF 页 + ≤25 词) |
|---|---|---|---|
| C-1 RE/examples.md:59 | PDF_TYPO 取舍 (阻断) | KB 照录 "IREEA2" 且未登记. 正确值可由 PDF 自身确定: 同句并列 "IRREA1" (叙述统一去 RE 前缀: BRESFL / IRESFL / IRREA1), p312 suppre r4 QNAM REIRREA2 + QLABEL "Inadequate Result Reason 2". 按补充口径 → KB 写 "IRREA2" 并登记 T-1. writer 理由 "叙述非表格单元不登记" 与口径不符 (pre-corrdinating / B-GF T-4 GFLINKID→GFLNKID 均为叙述先例) | p311 "represented by QNAM="IRREA1" and "IREEA2"."; p312 r4 "REIRREA2 Inadequate Result Reason 2" |
| N-1 RE/assumptions.md:17 | 范围外 (非阻断, 已登记 O30) | assumption 3 缺 "variables" (R2 REAL_GAP). 授权明确不改 assumptions 列表 → writer 处理正确; 建议主控若愿可在 attempt 2 一并授权 (单词补入) | p310 "Any Identifier variables, Timing variables, or Findings general observation class qualifiers" |
| N-2 RE/spec.md | 范围外 (非阻断, 已归 O24/O15) | spec 表脚注 "In this column, an asterisk (*) …" / "CDISC/NCI codelist values …" 缺 | p310 脚注 1 |

### CONDITIONAL 修正清单 (writer attempt 2)
1. `knowledge_base/domains/RE/examples.md:59`: `"IREEA2"` → `"IRREA2"` (仅此一处, 其余字符不动).
2. writer checkpoint 增 PDF_TYPO 清单 T-1: p311 叙述 "IREEA2" → KB "IRREA2"; 依据 = 同句 IRREA1 并列编号 + p312 suppre r4 QNAM REIRREA2 / QLABEL "Inadequate Result Reason 2"; writer.jsonl 补一行.
3. 改后复跑 fp_match, 确认 ig34_p0311 该原子仍命中 RE/examples.md (预期 EXACT→EQUIVALENT/PARTIAL 属登记内), 回 reviewer 复审 delta.

### G-TB4 表格 (census OK 6/6 + 渲染图独立逐格)
census 与 bbox 同源 → 6 张表全部按渲染图 (p311/p312 110dpi) 逐行人工核:
| KB 表 (行) | PDF | 表头/列序 | 逐行结果 |
|---|---|---|---|
| Ex1 re.xpt (:15-21, 本批触碰) | p311 | 15 列一致 (含 "..." 列) | r1-r5 一致; "..." 列 5 格 PDF 为空格 = KB 改后空; r3/r4 REORREF 空一致 |
| Ex1 di.xpt (:27-30) | p311 | 一致 | r1-r2 一致 |
| Ex1 du.xpt (:36-38) | p311 | 一致 | r1 一致 (USUBJID 空) |
| Ex2 re.xpt (:49-54) | p311 | 16 列一致 | r1-r4 一致 (PDF 折行 "XYZ-001-/001", "VISIT/2", "2013-04-/23" 为单元格换行, KB 合并正确) |
| Ex2 suppre.xpt (:63-68) | p312 | 一致 | r1-r4 一致 (QLABEL "Inadequate Result Reason 1/2" 折行合并正确; QEVAL 空) |
| Ex2 di.xpt (:74-76) | p312 | 一致 | r1 一致 |
触碰的 UNPARSEABLE / pdf_unparsed 表: 无.

### 双向全扫 (p308-312, 含表格原子)
- PDF→KB (`scan.py` 句级规范化 + `chk.py` 拼接句单查): RE 叙述/标题/Assumptions/Examples 全部命中 assumptions.md + examples.md, 除 N-1 (assumption 3). 其余未命中 = spec 表行/脚注 (spec.md, 范围外) / 版权页脚 / UR 节 / pdftotext 表格串列.
- KB→PDF (全文件, 不只 diff): assumptions.md 每行 + examples.md 每叙述行均在 PDF; 表格逐格: 仅 Ex2 re REDTC "2013-04-23" 文本层未命中 = PDF 单元格折行 "2013-04-/23" (渲染确认), 非差异. assumptions.md:17 = N-1.
- KB_AUTHORED / D6: 无自写解释性内容, 无伪节号. `# RE — Examples` / `## Example N` / `**xxx.xpt**` = 导航, 不加 KB note.

### G-TB6 反向溯源 (diff 9 新增行)
| diff 行 | 出处 / 签字 |
|---|---|
| assumptions.md:3 `## RE – Description/Overview` | 结构行 (PDF p308 小标题同名) — 签字 |
| assumptions.md:4 / :6 空行 | 结构行 — 签字 |
| assumptions.md:5 Description 句 | p308 逐字 (规范化 in-KB 命中; 折行整词无连字符) |
| examples.md:17-21 (5 行) | p311 Ex1 re.xpt r1-r5 渲染逐格一致 |
无出处词句: 0.

### 位置 / 授权 / 副作用
- Description/Overview 位于 `# RE — Assumptions` 与 `## RE – Specification` 之间, 格式同 CM / BE 先例; spec 首句 :9 已逐字存在 (p308), 未改. 授权外改动: 0 (assumptions 列表未动).
- 整个 KB diff: RE 2 文件 + BS/SM/NV (他批, 本批未触); RE 标题/锚点未变; 表格已有正确格未改坏.

### R2 recheck
- t2_recheck = 0 条. 全扫中发现的 R2 型缺失仅 N-1 (范围外, O30).

### 新增 atom / 删除清单复核
- 新增 atom: 无 (Description 为授权项). 删除 D-1 ("..." 数据格 ×5) 依据成立.

## attempt 2 (2026-11-26, 复审 writer a2 delta)

**verdict: PASS** — C-1 已关闭; N-1/O30 (主控追加授权) 逐字正确; 无其他改动.

- `git diff HEAD -- knowledge_base/domains/RE` 全量: 相对 attempt 1 只多 2 行改动 — examples.md:59 `"IREEA2"`→`"IRREA2"`, assumptions.md:17 补 "variables"; 其余 (Description 4 行 + Ex1 "..." 5 格) 与 a1 相同. md5: assumptions `925dabf6…`, examples `18d19ec3…`, spec.md `47514a45…` 未动 (与 writer a2 声明一致).
- assumptions.md:17 去掉 "3. " 后在 p308-312 pdftotext 中逐字命中 (`kb in raw` = True) — p310 "Any Identifier variables, Timing variables, or Findings …".
- examples.md:59: 文件内 "IREEA2" 已无, "IRREA2" 1 处; 该行其余字符不变. writer checkpoint a2 已登记 T-1, 依据 (同句 IRREA1 + p312 suppre r4 REIRREA2 / "Inadequate Result Reason 2") 与 reviewer C-1 一致; writer.jsonl 已补 2 行.
- 全扫 KB→PDF 复跑 (`python3 -I $S/scan.py $S`): 不在 PDF 中的只剩 :51-54 REDTC 折行 (非差异) + :59 (= 已登记 T-1); assumptions.md 全文件 0 缺.
- census 复跑 (`table_census.py --manifest $S/manifest.json --out $S/census_a2.json`): KB tables 6, OK 6, diffs 0.
- fp_match 复跑 (`--out $S/fp_a2.jsonl --regress-out $S/fp_regress_a2.jsonl`): 全量 regress 49; RE 页 1 条 = ig34_p0311_a035 (EQUIVALENT→未命中), 原子即 "IREEA2" 句, 系 T-1 有意修正引起, **预期回归**; p0310 assumption 3 原子 a007-a009 命中 RE/assumptions.md.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (= 基线).
- 备注: out_of_scope_findings.md O30 已改为 "主控授权 B-RE a2 一并补"; 可标记关闭.
