# syntax=docker.io/docker/dockerfile-upstream:1.2.0
# =========================================================
# === Build Backend Base                                ===
# =========================================================
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.9

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles

WORKDIR $APP_HOME

LABEL maintainer='api.imperfect@gmail.com'
LABEL youtube="https://www.youtube.com/c/APIImperfect"
LABEL description="Development image for Real Estate Project"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # opencv dependencies
  ffmpeg libsm6 libxext6 \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

RUN pip3 install poetry
ENV POETRY_VIRTUALENVS_CREATE=false

# Allow user to manage deps in dev container
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN poetry export -f requirements.txt -o requirements.txt --without-hashes
RUN --mount=type=cache,target=/root/.cache/pip \
  pip install -r ./requirements.txt


COPY ./docker/local/django/entrypoint /entrypoint
# Fix newline format from windows to unix system
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower


ENTRYPOINT [ "/entrypoint"]
