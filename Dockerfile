FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get -y update
RUN apt-get -y upgrade


RUN apt-get -y install git


RUN git clone https://github.com/noatgnu/cactus.git
WORKDIR /app/cactus
RUN pip3 install -r requirements.txt
RUN apt-get -y install supervisor
RUN service supervisor stop
RUN service supervisor start
RUN supervisord -c /app/cactus/super.docker.conf

RUN alembic downgrade base
RUN alembic upgrade head

RUN ps aux | grep supervisor
RUN supervisorctl status

RUN supervisorctl restart cactus:*