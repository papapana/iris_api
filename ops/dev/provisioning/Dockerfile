FROM python:3.8-slim-buster

LABEL MAINTAINER="Vassilis Papapanagiotou <bpapapana@gmail.com>"

# install dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean

RUN pip install pandas==1.0.1 pymongo==3.9.0

ADD scripts/provision_db.py /provision_db.py

COPY scripts/wait_for_mongo.sh /wait_for_mongo.sh

RUN chmod 700 /wait_for_mongo.sh

