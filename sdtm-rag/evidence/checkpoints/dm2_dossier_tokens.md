# DM2 — T2 研读包 token 计量 (2026-09-15)

复跑:
- 默认范围 (含选择肢): `.venv/bin/python eval/prod_wirein/dm2_dossier_tokens.py`
- 默认范围 (去选择肢, 备选数字): `.venv/bin/python eval/prod_wirein/dm2_dossier_tokens.py --no-choices`

## ⚠ tokenizer 口径说明

litellm 1.88.1 对 `selectable_models` 四个 bedrock/converse 模型串 (`server/config.py:59`)
都没命中它内置的 model→tokenizer 映射表 (`litellm.utils._select_tokenizer` 静默回落,
两次运行 stderr 均为空, 没有打印警告), 实测四档全部回落到同一个 `openai_tokenizer`
(`tiktoken cl100k_base`) 计数 —— 因此下表四列数字**逐字相同**, 是同一套 cl100k_base
估计值, 不是四个模型各自的原生 tokenizer 结果。量级参考可用, 精确值不可用; 若要
精确数字需换算 (Bedrock 侧 token 计价接口, 或已知模型专属 tokenizer 库), 本次未做。

## 数字

| 范围 | chars (A/B) | opus-5 | sonnet-5 | gpt-terra | gpt-sol |
|---|---|---|---|---|---|
| s4-s12 + 一览含选择肢 (默认) | 166563 (92532/74031) | 133652 | 133652 | 133652 | 133652 |
| s4-s12 + 一览去选择肢 (`--no-choices`) | 139976 (92532/47444) | 106993 | 106993 | 106993 | 106993 |

n_sections=52, n_items=959 (两次运行相同; `--no-choices` 只改写 B 段每行文本, 不改条目数/章节数)。

## 裁定规则 (spec §3)

Claude 档 ≤ 150K token → 按默认范围实施. 否则由用户点收窄顺序: (1) 一览去选择肢 (2) 收白名单.

两档 (含选择肢 133652 / 去选择肢 106993, 均为 cl100k_base 估计值) 都 ≤ 150K, 按规则
可直接按默认范围实施; 已备好去选择肢兜底数字供用户参考。

## 用户裁定

(待填: 范围 / 日期)
