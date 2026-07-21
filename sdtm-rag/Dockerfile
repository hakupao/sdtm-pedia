# sdtm-rag Phase 1 base image
# Python 3.11 (avoids Apple Silicon Py 3.13 pyreadstat build issues per R-20)
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# System deps: pyreadstat needs gcc + libxml2 for build; tiktoken pulls rustc on some platforms
RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc g++ libxml2-dev libssl-dev curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install package. Copy pyproject + the declared source packages BEFORE `pip install .`
# (setuptools needs the package dirs present to build the wheel — installing with only
# pyproject.toml present fails). data/ and knowledge_base/ are NOT copied: they are bind
# volumes at runtime (see docker-compose.yml), keeping the image lean.
COPY pyproject.toml README.md ./
COPY server ./server
COPY scripts ./scripts
COPY ui ./ui
COPY eval ./eval
RUN pip install --upgrade pip setuptools wheel \
    && (pip install . \
        || (pip install '.[fallback]' && echo "WARN: pyreadstat fallback to sas7bdat applied"))

# data/ is a mounted volume (chroma persist + uploaded datasets)
VOLUME ["/app/data"]

EXPOSE 8000 8501

# Default cmd: run FastAPI; override in compose for Streamlit UI service
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
