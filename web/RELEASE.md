# Cutting a release (v1.0+)

The website's `DownloadsSection` (gated by `PUBLIC_RELEASE_PUBLISHED`) links
to GitHub release assets at
`https://github.com/hakupao/sdtm-pedia/releases/download/{tag}/{filename}`.
This doc covers how to build those bundle zips and publish a release.

## 1. Build bundles locally

```
cd web && bash scripts/build-bundles.sh v1.0
```

Outputs 4 zips under `web/dist-bundles/` (gitignored). Sizes should roughly match
`web/src/data/downloads.json`:

| platform   | files | size  |
|------------|-------|-------|
| claude     | 19    | 4.6 MB|
| chatgpt    |  9    | 9.3 MB|
| gemini     |  4    | 2.2 MB|
| notebooklm | 43    | 9.4 MB|

Verify:

```
ls -lh web/dist-bundles/
unzip -l web/dist-bundles/claude_bundle_v1.0.zip | head
```

## 2. Tag + create GH Release

```
cd /Users/bojiangzhang/MyProject/SDTM-compare
git tag v1.0
git push origin v1.0
gh release create v1.0 \
  --title "v1.0" \
  --notes-file ai_platforms/release/v1.0/CHANGELOG.md \
  web/dist-bundles/*.zip
```

## 3. Verify URLs resolve

```
for f in claude_bundle_v1.0.zip chatgpt_bundle_v1.0.zip gemini_bundle_v1.0.zip notebooklm_bundle_v1.0.zip; do
  curl -sI "https://github.com/hakupao/sdtm-pedia/releases/download/v1.0/$f" | head -1
done
```

Expected: each returns `HTTP/2 302` (redirect to S3 download).

## 4. Flip the website feature flag

Set `PUBLIC_RELEASE_PUBLISHED=true` in the CF Pages deploy environment (or
edit `web/.env`). The DownloadsSection then renders the 4-bundle grid
instead of the "release pending" placeholder.

## Bumping version (v1.1+)

1. Edit `web/src/data/downloads.json` — bump `tag` to `v1.1` and update
   each bundle's `files`/`sizeMB` if changed.
2. Re-run the build script with the new version: `bash scripts/build-bundles.sh v1.1`.
3. Tag, push, `gh release create v1.1 ...` as above.
4. The website automatically picks up the new tag from `downloads.json` on
   next build/deploy. No code change needed.

## Sources

The bundles are built from `ai_platforms/release/v1.0/self_deploy/{claude,chatgpt,gemini,notebooklm}/`.
Each platform directory is an independent self-contained deploy bundle —
system prompt + uploads/ + tutorial × 3 langs. See
`ai_platforms/release/v1.0/README.{zh,en,ja}.md` for the deployment flow.
