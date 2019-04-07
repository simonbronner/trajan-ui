FROM python:latest

MAINTAINER "Simon Bronner" <simon@bronner.network>

WORKDIR /app

RUN pip install Django

EXPOSE 8000

ADD run.sh /run.sh
ADD manage.py /app/
ADD django_poll /app/django_poll
ADD trajan /app/trajan
ADD requirements.txt /app/
ADD prod.settings.py /app/django_poll/settings.py

CMD ["/run.sh"]
