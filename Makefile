build:
	docker-compose build

up:
	docker-compose up -d

up-non-daemon:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && \
	docker-compose start

shell-web:
	docker exec -ti tati-service-app bash

shell-db:
	docker exec -ti tati-service-database bash

log-web:
	docker-compose logs -f web

log-db:
	docker-compose logs -f db

migrate:
	docker-compose exec web /usr/src/app/src/manage.py makemigrations && \
	docker-compose exec web /usr/src/app/src/manage.py migrate
