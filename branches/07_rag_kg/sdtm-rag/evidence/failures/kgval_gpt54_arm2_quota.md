# 失败归档: gpt54 arm2 未采集 (OpenAI 配额耗尽)

> 日期 2026-06-21。KG 价值 eval, GPT-5.4 第三模型臂。

## 输入
`eval/run_eval.py eval/test_set_kg_value.yml --structured-lookup --hybrid --structured-answer --graph-answer --model openai/gpt-5.4 --temperature 0 --judge --judge-model deepseek/deepseek-chat --full-answers` (arm2)。

## 产物 / 现象
- arm0 ✓ (judge_avg 0.587) + arm1 ✓ (judge_avg 0.725) 成功写出。
- **arm2 在跑到一半时报 `litellm.RateLimitError: OpenAIException - You exceeded your current quota`** → `kgval_arm2_gpt54.json` 未生成。
- GPT-5.4 ($2.50/$15 per 1M) 比 gpt-4o 贵, 3 臂跑到第 3 臂时把 OpenAI 余额额度跑空。

## 技术判定
非代码 bug。run_eval litellm 调用正确 (arm0/arm1 同命令成功)。纯计费/配额耗尽。

## 业务判定
**不阻塞 verdict**。ΔSP3 (SP3 边际) 由 ds + gpt4o 两个完整 3-臂模型确认 (均 ≈0); gpt54 的作用是第三模型确认 **SP2** (arm0→arm1 +14pp judge), arm0/arm1 已采到, 该确认成立。gpt54 arm2 (ΔSP3 第三确认) 是 nice-to-have 非必需。

## 下一 attempt 输入 (若要补)
给 OpenAI 账号充值后重跑单条:
`... --graph-answer --model openai/gpt-5.4 ... --output eval/prod_wirein/kgval_arm2_gpt54.json`
然后 analyzer MODELS 已含 "gpt54", 自动并入 (现因缺 arm2 被跳过)。预估成本 ~$0.5 一臂。

## 教训
多模型多臂跑前应预估各 provider 配额 (尤其前沿模型单价高)。可先跑最便宜模型全臂拿 verdict, 贵模型作确认臂时先确认配额够 N 臂。
