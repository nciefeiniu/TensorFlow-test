#!/bin/bash

nohup sudo docker-compose up -d --build proxy &

nohup sudo exec -it server1 service nginx start &

