# Step 13 上传 + Step 14 容量验证 报告

> 执行日期: 2026-04-18
> Project: SDTM Expert v3.4
> Project URL: https://claude.ai/project/019d9e05-9286-77fc-a621-675ce52d30ec
> Project ID: 019d9e05-9286-77fc-a621-675ce52d30ec

## 完成情况

| Step | 内容 | 状态 |
|:-:|------|:-:|
| 13.1 | 创建 Project "SDTM Expert v3.4" + 描述 | ✅ DONE |
| 13.2 | 粘贴 `system_prompt.md` 到 Project Instructions | ✅ DONE |
| 13.3 | 上传 9 个知识库 .md 到 Project Files | ✅ DONE |
| 14.1 | 容量验证 | ✅ DONE（见下方）|

## Files 清单（9/9，UI 显示行数）

| 序 | 文件 | UI 行数 |
|:-:|------|-------:|
| 00 | 00_routing.md | 212 |
| 01 | 01_index.md | 76 |
| 02 | 02_chapters.md | 2,181 |
| 03 | 03_model.md | 1,114 |
| 04 | 04_variable_index.md | 379 |
| 05 | 05_mega_spec.md | 2,865 |
| 06 | 06_assumptions.md | 1,050 |
| 07 | 07_examples_catalog.md | 394 |
| 08 | 08_terminology_map.md | 1,205 |

## 容量实测值

```
12% of project capacity used
• Indexing（上传后索引中）
```

## 关键偏差：实测 12% vs PLAN 预期 95-98%

**偏差幅度**: 预期 192K/200K ≈ 96%，实测 12%，相差约 8 倍。

**推测原因**（未验证，需进一步求证）:
1. **Claude Projects 上限已升级**: 根据 12% 的比例反推，当前上限可能约 **1.5M-1.6M tokens**（而非 PLAN 时的 200K）。这与 Anthropic 近年扩展 Projects 容量的趋势一致。
2. **Tokenizer 更高效**: 新版 tokenizer 对中英混合 Markdown 压缩更好。
3. **显示口径变化**: "project capacity" 可能已不是纯 token 百分比，而是综合存储/索引的指标。

**需做的事**:
- 推测 1 若成立，整个压缩策略可以放宽：之前被剔除的 Example 数据表、CT Term 值原文可以直接带进来（解除 PLAN §7 里四条"坦诚边界"的必要性）。
- 但**暂不改动 System Prompt**，等 Layer 2 测试（T1-T8）确认 Claude 确实能搜索大容量下的文件后再说。

## 文件来源溯源疑点（待用户确认）

- 我在远程 Chrome（tabId 247462227）上的 `file_upload` 调用返回 `"Not allowed"`（因为路径 `/Users/bojiangzhang/...` 在远程机上不存在）。
- 切换到本地 Chrome（tabId 1009013834）后导航到 Project URL，**发现 9 个文件已全部在 Files 区域**。
- **推测（未验证）**: 用户在等我重新连接期间自己用本地 Chrome 拖拽上传了；或者之前某次 session 已传过。
- **需要用户确认**: 是否是你手动传的？若不是，需查用户行为日志以排除异常。

## Step 14 Layer 2 测试（T1-T8）

**状态**: 未启动。按 UPLOAD_TUTORIAL.md §5-6，由用户（Bojiang）在本 Project 内手动执行，记录回答并填写 test_results.md。

## 下一步

1. 等索引完成（"• Indexing" 消失）
2. 跑 smoke test（"列出你拥有的文件，每个文件一句话说明"）
3. 跑 T1-T8 矩阵
4. 根据容量富余情况，决定是否 Phase 7 扩展知识库（加 examples 数据、terminology 全文）
