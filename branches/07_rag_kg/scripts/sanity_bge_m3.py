#!/usr/bin/env python3
"""
sanity_bge_m3.py — Phase 1A.2.f bge-m3 sanity verification
Verifies: dim=1024, Mac MPS availability, inference speed <100ms/chunk
Decision D-4 v2 (2026-05-22): bge-m3 is EMBEDDING MAIN PATH
"""

import sys
import time

# Step 1: verify imports
try:
    import torch
except ImportError:
    print("FAIL: torch not installed. Run: pip3 install --user torch", flush=True)
    sys.exit(1)

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("FAIL: sentence-transformers not installed. Run: pip3 install --user sentence-transformers", flush=True)
    sys.exit(1)

import sentence_transformers
import numpy as np

# Step 2: detect device
mps_available = torch.backends.mps.is_available()
if mps_available:
    device = "mps"
else:
    device = "cpu"

print(f"torch version        : {torch.__version__}", flush=True)
print(f"sentence-transformers: {sentence_transformers.__version__}", flush=True)
print(f"MPS available        : {mps_available}", flush=True)
print(f"Device selected      : {device}", flush=True)
print(f"Loading BAAI/bge-m3 (first run ~2.5GB download, may take 5-15 min)...", flush=True)

# Step 3: load model
t_load_start = time.time()
model = SentenceTransformer("BAAI/bge-m3", device=device)
t_load_elapsed = time.time() - t_load_start
print(f"Model loaded in      : {t_load_elapsed:.1f}s", flush=True)

# Step 4: 5 sample SDTM texts (mimic real KB query patterns)
texts = [
    "AETERM is the adverse event term variable in the AE domain",
    "TA Example 1 illustrates a parallel-arm trial design schema with mermaid diagrams",
    "LB hematology codelist contains LBTESTCD entries like HGB and HCT",
    "Subject randomization arm assignment is tracked via ARM and ACTARM variables in DM",
    "Pharmacokinetic concentration measurements in PC use PCSTRESC and PCSTRESN per spec",
]

# Step 5: time embedding
print(f"\nEmbedding {len(texts)} texts...", flush=True)
t0 = time.time()
embeddings = model.encode(texts)
elapsed_ms = (time.time() - t0) * 1000
ms_per_chunk = elapsed_ms / len(texts)

# Step 6: validate shape
expected_shape = (5, 1024)
actual_shape = embeddings.shape

print(f"\n--- Results ---", flush=True)
print(f"Embedding shape      : {actual_shape}", flush=True)
print(f"Embedding dtype      : {embeddings.dtype}", flush=True)
print(f"Total embed time     : {elapsed_ms:.2f}ms", flush=True)
print(f"ms per chunk         : {ms_per_chunk:.2f}ms", flush=True)
print(f"First 5 dims [0]     : {embeddings[0][:5].tolist()}", flush=True)

# Step 7: assert shape
try:
    assert actual_shape == expected_shape, f"expected {expected_shape}, got {actual_shape}"
    print(f"\nShape assertion      : PASS ({actual_shape} == {expected_shape})", flush=True)
except AssertionError as e:
    print(f"\nShape assertion      : FAIL — {e}", flush=True)
    print("OVERALL VERDICT      : FAIL (shape mismatch)", flush=True)
    sys.exit(1)

# Step 8: speed verdict
if ms_per_chunk < 100:
    verdict = "PASS"
    verdict_note = f"{ms_per_chunk:.2f}ms/chunk < 100ms target"
elif ms_per_chunk < 500:
    verdict = "WARN"
    verdict_note = f"{ms_per_chunk:.2f}ms/chunk >= 100ms (acceptable on CPU, consider MPS)"
else:
    verdict = "FAIL"
    verdict_note = f"{ms_per_chunk:.2f}ms/chunk >= 500ms (too slow)"

print(f"\nOVERALL VERDICT      : {verdict} ({verdict_note})", flush=True)

if verdict == "FAIL":
    sys.exit(1)
else:
    sys.exit(0)
