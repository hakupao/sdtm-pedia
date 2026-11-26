# T1.4 R2 扫描: 全部 REWRITE_OK 是否属 '丢短语但别处有'

<!-- chain: E (plans) -->
> 生成: `scripts/helpers/t2_pkg.py` (2026-11-26) 读 `work/triage_merged.json` (含 `work/t1_rulings.json`); 只列 ID / 位置 / 计数, 不含 PDF 原文.

R2 (用户): 改写丢失短语, 即使同节上下文 / 同表行已有 → **REAL_GAP, 补回原文**.
判据: writer/reviewer 理由**承认** kb_loc 处缺某片段, 并用另一行 / 另一处 / 隐含 / 约定来开脱 →
片段是内容 (限定词 / 计数 / 术语 / 交叉引用) → FLIP (REAL_GAP); 只是标签、结构或 C02 型多行映射 → RECHECK (`t2_recheck=true`, T2 reviewer 回 PDF 定);
理由逐信息点给到 KB 行、未承认缺失 → KEEP. 97 条逐条人工判 (关键词 grep 只作辅助).
**注**: 标定集 C02 自身 (ig34_p0043_a012) 用 :894 覆盖 :898 缺的 'observation', 与 R2 有张力 → 列 RECHECK, 不在此裁; 请用户确认 C02 是否仍作 REWRITE_OK 标杆.

