# Bedrock 账号拒绝 Anthropic 模型 — 事件记录 (2026-09-11)

> 状态: **外部阻断, 未解决** (AWS 账号侧权限, 仓库内无法修复)
> 起源: 用户从局域网另一台机器 (192.168.100.28) 提问「RSTPT 的用法…可以单独使用吗」无回复

## 1. 现象与时间线 (取自 `logs/api.launchd.log`)

| 时刻 | 事件 |
|---|---|
| 2026-09-09 10:49 | 最后一次 Anthropic 模型成功调用 (flag 记录; C2R V3 评测 28/28 零回退亦在 09-09) |
| 09-11 10:05:25 | `light` 路由组 (opus-5@Bedrock) 400: `Access to Anthropic models is not allowed for this account`; 无 fallback (内部组按设计不配) → `route_corpus_fallback_both` |
| 09-11 10:05:28 | 第 1 次 `POST /api/ask_stream` 结束 (200, 与路由完成同秒); 紧接整页重载 → 判为客户端中断, 无 `stream_failed` / `model_fell_back` 记录 |
| 09-11 10:08:13 | 第 2 次提问, 同样路由报错 → both |
| 09-11 10:08:52 | `model_fell_back model_id=opus-5 models_used=['deepseek-v4-pro']`, 200 (39 s) — 答案由 DeepSeek 兜底给出, 带回退徽章 |

日志中该错误共 20 处, 全部 09-11。仓库自 09-09 提交 1a27b01 后无服务端改动, 工作树 clean —— **不是改修引起**。

## 2. 直接复现 (2026-09-11 10:40, 本机, `.env` 同生产)

```
cd sdtm-rag && .venv/bin/python - <<'PY'
import litellm
from dotenv import load_dotenv; load_dotenv(".env")
for m in ["bedrock/converse/global.anthropic.claude-opus-5",
          "bedrock/converse/global.anthropic.claude-sonnet-5",
          "bedrock/converse/global.openai.gpt-5.6-terra",
          "bedrock/converse/global.openai.gpt-5.6-sol",
          "deepseek/deepseek-v4-pro"]:
    try:
        r = litellm.completion(model=m, messages=[{"role":"user","content":"say ok"}], max_tokens=20, timeout=30)
        print("OK  ", m, repr(r.choices[0].message.content)[:40])
    except Exception as e:
        print("FAIL", m, str(e)[:160].replace("\n"," "))
PY
```

结果:

| 模型 | 结果 |
|---|---|
| bedrock opus-5 | FAIL `Access to Anthropic models is not allowed for this account.` |
| bedrock sonnet-5 | FAIL 同上 |
| bedrock gpt-5.6-terra | OK |
| bedrock gpt-5.6-sol | OK |
| deepseek-v4-pro | OK |

## 3. 对生产的影响

- 服务仍可答 (答题组 opus-5 → `default-fallback` DeepSeek, `fell_back=true` 徽章可见); 但每题多付 ~3 s 路由报错 + 3000 行 Rich traceback 进日志, 且模型悄悄变成个人流量 DeepSeek (spec C1 明示代价)。
- 用户可选 gpt-terra / gpt-sol 避开回退。
- 内部 `light`/`hard`/`default` 三组均指向 opus-5, 无 fallback: 路由/难题通道每次都先撞 400。

## 4. 处置

- 仓库侧: 不改代码 (账号权限问题, 换默认模型是用户决策; 见 `model_compare_2026-09.md` Q1 「数据不足以建议」)。
- 用户侧: 向 AWS / IT 确认该账号 Bedrock 的 Anthropic model access 是否被撤销或订阅到期 (region ap-northeast-1, global.* profile)。
- 临时缓解 (若需, 由用户裁定): `.env` 把 `SDTM_RAG_LIGHT_MODEL` / `SDTM_RAG_DEFAULT_MODEL` / `SDTM_RAG_HARD_MODEL` 临时指到 `bedrock/converse/global.openai.gpt-5.6-terra`, 再 `launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api`。
- 下游影响: C2R N1 复测 opus-5 臂挂起 (PLAN §6)。
