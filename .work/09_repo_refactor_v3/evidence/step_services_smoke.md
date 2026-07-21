# 段4b 服务迁移 + 验活 evidence (2026-07-21)

- venv: 旧 .venv 删除, 新位置 `uv sync --all-extras` 重建, fastapi/chromadb import OK
- KB 锚点直测: Settings().kb_root == /Users/bojiangzhang/MyProject/sdtm-pedia/knowledge_base, INDEX.md 存在 ✅
- plist ×2: 4 处路径 sed 迁移, `grep branches` = 0, plutil lint OK ×2
- 服务: bootstrap 后 api {"status":"ok"} / ui HTTP 200 / neo4j 全程未动 (pid 1691 不变)
- api 启动日志: chunks=4146, graph_engine domains=63, hybrid/guardrail/structured_lookup 全 ON, rag_init 1.66s
- 端到端: /api/ask 真答 TV Required 变量 → sources: 15, 中文回答正常
- **执行中发现并修复 plan 遗漏**: scripts/tests/ 11 个文件的 KB_ROOT = parents[5] 锚 (调研误判 tests 全自锚)。
  深度变化后指向 $HOME/knowledge_base: 3 个测试 FAIL, 其余静默 skip — 静默指空风险的实证。
  批量改 parents[3] 后: **pytest 525 passed 0 failed** (> 迁移前 521, 之前有测试在静默 skip)
