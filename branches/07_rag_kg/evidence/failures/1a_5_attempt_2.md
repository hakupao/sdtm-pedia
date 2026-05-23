# Phase 1A.5 Ingest — Attempt 2 Failure Log (Rule B)

> 状态: **FAILED** — same OOM even at batch_size=8; sentence-transformers 5.x sorts ALL chunks by length before batching, so batch=8 puts the 8 longest chunks (5K tokens each) together → SDPA on MPS = 32 GiB.

## 输入

- ingest.py v2 (batch_size=64→8, single model.encode() call)
- terminology.py fix already verified (209 tests pass)

## 失败点

```
RuntimeError: Invalid buffer size: 32.00 GiB
  at torch.nn.functional.scaled_dot_product_attention
```

Size INCREASED from 16→32 GiB because batch=8 with 8×5K tokens → 8×5K²×4B×2 = 32 GiB.

## 技术判定

sentence-transformers ≥ 5.x encode() 内部先 sort_by_length, 再按 batch_size 分批.
所以 batch=8 时 first batch = 8 个最长 chunk, 全部 ~5K tokens.
SDPA (scaled_dot_product_attention) 需要 Q×K = batch × heads × seq × seq 大小的 attention buffer.
8 × 12heads × 5K × 5K × 4B = ~9.6 GB per head × 12 = still huge.
32 GiB 说明内部有额外 buffer alloc (intermediate + output).

## 下一 attempt 输入

修 ingest.py → 长度分桶 (length-bucketed) encode:
- 按 chunk_size_tokens 分三桶:
  - ≤512: batch=64 (fast, ~1.6ms/chunk)
  - ≤2048: batch=16
  - >2048: batch=2 (per probe: bs=2 with 4500-word text = OK 6.8s for 2 chunks)
- 每桶单独调用 model.encode(bucket_texts, batch_size=bucket_bs)
- 结果按原始 index 回填
- 完全绕过 sentence-transformers 内部 sort-and-batch
