# NotebookLM 管理员部署指南

本指南面向需要自行配置或维护 SDTM Pedia NotebookLM 实例的管理员。普通用户通常只需要访问团队已经配置好的 notebook。

## 适用场景

- 团队希望使用更严格的来源边界和引用回查。
- 管理员需要维护一个基于 NotebookLM 的 SDTM Pedia notebook。
- 需要把发布包中的说明和 source 文件加入 NotebookLM。

## 前置条件

- 具备可创建和共享 NotebookLM notebook 的 Google 账号或组织权限。
- 能访问本发布包中的 `instructions.md` 和 `uploads/` 文件夹。
- 已确认组织允许在 NotebookLM 中使用相应资料，并遵守数据安全要求。

## 部署步骤

1. 在 NotebookLM 中创建新的 notebook。
2. 将 `uploads/` 下的 42 个 source Markdown 文件加入 notebook。不要把清单或说明文件当作 source 上传。
3. 等待文件完成处理，并检查 source 列表是否完整。
4. 将 `instructions.md` 的完整内容加入 Chat 的 Custom mode / 自定义说明区域。
5. 使用少量标准问题确认变量定义、域边界和引用回查可以正常工作。
6. 按组织政策设置共享范围。

## 建议命名

建议使用:

> SDTM Pedia - Internal Reference

说明中应明确它是 SDTM 标准查询辅助工具，不替代 CDISC 官方出版物或组织内部 SOP。

## 基础验证

部署后建议确认:

- 能解释 `AESER` 的含义和使用属性。
- 能回答 `LBNRIND` 等常见受控术语问题。
- 能区分 `LB`、`MB`、`IS` 的适用场景。
- 回答中能显示或指向可回查来源。

如果回答找不到明显应存在的内容，优先检查 source 是否完整、是否有处理失败的文件、Custom mode 说明是否完整。

## 团队共享

共享前请确认:

- 访问链接或邀请范围是否符合组织政策。
- 谁可以编辑 notebook 或 source。
- 是否禁止输入项目机密、患者信息或未脱敏数据。
- 是否需要为普通用户提供“只用于参考查询”的说明。

## 维护建议

- 更新 source 前先复制一个管理员测试 notebook。
- 更新后重新做基础验证。
- 记录更新日期、维护者、变更摘要和验证结果。

## 使用边界

NotebookLM 更适合需要严格来源边界和引用回查的场景。它仍然是 SDTM 查询辅助工具，不替代 CDISC 官方资料、医学判断或组织内部质量流程。
