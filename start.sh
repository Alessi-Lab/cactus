#!/bin/bash
sed -i '18s/file_config/#file_config/g' /app/cactus/cactus/handlers.py
sed -i '19s/#config_file_docker/file_config/g' /app/cactus/cactus/handlers.py
if [ "${NETPHOS}" = "1" ]; then
    cd /app/netphos;
    uncompress /app/netphos/netphos-3.1.Linux.tar.Z;
    tar -xvf /app/netphos/netphos-3.1.Linux.tar;
    rm /app/netphos/ape-1.0/ape;
    mv /app/cactus/ape.docker /app/netphos/ape-1.0/ape
    chmod 777 /app/netphos/ape-1.0/ape
fi
export NETPHOS="0"
service nginx restart
nginx -g "daemon off;"
supervisord -n -c /app/cactus/super.docker.conf