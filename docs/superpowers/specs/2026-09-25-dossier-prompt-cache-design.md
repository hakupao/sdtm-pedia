# DM2 研读包 prompt cache (T11) design (2026-09-25)

> 起因: 研读包每题 ~146-156K prompt token 全价; 生成后确定性闸的重答再翻一倍; opus 已恢复 auto。

## §1 实测可行性 (零改码, 已完成)
`bedrock/converse/global.anthropic.claude-opus-5` 经 litellm, system 为 ~12K token 静态文本块 + `cache_control: {"type":"ephemeral"}`, 连发两次:
第 1 次 `cache_creation_input_tokens=12014`, 第 2 次 `cache_read_input_tokens=12014` (litellm 同时映射到 `prompt_tokens_details.cached_tokens`)。
复跑: `cd sdtm-rag && .venv/bin/python $TMPDIR/cache_probe.py` (脚本内容见本 spec 附录 A)。Opus 5 最小可缓存前缀 512 token; 5m / 1h 两档 TTL, Bedrock 均支持。

## §2 布局改动 (唯一必要的 prompt 结构变化)
现状: 研读包拼在**最后一条 user 消息**里, 位于**每题不同**的 CDISC 检索 context 之后 ⇒ 任何断点都缓存不到研读包。
改为: 研读包挂上时, `messages[0]` (system) = 原 system + `_DOSSIER_RULES` + `\n\n` + 研读包全文, 末尾一个 `cache_control` 断点 (5m); user 消息里不再含研读包。
- system 以 content block 列表形式发送 (`[{"type":"text","text":…,"cache_control":{"type":"ephemeral"}}]`), 仅研读包挂上时如此; 未挂时 system 仍为字符串, 输出与改动前逐字节相同。
- 研读包正文**逐字节不变**; `_DOSSIER_RULES` 只改指代句 (「The context ends with 【本研究 研読パッケージ】」→ 指向 system 末尾该块), 其余规则一字不改; pin 测试同步。
- 前缀 = system (按 routed corpus 至多 3 种变体) ⇒ 同一 corpus 下跨问题、跨对话、同对话追问、闸重答全部命中。
- 非 Anthropic 回退模型 (deepseek 等): litellm 对不支持的 provider 须能丢弃 `cache_control` 或降级为字符串 —— 实现须实测 / 测试回退路径不 400。

## §3 经济性 (预登记, 不夸大)
写入 1.25× / 读取 0.1× (5m TTL, 从请求**开始**计时)。孤立单问 (5 分钟内无第二次同前缀请求) 比现状**贵 25%** (研读包部分); 5 分钟内任一次复用即省 ~65%。盈亏平衡复用率 ≈ 22%。
闸重答 (同请求内第二轮) 必然命中 ⇒ 重答成本从 ~2× 降到 ~1.35×。
不选 1h TTL: 写入 2×, 人工问答流量稀疏时更亏; 可改为配置项。
- 配置 `dossier_prompt_cache: bool = True` (kill switch); `/api/info` 暴露。
- `done` / `/api/ask` 的 `usage` 透传 `cache_creation_input_tokens` / `cache_read_input_tokens` (两轮累计), e2e summary 行打印。

## §4 验证 (预登记, 实跑前单独 commit 进 `dm2_dossier_e2e.md` §0⁶)
- 零 LLM: 未挂时逐字节 golden; 挂上时 system 末块 = 规则 + 研读包且带断点、user 消息不含研读包; 回退模型路径不 400 (mock)。
- 实跑: opus × 同 6 题 (attempt 7 题集), 按 §0⁵ 同判据 + 常设裁定判分, **目标 6/6** (布局改动不得降质); 另报: 第 1 题 `cache_creation≈研读包`、第 2-6 题 `cache_read>0` (同 corpus), 总 prompt 成本相对 attempt 7 的比例。
- 未达 ⇒ `dossier_prompt_cache=False` 回滚布局 (kill switch 同时恢复旧布局), 归档失败。

## §5 不做
不改研读包内容 / 触发器 / 闸 / auto 名单; 不做 pre-warm (流量稀疏, 预热即纯写入成本)。

## 附录 A — 探针
```python
from dotenv import load_dotenv; load_dotenv(".env")
import litellm
big = "SDTM cache probe static block. " + ("The Disposition domain records protocol milestones and disposition events. " * 600)
for i in range(2):
    r = litellm.completion(model="bedrock/converse/global.anthropic.claude-opus-5", max_tokens=5, timeout=120,
        messages=[{"role":"system","content":[{"type":"text","text":big,"cache_control":{"type":"ephemeral"}}]},
                  {"role":"user","content":f"ping {i}"}])
    print(i, r.usage)
```
