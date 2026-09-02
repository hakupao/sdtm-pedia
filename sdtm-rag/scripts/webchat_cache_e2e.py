"""End-to-end harness for the webchat browser-cache gate.

Why a harness and not a pytest case: the defect is "the server serves the new file, the
browser executes an old one". A TestClient assertion on response headers cannot see it —
only a real browser's HTTP cache can. This script provides the server + file-mutation half;
the browser half is driven externally (see the runbook in the module docstring below).

Runbook (each command from sdtm-rag/):
    D=/tmp/webchat_cache_e2e
    .venv/bin/python -m scripts.webchat_cache_e2e setup  $D V1
    .venv/bin/python -m scripts.webchat_cache_e2e serve  $D 8011   # background, NOT port 8000
    # browser: navigate to http://127.0.0.1:8011/  -> markers must read V1
    .venv/bin/python -m scripts.webchat_cache_e2e setup  $D V2
    # browser: navigate away (about:blank) then back to http://127.0.0.1:8011/
    #          -> markers must read V2 without a hard reload
    # cleanup: kill the serve process

The generated page carries two independent markers so both halves of the fix are covered:
`#doc-version` comes from index.html (served by the `GET /` FileResponse) and
`window.__MARKER` comes from /static/marker.js (served by the StaticFiles mount).

The generated files are backdated: a browser's heuristic freshness for a response with no
Cache-Control is a fraction of (now - Last-Modified), so a file whose mtime is minutes old
would be revalidated anyway and the unfixed server would look healthy. Backdating by weeks
buys a heuristic lifetime of days, which is what real deployed assets look like.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

_BACKDATE_S = 30 * 24 * 3600  # ~3 days of heuristic freshness at the usual 10% rule

_INDEX = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8" /><title>webchat cache e2e</title></head>
<body>
  <h1 id="doc-version">{version}</h1>
  <p id="doc-padding">{padding}</p>
  <script src="/static/marker.js"></script>
</body>
</html>
"""

_MARKER = 'window.__MARKER = "{version}";{padding}\n'


def setup(directory: Path, version: str) -> None:
    """Write the marker pair at `version` and backdate both files.

    The padding makes the two versions differ in byte length. Starlette derives the ETag
    from (mtime, size), so same-size versions at the same backdated mtime would collide and
    the revalidation would answer 304 with stale content — a green gate that proves nothing.
    """
    directory.mkdir(parents=True, exist_ok=True)
    padding = "." * (len(version) * 17)
    files = {
        "index.html": _INDEX.format(version=version, padding=padding),
        "marker.js": _MARKER.format(version=version, padding=" //" + padding),
    }
    backdated = time.time() - _BACKDATE_S
    for name, text in files.items():
        path = directory / name
        path.write_text(text, encoding="utf-8")
        os.utime(path, (backdated, backdated))
    print(f"setup {directory} -> {version} ({len(files)} files, mtime backdated)")


def serve(directory: Path, port: int) -> None:
    """Serve the REAL app factory against `directory`.

    Pointing server.main._WEBCHAT_DIR at the temp directory before create_app() keeps the
    thing under test the production wiring (mount + index route) rather than a lookalike
    stub. Lifespan is off so no RAG engine is built for a static-file test.
    """
    import uvicorn

    from server import main as server_main

    server_main._WEBCHAT_DIR = directory
    uvicorn.run(server_main.create_app(), host="127.0.0.1", port=port, lifespan="off")


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    command, directory = argv[1], Path(argv[2])
    if command == "setup":
        setup(directory, argv[3] if len(argv) > 3 else "V1")
        return 0
    if command == "serve":
        serve(directory, int(argv[3]) if len(argv) > 3 else 8011)
        return 0
    print(f"unknown command: {command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
