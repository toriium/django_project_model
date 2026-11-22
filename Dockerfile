# ---- build stage: installs dependencies and collects static files ----
FROM python:3.12-slim AS builder

RUN pip install --no-cache-dir uv

WORKDIR /app

# Install dependencies first (cached layer while lock files don't change)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project


COPY . .
RUN DOCKER_BUILD=1 .venv/bin/python manage.py collectstatic --noinput

# ---- runtime stage: only the ready-to-run app, no build tools ----
FROM python:3.12-slim

# Non-root user that only runs the app (home is needed for gunicorn's control socket)
RUN useradd --create-home --shell /usr/sbin/nologin appuser

WORKDIR /app

# Files stay owned by root, so appuser can read/execute but not modify them
COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:$PATH" PYTHONUNBUFFERED=1

USER appuser

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
