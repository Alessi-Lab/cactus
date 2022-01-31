#!/bin/bash

service nginx stop
nginx -g "daemon off;"
service nginx start
supervisord -n -c /app/cactus/super.docker.conf