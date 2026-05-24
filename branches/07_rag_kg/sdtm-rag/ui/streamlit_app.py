"""Streamlit chat UI for SDTM RAG Q&A (Phase 1B.4).

Run (after starting FastAPI server):
  streamlit run ui/streamlit_app.py
"""
from __future__ import annotations

import os

import requests
import streamlit as st

API_URL = os.getenv("SDTM_RAG_API_URL", "http://localhost:8000")

st.set_page_config(page_title="SDTM Knowledge Base Q&A", layout="wide")
st.title("SDTM Knowledge Base Q&A")

# ── Sidebar ──────────────────────────────────────────────────────────────

with st.sidebar:
    st.header("Settings")
    model = st.selectbox(
        "Model",
        ["default", "hard", "light"],
        index=0,
        help="default=Sonnet, hard=Opus, light=Haiku",
    )
    top_k = st.slider("Retrieval Top-K", 5, 30, 15)
    domain_filter = st.text_input("Domain filter (e.g. AE, DM)", "")
    file_type_filter = st.selectbox(
        "File type filter",
        [
            "(all)",
            "spec",
            "assumptions",
            "examples",
            "chapter",
            "model",
            "terminology",
            "variable_index",
        ],
    )

    st.divider()
    if st.button("Check API"):
        try:
            r = requests.get(f"{API_URL}/api/health", timeout=5)
            st.success(f"API OK: {r.json()}")
            r2 = requests.get(f"{API_URL}/api/info", timeout=5)
            info = r2.json()
            st.info(
                f"Collection: {info['collection_name']}  \n"
                f"Chunks: {info['chunk_count']}  \n"
                f"Model: {info['default_model']}"
            )
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect. Start server first.")
        except Exception as e:
            st.error(f"Error: {e}")

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.session_state.history = []
        st.rerun()

# ── Chat state ───────────────────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []
if "history" not in st.session_state:
    st.session_state.history = []

# ── Helpers ───────────────────────────────────────────────────────────────


def _render_sources(sources: list[dict]) -> None:
    with st.expander(f"Sources ({len(sources)})"):
        for s in sources:
            label = f"**{s['source']}**"
            if s.get("section"):
                label += f" -- {s['section']}"
            label += f"  (sim: {s['similarity']:.3f})"
            st.markdown(label)
            st.text(s["text_preview"])
            st.divider()


# ── Display chat history ─────────────────────────────────────────────────

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            _render_sources(msg["sources"])


# ── Chat input ───────────────────────────────────────────────────────────

if prompt := st.chat_input("Ask about SDTM..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Retrieving and generating..."):
            payload: dict = {
                "question": prompt,
                "model": model,
                "top_k": top_k,
                "history": st.session_state.history[-10:],
            }
            if domain_filter.strip():
                payload["domain"] = domain_filter.strip().upper()
            if file_type_filter != "(all)":
                payload["file_type"] = file_type_filter

            try:
                r = requests.post(
                    f"{API_URL}/api/ask", json=payload, timeout=120
                )
                r.raise_for_status()
                data = r.json()

                answer = data["answer"]
                st.markdown(answer)

                sources = data.get("sources", [])
                if sources:
                    _render_sources(sources)

                if data.get("usage"):
                    st.caption(
                        f"Model: {data['model_used']} | "
                        f"Tokens: {data['usage']['total_tokens']}"
                    )

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer, "sources": sources}
                )
                st.session_state.history.append(
                    {"role": "user", "content": prompt}
                )
                st.session_state.history.append(
                    {"role": "assistant", "content": answer}
                )

            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to API server. "
                    "Start it first: `uvicorn server.main:app`"
                )
            except requests.exceptions.HTTPError as e:
                st.error(
                    f"API error {e.response.status_code}: "
                    f"{e.response.text[:500]}"
                )
            except Exception as e:
                st.error(f"Unexpected error: {e}")
