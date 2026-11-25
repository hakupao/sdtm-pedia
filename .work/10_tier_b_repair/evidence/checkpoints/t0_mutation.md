# T0.4 闸的变异验证 (G-TB9) — checkpoint

> 状态: **PASS, 等用户 ack (hard checkpoint)** (2026-11-25); 执行: `oh-my-claudecode:executor` (opus)
> 规则: retrospective §4 规则 5 (变异验证). 只改 `work/scratch/knowledge_base/` (KB 临时副本, gitignored); 真 KB / archive / releases 未动.
> 完整输出: `evidence/checkpoints/t0_mutation.log` (下方为摘录)

## 0. 复跑命令 (干净 checkout 也能从头跑)

所有命令都在仓库根目录 (`/Volumes/DevSSD/Project/sdtm-pedia`) 运行; 需要本地有 `source/cdisc/` 下的 PDF (gitignored) 和 `pdftotext` (poppler).

```bash
T=.work/10_tier_b_repair
# (1) T0.2 工作副本 (pdf/md_atoms 两份副本是 gitignored 的, 与 archive 原件 md5 一致, 见 _progress.json md5)
cp archive/deep_verification/coverage_ledger.jsonl $T/work/coverage_ledger.wc.jsonl
cp archive/deep_verification/pdf_atoms.jsonl archive/deep_verification/md_atoms.jsonl $T/work/
# (2) T0.3 页文本缓存 + 页码抽查 (断言 461 / 74 页)
python3 -I $T/scripts/t0_pdf_pages.py
# (3) 基线 (在真 KB 上生成)
python3 -I $T/scripts/t3_recompute.py --check-against archive/deep_verification/section_coverage.jsonl   # 399 行 0 差异, exit 0
cp $T/work/section_coverage.wc.jsonl $T/work/section_coverage.wc.baseline.jsonl
python3 -I $T/scripts/fp_match.py --out $T/work/fp_baseline.jsonl
python3 -I $T/scripts/table_census.py --pages ig34:275-284 \
  --kb knowledge_base/domains/PC/examples.md knowledge_base/domains/PP/examples.md knowledge_base/domains/PC/assumptions.md \
  --out $T/work/census_BPCPP.json        # exit 1: 基线本身就有 DIFF (Issue 5 等), 属预期
# (4) 范围外探测 (§4 用到)
python3 -I $T/scripts/table_census.py --pages ig34:272-275 --kb knowledge_base/domains/PP/examples.md \
  --out $T/work/scratch/census_p272_275.json
# (5) 变异 M0..M3 + 复原 (约 2 分钟)
bash $T/scripts/t0_mutation.sh > $T/evidence/checkpoints/t0_mutation.log 2>&1
```

红 / 绿的定义: 与**基线**相比有变化 → 退出码 1, 输出 `RESULT: RED`; 无变化 → 退出码 0, 输出 `GREEN`.
基线本身不干净 (ledger 过期; §5.0 范围 1,459 个 gap 原子, 其中现行 142 节的 1,389 个里 PARTIAL 占 1,312; B-PCPP 表有 42 处 DIFF),
所以"0 发现"不能当绿的判据, 只看相对基线的变化.
`t3_recompute` 只读 ledger, 它变红靠的是这条链: `fp_match --regress-out` 输出回退原子 → `t3_recompute --downgrade` 把这些原子在内存里从 EXACT/EQUIVALENT 降为 MISSING → 与基线 diff. 没有手改 ledger.

## 1. 结果矩阵 (退出码)

| 变异 | 内容 | fp_match | table_census | t3_recompute | 预期 | 判定 |
|---|---|:-:|:-:|:-:|---|---|
| M0 | 未改动的副本 (副本 md5 = 真 KB md5 `5ae88550…`) | 0 | 0 | 0 | 全绿 | PASS |
| M1 | 删 1 句 prose: `ch01_introduction.md` 中原子 `ig34_p0008_a022` (EXACT, 文件内唯一) | **1** | 0 | **1** | fp 红 | PASS |
| M2 | 改 1 个表格值 (单行记录, `columns` 模式): `PC/examples.md:78` Ex1 Method C row 5 IDVARVAL `4`→`9` | 0 | **1** | 0 | census 红 | PASS |
| M2b | 把值挪进相邻空格子: `PC/assumptions.md:31` relrec row 1, `MANY` 从 RELTYPE 挪到 IDVARVAL | 0 | **1** | 0 | census 红 | PASS |
| M2c | 改 1 个值 (PDF 折行记录, `multiset` 模式): `PC/assumptions.md:69` pc.xpt row 13 PCORRES `10`→`11` | 0 | **1** | 0 | census 红 | PASS |
| M2d | 删 KB 表的 1 行: `PC/examples.md:119` Ex1 Method D row 20 | 0 | **1** | 0 | census 红 | PASS |
| M3 | 删 1 个子节: `ch04_general_assumptions.md` `#### 4.5.1.2 Tests Not Done` (第 1171-1207 行) | **1** | 0 | **1** | fp + t3 红 | PASS |
| RESTORE | 重新复制未改动的 KB | 0 | 0 | 0 | 全绿 | PASS |

