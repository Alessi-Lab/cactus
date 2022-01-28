FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app


RUN apt-get -y update
RUN apt-get -y upgrade


RUN apt-get -y install git
RUN apt-get -y install nginx

RUN git clone https://github.com/noatgnu/cactus.git
WORKDIR /app/cactus
RUN pip3 install -r requirements.txt
RUN alembic downgrade base
RUN alembic upgrade head
RUN apt-get -y install supervisor
RUN service supervisor stop

CMD ["supervisord", "-c", "/app/cactus/super.docker.conf"]
CMD ["nginx", "-c", "/app/cactus/nginx.conf"]
RUN service nginx restart
EXPOSE 8001
EXPOSE 8002
EXPOSE 80
