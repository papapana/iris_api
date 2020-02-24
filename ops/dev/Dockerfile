FROM python:3.8.1-alpine

ENV PYTHONBUFFERED 1
ENV HOME /iris_api

RUN addgroup -S iris_api && adduser -S iris_api -G iris_api
RUN mkdir -p /iris_api

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && rm -rf /root/.cache/pip

WORKDIR /iris_api

EXPOSE 8000

COPY . /iris_api

RUN pip install -e /iris_api
RUN pip install ipython