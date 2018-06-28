FROM tensorflow/tensorflow:1.8.0-py3

ADD ./conf/sources.list /etc/apt/sources.list
ADD ./conf/pip.conf ~/.pip/pip.conf
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y python3-pip \
    && apt install -y nginx \
    && apt update -y \
    && pip3 install --upgrade pip \
    && pip3 install django==1.11 \
    && pip3 install uwsgi

COPY ./webapp/ /home/translation_web/
WORKDIR /home/translation_web/
RUN ls
RUN python3 manage.py collectstatic

ADD ./conf/django.conf /etc/nginx/sites-enabled/django.conf
ADD ./conf/django_uwsgi.ini /home/

WORKDIR /home/
RUN uwsgi --ini django_uwsgi.ini	

CMD ["service", "nginx", "restart"]
