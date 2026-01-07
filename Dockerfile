FROM python:3.14.2-alpine3.23

RUN apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers

ENV POETRY_VERSION=1.7.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

RUN pip install --no-cache-dir poetry==$POETRY_VERSION

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-interaction --no-ansi

COPY logs/ logs/
COPY src/ src/

ENTRYPOINT ["poetry", "run", "python", "-m", "src.main", "logs/access.log"]
