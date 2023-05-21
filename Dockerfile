# syntax=docker/dockerfile:1
FROM python:3.11

WORKDIR ./app
COPY . .
RUN chmod 775 script.sh

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r requirements.txt
