FROM python:3.6.5-alpine3.7

# necessario para imprimir na console os logs da aplicação (do Django por ex)
ENV PYTHONUNBUFFERED 1

# Initialize
RUN mkdir -p /data/web
COPY requirements.txt /data/web/

# Setup
WORKDIR /data/web
RUN apk update && \
	apk upgrade && \
	apk add --update bash-completion postgresql-client postgresql-dev build-base gettext && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

# Clean
RUN apk del -r postgresql

# Prepare
COPY . /data/web/
RUN mkdir -p mydjango/static/admin
