# 管理员部署指南索引

本目录面向需要自行配置或维护 SDTM Pedia 平台实例的管理员。普通用户通常只需要访问团队已经配置好的 Claude Project、ChatGPT GPT、Gemini Gem 或 NotebookLM notebook。

## 何时需要阅读本目录

- 团队没有现成入口，需要管理员新建实例。
- 需要在组织内部统一维护访问权限、说明文本和知识文件。
- 需要更新或替换已有实例。
- 需要验证实例是否能回答基础 SDTM 查询。

## 平台指南

| 平台 | 指南 | 适合情况 |
| --- | --- | --- |
| Claude Projects | [claude/tutorial.zh.md](./claude/tutorial.zh.md) | 复杂标准解释和跨域推理。 |
| ChatGPT GPTs | [chatgpt/tutorial.zh.md](./chatgpt/tutorial.zh.md) | 团队日常查询和熟悉的 ChatGPT 入口。 |
| Gemini Gems | [gemini/tutorial.zh.md](./gemini/tutorial.zh.md) | 较长上下文综合和开放式比较。 |
| NotebookLM | [notebooklm/tutorial.zh.md](./notebooklm/tutorial.zh.md) | 严格来源边界和引用回查。 |

## 共通原则

- 使用发布包中对应平台目录下的说明文件和 `uploads/` 内容。
- 不要擅自改写指令文本或重命名知识文件，除非你正在维护一个新版本。
- 共享前确认组织的数据安全、患者隐私和访问权限要求。
- 只给少数维护者编辑权限，普通用户保留使用权限。
- 更新后用少量标准问题确认变量定义、域边界和受控术语查询能正常工作。

## 使用边界

部署完成的平台实例仍是 SDTM 查询辅助工具，不替代 CDISC 官方出版物、医学判断、项目级映射复核或组织内部质量流程。
