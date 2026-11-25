# Tier B 修复 — 基线清单 (T0 inventory)

> 状态: T0 基线已出 (2026-11-25), 只读分析, 未改 `knowledge_base/` / `archive/`
> 复跑命令 (两步, 结果确定性):
> ```bash
> git show f024a3f:branches/06_deep_verification/section_coverage.jsonl > /tmp/sc_p4b_orig.jsonl
> python3 -I .work/10_tier_b_repair/scripts/t0_inventory.py /tmp/sc_p4b_orig.jsonl
> ```
> 产物: `inventory.jsonl` (173 行, 每节一行, 含 gap 原子 id) + `inventory_table.md` (逐节表)
> inventory.jsonl md5 (本次): `0e2248fda1fad6d87e6803ee2b225748`

## 1. 56 / 110 核对结论

| 数据版本 | SIBLING_DROPPED | CONTENT_TRUNCATED | 合计 | 出处 |
|---|--:|--:|--:|---|
| P4b 原始 (commit `f024a3f`, P6 T5 之前) | **56** | **110** | 166 | RETRO 缺口 3 / P6 plan 引用的就是这一版 |
| 现行 `archive/deep_verification/section_coverage.jsonl` (v1.4 C1 重跑, 2026-05-22) | **49** | **93** | 142 | 本次用同脚本 + 现 ledger 重跑, 去掉 `aggregated_by` 字段后 399 行全等 |
| 现行 failure_patterns (一节可多标签) | 66 | 114 | — | 不是 aggregate verdict, 别混用 |

- **56/110 数字本身正确, 但已过时**: 它是 P6 T5 改 ledger 前的快照. v1.4 C1 已结算 T5, 现行是 **49/93 = 142 节**.
- 原 166 节去向: 133 仍 Tier B (CT→CT 86, SD→SD 47) + 2 SD→CT; 31 节已升级 (→FULL 18 / →MOSTLY 13);
  另有 7 节由原 SKELETON_ONLY 降入 Tier B (→CT 5, →SD 2). 并集 173 节, 全部列入 `inventory.jsonl`.
- **坑**: `section_id` 不唯一 (399 行只有 308 个 id), 必须用 `(source, section_key)` 作键. 本清单另发 `tb_id` (TB-001..173) 作稳定键.

## 2. 现行 142 节的原子画像

| 指标 | 值 | 说明 |
|---|--:|---|
| 节数 (ig34 / sv20) | 142 (121 / 21) | |
| 非 HEADING 内容原子 | 5,721 | |
| gap 原子 (ledger 非 EXACT/EQUIVALENT/IE) | **1,389** | PARTIAL 1,312 / MISPLACED 43 / ERROR 21 / MISSING 13 |
| gap 按类型 | TABLE_ROW 775 / SENTENCE 270 / LIST_ITEM 142 / CODE_LITERAL 92 / TABLE_HEADER 63 / NOTE 22 / CROSS_REF 13 / FIGURE 12 | |
| 指纹探针: verbatim 已在目标文件 | 299 | 归一化后子串命中 (≈ ledger 标签过期) |
| 指纹探针: verbatim 在 KB 任意处 | 445 | 含错位到别的文件 |
| 指纹探针: KB 中无 verbatim | **944** | **上界**, 不是缺失数 (见下) |
| 944 再拆: spec 表行 / prose / 其他 | 452 / 240 / 252 | spec 行 = 域 Specification 表 (KB 由 xlsx 生成 spec.md, 结构不同) |
| 含"无 verbatim prose"的节 | 52 | 真实补写的主战场 |
| 去 IE 后密度 ≥ 0.80 的节 | 47 / 142 | p4b 密度分母含 IE, 系统性压低 |
| SIBLING_DROPPED 且自身 0 内容原子 | 21 | 只能靠子节修好来消 |
| 无目标文件 (md_target_files 空) | 27 | 21 个纯结构父节 + 6 个需定位 |

**关键判断**:
1. ledger 不是修复清单. PARTIAL 标签来自 P4a LLM 匹配, P7 抽样 60 条里 31 条标签错; `md_atoms.jsonl` 早于 T4b Wave 1-3、v1.3、v1.4 C4 的 KB 改动. 例: TB-043 §4.4.7 (--STRF/--ENRF) KB 里存在, 但被改写成表格 + 合并段落 → 探针判"无 verbatim", 实为**改写**, 是否丢信息要逐句裁决.
2. 944 里 452 条是域 spec 表行, 按 P6 T2 Round 2 先例 (SPEC_TABLE_ROW 747 条已 IE) 大概率归 IE 候选, 需用户 ack.
3. 真正要补写的量要等 T1 分诊后才知道; 目前只能给区间 (见 PLAN §7).

## 3. 按修复目标分组 (批次划分依据)

| 分组 (主目标文件) | 节 | gap 原子 | 探针缺 | 备注 |
|---|--:|--:|--:|---|
| chapters/ch04_general_assumptions.md | 22 | 235 | 126 | 最大单文件, 拆 2 批串行 |
| chapters/ch02_fundamentals.md | 8 | 76 | 57 | |
| chapters/ch01_introduction.md | 5 | 54 | 53 | |
| chapters/ch08_relationships.md | 7 | 46 | 36 | |
| chapters/ch03_submitting_data.md | 1 | 50 | 1 | 多为标签过期 |
| model/03,04,05,02 (sv20) | 14 | 50 | 48 | 4 文件 1 批 |
| domains/* (39 个域目录) | 58 | 792 | 619 | 前 8 域占 364: AE 68 / CP 60 / EG 50 / CV 41 / NV 39 / ML 37 / MI 37 / CE 32 |
| (未定位 / 纯结构父节) | 27 | 86 | 4 | 随子节消; 6 节需 T1 定位 |

逐节明细见 `inventory_table.md`.

## 4. Issue 5 (§6.3.5.9.3 PP-PC) 的 143

`issues_found.md` Issue 5 记 "143 TABLE_ROW data-value 差异", **用现行数据复现不出 143**. 现行 §6.3.5.9.3 各节:

| 节 | 现 verdict | 原子 | PARTIAL | MISPLACED |
|---|---|--:|--:|--:|
| 主节 | STRUCTURE_DRIFTED (不在 Tier B 名单) | 75 | 0 | 13 |
| Example 1 / 2 | FULL_COVERAGE | 100 / 50 | 0 | 0 |
| Example 3 | CONTENT_TRUNCATED | 84 | 62 | 0 |
| Example 4 | CONTENT_TRUNCATED | 88 | 20 | 0 |
| Conclusions | FULL_COVERAGE | 1 | 0 | 0 |

现可数 82 PARTIAL + 13 MISPLACED = 95. 143 可能来自 T4 Tier A 时的另一口径 (trace 第 180 行只给数字没给清单). 处理: PLAN 设独立批次 B-PCPP, 不靠 143 这个数, 按 PDF p275-284 做整表逐格核对 (PC/examples.md + PP/examples.md + PC/assumptions.md).

## 5. 范围外但相关 (仅记录)

- 现行仍显示 SKELETON_ONLY 46 / STRUCTURE_DRIFTED 23 — Tier A 声称已修, 但 ledger 没随 KB 刷新, 所以 p4b 还报旧状态. 本项目 T3 刷新工作副本 ledger 时会顺带结算, 不另开修复.
