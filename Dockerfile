# Dockerfile
FROM python:3.10

ENV DJANGO_SETTINGS_MODULE=SilthsSanctuary.settings.local

WORKDIR /app
COPY . SilthsSanctuary
COPY manage.py requirements.txt /app/

RUN mkdir logs

# install psycopg2 dependencies
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

RUN pip install -r requirements.txt
RUN pip install gunicorn

WORKDIR /app
COPY ./gunicorn.sh /

ENTRYPOINT ["/gunicorn.sh"]