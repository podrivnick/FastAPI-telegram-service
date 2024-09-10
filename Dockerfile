FROM python:3.12.1-slim-bullseye as builder

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.8.2 && \
    poetry export -o requirements.txt --without-hashes

FROM python:3.12.1-slim-bullseye as dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY --from=builder requirements.txt /app

RUN apt-get update -y && \
        apt-get install -y --no-install-recommends python3-dev \
        gcc \
        musl-dev && \
        pip install --no-cache-dir --upgrade pip==24.0 && pip install --no-cache-dir -r requirements.txt \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY /app/ /app/**

EXPOSE 8000
