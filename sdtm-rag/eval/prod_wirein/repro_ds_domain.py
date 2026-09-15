import os, sys, collections
sys.path.insert(0, os.getcwd())
from fastapi.testclient import TestClient
import server.main as m
app = getattr(m, "app", None) or m.create_app()
QS = [
 "本研究中，哪些数据适合进入 SDTM 的 DS 域？",
 "从 PRT（手順書）的要求出发，本研究有哪些数据应该映射到 SDTM DS（Disposition）域？请列出源字段。",
 "本研究のDSドメインに入るべきデータは何ですか",
]
with TestClient(app) as c:
    fed = app.state.federation
    for q in QS:
        chunks, routed = fed.retrieve(q, corpus="both")
        print("\n###", q, "| routed:", routed, "| n:", len(chunks))
        forms = collections.Counter()
        for ch in chunks:
            md = {"source": ch.source, "section": ch.section, "form_oid": None}
            src = os.path.basename(str(ch.source))
            sec = (str(ch.section or ""))[:45] + ("  via_lookup" if ch.via_lookup else "")
            print(f"  [{ch.corpus}] {src} | {sec}")
            if ch.corpus == "study": forms[src.split("__")[1] if "__" in src else src] += 1
        print("  study forms:", dict(forms))
