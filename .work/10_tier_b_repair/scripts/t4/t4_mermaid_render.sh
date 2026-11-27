#!/usr/bin/env bash
# U-11 / O51: 抽出 knowledge_base/ 全部 ```mermaid 块, 用 mermaid-cli 11.4.2 + 本机 Chrome 渲染; 任一失败 → exit 1.
# 用法: bash .work/10_tier_b_repair/scripts/t4/t4_mermaid_render.sh <scratch_dir>
set -u; S=${1:?scratch dir}; mkdir -p "$S"; cd "$(git rev-parse --show-toplevel)"
python3 -I - "$S" <<'PY'
import sys,pathlib,subprocess
S=pathlib.Path(sys.argv[1]); n=0
for f in subprocess.check_output(['git','grep','-l','```mermaid','--','knowledge_base']).decode().split():
    L=open(f).read().split('\n'); i=0
    while i<len(L):
        if L[i].strip()=='```mermaid':
            j=i+1
            while L[j].strip()!='```': j+=1
            n+=1; (S/f"b{n:02d}.mmd").write_text('\n'.join(L[i+1:j])+'\n'); print(f"b{n:02d}\t{f}:{i+1}")
            i=j
        i+=1
PY
echo '{"executablePath":"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome","args":["--no-sandbox"]}' > "$S/pp.json"
ok=0; bad=0
for f in "$S"/b*.mmd; do
  if npx -y @mermaid-js/mermaid-cli@11.4.2 -p "$S/pp.json" -i "$f" -o "${f%.mmd}.svg" -q >"${f%.mmd}.log" 2>&1 && ! grep -qi "syntax error" "${f%.mmd}.svg"; then ok=$((ok+1)); else bad=$((bad+1)); echo "FAIL $f"; fi
done
echo "mermaid blocks OK $ok FAIL $bad"; [ $bad -eq 0 ]
