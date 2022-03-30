#!/bin/bash
if [ "${NETPHOS}" = "1" ]; then
    cd /app/netphos;
    uncompress /app/netphos/netphos-3.1.Linux.tar.Z;
    tar -xvf /app/netphos/netphos-3.1.Linux.tar;
    rm /app/netphos/ape-1.0/ape;
    mv /app/cactus/ape.docker /app/netphos/ape-1.0/ape
fi
export NETPHOS="0"
service nginx restart
nginx -g "daemon off;"
supervisord -n -c /app/cactus/super.docker.conf