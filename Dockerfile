FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-install-project

COPY app.py ./

FROM python:3.13-slim

RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/app.py ./

RUN chown -R appuser:appuser /app

USER appuser

ENV PYTHONUNBUFFERED=1

CMD ["/app/.venv/bin/python", "app.py"]
