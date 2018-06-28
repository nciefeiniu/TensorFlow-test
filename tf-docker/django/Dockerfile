FROM tensorflow/tensorflow:1.8.0-py3

ADD ./conf/sources.list /etc/apt/sources.list
ADD ./conf/pip.conf /root/.pip/pip.conf
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y python3-pip \
    && apt install -y nginx \
    && echo "\ndaemon off;" >> /etc/nginx/nginx.conf \
    && pip3 install --upgrade pip \
    && pip3 install django==1.11 \
    && pip3 install uwsgi

COPY ./webapp/ /home/translation_web/
WORKDIR /home/translation_web/
RUN ls
RUN python3 manage.py collectstatic

#ADD ./conf/mime.types /etc/nginx/conf/mime.types
COPY ./conf/django.conf /etc/nginx/sites-enabled/django.conf
RUN cat /etc/nginx/sites-enabled/django.conf
#RUN service nginx restart

ADD ./conf/django_uwsgi.ini /home/
ADD ./conf/start_uwsgi.sh /home/

WORKDIR /home/
#RUN nohup uwsgi --ini django_uwsgi.ini &
RUN chmod +x start_uwsgi.sh

