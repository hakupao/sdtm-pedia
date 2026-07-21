# Claude Project 管理员部署指南

本指南面向需要自行配置或维护 SDTM Pedia Claude Project 的管理员。普通用户通常只需要访问团队已经配置好的 Project。

## 适用场景

- 团队需要一个适合复杂 SDTM 标准查询的共享入口。
- 管理员希望在 Claude Projects 中维护统一的 SDTM Pedia 实例。
- 需要把发布包中的知识文件和项目指令加入 Claude Project。

## 前置条件

- 具备可创建 Claude Project 的账号和组织权限。
- 能访问本发布包中的 `system_prompt.md` 和 `uploads/` 文件夹。
- 已确认组织允许在 Claude 中使用相应资料，并遵守数据安全要求。

## 部署步骤

1. 在 Claude 中创建新的 Project。
2. 将 `system_prompt.md` 的完整内容粘贴到 Project instructions。
3. 将 `uploads/` 下的 19 个 Markdown 文件上传到 Project knowledge。
4. 保存 Project，并设置合适的名称、说明和访问权限。
5. 使用少量标准问题确认变量定义、域边界和跨域解释可以正常回答。

## 建议命名

建议使用:

> SDTM Pedia - Internal Reference

说明中应明确它是 SDTM 标准查询辅助工具，不替代 CDISC 官方出版物或组织内部 SOP。

## 基础验证

部署后建议确认:

- 能解释 AE 域关键变量的含义和使用属性。
- 能区分 LB、MB、IS 等常见域边界。
- 对不在标准中的变量或数据集保持谨慎。
- 回答能给出可回查依据。

如果回答偏离预期，优先检查 Project instructions 是否完整、19 个知识文件是否全部上传、文件名是否保持不变。

## 团队共享

共享前请确认:

- 谁可以访问 Project。
- 谁可以修改 instructions 或知识文件。
- 是否禁止输入项目机密、患者信息或未脱敏数据。
- 是否需要为用户提供使用边界说明。

建议只给少数维护者编辑权限，避免配置被误改。

## 维护建议

- 更新前先复制一个管理员测试 Project。
- 验证通过后再替换正式实例中的指令或知识文件。
- 保留更新记录，包括日期、维护者、变更摘要和基本验证结果。

## 使用边界

Claude Project 实例可作为 SDTM 查询和解释辅助工具。正式提交、医学编码、项目级映射和质量控制仍应由负责人员按组织流程确认。