**G-TB9: 计划要求的 3 项变异 (M1 / M2 / M3) 都按预期变红, 另加的 3 项表格变异 (M2b-d) 也都变红; 复原后全绿.**
前后真 KB md5 都是 `5ae88550adcecaf3c9349233f7fa07fc`; `git status --short knowledge_base archive releases` 为空.

## 2. 关键输出摘录

```
[M1] BASELINE …fp_baseline.jsonl: regressions=1 new_hits=0
       REGRESS ig34_p0008_a022 EXACT §1.4 [How to Read this Implementation Guide]
[M1] downgraded EXACT/EQUIVALENT -> MISSING (fp regression): 1
     DIFF ('ig34', '§1.4 [How to Read this Implementation Guide]') {'coverage_density': (0.7333, 0.6667), 'tb_residual_gap': (4, 5), …}
[M2]  CHANGED knowledge_base/domains/PC/examples.md 72 DIFF [{'row': 5, 'mode': 'columns', 'kb_only': ["col6='9'"], 'pdf_only': ["col6='4'"]}]
[M2b] CHANGED knowledge_base/domains/PC/assumptions.md 29 DIFF [{'row': 1, 'mode': 'columns', 'kb_only': ["col6='MANY'", "col7=''"], 'pdf_only': ["col6=''", "col7='MANY'"]}]
[M2c] CHANGED knowledge_base/domains/PC/assumptions.md 55 DIFF [{'row': 13, 'mode': 'multiset', 'kb_only': ['11'], 'pdf_only': ['10']}]
[M2d] CHANGED knowledge_base/domains/PC/examples.md 98 DIFF [{'row': 20, 'kb_only': [], 'pdf_only': 'ROW'}]
      (另有 11 条 CHANGED 只是删行后后面表格的行号整体前移 1, 状态与 diff 不变)
[M3] BASELINE …: regressions=23 new_hits=0   (ig34_p0052_a005..; 全部 §4.5.1.2)
[M3] downgraded EXACT/EQUIVALENT -> MISSING (fp regression): 23
     DIFF ('ig34', '§4.5.1 […]')        {'aggregate_verdict': ('FULL_COVERAGE', 'SIBLING_DROPPED')}
     DIFF ('ig34', '§4.5.1.2 [Tests Not Done]') {'aggregate_verdict': ('FULL_COVERAGE', 'SKELETON_ONLY'),
          'coverage_density': (1.0, 0.1481), 'tb_g1_pass': (True, False), 'tb_g2_pass': (True, False), 'tb_residual_gap': (0, 23)}
```

## 3. 闸已知的盲区 (T2 reviewer 要知道)

1. **M2 中 fp_match 没变红**: 被改的 relrec 行在 KB 里有完全相同的副本 (Ex2 Method C、`PP/examples.md:167`),
   指纹在目标文件里照样能命中. 表格值只能靠 census 守 (B8 / G-TB4), 不能靠 fp_match.
2. fp_match 只能检出"在基线里命中、现在没命中"的原子. 本来就不是逐字的 EQUIVALENT (改写过的) 原子删掉后它看不到 → 要靠 T3.2 的 G-TB6 git-diff 反向溯源和 reviewer.
3. 同一句话在同一个文件出现两次时, 删掉一次不会变红 (M1 特意选了文件内唯一的句子).
4. census 有三种比对模式 (每张表的 `row_modes` 里有计数):
   - `columns`: 单行记录, 表头也是单行. 按表头 x 坐标把值分到列里, **逐格比, 空格子也比** (M2 / M2b 证明有效). B-PCPP 中所有 relrec 表、pp.xpt (p277) 都走这个模式.
   - `order`: 单行记录, 但表头列数对不上. 只按 token 顺序比, **空格子不可见**, 值挪到相邻空格子检不出. B-PCPP 范围内没有这种行 (columns 292 行 / multiset 35 行 / order 0 行).
   - `multiset`: PDF 折行记录 (pc.xpt p276, §6.3.5.9.2 pp.xpt p275). 按 token 多重集比 (M2c 证明值改动能检出); **同一行里两个值互换、值挪进空格子都检不出**,
     也分不清哪一列错 (例如 pc.xpt 只能看出"某个 PCGRPID 列"错). 这些行 reviewer 要按列人工核.
5. census 按内容配对 KB 表和 PDF 表. KB 表整体抄错时可能配到另一张相似的表上 (见 §4 的 PP Ex1). 结果仍是红, 但 DIFF 明细要人工看.
6. census 只比表, 不比表前的说明文字. 说明文字和表互相矛盾 (例如 §4 的 Ex1 Method B) 它看不到.

## 4. T0.3b census 试跑 (p275-284, B-PCPP) 顺带发现 (只记录, T1/T2 处理)

