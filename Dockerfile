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
RUN service nginx stop
COPY nginx.docker.conf /etc/nginx/tornado.conf
RUN pip3 install -r requirements.txt
RUN alembic downgrade base
RUN alembic upgrade head
RUN apt-get -y install supervisor
RUN service supervisor stop
RUN mkdir /app/nginx
RUN touch /app/nginx/error.log
RUN touch /app/nginx/access.log
CMD ["supervisord", "-c", "/app/cactus/super.docker.conf"]
CMD ["nginx", "-c", "/etc/nginx/nginx.conf"]
EXPOSE 8000
EXPOSE 8001
EXPOSE 80
CMD ["bash"]