# B0 — 4 平台 uploads baseline 备份

> Date: 2026-05-20
> Phase: B — 4-platform rebuild + system_prompt audit
> Step: B0
> Status: PASS

---

## 1. 备份动作

```
cp -R ai_platforms/chatgpt_gpt/current/uploads     → .work/07_release_v1_3/backups/chatgpt_uploads
cp -R ai_platforms/gemini_gems/current/uploads     → .work/07_release_v1_3/backups/gemini_uploads
cp -R ai_platforms/notebooklm/current/uploads      → .work/07_release_v1_3/backups/notebooklm_uploads
cp -R ai_platforms/claude_projects/current/uploads → .work/07_release_v1_3/backups/claude_uploads
```

## 2. Size 验证 (匹配 v1.1 baseline 25.5 MB)

| Platform | Size | v1.1 baseline | Match |
|---|:-:|:-:|:-:|
| chatgpt | 9.3 MB | 9.3 MB | ✅ |
| gemini | 2.2 MB | 2.2 MB | ✅ |
| notebooklm | 9.4 MB | 9.5 MB | ✅ (一 bucket re-merge 细微差) |
| claude_projects | 4.6 MB | 4.6 MB | ✅ |
| **Total** | **25.5 MB** | **~25 MB** | ✅ |

## 3. 用途

- B2 rebuild 失败时 rollback baseline
- B3 cross-platform delta oracle 计算 baseline diff
- B4 system_prompt audit 时 grep baseline 数字引用

## 4. Gate

| Check | Verdict |
|---|:-:|
| 4 平台目录全备份 | ✅ |
| Size sanity ~25 MB | ✅ |
| 与 v1.2 LIVE 一致 (Phase A KB 改动还未 rebuild bundle) | ✅ |

PASS.
