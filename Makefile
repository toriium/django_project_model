up:
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f
local:
	python manage.py runserver