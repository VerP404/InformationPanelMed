FROM python:3.11-slim

RUN mkdir code
WORKDIR code

ADD requirements.txt /code/
RUN pip install -r requirements.txt


ADD . /code/
ADD .env.docker /code/.env

ENV APP_NAME=INFORMATIONPANELMED


CMD gunicorn InformationPanelMed.wsgi:application -b 0.0.0.0:8000
