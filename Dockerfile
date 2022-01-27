FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get -y install git
RUN apt-get -y install 
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN git clone https://github.com/noatgnu/cactus.git

WORKDIR /app/cactus
RUN $HOME/.poetry/bin/poetry --version
RUN $HOME/.poetry/bin/poetry install
RUN $HOME/.poetry/bin/poetry run alembic downgrade base
RUN $HOME/.poetry/bin/poetry run alembic upgrade head
