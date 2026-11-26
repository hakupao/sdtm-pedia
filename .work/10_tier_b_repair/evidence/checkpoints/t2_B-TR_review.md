# T2 B-TR reviewer verdict

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**VERDICT: PASS** (0 缺陷; T-1..T-3 成立; T-4 裁定 = PDF 忠实状态, KB 保持空, 仅登记)

- base 97e1895; KB md5 复核: TR/examples.md `415debd69c524ff5ee855b89f4f44df4` / TR/assumptions.md `c4f681f0e281e9eb2ac41e5219ba2c79` (= writer 报告)
- 范围: 只审 TR (LB/MB diff 属并行批). TR diff 只涉及 TR/examples.md (白名单内); 标题/锚点未变; delete_only_source_lines 为空.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-TR_reviewer/` (p-355..358.png 150dpi, L355-358.txt layout, chk.py)

### 命令与结果 (可复跑, 仓库根)
```
S=<scratch>; P="source/cdisc/SDTMIG v3.4 (no header footer).pdf"
pdftoppm -f 355 -l 358 -r 150 -png "$P" $S/p           # 渲染图逐格人工核
for p in 355 356 357 358; do pdftotext -layout -f $p -l $p "$P" $S/L$p.txt; done
python3 -I $S/chk.py $S    # 独立方法: layout 行块词多重集 vs KB 行 (连字符折行配对), 非 bbox 分列
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json  # exit 1
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
python3 tools/check_links.py | tail -1
```
- census: TR 表 :15 UNPARSEABLE(未触碰) / :17 DIFF 32 / :51 OK / :68 DIFF 1 / :107 OK. 32 = 16 行 × (Row,TRSEQ) 全 T-1; 1 = :84 TRSTRESC -50 vs PDF -60 (T-2).
- chk.py 残差 (layout 方法, 独立于 bbox): Ex3 32/32 行仅 row15 `-50/-60` (T-2) + 页脚日期噪声; Ex2 27/27 行仅 Row/TRSEQ 偏 1 (T-1) + row25 `IMAGE QUALITY` vs `IMAGEQUALITY` (T-3). 其余每词一一对上.
- fp_match: RESULT RED, 11 条回归全为 ig34_p0257-0263 (MB, 别批); TR 0 条.
- check_links: live docs 42 (基线 42).

### 人工逐格 (渲染图 p355-358) — 列序与每格
| 表 | 结果 |
|---|---|
| Ex2 tr.xpt 表头 | 一致 (TRREASND; 列序 ...TRSTAT TRREASND TRMETHOD TREVAL VISITNUM VISIT TRDTC TRDY) |
| Ex2 行 1-11 (PDF 1-11) | 一致 (含 行3 2010-01-02/-2, 行7 -3, 行8 -2, 行6 "Non Lymph") |
| Ex2 行 12-27 (PDF 13-28) | 除 Row/TRSEQ (T-1) 外一致; 行14-19 VISIT=WEEK 6, TRDTC/TRDY 空; 行24/25 无日期; 行25 TRREASND "NOT ASSESSABLE: POOR IMAGE QUALITY" (p355 底 + p356 顶续行) |
| Ex2 行 26 (PDF 27) | TRORRES..TRSTRESU 空, TRSTAT 空, TRREASND 空, CT SCAN, INVESTIGATOR, 60, WEEK 12, 2010-04-02, 88 — 一致 |
| Ex3 tr.xpt 表头 | 一致 (TRNAM 在 TRMETHOD 前) |
| Ex3 行 1-32 | 逐格一致 (TRNAM 全 ACE IMAGING; TRMETHOD: 1 MRI,2-3 CT,4-5 空,6 CT,7 MRI,8 MRI,9-10 CT,11-16 空,17 CT,18 MRI,19 CT,20 MRI,21-22 CT,23-28 空,29 CT,30 MRI,31 CT,32 MRI); 唯一差 行15 TRSTRESC (T-2) |
| Ex3 relrec.xpt + 引句 | 一致 (p358 "The relationship between the TU and TR records is represented in RELREC.") |

### 指定核查
1. Ex3 重建 28→32: 渲染图 + layout 词多重集双法核, 32 行全对; TRNAM/TRMETHOD 互换正确.
2. 旧 KB 行 20 (R1-NEW01 DIAMETER 7 mm, TRDY 55): PDF p356-358 无任何 R1-NEW01 DIAMETER 行, 无 TRDY 55; PDF 行 20 = R1-T01 DIAMETER 7 mm MRI 2010-04-02 88 (旧 KB 把 A3 值错位). 删除正确.
3. PDF_TYPO: T-1 成立 (PDF 叙述 p354 "Rows 9-21"/"Rows 22-27" 与连续编号一致, 表跳 12); T-2 成立 (同行 TRORRES -50 / TRSTRESN -50, 仅 TRSTRESC -60); T-3 成立 (p356 续行文字层 "POOR IMAGEQUALITY", 渲染亦连写).
4. **T-4 裁定: PDF 忠实状态, KB 保持空 (不恢复 NOT DONE).** 依据: p356 顶 "POOR IMAGEQUALITY" 位于表头下一独立续行格, 承接 p355 行 26 "NOT ASSESSABLE:" (冒号续接), 属行 26 TRREASND; 行 27 本行 TRSTAT/TRREASND 格为空. 旧 KB "NOT DONE / POOR IMAGE INEQUALITY" 是抽取时把续行误挂到行 27 的产物, 非 PDF 值, 无"合理值"可保留. 该行有 CT SCAN + 日期 + TRDY 88 (与已执行评估行同型, NOT DONE 行均无日期), 若 PDF 有疏漏也是 TRORRES/TRSTRESC 缺值 (值不可知, 不可臆造). → 登记 T-4 "PDF 疑漏 TRORRES/TRSTRESC; KB 照 PDF 空", 不改 KB.
   精确格值 (KB :44): `| 26 | ABC | TR | 44444 | 26 | NON-TARGET | A3 | NT01 | TUMSTATE | Tumor State | | | | | | | | CT SCAN | INVESTIGATOR | 60 | WEEK 12 | 2010-04-02 | 88 |`

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | 1-6 | 无 | — |

### G-TB6 结构行签字
- :17 Ex2 表头 (改 TRREASND) — PDF p355 表头, 签字.
- :68-69 Ex3 表头/分隔线 — PDF p356 表头, 签字.
- :102 空行, :103 引句 (PDF p358 原句), :105 `**relrec.xpt**`, :107-108 relrec 表头/分隔线 — 签字.
- 新增/改动数据行 Ex2 14 行 + Ex3 32 行 + relrec 2 行, 无出处行 0.
- KB_AUTHORED :3 Note / "(continued from TU)" 未改动, 纯导航不矛盾, 保留.

### R2 recheck
- t2_recheck 为空, 无.
