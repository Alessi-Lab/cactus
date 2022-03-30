#!/bin/bash
if [ "${NETPHOS}" = "1" ]; then
    uncompress /app/netphos/netphos-3.1.Linux.tar.Z;
    tar -xvf /app/netphos/netphos-3.1.Linux.tar;
    rm /app/netphos/ape-1.0;
    mv /app/cactus/ape.docker /app/netphos/ape-1.0/ape
fi

service nginx restart
nginx -g "daemon off;"
supervisord -n -c /app/cactus/super.docker.conf