FROM python:3.8-slim AS base

ENV PIP_NO_CACHE_DIR=off
RUN pip install pipenv

WORKDIR /app
COPY Pipfile* ./

RUN pipenv install --system --deploy


FROM base AS deploy

RUN pip install gunicorn

COPY . ./

EXPOSE 8000

ENTRYPOINT ["/app/docker-entrypoint.sh"]