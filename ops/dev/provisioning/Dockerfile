FROM python:3.8-slim-buster

LABEL MAINTAINER="Vassilis Papapanagiotou <bpapapana@gmail.com>"

RUN pip install pandas==1.0.1 pymongo==3.9.0

ADD scripts/provision_db.py /provision_db.py
