#!/bin/bash
IP=$(getent hosts cli.au.team | awk '{print $1}')
IP=${IP:-20.20.20.151}

if [ "$1" = "--host" ]; then
  echo '{}'
else
  cat << EOF
{
  "clients": { "hosts": ["cli"] },
  "_meta": { "hostvars": { "cli": { "ansible_host": "$IP" } } }
}
EOF
fi
