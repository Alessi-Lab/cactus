#!/bin/bash
if [[ -z "${NETPHOS}" ]]; then
  echo "${NETPHOS}"
  if [ "${NETPHOS}" = "1" ]; then
      cd /app/netphos/ &&
      uncompress /app/netphos/netphos-3.1.Linux.tar.Z &&
      tar -xvf /app/netphos/netphos-3.1.Linux.tar;
  fi
fi

service nginx restart
nginx -g "daemon off;"
supervisord -n -c /app/cactus/super.docker.conf