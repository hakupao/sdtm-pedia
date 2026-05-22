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

# Install package
COPY pyproject.toml ./
RUN pip install --upgrade pip setuptools wheel
# Install with editable mode disabled in image; source mounted via compose volume in dev
RUN pip install . || (pip install .[fallback] && echo "WARN: pyreadstat fallback to sas7bdat applied")

COPY . /app

# data/ is a mounted volume (chroma persist + uploaded datasets)
VOLUME ["/app/data"]

EXPOSE 8000 8501

# Default cmd: run FastAPI; override in compose for Streamlit UI service
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
