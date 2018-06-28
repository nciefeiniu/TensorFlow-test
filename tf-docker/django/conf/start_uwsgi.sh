#!/bin/bash

nohup /etc/init.d/nginx start &
nohup uwsgi --ini django_uwsgi.ini &
