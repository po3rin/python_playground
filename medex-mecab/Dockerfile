FROM python:3.7.8-slim-buster

RUN apt-get update && \
    # https://github.com/grpc/grpc/issues/22581#issuecomment-608644271
    apt-get install -y build-essential git && \
    pip install --upgrade pip setuptools && \ 
    pip install poetry unidic-lite

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi \
    && touch /usr/local/etc/mecabrc 

COPY dnorm.py sample.txt /app/
