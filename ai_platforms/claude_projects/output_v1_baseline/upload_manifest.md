# Upload Manifest — Phase 6.5 Claude Project

> Generated: 2026-04-17T14:23:22Z (max mtime of output/*.md)
> Source: ai_platforms/claude_projects/output/*.md
> Built by: scripts/build_all.py (Layer 1 verifier)

## 文件清单 (11 个)

| 序 | 文件 | Tokens | md5 | 上传说明 |
|----|------|-------:|-----|---------|
| 00 | 00_routing.md | 2,657 | 65603fe7d53e85183643010796ce7bcc | Project Knowledge |
| 01 | 01_index.md | 1,562 | 1494e4b9951fa86354017e93c8a3a272 | Project Knowledge |
| 02 | 02_chapters.md | 44,874 | e1e8beaea66d560319b76d85348ef7fe | Project Knowledge |
| 03 | 03_model.md | 17,689 | de9a010f1dee0a062d29c92e306bd27a | Project Knowledge |
| 04 | 04_variable_index.md | 14,938 | 1741fa9fe31a62e36161e0202c3d7250 | Project Knowledge |
| 05 | 05_mega_spec.md | 65,993 | 79aa0bfb5dbfc7556e628140106a30e3 | Project Knowledge |
| 06 | 06_assumptions.md | 17,509 | 742a57c06a760bda55106e63251a070d | Project Knowledge |
| 07 | 07_examples_catalog.md | 4,295 | d090cd53b01ac650ad9a799a6514accf | Project Knowledge |
| 08 | 08_terminology_map.md | 20,536 | e00d68cd49f693e8c051712f9c2f9c6b | Project Knowledge |
| -- | system_prompt.md | 1,983 | a23d7bc42e7a04844ca914a2da7bde3b | **粘贴到 Project Instructions** |
| **合计** | — | **192,036** | — | — |

预算余量: 2,964 tokens (1.52%; limit=195,000, used=98.48%)

## Layer 1 检查 (§5.1)

| # | 检查项 | 标准 | 实测 | 结果 |
|---|-------|------|------|:-:|
| C1 | 总 tokens | ≤195,000 | 192,036 | PASS |
| C2 | Mega Spec 63 域覆盖 | 63 × `## XX —` | 63 | PASS |
| C3 | Assumptions 63 域覆盖 | 63 × `## XX` | 63 | PASS |
| C4 | Examples Catalog 63 域覆盖 | 63 × `### XX` | 63 | PASS |
| C5 | Cross References 保留 | 63 × `### Cross References` | 63 | PASS |
| C6 | ch04 完整保留 | ch04 ≥95% of source chars | 99.97% (124521/124560 chars) | PASS |
| C7 | ROUTING 原样搬运 | md5(out) == md5(src) | 65603fe7d5 vs 65603fe7d5 | PASS |
| C8 | 源路径标注存在 | ≥1 source-path annotation per merged file | all 7 merged files annotated | PASS |
| C9 | Terminology 映射覆盖 | ≥1000 codelist rows | 1005 | PASS |
| C10 | 输出文件数 | 10 artifacts (9 content + routing + system_prompt) | 10 content .md present + upload_manifest.md = 11 | PASS |

**Layer 1 结果: 10/10 PASS**

## 压缩率统计 (§5.3)

| 分区 | 源 tokens | 压缩后 | 压缩率 | 是否有损 |
|------|----------:|-------:|-------:|---------|
| ROUTING | 2,657 | 2,657 | 0% | 否 |
| INDEX | 5,032 | 1,562 | 69.0% | 部分 |
| chapters | 60,525 | 44,874 | 25.9% | 部分 |
| model | 17,573 | 17,689 | +0.66% | 否 |
| VARIABLE_INDEX | 38,452 | 14,938 | 61.2% | 部分 |
| specs (63) | 184,943 | 65,993 | 64.3% | 部分 |
| assumptions (63) | 53,708 | 17,509 | 67.4% | 部分 |
| examples (63) | 219,814 | 4,295 | 98.0% | 有损 (目录化) |
| terminology (91) | 1,944,449 | 20,536 | 98.9% | 有损 (映射表) |
| **合计** | **2,527,153** | **190,053** | **92.5%** | 部分有损 |

## 上传步骤 (手动, Step 13)

1. 登录 Claude → 新建 Project "SDTM Expert v3.4"
2. 在 **Project Instructions** 粘贴 `system_prompt.md` 全文
3. 在 **Project Knowledge** 上传 9 个内容文件 (`00_routing.md` … `08_terminology_map.md`)
4. 确认 Project 容量显示 ≈ 95–98%
5. 执行 §5.2 T1-T8 测试矩阵（Step 14）

## 若 Layer 1 FAIL

- 找对应 Step 重跑脚本 (见 PLAN.md §7.4)
- 修复后再跑 `python3 build_all.py` 刷新本 manifest
- 不要在本脚本里做 hack 式绕过；失败信号属于上游 Step

**Recommendation**: READY_FOR_UPLOAD — Layer 1 全部 PASS, 可进入 Step 13