| # | atom_id | kb_loc | 判 | 理由 |
|--:|---|---|---|---|
| 1 | ig34_p0009_a026 | knowledge_base/chapters/ch01_introduction.md:85 | FLIP | 丢 'as noted in the table note' (指向表注的交叉引用) |
| 2 | ig34_p0010_a001 | knowledge_base/chapters/ch01_introduction.md:85 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 3 | ig34_p0010_a002 | knowledge_base/chapters/ch01_introduction.md:85 | KEEP | KB 多一个 'has' (增词非丢失, 意同) |
| 4 | ig34_p0010_a006 | knowledge_base/chapters/ch01_introduction.md:85 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 5 | ig34_p0010_a007 | knowledge_base/chapters/ch01_introduction.md:85 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 6 | ig34_p0010_a008 | knowledge_base/chapters/ch01_introduction.md:85 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 7 | ig34_p0010_a009 | knowledge_base/chapters/ch01_introduction.md:85 | RECHECK | 'Format' 小标题丢 (仅标签) |
| 8 | ig34_p0010_a010 | knowledge_base/chapters/ch01_introduction.md:86 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 9 | ig34_p0010_a011 | knowledge_base/chapters/ch01_introduction.md:87 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 10 | ig34_p0010_a012 | knowledge_base/chapters/ch01_introduction.md:87 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 11 | ig34_p0010_a013 | knowledge_base/chapters/ch01_introduction.md:87 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 12 | ig34_p0010_a015 | knowledge_base/chapters/ch01_introduction.md:87 | KEEP | URL 前加 'the NCI website' (增词) |
| 13 | ig34_p0011_a008 | knowledge_base/chapters/ch02_fundamentals.md:27 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 14 | ig34_p0011_a014 | knowledge_base/chapters/ch02_fundamentals.md:35 | FLIP | 数字 5 由行数隐含, 原文计数短语丢 |
| 15 | ig34_p0011_a015 | knowledge_base/chapters/ch02_fundamentals.md:39 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 16 | ig34_p0011_a017 | knowledge_base/chapters/ch02_fundamentals.md:41 | RECHECK | 'equivalent terms' 改写为 'for' |
| 17 | ig34_p0011_a018 | knowledge_base/chapters/ch02_fundamentals.md:42 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 18 | ig34_p0011_a019 | knowledge_base/chapters/ch02_fundamentals.md:43 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 19 | ig34_p0011_a022 | knowledge_base/chapters/ch02_fundamentals.md:48 | FLIP | 'study day of the start' 由引语隐含; 与 a020 同口径 (a020 用户裁 REAL_GAP) |
| 20 | ig34_p0011_a030 | knowledge_base/chapters/ch02_fundamentals.md:55 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 21 | ig34_p0012_a007 | knowledge_base/chapters/ch02_fundamentals.md:65 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 22 | ig34_p0012_a017 | knowledge_base/chapters/ch02_fundamentals.md:79 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 23 | ig34_p0012_a026 | knowledge_base/chapters/ch02_fundamentals.md:93 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 24 | ig34_p0012_a027 | knowledge_base/chapters/ch02_fundamentals.md:94 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 25 | ig34_p0012_a028 | knowledge_base/chapters/ch02_fundamentals.md:95 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 26 | ig34_p0013_a011 | knowledge_base/chapters/ch02_fundamentals.md:104 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 27 | ig34_p0013_a018 | knowledge_base/chapters/ch02_fundamentals.md:111 | FLIP | Define-XML 管理无数据 一句被移到同节 :102, 原位缺 |
| 28 | ig34_p0013_a023 | knowledge_base/chapters/ch02_fundamentals.md:128 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 29 | ig34_p0032_a014 | knowledge_base/chapters/ch04_general_assumptions.md:400 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 30 | ig34_p0032_a020 | knowledge_base/chapters/ch04_general_assumptions.md:414 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 31 | ig34_p0032_a024 | knowledge_base/chapters/ch04_general_assumptions.md:419 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 32 | ig34_p0042_a006 | knowledge_base/chapters/ch04_general_assumptions.md:856 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 33 | ig34_p0042_a008 | knowledge_base/chapters/ch04_general_assumptions.md:853 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 34 | ig34_p0042_a026 | knowledge_base/chapters/ch04_general_assumptions.md:875 | KEEP | 本原子在; :879 值差另记 O12 |
| 35 | ig34_p0043_a012 | knowledge_base/chapters/ch04_general_assumptions.md:898 | RECHECK | C02 型: 'observation' 由 :894 覆盖 (多行映射, R2 下待定) |
| 36 | ig34_p0043_a013 | knowledge_base/chapters/ch04_general_assumptions.md:899 | RECHECK | C02 型: 参考期由 :894 覆盖 |
| 37 | ig34_p0043_a014 | knowledge_base/chapters/ch04_general_assumptions.md:898 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 38 | ig34_p0043_a017 | knowledge_base/chapters/ch04_general_assumptions.md:899 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 39 | ig34_p0043_a023 | knowledge_base/chapters/ch04_general_assumptions.md:903 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 40 | ig34_p0044_a002 | knowledge_base/chapters/ch04_general_assumptions.md:909 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 41 | ig34_p0044_a003 | knowledge_base/chapters/ch04_general_assumptions.md:916 | RECHECK | 两种情形被压成一条限制说明 |
| 42 | ig34_p0044_a004 | knowledge_base/chapters/ch04_general_assumptions.md:911 | RECHECK | C02 型: 排除 AFTER 在 :916 另行 |
| 43 | ig34_p0044_a008 | knowledge_base/chapters/ch04_general_assumptions.md:916 | RECHECK | C02 型: AFTER 有效条件在 :916 另行 |
| 44 | ig34_p0044_a013 | knowledge_base/chapters/ch04_general_assumptions.md:927 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 45 | ig34_p0044_a014 | knowledge_base/chapters/ch04_general_assumptions.md:927 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 46 | ig34_p0044_a015 | knowledge_base/chapters/ch04_general_assumptions.md:927 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 47 | ig34_p0045_a002 | knowledge_base/chapters/ch04_general_assumptions.md:947 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 48 | ig34_p0045_a003 | knowledge_base/chapters/ch04_general_assumptions.md:947 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 49 | ig34_p0045_a004 | knowledge_base/chapters/ch04_general_assumptions.md:947 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 50 | ig34_p0045_a016 | knowledge_base/chapters/ch04_general_assumptions.md:957 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 51 | ig34_p0045_a017 | knowledge_base/chapters/ch04_general_assumptions.md:957 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 52 | ig34_p0071_a002 | knowledge_base/domains/DM/examples.md:180 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 53 | ig34_p0115_a030 | knowledge_base/domains/EX/examples.md:243 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 54 | ig34_p0121_a005 | knowledge_base/domains/ML/spec.md:3 | RECHECK | 数据集标题行 'ml.xpt … Tabulation' 由文件约定隐含 (同 R4 受阻 5 条标题行, 待用户) |
| 55 | ig34_p0139_a010 | knowledge_base/domains/AE/assumptions.md:39 | RECHECK | KB 把 '…/etc.' 扩写成 6 项 (O11, 超出 PDF) |
| 56 | ig34_p0151_a0013 | knowledge_base/domains/CE/examples.md:13 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 57 | ig34_p0151_a0015 | knowledge_base/domains/CE/examples.md:14 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 58 | ig34_p0151_a0017 | knowledge_base/domains/CE/examples.md:15 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 59 | ig34_p0151_a0019 | knowledge_base/domains/CE/examples.md:16 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 60 | ig34_p0152_a0004 | knowledge_base/domains/CE/examples.md:43 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 61 | ig34_p0152_a0005 | knowledge_base/domains/CE/examples.md:43 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 62 | ig34_p0152_a0006 | knowledge_base/domains/CE/examples.md:43 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 63 | ig34_p0152_a0007 | knowledge_base/domains/CE/examples.md:44 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 64 | ig34_p0152_a0008 | knowledge_base/domains/CE/examples.md:44 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 65 | ig34_p0152_a0009 | knowledge_base/domains/CE/examples.md:44 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 66 | ig34_p0152_a0010 | knowledge_base/domains/CE/examples.md:45 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 67 | ig34_p0152_a0011 | knowledge_base/domains/CE/examples.md:45 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 68 | ig34_p0152_a0012 | knowledge_base/domains/CE/examples.md:45 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 69 | ig34_p0152_a0014 | knowledge_base/domains/CE/examples.md:46 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 70 | ig34_p0152_a0015 | knowledge_base/domains/CE/examples.md:46 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 71 | ig34_p0153_a0001 | knowledge_base/domains/CE/examples.md:70 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 72 | ig34_p0153_a0006 | knowledge_base/domains/CE/examples.md:77 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 73 | ig34_p0153_a0007 | knowledge_base/domains/CE/examples.md:77 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 74 | ig34_p0153_a0008 | knowledge_base/domains/CE/examples.md:77 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 75 | ig34_p0153_a0009 | knowledge_base/domains/CE/examples.md:77 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 76 | ig34_p0153_a0011 | knowledge_base/domains/CE/examples.md:79 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 77 | ig34_p0153_a0012 | knowledge_base/domains/CE/examples.md:79 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 78 | ig34_p0153_a0013 | knowledge_base/domains/CE/examples.md:79 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 79 | ig34_p0153_a0016 | knowledge_base/domains/CE/examples.md:80 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 80 | ig34_p0153_a0018 | knowledge_base/domains/CE/examples.md:81 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 81 | ig34_p0153_a0019 | knowledge_base/domains/CE/examples.md:81 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 82 | ig34_p0153_a0022 | knowledge_base/domains/CE/examples.md:82 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 83 | ig34_p0153_a0023 | knowledge_base/domains/CE/examples.md:83 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 84 | ig34_p0153_a0024 | knowledge_base/domains/CE/examples.md:83 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 85 | ig34_p0153_a0025 | knowledge_base/domains/CE/examples.md:83 | KEEP | CRF / 表格多行合并为单行, 各值与对应关系在 |
| 86 | ig34_p0367_a013 | knowledge_base/domains/FA/examples.md:14 | RECHECK | 4 行合并为 1 行, 症状-选项对应靠顺序 |
| 87 | ig34_p0367_a016 | knowledge_base/domains/FA/examples.md:17 | RECHECK | 4 行合并为 1 行, 症状-选项对应靠顺序 |
| 88 | ig34_p0367_a019 | knowledge_base/domains/FA/examples.md:20 | RECHECK | 4 行合并为 1 行, 症状-选项对应靠顺序 |
| 89 | ig34_p0374_a011 | knowledge_base/domains/FA/examples.md:264 | RECHECK | KB 表头 6 列 / 数据行 9 列, 表格不齐 |
| 90 | ig34_p0397_a003 | knowledge_base/domains/TA/examples.md:498 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 91 | ig34_p0397_a004 | knowledge_base/domains/TA/examples.md:498 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 92 | ig34_p0398_a010 | knowledge_base/domains/TA/examples.md:566 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 93 | ig34_p0398_a017 | knowledge_base/domains/TA/examples.md:566 | KEEP | 信息点逐一映射到 KB 行, 未承认缺失 |
| 94 | sv20_p0005_a004 | knowledge_base/model/01_concepts_and_terms.md:102 | KEEP | T1.3 reviewer: 信息点全在 model/01:102 |
| 95 | sv20_p0008_a004 | knowledge_base/model/01_concepts_and_terms.md:7 | FLIP | 丢 '(see Concept Map, below)' 交叉引用 |
| 96 | sv20_p0009_a016 | knowledge_base/model/01_concepts_and_terms.md:65 | RECHECK | 括号内概念示例被具体变量例替换 |
| 97 | sv20_p0009_a019 | knowledge_base/model/01_concepts_and_terms.md:86 | RECHECK | 'described in Section 2.2' 交叉引用因所在即 2.2 而略 |

合计: 97 条 → FLIP 5 / RECHECK 15 / KEEP 77. 另 4 条 pending_user (ig34_p0010_a023 / p0011_a020 / p0012_a005 / p0056_a006) 按 R2 定为 REAL_GAP (R2-ack).
