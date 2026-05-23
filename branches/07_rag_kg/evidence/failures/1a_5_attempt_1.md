# Phase 1A.5 Ingest — Attempt 1 Failure Log (Rule B)

> 状态: **FAILED** — embedding OOM on first encode() call. Fix: lower batch_size to 8, sort by length.

## 输入

- 命令: `python3 scripts/ingest.py --retrieval-sanity`
- terminology.py 已修 (lb_part2/3 N=100 row slicing PASS pytest 209/209)
- ingest.py v1 (initial implementation, batch_size=64)
- KB SHA: 453df45a4d863ba5de647f4b7bf79ea0ae436f2d

## 产物 (失败前阶段)

- Chunking 阶段成功: 4146 chunks from 294 files
  - assumptions: 476 (64 files — 注: 比 spec 多 1, 待 1A.6 trace)
  - chapter: 76 (6 files)
  - examples: 209 (63 files)
  - model: 28 (6 files)
  - spec: 2164 (63 files)
  - terminology: 1128 (91 files)
  - variable_index: 65 (1 file)
- Total tokens: 2,543,220 (avg 613 tokens/chunk)
- bge-m3 model 加载 OK on MPS (8.0s 冷启)

## 失败点

`sentence_transformers.SentenceTransformer.encode(batch_size=64)` 第一个 batch 就 OOM:

```
RuntimeError: Invalid buffer size: 16.00 GiB
  at transformers/modeling_attn_mask_utils.py:194
  expanded_mask = mask[:, None, None, :].expand(bsz, 1, tgt_len, src_len).to(dtype)
```

## 技术判定

- bge-m3 默认 `max_seq_length=8192`. sentence-transformers `encode()` 会把 batch
  内所有序列 pad 到 batch 最长那条 → attention mask = batch × 1 × max_len × max_len bytes
- 我们的语料里 lb_part2/3 切片每段 4-5K token, spec/examples chunks 也有 1-2K
  混杂. batch=64 + max 8192 → 64 × 8192 × 8192 = 16 GiB attention mask, MPS OOM
- 1A.2.f benchmark (11.32 ms/chunk batch=64) 是在 dummy 短文本上测的, 不代表
  生产语料分布. 需要 batch 大小自适应或排序+小 batch

## 业务判定

- **NOT a chunking bug** — chunks themselves correct (lb_part2/3 max 5412 tokens, 全部 < 8191)
- 仅是 embedding 执行参数问题
- 修复后必须重跑全量 + 重新 verify retrieval

## 下一 attempt 输入

修 ingest.py:
1. `batch_size` 64 → 8 (减 8 倍 memory)
2. encode 前按 chunk token 长度排序, 短 chunks 先嵌入, 自然均摊
3. `model.max_seq_length` 保持 8192 (覆盖全部 chunks)
4. 加 `Length-bucketing`: encode() 用 sentence-transformers 自带 sort/restore

实现细节 (sentence-transformers ≥ 5.x):
- `encode(...)` 默认 `convert_to_numpy=True` 已经 sort by length descending
  internally + restore order on return. 所以只需要降 batch_size.
- 验证下 batch_size 候选: 4146 chunks / 8 = 519 batches. 长 batch ~5K tokens →
  attention mask 8 × 5K × 5K × 1B = 200 MB, 完全 OK.

预计 wallclock: 4146 chunks × 30 ms/chunk (warm small batch) = 124s ≈ 2 min.

## Lessons learned

- Sanity benchmark 必须用生产语料样本 (不是 dummy ~50 char strings)
- bge-m3 max_seq_length=8192 + batch=64 内存爆炸是 well-known issue,
  生产 ingest 必须降 batch_size 或 split by length bucket
