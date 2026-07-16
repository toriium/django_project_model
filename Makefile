up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f
local:
	uv run python manage.py runserver

format:
	djlint . --reformat && ruff format && ruff check --fix