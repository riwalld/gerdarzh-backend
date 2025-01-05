FROM python:3.12-alpine as build

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.8.3

RUN apk update && apk add --no-cache \
  gcc \
  gettext \
  libmagic \
  make \
  musl-dev \
  mariadb-connector-c-dev \
  pkgconfig \
  python3-dev \
  py3-setuptools

RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /app
RUN chown -R ${UID:-33}:${GID:-33} /app
COPY --chown=${UID:-33}:${GID:-33} poetry.lock pyproject.toml /app/


# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install $(test "$USE_ENV" == prod && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY --chown=${UID:-33}:${GID:-33} . /app

# Prod
FROM build as prod
COPY --chown=${UID:-33}:${GID:-33} ./start-prod-server.sh /usr/local/bin/start-prod-server.sh
USER ${UID:-33}
RUN chmod +x /usr/local/bin/start-prod-server.sh
CMD ["start-prod-server.sh"]
