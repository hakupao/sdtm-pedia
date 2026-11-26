# T2 B-SU writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `437c2ad9205fbacf495e35fa5928492fff8ed852` (SU 文件改前工作树 clean)
- md5: SU/assumptions.md `c6043758b6bb5fc636937c9fd7b82929` → `963f8b5fad9750d98743481cfd2a6bd4` (20 → 30 行); SU/examples.md 未动 `d5b3e9a86424056bd4854b556bd7dd60`; SU/spec.md 未动 `fb692d806c0964aa9167729882335083`
- 白名单: batch json kb_files = examples.md; assumptions.md 按通用主控授权 (Description/Overview + spec 首句, O17)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SU_writer/` (before 副本, p129/p132/p133 渲染 110dpi, cmp.py)
- 节页范围核 (O20): p129 "6.1.6 Substance Use (SU)" (Description/Overview + spec 首句 + spec 表) → p130-131 (spec 续 + 脚注; Assumptions 1-4) → p132 (5; Examples Ex1 叙述 Row 1-7) → **p133 (su.xpt 表; 其后 6.2 Models for Events Domains)**. batch hi=132 **不全**, 实际完整范围 p129-133; 本域无节引言 NOTE.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | SU/assumptions.md:3-5 | ig34_p0129_a003 (REAL_GAP) | INSERTED | 新增 `## SU – Description/Overview` + 定义句逐字 (CM/CE 先例) | 129 |
| 2 | SU/assumptions.md:7-9 | spec 首句 (O17, 原 R4-blocked; 通用授权) | INSERTED | 新增 `## SU – Specification` + `su.xpt, Substance Use — Interventions. One record per substance type per reported occurrence per subject, Tabulation.` | 129 |
| 3 | SU/assumptions.md:11 | 结构 (CE/CM 先例) | INSERTED | 新增 `## SU – Assumptions` (PDF 原标题) | 131 |

- 覆盖率自查: atoms 1 = #1; census DIFF 0 / pdf_only 0 / unparseable 0; 授权/结构 2 (#2-3).

### census 表处理
- 本批 census 无 DIFF / pdf_only. su.xpt (examples.md:33) 对 p133 渲染图逐格人工复核 7 行 × 18 列: 0 差 (Row 1 SUSTDTC/SUENDTC 空、SUSTTPT/SUENTPT 2006-01-01; Row 3 SUENDTC 2003、SUSTTPT 2006-03-15 BEFORE; Row 6-7 NOT DONE + SUREASND 全文).

### PDF_TYPO 清单
- T-1 (p132 Ex1 Row 1 说明): PDF "SUENTTP = "2006-01-01"" 为笔误; 正确值由 PDF 自身确定 (spec p131 变量名 SUENTPT; 同页 Row 3 说明 "SUENTPT"; p133 表头 SUENTPT) → KB 保留 `SUENTPT` (examples.md:23), 不改.

### 双向全扫 (含表格原子)
- PDF→KB: p129 节首至 p133 6.2 前, 叙述/列表经规范化 (弯→直引号、合并换行、去 Markdown 记号) 词级 diff (`cmp.py`, 命令见下): assumptions 1-5 逐字一致; Examples 引言/列表/Not shown/Row 1-7 逐字一致, 仅余 T-1 与标题导航差 (`6.1.6 …`/`SU – Examples` ↔ `# SU — Assumptions`/`# SU — Examples`/`## Example 1`, 先例同). Ex1 su.xpt 逐格 0 差 (见上).
- KB→PDF: assumptions.md / examples.md 每行均有 PDF 出处; 无 KB 自写解释性内容 (无需 D6), 表前 `**su.xpt**` 为 PDF 表标题.
- 未改: 弯引号 ("Have you ever smoked tobacco?"、sponsor's、"Current") PDF 为弯引号, KB 直引号, 同 KB 全局惯例 (CE 先例未动).
- spec 表 (p129-131) 属 spec.md, 非白名单: 粗核 CDISC Notes 无可见差异 (KB 受控术语列用 C-code 为全局惯例); 归 O15 spec 全域扫描.

### 新增 atom 清单 (R3)
- 无 (叙述全扫未发现其他缺失).

### 删除清单
- 无删除.

### 范围外发现
- F-1: batch json pdf_ranges hi=132 漏 p133 (su.xpt 表页), 账本侧 O20 同类.

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SU_writer
P=.work/10_tier_b_repair/work/pdf_pages
(sed -n '1,7p' $P/ig34_p0129.txt; sed -n '/SU – Assumptions/,$p' $P/ig34_p0131.txt | grep -v '©\|^2021'; sed -n '1,3p' $P/ig34_p0132.txt) > $S/pdf_head.txt
python3 -I $S/cmp.py $S/pdf_head.txt knowledge_base/domains/SU/assumptions.md   # 仅标题/表头导航差
sed -n '/^SU – Examples/,$p' $P/ig34_p0132.txt | grep -v '©\|^2021' > $S/pdf_ex.txt
python3 -I $S/cmp.py $S/pdf_ex.txt <(sed '/^\*\*su.xpt/,$d' knowledge_base/domains/SU/examples.md)   # 仅标题差 + SUENTTP→SUENTPT (T-1)
for p in 129 132 133; do pdftoppm -f $p -l $p -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p$p; done
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat
```
 knowledge_base/domains/SU/assumptions.md | 10 ++++++++++
 1 file changed, 10 insertions(+)
```

## 主控勘误 (2026-11-26, 据 t2_B-SU_audit.md)
- T-1 位置: 上文与 `B-SU.writer.jsonl` 写的 `examples.md:23` 应为 `examples.md:19` (:23 为 Row 3); KB 值无误。
