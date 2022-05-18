FROM python:3.8.5-alpine

WORKDIR /srv/code

#default enviroment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

RUN apk upgrade --available && apk add gcc python3-dev musl-dev

COPY requirements.txt .
RUN pip install -r requirements.txt
