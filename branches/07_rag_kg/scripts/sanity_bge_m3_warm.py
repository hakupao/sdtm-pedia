#!/usr/bin/env python3
"""sanity_bge_m3_warm.py — warm-state + batch throughput benchmark.

Follow-up to sanity_bge_m3.py (cold run = 583ms/chunk FAIL). Cold-start MPS
JIT compile + tiny single-batch (n=5) doesn't amortize overhead. Real workload:
  - Ingest: batch encode ~4300 chunks at batch_size=32-64
  - Query:  single inference per query, but model warm in process

This script measures:
  1. Cold load (model already cached locally from prior run)
  2. Warm single-text inference (5 runs avg)
  3. Batch throughput @ batch_size in [1, 8, 32, 64]
"""

from __future__ import annotations

import time

import torch
from sentence_transformers import SentenceTransformer

device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Device: {device}")

print("Loading bge-m3 (cached locally)...")
t0 = time.time()
model = SentenceTransformer("BAAI/bge-m3", device=device)
print(f"Model load: {time.time() - t0:.1f}s")

base_text = (
    "AETERM is the adverse event term variable in the AE domain. "
    "TA Example illustrates parallel-arm trial design. "
    "LB hematology codelist contains LBTESTCD entries like HGB and HCT."
)

# Warm-up (MPS JIT compile)
print("\nWarm-up (3 dummy runs)...")
for _ in range(3):
    model.encode([base_text])

# Single-text inference (5 runs)
print("\n=== Single-text inference (warm) ===")
single_times = []
for i in range(5):
    t = time.time()
    model.encode([base_text])
    dt = (time.time() - t) * 1000
    single_times.append(dt)
    print(f"  run {i+1}: {dt:.2f}ms")
print(f"single warm avg: {sum(single_times)/len(single_times):.2f}ms")
print(f"single warm min: {min(single_times):.2f}ms")

# Batch throughput
print("\n=== Batch throughput ===")
print(f"{'batch':>6} | {'total ms':>10} | {'ms/chunk':>10}")
print("-" * 36)
for bs in [1, 8, 32, 64]:
    texts = [base_text] * bs
    # 1 warm-up run per batch size
    model.encode(texts)
    t = time.time()
    model.encode(texts)
    dt_ms = (time.time() - t) * 1000
    print(f"{bs:>6} | {dt_ms:>10.2f} | {dt_ms/bs:>10.2f}")

# Realistic full-ingest estimate
print("\n=== Full-ingest estimate ===")
n_chunks = 4304  # per phase_1a_0_sanity.md §5
texts = [base_text] * 64
# warm-up
model.encode(texts)
t = time.time()
model.encode(texts)
ms_per_64 = (time.time() - t) * 1000
ms_per_chunk_batch64 = ms_per_64 / 64
total_ingest_s = (n_chunks * ms_per_chunk_batch64) / 1000
print(f"@ batch_size=64: {ms_per_chunk_batch64:.2f}ms/chunk")
print(f"Full ingest (~{n_chunks} chunks): {total_ingest_s:.0f}s = {total_ingest_s/60:.1f}min")
