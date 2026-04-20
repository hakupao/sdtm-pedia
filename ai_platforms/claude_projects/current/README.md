# current/ — SDTM 知识库 Claude Project 发布版

> 这是当前发布版. 你要部署或使用的就是这里.

## 快速开始

**第一次部署 Claude Project?** → 读 [UPLOAD_TUTORIAL.md](UPLOAD_TUTORIAL.md), 跟着 10 章节走一遍 (30-90 分钟).

**已经部署过, 只想更新?** → 下一节《更新部署》.

**想在命令行或 API 里用?** → Claude Projects 不支持 API 访问 (只能在 Web UI), 如果要 API 可部署的版本请看 `../../DESIGN_RAG_KG.md` 的 Phase 7 计划.

---

## 发布版构成

- **19 个知识库文件** ([uploads/](uploads/)): 覆盖 CDISC SDTM v3.4 的 63 域 + terminology codelist + chapters 全展开
- **1 份 System Prompt** ([system_prompt.md](system_prompt.md)): Claude Project 的 Custom Instructions, 定义查询路由和边界处理
- **1 份上传清单** ([upload_manifest.md](upload_manifest.md)): 每个文件的 token 数、内容概要、源文件路径

**总量**: ~1,286,161 tokens (约 1.29M), 19 个 `.md` 文件.

---

## 更新部署

如果本目录的内容有更新 (上游知识库重 build 后的新发布):

1. 打开已有 Claude Project → **Edit**
2. 删除 Project Knowledge 里所有旧文件
3. 上传 [uploads/](uploads/) 下全部 19 个新文件
4. 如果 [system_prompt.md](system_prompt.md) 也有更新, 同步替换 Custom Instructions
5. 等 Indexing (后台, 不必真等) → 跑 [UPLOAD_TUTORIAL.md](UPLOAD_TUTORIAL.md) §5 的 Smoke Test 3 题确认

---

## 能力范围

能准确回答:
- SDTM 变量定义 (Core / Role / Type / CT)
- Codelist 完整 Term 表 (高频 + 中频 codelist 全 inline)
- Example 数据表 (63 域 100% 覆盖)
- 章节引用 (§4.3.6 AE / §8.3 RELREC / §4.4 Timing 等精确章节号)
- 跨域关联 (PC↔PP RELREC / EPOCH 哪些域用等)
- 边界识别 (不在源的变量会坦诚声明, 不臆造)

不直接给出, 但会指引源文件 + NCI EVS Browser:
- **6 个 giant codelist 的完整 term 表**: C65047 Lab Test Code (2,536 terms), C67154 Micro Test Name (2,536 terms), C85491 Unit (1,639 terms), C85494 (592), C120527/C120528 (558 each). 这些体量超过 500 terms, 走 Deferred stub 模式, 模型会声明"未 inline", 并指引到源文件和 NCI EVS Browser.

覆盖不完整 (约 44%):
- **questionnaires codelist 长尾 296 条**: 业务上优先级最低, 未 inline. 如果问及, 模型会声明"Project 未覆盖"并建议去 NCI EVS 查.

---

## 覆盖率数据

| 类别 | 覆盖率 | 说明 |
|------|-------:|------|
| Core codelist | 99.3% (146/147) | 仅剩 1 个 MedDRA 级 giant 走 Deferred stub |
| Supplementary codelist | **100%** (188/188) | 全部 inline |
| Questionnaires codelist | 55.8% (374/670) | 业务最低优先级, 长尾归 Phase 7 |
| 63 SDTM 域 examples | **100%** | 全部数据表 inline |
| 6 章 chapters (ch01-ch10) | **100%** | byte-exact 展开 |
| Deferred stub (giant codelist) | 6 个 | C65047/C67154/C85491/C85494/C120527/C120528 |

---

## 测试基线

本发布版部署后应通过的回归测试矩阵: [../dev/test_results.md](../dev/test_results.md) (T1-T22 + T-core-reb + T-supp-reb, 共 24 题, 部署正确后应 24/24 PASS).

---

## 相关文档 (可选阅读)

**用户向**:
- [UPLOAD_TUTORIAL.md](UPLOAD_TUTORIAL.md) — 完整部署教程
- [../README.md](../README.md) — Claude Project 目录结构总览

**开发者向** (方法论, 不影响使用):
- [../docs/](../docs/) — 方法论文档 (开发计划/复盘/RAG 衰减曲线/Phase 7 交接/容量调研)
- [../dev/](../dev/) — 开发过程产物 (脚本/evidence/A/B 报告 等)
- [../archive/](../archive/) — 早期迭代归档

---

## 限制与注意

- **不支持公开分享**: Claude Projects 目前不能生成公开链接, 只能 Team/Enterprise 套餐内部共享
- **不支持 API 访问**: 发布版只能在 Claude Web UI 使用, 不能 programmatic query
- **需要 Claude Pro 及以上**: 免费套餐 capacity 不够容纳本发布版
- **知识库边界**: SDTM v3.4 标准, 不覆盖其他 CDISC 标准 (ADaM/CDASH/SEND) 也不覆盖药品临床数据本身
- **可能需要重部署**: 如果 Anthropic 调整 Claude Projects 的容量或 RAG 机制, 本发布版部署效果可能变化

---

*如果部署有问题, 参考 [UPLOAD_TUTORIAL.md](UPLOAD_TUTORIAL.md) §7 排错手册.*
