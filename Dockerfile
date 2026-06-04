FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# System deps: pandas_ta may need build tools for native deps on slim base.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./
RUN pip install --upgrade pip \
    && pip install \
        "streamlit>=1.32.0" \
        "plotly>=5.18.0" \
        "pandas_ta>=0.3.14b0" \
        "requests>=2.31.0" \
        "pyyaml>=6.0"

COPY app.py ./
COPY pages ./pages
COPY openbb_client ./openbb_client
COPY components ./components

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl --fail --silent http://localhost:8501/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "app.py", \
            "--server.address=0.0.0.0", \
            "--server.port=8501", \
            "--server.headless=true", \
            "--browser.gatherUsageStats=false"]
