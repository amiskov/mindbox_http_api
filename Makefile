# Local Development
run:
	export POSTGRES_DB=mindbox_categories; \
	export POSTGRES_USER=andreymiskov; \
	export POSTGRES_PASSWORD=; \
	export POSTGRES_HOST=localhost; \
	export POSTGRES_PORT=5432; \
	python src/main.py

# Docker
up:
	docker compose up
down:
	docker compose down -v
