# B-ch04 attempt 3 归档 (规则 B)

- 输入: attempt 2 终态 (md5 545883c1…) + auditor FAIL F1-F3 + 主控要求 p22-59 双向逐句扫描.
- 产物: `t2_B-ch04_attempt_3.patch` (= git diff 6fea563 -- ch04, 818 行; md5 `e11c6093560b572277b2bb5faa033b93`, +240/−168); checkpoint §attempt 3.
- 技术判定: reviewer a3 CONDITIONAL (t2_B-ch04_review_a3.md). writer 声明的改动全部成立; fp 回归 0, census DIFF 1 (T-1), live docs 42.
- 业务判定: 未过. reviewer 独立全扫另发现 HIGH 4 / MEDIUM 6 / LOW 13: 时长表数值错 (:814)、p28 MK 示例表整表缺、伪节号 4.2.1.1-4.2.1.3、--OBJ 决策树 Mermaid 分支与 PDF 图相反、未标注的 KB 自写表/句等.
- 根因: writer 正向扫描只覆盖 SENTENCE/LIST_ITEM/HEADING/CROSS_REF/NOTE, 漏了 TABLE_ROW/TABLE_HEADER/CODE_LITERAL; 反向扫描只看了改写过的段, 没扫全文件; census 看不到无 Row 列 / UNPARSEABLE 的表, 也没有对渲染人工逐格.
- 下一 attempt 输入: 不回滚, 在 md5 e11c6093… 基础上按修正清单 1-13 + H1-H4 修; 再做含表格原子的完整双向扫描 (全文件反向); 按 dispatch notes 末尾 3 条新口径 (表格原子全扫 / 伪节号 / Mermaid).
