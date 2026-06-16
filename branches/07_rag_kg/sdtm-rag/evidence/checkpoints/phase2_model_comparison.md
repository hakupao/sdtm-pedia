# 四方模型对比 (主力决策数据) — DeepSeek-v4-pro / Sonnet-4.6 / GPT-4o / GPT-5.4-mini

> 日期: 2026-06-16 · DEPLOY_PLAN §3 阶段2 ③ · 规则 A (模型决策必须有 eval 数据 + 语义抽检)
> 测试集: `eval/test_set_v3.yml` (140 题) · 报告: `eval/cmp_{deepseek,sonnet,gpt4o,gpt54mini}_v3.json`
> (DeepSeek/Sonnet 2-way 先做; GPT-4o + GPT-5.4-mini 应用户要求补测, gpt-5.4-mini=2026-03 发布, 晚于模型知识截止, 经 OpenAI /models 查实存在)

## 配置 (公平配对)
四模型**完全同条件**: top_k=15, temperature=0(gpt-5.4-mini 经冒烟确认接受 temp=0), 检索杠杆全 ON(structured_lookup + hybrid-rrf + guardrail, **匹配生产**), 同判官 `deepseek/deepseek-chat`(temp=0, 答案匿名仅见文本)。仅答题模型不同。

## 结果

| 指标 | DeepSeek-v4-pro | Sonnet-4.6 | GPT-4o | GPT-5.4-mini |
|------|---------|---------|---------|---------|
| Overall (src+judge) | 96.6% | **97.8%** | 95.0% | 94.9% |
| **判官 fact-recall (per-q 均值)** | 93.6% | **96.0%** | 90.4% | 90.2% |
| — single_domain | 92.2% | **97.5%** | 90.6% | 88.8% |
| — cross_domain | 93.3% | **95.3%** | 87.3% | 88.2% |
| — concept | 98.7% | **100%** | 98.7% | 96.0% |
| — mixed | 91.0% | 91.0% | 87.7% | 90.7% |
| source recall (全类别) | ~100% | ~100% | ~100% | ~100% |
| 答题成本 (140q) | $1.04 | $10.09 | $5.47 | $1.73 |
| **每题成本** | **$0.0075** | $0.0721 | $0.0391 | $0.0123 |
| 平均延迟/题 | 19.5s | 37.4s* | 29.2s* | **4.1s** |
| verdict | PASS | PASS | PASS | PASS |

\* Sonnet & GPT-4o 延迟被 provider 速率限制 backoff 灌水, 非模型速度。GPT-5.4-mini 4.1s 是真快。
成本: DeepSeek/Sonnet 用 §9 表, OpenAI 用 litellm cost_per_token(统一 `server.cost.estimate_cost`)。

## 排名与关键发现
- **质量**: Sonnet (96.0) > DeepSeek (93.6) > GPT-4o (90.4) ≈ GPT-5.4-mini (90.2)。**两个 OpenAI 模型都低于 DeepSeek**(本 SDTM KB 上)。
- **独占最佳/最差**(某题唯一最高/最低判分): 最佳 Sonnet 7 / GPT-4o 2 / DeepSeek 1 / mini 0; 最差 mini 12 / GPT-4o 10 / DeepSeek 3 / Sonnet 1。→ mini 从不独占最佳、最常独占最差, 但均值仍≈GPT-4o(很少灾难性错, 只是少出彩)。
- **GPT-5.4-mini 完胜 GPT-4o**: 同等质量(~90%)、1/3 成本($0.012 vs $0.039)、7x 速度(4.1s vs 29s)。要用 OpenAI 这条, mini 比 4o 划算; 但都不及 DeepSeek。
- **DeepSeek 是质量/价格之王**: 比两个 OpenAI 都准, 且最便宜。强化"维持 DeepSeek 默认"决定。

## 语义抽检 (规则 A)
- **"枚举弱"是便宜模型共性**: q02 (DM 全部 Core=Req 变量) DeepSeek=14% / mini=43%, 都只列了 DOMAIN 就收(spec.md 在上下文里); Sonnet/GPT-4o=100% 完整枚举。
- **GPT-5.4-mini 失分性质 = 不完整, 非编造**: 7 题落后最佳≥40pt(q02/q10/q14/q66/q70/q121...), 全是漏变量名/漏 cross-domain 细节(USUBJID/SREL/TRLNKID/LB/VS...); 它 grounding 正常("shown in the retrieved context"), 只是 recall 低。典型 mini 行为: 安全但不够全。
- **Sonnet 强在完整枚举**(7 次独占最佳), 是稳定模型能力差, 非判官偏置(同判官且 Sonnet 得分最高)。

## 决策 (§3 ④⑤)
- 建议(我): 质量优先可切 Sonnet; 性价比看 DeepSeek。
- **决策(你, 2026-06-16): 维持 DeepSeek-v4-pro 默认。** 四方数据进一步支撑: DeepSeek 比两个 OpenAI 都准且最便宜, 仅 Sonnet 质量更高但 9.6x 成本。Sonnet 留 hard 档 / Compare 高风险题手动核验。无需改 .env(默认已是 deepseek-v4-pro)。
- 备选认知: 若日后要"快"——GPT-5.4-mini 4.1s + $0.012 是最快最便宜的 ~90% 档; 若要"最准"——Sonnet。三者已在 Compare 槽里随时可调(FR7)。
- 规则 A 满足: 决策有 140 题 × 4 模型 eval + 语义抽检支撑。
