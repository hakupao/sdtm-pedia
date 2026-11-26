# T2 B-VS writer checkpoint — attempt 1 (2026-11-26)

- base HEAD: `78c859fa3a7cd7c47b16a5ac22fffe5e1074666b`
- md5 before: VS/assumptions.md `f60ee4b93ab75845f3e6c69c9d9d77d2`; VS/examples.md `89be8a4ae1613e0d6d0b7b4d9cdb77f1`; VS/spec.md `a1508c13e384645e734e7deba4dce430` (未动)
- md5 after: VS/assumptions.md `27431c96a12ffc693bda4963f852b70e`; VS/examples.md `2832480cc18de5bd4c1560d8f5ee1ede`
- 范围: batch kb_files = VS/examples.md; 主控授权追加 VS/assumptions.md (仅 Description/Overview + spec 首句, 按 CM 先例)
- pdf_ranges 核对 (O20): VS §6.3.13 起于 p358 (TR 表尾之后), Description/Specification 在 p358, spec 表 p358-360, Assumptions/Examples p360, Ex1 表跨 p360-361, p361 中部起 §6.4 FA. batch pdf_ranges 358-361 覆盖整节, 无漏页.
- 真值: `work/pdf_pages/ig34_p0358..0361.txt` + pdftoppm 渲染 (p360 右侧 VSDTC..VSTPTNUM 列; p361 全表左右两段) 逐格目视.

## 变更清单
| # | kb_file:line (改后) | ref | action | before → after | PDF 页 |
|---|---|---|---|---|---|
| 1 | VS/assumptions.md:3-5 | O13 / ig34_p0358_a014 | INSERTED | 新增 `## VS – Description/Overview` + 定义句 (findings domain … height and weight) 逐字 | 358 |
| 2 | VS/assumptions.md:7-9 | spec 首句 (dispatch notes 域 spec 首句口径) | INSERTED | 新增 `## VS – Specification` + "vs.xpt, Vital Signs — Findings. One record per … Tabulation." 逐字 | 358 |
| 3 | VS/assumptions.md:11 | 结构 | INSERTED | 新增 `## VS – Assumptions` 标题 (PDF 原标题, 同 CM/SC 先例); 原 1-4 条未动 | 360 |
| 4 | VS/examples.md:17 | census:VS/examples.md:17:1:VSTPT | REPLACED | BASELINE → BASELINE 1 | 360 |
| 5 | VS/examples.md:18 | census:VS/examples.md:18:2:VSTPT | REPLACED | BASELINE → BASELINE 2 | 360 |
| 6 | VS/examples.md:19 | census:VS/examples.md:19:3:VSTPT | REPLACED | BASELINE → BASELINE 1 | 360 |
| 7 | VS/examples.md:20 | census:VS/examples.md:20:4:VSTPT | REPLACED | BASELINE → BASELINE 2 | 360 |
| 8 | VS/examples.md:22 | census:VS/examples.md:22:6:VSTPT | REPLACED | BASELINE → BASELINE 1 | 361 |
| 9 | VS/examples.md:23 | census:VS/examples.md:23:7:VSORRES | REPLACED | 38.2 → 36.2 | 361 |
| 10 | VS/examples.md:23 | census:VS/examples.md:23:7:VSSTRESC | REPLACED | 38.2 → 36.2 | 361 |
| 11 | VS/examples.md:23 | census:VS/examples.md:23:7:VSSTRESN | REPLACED | 38.2 → 36.2 | 361 |
| 12 | VS/examples.md:23 | census:VS/examples.md:23:7:VSTPT | REPLACED | BASELINE → BASELINE 2 | 361 |
| 13 | VS/examples.md:28 | census:VS/examples.md:28:12:VSSTRESC | REPLACED | 38.2 → 36.2 (VSSTRESN 已是 36.2, 现同行一致) | 361 |

atoms[] = 0; census DIFF 表 1 张 (10 cell diffs, kb_lines 17/18/19/20/22/23/28) 全部处理. pdf_only / pdf_unparsed / unparseable 均 0.

## 双向全扫 (p358-361 VS 部分)
- PDF→KB: §6.3.13 标题/Description 句/Specification 句 (已补); spec 变量表 p358-360 属 spec.md (不在本批); 脚注 "1In this column…" 属 spec.md; Assumptions 1-4 与 KB 逐字一致; Examples 引言句 + 5 条 Rows 说明逐字一致; vs.xpt 表 13 行 × 25 列逐格对渲染 (行 1-4 左段对 layout 文本 + 右段对渲染; 行 5-13 左右两段全部对渲染), 除上述 10 格外全一致.
- KB→PDF: assumptions.md / examples.md 无 KB 自写解释内容, 无 D6/D2 项. `**vs.xpt**` / `## Example 1` 为纯导航.
- 删除清单: 无 (仅 VALUE_DIFF 旧值替换).

## PDF_TYPO
无. 行 7 改为 36.2 是 KB 错 (PDF 行 7 VSORRES/STRESC/STRESN 三格一致 36.2); 行 12 KB 原 VSSTRESC 38.2 与同行 VSSTRESN 36.2 自相矛盾, PDF 两格均 36.2.
注: 行 12 PDF 97.16 F → 36.2 C 数值换算 ≈ 36.2 ✓. 行 7 (Baseline 第二次 TEMP 36.2 C) 为 PDF 原值, 不判 typo.
预期 fp 回归: 无 (无 PDF_TYPO 偏离 PDF 的写法; 所有改动均为 KB 值改成 PDF 值).

## 范围外发现
- VS/spec.md 未在本批核查 (spec 表 p358-360); 顶部 `> Class/Structure` 行为 KB 摘要式, 非 PDF 原句 — 已由 assumptions.md Specification 节补原句, spec.md 未动.

## git diff --stat
```
 knowledge_base/domains/VS/assumptions.md | 10 ++++++++++
 knowledge_base/domains/VS/examples.md    | 14 +++++++-------
 2 files changed, 17 insertions(+), 7 deletions(-)
```
