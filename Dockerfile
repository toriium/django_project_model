FROM python:3.12-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .

# Collect static files
RUN uv run python manage.py collectstatic --noinput

# Run the application
CMD ["uv", "run", "gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
