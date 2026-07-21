# 段1 磁盘垃圾清理 evidence (2026-07-21)

- 前置门: chroma 健康预检 `/api/ask` 真答 → sources: 15 ✅ (删备份放行)
- 删除: .mypy_cache 86M / pytest·ruff cache / __pycache__×7 / egg-info / .omx 15M / 游离 .omc×4 / chroma_backup×2 93M / web dist+dist-bundles+.astro+test-results ~74M / 根 node_modules 17M + package-lock / .DS_Store×18
- 仓库体积: 2.1G → 1.8G (另 git gc 在段0 已把 .git 146M→42.6M pack)
- git status: 空 (全部为 ignored/untracked 内容, 零 git 影响)