命令: 见 §0 (3) 最后一条; 输出 `work/census_BPCPP.json`.
- 解析: PDF 18 张表**全部解析并配对**, 本范围内没有 PDF_UNPARSED, 也没有 PDF_ONLY; 比对了 3,551 个格子 (只算页码范围内的行, 含空格子).
  KB 24 张表: OK 13 / DIFF 7 / NO_PDF 3 (§6.3.5.9.2 在 p272-274 的表, 超出范围) / UNPARSEABLE 1 (`PP/examples.md:135` "Method label mapping", KB 自建的表, 没有 Row 列, PDF 里没有对应表).
- 范围外探测 (§0 (4)): p274 有 2 张单元格垂直居中的表 (§6.3.5.9.2 Ex2 的 pp.xpt 与 QNAM/QVAL 补充限定表), 判为 PDF_UNPARSED, **须人工逐格核对**.
- DIFF 明细 (共 42 处):
  - **KB 值错 (VALUE_DIFF 候选)**:
    - `PC/assumptions.md:55` pc.xpt 13 行: 某个 PCGRPID 列 `DY1_DRGX` 与 PDF `DY1_DRGX_A` / `_D` 不符; 时间如 09:00, PDF 为 09:20.
    - `PC/assumptions.md:86` pp.xpt 12 行: PPSEQ 和 PPGRPID (Example 4) 两列整列错位. `PP/examples.md:112` 里的同一张表是对的.
    - `PC/examples.md:236` Ex3 Method A row 3: KB 写 `DYIDRGX_A` (字母 I), PDF 为 `DY1DRGX_A`.
    - `PP/examples.md:87` (§6.3.5.9.2 Ex3): PPRFTDTC 11 行, KB 写 `2001-02-25T08:00`, PDF 为 `2001-02-01/15T08:00`; row 7 KB 写 `L/h`, PDF 为 `L/hr`.
    - `PP/examples.md:87,112` 表头: KB 写 `PPRFDTC`, PDF 为 `PPRFTDTC`.
  - **PDF 自身疑似笔误 (PDF_TYPO 候选, KB 合理)**:
    - p277 Ex1 Method A row 3: PDF 写 `PC … PPGRPID DY8_DRGX`, KB 写 PCGRPID.
    - p278 Ex1 Method B row 13 / 26: PDF 写 RDOMAIN `PC` 配 `PPGRPID`, KB 写 PP.
  - **PDF 前后自相矛盾 (census 看不到, 人工发现)**: p277 的说明文字写 "Rows 14-26: … RELID "2" … PPGRPID = "DY8DRGX"",
    但 p278 的表里 row 14-26 是 RELID 1, row 26 是 DY1DRGX. KB 两处都照抄了, 所以 census 是绿的. 记为 PDF_TYPO 候选.
- **范围外的大发现**: `PP/examples.md:16` (§6.3.5.9.2 Example 1, 24 行) 的内容更像 PDF 的 Example 3 (DRUGA_DAY1, 0.65 …), 而 PDF p273 的 Example 1 (DAY1_PAR, 1.87 …) 在 KB 里没有配上 (PDF_ONLY). 疑似整表放错或抄错, T1 要列入.
- Issue 5 的 "143" 仍无法复现. census 给出的确定性数字是: B-PCPP 范围内 42 处 DIFF, 其中表头 2 处、PDF_TYPO 候选 3 处.

## 5. 补丁: 预期表断言 (verifier nit #1, 用户 ack 附带要求) — 2026-11-25T13:47Z

- `scripts/t0_mutation.sh` 加 `expect()` 预期表 (fp census t3 退出码): M0/RESTORE `0 0 0`; M1/M3 `1 0 1`; M2/M2b/M2c/M2d `0 1 0`.
  每个变异实际退出码与预期不符 → 记 MISMATCH; 末尾打印预期表, 有不符 `exit 1`, 全符 `exit 0`. (bash 3.2 无关联数组, 用 case 函数.)
- 复跑: `cd /Volumes/DevSSD/Project/sdtm-pedia && bash .work/10_tier_b_repair/scripts/t0_mutation.sh > .work/10_tier_b_repair/evidence/checkpoints/t0_mutation_v2.log 2>&1; echo $?`
  → **exit 0**, 完整 log `evidence/checkpoints/t0_mutation_v2.log` (原 `t0_mutation.log` 保留不覆盖). 末段:

```
M0       expect=[0 0 0] got=[0 0 0] OK
M1       expect=[1 0 1] got=[1 0 1] OK
M2       expect=[0 1 0] got=[0 1 0] OK
M2b      expect=[0 1 0] got=[0 1 0] OK
M2c      expect=[0 1 0] got=[0 1 0] OK
M2d      expect=[0 1 0] got=[0 1 0] OK
M3       expect=[1 0 1] got=[1 0 1] OK
RESTORE  expect=[0 0 0] got=[0 0 0] OK
MUTATION RESULT: ALL MATCH (exit 0)
```
- 断言本身的反向验证: 取脚本第 18-19 行 (`expect()` + 计数器) 套最小 harness, 喂 `M2 got="0 0 0"` (模拟 census 失明) → `mismatch detected`, exit 1. 真 KB md5 前后均 `5ae88550…`.
