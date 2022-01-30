#!/bin/bash

service nginx restart
nginx -g "daemon off" &
supervisord -n -c /app/cactus/super.docker.conf