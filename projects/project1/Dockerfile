FROM python:3.6.5-alpine3.7

# necessario para imprimir na console os logs da aplicação (do Django por ex)
ENV PYTHONUNBUFFERED 1

# Setup
RUN apk update && \
	apk upgrade && \
	apk add --update bash-completion postgresql-client postgresql-dev build-base gettext && \
	pip install --upgrade pip

RUN mkdir -p /usr/src/app
ADD requirements.txt /usr/src/app

WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

# Clean
RUN apk del -r postgresql
