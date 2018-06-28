
FROM ubuntu:16.04

ADD ./sources.list /etc/apt/sources.list

RUN apt update \
    && apt install -y nginx

#ADD ./mime.types /etc/nginx/conf/mime.types
COPY ./nginx.conf /etc/nginx/nginx.conf

RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

WORKDIR /etc/nginx
