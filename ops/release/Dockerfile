FROM python:3.8-slim-bullseye

LABEL MAINTAINER="Vassilis Papapanagiotou <bpapapana@gmail.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000

ENV PYTHONBUFFERED 1
ENV HOME /iris_api

RUN groupadd -r iris_api && useradd -r -g iris_api iris_api
RUN mkdir -p /iris_api

WORKDIR /iris_api

EXPOSE 8000

COPY . /iris_api

RUN pip install -e /iris_api

RUN chown -R iris_api:iris_api .
USER iris_api
ENTRYPOINT []